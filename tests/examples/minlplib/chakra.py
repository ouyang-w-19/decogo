#  NLP written by GAMS Convert at 04/21/18 13:51:14
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         42       42        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         63       63        0        0        0        0        0        0
#  FX      2        2        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        143      102       41        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(1,None),initialize=2.65787165646338)
m.x2 = Var(within=Reals,bounds=(1,None),initialize=2.82088780167558)
m.x3 = Var(within=Reals,bounds=(1,None),initialize=2.99388978021114)
m.x4 = Var(within=Reals,bounds=(1,None),initialize=3.17748858499683)
m.x5 = Var(within=Reals,bounds=(1,None),initialize=3.37233255315755)
m.x6 = Var(within=Reals,bounds=(1,None),initialize=3.57910964624529)
m.x7 = Var(within=Reals,bounds=(1,None),initialize=3.79854986956959)
m.x8 = Var(within=Reals,bounds=(1,None),initialize=4.03142783910829)
m.x9 = Var(within=Reals,bounds=(1,None),initialize=4.27856550499249)
m.x10 = Var(within=Reals,bounds=(1,None),initialize=4.54083504110911)
m.x11 = Var(within=Reals,bounds=(1,None),initialize=4.81916191094403)
m.x12 = Var(within=Reals,bounds=(1,None),initialize=5.11452812040594)
m.x13 = Var(within=Reals,bounds=(1,None),initialize=5.42797566902516)
m.x14 = Var(within=Reals,bounds=(1,None),initialize=5.76061021161472)
m.x15 = Var(within=Reals,bounds=(1,None),initialize=6.11360494321835)
m.x16 = Var(within=Reals,bounds=(1,None),initialize=6.48820472094886)
m.x17 = Var(within=Reals,bounds=(1,None),initialize=6.88573043715017)
m.x18 = Var(within=Reals,bounds=(1,None),initialize=7.30758365919495)
m.x19 = Var(within=Reals,bounds=(1,None),initialize=7.75525155216026)
m.x20 = Var(within=Reals,bounds=(1,None),initialize=8.23031210161431)
m.x21 = Var(within=Reals,bounds=(4.275,4.275),initialize=4.275)
m.x22 = Var(within=Reals,bounds=(1,None),initialize=4.5315)
m.x23 = Var(within=Reals,bounds=(1,None),initialize=4.80339)
m.x24 = Var(within=Reals,bounds=(1,None),initialize=5.0915934)
m.x25 = Var(within=Reals,bounds=(1,None),initialize=5.397089004)
m.x26 = Var(within=Reals,bounds=(1,None),initialize=5.72091434424)
m.x27 = Var(within=Reals,bounds=(1,None),initialize=6.0641692048944)
m.x28 = Var(within=Reals,bounds=(1,None),initialize=6.42801935718807)
m.x29 = Var(within=Reals,bounds=(1,None),initialize=6.81370051861935)
m.x30 = Var(within=Reals,bounds=(1,None),initialize=7.22252254973651)
m.x31 = Var(within=Reals,bounds=(1,None),initialize=7.6558739027207)
m.x32 = Var(within=Reals,bounds=(1,None),initialize=8.11522633688395)
m.x33 = Var(within=Reals,bounds=(1,None),initialize=8.60213991709698)
m.x34 = Var(within=Reals,bounds=(1,None),initialize=9.1182683121228)
m.x35 = Var(within=Reals,bounds=(1,None),initialize=9.66536441085017)
m.x36 = Var(within=Reals,bounds=(1,None),initialize=10.2452862755012)
m.x37 = Var(within=Reals,bounds=(1,None),initialize=10.8600034520313)
m.x38 = Var(within=Reals,bounds=(1,None),initialize=11.5116036591531)
m.x39 = Var(within=Reals,bounds=(1,None),initialize=12.2022998787023)
m.x40 = Var(within=Reals,bounds=(1,None),initialize=12.9344378714245)
m.x41 = Var(within=Reals,bounds=(13.7105041437099,13.7105041437099),initialize=13.7105041437099)
m.x42 = Var(within=Reals,bounds=(1,None),initialize=15)
m.x43 = Var(within=Reals,bounds=(1,None),initialize=15.8671283435366)
m.x44 = Var(within=Reals,bounds=(1,None),initialize=16.7843841246842)
m.x45 = Var(within=Reals,bounds=(1,None),initialize=17.7546651382389)
m.x46 = Var(within=Reals,bounds=(1,None),initialize=18.7810366963301)
m.x47 = Var(within=Reals,bounds=(1,None),initialize=19.866741312356)
m.x48 = Var(within=Reals,bounds=(1,None),initialize=21.0152089447329)
m.x49 = Var(within=Reals,bounds=(1,None),initialize=22.2300678328211)
m.x50 = Var(within=Reals,bounds=(1,None),initialize=23.5151559592598)
m.x51 = Var(within=Reals,bounds=(1,None),initialize=24.8745331749237)
m.x52 = Var(within=Reals,bounds=(1,None),initialize=26.3124940248049)
m.x53 = Var(within=Reals,bounds=(1,None),initialize=27.8335813153413)
m.x54 = Var(within=Reals,bounds=(1,None),initialize=29.4426004660523)
m.x55 = Var(within=Reals,bounds=(1,None),initialize=31.1446346908215)
m.x56 = Var(within=Reals,bounds=(1,None),initialize=32.9450610567885)
m.x57 = Var(within=Reals,bounds=(1,None),initialize=34.8495674715809)
m.x58 = Var(within=Reals,bounds=(1,None),initialize=36.8641706525542)
m.x59 = Var(within=Reals,bounds=(1,None),initialize=38.9952351348075)
m.x60 = Var(within=Reals,bounds=(1,None),initialize=41.2494933780253)
m.x61 = Var(within=Reals,bounds=(1,None),initialize=43.6340670356661)
m.x62 = Var(within=Reals,bounds=(1,None),initialize=46.156489453693)

m.obj = Objective(expr=-(10*m.x1**0.1 + 9.70873786407767*m.x2**0.1 + 9.42595909133755*m.x3**0.1 + 9.1514165935316*m.x4**
                       0.1 + 8.88487047915689*m.x5**0.1 + 8.62608784384164*m.x6**0.1 + 8.37484256683654*m.x7**0.1 + 
                       8.13091511343354*m.x8**0.1 + 7.89409234313936*m.x9**0.1 + 7.66416732343627*m.x10**0.1 + 
                       7.44093914896725*m.x11**0.1 + 7.22421276598762*m.x12**0.1 + 7.01379880192973*m.x13**0.1 + 
                       6.80951339993178*m.x14**0.1 + 6.61117805818619*m.x15**0.1 + 6.41861947396717*m.x16**0.1 + 
                       6.23166939220114*m.x17**0.1 + 6.05016445844771*m.x18**0.1 + 5.87394607616282*m.x19**0.1 + 
                       5.70286026811925*m.x20**0.1), sense=minimize)

m.c1 = Constraint(expr=   m.x1 - m.x21 - 0.95*m.x42 + m.x43 == 0)

m.c2 = Constraint(expr=   m.x2 - m.x22 - 0.95*m.x43 + m.x44 == 0)

m.c3 = Constraint(expr=   m.x3 - m.x23 - 0.95*m.x44 + m.x45 == 0)

m.c4 = Constraint(expr=   m.x4 - m.x24 - 0.95*m.x45 + m.x46 == 0)

m.c5 = Constraint(expr=   m.x5 - m.x25 - 0.95*m.x46 + m.x47 == 0)

m.c6 = Constraint(expr=   m.x6 - m.x26 - 0.95*m.x47 + m.x48 == 0)

m.c7 = Constraint(expr=   m.x7 - m.x27 - 0.95*m.x48 + m.x49 == 0)

m.c8 = Constraint(expr=   m.x8 - m.x28 - 0.95*m.x49 + m.x50 == 0)

m.c9 = Constraint(expr=   m.x9 - m.x29 - 0.95*m.x50 + m.x51 == 0)

m.c10 = Constraint(expr=   m.x10 - m.x30 - 0.95*m.x51 + m.x52 == 0)

m.c11 = Constraint(expr=   m.x11 - m.x31 - 0.95*m.x52 + m.x53 == 0)

m.c12 = Constraint(expr=   m.x12 - m.x32 - 0.95*m.x53 + m.x54 == 0)

m.c13 = Constraint(expr=   m.x13 - m.x33 - 0.95*m.x54 + m.x55 == 0)

m.c14 = Constraint(expr=   m.x14 - m.x34 - 0.95*m.x55 + m.x56 == 0)

m.c15 = Constraint(expr=   m.x15 - m.x35 - 0.95*m.x56 + m.x57 == 0)

m.c16 = Constraint(expr=   m.x16 - m.x36 - 0.95*m.x57 + m.x58 == 0)

m.c17 = Constraint(expr=   m.x17 - m.x37 - 0.95*m.x58 + m.x59 == 0)

m.c18 = Constraint(expr=   m.x18 - m.x38 - 0.95*m.x59 + m.x60 == 0)

m.c19 = Constraint(expr=   m.x19 - m.x39 - 0.95*m.x60 + m.x61 == 0)

m.c20 = Constraint(expr=   m.x20 - m.x40 - 0.95*m.x61 + m.x62 == 0)

m.c21 = Constraint(expr=-0.560877056310648*m.x42**0.75 + m.x21 == 0)

m.c22 = Constraint(expr=-0.569991308475696*m.x43**0.75 + m.x22 == 0)

m.c23 = Constraint(expr=-0.579253667238426*m.x44**0.75 + m.x23 == 0)

m.c24 = Constraint(expr=-0.58866653933105*m.x45**0.75 + m.x24 == 0)

m.c25 = Constraint(expr=-0.59823237059518*m.x46**0.75 + m.x25 == 0)

m.c26 = Constraint(expr=-0.607953646617352*m.x47**0.75 + m.x26 == 0)

m.c27 = Constraint(expr=-0.617832893374884*m.x48**0.75 + m.x27 == 0)

m.c28 = Constraint(expr=-0.627872677892226*m.x49**0.75 + m.x28 == 0)

m.c29 = Constraint(expr=-0.638075608907974*m.x50**0.75 + m.x29 == 0)

m.c30 = Constraint(expr=-0.648444337552729*m.x51**0.75 + m.x30 == 0)

m.c31 = Constraint(expr=-0.658981558037961*m.x52**0.75 + m.x31 == 0)

m.c32 = Constraint(expr=-0.669690008356078*m.x53**0.75 + m.x32 == 0)

m.c33 = Constraint(expr=-0.680572470991864*m.x54**0.75 + m.x33 == 0)

m.c34 = Constraint(expr=-0.691631773645482*m.x55**0.75 + m.x34 == 0)

m.c35 = Constraint(expr=-0.702870789967221*m.x56**0.75 + m.x35 == 0)

m.c36 = Constraint(expr=-0.714292440304189*m.x57**0.75 + m.x36 == 0)

m.c37 = Constraint(expr=-0.725899692459132*m.x58**0.75 + m.x37 == 0)

m.c38 = Constraint(expr=-0.737695562461593*m.x59**0.75 + m.x38 == 0)

m.c39 = Constraint(expr=-0.749683115351594*m.x60**0.75 + m.x39 == 0)

m.c40 = Constraint(expr=-0.761865465976057*m.x61**0.75 + m.x40 == 0)

m.c41 = Constraint(expr=-0.774245779798168*m.x62**0.75 + m.x41 == 0)
