#  MINLP written by GAMS Convert at 04/21/18 13:52:22
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         82       82        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        244        1      243        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        487      244      243        0
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
m.b211 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b212 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b213 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b214 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b215 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b216 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b217 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b218 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b219 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b220 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b221 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b222 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b223 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b224 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b225 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b226 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b227 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b228 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b229 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b230 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b231 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b232 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b233 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b234 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b235 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b236 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b237 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b238 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b239 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b240 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b241 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b242 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b243 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=m.b1*m.b25 - m.b1*m.b4 + m.b1*m.b28 + m.b1*m.b217 - m.b2*m.b5 + m.b2*m.b26 + m.b2*m.b29 + m.b2*
                       m.b218 - m.b3*m.b6 + m.b3*m.b27 + m.b3*m.b30 + m.b3*m.b219 - m.b4*m.b7 - m.b4*m.b31 + m.b4*m.b220
                        - m.b5*m.b8 - m.b5*m.b32 + m.b5*m.b221 - m.b6*m.b9 - m.b6*m.b33 + m.b6*m.b222 - m.b7*m.b10 + 
                       m.b7*m.b34 - m.b7*m.b223 - m.b8*m.b11 + m.b8*m.b35 - m.b8*m.b224 - m.b9*m.b12 + m.b9*m.b36 - m.b9
                       *m.b225 - m.b10*m.b13 - m.b10*m.b37 + m.b10*m.b226 - m.b11*m.b14 - m.b11*m.b38 + m.b11*m.b227 - 
                       m.b12*m.b15 - m.b12*m.b39 + m.b12*m.b228 - m.b13*m.b16 - m.b13*m.b40 - m.b13*m.b229 - m.b14*m.b17
                        - m.b14*m.b41 - m.b14*m.b230 - m.b15*m.b18 - m.b15*m.b42 - m.b15*m.b231 + m.b16*m.b19 - m.b16*
                       m.b43 + m.b16*m.b232 + m.b17*m.b20 - m.b17*m.b44 + m.b17*m.b233 + m.b18*m.b21 - m.b18*m.b45 + 
                       m.b18*m.b234 - m.b19*m.b22 - m.b19*m.b46 - m.b19*m.b235 - m.b20*m.b23 - m.b20*m.b47 - m.b20*
                       m.b236 - m.b21*m.b24 - m.b21*m.b48 - m.b21*m.b237 + m.b22*m.b25 + m.b22*m.b49 + m.b22*m.b238 + 
                       m.b23*m.b26 + m.b23*m.b50 + m.b23*m.b239 + m.b24*m.b27 + m.b24*m.b51 + m.b24*m.b240 - m.b25*m.b52
                        - m.b25*m.b241 - m.b26*m.b53 - m.b26*m.b242 - m.b27*m.b54 - m.b27*m.b243 + m.b28*m.b31 + m.b28*
                       m.b52 + m.b28*m.b55 + m.b29*m.b32 + m.b29*m.b53 + m.b29*m.b56 + m.b30*m.b33 + m.b30*m.b54 + m.b30
                       *m.b57 + m.b31*m.b34 - m.b31*m.b58 + m.b32*m.b35 - m.b32*m.b59 + m.b33*m.b36 - m.b33*m.b60 + 
                       m.b34*m.b37 + m.b34*m.b61 + m.b35*m.b38 + m.b35*m.b62 + m.b36*m.b39 + m.b36*m.b63 + m.b37*m.b40
                        - m.b37*m.b64 + m.b38*m.b41 - m.b38*m.b65 + m.b39*m.b42 - m.b39*m.b66 + m.b40*m.b43 + m.b40*
                       m.b67 + m.b41*m.b44 + m.b41*m.b68 + m.b42*m.b45 + m.b42*m.b69 + m.b43*m.b46 - m.b43*m.b70 + m.b44
                       *m.b47 - m.b44*m.b71 + m.b45*m.b48 - m.b45*m.b72 - m.b46*m.b49 - m.b46*m.b73 - m.b47*m.b50 - 
                       m.b47*m.b74 - m.b48*m.b51 - m.b48*m.b75 - m.b49*m.b52 - m.b49*m.b76 - m.b50*m.b53 - m.b50*m.b77
                        - m.b51*m.b54 - m.b51*m.b78 - m.b52*m.b79 - m.b53*m.b80 - m.b54*m.b81 - m.b55*m.b58 + m.b55*
                       m.b79 - m.b55*m.b82 - m.b56*m.b59 + m.b56*m.b80 - m.b56*m.b83 - m.b57*m.b60 + m.b57*m.b81 - m.b57
                       *m.b84 + m.b58*m.b61 - m.b58*m.b85 + m.b59*m.b62 - m.b59*m.b86 + m.b60*m.b63 - m.b60*m.b87 - 
                       m.b61*m.b64 + m.b61*m.b88 - m.b62*m.b65 + m.b62*m.b89 - m.b63*m.b66 + m.b63*m.b90 - m.b64*m.b67
                        - m.b64*m.b91 - m.b65*m.b68 - m.b65*m.b92 - m.b66*m.b69 - m.b66*m.b93 + m.b67*m.b70 - m.b67*
                       m.b94 + m.b68*m.b71 - m.b68*m.b95 + m.b69*m.b72 - m.b69*m.b96 + m.b70*m.b73 - m.b70*m.b97 + m.b71
                       *m.b74 - m.b71*m.b98 + m.b72*m.b75 - m.b72*m.b99 + m.b73*m.b76 + m.b73*m.b100 + m.b74*m.b77 + 
                       m.b74*m.b101 + m.b75*m.b78 + m.b75*m.b102 + m.b76*m.b79 + m.b76*m.b103 + m.b77*m.b80 + m.b77*
                       m.b104 + m.b78*m.b81 + m.b78*m.b105 + m.b79*m.b106 + m.b80*m.b107 + m.b81*m.b108 + m.b82*m.b85 - 
                       m.b82*m.b106 + m.b82*m.b109 + m.b83*m.b86 - m.b83*m.b107 + m.b83*m.b110 + m.b84*m.b87 - m.b84*
                       m.b108 + m.b84*m.b111 - m.b85*m.b88 - m.b85*m.b112 - m.b86*m.b89 - m.b86*m.b113 - m.b87*m.b90 - 
                       m.b87*m.b114 - m.b88*m.b91 - m.b88*m.b115 - m.b89*m.b92 - m.b89*m.b116 - m.b90*m.b93 - m.b90*
                       m.b117 - m.b91*m.b94 + m.b91*m.b118 - m.b92*m.b95 + m.b92*m.b119 - m.b93*m.b96 + m.b93*m.b120 - 
                       m.b94*m.b97 + m.b94*m.b121 - m.b95*m.b98 + m.b95*m.b122 - m.b96*m.b99 + m.b96*m.b123 - m.b97*
                       m.b100 + m.b97*m.b124 - m.b98*m.b101 + m.b98*m.b125 - m.b99*m.b102 + m.b99*m.b126 + m.b100*m.b103
                        - m.b100*m.b127 + m.b101*m.b104 - m.b101*m.b128 + m.b102*m.b105 - m.b102*m.b129 + m.b103*m.b106
                        - m.b103*m.b130 + m.b104*m.b107 - m.b104*m.b131 + m.b105*m.b108 - m.b105*m.b132 + m.b106*m.b133
                        + m.b107*m.b134 + m.b108*m.b135 - m.b109*m.b112 - m.b109*m.b133 - m.b109*m.b136 - m.b110*m.b113
                        - m.b110*m.b134 - m.b110*m.b137 - m.b111*m.b114 - m.b111*m.b135 - m.b111*m.b138 + m.b112*m.b115
                        + m.b112*m.b139 + m.b113*m.b116 + m.b113*m.b140 + m.b114*m.b117 + m.b114*m.b141 - m.b115*m.b118
                        - m.b115*m.b142 - m.b116*m.b119 - m.b116*m.b143 - m.b117*m.b120 - m.b117*m.b144 + m.b118*m.b121
                        + m.b118*m.b145 + m.b119*m.b122 + m.b119*m.b146 + m.b120*m.b123 + m.b120*m.b147 - m.b121*m.b124
                        - m.b121*m.b148 - m.b122*m.b125 - m.b122*m.b149 - m.b123*m.b126 - m.b123*m.b150 - m.b124*m.b127
                        + m.b124*m.b151 - m.b125*m.b128 + m.b125*m.b152 - m.b126*m.b129 + m.b126*m.b153 - m.b127*m.b130
                        + m.b127*m.b154 - m.b128*m.b131 + m.b128*m.b155 - m.b129*m.b132 + m.b129*m.b156 + m.b130*m.b133
                        + m.b130*m.b157 + m.b131*m.b134 + m.b131*m.b158 + m.b132*m.b135 + m.b132*m.b159 + m.b133*m.b160
                        + m.b134*m.b161 + m.b135*m.b162 - m.b136*m.b139 - m.b136*m.b160 + m.b136*m.b163 - m.b137*m.b140
                        - m.b137*m.b161 + m.b137*m.b164 - m.b138*m.b141 - m.b138*m.b162 + m.b138*m.b165 - m.b139*m.b142
                        + m.b139*m.b166 - m.b140*m.b143 + m.b140*m.b167 - m.b141*m.b144 + m.b141*m.b168 - m.b142*m.b145
                        + m.b142*m.b169 - m.b143*m.b146 + m.b143*m.b170 - m.b144*m.b147 + m.b144*m.b171 - m.b145*m.b148
                        + m.b145*m.b172 - m.b146*m.b149 + m.b146*m.b173 - m.b147*m.b150 + m.b147*m.b174 - m.b148*m.b151
                        - m.b148*m.b175 - m.b149*m.b152 - m.b149*m.b176 - m.b150*m.b153 - m.b150*m.b177 + m.b151*m.b154
                        + m.b151*m.b178 + m.b152*m.b155 + m.b152*m.b179 + m.b153*m.b156 + m.b153*m.b180 - m.b154*m.b157
                        + m.b154*m.b181 - m.b155*m.b158 + m.b155*m.b182 - m.b156*m.b159 + m.b156*m.b183 + m.b157*m.b160
                        + m.b157*m.b184 + m.b158*m.b161 + m.b158*m.b185 + m.b159*m.b162 + m.b159*m.b186 + m.b160*m.b187
                        + m.b161*m.b188 + m.b162*m.b189 - m.b163*m.b166 + m.b163*m.b187 + m.b163*m.b190 - m.b164*m.b167
                        + m.b164*m.b188 + m.b164*m.b191 - m.b165*m.b168 + m.b165*m.b189 + m.b165*m.b192 + m.b166*m.b169
                        + m.b166*m.b193 + m.b167*m.b170 + m.b167*m.b194 + m.b168*m.b171 + m.b168*m.b195 - m.b169*m.b172
                        + m.b169*m.b196 - m.b170*m.b173 + m.b170*m.b197 - m.b171*m.b174 + m.b171*m.b198 + m.b172*m.b175
                        - m.b172*m.b199 + m.b173*m.b176 - m.b173*m.b200 + m.b174*m.b177 - m.b174*m.b201 - m.b175*m.b178
                        + m.b175*m.b202 - m.b176*m.b179 + m.b176*m.b203 - m.b177*m.b180 + m.b177*m.b204 - m.b178*m.b181
                        - m.b178*m.b205 - m.b179*m.b182 - m.b179*m.b206 - m.b180*m.b183 - m.b180*m.b207 + m.b181*m.b184
                        + m.b181*m.b208 + m.b182*m.b185 + m.b182*m.b209 + m.b183*m.b186 + m.b183*m.b210 + m.b184*m.b187
                        + m.b184*m.b211 + m.b185*m.b188 + m.b185*m.b212 + m.b186*m.b189 + m.b186*m.b213 - m.b187*m.b214
                        - m.b188*m.b215 - m.b189*m.b216 - m.b190*m.b193 - m.b190*m.b214 + m.b190*m.b217 - m.b191*m.b194
                        - m.b191*m.b215 + m.b191*m.b218 - m.b192*m.b195 - m.b192*m.b216 + m.b192*m.b219 - m.b193*m.b196
                        + m.b193*m.b220 - m.b194*m.b197 + m.b194*m.b221 - m.b195*m.b198 + m.b195*m.b222 + m.b196*m.b199
                        + m.b196*m.b223 + m.b197*m.b200 + m.b197*m.b224 + m.b198*m.b201 + m.b198*m.b225 + m.b199*m.b202
                        + m.b199*m.b226 + m.b200*m.b203 + m.b200*m.b227 + m.b201*m.b204 + m.b201*m.b228 - m.b202*m.b205
                        + m.b202*m.b229 - m.b203*m.b206 + m.b203*m.b230 - m.b204*m.b207 + m.b204*m.b231 + m.b205*m.b208
                        - m.b205*m.b232 + m.b206*m.b209 - m.b206*m.b233 + m.b207*m.b210 - m.b207*m.b234 - m.b208*m.b211
                        - m.b208*m.b235 - m.b209*m.b212 - m.b209*m.b236 - m.b210*m.b213 - m.b210*m.b237 - m.b211*m.b214
                        - m.b211*m.b238 - m.b212*m.b215 - m.b212*m.b239 - m.b213*m.b216 - m.b213*m.b240 + m.b214*m.b241
                        + m.b215*m.b242 + m.b216*m.b243 - m.b217*m.b220 + m.b217*m.b241 - m.b218*m.b221 + m.b218*m.b242
                        - m.b219*m.b222 + m.b219*m.b243 - m.b220*m.b223 - m.b221*m.b224 - m.b222*m.b225 + m.b223*m.b226
                        + m.b224*m.b227 + m.b225*m.b228 - m.b226*m.b229 - m.b227*m.b230 - m.b228*m.b231 + m.b229*m.b232
                        + m.b230*m.b233 + m.b231*m.b234 - m.b232*m.b235 - m.b233*m.b236 - m.b234*m.b237 - m.b235*m.b238
                        - m.b236*m.b239 - m.b237*m.b240 - m.b238*m.b241 - m.b239*m.b242 - m.b240*m.b243, sense=minimize)

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

m.c71 = Constraint(expr=   m.b211 + m.b212 + m.b213 == 1)

m.c72 = Constraint(expr=   m.b214 + m.b215 + m.b216 == 1)

m.c73 = Constraint(expr=   m.b217 + m.b218 + m.b219 == 1)

m.c74 = Constraint(expr=   m.b220 + m.b221 + m.b222 == 1)

m.c75 = Constraint(expr=   m.b223 + m.b224 + m.b225 == 1)

m.c76 = Constraint(expr=   m.b226 + m.b227 + m.b228 == 1)

m.c77 = Constraint(expr=   m.b229 + m.b230 + m.b231 == 1)

m.c78 = Constraint(expr=   m.b232 + m.b233 + m.b234 == 1)

m.c79 = Constraint(expr=   m.b235 + m.b236 + m.b237 == 1)

m.c80 = Constraint(expr=   m.b238 + m.b239 + m.b240 == 1)

m.c81 = Constraint(expr=   m.b241 + m.b242 + m.b243 == 1)
