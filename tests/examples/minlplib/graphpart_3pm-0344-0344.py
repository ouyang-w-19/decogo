#  MINLP written by GAMS Convert at 04/21/18 13:52:23
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

m.obj = Objective(expr=m.b1*m.b4 + m.b1*m.b10 + m.b1*m.b13 - m.b1*m.b25 + m.b1*m.b37 - m.b1*m.b109 + m.b2*m.b5 + m.b2*
                       m.b11 + m.b2*m.b14 - m.b2*m.b26 + m.b2*m.b38 - m.b2*m.b110 + m.b3*m.b6 + m.b3*m.b12 + m.b3*m.b15
                        - m.b3*m.b27 + m.b3*m.b39 - m.b3*m.b111 - m.b4*m.b7 - m.b4*m.b16 - m.b4*m.b28 - m.b4*m.b40 - 
                       m.b4*m.b112 - m.b5*m.b8 - m.b5*m.b17 - m.b5*m.b29 - m.b5*m.b41 - m.b5*m.b113 - m.b6*m.b9 - m.b6*
                       m.b18 - m.b6*m.b30 - m.b6*m.b42 - m.b6*m.b114 - m.b7*m.b10 + m.b7*m.b19 - m.b7*m.b31 - m.b7*m.b43
                        + m.b7*m.b115 - m.b8*m.b11 + m.b8*m.b20 - m.b8*m.b32 - m.b8*m.b44 + m.b8*m.b116 - m.b9*m.b12 + 
                       m.b9*m.b21 - m.b9*m.b33 - m.b9*m.b45 + m.b9*m.b117 - m.b10*m.b22 - m.b10*m.b34 + m.b10*m.b46 + 
                       m.b10*m.b118 - m.b11*m.b23 - m.b11*m.b35 + m.b11*m.b47 + m.b11*m.b119 - m.b12*m.b24 - m.b12*m.b36
                        + m.b12*m.b48 + m.b12*m.b120 + m.b13*m.b16 + m.b13*m.b22 - m.b13*m.b25 + m.b13*m.b49 + m.b13*
                       m.b121 + m.b14*m.b17 + m.b14*m.b23 - m.b14*m.b26 + m.b14*m.b50 + m.b14*m.b122 + m.b15*m.b18 + 
                       m.b15*m.b24 - m.b15*m.b27 + m.b15*m.b51 + m.b15*m.b123 - m.b16*m.b19 + m.b16*m.b28 + m.b16*m.b52
                        + m.b16*m.b124 - m.b17*m.b20 + m.b17*m.b29 + m.b17*m.b53 + m.b17*m.b125 - m.b18*m.b21 + m.b18*
                       m.b30 + m.b18*m.b54 + m.b18*m.b126 + m.b19*m.b22 - m.b19*m.b31 - m.b19*m.b55 + m.b19*m.b127 + 
                       m.b20*m.b23 - m.b20*m.b32 - m.b20*m.b56 + m.b20*m.b128 + m.b21*m.b24 - m.b21*m.b33 - m.b21*m.b57
                        + m.b21*m.b129 + m.b22*m.b34 + m.b22*m.b58 + m.b22*m.b130 + m.b23*m.b35 + m.b23*m.b59 + m.b23*
                       m.b131 + m.b24*m.b36 + m.b24*m.b60 + m.b24*m.b132 + m.b25*m.b28 - m.b25*m.b34 + m.b25*m.b61 + 
                       m.b25*m.b133 + m.b26*m.b29 - m.b26*m.b35 + m.b26*m.b62 + m.b26*m.b134 + m.b27*m.b30 - m.b27*m.b36
                        + m.b27*m.b63 + m.b27*m.b135 - m.b28*m.b31 - m.b28*m.b64 - m.b28*m.b136 - m.b29*m.b32 - m.b29*
                       m.b65 - m.b29*m.b137 - m.b30*m.b33 - m.b30*m.b66 - m.b30*m.b138 - m.b31*m.b34 + m.b31*m.b67 - 
                       m.b31*m.b139 - m.b32*m.b35 + m.b32*m.b68 - m.b32*m.b140 - m.b33*m.b36 + m.b33*m.b69 - m.b33*
                       m.b141 - m.b34*m.b70 - m.b34*m.b142 - m.b35*m.b71 - m.b35*m.b143 - m.b36*m.b72 - m.b36*m.b144 + 
                       m.b37*m.b40 - m.b37*m.b46 - m.b37*m.b49 + m.b37*m.b61 - m.b37*m.b73 + m.b38*m.b41 - m.b38*m.b47
                        - m.b38*m.b50 + m.b38*m.b62 - m.b38*m.b74 + m.b39*m.b42 - m.b39*m.b48 - m.b39*m.b51 + m.b39*
                       m.b63 - m.b39*m.b75 + m.b40*m.b43 - m.b40*m.b52 + m.b40*m.b64 - m.b40*m.b76 + m.b41*m.b44 - m.b41
                       *m.b53 + m.b41*m.b65 - m.b41*m.b77 + m.b42*m.b45 - m.b42*m.b54 + m.b42*m.b66 - m.b42*m.b78 - 
                       m.b43*m.b46 + m.b43*m.b55 + m.b43*m.b67 - m.b43*m.b79 - m.b44*m.b47 + m.b44*m.b56 + m.b44*m.b68
                        - m.b44*m.b80 - m.b45*m.b48 + m.b45*m.b57 + m.b45*m.b69 - m.b45*m.b81 - m.b46*m.b58 + m.b46*
                       m.b70 - m.b46*m.b82 - m.b47*m.b59 + m.b47*m.b71 - m.b47*m.b83 - m.b48*m.b60 + m.b48*m.b72 - m.b48
                       *m.b84 - m.b49*m.b52 + m.b49*m.b58 + m.b49*m.b61 + m.b49*m.b85 - m.b50*m.b53 + m.b50*m.b59 + 
                       m.b50*m.b62 + m.b50*m.b86 - m.b51*m.b54 + m.b51*m.b60 + m.b51*m.b63 + m.b51*m.b87 - m.b52*m.b55
                        - m.b52*m.b64 - m.b52*m.b88 - m.b53*m.b56 - m.b53*m.b65 - m.b53*m.b89 - m.b54*m.b57 - m.b54*
                       m.b66 - m.b54*m.b90 - m.b55*m.b58 - m.b55*m.b67 + m.b55*m.b91 - m.b56*m.b59 - m.b56*m.b68 + m.b56
                       *m.b92 - m.b57*m.b60 - m.b57*m.b69 + m.b57*m.b93 - m.b58*m.b70 + m.b58*m.b94 - m.b59*m.b71 + 
                       m.b59*m.b95 - m.b60*m.b72 + m.b60*m.b96 - m.b61*m.b64 + m.b61*m.b70 - m.b61*m.b97 - m.b62*m.b65
                        + m.b62*m.b71 - m.b62*m.b98 - m.b63*m.b66 + m.b63*m.b72 - m.b63*m.b99 + m.b64*m.b67 - m.b64*
                       m.b100 + m.b65*m.b68 - m.b65*m.b101 + m.b66*m.b69 - m.b66*m.b102 - m.b67*m.b70 + m.b67*m.b103 - 
                       m.b68*m.b71 + m.b68*m.b104 - m.b69*m.b72 + m.b69*m.b105 + m.b70*m.b106 + m.b71*m.b107 + m.b72*
                       m.b108 - m.b73*m.b76 - m.b73*m.b82 + m.b73*m.b85 - m.b73*m.b97 + m.b73*m.b109 - m.b74*m.b77 - 
                       m.b74*m.b83 + m.b74*m.b86 - m.b74*m.b98 + m.b74*m.b110 - m.b75*m.b78 - m.b75*m.b84 + m.b75*m.b87
                        - m.b75*m.b99 + m.b75*m.b111 - m.b76*m.b79 + m.b76*m.b88 + m.b76*m.b100 - m.b76*m.b112 - m.b77*
                       m.b80 + m.b77*m.b89 + m.b77*m.b101 - m.b77*m.b113 - m.b78*m.b81 + m.b78*m.b90 + m.b78*m.b102 - 
                       m.b78*m.b114 + m.b79*m.b82 - m.b79*m.b91 - m.b79*m.b103 + m.b79*m.b115 + m.b80*m.b83 - m.b80*
                       m.b92 - m.b80*m.b104 + m.b80*m.b116 + m.b81*m.b84 - m.b81*m.b93 - m.b81*m.b105 + m.b81*m.b117 - 
                       m.b82*m.b94 + m.b82*m.b106 + m.b82*m.b118 - m.b83*m.b95 + m.b83*m.b107 + m.b83*m.b119 - m.b84*
                       m.b96 + m.b84*m.b108 + m.b84*m.b120 + m.b85*m.b88 - m.b85*m.b94 + m.b85*m.b97 + m.b85*m.b121 + 
                       m.b86*m.b89 - m.b86*m.b95 + m.b86*m.b98 + m.b86*m.b122 + m.b87*m.b90 - m.b87*m.b96 + m.b87*m.b99
                        + m.b87*m.b123 + m.b88*m.b91 + m.b88*m.b100 - m.b88*m.b124 + m.b89*m.b92 + m.b89*m.b101 - m.b89*
                       m.b125 + m.b90*m.b93 + m.b90*m.b102 - m.b90*m.b126 + m.b91*m.b94 - m.b91*m.b103 + m.b91*m.b127 + 
                       m.b92*m.b95 - m.b92*m.b104 + m.b92*m.b128 + m.b93*m.b96 - m.b93*m.b105 + m.b93*m.b129 - m.b94*
                       m.b106 + m.b94*m.b130 - m.b95*m.b107 + m.b95*m.b131 - m.b96*m.b108 + m.b96*m.b132 - m.b97*m.b100
                        + m.b97*m.b106 - m.b97*m.b133 - m.b98*m.b101 + m.b98*m.b107 - m.b98*m.b134 - m.b99*m.b102 + 
                       m.b99*m.b108 - m.b99*m.b135 + m.b100*m.b103 + m.b100*m.b136 + m.b101*m.b104 + m.b101*m.b137 + 
                       m.b102*m.b105 + m.b102*m.b138 - m.b103*m.b106 - m.b103*m.b139 - m.b104*m.b107 - m.b104*m.b140 - 
                       m.b105*m.b108 - m.b105*m.b141 + m.b106*m.b142 + m.b107*m.b143 + m.b108*m.b144 - m.b109*m.b112 - 
                       m.b109*m.b118 + m.b109*m.b121 - m.b109*m.b133 - m.b110*m.b113 - m.b110*m.b119 + m.b110*m.b122 - 
                       m.b110*m.b134 - m.b111*m.b114 - m.b111*m.b120 + m.b111*m.b123 - m.b111*m.b135 - m.b112*m.b115 - 
                       m.b112*m.b124 + m.b112*m.b136 - m.b113*m.b116 - m.b113*m.b125 + m.b113*m.b137 - m.b114*m.b117 - 
                       m.b114*m.b126 + m.b114*m.b138 - m.b115*m.b118 - m.b115*m.b127 - m.b115*m.b139 - m.b116*m.b119 - 
                       m.b116*m.b128 - m.b116*m.b140 - m.b117*m.b120 - m.b117*m.b129 - m.b117*m.b141 + m.b118*m.b130 + 
                       m.b118*m.b142 + m.b119*m.b131 + m.b119*m.b143 + m.b120*m.b132 + m.b120*m.b144 + m.b121*m.b124 - 
                       m.b121*m.b130 - m.b121*m.b133 + m.b122*m.b125 - m.b122*m.b131 - m.b122*m.b134 + m.b123*m.b126 - 
                       m.b123*m.b132 - m.b123*m.b135 + m.b124*m.b127 + m.b124*m.b136 + m.b125*m.b128 + m.b125*m.b137 + 
                       m.b126*m.b129 + m.b126*m.b138 + m.b127*m.b130 - m.b127*m.b139 + m.b128*m.b131 - m.b128*m.b140 + 
                       m.b129*m.b132 - m.b129*m.b141 + m.b130*m.b142 + m.b131*m.b143 + m.b132*m.b144 + m.b133*m.b136 + 
                       m.b133*m.b142 + m.b134*m.b137 + m.b134*m.b143 + m.b135*m.b138 + m.b135*m.b144 + m.b136*m.b139 + 
                       m.b137*m.b140 + m.b138*m.b141 - m.b139*m.b142 - m.b140*m.b143 - m.b141*m.b144, sense=minimize)

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
