#  NLP written by GAMS Convert at 04/21/18 13:51:41
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         51       51        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        151      151        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        301        1      300        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(None,None),initialize=0.412915943504718)
m.x2 = Var(within=Reals,bounds=(None,None),initialize=0.3838430960645)
m.x3 = Var(within=Reals,bounds=(None,None),initialize=-0.875163658226184)
m.x4 = Var(within=Reals,bounds=(None,None),initialize=-0.245760628172242)
m.x5 = Var(within=Reals,bounds=(None,None),initialize=-0.0702993897778083)
m.x6 = Var(within=Reals,bounds=(None,None),initialize=0.0513742837947186)
m.x7 = Var(within=Reals,bounds=(None,None),initialize=-0.530077754824334)
m.x8 = Var(within=Reals,bounds=(None,None),initialize=0.612931927822947)
m.x9 = Var(within=Reals,bounds=(None,None),initialize=0.0902147810017304)
m.x10 = Var(within=Reals,bounds=(None,None),initialize=-0.607029792519237)
m.x11 = Var(within=Reals,bounds=(None,None),initialize=0.226602472891738)
m.x12 = Var(within=Reals,bounds=(None,None),initialize=-0.461415158914053)
m.x13 = Var(within=Reals,bounds=(None,None),initialize=0.995212907982449)
m.x14 = Var(within=Reals,bounds=(None,None),initialize=0.0543381770090441)
m.x15 = Var(within=Reals,bounds=(None,None),initialize=0.361698274073243)
m.x16 = Var(within=Reals,bounds=(None,None),initialize=-0.068382870884331)
m.x17 = Var(within=Reals,bounds=(None,None),initialize=0.519241857953898)
m.x18 = Var(within=Reals,bounds=(None,None),initialize=-0.00046974709253693)
m.x19 = Var(within=Reals,bounds=(None,None),initialize=-0.458480726824807)
m.x20 = Var(within=Reals,bounds=(None,None),initialize=-0.829624965949446)
m.x21 = Var(within=Reals,bounds=(None,None),initialize=-0.43975255775501)
m.x22 = Var(within=Reals,bounds=(None,None),initialize=-0.416033582294912)
m.x23 = Var(within=Reals,bounds=(None,None),initialize=0.270123381197924)
m.x24 = Var(within=Reals,bounds=(None,None),initialize=0.121889781143431)
m.x25 = Var(within=Reals,bounds=(None,None),initialize=-0.78773772401658)
m.x26 = Var(within=Reals,bounds=(None,None),initialize=0.306186483969191)
m.x27 = Var(within=Reals,bounds=(None,None),initialize=0.0972891428088812)
m.x28 = Var(within=Reals,bounds=(None,None),initialize=-0.1939877314045)
m.x29 = Var(within=Reals,bounds=(None,None),initialize=0.114781428562405)
m.x30 = Var(within=Reals,bounds=(None,None),initialize=-0.0713821085130848)
m.x31 = Var(within=Reals,bounds=(None,None),initialize=0.45566318842306)
m.x32 = Var(within=Reals,bounds=(None,None),initialize=-0.0159124038305379)
m.x33 = Var(within=Reals,bounds=(None,None),initialize=0.400811568951403)
m.x34 = Var(within=Reals,bounds=(None,None),initialize=0.69574264402932)
m.x35 = Var(within=Reals,bounds=(None,None),initialize=-0.0433905175011045)
m.x36 = Var(within=Reals,bounds=(None,None),initialize=-0.116090216013241)
m.x37 = Var(within=Reals,bounds=(None,None),initialize=-0.715907336995362)
m.x38 = Var(within=Reals,bounds=(None,None),initialize=-0.143124356348335)
m.x39 = Var(within=Reals,bounds=(None,None),initialize=-0.587140189822367)
m.x40 = Var(within=Reals,bounds=(None,None),initialize=-0.110020382752765)
m.x41 = Var(within=Reals,bounds=(None,None),initialize=-0.0171893128215058)
m.x42 = Var(within=Reals,bounds=(None,None),initialize=0.677951797257343)
m.x43 = Var(within=Reals,bounds=(None,None),initialize=-0.361711133483903)
m.x44 = Var(within=Reals,bounds=(None,None),initialize=0.62874865356649)
m.x45 = Var(within=Reals,bounds=(None,None),initialize=-0.500538790690622)
m.x46 = Var(within=Reals,bounds=(None,None),initialize=0.111577365020531)
m.x47 = Var(within=Reals,bounds=(None,None),initialize=-0.223543148037772)
m.x48 = Var(within=Reals,bounds=(None,None),initialize=-0.685468159033124)
m.x49 = Var(within=Reals,bounds=(None,None),initialize=0.0216693946753158)
m.x50 = Var(within=Reals,bounds=(None,None),initialize=-0.287417083131714)
m.x51 = Var(within=Reals,bounds=(None,None),initialize=0.771020737311453)
m.x52 = Var(within=Reals,bounds=(None,None),initialize=-0.578255330779784)
m.x53 = Var(within=Reals,bounds=(None,None),initialize=-0.286641581254972)
m.x54 = Var(within=Reals,bounds=(None,None),initialize=0.738368670585217)
m.x55 = Var(within=Reals,bounds=(None,None),initialize=0.258809684877274)
m.x56 = Var(within=Reals,bounds=(None,None),initialize=0.312323590525228)
m.x57 = Var(within=Reals,bounds=(None,None),initialize=0.731225797811487)
m.x58 = Var(within=Reals,bounds=(None,None),initialize=-0.77729603067813)
m.x59 = Var(within=Reals,bounds=(None,None),initialize=0.0404702297131352)
m.x60 = Var(within=Reals,bounds=(None,None),initialize=-0.00080350903065797)
m.x61 = Var(within=Reals,bounds=(None,None),initialize=-0.00268022003502952)
m.x62 = Var(within=Reals,bounds=(None,None),initialize=-0.248903894664738)
m.x63 = Var(within=Reals,bounds=(None,None),initialize=-0.0555034948358933)
m.x64 = Var(within=Reals,bounds=(None,None),initialize=-0.70455301525129)
m.x65 = Var(within=Reals,bounds=(None,None),initialize=0.388543566592611)
m.x66 = Var(within=Reals,bounds=(None,None),initialize=-0.0823639193144952)
m.x67 = Var(within=Reals,bounds=(None,None),initialize=0.812741649197509)
m.x68 = Var(within=Reals,bounds=(None,None),initialize=0.928346955901181)
m.x69 = Var(within=Reals,bounds=(None,None),initialize=-0.820835634806987)
m.x70 = Var(within=Reals,bounds=(None,None),initialize=0.356807331541876)
m.x71 = Var(within=Reals,bounds=(None,None),initialize=0.533612477974662)
m.x72 = Var(within=Reals,bounds=(None,None),initialize=0.561849569548856)
m.x73 = Var(within=Reals,bounds=(None,None),initialize=0.293109181957298)
m.x74 = Var(within=Reals,bounds=(None,None),initialize=0.167992724833905)
m.x75 = Var(within=Reals,bounds=(None,None),initialize=-0.493781355212929)
m.x76 = Var(within=Reals,bounds=(None,None),initialize=-0.549625073571091)
m.x77 = Var(within=Reals,bounds=(None,None),initialize=0.803209607420834)
m.x78 = Var(within=Reals,bounds=(None,None),initialize=-0.33149728022952)
m.x79 = Var(within=Reals,bounds=(None,None),initialize=-0.700258736193931)
m.x80 = Var(within=Reals,bounds=(None,None),initialize=0.203640999103717)
m.x81 = Var(within=Reals,bounds=(None,None),initialize=0.379337496768655)
m.x82 = Var(within=Reals,bounds=(None,None),initialize=-0.000238458138369305)
m.x83 = Var(within=Reals,bounds=(None,None),initialize=0.633095941850339)
m.x84 = Var(within=Reals,bounds=(None,None),initialize=-0.718290996434478)
m.x85 = Var(within=Reals,bounds=(None,None),initialize=0.455524269739257)
m.x86 = Var(within=Reals,bounds=(None,None),initialize=0.507154876398668)
m.x87 = Var(within=Reals,bounds=(None,None),initialize=-0.479694970009749)
m.x88 = Var(within=Reals,bounds=(None,None),initialize=-0.82678325367307)
m.x89 = Var(within=Reals,bounds=(None,None),initialize=-0.611612577688738)
m.x90 = Var(within=Reals,bounds=(None,None),initialize=0.0254664921612672)
m.x91 = Var(within=Reals,bounds=(None,None),initialize=0.0104141064003352)
m.x92 = Var(within=Reals,bounds=(None,None),initialize=0.618411541089136)
m.x93 = Var(within=Reals,bounds=(None,None),initialize=0.847347064020686)
m.x94 = Var(within=Reals,bounds=(None,None),initialize=0.189334135530726)
m.x95 = Var(within=Reals,bounds=(None,None),initialize=0.804834808110123)
m.x96 = Var(within=Reals,bounds=(None,None),initialize=0.24546802245074)
m.x97 = Var(within=Reals,bounds=(None,None),initialize=-0.290924922947003)
m.x98 = Var(within=Reals,bounds=(None,None),initialize=-0.275117341525081)
m.x99 = Var(within=Reals,bounds=(None,None),initialize=-0.171863346376444)
m.x100 = Var(within=Reals,bounds=(None,None),initialize=0.927914864005114)
m.x101 = Var(within=Reals,bounds=(None,None),initialize=-0.484796293545353)
m.x102 = Var(within=Reals,bounds=(None,None),initialize=-0.719920308109434)
m.x103 = Var(within=Reals,bounds=(None,None),initialize=-0.389775801218869)
m.x104 = Var(within=Reals,bounds=(None,None),initialize=0.628023423081181)
m.x105 = Var(within=Reals,bounds=(None,None),initialize=0.963366774811439)
m.x106 = Var(within=Reals,bounds=(None,None),initialize=0.948585609086502)
m.x107 = Var(within=Reals,bounds=(None,None),initialize=-0.429332512693072)
m.x108 = Var(within=Reals,bounds=(None,None),initialize=-0.141863781661385)
m.x109 = Var(within=Reals,bounds=(None,None),initialize=0.995099720528438)
m.x110 = Var(within=Reals,bounds=(None,None),initialize=-0.794678667995618)
m.x111 = Var(within=Reals,bounds=(None,None),initialize=0.973983642419067)
m.x112 = Var(within=Reals,bounds=(None,None),initialize=0.851553229308094)
m.x113 = Var(within=Reals,bounds=(None,None),initialize=-0.080440225298782)
m.x114 = Var(within=Reals,bounds=(None,None),initialize=-0.707567955195577)
m.x115 = Var(within=Reals,bounds=(None,None),initialize=0.847471684123977)
m.x116 = Var(within=Reals,bounds=(None,None),initialize=0.994253472593771)
m.x117 = Var(within=Reals,bounds=(None,None),initialize=-0.264270514072789)
m.x118 = Var(within=Reals,bounds=(None,None),initialize=-0.371714552858346)
m.x119 = Var(within=Reals,bounds=(None,None),initialize=0.340623375241935)
m.x120 = Var(within=Reals,bounds=(None,None),initialize=0.429430953741514)
m.x121 = Var(within=Reals,bounds=(None,None),initialize=0.722409448510793)
m.x122 = Var(within=Reals,bounds=(None,None),initialize=0.715011272359134)
m.x123 = Var(within=Reals,bounds=(None,None),initialize=0.917126145294378)
m.x124 = Var(within=Reals,bounds=(None,None),initialize=-0.978223556072786)
m.x125 = Var(within=Reals,bounds=(None,None),initialize=0.368305920947874)
m.x126 = Var(within=Reals,bounds=(None,None),initialize=-0.777278660157705)
m.x127 = Var(within=Reals,bounds=(None,None),initialize=0.587698178692416)
m.x128 = Var(within=Reals,bounds=(None,None),initialize=0.923297521530826)
m.x129 = Var(within=Reals,bounds=(None,None),initialize=-0.70460125322146)
m.x130 = Var(within=Reals,bounds=(None,None),initialize=0.976439930599044)
m.x131 = Var(within=Reals,bounds=(None,None),initialize=0.805278909609224)
m.x132 = Var(within=Reals,bounds=(None,None),initialize=0.999873361252339)
m.x133 = Var(within=Reals,bounds=(None,None),initialize=0.662223236233331)
m.x134 = Var(within=Reals,bounds=(None,None),initialize=0.00046660503194269)
m.x135 = Var(within=Reals,bounds=(None,None),initialize=0.8891652842242)
m.x136 = Var(within=Reals,bounds=(None,None),initialize=0.854000581434843)
m.x137 = Var(within=Reals,bounds=(None,None),initialize=0.507315898216836)
m.x138 = Var(within=Reals,bounds=(None,None),initialize=0.544008152572778)
m.x139 = Var(within=Reals,bounds=(None,None),initialize=0.530279598238789)
m.x140 = Var(within=Reals,bounds=(None,None),initialize=-0.993603025939402)
m.x141 = Var(within=Reals,bounds=(None,None),initialize=-0.999798016557648)
m.x142 = Var(within=Reals,bounds=(None,None),initialize=0.397427385119971)
m.x143 = Var(within=Reals,bounds=(None,None),initialize=0.388803303753084)
m.x144 = Var(within=Reals,bounds=(None,None),initialize=-0.754206679737828)
m.x145 = Var(within=Reals,bounds=(None,None),initialize=0.318907275972674)
m.x146 = Var(within=Reals,bounds=(None,None),initialize=-0.96296206652661)
m.x147 = Var(within=Reals,bounds=(None,None),initialize=0.930264021755997)
m.x148 = Var(within=Reals,bounds=(None,None),initialize=-0.674124507301071)
m.x149 = Var(within=Reals,bounds=(None,None),initialize=0.984882443496022)
m.x150 = Var(within=Reals,bounds=(None,None),initialize=-0.237414038090479)

m.obj = Objective(expr=1/sqrt((m.x1 - m.x2)**2 + (m.x51 - m.x52)**2 + (m.x101 - m.x102)**2) + 1/sqrt((m.x1 - m.x3)**2 + 
                       (m.x51 - m.x53)**2 + (m.x101 - m.x103)**2) + 1/sqrt((m.x1 - m.x4)**2 + (m.x51 - m.x54)**2 + (
                       m.x101 - m.x104)**2) + 1/sqrt((m.x1 - m.x5)**2 + (m.x51 - m.x55)**2 + (m.x101 - m.x105)**2) + 1/
                       sqrt((m.x1 - m.x6)**2 + (m.x51 - m.x56)**2 + (m.x101 - m.x106)**2) + 1/sqrt((m.x1 - m.x7)**2 + (
                       m.x51 - m.x57)**2 + (m.x101 - m.x107)**2) + 1/sqrt((m.x1 - m.x8)**2 + (m.x51 - m.x58)**2 + (
                       m.x101 - m.x108)**2) + 1/sqrt((m.x1 - m.x9)**2 + (m.x51 - m.x59)**2 + (m.x101 - m.x109)**2) + 1/
                       sqrt((m.x1 - m.x10)**2 + (m.x51 - m.x60)**2 + (m.x101 - m.x110)**2) + 1/sqrt((m.x1 - m.x11)**2 + 
                       (m.x51 - m.x61)**2 + (m.x101 - m.x111)**2) + 1/sqrt((m.x1 - m.x12)**2 + (m.x51 - m.x62)**2 + (
                       m.x101 - m.x112)**2) + 1/sqrt((m.x1 - m.x13)**2 + (m.x51 - m.x63)**2 + (m.x101 - m.x113)**2) + 1/
                       sqrt((m.x1 - m.x14)**2 + (m.x51 - m.x64)**2 + (m.x101 - m.x114)**2) + 1/sqrt((m.x1 - m.x15)**2 + 
                       (m.x51 - m.x65)**2 + (m.x101 - m.x115)**2) + 1/sqrt((m.x1 - m.x16)**2 + (m.x51 - m.x66)**2 + (
                       m.x101 - m.x116)**2) + 1/sqrt((m.x1 - m.x17)**2 + (m.x51 - m.x67)**2 + (m.x101 - m.x117)**2) + 1/
                       sqrt((m.x1 - m.x18)**2 + (m.x51 - m.x68)**2 + (m.x101 - m.x118)**2) + 1/sqrt((m.x1 - m.x19)**2 + 
                       (m.x51 - m.x69)**2 + (m.x101 - m.x119)**2) + 1/sqrt((m.x1 - m.x20)**2 + (m.x51 - m.x70)**2 + (
                       m.x101 - m.x120)**2) + 1/sqrt((m.x1 - m.x21)**2 + (m.x51 - m.x71)**2 + (m.x101 - m.x121)**2) + 1/
                       sqrt((m.x1 - m.x22)**2 + (m.x51 - m.x72)**2 + (m.x101 - m.x122)**2) + 1/sqrt((m.x1 - m.x23)**2 + 
                       (m.x51 - m.x73)**2 + (m.x101 - m.x123)**2) + 1/sqrt((m.x1 - m.x24)**2 + (m.x51 - m.x74)**2 + (
                       m.x101 - m.x124)**2) + 1/sqrt((m.x1 - m.x25)**2 + (m.x51 - m.x75)**2 + (m.x101 - m.x125)**2) + 1/
                       sqrt((m.x1 - m.x26)**2 + (m.x51 - m.x76)**2 + (m.x101 - m.x126)**2) + 1/sqrt((m.x1 - m.x27)**2 + 
                       (m.x51 - m.x77)**2 + (m.x101 - m.x127)**2) + 1/sqrt((m.x1 - m.x28)**2 + (m.x51 - m.x78)**2 + (
                       m.x101 - m.x128)**2) + 1/sqrt((m.x1 - m.x29)**2 + (m.x51 - m.x79)**2 + (m.x101 - m.x129)**2) + 1/
                       sqrt((m.x1 - m.x30)**2 + (m.x51 - m.x80)**2 + (m.x101 - m.x130)**2) + 1/sqrt((m.x1 - m.x31)**2 + 
                       (m.x51 - m.x81)**2 + (m.x101 - m.x131)**2) + 1/sqrt((m.x1 - m.x32)**2 + (m.x51 - m.x82)**2 + (
                       m.x101 - m.x132)**2) + 1/sqrt((m.x1 - m.x33)**2 + (m.x51 - m.x83)**2 + (m.x101 - m.x133)**2) + 1/
                       sqrt((m.x1 - m.x34)**2 + (m.x51 - m.x84)**2 + (m.x101 - m.x134)**2) + 1/sqrt((m.x1 - m.x35)**2 + 
                       (m.x51 - m.x85)**2 + (m.x101 - m.x135)**2) + 1/sqrt((m.x1 - m.x36)**2 + (m.x51 - m.x86)**2 + (
                       m.x101 - m.x136)**2) + 1/sqrt((m.x1 - m.x37)**2 + (m.x51 - m.x87)**2 + (m.x101 - m.x137)**2) + 1/
                       sqrt((m.x1 - m.x38)**2 + (m.x51 - m.x88)**2 + (m.x101 - m.x138)**2) + 1/sqrt((m.x1 - m.x39)**2 + 
                       (m.x51 - m.x89)**2 + (m.x101 - m.x139)**2) + 1/sqrt((m.x1 - m.x40)**2 + (m.x51 - m.x90)**2 + (
                       m.x101 - m.x140)**2) + 1/sqrt((m.x1 - m.x41)**2 + (m.x51 - m.x91)**2 + (m.x101 - m.x141)**2) + 1/
                       sqrt((m.x1 - m.x42)**2 + (m.x51 - m.x92)**2 + (m.x101 - m.x142)**2) + 1/sqrt((m.x1 - m.x43)**2 + 
                       (m.x51 - m.x93)**2 + (m.x101 - m.x143)**2) + 1/sqrt((m.x1 - m.x44)**2 + (m.x51 - m.x94)**2 + (
                       m.x101 - m.x144)**2) + 1/sqrt((m.x1 - m.x45)**2 + (m.x51 - m.x95)**2 + (m.x101 - m.x145)**2) + 1/
                       sqrt((m.x1 - m.x46)**2 + (m.x51 - m.x96)**2 + (m.x101 - m.x146)**2) + 1/sqrt((m.x1 - m.x47)**2 + 
                       (m.x51 - m.x97)**2 + (m.x101 - m.x147)**2) + 1/sqrt((m.x1 - m.x48)**2 + (m.x51 - m.x98)**2 + (
                       m.x101 - m.x148)**2) + 1/sqrt((m.x1 - m.x49)**2 + (m.x51 - m.x99)**2 + (m.x101 - m.x149)**2) + 1/
                       sqrt((m.x1 - m.x50)**2 + (m.x51 - m.x100)**2 + (m.x101 - m.x150)**2) + 1/sqrt((m.x2 - m.x3)**2 + 
                       (m.x52 - m.x53)**2 + (m.x102 - m.x103)**2) + 1/sqrt((m.x2 - m.x4)**2 + (m.x52 - m.x54)**2 + (
                       m.x102 - m.x104)**2) + 1/sqrt((m.x2 - m.x5)**2 + (m.x52 - m.x55)**2 + (m.x102 - m.x105)**2) + 1/
                       sqrt((m.x2 - m.x6)**2 + (m.x52 - m.x56)**2 + (m.x102 - m.x106)**2) + 1/sqrt((m.x2 - m.x7)**2 + (
                       m.x52 - m.x57)**2 + (m.x102 - m.x107)**2) + 1/sqrt((m.x2 - m.x8)**2 + (m.x52 - m.x58)**2 + (
                       m.x102 - m.x108)**2) + 1/sqrt((m.x2 - m.x9)**2 + (m.x52 - m.x59)**2 + (m.x102 - m.x109)**2) + 1/
                       sqrt((m.x2 - m.x10)**2 + (m.x52 - m.x60)**2 + (m.x102 - m.x110)**2) + 1/sqrt((m.x2 - m.x11)**2 + 
                       (m.x52 - m.x61)**2 + (m.x102 - m.x111)**2) + 1/sqrt((m.x2 - m.x12)**2 + (m.x52 - m.x62)**2 + (
                       m.x102 - m.x112)**2) + 1/sqrt((m.x2 - m.x13)**2 + (m.x52 - m.x63)**2 + (m.x102 - m.x113)**2) + 1/
                       sqrt((m.x2 - m.x14)**2 + (m.x52 - m.x64)**2 + (m.x102 - m.x114)**2) + 1/sqrt((m.x2 - m.x15)**2 + 
                       (m.x52 - m.x65)**2 + (m.x102 - m.x115)**2) + 1/sqrt((m.x2 - m.x16)**2 + (m.x52 - m.x66)**2 + (
                       m.x102 - m.x116)**2) + 1/sqrt((m.x2 - m.x17)**2 + (m.x52 - m.x67)**2 + (m.x102 - m.x117)**2) + 1/
                       sqrt((m.x2 - m.x18)**2 + (m.x52 - m.x68)**2 + (m.x102 - m.x118)**2) + 1/sqrt((m.x2 - m.x19)**2 + 
                       (m.x52 - m.x69)**2 + (m.x102 - m.x119)**2) + 1/sqrt((m.x2 - m.x20)**2 + (m.x52 - m.x70)**2 + (
                       m.x102 - m.x120)**2) + 1/sqrt((m.x2 - m.x21)**2 + (m.x52 - m.x71)**2 + (m.x102 - m.x121)**2) + 1/
                       sqrt((m.x2 - m.x22)**2 + (m.x52 - m.x72)**2 + (m.x102 - m.x122)**2) + 1/sqrt((m.x2 - m.x23)**2 + 
                       (m.x52 - m.x73)**2 + (m.x102 - m.x123)**2) + 1/sqrt((m.x2 - m.x24)**2 + (m.x52 - m.x74)**2 + (
                       m.x102 - m.x124)**2) + 1/sqrt((m.x2 - m.x25)**2 + (m.x52 - m.x75)**2 + (m.x102 - m.x125)**2) + 1/
                       sqrt((m.x2 - m.x26)**2 + (m.x52 - m.x76)**2 + (m.x102 - m.x126)**2) + 1/sqrt((m.x2 - m.x27)**2 + 
                       (m.x52 - m.x77)**2 + (m.x102 - m.x127)**2) + 1/sqrt((m.x2 - m.x28)**2 + (m.x52 - m.x78)**2 + (
                       m.x102 - m.x128)**2) + 1/sqrt((m.x2 - m.x29)**2 + (m.x52 - m.x79)**2 + (m.x102 - m.x129)**2) + 1/
                       sqrt((m.x2 - m.x30)**2 + (m.x52 - m.x80)**2 + (m.x102 - m.x130)**2) + 1/sqrt((m.x2 - m.x31)**2 + 
                       (m.x52 - m.x81)**2 + (m.x102 - m.x131)**2) + 1/sqrt((m.x2 - m.x32)**2 + (m.x52 - m.x82)**2 + (
                       m.x102 - m.x132)**2) + 1/sqrt((m.x2 - m.x33)**2 + (m.x52 - m.x83)**2 + (m.x102 - m.x133)**2) + 1/
                       sqrt((m.x2 - m.x34)**2 + (m.x52 - m.x84)**2 + (m.x102 - m.x134)**2) + 1/sqrt((m.x2 - m.x35)**2 + 
                       (m.x52 - m.x85)**2 + (m.x102 - m.x135)**2) + 1/sqrt((m.x2 - m.x36)**2 + (m.x52 - m.x86)**2 + (
                       m.x102 - m.x136)**2) + 1/sqrt((m.x2 - m.x37)**2 + (m.x52 - m.x87)**2 + (m.x102 - m.x137)**2) + 1/
                       sqrt((m.x2 - m.x38)**2 + (m.x52 - m.x88)**2 + (m.x102 - m.x138)**2) + 1/sqrt((m.x2 - m.x39)**2 + 
                       (m.x52 - m.x89)**2 + (m.x102 - m.x139)**2) + 1/sqrt((m.x2 - m.x40)**2 + (m.x52 - m.x90)**2 + (
                       m.x102 - m.x140)**2) + 1/sqrt((m.x2 - m.x41)**2 + (m.x52 - m.x91)**2 + (m.x102 - m.x141)**2) + 1/
                       sqrt((m.x2 - m.x42)**2 + (m.x52 - m.x92)**2 + (m.x102 - m.x142)**2) + 1/sqrt((m.x2 - m.x43)**2 + 
                       (m.x52 - m.x93)**2 + (m.x102 - m.x143)**2) + 1/sqrt((m.x2 - m.x44)**2 + (m.x52 - m.x94)**2 + (
                       m.x102 - m.x144)**2) + 1/sqrt((m.x2 - m.x45)**2 + (m.x52 - m.x95)**2 + (m.x102 - m.x145)**2) + 1/
                       sqrt((m.x2 - m.x46)**2 + (m.x52 - m.x96)**2 + (m.x102 - m.x146)**2) + 1/sqrt((m.x2 - m.x47)**2 + 
                       (m.x52 - m.x97)**2 + (m.x102 - m.x147)**2) + 1/sqrt((m.x2 - m.x48)**2 + (m.x52 - m.x98)**2 + (
                       m.x102 - m.x148)**2) + 1/sqrt((m.x2 - m.x49)**2 + (m.x52 - m.x99)**2 + (m.x102 - m.x149)**2) + 1/
                       sqrt((m.x2 - m.x50)**2 + (m.x52 - m.x100)**2 + (m.x102 - m.x150)**2) + 1/sqrt((m.x3 - m.x4)**2 + 
                       (m.x53 - m.x54)**2 + (m.x103 - m.x104)**2) + 1/sqrt((m.x3 - m.x5)**2 + (m.x53 - m.x55)**2 + (
                       m.x103 - m.x105)**2) + 1/sqrt((m.x3 - m.x6)**2 + (m.x53 - m.x56)**2 + (m.x103 - m.x106)**2) + 1/
                       sqrt((m.x3 - m.x7)**2 + (m.x53 - m.x57)**2 + (m.x103 - m.x107)**2) + 1/sqrt((m.x3 - m.x8)**2 + (
                       m.x53 - m.x58)**2 + (m.x103 - m.x108)**2) + 1/sqrt((m.x3 - m.x9)**2 + (m.x53 - m.x59)**2 + (
                       m.x103 - m.x109)**2) + 1/sqrt((m.x3 - m.x10)**2 + (m.x53 - m.x60)**2 + (m.x103 - m.x110)**2) + 1/
                       sqrt((m.x3 - m.x11)**2 + (m.x53 - m.x61)**2 + (m.x103 - m.x111)**2) + 1/sqrt((m.x3 - m.x12)**2 + 
                       (m.x53 - m.x62)**2 + (m.x103 - m.x112)**2) + 1/sqrt((m.x3 - m.x13)**2 + (m.x53 - m.x63)**2 + (
                       m.x103 - m.x113)**2) + 1/sqrt((m.x3 - m.x14)**2 + (m.x53 - m.x64)**2 + (m.x103 - m.x114)**2) + 1/
                       sqrt((m.x3 - m.x15)**2 + (m.x53 - m.x65)**2 + (m.x103 - m.x115)**2) + 1/sqrt((m.x3 - m.x16)**2 + 
                       (m.x53 - m.x66)**2 + (m.x103 - m.x116)**2) + 1/sqrt((m.x3 - m.x17)**2 + (m.x53 - m.x67)**2 + (
                       m.x103 - m.x117)**2) + 1/sqrt((m.x3 - m.x18)**2 + (m.x53 - m.x68)**2 + (m.x103 - m.x118)**2) + 1/
                       sqrt((m.x3 - m.x19)**2 + (m.x53 - m.x69)**2 + (m.x103 - m.x119)**2) + 1/sqrt((m.x3 - m.x20)**2 + 
                       (m.x53 - m.x70)**2 + (m.x103 - m.x120)**2) + 1/sqrt((m.x3 - m.x21)**2 + (m.x53 - m.x71)**2 + (
                       m.x103 - m.x121)**2) + 1/sqrt((m.x3 - m.x22)**2 + (m.x53 - m.x72)**2 + (m.x103 - m.x122)**2) + 1/
                       sqrt((m.x3 - m.x23)**2 + (m.x53 - m.x73)**2 + (m.x103 - m.x123)**2) + 1/sqrt((m.x3 - m.x24)**2 + 
                       (m.x53 - m.x74)**2 + (m.x103 - m.x124)**2) + 1/sqrt((m.x3 - m.x25)**2 + (m.x53 - m.x75)**2 + (
                       m.x103 - m.x125)**2) + 1/sqrt((m.x3 - m.x26)**2 + (m.x53 - m.x76)**2 + (m.x103 - m.x126)**2) + 1/
                       sqrt((m.x3 - m.x27)**2 + (m.x53 - m.x77)**2 + (m.x103 - m.x127)**2) + 1/sqrt((m.x3 - m.x28)**2 + 
                       (m.x53 - m.x78)**2 + (m.x103 - m.x128)**2) + 1/sqrt((m.x3 - m.x29)**2 + (m.x53 - m.x79)**2 + (
                       m.x103 - m.x129)**2) + 1/sqrt((m.x3 - m.x30)**2 + (m.x53 - m.x80)**2 + (m.x103 - m.x130)**2) + 1/
                       sqrt((m.x3 - m.x31)**2 + (m.x53 - m.x81)**2 + (m.x103 - m.x131)**2) + 1/sqrt((m.x3 - m.x32)**2 + 
                       (m.x53 - m.x82)**2 + (m.x103 - m.x132)**2) + 1/sqrt((m.x3 - m.x33)**2 + (m.x53 - m.x83)**2 + (
                       m.x103 - m.x133)**2) + 1/sqrt((m.x3 - m.x34)**2 + (m.x53 - m.x84)**2 + (m.x103 - m.x134)**2) + 1/
                       sqrt((m.x3 - m.x35)**2 + (m.x53 - m.x85)**2 + (m.x103 - m.x135)**2) + 1/sqrt((m.x3 - m.x36)**2 + 
                       (m.x53 - m.x86)**2 + (m.x103 - m.x136)**2) + 1/sqrt((m.x3 - m.x37)**2 + (m.x53 - m.x87)**2 + (
                       m.x103 - m.x137)**2) + 1/sqrt((m.x3 - m.x38)**2 + (m.x53 - m.x88)**2 + (m.x103 - m.x138)**2) + 1/
                       sqrt((m.x3 - m.x39)**2 + (m.x53 - m.x89)**2 + (m.x103 - m.x139)**2) + 1/sqrt((m.x3 - m.x40)**2 + 
                       (m.x53 - m.x90)**2 + (m.x103 - m.x140)**2) + 1/sqrt((m.x3 - m.x41)**2 + (m.x53 - m.x91)**2 + (
                       m.x103 - m.x141)**2) + 1/sqrt((m.x3 - m.x42)**2 + (m.x53 - m.x92)**2 + (m.x103 - m.x142)**2) + 1/
                       sqrt((m.x3 - m.x43)**2 + (m.x53 - m.x93)**2 + (m.x103 - m.x143)**2) + 1/sqrt((m.x3 - m.x44)**2 + 
                       (m.x53 - m.x94)**2 + (m.x103 - m.x144)**2) + 1/sqrt((m.x3 - m.x45)**2 + (m.x53 - m.x95)**2 + (
                       m.x103 - m.x145)**2) + 1/sqrt((m.x3 - m.x46)**2 + (m.x53 - m.x96)**2 + (m.x103 - m.x146)**2) + 1/
                       sqrt((m.x3 - m.x47)**2 + (m.x53 - m.x97)**2 + (m.x103 - m.x147)**2) + 1/sqrt((m.x3 - m.x48)**2 + 
                       (m.x53 - m.x98)**2 + (m.x103 - m.x148)**2) + 1/sqrt((m.x3 - m.x49)**2 + (m.x53 - m.x99)**2 + (
                       m.x103 - m.x149)**2) + 1/sqrt((m.x3 - m.x50)**2 + (m.x53 - m.x100)**2 + (m.x103 - m.x150)**2) + 1
                       /sqrt((m.x4 - m.x5)**2 + (m.x54 - m.x55)**2 + (m.x104 - m.x105)**2) + 1/sqrt((m.x4 - m.x6)**2 + (
                       m.x54 - m.x56)**2 + (m.x104 - m.x106)**2) + 1/sqrt((m.x4 - m.x7)**2 + (m.x54 - m.x57)**2 + (
                       m.x104 - m.x107)**2) + 1/sqrt((m.x4 - m.x8)**2 + (m.x54 - m.x58)**2 + (m.x104 - m.x108)**2) + 1/
                       sqrt((m.x4 - m.x9)**2 + (m.x54 - m.x59)**2 + (m.x104 - m.x109)**2) + 1/sqrt((m.x4 - m.x10)**2 + (
                       m.x54 - m.x60)**2 + (m.x104 - m.x110)**2) + 1/sqrt((m.x4 - m.x11)**2 + (m.x54 - m.x61)**2 + (
                       m.x104 - m.x111)**2) + 1/sqrt((m.x4 - m.x12)**2 + (m.x54 - m.x62)**2 + (m.x104 - m.x112)**2) + 1/
                       sqrt((m.x4 - m.x13)**2 + (m.x54 - m.x63)**2 + (m.x104 - m.x113)**2) + 1/sqrt((m.x4 - m.x14)**2 + 
                       (m.x54 - m.x64)**2 + (m.x104 - m.x114)**2) + 1/sqrt((m.x4 - m.x15)**2 + (m.x54 - m.x65)**2 + (
                       m.x104 - m.x115)**2) + 1/sqrt((m.x4 - m.x16)**2 + (m.x54 - m.x66)**2 + (m.x104 - m.x116)**2) + 1/
                       sqrt((m.x4 - m.x17)**2 + (m.x54 - m.x67)**2 + (m.x104 - m.x117)**2) + 1/sqrt((m.x4 - m.x18)**2 + 
                       (m.x54 - m.x68)**2 + (m.x104 - m.x118)**2) + 1/sqrt((m.x4 - m.x19)**2 + (m.x54 - m.x69)**2 + (
                       m.x104 - m.x119)**2) + 1/sqrt((m.x4 - m.x20)**2 + (m.x54 - m.x70)**2 + (m.x104 - m.x120)**2) + 1/
                       sqrt((m.x4 - m.x21)**2 + (m.x54 - m.x71)**2 + (m.x104 - m.x121)**2) + 1/sqrt((m.x4 - m.x22)**2 + 
                       (m.x54 - m.x72)**2 + (m.x104 - m.x122)**2) + 1/sqrt((m.x4 - m.x23)**2 + (m.x54 - m.x73)**2 + (
                       m.x104 - m.x123)**2) + 1/sqrt((m.x4 - m.x24)**2 + (m.x54 - m.x74)**2 + (m.x104 - m.x124)**2) + 1/
                       sqrt((m.x4 - m.x25)**2 + (m.x54 - m.x75)**2 + (m.x104 - m.x125)**2) + 1/sqrt((m.x4 - m.x26)**2 + 
                       (m.x54 - m.x76)**2 + (m.x104 - m.x126)**2) + 1/sqrt((m.x4 - m.x27)**2 + (m.x54 - m.x77)**2 + (
                       m.x104 - m.x127)**2) + 1/sqrt((m.x4 - m.x28)**2 + (m.x54 - m.x78)**2 + (m.x104 - m.x128)**2) + 1/
                       sqrt((m.x4 - m.x29)**2 + (m.x54 - m.x79)**2 + (m.x104 - m.x129)**2) + 1/sqrt((m.x4 - m.x30)**2 + 
                       (m.x54 - m.x80)**2 + (m.x104 - m.x130)**2) + 1/sqrt((m.x4 - m.x31)**2 + (m.x54 - m.x81)**2 + (
                       m.x104 - m.x131)**2) + 1/sqrt((m.x4 - m.x32)**2 + (m.x54 - m.x82)**2 + (m.x104 - m.x132)**2) + 1/
                       sqrt((m.x4 - m.x33)**2 + (m.x54 - m.x83)**2 + (m.x104 - m.x133)**2) + 1/sqrt((m.x4 - m.x34)**2 + 
                       (m.x54 - m.x84)**2 + (m.x104 - m.x134)**2) + 1/sqrt((m.x4 - m.x35)**2 + (m.x54 - m.x85)**2 + (
                       m.x104 - m.x135)**2) + 1/sqrt((m.x4 - m.x36)**2 + (m.x54 - m.x86)**2 + (m.x104 - m.x136)**2) + 1/
                       sqrt((m.x4 - m.x37)**2 + (m.x54 - m.x87)**2 + (m.x104 - m.x137)**2) + 1/sqrt((m.x4 - m.x38)**2 + 
                       (m.x54 - m.x88)**2 + (m.x104 - m.x138)**2) + 1/sqrt((m.x4 - m.x39)**2 + (m.x54 - m.x89)**2 + (
                       m.x104 - m.x139)**2) + 1/sqrt((m.x4 - m.x40)**2 + (m.x54 - m.x90)**2 + (m.x104 - m.x140)**2) + 1/
                       sqrt((m.x4 - m.x41)**2 + (m.x54 - m.x91)**2 + (m.x104 - m.x141)**2) + 1/sqrt((m.x4 - m.x42)**2 + 
                       (m.x54 - m.x92)**2 + (m.x104 - m.x142)**2) + 1/sqrt((m.x4 - m.x43)**2 + (m.x54 - m.x93)**2 + (
                       m.x104 - m.x143)**2) + 1/sqrt((m.x4 - m.x44)**2 + (m.x54 - m.x94)**2 + (m.x104 - m.x144)**2) + 1/
                       sqrt((m.x4 - m.x45)**2 + (m.x54 - m.x95)**2 + (m.x104 - m.x145)**2) + 1/sqrt((m.x4 - m.x46)**2 + 
                       (m.x54 - m.x96)**2 + (m.x104 - m.x146)**2) + 1/sqrt((m.x4 - m.x47)**2 + (m.x54 - m.x97)**2 + (
                       m.x104 - m.x147)**2) + 1/sqrt((m.x4 - m.x48)**2 + (m.x54 - m.x98)**2 + (m.x104 - m.x148)**2) + 1/
                       sqrt((m.x4 - m.x49)**2 + (m.x54 - m.x99)**2 + (m.x104 - m.x149)**2) + 1/sqrt((m.x4 - m.x50)**2 + 
                       (m.x54 - m.x100)**2 + (m.x104 - m.x150)**2) + 1/sqrt((m.x5 - m.x6)**2 + (m.x55 - m.x56)**2 + (
                       m.x105 - m.x106)**2) + 1/sqrt((m.x5 - m.x7)**2 + (m.x55 - m.x57)**2 + (m.x105 - m.x107)**2) + 1/
                       sqrt((m.x5 - m.x8)**2 + (m.x55 - m.x58)**2 + (m.x105 - m.x108)**2) + 1/sqrt((m.x5 - m.x9)**2 + (
                       m.x55 - m.x59)**2 + (m.x105 - m.x109)**2) + 1/sqrt((m.x5 - m.x10)**2 + (m.x55 - m.x60)**2 + (
                       m.x105 - m.x110)**2) + 1/sqrt((m.x5 - m.x11)**2 + (m.x55 - m.x61)**2 + (m.x105 - m.x111)**2) + 1/
                       sqrt((m.x5 - m.x12)**2 + (m.x55 - m.x62)**2 + (m.x105 - m.x112)**2) + 1/sqrt((m.x5 - m.x13)**2 + 
                       (m.x55 - m.x63)**2 + (m.x105 - m.x113)**2) + 1/sqrt((m.x5 - m.x14)**2 + (m.x55 - m.x64)**2 + (
                       m.x105 - m.x114)**2) + 1/sqrt((m.x5 - m.x15)**2 + (m.x55 - m.x65)**2 + (m.x105 - m.x115)**2) + 1/
                       sqrt((m.x5 - m.x16)**2 + (m.x55 - m.x66)**2 + (m.x105 - m.x116)**2) + 1/sqrt((m.x5 - m.x17)**2 + 
                       (m.x55 - m.x67)**2 + (m.x105 - m.x117)**2) + 1/sqrt((m.x5 - m.x18)**2 + (m.x55 - m.x68)**2 + (
                       m.x105 - m.x118)**2) + 1/sqrt((m.x5 - m.x19)**2 + (m.x55 - m.x69)**2 + (m.x105 - m.x119)**2) + 1/
                       sqrt((m.x5 - m.x20)**2 + (m.x55 - m.x70)**2 + (m.x105 - m.x120)**2) + 1/sqrt((m.x5 - m.x21)**2 + 
                       (m.x55 - m.x71)**2 + (m.x105 - m.x121)**2) + 1/sqrt((m.x5 - m.x22)**2 + (m.x55 - m.x72)**2 + (
                       m.x105 - m.x122)**2) + 1/sqrt((m.x5 - m.x23)**2 + (m.x55 - m.x73)**2 + (m.x105 - m.x123)**2) + 1/
                       sqrt((m.x5 - m.x24)**2 + (m.x55 - m.x74)**2 + (m.x105 - m.x124)**2) + 1/sqrt((m.x5 - m.x25)**2 + 
                       (m.x55 - m.x75)**2 + (m.x105 - m.x125)**2) + 1/sqrt((m.x5 - m.x26)**2 + (m.x55 - m.x76)**2 + (
                       m.x105 - m.x126)**2) + 1/sqrt((m.x5 - m.x27)**2 + (m.x55 - m.x77)**2 + (m.x105 - m.x127)**2) + 1/
                       sqrt((m.x5 - m.x28)**2 + (m.x55 - m.x78)**2 + (m.x105 - m.x128)**2) + 1/sqrt((m.x5 - m.x29)**2 + 
                       (m.x55 - m.x79)**2 + (m.x105 - m.x129)**2) + 1/sqrt((m.x5 - m.x30)**2 + (m.x55 - m.x80)**2 + (
                       m.x105 - m.x130)**2) + 1/sqrt((m.x5 - m.x31)**2 + (m.x55 - m.x81)**2 + (m.x105 - m.x131)**2) + 1/
                       sqrt((m.x5 - m.x32)**2 + (m.x55 - m.x82)**2 + (m.x105 - m.x132)**2) + 1/sqrt((m.x5 - m.x33)**2 + 
                       (m.x55 - m.x83)**2 + (m.x105 - m.x133)**2) + 1/sqrt((m.x5 - m.x34)**2 + (m.x55 - m.x84)**2 + (
                       m.x105 - m.x134)**2) + 1/sqrt((m.x5 - m.x35)**2 + (m.x55 - m.x85)**2 + (m.x105 - m.x135)**2) + 1/
                       sqrt((m.x5 - m.x36)**2 + (m.x55 - m.x86)**2 + (m.x105 - m.x136)**2) + 1/sqrt((m.x5 - m.x37)**2 + 
                       (m.x55 - m.x87)**2 + (m.x105 - m.x137)**2) + 1/sqrt((m.x5 - m.x38)**2 + (m.x55 - m.x88)**2 + (
                       m.x105 - m.x138)**2) + 1/sqrt((m.x5 - m.x39)**2 + (m.x55 - m.x89)**2 + (m.x105 - m.x139)**2) + 1/
                       sqrt((m.x5 - m.x40)**2 + (m.x55 - m.x90)**2 + (m.x105 - m.x140)**2) + 1/sqrt((m.x5 - m.x41)**2 + 
                       (m.x55 - m.x91)**2 + (m.x105 - m.x141)**2) + 1/sqrt((m.x5 - m.x42)**2 + (m.x55 - m.x92)**2 + (
                       m.x105 - m.x142)**2) + 1/sqrt((m.x5 - m.x43)**2 + (m.x55 - m.x93)**2 + (m.x105 - m.x143)**2) + 1/
                       sqrt((m.x5 - m.x44)**2 + (m.x55 - m.x94)**2 + (m.x105 - m.x144)**2) + 1/sqrt((m.x5 - m.x45)**2 + 
                       (m.x55 - m.x95)**2 + (m.x105 - m.x145)**2) + 1/sqrt((m.x5 - m.x46)**2 + (m.x55 - m.x96)**2 + (
                       m.x105 - m.x146)**2) + 1/sqrt((m.x5 - m.x47)**2 + (m.x55 - m.x97)**2 + (m.x105 - m.x147)**2) + 1/
                       sqrt((m.x5 - m.x48)**2 + (m.x55 - m.x98)**2 + (m.x105 - m.x148)**2) + 1/sqrt((m.x5 - m.x49)**2 + 
                       (m.x55 - m.x99)**2 + (m.x105 - m.x149)**2) + 1/sqrt((m.x5 - m.x50)**2 + (m.x55 - m.x100)**2 + (
                       m.x105 - m.x150)**2) + 1/sqrt((m.x6 - m.x7)**2 + (m.x56 - m.x57)**2 + (m.x106 - m.x107)**2) + 1/
                       sqrt((m.x6 - m.x8)**2 + (m.x56 - m.x58)**2 + (m.x106 - m.x108)**2) + 1/sqrt((m.x6 - m.x9)**2 + (
                       m.x56 - m.x59)**2 + (m.x106 - m.x109)**2) + 1/sqrt((m.x6 - m.x10)**2 + (m.x56 - m.x60)**2 + (
                       m.x106 - m.x110)**2) + 1/sqrt((m.x6 - m.x11)**2 + (m.x56 - m.x61)**2 + (m.x106 - m.x111)**2) + 1/
                       sqrt((m.x6 - m.x12)**2 + (m.x56 - m.x62)**2 + (m.x106 - m.x112)**2) + 1/sqrt((m.x6 - m.x13)**2 + 
                       (m.x56 - m.x63)**2 + (m.x106 - m.x113)**2) + 1/sqrt((m.x6 - m.x14)**2 + (m.x56 - m.x64)**2 + (
                       m.x106 - m.x114)**2) + 1/sqrt((m.x6 - m.x15)**2 + (m.x56 - m.x65)**2 + (m.x106 - m.x115)**2) + 1/
                       sqrt((m.x6 - m.x16)**2 + (m.x56 - m.x66)**2 + (m.x106 - m.x116)**2) + 1/sqrt((m.x6 - m.x17)**2 + 
                       (m.x56 - m.x67)**2 + (m.x106 - m.x117)**2) + 1/sqrt((m.x6 - m.x18)**2 + (m.x56 - m.x68)**2 + (
                       m.x106 - m.x118)**2) + 1/sqrt((m.x6 - m.x19)**2 + (m.x56 - m.x69)**2 + (m.x106 - m.x119)**2) + 1/
                       sqrt((m.x6 - m.x20)**2 + (m.x56 - m.x70)**2 + (m.x106 - m.x120)**2) + 1/sqrt((m.x6 - m.x21)**2 + 
                       (m.x56 - m.x71)**2 + (m.x106 - m.x121)**2) + 1/sqrt((m.x6 - m.x22)**2 + (m.x56 - m.x72)**2 + (
                       m.x106 - m.x122)**2) + 1/sqrt((m.x6 - m.x23)**2 + (m.x56 - m.x73)**2 + (m.x106 - m.x123)**2) + 1/
                       sqrt((m.x6 - m.x24)**2 + (m.x56 - m.x74)**2 + (m.x106 - m.x124)**2) + 1/sqrt((m.x6 - m.x25)**2 + 
                       (m.x56 - m.x75)**2 + (m.x106 - m.x125)**2) + 1/sqrt((m.x6 - m.x26)**2 + (m.x56 - m.x76)**2 + (
                       m.x106 - m.x126)**2) + 1/sqrt((m.x6 - m.x27)**2 + (m.x56 - m.x77)**2 + (m.x106 - m.x127)**2) + 1/
                       sqrt((m.x6 - m.x28)**2 + (m.x56 - m.x78)**2 + (m.x106 - m.x128)**2) + 1/sqrt((m.x6 - m.x29)**2 + 
                       (m.x56 - m.x79)**2 + (m.x106 - m.x129)**2) + 1/sqrt((m.x6 - m.x30)**2 + (m.x56 - m.x80)**2 + (
                       m.x106 - m.x130)**2) + 1/sqrt((m.x6 - m.x31)**2 + (m.x56 - m.x81)**2 + (m.x106 - m.x131)**2) + 1/
                       sqrt((m.x6 - m.x32)**2 + (m.x56 - m.x82)**2 + (m.x106 - m.x132)**2) + 1/sqrt((m.x6 - m.x33)**2 + 
                       (m.x56 - m.x83)**2 + (m.x106 - m.x133)**2) + 1/sqrt((m.x6 - m.x34)**2 + (m.x56 - m.x84)**2 + (
                       m.x106 - m.x134)**2) + 1/sqrt((m.x6 - m.x35)**2 + (m.x56 - m.x85)**2 + (m.x106 - m.x135)**2) + 1/
                       sqrt((m.x6 - m.x36)**2 + (m.x56 - m.x86)**2 + (m.x106 - m.x136)**2) + 1/sqrt((m.x6 - m.x37)**2 + 
                       (m.x56 - m.x87)**2 + (m.x106 - m.x137)**2) + 1/sqrt((m.x6 - m.x38)**2 + (m.x56 - m.x88)**2 + (
                       m.x106 - m.x138)**2) + 1/sqrt((m.x6 - m.x39)**2 + (m.x56 - m.x89)**2 + (m.x106 - m.x139)**2) + 1/
                       sqrt((m.x6 - m.x40)**2 + (m.x56 - m.x90)**2 + (m.x106 - m.x140)**2) + 1/sqrt((m.x6 - m.x41)**2 + 
                       (m.x56 - m.x91)**2 + (m.x106 - m.x141)**2) + 1/sqrt((m.x6 - m.x42)**2 + (m.x56 - m.x92)**2 + (
                       m.x106 - m.x142)**2) + 1/sqrt((m.x6 - m.x43)**2 + (m.x56 - m.x93)**2 + (m.x106 - m.x143)**2) + 1/
                       sqrt((m.x6 - m.x44)**2 + (m.x56 - m.x94)**2 + (m.x106 - m.x144)**2) + 1/sqrt((m.x6 - m.x45)**2 + 
                       (m.x56 - m.x95)**2 + (m.x106 - m.x145)**2) + 1/sqrt((m.x6 - m.x46)**2 + (m.x56 - m.x96)**2 + (
                       m.x106 - m.x146)**2) + 1/sqrt((m.x6 - m.x47)**2 + (m.x56 - m.x97)**2 + (m.x106 - m.x147)**2) + 1/
                       sqrt((m.x6 - m.x48)**2 + (m.x56 - m.x98)**2 + (m.x106 - m.x148)**2) + 1/sqrt((m.x6 - m.x49)**2 + 
                       (m.x56 - m.x99)**2 + (m.x106 - m.x149)**2) + 1/sqrt((m.x6 - m.x50)**2 + (m.x56 - m.x100)**2 + (
                       m.x106 - m.x150)**2) + 1/sqrt((m.x7 - m.x8)**2 + (m.x57 - m.x58)**2 + (m.x107 - m.x108)**2) + 1/
                       sqrt((m.x7 - m.x9)**2 + (m.x57 - m.x59)**2 + (m.x107 - m.x109)**2) + 1/sqrt((m.x7 - m.x10)**2 + (
                       m.x57 - m.x60)**2 + (m.x107 - m.x110)**2) + 1/sqrt((m.x7 - m.x11)**2 + (m.x57 - m.x61)**2 + (
                       m.x107 - m.x111)**2) + 1/sqrt((m.x7 - m.x12)**2 + (m.x57 - m.x62)**2 + (m.x107 - m.x112)**2) + 1/
                       sqrt((m.x7 - m.x13)**2 + (m.x57 - m.x63)**2 + (m.x107 - m.x113)**2) + 1/sqrt((m.x7 - m.x14)**2 + 
                       (m.x57 - m.x64)**2 + (m.x107 - m.x114)**2) + 1/sqrt((m.x7 - m.x15)**2 + (m.x57 - m.x65)**2 + (
                       m.x107 - m.x115)**2) + 1/sqrt((m.x7 - m.x16)**2 + (m.x57 - m.x66)**2 + (m.x107 - m.x116)**2) + 1/
                       sqrt((m.x7 - m.x17)**2 + (m.x57 - m.x67)**2 + (m.x107 - m.x117)**2) + 1/sqrt((m.x7 - m.x18)**2 + 
                       (m.x57 - m.x68)**2 + (m.x107 - m.x118)**2) + 1/sqrt((m.x7 - m.x19)**2 + (m.x57 - m.x69)**2 + (
                       m.x107 - m.x119)**2) + 1/sqrt((m.x7 - m.x20)**2 + (m.x57 - m.x70)**2 + (m.x107 - m.x120)**2) + 1/
                       sqrt((m.x7 - m.x21)**2 + (m.x57 - m.x71)**2 + (m.x107 - m.x121)**2) + 1/sqrt((m.x7 - m.x22)**2 + 
                       (m.x57 - m.x72)**2 + (m.x107 - m.x122)**2) + 1/sqrt((m.x7 - m.x23)**2 + (m.x57 - m.x73)**2 + (
                       m.x107 - m.x123)**2) + 1/sqrt((m.x7 - m.x24)**2 + (m.x57 - m.x74)**2 + (m.x107 - m.x124)**2) + 1/
                       sqrt((m.x7 - m.x25)**2 + (m.x57 - m.x75)**2 + (m.x107 - m.x125)**2) + 1/sqrt((m.x7 - m.x26)**2 + 
                       (m.x57 - m.x76)**2 + (m.x107 - m.x126)**2) + 1/sqrt((m.x7 - m.x27)**2 + (m.x57 - m.x77)**2 + (
                       m.x107 - m.x127)**2) + 1/sqrt((m.x7 - m.x28)**2 + (m.x57 - m.x78)**2 + (m.x107 - m.x128)**2) + 1/
                       sqrt((m.x7 - m.x29)**2 + (m.x57 - m.x79)**2 + (m.x107 - m.x129)**2) + 1/sqrt((m.x7 - m.x30)**2 + 
                       (m.x57 - m.x80)**2 + (m.x107 - m.x130)**2) + 1/sqrt((m.x7 - m.x31)**2 + (m.x57 - m.x81)**2 + (
                       m.x107 - m.x131)**2) + 1/sqrt((m.x7 - m.x32)**2 + (m.x57 - m.x82)**2 + (m.x107 - m.x132)**2) + 1/
                       sqrt((m.x7 - m.x33)**2 + (m.x57 - m.x83)**2 + (m.x107 - m.x133)**2) + 1/sqrt((m.x7 - m.x34)**2 + 
                       (m.x57 - m.x84)**2 + (m.x107 - m.x134)**2) + 1/sqrt((m.x7 - m.x35)**2 + (m.x57 - m.x85)**2 + (
                       m.x107 - m.x135)**2) + 1/sqrt((m.x7 - m.x36)**2 + (m.x57 - m.x86)**2 + (m.x107 - m.x136)**2) + 1/
                       sqrt((m.x7 - m.x37)**2 + (m.x57 - m.x87)**2 + (m.x107 - m.x137)**2) + 1/sqrt((m.x7 - m.x38)**2 + 
                       (m.x57 - m.x88)**2 + (m.x107 - m.x138)**2) + 1/sqrt((m.x7 - m.x39)**2 + (m.x57 - m.x89)**2 + (
                       m.x107 - m.x139)**2) + 1/sqrt((m.x7 - m.x40)**2 + (m.x57 - m.x90)**2 + (m.x107 - m.x140)**2) + 1/
                       sqrt((m.x7 - m.x41)**2 + (m.x57 - m.x91)**2 + (m.x107 - m.x141)**2) + 1/sqrt((m.x7 - m.x42)**2 + 
                       (m.x57 - m.x92)**2 + (m.x107 - m.x142)**2) + 1/sqrt((m.x7 - m.x43)**2 + (m.x57 - m.x93)**2 + (
                       m.x107 - m.x143)**2) + 1/sqrt((m.x7 - m.x44)**2 + (m.x57 - m.x94)**2 + (m.x107 - m.x144)**2) + 1/
                       sqrt((m.x7 - m.x45)**2 + (m.x57 - m.x95)**2 + (m.x107 - m.x145)**2) + 1/sqrt((m.x7 - m.x46)**2 + 
                       (m.x57 - m.x96)**2 + (m.x107 - m.x146)**2) + 1/sqrt((m.x7 - m.x47)**2 + (m.x57 - m.x97)**2 + (
                       m.x107 - m.x147)**2) + 1/sqrt((m.x7 - m.x48)**2 + (m.x57 - m.x98)**2 + (m.x107 - m.x148)**2) + 1/
                       sqrt((m.x7 - m.x49)**2 + (m.x57 - m.x99)**2 + (m.x107 - m.x149)**2) + 1/sqrt((m.x7 - m.x50)**2 + 
                       (m.x57 - m.x100)**2 + (m.x107 - m.x150)**2) + 1/sqrt((m.x8 - m.x9)**2 + (m.x58 - m.x59)**2 + (
                       m.x108 - m.x109)**2) + 1/sqrt((m.x8 - m.x10)**2 + (m.x58 - m.x60)**2 + (m.x108 - m.x110)**2) + 1/
                       sqrt((m.x8 - m.x11)**2 + (m.x58 - m.x61)**2 + (m.x108 - m.x111)**2) + 1/sqrt((m.x8 - m.x12)**2 + 
                       (m.x58 - m.x62)**2 + (m.x108 - m.x112)**2) + 1/sqrt((m.x8 - m.x13)**2 + (m.x58 - m.x63)**2 + (
                       m.x108 - m.x113)**2) + 1/sqrt((m.x8 - m.x14)**2 + (m.x58 - m.x64)**2 + (m.x108 - m.x114)**2) + 1/
                       sqrt((m.x8 - m.x15)**2 + (m.x58 - m.x65)**2 + (m.x108 - m.x115)**2) + 1/sqrt((m.x8 - m.x16)**2 + 
                       (m.x58 - m.x66)**2 + (m.x108 - m.x116)**2) + 1/sqrt((m.x8 - m.x17)**2 + (m.x58 - m.x67)**2 + (
                       m.x108 - m.x117)**2) + 1/sqrt((m.x8 - m.x18)**2 + (m.x58 - m.x68)**2 + (m.x108 - m.x118)**2) + 1/
                       sqrt((m.x8 - m.x19)**2 + (m.x58 - m.x69)**2 + (m.x108 - m.x119)**2) + 1/sqrt((m.x8 - m.x20)**2 + 
                       (m.x58 - m.x70)**2 + (m.x108 - m.x120)**2) + 1/sqrt((m.x8 - m.x21)**2 + (m.x58 - m.x71)**2 + (
                       m.x108 - m.x121)**2) + 1/sqrt((m.x8 - m.x22)**2 + (m.x58 - m.x72)**2 + (m.x108 - m.x122)**2) + 1/
                       sqrt((m.x8 - m.x23)**2 + (m.x58 - m.x73)**2 + (m.x108 - m.x123)**2) + 1/sqrt((m.x8 - m.x24)**2 + 
                       (m.x58 - m.x74)**2 + (m.x108 - m.x124)**2) + 1/sqrt((m.x8 - m.x25)**2 + (m.x58 - m.x75)**2 + (
                       m.x108 - m.x125)**2) + 1/sqrt((m.x8 - m.x26)**2 + (m.x58 - m.x76)**2 + (m.x108 - m.x126)**2) + 1/
                       sqrt((m.x8 - m.x27)**2 + (m.x58 - m.x77)**2 + (m.x108 - m.x127)**2) + 1/sqrt((m.x8 - m.x28)**2 + 
                       (m.x58 - m.x78)**2 + (m.x108 - m.x128)**2) + 1/sqrt((m.x8 - m.x29)**2 + (m.x58 - m.x79)**2 + (
                       m.x108 - m.x129)**2) + 1/sqrt((m.x8 - m.x30)**2 + (m.x58 - m.x80)**2 + (m.x108 - m.x130)**2) + 1/
                       sqrt((m.x8 - m.x31)**2 + (m.x58 - m.x81)**2 + (m.x108 - m.x131)**2) + 1/sqrt((m.x8 - m.x32)**2 + 
                       (m.x58 - m.x82)**2 + (m.x108 - m.x132)**2) + 1/sqrt((m.x8 - m.x33)**2 + (m.x58 - m.x83)**2 + (
                       m.x108 - m.x133)**2) + 1/sqrt((m.x8 - m.x34)**2 + (m.x58 - m.x84)**2 + (m.x108 - m.x134)**2) + 1/
                       sqrt((m.x8 - m.x35)**2 + (m.x58 - m.x85)**2 + (m.x108 - m.x135)**2) + 1/sqrt((m.x8 - m.x36)**2 + 
                       (m.x58 - m.x86)**2 + (m.x108 - m.x136)**2) + 1/sqrt((m.x8 - m.x37)**2 + (m.x58 - m.x87)**2 + (
                       m.x108 - m.x137)**2) + 1/sqrt((m.x8 - m.x38)**2 + (m.x58 - m.x88)**2 + (m.x108 - m.x138)**2) + 1/
                       sqrt((m.x8 - m.x39)**2 + (m.x58 - m.x89)**2 + (m.x108 - m.x139)**2) + 1/sqrt((m.x8 - m.x40)**2 + 
                       (m.x58 - m.x90)**2 + (m.x108 - m.x140)**2) + 1/sqrt((m.x8 - m.x41)**2 + (m.x58 - m.x91)**2 + (
                       m.x108 - m.x141)**2) + 1/sqrt((m.x8 - m.x42)**2 + (m.x58 - m.x92)**2 + (m.x108 - m.x142)**2) + 1/
                       sqrt((m.x8 - m.x43)**2 + (m.x58 - m.x93)**2 + (m.x108 - m.x143)**2) + 1/sqrt((m.x8 - m.x44)**2 + 
                       (m.x58 - m.x94)**2 + (m.x108 - m.x144)**2) + 1/sqrt((m.x8 - m.x45)**2 + (m.x58 - m.x95)**2 + (
                       m.x108 - m.x145)**2) + 1/sqrt((m.x8 - m.x46)**2 + (m.x58 - m.x96)**2 + (m.x108 - m.x146)**2) + 1/
                       sqrt((m.x8 - m.x47)**2 + (m.x58 - m.x97)**2 + (m.x108 - m.x147)**2) + 1/sqrt((m.x8 - m.x48)**2 + 
                       (m.x58 - m.x98)**2 + (m.x108 - m.x148)**2) + 1/sqrt((m.x8 - m.x49)**2 + (m.x58 - m.x99)**2 + (
                       m.x108 - m.x149)**2) + 1/sqrt((m.x8 - m.x50)**2 + (m.x58 - m.x100)**2 + (m.x108 - m.x150)**2) + 1
                       /sqrt((m.x9 - m.x10)**2 + (m.x59 - m.x60)**2 + (m.x109 - m.x110)**2) + 1/sqrt((m.x9 - m.x11)**2
                        + (m.x59 - m.x61)**2 + (m.x109 - m.x111)**2) + 1/sqrt((m.x9 - m.x12)**2 + (m.x59 - m.x62)**2 + (
                       m.x109 - m.x112)**2) + 1/sqrt((m.x9 - m.x13)**2 + (m.x59 - m.x63)**2 + (m.x109 - m.x113)**2) + 1/
                       sqrt((m.x9 - m.x14)**2 + (m.x59 - m.x64)**2 + (m.x109 - m.x114)**2) + 1/sqrt((m.x9 - m.x15)**2 + 
                       (m.x59 - m.x65)**2 + (m.x109 - m.x115)**2) + 1/sqrt((m.x9 - m.x16)**2 + (m.x59 - m.x66)**2 + (
                       m.x109 - m.x116)**2) + 1/sqrt((m.x9 - m.x17)**2 + (m.x59 - m.x67)**2 + (m.x109 - m.x117)**2) + 1/
                       sqrt((m.x9 - m.x18)**2 + (m.x59 - m.x68)**2 + (m.x109 - m.x118)**2) + 1/sqrt((m.x9 - m.x19)**2 + 
                       (m.x59 - m.x69)**2 + (m.x109 - m.x119)**2) + 1/sqrt((m.x9 - m.x20)**2 + (m.x59 - m.x70)**2 + (
                       m.x109 - m.x120)**2) + 1/sqrt((m.x9 - m.x21)**2 + (m.x59 - m.x71)**2 + (m.x109 - m.x121)**2) + 1/
                       sqrt((m.x9 - m.x22)**2 + (m.x59 - m.x72)**2 + (m.x109 - m.x122)**2) + 1/sqrt((m.x9 - m.x23)**2 + 
                       (m.x59 - m.x73)**2 + (m.x109 - m.x123)**2) + 1/sqrt((m.x9 - m.x24)**2 + (m.x59 - m.x74)**2 + (
                       m.x109 - m.x124)**2) + 1/sqrt((m.x9 - m.x25)**2 + (m.x59 - m.x75)**2 + (m.x109 - m.x125)**2) + 1/
                       sqrt((m.x9 - m.x26)**2 + (m.x59 - m.x76)**2 + (m.x109 - m.x126)**2) + 1/sqrt((m.x9 - m.x27)**2 + 
                       (m.x59 - m.x77)**2 + (m.x109 - m.x127)**2) + 1/sqrt((m.x9 - m.x28)**2 + (m.x59 - m.x78)**2 + (
                       m.x109 - m.x128)**2) + 1/sqrt((m.x9 - m.x29)**2 + (m.x59 - m.x79)**2 + (m.x109 - m.x129)**2) + 1/
                       sqrt((m.x9 - m.x30)**2 + (m.x59 - m.x80)**2 + (m.x109 - m.x130)**2) + 1/sqrt((m.x9 - m.x31)**2 + 
                       (m.x59 - m.x81)**2 + (m.x109 - m.x131)**2) + 1/sqrt((m.x9 - m.x32)**2 + (m.x59 - m.x82)**2 + (
                       m.x109 - m.x132)**2) + 1/sqrt((m.x9 - m.x33)**2 + (m.x59 - m.x83)**2 + (m.x109 - m.x133)**2) + 1/
                       sqrt((m.x9 - m.x34)**2 + (m.x59 - m.x84)**2 + (m.x109 - m.x134)**2) + 1/sqrt((m.x9 - m.x35)**2 + 
                       (m.x59 - m.x85)**2 + (m.x109 - m.x135)**2) + 1/sqrt((m.x9 - m.x36)**2 + (m.x59 - m.x86)**2 + (
                       m.x109 - m.x136)**2) + 1/sqrt((m.x9 - m.x37)**2 + (m.x59 - m.x87)**2 + (m.x109 - m.x137)**2) + 1/
                       sqrt((m.x9 - m.x38)**2 + (m.x59 - m.x88)**2 + (m.x109 - m.x138)**2) + 1/sqrt((m.x9 - m.x39)**2 + 
                       (m.x59 - m.x89)**2 + (m.x109 - m.x139)**2) + 1/sqrt((m.x9 - m.x40)**2 + (m.x59 - m.x90)**2 + (
                       m.x109 - m.x140)**2) + 1/sqrt((m.x9 - m.x41)**2 + (m.x59 - m.x91)**2 + (m.x109 - m.x141)**2) + 1/
                       sqrt((m.x9 - m.x42)**2 + (m.x59 - m.x92)**2 + (m.x109 - m.x142)**2) + 1/sqrt((m.x9 - m.x43)**2 + 
                       (m.x59 - m.x93)**2 + (m.x109 - m.x143)**2) + 1/sqrt((m.x9 - m.x44)**2 + (m.x59 - m.x94)**2 + (
                       m.x109 - m.x144)**2) + 1/sqrt((m.x9 - m.x45)**2 + (m.x59 - m.x95)**2 + (m.x109 - m.x145)**2) + 1/
                       sqrt((m.x9 - m.x46)**2 + (m.x59 - m.x96)**2 + (m.x109 - m.x146)**2) + 1/sqrt((m.x9 - m.x47)**2 + 
                       (m.x59 - m.x97)**2 + (m.x109 - m.x147)**2) + 1/sqrt((m.x9 - m.x48)**2 + (m.x59 - m.x98)**2 + (
                       m.x109 - m.x148)**2) + 1/sqrt((m.x9 - m.x49)**2 + (m.x59 - m.x99)**2 + (m.x109 - m.x149)**2) + 1/
                       sqrt((m.x9 - m.x50)**2 + (m.x59 - m.x100)**2 + (m.x109 - m.x150)**2) + 1/sqrt((m.x10 - m.x11)**2
                        + (m.x60 - m.x61)**2 + (m.x110 - m.x111)**2) + 1/sqrt((m.x10 - m.x12)**2 + (m.x60 - m.x62)**2 + 
                       (m.x110 - m.x112)**2) + 1/sqrt((m.x10 - m.x13)**2 + (m.x60 - m.x63)**2 + (m.x110 - m.x113)**2) + 
                       1/sqrt((m.x10 - m.x14)**2 + (m.x60 - m.x64)**2 + (m.x110 - m.x114)**2) + 1/sqrt((m.x10 - m.x15)**
                       2 + (m.x60 - m.x65)**2 + (m.x110 - m.x115)**2) + 1/sqrt((m.x10 - m.x16)**2 + (m.x60 - m.x66)**2
                        + (m.x110 - m.x116)**2) + 1/sqrt((m.x10 - m.x17)**2 + (m.x60 - m.x67)**2 + (m.x110 - m.x117)**2)
                        + 1/sqrt((m.x10 - m.x18)**2 + (m.x60 - m.x68)**2 + (m.x110 - m.x118)**2) + 1/sqrt((m.x10 - m.x19
                       )**2 + (m.x60 - m.x69)**2 + (m.x110 - m.x119)**2) + 1/sqrt((m.x10 - m.x20)**2 + (m.x60 - m.x70)**
                       2 + (m.x110 - m.x120)**2) + 1/sqrt((m.x10 - m.x21)**2 + (m.x60 - m.x71)**2 + (m.x110 - m.x121)**2
                       ) + 1/sqrt((m.x10 - m.x22)**2 + (m.x60 - m.x72)**2 + (m.x110 - m.x122)**2) + 1/sqrt((m.x10 - 
                       m.x23)**2 + (m.x60 - m.x73)**2 + (m.x110 - m.x123)**2) + 1/sqrt((m.x10 - m.x24)**2 + (m.x60 - 
                       m.x74)**2 + (m.x110 - m.x124)**2) + 1/sqrt((m.x10 - m.x25)**2 + (m.x60 - m.x75)**2 + (m.x110 - 
                       m.x125)**2) + 1/sqrt((m.x10 - m.x26)**2 + (m.x60 - m.x76)**2 + (m.x110 - m.x126)**2) + 1/sqrt((
                       m.x10 - m.x27)**2 + (m.x60 - m.x77)**2 + (m.x110 - m.x127)**2) + 1/sqrt((m.x10 - m.x28)**2 + (
                       m.x60 - m.x78)**2 + (m.x110 - m.x128)**2) + 1/sqrt((m.x10 - m.x29)**2 + (m.x60 - m.x79)**2 + (
                       m.x110 - m.x129)**2) + 1/sqrt((m.x10 - m.x30)**2 + (m.x60 - m.x80)**2 + (m.x110 - m.x130)**2) + 1
                       /sqrt((m.x10 - m.x31)**2 + (m.x60 - m.x81)**2 + (m.x110 - m.x131)**2) + 1/sqrt((m.x10 - m.x32)**2
                        + (m.x60 - m.x82)**2 + (m.x110 - m.x132)**2) + 1/sqrt((m.x10 - m.x33)**2 + (m.x60 - m.x83)**2 + 
                       (m.x110 - m.x133)**2) + 1/sqrt((m.x10 - m.x34)**2 + (m.x60 - m.x84)**2 + (m.x110 - m.x134)**2) + 
                       1/sqrt((m.x10 - m.x35)**2 + (m.x60 - m.x85)**2 + (m.x110 - m.x135)**2) + 1/sqrt((m.x10 - m.x36)**
                       2 + (m.x60 - m.x86)**2 + (m.x110 - m.x136)**2) + 1/sqrt((m.x10 - m.x37)**2 + (m.x60 - m.x87)**2
                        + (m.x110 - m.x137)**2) + 1/sqrt((m.x10 - m.x38)**2 + (m.x60 - m.x88)**2 + (m.x110 - m.x138)**2)
                        + 1/sqrt((m.x10 - m.x39)**2 + (m.x60 - m.x89)**2 + (m.x110 - m.x139)**2) + 1/sqrt((m.x10 - m.x40
                       )**2 + (m.x60 - m.x90)**2 + (m.x110 - m.x140)**2) + 1/sqrt((m.x10 - m.x41)**2 + (m.x60 - m.x91)**
                       2 + (m.x110 - m.x141)**2) + 1/sqrt((m.x10 - m.x42)**2 + (m.x60 - m.x92)**2 + (m.x110 - m.x142)**2
                       ) + 1/sqrt((m.x10 - m.x43)**2 + (m.x60 - m.x93)**2 + (m.x110 - m.x143)**2) + 1/sqrt((m.x10 - 
                       m.x44)**2 + (m.x60 - m.x94)**2 + (m.x110 - m.x144)**2) + 1/sqrt((m.x10 - m.x45)**2 + (m.x60 - 
                       m.x95)**2 + (m.x110 - m.x145)**2) + 1/sqrt((m.x10 - m.x46)**2 + (m.x60 - m.x96)**2 + (m.x110 - 
                       m.x146)**2) + 1/sqrt((m.x10 - m.x47)**2 + (m.x60 - m.x97)**2 + (m.x110 - m.x147)**2) + 1/sqrt((
                       m.x10 - m.x48)**2 + (m.x60 - m.x98)**2 + (m.x110 - m.x148)**2) + 1/sqrt((m.x10 - m.x49)**2 + (
                       m.x60 - m.x99)**2 + (m.x110 - m.x149)**2) + 1/sqrt((m.x10 - m.x50)**2 + (m.x60 - m.x100)**2 + (
                       m.x110 - m.x150)**2) + 1/sqrt((m.x11 - m.x12)**2 + (m.x61 - m.x62)**2 + (m.x111 - m.x112)**2) + 1
                       /sqrt((m.x11 - m.x13)**2 + (m.x61 - m.x63)**2 + (m.x111 - m.x113)**2) + 1/sqrt((m.x11 - m.x14)**2
                        + (m.x61 - m.x64)**2 + (m.x111 - m.x114)**2) + 1/sqrt((m.x11 - m.x15)**2 + (m.x61 - m.x65)**2 + 
                       (m.x111 - m.x115)**2) + 1/sqrt((m.x11 - m.x16)**2 + (m.x61 - m.x66)**2 + (m.x111 - m.x116)**2) + 
                       1/sqrt((m.x11 - m.x17)**2 + (m.x61 - m.x67)**2 + (m.x111 - m.x117)**2) + 1/sqrt((m.x11 - m.x18)**
                       2 + (m.x61 - m.x68)**2 + (m.x111 - m.x118)**2) + 1/sqrt((m.x11 - m.x19)**2 + (m.x61 - m.x69)**2
                        + (m.x111 - m.x119)**2) + 1/sqrt((m.x11 - m.x20)**2 + (m.x61 - m.x70)**2 + (m.x111 - m.x120)**2)
                        + 1/sqrt((m.x11 - m.x21)**2 + (m.x61 - m.x71)**2 + (m.x111 - m.x121)**2) + 1/sqrt((m.x11 - m.x22
                       )**2 + (m.x61 - m.x72)**2 + (m.x111 - m.x122)**2) + 1/sqrt((m.x11 - m.x23)**2 + (m.x61 - m.x73)**
                       2 + (m.x111 - m.x123)**2) + 1/sqrt((m.x11 - m.x24)**2 + (m.x61 - m.x74)**2 + (m.x111 - m.x124)**2
                       ) + 1/sqrt((m.x11 - m.x25)**2 + (m.x61 - m.x75)**2 + (m.x111 - m.x125)**2) + 1/sqrt((m.x11 - 
                       m.x26)**2 + (m.x61 - m.x76)**2 + (m.x111 - m.x126)**2) + 1/sqrt((m.x11 - m.x27)**2 + (m.x61 - 
                       m.x77)**2 + (m.x111 - m.x127)**2) + 1/sqrt((m.x11 - m.x28)**2 + (m.x61 - m.x78)**2 + (m.x111 - 
                       m.x128)**2) + 1/sqrt((m.x11 - m.x29)**2 + (m.x61 - m.x79)**2 + (m.x111 - m.x129)**2) + 1/sqrt((
                       m.x11 - m.x30)**2 + (m.x61 - m.x80)**2 + (m.x111 - m.x130)**2) + 1/sqrt((m.x11 - m.x31)**2 + (
                       m.x61 - m.x81)**2 + (m.x111 - m.x131)**2) + 1/sqrt((m.x11 - m.x32)**2 + (m.x61 - m.x82)**2 + (
                       m.x111 - m.x132)**2) + 1/sqrt((m.x11 - m.x33)**2 + (m.x61 - m.x83)**2 + (m.x111 - m.x133)**2) + 1
                       /sqrt((m.x11 - m.x34)**2 + (m.x61 - m.x84)**2 + (m.x111 - m.x134)**2) + 1/sqrt((m.x11 - m.x35)**2
                        + (m.x61 - m.x85)**2 + (m.x111 - m.x135)**2) + 1/sqrt((m.x11 - m.x36)**2 + (m.x61 - m.x86)**2 + 
                       (m.x111 - m.x136)**2) + 1/sqrt((m.x11 - m.x37)**2 + (m.x61 - m.x87)**2 + (m.x111 - m.x137)**2) + 
                       1/sqrt((m.x11 - m.x38)**2 + (m.x61 - m.x88)**2 + (m.x111 - m.x138)**2) + 1/sqrt((m.x11 - m.x39)**
                       2 + (m.x61 - m.x89)**2 + (m.x111 - m.x139)**2) + 1/sqrt((m.x11 - m.x40)**2 + (m.x61 - m.x90)**2
                        + (m.x111 - m.x140)**2) + 1/sqrt((m.x11 - m.x41)**2 + (m.x61 - m.x91)**2 + (m.x111 - m.x141)**2)
                        + 1/sqrt((m.x11 - m.x42)**2 + (m.x61 - m.x92)**2 + (m.x111 - m.x142)**2) + 1/sqrt((m.x11 - m.x43
                       )**2 + (m.x61 - m.x93)**2 + (m.x111 - m.x143)**2) + 1/sqrt((m.x11 - m.x44)**2 + (m.x61 - m.x94)**
                       2 + (m.x111 - m.x144)**2) + 1/sqrt((m.x11 - m.x45)**2 + (m.x61 - m.x95)**2 + (m.x111 - m.x145)**2
                       ) + 1/sqrt((m.x11 - m.x46)**2 + (m.x61 - m.x96)**2 + (m.x111 - m.x146)**2) + 1/sqrt((m.x11 - 
                       m.x47)**2 + (m.x61 - m.x97)**2 + (m.x111 - m.x147)**2) + 1/sqrt((m.x11 - m.x48)**2 + (m.x61 - 
                       m.x98)**2 + (m.x111 - m.x148)**2) + 1/sqrt((m.x11 - m.x49)**2 + (m.x61 - m.x99)**2 + (m.x111 - 
                       m.x149)**2) + 1/sqrt((m.x11 - m.x50)**2 + (m.x61 - m.x100)**2 + (m.x111 - m.x150)**2) + 1/sqrt((
                       m.x12 - m.x13)**2 + (m.x62 - m.x63)**2 + (m.x112 - m.x113)**2) + 1/sqrt((m.x12 - m.x14)**2 + (
                       m.x62 - m.x64)**2 + (m.x112 - m.x114)**2) + 1/sqrt((m.x12 - m.x15)**2 + (m.x62 - m.x65)**2 + (
                       m.x112 - m.x115)**2) + 1/sqrt((m.x12 - m.x16)**2 + (m.x62 - m.x66)**2 + (m.x112 - m.x116)**2) + 1
                       /sqrt((m.x12 - m.x17)**2 + (m.x62 - m.x67)**2 + (m.x112 - m.x117)**2) + 1/sqrt((m.x12 - m.x18)**2
                        + (m.x62 - m.x68)**2 + (m.x112 - m.x118)**2) + 1/sqrt((m.x12 - m.x19)**2 + (m.x62 - m.x69)**2 + 
                       (m.x112 - m.x119)**2) + 1/sqrt((m.x12 - m.x20)**2 + (m.x62 - m.x70)**2 + (m.x112 - m.x120)**2) + 
                       1/sqrt((m.x12 - m.x21)**2 + (m.x62 - m.x71)**2 + (m.x112 - m.x121)**2) + 1/sqrt((m.x12 - m.x22)**
                       2 + (m.x62 - m.x72)**2 + (m.x112 - m.x122)**2) + 1/sqrt((m.x12 - m.x23)**2 + (m.x62 - m.x73)**2
                        + (m.x112 - m.x123)**2) + 1/sqrt((m.x12 - m.x24)**2 + (m.x62 - m.x74)**2 + (m.x112 - m.x124)**2)
                        + 1/sqrt((m.x12 - m.x25)**2 + (m.x62 - m.x75)**2 + (m.x112 - m.x125)**2) + 1/sqrt((m.x12 - m.x26
                       )**2 + (m.x62 - m.x76)**2 + (m.x112 - m.x126)**2) + 1/sqrt((m.x12 - m.x27)**2 + (m.x62 - m.x77)**
                       2 + (m.x112 - m.x127)**2) + 1/sqrt((m.x12 - m.x28)**2 + (m.x62 - m.x78)**2 + (m.x112 - m.x128)**2
                       ) + 1/sqrt((m.x12 - m.x29)**2 + (m.x62 - m.x79)**2 + (m.x112 - m.x129)**2) + 1/sqrt((m.x12 - 
                       m.x30)**2 + (m.x62 - m.x80)**2 + (m.x112 - m.x130)**2) + 1/sqrt((m.x12 - m.x31)**2 + (m.x62 - 
                       m.x81)**2 + (m.x112 - m.x131)**2) + 1/sqrt((m.x12 - m.x32)**2 + (m.x62 - m.x82)**2 + (m.x112 - 
                       m.x132)**2) + 1/sqrt((m.x12 - m.x33)**2 + (m.x62 - m.x83)**2 + (m.x112 - m.x133)**2) + 1/sqrt((
                       m.x12 - m.x34)**2 + (m.x62 - m.x84)**2 + (m.x112 - m.x134)**2) + 1/sqrt((m.x12 - m.x35)**2 + (
                       m.x62 - m.x85)**2 + (m.x112 - m.x135)**2) + 1/sqrt((m.x12 - m.x36)**2 + (m.x62 - m.x86)**2 + (
                       m.x112 - m.x136)**2) + 1/sqrt((m.x12 - m.x37)**2 + (m.x62 - m.x87)**2 + (m.x112 - m.x137)**2) + 1
                       /sqrt((m.x12 - m.x38)**2 + (m.x62 - m.x88)**2 + (m.x112 - m.x138)**2) + 1/sqrt((m.x12 - m.x39)**2
                        + (m.x62 - m.x89)**2 + (m.x112 - m.x139)**2) + 1/sqrt((m.x12 - m.x40)**2 + (m.x62 - m.x90)**2 + 
                       (m.x112 - m.x140)**2) + 1/sqrt((m.x12 - m.x41)**2 + (m.x62 - m.x91)**2 + (m.x112 - m.x141)**2) + 
                       1/sqrt((m.x12 - m.x42)**2 + (m.x62 - m.x92)**2 + (m.x112 - m.x142)**2) + 1/sqrt((m.x12 - m.x43)**
                       2 + (m.x62 - m.x93)**2 + (m.x112 - m.x143)**2) + 1/sqrt((m.x12 - m.x44)**2 + (m.x62 - m.x94)**2
                        + (m.x112 - m.x144)**2) + 1/sqrt((m.x12 - m.x45)**2 + (m.x62 - m.x95)**2 + (m.x112 - m.x145)**2)
                        + 1/sqrt((m.x12 - m.x46)**2 + (m.x62 - m.x96)**2 + (m.x112 - m.x146)**2) + 1/sqrt((m.x12 - m.x47
                       )**2 + (m.x62 - m.x97)**2 + (m.x112 - m.x147)**2) + 1/sqrt((m.x12 - m.x48)**2 + (m.x62 - m.x98)**
                       2 + (m.x112 - m.x148)**2) + 1/sqrt((m.x12 - m.x49)**2 + (m.x62 - m.x99)**2 + (m.x112 - m.x149)**2
                       ) + 1/sqrt((m.x12 - m.x50)**2 + (m.x62 - m.x100)**2 + (m.x112 - m.x150)**2) + 1/sqrt((m.x13 - 
                       m.x14)**2 + (m.x63 - m.x64)**2 + (m.x113 - m.x114)**2) + 1/sqrt((m.x13 - m.x15)**2 + (m.x63 - 
                       m.x65)**2 + (m.x113 - m.x115)**2) + 1/sqrt((m.x13 - m.x16)**2 + (m.x63 - m.x66)**2 + (m.x113 - 
                       m.x116)**2) + 1/sqrt((m.x13 - m.x17)**2 + (m.x63 - m.x67)**2 + (m.x113 - m.x117)**2) + 1/sqrt((
                       m.x13 - m.x18)**2 + (m.x63 - m.x68)**2 + (m.x113 - m.x118)**2) + 1/sqrt((m.x13 - m.x19)**2 + (
                       m.x63 - m.x69)**2 + (m.x113 - m.x119)**2) + 1/sqrt((m.x13 - m.x20)**2 + (m.x63 - m.x70)**2 + (
                       m.x113 - m.x120)**2) + 1/sqrt((m.x13 - m.x21)**2 + (m.x63 - m.x71)**2 + (m.x113 - m.x121)**2) + 1
                       /sqrt((m.x13 - m.x22)**2 + (m.x63 - m.x72)**2 + (m.x113 - m.x122)**2) + 1/sqrt((m.x13 - m.x23)**2
                        + (m.x63 - m.x73)**2 + (m.x113 - m.x123)**2) + 1/sqrt((m.x13 - m.x24)**2 + (m.x63 - m.x74)**2 + 
                       (m.x113 - m.x124)**2) + 1/sqrt((m.x13 - m.x25)**2 + (m.x63 - m.x75)**2 + (m.x113 - m.x125)**2) + 
                       1/sqrt((m.x13 - m.x26)**2 + (m.x63 - m.x76)**2 + (m.x113 - m.x126)**2) + 1/sqrt((m.x13 - m.x27)**
                       2 + (m.x63 - m.x77)**2 + (m.x113 - m.x127)**2) + 1/sqrt((m.x13 - m.x28)**2 + (m.x63 - m.x78)**2
                        + (m.x113 - m.x128)**2) + 1/sqrt((m.x13 - m.x29)**2 + (m.x63 - m.x79)**2 + (m.x113 - m.x129)**2)
                        + 1/sqrt((m.x13 - m.x30)**2 + (m.x63 - m.x80)**2 + (m.x113 - m.x130)**2) + 1/sqrt((m.x13 - m.x31
                       )**2 + (m.x63 - m.x81)**2 + (m.x113 - m.x131)**2) + 1/sqrt((m.x13 - m.x32)**2 + (m.x63 - m.x82)**
                       2 + (m.x113 - m.x132)**2) + 1/sqrt((m.x13 - m.x33)**2 + (m.x63 - m.x83)**2 + (m.x113 - m.x133)**2
                       ) + 1/sqrt((m.x13 - m.x34)**2 + (m.x63 - m.x84)**2 + (m.x113 - m.x134)**2) + 1/sqrt((m.x13 - 
                       m.x35)**2 + (m.x63 - m.x85)**2 + (m.x113 - m.x135)**2) + 1/sqrt((m.x13 - m.x36)**2 + (m.x63 - 
                       m.x86)**2 + (m.x113 - m.x136)**2) + 1/sqrt((m.x13 - m.x37)**2 + (m.x63 - m.x87)**2 + (m.x113 - 
                       m.x137)**2) + 1/sqrt((m.x13 - m.x38)**2 + (m.x63 - m.x88)**2 + (m.x113 - m.x138)**2) + 1/sqrt((
                       m.x13 - m.x39)**2 + (m.x63 - m.x89)**2 + (m.x113 - m.x139)**2) + 1/sqrt((m.x13 - m.x40)**2 + (
                       m.x63 - m.x90)**2 + (m.x113 - m.x140)**2) + 1/sqrt((m.x13 - m.x41)**2 + (m.x63 - m.x91)**2 + (
                       m.x113 - m.x141)**2) + 1/sqrt((m.x13 - m.x42)**2 + (m.x63 - m.x92)**2 + (m.x113 - m.x142)**2) + 1
                       /sqrt((m.x13 - m.x43)**2 + (m.x63 - m.x93)**2 + (m.x113 - m.x143)**2) + 1/sqrt((m.x13 - m.x44)**2
                        + (m.x63 - m.x94)**2 + (m.x113 - m.x144)**2) + 1/sqrt((m.x13 - m.x45)**2 + (m.x63 - m.x95)**2 + 
                       (m.x113 - m.x145)**2) + 1/sqrt((m.x13 - m.x46)**2 + (m.x63 - m.x96)**2 + (m.x113 - m.x146)**2) + 
                       1/sqrt((m.x13 - m.x47)**2 + (m.x63 - m.x97)**2 + (m.x113 - m.x147)**2) + 1/sqrt((m.x13 - m.x48)**
                       2 + (m.x63 - m.x98)**2 + (m.x113 - m.x148)**2) + 1/sqrt((m.x13 - m.x49)**2 + (m.x63 - m.x99)**2
                        + (m.x113 - m.x149)**2) + 1/sqrt((m.x13 - m.x50)**2 + (m.x63 - m.x100)**2 + (m.x113 - m.x150)**2
                       ) + 1/sqrt((m.x14 - m.x15)**2 + (m.x64 - m.x65)**2 + (m.x114 - m.x115)**2) + 1/sqrt((m.x14 - 
                       m.x16)**2 + (m.x64 - m.x66)**2 + (m.x114 - m.x116)**2) + 1/sqrt((m.x14 - m.x17)**2 + (m.x64 - 
                       m.x67)**2 + (m.x114 - m.x117)**2) + 1/sqrt((m.x14 - m.x18)**2 + (m.x64 - m.x68)**2 + (m.x114 - 
                       m.x118)**2) + 1/sqrt((m.x14 - m.x19)**2 + (m.x64 - m.x69)**2 + (m.x114 - m.x119)**2) + 1/sqrt((
                       m.x14 - m.x20)**2 + (m.x64 - m.x70)**2 + (m.x114 - m.x120)**2) + 1/sqrt((m.x14 - m.x21)**2 + (
                       m.x64 - m.x71)**2 + (m.x114 - m.x121)**2) + 1/sqrt((m.x14 - m.x22)**2 + (m.x64 - m.x72)**2 + (
                       m.x114 - m.x122)**2) + 1/sqrt((m.x14 - m.x23)**2 + (m.x64 - m.x73)**2 + (m.x114 - m.x123)**2) + 1
                       /sqrt((m.x14 - m.x24)**2 + (m.x64 - m.x74)**2 + (m.x114 - m.x124)**2) + 1/sqrt((m.x14 - m.x25)**2
                        + (m.x64 - m.x75)**2 + (m.x114 - m.x125)**2) + 1/sqrt((m.x14 - m.x26)**2 + (m.x64 - m.x76)**2 + 
                       (m.x114 - m.x126)**2) + 1/sqrt((m.x14 - m.x27)**2 + (m.x64 - m.x77)**2 + (m.x114 - m.x127)**2) + 
                       1/sqrt((m.x14 - m.x28)**2 + (m.x64 - m.x78)**2 + (m.x114 - m.x128)**2) + 1/sqrt((m.x14 - m.x29)**
                       2 + (m.x64 - m.x79)**2 + (m.x114 - m.x129)**2) + 1/sqrt((m.x14 - m.x30)**2 + (m.x64 - m.x80)**2
                        + (m.x114 - m.x130)**2) + 1/sqrt((m.x14 - m.x31)**2 + (m.x64 - m.x81)**2 + (m.x114 - m.x131)**2)
                        + 1/sqrt((m.x14 - m.x32)**2 + (m.x64 - m.x82)**2 + (m.x114 - m.x132)**2) + 1/sqrt((m.x14 - m.x33
                       )**2 + (m.x64 - m.x83)**2 + (m.x114 - m.x133)**2) + 1/sqrt((m.x14 - m.x34)**2 + (m.x64 - m.x84)**
                       2 + (m.x114 - m.x134)**2) + 1/sqrt((m.x14 - m.x35)**2 + (m.x64 - m.x85)**2 + (m.x114 - m.x135)**2
                       ) + 1/sqrt((m.x14 - m.x36)**2 + (m.x64 - m.x86)**2 + (m.x114 - m.x136)**2) + 1/sqrt((m.x14 - 
                       m.x37)**2 + (m.x64 - m.x87)**2 + (m.x114 - m.x137)**2) + 1/sqrt((m.x14 - m.x38)**2 + (m.x64 - 
                       m.x88)**2 + (m.x114 - m.x138)**2) + 1/sqrt((m.x14 - m.x39)**2 + (m.x64 - m.x89)**2 + (m.x114 - 
                       m.x139)**2) + 1/sqrt((m.x14 - m.x40)**2 + (m.x64 - m.x90)**2 + (m.x114 - m.x140)**2) + 1/sqrt((
                       m.x14 - m.x41)**2 + (m.x64 - m.x91)**2 + (m.x114 - m.x141)**2) + 1/sqrt((m.x14 - m.x42)**2 + (
                       m.x64 - m.x92)**2 + (m.x114 - m.x142)**2) + 1/sqrt((m.x14 - m.x43)**2 + (m.x64 - m.x93)**2 + (
                       m.x114 - m.x143)**2) + 1/sqrt((m.x14 - m.x44)**2 + (m.x64 - m.x94)**2 + (m.x114 - m.x144)**2) + 1
                       /sqrt((m.x14 - m.x45)**2 + (m.x64 - m.x95)**2 + (m.x114 - m.x145)**2) + 1/sqrt((m.x14 - m.x46)**2
                        + (m.x64 - m.x96)**2 + (m.x114 - m.x146)**2) + 1/sqrt((m.x14 - m.x47)**2 + (m.x64 - m.x97)**2 + 
                       (m.x114 - m.x147)**2) + 1/sqrt((m.x14 - m.x48)**2 + (m.x64 - m.x98)**2 + (m.x114 - m.x148)**2) + 
                       1/sqrt((m.x14 - m.x49)**2 + (m.x64 - m.x99)**2 + (m.x114 - m.x149)**2) + 1/sqrt((m.x14 - m.x50)**
                       2 + (m.x64 - m.x100)**2 + (m.x114 - m.x150)**2) + 1/sqrt((m.x15 - m.x16)**2 + (m.x65 - m.x66)**2
                        + (m.x115 - m.x116)**2) + 1/sqrt((m.x15 - m.x17)**2 + (m.x65 - m.x67)**2 + (m.x115 - m.x117)**2)
                        + 1/sqrt((m.x15 - m.x18)**2 + (m.x65 - m.x68)**2 + (m.x115 - m.x118)**2) + 1/sqrt((m.x15 - m.x19
                       )**2 + (m.x65 - m.x69)**2 + (m.x115 - m.x119)**2) + 1/sqrt((m.x15 - m.x20)**2 + (m.x65 - m.x70)**
                       2 + (m.x115 - m.x120)**2) + 1/sqrt((m.x15 - m.x21)**2 + (m.x65 - m.x71)**2 + (m.x115 - m.x121)**2
                       ) + 1/sqrt((m.x15 - m.x22)**2 + (m.x65 - m.x72)**2 + (m.x115 - m.x122)**2) + 1/sqrt((m.x15 - 
                       m.x23)**2 + (m.x65 - m.x73)**2 + (m.x115 - m.x123)**2) + 1/sqrt((m.x15 - m.x24)**2 + (m.x65 - 
                       m.x74)**2 + (m.x115 - m.x124)**2) + 1/sqrt((m.x15 - m.x25)**2 + (m.x65 - m.x75)**2 + (m.x115 - 
                       m.x125)**2) + 1/sqrt((m.x15 - m.x26)**2 + (m.x65 - m.x76)**2 + (m.x115 - m.x126)**2) + 1/sqrt((
                       m.x15 - m.x27)**2 + (m.x65 - m.x77)**2 + (m.x115 - m.x127)**2) + 1/sqrt((m.x15 - m.x28)**2 + (
                       m.x65 - m.x78)**2 + (m.x115 - m.x128)**2) + 1/sqrt((m.x15 - m.x29)**2 + (m.x65 - m.x79)**2 + (
                       m.x115 - m.x129)**2) + 1/sqrt((m.x15 - m.x30)**2 + (m.x65 - m.x80)**2 + (m.x115 - m.x130)**2) + 1
                       /sqrt((m.x15 - m.x31)**2 + (m.x65 - m.x81)**2 + (m.x115 - m.x131)**2) + 1/sqrt((m.x15 - m.x32)**2
                        + (m.x65 - m.x82)**2 + (m.x115 - m.x132)**2) + 1/sqrt((m.x15 - m.x33)**2 + (m.x65 - m.x83)**2 + 
                       (m.x115 - m.x133)**2) + 1/sqrt((m.x15 - m.x34)**2 + (m.x65 - m.x84)**2 + (m.x115 - m.x134)**2) + 
                       1/sqrt((m.x15 - m.x35)**2 + (m.x65 - m.x85)**2 + (m.x115 - m.x135)**2) + 1/sqrt((m.x15 - m.x36)**
                       2 + (m.x65 - m.x86)**2 + (m.x115 - m.x136)**2) + 1/sqrt((m.x15 - m.x37)**2 + (m.x65 - m.x87)**2
                        + (m.x115 - m.x137)**2) + 1/sqrt((m.x15 - m.x38)**2 + (m.x65 - m.x88)**2 + (m.x115 - m.x138)**2)
                        + 1/sqrt((m.x15 - m.x39)**2 + (m.x65 - m.x89)**2 + (m.x115 - m.x139)**2) + 1/sqrt((m.x15 - m.x40
                       )**2 + (m.x65 - m.x90)**2 + (m.x115 - m.x140)**2) + 1/sqrt((m.x15 - m.x41)**2 + (m.x65 - m.x91)**
                       2 + (m.x115 - m.x141)**2) + 1/sqrt((m.x15 - m.x42)**2 + (m.x65 - m.x92)**2 + (m.x115 - m.x142)**2
                       ) + 1/sqrt((m.x15 - m.x43)**2 + (m.x65 - m.x93)**2 + (m.x115 - m.x143)**2) + 1/sqrt((m.x15 - 
                       m.x44)**2 + (m.x65 - m.x94)**2 + (m.x115 - m.x144)**2) + 1/sqrt((m.x15 - m.x45)**2 + (m.x65 - 
                       m.x95)**2 + (m.x115 - m.x145)**2) + 1/sqrt((m.x15 - m.x46)**2 + (m.x65 - m.x96)**2 + (m.x115 - 
                       m.x146)**2) + 1/sqrt((m.x15 - m.x47)**2 + (m.x65 - m.x97)**2 + (m.x115 - m.x147)**2) + 1/sqrt((
                       m.x15 - m.x48)**2 + (m.x65 - m.x98)**2 + (m.x115 - m.x148)**2) + 1/sqrt((m.x15 - m.x49)**2 + (
                       m.x65 - m.x99)**2 + (m.x115 - m.x149)**2) + 1/sqrt((m.x15 - m.x50)**2 + (m.x65 - m.x100)**2 + (
                       m.x115 - m.x150)**2) + 1/sqrt((m.x16 - m.x17)**2 + (m.x66 - m.x67)**2 + (m.x116 - m.x117)**2) + 1
                       /sqrt((m.x16 - m.x18)**2 + (m.x66 - m.x68)**2 + (m.x116 - m.x118)**2) + 1/sqrt((m.x16 - m.x19)**2
                        + (m.x66 - m.x69)**2 + (m.x116 - m.x119)**2) + 1/sqrt((m.x16 - m.x20)**2 + (m.x66 - m.x70)**2 + 
                       (m.x116 - m.x120)**2) + 1/sqrt((m.x16 - m.x21)**2 + (m.x66 - m.x71)**2 + (m.x116 - m.x121)**2) + 
                       1/sqrt((m.x16 - m.x22)**2 + (m.x66 - m.x72)**2 + (m.x116 - m.x122)**2) + 1/sqrt((m.x16 - m.x23)**
                       2 + (m.x66 - m.x73)**2 + (m.x116 - m.x123)**2) + 1/sqrt((m.x16 - m.x24)**2 + (m.x66 - m.x74)**2
                        + (m.x116 - m.x124)**2) + 1/sqrt((m.x16 - m.x25)**2 + (m.x66 - m.x75)**2 + (m.x116 - m.x125)**2)
                        + 1/sqrt((m.x16 - m.x26)**2 + (m.x66 - m.x76)**2 + (m.x116 - m.x126)**2) + 1/sqrt((m.x16 - m.x27
                       )**2 + (m.x66 - m.x77)**2 + (m.x116 - m.x127)**2) + 1/sqrt((m.x16 - m.x28)**2 + (m.x66 - m.x78)**
                       2 + (m.x116 - m.x128)**2) + 1/sqrt((m.x16 - m.x29)**2 + (m.x66 - m.x79)**2 + (m.x116 - m.x129)**2
                       ) + 1/sqrt((m.x16 - m.x30)**2 + (m.x66 - m.x80)**2 + (m.x116 - m.x130)**2) + 1/sqrt((m.x16 - 
                       m.x31)**2 + (m.x66 - m.x81)**2 + (m.x116 - m.x131)**2) + 1/sqrt((m.x16 - m.x32)**2 + (m.x66 - 
                       m.x82)**2 + (m.x116 - m.x132)**2) + 1/sqrt((m.x16 - m.x33)**2 + (m.x66 - m.x83)**2 + (m.x116 - 
                       m.x133)**2) + 1/sqrt((m.x16 - m.x34)**2 + (m.x66 - m.x84)**2 + (m.x116 - m.x134)**2) + 1/sqrt((
                       m.x16 - m.x35)**2 + (m.x66 - m.x85)**2 + (m.x116 - m.x135)**2) + 1/sqrt((m.x16 - m.x36)**2 + (
                       m.x66 - m.x86)**2 + (m.x116 - m.x136)**2) + 1/sqrt((m.x16 - m.x37)**2 + (m.x66 - m.x87)**2 + (
                       m.x116 - m.x137)**2) + 1/sqrt((m.x16 - m.x38)**2 + (m.x66 - m.x88)**2 + (m.x116 - m.x138)**2) + 1
                       /sqrt((m.x16 - m.x39)**2 + (m.x66 - m.x89)**2 + (m.x116 - m.x139)**2) + 1/sqrt((m.x16 - m.x40)**2
                        + (m.x66 - m.x90)**2 + (m.x116 - m.x140)**2) + 1/sqrt((m.x16 - m.x41)**2 + (m.x66 - m.x91)**2 + 
                       (m.x116 - m.x141)**2) + 1/sqrt((m.x16 - m.x42)**2 + (m.x66 - m.x92)**2 + (m.x116 - m.x142)**2) + 
                       1/sqrt((m.x16 - m.x43)**2 + (m.x66 - m.x93)**2 + (m.x116 - m.x143)**2) + 1/sqrt((m.x16 - m.x44)**
                       2 + (m.x66 - m.x94)**2 + (m.x116 - m.x144)**2) + 1/sqrt((m.x16 - m.x45)**2 + (m.x66 - m.x95)**2
                        + (m.x116 - m.x145)**2) + 1/sqrt((m.x16 - m.x46)**2 + (m.x66 - m.x96)**2 + (m.x116 - m.x146)**2)
                        + 1/sqrt((m.x16 - m.x47)**2 + (m.x66 - m.x97)**2 + (m.x116 - m.x147)**2) + 1/sqrt((m.x16 - m.x48
                       )**2 + (m.x66 - m.x98)**2 + (m.x116 - m.x148)**2) + 1/sqrt((m.x16 - m.x49)**2 + (m.x66 - m.x99)**
                       2 + (m.x116 - m.x149)**2) + 1/sqrt((m.x16 - m.x50)**2 + (m.x66 - m.x100)**2 + (m.x116 - m.x150)**
                       2) + 1/sqrt((m.x17 - m.x18)**2 + (m.x67 - m.x68)**2 + (m.x117 - m.x118)**2) + 1/sqrt((m.x17 - 
                       m.x19)**2 + (m.x67 - m.x69)**2 + (m.x117 - m.x119)**2) + 1/sqrt((m.x17 - m.x20)**2 + (m.x67 - 
                       m.x70)**2 + (m.x117 - m.x120)**2) + 1/sqrt((m.x17 - m.x21)**2 + (m.x67 - m.x71)**2 + (m.x117 - 
                       m.x121)**2) + 1/sqrt((m.x17 - m.x22)**2 + (m.x67 - m.x72)**2 + (m.x117 - m.x122)**2) + 1/sqrt((
                       m.x17 - m.x23)**2 + (m.x67 - m.x73)**2 + (m.x117 - m.x123)**2) + 1/sqrt((m.x17 - m.x24)**2 + (
                       m.x67 - m.x74)**2 + (m.x117 - m.x124)**2) + 1/sqrt((m.x17 - m.x25)**2 + (m.x67 - m.x75)**2 + (
                       m.x117 - m.x125)**2) + 1/sqrt((m.x17 - m.x26)**2 + (m.x67 - m.x76)**2 + (m.x117 - m.x126)**2) + 1
                       /sqrt((m.x17 - m.x27)**2 + (m.x67 - m.x77)**2 + (m.x117 - m.x127)**2) + 1/sqrt((m.x17 - m.x28)**2
                        + (m.x67 - m.x78)**2 + (m.x117 - m.x128)**2) + 1/sqrt((m.x17 - m.x29)**2 + (m.x67 - m.x79)**2 + 
                       (m.x117 - m.x129)**2) + 1/sqrt((m.x17 - m.x30)**2 + (m.x67 - m.x80)**2 + (m.x117 - m.x130)**2) + 
                       1/sqrt((m.x17 - m.x31)**2 + (m.x67 - m.x81)**2 + (m.x117 - m.x131)**2) + 1/sqrt((m.x17 - m.x32)**
                       2 + (m.x67 - m.x82)**2 + (m.x117 - m.x132)**2) + 1/sqrt((m.x17 - m.x33)**2 + (m.x67 - m.x83)**2
                        + (m.x117 - m.x133)**2) + 1/sqrt((m.x17 - m.x34)**2 + (m.x67 - m.x84)**2 + (m.x117 - m.x134)**2)
                        + 1/sqrt((m.x17 - m.x35)**2 + (m.x67 - m.x85)**2 + (m.x117 - m.x135)**2) + 1/sqrt((m.x17 - m.x36
                       )**2 + (m.x67 - m.x86)**2 + (m.x117 - m.x136)**2) + 1/sqrt((m.x17 - m.x37)**2 + (m.x67 - m.x87)**
                       2 + (m.x117 - m.x137)**2) + 1/sqrt((m.x17 - m.x38)**2 + (m.x67 - m.x88)**2 + (m.x117 - m.x138)**2
                       ) + 1/sqrt((m.x17 - m.x39)**2 + (m.x67 - m.x89)**2 + (m.x117 - m.x139)**2) + 1/sqrt((m.x17 - 
                       m.x40)**2 + (m.x67 - m.x90)**2 + (m.x117 - m.x140)**2) + 1/sqrt((m.x17 - m.x41)**2 + (m.x67 - 
                       m.x91)**2 + (m.x117 - m.x141)**2) + 1/sqrt((m.x17 - m.x42)**2 + (m.x67 - m.x92)**2 + (m.x117 - 
                       m.x142)**2) + 1/sqrt((m.x17 - m.x43)**2 + (m.x67 - m.x93)**2 + (m.x117 - m.x143)**2) + 1/sqrt((
                       m.x17 - m.x44)**2 + (m.x67 - m.x94)**2 + (m.x117 - m.x144)**2) + 1/sqrt((m.x17 - m.x45)**2 + (
                       m.x67 - m.x95)**2 + (m.x117 - m.x145)**2) + 1/sqrt((m.x17 - m.x46)**2 + (m.x67 - m.x96)**2 + (
                       m.x117 - m.x146)**2) + 1/sqrt((m.x17 - m.x47)**2 + (m.x67 - m.x97)**2 + (m.x117 - m.x147)**2) + 1
                       /sqrt((m.x17 - m.x48)**2 + (m.x67 - m.x98)**2 + (m.x117 - m.x148)**2) + 1/sqrt((m.x17 - m.x49)**2
                        + (m.x67 - m.x99)**2 + (m.x117 - m.x149)**2) + 1/sqrt((m.x17 - m.x50)**2 + (m.x67 - m.x100)**2
                        + (m.x117 - m.x150)**2) + 1/sqrt((m.x18 - m.x19)**2 + (m.x68 - m.x69)**2 + (m.x118 - m.x119)**2)
                        + 1/sqrt((m.x18 - m.x20)**2 + (m.x68 - m.x70)**2 + (m.x118 - m.x120)**2) + 1/sqrt((m.x18 - m.x21
                       )**2 + (m.x68 - m.x71)**2 + (m.x118 - m.x121)**2) + 1/sqrt((m.x18 - m.x22)**2 + (m.x68 - m.x72)**
                       2 + (m.x118 - m.x122)**2) + 1/sqrt((m.x18 - m.x23)**2 + (m.x68 - m.x73)**2 + (m.x118 - m.x123)**2
                       ) + 1/sqrt((m.x18 - m.x24)**2 + (m.x68 - m.x74)**2 + (m.x118 - m.x124)**2) + 1/sqrt((m.x18 - 
                       m.x25)**2 + (m.x68 - m.x75)**2 + (m.x118 - m.x125)**2) + 1/sqrt((m.x18 - m.x26)**2 + (m.x68 - 
                       m.x76)**2 + (m.x118 - m.x126)**2) + 1/sqrt((m.x18 - m.x27)**2 + (m.x68 - m.x77)**2 + (m.x118 - 
                       m.x127)**2) + 1/sqrt((m.x18 - m.x28)**2 + (m.x68 - m.x78)**2 + (m.x118 - m.x128)**2) + 1/sqrt((
                       m.x18 - m.x29)**2 + (m.x68 - m.x79)**2 + (m.x118 - m.x129)**2) + 1/sqrt((m.x18 - m.x30)**2 + (
                       m.x68 - m.x80)**2 + (m.x118 - m.x130)**2) + 1/sqrt((m.x18 - m.x31)**2 + (m.x68 - m.x81)**2 + (
                       m.x118 - m.x131)**2) + 1/sqrt((m.x18 - m.x32)**2 + (m.x68 - m.x82)**2 + (m.x118 - m.x132)**2) + 1
                       /sqrt((m.x18 - m.x33)**2 + (m.x68 - m.x83)**2 + (m.x118 - m.x133)**2) + 1/sqrt((m.x18 - m.x34)**2
                        + (m.x68 - m.x84)**2 + (m.x118 - m.x134)**2) + 1/sqrt((m.x18 - m.x35)**2 + (m.x68 - m.x85)**2 + 
                       (m.x118 - m.x135)**2) + 1/sqrt((m.x18 - m.x36)**2 + (m.x68 - m.x86)**2 + (m.x118 - m.x136)**2) + 
                       1/sqrt((m.x18 - m.x37)**2 + (m.x68 - m.x87)**2 + (m.x118 - m.x137)**2) + 1/sqrt((m.x18 - m.x38)**
                       2 + (m.x68 - m.x88)**2 + (m.x118 - m.x138)**2) + 1/sqrt((m.x18 - m.x39)**2 + (m.x68 - m.x89)**2
                        + (m.x118 - m.x139)**2) + 1/sqrt((m.x18 - m.x40)**2 + (m.x68 - m.x90)**2 + (m.x118 - m.x140)**2)
                        + 1/sqrt((m.x18 - m.x41)**2 + (m.x68 - m.x91)**2 + (m.x118 - m.x141)**2) + 1/sqrt((m.x18 - m.x42
                       )**2 + (m.x68 - m.x92)**2 + (m.x118 - m.x142)**2) + 1/sqrt((m.x18 - m.x43)**2 + (m.x68 - m.x93)**
                       2 + (m.x118 - m.x143)**2) + 1/sqrt((m.x18 - m.x44)**2 + (m.x68 - m.x94)**2 + (m.x118 - m.x144)**2
                       ) + 1/sqrt((m.x18 - m.x45)**2 + (m.x68 - m.x95)**2 + (m.x118 - m.x145)**2) + 1/sqrt((m.x18 - 
                       m.x46)**2 + (m.x68 - m.x96)**2 + (m.x118 - m.x146)**2) + 1/sqrt((m.x18 - m.x47)**2 + (m.x68 - 
                       m.x97)**2 + (m.x118 - m.x147)**2) + 1/sqrt((m.x18 - m.x48)**2 + (m.x68 - m.x98)**2 + (m.x118 - 
                       m.x148)**2) + 1/sqrt((m.x18 - m.x49)**2 + (m.x68 - m.x99)**2 + (m.x118 - m.x149)**2) + 1/sqrt((
                       m.x18 - m.x50)**2 + (m.x68 - m.x100)**2 + (m.x118 - m.x150)**2) + 1/sqrt((m.x19 - m.x20)**2 + (
                       m.x69 - m.x70)**2 + (m.x119 - m.x120)**2) + 1/sqrt((m.x19 - m.x21)**2 + (m.x69 - m.x71)**2 + (
                       m.x119 - m.x121)**2) + 1/sqrt((m.x19 - m.x22)**2 + (m.x69 - m.x72)**2 + (m.x119 - m.x122)**2) + 1
                       /sqrt((m.x19 - m.x23)**2 + (m.x69 - m.x73)**2 + (m.x119 - m.x123)**2) + 1/sqrt((m.x19 - m.x24)**2
                        + (m.x69 - m.x74)**2 + (m.x119 - m.x124)**2) + 1/sqrt((m.x19 - m.x25)**2 + (m.x69 - m.x75)**2 + 
                       (m.x119 - m.x125)**2) + 1/sqrt((m.x19 - m.x26)**2 + (m.x69 - m.x76)**2 + (m.x119 - m.x126)**2) + 
                       1/sqrt((m.x19 - m.x27)**2 + (m.x69 - m.x77)**2 + (m.x119 - m.x127)**2) + 1/sqrt((m.x19 - m.x28)**
                       2 + (m.x69 - m.x78)**2 + (m.x119 - m.x128)**2) + 1/sqrt((m.x19 - m.x29)**2 + (m.x69 - m.x79)**2
                        + (m.x119 - m.x129)**2) + 1/sqrt((m.x19 - m.x30)**2 + (m.x69 - m.x80)**2 + (m.x119 - m.x130)**2)
                        + 1/sqrt((m.x19 - m.x31)**2 + (m.x69 - m.x81)**2 + (m.x119 - m.x131)**2) + 1/sqrt((m.x19 - m.x32
                       )**2 + (m.x69 - m.x82)**2 + (m.x119 - m.x132)**2) + 1/sqrt((m.x19 - m.x33)**2 + (m.x69 - m.x83)**
                       2 + (m.x119 - m.x133)**2) + 1/sqrt((m.x19 - m.x34)**2 + (m.x69 - m.x84)**2 + (m.x119 - m.x134)**2
                       ) + 1/sqrt((m.x19 - m.x35)**2 + (m.x69 - m.x85)**2 + (m.x119 - m.x135)**2) + 1/sqrt((m.x19 - 
                       m.x36)**2 + (m.x69 - m.x86)**2 + (m.x119 - m.x136)**2) + 1/sqrt((m.x19 - m.x37)**2 + (m.x69 - 
                       m.x87)**2 + (m.x119 - m.x137)**2) + 1/sqrt((m.x19 - m.x38)**2 + (m.x69 - m.x88)**2 + (m.x119 - 
                       m.x138)**2) + 1/sqrt((m.x19 - m.x39)**2 + (m.x69 - m.x89)**2 + (m.x119 - m.x139)**2) + 1/sqrt((
                       m.x19 - m.x40)**2 + (m.x69 - m.x90)**2 + (m.x119 - m.x140)**2) + 1/sqrt((m.x19 - m.x41)**2 + (
                       m.x69 - m.x91)**2 + (m.x119 - m.x141)**2) + 1/sqrt((m.x19 - m.x42)**2 + (m.x69 - m.x92)**2 + (
                       m.x119 - m.x142)**2) + 1/sqrt((m.x19 - m.x43)**2 + (m.x69 - m.x93)**2 + (m.x119 - m.x143)**2) + 1
                       /sqrt((m.x19 - m.x44)**2 + (m.x69 - m.x94)**2 + (m.x119 - m.x144)**2) + 1/sqrt((m.x19 - m.x45)**2
                        + (m.x69 - m.x95)**2 + (m.x119 - m.x145)**2) + 1/sqrt((m.x19 - m.x46)**2 + (m.x69 - m.x96)**2 + 
                       (m.x119 - m.x146)**2) + 1/sqrt((m.x19 - m.x47)**2 + (m.x69 - m.x97)**2 + (m.x119 - m.x147)**2) + 
                       1/sqrt((m.x19 - m.x48)**2 + (m.x69 - m.x98)**2 + (m.x119 - m.x148)**2) + 1/sqrt((m.x19 - m.x49)**
                       2 + (m.x69 - m.x99)**2 + (m.x119 - m.x149)**2) + 1/sqrt((m.x19 - m.x50)**2 + (m.x69 - m.x100)**2
                        + (m.x119 - m.x150)**2) + 1/sqrt((m.x20 - m.x21)**2 + (m.x70 - m.x71)**2 + (m.x120 - m.x121)**2)
                        + 1/sqrt((m.x20 - m.x22)**2 + (m.x70 - m.x72)**2 + (m.x120 - m.x122)**2) + 1/sqrt((m.x20 - m.x23
                       )**2 + (m.x70 - m.x73)**2 + (m.x120 - m.x123)**2) + 1/sqrt((m.x20 - m.x24)**2 + (m.x70 - m.x74)**
                       2 + (m.x120 - m.x124)**2) + 1/sqrt((m.x20 - m.x25)**2 + (m.x70 - m.x75)**2 + (m.x120 - m.x125)**2
                       ) + 1/sqrt((m.x20 - m.x26)**2 + (m.x70 - m.x76)**2 + (m.x120 - m.x126)**2) + 1/sqrt((m.x20 - 
                       m.x27)**2 + (m.x70 - m.x77)**2 + (m.x120 - m.x127)**2) + 1/sqrt((m.x20 - m.x28)**2 + (m.x70 - 
                       m.x78)**2 + (m.x120 - m.x128)**2) + 1/sqrt((m.x20 - m.x29)**2 + (m.x70 - m.x79)**2 + (m.x120 - 
                       m.x129)**2) + 1/sqrt((m.x20 - m.x30)**2 + (m.x70 - m.x80)**2 + (m.x120 - m.x130)**2) + 1/sqrt((
                       m.x20 - m.x31)**2 + (m.x70 - m.x81)**2 + (m.x120 - m.x131)**2) + 1/sqrt((m.x20 - m.x32)**2 + (
                       m.x70 - m.x82)**2 + (m.x120 - m.x132)**2) + 1/sqrt((m.x20 - m.x33)**2 + (m.x70 - m.x83)**2 + (
                       m.x120 - m.x133)**2) + 1/sqrt((m.x20 - m.x34)**2 + (m.x70 - m.x84)**2 + (m.x120 - m.x134)**2) + 1
                       /sqrt((m.x20 - m.x35)**2 + (m.x70 - m.x85)**2 + (m.x120 - m.x135)**2) + 1/sqrt((m.x20 - m.x36)**2
                        + (m.x70 - m.x86)**2 + (m.x120 - m.x136)**2) + 1/sqrt((m.x20 - m.x37)**2 + (m.x70 - m.x87)**2 + 
                       (m.x120 - m.x137)**2) + 1/sqrt((m.x20 - m.x38)**2 + (m.x70 - m.x88)**2 + (m.x120 - m.x138)**2) + 
                       1/sqrt((m.x20 - m.x39)**2 + (m.x70 - m.x89)**2 + (m.x120 - m.x139)**2) + 1/sqrt((m.x20 - m.x40)**
                       2 + (m.x70 - m.x90)**2 + (m.x120 - m.x140)**2) + 1/sqrt((m.x20 - m.x41)**2 + (m.x70 - m.x91)**2
                        + (m.x120 - m.x141)**2) + 1/sqrt((m.x20 - m.x42)**2 + (m.x70 - m.x92)**2 + (m.x120 - m.x142)**2)
                        + 1/sqrt((m.x20 - m.x43)**2 + (m.x70 - m.x93)**2 + (m.x120 - m.x143)**2) + 1/sqrt((m.x20 - m.x44
                       )**2 + (m.x70 - m.x94)**2 + (m.x120 - m.x144)**2) + 1/sqrt((m.x20 - m.x45)**2 + (m.x70 - m.x95)**
                       2 + (m.x120 - m.x145)**2) + 1/sqrt((m.x20 - m.x46)**2 + (m.x70 - m.x96)**2 + (m.x120 - m.x146)**2
                       ) + 1/sqrt((m.x20 - m.x47)**2 + (m.x70 - m.x97)**2 + (m.x120 - m.x147)**2) + 1/sqrt((m.x20 - 
                       m.x48)**2 + (m.x70 - m.x98)**2 + (m.x120 - m.x148)**2) + 1/sqrt((m.x20 - m.x49)**2 + (m.x70 - 
                       m.x99)**2 + (m.x120 - m.x149)**2) + 1/sqrt((m.x20 - m.x50)**2 + (m.x70 - m.x100)**2 + (m.x120 - 
                       m.x150)**2) + 1/sqrt((m.x21 - m.x22)**2 + (m.x71 - m.x72)**2 + (m.x121 - m.x122)**2) + 1/sqrt((
                       m.x21 - m.x23)**2 + (m.x71 - m.x73)**2 + (m.x121 - m.x123)**2) + 1/sqrt((m.x21 - m.x24)**2 + (
                       m.x71 - m.x74)**2 + (m.x121 - m.x124)**2) + 1/sqrt((m.x21 - m.x25)**2 + (m.x71 - m.x75)**2 + (
                       m.x121 - m.x125)**2) + 1/sqrt((m.x21 - m.x26)**2 + (m.x71 - m.x76)**2 + (m.x121 - m.x126)**2) + 1
                       /sqrt((m.x21 - m.x27)**2 + (m.x71 - m.x77)**2 + (m.x121 - m.x127)**2) + 1/sqrt((m.x21 - m.x28)**2
                        + (m.x71 - m.x78)**2 + (m.x121 - m.x128)**2) + 1/sqrt((m.x21 - m.x29)**2 + (m.x71 - m.x79)**2 + 
                       (m.x121 - m.x129)**2) + 1/sqrt((m.x21 - m.x30)**2 + (m.x71 - m.x80)**2 + (m.x121 - m.x130)**2) + 
                       1/sqrt((m.x21 - m.x31)**2 + (m.x71 - m.x81)**2 + (m.x121 - m.x131)**2) + 1/sqrt((m.x21 - m.x32)**
                       2 + (m.x71 - m.x82)**2 + (m.x121 - m.x132)**2) + 1/sqrt((m.x21 - m.x33)**2 + (m.x71 - m.x83)**2
                        + (m.x121 - m.x133)**2) + 1/sqrt((m.x21 - m.x34)**2 + (m.x71 - m.x84)**2 + (m.x121 - m.x134)**2)
                        + 1/sqrt((m.x21 - m.x35)**2 + (m.x71 - m.x85)**2 + (m.x121 - m.x135)**2) + 1/sqrt((m.x21 - m.x36
                       )**2 + (m.x71 - m.x86)**2 + (m.x121 - m.x136)**2) + 1/sqrt((m.x21 - m.x37)**2 + (m.x71 - m.x87)**
                       2 + (m.x121 - m.x137)**2) + 1/sqrt((m.x21 - m.x38)**2 + (m.x71 - m.x88)**2 + (m.x121 - m.x138)**2
                       ) + 1/sqrt((m.x21 - m.x39)**2 + (m.x71 - m.x89)**2 + (m.x121 - m.x139)**2) + 1/sqrt((m.x21 - 
                       m.x40)**2 + (m.x71 - m.x90)**2 + (m.x121 - m.x140)**2) + 1/sqrt((m.x21 - m.x41)**2 + (m.x71 - 
                       m.x91)**2 + (m.x121 - m.x141)**2) + 1/sqrt((m.x21 - m.x42)**2 + (m.x71 - m.x92)**2 + (m.x121 - 
                       m.x142)**2) + 1/sqrt((m.x21 - m.x43)**2 + (m.x71 - m.x93)**2 + (m.x121 - m.x143)**2) + 1/sqrt((
                       m.x21 - m.x44)**2 + (m.x71 - m.x94)**2 + (m.x121 - m.x144)**2) + 1/sqrt((m.x21 - m.x45)**2 + (
                       m.x71 - m.x95)**2 + (m.x121 - m.x145)**2) + 1/sqrt((m.x21 - m.x46)**2 + (m.x71 - m.x96)**2 + (
                       m.x121 - m.x146)**2) + 1/sqrt((m.x21 - m.x47)**2 + (m.x71 - m.x97)**2 + (m.x121 - m.x147)**2) + 1
                       /sqrt((m.x21 - m.x48)**2 + (m.x71 - m.x98)**2 + (m.x121 - m.x148)**2) + 1/sqrt((m.x21 - m.x49)**2
                        + (m.x71 - m.x99)**2 + (m.x121 - m.x149)**2) + 1/sqrt((m.x21 - m.x50)**2 + (m.x71 - m.x100)**2
                        + (m.x121 - m.x150)**2) + 1/sqrt((m.x22 - m.x23)**2 + (m.x72 - m.x73)**2 + (m.x122 - m.x123)**2)
                        + 1/sqrt((m.x22 - m.x24)**2 + (m.x72 - m.x74)**2 + (m.x122 - m.x124)**2) + 1/sqrt((m.x22 - m.x25
                       )**2 + (m.x72 - m.x75)**2 + (m.x122 - m.x125)**2) + 1/sqrt((m.x22 - m.x26)**2 + (m.x72 - m.x76)**
                       2 + (m.x122 - m.x126)**2) + 1/sqrt((m.x22 - m.x27)**2 + (m.x72 - m.x77)**2 + (m.x122 - m.x127)**2
                       ) + 1/sqrt((m.x22 - m.x28)**2 + (m.x72 - m.x78)**2 + (m.x122 - m.x128)**2) + 1/sqrt((m.x22 - 
                       m.x29)**2 + (m.x72 - m.x79)**2 + (m.x122 - m.x129)**2) + 1/sqrt((m.x22 - m.x30)**2 + (m.x72 - 
                       m.x80)**2 + (m.x122 - m.x130)**2) + 1/sqrt((m.x22 - m.x31)**2 + (m.x72 - m.x81)**2 + (m.x122 - 
                       m.x131)**2) + 1/sqrt((m.x22 - m.x32)**2 + (m.x72 - m.x82)**2 + (m.x122 - m.x132)**2) + 1/sqrt((
                       m.x22 - m.x33)**2 + (m.x72 - m.x83)**2 + (m.x122 - m.x133)**2) + 1/sqrt((m.x22 - m.x34)**2 + (
                       m.x72 - m.x84)**2 + (m.x122 - m.x134)**2) + 1/sqrt((m.x22 - m.x35)**2 + (m.x72 - m.x85)**2 + (
                       m.x122 - m.x135)**2) + 1/sqrt((m.x22 - m.x36)**2 + (m.x72 - m.x86)**2 + (m.x122 - m.x136)**2) + 1
                       /sqrt((m.x22 - m.x37)**2 + (m.x72 - m.x87)**2 + (m.x122 - m.x137)**2) + 1/sqrt((m.x22 - m.x38)**2
                        + (m.x72 - m.x88)**2 + (m.x122 - m.x138)**2) + 1/sqrt((m.x22 - m.x39)**2 + (m.x72 - m.x89)**2 + 
                       (m.x122 - m.x139)**2) + 1/sqrt((m.x22 - m.x40)**2 + (m.x72 - m.x90)**2 + (m.x122 - m.x140)**2) + 
                       1/sqrt((m.x22 - m.x41)**2 + (m.x72 - m.x91)**2 + (m.x122 - m.x141)**2) + 1/sqrt((m.x22 - m.x42)**
                       2 + (m.x72 - m.x92)**2 + (m.x122 - m.x142)**2) + 1/sqrt((m.x22 - m.x43)**2 + (m.x72 - m.x93)**2
                        + (m.x122 - m.x143)**2) + 1/sqrt((m.x22 - m.x44)**2 + (m.x72 - m.x94)**2 + (m.x122 - m.x144)**2)
                        + 1/sqrt((m.x22 - m.x45)**2 + (m.x72 - m.x95)**2 + (m.x122 - m.x145)**2) + 1/sqrt((m.x22 - m.x46
                       )**2 + (m.x72 - m.x96)**2 + (m.x122 - m.x146)**2) + 1/sqrt((m.x22 - m.x47)**2 + (m.x72 - m.x97)**
                       2 + (m.x122 - m.x147)**2) + 1/sqrt((m.x22 - m.x48)**2 + (m.x72 - m.x98)**2 + (m.x122 - m.x148)**2
                       ) + 1/sqrt((m.x22 - m.x49)**2 + (m.x72 - m.x99)**2 + (m.x122 - m.x149)**2) + 1/sqrt((m.x22 - 
                       m.x50)**2 + (m.x72 - m.x100)**2 + (m.x122 - m.x150)**2) + 1/sqrt((m.x23 - m.x24)**2 + (m.x73 - 
                       m.x74)**2 + (m.x123 - m.x124)**2) + 1/sqrt((m.x23 - m.x25)**2 + (m.x73 - m.x75)**2 + (m.x123 - 
                       m.x125)**2) + 1/sqrt((m.x23 - m.x26)**2 + (m.x73 - m.x76)**2 + (m.x123 - m.x126)**2) + 1/sqrt((
                       m.x23 - m.x27)**2 + (m.x73 - m.x77)**2 + (m.x123 - m.x127)**2) + 1/sqrt((m.x23 - m.x28)**2 + (
                       m.x73 - m.x78)**2 + (m.x123 - m.x128)**2) + 1/sqrt((m.x23 - m.x29)**2 + (m.x73 - m.x79)**2 + (
                       m.x123 - m.x129)**2) + 1/sqrt((m.x23 - m.x30)**2 + (m.x73 - m.x80)**2 + (m.x123 - m.x130)**2) + 1
                       /sqrt((m.x23 - m.x31)**2 + (m.x73 - m.x81)**2 + (m.x123 - m.x131)**2) + 1/sqrt((m.x23 - m.x32)**2
                        + (m.x73 - m.x82)**2 + (m.x123 - m.x132)**2) + 1/sqrt((m.x23 - m.x33)**2 + (m.x73 - m.x83)**2 + 
                       (m.x123 - m.x133)**2) + 1/sqrt((m.x23 - m.x34)**2 + (m.x73 - m.x84)**2 + (m.x123 - m.x134)**2) + 
                       1/sqrt((m.x23 - m.x35)**2 + (m.x73 - m.x85)**2 + (m.x123 - m.x135)**2) + 1/sqrt((m.x23 - m.x36)**
                       2 + (m.x73 - m.x86)**2 + (m.x123 - m.x136)**2) + 1/sqrt((m.x23 - m.x37)**2 + (m.x73 - m.x87)**2
                        + (m.x123 - m.x137)**2) + 1/sqrt((m.x23 - m.x38)**2 + (m.x73 - m.x88)**2 + (m.x123 - m.x138)**2)
                        + 1/sqrt((m.x23 - m.x39)**2 + (m.x73 - m.x89)**2 + (m.x123 - m.x139)**2) + 1/sqrt((m.x23 - m.x40
                       )**2 + (m.x73 - m.x90)**2 + (m.x123 - m.x140)**2) + 1/sqrt((m.x23 - m.x41)**2 + (m.x73 - m.x91)**
                       2 + (m.x123 - m.x141)**2) + 1/sqrt((m.x23 - m.x42)**2 + (m.x73 - m.x92)**2 + (m.x123 - m.x142)**2
                       ) + 1/sqrt((m.x23 - m.x43)**2 + (m.x73 - m.x93)**2 + (m.x123 - m.x143)**2) + 1/sqrt((m.x23 - 
                       m.x44)**2 + (m.x73 - m.x94)**2 + (m.x123 - m.x144)**2) + 1/sqrt((m.x23 - m.x45)**2 + (m.x73 - 
                       m.x95)**2 + (m.x123 - m.x145)**2) + 1/sqrt((m.x23 - m.x46)**2 + (m.x73 - m.x96)**2 + (m.x123 - 
                       m.x146)**2) + 1/sqrt((m.x23 - m.x47)**2 + (m.x73 - m.x97)**2 + (m.x123 - m.x147)**2) + 1/sqrt((
                       m.x23 - m.x48)**2 + (m.x73 - m.x98)**2 + (m.x123 - m.x148)**2) + 1/sqrt((m.x23 - m.x49)**2 + (
                       m.x73 - m.x99)**2 + (m.x123 - m.x149)**2) + 1/sqrt((m.x23 - m.x50)**2 + (m.x73 - m.x100)**2 + (
                       m.x123 - m.x150)**2) + 1/sqrt((m.x24 - m.x25)**2 + (m.x74 - m.x75)**2 + (m.x124 - m.x125)**2) + 1
                       /sqrt((m.x24 - m.x26)**2 + (m.x74 - m.x76)**2 + (m.x124 - m.x126)**2) + 1/sqrt((m.x24 - m.x27)**2
                        + (m.x74 - m.x77)**2 + (m.x124 - m.x127)**2) + 1/sqrt((m.x24 - m.x28)**2 + (m.x74 - m.x78)**2 + 
                       (m.x124 - m.x128)**2) + 1/sqrt((m.x24 - m.x29)**2 + (m.x74 - m.x79)**2 + (m.x124 - m.x129)**2) + 
                       1/sqrt((m.x24 - m.x30)**2 + (m.x74 - m.x80)**2 + (m.x124 - m.x130)**2) + 1/sqrt((m.x24 - m.x31)**
                       2 + (m.x74 - m.x81)**2 + (m.x124 - m.x131)**2) + 1/sqrt((m.x24 - m.x32)**2 + (m.x74 - m.x82)**2
                        + (m.x124 - m.x132)**2) + 1/sqrt((m.x24 - m.x33)**2 + (m.x74 - m.x83)**2 + (m.x124 - m.x133)**2)
                        + 1/sqrt((m.x24 - m.x34)**2 + (m.x74 - m.x84)**2 + (m.x124 - m.x134)**2) + 1/sqrt((m.x24 - m.x35
                       )**2 + (m.x74 - m.x85)**2 + (m.x124 - m.x135)**2) + 1/sqrt((m.x24 - m.x36)**2 + (m.x74 - m.x86)**
                       2 + (m.x124 - m.x136)**2) + 1/sqrt((m.x24 - m.x37)**2 + (m.x74 - m.x87)**2 + (m.x124 - m.x137)**2
                       ) + 1/sqrt((m.x24 - m.x38)**2 + (m.x74 - m.x88)**2 + (m.x124 - m.x138)**2) + 1/sqrt((m.x24 - 
                       m.x39)**2 + (m.x74 - m.x89)**2 + (m.x124 - m.x139)**2) + 1/sqrt((m.x24 - m.x40)**2 + (m.x74 - 
                       m.x90)**2 + (m.x124 - m.x140)**2) + 1/sqrt((m.x24 - m.x41)**2 + (m.x74 - m.x91)**2 + (m.x124 - 
                       m.x141)**2) + 1/sqrt((m.x24 - m.x42)**2 + (m.x74 - m.x92)**2 + (m.x124 - m.x142)**2) + 1/sqrt((
                       m.x24 - m.x43)**2 + (m.x74 - m.x93)**2 + (m.x124 - m.x143)**2) + 1/sqrt((m.x24 - m.x44)**2 + (
                       m.x74 - m.x94)**2 + (m.x124 - m.x144)**2) + 1/sqrt((m.x24 - m.x45)**2 + (m.x74 - m.x95)**2 + (
                       m.x124 - m.x145)**2) + 1/sqrt((m.x24 - m.x46)**2 + (m.x74 - m.x96)**2 + (m.x124 - m.x146)**2) + 1
                       /sqrt((m.x24 - m.x47)**2 + (m.x74 - m.x97)**2 + (m.x124 - m.x147)**2) + 1/sqrt((m.x24 - m.x48)**2
                        + (m.x74 - m.x98)**2 + (m.x124 - m.x148)**2) + 1/sqrt((m.x24 - m.x49)**2 + (m.x74 - m.x99)**2 + 
                       (m.x124 - m.x149)**2) + 1/sqrt((m.x24 - m.x50)**2 + (m.x74 - m.x100)**2 + (m.x124 - m.x150)**2)
                        + 1/sqrt((m.x25 - m.x26)**2 + (m.x75 - m.x76)**2 + (m.x125 - m.x126)**2) + 1/sqrt((m.x25 - m.x27
                       )**2 + (m.x75 - m.x77)**2 + (m.x125 - m.x127)**2) + 1/sqrt((m.x25 - m.x28)**2 + (m.x75 - m.x78)**
                       2 + (m.x125 - m.x128)**2) + 1/sqrt((m.x25 - m.x29)**2 + (m.x75 - m.x79)**2 + (m.x125 - m.x129)**2
                       ) + 1/sqrt((m.x25 - m.x30)**2 + (m.x75 - m.x80)**2 + (m.x125 - m.x130)**2) + 1/sqrt((m.x25 - 
                       m.x31)**2 + (m.x75 - m.x81)**2 + (m.x125 - m.x131)**2) + 1/sqrt((m.x25 - m.x32)**2 + (m.x75 - 
                       m.x82)**2 + (m.x125 - m.x132)**2) + 1/sqrt((m.x25 - m.x33)**2 + (m.x75 - m.x83)**2 + (m.x125 - 
                       m.x133)**2) + 1/sqrt((m.x25 - m.x34)**2 + (m.x75 - m.x84)**2 + (m.x125 - m.x134)**2) + 1/sqrt((
                       m.x25 - m.x35)**2 + (m.x75 - m.x85)**2 + (m.x125 - m.x135)**2) + 1/sqrt((m.x25 - m.x36)**2 + (
                       m.x75 - m.x86)**2 + (m.x125 - m.x136)**2) + 1/sqrt((m.x25 - m.x37)**2 + (m.x75 - m.x87)**2 + (
                       m.x125 - m.x137)**2) + 1/sqrt((m.x25 - m.x38)**2 + (m.x75 - m.x88)**2 + (m.x125 - m.x138)**2) + 1
                       /sqrt((m.x25 - m.x39)**2 + (m.x75 - m.x89)**2 + (m.x125 - m.x139)**2) + 1/sqrt((m.x25 - m.x40)**2
                        + (m.x75 - m.x90)**2 + (m.x125 - m.x140)**2) + 1/sqrt((m.x25 - m.x41)**2 + (m.x75 - m.x91)**2 + 
                       (m.x125 - m.x141)**2) + 1/sqrt((m.x25 - m.x42)**2 + (m.x75 - m.x92)**2 + (m.x125 - m.x142)**2) + 
                       1/sqrt((m.x25 - m.x43)**2 + (m.x75 - m.x93)**2 + (m.x125 - m.x143)**2) + 1/sqrt((m.x25 - m.x44)**
                       2 + (m.x75 - m.x94)**2 + (m.x125 - m.x144)**2) + 1/sqrt((m.x25 - m.x45)**2 + (m.x75 - m.x95)**2
                        + (m.x125 - m.x145)**2) + 1/sqrt((m.x25 - m.x46)**2 + (m.x75 - m.x96)**2 + (m.x125 - m.x146)**2)
                        + 1/sqrt((m.x25 - m.x47)**2 + (m.x75 - m.x97)**2 + (m.x125 - m.x147)**2) + 1/sqrt((m.x25 - m.x48
                       )**2 + (m.x75 - m.x98)**2 + (m.x125 - m.x148)**2) + 1/sqrt((m.x25 - m.x49)**2 + (m.x75 - m.x99)**
                       2 + (m.x125 - m.x149)**2) + 1/sqrt((m.x25 - m.x50)**2 + (m.x75 - m.x100)**2 + (m.x125 - m.x150)**
                       2) + 1/sqrt((m.x26 - m.x27)**2 + (m.x76 - m.x77)**2 + (m.x126 - m.x127)**2) + 1/sqrt((m.x26 - 
                       m.x28)**2 + (m.x76 - m.x78)**2 + (m.x126 - m.x128)**2) + 1/sqrt((m.x26 - m.x29)**2 + (m.x76 - 
                       m.x79)**2 + (m.x126 - m.x129)**2) + 1/sqrt((m.x26 - m.x30)**2 + (m.x76 - m.x80)**2 + (m.x126 - 
                       m.x130)**2) + 1/sqrt((m.x26 - m.x31)**2 + (m.x76 - m.x81)**2 + (m.x126 - m.x131)**2) + 1/sqrt((
                       m.x26 - m.x32)**2 + (m.x76 - m.x82)**2 + (m.x126 - m.x132)**2) + 1/sqrt((m.x26 - m.x33)**2 + (
                       m.x76 - m.x83)**2 + (m.x126 - m.x133)**2) + 1/sqrt((m.x26 - m.x34)**2 + (m.x76 - m.x84)**2 + (
                       m.x126 - m.x134)**2) + 1/sqrt((m.x26 - m.x35)**2 + (m.x76 - m.x85)**2 + (m.x126 - m.x135)**2) + 1
                       /sqrt((m.x26 - m.x36)**2 + (m.x76 - m.x86)**2 + (m.x126 - m.x136)**2) + 1/sqrt((m.x26 - m.x37)**2
                        + (m.x76 - m.x87)**2 + (m.x126 - m.x137)**2) + 1/sqrt((m.x26 - m.x38)**2 + (m.x76 - m.x88)**2 + 
                       (m.x126 - m.x138)**2) + 1/sqrt((m.x26 - m.x39)**2 + (m.x76 - m.x89)**2 + (m.x126 - m.x139)**2) + 
                       1/sqrt((m.x26 - m.x40)**2 + (m.x76 - m.x90)**2 + (m.x126 - m.x140)**2) + 1/sqrt((m.x26 - m.x41)**
                       2 + (m.x76 - m.x91)**2 + (m.x126 - m.x141)**2) + 1/sqrt((m.x26 - m.x42)**2 + (m.x76 - m.x92)**2
                        + (m.x126 - m.x142)**2) + 1/sqrt((m.x26 - m.x43)**2 + (m.x76 - m.x93)**2 + (m.x126 - m.x143)**2)
                        + 1/sqrt((m.x26 - m.x44)**2 + (m.x76 - m.x94)**2 + (m.x126 - m.x144)**2) + 1/sqrt((m.x26 - m.x45
                       )**2 + (m.x76 - m.x95)**2 + (m.x126 - m.x145)**2) + 1/sqrt((m.x26 - m.x46)**2 + (m.x76 - m.x96)**
                       2 + (m.x126 - m.x146)**2) + 1/sqrt((m.x26 - m.x47)**2 + (m.x76 - m.x97)**2 + (m.x126 - m.x147)**2
                       ) + 1/sqrt((m.x26 - m.x48)**2 + (m.x76 - m.x98)**2 + (m.x126 - m.x148)**2) + 1/sqrt((m.x26 - 
                       m.x49)**2 + (m.x76 - m.x99)**2 + (m.x126 - m.x149)**2) + 1/sqrt((m.x26 - m.x50)**2 + (m.x76 - 
                       m.x100)**2 + (m.x126 - m.x150)**2) + 1/sqrt((m.x27 - m.x28)**2 + (m.x77 - m.x78)**2 + (m.x127 - 
                       m.x128)**2) + 1/sqrt((m.x27 - m.x29)**2 + (m.x77 - m.x79)**2 + (m.x127 - m.x129)**2) + 1/sqrt((
                       m.x27 - m.x30)**2 + (m.x77 - m.x80)**2 + (m.x127 - m.x130)**2) + 1/sqrt((m.x27 - m.x31)**2 + (
                       m.x77 - m.x81)**2 + (m.x127 - m.x131)**2) + 1/sqrt((m.x27 - m.x32)**2 + (m.x77 - m.x82)**2 + (
                       m.x127 - m.x132)**2) + 1/sqrt((m.x27 - m.x33)**2 + (m.x77 - m.x83)**2 + (m.x127 - m.x133)**2) + 1
                       /sqrt((m.x27 - m.x34)**2 + (m.x77 - m.x84)**2 + (m.x127 - m.x134)**2) + 1/sqrt((m.x27 - m.x35)**2
                        + (m.x77 - m.x85)**2 + (m.x127 - m.x135)**2) + 1/sqrt((m.x27 - m.x36)**2 + (m.x77 - m.x86)**2 + 
                       (m.x127 - m.x136)**2) + 1/sqrt((m.x27 - m.x37)**2 + (m.x77 - m.x87)**2 + (m.x127 - m.x137)**2) + 
                       1/sqrt((m.x27 - m.x38)**2 + (m.x77 - m.x88)**2 + (m.x127 - m.x138)**2) + 1/sqrt((m.x27 - m.x39)**
                       2 + (m.x77 - m.x89)**2 + (m.x127 - m.x139)**2) + 1/sqrt((m.x27 - m.x40)**2 + (m.x77 - m.x90)**2
                        + (m.x127 - m.x140)**2) + 1/sqrt((m.x27 - m.x41)**2 + (m.x77 - m.x91)**2 + (m.x127 - m.x141)**2)
                        + 1/sqrt((m.x27 - m.x42)**2 + (m.x77 - m.x92)**2 + (m.x127 - m.x142)**2) + 1/sqrt((m.x27 - m.x43
                       )**2 + (m.x77 - m.x93)**2 + (m.x127 - m.x143)**2) + 1/sqrt((m.x27 - m.x44)**2 + (m.x77 - m.x94)**
                       2 + (m.x127 - m.x144)**2) + 1/sqrt((m.x27 - m.x45)**2 + (m.x77 - m.x95)**2 + (m.x127 - m.x145)**2
                       ) + 1/sqrt((m.x27 - m.x46)**2 + (m.x77 - m.x96)**2 + (m.x127 - m.x146)**2) + 1/sqrt((m.x27 - 
                       m.x47)**2 + (m.x77 - m.x97)**2 + (m.x127 - m.x147)**2) + 1/sqrt((m.x27 - m.x48)**2 + (m.x77 - 
                       m.x98)**2 + (m.x127 - m.x148)**2) + 1/sqrt((m.x27 - m.x49)**2 + (m.x77 - m.x99)**2 + (m.x127 - 
                       m.x149)**2) + 1/sqrt((m.x27 - m.x50)**2 + (m.x77 - m.x100)**2 + (m.x127 - m.x150)**2) + 1/sqrt((
                       m.x28 - m.x29)**2 + (m.x78 - m.x79)**2 + (m.x128 - m.x129)**2) + 1/sqrt((m.x28 - m.x30)**2 + (
                       m.x78 - m.x80)**2 + (m.x128 - m.x130)**2) + 1/sqrt((m.x28 - m.x31)**2 + (m.x78 - m.x81)**2 + (
                       m.x128 - m.x131)**2) + 1/sqrt((m.x28 - m.x32)**2 + (m.x78 - m.x82)**2 + (m.x128 - m.x132)**2) + 1
                       /sqrt((m.x28 - m.x33)**2 + (m.x78 - m.x83)**2 + (m.x128 - m.x133)**2) + 1/sqrt((m.x28 - m.x34)**2
                        + (m.x78 - m.x84)**2 + (m.x128 - m.x134)**2) + 1/sqrt((m.x28 - m.x35)**2 + (m.x78 - m.x85)**2 + 
                       (m.x128 - m.x135)**2) + 1/sqrt((m.x28 - m.x36)**2 + (m.x78 - m.x86)**2 + (m.x128 - m.x136)**2) + 
                       1/sqrt((m.x28 - m.x37)**2 + (m.x78 - m.x87)**2 + (m.x128 - m.x137)**2) + 1/sqrt((m.x28 - m.x38)**
                       2 + (m.x78 - m.x88)**2 + (m.x128 - m.x138)**2) + 1/sqrt((m.x28 - m.x39)**2 + (m.x78 - m.x89)**2
                        + (m.x128 - m.x139)**2) + 1/sqrt((m.x28 - m.x40)**2 + (m.x78 - m.x90)**2 + (m.x128 - m.x140)**2)
                        + 1/sqrt((m.x28 - m.x41)**2 + (m.x78 - m.x91)**2 + (m.x128 - m.x141)**2) + 1/sqrt((m.x28 - m.x42
                       )**2 + (m.x78 - m.x92)**2 + (m.x128 - m.x142)**2) + 1/sqrt((m.x28 - m.x43)**2 + (m.x78 - m.x93)**
                       2 + (m.x128 - m.x143)**2) + 1/sqrt((m.x28 - m.x44)**2 + (m.x78 - m.x94)**2 + (m.x128 - m.x144)**2
                       ) + 1/sqrt((m.x28 - m.x45)**2 + (m.x78 - m.x95)**2 + (m.x128 - m.x145)**2) + 1/sqrt((m.x28 - 
                       m.x46)**2 + (m.x78 - m.x96)**2 + (m.x128 - m.x146)**2) + 1/sqrt((m.x28 - m.x47)**2 + (m.x78 - 
                       m.x97)**2 + (m.x128 - m.x147)**2) + 1/sqrt((m.x28 - m.x48)**2 + (m.x78 - m.x98)**2 + (m.x128 - 
                       m.x148)**2) + 1/sqrt((m.x28 - m.x49)**2 + (m.x78 - m.x99)**2 + (m.x128 - m.x149)**2) + 1/sqrt((
                       m.x28 - m.x50)**2 + (m.x78 - m.x100)**2 + (m.x128 - m.x150)**2) + 1/sqrt((m.x29 - m.x30)**2 + (
                       m.x79 - m.x80)**2 + (m.x129 - m.x130)**2) + 1/sqrt((m.x29 - m.x31)**2 + (m.x79 - m.x81)**2 + (
                       m.x129 - m.x131)**2) + 1/sqrt((m.x29 - m.x32)**2 + (m.x79 - m.x82)**2 + (m.x129 - m.x132)**2) + 1
                       /sqrt((m.x29 - m.x33)**2 + (m.x79 - m.x83)**2 + (m.x129 - m.x133)**2) + 1/sqrt((m.x29 - m.x34)**2
                        + (m.x79 - m.x84)**2 + (m.x129 - m.x134)**2) + 1/sqrt((m.x29 - m.x35)**2 + (m.x79 - m.x85)**2 + 
                       (m.x129 - m.x135)**2) + 1/sqrt((m.x29 - m.x36)**2 + (m.x79 - m.x86)**2 + (m.x129 - m.x136)**2) + 
                       1/sqrt((m.x29 - m.x37)**2 + (m.x79 - m.x87)**2 + (m.x129 - m.x137)**2) + 1/sqrt((m.x29 - m.x38)**
                       2 + (m.x79 - m.x88)**2 + (m.x129 - m.x138)**2) + 1/sqrt((m.x29 - m.x39)**2 + (m.x79 - m.x89)**2
                        + (m.x129 - m.x139)**2) + 1/sqrt((m.x29 - m.x40)**2 + (m.x79 - m.x90)**2 + (m.x129 - m.x140)**2)
                        + 1/sqrt((m.x29 - m.x41)**2 + (m.x79 - m.x91)**2 + (m.x129 - m.x141)**2) + 1/sqrt((m.x29 - m.x42
                       )**2 + (m.x79 - m.x92)**2 + (m.x129 - m.x142)**2) + 1/sqrt((m.x29 - m.x43)**2 + (m.x79 - m.x93)**
                       2 + (m.x129 - m.x143)**2) + 1/sqrt((m.x29 - m.x44)**2 + (m.x79 - m.x94)**2 + (m.x129 - m.x144)**2
                       ) + 1/sqrt((m.x29 - m.x45)**2 + (m.x79 - m.x95)**2 + (m.x129 - m.x145)**2) + 1/sqrt((m.x29 - 
                       m.x46)**2 + (m.x79 - m.x96)**2 + (m.x129 - m.x146)**2) + 1/sqrt((m.x29 - m.x47)**2 + (m.x79 - 
                       m.x97)**2 + (m.x129 - m.x147)**2) + 1/sqrt((m.x29 - m.x48)**2 + (m.x79 - m.x98)**2 + (m.x129 - 
                       m.x148)**2) + 1/sqrt((m.x29 - m.x49)**2 + (m.x79 - m.x99)**2 + (m.x129 - m.x149)**2) + 1/sqrt((
                       m.x29 - m.x50)**2 + (m.x79 - m.x100)**2 + (m.x129 - m.x150)**2) + 1/sqrt((m.x30 - m.x31)**2 + (
                       m.x80 - m.x81)**2 + (m.x130 - m.x131)**2) + 1/sqrt((m.x30 - m.x32)**2 + (m.x80 - m.x82)**2 + (
                       m.x130 - m.x132)**2) + 1/sqrt((m.x30 - m.x33)**2 + (m.x80 - m.x83)**2 + (m.x130 - m.x133)**2) + 1
                       /sqrt((m.x30 - m.x34)**2 + (m.x80 - m.x84)**2 + (m.x130 - m.x134)**2) + 1/sqrt((m.x30 - m.x35)**2
                        + (m.x80 - m.x85)**2 + (m.x130 - m.x135)**2) + 1/sqrt((m.x30 - m.x36)**2 + (m.x80 - m.x86)**2 + 
                       (m.x130 - m.x136)**2) + 1/sqrt((m.x30 - m.x37)**2 + (m.x80 - m.x87)**2 + (m.x130 - m.x137)**2) + 
                       1/sqrt((m.x30 - m.x38)**2 + (m.x80 - m.x88)**2 + (m.x130 - m.x138)**2) + 1/sqrt((m.x30 - m.x39)**
                       2 + (m.x80 - m.x89)**2 + (m.x130 - m.x139)**2) + 1/sqrt((m.x30 - m.x40)**2 + (m.x80 - m.x90)**2
                        + (m.x130 - m.x140)**2) + 1/sqrt((m.x30 - m.x41)**2 + (m.x80 - m.x91)**2 + (m.x130 - m.x141)**2)
                        + 1/sqrt((m.x30 - m.x42)**2 + (m.x80 - m.x92)**2 + (m.x130 - m.x142)**2) + 1/sqrt((m.x30 - m.x43
                       )**2 + (m.x80 - m.x93)**2 + (m.x130 - m.x143)**2) + 1/sqrt((m.x30 - m.x44)**2 + (m.x80 - m.x94)**
                       2 + (m.x130 - m.x144)**2) + 1/sqrt((m.x30 - m.x45)**2 + (m.x80 - m.x95)**2 + (m.x130 - m.x145)**2
                       ) + 1/sqrt((m.x30 - m.x46)**2 + (m.x80 - m.x96)**2 + (m.x130 - m.x146)**2) + 1/sqrt((m.x30 - 
                       m.x47)**2 + (m.x80 - m.x97)**2 + (m.x130 - m.x147)**2) + 1/sqrt((m.x30 - m.x48)**2 + (m.x80 - 
                       m.x98)**2 + (m.x130 - m.x148)**2) + 1/sqrt((m.x30 - m.x49)**2 + (m.x80 - m.x99)**2 + (m.x130 - 
                       m.x149)**2) + 1/sqrt((m.x30 - m.x50)**2 + (m.x80 - m.x100)**2 + (m.x130 - m.x150)**2) + 1/sqrt((
                       m.x31 - m.x32)**2 + (m.x81 - m.x82)**2 + (m.x131 - m.x132)**2) + 1/sqrt((m.x31 - m.x33)**2 + (
                       m.x81 - m.x83)**2 + (m.x131 - m.x133)**2) + 1/sqrt((m.x31 - m.x34)**2 + (m.x81 - m.x84)**2 + (
                       m.x131 - m.x134)**2) + 1/sqrt((m.x31 - m.x35)**2 + (m.x81 - m.x85)**2 + (m.x131 - m.x135)**2) + 1
                       /sqrt((m.x31 - m.x36)**2 + (m.x81 - m.x86)**2 + (m.x131 - m.x136)**2) + 1/sqrt((m.x31 - m.x37)**2
                        + (m.x81 - m.x87)**2 + (m.x131 - m.x137)**2) + 1/sqrt((m.x31 - m.x38)**2 + (m.x81 - m.x88)**2 + 
                       (m.x131 - m.x138)**2) + 1/sqrt((m.x31 - m.x39)**2 + (m.x81 - m.x89)**2 + (m.x131 - m.x139)**2) + 
                       1/sqrt((m.x31 - m.x40)**2 + (m.x81 - m.x90)**2 + (m.x131 - m.x140)**2) + 1/sqrt((m.x31 - m.x41)**
                       2 + (m.x81 - m.x91)**2 + (m.x131 - m.x141)**2) + 1/sqrt((m.x31 - m.x42)**2 + (m.x81 - m.x92)**2
                        + (m.x131 - m.x142)**2) + 1/sqrt((m.x31 - m.x43)**2 + (m.x81 - m.x93)**2 + (m.x131 - m.x143)**2)
                        + 1/sqrt((m.x31 - m.x44)**2 + (m.x81 - m.x94)**2 + (m.x131 - m.x144)**2) + 1/sqrt((m.x31 - m.x45
                       )**2 + (m.x81 - m.x95)**2 + (m.x131 - m.x145)**2) + 1/sqrt((m.x31 - m.x46)**2 + (m.x81 - m.x96)**
                       2 + (m.x131 - m.x146)**2) + 1/sqrt((m.x31 - m.x47)**2 + (m.x81 - m.x97)**2 + (m.x131 - m.x147)**2
                       ) + 1/sqrt((m.x31 - m.x48)**2 + (m.x81 - m.x98)**2 + (m.x131 - m.x148)**2) + 1/sqrt((m.x31 - 
                       m.x49)**2 + (m.x81 - m.x99)**2 + (m.x131 - m.x149)**2) + 1/sqrt((m.x31 - m.x50)**2 + (m.x81 - 
                       m.x100)**2 + (m.x131 - m.x150)**2) + 1/sqrt((m.x32 - m.x33)**2 + (m.x82 - m.x83)**2 + (m.x132 - 
                       m.x133)**2) + 1/sqrt((m.x32 - m.x34)**2 + (m.x82 - m.x84)**2 + (m.x132 - m.x134)**2) + 1/sqrt((
                       m.x32 - m.x35)**2 + (m.x82 - m.x85)**2 + (m.x132 - m.x135)**2) + 1/sqrt((m.x32 - m.x36)**2 + (
                       m.x82 - m.x86)**2 + (m.x132 - m.x136)**2) + 1/sqrt((m.x32 - m.x37)**2 + (m.x82 - m.x87)**2 + (
                       m.x132 - m.x137)**2) + 1/sqrt((m.x32 - m.x38)**2 + (m.x82 - m.x88)**2 + (m.x132 - m.x138)**2) + 1
                       /sqrt((m.x32 - m.x39)**2 + (m.x82 - m.x89)**2 + (m.x132 - m.x139)**2) + 1/sqrt((m.x32 - m.x40)**2
                        + (m.x82 - m.x90)**2 + (m.x132 - m.x140)**2) + 1/sqrt((m.x32 - m.x41)**2 + (m.x82 - m.x91)**2 + 
                       (m.x132 - m.x141)**2) + 1/sqrt((m.x32 - m.x42)**2 + (m.x82 - m.x92)**2 + (m.x132 - m.x142)**2) + 
                       1/sqrt((m.x32 - m.x43)**2 + (m.x82 - m.x93)**2 + (m.x132 - m.x143)**2) + 1/sqrt((m.x32 - m.x44)**
                       2 + (m.x82 - m.x94)**2 + (m.x132 - m.x144)**2) + 1/sqrt((m.x32 - m.x45)**2 + (m.x82 - m.x95)**2
                        + (m.x132 - m.x145)**2) + 1/sqrt((m.x32 - m.x46)**2 + (m.x82 - m.x96)**2 + (m.x132 - m.x146)**2)
                        + 1/sqrt((m.x32 - m.x47)**2 + (m.x82 - m.x97)**2 + (m.x132 - m.x147)**2) + 1/sqrt((m.x32 - m.x48
                       )**2 + (m.x82 - m.x98)**2 + (m.x132 - m.x148)**2) + 1/sqrt((m.x32 - m.x49)**2 + (m.x82 - m.x99)**
                       2 + (m.x132 - m.x149)**2) + 1/sqrt((m.x32 - m.x50)**2 + (m.x82 - m.x100)**2 + (m.x132 - m.x150)**
                       2) + 1/sqrt((m.x33 - m.x34)**2 + (m.x83 - m.x84)**2 + (m.x133 - m.x134)**2) + 1/sqrt((m.x33 - 
                       m.x35)**2 + (m.x83 - m.x85)**2 + (m.x133 - m.x135)**2) + 1/sqrt((m.x33 - m.x36)**2 + (m.x83 - 
                       m.x86)**2 + (m.x133 - m.x136)**2) + 1/sqrt((m.x33 - m.x37)**2 + (m.x83 - m.x87)**2 + (m.x133 - 
                       m.x137)**2) + 1/sqrt((m.x33 - m.x38)**2 + (m.x83 - m.x88)**2 + (m.x133 - m.x138)**2) + 1/sqrt((
                       m.x33 - m.x39)**2 + (m.x83 - m.x89)**2 + (m.x133 - m.x139)**2) + 1/sqrt((m.x33 - m.x40)**2 + (
                       m.x83 - m.x90)**2 + (m.x133 - m.x140)**2) + 1/sqrt((m.x33 - m.x41)**2 + (m.x83 - m.x91)**2 + (
                       m.x133 - m.x141)**2) + 1/sqrt((m.x33 - m.x42)**2 + (m.x83 - m.x92)**2 + (m.x133 - m.x142)**2) + 1
                       /sqrt((m.x33 - m.x43)**2 + (m.x83 - m.x93)**2 + (m.x133 - m.x143)**2) + 1/sqrt((m.x33 - m.x44)**2
                        + (m.x83 - m.x94)**2 + (m.x133 - m.x144)**2) + 1/sqrt((m.x33 - m.x45)**2 + (m.x83 - m.x95)**2 + 
                       (m.x133 - m.x145)**2) + 1/sqrt((m.x33 - m.x46)**2 + (m.x83 - m.x96)**2 + (m.x133 - m.x146)**2) + 
                       1/sqrt((m.x33 - m.x47)**2 + (m.x83 - m.x97)**2 + (m.x133 - m.x147)**2) + 1/sqrt((m.x33 - m.x48)**
                       2 + (m.x83 - m.x98)**2 + (m.x133 - m.x148)**2) + 1/sqrt((m.x33 - m.x49)**2 + (m.x83 - m.x99)**2
                        + (m.x133 - m.x149)**2) + 1/sqrt((m.x33 - m.x50)**2 + (m.x83 - m.x100)**2 + (m.x133 - m.x150)**2
                       ) + 1/sqrt((m.x34 - m.x35)**2 + (m.x84 - m.x85)**2 + (m.x134 - m.x135)**2) + 1/sqrt((m.x34 - 
                       m.x36)**2 + (m.x84 - m.x86)**2 + (m.x134 - m.x136)**2) + 1/sqrt((m.x34 - m.x37)**2 + (m.x84 - 
                       m.x87)**2 + (m.x134 - m.x137)**2) + 1/sqrt((m.x34 - m.x38)**2 + (m.x84 - m.x88)**2 + (m.x134 - 
                       m.x138)**2) + 1/sqrt((m.x34 - m.x39)**2 + (m.x84 - m.x89)**2 + (m.x134 - m.x139)**2) + 1/sqrt((
                       m.x34 - m.x40)**2 + (m.x84 - m.x90)**2 + (m.x134 - m.x140)**2) + 1/sqrt((m.x34 - m.x41)**2 + (
                       m.x84 - m.x91)**2 + (m.x134 - m.x141)**2) + 1/sqrt((m.x34 - m.x42)**2 + (m.x84 - m.x92)**2 + (
                       m.x134 - m.x142)**2) + 1/sqrt((m.x34 - m.x43)**2 + (m.x84 - m.x93)**2 + (m.x134 - m.x143)**2) + 1
                       /sqrt((m.x34 - m.x44)**2 + (m.x84 - m.x94)**2 + (m.x134 - m.x144)**2) + 1/sqrt((m.x34 - m.x45)**2
                        + (m.x84 - m.x95)**2 + (m.x134 - m.x145)**2) + 1/sqrt((m.x34 - m.x46)**2 + (m.x84 - m.x96)**2 + 
                       (m.x134 - m.x146)**2) + 1/sqrt((m.x34 - m.x47)**2 + (m.x84 - m.x97)**2 + (m.x134 - m.x147)**2) + 
                       1/sqrt((m.x34 - m.x48)**2 + (m.x84 - m.x98)**2 + (m.x134 - m.x148)**2) + 1/sqrt((m.x34 - m.x49)**
                       2 + (m.x84 - m.x99)**2 + (m.x134 - m.x149)**2) + 1/sqrt((m.x34 - m.x50)**2 + (m.x84 - m.x100)**2
                        + (m.x134 - m.x150)**2) + 1/sqrt((m.x35 - m.x36)**2 + (m.x85 - m.x86)**2 + (m.x135 - m.x136)**2)
                        + 1/sqrt((m.x35 - m.x37)**2 + (m.x85 - m.x87)**2 + (m.x135 - m.x137)**2) + 1/sqrt((m.x35 - m.x38
                       )**2 + (m.x85 - m.x88)**2 + (m.x135 - m.x138)**2) + 1/sqrt((m.x35 - m.x39)**2 + (m.x85 - m.x89)**
                       2 + (m.x135 - m.x139)**2) + 1/sqrt((m.x35 - m.x40)**2 + (m.x85 - m.x90)**2 + (m.x135 - m.x140)**2
                       ) + 1/sqrt((m.x35 - m.x41)**2 + (m.x85 - m.x91)**2 + (m.x135 - m.x141)**2) + 1/sqrt((m.x35 - 
                       m.x42)**2 + (m.x85 - m.x92)**2 + (m.x135 - m.x142)**2) + 1/sqrt((m.x35 - m.x43)**2 + (m.x85 - 
                       m.x93)**2 + (m.x135 - m.x143)**2) + 1/sqrt((m.x35 - m.x44)**2 + (m.x85 - m.x94)**2 + (m.x135 - 
                       m.x144)**2) + 1/sqrt((m.x35 - m.x45)**2 + (m.x85 - m.x95)**2 + (m.x135 - m.x145)**2) + 1/sqrt((
                       m.x35 - m.x46)**2 + (m.x85 - m.x96)**2 + (m.x135 - m.x146)**2) + 1/sqrt((m.x35 - m.x47)**2 + (
                       m.x85 - m.x97)**2 + (m.x135 - m.x147)**2) + 1/sqrt((m.x35 - m.x48)**2 + (m.x85 - m.x98)**2 + (
                       m.x135 - m.x148)**2) + 1/sqrt((m.x35 - m.x49)**2 + (m.x85 - m.x99)**2 + (m.x135 - m.x149)**2) + 1
                       /sqrt((m.x35 - m.x50)**2 + (m.x85 - m.x100)**2 + (m.x135 - m.x150)**2) + 1/sqrt((m.x36 - m.x37)**
                       2 + (m.x86 - m.x87)**2 + (m.x136 - m.x137)**2) + 1/sqrt((m.x36 - m.x38)**2 + (m.x86 - m.x88)**2
                        + (m.x136 - m.x138)**2) + 1/sqrt((m.x36 - m.x39)**2 + (m.x86 - m.x89)**2 + (m.x136 - m.x139)**2)
                        + 1/sqrt((m.x36 - m.x40)**2 + (m.x86 - m.x90)**2 + (m.x136 - m.x140)**2) + 1/sqrt((m.x36 - m.x41
                       )**2 + (m.x86 - m.x91)**2 + (m.x136 - m.x141)**2) + 1/sqrt((m.x36 - m.x42)**2 + (m.x86 - m.x92)**
                       2 + (m.x136 - m.x142)**2) + 1/sqrt((m.x36 - m.x43)**2 + (m.x86 - m.x93)**2 + (m.x136 - m.x143)**2
                       ) + 1/sqrt((m.x36 - m.x44)**2 + (m.x86 - m.x94)**2 + (m.x136 - m.x144)**2) + 1/sqrt((m.x36 - 
                       m.x45)**2 + (m.x86 - m.x95)**2 + (m.x136 - m.x145)**2) + 1/sqrt((m.x36 - m.x46)**2 + (m.x86 - 
                       m.x96)**2 + (m.x136 - m.x146)**2) + 1/sqrt((m.x36 - m.x47)**2 + (m.x86 - m.x97)**2 + (m.x136 - 
                       m.x147)**2) + 1/sqrt((m.x36 - m.x48)**2 + (m.x86 - m.x98)**2 + (m.x136 - m.x148)**2) + 1/sqrt((
                       m.x36 - m.x49)**2 + (m.x86 - m.x99)**2 + (m.x136 - m.x149)**2) + 1/sqrt((m.x36 - m.x50)**2 + (
                       m.x86 - m.x100)**2 + (m.x136 - m.x150)**2) + 1/sqrt((m.x37 - m.x38)**2 + (m.x87 - m.x88)**2 + (
                       m.x137 - m.x138)**2) + 1/sqrt((m.x37 - m.x39)**2 + (m.x87 - m.x89)**2 + (m.x137 - m.x139)**2) + 1
                       /sqrt((m.x37 - m.x40)**2 + (m.x87 - m.x90)**2 + (m.x137 - m.x140)**2) + 1/sqrt((m.x37 - m.x41)**2
                        + (m.x87 - m.x91)**2 + (m.x137 - m.x141)**2) + 1/sqrt((m.x37 - m.x42)**2 + (m.x87 - m.x92)**2 + 
                       (m.x137 - m.x142)**2) + 1/sqrt((m.x37 - m.x43)**2 + (m.x87 - m.x93)**2 + (m.x137 - m.x143)**2) + 
                       1/sqrt((m.x37 - m.x44)**2 + (m.x87 - m.x94)**2 + (m.x137 - m.x144)**2) + 1/sqrt((m.x37 - m.x45)**
                       2 + (m.x87 - m.x95)**2 + (m.x137 - m.x145)**2) + 1/sqrt((m.x37 - m.x46)**2 + (m.x87 - m.x96)**2
                        + (m.x137 - m.x146)**2) + 1/sqrt((m.x37 - m.x47)**2 + (m.x87 - m.x97)**2 + (m.x137 - m.x147)**2)
                        + 1/sqrt((m.x37 - m.x48)**2 + (m.x87 - m.x98)**2 + (m.x137 - m.x148)**2) + 1/sqrt((m.x37 - m.x49
                       )**2 + (m.x87 - m.x99)**2 + (m.x137 - m.x149)**2) + 1/sqrt((m.x37 - m.x50)**2 + (m.x87 - m.x100)
                       **2 + (m.x137 - m.x150)**2) + 1/sqrt((m.x38 - m.x39)**2 + (m.x88 - m.x89)**2 + (m.x138 - m.x139)
                       **2) + 1/sqrt((m.x38 - m.x40)**2 + (m.x88 - m.x90)**2 + (m.x138 - m.x140)**2) + 1/sqrt((m.x38 - 
                       m.x41)**2 + (m.x88 - m.x91)**2 + (m.x138 - m.x141)**2) + 1/sqrt((m.x38 - m.x42)**2 + (m.x88 - 
                       m.x92)**2 + (m.x138 - m.x142)**2) + 1/sqrt((m.x38 - m.x43)**2 + (m.x88 - m.x93)**2 + (m.x138 - 
                       m.x143)**2) + 1/sqrt((m.x38 - m.x44)**2 + (m.x88 - m.x94)**2 + (m.x138 - m.x144)**2) + 1/sqrt((
                       m.x38 - m.x45)**2 + (m.x88 - m.x95)**2 + (m.x138 - m.x145)**2) + 1/sqrt((m.x38 - m.x46)**2 + (
                       m.x88 - m.x96)**2 + (m.x138 - m.x146)**2) + 1/sqrt((m.x38 - m.x47)**2 + (m.x88 - m.x97)**2 + (
                       m.x138 - m.x147)**2) + 1/sqrt((m.x38 - m.x48)**2 + (m.x88 - m.x98)**2 + (m.x138 - m.x148)**2) + 1
                       /sqrt((m.x38 - m.x49)**2 + (m.x88 - m.x99)**2 + (m.x138 - m.x149)**2) + 1/sqrt((m.x38 - m.x50)**2
                        + (m.x88 - m.x100)**2 + (m.x138 - m.x150)**2) + 1/sqrt((m.x39 - m.x40)**2 + (m.x89 - m.x90)**2
                        + (m.x139 - m.x140)**2) + 1/sqrt((m.x39 - m.x41)**2 + (m.x89 - m.x91)**2 + (m.x139 - m.x141)**2)
                        + 1/sqrt((m.x39 - m.x42)**2 + (m.x89 - m.x92)**2 + (m.x139 - m.x142)**2) + 1/sqrt((m.x39 - m.x43
                       )**2 + (m.x89 - m.x93)**2 + (m.x139 - m.x143)**2) + 1/sqrt((m.x39 - m.x44)**2 + (m.x89 - m.x94)**
                       2 + (m.x139 - m.x144)**2) + 1/sqrt((m.x39 - m.x45)**2 + (m.x89 - m.x95)**2 + (m.x139 - m.x145)**2
                       ) + 1/sqrt((m.x39 - m.x46)**2 + (m.x89 - m.x96)**2 + (m.x139 - m.x146)**2) + 1/sqrt((m.x39 - 
                       m.x47)**2 + (m.x89 - m.x97)**2 + (m.x139 - m.x147)**2) + 1/sqrt((m.x39 - m.x48)**2 + (m.x89 - 
                       m.x98)**2 + (m.x139 - m.x148)**2) + 1/sqrt((m.x39 - m.x49)**2 + (m.x89 - m.x99)**2 + (m.x139 - 
                       m.x149)**2) + 1/sqrt((m.x39 - m.x50)**2 + (m.x89 - m.x100)**2 + (m.x139 - m.x150)**2) + 1/sqrt((
                       m.x40 - m.x41)**2 + (m.x90 - m.x91)**2 + (m.x140 - m.x141)**2) + 1/sqrt((m.x40 - m.x42)**2 + (
                       m.x90 - m.x92)**2 + (m.x140 - m.x142)**2) + 1/sqrt((m.x40 - m.x43)**2 + (m.x90 - m.x93)**2 + (
                       m.x140 - m.x143)**2) + 1/sqrt((m.x40 - m.x44)**2 + (m.x90 - m.x94)**2 + (m.x140 - m.x144)**2) + 1
                       /sqrt((m.x40 - m.x45)**2 + (m.x90 - m.x95)**2 + (m.x140 - m.x145)**2) + 1/sqrt((m.x40 - m.x46)**2
                        + (m.x90 - m.x96)**2 + (m.x140 - m.x146)**2) + 1/sqrt((m.x40 - m.x47)**2 + (m.x90 - m.x97)**2 + 
                       (m.x140 - m.x147)**2) + 1/sqrt((m.x40 - m.x48)**2 + (m.x90 - m.x98)**2 + (m.x140 - m.x148)**2) + 
                       1/sqrt((m.x40 - m.x49)**2 + (m.x90 - m.x99)**2 + (m.x140 - m.x149)**2) + 1/sqrt((m.x40 - m.x50)**
                       2 + (m.x90 - m.x100)**2 + (m.x140 - m.x150)**2) + 1/sqrt((m.x41 - m.x42)**2 + (m.x91 - m.x92)**2
                        + (m.x141 - m.x142)**2) + 1/sqrt((m.x41 - m.x43)**2 + (m.x91 - m.x93)**2 + (m.x141 - m.x143)**2)
                        + 1/sqrt((m.x41 - m.x44)**2 + (m.x91 - m.x94)**2 + (m.x141 - m.x144)**2) + 1/sqrt((m.x41 - m.x45
                       )**2 + (m.x91 - m.x95)**2 + (m.x141 - m.x145)**2) + 1/sqrt((m.x41 - m.x46)**2 + (m.x91 - m.x96)**
                       2 + (m.x141 - m.x146)**2) + 1/sqrt((m.x41 - m.x47)**2 + (m.x91 - m.x97)**2 + (m.x141 - m.x147)**2
                       ) + 1/sqrt((m.x41 - m.x48)**2 + (m.x91 - m.x98)**2 + (m.x141 - m.x148)**2) + 1/sqrt((m.x41 - 
                       m.x49)**2 + (m.x91 - m.x99)**2 + (m.x141 - m.x149)**2) + 1/sqrt((m.x41 - m.x50)**2 + (m.x91 - 
                       m.x100)**2 + (m.x141 - m.x150)**2) + 1/sqrt((m.x42 - m.x43)**2 + (m.x92 - m.x93)**2 + (m.x142 - 
                       m.x143)**2) + 1/sqrt((m.x42 - m.x44)**2 + (m.x92 - m.x94)**2 + (m.x142 - m.x144)**2) + 1/sqrt((
                       m.x42 - m.x45)**2 + (m.x92 - m.x95)**2 + (m.x142 - m.x145)**2) + 1/sqrt((m.x42 - m.x46)**2 + (
                       m.x92 - m.x96)**2 + (m.x142 - m.x146)**2) + 1/sqrt((m.x42 - m.x47)**2 + (m.x92 - m.x97)**2 + (
                       m.x142 - m.x147)**2) + 1/sqrt((m.x42 - m.x48)**2 + (m.x92 - m.x98)**2 + (m.x142 - m.x148)**2) + 1
                       /sqrt((m.x42 - m.x49)**2 + (m.x92 - m.x99)**2 + (m.x142 - m.x149)**2) + 1/sqrt((m.x42 - m.x50)**2
                        + (m.x92 - m.x100)**2 + (m.x142 - m.x150)**2) + 1/sqrt((m.x43 - m.x44)**2 + (m.x93 - m.x94)**2
                        + (m.x143 - m.x144)**2) + 1/sqrt((m.x43 - m.x45)**2 + (m.x93 - m.x95)**2 + (m.x143 - m.x145)**2)
                        + 1/sqrt((m.x43 - m.x46)**2 + (m.x93 - m.x96)**2 + (m.x143 - m.x146)**2) + 1/sqrt((m.x43 - m.x47
                       )**2 + (m.x93 - m.x97)**2 + (m.x143 - m.x147)**2) + 1/sqrt((m.x43 - m.x48)**2 + (m.x93 - m.x98)**
                       2 + (m.x143 - m.x148)**2) + 1/sqrt((m.x43 - m.x49)**2 + (m.x93 - m.x99)**2 + (m.x143 - m.x149)**2
                       ) + 1/sqrt((m.x43 - m.x50)**2 + (m.x93 - m.x100)**2 + (m.x143 - m.x150)**2) + 1/sqrt((m.x44 - 
                       m.x45)**2 + (m.x94 - m.x95)**2 + (m.x144 - m.x145)**2) + 1/sqrt((m.x44 - m.x46)**2 + (m.x94 - 
                       m.x96)**2 + (m.x144 - m.x146)**2) + 1/sqrt((m.x44 - m.x47)**2 + (m.x94 - m.x97)**2 + (m.x144 - 
                       m.x147)**2) + 1/sqrt((m.x44 - m.x48)**2 + (m.x94 - m.x98)**2 + (m.x144 - m.x148)**2) + 1/sqrt((
                       m.x44 - m.x49)**2 + (m.x94 - m.x99)**2 + (m.x144 - m.x149)**2) + 1/sqrt((m.x44 - m.x50)**2 + (
                       m.x94 - m.x100)**2 + (m.x144 - m.x150)**2) + 1/sqrt((m.x45 - m.x46)**2 + (m.x95 - m.x96)**2 + (
                       m.x145 - m.x146)**2) + 1/sqrt((m.x45 - m.x47)**2 + (m.x95 - m.x97)**2 + (m.x145 - m.x147)**2) + 1
                       /sqrt((m.x45 - m.x48)**2 + (m.x95 - m.x98)**2 + (m.x145 - m.x148)**2) + 1/sqrt((m.x45 - m.x49)**2
                        + (m.x95 - m.x99)**2 + (m.x145 - m.x149)**2) + 1/sqrt((m.x45 - m.x50)**2 + (m.x95 - m.x100)**2
                        + (m.x145 - m.x150)**2) + 1/sqrt((m.x46 - m.x47)**2 + (m.x96 - m.x97)**2 + (m.x146 - m.x147)**2)
                        + 1/sqrt((m.x46 - m.x48)**2 + (m.x96 - m.x98)**2 + (m.x146 - m.x148)**2) + 1/sqrt((m.x46 - m.x49
                       )**2 + (m.x96 - m.x99)**2 + (m.x146 - m.x149)**2) + 1/sqrt((m.x46 - m.x50)**2 + (m.x96 - m.x100)
                       **2 + (m.x146 - m.x150)**2) + 1/sqrt((m.x47 - m.x48)**2 + (m.x97 - m.x98)**2 + (m.x147 - m.x148)
                       **2) + 1/sqrt((m.x47 - m.x49)**2 + (m.x97 - m.x99)**2 + (m.x147 - m.x149)**2) + 1/sqrt((m.x47 - 
                       m.x50)**2 + (m.x97 - m.x100)**2 + (m.x147 - m.x150)**2) + 1/sqrt((m.x48 - m.x49)**2 + (m.x98 - 
                       m.x99)**2 + (m.x148 - m.x149)**2) + 1/sqrt((m.x48 - m.x50)**2 + (m.x98 - m.x100)**2 + (m.x148 - 
                       m.x150)**2) + 1/sqrt((m.x49 - m.x50)**2 + (m.x99 - m.x100)**2 + (m.x149 - m.x150)**2)
                       , sense=minimize)

m.c2 = Constraint(expr=m.x1**2 + m.x51**2 + m.x101**2 == 1)

m.c3 = Constraint(expr=m.x2**2 + m.x52**2 + m.x102**2 == 1)

m.c4 = Constraint(expr=m.x3**2 + m.x53**2 + m.x103**2 == 1)

m.c5 = Constraint(expr=m.x4**2 + m.x54**2 + m.x104**2 == 1)

m.c6 = Constraint(expr=m.x5**2 + m.x55**2 + m.x105**2 == 1)

m.c7 = Constraint(expr=m.x6**2 + m.x56**2 + m.x106**2 == 1)

m.c8 = Constraint(expr=m.x7**2 + m.x57**2 + m.x107**2 == 1)

m.c9 = Constraint(expr=m.x8**2 + m.x58**2 + m.x108**2 == 1)

m.c10 = Constraint(expr=m.x9**2 + m.x59**2 + m.x109**2 == 1)

m.c11 = Constraint(expr=m.x10**2 + m.x60**2 + m.x110**2 == 1)

m.c12 = Constraint(expr=m.x11**2 + m.x61**2 + m.x111**2 == 1)

m.c13 = Constraint(expr=m.x12**2 + m.x62**2 + m.x112**2 == 1)

m.c14 = Constraint(expr=m.x13**2 + m.x63**2 + m.x113**2 == 1)

m.c15 = Constraint(expr=m.x14**2 + m.x64**2 + m.x114**2 == 1)

m.c16 = Constraint(expr=m.x15**2 + m.x65**2 + m.x115**2 == 1)

m.c17 = Constraint(expr=m.x16**2 + m.x66**2 + m.x116**2 == 1)

m.c18 = Constraint(expr=m.x17**2 + m.x67**2 + m.x117**2 == 1)

m.c19 = Constraint(expr=m.x18**2 + m.x68**2 + m.x118**2 == 1)

m.c20 = Constraint(expr=m.x19**2 + m.x69**2 + m.x119**2 == 1)

m.c21 = Constraint(expr=m.x20**2 + m.x70**2 + m.x120**2 == 1)

m.c22 = Constraint(expr=m.x21**2 + m.x71**2 + m.x121**2 == 1)

m.c23 = Constraint(expr=m.x22**2 + m.x72**2 + m.x122**2 == 1)

m.c24 = Constraint(expr=m.x23**2 + m.x73**2 + m.x123**2 == 1)

m.c25 = Constraint(expr=m.x24**2 + m.x74**2 + m.x124**2 == 1)

m.c26 = Constraint(expr=m.x25**2 + m.x75**2 + m.x125**2 == 1)

m.c27 = Constraint(expr=m.x26**2 + m.x76**2 + m.x126**2 == 1)

m.c28 = Constraint(expr=m.x27**2 + m.x77**2 + m.x127**2 == 1)

m.c29 = Constraint(expr=m.x28**2 + m.x78**2 + m.x128**2 == 1)

m.c30 = Constraint(expr=m.x29**2 + m.x79**2 + m.x129**2 == 1)

m.c31 = Constraint(expr=m.x30**2 + m.x80**2 + m.x130**2 == 1)

m.c32 = Constraint(expr=m.x31**2 + m.x81**2 + m.x131**2 == 1)

m.c33 = Constraint(expr=m.x32**2 + m.x82**2 + m.x132**2 == 1)

m.c34 = Constraint(expr=m.x33**2 + m.x83**2 + m.x133**2 == 1)

m.c35 = Constraint(expr=m.x34**2 + m.x84**2 + m.x134**2 == 1)

m.c36 = Constraint(expr=m.x35**2 + m.x85**2 + m.x135**2 == 1)

m.c37 = Constraint(expr=m.x36**2 + m.x86**2 + m.x136**2 == 1)

m.c38 = Constraint(expr=m.x37**2 + m.x87**2 + m.x137**2 == 1)

m.c39 = Constraint(expr=m.x38**2 + m.x88**2 + m.x138**2 == 1)

m.c40 = Constraint(expr=m.x39**2 + m.x89**2 + m.x139**2 == 1)

m.c41 = Constraint(expr=m.x40**2 + m.x90**2 + m.x140**2 == 1)

m.c42 = Constraint(expr=m.x41**2 + m.x91**2 + m.x141**2 == 1)

m.c43 = Constraint(expr=m.x42**2 + m.x92**2 + m.x142**2 == 1)

m.c44 = Constraint(expr=m.x43**2 + m.x93**2 + m.x143**2 == 1)

m.c45 = Constraint(expr=m.x44**2 + m.x94**2 + m.x144**2 == 1)

m.c46 = Constraint(expr=m.x45**2 + m.x95**2 + m.x145**2 == 1)

m.c47 = Constraint(expr=m.x46**2 + m.x96**2 + m.x146**2 == 1)

m.c48 = Constraint(expr=m.x47**2 + m.x97**2 + m.x147**2 == 1)

m.c49 = Constraint(expr=m.x48**2 + m.x98**2 + m.x148**2 == 1)

m.c50 = Constraint(expr=m.x49**2 + m.x99**2 + m.x149**2 == 1)

m.c51 = Constraint(expr=m.x50**2 + m.x100**2 + m.x150**2 == 1)
