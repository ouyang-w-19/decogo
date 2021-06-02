#  NLP written by GAMS Convert at 04/21/18 13:51:41
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         26       26        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         76       76        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        151        1      150        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(None,None),initialize=0.239180341590991)
m.x2 = Var(within=Reals,bounds=(None,None),initialize=0.366795705695488)
m.x3 = Var(within=Reals,bounds=(None,None),initialize=-0.824393694345008)
m.x4 = Var(within=Reals,bounds=(None,None),initialize=-0.20445364152556)
m.x5 = Var(within=Reals,bounds=(None,None),initialize=-0.213822736723748)
m.x6 = Var(within=Reals,bounds=(None,None),initialize=0.0552164684243268)
m.x7 = Var(within=Reals,bounds=(None,None),initialize=-0.586906863272324)
m.x8 = Var(within=Reals,bounds=(None,None),initialize=0.298593602647523)
m.x9 = Var(within=Reals,bounds=(None,None),initialize=0.355869249309419)
m.x10 = Var(within=Reals,bounds=(None,None),initialize=-0.739872584978883)
m.x11 = Var(within=Reals,bounds=(None,None),initialize=0.781972693719759)
m.x12 = Var(within=Reals,bounds=(None,None),initialize=-0.842050067383099)
m.x13 = Var(within=Reals,bounds=(None,None),initialize=0.763853183973836)
m.x14 = Var(within=Reals,bounds=(None,None),initialize=0.0707385883845137)
m.x15 = Var(within=Reals,bounds=(None,None),initialize=0.676966872258273)
m.x16 = Var(within=Reals,bounds=(None,None),initialize=-0.615239159391388)
m.x17 = Var(within=Reals,bounds=(None,None),initialize=0.194562217624882)
m.x18 = Var(within=Reals,bounds=(None,None),initialize=-0.000422232856522465)
m.x19 = Var(within=Reals,bounds=(None,None),initialize=-0.0710616666815774)
m.x20 = Var(within=Reals,bounds=(None,None),initialize=-0.802987831773153)
m.x21 = Var(within=Reals,bounds=(None,None),initialize=-0.344305154696255)
m.x22 = Var(within=Reals,bounds=(None,None),initialize=-0.533805829063186)
m.x23 = Var(within=Reals,bounds=(None,None),initialize=0.665382373979989)
m.x24 = Var(within=Reals,bounds=(None,None),initialize=0.388420087049812)
m.x25 = Var(within=Reals,bounds=(None,None),initialize=-0.682029983840943)
m.x26 = Var(within=Reals,bounds=(None,None),initialize=0.446611486489583)
m.x27 = Var(within=Reals,bounds=(None,None),initialize=-0.552573627870873)
m.x28 = Var(within=Reals,bounds=(None,None),initialize=-0.270012939754188)
m.x29 = Var(within=Reals,bounds=(None,None),initialize=0.614265045675796)
m.x30 = Var(within=Reals,bounds=(None,None),initialize=0.787195952709942)
m.x31 = Var(within=Reals,bounds=(None,None),initialize=0.335681675744966)
m.x32 = Var(within=Reals,bounds=(None,None),initialize=0.809619787722586)
m.x33 = Var(within=Reals,bounds=(None,None),initialize=-0.378664598119689)
m.x34 = Var(within=Reals,bounds=(None,None),initialize=0.159642467758326)
m.x35 = Var(within=Reals,bounds=(None,None),initialize=-0.000979349466686923)
m.x36 = Var(within=Reals,bounds=(None,None),initialize=-0.00924905564272029)
m.x37 = Var(within=Reals,bounds=(None,None),initialize=-0.454232023429031)
m.x38 = Var(within=Reals,bounds=(None,None),initialize=-0.042600453543173)
m.x39 = Var(within=Reals,bounds=(None,None),initialize=-0.91720202046222)
m.x40 = Var(within=Reals,bounds=(None,None),initialize=0.727211440768476)
m.x41 = Var(within=Reals,bounds=(None,None),initialize=-0.741026339314474)
m.x42 = Var(within=Reals,bounds=(None,None),initialize=0.304537885768853)
m.x43 = Var(within=Reals,bounds=(None,None),initialize=0.834446009909628)
m.x44 = Var(within=Reals,bounds=(None,None),initialize=-0.127224428134585)
m.x45 = Var(within=Reals,bounds=(None,None),initialize=0.34535116139819)
m.x46 = Var(within=Reals,bounds=(None,None),initialize=0.417792969107124)
m.x47 = Var(within=Reals,bounds=(None,None),initialize=0.720899917808122)
m.x48 = Var(within=Reals,bounds=(None,None),initialize=0.72200222898579)
m.x49 = Var(within=Reals,bounds=(None,None),initialize=0.535334038601125)
m.x50 = Var(within=Reals,bounds=(None,None),initialize=-0.427520073559083)
m.x51 = Var(within=Reals,bounds=(None,None),initialize=-0.862166424962131)
m.x52 = Var(within=Reals,bounds=(None,None),initialize=0.748413853469436)
m.x53 = Var(within=Reals,bounds=(None,None),initialize=-0.497461605643582)
m.x54 = Var(within=Reals,bounds=(None,None),initialize=-0.762152978166359)
m.x55 = Var(within=Reals,bounds=(None,None),initialize=0.578448242539515)
m.x56 = Var(within=Reals,bounds=(None,None),initialize=0.940355759371844)
m.x57 = Var(within=Reals,bounds=(None,None),initialize=-0.00749220741006433)
m.x58 = Var(within=Reals,bounds=(None,None),initialize=0.876045080226371)
m.x59 = Var(within=Reals,bounds=(None,None),initialize=-0.920799304888955)
m.x60 = Var(within=Reals,bounds=(None,None),initialize=0.672746310931013)
m.x61 = Var(within=Reals,bounds=(None,None),initialize=0.623244062343463)
m.x62 = Var(within=Reals,bounds=(None,None),initialize=-0.290903683221246)
m.x63 = Var(within=Reals,bounds=(None,None),initialize=-0.643982542225292)
m.x64 = Var(within=Reals,bounds=(None,None),initialize=-0.392092470947082)
m.x65 = Var(within=Reals,bounds=(None,None),initialize=0.113487330924153)
m.x66 = Var(within=Reals,bounds=(None,None),initialize=0.268999518946722)
m.x67 = Var(within=Reals,bounds=(None,None),initialize=0.932417406317752)
m.x68 = Var(within=Reals,bounds=(None,None),initialize=0.551089537430458)
m.x69 = Var(within=Reals,bounds=(None,None),initialize=0.989325115628965)
m.x70 = Var(within=Reals,bounds=(None,None),initialize=0.485739762985462)
m.x71 = Var(within=Reals,bounds=(None,None),initialize=0.840775234776954)
m.x72 = Var(within=Reals,bounds=(None,None),initialize=-0.441989417704098)
m.x73 = Var(within=Reals,bounds=(None,None),initialize=-0.189681516591112)
m.x74 = Var(within=Reals,bounds=(None,None),initialize=-0.750031534731191)
m.x75 = Var(within=Reals,bounds=(None,None),initialize=0.593347864111736)

m.obj = Objective(expr=1/sqrt((m.x1 - m.x2)**2 + (m.x26 - m.x27)**2 + (m.x51 - m.x52)**2) + 1/sqrt((m.x1 - m.x3)**2 + (
                       m.x26 - m.x28)**2 + (m.x51 - m.x53)**2) + 1/sqrt((m.x1 - m.x4)**2 + (m.x26 - m.x29)**2 + (m.x51
                        - m.x54)**2) + 1/sqrt((m.x1 - m.x5)**2 + (m.x26 - m.x30)**2 + (m.x51 - m.x55)**2) + 1/sqrt((m.x1
                        - m.x6)**2 + (m.x26 - m.x31)**2 + (m.x51 - m.x56)**2) + 1/sqrt((m.x1 - m.x7)**2 + (m.x26 - m.x32
                       )**2 + (m.x51 - m.x57)**2) + 1/sqrt((m.x1 - m.x8)**2 + (m.x26 - m.x33)**2 + (m.x51 - m.x58)**2)
                        + 1/sqrt((m.x1 - m.x9)**2 + (m.x26 - m.x34)**2 + (m.x51 - m.x59)**2) + 1/sqrt((m.x1 - m.x10)**2
                        + (m.x26 - m.x35)**2 + (m.x51 - m.x60)**2) + 1/sqrt((m.x1 - m.x11)**2 + (m.x26 - m.x36)**2 + (
                       m.x51 - m.x61)**2) + 1/sqrt((m.x1 - m.x12)**2 + (m.x26 - m.x37)**2 + (m.x51 - m.x62)**2) + 1/
                       sqrt((m.x1 - m.x13)**2 + (m.x26 - m.x38)**2 + (m.x51 - m.x63)**2) + 1/sqrt((m.x1 - m.x14)**2 + (
                       m.x26 - m.x39)**2 + (m.x51 - m.x64)**2) + 1/sqrt((m.x1 - m.x15)**2 + (m.x26 - m.x40)**2 + (m.x51
                        - m.x65)**2) + 1/sqrt((m.x1 - m.x16)**2 + (m.x26 - m.x41)**2 + (m.x51 - m.x66)**2) + 1/sqrt((
                       m.x1 - m.x17)**2 + (m.x26 - m.x42)**2 + (m.x51 - m.x67)**2) + 1/sqrt((m.x1 - m.x18)**2 + (m.x26
                        - m.x43)**2 + (m.x51 - m.x68)**2) + 1/sqrt((m.x1 - m.x19)**2 + (m.x26 - m.x44)**2 + (m.x51 - 
                       m.x69)**2) + 1/sqrt((m.x1 - m.x20)**2 + (m.x26 - m.x45)**2 + (m.x51 - m.x70)**2) + 1/sqrt((m.x1
                        - m.x21)**2 + (m.x26 - m.x46)**2 + (m.x51 - m.x71)**2) + 1/sqrt((m.x1 - m.x22)**2 + (m.x26 - 
                       m.x47)**2 + (m.x51 - m.x72)**2) + 1/sqrt((m.x1 - m.x23)**2 + (m.x26 - m.x48)**2 + (m.x51 - m.x73)
                       **2) + 1/sqrt((m.x1 - m.x24)**2 + (m.x26 - m.x49)**2 + (m.x51 - m.x74)**2) + 1/sqrt((m.x1 - m.x25
                       )**2 + (m.x26 - m.x50)**2 + (m.x51 - m.x75)**2) + 1/sqrt((m.x2 - m.x3)**2 + (m.x27 - m.x28)**2 + 
                       (m.x52 - m.x53)**2) + 1/sqrt((m.x2 - m.x4)**2 + (m.x27 - m.x29)**2 + (m.x52 - m.x54)**2) + 1/
                       sqrt((m.x2 - m.x5)**2 + (m.x27 - m.x30)**2 + (m.x52 - m.x55)**2) + 1/sqrt((m.x2 - m.x6)**2 + (
                       m.x27 - m.x31)**2 + (m.x52 - m.x56)**2) + 1/sqrt((m.x2 - m.x7)**2 + (m.x27 - m.x32)**2 + (m.x52
                        - m.x57)**2) + 1/sqrt((m.x2 - m.x8)**2 + (m.x27 - m.x33)**2 + (m.x52 - m.x58)**2) + 1/sqrt((m.x2
                        - m.x9)**2 + (m.x27 - m.x34)**2 + (m.x52 - m.x59)**2) + 1/sqrt((m.x2 - m.x10)**2 + (m.x27 - 
                       m.x35)**2 + (m.x52 - m.x60)**2) + 1/sqrt((m.x2 - m.x11)**2 + (m.x27 - m.x36)**2 + (m.x52 - m.x61)
                       **2) + 1/sqrt((m.x2 - m.x12)**2 + (m.x27 - m.x37)**2 + (m.x52 - m.x62)**2) + 1/sqrt((m.x2 - m.x13
                       )**2 + (m.x27 - m.x38)**2 + (m.x52 - m.x63)**2) + 1/sqrt((m.x2 - m.x14)**2 + (m.x27 - m.x39)**2
                        + (m.x52 - m.x64)**2) + 1/sqrt((m.x2 - m.x15)**2 + (m.x27 - m.x40)**2 + (m.x52 - m.x65)**2) + 1/
                       sqrt((m.x2 - m.x16)**2 + (m.x27 - m.x41)**2 + (m.x52 - m.x66)**2) + 1/sqrt((m.x2 - m.x17)**2 + (
                       m.x27 - m.x42)**2 + (m.x52 - m.x67)**2) + 1/sqrt((m.x2 - m.x18)**2 + (m.x27 - m.x43)**2 + (m.x52
                        - m.x68)**2) + 1/sqrt((m.x2 - m.x19)**2 + (m.x27 - m.x44)**2 + (m.x52 - m.x69)**2) + 1/sqrt((
                       m.x2 - m.x20)**2 + (m.x27 - m.x45)**2 + (m.x52 - m.x70)**2) + 1/sqrt((m.x2 - m.x21)**2 + (m.x27
                        - m.x46)**2 + (m.x52 - m.x71)**2) + 1/sqrt((m.x2 - m.x22)**2 + (m.x27 - m.x47)**2 + (m.x52 - 
                       m.x72)**2) + 1/sqrt((m.x2 - m.x23)**2 + (m.x27 - m.x48)**2 + (m.x52 - m.x73)**2) + 1/sqrt((m.x2
                        - m.x24)**2 + (m.x27 - m.x49)**2 + (m.x52 - m.x74)**2) + 1/sqrt((m.x2 - m.x25)**2 + (m.x27 - 
                       m.x50)**2 + (m.x52 - m.x75)**2) + 1/sqrt((m.x3 - m.x4)**2 + (m.x28 - m.x29)**2 + (m.x53 - m.x54)
                       **2) + 1/sqrt((m.x3 - m.x5)**2 + (m.x28 - m.x30)**2 + (m.x53 - m.x55)**2) + 1/sqrt((m.x3 - m.x6)
                       **2 + (m.x28 - m.x31)**2 + (m.x53 - m.x56)**2) + 1/sqrt((m.x3 - m.x7)**2 + (m.x28 - m.x32)**2 + (
                       m.x53 - m.x57)**2) + 1/sqrt((m.x3 - m.x8)**2 + (m.x28 - m.x33)**2 + (m.x53 - m.x58)**2) + 1/sqrt(
                       (m.x3 - m.x9)**2 + (m.x28 - m.x34)**2 + (m.x53 - m.x59)**2) + 1/sqrt((m.x3 - m.x10)**2 + (m.x28
                        - m.x35)**2 + (m.x53 - m.x60)**2) + 1/sqrt((m.x3 - m.x11)**2 + (m.x28 - m.x36)**2 + (m.x53 - 
                       m.x61)**2) + 1/sqrt((m.x3 - m.x12)**2 + (m.x28 - m.x37)**2 + (m.x53 - m.x62)**2) + 1/sqrt((m.x3
                        - m.x13)**2 + (m.x28 - m.x38)**2 + (m.x53 - m.x63)**2) + 1/sqrt((m.x3 - m.x14)**2 + (m.x28 - 
                       m.x39)**2 + (m.x53 - m.x64)**2) + 1/sqrt((m.x3 - m.x15)**2 + (m.x28 - m.x40)**2 + (m.x53 - m.x65)
                       **2) + 1/sqrt((m.x3 - m.x16)**2 + (m.x28 - m.x41)**2 + (m.x53 - m.x66)**2) + 1/sqrt((m.x3 - m.x17
                       )**2 + (m.x28 - m.x42)**2 + (m.x53 - m.x67)**2) + 1/sqrt((m.x3 - m.x18)**2 + (m.x28 - m.x43)**2
                        + (m.x53 - m.x68)**2) + 1/sqrt((m.x3 - m.x19)**2 + (m.x28 - m.x44)**2 + (m.x53 - m.x69)**2) + 1/
                       sqrt((m.x3 - m.x20)**2 + (m.x28 - m.x45)**2 + (m.x53 - m.x70)**2) + 1/sqrt((m.x3 - m.x21)**2 + (
                       m.x28 - m.x46)**2 + (m.x53 - m.x71)**2) + 1/sqrt((m.x3 - m.x22)**2 + (m.x28 - m.x47)**2 + (m.x53
                        - m.x72)**2) + 1/sqrt((m.x3 - m.x23)**2 + (m.x28 - m.x48)**2 + (m.x53 - m.x73)**2) + 1/sqrt((
                       m.x3 - m.x24)**2 + (m.x28 - m.x49)**2 + (m.x53 - m.x74)**2) + 1/sqrt((m.x3 - m.x25)**2 + (m.x28
                        - m.x50)**2 + (m.x53 - m.x75)**2) + 1/sqrt((m.x4 - m.x5)**2 + (m.x29 - m.x30)**2 + (m.x54 - 
                       m.x55)**2) + 1/sqrt((m.x4 - m.x6)**2 + (m.x29 - m.x31)**2 + (m.x54 - m.x56)**2) + 1/sqrt((m.x4 - 
                       m.x7)**2 + (m.x29 - m.x32)**2 + (m.x54 - m.x57)**2) + 1/sqrt((m.x4 - m.x8)**2 + (m.x29 - m.x33)**
                       2 + (m.x54 - m.x58)**2) + 1/sqrt((m.x4 - m.x9)**2 + (m.x29 - m.x34)**2 + (m.x54 - m.x59)**2) + 1/
                       sqrt((m.x4 - m.x10)**2 + (m.x29 - m.x35)**2 + (m.x54 - m.x60)**2) + 1/sqrt((m.x4 - m.x11)**2 + (
                       m.x29 - m.x36)**2 + (m.x54 - m.x61)**2) + 1/sqrt((m.x4 - m.x12)**2 + (m.x29 - m.x37)**2 + (m.x54
                        - m.x62)**2) + 1/sqrt((m.x4 - m.x13)**2 + (m.x29 - m.x38)**2 + (m.x54 - m.x63)**2) + 1/sqrt((
                       m.x4 - m.x14)**2 + (m.x29 - m.x39)**2 + (m.x54 - m.x64)**2) + 1/sqrt((m.x4 - m.x15)**2 + (m.x29
                        - m.x40)**2 + (m.x54 - m.x65)**2) + 1/sqrt((m.x4 - m.x16)**2 + (m.x29 - m.x41)**2 + (m.x54 - 
                       m.x66)**2) + 1/sqrt((m.x4 - m.x17)**2 + (m.x29 - m.x42)**2 + (m.x54 - m.x67)**2) + 1/sqrt((m.x4
                        - m.x18)**2 + (m.x29 - m.x43)**2 + (m.x54 - m.x68)**2) + 1/sqrt((m.x4 - m.x19)**2 + (m.x29 - 
                       m.x44)**2 + (m.x54 - m.x69)**2) + 1/sqrt((m.x4 - m.x20)**2 + (m.x29 - m.x45)**2 + (m.x54 - m.x70)
                       **2) + 1/sqrt((m.x4 - m.x21)**2 + (m.x29 - m.x46)**2 + (m.x54 - m.x71)**2) + 1/sqrt((m.x4 - m.x22
                       )**2 + (m.x29 - m.x47)**2 + (m.x54 - m.x72)**2) + 1/sqrt((m.x4 - m.x23)**2 + (m.x29 - m.x48)**2
                        + (m.x54 - m.x73)**2) + 1/sqrt((m.x4 - m.x24)**2 + (m.x29 - m.x49)**2 + (m.x54 - m.x74)**2) + 1/
                       sqrt((m.x4 - m.x25)**2 + (m.x29 - m.x50)**2 + (m.x54 - m.x75)**2) + 1/sqrt((m.x5 - m.x6)**2 + (
                       m.x30 - m.x31)**2 + (m.x55 - m.x56)**2) + 1/sqrt((m.x5 - m.x7)**2 + (m.x30 - m.x32)**2 + (m.x55
                        - m.x57)**2) + 1/sqrt((m.x5 - m.x8)**2 + (m.x30 - m.x33)**2 + (m.x55 - m.x58)**2) + 1/sqrt((m.x5
                        - m.x9)**2 + (m.x30 - m.x34)**2 + (m.x55 - m.x59)**2) + 1/sqrt((m.x5 - m.x10)**2 + (m.x30 - 
                       m.x35)**2 + (m.x55 - m.x60)**2) + 1/sqrt((m.x5 - m.x11)**2 + (m.x30 - m.x36)**2 + (m.x55 - m.x61)
                       **2) + 1/sqrt((m.x5 - m.x12)**2 + (m.x30 - m.x37)**2 + (m.x55 - m.x62)**2) + 1/sqrt((m.x5 - m.x13
                       )**2 + (m.x30 - m.x38)**2 + (m.x55 - m.x63)**2) + 1/sqrt((m.x5 - m.x14)**2 + (m.x30 - m.x39)**2
                        + (m.x55 - m.x64)**2) + 1/sqrt((m.x5 - m.x15)**2 + (m.x30 - m.x40)**2 + (m.x55 - m.x65)**2) + 1/
                       sqrt((m.x5 - m.x16)**2 + (m.x30 - m.x41)**2 + (m.x55 - m.x66)**2) + 1/sqrt((m.x5 - m.x17)**2 + (
                       m.x30 - m.x42)**2 + (m.x55 - m.x67)**2) + 1/sqrt((m.x5 - m.x18)**2 + (m.x30 - m.x43)**2 + (m.x55
                        - m.x68)**2) + 1/sqrt((m.x5 - m.x19)**2 + (m.x30 - m.x44)**2 + (m.x55 - m.x69)**2) + 1/sqrt((
                       m.x5 - m.x20)**2 + (m.x30 - m.x45)**2 + (m.x55 - m.x70)**2) + 1/sqrt((m.x5 - m.x21)**2 + (m.x30
                        - m.x46)**2 + (m.x55 - m.x71)**2) + 1/sqrt((m.x5 - m.x22)**2 + (m.x30 - m.x47)**2 + (m.x55 - 
                       m.x72)**2) + 1/sqrt((m.x5 - m.x23)**2 + (m.x30 - m.x48)**2 + (m.x55 - m.x73)**2) + 1/sqrt((m.x5
                        - m.x24)**2 + (m.x30 - m.x49)**2 + (m.x55 - m.x74)**2) + 1/sqrt((m.x5 - m.x25)**2 + (m.x30 - 
                       m.x50)**2 + (m.x55 - m.x75)**2) + 1/sqrt((m.x6 - m.x7)**2 + (m.x31 - m.x32)**2 + (m.x56 - m.x57)
                       **2) + 1/sqrt((m.x6 - m.x8)**2 + (m.x31 - m.x33)**2 + (m.x56 - m.x58)**2) + 1/sqrt((m.x6 - m.x9)
                       **2 + (m.x31 - m.x34)**2 + (m.x56 - m.x59)**2) + 1/sqrt((m.x6 - m.x10)**2 + (m.x31 - m.x35)**2 + 
                       (m.x56 - m.x60)**2) + 1/sqrt((m.x6 - m.x11)**2 + (m.x31 - m.x36)**2 + (m.x56 - m.x61)**2) + 1/
                       sqrt((m.x6 - m.x12)**2 + (m.x31 - m.x37)**2 + (m.x56 - m.x62)**2) + 1/sqrt((m.x6 - m.x13)**2 + (
                       m.x31 - m.x38)**2 + (m.x56 - m.x63)**2) + 1/sqrt((m.x6 - m.x14)**2 + (m.x31 - m.x39)**2 + (m.x56
                        - m.x64)**2) + 1/sqrt((m.x6 - m.x15)**2 + (m.x31 - m.x40)**2 + (m.x56 - m.x65)**2) + 1/sqrt((
                       m.x6 - m.x16)**2 + (m.x31 - m.x41)**2 + (m.x56 - m.x66)**2) + 1/sqrt((m.x6 - m.x17)**2 + (m.x31
                        - m.x42)**2 + (m.x56 - m.x67)**2) + 1/sqrt((m.x6 - m.x18)**2 + (m.x31 - m.x43)**2 + (m.x56 - 
                       m.x68)**2) + 1/sqrt((m.x6 - m.x19)**2 + (m.x31 - m.x44)**2 + (m.x56 - m.x69)**2) + 1/sqrt((m.x6
                        - m.x20)**2 + (m.x31 - m.x45)**2 + (m.x56 - m.x70)**2) + 1/sqrt((m.x6 - m.x21)**2 + (m.x31 - 
                       m.x46)**2 + (m.x56 - m.x71)**2) + 1/sqrt((m.x6 - m.x22)**2 + (m.x31 - m.x47)**2 + (m.x56 - m.x72)
                       **2) + 1/sqrt((m.x6 - m.x23)**2 + (m.x31 - m.x48)**2 + (m.x56 - m.x73)**2) + 1/sqrt((m.x6 - m.x24
                       )**2 + (m.x31 - m.x49)**2 + (m.x56 - m.x74)**2) + 1/sqrt((m.x6 - m.x25)**2 + (m.x31 - m.x50)**2
                        + (m.x56 - m.x75)**2) + 1/sqrt((m.x7 - m.x8)**2 + (m.x32 - m.x33)**2 + (m.x57 - m.x58)**2) + 1/
                       sqrt((m.x7 - m.x9)**2 + (m.x32 - m.x34)**2 + (m.x57 - m.x59)**2) + 1/sqrt((m.x7 - m.x10)**2 + (
                       m.x32 - m.x35)**2 + (m.x57 - m.x60)**2) + 1/sqrt((m.x7 - m.x11)**2 + (m.x32 - m.x36)**2 + (m.x57
                        - m.x61)**2) + 1/sqrt((m.x7 - m.x12)**2 + (m.x32 - m.x37)**2 + (m.x57 - m.x62)**2) + 1/sqrt((
                       m.x7 - m.x13)**2 + (m.x32 - m.x38)**2 + (m.x57 - m.x63)**2) + 1/sqrt((m.x7 - m.x14)**2 + (m.x32
                        - m.x39)**2 + (m.x57 - m.x64)**2) + 1/sqrt((m.x7 - m.x15)**2 + (m.x32 - m.x40)**2 + (m.x57 - 
                       m.x65)**2) + 1/sqrt((m.x7 - m.x16)**2 + (m.x32 - m.x41)**2 + (m.x57 - m.x66)**2) + 1/sqrt((m.x7
                        - m.x17)**2 + (m.x32 - m.x42)**2 + (m.x57 - m.x67)**2) + 1/sqrt((m.x7 - m.x18)**2 + (m.x32 - 
                       m.x43)**2 + (m.x57 - m.x68)**2) + 1/sqrt((m.x7 - m.x19)**2 + (m.x32 - m.x44)**2 + (m.x57 - m.x69)
                       **2) + 1/sqrt((m.x7 - m.x20)**2 + (m.x32 - m.x45)**2 + (m.x57 - m.x70)**2) + 1/sqrt((m.x7 - m.x21
                       )**2 + (m.x32 - m.x46)**2 + (m.x57 - m.x71)**2) + 1/sqrt((m.x7 - m.x22)**2 + (m.x32 - m.x47)**2
                        + (m.x57 - m.x72)**2) + 1/sqrt((m.x7 - m.x23)**2 + (m.x32 - m.x48)**2 + (m.x57 - m.x73)**2) + 1/
                       sqrt((m.x7 - m.x24)**2 + (m.x32 - m.x49)**2 + (m.x57 - m.x74)**2) + 1/sqrt((m.x7 - m.x25)**2 + (
                       m.x32 - m.x50)**2 + (m.x57 - m.x75)**2) + 1/sqrt((m.x8 - m.x9)**2 + (m.x33 - m.x34)**2 + (m.x58
                        - m.x59)**2) + 1/sqrt((m.x8 - m.x10)**2 + (m.x33 - m.x35)**2 + (m.x58 - m.x60)**2) + 1/sqrt((
                       m.x8 - m.x11)**2 + (m.x33 - m.x36)**2 + (m.x58 - m.x61)**2) + 1/sqrt((m.x8 - m.x12)**2 + (m.x33
                        - m.x37)**2 + (m.x58 - m.x62)**2) + 1/sqrt((m.x8 - m.x13)**2 + (m.x33 - m.x38)**2 + (m.x58 - 
                       m.x63)**2) + 1/sqrt((m.x8 - m.x14)**2 + (m.x33 - m.x39)**2 + (m.x58 - m.x64)**2) + 1/sqrt((m.x8
                        - m.x15)**2 + (m.x33 - m.x40)**2 + (m.x58 - m.x65)**2) + 1/sqrt((m.x8 - m.x16)**2 + (m.x33 - 
                       m.x41)**2 + (m.x58 - m.x66)**2) + 1/sqrt((m.x8 - m.x17)**2 + (m.x33 - m.x42)**2 + (m.x58 - m.x67)
                       **2) + 1/sqrt((m.x8 - m.x18)**2 + (m.x33 - m.x43)**2 + (m.x58 - m.x68)**2) + 1/sqrt((m.x8 - m.x19
                       )**2 + (m.x33 - m.x44)**2 + (m.x58 - m.x69)**2) + 1/sqrt((m.x8 - m.x20)**2 + (m.x33 - m.x45)**2
                        + (m.x58 - m.x70)**2) + 1/sqrt((m.x8 - m.x21)**2 + (m.x33 - m.x46)**2 + (m.x58 - m.x71)**2) + 1/
                       sqrt((m.x8 - m.x22)**2 + (m.x33 - m.x47)**2 + (m.x58 - m.x72)**2) + 1/sqrt((m.x8 - m.x23)**2 + (
                       m.x33 - m.x48)**2 + (m.x58 - m.x73)**2) + 1/sqrt((m.x8 - m.x24)**2 + (m.x33 - m.x49)**2 + (m.x58
                        - m.x74)**2) + 1/sqrt((m.x8 - m.x25)**2 + (m.x33 - m.x50)**2 + (m.x58 - m.x75)**2) + 1/sqrt((
                       m.x9 - m.x10)**2 + (m.x34 - m.x35)**2 + (m.x59 - m.x60)**2) + 1/sqrt((m.x9 - m.x11)**2 + (m.x34
                        - m.x36)**2 + (m.x59 - m.x61)**2) + 1/sqrt((m.x9 - m.x12)**2 + (m.x34 - m.x37)**2 + (m.x59 - 
                       m.x62)**2) + 1/sqrt((m.x9 - m.x13)**2 + (m.x34 - m.x38)**2 + (m.x59 - m.x63)**2) + 1/sqrt((m.x9
                        - m.x14)**2 + (m.x34 - m.x39)**2 + (m.x59 - m.x64)**2) + 1/sqrt((m.x9 - m.x15)**2 + (m.x34 - 
                       m.x40)**2 + (m.x59 - m.x65)**2) + 1/sqrt((m.x9 - m.x16)**2 + (m.x34 - m.x41)**2 + (m.x59 - m.x66)
                       **2) + 1/sqrt((m.x9 - m.x17)**2 + (m.x34 - m.x42)**2 + (m.x59 - m.x67)**2) + 1/sqrt((m.x9 - m.x18
                       )**2 + (m.x34 - m.x43)**2 + (m.x59 - m.x68)**2) + 1/sqrt((m.x9 - m.x19)**2 + (m.x34 - m.x44)**2
                        + (m.x59 - m.x69)**2) + 1/sqrt((m.x9 - m.x20)**2 + (m.x34 - m.x45)**2 + (m.x59 - m.x70)**2) + 1/
                       sqrt((m.x9 - m.x21)**2 + (m.x34 - m.x46)**2 + (m.x59 - m.x71)**2) + 1/sqrt((m.x9 - m.x22)**2 + (
                       m.x34 - m.x47)**2 + (m.x59 - m.x72)**2) + 1/sqrt((m.x9 - m.x23)**2 + (m.x34 - m.x48)**2 + (m.x59
                        - m.x73)**2) + 1/sqrt((m.x9 - m.x24)**2 + (m.x34 - m.x49)**2 + (m.x59 - m.x74)**2) + 1/sqrt((
                       m.x9 - m.x25)**2 + (m.x34 - m.x50)**2 + (m.x59 - m.x75)**2) + 1/sqrt((m.x10 - m.x11)**2 + (m.x35
                        - m.x36)**2 + (m.x60 - m.x61)**2) + 1/sqrt((m.x10 - m.x12)**2 + (m.x35 - m.x37)**2 + (m.x60 - 
                       m.x62)**2) + 1/sqrt((m.x10 - m.x13)**2 + (m.x35 - m.x38)**2 + (m.x60 - m.x63)**2) + 1/sqrt((m.x10
                        - m.x14)**2 + (m.x35 - m.x39)**2 + (m.x60 - m.x64)**2) + 1/sqrt((m.x10 - m.x15)**2 + (m.x35 - 
                       m.x40)**2 + (m.x60 - m.x65)**2) + 1/sqrt((m.x10 - m.x16)**2 + (m.x35 - m.x41)**2 + (m.x60 - m.x66
                       )**2) + 1/sqrt((m.x10 - m.x17)**2 + (m.x35 - m.x42)**2 + (m.x60 - m.x67)**2) + 1/sqrt((m.x10 - 
                       m.x18)**2 + (m.x35 - m.x43)**2 + (m.x60 - m.x68)**2) + 1/sqrt((m.x10 - m.x19)**2 + (m.x35 - m.x44
                       )**2 + (m.x60 - m.x69)**2) + 1/sqrt((m.x10 - m.x20)**2 + (m.x35 - m.x45)**2 + (m.x60 - m.x70)**2)
                        + 1/sqrt((m.x10 - m.x21)**2 + (m.x35 - m.x46)**2 + (m.x60 - m.x71)**2) + 1/sqrt((m.x10 - m.x22)
                       **2 + (m.x35 - m.x47)**2 + (m.x60 - m.x72)**2) + 1/sqrt((m.x10 - m.x23)**2 + (m.x35 - m.x48)**2
                        + (m.x60 - m.x73)**2) + 1/sqrt((m.x10 - m.x24)**2 + (m.x35 - m.x49)**2 + (m.x60 - m.x74)**2) + 1
                       /sqrt((m.x10 - m.x25)**2 + (m.x35 - m.x50)**2 + (m.x60 - m.x75)**2) + 1/sqrt((m.x11 - m.x12)**2
                        + (m.x36 - m.x37)**2 + (m.x61 - m.x62)**2) + 1/sqrt((m.x11 - m.x13)**2 + (m.x36 - m.x38)**2 + (
                       m.x61 - m.x63)**2) + 1/sqrt((m.x11 - m.x14)**2 + (m.x36 - m.x39)**2 + (m.x61 - m.x64)**2) + 1/
                       sqrt((m.x11 - m.x15)**2 + (m.x36 - m.x40)**2 + (m.x61 - m.x65)**2) + 1/sqrt((m.x11 - m.x16)**2 + 
                       (m.x36 - m.x41)**2 + (m.x61 - m.x66)**2) + 1/sqrt((m.x11 - m.x17)**2 + (m.x36 - m.x42)**2 + (
                       m.x61 - m.x67)**2) + 1/sqrt((m.x11 - m.x18)**2 + (m.x36 - m.x43)**2 + (m.x61 - m.x68)**2) + 1/
                       sqrt((m.x11 - m.x19)**2 + (m.x36 - m.x44)**2 + (m.x61 - m.x69)**2) + 1/sqrt((m.x11 - m.x20)**2 + 
                       (m.x36 - m.x45)**2 + (m.x61 - m.x70)**2) + 1/sqrt((m.x11 - m.x21)**2 + (m.x36 - m.x46)**2 + (
                       m.x61 - m.x71)**2) + 1/sqrt((m.x11 - m.x22)**2 + (m.x36 - m.x47)**2 + (m.x61 - m.x72)**2) + 1/
                       sqrt((m.x11 - m.x23)**2 + (m.x36 - m.x48)**2 + (m.x61 - m.x73)**2) + 1/sqrt((m.x11 - m.x24)**2 + 
                       (m.x36 - m.x49)**2 + (m.x61 - m.x74)**2) + 1/sqrt((m.x11 - m.x25)**2 + (m.x36 - m.x50)**2 + (
                       m.x61 - m.x75)**2) + 1/sqrt((m.x12 - m.x13)**2 + (m.x37 - m.x38)**2 + (m.x62 - m.x63)**2) + 1/
                       sqrt((m.x12 - m.x14)**2 + (m.x37 - m.x39)**2 + (m.x62 - m.x64)**2) + 1/sqrt((m.x12 - m.x15)**2 + 
                       (m.x37 - m.x40)**2 + (m.x62 - m.x65)**2) + 1/sqrt((m.x12 - m.x16)**2 + (m.x37 - m.x41)**2 + (
                       m.x62 - m.x66)**2) + 1/sqrt((m.x12 - m.x17)**2 + (m.x37 - m.x42)**2 + (m.x62 - m.x67)**2) + 1/
                       sqrt((m.x12 - m.x18)**2 + (m.x37 - m.x43)**2 + (m.x62 - m.x68)**2) + 1/sqrt((m.x12 - m.x19)**2 + 
                       (m.x37 - m.x44)**2 + (m.x62 - m.x69)**2) + 1/sqrt((m.x12 - m.x20)**2 + (m.x37 - m.x45)**2 + (
                       m.x62 - m.x70)**2) + 1/sqrt((m.x12 - m.x21)**2 + (m.x37 - m.x46)**2 + (m.x62 - m.x71)**2) + 1/
                       sqrt((m.x12 - m.x22)**2 + (m.x37 - m.x47)**2 + (m.x62 - m.x72)**2) + 1/sqrt((m.x12 - m.x23)**2 + 
                       (m.x37 - m.x48)**2 + (m.x62 - m.x73)**2) + 1/sqrt((m.x12 - m.x24)**2 + (m.x37 - m.x49)**2 + (
                       m.x62 - m.x74)**2) + 1/sqrt((m.x12 - m.x25)**2 + (m.x37 - m.x50)**2 + (m.x62 - m.x75)**2) + 1/
                       sqrt((m.x13 - m.x14)**2 + (m.x38 - m.x39)**2 + (m.x63 - m.x64)**2) + 1/sqrt((m.x13 - m.x15)**2 + 
                       (m.x38 - m.x40)**2 + (m.x63 - m.x65)**2) + 1/sqrt((m.x13 - m.x16)**2 + (m.x38 - m.x41)**2 + (
                       m.x63 - m.x66)**2) + 1/sqrt((m.x13 - m.x17)**2 + (m.x38 - m.x42)**2 + (m.x63 - m.x67)**2) + 1/
                       sqrt((m.x13 - m.x18)**2 + (m.x38 - m.x43)**2 + (m.x63 - m.x68)**2) + 1/sqrt((m.x13 - m.x19)**2 + 
                       (m.x38 - m.x44)**2 + (m.x63 - m.x69)**2) + 1/sqrt((m.x13 - m.x20)**2 + (m.x38 - m.x45)**2 + (
                       m.x63 - m.x70)**2) + 1/sqrt((m.x13 - m.x21)**2 + (m.x38 - m.x46)**2 + (m.x63 - m.x71)**2) + 1/
                       sqrt((m.x13 - m.x22)**2 + (m.x38 - m.x47)**2 + (m.x63 - m.x72)**2) + 1/sqrt((m.x13 - m.x23)**2 + 
                       (m.x38 - m.x48)**2 + (m.x63 - m.x73)**2) + 1/sqrt((m.x13 - m.x24)**2 + (m.x38 - m.x49)**2 + (
                       m.x63 - m.x74)**2) + 1/sqrt((m.x13 - m.x25)**2 + (m.x38 - m.x50)**2 + (m.x63 - m.x75)**2) + 1/
                       sqrt((m.x14 - m.x15)**2 + (m.x39 - m.x40)**2 + (m.x64 - m.x65)**2) + 1/sqrt((m.x14 - m.x16)**2 + 
                       (m.x39 - m.x41)**2 + (m.x64 - m.x66)**2) + 1/sqrt((m.x14 - m.x17)**2 + (m.x39 - m.x42)**2 + (
                       m.x64 - m.x67)**2) + 1/sqrt((m.x14 - m.x18)**2 + (m.x39 - m.x43)**2 + (m.x64 - m.x68)**2) + 1/
                       sqrt((m.x14 - m.x19)**2 + (m.x39 - m.x44)**2 + (m.x64 - m.x69)**2) + 1/sqrt((m.x14 - m.x20)**2 + 
                       (m.x39 - m.x45)**2 + (m.x64 - m.x70)**2) + 1/sqrt((m.x14 - m.x21)**2 + (m.x39 - m.x46)**2 + (
                       m.x64 - m.x71)**2) + 1/sqrt((m.x14 - m.x22)**2 + (m.x39 - m.x47)**2 + (m.x64 - m.x72)**2) + 1/
                       sqrt((m.x14 - m.x23)**2 + (m.x39 - m.x48)**2 + (m.x64 - m.x73)**2) + 1/sqrt((m.x14 - m.x24)**2 + 
                       (m.x39 - m.x49)**2 + (m.x64 - m.x74)**2) + 1/sqrt((m.x14 - m.x25)**2 + (m.x39 - m.x50)**2 + (
                       m.x64 - m.x75)**2) + 1/sqrt((m.x15 - m.x16)**2 + (m.x40 - m.x41)**2 + (m.x65 - m.x66)**2) + 1/
                       sqrt((m.x15 - m.x17)**2 + (m.x40 - m.x42)**2 + (m.x65 - m.x67)**2) + 1/sqrt((m.x15 - m.x18)**2 + 
                       (m.x40 - m.x43)**2 + (m.x65 - m.x68)**2) + 1/sqrt((m.x15 - m.x19)**2 + (m.x40 - m.x44)**2 + (
                       m.x65 - m.x69)**2) + 1/sqrt((m.x15 - m.x20)**2 + (m.x40 - m.x45)**2 + (m.x65 - m.x70)**2) + 1/
                       sqrt((m.x15 - m.x21)**2 + (m.x40 - m.x46)**2 + (m.x65 - m.x71)**2) + 1/sqrt((m.x15 - m.x22)**2 + 
                       (m.x40 - m.x47)**2 + (m.x65 - m.x72)**2) + 1/sqrt((m.x15 - m.x23)**2 + (m.x40 - m.x48)**2 + (
                       m.x65 - m.x73)**2) + 1/sqrt((m.x15 - m.x24)**2 + (m.x40 - m.x49)**2 + (m.x65 - m.x74)**2) + 1/
                       sqrt((m.x15 - m.x25)**2 + (m.x40 - m.x50)**2 + (m.x65 - m.x75)**2) + 1/sqrt((m.x16 - m.x17)**2 + 
                       (m.x41 - m.x42)**2 + (m.x66 - m.x67)**2) + 1/sqrt((m.x16 - m.x18)**2 + (m.x41 - m.x43)**2 + (
                       m.x66 - m.x68)**2) + 1/sqrt((m.x16 - m.x19)**2 + (m.x41 - m.x44)**2 + (m.x66 - m.x69)**2) + 1/
                       sqrt((m.x16 - m.x20)**2 + (m.x41 - m.x45)**2 + (m.x66 - m.x70)**2) + 1/sqrt((m.x16 - m.x21)**2 + 
                       (m.x41 - m.x46)**2 + (m.x66 - m.x71)**2) + 1/sqrt((m.x16 - m.x22)**2 + (m.x41 - m.x47)**2 + (
                       m.x66 - m.x72)**2) + 1/sqrt((m.x16 - m.x23)**2 + (m.x41 - m.x48)**2 + (m.x66 - m.x73)**2) + 1/
                       sqrt((m.x16 - m.x24)**2 + (m.x41 - m.x49)**2 + (m.x66 - m.x74)**2) + 1/sqrt((m.x16 - m.x25)**2 + 
                       (m.x41 - m.x50)**2 + (m.x66 - m.x75)**2) + 1/sqrt((m.x17 - m.x18)**2 + (m.x42 - m.x43)**2 + (
                       m.x67 - m.x68)**2) + 1/sqrt((m.x17 - m.x19)**2 + (m.x42 - m.x44)**2 + (m.x67 - m.x69)**2) + 1/
                       sqrt((m.x17 - m.x20)**2 + (m.x42 - m.x45)**2 + (m.x67 - m.x70)**2) + 1/sqrt((m.x17 - m.x21)**2 + 
                       (m.x42 - m.x46)**2 + (m.x67 - m.x71)**2) + 1/sqrt((m.x17 - m.x22)**2 + (m.x42 - m.x47)**2 + (
                       m.x67 - m.x72)**2) + 1/sqrt((m.x17 - m.x23)**2 + (m.x42 - m.x48)**2 + (m.x67 - m.x73)**2) + 1/
                       sqrt((m.x17 - m.x24)**2 + (m.x42 - m.x49)**2 + (m.x67 - m.x74)**2) + 1/sqrt((m.x17 - m.x25)**2 + 
                       (m.x42 - m.x50)**2 + (m.x67 - m.x75)**2) + 1/sqrt((m.x18 - m.x19)**2 + (m.x43 - m.x44)**2 + (
                       m.x68 - m.x69)**2) + 1/sqrt((m.x18 - m.x20)**2 + (m.x43 - m.x45)**2 + (m.x68 - m.x70)**2) + 1/
                       sqrt((m.x18 - m.x21)**2 + (m.x43 - m.x46)**2 + (m.x68 - m.x71)**2) + 1/sqrt((m.x18 - m.x22)**2 + 
                       (m.x43 - m.x47)**2 + (m.x68 - m.x72)**2) + 1/sqrt((m.x18 - m.x23)**2 + (m.x43 - m.x48)**2 + (
                       m.x68 - m.x73)**2) + 1/sqrt((m.x18 - m.x24)**2 + (m.x43 - m.x49)**2 + (m.x68 - m.x74)**2) + 1/
                       sqrt((m.x18 - m.x25)**2 + (m.x43 - m.x50)**2 + (m.x68 - m.x75)**2) + 1/sqrt((m.x19 - m.x20)**2 + 
                       (m.x44 - m.x45)**2 + (m.x69 - m.x70)**2) + 1/sqrt((m.x19 - m.x21)**2 + (m.x44 - m.x46)**2 + (
                       m.x69 - m.x71)**2) + 1/sqrt((m.x19 - m.x22)**2 + (m.x44 - m.x47)**2 + (m.x69 - m.x72)**2) + 1/
                       sqrt((m.x19 - m.x23)**2 + (m.x44 - m.x48)**2 + (m.x69 - m.x73)**2) + 1/sqrt((m.x19 - m.x24)**2 + 
                       (m.x44 - m.x49)**2 + (m.x69 - m.x74)**2) + 1/sqrt((m.x19 - m.x25)**2 + (m.x44 - m.x50)**2 + (
                       m.x69 - m.x75)**2) + 1/sqrt((m.x20 - m.x21)**2 + (m.x45 - m.x46)**2 + (m.x70 - m.x71)**2) + 1/
                       sqrt((m.x20 - m.x22)**2 + (m.x45 - m.x47)**2 + (m.x70 - m.x72)**2) + 1/sqrt((m.x20 - m.x23)**2 + 
                       (m.x45 - m.x48)**2 + (m.x70 - m.x73)**2) + 1/sqrt((m.x20 - m.x24)**2 + (m.x45 - m.x49)**2 + (
                       m.x70 - m.x74)**2) + 1/sqrt((m.x20 - m.x25)**2 + (m.x45 - m.x50)**2 + (m.x70 - m.x75)**2) + 1/
                       sqrt((m.x21 - m.x22)**2 + (m.x46 - m.x47)**2 + (m.x71 - m.x72)**2) + 1/sqrt((m.x21 - m.x23)**2 + 
                       (m.x46 - m.x48)**2 + (m.x71 - m.x73)**2) + 1/sqrt((m.x21 - m.x24)**2 + (m.x46 - m.x49)**2 + (
                       m.x71 - m.x74)**2) + 1/sqrt((m.x21 - m.x25)**2 + (m.x46 - m.x50)**2 + (m.x71 - m.x75)**2) + 1/
                       sqrt((m.x22 - m.x23)**2 + (m.x47 - m.x48)**2 + (m.x72 - m.x73)**2) + 1/sqrt((m.x22 - m.x24)**2 + 
                       (m.x47 - m.x49)**2 + (m.x72 - m.x74)**2) + 1/sqrt((m.x22 - m.x25)**2 + (m.x47 - m.x50)**2 + (
                       m.x72 - m.x75)**2) + 1/sqrt((m.x23 - m.x24)**2 + (m.x48 - m.x49)**2 + (m.x73 - m.x74)**2) + 1/
                       sqrt((m.x23 - m.x25)**2 + (m.x48 - m.x50)**2 + (m.x73 - m.x75)**2) + 1/sqrt((m.x24 - m.x25)**2 + 
                       (m.x49 - m.x50)**2 + (m.x74 - m.x75)**2), sense=minimize)

m.c2 = Constraint(expr=m.x1**2 + m.x26**2 + m.x51**2 == 1)

m.c3 = Constraint(expr=m.x2**2 + m.x27**2 + m.x52**2 == 1)

m.c4 = Constraint(expr=m.x3**2 + m.x28**2 + m.x53**2 == 1)

m.c5 = Constraint(expr=m.x4**2 + m.x29**2 + m.x54**2 == 1)

m.c6 = Constraint(expr=m.x5**2 + m.x30**2 + m.x55**2 == 1)

m.c7 = Constraint(expr=m.x6**2 + m.x31**2 + m.x56**2 == 1)

m.c8 = Constraint(expr=m.x7**2 + m.x32**2 + m.x57**2 == 1)

m.c9 = Constraint(expr=m.x8**2 + m.x33**2 + m.x58**2 == 1)

m.c10 = Constraint(expr=m.x9**2 + m.x34**2 + m.x59**2 == 1)

m.c11 = Constraint(expr=m.x10**2 + m.x35**2 + m.x60**2 == 1)

m.c12 = Constraint(expr=m.x11**2 + m.x36**2 + m.x61**2 == 1)

m.c13 = Constraint(expr=m.x12**2 + m.x37**2 + m.x62**2 == 1)

m.c14 = Constraint(expr=m.x13**2 + m.x38**2 + m.x63**2 == 1)

m.c15 = Constraint(expr=m.x14**2 + m.x39**2 + m.x64**2 == 1)

m.c16 = Constraint(expr=m.x15**2 + m.x40**2 + m.x65**2 == 1)

m.c17 = Constraint(expr=m.x16**2 + m.x41**2 + m.x66**2 == 1)

m.c18 = Constraint(expr=m.x17**2 + m.x42**2 + m.x67**2 == 1)

m.c19 = Constraint(expr=m.x18**2 + m.x43**2 + m.x68**2 == 1)

m.c20 = Constraint(expr=m.x19**2 + m.x44**2 + m.x69**2 == 1)

m.c21 = Constraint(expr=m.x20**2 + m.x45**2 + m.x70**2 == 1)

m.c22 = Constraint(expr=m.x21**2 + m.x46**2 + m.x71**2 == 1)

m.c23 = Constraint(expr=m.x22**2 + m.x47**2 + m.x72**2 == 1)

m.c24 = Constraint(expr=m.x23**2 + m.x48**2 + m.x73**2 == 1)

m.c25 = Constraint(expr=m.x24**2 + m.x49**2 + m.x74**2 == 1)

m.c26 = Constraint(expr=m.x25**2 + m.x50**2 + m.x75**2 == 1)
