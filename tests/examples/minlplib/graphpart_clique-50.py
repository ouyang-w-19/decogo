#  MINLP written by GAMS Convert at 04/21/18 13:52:23
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         51       51        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        151        1      150        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        301      151      150        0
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
m.b145 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b146 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b147 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b148 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b149 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b150 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=m.b1*m.b4 + 2*m.b1*m.b7 + 3*m.b1*m.b10 + 4*m.b1*m.b13 + 5*m.b1*m.b16 + 6*m.b1*m.b19 + 7*m.b1*
                       m.b22 + 8*m.b1*m.b25 + 9*m.b1*m.b28 + 10*m.b1*m.b31 + 11*m.b1*m.b34 + 12*m.b1*m.b37 + 13*m.b1*
                       m.b40 + 14*m.b1*m.b43 + 15*m.b1*m.b46 + 16*m.b1*m.b49 + 17*m.b1*m.b52 + 18*m.b1*m.b55 + 19*m.b1*
                       m.b58 + 20*m.b1*m.b61 + 21*m.b1*m.b64 + 22*m.b1*m.b67 + 23*m.b1*m.b70 + 24*m.b1*m.b73 + 25*m.b1*
                       m.b76 + 26*m.b1*m.b79 + 27*m.b1*m.b82 + 28*m.b1*m.b85 + 29*m.b1*m.b88 + 30*m.b1*m.b91 + 31*m.b1*
                       m.b94 + 32*m.b1*m.b97 + 33*m.b1*m.b100 + 34*m.b1*m.b103 + 35*m.b1*m.b106 + 36*m.b1*m.b109 + 37*
                       m.b1*m.b112 + 38*m.b1*m.b115 + 39*m.b1*m.b118 + 40*m.b1*m.b121 + 41*m.b1*m.b124 + 42*m.b1*m.b127
                        + 43*m.b1*m.b130 + 44*m.b1*m.b133 + 45*m.b1*m.b136 + 46*m.b1*m.b139 + 47*m.b1*m.b142 + 48*m.b1*
                       m.b145 + 49*m.b1*m.b148 + m.b2*m.b5 + 2*m.b2*m.b8 + 3*m.b2*m.b11 + 4*m.b2*m.b14 + 5*m.b2*m.b17 + 
                       6*m.b2*m.b20 + 7*m.b2*m.b23 + 8*m.b2*m.b26 + 9*m.b2*m.b29 + 10*m.b2*m.b32 + 11*m.b2*m.b35 + 12*
                       m.b2*m.b38 + 13*m.b2*m.b41 + 14*m.b2*m.b44 + 15*m.b2*m.b47 + 16*m.b2*m.b50 + 17*m.b2*m.b53 + 18*
                       m.b2*m.b56 + 19*m.b2*m.b59 + 20*m.b2*m.b62 + 21*m.b2*m.b65 + 22*m.b2*m.b68 + 23*m.b2*m.b71 + 24*
                       m.b2*m.b74 + 25*m.b2*m.b77 + 26*m.b2*m.b80 + 27*m.b2*m.b83 + 28*m.b2*m.b86 + 29*m.b2*m.b89 + 30*
                       m.b2*m.b92 + 31*m.b2*m.b95 + 32*m.b2*m.b98 + 33*m.b2*m.b101 + 34*m.b2*m.b104 + 35*m.b2*m.b107 + 
                       36*m.b2*m.b110 + 37*m.b2*m.b113 + 38*m.b2*m.b116 + 39*m.b2*m.b119 + 40*m.b2*m.b122 + 41*m.b2*
                       m.b125 + 42*m.b2*m.b128 + 43*m.b2*m.b131 + 44*m.b2*m.b134 + 45*m.b2*m.b137 + 46*m.b2*m.b140 + 47*
                       m.b2*m.b143 + 48*m.b2*m.b146 + 49*m.b2*m.b149 + m.b3*m.b6 + 2*m.b3*m.b9 + 3*m.b3*m.b12 + 4*m.b3*
                       m.b15 + 5*m.b3*m.b18 + 6*m.b3*m.b21 + 7*m.b3*m.b24 + 8*m.b3*m.b27 + 9*m.b3*m.b30 + 10*m.b3*m.b33
                        + 11*m.b3*m.b36 + 12*m.b3*m.b39 + 13*m.b3*m.b42 + 14*m.b3*m.b45 + 15*m.b3*m.b48 + 16*m.b3*m.b51
                        + 17*m.b3*m.b54 + 18*m.b3*m.b57 + 19*m.b3*m.b60 + 20*m.b3*m.b63 + 21*m.b3*m.b66 + 22*m.b3*m.b69
                        + 23*m.b3*m.b72 + 24*m.b3*m.b75 + 25*m.b3*m.b78 + 26*m.b3*m.b81 + 27*m.b3*m.b84 + 28*m.b3*m.b87
                        + 29*m.b3*m.b90 + 30*m.b3*m.b93 + 31*m.b3*m.b96 + 32*m.b3*m.b99 + 33*m.b3*m.b102 + 34*m.b3*
                       m.b105 + 35*m.b3*m.b108 + 36*m.b3*m.b111 + 37*m.b3*m.b114 + 38*m.b3*m.b117 + 39*m.b3*m.b120 + 40*
                       m.b3*m.b123 + 41*m.b3*m.b126 + 42*m.b3*m.b129 + 43*m.b3*m.b132 + 44*m.b3*m.b135 + 45*m.b3*m.b138
                        + 46*m.b3*m.b141 + 47*m.b3*m.b144 + 48*m.b3*m.b147 + 49*m.b3*m.b150 + m.b4*m.b7 + 2*m.b4*m.b10
                        + 3*m.b4*m.b13 + 4*m.b4*m.b16 + 5*m.b4*m.b19 + 6*m.b4*m.b22 + 7*m.b4*m.b25 + 8*m.b4*m.b28 + 9*
                       m.b4*m.b31 + 10*m.b4*m.b34 + 11*m.b4*m.b37 + 12*m.b4*m.b40 + 13*m.b4*m.b43 + 14*m.b4*m.b46 + 15*
                       m.b4*m.b49 + 16*m.b4*m.b52 + 17*m.b4*m.b55 + 18*m.b4*m.b58 + 19*m.b4*m.b61 + 20*m.b4*m.b64 + 21*
                       m.b4*m.b67 + 22*m.b4*m.b70 + 23*m.b4*m.b73 + 24*m.b4*m.b76 + 25*m.b4*m.b79 + 26*m.b4*m.b82 + 27*
                       m.b4*m.b85 + 28*m.b4*m.b88 + 29*m.b4*m.b91 + 30*m.b4*m.b94 + 31*m.b4*m.b97 + 32*m.b4*m.b100 + 33*
                       m.b4*m.b103 + 34*m.b4*m.b106 + 35*m.b4*m.b109 + 36*m.b4*m.b112 + 37*m.b4*m.b115 + 38*m.b4*m.b118
                        + 39*m.b4*m.b121 + 40*m.b4*m.b124 + 41*m.b4*m.b127 + 42*m.b4*m.b130 + 43*m.b4*m.b133 + 44*m.b4*
                       m.b136 + 45*m.b4*m.b139 + 46*m.b4*m.b142 + 47*m.b4*m.b145 + 48*m.b4*m.b148 + m.b5*m.b8 + 2*m.b5*
                       m.b11 + 3*m.b5*m.b14 + 4*m.b5*m.b17 + 5*m.b5*m.b20 + 6*m.b5*m.b23 + 7*m.b5*m.b26 + 8*m.b5*m.b29
                        + 9*m.b5*m.b32 + 10*m.b5*m.b35 + 11*m.b5*m.b38 + 12*m.b5*m.b41 + 13*m.b5*m.b44 + 14*m.b5*m.b47
                        + 15*m.b5*m.b50 + 16*m.b5*m.b53 + 17*m.b5*m.b56 + 18*m.b5*m.b59 + 19*m.b5*m.b62 + 20*m.b5*m.b65
                        + 21*m.b5*m.b68 + 22*m.b5*m.b71 + 23*m.b5*m.b74 + 24*m.b5*m.b77 + 25*m.b5*m.b80 + 26*m.b5*m.b83
                        + 27*m.b5*m.b86 + 28*m.b5*m.b89 + 29*m.b5*m.b92 + 30*m.b5*m.b95 + 31*m.b5*m.b98 + 32*m.b5*m.b101
                        + 33*m.b5*m.b104 + 34*m.b5*m.b107 + 35*m.b5*m.b110 + 36*m.b5*m.b113 + 37*m.b5*m.b116 + 38*m.b5*
                       m.b119 + 39*m.b5*m.b122 + 40*m.b5*m.b125 + 41*m.b5*m.b128 + 42*m.b5*m.b131 + 43*m.b5*m.b134 + 44*
                       m.b5*m.b137 + 45*m.b5*m.b140 + 46*m.b5*m.b143 + 47*m.b5*m.b146 + 48*m.b5*m.b149 + m.b6*m.b9 + 2*
                       m.b6*m.b12 + 3*m.b6*m.b15 + 4*m.b6*m.b18 + 5*m.b6*m.b21 + 6*m.b6*m.b24 + 7*m.b6*m.b27 + 8*m.b6*
                       m.b30 + 9*m.b6*m.b33 + 10*m.b6*m.b36 + 11*m.b6*m.b39 + 12*m.b6*m.b42 + 13*m.b6*m.b45 + 14*m.b6*
                       m.b48 + 15*m.b6*m.b51 + 16*m.b6*m.b54 + 17*m.b6*m.b57 + 18*m.b6*m.b60 + 19*m.b6*m.b63 + 20*m.b6*
                       m.b66 + 21*m.b6*m.b69 + 22*m.b6*m.b72 + 23*m.b6*m.b75 + 24*m.b6*m.b78 + 25*m.b6*m.b81 + 26*m.b6*
                       m.b84 + 27*m.b6*m.b87 + 28*m.b6*m.b90 + 29*m.b6*m.b93 + 30*m.b6*m.b96 + 31*m.b6*m.b99 + 32*m.b6*
                       m.b102 + 33*m.b6*m.b105 + 34*m.b6*m.b108 + 35*m.b6*m.b111 + 36*m.b6*m.b114 + 37*m.b6*m.b117 + 38*
                       m.b6*m.b120 + 39*m.b6*m.b123 + 40*m.b6*m.b126 + 41*m.b6*m.b129 + 42*m.b6*m.b132 + 43*m.b6*m.b135
                        + 44*m.b6*m.b138 + 45*m.b6*m.b141 + 46*m.b6*m.b144 + 47*m.b6*m.b147 + 48*m.b6*m.b150 + m.b7*
                       m.b10 + 2*m.b7*m.b13 + 3*m.b7*m.b16 + 4*m.b7*m.b19 + 5*m.b7*m.b22 + 6*m.b7*m.b25 + 7*m.b7*m.b28
                        + 8*m.b7*m.b31 + 9*m.b7*m.b34 + 10*m.b7*m.b37 + 11*m.b7*m.b40 + 12*m.b7*m.b43 + 13*m.b7*m.b46 + 
                       14*m.b7*m.b49 + 15*m.b7*m.b52 + 16*m.b7*m.b55 + 17*m.b7*m.b58 + 18*m.b7*m.b61 + 19*m.b7*m.b64 + 
                       20*m.b7*m.b67 + 21*m.b7*m.b70 + 22*m.b7*m.b73 + 23*m.b7*m.b76 + 24*m.b7*m.b79 + 25*m.b7*m.b82 + 
                       26*m.b7*m.b85 + 27*m.b7*m.b88 + 28*m.b7*m.b91 + 29*m.b7*m.b94 + 30*m.b7*m.b97 + 31*m.b7*m.b100 + 
                       32*m.b7*m.b103 + 33*m.b7*m.b106 + 34*m.b7*m.b109 + 35*m.b7*m.b112 + 36*m.b7*m.b115 + 37*m.b7*
                       m.b118 + 38*m.b7*m.b121 + 39*m.b7*m.b124 + 40*m.b7*m.b127 + 41*m.b7*m.b130 + 42*m.b7*m.b133 + 43*
                       m.b7*m.b136 + 44*m.b7*m.b139 + 45*m.b7*m.b142 + 46*m.b7*m.b145 + 47*m.b7*m.b148 + m.b8*m.b11 + 2*
                       m.b8*m.b14 + 3*m.b8*m.b17 + 4*m.b8*m.b20 + 5*m.b8*m.b23 + 6*m.b8*m.b26 + 7*m.b8*m.b29 + 8*m.b8*
                       m.b32 + 9*m.b8*m.b35 + 10*m.b8*m.b38 + 11*m.b8*m.b41 + 12*m.b8*m.b44 + 13*m.b8*m.b47 + 14*m.b8*
                       m.b50 + 15*m.b8*m.b53 + 16*m.b8*m.b56 + 17*m.b8*m.b59 + 18*m.b8*m.b62 + 19*m.b8*m.b65 + 20*m.b8*
                       m.b68 + 21*m.b8*m.b71 + 22*m.b8*m.b74 + 23*m.b8*m.b77 + 24*m.b8*m.b80 + 25*m.b8*m.b83 + 26*m.b8*
                       m.b86 + 27*m.b8*m.b89 + 28*m.b8*m.b92 + 29*m.b8*m.b95 + 30*m.b8*m.b98 + 31*m.b8*m.b101 + 32*m.b8*
                       m.b104 + 33*m.b8*m.b107 + 34*m.b8*m.b110 + 35*m.b8*m.b113 + 36*m.b8*m.b116 + 37*m.b8*m.b119 + 38*
                       m.b8*m.b122 + 39*m.b8*m.b125 + 40*m.b8*m.b128 + 41*m.b8*m.b131 + 42*m.b8*m.b134 + 43*m.b8*m.b137
                        + 44*m.b8*m.b140 + 45*m.b8*m.b143 + 46*m.b8*m.b146 + 47*m.b8*m.b149 + m.b9*m.b12 + 2*m.b9*m.b15
                        + 3*m.b9*m.b18 + 4*m.b9*m.b21 + 5*m.b9*m.b24 + 6*m.b9*m.b27 + 7*m.b9*m.b30 + 8*m.b9*m.b33 + 9*
                       m.b9*m.b36 + 10*m.b9*m.b39 + 11*m.b9*m.b42 + 12*m.b9*m.b45 + 13*m.b9*m.b48 + 14*m.b9*m.b51 + 15*
                       m.b9*m.b54 + 16*m.b9*m.b57 + 17*m.b9*m.b60 + 18*m.b9*m.b63 + 19*m.b9*m.b66 + 20*m.b9*m.b69 + 21*
                       m.b9*m.b72 + 22*m.b9*m.b75 + 23*m.b9*m.b78 + 24*m.b9*m.b81 + 25*m.b9*m.b84 + 26*m.b9*m.b87 + 27*
                       m.b9*m.b90 + 28*m.b9*m.b93 + 29*m.b9*m.b96 + 30*m.b9*m.b99 + 31*m.b9*m.b102 + 32*m.b9*m.b105 + 33
                       *m.b9*m.b108 + 34*m.b9*m.b111 + 35*m.b9*m.b114 + 36*m.b9*m.b117 + 37*m.b9*m.b120 + 38*m.b9*m.b123
                        + 39*m.b9*m.b126 + 40*m.b9*m.b129 + 41*m.b9*m.b132 + 42*m.b9*m.b135 + 43*m.b9*m.b138 + 44*m.b9*
                       m.b141 + 45*m.b9*m.b144 + 46*m.b9*m.b147 + 47*m.b9*m.b150 + m.b10*m.b13 + 2*m.b10*m.b16 + 3*m.b10
                       *m.b19 + 4*m.b10*m.b22 + 5*m.b10*m.b25 + 6*m.b10*m.b28 + 7*m.b10*m.b31 + 8*m.b10*m.b34 + 9*m.b10*
                       m.b37 + 10*m.b10*m.b40 + 11*m.b10*m.b43 + 12*m.b10*m.b46 + 13*m.b10*m.b49 + 14*m.b10*m.b52 + 15*
                       m.b10*m.b55 + 16*m.b10*m.b58 + 17*m.b10*m.b61 + 18*m.b10*m.b64 + 19*m.b10*m.b67 + 20*m.b10*m.b70
                        + 21*m.b10*m.b73 + 22*m.b10*m.b76 + 23*m.b10*m.b79 + 24*m.b10*m.b82 + 25*m.b10*m.b85 + 26*m.b10*
                       m.b88 + 27*m.b10*m.b91 + 28*m.b10*m.b94 + 29*m.b10*m.b97 + 30*m.b10*m.b100 + 31*m.b10*m.b103 + 32
                       *m.b10*m.b106 + 33*m.b10*m.b109 + 34*m.b10*m.b112 + 35*m.b10*m.b115 + 36*m.b10*m.b118 + 37*m.b10*
                       m.b121 + 38*m.b10*m.b124 + 39*m.b10*m.b127 + 40*m.b10*m.b130 + 41*m.b10*m.b133 + 42*m.b10*m.b136
                        + 43*m.b10*m.b139 + 44*m.b10*m.b142 + 45*m.b10*m.b145 + 46*m.b10*m.b148 + m.b11*m.b14 + 2*m.b11*
                       m.b17 + 3*m.b11*m.b20 + 4*m.b11*m.b23 + 5*m.b11*m.b26 + 6*m.b11*m.b29 + 7*m.b11*m.b32 + 8*m.b11*
                       m.b35 + 9*m.b11*m.b38 + 10*m.b11*m.b41 + 11*m.b11*m.b44 + 12*m.b11*m.b47 + 13*m.b11*m.b50 + 14*
                       m.b11*m.b53 + 15*m.b11*m.b56 + 16*m.b11*m.b59 + 17*m.b11*m.b62 + 18*m.b11*m.b65 + 19*m.b11*m.b68
                        + 20*m.b11*m.b71 + 21*m.b11*m.b74 + 22*m.b11*m.b77 + 23*m.b11*m.b80 + 24*m.b11*m.b83 + 25*m.b11*
                       m.b86 + 26*m.b11*m.b89 + 27*m.b11*m.b92 + 28*m.b11*m.b95 + 29*m.b11*m.b98 + 30*m.b11*m.b101 + 31*
                       m.b11*m.b104 + 32*m.b11*m.b107 + 33*m.b11*m.b110 + 34*m.b11*m.b113 + 35*m.b11*m.b116 + 36*m.b11*
                       m.b119 + 37*m.b11*m.b122 + 38*m.b11*m.b125 + 39*m.b11*m.b128 + 40*m.b11*m.b131 + 41*m.b11*m.b134
                        + 42*m.b11*m.b137 + 43*m.b11*m.b140 + 44*m.b11*m.b143 + 45*m.b11*m.b146 + 46*m.b11*m.b149 + 
                       m.b12*m.b15 + 2*m.b12*m.b18 + 3*m.b12*m.b21 + 4*m.b12*m.b24 + 5*m.b12*m.b27 + 6*m.b12*m.b30 + 7*
                       m.b12*m.b33 + 8*m.b12*m.b36 + 9*m.b12*m.b39 + 10*m.b12*m.b42 + 11*m.b12*m.b45 + 12*m.b12*m.b48 + 
                       13*m.b12*m.b51 + 14*m.b12*m.b54 + 15*m.b12*m.b57 + 16*m.b12*m.b60 + 17*m.b12*m.b63 + 18*m.b12*
                       m.b66 + 19*m.b12*m.b69 + 20*m.b12*m.b72 + 21*m.b12*m.b75 + 22*m.b12*m.b78 + 23*m.b12*m.b81 + 24*
                       m.b12*m.b84 + 25*m.b12*m.b87 + 26*m.b12*m.b90 + 27*m.b12*m.b93 + 28*m.b12*m.b96 + 29*m.b12*m.b99
                        + 30*m.b12*m.b102 + 31*m.b12*m.b105 + 32*m.b12*m.b108 + 33*m.b12*m.b111 + 34*m.b12*m.b114 + 35*
                       m.b12*m.b117 + 36*m.b12*m.b120 + 37*m.b12*m.b123 + 38*m.b12*m.b126 + 39*m.b12*m.b129 + 40*m.b12*
                       m.b132 + 41*m.b12*m.b135 + 42*m.b12*m.b138 + 43*m.b12*m.b141 + 44*m.b12*m.b144 + 45*m.b12*m.b147
                        + 46*m.b12*m.b150 + m.b13*m.b16 + 2*m.b13*m.b19 + 3*m.b13*m.b22 + 4*m.b13*m.b25 + 5*m.b13*m.b28
                        + 6*m.b13*m.b31 + 7*m.b13*m.b34 + 8*m.b13*m.b37 + 9*m.b13*m.b40 + 10*m.b13*m.b43 + 11*m.b13*
                       m.b46 + 12*m.b13*m.b49 + 13*m.b13*m.b52 + 14*m.b13*m.b55 + 15*m.b13*m.b58 + 16*m.b13*m.b61 + 17*
                       m.b13*m.b64 + 18*m.b13*m.b67 + 19*m.b13*m.b70 + 20*m.b13*m.b73 + 21*m.b13*m.b76 + 22*m.b13*m.b79
                        + 23*m.b13*m.b82 + 24*m.b13*m.b85 + 25*m.b13*m.b88 + 26*m.b13*m.b91 + 27*m.b13*m.b94 + 28*m.b13*
                       m.b97 + 29*m.b13*m.b100 + 30*m.b13*m.b103 + 31*m.b13*m.b106 + 32*m.b13*m.b109 + 33*m.b13*m.b112
                        + 34*m.b13*m.b115 + 35*m.b13*m.b118 + 36*m.b13*m.b121 + 37*m.b13*m.b124 + 38*m.b13*m.b127 + 39*
                       m.b13*m.b130 + 40*m.b13*m.b133 + 41*m.b13*m.b136 + 42*m.b13*m.b139 + 43*m.b13*m.b142 + 44*m.b13*
                       m.b145 + 45*m.b13*m.b148 + m.b14*m.b17 + 2*m.b14*m.b20 + 3*m.b14*m.b23 + 4*m.b14*m.b26 + 5*m.b14*
                       m.b29 + 6*m.b14*m.b32 + 7*m.b14*m.b35 + 8*m.b14*m.b38 + 9*m.b14*m.b41 + 10*m.b14*m.b44 + 11*m.b14
                       *m.b47 + 12*m.b14*m.b50 + 13*m.b14*m.b53 + 14*m.b14*m.b56 + 15*m.b14*m.b59 + 16*m.b14*m.b62 + 17*
                       m.b14*m.b65 + 18*m.b14*m.b68 + 19*m.b14*m.b71 + 20*m.b14*m.b74 + 21*m.b14*m.b77 + 22*m.b14*m.b80
                        + 23*m.b14*m.b83 + 24*m.b14*m.b86 + 25*m.b14*m.b89 + 26*m.b14*m.b92 + 27*m.b14*m.b95 + 28*m.b14*
                       m.b98 + 29*m.b14*m.b101 + 30*m.b14*m.b104 + 31*m.b14*m.b107 + 32*m.b14*m.b110 + 33*m.b14*m.b113
                        + 34*m.b14*m.b116 + 35*m.b14*m.b119 + 36*m.b14*m.b122 + 37*m.b14*m.b125 + 38*m.b14*m.b128 + 39*
                       m.b14*m.b131 + 40*m.b14*m.b134 + 41*m.b14*m.b137 + 42*m.b14*m.b140 + 43*m.b14*m.b143 + 44*m.b14*
                       m.b146 + 45*m.b14*m.b149 + m.b15*m.b18 + 2*m.b15*m.b21 + 3*m.b15*m.b24 + 4*m.b15*m.b27 + 5*m.b15*
                       m.b30 + 6*m.b15*m.b33 + 7*m.b15*m.b36 + 8*m.b15*m.b39 + 9*m.b15*m.b42 + 10*m.b15*m.b45 + 11*m.b15
                       *m.b48 + 12*m.b15*m.b51 + 13*m.b15*m.b54 + 14*m.b15*m.b57 + 15*m.b15*m.b60 + 16*m.b15*m.b63 + 17*
                       m.b15*m.b66 + 18*m.b15*m.b69 + 19*m.b15*m.b72 + 20*m.b15*m.b75 + 21*m.b15*m.b78 + 22*m.b15*m.b81
                        + 23*m.b15*m.b84 + 24*m.b15*m.b87 + 25*m.b15*m.b90 + 26*m.b15*m.b93 + 27*m.b15*m.b96 + 28*m.b15*
                       m.b99 + 29*m.b15*m.b102 + 30*m.b15*m.b105 + 31*m.b15*m.b108 + 32*m.b15*m.b111 + 33*m.b15*m.b114
                        + 34*m.b15*m.b117 + 35*m.b15*m.b120 + 36*m.b15*m.b123 + 37*m.b15*m.b126 + 38*m.b15*m.b129 + 39*
                       m.b15*m.b132 + 40*m.b15*m.b135 + 41*m.b15*m.b138 + 42*m.b15*m.b141 + 43*m.b15*m.b144 + 44*m.b15*
                       m.b147 + 45*m.b15*m.b150 + m.b16*m.b19 + 2*m.b16*m.b22 + 3*m.b16*m.b25 + 4*m.b16*m.b28 + 5*m.b16*
                       m.b31 + 6*m.b16*m.b34 + 7*m.b16*m.b37 + 8*m.b16*m.b40 + 9*m.b16*m.b43 + 10*m.b16*m.b46 + 11*m.b16
                       *m.b49 + 12*m.b16*m.b52 + 13*m.b16*m.b55 + 14*m.b16*m.b58 + 15*m.b16*m.b61 + 16*m.b16*m.b64 + 17*
                       m.b16*m.b67 + 18*m.b16*m.b70 + 19*m.b16*m.b73 + 20*m.b16*m.b76 + 21*m.b16*m.b79 + 22*m.b16*m.b82
                        + 23*m.b16*m.b85 + 24*m.b16*m.b88 + 25*m.b16*m.b91 + 26*m.b16*m.b94 + 27*m.b16*m.b97 + 28*m.b16*
                       m.b100 + 29*m.b16*m.b103 + 30*m.b16*m.b106 + 31*m.b16*m.b109 + 32*m.b16*m.b112 + 33*m.b16*m.b115
                        + 34*m.b16*m.b118 + 35*m.b16*m.b121 + 36*m.b16*m.b124 + 37*m.b16*m.b127 + 38*m.b16*m.b130 + 39*
                       m.b16*m.b133 + 40*m.b16*m.b136 + 41*m.b16*m.b139 + 42*m.b16*m.b142 + 43*m.b16*m.b145 + 44*m.b16*
                       m.b148 + m.b17*m.b20 + 2*m.b17*m.b23 + 3*m.b17*m.b26 + 4*m.b17*m.b29 + 5*m.b17*m.b32 + 6*m.b17*
                       m.b35 + 7*m.b17*m.b38 + 8*m.b17*m.b41 + 9*m.b17*m.b44 + 10*m.b17*m.b47 + 11*m.b17*m.b50 + 12*
                       m.b17*m.b53 + 13*m.b17*m.b56 + 14*m.b17*m.b59 + 15*m.b17*m.b62 + 16*m.b17*m.b65 + 17*m.b17*m.b68
                        + 18*m.b17*m.b71 + 19*m.b17*m.b74 + 20*m.b17*m.b77 + 21*m.b17*m.b80 + 22*m.b17*m.b83 + 23*m.b17*
                       m.b86 + 24*m.b17*m.b89 + 25*m.b17*m.b92 + 26*m.b17*m.b95 + 27*m.b17*m.b98 + 28*m.b17*m.b101 + 29*
                       m.b17*m.b104 + 30*m.b17*m.b107 + 31*m.b17*m.b110 + 32*m.b17*m.b113 + 33*m.b17*m.b116 + 34*m.b17*
                       m.b119 + 35*m.b17*m.b122 + 36*m.b17*m.b125 + 37*m.b17*m.b128 + 38*m.b17*m.b131 + 39*m.b17*m.b134
                        + 40*m.b17*m.b137 + 41*m.b17*m.b140 + 42*m.b17*m.b143 + 43*m.b17*m.b146 + 44*m.b17*m.b149 + 
                       m.b18*m.b21 + 2*m.b18*m.b24 + 3*m.b18*m.b27 + 4*m.b18*m.b30 + 5*m.b18*m.b33 + 6*m.b18*m.b36 + 7*
                       m.b18*m.b39 + 8*m.b18*m.b42 + 9*m.b18*m.b45 + 10*m.b18*m.b48 + 11*m.b18*m.b51 + 12*m.b18*m.b54 + 
                       13*m.b18*m.b57 + 14*m.b18*m.b60 + 15*m.b18*m.b63 + 16*m.b18*m.b66 + 17*m.b18*m.b69 + 18*m.b18*
                       m.b72 + 19*m.b18*m.b75 + 20*m.b18*m.b78 + 21*m.b18*m.b81 + 22*m.b18*m.b84 + 23*m.b18*m.b87 + 24*
                       m.b18*m.b90 + 25*m.b18*m.b93 + 26*m.b18*m.b96 + 27*m.b18*m.b99 + 28*m.b18*m.b102 + 29*m.b18*
                       m.b105 + 30*m.b18*m.b108 + 31*m.b18*m.b111 + 32*m.b18*m.b114 + 33*m.b18*m.b117 + 34*m.b18*m.b120
                        + 35*m.b18*m.b123 + 36*m.b18*m.b126 + 37*m.b18*m.b129 + 38*m.b18*m.b132 + 39*m.b18*m.b135 + 40*
                       m.b18*m.b138 + 41*m.b18*m.b141 + 42*m.b18*m.b144 + 43*m.b18*m.b147 + 44*m.b18*m.b150 + m.b19*
                       m.b22 + 2*m.b19*m.b25 + 3*m.b19*m.b28 + 4*m.b19*m.b31 + 5*m.b19*m.b34 + 6*m.b19*m.b37 + 7*m.b19*
                       m.b40 + 8*m.b19*m.b43 + 9*m.b19*m.b46 + 10*m.b19*m.b49 + 11*m.b19*m.b52 + 12*m.b19*m.b55 + 13*
                       m.b19*m.b58 + 14*m.b19*m.b61 + 15*m.b19*m.b64 + 16*m.b19*m.b67 + 17*m.b19*m.b70 + 18*m.b19*m.b73
                        + 19*m.b19*m.b76 + 20*m.b19*m.b79 + 21*m.b19*m.b82 + 22*m.b19*m.b85 + 23*m.b19*m.b88 + 24*m.b19*
                       m.b91 + 25*m.b19*m.b94 + 26*m.b19*m.b97 + 27*m.b19*m.b100 + 28*m.b19*m.b103 + 29*m.b19*m.b106 + 
                       30*m.b19*m.b109 + 31*m.b19*m.b112 + 32*m.b19*m.b115 + 33*m.b19*m.b118 + 34*m.b19*m.b121 + 35*
                       m.b19*m.b124 + 36*m.b19*m.b127 + 37*m.b19*m.b130 + 38*m.b19*m.b133 + 39*m.b19*m.b136 + 40*m.b19*
                       m.b139 + 41*m.b19*m.b142 + 42*m.b19*m.b145 + 43*m.b19*m.b148 + m.b20*m.b23 + 2*m.b20*m.b26 + 3*
                       m.b20*m.b29 + 4*m.b20*m.b32 + 5*m.b20*m.b35 + 6*m.b20*m.b38 + 7*m.b20*m.b41 + 8*m.b20*m.b44 + 9*
                       m.b20*m.b47 + 10*m.b20*m.b50 + 11*m.b20*m.b53 + 12*m.b20*m.b56 + 13*m.b20*m.b59 + 14*m.b20*m.b62
                        + 15*m.b20*m.b65 + 16*m.b20*m.b68 + 17*m.b20*m.b71 + 18*m.b20*m.b74 + 19*m.b20*m.b77 + 20*m.b20*
                       m.b80 + 21*m.b20*m.b83 + 22*m.b20*m.b86 + 23*m.b20*m.b89 + 24*m.b20*m.b92 + 25*m.b20*m.b95 + 26*
                       m.b20*m.b98 + 27*m.b20*m.b101 + 28*m.b20*m.b104 + 29*m.b20*m.b107 + 30*m.b20*m.b110 + 31*m.b20*
                       m.b113 + 32*m.b20*m.b116 + 33*m.b20*m.b119 + 34*m.b20*m.b122 + 35*m.b20*m.b125 + 36*m.b20*m.b128
                        + 37*m.b20*m.b131 + 38*m.b20*m.b134 + 39*m.b20*m.b137 + 40*m.b20*m.b140 + 41*m.b20*m.b143 + 42*
                       m.b20*m.b146 + 43*m.b20*m.b149 + m.b21*m.b24 + 2*m.b21*m.b27 + 3*m.b21*m.b30 + 4*m.b21*m.b33 + 5*
                       m.b21*m.b36 + 6*m.b21*m.b39 + 7*m.b21*m.b42 + 8*m.b21*m.b45 + 9*m.b21*m.b48 + 10*m.b21*m.b51 + 11
                       *m.b21*m.b54 + 12*m.b21*m.b57 + 13*m.b21*m.b60 + 14*m.b21*m.b63 + 15*m.b21*m.b66 + 16*m.b21*m.b69
                        + 17*m.b21*m.b72 + 18*m.b21*m.b75 + 19*m.b21*m.b78 + 20*m.b21*m.b81 + 21*m.b21*m.b84 + 22*m.b21*
                       m.b87 + 23*m.b21*m.b90 + 24*m.b21*m.b93 + 25*m.b21*m.b96 + 26*m.b21*m.b99 + 27*m.b21*m.b102 + 28*
                       m.b21*m.b105 + 29*m.b21*m.b108 + 30*m.b21*m.b111 + 31*m.b21*m.b114 + 32*m.b21*m.b117 + 33*m.b21*
                       m.b120 + 34*m.b21*m.b123 + 35*m.b21*m.b126 + 36*m.b21*m.b129 + 37*m.b21*m.b132 + 38*m.b21*m.b135
                        + 39*m.b21*m.b138 + 40*m.b21*m.b141 + 41*m.b21*m.b144 + 42*m.b21*m.b147 + 43*m.b21*m.b150 + 
                       m.b22*m.b25 + 2*m.b22*m.b28 + 3*m.b22*m.b31 + 4*m.b22*m.b34 + 5*m.b22*m.b37 + 6*m.b22*m.b40 + 7*
                       m.b22*m.b43 + 8*m.b22*m.b46 + 9*m.b22*m.b49 + 10*m.b22*m.b52 + 11*m.b22*m.b55 + 12*m.b22*m.b58 + 
                       13*m.b22*m.b61 + 14*m.b22*m.b64 + 15*m.b22*m.b67 + 16*m.b22*m.b70 + 17*m.b22*m.b73 + 18*m.b22*
                       m.b76 + 19*m.b22*m.b79 + 20*m.b22*m.b82 + 21*m.b22*m.b85 + 22*m.b22*m.b88 + 23*m.b22*m.b91 + 24*
                       m.b22*m.b94 + 25*m.b22*m.b97 + 26*m.b22*m.b100 + 27*m.b22*m.b103 + 28*m.b22*m.b106 + 29*m.b22*
                       m.b109 + 30*m.b22*m.b112 + 31*m.b22*m.b115 + 32*m.b22*m.b118 + 33*m.b22*m.b121 + 34*m.b22*m.b124
                        + 35*m.b22*m.b127 + 36*m.b22*m.b130 + 37*m.b22*m.b133 + 38*m.b22*m.b136 + 39*m.b22*m.b139 + 40*
                       m.b22*m.b142 + 41*m.b22*m.b145 + 42*m.b22*m.b148 + m.b23*m.b26 + 2*m.b23*m.b29 + 3*m.b23*m.b32 + 
                       4*m.b23*m.b35 + 5*m.b23*m.b38 + 6*m.b23*m.b41 + 7*m.b23*m.b44 + 8*m.b23*m.b47 + 9*m.b23*m.b50 + 
                       10*m.b23*m.b53 + 11*m.b23*m.b56 + 12*m.b23*m.b59 + 13*m.b23*m.b62 + 14*m.b23*m.b65 + 15*m.b23*
                       m.b68 + 16*m.b23*m.b71 + 17*m.b23*m.b74 + 18*m.b23*m.b77 + 19*m.b23*m.b80 + 20*m.b23*m.b83 + 21*
                       m.b23*m.b86 + 22*m.b23*m.b89 + 23*m.b23*m.b92 + 24*m.b23*m.b95 + 25*m.b23*m.b98 + 26*m.b23*m.b101
                        + 27*m.b23*m.b104 + 28*m.b23*m.b107 + 29*m.b23*m.b110 + 30*m.b23*m.b113 + 31*m.b23*m.b116 + 32*
                       m.b23*m.b119 + 33*m.b23*m.b122 + 34*m.b23*m.b125 + 35*m.b23*m.b128 + 36*m.b23*m.b131 + 37*m.b23*
                       m.b134 + 38*m.b23*m.b137 + 39*m.b23*m.b140 + 40*m.b23*m.b143 + 41*m.b23*m.b146 + 42*m.b23*m.b149
                        + m.b24*m.b27 + 2*m.b24*m.b30 + 3*m.b24*m.b33 + 4*m.b24*m.b36 + 5*m.b24*m.b39 + 6*m.b24*m.b42 + 
                       7*m.b24*m.b45 + 8*m.b24*m.b48 + 9*m.b24*m.b51 + 10*m.b24*m.b54 + 11*m.b24*m.b57 + 12*m.b24*m.b60
                        + 13*m.b24*m.b63 + 14*m.b24*m.b66 + 15*m.b24*m.b69 + 16*m.b24*m.b72 + 17*m.b24*m.b75 + 18*m.b24*
                       m.b78 + 19*m.b24*m.b81 + 20*m.b24*m.b84 + 21*m.b24*m.b87 + 22*m.b24*m.b90 + 23*m.b24*m.b93 + 24*
                       m.b24*m.b96 + 25*m.b24*m.b99 + 26*m.b24*m.b102 + 27*m.b24*m.b105 + 28*m.b24*m.b108 + 29*m.b24*
                       m.b111 + 30*m.b24*m.b114 + 31*m.b24*m.b117 + 32*m.b24*m.b120 + 33*m.b24*m.b123 + 34*m.b24*m.b126
                        + 35*m.b24*m.b129 + 36*m.b24*m.b132 + 37*m.b24*m.b135 + 38*m.b24*m.b138 + 39*m.b24*m.b141 + 40*
                       m.b24*m.b144 + 41*m.b24*m.b147 + 42*m.b24*m.b150 + m.b25*m.b28 + 2*m.b25*m.b31 + 3*m.b25*m.b34 + 
                       4*m.b25*m.b37 + 5*m.b25*m.b40 + 6*m.b25*m.b43 + 7*m.b25*m.b46 + 8*m.b25*m.b49 + 9*m.b25*m.b52 + 
                       10*m.b25*m.b55 + 11*m.b25*m.b58 + 12*m.b25*m.b61 + 13*m.b25*m.b64 + 14*m.b25*m.b67 + 15*m.b25*
                       m.b70 + 16*m.b25*m.b73 + 17*m.b25*m.b76 + 18*m.b25*m.b79 + 19*m.b25*m.b82 + 20*m.b25*m.b85 + 21*
                       m.b25*m.b88 + 22*m.b25*m.b91 + 23*m.b25*m.b94 + 24*m.b25*m.b97 + 25*m.b25*m.b100 + 26*m.b25*
                       m.b103 + 27*m.b25*m.b106 + 28*m.b25*m.b109 + 29*m.b25*m.b112 + 30*m.b25*m.b115 + 31*m.b25*m.b118
                        + 32*m.b25*m.b121 + 33*m.b25*m.b124 + 34*m.b25*m.b127 + 35*m.b25*m.b130 + 36*m.b25*m.b133 + 37*
                       m.b25*m.b136 + 38*m.b25*m.b139 + 39*m.b25*m.b142 + 40*m.b25*m.b145 + 41*m.b25*m.b148 + m.b26*
                       m.b29 + 2*m.b26*m.b32 + 3*m.b26*m.b35 + 4*m.b26*m.b38 + 5*m.b26*m.b41 + 6*m.b26*m.b44 + 7*m.b26*
                       m.b47 + 8*m.b26*m.b50 + 9*m.b26*m.b53 + 10*m.b26*m.b56 + 11*m.b26*m.b59 + 12*m.b26*m.b62 + 13*
                       m.b26*m.b65 + 14*m.b26*m.b68 + 15*m.b26*m.b71 + 16*m.b26*m.b74 + 17*m.b26*m.b77 + 18*m.b26*m.b80
                        + 19*m.b26*m.b83 + 20*m.b26*m.b86 + 21*m.b26*m.b89 + 22*m.b26*m.b92 + 23*m.b26*m.b95 + 24*m.b26*
                       m.b98 + 25*m.b26*m.b101 + 26*m.b26*m.b104 + 27*m.b26*m.b107 + 28*m.b26*m.b110 + 29*m.b26*m.b113
                        + 30*m.b26*m.b116 + 31*m.b26*m.b119 + 32*m.b26*m.b122 + 33*m.b26*m.b125 + 34*m.b26*m.b128 + 35*
                       m.b26*m.b131 + 36*m.b26*m.b134 + 37*m.b26*m.b137 + 38*m.b26*m.b140 + 39*m.b26*m.b143 + 40*m.b26*
                       m.b146 + 41*m.b26*m.b149 + m.b27*m.b30 + 2*m.b27*m.b33 + 3*m.b27*m.b36 + 4*m.b27*m.b39 + 5*m.b27*
                       m.b42 + 6*m.b27*m.b45 + 7*m.b27*m.b48 + 8*m.b27*m.b51 + 9*m.b27*m.b54 + 10*m.b27*m.b57 + 11*m.b27
                       *m.b60 + 12*m.b27*m.b63 + 13*m.b27*m.b66 + 14*m.b27*m.b69 + 15*m.b27*m.b72 + 16*m.b27*m.b75 + 17*
                       m.b27*m.b78 + 18*m.b27*m.b81 + 19*m.b27*m.b84 + 20*m.b27*m.b87 + 21*m.b27*m.b90 + 22*m.b27*m.b93
                        + 23*m.b27*m.b96 + 24*m.b27*m.b99 + 25*m.b27*m.b102 + 26*m.b27*m.b105 + 27*m.b27*m.b108 + 28*
                       m.b27*m.b111 + 29*m.b27*m.b114 + 30*m.b27*m.b117 + 31*m.b27*m.b120 + 32*m.b27*m.b123 + 33*m.b27*
                       m.b126 + 34*m.b27*m.b129 + 35*m.b27*m.b132 + 36*m.b27*m.b135 + 37*m.b27*m.b138 + 38*m.b27*m.b141
                        + 39*m.b27*m.b144 + 40*m.b27*m.b147 + 41*m.b27*m.b150 + m.b28*m.b31 + 2*m.b28*m.b34 + 3*m.b28*
                       m.b37 + 4*m.b28*m.b40 + 5*m.b28*m.b43 + 6*m.b28*m.b46 + 7*m.b28*m.b49 + 8*m.b28*m.b52 + 9*m.b28*
                       m.b55 + 10*m.b28*m.b58 + 11*m.b28*m.b61 + 12*m.b28*m.b64 + 13*m.b28*m.b67 + 14*m.b28*m.b70 + 15*
                       m.b28*m.b73 + 16*m.b28*m.b76 + 17*m.b28*m.b79 + 18*m.b28*m.b82 + 19*m.b28*m.b85 + 20*m.b28*m.b88
                        + 21*m.b28*m.b91 + 22*m.b28*m.b94 + 23*m.b28*m.b97 + 24*m.b28*m.b100 + 25*m.b28*m.b103 + 26*
                       m.b28*m.b106 + 27*m.b28*m.b109 + 28*m.b28*m.b112 + 29*m.b28*m.b115 + 30*m.b28*m.b118 + 31*m.b28*
                       m.b121 + 32*m.b28*m.b124 + 33*m.b28*m.b127 + 34*m.b28*m.b130 + 35*m.b28*m.b133 + 36*m.b28*m.b136
                        + 37*m.b28*m.b139 + 38*m.b28*m.b142 + 39*m.b28*m.b145 + 40*m.b28*m.b148 + m.b29*m.b32 + 2*m.b29*
                       m.b35 + 3*m.b29*m.b38 + 4*m.b29*m.b41 + 5*m.b29*m.b44 + 6*m.b29*m.b47 + 7*m.b29*m.b50 + 8*m.b29*
                       m.b53 + 9*m.b29*m.b56 + 10*m.b29*m.b59 + 11*m.b29*m.b62 + 12*m.b29*m.b65 + 13*m.b29*m.b68 + 14*
                       m.b29*m.b71 + 15*m.b29*m.b74 + 16*m.b29*m.b77 + 17*m.b29*m.b80 + 18*m.b29*m.b83 + 19*m.b29*m.b86
                        + 20*m.b29*m.b89 + 21*m.b29*m.b92 + 22*m.b29*m.b95 + 23*m.b29*m.b98 + 24*m.b29*m.b101 + 25*m.b29
                       *m.b104 + 26*m.b29*m.b107 + 27*m.b29*m.b110 + 28*m.b29*m.b113 + 29*m.b29*m.b116 + 30*m.b29*m.b119
                        + 31*m.b29*m.b122 + 32*m.b29*m.b125 + 33*m.b29*m.b128 + 34*m.b29*m.b131 + 35*m.b29*m.b134 + 36*
                       m.b29*m.b137 + 37*m.b29*m.b140 + 38*m.b29*m.b143 + 39*m.b29*m.b146 + 40*m.b29*m.b149 + m.b30*
                       m.b33 + 2*m.b30*m.b36 + 3*m.b30*m.b39 + 4*m.b30*m.b42 + 5*m.b30*m.b45 + 6*m.b30*m.b48 + 7*m.b30*
                       m.b51 + 8*m.b30*m.b54 + 9*m.b30*m.b57 + 10*m.b30*m.b60 + 11*m.b30*m.b63 + 12*m.b30*m.b66 + 13*
                       m.b30*m.b69 + 14*m.b30*m.b72 + 15*m.b30*m.b75 + 16*m.b30*m.b78 + 17*m.b30*m.b81 + 18*m.b30*m.b84
                        + 19*m.b30*m.b87 + 20*m.b30*m.b90 + 21*m.b30*m.b93 + 22*m.b30*m.b96 + 23*m.b30*m.b99 + 24*m.b30*
                       m.b102 + 25*m.b30*m.b105 + 26*m.b30*m.b108 + 27*m.b30*m.b111 + 28*m.b30*m.b114 + 29*m.b30*m.b117
                        + 30*m.b30*m.b120 + 31*m.b30*m.b123 + 32*m.b30*m.b126 + 33*m.b30*m.b129 + 34*m.b30*m.b132 + 35*
                       m.b30*m.b135 + 36*m.b30*m.b138 + 37*m.b30*m.b141 + 38*m.b30*m.b144 + 39*m.b30*m.b147 + 40*m.b30*
                       m.b150 + m.b31*m.b34 + 2*m.b31*m.b37 + 3*m.b31*m.b40 + 4*m.b31*m.b43 + 5*m.b31*m.b46 + 6*m.b31*
                       m.b49 + 7*m.b31*m.b52 + 8*m.b31*m.b55 + 9*m.b31*m.b58 + 10*m.b31*m.b61 + 11*m.b31*m.b64 + 12*
                       m.b31*m.b67 + 13*m.b31*m.b70 + 14*m.b31*m.b73 + 15*m.b31*m.b76 + 16*m.b31*m.b79 + 17*m.b31*m.b82
                        + 18*m.b31*m.b85 + 19*m.b31*m.b88 + 20*m.b31*m.b91 + 21*m.b31*m.b94 + 22*m.b31*m.b97 + 23*m.b31*
                       m.b100 + 24*m.b31*m.b103 + 25*m.b31*m.b106 + 26*m.b31*m.b109 + 27*m.b31*m.b112 + 28*m.b31*m.b115
                        + 29*m.b31*m.b118 + 30*m.b31*m.b121 + 31*m.b31*m.b124 + 32*m.b31*m.b127 + 33*m.b31*m.b130 + 34*
                       m.b31*m.b133 + 35*m.b31*m.b136 + 36*m.b31*m.b139 + 37*m.b31*m.b142 + 38*m.b31*m.b145 + 39*m.b31*
                       m.b148 + m.b32*m.b35 + 2*m.b32*m.b38 + 3*m.b32*m.b41 + 4*m.b32*m.b44 + 5*m.b32*m.b47 + 6*m.b32*
                       m.b50 + 7*m.b32*m.b53 + 8*m.b32*m.b56 + 9*m.b32*m.b59 + 10*m.b32*m.b62 + 11*m.b32*m.b65 + 12*
                       m.b32*m.b68 + 13*m.b32*m.b71 + 14*m.b32*m.b74 + 15*m.b32*m.b77 + 16*m.b32*m.b80 + 17*m.b32*m.b83
                        + 18*m.b32*m.b86 + 19*m.b32*m.b89 + 20*m.b32*m.b92 + 21*m.b32*m.b95 + 22*m.b32*m.b98 + 23*m.b32*
                       m.b101 + 24*m.b32*m.b104 + 25*m.b32*m.b107 + 26*m.b32*m.b110 + 27*m.b32*m.b113 + 28*m.b32*m.b116
                        + 29*m.b32*m.b119 + 30*m.b32*m.b122 + 31*m.b32*m.b125 + 32*m.b32*m.b128 + 33*m.b32*m.b131 + 34*
                       m.b32*m.b134 + 35*m.b32*m.b137 + 36*m.b32*m.b140 + 37*m.b32*m.b143 + 38*m.b32*m.b146 + 39*m.b32*
                       m.b149 + m.b33*m.b36 + 2*m.b33*m.b39 + 3*m.b33*m.b42 + 4*m.b33*m.b45 + 5*m.b33*m.b48 + 6*m.b33*
                       m.b51 + 7*m.b33*m.b54 + 8*m.b33*m.b57 + 9*m.b33*m.b60 + 10*m.b33*m.b63 + 11*m.b33*m.b66 + 12*
                       m.b33*m.b69 + 13*m.b33*m.b72 + 14*m.b33*m.b75 + 15*m.b33*m.b78 + 16*m.b33*m.b81 + 17*m.b33*m.b84
                        + 18*m.b33*m.b87 + 19*m.b33*m.b90 + 20*m.b33*m.b93 + 21*m.b33*m.b96 + 22*m.b33*m.b99 + 23*m.b33*
                       m.b102 + 24*m.b33*m.b105 + 25*m.b33*m.b108 + 26*m.b33*m.b111 + 27*m.b33*m.b114 + 28*m.b33*m.b117
                        + 29*m.b33*m.b120 + 30*m.b33*m.b123 + 31*m.b33*m.b126 + 32*m.b33*m.b129 + 33*m.b33*m.b132 + 34*
                       m.b33*m.b135 + 35*m.b33*m.b138 + 36*m.b33*m.b141 + 37*m.b33*m.b144 + 38*m.b33*m.b147 + 39*m.b33*
                       m.b150 + m.b34*m.b37 + 2*m.b34*m.b40 + 3*m.b34*m.b43 + 4*m.b34*m.b46 + 5*m.b34*m.b49 + 6*m.b34*
                       m.b52 + 7*m.b34*m.b55 + 8*m.b34*m.b58 + 9*m.b34*m.b61 + 10*m.b34*m.b64 + 11*m.b34*m.b67 + 12*
                       m.b34*m.b70 + 13*m.b34*m.b73 + 14*m.b34*m.b76 + 15*m.b34*m.b79 + 16*m.b34*m.b82 + 17*m.b34*m.b85
                        + 18*m.b34*m.b88 + 19*m.b34*m.b91 + 20*m.b34*m.b94 + 21*m.b34*m.b97 + 22*m.b34*m.b100 + 23*m.b34
                       *m.b103 + 24*m.b34*m.b106 + 25*m.b34*m.b109 + 26*m.b34*m.b112 + 27*m.b34*m.b115 + 28*m.b34*m.b118
                        + 29*m.b34*m.b121 + 30*m.b34*m.b124 + 31*m.b34*m.b127 + 32*m.b34*m.b130 + 33*m.b34*m.b133 + 34*
                       m.b34*m.b136 + 35*m.b34*m.b139 + 36*m.b34*m.b142 + 37*m.b34*m.b145 + 38*m.b34*m.b148 + m.b35*
                       m.b38 + 2*m.b35*m.b41 + 3*m.b35*m.b44 + 4*m.b35*m.b47 + 5*m.b35*m.b50 + 6*m.b35*m.b53 + 7*m.b35*
                       m.b56 + 8*m.b35*m.b59 + 9*m.b35*m.b62 + 10*m.b35*m.b65 + 11*m.b35*m.b68 + 12*m.b35*m.b71 + 13*
                       m.b35*m.b74 + 14*m.b35*m.b77 + 15*m.b35*m.b80 + 16*m.b35*m.b83 + 17*m.b35*m.b86 + 18*m.b35*m.b89
                        + 19*m.b35*m.b92 + 20*m.b35*m.b95 + 21*m.b35*m.b98 + 22*m.b35*m.b101 + 23*m.b35*m.b104 + 24*
                       m.b35*m.b107 + 25*m.b35*m.b110 + 26*m.b35*m.b113 + 27*m.b35*m.b116 + 28*m.b35*m.b119 + 29*m.b35*
                       m.b122 + 30*m.b35*m.b125 + 31*m.b35*m.b128 + 32*m.b35*m.b131 + 33*m.b35*m.b134 + 34*m.b35*m.b137
                        + 35*m.b35*m.b140 + 36*m.b35*m.b143 + 37*m.b35*m.b146 + 38*m.b35*m.b149 + m.b36*m.b39 + 2*m.b36*
                       m.b42 + 3*m.b36*m.b45 + 4*m.b36*m.b48 + 5*m.b36*m.b51 + 6*m.b36*m.b54 + 7*m.b36*m.b57 + 8*m.b36*
                       m.b60 + 9*m.b36*m.b63 + 10*m.b36*m.b66 + 11*m.b36*m.b69 + 12*m.b36*m.b72 + 13*m.b36*m.b75 + 14*
                       m.b36*m.b78 + 15*m.b36*m.b81 + 16*m.b36*m.b84 + 17*m.b36*m.b87 + 18*m.b36*m.b90 + 19*m.b36*m.b93
                        + 20*m.b36*m.b96 + 21*m.b36*m.b99 + 22*m.b36*m.b102 + 23*m.b36*m.b105 + 24*m.b36*m.b108 + 25*
                       m.b36*m.b111 + 26*m.b36*m.b114 + 27*m.b36*m.b117 + 28*m.b36*m.b120 + 29*m.b36*m.b123 + 30*m.b36*
                       m.b126 + 31*m.b36*m.b129 + 32*m.b36*m.b132 + 33*m.b36*m.b135 + 34*m.b36*m.b138 + 35*m.b36*m.b141
                        + 36*m.b36*m.b144 + 37*m.b36*m.b147 + 38*m.b36*m.b150 + m.b37*m.b40 + 2*m.b37*m.b43 + 3*m.b37*
                       m.b46 + 4*m.b37*m.b49 + 5*m.b37*m.b52 + 6*m.b37*m.b55 + 7*m.b37*m.b58 + 8*m.b37*m.b61 + 9*m.b37*
                       m.b64 + 10*m.b37*m.b67 + 11*m.b37*m.b70 + 12*m.b37*m.b73 + 13*m.b37*m.b76 + 14*m.b37*m.b79 + 15*
                       m.b37*m.b82 + 16*m.b37*m.b85 + 17*m.b37*m.b88 + 18*m.b37*m.b91 + 19*m.b37*m.b94 + 20*m.b37*m.b97
                        + 21*m.b37*m.b100 + 22*m.b37*m.b103 + 23*m.b37*m.b106 + 24*m.b37*m.b109 + 25*m.b37*m.b112 + 26*
                       m.b37*m.b115 + 27*m.b37*m.b118 + 28*m.b37*m.b121 + 29*m.b37*m.b124 + 30*m.b37*m.b127 + 31*m.b37*
                       m.b130 + 32*m.b37*m.b133 + 33*m.b37*m.b136 + 34*m.b37*m.b139 + 35*m.b37*m.b142 + 36*m.b37*m.b145
                        + 37*m.b37*m.b148 + m.b38*m.b41 + 2*m.b38*m.b44 + 3*m.b38*m.b47 + 4*m.b38*m.b50 + 5*m.b38*m.b53
                        + 6*m.b38*m.b56 + 7*m.b38*m.b59 + 8*m.b38*m.b62 + 9*m.b38*m.b65 + 10*m.b38*m.b68 + 11*m.b38*
                       m.b71 + 12*m.b38*m.b74 + 13*m.b38*m.b77 + 14*m.b38*m.b80 + 15*m.b38*m.b83 + 16*m.b38*m.b86 + 17*
                       m.b38*m.b89 + 18*m.b38*m.b92 + 19*m.b38*m.b95 + 20*m.b38*m.b98 + 21*m.b38*m.b101 + 22*m.b38*
                       m.b104 + 23*m.b38*m.b107 + 24*m.b38*m.b110 + 25*m.b38*m.b113 + 26*m.b38*m.b116 + 27*m.b38*m.b119
                        + 28*m.b38*m.b122 + 29*m.b38*m.b125 + 30*m.b38*m.b128 + 31*m.b38*m.b131 + 32*m.b38*m.b134 + 33*
                       m.b38*m.b137 + 34*m.b38*m.b140 + 35*m.b38*m.b143 + 36*m.b38*m.b146 + 37*m.b38*m.b149 + m.b39*
                       m.b42 + 2*m.b39*m.b45 + 3*m.b39*m.b48 + 4*m.b39*m.b51 + 5*m.b39*m.b54 + 6*m.b39*m.b57 + 7*m.b39*
                       m.b60 + 8*m.b39*m.b63 + 9*m.b39*m.b66 + 10*m.b39*m.b69 + 11*m.b39*m.b72 + 12*m.b39*m.b75 + 13*
                       m.b39*m.b78 + 14*m.b39*m.b81 + 15*m.b39*m.b84 + 16*m.b39*m.b87 + 17*m.b39*m.b90 + 18*m.b39*m.b93
                        + 19*m.b39*m.b96 + 20*m.b39*m.b99 + 21*m.b39*m.b102 + 22*m.b39*m.b105 + 23*m.b39*m.b108 + 24*
                       m.b39*m.b111 + 25*m.b39*m.b114 + 26*m.b39*m.b117 + 27*m.b39*m.b120 + 28*m.b39*m.b123 + 29*m.b39*
                       m.b126 + 30*m.b39*m.b129 + 31*m.b39*m.b132 + 32*m.b39*m.b135 + 33*m.b39*m.b138 + 34*m.b39*m.b141
                        + 35*m.b39*m.b144 + 36*m.b39*m.b147 + 37*m.b39*m.b150 + m.b40*m.b43 + 2*m.b40*m.b46 + 3*m.b40*
                       m.b49 + 4*m.b40*m.b52 + 5*m.b40*m.b55 + 6*m.b40*m.b58 + 7*m.b40*m.b61 + 8*m.b40*m.b64 + 9*m.b40*
                       m.b67 + 10*m.b40*m.b70 + 11*m.b40*m.b73 + 12*m.b40*m.b76 + 13*m.b40*m.b79 + 14*m.b40*m.b82 + 15*
                       m.b40*m.b85 + 16*m.b40*m.b88 + 17*m.b40*m.b91 + 18*m.b40*m.b94 + 19*m.b40*m.b97 + 20*m.b40*m.b100
                        + 21*m.b40*m.b103 + 22*m.b40*m.b106 + 23*m.b40*m.b109 + 24*m.b40*m.b112 + 25*m.b40*m.b115 + 26*
                       m.b40*m.b118 + 27*m.b40*m.b121 + 28*m.b40*m.b124 + 29*m.b40*m.b127 + 30*m.b40*m.b130 + 31*m.b40*
                       m.b133 + 32*m.b40*m.b136 + 33*m.b40*m.b139 + 34*m.b40*m.b142 + 35*m.b40*m.b145 + 36*m.b40*m.b148
                        + m.b41*m.b44 + 2*m.b41*m.b47 + 3*m.b41*m.b50 + 4*m.b41*m.b53 + 5*m.b41*m.b56 + 6*m.b41*m.b59 + 
                       7*m.b41*m.b62 + 8*m.b41*m.b65 + 9*m.b41*m.b68 + 10*m.b41*m.b71 + 11*m.b41*m.b74 + 12*m.b41*m.b77
                        + 13*m.b41*m.b80 + 14*m.b41*m.b83 + 15*m.b41*m.b86 + 16*m.b41*m.b89 + 17*m.b41*m.b92 + 18*m.b41*
                       m.b95 + 19*m.b41*m.b98 + 20*m.b41*m.b101 + 21*m.b41*m.b104 + 22*m.b41*m.b107 + 23*m.b41*m.b110 + 
                       24*m.b41*m.b113 + 25*m.b41*m.b116 + 26*m.b41*m.b119 + 27*m.b41*m.b122 + 28*m.b41*m.b125 + 29*
                       m.b41*m.b128 + 30*m.b41*m.b131 + 31*m.b41*m.b134 + 32*m.b41*m.b137 + 33*m.b41*m.b140 + 34*m.b41*
                       m.b143 + 35*m.b41*m.b146 + 36*m.b41*m.b149 + m.b42*m.b45 + 2*m.b42*m.b48 + 3*m.b42*m.b51 + 4*
                       m.b42*m.b54 + 5*m.b42*m.b57 + 6*m.b42*m.b60 + 7*m.b42*m.b63 + 8*m.b42*m.b66 + 9*m.b42*m.b69 + 10*
                       m.b42*m.b72 + 11*m.b42*m.b75 + 12*m.b42*m.b78 + 13*m.b42*m.b81 + 14*m.b42*m.b84 + 15*m.b42*m.b87
                        + 16*m.b42*m.b90 + 17*m.b42*m.b93 + 18*m.b42*m.b96 + 19*m.b42*m.b99 + 20*m.b42*m.b102 + 21*m.b42
                       *m.b105 + 22*m.b42*m.b108 + 23*m.b42*m.b111 + 24*m.b42*m.b114 + 25*m.b42*m.b117 + 26*m.b42*m.b120
                        + 27*m.b42*m.b123 + 28*m.b42*m.b126 + 29*m.b42*m.b129 + 30*m.b42*m.b132 + 31*m.b42*m.b135 + 32*
                       m.b42*m.b138 + 33*m.b42*m.b141 + 34*m.b42*m.b144 + 35*m.b42*m.b147 + 36*m.b42*m.b150 + m.b43*
                       m.b46 + 2*m.b43*m.b49 + 3*m.b43*m.b52 + 4*m.b43*m.b55 + 5*m.b43*m.b58 + 6*m.b43*m.b61 + 7*m.b43*
                       m.b64 + 8*m.b43*m.b67 + 9*m.b43*m.b70 + 10*m.b43*m.b73 + 11*m.b43*m.b76 + 12*m.b43*m.b79 + 13*
                       m.b43*m.b82 + 14*m.b43*m.b85 + 15*m.b43*m.b88 + 16*m.b43*m.b91 + 17*m.b43*m.b94 + 18*m.b43*m.b97
                        + 19*m.b43*m.b100 + 20*m.b43*m.b103 + 21*m.b43*m.b106 + 22*m.b43*m.b109 + 23*m.b43*m.b112 + 24*
                       m.b43*m.b115 + 25*m.b43*m.b118 + 26*m.b43*m.b121 + 27*m.b43*m.b124 + 28*m.b43*m.b127 + 29*m.b43*
                       m.b130 + 30*m.b43*m.b133 + 31*m.b43*m.b136 + 32*m.b43*m.b139 + 33*m.b43*m.b142 + 34*m.b43*m.b145
                        + 35*m.b43*m.b148 + m.b44*m.b47 + 2*m.b44*m.b50 + 3*m.b44*m.b53 + 4*m.b44*m.b56 + 5*m.b44*m.b59
                        + 6*m.b44*m.b62 + 7*m.b44*m.b65 + 8*m.b44*m.b68 + 9*m.b44*m.b71 + 10*m.b44*m.b74 + 11*m.b44*
                       m.b77 + 12*m.b44*m.b80 + 13*m.b44*m.b83 + 14*m.b44*m.b86 + 15*m.b44*m.b89 + 16*m.b44*m.b92 + 17*
                       m.b44*m.b95 + 18*m.b44*m.b98 + 19*m.b44*m.b101 + 20*m.b44*m.b104 + 21*m.b44*m.b107 + 22*m.b44*
                       m.b110 + 23*m.b44*m.b113 + 24*m.b44*m.b116 + 25*m.b44*m.b119 + 26*m.b44*m.b122 + 27*m.b44*m.b125
                        + 28*m.b44*m.b128 + 29*m.b44*m.b131 + 30*m.b44*m.b134 + 31*m.b44*m.b137 + 32*m.b44*m.b140 + 33*
                       m.b44*m.b143 + 34*m.b44*m.b146 + 35*m.b44*m.b149 + m.b45*m.b48 + 2*m.b45*m.b51 + 3*m.b45*m.b54 + 
                       4*m.b45*m.b57 + 5*m.b45*m.b60 + 6*m.b45*m.b63 + 7*m.b45*m.b66 + 8*m.b45*m.b69 + 9*m.b45*m.b72 + 
                       10*m.b45*m.b75 + 11*m.b45*m.b78 + 12*m.b45*m.b81 + 13*m.b45*m.b84 + 14*m.b45*m.b87 + 15*m.b45*
                       m.b90 + 16*m.b45*m.b93 + 17*m.b45*m.b96 + 18*m.b45*m.b99 + 19*m.b45*m.b102 + 20*m.b45*m.b105 + 21
                       *m.b45*m.b108 + 22*m.b45*m.b111 + 23*m.b45*m.b114 + 24*m.b45*m.b117 + 25*m.b45*m.b120 + 26*m.b45*
                       m.b123 + 27*m.b45*m.b126 + 28*m.b45*m.b129 + 29*m.b45*m.b132 + 30*m.b45*m.b135 + 31*m.b45*m.b138
                        + 32*m.b45*m.b141 + 33*m.b45*m.b144 + 34*m.b45*m.b147 + 35*m.b45*m.b150 + m.b46*m.b49 + 2*m.b46*
                       m.b52 + 3*m.b46*m.b55 + 4*m.b46*m.b58 + 5*m.b46*m.b61 + 6*m.b46*m.b64 + 7*m.b46*m.b67 + 8*m.b46*
                       m.b70 + 9*m.b46*m.b73 + 10*m.b46*m.b76 + 11*m.b46*m.b79 + 12*m.b46*m.b82 + 13*m.b46*m.b85 + 14*
                       m.b46*m.b88 + 15*m.b46*m.b91 + 16*m.b46*m.b94 + 17*m.b46*m.b97 + 18*m.b46*m.b100 + 19*m.b46*
                       m.b103 + 20*m.b46*m.b106 + 21*m.b46*m.b109 + 22*m.b46*m.b112 + 23*m.b46*m.b115 + 24*m.b46*m.b118
                        + 25*m.b46*m.b121 + 26*m.b46*m.b124 + 27*m.b46*m.b127 + 28*m.b46*m.b130 + 29*m.b46*m.b133 + 30*
                       m.b46*m.b136 + 31*m.b46*m.b139 + 32*m.b46*m.b142 + 33*m.b46*m.b145 + 34*m.b46*m.b148 + m.b47*
                       m.b50 + 2*m.b47*m.b53 + 3*m.b47*m.b56 + 4*m.b47*m.b59 + 5*m.b47*m.b62 + 6*m.b47*m.b65 + 7*m.b47*
                       m.b68 + 8*m.b47*m.b71 + 9*m.b47*m.b74 + 10*m.b47*m.b77 + 11*m.b47*m.b80 + 12*m.b47*m.b83 + 13*
                       m.b47*m.b86 + 14*m.b47*m.b89 + 15*m.b47*m.b92 + 16*m.b47*m.b95 + 17*m.b47*m.b98 + 18*m.b47*m.b101
                        + 19*m.b47*m.b104 + 20*m.b47*m.b107 + 21*m.b47*m.b110 + 22*m.b47*m.b113 + 23*m.b47*m.b116 + 24*
                       m.b47*m.b119 + 25*m.b47*m.b122 + 26*m.b47*m.b125 + 27*m.b47*m.b128 + 28*m.b47*m.b131 + 29*m.b47*
                       m.b134 + 30*m.b47*m.b137 + 31*m.b47*m.b140 + 32*m.b47*m.b143 + 33*m.b47*m.b146 + 34*m.b47*m.b149
                        + m.b48*m.b51 + 2*m.b48*m.b54 + 3*m.b48*m.b57 + 4*m.b48*m.b60 + 5*m.b48*m.b63 + 6*m.b48*m.b66 + 
                       7*m.b48*m.b69 + 8*m.b48*m.b72 + 9*m.b48*m.b75 + 10*m.b48*m.b78 + 11*m.b48*m.b81 + 12*m.b48*m.b84
                        + 13*m.b48*m.b87 + 14*m.b48*m.b90 + 15*m.b48*m.b93 + 16*m.b48*m.b96 + 17*m.b48*m.b99 + 18*m.b48*
                       m.b102 + 19*m.b48*m.b105 + 20*m.b48*m.b108 + 21*m.b48*m.b111 + 22*m.b48*m.b114 + 23*m.b48*m.b117
                        + 24*m.b48*m.b120 + 25*m.b48*m.b123 + 26*m.b48*m.b126 + 27*m.b48*m.b129 + 28*m.b48*m.b132 + 29*
                       m.b48*m.b135 + 30*m.b48*m.b138 + 31*m.b48*m.b141 + 32*m.b48*m.b144 + 33*m.b48*m.b147 + 34*m.b48*
                       m.b150 + m.b49*m.b52 + 2*m.b49*m.b55 + 3*m.b49*m.b58 + 4*m.b49*m.b61 + 5*m.b49*m.b64 + 6*m.b49*
                       m.b67 + 7*m.b49*m.b70 + 8*m.b49*m.b73 + 9*m.b49*m.b76 + 10*m.b49*m.b79 + 11*m.b49*m.b82 + 12*
                       m.b49*m.b85 + 13*m.b49*m.b88 + 14*m.b49*m.b91 + 15*m.b49*m.b94 + 16*m.b49*m.b97 + 17*m.b49*m.b100
                        + 18*m.b49*m.b103 + 19*m.b49*m.b106 + 20*m.b49*m.b109 + 21*m.b49*m.b112 + 22*m.b49*m.b115 + 23*
                       m.b49*m.b118 + 24*m.b49*m.b121 + 25*m.b49*m.b124 + 26*m.b49*m.b127 + 27*m.b49*m.b130 + 28*m.b49*
                       m.b133 + 29*m.b49*m.b136 + 30*m.b49*m.b139 + 31*m.b49*m.b142 + 32*m.b49*m.b145 + 33*m.b49*m.b148
                        + m.b50*m.b53 + 2*m.b50*m.b56 + 3*m.b50*m.b59 + 4*m.b50*m.b62 + 5*m.b50*m.b65 + 6*m.b50*m.b68 + 
                       7*m.b50*m.b71 + 8*m.b50*m.b74 + 9*m.b50*m.b77 + 10*m.b50*m.b80 + 11*m.b50*m.b83 + 12*m.b50*m.b86
                        + 13*m.b50*m.b89 + 14*m.b50*m.b92 + 15*m.b50*m.b95 + 16*m.b50*m.b98 + 17*m.b50*m.b101 + 18*m.b50
                       *m.b104 + 19*m.b50*m.b107 + 20*m.b50*m.b110 + 21*m.b50*m.b113 + 22*m.b50*m.b116 + 23*m.b50*m.b119
                        + 24*m.b50*m.b122 + 25*m.b50*m.b125 + 26*m.b50*m.b128 + 27*m.b50*m.b131 + 28*m.b50*m.b134 + 29*
                       m.b50*m.b137 + 30*m.b50*m.b140 + 31*m.b50*m.b143 + 32*m.b50*m.b146 + 33*m.b50*m.b149 + m.b51*
                       m.b54 + 2*m.b51*m.b57 + 3*m.b51*m.b60 + 4*m.b51*m.b63 + 5*m.b51*m.b66 + 6*m.b51*m.b69 + 7*m.b51*
                       m.b72 + 8*m.b51*m.b75 + 9*m.b51*m.b78 + 10*m.b51*m.b81 + 11*m.b51*m.b84 + 12*m.b51*m.b87 + 13*
                       m.b51*m.b90 + 14*m.b51*m.b93 + 15*m.b51*m.b96 + 16*m.b51*m.b99 + 17*m.b51*m.b102 + 18*m.b51*
                       m.b105 + 19*m.b51*m.b108 + 20*m.b51*m.b111 + 21*m.b51*m.b114 + 22*m.b51*m.b117 + 23*m.b51*m.b120
                        + 24*m.b51*m.b123 + 25*m.b51*m.b126 + 26*m.b51*m.b129 + 27*m.b51*m.b132 + 28*m.b51*m.b135 + 29*
                       m.b51*m.b138 + 30*m.b51*m.b141 + 31*m.b51*m.b144 + 32*m.b51*m.b147 + 33*m.b51*m.b150 + m.b52*
                       m.b55 + 2*m.b52*m.b58 + 3*m.b52*m.b61 + 4*m.b52*m.b64 + 5*m.b52*m.b67 + 6*m.b52*m.b70 + 7*m.b52*
                       m.b73 + 8*m.b52*m.b76 + 9*m.b52*m.b79 + 10*m.b52*m.b82 + 11*m.b52*m.b85 + 12*m.b52*m.b88 + 13*
                       m.b52*m.b91 + 14*m.b52*m.b94 + 15*m.b52*m.b97 + 16*m.b52*m.b100 + 17*m.b52*m.b103 + 18*m.b52*
                       m.b106 + 19*m.b52*m.b109 + 20*m.b52*m.b112 + 21*m.b52*m.b115 + 22*m.b52*m.b118 + 23*m.b52*m.b121
                        + 24*m.b52*m.b124 + 25*m.b52*m.b127 + 26*m.b52*m.b130 + 27*m.b52*m.b133 + 28*m.b52*m.b136 + 29*
                       m.b52*m.b139 + 30*m.b52*m.b142 + 31*m.b52*m.b145 + 32*m.b52*m.b148 + m.b53*m.b56 + 2*m.b53*m.b59
                        + 3*m.b53*m.b62 + 4*m.b53*m.b65 + 5*m.b53*m.b68 + 6*m.b53*m.b71 + 7*m.b53*m.b74 + 8*m.b53*m.b77
                        + 9*m.b53*m.b80 + 10*m.b53*m.b83 + 11*m.b53*m.b86 + 12*m.b53*m.b89 + 13*m.b53*m.b92 + 14*m.b53*
                       m.b95 + 15*m.b53*m.b98 + 16*m.b53*m.b101 + 17*m.b53*m.b104 + 18*m.b53*m.b107 + 19*m.b53*m.b110 + 
                       20*m.b53*m.b113 + 21*m.b53*m.b116 + 22*m.b53*m.b119 + 23*m.b53*m.b122 + 24*m.b53*m.b125 + 25*
                       m.b53*m.b128 + 26*m.b53*m.b131 + 27*m.b53*m.b134 + 28*m.b53*m.b137 + 29*m.b53*m.b140 + 30*m.b53*
                       m.b143 + 31*m.b53*m.b146 + 32*m.b53*m.b149 + m.b54*m.b57 + 2*m.b54*m.b60 + 3*m.b54*m.b63 + 4*
                       m.b54*m.b66 + 5*m.b54*m.b69 + 6*m.b54*m.b72 + 7*m.b54*m.b75 + 8*m.b54*m.b78 + 9*m.b54*m.b81 + 10*
                       m.b54*m.b84 + 11*m.b54*m.b87 + 12*m.b54*m.b90 + 13*m.b54*m.b93 + 14*m.b54*m.b96 + 15*m.b54*m.b99
                        + 16*m.b54*m.b102 + 17*m.b54*m.b105 + 18*m.b54*m.b108 + 19*m.b54*m.b111 + 20*m.b54*m.b114 + 21*
                       m.b54*m.b117 + 22*m.b54*m.b120 + 23*m.b54*m.b123 + 24*m.b54*m.b126 + 25*m.b54*m.b129 + 26*m.b54*
                       m.b132 + 27*m.b54*m.b135 + 28*m.b54*m.b138 + 29*m.b54*m.b141 + 30*m.b54*m.b144 + 31*m.b54*m.b147
                        + 32*m.b54*m.b150 + m.b55*m.b58 + 2*m.b55*m.b61 + 3*m.b55*m.b64 + 4*m.b55*m.b67 + 5*m.b55*m.b70
                        + 6*m.b55*m.b73 + 7*m.b55*m.b76 + 8*m.b55*m.b79 + 9*m.b55*m.b82 + 10*m.b55*m.b85 + 11*m.b55*
                       m.b88 + 12*m.b55*m.b91 + 13*m.b55*m.b94 + 14*m.b55*m.b97 + 15*m.b55*m.b100 + 16*m.b55*m.b103 + 17
                       *m.b55*m.b106 + 18*m.b55*m.b109 + 19*m.b55*m.b112 + 20*m.b55*m.b115 + 21*m.b55*m.b118 + 22*m.b55*
                       m.b121 + 23*m.b55*m.b124 + 24*m.b55*m.b127 + 25*m.b55*m.b130 + 26*m.b55*m.b133 + 27*m.b55*m.b136
                        + 28*m.b55*m.b139 + 29*m.b55*m.b142 + 30*m.b55*m.b145 + 31*m.b55*m.b148 + m.b56*m.b59 + 2*m.b56*
                       m.b62 + 3*m.b56*m.b65 + 4*m.b56*m.b68 + 5*m.b56*m.b71 + 6*m.b56*m.b74 + 7*m.b56*m.b77 + 8*m.b56*
                       m.b80 + 9*m.b56*m.b83 + 10*m.b56*m.b86 + 11*m.b56*m.b89 + 12*m.b56*m.b92 + 13*m.b56*m.b95 + 14*
                       m.b56*m.b98 + 15*m.b56*m.b101 + 16*m.b56*m.b104 + 17*m.b56*m.b107 + 18*m.b56*m.b110 + 19*m.b56*
                       m.b113 + 20*m.b56*m.b116 + 21*m.b56*m.b119 + 22*m.b56*m.b122 + 23*m.b56*m.b125 + 24*m.b56*m.b128
                        + 25*m.b56*m.b131 + 26*m.b56*m.b134 + 27*m.b56*m.b137 + 28*m.b56*m.b140 + 29*m.b56*m.b143 + 30*
                       m.b56*m.b146 + 31*m.b56*m.b149 + m.b57*m.b60 + 2*m.b57*m.b63 + 3*m.b57*m.b66 + 4*m.b57*m.b69 + 5*
                       m.b57*m.b72 + 6*m.b57*m.b75 + 7*m.b57*m.b78 + 8*m.b57*m.b81 + 9*m.b57*m.b84 + 10*m.b57*m.b87 + 11
                       *m.b57*m.b90 + 12*m.b57*m.b93 + 13*m.b57*m.b96 + 14*m.b57*m.b99 + 15*m.b57*m.b102 + 16*m.b57*
                       m.b105 + 17*m.b57*m.b108 + 18*m.b57*m.b111 + 19*m.b57*m.b114 + 20*m.b57*m.b117 + 21*m.b57*m.b120
                        + 22*m.b57*m.b123 + 23*m.b57*m.b126 + 24*m.b57*m.b129 + 25*m.b57*m.b132 + 26*m.b57*m.b135 + 27*
                       m.b57*m.b138 + 28*m.b57*m.b141 + 29*m.b57*m.b144 + 30*m.b57*m.b147 + 31*m.b57*m.b150 + m.b58*
                       m.b61 + 2*m.b58*m.b64 + 3*m.b58*m.b67 + 4*m.b58*m.b70 + 5*m.b58*m.b73 + 6*m.b58*m.b76 + 7*m.b58*
                       m.b79 + 8*m.b58*m.b82 + 9*m.b58*m.b85 + 10*m.b58*m.b88 + 11*m.b58*m.b91 + 12*m.b58*m.b94 + 13*
                       m.b58*m.b97 + 14*m.b58*m.b100 + 15*m.b58*m.b103 + 16*m.b58*m.b106 + 17*m.b58*m.b109 + 18*m.b58*
                       m.b112 + 19*m.b58*m.b115 + 20*m.b58*m.b118 + 21*m.b58*m.b121 + 22*m.b58*m.b124 + 23*m.b58*m.b127
                        + 24*m.b58*m.b130 + 25*m.b58*m.b133 + 26*m.b58*m.b136 + 27*m.b58*m.b139 + 28*m.b58*m.b142 + 29*
                       m.b58*m.b145 + 30*m.b58*m.b148 + m.b59*m.b62 + 2*m.b59*m.b65 + 3*m.b59*m.b68 + 4*m.b59*m.b71 + 5*
                       m.b59*m.b74 + 6*m.b59*m.b77 + 7*m.b59*m.b80 + 8*m.b59*m.b83 + 9*m.b59*m.b86 + 10*m.b59*m.b89 + 11
                       *m.b59*m.b92 + 12*m.b59*m.b95 + 13*m.b59*m.b98 + 14*m.b59*m.b101 + 15*m.b59*m.b104 + 16*m.b59*
                       m.b107 + 17*m.b59*m.b110 + 18*m.b59*m.b113 + 19*m.b59*m.b116 + 20*m.b59*m.b119 + 21*m.b59*m.b122
                        + 22*m.b59*m.b125 + 23*m.b59*m.b128 + 24*m.b59*m.b131 + 25*m.b59*m.b134 + 26*m.b59*m.b137 + 27*
                       m.b59*m.b140 + 28*m.b59*m.b143 + 29*m.b59*m.b146 + 30*m.b59*m.b149 + m.b60*m.b63 + 2*m.b60*m.b66
                        + 3*m.b60*m.b69 + 4*m.b60*m.b72 + 5*m.b60*m.b75 + 6*m.b60*m.b78 + 7*m.b60*m.b81 + 8*m.b60*m.b84
                        + 9*m.b60*m.b87 + 10*m.b60*m.b90 + 11*m.b60*m.b93 + 12*m.b60*m.b96 + 13*m.b60*m.b99 + 14*m.b60*
                       m.b102 + 15*m.b60*m.b105 + 16*m.b60*m.b108 + 17*m.b60*m.b111 + 18*m.b60*m.b114 + 19*m.b60*m.b117
                        + 20*m.b60*m.b120 + 21*m.b60*m.b123 + 22*m.b60*m.b126 + 23*m.b60*m.b129 + 24*m.b60*m.b132 + 25*
                       m.b60*m.b135 + 26*m.b60*m.b138 + 27*m.b60*m.b141 + 28*m.b60*m.b144 + 29*m.b60*m.b147 + 30*m.b60*
                       m.b150 + m.b61*m.b64 + 2*m.b61*m.b67 + 3*m.b61*m.b70 + 4*m.b61*m.b73 + 5*m.b61*m.b76 + 6*m.b61*
                       m.b79 + 7*m.b61*m.b82 + 8*m.b61*m.b85 + 9*m.b61*m.b88 + 10*m.b61*m.b91 + 11*m.b61*m.b94 + 12*
                       m.b61*m.b97 + 13*m.b61*m.b100 + 14*m.b61*m.b103 + 15*m.b61*m.b106 + 16*m.b61*m.b109 + 17*m.b61*
                       m.b112 + 18*m.b61*m.b115 + 19*m.b61*m.b118 + 20*m.b61*m.b121 + 21*m.b61*m.b124 + 22*m.b61*m.b127
                        + 23*m.b61*m.b130 + 24*m.b61*m.b133 + 25*m.b61*m.b136 + 26*m.b61*m.b139 + 27*m.b61*m.b142 + 28*
                       m.b61*m.b145 + 29*m.b61*m.b148 + m.b62*m.b65 + 2*m.b62*m.b68 + 3*m.b62*m.b71 + 4*m.b62*m.b74 + 5*
                       m.b62*m.b77 + 6*m.b62*m.b80 + 7*m.b62*m.b83 + 8*m.b62*m.b86 + 9*m.b62*m.b89 + 10*m.b62*m.b92 + 11
                       *m.b62*m.b95 + 12*m.b62*m.b98 + 13*m.b62*m.b101 + 14*m.b62*m.b104 + 15*m.b62*m.b107 + 16*m.b62*
                       m.b110 + 17*m.b62*m.b113 + 18*m.b62*m.b116 + 19*m.b62*m.b119 + 20*m.b62*m.b122 + 21*m.b62*m.b125
                        + 22*m.b62*m.b128 + 23*m.b62*m.b131 + 24*m.b62*m.b134 + 25*m.b62*m.b137 + 26*m.b62*m.b140 + 27*
                       m.b62*m.b143 + 28*m.b62*m.b146 + 29*m.b62*m.b149 + m.b63*m.b66 + 2*m.b63*m.b69 + 3*m.b63*m.b72 + 
                       4*m.b63*m.b75 + 5*m.b63*m.b78 + 6*m.b63*m.b81 + 7*m.b63*m.b84 + 8*m.b63*m.b87 + 9*m.b63*m.b90 + 
                       10*m.b63*m.b93 + 11*m.b63*m.b96 + 12*m.b63*m.b99 + 13*m.b63*m.b102 + 14*m.b63*m.b105 + 15*m.b63*
                       m.b108 + 16*m.b63*m.b111 + 17*m.b63*m.b114 + 18*m.b63*m.b117 + 19*m.b63*m.b120 + 20*m.b63*m.b123
                        + 21*m.b63*m.b126 + 22*m.b63*m.b129 + 23*m.b63*m.b132 + 24*m.b63*m.b135 + 25*m.b63*m.b138 + 26*
                       m.b63*m.b141 + 27*m.b63*m.b144 + 28*m.b63*m.b147 + 29*m.b63*m.b150 + m.b64*m.b67 + 2*m.b64*m.b70
                        + 3*m.b64*m.b73 + 4*m.b64*m.b76 + 5*m.b64*m.b79 + 6*m.b64*m.b82 + 7*m.b64*m.b85 + 8*m.b64*m.b88
                        + 9*m.b64*m.b91 + 10*m.b64*m.b94 + 11*m.b64*m.b97 + 12*m.b64*m.b100 + 13*m.b64*m.b103 + 14*m.b64
                       *m.b106 + 15*m.b64*m.b109 + 16*m.b64*m.b112 + 17*m.b64*m.b115 + 18*m.b64*m.b118 + 19*m.b64*m.b121
                        + 20*m.b64*m.b124 + 21*m.b64*m.b127 + 22*m.b64*m.b130 + 23*m.b64*m.b133 + 24*m.b64*m.b136 + 25*
                       m.b64*m.b139 + 26*m.b64*m.b142 + 27*m.b64*m.b145 + 28*m.b64*m.b148 + m.b65*m.b68 + 2*m.b65*m.b71
                        + 3*m.b65*m.b74 + 4*m.b65*m.b77 + 5*m.b65*m.b80 + 6*m.b65*m.b83 + 7*m.b65*m.b86 + 8*m.b65*m.b89
                        + 9*m.b65*m.b92 + 10*m.b65*m.b95 + 11*m.b65*m.b98 + 12*m.b65*m.b101 + 13*m.b65*m.b104 + 14*m.b65
                       *m.b107 + 15*m.b65*m.b110 + 16*m.b65*m.b113 + 17*m.b65*m.b116 + 18*m.b65*m.b119 + 19*m.b65*m.b122
                        + 20*m.b65*m.b125 + 21*m.b65*m.b128 + 22*m.b65*m.b131 + 23*m.b65*m.b134 + 24*m.b65*m.b137 + 25*
                       m.b65*m.b140 + 26*m.b65*m.b143 + 27*m.b65*m.b146 + 28*m.b65*m.b149 + m.b66*m.b69 + 2*m.b66*m.b72
                        + 3*m.b66*m.b75 + 4*m.b66*m.b78 + 5*m.b66*m.b81 + 6*m.b66*m.b84 + 7*m.b66*m.b87 + 8*m.b66*m.b90
                        + 9*m.b66*m.b93 + 10*m.b66*m.b96 + 11*m.b66*m.b99 + 12*m.b66*m.b102 + 13*m.b66*m.b105 + 14*m.b66
                       *m.b108 + 15*m.b66*m.b111 + 16*m.b66*m.b114 + 17*m.b66*m.b117 + 18*m.b66*m.b120 + 19*m.b66*m.b123
                        + 20*m.b66*m.b126 + 21*m.b66*m.b129 + 22*m.b66*m.b132 + 23*m.b66*m.b135 + 24*m.b66*m.b138 + 25*
                       m.b66*m.b141 + 26*m.b66*m.b144 + 27*m.b66*m.b147 + 28*m.b66*m.b150 + m.b67*m.b70 + 2*m.b67*m.b73
                        + 3*m.b67*m.b76 + 4*m.b67*m.b79 + 5*m.b67*m.b82 + 6*m.b67*m.b85 + 7*m.b67*m.b88 + 8*m.b67*m.b91
                        + 9*m.b67*m.b94 + 10*m.b67*m.b97 + 11*m.b67*m.b100 + 12*m.b67*m.b103 + 13*m.b67*m.b106 + 14*
                       m.b67*m.b109 + 15*m.b67*m.b112 + 16*m.b67*m.b115 + 17*m.b67*m.b118 + 18*m.b67*m.b121 + 19*m.b67*
                       m.b124 + 20*m.b67*m.b127 + 21*m.b67*m.b130 + 22*m.b67*m.b133 + 23*m.b67*m.b136 + 24*m.b67*m.b139
                        + 25*m.b67*m.b142 + 26*m.b67*m.b145 + 27*m.b67*m.b148 + m.b68*m.b71 + 2*m.b68*m.b74 + 3*m.b68*
                       m.b77 + 4*m.b68*m.b80 + 5*m.b68*m.b83 + 6*m.b68*m.b86 + 7*m.b68*m.b89 + 8*m.b68*m.b92 + 9*m.b68*
                       m.b95 + 10*m.b68*m.b98 + 11*m.b68*m.b101 + 12*m.b68*m.b104 + 13*m.b68*m.b107 + 14*m.b68*m.b110 + 
                       15*m.b68*m.b113 + 16*m.b68*m.b116 + 17*m.b68*m.b119 + 18*m.b68*m.b122 + 19*m.b68*m.b125 + 20*
                       m.b68*m.b128 + 21*m.b68*m.b131 + 22*m.b68*m.b134 + 23*m.b68*m.b137 + 24*m.b68*m.b140 + 25*m.b68*
                       m.b143 + 26*m.b68*m.b146 + 27*m.b68*m.b149 + m.b69*m.b72 + 2*m.b69*m.b75 + 3*m.b69*m.b78 + 4*
                       m.b69*m.b81 + 5*m.b69*m.b84 + 6*m.b69*m.b87 + 7*m.b69*m.b90 + 8*m.b69*m.b93 + 9*m.b69*m.b96 + 10*
                       m.b69*m.b99 + 11*m.b69*m.b102 + 12*m.b69*m.b105 + 13*m.b69*m.b108 + 14*m.b69*m.b111 + 15*m.b69*
                       m.b114 + 16*m.b69*m.b117 + 17*m.b69*m.b120 + 18*m.b69*m.b123 + 19*m.b69*m.b126 + 20*m.b69*m.b129
                        + 21*m.b69*m.b132 + 22*m.b69*m.b135 + 23*m.b69*m.b138 + 24*m.b69*m.b141 + 25*m.b69*m.b144 + 26*
                       m.b69*m.b147 + 27*m.b69*m.b150 + m.b70*m.b73 + 2*m.b70*m.b76 + 3*m.b70*m.b79 + 4*m.b70*m.b82 + 5*
                       m.b70*m.b85 + 6*m.b70*m.b88 + 7*m.b70*m.b91 + 8*m.b70*m.b94 + 9*m.b70*m.b97 + 10*m.b70*m.b100 + 
                       11*m.b70*m.b103 + 12*m.b70*m.b106 + 13*m.b70*m.b109 + 14*m.b70*m.b112 + 15*m.b70*m.b115 + 16*
                       m.b70*m.b118 + 17*m.b70*m.b121 + 18*m.b70*m.b124 + 19*m.b70*m.b127 + 20*m.b70*m.b130 + 21*m.b70*
                       m.b133 + 22*m.b70*m.b136 + 23*m.b70*m.b139 + 24*m.b70*m.b142 + 25*m.b70*m.b145 + 26*m.b70*m.b148
                        + m.b71*m.b74 + 2*m.b71*m.b77 + 3*m.b71*m.b80 + 4*m.b71*m.b83 + 5*m.b71*m.b86 + 6*m.b71*m.b89 + 
                       7*m.b71*m.b92 + 8*m.b71*m.b95 + 9*m.b71*m.b98 + 10*m.b71*m.b101 + 11*m.b71*m.b104 + 12*m.b71*
                       m.b107 + 13*m.b71*m.b110 + 14*m.b71*m.b113 + 15*m.b71*m.b116 + 16*m.b71*m.b119 + 17*m.b71*m.b122
                        + 18*m.b71*m.b125 + 19*m.b71*m.b128 + 20*m.b71*m.b131 + 21*m.b71*m.b134 + 22*m.b71*m.b137 + 23*
                       m.b71*m.b140 + 24*m.b71*m.b143 + 25*m.b71*m.b146 + 26*m.b71*m.b149 + m.b72*m.b75 + 2*m.b72*m.b78
                        + 3*m.b72*m.b81 + 4*m.b72*m.b84 + 5*m.b72*m.b87 + 6*m.b72*m.b90 + 7*m.b72*m.b93 + 8*m.b72*m.b96
                        + 9*m.b72*m.b99 + 10*m.b72*m.b102 + 11*m.b72*m.b105 + 12*m.b72*m.b108 + 13*m.b72*m.b111 + 14*
                       m.b72*m.b114 + 15*m.b72*m.b117 + 16*m.b72*m.b120 + 17*m.b72*m.b123 + 18*m.b72*m.b126 + 19*m.b72*
                       m.b129 + 20*m.b72*m.b132 + 21*m.b72*m.b135 + 22*m.b72*m.b138 + 23*m.b72*m.b141 + 24*m.b72*m.b144
                        + 25*m.b72*m.b147 + 26*m.b72*m.b150 + m.b73*m.b76 + 2*m.b73*m.b79 + 3*m.b73*m.b82 + 4*m.b73*
                       m.b85 + 5*m.b73*m.b88 + 6*m.b73*m.b91 + 7*m.b73*m.b94 + 8*m.b73*m.b97 + 9*m.b73*m.b100 + 10*m.b73
                       *m.b103 + 11*m.b73*m.b106 + 12*m.b73*m.b109 + 13*m.b73*m.b112 + 14*m.b73*m.b115 + 15*m.b73*m.b118
                        + 16*m.b73*m.b121 + 17*m.b73*m.b124 + 18*m.b73*m.b127 + 19*m.b73*m.b130 + 20*m.b73*m.b133 + 21*
                       m.b73*m.b136 + 22*m.b73*m.b139 + 23*m.b73*m.b142 + 24*m.b73*m.b145 + 25*m.b73*m.b148 + m.b74*
                       m.b77 + 2*m.b74*m.b80 + 3*m.b74*m.b83 + 4*m.b74*m.b86 + 5*m.b74*m.b89 + 6*m.b74*m.b92 + 7*m.b74*
                       m.b95 + 8*m.b74*m.b98 + 9*m.b74*m.b101 + 10*m.b74*m.b104 + 11*m.b74*m.b107 + 12*m.b74*m.b110 + 13
                       *m.b74*m.b113 + 14*m.b74*m.b116 + 15*m.b74*m.b119 + 16*m.b74*m.b122 + 17*m.b74*m.b125 + 18*m.b74*
                       m.b128 + 19*m.b74*m.b131 + 20*m.b74*m.b134 + 21*m.b74*m.b137 + 22*m.b74*m.b140 + 23*m.b74*m.b143
                        + 24*m.b74*m.b146 + 25*m.b74*m.b149 + m.b75*m.b78 + 2*m.b75*m.b81 + 3*m.b75*m.b84 + 4*m.b75*
                       m.b87 + 5*m.b75*m.b90 + 6*m.b75*m.b93 + 7*m.b75*m.b96 + 8*m.b75*m.b99 + 9*m.b75*m.b102 + 10*m.b75
                       *m.b105 + 11*m.b75*m.b108 + 12*m.b75*m.b111 + 13*m.b75*m.b114 + 14*m.b75*m.b117 + 15*m.b75*m.b120
                        + 16*m.b75*m.b123 + 17*m.b75*m.b126 + 18*m.b75*m.b129 + 19*m.b75*m.b132 + 20*m.b75*m.b135 + 21*
                       m.b75*m.b138 + 22*m.b75*m.b141 + 23*m.b75*m.b144 + 24*m.b75*m.b147 + 25*m.b75*m.b150 + m.b76*
                       m.b79 + 2*m.b76*m.b82 + 3*m.b76*m.b85 + 4*m.b76*m.b88 + 5*m.b76*m.b91 + 6*m.b76*m.b94 + 7*m.b76*
                       m.b97 + 8*m.b76*m.b100 + 9*m.b76*m.b103 + 10*m.b76*m.b106 + 11*m.b76*m.b109 + 12*m.b76*m.b112 + 
                       13*m.b76*m.b115 + 14*m.b76*m.b118 + 15*m.b76*m.b121 + 16*m.b76*m.b124 + 17*m.b76*m.b127 + 18*
                       m.b76*m.b130 + 19*m.b76*m.b133 + 20*m.b76*m.b136 + 21*m.b76*m.b139 + 22*m.b76*m.b142 + 23*m.b76*
                       m.b145 + 24*m.b76*m.b148 + m.b77*m.b80 + 2*m.b77*m.b83 + 3*m.b77*m.b86 + 4*m.b77*m.b89 + 5*m.b77*
                       m.b92 + 6*m.b77*m.b95 + 7*m.b77*m.b98 + 8*m.b77*m.b101 + 9*m.b77*m.b104 + 10*m.b77*m.b107 + 11*
                       m.b77*m.b110 + 12*m.b77*m.b113 + 13*m.b77*m.b116 + 14*m.b77*m.b119 + 15*m.b77*m.b122 + 16*m.b77*
                       m.b125 + 17*m.b77*m.b128 + 18*m.b77*m.b131 + 19*m.b77*m.b134 + 20*m.b77*m.b137 + 21*m.b77*m.b140
                        + 22*m.b77*m.b143 + 23*m.b77*m.b146 + 24*m.b77*m.b149 + m.b78*m.b81 + 2*m.b78*m.b84 + 3*m.b78*
                       m.b87 + 4*m.b78*m.b90 + 5*m.b78*m.b93 + 6*m.b78*m.b96 + 7*m.b78*m.b99 + 8*m.b78*m.b102 + 9*m.b78*
                       m.b105 + 10*m.b78*m.b108 + 11*m.b78*m.b111 + 12*m.b78*m.b114 + 13*m.b78*m.b117 + 14*m.b78*m.b120
                        + 15*m.b78*m.b123 + 16*m.b78*m.b126 + 17*m.b78*m.b129 + 18*m.b78*m.b132 + 19*m.b78*m.b135 + 20*
                       m.b78*m.b138 + 21*m.b78*m.b141 + 22*m.b78*m.b144 + 23*m.b78*m.b147 + 24*m.b78*m.b150 + m.b79*
                       m.b82 + 2*m.b79*m.b85 + 3*m.b79*m.b88 + 4*m.b79*m.b91 + 5*m.b79*m.b94 + 6*m.b79*m.b97 + 7*m.b79*
                       m.b100 + 8*m.b79*m.b103 + 9*m.b79*m.b106 + 10*m.b79*m.b109 + 11*m.b79*m.b112 + 12*m.b79*m.b115 + 
                       13*m.b79*m.b118 + 14*m.b79*m.b121 + 15*m.b79*m.b124 + 16*m.b79*m.b127 + 17*m.b79*m.b130 + 18*
                       m.b79*m.b133 + 19*m.b79*m.b136 + 20*m.b79*m.b139 + 21*m.b79*m.b142 + 22*m.b79*m.b145 + 23*m.b79*
                       m.b148 + m.b80*m.b83 + 2*m.b80*m.b86 + 3*m.b80*m.b89 + 4*m.b80*m.b92 + 5*m.b80*m.b95 + 6*m.b80*
                       m.b98 + 7*m.b80*m.b101 + 8*m.b80*m.b104 + 9*m.b80*m.b107 + 10*m.b80*m.b110 + 11*m.b80*m.b113 + 12
                       *m.b80*m.b116 + 13*m.b80*m.b119 + 14*m.b80*m.b122 + 15*m.b80*m.b125 + 16*m.b80*m.b128 + 17*m.b80*
                       m.b131 + 18*m.b80*m.b134 + 19*m.b80*m.b137 + 20*m.b80*m.b140 + 21*m.b80*m.b143 + 22*m.b80*m.b146
                        + 23*m.b80*m.b149 + m.b81*m.b84 + 2*m.b81*m.b87 + 3*m.b81*m.b90 + 4*m.b81*m.b93 + 5*m.b81*m.b96
                        + 6*m.b81*m.b99 + 7*m.b81*m.b102 + 8*m.b81*m.b105 + 9*m.b81*m.b108 + 10*m.b81*m.b111 + 11*m.b81*
                       m.b114 + 12*m.b81*m.b117 + 13*m.b81*m.b120 + 14*m.b81*m.b123 + 15*m.b81*m.b126 + 16*m.b81*m.b129
                        + 17*m.b81*m.b132 + 18*m.b81*m.b135 + 19*m.b81*m.b138 + 20*m.b81*m.b141 + 21*m.b81*m.b144 + 22*
                       m.b81*m.b147 + 23*m.b81*m.b150 + m.b82*m.b85 + 2*m.b82*m.b88 + 3*m.b82*m.b91 + 4*m.b82*m.b94 + 5*
                       m.b82*m.b97 + 6*m.b82*m.b100 + 7*m.b82*m.b103 + 8*m.b82*m.b106 + 9*m.b82*m.b109 + 10*m.b82*m.b112
                        + 11*m.b82*m.b115 + 12*m.b82*m.b118 + 13*m.b82*m.b121 + 14*m.b82*m.b124 + 15*m.b82*m.b127 + 16*
                       m.b82*m.b130 + 17*m.b82*m.b133 + 18*m.b82*m.b136 + 19*m.b82*m.b139 + 20*m.b82*m.b142 + 21*m.b82*
                       m.b145 + 22*m.b82*m.b148 + m.b83*m.b86 + 2*m.b83*m.b89 + 3*m.b83*m.b92 + 4*m.b83*m.b95 + 5*m.b83*
                       m.b98 + 6*m.b83*m.b101 + 7*m.b83*m.b104 + 8*m.b83*m.b107 + 9*m.b83*m.b110 + 10*m.b83*m.b113 + 11*
                       m.b83*m.b116 + 12*m.b83*m.b119 + 13*m.b83*m.b122 + 14*m.b83*m.b125 + 15*m.b83*m.b128 + 16*m.b83*
                       m.b131 + 17*m.b83*m.b134 + 18*m.b83*m.b137 + 19*m.b83*m.b140 + 20*m.b83*m.b143 + 21*m.b83*m.b146
                        + 22*m.b83*m.b149 + m.b84*m.b87 + 2*m.b84*m.b90 + 3*m.b84*m.b93 + 4*m.b84*m.b96 + 5*m.b84*m.b99
                        + 6*m.b84*m.b102 + 7*m.b84*m.b105 + 8*m.b84*m.b108 + 9*m.b84*m.b111 + 10*m.b84*m.b114 + 11*m.b84
                       *m.b117 + 12*m.b84*m.b120 + 13*m.b84*m.b123 + 14*m.b84*m.b126 + 15*m.b84*m.b129 + 16*m.b84*m.b132
                        + 17*m.b84*m.b135 + 18*m.b84*m.b138 + 19*m.b84*m.b141 + 20*m.b84*m.b144 + 21*m.b84*m.b147 + 22*
                       m.b84*m.b150 + m.b85*m.b88 + 2*m.b85*m.b91 + 3*m.b85*m.b94 + 4*m.b85*m.b97 + 5*m.b85*m.b100 + 6*
                       m.b85*m.b103 + 7*m.b85*m.b106 + 8*m.b85*m.b109 + 9*m.b85*m.b112 + 10*m.b85*m.b115 + 11*m.b85*
                       m.b118 + 12*m.b85*m.b121 + 13*m.b85*m.b124 + 14*m.b85*m.b127 + 15*m.b85*m.b130 + 16*m.b85*m.b133
                        + 17*m.b85*m.b136 + 18*m.b85*m.b139 + 19*m.b85*m.b142 + 20*m.b85*m.b145 + 21*m.b85*m.b148 + 
                       m.b86*m.b89 + 2*m.b86*m.b92 + 3*m.b86*m.b95 + 4*m.b86*m.b98 + 5*m.b86*m.b101 + 6*m.b86*m.b104 + 7
                       *m.b86*m.b107 + 8*m.b86*m.b110 + 9*m.b86*m.b113 + 10*m.b86*m.b116 + 11*m.b86*m.b119 + 12*m.b86*
                       m.b122 + 13*m.b86*m.b125 + 14*m.b86*m.b128 + 15*m.b86*m.b131 + 16*m.b86*m.b134 + 17*m.b86*m.b137
                        + 18*m.b86*m.b140 + 19*m.b86*m.b143 + 20*m.b86*m.b146 + 21*m.b86*m.b149 + m.b87*m.b90 + 2*m.b87*
                       m.b93 + 3*m.b87*m.b96 + 4*m.b87*m.b99 + 5*m.b87*m.b102 + 6*m.b87*m.b105 + 7*m.b87*m.b108 + 8*
                       m.b87*m.b111 + 9*m.b87*m.b114 + 10*m.b87*m.b117 + 11*m.b87*m.b120 + 12*m.b87*m.b123 + 13*m.b87*
                       m.b126 + 14*m.b87*m.b129 + 15*m.b87*m.b132 + 16*m.b87*m.b135 + 17*m.b87*m.b138 + 18*m.b87*m.b141
                        + 19*m.b87*m.b144 + 20*m.b87*m.b147 + 21*m.b87*m.b150 + m.b88*m.b91 + 2*m.b88*m.b94 + 3*m.b88*
                       m.b97 + 4*m.b88*m.b100 + 5*m.b88*m.b103 + 6*m.b88*m.b106 + 7*m.b88*m.b109 + 8*m.b88*m.b112 + 9*
                       m.b88*m.b115 + 10*m.b88*m.b118 + 11*m.b88*m.b121 + 12*m.b88*m.b124 + 13*m.b88*m.b127 + 14*m.b88*
                       m.b130 + 15*m.b88*m.b133 + 16*m.b88*m.b136 + 17*m.b88*m.b139 + 18*m.b88*m.b142 + 19*m.b88*m.b145
                        + 20*m.b88*m.b148 + m.b89*m.b92 + 2*m.b89*m.b95 + 3*m.b89*m.b98 + 4*m.b89*m.b101 + 5*m.b89*
                       m.b104 + 6*m.b89*m.b107 + 7*m.b89*m.b110 + 8*m.b89*m.b113 + 9*m.b89*m.b116 + 10*m.b89*m.b119 + 11
                       *m.b89*m.b122 + 12*m.b89*m.b125 + 13*m.b89*m.b128 + 14*m.b89*m.b131 + 15*m.b89*m.b134 + 16*m.b89*
                       m.b137 + 17*m.b89*m.b140 + 18*m.b89*m.b143 + 19*m.b89*m.b146 + 20*m.b89*m.b149 + m.b90*m.b93 + 2*
                       m.b90*m.b96 + 3*m.b90*m.b99 + 4*m.b90*m.b102 + 5*m.b90*m.b105 + 6*m.b90*m.b108 + 7*m.b90*m.b111
                        + 8*m.b90*m.b114 + 9*m.b90*m.b117 + 10*m.b90*m.b120 + 11*m.b90*m.b123 + 12*m.b90*m.b126 + 13*
                       m.b90*m.b129 + 14*m.b90*m.b132 + 15*m.b90*m.b135 + 16*m.b90*m.b138 + 17*m.b90*m.b141 + 18*m.b90*
                       m.b144 + 19*m.b90*m.b147 + 20*m.b90*m.b150 + m.b91*m.b94 + 2*m.b91*m.b97 + 3*m.b91*m.b100 + 4*
                       m.b91*m.b103 + 5*m.b91*m.b106 + 6*m.b91*m.b109 + 7*m.b91*m.b112 + 8*m.b91*m.b115 + 9*m.b91*m.b118
                        + 10*m.b91*m.b121 + 11*m.b91*m.b124 + 12*m.b91*m.b127 + 13*m.b91*m.b130 + 14*m.b91*m.b133 + 15*
                       m.b91*m.b136 + 16*m.b91*m.b139 + 17*m.b91*m.b142 + 18*m.b91*m.b145 + 19*m.b91*m.b148 + m.b92*
                       m.b95 + 2*m.b92*m.b98 + 3*m.b92*m.b101 + 4*m.b92*m.b104 + 5*m.b92*m.b107 + 6*m.b92*m.b110 + 7*
                       m.b92*m.b113 + 8*m.b92*m.b116 + 9*m.b92*m.b119 + 10*m.b92*m.b122 + 11*m.b92*m.b125 + 12*m.b92*
                       m.b128 + 13*m.b92*m.b131 + 14*m.b92*m.b134 + 15*m.b92*m.b137 + 16*m.b92*m.b140 + 17*m.b92*m.b143
                        + 18*m.b92*m.b146 + 19*m.b92*m.b149 + m.b93*m.b96 + 2*m.b93*m.b99 + 3*m.b93*m.b102 + 4*m.b93*
                       m.b105 + 5*m.b93*m.b108 + 6*m.b93*m.b111 + 7*m.b93*m.b114 + 8*m.b93*m.b117 + 9*m.b93*m.b120 + 10*
                       m.b93*m.b123 + 11*m.b93*m.b126 + 12*m.b93*m.b129 + 13*m.b93*m.b132 + 14*m.b93*m.b135 + 15*m.b93*
                       m.b138 + 16*m.b93*m.b141 + 17*m.b93*m.b144 + 18*m.b93*m.b147 + 19*m.b93*m.b150 + m.b94*m.b97 + 2*
                       m.b94*m.b100 + 3*m.b94*m.b103 + 4*m.b94*m.b106 + 5*m.b94*m.b109 + 6*m.b94*m.b112 + 7*m.b94*m.b115
                        + 8*m.b94*m.b118 + 9*m.b94*m.b121 + 10*m.b94*m.b124 + 11*m.b94*m.b127 + 12*m.b94*m.b130 + 13*
                       m.b94*m.b133 + 14*m.b94*m.b136 + 15*m.b94*m.b139 + 16*m.b94*m.b142 + 17*m.b94*m.b145 + 18*m.b94*
                       m.b148 + m.b95*m.b98 + 2*m.b95*m.b101 + 3*m.b95*m.b104 + 4*m.b95*m.b107 + 5*m.b95*m.b110 + 6*
                       m.b95*m.b113 + 7*m.b95*m.b116 + 8*m.b95*m.b119 + 9*m.b95*m.b122 + 10*m.b95*m.b125 + 11*m.b95*
                       m.b128 + 12*m.b95*m.b131 + 13*m.b95*m.b134 + 14*m.b95*m.b137 + 15*m.b95*m.b140 + 16*m.b95*m.b143
                        + 17*m.b95*m.b146 + 18*m.b95*m.b149 + m.b96*m.b99 + 2*m.b96*m.b102 + 3*m.b96*m.b105 + 4*m.b96*
                       m.b108 + 5*m.b96*m.b111 + 6*m.b96*m.b114 + 7*m.b96*m.b117 + 8*m.b96*m.b120 + 9*m.b96*m.b123 + 10*
                       m.b96*m.b126 + 11*m.b96*m.b129 + 12*m.b96*m.b132 + 13*m.b96*m.b135 + 14*m.b96*m.b138 + 15*m.b96*
                       m.b141 + 16*m.b96*m.b144 + 17*m.b96*m.b147 + 18*m.b96*m.b150 + m.b97*m.b100 + 2*m.b97*m.b103 + 3*
                       m.b97*m.b106 + 4*m.b97*m.b109 + 5*m.b97*m.b112 + 6*m.b97*m.b115 + 7*m.b97*m.b118 + 8*m.b97*m.b121
                        + 9*m.b97*m.b124 + 10*m.b97*m.b127 + 11*m.b97*m.b130 + 12*m.b97*m.b133 + 13*m.b97*m.b136 + 14*
                       m.b97*m.b139 + 15*m.b97*m.b142 + 16*m.b97*m.b145 + 17*m.b97*m.b148 + m.b98*m.b101 + 2*m.b98*
                       m.b104 + 3*m.b98*m.b107 + 4*m.b98*m.b110 + 5*m.b98*m.b113 + 6*m.b98*m.b116 + 7*m.b98*m.b119 + 8*
                       m.b98*m.b122 + 9*m.b98*m.b125 + 10*m.b98*m.b128 + 11*m.b98*m.b131 + 12*m.b98*m.b134 + 13*m.b98*
                       m.b137 + 14*m.b98*m.b140 + 15*m.b98*m.b143 + 16*m.b98*m.b146 + 17*m.b98*m.b149 + m.b99*m.b102 + 2
                       *m.b99*m.b105 + 3*m.b99*m.b108 + 4*m.b99*m.b111 + 5*m.b99*m.b114 + 6*m.b99*m.b117 + 7*m.b99*
                       m.b120 + 8*m.b99*m.b123 + 9*m.b99*m.b126 + 10*m.b99*m.b129 + 11*m.b99*m.b132 + 12*m.b99*m.b135 + 
                       13*m.b99*m.b138 + 14*m.b99*m.b141 + 15*m.b99*m.b144 + 16*m.b99*m.b147 + 17*m.b99*m.b150 + m.b100*
                       m.b103 + 2*m.b100*m.b106 + 3*m.b100*m.b109 + 4*m.b100*m.b112 + 5*m.b100*m.b115 + 6*m.b100*m.b118
                        + 7*m.b100*m.b121 + 8*m.b100*m.b124 + 9*m.b100*m.b127 + 10*m.b100*m.b130 + 11*m.b100*m.b133 + 12
                       *m.b100*m.b136 + 13*m.b100*m.b139 + 14*m.b100*m.b142 + 15*m.b100*m.b145 + 16*m.b100*m.b148 + 
                       m.b101*m.b104 + 2*m.b101*m.b107 + 3*m.b101*m.b110 + 4*m.b101*m.b113 + 5*m.b101*m.b116 + 6*m.b101*
                       m.b119 + 7*m.b101*m.b122 + 8*m.b101*m.b125 + 9*m.b101*m.b128 + 10*m.b101*m.b131 + 11*m.b101*
                       m.b134 + 12*m.b101*m.b137 + 13*m.b101*m.b140 + 14*m.b101*m.b143 + 15*m.b101*m.b146 + 16*m.b101*
                       m.b149 + m.b102*m.b105 + 2*m.b102*m.b108 + 3*m.b102*m.b111 + 4*m.b102*m.b114 + 5*m.b102*m.b117 + 
                       6*m.b102*m.b120 + 7*m.b102*m.b123 + 8*m.b102*m.b126 + 9*m.b102*m.b129 + 10*m.b102*m.b132 + 11*
                       m.b102*m.b135 + 12*m.b102*m.b138 + 13*m.b102*m.b141 + 14*m.b102*m.b144 + 15*m.b102*m.b147 + 16*
                       m.b102*m.b150 + m.b103*m.b106 + 2*m.b103*m.b109 + 3*m.b103*m.b112 + 4*m.b103*m.b115 + 5*m.b103*
                       m.b118 + 6*m.b103*m.b121 + 7*m.b103*m.b124 + 8*m.b103*m.b127 + 9*m.b103*m.b130 + 10*m.b103*m.b133
                        + 11*m.b103*m.b136 + 12*m.b103*m.b139 + 13*m.b103*m.b142 + 14*m.b103*m.b145 + 15*m.b103*m.b148
                        + m.b104*m.b107 + 2*m.b104*m.b110 + 3*m.b104*m.b113 + 4*m.b104*m.b116 + 5*m.b104*m.b119 + 6*
                       m.b104*m.b122 + 7*m.b104*m.b125 + 8*m.b104*m.b128 + 9*m.b104*m.b131 + 10*m.b104*m.b134 + 11*
                       m.b104*m.b137 + 12*m.b104*m.b140 + 13*m.b104*m.b143 + 14*m.b104*m.b146 + 15*m.b104*m.b149 + 
                       m.b105*m.b108 + 2*m.b105*m.b111 + 3*m.b105*m.b114 + 4*m.b105*m.b117 + 5*m.b105*m.b120 + 6*m.b105*
                       m.b123 + 7*m.b105*m.b126 + 8*m.b105*m.b129 + 9*m.b105*m.b132 + 10*m.b105*m.b135 + 11*m.b105*
                       m.b138 + 12*m.b105*m.b141 + 13*m.b105*m.b144 + 14*m.b105*m.b147 + 15*m.b105*m.b150 + m.b106*
                       m.b109 + 2*m.b106*m.b112 + 3*m.b106*m.b115 + 4*m.b106*m.b118 + 5*m.b106*m.b121 + 6*m.b106*m.b124
                        + 7*m.b106*m.b127 + 8*m.b106*m.b130 + 9*m.b106*m.b133 + 10*m.b106*m.b136 + 11*m.b106*m.b139 + 12
                       *m.b106*m.b142 + 13*m.b106*m.b145 + 14*m.b106*m.b148 + m.b107*m.b110 + 2*m.b107*m.b113 + 3*m.b107
                       *m.b116 + 4*m.b107*m.b119 + 5*m.b107*m.b122 + 6*m.b107*m.b125 + 7*m.b107*m.b128 + 8*m.b107*m.b131
                        + 9*m.b107*m.b134 + 10*m.b107*m.b137 + 11*m.b107*m.b140 + 12*m.b107*m.b143 + 13*m.b107*m.b146 + 
                       14*m.b107*m.b149 + m.b108*m.b111 + 2*m.b108*m.b114 + 3*m.b108*m.b117 + 4*m.b108*m.b120 + 5*m.b108
                       *m.b123 + 6*m.b108*m.b126 + 7*m.b108*m.b129 + 8*m.b108*m.b132 + 9*m.b108*m.b135 + 10*m.b108*
                       m.b138 + 11*m.b108*m.b141 + 12*m.b108*m.b144 + 13*m.b108*m.b147 + 14*m.b108*m.b150 + m.b109*
                       m.b112 + 2*m.b109*m.b115 + 3*m.b109*m.b118 + 4*m.b109*m.b121 + 5*m.b109*m.b124 + 6*m.b109*m.b127
                        + 7*m.b109*m.b130 + 8*m.b109*m.b133 + 9*m.b109*m.b136 + 10*m.b109*m.b139 + 11*m.b109*m.b142 + 12
                       *m.b109*m.b145 + 13*m.b109*m.b148 + m.b110*m.b113 + 2*m.b110*m.b116 + 3*m.b110*m.b119 + 4*m.b110*
                       m.b122 + 5*m.b110*m.b125 + 6*m.b110*m.b128 + 7*m.b110*m.b131 + 8*m.b110*m.b134 + 9*m.b110*m.b137
                        + 10*m.b110*m.b140 + 11*m.b110*m.b143 + 12*m.b110*m.b146 + 13*m.b110*m.b149 + m.b111*m.b114 + 2*
                       m.b111*m.b117 + 3*m.b111*m.b120 + 4*m.b111*m.b123 + 5*m.b111*m.b126 + 6*m.b111*m.b129 + 7*m.b111*
                       m.b132 + 8*m.b111*m.b135 + 9*m.b111*m.b138 + 10*m.b111*m.b141 + 11*m.b111*m.b144 + 12*m.b111*
                       m.b147 + 13*m.b111*m.b150 + m.b112*m.b115 + 2*m.b112*m.b118 + 3*m.b112*m.b121 + 4*m.b112*m.b124
                        + 5*m.b112*m.b127 + 6*m.b112*m.b130 + 7*m.b112*m.b133 + 8*m.b112*m.b136 + 9*m.b112*m.b139 + 10*
                       m.b112*m.b142 + 11*m.b112*m.b145 + 12*m.b112*m.b148 + m.b113*m.b116 + 2*m.b113*m.b119 + 3*m.b113*
                       m.b122 + 4*m.b113*m.b125 + 5*m.b113*m.b128 + 6*m.b113*m.b131 + 7*m.b113*m.b134 + 8*m.b113*m.b137
                        + 9*m.b113*m.b140 + 10*m.b113*m.b143 + 11*m.b113*m.b146 + 12*m.b113*m.b149 + m.b114*m.b117 + 2*
                       m.b114*m.b120 + 3*m.b114*m.b123 + 4*m.b114*m.b126 + 5*m.b114*m.b129 + 6*m.b114*m.b132 + 7*m.b114*
                       m.b135 + 8*m.b114*m.b138 + 9*m.b114*m.b141 + 10*m.b114*m.b144 + 11*m.b114*m.b147 + 12*m.b114*
                       m.b150 + m.b115*m.b118 + 2*m.b115*m.b121 + 3*m.b115*m.b124 + 4*m.b115*m.b127 + 5*m.b115*m.b130 + 
                       6*m.b115*m.b133 + 7*m.b115*m.b136 + 8*m.b115*m.b139 + 9*m.b115*m.b142 + 10*m.b115*m.b145 + 11*
                       m.b115*m.b148 + m.b116*m.b119 + 2*m.b116*m.b122 + 3*m.b116*m.b125 + 4*m.b116*m.b128 + 5*m.b116*
                       m.b131 + 6*m.b116*m.b134 + 7*m.b116*m.b137 + 8*m.b116*m.b140 + 9*m.b116*m.b143 + 10*m.b116*m.b146
                        + 11*m.b116*m.b149 + m.b117*m.b120 + 2*m.b117*m.b123 + 3*m.b117*m.b126 + 4*m.b117*m.b129 + 5*
                       m.b117*m.b132 + 6*m.b117*m.b135 + 7*m.b117*m.b138 + 8*m.b117*m.b141 + 9*m.b117*m.b144 + 10*m.b117
                       *m.b147 + 11*m.b117*m.b150 + m.b118*m.b121 + 2*m.b118*m.b124 + 3*m.b118*m.b127 + 4*m.b118*m.b130
                        + 5*m.b118*m.b133 + 6*m.b118*m.b136 + 7*m.b118*m.b139 + 8*m.b118*m.b142 + 9*m.b118*m.b145 + 10*
                       m.b118*m.b148 + m.b119*m.b122 + 2*m.b119*m.b125 + 3*m.b119*m.b128 + 4*m.b119*m.b131 + 5*m.b119*
                       m.b134 + 6*m.b119*m.b137 + 7*m.b119*m.b140 + 8*m.b119*m.b143 + 9*m.b119*m.b146 + 10*m.b119*m.b149
                        + m.b120*m.b123 + 2*m.b120*m.b126 + 3*m.b120*m.b129 + 4*m.b120*m.b132 + 5*m.b120*m.b135 + 6*
                       m.b120*m.b138 + 7*m.b120*m.b141 + 8*m.b120*m.b144 + 9*m.b120*m.b147 + 10*m.b120*m.b150 + m.b121*
                       m.b124 + 2*m.b121*m.b127 + 3*m.b121*m.b130 + 4*m.b121*m.b133 + 5*m.b121*m.b136 + 6*m.b121*m.b139
                        + 7*m.b121*m.b142 + 8*m.b121*m.b145 + 9*m.b121*m.b148 + m.b122*m.b125 + 2*m.b122*m.b128 + 3*
                       m.b122*m.b131 + 4*m.b122*m.b134 + 5*m.b122*m.b137 + 6*m.b122*m.b140 + 7*m.b122*m.b143 + 8*m.b122*
                       m.b146 + 9*m.b122*m.b149 + m.b123*m.b126 + 2*m.b123*m.b129 + 3*m.b123*m.b132 + 4*m.b123*m.b135 + 
                       5*m.b123*m.b138 + 6*m.b123*m.b141 + 7*m.b123*m.b144 + 8*m.b123*m.b147 + 9*m.b123*m.b150 + m.b124*
                       m.b127 + 2*m.b124*m.b130 + 3*m.b124*m.b133 + 4*m.b124*m.b136 + 5*m.b124*m.b139 + 6*m.b124*m.b142
                        + 7*m.b124*m.b145 + 8*m.b124*m.b148 + m.b125*m.b128 + 2*m.b125*m.b131 + 3*m.b125*m.b134 + 4*
                       m.b125*m.b137 + 5*m.b125*m.b140 + 6*m.b125*m.b143 + 7*m.b125*m.b146 + 8*m.b125*m.b149 + m.b126*
                       m.b129 + 2*m.b126*m.b132 + 3*m.b126*m.b135 + 4*m.b126*m.b138 + 5*m.b126*m.b141 + 6*m.b126*m.b144
                        + 7*m.b126*m.b147 + 8*m.b126*m.b150 + m.b127*m.b130 + 2*m.b127*m.b133 + 3*m.b127*m.b136 + 4*
                       m.b127*m.b139 + 5*m.b127*m.b142 + 6*m.b127*m.b145 + 7*m.b127*m.b148 + m.b128*m.b131 + 2*m.b128*
                       m.b134 + 3*m.b128*m.b137 + 4*m.b128*m.b140 + 5*m.b128*m.b143 + 6*m.b128*m.b146 + 7*m.b128*m.b149
                        + m.b129*m.b132 + 2*m.b129*m.b135 + 3*m.b129*m.b138 + 4*m.b129*m.b141 + 5*m.b129*m.b144 + 6*
                       m.b129*m.b147 + 7*m.b129*m.b150 + m.b130*m.b133 + 2*m.b130*m.b136 + 3*m.b130*m.b139 + 4*m.b130*
                       m.b142 + 5*m.b130*m.b145 + 6*m.b130*m.b148 + m.b131*m.b134 + 2*m.b131*m.b137 + 3*m.b131*m.b140 + 
                       4*m.b131*m.b143 + 5*m.b131*m.b146 + 6*m.b131*m.b149 + m.b132*m.b135 + 2*m.b132*m.b138 + 3*m.b132*
                       m.b141 + 4*m.b132*m.b144 + 5*m.b132*m.b147 + 6*m.b132*m.b150 + m.b133*m.b136 + 2*m.b133*m.b139 + 
                       3*m.b133*m.b142 + 4*m.b133*m.b145 + 5*m.b133*m.b148 + m.b134*m.b137 + 2*m.b134*m.b140 + 3*m.b134*
                       m.b143 + 4*m.b134*m.b146 + 5*m.b134*m.b149 + m.b135*m.b138 + 2*m.b135*m.b141 + 3*m.b135*m.b144 + 
                       4*m.b135*m.b147 + 5*m.b135*m.b150 + m.b136*m.b139 + 2*m.b136*m.b142 + 3*m.b136*m.b145 + 4*m.b136*
                       m.b148 + m.b137*m.b140 + 2*m.b137*m.b143 + 3*m.b137*m.b146 + 4*m.b137*m.b149 + m.b138*m.b141 + 2*
                       m.b138*m.b144 + 3*m.b138*m.b147 + 4*m.b138*m.b150 + m.b139*m.b142 + 2*m.b139*m.b145 + 3*m.b139*
                       m.b148 + m.b140*m.b143 + 2*m.b140*m.b146 + 3*m.b140*m.b149 + m.b141*m.b144 + 2*m.b141*m.b147 + 3*
                       m.b141*m.b150 + m.b142*m.b145 + 2*m.b142*m.b148 + m.b143*m.b146 + 2*m.b143*m.b149 + m.b144*m.b147
                        + 2*m.b144*m.b150 + m.b145*m.b148 + m.b146*m.b149 + m.b147*m.b150, sense=minimize)

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

m.c49 = Constraint(expr=   m.b145 + m.b146 + m.b147 == 1)

m.c50 = Constraint(expr=   m.b148 + m.b149 + m.b150 == 1)
