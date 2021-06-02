#  MINLP written by GAMS Convert at 04/21/18 13:51:16
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         47       31        0       16        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        241        1      240        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        721      481      240        0
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

m.obj = Objective(expr=368*m.b1*m.b145 + 414*m.b1*m.b146 + 460*m.b1*m.b147 + 506*m.b1*m.b148 + 552*m.b1*m.b149 + 598*
                       m.b1*m.b150 + 644*m.b1*m.b151 + 690*m.b1*m.b152 + 280*m.b1*m.b209 + 315*m.b1*m.b210 + 350*m.b1*
                       m.b211 + 385*m.b1*m.b212 + 420*m.b1*m.b213 + 455*m.b1*m.b214 + 490*m.b1*m.b215 + 525*m.b1*m.b216
                        + 414*m.b2*m.b145 + 368*m.b2*m.b146 + 414*m.b2*m.b147 + 460*m.b2*m.b148 + 506*m.b2*m.b149 + 552*
                       m.b2*m.b150 + 598*m.b2*m.b151 + 644*m.b2*m.b152 + 315*m.b2*m.b209 + 280*m.b2*m.b210 + 315*m.b2*
                       m.b211 + 350*m.b2*m.b212 + 385*m.b2*m.b213 + 420*m.b2*m.b214 + 455*m.b2*m.b215 + 490*m.b2*m.b216
                        + 460*m.b3*m.b145 + 414*m.b3*m.b146 + 368*m.b3*m.b147 + 414*m.b3*m.b148 + 460*m.b3*m.b149 + 506*
                       m.b3*m.b150 + 552*m.b3*m.b151 + 598*m.b3*m.b152 + 350*m.b3*m.b209 + 315*m.b3*m.b210 + 280*m.b3*
                       m.b211 + 315*m.b3*m.b212 + 350*m.b3*m.b213 + 385*m.b3*m.b214 + 420*m.b3*m.b215 + 455*m.b3*m.b216
                        + 506*m.b4*m.b145 + 460*m.b4*m.b146 + 414*m.b4*m.b147 + 368*m.b4*m.b148 + 414*m.b4*m.b149 + 460*
                       m.b4*m.b150 + 506*m.b4*m.b151 + 552*m.b4*m.b152 + 385*m.b4*m.b209 + 350*m.b4*m.b210 + 315*m.b4*
                       m.b211 + 280*m.b4*m.b212 + 315*m.b4*m.b213 + 350*m.b4*m.b214 + 385*m.b4*m.b215 + 420*m.b4*m.b216
                        + 552*m.b5*m.b145 + 506*m.b5*m.b146 + 460*m.b5*m.b147 + 414*m.b5*m.b148 + 368*m.b5*m.b149 + 414*
                       m.b5*m.b150 + 460*m.b5*m.b151 + 506*m.b5*m.b152 + 420*m.b5*m.b209 + 385*m.b5*m.b210 + 350*m.b5*
                       m.b211 + 315*m.b5*m.b212 + 280*m.b5*m.b213 + 315*m.b5*m.b214 + 350*m.b5*m.b215 + 385*m.b5*m.b216
                        + 598*m.b6*m.b145 + 552*m.b6*m.b146 + 506*m.b6*m.b147 + 460*m.b6*m.b148 + 414*m.b6*m.b149 + 368*
                       m.b6*m.b150 + 414*m.b6*m.b151 + 460*m.b6*m.b152 + 455*m.b6*m.b209 + 420*m.b6*m.b210 + 385*m.b6*
                       m.b211 + 350*m.b6*m.b212 + 315*m.b6*m.b213 + 280*m.b6*m.b214 + 315*m.b6*m.b215 + 350*m.b6*m.b216
                        + 644*m.b7*m.b145 + 598*m.b7*m.b146 + 552*m.b7*m.b147 + 506*m.b7*m.b148 + 460*m.b7*m.b149 + 414*
                       m.b7*m.b150 + 368*m.b7*m.b151 + 414*m.b7*m.b152 + 490*m.b7*m.b209 + 455*m.b7*m.b210 + 420*m.b7*
                       m.b211 + 385*m.b7*m.b212 + 350*m.b7*m.b213 + 315*m.b7*m.b214 + 280*m.b7*m.b215 + 315*m.b7*m.b216
                        + 690*m.b8*m.b145 + 644*m.b8*m.b146 + 598*m.b8*m.b147 + 552*m.b8*m.b148 + 506*m.b8*m.b149 + 460*
                       m.b8*m.b150 + 414*m.b8*m.b151 + 368*m.b8*m.b152 + 525*m.b8*m.b209 + 490*m.b8*m.b210 + 455*m.b8*
                       m.b211 + 420*m.b8*m.b212 + 385*m.b8*m.b213 + 350*m.b8*m.b214 + 315*m.b8*m.b215 + 280*m.b8*m.b216
                        + 272*m.b9*m.b161 + 306*m.b9*m.b162 + 340*m.b9*m.b163 + 374*m.b9*m.b164 + 408*m.b9*m.b165 + 442*
                       m.b9*m.b166 + 476*m.b9*m.b167 + 510*m.b9*m.b168 + 160*m.b9*m.b177 + 180*m.b9*m.b178 + 200*m.b9*
                       m.b179 + 220*m.b9*m.b180 + 240*m.b9*m.b181 + 260*m.b9*m.b182 + 280*m.b9*m.b183 + 300*m.b9*m.b184
                        + 128*m.b9*m.b185 + 144*m.b9*m.b186 + 160*m.b9*m.b187 + 176*m.b9*m.b188 + 192*m.b9*m.b189 + 208*
                       m.b9*m.b190 + 224*m.b9*m.b191 + 240*m.b9*m.b192 + 152*m.b9*m.b193 + 171*m.b9*m.b194 + 190*m.b9*
                       m.b195 + 209*m.b9*m.b196 + 228*m.b9*m.b197 + 247*m.b9*m.b198 + 266*m.b9*m.b199 + 285*m.b9*m.b200
                        + 200*m.b9*m.b233 + 225*m.b9*m.b234 + 250*m.b9*m.b235 + 275*m.b9*m.b236 + 300*m.b9*m.b237 + 325*
                       m.b9*m.b238 + 350*m.b9*m.b239 + 375*m.b9*m.b240 + 306*m.b10*m.b161 + 272*m.b10*m.b162 + 306*m.b10
                       *m.b163 + 340*m.b10*m.b164 + 374*m.b10*m.b165 + 408*m.b10*m.b166 + 442*m.b10*m.b167 + 476*m.b10*
                       m.b168 + 180*m.b10*m.b177 + 160*m.b10*m.b178 + 180*m.b10*m.b179 + 200*m.b10*m.b180 + 220*m.b10*
                       m.b181 + 240*m.b10*m.b182 + 260*m.b10*m.b183 + 280*m.b10*m.b184 + 144*m.b10*m.b185 + 128*m.b10*
                       m.b186 + 144*m.b10*m.b187 + 160*m.b10*m.b188 + 176*m.b10*m.b189 + 192*m.b10*m.b190 + 208*m.b10*
                       m.b191 + 224*m.b10*m.b192 + 171*m.b10*m.b193 + 152*m.b10*m.b194 + 171*m.b10*m.b195 + 190*m.b10*
                       m.b196 + 209*m.b10*m.b197 + 228*m.b10*m.b198 + 247*m.b10*m.b199 + 266*m.b10*m.b200 + 225*m.b10*
                       m.b233 + 200*m.b10*m.b234 + 225*m.b10*m.b235 + 250*m.b10*m.b236 + 275*m.b10*m.b237 + 300*m.b10*
                       m.b238 + 325*m.b10*m.b239 + 350*m.b10*m.b240 + 340*m.b11*m.b161 + 306*m.b11*m.b162 + 272*m.b11*
                       m.b163 + 306*m.b11*m.b164 + 340*m.b11*m.b165 + 374*m.b11*m.b166 + 408*m.b11*m.b167 + 442*m.b11*
                       m.b168 + 200*m.b11*m.b177 + 180*m.b11*m.b178 + 160*m.b11*m.b179 + 180*m.b11*m.b180 + 200*m.b11*
                       m.b181 + 220*m.b11*m.b182 + 240*m.b11*m.b183 + 260*m.b11*m.b184 + 160*m.b11*m.b185 + 144*m.b11*
                       m.b186 + 128*m.b11*m.b187 + 144*m.b11*m.b188 + 160*m.b11*m.b189 + 176*m.b11*m.b190 + 192*m.b11*
                       m.b191 + 208*m.b11*m.b192 + 190*m.b11*m.b193 + 171*m.b11*m.b194 + 152*m.b11*m.b195 + 171*m.b11*
                       m.b196 + 190*m.b11*m.b197 + 209*m.b11*m.b198 + 228*m.b11*m.b199 + 247*m.b11*m.b200 + 250*m.b11*
                       m.b233 + 225*m.b11*m.b234 + 200*m.b11*m.b235 + 225*m.b11*m.b236 + 250*m.b11*m.b237 + 275*m.b11*
                       m.b238 + 300*m.b11*m.b239 + 325*m.b11*m.b240 + 374*m.b12*m.b161 + 340*m.b12*m.b162 + 306*m.b12*
                       m.b163 + 272*m.b12*m.b164 + 306*m.b12*m.b165 + 340*m.b12*m.b166 + 374*m.b12*m.b167 + 408*m.b12*
                       m.b168 + 220*m.b12*m.b177 + 200*m.b12*m.b178 + 180*m.b12*m.b179 + 160*m.b12*m.b180 + 180*m.b12*
                       m.b181 + 200*m.b12*m.b182 + 220*m.b12*m.b183 + 240*m.b12*m.b184 + 176*m.b12*m.b185 + 160*m.b12*
                       m.b186 + 144*m.b12*m.b187 + 128*m.b12*m.b188 + 144*m.b12*m.b189 + 160*m.b12*m.b190 + 176*m.b12*
                       m.b191 + 192*m.b12*m.b192 + 209*m.b12*m.b193 + 190*m.b12*m.b194 + 171*m.b12*m.b195 + 152*m.b12*
                       m.b196 + 171*m.b12*m.b197 + 190*m.b12*m.b198 + 209*m.b12*m.b199 + 228*m.b12*m.b200 + 275*m.b12*
                       m.b233 + 250*m.b12*m.b234 + 225*m.b12*m.b235 + 200*m.b12*m.b236 + 225*m.b12*m.b237 + 250*m.b12*
                       m.b238 + 275*m.b12*m.b239 + 300*m.b12*m.b240 + 408*m.b13*m.b161 + 374*m.b13*m.b162 + 340*m.b13*
                       m.b163 + 306*m.b13*m.b164 + 272*m.b13*m.b165 + 306*m.b13*m.b166 + 340*m.b13*m.b167 + 374*m.b13*
                       m.b168 + 240*m.b13*m.b177 + 220*m.b13*m.b178 + 200*m.b13*m.b179 + 180*m.b13*m.b180 + 160*m.b13*
                       m.b181 + 180*m.b13*m.b182 + 200*m.b13*m.b183 + 220*m.b13*m.b184 + 192*m.b13*m.b185 + 176*m.b13*
                       m.b186 + 160*m.b13*m.b187 + 144*m.b13*m.b188 + 128*m.b13*m.b189 + 144*m.b13*m.b190 + 160*m.b13*
                       m.b191 + 176*m.b13*m.b192 + 228*m.b13*m.b193 + 209*m.b13*m.b194 + 190*m.b13*m.b195 + 171*m.b13*
                       m.b196 + 152*m.b13*m.b197 + 171*m.b13*m.b198 + 190*m.b13*m.b199 + 209*m.b13*m.b200 + 300*m.b13*
                       m.b233 + 275*m.b13*m.b234 + 250*m.b13*m.b235 + 225*m.b13*m.b236 + 200*m.b13*m.b237 + 225*m.b13*
                       m.b238 + 250*m.b13*m.b239 + 275*m.b13*m.b240 + 442*m.b14*m.b161 + 408*m.b14*m.b162 + 374*m.b14*
                       m.b163 + 340*m.b14*m.b164 + 306*m.b14*m.b165 + 272*m.b14*m.b166 + 306*m.b14*m.b167 + 340*m.b14*
                       m.b168 + 260*m.b14*m.b177 + 240*m.b14*m.b178 + 220*m.b14*m.b179 + 200*m.b14*m.b180 + 180*m.b14*
                       m.b181 + 160*m.b14*m.b182 + 180*m.b14*m.b183 + 200*m.b14*m.b184 + 208*m.b14*m.b185 + 192*m.b14*
                       m.b186 + 176*m.b14*m.b187 + 160*m.b14*m.b188 + 144*m.b14*m.b189 + 128*m.b14*m.b190 + 144*m.b14*
                       m.b191 + 160*m.b14*m.b192 + 247*m.b14*m.b193 + 228*m.b14*m.b194 + 209*m.b14*m.b195 + 190*m.b14*
                       m.b196 + 171*m.b14*m.b197 + 152*m.b14*m.b198 + 171*m.b14*m.b199 + 190*m.b14*m.b200 + 325*m.b14*
                       m.b233 + 300*m.b14*m.b234 + 275*m.b14*m.b235 + 250*m.b14*m.b236 + 225*m.b14*m.b237 + 200*m.b14*
                       m.b238 + 225*m.b14*m.b239 + 250*m.b14*m.b240 + 476*m.b15*m.b161 + 442*m.b15*m.b162 + 408*m.b15*
                       m.b163 + 374*m.b15*m.b164 + 340*m.b15*m.b165 + 306*m.b15*m.b166 + 272*m.b15*m.b167 + 306*m.b15*
                       m.b168 + 280*m.b15*m.b177 + 260*m.b15*m.b178 + 240*m.b15*m.b179 + 220*m.b15*m.b180 + 200*m.b15*
                       m.b181 + 180*m.b15*m.b182 + 160*m.b15*m.b183 + 180*m.b15*m.b184 + 224*m.b15*m.b185 + 208*m.b15*
                       m.b186 + 192*m.b15*m.b187 + 176*m.b15*m.b188 + 160*m.b15*m.b189 + 144*m.b15*m.b190 + 128*m.b15*
                       m.b191 + 144*m.b15*m.b192 + 266*m.b15*m.b193 + 247*m.b15*m.b194 + 228*m.b15*m.b195 + 209*m.b15*
                       m.b196 + 190*m.b15*m.b197 + 171*m.b15*m.b198 + 152*m.b15*m.b199 + 171*m.b15*m.b200 + 350*m.b15*
                       m.b233 + 325*m.b15*m.b234 + 300*m.b15*m.b235 + 275*m.b15*m.b236 + 250*m.b15*m.b237 + 225*m.b15*
                       m.b238 + 200*m.b15*m.b239 + 225*m.b15*m.b240 + 510*m.b16*m.b161 + 476*m.b16*m.b162 + 442*m.b16*
                       m.b163 + 408*m.b16*m.b164 + 374*m.b16*m.b165 + 340*m.b16*m.b166 + 306*m.b16*m.b167 + 272*m.b16*
                       m.b168 + 300*m.b16*m.b177 + 280*m.b16*m.b178 + 260*m.b16*m.b179 + 240*m.b16*m.b180 + 220*m.b16*
                       m.b181 + 200*m.b16*m.b182 + 180*m.b16*m.b183 + 160*m.b16*m.b184 + 240*m.b16*m.b185 + 224*m.b16*
                       m.b186 + 208*m.b16*m.b187 + 192*m.b16*m.b188 + 176*m.b16*m.b189 + 160*m.b16*m.b190 + 144*m.b16*
                       m.b191 + 128*m.b16*m.b192 + 285*m.b16*m.b193 + 266*m.b16*m.b194 + 247*m.b16*m.b195 + 228*m.b16*
                       m.b196 + 209*m.b16*m.b197 + 190*m.b16*m.b198 + 171*m.b16*m.b199 + 152*m.b16*m.b200 + 375*m.b16*
                       m.b233 + 350*m.b16*m.b234 + 325*m.b16*m.b235 + 300*m.b16*m.b236 + 275*m.b16*m.b237 + 250*m.b16*
                       m.b238 + 225*m.b16*m.b239 + 200*m.b16*m.b240 + 240*m.b17*m.b169 + 270*m.b17*m.b170 + 300*m.b17*
                       m.b171 + 330*m.b17*m.b172 + 360*m.b17*m.b173 + 390*m.b17*m.b174 + 420*m.b17*m.b175 + 450*m.b17*
                       m.b176 + 224*m.b17*m.b193 + 252*m.b17*m.b194 + 280*m.b17*m.b195 + 308*m.b17*m.b196 + 336*m.b17*
                       m.b197 + 364*m.b17*m.b198 + 392*m.b17*m.b199 + 420*m.b17*m.b200 + 200*m.b17*m.b201 + 225*m.b17*
                       m.b202 + 250*m.b17*m.b203 + 275*m.b17*m.b204 + 300*m.b17*m.b205 + 325*m.b17*m.b206 + 350*m.b17*
                       m.b207 + 375*m.b17*m.b208 + 136*m.b17*m.b209 + 153*m.b17*m.b210 + 170*m.b17*m.b211 + 187*m.b17*
                       m.b212 + 204*m.b17*m.b213 + 221*m.b17*m.b214 + 238*m.b17*m.b215 + 255*m.b17*m.b216 + 270*m.b18*
                       m.b169 + 240*m.b18*m.b170 + 270*m.b18*m.b171 + 300*m.b18*m.b172 + 330*m.b18*m.b173 + 360*m.b18*
                       m.b174 + 390*m.b18*m.b175 + 420*m.b18*m.b176 + 252*m.b18*m.b193 + 224*m.b18*m.b194 + 252*m.b18*
                       m.b195 + 280*m.b18*m.b196 + 308*m.b18*m.b197 + 336*m.b18*m.b198 + 364*m.b18*m.b199 + 392*m.b18*
                       m.b200 + 225*m.b18*m.b201 + 200*m.b18*m.b202 + 225*m.b18*m.b203 + 250*m.b18*m.b204 + 275*m.b18*
                       m.b205 + 300*m.b18*m.b206 + 325*m.b18*m.b207 + 350*m.b18*m.b208 + 153*m.b18*m.b209 + 136*m.b18*
                       m.b210 + 153*m.b18*m.b211 + 170*m.b18*m.b212 + 187*m.b18*m.b213 + 204*m.b18*m.b214 + 221*m.b18*
                       m.b215 + 238*m.b18*m.b216 + 300*m.b19*m.b169 + 270*m.b19*m.b170 + 240*m.b19*m.b171 + 270*m.b19*
                       m.b172 + 300*m.b19*m.b173 + 330*m.b19*m.b174 + 360*m.b19*m.b175 + 390*m.b19*m.b176 + 280*m.b19*
                       m.b193 + 252*m.b19*m.b194 + 224*m.b19*m.b195 + 252*m.b19*m.b196 + 280*m.b19*m.b197 + 308*m.b19*
                       m.b198 + 336*m.b19*m.b199 + 364*m.b19*m.b200 + 250*m.b19*m.b201 + 225*m.b19*m.b202 + 200*m.b19*
                       m.b203 + 225*m.b19*m.b204 + 250*m.b19*m.b205 + 275*m.b19*m.b206 + 300*m.b19*m.b207 + 325*m.b19*
                       m.b208 + 170*m.b19*m.b209 + 153*m.b19*m.b210 + 136*m.b19*m.b211 + 153*m.b19*m.b212 + 170*m.b19*
                       m.b213 + 187*m.b19*m.b214 + 204*m.b19*m.b215 + 221*m.b19*m.b216 + 330*m.b20*m.b169 + 300*m.b20*
                       m.b170 + 270*m.b20*m.b171 + 240*m.b20*m.b172 + 270*m.b20*m.b173 + 300*m.b20*m.b174 + 330*m.b20*
                       m.b175 + 360*m.b20*m.b176 + 308*m.b20*m.b193 + 280*m.b20*m.b194 + 252*m.b20*m.b195 + 224*m.b20*
                       m.b196 + 252*m.b20*m.b197 + 280*m.b20*m.b198 + 308*m.b20*m.b199 + 336*m.b20*m.b200 + 275*m.b20*
                       m.b201 + 250*m.b20*m.b202 + 225*m.b20*m.b203 + 200*m.b20*m.b204 + 225*m.b20*m.b205 + 250*m.b20*
                       m.b206 + 275*m.b20*m.b207 + 300*m.b20*m.b208 + 187*m.b20*m.b209 + 170*m.b20*m.b210 + 153*m.b20*
                       m.b211 + 136*m.b20*m.b212 + 153*m.b20*m.b213 + 170*m.b20*m.b214 + 187*m.b20*m.b215 + 204*m.b20*
                       m.b216 + 360*m.b21*m.b169 + 330*m.b21*m.b170 + 300*m.b21*m.b171 + 270*m.b21*m.b172 + 240*m.b21*
                       m.b173 + 270*m.b21*m.b174 + 300*m.b21*m.b175 + 330*m.b21*m.b176 + 336*m.b21*m.b193 + 308*m.b21*
                       m.b194 + 280*m.b21*m.b195 + 252*m.b21*m.b196 + 224*m.b21*m.b197 + 252*m.b21*m.b198 + 280*m.b21*
                       m.b199 + 308*m.b21*m.b200 + 300*m.b21*m.b201 + 275*m.b21*m.b202 + 250*m.b21*m.b203 + 225*m.b21*
                       m.b204 + 200*m.b21*m.b205 + 225*m.b21*m.b206 + 250*m.b21*m.b207 + 275*m.b21*m.b208 + 204*m.b21*
                       m.b209 + 187*m.b21*m.b210 + 170*m.b21*m.b211 + 153*m.b21*m.b212 + 136*m.b21*m.b213 + 153*m.b21*
                       m.b214 + 170*m.b21*m.b215 + 187*m.b21*m.b216 + 390*m.b22*m.b169 + 360*m.b22*m.b170 + 330*m.b22*
                       m.b171 + 300*m.b22*m.b172 + 270*m.b22*m.b173 + 240*m.b22*m.b174 + 270*m.b22*m.b175 + 300*m.b22*
                       m.b176 + 364*m.b22*m.b193 + 336*m.b22*m.b194 + 308*m.b22*m.b195 + 280*m.b22*m.b196 + 252*m.b22*
                       m.b197 + 224*m.b22*m.b198 + 252*m.b22*m.b199 + 280*m.b22*m.b200 + 325*m.b22*m.b201 + 300*m.b22*
                       m.b202 + 275*m.b22*m.b203 + 250*m.b22*m.b204 + 225*m.b22*m.b205 + 200*m.b22*m.b206 + 225*m.b22*
                       m.b207 + 250*m.b22*m.b208 + 221*m.b22*m.b209 + 204*m.b22*m.b210 + 187*m.b22*m.b211 + 170*m.b22*
                       m.b212 + 153*m.b22*m.b213 + 136*m.b22*m.b214 + 153*m.b22*m.b215 + 170*m.b22*m.b216 + 420*m.b23*
                       m.b169 + 390*m.b23*m.b170 + 360*m.b23*m.b171 + 330*m.b23*m.b172 + 300*m.b23*m.b173 + 270*m.b23*
                       m.b174 + 240*m.b23*m.b175 + 270*m.b23*m.b176 + 392*m.b23*m.b193 + 364*m.b23*m.b194 + 336*m.b23*
                       m.b195 + 308*m.b23*m.b196 + 280*m.b23*m.b197 + 252*m.b23*m.b198 + 224*m.b23*m.b199 + 252*m.b23*
                       m.b200 + 350*m.b23*m.b201 + 325*m.b23*m.b202 + 300*m.b23*m.b203 + 275*m.b23*m.b204 + 250*m.b23*
                       m.b205 + 225*m.b23*m.b206 + 200*m.b23*m.b207 + 225*m.b23*m.b208 + 238*m.b23*m.b209 + 221*m.b23*
                       m.b210 + 204*m.b23*m.b211 + 187*m.b23*m.b212 + 170*m.b23*m.b213 + 153*m.b23*m.b214 + 136*m.b23*
                       m.b215 + 153*m.b23*m.b216 + 450*m.b24*m.b169 + 420*m.b24*m.b170 + 390*m.b24*m.b171 + 360*m.b24*
                       m.b172 + 330*m.b24*m.b173 + 300*m.b24*m.b174 + 270*m.b24*m.b175 + 240*m.b24*m.b176 + 420*m.b24*
                       m.b193 + 392*m.b24*m.b194 + 364*m.b24*m.b195 + 336*m.b24*m.b196 + 308*m.b24*m.b197 + 280*m.b24*
                       m.b198 + 252*m.b24*m.b199 + 224*m.b24*m.b200 + 375*m.b24*m.b201 + 350*m.b24*m.b202 + 325*m.b24*
                       m.b203 + 300*m.b24*m.b204 + 275*m.b24*m.b205 + 250*m.b24*m.b206 + 225*m.b24*m.b207 + 200*m.b24*
                       m.b208 + 255*m.b24*m.b209 + 238*m.b24*m.b210 + 221*m.b24*m.b211 + 204*m.b24*m.b212 + 187*m.b24*
                       m.b213 + 170*m.b24*m.b214 + 153*m.b24*m.b215 + 136*m.b24*m.b216 + 160*m.b25*m.b145 + 180*m.b25*
                       m.b146 + 200*m.b25*m.b147 + 220*m.b25*m.b148 + 240*m.b25*m.b149 + 260*m.b25*m.b150 + 280*m.b25*
                       m.b151 + 300*m.b25*m.b152 + 240*m.b25*m.b161 + 270*m.b25*m.b162 + 300*m.b25*m.b163 + 330*m.b25*
                       m.b164 + 360*m.b25*m.b165 + 390*m.b25*m.b166 + 420*m.b25*m.b167 + 450*m.b25*m.b168 + 180*m.b26*
                       m.b145 + 160*m.b26*m.b146 + 180*m.b26*m.b147 + 200*m.b26*m.b148 + 220*m.b26*m.b149 + 240*m.b26*
                       m.b150 + 260*m.b26*m.b151 + 280*m.b26*m.b152 + 270*m.b26*m.b161 + 240*m.b26*m.b162 + 270*m.b26*
                       m.b163 + 300*m.b26*m.b164 + 330*m.b26*m.b165 + 360*m.b26*m.b166 + 390*m.b26*m.b167 + 420*m.b26*
                       m.b168 + 200*m.b27*m.b145 + 180*m.b27*m.b146 + 160*m.b27*m.b147 + 180*m.b27*m.b148 + 200*m.b27*
                       m.b149 + 220*m.b27*m.b150 + 240*m.b27*m.b151 + 260*m.b27*m.b152 + 300*m.b27*m.b161 + 270*m.b27*
                       m.b162 + 240*m.b27*m.b163 + 270*m.b27*m.b164 + 300*m.b27*m.b165 + 330*m.b27*m.b166 + 360*m.b27*
                       m.b167 + 390*m.b27*m.b168 + 220*m.b28*m.b145 + 200*m.b28*m.b146 + 180*m.b28*m.b147 + 160*m.b28*
                       m.b148 + 180*m.b28*m.b149 + 200*m.b28*m.b150 + 220*m.b28*m.b151 + 240*m.b28*m.b152 + 330*m.b28*
                       m.b161 + 300*m.b28*m.b162 + 270*m.b28*m.b163 + 240*m.b28*m.b164 + 270*m.b28*m.b165 + 300*m.b28*
                       m.b166 + 330*m.b28*m.b167 + 360*m.b28*m.b168 + 240*m.b29*m.b145 + 220*m.b29*m.b146 + 200*m.b29*
                       m.b147 + 180*m.b29*m.b148 + 160*m.b29*m.b149 + 180*m.b29*m.b150 + 200*m.b29*m.b151 + 220*m.b29*
                       m.b152 + 360*m.b29*m.b161 + 330*m.b29*m.b162 + 300*m.b29*m.b163 + 270*m.b29*m.b164 + 240*m.b29*
                       m.b165 + 270*m.b29*m.b166 + 300*m.b29*m.b167 + 330*m.b29*m.b168 + 260*m.b30*m.b145 + 240*m.b30*
                       m.b146 + 220*m.b30*m.b147 + 200*m.b30*m.b148 + 180*m.b30*m.b149 + 160*m.b30*m.b150 + 180*m.b30*
                       m.b151 + 200*m.b30*m.b152 + 390*m.b30*m.b161 + 360*m.b30*m.b162 + 330*m.b30*m.b163 + 300*m.b30*
                       m.b164 + 270*m.b30*m.b165 + 240*m.b30*m.b166 + 270*m.b30*m.b167 + 300*m.b30*m.b168 + 280*m.b31*
                       m.b145 + 260*m.b31*m.b146 + 240*m.b31*m.b147 + 220*m.b31*m.b148 + 200*m.b31*m.b149 + 180*m.b31*
                       m.b150 + 160*m.b31*m.b151 + 180*m.b31*m.b152 + 420*m.b31*m.b161 + 390*m.b31*m.b162 + 360*m.b31*
                       m.b163 + 330*m.b31*m.b164 + 300*m.b31*m.b165 + 270*m.b31*m.b166 + 240*m.b31*m.b167 + 270*m.b31*
                       m.b168 + 300*m.b32*m.b145 + 280*m.b32*m.b146 + 260*m.b32*m.b147 + 240*m.b32*m.b148 + 220*m.b32*
                       m.b149 + 200*m.b32*m.b150 + 180*m.b32*m.b151 + 160*m.b32*m.b152 + 450*m.b32*m.b161 + 420*m.b32*
                       m.b162 + 390*m.b32*m.b163 + 360*m.b32*m.b164 + 330*m.b32*m.b165 + 300*m.b32*m.b166 + 270*m.b32*
                       m.b167 + 240*m.b32*m.b168 + 104*m.b33*m.b121 + 117*m.b33*m.b122 + 130*m.b33*m.b123 + 143*m.b33*
                       m.b124 + 156*m.b33*m.b125 + 169*m.b33*m.b126 + 182*m.b33*m.b127 + 195*m.b33*m.b128 + 304*m.b33*
                       m.b145 + 342*m.b33*m.b146 + 380*m.b33*m.b147 + 418*m.b33*m.b148 + 456*m.b33*m.b149 + 494*m.b33*
                       m.b150 + 532*m.b33*m.b151 + 570*m.b33*m.b152 + 117*m.b34*m.b121 + 104*m.b34*m.b122 + 117*m.b34*
                       m.b123 + 130*m.b34*m.b124 + 143*m.b34*m.b125 + 156*m.b34*m.b126 + 169*m.b34*m.b127 + 182*m.b34*
                       m.b128 + 342*m.b34*m.b145 + 304*m.b34*m.b146 + 342*m.b34*m.b147 + 380*m.b34*m.b148 + 418*m.b34*
                       m.b149 + 456*m.b34*m.b150 + 494*m.b34*m.b151 + 532*m.b34*m.b152 + 130*m.b35*m.b121 + 117*m.b35*
                       m.b122 + 104*m.b35*m.b123 + 117*m.b35*m.b124 + 130*m.b35*m.b125 + 143*m.b35*m.b126 + 156*m.b35*
                       m.b127 + 169*m.b35*m.b128 + 380*m.b35*m.b145 + 342*m.b35*m.b146 + 304*m.b35*m.b147 + 342*m.b35*
                       m.b148 + 380*m.b35*m.b149 + 418*m.b35*m.b150 + 456*m.b35*m.b151 + 494*m.b35*m.b152 + 143*m.b36*
                       m.b121 + 130*m.b36*m.b122 + 117*m.b36*m.b123 + 104*m.b36*m.b124 + 117*m.b36*m.b125 + 130*m.b36*
                       m.b126 + 143*m.b36*m.b127 + 156*m.b36*m.b128 + 418*m.b36*m.b145 + 380*m.b36*m.b146 + 342*m.b36*
                       m.b147 + 304*m.b36*m.b148 + 342*m.b36*m.b149 + 380*m.b36*m.b150 + 418*m.b36*m.b151 + 456*m.b36*
                       m.b152 + 156*m.b37*m.b121 + 143*m.b37*m.b122 + 130*m.b37*m.b123 + 117*m.b37*m.b124 + 104*m.b37*
                       m.b125 + 117*m.b37*m.b126 + 130*m.b37*m.b127 + 143*m.b37*m.b128 + 456*m.b37*m.b145 + 418*m.b37*
                       m.b146 + 380*m.b37*m.b147 + 342*m.b37*m.b148 + 304*m.b37*m.b149 + 342*m.b37*m.b150 + 380*m.b37*
                       m.b151 + 418*m.b37*m.b152 + 169*m.b38*m.b121 + 156*m.b38*m.b122 + 143*m.b38*m.b123 + 130*m.b38*
                       m.b124 + 117*m.b38*m.b125 + 104*m.b38*m.b126 + 117*m.b38*m.b127 + 130*m.b38*m.b128 + 494*m.b38*
                       m.b145 + 456*m.b38*m.b146 + 418*m.b38*m.b147 + 380*m.b38*m.b148 + 342*m.b38*m.b149 + 304*m.b38*
                       m.b150 + 342*m.b38*m.b151 + 380*m.b38*m.b152 + 182*m.b39*m.b121 + 169*m.b39*m.b122 + 156*m.b39*
                       m.b123 + 143*m.b39*m.b124 + 130*m.b39*m.b125 + 117*m.b39*m.b126 + 104*m.b39*m.b127 + 117*m.b39*
                       m.b128 + 532*m.b39*m.b145 + 494*m.b39*m.b146 + 456*m.b39*m.b147 + 418*m.b39*m.b148 + 380*m.b39*
                       m.b149 + 342*m.b39*m.b150 + 304*m.b39*m.b151 + 342*m.b39*m.b152 + 195*m.b40*m.b121 + 182*m.b40*
                       m.b122 + 169*m.b40*m.b123 + 156*m.b40*m.b124 + 143*m.b40*m.b125 + 130*m.b40*m.b126 + 117*m.b40*
                       m.b127 + 104*m.b40*m.b128 + 570*m.b40*m.b145 + 532*m.b40*m.b146 + 494*m.b40*m.b147 + 456*m.b40*
                       m.b148 + 418*m.b40*m.b149 + 380*m.b40*m.b150 + 342*m.b40*m.b151 + 304*m.b40*m.b152 + 392*m.b41*
                       m.b137 + 441*m.b41*m.b138 + 490*m.b41*m.b139 + 539*m.b41*m.b140 + 588*m.b41*m.b141 + 637*m.b41*
                       m.b142 + 686*m.b41*m.b143 + 735*m.b41*m.b144 + 304*m.b41*m.b145 + 342*m.b41*m.b146 + 380*m.b41*
                       m.b147 + 418*m.b41*m.b148 + 456*m.b41*m.b149 + 494*m.b41*m.b150 + 532*m.b41*m.b151 + 570*m.b41*
                       m.b152 + 264*m.b41*m.b161 + 297*m.b41*m.b162 + 330*m.b41*m.b163 + 363*m.b41*m.b164 + 396*m.b41*
                       m.b165 + 429*m.b41*m.b166 + 462*m.b41*m.b167 + 495*m.b41*m.b168 + 160*m.b41*m.b201 + 180*m.b41*
                       m.b202 + 200*m.b41*m.b203 + 220*m.b41*m.b204 + 240*m.b41*m.b205 + 260*m.b41*m.b206 + 280*m.b41*
                       m.b207 + 300*m.b41*m.b208 + 176*m.b41*m.b217 + 198*m.b41*m.b218 + 220*m.b41*m.b219 + 242*m.b41*
                       m.b220 + 264*m.b41*m.b221 + 286*m.b41*m.b222 + 308*m.b41*m.b223 + 330*m.b41*m.b224 + 272*m.b41*
                       m.b233 + 306*m.b41*m.b234 + 340*m.b41*m.b235 + 374*m.b41*m.b236 + 408*m.b41*m.b237 + 442*m.b41*
                       m.b238 + 476*m.b41*m.b239 + 510*m.b41*m.b240 + 441*m.b42*m.b137 + 392*m.b42*m.b138 + 441*m.b42*
                       m.b139 + 490*m.b42*m.b140 + 539*m.b42*m.b141 + 588*m.b42*m.b142 + 637*m.b42*m.b143 + 686*m.b42*
                       m.b144 + 342*m.b42*m.b145 + 304*m.b42*m.b146 + 342*m.b42*m.b147 + 380*m.b42*m.b148 + 418*m.b42*
                       m.b149 + 456*m.b42*m.b150 + 494*m.b42*m.b151 + 532*m.b42*m.b152 + 297*m.b42*m.b161 + 264*m.b42*
                       m.b162 + 297*m.b42*m.b163 + 330*m.b42*m.b164 + 363*m.b42*m.b165 + 396*m.b42*m.b166 + 429*m.b42*
                       m.b167 + 462*m.b42*m.b168 + 180*m.b42*m.b201 + 160*m.b42*m.b202 + 180*m.b42*m.b203 + 200*m.b42*
                       m.b204 + 220*m.b42*m.b205 + 240*m.b42*m.b206 + 260*m.b42*m.b207 + 280*m.b42*m.b208 + 198*m.b42*
                       m.b217 + 176*m.b42*m.b218 + 198*m.b42*m.b219 + 220*m.b42*m.b220 + 242*m.b42*m.b221 + 264*m.b42*
                       m.b222 + 286*m.b42*m.b223 + 308*m.b42*m.b224 + 306*m.b42*m.b233 + 272*m.b42*m.b234 + 306*m.b42*
                       m.b235 + 340*m.b42*m.b236 + 374*m.b42*m.b237 + 408*m.b42*m.b238 + 442*m.b42*m.b239 + 476*m.b42*
                       m.b240 + 490*m.b43*m.b137 + 441*m.b43*m.b138 + 392*m.b43*m.b139 + 441*m.b43*m.b140 + 490*m.b43*
                       m.b141 + 539*m.b43*m.b142 + 588*m.b43*m.b143 + 637*m.b43*m.b144 + 380*m.b43*m.b145 + 342*m.b43*
                       m.b146 + 304*m.b43*m.b147 + 342*m.b43*m.b148 + 380*m.b43*m.b149 + 418*m.b43*m.b150 + 456*m.b43*
                       m.b151 + 494*m.b43*m.b152 + 330*m.b43*m.b161 + 297*m.b43*m.b162 + 264*m.b43*m.b163 + 297*m.b43*
                       m.b164 + 330*m.b43*m.b165 + 363*m.b43*m.b166 + 396*m.b43*m.b167 + 429*m.b43*m.b168 + 200*m.b43*
                       m.b201 + 180*m.b43*m.b202 + 160*m.b43*m.b203 + 180*m.b43*m.b204 + 200*m.b43*m.b205 + 220*m.b43*
                       m.b206 + 240*m.b43*m.b207 + 260*m.b43*m.b208 + 220*m.b43*m.b217 + 198*m.b43*m.b218 + 176*m.b43*
                       m.b219 + 198*m.b43*m.b220 + 220*m.b43*m.b221 + 242*m.b43*m.b222 + 264*m.b43*m.b223 + 286*m.b43*
                       m.b224 + 340*m.b43*m.b233 + 306*m.b43*m.b234 + 272*m.b43*m.b235 + 306*m.b43*m.b236 + 340*m.b43*
                       m.b237 + 374*m.b43*m.b238 + 408*m.b43*m.b239 + 442*m.b43*m.b240 + 539*m.b44*m.b137 + 490*m.b44*
                       m.b138 + 441*m.b44*m.b139 + 392*m.b44*m.b140 + 441*m.b44*m.b141 + 490*m.b44*m.b142 + 539*m.b44*
                       m.b143 + 588*m.b44*m.b144 + 418*m.b44*m.b145 + 380*m.b44*m.b146 + 342*m.b44*m.b147 + 304*m.b44*
                       m.b148 + 342*m.b44*m.b149 + 380*m.b44*m.b150 + 418*m.b44*m.b151 + 456*m.b44*m.b152 + 363*m.b44*
                       m.b161 + 330*m.b44*m.b162 + 297*m.b44*m.b163 + 264*m.b44*m.b164 + 297*m.b44*m.b165 + 330*m.b44*
                       m.b166 + 363*m.b44*m.b167 + 396*m.b44*m.b168 + 220*m.b44*m.b201 + 200*m.b44*m.b202 + 180*m.b44*
                       m.b203 + 160*m.b44*m.b204 + 180*m.b44*m.b205 + 200*m.b44*m.b206 + 220*m.b44*m.b207 + 240*m.b44*
                       m.b208 + 242*m.b44*m.b217 + 220*m.b44*m.b218 + 198*m.b44*m.b219 + 176*m.b44*m.b220 + 198*m.b44*
                       m.b221 + 220*m.b44*m.b222 + 242*m.b44*m.b223 + 264*m.b44*m.b224 + 374*m.b44*m.b233 + 340*m.b44*
                       m.b234 + 306*m.b44*m.b235 + 272*m.b44*m.b236 + 306*m.b44*m.b237 + 340*m.b44*m.b238 + 374*m.b44*
                       m.b239 + 408*m.b44*m.b240 + 588*m.b45*m.b137 + 539*m.b45*m.b138 + 490*m.b45*m.b139 + 441*m.b45*
                       m.b140 + 392*m.b45*m.b141 + 441*m.b45*m.b142 + 490*m.b45*m.b143 + 539*m.b45*m.b144 + 456*m.b45*
                       m.b145 + 418*m.b45*m.b146 + 380*m.b45*m.b147 + 342*m.b45*m.b148 + 304*m.b45*m.b149 + 342*m.b45*
                       m.b150 + 380*m.b45*m.b151 + 418*m.b45*m.b152 + 396*m.b45*m.b161 + 363*m.b45*m.b162 + 330*m.b45*
                       m.b163 + 297*m.b45*m.b164 + 264*m.b45*m.b165 + 297*m.b45*m.b166 + 330*m.b45*m.b167 + 363*m.b45*
                       m.b168 + 240*m.b45*m.b201 + 220*m.b45*m.b202 + 200*m.b45*m.b203 + 180*m.b45*m.b204 + 160*m.b45*
                       m.b205 + 180*m.b45*m.b206 + 200*m.b45*m.b207 + 220*m.b45*m.b208 + 264*m.b45*m.b217 + 242*m.b45*
                       m.b218 + 220*m.b45*m.b219 + 198*m.b45*m.b220 + 176*m.b45*m.b221 + 198*m.b45*m.b222 + 220*m.b45*
                       m.b223 + 242*m.b45*m.b224 + 408*m.b45*m.b233 + 374*m.b45*m.b234 + 340*m.b45*m.b235 + 306*m.b45*
                       m.b236 + 272*m.b45*m.b237 + 306*m.b45*m.b238 + 340*m.b45*m.b239 + 374*m.b45*m.b240 + 637*m.b46*
                       m.b137 + 588*m.b46*m.b138 + 539*m.b46*m.b139 + 490*m.b46*m.b140 + 441*m.b46*m.b141 + 392*m.b46*
                       m.b142 + 441*m.b46*m.b143 + 490*m.b46*m.b144 + 494*m.b46*m.b145 + 456*m.b46*m.b146 + 418*m.b46*
                       m.b147 + 380*m.b46*m.b148 + 342*m.b46*m.b149 + 304*m.b46*m.b150 + 342*m.b46*m.b151 + 380*m.b46*
                       m.b152 + 429*m.b46*m.b161 + 396*m.b46*m.b162 + 363*m.b46*m.b163 + 330*m.b46*m.b164 + 297*m.b46*
                       m.b165 + 264*m.b46*m.b166 + 297*m.b46*m.b167 + 330*m.b46*m.b168 + 260*m.b46*m.b201 + 240*m.b46*
                       m.b202 + 220*m.b46*m.b203 + 200*m.b46*m.b204 + 180*m.b46*m.b205 + 160*m.b46*m.b206 + 180*m.b46*
                       m.b207 + 200*m.b46*m.b208 + 286*m.b46*m.b217 + 264*m.b46*m.b218 + 242*m.b46*m.b219 + 220*m.b46*
                       m.b220 + 198*m.b46*m.b221 + 176*m.b46*m.b222 + 198*m.b46*m.b223 + 220*m.b46*m.b224 + 442*m.b46*
                       m.b233 + 408*m.b46*m.b234 + 374*m.b46*m.b235 + 340*m.b46*m.b236 + 306*m.b46*m.b237 + 272*m.b46*
                       m.b238 + 306*m.b46*m.b239 + 340*m.b46*m.b240 + 686*m.b47*m.b137 + 637*m.b47*m.b138 + 588*m.b47*
                       m.b139 + 539*m.b47*m.b140 + 490*m.b47*m.b141 + 441*m.b47*m.b142 + 392*m.b47*m.b143 + 441*m.b47*
                       m.b144 + 532*m.b47*m.b145 + 494*m.b47*m.b146 + 456*m.b47*m.b147 + 418*m.b47*m.b148 + 380*m.b47*
                       m.b149 + 342*m.b47*m.b150 + 304*m.b47*m.b151 + 342*m.b47*m.b152 + 462*m.b47*m.b161 + 429*m.b47*
                       m.b162 + 396*m.b47*m.b163 + 363*m.b47*m.b164 + 330*m.b47*m.b165 + 297*m.b47*m.b166 + 264*m.b47*
                       m.b167 + 297*m.b47*m.b168 + 280*m.b47*m.b201 + 260*m.b47*m.b202 + 240*m.b47*m.b203 + 220*m.b47*
                       m.b204 + 200*m.b47*m.b205 + 180*m.b47*m.b206 + 160*m.b47*m.b207 + 180*m.b47*m.b208 + 308*m.b47*
                       m.b217 + 286*m.b47*m.b218 + 264*m.b47*m.b219 + 242*m.b47*m.b220 + 220*m.b47*m.b221 + 198*m.b47*
                       m.b222 + 176*m.b47*m.b223 + 198*m.b47*m.b224 + 476*m.b47*m.b233 + 442*m.b47*m.b234 + 408*m.b47*
                       m.b235 + 374*m.b47*m.b236 + 340*m.b47*m.b237 + 306*m.b47*m.b238 + 272*m.b47*m.b239 + 306*m.b47*
                       m.b240 + 735*m.b48*m.b137 + 686*m.b48*m.b138 + 637*m.b48*m.b139 + 588*m.b48*m.b140 + 539*m.b48*
                       m.b141 + 490*m.b48*m.b142 + 441*m.b48*m.b143 + 392*m.b48*m.b144 + 570*m.b48*m.b145 + 532*m.b48*
                       m.b146 + 494*m.b48*m.b147 + 456*m.b48*m.b148 + 418*m.b48*m.b149 + 380*m.b48*m.b150 + 342*m.b48*
                       m.b151 + 304*m.b48*m.b152 + 495*m.b48*m.b161 + 462*m.b48*m.b162 + 429*m.b48*m.b163 + 396*m.b48*
                       m.b164 + 363*m.b48*m.b165 + 330*m.b48*m.b166 + 297*m.b48*m.b167 + 264*m.b48*m.b168 + 300*m.b48*
                       m.b201 + 280*m.b48*m.b202 + 260*m.b48*m.b203 + 240*m.b48*m.b204 + 220*m.b48*m.b205 + 200*m.b48*
                       m.b206 + 180*m.b48*m.b207 + 160*m.b48*m.b208 + 330*m.b48*m.b217 + 308*m.b48*m.b218 + 286*m.b48*
                       m.b219 + 264*m.b48*m.b220 + 242*m.b48*m.b221 + 220*m.b48*m.b222 + 198*m.b48*m.b223 + 176*m.b48*
                       m.b224 + 510*m.b48*m.b233 + 476*m.b48*m.b234 + 442*m.b48*m.b235 + 408*m.b48*m.b236 + 374*m.b48*
                       m.b237 + 340*m.b48*m.b238 + 306*m.b48*m.b239 + 272*m.b48*m.b240 + 136*m.b49*m.b201 + 153*m.b49*
                       m.b202 + 170*m.b49*m.b203 + 187*m.b49*m.b204 + 204*m.b49*m.b205 + 221*m.b49*m.b206 + 238*m.b49*
                       m.b207 + 255*m.b49*m.b208 + 96*m.b49*m.b217 + 108*m.b49*m.b218 + 120*m.b49*m.b219 + 132*m.b49*
                       m.b220 + 144*m.b49*m.b221 + 156*m.b49*m.b222 + 168*m.b49*m.b223 + 180*m.b49*m.b224 + 376*m.b49*
                       m.b225 + 423*m.b49*m.b226 + 470*m.b49*m.b227 + 517*m.b49*m.b228 + 564*m.b49*m.b229 + 611*m.b49*
                       m.b230 + 658*m.b49*m.b231 + 705*m.b49*m.b232 + 160*m.b49*m.b233 + 180*m.b49*m.b234 + 200*m.b49*
                       m.b235 + 220*m.b49*m.b236 + 240*m.b49*m.b237 + 260*m.b49*m.b238 + 280*m.b49*m.b239 + 300*m.b49*
                       m.b240 + 153*m.b50*m.b201 + 136*m.b50*m.b202 + 153*m.b50*m.b203 + 170*m.b50*m.b204 + 187*m.b50*
                       m.b205 + 204*m.b50*m.b206 + 221*m.b50*m.b207 + 238*m.b50*m.b208 + 108*m.b50*m.b217 + 96*m.b50*
                       m.b218 + 108*m.b50*m.b219 + 120*m.b50*m.b220 + 132*m.b50*m.b221 + 144*m.b50*m.b222 + 156*m.b50*
                       m.b223 + 168*m.b50*m.b224 + 423*m.b50*m.b225 + 376*m.b50*m.b226 + 423*m.b50*m.b227 + 470*m.b50*
                       m.b228 + 517*m.b50*m.b229 + 564*m.b50*m.b230 + 611*m.b50*m.b231 + 658*m.b50*m.b232 + 180*m.b50*
                       m.b233 + 160*m.b50*m.b234 + 180*m.b50*m.b235 + 200*m.b50*m.b236 + 220*m.b50*m.b237 + 240*m.b50*
                       m.b238 + 260*m.b50*m.b239 + 280*m.b50*m.b240 + 170*m.b51*m.b201 + 153*m.b51*m.b202 + 136*m.b51*
                       m.b203 + 153*m.b51*m.b204 + 170*m.b51*m.b205 + 187*m.b51*m.b206 + 204*m.b51*m.b207 + 221*m.b51*
                       m.b208 + 120*m.b51*m.b217 + 108*m.b51*m.b218 + 96*m.b51*m.b219 + 108*m.b51*m.b220 + 120*m.b51*
                       m.b221 + 132*m.b51*m.b222 + 144*m.b51*m.b223 + 156*m.b51*m.b224 + 470*m.b51*m.b225 + 423*m.b51*
                       m.b226 + 376*m.b51*m.b227 + 423*m.b51*m.b228 + 470*m.b51*m.b229 + 517*m.b51*m.b230 + 564*m.b51*
                       m.b231 + 611*m.b51*m.b232 + 200*m.b51*m.b233 + 180*m.b51*m.b234 + 160*m.b51*m.b235 + 180*m.b51*
                       m.b236 + 200*m.b51*m.b237 + 220*m.b51*m.b238 + 240*m.b51*m.b239 + 260*m.b51*m.b240 + 187*m.b52*
                       m.b201 + 170*m.b52*m.b202 + 153*m.b52*m.b203 + 136*m.b52*m.b204 + 153*m.b52*m.b205 + 170*m.b52*
                       m.b206 + 187*m.b52*m.b207 + 204*m.b52*m.b208 + 132*m.b52*m.b217 + 120*m.b52*m.b218 + 108*m.b52*
                       m.b219 + 96*m.b52*m.b220 + 108*m.b52*m.b221 + 120*m.b52*m.b222 + 132*m.b52*m.b223 + 144*m.b52*
                       m.b224 + 517*m.b52*m.b225 + 470*m.b52*m.b226 + 423*m.b52*m.b227 + 376*m.b52*m.b228 + 423*m.b52*
                       m.b229 + 470*m.b52*m.b230 + 517*m.b52*m.b231 + 564*m.b52*m.b232 + 220*m.b52*m.b233 + 200*m.b52*
                       m.b234 + 180*m.b52*m.b235 + 160*m.b52*m.b236 + 180*m.b52*m.b237 + 200*m.b52*m.b238 + 220*m.b52*
                       m.b239 + 240*m.b52*m.b240 + 204*m.b53*m.b201 + 187*m.b53*m.b202 + 170*m.b53*m.b203 + 153*m.b53*
                       m.b204 + 136*m.b53*m.b205 + 153*m.b53*m.b206 + 170*m.b53*m.b207 + 187*m.b53*m.b208 + 144*m.b53*
                       m.b217 + 132*m.b53*m.b218 + 120*m.b53*m.b219 + 108*m.b53*m.b220 + 96*m.b53*m.b221 + 108*m.b53*
                       m.b222 + 120*m.b53*m.b223 + 132*m.b53*m.b224 + 564*m.b53*m.b225 + 517*m.b53*m.b226 + 470*m.b53*
                       m.b227 + 423*m.b53*m.b228 + 376*m.b53*m.b229 + 423*m.b53*m.b230 + 470*m.b53*m.b231 + 517*m.b53*
                       m.b232 + 240*m.b53*m.b233 + 220*m.b53*m.b234 + 200*m.b53*m.b235 + 180*m.b53*m.b236 + 160*m.b53*
                       m.b237 + 180*m.b53*m.b238 + 200*m.b53*m.b239 + 220*m.b53*m.b240 + 221*m.b54*m.b201 + 204*m.b54*
                       m.b202 + 187*m.b54*m.b203 + 170*m.b54*m.b204 + 153*m.b54*m.b205 + 136*m.b54*m.b206 + 153*m.b54*
                       m.b207 + 170*m.b54*m.b208 + 156*m.b54*m.b217 + 144*m.b54*m.b218 + 132*m.b54*m.b219 + 120*m.b54*
                       m.b220 + 108*m.b54*m.b221 + 96*m.b54*m.b222 + 108*m.b54*m.b223 + 120*m.b54*m.b224 + 611*m.b54*
                       m.b225 + 564*m.b54*m.b226 + 517*m.b54*m.b227 + 470*m.b54*m.b228 + 423*m.b54*m.b229 + 376*m.b54*
                       m.b230 + 423*m.b54*m.b231 + 470*m.b54*m.b232 + 260*m.b54*m.b233 + 240*m.b54*m.b234 + 220*m.b54*
                       m.b235 + 200*m.b54*m.b236 + 180*m.b54*m.b237 + 160*m.b54*m.b238 + 180*m.b54*m.b239 + 200*m.b54*
                       m.b240 + 238*m.b55*m.b201 + 221*m.b55*m.b202 + 204*m.b55*m.b203 + 187*m.b55*m.b204 + 170*m.b55*
                       m.b205 + 153*m.b55*m.b206 + 136*m.b55*m.b207 + 153*m.b55*m.b208 + 168*m.b55*m.b217 + 156*m.b55*
                       m.b218 + 144*m.b55*m.b219 + 132*m.b55*m.b220 + 120*m.b55*m.b221 + 108*m.b55*m.b222 + 96*m.b55*
                       m.b223 + 108*m.b55*m.b224 + 658*m.b55*m.b225 + 611*m.b55*m.b226 + 564*m.b55*m.b227 + 517*m.b55*
                       m.b228 + 470*m.b55*m.b229 + 423*m.b55*m.b230 + 376*m.b55*m.b231 + 423*m.b55*m.b232 + 280*m.b55*
                       m.b233 + 260*m.b55*m.b234 + 240*m.b55*m.b235 + 220*m.b55*m.b236 + 200*m.b55*m.b237 + 180*m.b55*
                       m.b238 + 160*m.b55*m.b239 + 180*m.b55*m.b240 + 255*m.b56*m.b201 + 238*m.b56*m.b202 + 221*m.b56*
                       m.b203 + 204*m.b56*m.b204 + 187*m.b56*m.b205 + 170*m.b56*m.b206 + 153*m.b56*m.b207 + 136*m.b56*
                       m.b208 + 180*m.b56*m.b217 + 168*m.b56*m.b218 + 156*m.b56*m.b219 + 144*m.b56*m.b220 + 132*m.b56*
                       m.b221 + 120*m.b56*m.b222 + 108*m.b56*m.b223 + 96*m.b56*m.b224 + 705*m.b56*m.b225 + 658*m.b56*
                       m.b226 + 611*m.b56*m.b227 + 564*m.b56*m.b228 + 517*m.b56*m.b229 + 470*m.b56*m.b230 + 423*m.b56*
                       m.b231 + 376*m.b56*m.b232 + 300*m.b56*m.b233 + 280*m.b56*m.b234 + 260*m.b56*m.b235 + 240*m.b56*
                       m.b236 + 220*m.b56*m.b237 + 200*m.b56*m.b238 + 180*m.b56*m.b239 + 160*m.b56*m.b240 + 320*m.b57*
                       m.b169 + 360*m.b57*m.b170 + 400*m.b57*m.b171 + 440*m.b57*m.b172 + 480*m.b57*m.b173 + 520*m.b57*
                       m.b174 + 560*m.b57*m.b175 + 600*m.b57*m.b176 + 368*m.b57*m.b201 + 414*m.b57*m.b202 + 460*m.b57*
                       m.b203 + 506*m.b57*m.b204 + 552*m.b57*m.b205 + 598*m.b57*m.b206 + 644*m.b57*m.b207 + 690*m.b57*
                       m.b208 + 336*m.b57*m.b217 + 378*m.b57*m.b218 + 420*m.b57*m.b219 + 462*m.b57*m.b220 + 504*m.b57*
                       m.b221 + 546*m.b57*m.b222 + 588*m.b57*m.b223 + 630*m.b57*m.b224 + 360*m.b58*m.b169 + 320*m.b58*
                       m.b170 + 360*m.b58*m.b171 + 400*m.b58*m.b172 + 440*m.b58*m.b173 + 480*m.b58*m.b174 + 520*m.b58*
                       m.b175 + 560*m.b58*m.b176 + 414*m.b58*m.b201 + 368*m.b58*m.b202 + 414*m.b58*m.b203 + 460*m.b58*
                       m.b204 + 506*m.b58*m.b205 + 552*m.b58*m.b206 + 598*m.b58*m.b207 + 644*m.b58*m.b208 + 378*m.b58*
                       m.b217 + 336*m.b58*m.b218 + 378*m.b58*m.b219 + 420*m.b58*m.b220 + 462*m.b58*m.b221 + 504*m.b58*
                       m.b222 + 546*m.b58*m.b223 + 588*m.b58*m.b224 + 400*m.b59*m.b169 + 360*m.b59*m.b170 + 320*m.b59*
                       m.b171 + 360*m.b59*m.b172 + 400*m.b59*m.b173 + 440*m.b59*m.b174 + 480*m.b59*m.b175 + 520*m.b59*
                       m.b176 + 460*m.b59*m.b201 + 414*m.b59*m.b202 + 368*m.b59*m.b203 + 414*m.b59*m.b204 + 460*m.b59*
                       m.b205 + 506*m.b59*m.b206 + 552*m.b59*m.b207 + 598*m.b59*m.b208 + 420*m.b59*m.b217 + 378*m.b59*
                       m.b218 + 336*m.b59*m.b219 + 378*m.b59*m.b220 + 420*m.b59*m.b221 + 462*m.b59*m.b222 + 504*m.b59*
                       m.b223 + 546*m.b59*m.b224 + 440*m.b60*m.b169 + 400*m.b60*m.b170 + 360*m.b60*m.b171 + 320*m.b60*
                       m.b172 + 360*m.b60*m.b173 + 400*m.b60*m.b174 + 440*m.b60*m.b175 + 480*m.b60*m.b176 + 506*m.b60*
                       m.b201 + 460*m.b60*m.b202 + 414*m.b60*m.b203 + 368*m.b60*m.b204 + 414*m.b60*m.b205 + 460*m.b60*
                       m.b206 + 506*m.b60*m.b207 + 552*m.b60*m.b208 + 462*m.b60*m.b217 + 420*m.b60*m.b218 + 378*m.b60*
                       m.b219 + 336*m.b60*m.b220 + 378*m.b60*m.b221 + 420*m.b60*m.b222 + 462*m.b60*m.b223 + 504*m.b60*
                       m.b224 + 480*m.b61*m.b169 + 440*m.b61*m.b170 + 400*m.b61*m.b171 + 360*m.b61*m.b172 + 320*m.b61*
                       m.b173 + 360*m.b61*m.b174 + 400*m.b61*m.b175 + 440*m.b61*m.b176 + 552*m.b61*m.b201 + 506*m.b61*
                       m.b202 + 460*m.b61*m.b203 + 414*m.b61*m.b204 + 368*m.b61*m.b205 + 414*m.b61*m.b206 + 460*m.b61*
                       m.b207 + 506*m.b61*m.b208 + 504*m.b61*m.b217 + 462*m.b61*m.b218 + 420*m.b61*m.b219 + 378*m.b61*
                       m.b220 + 336*m.b61*m.b221 + 378*m.b61*m.b222 + 420*m.b61*m.b223 + 462*m.b61*m.b224 + 520*m.b62*
                       m.b169 + 480*m.b62*m.b170 + 440*m.b62*m.b171 + 400*m.b62*m.b172 + 360*m.b62*m.b173 + 320*m.b62*
                       m.b174 + 360*m.b62*m.b175 + 400*m.b62*m.b176 + 598*m.b62*m.b201 + 552*m.b62*m.b202 + 506*m.b62*
                       m.b203 + 460*m.b62*m.b204 + 414*m.b62*m.b205 + 368*m.b62*m.b206 + 414*m.b62*m.b207 + 460*m.b62*
                       m.b208 + 546*m.b62*m.b217 + 504*m.b62*m.b218 + 462*m.b62*m.b219 + 420*m.b62*m.b220 + 378*m.b62*
                       m.b221 + 336*m.b62*m.b222 + 378*m.b62*m.b223 + 420*m.b62*m.b224 + 560*m.b63*m.b169 + 520*m.b63*
                       m.b170 + 480*m.b63*m.b171 + 440*m.b63*m.b172 + 400*m.b63*m.b173 + 360*m.b63*m.b174 + 320*m.b63*
                       m.b175 + 360*m.b63*m.b176 + 644*m.b63*m.b201 + 598*m.b63*m.b202 + 552*m.b63*m.b203 + 506*m.b63*
                       m.b204 + 460*m.b63*m.b205 + 414*m.b63*m.b206 + 368*m.b63*m.b207 + 414*m.b63*m.b208 + 588*m.b63*
                       m.b217 + 546*m.b63*m.b218 + 504*m.b63*m.b219 + 462*m.b63*m.b220 + 420*m.b63*m.b221 + 378*m.b63*
                       m.b222 + 336*m.b63*m.b223 + 378*m.b63*m.b224 + 600*m.b64*m.b169 + 560*m.b64*m.b170 + 520*m.b64*
                       m.b171 + 480*m.b64*m.b172 + 440*m.b64*m.b173 + 400*m.b64*m.b174 + 360*m.b64*m.b175 + 320*m.b64*
                       m.b176 + 690*m.b64*m.b201 + 644*m.b64*m.b202 + 598*m.b64*m.b203 + 552*m.b64*m.b204 + 506*m.b64*
                       m.b205 + 460*m.b64*m.b206 + 414*m.b64*m.b207 + 368*m.b64*m.b208 + 630*m.b64*m.b217 + 588*m.b64*
                       m.b218 + 546*m.b64*m.b219 + 504*m.b64*m.b220 + 462*m.b64*m.b221 + 420*m.b64*m.b222 + 378*m.b64*
                       m.b223 + 336*m.b64*m.b224 + 384*m.b65*m.b177 + 432*m.b65*m.b178 + 480*m.b65*m.b179 + 528*m.b65*
                       m.b180 + 576*m.b65*m.b181 + 624*m.b65*m.b182 + 672*m.b65*m.b183 + 720*m.b65*m.b184 + 88*m.b65*
                       m.b185 + 99*m.b65*m.b186 + 110*m.b65*m.b187 + 121*m.b65*m.b188 + 132*m.b65*m.b189 + 143*m.b65*
                       m.b190 + 154*m.b65*m.b191 + 165*m.b65*m.b192 + 192*m.b65*m.b225 + 216*m.b65*m.b226 + 240*m.b65*
                       m.b227 + 264*m.b65*m.b228 + 288*m.b65*m.b229 + 312*m.b65*m.b230 + 336*m.b65*m.b231 + 360*m.b65*
                       m.b232 + 432*m.b66*m.b177 + 384*m.b66*m.b178 + 432*m.b66*m.b179 + 480*m.b66*m.b180 + 528*m.b66*
                       m.b181 + 576*m.b66*m.b182 + 624*m.b66*m.b183 + 672*m.b66*m.b184 + 99*m.b66*m.b185 + 88*m.b66*
                       m.b186 + 99*m.b66*m.b187 + 110*m.b66*m.b188 + 121*m.b66*m.b189 + 132*m.b66*m.b190 + 143*m.b66*
                       m.b191 + 154*m.b66*m.b192 + 216*m.b66*m.b225 + 192*m.b66*m.b226 + 216*m.b66*m.b227 + 240*m.b66*
                       m.b228 + 264*m.b66*m.b229 + 288*m.b66*m.b230 + 312*m.b66*m.b231 + 336*m.b66*m.b232 + 480*m.b67*
                       m.b177 + 432*m.b67*m.b178 + 384*m.b67*m.b179 + 432*m.b67*m.b180 + 480*m.b67*m.b181 + 528*m.b67*
                       m.b182 + 576*m.b67*m.b183 + 624*m.b67*m.b184 + 110*m.b67*m.b185 + 99*m.b67*m.b186 + 88*m.b67*
                       m.b187 + 99*m.b67*m.b188 + 110*m.b67*m.b189 + 121*m.b67*m.b190 + 132*m.b67*m.b191 + 143*m.b67*
                       m.b192 + 240*m.b67*m.b225 + 216*m.b67*m.b226 + 192*m.b67*m.b227 + 216*m.b67*m.b228 + 240*m.b67*
                       m.b229 + 264*m.b67*m.b230 + 288*m.b67*m.b231 + 312*m.b67*m.b232 + 528*m.b68*m.b177 + 480*m.b68*
                       m.b178 + 432*m.b68*m.b179 + 384*m.b68*m.b180 + 432*m.b68*m.b181 + 480*m.b68*m.b182 + 528*m.b68*
                       m.b183 + 576*m.b68*m.b184 + 121*m.b68*m.b185 + 110*m.b68*m.b186 + 99*m.b68*m.b187 + 88*m.b68*
                       m.b188 + 99*m.b68*m.b189 + 110*m.b68*m.b190 + 121*m.b68*m.b191 + 132*m.b68*m.b192 + 264*m.b68*
                       m.b225 + 240*m.b68*m.b226 + 216*m.b68*m.b227 + 192*m.b68*m.b228 + 216*m.b68*m.b229 + 240*m.b68*
                       m.b230 + 264*m.b68*m.b231 + 288*m.b68*m.b232 + 576*m.b69*m.b177 + 528*m.b69*m.b178 + 480*m.b69*
                       m.b179 + 432*m.b69*m.b180 + 384*m.b69*m.b181 + 432*m.b69*m.b182 + 480*m.b69*m.b183 + 528*m.b69*
                       m.b184 + 132*m.b69*m.b185 + 121*m.b69*m.b186 + 110*m.b69*m.b187 + 99*m.b69*m.b188 + 88*m.b69*
                       m.b189 + 99*m.b69*m.b190 + 110*m.b69*m.b191 + 121*m.b69*m.b192 + 288*m.b69*m.b225 + 264*m.b69*
                       m.b226 + 240*m.b69*m.b227 + 216*m.b69*m.b228 + 192*m.b69*m.b229 + 216*m.b69*m.b230 + 240*m.b69*
                       m.b231 + 264*m.b69*m.b232 + 624*m.b70*m.b177 + 576*m.b70*m.b178 + 528*m.b70*m.b179 + 480*m.b70*
                       m.b180 + 432*m.b70*m.b181 + 384*m.b70*m.b182 + 432*m.b70*m.b183 + 480*m.b70*m.b184 + 143*m.b70*
                       m.b185 + 132*m.b70*m.b186 + 121*m.b70*m.b187 + 110*m.b70*m.b188 + 99*m.b70*m.b189 + 88*m.b70*
                       m.b190 + 99*m.b70*m.b191 + 110*m.b70*m.b192 + 312*m.b70*m.b225 + 288*m.b70*m.b226 + 264*m.b70*
                       m.b227 + 240*m.b70*m.b228 + 216*m.b70*m.b229 + 192*m.b70*m.b230 + 216*m.b70*m.b231 + 240*m.b70*
                       m.b232 + 672*m.b71*m.b177 + 624*m.b71*m.b178 + 576*m.b71*m.b179 + 528*m.b71*m.b180 + 480*m.b71*
                       m.b181 + 432*m.b71*m.b182 + 384*m.b71*m.b183 + 432*m.b71*m.b184 + 154*m.b71*m.b185 + 143*m.b71*
                       m.b186 + 132*m.b71*m.b187 + 121*m.b71*m.b188 + 110*m.b71*m.b189 + 99*m.b71*m.b190 + 88*m.b71*
                       m.b191 + 99*m.b71*m.b192 + 336*m.b71*m.b225 + 312*m.b71*m.b226 + 288*m.b71*m.b227 + 264*m.b71*
                       m.b228 + 240*m.b71*m.b229 + 216*m.b71*m.b230 + 192*m.b71*m.b231 + 216*m.b71*m.b232 + 720*m.b72*
                       m.b177 + 672*m.b72*m.b178 + 624*m.b72*m.b179 + 576*m.b72*m.b180 + 528*m.b72*m.b181 + 480*m.b72*
                       m.b182 + 432*m.b72*m.b183 + 384*m.b72*m.b184 + 165*m.b72*m.b185 + 154*m.b72*m.b186 + 143*m.b72*
                       m.b187 + 132*m.b72*m.b188 + 121*m.b72*m.b189 + 110*m.b72*m.b190 + 99*m.b72*m.b191 + 88*m.b72*
                       m.b192 + 360*m.b72*m.b225 + 336*m.b72*m.b226 + 312*m.b72*m.b227 + 288*m.b72*m.b228 + 264*m.b72*
                       m.b229 + 240*m.b72*m.b230 + 216*m.b72*m.b231 + 192*m.b72*m.b232 + 120*m.b73*m.b121 + 135*m.b73*
                       m.b122 + 150*m.b73*m.b123 + 165*m.b73*m.b124 + 180*m.b73*m.b125 + 195*m.b73*m.b126 + 210*m.b73*
                       m.b127 + 225*m.b73*m.b128 + 248*m.b73*m.b129 + 279*m.b73*m.b130 + 310*m.b73*m.b131 + 341*m.b73*
                       m.b132 + 372*m.b73*m.b133 + 403*m.b73*m.b134 + 434*m.b73*m.b135 + 465*m.b73*m.b136 + 312*m.b73*
                       m.b145 + 351*m.b73*m.b146 + 390*m.b73*m.b147 + 429*m.b73*m.b148 + 468*m.b73*m.b149 + 507*m.b73*
                       m.b150 + 546*m.b73*m.b151 + 585*m.b73*m.b152 + 128*m.b73*m.b153 + 144*m.b73*m.b154 + 160*m.b73*
                       m.b155 + 176*m.b73*m.b156 + 192*m.b73*m.b157 + 208*m.b73*m.b158 + 224*m.b73*m.b159 + 240*m.b73*
                       m.b160 + 368*m.b73*m.b185 + 414*m.b73*m.b186 + 460*m.b73*m.b187 + 506*m.b73*m.b188 + 552*m.b73*
                       m.b189 + 598*m.b73*m.b190 + 644*m.b73*m.b191 + 690*m.b73*m.b192 + 336*m.b73*m.b233 + 378*m.b73*
                       m.b234 + 420*m.b73*m.b235 + 462*m.b73*m.b236 + 504*m.b73*m.b237 + 546*m.b73*m.b238 + 588*m.b73*
                       m.b239 + 630*m.b73*m.b240 + 135*m.b74*m.b121 + 120*m.b74*m.b122 + 135*m.b74*m.b123 + 150*m.b74*
                       m.b124 + 165*m.b74*m.b125 + 180*m.b74*m.b126 + 195*m.b74*m.b127 + 210*m.b74*m.b128 + 279*m.b74*
                       m.b129 + 248*m.b74*m.b130 + 279*m.b74*m.b131 + 310*m.b74*m.b132 + 341*m.b74*m.b133 + 372*m.b74*
                       m.b134 + 403*m.b74*m.b135 + 434*m.b74*m.b136 + 351*m.b74*m.b145 + 312*m.b74*m.b146 + 351*m.b74*
                       m.b147 + 390*m.b74*m.b148 + 429*m.b74*m.b149 + 468*m.b74*m.b150 + 507*m.b74*m.b151 + 546*m.b74*
                       m.b152 + 144*m.b74*m.b153 + 128*m.b74*m.b154 + 144*m.b74*m.b155 + 160*m.b74*m.b156 + 176*m.b74*
                       m.b157 + 192*m.b74*m.b158 + 208*m.b74*m.b159 + 224*m.b74*m.b160 + 414*m.b74*m.b185 + 368*m.b74*
                       m.b186 + 414*m.b74*m.b187 + 460*m.b74*m.b188 + 506*m.b74*m.b189 + 552*m.b74*m.b190 + 598*m.b74*
                       m.b191 + 644*m.b74*m.b192 + 378*m.b74*m.b233 + 336*m.b74*m.b234 + 378*m.b74*m.b235 + 420*m.b74*
                       m.b236 + 462*m.b74*m.b237 + 504*m.b74*m.b238 + 546*m.b74*m.b239 + 588*m.b74*m.b240 + 150*m.b75*
                       m.b121 + 135*m.b75*m.b122 + 120*m.b75*m.b123 + 135*m.b75*m.b124 + 150*m.b75*m.b125 + 165*m.b75*
                       m.b126 + 180*m.b75*m.b127 + 195*m.b75*m.b128 + 310*m.b75*m.b129 + 279*m.b75*m.b130 + 248*m.b75*
                       m.b131 + 279*m.b75*m.b132 + 310*m.b75*m.b133 + 341*m.b75*m.b134 + 372*m.b75*m.b135 + 403*m.b75*
                       m.b136 + 390*m.b75*m.b145 + 351*m.b75*m.b146 + 312*m.b75*m.b147 + 351*m.b75*m.b148 + 390*m.b75*
                       m.b149 + 429*m.b75*m.b150 + 468*m.b75*m.b151 + 507*m.b75*m.b152 + 160*m.b75*m.b153 + 144*m.b75*
                       m.b154 + 128*m.b75*m.b155 + 144*m.b75*m.b156 + 160*m.b75*m.b157 + 176*m.b75*m.b158 + 192*m.b75*
                       m.b159 + 208*m.b75*m.b160 + 460*m.b75*m.b185 + 414*m.b75*m.b186 + 368*m.b75*m.b187 + 414*m.b75*
                       m.b188 + 460*m.b75*m.b189 + 506*m.b75*m.b190 + 552*m.b75*m.b191 + 598*m.b75*m.b192 + 420*m.b75*
                       m.b233 + 378*m.b75*m.b234 + 336*m.b75*m.b235 + 378*m.b75*m.b236 + 420*m.b75*m.b237 + 462*m.b75*
                       m.b238 + 504*m.b75*m.b239 + 546*m.b75*m.b240 + 165*m.b76*m.b121 + 150*m.b76*m.b122 + 135*m.b76*
                       m.b123 + 120*m.b76*m.b124 + 135*m.b76*m.b125 + 150*m.b76*m.b126 + 165*m.b76*m.b127 + 180*m.b76*
                       m.b128 + 341*m.b76*m.b129 + 310*m.b76*m.b130 + 279*m.b76*m.b131 + 248*m.b76*m.b132 + 279*m.b76*
                       m.b133 + 310*m.b76*m.b134 + 341*m.b76*m.b135 + 372*m.b76*m.b136 + 429*m.b76*m.b145 + 390*m.b76*
                       m.b146 + 351*m.b76*m.b147 + 312*m.b76*m.b148 + 351*m.b76*m.b149 + 390*m.b76*m.b150 + 429*m.b76*
                       m.b151 + 468*m.b76*m.b152 + 176*m.b76*m.b153 + 160*m.b76*m.b154 + 144*m.b76*m.b155 + 128*m.b76*
                       m.b156 + 144*m.b76*m.b157 + 160*m.b76*m.b158 + 176*m.b76*m.b159 + 192*m.b76*m.b160 + 506*m.b76*
                       m.b185 + 460*m.b76*m.b186 + 414*m.b76*m.b187 + 368*m.b76*m.b188 + 414*m.b76*m.b189 + 460*m.b76*
                       m.b190 + 506*m.b76*m.b191 + 552*m.b76*m.b192 + 462*m.b76*m.b233 + 420*m.b76*m.b234 + 378*m.b76*
                       m.b235 + 336*m.b76*m.b236 + 378*m.b76*m.b237 + 420*m.b76*m.b238 + 462*m.b76*m.b239 + 504*m.b76*
                       m.b240 + 180*m.b77*m.b121 + 165*m.b77*m.b122 + 150*m.b77*m.b123 + 135*m.b77*m.b124 + 120*m.b77*
                       m.b125 + 135*m.b77*m.b126 + 150*m.b77*m.b127 + 165*m.b77*m.b128 + 372*m.b77*m.b129 + 341*m.b77*
                       m.b130 + 310*m.b77*m.b131 + 279*m.b77*m.b132 + 248*m.b77*m.b133 + 279*m.b77*m.b134 + 310*m.b77*
                       m.b135 + 341*m.b77*m.b136 + 468*m.b77*m.b145 + 429*m.b77*m.b146 + 390*m.b77*m.b147 + 351*m.b77*
                       m.b148 + 312*m.b77*m.b149 + 351*m.b77*m.b150 + 390*m.b77*m.b151 + 429*m.b77*m.b152 + 192*m.b77*
                       m.b153 + 176*m.b77*m.b154 + 160*m.b77*m.b155 + 144*m.b77*m.b156 + 128*m.b77*m.b157 + 144*m.b77*
                       m.b158 + 160*m.b77*m.b159 + 176*m.b77*m.b160 + 552*m.b77*m.b185 + 506*m.b77*m.b186 + 460*m.b77*
                       m.b187 + 414*m.b77*m.b188 + 368*m.b77*m.b189 + 414*m.b77*m.b190 + 460*m.b77*m.b191 + 506*m.b77*
                       m.b192 + 504*m.b77*m.b233 + 462*m.b77*m.b234 + 420*m.b77*m.b235 + 378*m.b77*m.b236 + 336*m.b77*
                       m.b237 + 378*m.b77*m.b238 + 420*m.b77*m.b239 + 462*m.b77*m.b240 + 195*m.b78*m.b121 + 180*m.b78*
                       m.b122 + 165*m.b78*m.b123 + 150*m.b78*m.b124 + 135*m.b78*m.b125 + 120*m.b78*m.b126 + 135*m.b78*
                       m.b127 + 150*m.b78*m.b128 + 403*m.b78*m.b129 + 372*m.b78*m.b130 + 341*m.b78*m.b131 + 310*m.b78*
                       m.b132 + 279*m.b78*m.b133 + 248*m.b78*m.b134 + 279*m.b78*m.b135 + 310*m.b78*m.b136 + 507*m.b78*
                       m.b145 + 468*m.b78*m.b146 + 429*m.b78*m.b147 + 390*m.b78*m.b148 + 351*m.b78*m.b149 + 312*m.b78*
                       m.b150 + 351*m.b78*m.b151 + 390*m.b78*m.b152 + 208*m.b78*m.b153 + 192*m.b78*m.b154 + 176*m.b78*
                       m.b155 + 160*m.b78*m.b156 + 144*m.b78*m.b157 + 128*m.b78*m.b158 + 144*m.b78*m.b159 + 160*m.b78*
                       m.b160 + 598*m.b78*m.b185 + 552*m.b78*m.b186 + 506*m.b78*m.b187 + 460*m.b78*m.b188 + 414*m.b78*
                       m.b189 + 368*m.b78*m.b190 + 414*m.b78*m.b191 + 460*m.b78*m.b192 + 546*m.b78*m.b233 + 504*m.b78*
                       m.b234 + 462*m.b78*m.b235 + 420*m.b78*m.b236 + 378*m.b78*m.b237 + 336*m.b78*m.b238 + 378*m.b78*
                       m.b239 + 420*m.b78*m.b240 + 210*m.b79*m.b121 + 195*m.b79*m.b122 + 180*m.b79*m.b123 + 165*m.b79*
                       m.b124 + 150*m.b79*m.b125 + 135*m.b79*m.b126 + 120*m.b79*m.b127 + 135*m.b79*m.b128 + 434*m.b79*
                       m.b129 + 403*m.b79*m.b130 + 372*m.b79*m.b131 + 341*m.b79*m.b132 + 310*m.b79*m.b133 + 279*m.b79*
                       m.b134 + 248*m.b79*m.b135 + 279*m.b79*m.b136 + 546*m.b79*m.b145 + 507*m.b79*m.b146 + 468*m.b79*
                       m.b147 + 429*m.b79*m.b148 + 390*m.b79*m.b149 + 351*m.b79*m.b150 + 312*m.b79*m.b151 + 351*m.b79*
                       m.b152 + 224*m.b79*m.b153 + 208*m.b79*m.b154 + 192*m.b79*m.b155 + 176*m.b79*m.b156 + 160*m.b79*
                       m.b157 + 144*m.b79*m.b158 + 128*m.b79*m.b159 + 144*m.b79*m.b160 + 644*m.b79*m.b185 + 598*m.b79*
                       m.b186 + 552*m.b79*m.b187 + 506*m.b79*m.b188 + 460*m.b79*m.b189 + 414*m.b79*m.b190 + 368*m.b79*
                       m.b191 + 414*m.b79*m.b192 + 588*m.b79*m.b233 + 546*m.b79*m.b234 + 504*m.b79*m.b235 + 462*m.b79*
                       m.b236 + 420*m.b79*m.b237 + 378*m.b79*m.b238 + 336*m.b79*m.b239 + 378*m.b79*m.b240 + 225*m.b80*
                       m.b121 + 210*m.b80*m.b122 + 195*m.b80*m.b123 + 180*m.b80*m.b124 + 165*m.b80*m.b125 + 150*m.b80*
                       m.b126 + 135*m.b80*m.b127 + 120*m.b80*m.b128 + 465*m.b80*m.b129 + 434*m.b80*m.b130 + 403*m.b80*
                       m.b131 + 372*m.b80*m.b132 + 341*m.b80*m.b133 + 310*m.b80*m.b134 + 279*m.b80*m.b135 + 248*m.b80*
                       m.b136 + 585*m.b80*m.b145 + 546*m.b80*m.b146 + 507*m.b80*m.b147 + 468*m.b80*m.b148 + 429*m.b80*
                       m.b149 + 390*m.b80*m.b150 + 351*m.b80*m.b151 + 312*m.b80*m.b152 + 240*m.b80*m.b153 + 224*m.b80*
                       m.b154 + 208*m.b80*m.b155 + 192*m.b80*m.b156 + 176*m.b80*m.b157 + 160*m.b80*m.b158 + 144*m.b80*
                       m.b159 + 128*m.b80*m.b160 + 690*m.b80*m.b185 + 644*m.b80*m.b186 + 598*m.b80*m.b187 + 552*m.b80*
                       m.b188 + 506*m.b80*m.b189 + 460*m.b80*m.b190 + 414*m.b80*m.b191 + 368*m.b80*m.b192 + 630*m.b80*
                       m.b233 + 588*m.b80*m.b234 + 546*m.b80*m.b235 + 504*m.b80*m.b236 + 462*m.b80*m.b237 + 420*m.b80*
                       m.b238 + 378*m.b80*m.b239 + 336*m.b80*m.b240 + 368*m.b81*m.b129 + 414*m.b81*m.b130 + 460*m.b81*
                       m.b131 + 506*m.b81*m.b132 + 552*m.b81*m.b133 + 598*m.b81*m.b134 + 644*m.b81*m.b135 + 690*m.b81*
                       m.b136 + 224*m.b81*m.b153 + 252*m.b81*m.b154 + 280*m.b81*m.b155 + 308*m.b81*m.b156 + 336*m.b81*
                       m.b157 + 364*m.b81*m.b158 + 392*m.b81*m.b159 + 420*m.b81*m.b160 + 88*m.b81*m.b185 + 99*m.b81*
                       m.b186 + 110*m.b81*m.b187 + 121*m.b81*m.b188 + 132*m.b81*m.b189 + 143*m.b81*m.b190 + 154*m.b81*
                       m.b191 + 165*m.b81*m.b192 + 224*m.b81*m.b193 + 252*m.b81*m.b194 + 280*m.b81*m.b195 + 308*m.b81*
                       m.b196 + 336*m.b81*m.b197 + 364*m.b81*m.b198 + 392*m.b81*m.b199 + 420*m.b81*m.b200 + 414*m.b82*
                       m.b129 + 368*m.b82*m.b130 + 414*m.b82*m.b131 + 460*m.b82*m.b132 + 506*m.b82*m.b133 + 552*m.b82*
                       m.b134 + 598*m.b82*m.b135 + 644*m.b82*m.b136 + 252*m.b82*m.b153 + 224*m.b82*m.b154 + 252*m.b82*
                       m.b155 + 280*m.b82*m.b156 + 308*m.b82*m.b157 + 336*m.b82*m.b158 + 364*m.b82*m.b159 + 392*m.b82*
                       m.b160 + 99*m.b82*m.b185 + 88*m.b82*m.b186 + 99*m.b82*m.b187 + 110*m.b82*m.b188 + 121*m.b82*
                       m.b189 + 132*m.b82*m.b190 + 143*m.b82*m.b191 + 154*m.b82*m.b192 + 252*m.b82*m.b193 + 224*m.b82*
                       m.b194 + 252*m.b82*m.b195 + 280*m.b82*m.b196 + 308*m.b82*m.b197 + 336*m.b82*m.b198 + 364*m.b82*
                       m.b199 + 392*m.b82*m.b200 + 460*m.b83*m.b129 + 414*m.b83*m.b130 + 368*m.b83*m.b131 + 414*m.b83*
                       m.b132 + 460*m.b83*m.b133 + 506*m.b83*m.b134 + 552*m.b83*m.b135 + 598*m.b83*m.b136 + 280*m.b83*
                       m.b153 + 252*m.b83*m.b154 + 224*m.b83*m.b155 + 252*m.b83*m.b156 + 280*m.b83*m.b157 + 308*m.b83*
                       m.b158 + 336*m.b83*m.b159 + 364*m.b83*m.b160 + 110*m.b83*m.b185 + 99*m.b83*m.b186 + 88*m.b83*
                       m.b187 + 99*m.b83*m.b188 + 110*m.b83*m.b189 + 121*m.b83*m.b190 + 132*m.b83*m.b191 + 143*m.b83*
                       m.b192 + 280*m.b83*m.b193 + 252*m.b83*m.b194 + 224*m.b83*m.b195 + 252*m.b83*m.b196 + 280*m.b83*
                       m.b197 + 308*m.b83*m.b198 + 336*m.b83*m.b199 + 364*m.b83*m.b200 + 506*m.b84*m.b129 + 460*m.b84*
                       m.b130 + 414*m.b84*m.b131 + 368*m.b84*m.b132 + 414*m.b84*m.b133 + 460*m.b84*m.b134 + 506*m.b84*
                       m.b135 + 552*m.b84*m.b136 + 308*m.b84*m.b153 + 280*m.b84*m.b154 + 252*m.b84*m.b155 + 224*m.b84*
                       m.b156 + 252*m.b84*m.b157 + 280*m.b84*m.b158 + 308*m.b84*m.b159 + 336*m.b84*m.b160 + 121*m.b84*
                       m.b185 + 110*m.b84*m.b186 + 99*m.b84*m.b187 + 88*m.b84*m.b188 + 99*m.b84*m.b189 + 110*m.b84*
                       m.b190 + 121*m.b84*m.b191 + 132*m.b84*m.b192 + 308*m.b84*m.b193 + 280*m.b84*m.b194 + 252*m.b84*
                       m.b195 + 224*m.b84*m.b196 + 252*m.b84*m.b197 + 280*m.b84*m.b198 + 308*m.b84*m.b199 + 336*m.b84*
                       m.b200 + 552*m.b85*m.b129 + 506*m.b85*m.b130 + 460*m.b85*m.b131 + 414*m.b85*m.b132 + 368*m.b85*
                       m.b133 + 414*m.b85*m.b134 + 460*m.b85*m.b135 + 506*m.b85*m.b136 + 336*m.b85*m.b153 + 308*m.b85*
                       m.b154 + 280*m.b85*m.b155 + 252*m.b85*m.b156 + 224*m.b85*m.b157 + 252*m.b85*m.b158 + 280*m.b85*
                       m.b159 + 308*m.b85*m.b160 + 132*m.b85*m.b185 + 121*m.b85*m.b186 + 110*m.b85*m.b187 + 99*m.b85*
                       m.b188 + 88*m.b85*m.b189 + 99*m.b85*m.b190 + 110*m.b85*m.b191 + 121*m.b85*m.b192 + 336*m.b85*
                       m.b193 + 308*m.b85*m.b194 + 280*m.b85*m.b195 + 252*m.b85*m.b196 + 224*m.b85*m.b197 + 252*m.b85*
                       m.b198 + 280*m.b85*m.b199 + 308*m.b85*m.b200 + 598*m.b86*m.b129 + 552*m.b86*m.b130 + 506*m.b86*
                       m.b131 + 460*m.b86*m.b132 + 414*m.b86*m.b133 + 368*m.b86*m.b134 + 414*m.b86*m.b135 + 460*m.b86*
                       m.b136 + 364*m.b86*m.b153 + 336*m.b86*m.b154 + 308*m.b86*m.b155 + 280*m.b86*m.b156 + 252*m.b86*
                       m.b157 + 224*m.b86*m.b158 + 252*m.b86*m.b159 + 280*m.b86*m.b160 + 143*m.b86*m.b185 + 132*m.b86*
                       m.b186 + 121*m.b86*m.b187 + 110*m.b86*m.b188 + 99*m.b86*m.b189 + 88*m.b86*m.b190 + 99*m.b86*
                       m.b191 + 110*m.b86*m.b192 + 364*m.b86*m.b193 + 336*m.b86*m.b194 + 308*m.b86*m.b195 + 280*m.b86*
                       m.b196 + 252*m.b86*m.b197 + 224*m.b86*m.b198 + 252*m.b86*m.b199 + 280*m.b86*m.b200 + 644*m.b87*
                       m.b129 + 598*m.b87*m.b130 + 552*m.b87*m.b131 + 506*m.b87*m.b132 + 460*m.b87*m.b133 + 414*m.b87*
                       m.b134 + 368*m.b87*m.b135 + 414*m.b87*m.b136 + 392*m.b87*m.b153 + 364*m.b87*m.b154 + 336*m.b87*
                       m.b155 + 308*m.b87*m.b156 + 280*m.b87*m.b157 + 252*m.b87*m.b158 + 224*m.b87*m.b159 + 252*m.b87*
                       m.b160 + 154*m.b87*m.b185 + 143*m.b87*m.b186 + 132*m.b87*m.b187 + 121*m.b87*m.b188 + 110*m.b87*
                       m.b189 + 99*m.b87*m.b190 + 88*m.b87*m.b191 + 99*m.b87*m.b192 + 392*m.b87*m.b193 + 364*m.b87*
                       m.b194 + 336*m.b87*m.b195 + 308*m.b87*m.b196 + 280*m.b87*m.b197 + 252*m.b87*m.b198 + 224*m.b87*
                       m.b199 + 252*m.b87*m.b200 + 690*m.b88*m.b129 + 644*m.b88*m.b130 + 598*m.b88*m.b131 + 552*m.b88*
                       m.b132 + 506*m.b88*m.b133 + 460*m.b88*m.b134 + 414*m.b88*m.b135 + 368*m.b88*m.b136 + 420*m.b88*
                       m.b153 + 392*m.b88*m.b154 + 364*m.b88*m.b155 + 336*m.b88*m.b156 + 308*m.b88*m.b157 + 280*m.b88*
                       m.b158 + 252*m.b88*m.b159 + 224*m.b88*m.b160 + 165*m.b88*m.b185 + 154*m.b88*m.b186 + 143*m.b88*
                       m.b187 + 132*m.b88*m.b188 + 121*m.b88*m.b189 + 110*m.b88*m.b190 + 99*m.b88*m.b191 + 88*m.b88*
                       m.b192 + 420*m.b88*m.b193 + 392*m.b88*m.b194 + 364*m.b88*m.b195 + 336*m.b88*m.b196 + 308*m.b88*
                       m.b197 + 280*m.b88*m.b198 + 252*m.b88*m.b199 + 224*m.b88*m.b200 + 320*m.b89*m.b129 + 360*m.b89*
                       m.b130 + 400*m.b89*m.b131 + 440*m.b89*m.b132 + 480*m.b89*m.b133 + 520*m.b89*m.b134 + 560*m.b89*
                       m.b135 + 600*m.b89*m.b136 + 128*m.b89*m.b153 + 144*m.b89*m.b154 + 160*m.b89*m.b155 + 176*m.b89*
                       m.b156 + 192*m.b89*m.b157 + 208*m.b89*m.b158 + 224*m.b89*m.b159 + 240*m.b89*m.b160 + 88*m.b89*
                       m.b177 + 99*m.b89*m.b178 + 110*m.b89*m.b179 + 121*m.b89*m.b180 + 132*m.b89*m.b181 + 143*m.b89*
                       m.b182 + 154*m.b89*m.b183 + 165*m.b89*m.b184 + 200*m.b89*m.b193 + 225*m.b89*m.b194 + 250*m.b89*
                       m.b195 + 275*m.b89*m.b196 + 300*m.b89*m.b197 + 325*m.b89*m.b198 + 350*m.b89*m.b199 + 375*m.b89*
                       m.b200 + 360*m.b90*m.b129 + 320*m.b90*m.b130 + 360*m.b90*m.b131 + 400*m.b90*m.b132 + 440*m.b90*
                       m.b133 + 480*m.b90*m.b134 + 520*m.b90*m.b135 + 560*m.b90*m.b136 + 144*m.b90*m.b153 + 128*m.b90*
                       m.b154 + 144*m.b90*m.b155 + 160*m.b90*m.b156 + 176*m.b90*m.b157 + 192*m.b90*m.b158 + 208*m.b90*
                       m.b159 + 224*m.b90*m.b160 + 99*m.b90*m.b177 + 88*m.b90*m.b178 + 99*m.b90*m.b179 + 110*m.b90*
                       m.b180 + 121*m.b90*m.b181 + 132*m.b90*m.b182 + 143*m.b90*m.b183 + 154*m.b90*m.b184 + 225*m.b90*
                       m.b193 + 200*m.b90*m.b194 + 225*m.b90*m.b195 + 250*m.b90*m.b196 + 275*m.b90*m.b197 + 300*m.b90*
                       m.b198 + 325*m.b90*m.b199 + 350*m.b90*m.b200 + 400*m.b91*m.b129 + 360*m.b91*m.b130 + 320*m.b91*
                       m.b131 + 360*m.b91*m.b132 + 400*m.b91*m.b133 + 440*m.b91*m.b134 + 480*m.b91*m.b135 + 520*m.b91*
                       m.b136 + 160*m.b91*m.b153 + 144*m.b91*m.b154 + 128*m.b91*m.b155 + 144*m.b91*m.b156 + 160*m.b91*
                       m.b157 + 176*m.b91*m.b158 + 192*m.b91*m.b159 + 208*m.b91*m.b160 + 110*m.b91*m.b177 + 99*m.b91*
                       m.b178 + 88*m.b91*m.b179 + 99*m.b91*m.b180 + 110*m.b91*m.b181 + 121*m.b91*m.b182 + 132*m.b91*
                       m.b183 + 143*m.b91*m.b184 + 250*m.b91*m.b193 + 225*m.b91*m.b194 + 200*m.b91*m.b195 + 225*m.b91*
                       m.b196 + 250*m.b91*m.b197 + 275*m.b91*m.b198 + 300*m.b91*m.b199 + 325*m.b91*m.b200 + 440*m.b92*
                       m.b129 + 400*m.b92*m.b130 + 360*m.b92*m.b131 + 320*m.b92*m.b132 + 360*m.b92*m.b133 + 400*m.b92*
                       m.b134 + 440*m.b92*m.b135 + 480*m.b92*m.b136 + 176*m.b92*m.b153 + 160*m.b92*m.b154 + 144*m.b92*
                       m.b155 + 128*m.b92*m.b156 + 144*m.b92*m.b157 + 160*m.b92*m.b158 + 176*m.b92*m.b159 + 192*m.b92*
                       m.b160 + 121*m.b92*m.b177 + 110*m.b92*m.b178 + 99*m.b92*m.b179 + 88*m.b92*m.b180 + 99*m.b92*
                       m.b181 + 110*m.b92*m.b182 + 121*m.b92*m.b183 + 132*m.b92*m.b184 + 275*m.b92*m.b193 + 250*m.b92*
                       m.b194 + 225*m.b92*m.b195 + 200*m.b92*m.b196 + 225*m.b92*m.b197 + 250*m.b92*m.b198 + 275*m.b92*
                       m.b199 + 300*m.b92*m.b200 + 480*m.b93*m.b129 + 440*m.b93*m.b130 + 400*m.b93*m.b131 + 360*m.b93*
                       m.b132 + 320*m.b93*m.b133 + 360*m.b93*m.b134 + 400*m.b93*m.b135 + 440*m.b93*m.b136 + 192*m.b93*
                       m.b153 + 176*m.b93*m.b154 + 160*m.b93*m.b155 + 144*m.b93*m.b156 + 128*m.b93*m.b157 + 144*m.b93*
                       m.b158 + 160*m.b93*m.b159 + 176*m.b93*m.b160 + 132*m.b93*m.b177 + 121*m.b93*m.b178 + 110*m.b93*
                       m.b179 + 99*m.b93*m.b180 + 88*m.b93*m.b181 + 99*m.b93*m.b182 + 110*m.b93*m.b183 + 121*m.b93*
                       m.b184 + 300*m.b93*m.b193 + 275*m.b93*m.b194 + 250*m.b93*m.b195 + 225*m.b93*m.b196 + 200*m.b93*
                       m.b197 + 225*m.b93*m.b198 + 250*m.b93*m.b199 + 275*m.b93*m.b200 + 520*m.b94*m.b129 + 480*m.b94*
                       m.b130 + 440*m.b94*m.b131 + 400*m.b94*m.b132 + 360*m.b94*m.b133 + 320*m.b94*m.b134 + 360*m.b94*
                       m.b135 + 400*m.b94*m.b136 + 208*m.b94*m.b153 + 192*m.b94*m.b154 + 176*m.b94*m.b155 + 160*m.b94*
                       m.b156 + 144*m.b94*m.b157 + 128*m.b94*m.b158 + 144*m.b94*m.b159 + 160*m.b94*m.b160 + 143*m.b94*
                       m.b177 + 132*m.b94*m.b178 + 121*m.b94*m.b179 + 110*m.b94*m.b180 + 99*m.b94*m.b181 + 88*m.b94*
                       m.b182 + 99*m.b94*m.b183 + 110*m.b94*m.b184 + 325*m.b94*m.b193 + 300*m.b94*m.b194 + 275*m.b94*
                       m.b195 + 250*m.b94*m.b196 + 225*m.b94*m.b197 + 200*m.b94*m.b198 + 225*m.b94*m.b199 + 250*m.b94*
                       m.b200 + 560*m.b95*m.b129 + 520*m.b95*m.b130 + 480*m.b95*m.b131 + 440*m.b95*m.b132 + 400*m.b95*
                       m.b133 + 360*m.b95*m.b134 + 320*m.b95*m.b135 + 360*m.b95*m.b136 + 224*m.b95*m.b153 + 208*m.b95*
                       m.b154 + 192*m.b95*m.b155 + 176*m.b95*m.b156 + 160*m.b95*m.b157 + 144*m.b95*m.b158 + 128*m.b95*
                       m.b159 + 144*m.b95*m.b160 + 154*m.b95*m.b177 + 143*m.b95*m.b178 + 132*m.b95*m.b179 + 121*m.b95*
                       m.b180 + 110*m.b95*m.b181 + 99*m.b95*m.b182 + 88*m.b95*m.b183 + 99*m.b95*m.b184 + 350*m.b95*
                       m.b193 + 325*m.b95*m.b194 + 300*m.b95*m.b195 + 275*m.b95*m.b196 + 250*m.b95*m.b197 + 225*m.b95*
                       m.b198 + 200*m.b95*m.b199 + 225*m.b95*m.b200 + 600*m.b96*m.b129 + 560*m.b96*m.b130 + 520*m.b96*
                       m.b131 + 480*m.b96*m.b132 + 440*m.b96*m.b133 + 400*m.b96*m.b134 + 360*m.b96*m.b135 + 320*m.b96*
                       m.b136 + 240*m.b96*m.b153 + 224*m.b96*m.b154 + 208*m.b96*m.b155 + 192*m.b96*m.b156 + 176*m.b96*
                       m.b157 + 160*m.b96*m.b158 + 144*m.b96*m.b159 + 128*m.b96*m.b160 + 165*m.b96*m.b177 + 154*m.b96*
                       m.b178 + 143*m.b96*m.b179 + 132*m.b96*m.b180 + 121*m.b96*m.b181 + 110*m.b96*m.b182 + 99*m.b96*
                       m.b183 + 88*m.b96*m.b184 + 375*m.b96*m.b193 + 350*m.b96*m.b194 + 325*m.b96*m.b195 + 300*m.b96*
                       m.b196 + 275*m.b96*m.b197 + 250*m.b96*m.b198 + 225*m.b96*m.b199 + 200*m.b96*m.b200 + 320*m.b97*
                       m.b121 + 360*m.b97*m.b122 + 400*m.b97*m.b123 + 440*m.b97*m.b124 + 480*m.b97*m.b125 + 520*m.b97*
                       m.b126 + 560*m.b97*m.b127 + 600*m.b97*m.b128 + 344*m.b97*m.b129 + 387*m.b97*m.b130 + 430*m.b97*
                       m.b131 + 473*m.b97*m.b132 + 516*m.b97*m.b133 + 559*m.b97*m.b134 + 602*m.b97*m.b135 + 645*m.b97*
                       m.b136 + 280*m.b97*m.b169 + 315*m.b97*m.b170 + 350*m.b97*m.b171 + 385*m.b97*m.b172 + 420*m.b97*
                       m.b173 + 455*m.b97*m.b174 + 490*m.b97*m.b175 + 525*m.b97*m.b176 + 136*m.b97*m.b193 + 153*m.b97*
                       m.b194 + 170*m.b97*m.b195 + 187*m.b97*m.b196 + 204*m.b97*m.b197 + 221*m.b97*m.b198 + 238*m.b97*
                       m.b199 + 255*m.b97*m.b200 + 336*m.b97*m.b209 + 378*m.b97*m.b210 + 420*m.b97*m.b211 + 462*m.b97*
                       m.b212 + 504*m.b97*m.b213 + 546*m.b97*m.b214 + 588*m.b97*m.b215 + 630*m.b97*m.b216 + 256*m.b97*
                       m.b217 + 288*m.b97*m.b218 + 320*m.b97*m.b219 + 352*m.b97*m.b220 + 384*m.b97*m.b221 + 416*m.b97*
                       m.b222 + 448*m.b97*m.b223 + 480*m.b97*m.b224 + 360*m.b98*m.b121 + 320*m.b98*m.b122 + 360*m.b98*
                       m.b123 + 400*m.b98*m.b124 + 440*m.b98*m.b125 + 480*m.b98*m.b126 + 520*m.b98*m.b127 + 560*m.b98*
                       m.b128 + 387*m.b98*m.b129 + 344*m.b98*m.b130 + 387*m.b98*m.b131 + 430*m.b98*m.b132 + 473*m.b98*
                       m.b133 + 516*m.b98*m.b134 + 559*m.b98*m.b135 + 602*m.b98*m.b136 + 315*m.b98*m.b169 + 280*m.b98*
                       m.b170 + 315*m.b98*m.b171 + 350*m.b98*m.b172 + 385*m.b98*m.b173 + 420*m.b98*m.b174 + 455*m.b98*
                       m.b175 + 490*m.b98*m.b176 + 153*m.b98*m.b193 + 136*m.b98*m.b194 + 153*m.b98*m.b195 + 170*m.b98*
                       m.b196 + 187*m.b98*m.b197 + 204*m.b98*m.b198 + 221*m.b98*m.b199 + 238*m.b98*m.b200 + 378*m.b98*
                       m.b209 + 336*m.b98*m.b210 + 378*m.b98*m.b211 + 420*m.b98*m.b212 + 462*m.b98*m.b213 + 504*m.b98*
                       m.b214 + 546*m.b98*m.b215 + 588*m.b98*m.b216 + 288*m.b98*m.b217 + 256*m.b98*m.b218 + 288*m.b98*
                       m.b219 + 320*m.b98*m.b220 + 352*m.b98*m.b221 + 384*m.b98*m.b222 + 416*m.b98*m.b223 + 448*m.b98*
                       m.b224 + 400*m.b99*m.b121 + 360*m.b99*m.b122 + 320*m.b99*m.b123 + 360*m.b99*m.b124 + 400*m.b99*
                       m.b125 + 440*m.b99*m.b126 + 480*m.b99*m.b127 + 520*m.b99*m.b128 + 430*m.b99*m.b129 + 387*m.b99*
                       m.b130 + 344*m.b99*m.b131 + 387*m.b99*m.b132 + 430*m.b99*m.b133 + 473*m.b99*m.b134 + 516*m.b99*
                       m.b135 + 559*m.b99*m.b136 + 350*m.b99*m.b169 + 315*m.b99*m.b170 + 280*m.b99*m.b171 + 315*m.b99*
                       m.b172 + 350*m.b99*m.b173 + 385*m.b99*m.b174 + 420*m.b99*m.b175 + 455*m.b99*m.b176 + 170*m.b99*
                       m.b193 + 153*m.b99*m.b194 + 136*m.b99*m.b195 + 153*m.b99*m.b196 + 170*m.b99*m.b197 + 187*m.b99*
                       m.b198 + 204*m.b99*m.b199 + 221*m.b99*m.b200 + 420*m.b99*m.b209 + 378*m.b99*m.b210 + 336*m.b99*
                       m.b211 + 378*m.b99*m.b212 + 420*m.b99*m.b213 + 462*m.b99*m.b214 + 504*m.b99*m.b215 + 546*m.b99*
                       m.b216 + 320*m.b99*m.b217 + 288*m.b99*m.b218 + 256*m.b99*m.b219 + 288*m.b99*m.b220 + 320*m.b99*
                       m.b221 + 352*m.b99*m.b222 + 384*m.b99*m.b223 + 416*m.b99*m.b224 + 440*m.b100*m.b121 + 400*m.b100*
                       m.b122 + 360*m.b100*m.b123 + 320*m.b100*m.b124 + 360*m.b100*m.b125 + 400*m.b100*m.b126 + 440*
                       m.b100*m.b127 + 480*m.b100*m.b128 + 473*m.b100*m.b129 + 430*m.b100*m.b130 + 387*m.b100*m.b131 + 
                       344*m.b100*m.b132 + 387*m.b100*m.b133 + 430*m.b100*m.b134 + 473*m.b100*m.b135 + 516*m.b100*m.b136
                        + 385*m.b100*m.b169 + 350*m.b100*m.b170 + 315*m.b100*m.b171 + 280*m.b100*m.b172 + 315*m.b100*
                       m.b173 + 350*m.b100*m.b174 + 385*m.b100*m.b175 + 420*m.b100*m.b176 + 187*m.b100*m.b193 + 170*
                       m.b100*m.b194 + 153*m.b100*m.b195 + 136*m.b100*m.b196 + 153*m.b100*m.b197 + 170*m.b100*m.b198 + 
                       187*m.b100*m.b199 + 204*m.b100*m.b200 + 462*m.b100*m.b209 + 420*m.b100*m.b210 + 378*m.b100*m.b211
                        + 336*m.b100*m.b212 + 378*m.b100*m.b213 + 420*m.b100*m.b214 + 462*m.b100*m.b215 + 504*m.b100*
                       m.b216 + 352*m.b100*m.b217 + 320*m.b100*m.b218 + 288*m.b100*m.b219 + 256*m.b100*m.b220 + 288*
                       m.b100*m.b221 + 320*m.b100*m.b222 + 352*m.b100*m.b223 + 384*m.b100*m.b224 + 480*m.b101*m.b121 + 
                       440*m.b101*m.b122 + 400*m.b101*m.b123 + 360*m.b101*m.b124 + 320*m.b101*m.b125 + 360*m.b101*m.b126
                        + 400*m.b101*m.b127 + 440*m.b101*m.b128 + 516*m.b101*m.b129 + 473*m.b101*m.b130 + 430*m.b101*
                       m.b131 + 387*m.b101*m.b132 + 344*m.b101*m.b133 + 387*m.b101*m.b134 + 430*m.b101*m.b135 + 473*
                       m.b101*m.b136 + 420*m.b101*m.b169 + 385*m.b101*m.b170 + 350*m.b101*m.b171 + 315*m.b101*m.b172 + 
                       280*m.b101*m.b173 + 315*m.b101*m.b174 + 350*m.b101*m.b175 + 385*m.b101*m.b176 + 204*m.b101*m.b193
                        + 187*m.b101*m.b194 + 170*m.b101*m.b195 + 153*m.b101*m.b196 + 136*m.b101*m.b197 + 153*m.b101*
                       m.b198 + 170*m.b101*m.b199 + 187*m.b101*m.b200 + 504*m.b101*m.b209 + 462*m.b101*m.b210 + 420*
                       m.b101*m.b211 + 378*m.b101*m.b212 + 336*m.b101*m.b213 + 378*m.b101*m.b214 + 420*m.b101*m.b215 + 
                       462*m.b101*m.b216 + 384*m.b101*m.b217 + 352*m.b101*m.b218 + 320*m.b101*m.b219 + 288*m.b101*m.b220
                        + 256*m.b101*m.b221 + 288*m.b101*m.b222 + 320*m.b101*m.b223 + 352*m.b101*m.b224 + 520*m.b102*
                       m.b121 + 480*m.b102*m.b122 + 440*m.b102*m.b123 + 400*m.b102*m.b124 + 360*m.b102*m.b125 + 320*
                       m.b102*m.b126 + 360*m.b102*m.b127 + 400*m.b102*m.b128 + 559*m.b102*m.b129 + 516*m.b102*m.b130 + 
                       473*m.b102*m.b131 + 430*m.b102*m.b132 + 387*m.b102*m.b133 + 344*m.b102*m.b134 + 387*m.b102*m.b135
                        + 430*m.b102*m.b136 + 455*m.b102*m.b169 + 420*m.b102*m.b170 + 385*m.b102*m.b171 + 350*m.b102*
                       m.b172 + 315*m.b102*m.b173 + 280*m.b102*m.b174 + 315*m.b102*m.b175 + 350*m.b102*m.b176 + 221*
                       m.b102*m.b193 + 204*m.b102*m.b194 + 187*m.b102*m.b195 + 170*m.b102*m.b196 + 153*m.b102*m.b197 + 
                       136*m.b102*m.b198 + 153*m.b102*m.b199 + 170*m.b102*m.b200 + 546*m.b102*m.b209 + 504*m.b102*m.b210
                        + 462*m.b102*m.b211 + 420*m.b102*m.b212 + 378*m.b102*m.b213 + 336*m.b102*m.b214 + 378*m.b102*
                       m.b215 + 420*m.b102*m.b216 + 416*m.b102*m.b217 + 384*m.b102*m.b218 + 352*m.b102*m.b219 + 320*
                       m.b102*m.b220 + 288*m.b102*m.b221 + 256*m.b102*m.b222 + 288*m.b102*m.b223 + 320*m.b102*m.b224 + 
                       560*m.b103*m.b121 + 520*m.b103*m.b122 + 480*m.b103*m.b123 + 440*m.b103*m.b124 + 400*m.b103*m.b125
                        + 360*m.b103*m.b126 + 320*m.b103*m.b127 + 360*m.b103*m.b128 + 602*m.b103*m.b129 + 559*m.b103*
                       m.b130 + 516*m.b103*m.b131 + 473*m.b103*m.b132 + 430*m.b103*m.b133 + 387*m.b103*m.b134 + 344*
                       m.b103*m.b135 + 387*m.b103*m.b136 + 490*m.b103*m.b169 + 455*m.b103*m.b170 + 420*m.b103*m.b171 + 
                       385*m.b103*m.b172 + 350*m.b103*m.b173 + 315*m.b103*m.b174 + 280*m.b103*m.b175 + 315*m.b103*m.b176
                        + 238*m.b103*m.b193 + 221*m.b103*m.b194 + 204*m.b103*m.b195 + 187*m.b103*m.b196 + 170*m.b103*
                       m.b197 + 153*m.b103*m.b198 + 136*m.b103*m.b199 + 153*m.b103*m.b200 + 588*m.b103*m.b209 + 546*
                       m.b103*m.b210 + 504*m.b103*m.b211 + 462*m.b103*m.b212 + 420*m.b103*m.b213 + 378*m.b103*m.b214 + 
                       336*m.b103*m.b215 + 378*m.b103*m.b216 + 448*m.b103*m.b217 + 416*m.b103*m.b218 + 384*m.b103*m.b219
                        + 352*m.b103*m.b220 + 320*m.b103*m.b221 + 288*m.b103*m.b222 + 256*m.b103*m.b223 + 288*m.b103*
                       m.b224 + 600*m.b104*m.b121 + 560*m.b104*m.b122 + 520*m.b104*m.b123 + 480*m.b104*m.b124 + 440*
                       m.b104*m.b125 + 400*m.b104*m.b126 + 360*m.b104*m.b127 + 320*m.b104*m.b128 + 645*m.b104*m.b129 + 
                       602*m.b104*m.b130 + 559*m.b104*m.b131 + 516*m.b104*m.b132 + 473*m.b104*m.b133 + 430*m.b104*m.b134
                        + 387*m.b104*m.b135 + 344*m.b104*m.b136 + 525*m.b104*m.b169 + 490*m.b104*m.b170 + 455*m.b104*
                       m.b171 + 420*m.b104*m.b172 + 385*m.b104*m.b173 + 350*m.b104*m.b174 + 315*m.b104*m.b175 + 280*
                       m.b104*m.b176 + 255*m.b104*m.b193 + 238*m.b104*m.b194 + 221*m.b104*m.b195 + 204*m.b104*m.b196 + 
                       187*m.b104*m.b197 + 170*m.b104*m.b198 + 153*m.b104*m.b199 + 136*m.b104*m.b200 + 630*m.b104*m.b209
                        + 588*m.b104*m.b210 + 546*m.b104*m.b211 + 504*m.b104*m.b212 + 462*m.b104*m.b213 + 420*m.b104*
                       m.b214 + 378*m.b104*m.b215 + 336*m.b104*m.b216 + 480*m.b104*m.b217 + 448*m.b104*m.b218 + 416*
                       m.b104*m.b219 + 384*m.b104*m.b220 + 352*m.b104*m.b221 + 320*m.b104*m.b222 + 288*m.b104*m.b223 + 
                       256*m.b104*m.b224 + 320*m.b105*m.b129 + 360*m.b105*m.b130 + 400*m.b105*m.b131 + 440*m.b105*m.b132
                        + 480*m.b105*m.b133 + 520*m.b105*m.b134 + 560*m.b105*m.b135 + 600*m.b105*m.b136 + 384*m.b105*
                       m.b161 + 432*m.b105*m.b162 + 480*m.b105*m.b163 + 528*m.b105*m.b164 + 576*m.b105*m.b165 + 624*
                       m.b105*m.b166 + 672*m.b105*m.b167 + 720*m.b105*m.b168 + 184*m.b105*m.b201 + 207*m.b105*m.b202 + 
                       230*m.b105*m.b203 + 253*m.b105*m.b204 + 276*m.b105*m.b205 + 299*m.b105*m.b206 + 322*m.b105*m.b207
                        + 345*m.b105*m.b208 + 232*m.b105*m.b217 + 261*m.b105*m.b218 + 290*m.b105*m.b219 + 319*m.b105*
                       m.b220 + 348*m.b105*m.b221 + 377*m.b105*m.b222 + 406*m.b105*m.b223 + 435*m.b105*m.b224 + 360*
                       m.b106*m.b129 + 320*m.b106*m.b130 + 360*m.b106*m.b131 + 400*m.b106*m.b132 + 440*m.b106*m.b133 + 
                       480*m.b106*m.b134 + 520*m.b106*m.b135 + 560*m.b106*m.b136 + 432*m.b106*m.b161 + 384*m.b106*m.b162
                        + 432*m.b106*m.b163 + 480*m.b106*m.b164 + 528*m.b106*m.b165 + 576*m.b106*m.b166 + 624*m.b106*
                       m.b167 + 672*m.b106*m.b168 + 207*m.b106*m.b201 + 184*m.b106*m.b202 + 207*m.b106*m.b203 + 230*
                       m.b106*m.b204 + 253*m.b106*m.b205 + 276*m.b106*m.b206 + 299*m.b106*m.b207 + 322*m.b106*m.b208 + 
                       261*m.b106*m.b217 + 232*m.b106*m.b218 + 261*m.b106*m.b219 + 290*m.b106*m.b220 + 319*m.b106*m.b221
                        + 348*m.b106*m.b222 + 377*m.b106*m.b223 + 406*m.b106*m.b224 + 400*m.b107*m.b129 + 360*m.b107*
                       m.b130 + 320*m.b107*m.b131 + 360*m.b107*m.b132 + 400*m.b107*m.b133 + 440*m.b107*m.b134 + 480*
                       m.b107*m.b135 + 520*m.b107*m.b136 + 480*m.b107*m.b161 + 432*m.b107*m.b162 + 384*m.b107*m.b163 + 
                       432*m.b107*m.b164 + 480*m.b107*m.b165 + 528*m.b107*m.b166 + 576*m.b107*m.b167 + 624*m.b107*m.b168
                        + 230*m.b107*m.b201 + 207*m.b107*m.b202 + 184*m.b107*m.b203 + 207*m.b107*m.b204 + 230*m.b107*
                       m.b205 + 253*m.b107*m.b206 + 276*m.b107*m.b207 + 299*m.b107*m.b208 + 290*m.b107*m.b217 + 261*
                       m.b107*m.b218 + 232*m.b107*m.b219 + 261*m.b107*m.b220 + 290*m.b107*m.b221 + 319*m.b107*m.b222 + 
                       348*m.b107*m.b223 + 377*m.b107*m.b224 + 440*m.b108*m.b129 + 400*m.b108*m.b130 + 360*m.b108*m.b131
                        + 320*m.b108*m.b132 + 360*m.b108*m.b133 + 400*m.b108*m.b134 + 440*m.b108*m.b135 + 480*m.b108*
                       m.b136 + 528*m.b108*m.b161 + 480*m.b108*m.b162 + 432*m.b108*m.b163 + 384*m.b108*m.b164 + 432*
                       m.b108*m.b165 + 480*m.b108*m.b166 + 528*m.b108*m.b167 + 576*m.b108*m.b168 + 253*m.b108*m.b201 + 
                       230*m.b108*m.b202 + 207*m.b108*m.b203 + 184*m.b108*m.b204 + 207*m.b108*m.b205 + 230*m.b108*m.b206
                        + 253*m.b108*m.b207 + 276*m.b108*m.b208 + 319*m.b108*m.b217 + 290*m.b108*m.b218 + 261*m.b108*
                       m.b219 + 232*m.b108*m.b220 + 261*m.b108*m.b221 + 290*m.b108*m.b222 + 319*m.b108*m.b223 + 348*
                       m.b108*m.b224 + 480*m.b109*m.b129 + 440*m.b109*m.b130 + 400*m.b109*m.b131 + 360*m.b109*m.b132 + 
                       320*m.b109*m.b133 + 360*m.b109*m.b134 + 400*m.b109*m.b135 + 440*m.b109*m.b136 + 576*m.b109*m.b161
                        + 528*m.b109*m.b162 + 480*m.b109*m.b163 + 432*m.b109*m.b164 + 384*m.b109*m.b165 + 432*m.b109*
                       m.b166 + 480*m.b109*m.b167 + 528*m.b109*m.b168 + 276*m.b109*m.b201 + 253*m.b109*m.b202 + 230*
                       m.b109*m.b203 + 207*m.b109*m.b204 + 184*m.b109*m.b205 + 207*m.b109*m.b206 + 230*m.b109*m.b207 + 
                       253*m.b109*m.b208 + 348*m.b109*m.b217 + 319*m.b109*m.b218 + 290*m.b109*m.b219 + 261*m.b109*m.b220
                        + 232*m.b109*m.b221 + 261*m.b109*m.b222 + 290*m.b109*m.b223 + 319*m.b109*m.b224 + 520*m.b110*
                       m.b129 + 480*m.b110*m.b130 + 440*m.b110*m.b131 + 400*m.b110*m.b132 + 360*m.b110*m.b133 + 320*
                       m.b110*m.b134 + 360*m.b110*m.b135 + 400*m.b110*m.b136 + 624*m.b110*m.b161 + 576*m.b110*m.b162 + 
                       528*m.b110*m.b163 + 480*m.b110*m.b164 + 432*m.b110*m.b165 + 384*m.b110*m.b166 + 432*m.b110*m.b167
                        + 480*m.b110*m.b168 + 299*m.b110*m.b201 + 276*m.b110*m.b202 + 253*m.b110*m.b203 + 230*m.b110*
                       m.b204 + 207*m.b110*m.b205 + 184*m.b110*m.b206 + 207*m.b110*m.b207 + 230*m.b110*m.b208 + 377*
                       m.b110*m.b217 + 348*m.b110*m.b218 + 319*m.b110*m.b219 + 290*m.b110*m.b220 + 261*m.b110*m.b221 + 
                       232*m.b110*m.b222 + 261*m.b110*m.b223 + 290*m.b110*m.b224 + 560*m.b111*m.b129 + 520*m.b111*m.b130
                        + 480*m.b111*m.b131 + 440*m.b111*m.b132 + 400*m.b111*m.b133 + 360*m.b111*m.b134 + 320*m.b111*
                       m.b135 + 360*m.b111*m.b136 + 672*m.b111*m.b161 + 624*m.b111*m.b162 + 576*m.b111*m.b163 + 528*
                       m.b111*m.b164 + 480*m.b111*m.b165 + 432*m.b111*m.b166 + 384*m.b111*m.b167 + 432*m.b111*m.b168 + 
                       322*m.b111*m.b201 + 299*m.b111*m.b202 + 276*m.b111*m.b203 + 253*m.b111*m.b204 + 230*m.b111*m.b205
                        + 207*m.b111*m.b206 + 184*m.b111*m.b207 + 207*m.b111*m.b208 + 406*m.b111*m.b217 + 377*m.b111*
                       m.b218 + 348*m.b111*m.b219 + 319*m.b111*m.b220 + 290*m.b111*m.b221 + 261*m.b111*m.b222 + 232*
                       m.b111*m.b223 + 261*m.b111*m.b224 + 600*m.b112*m.b129 + 560*m.b112*m.b130 + 520*m.b112*m.b131 + 
                       480*m.b112*m.b132 + 440*m.b112*m.b133 + 400*m.b112*m.b134 + 360*m.b112*m.b135 + 320*m.b112*m.b136
                        + 720*m.b112*m.b161 + 672*m.b112*m.b162 + 624*m.b112*m.b163 + 576*m.b112*m.b164 + 528*m.b112*
                       m.b165 + 480*m.b112*m.b166 + 432*m.b112*m.b167 + 384*m.b112*m.b168 + 345*m.b112*m.b201 + 322*
                       m.b112*m.b202 + 299*m.b112*m.b203 + 276*m.b112*m.b204 + 253*m.b112*m.b205 + 230*m.b112*m.b206 + 
                       207*m.b112*m.b207 + 184*m.b112*m.b208 + 435*m.b112*m.b217 + 406*m.b112*m.b218 + 377*m.b112*m.b219
                        + 348*m.b112*m.b220 + 319*m.b112*m.b221 + 290*m.b112*m.b222 + 261*m.b112*m.b223 + 232*m.b112*
                       m.b224 + 184*m.b113*m.b185 + 207*m.b113*m.b186 + 230*m.b113*m.b187 + 253*m.b113*m.b188 + 276*
                       m.b113*m.b189 + 299*m.b113*m.b190 + 322*m.b113*m.b191 + 345*m.b113*m.b192 + 184*m.b113*m.b209 + 
                       207*m.b113*m.b210 + 230*m.b113*m.b211 + 253*m.b113*m.b212 + 276*m.b113*m.b213 + 299*m.b113*m.b214
                        + 322*m.b113*m.b215 + 345*m.b113*m.b216 + 207*m.b114*m.b185 + 184*m.b114*m.b186 + 207*m.b114*
                       m.b187 + 230*m.b114*m.b188 + 253*m.b114*m.b189 + 276*m.b114*m.b190 + 299*m.b114*m.b191 + 322*
                       m.b114*m.b192 + 207*m.b114*m.b209 + 184*m.b114*m.b210 + 207*m.b114*m.b211 + 230*m.b114*m.b212 + 
                       253*m.b114*m.b213 + 276*m.b114*m.b214 + 299*m.b114*m.b215 + 322*m.b114*m.b216 + 230*m.b115*m.b185
                        + 207*m.b115*m.b186 + 184*m.b115*m.b187 + 207*m.b115*m.b188 + 230*m.b115*m.b189 + 253*m.b115*
                       m.b190 + 276*m.b115*m.b191 + 299*m.b115*m.b192 + 230*m.b115*m.b209 + 207*m.b115*m.b210 + 184*
                       m.b115*m.b211 + 207*m.b115*m.b212 + 230*m.b115*m.b213 + 253*m.b115*m.b214 + 276*m.b115*m.b215 + 
                       299*m.b115*m.b216 + 253*m.b116*m.b185 + 230*m.b116*m.b186 + 207*m.b116*m.b187 + 184*m.b116*m.b188
                        + 207*m.b116*m.b189 + 230*m.b116*m.b190 + 253*m.b116*m.b191 + 276*m.b116*m.b192 + 253*m.b116*
                       m.b209 + 230*m.b116*m.b210 + 207*m.b116*m.b211 + 184*m.b116*m.b212 + 207*m.b116*m.b213 + 230*
                       m.b116*m.b214 + 253*m.b116*m.b215 + 276*m.b116*m.b216 + 276*m.b117*m.b185 + 253*m.b117*m.b186 + 
                       230*m.b117*m.b187 + 207*m.b117*m.b188 + 184*m.b117*m.b189 + 207*m.b117*m.b190 + 230*m.b117*m.b191
                        + 253*m.b117*m.b192 + 276*m.b117*m.b209 + 253*m.b117*m.b210 + 230*m.b117*m.b211 + 207*m.b117*
                       m.b212 + 184*m.b117*m.b213 + 207*m.b117*m.b214 + 230*m.b117*m.b215 + 253*m.b117*m.b216 + 299*
                       m.b118*m.b185 + 276*m.b118*m.b186 + 253*m.b118*m.b187 + 230*m.b118*m.b188 + 207*m.b118*m.b189 + 
                       184*m.b118*m.b190 + 207*m.b118*m.b191 + 230*m.b118*m.b192 + 299*m.b118*m.b209 + 276*m.b118*m.b210
                        + 253*m.b118*m.b211 + 230*m.b118*m.b212 + 207*m.b118*m.b213 + 184*m.b118*m.b214 + 207*m.b118*
                       m.b215 + 230*m.b118*m.b216 + 322*m.b119*m.b185 + 299*m.b119*m.b186 + 276*m.b119*m.b187 + 253*
                       m.b119*m.b188 + 230*m.b119*m.b189 + 207*m.b119*m.b190 + 184*m.b119*m.b191 + 207*m.b119*m.b192 + 
                       322*m.b119*m.b209 + 299*m.b119*m.b210 + 276*m.b119*m.b211 + 253*m.b119*m.b212 + 230*m.b119*m.b213
                        + 207*m.b119*m.b214 + 184*m.b119*m.b215 + 207*m.b119*m.b216 + 345*m.b120*m.b185 + 322*m.b120*
                       m.b186 + 299*m.b120*m.b187 + 276*m.b120*m.b188 + 253*m.b120*m.b189 + 230*m.b120*m.b190 + 207*
                       m.b120*m.b191 + 184*m.b120*m.b192 + 345*m.b120*m.b209 + 322*m.b120*m.b210 + 299*m.b120*m.b211 + 
                       276*m.b120*m.b212 + 253*m.b120*m.b213 + 230*m.b120*m.b214 + 207*m.b120*m.b215 + 184*m.b120*m.b216
                       , sense=minimize)

m.c2 = Constraint(expr=   m.b1 + m.b2 + m.b3 + m.b4 + m.b5 + m.b6 + m.b7 + m.b8 == 1)

m.c3 = Constraint(expr=   m.b9 + m.b10 + m.b11 + m.b12 + m.b13 + m.b14 + m.b15 + m.b16 == 1)

m.c4 = Constraint(expr=   m.b17 + m.b18 + m.b19 + m.b20 + m.b21 + m.b22 + m.b23 + m.b24 == 1)

m.c5 = Constraint(expr=   m.b25 + m.b26 + m.b27 + m.b28 + m.b29 + m.b30 + m.b31 + m.b32 == 1)

m.c6 = Constraint(expr=   m.b33 + m.b34 + m.b35 + m.b36 + m.b37 + m.b38 + m.b39 + m.b40 == 1)

m.c7 = Constraint(expr=   m.b41 + m.b42 + m.b43 + m.b44 + m.b45 + m.b46 + m.b47 + m.b48 == 1)

m.c8 = Constraint(expr=   m.b49 + m.b50 + m.b51 + m.b52 + m.b53 + m.b54 + m.b55 + m.b56 == 1)

m.c9 = Constraint(expr=   m.b57 + m.b58 + m.b59 + m.b60 + m.b61 + m.b62 + m.b63 + m.b64 == 1)

m.c10 = Constraint(expr=   m.b65 + m.b66 + m.b67 + m.b68 + m.b69 + m.b70 + m.b71 + m.b72 == 1)

m.c11 = Constraint(expr=   m.b73 + m.b74 + m.b75 + m.b76 + m.b77 + m.b78 + m.b79 + m.b80 == 1)

m.c12 = Constraint(expr=   m.b81 + m.b82 + m.b83 + m.b84 + m.b85 + m.b86 + m.b87 + m.b88 == 1)

m.c13 = Constraint(expr=   m.b89 + m.b90 + m.b91 + m.b92 + m.b93 + m.b94 + m.b95 + m.b96 == 1)

m.c14 = Constraint(expr=   m.b97 + m.b98 + m.b99 + m.b100 + m.b101 + m.b102 + m.b103 + m.b104 == 1)

m.c15 = Constraint(expr=   m.b105 + m.b106 + m.b107 + m.b108 + m.b109 + m.b110 + m.b111 + m.b112 == 1)

m.c16 = Constraint(expr=   m.b113 + m.b114 + m.b115 + m.b116 + m.b117 + m.b118 + m.b119 + m.b120 == 1)

m.c17 = Constraint(expr=   m.b121 + m.b122 + m.b123 + m.b124 + m.b125 + m.b126 + m.b127 + m.b128 == 1)

m.c18 = Constraint(expr=   m.b129 + m.b130 + m.b131 + m.b132 + m.b133 + m.b134 + m.b135 + m.b136 == 1)

m.c19 = Constraint(expr=   m.b137 + m.b138 + m.b139 + m.b140 + m.b141 + m.b142 + m.b143 + m.b144 == 1)

m.c20 = Constraint(expr=   m.b145 + m.b146 + m.b147 + m.b148 + m.b149 + m.b150 + m.b151 + m.b152 == 1)

m.c21 = Constraint(expr=   m.b153 + m.b154 + m.b155 + m.b156 + m.b157 + m.b158 + m.b159 + m.b160 == 1)

m.c22 = Constraint(expr=   m.b161 + m.b162 + m.b163 + m.b164 + m.b165 + m.b166 + m.b167 + m.b168 == 1)

m.c23 = Constraint(expr=   m.b169 + m.b170 + m.b171 + m.b172 + m.b173 + m.b174 + m.b175 + m.b176 == 1)

m.c24 = Constraint(expr=   m.b177 + m.b178 + m.b179 + m.b180 + m.b181 + m.b182 + m.b183 + m.b184 == 1)

m.c25 = Constraint(expr=   m.b185 + m.b186 + m.b187 + m.b188 + m.b189 + m.b190 + m.b191 + m.b192 == 1)

m.c26 = Constraint(expr=   m.b193 + m.b194 + m.b195 + m.b196 + m.b197 + m.b198 + m.b199 + m.b200 == 1)

m.c27 = Constraint(expr=   m.b201 + m.b202 + m.b203 + m.b204 + m.b205 + m.b206 + m.b207 + m.b208 == 1)

m.c28 = Constraint(expr=   m.b209 + m.b210 + m.b211 + m.b212 + m.b213 + m.b214 + m.b215 + m.b216 == 1)

m.c29 = Constraint(expr=   m.b217 + m.b218 + m.b219 + m.b220 + m.b221 + m.b222 + m.b223 + m.b224 == 1)

m.c30 = Constraint(expr=   m.b225 + m.b226 + m.b227 + m.b228 + m.b229 + m.b230 + m.b231 + m.b232 == 1)

m.c31 = Constraint(expr=   m.b233 + m.b234 + m.b235 + m.b236 + m.b237 + m.b238 + m.b239 + m.b240 == 1)

m.c32 = Constraint(expr=   81*m.b1 + 114*m.b9 + 100*m.b17 + 50*m.b25 + 51*m.b33 + 196*m.b41 + 96*m.b49 + 128*m.b57
                         + 83*m.b65 + 189*m.b73 + 113*m.b81 + 92*m.b89 + 209*m.b97 + 140*m.b105 + 46*m.b113 <= 233)

m.c33 = Constraint(expr=   81*m.b2 + 114*m.b10 + 100*m.b18 + 50*m.b26 + 51*m.b34 + 196*m.b42 + 96*m.b50 + 128*m.b58
                         + 83*m.b66 + 189*m.b74 + 113*m.b82 + 92*m.b90 + 209*m.b98 + 140*m.b106 + 46*m.b114 <= 233)

m.c34 = Constraint(expr=   81*m.b3 + 114*m.b11 + 100*m.b19 + 50*m.b27 + 51*m.b35 + 196*m.b43 + 96*m.b51 + 128*m.b59
                         + 83*m.b67 + 189*m.b75 + 113*m.b83 + 92*m.b91 + 209*m.b99 + 140*m.b107 + 46*m.b115 <= 233)

m.c35 = Constraint(expr=   81*m.b4 + 114*m.b12 + 100*m.b20 + 50*m.b28 + 51*m.b36 + 196*m.b44 + 96*m.b52 + 128*m.b60
                         + 83*m.b68 + 189*m.b76 + 113*m.b84 + 92*m.b92 + 209*m.b100 + 140*m.b108 + 46*m.b116 <= 233)

m.c36 = Constraint(expr=   81*m.b5 + 114*m.b13 + 100*m.b21 + 50*m.b29 + 51*m.b37 + 196*m.b45 + 96*m.b53 + 128*m.b61
                         + 83*m.b69 + 189*m.b77 + 113*m.b85 + 92*m.b93 + 209*m.b101 + 140*m.b109 + 46*m.b117 <= 233)

m.c37 = Constraint(expr=   81*m.b6 + 114*m.b14 + 100*m.b22 + 50*m.b30 + 51*m.b38 + 196*m.b46 + 96*m.b54 + 128*m.b62
                         + 83*m.b70 + 189*m.b78 + 113*m.b86 + 92*m.b94 + 209*m.b102 + 140*m.b110 + 46*m.b118 <= 233)

m.c38 = Constraint(expr=   81*m.b7 + 114*m.b15 + 100*m.b23 + 50*m.b31 + 51*m.b39 + 196*m.b47 + 96*m.b55 + 128*m.b63
                         + 83*m.b71 + 189*m.b79 + 113*m.b87 + 92*m.b95 + 209*m.b103 + 140*m.b111 + 46*m.b119 <= 233)

m.c39 = Constraint(expr=   81*m.b8 + 114*m.b16 + 100*m.b24 + 50*m.b32 + 51*m.b40 + 196*m.b48 + 96*m.b56 + 128*m.b64
                         + 83*m.b72 + 189*m.b80 + 113*m.b88 + 92*m.b96 + 209*m.b104 + 140*m.b112 + 46*m.b120 <= 233)

m.c40 = Constraint(expr=   68*m.b121 + 200*m.b129 + 49*m.b137 + 181*m.b145 + 60*m.b153 + 145*m.b161 + 105*m.b169
                         + 79*m.b177 + 107*m.b185 + 117*m.b193 + 131*m.b201 + 117*m.b209 + 137*m.b217 + 71*m.b225
                         + 121*m.b233 <= 233)

m.c41 = Constraint(expr=   68*m.b122 + 200*m.b130 + 49*m.b138 + 181*m.b146 + 60*m.b154 + 145*m.b162 + 105*m.b170
                         + 79*m.b178 + 107*m.b186 + 117*m.b194 + 131*m.b202 + 117*m.b210 + 137*m.b218 + 71*m.b226
                         + 121*m.b234 <= 233)

m.c42 = Constraint(expr=   68*m.b123 + 200*m.b131 + 49*m.b139 + 181*m.b147 + 60*m.b155 + 145*m.b163 + 105*m.b171
                         + 79*m.b179 + 107*m.b187 + 117*m.b195 + 131*m.b203 + 117*m.b211 + 137*m.b219 + 71*m.b227
                         + 121*m.b235 <= 233)

m.c43 = Constraint(expr=   68*m.b124 + 200*m.b132 + 49*m.b140 + 181*m.b148 + 60*m.b156 + 145*m.b164 + 105*m.b172
                         + 79*m.b180 + 107*m.b188 + 117*m.b196 + 131*m.b204 + 117*m.b212 + 137*m.b220 + 71*m.b228
                         + 121*m.b236 <= 233)

m.c44 = Constraint(expr=   68*m.b125 + 200*m.b133 + 49*m.b141 + 181*m.b149 + 60*m.b157 + 145*m.b165 + 105*m.b173
                         + 79*m.b181 + 107*m.b189 + 117*m.b197 + 131*m.b205 + 117*m.b213 + 137*m.b221 + 71*m.b229
                         + 121*m.b237 <= 233)

m.c45 = Constraint(expr=   68*m.b126 + 200*m.b134 + 49*m.b142 + 181*m.b150 + 60*m.b158 + 145*m.b166 + 105*m.b174
                         + 79*m.b182 + 107*m.b190 + 117*m.b198 + 131*m.b206 + 117*m.b214 + 137*m.b222 + 71*m.b230
                         + 121*m.b238 <= 233)

m.c46 = Constraint(expr=   68*m.b127 + 200*m.b135 + 49*m.b143 + 181*m.b151 + 60*m.b159 + 145*m.b167 + 105*m.b175
                         + 79*m.b183 + 107*m.b191 + 117*m.b199 + 131*m.b207 + 117*m.b215 + 137*m.b223 + 71*m.b231
                         + 121*m.b239 <= 233)

m.c47 = Constraint(expr=   68*m.b128 + 200*m.b136 + 49*m.b144 + 181*m.b152 + 60*m.b160 + 145*m.b168 + 105*m.b176
                         + 79*m.b184 + 107*m.b192 + 117*m.b200 + 131*m.b208 + 117*m.b216 + 137*m.b224 + 71*m.b232
                         + 121*m.b240 <= 233)
