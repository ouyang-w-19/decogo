#  NLP written by GAMS Convert at 04/21/18 13:51:42
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         71       70        0        1        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         98       98        0        0        0        0        0        0
#  FX      1        1        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        226      191       35        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(12.32657617084,12.32657617084),initialize=12.32657617084)
m.x2 = Var(within=Reals,bounds=(10.9,None),initialize=14.6486885348509)
m.x3 = Var(within=Reals,bounds=(10.9,None),initialize=16.9818448409483)
m.x4 = Var(within=Reals,bounds=(10.9,None),initialize=19.6866124578966)
m.x5 = Var(within=Reals,bounds=(10.9,None),initialize=22.8221794332309)
m.x6 = Var(within=Reals,bounds=(10.9,None),initialize=26.4571609359673)
m.x7 = Var(within=Reals,bounds=(10.9,None),initialize=30.6711007526496)
m.x8 = Var(within=Reals,bounds=(10.9,None),initialize=35.5562119327899)
m.x9 = Var(within=Reals,bounds=(10.9,None),initialize=41.2193946739997)
m.x10 = Var(within=Reals,bounds=(1.0317041301,None),initialize=1.0317041301)
m.x11 = Var(within=Reals,bounds=(1.0317041301,None),initialize=1.0317041301)
m.x12 = Var(within=Reals,bounds=(1.0317041301,None),initialize=1.0317041301)
m.x13 = Var(within=Reals,bounds=(1.0317041301,None),initialize=1.0317041301)
m.x14 = Var(within=Reals,bounds=(1.0317041301,None),initialize=1.0317041301)
m.x15 = Var(within=Reals,bounds=(1.0317041301,None),initialize=1.0317041301)
m.x16 = Var(within=Reals,bounds=(1.0317041301,None),initialize=1.0317041301)
m.x17 = Var(within=Reals,bounds=(1.0317041301,None),initialize=1.0317041301)
m.x18 = Var(within=Reals,bounds=(4.25,None),initialize=4.926914815775)
m.x19 = Var(within=Reals,bounds=(4.25,None),initialize=5.71164461221252)
m.x20 = Var(within=Reals,bounds=(4.25,None),initialize=6.62136152055325)
m.x21 = Var(within=Reals,bounds=(4.25,None),initialize=7.67597274734501)
m.x22 = Var(within=Reals,bounds=(4.25,None),initialize=8.89855620103042)
m.x23 = Var(within=Reals,bounds=(4.25,None),initialize=10.3158655025561)
m.x24 = Var(within=Reals,bounds=(4.25,None),initialize=11.958915431079)
m.x25 = Var(within=Reals,bounds=(4.25,None),initialize=13.8636606159961)
m.x26 = Var(within=Reals,bounds=(4.25,None),initialize=16.0717823270182)
m.x27 = Var(within=Reals,bounds=(0.508311836408595,None),initialize=0.508311836408595)
m.x28 = Var(within=Reals,bounds=(0.589272733608307,None),initialize=0.589272733608307)
m.x29 = Var(within=Reals,bounds=(0.683128602764001,None),initialize=0.683128602764001)
m.x30 = Var(within=Reals,bounds=(0.79193327859709,None),initialize=0.79193327859709)
m.x31 = Var(within=Reals,bounds=(0.918067718453005,None),initialize=0.918067718453005)
m.x32 = Var(within=Reals,bounds=(1.06429210445432,None),initialize=1.06429210445432)
m.x33 = Var(within=Reals,bounds=(1.23380624417608,None),initialize=1.23380624417608)
m.x34 = Var(within=Reals,bounds=(1.43031959158279,None),initialize=1.43031959158279)
m.x35 = Var(within=Reals,bounds=(2.5,None),initialize=2.89818518575)
m.x36 = Var(within=Reals,bounds=(2.5,None),initialize=3.35979094836031)
m.x37 = Var(within=Reals,bounds=(2.5,None),initialize=3.89491854150191)
m.x38 = Var(within=Reals,bounds=(2.5,None),initialize=4.51527808667354)
m.x39 = Var(within=Reals,bounds=(2.5,None),initialize=5.23444482413554)
m.x40 = Var(within=Reals,bounds=(2.5,None),initialize=6.06815617797415)
m.x41 = Var(within=Reals,bounds=(2.5,None),initialize=7.03465613592881)
m.x42 = Var(within=Reals,bounds=(2.5,None),initialize=8.15509447999769)
m.x43 = Var(within=Reals,bounds=(2.5,None),initialize=9.45398960412836)
m.x44 = Var(within=Reals,bounds=(0.257926032525,None),initialize=0.257926032525)
m.x45 = Var(within=Reals,bounds=(0.299006962593291,None),initialize=0.299006962593291)
m.x46 = Var(within=Reals,bounds=(0.346631019769593,None),initialize=0.346631019769593)
m.x47 = Var(within=Reals,bounds=(0.401840354567059,None),initialize=0.401840354567059)
m.x48 = Var(within=Reals,bounds=(0.465843105057112,None),initialize=0.465843105057112)
m.x49 = Var(within=Reals,bounds=(0.540039834384121,None),initialize=0.540039834384121)
m.x50 = Var(within=Reals,bounds=(0.626054179090777,None),initialize=0.626054179090777)
m.x51 = Var(within=Reals,bounds=(0.725768378927107,None),initialize=0.725768378927107)
m.x52 = Var(within=Reals,bounds=(0.841364465636933,None),initialize=0.841364465636933)
m.x53 = Var(within=Reals,bounds=(50,None),initialize=57.963703715)
m.x54 = Var(within=Reals,bounds=(50,None),initialize=67.1958189672061)
m.x55 = Var(within=Reals,bounds=(50,None),initialize=77.8983708300382)
m.x56 = Var(within=Reals,bounds=(50,None),initialize=90.3055617334707)
m.x57 = Var(within=Reals,bounds=(50,None),initialize=104.688896482711)
m.x58 = Var(within=Reals,bounds=(50,None),initialize=121.363123559483)
m.x59 = Var(within=Reals,bounds=(50,None),initialize=140.693122718576)
m.x60 = Var(within=Reals,bounds=(50,None),initialize=163.101889599954)
m.x61 = Var(within=Reals,bounds=(50,None),initialize=189.079792082567)
m.x62 = Var(within=Reals,bounds=(5.1585206505,None),initialize=5.1585206505)
m.x63 = Var(within=Reals,bounds=(5.98013925186582,None),initialize=5.98013925186582)
m.x64 = Var(within=Reals,bounds=(6.93262039539185,None),initialize=6.93262039539185)
m.x65 = Var(within=Reals,bounds=(8.03680709134119,None),initialize=8.03680709134119)
m.x66 = Var(within=Reals,bounds=(9.31686210114223,None),initialize=9.31686210114223)
m.x67 = Var(within=Reals,bounds=(10.8007966876824,None),initialize=10.8007966876824)
m.x68 = Var(within=Reals,bounds=(12.5210835818155,None),initialize=12.5210835818155)
m.x69 = Var(within=Reals,bounds=(14.5153675785421,None),initialize=14.5153675785421)
m.x70 = Var(within=Reals,bounds=(16.8272893127387,None),initialize=16.8272893127387)
m.x71 = Var(within=Reals,bounds=(3.2,None),initialize=3.70967703776)
m.x72 = Var(within=Reals,bounds=(3.2,None),initialize=4.30053241390119)
m.x73 = Var(within=Reals,bounds=(3.2,None),initialize=4.98549573312245)
m.x74 = Var(within=Reals,bounds=(3.2,None),initialize=5.77955595094213)
m.x75 = Var(within=Reals,bounds=(3.2,None),initialize=6.70008937489349)
m.x76 = Var(within=Reals,bounds=(3.2,None),initialize=7.76723990780692)
m.x77 = Var(within=Reals,bounds=(3.2,None),initialize=9.00435985398888)
m.x78 = Var(within=Reals,bounds=(3.2,None),initialize=10.438520934397)
m.x79 = Var(within=Reals,bounds=(3.2,None),initialize=12.1011066932843)
m.x80 = Var(within=Reals,bounds=(0.7,None),initialize=0.81149185201)
m.x81 = Var(within=Reals,bounds=(0.7,None),initialize=0.940741465540885)
m.x82 = Var(within=Reals,bounds=(0.7,None),initialize=1.09057719162054)
m.x83 = Var(within=Reals,bounds=(0.7,None),initialize=1.26427786426859)
m.x84 = Var(within=Reals,bounds=(0.7,None),initialize=1.46564455075795)
m.x85 = Var(within=Reals,bounds=(0.7,None),initialize=1.69908372983276)
m.x86 = Var(within=Reals,bounds=(0.7,None),initialize=1.96970371806007)
m.x87 = Var(within=Reals,bounds=(0.7,None),initialize=2.28342645439935)
m.x88 = Var(within=Reals,bounds=(0.7,None),initialize=2.64711708915594)
m.x89 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x90 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x91 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x92 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x93 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x94 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x95 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x96 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x97 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=-(0.8153726976*log(m.x71) + 0.664832635991501*log(m.x72) + 0.542086379860909*log(m.x73) + 
                       0.442002433879407*log(m.x74) + 0.360396716858018*log(m.x75) + 0.293857643230706*log(m.x76) + 
                       0.239603499271399*log(m.x77) + 0.19536615155532*log(m.x78) + 3.98240565033479*log(m.x79))
                       , sense=minimize)

m.c1 = Constraint(expr=   m.x10 - 4.91287681*m.x80 == 0)

m.c2 = Constraint(expr=   m.x11 - 4.91287681*m.x81 == 0)

m.c3 = Constraint(expr=   m.x12 - 4.91287681*m.x82 == 0)

m.c4 = Constraint(expr=   m.x13 - 4.91287681*m.x83 == 0)

m.c5 = Constraint(expr=   m.x14 - 4.91287681*m.x84 == 0)

m.c6 = Constraint(expr=   m.x15 - 4.91287681*m.x85 == 0)

m.c7 = Constraint(expr=   m.x16 - 4.91287681*m.x86 == 0)

m.c8 = Constraint(expr=   m.x17 - 4.91287681*m.x87 == 0)

m.c9 = Constraint(expr=-(0.820744282617518*m.x10**(-0.342222222222222) + 0.306708090151268*m.x45**(-0.427777777777778)*
                       m.x63**(-0.794444444444445))**(-0.818181818181818) + m.x27 == 0)

m.c10 = Constraint(expr=-(0.7206494796327*m.x11**(-0.342222222222222) + 0.306708090151268*m.x46**(-0.427777777777778)*
                        m.x64**(-0.794444444444445))**(-0.818181818181818) + m.x28 == 0)

m.c11 = Constraint(expr=-(0.632761852252708*m.x12**(-0.342222222222222) + 0.306708090151268*m.x47**(-0.427777777777778)*
                        m.x65**(-0.794444444444445))**(-0.818181818181818) + m.x29 == 0)

m.c12 = Constraint(expr=-(0.555592660485018*m.x13**(-0.342222222222222) + 0.306708090151268*m.x48**(-0.427777777777778)*
                        m.x66**(-0.794444444444445))**(-0.818181818181818) + m.x30 == 0)

m.c13 = Constraint(expr=-(0.487834725317074*m.x14**(-0.342222222222222) + 0.306708090151268*m.x49**(-0.427777777777778)*
                        m.x67**(-0.794444444444445))**(-0.818181818181818) + m.x31 == 0)

m.c14 = Constraint(expr=-(0.428340286240339*m.x15**(-0.342222222222222) + 0.306708090151268*m.x50**(-0.427777777777778)*
                        m.x68**(-0.794444444444445))**(-0.818181818181818) + m.x32 == 0)

m.c15 = Constraint(expr=-(0.376101559185243*m.x16**(-0.342222222222222) + 0.306708090151268*m.x51**(-0.427777777777778)*
                        m.x69**(-0.794444444444445))**(-0.818181818181818) + m.x33 == 0)

m.c16 = Constraint(expr=-(0.330233665535262*m.x17**(-0.342222222222222) + 0.306708090151268*m.x52**(-0.427777777777778)*
                        m.x70**(-0.794444444444445))**(-0.818181818181818) + m.x34 == 0)

m.c17 = Constraint(expr= - m.x35 + m.x44 == -2.038431744)

m.c18 = Constraint(expr=   0.8153726976*m.x35 - m.x36 + m.x45 == 0)

m.c19 = Constraint(expr=   0.8153726976*m.x36 - m.x37 + m.x46 == 0)

m.c20 = Constraint(expr=   0.8153726976*m.x37 - m.x38 + m.x47 == 0)

m.c21 = Constraint(expr=   0.8153726976*m.x38 - m.x39 + m.x48 == 0)

m.c22 = Constraint(expr=   0.8153726976*m.x39 - m.x40 + m.x49 == 0)

m.c23 = Constraint(expr=   0.8153726976*m.x40 - m.x41 + m.x50 == 0)

m.c24 = Constraint(expr=   0.8153726976*m.x41 - m.x42 + m.x51 == 0)

m.c25 = Constraint(expr=   0.8153726976*m.x42 - m.x43 + m.x52 == 0)

m.c26 = Constraint(expr= - m.x53 + m.x62 == -40.76863488)

m.c27 = Constraint(expr=   0.8153726976*m.x53 - m.x54 + m.x63 == 0)

m.c28 = Constraint(expr=   0.8153726976*m.x54 - m.x55 + m.x64 == 0)

m.c29 = Constraint(expr=   0.8153726976*m.x55 - m.x56 + m.x65 == 0)

m.c30 = Constraint(expr=   0.8153726976*m.x56 - m.x57 + m.x66 == 0)

m.c31 = Constraint(expr=   0.8153726976*m.x57 - m.x58 + m.x67 == 0)

m.c32 = Constraint(expr=   0.8153726976*m.x58 - m.x59 + m.x68 == 0)

m.c33 = Constraint(expr=   0.8153726976*m.x59 - m.x60 + m.x69 == 0)

m.c34 = Constraint(expr=   0.8153726976*m.x60 - m.x61 + m.x70 == 0)

m.c35 = Constraint(expr= - 0.8153726976*m.x1 + m.x2 - m.x10 == 0)

m.c36 = Constraint(expr= - 0.8153726976*m.x2 + m.x3 - m.x11 == 0)

m.c37 = Constraint(expr= - 0.8153726976*m.x3 + m.x4 - m.x12 == 0)

m.c38 = Constraint(expr= - 0.8153726976*m.x4 + m.x5 - m.x13 == 0)

m.c39 = Constraint(expr= - 0.8153726976*m.x5 + m.x6 - m.x14 == 0)

m.c40 = Constraint(expr= - 0.8153726976*m.x6 + m.x7 - m.x15 == 0)

m.c41 = Constraint(expr= - 0.8153726976*m.x7 + m.x8 - m.x16 == 0)

m.c42 = Constraint(expr= - 0.8153726976*m.x8 + m.x9 - m.x17 == 0)

m.c43 = Constraint(expr=-(0.612508399277048 + 0.306708090151268*m.x44**(-0.427777777777778)*m.x62**(-0.794444444444445))
                        **(-0.818181818181818) + m.x18 == 3.4653339648)

m.c44 = Constraint(expr= - 0.8153726976*m.x18 + m.x19 - m.x27 == 0)

m.c45 = Constraint(expr= - 0.8153726976*m.x19 + m.x20 - m.x28 == 0)

m.c46 = Constraint(expr= - 0.8153726976*m.x20 + m.x21 - m.x29 == 0)

m.c47 = Constraint(expr= - 0.8153726976*m.x21 + m.x22 - m.x30 == 0)

m.c48 = Constraint(expr= - 0.8153726976*m.x22 + m.x23 - m.x31 == 0)

m.c49 = Constraint(expr= - 0.8153726976*m.x23 + m.x24 - m.x32 == 0)

m.c50 = Constraint(expr= - 0.8153726976*m.x24 + m.x25 - m.x33 == 0)

m.c51 = Constraint(expr= - 0.8153726976*m.x25 + m.x26 - m.x34 == 0)

m.c52 = Constraint(expr= - 52.550502505*m.x35 - 4.9683636144*m.x53 + 1000*m.x89 == 0)

m.c53 = Constraint(expr= - 55.2311062705602*m.x36 - 5.48547488997641*m.x54 + 1000*m.x90 == 0)

m.c54 = Constraint(expr= - 58.0484477684999*m.x37 - 6.05640752245858*m.x55 + 1000*m.x91 == 0)

m.c55 = Constraint(expr= - 61.0095019973984*m.x38 - 6.68676328190259*m.x56 + 1000*m.x92 == 0)

m.c56 = Constraint(expr= - 64.1215997508617*m.x39 - 7.38272697509128*m.x57 + 1000*m.x93 == 0)

m.c57 = Constraint(expr= - 67.3924457666453*m.x40 - 8.15112712846509*m.x58 + 1000*m.x94 == 0)

m.c58 = Constraint(expr= - 70.8301378015635*m.x41 - 8.99950298698105*m.x59 + 1000*m.x95 == 0)

m.c59 = Constraint(expr= - 74.4431866794111*m.x42 - 9.93617848626683*m.x60 + 1000*m.x96 == 0)

m.c60 = Constraint(expr= - 78.2405373615315*m.x43 - 10.970343923856*m.x61 + 1000*m.x97 == 0)

m.c61 = Constraint(expr=   m.x18 - m.x71 - m.x80 - m.x89 == 0)

m.c62 = Constraint(expr=   m.x19 - m.x72 - m.x81 - m.x90 == 0)

m.c63 = Constraint(expr=   m.x20 - m.x73 - m.x82 - m.x91 == 0)

m.c64 = Constraint(expr=   m.x21 - m.x74 - m.x83 - m.x92 == 0)

m.c65 = Constraint(expr=   m.x22 - m.x75 - m.x84 - m.x93 == 0)

m.c66 = Constraint(expr=   m.x23 - m.x76 - m.x85 - m.x94 == 0)

m.c67 = Constraint(expr=   m.x24 - m.x77 - m.x86 - m.x95 == 0)

m.c68 = Constraint(expr=   m.x25 - m.x78 - m.x87 - m.x96 == 0)

m.c69 = Constraint(expr=   m.x26 - m.x79 - m.x88 - m.x97 == 0)

m.c70 = Constraint(expr=   0.07*m.x9 - m.x88 <= 0)
