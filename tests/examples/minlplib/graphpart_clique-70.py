#  MINLP written by GAMS Convert at 04/21/18 13:52:23
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         71       71        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        211        1      210        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        421      211      210        0
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
m.b151 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b152 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b153 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b154 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b155 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b156 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b157 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b158 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b159 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b160 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b161 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b162 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b163 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b164 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b165 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b166 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b167 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b168 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b169 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b170 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b171 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b172 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b173 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b174 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b175 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b176 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b177 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b178 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b179 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b180 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b181 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b182 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b183 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b184 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b185 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b186 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b187 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b188 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b189 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b190 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b191 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b192 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b193 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b194 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b195 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b196 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b197 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b198 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b199 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b200 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b201 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b202 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b203 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b204 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b205 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b206 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b207 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b208 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b209 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b210 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=m.b1*m.b4 + 2*m.b1*m.b7 + 3*m.b1*m.b10 + 4*m.b1*m.b13 + 5*m.b1*m.b16 + 6*m.b1*m.b19 + 7*m.b1*
                       m.b22 + 8*m.b1*m.b25 + 9*m.b1*m.b28 + 10*m.b1*m.b31 + 11*m.b1*m.b34 + 12*m.b1*m.b37 + 13*m.b1*
                       m.b40 + 14*m.b1*m.b43 + 15*m.b1*m.b46 + 16*m.b1*m.b49 + 17*m.b1*m.b52 + 18*m.b1*m.b55 + 19*m.b1*
                       m.b58 + 20*m.b1*m.b61 + 21*m.b1*m.b64 + 22*m.b1*m.b67 + 23*m.b1*m.b70 + 24*m.b1*m.b73 + 25*m.b1*
                       m.b76 + 26*m.b1*m.b79 + 27*m.b1*m.b82 + 28*m.b1*m.b85 + 29*m.b1*m.b88 + 30*m.b1*m.b91 + 31*m.b1*
                       m.b94 + 32*m.b1*m.b97 + 33*m.b1*m.b100 + 34*m.b1*m.b103 + 35*m.b1*m.b106 + 36*m.b1*m.b109 + 37*
                       m.b1*m.b112 + 38*m.b1*m.b115 + 39*m.b1*m.b118 + 40*m.b1*m.b121 + 41*m.b1*m.b124 + 42*m.b1*m.b127
                        + 43*m.b1*m.b130 + 44*m.b1*m.b133 + 45*m.b1*m.b136 + 46*m.b1*m.b139 + 47*m.b1*m.b142 + 48*m.b1*
                       m.b145 + 49*m.b1*m.b148 + 50*m.b1*m.b151 + 51*m.b1*m.b154 + 52*m.b1*m.b157 + 53*m.b1*m.b160 + 54*
                       m.b1*m.b163 + 55*m.b1*m.b166 + 56*m.b1*m.b169 + 57*m.b1*m.b172 + 58*m.b1*m.b175 + 59*m.b1*m.b178
                        + 60*m.b1*m.b181 + 61*m.b1*m.b184 + 62*m.b1*m.b187 + 63*m.b1*m.b190 + 64*m.b1*m.b193 + 65*m.b1*
                       m.b196 + 66*m.b1*m.b199 + 67*m.b1*m.b202 + 68*m.b1*m.b205 + 69*m.b1*m.b208 + m.b2*m.b5 + 2*m.b2*
                       m.b8 + 3*m.b2*m.b11 + 4*m.b2*m.b14 + 5*m.b2*m.b17 + 6*m.b2*m.b20 + 7*m.b2*m.b23 + 8*m.b2*m.b26 + 
                       9*m.b2*m.b29 + 10*m.b2*m.b32 + 11*m.b2*m.b35 + 12*m.b2*m.b38 + 13*m.b2*m.b41 + 14*m.b2*m.b44 + 15
                       *m.b2*m.b47 + 16*m.b2*m.b50 + 17*m.b2*m.b53 + 18*m.b2*m.b56 + 19*m.b2*m.b59 + 20*m.b2*m.b62 + 21*
                       m.b2*m.b65 + 22*m.b2*m.b68 + 23*m.b2*m.b71 + 24*m.b2*m.b74 + 25*m.b2*m.b77 + 26*m.b2*m.b80 + 27*
                       m.b2*m.b83 + 28*m.b2*m.b86 + 29*m.b2*m.b89 + 30*m.b2*m.b92 + 31*m.b2*m.b95 + 32*m.b2*m.b98 + 33*
                       m.b2*m.b101 + 34*m.b2*m.b104 + 35*m.b2*m.b107 + 36*m.b2*m.b110 + 37*m.b2*m.b113 + 38*m.b2*m.b116
                        + 39*m.b2*m.b119 + 40*m.b2*m.b122 + 41*m.b2*m.b125 + 42*m.b2*m.b128 + 43*m.b2*m.b131 + 44*m.b2*
                       m.b134 + 45*m.b2*m.b137 + 46*m.b2*m.b140 + 47*m.b2*m.b143 + 48*m.b2*m.b146 + 49*m.b2*m.b149 + 50*
                       m.b2*m.b152 + 51*m.b2*m.b155 + 52*m.b2*m.b158 + 53*m.b2*m.b161 + 54*m.b2*m.b164 + 55*m.b2*m.b167
                        + 56*m.b2*m.b170 + 57*m.b2*m.b173 + 58*m.b2*m.b176 + 59*m.b2*m.b179 + 60*m.b2*m.b182 + 61*m.b2*
                       m.b185 + 62*m.b2*m.b188 + 63*m.b2*m.b191 + 64*m.b2*m.b194 + 65*m.b2*m.b197 + 66*m.b2*m.b200 + 67*
                       m.b2*m.b203 + 68*m.b2*m.b206 + 69*m.b2*m.b209 + m.b3*m.b6 + 2*m.b3*m.b9 + 3*m.b3*m.b12 + 4*m.b3*
                       m.b15 + 5*m.b3*m.b18 + 6*m.b3*m.b21 + 7*m.b3*m.b24 + 8*m.b3*m.b27 + 9*m.b3*m.b30 + 10*m.b3*m.b33
                        + 11*m.b3*m.b36 + 12*m.b3*m.b39 + 13*m.b3*m.b42 + 14*m.b3*m.b45 + 15*m.b3*m.b48 + 16*m.b3*m.b51
                        + 17*m.b3*m.b54 + 18*m.b3*m.b57 + 19*m.b3*m.b60 + 20*m.b3*m.b63 + 21*m.b3*m.b66 + 22*m.b3*m.b69
                        + 23*m.b3*m.b72 + 24*m.b3*m.b75 + 25*m.b3*m.b78 + 26*m.b3*m.b81 + 27*m.b3*m.b84 + 28*m.b3*m.b87
                        + 29*m.b3*m.b90 + 30*m.b3*m.b93 + 31*m.b3*m.b96 + 32*m.b3*m.b99 + 33*m.b3*m.b102 + 34*m.b3*
                       m.b105 + 35*m.b3*m.b108 + 36*m.b3*m.b111 + 37*m.b3*m.b114 + 38*m.b3*m.b117 + 39*m.b3*m.b120 + 40*
                       m.b3*m.b123 + 41*m.b3*m.b126 + 42*m.b3*m.b129 + 43*m.b3*m.b132 + 44*m.b3*m.b135 + 45*m.b3*m.b138
                        + 46*m.b3*m.b141 + 47*m.b3*m.b144 + 48*m.b3*m.b147 + 49*m.b3*m.b150 + 50*m.b3*m.b153 + 51*m.b3*
                       m.b156 + 52*m.b3*m.b159 + 53*m.b3*m.b162 + 54*m.b3*m.b165 + 55*m.b3*m.b168 + 56*m.b3*m.b171 + 57*
                       m.b3*m.b174 + 58*m.b3*m.b177 + 59*m.b3*m.b180 + 60*m.b3*m.b183 + 61*m.b3*m.b186 + 62*m.b3*m.b189
                        + 63*m.b3*m.b192 + 64*m.b3*m.b195 + 65*m.b3*m.b198 + 66*m.b3*m.b201 + 67*m.b3*m.b204 + 68*m.b3*
                       m.b207 + 69*m.b3*m.b210 + m.b4*m.b7 + 2*m.b4*m.b10 + 3*m.b4*m.b13 + 4*m.b4*m.b16 + 5*m.b4*m.b19
                        + 6*m.b4*m.b22 + 7*m.b4*m.b25 + 8*m.b4*m.b28 + 9*m.b4*m.b31 + 10*m.b4*m.b34 + 11*m.b4*m.b37 + 12
                       *m.b4*m.b40 + 13*m.b4*m.b43 + 14*m.b4*m.b46 + 15*m.b4*m.b49 + 16*m.b4*m.b52 + 17*m.b4*m.b55 + 18*
                       m.b4*m.b58 + 19*m.b4*m.b61 + 20*m.b4*m.b64 + 21*m.b4*m.b67 + 22*m.b4*m.b70 + 23*m.b4*m.b73 + 24*
                       m.b4*m.b76 + 25*m.b4*m.b79 + 26*m.b4*m.b82 + 27*m.b4*m.b85 + 28*m.b4*m.b88 + 29*m.b4*m.b91 + 30*
                       m.b4*m.b94 + 31*m.b4*m.b97 + 32*m.b4*m.b100 + 33*m.b4*m.b103 + 34*m.b4*m.b106 + 35*m.b4*m.b109 + 
                       36*m.b4*m.b112 + 37*m.b4*m.b115 + 38*m.b4*m.b118 + 39*m.b4*m.b121 + 40*m.b4*m.b124 + 41*m.b4*
                       m.b127 + 42*m.b4*m.b130 + 43*m.b4*m.b133 + 44*m.b4*m.b136 + 45*m.b4*m.b139 + 46*m.b4*m.b142 + 47*
                       m.b4*m.b145 + 48*m.b4*m.b148 + 49*m.b4*m.b151 + 50*m.b4*m.b154 + 51*m.b4*m.b157 + 52*m.b4*m.b160
                        + 53*m.b4*m.b163 + 54*m.b4*m.b166 + 55*m.b4*m.b169 + 56*m.b4*m.b172 + 57*m.b4*m.b175 + 58*m.b4*
                       m.b178 + 59*m.b4*m.b181 + 60*m.b4*m.b184 + 61*m.b4*m.b187 + 62*m.b4*m.b190 + 63*m.b4*m.b193 + 64*
                       m.b4*m.b196 + 65*m.b4*m.b199 + 66*m.b4*m.b202 + 67*m.b4*m.b205 + 68*m.b4*m.b208 + m.b5*m.b8 + 2*
                       m.b5*m.b11 + 3*m.b5*m.b14 + 4*m.b5*m.b17 + 5*m.b5*m.b20 + 6*m.b5*m.b23 + 7*m.b5*m.b26 + 8*m.b5*
                       m.b29 + 9*m.b5*m.b32 + 10*m.b5*m.b35 + 11*m.b5*m.b38 + 12*m.b5*m.b41 + 13*m.b5*m.b44 + 14*m.b5*
                       m.b47 + 15*m.b5*m.b50 + 16*m.b5*m.b53 + 17*m.b5*m.b56 + 18*m.b5*m.b59 + 19*m.b5*m.b62 + 20*m.b5*
                       m.b65 + 21*m.b5*m.b68 + 22*m.b5*m.b71 + 23*m.b5*m.b74 + 24*m.b5*m.b77 + 25*m.b5*m.b80 + 26*m.b5*
                       m.b83 + 27*m.b5*m.b86 + 28*m.b5*m.b89 + 29*m.b5*m.b92 + 30*m.b5*m.b95 + 31*m.b5*m.b98 + 32*m.b5*
                       m.b101 + 33*m.b5*m.b104 + 34*m.b5*m.b107 + 35*m.b5*m.b110 + 36*m.b5*m.b113 + 37*m.b5*m.b116 + 38*
                       m.b5*m.b119 + 39*m.b5*m.b122 + 40*m.b5*m.b125 + 41*m.b5*m.b128 + 42*m.b5*m.b131 + 43*m.b5*m.b134
                        + 44*m.b5*m.b137 + 45*m.b5*m.b140 + 46*m.b5*m.b143 + 47*m.b5*m.b146 + 48*m.b5*m.b149 + 49*m.b5*
                       m.b152 + 50*m.b5*m.b155 + 51*m.b5*m.b158 + 52*m.b5*m.b161 + 53*m.b5*m.b164 + 54*m.b5*m.b167 + 55*
                       m.b5*m.b170 + 56*m.b5*m.b173 + 57*m.b5*m.b176 + 58*m.b5*m.b179 + 59*m.b5*m.b182 + 60*m.b5*m.b185
                        + 61*m.b5*m.b188 + 62*m.b5*m.b191 + 63*m.b5*m.b194 + 64*m.b5*m.b197 + 65*m.b5*m.b200 + 66*m.b5*
                       m.b203 + 67*m.b5*m.b206 + 68*m.b5*m.b209 + m.b6*m.b9 + 2*m.b6*m.b12 + 3*m.b6*m.b15 + 4*m.b6*m.b18
                        + 5*m.b6*m.b21 + 6*m.b6*m.b24 + 7*m.b6*m.b27 + 8*m.b6*m.b30 + 9*m.b6*m.b33 + 10*m.b6*m.b36 + 11*
                       m.b6*m.b39 + 12*m.b6*m.b42 + 13*m.b6*m.b45 + 14*m.b6*m.b48 + 15*m.b6*m.b51 + 16*m.b6*m.b54 + 17*
                       m.b6*m.b57 + 18*m.b6*m.b60 + 19*m.b6*m.b63 + 20*m.b6*m.b66 + 21*m.b6*m.b69 + 22*m.b6*m.b72 + 23*
                       m.b6*m.b75 + 24*m.b6*m.b78 + 25*m.b6*m.b81 + 26*m.b6*m.b84 + 27*m.b6*m.b87 + 28*m.b6*m.b90 + 29*
                       m.b6*m.b93 + 30*m.b6*m.b96 + 31*m.b6*m.b99 + 32*m.b6*m.b102 + 33*m.b6*m.b105 + 34*m.b6*m.b108 + 
                       35*m.b6*m.b111 + 36*m.b6*m.b114 + 37*m.b6*m.b117 + 38*m.b6*m.b120 + 39*m.b6*m.b123 + 40*m.b6*
                       m.b126 + 41*m.b6*m.b129 + 42*m.b6*m.b132 + 43*m.b6*m.b135 + 44*m.b6*m.b138 + 45*m.b6*m.b141 + 46*
                       m.b6*m.b144 + 47*m.b6*m.b147 + 48*m.b6*m.b150 + 49*m.b6*m.b153 + 50*m.b6*m.b156 + 51*m.b6*m.b159
                        + 52*m.b6*m.b162 + 53*m.b6*m.b165 + 54*m.b6*m.b168 + 55*m.b6*m.b171 + 56*m.b6*m.b174 + 57*m.b6*
                       m.b177 + 58*m.b6*m.b180 + 59*m.b6*m.b183 + 60*m.b6*m.b186 + 61*m.b6*m.b189 + 62*m.b6*m.b192 + 63*
                       m.b6*m.b195 + 64*m.b6*m.b198 + 65*m.b6*m.b201 + 66*m.b6*m.b204 + 67*m.b6*m.b207 + 68*m.b6*m.b210
                        + m.b7*m.b10 + 2*m.b7*m.b13 + 3*m.b7*m.b16 + 4*m.b7*m.b19 + 5*m.b7*m.b22 + 6*m.b7*m.b25 + 7*m.b7
                       *m.b28 + 8*m.b7*m.b31 + 9*m.b7*m.b34 + 10*m.b7*m.b37 + 11*m.b7*m.b40 + 12*m.b7*m.b43 + 13*m.b7*
                       m.b46 + 14*m.b7*m.b49 + 15*m.b7*m.b52 + 16*m.b7*m.b55 + 17*m.b7*m.b58 + 18*m.b7*m.b61 + 19*m.b7*
                       m.b64 + 20*m.b7*m.b67 + 21*m.b7*m.b70 + 22*m.b7*m.b73 + 23*m.b7*m.b76 + 24*m.b7*m.b79 + 25*m.b7*
                       m.b82 + 26*m.b7*m.b85 + 27*m.b7*m.b88 + 28*m.b7*m.b91 + 29*m.b7*m.b94 + 30*m.b7*m.b97 + 31*m.b7*
                       m.b100 + 32*m.b7*m.b103 + 33*m.b7*m.b106 + 34*m.b7*m.b109 + 35*m.b7*m.b112 + 36*m.b7*m.b115 + 37*
                       m.b7*m.b118 + 38*m.b7*m.b121 + 39*m.b7*m.b124 + 40*m.b7*m.b127 + 41*m.b7*m.b130 + 42*m.b7*m.b133
                        + 43*m.b7*m.b136 + 44*m.b7*m.b139 + 45*m.b7*m.b142 + 46*m.b7*m.b145 + 47*m.b7*m.b148 + 48*m.b7*
                       m.b151 + 49*m.b7*m.b154 + 50*m.b7*m.b157 + 51*m.b7*m.b160 + 52*m.b7*m.b163 + 53*m.b7*m.b166 + 54*
                       m.b7*m.b169 + 55*m.b7*m.b172 + 56*m.b7*m.b175 + 57*m.b7*m.b178 + 58*m.b7*m.b181 + 59*m.b7*m.b184
                        + 60*m.b7*m.b187 + 61*m.b7*m.b190 + 62*m.b7*m.b193 + 63*m.b7*m.b196 + 64*m.b7*m.b199 + 65*m.b7*
                       m.b202 + 66*m.b7*m.b205 + 67*m.b7*m.b208 + m.b8*m.b11 + 2*m.b8*m.b14 + 3*m.b8*m.b17 + 4*m.b8*
                       m.b20 + 5*m.b8*m.b23 + 6*m.b8*m.b26 + 7*m.b8*m.b29 + 8*m.b8*m.b32 + 9*m.b8*m.b35 + 10*m.b8*m.b38
                        + 11*m.b8*m.b41 + 12*m.b8*m.b44 + 13*m.b8*m.b47 + 14*m.b8*m.b50 + 15*m.b8*m.b53 + 16*m.b8*m.b56
                        + 17*m.b8*m.b59 + 18*m.b8*m.b62 + 19*m.b8*m.b65 + 20*m.b8*m.b68 + 21*m.b8*m.b71 + 22*m.b8*m.b74
                        + 23*m.b8*m.b77 + 24*m.b8*m.b80 + 25*m.b8*m.b83 + 26*m.b8*m.b86 + 27*m.b8*m.b89 + 28*m.b8*m.b92
                        + 29*m.b8*m.b95 + 30*m.b8*m.b98 + 31*m.b8*m.b101 + 32*m.b8*m.b104 + 33*m.b8*m.b107 + 34*m.b8*
                       m.b110 + 35*m.b8*m.b113 + 36*m.b8*m.b116 + 37*m.b8*m.b119 + 38*m.b8*m.b122 + 39*m.b8*m.b125 + 40*
                       m.b8*m.b128 + 41*m.b8*m.b131 + 42*m.b8*m.b134 + 43*m.b8*m.b137 + 44*m.b8*m.b140 + 45*m.b8*m.b143
                        + 46*m.b8*m.b146 + 47*m.b8*m.b149 + 48*m.b8*m.b152 + 49*m.b8*m.b155 + 50*m.b8*m.b158 + 51*m.b8*
                       m.b161 + 52*m.b8*m.b164 + 53*m.b8*m.b167 + 54*m.b8*m.b170 + 55*m.b8*m.b173 + 56*m.b8*m.b176 + 57*
                       m.b8*m.b179 + 58*m.b8*m.b182 + 59*m.b8*m.b185 + 60*m.b8*m.b188 + 61*m.b8*m.b191 + 62*m.b8*m.b194
                        + 63*m.b8*m.b197 + 64*m.b8*m.b200 + 65*m.b8*m.b203 + 66*m.b8*m.b206 + 67*m.b8*m.b209 + m.b9*
                       m.b12 + 2*m.b9*m.b15 + 3*m.b9*m.b18 + 4*m.b9*m.b21 + 5*m.b9*m.b24 + 6*m.b9*m.b27 + 7*m.b9*m.b30
                        + 8*m.b9*m.b33 + 9*m.b9*m.b36 + 10*m.b9*m.b39 + 11*m.b9*m.b42 + 12*m.b9*m.b45 + 13*m.b9*m.b48 + 
                       14*m.b9*m.b51 + 15*m.b9*m.b54 + 16*m.b9*m.b57 + 17*m.b9*m.b60 + 18*m.b9*m.b63 + 19*m.b9*m.b66 + 
                       20*m.b9*m.b69 + 21*m.b9*m.b72 + 22*m.b9*m.b75 + 23*m.b9*m.b78 + 24*m.b9*m.b81 + 25*m.b9*m.b84 + 
                       26*m.b9*m.b87 + 27*m.b9*m.b90 + 28*m.b9*m.b93 + 29*m.b9*m.b96 + 30*m.b9*m.b99 + 31*m.b9*m.b102 + 
                       32*m.b9*m.b105 + 33*m.b9*m.b108 + 34*m.b9*m.b111 + 35*m.b9*m.b114 + 36*m.b9*m.b117 + 37*m.b9*
                       m.b120 + 38*m.b9*m.b123 + 39*m.b9*m.b126 + 40*m.b9*m.b129 + 41*m.b9*m.b132 + 42*m.b9*m.b135 + 43*
                       m.b9*m.b138 + 44*m.b9*m.b141 + 45*m.b9*m.b144 + 46*m.b9*m.b147 + 47*m.b9*m.b150 + 48*m.b9*m.b153
                        + 49*m.b9*m.b156 + 50*m.b9*m.b159 + 51*m.b9*m.b162 + 52*m.b9*m.b165 + 53*m.b9*m.b168 + 54*m.b9*
                       m.b171 + 55*m.b9*m.b174 + 56*m.b9*m.b177 + 57*m.b9*m.b180 + 58*m.b9*m.b183 + 59*m.b9*m.b186 + 60*
                       m.b9*m.b189 + 61*m.b9*m.b192 + 62*m.b9*m.b195 + 63*m.b9*m.b198 + 64*m.b9*m.b201 + 65*m.b9*m.b204
                        + 66*m.b9*m.b207 + 67*m.b9*m.b210 + m.b10*m.b13 + 2*m.b10*m.b16 + 3*m.b10*m.b19 + 4*m.b10*m.b22
                        + 5*m.b10*m.b25 + 6*m.b10*m.b28 + 7*m.b10*m.b31 + 8*m.b10*m.b34 + 9*m.b10*m.b37 + 10*m.b10*m.b40
                        + 11*m.b10*m.b43 + 12*m.b10*m.b46 + 13*m.b10*m.b49 + 14*m.b10*m.b52 + 15*m.b10*m.b55 + 16*m.b10*
                       m.b58 + 17*m.b10*m.b61 + 18*m.b10*m.b64 + 19*m.b10*m.b67 + 20*m.b10*m.b70 + 21*m.b10*m.b73 + 22*
                       m.b10*m.b76 + 23*m.b10*m.b79 + 24*m.b10*m.b82 + 25*m.b10*m.b85 + 26*m.b10*m.b88 + 27*m.b10*m.b91
                        + 28*m.b10*m.b94 + 29*m.b10*m.b97 + 30*m.b10*m.b100 + 31*m.b10*m.b103 + 32*m.b10*m.b106 + 33*
                       m.b10*m.b109 + 34*m.b10*m.b112 + 35*m.b10*m.b115 + 36*m.b10*m.b118 + 37*m.b10*m.b121 + 38*m.b10*
                       m.b124 + 39*m.b10*m.b127 + 40*m.b10*m.b130 + 41*m.b10*m.b133 + 42*m.b10*m.b136 + 43*m.b10*m.b139
                        + 44*m.b10*m.b142 + 45*m.b10*m.b145 + 46*m.b10*m.b148 + 47*m.b10*m.b151 + 48*m.b10*m.b154 + 49*
                       m.b10*m.b157 + 50*m.b10*m.b160 + 51*m.b10*m.b163 + 52*m.b10*m.b166 + 53*m.b10*m.b169 + 54*m.b10*
                       m.b172 + 55*m.b10*m.b175 + 56*m.b10*m.b178 + 57*m.b10*m.b181 + 58*m.b10*m.b184 + 59*m.b10*m.b187
                        + 60*m.b10*m.b190 + 61*m.b10*m.b193 + 62*m.b10*m.b196 + 63*m.b10*m.b199 + 64*m.b10*m.b202 + 65*
                       m.b10*m.b205 + 66*m.b10*m.b208 + m.b11*m.b14 + 2*m.b11*m.b17 + 3*m.b11*m.b20 + 4*m.b11*m.b23 + 5*
                       m.b11*m.b26 + 6*m.b11*m.b29 + 7*m.b11*m.b32 + 8*m.b11*m.b35 + 9*m.b11*m.b38 + 10*m.b11*m.b41 + 11
                       *m.b11*m.b44 + 12*m.b11*m.b47 + 13*m.b11*m.b50 + 14*m.b11*m.b53 + 15*m.b11*m.b56 + 16*m.b11*m.b59
                        + 17*m.b11*m.b62 + 18*m.b11*m.b65 + 19*m.b11*m.b68 + 20*m.b11*m.b71 + 21*m.b11*m.b74 + 22*m.b11*
                       m.b77 + 23*m.b11*m.b80 + 24*m.b11*m.b83 + 25*m.b11*m.b86 + 26*m.b11*m.b89 + 27*m.b11*m.b92 + 28*
                       m.b11*m.b95 + 29*m.b11*m.b98 + 30*m.b11*m.b101 + 31*m.b11*m.b104 + 32*m.b11*m.b107 + 33*m.b11*
                       m.b110 + 34*m.b11*m.b113 + 35*m.b11*m.b116 + 36*m.b11*m.b119 + 37*m.b11*m.b122 + 38*m.b11*m.b125
                        + 39*m.b11*m.b128 + 40*m.b11*m.b131 + 41*m.b11*m.b134 + 42*m.b11*m.b137 + 43*m.b11*m.b140 + 44*
                       m.b11*m.b143 + 45*m.b11*m.b146 + 46*m.b11*m.b149 + 47*m.b11*m.b152 + 48*m.b11*m.b155 + 49*m.b11*
                       m.b158 + 50*m.b11*m.b161 + 51*m.b11*m.b164 + 52*m.b11*m.b167 + 53*m.b11*m.b170 + 54*m.b11*m.b173
                        + 55*m.b11*m.b176 + 56*m.b11*m.b179 + 57*m.b11*m.b182 + 58*m.b11*m.b185 + 59*m.b11*m.b188 + 60*
                       m.b11*m.b191 + 61*m.b11*m.b194 + 62*m.b11*m.b197 + 63*m.b11*m.b200 + 64*m.b11*m.b203 + 65*m.b11*
                       m.b206 + 66*m.b11*m.b209 + m.b12*m.b15 + 2*m.b12*m.b18 + 3*m.b12*m.b21 + 4*m.b12*m.b24 + 5*m.b12*
                       m.b27 + 6*m.b12*m.b30 + 7*m.b12*m.b33 + 8*m.b12*m.b36 + 9*m.b12*m.b39 + 10*m.b12*m.b42 + 11*m.b12
                       *m.b45 + 12*m.b12*m.b48 + 13*m.b12*m.b51 + 14*m.b12*m.b54 + 15*m.b12*m.b57 + 16*m.b12*m.b60 + 17*
                       m.b12*m.b63 + 18*m.b12*m.b66 + 19*m.b12*m.b69 + 20*m.b12*m.b72 + 21*m.b12*m.b75 + 22*m.b12*m.b78
                        + 23*m.b12*m.b81 + 24*m.b12*m.b84 + 25*m.b12*m.b87 + 26*m.b12*m.b90 + 27*m.b12*m.b93 + 28*m.b12*
                       m.b96 + 29*m.b12*m.b99 + 30*m.b12*m.b102 + 31*m.b12*m.b105 + 32*m.b12*m.b108 + 33*m.b12*m.b111 + 
                       34*m.b12*m.b114 + 35*m.b12*m.b117 + 36*m.b12*m.b120 + 37*m.b12*m.b123 + 38*m.b12*m.b126 + 39*
                       m.b12*m.b129 + 40*m.b12*m.b132 + 41*m.b12*m.b135 + 42*m.b12*m.b138 + 43*m.b12*m.b141 + 44*m.b12*
                       m.b144 + 45*m.b12*m.b147 + 46*m.b12*m.b150 + 47*m.b12*m.b153 + 48*m.b12*m.b156 + 49*m.b12*m.b159
                        + 50*m.b12*m.b162 + 51*m.b12*m.b165 + 52*m.b12*m.b168 + 53*m.b12*m.b171 + 54*m.b12*m.b174 + 55*
                       m.b12*m.b177 + 56*m.b12*m.b180 + 57*m.b12*m.b183 + 58*m.b12*m.b186 + 59*m.b12*m.b189 + 60*m.b12*
                       m.b192 + 61*m.b12*m.b195 + 62*m.b12*m.b198 + 63*m.b12*m.b201 + 64*m.b12*m.b204 + 65*m.b12*m.b207
                        + 66*m.b12*m.b210 + m.b13*m.b16 + 2*m.b13*m.b19 + 3*m.b13*m.b22 + 4*m.b13*m.b25 + 5*m.b13*m.b28
                        + 6*m.b13*m.b31 + 7*m.b13*m.b34 + 8*m.b13*m.b37 + 9*m.b13*m.b40 + 10*m.b13*m.b43 + 11*m.b13*
                       m.b46 + 12*m.b13*m.b49 + 13*m.b13*m.b52 + 14*m.b13*m.b55 + 15*m.b13*m.b58 + 16*m.b13*m.b61 + 17*
                       m.b13*m.b64 + 18*m.b13*m.b67 + 19*m.b13*m.b70 + 20*m.b13*m.b73 + 21*m.b13*m.b76 + 22*m.b13*m.b79
                        + 23*m.b13*m.b82 + 24*m.b13*m.b85 + 25*m.b13*m.b88 + 26*m.b13*m.b91 + 27*m.b13*m.b94 + 28*m.b13*
                       m.b97 + 29*m.b13*m.b100 + 30*m.b13*m.b103 + 31*m.b13*m.b106 + 32*m.b13*m.b109 + 33*m.b13*m.b112
                        + 34*m.b13*m.b115 + 35*m.b13*m.b118 + 36*m.b13*m.b121 + 37*m.b13*m.b124 + 38*m.b13*m.b127 + 39*
                       m.b13*m.b130 + 40*m.b13*m.b133 + 41*m.b13*m.b136 + 42*m.b13*m.b139 + 43*m.b13*m.b142 + 44*m.b13*
                       m.b145 + 45*m.b13*m.b148 + 46*m.b13*m.b151 + 47*m.b13*m.b154 + 48*m.b13*m.b157 + 49*m.b13*m.b160
                        + 50*m.b13*m.b163 + 51*m.b13*m.b166 + 52*m.b13*m.b169 + 53*m.b13*m.b172 + 54*m.b13*m.b175 + 55*
                       m.b13*m.b178 + 56*m.b13*m.b181 + 57*m.b13*m.b184 + 58*m.b13*m.b187 + 59*m.b13*m.b190 + 60*m.b13*
                       m.b193 + 61*m.b13*m.b196 + 62*m.b13*m.b199 + 63*m.b13*m.b202 + 64*m.b13*m.b205 + 65*m.b13*m.b208
                        + m.b14*m.b17 + 2*m.b14*m.b20 + 3*m.b14*m.b23 + 4*m.b14*m.b26 + 5*m.b14*m.b29 + 6*m.b14*m.b32 + 
                       7*m.b14*m.b35 + 8*m.b14*m.b38 + 9*m.b14*m.b41 + 10*m.b14*m.b44 + 11*m.b14*m.b47 + 12*m.b14*m.b50
                        + 13*m.b14*m.b53 + 14*m.b14*m.b56 + 15*m.b14*m.b59 + 16*m.b14*m.b62 + 17*m.b14*m.b65 + 18*m.b14*
                       m.b68 + 19*m.b14*m.b71 + 20*m.b14*m.b74 + 21*m.b14*m.b77 + 22*m.b14*m.b80 + 23*m.b14*m.b83 + 24*
                       m.b14*m.b86 + 25*m.b14*m.b89 + 26*m.b14*m.b92 + 27*m.b14*m.b95 + 28*m.b14*m.b98 + 29*m.b14*m.b101
                        + 30*m.b14*m.b104 + 31*m.b14*m.b107 + 32*m.b14*m.b110 + 33*m.b14*m.b113 + 34*m.b14*m.b116 + 35*
                       m.b14*m.b119 + 36*m.b14*m.b122 + 37*m.b14*m.b125 + 38*m.b14*m.b128 + 39*m.b14*m.b131 + 40*m.b14*
                       m.b134 + 41*m.b14*m.b137 + 42*m.b14*m.b140 + 43*m.b14*m.b143 + 44*m.b14*m.b146 + 45*m.b14*m.b149
                        + 46*m.b14*m.b152 + 47*m.b14*m.b155 + 48*m.b14*m.b158 + 49*m.b14*m.b161 + 50*m.b14*m.b164 + 51*
                       m.b14*m.b167 + 52*m.b14*m.b170 + 53*m.b14*m.b173 + 54*m.b14*m.b176 + 55*m.b14*m.b179 + 56*m.b14*
                       m.b182 + 57*m.b14*m.b185 + 58*m.b14*m.b188 + 59*m.b14*m.b191 + 60*m.b14*m.b194 + 61*m.b14*m.b197
                        + 62*m.b14*m.b200 + 63*m.b14*m.b203 + 64*m.b14*m.b206 + 65*m.b14*m.b209 + m.b15*m.b18 + 2*m.b15*
                       m.b21 + 3*m.b15*m.b24 + 4*m.b15*m.b27 + 5*m.b15*m.b30 + 6*m.b15*m.b33 + 7*m.b15*m.b36 + 8*m.b15*
                       m.b39 + 9*m.b15*m.b42 + 10*m.b15*m.b45 + 11*m.b15*m.b48 + 12*m.b15*m.b51 + 13*m.b15*m.b54 + 14*
                       m.b15*m.b57 + 15*m.b15*m.b60 + 16*m.b15*m.b63 + 17*m.b15*m.b66 + 18*m.b15*m.b69 + 19*m.b15*m.b72
                        + 20*m.b15*m.b75 + 21*m.b15*m.b78 + 22*m.b15*m.b81 + 23*m.b15*m.b84 + 24*m.b15*m.b87 + 25*m.b15*
                       m.b90 + 26*m.b15*m.b93 + 27*m.b15*m.b96 + 28*m.b15*m.b99 + 29*m.b15*m.b102 + 30*m.b15*m.b105 + 31
                       *m.b15*m.b108 + 32*m.b15*m.b111 + 33*m.b15*m.b114 + 34*m.b15*m.b117 + 35*m.b15*m.b120 + 36*m.b15*
                       m.b123 + 37*m.b15*m.b126 + 38*m.b15*m.b129 + 39*m.b15*m.b132 + 40*m.b15*m.b135 + 41*m.b15*m.b138
                        + 42*m.b15*m.b141 + 43*m.b15*m.b144 + 44*m.b15*m.b147 + 45*m.b15*m.b150 + 46*m.b15*m.b153 + 47*
                       m.b15*m.b156 + 48*m.b15*m.b159 + 49*m.b15*m.b162 + 50*m.b15*m.b165 + 51*m.b15*m.b168 + 52*m.b15*
                       m.b171 + 53*m.b15*m.b174 + 54*m.b15*m.b177 + 55*m.b15*m.b180 + 56*m.b15*m.b183 + 57*m.b15*m.b186
                        + 58*m.b15*m.b189 + 59*m.b15*m.b192 + 60*m.b15*m.b195 + 61*m.b15*m.b198 + 62*m.b15*m.b201 + 63*
                       m.b15*m.b204 + 64*m.b15*m.b207 + 65*m.b15*m.b210 + m.b16*m.b19 + 2*m.b16*m.b22 + 3*m.b16*m.b25 + 
                       4*m.b16*m.b28 + 5*m.b16*m.b31 + 6*m.b16*m.b34 + 7*m.b16*m.b37 + 8*m.b16*m.b40 + 9*m.b16*m.b43 + 
                       10*m.b16*m.b46 + 11*m.b16*m.b49 + 12*m.b16*m.b52 + 13*m.b16*m.b55 + 14*m.b16*m.b58 + 15*m.b16*
                       m.b61 + 16*m.b16*m.b64 + 17*m.b16*m.b67 + 18*m.b16*m.b70 + 19*m.b16*m.b73 + 20*m.b16*m.b76 + 21*
                       m.b16*m.b79 + 22*m.b16*m.b82 + 23*m.b16*m.b85 + 24*m.b16*m.b88 + 25*m.b16*m.b91 + 26*m.b16*m.b94
                        + 27*m.b16*m.b97 + 28*m.b16*m.b100 + 29*m.b16*m.b103 + 30*m.b16*m.b106 + 31*m.b16*m.b109 + 32*
                       m.b16*m.b112 + 33*m.b16*m.b115 + 34*m.b16*m.b118 + 35*m.b16*m.b121 + 36*m.b16*m.b124 + 37*m.b16*
                       m.b127 + 38*m.b16*m.b130 + 39*m.b16*m.b133 + 40*m.b16*m.b136 + 41*m.b16*m.b139 + 42*m.b16*m.b142
                        + 43*m.b16*m.b145 + 44*m.b16*m.b148 + 45*m.b16*m.b151 + 46*m.b16*m.b154 + 47*m.b16*m.b157 + 48*
                       m.b16*m.b160 + 49*m.b16*m.b163 + 50*m.b16*m.b166 + 51*m.b16*m.b169 + 52*m.b16*m.b172 + 53*m.b16*
                       m.b175 + 54*m.b16*m.b178 + 55*m.b16*m.b181 + 56*m.b16*m.b184 + 57*m.b16*m.b187 + 58*m.b16*m.b190
                        + 59*m.b16*m.b193 + 60*m.b16*m.b196 + 61*m.b16*m.b199 + 62*m.b16*m.b202 + 63*m.b16*m.b205 + 64*
                       m.b16*m.b208 + m.b17*m.b20 + 2*m.b17*m.b23 + 3*m.b17*m.b26 + 4*m.b17*m.b29 + 5*m.b17*m.b32 + 6*
                       m.b17*m.b35 + 7*m.b17*m.b38 + 8*m.b17*m.b41 + 9*m.b17*m.b44 + 10*m.b17*m.b47 + 11*m.b17*m.b50 + 
                       12*m.b17*m.b53 + 13*m.b17*m.b56 + 14*m.b17*m.b59 + 15*m.b17*m.b62 + 16*m.b17*m.b65 + 17*m.b17*
                       m.b68 + 18*m.b17*m.b71 + 19*m.b17*m.b74 + 20*m.b17*m.b77 + 21*m.b17*m.b80 + 22*m.b17*m.b83 + 23*
                       m.b17*m.b86 + 24*m.b17*m.b89 + 25*m.b17*m.b92 + 26*m.b17*m.b95 + 27*m.b17*m.b98 + 28*m.b17*m.b101
                        + 29*m.b17*m.b104 + 30*m.b17*m.b107 + 31*m.b17*m.b110 + 32*m.b17*m.b113 + 33*m.b17*m.b116 + 34*
                       m.b17*m.b119 + 35*m.b17*m.b122 + 36*m.b17*m.b125 + 37*m.b17*m.b128 + 38*m.b17*m.b131 + 39*m.b17*
                       m.b134 + 40*m.b17*m.b137 + 41*m.b17*m.b140 + 42*m.b17*m.b143 + 43*m.b17*m.b146 + 44*m.b17*m.b149
                        + 45*m.b17*m.b152 + 46*m.b17*m.b155 + 47*m.b17*m.b158 + 48*m.b17*m.b161 + 49*m.b17*m.b164 + 50*
                       m.b17*m.b167 + 51*m.b17*m.b170 + 52*m.b17*m.b173 + 53*m.b17*m.b176 + 54*m.b17*m.b179 + 55*m.b17*
                       m.b182 + 56*m.b17*m.b185 + 57*m.b17*m.b188 + 58*m.b17*m.b191 + 59*m.b17*m.b194 + 60*m.b17*m.b197
                        + 61*m.b17*m.b200 + 62*m.b17*m.b203 + 63*m.b17*m.b206 + 64*m.b17*m.b209 + m.b18*m.b21 + 2*m.b18*
                       m.b24 + 3*m.b18*m.b27 + 4*m.b18*m.b30 + 5*m.b18*m.b33 + 6*m.b18*m.b36 + 7*m.b18*m.b39 + 8*m.b18*
                       m.b42 + 9*m.b18*m.b45 + 10*m.b18*m.b48 + 11*m.b18*m.b51 + 12*m.b18*m.b54 + 13*m.b18*m.b57 + 14*
                       m.b18*m.b60 + 15*m.b18*m.b63 + 16*m.b18*m.b66 + 17*m.b18*m.b69 + 18*m.b18*m.b72 + 19*m.b18*m.b75
                        + 20*m.b18*m.b78 + 21*m.b18*m.b81 + 22*m.b18*m.b84 + 23*m.b18*m.b87 + 24*m.b18*m.b90 + 25*m.b18*
                       m.b93 + 26*m.b18*m.b96 + 27*m.b18*m.b99 + 28*m.b18*m.b102 + 29*m.b18*m.b105 + 30*m.b18*m.b108 + 
                       31*m.b18*m.b111 + 32*m.b18*m.b114 + 33*m.b18*m.b117 + 34*m.b18*m.b120 + 35*m.b18*m.b123 + 36*
                       m.b18*m.b126 + 37*m.b18*m.b129 + 38*m.b18*m.b132 + 39*m.b18*m.b135 + 40*m.b18*m.b138 + 41*m.b18*
                       m.b141 + 42*m.b18*m.b144 + 43*m.b18*m.b147 + 44*m.b18*m.b150 + 45*m.b18*m.b153 + 46*m.b18*m.b156
                        + 47*m.b18*m.b159 + 48*m.b18*m.b162 + 49*m.b18*m.b165 + 50*m.b18*m.b168 + 51*m.b18*m.b171 + 52*
                       m.b18*m.b174 + 53*m.b18*m.b177 + 54*m.b18*m.b180 + 55*m.b18*m.b183 + 56*m.b18*m.b186 + 57*m.b18*
                       m.b189 + 58*m.b18*m.b192 + 59*m.b18*m.b195 + 60*m.b18*m.b198 + 61*m.b18*m.b201 + 62*m.b18*m.b204
                        + 63*m.b18*m.b207 + 64*m.b18*m.b210 + m.b19*m.b22 + 2*m.b19*m.b25 + 3*m.b19*m.b28 + 4*m.b19*
                       m.b31 + 5*m.b19*m.b34 + 6*m.b19*m.b37 + 7*m.b19*m.b40 + 8*m.b19*m.b43 + 9*m.b19*m.b46 + 10*m.b19*
                       m.b49 + 11*m.b19*m.b52 + 12*m.b19*m.b55 + 13*m.b19*m.b58 + 14*m.b19*m.b61 + 15*m.b19*m.b64 + 16*
                       m.b19*m.b67 + 17*m.b19*m.b70 + 18*m.b19*m.b73 + 19*m.b19*m.b76 + 20*m.b19*m.b79 + 21*m.b19*m.b82
                        + 22*m.b19*m.b85 + 23*m.b19*m.b88 + 24*m.b19*m.b91 + 25*m.b19*m.b94 + 26*m.b19*m.b97 + 27*m.b19*
                       m.b100 + 28*m.b19*m.b103 + 29*m.b19*m.b106 + 30*m.b19*m.b109 + 31*m.b19*m.b112 + 32*m.b19*m.b115
                        + 33*m.b19*m.b118 + 34*m.b19*m.b121 + 35*m.b19*m.b124 + 36*m.b19*m.b127 + 37*m.b19*m.b130 + 38*
                       m.b19*m.b133 + 39*m.b19*m.b136 + 40*m.b19*m.b139 + 41*m.b19*m.b142 + 42*m.b19*m.b145 + 43*m.b19*
                       m.b148 + 44*m.b19*m.b151 + 45*m.b19*m.b154 + 46*m.b19*m.b157 + 47*m.b19*m.b160 + 48*m.b19*m.b163
                        + 49*m.b19*m.b166 + 50*m.b19*m.b169 + 51*m.b19*m.b172 + 52*m.b19*m.b175 + 53*m.b19*m.b178 + 54*
                       m.b19*m.b181 + 55*m.b19*m.b184 + 56*m.b19*m.b187 + 57*m.b19*m.b190 + 58*m.b19*m.b193 + 59*m.b19*
                       m.b196 + 60*m.b19*m.b199 + 61*m.b19*m.b202 + 62*m.b19*m.b205 + 63*m.b19*m.b208 + m.b20*m.b23 + 2*
                       m.b20*m.b26 + 3*m.b20*m.b29 + 4*m.b20*m.b32 + 5*m.b20*m.b35 + 6*m.b20*m.b38 + 7*m.b20*m.b41 + 8*
                       m.b20*m.b44 + 9*m.b20*m.b47 + 10*m.b20*m.b50 + 11*m.b20*m.b53 + 12*m.b20*m.b56 + 13*m.b20*m.b59
                        + 14*m.b20*m.b62 + 15*m.b20*m.b65 + 16*m.b20*m.b68 + 17*m.b20*m.b71 + 18*m.b20*m.b74 + 19*m.b20*
                       m.b77 + 20*m.b20*m.b80 + 21*m.b20*m.b83 + 22*m.b20*m.b86 + 23*m.b20*m.b89 + 24*m.b20*m.b92 + 25*
                       m.b20*m.b95 + 26*m.b20*m.b98 + 27*m.b20*m.b101 + 28*m.b20*m.b104 + 29*m.b20*m.b107 + 30*m.b20*
                       m.b110 + 31*m.b20*m.b113 + 32*m.b20*m.b116 + 33*m.b20*m.b119 + 34*m.b20*m.b122 + 35*m.b20*m.b125
                        + 36*m.b20*m.b128 + 37*m.b20*m.b131 + 38*m.b20*m.b134 + 39*m.b20*m.b137 + 40*m.b20*m.b140 + 41*
                       m.b20*m.b143 + 42*m.b20*m.b146 + 43*m.b20*m.b149 + 44*m.b20*m.b152 + 45*m.b20*m.b155 + 46*m.b20*
                       m.b158 + 47*m.b20*m.b161 + 48*m.b20*m.b164 + 49*m.b20*m.b167 + 50*m.b20*m.b170 + 51*m.b20*m.b173
                        + 52*m.b20*m.b176 + 53*m.b20*m.b179 + 54*m.b20*m.b182 + 55*m.b20*m.b185 + 56*m.b20*m.b188 + 57*
                       m.b20*m.b191 + 58*m.b20*m.b194 + 59*m.b20*m.b197 + 60*m.b20*m.b200 + 61*m.b20*m.b203 + 62*m.b20*
                       m.b206 + 63*m.b20*m.b209 + m.b21*m.b24 + 2*m.b21*m.b27 + 3*m.b21*m.b30 + 4*m.b21*m.b33 + 5*m.b21*
                       m.b36 + 6*m.b21*m.b39 + 7*m.b21*m.b42 + 8*m.b21*m.b45 + 9*m.b21*m.b48 + 10*m.b21*m.b51 + 11*m.b21
                       *m.b54 + 12*m.b21*m.b57 + 13*m.b21*m.b60 + 14*m.b21*m.b63 + 15*m.b21*m.b66 + 16*m.b21*m.b69 + 17*
                       m.b21*m.b72 + 18*m.b21*m.b75 + 19*m.b21*m.b78 + 20*m.b21*m.b81 + 21*m.b21*m.b84 + 22*m.b21*m.b87
                        + 23*m.b21*m.b90 + 24*m.b21*m.b93 + 25*m.b21*m.b96 + 26*m.b21*m.b99 + 27*m.b21*m.b102 + 28*m.b21
                       *m.b105 + 29*m.b21*m.b108 + 30*m.b21*m.b111 + 31*m.b21*m.b114 + 32*m.b21*m.b117 + 33*m.b21*m.b120
                        + 34*m.b21*m.b123 + 35*m.b21*m.b126 + 36*m.b21*m.b129 + 37*m.b21*m.b132 + 38*m.b21*m.b135 + 39*
                       m.b21*m.b138 + 40*m.b21*m.b141 + 41*m.b21*m.b144 + 42*m.b21*m.b147 + 43*m.b21*m.b150 + 44*m.b21*
                       m.b153 + 45*m.b21*m.b156 + 46*m.b21*m.b159 + 47*m.b21*m.b162 + 48*m.b21*m.b165 + 49*m.b21*m.b168
                        + 50*m.b21*m.b171 + 51*m.b21*m.b174 + 52*m.b21*m.b177 + 53*m.b21*m.b180 + 54*m.b21*m.b183 + 55*
                       m.b21*m.b186 + 56*m.b21*m.b189 + 57*m.b21*m.b192 + 58*m.b21*m.b195 + 59*m.b21*m.b198 + 60*m.b21*
                       m.b201 + 61*m.b21*m.b204 + 62*m.b21*m.b207 + 63*m.b21*m.b210 + m.b22*m.b25 + 2*m.b22*m.b28 + 3*
                       m.b22*m.b31 + 4*m.b22*m.b34 + 5*m.b22*m.b37 + 6*m.b22*m.b40 + 7*m.b22*m.b43 + 8*m.b22*m.b46 + 9*
                       m.b22*m.b49 + 10*m.b22*m.b52 + 11*m.b22*m.b55 + 12*m.b22*m.b58 + 13*m.b22*m.b61 + 14*m.b22*m.b64
                        + 15*m.b22*m.b67 + 16*m.b22*m.b70 + 17*m.b22*m.b73 + 18*m.b22*m.b76 + 19*m.b22*m.b79 + 20*m.b22*
                       m.b82 + 21*m.b22*m.b85 + 22*m.b22*m.b88 + 23*m.b22*m.b91 + 24*m.b22*m.b94 + 25*m.b22*m.b97 + 26*
                       m.b22*m.b100 + 27*m.b22*m.b103 + 28*m.b22*m.b106 + 29*m.b22*m.b109 + 30*m.b22*m.b112 + 31*m.b22*
                       m.b115 + 32*m.b22*m.b118 + 33*m.b22*m.b121 + 34*m.b22*m.b124 + 35*m.b22*m.b127 + 36*m.b22*m.b130
                        + 37*m.b22*m.b133 + 38*m.b22*m.b136 + 39*m.b22*m.b139 + 40*m.b22*m.b142 + 41*m.b22*m.b145 + 42*
                       m.b22*m.b148 + 43*m.b22*m.b151 + 44*m.b22*m.b154 + 45*m.b22*m.b157 + 46*m.b22*m.b160 + 47*m.b22*
                       m.b163 + 48*m.b22*m.b166 + 49*m.b22*m.b169 + 50*m.b22*m.b172 + 51*m.b22*m.b175 + 52*m.b22*m.b178
                        + 53*m.b22*m.b181 + 54*m.b22*m.b184 + 55*m.b22*m.b187 + 56*m.b22*m.b190 + 57*m.b22*m.b193 + 58*
                       m.b22*m.b196 + 59*m.b22*m.b199 + 60*m.b22*m.b202 + 61*m.b22*m.b205 + 62*m.b22*m.b208 + m.b23*
                       m.b26 + 2*m.b23*m.b29 + 3*m.b23*m.b32 + 4*m.b23*m.b35 + 5*m.b23*m.b38 + 6*m.b23*m.b41 + 7*m.b23*
                       m.b44 + 8*m.b23*m.b47 + 9*m.b23*m.b50 + 10*m.b23*m.b53 + 11*m.b23*m.b56 + 12*m.b23*m.b59 + 13*
                       m.b23*m.b62 + 14*m.b23*m.b65 + 15*m.b23*m.b68 + 16*m.b23*m.b71 + 17*m.b23*m.b74 + 18*m.b23*m.b77
                        + 19*m.b23*m.b80 + 20*m.b23*m.b83 + 21*m.b23*m.b86 + 22*m.b23*m.b89 + 23*m.b23*m.b92 + 24*m.b23*
                       m.b95 + 25*m.b23*m.b98 + 26*m.b23*m.b101 + 27*m.b23*m.b104 + 28*m.b23*m.b107 + 29*m.b23*m.b110 + 
                       30*m.b23*m.b113 + 31*m.b23*m.b116 + 32*m.b23*m.b119 + 33*m.b23*m.b122 + 34*m.b23*m.b125 + 35*
                       m.b23*m.b128 + 36*m.b23*m.b131 + 37*m.b23*m.b134 + 38*m.b23*m.b137 + 39*m.b23*m.b140 + 40*m.b23*
                       m.b143 + 41*m.b23*m.b146 + 42*m.b23*m.b149 + 43*m.b23*m.b152 + 44*m.b23*m.b155 + 45*m.b23*m.b158
                        + 46*m.b23*m.b161 + 47*m.b23*m.b164 + 48*m.b23*m.b167 + 49*m.b23*m.b170 + 50*m.b23*m.b173 + 51*
                       m.b23*m.b176 + 52*m.b23*m.b179 + 53*m.b23*m.b182 + 54*m.b23*m.b185 + 55*m.b23*m.b188 + 56*m.b23*
                       m.b191 + 57*m.b23*m.b194 + 58*m.b23*m.b197 + 59*m.b23*m.b200 + 60*m.b23*m.b203 + 61*m.b23*m.b206
                        + 62*m.b23*m.b209 + m.b24*m.b27 + 2*m.b24*m.b30 + 3*m.b24*m.b33 + 4*m.b24*m.b36 + 5*m.b24*m.b39
                        + 6*m.b24*m.b42 + 7*m.b24*m.b45 + 8*m.b24*m.b48 + 9*m.b24*m.b51 + 10*m.b24*m.b54 + 11*m.b24*
                       m.b57 + 12*m.b24*m.b60 + 13*m.b24*m.b63 + 14*m.b24*m.b66 + 15*m.b24*m.b69 + 16*m.b24*m.b72 + 17*
                       m.b24*m.b75 + 18*m.b24*m.b78 + 19*m.b24*m.b81 + 20*m.b24*m.b84 + 21*m.b24*m.b87 + 22*m.b24*m.b90
                        + 23*m.b24*m.b93 + 24*m.b24*m.b96 + 25*m.b24*m.b99 + 26*m.b24*m.b102 + 27*m.b24*m.b105 + 28*
                       m.b24*m.b108 + 29*m.b24*m.b111 + 30*m.b24*m.b114 + 31*m.b24*m.b117 + 32*m.b24*m.b120 + 33*m.b24*
                       m.b123 + 34*m.b24*m.b126 + 35*m.b24*m.b129 + 36*m.b24*m.b132 + 37*m.b24*m.b135 + 38*m.b24*m.b138
                        + 39*m.b24*m.b141 + 40*m.b24*m.b144 + 41*m.b24*m.b147 + 42*m.b24*m.b150 + 43*m.b24*m.b153 + 44*
                       m.b24*m.b156 + 45*m.b24*m.b159 + 46*m.b24*m.b162 + 47*m.b24*m.b165 + 48*m.b24*m.b168 + 49*m.b24*
                       m.b171 + 50*m.b24*m.b174 + 51*m.b24*m.b177 + 52*m.b24*m.b180 + 53*m.b24*m.b183 + 54*m.b24*m.b186
                        + 55*m.b24*m.b189 + 56*m.b24*m.b192 + 57*m.b24*m.b195 + 58*m.b24*m.b198 + 59*m.b24*m.b201 + 60*
                       m.b24*m.b204 + 61*m.b24*m.b207 + 62*m.b24*m.b210 + m.b25*m.b28 + 2*m.b25*m.b31 + 3*m.b25*m.b34 + 
                       4*m.b25*m.b37 + 5*m.b25*m.b40 + 6*m.b25*m.b43 + 7*m.b25*m.b46 + 8*m.b25*m.b49 + 9*m.b25*m.b52 + 
                       10*m.b25*m.b55 + 11*m.b25*m.b58 + 12*m.b25*m.b61 + 13*m.b25*m.b64 + 14*m.b25*m.b67 + 15*m.b25*
                       m.b70 + 16*m.b25*m.b73 + 17*m.b25*m.b76 + 18*m.b25*m.b79 + 19*m.b25*m.b82 + 20*m.b25*m.b85 + 21*
                       m.b25*m.b88 + 22*m.b25*m.b91 + 23*m.b25*m.b94 + 24*m.b25*m.b97 + 25*m.b25*m.b100 + 26*m.b25*
                       m.b103 + 27*m.b25*m.b106 + 28*m.b25*m.b109 + 29*m.b25*m.b112 + 30*m.b25*m.b115 + 31*m.b25*m.b118
                        + 32*m.b25*m.b121 + 33*m.b25*m.b124 + 34*m.b25*m.b127 + 35*m.b25*m.b130 + 36*m.b25*m.b133 + 37*
                       m.b25*m.b136 + 38*m.b25*m.b139 + 39*m.b25*m.b142 + 40*m.b25*m.b145 + 41*m.b25*m.b148 + 42*m.b25*
                       m.b151 + 43*m.b25*m.b154 + 44*m.b25*m.b157 + 45*m.b25*m.b160 + 46*m.b25*m.b163 + 47*m.b25*m.b166
                        + 48*m.b25*m.b169 + 49*m.b25*m.b172 + 50*m.b25*m.b175 + 51*m.b25*m.b178 + 52*m.b25*m.b181 + 53*
                       m.b25*m.b184 + 54*m.b25*m.b187 + 55*m.b25*m.b190 + 56*m.b25*m.b193 + 57*m.b25*m.b196 + 58*m.b25*
                       m.b199 + 59*m.b25*m.b202 + 60*m.b25*m.b205 + 61*m.b25*m.b208 + m.b26*m.b29 + 2*m.b26*m.b32 + 3*
                       m.b26*m.b35 + 4*m.b26*m.b38 + 5*m.b26*m.b41 + 6*m.b26*m.b44 + 7*m.b26*m.b47 + 8*m.b26*m.b50 + 9*
                       m.b26*m.b53 + 10*m.b26*m.b56 + 11*m.b26*m.b59 + 12*m.b26*m.b62 + 13*m.b26*m.b65 + 14*m.b26*m.b68
                        + 15*m.b26*m.b71 + 16*m.b26*m.b74 + 17*m.b26*m.b77 + 18*m.b26*m.b80 + 19*m.b26*m.b83 + 20*m.b26*
                       m.b86 + 21*m.b26*m.b89 + 22*m.b26*m.b92 + 23*m.b26*m.b95 + 24*m.b26*m.b98 + 25*m.b26*m.b101 + 26*
                       m.b26*m.b104 + 27*m.b26*m.b107 + 28*m.b26*m.b110 + 29*m.b26*m.b113 + 30*m.b26*m.b116 + 31*m.b26*
                       m.b119 + 32*m.b26*m.b122 + 33*m.b26*m.b125 + 34*m.b26*m.b128 + 35*m.b26*m.b131 + 36*m.b26*m.b134
                        + 37*m.b26*m.b137 + 38*m.b26*m.b140 + 39*m.b26*m.b143 + 40*m.b26*m.b146 + 41*m.b26*m.b149 + 42*
                       m.b26*m.b152 + 43*m.b26*m.b155 + 44*m.b26*m.b158 + 45*m.b26*m.b161 + 46*m.b26*m.b164 + 47*m.b26*
                       m.b167 + 48*m.b26*m.b170 + 49*m.b26*m.b173 + 50*m.b26*m.b176 + 51*m.b26*m.b179 + 52*m.b26*m.b182
                        + 53*m.b26*m.b185 + 54*m.b26*m.b188 + 55*m.b26*m.b191 + 56*m.b26*m.b194 + 57*m.b26*m.b197 + 58*
                       m.b26*m.b200 + 59*m.b26*m.b203 + 60*m.b26*m.b206 + 61*m.b26*m.b209 + m.b27*m.b30 + 2*m.b27*m.b33
                        + 3*m.b27*m.b36 + 4*m.b27*m.b39 + 5*m.b27*m.b42 + 6*m.b27*m.b45 + 7*m.b27*m.b48 + 8*m.b27*m.b51
                        + 9*m.b27*m.b54 + 10*m.b27*m.b57 + 11*m.b27*m.b60 + 12*m.b27*m.b63 + 13*m.b27*m.b66 + 14*m.b27*
                       m.b69 + 15*m.b27*m.b72 + 16*m.b27*m.b75 + 17*m.b27*m.b78 + 18*m.b27*m.b81 + 19*m.b27*m.b84 + 20*
                       m.b27*m.b87 + 21*m.b27*m.b90 + 22*m.b27*m.b93 + 23*m.b27*m.b96 + 24*m.b27*m.b99 + 25*m.b27*m.b102
                        + 26*m.b27*m.b105 + 27*m.b27*m.b108 + 28*m.b27*m.b111 + 29*m.b27*m.b114 + 30*m.b27*m.b117 + 31*
                       m.b27*m.b120 + 32*m.b27*m.b123 + 33*m.b27*m.b126 + 34*m.b27*m.b129 + 35*m.b27*m.b132 + 36*m.b27*
                       m.b135 + 37*m.b27*m.b138 + 38*m.b27*m.b141 + 39*m.b27*m.b144 + 40*m.b27*m.b147 + 41*m.b27*m.b150
                        + 42*m.b27*m.b153 + 43*m.b27*m.b156 + 44*m.b27*m.b159 + 45*m.b27*m.b162 + 46*m.b27*m.b165 + 47*
                       m.b27*m.b168 + 48*m.b27*m.b171 + 49*m.b27*m.b174 + 50*m.b27*m.b177 + 51*m.b27*m.b180 + 52*m.b27*
                       m.b183 + 53*m.b27*m.b186 + 54*m.b27*m.b189 + 55*m.b27*m.b192 + 56*m.b27*m.b195 + 57*m.b27*m.b198
                        + 58*m.b27*m.b201 + 59*m.b27*m.b204 + 60*m.b27*m.b207 + 61*m.b27*m.b210 + m.b28*m.b31 + 2*m.b28*
                       m.b34 + 3*m.b28*m.b37 + 4*m.b28*m.b40 + 5*m.b28*m.b43 + 6*m.b28*m.b46 + 7*m.b28*m.b49 + 8*m.b28*
                       m.b52 + 9*m.b28*m.b55 + 10*m.b28*m.b58 + 11*m.b28*m.b61 + 12*m.b28*m.b64 + 13*m.b28*m.b67 + 14*
                       m.b28*m.b70 + 15*m.b28*m.b73 + 16*m.b28*m.b76 + 17*m.b28*m.b79 + 18*m.b28*m.b82 + 19*m.b28*m.b85
                        + 20*m.b28*m.b88 + 21*m.b28*m.b91 + 22*m.b28*m.b94 + 23*m.b28*m.b97 + 24*m.b28*m.b100 + 25*m.b28
                       *m.b103 + 26*m.b28*m.b106 + 27*m.b28*m.b109 + 28*m.b28*m.b112 + 29*m.b28*m.b115 + 30*m.b28*m.b118
                        + 31*m.b28*m.b121 + 32*m.b28*m.b124 + 33*m.b28*m.b127 + 34*m.b28*m.b130 + 35*m.b28*m.b133 + 36*
                       m.b28*m.b136 + 37*m.b28*m.b139 + 38*m.b28*m.b142 + 39*m.b28*m.b145 + 40*m.b28*m.b148 + 41*m.b28*
                       m.b151 + 42*m.b28*m.b154 + 43*m.b28*m.b157 + 44*m.b28*m.b160 + 45*m.b28*m.b163 + 46*m.b28*m.b166
                        + 47*m.b28*m.b169 + 48*m.b28*m.b172 + 49*m.b28*m.b175 + 50*m.b28*m.b178 + 51*m.b28*m.b181 + 52*
                       m.b28*m.b184 + 53*m.b28*m.b187 + 54*m.b28*m.b190 + 55*m.b28*m.b193 + 56*m.b28*m.b196 + 57*m.b28*
                       m.b199 + 58*m.b28*m.b202 + 59*m.b28*m.b205 + 60*m.b28*m.b208 + m.b29*m.b32 + 2*m.b29*m.b35 + 3*
                       m.b29*m.b38 + 4*m.b29*m.b41 + 5*m.b29*m.b44 + 6*m.b29*m.b47 + 7*m.b29*m.b50 + 8*m.b29*m.b53 + 9*
                       m.b29*m.b56 + 10*m.b29*m.b59 + 11*m.b29*m.b62 + 12*m.b29*m.b65 + 13*m.b29*m.b68 + 14*m.b29*m.b71
                        + 15*m.b29*m.b74 + 16*m.b29*m.b77 + 17*m.b29*m.b80 + 18*m.b29*m.b83 + 19*m.b29*m.b86 + 20*m.b29*
                       m.b89 + 21*m.b29*m.b92 + 22*m.b29*m.b95 + 23*m.b29*m.b98 + 24*m.b29*m.b101 + 25*m.b29*m.b104 + 26
                       *m.b29*m.b107 + 27*m.b29*m.b110 + 28*m.b29*m.b113 + 29*m.b29*m.b116 + 30*m.b29*m.b119 + 31*m.b29*
                       m.b122 + 32*m.b29*m.b125 + 33*m.b29*m.b128 + 34*m.b29*m.b131 + 35*m.b29*m.b134 + 36*m.b29*m.b137
                        + 37*m.b29*m.b140 + 38*m.b29*m.b143 + 39*m.b29*m.b146 + 40*m.b29*m.b149 + 41*m.b29*m.b152 + 42*
                       m.b29*m.b155 + 43*m.b29*m.b158 + 44*m.b29*m.b161 + 45*m.b29*m.b164 + 46*m.b29*m.b167 + 47*m.b29*
                       m.b170 + 48*m.b29*m.b173 + 49*m.b29*m.b176 + 50*m.b29*m.b179 + 51*m.b29*m.b182 + 52*m.b29*m.b185
                        + 53*m.b29*m.b188 + 54*m.b29*m.b191 + 55*m.b29*m.b194 + 56*m.b29*m.b197 + 57*m.b29*m.b200 + 58*
                       m.b29*m.b203 + 59*m.b29*m.b206 + 60*m.b29*m.b209 + m.b30*m.b33 + 2*m.b30*m.b36 + 3*m.b30*m.b39 + 
                       4*m.b30*m.b42 + 5*m.b30*m.b45 + 6*m.b30*m.b48 + 7*m.b30*m.b51 + 8*m.b30*m.b54 + 9*m.b30*m.b57 + 
                       10*m.b30*m.b60 + 11*m.b30*m.b63 + 12*m.b30*m.b66 + 13*m.b30*m.b69 + 14*m.b30*m.b72 + 15*m.b30*
                       m.b75 + 16*m.b30*m.b78 + 17*m.b30*m.b81 + 18*m.b30*m.b84 + 19*m.b30*m.b87 + 20*m.b30*m.b90 + 21*
                       m.b30*m.b93 + 22*m.b30*m.b96 + 23*m.b30*m.b99 + 24*m.b30*m.b102 + 25*m.b30*m.b105 + 26*m.b30*
                       m.b108 + 27*m.b30*m.b111 + 28*m.b30*m.b114 + 29*m.b30*m.b117 + 30*m.b30*m.b120 + 31*m.b30*m.b123
                        + 32*m.b30*m.b126 + 33*m.b30*m.b129 + 34*m.b30*m.b132 + 35*m.b30*m.b135 + 36*m.b30*m.b138 + 37*
                       m.b30*m.b141 + 38*m.b30*m.b144 + 39*m.b30*m.b147 + 40*m.b30*m.b150 + 41*m.b30*m.b153 + 42*m.b30*
                       m.b156 + 43*m.b30*m.b159 + 44*m.b30*m.b162 + 45*m.b30*m.b165 + 46*m.b30*m.b168 + 47*m.b30*m.b171
                        + 48*m.b30*m.b174 + 49*m.b30*m.b177 + 50*m.b30*m.b180 + 51*m.b30*m.b183 + 52*m.b30*m.b186 + 53*
                       m.b30*m.b189 + 54*m.b30*m.b192 + 55*m.b30*m.b195 + 56*m.b30*m.b198 + 57*m.b30*m.b201 + 58*m.b30*
                       m.b204 + 59*m.b30*m.b207 + 60*m.b30*m.b210 + m.b31*m.b34 + 2*m.b31*m.b37 + 3*m.b31*m.b40 + 4*
                       m.b31*m.b43 + 5*m.b31*m.b46 + 6*m.b31*m.b49 + 7*m.b31*m.b52 + 8*m.b31*m.b55 + 9*m.b31*m.b58 + 10*
                       m.b31*m.b61 + 11*m.b31*m.b64 + 12*m.b31*m.b67 + 13*m.b31*m.b70 + 14*m.b31*m.b73 + 15*m.b31*m.b76
                        + 16*m.b31*m.b79 + 17*m.b31*m.b82 + 18*m.b31*m.b85 + 19*m.b31*m.b88 + 20*m.b31*m.b91 + 21*m.b31*
                       m.b94 + 22*m.b31*m.b97 + 23*m.b31*m.b100 + 24*m.b31*m.b103 + 25*m.b31*m.b106 + 26*m.b31*m.b109 + 
                       27*m.b31*m.b112 + 28*m.b31*m.b115 + 29*m.b31*m.b118 + 30*m.b31*m.b121 + 31*m.b31*m.b124 + 32*
                       m.b31*m.b127 + 33*m.b31*m.b130 + 34*m.b31*m.b133 + 35*m.b31*m.b136 + 36*m.b31*m.b139 + 37*m.b31*
                       m.b142 + 38*m.b31*m.b145 + 39*m.b31*m.b148 + 40*m.b31*m.b151 + 41*m.b31*m.b154 + 42*m.b31*m.b157
                        + 43*m.b31*m.b160 + 44*m.b31*m.b163 + 45*m.b31*m.b166 + 46*m.b31*m.b169 + 47*m.b31*m.b172 + 48*
                       m.b31*m.b175 + 49*m.b31*m.b178 + 50*m.b31*m.b181 + 51*m.b31*m.b184 + 52*m.b31*m.b187 + 53*m.b31*
                       m.b190 + 54*m.b31*m.b193 + 55*m.b31*m.b196 + 56*m.b31*m.b199 + 57*m.b31*m.b202 + 58*m.b31*m.b205
                        + 59*m.b31*m.b208 + m.b32*m.b35 + 2*m.b32*m.b38 + 3*m.b32*m.b41 + 4*m.b32*m.b44 + 5*m.b32*m.b47
                        + 6*m.b32*m.b50 + 7*m.b32*m.b53 + 8*m.b32*m.b56 + 9*m.b32*m.b59 + 10*m.b32*m.b62 + 11*m.b32*
                       m.b65 + 12*m.b32*m.b68 + 13*m.b32*m.b71 + 14*m.b32*m.b74 + 15*m.b32*m.b77 + 16*m.b32*m.b80 + 17*
                       m.b32*m.b83 + 18*m.b32*m.b86 + 19*m.b32*m.b89 + 20*m.b32*m.b92 + 21*m.b32*m.b95 + 22*m.b32*m.b98
                        + 23*m.b32*m.b101 + 24*m.b32*m.b104 + 25*m.b32*m.b107 + 26*m.b32*m.b110 + 27*m.b32*m.b113 + 28*
                       m.b32*m.b116 + 29*m.b32*m.b119 + 30*m.b32*m.b122 + 31*m.b32*m.b125 + 32*m.b32*m.b128 + 33*m.b32*
                       m.b131 + 34*m.b32*m.b134 + 35*m.b32*m.b137 + 36*m.b32*m.b140 + 37*m.b32*m.b143 + 38*m.b32*m.b146
                        + 39*m.b32*m.b149 + 40*m.b32*m.b152 + 41*m.b32*m.b155 + 42*m.b32*m.b158 + 43*m.b32*m.b161 + 44*
                       m.b32*m.b164 + 45*m.b32*m.b167 + 46*m.b32*m.b170 + 47*m.b32*m.b173 + 48*m.b32*m.b176 + 49*m.b32*
                       m.b179 + 50*m.b32*m.b182 + 51*m.b32*m.b185 + 52*m.b32*m.b188 + 53*m.b32*m.b191 + 54*m.b32*m.b194
                        + 55*m.b32*m.b197 + 56*m.b32*m.b200 + 57*m.b32*m.b203 + 58*m.b32*m.b206 + 59*m.b32*m.b209 + 
                       m.b33*m.b36 + 2*m.b33*m.b39 + 3*m.b33*m.b42 + 4*m.b33*m.b45 + 5*m.b33*m.b48 + 6*m.b33*m.b51 + 7*
                       m.b33*m.b54 + 8*m.b33*m.b57 + 9*m.b33*m.b60 + 10*m.b33*m.b63 + 11*m.b33*m.b66 + 12*m.b33*m.b69 + 
                       13*m.b33*m.b72 + 14*m.b33*m.b75 + 15*m.b33*m.b78 + 16*m.b33*m.b81 + 17*m.b33*m.b84 + 18*m.b33*
                       m.b87 + 19*m.b33*m.b90 + 20*m.b33*m.b93 + 21*m.b33*m.b96 + 22*m.b33*m.b99 + 23*m.b33*m.b102 + 24*
                       m.b33*m.b105 + 25*m.b33*m.b108 + 26*m.b33*m.b111 + 27*m.b33*m.b114 + 28*m.b33*m.b117 + 29*m.b33*
                       m.b120 + 30*m.b33*m.b123 + 31*m.b33*m.b126 + 32*m.b33*m.b129 + 33*m.b33*m.b132 + 34*m.b33*m.b135
                        + 35*m.b33*m.b138 + 36*m.b33*m.b141 + 37*m.b33*m.b144 + 38*m.b33*m.b147 + 39*m.b33*m.b150 + 40*
                       m.b33*m.b153 + 41*m.b33*m.b156 + 42*m.b33*m.b159 + 43*m.b33*m.b162 + 44*m.b33*m.b165 + 45*m.b33*
                       m.b168 + 46*m.b33*m.b171 + 47*m.b33*m.b174 + 48*m.b33*m.b177 + 49*m.b33*m.b180 + 50*m.b33*m.b183
                        + 51*m.b33*m.b186 + 52*m.b33*m.b189 + 53*m.b33*m.b192 + 54*m.b33*m.b195 + 55*m.b33*m.b198 + 56*
                       m.b33*m.b201 + 57*m.b33*m.b204 + 58*m.b33*m.b207 + 59*m.b33*m.b210 + m.b34*m.b37 + 2*m.b34*m.b40
                        + 3*m.b34*m.b43 + 4*m.b34*m.b46 + 5*m.b34*m.b49 + 6*m.b34*m.b52 + 7*m.b34*m.b55 + 8*m.b34*m.b58
                        + 9*m.b34*m.b61 + 10*m.b34*m.b64 + 11*m.b34*m.b67 + 12*m.b34*m.b70 + 13*m.b34*m.b73 + 14*m.b34*
                       m.b76 + 15*m.b34*m.b79 + 16*m.b34*m.b82 + 17*m.b34*m.b85 + 18*m.b34*m.b88 + 19*m.b34*m.b91 + 20*
                       m.b34*m.b94 + 21*m.b34*m.b97 + 22*m.b34*m.b100 + 23*m.b34*m.b103 + 24*m.b34*m.b106 + 25*m.b34*
                       m.b109 + 26*m.b34*m.b112 + 27*m.b34*m.b115 + 28*m.b34*m.b118 + 29*m.b34*m.b121 + 30*m.b34*m.b124
                        + 31*m.b34*m.b127 + 32*m.b34*m.b130 + 33*m.b34*m.b133 + 34*m.b34*m.b136 + 35*m.b34*m.b139 + 36*
                       m.b34*m.b142 + 37*m.b34*m.b145 + 38*m.b34*m.b148 + 39*m.b34*m.b151 + 40*m.b34*m.b154 + 41*m.b34*
                       m.b157 + 42*m.b34*m.b160 + 43*m.b34*m.b163 + 44*m.b34*m.b166 + 45*m.b34*m.b169 + 46*m.b34*m.b172
                        + 47*m.b34*m.b175 + 48*m.b34*m.b178 + 49*m.b34*m.b181 + 50*m.b34*m.b184 + 51*m.b34*m.b187 + 52*
                       m.b34*m.b190 + 53*m.b34*m.b193 + 54*m.b34*m.b196 + 55*m.b34*m.b199 + 56*m.b34*m.b202 + 57*m.b34*
                       m.b205 + 58*m.b34*m.b208 + m.b35*m.b38 + 2*m.b35*m.b41 + 3*m.b35*m.b44 + 4*m.b35*m.b47 + 5*m.b35*
                       m.b50 + 6*m.b35*m.b53 + 7*m.b35*m.b56 + 8*m.b35*m.b59 + 9*m.b35*m.b62 + 10*m.b35*m.b65 + 11*m.b35
                       *m.b68 + 12*m.b35*m.b71 + 13*m.b35*m.b74 + 14*m.b35*m.b77 + 15*m.b35*m.b80 + 16*m.b35*m.b83 + 17*
                       m.b35*m.b86 + 18*m.b35*m.b89 + 19*m.b35*m.b92 + 20*m.b35*m.b95 + 21*m.b35*m.b98 + 22*m.b35*m.b101
                        + 23*m.b35*m.b104 + 24*m.b35*m.b107 + 25*m.b35*m.b110 + 26*m.b35*m.b113 + 27*m.b35*m.b116 + 28*
                       m.b35*m.b119 + 29*m.b35*m.b122 + 30*m.b35*m.b125 + 31*m.b35*m.b128 + 32*m.b35*m.b131 + 33*m.b35*
                       m.b134 + 34*m.b35*m.b137 + 35*m.b35*m.b140 + 36*m.b35*m.b143 + 37*m.b35*m.b146 + 38*m.b35*m.b149
                        + 39*m.b35*m.b152 + 40*m.b35*m.b155 + 41*m.b35*m.b158 + 42*m.b35*m.b161 + 43*m.b35*m.b164 + 44*
                       m.b35*m.b167 + 45*m.b35*m.b170 + 46*m.b35*m.b173 + 47*m.b35*m.b176 + 48*m.b35*m.b179 + 49*m.b35*
                       m.b182 + 50*m.b35*m.b185 + 51*m.b35*m.b188 + 52*m.b35*m.b191 + 53*m.b35*m.b194 + 54*m.b35*m.b197
                        + 55*m.b35*m.b200 + 56*m.b35*m.b203 + 57*m.b35*m.b206 + 58*m.b35*m.b209 + m.b36*m.b39 + 2*m.b36*
                       m.b42 + 3*m.b36*m.b45 + 4*m.b36*m.b48 + 5*m.b36*m.b51 + 6*m.b36*m.b54 + 7*m.b36*m.b57 + 8*m.b36*
                       m.b60 + 9*m.b36*m.b63 + 10*m.b36*m.b66 + 11*m.b36*m.b69 + 12*m.b36*m.b72 + 13*m.b36*m.b75 + 14*
                       m.b36*m.b78 + 15*m.b36*m.b81 + 16*m.b36*m.b84 + 17*m.b36*m.b87 + 18*m.b36*m.b90 + 19*m.b36*m.b93
                        + 20*m.b36*m.b96 + 21*m.b36*m.b99 + 22*m.b36*m.b102 + 23*m.b36*m.b105 + 24*m.b36*m.b108 + 25*
                       m.b36*m.b111 + 26*m.b36*m.b114 + 27*m.b36*m.b117 + 28*m.b36*m.b120 + 29*m.b36*m.b123 + 30*m.b36*
                       m.b126 + 31*m.b36*m.b129 + 32*m.b36*m.b132 + 33*m.b36*m.b135 + 34*m.b36*m.b138 + 35*m.b36*m.b141
                        + 36*m.b36*m.b144 + 37*m.b36*m.b147 + 38*m.b36*m.b150 + 39*m.b36*m.b153 + 40*m.b36*m.b156 + 41*
                       m.b36*m.b159 + 42*m.b36*m.b162 + 43*m.b36*m.b165 + 44*m.b36*m.b168 + 45*m.b36*m.b171 + 46*m.b36*
                       m.b174 + 47*m.b36*m.b177 + 48*m.b36*m.b180 + 49*m.b36*m.b183 + 50*m.b36*m.b186 + 51*m.b36*m.b189
                        + 52*m.b36*m.b192 + 53*m.b36*m.b195 + 54*m.b36*m.b198 + 55*m.b36*m.b201 + 56*m.b36*m.b204 + 57*
                       m.b36*m.b207 + 58*m.b36*m.b210 + m.b37*m.b40 + 2*m.b37*m.b43 + 3*m.b37*m.b46 + 4*m.b37*m.b49 + 5*
                       m.b37*m.b52 + 6*m.b37*m.b55 + 7*m.b37*m.b58 + 8*m.b37*m.b61 + 9*m.b37*m.b64 + 10*m.b37*m.b67 + 11
                       *m.b37*m.b70 + 12*m.b37*m.b73 + 13*m.b37*m.b76 + 14*m.b37*m.b79 + 15*m.b37*m.b82 + 16*m.b37*m.b85
                        + 17*m.b37*m.b88 + 18*m.b37*m.b91 + 19*m.b37*m.b94 + 20*m.b37*m.b97 + 21*m.b37*m.b100 + 22*m.b37
                       *m.b103 + 23*m.b37*m.b106 + 24*m.b37*m.b109 + 25*m.b37*m.b112 + 26*m.b37*m.b115 + 27*m.b37*m.b118
                        + 28*m.b37*m.b121 + 29*m.b37*m.b124 + 30*m.b37*m.b127 + 31*m.b37*m.b130 + 32*m.b37*m.b133 + 33*
                       m.b37*m.b136 + 34*m.b37*m.b139 + 35*m.b37*m.b142 + 36*m.b37*m.b145 + 37*m.b37*m.b148 + 38*m.b37*
                       m.b151 + 39*m.b37*m.b154 + 40*m.b37*m.b157 + 41*m.b37*m.b160 + 42*m.b37*m.b163 + 43*m.b37*m.b166
                        + 44*m.b37*m.b169 + 45*m.b37*m.b172 + 46*m.b37*m.b175 + 47*m.b37*m.b178 + 48*m.b37*m.b181 + 49*
                       m.b37*m.b184 + 50*m.b37*m.b187 + 51*m.b37*m.b190 + 52*m.b37*m.b193 + 53*m.b37*m.b196 + 54*m.b37*
                       m.b199 + 55*m.b37*m.b202 + 56*m.b37*m.b205 + 57*m.b37*m.b208 + m.b38*m.b41 + 2*m.b38*m.b44 + 3*
                       m.b38*m.b47 + 4*m.b38*m.b50 + 5*m.b38*m.b53 + 6*m.b38*m.b56 + 7*m.b38*m.b59 + 8*m.b38*m.b62 + 9*
                       m.b38*m.b65 + 10*m.b38*m.b68 + 11*m.b38*m.b71 + 12*m.b38*m.b74 + 13*m.b38*m.b77 + 14*m.b38*m.b80
                        + 15*m.b38*m.b83 + 16*m.b38*m.b86 + 17*m.b38*m.b89 + 18*m.b38*m.b92 + 19*m.b38*m.b95 + 20*m.b38*
                       m.b98 + 21*m.b38*m.b101 + 22*m.b38*m.b104 + 23*m.b38*m.b107 + 24*m.b38*m.b110 + 25*m.b38*m.b113
                        + 26*m.b38*m.b116 + 27*m.b38*m.b119 + 28*m.b38*m.b122 + 29*m.b38*m.b125 + 30*m.b38*m.b128 + 31*
                       m.b38*m.b131 + 32*m.b38*m.b134 + 33*m.b38*m.b137 + 34*m.b38*m.b140 + 35*m.b38*m.b143 + 36*m.b38*
                       m.b146 + 37*m.b38*m.b149 + 38*m.b38*m.b152 + 39*m.b38*m.b155 + 40*m.b38*m.b158 + 41*m.b38*m.b161
                        + 42*m.b38*m.b164 + 43*m.b38*m.b167 + 44*m.b38*m.b170 + 45*m.b38*m.b173 + 46*m.b38*m.b176 + 47*
                       m.b38*m.b179 + 48*m.b38*m.b182 + 49*m.b38*m.b185 + 50*m.b38*m.b188 + 51*m.b38*m.b191 + 52*m.b38*
                       m.b194 + 53*m.b38*m.b197 + 54*m.b38*m.b200 + 55*m.b38*m.b203 + 56*m.b38*m.b206 + 57*m.b38*m.b209
                        + m.b39*m.b42 + 2*m.b39*m.b45 + 3*m.b39*m.b48 + 4*m.b39*m.b51 + 5*m.b39*m.b54 + 6*m.b39*m.b57 + 
                       7*m.b39*m.b60 + 8*m.b39*m.b63 + 9*m.b39*m.b66 + 10*m.b39*m.b69 + 11*m.b39*m.b72 + 12*m.b39*m.b75
                        + 13*m.b39*m.b78 + 14*m.b39*m.b81 + 15*m.b39*m.b84 + 16*m.b39*m.b87 + 17*m.b39*m.b90 + 18*m.b39*
                       m.b93 + 19*m.b39*m.b96 + 20*m.b39*m.b99 + 21*m.b39*m.b102 + 22*m.b39*m.b105 + 23*m.b39*m.b108 + 
                       24*m.b39*m.b111 + 25*m.b39*m.b114 + 26*m.b39*m.b117 + 27*m.b39*m.b120 + 28*m.b39*m.b123 + 29*
                       m.b39*m.b126 + 30*m.b39*m.b129 + 31*m.b39*m.b132 + 32*m.b39*m.b135 + 33*m.b39*m.b138 + 34*m.b39*
                       m.b141 + 35*m.b39*m.b144 + 36*m.b39*m.b147 + 37*m.b39*m.b150 + 38*m.b39*m.b153 + 39*m.b39*m.b156
                        + 40*m.b39*m.b159 + 41*m.b39*m.b162 + 42*m.b39*m.b165 + 43*m.b39*m.b168 + 44*m.b39*m.b171 + 45*
                       m.b39*m.b174 + 46*m.b39*m.b177 + 47*m.b39*m.b180 + 48*m.b39*m.b183 + 49*m.b39*m.b186 + 50*m.b39*
                       m.b189 + 51*m.b39*m.b192 + 52*m.b39*m.b195 + 53*m.b39*m.b198 + 54*m.b39*m.b201 + 55*m.b39*m.b204
                        + 56*m.b39*m.b207 + 57*m.b39*m.b210 + m.b40*m.b43 + 2*m.b40*m.b46 + 3*m.b40*m.b49 + 4*m.b40*
                       m.b52 + 5*m.b40*m.b55 + 6*m.b40*m.b58 + 7*m.b40*m.b61 + 8*m.b40*m.b64 + 9*m.b40*m.b67 + 10*m.b40*
                       m.b70 + 11*m.b40*m.b73 + 12*m.b40*m.b76 + 13*m.b40*m.b79 + 14*m.b40*m.b82 + 15*m.b40*m.b85 + 16*
                       m.b40*m.b88 + 17*m.b40*m.b91 + 18*m.b40*m.b94 + 19*m.b40*m.b97 + 20*m.b40*m.b100 + 21*m.b40*
                       m.b103 + 22*m.b40*m.b106 + 23*m.b40*m.b109 + 24*m.b40*m.b112 + 25*m.b40*m.b115 + 26*m.b40*m.b118
                        + 27*m.b40*m.b121 + 28*m.b40*m.b124 + 29*m.b40*m.b127 + 30*m.b40*m.b130 + 31*m.b40*m.b133 + 32*
                       m.b40*m.b136 + 33*m.b40*m.b139 + 34*m.b40*m.b142 + 35*m.b40*m.b145 + 36*m.b40*m.b148 + 37*m.b40*
                       m.b151 + 38*m.b40*m.b154 + 39*m.b40*m.b157 + 40*m.b40*m.b160 + 41*m.b40*m.b163 + 42*m.b40*m.b166
                        + 43*m.b40*m.b169 + 44*m.b40*m.b172 + 45*m.b40*m.b175 + 46*m.b40*m.b178 + 47*m.b40*m.b181 + 48*
                       m.b40*m.b184 + 49*m.b40*m.b187 + 50*m.b40*m.b190 + 51*m.b40*m.b193 + 52*m.b40*m.b196 + 53*m.b40*
                       m.b199 + 54*m.b40*m.b202 + 55*m.b40*m.b205 + 56*m.b40*m.b208 + m.b41*m.b44 + 2*m.b41*m.b47 + 3*
                       m.b41*m.b50 + 4*m.b41*m.b53 + 5*m.b41*m.b56 + 6*m.b41*m.b59 + 7*m.b41*m.b62 + 8*m.b41*m.b65 + 9*
                       m.b41*m.b68 + 10*m.b41*m.b71 + 11*m.b41*m.b74 + 12*m.b41*m.b77 + 13*m.b41*m.b80 + 14*m.b41*m.b83
                        + 15*m.b41*m.b86 + 16*m.b41*m.b89 + 17*m.b41*m.b92 + 18*m.b41*m.b95 + 19*m.b41*m.b98 + 20*m.b41*
                       m.b101 + 21*m.b41*m.b104 + 22*m.b41*m.b107 + 23*m.b41*m.b110 + 24*m.b41*m.b113 + 25*m.b41*m.b116
                        + 26*m.b41*m.b119 + 27*m.b41*m.b122 + 28*m.b41*m.b125 + 29*m.b41*m.b128 + 30*m.b41*m.b131 + 31*
                       m.b41*m.b134 + 32*m.b41*m.b137 + 33*m.b41*m.b140 + 34*m.b41*m.b143 + 35*m.b41*m.b146 + 36*m.b41*
                       m.b149 + 37*m.b41*m.b152 + 38*m.b41*m.b155 + 39*m.b41*m.b158 + 40*m.b41*m.b161 + 41*m.b41*m.b164
                        + 42*m.b41*m.b167 + 43*m.b41*m.b170 + 44*m.b41*m.b173 + 45*m.b41*m.b176 + 46*m.b41*m.b179 + 47*
                       m.b41*m.b182 + 48*m.b41*m.b185 + 49*m.b41*m.b188 + 50*m.b41*m.b191 + 51*m.b41*m.b194 + 52*m.b41*
                       m.b197 + 53*m.b41*m.b200 + 54*m.b41*m.b203 + 55*m.b41*m.b206 + 56*m.b41*m.b209 + m.b42*m.b45 + 2*
                       m.b42*m.b48 + 3*m.b42*m.b51 + 4*m.b42*m.b54 + 5*m.b42*m.b57 + 6*m.b42*m.b60 + 7*m.b42*m.b63 + 8*
                       m.b42*m.b66 + 9*m.b42*m.b69 + 10*m.b42*m.b72 + 11*m.b42*m.b75 + 12*m.b42*m.b78 + 13*m.b42*m.b81
                        + 14*m.b42*m.b84 + 15*m.b42*m.b87 + 16*m.b42*m.b90 + 17*m.b42*m.b93 + 18*m.b42*m.b96 + 19*m.b42*
                       m.b99 + 20*m.b42*m.b102 + 21*m.b42*m.b105 + 22*m.b42*m.b108 + 23*m.b42*m.b111 + 24*m.b42*m.b114
                        + 25*m.b42*m.b117 + 26*m.b42*m.b120 + 27*m.b42*m.b123 + 28*m.b42*m.b126 + 29*m.b42*m.b129 + 30*
                       m.b42*m.b132 + 31*m.b42*m.b135 + 32*m.b42*m.b138 + 33*m.b42*m.b141 + 34*m.b42*m.b144 + 35*m.b42*
                       m.b147 + 36*m.b42*m.b150 + 37*m.b42*m.b153 + 38*m.b42*m.b156 + 39*m.b42*m.b159 + 40*m.b42*m.b162
                        + 41*m.b42*m.b165 + 42*m.b42*m.b168 + 43*m.b42*m.b171 + 44*m.b42*m.b174 + 45*m.b42*m.b177 + 46*
                       m.b42*m.b180 + 47*m.b42*m.b183 + 48*m.b42*m.b186 + 49*m.b42*m.b189 + 50*m.b42*m.b192 + 51*m.b42*
                       m.b195 + 52*m.b42*m.b198 + 53*m.b42*m.b201 + 54*m.b42*m.b204 + 55*m.b42*m.b207 + 56*m.b42*m.b210
                        + m.b43*m.b46 + 2*m.b43*m.b49 + 3*m.b43*m.b52 + 4*m.b43*m.b55 + 5*m.b43*m.b58 + 6*m.b43*m.b61 + 
                       7*m.b43*m.b64 + 8*m.b43*m.b67 + 9*m.b43*m.b70 + 10*m.b43*m.b73 + 11*m.b43*m.b76 + 12*m.b43*m.b79
                        + 13*m.b43*m.b82 + 14*m.b43*m.b85 + 15*m.b43*m.b88 + 16*m.b43*m.b91 + 17*m.b43*m.b94 + 18*m.b43*
                       m.b97 + 19*m.b43*m.b100 + 20*m.b43*m.b103 + 21*m.b43*m.b106 + 22*m.b43*m.b109 + 23*m.b43*m.b112
                        + 24*m.b43*m.b115 + 25*m.b43*m.b118 + 26*m.b43*m.b121 + 27*m.b43*m.b124 + 28*m.b43*m.b127 + 29*
                       m.b43*m.b130 + 30*m.b43*m.b133 + 31*m.b43*m.b136 + 32*m.b43*m.b139 + 33*m.b43*m.b142 + 34*m.b43*
                       m.b145 + 35*m.b43*m.b148 + 36*m.b43*m.b151 + 37*m.b43*m.b154 + 38*m.b43*m.b157 + 39*m.b43*m.b160
                        + 40*m.b43*m.b163 + 41*m.b43*m.b166 + 42*m.b43*m.b169 + 43*m.b43*m.b172 + 44*m.b43*m.b175 + 45*
                       m.b43*m.b178 + 46*m.b43*m.b181 + 47*m.b43*m.b184 + 48*m.b43*m.b187 + 49*m.b43*m.b190 + 50*m.b43*
                       m.b193 + 51*m.b43*m.b196 + 52*m.b43*m.b199 + 53*m.b43*m.b202 + 54*m.b43*m.b205 + 55*m.b43*m.b208
                        + m.b44*m.b47 + 2*m.b44*m.b50 + 3*m.b44*m.b53 + 4*m.b44*m.b56 + 5*m.b44*m.b59 + 6*m.b44*m.b62 + 
                       7*m.b44*m.b65 + 8*m.b44*m.b68 + 9*m.b44*m.b71 + 10*m.b44*m.b74 + 11*m.b44*m.b77 + 12*m.b44*m.b80
                        + 13*m.b44*m.b83 + 14*m.b44*m.b86 + 15*m.b44*m.b89 + 16*m.b44*m.b92 + 17*m.b44*m.b95 + 18*m.b44*
                       m.b98 + 19*m.b44*m.b101 + 20*m.b44*m.b104 + 21*m.b44*m.b107 + 22*m.b44*m.b110 + 23*m.b44*m.b113
                        + 24*m.b44*m.b116 + 25*m.b44*m.b119 + 26*m.b44*m.b122 + 27*m.b44*m.b125 + 28*m.b44*m.b128 + 29*
                       m.b44*m.b131 + 30*m.b44*m.b134 + 31*m.b44*m.b137 + 32*m.b44*m.b140 + 33*m.b44*m.b143 + 34*m.b44*
                       m.b146 + 35*m.b44*m.b149 + 36*m.b44*m.b152 + 37*m.b44*m.b155 + 38*m.b44*m.b158 + 39*m.b44*m.b161
                        + 40*m.b44*m.b164 + 41*m.b44*m.b167 + 42*m.b44*m.b170 + 43*m.b44*m.b173 + 44*m.b44*m.b176 + 45*
                       m.b44*m.b179 + 46*m.b44*m.b182 + 47*m.b44*m.b185 + 48*m.b44*m.b188 + 49*m.b44*m.b191 + 50*m.b44*
                       m.b194 + 51*m.b44*m.b197 + 52*m.b44*m.b200 + 53*m.b44*m.b203 + 54*m.b44*m.b206 + 55*m.b44*m.b209
                        + m.b45*m.b48 + 2*m.b45*m.b51 + 3*m.b45*m.b54 + 4*m.b45*m.b57 + 5*m.b45*m.b60 + 6*m.b45*m.b63 + 
                       7*m.b45*m.b66 + 8*m.b45*m.b69 + 9*m.b45*m.b72 + 10*m.b45*m.b75 + 11*m.b45*m.b78 + 12*m.b45*m.b81
                        + 13*m.b45*m.b84 + 14*m.b45*m.b87 + 15*m.b45*m.b90 + 16*m.b45*m.b93 + 17*m.b45*m.b96 + 18*m.b45*
                       m.b99 + 19*m.b45*m.b102 + 20*m.b45*m.b105 + 21*m.b45*m.b108 + 22*m.b45*m.b111 + 23*m.b45*m.b114
                        + 24*m.b45*m.b117 + 25*m.b45*m.b120 + 26*m.b45*m.b123 + 27*m.b45*m.b126 + 28*m.b45*m.b129 + 29*
                       m.b45*m.b132 + 30*m.b45*m.b135 + 31*m.b45*m.b138 + 32*m.b45*m.b141 + 33*m.b45*m.b144 + 34*m.b45*
                       m.b147 + 35*m.b45*m.b150 + 36*m.b45*m.b153 + 37*m.b45*m.b156 + 38*m.b45*m.b159 + 39*m.b45*m.b162
                        + 40*m.b45*m.b165 + 41*m.b45*m.b168 + 42*m.b45*m.b171 + 43*m.b45*m.b174 + 44*m.b45*m.b177 + 45*
                       m.b45*m.b180 + 46*m.b45*m.b183 + 47*m.b45*m.b186 + 48*m.b45*m.b189 + 49*m.b45*m.b192 + 50*m.b45*
                       m.b195 + 51*m.b45*m.b198 + 52*m.b45*m.b201 + 53*m.b45*m.b204 + 54*m.b45*m.b207 + 55*m.b45*m.b210
                        + m.b46*m.b49 + 2*m.b46*m.b52 + 3*m.b46*m.b55 + 4*m.b46*m.b58 + 5*m.b46*m.b61 + 6*m.b46*m.b64 + 
                       7*m.b46*m.b67 + 8*m.b46*m.b70 + 9*m.b46*m.b73 + 10*m.b46*m.b76 + 11*m.b46*m.b79 + 12*m.b46*m.b82
                        + 13*m.b46*m.b85 + 14*m.b46*m.b88 + 15*m.b46*m.b91 + 16*m.b46*m.b94 + 17*m.b46*m.b97 + 18*m.b46*
                       m.b100 + 19*m.b46*m.b103 + 20*m.b46*m.b106 + 21*m.b46*m.b109 + 22*m.b46*m.b112 + 23*m.b46*m.b115
                        + 24*m.b46*m.b118 + 25*m.b46*m.b121 + 26*m.b46*m.b124 + 27*m.b46*m.b127 + 28*m.b46*m.b130 + 29*
                       m.b46*m.b133 + 30*m.b46*m.b136 + 31*m.b46*m.b139 + 32*m.b46*m.b142 + 33*m.b46*m.b145 + 34*m.b46*
                       m.b148 + 35*m.b46*m.b151 + 36*m.b46*m.b154 + 37*m.b46*m.b157 + 38*m.b46*m.b160 + 39*m.b46*m.b163
                        + 40*m.b46*m.b166 + 41*m.b46*m.b169 + 42*m.b46*m.b172 + 43*m.b46*m.b175 + 44*m.b46*m.b178 + 45*
                       m.b46*m.b181 + 46*m.b46*m.b184 + 47*m.b46*m.b187 + 48*m.b46*m.b190 + 49*m.b46*m.b193 + 50*m.b46*
                       m.b196 + 51*m.b46*m.b199 + 52*m.b46*m.b202 + 53*m.b46*m.b205 + 54*m.b46*m.b208 + m.b47*m.b50 + 2*
                       m.b47*m.b53 + 3*m.b47*m.b56 + 4*m.b47*m.b59 + 5*m.b47*m.b62 + 6*m.b47*m.b65 + 7*m.b47*m.b68 + 8*
                       m.b47*m.b71 + 9*m.b47*m.b74 + 10*m.b47*m.b77 + 11*m.b47*m.b80 + 12*m.b47*m.b83 + 13*m.b47*m.b86
                        + 14*m.b47*m.b89 + 15*m.b47*m.b92 + 16*m.b47*m.b95 + 17*m.b47*m.b98 + 18*m.b47*m.b101 + 19*m.b47
                       *m.b104 + 20*m.b47*m.b107 + 21*m.b47*m.b110 + 22*m.b47*m.b113 + 23*m.b47*m.b116 + 24*m.b47*m.b119
                        + 25*m.b47*m.b122 + 26*m.b47*m.b125 + 27*m.b47*m.b128 + 28*m.b47*m.b131 + 29*m.b47*m.b134 + 30*
                       m.b47*m.b137 + 31*m.b47*m.b140 + 32*m.b47*m.b143 + 33*m.b47*m.b146 + 34*m.b47*m.b149 + 35*m.b47*
                       m.b152 + 36*m.b47*m.b155 + 37*m.b47*m.b158 + 38*m.b47*m.b161 + 39*m.b47*m.b164 + 40*m.b47*m.b167
                        + 41*m.b47*m.b170 + 42*m.b47*m.b173 + 43*m.b47*m.b176 + 44*m.b47*m.b179 + 45*m.b47*m.b182 + 46*
                       m.b47*m.b185 + 47*m.b47*m.b188 + 48*m.b47*m.b191 + 49*m.b47*m.b194 + 50*m.b47*m.b197 + 51*m.b47*
                       m.b200 + 52*m.b47*m.b203 + 53*m.b47*m.b206 + 54*m.b47*m.b209 + m.b48*m.b51 + 2*m.b48*m.b54 + 3*
                       m.b48*m.b57 + 4*m.b48*m.b60 + 5*m.b48*m.b63 + 6*m.b48*m.b66 + 7*m.b48*m.b69 + 8*m.b48*m.b72 + 9*
                       m.b48*m.b75 + 10*m.b48*m.b78 + 11*m.b48*m.b81 + 12*m.b48*m.b84 + 13*m.b48*m.b87 + 14*m.b48*m.b90
                        + 15*m.b48*m.b93 + 16*m.b48*m.b96 + 17*m.b48*m.b99 + 18*m.b48*m.b102 + 19*m.b48*m.b105 + 20*
                       m.b48*m.b108 + 21*m.b48*m.b111 + 22*m.b48*m.b114 + 23*m.b48*m.b117 + 24*m.b48*m.b120 + 25*m.b48*
                       m.b123 + 26*m.b48*m.b126 + 27*m.b48*m.b129 + 28*m.b48*m.b132 + 29*m.b48*m.b135 + 30*m.b48*m.b138
                        + 31*m.b48*m.b141 + 32*m.b48*m.b144 + 33*m.b48*m.b147 + 34*m.b48*m.b150 + 35*m.b48*m.b153 + 36*
                       m.b48*m.b156 + 37*m.b48*m.b159 + 38*m.b48*m.b162 + 39*m.b48*m.b165 + 40*m.b48*m.b168 + 41*m.b48*
                       m.b171 + 42*m.b48*m.b174 + 43*m.b48*m.b177 + 44*m.b48*m.b180 + 45*m.b48*m.b183 + 46*m.b48*m.b186
                        + 47*m.b48*m.b189 + 48*m.b48*m.b192 + 49*m.b48*m.b195 + 50*m.b48*m.b198 + 51*m.b48*m.b201 + 52*
                       m.b48*m.b204 + 53*m.b48*m.b207 + 54*m.b48*m.b210 + m.b49*m.b52 + 2*m.b49*m.b55 + 3*m.b49*m.b58 + 
                       4*m.b49*m.b61 + 5*m.b49*m.b64 + 6*m.b49*m.b67 + 7*m.b49*m.b70 + 8*m.b49*m.b73 + 9*m.b49*m.b76 + 
                       10*m.b49*m.b79 + 11*m.b49*m.b82 + 12*m.b49*m.b85 + 13*m.b49*m.b88 + 14*m.b49*m.b91 + 15*m.b49*
                       m.b94 + 16*m.b49*m.b97 + 17*m.b49*m.b100 + 18*m.b49*m.b103 + 19*m.b49*m.b106 + 20*m.b49*m.b109 + 
                       21*m.b49*m.b112 + 22*m.b49*m.b115 + 23*m.b49*m.b118 + 24*m.b49*m.b121 + 25*m.b49*m.b124 + 26*
                       m.b49*m.b127 + 27*m.b49*m.b130 + 28*m.b49*m.b133 + 29*m.b49*m.b136 + 30*m.b49*m.b139 + 31*m.b49*
                       m.b142 + 32*m.b49*m.b145 + 33*m.b49*m.b148 + 34*m.b49*m.b151 + 35*m.b49*m.b154 + 36*m.b49*m.b157
                        + 37*m.b49*m.b160 + 38*m.b49*m.b163 + 39*m.b49*m.b166 + 40*m.b49*m.b169 + 41*m.b49*m.b172 + 42*
                       m.b49*m.b175 + 43*m.b49*m.b178 + 44*m.b49*m.b181 + 45*m.b49*m.b184 + 46*m.b49*m.b187 + 47*m.b49*
                       m.b190 + 48*m.b49*m.b193 + 49*m.b49*m.b196 + 50*m.b49*m.b199 + 51*m.b49*m.b202 + 52*m.b49*m.b205
                        + 53*m.b49*m.b208 + m.b50*m.b53 + 2*m.b50*m.b56 + 3*m.b50*m.b59 + 4*m.b50*m.b62 + 5*m.b50*m.b65
                        + 6*m.b50*m.b68 + 7*m.b50*m.b71 + 8*m.b50*m.b74 + 9*m.b50*m.b77 + 10*m.b50*m.b80 + 11*m.b50*
                       m.b83 + 12*m.b50*m.b86 + 13*m.b50*m.b89 + 14*m.b50*m.b92 + 15*m.b50*m.b95 + 16*m.b50*m.b98 + 17*
                       m.b50*m.b101 + 18*m.b50*m.b104 + 19*m.b50*m.b107 + 20*m.b50*m.b110 + 21*m.b50*m.b113 + 22*m.b50*
                       m.b116 + 23*m.b50*m.b119 + 24*m.b50*m.b122 + 25*m.b50*m.b125 + 26*m.b50*m.b128 + 27*m.b50*m.b131
                        + 28*m.b50*m.b134 + 29*m.b50*m.b137 + 30*m.b50*m.b140 + 31*m.b50*m.b143 + 32*m.b50*m.b146 + 33*
                       m.b50*m.b149 + 34*m.b50*m.b152 + 35*m.b50*m.b155 + 36*m.b50*m.b158 + 37*m.b50*m.b161 + 38*m.b50*
                       m.b164 + 39*m.b50*m.b167 + 40*m.b50*m.b170 + 41*m.b50*m.b173 + 42*m.b50*m.b176 + 43*m.b50*m.b179
                        + 44*m.b50*m.b182 + 45*m.b50*m.b185 + 46*m.b50*m.b188 + 47*m.b50*m.b191 + 48*m.b50*m.b194 + 49*
                       m.b50*m.b197 + 50*m.b50*m.b200 + 51*m.b50*m.b203 + 52*m.b50*m.b206 + 53*m.b50*m.b209 + m.b51*
                       m.b54 + 2*m.b51*m.b57 + 3*m.b51*m.b60 + 4*m.b51*m.b63 + 5*m.b51*m.b66 + 6*m.b51*m.b69 + 7*m.b51*
                       m.b72 + 8*m.b51*m.b75 + 9*m.b51*m.b78 + 10*m.b51*m.b81 + 11*m.b51*m.b84 + 12*m.b51*m.b87 + 13*
                       m.b51*m.b90 + 14*m.b51*m.b93 + 15*m.b51*m.b96 + 16*m.b51*m.b99 + 17*m.b51*m.b102 + 18*m.b51*
                       m.b105 + 19*m.b51*m.b108 + 20*m.b51*m.b111 + 21*m.b51*m.b114 + 22*m.b51*m.b117 + 23*m.b51*m.b120
                        + 24*m.b51*m.b123 + 25*m.b51*m.b126 + 26*m.b51*m.b129 + 27*m.b51*m.b132 + 28*m.b51*m.b135 + 29*
                       m.b51*m.b138 + 30*m.b51*m.b141 + 31*m.b51*m.b144 + 32*m.b51*m.b147 + 33*m.b51*m.b150 + 34*m.b51*
                       m.b153 + 35*m.b51*m.b156 + 36*m.b51*m.b159 + 37*m.b51*m.b162 + 38*m.b51*m.b165 + 39*m.b51*m.b168
                        + 40*m.b51*m.b171 + 41*m.b51*m.b174 + 42*m.b51*m.b177 + 43*m.b51*m.b180 + 44*m.b51*m.b183 + 45*
                       m.b51*m.b186 + 46*m.b51*m.b189 + 47*m.b51*m.b192 + 48*m.b51*m.b195 + 49*m.b51*m.b198 + 50*m.b51*
                       m.b201 + 51*m.b51*m.b204 + 52*m.b51*m.b207 + 53*m.b51*m.b210 + m.b52*m.b55 + 2*m.b52*m.b58 + 3*
                       m.b52*m.b61 + 4*m.b52*m.b64 + 5*m.b52*m.b67 + 6*m.b52*m.b70 + 7*m.b52*m.b73 + 8*m.b52*m.b76 + 9*
                       m.b52*m.b79 + 10*m.b52*m.b82 + 11*m.b52*m.b85 + 12*m.b52*m.b88 + 13*m.b52*m.b91 + 14*m.b52*m.b94
                        + 15*m.b52*m.b97 + 16*m.b52*m.b100 + 17*m.b52*m.b103 + 18*m.b52*m.b106 + 19*m.b52*m.b109 + 20*
                       m.b52*m.b112 + 21*m.b52*m.b115 + 22*m.b52*m.b118 + 23*m.b52*m.b121 + 24*m.b52*m.b124 + 25*m.b52*
                       m.b127 + 26*m.b52*m.b130 + 27*m.b52*m.b133 + 28*m.b52*m.b136 + 29*m.b52*m.b139 + 30*m.b52*m.b142
                        + 31*m.b52*m.b145 + 32*m.b52*m.b148 + 33*m.b52*m.b151 + 34*m.b52*m.b154 + 35*m.b52*m.b157 + 36*
                       m.b52*m.b160 + 37*m.b52*m.b163 + 38*m.b52*m.b166 + 39*m.b52*m.b169 + 40*m.b52*m.b172 + 41*m.b52*
                       m.b175 + 42*m.b52*m.b178 + 43*m.b52*m.b181 + 44*m.b52*m.b184 + 45*m.b52*m.b187 + 46*m.b52*m.b190
                        + 47*m.b52*m.b193 + 48*m.b52*m.b196 + 49*m.b52*m.b199 + 50*m.b52*m.b202 + 51*m.b52*m.b205 + 52*
                       m.b52*m.b208 + m.b53*m.b56 + 2*m.b53*m.b59 + 3*m.b53*m.b62 + 4*m.b53*m.b65 + 5*m.b53*m.b68 + 6*
                       m.b53*m.b71 + 7*m.b53*m.b74 + 8*m.b53*m.b77 + 9*m.b53*m.b80 + 10*m.b53*m.b83 + 11*m.b53*m.b86 + 
                       12*m.b53*m.b89 + 13*m.b53*m.b92 + 14*m.b53*m.b95 + 15*m.b53*m.b98 + 16*m.b53*m.b101 + 17*m.b53*
                       m.b104 + 18*m.b53*m.b107 + 19*m.b53*m.b110 + 20*m.b53*m.b113 + 21*m.b53*m.b116 + 22*m.b53*m.b119
                        + 23*m.b53*m.b122 + 24*m.b53*m.b125 + 25*m.b53*m.b128 + 26*m.b53*m.b131 + 27*m.b53*m.b134 + 28*
                       m.b53*m.b137 + 29*m.b53*m.b140 + 30*m.b53*m.b143 + 31*m.b53*m.b146 + 32*m.b53*m.b149 + 33*m.b53*
                       m.b152 + 34*m.b53*m.b155 + 35*m.b53*m.b158 + 36*m.b53*m.b161 + 37*m.b53*m.b164 + 38*m.b53*m.b167
                        + 39*m.b53*m.b170 + 40*m.b53*m.b173 + 41*m.b53*m.b176 + 42*m.b53*m.b179 + 43*m.b53*m.b182 + 44*
                       m.b53*m.b185 + 45*m.b53*m.b188 + 46*m.b53*m.b191 + 47*m.b53*m.b194 + 48*m.b53*m.b197 + 49*m.b53*
                       m.b200 + 50*m.b53*m.b203 + 51*m.b53*m.b206 + 52*m.b53*m.b209 + m.b54*m.b57 + 2*m.b54*m.b60 + 3*
                       m.b54*m.b63 + 4*m.b54*m.b66 + 5*m.b54*m.b69 + 6*m.b54*m.b72 + 7*m.b54*m.b75 + 8*m.b54*m.b78 + 9*
                       m.b54*m.b81 + 10*m.b54*m.b84 + 11*m.b54*m.b87 + 12*m.b54*m.b90 + 13*m.b54*m.b93 + 14*m.b54*m.b96
                        + 15*m.b54*m.b99 + 16*m.b54*m.b102 + 17*m.b54*m.b105 + 18*m.b54*m.b108 + 19*m.b54*m.b111 + 20*
                       m.b54*m.b114 + 21*m.b54*m.b117 + 22*m.b54*m.b120 + 23*m.b54*m.b123 + 24*m.b54*m.b126 + 25*m.b54*
                       m.b129 + 26*m.b54*m.b132 + 27*m.b54*m.b135 + 28*m.b54*m.b138 + 29*m.b54*m.b141 + 30*m.b54*m.b144
                        + 31*m.b54*m.b147 + 32*m.b54*m.b150 + 33*m.b54*m.b153 + 34*m.b54*m.b156 + 35*m.b54*m.b159 + 36*
                       m.b54*m.b162 + 37*m.b54*m.b165 + 38*m.b54*m.b168 + 39*m.b54*m.b171 + 40*m.b54*m.b174 + 41*m.b54*
                       m.b177 + 42*m.b54*m.b180 + 43*m.b54*m.b183 + 44*m.b54*m.b186 + 45*m.b54*m.b189 + 46*m.b54*m.b192
                        + 47*m.b54*m.b195 + 48*m.b54*m.b198 + 49*m.b54*m.b201 + 50*m.b54*m.b204 + 51*m.b54*m.b207 + 52*
                       m.b54*m.b210 + m.b55*m.b58 + 2*m.b55*m.b61 + 3*m.b55*m.b64 + 4*m.b55*m.b67 + 5*m.b55*m.b70 + 6*
                       m.b55*m.b73 + 7*m.b55*m.b76 + 8*m.b55*m.b79 + 9*m.b55*m.b82 + 10*m.b55*m.b85 + 11*m.b55*m.b88 + 
                       12*m.b55*m.b91 + 13*m.b55*m.b94 + 14*m.b55*m.b97 + 15*m.b55*m.b100 + 16*m.b55*m.b103 + 17*m.b55*
                       m.b106 + 18*m.b55*m.b109 + 19*m.b55*m.b112 + 20*m.b55*m.b115 + 21*m.b55*m.b118 + 22*m.b55*m.b121
                        + 23*m.b55*m.b124 + 24*m.b55*m.b127 + 25*m.b55*m.b130 + 26*m.b55*m.b133 + 27*m.b55*m.b136 + 28*
                       m.b55*m.b139 + 29*m.b55*m.b142 + 30*m.b55*m.b145 + 31*m.b55*m.b148 + 32*m.b55*m.b151 + 33*m.b55*
                       m.b154 + 34*m.b55*m.b157 + 35*m.b55*m.b160 + 36*m.b55*m.b163 + 37*m.b55*m.b166 + 38*m.b55*m.b169
                        + 39*m.b55*m.b172 + 40*m.b55*m.b175 + 41*m.b55*m.b178 + 42*m.b55*m.b181 + 43*m.b55*m.b184 + 44*
                       m.b55*m.b187 + 45*m.b55*m.b190 + 46*m.b55*m.b193 + 47*m.b55*m.b196 + 48*m.b55*m.b199 + 49*m.b55*
                       m.b202 + 50*m.b55*m.b205 + 51*m.b55*m.b208 + m.b56*m.b59 + 2*m.b56*m.b62 + 3*m.b56*m.b65 + 4*
                       m.b56*m.b68 + 5*m.b56*m.b71 + 6*m.b56*m.b74 + 7*m.b56*m.b77 + 8*m.b56*m.b80 + 9*m.b56*m.b83 + 10*
                       m.b56*m.b86 + 11*m.b56*m.b89 + 12*m.b56*m.b92 + 13*m.b56*m.b95 + 14*m.b56*m.b98 + 15*m.b56*m.b101
                        + 16*m.b56*m.b104 + 17*m.b56*m.b107 + 18*m.b56*m.b110 + 19*m.b56*m.b113 + 20*m.b56*m.b116 + 21*
                       m.b56*m.b119 + 22*m.b56*m.b122 + 23*m.b56*m.b125 + 24*m.b56*m.b128 + 25*m.b56*m.b131 + 26*m.b56*
                       m.b134 + 27*m.b56*m.b137 + 28*m.b56*m.b140 + 29*m.b56*m.b143 + 30*m.b56*m.b146 + 31*m.b56*m.b149
                        + 32*m.b56*m.b152 + 33*m.b56*m.b155 + 34*m.b56*m.b158 + 35*m.b56*m.b161 + 36*m.b56*m.b164 + 37*
                       m.b56*m.b167 + 38*m.b56*m.b170 + 39*m.b56*m.b173 + 40*m.b56*m.b176 + 41*m.b56*m.b179 + 42*m.b56*
                       m.b182 + 43*m.b56*m.b185 + 44*m.b56*m.b188 + 45*m.b56*m.b191 + 46*m.b56*m.b194 + 47*m.b56*m.b197
                        + 48*m.b56*m.b200 + 49*m.b56*m.b203 + 50*m.b56*m.b206 + 51*m.b56*m.b209 + m.b57*m.b60 + 2*m.b57*
                       m.b63 + 3*m.b57*m.b66 + 4*m.b57*m.b69 + 5*m.b57*m.b72 + 6*m.b57*m.b75 + 7*m.b57*m.b78 + 8*m.b57*
                       m.b81 + 9*m.b57*m.b84 + 10*m.b57*m.b87 + 11*m.b57*m.b90 + 12*m.b57*m.b93 + 13*m.b57*m.b96 + 14*
                       m.b57*m.b99 + 15*m.b57*m.b102 + 16*m.b57*m.b105 + 17*m.b57*m.b108 + 18*m.b57*m.b111 + 19*m.b57*
                       m.b114 + 20*m.b57*m.b117 + 21*m.b57*m.b120 + 22*m.b57*m.b123 + 23*m.b57*m.b126 + 24*m.b57*m.b129
                        + 25*m.b57*m.b132 + 26*m.b57*m.b135 + 27*m.b57*m.b138 + 28*m.b57*m.b141 + 29*m.b57*m.b144 + 30*
                       m.b57*m.b147 + 31*m.b57*m.b150 + 32*m.b57*m.b153 + 33*m.b57*m.b156 + 34*m.b57*m.b159 + 35*m.b57*
                       m.b162 + 36*m.b57*m.b165 + 37*m.b57*m.b168 + 38*m.b57*m.b171 + 39*m.b57*m.b174 + 40*m.b57*m.b177
                        + 41*m.b57*m.b180 + 42*m.b57*m.b183 + 43*m.b57*m.b186 + 44*m.b57*m.b189 + 45*m.b57*m.b192 + 46*
                       m.b57*m.b195 + 47*m.b57*m.b198 + 48*m.b57*m.b201 + 49*m.b57*m.b204 + 50*m.b57*m.b207 + 51*m.b57*
                       m.b210 + m.b58*m.b61 + 2*m.b58*m.b64 + 3*m.b58*m.b67 + 4*m.b58*m.b70 + 5*m.b58*m.b73 + 6*m.b58*
                       m.b76 + 7*m.b58*m.b79 + 8*m.b58*m.b82 + 9*m.b58*m.b85 + 10*m.b58*m.b88 + 11*m.b58*m.b91 + 12*
                       m.b58*m.b94 + 13*m.b58*m.b97 + 14*m.b58*m.b100 + 15*m.b58*m.b103 + 16*m.b58*m.b106 + 17*m.b58*
                       m.b109 + 18*m.b58*m.b112 + 19*m.b58*m.b115 + 20*m.b58*m.b118 + 21*m.b58*m.b121 + 22*m.b58*m.b124
                        + 23*m.b58*m.b127 + 24*m.b58*m.b130 + 25*m.b58*m.b133 + 26*m.b58*m.b136 + 27*m.b58*m.b139 + 28*
                       m.b58*m.b142 + 29*m.b58*m.b145 + 30*m.b58*m.b148 + 31*m.b58*m.b151 + 32*m.b58*m.b154 + 33*m.b58*
                       m.b157 + 34*m.b58*m.b160 + 35*m.b58*m.b163 + 36*m.b58*m.b166 + 37*m.b58*m.b169 + 38*m.b58*m.b172
                        + 39*m.b58*m.b175 + 40*m.b58*m.b178 + 41*m.b58*m.b181 + 42*m.b58*m.b184 + 43*m.b58*m.b187 + 44*
                       m.b58*m.b190 + 45*m.b58*m.b193 + 46*m.b58*m.b196 + 47*m.b58*m.b199 + 48*m.b58*m.b202 + 49*m.b58*
                       m.b205 + 50*m.b58*m.b208 + m.b59*m.b62 + 2*m.b59*m.b65 + 3*m.b59*m.b68 + 4*m.b59*m.b71 + 5*m.b59*
                       m.b74 + 6*m.b59*m.b77 + 7*m.b59*m.b80 + 8*m.b59*m.b83 + 9*m.b59*m.b86 + 10*m.b59*m.b89 + 11*m.b59
                       *m.b92 + 12*m.b59*m.b95 + 13*m.b59*m.b98 + 14*m.b59*m.b101 + 15*m.b59*m.b104 + 16*m.b59*m.b107 + 
                       17*m.b59*m.b110 + 18*m.b59*m.b113 + 19*m.b59*m.b116 + 20*m.b59*m.b119 + 21*m.b59*m.b122 + 22*
                       m.b59*m.b125 + 23*m.b59*m.b128 + 24*m.b59*m.b131 + 25*m.b59*m.b134 + 26*m.b59*m.b137 + 27*m.b59*
                       m.b140 + 28*m.b59*m.b143 + 29*m.b59*m.b146 + 30*m.b59*m.b149 + 31*m.b59*m.b152 + 32*m.b59*m.b155
                        + 33*m.b59*m.b158 + 34*m.b59*m.b161 + 35*m.b59*m.b164 + 36*m.b59*m.b167 + 37*m.b59*m.b170 + 38*
                       m.b59*m.b173 + 39*m.b59*m.b176 + 40*m.b59*m.b179 + 41*m.b59*m.b182 + 42*m.b59*m.b185 + 43*m.b59*
                       m.b188 + 44*m.b59*m.b191 + 45*m.b59*m.b194 + 46*m.b59*m.b197 + 47*m.b59*m.b200 + 48*m.b59*m.b203
                        + 49*m.b59*m.b206 + 50*m.b59*m.b209 + m.b60*m.b63 + 2*m.b60*m.b66 + 3*m.b60*m.b69 + 4*m.b60*
                       m.b72 + 5*m.b60*m.b75 + 6*m.b60*m.b78 + 7*m.b60*m.b81 + 8*m.b60*m.b84 + 9*m.b60*m.b87 + 10*m.b60*
                       m.b90 + 11*m.b60*m.b93 + 12*m.b60*m.b96 + 13*m.b60*m.b99 + 14*m.b60*m.b102 + 15*m.b60*m.b105 + 16
                       *m.b60*m.b108 + 17*m.b60*m.b111 + 18*m.b60*m.b114 + 19*m.b60*m.b117 + 20*m.b60*m.b120 + 21*m.b60*
                       m.b123 + 22*m.b60*m.b126 + 23*m.b60*m.b129 + 24*m.b60*m.b132 + 25*m.b60*m.b135 + 26*m.b60*m.b138
                        + 27*m.b60*m.b141 + 28*m.b60*m.b144 + 29*m.b60*m.b147 + 30*m.b60*m.b150 + 31*m.b60*m.b153 + 32*
                       m.b60*m.b156 + 33*m.b60*m.b159 + 34*m.b60*m.b162 + 35*m.b60*m.b165 + 36*m.b60*m.b168 + 37*m.b60*
                       m.b171 + 38*m.b60*m.b174 + 39*m.b60*m.b177 + 40*m.b60*m.b180 + 41*m.b60*m.b183 + 42*m.b60*m.b186
                        + 43*m.b60*m.b189 + 44*m.b60*m.b192 + 45*m.b60*m.b195 + 46*m.b60*m.b198 + 47*m.b60*m.b201 + 48*
                       m.b60*m.b204 + 49*m.b60*m.b207 + 50*m.b60*m.b210 + m.b61*m.b64 + 2*m.b61*m.b67 + 3*m.b61*m.b70 + 
                       4*m.b61*m.b73 + 5*m.b61*m.b76 + 6*m.b61*m.b79 + 7*m.b61*m.b82 + 8*m.b61*m.b85 + 9*m.b61*m.b88 + 
                       10*m.b61*m.b91 + 11*m.b61*m.b94 + 12*m.b61*m.b97 + 13*m.b61*m.b100 + 14*m.b61*m.b103 + 15*m.b61*
                       m.b106 + 16*m.b61*m.b109 + 17*m.b61*m.b112 + 18*m.b61*m.b115 + 19*m.b61*m.b118 + 20*m.b61*m.b121
                        + 21*m.b61*m.b124 + 22*m.b61*m.b127 + 23*m.b61*m.b130 + 24*m.b61*m.b133 + 25*m.b61*m.b136 + 26*
                       m.b61*m.b139 + 27*m.b61*m.b142 + 28*m.b61*m.b145 + 29*m.b61*m.b148 + 30*m.b61*m.b151 + 31*m.b61*
                       m.b154 + 32*m.b61*m.b157 + 33*m.b61*m.b160 + 34*m.b61*m.b163 + 35*m.b61*m.b166 + 36*m.b61*m.b169
                        + 37*m.b61*m.b172 + 38*m.b61*m.b175 + 39*m.b61*m.b178 + 40*m.b61*m.b181 + 41*m.b61*m.b184 + 42*
                       m.b61*m.b187 + 43*m.b61*m.b190 + 44*m.b61*m.b193 + 45*m.b61*m.b196 + 46*m.b61*m.b199 + 47*m.b61*
                       m.b202 + 48*m.b61*m.b205 + 49*m.b61*m.b208 + m.b62*m.b65 + 2*m.b62*m.b68 + 3*m.b62*m.b71 + 4*
                       m.b62*m.b74 + 5*m.b62*m.b77 + 6*m.b62*m.b80 + 7*m.b62*m.b83 + 8*m.b62*m.b86 + 9*m.b62*m.b89 + 10*
                       m.b62*m.b92 + 11*m.b62*m.b95 + 12*m.b62*m.b98 + 13*m.b62*m.b101 + 14*m.b62*m.b104 + 15*m.b62*
                       m.b107 + 16*m.b62*m.b110 + 17*m.b62*m.b113 + 18*m.b62*m.b116 + 19*m.b62*m.b119 + 20*m.b62*m.b122
                        + 21*m.b62*m.b125 + 22*m.b62*m.b128 + 23*m.b62*m.b131 + 24*m.b62*m.b134 + 25*m.b62*m.b137 + 26*
                       m.b62*m.b140 + 27*m.b62*m.b143 + 28*m.b62*m.b146 + 29*m.b62*m.b149 + 30*m.b62*m.b152 + 31*m.b62*
                       m.b155 + 32*m.b62*m.b158 + 33*m.b62*m.b161 + 34*m.b62*m.b164 + 35*m.b62*m.b167 + 36*m.b62*m.b170
                        + 37*m.b62*m.b173 + 38*m.b62*m.b176 + 39*m.b62*m.b179 + 40*m.b62*m.b182 + 41*m.b62*m.b185 + 42*
                       m.b62*m.b188 + 43*m.b62*m.b191 + 44*m.b62*m.b194 + 45*m.b62*m.b197 + 46*m.b62*m.b200 + 47*m.b62*
                       m.b203 + 48*m.b62*m.b206 + 49*m.b62*m.b209 + m.b63*m.b66 + 2*m.b63*m.b69 + 3*m.b63*m.b72 + 4*
                       m.b63*m.b75 + 5*m.b63*m.b78 + 6*m.b63*m.b81 + 7*m.b63*m.b84 + 8*m.b63*m.b87 + 9*m.b63*m.b90 + 10*
                       m.b63*m.b93 + 11*m.b63*m.b96 + 12*m.b63*m.b99 + 13*m.b63*m.b102 + 14*m.b63*m.b105 + 15*m.b63*
                       m.b108 + 16*m.b63*m.b111 + 17*m.b63*m.b114 + 18*m.b63*m.b117 + 19*m.b63*m.b120 + 20*m.b63*m.b123
                        + 21*m.b63*m.b126 + 22*m.b63*m.b129 + 23*m.b63*m.b132 + 24*m.b63*m.b135 + 25*m.b63*m.b138 + 26*
                       m.b63*m.b141 + 27*m.b63*m.b144 + 28*m.b63*m.b147 + 29*m.b63*m.b150 + 30*m.b63*m.b153 + 31*m.b63*
                       m.b156 + 32*m.b63*m.b159 + 33*m.b63*m.b162 + 34*m.b63*m.b165 + 35*m.b63*m.b168 + 36*m.b63*m.b171
                        + 37*m.b63*m.b174 + 38*m.b63*m.b177 + 39*m.b63*m.b180 + 40*m.b63*m.b183 + 41*m.b63*m.b186 + 42*
                       m.b63*m.b189 + 43*m.b63*m.b192 + 44*m.b63*m.b195 + 45*m.b63*m.b198 + 46*m.b63*m.b201 + 47*m.b63*
                       m.b204 + 48*m.b63*m.b207 + 49*m.b63*m.b210 + m.b64*m.b67 + 2*m.b64*m.b70 + 3*m.b64*m.b73 + 4*
                       m.b64*m.b76 + 5*m.b64*m.b79 + 6*m.b64*m.b82 + 7*m.b64*m.b85 + 8*m.b64*m.b88 + 9*m.b64*m.b91 + 10*
                       m.b64*m.b94 + 11*m.b64*m.b97 + 12*m.b64*m.b100 + 13*m.b64*m.b103 + 14*m.b64*m.b106 + 15*m.b64*
                       m.b109 + 16*m.b64*m.b112 + 17*m.b64*m.b115 + 18*m.b64*m.b118 + 19*m.b64*m.b121 + 20*m.b64*m.b124
                        + 21*m.b64*m.b127 + 22*m.b64*m.b130 + 23*m.b64*m.b133 + 24*m.b64*m.b136 + 25*m.b64*m.b139 + 26*
                       m.b64*m.b142 + 27*m.b64*m.b145 + 28*m.b64*m.b148 + 29*m.b64*m.b151 + 30*m.b64*m.b154 + 31*m.b64*
                       m.b157 + 32*m.b64*m.b160 + 33*m.b64*m.b163 + 34*m.b64*m.b166 + 35*m.b64*m.b169 + 36*m.b64*m.b172
                        + 37*m.b64*m.b175 + 38*m.b64*m.b178 + 39*m.b64*m.b181 + 40*m.b64*m.b184 + 41*m.b64*m.b187 + 42*
                       m.b64*m.b190 + 43*m.b64*m.b193 + 44*m.b64*m.b196 + 45*m.b64*m.b199 + 46*m.b64*m.b202 + 47*m.b64*
                       m.b205 + 48*m.b64*m.b208 + m.b65*m.b68 + 2*m.b65*m.b71 + 3*m.b65*m.b74 + 4*m.b65*m.b77 + 5*m.b65*
                       m.b80 + 6*m.b65*m.b83 + 7*m.b65*m.b86 + 8*m.b65*m.b89 + 9*m.b65*m.b92 + 10*m.b65*m.b95 + 11*m.b65
                       *m.b98 + 12*m.b65*m.b101 + 13*m.b65*m.b104 + 14*m.b65*m.b107 + 15*m.b65*m.b110 + 16*m.b65*m.b113
                        + 17*m.b65*m.b116 + 18*m.b65*m.b119 + 19*m.b65*m.b122 + 20*m.b65*m.b125 + 21*m.b65*m.b128 + 22*
                       m.b65*m.b131 + 23*m.b65*m.b134 + 24*m.b65*m.b137 + 25*m.b65*m.b140 + 26*m.b65*m.b143 + 27*m.b65*
                       m.b146 + 28*m.b65*m.b149 + 29*m.b65*m.b152 + 30*m.b65*m.b155 + 31*m.b65*m.b158 + 32*m.b65*m.b161
                        + 33*m.b65*m.b164 + 34*m.b65*m.b167 + 35*m.b65*m.b170 + 36*m.b65*m.b173 + 37*m.b65*m.b176 + 38*
                       m.b65*m.b179 + 39*m.b65*m.b182 + 40*m.b65*m.b185 + 41*m.b65*m.b188 + 42*m.b65*m.b191 + 43*m.b65*
                       m.b194 + 44*m.b65*m.b197 + 45*m.b65*m.b200 + 46*m.b65*m.b203 + 47*m.b65*m.b206 + 48*m.b65*m.b209
                        + m.b66*m.b69 + 2*m.b66*m.b72 + 3*m.b66*m.b75 + 4*m.b66*m.b78 + 5*m.b66*m.b81 + 6*m.b66*m.b84 + 
                       7*m.b66*m.b87 + 8*m.b66*m.b90 + 9*m.b66*m.b93 + 10*m.b66*m.b96 + 11*m.b66*m.b99 + 12*m.b66*m.b102
                        + 13*m.b66*m.b105 + 14*m.b66*m.b108 + 15*m.b66*m.b111 + 16*m.b66*m.b114 + 17*m.b66*m.b117 + 18*
                       m.b66*m.b120 + 19*m.b66*m.b123 + 20*m.b66*m.b126 + 21*m.b66*m.b129 + 22*m.b66*m.b132 + 23*m.b66*
                       m.b135 + 24*m.b66*m.b138 + 25*m.b66*m.b141 + 26*m.b66*m.b144 + 27*m.b66*m.b147 + 28*m.b66*m.b150
                        + 29*m.b66*m.b153 + 30*m.b66*m.b156 + 31*m.b66*m.b159 + 32*m.b66*m.b162 + 33*m.b66*m.b165 + 34*
                       m.b66*m.b168 + 35*m.b66*m.b171 + 36*m.b66*m.b174 + 37*m.b66*m.b177 + 38*m.b66*m.b180 + 39*m.b66*
                       m.b183 + 40*m.b66*m.b186 + 41*m.b66*m.b189 + 42*m.b66*m.b192 + 43*m.b66*m.b195 + 44*m.b66*m.b198
                        + 45*m.b66*m.b201 + 46*m.b66*m.b204 + 47*m.b66*m.b207 + 48*m.b66*m.b210 + m.b67*m.b70 + 2*m.b67*
                       m.b73 + 3*m.b67*m.b76 + 4*m.b67*m.b79 + 5*m.b67*m.b82 + 6*m.b67*m.b85 + 7*m.b67*m.b88 + 8*m.b67*
                       m.b91 + 9*m.b67*m.b94 + 10*m.b67*m.b97 + 11*m.b67*m.b100 + 12*m.b67*m.b103 + 13*m.b67*m.b106 + 14
                       *m.b67*m.b109 + 15*m.b67*m.b112 + 16*m.b67*m.b115 + 17*m.b67*m.b118 + 18*m.b67*m.b121 + 19*m.b67*
                       m.b124 + 20*m.b67*m.b127 + 21*m.b67*m.b130 + 22*m.b67*m.b133 + 23*m.b67*m.b136 + 24*m.b67*m.b139
                        + 25*m.b67*m.b142 + 26*m.b67*m.b145 + 27*m.b67*m.b148 + 28*m.b67*m.b151 + 29*m.b67*m.b154 + 30*
                       m.b67*m.b157 + 31*m.b67*m.b160 + 32*m.b67*m.b163 + 33*m.b67*m.b166 + 34*m.b67*m.b169 + 35*m.b67*
                       m.b172 + 36*m.b67*m.b175 + 37*m.b67*m.b178 + 38*m.b67*m.b181 + 39*m.b67*m.b184 + 40*m.b67*m.b187
                        + 41*m.b67*m.b190 + 42*m.b67*m.b193 + 43*m.b67*m.b196 + 44*m.b67*m.b199 + 45*m.b67*m.b202 + 46*
                       m.b67*m.b205 + 47*m.b67*m.b208 + m.b68*m.b71 + 2*m.b68*m.b74 + 3*m.b68*m.b77 + 4*m.b68*m.b80 + 5*
                       m.b68*m.b83 + 6*m.b68*m.b86 + 7*m.b68*m.b89 + 8*m.b68*m.b92 + 9*m.b68*m.b95 + 10*m.b68*m.b98 + 11
                       *m.b68*m.b101 + 12*m.b68*m.b104 + 13*m.b68*m.b107 + 14*m.b68*m.b110 + 15*m.b68*m.b113 + 16*m.b68*
                       m.b116 + 17*m.b68*m.b119 + 18*m.b68*m.b122 + 19*m.b68*m.b125 + 20*m.b68*m.b128 + 21*m.b68*m.b131
                        + 22*m.b68*m.b134 + 23*m.b68*m.b137 + 24*m.b68*m.b140 + 25*m.b68*m.b143 + 26*m.b68*m.b146 + 27*
                       m.b68*m.b149 + 28*m.b68*m.b152 + 29*m.b68*m.b155 + 30*m.b68*m.b158 + 31*m.b68*m.b161 + 32*m.b68*
                       m.b164 + 33*m.b68*m.b167 + 34*m.b68*m.b170 + 35*m.b68*m.b173 + 36*m.b68*m.b176 + 37*m.b68*m.b179
                        + 38*m.b68*m.b182 + 39*m.b68*m.b185 + 40*m.b68*m.b188 + 41*m.b68*m.b191 + 42*m.b68*m.b194 + 43*
                       m.b68*m.b197 + 44*m.b68*m.b200 + 45*m.b68*m.b203 + 46*m.b68*m.b206 + 47*m.b68*m.b209 + m.b69*
                       m.b72 + 2*m.b69*m.b75 + 3*m.b69*m.b78 + 4*m.b69*m.b81 + 5*m.b69*m.b84 + 6*m.b69*m.b87 + 7*m.b69*
                       m.b90 + 8*m.b69*m.b93 + 9*m.b69*m.b96 + 10*m.b69*m.b99 + 11*m.b69*m.b102 + 12*m.b69*m.b105 + 13*
                       m.b69*m.b108 + 14*m.b69*m.b111 + 15*m.b69*m.b114 + 16*m.b69*m.b117 + 17*m.b69*m.b120 + 18*m.b69*
                       m.b123 + 19*m.b69*m.b126 + 20*m.b69*m.b129 + 21*m.b69*m.b132 + 22*m.b69*m.b135 + 23*m.b69*m.b138
                        + 24*m.b69*m.b141 + 25*m.b69*m.b144 + 26*m.b69*m.b147 + 27*m.b69*m.b150 + 28*m.b69*m.b153 + 29*
                       m.b69*m.b156 + 30*m.b69*m.b159 + 31*m.b69*m.b162 + 32*m.b69*m.b165 + 33*m.b69*m.b168 + 34*m.b69*
                       m.b171 + 35*m.b69*m.b174 + 36*m.b69*m.b177 + 37*m.b69*m.b180 + 38*m.b69*m.b183 + 39*m.b69*m.b186
                        + 40*m.b69*m.b189 + 41*m.b69*m.b192 + 42*m.b69*m.b195 + 43*m.b69*m.b198 + 44*m.b69*m.b201 + 45*
                       m.b69*m.b204 + 46*m.b69*m.b207 + 47*m.b69*m.b210 + m.b70*m.b73 + 2*m.b70*m.b76 + 3*m.b70*m.b79 + 
                       4*m.b70*m.b82 + 5*m.b70*m.b85 + 6*m.b70*m.b88 + 7*m.b70*m.b91 + 8*m.b70*m.b94 + 9*m.b70*m.b97 + 
                       10*m.b70*m.b100 + 11*m.b70*m.b103 + 12*m.b70*m.b106 + 13*m.b70*m.b109 + 14*m.b70*m.b112 + 15*
                       m.b70*m.b115 + 16*m.b70*m.b118 + 17*m.b70*m.b121 + 18*m.b70*m.b124 + 19*m.b70*m.b127 + 20*m.b70*
                       m.b130 + 21*m.b70*m.b133 + 22*m.b70*m.b136 + 23*m.b70*m.b139 + 24*m.b70*m.b142 + 25*m.b70*m.b145
                        + 26*m.b70*m.b148 + 27*m.b70*m.b151 + 28*m.b70*m.b154 + 29*m.b70*m.b157 + 30*m.b70*m.b160 + 31*
                       m.b70*m.b163 + 32*m.b70*m.b166 + 33*m.b70*m.b169 + 34*m.b70*m.b172 + 35*m.b70*m.b175 + 36*m.b70*
                       m.b178 + 37*m.b70*m.b181 + 38*m.b70*m.b184 + 39*m.b70*m.b187 + 40*m.b70*m.b190 + 41*m.b70*m.b193
                        + 42*m.b70*m.b196 + 43*m.b70*m.b199 + 44*m.b70*m.b202 + 45*m.b70*m.b205 + 46*m.b70*m.b208 + 
                       m.b71*m.b74 + 2*m.b71*m.b77 + 3*m.b71*m.b80 + 4*m.b71*m.b83 + 5*m.b71*m.b86 + 6*m.b71*m.b89 + 7*
                       m.b71*m.b92 + 8*m.b71*m.b95 + 9*m.b71*m.b98 + 10*m.b71*m.b101 + 11*m.b71*m.b104 + 12*m.b71*m.b107
                        + 13*m.b71*m.b110 + 14*m.b71*m.b113 + 15*m.b71*m.b116 + 16*m.b71*m.b119 + 17*m.b71*m.b122 + 18*
                       m.b71*m.b125 + 19*m.b71*m.b128 + 20*m.b71*m.b131 + 21*m.b71*m.b134 + 22*m.b71*m.b137 + 23*m.b71*
                       m.b140 + 24*m.b71*m.b143 + 25*m.b71*m.b146 + 26*m.b71*m.b149 + 27*m.b71*m.b152 + 28*m.b71*m.b155
                        + 29*m.b71*m.b158 + 30*m.b71*m.b161 + 31*m.b71*m.b164 + 32*m.b71*m.b167 + 33*m.b71*m.b170 + 34*
                       m.b71*m.b173 + 35*m.b71*m.b176 + 36*m.b71*m.b179 + 37*m.b71*m.b182 + 38*m.b71*m.b185 + 39*m.b71*
                       m.b188 + 40*m.b71*m.b191 + 41*m.b71*m.b194 + 42*m.b71*m.b197 + 43*m.b71*m.b200 + 44*m.b71*m.b203
                        + 45*m.b71*m.b206 + 46*m.b71*m.b209 + m.b72*m.b75 + 2*m.b72*m.b78 + 3*m.b72*m.b81 + 4*m.b72*
                       m.b84 + 5*m.b72*m.b87 + 6*m.b72*m.b90 + 7*m.b72*m.b93 + 8*m.b72*m.b96 + 9*m.b72*m.b99 + 10*m.b72*
                       m.b102 + 11*m.b72*m.b105 + 12*m.b72*m.b108 + 13*m.b72*m.b111 + 14*m.b72*m.b114 + 15*m.b72*m.b117
                        + 16*m.b72*m.b120 + 17*m.b72*m.b123 + 18*m.b72*m.b126 + 19*m.b72*m.b129 + 20*m.b72*m.b132 + 21*
                       m.b72*m.b135 + 22*m.b72*m.b138 + 23*m.b72*m.b141 + 24*m.b72*m.b144 + 25*m.b72*m.b147 + 26*m.b72*
                       m.b150 + 27*m.b72*m.b153 + 28*m.b72*m.b156 + 29*m.b72*m.b159 + 30*m.b72*m.b162 + 31*m.b72*m.b165
                        + 32*m.b72*m.b168 + 33*m.b72*m.b171 + 34*m.b72*m.b174 + 35*m.b72*m.b177 + 36*m.b72*m.b180 + 37*
                       m.b72*m.b183 + 38*m.b72*m.b186 + 39*m.b72*m.b189 + 40*m.b72*m.b192 + 41*m.b72*m.b195 + 42*m.b72*
                       m.b198 + 43*m.b72*m.b201 + 44*m.b72*m.b204 + 45*m.b72*m.b207 + 46*m.b72*m.b210 + m.b73*m.b76 + 2*
                       m.b73*m.b79 + 3*m.b73*m.b82 + 4*m.b73*m.b85 + 5*m.b73*m.b88 + 6*m.b73*m.b91 + 7*m.b73*m.b94 + 8*
                       m.b73*m.b97 + 9*m.b73*m.b100 + 10*m.b73*m.b103 + 11*m.b73*m.b106 + 12*m.b73*m.b109 + 13*m.b73*
                       m.b112 + 14*m.b73*m.b115 + 15*m.b73*m.b118 + 16*m.b73*m.b121 + 17*m.b73*m.b124 + 18*m.b73*m.b127
                        + 19*m.b73*m.b130 + 20*m.b73*m.b133 + 21*m.b73*m.b136 + 22*m.b73*m.b139 + 23*m.b73*m.b142 + 24*
                       m.b73*m.b145 + 25*m.b73*m.b148 + 26*m.b73*m.b151 + 27*m.b73*m.b154 + 28*m.b73*m.b157 + 29*m.b73*
                       m.b160 + 30*m.b73*m.b163 + 31*m.b73*m.b166 + 32*m.b73*m.b169 + 33*m.b73*m.b172 + 34*m.b73*m.b175
                        + 35*m.b73*m.b178 + 36*m.b73*m.b181 + 37*m.b73*m.b184 + 38*m.b73*m.b187 + 39*m.b73*m.b190 + 40*
                       m.b73*m.b193 + 41*m.b73*m.b196 + 42*m.b73*m.b199 + 43*m.b73*m.b202 + 44*m.b73*m.b205 + 45*m.b73*
                       m.b208 + m.b74*m.b77 + 2*m.b74*m.b80 + 3*m.b74*m.b83 + 4*m.b74*m.b86 + 5*m.b74*m.b89 + 6*m.b74*
                       m.b92 + 7*m.b74*m.b95 + 8*m.b74*m.b98 + 9*m.b74*m.b101 + 10*m.b74*m.b104 + 11*m.b74*m.b107 + 12*
                       m.b74*m.b110 + 13*m.b74*m.b113 + 14*m.b74*m.b116 + 15*m.b74*m.b119 + 16*m.b74*m.b122 + 17*m.b74*
                       m.b125 + 18*m.b74*m.b128 + 19*m.b74*m.b131 + 20*m.b74*m.b134 + 21*m.b74*m.b137 + 22*m.b74*m.b140
                        + 23*m.b74*m.b143 + 24*m.b74*m.b146 + 25*m.b74*m.b149 + 26*m.b74*m.b152 + 27*m.b74*m.b155 + 28*
                       m.b74*m.b158 + 29*m.b74*m.b161 + 30*m.b74*m.b164 + 31*m.b74*m.b167 + 32*m.b74*m.b170 + 33*m.b74*
                       m.b173 + 34*m.b74*m.b176 + 35*m.b74*m.b179 + 36*m.b74*m.b182 + 37*m.b74*m.b185 + 38*m.b74*m.b188
                        + 39*m.b74*m.b191 + 40*m.b74*m.b194 + 41*m.b74*m.b197 + 42*m.b74*m.b200 + 43*m.b74*m.b203 + 44*
                       m.b74*m.b206 + 45*m.b74*m.b209 + m.b75*m.b78 + 2*m.b75*m.b81 + 3*m.b75*m.b84 + 4*m.b75*m.b87 + 5*
                       m.b75*m.b90 + 6*m.b75*m.b93 + 7*m.b75*m.b96 + 8*m.b75*m.b99 + 9*m.b75*m.b102 + 10*m.b75*m.b105 + 
                       11*m.b75*m.b108 + 12*m.b75*m.b111 + 13*m.b75*m.b114 + 14*m.b75*m.b117 + 15*m.b75*m.b120 + 16*
                       m.b75*m.b123 + 17*m.b75*m.b126 + 18*m.b75*m.b129 + 19*m.b75*m.b132 + 20*m.b75*m.b135 + 21*m.b75*
                       m.b138 + 22*m.b75*m.b141 + 23*m.b75*m.b144 + 24*m.b75*m.b147 + 25*m.b75*m.b150 + 26*m.b75*m.b153
                        + 27*m.b75*m.b156 + 28*m.b75*m.b159 + 29*m.b75*m.b162 + 30*m.b75*m.b165 + 31*m.b75*m.b168 + 32*
                       m.b75*m.b171 + 33*m.b75*m.b174 + 34*m.b75*m.b177 + 35*m.b75*m.b180 + 36*m.b75*m.b183 + 37*m.b75*
                       m.b186 + 38*m.b75*m.b189 + 39*m.b75*m.b192 + 40*m.b75*m.b195 + 41*m.b75*m.b198 + 42*m.b75*m.b201
                        + 43*m.b75*m.b204 + 44*m.b75*m.b207 + 45*m.b75*m.b210 + m.b76*m.b79 + 2*m.b76*m.b82 + 3*m.b76*
                       m.b85 + 4*m.b76*m.b88 + 5*m.b76*m.b91 + 6*m.b76*m.b94 + 7*m.b76*m.b97 + 8*m.b76*m.b100 + 9*m.b76*
                       m.b103 + 10*m.b76*m.b106 + 11*m.b76*m.b109 + 12*m.b76*m.b112 + 13*m.b76*m.b115 + 14*m.b76*m.b118
                        + 15*m.b76*m.b121 + 16*m.b76*m.b124 + 17*m.b76*m.b127 + 18*m.b76*m.b130 + 19*m.b76*m.b133 + 20*
                       m.b76*m.b136 + 21*m.b76*m.b139 + 22*m.b76*m.b142 + 23*m.b76*m.b145 + 24*m.b76*m.b148 + 25*m.b76*
                       m.b151 + 26*m.b76*m.b154 + 27*m.b76*m.b157 + 28*m.b76*m.b160 + 29*m.b76*m.b163 + 30*m.b76*m.b166
                        + 31*m.b76*m.b169 + 32*m.b76*m.b172 + 33*m.b76*m.b175 + 34*m.b76*m.b178 + 35*m.b76*m.b181 + 36*
                       m.b76*m.b184 + 37*m.b76*m.b187 + 38*m.b76*m.b190 + 39*m.b76*m.b193 + 40*m.b76*m.b196 + 41*m.b76*
                       m.b199 + 42*m.b76*m.b202 + 43*m.b76*m.b205 + 44*m.b76*m.b208 + m.b77*m.b80 + 2*m.b77*m.b83 + 3*
                       m.b77*m.b86 + 4*m.b77*m.b89 + 5*m.b77*m.b92 + 6*m.b77*m.b95 + 7*m.b77*m.b98 + 8*m.b77*m.b101 + 9*
                       m.b77*m.b104 + 10*m.b77*m.b107 + 11*m.b77*m.b110 + 12*m.b77*m.b113 + 13*m.b77*m.b116 + 14*m.b77*
                       m.b119 + 15*m.b77*m.b122 + 16*m.b77*m.b125 + 17*m.b77*m.b128 + 18*m.b77*m.b131 + 19*m.b77*m.b134
                        + 20*m.b77*m.b137 + 21*m.b77*m.b140 + 22*m.b77*m.b143 + 23*m.b77*m.b146 + 24*m.b77*m.b149 + 25*
                       m.b77*m.b152 + 26*m.b77*m.b155 + 27*m.b77*m.b158 + 28*m.b77*m.b161 + 29*m.b77*m.b164 + 30*m.b77*
                       m.b167 + 31*m.b77*m.b170 + 32*m.b77*m.b173 + 33*m.b77*m.b176 + 34*m.b77*m.b179 + 35*m.b77*m.b182
                        + 36*m.b77*m.b185 + 37*m.b77*m.b188 + 38*m.b77*m.b191 + 39*m.b77*m.b194 + 40*m.b77*m.b197 + 41*
                       m.b77*m.b200 + 42*m.b77*m.b203 + 43*m.b77*m.b206 + 44*m.b77*m.b209 + m.b78*m.b81 + 2*m.b78*m.b84
                        + 3*m.b78*m.b87 + 4*m.b78*m.b90 + 5*m.b78*m.b93 + 6*m.b78*m.b96 + 7*m.b78*m.b99 + 8*m.b78*m.b102
                        + 9*m.b78*m.b105 + 10*m.b78*m.b108 + 11*m.b78*m.b111 + 12*m.b78*m.b114 + 13*m.b78*m.b117 + 14*
                       m.b78*m.b120 + 15*m.b78*m.b123 + 16*m.b78*m.b126 + 17*m.b78*m.b129 + 18*m.b78*m.b132 + 19*m.b78*
                       m.b135 + 20*m.b78*m.b138 + 21*m.b78*m.b141 + 22*m.b78*m.b144 + 23*m.b78*m.b147 + 24*m.b78*m.b150
                        + 25*m.b78*m.b153 + 26*m.b78*m.b156 + 27*m.b78*m.b159 + 28*m.b78*m.b162 + 29*m.b78*m.b165 + 30*
                       m.b78*m.b168 + 31*m.b78*m.b171 + 32*m.b78*m.b174 + 33*m.b78*m.b177 + 34*m.b78*m.b180 + 35*m.b78*
                       m.b183 + 36*m.b78*m.b186 + 37*m.b78*m.b189 + 38*m.b78*m.b192 + 39*m.b78*m.b195 + 40*m.b78*m.b198
                        + 41*m.b78*m.b201 + 42*m.b78*m.b204 + 43*m.b78*m.b207 + 44*m.b78*m.b210 + m.b79*m.b82 + 2*m.b79*
                       m.b85 + 3*m.b79*m.b88 + 4*m.b79*m.b91 + 5*m.b79*m.b94 + 6*m.b79*m.b97 + 7*m.b79*m.b100 + 8*m.b79*
                       m.b103 + 9*m.b79*m.b106 + 10*m.b79*m.b109 + 11*m.b79*m.b112 + 12*m.b79*m.b115 + 13*m.b79*m.b118
                        + 14*m.b79*m.b121 + 15*m.b79*m.b124 + 16*m.b79*m.b127 + 17*m.b79*m.b130 + 18*m.b79*m.b133 + 19*
                       m.b79*m.b136 + 20*m.b79*m.b139 + 21*m.b79*m.b142 + 22*m.b79*m.b145 + 23*m.b79*m.b148 + 24*m.b79*
                       m.b151 + 25*m.b79*m.b154 + 26*m.b79*m.b157 + 27*m.b79*m.b160 + 28*m.b79*m.b163 + 29*m.b79*m.b166
                        + 30*m.b79*m.b169 + 31*m.b79*m.b172 + 32*m.b79*m.b175 + 33*m.b79*m.b178 + 34*m.b79*m.b181 + 35*
                       m.b79*m.b184 + 36*m.b79*m.b187 + 37*m.b79*m.b190 + 38*m.b79*m.b193 + 39*m.b79*m.b196 + 40*m.b79*
                       m.b199 + 41*m.b79*m.b202 + 42*m.b79*m.b205 + 43*m.b79*m.b208 + m.b80*m.b83 + 2*m.b80*m.b86 + 3*
                       m.b80*m.b89 + 4*m.b80*m.b92 + 5*m.b80*m.b95 + 6*m.b80*m.b98 + 7*m.b80*m.b101 + 8*m.b80*m.b104 + 9
                       *m.b80*m.b107 + 10*m.b80*m.b110 + 11*m.b80*m.b113 + 12*m.b80*m.b116 + 13*m.b80*m.b119 + 14*m.b80*
                       m.b122 + 15*m.b80*m.b125 + 16*m.b80*m.b128 + 17*m.b80*m.b131 + 18*m.b80*m.b134 + 19*m.b80*m.b137
                        + 20*m.b80*m.b140 + 21*m.b80*m.b143 + 22*m.b80*m.b146 + 23*m.b80*m.b149 + 24*m.b80*m.b152 + 25*
                       m.b80*m.b155 + 26*m.b80*m.b158 + 27*m.b80*m.b161 + 28*m.b80*m.b164 + 29*m.b80*m.b167 + 30*m.b80*
                       m.b170 + 31*m.b80*m.b173 + 32*m.b80*m.b176 + 33*m.b80*m.b179 + 34*m.b80*m.b182 + 35*m.b80*m.b185
                        + 36*m.b80*m.b188 + 37*m.b80*m.b191 + 38*m.b80*m.b194 + 39*m.b80*m.b197 + 40*m.b80*m.b200 + 41*
                       m.b80*m.b203 + 42*m.b80*m.b206 + 43*m.b80*m.b209 + m.b81*m.b84 + 2*m.b81*m.b87 + 3*m.b81*m.b90 + 
                       4*m.b81*m.b93 + 5*m.b81*m.b96 + 6*m.b81*m.b99 + 7*m.b81*m.b102 + 8*m.b81*m.b105 + 9*m.b81*m.b108
                        + 10*m.b81*m.b111 + 11*m.b81*m.b114 + 12*m.b81*m.b117 + 13*m.b81*m.b120 + 14*m.b81*m.b123 + 15*
                       m.b81*m.b126 + 16*m.b81*m.b129 + 17*m.b81*m.b132 + 18*m.b81*m.b135 + 19*m.b81*m.b138 + 20*m.b81*
                       m.b141 + 21*m.b81*m.b144 + 22*m.b81*m.b147 + 23*m.b81*m.b150 + 24*m.b81*m.b153 + 25*m.b81*m.b156
                        + 26*m.b81*m.b159 + 27*m.b81*m.b162 + 28*m.b81*m.b165 + 29*m.b81*m.b168 + 30*m.b81*m.b171 + 31*
                       m.b81*m.b174 + 32*m.b81*m.b177 + 33*m.b81*m.b180 + 34*m.b81*m.b183 + 35*m.b81*m.b186 + 36*m.b81*
                       m.b189 + 37*m.b81*m.b192 + 38*m.b81*m.b195 + 39*m.b81*m.b198 + 40*m.b81*m.b201 + 41*m.b81*m.b204
                        + 42*m.b81*m.b207 + 43*m.b81*m.b210 + m.b82*m.b85 + 2*m.b82*m.b88 + 3*m.b82*m.b91 + 4*m.b82*
                       m.b94 + 5*m.b82*m.b97 + 6*m.b82*m.b100 + 7*m.b82*m.b103 + 8*m.b82*m.b106 + 9*m.b82*m.b109 + 10*
                       m.b82*m.b112 + 11*m.b82*m.b115 + 12*m.b82*m.b118 + 13*m.b82*m.b121 + 14*m.b82*m.b124 + 15*m.b82*
                       m.b127 + 16*m.b82*m.b130 + 17*m.b82*m.b133 + 18*m.b82*m.b136 + 19*m.b82*m.b139 + 20*m.b82*m.b142
                        + 21*m.b82*m.b145 + 22*m.b82*m.b148 + 23*m.b82*m.b151 + 24*m.b82*m.b154 + 25*m.b82*m.b157 + 26*
                       m.b82*m.b160 + 27*m.b82*m.b163 + 28*m.b82*m.b166 + 29*m.b82*m.b169 + 30*m.b82*m.b172 + 31*m.b82*
                       m.b175 + 32*m.b82*m.b178 + 33*m.b82*m.b181 + 34*m.b82*m.b184 + 35*m.b82*m.b187 + 36*m.b82*m.b190
                        + 37*m.b82*m.b193 + 38*m.b82*m.b196 + 39*m.b82*m.b199 + 40*m.b82*m.b202 + 41*m.b82*m.b205 + 42*
                       m.b82*m.b208 + m.b83*m.b86 + 2*m.b83*m.b89 + 3*m.b83*m.b92 + 4*m.b83*m.b95 + 5*m.b83*m.b98 + 6*
                       m.b83*m.b101 + 7*m.b83*m.b104 + 8*m.b83*m.b107 + 9*m.b83*m.b110 + 10*m.b83*m.b113 + 11*m.b83*
                       m.b116 + 12*m.b83*m.b119 + 13*m.b83*m.b122 + 14*m.b83*m.b125 + 15*m.b83*m.b128 + 16*m.b83*m.b131
                        + 17*m.b83*m.b134 + 18*m.b83*m.b137 + 19*m.b83*m.b140 + 20*m.b83*m.b143 + 21*m.b83*m.b146 + 22*
                       m.b83*m.b149 + 23*m.b83*m.b152 + 24*m.b83*m.b155 + 25*m.b83*m.b158 + 26*m.b83*m.b161 + 27*m.b83*
                       m.b164 + 28*m.b83*m.b167 + 29*m.b83*m.b170 + 30*m.b83*m.b173 + 31*m.b83*m.b176 + 32*m.b83*m.b179
                        + 33*m.b83*m.b182 + 34*m.b83*m.b185 + 35*m.b83*m.b188 + 36*m.b83*m.b191 + 37*m.b83*m.b194 + 38*
                       m.b83*m.b197 + 39*m.b83*m.b200 + 40*m.b83*m.b203 + 41*m.b83*m.b206 + 42*m.b83*m.b209 + m.b84*
                       m.b87 + 2*m.b84*m.b90 + 3*m.b84*m.b93 + 4*m.b84*m.b96 + 5*m.b84*m.b99 + 6*m.b84*m.b102 + 7*m.b84*
                       m.b105 + 8*m.b84*m.b108 + 9*m.b84*m.b111 + 10*m.b84*m.b114 + 11*m.b84*m.b117 + 12*m.b84*m.b120 + 
                       13*m.b84*m.b123 + 14*m.b84*m.b126 + 15*m.b84*m.b129 + 16*m.b84*m.b132 + 17*m.b84*m.b135 + 18*
                       m.b84*m.b138 + 19*m.b84*m.b141 + 20*m.b84*m.b144 + 21*m.b84*m.b147 + 22*m.b84*m.b150 + 23*m.b84*
                       m.b153 + 24*m.b84*m.b156 + 25*m.b84*m.b159 + 26*m.b84*m.b162 + 27*m.b84*m.b165 + 28*m.b84*m.b168
                        + 29*m.b84*m.b171 + 30*m.b84*m.b174 + 31*m.b84*m.b177 + 32*m.b84*m.b180 + 33*m.b84*m.b183 + 34*
                       m.b84*m.b186 + 35*m.b84*m.b189 + 36*m.b84*m.b192 + 37*m.b84*m.b195 + 38*m.b84*m.b198 + 39*m.b84*
                       m.b201 + 40*m.b84*m.b204 + 41*m.b84*m.b207 + 42*m.b84*m.b210 + m.b85*m.b88 + 2*m.b85*m.b91 + 3*
                       m.b85*m.b94 + 4*m.b85*m.b97 + 5*m.b85*m.b100 + 6*m.b85*m.b103 + 7*m.b85*m.b106 + 8*m.b85*m.b109
                        + 9*m.b85*m.b112 + 10*m.b85*m.b115 + 11*m.b85*m.b118 + 12*m.b85*m.b121 + 13*m.b85*m.b124 + 14*
                       m.b85*m.b127 + 15*m.b85*m.b130 + 16*m.b85*m.b133 + 17*m.b85*m.b136 + 18*m.b85*m.b139 + 19*m.b85*
                       m.b142 + 20*m.b85*m.b145 + 21*m.b85*m.b148 + 22*m.b85*m.b151 + 23*m.b85*m.b154 + 24*m.b85*m.b157
                        + 25*m.b85*m.b160 + 26*m.b85*m.b163 + 27*m.b85*m.b166 + 28*m.b85*m.b169 + 29*m.b85*m.b172 + 30*
                       m.b85*m.b175 + 31*m.b85*m.b178 + 32*m.b85*m.b181 + 33*m.b85*m.b184 + 34*m.b85*m.b187 + 35*m.b85*
                       m.b190 + 36*m.b85*m.b193 + 37*m.b85*m.b196 + 38*m.b85*m.b199 + 39*m.b85*m.b202 + 40*m.b85*m.b205
                        + 41*m.b85*m.b208 + m.b86*m.b89 + 2*m.b86*m.b92 + 3*m.b86*m.b95 + 4*m.b86*m.b98 + 5*m.b86*m.b101
                        + 6*m.b86*m.b104 + 7*m.b86*m.b107 + 8*m.b86*m.b110 + 9*m.b86*m.b113 + 10*m.b86*m.b116 + 11*m.b86
                       *m.b119 + 12*m.b86*m.b122 + 13*m.b86*m.b125 + 14*m.b86*m.b128 + 15*m.b86*m.b131 + 16*m.b86*m.b134
                        + 17*m.b86*m.b137 + 18*m.b86*m.b140 + 19*m.b86*m.b143 + 20*m.b86*m.b146 + 21*m.b86*m.b149 + 22*
                       m.b86*m.b152 + 23*m.b86*m.b155 + 24*m.b86*m.b158 + 25*m.b86*m.b161 + 26*m.b86*m.b164 + 27*m.b86*
                       m.b167 + 28*m.b86*m.b170 + 29*m.b86*m.b173 + 30*m.b86*m.b176 + 31*m.b86*m.b179 + 32*m.b86*m.b182
                        + 33*m.b86*m.b185 + 34*m.b86*m.b188 + 35*m.b86*m.b191 + 36*m.b86*m.b194 + 37*m.b86*m.b197 + 38*
                       m.b86*m.b200 + 39*m.b86*m.b203 + 40*m.b86*m.b206 + 41*m.b86*m.b209 + m.b87*m.b90 + 2*m.b87*m.b93
                        + 3*m.b87*m.b96 + 4*m.b87*m.b99 + 5*m.b87*m.b102 + 6*m.b87*m.b105 + 7*m.b87*m.b108 + 8*m.b87*
                       m.b111 + 9*m.b87*m.b114 + 10*m.b87*m.b117 + 11*m.b87*m.b120 + 12*m.b87*m.b123 + 13*m.b87*m.b126
                        + 14*m.b87*m.b129 + 15*m.b87*m.b132 + 16*m.b87*m.b135 + 17*m.b87*m.b138 + 18*m.b87*m.b141 + 19*
                       m.b87*m.b144 + 20*m.b87*m.b147 + 21*m.b87*m.b150 + 22*m.b87*m.b153 + 23*m.b87*m.b156 + 24*m.b87*
                       m.b159 + 25*m.b87*m.b162 + 26*m.b87*m.b165 + 27*m.b87*m.b168 + 28*m.b87*m.b171 + 29*m.b87*m.b174
                        + 30*m.b87*m.b177 + 31*m.b87*m.b180 + 32*m.b87*m.b183 + 33*m.b87*m.b186 + 34*m.b87*m.b189 + 35*
                       m.b87*m.b192 + 36*m.b87*m.b195 + 37*m.b87*m.b198 + 38*m.b87*m.b201 + 39*m.b87*m.b204 + 40*m.b87*
                       m.b207 + 41*m.b87*m.b210 + m.b88*m.b91 + 2*m.b88*m.b94 + 3*m.b88*m.b97 + 4*m.b88*m.b100 + 5*m.b88
                       *m.b103 + 6*m.b88*m.b106 + 7*m.b88*m.b109 + 8*m.b88*m.b112 + 9*m.b88*m.b115 + 10*m.b88*m.b118 + 
                       11*m.b88*m.b121 + 12*m.b88*m.b124 + 13*m.b88*m.b127 + 14*m.b88*m.b130 + 15*m.b88*m.b133 + 16*
                       m.b88*m.b136 + 17*m.b88*m.b139 + 18*m.b88*m.b142 + 19*m.b88*m.b145 + 20*m.b88*m.b148 + 21*m.b88*
                       m.b151 + 22*m.b88*m.b154 + 23*m.b88*m.b157 + 24*m.b88*m.b160 + 25*m.b88*m.b163 + 26*m.b88*m.b166
                        + 27*m.b88*m.b169 + 28*m.b88*m.b172 + 29*m.b88*m.b175 + 30*m.b88*m.b178 + 31*m.b88*m.b181 + 32*
                       m.b88*m.b184 + 33*m.b88*m.b187 + 34*m.b88*m.b190 + 35*m.b88*m.b193 + 36*m.b88*m.b196 + 37*m.b88*
                       m.b199 + 38*m.b88*m.b202 + 39*m.b88*m.b205 + 40*m.b88*m.b208 + m.b89*m.b92 + 2*m.b89*m.b95 + 3*
                       m.b89*m.b98 + 4*m.b89*m.b101 + 5*m.b89*m.b104 + 6*m.b89*m.b107 + 7*m.b89*m.b110 + 8*m.b89*m.b113
                        + 9*m.b89*m.b116 + 10*m.b89*m.b119 + 11*m.b89*m.b122 + 12*m.b89*m.b125 + 13*m.b89*m.b128 + 14*
                       m.b89*m.b131 + 15*m.b89*m.b134 + 16*m.b89*m.b137 + 17*m.b89*m.b140 + 18*m.b89*m.b143 + 19*m.b89*
                       m.b146 + 20*m.b89*m.b149 + 21*m.b89*m.b152 + 22*m.b89*m.b155 + 23*m.b89*m.b158 + 24*m.b89*m.b161
                        + 25*m.b89*m.b164 + 26*m.b89*m.b167 + 27*m.b89*m.b170 + 28*m.b89*m.b173 + 29*m.b89*m.b176 + 30*
                       m.b89*m.b179 + 31*m.b89*m.b182 + 32*m.b89*m.b185 + 33*m.b89*m.b188 + 34*m.b89*m.b191 + 35*m.b89*
                       m.b194 + 36*m.b89*m.b197 + 37*m.b89*m.b200 + 38*m.b89*m.b203 + 39*m.b89*m.b206 + 40*m.b89*m.b209
                        + m.b90*m.b93 + 2*m.b90*m.b96 + 3*m.b90*m.b99 + 4*m.b90*m.b102 + 5*m.b90*m.b105 + 6*m.b90*m.b108
                        + 7*m.b90*m.b111 + 8*m.b90*m.b114 + 9*m.b90*m.b117 + 10*m.b90*m.b120 + 11*m.b90*m.b123 + 12*
                       m.b90*m.b126 + 13*m.b90*m.b129 + 14*m.b90*m.b132 + 15*m.b90*m.b135 + 16*m.b90*m.b138 + 17*m.b90*
                       m.b141 + 18*m.b90*m.b144 + 19*m.b90*m.b147 + 20*m.b90*m.b150 + 21*m.b90*m.b153 + 22*m.b90*m.b156
                        + 23*m.b90*m.b159 + 24*m.b90*m.b162 + 25*m.b90*m.b165 + 26*m.b90*m.b168 + 27*m.b90*m.b171 + 28*
                       m.b90*m.b174 + 29*m.b90*m.b177 + 30*m.b90*m.b180 + 31*m.b90*m.b183 + 32*m.b90*m.b186 + 33*m.b90*
                       m.b189 + 34*m.b90*m.b192 + 35*m.b90*m.b195 + 36*m.b90*m.b198 + 37*m.b90*m.b201 + 38*m.b90*m.b204
                        + 39*m.b90*m.b207 + 40*m.b90*m.b210 + m.b91*m.b94 + 2*m.b91*m.b97 + 3*m.b91*m.b100 + 4*m.b91*
                       m.b103 + 5*m.b91*m.b106 + 6*m.b91*m.b109 + 7*m.b91*m.b112 + 8*m.b91*m.b115 + 9*m.b91*m.b118 + 10*
                       m.b91*m.b121 + 11*m.b91*m.b124 + 12*m.b91*m.b127 + 13*m.b91*m.b130 + 14*m.b91*m.b133 + 15*m.b91*
                       m.b136 + 16*m.b91*m.b139 + 17*m.b91*m.b142 + 18*m.b91*m.b145 + 19*m.b91*m.b148 + 20*m.b91*m.b151
                        + 21*m.b91*m.b154 + 22*m.b91*m.b157 + 23*m.b91*m.b160 + 24*m.b91*m.b163 + 25*m.b91*m.b166 + 26*
                       m.b91*m.b169 + 27*m.b91*m.b172 + 28*m.b91*m.b175 + 29*m.b91*m.b178 + 30*m.b91*m.b181 + 31*m.b91*
                       m.b184 + 32*m.b91*m.b187 + 33*m.b91*m.b190 + 34*m.b91*m.b193 + 35*m.b91*m.b196 + 36*m.b91*m.b199
                        + 37*m.b91*m.b202 + 38*m.b91*m.b205 + 39*m.b91*m.b208 + m.b92*m.b95 + 2*m.b92*m.b98 + 3*m.b92*
                       m.b101 + 4*m.b92*m.b104 + 5*m.b92*m.b107 + 6*m.b92*m.b110 + 7*m.b92*m.b113 + 8*m.b92*m.b116 + 9*
                       m.b92*m.b119 + 10*m.b92*m.b122 + 11*m.b92*m.b125 + 12*m.b92*m.b128 + 13*m.b92*m.b131 + 14*m.b92*
                       m.b134 + 15*m.b92*m.b137 + 16*m.b92*m.b140 + 17*m.b92*m.b143 + 18*m.b92*m.b146 + 19*m.b92*m.b149
                        + 20*m.b92*m.b152 + 21*m.b92*m.b155 + 22*m.b92*m.b158 + 23*m.b92*m.b161 + 24*m.b92*m.b164 + 25*
                       m.b92*m.b167 + 26*m.b92*m.b170 + 27*m.b92*m.b173 + 28*m.b92*m.b176 + 29*m.b92*m.b179 + 30*m.b92*
                       m.b182 + 31*m.b92*m.b185 + 32*m.b92*m.b188 + 33*m.b92*m.b191 + 34*m.b92*m.b194 + 35*m.b92*m.b197
                        + 36*m.b92*m.b200 + 37*m.b92*m.b203 + 38*m.b92*m.b206 + 39*m.b92*m.b209 + m.b93*m.b96 + 2*m.b93*
                       m.b99 + 3*m.b93*m.b102 + 4*m.b93*m.b105 + 5*m.b93*m.b108 + 6*m.b93*m.b111 + 7*m.b93*m.b114 + 8*
                       m.b93*m.b117 + 9*m.b93*m.b120 + 10*m.b93*m.b123 + 11*m.b93*m.b126 + 12*m.b93*m.b129 + 13*m.b93*
                       m.b132 + 14*m.b93*m.b135 + 15*m.b93*m.b138 + 16*m.b93*m.b141 + 17*m.b93*m.b144 + 18*m.b93*m.b147
                        + 19*m.b93*m.b150 + 20*m.b93*m.b153 + 21*m.b93*m.b156 + 22*m.b93*m.b159 + 23*m.b93*m.b162 + 24*
                       m.b93*m.b165 + 25*m.b93*m.b168 + 26*m.b93*m.b171 + 27*m.b93*m.b174 + 28*m.b93*m.b177 + 29*m.b93*
                       m.b180 + 30*m.b93*m.b183 + 31*m.b93*m.b186 + 32*m.b93*m.b189 + 33*m.b93*m.b192 + 34*m.b93*m.b195
                        + 35*m.b93*m.b198 + 36*m.b93*m.b201 + 37*m.b93*m.b204 + 38*m.b93*m.b207 + 39*m.b93*m.b210 + 
                       m.b94*m.b97 + 2*m.b94*m.b100 + 3*m.b94*m.b103 + 4*m.b94*m.b106 + 5*m.b94*m.b109 + 6*m.b94*m.b112
                        + 7*m.b94*m.b115 + 8*m.b94*m.b118 + 9*m.b94*m.b121 + 10*m.b94*m.b124 + 11*m.b94*m.b127 + 12*
                       m.b94*m.b130 + 13*m.b94*m.b133 + 14*m.b94*m.b136 + 15*m.b94*m.b139 + 16*m.b94*m.b142 + 17*m.b94*
                       m.b145 + 18*m.b94*m.b148 + 19*m.b94*m.b151 + 20*m.b94*m.b154 + 21*m.b94*m.b157 + 22*m.b94*m.b160
                        + 23*m.b94*m.b163 + 24*m.b94*m.b166 + 25*m.b94*m.b169 + 26*m.b94*m.b172 + 27*m.b94*m.b175 + 28*
                       m.b94*m.b178 + 29*m.b94*m.b181 + 30*m.b94*m.b184 + 31*m.b94*m.b187 + 32*m.b94*m.b190 + 33*m.b94*
                       m.b193 + 34*m.b94*m.b196 + 35*m.b94*m.b199 + 36*m.b94*m.b202 + 37*m.b94*m.b205 + 38*m.b94*m.b208
                        + m.b95*m.b98 + 2*m.b95*m.b101 + 3*m.b95*m.b104 + 4*m.b95*m.b107 + 5*m.b95*m.b110 + 6*m.b95*
                       m.b113 + 7*m.b95*m.b116 + 8*m.b95*m.b119 + 9*m.b95*m.b122 + 10*m.b95*m.b125 + 11*m.b95*m.b128 + 
                       12*m.b95*m.b131 + 13*m.b95*m.b134 + 14*m.b95*m.b137 + 15*m.b95*m.b140 + 16*m.b95*m.b143 + 17*
                       m.b95*m.b146 + 18*m.b95*m.b149 + 19*m.b95*m.b152 + 20*m.b95*m.b155 + 21*m.b95*m.b158 + 22*m.b95*
                       m.b161 + 23*m.b95*m.b164 + 24*m.b95*m.b167 + 25*m.b95*m.b170 + 26*m.b95*m.b173 + 27*m.b95*m.b176
                        + 28*m.b95*m.b179 + 29*m.b95*m.b182 + 30*m.b95*m.b185 + 31*m.b95*m.b188 + 32*m.b95*m.b191 + 33*
                       m.b95*m.b194 + 34*m.b95*m.b197 + 35*m.b95*m.b200 + 36*m.b95*m.b203 + 37*m.b95*m.b206 + 38*m.b95*
                       m.b209 + m.b96*m.b99 + 2*m.b96*m.b102 + 3*m.b96*m.b105 + 4*m.b96*m.b108 + 5*m.b96*m.b111 + 6*
                       m.b96*m.b114 + 7*m.b96*m.b117 + 8*m.b96*m.b120 + 9*m.b96*m.b123 + 10*m.b96*m.b126 + 11*m.b96*
                       m.b129 + 12*m.b96*m.b132 + 13*m.b96*m.b135 + 14*m.b96*m.b138 + 15*m.b96*m.b141 + 16*m.b96*m.b144
                        + 17*m.b96*m.b147 + 18*m.b96*m.b150 + 19*m.b96*m.b153 + 20*m.b96*m.b156 + 21*m.b96*m.b159 + 22*
                       m.b96*m.b162 + 23*m.b96*m.b165 + 24*m.b96*m.b168 + 25*m.b96*m.b171 + 26*m.b96*m.b174 + 27*m.b96*
                       m.b177 + 28*m.b96*m.b180 + 29*m.b96*m.b183 + 30*m.b96*m.b186 + 31*m.b96*m.b189 + 32*m.b96*m.b192
                        + 33*m.b96*m.b195 + 34*m.b96*m.b198 + 35*m.b96*m.b201 + 36*m.b96*m.b204 + 37*m.b96*m.b207 + 38*
                       m.b96*m.b210 + m.b97*m.b100 + 2*m.b97*m.b103 + 3*m.b97*m.b106 + 4*m.b97*m.b109 + 5*m.b97*m.b112
                        + 6*m.b97*m.b115 + 7*m.b97*m.b118 + 8*m.b97*m.b121 + 9*m.b97*m.b124 + 10*m.b97*m.b127 + 11*m.b97
                       *m.b130 + 12*m.b97*m.b133 + 13*m.b97*m.b136 + 14*m.b97*m.b139 + 15*m.b97*m.b142 + 16*m.b97*m.b145
                        + 17*m.b97*m.b148 + 18*m.b97*m.b151 + 19*m.b97*m.b154 + 20*m.b97*m.b157 + 21*m.b97*m.b160 + 22*
                       m.b97*m.b163 + 23*m.b97*m.b166 + 24*m.b97*m.b169 + 25*m.b97*m.b172 + 26*m.b97*m.b175 + 27*m.b97*
                       m.b178 + 28*m.b97*m.b181 + 29*m.b97*m.b184 + 30*m.b97*m.b187 + 31*m.b97*m.b190 + 32*m.b97*m.b193
                        + 33*m.b97*m.b196 + 34*m.b97*m.b199 + 35*m.b97*m.b202 + 36*m.b97*m.b205 + 37*m.b97*m.b208 + 
                       m.b98*m.b101 + 2*m.b98*m.b104 + 3*m.b98*m.b107 + 4*m.b98*m.b110 + 5*m.b98*m.b113 + 6*m.b98*m.b116
                        + 7*m.b98*m.b119 + 8*m.b98*m.b122 + 9*m.b98*m.b125 + 10*m.b98*m.b128 + 11*m.b98*m.b131 + 12*
                       m.b98*m.b134 + 13*m.b98*m.b137 + 14*m.b98*m.b140 + 15*m.b98*m.b143 + 16*m.b98*m.b146 + 17*m.b98*
                       m.b149 + 18*m.b98*m.b152 + 19*m.b98*m.b155 + 20*m.b98*m.b158 + 21*m.b98*m.b161 + 22*m.b98*m.b164
                        + 23*m.b98*m.b167 + 24*m.b98*m.b170 + 25*m.b98*m.b173 + 26*m.b98*m.b176 + 27*m.b98*m.b179 + 28*
                       m.b98*m.b182 + 29*m.b98*m.b185 + 30*m.b98*m.b188 + 31*m.b98*m.b191 + 32*m.b98*m.b194 + 33*m.b98*
                       m.b197 + 34*m.b98*m.b200 + 35*m.b98*m.b203 + 36*m.b98*m.b206 + 37*m.b98*m.b209 + m.b99*m.b102 + 2
                       *m.b99*m.b105 + 3*m.b99*m.b108 + 4*m.b99*m.b111 + 5*m.b99*m.b114 + 6*m.b99*m.b117 + 7*m.b99*
                       m.b120 + 8*m.b99*m.b123 + 9*m.b99*m.b126 + 10*m.b99*m.b129 + 11*m.b99*m.b132 + 12*m.b99*m.b135 + 
                       13*m.b99*m.b138 + 14*m.b99*m.b141 + 15*m.b99*m.b144 + 16*m.b99*m.b147 + 17*m.b99*m.b150 + 18*
                       m.b99*m.b153 + 19*m.b99*m.b156 + 20*m.b99*m.b159 + 21*m.b99*m.b162 + 22*m.b99*m.b165 + 23*m.b99*
                       m.b168 + 24*m.b99*m.b171 + 25*m.b99*m.b174 + 26*m.b99*m.b177 + 27*m.b99*m.b180 + 28*m.b99*m.b183
                        + 29*m.b99*m.b186 + 30*m.b99*m.b189 + 31*m.b99*m.b192 + 32*m.b99*m.b195 + 33*m.b99*m.b198 + 34*
                       m.b99*m.b201 + 35*m.b99*m.b204 + 36*m.b99*m.b207 + 37*m.b99*m.b210 + m.b100*m.b103 + 2*m.b100*
                       m.b106 + 3*m.b100*m.b109 + 4*m.b100*m.b112 + 5*m.b100*m.b115 + 6*m.b100*m.b118 + 7*m.b100*m.b121
                        + 8*m.b100*m.b124 + 9*m.b100*m.b127 + 10*m.b100*m.b130 + 11*m.b100*m.b133 + 12*m.b100*m.b136 + 
                       13*m.b100*m.b139 + 14*m.b100*m.b142 + 15*m.b100*m.b145 + 16*m.b100*m.b148 + 17*m.b100*m.b151 + 18
                       *m.b100*m.b154 + 19*m.b100*m.b157 + 20*m.b100*m.b160 + 21*m.b100*m.b163 + 22*m.b100*m.b166 + 23*
                       m.b100*m.b169 + 24*m.b100*m.b172 + 25*m.b100*m.b175 + 26*m.b100*m.b178 + 27*m.b100*m.b181 + 28*
                       m.b100*m.b184 + 29*m.b100*m.b187 + 30*m.b100*m.b190 + 31*m.b100*m.b193 + 32*m.b100*m.b196 + 33*
                       m.b100*m.b199 + 34*m.b100*m.b202 + 35*m.b100*m.b205 + 36*m.b100*m.b208 + m.b101*m.b104 + 2*m.b101
                       *m.b107 + 3*m.b101*m.b110 + 4*m.b101*m.b113 + 5*m.b101*m.b116 + 6*m.b101*m.b119 + 7*m.b101*m.b122
                        + 8*m.b101*m.b125 + 9*m.b101*m.b128 + 10*m.b101*m.b131 + 11*m.b101*m.b134 + 12*m.b101*m.b137 + 
                       13*m.b101*m.b140 + 14*m.b101*m.b143 + 15*m.b101*m.b146 + 16*m.b101*m.b149 + 17*m.b101*m.b152 + 18
                       *m.b101*m.b155 + 19*m.b101*m.b158 + 20*m.b101*m.b161 + 21*m.b101*m.b164 + 22*m.b101*m.b167 + 23*
                       m.b101*m.b170 + 24*m.b101*m.b173 + 25*m.b101*m.b176 + 26*m.b101*m.b179 + 27*m.b101*m.b182 + 28*
                       m.b101*m.b185 + 29*m.b101*m.b188 + 30*m.b101*m.b191 + 31*m.b101*m.b194 + 32*m.b101*m.b197 + 33*
                       m.b101*m.b200 + 34*m.b101*m.b203 + 35*m.b101*m.b206 + 36*m.b101*m.b209 + m.b102*m.b105 + 2*m.b102
                       *m.b108 + 3*m.b102*m.b111 + 4*m.b102*m.b114 + 5*m.b102*m.b117 + 6*m.b102*m.b120 + 7*m.b102*m.b123
                        + 8*m.b102*m.b126 + 9*m.b102*m.b129 + 10*m.b102*m.b132 + 11*m.b102*m.b135 + 12*m.b102*m.b138 + 
                       13*m.b102*m.b141 + 14*m.b102*m.b144 + 15*m.b102*m.b147 + 16*m.b102*m.b150 + 17*m.b102*m.b153 + 18
                       *m.b102*m.b156 + 19*m.b102*m.b159 + 20*m.b102*m.b162 + 21*m.b102*m.b165 + 22*m.b102*m.b168 + 23*
                       m.b102*m.b171 + 24*m.b102*m.b174 + 25*m.b102*m.b177 + 26*m.b102*m.b180 + 27*m.b102*m.b183 + 28*
                       m.b102*m.b186 + 29*m.b102*m.b189 + 30*m.b102*m.b192 + 31*m.b102*m.b195 + 32*m.b102*m.b198 + 33*
                       m.b102*m.b201 + 34*m.b102*m.b204 + 35*m.b102*m.b207 + 36*m.b102*m.b210 + m.b103*m.b106 + 2*m.b103
                       *m.b109 + 3*m.b103*m.b112 + 4*m.b103*m.b115 + 5*m.b103*m.b118 + 6*m.b103*m.b121 + 7*m.b103*m.b124
                        + 8*m.b103*m.b127 + 9*m.b103*m.b130 + 10*m.b103*m.b133 + 11*m.b103*m.b136 + 12*m.b103*m.b139 + 
                       13*m.b103*m.b142 + 14*m.b103*m.b145 + 15*m.b103*m.b148 + 16*m.b103*m.b151 + 17*m.b103*m.b154 + 18
                       *m.b103*m.b157 + 19*m.b103*m.b160 + 20*m.b103*m.b163 + 21*m.b103*m.b166 + 22*m.b103*m.b169 + 23*
                       m.b103*m.b172 + 24*m.b103*m.b175 + 25*m.b103*m.b178 + 26*m.b103*m.b181 + 27*m.b103*m.b184 + 28*
                       m.b103*m.b187 + 29*m.b103*m.b190 + 30*m.b103*m.b193 + 31*m.b103*m.b196 + 32*m.b103*m.b199 + 33*
                       m.b103*m.b202 + 34*m.b103*m.b205 + 35*m.b103*m.b208 + m.b104*m.b107 + 2*m.b104*m.b110 + 3*m.b104*
                       m.b113 + 4*m.b104*m.b116 + 5*m.b104*m.b119 + 6*m.b104*m.b122 + 7*m.b104*m.b125 + 8*m.b104*m.b128
                        + 9*m.b104*m.b131 + 10*m.b104*m.b134 + 11*m.b104*m.b137 + 12*m.b104*m.b140 + 13*m.b104*m.b143 + 
                       14*m.b104*m.b146 + 15*m.b104*m.b149 + 16*m.b104*m.b152 + 17*m.b104*m.b155 + 18*m.b104*m.b158 + 19
                       *m.b104*m.b161 + 20*m.b104*m.b164 + 21*m.b104*m.b167 + 22*m.b104*m.b170 + 23*m.b104*m.b173 + 24*
                       m.b104*m.b176 + 25*m.b104*m.b179 + 26*m.b104*m.b182 + 27*m.b104*m.b185 + 28*m.b104*m.b188 + 29*
                       m.b104*m.b191 + 30*m.b104*m.b194 + 31*m.b104*m.b197 + 32*m.b104*m.b200 + 33*m.b104*m.b203 + 34*
                       m.b104*m.b206 + 35*m.b104*m.b209 + m.b105*m.b108 + 2*m.b105*m.b111 + 3*m.b105*m.b114 + 4*m.b105*
                       m.b117 + 5*m.b105*m.b120 + 6*m.b105*m.b123 + 7*m.b105*m.b126 + 8*m.b105*m.b129 + 9*m.b105*m.b132
                        + 10*m.b105*m.b135 + 11*m.b105*m.b138 + 12*m.b105*m.b141 + 13*m.b105*m.b144 + 14*m.b105*m.b147
                        + 15*m.b105*m.b150 + 16*m.b105*m.b153 + 17*m.b105*m.b156 + 18*m.b105*m.b159 + 19*m.b105*m.b162
                        + 20*m.b105*m.b165 + 21*m.b105*m.b168 + 22*m.b105*m.b171 + 23*m.b105*m.b174 + 24*m.b105*m.b177
                        + 25*m.b105*m.b180 + 26*m.b105*m.b183 + 27*m.b105*m.b186 + 28*m.b105*m.b189 + 29*m.b105*m.b192
                        + 30*m.b105*m.b195 + 31*m.b105*m.b198 + 32*m.b105*m.b201 + 33*m.b105*m.b204 + 34*m.b105*m.b207
                        + 35*m.b105*m.b210 + m.b106*m.b109 + 2*m.b106*m.b112 + 3*m.b106*m.b115 + 4*m.b106*m.b118 + 5*
                       m.b106*m.b121 + 6*m.b106*m.b124 + 7*m.b106*m.b127 + 8*m.b106*m.b130 + 9*m.b106*m.b133 + 10*m.b106
                       *m.b136 + 11*m.b106*m.b139 + 12*m.b106*m.b142 + 13*m.b106*m.b145 + 14*m.b106*m.b148 + 15*m.b106*
                       m.b151 + 16*m.b106*m.b154 + 17*m.b106*m.b157 + 18*m.b106*m.b160 + 19*m.b106*m.b163 + 20*m.b106*
                       m.b166 + 21*m.b106*m.b169 + 22*m.b106*m.b172 + 23*m.b106*m.b175 + 24*m.b106*m.b178 + 25*m.b106*
                       m.b181 + 26*m.b106*m.b184 + 27*m.b106*m.b187 + 28*m.b106*m.b190 + 29*m.b106*m.b193 + 30*m.b106*
                       m.b196 + 31*m.b106*m.b199 + 32*m.b106*m.b202 + 33*m.b106*m.b205 + 34*m.b106*m.b208 + m.b107*
                       m.b110 + 2*m.b107*m.b113 + 3*m.b107*m.b116 + 4*m.b107*m.b119 + 5*m.b107*m.b122 + 6*m.b107*m.b125
                        + 7*m.b107*m.b128 + 8*m.b107*m.b131 + 9*m.b107*m.b134 + 10*m.b107*m.b137 + 11*m.b107*m.b140 + 12
                       *m.b107*m.b143 + 13*m.b107*m.b146 + 14*m.b107*m.b149 + 15*m.b107*m.b152 + 16*m.b107*m.b155 + 17*
                       m.b107*m.b158 + 18*m.b107*m.b161 + 19*m.b107*m.b164 + 20*m.b107*m.b167 + 21*m.b107*m.b170 + 22*
                       m.b107*m.b173 + 23*m.b107*m.b176 + 24*m.b107*m.b179 + 25*m.b107*m.b182 + 26*m.b107*m.b185 + 27*
                       m.b107*m.b188 + 28*m.b107*m.b191 + 29*m.b107*m.b194 + 30*m.b107*m.b197 + 31*m.b107*m.b200 + 32*
                       m.b107*m.b203 + 33*m.b107*m.b206 + 34*m.b107*m.b209 + m.b108*m.b111 + 2*m.b108*m.b114 + 3*m.b108*
                       m.b117 + 4*m.b108*m.b120 + 5*m.b108*m.b123 + 6*m.b108*m.b126 + 7*m.b108*m.b129 + 8*m.b108*m.b132
                        + 9*m.b108*m.b135 + 10*m.b108*m.b138 + 11*m.b108*m.b141 + 12*m.b108*m.b144 + 13*m.b108*m.b147 + 
                       14*m.b108*m.b150 + 15*m.b108*m.b153 + 16*m.b108*m.b156 + 17*m.b108*m.b159 + 18*m.b108*m.b162 + 19
                       *m.b108*m.b165 + 20*m.b108*m.b168 + 21*m.b108*m.b171 + 22*m.b108*m.b174 + 23*m.b108*m.b177 + 24*
                       m.b108*m.b180 + 25*m.b108*m.b183 + 26*m.b108*m.b186 + 27*m.b108*m.b189 + 28*m.b108*m.b192 + 29*
                       m.b108*m.b195 + 30*m.b108*m.b198 + 31*m.b108*m.b201 + 32*m.b108*m.b204 + 33*m.b108*m.b207 + 34*
                       m.b108*m.b210 + m.b109*m.b112 + 2*m.b109*m.b115 + 3*m.b109*m.b118 + 4*m.b109*m.b121 + 5*m.b109*
                       m.b124 + 6*m.b109*m.b127 + 7*m.b109*m.b130 + 8*m.b109*m.b133 + 9*m.b109*m.b136 + 10*m.b109*m.b139
                        + 11*m.b109*m.b142 + 12*m.b109*m.b145 + 13*m.b109*m.b148 + 14*m.b109*m.b151 + 15*m.b109*m.b154
                        + 16*m.b109*m.b157 + 17*m.b109*m.b160 + 18*m.b109*m.b163 + 19*m.b109*m.b166 + 20*m.b109*m.b169
                        + 21*m.b109*m.b172 + 22*m.b109*m.b175 + 23*m.b109*m.b178 + 24*m.b109*m.b181 + 25*m.b109*m.b184
                        + 26*m.b109*m.b187 + 27*m.b109*m.b190 + 28*m.b109*m.b193 + 29*m.b109*m.b196 + 30*m.b109*m.b199
                        + 31*m.b109*m.b202 + 32*m.b109*m.b205 + 33*m.b109*m.b208 + m.b110*m.b113 + 2*m.b110*m.b116 + 3*
                       m.b110*m.b119 + 4*m.b110*m.b122 + 5*m.b110*m.b125 + 6*m.b110*m.b128 + 7*m.b110*m.b131 + 8*m.b110*
                       m.b134 + 9*m.b110*m.b137 + 10*m.b110*m.b140 + 11*m.b110*m.b143 + 12*m.b110*m.b146 + 13*m.b110*
                       m.b149 + 14*m.b110*m.b152 + 15*m.b110*m.b155 + 16*m.b110*m.b158 + 17*m.b110*m.b161 + 18*m.b110*
                       m.b164 + 19*m.b110*m.b167 + 20*m.b110*m.b170 + 21*m.b110*m.b173 + 22*m.b110*m.b176 + 23*m.b110*
                       m.b179 + 24*m.b110*m.b182 + 25*m.b110*m.b185 + 26*m.b110*m.b188 + 27*m.b110*m.b191 + 28*m.b110*
                       m.b194 + 29*m.b110*m.b197 + 30*m.b110*m.b200 + 31*m.b110*m.b203 + 32*m.b110*m.b206 + 33*m.b110*
                       m.b209 + m.b111*m.b114 + 2*m.b111*m.b117 + 3*m.b111*m.b120 + 4*m.b111*m.b123 + 5*m.b111*m.b126 + 
                       6*m.b111*m.b129 + 7*m.b111*m.b132 + 8*m.b111*m.b135 + 9*m.b111*m.b138 + 10*m.b111*m.b141 + 11*
                       m.b111*m.b144 + 12*m.b111*m.b147 + 13*m.b111*m.b150 + 14*m.b111*m.b153 + 15*m.b111*m.b156 + 16*
                       m.b111*m.b159 + 17*m.b111*m.b162 + 18*m.b111*m.b165 + 19*m.b111*m.b168 + 20*m.b111*m.b171 + 21*
                       m.b111*m.b174 + 22*m.b111*m.b177 + 23*m.b111*m.b180 + 24*m.b111*m.b183 + 25*m.b111*m.b186 + 26*
                       m.b111*m.b189 + 27*m.b111*m.b192 + 28*m.b111*m.b195 + 29*m.b111*m.b198 + 30*m.b111*m.b201 + 31*
                       m.b111*m.b204 + 32*m.b111*m.b207 + 33*m.b111*m.b210 + m.b112*m.b115 + 2*m.b112*m.b118 + 3*m.b112*
                       m.b121 + 4*m.b112*m.b124 + 5*m.b112*m.b127 + 6*m.b112*m.b130 + 7*m.b112*m.b133 + 8*m.b112*m.b136
                        + 9*m.b112*m.b139 + 10*m.b112*m.b142 + 11*m.b112*m.b145 + 12*m.b112*m.b148 + 13*m.b112*m.b151 + 
                       14*m.b112*m.b154 + 15*m.b112*m.b157 + 16*m.b112*m.b160 + 17*m.b112*m.b163 + 18*m.b112*m.b166 + 19
                       *m.b112*m.b169 + 20*m.b112*m.b172 + 21*m.b112*m.b175 + 22*m.b112*m.b178 + 23*m.b112*m.b181 + 24*
                       m.b112*m.b184 + 25*m.b112*m.b187 + 26*m.b112*m.b190 + 27*m.b112*m.b193 + 28*m.b112*m.b196 + 29*
                       m.b112*m.b199 + 30*m.b112*m.b202 + 31*m.b112*m.b205 + 32*m.b112*m.b208 + m.b113*m.b116 + 2*m.b113
                       *m.b119 + 3*m.b113*m.b122 + 4*m.b113*m.b125 + 5*m.b113*m.b128 + 6*m.b113*m.b131 + 7*m.b113*m.b134
                        + 8*m.b113*m.b137 + 9*m.b113*m.b140 + 10*m.b113*m.b143 + 11*m.b113*m.b146 + 12*m.b113*m.b149 + 
                       13*m.b113*m.b152 + 14*m.b113*m.b155 + 15*m.b113*m.b158 + 16*m.b113*m.b161 + 17*m.b113*m.b164 + 18
                       *m.b113*m.b167 + 19*m.b113*m.b170 + 20*m.b113*m.b173 + 21*m.b113*m.b176 + 22*m.b113*m.b179 + 23*
                       m.b113*m.b182 + 24*m.b113*m.b185 + 25*m.b113*m.b188 + 26*m.b113*m.b191 + 27*m.b113*m.b194 + 28*
                       m.b113*m.b197 + 29*m.b113*m.b200 + 30*m.b113*m.b203 + 31*m.b113*m.b206 + 32*m.b113*m.b209 + 
                       m.b114*m.b117 + 2*m.b114*m.b120 + 3*m.b114*m.b123 + 4*m.b114*m.b126 + 5*m.b114*m.b129 + 6*m.b114*
                       m.b132 + 7*m.b114*m.b135 + 8*m.b114*m.b138 + 9*m.b114*m.b141 + 10*m.b114*m.b144 + 11*m.b114*
                       m.b147 + 12*m.b114*m.b150 + 13*m.b114*m.b153 + 14*m.b114*m.b156 + 15*m.b114*m.b159 + 16*m.b114*
                       m.b162 + 17*m.b114*m.b165 + 18*m.b114*m.b168 + 19*m.b114*m.b171 + 20*m.b114*m.b174 + 21*m.b114*
                       m.b177 + 22*m.b114*m.b180 + 23*m.b114*m.b183 + 24*m.b114*m.b186 + 25*m.b114*m.b189 + 26*m.b114*
                       m.b192 + 27*m.b114*m.b195 + 28*m.b114*m.b198 + 29*m.b114*m.b201 + 30*m.b114*m.b204 + 31*m.b114*
                       m.b207 + 32*m.b114*m.b210 + m.b115*m.b118 + 2*m.b115*m.b121 + 3*m.b115*m.b124 + 4*m.b115*m.b127
                        + 5*m.b115*m.b130 + 6*m.b115*m.b133 + 7*m.b115*m.b136 + 8*m.b115*m.b139 + 9*m.b115*m.b142 + 10*
                       m.b115*m.b145 + 11*m.b115*m.b148 + 12*m.b115*m.b151 + 13*m.b115*m.b154 + 14*m.b115*m.b157 + 15*
                       m.b115*m.b160 + 16*m.b115*m.b163 + 17*m.b115*m.b166 + 18*m.b115*m.b169 + 19*m.b115*m.b172 + 20*
                       m.b115*m.b175 + 21*m.b115*m.b178 + 22*m.b115*m.b181 + 23*m.b115*m.b184 + 24*m.b115*m.b187 + 25*
                       m.b115*m.b190 + 26*m.b115*m.b193 + 27*m.b115*m.b196 + 28*m.b115*m.b199 + 29*m.b115*m.b202 + 30*
                       m.b115*m.b205 + 31*m.b115*m.b208 + m.b116*m.b119 + 2*m.b116*m.b122 + 3*m.b116*m.b125 + 4*m.b116*
                       m.b128 + 5*m.b116*m.b131 + 6*m.b116*m.b134 + 7*m.b116*m.b137 + 8*m.b116*m.b140 + 9*m.b116*m.b143
                        + 10*m.b116*m.b146 + 11*m.b116*m.b149 + 12*m.b116*m.b152 + 13*m.b116*m.b155 + 14*m.b116*m.b158
                        + 15*m.b116*m.b161 + 16*m.b116*m.b164 + 17*m.b116*m.b167 + 18*m.b116*m.b170 + 19*m.b116*m.b173
                        + 20*m.b116*m.b176 + 21*m.b116*m.b179 + 22*m.b116*m.b182 + 23*m.b116*m.b185 + 24*m.b116*m.b188
                        + 25*m.b116*m.b191 + 26*m.b116*m.b194 + 27*m.b116*m.b197 + 28*m.b116*m.b200 + 29*m.b116*m.b203
                        + 30*m.b116*m.b206 + 31*m.b116*m.b209 + m.b117*m.b120 + 2*m.b117*m.b123 + 3*m.b117*m.b126 + 4*
                       m.b117*m.b129 + 5*m.b117*m.b132 + 6*m.b117*m.b135 + 7*m.b117*m.b138 + 8*m.b117*m.b141 + 9*m.b117*
                       m.b144 + 10*m.b117*m.b147 + 11*m.b117*m.b150 + 12*m.b117*m.b153 + 13*m.b117*m.b156 + 14*m.b117*
                       m.b159 + 15*m.b117*m.b162 + 16*m.b117*m.b165 + 17*m.b117*m.b168 + 18*m.b117*m.b171 + 19*m.b117*
                       m.b174 + 20*m.b117*m.b177 + 21*m.b117*m.b180 + 22*m.b117*m.b183 + 23*m.b117*m.b186 + 24*m.b117*
                       m.b189 + 25*m.b117*m.b192 + 26*m.b117*m.b195 + 27*m.b117*m.b198 + 28*m.b117*m.b201 + 29*m.b117*
                       m.b204 + 30*m.b117*m.b207 + 31*m.b117*m.b210 + m.b118*m.b121 + 2*m.b118*m.b124 + 3*m.b118*m.b127
                        + 4*m.b118*m.b130 + 5*m.b118*m.b133 + 6*m.b118*m.b136 + 7*m.b118*m.b139 + 8*m.b118*m.b142 + 9*
                       m.b118*m.b145 + 10*m.b118*m.b148 + 11*m.b118*m.b151 + 12*m.b118*m.b154 + 13*m.b118*m.b157 + 14*
                       m.b118*m.b160 + 15*m.b118*m.b163 + 16*m.b118*m.b166 + 17*m.b118*m.b169 + 18*m.b118*m.b172 + 19*
                       m.b118*m.b175 + 20*m.b118*m.b178 + 21*m.b118*m.b181 + 22*m.b118*m.b184 + 23*m.b118*m.b187 + 24*
                       m.b118*m.b190 + 25*m.b118*m.b193 + 26*m.b118*m.b196 + 27*m.b118*m.b199 + 28*m.b118*m.b202 + 29*
                       m.b118*m.b205 + 30*m.b118*m.b208 + m.b119*m.b122 + 2*m.b119*m.b125 + 3*m.b119*m.b128 + 4*m.b119*
                       m.b131 + 5*m.b119*m.b134 + 6*m.b119*m.b137 + 7*m.b119*m.b140 + 8*m.b119*m.b143 + 9*m.b119*m.b146
                        + 10*m.b119*m.b149 + 11*m.b119*m.b152 + 12*m.b119*m.b155 + 13*m.b119*m.b158 + 14*m.b119*m.b161
                        + 15*m.b119*m.b164 + 16*m.b119*m.b167 + 17*m.b119*m.b170 + 18*m.b119*m.b173 + 19*m.b119*m.b176
                        + 20*m.b119*m.b179 + 21*m.b119*m.b182 + 22*m.b119*m.b185 + 23*m.b119*m.b188 + 24*m.b119*m.b191
                        + 25*m.b119*m.b194 + 26*m.b119*m.b197 + 27*m.b119*m.b200 + 28*m.b119*m.b203 + 29*m.b119*m.b206
                        + 30*m.b119*m.b209 + m.b120*m.b123 + 2*m.b120*m.b126 + 3*m.b120*m.b129 + 4*m.b120*m.b132 + 5*
                       m.b120*m.b135 + 6*m.b120*m.b138 + 7*m.b120*m.b141 + 8*m.b120*m.b144 + 9*m.b120*m.b147 + 10*m.b120
                       *m.b150 + 11*m.b120*m.b153 + 12*m.b120*m.b156 + 13*m.b120*m.b159 + 14*m.b120*m.b162 + 15*m.b120*
                       m.b165 + 16*m.b120*m.b168 + 17*m.b120*m.b171 + 18*m.b120*m.b174 + 19*m.b120*m.b177 + 20*m.b120*
                       m.b180 + 21*m.b120*m.b183 + 22*m.b120*m.b186 + 23*m.b120*m.b189 + 24*m.b120*m.b192 + 25*m.b120*
                       m.b195 + 26*m.b120*m.b198 + 27*m.b120*m.b201 + 28*m.b120*m.b204 + 29*m.b120*m.b207 + 30*m.b120*
                       m.b210 + m.b121*m.b124 + 2*m.b121*m.b127 + 3*m.b121*m.b130 + 4*m.b121*m.b133 + 5*m.b121*m.b136 + 
                       6*m.b121*m.b139 + 7*m.b121*m.b142 + 8*m.b121*m.b145 + 9*m.b121*m.b148 + 10*m.b121*m.b151 + 11*
                       m.b121*m.b154 + 12*m.b121*m.b157 + 13*m.b121*m.b160 + 14*m.b121*m.b163 + 15*m.b121*m.b166 + 16*
                       m.b121*m.b169 + 17*m.b121*m.b172 + 18*m.b121*m.b175 + 19*m.b121*m.b178 + 20*m.b121*m.b181 + 21*
                       m.b121*m.b184 + 22*m.b121*m.b187 + 23*m.b121*m.b190 + 24*m.b121*m.b193 + 25*m.b121*m.b196 + 26*
                       m.b121*m.b199 + 27*m.b121*m.b202 + 28*m.b121*m.b205 + 29*m.b121*m.b208 + m.b122*m.b125 + 2*m.b122
                       *m.b128 + 3*m.b122*m.b131 + 4*m.b122*m.b134 + 5*m.b122*m.b137 + 6*m.b122*m.b140 + 7*m.b122*m.b143
                        + 8*m.b122*m.b146 + 9*m.b122*m.b149 + 10*m.b122*m.b152 + 11*m.b122*m.b155 + 12*m.b122*m.b158 + 
                       13*m.b122*m.b161 + 14*m.b122*m.b164 + 15*m.b122*m.b167 + 16*m.b122*m.b170 + 17*m.b122*m.b173 + 18
                       *m.b122*m.b176 + 19*m.b122*m.b179 + 20*m.b122*m.b182 + 21*m.b122*m.b185 + 22*m.b122*m.b188 + 23*
                       m.b122*m.b191 + 24*m.b122*m.b194 + 25*m.b122*m.b197 + 26*m.b122*m.b200 + 27*m.b122*m.b203 + 28*
                       m.b122*m.b206 + 29*m.b122*m.b209 + m.b123*m.b126 + 2*m.b123*m.b129 + 3*m.b123*m.b132 + 4*m.b123*
                       m.b135 + 5*m.b123*m.b138 + 6*m.b123*m.b141 + 7*m.b123*m.b144 + 8*m.b123*m.b147 + 9*m.b123*m.b150
                        + 10*m.b123*m.b153 + 11*m.b123*m.b156 + 12*m.b123*m.b159 + 13*m.b123*m.b162 + 14*m.b123*m.b165
                        + 15*m.b123*m.b168 + 16*m.b123*m.b171 + 17*m.b123*m.b174 + 18*m.b123*m.b177 + 19*m.b123*m.b180
                        + 20*m.b123*m.b183 + 21*m.b123*m.b186 + 22*m.b123*m.b189 + 23*m.b123*m.b192 + 24*m.b123*m.b195
                        + 25*m.b123*m.b198 + 26*m.b123*m.b201 + 27*m.b123*m.b204 + 28*m.b123*m.b207 + 29*m.b123*m.b210
                        + m.b124*m.b127 + 2*m.b124*m.b130 + 3*m.b124*m.b133 + 4*m.b124*m.b136 + 5*m.b124*m.b139 + 6*
                       m.b124*m.b142 + 7*m.b124*m.b145 + 8*m.b124*m.b148 + 9*m.b124*m.b151 + 10*m.b124*m.b154 + 11*
                       m.b124*m.b157 + 12*m.b124*m.b160 + 13*m.b124*m.b163 + 14*m.b124*m.b166 + 15*m.b124*m.b169 + 16*
                       m.b124*m.b172 + 17*m.b124*m.b175 + 18*m.b124*m.b178 + 19*m.b124*m.b181 + 20*m.b124*m.b184 + 21*
                       m.b124*m.b187 + 22*m.b124*m.b190 + 23*m.b124*m.b193 + 24*m.b124*m.b196 + 25*m.b124*m.b199 + 26*
                       m.b124*m.b202 + 27*m.b124*m.b205 + 28*m.b124*m.b208 + m.b125*m.b128 + 2*m.b125*m.b131 + 3*m.b125*
                       m.b134 + 4*m.b125*m.b137 + 5*m.b125*m.b140 + 6*m.b125*m.b143 + 7*m.b125*m.b146 + 8*m.b125*m.b149
                        + 9*m.b125*m.b152 + 10*m.b125*m.b155 + 11*m.b125*m.b158 + 12*m.b125*m.b161 + 13*m.b125*m.b164 + 
                       14*m.b125*m.b167 + 15*m.b125*m.b170 + 16*m.b125*m.b173 + 17*m.b125*m.b176 + 18*m.b125*m.b179 + 19
                       *m.b125*m.b182 + 20*m.b125*m.b185 + 21*m.b125*m.b188 + 22*m.b125*m.b191 + 23*m.b125*m.b194 + 24*
                       m.b125*m.b197 + 25*m.b125*m.b200 + 26*m.b125*m.b203 + 27*m.b125*m.b206 + 28*m.b125*m.b209 + 
                       m.b126*m.b129 + 2*m.b126*m.b132 + 3*m.b126*m.b135 + 4*m.b126*m.b138 + 5*m.b126*m.b141 + 6*m.b126*
                       m.b144 + 7*m.b126*m.b147 + 8*m.b126*m.b150 + 9*m.b126*m.b153 + 10*m.b126*m.b156 + 11*m.b126*
                       m.b159 + 12*m.b126*m.b162 + 13*m.b126*m.b165 + 14*m.b126*m.b168 + 15*m.b126*m.b171 + 16*m.b126*
                       m.b174 + 17*m.b126*m.b177 + 18*m.b126*m.b180 + 19*m.b126*m.b183 + 20*m.b126*m.b186 + 21*m.b126*
                       m.b189 + 22*m.b126*m.b192 + 23*m.b126*m.b195 + 24*m.b126*m.b198 + 25*m.b126*m.b201 + 26*m.b126*
                       m.b204 + 27*m.b126*m.b207 + 28*m.b126*m.b210 + m.b127*m.b130 + 2*m.b127*m.b133 + 3*m.b127*m.b136
                        + 4*m.b127*m.b139 + 5*m.b127*m.b142 + 6*m.b127*m.b145 + 7*m.b127*m.b148 + 8*m.b127*m.b151 + 9*
                       m.b127*m.b154 + 10*m.b127*m.b157 + 11*m.b127*m.b160 + 12*m.b127*m.b163 + 13*m.b127*m.b166 + 14*
                       m.b127*m.b169 + 15*m.b127*m.b172 + 16*m.b127*m.b175 + 17*m.b127*m.b178 + 18*m.b127*m.b181 + 19*
                       m.b127*m.b184 + 20*m.b127*m.b187 + 21*m.b127*m.b190 + 22*m.b127*m.b193 + 23*m.b127*m.b196 + 24*
                       m.b127*m.b199 + 25*m.b127*m.b202 + 26*m.b127*m.b205 + 27*m.b127*m.b208 + m.b128*m.b131 + 2*m.b128
                       *m.b134 + 3*m.b128*m.b137 + 4*m.b128*m.b140 + 5*m.b128*m.b143 + 6*m.b128*m.b146 + 7*m.b128*m.b149
                        + 8*m.b128*m.b152 + 9*m.b128*m.b155 + 10*m.b128*m.b158 + 11*m.b128*m.b161 + 12*m.b128*m.b164 + 
                       13*m.b128*m.b167 + 14*m.b128*m.b170 + 15*m.b128*m.b173 + 16*m.b128*m.b176 + 17*m.b128*m.b179 + 18
                       *m.b128*m.b182 + 19*m.b128*m.b185 + 20*m.b128*m.b188 + 21*m.b128*m.b191 + 22*m.b128*m.b194 + 23*
                       m.b128*m.b197 + 24*m.b128*m.b200 + 25*m.b128*m.b203 + 26*m.b128*m.b206 + 27*m.b128*m.b209 + 
                       m.b129*m.b132 + 2*m.b129*m.b135 + 3*m.b129*m.b138 + 4*m.b129*m.b141 + 5*m.b129*m.b144 + 6*m.b129*
                       m.b147 + 7*m.b129*m.b150 + 8*m.b129*m.b153 + 9*m.b129*m.b156 + 10*m.b129*m.b159 + 11*m.b129*
                       m.b162 + 12*m.b129*m.b165 + 13*m.b129*m.b168 + 14*m.b129*m.b171 + 15*m.b129*m.b174 + 16*m.b129*
                       m.b177 + 17*m.b129*m.b180 + 18*m.b129*m.b183 + 19*m.b129*m.b186 + 20*m.b129*m.b189 + 21*m.b129*
                       m.b192 + 22*m.b129*m.b195 + 23*m.b129*m.b198 + 24*m.b129*m.b201 + 25*m.b129*m.b204 + 26*m.b129*
                       m.b207 + 27*m.b129*m.b210 + m.b130*m.b133 + 2*m.b130*m.b136 + 3*m.b130*m.b139 + 4*m.b130*m.b142
                        + 5*m.b130*m.b145 + 6*m.b130*m.b148 + 7*m.b130*m.b151 + 8*m.b130*m.b154 + 9*m.b130*m.b157 + 10*
                       m.b130*m.b160 + 11*m.b130*m.b163 + 12*m.b130*m.b166 + 13*m.b130*m.b169 + 14*m.b130*m.b172 + 15*
                       m.b130*m.b175 + 16*m.b130*m.b178 + 17*m.b130*m.b181 + 18*m.b130*m.b184 + 19*m.b130*m.b187 + 20*
                       m.b130*m.b190 + 21*m.b130*m.b193 + 22*m.b130*m.b196 + 23*m.b130*m.b199 + 24*m.b130*m.b202 + 25*
                       m.b130*m.b205 + 26*m.b130*m.b208 + m.b131*m.b134 + 2*m.b131*m.b137 + 3*m.b131*m.b140 + 4*m.b131*
                       m.b143 + 5*m.b131*m.b146 + 6*m.b131*m.b149 + 7*m.b131*m.b152 + 8*m.b131*m.b155 + 9*m.b131*m.b158
                        + 10*m.b131*m.b161 + 11*m.b131*m.b164 + 12*m.b131*m.b167 + 13*m.b131*m.b170 + 14*m.b131*m.b173
                        + 15*m.b131*m.b176 + 16*m.b131*m.b179 + 17*m.b131*m.b182 + 18*m.b131*m.b185 + 19*m.b131*m.b188
                        + 20*m.b131*m.b191 + 21*m.b131*m.b194 + 22*m.b131*m.b197 + 23*m.b131*m.b200 + 24*m.b131*m.b203
                        + 25*m.b131*m.b206 + 26*m.b131*m.b209 + m.b132*m.b135 + 2*m.b132*m.b138 + 3*m.b132*m.b141 + 4*
                       m.b132*m.b144 + 5*m.b132*m.b147 + 6*m.b132*m.b150 + 7*m.b132*m.b153 + 8*m.b132*m.b156 + 9*m.b132*
                       m.b159 + 10*m.b132*m.b162 + 11*m.b132*m.b165 + 12*m.b132*m.b168 + 13*m.b132*m.b171 + 14*m.b132*
                       m.b174 + 15*m.b132*m.b177 + 16*m.b132*m.b180 + 17*m.b132*m.b183 + 18*m.b132*m.b186 + 19*m.b132*
                       m.b189 + 20*m.b132*m.b192 + 21*m.b132*m.b195 + 22*m.b132*m.b198 + 23*m.b132*m.b201 + 24*m.b132*
                       m.b204 + 25*m.b132*m.b207 + 26*m.b132*m.b210 + m.b133*m.b136 + 2*m.b133*m.b139 + 3*m.b133*m.b142
                        + 4*m.b133*m.b145 + 5*m.b133*m.b148 + 6*m.b133*m.b151 + 7*m.b133*m.b154 + 8*m.b133*m.b157 + 9*
                       m.b133*m.b160 + 10*m.b133*m.b163 + 11*m.b133*m.b166 + 12*m.b133*m.b169 + 13*m.b133*m.b172 + 14*
                       m.b133*m.b175 + 15*m.b133*m.b178 + 16*m.b133*m.b181 + 17*m.b133*m.b184 + 18*m.b133*m.b187 + 19*
                       m.b133*m.b190 + 20*m.b133*m.b193 + 21*m.b133*m.b196 + 22*m.b133*m.b199 + 23*m.b133*m.b202 + 24*
                       m.b133*m.b205 + 25*m.b133*m.b208 + m.b134*m.b137 + 2*m.b134*m.b140 + 3*m.b134*m.b143 + 4*m.b134*
                       m.b146 + 5*m.b134*m.b149 + 6*m.b134*m.b152 + 7*m.b134*m.b155 + 8*m.b134*m.b158 + 9*m.b134*m.b161
                        + 10*m.b134*m.b164 + 11*m.b134*m.b167 + 12*m.b134*m.b170 + 13*m.b134*m.b173 + 14*m.b134*m.b176
                        + 15*m.b134*m.b179 + 16*m.b134*m.b182 + 17*m.b134*m.b185 + 18*m.b134*m.b188 + 19*m.b134*m.b191
                        + 20*m.b134*m.b194 + 21*m.b134*m.b197 + 22*m.b134*m.b200 + 23*m.b134*m.b203 + 24*m.b134*m.b206
                        + 25*m.b134*m.b209 + m.b135*m.b138 + 2*m.b135*m.b141 + 3*m.b135*m.b144 + 4*m.b135*m.b147 + 5*
                       m.b135*m.b150 + 6*m.b135*m.b153 + 7*m.b135*m.b156 + 8*m.b135*m.b159 + 9*m.b135*m.b162 + 10*m.b135
                       *m.b165 + 11*m.b135*m.b168 + 12*m.b135*m.b171 + 13*m.b135*m.b174 + 14*m.b135*m.b177 + 15*m.b135*
                       m.b180 + 16*m.b135*m.b183 + 17*m.b135*m.b186 + 18*m.b135*m.b189 + 19*m.b135*m.b192 + 20*m.b135*
                       m.b195 + 21*m.b135*m.b198 + 22*m.b135*m.b201 + 23*m.b135*m.b204 + 24*m.b135*m.b207 + 25*m.b135*
                       m.b210 + m.b136*m.b139 + 2*m.b136*m.b142 + 3*m.b136*m.b145 + 4*m.b136*m.b148 + 5*m.b136*m.b151 + 
                       6*m.b136*m.b154 + 7*m.b136*m.b157 + 8*m.b136*m.b160 + 9*m.b136*m.b163 + 10*m.b136*m.b166 + 11*
                       m.b136*m.b169 + 12*m.b136*m.b172 + 13*m.b136*m.b175 + 14*m.b136*m.b178 + 15*m.b136*m.b181 + 16*
                       m.b136*m.b184 + 17*m.b136*m.b187 + 18*m.b136*m.b190 + 19*m.b136*m.b193 + 20*m.b136*m.b196 + 21*
                       m.b136*m.b199 + 22*m.b136*m.b202 + 23*m.b136*m.b205 + 24*m.b136*m.b208 + m.b137*m.b140 + 2*m.b137
                       *m.b143 + 3*m.b137*m.b146 + 4*m.b137*m.b149 + 5*m.b137*m.b152 + 6*m.b137*m.b155 + 7*m.b137*m.b158
                        + 8*m.b137*m.b161 + 9*m.b137*m.b164 + 10*m.b137*m.b167 + 11*m.b137*m.b170 + 12*m.b137*m.b173 + 
                       13*m.b137*m.b176 + 14*m.b137*m.b179 + 15*m.b137*m.b182 + 16*m.b137*m.b185 + 17*m.b137*m.b188 + 18
                       *m.b137*m.b191 + 19*m.b137*m.b194 + 20*m.b137*m.b197 + 21*m.b137*m.b200 + 22*m.b137*m.b203 + 23*
                       m.b137*m.b206 + 24*m.b137*m.b209 + m.b138*m.b141 + 2*m.b138*m.b144 + 3*m.b138*m.b147 + 4*m.b138*
                       m.b150 + 5*m.b138*m.b153 + 6*m.b138*m.b156 + 7*m.b138*m.b159 + 8*m.b138*m.b162 + 9*m.b138*m.b165
                        + 10*m.b138*m.b168 + 11*m.b138*m.b171 + 12*m.b138*m.b174 + 13*m.b138*m.b177 + 14*m.b138*m.b180
                        + 15*m.b138*m.b183 + 16*m.b138*m.b186 + 17*m.b138*m.b189 + 18*m.b138*m.b192 + 19*m.b138*m.b195
                        + 20*m.b138*m.b198 + 21*m.b138*m.b201 + 22*m.b138*m.b204 + 23*m.b138*m.b207 + 24*m.b138*m.b210
                        + m.b139*m.b142 + 2*m.b139*m.b145 + 3*m.b139*m.b148 + 4*m.b139*m.b151 + 5*m.b139*m.b154 + 6*
                       m.b139*m.b157 + 7*m.b139*m.b160 + 8*m.b139*m.b163 + 9*m.b139*m.b166 + 10*m.b139*m.b169 + 11*
                       m.b139*m.b172 + 12*m.b139*m.b175 + 13*m.b139*m.b178 + 14*m.b139*m.b181 + 15*m.b139*m.b184 + 16*
                       m.b139*m.b187 + 17*m.b139*m.b190 + 18*m.b139*m.b193 + 19*m.b139*m.b196 + 20*m.b139*m.b199 + 21*
                       m.b139*m.b202 + 22*m.b139*m.b205 + 23*m.b139*m.b208 + m.b140*m.b143 + 2*m.b140*m.b146 + 3*m.b140*
                       m.b149 + 4*m.b140*m.b152 + 5*m.b140*m.b155 + 6*m.b140*m.b158 + 7*m.b140*m.b161 + 8*m.b140*m.b164
                        + 9*m.b140*m.b167 + 10*m.b140*m.b170 + 11*m.b140*m.b173 + 12*m.b140*m.b176 + 13*m.b140*m.b179 + 
                       14*m.b140*m.b182 + 15*m.b140*m.b185 + 16*m.b140*m.b188 + 17*m.b140*m.b191 + 18*m.b140*m.b194 + 19
                       *m.b140*m.b197 + 20*m.b140*m.b200 + 21*m.b140*m.b203 + 22*m.b140*m.b206 + 23*m.b140*m.b209 + 
                       m.b141*m.b144 + 2*m.b141*m.b147 + 3*m.b141*m.b150 + 4*m.b141*m.b153 + 5*m.b141*m.b156 + 6*m.b141*
                       m.b159 + 7*m.b141*m.b162 + 8*m.b141*m.b165 + 9*m.b141*m.b168 + 10*m.b141*m.b171 + 11*m.b141*
                       m.b174 + 12*m.b141*m.b177 + 13*m.b141*m.b180 + 14*m.b141*m.b183 + 15*m.b141*m.b186 + 16*m.b141*
                       m.b189 + 17*m.b141*m.b192 + 18*m.b141*m.b195 + 19*m.b141*m.b198 + 20*m.b141*m.b201 + 21*m.b141*
                       m.b204 + 22*m.b141*m.b207 + 23*m.b141*m.b210 + m.b142*m.b145 + 2*m.b142*m.b148 + 3*m.b142*m.b151
                        + 4*m.b142*m.b154 + 5*m.b142*m.b157 + 6*m.b142*m.b160 + 7*m.b142*m.b163 + 8*m.b142*m.b166 + 9*
                       m.b142*m.b169 + 10*m.b142*m.b172 + 11*m.b142*m.b175 + 12*m.b142*m.b178 + 13*m.b142*m.b181 + 14*
                       m.b142*m.b184 + 15*m.b142*m.b187 + 16*m.b142*m.b190 + 17*m.b142*m.b193 + 18*m.b142*m.b196 + 19*
                       m.b142*m.b199 + 20*m.b142*m.b202 + 21*m.b142*m.b205 + 22*m.b142*m.b208 + m.b143*m.b146 + 2*m.b143
                       *m.b149 + 3*m.b143*m.b152 + 4*m.b143*m.b155 + 5*m.b143*m.b158 + 6*m.b143*m.b161 + 7*m.b143*m.b164
                        + 8*m.b143*m.b167 + 9*m.b143*m.b170 + 10*m.b143*m.b173 + 11*m.b143*m.b176 + 12*m.b143*m.b179 + 
                       13*m.b143*m.b182 + 14*m.b143*m.b185 + 15*m.b143*m.b188 + 16*m.b143*m.b191 + 17*m.b143*m.b194 + 18
                       *m.b143*m.b197 + 19*m.b143*m.b200 + 20*m.b143*m.b203 + 21*m.b143*m.b206 + 22*m.b143*m.b209 + 
                       m.b144*m.b147 + 2*m.b144*m.b150 + 3*m.b144*m.b153 + 4*m.b144*m.b156 + 5*m.b144*m.b159 + 6*m.b144*
                       m.b162 + 7*m.b144*m.b165 + 8*m.b144*m.b168 + 9*m.b144*m.b171 + 10*m.b144*m.b174 + 11*m.b144*
                       m.b177 + 12*m.b144*m.b180 + 13*m.b144*m.b183 + 14*m.b144*m.b186 + 15*m.b144*m.b189 + 16*m.b144*
                       m.b192 + 17*m.b144*m.b195 + 18*m.b144*m.b198 + 19*m.b144*m.b201 + 20*m.b144*m.b204 + 21*m.b144*
                       m.b207 + 22*m.b144*m.b210 + m.b145*m.b148 + 2*m.b145*m.b151 + 3*m.b145*m.b154 + 4*m.b145*m.b157
                        + 5*m.b145*m.b160 + 6*m.b145*m.b163 + 7*m.b145*m.b166 + 8*m.b145*m.b169 + 9*m.b145*m.b172 + 10*
                       m.b145*m.b175 + 11*m.b145*m.b178 + 12*m.b145*m.b181 + 13*m.b145*m.b184 + 14*m.b145*m.b187 + 15*
                       m.b145*m.b190 + 16*m.b145*m.b193 + 17*m.b145*m.b196 + 18*m.b145*m.b199 + 19*m.b145*m.b202 + 20*
                       m.b145*m.b205 + 21*m.b145*m.b208 + m.b146*m.b149 + 2*m.b146*m.b152 + 3*m.b146*m.b155 + 4*m.b146*
                       m.b158 + 5*m.b146*m.b161 + 6*m.b146*m.b164 + 7*m.b146*m.b167 + 8*m.b146*m.b170 + 9*m.b146*m.b173
                        + 10*m.b146*m.b176 + 11*m.b146*m.b179 + 12*m.b146*m.b182 + 13*m.b146*m.b185 + 14*m.b146*m.b188
                        + 15*m.b146*m.b191 + 16*m.b146*m.b194 + 17*m.b146*m.b197 + 18*m.b146*m.b200 + 19*m.b146*m.b203
                        + 20*m.b146*m.b206 + 21*m.b146*m.b209 + m.b147*m.b150 + 2*m.b147*m.b153 + 3*m.b147*m.b156 + 4*
                       m.b147*m.b159 + 5*m.b147*m.b162 + 6*m.b147*m.b165 + 7*m.b147*m.b168 + 8*m.b147*m.b171 + 9*m.b147*
                       m.b174 + 10*m.b147*m.b177 + 11*m.b147*m.b180 + 12*m.b147*m.b183 + 13*m.b147*m.b186 + 14*m.b147*
                       m.b189 + 15*m.b147*m.b192 + 16*m.b147*m.b195 + 17*m.b147*m.b198 + 18*m.b147*m.b201 + 19*m.b147*
                       m.b204 + 20*m.b147*m.b207 + 21*m.b147*m.b210 + m.b148*m.b151 + 2*m.b148*m.b154 + 3*m.b148*m.b157
                        + 4*m.b148*m.b160 + 5*m.b148*m.b163 + 6*m.b148*m.b166 + 7*m.b148*m.b169 + 8*m.b148*m.b172 + 9*
                       m.b148*m.b175 + 10*m.b148*m.b178 + 11*m.b148*m.b181 + 12*m.b148*m.b184 + 13*m.b148*m.b187 + 14*
                       m.b148*m.b190 + 15*m.b148*m.b193 + 16*m.b148*m.b196 + 17*m.b148*m.b199 + 18*m.b148*m.b202 + 19*
                       m.b148*m.b205 + 20*m.b148*m.b208 + m.b149*m.b152 + 2*m.b149*m.b155 + 3*m.b149*m.b158 + 4*m.b149*
                       m.b161 + 5*m.b149*m.b164 + 6*m.b149*m.b167 + 7*m.b149*m.b170 + 8*m.b149*m.b173 + 9*m.b149*m.b176
                        + 10*m.b149*m.b179 + 11*m.b149*m.b182 + 12*m.b149*m.b185 + 13*m.b149*m.b188 + 14*m.b149*m.b191
                        + 15*m.b149*m.b194 + 16*m.b149*m.b197 + 17*m.b149*m.b200 + 18*m.b149*m.b203 + 19*m.b149*m.b206
                        + 20*m.b149*m.b209 + m.b150*m.b153 + 2*m.b150*m.b156 + 3*m.b150*m.b159 + 4*m.b150*m.b162 + 5*
                       m.b150*m.b165 + 6*m.b150*m.b168 + 7*m.b150*m.b171 + 8*m.b150*m.b174 + 9*m.b150*m.b177 + 10*m.b150
                       *m.b180 + 11*m.b150*m.b183 + 12*m.b150*m.b186 + 13*m.b150*m.b189 + 14*m.b150*m.b192 + 15*m.b150*
                       m.b195 + 16*m.b150*m.b198 + 17*m.b150*m.b201 + 18*m.b150*m.b204 + 19*m.b150*m.b207 + 20*m.b150*
                       m.b210 + m.b151*m.b154 + 2*m.b151*m.b157 + 3*m.b151*m.b160 + 4*m.b151*m.b163 + 5*m.b151*m.b166 + 
                       6*m.b151*m.b169 + 7*m.b151*m.b172 + 8*m.b151*m.b175 + 9*m.b151*m.b178 + 10*m.b151*m.b181 + 11*
                       m.b151*m.b184 + 12*m.b151*m.b187 + 13*m.b151*m.b190 + 14*m.b151*m.b193 + 15*m.b151*m.b196 + 16*
                       m.b151*m.b199 + 17*m.b151*m.b202 + 18*m.b151*m.b205 + 19*m.b151*m.b208 + m.b152*m.b155 + 2*m.b152
                       *m.b158 + 3*m.b152*m.b161 + 4*m.b152*m.b164 + 5*m.b152*m.b167 + 6*m.b152*m.b170 + 7*m.b152*m.b173
                        + 8*m.b152*m.b176 + 9*m.b152*m.b179 + 10*m.b152*m.b182 + 11*m.b152*m.b185 + 12*m.b152*m.b188 + 
                       13*m.b152*m.b191 + 14*m.b152*m.b194 + 15*m.b152*m.b197 + 16*m.b152*m.b200 + 17*m.b152*m.b203 + 18
                       *m.b152*m.b206 + 19*m.b152*m.b209 + m.b153*m.b156 + 2*m.b153*m.b159 + 3*m.b153*m.b162 + 4*m.b153*
                       m.b165 + 5*m.b153*m.b168 + 6*m.b153*m.b171 + 7*m.b153*m.b174 + 8*m.b153*m.b177 + 9*m.b153*m.b180
                        + 10*m.b153*m.b183 + 11*m.b153*m.b186 + 12*m.b153*m.b189 + 13*m.b153*m.b192 + 14*m.b153*m.b195
                        + 15*m.b153*m.b198 + 16*m.b153*m.b201 + 17*m.b153*m.b204 + 18*m.b153*m.b207 + 19*m.b153*m.b210
                        + m.b154*m.b157 + 2*m.b154*m.b160 + 3*m.b154*m.b163 + 4*m.b154*m.b166 + 5*m.b154*m.b169 + 6*
                       m.b154*m.b172 + 7*m.b154*m.b175 + 8*m.b154*m.b178 + 9*m.b154*m.b181 + 10*m.b154*m.b184 + 11*
                       m.b154*m.b187 + 12*m.b154*m.b190 + 13*m.b154*m.b193 + 14*m.b154*m.b196 + 15*m.b154*m.b199 + 16*
                       m.b154*m.b202 + 17*m.b154*m.b205 + 18*m.b154*m.b208 + m.b155*m.b158 + 2*m.b155*m.b161 + 3*m.b155*
                       m.b164 + 4*m.b155*m.b167 + 5*m.b155*m.b170 + 6*m.b155*m.b173 + 7*m.b155*m.b176 + 8*m.b155*m.b179
                        + 9*m.b155*m.b182 + 10*m.b155*m.b185 + 11*m.b155*m.b188 + 12*m.b155*m.b191 + 13*m.b155*m.b194 + 
                       14*m.b155*m.b197 + 15*m.b155*m.b200 + 16*m.b155*m.b203 + 17*m.b155*m.b206 + 18*m.b155*m.b209 + 
                       m.b156*m.b159 + 2*m.b156*m.b162 + 3*m.b156*m.b165 + 4*m.b156*m.b168 + 5*m.b156*m.b171 + 6*m.b156*
                       m.b174 + 7*m.b156*m.b177 + 8*m.b156*m.b180 + 9*m.b156*m.b183 + 10*m.b156*m.b186 + 11*m.b156*
                       m.b189 + 12*m.b156*m.b192 + 13*m.b156*m.b195 + 14*m.b156*m.b198 + 15*m.b156*m.b201 + 16*m.b156*
                       m.b204 + 17*m.b156*m.b207 + 18*m.b156*m.b210 + m.b157*m.b160 + 2*m.b157*m.b163 + 3*m.b157*m.b166
                        + 4*m.b157*m.b169 + 5*m.b157*m.b172 + 6*m.b157*m.b175 + 7*m.b157*m.b178 + 8*m.b157*m.b181 + 9*
                       m.b157*m.b184 + 10*m.b157*m.b187 + 11*m.b157*m.b190 + 12*m.b157*m.b193 + 13*m.b157*m.b196 + 14*
                       m.b157*m.b199 + 15*m.b157*m.b202 + 16*m.b157*m.b205 + 17*m.b157*m.b208 + m.b158*m.b161 + 2*m.b158
                       *m.b164 + 3*m.b158*m.b167 + 4*m.b158*m.b170 + 5*m.b158*m.b173 + 6*m.b158*m.b176 + 7*m.b158*m.b179
                        + 8*m.b158*m.b182 + 9*m.b158*m.b185 + 10*m.b158*m.b188 + 11*m.b158*m.b191 + 12*m.b158*m.b194 + 
                       13*m.b158*m.b197 + 14*m.b158*m.b200 + 15*m.b158*m.b203 + 16*m.b158*m.b206 + 17*m.b158*m.b209 + 
                       m.b159*m.b162 + 2*m.b159*m.b165 + 3*m.b159*m.b168 + 4*m.b159*m.b171 + 5*m.b159*m.b174 + 6*m.b159*
                       m.b177 + 7*m.b159*m.b180 + 8*m.b159*m.b183 + 9*m.b159*m.b186 + 10*m.b159*m.b189 + 11*m.b159*
                       m.b192 + 12*m.b159*m.b195 + 13*m.b159*m.b198 + 14*m.b159*m.b201 + 15*m.b159*m.b204 + 16*m.b159*
                       m.b207 + 17*m.b159*m.b210 + m.b160*m.b163 + 2*m.b160*m.b166 + 3*m.b160*m.b169 + 4*m.b160*m.b172
                        + 5*m.b160*m.b175 + 6*m.b160*m.b178 + 7*m.b160*m.b181 + 8*m.b160*m.b184 + 9*m.b160*m.b187 + 10*
                       m.b160*m.b190 + 11*m.b160*m.b193 + 12*m.b160*m.b196 + 13*m.b160*m.b199 + 14*m.b160*m.b202 + 15*
                       m.b160*m.b205 + 16*m.b160*m.b208 + m.b161*m.b164 + 2*m.b161*m.b167 + 3*m.b161*m.b170 + 4*m.b161*
                       m.b173 + 5*m.b161*m.b176 + 6*m.b161*m.b179 + 7*m.b161*m.b182 + 8*m.b161*m.b185 + 9*m.b161*m.b188
                        + 10*m.b161*m.b191 + 11*m.b161*m.b194 + 12*m.b161*m.b197 + 13*m.b161*m.b200 + 14*m.b161*m.b203
                        + 15*m.b161*m.b206 + 16*m.b161*m.b209 + m.b162*m.b165 + 2*m.b162*m.b168 + 3*m.b162*m.b171 + 4*
                       m.b162*m.b174 + 5*m.b162*m.b177 + 6*m.b162*m.b180 + 7*m.b162*m.b183 + 8*m.b162*m.b186 + 9*m.b162*
                       m.b189 + 10*m.b162*m.b192 + 11*m.b162*m.b195 + 12*m.b162*m.b198 + 13*m.b162*m.b201 + 14*m.b162*
                       m.b204 + 15*m.b162*m.b207 + 16*m.b162*m.b210 + m.b163*m.b166 + 2*m.b163*m.b169 + 3*m.b163*m.b172
                        + 4*m.b163*m.b175 + 5*m.b163*m.b178 + 6*m.b163*m.b181 + 7*m.b163*m.b184 + 8*m.b163*m.b187 + 9*
                       m.b163*m.b190 + 10*m.b163*m.b193 + 11*m.b163*m.b196 + 12*m.b163*m.b199 + 13*m.b163*m.b202 + 14*
                       m.b163*m.b205 + 15*m.b163*m.b208 + m.b164*m.b167 + 2*m.b164*m.b170 + 3*m.b164*m.b173 + 4*m.b164*
                       m.b176 + 5*m.b164*m.b179 + 6*m.b164*m.b182 + 7*m.b164*m.b185 + 8*m.b164*m.b188 + 9*m.b164*m.b191
                        + 10*m.b164*m.b194 + 11*m.b164*m.b197 + 12*m.b164*m.b200 + 13*m.b164*m.b203 + 14*m.b164*m.b206
                        + 15*m.b164*m.b209 + m.b165*m.b168 + 2*m.b165*m.b171 + 3*m.b165*m.b174 + 4*m.b165*m.b177 + 5*
                       m.b165*m.b180 + 6*m.b165*m.b183 + 7*m.b165*m.b186 + 8*m.b165*m.b189 + 9*m.b165*m.b192 + 10*m.b165
                       *m.b195 + 11*m.b165*m.b198 + 12*m.b165*m.b201 + 13*m.b165*m.b204 + 14*m.b165*m.b207 + 15*m.b165*
                       m.b210 + m.b166*m.b169 + 2*m.b166*m.b172 + 3*m.b166*m.b175 + 4*m.b166*m.b178 + 5*m.b166*m.b181 + 
                       6*m.b166*m.b184 + 7*m.b166*m.b187 + 8*m.b166*m.b190 + 9*m.b166*m.b193 + 10*m.b166*m.b196 + 11*
                       m.b166*m.b199 + 12*m.b166*m.b202 + 13*m.b166*m.b205 + 14*m.b166*m.b208 + m.b167*m.b170 + 2*m.b167
                       *m.b173 + 3*m.b167*m.b176 + 4*m.b167*m.b179 + 5*m.b167*m.b182 + 6*m.b167*m.b185 + 7*m.b167*m.b188
                        + 8*m.b167*m.b191 + 9*m.b167*m.b194 + 10*m.b167*m.b197 + 11*m.b167*m.b200 + 12*m.b167*m.b203 + 
                       13*m.b167*m.b206 + 14*m.b167*m.b209 + m.b168*m.b171 + 2*m.b168*m.b174 + 3*m.b168*m.b177 + 4*
                       m.b168*m.b180 + 5*m.b168*m.b183 + 6*m.b168*m.b186 + 7*m.b168*m.b189 + 8*m.b168*m.b192 + 9*m.b168*
                       m.b195 + 10*m.b168*m.b198 + 11*m.b168*m.b201 + 12*m.b168*m.b204 + 13*m.b168*m.b207 + 14*m.b168*
                       m.b210 + m.b169*m.b172 + 2*m.b169*m.b175 + 3*m.b169*m.b178 + 4*m.b169*m.b181 + 5*m.b169*m.b184 + 
                       6*m.b169*m.b187 + 7*m.b169*m.b190 + 8*m.b169*m.b193 + 9*m.b169*m.b196 + 10*m.b169*m.b199 + 11*
                       m.b169*m.b202 + 12*m.b169*m.b205 + 13*m.b169*m.b208 + m.b170*m.b173 + 2*m.b170*m.b176 + 3*m.b170*
                       m.b179 + 4*m.b170*m.b182 + 5*m.b170*m.b185 + 6*m.b170*m.b188 + 7*m.b170*m.b191 + 8*m.b170*m.b194
                        + 9*m.b170*m.b197 + 10*m.b170*m.b200 + 11*m.b170*m.b203 + 12*m.b170*m.b206 + 13*m.b170*m.b209 + 
                       m.b171*m.b174 + 2*m.b171*m.b177 + 3*m.b171*m.b180 + 4*m.b171*m.b183 + 5*m.b171*m.b186 + 6*m.b171*
                       m.b189 + 7*m.b171*m.b192 + 8*m.b171*m.b195 + 9*m.b171*m.b198 + 10*m.b171*m.b201 + 11*m.b171*
                       m.b204 + 12*m.b171*m.b207 + 13*m.b171*m.b210 + m.b172*m.b175 + 2*m.b172*m.b178 + 3*m.b172*m.b181
                        + 4*m.b172*m.b184 + 5*m.b172*m.b187 + 6*m.b172*m.b190 + 7*m.b172*m.b193 + 8*m.b172*m.b196 + 9*
                       m.b172*m.b199 + 10*m.b172*m.b202 + 11*m.b172*m.b205 + 12*m.b172*m.b208 + m.b173*m.b176 + 2*m.b173
                       *m.b179 + 3*m.b173*m.b182 + 4*m.b173*m.b185 + 5*m.b173*m.b188 + 6*m.b173*m.b191 + 7*m.b173*m.b194
                        + 8*m.b173*m.b197 + 9*m.b173*m.b200 + 10*m.b173*m.b203 + 11*m.b173*m.b206 + 12*m.b173*m.b209 + 
                       m.b174*m.b177 + 2*m.b174*m.b180 + 3*m.b174*m.b183 + 4*m.b174*m.b186 + 5*m.b174*m.b189 + 6*m.b174*
                       m.b192 + 7*m.b174*m.b195 + 8*m.b174*m.b198 + 9*m.b174*m.b201 + 10*m.b174*m.b204 + 11*m.b174*
                       m.b207 + 12*m.b174*m.b210 + m.b175*m.b178 + 2*m.b175*m.b181 + 3*m.b175*m.b184 + 4*m.b175*m.b187
                        + 5*m.b175*m.b190 + 6*m.b175*m.b193 + 7*m.b175*m.b196 + 8*m.b175*m.b199 + 9*m.b175*m.b202 + 10*
                       m.b175*m.b205 + 11*m.b175*m.b208 + m.b176*m.b179 + 2*m.b176*m.b182 + 3*m.b176*m.b185 + 4*m.b176*
                       m.b188 + 5*m.b176*m.b191 + 6*m.b176*m.b194 + 7*m.b176*m.b197 + 8*m.b176*m.b200 + 9*m.b176*m.b203
                        + 10*m.b176*m.b206 + 11*m.b176*m.b209 + m.b177*m.b180 + 2*m.b177*m.b183 + 3*m.b177*m.b186 + 4*
                       m.b177*m.b189 + 5*m.b177*m.b192 + 6*m.b177*m.b195 + 7*m.b177*m.b198 + 8*m.b177*m.b201 + 9*m.b177*
                       m.b204 + 10*m.b177*m.b207 + 11*m.b177*m.b210 + m.b178*m.b181 + 2*m.b178*m.b184 + 3*m.b178*m.b187
                        + 4*m.b178*m.b190 + 5*m.b178*m.b193 + 6*m.b178*m.b196 + 7*m.b178*m.b199 + 8*m.b178*m.b202 + 9*
                       m.b178*m.b205 + 10*m.b178*m.b208 + m.b179*m.b182 + 2*m.b179*m.b185 + 3*m.b179*m.b188 + 4*m.b179*
                       m.b191 + 5*m.b179*m.b194 + 6*m.b179*m.b197 + 7*m.b179*m.b200 + 8*m.b179*m.b203 + 9*m.b179*m.b206
                        + 10*m.b179*m.b209 + m.b180*m.b183 + 2*m.b180*m.b186 + 3*m.b180*m.b189 + 4*m.b180*m.b192 + 5*
                       m.b180*m.b195 + 6*m.b180*m.b198 + 7*m.b180*m.b201 + 8*m.b180*m.b204 + 9*m.b180*m.b207 + 10*m.b180
                       *m.b210 + m.b181*m.b184 + 2*m.b181*m.b187 + 3*m.b181*m.b190 + 4*m.b181*m.b193 + 5*m.b181*m.b196
                        + 6*m.b181*m.b199 + 7*m.b181*m.b202 + 8*m.b181*m.b205 + 9*m.b181*m.b208 + m.b182*m.b185 + 2*
                       m.b182*m.b188 + 3*m.b182*m.b191 + 4*m.b182*m.b194 + 5*m.b182*m.b197 + 6*m.b182*m.b200 + 7*m.b182*
                       m.b203 + 8*m.b182*m.b206 + 9*m.b182*m.b209 + m.b183*m.b186 + 2*m.b183*m.b189 + 3*m.b183*m.b192 + 
                       4*m.b183*m.b195 + 5*m.b183*m.b198 + 6*m.b183*m.b201 + 7*m.b183*m.b204 + 8*m.b183*m.b207 + 9*
                       m.b183*m.b210 + m.b184*m.b187 + 2*m.b184*m.b190 + 3*m.b184*m.b193 + 4*m.b184*m.b196 + 5*m.b184*
                       m.b199 + 6*m.b184*m.b202 + 7*m.b184*m.b205 + 8*m.b184*m.b208 + m.b185*m.b188 + 2*m.b185*m.b191 + 
                       3*m.b185*m.b194 + 4*m.b185*m.b197 + 5*m.b185*m.b200 + 6*m.b185*m.b203 + 7*m.b185*m.b206 + 8*
                       m.b185*m.b209 + m.b186*m.b189 + 2*m.b186*m.b192 + 3*m.b186*m.b195 + 4*m.b186*m.b198 + 5*m.b186*
                       m.b201 + 6*m.b186*m.b204 + 7*m.b186*m.b207 + 8*m.b186*m.b210 + m.b187*m.b190 + 2*m.b187*m.b193 + 
                       3*m.b187*m.b196 + 4*m.b187*m.b199 + 5*m.b187*m.b202 + 6*m.b187*m.b205 + 7*m.b187*m.b208 + m.b188*
                       m.b191 + 2*m.b188*m.b194 + 3*m.b188*m.b197 + 4*m.b188*m.b200 + 5*m.b188*m.b203 + 6*m.b188*m.b206
                        + 7*m.b188*m.b209 + m.b189*m.b192 + 2*m.b189*m.b195 + 3*m.b189*m.b198 + 4*m.b189*m.b201 + 5*
                       m.b189*m.b204 + 6*m.b189*m.b207 + 7*m.b189*m.b210 + m.b190*m.b193 + 2*m.b190*m.b196 + 3*m.b190*
                       m.b199 + 4*m.b190*m.b202 + 5*m.b190*m.b205 + 6*m.b190*m.b208 + m.b191*m.b194 + 2*m.b191*m.b197 + 
                       3*m.b191*m.b200 + 4*m.b191*m.b203 + 5*m.b191*m.b206 + 6*m.b191*m.b209 + m.b192*m.b195 + 2*m.b192*
                       m.b198 + 3*m.b192*m.b201 + 4*m.b192*m.b204 + 5*m.b192*m.b207 + 6*m.b192*m.b210 + m.b193*m.b196 + 
                       2*m.b193*m.b199 + 3*m.b193*m.b202 + 4*m.b193*m.b205 + 5*m.b193*m.b208 + m.b194*m.b197 + 2*m.b194*
                       m.b200 + 3*m.b194*m.b203 + 4*m.b194*m.b206 + 5*m.b194*m.b209 + m.b195*m.b198 + 2*m.b195*m.b201 + 
                       3*m.b195*m.b204 + 4*m.b195*m.b207 + 5*m.b195*m.b210 + m.b196*m.b199 + 2*m.b196*m.b202 + 3*m.b196*
                       m.b205 + 4*m.b196*m.b208 + m.b197*m.b200 + 2*m.b197*m.b203 + 3*m.b197*m.b206 + 4*m.b197*m.b209 + 
                       m.b198*m.b201 + 2*m.b198*m.b204 + 3*m.b198*m.b207 + 4*m.b198*m.b210 + m.b199*m.b202 + 2*m.b199*
                       m.b205 + 3*m.b199*m.b208 + m.b200*m.b203 + 2*m.b200*m.b206 + 3*m.b200*m.b209 + m.b201*m.b204 + 2*
                       m.b201*m.b207 + 3*m.b201*m.b210 + m.b202*m.b205 + 2*m.b202*m.b208 + m.b203*m.b206 + 2*m.b203*
                       m.b209 + m.b204*m.b207 + 2*m.b204*m.b210 + m.b205*m.b208 + m.b206*m.b209 + m.b207*m.b210
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

m.c51 = Constraint(expr=   m.b151 + m.b152 + m.b153 == 1)

m.c52 = Constraint(expr=   m.b154 + m.b155 + m.b156 == 1)

m.c53 = Constraint(expr=   m.b157 + m.b158 + m.b159 == 1)

m.c54 = Constraint(expr=   m.b160 + m.b161 + m.b162 == 1)

m.c55 = Constraint(expr=   m.b163 + m.b164 + m.b165 == 1)

m.c56 = Constraint(expr=   m.b166 + m.b167 + m.b168 == 1)

m.c57 = Constraint(expr=   m.b169 + m.b170 + m.b171 == 1)

m.c58 = Constraint(expr=   m.b172 + m.b173 + m.b174 == 1)

m.c59 = Constraint(expr=   m.b175 + m.b176 + m.b177 == 1)

m.c60 = Constraint(expr=   m.b178 + m.b179 + m.b180 == 1)

m.c61 = Constraint(expr=   m.b181 + m.b182 + m.b183 == 1)

m.c62 = Constraint(expr=   m.b184 + m.b185 + m.b186 == 1)

m.c63 = Constraint(expr=   m.b187 + m.b188 + m.b189 == 1)

m.c64 = Constraint(expr=   m.b190 + m.b191 + m.b192 == 1)

m.c65 = Constraint(expr=   m.b193 + m.b194 + m.b195 == 1)

m.c66 = Constraint(expr=   m.b196 + m.b197 + m.b198 == 1)

m.c67 = Constraint(expr=   m.b199 + m.b200 + m.b201 == 1)

m.c68 = Constraint(expr=   m.b202 + m.b203 + m.b204 == 1)

m.c69 = Constraint(expr=   m.b205 + m.b206 + m.b207 == 1)

m.c70 = Constraint(expr=   m.b208 + m.b209 + m.b210 == 1)
