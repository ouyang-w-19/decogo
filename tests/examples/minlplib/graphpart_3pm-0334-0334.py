#  MINLP written by GAMS Convert at 04/21/18 13:52:23
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

m.obj = Objective(expr=m.b1*m.b7 - m.b1*m.b4 - m.b1*m.b10 + m.b1*m.b19 + m.b1*m.b28 + m.b1*m.b82 - m.b2*m.b5 + m.b2*m.b8
                        - m.b2*m.b11 + m.b2*m.b20 + m.b2*m.b29 + m.b2*m.b83 - m.b3*m.b6 + m.b3*m.b9 - m.b3*m.b12 + m.b3*
                       m.b21 + m.b3*m.b30 + m.b3*m.b84 - m.b4*m.b7 - m.b4*m.b13 - m.b4*m.b22 - m.b4*m.b31 + m.b4*m.b85
                        - m.b5*m.b8 - m.b5*m.b14 - m.b5*m.b23 - m.b5*m.b32 + m.b5*m.b86 - m.b6*m.b9 - m.b6*m.b15 - m.b6*
                       m.b24 - m.b6*m.b33 + m.b6*m.b87 + m.b7*m.b16 - m.b7*m.b25 + m.b7*m.b34 + m.b7*m.b88 + m.b8*m.b17
                        - m.b8*m.b26 + m.b8*m.b35 + m.b8*m.b89 + m.b9*m.b18 - m.b9*m.b27 + m.b9*m.b36 + m.b9*m.b90 + 
                       m.b10*m.b13 - m.b10*m.b16 + m.b10*m.b19 + m.b10*m.b37 - m.b10*m.b91 + m.b11*m.b14 - m.b11*m.b17
                        + m.b11*m.b20 + m.b11*m.b38 - m.b11*m.b92 + m.b12*m.b15 - m.b12*m.b18 + m.b12*m.b21 + m.b12*
                       m.b39 - m.b12*m.b93 - m.b13*m.b16 + m.b13*m.b22 + m.b13*m.b40 + m.b13*m.b94 - m.b14*m.b17 + m.b14
                       *m.b23 + m.b14*m.b41 + m.b14*m.b95 - m.b15*m.b18 + m.b15*m.b24 + m.b15*m.b42 + m.b15*m.b96 + 
                       m.b16*m.b25 + m.b16*m.b43 - m.b16*m.b97 + m.b17*m.b26 + m.b17*m.b44 - m.b17*m.b98 + m.b18*m.b27
                        + m.b18*m.b45 - m.b18*m.b99 - m.b19*m.b22 - m.b19*m.b25 + m.b19*m.b46 - m.b19*m.b100 - m.b20*
                       m.b23 - m.b20*m.b26 + m.b20*m.b47 - m.b20*m.b101 - m.b21*m.b24 - m.b21*m.b27 + m.b21*m.b48 - 
                       m.b21*m.b102 - m.b22*m.b25 - m.b22*m.b49 + m.b22*m.b103 - m.b23*m.b26 - m.b23*m.b50 + m.b23*
                       m.b104 - m.b24*m.b27 - m.b24*m.b51 + m.b24*m.b105 + m.b25*m.b52 + m.b25*m.b106 + m.b26*m.b53 + 
                       m.b26*m.b107 + m.b27*m.b54 + m.b27*m.b108 - m.b28*m.b31 - m.b28*m.b34 - m.b28*m.b37 + m.b28*m.b46
                        - m.b28*m.b55 - m.b29*m.b32 - m.b29*m.b35 - m.b29*m.b38 + m.b29*m.b47 - m.b29*m.b56 - m.b30*
                       m.b33 - m.b30*m.b36 - m.b30*m.b39 + m.b30*m.b48 - m.b30*m.b57 - m.b31*m.b34 + m.b31*m.b40 + m.b31
                       *m.b49 - m.b31*m.b58 - m.b32*m.b35 + m.b32*m.b41 + m.b32*m.b50 - m.b32*m.b59 - m.b33*m.b36 + 
                       m.b33*m.b42 + m.b33*m.b51 - m.b33*m.b60 + m.b34*m.b43 + m.b34*m.b52 + m.b34*m.b61 + m.b35*m.b44
                        + m.b35*m.b53 + m.b35*m.b62 + m.b36*m.b45 + m.b36*m.b54 + m.b36*m.b63 + m.b37*m.b40 - m.b37*
                       m.b43 - m.b37*m.b46 + m.b37*m.b64 + m.b38*m.b41 - m.b38*m.b44 - m.b38*m.b47 + m.b38*m.b65 + m.b39
                       *m.b42 - m.b39*m.b45 - m.b39*m.b48 + m.b39*m.b66 - m.b40*m.b43 + m.b40*m.b49 + m.b40*m.b67 - 
                       m.b41*m.b44 + m.b41*m.b50 + m.b41*m.b68 - m.b42*m.b45 + m.b42*m.b51 + m.b42*m.b69 - m.b43*m.b52
                        - m.b43*m.b70 - m.b44*m.b53 - m.b44*m.b71 - m.b45*m.b54 - m.b45*m.b72 + m.b46*m.b49 + m.b46*
                       m.b52 + m.b46*m.b73 + m.b47*m.b50 + m.b47*m.b53 + m.b47*m.b74 + m.b48*m.b51 + m.b48*m.b54 + m.b48
                       *m.b75 + m.b49*m.b52 - m.b49*m.b76 + m.b50*m.b53 - m.b50*m.b77 + m.b51*m.b54 - m.b51*m.b78 - 
                       m.b52*m.b79 - m.b53*m.b80 - m.b54*m.b81 - m.b55*m.b58 - m.b55*m.b61 + m.b55*m.b64 - m.b55*m.b73
                        + m.b55*m.b82 - m.b56*m.b59 - m.b56*m.b62 + m.b56*m.b65 - m.b56*m.b74 + m.b56*m.b83 - m.b57*
                       m.b60 - m.b57*m.b63 + m.b57*m.b66 - m.b57*m.b75 + m.b57*m.b84 + m.b58*m.b61 - m.b58*m.b67 + m.b58
                       *m.b76 - m.b58*m.b85 + m.b59*m.b62 - m.b59*m.b68 + m.b59*m.b77 - m.b59*m.b86 + m.b60*m.b63 - 
                       m.b60*m.b69 + m.b60*m.b78 - m.b60*m.b87 + m.b61*m.b70 - m.b61*m.b79 - m.b61*m.b88 + m.b62*m.b71
                        - m.b62*m.b80 - m.b62*m.b89 + m.b63*m.b72 - m.b63*m.b81 - m.b63*m.b90 + m.b64*m.b67 + m.b64*
                       m.b70 + m.b64*m.b73 - m.b64*m.b91 + m.b65*m.b68 + m.b65*m.b71 + m.b65*m.b74 - m.b65*m.b92 + m.b66
                       *m.b69 + m.b66*m.b72 + m.b66*m.b75 - m.b66*m.b93 + m.b67*m.b70 + m.b67*m.b76 + m.b67*m.b94 + 
                       m.b68*m.b71 + m.b68*m.b77 + m.b68*m.b95 + m.b69*m.b72 + m.b69*m.b78 + m.b69*m.b96 - m.b70*m.b79
                        - m.b70*m.b97 - m.b71*m.b80 - m.b71*m.b98 - m.b72*m.b81 - m.b72*m.b99 - m.b73*m.b76 - m.b73*
                       m.b79 - m.b73*m.b100 - m.b74*m.b77 - m.b74*m.b80 - m.b74*m.b101 - m.b75*m.b78 - m.b75*m.b81 - 
                       m.b75*m.b102 - m.b76*m.b79 - m.b76*m.b103 - m.b77*m.b80 - m.b77*m.b104 - m.b78*m.b81 - m.b78*
                       m.b105 - m.b79*m.b106 - m.b80*m.b107 - m.b81*m.b108 - m.b82*m.b85 - m.b82*m.b88 + m.b82*m.b91 + 
                       m.b82*m.b100 - m.b83*m.b86 - m.b83*m.b89 + m.b83*m.b92 + m.b83*m.b101 - m.b84*m.b87 - m.b84*m.b90
                        + m.b84*m.b93 + m.b84*m.b102 + m.b85*m.b88 - m.b85*m.b94 + m.b85*m.b103 + m.b86*m.b89 - m.b86*
                       m.b95 + m.b86*m.b104 + m.b87*m.b90 - m.b87*m.b96 + m.b87*m.b105 - m.b88*m.b97 - m.b88*m.b106 - 
                       m.b89*m.b98 - m.b89*m.b107 - m.b90*m.b99 - m.b90*m.b108 - m.b91*m.b94 + m.b91*m.b97 - m.b91*
                       m.b100 - m.b92*m.b95 + m.b92*m.b98 - m.b92*m.b101 - m.b93*m.b96 + m.b93*m.b99 - m.b93*m.b102 + 
                       m.b94*m.b97 - m.b94*m.b103 + m.b95*m.b98 - m.b95*m.b104 + m.b96*m.b99 - m.b96*m.b105 + m.b97*
                       m.b106 + m.b98*m.b107 + m.b99*m.b108 + m.b100*m.b103 - m.b100*m.b106 + m.b101*m.b104 - m.b101*
                       m.b107 + m.b102*m.b105 - m.b102*m.b108 + m.b103*m.b106 + m.b104*m.b107 + m.b105*m.b108
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
