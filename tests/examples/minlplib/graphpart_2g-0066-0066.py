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

m.obj = Objective(expr=50078*m.b1*m.b4 + 117720*m.b1*m.b16 - 43049*m.b1*m.b19 + 13155*m.b1*m.b91 + 50078*m.b2*m.b5 + 
                       117720*m.b2*m.b17 - 43049*m.b2*m.b20 + 13155*m.b2*m.b92 + 50078*m.b3*m.b6 + 117720*m.b3*m.b18 - 
                       43049*m.b3*m.b21 + 13155*m.b3*m.b93 + 19451*m.b4*m.b7 - 81035*m.b4*m.b22 - 105510*m.b4*m.b94 + 
                       19451*m.b5*m.b8 - 81035*m.b5*m.b23 - 105510*m.b5*m.b95 + 19451*m.b6*m.b9 - 81035*m.b6*m.b24 - 
                       105510*m.b6*m.b96 - 31535*m.b7*m.b10 - 91808*m.b7*m.b25 + 3251*m.b7*m.b97 - 31535*m.b8*m.b11 - 
                       91808*m.b8*m.b26 + 3251*m.b8*m.b98 - 31535*m.b9*m.b12 - 91808*m.b9*m.b27 + 3251*m.b9*m.b99 + 
                       144057*m.b10*m.b13 - 102239*m.b10*m.b28 + 25384*m.b10*m.b100 + 144057*m.b11*m.b14 - 102239*m.b11*
                       m.b29 + 25384*m.b11*m.b101 + 144057*m.b12*m.b15 - 102239*m.b12*m.b30 + 25384*m.b12*m.b102 - 78656
                       *m.b13*m.b16 - 156991*m.b13*m.b31 - 26788*m.b13*m.b103 - 78656*m.b14*m.b17 - 156991*m.b14*m.b32
                        - 26788*m.b14*m.b104 - 78656*m.b15*m.b18 - 156991*m.b15*m.b33 - 26788*m.b15*m.b105 - 40629*m.b16
                       *m.b34 + 187339*m.b16*m.b106 - 40629*m.b17*m.b35 + 187339*m.b17*m.b107 - 40629*m.b18*m.b36 + 
                       187339*m.b18*m.b108 - 64123*m.b19*m.b22 + 193957*m.b19*m.b34 - 42715*m.b19*m.b37 - 64123*m.b20*
                       m.b23 + 193957*m.b20*m.b35 - 42715*m.b20*m.b38 - 64123*m.b21*m.b24 + 193957*m.b21*m.b36 - 42715*
                       m.b21*m.b39 - 109684*m.b22*m.b25 - 7040*m.b22*m.b40 - 109684*m.b23*m.b26 - 7040*m.b23*m.b41 - 
                       109684*m.b24*m.b27 - 7040*m.b24*m.b42 - 104107*m.b25*m.b28 + 4745*m.b25*m.b43 - 104107*m.b26*
                       m.b29 + 4745*m.b26*m.b44 - 104107*m.b27*m.b30 + 4745*m.b27*m.b45 - 89768*m.b28*m.b31 + 111318*
                       m.b28*m.b46 - 89768*m.b29*m.b32 + 111318*m.b29*m.b47 - 89768*m.b30*m.b33 + 111318*m.b30*m.b48 - 
                       87660*m.b31*m.b34 - 59350*m.b31*m.b49 - 87660*m.b32*m.b35 - 59350*m.b32*m.b50 - 87660*m.b33*m.b36
                        - 59350*m.b33*m.b51 - 53495*m.b34*m.b52 - 53495*m.b35*m.b53 - 53495*m.b36*m.b54 + 98616*m.b37*
                       m.b40 - 166277*m.b37*m.b52 + 121306*m.b37*m.b55 + 98616*m.b38*m.b41 - 166277*m.b38*m.b53 + 121306
                       *m.b38*m.b56 + 98616*m.b39*m.b42 - 166277*m.b39*m.b54 + 121306*m.b39*m.b57 + 185685*m.b40*m.b43
                        + 162679*m.b40*m.b58 + 185685*m.b41*m.b44 + 162679*m.b41*m.b59 + 185685*m.b42*m.b45 + 162679*
                       m.b42*m.b60 - 34358*m.b43*m.b46 - 197375*m.b43*m.b61 - 34358*m.b44*m.b47 - 197375*m.b44*m.b62 - 
                       34358*m.b45*m.b48 - 197375*m.b45*m.b63 - 57511*m.b46*m.b49 - 19008*m.b46*m.b64 - 57511*m.b47*
                       m.b50 - 19008*m.b47*m.b65 - 57511*m.b48*m.b51 - 19008*m.b48*m.b66 - 9951*m.b49*m.b52 - 7268*m.b49
                       *m.b67 - 9951*m.b50*m.b53 - 7268*m.b50*m.b68 - 9951*m.b51*m.b54 - 7268*m.b51*m.b69 - 62799*m.b52*
                       m.b70 - 62799*m.b53*m.b71 - 62799*m.b54*m.b72 - 60076*m.b55*m.b58 + 20720*m.b55*m.b70 + 53669*
                       m.b55*m.b73 - 60076*m.b56*m.b59 + 20720*m.b56*m.b71 + 53669*m.b56*m.b74 - 60076*m.b57*m.b60 + 
                       20720*m.b57*m.b72 + 53669*m.b57*m.b75 + 30538*m.b58*m.b61 - 71849*m.b58*m.b76 + 30538*m.b59*m.b62
                        - 71849*m.b59*m.b77 + 30538*m.b60*m.b63 - 71849*m.b60*m.b78 + 84983*m.b61*m.b64 + 89697*m.b61*
                       m.b79 + 84983*m.b62*m.b65 + 89697*m.b62*m.b80 + 84983*m.b63*m.b66 + 89697*m.b63*m.b81 + 123972*
                       m.b64*m.b67 - 71412*m.b64*m.b82 + 123972*m.b65*m.b68 - 71412*m.b65*m.b83 + 123972*m.b66*m.b69 - 
                       71412*m.b66*m.b84 + 98426*m.b67*m.b70 - 14872*m.b67*m.b85 + 98426*m.b68*m.b71 - 14872*m.b68*m.b86
                        + 98426*m.b69*m.b72 - 14872*m.b69*m.b87 - 139665*m.b70*m.b88 - 139665*m.b71*m.b89 - 139665*m.b72
                       *m.b90 - 13082*m.b73*m.b76 + 244658*m.b73*m.b88 + 98492*m.b73*m.b91 - 13082*m.b74*m.b77 + 244658*
                       m.b74*m.b89 + 98492*m.b74*m.b92 - 13082*m.b75*m.b78 + 244658*m.b75*m.b90 + 98492*m.b75*m.b93 + 
                       102438*m.b76*m.b79 + 36098*m.b76*m.b94 + 102438*m.b77*m.b80 + 36098*m.b77*m.b95 + 102438*m.b78*
                       m.b81 + 36098*m.b78*m.b96 + 283615*m.b79*m.b82 - 42312*m.b79*m.b97 + 283615*m.b80*m.b83 - 42312*
                       m.b80*m.b98 + 283615*m.b81*m.b84 - 42312*m.b81*m.b99 - 89738*m.b82*m.b85 - 112724*m.b82*m.b100 - 
                       89738*m.b83*m.b86 - 112724*m.b83*m.b101 - 89738*m.b84*m.b87 - 112724*m.b84*m.b102 + 46994*m.b85*
                       m.b88 - 99160*m.b85*m.b103 + 46994*m.b86*m.b89 - 99160*m.b86*m.b104 + 46994*m.b87*m.b90 - 99160*
                       m.b87*m.b105 - 36555*m.b88*m.b106 - 36555*m.b89*m.b107 - 36555*m.b90*m.b108 + 48924*m.b91*m.b94
                        - 110970*m.b91*m.b106 + 48924*m.b92*m.b95 - 110970*m.b92*m.b107 + 48924*m.b93*m.b96 - 110970*
                       m.b93*m.b108 - 189064*m.b94*m.b97 - 189064*m.b95*m.b98 - 189064*m.b96*m.b99 + 24208*m.b97*m.b100
                        + 24208*m.b98*m.b101 + 24208*m.b99*m.b102 - 202185*m.b100*m.b103 - 202185*m.b101*m.b104 - 202185
                       *m.b102*m.b105 - 4003*m.b103*m.b106 - 4003*m.b104*m.b107 - 4003*m.b105*m.b108, sense=minimize)

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
