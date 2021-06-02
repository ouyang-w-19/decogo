#  MINLP written by GAMS Convert at 04/21/18 13:54:17
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          1        0        0        1        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        232        1      231        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        232        1      231        0


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
m.x232 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=m.x232, sense=maximize)

m.c1 = Constraint(expr=2*m.b1*m.b2 - 2*m.b1 - 2*m.b2 + 2*m.b1*m.b85 - 2*m.b85 + 2*m.b1*m.b166 - 2*m.b1*m.b170 + 2*m.b2*
                       m.b62 - 4*m.b62 - 2*m.b2*m.b125 + 2*m.b125 + 2*m.b2*m.b167 - 2*m.b3*m.b89 - 2*m.b3 + 2*m.b89 + 2*
                       m.b3*m.b172 + 2*m.b3*m.b180 + 2*m.b3*m.b181 - 2*m.b4*m.b110 - 2*m.b4 + 2*m.b110 + 2*m.b4*m.b169
                        + 2*m.b4*m.b172 + 2*m.b4*m.b186 + 2*m.b5*m.b8 - 2*m.b5 - 4*m.b8 + 2*m.b5*m.b176 + 2*m.b6*m.b36
                        - 2*m.b6 - 2*m.b36 + 2*m.b6*m.b50 - 2*m.b50 - 2*m.b6*m.b135 + 2*m.b135 + 2*m.b6*m.b169 + 2*m.b7*
                       m.b20 - 2*m.b7 - 2*m.b20 - 2*m.b7*m.b118 + 2*m.b118 + 2*m.b7*m.b194 + 2*m.b7*m.b195 + 2*m.b8*
                       m.b48 - 2*m.b48 + 2*m.b8*m.b50 + 2*m.b8*m.b173 + 2*m.b9*m.b20 - 2*m.b9 + 2*m.b9*m.b29 - 4*m.b29
                        + 2*m.b9*m.b76 - 2*m.b76 - 2*m.b9*m.b146 + 2*m.b146 + 2*m.b10*m.b29 - 2*m.b10 + 2*m.b10*m.b40 - 
                       4*m.b40 + 2*m.b10*m.b99 - 4*m.b99 - 2*m.b10*m.b203 + 2*m.b11*m.b23 - 2*m.b11 - 2*m.b23 + 2*m.b11*
                       m.b133 - 4*m.b133 + 2*m.b12*m.b40 - 2*m.b12 + 2*m.b12*m.b56 - 4*m.b56 + 2*m.b12*m.b119 - 4*m.b119
                        - 2*m.b12*m.b207 - 2*m.b13*m.b20 - 2*m.b13 + 2*m.b13*m.b31 - 4*m.b31 + 2*m.b13*m.b40 + 2*m.b13*
                       m.b208 + 2*m.b14*m.b56 - 4*m.b14 + 2*m.b14*m.b77 - 4*m.b77 + 2*m.b14*m.b147 - 4*m.b147 + 2*m.b14*
                       m.b207 + 2*m.b15*m.b31 - 2*m.b15 + 2*m.b15*m.b42 - 4*m.b42 + 2*m.b15*m.b56 - 2*m.b15*m.b195 + 2*
                       m.b16*m.b46 - 2*m.b16 - 4*m.b46 + 2*m.b16*m.b205 + 2*m.b17*m.b18 - 2*m.b17 - 2*m.b18 + 2*m.b17*
                       m.b25 - 2*m.b25 + 2*m.b17*m.b93 - 4*m.b93 - 2*m.b17*m.b182 + 2*m.b18*m.b26 - 2*m.b26 + 2*m.b18*
                       m.b38 - 2*m.b38 - 2*m.b18*m.b214 + 2*m.b19*m.b77 - 2*m.b19 + 2*m.b19*m.b101 - 2*m.b101 - 2*m.b19*
                       m.b163 + 2*m.b19*m.b203 + 2*m.b20*m.b30 - 4*m.b30 + 2*m.b21*m.b42 - 4*m.b21 + 2*m.b21*m.b58 - 4*
                       m.b58 + 2*m.b21*m.b77 + 2*m.b21*m.b195 - 2*m.b22*m.b23 - 2*m.b22 + 2*m.b22*m.b44 - 4*m.b44 + 2*
                       m.b22*m.b66 - 4*m.b66 + 2*m.b22*m.b213 + 2*m.b23*m.b24 - 2*m.b24 + 2*m.b23*m.b65 - 4*m.b65 + 2*
                       m.b24*m.b66 + 2*m.b25*m.b27 - 4*m.b27 + 2*m.b25*m.b53 - 2*m.b53 - 2*m.b25*m.b116 + 4*m.b116 + 2*
                       m.b26*m.b28 - 4*m.b28 + 2*m.b26*m.b164 - 2*m.b26*m.b193 + 2*m.b27*m.b28 + 2*m.b27*m.b164 + 2*
                       m.b27*m.b212 + 2*m.b28*m.b118 + 2*m.b28*m.b163 + 2*m.b29*m.b41 - 2*m.b41 + 2*m.b29*m.b150 - 2*
                       m.b150 + 2*m.b30*m.b58 + 2*m.b30*m.b80 - 4*m.b80 + 2*m.b30*m.b101 + 2*m.b31*m.b59 - 4*m.b59 + 2*
                       m.b31*m.b200 + 2*m.b32*m.b33 - 4*m.b32 - 2*m.b33 + 2*m.b32*m.b63 - 2*m.b63 + 2*m.b32*m.b210 + 2*
                       m.b32*m.b216 + 2*m.b33*m.b64 - 4*m.b64 + 2*m.b33*m.b87 - 4*m.b87 - 2*m.b33*m.b205 + 2*m.b34*m.b35
                        - 2*m.b34 - 2*m.b35 + 2*m.b34*m.b86 - 4*m.b86 - 2*m.b34*m.b210 + 2*m.b34*m.b211 + 2*m.b35*m.b87
                        + 2*m.b36*m.b49 - 2*m.b49 + 2*m.b37*m.b49 - 4*m.b37 + 2*m.b37*m.b91 - 2*m.b91 + 2*m.b37*m.b176
                        + 2*m.b37*m.b202 - 2*m.b38*m.b39 + 2*m.b39 + 2*m.b38*m.b177 + 2*m.b38*m.b189 + 2*m.b39*m.b98 + 2
                       *m.b98 - 2*m.b39*m.b146 - 2*m.b39*m.b218 + 2*m.b40*m.b57 - 2*m.b57 + 2*m.b41*m.b80 + 2*m.b41*
                       m.b104 - 4*m.b104 - 2*m.b41*m.b149 - 2*m.b149 + 2*m.b42*m.b153 + 2*m.b153 + 2*m.b42*m.b196 + 2*
                       m.b43*m.b44 - 2*m.b43 + 2*m.b43*m.b156 - 2*m.b156 + 2*m.b43*m.b213 - 2*m.b43*m.b220 + 2*m.b44*
                       m.b45 - 4*m.b45 + 2*m.b44*m.b83 - 2*m.b83 + 2*m.b45*m.b84 - 4*m.b84 + 2*m.b45*m.b109 - 2*m.b109
                        + 2*m.b45*m.b205 + 2*m.b46*m.b47 - 2*m.b47 + 2*m.b46*m.b159 - 2*m.b159 + 2*m.b46*m.b210 + 2*
                       m.b47*m.b109 + 2*m.b48*m.b69 - 2*m.b69 + 2*m.b49*m.b51 - 2*m.b51 - 2*m.b49*m.b186 - 2*m.b50*
                       m.b138 + 2*m.b138 + 2*m.b50*m.b168 + 2*m.b51*m.b69 + 2*m.b51*m.b138 - 2*m.b51*m.b206 + 2*m.b52*
                       m.b53 - 2*m.b52 - 2*m.b52*m.b54 + 2*m.b54 + 2*m.b52*m.b171 + 2*m.b52*m.b202 - 2*m.b53*m.b115 + 2*
                       m.b115 + 2*m.b53*m.b182 + 2*m.b54*m.b115 - 2*m.b54*m.b142 + 2*m.b142 - 2*m.b54*m.b221 - 2*m.b55*
                       m.b184 + 2*m.b55 + 2*m.b55*m.b194 - 2*m.b55*m.b203 - 2*m.b55*m.b222 + 2*m.b56*m.b79 - 2*m.b79 + 2
                       *m.b57*m.b104 + 2*m.b57*m.b122 - 4*m.b122 - 2*m.b57*m.b219 + 2*m.b58*m.b60 - 2*m.b60 + 2*m.b58*
                       m.b204 + 2*m.b59*m.b61 - 2*m.b61 + 2*m.b59*m.b62 + 2*m.b59*m.b152 - 4*m.b152 + 2*m.b60*m.b62 + 2*
                       m.b60*m.b122 - 2*m.b60*m.b185 - 2*m.b61*m.b63 + 2*m.b61*m.b127 - 2*m.b127 + 2*m.b61*m.b165 + 2*
                       m.b62*m.b63 + 2*m.b63*m.b64 + 2*m.b64*m.b65 + 2*m.b64*m.b107 - 2*m.b107 + 2*m.b65*m.b108 - 4*
                       m.b108 + 2*m.b65*m.b132 - 2*m.b132 + 2*m.b66*m.b67 - 2*m.b67 + 2*m.b66*m.b131 - 2*m.b131 + 2*
                       m.b67*m.b132 - 2*m.b68*m.b176 + 2*m.b68 - 2*m.b68*m.b223 + 2*m.b69*m.b70 - 2*m.b70 - 2*m.b69*
                       m.b180 + 2*m.b70*m.b197 - 2*m.b70*m.b209 + 2*m.b70*m.b223 + 2*m.b71*m.b72 - 2*m.b71 - 2*m.b72 - 2
                       *m.b71*m.b73 + 2*m.b73 + 2*m.b71*m.b168 + 2*m.b71*m.b206 - 2*m.b72*m.b95 + 2*m.b95 + 2*m.b72*
                       m.b177 + 2*m.b72*m.b187 + 2*m.b73*m.b95 - 2*m.b73*m.b212 - 2*m.b73*m.b225 - 2*m.b74*m.b75 + 2*
                       m.b74 + 2*m.b75 - 2*m.b74*m.b142 - 2*m.b74*m.b174 + 2*m.b74*m.b178 + 2*m.b75*m.b76 - 2*m.b75*
                       m.b207 - 2*m.b75*m.b226 + 2*m.b76*m.b100 - 2*m.b100 - 2*m.b76*m.b178 + 2*m.b77*m.b103 - 4*m.b103
                        + 2*m.b78*m.b100 - 4*m.b78 + 2*m.b78*m.b103 + 2*m.b78*m.b150 + 2*m.b78*m.b190 - 2*m.b79*m.b102
                        - 2*m.b102 + 2*m.b79*m.b122 + 2*m.b79*m.b151 - 4*m.b151 + 2*m.b80*m.b81 - 4*m.b81 + 2*m.b80*
                       m.b200 + 2*m.b81*m.b151 + 2*m.b81*m.b185 + 2*m.b81*m.b220 - 2*m.b82*m.b83 + 2*m.b82 - 2*m.b82*
                       m.b153 - 2*m.b82*m.b165 + 2*m.b82*m.b175 + 2*m.b83*m.b84 + 2*m.b83*m.b220 + 2*m.b84*m.b86 + 2*
                       m.b84*m.b128 - 2*m.b128 - 2*m.b85*m.b109 + 2*m.b85*m.b129 - 2*m.b129 + 2*m.b85*m.b161 - 4*m.b161
                        + 2*m.b86*m.b130 - 2*m.b130 + 2*m.b86*m.b161 + 2*m.b87*m.b88 - 2*m.b88 + 2*m.b87*m.b160 - 2*
                       m.b160 + 2*m.b88*m.b161 - 2*m.b89*m.b227 - 2*m.b90*m.b91 - 2*m.b90 + 2*m.b90*m.b92 - 2*m.b92 + 2*
                       m.b90*m.b223 + 2*m.b90*m.b227 + 2*m.b91*m.b93 + 2*m.b91*m.b192 + 2*m.b92*m.b93 - 2*m.b92*m.b172
                        + 2*m.b92*m.b187 + 2*m.b93*m.b214 + 2*m.b94*m.b174 - 2*m.b94 + 2*m.b94*m.b191 + 2*m.b94*m.b198
                        - 2*m.b94*m.b199 - 2*m.b95*m.b116 - 2*m.b95*m.b226 - 2*m.b96*m.b97 + 4*m.b96 - 2*m.b97 - 2*m.b96
                       *m.b115 - 2*m.b96*m.b177 - 2*m.b96*m.b178 + 2*m.b97*m.b99 + 2*m.b97*m.b207 + 2*m.b97*m.b226 - 2*
                       m.b98*m.b120 - 2*m.b120 - 2*m.b98*m.b189 - 2*m.b98*m.b190 + 2*m.b99*m.b120 + 2*m.b99*m.b178 + 2*
                       m.b100*m.b102 - 2*m.b100*m.b194 + 2*m.b101*m.b121 - 4*m.b121 - 2*m.b101*m.b215 + 2*m.b102*m.b120
                        + 2*m.b102*m.b121 + 2*m.b103*m.b105 - 2*m.b105 + 2*m.b103*m.b151 + 2*m.b104*m.b106 - 4*m.b106 + 
                       2*m.b104*m.b196 + 2*m.b105*m.b106 + 2*m.b105*m.b121 - 2*m.b105*m.b165 + 2*m.b106*m.b155 + 2*
                       m.b155 + 2*m.b106*m.b217 + 2*m.b107*m.b108 - 2*m.b107*m.b179 + 2*m.b107*m.b217 + 2*m.b108*m.b157
                        - 2*m.b157 + 2*m.b108*m.b159 + 2*m.b109*m.b229 - 2*m.b110*m.b136 - 2*m.b136 + 2*m.b111*m.b112 - 
                       4*m.b111 - 2*m.b112 + 2*m.b111*m.b136 + 2*m.b111*m.b209 + 2*m.b111*m.b227 - 2*m.b112*m.b181 + 2*
                       m.b112*m.b182 + 2*m.b112*m.b225 - 2*m.b113*m.b174 + 2*m.b113 - 2*m.b113*m.b191 + 2*m.b113*m.b192
                        - 2*m.b113*m.b193 - 2*m.b114*m.b192 - 2*m.b114 + 2*m.b114*m.b193 + 2*m.b114*m.b212 + 2*m.b114*
                       m.b225 - 2*m.b115*m.b222 - 2*m.b116*m.b117 - 2*m.b117 - 2*m.b116*m.b183 + 2*m.b117*m.b119 + 2*
                       m.b117*m.b203 + 2*m.b117*m.b222 - 2*m.b118*m.b148 - 2*m.b148 - 2*m.b118*m.b164 + 2*m.b119*m.b148
                        + 2*m.b119*m.b183 + 2*m.b120*m.b219 + 2*m.b121*m.b123 - 2*m.b123 + 2*m.b122*m.b124 - 4*m.b124 + 
                       2*m.b123*m.b124 + 2*m.b123*m.b165 - 2*m.b123*m.b231 + 2*m.b124*m.b125 + 2*m.b124*m.b126 - 2*
                       m.b126 - 2*m.b125*m.b128 - 2*m.b125*m.b200 + 2*m.b126*m.b128 - 2*m.b126*m.b204 + 2*m.b126*m.b216
                        + 2*m.b127*m.b129 - 2*m.b127*m.b130 + 2*m.b127*m.b185 + 2*m.b128*m.b130 - 2*m.b129*m.b131 + 2*
                       m.b129*m.b170 + 2*m.b130*m.b131 + 2*m.b131*m.b133 + 2*m.b132*m.b134 - 2*m.b134 - 2*m.b132*m.b166
                        + 2*m.b133*m.b134 + 2*m.b133*m.b166 - 2*m.b135*m.b201 + 2*m.b136*m.b137 - 4*m.b137 + 2*m.b136*
                       m.b228 + 2*m.b137*m.b139 - 4*m.b139 + 2*m.b137*m.b201 + 2*m.b137*m.b206 - 2*m.b138*m.b191 - 2*
                       m.b138*m.b221 + 2*m.b139*m.b181 + 2*m.b139*m.b188 + 2*m.b139*m.b221 - 2*m.b140*m.b143 + 2*m.b140
                        - 2*m.b143 - 2*m.b140*m.b177 - 2*m.b140*m.b187 + 2*m.b140*m.b188 + 2*m.b141*m.b142 - 2*m.b141 + 
                       2*m.b141*m.b143 - 2*m.b141*m.b188 + 2*m.b141*m.b221 - 2*m.b142*m.b218 + 2*m.b143*m.b144 + 2*
                       m.b144 + 2*m.b143*m.b218 - 2*m.b144*m.b145 - 2*m.b145 - 2*m.b144*m.b189 - 2*m.b144*m.b199 + 2*
                       m.b145*m.b146 + 2*m.b145*m.b147 + 2*m.b145*m.b218 - 2*m.b146*m.b215 + 2*m.b147*m.b189 + 2*m.b147*
                       m.b215 + 2*m.b148*m.b149 + 2*m.b148*m.b219 + 2*m.b149*m.b215 + 2*m.b149*m.b231 + 2*m.b150*m.b152
                        - 2*m.b150*m.b208 + 2*m.b151*m.b154 - 4*m.b154 + 2*m.b152*m.b154 + 2*m.b152*m.b231 - 2*m.b153*
                       m.b156 - 2*m.b153*m.b208 + 2*m.b154*m.b156 + 2*m.b154*m.b179 - 2*m.b155*m.b157 - 2*m.b155*m.b170
                        - 2*m.b155*m.b196 + 2*m.b156*m.b157 + 2*m.b157*m.b158 - 2*m.b158 + 2*m.b158*m.b159 + 2*m.b158*
                       m.b160 - 2*m.b158*m.b175 - 2*m.b159*m.b230 - 2*m.b160*m.b167 + 2*m.b160*m.b230 + 2*m.b161*m.b162
                        - 2*m.b162 + 2*m.b162*m.b230 - 2*m.b163*m.b164 + 2*m.b163*m.b190 - 2*m.b166*m.b167 + 2*m.b167*
                       m.b175 - 2*m.b168*m.b169 - 2*m.b168*m.b198 - 2*m.b169*m.b197 + 2*m.b170*m.b179 - 2*m.b171*m.b172
                        + 2*m.b171*m.b173 - 2*m.b171*m.b192 - 2*m.b173*m.b201 - 2*m.b173*m.b202 + 2*m.b174*m.b184 - 2*
                       m.b175*m.b185 - 2*m.b176*m.b181 - 2*m.b179*m.b204 - 2*m.b182*m.b206 + 2*m.b183*m.b184 - 2*m.b183*
                       m.b194 - 2*m.b184*m.b212 - 2*m.b187*m.b202 - 2*m.b188*m.b209 - 2*m.b190*m.b195 + 2*m.b191*m.b197
                        + 2*m.b193*m.b222 - 2*m.b196*m.b220 - 2*m.b197*m.b225 + 2*m.b198*m.b209 - 2*m.b198*m.b214 + 2*
                       m.b199*m.b214 + 2*m.b199*m.b226 - 2*m.b200*m.b217 + 2*m.b201*m.b224 + 2*m.b204*m.b208 - 2*m.b205*
                       m.b211 - 2*m.b210*m.b213 - 2*m.b213*m.b216 - 2*m.b216*m.b217 - 2*m.b219*m.b231 - 2*m.b223*m.b224
                        - 2*m.b227*m.b228 - 2*m.b229*m.b230 + m.x232 <= 0)
