#  NLP written by GAMS Convert at 04/21/18 13:51:47
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         31       31        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         43       43        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        141       11      130        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0.285,0.315),initialize=0.29015241396)
m.x2 = Var(within=Reals,bounds=(0.546,0.636),initialize=0.62189400372)
m.x3 = Var(within=Reals,bounds=(0.999071638557945,1.00092836144205),initialize=1.00009353307628)
m.x4 = Var(within=Reals,bounds=(481.55,486.05),initialize=482.905120568)
m.x5 = Var(within=Reals,bounds=(0.385,0.415),initialize=0.39376636351)
m.x6 = Var(within=Reals,bounds=(0.557,0.647),initialize=0.57716475803)
m.x7 = Var(within=Reals,bounds=(0.999071638557945,1.00092836144205),initialize=0.999721176860282)
m.x8 = Var(within=Reals,bounds=(490.95,495.45),initialize=494.8032165615)
m.x9 = Var(within=Reals,bounds=(0.485,0.515),initialize=0.48701341169)
m.x10 = Var(within=Reals,bounds=(0.567,0.657),initialize=0.61201896021)
m.x11 = Var(within=Reals,bounds=(0.999071638557945,1.00092836144205),initialize=1.00092486639703)
m.x12 = Var(within=Reals,bounds=(497.65,502.15),initialize=500.254300201)
m.x13 = Var(within=Reals,bounds=(0.685,0.715),initialize=0.71473399117)
m.x14 = Var(within=Reals,bounds=(0.612,0.702),initialize=0.68060254203)
m.x15 = Var(within=Reals,bounds=(0.999071638557945,1.00092836144205),initialize=0.999314298281912)
m.x16 = Var(within=Reals,bounds=(499.15,503.65),initialize=502.0287344155)
m.x17 = Var(within=Reals,bounds=(0.885,0.915),initialize=0.88978553592)
m.x18 = Var(within=Reals,bounds=(0.769,0.859),initialize=0.79150724797)
m.x19 = Var(within=Reals,bounds=(0.999071638557945,1.00092836144205),initialize=1.00031365361411)
m.x20 = Var(within=Reals,bounds=(467.45,471.95),initialize=469.4091037145)
m.x21 = Var(within=Reals,bounds=(1,2),initialize=1.9)
m.x22 = Var(within=Reals,bounds=(1,2),initialize=1.6)
m.x23 = Var(within=Reals,bounds=(0.1,None),initialize=1)
m.x24 = Var(within=Reals,bounds=(0.1,None),initialize=1)
m.x25 = Var(within=Reals,bounds=(0.1,None),initialize=1)
m.x26 = Var(within=Reals,bounds=(0.1,None),initialize=1)
m.x27 = Var(within=Reals,bounds=(0.1,None),initialize=1)
m.x28 = Var(within=Reals,bounds=(0.1,None),initialize=1)
m.x29 = Var(within=Reals,bounds=(0.1,None),initialize=1)
m.x30 = Var(within=Reals,bounds=(0.1,None),initialize=1)
m.x31 = Var(within=Reals,bounds=(0.1,None),initialize=1)
m.x32 = Var(within=Reals,bounds=(0.1,None),initialize=1)
m.x33 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x34 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x35 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x36 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x37 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x38 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x39 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x40 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x41 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x42 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=(-60 + 200*m.x1)**2 + (-39.4 + 66.6666666666667*m.x2)**2 + (-3231.5 + 3231.5*m.x3)**2 + (-
                       645.066666666667 + 1.33333333333333*m.x4)**2 + (-80 + 200*m.x5)**2 + (-40.1333333333333 + 
                       66.6666666666667*m.x6)**2 + (-3231.5 + 3231.5*m.x7)**2 + (-657.6 + 1.33333333333333*m.x8)**2 + (-
                       100 + 200*m.x9)**2 + (-40.8 + 66.6666666666667*m.x10)**2 + (-3231.5 + 3231.5*m.x11)**2 + (-
                       666.533333333333 + 1.33333333333333*m.x12)**2 + (-140 + 200*m.x13)**2 + (-43.8 + 66.6666666666667
                       *m.x14)**2 + (-3231.5 + 3231.5*m.x15)**2 + (-668.533333333333 + 1.33333333333333*m.x16)**2 + (-
                       180 + 200*m.x17)**2 + (-54.2666666666667 + 66.6666666666667*m.x18)**2 + (-3231.5 + 3231.5*m.x19)
                       **2 + (-626.266666666667 + 1.33333333333333*m.x20)**2, sense=minimize)

m.c2 = Constraint(expr=exp(18.5875 - 3626.55/(-34.29 + 323.15*m.x3)) - m.x33 == 0)

m.c3 = Constraint(expr=exp(16.1764 - 2927.17/(-50.22 + 323.15*m.x3)) - m.x34 == 0)

m.c4 = Constraint(expr=exp(18.5875 - 3626.55/(-34.29 + 323.15*m.x7)) - m.x35 == 0)

m.c5 = Constraint(expr=exp(16.1764 - 2927.17/(-50.22 + 323.15*m.x7)) - m.x36 == 0)

m.c6 = Constraint(expr=exp(18.5875 - 3626.55/(-34.29 + 323.15*m.x11)) - m.x37 == 0)

m.c7 = Constraint(expr=exp(16.1764 - 2927.17/(-50.22 + 323.15*m.x11)) - m.x38 == 0)

m.c8 = Constraint(expr=exp(18.5875 - 3626.55/(-34.29 + 323.15*m.x15)) - m.x39 == 0)

m.c9 = Constraint(expr=exp(16.1764 - 2927.17/(-50.22 + 323.15*m.x15)) - m.x40 == 0)

m.c10 = Constraint(expr=exp(18.5875 - 3626.55/(-34.29 + 323.15*m.x19)) - m.x41 == 0)

m.c11 = Constraint(expr=exp(16.1764 - 2927.17/(-50.22 + 323.15*m.x19)) - m.x42 == 0)

m.c12 = Constraint(expr=m.x23*m.x1*m.x33 - m.x2*m.x4 == 0)

m.c13 = Constraint(expr=m.x25*m.x5*m.x35 - m.x6*m.x8 == 0)

m.c14 = Constraint(expr=m.x27*m.x9*m.x37 - m.x10*m.x12 == 0)

m.c15 = Constraint(expr=m.x29*m.x13*m.x39 - m.x14*m.x16 == 0)

m.c16 = Constraint(expr=m.x31*m.x17*m.x41 - m.x18*m.x20 == 0)

m.c17 = Constraint(expr=m.x24*(1 - m.x1)*m.x34 - (1 - m.x2)*m.x4 == 0)

m.c18 = Constraint(expr=m.x26*(1 - m.x5)*m.x36 - (1 - m.x6)*m.x8 == 0)

m.c19 = Constraint(expr=m.x28*(1 - m.x9)*m.x38 - (1 - m.x10)*m.x12 == 0)

m.c20 = Constraint(expr=m.x30*(1 - m.x13)*m.x40 - (1 - m.x14)*m.x16 == 0)

m.c21 = Constraint(expr=m.x32*(1 - m.x17)*m.x42 - (1 - m.x18)*m.x20 == 0)

m.c22 = Constraint(expr=m.x21/m.x3/(1 + m.x21/m.x22*m.x1/(1 - m.x1))**2 - log(m.x23) == 0)

m.c23 = Constraint(expr=m.x21/m.x7/(1 + m.x21/m.x22*m.x5/(1 - m.x5))**2 - log(m.x25) == 0)

m.c24 = Constraint(expr=m.x21/m.x11/(1 + m.x21/m.x22*m.x9/(1 - m.x9))**2 - log(m.x27) == 0)

m.c25 = Constraint(expr=m.x21/m.x15/(1 + m.x21/m.x22*m.x13/(1 - m.x13))**2 - log(m.x29) == 0)

m.c26 = Constraint(expr=m.x21/m.x19/(1 + m.x21/m.x22*m.x17/(1 - m.x17))**2 - log(m.x31) == 0)

m.c27 = Constraint(expr=m.x22/m.x3/(1 + m.x22/m.x21*(1 - m.x1)/m.x1)**2 - log(m.x24) == 0)

m.c28 = Constraint(expr=m.x22/m.x7/(1 + m.x22/m.x21*(1 - m.x5)/m.x5)**2 - log(m.x26) == 0)

m.c29 = Constraint(expr=m.x22/m.x11/(1 + m.x22/m.x21*(1 - m.x9)/m.x9)**2 - log(m.x28) == 0)

m.c30 = Constraint(expr=m.x22/m.x15/(1 + m.x22/m.x21*(1 - m.x13)/m.x13)**2 - log(m.x30) == 0)

m.c31 = Constraint(expr=m.x22/m.x19/(1 + m.x22/m.x21*(1 - m.x17)/m.x17)**2 - log(m.x32) == 0)
