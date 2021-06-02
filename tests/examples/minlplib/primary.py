#  MINLP written by GAMS Convert at 04/21/18 13:54:00
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        164       30       30      104        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         82       22        8       52        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1637     1394      243        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.i1 = Var(within=Integers,bounds=(0,15),initialize=0)
m.i2 = Var(within=Integers,bounds=(0,15),initialize=0)
m.i3 = Var(within=Integers,bounds=(0,15),initialize=0)
m.i4 = Var(within=Integers,bounds=(0,15),initialize=0)
m.i5 = Var(within=Integers,bounds=(0,15),initialize=0)
m.i6 = Var(within=Integers,bounds=(0,15),initialize=0)
m.i7 = Var(within=Integers,bounds=(0,15),initialize=0)
m.i8 = Var(within=Integers,bounds=(0,15),initialize=0)
m.i9 = Var(within=Integers,bounds=(0,15),initialize=0)
m.i10 = Var(within=Integers,bounds=(0,15),initialize=0)
m.i11 = Var(within=Integers,bounds=(0,15),initialize=0)
m.i12 = Var(within=Integers,bounds=(0,15),initialize=0)
m.i13 = Var(within=Integers,bounds=(0,15),initialize=0)
m.i14 = Var(within=Integers,bounds=(0,15),initialize=0)
m.i15 = Var(within=Integers,bounds=(0,15),initialize=0)
m.i16 = Var(within=Integers,bounds=(0,15),initialize=0)
m.i17 = Var(within=Integers,bounds=(0,15),initialize=0)
m.i18 = Var(within=Integers,bounds=(0,15),initialize=0)
m.i19 = Var(within=Integers,bounds=(0,15),initialize=0)
m.i20 = Var(within=Integers,bounds=(0,15),initialize=0)
m.i21 = Var(within=Integers,bounds=(0,15),initialize=0)
m.i22 = Var(within=Integers,bounds=(0,15),initialize=0)
m.i23 = Var(within=Integers,bounds=(0,15),initialize=0)
m.i24 = Var(within=Integers,bounds=(0,15),initialize=0)
m.i25 = Var(within=Integers,bounds=(0,15),initialize=0)
m.i26 = Var(within=Integers,bounds=(0,15),initialize=0)
m.i27 = Var(within=Integers,bounds=(0,15),initialize=0)
m.i28 = Var(within=Integers,bounds=(0,15),initialize=0)
m.i29 = Var(within=Integers,bounds=(0,15),initialize=0)
m.i30 = Var(within=Integers,bounds=(0,15),initialize=0)
m.i31 = Var(within=Integers,bounds=(0,15),initialize=0)
m.i32 = Var(within=Integers,bounds=(0,15),initialize=0)
m.i33 = Var(within=Integers,bounds=(0,15),initialize=0)
m.i34 = Var(within=Integers,bounds=(0,15),initialize=0)
m.i35 = Var(within=Integers,bounds=(0,15),initialize=0)
m.i36 = Var(within=Integers,bounds=(0,15),initialize=0)
m.i37 = Var(within=Integers,bounds=(0,15),initialize=0)
m.i38 = Var(within=Integers,bounds=(0,15),initialize=0)
m.i39 = Var(within=Integers,bounds=(0,15),initialize=0)
m.i40 = Var(within=Integers,bounds=(0,15),initialize=0)
m.i41 = Var(within=Integers,bounds=(0,15),initialize=0)
m.i42 = Var(within=Integers,bounds=(0,15),initialize=0)
m.i43 = Var(within=Integers,bounds=(0,15),initialize=0)
m.i44 = Var(within=Integers,bounds=(0,15),initialize=0)
m.i45 = Var(within=Integers,bounds=(0,172),initialize=0)
m.i46 = Var(within=Integers,bounds=(0,330),initialize=0)
m.i47 = Var(within=Integers,bounds=(0,232),initialize=0)
m.i48 = Var(within=Integers,bounds=(0,60),initialize=0)
m.i49 = Var(within=Integers,bounds=(0,30),initialize=0)
m.i50 = Var(within=Integers,bounds=(0,15),initialize=0)
m.i51 = Var(within=Integers,bounds=(0,225),initialize=0)
m.i52 = Var(within=Integers,bounds=(0,60),initialize=0)
m.b53 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b54 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b55 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b56 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b57 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b58 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b59 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b60 = Var(within=Binary,bounds=(0,1),initialize=0)
m.x61 = Var(within=Reals,bounds=(50,1000),initialize=50)
m.x62 = Var(within=Reals,bounds=(100,2000),initialize=100)
m.x63 = Var(within=Reals,bounds=(2,200),initialize=2)
m.x64 = Var(within=Reals,bounds=(1,135),initialize=1)
m.x65 = Var(within=Reals,bounds=(0.001,1),initialize=0.001)
m.x66 = Var(within=Reals,bounds=(0.001,1),initialize=0.001)
m.x67 = Var(within=Reals,bounds=(0.001,1),initialize=0.001)
m.x68 = Var(within=Reals,bounds=(0.001,1),initialize=0.001)
m.x69 = Var(within=Reals,bounds=(-1,1.3),initialize=0)
m.x70 = Var(within=Reals,bounds=(1,32.2),initialize=1)
m.x71 = Var(within=Reals,bounds=(10,110),initialize=10)
m.x72 = Var(within=Reals,bounds=(18.4,100),initialize=18.4)
m.x73 = Var(within=Reals,bounds=(0,5300),initialize=0)
m.x74 = Var(within=Reals,bounds=(0.48,2500),initialize=0.48)
m.x75 = Var(within=Reals,bounds=(0.001,1),initialize=0.001)
m.x76 = Var(within=Reals,bounds=(1.4,14),initialize=1.4)
m.x77 = Var(within=Reals,bounds=(0.001,1),initialize=0.001)
m.x78 = Var(within=Reals,bounds=(1.4,14),initialize=1.4)
m.x79 = Var(within=Reals,bounds=(-5.4,6100),initialize=0)
m.x80 = Var(within=Reals,bounds=(-16000,0),initialize=0)
m.x81 = Var(within=Reals,bounds=(-1,10),initialize=0)

m.obj = Objective(expr=-m.x72/m.x70, sense=minimize)

m.c1 = Constraint(expr= - 23.58*m.i1 - 22.88*m.i2 - 21.74*m.i3 - 18.25*m.i4 - 18.18*m.i5 - 24.96*m.i6 - 24.14*m.i7
                        - 26.15*m.i8 - 9.2*m.i9 - 27.38*m.i10 - 27.15*m.i11 - 21.78*m.i12 - 21.78*m.i13 - 21.32*m.i14
                        - 21.32*m.i15 - 21.32*m.i16 - 26.73*m.i17 - 31.01*m.i18 - 31.01*m.i19 - 31.01*m.i20 + 0.03*m.i21
                        - 38.13*m.i22 - 66.86*m.i23 - 93.84*m.i24 - 92.88*m.i25 - 22.42*m.i26 - 31.22*m.i27
                        - 76.75*m.i28 - 94.97*m.i29 - 72.24*m.i30 - 169.09*m.i31 - 81.1*m.i32 + 10.5*m.i33 - 73.23*m.i34
                        - 50.17*m.i35 - 52.82*m.i36 - 11.74*m.i37 - 74.6*m.i38 - 57.55*m.i39 - 125.66*m.i40
                        - 152.54*m.i41 - 63.56*m.i42 - 68.78*m.i43 - 52.1*m.i44 + m.x61 == 198.2)

m.c2 = Constraint(expr=-m.x61/(0.584 + 0.0136065*m.i1 - (0.0141*m.i1 + 0.0189*m.i2 + 0.0164*m.i3 + 0.0067*m.i4 + 0.0113*
                       m.i5 + 0.0129*m.i6 + 0.0117*m.i7 + 0.0026*m.i8 + 0.0027*m.i9 + 0.002*m.i10 + 0.01*m.i11 + 0.0122*
                       m.i12 + 0.0122*m.i13 + 0.0042*m.i14 + 0.0042*m.i15 + 0.0042*m.i16 + 0.0082*m.i17 + 0.0143*m.i18
                        + 0.0143*m.i19 + 0.0143*m.i20 + 0.0111*m.i21 + 0.0105*m.i22 + 0.0133*m.i23 + 0.0068*m.i24 + 
                       0.0741*m.i25 + 0.0168*m.i26 + 0.0098*m.i27 + 0.038*m.i28 + 0.0284*m.i29 + 0.0379*m.i30 + 0.0791*
                       m.i31 + 0.0481*m.i32 + 0.0143*m.i33 + 0.0243*m.i34 + 0.0295*m.i35 + 0.013*m.i36 + 0.0169*m.i37 + 
                       0.0255*m.i38 + 0.0085*m.i39 + 0.0496*m.i40 + 0.0437*m.i41 + 0.0031*m.i42 + 0.0119*m.i43 + 0.0019*
                       m.i44)**2 + 0.0182385*m.i2 + 0.015826*m.i3 + 0.0064655*m.i4 + 0.0109045*m.i5 + 0.0124485*m.i6 + 
                       0.0112905*m.i7 + 0.002509*m.i8 + 0.0026055*m.i9 + 0.00193*m.i10 + 0.00965*m.i11 + 0.011773*m.i12
                        + 0.011773*m.i13 + 0.004053*m.i14 + 0.004053*m.i15 + 0.004053*m.i16 + 0.007913*m.i17 + 0.0137995
                       *m.i18 + 0.0137995*m.i19 + 0.0137995*m.i20 + 0.0107115*m.i21 + 0.0101325*m.i22 + 0.0128345*m.i23
                        + 0.006562*m.i24 + 0.0715065*m.i25 + 0.016212*m.i26 + 0.009457*m.i27 + 0.03667*m.i28 + 0.027406*
                       m.i29 + 0.0365735*m.i30 + 0.0763315*m.i31 + 0.0464165*m.i32 + 0.0137995*m.i33 + 0.0234495*m.i34
                        + 0.0284675*m.i35 + 0.012545*m.i36 + 0.0163085*m.i37 + 0.0246075*m.i38 + 0.0082025*m.i39 + 
                       0.047864*m.i40 + 0.0421705*m.i41 + 0.0029915*m.i42 + 0.0114835*m.i43 + 0.0018335*m.i44) + m.x62
                        == 0)

m.c3 = Constraint(expr=-1/(0.113 + 0.014*m.i1 + 0.0096*m.i2 + 0.0044*m.i3 - 0.0011*m.i4 + 0.0124*m.i5 + 0.007*m.i6 + 
                       0.0021*m.i7 + 0.0004*m.i8 + 0.0072*m.i9 + 0.0016*m.i10 + 0.0071*m.i11 + 0.006*m.i12 + 0.006*m.i13
                        - 0.0029*m.i14 - 0.0029*m.i15 - 0.0029*m.i16 + 0.0053*m.i17 + 0.0024*m.i18 + 0.0024*m.i19 + 
                       0.0024*m.i20 + 0.0089*m.i21 + 0.0081*m.i22 - 0.0025*m.i23 + 0.0066*m.i24 - 0.0048*m.i25 + 0.0017*
                       m.i26 - 0.0016*m.i27 + 0.0033*m.i28 + 0.0036*m.i29 + 0.0066*m.i30 + 0.0051*m.i31 + 0.0091*m.i32
                        - 0.0069*m.i33 - 0.0013*m.i34 - 0.0013*m.i35 - 0.005*m.i36 - 0.0042*m.i37 + 0.0131*m.i38 - 
                       0.0044*m.i39 + 0.0165*m.i40 + 0.0032*m.i41 - 0.002*m.i42 - 0.0017*m.i43 - 0.0019*m.i44)**2
                        + m.x63 == 0)

m.c4 = Constraint(expr= - 27.9060362667016*m.i1 - 22.6378084870734*m.i2 - 17.139736374375*m.i3 - 11.6136038458281*m.i4
                        - 24.6572239375156*m.i5 - 15.4652846358562*m.i6 - 10.3292345315312*m.i7 - 18.4762155922406*m.i8
                        - 24.4091998531656*m.i9 - 13.0986012113105*m.i10 - 17.9476983094687*m.i11
                        - 14.904978927175*m.i12 - 14.904978927175*m.i13 - 7.02123776995307*m.i14
                        - 7.02123776995307*m.i15 - 7.02123776995307*m.i16 - 14.2028684258641*m.i17
                        - 10.9018002093344*m.i18 - 10.9018002093344*m.i19 - 10.9018002093344*m.i20
                        - 13.5482021250156*m.i21 - 18.6172418998938*m.i22 - 19.3804300725235*m.i23
                        - 22.3977664311391*m.i24 - 18.1753929278063*m.i25 - 15.1179767129938*m.i26
                        - 12.7299939157219*m.i27 - 23.1465990779122*m.i28 - 23.1027820855781*m.i29
                        - 32.3493558653063*m.i30 - 41.8754787811391*m.i31 - 38.6579257229438*m.i32
                        - 13.2334131164469*m.i33 - 26.489960594675*m.i34 - 17.2714223569766*m.i35
                        - 12.6966779338688*m.i36 - 11.7078216565312*m.i37 - 10.8040394990938*m.i39
                        - 28.2386206875156*m.i40 - 33.7063565892125*m.i41 - 26.3895787500156*m.i42
                        - 20.7267295870188*m.i43 - 19.9761272356828*m.i44 + m.x64 == -4.74320181253128)

m.c5 = Constraint(expr=-m.x61/m.x62 + m.x65 == 0)

m.c6 = Constraint(expr=-294.25/m.x62 + m.x66 == 0)

m.c7 = Constraint(expr=-316.45/m.x62 + m.x67 == 0)

m.c8 = Constraint(expr=-272.05/m.x62 + m.x68 == 0)

m.c9 = Constraint(expr=log(0.987166831194472*m.x63) - 6.09648/m.x65 - 1.28862*log(m.x65) + 0.169347*m.x65**6 + m.x79
                        == -5.97214)

m.c10 = Constraint(expr=15.6875/m.x65 + 13.4721*log(m.x65) - 0.43577*m.x65**6 + m.x80 == 15.2518)

m.c11 = Constraint(expr=m.x69*m.x80 - m.x79 == 0)

m.c12 = Constraint(expr=-(3.7413/(1 - m.x66) + 52.3782*(1 - m.x66)**0.333333333333333*m.x69/m.x66 + 35.563135*m.x69 + 
                        3.620747*m.x69/(1 - m.x66)) - m.x64 + 4.1868*m.x70 == 12.0553)

m.c13 = Constraint(expr= - 2.373*m.i1 - 2.226*m.i2 - 1.691*m.i3 - 0.636*m.i4 - 1.724*m.i5 - 2.205*m.i6 - 2.138*m.i7
                         - 2.661*m.i8 - 1.155*m.i9 - 3.302*m.i10 - 2.398*m.i11 - 1.942*m.i12 - 1.942*m.i13 - 0.664*m.i14
                         - 0.664*m.i15 - 0.664*m.i16 - 2.544*m.i17 - 3.059*m.i18 - 3.059*m.i19 - 3.059*m.i20
                         + 0.67*m.i21 - 4.532*m.i22 - 6.582*m.i23 - 9.52*m.i24 - 16.826*m.i25 - 2.41*m.i26 - 4.682*m.i27
                         - 8.972*m.i28 - 6.645*m.i29 - 9.093*m.i30 - 19.537*m.i31 - 9.633*m.i32 - 5.909*m.i33
                         - 10.788*m.i34 - 6.436*m.i35 - 6.93*m.i36 - 1.896*m.i37 - 3.335*m.i38 - 6.528*m.i39
                         - 12.851*m.i40 - 16.738*m.i41 - 6.884*m.i42 - 6.817*m.i43 - 5.984*m.i44 + m.x71 == 15.3)

m.c14 = Constraint(expr=-((1 - m.x68)/(1 - m.x65))**0.38*m.x71 + m.x72 == 0)

m.c15 = Constraint(expr=-log(0.987166831194472*m.x63)*m.x65/(1 - m.x65) + m.x73 == 0)

m.c16 = Constraint(expr= - 0.4605*m.x73 + m.x74 == 0.4835)

m.c17 = Constraint(expr=-(m.x73 - (1 + m.x65)*m.x74)/m.x74/(3 + m.x65)/(1 - m.x65)**2 + m.x81 == 0)

m.c18 = Constraint(expr=-exp(-(1 + m.x81*(3 + m.x67)*(1 - m.x67)**3 - m.x67**2)*m.x74/m.x67) + m.x75 == 0)

m.c19 = Constraint(expr=-m.x75*m.x63 + m.x76 == 0)

m.c20 = Constraint(expr=-exp(-(1 + m.x81*(3 + m.x68)*(1 - m.x68)**3 - m.x68**2)*m.x74/m.x68) + m.x77 == 0)

m.c21 = Constraint(expr=-m.x77*m.x63 + m.x78 == 0)

m.c22 = Constraint(expr=   m.i1 + m.i2 + m.i3 + m.i4 + m.i5 + m.i6 + m.i7 + m.i8 + m.i9 + m.i10 + m.i11 + m.i12 + m.i13
                         + m.i14 + m.i15 + m.i16 + m.i17 + m.i18 + m.i19 + m.i20 + m.i21 + m.i22 + m.i23 + m.i24 + m.i25
                         + m.i26 + m.i27 + m.i28 + m.i29 + m.i30 + m.i31 + m.i32 + m.i33 + m.i34 + m.i35 + m.i36 + m.i37
                         + m.i38 + m.i39 + m.i40 + m.i41 + m.i42 + m.i43 + m.i44 >= 2)

m.c23 = Constraint(expr=   m.i1 + m.i2 + m.i3 + m.i4 + m.i5 + m.i6 + m.i7 + m.i8 + m.i9 + m.i10 + m.i21 + m.i22 + m.i23
                         + m.i24 + m.i25 + m.i26 + m.i28 + m.i30 + m.i31 + m.i32 + m.i33 + m.i34 + m.i35 + m.i37 + m.i38
                         + m.i40 + m.i41 + m.i42 + m.i43 - m.b53 >= 0)

m.c24 = Constraint(expr=   m.i1 - 15*m.b53 <= 0)

m.c25 = Constraint(expr=   m.i2 - 15*m.b53 <= 0)

m.c26 = Constraint(expr=   m.i3 - 15*m.b53 <= 0)

m.c27 = Constraint(expr=   m.i4 - 15*m.b53 <= 0)

m.c28 = Constraint(expr=   m.i5 - 15*m.b53 <= 0)

m.c29 = Constraint(expr=   m.i6 - 15*m.b53 <= 0)

m.c30 = Constraint(expr=   m.i7 - 15*m.b53 <= 0)

m.c31 = Constraint(expr=   m.i8 - 15*m.b53 <= 0)

m.c32 = Constraint(expr=   m.i9 - 15*m.b53 <= 0)

m.c33 = Constraint(expr=   m.i10 - 15*m.b53 <= 0)

m.c34 = Constraint(expr=   m.i21 - 15*m.b53 <= 0)

m.c35 = Constraint(expr=   m.i22 - 15*m.b53 <= 0)

m.c36 = Constraint(expr=   m.i23 - 15*m.b53 <= 0)

m.c37 = Constraint(expr=   m.i24 - 15*m.b53 <= 0)

m.c38 = Constraint(expr=   m.i25 - 15*m.b53 <= 0)

m.c39 = Constraint(expr=   m.i26 - 15*m.b53 <= 0)

m.c40 = Constraint(expr=   m.i28 - 15*m.b53 <= 0)

m.c41 = Constraint(expr=   m.i30 - 15*m.b53 <= 0)

m.c42 = Constraint(expr=   m.i31 - 15*m.b53 <= 0)

m.c43 = Constraint(expr=   m.i32 - 15*m.b53 <= 0)

m.c44 = Constraint(expr=   m.i33 - 15*m.b53 <= 0)

m.c45 = Constraint(expr=   m.i34 - 15*m.b53 <= 0)

m.c46 = Constraint(expr=   m.i35 - 15*m.b53 <= 0)

m.c47 = Constraint(expr=   m.i37 - 15*m.b53 <= 0)

m.c48 = Constraint(expr=   m.i38 - 15*m.b53 <= 0)

m.c49 = Constraint(expr=   m.i40 - 15*m.b53 <= 0)

m.c50 = Constraint(expr=   m.i41 - 15*m.b53 <= 0)

m.c51 = Constraint(expr=   m.i42 - 15*m.b53 <= 0)

m.c52 = Constraint(expr=   m.i43 - 15*m.b53 <= 0)

m.c53 = Constraint(expr=   m.i11 + m.i12 + m.i14 + m.i17 + m.i18 + m.i27 + m.i29 + m.i36 + m.i39 + m.i44 - m.b54 >= 0)

m.c54 = Constraint(expr=   m.i11 - 15*m.b54 <= 0)

m.c55 = Constraint(expr=   m.i12 - 15*m.b54 <= 0)

m.c56 = Constraint(expr=   m.i14 - 15*m.b54 <= 0)

m.c57 = Constraint(expr=   m.i17 - 15*m.b54 <= 0)

m.c58 = Constraint(expr=   m.i18 - 15*m.b54 <= 0)

m.c59 = Constraint(expr=   m.i27 - 15*m.b54 <= 0)

m.c60 = Constraint(expr=   m.i29 - 15*m.b54 <= 0)

m.c61 = Constraint(expr=   m.i36 - 15*m.b54 <= 0)

m.c62 = Constraint(expr=   m.i29 - 15*m.b54 <= 0)

m.c63 = Constraint(expr=   m.i44 - 15*m.b54 <= 0)

m.c64 = Constraint(expr=   m.i13 + m.i15 + m.i16 + m.i19 + m.i20 - m.b55 >= 0)

m.c65 = Constraint(expr=   m.i13 - 15*m.b55 <= 0)

m.c66 = Constraint(expr=   m.i15 - 15*m.b55 <= 0)

m.c67 = Constraint(expr=   m.i16 - 15*m.b55 <= 0)

m.c68 = Constraint(expr=   m.i19 - 15*m.b55 <= 0)

m.c69 = Constraint(expr=   m.i20 - 15*m.b55 <= 0)

m.c70 = Constraint(expr= - m.b53 - m.b54 + m.b55 >= -1)

m.c71 = Constraint(expr= - m.b53 - m.b54 + m.b55 <= 0)

m.c72 = Constraint(expr=   m.i11 + m.i12 + m.i13 + m.i14 + m.i15 + m.i16 + m.i17 + m.i18 + m.i19 + m.i20 + m.i27 + m.i29
                         + m.i36 + m.i39 + m.i44 - 3*m.b56 >= 0)

m.c73 = Constraint(expr=   m.i11 - 15*m.b56 <= 0)

m.c74 = Constraint(expr=   m.i12 - 15*m.b56 <= 0)

m.c75 = Constraint(expr=   m.i13 - 15*m.b56 <= 0)

m.c76 = Constraint(expr=   m.i14 - 15*m.b56 <= 0)

m.c77 = Constraint(expr=   m.i15 - 15*m.b56 <= 0)

m.c78 = Constraint(expr=   m.i16 - 15*m.b56 <= 0)

m.c79 = Constraint(expr=   m.i17 - 15*m.b56 <= 0)

m.c80 = Constraint(expr=   m.i18 - 15*m.b56 <= 0)

m.c81 = Constraint(expr=   m.i19 - 15*m.b56 <= 0)

m.c82 = Constraint(expr=   m.i20 - 15*m.b56 <= 0)

m.c83 = Constraint(expr=   m.i27 - 15*m.b56 <= 0)

m.c84 = Constraint(expr=   m.i29 - 15*m.b56 <= 0)

m.c85 = Constraint(expr=   m.i36 - 15*m.b56 <= 0)

m.c86 = Constraint(expr=   m.i39 - 15*m.b56 <= 0)

m.c87 = Constraint(expr=   m.i44 - 15*m.b56 <= 0)

m.c88 = Constraint(expr=   m.i1 + m.i3 + m.i5 + m.i7 + m.i9 + m.i12 + m.i13 + m.i18 + m.i19 + m.i20 + m.i21 + m.i22
                         + m.i23 + m.i24 + m.i25 + m.i30 + m.i31 + m.i33 + m.i34 + m.i37 + m.i40 + m.i41 + m.i42
                         - 2*m.i45 == 0)

m.c89 = Constraint(expr= - m.i1 + m.i3 + 2*m.i4 - m.i5 + m.i7 - m.i9 + m.i12 + m.i13 + 2*m.i14 + 2*m.i15 + 2*m.i16
                         + m.i18 + m.i19 + m.i20 - m.i21 - m.i22 - m.i23 - m.i24 - m.i25 - m.i30 - m.i31 - m.i33 - m.i34
                         + m.i37 - m.i40 - m.i41 - m.i42 >= -2)

m.c90 = Constraint(expr=m.i1 - (m.i1 + m.i2 + m.i3 + m.i4 + m.i5 + m.i6 + m.i7 + m.i8 + m.i9 + m.i10 + m.i11 + m.i12 + 
                        m.i13 + m.i14 + m.i15 + m.i16 + m.i17 + m.i18 + m.i19 + m.i20 + m.i21 + m.i22 + m.i23 + m.i24 + 
                        m.i25 + m.i26 + m.i27 + m.i28 + m.i29 + m.i30 + m.i31 + m.i32 + m.i33 + m.i34 + m.i35 + m.i36 + 
                        m.i37 + m.i38 + m.i39 + m.i40 + m.i41 + m.i42 + m.i43 + m.i44)**2 + 2*m.i2 + 3*m.i3 + 4*m.i4 + 
                        m.i5 + 2*m.i6 + 3*m.i7 + 2*m.i8 + m.i9 + 2*m.i10 + 2*m.i11 + 3*m.i12 + 3*m.i13 + 4*m.i14 + 4*
                        m.i15 + 4*m.i16 + 2*m.i17 + 3*m.i18 + 3*m.i19 + 3*m.i20 + m.i21 + m.i22 + m.i23 + m.i24 + m.i25
                         + 2*m.i26 + 2*m.i27 + 2*m.i28 + 2*m.i29 + m.i30 + m.i31 + 2*m.i32 + m.i33 + m.i34 + 2*m.i35 + 2
                        *m.i36 + 3*m.i37 + 2*m.i38 + 2*m.i39 + m.i40 + m.i41 + m.i42 + 2*m.i43 + 2*m.i44 + m.i1 + m.i2
                         + m.i3 + m.i4 + m.i5 + m.i6 + m.i7 + m.i8 + m.i9 + m.i10 + m.i11 + m.i12 + m.i13 + m.i14 + 
                        m.i15 + m.i16 + m.i17 + m.i18 + m.i19 + m.i20 + m.i21 + m.i22 + m.i23 + m.i24 + m.i25 + m.i26 + 
                        m.i27 + m.i28 + m.i29 + m.i30 + m.i31 + m.i32 + m.i33 + m.i34 + m.i35 + m.i36 + m.i37 + m.i38 + 
                        m.i39 + m.i40 + m.i41 + m.i42 + m.i43 + m.i44 <= 0)

m.c91 = Constraint(expr=   m.i13 + m.i15 + m.i16 + m.i19 + m.i20 - m.b58 >= 0)

m.c92 = Constraint(expr=   m.i13 - 15*m.b58 <= 0)

m.c93 = Constraint(expr=   m.i15 - 15*m.b58 <= 0)

m.c94 = Constraint(expr=   m.i16 - 15*m.b58 <= 0)

m.c95 = Constraint(expr=   m.i19 - 15*m.b58 <= 0)

m.c96 = Constraint(expr=   m.i20 - 15*m.b58 <= 0)

m.c97 = Constraint(expr=   m.i1 - m.i3 - 2*m.i4 + m.i5 - m.i7 + m.i9 - m.i13 - 2*m.i15 - 2*m.i16 - m.i19 - m.i20 + m.i21
                         + m.i22 + m.i23 + m.i24 + m.i25 + m.i30 + m.i31 + m.i33 + m.i34 - m.i37 + m.i40 + m.i41 + m.i42
                         + 225*m.b58 <= 225)

m.c98 = Constraint(expr=   m.i11 + m.i12 + m.i13 + m.i14 + m.i15 + m.i16 + m.i17 + m.i18 + m.i19 + m.i20 + m.i27 + m.i29
                         + m.i36 + m.i39 + m.i44 - m.b57 >= 0)

m.c99 = Constraint(expr=   m.i11 - 15*m.b57 <= 0)

m.c100 = Constraint(expr=   m.i12 - 15*m.b57 <= 0)

m.c101 = Constraint(expr=   m.i13 - 15*m.b57 <= 0)

m.c102 = Constraint(expr=   m.i14 - 15*m.b57 <= 0)

m.c103 = Constraint(expr=   m.i15 - 15*m.b57 <= 0)

m.c104 = Constraint(expr=   m.i16 - 15*m.b57 <= 0)

m.c105 = Constraint(expr=   m.i17 - 15*m.b57 <= 0)

m.c106 = Constraint(expr=   m.i18 - 15*m.b57 <= 0)

m.c107 = Constraint(expr=   m.i19 - 15*m.b57 <= 0)

m.c108 = Constraint(expr=   m.i20 - 15*m.b57 <= 0)

m.c109 = Constraint(expr=   m.i27 - 15*m.b57 <= 0)

m.c110 = Constraint(expr=   m.i29 - 15*m.b57 <= 0)

m.c111 = Constraint(expr=   m.i36 - 15*m.b57 <= 0)

m.c112 = Constraint(expr=   m.i39 - 15*m.b57 <= 0)

m.c113 = Constraint(expr=   m.i44 - 15*m.b57 <= 0)

m.c114 = Constraint(expr=   m.i1 - m.i3 - 2*m.i4 + m.i5 - m.i7 + m.i9 + m.i21 + m.i22 + m.i23 + m.i24 + m.i25 + m.i30
                          + m.i31 + m.i33 + m.i34 - m.i37 + m.i40 + m.i41 + m.i42 + 77*m.b57 >= 2)

m.c115 = Constraint(expr=   m.i1 - m.i3 - 2*m.i4 + m.i5 - m.i7 + m.i9 + m.i21 + m.i22 + m.i23 + m.i24 + m.i25 + m.i30
                          + m.i31 + m.i33 + m.i34 - m.i37 + m.i40 + m.i41 + m.i42 - 223*m.b57 <= 2)

m.c116 = Constraint(expr=   m.i1 + 2*m.i2 + 3*m.i3 + 4*m.i4 + m.i6 + 2*m.i7 + m.i10 + m.i13 + m.i15 + 2*m.i16 + m.i19
                          + m.i21 + m.i22 + m.i23 + m.i24 + m.i25 + 2*m.i26 + 2*m.i28 + m.i30 + m.i31 + 2*m.i32 + m.i34
                          + 2*m.i35 + 3*m.i37 + m.i38 + m.i40 + m.i41 + m.i42 + 2*m.i43 - 2*m.i46 == 0)

m.c117 = Constraint(expr=   2*m.i11 + 3*m.i12 + 2*m.i13 + 4*m.i14 + 3*m.i15 + 2*m.i16 + m.i17 + 2*m.i18 + m.i19
                          + 2*m.i20 + 2*m.i27 + 2*m.i29 + 2*m.i36 + m.i39 + 2*m.i44 - 2*m.i47 == 0)

m.c118 = Constraint(expr=   m.i5 + m.i6 + m.i7 + 2*m.i8 + m.i20 + m.i33 + m.i38 - 2*m.i48 == 0)

m.c119 = Constraint(expr=   m.i17 + m.i18 + m.i19 + m.i39 - 2*m.i49 == 0)

m.c120 = Constraint(expr=   m.i9 + m.i10 - 2*m.i50 == 0)

m.c121 = Constraint(expr=   m.i1 + m.i3 + m.i4 + m.i5 + m.i6 + m.i7 + m.i8 + m.i9 + m.i10 + m.i11 + m.i12 + m.i13
                          + m.i14 + m.i15 + m.i16 + m.i17 + m.i18 + m.i19 + m.i20 + m.i21 + m.i22 + m.i23 + m.i24
                          + m.i25 + m.i26 + m.i27 + m.i28 + m.i29 + m.i30 + m.i31 + m.i32 + m.i33 + m.i34 + m.i35
                          + m.i36 + m.i37 + m.i38 + m.i39 + m.i40 + m.i41 + m.i42 + m.i43 + m.i44 >= 2)

m.c122 = Constraint(expr=   m.i1 + m.i2 - m.i3 + m.i4 + m.i5 + m.i6 + m.i7 + m.i8 + m.i9 + m.i10 + m.i11 + m.i12 + m.i13
                          + m.i14 + m.i15 + m.i16 + m.i17 + m.i18 + m.i19 + m.i20 + m.i21 + m.i22 + m.i23 + m.i24
                          + m.i25 + m.i26 + m.i27 + m.i28 + m.i29 + m.i30 + m.i31 + m.i32 + m.i33 + m.i34 + m.i35
                          + m.i36 + m.i37 + m.i38 + m.i39 + m.i40 + m.i41 + m.i42 + m.i43 + m.i44 >= 2)

m.c123 = Constraint(expr=   m.i1 + m.i2 + m.i3 - 2*m.i4 + m.i5 + m.i6 + m.i7 + m.i8 + m.i9 + m.i10 + m.i11 + m.i12
                          + m.i13 + m.i14 + m.i15 + m.i16 + m.i17 + m.i18 + m.i19 + m.i20 + m.i21 + m.i22 + m.i23
                          + m.i24 + m.i25 + m.i26 + m.i27 + m.i28 + m.i29 + m.i30 + m.i31 + m.i32 + m.i33 + m.i34
                          + m.i35 + m.i36 + m.i37 + m.i38 + m.i39 + m.i40 + m.i41 + m.i42 + m.i43 + m.i44 >= 2)

m.c124 = Constraint(expr=   m.i1 + m.i2 + m.i3 + m.i4 + m.i5 + m.i7 + m.i8 + m.i9 + m.i10 + m.i11 + m.i12 + m.i13
                          + m.i14 + m.i15 + m.i16 + m.i17 + m.i18 + m.i19 + m.i20 + m.i21 + m.i22 + m.i23 + m.i24
                          + m.i25 + m.i26 + m.i27 + m.i28 + m.i29 + m.i30 + m.i31 + m.i32 + m.i33 + m.i34 + m.i35
                          + m.i36 + m.i37 + m.i38 + m.i39 + m.i40 + m.i41 + m.i42 + m.i43 + m.i44 >= 2)

m.c125 = Constraint(expr=   m.i1 + m.i2 + m.i3 + m.i4 + m.i5 + m.i6 - m.i7 + m.i8 + m.i9 + m.i10 + m.i11 + m.i12 + m.i13
                          + m.i14 + m.i15 + m.i16 + m.i17 + m.i18 + m.i19 + m.i20 + m.i21 + m.i22 + m.i23 + m.i24
                          + m.i25 + m.i26 + m.i27 + m.i28 + m.i29 + m.i30 + m.i31 + m.i32 + m.i33 + m.i34 + m.i35
                          + m.i36 + m.i37 + m.i38 + m.i39 + m.i40 + m.i41 + m.i42 + m.i43 + m.i44 >= 2)

m.c126 = Constraint(expr=   m.i1 + m.i2 + m.i3 + m.i4 + m.i5 + m.i6 + m.i7 + m.i9 + m.i10 + m.i11 + m.i12 + m.i13
                          + m.i14 + m.i15 + m.i16 + m.i17 + m.i18 + m.i19 + m.i20 + m.i21 + m.i22 + m.i23 + m.i24
                          + m.i25 + m.i26 + m.i27 + m.i28 + m.i29 + m.i30 + m.i31 + m.i32 + m.i33 + m.i34 + m.i35
                          + m.i36 + m.i37 + m.i38 + m.i39 + m.i40 + m.i41 + m.i42 + m.i43 + m.i44 >= 2)

m.c127 = Constraint(expr=   m.i1 + m.i2 + m.i3 + m.i4 + m.i5 + m.i6 + m.i7 + m.i8 + m.i9 + m.i11 + m.i12 + m.i13 + m.i14
                          + m.i15 + m.i16 + m.i17 + m.i18 + m.i19 + m.i20 + m.i21 + m.i22 + m.i23 + m.i24 + m.i25
                          + m.i26 + m.i27 + m.i28 + m.i29 + m.i30 + m.i31 + m.i32 + m.i33 + m.i34 + m.i35 + m.i36
                          + m.i37 + m.i38 + m.i39 + m.i40 + m.i41 + m.i42 + m.i43 + m.i44 >= 2)

m.c128 = Constraint(expr=   m.i1 + m.i2 + m.i3 + m.i4 + m.i5 + m.i6 + m.i7 + m.i8 + m.i9 + m.i10 + m.i11 + m.i12 + m.i13
                          + m.i14 + m.i15 + m.i16 + m.i17 + m.i18 + m.i19 + m.i20 + m.i21 + m.i22 + m.i23 + m.i24
                          + m.i25 + m.i27 + m.i28 + m.i29 + m.i30 + m.i31 + m.i32 + m.i33 + m.i34 + m.i35 + m.i36
                          + m.i37 + m.i38 + m.i39 + m.i40 + m.i41 + m.i42 + m.i43 + m.i44 >= 2)

m.c129 = Constraint(expr=   m.i1 + m.i2 + m.i3 + m.i4 + m.i5 + m.i6 + m.i7 + m.i8 + m.i9 + m.i10 + m.i11 + m.i12 + m.i13
                          + m.i14 + m.i15 + m.i16 + m.i17 + m.i18 + m.i19 + m.i20 + m.i21 + m.i22 + m.i23 + m.i24
                          + m.i25 + m.i26 + m.i27 + m.i29 + m.i30 + m.i31 + m.i32 + m.i33 + m.i34 + m.i35 + m.i36
                          + m.i37 + m.i38 + m.i39 + m.i40 + m.i41 + m.i42 + m.i43 + m.i44 >= 2)

m.c130 = Constraint(expr=   m.i1 + m.i2 + m.i3 + m.i4 + m.i5 + m.i6 + m.i7 + m.i8 + m.i9 + m.i10 + m.i11 + m.i12 + m.i13
                          + m.i14 + m.i15 + m.i16 + m.i17 + m.i18 + m.i19 + m.i20 + m.i21 + m.i22 + m.i23 + m.i24
                          + m.i25 + m.i26 + m.i27 + m.i28 + m.i29 + m.i30 + m.i31 + m.i33 + m.i34 + m.i35 + m.i36
                          + m.i37 + m.i38 + m.i39 + m.i40 + m.i41 + m.i42 + m.i43 + m.i44 >= 2)

m.c131 = Constraint(expr=   m.i1 + m.i2 + m.i3 + m.i4 + m.i5 + m.i6 + m.i7 + m.i8 + m.i9 + m.i10 + m.i11 + m.i12 + m.i13
                          + m.i14 + m.i15 + m.i16 + m.i17 + m.i18 + m.i19 + m.i20 + m.i21 + m.i22 + m.i23 + m.i24
                          + m.i25 + m.i26 + m.i27 + m.i28 + m.i29 + m.i30 + m.i31 + m.i32 + m.i33 + m.i34 + m.i36
                          + m.i37 + m.i38 + m.i39 + m.i40 + m.i41 + m.i42 + m.i43 + m.i44 >= 2)

m.c132 = Constraint(expr=   m.i1 + m.i2 + m.i3 + m.i4 + m.i5 + m.i6 + m.i7 + m.i8 + m.i9 + m.i10 + m.i11 + m.i12 + m.i13
                          + m.i14 + m.i15 + m.i16 + m.i17 + m.i18 + m.i19 + m.i20 + m.i21 + m.i22 + m.i23 + m.i24
                          + m.i25 + m.i26 + m.i27 + m.i28 + m.i29 + m.i30 + m.i31 + m.i32 + m.i33 + m.i34 + m.i35
                          + m.i36 - m.i37 + m.i38 + m.i39 + m.i40 + m.i41 + m.i42 + m.i43 + m.i44 >= 2)

m.c133 = Constraint(expr=   m.i1 + m.i2 + m.i3 + m.i4 + m.i5 + m.i6 + m.i7 + m.i8 + m.i9 + m.i10 + m.i11 + m.i12 + m.i13
                          + m.i14 + m.i15 + m.i16 + m.i17 + m.i18 + m.i19 + m.i20 + m.i21 + m.i22 + m.i23 + m.i24
                          + m.i25 + m.i26 + m.i27 + m.i28 + m.i29 + m.i30 + m.i31 + m.i32 + m.i33 + m.i34 + m.i35
                          + m.i36 + m.i37 + m.i39 + m.i40 + m.i41 + m.i42 + m.i43 + m.i44 >= 2)

m.c134 = Constraint(expr=   m.i1 + m.i2 + m.i3 + m.i4 + m.i5 + m.i6 + m.i7 + m.i8 + m.i9 + m.i10 + m.i11 + m.i12 + m.i13
                          + m.i14 + m.i15 + m.i16 + m.i17 + m.i18 + m.i19 + m.i20 + m.i21 + m.i22 + m.i23 + m.i24
                          + m.i25 + m.i26 + m.i27 + m.i28 + m.i29 + m.i30 + m.i31 + m.i32 + m.i33 + m.i34 + m.i35
                          + m.i36 + m.i37 + m.i38 + m.i39 + m.i40 + m.i41 + m.i42 + m.i44 >= 2)

m.c135 = Constraint(expr=   m.i2 + m.i3 + m.i4 + m.i6 + m.i7 + m.i8 + m.i10 + m.i16 + m.i26 + m.i28 + m.i32 + m.i35
                          + m.i37 + m.i38 + m.i43 - m.b59 >= 0)

m.c136 = Constraint(expr=   m.i2 - 15*m.b59 <= 0)

m.c137 = Constraint(expr=   m.i3 - 15*m.b59 <= 0)

m.c138 = Constraint(expr=   m.i4 - 15*m.b59 <= 0)

m.c139 = Constraint(expr=   m.i6 - 15*m.b59 <= 0)

m.c140 = Constraint(expr=   m.i7 - 15*m.b59 <= 0)

m.c141 = Constraint(expr=   m.i8 - 15*m.b59 <= 0)

m.c142 = Constraint(expr=   m.i10 - 15*m.b59 <= 0)

m.c143 = Constraint(expr=   m.i16 - 15*m.b59 <= 0)

m.c144 = Constraint(expr=   m.i26 - 15*m.b59 <= 0)

m.c145 = Constraint(expr=   m.i28 - 15*m.b59 <= 0)

m.c146 = Constraint(expr=   m.i32 - 15*m.b59 <= 0)

m.c147 = Constraint(expr=   m.i35 - 15*m.b59 <= 0)

m.c148 = Constraint(expr=   m.i37 - 15*m.b59 <= 0)

m.c149 = Constraint(expr=   m.i38 - 15*m.b59 <= 0)

m.c150 = Constraint(expr=   m.i43 - 15*m.b59 <= 0)

m.c151 = Constraint(expr=   m.i1 - 2*m.i2 - 3*m.i3 - 4*m.i4 - m.i6 - 2*m.i7 - m.i10 + m.i13 + m.i15 - 2*m.i16 + m.i19
                          + m.i21 + m.i22 + m.i23 + m.i24 + m.i25 - 2*m.i26 - 2*m.i28 + m.i30 + m.i31 - 2*m.i32 + m.i34
                          - 2*m.i35 - 3*m.i37 - m.i38 + m.i40 + m.i41 + m.i42 - 2*m.i43 - 225*m.b56 + 225*m.b59 <= 225)

m.c152 = Constraint(expr=   m.i5 - m.i6 - m.i7 - 2*m.i8 + m.i20 + m.i33 - m.i38 - 45*m.b56 + 45*m.b59 <= 45)

m.c153 = Constraint(expr=   m.i9 - m.i10 - 15*m.b56 + 15*m.b59 <= 15)

m.c154 = Constraint(expr= - m.i1 + m.i3 + 2*m.i4 - m.i5 + m.i7 - m.i9 - m.i13 - m.i15 - m.i19 - m.i20 - m.i21 - m.i22
                          - m.i23 - m.i24 - m.i25 - m.i30 - m.i31 - m.i33 - m.i34 + m.i37 - m.i40 - m.i41 - m.i42
                          - 525*m.b56 <= -2)

m.c155 = Constraint(expr= - m.i1 + m.i3 + 2*m.i4 - m.i5 + m.i7 - m.i9 - m.i13 - m.i15 - m.i19 - m.i20 - m.i21 - m.i22
                          - m.i23 - m.i24 - m.i25 - m.i30 - m.i31 - m.i33 - m.i34 + m.i37 - m.i40 - m.i41 - m.i42
                          + 525*m.b56 >= -2)

m.c156 = Constraint(expr=   m.i11 + m.i12 + m.i13 + m.i14 + m.i15 + m.i16 + m.i17 + m.i18 + m.i19 + m.i20 + m.i27
                          + m.i29 + m.i36 + m.i39 + m.i44 - m.i51 == 0)

m.c157 = Constraint(expr=   m.i17 + m.i18 + m.i19 + m.i39 - m.i52 == 0)

m.c158 = Constraint(expr=m.i51 - m.i51**2 + 2*m.i47 - m.b60 <= -1)

m.c159 = Constraint(expr=m.i52 - m.i52**2 + 2*m.i49 <= 0)

m.c160 = Constraint(expr=m.b60*m.i1 + 2*m.b60*m.i2 + 3*m.b60*m.i3 + 4*m.b60*m.i4 + m.b60*m.i6 + 2*m.b60*m.i7 + m.b60*
                         m.i10 + m.b60*m.i21 + m.b60*m.i22 + m.b60*m.i23 + m.b60*m.i24 + m.b60*m.i25 + 2*m.b60*m.i26 + 2
                         *m.b60*m.i28 + m.b60*m.i30 + m.b60*m.i31 + 2*m.b60*m.i32 + m.b60*m.i34 + 2*m.b60*m.i35 + 3*
                         m.b60*m.i37 + m.b60*m.i38 + m.b60*m.i40 + m.b60*m.i41 + m.b60*m.i42 + 2*m.b60*m.i43 - m.b60*
                         m.i13 - m.b60*m.i15 - 2*m.b60*m.i16 - m.b60*m.i19 >= 0)

m.c161 = Constraint(expr=m.i7*m.i8 + m.i6*m.i8 + m.i20*m.i8 + m.i7*m.i38 + m.i6*m.i38 + m.i20*m.i38 - m.i7*m.i33 - m.i6*
                         m.i33 - m.i20*m.i33 >= 0)

m.c162 = Constraint(expr=m.i28*m.i1 + m.i28*m.i2 + m.i28*m.i3 + m.i28*m.i4 + m.i28*m.i6 + m.i28*m.i7 + m.i28*m.i10 + 
                         m.i28*m.i13 + m.i28*m.i15 + m.i28*m.i16 + m.i28*m.i19 + m.i28*m.i21 + m.i28*m.i22 + m.i28*m.i23
                          + m.i28*m.i24 + m.i28*m.i26 + m.i28*m.i30 + m.i28*m.i31 + m.i28*m.i32 + m.i28*m.i34 + m.i28*
                         m.i35 + m.i28*m.i37 + m.i28*m.i38 + m.i28*m.i40 + m.i28*m.i41 + m.i28*m.i42 + m.i28*m.i43 - 
                         m.i28*m.i25 >= 0)

m.c163 = Constraint(expr=m.i2*m.i28*m.i26 + m.i3*m.i28*m.i26 + m.i4*m.i28*m.i26 + m.i7*m.i28*m.i26 + m.i16*m.i28*m.i26
                          + m.i32*m.i28*m.i26 + m.i35*m.i28*m.i26 + m.i37*m.i28*m.i26 + m.i43*m.i28*m.i26 - 0.5*m.i28*
                         m.i26*m.i26 - 0.5*m.i28*m.i26*m.i28 + 0.5*m.i28*m.i26*((m.i26 - m.i28)*(m.i26 - m.i28))**0.5
                          >= 0)
