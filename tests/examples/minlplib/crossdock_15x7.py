#  MINLP written by GAMS Convert at 04/21/18 13:51:16
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         45       31        0       14        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        211        1      210        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        631      421      210        0
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

m.obj = Objective(expr=248*m.b1*m.b113 + 279*m.b1*m.b114 + 310*m.b1*m.b115 + 341*m.b1*m.b116 + 372*m.b1*m.b117 + 403*
                       m.b1*m.b118 + 434*m.b1*m.b119 + 304*m.b1*m.b148 + 342*m.b1*m.b149 + 380*m.b1*m.b150 + 418*m.b1*
                       m.b151 + 456*m.b1*m.b152 + 494*m.b1*m.b153 + 532*m.b1*m.b154 + 312*m.b1*m.b155 + 351*m.b1*m.b156
                        + 390*m.b1*m.b157 + 429*m.b1*m.b158 + 468*m.b1*m.b159 + 507*m.b1*m.b160 + 546*m.b1*m.b161 + 176*
                       m.b1*m.b204 + 198*m.b1*m.b205 + 220*m.b1*m.b206 + 242*m.b1*m.b207 + 264*m.b1*m.b208 + 286*m.b1*
                       m.b209 + 308*m.b1*m.b210 + 279*m.b2*m.b113 + 248*m.b2*m.b114 + 279*m.b2*m.b115 + 310*m.b2*m.b116
                        + 341*m.b2*m.b117 + 372*m.b2*m.b118 + 403*m.b2*m.b119 + 342*m.b2*m.b148 + 304*m.b2*m.b149 + 342*
                       m.b2*m.b150 + 380*m.b2*m.b151 + 418*m.b2*m.b152 + 456*m.b2*m.b153 + 494*m.b2*m.b154 + 351*m.b2*
                       m.b155 + 312*m.b2*m.b156 + 351*m.b2*m.b157 + 390*m.b2*m.b158 + 429*m.b2*m.b159 + 468*m.b2*m.b160
                        + 507*m.b2*m.b161 + 198*m.b2*m.b204 + 176*m.b2*m.b205 + 198*m.b2*m.b206 + 220*m.b2*m.b207 + 242*
                       m.b2*m.b208 + 264*m.b2*m.b209 + 286*m.b2*m.b210 + 310*m.b3*m.b113 + 279*m.b3*m.b114 + 248*m.b3*
                       m.b115 + 279*m.b3*m.b116 + 310*m.b3*m.b117 + 341*m.b3*m.b118 + 372*m.b3*m.b119 + 380*m.b3*m.b148
                        + 342*m.b3*m.b149 + 304*m.b3*m.b150 + 342*m.b3*m.b151 + 380*m.b3*m.b152 + 418*m.b3*m.b153 + 456*
                       m.b3*m.b154 + 390*m.b3*m.b155 + 351*m.b3*m.b156 + 312*m.b3*m.b157 + 351*m.b3*m.b158 + 390*m.b3*
                       m.b159 + 429*m.b3*m.b160 + 468*m.b3*m.b161 + 220*m.b3*m.b204 + 198*m.b3*m.b205 + 176*m.b3*m.b206
                        + 198*m.b3*m.b207 + 220*m.b3*m.b208 + 242*m.b3*m.b209 + 264*m.b3*m.b210 + 341*m.b4*m.b113 + 310*
                       m.b4*m.b114 + 279*m.b4*m.b115 + 248*m.b4*m.b116 + 279*m.b4*m.b117 + 310*m.b4*m.b118 + 341*m.b4*
                       m.b119 + 418*m.b4*m.b148 + 380*m.b4*m.b149 + 342*m.b4*m.b150 + 304*m.b4*m.b151 + 342*m.b4*m.b152
                        + 380*m.b4*m.b153 + 418*m.b4*m.b154 + 429*m.b4*m.b155 + 390*m.b4*m.b156 + 351*m.b4*m.b157 + 312*
                       m.b4*m.b158 + 351*m.b4*m.b159 + 390*m.b4*m.b160 + 429*m.b4*m.b161 + 242*m.b4*m.b204 + 220*m.b4*
                       m.b205 + 198*m.b4*m.b206 + 176*m.b4*m.b207 + 198*m.b4*m.b208 + 220*m.b4*m.b209 + 242*m.b4*m.b210
                        + 372*m.b5*m.b113 + 341*m.b5*m.b114 + 310*m.b5*m.b115 + 279*m.b5*m.b116 + 248*m.b5*m.b117 + 279*
                       m.b5*m.b118 + 310*m.b5*m.b119 + 456*m.b5*m.b148 + 418*m.b5*m.b149 + 380*m.b5*m.b150 + 342*m.b5*
                       m.b151 + 304*m.b5*m.b152 + 342*m.b5*m.b153 + 380*m.b5*m.b154 + 468*m.b5*m.b155 + 429*m.b5*m.b156
                        + 390*m.b5*m.b157 + 351*m.b5*m.b158 + 312*m.b5*m.b159 + 351*m.b5*m.b160 + 390*m.b5*m.b161 + 264*
                       m.b5*m.b204 + 242*m.b5*m.b205 + 220*m.b5*m.b206 + 198*m.b5*m.b207 + 176*m.b5*m.b208 + 198*m.b5*
                       m.b209 + 220*m.b5*m.b210 + 403*m.b6*m.b113 + 372*m.b6*m.b114 + 341*m.b6*m.b115 + 310*m.b6*m.b116
                        + 279*m.b6*m.b117 + 248*m.b6*m.b118 + 279*m.b6*m.b119 + 494*m.b6*m.b148 + 456*m.b6*m.b149 + 418*
                       m.b6*m.b150 + 380*m.b6*m.b151 + 342*m.b6*m.b152 + 304*m.b6*m.b153 + 342*m.b6*m.b154 + 507*m.b6*
                       m.b155 + 468*m.b6*m.b156 + 429*m.b6*m.b157 + 390*m.b6*m.b158 + 351*m.b6*m.b159 + 312*m.b6*m.b160
                        + 351*m.b6*m.b161 + 286*m.b6*m.b204 + 264*m.b6*m.b205 + 242*m.b6*m.b206 + 220*m.b6*m.b207 + 198*
                       m.b6*m.b208 + 176*m.b6*m.b209 + 198*m.b6*m.b210 + 434*m.b7*m.b113 + 403*m.b7*m.b114 + 372*m.b7*
                       m.b115 + 341*m.b7*m.b116 + 310*m.b7*m.b117 + 279*m.b7*m.b118 + 248*m.b7*m.b119 + 532*m.b7*m.b148
                        + 494*m.b7*m.b149 + 456*m.b7*m.b150 + 418*m.b7*m.b151 + 380*m.b7*m.b152 + 342*m.b7*m.b153 + 304*
                       m.b7*m.b154 + 546*m.b7*m.b155 + 507*m.b7*m.b156 + 468*m.b7*m.b157 + 429*m.b7*m.b158 + 390*m.b7*
                       m.b159 + 351*m.b7*m.b160 + 312*m.b7*m.b161 + 308*m.b7*m.b204 + 286*m.b7*m.b205 + 264*m.b7*m.b206
                        + 242*m.b7*m.b207 + 220*m.b7*m.b208 + 198*m.b7*m.b209 + 176*m.b7*m.b210 + 184*m.b8*m.b120 + 207*
                       m.b8*m.b121 + 230*m.b8*m.b122 + 253*m.b8*m.b123 + 276*m.b8*m.b124 + 299*m.b8*m.b125 + 322*m.b8*
                       m.b126 + 192*m.b8*m.b162 + 216*m.b8*m.b163 + 240*m.b8*m.b164 + 264*m.b8*m.b165 + 288*m.b8*m.b166
                        + 312*m.b8*m.b167 + 336*m.b8*m.b168 + 160*m.b8*m.b197 + 180*m.b8*m.b198 + 200*m.b8*m.b199 + 220*
                       m.b8*m.b200 + 240*m.b8*m.b201 + 260*m.b8*m.b202 + 280*m.b8*m.b203 + 136*m.b8*m.b204 + 153*m.b8*
                       m.b205 + 170*m.b8*m.b206 + 187*m.b8*m.b207 + 204*m.b8*m.b208 + 221*m.b8*m.b209 + 238*m.b8*m.b210
                        + 207*m.b9*m.b120 + 184*m.b9*m.b121 + 207*m.b9*m.b122 + 230*m.b9*m.b123 + 253*m.b9*m.b124 + 276*
                       m.b9*m.b125 + 299*m.b9*m.b126 + 216*m.b9*m.b162 + 192*m.b9*m.b163 + 216*m.b9*m.b164 + 240*m.b9*
                       m.b165 + 264*m.b9*m.b166 + 288*m.b9*m.b167 + 312*m.b9*m.b168 + 180*m.b9*m.b197 + 160*m.b9*m.b198
                        + 180*m.b9*m.b199 + 200*m.b9*m.b200 + 220*m.b9*m.b201 + 240*m.b9*m.b202 + 260*m.b9*m.b203 + 153*
                       m.b9*m.b204 + 136*m.b9*m.b205 + 153*m.b9*m.b206 + 170*m.b9*m.b207 + 187*m.b9*m.b208 + 204*m.b9*
                       m.b209 + 221*m.b9*m.b210 + 230*m.b10*m.b120 + 207*m.b10*m.b121 + 184*m.b10*m.b122 + 207*m.b10*
                       m.b123 + 230*m.b10*m.b124 + 253*m.b10*m.b125 + 276*m.b10*m.b126 + 240*m.b10*m.b162 + 216*m.b10*
                       m.b163 + 192*m.b10*m.b164 + 216*m.b10*m.b165 + 240*m.b10*m.b166 + 264*m.b10*m.b167 + 288*m.b10*
                       m.b168 + 200*m.b10*m.b197 + 180*m.b10*m.b198 + 160*m.b10*m.b199 + 180*m.b10*m.b200 + 200*m.b10*
                       m.b201 + 220*m.b10*m.b202 + 240*m.b10*m.b203 + 170*m.b10*m.b204 + 153*m.b10*m.b205 + 136*m.b10*
                       m.b206 + 153*m.b10*m.b207 + 170*m.b10*m.b208 + 187*m.b10*m.b209 + 204*m.b10*m.b210 + 253*m.b11*
                       m.b120 + 230*m.b11*m.b121 + 207*m.b11*m.b122 + 184*m.b11*m.b123 + 207*m.b11*m.b124 + 230*m.b11*
                       m.b125 + 253*m.b11*m.b126 + 264*m.b11*m.b162 + 240*m.b11*m.b163 + 216*m.b11*m.b164 + 192*m.b11*
                       m.b165 + 216*m.b11*m.b166 + 240*m.b11*m.b167 + 264*m.b11*m.b168 + 220*m.b11*m.b197 + 200*m.b11*
                       m.b198 + 180*m.b11*m.b199 + 160*m.b11*m.b200 + 180*m.b11*m.b201 + 200*m.b11*m.b202 + 220*m.b11*
                       m.b203 + 187*m.b11*m.b204 + 170*m.b11*m.b205 + 153*m.b11*m.b206 + 136*m.b11*m.b207 + 153*m.b11*
                       m.b208 + 170*m.b11*m.b209 + 187*m.b11*m.b210 + 276*m.b12*m.b120 + 253*m.b12*m.b121 + 230*m.b12*
                       m.b122 + 207*m.b12*m.b123 + 184*m.b12*m.b124 + 207*m.b12*m.b125 + 230*m.b12*m.b126 + 288*m.b12*
                       m.b162 + 264*m.b12*m.b163 + 240*m.b12*m.b164 + 216*m.b12*m.b165 + 192*m.b12*m.b166 + 216*m.b12*
                       m.b167 + 240*m.b12*m.b168 + 240*m.b12*m.b197 + 220*m.b12*m.b198 + 200*m.b12*m.b199 + 180*m.b12*
                       m.b200 + 160*m.b12*m.b201 + 180*m.b12*m.b202 + 200*m.b12*m.b203 + 204*m.b12*m.b204 + 187*m.b12*
                       m.b205 + 170*m.b12*m.b206 + 153*m.b12*m.b207 + 136*m.b12*m.b208 + 153*m.b12*m.b209 + 170*m.b12*
                       m.b210 + 299*m.b13*m.b120 + 276*m.b13*m.b121 + 253*m.b13*m.b122 + 230*m.b13*m.b123 + 207*m.b13*
                       m.b124 + 184*m.b13*m.b125 + 207*m.b13*m.b126 + 312*m.b13*m.b162 + 288*m.b13*m.b163 + 264*m.b13*
                       m.b164 + 240*m.b13*m.b165 + 216*m.b13*m.b166 + 192*m.b13*m.b167 + 216*m.b13*m.b168 + 260*m.b13*
                       m.b197 + 240*m.b13*m.b198 + 220*m.b13*m.b199 + 200*m.b13*m.b200 + 180*m.b13*m.b201 + 160*m.b13*
                       m.b202 + 180*m.b13*m.b203 + 221*m.b13*m.b204 + 204*m.b13*m.b205 + 187*m.b13*m.b206 + 170*m.b13*
                       m.b207 + 153*m.b13*m.b208 + 136*m.b13*m.b209 + 153*m.b13*m.b210 + 322*m.b14*m.b120 + 299*m.b14*
                       m.b121 + 276*m.b14*m.b122 + 253*m.b14*m.b123 + 230*m.b14*m.b124 + 207*m.b14*m.b125 + 184*m.b14*
                       m.b126 + 336*m.b14*m.b162 + 312*m.b14*m.b163 + 288*m.b14*m.b164 + 264*m.b14*m.b165 + 240*m.b14*
                       m.b166 + 216*m.b14*m.b167 + 192*m.b14*m.b168 + 280*m.b14*m.b197 + 260*m.b14*m.b198 + 240*m.b14*
                       m.b199 + 220*m.b14*m.b200 + 200*m.b14*m.b201 + 180*m.b14*m.b202 + 160*m.b14*m.b203 + 238*m.b14*
                       m.b204 + 221*m.b14*m.b205 + 204*m.b14*m.b206 + 187*m.b14*m.b207 + 170*m.b14*m.b208 + 153*m.b14*
                       m.b209 + 136*m.b14*m.b210 + 120*m.b15*m.b127 + 135*m.b15*m.b128 + 150*m.b15*m.b129 + 165*m.b15*
                       m.b130 + 180*m.b15*m.b131 + 195*m.b15*m.b132 + 210*m.b15*m.b133 + 144*m.b15*m.b148 + 162*m.b15*
                       m.b149 + 180*m.b15*m.b150 + 198*m.b15*m.b151 + 216*m.b15*m.b152 + 234*m.b15*m.b153 + 252*m.b15*
                       m.b154 + 240*m.b15*m.b155 + 270*m.b15*m.b156 + 300*m.b15*m.b157 + 330*m.b15*m.b158 + 360*m.b15*
                       m.b159 + 390*m.b15*m.b160 + 420*m.b15*m.b161 + 135*m.b16*m.b127 + 120*m.b16*m.b128 + 135*m.b16*
                       m.b129 + 150*m.b16*m.b130 + 165*m.b16*m.b131 + 180*m.b16*m.b132 + 195*m.b16*m.b133 + 162*m.b16*
                       m.b148 + 144*m.b16*m.b149 + 162*m.b16*m.b150 + 180*m.b16*m.b151 + 198*m.b16*m.b152 + 216*m.b16*
                       m.b153 + 234*m.b16*m.b154 + 270*m.b16*m.b155 + 240*m.b16*m.b156 + 270*m.b16*m.b157 + 300*m.b16*
                       m.b158 + 330*m.b16*m.b159 + 360*m.b16*m.b160 + 390*m.b16*m.b161 + 150*m.b17*m.b127 + 135*m.b17*
                       m.b128 + 120*m.b17*m.b129 + 135*m.b17*m.b130 + 150*m.b17*m.b131 + 165*m.b17*m.b132 + 180*m.b17*
                       m.b133 + 180*m.b17*m.b148 + 162*m.b17*m.b149 + 144*m.b17*m.b150 + 162*m.b17*m.b151 + 180*m.b17*
                       m.b152 + 198*m.b17*m.b153 + 216*m.b17*m.b154 + 300*m.b17*m.b155 + 270*m.b17*m.b156 + 240*m.b17*
                       m.b157 + 270*m.b17*m.b158 + 300*m.b17*m.b159 + 330*m.b17*m.b160 + 360*m.b17*m.b161 + 165*m.b18*
                       m.b127 + 150*m.b18*m.b128 + 135*m.b18*m.b129 + 120*m.b18*m.b130 + 135*m.b18*m.b131 + 150*m.b18*
                       m.b132 + 165*m.b18*m.b133 + 198*m.b18*m.b148 + 180*m.b18*m.b149 + 162*m.b18*m.b150 + 144*m.b18*
                       m.b151 + 162*m.b18*m.b152 + 180*m.b18*m.b153 + 198*m.b18*m.b154 + 330*m.b18*m.b155 + 300*m.b18*
                       m.b156 + 270*m.b18*m.b157 + 240*m.b18*m.b158 + 270*m.b18*m.b159 + 300*m.b18*m.b160 + 330*m.b18*
                       m.b161 + 180*m.b19*m.b127 + 165*m.b19*m.b128 + 150*m.b19*m.b129 + 135*m.b19*m.b130 + 120*m.b19*
                       m.b131 + 135*m.b19*m.b132 + 150*m.b19*m.b133 + 216*m.b19*m.b148 + 198*m.b19*m.b149 + 180*m.b19*
                       m.b150 + 162*m.b19*m.b151 + 144*m.b19*m.b152 + 162*m.b19*m.b153 + 180*m.b19*m.b154 + 360*m.b19*
                       m.b155 + 330*m.b19*m.b156 + 300*m.b19*m.b157 + 270*m.b19*m.b158 + 240*m.b19*m.b159 + 270*m.b19*
                       m.b160 + 300*m.b19*m.b161 + 195*m.b20*m.b127 + 180*m.b20*m.b128 + 165*m.b20*m.b129 + 150*m.b20*
                       m.b130 + 135*m.b20*m.b131 + 120*m.b20*m.b132 + 135*m.b20*m.b133 + 234*m.b20*m.b148 + 216*m.b20*
                       m.b149 + 198*m.b20*m.b150 + 180*m.b20*m.b151 + 162*m.b20*m.b152 + 144*m.b20*m.b153 + 162*m.b20*
                       m.b154 + 390*m.b20*m.b155 + 360*m.b20*m.b156 + 330*m.b20*m.b157 + 300*m.b20*m.b158 + 270*m.b20*
                       m.b159 + 240*m.b20*m.b160 + 270*m.b20*m.b161 + 210*m.b21*m.b127 + 195*m.b21*m.b128 + 180*m.b21*
                       m.b129 + 165*m.b21*m.b130 + 150*m.b21*m.b131 + 135*m.b21*m.b132 + 120*m.b21*m.b133 + 252*m.b21*
                       m.b148 + 234*m.b21*m.b149 + 216*m.b21*m.b150 + 198*m.b21*m.b151 + 180*m.b21*m.b152 + 162*m.b21*
                       m.b153 + 144*m.b21*m.b154 + 420*m.b21*m.b155 + 390*m.b21*m.b156 + 360*m.b21*m.b157 + 330*m.b21*
                       m.b158 + 300*m.b21*m.b159 + 270*m.b21*m.b160 + 240*m.b21*m.b161 + 344*m.b22*m.b106 + 387*m.b22*
                       m.b107 + 430*m.b22*m.b108 + 473*m.b22*m.b109 + 516*m.b22*m.b110 + 559*m.b22*m.b111 + 602*m.b22*
                       m.b112 + 320*m.b22*m.b113 + 360*m.b22*m.b114 + 400*m.b22*m.b115 + 440*m.b22*m.b116 + 480*m.b22*
                       m.b117 + 520*m.b22*m.b118 + 560*m.b22*m.b119 + 224*m.b22*m.b141 + 252*m.b22*m.b142 + 280*m.b22*
                       m.b143 + 308*m.b22*m.b144 + 336*m.b22*m.b145 + 364*m.b22*m.b146 + 392*m.b22*m.b147 + 120*m.b22*
                       m.b148 + 135*m.b22*m.b149 + 150*m.b22*m.b150 + 165*m.b22*m.b151 + 180*m.b22*m.b152 + 195*m.b22*
                       m.b153 + 210*m.b22*m.b154 + 208*m.b22*m.b162 + 234*m.b22*m.b163 + 260*m.b22*m.b164 + 286*m.b22*
                       m.b165 + 312*m.b22*m.b166 + 338*m.b22*m.b167 + 364*m.b22*m.b168 + 248*m.b22*m.b176 + 279*m.b22*
                       m.b177 + 310*m.b22*m.b178 + 341*m.b22*m.b179 + 372*m.b22*m.b180 + 403*m.b22*m.b181 + 434*m.b22*
                       m.b182 + 400*m.b22*m.b204 + 450*m.b22*m.b205 + 500*m.b22*m.b206 + 550*m.b22*m.b207 + 600*m.b22*
                       m.b208 + 650*m.b22*m.b209 + 700*m.b22*m.b210 + 387*m.b23*m.b106 + 344*m.b23*m.b107 + 387*m.b23*
                       m.b108 + 430*m.b23*m.b109 + 473*m.b23*m.b110 + 516*m.b23*m.b111 + 559*m.b23*m.b112 + 360*m.b23*
                       m.b113 + 320*m.b23*m.b114 + 360*m.b23*m.b115 + 400*m.b23*m.b116 + 440*m.b23*m.b117 + 480*m.b23*
                       m.b118 + 520*m.b23*m.b119 + 252*m.b23*m.b141 + 224*m.b23*m.b142 + 252*m.b23*m.b143 + 280*m.b23*
                       m.b144 + 308*m.b23*m.b145 + 336*m.b23*m.b146 + 364*m.b23*m.b147 + 135*m.b23*m.b148 + 120*m.b23*
                       m.b149 + 135*m.b23*m.b150 + 150*m.b23*m.b151 + 165*m.b23*m.b152 + 180*m.b23*m.b153 + 195*m.b23*
                       m.b154 + 234*m.b23*m.b162 + 208*m.b23*m.b163 + 234*m.b23*m.b164 + 260*m.b23*m.b165 + 286*m.b23*
                       m.b166 + 312*m.b23*m.b167 + 338*m.b23*m.b168 + 279*m.b23*m.b176 + 248*m.b23*m.b177 + 279*m.b23*
                       m.b178 + 310*m.b23*m.b179 + 341*m.b23*m.b180 + 372*m.b23*m.b181 + 403*m.b23*m.b182 + 450*m.b23*
                       m.b204 + 400*m.b23*m.b205 + 450*m.b23*m.b206 + 500*m.b23*m.b207 + 550*m.b23*m.b208 + 600*m.b23*
                       m.b209 + 650*m.b23*m.b210 + 430*m.b24*m.b106 + 387*m.b24*m.b107 + 344*m.b24*m.b108 + 387*m.b24*
                       m.b109 + 430*m.b24*m.b110 + 473*m.b24*m.b111 + 516*m.b24*m.b112 + 400*m.b24*m.b113 + 360*m.b24*
                       m.b114 + 320*m.b24*m.b115 + 360*m.b24*m.b116 + 400*m.b24*m.b117 + 440*m.b24*m.b118 + 480*m.b24*
                       m.b119 + 280*m.b24*m.b141 + 252*m.b24*m.b142 + 224*m.b24*m.b143 + 252*m.b24*m.b144 + 280*m.b24*
                       m.b145 + 308*m.b24*m.b146 + 336*m.b24*m.b147 + 150*m.b24*m.b148 + 135*m.b24*m.b149 + 120*m.b24*
                       m.b150 + 135*m.b24*m.b151 + 150*m.b24*m.b152 + 165*m.b24*m.b153 + 180*m.b24*m.b154 + 260*m.b24*
                       m.b162 + 234*m.b24*m.b163 + 208*m.b24*m.b164 + 234*m.b24*m.b165 + 260*m.b24*m.b166 + 286*m.b24*
                       m.b167 + 312*m.b24*m.b168 + 310*m.b24*m.b176 + 279*m.b24*m.b177 + 248*m.b24*m.b178 + 279*m.b24*
                       m.b179 + 310*m.b24*m.b180 + 341*m.b24*m.b181 + 372*m.b24*m.b182 + 500*m.b24*m.b204 + 450*m.b24*
                       m.b205 + 400*m.b24*m.b206 + 450*m.b24*m.b207 + 500*m.b24*m.b208 + 550*m.b24*m.b209 + 600*m.b24*
                       m.b210 + 473*m.b25*m.b106 + 430*m.b25*m.b107 + 387*m.b25*m.b108 + 344*m.b25*m.b109 + 387*m.b25*
                       m.b110 + 430*m.b25*m.b111 + 473*m.b25*m.b112 + 440*m.b25*m.b113 + 400*m.b25*m.b114 + 360*m.b25*
                       m.b115 + 320*m.b25*m.b116 + 360*m.b25*m.b117 + 400*m.b25*m.b118 + 440*m.b25*m.b119 + 308*m.b25*
                       m.b141 + 280*m.b25*m.b142 + 252*m.b25*m.b143 + 224*m.b25*m.b144 + 252*m.b25*m.b145 + 280*m.b25*
                       m.b146 + 308*m.b25*m.b147 + 165*m.b25*m.b148 + 150*m.b25*m.b149 + 135*m.b25*m.b150 + 120*m.b25*
                       m.b151 + 135*m.b25*m.b152 + 150*m.b25*m.b153 + 165*m.b25*m.b154 + 286*m.b25*m.b162 + 260*m.b25*
                       m.b163 + 234*m.b25*m.b164 + 208*m.b25*m.b165 + 234*m.b25*m.b166 + 260*m.b25*m.b167 + 286*m.b25*
                       m.b168 + 341*m.b25*m.b176 + 310*m.b25*m.b177 + 279*m.b25*m.b178 + 248*m.b25*m.b179 + 279*m.b25*
                       m.b180 + 310*m.b25*m.b181 + 341*m.b25*m.b182 + 550*m.b25*m.b204 + 500*m.b25*m.b205 + 450*m.b25*
                       m.b206 + 400*m.b25*m.b207 + 450*m.b25*m.b208 + 500*m.b25*m.b209 + 550*m.b25*m.b210 + 516*m.b26*
                       m.b106 + 473*m.b26*m.b107 + 430*m.b26*m.b108 + 387*m.b26*m.b109 + 344*m.b26*m.b110 + 387*m.b26*
                       m.b111 + 430*m.b26*m.b112 + 480*m.b26*m.b113 + 440*m.b26*m.b114 + 400*m.b26*m.b115 + 360*m.b26*
                       m.b116 + 320*m.b26*m.b117 + 360*m.b26*m.b118 + 400*m.b26*m.b119 + 336*m.b26*m.b141 + 308*m.b26*
                       m.b142 + 280*m.b26*m.b143 + 252*m.b26*m.b144 + 224*m.b26*m.b145 + 252*m.b26*m.b146 + 280*m.b26*
                       m.b147 + 180*m.b26*m.b148 + 165*m.b26*m.b149 + 150*m.b26*m.b150 + 135*m.b26*m.b151 + 120*m.b26*
                       m.b152 + 135*m.b26*m.b153 + 150*m.b26*m.b154 + 312*m.b26*m.b162 + 286*m.b26*m.b163 + 260*m.b26*
                       m.b164 + 234*m.b26*m.b165 + 208*m.b26*m.b166 + 234*m.b26*m.b167 + 260*m.b26*m.b168 + 372*m.b26*
                       m.b176 + 341*m.b26*m.b177 + 310*m.b26*m.b178 + 279*m.b26*m.b179 + 248*m.b26*m.b180 + 279*m.b26*
                       m.b181 + 310*m.b26*m.b182 + 600*m.b26*m.b204 + 550*m.b26*m.b205 + 500*m.b26*m.b206 + 450*m.b26*
                       m.b207 + 400*m.b26*m.b208 + 450*m.b26*m.b209 + 500*m.b26*m.b210 + 559*m.b27*m.b106 + 516*m.b27*
                       m.b107 + 473*m.b27*m.b108 + 430*m.b27*m.b109 + 387*m.b27*m.b110 + 344*m.b27*m.b111 + 387*m.b27*
                       m.b112 + 520*m.b27*m.b113 + 480*m.b27*m.b114 + 440*m.b27*m.b115 + 400*m.b27*m.b116 + 360*m.b27*
                       m.b117 + 320*m.b27*m.b118 + 360*m.b27*m.b119 + 364*m.b27*m.b141 + 336*m.b27*m.b142 + 308*m.b27*
                       m.b143 + 280*m.b27*m.b144 + 252*m.b27*m.b145 + 224*m.b27*m.b146 + 252*m.b27*m.b147 + 195*m.b27*
                       m.b148 + 180*m.b27*m.b149 + 165*m.b27*m.b150 + 150*m.b27*m.b151 + 135*m.b27*m.b152 + 120*m.b27*
                       m.b153 + 135*m.b27*m.b154 + 338*m.b27*m.b162 + 312*m.b27*m.b163 + 286*m.b27*m.b164 + 260*m.b27*
                       m.b165 + 234*m.b27*m.b166 + 208*m.b27*m.b167 + 234*m.b27*m.b168 + 403*m.b27*m.b176 + 372*m.b27*
                       m.b177 + 341*m.b27*m.b178 + 310*m.b27*m.b179 + 279*m.b27*m.b180 + 248*m.b27*m.b181 + 279*m.b27*
                       m.b182 + 650*m.b27*m.b204 + 600*m.b27*m.b205 + 550*m.b27*m.b206 + 500*m.b27*m.b207 + 450*m.b27*
                       m.b208 + 400*m.b27*m.b209 + 450*m.b27*m.b210 + 602*m.b28*m.b106 + 559*m.b28*m.b107 + 516*m.b28*
                       m.b108 + 473*m.b28*m.b109 + 430*m.b28*m.b110 + 387*m.b28*m.b111 + 344*m.b28*m.b112 + 560*m.b28*
                       m.b113 + 520*m.b28*m.b114 + 480*m.b28*m.b115 + 440*m.b28*m.b116 + 400*m.b28*m.b117 + 360*m.b28*
                       m.b118 + 320*m.b28*m.b119 + 392*m.b28*m.b141 + 364*m.b28*m.b142 + 336*m.b28*m.b143 + 308*m.b28*
                       m.b144 + 280*m.b28*m.b145 + 252*m.b28*m.b146 + 224*m.b28*m.b147 + 210*m.b28*m.b148 + 195*m.b28*
                       m.b149 + 180*m.b28*m.b150 + 165*m.b28*m.b151 + 150*m.b28*m.b152 + 135*m.b28*m.b153 + 120*m.b28*
                       m.b154 + 364*m.b28*m.b162 + 338*m.b28*m.b163 + 312*m.b28*m.b164 + 286*m.b28*m.b165 + 260*m.b28*
                       m.b166 + 234*m.b28*m.b167 + 208*m.b28*m.b168 + 434*m.b28*m.b176 + 403*m.b28*m.b177 + 372*m.b28*
                       m.b178 + 341*m.b28*m.b179 + 310*m.b28*m.b180 + 279*m.b28*m.b181 + 248*m.b28*m.b182 + 700*m.b28*
                       m.b204 + 650*m.b28*m.b205 + 600*m.b28*m.b206 + 550*m.b28*m.b207 + 500*m.b28*m.b208 + 450*m.b28*
                       m.b209 + 400*m.b28*m.b210 + 168*m.b29*m.b120 + 189*m.b29*m.b121 + 210*m.b29*m.b122 + 231*m.b29*
                       m.b123 + 252*m.b29*m.b124 + 273*m.b29*m.b125 + 294*m.b29*m.b126 + 160*m.b29*m.b148 + 180*m.b29*
                       m.b149 + 200*m.b29*m.b150 + 220*m.b29*m.b151 + 240*m.b29*m.b152 + 260*m.b29*m.b153 + 280*m.b29*
                       m.b154 + 96*m.b29*m.b155 + 108*m.b29*m.b156 + 120*m.b29*m.b157 + 132*m.b29*m.b158 + 144*m.b29*
                       m.b159 + 156*m.b29*m.b160 + 168*m.b29*m.b161 + 304*m.b29*m.b162 + 342*m.b29*m.b163 + 380*m.b29*
                       m.b164 + 418*m.b29*m.b165 + 456*m.b29*m.b166 + 494*m.b29*m.b167 + 532*m.b29*m.b168 + 96*m.b29*
                       m.b176 + 108*m.b29*m.b177 + 120*m.b29*m.b178 + 132*m.b29*m.b179 + 144*m.b29*m.b180 + 156*m.b29*
                       m.b181 + 168*m.b29*m.b182 + 189*m.b30*m.b120 + 168*m.b30*m.b121 + 189*m.b30*m.b122 + 210*m.b30*
                       m.b123 + 231*m.b30*m.b124 + 252*m.b30*m.b125 + 273*m.b30*m.b126 + 180*m.b30*m.b148 + 160*m.b30*
                       m.b149 + 180*m.b30*m.b150 + 200*m.b30*m.b151 + 220*m.b30*m.b152 + 240*m.b30*m.b153 + 260*m.b30*
                       m.b154 + 108*m.b30*m.b155 + 96*m.b30*m.b156 + 108*m.b30*m.b157 + 120*m.b30*m.b158 + 132*m.b30*
                       m.b159 + 144*m.b30*m.b160 + 156*m.b30*m.b161 + 342*m.b30*m.b162 + 304*m.b30*m.b163 + 342*m.b30*
                       m.b164 + 380*m.b30*m.b165 + 418*m.b30*m.b166 + 456*m.b30*m.b167 + 494*m.b30*m.b168 + 108*m.b30*
                       m.b176 + 96*m.b30*m.b177 + 108*m.b30*m.b178 + 120*m.b30*m.b179 + 132*m.b30*m.b180 + 144*m.b30*
                       m.b181 + 156*m.b30*m.b182 + 210*m.b31*m.b120 + 189*m.b31*m.b121 + 168*m.b31*m.b122 + 189*m.b31*
                       m.b123 + 210*m.b31*m.b124 + 231*m.b31*m.b125 + 252*m.b31*m.b126 + 200*m.b31*m.b148 + 180*m.b31*
                       m.b149 + 160*m.b31*m.b150 + 180*m.b31*m.b151 + 200*m.b31*m.b152 + 220*m.b31*m.b153 + 240*m.b31*
                       m.b154 + 120*m.b31*m.b155 + 108*m.b31*m.b156 + 96*m.b31*m.b157 + 108*m.b31*m.b158 + 120*m.b31*
                       m.b159 + 132*m.b31*m.b160 + 144*m.b31*m.b161 + 380*m.b31*m.b162 + 342*m.b31*m.b163 + 304*m.b31*
                       m.b164 + 342*m.b31*m.b165 + 380*m.b31*m.b166 + 418*m.b31*m.b167 + 456*m.b31*m.b168 + 120*m.b31*
                       m.b176 + 108*m.b31*m.b177 + 96*m.b31*m.b178 + 108*m.b31*m.b179 + 120*m.b31*m.b180 + 132*m.b31*
                       m.b181 + 144*m.b31*m.b182 + 231*m.b32*m.b120 + 210*m.b32*m.b121 + 189*m.b32*m.b122 + 168*m.b32*
                       m.b123 + 189*m.b32*m.b124 + 210*m.b32*m.b125 + 231*m.b32*m.b126 + 220*m.b32*m.b148 + 200*m.b32*
                       m.b149 + 180*m.b32*m.b150 + 160*m.b32*m.b151 + 180*m.b32*m.b152 + 200*m.b32*m.b153 + 220*m.b32*
                       m.b154 + 132*m.b32*m.b155 + 120*m.b32*m.b156 + 108*m.b32*m.b157 + 96*m.b32*m.b158 + 108*m.b32*
                       m.b159 + 120*m.b32*m.b160 + 132*m.b32*m.b161 + 418*m.b32*m.b162 + 380*m.b32*m.b163 + 342*m.b32*
                       m.b164 + 304*m.b32*m.b165 + 342*m.b32*m.b166 + 380*m.b32*m.b167 + 418*m.b32*m.b168 + 132*m.b32*
                       m.b176 + 120*m.b32*m.b177 + 108*m.b32*m.b178 + 96*m.b32*m.b179 + 108*m.b32*m.b180 + 120*m.b32*
                       m.b181 + 132*m.b32*m.b182 + 252*m.b33*m.b120 + 231*m.b33*m.b121 + 210*m.b33*m.b122 + 189*m.b33*
                       m.b123 + 168*m.b33*m.b124 + 189*m.b33*m.b125 + 210*m.b33*m.b126 + 240*m.b33*m.b148 + 220*m.b33*
                       m.b149 + 200*m.b33*m.b150 + 180*m.b33*m.b151 + 160*m.b33*m.b152 + 180*m.b33*m.b153 + 200*m.b33*
                       m.b154 + 144*m.b33*m.b155 + 132*m.b33*m.b156 + 120*m.b33*m.b157 + 108*m.b33*m.b158 + 96*m.b33*
                       m.b159 + 108*m.b33*m.b160 + 120*m.b33*m.b161 + 456*m.b33*m.b162 + 418*m.b33*m.b163 + 380*m.b33*
                       m.b164 + 342*m.b33*m.b165 + 304*m.b33*m.b166 + 342*m.b33*m.b167 + 380*m.b33*m.b168 + 144*m.b33*
                       m.b176 + 132*m.b33*m.b177 + 120*m.b33*m.b178 + 108*m.b33*m.b179 + 96*m.b33*m.b180 + 108*m.b33*
                       m.b181 + 120*m.b33*m.b182 + 273*m.b34*m.b120 + 252*m.b34*m.b121 + 231*m.b34*m.b122 + 210*m.b34*
                       m.b123 + 189*m.b34*m.b124 + 168*m.b34*m.b125 + 189*m.b34*m.b126 + 260*m.b34*m.b148 + 240*m.b34*
                       m.b149 + 220*m.b34*m.b150 + 200*m.b34*m.b151 + 180*m.b34*m.b152 + 160*m.b34*m.b153 + 180*m.b34*
                       m.b154 + 156*m.b34*m.b155 + 144*m.b34*m.b156 + 132*m.b34*m.b157 + 120*m.b34*m.b158 + 108*m.b34*
                       m.b159 + 96*m.b34*m.b160 + 108*m.b34*m.b161 + 494*m.b34*m.b162 + 456*m.b34*m.b163 + 418*m.b34*
                       m.b164 + 380*m.b34*m.b165 + 342*m.b34*m.b166 + 304*m.b34*m.b167 + 342*m.b34*m.b168 + 156*m.b34*
                       m.b176 + 144*m.b34*m.b177 + 132*m.b34*m.b178 + 120*m.b34*m.b179 + 108*m.b34*m.b180 + 96*m.b34*
                       m.b181 + 108*m.b34*m.b182 + 294*m.b35*m.b120 + 273*m.b35*m.b121 + 252*m.b35*m.b122 + 231*m.b35*
                       m.b123 + 210*m.b35*m.b124 + 189*m.b35*m.b125 + 168*m.b35*m.b126 + 280*m.b35*m.b148 + 260*m.b35*
                       m.b149 + 240*m.b35*m.b150 + 220*m.b35*m.b151 + 200*m.b35*m.b152 + 180*m.b35*m.b153 + 160*m.b35*
                       m.b154 + 168*m.b35*m.b155 + 156*m.b35*m.b156 + 144*m.b35*m.b157 + 132*m.b35*m.b158 + 120*m.b35*
                       m.b159 + 108*m.b35*m.b160 + 96*m.b35*m.b161 + 532*m.b35*m.b162 + 494*m.b35*m.b163 + 456*m.b35*
                       m.b164 + 418*m.b35*m.b165 + 380*m.b35*m.b166 + 342*m.b35*m.b167 + 304*m.b35*m.b168 + 168*m.b35*
                       m.b176 + 156*m.b35*m.b177 + 144*m.b35*m.b178 + 132*m.b35*m.b179 + 120*m.b35*m.b180 + 108*m.b35*
                       m.b181 + 96*m.b35*m.b182 + 368*m.b36*m.b113 + 414*m.b36*m.b114 + 460*m.b36*m.b115 + 506*m.b36*
                       m.b116 + 552*m.b36*m.b117 + 598*m.b36*m.b118 + 644*m.b36*m.b119 + 304*m.b36*m.b169 + 342*m.b36*
                       m.b170 + 380*m.b36*m.b171 + 418*m.b36*m.b172 + 456*m.b36*m.b173 + 494*m.b36*m.b174 + 532*m.b36*
                       m.b175 + 272*m.b36*m.b204 + 306*m.b36*m.b205 + 340*m.b36*m.b206 + 374*m.b36*m.b207 + 408*m.b36*
                       m.b208 + 442*m.b36*m.b209 + 476*m.b36*m.b210 + 414*m.b37*m.b113 + 368*m.b37*m.b114 + 414*m.b37*
                       m.b115 + 460*m.b37*m.b116 + 506*m.b37*m.b117 + 552*m.b37*m.b118 + 598*m.b37*m.b119 + 342*m.b37*
                       m.b169 + 304*m.b37*m.b170 + 342*m.b37*m.b171 + 380*m.b37*m.b172 + 418*m.b37*m.b173 + 456*m.b37*
                       m.b174 + 494*m.b37*m.b175 + 306*m.b37*m.b204 + 272*m.b37*m.b205 + 306*m.b37*m.b206 + 340*m.b37*
                       m.b207 + 374*m.b37*m.b208 + 408*m.b37*m.b209 + 442*m.b37*m.b210 + 460*m.b38*m.b113 + 414*m.b38*
                       m.b114 + 368*m.b38*m.b115 + 414*m.b38*m.b116 + 460*m.b38*m.b117 + 506*m.b38*m.b118 + 552*m.b38*
                       m.b119 + 380*m.b38*m.b169 + 342*m.b38*m.b170 + 304*m.b38*m.b171 + 342*m.b38*m.b172 + 380*m.b38*
                       m.b173 + 418*m.b38*m.b174 + 456*m.b38*m.b175 + 340*m.b38*m.b204 + 306*m.b38*m.b205 + 272*m.b38*
                       m.b206 + 306*m.b38*m.b207 + 340*m.b38*m.b208 + 374*m.b38*m.b209 + 408*m.b38*m.b210 + 506*m.b39*
                       m.b113 + 460*m.b39*m.b114 + 414*m.b39*m.b115 + 368*m.b39*m.b116 + 414*m.b39*m.b117 + 460*m.b39*
                       m.b118 + 506*m.b39*m.b119 + 418*m.b39*m.b169 + 380*m.b39*m.b170 + 342*m.b39*m.b171 + 304*m.b39*
                       m.b172 + 342*m.b39*m.b173 + 380*m.b39*m.b174 + 418*m.b39*m.b175 + 374*m.b39*m.b204 + 340*m.b39*
                       m.b205 + 306*m.b39*m.b206 + 272*m.b39*m.b207 + 306*m.b39*m.b208 + 340*m.b39*m.b209 + 374*m.b39*
                       m.b210 + 552*m.b40*m.b113 + 506*m.b40*m.b114 + 460*m.b40*m.b115 + 414*m.b40*m.b116 + 368*m.b40*
                       m.b117 + 414*m.b40*m.b118 + 460*m.b40*m.b119 + 456*m.b40*m.b169 + 418*m.b40*m.b170 + 380*m.b40*
                       m.b171 + 342*m.b40*m.b172 + 304*m.b40*m.b173 + 342*m.b40*m.b174 + 380*m.b40*m.b175 + 408*m.b40*
                       m.b204 + 374*m.b40*m.b205 + 340*m.b40*m.b206 + 306*m.b40*m.b207 + 272*m.b40*m.b208 + 306*m.b40*
                       m.b209 + 340*m.b40*m.b210 + 598*m.b41*m.b113 + 552*m.b41*m.b114 + 506*m.b41*m.b115 + 460*m.b41*
                       m.b116 + 414*m.b41*m.b117 + 368*m.b41*m.b118 + 414*m.b41*m.b119 + 494*m.b41*m.b169 + 456*m.b41*
                       m.b170 + 418*m.b41*m.b171 + 380*m.b41*m.b172 + 342*m.b41*m.b173 + 304*m.b41*m.b174 + 342*m.b41*
                       m.b175 + 442*m.b41*m.b204 + 408*m.b41*m.b205 + 374*m.b41*m.b206 + 340*m.b41*m.b207 + 306*m.b41*
                       m.b208 + 272*m.b41*m.b209 + 306*m.b41*m.b210 + 644*m.b42*m.b113 + 598*m.b42*m.b114 + 552*m.b42*
                       m.b115 + 506*m.b42*m.b116 + 460*m.b42*m.b117 + 414*m.b42*m.b118 + 368*m.b42*m.b119 + 532*m.b42*
                       m.b169 + 494*m.b42*m.b170 + 456*m.b42*m.b171 + 418*m.b42*m.b172 + 380*m.b42*m.b173 + 342*m.b42*
                       m.b174 + 304*m.b42*m.b175 + 476*m.b42*m.b204 + 442*m.b42*m.b205 + 408*m.b42*m.b206 + 374*m.b42*
                       m.b207 + 340*m.b42*m.b208 + 306*m.b42*m.b209 + 272*m.b42*m.b210 + 248*m.b43*m.b120 + 279*m.b43*
                       m.b121 + 310*m.b43*m.b122 + 341*m.b43*m.b123 + 372*m.b43*m.b124 + 403*m.b43*m.b125 + 434*m.b43*
                       m.b126 + 248*m.b43*m.b190 + 279*m.b43*m.b191 + 310*m.b43*m.b192 + 341*m.b43*m.b193 + 372*m.b43*
                       m.b194 + 403*m.b43*m.b195 + 434*m.b43*m.b196 + 279*m.b44*m.b120 + 248*m.b44*m.b121 + 279*m.b44*
                       m.b122 + 310*m.b44*m.b123 + 341*m.b44*m.b124 + 372*m.b44*m.b125 + 403*m.b44*m.b126 + 279*m.b44*
                       m.b190 + 248*m.b44*m.b191 + 279*m.b44*m.b192 + 310*m.b44*m.b193 + 341*m.b44*m.b194 + 372*m.b44*
                       m.b195 + 403*m.b44*m.b196 + 310*m.b45*m.b120 + 279*m.b45*m.b121 + 248*m.b45*m.b122 + 279*m.b45*
                       m.b123 + 310*m.b45*m.b124 + 341*m.b45*m.b125 + 372*m.b45*m.b126 + 310*m.b45*m.b190 + 279*m.b45*
                       m.b191 + 248*m.b45*m.b192 + 279*m.b45*m.b193 + 310*m.b45*m.b194 + 341*m.b45*m.b195 + 372*m.b45*
                       m.b196 + 341*m.b46*m.b120 + 310*m.b46*m.b121 + 279*m.b46*m.b122 + 248*m.b46*m.b123 + 279*m.b46*
                       m.b124 + 310*m.b46*m.b125 + 341*m.b46*m.b126 + 341*m.b46*m.b190 + 310*m.b46*m.b191 + 279*m.b46*
                       m.b192 + 248*m.b46*m.b193 + 279*m.b46*m.b194 + 310*m.b46*m.b195 + 341*m.b46*m.b196 + 372*m.b47*
                       m.b120 + 341*m.b47*m.b121 + 310*m.b47*m.b122 + 279*m.b47*m.b123 + 248*m.b47*m.b124 + 279*m.b47*
                       m.b125 + 310*m.b47*m.b126 + 372*m.b47*m.b190 + 341*m.b47*m.b191 + 310*m.b47*m.b192 + 279*m.b47*
                       m.b193 + 248*m.b47*m.b194 + 279*m.b47*m.b195 + 310*m.b47*m.b196 + 403*m.b48*m.b120 + 372*m.b48*
                       m.b121 + 341*m.b48*m.b122 + 310*m.b48*m.b123 + 279*m.b48*m.b124 + 248*m.b48*m.b125 + 279*m.b48*
                       m.b126 + 403*m.b48*m.b190 + 372*m.b48*m.b191 + 341*m.b48*m.b192 + 310*m.b48*m.b193 + 279*m.b48*
                       m.b194 + 248*m.b48*m.b195 + 279*m.b48*m.b196 + 434*m.b49*m.b120 + 403*m.b49*m.b121 + 372*m.b49*
                       m.b122 + 341*m.b49*m.b123 + 310*m.b49*m.b124 + 279*m.b49*m.b125 + 248*m.b49*m.b126 + 434*m.b49*
                       m.b190 + 403*m.b49*m.b191 + 372*m.b49*m.b192 + 341*m.b49*m.b193 + 310*m.b49*m.b194 + 279*m.b49*
                       m.b195 + 248*m.b49*m.b196 + 128*m.b50*m.b162 + 144*m.b50*m.b163 + 160*m.b50*m.b164 + 176*m.b50*
                       m.b165 + 192*m.b50*m.b166 + 208*m.b50*m.b167 + 224*m.b50*m.b168 + 184*m.b50*m.b190 + 207*m.b50*
                       m.b191 + 230*m.b50*m.b192 + 253*m.b50*m.b193 + 276*m.b50*m.b194 + 299*m.b50*m.b195 + 322*m.b50*
                       m.b196 + 184*m.b50*m.b197 + 207*m.b50*m.b198 + 230*m.b50*m.b199 + 253*m.b50*m.b200 + 276*m.b50*
                       m.b201 + 299*m.b50*m.b202 + 322*m.b50*m.b203 + 144*m.b51*m.b162 + 128*m.b51*m.b163 + 144*m.b51*
                       m.b164 + 160*m.b51*m.b165 + 176*m.b51*m.b166 + 192*m.b51*m.b167 + 208*m.b51*m.b168 + 207*m.b51*
                       m.b190 + 184*m.b51*m.b191 + 207*m.b51*m.b192 + 230*m.b51*m.b193 + 253*m.b51*m.b194 + 276*m.b51*
                       m.b195 + 299*m.b51*m.b196 + 207*m.b51*m.b197 + 184*m.b51*m.b198 + 207*m.b51*m.b199 + 230*m.b51*
                       m.b200 + 253*m.b51*m.b201 + 276*m.b51*m.b202 + 299*m.b51*m.b203 + 160*m.b52*m.b162 + 144*m.b52*
                       m.b163 + 128*m.b52*m.b164 + 144*m.b52*m.b165 + 160*m.b52*m.b166 + 176*m.b52*m.b167 + 192*m.b52*
                       m.b168 + 230*m.b52*m.b190 + 207*m.b52*m.b191 + 184*m.b52*m.b192 + 207*m.b52*m.b193 + 230*m.b52*
                       m.b194 + 253*m.b52*m.b195 + 276*m.b52*m.b196 + 230*m.b52*m.b197 + 207*m.b52*m.b198 + 184*m.b52*
                       m.b199 + 207*m.b52*m.b200 + 230*m.b52*m.b201 + 253*m.b52*m.b202 + 276*m.b52*m.b203 + 176*m.b53*
                       m.b162 + 160*m.b53*m.b163 + 144*m.b53*m.b164 + 128*m.b53*m.b165 + 144*m.b53*m.b166 + 160*m.b53*
                       m.b167 + 176*m.b53*m.b168 + 253*m.b53*m.b190 + 230*m.b53*m.b191 + 207*m.b53*m.b192 + 184*m.b53*
                       m.b193 + 207*m.b53*m.b194 + 230*m.b53*m.b195 + 253*m.b53*m.b196 + 253*m.b53*m.b197 + 230*m.b53*
                       m.b198 + 207*m.b53*m.b199 + 184*m.b53*m.b200 + 207*m.b53*m.b201 + 230*m.b53*m.b202 + 253*m.b53*
                       m.b203 + 192*m.b54*m.b162 + 176*m.b54*m.b163 + 160*m.b54*m.b164 + 144*m.b54*m.b165 + 128*m.b54*
                       m.b166 + 144*m.b54*m.b167 + 160*m.b54*m.b168 + 276*m.b54*m.b190 + 253*m.b54*m.b191 + 230*m.b54*
                       m.b192 + 207*m.b54*m.b193 + 184*m.b54*m.b194 + 207*m.b54*m.b195 + 230*m.b54*m.b196 + 276*m.b54*
                       m.b197 + 253*m.b54*m.b198 + 230*m.b54*m.b199 + 207*m.b54*m.b200 + 184*m.b54*m.b201 + 207*m.b54*
                       m.b202 + 230*m.b54*m.b203 + 208*m.b55*m.b162 + 192*m.b55*m.b163 + 176*m.b55*m.b164 + 160*m.b55*
                       m.b165 + 144*m.b55*m.b166 + 128*m.b55*m.b167 + 144*m.b55*m.b168 + 299*m.b55*m.b190 + 276*m.b55*
                       m.b191 + 253*m.b55*m.b192 + 230*m.b55*m.b193 + 207*m.b55*m.b194 + 184*m.b55*m.b195 + 207*m.b55*
                       m.b196 + 299*m.b55*m.b197 + 276*m.b55*m.b198 + 253*m.b55*m.b199 + 230*m.b55*m.b200 + 207*m.b55*
                       m.b201 + 184*m.b55*m.b202 + 207*m.b55*m.b203 + 224*m.b56*m.b162 + 208*m.b56*m.b163 + 192*m.b56*
                       m.b164 + 176*m.b56*m.b165 + 160*m.b56*m.b166 + 144*m.b56*m.b167 + 128*m.b56*m.b168 + 322*m.b56*
                       m.b190 + 299*m.b56*m.b191 + 276*m.b56*m.b192 + 253*m.b56*m.b193 + 230*m.b56*m.b194 + 207*m.b56*
                       m.b195 + 184*m.b56*m.b196 + 322*m.b56*m.b197 + 299*m.b56*m.b198 + 276*m.b56*m.b199 + 253*m.b56*
                       m.b200 + 230*m.b56*m.b201 + 207*m.b56*m.b202 + 184*m.b56*m.b203 + 160*m.b57*m.b120 + 180*m.b57*
                       m.b121 + 200*m.b57*m.b122 + 220*m.b57*m.b123 + 240*m.b57*m.b124 + 260*m.b57*m.b125 + 280*m.b57*
                       m.b126 + 160*m.b57*m.b127 + 180*m.b57*m.b128 + 200*m.b57*m.b129 + 220*m.b57*m.b130 + 240*m.b57*
                       m.b131 + 260*m.b57*m.b132 + 280*m.b57*m.b133 + 312*m.b57*m.b141 + 351*m.b57*m.b142 + 390*m.b57*
                       m.b143 + 429*m.b57*m.b144 + 468*m.b57*m.b145 + 507*m.b57*m.b146 + 546*m.b57*m.b147 + 248*m.b57*
                       m.b155 + 279*m.b57*m.b156 + 310*m.b57*m.b157 + 341*m.b57*m.b158 + 372*m.b57*m.b159 + 403*m.b57*
                       m.b160 + 434*m.b57*m.b161 + 88*m.b57*m.b176 + 99*m.b57*m.b177 + 110*m.b57*m.b178 + 121*m.b57*
                       m.b179 + 132*m.b57*m.b180 + 143*m.b57*m.b181 + 154*m.b57*m.b182 + 136*m.b57*m.b183 + 153*m.b57*
                       m.b184 + 170*m.b57*m.b185 + 187*m.b57*m.b186 + 204*m.b57*m.b187 + 221*m.b57*m.b188 + 238*m.b57*
                       m.b189 + 180*m.b58*m.b120 + 160*m.b58*m.b121 + 180*m.b58*m.b122 + 200*m.b58*m.b123 + 220*m.b58*
                       m.b124 + 240*m.b58*m.b125 + 260*m.b58*m.b126 + 180*m.b58*m.b127 + 160*m.b58*m.b128 + 180*m.b58*
                       m.b129 + 200*m.b58*m.b130 + 220*m.b58*m.b131 + 240*m.b58*m.b132 + 260*m.b58*m.b133 + 351*m.b58*
                       m.b141 + 312*m.b58*m.b142 + 351*m.b58*m.b143 + 390*m.b58*m.b144 + 429*m.b58*m.b145 + 468*m.b58*
                       m.b146 + 507*m.b58*m.b147 + 279*m.b58*m.b155 + 248*m.b58*m.b156 + 279*m.b58*m.b157 + 310*m.b58*
                       m.b158 + 341*m.b58*m.b159 + 372*m.b58*m.b160 + 403*m.b58*m.b161 + 99*m.b58*m.b176 + 88*m.b58*
                       m.b177 + 99*m.b58*m.b178 + 110*m.b58*m.b179 + 121*m.b58*m.b180 + 132*m.b58*m.b181 + 143*m.b58*
                       m.b182 + 153*m.b58*m.b183 + 136*m.b58*m.b184 + 153*m.b58*m.b185 + 170*m.b58*m.b186 + 187*m.b58*
                       m.b187 + 204*m.b58*m.b188 + 221*m.b58*m.b189 + 200*m.b59*m.b120 + 180*m.b59*m.b121 + 160*m.b59*
                       m.b122 + 180*m.b59*m.b123 + 200*m.b59*m.b124 + 220*m.b59*m.b125 + 240*m.b59*m.b126 + 200*m.b59*
                       m.b127 + 180*m.b59*m.b128 + 160*m.b59*m.b129 + 180*m.b59*m.b130 + 200*m.b59*m.b131 + 220*m.b59*
                       m.b132 + 240*m.b59*m.b133 + 390*m.b59*m.b141 + 351*m.b59*m.b142 + 312*m.b59*m.b143 + 351*m.b59*
                       m.b144 + 390*m.b59*m.b145 + 429*m.b59*m.b146 + 468*m.b59*m.b147 + 310*m.b59*m.b155 + 279*m.b59*
                       m.b156 + 248*m.b59*m.b157 + 279*m.b59*m.b158 + 310*m.b59*m.b159 + 341*m.b59*m.b160 + 372*m.b59*
                       m.b161 + 110*m.b59*m.b176 + 99*m.b59*m.b177 + 88*m.b59*m.b178 + 99*m.b59*m.b179 + 110*m.b59*
                       m.b180 + 121*m.b59*m.b181 + 132*m.b59*m.b182 + 170*m.b59*m.b183 + 153*m.b59*m.b184 + 136*m.b59*
                       m.b185 + 153*m.b59*m.b186 + 170*m.b59*m.b187 + 187*m.b59*m.b188 + 204*m.b59*m.b189 + 220*m.b60*
                       m.b120 + 200*m.b60*m.b121 + 180*m.b60*m.b122 + 160*m.b60*m.b123 + 180*m.b60*m.b124 + 200*m.b60*
                       m.b125 + 220*m.b60*m.b126 + 220*m.b60*m.b127 + 200*m.b60*m.b128 + 180*m.b60*m.b129 + 160*m.b60*
                       m.b130 + 180*m.b60*m.b131 + 200*m.b60*m.b132 + 220*m.b60*m.b133 + 429*m.b60*m.b141 + 390*m.b60*
                       m.b142 + 351*m.b60*m.b143 + 312*m.b60*m.b144 + 351*m.b60*m.b145 + 390*m.b60*m.b146 + 429*m.b60*
                       m.b147 + 341*m.b60*m.b155 + 310*m.b60*m.b156 + 279*m.b60*m.b157 + 248*m.b60*m.b158 + 279*m.b60*
                       m.b159 + 310*m.b60*m.b160 + 341*m.b60*m.b161 + 121*m.b60*m.b176 + 110*m.b60*m.b177 + 99*m.b60*
                       m.b178 + 88*m.b60*m.b179 + 99*m.b60*m.b180 + 110*m.b60*m.b181 + 121*m.b60*m.b182 + 187*m.b60*
                       m.b183 + 170*m.b60*m.b184 + 153*m.b60*m.b185 + 136*m.b60*m.b186 + 153*m.b60*m.b187 + 170*m.b60*
                       m.b188 + 187*m.b60*m.b189 + 240*m.b61*m.b120 + 220*m.b61*m.b121 + 200*m.b61*m.b122 + 180*m.b61*
                       m.b123 + 160*m.b61*m.b124 + 180*m.b61*m.b125 + 200*m.b61*m.b126 + 240*m.b61*m.b127 + 220*m.b61*
                       m.b128 + 200*m.b61*m.b129 + 180*m.b61*m.b130 + 160*m.b61*m.b131 + 180*m.b61*m.b132 + 200*m.b61*
                       m.b133 + 468*m.b61*m.b141 + 429*m.b61*m.b142 + 390*m.b61*m.b143 + 351*m.b61*m.b144 + 312*m.b61*
                       m.b145 + 351*m.b61*m.b146 + 390*m.b61*m.b147 + 372*m.b61*m.b155 + 341*m.b61*m.b156 + 310*m.b61*
                       m.b157 + 279*m.b61*m.b158 + 248*m.b61*m.b159 + 279*m.b61*m.b160 + 310*m.b61*m.b161 + 132*m.b61*
                       m.b176 + 121*m.b61*m.b177 + 110*m.b61*m.b178 + 99*m.b61*m.b179 + 88*m.b61*m.b180 + 99*m.b61*
                       m.b181 + 110*m.b61*m.b182 + 204*m.b61*m.b183 + 187*m.b61*m.b184 + 170*m.b61*m.b185 + 153*m.b61*
                       m.b186 + 136*m.b61*m.b187 + 153*m.b61*m.b188 + 170*m.b61*m.b189 + 260*m.b62*m.b120 + 240*m.b62*
                       m.b121 + 220*m.b62*m.b122 + 200*m.b62*m.b123 + 180*m.b62*m.b124 + 160*m.b62*m.b125 + 180*m.b62*
                       m.b126 + 260*m.b62*m.b127 + 240*m.b62*m.b128 + 220*m.b62*m.b129 + 200*m.b62*m.b130 + 180*m.b62*
                       m.b131 + 160*m.b62*m.b132 + 180*m.b62*m.b133 + 507*m.b62*m.b141 + 468*m.b62*m.b142 + 429*m.b62*
                       m.b143 + 390*m.b62*m.b144 + 351*m.b62*m.b145 + 312*m.b62*m.b146 + 351*m.b62*m.b147 + 403*m.b62*
                       m.b155 + 372*m.b62*m.b156 + 341*m.b62*m.b157 + 310*m.b62*m.b158 + 279*m.b62*m.b159 + 248*m.b62*
                       m.b160 + 279*m.b62*m.b161 + 143*m.b62*m.b176 + 132*m.b62*m.b177 + 121*m.b62*m.b178 + 110*m.b62*
                       m.b179 + 99*m.b62*m.b180 + 88*m.b62*m.b181 + 99*m.b62*m.b182 + 221*m.b62*m.b183 + 204*m.b62*
                       m.b184 + 187*m.b62*m.b185 + 170*m.b62*m.b186 + 153*m.b62*m.b187 + 136*m.b62*m.b188 + 153*m.b62*
                       m.b189 + 280*m.b63*m.b120 + 260*m.b63*m.b121 + 240*m.b63*m.b122 + 220*m.b63*m.b123 + 200*m.b63*
                       m.b124 + 180*m.b63*m.b125 + 160*m.b63*m.b126 + 280*m.b63*m.b127 + 260*m.b63*m.b128 + 240*m.b63*
                       m.b129 + 220*m.b63*m.b130 + 200*m.b63*m.b131 + 180*m.b63*m.b132 + 160*m.b63*m.b133 + 546*m.b63*
                       m.b141 + 507*m.b63*m.b142 + 468*m.b63*m.b143 + 429*m.b63*m.b144 + 390*m.b63*m.b145 + 351*m.b63*
                       m.b146 + 312*m.b63*m.b147 + 434*m.b63*m.b155 + 403*m.b63*m.b156 + 372*m.b63*m.b157 + 341*m.b63*
                       m.b158 + 310*m.b63*m.b159 + 279*m.b63*m.b160 + 248*m.b63*m.b161 + 154*m.b63*m.b176 + 143*m.b63*
                       m.b177 + 132*m.b63*m.b178 + 121*m.b63*m.b179 + 110*m.b63*m.b180 + 99*m.b63*m.b181 + 88*m.b63*
                       m.b182 + 238*m.b63*m.b183 + 221*m.b63*m.b184 + 204*m.b63*m.b185 + 187*m.b63*m.b186 + 170*m.b63*
                       m.b187 + 153*m.b63*m.b188 + 136*m.b63*m.b189 + 304*m.b64*m.b106 + 342*m.b64*m.b107 + 380*m.b64*
                       m.b108 + 418*m.b64*m.b109 + 456*m.b64*m.b110 + 494*m.b64*m.b111 + 532*m.b64*m.b112 + 392*m.b64*
                       m.b141 + 441*m.b64*m.b142 + 490*m.b64*m.b143 + 539*m.b64*m.b144 + 588*m.b64*m.b145 + 637*m.b64*
                       m.b146 + 686*m.b64*m.b147 + 336*m.b64*m.b204 + 378*m.b64*m.b205 + 420*m.b64*m.b206 + 462*m.b64*
                       m.b207 + 504*m.b64*m.b208 + 546*m.b64*m.b209 + 588*m.b64*m.b210 + 342*m.b65*m.b106 + 304*m.b65*
                       m.b107 + 342*m.b65*m.b108 + 380*m.b65*m.b109 + 418*m.b65*m.b110 + 456*m.b65*m.b111 + 494*m.b65*
                       m.b112 + 441*m.b65*m.b141 + 392*m.b65*m.b142 + 441*m.b65*m.b143 + 490*m.b65*m.b144 + 539*m.b65*
                       m.b145 + 588*m.b65*m.b146 + 637*m.b65*m.b147 + 378*m.b65*m.b204 + 336*m.b65*m.b205 + 378*m.b65*
                       m.b206 + 420*m.b65*m.b207 + 462*m.b65*m.b208 + 504*m.b65*m.b209 + 546*m.b65*m.b210 + 380*m.b66*
                       m.b106 + 342*m.b66*m.b107 + 304*m.b66*m.b108 + 342*m.b66*m.b109 + 380*m.b66*m.b110 + 418*m.b66*
                       m.b111 + 456*m.b66*m.b112 + 490*m.b66*m.b141 + 441*m.b66*m.b142 + 392*m.b66*m.b143 + 441*m.b66*
                       m.b144 + 490*m.b66*m.b145 + 539*m.b66*m.b146 + 588*m.b66*m.b147 + 420*m.b66*m.b204 + 378*m.b66*
                       m.b205 + 336*m.b66*m.b206 + 378*m.b66*m.b207 + 420*m.b66*m.b208 + 462*m.b66*m.b209 + 504*m.b66*
                       m.b210 + 418*m.b67*m.b106 + 380*m.b67*m.b107 + 342*m.b67*m.b108 + 304*m.b67*m.b109 + 342*m.b67*
                       m.b110 + 380*m.b67*m.b111 + 418*m.b67*m.b112 + 539*m.b67*m.b141 + 490*m.b67*m.b142 + 441*m.b67*
                       m.b143 + 392*m.b67*m.b144 + 441*m.b67*m.b145 + 490*m.b67*m.b146 + 539*m.b67*m.b147 + 462*m.b67*
                       m.b204 + 420*m.b67*m.b205 + 378*m.b67*m.b206 + 336*m.b67*m.b207 + 378*m.b67*m.b208 + 420*m.b67*
                       m.b209 + 462*m.b67*m.b210 + 456*m.b68*m.b106 + 418*m.b68*m.b107 + 380*m.b68*m.b108 + 342*m.b68*
                       m.b109 + 304*m.b68*m.b110 + 342*m.b68*m.b111 + 380*m.b68*m.b112 + 588*m.b68*m.b141 + 539*m.b68*
                       m.b142 + 490*m.b68*m.b143 + 441*m.b68*m.b144 + 392*m.b68*m.b145 + 441*m.b68*m.b146 + 490*m.b68*
                       m.b147 + 504*m.b68*m.b204 + 462*m.b68*m.b205 + 420*m.b68*m.b206 + 378*m.b68*m.b207 + 336*m.b68*
                       m.b208 + 378*m.b68*m.b209 + 420*m.b68*m.b210 + 494*m.b69*m.b106 + 456*m.b69*m.b107 + 418*m.b69*
                       m.b108 + 380*m.b69*m.b109 + 342*m.b69*m.b110 + 304*m.b69*m.b111 + 342*m.b69*m.b112 + 637*m.b69*
                       m.b141 + 588*m.b69*m.b142 + 539*m.b69*m.b143 + 490*m.b69*m.b144 + 441*m.b69*m.b145 + 392*m.b69*
                       m.b146 + 441*m.b69*m.b147 + 546*m.b69*m.b204 + 504*m.b69*m.b205 + 462*m.b69*m.b206 + 420*m.b69*
                       m.b207 + 378*m.b69*m.b208 + 336*m.b69*m.b209 + 378*m.b69*m.b210 + 532*m.b70*m.b106 + 494*m.b70*
                       m.b107 + 456*m.b70*m.b108 + 418*m.b70*m.b109 + 380*m.b70*m.b110 + 342*m.b70*m.b111 + 304*m.b70*
                       m.b112 + 686*m.b70*m.b141 + 637*m.b70*m.b142 + 588*m.b70*m.b143 + 539*m.b70*m.b144 + 490*m.b70*
                       m.b145 + 441*m.b70*m.b146 + 392*m.b70*m.b147 + 588*m.b70*m.b204 + 546*m.b70*m.b205 + 504*m.b70*
                       m.b206 + 462*m.b70*m.b207 + 420*m.b70*m.b208 + 378*m.b70*m.b209 + 336*m.b70*m.b210 + 200*m.b71*
                       m.b183 + 225*m.b71*m.b184 + 250*m.b71*m.b185 + 275*m.b71*m.b186 + 300*m.b71*m.b187 + 325*m.b71*
                       m.b188 + 350*m.b71*m.b189 + 225*m.b72*m.b183 + 200*m.b72*m.b184 + 225*m.b72*m.b185 + 250*m.b72*
                       m.b186 + 275*m.b72*m.b187 + 300*m.b72*m.b188 + 325*m.b72*m.b189 + 250*m.b73*m.b183 + 225*m.b73*
                       m.b184 + 200*m.b73*m.b185 + 225*m.b73*m.b186 + 250*m.b73*m.b187 + 275*m.b73*m.b188 + 300*m.b73*
                       m.b189 + 275*m.b74*m.b183 + 250*m.b74*m.b184 + 225*m.b74*m.b185 + 200*m.b74*m.b186 + 225*m.b74*
                       m.b187 + 250*m.b74*m.b188 + 275*m.b74*m.b189 + 300*m.b75*m.b183 + 275*m.b75*m.b184 + 250*m.b75*
                       m.b185 + 225*m.b75*m.b186 + 200*m.b75*m.b187 + 225*m.b75*m.b188 + 250*m.b75*m.b189 + 325*m.b76*
                       m.b183 + 300*m.b76*m.b184 + 275*m.b76*m.b185 + 250*m.b76*m.b186 + 225*m.b76*m.b187 + 200*m.b76*
                       m.b188 + 225*m.b76*m.b189 + 350*m.b77*m.b183 + 325*m.b77*m.b184 + 300*m.b77*m.b185 + 275*m.b77*
                       m.b186 + 250*m.b77*m.b187 + 225*m.b77*m.b188 + 200*m.b77*m.b189 + 256*m.b78*m.b155 + 288*m.b78*
                       m.b156 + 320*m.b78*m.b157 + 352*m.b78*m.b158 + 384*m.b78*m.b159 + 416*m.b78*m.b160 + 448*m.b78*
                       m.b161 + 360*m.b78*m.b183 + 405*m.b78*m.b184 + 450*m.b78*m.b185 + 495*m.b78*m.b186 + 540*m.b78*
                       m.b187 + 585*m.b78*m.b188 + 630*m.b78*m.b189 + 344*m.b78*m.b204 + 387*m.b78*m.b205 + 430*m.b78*
                       m.b206 + 473*m.b78*m.b207 + 516*m.b78*m.b208 + 559*m.b78*m.b209 + 602*m.b78*m.b210 + 288*m.b79*
                       m.b155 + 256*m.b79*m.b156 + 288*m.b79*m.b157 + 320*m.b79*m.b158 + 352*m.b79*m.b159 + 384*m.b79*
                       m.b160 + 416*m.b79*m.b161 + 405*m.b79*m.b183 + 360*m.b79*m.b184 + 405*m.b79*m.b185 + 450*m.b79*
                       m.b186 + 495*m.b79*m.b187 + 540*m.b79*m.b188 + 585*m.b79*m.b189 + 387*m.b79*m.b204 + 344*m.b79*
                       m.b205 + 387*m.b79*m.b206 + 430*m.b79*m.b207 + 473*m.b79*m.b208 + 516*m.b79*m.b209 + 559*m.b79*
                       m.b210 + 320*m.b80*m.b155 + 288*m.b80*m.b156 + 256*m.b80*m.b157 + 288*m.b80*m.b158 + 320*m.b80*
                       m.b159 + 352*m.b80*m.b160 + 384*m.b80*m.b161 + 450*m.b80*m.b183 + 405*m.b80*m.b184 + 360*m.b80*
                       m.b185 + 405*m.b80*m.b186 + 450*m.b80*m.b187 + 495*m.b80*m.b188 + 540*m.b80*m.b189 + 430*m.b80*
                       m.b204 + 387*m.b80*m.b205 + 344*m.b80*m.b206 + 387*m.b80*m.b207 + 430*m.b80*m.b208 + 473*m.b80*
                       m.b209 + 516*m.b80*m.b210 + 352*m.b81*m.b155 + 320*m.b81*m.b156 + 288*m.b81*m.b157 + 256*m.b81*
                       m.b158 + 288*m.b81*m.b159 + 320*m.b81*m.b160 + 352*m.b81*m.b161 + 495*m.b81*m.b183 + 450*m.b81*
                       m.b184 + 405*m.b81*m.b185 + 360*m.b81*m.b186 + 405*m.b81*m.b187 + 450*m.b81*m.b188 + 495*m.b81*
                       m.b189 + 473*m.b81*m.b204 + 430*m.b81*m.b205 + 387*m.b81*m.b206 + 344*m.b81*m.b207 + 387*m.b81*
                       m.b208 + 430*m.b81*m.b209 + 473*m.b81*m.b210 + 384*m.b82*m.b155 + 352*m.b82*m.b156 + 320*m.b82*
                       m.b157 + 288*m.b82*m.b158 + 256*m.b82*m.b159 + 288*m.b82*m.b160 + 320*m.b82*m.b161 + 540*m.b82*
                       m.b183 + 495*m.b82*m.b184 + 450*m.b82*m.b185 + 405*m.b82*m.b186 + 360*m.b82*m.b187 + 405*m.b82*
                       m.b188 + 450*m.b82*m.b189 + 516*m.b82*m.b204 + 473*m.b82*m.b205 + 430*m.b82*m.b206 + 387*m.b82*
                       m.b207 + 344*m.b82*m.b208 + 387*m.b82*m.b209 + 430*m.b82*m.b210 + 416*m.b83*m.b155 + 384*m.b83*
                       m.b156 + 352*m.b83*m.b157 + 320*m.b83*m.b158 + 288*m.b83*m.b159 + 256*m.b83*m.b160 + 288*m.b83*
                       m.b161 + 585*m.b83*m.b183 + 540*m.b83*m.b184 + 495*m.b83*m.b185 + 450*m.b83*m.b186 + 405*m.b83*
                       m.b187 + 360*m.b83*m.b188 + 405*m.b83*m.b189 + 559*m.b83*m.b204 + 516*m.b83*m.b205 + 473*m.b83*
                       m.b206 + 430*m.b83*m.b207 + 387*m.b83*m.b208 + 344*m.b83*m.b209 + 387*m.b83*m.b210 + 448*m.b84*
                       m.b155 + 416*m.b84*m.b156 + 384*m.b84*m.b157 + 352*m.b84*m.b158 + 320*m.b84*m.b159 + 288*m.b84*
                       m.b160 + 256*m.b84*m.b161 + 630*m.b84*m.b183 + 585*m.b84*m.b184 + 540*m.b84*m.b185 + 495*m.b84*
                       m.b186 + 450*m.b84*m.b187 + 405*m.b84*m.b188 + 360*m.b84*m.b189 + 602*m.b84*m.b204 + 559*m.b84*
                       m.b205 + 516*m.b84*m.b206 + 473*m.b84*m.b207 + 430*m.b84*m.b208 + 387*m.b84*m.b209 + 344*m.b84*
                       m.b210 + 264*m.b85*m.b120 + 297*m.b85*m.b121 + 330*m.b85*m.b122 + 363*m.b85*m.b123 + 396*m.b85*
                       m.b124 + 429*m.b85*m.b125 + 462*m.b85*m.b126 + 112*m.b85*m.b141 + 126*m.b85*m.b142 + 140*m.b85*
                       m.b143 + 154*m.b85*m.b144 + 168*m.b85*m.b145 + 182*m.b85*m.b146 + 196*m.b85*m.b147 + 240*m.b85*
                       m.b148 + 270*m.b85*m.b149 + 300*m.b85*m.b150 + 330*m.b85*m.b151 + 360*m.b85*m.b152 + 390*m.b85*
                       m.b153 + 420*m.b85*m.b154 + 128*m.b85*m.b176 + 144*m.b85*m.b177 + 160*m.b85*m.b178 + 176*m.b85*
                       m.b179 + 192*m.b85*m.b180 + 208*m.b85*m.b181 + 224*m.b85*m.b182 + 297*m.b86*m.b120 + 264*m.b86*
                       m.b121 + 297*m.b86*m.b122 + 330*m.b86*m.b123 + 363*m.b86*m.b124 + 396*m.b86*m.b125 + 429*m.b86*
                       m.b126 + 126*m.b86*m.b141 + 112*m.b86*m.b142 + 126*m.b86*m.b143 + 140*m.b86*m.b144 + 154*m.b86*
                       m.b145 + 168*m.b86*m.b146 + 182*m.b86*m.b147 + 270*m.b86*m.b148 + 240*m.b86*m.b149 + 270*m.b86*
                       m.b150 + 300*m.b86*m.b151 + 330*m.b86*m.b152 + 360*m.b86*m.b153 + 390*m.b86*m.b154 + 144*m.b86*
                       m.b176 + 128*m.b86*m.b177 + 144*m.b86*m.b178 + 160*m.b86*m.b179 + 176*m.b86*m.b180 + 192*m.b86*
                       m.b181 + 208*m.b86*m.b182 + 330*m.b87*m.b120 + 297*m.b87*m.b121 + 264*m.b87*m.b122 + 297*m.b87*
                       m.b123 + 330*m.b87*m.b124 + 363*m.b87*m.b125 + 396*m.b87*m.b126 + 140*m.b87*m.b141 + 126*m.b87*
                       m.b142 + 112*m.b87*m.b143 + 126*m.b87*m.b144 + 140*m.b87*m.b145 + 154*m.b87*m.b146 + 168*m.b87*
                       m.b147 + 300*m.b87*m.b148 + 270*m.b87*m.b149 + 240*m.b87*m.b150 + 270*m.b87*m.b151 + 300*m.b87*
                       m.b152 + 330*m.b87*m.b153 + 360*m.b87*m.b154 + 160*m.b87*m.b176 + 144*m.b87*m.b177 + 128*m.b87*
                       m.b178 + 144*m.b87*m.b179 + 160*m.b87*m.b180 + 176*m.b87*m.b181 + 192*m.b87*m.b182 + 363*m.b88*
                       m.b120 + 330*m.b88*m.b121 + 297*m.b88*m.b122 + 264*m.b88*m.b123 + 297*m.b88*m.b124 + 330*m.b88*
                       m.b125 + 363*m.b88*m.b126 + 154*m.b88*m.b141 + 140*m.b88*m.b142 + 126*m.b88*m.b143 + 112*m.b88*
                       m.b144 + 126*m.b88*m.b145 + 140*m.b88*m.b146 + 154*m.b88*m.b147 + 330*m.b88*m.b148 + 300*m.b88*
                       m.b149 + 270*m.b88*m.b150 + 240*m.b88*m.b151 + 270*m.b88*m.b152 + 300*m.b88*m.b153 + 330*m.b88*
                       m.b154 + 176*m.b88*m.b176 + 160*m.b88*m.b177 + 144*m.b88*m.b178 + 128*m.b88*m.b179 + 144*m.b88*
                       m.b180 + 160*m.b88*m.b181 + 176*m.b88*m.b182 + 396*m.b89*m.b120 + 363*m.b89*m.b121 + 330*m.b89*
                       m.b122 + 297*m.b89*m.b123 + 264*m.b89*m.b124 + 297*m.b89*m.b125 + 330*m.b89*m.b126 + 168*m.b89*
                       m.b141 + 154*m.b89*m.b142 + 140*m.b89*m.b143 + 126*m.b89*m.b144 + 112*m.b89*m.b145 + 126*m.b89*
                       m.b146 + 140*m.b89*m.b147 + 360*m.b89*m.b148 + 330*m.b89*m.b149 + 300*m.b89*m.b150 + 270*m.b89*
                       m.b151 + 240*m.b89*m.b152 + 270*m.b89*m.b153 + 300*m.b89*m.b154 + 192*m.b89*m.b176 + 176*m.b89*
                       m.b177 + 160*m.b89*m.b178 + 144*m.b89*m.b179 + 128*m.b89*m.b180 + 144*m.b89*m.b181 + 160*m.b89*
                       m.b182 + 429*m.b90*m.b120 + 396*m.b90*m.b121 + 363*m.b90*m.b122 + 330*m.b90*m.b123 + 297*m.b90*
                       m.b124 + 264*m.b90*m.b125 + 297*m.b90*m.b126 + 182*m.b90*m.b141 + 168*m.b90*m.b142 + 154*m.b90*
                       m.b143 + 140*m.b90*m.b144 + 126*m.b90*m.b145 + 112*m.b90*m.b146 + 126*m.b90*m.b147 + 390*m.b90*
                       m.b148 + 360*m.b90*m.b149 + 330*m.b90*m.b150 + 300*m.b90*m.b151 + 270*m.b90*m.b152 + 240*m.b90*
                       m.b153 + 270*m.b90*m.b154 + 208*m.b90*m.b176 + 192*m.b90*m.b177 + 176*m.b90*m.b178 + 160*m.b90*
                       m.b179 + 144*m.b90*m.b180 + 128*m.b90*m.b181 + 144*m.b90*m.b182 + 462*m.b91*m.b120 + 429*m.b91*
                       m.b121 + 396*m.b91*m.b122 + 363*m.b91*m.b123 + 330*m.b91*m.b124 + 297*m.b91*m.b125 + 264*m.b91*
                       m.b126 + 196*m.b91*m.b141 + 182*m.b91*m.b142 + 168*m.b91*m.b143 + 154*m.b91*m.b144 + 140*m.b91*
                       m.b145 + 126*m.b91*m.b146 + 112*m.b91*m.b147 + 420*m.b91*m.b148 + 390*m.b91*m.b149 + 360*m.b91*
                       m.b150 + 330*m.b91*m.b151 + 300*m.b91*m.b152 + 270*m.b91*m.b153 + 240*m.b91*m.b154 + 224*m.b91*
                       m.b176 + 208*m.b91*m.b177 + 192*m.b91*m.b178 + 176*m.b91*m.b179 + 160*m.b91*m.b180 + 144*m.b91*
                       m.b181 + 128*m.b91*m.b182 + 248*m.b92*m.b106 + 279*m.b92*m.b107 + 310*m.b92*m.b108 + 341*m.b92*
                       m.b109 + 372*m.b92*m.b110 + 403*m.b92*m.b111 + 434*m.b92*m.b112 + 272*m.b92*m.b134 + 306*m.b92*
                       m.b135 + 340*m.b92*m.b136 + 374*m.b92*m.b137 + 408*m.b92*m.b138 + 442*m.b92*m.b139 + 476*m.b92*
                       m.b140 + 240*m.b92*m.b141 + 270*m.b92*m.b142 + 300*m.b92*m.b143 + 330*m.b92*m.b144 + 360*m.b92*
                       m.b145 + 390*m.b92*m.b146 + 420*m.b92*m.b147 + 272*m.b92*m.b155 + 306*m.b92*m.b156 + 340*m.b92*
                       m.b157 + 374*m.b92*m.b158 + 408*m.b92*m.b159 + 442*m.b92*m.b160 + 476*m.b92*m.b161 + 112*m.b92*
                       m.b162 + 126*m.b92*m.b163 + 140*m.b92*m.b164 + 154*m.b92*m.b165 + 168*m.b92*m.b166 + 182*m.b92*
                       m.b167 + 196*m.b92*m.b168 + 184*m.b92*m.b197 + 207*m.b92*m.b198 + 230*m.b92*m.b199 + 253*m.b92*
                       m.b200 + 276*m.b92*m.b201 + 299*m.b92*m.b202 + 322*m.b92*m.b203 + 279*m.b93*m.b106 + 248*m.b93*
                       m.b107 + 279*m.b93*m.b108 + 310*m.b93*m.b109 + 341*m.b93*m.b110 + 372*m.b93*m.b111 + 403*m.b93*
                       m.b112 + 306*m.b93*m.b134 + 272*m.b93*m.b135 + 306*m.b93*m.b136 + 340*m.b93*m.b137 + 374*m.b93*
                       m.b138 + 408*m.b93*m.b139 + 442*m.b93*m.b140 + 270*m.b93*m.b141 + 240*m.b93*m.b142 + 270*m.b93*
                       m.b143 + 300*m.b93*m.b144 + 330*m.b93*m.b145 + 360*m.b93*m.b146 + 390*m.b93*m.b147 + 306*m.b93*
                       m.b155 + 272*m.b93*m.b156 + 306*m.b93*m.b157 + 340*m.b93*m.b158 + 374*m.b93*m.b159 + 408*m.b93*
                       m.b160 + 442*m.b93*m.b161 + 126*m.b93*m.b162 + 112*m.b93*m.b163 + 126*m.b93*m.b164 + 140*m.b93*
                       m.b165 + 154*m.b93*m.b166 + 168*m.b93*m.b167 + 182*m.b93*m.b168 + 207*m.b93*m.b197 + 184*m.b93*
                       m.b198 + 207*m.b93*m.b199 + 230*m.b93*m.b200 + 253*m.b93*m.b201 + 276*m.b93*m.b202 + 299*m.b93*
                       m.b203 + 310*m.b94*m.b106 + 279*m.b94*m.b107 + 248*m.b94*m.b108 + 279*m.b94*m.b109 + 310*m.b94*
                       m.b110 + 341*m.b94*m.b111 + 372*m.b94*m.b112 + 340*m.b94*m.b134 + 306*m.b94*m.b135 + 272*m.b94*
                       m.b136 + 306*m.b94*m.b137 + 340*m.b94*m.b138 + 374*m.b94*m.b139 + 408*m.b94*m.b140 + 300*m.b94*
                       m.b141 + 270*m.b94*m.b142 + 240*m.b94*m.b143 + 270*m.b94*m.b144 + 300*m.b94*m.b145 + 330*m.b94*
                       m.b146 + 360*m.b94*m.b147 + 340*m.b94*m.b155 + 306*m.b94*m.b156 + 272*m.b94*m.b157 + 306*m.b94*
                       m.b158 + 340*m.b94*m.b159 + 374*m.b94*m.b160 + 408*m.b94*m.b161 + 140*m.b94*m.b162 + 126*m.b94*
                       m.b163 + 112*m.b94*m.b164 + 126*m.b94*m.b165 + 140*m.b94*m.b166 + 154*m.b94*m.b167 + 168*m.b94*
                       m.b168 + 230*m.b94*m.b197 + 207*m.b94*m.b198 + 184*m.b94*m.b199 + 207*m.b94*m.b200 + 230*m.b94*
                       m.b201 + 253*m.b94*m.b202 + 276*m.b94*m.b203 + 341*m.b95*m.b106 + 310*m.b95*m.b107 + 279*m.b95*
                       m.b108 + 248*m.b95*m.b109 + 279*m.b95*m.b110 + 310*m.b95*m.b111 + 341*m.b95*m.b112 + 374*m.b95*
                       m.b134 + 340*m.b95*m.b135 + 306*m.b95*m.b136 + 272*m.b95*m.b137 + 306*m.b95*m.b138 + 340*m.b95*
                       m.b139 + 374*m.b95*m.b140 + 330*m.b95*m.b141 + 300*m.b95*m.b142 + 270*m.b95*m.b143 + 240*m.b95*
                       m.b144 + 270*m.b95*m.b145 + 300*m.b95*m.b146 + 330*m.b95*m.b147 + 374*m.b95*m.b155 + 340*m.b95*
                       m.b156 + 306*m.b95*m.b157 + 272*m.b95*m.b158 + 306*m.b95*m.b159 + 340*m.b95*m.b160 + 374*m.b95*
                       m.b161 + 154*m.b95*m.b162 + 140*m.b95*m.b163 + 126*m.b95*m.b164 + 112*m.b95*m.b165 + 126*m.b95*
                       m.b166 + 140*m.b95*m.b167 + 154*m.b95*m.b168 + 253*m.b95*m.b197 + 230*m.b95*m.b198 + 207*m.b95*
                       m.b199 + 184*m.b95*m.b200 + 207*m.b95*m.b201 + 230*m.b95*m.b202 + 253*m.b95*m.b203 + 372*m.b96*
                       m.b106 + 341*m.b96*m.b107 + 310*m.b96*m.b108 + 279*m.b96*m.b109 + 248*m.b96*m.b110 + 279*m.b96*
                       m.b111 + 310*m.b96*m.b112 + 408*m.b96*m.b134 + 374*m.b96*m.b135 + 340*m.b96*m.b136 + 306*m.b96*
                       m.b137 + 272*m.b96*m.b138 + 306*m.b96*m.b139 + 340*m.b96*m.b140 + 360*m.b96*m.b141 + 330*m.b96*
                       m.b142 + 300*m.b96*m.b143 + 270*m.b96*m.b144 + 240*m.b96*m.b145 + 270*m.b96*m.b146 + 300*m.b96*
                       m.b147 + 408*m.b96*m.b155 + 374*m.b96*m.b156 + 340*m.b96*m.b157 + 306*m.b96*m.b158 + 272*m.b96*
                       m.b159 + 306*m.b96*m.b160 + 340*m.b96*m.b161 + 168*m.b96*m.b162 + 154*m.b96*m.b163 + 140*m.b96*
                       m.b164 + 126*m.b96*m.b165 + 112*m.b96*m.b166 + 126*m.b96*m.b167 + 140*m.b96*m.b168 + 276*m.b96*
                       m.b197 + 253*m.b96*m.b198 + 230*m.b96*m.b199 + 207*m.b96*m.b200 + 184*m.b96*m.b201 + 207*m.b96*
                       m.b202 + 230*m.b96*m.b203 + 403*m.b97*m.b106 + 372*m.b97*m.b107 + 341*m.b97*m.b108 + 310*m.b97*
                       m.b109 + 279*m.b97*m.b110 + 248*m.b97*m.b111 + 279*m.b97*m.b112 + 442*m.b97*m.b134 + 408*m.b97*
                       m.b135 + 374*m.b97*m.b136 + 340*m.b97*m.b137 + 306*m.b97*m.b138 + 272*m.b97*m.b139 + 306*m.b97*
                       m.b140 + 390*m.b97*m.b141 + 360*m.b97*m.b142 + 330*m.b97*m.b143 + 300*m.b97*m.b144 + 270*m.b97*
                       m.b145 + 240*m.b97*m.b146 + 270*m.b97*m.b147 + 442*m.b97*m.b155 + 408*m.b97*m.b156 + 374*m.b97*
                       m.b157 + 340*m.b97*m.b158 + 306*m.b97*m.b159 + 272*m.b97*m.b160 + 306*m.b97*m.b161 + 182*m.b97*
                       m.b162 + 168*m.b97*m.b163 + 154*m.b97*m.b164 + 140*m.b97*m.b165 + 126*m.b97*m.b166 + 112*m.b97*
                       m.b167 + 126*m.b97*m.b168 + 299*m.b97*m.b197 + 276*m.b97*m.b198 + 253*m.b97*m.b199 + 230*m.b97*
                       m.b200 + 207*m.b97*m.b201 + 184*m.b97*m.b202 + 207*m.b97*m.b203 + 434*m.b98*m.b106 + 403*m.b98*
                       m.b107 + 372*m.b98*m.b108 + 341*m.b98*m.b109 + 310*m.b98*m.b110 + 279*m.b98*m.b111 + 248*m.b98*
                       m.b112 + 476*m.b98*m.b134 + 442*m.b98*m.b135 + 408*m.b98*m.b136 + 374*m.b98*m.b137 + 340*m.b98*
                       m.b138 + 306*m.b98*m.b139 + 272*m.b98*m.b140 + 420*m.b98*m.b141 + 390*m.b98*m.b142 + 360*m.b98*
                       m.b143 + 330*m.b98*m.b144 + 300*m.b98*m.b145 + 270*m.b98*m.b146 + 240*m.b98*m.b147 + 476*m.b98*
                       m.b155 + 442*m.b98*m.b156 + 408*m.b98*m.b157 + 374*m.b98*m.b158 + 340*m.b98*m.b159 + 306*m.b98*
                       m.b160 + 272*m.b98*m.b161 + 196*m.b98*m.b162 + 182*m.b98*m.b163 + 168*m.b98*m.b164 + 154*m.b98*
                       m.b165 + 140*m.b98*m.b166 + 126*m.b98*m.b167 + 112*m.b98*m.b168 + 322*m.b98*m.b197 + 299*m.b98*
                       m.b198 + 276*m.b98*m.b199 + 253*m.b98*m.b200 + 230*m.b98*m.b201 + 207*m.b98*m.b202 + 184*m.b98*
                       m.b203 + 328*m.b99*m.b113 + 369*m.b99*m.b114 + 410*m.b99*m.b115 + 451*m.b99*m.b116 + 492*m.b99*
                       m.b117 + 533*m.b99*m.b118 + 574*m.b99*m.b119 + 256*m.b99*m.b176 + 288*m.b99*m.b177 + 320*m.b99*
                       m.b178 + 352*m.b99*m.b179 + 384*m.b99*m.b180 + 416*m.b99*m.b181 + 448*m.b99*m.b182 + 200*m.b99*
                       m.b190 + 225*m.b99*m.b191 + 250*m.b99*m.b192 + 275*m.b99*m.b193 + 300*m.b99*m.b194 + 325*m.b99*
                       m.b195 + 350*m.b99*m.b196 + 369*m.b100*m.b113 + 328*m.b100*m.b114 + 369*m.b100*m.b115 + 410*
                       m.b100*m.b116 + 451*m.b100*m.b117 + 492*m.b100*m.b118 + 533*m.b100*m.b119 + 288*m.b100*m.b176 + 
                       256*m.b100*m.b177 + 288*m.b100*m.b178 + 320*m.b100*m.b179 + 352*m.b100*m.b180 + 384*m.b100*m.b181
                        + 416*m.b100*m.b182 + 225*m.b100*m.b190 + 200*m.b100*m.b191 + 225*m.b100*m.b192 + 250*m.b100*
                       m.b193 + 275*m.b100*m.b194 + 300*m.b100*m.b195 + 325*m.b100*m.b196 + 410*m.b101*m.b113 + 369*
                       m.b101*m.b114 + 328*m.b101*m.b115 + 369*m.b101*m.b116 + 410*m.b101*m.b117 + 451*m.b101*m.b118 + 
                       492*m.b101*m.b119 + 320*m.b101*m.b176 + 288*m.b101*m.b177 + 256*m.b101*m.b178 + 288*m.b101*m.b179
                        + 320*m.b101*m.b180 + 352*m.b101*m.b181 + 384*m.b101*m.b182 + 250*m.b101*m.b190 + 225*m.b101*
                       m.b191 + 200*m.b101*m.b192 + 225*m.b101*m.b193 + 250*m.b101*m.b194 + 275*m.b101*m.b195 + 300*
                       m.b101*m.b196 + 451*m.b102*m.b113 + 410*m.b102*m.b114 + 369*m.b102*m.b115 + 328*m.b102*m.b116 + 
                       369*m.b102*m.b117 + 410*m.b102*m.b118 + 451*m.b102*m.b119 + 352*m.b102*m.b176 + 320*m.b102*m.b177
                        + 288*m.b102*m.b178 + 256*m.b102*m.b179 + 288*m.b102*m.b180 + 320*m.b102*m.b181 + 352*m.b102*
                       m.b182 + 275*m.b102*m.b190 + 250*m.b102*m.b191 + 225*m.b102*m.b192 + 200*m.b102*m.b193 + 225*
                       m.b102*m.b194 + 250*m.b102*m.b195 + 275*m.b102*m.b196 + 492*m.b103*m.b113 + 451*m.b103*m.b114 + 
                       410*m.b103*m.b115 + 369*m.b103*m.b116 + 328*m.b103*m.b117 + 369*m.b103*m.b118 + 410*m.b103*m.b119
                        + 384*m.b103*m.b176 + 352*m.b103*m.b177 + 320*m.b103*m.b178 + 288*m.b103*m.b179 + 256*m.b103*
                       m.b180 + 288*m.b103*m.b181 + 320*m.b103*m.b182 + 300*m.b103*m.b190 + 275*m.b103*m.b191 + 250*
                       m.b103*m.b192 + 225*m.b103*m.b193 + 200*m.b103*m.b194 + 225*m.b103*m.b195 + 250*m.b103*m.b196 + 
                       533*m.b104*m.b113 + 492*m.b104*m.b114 + 451*m.b104*m.b115 + 410*m.b104*m.b116 + 369*m.b104*m.b117
                        + 328*m.b104*m.b118 + 369*m.b104*m.b119 + 416*m.b104*m.b176 + 384*m.b104*m.b177 + 352*m.b104*
                       m.b178 + 320*m.b104*m.b179 + 288*m.b104*m.b180 + 256*m.b104*m.b181 + 288*m.b104*m.b182 + 325*
                       m.b104*m.b190 + 300*m.b104*m.b191 + 275*m.b104*m.b192 + 250*m.b104*m.b193 + 225*m.b104*m.b194 + 
                       200*m.b104*m.b195 + 225*m.b104*m.b196 + 574*m.b105*m.b113 + 533*m.b105*m.b114 + 492*m.b105*m.b115
                        + 451*m.b105*m.b116 + 410*m.b105*m.b117 + 369*m.b105*m.b118 + 328*m.b105*m.b119 + 448*m.b105*
                       m.b176 + 416*m.b105*m.b177 + 384*m.b105*m.b178 + 352*m.b105*m.b179 + 320*m.b105*m.b180 + 288*
                       m.b105*m.b181 + 256*m.b105*m.b182 + 350*m.b105*m.b190 + 325*m.b105*m.b191 + 300*m.b105*m.b192 + 
                       275*m.b105*m.b193 + 250*m.b105*m.b194 + 225*m.b105*m.b195 + 200*m.b105*m.b196, sense=minimize)

m.c2 = Constraint(expr=   m.b1 + m.b2 + m.b3 + m.b4 + m.b5 + m.b6 + m.b7 == 1)

m.c3 = Constraint(expr=   m.b8 + m.b9 + m.b10 + m.b11 + m.b12 + m.b13 + m.b14 == 1)

m.c4 = Constraint(expr=   m.b15 + m.b16 + m.b17 + m.b18 + m.b19 + m.b20 + m.b21 == 1)

m.c5 = Constraint(expr=   m.b22 + m.b23 + m.b24 + m.b25 + m.b26 + m.b27 + m.b28 == 1)

m.c6 = Constraint(expr=   m.b29 + m.b30 + m.b31 + m.b32 + m.b33 + m.b34 + m.b35 == 1)

m.c7 = Constraint(expr=   m.b36 + m.b37 + m.b38 + m.b39 + m.b40 + m.b41 + m.b42 == 1)

m.c8 = Constraint(expr=   m.b43 + m.b44 + m.b45 + m.b46 + m.b47 + m.b48 + m.b49 == 1)

m.c9 = Constraint(expr=   m.b50 + m.b51 + m.b52 + m.b53 + m.b54 + m.b55 + m.b56 == 1)

m.c10 = Constraint(expr=   m.b57 + m.b58 + m.b59 + m.b60 + m.b61 + m.b62 + m.b63 == 1)

m.c11 = Constraint(expr=   m.b64 + m.b65 + m.b66 + m.b67 + m.b68 + m.b69 + m.b70 == 1)

m.c12 = Constraint(expr=   m.b71 + m.b72 + m.b73 + m.b74 + m.b75 + m.b76 + m.b77 == 1)

m.c13 = Constraint(expr=   m.b78 + m.b79 + m.b80 + m.b81 + m.b82 + m.b83 + m.b84 == 1)

m.c14 = Constraint(expr=   m.b85 + m.b86 + m.b87 + m.b88 + m.b89 + m.b90 + m.b91 == 1)

m.c15 = Constraint(expr=   m.b92 + m.b93 + m.b94 + m.b95 + m.b96 + m.b97 + m.b98 == 1)

m.c16 = Constraint(expr=   m.b99 + m.b100 + m.b101 + m.b102 + m.b103 + m.b104 + m.b105 == 1)

m.c17 = Constraint(expr=   m.b106 + m.b107 + m.b108 + m.b109 + m.b110 + m.b111 + m.b112 == 1)

m.c18 = Constraint(expr=   m.b113 + m.b114 + m.b115 + m.b116 + m.b117 + m.b118 + m.b119 == 1)

m.c19 = Constraint(expr=   m.b120 + m.b121 + m.b122 + m.b123 + m.b124 + m.b125 + m.b126 == 1)

m.c20 = Constraint(expr=   m.b127 + m.b128 + m.b129 + m.b130 + m.b131 + m.b132 + m.b133 == 1)

m.c21 = Constraint(expr=   m.b134 + m.b135 + m.b136 + m.b137 + m.b138 + m.b139 + m.b140 == 1)

m.c22 = Constraint(expr=   m.b141 + m.b142 + m.b143 + m.b144 + m.b145 + m.b146 + m.b147 == 1)

m.c23 = Constraint(expr=   m.b148 + m.b149 + m.b150 + m.b151 + m.b152 + m.b153 + m.b154 == 1)

m.c24 = Constraint(expr=   m.b155 + m.b156 + m.b157 + m.b158 + m.b159 + m.b160 + m.b161 == 1)

m.c25 = Constraint(expr=   m.b162 + m.b163 + m.b164 + m.b165 + m.b166 + m.b167 + m.b168 == 1)

m.c26 = Constraint(expr=   m.b169 + m.b170 + m.b171 + m.b172 + m.b173 + m.b174 + m.b175 == 1)

m.c27 = Constraint(expr=   m.b176 + m.b177 + m.b178 + m.b179 + m.b180 + m.b181 + m.b182 == 1)

m.c28 = Constraint(expr=   m.b183 + m.b184 + m.b185 + m.b186 + m.b187 + m.b188 + m.b189 == 1)

m.c29 = Constraint(expr=   m.b190 + m.b191 + m.b192 + m.b193 + m.b194 + m.b195 + m.b196 == 1)

m.c30 = Constraint(expr=   m.b197 + m.b198 + m.b199 + m.b200 + m.b201 + m.b202 + m.b203 == 1)

m.c31 = Constraint(expr=   m.b204 + m.b205 + m.b206 + m.b207 + m.b208 + m.b209 + m.b210 == 1)

m.c32 = Constraint(expr=   130*m.b1 + 84*m.b8 + 63*m.b15 + 233*m.b22 + 103*m.b29 + 118*m.b36 + 62*m.b43 + 62*m.b50
                         + 138*m.b57 + 129*m.b64 + 25*m.b71 + 120*m.b78 + 93*m.b85 + 166*m.b92 + 98*m.b99 <= 302)

m.c33 = Constraint(expr=   130*m.b2 + 84*m.b9 + 63*m.b16 + 233*m.b23 + 103*m.b30 + 118*m.b37 + 62*m.b44 + 62*m.b51
                         + 138*m.b58 + 129*m.b65 + 25*m.b72 + 120*m.b79 + 93*m.b86 + 166*m.b93 + 98*m.b100 <= 302)

m.c34 = Constraint(expr=   130*m.b3 + 84*m.b10 + 63*m.b17 + 233*m.b24 + 103*m.b31 + 118*m.b38 + 62*m.b45 + 62*m.b52
                         + 138*m.b59 + 129*m.b66 + 25*m.b73 + 120*m.b80 + 93*m.b87 + 166*m.b94 + 98*m.b101 <= 302)

m.c35 = Constraint(expr=   130*m.b4 + 84*m.b11 + 63*m.b18 + 233*m.b25 + 103*m.b32 + 118*m.b39 + 62*m.b46 + 62*m.b53
                         + 138*m.b60 + 129*m.b67 + 25*m.b74 + 120*m.b81 + 93*m.b88 + 166*m.b95 + 98*m.b102 <= 302)

m.c36 = Constraint(expr=   130*m.b5 + 84*m.b12 + 63*m.b19 + 233*m.b26 + 103*m.b33 + 118*m.b40 + 62*m.b47 + 62*m.b54
                         + 138*m.b61 + 129*m.b68 + 25*m.b75 + 120*m.b82 + 93*m.b89 + 166*m.b96 + 98*m.b103 <= 302)

m.c37 = Constraint(expr=   130*m.b6 + 84*m.b13 + 63*m.b20 + 233*m.b27 + 103*m.b34 + 118*m.b41 + 62*m.b48 + 62*m.b55
                         + 138*m.b62 + 129*m.b69 + 25*m.b76 + 120*m.b83 + 93*m.b90 + 166*m.b97 + 98*m.b104 <= 302)

m.c38 = Constraint(expr=   130*m.b7 + 84*m.b14 + 63*m.b21 + 233*m.b28 + 103*m.b35 + 118*m.b42 + 62*m.b49 + 62*m.b56
                         + 138*m.b63 + 129*m.b70 + 25*m.b77 + 120*m.b84 + 93*m.b91 + 166*m.b98 + 98*m.b105 <= 302)

m.c39 = Constraint(expr=   112*m.b106 + 158*m.b113 + 128*m.b120 + 35*m.b127 + 34*m.b134 + 160*m.b141 + 121*m.b148
                         + 178*m.b155 + 118*m.b162 + 38*m.b169 + 102*m.b176 + 87*m.b183 + 79*m.b190 + 66*m.b197
                         + 208*m.b204 <= 302)

m.c40 = Constraint(expr=   112*m.b107 + 158*m.b114 + 128*m.b121 + 35*m.b128 + 34*m.b135 + 160*m.b142 + 121*m.b149
                         + 178*m.b156 + 118*m.b163 + 38*m.b170 + 102*m.b177 + 87*m.b184 + 79*m.b191 + 66*m.b198
                         + 208*m.b205 <= 302)

m.c41 = Constraint(expr=   112*m.b108 + 158*m.b115 + 128*m.b122 + 35*m.b129 + 34*m.b136 + 160*m.b143 + 121*m.b150
                         + 178*m.b157 + 118*m.b164 + 38*m.b171 + 102*m.b178 + 87*m.b185 + 79*m.b192 + 66*m.b199
                         + 208*m.b206 <= 302)

m.c42 = Constraint(expr=   112*m.b109 + 158*m.b116 + 128*m.b123 + 35*m.b130 + 34*m.b137 + 160*m.b144 + 121*m.b151
                         + 178*m.b158 + 118*m.b165 + 38*m.b172 + 102*m.b179 + 87*m.b186 + 79*m.b193 + 66*m.b200
                         + 208*m.b207 <= 302)

m.c43 = Constraint(expr=   112*m.b110 + 158*m.b117 + 128*m.b124 + 35*m.b131 + 34*m.b138 + 160*m.b145 + 121*m.b152
                         + 178*m.b159 + 118*m.b166 + 38*m.b173 + 102*m.b180 + 87*m.b187 + 79*m.b194 + 66*m.b201
                         + 208*m.b208 <= 302)

m.c44 = Constraint(expr=   112*m.b111 + 158*m.b118 + 128*m.b125 + 35*m.b132 + 34*m.b139 + 160*m.b146 + 121*m.b153
                         + 178*m.b160 + 118*m.b167 + 38*m.b174 + 102*m.b181 + 87*m.b188 + 79*m.b195 + 66*m.b202
                         + 208*m.b209 <= 302)

m.c45 = Constraint(expr=   112*m.b112 + 158*m.b119 + 128*m.b126 + 35*m.b133 + 34*m.b140 + 160*m.b147 + 121*m.b154
                         + 178*m.b161 + 118*m.b168 + 38*m.b175 + 102*m.b182 + 87*m.b189 + 79*m.b196 + 66*m.b203
                         + 208*m.b210 <= 302)
