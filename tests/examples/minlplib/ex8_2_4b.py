#  NLP written by GAMS Convert at 04/21/18 13:51:47
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         88        7        6       75        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         62       62        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        378       69      309        0
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
m.x55 = Var(within=Reals,bounds=(4.82831,7.1591),initialize=4.82831)
m.x56 = Var(within=Reals,bounds=(4.42285,6.7071),initialize=4.42285)
m.x57 = Var(within=Reals,bounds=(0.00622203373693604,0.0640002391877942),initialize=0.00622203373693604)
m.x58 = Var(within=Reals,bounds=(0.0155550843423401,0.160000597969486),initialize=0.0155550843423401)
m.x59 = Var(within=Reals,bounds=(0.00622203373693604,0.0640002391877942),initialize=0.00622203373693604)
m.x60 = Var(within=Reals,bounds=(0.019555254080048,0.191999736805455),initialize=0.019555254080048)
m.x61 = Var(within=Reals,bounds=(0.00488881352001201,0.0479999342013636),initialize=0.00488881352001201)
m.x62 = Var(within=Reals,bounds=(0.00488881352001201,0.0479999342013636),initialize=0.00488881352001201)

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

m.c8 = Constraint(expr=m.x5*m.x57 + m.x30*m.x60 <= 8)

m.c9 = Constraint(expr=m.x6*m.x57 + m.x31*m.x60 <= 8)

m.c10 = Constraint(expr=m.x7*m.x57 + m.x32*m.x60 <= 8)

m.c11 = Constraint(expr=m.x8*m.x57 + m.x33*m.x60 <= 8)

m.c12 = Constraint(expr=m.x9*m.x57 + m.x34*m.x60 <= 8)

m.c13 = Constraint(expr=m.x10*m.x57 + m.x35*m.x60 <= 8)

m.c14 = Constraint(expr=m.x11*m.x57 + m.x36*m.x60 <= 8)

m.c15 = Constraint(expr=m.x12*m.x57 + m.x37*m.x60 <= 8)

m.c16 = Constraint(expr=m.x13*m.x57 + m.x38*m.x60 <= 8)

m.c17 = Constraint(expr=m.x14*m.x57 + m.x39*m.x60 <= 8)

m.c18 = Constraint(expr=m.x15*m.x57 + m.x40*m.x60 <= 8)

m.c19 = Constraint(expr=m.x16*m.x57 + m.x41*m.x60 <= 8)

m.c20 = Constraint(expr=m.x17*m.x57 + m.x42*m.x60 <= 8)

m.c21 = Constraint(expr=m.x18*m.x57 + m.x43*m.x60 <= 8)

m.c22 = Constraint(expr=m.x19*m.x57 + m.x44*m.x60 <= 8)

m.c23 = Constraint(expr=m.x20*m.x57 + m.x45*m.x60 <= 8)

m.c24 = Constraint(expr=m.x21*m.x57 + m.x46*m.x60 <= 8)

m.c25 = Constraint(expr=m.x22*m.x57 + m.x47*m.x60 <= 8)

m.c26 = Constraint(expr=m.x23*m.x57 + m.x48*m.x60 <= 8)

m.c27 = Constraint(expr=m.x24*m.x57 + m.x49*m.x60 <= 8)

m.c28 = Constraint(expr=m.x25*m.x57 + m.x50*m.x60 <= 8)

m.c29 = Constraint(expr=m.x26*m.x57 + m.x51*m.x60 <= 8)

m.c30 = Constraint(expr=m.x27*m.x57 + m.x52*m.x60 <= 8)

m.c31 = Constraint(expr=m.x28*m.x57 + m.x53*m.x60 <= 8)

m.c32 = Constraint(expr=m.x29*m.x57 + m.x54*m.x60 <= 8)

m.c33 = Constraint(expr=m.x5*m.x58 + m.x30*m.x61 <= 8)

m.c34 = Constraint(expr=m.x6*m.x58 + m.x31*m.x61 <= 8)

m.c35 = Constraint(expr=m.x7*m.x58 + m.x32*m.x61 <= 8)

m.c36 = Constraint(expr=m.x8*m.x58 + m.x33*m.x61 <= 8)

m.c37 = Constraint(expr=m.x9*m.x58 + m.x34*m.x61 <= 8)

m.c38 = Constraint(expr=m.x10*m.x58 + m.x35*m.x61 <= 8)

m.c39 = Constraint(expr=m.x11*m.x58 + m.x36*m.x61 <= 8)

m.c40 = Constraint(expr=m.x12*m.x58 + m.x37*m.x61 <= 8)

m.c41 = Constraint(expr=m.x13*m.x58 + m.x38*m.x61 <= 8)

m.c42 = Constraint(expr=m.x14*m.x58 + m.x39*m.x61 <= 8)

m.c43 = Constraint(expr=m.x15*m.x58 + m.x40*m.x61 <= 8)

m.c44 = Constraint(expr=m.x16*m.x58 + m.x41*m.x61 <= 8)

m.c45 = Constraint(expr=m.x17*m.x58 + m.x42*m.x61 <= 8)

m.c46 = Constraint(expr=m.x18*m.x58 + m.x43*m.x61 <= 8)

m.c47 = Constraint(expr=m.x19*m.x58 + m.x44*m.x61 <= 8)

m.c48 = Constraint(expr=m.x20*m.x58 + m.x45*m.x61 <= 8)

m.c49 = Constraint(expr=m.x21*m.x58 + m.x46*m.x61 <= 8)

m.c50 = Constraint(expr=m.x22*m.x58 + m.x47*m.x61 <= 8)

m.c51 = Constraint(expr=m.x23*m.x58 + m.x48*m.x61 <= 8)

m.c52 = Constraint(expr=m.x24*m.x58 + m.x49*m.x61 <= 8)

m.c53 = Constraint(expr=m.x25*m.x58 + m.x50*m.x61 <= 8)

m.c54 = Constraint(expr=m.x26*m.x58 + m.x51*m.x61 <= 8)

m.c55 = Constraint(expr=m.x27*m.x58 + m.x52*m.x61 <= 8)

m.c56 = Constraint(expr=m.x28*m.x58 + m.x53*m.x61 <= 8)

m.c57 = Constraint(expr=m.x29*m.x58 + m.x54*m.x61 <= 8)

m.c58 = Constraint(expr=m.x5*m.x59 + m.x30*m.x62 <= 8)

m.c59 = Constraint(expr=m.x6*m.x59 + m.x31*m.x62 <= 8)

m.c60 = Constraint(expr=m.x7*m.x59 + m.x32*m.x62 <= 8)

m.c61 = Constraint(expr=m.x8*m.x59 + m.x33*m.x62 <= 8)

m.c62 = Constraint(expr=m.x9*m.x59 + m.x34*m.x62 <= 8)

m.c63 = Constraint(expr=m.x10*m.x59 + m.x35*m.x62 <= 8)

m.c64 = Constraint(expr=m.x11*m.x59 + m.x36*m.x62 <= 8)

m.c65 = Constraint(expr=m.x12*m.x59 + m.x37*m.x62 <= 8)

m.c66 = Constraint(expr=m.x13*m.x59 + m.x38*m.x62 <= 8)

m.c67 = Constraint(expr=m.x14*m.x59 + m.x39*m.x62 <= 8)

m.c68 = Constraint(expr=m.x15*m.x59 + m.x40*m.x62 <= 8)

m.c69 = Constraint(expr=m.x16*m.x59 + m.x41*m.x62 <= 8)

m.c70 = Constraint(expr=m.x17*m.x59 + m.x42*m.x62 <= 8)

m.c71 = Constraint(expr=m.x18*m.x59 + m.x43*m.x62 <= 8)

m.c72 = Constraint(expr=m.x19*m.x59 + m.x44*m.x62 <= 8)

m.c73 = Constraint(expr=m.x20*m.x59 + m.x45*m.x62 <= 8)

m.c74 = Constraint(expr=m.x21*m.x59 + m.x46*m.x62 <= 8)

m.c75 = Constraint(expr=m.x22*m.x59 + m.x47*m.x62 <= 8)

m.c76 = Constraint(expr=m.x23*m.x59 + m.x48*m.x62 <= 8)

m.c77 = Constraint(expr=m.x24*m.x59 + m.x49*m.x62 <= 8)

m.c78 = Constraint(expr=m.x25*m.x59 + m.x50*m.x62 <= 8)

m.c79 = Constraint(expr=m.x26*m.x59 + m.x51*m.x62 <= 8)

m.c80 = Constraint(expr=m.x27*m.x59 + m.x52*m.x62 <= 8)

m.c81 = Constraint(expr=m.x28*m.x59 + m.x53*m.x62 <= 8)

m.c82 = Constraint(expr=m.x29*m.x59 + m.x54*m.x62 <= 8)

m.c83 = Constraint(expr=-exp(2.07944154167984 - m.x55) + m.x57 == 0)

m.c84 = Constraint(expr=-exp(2.99573227355399 - m.x55) + m.x58 == 0)

m.c85 = Constraint(expr=-exp(2.07944154167984 - m.x55) + m.x59 == 0)

m.c86 = Constraint(expr=-exp(2.77258872223978 - m.x56) + m.x60 == 0)

m.c87 = Constraint(expr=-exp(1.38629436111989 - m.x56) + m.x61 == 0)

m.c88 = Constraint(expr=-exp(1.38629436111989 - m.x56) + m.x62 == 0)
