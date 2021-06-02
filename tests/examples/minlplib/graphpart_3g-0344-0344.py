#  MINLP written by GAMS Convert at 04/21/18 13:52:22
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         49       49        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        145        1      144        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        289      145      144        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.b1 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b5 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b6 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b7 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b8 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b9 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b10 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b11 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b12 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b13 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b14 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b15 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b16 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b17 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b18 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b19 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b20 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b21 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b22 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b23 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b24 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b25 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b26 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b27 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b28 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b29 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b30 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b31 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b32 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b33 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b34 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b35 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b36 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b37 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b38 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b39 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b40 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b41 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b42 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b43 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b44 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b45 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b46 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b47 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b48 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b49 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b50 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b51 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b52 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b53 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b54 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b55 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b56 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b57 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b58 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b59 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b60 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b61 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b62 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b63 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b64 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b65 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b66 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b67 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b68 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b69 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b70 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b71 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b72 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b73 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b74 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b75 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b76 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b77 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b78 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b79 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b80 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b81 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b82 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b83 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b84 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b85 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b86 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b87 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b88 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b89 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b90 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b91 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b92 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b93 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b94 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b95 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b96 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b97 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b98 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b99 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b100 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b101 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b102 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b103 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b104 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b105 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b106 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b107 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b108 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b109 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b110 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b111 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b112 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b113 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b114 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b115 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b116 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b117 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b118 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b119 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b120 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b121 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b122 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b123 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b124 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b125 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b126 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b127 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b128 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b129 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b130 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b131 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b132 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b133 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b134 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b135 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b136 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b137 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b138 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b139 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b140 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b141 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b142 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b143 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b144 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=37177*m.b1*m.b10 - 123362*m.b1*m.b4 + 135068*m.b1*m.b13 - 10174*m.b1*m.b25 + 112363*m.b1*m.b37 - 
                       174059*m.b1*m.b109 - 123362*m.b2*m.b5 + 37177*m.b2*m.b11 + 135068*m.b2*m.b14 - 10174*m.b2*m.b26
                        + 112363*m.b2*m.b38 - 174059*m.b2*m.b110 - 123362*m.b3*m.b6 + 37177*m.b3*m.b12 + 135068*m.b3*
                       m.b15 - 10174*m.b3*m.b27 + 112363*m.b3*m.b39 - 174059*m.b3*m.b111 + 1496*m.b4*m.b7 - 86083*m.b4*
                       m.b16 + 116754*m.b4*m.b28 - 135325*m.b4*m.b40 - 78283*m.b4*m.b112 + 1496*m.b5*m.b8 - 86083*m.b5*
                       m.b17 + 116754*m.b5*m.b29 - 135325*m.b5*m.b41 - 78283*m.b5*m.b113 + 1496*m.b6*m.b9 - 86083*m.b6*
                       m.b18 + 116754*m.b6*m.b30 - 135325*m.b6*m.b42 - 78283*m.b6*m.b114 + 167165*m.b7*m.b10 + 48311*
                       m.b7*m.b19 + 168758*m.b7*m.b31 - 19619*m.b7*m.b43 + 43825*m.b7*m.b115 + 167165*m.b8*m.b11 + 48311
                       *m.b8*m.b20 + 168758*m.b8*m.b32 - 19619*m.b8*m.b44 + 43825*m.b8*m.b116 + 167165*m.b9*m.b12 + 
                       48311*m.b9*m.b21 + 168758*m.b9*m.b33 - 19619*m.b9*m.b45 + 43825*m.b9*m.b117 + 40689*m.b10*m.b22
                        + 27673*m.b10*m.b34 + 20805*m.b10*m.b46 + 45651*m.b10*m.b118 + 40689*m.b11*m.b23 + 27673*m.b11*
                       m.b35 + 20805*m.b11*m.b47 + 45651*m.b11*m.b119 + 40689*m.b12*m.b24 + 27673*m.b12*m.b36 + 20805*
                       m.b12*m.b48 + 45651*m.b12*m.b120 - 109255*m.b13*m.b16 - 119367*m.b13*m.b22 + 20179*m.b13*m.b25 - 
                       25440*m.b13*m.b49 + 248492*m.b13*m.b121 - 109255*m.b14*m.b17 - 119367*m.b14*m.b23 + 20179*m.b14*
                       m.b26 - 25440*m.b14*m.b50 + 248492*m.b14*m.b122 - 109255*m.b15*m.b18 - 119367*m.b15*m.b24 + 20179
                       *m.b15*m.b27 - 25440*m.b15*m.b51 + 248492*m.b15*m.b123 + 46814*m.b16*m.b19 + 51470*m.b16*m.b28 + 
                       80578*m.b16*m.b52 + 3701*m.b16*m.b124 + 46814*m.b17*m.b20 + 51470*m.b17*m.b29 + 80578*m.b17*m.b53
                        + 3701*m.b17*m.b125 + 46814*m.b18*m.b21 + 51470*m.b18*m.b30 + 80578*m.b18*m.b54 + 3701*m.b18*
                       m.b126 + 80772*m.b19*m.b22 + 147754*m.b19*m.b31 + 175164*m.b19*m.b55 - 1841*m.b19*m.b127 + 80772*
                       m.b20*m.b23 + 147754*m.b20*m.b32 + 175164*m.b20*m.b56 - 1841*m.b20*m.b128 + 80772*m.b21*m.b24 + 
                       147754*m.b21*m.b33 + 175164*m.b21*m.b57 - 1841*m.b21*m.b129 + 55808*m.b22*m.b34 - 217714*m.b22*
                       m.b58 + 103147*m.b22*m.b130 + 55808*m.b23*m.b35 - 217714*m.b23*m.b59 + 103147*m.b23*m.b131 + 
                       55808*m.b24*m.b36 - 217714*m.b24*m.b60 + 103147*m.b24*m.b132 - 61931*m.b25*m.b28 - 88108*m.b25*
                       m.b34 - 130441*m.b25*m.b61 + 3699*m.b25*m.b133 - 61931*m.b26*m.b29 - 88108*m.b26*m.b35 - 130441*
                       m.b26*m.b62 + 3699*m.b26*m.b134 - 61931*m.b27*m.b30 - 88108*m.b27*m.b36 - 130441*m.b27*m.b63 + 
                       3699*m.b27*m.b135 + 100468*m.b28*m.b31 - 77669*m.b28*m.b64 - 186268*m.b28*m.b136 + 100468*m.b29*
                       m.b32 - 77669*m.b29*m.b65 - 186268*m.b29*m.b137 + 100468*m.b30*m.b33 - 77669*m.b30*m.b66 - 186268
                       *m.b30*m.b138 - 128480*m.b31*m.b34 - 110381*m.b31*m.b67 - 157818*m.b31*m.b139 - 128480*m.b32*
                       m.b35 - 110381*m.b32*m.b68 - 157818*m.b32*m.b140 - 128480*m.b33*m.b36 - 110381*m.b33*m.b69 - 
                       157818*m.b33*m.b141 + 25177*m.b34*m.b70 - 66379*m.b34*m.b142 + 25177*m.b35*m.b71 - 66379*m.b35*
                       m.b143 + 25177*m.b36*m.b72 - 66379*m.b36*m.b144 + 50456*m.b37*m.b40 + 26576*m.b37*m.b46 - 45705*
                       m.b37*m.b49 + 79590*m.b37*m.b61 - 3381*m.b37*m.b73 + 50456*m.b38*m.b41 + 26576*m.b38*m.b47 - 
                       45705*m.b38*m.b50 + 79590*m.b38*m.b62 - 3381*m.b38*m.b74 + 50456*m.b39*m.b42 + 26576*m.b39*m.b48
                        - 45705*m.b39*m.b51 + 79590*m.b39*m.b63 - 3381*m.b39*m.b75 - 114651*m.b40*m.b43 - 105547*m.b40*
                       m.b52 - 92459*m.b40*m.b64 - 85605*m.b40*m.b76 - 114651*m.b41*m.b44 - 105547*m.b41*m.b53 - 92459*
                       m.b41*m.b65 - 85605*m.b41*m.b77 - 114651*m.b42*m.b45 - 105547*m.b42*m.b54 - 92459*m.b42*m.b66 - 
                       85605*m.b42*m.b78 + 60686*m.b43*m.b46 + 35436*m.b43*m.b55 + 36881*m.b43*m.b67 + 63966*m.b43*m.b79
                        + 60686*m.b44*m.b47 + 35436*m.b44*m.b56 + 36881*m.b44*m.b68 + 63966*m.b44*m.b80 + 60686*m.b45*
                       m.b48 + 35436*m.b45*m.b57 + 36881*m.b45*m.b69 + 63966*m.b45*m.b81 + 98324*m.b46*m.b58 - 142437*
                       m.b46*m.b70 - 113425*m.b46*m.b82 + 98324*m.b47*m.b59 - 142437*m.b47*m.b71 - 113425*m.b47*m.b83 + 
                       98324*m.b48*m.b60 - 142437*m.b48*m.b72 - 113425*m.b48*m.b84 - 182685*m.b49*m.b52 - 72416*m.b49*
                       m.b58 - 17870*m.b49*m.b61 + 98276*m.b49*m.b85 - 182685*m.b50*m.b53 - 72416*m.b50*m.b59 - 17870*
                       m.b50*m.b62 + 98276*m.b50*m.b86 - 182685*m.b51*m.b54 - 72416*m.b51*m.b60 - 17870*m.b51*m.b63 + 
                       98276*m.b51*m.b87 - 273533*m.b52*m.b55 - 241208*m.b52*m.b64 - 49346*m.b52*m.b88 - 273533*m.b53*
                       m.b56 - 241208*m.b53*m.b65 - 49346*m.b53*m.b89 - 273533*m.b54*m.b57 - 241208*m.b54*m.b66 - 49346*
                       m.b54*m.b90 - 64316*m.b55*m.b58 - 135240*m.b55*m.b67 - 180528*m.b55*m.b91 - 64316*m.b56*m.b59 - 
                       135240*m.b56*m.b68 - 180528*m.b56*m.b92 - 64316*m.b57*m.b60 - 135240*m.b57*m.b69 - 180528*m.b57*
                       m.b93 + 91874*m.b58*m.b70 - 3696*m.b58*m.b94 + 91874*m.b59*m.b71 - 3696*m.b59*m.b95 + 91874*m.b60
                       *m.b72 - 3696*m.b60*m.b96 - 40119*m.b61*m.b64 + 122867*m.b61*m.b70 - 61997*m.b61*m.b97 - 40119*
                       m.b62*m.b65 + 122867*m.b62*m.b71 - 61997*m.b62*m.b98 - 40119*m.b63*m.b66 + 122867*m.b63*m.b72 - 
                       61997*m.b63*m.b99 - 37348*m.b64*m.b67 + 175208*m.b64*m.b100 - 37348*m.b65*m.b68 + 175208*m.b65*
                       m.b101 - 37348*m.b66*m.b69 + 175208*m.b66*m.b102 - 22393*m.b67*m.b70 - 14921*m.b67*m.b103 - 22393
                       *m.b68*m.b71 - 14921*m.b68*m.b104 - 22393*m.b69*m.b72 - 14921*m.b69*m.b105 - 601*m.b70*m.b106 - 
                       601*m.b71*m.b107 - 601*m.b72*m.b108 - 76681*m.b73*m.b76 + 12689*m.b73*m.b82 + 208440*m.b73*m.b85
                        - 27358*m.b73*m.b97 - 73618*m.b73*m.b109 - 76681*m.b74*m.b77 + 12689*m.b74*m.b83 + 208440*m.b74*
                       m.b86 - 27358*m.b74*m.b98 - 73618*m.b74*m.b110 - 76681*m.b75*m.b78 + 12689*m.b75*m.b84 + 208440*
                       m.b75*m.b87 - 27358*m.b75*m.b99 - 73618*m.b75*m.b111 + 21498*m.b76*m.b79 + 46551*m.b76*m.b88 + 
                       150817*m.b76*m.b100 - 15190*m.b76*m.b112 + 21498*m.b77*m.b80 + 46551*m.b77*m.b89 + 150817*m.b77*
                       m.b101 - 15190*m.b77*m.b113 + 21498*m.b78*m.b81 + 46551*m.b78*m.b90 + 150817*m.b78*m.b102 - 15190
                       *m.b78*m.b114 + 28754*m.b79*m.b82 - 106952*m.b79*m.b91 - 65156*m.b79*m.b103 + 70131*m.b79*m.b115
                        + 28754*m.b80*m.b83 - 106952*m.b80*m.b92 - 65156*m.b80*m.b104 + 70131*m.b80*m.b116 + 28754*m.b81
                       *m.b84 - 106952*m.b81*m.b93 - 65156*m.b81*m.b105 + 70131*m.b81*m.b117 + 32192*m.b82*m.b94 - 81667
                       *m.b82*m.b106 - 72237*m.b82*m.b118 + 32192*m.b83*m.b95 - 81667*m.b83*m.b107 - 72237*m.b83*m.b119
                        + 32192*m.b84*m.b96 - 81667*m.b84*m.b108 - 72237*m.b84*m.b120 + 28857*m.b85*m.b88 - 21532*m.b85*
                       m.b94 + 34081*m.b85*m.b97 + 217807*m.b85*m.b121 + 28857*m.b86*m.b89 - 21532*m.b86*m.b95 + 34081*
                       m.b86*m.b98 + 217807*m.b86*m.b122 + 28857*m.b87*m.b90 - 21532*m.b87*m.b96 + 34081*m.b87*m.b99 + 
                       217807*m.b87*m.b123 - 14063*m.b88*m.b91 - 32891*m.b88*m.b100 + 150197*m.b88*m.b124 - 14063*m.b89*
                       m.b92 - 32891*m.b89*m.b101 + 150197*m.b89*m.b125 - 14063*m.b90*m.b93 - 32891*m.b90*m.b102 + 
                       150197*m.b90*m.b126 - 8558*m.b91*m.b94 - 186729*m.b91*m.b103 + 15271*m.b91*m.b127 - 8558*m.b92*
                       m.b95 - 186729*m.b92*m.b104 + 15271*m.b92*m.b128 - 8558*m.b93*m.b96 - 186729*m.b93*m.b105 + 15271
                       *m.b93*m.b129 + 99216*m.b94*m.b106 + 17426*m.b94*m.b130 + 99216*m.b95*m.b107 + 17426*m.b95*m.b131
                        + 99216*m.b96*m.b108 + 17426*m.b96*m.b132 - 84666*m.b97*m.b100 + 6362*m.b97*m.b106 - 50758*m.b97
                       *m.b133 - 84666*m.b98*m.b101 + 6362*m.b98*m.b107 - 50758*m.b98*m.b134 - 84666*m.b99*m.b102 + 6362
                       *m.b99*m.b108 - 50758*m.b99*m.b135 - 69658*m.b100*m.b103 - 124701*m.b100*m.b136 - 69658*m.b101*
                       m.b104 - 124701*m.b101*m.b137 - 69658*m.b102*m.b105 - 124701*m.b102*m.b138 - 51670*m.b103*m.b106
                        - 271413*m.b103*m.b139 - 51670*m.b104*m.b107 - 271413*m.b104*m.b140 - 51670*m.b105*m.b108 - 
                       271413*m.b105*m.b141 + 32359*m.b106*m.b142 + 32359*m.b107*m.b143 + 32359*m.b108*m.b144 + 26315*
                       m.b109*m.b112 - 173269*m.b109*m.b118 - 81930*m.b109*m.b121 + 77066*m.b109*m.b133 + 26315*m.b110*
                       m.b113 - 173269*m.b110*m.b119 - 81930*m.b110*m.b122 + 77066*m.b110*m.b134 + 26315*m.b111*m.b114
                        - 173269*m.b111*m.b120 - 81930*m.b111*m.b123 + 77066*m.b111*m.b135 + 185719*m.b112*m.b115 + 
                       48690*m.b112*m.b124 - 73445*m.b112*m.b136 + 185719*m.b113*m.b116 + 48690*m.b113*m.b125 - 73445*
                       m.b113*m.b137 + 185719*m.b114*m.b117 + 48690*m.b114*m.b126 - 73445*m.b114*m.b138 - 69569*m.b115*
                       m.b118 + 128748*m.b115*m.b127 + 72205*m.b115*m.b139 - 69569*m.b116*m.b119 + 128748*m.b116*m.b128
                        + 72205*m.b116*m.b140 - 69569*m.b117*m.b120 + 128748*m.b117*m.b129 + 72205*m.b117*m.b141 + 18784
                       *m.b118*m.b130 + 123614*m.b118*m.b142 + 18784*m.b119*m.b131 + 123614*m.b119*m.b143 + 18784*m.b120
                       *m.b132 + 123614*m.b120*m.b144 - 202564*m.b121*m.b124 + 48234*m.b121*m.b130 + 50091*m.b121*m.b133
                        - 202564*m.b122*m.b125 + 48234*m.b122*m.b131 + 50091*m.b122*m.b134 - 202564*m.b123*m.b126 + 
                       48234*m.b123*m.b132 + 50091*m.b123*m.b135 + 96700*m.b124*m.b127 + 9225*m.b124*m.b136 + 96700*
                       m.b125*m.b128 + 9225*m.b125*m.b137 + 96700*m.b126*m.b129 + 9225*m.b126*m.b138 + 109964*m.b127*
                       m.b130 + 113810*m.b127*m.b139 + 109964*m.b128*m.b131 + 113810*m.b128*m.b140 + 109964*m.b129*
                       m.b132 + 113810*m.b129*m.b141 - 118476*m.b130*m.b142 - 118476*m.b131*m.b143 - 118476*m.b132*
                       m.b144 - 36835*m.b133*m.b136 + 9987*m.b133*m.b142 - 36835*m.b134*m.b137 + 9987*m.b134*m.b143 - 
                       36835*m.b135*m.b138 + 9987*m.b135*m.b144 + 10830*m.b136*m.b139 + 10830*m.b137*m.b140 + 10830*
                       m.b138*m.b141 - 32179*m.b139*m.b142 - 32179*m.b140*m.b143 - 32179*m.b141*m.b144, sense=minimize)

m.c1 = Constraint(expr=   m.b1 + m.b2 + m.b3 == 1)

m.c2 = Constraint(expr=   m.b4 + m.b5 + m.b6 == 1)

m.c3 = Constraint(expr=   m.b7 + m.b8 + m.b9 == 1)

m.c4 = Constraint(expr=   m.b10 + m.b11 + m.b12 == 1)

m.c5 = Constraint(expr=   m.b13 + m.b14 + m.b15 == 1)

m.c6 = Constraint(expr=   m.b16 + m.b17 + m.b18 == 1)

m.c7 = Constraint(expr=   m.b19 + m.b20 + m.b21 == 1)

m.c8 = Constraint(expr=   m.b22 + m.b23 + m.b24 == 1)

m.c9 = Constraint(expr=   m.b25 + m.b26 + m.b27 == 1)

m.c10 = Constraint(expr=   m.b28 + m.b29 + m.b30 == 1)

m.c11 = Constraint(expr=   m.b31 + m.b32 + m.b33 == 1)

m.c12 = Constraint(expr=   m.b34 + m.b35 + m.b36 == 1)

m.c13 = Constraint(expr=   m.b37 + m.b38 + m.b39 == 1)

m.c14 = Constraint(expr=   m.b40 + m.b41 + m.b42 == 1)

m.c15 = Constraint(expr=   m.b43 + m.b44 + m.b45 == 1)

m.c16 = Constraint(expr=   m.b46 + m.b47 + m.b48 == 1)

m.c17 = Constraint(expr=   m.b49 + m.b50 + m.b51 == 1)

m.c18 = Constraint(expr=   m.b52 + m.b53 + m.b54 == 1)

m.c19 = Constraint(expr=   m.b55 + m.b56 + m.b57 == 1)

m.c20 = Constraint(expr=   m.b58 + m.b59 + m.b60 == 1)

m.c21 = Constraint(expr=   m.b61 + m.b62 + m.b63 == 1)

m.c22 = Constraint(expr=   m.b64 + m.b65 + m.b66 == 1)

m.c23 = Constraint(expr=   m.b67 + m.b68 + m.b69 == 1)

m.c24 = Constraint(expr=   m.b70 + m.b71 + m.b72 == 1)

m.c25 = Constraint(expr=   m.b73 + m.b74 + m.b75 == 1)

m.c26 = Constraint(expr=   m.b76 + m.b77 + m.b78 == 1)

m.c27 = Constraint(expr=   m.b79 + m.b80 + m.b81 == 1)

m.c28 = Constraint(expr=   m.b82 + m.b83 + m.b84 == 1)

m.c29 = Constraint(expr=   m.b85 + m.b86 + m.b87 == 1)

m.c30 = Constraint(expr=   m.b88 + m.b89 + m.b90 == 1)

m.c31 = Constraint(expr=   m.b91 + m.b92 + m.b93 == 1)

m.c32 = Constraint(expr=   m.b94 + m.b95 + m.b96 == 1)

m.c33 = Constraint(expr=   m.b97 + m.b98 + m.b99 == 1)

m.c34 = Constraint(expr=   m.b100 + m.b101 + m.b102 == 1)

m.c35 = Constraint(expr=   m.b103 + m.b104 + m.b105 == 1)

m.c36 = Constraint(expr=   m.b106 + m.b107 + m.b108 == 1)

m.c37 = Constraint(expr=   m.b109 + m.b110 + m.b111 == 1)

m.c38 = Constraint(expr=   m.b112 + m.b113 + m.b114 == 1)

m.c39 = Constraint(expr=   m.b115 + m.b116 + m.b117 == 1)

m.c40 = Constraint(expr=   m.b118 + m.b119 + m.b120 == 1)

m.c41 = Constraint(expr=   m.b121 + m.b122 + m.b123 == 1)

m.c42 = Constraint(expr=   m.b124 + m.b125 + m.b126 == 1)

m.c43 = Constraint(expr=   m.b127 + m.b128 + m.b129 == 1)

m.c44 = Constraint(expr=   m.b130 + m.b131 + m.b132 == 1)

m.c45 = Constraint(expr=   m.b133 + m.b134 + m.b135 == 1)

m.c46 = Constraint(expr=   m.b136 + m.b137 + m.b138 == 1)

m.c47 = Constraint(expr=   m.b139 + m.b140 + m.b141 == 1)

m.c48 = Constraint(expr=   m.b142 + m.b143 + m.b144 == 1)
