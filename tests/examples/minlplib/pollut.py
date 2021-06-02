#  NLP written by GAMS Convert at 04/21/18 13:53:09
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          9        3        1        5        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         43       43        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        167      127       40        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(17643.6,41168.4),initialize=29406)
m.x2 = Var(within=Reals,bounds=(12825,29925),initialize=21375)
m.x3 = Var(within=Reals,bounds=(5053.8,11792.2),initialize=8423)
m.x4 = Var(within=Reals,bounds=(8323.8,19422.2),initialize=13873)
m.x5 = Var(within=Reals,bounds=(5082,11858),initialize=8470)
m.x6 = Var(within=Reals,bounds=(21825,50925),initialize=36375)
m.x7 = Var(within=Reals,bounds=(39609.6,92422.4),initialize=66016)
m.x8 = Var(within=Reals,bounds=(48080.4,112187.6),initialize=80134)
m.x9 = Var(within=Reals,bounds=(796.2,1857.8),initialize=1327)
m.x10 = Var(within=Reals,bounds=(2648.4,6179.6),initialize=4414)
m.x11 = Var(within=Reals,bounds=(2225.4,5192.6),initialize=3709)
m.x12 = Var(within=Reals,bounds=(8697.6,20294.4),initialize=14496)
m.x13 = Var(within=Reals,bounds=(61439.4,143358.6),initialize=102399)
m.x14 = Var(within=Reals,bounds=(16804.8,39211.2),initialize=28008)
m.x15 = Var(within=Reals,bounds=(41588.4,97039.6),initialize=69314)
m.x16 = Var(within=Reals,bounds=(54008.4,126019.6),initialize=90014)
m.x17 = Var(within=Reals,bounds=(17616,41104),initialize=29360)
m.x18 = Var(within=Reals,bounds=(16612.2,38761.8),initialize=27687)
m.x19 = Var(within=Reals,bounds=(2405.4,5612.6),initialize=4009)
m.x20 = Var(within=Reals,bounds=(14593.8,34052.2),initialize=24323)
m.x21 = Var(within=Reals,bounds=(14825.4,34592.6),initialize=24709)
m.x22 = Var(within=Reals,bounds=(11350.8,26485.2),initialize=18918)
m.x23 = Var(within=Reals,bounds=(12381.6,28890.4),initialize=20636)
m.x24 = Var(within=Reals,bounds=(6274.2,14639.8),initialize=10457)
m.x25 = Var(within=Reals,bounds=(5843.4,13634.6),initialize=9739)
m.x26 = Var(within=Reals,bounds=(11328,26432),initialize=18880)
m.x27 = Var(within=Reals,bounds=(26688,62272),initialize=44480)
m.x28 = Var(within=Reals,bounds=(21915.6,51136.4),initialize=36526)
m.x29 = Var(within=Reals,bounds=(454.8,1061.2),initialize=758)
m.x30 = Var(within=Reals,bounds=(2952.6,6889.4),initialize=4921)
m.x31 = Var(within=Reals,bounds=(4059.6,9472.4),initialize=6766)
m.x32 = Var(within=Reals,bounds=(5620.8,13115.2),initialize=9368)
m.x33 = Var(within=Reals,bounds=(18676.2,43577.8),initialize=31127)
m.x34 = Var(within=Reals,bounds=(699.6,1632.4),initialize=1166)
m.x35 = Var(within=Reals,bounds=(35715,83335),initialize=59525)
m.x36 = Var(within=Reals,bounds=(37828.8,88267.2),initialize=63048)
m.x37 = Var(within=Reals,bounds=(17903.4,41774.6),initialize=29839)
m.x38 = Var(within=Reals,bounds=(10167,23723),initialize=16945)
m.x39 = Var(within=Reals,bounds=(2896.8,6759.2),initialize=4828)
m.x40 = Var(within=Reals,bounds=(14741.4,34396.6),initialize=24569)
m.x41 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x42 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=-(9.6*m.x1**0.879*m.x21**0.121 + 6.353*m.x2**0.806*m.x22**0.194 + 9.818*m.x3**0.796*m.x23**0.204
                        + 7.371*m.x4**0.819*m.x24**0.181 + 10.22*m.x5**0.829*m.x25**0.171 + 6.255*m.x6**0.855*m.x26**
                       0.145 + 8.149*m.x7**0.696*m.x27**0.304 + 7.794*m.x8**0.854*m.x28**0.146 + 8.4*m.x9**0.827*m.x29**
                       0.173 + 9.933*m.x10**0.826*m.x30**0.174 + 11.069*m.x11**0.833*m.x31**0.167 + 6.528*m.x12**0.808*
                       m.x32**0.192 + 7.928*m.x13**0.884*m.x33**0.116 + 10.559*m.x14**0.909*m.x34**0.091 + 6.606*m.x15**
                       0.773*m.x35**0.227 + 7.153*m.x16**0.792*m.x36**0.208 + 11.146*m.x17**0.849*m.x37**0.151 + 6.884*
                       m.x18**0.801*m.x38**0.199 + 6.66*m.x19**0.747*m.x39**0.253 + 7.929*m.x20**0.818*m.x40**0.182)
                       , sense=minimize)

m.c2 = Constraint(expr=   0.797744360902256*m.x1 + 0.208131595282433*m.x2 + 0.395400943396226*m.x3
                        + 0.00945378151260504*m.x4 + 0.016020942408377*m.x5 + 1.32848209209778*m.x6
                        + 0.347442922374429*m.x7 + 0.534329395413482*m.x8 + 0.284322678843227*m.x9
                        + 0.283080040526849*m.x10 + 0.341982864137087*m.x11 + 0.0127927927927928*m.x12
                        + 0.0437154696132597*m.x13 + 0.00886939571150097*m.x14 + 0.00797702616464582*m.x15
                        + 0.00590969455511288*m.x16 + 0.0137430167597765*m.x17 + 0.00493133583021223*m.x18
                        + 0.0273858921161826*m.x19 + 0.0741242038216561*m.x20 <= 153000)

m.c3 = Constraint(expr=   0.0854323308270677*m.x1 + 0.153320918684047*m.x2 + 0.29127358490566*m.x3
                        + 0.00588235294117647*m.x4 + 0.00879581151832461*m.x5 + 0.424161455372371*m.x6
                        + 0.263333333333333*m.x7 + 0.400764419735928*m.x8 + 0.126560121765601*m.x9
                        + 0.0462006079027356*m.x10 + 0.0558139534883721*m.x11 + 0.528528528528528*m.x12
                        + 0.163052486187845*m.x13 + 0.329044834307992*m.x14 + 0.0548819400127632*m.x15
                        + 0.0249667994687915*m.x16 + 0.0412290502793296*m.x17 + 0.00792759051186017*m.x18
                        + 0.0174273858921162*m.x19 + 0.0200636942675159*m.x20 <= 120000)

m.c4 = Constraint(expr=   0.281015037593985*m.x1 + 0.557417752948479*m.x2 + 0.327830188679245*m.x3
                        + 0.48249299719888*m.x4 + 0.366492146596859*m.x5 + 0.266628766344514*m.x6
                        + 0.0589041095890411*m.x7 + 0.373175816539263*m.x8 + 2.06088280060883*m.x9
                        + 0.611955420466059*m.x10 + 0.609547123623011*m.x11 + 0.691291291291291*m.x12
                        + 0.614640883977901*m.x13 + 0.260233918128655*m.x14 + 0.433312061263561*m.x15
                        + 0.412350597609562*m.x16 + 0.329608938547486*m.x17 + 0.491260923845194*m.x18
                        + 0.264868603042877*m.x19 + 0.337579617834395*m.x20 <= 250000)

m.c5 = Constraint(expr=   0.676221804511278*m.x1 + 1.05723153320919*m.x2 + 0.158608490566038*m.x3
                        + 0.112464985994398*m.x4 + 0.149633507853403*m.x5 + 0.883001705514497*m.x6
                        + 0.0844748858447489*m.x7 + 0.6726893676164*m.x8 + 0.220700152207002*m.x9
                        + 0.932117527862209*m.x10 + 0.895960832313342*m.x11 + 0.571771771771772*m.x12
                        + 0.537292817679558*m.x13 + 0.362573099415205*m.x14 + 0.314613911933631*m.x15
                        + 0.164674634794157*m.x16 + 0.256983240223464*m.x17 + 0.268414481897628*m.x18
                        + 0.208160442600277*m.x19 + 0.278662420382166*m.x20 <= 250000)

m.c6 = Constraint(expr=   m.x41 - 0.9*m.x42 >= 0)

m.c7 = Constraint(expr=   m.x41 - 1.4*m.x42 <= 0)

m.c8 = Constraint(expr= - m.x1 - m.x2 - m.x3 - m.x4 - m.x5 - m.x6 - m.x7 - m.x8 - m.x9 - m.x10 - m.x11 - m.x12 - m.x13
                        - m.x14 - m.x15 - m.x16 - m.x17 - m.x18 - m.x19 - m.x20 + m.x41 == 0)

m.c9 = Constraint(expr= - m.x21 - m.x22 - m.x23 - m.x24 - m.x25 - m.x26 - m.x27 - m.x28 - m.x29 - m.x30 - m.x31 - m.x32
                        - m.x33 - m.x34 - m.x35 - m.x36 - m.x37 - m.x38 - m.x39 - m.x40 + m.x42 == 0)
