#  MINLP written by GAMS Convert at 04/21/18 13:52:22
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         37       37        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        109        1      108        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        217      109      108        0
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

m.obj = Objective(expr=150789*m.b1*m.b4 + 96635*m.b1*m.b7 + 82016*m.b1*m.b10 + 71188*m.b1*m.b19 + 29652*m.b1*m.b28 + 
                       27563*m.b1*m.b82 + 150789*m.b2*m.b5 + 96635*m.b2*m.b8 + 82016*m.b2*m.b11 + 71188*m.b2*m.b20 + 
                       29652*m.b2*m.b29 + 27563*m.b2*m.b83 + 150789*m.b3*m.b6 + 96635*m.b3*m.b9 + 82016*m.b3*m.b12 + 
                       71188*m.b3*m.b21 + 29652*m.b3*m.b30 + 27563*m.b3*m.b84 - 138432*m.b4*m.b7 + 135804*m.b4*m.b13 - 
                       33425*m.b4*m.b22 + 47873*m.b4*m.b31 + 37799*m.b4*m.b85 - 138432*m.b5*m.b8 + 135804*m.b5*m.b14 - 
                       33425*m.b5*m.b23 + 47873*m.b5*m.b32 + 37799*m.b5*m.b86 - 138432*m.b6*m.b9 + 135804*m.b6*m.b15 - 
                       33425*m.b6*m.b24 + 47873*m.b6*m.b33 + 37799*m.b6*m.b87 + 89572*m.b7*m.b16 - 123622*m.b7*m.b25 + 
                       36597*m.b7*m.b34 - 88889*m.b7*m.b88 + 89572*m.b8*m.b17 - 123622*m.b8*m.b26 + 36597*m.b8*m.b35 - 
                       88889*m.b8*m.b89 + 89572*m.b9*m.b18 - 123622*m.b9*m.b27 + 36597*m.b9*m.b36 - 88889*m.b9*m.b90 - 
                       28003*m.b10*m.b13 + 64386*m.b10*m.b16 + 15848*m.b10*m.b19 - 68711*m.b10*m.b37 + 20433*m.b10*m.b91
                        - 28003*m.b11*m.b14 + 64386*m.b11*m.b17 + 15848*m.b11*m.b20 - 68711*m.b11*m.b38 + 20433*m.b11*
                       m.b92 - 28003*m.b12*m.b15 + 64386*m.b12*m.b18 + 15848*m.b12*m.b21 - 68711*m.b12*m.b39 + 20433*
                       m.b12*m.b93 + 37906*m.b13*m.b16 - 100230*m.b13*m.b22 - 12359*m.b13*m.b40 + 81013*m.b13*m.b94 + 
                       37906*m.b14*m.b17 - 100230*m.b14*m.b23 - 12359*m.b14*m.b41 + 81013*m.b14*m.b95 + 37906*m.b15*
                       m.b18 - 100230*m.b15*m.b24 - 12359*m.b15*m.b42 + 81013*m.b15*m.b96 - 137368*m.b16*m.b25 + 23213*
                       m.b16*m.b43 + 23379*m.b16*m.b97 - 137368*m.b17*m.b26 + 23213*m.b17*m.b44 + 23379*m.b17*m.b98 - 
                       137368*m.b18*m.b27 + 23213*m.b18*m.b45 + 23379*m.b18*m.b99 - 98974*m.b19*m.b22 + 231831*m.b19*
                       m.b25 - 216126*m.b19*m.b46 - 217144*m.b19*m.b100 - 98974*m.b20*m.b23 + 231831*m.b20*m.b26 - 
                       216126*m.b20*m.b47 - 217144*m.b20*m.b101 - 98974*m.b21*m.b24 + 231831*m.b21*m.b27 - 216126*m.b21*
                       m.b48 - 217144*m.b21*m.b102 + 35848*m.b22*m.b25 - 56735*m.b22*m.b49 - 129635*m.b22*m.b103 + 35848
                       *m.b23*m.b26 - 56735*m.b23*m.b50 - 129635*m.b23*m.b104 + 35848*m.b24*m.b27 - 56735*m.b24*m.b51 - 
                       129635*m.b24*m.b105 + 110264*m.b25*m.b52 + 64614*m.b25*m.b106 + 110264*m.b26*m.b53 + 64614*m.b26*
                       m.b107 + 110264*m.b27*m.b54 + 64614*m.b27*m.b108 - 57506*m.b28*m.b31 - 109539*m.b28*m.b34 - 
                       153027*m.b28*m.b37 + 74221*m.b28*m.b46 - 128728*m.b28*m.b55 - 57506*m.b29*m.b32 - 109539*m.b29*
                       m.b35 - 153027*m.b29*m.b38 + 74221*m.b29*m.b47 - 128728*m.b29*m.b56 - 57506*m.b30*m.b33 - 109539*
                       m.b30*m.b36 - 153027*m.b30*m.b39 + 74221*m.b30*m.b48 - 128728*m.b30*m.b57 - 61441*m.b31*m.b34 - 
                       38352*m.b31*m.b40 + 65016*m.b31*m.b49 - 87621*m.b31*m.b58 - 61441*m.b32*m.b35 - 38352*m.b32*m.b41
                        + 65016*m.b32*m.b50 - 87621*m.b32*m.b59 - 61441*m.b33*m.b36 - 38352*m.b33*m.b42 + 65016*m.b33*
                       m.b51 - 87621*m.b33*m.b60 + 89808*m.b34*m.b43 + 202917*m.b34*m.b52 - 130041*m.b34*m.b61 + 89808*
                       m.b35*m.b44 + 202917*m.b35*m.b53 - 130041*m.b35*m.b62 + 89808*m.b36*m.b45 + 202917*m.b36*m.b54 - 
                       130041*m.b36*m.b63 + 33035*m.b37*m.b40 + 71965*m.b37*m.b43 - 55696*m.b37*m.b46 - 183316*m.b37*
                       m.b64 + 33035*m.b38*m.b41 + 71965*m.b38*m.b44 - 55696*m.b38*m.b47 - 183316*m.b38*m.b65 + 33035*
                       m.b39*m.b42 + 71965*m.b39*m.b45 - 55696*m.b39*m.b48 - 183316*m.b39*m.b66 + 77370*m.b40*m.b43 + 
                       105654*m.b40*m.b49 + 32479*m.b40*m.b67 + 77370*m.b41*m.b44 + 105654*m.b41*m.b50 + 32479*m.b41*
                       m.b68 + 77370*m.b42*m.b45 + 105654*m.b42*m.b51 + 32479*m.b42*m.b69 - 54817*m.b43*m.b52 + 23875*
                       m.b43*m.b70 - 54817*m.b44*m.b53 + 23875*m.b44*m.b71 - 54817*m.b45*m.b54 + 23875*m.b45*m.b72 + 
                       156987*m.b46*m.b49 - 97706*m.b46*m.b52 + 66291*m.b46*m.b73 + 156987*m.b47*m.b50 - 97706*m.b47*
                       m.b53 + 66291*m.b47*m.b74 + 156987*m.b48*m.b51 - 97706*m.b48*m.b54 + 66291*m.b48*m.b75 - 170907*
                       m.b49*m.b52 - 4284*m.b49*m.b76 - 170907*m.b50*m.b53 - 4284*m.b50*m.b77 - 170907*m.b51*m.b54 - 
                       4284*m.b51*m.b78 - 52892*m.b52*m.b79 - 52892*m.b53*m.b80 - 52892*m.b54*m.b81 + 140020*m.b55*m.b58
                        + 172819*m.b55*m.b61 - 68559*m.b55*m.b64 + 127058*m.b55*m.b73 - 96654*m.b55*m.b82 + 140020*m.b56
                       *m.b59 + 172819*m.b56*m.b62 - 68559*m.b56*m.b65 + 127058*m.b56*m.b74 - 96654*m.b56*m.b83 + 140020
                       *m.b57*m.b60 + 172819*m.b57*m.b63 - 68559*m.b57*m.b66 + 127058*m.b57*m.b75 - 96654*m.b57*m.b84 + 
                       53214*m.b58*m.b61 + 113790*m.b58*m.b67 + 70369*m.b58*m.b76 + 40736*m.b58*m.b85 + 53214*m.b59*
                       m.b62 + 113790*m.b59*m.b68 + 70369*m.b59*m.b77 + 40736*m.b59*m.b86 + 53214*m.b60*m.b63 + 113790*
                       m.b60*m.b69 + 70369*m.b60*m.b78 + 40736*m.b60*m.b87 - 53179*m.b61*m.b70 - 40328*m.b61*m.b79 - 
                       76183*m.b61*m.b88 - 53179*m.b62*m.b71 - 40328*m.b62*m.b80 - 76183*m.b62*m.b89 - 53179*m.b63*m.b72
                        - 40328*m.b63*m.b81 - 76183*m.b63*m.b90 + 128807*m.b64*m.b67 + 9873*m.b64*m.b70 - 163252*m.b64*
                       m.b73 + 118598*m.b64*m.b91 + 128807*m.b65*m.b68 + 9873*m.b65*m.b71 - 163252*m.b65*m.b74 + 118598*
                       m.b65*m.b92 + 128807*m.b66*m.b69 + 9873*m.b66*m.b72 - 163252*m.b66*m.b75 + 118598*m.b66*m.b93 + 
                       26118*m.b67*m.b70 - 17710*m.b67*m.b76 - 47780*m.b67*m.b94 + 26118*m.b68*m.b71 - 17710*m.b68*m.b77
                        - 47780*m.b68*m.b95 + 26118*m.b69*m.b72 - 17710*m.b69*m.b78 - 47780*m.b69*m.b96 - 194573*m.b70*
                       m.b79 + 79568*m.b70*m.b97 - 194573*m.b71*m.b80 + 79568*m.b71*m.b98 - 194573*m.b72*m.b81 + 79568*
                       m.b72*m.b99 + 134721*m.b73*m.b76 - 43693*m.b73*m.b79 - 35040*m.b73*m.b100 + 134721*m.b74*m.b77 - 
                       43693*m.b74*m.b80 - 35040*m.b74*m.b101 + 134721*m.b75*m.b78 - 43693*m.b75*m.b81 - 35040*m.b75*
                       m.b102 - 154491*m.b76*m.b79 + 126672*m.b76*m.b103 - 154491*m.b77*m.b80 + 126672*m.b77*m.b104 - 
                       154491*m.b78*m.b81 + 126672*m.b78*m.b105 + 134687*m.b79*m.b106 + 134687*m.b80*m.b107 + 134687*
                       m.b81*m.b108 - 20223*m.b82*m.b85 + 16042*m.b82*m.b88 - 71597*m.b82*m.b91 + 105213*m.b82*m.b100 - 
                       20223*m.b83*m.b86 + 16042*m.b83*m.b89 - 71597*m.b83*m.b92 + 105213*m.b83*m.b101 - 20223*m.b84*
                       m.b87 + 16042*m.b84*m.b90 - 71597*m.b84*m.b93 + 105213*m.b84*m.b102 - 23477*m.b85*m.b88 + 131588*
                       m.b85*m.b94 + 77329*m.b85*m.b103 - 23477*m.b86*m.b89 + 131588*m.b86*m.b95 + 77329*m.b86*m.b104 - 
                       23477*m.b87*m.b90 + 131588*m.b87*m.b96 + 77329*m.b87*m.b105 + 243127*m.b88*m.b97 + 106932*m.b88*
                       m.b106 + 243127*m.b89*m.b98 + 106932*m.b89*m.b107 + 243127*m.b90*m.b99 + 106932*m.b90*m.b108 + 
                       173520*m.b91*m.b94 - 14664*m.b91*m.b97 + 37621*m.b91*m.b100 + 173520*m.b92*m.b95 - 14664*m.b92*
                       m.b98 + 37621*m.b92*m.b101 + 173520*m.b93*m.b96 - 14664*m.b93*m.b99 + 37621*m.b93*m.b102 - 95030*
                       m.b94*m.b97 + 10313*m.b94*m.b103 - 95030*m.b95*m.b98 + 10313*m.b95*m.b104 - 95030*m.b96*m.b99 + 
                       10313*m.b96*m.b105 + 102942*m.b97*m.b106 + 102942*m.b98*m.b107 + 102942*m.b99*m.b108 - 244497*
                       m.b100*m.b103 - 85233*m.b100*m.b106 - 244497*m.b101*m.b104 - 85233*m.b101*m.b107 - 244497*m.b102*
                       m.b105 - 85233*m.b102*m.b108 - 96225*m.b103*m.b106 - 96225*m.b104*m.b107 - 96225*m.b105*m.b108
                       , sense=minimize)

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
