#  NLP written by GAMS Convert at 04/21/18 13:51:46
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         34        3        6       25        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         58       58        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        170       65      105        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(6.21460809842219,8.41183267575841),initialize=6.21460809842219)
m.x3 = Var(within=Reals,bounds=(6.21460809842219,8.41183267575841),initialize=6.21460809842219)
m.x4 = Var(within=Reals,bounds=(6.21460809842219,8.41183267575841),initialize=6.21460809842219)
m.x5 = Var(within=Reals,bounds=(160,163.752806164),initialize=160)
m.x6 = Var(within=Reals,bounds=(160,163.752806164),initialize=160)
m.x7 = Var(within=Reals,bounds=(160,163.752806164),initialize=160)
m.x8 = Var(within=Reals,bounds=(160,163.752806164),initialize=160)
m.x9 = Var(within=Reals,bounds=(160,163.752806164),initialize=160)
m.x10 = Var(within=Reals,bounds=(160,178.461227596),initialize=160)
m.x11 = Var(within=Reals,bounds=(160,178.461227596),initialize=160)
m.x12 = Var(within=Reals,bounds=(160,178.461227596),initialize=160)
m.x13 = Var(within=Reals,bounds=(160,178.461227596),initialize=160)
m.x14 = Var(within=Reals,bounds=(160,178.461227596),initialize=160)
m.x15 = Var(within=Reals,bounds=(160,200),initialize=160)
m.x16 = Var(within=Reals,bounds=(160,200),initialize=160)
m.x17 = Var(within=Reals,bounds=(160,200),initialize=160)
m.x18 = Var(within=Reals,bounds=(160,200),initialize=160)
m.x19 = Var(within=Reals,bounds=(160,200),initialize=160)
m.x20 = Var(within=Reals,bounds=(160,221.538772404),initialize=160)
m.x21 = Var(within=Reals,bounds=(160,221.538772404),initialize=160)
m.x22 = Var(within=Reals,bounds=(160,221.538772404),initialize=160)
m.x23 = Var(within=Reals,bounds=(160,221.538772404),initialize=160)
m.x24 = Var(within=Reals,bounds=(160,221.538772404),initialize=160)
m.x25 = Var(within=Reals,bounds=(160,236.247193836),initialize=160)
m.x26 = Var(within=Reals,bounds=(160,236.247193836),initialize=160)
m.x27 = Var(within=Reals,bounds=(160,236.247193836),initialize=160)
m.x28 = Var(within=Reals,bounds=(160,236.247193836),initialize=160)
m.x29 = Var(within=Reals,bounds=(160,236.247193836),initialize=160)
m.x30 = Var(within=Reals,bounds=(60,63.752806164),initialize=60)
m.x31 = Var(within=Reals,bounds=(60,78.461227596),initialize=60)
m.x32 = Var(within=Reals,bounds=(60,100),initialize=60)
m.x33 = Var(within=Reals,bounds=(60,121.538772404),initialize=60)
m.x34 = Var(within=Reals,bounds=(60,136.247193836),initialize=60)
m.x35 = Var(within=Reals,bounds=(60,63.752806164),initialize=60)
m.x36 = Var(within=Reals,bounds=(60,78.461227596),initialize=60)
m.x37 = Var(within=Reals,bounds=(60,100),initialize=60)
m.x38 = Var(within=Reals,bounds=(60,121.538772404),initialize=60)
m.x39 = Var(within=Reals,bounds=(60,136.247193836),initialize=60)
m.x40 = Var(within=Reals,bounds=(60,63.752806164),initialize=60)
m.x41 = Var(within=Reals,bounds=(60,78.461227596),initialize=60)
m.x42 = Var(within=Reals,bounds=(60,100),initialize=60)
m.x43 = Var(within=Reals,bounds=(60,121.538772404),initialize=60)
m.x44 = Var(within=Reals,bounds=(60,136.247193836),initialize=60)
m.x45 = Var(within=Reals,bounds=(60,63.752806164),initialize=60)
m.x46 = Var(within=Reals,bounds=(60,78.461227596),initialize=60)
m.x47 = Var(within=Reals,bounds=(60,100),initialize=60)
m.x48 = Var(within=Reals,bounds=(60,121.538772404),initialize=60)
m.x49 = Var(within=Reals,bounds=(60,136.247193836),initialize=60)
m.x50 = Var(within=Reals,bounds=(60,63.752806164),initialize=60)
m.x51 = Var(within=Reals,bounds=(60,78.461227596),initialize=60)
m.x52 = Var(within=Reals,bounds=(60,100),initialize=60)
m.x53 = Var(within=Reals,bounds=(60,121.538772404),initialize=60)
m.x54 = Var(within=Reals,bounds=(60,136.247193836),initialize=60)
m.x55 = Var(within=Reals,bounds=(4.8283137373023,7.02553831463852),initialize=4.8283137373023)
m.x56 = Var(within=Reals,bounds=(4.42284862919414,6.62007320653036),initialize=4.42284862919414)
m.x57 = Var(within=Reals,bounds=(0.0177777777777778,0.16),initialize=0.0177777777777778)
m.x58 = Var(within=Reals,bounds=(0.0213333333333333,0.192),initialize=0.0213333333333333)

m.obj = Objective(expr=0.3*(10*exp(0.6*m.x2) + 10*exp(0.6*m.x3) + 10*exp(0.6*m.x4)) - 1.54711033913716E-6*m.x5
                        - 0.000219040316990534*m.x6 - 0.00264813118267794*m.x7 - 0.000219040316990534*m.x8
                        - 1.54711033913716E-6*m.x9 - 0.000219040316990533*m.x10 - 0.0310117896917886*m.x11
                        - 0.374923157717238*m.x12 - 0.0310117896917886*m.x13 - 0.000219040316990532*m.x14
                        - 0.00264813118267793*m.x15 - 0.374923157717237*m.x16 - 4.5327075795914*m.x17
                        - 0.374923157717237*m.x18 - 0.00264813118267791*m.x19 - 0.000219040316990532*m.x20
                        - 0.0310117896917884*m.x21 - 0.374923157717236*m.x22 - 0.0310117896917884*m.x23
                        - 0.000219040316990531*m.x24 - 1.54711033913713E-6*m.x25 - 0.000219040316990529*m.x26
                        - 0.00264813118267789*m.x27 - 0.000219040316990529*m.x28 - 1.54711033913712E-6*m.x29
                        - 1.9690495225382E-6*m.x30 - 0.000278778585260679*m.x31 - 0.00337034877795374*m.x32
                        - 0.000278778585260679*m.x33 - 1.9690495225382E-6*m.x34 - 0.000278778585260679*m.x35
                        - 0.0394695505168218*m.x36 - 0.477174928003758*m.x37 - 0.0394695505168218*m.x38
                        - 0.000278778585260677*m.x39 - 0.00337034877795372*m.x40 - 0.477174928003756*m.x41
                        - 5.7689005558436*m.x42 - 0.477174928003756*m.x43 - 0.00337034877795371*m.x44
                        - 0.000278778585260677*m.x45 - 0.0394695505168216*m.x46 - 0.477174928003755*m.x47
                        - 0.0394695505168216*m.x48 - 0.000278778585260676*m.x49 - 1.96904952253816E-6*m.x50
                        - 0.000278778585260674*m.x51 - 0.00337034877795367*m.x52 - 0.000278778585260674*m.x53
                        - 1.96904952253816E-6*m.x54, sense=minimize)

m.c2 = Constraint(expr=   m.x2 - m.x55 >= 0.693147180559945)

m.c3 = Constraint(expr=   m.x3 - m.x55 >= 1.09861228866811)

m.c4 = Constraint(expr=   m.x4 - m.x55 >= 1.38629436111989)

m.c5 = Constraint(expr=   m.x2 - m.x56 >= 1.38629436111989)

m.c6 = Constraint(expr=   m.x3 - m.x56 >= 1.79175946922805)

m.c7 = Constraint(expr=   m.x4 - m.x56 >= 1.09861228866811)

m.c8 = Constraint(expr=m.x5*m.x57 + m.x30*m.x58 <= 8)

m.c9 = Constraint(expr=m.x6*m.x57 + m.x31*m.x58 <= 8)

m.c10 = Constraint(expr=m.x7*m.x57 + m.x32*m.x58 <= 8)

m.c11 = Constraint(expr=m.x8*m.x57 + m.x33*m.x58 <= 8)

m.c12 = Constraint(expr=m.x9*m.x57 + m.x34*m.x58 <= 8)

m.c13 = Constraint(expr=m.x10*m.x57 + m.x35*m.x58 <= 8)

m.c14 = Constraint(expr=m.x11*m.x57 + m.x36*m.x58 <= 8)

m.c15 = Constraint(expr=m.x12*m.x57 + m.x37*m.x58 <= 8)

m.c16 = Constraint(expr=m.x13*m.x57 + m.x38*m.x58 <= 8)

m.c17 = Constraint(expr=m.x14*m.x57 + m.x39*m.x58 <= 8)

m.c18 = Constraint(expr=m.x15*m.x57 + m.x40*m.x58 <= 8)

m.c19 = Constraint(expr=m.x16*m.x57 + m.x41*m.x58 <= 8)

m.c20 = Constraint(expr=m.x17*m.x57 + m.x42*m.x58 <= 8)

m.c21 = Constraint(expr=m.x18*m.x57 + m.x43*m.x58 <= 8)

m.c22 = Constraint(expr=m.x19*m.x57 + m.x44*m.x58 <= 8)

m.c23 = Constraint(expr=m.x20*m.x57 + m.x45*m.x58 <= 8)

m.c24 = Constraint(expr=m.x21*m.x57 + m.x46*m.x58 <= 8)

m.c25 = Constraint(expr=m.x22*m.x57 + m.x47*m.x58 <= 8)

m.c26 = Constraint(expr=m.x23*m.x57 + m.x48*m.x58 <= 8)

m.c27 = Constraint(expr=m.x24*m.x57 + m.x49*m.x58 <= 8)

m.c28 = Constraint(expr=m.x25*m.x57 + m.x50*m.x58 <= 8)

m.c29 = Constraint(expr=m.x26*m.x57 + m.x51*m.x58 <= 8)

m.c30 = Constraint(expr=m.x27*m.x57 + m.x52*m.x58 <= 8)

m.c31 = Constraint(expr=m.x28*m.x57 + m.x53*m.x58 <= 8)

m.c32 = Constraint(expr=m.x29*m.x57 + m.x54*m.x58 <= 8)

m.c33 = Constraint(expr=-exp(2.99573227355399 - m.x55) + m.x57 == 0)

m.c34 = Constraint(expr=-exp(2.77258872223978 - m.x56) + m.x58 == 0)
