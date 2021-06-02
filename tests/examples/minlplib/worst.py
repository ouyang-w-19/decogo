#  NLP written by GAMS Convert at 04/21/18 13:55:19
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         30       30        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         35       35        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        112       59       53        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x3 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x4 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x5 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x6 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x7 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x8 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x9 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x10 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x11 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x12 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x13 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x14 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x15 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x16 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x17 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x18 = Var(within=Reals,bounds=(0.001,None),initialize=96.1523975231246)
m.x19 = Var(within=Reals,bounds=(0.001,None),initialize=95.8007796007676)
m.x20 = Var(within=Reals,bounds=(0.001,None),initialize=96.1523975231246)
m.x21 = Var(within=Reals,bounds=(0.001,None),initialize=95.8007796007676)
m.x22 = Var(within=Reals,bounds=(0.001,None),initialize=95.303225278852)
m.x23 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x31 = Var(within=Reals,bounds=(0.05245,0.0857),initialize=0.069075)
m.x32 = Var(within=Reals,bounds=(0.06175,0.095),initialize=0.078375)
m.x33 = Var(within=Reals,bounds=(0.0619,0.0939),initialize=0.0779)
m.x34 = Var(within=Reals,bounds=(0.0368,0.0768),initialize=0.0568)
m.x35 = Var(within=Reals,bounds=(0.0368,0.0768),initialize=0.0568)

m.obj = Objective(expr=   m.x18 + m.x19 + m.x20 + m.x21 + m.x22 - 30000*m.x23 + 25000*m.x24 - 30000*m.x25 - 50000*m.x26
                        + 25000*m.x27 + 5000*m.x28 + 15000*m.x29 + 50000*m.x30 + 20682900, sense=minimize)

m.c2 = Constraint(expr=-95.54*exp(0.09167*m.x31) + m.x18 == 0)

m.c3 = Constraint(expr=-93.27*exp(0.33889*m.x32) + m.x19 == 0)

m.c4 = Constraint(expr=-95.54*exp(0.09167*m.x31) + m.x20 == 0)

m.c5 = Constraint(expr=-93.27*exp(0.33889*m.x32) + m.x21 == 0)

m.c6 = Constraint(expr=-91.03*exp(0.58889*m.x33) + m.x22 == 0)

m.c7 = Constraint(expr=-exp(-0.33889*m.x32)*(errorf(m.x2)*m.x21 - 95*errorf(m.x10)) + m.x23 == 0)

m.c8 = Constraint(expr=-exp(-0.33889*m.x32)*(errorf(m.x3)*m.x21 - 97*errorf(m.x11)) + m.x25 == 0)

m.c9 = Constraint(expr=-exp(-0.58889*m.x33)*(errorf(m.x6)*m.x22 - 95*errorf(m.x14)) + m.x24 == 0)

m.c10 = Constraint(expr=-exp(-0.58889*m.x33)*(errorf(m.x7)*m.x22 - 97*errorf(m.x15)) + m.x26 == 0)

m.c11 = Constraint(expr=-exp(-0.58889*m.x33)*(errorf(m.x8)*m.x22 - 99*errorf(m.x16)) + m.x27 == 0)

m.c12 = Constraint(expr=-exp(-0.33889*m.x32)*(95*errorf(-m.x12) - errorf(-m.x4)*m.x21) + m.x28 == 0)

m.c13 = Constraint(expr=-exp(-0.33889*m.x32)*(97*errorf(-m.x13) - errorf(-m.x5)*m.x21) + m.x29 == 0)

m.c14 = Constraint(expr=-exp(-0.58889*m.x33)*(99*errorf(-m.x17) - errorf(-m.x9)*m.x22) + m.x30 == 0)

m.c15 = Constraint(expr=-1.71779218689115*(log(0.0105263157894737*m.x21) + 0.169445*m.x34**2)/m.x34 + m.x2 == 0)

m.c16 = Constraint(expr=-1.71779218689115*(log(0.0103092783505155*m.x21) + 0.169445*m.x34**2)/m.x34 + m.x3 == 0)

m.c17 = Constraint(expr=-1.71779218689115*(log(0.0105263157894737*m.x21) + 0.169445*m.x34**2)/m.x34 + m.x4 == 0)

m.c18 = Constraint(expr=-1.71779218689115*(log(0.0103092783505155*m.x21) + 0.169445*m.x34**2)/m.x34 + m.x5 == 0)

m.c19 = Constraint(expr=-1.30311549893554*(log(0.0105263157894737*m.x22) + 0.294445*m.x35**2)/m.x35 + m.x6 == 0)

m.c20 = Constraint(expr=-1.30311549893554*(log(0.0103092783505155*m.x22) + 0.294445*m.x35**2)/m.x35 + m.x7 == 0)

m.c21 = Constraint(expr=-1.30311549893554*(log(0.0101010101010101*m.x22) + 0.294445*m.x35**2)/m.x35 + m.x8 == 0)

m.c22 = Constraint(expr=-1.30311549893554*(log(0.0101010101010101*m.x22) + 0.294445*m.x35**2)/m.x35 + m.x9 == 0)

m.c23 = Constraint(expr= - m.x2 + m.x10 + 0.582142594215541*m.x34 == 0)

m.c24 = Constraint(expr= - m.x3 + m.x11 + 0.582142594215541*m.x34 == 0)

m.c25 = Constraint(expr= - m.x4 + m.x12 + 0.582142594215541*m.x34 == 0)

m.c26 = Constraint(expr= - m.x5 + m.x13 + 0.582142594215541*m.x34 == 0)

m.c27 = Constraint(expr= - m.x6 + m.x14 + 0.767391686168152*m.x35 == 0)

m.c28 = Constraint(expr= - m.x7 + m.x15 + 0.767391686168152*m.x35 == 0)

m.c29 = Constraint(expr= - m.x8 + m.x16 + 0.767391686168152*m.x35 == 0)

m.c30 = Constraint(expr= - m.x9 + m.x17 + 0.767391686168152*m.x35 == 0)
