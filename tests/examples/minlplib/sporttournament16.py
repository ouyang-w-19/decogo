#  MINLP written by GAMS Convert at 04/21/18 13:54:17
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          1        0        0        1        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        121        1      120        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        121        1      120        0


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
m.x121 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=m.x121, sense=maximize)

m.c1 = Constraint(expr=2*m.b1*m.b3 - 2*m.b1 - 2*m.b3 + 2*m.b1*m.b5 - 4*m.b5 + 2*m.b1*m.b38 + 2*m.b38 - 2*m.b1*m.b50 + 4*
                       m.b50 + 2*m.b2*m.b5 - 2*m.b2 + 2*m.b2*m.b7 - 4*m.b7 + 2*m.b2*m.b25 - 2*m.b25 - 2*m.b2*m.b68 + 2*
                       m.b68 - 2*m.b3*m.b6 - 2*m.b6 + 2*m.b3*m.b26 - 2*m.b26 + 2*m.b3*m.b39 - 2*m.b39 + 2*m.b4*m.b7 - 4*
                       m.b4 + 2*m.b4*m.b10 - 2*m.b10 + 2*m.b4*m.b18 - 2*m.b18 + 2*m.b4*m.b19 - 4*m.b19 + 2*m.b5*m.b8 - 4
                       *m.b8 + 2*m.b5*m.b39 + 2*m.b6*m.b7 + 2*m.b6*m.b15 - 4*m.b15 + 2*m.b6*m.b99 + 2*m.b7*m.b11 - 2*
                       m.b11 + 2*m.b8*m.b10 + 2*m.b8*m.b15 + 2*m.b8*m.b20 - 4*m.b20 + 2*m.b9*m.b23 - 2*m.b9 - 2*m.b23 + 
                       2*m.b9*m.b64 - 4*m.b64 + 2*m.b10*m.b14 - 2*m.b14 - 2*m.b10*m.b100 + 2*m.b11*m.b20 + 2*m.b11*m.b27
                        - 4*m.b27 - 2*m.b11*m.b71 - 2*m.b71 + 2*m.b12*m.b20 - 2*m.b12 + 2*m.b12*m.b29 - 4*m.b29 - 2*
                       m.b12*m.b99 + 2*m.b12*m.b104 + 2*m.b13*m.b18 - 2*m.b13 + 2*m.b13*m.b25 + 2*m.b14*m.b27 + 2*m.b14*
                       m.b40 - 2*m.b40 - 2*m.b14*m.b51 - 2*m.b51 + 2*m.b15*m.b21 - 4*m.b21 + 2*m.b15*m.b75 - 2*m.b75 + 2
                       *m.b16*m.b27 - 4*m.b16 + 2*m.b16*m.b29 + 2*m.b16*m.b43 - 4*m.b43 + 2*m.b16*m.b99 + 2*m.b17*m.b48
                        - 2*m.b17 - 2*m.b48 + 2*m.b17*m.b102 + 2*m.b18*m.b26 - 2*m.b18*m.b98 + 2*m.b19*m.b26 + 2*m.b19*
                       m.b103 + 2*m.b19*m.b106 + 2*m.b20*m.b28 - 2*m.b28 + 2*m.b21*m.b40 + 2*m.b21*m.b43 + 2*m.b21*m.b54
                        - 4*m.b54 - 2*m.b22*m.b23 - 2*m.b22 + 2*m.b22*m.b47 - 4*m.b47 + 2*m.b22*m.b63 - 2*m.b63 + 2*
                       m.b22*m.b107 + 2*m.b23*m.b24 - 2*m.b24 + 2*m.b23*m.b62 - 4*m.b62 + 2*m.b24*m.b63 + 2*m.b25*m.b105
                        - 2*m.b25*m.b112 - 2*m.b26*m.b114 + 2*m.b27*m.b42 - 2*m.b42 + 2*m.b28*m.b54 - 2*m.b28*m.b74 - 2*
                       m.b74 + 2*m.b28*m.b76 - 4*m.b76 + 2*m.b29*m.b30 - 2*m.b30 + 2*m.b29*m.b78 - 2*m.b78 + 2*m.b30*
                       m.b31 - 4*m.b31 + 2*m.b30*m.b76 - 2*m.b30*m.b80 + 2*m.b80 + 2*m.b31*m.b32 - 2*m.b32 + 2*m.b31*
                       m.b78 + 2*m.b31*m.b90 + 2*m.b32*m.b61 - 2*m.b61 + 2*m.b32*m.b81 - 2*m.b81 - 2*m.b32*m.b107 + 2*
                       m.b33*m.b35 - 2*m.b33 - 2*m.b35 + 2*m.b33*m.b60 - 2*m.b60 + 2*m.b33*m.b108 - 2*m.b33*m.b110 - 2*
                       m.b34*m.b48 + 2*m.b34 + 2*m.b34*m.b87 - 4*m.b87 - 2*m.b34*m.b89 - 2*m.b34*m.b94 + 2*m.b35*m.b61
                        + 2*m.b35*m.b87 - 2*m.b35*m.b102 + 2*m.b36*m.b37 - 2*m.b36 - 2*m.b37 + 2*m.b36*m.b86 - 4*m.b86
                        - 2*m.b36*m.b108 + 2*m.b36*m.b109 + 2*m.b37*m.b87 - 2*m.b38*m.b105 - 2*m.b38*m.b106 - 2*m.b38*
                       m.b116 + 2*m.b39*m.b41 - 4*m.b41 - 2*m.b39*m.b99 + 2*m.b40*m.b53 - 4*m.b53 - 2*m.b40*m.b73 - 2*
                       m.b73 + 2*m.b41*m.b52 - 2*m.b52 + 2*m.b41*m.b53 + 2*m.b41*m.b75 + 2*m.b42*m.b44 - 2*m.b44 + 2*
                       m.b42*m.b76 - 2*m.b42*m.b115 + 2*m.b43*m.b45 - 2*m.b45 + 2*m.b43*m.b56 + 2*m.b56 + 2*m.b44*m.b45
                        + 2*m.b44*m.b53 - 2*m.b44*m.b92 - 2*m.b45*m.b96 + 2*m.b45*m.b111 + 2*m.b46*m.b83 - 2*m.b46 - 2*
                       m.b83 - 2*m.b46*m.b97 + 2*m.b46*m.b107 + 2*m.b46*m.b111 + 2*m.b47*m.b82 - 2*m.b82 + 2*m.b47*m.b85
                        - 2*m.b85 + 2*m.b47*m.b110 + 2*m.b48*m.b108 + 2*m.b48*m.b118 - 2*m.b49*m.b68 + 2*m.b49 - 2*m.b49
                       *m.b117 - 2*m.b50*m.b66 + 2*m.b66 - 2*m.b50*m.b69 - 2*m.b69 - 2*m.b50*m.b103 + 2*m.b51*m.b69 + 2*
                       m.b51*m.b72 - 4*m.b72 + 2*m.b51*m.b116 + 2*m.b52*m.b70 - 4*m.b70 - 2*m.b52*m.b114 + 2*m.b52*
                       m.b115 + 2*m.b53*m.b55 - 2*m.b55 + 2*m.b54*m.b57 - 4*m.b57 + 2*m.b54*m.b101 + 2*m.b55*m.b57 + 2*
                       m.b55*m.b92 - 2*m.b55*m.b120 - 2*m.b56*m.b59 - 2*m.b59 - 2*m.b56*m.b97 - 2*m.b56*m.b104 + 2*m.b57
                       *m.b59 + 2*m.b57*m.b96 - 2*m.b58*m.b60 + 2*m.b58 - 2*m.b58*m.b92 + 2*m.b58*m.b95 - 2*m.b58*m.b101
                        + 2*m.b59*m.b60 + 2*m.b59*m.b110 + 2*m.b60*m.b94 + 2*m.b61*m.b62 - 2*m.b61*m.b91 + 2*m.b62*m.b64
                        + 2*m.b62*m.b94 + 2*m.b63*m.b65 - 2*m.b65 - 2*m.b63*m.b93 + 2*m.b64*m.b65 + 2*m.b64*m.b93 - 2*
                       m.b66*m.b113 + 2*m.b67*m.b68 - 2*m.b67 + 2*m.b67*m.b113 - 2*m.b68*m.b100 + 2*m.b69*m.b71 + 2*
                       m.b69*m.b117 + 2*m.b70*m.b73 + 2*m.b70*m.b112 + 2*m.b70*m.b116 + 2*m.b71*m.b73 + 2*m.b71*m.b100
                        + 2*m.b72*m.b74 + 2*m.b72*m.b114 + 2*m.b72*m.b115 + 2*m.b73*m.b74 + 2*m.b74*m.b120 + 2*m.b75*
                       m.b77 - 4*m.b77 - 2*m.b75*m.b104 + 2*m.b76*m.b79 - 4*m.b79 + 2*m.b77*m.b78 + 2*m.b77*m.b79 + 2*
                       m.b77*m.b120 - 2*m.b78*m.b81 + 2*m.b79*m.b80 + 2*m.b79*m.b81 - 2*m.b80*m.b82 - 2*m.b80*m.b90 + 2*
                       m.b81*m.b82 + 2*m.b82*m.b84 - 2*m.b84 + 2*m.b83*m.b85 + 2*m.b83*m.b86 - 2*m.b83*m.b95 + 2*m.b84*
                       m.b86 - 2*m.b84*m.b93 + 2*m.b84*m.b95 + 2*m.b85*m.b102 - 2*m.b85*m.b119 + 2*m.b86*m.b119 + 2*
                       m.b87*m.b88 - 2*m.b88 + 2*m.b88*m.b119 + 2*m.b89*m.b90 - 2*m.b89*m.b91 + 2*m.b89*m.b93 - 2*m.b90*
                       m.b94 + 2*m.b91*m.b96 + 2*m.b91*m.b97 + 2*m.b92*m.b97 - 2*m.b95*m.b96 + 2*m.b98*m.b117 + 2*m.b100
                       *m.b113 + 2*m.b101*m.b104 - 2*m.b101*m.b111 - 2*m.b102*m.b109 - 2*m.b107*m.b108 - 2*m.b110*m.b111
                        - 2*m.b112*m.b113 + 2*m.b112*m.b114 - 2*m.b115*m.b120 - 2*m.b116*m.b117 - 2*m.b118*m.b119
                        + m.x121 <= 0)
