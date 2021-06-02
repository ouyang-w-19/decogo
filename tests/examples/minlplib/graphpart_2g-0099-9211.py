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

m.obj = Objective(expr=75260*m.b1*m.b4 - 15525*m.b1*m.b25 + 1448*m.b1*m.b28 + 35332*m.b1*m.b217 + 75260*m.b2*m.b5 - 
                       15525*m.b2*m.b26 + 1448*m.b2*m.b29 + 35332*m.b2*m.b218 + 75260*m.b3*m.b6 - 15525*m.b3*m.b27 + 
                       1448*m.b3*m.b30 + 35332*m.b3*m.b219 + 65166*m.b4*m.b7 - 231070*m.b4*m.b31 - 32003*m.b4*m.b220 + 
                       65166*m.b5*m.b8 - 231070*m.b5*m.b32 - 32003*m.b5*m.b221 + 65166*m.b6*m.b9 - 231070*m.b6*m.b33 - 
                       32003*m.b6*m.b222 + 36246*m.b7*m.b10 + 54442*m.b7*m.b34 - 124520*m.b7*m.b223 + 36246*m.b8*m.b11
                        + 54442*m.b8*m.b35 - 124520*m.b8*m.b224 + 36246*m.b9*m.b12 + 54442*m.b9*m.b36 - 124520*m.b9*
                       m.b225 - 10022*m.b10*m.b13 + 170366*m.b10*m.b37 + 87801*m.b10*m.b226 - 10022*m.b11*m.b14 + 170366
                       *m.b11*m.b38 + 87801*m.b11*m.b227 - 10022*m.b12*m.b15 + 170366*m.b12*m.b39 + 87801*m.b12*m.b228
                        + 13961*m.b13*m.b16 + 95303*m.b13*m.b40 + 31421*m.b13*m.b229 + 13961*m.b14*m.b17 + 95303*m.b14*
                       m.b41 + 31421*m.b14*m.b230 + 13961*m.b15*m.b18 + 95303*m.b15*m.b42 + 31421*m.b15*m.b231 + 35992*
                       m.b16*m.b19 + 134080*m.b16*m.b43 - 130633*m.b16*m.b232 + 35992*m.b17*m.b20 + 134080*m.b17*m.b44
                        - 130633*m.b17*m.b233 + 35992*m.b18*m.b21 + 134080*m.b18*m.b45 - 130633*m.b18*m.b234 - 95577*
                       m.b19*m.b22 + 52867*m.b19*m.b46 - 46358*m.b19*m.b235 - 95577*m.b20*m.b23 + 52867*m.b20*m.b47 - 
                       46358*m.b20*m.b236 - 95577*m.b21*m.b24 + 52867*m.b21*m.b48 - 46358*m.b21*m.b237 - 135541*m.b22*
                       m.b25 + 244498*m.b22*m.b49 - 125443*m.b22*m.b238 - 135541*m.b23*m.b26 + 244498*m.b23*m.b50 - 
                       125443*m.b23*m.b239 - 135541*m.b24*m.b27 + 244498*m.b24*m.b51 - 125443*m.b24*m.b240 + 131606*
                       m.b25*m.b52 + 25578*m.b25*m.b241 + 131606*m.b26*m.b53 + 25578*m.b26*m.b242 + 131606*m.b27*m.b54
                        + 25578*m.b27*m.b243 + 59601*m.b28*m.b31 + 231059*m.b28*m.b52 - 84412*m.b28*m.b55 + 59601*m.b29*
                       m.b32 + 231059*m.b29*m.b53 - 84412*m.b29*m.b56 + 59601*m.b30*m.b33 + 231059*m.b30*m.b54 - 84412*
                       m.b30*m.b57 - 71617*m.b31*m.b34 - 72573*m.b31*m.b58 - 71617*m.b32*m.b35 - 72573*m.b32*m.b59 - 
                       71617*m.b33*m.b36 - 72573*m.b33*m.b60 + 29323*m.b34*m.b37 + 142316*m.b34*m.b61 + 29323*m.b35*
                       m.b38 + 142316*m.b35*m.b62 + 29323*m.b36*m.b39 + 142316*m.b36*m.b63 + 79296*m.b37*m.b40 + 2887*
                       m.b37*m.b64 + 79296*m.b38*m.b41 + 2887*m.b38*m.b65 + 79296*m.b39*m.b42 + 2887*m.b39*m.b66 + 18134
                       *m.b40*m.b43 - 24223*m.b40*m.b67 + 18134*m.b41*m.b44 - 24223*m.b41*m.b68 + 18134*m.b42*m.b45 - 
                       24223*m.b42*m.b69 - 36436*m.b43*m.b46 - 66297*m.b43*m.b70 - 36436*m.b44*m.b47 - 66297*m.b44*m.b71
                        - 36436*m.b45*m.b48 - 66297*m.b45*m.b72 - 31521*m.b46*m.b49 - 140287*m.b46*m.b73 - 31521*m.b47*
                       m.b50 - 140287*m.b47*m.b74 - 31521*m.b48*m.b51 - 140287*m.b48*m.b75 + 25570*m.b49*m.b52 + 23752*
                       m.b49*m.b76 + 25570*m.b50*m.b53 + 23752*m.b50*m.b77 + 25570*m.b51*m.b54 + 23752*m.b51*m.b78 + 
                       87355*m.b52*m.b79 + 87355*m.b53*m.b80 + 87355*m.b54*m.b81 + 170774*m.b55*m.b58 - 56803*m.b55*
                       m.b79 + 121940*m.b55*m.b82 + 170774*m.b56*m.b59 - 56803*m.b56*m.b80 + 121940*m.b56*m.b83 + 170774
                       *m.b57*m.b60 - 56803*m.b57*m.b81 + 121940*m.b57*m.b84 - 26527*m.b58*m.b61 - 130207*m.b58*m.b85 - 
                       26527*m.b59*m.b62 - 130207*m.b59*m.b86 - 26527*m.b60*m.b63 - 130207*m.b60*m.b87 + 6132*m.b61*
                       m.b64 + 277583*m.b61*m.b88 + 6132*m.b62*m.b65 + 277583*m.b62*m.b89 + 6132*m.b63*m.b66 + 277583*
                       m.b63*m.b90 + 22357*m.b64*m.b67 - 42350*m.b64*m.b91 + 22357*m.b65*m.b68 - 42350*m.b65*m.b92 + 
                       22357*m.b66*m.b69 - 42350*m.b66*m.b93 + 93718*m.b67*m.b70 - 47716*m.b67*m.b94 + 93718*m.b68*m.b71
                        - 47716*m.b68*m.b95 + 93718*m.b69*m.b72 - 47716*m.b69*m.b96 + 15950*m.b70*m.b73 - 196992*m.b70*
                       m.b97 + 15950*m.b71*m.b74 - 196992*m.b71*m.b98 + 15950*m.b72*m.b75 - 196992*m.b72*m.b99 + 24740*
                       m.b73*m.b76 + 12563*m.b73*m.b100 + 24740*m.b74*m.b77 + 12563*m.b74*m.b101 + 24740*m.b75*m.b78 + 
                       12563*m.b75*m.b102 - 94991*m.b76*m.b79 + 60642*m.b76*m.b103 - 94991*m.b77*m.b80 + 60642*m.b77*
                       m.b104 - 94991*m.b78*m.b81 + 60642*m.b78*m.b105 + 1123*m.b79*m.b106 + 1123*m.b80*m.b107 + 1123*
                       m.b81*m.b108 - 55825*m.b82*m.b85 + 197268*m.b82*m.b106 + 56412*m.b82*m.b109 - 55825*m.b83*m.b86
                        + 197268*m.b83*m.b107 + 56412*m.b83*m.b110 - 55825*m.b84*m.b87 + 197268*m.b84*m.b108 + 56412*
                       m.b84*m.b111 + 86140*m.b85*m.b88 + 154282*m.b85*m.b112 + 86140*m.b86*m.b89 + 154282*m.b86*m.b113
                        + 86140*m.b87*m.b90 + 154282*m.b87*m.b114 + 88205*m.b88*m.b91 - 1683*m.b88*m.b115 + 88205*m.b89*
                       m.b92 - 1683*m.b89*m.b116 + 88205*m.b90*m.b93 - 1683*m.b90*m.b117 - 104232*m.b91*m.b94 + 91137*
                       m.b91*m.b118 - 104232*m.b92*m.b95 + 91137*m.b92*m.b119 - 104232*m.b93*m.b96 + 91137*m.b93*m.b120
                        - 67932*m.b94*m.b97 + 29333*m.b94*m.b121 - 67932*m.b95*m.b98 + 29333*m.b95*m.b122 - 67932*m.b96*
                       m.b99 + 29333*m.b96*m.b123 + 157198*m.b97*m.b100 + 2407*m.b97*m.b124 + 157198*m.b98*m.b101 + 2407
                       *m.b98*m.b125 + 157198*m.b99*m.b102 + 2407*m.b99*m.b126 - 105460*m.b100*m.b103 + 2767*m.b100*
                       m.b127 - 105460*m.b101*m.b104 + 2767*m.b101*m.b128 - 105460*m.b102*m.b105 + 2767*m.b102*m.b129 + 
                       109601*m.b103*m.b106 + 81889*m.b103*m.b130 + 109601*m.b104*m.b107 + 81889*m.b104*m.b131 + 109601*
                       m.b105*m.b108 + 81889*m.b105*m.b132 - 43809*m.b106*m.b133 - 43809*m.b107*m.b134 - 43809*m.b108*
                       m.b135 + 33621*m.b109*m.b112 + 117056*m.b109*m.b133 + 80571*m.b109*m.b136 + 33621*m.b110*m.b113
                        + 117056*m.b110*m.b134 + 80571*m.b110*m.b137 + 33621*m.b111*m.b114 + 117056*m.b111*m.b135 + 
                       80571*m.b111*m.b138 - 40940*m.b112*m.b115 + 40376*m.b112*m.b139 - 40940*m.b113*m.b116 + 40376*
                       m.b113*m.b140 - 40940*m.b114*m.b117 + 40376*m.b114*m.b141 - 36171*m.b115*m.b118 + 51363*m.b115*
                       m.b142 - 36171*m.b116*m.b119 + 51363*m.b116*m.b143 - 36171*m.b117*m.b120 + 51363*m.b117*m.b144 - 
                       80014*m.b118*m.b121 + 272797*m.b118*m.b145 - 80014*m.b119*m.b122 + 272797*m.b119*m.b146 - 80014*
                       m.b120*m.b123 + 272797*m.b120*m.b147 + 121144*m.b121*m.b124 - 183096*m.b121*m.b148 + 121144*
                       m.b122*m.b125 - 183096*m.b122*m.b149 + 121144*m.b123*m.b126 - 183096*m.b123*m.b150 - 117673*
                       m.b124*m.b127 + 70156*m.b124*m.b151 - 117673*m.b125*m.b128 + 70156*m.b125*m.b152 - 117673*m.b126*
                       m.b129 + 70156*m.b126*m.b153 + 56696*m.b127*m.b130 - 151153*m.b127*m.b154 + 56696*m.b128*m.b131
                        - 151153*m.b128*m.b155 + 56696*m.b129*m.b132 - 151153*m.b129*m.b156 + 24312*m.b130*m.b133 - 
                       22362*m.b130*m.b157 + 24312*m.b131*m.b134 - 22362*m.b131*m.b158 + 24312*m.b132*m.b135 - 22362*
                       m.b132*m.b159 + 42805*m.b133*m.b160 + 42805*m.b134*m.b161 + 42805*m.b135*m.b162 + 13835*m.b136*
                       m.b139 + 175755*m.b136*m.b160 - 87081*m.b136*m.b163 + 13835*m.b137*m.b140 + 175755*m.b137*m.b161
                        - 87081*m.b137*m.b164 + 13835*m.b138*m.b141 + 175755*m.b138*m.b162 - 87081*m.b138*m.b165 - 17215
                       *m.b139*m.b142 + 61204*m.b139*m.b166 - 17215*m.b140*m.b143 + 61204*m.b140*m.b167 - 17215*m.b141*
                       m.b144 + 61204*m.b141*m.b168 + 29411*m.b142*m.b145 - 40374*m.b142*m.b169 + 29411*m.b143*m.b146 - 
                       40374*m.b143*m.b170 + 29411*m.b144*m.b147 - 40374*m.b144*m.b171 - 68599*m.b145*m.b148 - 19496*
                       m.b145*m.b172 - 68599*m.b146*m.b149 - 19496*m.b146*m.b173 - 68599*m.b147*m.b150 - 19496*m.b147*
                       m.b174 - 25570*m.b148*m.b151 + 127270*m.b148*m.b175 - 25570*m.b149*m.b152 + 127270*m.b149*m.b176
                        - 25570*m.b150*m.b153 + 127270*m.b150*m.b177 - 128950*m.b151*m.b154 - 126258*m.b151*m.b178 - 
                       128950*m.b152*m.b155 - 126258*m.b152*m.b179 - 128950*m.b153*m.b156 - 126258*m.b153*m.b180 + 78155
                       *m.b154*m.b157 - 119772*m.b154*m.b181 + 78155*m.b155*m.b158 - 119772*m.b155*m.b182 + 78155*m.b156
                       *m.b159 - 119772*m.b156*m.b183 - 11106*m.b157*m.b160 + 70126*m.b157*m.b184 - 11106*m.b158*m.b161
                        + 70126*m.b158*m.b185 - 11106*m.b159*m.b162 + 70126*m.b159*m.b186 + 63368*m.b160*m.b187 + 63368*
                       m.b161*m.b188 + 63368*m.b162*m.b189 + 53151*m.b163*m.b166 + 44231*m.b163*m.b187 - 34407*m.b163*
                       m.b190 + 53151*m.b164*m.b167 + 44231*m.b164*m.b188 - 34407*m.b164*m.b191 + 53151*m.b165*m.b168 + 
                       44231*m.b165*m.b189 - 34407*m.b165*m.b192 + 84442*m.b166*m.b169 - 139953*m.b166*m.b193 + 84442*
                       m.b167*m.b170 - 139953*m.b167*m.b194 + 84442*m.b168*m.b171 - 139953*m.b168*m.b195 - 73503*m.b169*
                       m.b172 - 27195*m.b169*m.b196 - 73503*m.b170*m.b173 - 27195*m.b170*m.b197 - 73503*m.b171*m.b174 - 
                       27195*m.b171*m.b198 - 75786*m.b172*m.b175 - 74004*m.b172*m.b199 - 75786*m.b173*m.b176 - 74004*
                       m.b173*m.b200 - 75786*m.b174*m.b177 - 74004*m.b174*m.b201 + 68383*m.b175*m.b178 - 83289*m.b175*
                       m.b202 + 68383*m.b176*m.b179 - 83289*m.b176*m.b203 + 68383*m.b177*m.b180 - 83289*m.b177*m.b204 + 
                       68587*m.b178*m.b181 - 68077*m.b178*m.b205 + 68587*m.b179*m.b182 - 68077*m.b179*m.b206 + 68587*
                       m.b180*m.b183 - 68077*m.b180*m.b207 + 37991*m.b181*m.b184 - 40892*m.b181*m.b208 + 37991*m.b182*
                       m.b185 - 40892*m.b182*m.b209 + 37991*m.b183*m.b186 - 40892*m.b183*m.b210 - 57619*m.b184*m.b187 - 
                       56916*m.b184*m.b211 - 57619*m.b185*m.b188 - 56916*m.b185*m.b212 - 57619*m.b186*m.b189 - 56916*
                       m.b186*m.b213 - 39383*m.b187*m.b214 - 39383*m.b188*m.b215 - 39383*m.b189*m.b216 - 32370*m.b190*
                       m.b193 + 66379*m.b190*m.b214 + 70753*m.b190*m.b217 - 32370*m.b191*m.b194 + 66379*m.b191*m.b215 + 
                       70753*m.b191*m.b218 - 32370*m.b192*m.b195 + 66379*m.b192*m.b216 + 70753*m.b192*m.b219 + 158042*
                       m.b193*m.b196 - 12977*m.b193*m.b220 + 158042*m.b194*m.b197 - 12977*m.b194*m.b221 + 158042*m.b195*
                       m.b198 - 12977*m.b195*m.b222 - 79140*m.b196*m.b199 + 449*m.b196*m.b223 - 79140*m.b197*m.b200 + 
                       449*m.b197*m.b224 - 79140*m.b198*m.b201 + 449*m.b198*m.b225 - 33542*m.b199*m.b202 - 97950*m.b199*
                       m.b226 - 33542*m.b200*m.b203 - 97950*m.b200*m.b227 - 33542*m.b201*m.b204 - 97950*m.b201*m.b228 + 
                       3867*m.b202*m.b205 - 142006*m.b202*m.b229 + 3867*m.b203*m.b206 - 142006*m.b203*m.b230 + 3867*
                       m.b204*m.b207 - 142006*m.b204*m.b231 - 43546*m.b205*m.b208 - 28496*m.b205*m.b232 - 43546*m.b206*
                       m.b209 - 28496*m.b206*m.b233 - 43546*m.b207*m.b210 - 28496*m.b207*m.b234 - 75840*m.b208*m.b211 + 
                       194773*m.b208*m.b235 - 75840*m.b209*m.b212 + 194773*m.b209*m.b236 - 75840*m.b210*m.b213 + 194773*
                       m.b210*m.b237 + 36249*m.b211*m.b214 + 64846*m.b211*m.b238 + 36249*m.b212*m.b215 + 64846*m.b212*
                       m.b239 + 36249*m.b213*m.b216 + 64846*m.b213*m.b240 + 45762*m.b214*m.b241 + 45762*m.b215*m.b242 + 
                       45762*m.b216*m.b243 - 5829*m.b217*m.b220 - 90980*m.b217*m.b241 - 5829*m.b218*m.b221 - 90980*
                       m.b218*m.b242 - 5829*m.b219*m.b222 - 90980*m.b219*m.b243 - 151277*m.b220*m.b223 - 151277*m.b221*
                       m.b224 - 151277*m.b222*m.b225 - 104815*m.b223*m.b226 - 104815*m.b224*m.b227 - 104815*m.b225*
                       m.b228 + 4707*m.b226*m.b229 + 4707*m.b227*m.b230 + 4707*m.b228*m.b231 + 60681*m.b229*m.b232 + 
                       60681*m.b230*m.b233 + 60681*m.b231*m.b234 - 64166*m.b232*m.b235 - 64166*m.b233*m.b236 - 64166*
                       m.b234*m.b237 + 7619*m.b235*m.b238 + 7619*m.b236*m.b239 + 7619*m.b237*m.b240 - 215647*m.b238*
                       m.b241 - 215647*m.b239*m.b242 - 215647*m.b240*m.b243, sense=minimize)

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
