#  NLP written by GAMS Convert at 04/21/18 13:50:54
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         15       15        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         31       31        0        0        0        0        0        0
#  FX      2        2        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        101       71       30        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(387.9,387.9),initialize=387.9)
m.x2 = Var(within=Reals,bounds=(None,None),initialize=387.9)
m.x3 = Var(within=Reals,bounds=(None,None),initialize=387.9)
m.x4 = Var(within=Reals,bounds=(None,None),initialize=387.9)
m.x5 = Var(within=Reals,bounds=(None,None),initialize=387.9)
m.x6 = Var(within=Reals,bounds=(None,None),initialize=387.9)
m.x7 = Var(within=Reals,bounds=(None,None),initialize=387.9)
m.x8 = Var(within=Reals,bounds=(None,None),initialize=387.9)
m.x9 = Var(within=Reals,bounds=(85.3,85.3),initialize=85.3)
m.x10 = Var(within=Reals,bounds=(None,None),initialize=85.3)
m.x11 = Var(within=Reals,bounds=(None,None),initialize=85.3)
m.x12 = Var(within=Reals,bounds=(None,None),initialize=85.3)
m.x13 = Var(within=Reals,bounds=(None,None),initialize=85.3)
m.x14 = Var(within=Reals,bounds=(None,None),initialize=85.3)
m.x15 = Var(within=Reals,bounds=(None,None),initialize=85.3)
m.x16 = Var(within=Reals,bounds=(None,None),initialize=85.3)
m.x17 = Var(within=Reals,bounds=(None,None),initialize=110.5)
m.x18 = Var(within=Reals,bounds=(None,None),initialize=110.5)
m.x19 = Var(within=Reals,bounds=(None,None),initialize=110.5)
m.x20 = Var(within=Reals,bounds=(None,None),initialize=110.5)
m.x21 = Var(within=Reals,bounds=(None,None),initialize=110.5)
m.x22 = Var(within=Reals,bounds=(None,None),initialize=110.5)
m.x23 = Var(within=Reals,bounds=(None,None),initialize=110.5)
m.x24 = Var(within=Reals,bounds=(None,None),initialize=147.1)
m.x25 = Var(within=Reals,bounds=(None,None),initialize=147.1)
m.x26 = Var(within=Reals,bounds=(None,None),initialize=147.1)
m.x27 = Var(within=Reals,bounds=(None,None),initialize=147.1)
m.x28 = Var(within=Reals,bounds=(None,None),initialize=147.1)
m.x29 = Var(within=Reals,bounds=(None,None),initialize=147.1)
m.x30 = Var(within=Reals,bounds=(None,None),initialize=147.1)

m.obj = Objective(expr=0.5*((-24.24375 + 0.0625*m.x1)*(-387.9 + m.x1) + (-85.3 + m.x9)*(-85.3 + m.x9) + (-24.425578125
                        + 0.0625*m.x2)*(-390.80925 + m.x2) + (-85.93975 + m.x10)*(-85.93975 + m.x10) + (-
                       24.6087699609375 + 0.0625*m.x3)*(-393.740319375 + m.x3) + (-86.584298125 + m.x11)*(-86.584298125
                        + m.x11) + (-24.7933357356445 + 0.0625*m.x4)*(-396.693371770313 + m.x4) + (-87.2336803609375 + 
                       m.x12)*(-87.2336803609375 + m.x12) + (-24.9792857536619 + 0.0625*m.x5)*(-399.66857205859 + m.x5)
                        + (-87.8879329636445 + m.x13)*(-87.8879329636445 + m.x13) + (-25.1666303968143 + 0.0625*m.x6)*(-
                       402.666086349029 + m.x6) + (-88.5470924608719 + m.x14)*(-88.5470924608719 + m.x14) + (-
                       25.3553801247904 + 0.0625*m.x7)*(-405.686081996647 + m.x7) + (-89.2111956543284 + m.x15)*(-
                       89.2111956543284 + m.x15) + (-2554.55454757264 + 6.25*m.x8)*(-408.728727611622 + m.x8) + (-
                       8988.02796217359 + 100*m.x16)*(-89.8802796217359 + m.x16)) + 0.5*((-110.5 + m.x17)*(-110.5 + 
                       m.x17) + (-65.3124 + 0.444*m.x24)*(-147.1 + m.x24) + (-111.32875 + m.x18)*(-111.32875 + m.x18) + 
                       (-65.802243 + 0.444*m.x25)*(-148.20325 + m.x25) + (-112.163715625 + m.x19)*(-112.163715625 + 
                       m.x19) + (-66.2957598225 + 0.444*m.x26)*(-149.314774375 + m.x26) + (-113.004943492188 + m.x20)*(-
                       113.004943492188 + m.x20) + (-66.7929780211688 + 0.444*m.x27)*(-150.434635182813 + m.x27) + (-
                       113.852480568379 + m.x21)*(-113.852480568379 + m.x21) + (-67.2939253563275 + 0.444*m.x28)*(-
                       151.562894946684 + m.x28) + (-114.706374172642 + m.x22)*(-114.706374172642 + m.x22) + (-
                       67.7986297965 + 0.444*m.x29)*(-152.699616658784 + m.x29) + (-115.566671978937 + m.x23)*(-
                       115.566671978937 + m.x23) + (-68.3071195199738 + 0.444*m.x30)*(-153.844863783725 + m.x30))
                       , sense=minimize)

m.c2 = Constraint(expr= - 0.914*m.x1 + m.x2 + 0.016*m.x9 - 0.305*m.x17 - 0.424*m.x24 == -59.4)

m.c3 = Constraint(expr= - 0.914*m.x2 + m.x3 + 0.016*m.x10 - 0.305*m.x18 - 0.424*m.x25 == -59.4)

m.c4 = Constraint(expr= - 0.914*m.x3 + m.x4 + 0.016*m.x11 - 0.305*m.x19 - 0.424*m.x26 == -59.4)

m.c5 = Constraint(expr= - 0.914*m.x4 + m.x5 + 0.016*m.x12 - 0.305*m.x20 - 0.424*m.x27 == -59.4)

m.c6 = Constraint(expr= - 0.914*m.x5 + m.x6 + 0.016*m.x13 - 0.305*m.x21 - 0.424*m.x28 == -59.4)

m.c7 = Constraint(expr= - 0.914*m.x6 + m.x7 + 0.016*m.x14 - 0.305*m.x22 - 0.424*m.x29 == -59.4)

m.c8 = Constraint(expr= - 0.914*m.x7 + m.x8 + 0.016*m.x15 - 0.305*m.x23 - 0.424*m.x30 == -59.4)

m.c9 = Constraint(expr= - 0.097*m.x1 - 0.424*m.x9 + m.x10 + 0.101*m.x17 - 1.459*m.x24 == -184.7)

m.c10 = Constraint(expr= - 0.097*m.x2 - 0.424*m.x10 + m.x11 + 0.101*m.x18 - 1.459*m.x25 == -184.7)

m.c11 = Constraint(expr= - 0.097*m.x3 - 0.424*m.x11 + m.x12 + 0.101*m.x19 - 1.459*m.x26 == -184.7)

m.c12 = Constraint(expr= - 0.097*m.x4 - 0.424*m.x12 + m.x13 + 0.101*m.x20 - 1.459*m.x27 == -184.7)

m.c13 = Constraint(expr= - 0.097*m.x5 - 0.424*m.x13 + m.x14 + 0.101*m.x21 - 1.459*m.x28 == -184.7)

m.c14 = Constraint(expr= - 0.097*m.x6 - 0.424*m.x14 + m.x15 + 0.101*m.x22 - 1.459*m.x29 == -184.7)

m.c15 = Constraint(expr= - 0.097*m.x7 - 0.424*m.x15 + m.x16 + 0.101*m.x23 - 1.459*m.x30 == -184.7)
