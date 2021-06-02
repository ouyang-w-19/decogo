#  MINLP written by GAMS Convert at 04/21/18 13:54:02
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#       3229        1     2902      326        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        254       41      213        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#      19216     6996    12220        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


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
m.x215 = Var(within=Reals,bounds=(0.599362,9.400638),initialize=0.599362)
m.x216 = Var(within=Reals,bounds=(0.599362,9.400638),initialize=0.599362)
m.x217 = Var(within=Reals,bounds=(0.599362,9.400638),initialize=0.599362)
m.x218 = Var(within=Reals,bounds=(0.599362,9.400638),initialize=0.599362)
m.x219 = Var(within=Reals,bounds=(0.599362,9.400638),initialize=0.599362)
m.x220 = Var(within=Reals,bounds=(0.599362,9.400638),initialize=0.599362)
m.x221 = Var(within=Reals,bounds=(0.599362,9.400638),initialize=0.599362)
m.x222 = Var(within=Reals,bounds=(0.599362,9.400638),initialize=0.599362)
m.x223 = Var(within=Reals,bounds=(0.599362,9.400638),initialize=0.599362)
m.x224 = Var(within=Reals,bounds=(0.599362,9.400638),initialize=0.599362)
m.x225 = Var(within=Reals,bounds=(0.599362,9.400638),initialize=0.599362)
m.x226 = Var(within=Reals,bounds=(0.599362,9.400638),initialize=0.599362)
m.x227 = Var(within=Reals,bounds=(0.342553,9.657447),initialize=0.342553)
m.x228 = Var(within=Reals,bounds=(0.342553,9.657447),initialize=0.342553)
m.x229 = Var(within=Reals,bounds=(0.342553,9.657447),initialize=0.342553)
m.x230 = Var(within=Reals,bounds=(0.342553,9.657447),initialize=0.342553)
m.x231 = Var(within=Reals,bounds=(0.342553,9.657447),initialize=0.342553)
m.x232 = Var(within=Reals,bounds=(0.342553,9.657447),initialize=0.342553)
m.x233 = Var(within=Reals,bounds=(0.342553,9.657447),initialize=0.342553)
m.x234 = Var(within=Reals,bounds=(0.342553,9.657447),initialize=0.342553)
m.x235 = Var(within=Reals,bounds=(0.342553,9.657447),initialize=0.342553)
m.x236 = Var(within=Reals,bounds=(0.342553,9.657447),initialize=0.342553)
m.x237 = Var(within=Reals,bounds=(0.85617,9.14383),initialize=0.85617)
m.x238 = Var(within=Reals,bounds=(0.85617,9.14383),initialize=0.85617)
m.x239 = Var(within=Reals,bounds=(0.85617,9.14383),initialize=0.85617)
m.x240 = Var(within=Reals,bounds=(0.85617,9.14383),initialize=0.85617)
m.x241 = Var(within=Reals,bounds=(0.85617,9.14383),initialize=0.85617)
m.x242 = Var(within=Reals,bounds=(0.85617,9.14383),initialize=0.85617)
m.x243 = Var(within=Reals,bounds=(0.85617,9.14383),initialize=0.85617)
m.x244 = Var(within=Reals,bounds=(0.85617,9.14383),initialize=0.85617)
m.x245 = Var(within=Reals,bounds=(0.85617,9.14383),initialize=0.85617)
m.x246 = Var(within=Reals,bounds=(0.85617,9.14383),initialize=0.85617)
m.x247 = Var(within=Reals,bounds=(1.52426,8.47574),initialize=1.52426)
m.x248 = Var(within=Reals,bounds=(1.52426,8.47574),initialize=1.52426)
m.x249 = Var(within=Reals,bounds=(1.52426,8.47574),initialize=1.52426)
m.x250 = Var(within=Reals,bounds=(1.52426,8.47574),initialize=1.52426)
m.x251 = Var(within=Reals,bounds=(1.93213,8.06787),initialize=1.93213)
m.x252 = Var(within=Reals,bounds=(1.93213,8.06787),initialize=1.93213)
m.x253 = Var(within=Reals,bounds=(1.93213,8.06787),initialize=1.93213)
m.x254 = Var(within=Reals,bounds=(1.93213,8.06787),initialize=1.93213)

m.obj = Objective(expr= - 0.287403606378025*m.b2 - 0.287403606378025*m.b3 - 0.287403606378025*m.b4
                        - 0.287403606378025*m.b5 - 0.287403606378025*m.b6 - 0.287403606378025*m.b7
                        - 0.287403606378025*m.b8 - 0.287403606378025*m.b9 - 0.287403606378025*m.b10
                        - 0.287403606378025*m.b11 - 0.287403606378025*m.b12 - 0.287403606378025*m.b13
                        - 0.287403606378025*m.b14 - 0.287403606378025*m.b15 - 0.287403606378025*m.b16
                        - 0.287403606378025*m.b17 - 0.287403606378025*m.b18 - 0.287403606378025*m.b19
                        - 0.0946538180425961*m.b20 - 0.0946538180425961*m.b21 - 0.0946538180425961*m.b22
                        - 0.0946538180425961*m.b23 - 0.0946538180425961*m.b24 - 0.0946538180425961*m.b25
                        - 0.0946538180425961*m.b26 - 0.0946538180425961*m.b27 - 0.0946538180425961*m.b28
                        - 0.0946538180425961*m.b29 - 0.0946538180425961*m.b30 - 0.0946538180425961*m.b31
                        - 0.0946538180425961*m.b32 - 0.0946538180425961*m.b33 - 0.0946538180425961*m.b34
                        - 0.584516458645496*m.b35 - 0.584516458645496*m.b36 - 0.584516458645496*m.b37
                        - 0.584516458645496*m.b38 - 0.584516458645496*m.b39 - 0.584516458645496*m.b40
                        - 0.584516458645496*m.b41 - 0.584516458645496*m.b42 - 0.584516458645496*m.b43
                        - 0.584516458645496*m.b44 - 0.584516458645496*m.b45 - 0.584516458645496*m.b46
                        - 0.584516458645496*m.b47 - 0.584516458645496*m.b48 - 0.584516458645496*m.b49
                        - 1.29409755392315*m.b50 - 1.29409755392315*m.b51 - 1.29409755392315*m.b52
                        - 1.29409755392315*m.b53 - 1.29409755392315*m.b54 - 1.29409755392315*m.b55
                        - 2.08582176557546*m.b56 - 2.08582176557546*m.b57 - 2.08582176557546*m.b58
                        - 2.08582176557546*m.b59 - 2.08582176557546*m.b60 - 2.08582176557546*m.b61
                        - 2.08582176557546*m.b62 - 2.08582176557546*m.b63 - 2.08582176557546*m.b64
                        - 2.08582176557546*m.b65 - 2.08582176557546*m.b66 - 2.08582176557546*m.b67
                        - 2.08582176557546*m.b68 - 2.08582176557546*m.b69 - 2.08582176557546*m.b70
                        - 2.08582176557546*m.b71 - 2.08582176557546*m.b72 - 2.08582176557546*m.b73
                        - 2.08582176557546*m.b74 - 2.08582176557546*m.b75 - 2.08582176557546*m.b76
                        - 2.08582176557546*m.b77 - 2.08582176557546*m.b78 - 2.08582176557546*m.b79
                        - 2.08582176557546*m.b80 - 2.08582176557546*m.b81 - 2.08582176557546*m.b82
                        - 2.08582176557546*m.b83 - 2.08582176557546*m.b84 - 2.08582176557546*m.b85
                        - 2.08582176557546*m.b86 - 2.08582176557546*m.b87 - 2.08582176557546*m.b88
                        - 2.08582176557546*m.b89 - 2.08582176557546*m.b90 - 2.08582176557546*m.b91
                        - 2.08582176557546*m.b92 - 2.08582176557546*m.b93 - 2.08582176557546*m.b94
                        - 2.08582176557546*m.b95 - 2.08582176557546*m.b96 - 2.08582176557546*m.b97
                        - 2.08582176557546*m.b98 - 2.08582176557546*m.b99 - 2.08582176557546*m.b100
                        - 2.08582176557546*m.b101 - 2.08582176557546*m.b102 - 2.08582176557546*m.b103
                        - 2.08582176557546*m.b104 - 2.08582176557546*m.b105 - 2.08582176557546*m.b106
                        - 2.08582176557546*m.b107 - 2.08582176557546*m.b108 - 2.08582176557546*m.b109
                        - 2.08582176557546*m.b110 - 2.08582176557546*m.b111 - 2.08582176557546*m.b112
                        - 2.08582176557546*m.b113 - 2.08582176557546*m.b114 - 2.08582176557546*m.b115
                        - 2.08582176557546*m.b116 - 2.08582176557546*m.b117 - 2.08582176557546*m.b118
                        - 2.08582176557546*m.b119 - 2.08582176557546*m.b120 - 2.08582176557546*m.b121
                        - 2.08582176557546*m.b122 - 2.08582176557546*m.b123 - 2.08582176557546*m.b124
                        - 2.08582176557546*m.b125 - 2.08582176557546*m.b126 - 2.08582176557546*m.b127
                        - 2.08582176557546*m.b128 - 2.08582176557546*m.b129 - 2.08582176557546*m.b130
                        - 2.08582176557546*m.b131 - 2.08582176557546*m.b132 - 2.08582176557546*m.b133
                        - 2.08582176557546*m.b134 - 2.08582176557546*m.b135 - 2.08582176557546*m.b136
                        - 2.08582176557546*m.b137 - 2.08582176557546*m.b138 - 2.08582176557546*m.b139
                        - 2.08582176557546*m.b140 - 2.08582176557546*m.b141 - 2.08582176557546*m.b142
                        - 2.08582176557546*m.b143 - 2.08582176557546*m.b144 - 2.08582176557546*m.b145
                        - 2.08582176557546*m.b146 - 2.08582176557546*m.b147 - 2.08582176557546*m.b148
                        - 2.08582176557546*m.b149 - 2.08582176557546*m.b150 - 2.08582176557546*m.b151
                        - 2.08582176557546*m.b152 - 2.08582176557546*m.b153 - 2.08582176557546*m.b154
                        - 2.08582176557546*m.b155 - 2.08582176557546*m.b156 - 2.08582176557546*m.b157
                        - 2.08582176557546*m.b158 - 2.08582176557546*m.b159 - 2.08582176557546*m.b160
                        - 2.08582176557546*m.b161 - 2.08582176557546*m.b162 - 2.08582176557546*m.b163
                        - 2.08582176557546*m.b164 - 2.08582176557546*m.b165 - 2.08582176557546*m.b166
                        - 2.08582176557546*m.b167 - 2.08582176557546*m.b168 - 2.08582176557546*m.b169
                        - 2.08582176557546*m.b170 - 2.08582176557546*m.b171 - 2.08582176557546*m.b172
                        - 2.08582176557546*m.b173 - 2.08582176557546*m.b174 - 2.08582176557546*m.b175
                        - 2.08582176557546*m.b176 - 2.08582176557546*m.b177 - 2.08582176557546*m.b178
                        - 2.08582176557546*m.b179 - 2.08582176557546*m.b180 - 2.08582176557546*m.b181
                        - 2.08582176557546*m.b182 - 2.08582176557546*m.b183 - 2.08582176557546*m.b184
                        - 2.08582176557546*m.b185 - 2.08582176557546*m.b186 - 2.08582176557546*m.b187
                        - 2.08582176557546*m.b188 - 2.08582176557546*m.b189 - 2.08582176557546*m.b190
                        - 2.08582176557546*m.b191 - 2.08582176557546*m.b192 - 2.08582176557546*m.b193
                        - 2.08582176557546*m.b194 - 2.08582176557546*m.b195 - 2.08582176557546*m.b196
                        - 2.08582176557546*m.b197 - 2.08582176557546*m.b198 - 2.08582176557546*m.b199
                        - 2.08582176557546*m.b200 - 2.08582176557546*m.b201 - 2.08582176557546*m.b202
                        - 2.08582176557546*m.b203 - 2.08582176557546*m.b204 - 2.08582176557546*m.b205
                        - 2.08582176557546*m.b206 - 2.08582176557546*m.b207 - 2.08582176557546*m.b208
                        - 2.08582176557546*m.b209 - 2.08582176557546*m.b210 - 2.08582176557546*m.b211
                        - 2.08582176557546*m.b212 - 2.08582176557546*m.b213 - 2.08582176557546*m.b214, sense=minimize)

m.c2 = Constraint(expr=m.x215**2 + m.x216**2 + m.x217**2 + m.x218**2 - 2*m.x215*m.x217 - 2*m.x216*m.x218
                        - 1.436939228176*m.b2 - 1.436939228176*m.b5 >= -1.436939228176)

m.c3 = Constraint(expr=m.x215**2 + m.x216**2 + m.x217**2 + m.x218**2 - 2*m.x215*m.x217 - 2*m.x216*m.x218
                        - 1.436939228176*m.b3 - 1.436939228176*m.b6 >= -1.436939228176)

m.c4 = Constraint(expr=m.x215**2 + m.x216**2 + m.x217**2 + m.x218**2 - 2*m.x215*m.x217 - 2*m.x216*m.x218
                        - 1.436939228176*m.b4 - 1.436939228176*m.b7 >= -1.436939228176)

m.c5 = Constraint(expr=m.x215**2 + m.x216**2 + m.x219**2 + m.x220**2 - 2*m.x215*m.x219 - 2*m.x216*m.x220
                        - 1.436939228176*m.b2 - 1.436939228176*m.b8 >= -1.436939228176)

m.c6 = Constraint(expr=m.x215**2 + m.x216**2 + m.x219**2 + m.x220**2 - 2*m.x215*m.x219 - 2*m.x216*m.x220
                        - 1.436939228176*m.b3 - 1.436939228176*m.b9 >= -1.436939228176)

m.c7 = Constraint(expr=m.x215**2 + m.x216**2 + m.x219**2 + m.x220**2 - 2*m.x215*m.x219 - 2*m.x216*m.x220
                        - 1.436939228176*m.b4 - 1.436939228176*m.b10 >= -1.436939228176)

m.c8 = Constraint(expr=m.x215**2 + m.x216**2 + m.x221**2 + m.x222**2 - 2*m.x216*m.x222 - 2*m.x215*m.x221
                        - 1.436939228176*m.b2 - 1.436939228176*m.b11 >= -1.436939228176)

m.c9 = Constraint(expr=m.x215**2 + m.x216**2 + m.x221**2 + m.x222**2 - 2*m.x216*m.x222 - 2*m.x215*m.x221
                        - 1.436939228176*m.b3 - 1.436939228176*m.b12 >= -1.436939228176)

m.c10 = Constraint(expr=m.x215**2 + m.x216**2 + m.x221**2 + m.x222**2 - 2*m.x216*m.x222 - 2*m.x215*m.x221
                         - 1.436939228176*m.b4 - 1.436939228176*m.b13 >= -1.436939228176)

m.c11 = Constraint(expr=m.x215**2 + m.x216**2 + m.x223**2 + m.x224**2 - 2*m.x215*m.x223 - 2*m.x216*m.x224
                         - 1.436939228176*m.b2 - 1.436939228176*m.b14 >= -1.436939228176)

m.c12 = Constraint(expr=m.x215**2 + m.x216**2 + m.x223**2 + m.x224**2 - 2*m.x216*m.x224 - 2*m.x215*m.x223
                         - 1.436939228176*m.b3 - 1.436939228176*m.b15 >= -1.436939228176)

m.c13 = Constraint(expr=m.x215**2 + m.x216**2 + m.x223**2 + m.x224**2 - 2*m.x216*m.x224 - 2*m.x215*m.x223
                         - 1.436939228176*m.b4 - 1.436939228176*m.b16 >= -1.436939228176)

m.c14 = Constraint(expr=m.x215**2 + m.x216**2 + m.x225**2 + m.x226**2 - 2*m.x215*m.x225 - 2*m.x216*m.x226
                         - 1.436939228176*m.b2 - 1.436939228176*m.b17 >= -1.436939228176)

m.c15 = Constraint(expr=m.x215**2 + m.x216**2 + m.x225**2 + m.x226**2 - 2*m.x215*m.x225 - 2*m.x216*m.x226
                         - 1.436939228176*m.b3 - 1.436939228176*m.b18 >= -1.436939228176)

m.c16 = Constraint(expr=m.x215**2 + m.x216**2 + m.x225**2 + m.x226**2 - 2*m.x215*m.x225 - 2*m.x216*m.x226
                         - 1.436939228176*m.b4 - 1.436939228176*m.b19 >= -1.436939228176)

m.c17 = Constraint(expr=m.x215**2 + m.x216**2 + m.x227**2 + m.x228**2 - 2*m.x216*m.x228 - 2*m.x215*m.x227
                         - 0.887203867225*m.b2 - 0.887203867225*m.b20 >= -0.887203867225)

m.c18 = Constraint(expr=m.x215**2 + m.x216**2 + m.x227**2 + m.x228**2 - 2*m.x216*m.x228 - 2*m.x215*m.x227
                         - 0.887203867225*m.b3 - 0.887203867225*m.b21 >= -0.887203867225)

m.c19 = Constraint(expr=m.x215**2 + m.x216**2 + m.x227**2 + m.x228**2 - 2*m.x216*m.x228 - 2*m.x215*m.x227
                         - 0.887203867225*m.b4 - 0.887203867225*m.b22 >= -0.887203867225)

m.c20 = Constraint(expr=m.x215**2 + m.x216**2 + m.x229**2 + m.x230**2 - 2*m.x215*m.x229 - 2*m.x216*m.x230
                         - 0.887203867225*m.b2 - 0.887203867225*m.b23 >= -0.887203867225)

m.c21 = Constraint(expr=m.x215**2 + m.x216**2 + m.x229**2 + m.x230**2 - 2*m.x215*m.x229 - 2*m.x216*m.x230
                         - 0.887203867225*m.b3 - 0.887203867225*m.b24 >= -0.887203867225)

m.c22 = Constraint(expr=m.x215**2 + m.x216**2 + m.x229**2 + m.x230**2 - 2*m.x215*m.x229 - 2*m.x216*m.x230
                         - 0.887203867225*m.b4 - 0.887203867225*m.b25 >= -0.887203867225)

m.c23 = Constraint(expr=m.x215**2 + m.x216**2 + m.x231**2 + m.x232**2 - 2*m.x216*m.x232 - 2*m.x215*m.x231
                         - 0.887203867225*m.b2 - 0.887203867225*m.b26 >= -0.887203867225)

m.c24 = Constraint(expr=m.x215**2 + m.x216**2 + m.x231**2 + m.x232**2 - 2*m.x216*m.x232 - 2*m.x215*m.x231
                         - 0.887203867225*m.b3 - 0.887203867225*m.b27 >= -0.887203867225)

m.c25 = Constraint(expr=m.x215**2 + m.x216**2 + m.x231**2 + m.x232**2 - 2*m.x216*m.x232 - 2*m.x215*m.x231
                         - 0.887203867225*m.b4 - 0.887203867225*m.b28 >= -0.887203867225)

m.c26 = Constraint(expr=m.x215**2 + m.x216**2 + m.x233**2 + m.x234**2 - 2*m.x216*m.x234 - 2*m.x215*m.x233
                         - 0.887203867225*m.b2 - 0.887203867225*m.b29 >= -0.887203867225)

m.c27 = Constraint(expr=m.x215**2 + m.x216**2 + m.x233**2 + m.x234**2 - 2*m.x216*m.x234 - 2*m.x215*m.x233
                         - 0.887203867225*m.b3 - 0.887203867225*m.b30 >= -0.887203867225)

m.c28 = Constraint(expr=m.x215**2 + m.x216**2 + m.x233**2 + m.x234**2 - 2*m.x216*m.x234 - 2*m.x215*m.x233
                         - 0.887203867225*m.b4 - 0.887203867225*m.b31 >= -0.887203867225)

m.c29 = Constraint(expr=m.x215**2 + m.x216**2 + m.x235**2 + m.x236**2 - 2*m.x215*m.x235 - 2*m.x216*m.x236
                         - 0.887203867225*m.b2 - 0.887203867225*m.b32 >= -0.887203867225)

m.c30 = Constraint(expr=m.x215**2 + m.x216**2 + m.x235**2 + m.x236**2 - 2*m.x215*m.x235 - 2*m.x216*m.x236
                         - 0.887203867225*m.b3 - 0.887203867225*m.b33 >= -0.887203867225)

m.c31 = Constraint(expr=m.x215**2 + m.x216**2 + m.x235**2 + m.x236**2 - 2*m.x216*m.x236 - 2*m.x215*m.x235
                         - 0.887203867225*m.b4 - 0.887203867225*m.b34 >= -0.887203867225)

m.c32 = Constraint(expr=m.x215**2 + m.x216**2 + m.x237**2 + m.x238**2 - 2*m.x216*m.x238 - 2*m.x215*m.x237
                         - 2.118573403024*m.b2 - 2.118573403024*m.b35 >= -2.118573403024)

m.c33 = Constraint(expr=m.x215**2 + m.x216**2 + m.x237**2 + m.x238**2 - 2*m.x216*m.x238 - 2*m.x215*m.x237
                         - 2.118573403024*m.b3 - 2.118573403024*m.b36 >= -2.118573403024)

m.c34 = Constraint(expr=m.x215**2 + m.x216**2 + m.x237**2 + m.x238**2 - 2*m.x216*m.x238 - 2*m.x215*m.x237
                         - 2.118573403024*m.b4 - 2.118573403024*m.b37 >= -2.118573403024)

m.c35 = Constraint(expr=m.x215**2 + m.x216**2 + m.x239**2 + m.x240**2 - 2*m.x216*m.x240 - 2*m.x215*m.x239
                         - 2.118573403024*m.b2 - 2.118573403024*m.b38 >= -2.118573403024)

m.c36 = Constraint(expr=m.x215**2 + m.x216**2 + m.x239**2 + m.x240**2 - 2*m.x215*m.x239 - 2*m.x216*m.x240
                         - 2.118573403024*m.b3 - 2.118573403024*m.b39 >= -2.118573403024)

m.c37 = Constraint(expr=m.x215**2 + m.x216**2 + m.x239**2 + m.x240**2 - 2*m.x215*m.x239 - 2*m.x216*m.x240
                         - 2.118573403024*m.b4 - 2.118573403024*m.b40 >= -2.118573403024)

m.c38 = Constraint(expr=m.x215**2 + m.x216**2 + m.x241**2 + m.x242**2 - 2*m.x215*m.x241 - 2*m.x216*m.x242
                         - 2.118573403024*m.b2 - 2.118573403024*m.b41 >= -2.118573403024)

m.c39 = Constraint(expr=m.x215**2 + m.x216**2 + m.x241**2 + m.x242**2 - 2*m.x215*m.x241 - 2*m.x216*m.x242
                         - 2.118573403024*m.b3 - 2.118573403024*m.b42 >= -2.118573403024)

m.c40 = Constraint(expr=m.x215**2 + m.x216**2 + m.x241**2 + m.x242**2 - 2*m.x215*m.x241 - 2*m.x216*m.x242
                         - 2.118573403024*m.b4 - 2.118573403024*m.b43 >= -2.118573403024)

m.c41 = Constraint(expr=m.x215**2 + m.x216**2 + m.x243**2 + m.x244**2 - 2*m.x215*m.x243 - 2*m.x216*m.x244
                         - 2.118573403024*m.b2 - 2.118573403024*m.b44 >= -2.118573403024)

m.c42 = Constraint(expr=m.x215**2 + m.x216**2 + m.x243**2 + m.x244**2 - 2*m.x215*m.x243 - 2*m.x216*m.x244
                         - 2.118573403024*m.b3 - 2.118573403024*m.b45 >= -2.118573403024)

m.c43 = Constraint(expr=m.x215**2 + m.x216**2 + m.x243**2 + m.x244**2 - 2*m.x215*m.x243 - 2*m.x216*m.x244
                         - 2.118573403024*m.b4 - 2.118573403024*m.b46 >= -2.118573403024)

m.c44 = Constraint(expr=m.x215**2 + m.x216**2 + m.x245**2 + m.x246**2 - 2*m.x215*m.x245 - 2*m.x216*m.x246
                         - 2.118573403024*m.b2 - 2.118573403024*m.b47 >= -2.118573403024)

m.c45 = Constraint(expr=m.x215**2 + m.x216**2 + m.x245**2 + m.x246**2 - 2*m.x215*m.x245 - 2*m.x216*m.x246
                         - 2.118573403024*m.b3 - 2.118573403024*m.b48 >= -2.118573403024)

m.c46 = Constraint(expr=m.x215**2 + m.x216**2 + m.x245**2 + m.x246**2 - 2*m.x215*m.x245 - 2*m.x216*m.x246
                         - 2.118573403024*m.b4 - 2.118573403024*m.b49 >= -2.118573403024)

m.c47 = Constraint(expr=m.x215**2 + m.x216**2 + m.x247**2 + m.x248**2 - 2*m.x215*m.x247 - 2*m.x216*m.x248
                         - 4.509770398884*m.b2 - 4.509770398884*m.b50 >= -4.509770398884)

m.c48 = Constraint(expr=m.x215**2 + m.x216**2 + m.x247**2 + m.x248**2 - 2*m.x215*m.x247 - 2*m.x216*m.x248
                         - 4.509770398884*m.b3 - 4.509770398884*m.b51 >= -4.509770398884)

m.c49 = Constraint(expr=m.x215**2 + m.x216**2 + m.x247**2 + m.x248**2 - 2*m.x215*m.x247 - 2*m.x216*m.x248
                         - 4.509770398884*m.b4 - 4.509770398884*m.b52 >= -4.509770398884)

m.c50 = Constraint(expr=m.x215**2 + m.x216**2 + m.x249**2 + m.x250**2 - 2*m.x215*m.x249 - 2*m.x216*m.x250
                         - 4.509770398884*m.b2 - 4.509770398884*m.b53 >= -4.509770398884)

m.c51 = Constraint(expr=m.x215**2 + m.x216**2 + m.x249**2 + m.x250**2 - 2*m.x215*m.x249 - 2*m.x216*m.x250
                         - 4.509770398884*m.b3 - 4.509770398884*m.b54 >= -4.509770398884)

m.c52 = Constraint(expr=m.x215**2 + m.x216**2 + m.x249**2 + m.x250**2 - 2*m.x215*m.x249 - 2*m.x216*m.x250
                         - 4.509770398884*m.b4 - 4.509770398884*m.b55 >= -4.509770398884)

m.c53 = Constraint(expr=m.x215**2 + m.x216**2 + m.x251**2 + m.x252**2 - 2*m.x215*m.x251 - 2*m.x216*m.x252
                         - 6.408451746064*m.b2 - 6.408451746064*m.b56 >= -6.408451746064)

m.c54 = Constraint(expr=m.x215**2 + m.x216**2 + m.x251**2 + m.x252**2 - 2*m.x215*m.x251 - 2*m.x216*m.x252
                         - 6.408451746064*m.b3 - 6.408451746064*m.b57 >= -6.408451746064)

m.c55 = Constraint(expr=m.x215**2 + m.x216**2 + m.x251**2 + m.x252**2 - 2*m.x215*m.x251 - 2*m.x216*m.x252
                         - 6.408451746064*m.b4 - 6.408451746064*m.b58 >= -6.408451746064)

m.c56 = Constraint(expr=m.x215**2 + m.x216**2 + m.x253**2 + m.x254**2 - 2*m.x215*m.x253 - 2*m.x216*m.x254
                         - 6.408451746064*m.b2 - 6.408451746064*m.b59 >= -6.408451746064)

m.c57 = Constraint(expr=m.x215**2 + m.x216**2 + m.x253**2 + m.x254**2 - 2*m.x215*m.x253 - 2*m.x216*m.x254
                         - 6.408451746064*m.b3 - 6.408451746064*m.b60 >= -6.408451746064)

m.c58 = Constraint(expr=m.x215**2 + m.x216**2 + m.x253**2 + m.x254**2 - 2*m.x215*m.x253 - 2*m.x216*m.x254
                         - 6.408451746064*m.b4 - 6.408451746064*m.b61 >= -6.408451746064)

m.c59 = Constraint(expr=m.x215**2 + m.x216**2 + m.x217**2 + m.x218**2 - 2*m.x215*m.x217 - 2*m.x216*m.x218
                         - 1.436939228176*m.b2 - 1.436939228176*m.b5 >= -1.436939228176)

m.c60 = Constraint(expr=m.x215**2 + m.x216**2 + m.x217**2 + m.x218**2 - 2*m.x215*m.x217 - 2*m.x216*m.x218
                         - 1.436939228176*m.b3 - 1.436939228176*m.b6 >= -1.436939228176)

m.c61 = Constraint(expr=m.x215**2 + m.x216**2 + m.x217**2 + m.x218**2 - 2*m.x215*m.x217 - 2*m.x216*m.x218
                         - 1.436939228176*m.b4 - 1.436939228176*m.b7 >= -1.436939228176)

m.c62 = Constraint(expr=m.x217**2 + m.x218**2 + m.x219**2 + m.x220**2 - 2*m.x217*m.x219 - 2*m.x218*m.x220
                         - 1.436939228176*m.b5 - 1.436939228176*m.b8 >= -1.436939228176)

m.c63 = Constraint(expr=m.x217**2 + m.x218**2 + m.x219**2 + m.x220**2 - 2*m.x217*m.x219 - 2*m.x218*m.x220
                         - 1.436939228176*m.b6 - 1.436939228176*m.b9 >= -1.436939228176)

m.c64 = Constraint(expr=m.x217**2 + m.x218**2 + m.x219**2 + m.x220**2 - 2*m.x217*m.x219 - 2*m.x218*m.x220
                         - 1.436939228176*m.b7 - 1.436939228176*m.b10 >= -1.436939228176)

m.c65 = Constraint(expr=m.x217**2 + m.x218**2 + m.x221**2 + m.x222**2 - 2*m.x218*m.x222 - 2*m.x217*m.x221
                         - 1.436939228176*m.b5 - 1.436939228176*m.b11 >= -1.436939228176)

m.c66 = Constraint(expr=m.x217**2 + m.x218**2 + m.x221**2 + m.x222**2 - 2*m.x218*m.x222 - 2*m.x217*m.x221
                         - 1.436939228176*m.b6 - 1.436939228176*m.b12 >= -1.436939228176)

m.c67 = Constraint(expr=m.x217**2 + m.x218**2 + m.x221**2 + m.x222**2 - 2*m.x218*m.x222 - 2*m.x217*m.x221
                         - 1.436939228176*m.b7 - 1.436939228176*m.b13 >= -1.436939228176)

m.c68 = Constraint(expr=m.x217**2 + m.x218**2 + m.x223**2 + m.x224**2 - 2*m.x217*m.x223 - 2*m.x218*m.x224
                         - 1.436939228176*m.b5 - 1.436939228176*m.b14 >= -1.436939228176)

m.c69 = Constraint(expr=m.x217**2 + m.x218**2 + m.x223**2 + m.x224**2 - 2*m.x217*m.x223 - 2*m.x218*m.x224
                         - 1.436939228176*m.b6 - 1.436939228176*m.b15 >= -1.436939228176)

m.c70 = Constraint(expr=m.x217**2 + m.x218**2 + m.x223**2 + m.x224**2 - 2*m.x217*m.x223 - 2*m.x218*m.x224
                         - 1.436939228176*m.b7 - 1.436939228176*m.b16 >= -1.436939228176)

m.c71 = Constraint(expr=m.x217**2 + m.x218**2 + m.x225**2 + m.x226**2 - 2*m.x218*m.x226 - 2*m.x217*m.x225
                         - 1.436939228176*m.b5 - 1.436939228176*m.b17 >= -1.436939228176)

m.c72 = Constraint(expr=m.x217**2 + m.x218**2 + m.x225**2 + m.x226**2 - 2*m.x218*m.x226 - 2*m.x217*m.x225
                         - 1.436939228176*m.b6 - 1.436939228176*m.b18 >= -1.436939228176)

m.c73 = Constraint(expr=m.x217**2 + m.x218**2 + m.x225**2 + m.x226**2 - 2*m.x218*m.x226 - 2*m.x217*m.x225
                         - 1.436939228176*m.b7 - 1.436939228176*m.b19 >= -1.436939228176)

m.c74 = Constraint(expr=m.x217**2 + m.x218**2 + m.x227**2 + m.x228**2 - 2*m.x217*m.x227 - 2*m.x218*m.x228
                         - 0.887203867225*m.b5 - 0.887203867225*m.b20 >= -0.887203867225)

m.c75 = Constraint(expr=m.x217**2 + m.x218**2 + m.x227**2 + m.x228**2 - 2*m.x217*m.x227 - 2*m.x218*m.x228
                         - 0.887203867225*m.b6 - 0.887203867225*m.b21 >= -0.887203867225)

m.c76 = Constraint(expr=m.x217**2 + m.x218**2 + m.x227**2 + m.x228**2 - 2*m.x217*m.x227 - 2*m.x218*m.x228
                         - 0.887203867225*m.b7 - 0.887203867225*m.b22 >= -0.887203867225)

m.c77 = Constraint(expr=m.x217**2 + m.x218**2 + m.x229**2 + m.x230**2 - 2*m.x218*m.x230 - 2*m.x217*m.x229
                         - 0.887203867225*m.b5 - 0.887203867225*m.b23 >= -0.887203867225)

m.c78 = Constraint(expr=m.x217**2 + m.x218**2 + m.x229**2 + m.x230**2 - 2*m.x218*m.x230 - 2*m.x217*m.x229
                         - 0.887203867225*m.b6 - 0.887203867225*m.b24 >= -0.887203867225)

m.c79 = Constraint(expr=m.x217**2 + m.x218**2 + m.x229**2 + m.x230**2 - 2*m.x218*m.x230 - 2*m.x217*m.x229
                         - 0.887203867225*m.b7 - 0.887203867225*m.b25 >= -0.887203867225)

m.c80 = Constraint(expr=m.x217**2 + m.x218**2 + m.x231**2 + m.x232**2 - 2*m.x218*m.x232 - 2*m.x217*m.x231
                         - 0.887203867225*m.b5 - 0.887203867225*m.b26 >= -0.887203867225)

m.c81 = Constraint(expr=m.x217**2 + m.x218**2 + m.x231**2 + m.x232**2 - 2*m.x218*m.x232 - 2*m.x217*m.x231
                         - 0.887203867225*m.b6 - 0.887203867225*m.b27 >= -0.887203867225)

m.c82 = Constraint(expr=m.x217**2 + m.x218**2 + m.x231**2 + m.x232**2 - 2*m.x218*m.x232 - 2*m.x217*m.x231
                         - 0.887203867225*m.b7 - 0.887203867225*m.b28 >= -0.887203867225)

m.c83 = Constraint(expr=m.x217**2 + m.x218**2 + m.x233**2 + m.x234**2 - 2*m.x217*m.x233 - 2*m.x218*m.x234
                         - 0.887203867225*m.b5 - 0.887203867225*m.b29 >= -0.887203867225)

m.c84 = Constraint(expr=m.x217**2 + m.x218**2 + m.x233**2 + m.x234**2 - 2*m.x217*m.x233 - 2*m.x218*m.x234
                         - 0.887203867225*m.b6 - 0.887203867225*m.b30 >= -0.887203867225)

m.c85 = Constraint(expr=m.x217**2 + m.x218**2 + m.x233**2 + m.x234**2 - 2*m.x217*m.x233 - 2*m.x218*m.x234
                         - 0.887203867225*m.b7 - 0.887203867225*m.b31 >= -0.887203867225)

m.c86 = Constraint(expr=m.x217**2 + m.x218**2 + m.x235**2 + m.x236**2 - 2*m.x217*m.x235 - 2*m.x218*m.x236
                         - 0.887203867225*m.b5 - 0.887203867225*m.b32 >= -0.887203867225)

m.c87 = Constraint(expr=m.x217**2 + m.x218**2 + m.x235**2 + m.x236**2 - 2*m.x217*m.x235 - 2*m.x218*m.x236
                         - 0.887203867225*m.b6 - 0.887203867225*m.b33 >= -0.887203867225)

m.c88 = Constraint(expr=m.x217**2 + m.x218**2 + m.x235**2 + m.x236**2 - 2*m.x217*m.x235 - 2*m.x218*m.x236
                         - 0.887203867225*m.b7 - 0.887203867225*m.b34 >= -0.887203867225)

m.c89 = Constraint(expr=m.x217**2 + m.x218**2 + m.x237**2 + m.x238**2 - 2*m.x218*m.x238 - 2*m.x217*m.x237
                         - 2.118573403024*m.b5 - 2.118573403024*m.b35 >= -2.118573403024)

m.c90 = Constraint(expr=m.x217**2 + m.x218**2 + m.x237**2 + m.x238**2 - 2*m.x218*m.x238 - 2*m.x217*m.x237
                         - 2.118573403024*m.b6 - 2.118573403024*m.b36 >= -2.118573403024)

m.c91 = Constraint(expr=m.x217**2 + m.x218**2 + m.x237**2 + m.x238**2 - 2*m.x218*m.x238 - 2*m.x217*m.x237
                         - 2.118573403024*m.b7 - 2.118573403024*m.b37 >= -2.118573403024)

m.c92 = Constraint(expr=m.x217**2 + m.x218**2 + m.x239**2 + m.x240**2 - 2*m.x218*m.x240 - 2*m.x217*m.x239
                         - 2.118573403024*m.b5 - 2.118573403024*m.b38 >= -2.118573403024)

m.c93 = Constraint(expr=m.x217**2 + m.x218**2 + m.x239**2 + m.x240**2 - 2*m.x218*m.x240 - 2*m.x217*m.x239
                         - 2.118573403024*m.b6 - 2.118573403024*m.b39 >= -2.118573403024)

m.c94 = Constraint(expr=m.x217**2 + m.x218**2 + m.x239**2 + m.x240**2 - 2*m.x218*m.x240 - 2*m.x217*m.x239
                         - 2.118573403024*m.b7 - 2.118573403024*m.b40 >= -2.118573403024)

m.c95 = Constraint(expr=m.x217**2 + m.x218**2 + m.x241**2 + m.x242**2 - 2*m.x217*m.x241 - 2*m.x218*m.x242
                         - 2.118573403024*m.b5 - 2.118573403024*m.b41 >= -2.118573403024)

m.c96 = Constraint(expr=m.x217**2 + m.x218**2 + m.x241**2 + m.x242**2 - 2*m.x217*m.x241 - 2*m.x218*m.x242
                         - 2.118573403024*m.b6 - 2.118573403024*m.b42 >= -2.118573403024)

m.c97 = Constraint(expr=m.x217**2 + m.x218**2 + m.x241**2 + m.x242**2 - 2*m.x217*m.x241 - 2*m.x218*m.x242
                         - 2.118573403024*m.b7 - 2.118573403024*m.b43 >= -2.118573403024)

m.c98 = Constraint(expr=m.x217**2 + m.x218**2 + m.x243**2 + m.x244**2 - 2*m.x217*m.x243 - 2*m.x218*m.x244
                         - 2.118573403024*m.b5 - 2.118573403024*m.b44 >= -2.118573403024)

m.c99 = Constraint(expr=m.x217**2 + m.x218**2 + m.x243**2 + m.x244**2 - 2*m.x217*m.x243 - 2*m.x218*m.x244
                         - 2.118573403024*m.b6 - 2.118573403024*m.b45 >= -2.118573403024)

m.c100 = Constraint(expr=m.x217**2 + m.x218**2 + m.x243**2 + m.x244**2 - 2*m.x217*m.x243 - 2*m.x218*m.x244
                          - 2.118573403024*m.b7 - 2.118573403024*m.b46 >= -2.118573403024)

m.c101 = Constraint(expr=m.x217**2 + m.x218**2 + m.x245**2 + m.x246**2 - 2*m.x217*m.x245 - 2*m.x218*m.x246
                          - 2.118573403024*m.b5 - 2.118573403024*m.b47 >= -2.118573403024)

m.c102 = Constraint(expr=m.x217**2 + m.x218**2 + m.x245**2 + m.x246**2 - 2*m.x217*m.x245 - 2*m.x218*m.x246
                          - 2.118573403024*m.b6 - 2.118573403024*m.b48 >= -2.118573403024)

m.c103 = Constraint(expr=m.x217**2 + m.x218**2 + m.x245**2 + m.x246**2 - 2*m.x217*m.x245 - 2*m.x218*m.x246
                          - 2.118573403024*m.b7 - 2.118573403024*m.b49 >= -2.118573403024)

m.c104 = Constraint(expr=m.x217**2 + m.x218**2 + m.x247**2 + m.x248**2 - 2*m.x217*m.x247 - 2*m.x218*m.x248
                          - 4.509770398884*m.b5 - 4.509770398884*m.b50 >= -4.509770398884)

m.c105 = Constraint(expr=m.x217**2 + m.x218**2 + m.x247**2 + m.x248**2 - 2*m.x217*m.x247 - 2*m.x218*m.x248
                          - 4.509770398884*m.b6 - 4.509770398884*m.b51 >= -4.509770398884)

m.c106 = Constraint(expr=m.x217**2 + m.x218**2 + m.x247**2 + m.x248**2 - 2*m.x217*m.x247 - 2*m.x218*m.x248
                          - 4.509770398884*m.b7 - 4.509770398884*m.b52 >= -4.509770398884)

m.c107 = Constraint(expr=m.x217**2 + m.x218**2 + m.x249**2 + m.x250**2 - 2*m.x217*m.x249 - 2*m.x218*m.x250
                          - 4.509770398884*m.b5 - 4.509770398884*m.b53 >= -4.509770398884)

m.c108 = Constraint(expr=m.x217**2 + m.x218**2 + m.x249**2 + m.x250**2 - 2*m.x217*m.x249 - 2*m.x218*m.x250
                          - 4.509770398884*m.b6 - 4.509770398884*m.b54 >= -4.509770398884)

m.c109 = Constraint(expr=m.x217**2 + m.x218**2 + m.x249**2 + m.x250**2 - 2*m.x217*m.x249 - 2*m.x218*m.x250
                          - 4.509770398884*m.b7 - 4.509770398884*m.b55 >= -4.509770398884)

m.c110 = Constraint(expr=m.x217**2 + m.x218**2 + m.x251**2 + m.x252**2 - 2*m.x217*m.x251 - 2*m.x218*m.x252
                          - 6.408451746064*m.b5 - 6.408451746064*m.b56 >= -6.408451746064)

m.c111 = Constraint(expr=m.x217**2 + m.x218**2 + m.x251**2 + m.x252**2 - 2*m.x217*m.x251 - 2*m.x218*m.x252
                          - 6.408451746064*m.b6 - 6.408451746064*m.b57 >= -6.408451746064)

m.c112 = Constraint(expr=m.x217**2 + m.x218**2 + m.x251**2 + m.x252**2 - 2*m.x217*m.x251 - 2*m.x218*m.x252
                          - 6.408451746064*m.b7 - 6.408451746064*m.b58 >= -6.408451746064)

m.c113 = Constraint(expr=m.x217**2 + m.x218**2 + m.x253**2 + m.x254**2 - 2*m.x217*m.x253 - 2*m.x218*m.x254
                          - 6.408451746064*m.b5 - 6.408451746064*m.b59 >= -6.408451746064)

m.c114 = Constraint(expr=m.x217**2 + m.x218**2 + m.x253**2 + m.x254**2 - 2*m.x217*m.x253 - 2*m.x218*m.x254
                          - 6.408451746064*m.b6 - 6.408451746064*m.b60 >= -6.408451746064)

m.c115 = Constraint(expr=m.x217**2 + m.x218**2 + m.x253**2 + m.x254**2 - 2*m.x217*m.x253 - 2*m.x218*m.x254
                          - 6.408451746064*m.b7 - 6.408451746064*m.b61 >= -6.408451746064)

m.c116 = Constraint(expr=m.x215**2 + m.x216**2 + m.x219**2 + m.x220**2 - 2*m.x215*m.x219 - 2*m.x216*m.x220
                          - 1.436939228176*m.b2 - 1.436939228176*m.b8 >= -1.436939228176)

m.c117 = Constraint(expr=m.x215**2 + m.x216**2 + m.x219**2 + m.x220**2 - 2*m.x215*m.x219 - 2*m.x216*m.x220
                          - 1.436939228176*m.b3 - 1.436939228176*m.b9 >= -1.436939228176)

m.c118 = Constraint(expr=m.x215**2 + m.x216**2 + m.x219**2 + m.x220**2 - 2*m.x215*m.x219 - 2*m.x216*m.x220
                          - 1.436939228176*m.b4 - 1.436939228176*m.b10 >= -1.436939228176)

m.c119 = Constraint(expr=m.x217**2 + m.x218**2 + m.x219**2 + m.x220**2 - 2*m.x217*m.x219 - 2*m.x218*m.x220
                          - 1.436939228176*m.b5 - 1.436939228176*m.b8 >= -1.436939228176)

m.c120 = Constraint(expr=m.x217**2 + m.x218**2 + m.x219**2 + m.x220**2 - 2*m.x217*m.x219 - 2*m.x218*m.x220
                          - 1.436939228176*m.b6 - 1.436939228176*m.b9 >= -1.436939228176)

m.c121 = Constraint(expr=m.x217**2 + m.x218**2 + m.x219**2 + m.x220**2 - 2*m.x217*m.x219 - 2*m.x218*m.x220
                          - 1.436939228176*m.b7 - 1.436939228176*m.b10 >= -1.436939228176)

m.c122 = Constraint(expr=m.x219**2 + m.x220**2 + m.x221**2 + m.x222**2 - 2*m.x219*m.x221 - 2*m.x220*m.x222
                          - 1.436939228176*m.b8 - 1.436939228176*m.b11 >= -1.436939228176)

m.c123 = Constraint(expr=m.x219**2 + m.x220**2 + m.x221**2 + m.x222**2 - 2*m.x219*m.x221 - 2*m.x220*m.x222
                          - 1.436939228176*m.b9 - 1.436939228176*m.b12 >= -1.436939228176)

m.c124 = Constraint(expr=m.x219**2 + m.x220**2 + m.x221**2 + m.x222**2 - 2*m.x219*m.x221 - 2*m.x220*m.x222
                          - 1.436939228176*m.b10 - 1.436939228176*m.b13 >= -1.436939228176)

m.c125 = Constraint(expr=m.x219**2 + m.x220**2 + m.x223**2 + m.x224**2 - 2*m.x220*m.x224 - 2*m.x219*m.x223
                          - 1.436939228176*m.b8 - 1.436939228176*m.b14 >= -1.436939228176)

m.c126 = Constraint(expr=m.x219**2 + m.x220**2 + m.x223**2 + m.x224**2 - 2*m.x220*m.x224 - 2*m.x219*m.x223
                          - 1.436939228176*m.b9 - 1.436939228176*m.b15 >= -1.436939228176)

m.c127 = Constraint(expr=m.x219**2 + m.x220**2 + m.x223**2 + m.x224**2 - 2*m.x220*m.x224 - 2*m.x219*m.x223
                          - 1.436939228176*m.b10 - 1.436939228176*m.b16 >= -1.436939228176)

m.c128 = Constraint(expr=m.x219**2 + m.x220**2 + m.x225**2 + m.x226**2 - 2*m.x220*m.x226 - 2*m.x219*m.x225
                          - 1.436939228176*m.b8 - 1.436939228176*m.b17 >= -1.436939228176)

m.c129 = Constraint(expr=m.x219**2 + m.x220**2 + m.x225**2 + m.x226**2 - 2*m.x220*m.x226 - 2*m.x219*m.x225
                          - 1.436939228176*m.b9 - 1.436939228176*m.b18 >= -1.436939228176)

m.c130 = Constraint(expr=m.x219**2 + m.x220**2 + m.x225**2 + m.x226**2 - 2*m.x220*m.x226 - 2*m.x219*m.x225
                          - 1.436939228176*m.b10 - 1.436939228176*m.b19 >= -1.436939228176)

m.c131 = Constraint(expr=m.x219**2 + m.x220**2 + m.x227**2 + m.x228**2 - 2*m.x220*m.x228 - 2*m.x219*m.x227
                          - 0.887203867225*m.b8 - 0.887203867225*m.b20 >= -0.887203867225)

m.c132 = Constraint(expr=m.x219**2 + m.x220**2 + m.x227**2 + m.x228**2 - 2*m.x220*m.x228 - 2*m.x219*m.x227
                          - 0.887203867225*m.b9 - 0.887203867225*m.b21 >= -0.887203867225)

m.c133 = Constraint(expr=m.x219**2 + m.x220**2 + m.x227**2 + m.x228**2 - 2*m.x220*m.x228 - 2*m.x219*m.x227
                          - 0.887203867225*m.b10 - 0.887203867225*m.b22 >= -0.887203867225)

m.c134 = Constraint(expr=m.x219**2 + m.x220**2 + m.x229**2 + m.x230**2 - 2*m.x220*m.x230 - 2*m.x219*m.x229
                          - 0.887203867225*m.b8 - 0.887203867225*m.b23 >= -0.887203867225)

m.c135 = Constraint(expr=m.x219**2 + m.x220**2 + m.x229**2 + m.x230**2 - 2*m.x220*m.x230 - 2*m.x219*m.x229
                          - 0.887203867225*m.b9 - 0.887203867225*m.b24 >= -0.887203867225)

m.c136 = Constraint(expr=m.x219**2 + m.x220**2 + m.x229**2 + m.x230**2 - 2*m.x220*m.x230 - 2*m.x219*m.x229
                          - 0.887203867225*m.b10 - 0.887203867225*m.b25 >= -0.887203867225)

m.c137 = Constraint(expr=m.x219**2 + m.x220**2 + m.x231**2 + m.x232**2 - 2*m.x219*m.x231 - 2*m.x220*m.x232
                          - 0.887203867225*m.b8 - 0.887203867225*m.b26 >= -0.887203867225)

m.c138 = Constraint(expr=m.x219**2 + m.x220**2 + m.x231**2 + m.x232**2 - 2*m.x219*m.x231 - 2*m.x220*m.x232
                          - 0.887203867225*m.b9 - 0.887203867225*m.b27 >= -0.887203867225)

m.c139 = Constraint(expr=m.x219**2 + m.x220**2 + m.x231**2 + m.x232**2 - 2*m.x219*m.x231 - 2*m.x220*m.x232
                          - 0.887203867225*m.b10 - 0.887203867225*m.b28 >= -0.887203867225)

m.c140 = Constraint(expr=m.x219**2 + m.x220**2 + m.x233**2 + m.x234**2 - 2*m.x220*m.x234 - 2*m.x219*m.x233
                          - 0.887203867225*m.b8 - 0.887203867225*m.b29 >= -0.887203867225)

m.c141 = Constraint(expr=m.x219**2 + m.x220**2 + m.x233**2 + m.x234**2 - 2*m.x220*m.x234 - 2*m.x219*m.x233
                          - 0.887203867225*m.b9 - 0.887203867225*m.b30 >= -0.887203867225)

m.c142 = Constraint(expr=m.x219**2 + m.x220**2 + m.x233**2 + m.x234**2 - 2*m.x220*m.x234 - 2*m.x219*m.x233
                          - 0.887203867225*m.b10 - 0.887203867225*m.b31 >= -0.887203867225)

m.c143 = Constraint(expr=m.x219**2 + m.x220**2 + m.x235**2 + m.x236**2 - 2*m.x219*m.x235 - 2*m.x220*m.x236
                          - 0.887203867225*m.b8 - 0.887203867225*m.b32 >= -0.887203867225)

m.c144 = Constraint(expr=m.x219**2 + m.x220**2 + m.x235**2 + m.x236**2 - 2*m.x219*m.x235 - 2*m.x220*m.x236
                          - 0.887203867225*m.b9 - 0.887203867225*m.b33 >= -0.887203867225)

m.c145 = Constraint(expr=m.x219**2 + m.x220**2 + m.x235**2 + m.x236**2 - 2*m.x219*m.x235 - 2*m.x220*m.x236
                          - 0.887203867225*m.b10 - 0.887203867225*m.b34 >= -0.887203867225)

m.c146 = Constraint(expr=m.x219**2 + m.x220**2 + m.x237**2 + m.x238**2 - 2*m.x220*m.x238 - 2*m.x219*m.x237
                          - 2.118573403024*m.b8 - 2.118573403024*m.b35 >= -2.118573403024)

m.c147 = Constraint(expr=m.x219**2 + m.x220**2 + m.x237**2 + m.x238**2 - 2*m.x220*m.x238 - 2*m.x219*m.x237
                          - 2.118573403024*m.b9 - 2.118573403024*m.b36 >= -2.118573403024)

m.c148 = Constraint(expr=m.x219**2 + m.x220**2 + m.x237**2 + m.x238**2 - 2*m.x220*m.x238 - 2*m.x219*m.x237
                          - 2.118573403024*m.b10 - 2.118573403024*m.b37 >= -2.118573403024)

m.c149 = Constraint(expr=m.x219**2 + m.x220**2 + m.x239**2 + m.x240**2 - 2*m.x220*m.x240 - 2*m.x219*m.x239
                          - 2.118573403024*m.b8 - 2.118573403024*m.b38 >= -2.118573403024)

m.c150 = Constraint(expr=m.x219**2 + m.x220**2 + m.x239**2 + m.x240**2 - 2*m.x220*m.x240 - 2*m.x219*m.x239
                          - 2.118573403024*m.b9 - 2.118573403024*m.b39 >= -2.118573403024)

m.c151 = Constraint(expr=m.x219**2 + m.x220**2 + m.x239**2 + m.x240**2 - 2*m.x219*m.x239 - 2*m.x220*m.x240
                          - 2.118573403024*m.b10 - 2.118573403024*m.b40 >= -2.118573403024)

m.c152 = Constraint(expr=m.x219**2 + m.x220**2 + m.x241**2 + m.x242**2 - 2*m.x219*m.x241 - 2*m.x220*m.x242
                          - 2.118573403024*m.b8 - 2.118573403024*m.b41 >= -2.118573403024)

m.c153 = Constraint(expr=m.x219**2 + m.x220**2 + m.x241**2 + m.x242**2 - 2*m.x219*m.x241 - 2*m.x220*m.x242
                          - 2.118573403024*m.b9 - 2.118573403024*m.b42 >= -2.118573403024)

m.c154 = Constraint(expr=m.x219**2 + m.x220**2 + m.x241**2 + m.x242**2 - 2*m.x219*m.x241 - 2*m.x220*m.x242
                          - 2.118573403024*m.b10 - 2.118573403024*m.b43 >= -2.118573403024)

m.c155 = Constraint(expr=m.x219**2 + m.x220**2 + m.x243**2 + m.x244**2 - 2*m.x219*m.x243 - 2*m.x220*m.x244
                          - 2.118573403024*m.b8 - 2.118573403024*m.b44 >= -2.118573403024)

m.c156 = Constraint(expr=m.x219**2 + m.x220**2 + m.x243**2 + m.x244**2 - 2*m.x219*m.x243 - 2*m.x220*m.x244
                          - 2.118573403024*m.b9 - 2.118573403024*m.b45 >= -2.118573403024)

m.c157 = Constraint(expr=m.x219**2 + m.x220**2 + m.x243**2 + m.x244**2 - 2*m.x219*m.x243 - 2*m.x220*m.x244
                          - 2.118573403024*m.b10 - 2.118573403024*m.b46 >= -2.118573403024)

m.c158 = Constraint(expr=m.x219**2 + m.x220**2 + m.x245**2 + m.x246**2 - 2*m.x219*m.x245 - 2*m.x220*m.x246
                          - 2.118573403024*m.b8 - 2.118573403024*m.b47 >= -2.118573403024)

m.c159 = Constraint(expr=m.x219**2 + m.x220**2 + m.x245**2 + m.x246**2 - 2*m.x219*m.x245 - 2*m.x220*m.x246
                          - 2.118573403024*m.b9 - 2.118573403024*m.b48 >= -2.118573403024)

m.c160 = Constraint(expr=m.x219**2 + m.x220**2 + m.x245**2 + m.x246**2 - 2*m.x219*m.x245 - 2*m.x220*m.x246
                          - 2.118573403024*m.b10 - 2.118573403024*m.b49 >= -2.118573403024)

m.c161 = Constraint(expr=m.x219**2 + m.x220**2 + m.x247**2 + m.x248**2 - 2*m.x219*m.x247 - 2*m.x220*m.x248
                          - 4.509770398884*m.b8 - 4.509770398884*m.b50 >= -4.509770398884)

m.c162 = Constraint(expr=m.x219**2 + m.x220**2 + m.x247**2 + m.x248**2 - 2*m.x219*m.x247 - 2*m.x220*m.x248
                          - 4.509770398884*m.b9 - 4.509770398884*m.b51 >= -4.509770398884)

m.c163 = Constraint(expr=m.x219**2 + m.x220**2 + m.x247**2 + m.x248**2 - 2*m.x219*m.x247 - 2*m.x220*m.x248
                          - 4.509770398884*m.b10 - 4.509770398884*m.b52 >= -4.509770398884)

m.c164 = Constraint(expr=m.x219**2 + m.x220**2 + m.x249**2 + m.x250**2 - 2*m.x219*m.x249 - 2*m.x220*m.x250
                          - 4.509770398884*m.b8 - 4.509770398884*m.b53 >= -4.509770398884)

m.c165 = Constraint(expr=m.x219**2 + m.x220**2 + m.x249**2 + m.x250**2 - 2*m.x219*m.x249 - 2*m.x220*m.x250
                          - 4.509770398884*m.b9 - 4.509770398884*m.b54 >= -4.509770398884)

m.c166 = Constraint(expr=m.x219**2 + m.x220**2 + m.x249**2 + m.x250**2 - 2*m.x219*m.x249 - 2*m.x220*m.x250
                          - 4.509770398884*m.b10 - 4.509770398884*m.b55 >= -4.509770398884)

m.c167 = Constraint(expr=m.x219**2 + m.x220**2 + m.x251**2 + m.x252**2 - 2*m.x219*m.x251 - 2*m.x220*m.x252
                          - 6.408451746064*m.b8 - 6.408451746064*m.b56 >= -6.408451746064)

m.c168 = Constraint(expr=m.x219**2 + m.x220**2 + m.x251**2 + m.x252**2 - 2*m.x219*m.x251 - 2*m.x220*m.x252
                          - 6.408451746064*m.b9 - 6.408451746064*m.b57 >= -6.408451746064)

m.c169 = Constraint(expr=m.x219**2 + m.x220**2 + m.x251**2 + m.x252**2 - 2*m.x219*m.x251 - 2*m.x220*m.x252
                          - 6.408451746064*m.b10 - 6.408451746064*m.b58 >= -6.408451746064)

m.c170 = Constraint(expr=m.x219**2 + m.x220**2 + m.x253**2 + m.x254**2 - 2*m.x219*m.x253 - 2*m.x220*m.x254
                          - 6.408451746064*m.b8 - 6.408451746064*m.b59 >= -6.408451746064)

m.c171 = Constraint(expr=m.x219**2 + m.x220**2 + m.x253**2 + m.x254**2 - 2*m.x219*m.x253 - 2*m.x220*m.x254
                          - 6.408451746064*m.b9 - 6.408451746064*m.b60 >= -6.408451746064)

m.c172 = Constraint(expr=m.x219**2 + m.x220**2 + m.x253**2 + m.x254**2 - 2*m.x219*m.x253 - 2*m.x220*m.x254
                          - 6.408451746064*m.b10 - 6.408451746064*m.b61 >= -6.408451746064)

m.c173 = Constraint(expr=m.x215**2 + m.x216**2 + m.x221**2 + m.x222**2 - 2*m.x216*m.x222 - 2*m.x215*m.x221
                          - 1.436939228176*m.b2 - 1.436939228176*m.b11 >= -1.436939228176)

m.c174 = Constraint(expr=m.x215**2 + m.x216**2 + m.x221**2 + m.x222**2 - 2*m.x216*m.x222 - 2*m.x215*m.x221
                          - 1.436939228176*m.b3 - 1.436939228176*m.b12 >= -1.436939228176)

m.c175 = Constraint(expr=m.x215**2 + m.x216**2 + m.x221**2 + m.x222**2 - 2*m.x216*m.x222 - 2*m.x215*m.x221
                          - 1.436939228176*m.b4 - 1.436939228176*m.b13 >= -1.436939228176)

m.c176 = Constraint(expr=m.x217**2 + m.x218**2 + m.x221**2 + m.x222**2 - 2*m.x218*m.x222 - 2*m.x217*m.x221
                          - 1.436939228176*m.b5 - 1.436939228176*m.b11 >= -1.436939228176)

m.c177 = Constraint(expr=m.x217**2 + m.x218**2 + m.x221**2 + m.x222**2 - 2*m.x218*m.x222 - 2*m.x217*m.x221
                          - 1.436939228176*m.b6 - 1.436939228176*m.b12 >= -1.436939228176)

m.c178 = Constraint(expr=m.x217**2 + m.x218**2 + m.x221**2 + m.x222**2 - 2*m.x218*m.x222 - 2*m.x217*m.x221
                          - 1.436939228176*m.b7 - 1.436939228176*m.b13 >= -1.436939228176)

m.c179 = Constraint(expr=m.x219**2 + m.x220**2 + m.x221**2 + m.x222**2 - 2*m.x219*m.x221 - 2*m.x220*m.x222
                          - 1.436939228176*m.b8 - 1.436939228176*m.b11 >= -1.436939228176)

m.c180 = Constraint(expr=m.x219**2 + m.x220**2 + m.x221**2 + m.x222**2 - 2*m.x219*m.x221 - 2*m.x220*m.x222
                          - 1.436939228176*m.b9 - 1.436939228176*m.b12 >= -1.436939228176)

m.c181 = Constraint(expr=m.x219**2 + m.x220**2 + m.x221**2 + m.x222**2 - 2*m.x219*m.x221 - 2*m.x220*m.x222
                          - 1.436939228176*m.b10 - 1.436939228176*m.b13 >= -1.436939228176)

m.c182 = Constraint(expr=m.x221**2 + m.x222**2 + m.x223**2 + m.x224**2 - 2*m.x221*m.x223 - 2*m.x222*m.x224
                          - 1.436939228176*m.b11 - 1.436939228176*m.b14 >= -1.436939228176)

m.c183 = Constraint(expr=m.x221**2 + m.x222**2 + m.x223**2 + m.x224**2 - 2*m.x221*m.x223 - 2*m.x222*m.x224
                          - 1.436939228176*m.b12 - 1.436939228176*m.b15 >= -1.436939228176)

m.c184 = Constraint(expr=m.x221**2 + m.x222**2 + m.x223**2 + m.x224**2 - 2*m.x221*m.x223 - 2*m.x222*m.x224
                          - 1.436939228176*m.b13 - 1.436939228176*m.b16 >= -1.436939228176)

m.c185 = Constraint(expr=m.x221**2 + m.x222**2 + m.x225**2 + m.x226**2 - 2*m.x221*m.x225 - 2*m.x222*m.x226
                          - 1.436939228176*m.b11 - 1.436939228176*m.b17 >= -1.436939228176)

m.c186 = Constraint(expr=m.x221**2 + m.x222**2 + m.x225**2 + m.x226**2 - 2*m.x221*m.x225 - 2*m.x222*m.x226
                          - 1.436939228176*m.b12 - 1.436939228176*m.b18 >= -1.436939228176)

m.c187 = Constraint(expr=m.x221**2 + m.x222**2 + m.x225**2 + m.x226**2 - 2*m.x221*m.x225 - 2*m.x222*m.x226
                          - 1.436939228176*m.b13 - 1.436939228176*m.b19 >= -1.436939228176)

m.c188 = Constraint(expr=m.x221**2 + m.x222**2 + m.x227**2 + m.x228**2 - 2*m.x221*m.x227 - 2*m.x222*m.x228
                          - 0.887203867225*m.b11 - 0.887203867225*m.b20 >= -0.887203867225)

m.c189 = Constraint(expr=m.x221**2 + m.x222**2 + m.x227**2 + m.x228**2 - 2*m.x221*m.x227 - 2*m.x222*m.x228
                          - 0.887203867225*m.b12 - 0.887203867225*m.b21 >= -0.887203867225)

m.c190 = Constraint(expr=m.x221**2 + m.x222**2 + m.x227**2 + m.x228**2 - 2*m.x221*m.x227 - 2*m.x222*m.x228
                          - 0.887203867225*m.b13 - 0.887203867225*m.b22 >= -0.887203867225)

m.c191 = Constraint(expr=m.x221**2 + m.x222**2 + m.x229**2 + m.x230**2 - 2*m.x221*m.x229 - 2*m.x222*m.x230
                          - 0.887203867225*m.b11 - 0.887203867225*m.b23 >= -0.887203867225)

m.c192 = Constraint(expr=m.x221**2 + m.x222**2 + m.x229**2 + m.x230**2 - 2*m.x221*m.x229 - 2*m.x222*m.x230
                          - 0.887203867225*m.b12 - 0.887203867225*m.b24 >= -0.887203867225)

m.c193 = Constraint(expr=m.x221**2 + m.x222**2 + m.x229**2 + m.x230**2 - 2*m.x221*m.x229 - 2*m.x222*m.x230
                          - 0.887203867225*m.b13 - 0.887203867225*m.b25 >= -0.887203867225)

m.c194 = Constraint(expr=m.x221**2 + m.x222**2 + m.x231**2 + m.x232**2 - 2*m.x221*m.x231 - 2*m.x222*m.x232
                          - 0.887203867225*m.b11 - 0.887203867225*m.b26 >= -0.887203867225)

m.c195 = Constraint(expr=m.x221**2 + m.x222**2 + m.x231**2 + m.x232**2 - 2*m.x221*m.x231 - 2*m.x222*m.x232
                          - 0.887203867225*m.b12 - 0.887203867225*m.b27 >= -0.887203867225)

m.c196 = Constraint(expr=m.x221**2 + m.x222**2 + m.x231**2 + m.x232**2 - 2*m.x221*m.x231 - 2*m.x222*m.x232
                          - 0.887203867225*m.b13 - 0.887203867225*m.b28 >= -0.887203867225)

m.c197 = Constraint(expr=m.x221**2 + m.x222**2 + m.x233**2 + m.x234**2 - 2*m.x221*m.x233 - 2*m.x222*m.x234
                          - 0.887203867225*m.b11 - 0.887203867225*m.b29 >= -0.887203867225)

m.c198 = Constraint(expr=m.x221**2 + m.x222**2 + m.x233**2 + m.x234**2 - 2*m.x221*m.x233 - 2*m.x222*m.x234
                          - 0.887203867225*m.b12 - 0.887203867225*m.b30 >= -0.887203867225)

m.c199 = Constraint(expr=m.x221**2 + m.x222**2 + m.x233**2 + m.x234**2 - 2*m.x221*m.x233 - 2*m.x222*m.x234
                          - 0.887203867225*m.b13 - 0.887203867225*m.b31 >= -0.887203867225)

m.c200 = Constraint(expr=m.x221**2 + m.x222**2 + m.x235**2 + m.x236**2 - 2*m.x221*m.x235 - 2*m.x222*m.x236
                          - 0.887203867225*m.b11 - 0.887203867225*m.b32 >= -0.887203867225)

m.c201 = Constraint(expr=m.x221**2 + m.x222**2 + m.x235**2 + m.x236**2 - 2*m.x221*m.x235 - 2*m.x222*m.x236
                          - 0.887203867225*m.b12 - 0.887203867225*m.b33 >= -0.887203867225)

m.c202 = Constraint(expr=m.x221**2 + m.x222**2 + m.x235**2 + m.x236**2 - 2*m.x221*m.x235 - 2*m.x222*m.x236
                          - 0.887203867225*m.b13 - 0.887203867225*m.b34 >= -0.887203867225)

m.c203 = Constraint(expr=m.x221**2 + m.x222**2 + m.x237**2 + m.x238**2 - 2*m.x221*m.x237 - 2*m.x222*m.x238
                          - 2.118573403024*m.b11 - 2.118573403024*m.b35 >= -2.118573403024)

m.c204 = Constraint(expr=m.x221**2 + m.x222**2 + m.x237**2 + m.x238**2 - 2*m.x221*m.x237 - 2*m.x222*m.x238
                          - 2.118573403024*m.b12 - 2.118573403024*m.b36 >= -2.118573403024)

m.c205 = Constraint(expr=m.x221**2 + m.x222**2 + m.x237**2 + m.x238**2 - 2*m.x221*m.x237 - 2*m.x222*m.x238
                          - 2.118573403024*m.b13 - 2.118573403024*m.b37 >= -2.118573403024)

m.c206 = Constraint(expr=m.x221**2 + m.x222**2 + m.x239**2 + m.x240**2 - 2*m.x221*m.x239 - 2*m.x222*m.x240
                          - 2.118573403024*m.b11 - 2.118573403024*m.b38 >= -2.118573403024)

m.c207 = Constraint(expr=m.x221**2 + m.x222**2 + m.x239**2 + m.x240**2 - 2*m.x221*m.x239 - 2*m.x222*m.x240
                          - 2.118573403024*m.b12 - 2.118573403024*m.b39 >= -2.118573403024)

m.c208 = Constraint(expr=m.x221**2 + m.x222**2 + m.x239**2 + m.x240**2 - 2*m.x221*m.x239 - 2*m.x222*m.x240
                          - 2.118573403024*m.b13 - 2.118573403024*m.b40 >= -2.118573403024)

m.c209 = Constraint(expr=m.x221**2 + m.x222**2 + m.x241**2 + m.x242**2 - 2*m.x221*m.x241 - 2*m.x222*m.x242
                          - 2.118573403024*m.b11 - 2.118573403024*m.b41 >= -2.118573403024)

m.c210 = Constraint(expr=m.x221**2 + m.x222**2 + m.x241**2 + m.x242**2 - 2*m.x221*m.x241 - 2*m.x222*m.x242
                          - 2.118573403024*m.b12 - 2.118573403024*m.b42 >= -2.118573403024)

m.c211 = Constraint(expr=m.x221**2 + m.x222**2 + m.x241**2 + m.x242**2 - 2*m.x221*m.x241 - 2*m.x222*m.x242
                          - 2.118573403024*m.b13 - 2.118573403024*m.b43 >= -2.118573403024)

m.c212 = Constraint(expr=m.x221**2 + m.x222**2 + m.x243**2 + m.x244**2 - 2*m.x221*m.x243 - 2*m.x222*m.x244
                          - 2.118573403024*m.b11 - 2.118573403024*m.b44 >= -2.118573403024)

m.c213 = Constraint(expr=m.x221**2 + m.x222**2 + m.x243**2 + m.x244**2 - 2*m.x221*m.x243 - 2*m.x222*m.x244
                          - 2.118573403024*m.b12 - 2.118573403024*m.b45 >= -2.118573403024)

m.c214 = Constraint(expr=m.x221**2 + m.x222**2 + m.x243**2 + m.x244**2 - 2*m.x221*m.x243 - 2*m.x222*m.x244
                          - 2.118573403024*m.b13 - 2.118573403024*m.b46 >= -2.118573403024)

m.c215 = Constraint(expr=m.x221**2 + m.x222**2 + m.x245**2 + m.x246**2 - 2*m.x222*m.x246 - 2*m.x221*m.x245
                          - 2.118573403024*m.b11 - 2.118573403024*m.b47 >= -2.118573403024)

m.c216 = Constraint(expr=m.x221**2 + m.x222**2 + m.x245**2 + m.x246**2 - 2*m.x222*m.x246 - 2*m.x221*m.x245
                          - 2.118573403024*m.b12 - 2.118573403024*m.b48 >= -2.118573403024)

m.c217 = Constraint(expr=m.x221**2 + m.x222**2 + m.x245**2 + m.x246**2 - 2*m.x222*m.x246 - 2*m.x221*m.x245
                          - 2.118573403024*m.b13 - 2.118573403024*m.b49 >= -2.118573403024)

m.c218 = Constraint(expr=m.x221**2 + m.x222**2 + m.x247**2 + m.x248**2 - 2*m.x222*m.x248 - 2*m.x221*m.x247
                          - 4.509770398884*m.b11 - 4.509770398884*m.b50 >= -4.509770398884)

m.c219 = Constraint(expr=m.x221**2 + m.x222**2 + m.x247**2 + m.x248**2 - 2*m.x222*m.x248 - 2*m.x221*m.x247
                          - 4.509770398884*m.b12 - 4.509770398884*m.b51 >= -4.509770398884)

m.c220 = Constraint(expr=m.x221**2 + m.x222**2 + m.x247**2 + m.x248**2 - 2*m.x222*m.x248 - 2*m.x221*m.x247
                          - 4.509770398884*m.b13 - 4.509770398884*m.b52 >= -4.509770398884)

m.c221 = Constraint(expr=m.x221**2 + m.x222**2 + m.x249**2 + m.x250**2 - 2*m.x221*m.x249 - 2*m.x222*m.x250
                          - 4.509770398884*m.b11 - 4.509770398884*m.b53 >= -4.509770398884)

m.c222 = Constraint(expr=m.x221**2 + m.x222**2 + m.x249**2 + m.x250**2 - 2*m.x221*m.x249 - 2*m.x222*m.x250
                          - 4.509770398884*m.b12 - 4.509770398884*m.b54 >= -4.509770398884)

m.c223 = Constraint(expr=m.x221**2 + m.x222**2 + m.x249**2 + m.x250**2 - 2*m.x221*m.x249 - 2*m.x222*m.x250
                          - 4.509770398884*m.b13 - 4.509770398884*m.b55 >= -4.509770398884)

m.c224 = Constraint(expr=m.x221**2 + m.x222**2 + m.x251**2 + m.x252**2 - 2*m.x222*m.x252 - 2*m.x221*m.x251
                          - 6.408451746064*m.b11 - 6.408451746064*m.b56 >= -6.408451746064)

m.c225 = Constraint(expr=m.x221**2 + m.x222**2 + m.x251**2 + m.x252**2 - 2*m.x222*m.x252 - 2*m.x221*m.x251
                          - 6.408451746064*m.b12 - 6.408451746064*m.b57 >= -6.408451746064)

m.c226 = Constraint(expr=m.x221**2 + m.x222**2 + m.x251**2 + m.x252**2 - 2*m.x222*m.x252 - 2*m.x221*m.x251
                          - 6.408451746064*m.b13 - 6.408451746064*m.b58 >= -6.408451746064)

m.c227 = Constraint(expr=m.x221**2 + m.x222**2 + m.x253**2 + m.x254**2 - 2*m.x221*m.x253 - 2*m.x222*m.x254
                          - 6.408451746064*m.b11 - 6.408451746064*m.b59 >= -6.408451746064)

m.c228 = Constraint(expr=m.x221**2 + m.x222**2 + m.x253**2 + m.x254**2 - 2*m.x221*m.x253 - 2*m.x222*m.x254
                          - 6.408451746064*m.b12 - 6.408451746064*m.b60 >= -6.408451746064)

m.c229 = Constraint(expr=m.x221**2 + m.x222**2 + m.x253**2 + m.x254**2 - 2*m.x221*m.x253 - 2*m.x222*m.x254
                          - 6.408451746064*m.b13 - 6.408451746064*m.b61 >= -6.408451746064)

m.c230 = Constraint(expr=m.x215**2 + m.x216**2 + m.x223**2 + m.x224**2 - 2*m.x216*m.x224 - 2*m.x215*m.x223
                          - 1.436939228176*m.b2 - 1.436939228176*m.b14 >= -1.436939228176)

m.c231 = Constraint(expr=m.x215**2 + m.x216**2 + m.x223**2 + m.x224**2 - 2*m.x216*m.x224 - 2*m.x215*m.x223
                          - 1.436939228176*m.b3 - 1.436939228176*m.b15 >= -1.436939228176)

m.c232 = Constraint(expr=m.x215**2 + m.x216**2 + m.x223**2 + m.x224**2 - 2*m.x216*m.x224 - 2*m.x215*m.x223
                          - 1.436939228176*m.b4 - 1.436939228176*m.b16 >= -1.436939228176)

m.c233 = Constraint(expr=m.x217**2 + m.x218**2 + m.x223**2 + m.x224**2 - 2*m.x217*m.x223 - 2*m.x218*m.x224
                          - 1.436939228176*m.b5 - 1.436939228176*m.b14 >= -1.436939228176)

m.c234 = Constraint(expr=m.x217**2 + m.x218**2 + m.x223**2 + m.x224**2 - 2*m.x217*m.x223 - 2*m.x218*m.x224
                          - 1.436939228176*m.b6 - 1.436939228176*m.b15 >= -1.436939228176)

m.c235 = Constraint(expr=m.x217**2 + m.x218**2 + m.x223**2 + m.x224**2 - 2*m.x217*m.x223 - 2*m.x218*m.x224
                          - 1.436939228176*m.b7 - 1.436939228176*m.b16 >= -1.436939228176)

m.c236 = Constraint(expr=m.x219**2 + m.x220**2 + m.x223**2 + m.x224**2 - 2*m.x220*m.x224 - 2*m.x219*m.x223
                          - 1.436939228176*m.b8 - 1.436939228176*m.b14 >= -1.436939228176)

m.c237 = Constraint(expr=m.x219**2 + m.x220**2 + m.x223**2 + m.x224**2 - 2*m.x220*m.x224 - 2*m.x219*m.x223
                          - 1.436939228176*m.b9 - 1.436939228176*m.b15 >= -1.436939228176)

m.c238 = Constraint(expr=m.x219**2 + m.x220**2 + m.x223**2 + m.x224**2 - 2*m.x220*m.x224 - 2*m.x219*m.x223
                          - 1.436939228176*m.b10 - 1.436939228176*m.b16 >= -1.436939228176)

m.c239 = Constraint(expr=m.x221**2 + m.x222**2 + m.x223**2 + m.x224**2 - 2*m.x221*m.x223 - 2*m.x222*m.x224
                          - 1.436939228176*m.b11 - 1.436939228176*m.b14 >= -1.436939228176)

m.c240 = Constraint(expr=m.x221**2 + m.x222**2 + m.x223**2 + m.x224**2 - 2*m.x221*m.x223 - 2*m.x222*m.x224
                          - 1.436939228176*m.b12 - 1.436939228176*m.b15 >= -1.436939228176)

m.c241 = Constraint(expr=m.x221**2 + m.x222**2 + m.x223**2 + m.x224**2 - 2*m.x221*m.x223 - 2*m.x222*m.x224
                          - 1.436939228176*m.b13 - 1.436939228176*m.b16 >= -1.436939228176)

m.c242 = Constraint(expr=m.x223**2 + m.x224**2 + m.x225**2 + m.x226**2 - 2*m.x223*m.x225 - 2*m.x224*m.x226
                          - 1.436939228176*m.b14 - 1.436939228176*m.b17 >= -1.436939228176)

m.c243 = Constraint(expr=m.x223**2 + m.x224**2 + m.x225**2 + m.x226**2 - 2*m.x223*m.x225 - 2*m.x224*m.x226
                          - 1.436939228176*m.b15 - 1.436939228176*m.b18 >= -1.436939228176)

m.c244 = Constraint(expr=m.x223**2 + m.x224**2 + m.x225**2 + m.x226**2 - 2*m.x223*m.x225 - 2*m.x224*m.x226
                          - 1.436939228176*m.b16 - 1.436939228176*m.b19 >= -1.436939228176)

m.c245 = Constraint(expr=m.x223**2 + m.x224**2 + m.x227**2 + m.x228**2 - 2*m.x223*m.x227 - 2*m.x224*m.x228
                          - 0.887203867225*m.b14 - 0.887203867225*m.b20 >= -0.887203867225)

m.c246 = Constraint(expr=m.x223**2 + m.x224**2 + m.x227**2 + m.x228**2 - 2*m.x223*m.x227 - 2*m.x224*m.x228
                          - 0.887203867225*m.b15 - 0.887203867225*m.b21 >= -0.887203867225)

m.c247 = Constraint(expr=m.x223**2 + m.x224**2 + m.x227**2 + m.x228**2 - 2*m.x223*m.x227 - 2*m.x224*m.x228
                          - 0.887203867225*m.b16 - 0.887203867225*m.b22 >= -0.887203867225)

m.c248 = Constraint(expr=m.x223**2 + m.x224**2 + m.x229**2 + m.x230**2 - 2*m.x223*m.x229 - 2*m.x224*m.x230
                          - 0.887203867225*m.b14 - 0.887203867225*m.b23 >= -0.887203867225)

m.c249 = Constraint(expr=m.x223**2 + m.x224**2 + m.x229**2 + m.x230**2 - 2*m.x223*m.x229 - 2*m.x224*m.x230
                          - 0.887203867225*m.b15 - 0.887203867225*m.b24 >= -0.887203867225)

m.c250 = Constraint(expr=m.x223**2 + m.x224**2 + m.x229**2 + m.x230**2 - 2*m.x223*m.x229 - 2*m.x224*m.x230
                          - 0.887203867225*m.b16 - 0.887203867225*m.b25 >= -0.887203867225)

m.c251 = Constraint(expr=m.x223**2 + m.x224**2 + m.x231**2 + m.x232**2 - 2*m.x223*m.x231 - 2*m.x224*m.x232
                          - 0.887203867225*m.b14 - 0.887203867225*m.b26 >= -0.887203867225)

m.c252 = Constraint(expr=m.x223**2 + m.x224**2 + m.x231**2 + m.x232**2 - 2*m.x223*m.x231 - 2*m.x224*m.x232
                          - 0.887203867225*m.b15 - 0.887203867225*m.b27 >= -0.887203867225)

m.c253 = Constraint(expr=m.x223**2 + m.x224**2 + m.x231**2 + m.x232**2 - 2*m.x223*m.x231 - 2*m.x224*m.x232
                          - 0.887203867225*m.b16 - 0.887203867225*m.b28 >= -0.887203867225)

m.c254 = Constraint(expr=m.x223**2 + m.x224**2 + m.x233**2 + m.x234**2 - 2*m.x223*m.x233 - 2*m.x224*m.x234
                          - 0.887203867225*m.b14 - 0.887203867225*m.b29 >= -0.887203867225)

m.c255 = Constraint(expr=m.x223**2 + m.x224**2 + m.x233**2 + m.x234**2 - 2*m.x223*m.x233 - 2*m.x224*m.x234
                          - 0.887203867225*m.b15 - 0.887203867225*m.b30 >= -0.887203867225)

m.c256 = Constraint(expr=m.x223**2 + m.x224**2 + m.x233**2 + m.x234**2 - 2*m.x223*m.x233 - 2*m.x224*m.x234
                          - 0.887203867225*m.b16 - 0.887203867225*m.b31 >= -0.887203867225)

m.c257 = Constraint(expr=m.x223**2 + m.x224**2 + m.x235**2 + m.x236**2 - 2*m.x223*m.x235 - 2*m.x224*m.x236
                          - 0.887203867225*m.b14 - 0.887203867225*m.b32 >= -0.887203867225)

m.c258 = Constraint(expr=m.x223**2 + m.x224**2 + m.x235**2 + m.x236**2 - 2*m.x223*m.x235 - 2*m.x224*m.x236
                          - 0.887203867225*m.b15 - 0.887203867225*m.b33 >= -0.887203867225)

m.c259 = Constraint(expr=m.x223**2 + m.x224**2 + m.x235**2 + m.x236**2 - 2*m.x223*m.x235 - 2*m.x224*m.x236
                          - 0.887203867225*m.b16 - 0.887203867225*m.b34 >= -0.887203867225)

m.c260 = Constraint(expr=m.x223**2 + m.x224**2 + m.x237**2 + m.x238**2 - 2*m.x223*m.x237 - 2*m.x224*m.x238
                          - 2.118573403024*m.b14 - 2.118573403024*m.b35 >= -2.118573403024)

m.c261 = Constraint(expr=m.x223**2 + m.x224**2 + m.x237**2 + m.x238**2 - 2*m.x223*m.x237 - 2*m.x224*m.x238
                          - 2.118573403024*m.b15 - 2.118573403024*m.b36 >= -2.118573403024)

m.c262 = Constraint(expr=m.x223**2 + m.x224**2 + m.x237**2 + m.x238**2 - 2*m.x223*m.x237 - 2*m.x224*m.x238
                          - 2.118573403024*m.b16 - 2.118573403024*m.b37 >= -2.118573403024)

m.c263 = Constraint(expr=m.x223**2 + m.x224**2 + m.x239**2 + m.x240**2 - 2*m.x223*m.x239 - 2*m.x224*m.x240
                          - 2.118573403024*m.b14 - 2.118573403024*m.b38 >= -2.118573403024)

m.c264 = Constraint(expr=m.x223**2 + m.x224**2 + m.x239**2 + m.x240**2 - 2*m.x223*m.x239 - 2*m.x224*m.x240
                          - 2.118573403024*m.b15 - 2.118573403024*m.b39 >= -2.118573403024)

m.c265 = Constraint(expr=m.x223**2 + m.x224**2 + m.x239**2 + m.x240**2 - 2*m.x223*m.x239 - 2*m.x224*m.x240
                          - 2.118573403024*m.b16 - 2.118573403024*m.b40 >= -2.118573403024)

m.c266 = Constraint(expr=m.x223**2 + m.x224**2 + m.x241**2 + m.x242**2 - 2*m.x223*m.x241 - 2*m.x224*m.x242
                          - 2.118573403024*m.b14 - 2.118573403024*m.b41 >= -2.118573403024)

m.c267 = Constraint(expr=m.x223**2 + m.x224**2 + m.x241**2 + m.x242**2 - 2*m.x223*m.x241 - 2*m.x224*m.x242
                          - 2.118573403024*m.b15 - 2.118573403024*m.b42 >= -2.118573403024)

m.c268 = Constraint(expr=m.x223**2 + m.x224**2 + m.x241**2 + m.x242**2 - 2*m.x224*m.x242 - 2*m.x223*m.x241
                          - 2.118573403024*m.b16 - 2.118573403024*m.b43 >= -2.118573403024)

m.c269 = Constraint(expr=m.x223**2 + m.x224**2 + m.x243**2 + m.x244**2 - 2*m.x224*m.x244 - 2*m.x223*m.x243
                          - 2.118573403024*m.b14 - 2.118573403024*m.b44 >= -2.118573403024)

m.c270 = Constraint(expr=m.x223**2 + m.x224**2 + m.x243**2 + m.x244**2 - 2*m.x224*m.x244 - 2*m.x223*m.x243
                          - 2.118573403024*m.b15 - 2.118573403024*m.b45 >= -2.118573403024)

m.c271 = Constraint(expr=m.x223**2 + m.x224**2 + m.x243**2 + m.x244**2 - 2*m.x224*m.x244 - 2*m.x223*m.x243
                          - 2.118573403024*m.b16 - 2.118573403024*m.b46 >= -2.118573403024)

m.c272 = Constraint(expr=m.x223**2 + m.x224**2 + m.x245**2 + m.x246**2 - 2*m.x224*m.x246 - 2*m.x223*m.x245
                          - 2.118573403024*m.b14 - 2.118573403024*m.b47 >= -2.118573403024)

m.c273 = Constraint(expr=m.x223**2 + m.x224**2 + m.x245**2 + m.x246**2 - 2*m.x224*m.x246 - 2*m.x223*m.x245
                          - 2.118573403024*m.b15 - 2.118573403024*m.b48 >= -2.118573403024)

m.c274 = Constraint(expr=m.x223**2 + m.x224**2 + m.x245**2 + m.x246**2 - 2*m.x224*m.x246 - 2*m.x223*m.x245
                          - 2.118573403024*m.b16 - 2.118573403024*m.b49 >= -2.118573403024)

m.c275 = Constraint(expr=m.x223**2 + m.x224**2 + m.x247**2 + m.x248**2 - 2*m.x223*m.x247 - 2*m.x224*m.x248
                          - 4.509770398884*m.b14 - 4.509770398884*m.b50 >= -4.509770398884)

m.c276 = Constraint(expr=m.x223**2 + m.x224**2 + m.x247**2 + m.x248**2 - 2*m.x223*m.x247 - 2*m.x224*m.x248
                          - 4.509770398884*m.b15 - 4.509770398884*m.b51 >= -4.509770398884)

m.c277 = Constraint(expr=m.x223**2 + m.x224**2 + m.x247**2 + m.x248**2 - 2*m.x223*m.x247 - 2*m.x224*m.x248
                          - 4.509770398884*m.b16 - 4.509770398884*m.b52 >= -4.509770398884)

m.c278 = Constraint(expr=m.x223**2 + m.x224**2 + m.x249**2 + m.x250**2 - 2*m.x224*m.x250 - 2*m.x223*m.x249
                          - 4.509770398884*m.b14 - 4.509770398884*m.b53 >= -4.509770398884)

m.c279 = Constraint(expr=m.x223**2 + m.x224**2 + m.x249**2 + m.x250**2 - 2*m.x224*m.x250 - 2*m.x223*m.x249
                          - 4.509770398884*m.b15 - 4.509770398884*m.b54 >= -4.509770398884)

m.c280 = Constraint(expr=m.x223**2 + m.x224**2 + m.x249**2 + m.x250**2 - 2*m.x224*m.x250 - 2*m.x223*m.x249
                          - 4.509770398884*m.b16 - 4.509770398884*m.b55 >= -4.509770398884)

m.c281 = Constraint(expr=m.x223**2 + m.x224**2 + m.x251**2 + m.x252**2 - 2*m.x223*m.x251 - 2*m.x224*m.x252
                          - 6.408451746064*m.b14 - 6.408451746064*m.b56 >= -6.408451746064)

m.c282 = Constraint(expr=m.x223**2 + m.x224**2 + m.x251**2 + m.x252**2 - 2*m.x223*m.x251 - 2*m.x224*m.x252
                          - 6.408451746064*m.b15 - 6.408451746064*m.b57 >= -6.408451746064)

m.c283 = Constraint(expr=m.x223**2 + m.x224**2 + m.x251**2 + m.x252**2 - 2*m.x223*m.x251 - 2*m.x224*m.x252
                          - 6.408451746064*m.b16 - 6.408451746064*m.b58 >= -6.408451746064)

m.c284 = Constraint(expr=m.x223**2 + m.x224**2 + m.x253**2 + m.x254**2 - 2*m.x224*m.x254 - 2*m.x223*m.x253
                          - 6.408451746064*m.b14 - 6.408451746064*m.b59 >= -6.408451746064)

m.c285 = Constraint(expr=m.x223**2 + m.x224**2 + m.x253**2 + m.x254**2 - 2*m.x224*m.x254 - 2*m.x223*m.x253
                          - 6.408451746064*m.b15 - 6.408451746064*m.b60 >= -6.408451746064)

m.c286 = Constraint(expr=m.x223**2 + m.x224**2 + m.x253**2 + m.x254**2 - 2*m.x224*m.x254 - 2*m.x223*m.x253
                          - 6.408451746064*m.b16 - 6.408451746064*m.b61 >= -6.408451746064)

m.c287 = Constraint(expr=m.x215**2 + m.x216**2 + m.x225**2 + m.x226**2 - 2*m.x215*m.x225 - 2*m.x216*m.x226
                          - 1.436939228176*m.b2 - 1.436939228176*m.b17 >= -1.436939228176)

m.c288 = Constraint(expr=m.x215**2 + m.x216**2 + m.x225**2 + m.x226**2 - 2*m.x215*m.x225 - 2*m.x216*m.x226
                          - 1.436939228176*m.b3 - 1.436939228176*m.b18 >= -1.436939228176)

m.c289 = Constraint(expr=m.x215**2 + m.x216**2 + m.x225**2 + m.x226**2 - 2*m.x215*m.x225 - 2*m.x216*m.x226
                          - 1.436939228176*m.b4 - 1.436939228176*m.b19 >= -1.436939228176)

m.c290 = Constraint(expr=m.x217**2 + m.x218**2 + m.x225**2 + m.x226**2 - 2*m.x218*m.x226 - 2*m.x217*m.x225
                          - 1.436939228176*m.b5 - 1.436939228176*m.b17 >= -1.436939228176)

m.c291 = Constraint(expr=m.x217**2 + m.x218**2 + m.x225**2 + m.x226**2 - 2*m.x218*m.x226 - 2*m.x217*m.x225
                          - 1.436939228176*m.b6 - 1.436939228176*m.b18 >= -1.436939228176)

m.c292 = Constraint(expr=m.x217**2 + m.x218**2 + m.x225**2 + m.x226**2 - 2*m.x218*m.x226 - 2*m.x217*m.x225
                          - 1.436939228176*m.b7 - 1.436939228176*m.b19 >= -1.436939228176)

m.c293 = Constraint(expr=m.x219**2 + m.x220**2 + m.x225**2 + m.x226**2 - 2*m.x220*m.x226 - 2*m.x219*m.x225
                          - 1.436939228176*m.b8 - 1.436939228176*m.b17 >= -1.436939228176)

m.c294 = Constraint(expr=m.x219**2 + m.x220**2 + m.x225**2 + m.x226**2 - 2*m.x220*m.x226 - 2*m.x219*m.x225
                          - 1.436939228176*m.b9 - 1.436939228176*m.b18 >= -1.436939228176)

m.c295 = Constraint(expr=m.x219**2 + m.x220**2 + m.x225**2 + m.x226**2 - 2*m.x220*m.x226 - 2*m.x219*m.x225
                          - 1.436939228176*m.b10 - 1.436939228176*m.b19 >= -1.436939228176)

m.c296 = Constraint(expr=m.x221**2 + m.x222**2 + m.x225**2 + m.x226**2 - 2*m.x221*m.x225 - 2*m.x222*m.x226
                          - 1.436939228176*m.b11 - 1.436939228176*m.b17 >= -1.436939228176)

m.c297 = Constraint(expr=m.x221**2 + m.x222**2 + m.x225**2 + m.x226**2 - 2*m.x221*m.x225 - 2*m.x222*m.x226
                          - 1.436939228176*m.b12 - 1.436939228176*m.b18 >= -1.436939228176)

m.c298 = Constraint(expr=m.x221**2 + m.x222**2 + m.x225**2 + m.x226**2 - 2*m.x221*m.x225 - 2*m.x222*m.x226
                          - 1.436939228176*m.b13 - 1.436939228176*m.b19 >= -1.436939228176)

m.c299 = Constraint(expr=m.x223**2 + m.x224**2 + m.x225**2 + m.x226**2 - 2*m.x223*m.x225 - 2*m.x224*m.x226
                          - 1.436939228176*m.b14 - 1.436939228176*m.b17 >= -1.436939228176)

m.c300 = Constraint(expr=m.x223**2 + m.x224**2 + m.x225**2 + m.x226**2 - 2*m.x223*m.x225 - 2*m.x224*m.x226
                          - 1.436939228176*m.b15 - 1.436939228176*m.b18 >= -1.436939228176)

m.c301 = Constraint(expr=m.x223**2 + m.x224**2 + m.x225**2 + m.x226**2 - 2*m.x223*m.x225 - 2*m.x224*m.x226
                          - 1.436939228176*m.b16 - 1.436939228176*m.b19 >= -1.436939228176)

m.c302 = Constraint(expr=m.x225**2 + m.x226**2 + m.x227**2 + m.x228**2 - 2*m.x225*m.x227 - 2*m.x226*m.x228
                          - 0.887203867225*m.b17 - 0.887203867225*m.b20 >= -0.887203867225)

m.c303 = Constraint(expr=m.x225**2 + m.x226**2 + m.x227**2 + m.x228**2 - 2*m.x225*m.x227 - 2*m.x226*m.x228
                          - 0.887203867225*m.b18 - 0.887203867225*m.b21 >= -0.887203867225)

m.c304 = Constraint(expr=m.x225**2 + m.x226**2 + m.x227**2 + m.x228**2 - 2*m.x225*m.x227 - 2*m.x226*m.x228
                          - 0.887203867225*m.b19 - 0.887203867225*m.b22 >= -0.887203867225)

m.c305 = Constraint(expr=m.x225**2 + m.x226**2 + m.x229**2 + m.x230**2 - 2*m.x225*m.x229 - 2*m.x226*m.x230
                          - 0.887203867225*m.b17 - 0.887203867225*m.b23 >= -0.887203867225)

m.c306 = Constraint(expr=m.x225**2 + m.x226**2 + m.x229**2 + m.x230**2 - 2*m.x225*m.x229 - 2*m.x226*m.x230
                          - 0.887203867225*m.b18 - 0.887203867225*m.b24 >= -0.887203867225)

m.c307 = Constraint(expr=m.x225**2 + m.x226**2 + m.x229**2 + m.x230**2 - 2*m.x225*m.x229 - 2*m.x226*m.x230
                          - 0.887203867225*m.b19 - 0.887203867225*m.b25 >= -0.887203867225)

m.c308 = Constraint(expr=m.x225**2 + m.x226**2 + m.x231**2 + m.x232**2 - 2*m.x225*m.x231 - 2*m.x226*m.x232
                          - 0.887203867225*m.b17 - 0.887203867225*m.b26 >= -0.887203867225)

m.c309 = Constraint(expr=m.x225**2 + m.x226**2 + m.x231**2 + m.x232**2 - 2*m.x225*m.x231 - 2*m.x226*m.x232
                          - 0.887203867225*m.b18 - 0.887203867225*m.b27 >= -0.887203867225)

m.c310 = Constraint(expr=m.x225**2 + m.x226**2 + m.x231**2 + m.x232**2 - 2*m.x225*m.x231 - 2*m.x226*m.x232
                          - 0.887203867225*m.b19 - 0.887203867225*m.b28 >= -0.887203867225)

m.c311 = Constraint(expr=m.x225**2 + m.x226**2 + m.x233**2 + m.x234**2 - 2*m.x225*m.x233 - 2*m.x226*m.x234
                          - 0.887203867225*m.b17 - 0.887203867225*m.b29 >= -0.887203867225)

m.c312 = Constraint(expr=m.x225**2 + m.x226**2 + m.x233**2 + m.x234**2 - 2*m.x225*m.x233 - 2*m.x226*m.x234
                          - 0.887203867225*m.b18 - 0.887203867225*m.b30 >= -0.887203867225)

m.c313 = Constraint(expr=m.x225**2 + m.x226**2 + m.x233**2 + m.x234**2 - 2*m.x225*m.x233 - 2*m.x226*m.x234
                          - 0.887203867225*m.b19 - 0.887203867225*m.b31 >= -0.887203867225)

m.c314 = Constraint(expr=m.x225**2 + m.x226**2 + m.x235**2 + m.x236**2 - 2*m.x225*m.x235 - 2*m.x226*m.x236
                          - 0.887203867225*m.b17 - 0.887203867225*m.b32 >= -0.887203867225)

m.c315 = Constraint(expr=m.x225**2 + m.x226**2 + m.x235**2 + m.x236**2 - 2*m.x225*m.x235 - 2*m.x226*m.x236
                          - 0.887203867225*m.b18 - 0.887203867225*m.b33 >= -0.887203867225)

m.c316 = Constraint(expr=m.x225**2 + m.x226**2 + m.x235**2 + m.x236**2 - 2*m.x225*m.x235 - 2*m.x226*m.x236
                          - 0.887203867225*m.b19 - 0.887203867225*m.b34 >= -0.887203867225)

m.c317 = Constraint(expr=m.x225**2 + m.x226**2 + m.x237**2 + m.x238**2 - 2*m.x225*m.x237 - 2*m.x226*m.x238
                          - 2.118573403024*m.b17 - 2.118573403024*m.b35 >= -2.118573403024)

m.c318 = Constraint(expr=m.x225**2 + m.x226**2 + m.x237**2 + m.x238**2 - 2*m.x225*m.x237 - 2*m.x226*m.x238
                          - 2.118573403024*m.b18 - 2.118573403024*m.b36 >= -2.118573403024)

m.c319 = Constraint(expr=m.x225**2 + m.x226**2 + m.x237**2 + m.x238**2 - 2*m.x225*m.x237 - 2*m.x226*m.x238
                          - 2.118573403024*m.b19 - 2.118573403024*m.b37 >= -2.118573403024)

m.c320 = Constraint(expr=m.x225**2 + m.x226**2 + m.x239**2 + m.x240**2 - 2*m.x225*m.x239 - 2*m.x226*m.x240
                          - 2.118573403024*m.b17 - 2.118573403024*m.b38 >= -2.118573403024)

m.c321 = Constraint(expr=m.x225**2 + m.x226**2 + m.x239**2 + m.x240**2 - 2*m.x225*m.x239 - 2*m.x226*m.x240
                          - 2.118573403024*m.b18 - 2.118573403024*m.b39 >= -2.118573403024)

m.c322 = Constraint(expr=m.x225**2 + m.x226**2 + m.x239**2 + m.x240**2 - 2*m.x225*m.x239 - 2*m.x226*m.x240
                          - 2.118573403024*m.b19 - 2.118573403024*m.b40 >= -2.118573403024)

m.c323 = Constraint(expr=m.x225**2 + m.x226**2 + m.x241**2 + m.x242**2 - 2*m.x226*m.x242 - 2*m.x225*m.x241
                          - 2.118573403024*m.b17 - 2.118573403024*m.b41 >= -2.118573403024)

m.c324 = Constraint(expr=m.x225**2 + m.x226**2 + m.x241**2 + m.x242**2 - 2*m.x226*m.x242 - 2*m.x225*m.x241
                          - 2.118573403024*m.b18 - 2.118573403024*m.b42 >= -2.118573403024)

m.c325 = Constraint(expr=m.x225**2 + m.x226**2 + m.x241**2 + m.x242**2 - 2*m.x226*m.x242 - 2*m.x225*m.x241
                          - 2.118573403024*m.b19 - 2.118573403024*m.b43 >= -2.118573403024)

m.c326 = Constraint(expr=m.x225**2 + m.x226**2 + m.x243**2 + m.x244**2 - 2*m.x226*m.x244 - 2*m.x225*m.x243
                          - 2.118573403024*m.b17 - 2.118573403024*m.b44 >= -2.118573403024)

m.c327 = Constraint(expr=m.x225**2 + m.x226**2 + m.x243**2 + m.x244**2 - 2*m.x226*m.x244 - 2*m.x225*m.x243
                          - 2.118573403024*m.b18 - 2.118573403024*m.b45 >= -2.118573403024)

m.c328 = Constraint(expr=m.x225**2 + m.x226**2 + m.x243**2 + m.x244**2 - 2*m.x226*m.x244 - 2*m.x225*m.x243
                          - 2.118573403024*m.b19 - 2.118573403024*m.b46 >= -2.118573403024)

m.c329 = Constraint(expr=m.x225**2 + m.x226**2 + m.x245**2 + m.x246**2 - 2*m.x225*m.x245 - 2*m.x226*m.x246
                          - 2.118573403024*m.b17 - 2.118573403024*m.b47 >= -2.118573403024)

m.c330 = Constraint(expr=m.x225**2 + m.x226**2 + m.x245**2 + m.x246**2 - 2*m.x225*m.x245 - 2*m.x226*m.x246
                          - 2.118573403024*m.b18 - 2.118573403024*m.b48 >= -2.118573403024)

m.c331 = Constraint(expr=m.x225**2 + m.x226**2 + m.x245**2 + m.x246**2 - 2*m.x225*m.x245 - 2*m.x226*m.x246
                          - 2.118573403024*m.b19 - 2.118573403024*m.b49 >= -2.118573403024)

m.c332 = Constraint(expr=m.x225**2 + m.x226**2 + m.x247**2 + m.x248**2 - 2*m.x226*m.x248 - 2*m.x225*m.x247
                          - 4.509770398884*m.b17 - 4.509770398884*m.b50 >= -4.509770398884)

m.c333 = Constraint(expr=m.x225**2 + m.x226**2 + m.x247**2 + m.x248**2 - 2*m.x226*m.x248 - 2*m.x225*m.x247
                          - 4.509770398884*m.b18 - 4.509770398884*m.b51 >= -4.509770398884)

m.c334 = Constraint(expr=m.x225**2 + m.x226**2 + m.x247**2 + m.x248**2 - 2*m.x225*m.x247 - 2*m.x226*m.x248
                          - 4.509770398884*m.b19 - 4.509770398884*m.b52 >= -4.509770398884)

m.c335 = Constraint(expr=m.x225**2 + m.x226**2 + m.x249**2 + m.x250**2 - 2*m.x225*m.x249 - 2*m.x226*m.x250
                          - 4.509770398884*m.b17 - 4.509770398884*m.b53 >= -4.509770398884)

m.c336 = Constraint(expr=m.x225**2 + m.x226**2 + m.x249**2 + m.x250**2 - 2*m.x225*m.x249 - 2*m.x226*m.x250
                          - 4.509770398884*m.b18 - 4.509770398884*m.b54 >= -4.509770398884)

m.c337 = Constraint(expr=m.x225**2 + m.x226**2 + m.x249**2 + m.x250**2 - 2*m.x225*m.x249 - 2*m.x226*m.x250
                          - 4.509770398884*m.b19 - 4.509770398884*m.b55 >= -4.509770398884)

m.c338 = Constraint(expr=m.x225**2 + m.x226**2 + m.x251**2 + m.x252**2 - 2*m.x226*m.x252 - 2*m.x225*m.x251
                          - 6.408451746064*m.b17 - 6.408451746064*m.b56 >= -6.408451746064)

m.c339 = Constraint(expr=m.x225**2 + m.x226**2 + m.x251**2 + m.x252**2 - 2*m.x226*m.x252 - 2*m.x225*m.x251
                          - 6.408451746064*m.b18 - 6.408451746064*m.b57 >= -6.408451746064)

m.c340 = Constraint(expr=m.x225**2 + m.x226**2 + m.x251**2 + m.x252**2 - 2*m.x226*m.x252 - 2*m.x225*m.x251
                          - 6.408451746064*m.b19 - 6.408451746064*m.b58 >= -6.408451746064)

m.c341 = Constraint(expr=m.x225**2 + m.x226**2 + m.x253**2 + m.x254**2 - 2*m.x226*m.x254 - 2*m.x225*m.x253
                          - 6.408451746064*m.b17 - 6.408451746064*m.b59 >= -6.408451746064)

m.c342 = Constraint(expr=m.x225**2 + m.x226**2 + m.x253**2 + m.x254**2 - 2*m.x226*m.x254 - 2*m.x225*m.x253
                          - 6.408451746064*m.b18 - 6.408451746064*m.b60 >= -6.408451746064)

m.c343 = Constraint(expr=m.x225**2 + m.x226**2 + m.x253**2 + m.x254**2 - 2*m.x226*m.x254 - 2*m.x225*m.x253
                          - 6.408451746064*m.b19 - 6.408451746064*m.b61 >= -6.408451746064)

m.c344 = Constraint(expr=m.x215**2 + m.x216**2 + m.x227**2 + m.x228**2 - 2*m.x216*m.x228 - 2*m.x215*m.x227
                          - 0.887203867225*m.b2 - 0.887203867225*m.b20 >= -0.887203867225)

m.c345 = Constraint(expr=m.x215**2 + m.x216**2 + m.x227**2 + m.x228**2 - 2*m.x216*m.x228 - 2*m.x215*m.x227
                          - 0.887203867225*m.b3 - 0.887203867225*m.b21 >= -0.887203867225)

m.c346 = Constraint(expr=m.x215**2 + m.x216**2 + m.x227**2 + m.x228**2 - 2*m.x216*m.x228 - 2*m.x215*m.x227
                          - 0.887203867225*m.b4 - 0.887203867225*m.b22 >= -0.887203867225)

m.c347 = Constraint(expr=m.x217**2 + m.x218**2 + m.x227**2 + m.x228**2 - 2*m.x217*m.x227 - 2*m.x218*m.x228
                          - 0.887203867225*m.b5 - 0.887203867225*m.b20 >= -0.887203867225)

m.c348 = Constraint(expr=m.x217**2 + m.x218**2 + m.x227**2 + m.x228**2 - 2*m.x217*m.x227 - 2*m.x218*m.x228
                          - 0.887203867225*m.b6 - 0.887203867225*m.b21 >= -0.887203867225)

m.c349 = Constraint(expr=m.x217**2 + m.x218**2 + m.x227**2 + m.x228**2 - 2*m.x217*m.x227 - 2*m.x218*m.x228
                          - 0.887203867225*m.b7 - 0.887203867225*m.b22 >= -0.887203867225)

m.c350 = Constraint(expr=m.x219**2 + m.x220**2 + m.x227**2 + m.x228**2 - 2*m.x220*m.x228 - 2*m.x219*m.x227
                          - 0.887203867225*m.b8 - 0.887203867225*m.b20 >= -0.887203867225)

m.c351 = Constraint(expr=m.x219**2 + m.x220**2 + m.x227**2 + m.x228**2 - 2*m.x220*m.x228 - 2*m.x219*m.x227
                          - 0.887203867225*m.b9 - 0.887203867225*m.b21 >= -0.887203867225)

m.c352 = Constraint(expr=m.x219**2 + m.x220**2 + m.x227**2 + m.x228**2 - 2*m.x220*m.x228 - 2*m.x219*m.x227
                          - 0.887203867225*m.b10 - 0.887203867225*m.b22 >= -0.887203867225)

m.c353 = Constraint(expr=m.x221**2 + m.x222**2 + m.x227**2 + m.x228**2 - 2*m.x221*m.x227 - 2*m.x222*m.x228
                          - 0.887203867225*m.b11 - 0.887203867225*m.b20 >= -0.887203867225)

m.c354 = Constraint(expr=m.x221**2 + m.x222**2 + m.x227**2 + m.x228**2 - 2*m.x221*m.x227 - 2*m.x222*m.x228
                          - 0.887203867225*m.b12 - 0.887203867225*m.b21 >= -0.887203867225)

m.c355 = Constraint(expr=m.x221**2 + m.x222**2 + m.x227**2 + m.x228**2 - 2*m.x221*m.x227 - 2*m.x222*m.x228
                          - 0.887203867225*m.b13 - 0.887203867225*m.b22 >= -0.887203867225)

m.c356 = Constraint(expr=m.x223**2 + m.x224**2 + m.x227**2 + m.x228**2 - 2*m.x223*m.x227 - 2*m.x224*m.x228
                          - 0.887203867225*m.b14 - 0.887203867225*m.b20 >= -0.887203867225)

m.c357 = Constraint(expr=m.x223**2 + m.x224**2 + m.x227**2 + m.x228**2 - 2*m.x223*m.x227 - 2*m.x224*m.x228
                          - 0.887203867225*m.b15 - 0.887203867225*m.b21 >= -0.887203867225)

m.c358 = Constraint(expr=m.x223**2 + m.x224**2 + m.x227**2 + m.x228**2 - 2*m.x223*m.x227 - 2*m.x224*m.x228
                          - 0.887203867225*m.b16 - 0.887203867225*m.b22 >= -0.887203867225)

m.c359 = Constraint(expr=m.x225**2 + m.x226**2 + m.x227**2 + m.x228**2 - 2*m.x225*m.x227 - 2*m.x226*m.x228
                          - 0.887203867225*m.b17 - 0.887203867225*m.b20 >= -0.887203867225)

m.c360 = Constraint(expr=m.x225**2 + m.x226**2 + m.x227**2 + m.x228**2 - 2*m.x225*m.x227 - 2*m.x226*m.x228
                          - 0.887203867225*m.b18 - 0.887203867225*m.b21 >= -0.887203867225)

m.c361 = Constraint(expr=m.x225**2 + m.x226**2 + m.x227**2 + m.x228**2 - 2*m.x225*m.x227 - 2*m.x226*m.x228
                          - 0.887203867225*m.b19 - 0.887203867225*m.b22 >= -0.887203867225)

m.c362 = Constraint(expr=m.x227**2 + m.x228**2 + m.x229**2 + m.x230**2 - 2*m.x227*m.x229 - 2*m.x228*m.x230
                          - 0.469370231236*m.b20 - 0.469370231236*m.b23 >= -0.469370231236)

m.c363 = Constraint(expr=m.x227**2 + m.x228**2 + m.x229**2 + m.x230**2 - 2*m.x227*m.x229 - 2*m.x228*m.x230
                          - 0.469370231236*m.b21 - 0.469370231236*m.b24 >= -0.469370231236)

m.c364 = Constraint(expr=m.x227**2 + m.x228**2 + m.x229**2 + m.x230**2 - 2*m.x227*m.x229 - 2*m.x228*m.x230
                          - 0.469370231236*m.b22 - 0.469370231236*m.b25 >= -0.469370231236)

m.c365 = Constraint(expr=m.x227**2 + m.x228**2 + m.x231**2 + m.x232**2 - 2*m.x227*m.x231 - 2*m.x228*m.x232
                          - 0.469370231236*m.b20 - 0.469370231236*m.b26 >= -0.469370231236)

m.c366 = Constraint(expr=m.x227**2 + m.x228**2 + m.x231**2 + m.x232**2 - 2*m.x227*m.x231 - 2*m.x228*m.x232
                          - 0.469370231236*m.b21 - 0.469370231236*m.b27 >= -0.469370231236)

m.c367 = Constraint(expr=m.x227**2 + m.x228**2 + m.x231**2 + m.x232**2 - 2*m.x227*m.x231 - 2*m.x228*m.x232
                          - 0.469370231236*m.b22 - 0.469370231236*m.b28 >= -0.469370231236)

m.c368 = Constraint(expr=m.x227**2 + m.x228**2 + m.x233**2 + m.x234**2 - 2*m.x227*m.x233 - 2*m.x228*m.x234
                          - 0.469370231236*m.b20 - 0.469370231236*m.b29 >= -0.469370231236)

m.c369 = Constraint(expr=m.x227**2 + m.x228**2 + m.x233**2 + m.x234**2 - 2*m.x227*m.x233 - 2*m.x228*m.x234
                          - 0.469370231236*m.b21 - 0.469370231236*m.b30 >= -0.469370231236)

m.c370 = Constraint(expr=m.x227**2 + m.x228**2 + m.x233**2 + m.x234**2 - 2*m.x227*m.x233 - 2*m.x228*m.x234
                          - 0.469370231236*m.b22 - 0.469370231236*m.b31 >= -0.469370231236)

m.c371 = Constraint(expr=m.x227**2 + m.x228**2 + m.x235**2 + m.x236**2 - 2*m.x227*m.x235 - 2*m.x228*m.x236
                          - 0.469370231236*m.b20 - 0.469370231236*m.b32 >= -0.469370231236)

m.c372 = Constraint(expr=m.x227**2 + m.x228**2 + m.x235**2 + m.x236**2 - 2*m.x227*m.x235 - 2*m.x228*m.x236
                          - 0.469370231236*m.b21 - 0.469370231236*m.b33 >= -0.469370231236)

m.c373 = Constraint(expr=m.x227**2 + m.x228**2 + m.x235**2 + m.x236**2 - 2*m.x227*m.x235 - 2*m.x228*m.x236
                          - 0.469370231236*m.b22 - 0.469370231236*m.b34 >= -0.469370231236)

m.c374 = Constraint(expr=m.x227**2 + m.x228**2 + m.x237**2 + m.x238**2 - 2*m.x227*m.x237 - 2*m.x228*m.x238
                          - 1.436936830729*m.b20 - 1.436936830729*m.b35 >= -1.436936830729)

m.c375 = Constraint(expr=m.x227**2 + m.x228**2 + m.x237**2 + m.x238**2 - 2*m.x227*m.x237 - 2*m.x228*m.x238
                          - 1.436936830729*m.b21 - 1.436936830729*m.b36 >= -1.436936830729)

m.c376 = Constraint(expr=m.x227**2 + m.x228**2 + m.x237**2 + m.x238**2 - 2*m.x227*m.x237 - 2*m.x228*m.x238
                          - 1.436936830729*m.b22 - 1.436936830729*m.b37 >= -1.436936830729)

m.c377 = Constraint(expr=m.x227**2 + m.x228**2 + m.x239**2 + m.x240**2 - 2*m.x227*m.x239 - 2*m.x228*m.x240
                          - 1.436936830729*m.b20 - 1.436936830729*m.b38 >= -1.436936830729)

m.c378 = Constraint(expr=m.x227**2 + m.x228**2 + m.x239**2 + m.x240**2 - 2*m.x227*m.x239 - 2*m.x228*m.x240
                          - 1.436936830729*m.b21 - 1.436936830729*m.b39 >= -1.436936830729)

m.c379 = Constraint(expr=m.x227**2 + m.x228**2 + m.x239**2 + m.x240**2 - 2*m.x227*m.x239 - 2*m.x228*m.x240
                          - 1.436936830729*m.b22 - 1.436936830729*m.b40 >= -1.436936830729)

m.c380 = Constraint(expr=m.x227**2 + m.x228**2 + m.x241**2 + m.x242**2 - 2*m.x227*m.x241 - 2*m.x228*m.x242
                          - 1.436936830729*m.b20 - 1.436936830729*m.b41 >= -1.436936830729)

m.c381 = Constraint(expr=m.x227**2 + m.x228**2 + m.x241**2 + m.x242**2 - 2*m.x227*m.x241 - 2*m.x228*m.x242
                          - 1.436936830729*m.b21 - 1.436936830729*m.b42 >= -1.436936830729)

m.c382 = Constraint(expr=m.x227**2 + m.x228**2 + m.x241**2 + m.x242**2 - 2*m.x227*m.x241 - 2*m.x228*m.x242
                          - 1.436936830729*m.b22 - 1.436936830729*m.b43 >= -1.436936830729)

m.c383 = Constraint(expr=m.x227**2 + m.x228**2 + m.x243**2 + m.x244**2 - 2*m.x228*m.x244 - 2*m.x227*m.x243
                          - 1.436936830729*m.b20 - 1.436936830729*m.b44 >= -1.436936830729)

m.c384 = Constraint(expr=m.x227**2 + m.x228**2 + m.x243**2 + m.x244**2 - 2*m.x228*m.x244 - 2*m.x227*m.x243
                          - 1.436936830729*m.b21 - 1.436936830729*m.b45 >= -1.436936830729)

m.c385 = Constraint(expr=m.x227**2 + m.x228**2 + m.x243**2 + m.x244**2 - 2*m.x228*m.x244 - 2*m.x227*m.x243
                          - 1.436936830729*m.b22 - 1.436936830729*m.b46 >= -1.436936830729)

m.c386 = Constraint(expr=m.x227**2 + m.x228**2 + m.x245**2 + m.x246**2 - 2*m.x228*m.x246 - 2*m.x227*m.x245
                          - 1.436936830729*m.b20 - 1.436936830729*m.b47 >= -1.436936830729)

m.c387 = Constraint(expr=m.x227**2 + m.x228**2 + m.x245**2 + m.x246**2 - 2*m.x228*m.x246 - 2*m.x227*m.x245
                          - 1.436936830729*m.b21 - 1.436936830729*m.b48 >= -1.436936830729)

m.c388 = Constraint(expr=m.x227**2 + m.x228**2 + m.x245**2 + m.x246**2 - 2*m.x228*m.x246 - 2*m.x227*m.x245
                          - 1.436936830729*m.b22 - 1.436936830729*m.b49 >= -1.436936830729)

m.c389 = Constraint(expr=m.x227**2 + m.x228**2 + m.x247**2 + m.x248**2 - 2*m.x227*m.x247 - 2*m.x228*m.x248
                          - 3.484990776969*m.b20 - 3.484990776969*m.b50 >= -3.484990776969)

m.c390 = Constraint(expr=m.x227**2 + m.x228**2 + m.x247**2 + m.x248**2 - 2*m.x227*m.x247 - 2*m.x228*m.x248
                          - 3.484990776969*m.b21 - 3.484990776969*m.b51 >= -3.484990776969)

m.c391 = Constraint(expr=m.x227**2 + m.x228**2 + m.x247**2 + m.x248**2 - 2*m.x227*m.x247 - 2*m.x228*m.x248
                          - 3.484990776969*m.b22 - 3.484990776969*m.b52 >= -3.484990776969)

m.c392 = Constraint(expr=m.x227**2 + m.x228**2 + m.x249**2 + m.x250**2 - 2*m.x228*m.x250 - 2*m.x227*m.x249
                          - 3.484990776969*m.b20 - 3.484990776969*m.b53 >= -3.484990776969)

m.c393 = Constraint(expr=m.x227**2 + m.x228**2 + m.x249**2 + m.x250**2 - 2*m.x228*m.x250 - 2*m.x227*m.x249
                          - 3.484990776969*m.b21 - 3.484990776969*m.b54 >= -3.484990776969)

m.c394 = Constraint(expr=m.x227**2 + m.x228**2 + m.x249**2 + m.x250**2 - 2*m.x228*m.x250 - 2*m.x227*m.x249
                          - 3.484990776969*m.b22 - 3.484990776969*m.b55 >= -3.484990776969)

m.c395 = Constraint(expr=m.x227**2 + m.x228**2 + m.x251**2 + m.x252**2 - 2*m.x227*m.x251 - 2*m.x228*m.x252
                          - 5.174182750489*m.b20 - 5.174182750489*m.b56 >= -5.174182750489)

m.c396 = Constraint(expr=m.x227**2 + m.x228**2 + m.x251**2 + m.x252**2 - 2*m.x227*m.x251 - 2*m.x228*m.x252
                          - 5.174182750489*m.b21 - 5.174182750489*m.b57 >= -5.174182750489)

m.c397 = Constraint(expr=m.x227**2 + m.x228**2 + m.x251**2 + m.x252**2 - 2*m.x227*m.x251 - 2*m.x228*m.x252
                          - 5.174182750489*m.b22 - 5.174182750489*m.b58 >= -5.174182750489)

m.c398 = Constraint(expr=m.x227**2 + m.x228**2 + m.x253**2 + m.x254**2 - 2*m.x228*m.x254 - 2*m.x227*m.x253
                          - 5.174182750489*m.b20 - 5.174182750489*m.b59 >= -5.174182750489)

m.c399 = Constraint(expr=m.x227**2 + m.x228**2 + m.x253**2 + m.x254**2 - 2*m.x228*m.x254 - 2*m.x227*m.x253
                          - 5.174182750489*m.b21 - 5.174182750489*m.b60 >= -5.174182750489)

m.c400 = Constraint(expr=m.x227**2 + m.x228**2 + m.x253**2 + m.x254**2 - 2*m.x228*m.x254 - 2*m.x227*m.x253
                          - 5.174182750489*m.b22 - 5.174182750489*m.b61 >= -5.174182750489)

m.c401 = Constraint(expr=m.x215**2 + m.x216**2 + m.x229**2 + m.x230**2 - 2*m.x215*m.x229 - 2*m.x216*m.x230
                          - 0.887203867225*m.b2 - 0.887203867225*m.b23 >= -0.887203867225)

m.c402 = Constraint(expr=m.x215**2 + m.x216**2 + m.x229**2 + m.x230**2 - 2*m.x215*m.x229 - 2*m.x216*m.x230
                          - 0.887203867225*m.b3 - 0.887203867225*m.b24 >= -0.887203867225)

m.c403 = Constraint(expr=m.x215**2 + m.x216**2 + m.x229**2 + m.x230**2 - 2*m.x215*m.x229 - 2*m.x216*m.x230
                          - 0.887203867225*m.b4 - 0.887203867225*m.b25 >= -0.887203867225)

m.c404 = Constraint(expr=m.x217**2 + m.x218**2 + m.x229**2 + m.x230**2 - 2*m.x218*m.x230 - 2*m.x217*m.x229
                          - 0.887203867225*m.b5 - 0.887203867225*m.b23 >= -0.887203867225)

m.c405 = Constraint(expr=m.x217**2 + m.x218**2 + m.x229**2 + m.x230**2 - 2*m.x218*m.x230 - 2*m.x217*m.x229
                          - 0.887203867225*m.b6 - 0.887203867225*m.b24 >= -0.887203867225)

m.c406 = Constraint(expr=m.x217**2 + m.x218**2 + m.x229**2 + m.x230**2 - 2*m.x218*m.x230 - 2*m.x217*m.x229
                          - 0.887203867225*m.b7 - 0.887203867225*m.b25 >= -0.887203867225)

m.c407 = Constraint(expr=m.x219**2 + m.x220**2 + m.x229**2 + m.x230**2 - 2*m.x220*m.x230 - 2*m.x219*m.x229
                          - 0.887203867225*m.b8 - 0.887203867225*m.b23 >= -0.887203867225)

m.c408 = Constraint(expr=m.x219**2 + m.x220**2 + m.x229**2 + m.x230**2 - 2*m.x220*m.x230 - 2*m.x219*m.x229
                          - 0.887203867225*m.b9 - 0.887203867225*m.b24 >= -0.887203867225)

m.c409 = Constraint(expr=m.x219**2 + m.x220**2 + m.x229**2 + m.x230**2 - 2*m.x220*m.x230 - 2*m.x219*m.x229
                          - 0.887203867225*m.b10 - 0.887203867225*m.b25 >= -0.887203867225)

m.c410 = Constraint(expr=m.x221**2 + m.x222**2 + m.x229**2 + m.x230**2 - 2*m.x221*m.x229 - 2*m.x222*m.x230
                          - 0.887203867225*m.b11 - 0.887203867225*m.b23 >= -0.887203867225)

m.c411 = Constraint(expr=m.x221**2 + m.x222**2 + m.x229**2 + m.x230**2 - 2*m.x221*m.x229 - 2*m.x222*m.x230
                          - 0.887203867225*m.b12 - 0.887203867225*m.b24 >= -0.887203867225)

m.c412 = Constraint(expr=m.x221**2 + m.x222**2 + m.x229**2 + m.x230**2 - 2*m.x221*m.x229 - 2*m.x222*m.x230
                          - 0.887203867225*m.b13 - 0.887203867225*m.b25 >= -0.887203867225)

m.c413 = Constraint(expr=m.x223**2 + m.x224**2 + m.x229**2 + m.x230**2 - 2*m.x223*m.x229 - 2*m.x224*m.x230
                          - 0.887203867225*m.b14 - 0.887203867225*m.b23 >= -0.887203867225)

m.c414 = Constraint(expr=m.x223**2 + m.x224**2 + m.x229**2 + m.x230**2 - 2*m.x223*m.x229 - 2*m.x224*m.x230
                          - 0.887203867225*m.b15 - 0.887203867225*m.b24 >= -0.887203867225)

m.c415 = Constraint(expr=m.x223**2 + m.x224**2 + m.x229**2 + m.x230**2 - 2*m.x223*m.x229 - 2*m.x224*m.x230
                          - 0.887203867225*m.b16 - 0.887203867225*m.b25 >= -0.887203867225)

m.c416 = Constraint(expr=m.x225**2 + m.x226**2 + m.x229**2 + m.x230**2 - 2*m.x225*m.x229 - 2*m.x226*m.x230
                          - 0.887203867225*m.b17 - 0.887203867225*m.b23 >= -0.887203867225)

m.c417 = Constraint(expr=m.x225**2 + m.x226**2 + m.x229**2 + m.x230**2 - 2*m.x225*m.x229 - 2*m.x226*m.x230
                          - 0.887203867225*m.b18 - 0.887203867225*m.b24 >= -0.887203867225)

m.c418 = Constraint(expr=m.x225**2 + m.x226**2 + m.x229**2 + m.x230**2 - 2*m.x225*m.x229 - 2*m.x226*m.x230
                          - 0.887203867225*m.b19 - 0.887203867225*m.b25 >= -0.887203867225)

m.c419 = Constraint(expr=m.x227**2 + m.x228**2 + m.x229**2 + m.x230**2 - 2*m.x227*m.x229 - 2*m.x228*m.x230
                          - 0.469370231236*m.b20 - 0.469370231236*m.b23 >= -0.469370231236)

m.c420 = Constraint(expr=m.x227**2 + m.x228**2 + m.x229**2 + m.x230**2 - 2*m.x227*m.x229 - 2*m.x228*m.x230
                          - 0.469370231236*m.b21 - 0.469370231236*m.b24 >= -0.469370231236)

m.c421 = Constraint(expr=m.x227**2 + m.x228**2 + m.x229**2 + m.x230**2 - 2*m.x227*m.x229 - 2*m.x228*m.x230
                          - 0.469370231236*m.b22 - 0.469370231236*m.b25 >= -0.469370231236)

m.c422 = Constraint(expr=m.x229**2 + m.x230**2 + m.x231**2 + m.x232**2 - 2*m.x229*m.x231 - 2*m.x230*m.x232
                          - 0.469370231236*m.b23 - 0.469370231236*m.b26 >= -0.469370231236)

m.c423 = Constraint(expr=m.x229**2 + m.x230**2 + m.x231**2 + m.x232**2 - 2*m.x229*m.x231 - 2*m.x230*m.x232
                          - 0.469370231236*m.b24 - 0.469370231236*m.b27 >= -0.469370231236)

m.c424 = Constraint(expr=m.x229**2 + m.x230**2 + m.x231**2 + m.x232**2 - 2*m.x229*m.x231 - 2*m.x230*m.x232
                          - 0.469370231236*m.b25 - 0.469370231236*m.b28 >= -0.469370231236)

m.c425 = Constraint(expr=m.x229**2 + m.x230**2 + m.x233**2 + m.x234**2 - 2*m.x229*m.x233 - 2*m.x230*m.x234
                          - 0.469370231236*m.b23 - 0.469370231236*m.b29 >= -0.469370231236)

m.c426 = Constraint(expr=m.x229**2 + m.x230**2 + m.x233**2 + m.x234**2 - 2*m.x229*m.x233 - 2*m.x230*m.x234
                          - 0.469370231236*m.b24 - 0.469370231236*m.b30 >= -0.469370231236)

m.c427 = Constraint(expr=m.x229**2 + m.x230**2 + m.x233**2 + m.x234**2 - 2*m.x229*m.x233 - 2*m.x230*m.x234
                          - 0.469370231236*m.b25 - 0.469370231236*m.b31 >= -0.469370231236)

m.c428 = Constraint(expr=m.x229**2 + m.x230**2 + m.x235**2 + m.x236**2 - 2*m.x229*m.x235 - 2*m.x230*m.x236
                          - 0.469370231236*m.b23 - 0.469370231236*m.b32 >= -0.469370231236)

m.c429 = Constraint(expr=m.x229**2 + m.x230**2 + m.x235**2 + m.x236**2 - 2*m.x229*m.x235 - 2*m.x230*m.x236
                          - 0.469370231236*m.b24 - 0.469370231236*m.b33 >= -0.469370231236)

m.c430 = Constraint(expr=m.x229**2 + m.x230**2 + m.x235**2 + m.x236**2 - 2*m.x229*m.x235 - 2*m.x230*m.x236
                          - 0.469370231236*m.b25 - 0.469370231236*m.b34 >= -0.469370231236)

m.c431 = Constraint(expr=m.x229**2 + m.x230**2 + m.x237**2 + m.x238**2 - 2*m.x229*m.x237 - 2*m.x230*m.x238
                          - 1.436936830729*m.b23 - 1.436936830729*m.b35 >= -1.436936830729)

m.c432 = Constraint(expr=m.x229**2 + m.x230**2 + m.x237**2 + m.x238**2 - 2*m.x229*m.x237 - 2*m.x230*m.x238
                          - 1.436936830729*m.b24 - 1.436936830729*m.b36 >= -1.436936830729)

m.c433 = Constraint(expr=m.x229**2 + m.x230**2 + m.x237**2 + m.x238**2 - 2*m.x229*m.x237 - 2*m.x230*m.x238
                          - 1.436936830729*m.b25 - 1.436936830729*m.b37 >= -1.436936830729)

m.c434 = Constraint(expr=m.x229**2 + m.x230**2 + m.x239**2 + m.x240**2 - 2*m.x229*m.x239 - 2*m.x230*m.x240
                          - 1.436936830729*m.b23 - 1.436936830729*m.b38 >= -1.436936830729)

m.c435 = Constraint(expr=m.x229**2 + m.x230**2 + m.x239**2 + m.x240**2 - 2*m.x229*m.x239 - 2*m.x230*m.x240
                          - 1.436936830729*m.b24 - 1.436936830729*m.b39 >= -1.436936830729)

m.c436 = Constraint(expr=m.x229**2 + m.x230**2 + m.x239**2 + m.x240**2 - 2*m.x229*m.x239 - 2*m.x230*m.x240
                          - 1.436936830729*m.b25 - 1.436936830729*m.b40 >= -1.436936830729)

m.c437 = Constraint(expr=m.x229**2 + m.x230**2 + m.x241**2 + m.x242**2 - 2*m.x229*m.x241 - 2*m.x230*m.x242
                          - 1.436936830729*m.b23 - 1.436936830729*m.b41 >= -1.436936830729)

m.c438 = Constraint(expr=m.x229**2 + m.x230**2 + m.x241**2 + m.x242**2 - 2*m.x230*m.x242 - 2*m.x229*m.x241
                          - 1.436936830729*m.b24 - 1.436936830729*m.b42 >= -1.436936830729)

m.c439 = Constraint(expr=m.x229**2 + m.x230**2 + m.x241**2 + m.x242**2 - 2*m.x230*m.x242 - 2*m.x229*m.x241
                          - 1.436936830729*m.b25 - 1.436936830729*m.b43 >= -1.436936830729)

m.c440 = Constraint(expr=m.x229**2 + m.x230**2 + m.x243**2 + m.x244**2 - 2*m.x230*m.x244 - 2*m.x229*m.x243
                          - 1.436936830729*m.b23 - 1.436936830729*m.b44 >= -1.436936830729)

m.c441 = Constraint(expr=m.x229**2 + m.x230**2 + m.x243**2 + m.x244**2 - 2*m.x230*m.x244 - 2*m.x229*m.x243
                          - 1.436936830729*m.b24 - 1.436936830729*m.b45 >= -1.436936830729)

m.c442 = Constraint(expr=m.x229**2 + m.x230**2 + m.x243**2 + m.x244**2 - 2*m.x230*m.x244 - 2*m.x229*m.x243
                          - 1.436936830729*m.b25 - 1.436936830729*m.b46 >= -1.436936830729)

m.c443 = Constraint(expr=m.x229**2 + m.x230**2 + m.x245**2 + m.x246**2 - 2*m.x229*m.x245 - 2*m.x230*m.x246
                          - 1.436936830729*m.b23 - 1.436936830729*m.b47 >= -1.436936830729)

m.c444 = Constraint(expr=m.x229**2 + m.x230**2 + m.x245**2 + m.x246**2 - 2*m.x229*m.x245 - 2*m.x230*m.x246
                          - 1.436936830729*m.b24 - 1.436936830729*m.b48 >= -1.436936830729)

m.c445 = Constraint(expr=m.x229**2 + m.x230**2 + m.x245**2 + m.x246**2 - 2*m.x229*m.x245 - 2*m.x230*m.x246
                          - 1.436936830729*m.b25 - 1.436936830729*m.b49 >= -1.436936830729)

m.c446 = Constraint(expr=m.x229**2 + m.x230**2 + m.x247**2 + m.x248**2 - 2*m.x230*m.x248 - 2*m.x229*m.x247
                          - 3.484990776969*m.b23 - 3.484990776969*m.b50 >= -3.484990776969)

m.c447 = Constraint(expr=m.x229**2 + m.x230**2 + m.x247**2 + m.x248**2 - 2*m.x230*m.x248 - 2*m.x229*m.x247
                          - 3.484990776969*m.b24 - 3.484990776969*m.b51 >= -3.484990776969)

m.c448 = Constraint(expr=m.x229**2 + m.x230**2 + m.x247**2 + m.x248**2 - 2*m.x229*m.x247 - 2*m.x230*m.x248
                          - 3.484990776969*m.b25 - 3.484990776969*m.b52 >= -3.484990776969)

m.c449 = Constraint(expr=m.x229**2 + m.x230**2 + m.x249**2 + m.x250**2 - 2*m.x229*m.x249 - 2*m.x230*m.x250
                          - 3.484990776969*m.b23 - 3.484990776969*m.b53 >= -3.484990776969)

m.c450 = Constraint(expr=m.x229**2 + m.x230**2 + m.x249**2 + m.x250**2 - 2*m.x229*m.x249 - 2*m.x230*m.x250
                          - 3.484990776969*m.b24 - 3.484990776969*m.b54 >= -3.484990776969)

m.c451 = Constraint(expr=m.x229**2 + m.x230**2 + m.x249**2 + m.x250**2 - 2*m.x229*m.x249 - 2*m.x230*m.x250
                          - 3.484990776969*m.b25 - 3.484990776969*m.b55 >= -3.484990776969)

m.c452 = Constraint(expr=m.x229**2 + m.x230**2 + m.x251**2 + m.x252**2 - 2*m.x230*m.x252 - 2*m.x229*m.x251
                          - 5.174182750489*m.b23 - 5.174182750489*m.b56 >= -5.174182750489)

m.c453 = Constraint(expr=m.x229**2 + m.x230**2 + m.x251**2 + m.x252**2 - 2*m.x230*m.x252 - 2*m.x229*m.x251
                          - 5.174182750489*m.b24 - 5.174182750489*m.b57 >= -5.174182750489)

m.c454 = Constraint(expr=m.x229**2 + m.x230**2 + m.x251**2 + m.x252**2 - 2*m.x230*m.x252 - 2*m.x229*m.x251
                          - 5.174182750489*m.b25 - 5.174182750489*m.b58 >= -5.174182750489)

m.c455 = Constraint(expr=m.x229**2 + m.x230**2 + m.x253**2 + m.x254**2 - 2*m.x230*m.x254 - 2*m.x229*m.x253
                          - 5.174182750489*m.b23 - 5.174182750489*m.b59 >= -5.174182750489)

m.c456 = Constraint(expr=m.x229**2 + m.x230**2 + m.x253**2 + m.x254**2 - 2*m.x230*m.x254 - 2*m.x229*m.x253
                          - 5.174182750489*m.b24 - 5.174182750489*m.b60 >= -5.174182750489)

m.c457 = Constraint(expr=m.x229**2 + m.x230**2 + m.x253**2 + m.x254**2 - 2*m.x230*m.x254 - 2*m.x229*m.x253
                          - 5.174182750489*m.b25 - 5.174182750489*m.b61 >= -5.174182750489)

m.c458 = Constraint(expr=m.x215**2 + m.x216**2 + m.x231**2 + m.x232**2 - 2*m.x216*m.x232 - 2*m.x215*m.x231
                          - 0.887203867225*m.b2 - 0.887203867225*m.b26 >= -0.887203867225)

m.c459 = Constraint(expr=m.x215**2 + m.x216**2 + m.x231**2 + m.x232**2 - 2*m.x216*m.x232 - 2*m.x215*m.x231
                          - 0.887203867225*m.b3 - 0.887203867225*m.b27 >= -0.887203867225)

m.c460 = Constraint(expr=m.x215**2 + m.x216**2 + m.x231**2 + m.x232**2 - 2*m.x216*m.x232 - 2*m.x215*m.x231
                          - 0.887203867225*m.b4 - 0.887203867225*m.b28 >= -0.887203867225)

m.c461 = Constraint(expr=m.x217**2 + m.x218**2 + m.x231**2 + m.x232**2 - 2*m.x218*m.x232 - 2*m.x217*m.x231
                          - 0.887203867225*m.b5 - 0.887203867225*m.b26 >= -0.887203867225)

m.c462 = Constraint(expr=m.x217**2 + m.x218**2 + m.x231**2 + m.x232**2 - 2*m.x218*m.x232 - 2*m.x217*m.x231
                          - 0.887203867225*m.b6 - 0.887203867225*m.b27 >= -0.887203867225)

m.c463 = Constraint(expr=m.x217**2 + m.x218**2 + m.x231**2 + m.x232**2 - 2*m.x218*m.x232 - 2*m.x217*m.x231
                          - 0.887203867225*m.b7 - 0.887203867225*m.b28 >= -0.887203867225)

m.c464 = Constraint(expr=m.x219**2 + m.x220**2 + m.x231**2 + m.x232**2 - 2*m.x219*m.x231 - 2*m.x220*m.x232
                          - 0.887203867225*m.b8 - 0.887203867225*m.b26 >= -0.887203867225)

m.c465 = Constraint(expr=m.x219**2 + m.x220**2 + m.x231**2 + m.x232**2 - 2*m.x219*m.x231 - 2*m.x220*m.x232
                          - 0.887203867225*m.b9 - 0.887203867225*m.b27 >= -0.887203867225)

m.c466 = Constraint(expr=m.x219**2 + m.x220**2 + m.x231**2 + m.x232**2 - 2*m.x219*m.x231 - 2*m.x220*m.x232
                          - 0.887203867225*m.b10 - 0.887203867225*m.b28 >= -0.887203867225)

m.c467 = Constraint(expr=m.x221**2 + m.x222**2 + m.x231**2 + m.x232**2 - 2*m.x221*m.x231 - 2*m.x222*m.x232
                          - 0.887203867225*m.b11 - 0.887203867225*m.b26 >= -0.887203867225)

m.c468 = Constraint(expr=m.x221**2 + m.x222**2 + m.x231**2 + m.x232**2 - 2*m.x221*m.x231 - 2*m.x222*m.x232
                          - 0.887203867225*m.b12 - 0.887203867225*m.b27 >= -0.887203867225)

m.c469 = Constraint(expr=m.x221**2 + m.x222**2 + m.x231**2 + m.x232**2 - 2*m.x221*m.x231 - 2*m.x222*m.x232
                          - 0.887203867225*m.b13 - 0.887203867225*m.b28 >= -0.887203867225)

m.c470 = Constraint(expr=m.x223**2 + m.x224**2 + m.x231**2 + m.x232**2 - 2*m.x223*m.x231 - 2*m.x224*m.x232
                          - 0.887203867225*m.b14 - 0.887203867225*m.b26 >= -0.887203867225)

m.c471 = Constraint(expr=m.x223**2 + m.x224**2 + m.x231**2 + m.x232**2 - 2*m.x223*m.x231 - 2*m.x224*m.x232
                          - 0.887203867225*m.b15 - 0.887203867225*m.b27 >= -0.887203867225)

m.c472 = Constraint(expr=m.x223**2 + m.x224**2 + m.x231**2 + m.x232**2 - 2*m.x223*m.x231 - 2*m.x224*m.x232
                          - 0.887203867225*m.b16 - 0.887203867225*m.b28 >= -0.887203867225)

m.c473 = Constraint(expr=m.x225**2 + m.x226**2 + m.x231**2 + m.x232**2 - 2*m.x225*m.x231 - 2*m.x226*m.x232
                          - 0.887203867225*m.b17 - 0.887203867225*m.b26 >= -0.887203867225)

m.c474 = Constraint(expr=m.x225**2 + m.x226**2 + m.x231**2 + m.x232**2 - 2*m.x225*m.x231 - 2*m.x226*m.x232
                          - 0.887203867225*m.b18 - 0.887203867225*m.b27 >= -0.887203867225)

m.c475 = Constraint(expr=m.x225**2 + m.x226**2 + m.x231**2 + m.x232**2 - 2*m.x225*m.x231 - 2*m.x226*m.x232
                          - 0.887203867225*m.b19 - 0.887203867225*m.b28 >= -0.887203867225)

m.c476 = Constraint(expr=m.x227**2 + m.x228**2 + m.x231**2 + m.x232**2 - 2*m.x227*m.x231 - 2*m.x228*m.x232
                          - 0.469370231236*m.b20 - 0.469370231236*m.b26 >= -0.469370231236)

m.c477 = Constraint(expr=m.x227**2 + m.x228**2 + m.x231**2 + m.x232**2 - 2*m.x227*m.x231 - 2*m.x228*m.x232
                          - 0.469370231236*m.b21 - 0.469370231236*m.b27 >= -0.469370231236)

m.c478 = Constraint(expr=m.x227**2 + m.x228**2 + m.x231**2 + m.x232**2 - 2*m.x227*m.x231 - 2*m.x228*m.x232
                          - 0.469370231236*m.b22 - 0.469370231236*m.b28 >= -0.469370231236)

m.c479 = Constraint(expr=m.x229**2 + m.x230**2 + m.x231**2 + m.x232**2 - 2*m.x229*m.x231 - 2*m.x230*m.x232
                          - 0.469370231236*m.b23 - 0.469370231236*m.b26 >= -0.469370231236)

m.c480 = Constraint(expr=m.x229**2 + m.x230**2 + m.x231**2 + m.x232**2 - 2*m.x229*m.x231 - 2*m.x230*m.x232
                          - 0.469370231236*m.b24 - 0.469370231236*m.b27 >= -0.469370231236)

m.c481 = Constraint(expr=m.x229**2 + m.x230**2 + m.x231**2 + m.x232**2 - 2*m.x229*m.x231 - 2*m.x230*m.x232
                          - 0.469370231236*m.b25 - 0.469370231236*m.b28 >= -0.469370231236)

m.c482 = Constraint(expr=m.x231**2 + m.x232**2 + m.x233**2 + m.x234**2 - 2*m.x231*m.x233 - 2*m.x232*m.x234
                          - 0.469370231236*m.b26 - 0.469370231236*m.b29 >= -0.469370231236)

m.c483 = Constraint(expr=m.x231**2 + m.x232**2 + m.x233**2 + m.x234**2 - 2*m.x231*m.x233 - 2*m.x232*m.x234
                          - 0.469370231236*m.b27 - 0.469370231236*m.b30 >= -0.469370231236)

m.c484 = Constraint(expr=m.x231**2 + m.x232**2 + m.x233**2 + m.x234**2 - 2*m.x231*m.x233 - 2*m.x232*m.x234
                          - 0.469370231236*m.b28 - 0.469370231236*m.b31 >= -0.469370231236)

m.c485 = Constraint(expr=m.x231**2 + m.x232**2 + m.x235**2 + m.x236**2 - 2*m.x231*m.x235 - 2*m.x232*m.x236
                          - 0.469370231236*m.b26 - 0.469370231236*m.b32 >= -0.469370231236)

m.c486 = Constraint(expr=m.x231**2 + m.x232**2 + m.x235**2 + m.x236**2 - 2*m.x231*m.x235 - 2*m.x232*m.x236
                          - 0.469370231236*m.b27 - 0.469370231236*m.b33 >= -0.469370231236)

m.c487 = Constraint(expr=m.x231**2 + m.x232**2 + m.x235**2 + m.x236**2 - 2*m.x231*m.x235 - 2*m.x232*m.x236
                          - 0.469370231236*m.b28 - 0.469370231236*m.b34 >= -0.469370231236)

m.c488 = Constraint(expr=m.x231**2 + m.x232**2 + m.x237**2 + m.x238**2 - 2*m.x231*m.x237 - 2*m.x232*m.x238
                          - 1.436936830729*m.b26 - 1.436936830729*m.b35 >= -1.436936830729)

m.c489 = Constraint(expr=m.x231**2 + m.x232**2 + m.x237**2 + m.x238**2 - 2*m.x231*m.x237 - 2*m.x232*m.x238
                          - 1.436936830729*m.b27 - 1.436936830729*m.b36 >= -1.436936830729)

m.c490 = Constraint(expr=m.x231**2 + m.x232**2 + m.x237**2 + m.x238**2 - 2*m.x231*m.x237 - 2*m.x232*m.x238
                          - 1.436936830729*m.b28 - 1.436936830729*m.b37 >= -1.436936830729)

m.c491 = Constraint(expr=m.x231**2 + m.x232**2 + m.x239**2 + m.x240**2 - 2*m.x231*m.x239 - 2*m.x232*m.x240
                          - 1.436936830729*m.b26 - 1.436936830729*m.b38 >= -1.436936830729)

m.c492 = Constraint(expr=m.x231**2 + m.x232**2 + m.x239**2 + m.x240**2 - 2*m.x231*m.x239 - 2*m.x232*m.x240
                          - 1.436936830729*m.b27 - 1.436936830729*m.b39 >= -1.436936830729)

m.c493 = Constraint(expr=m.x231**2 + m.x232**2 + m.x239**2 + m.x240**2 - 2*m.x231*m.x239 - 2*m.x232*m.x240
                          - 1.436936830729*m.b28 - 1.436936830729*m.b40 >= -1.436936830729)

m.c494 = Constraint(expr=m.x231**2 + m.x232**2 + m.x241**2 + m.x242**2 - 2*m.x232*m.x242 - 2*m.x231*m.x241
                          - 1.436936830729*m.b26 - 1.436936830729*m.b41 >= -1.436936830729)

m.c495 = Constraint(expr=m.x231**2 + m.x232**2 + m.x241**2 + m.x242**2 - 2*m.x232*m.x242 - 2*m.x231*m.x241
                          - 1.436936830729*m.b27 - 1.436936830729*m.b42 >= -1.436936830729)

m.c496 = Constraint(expr=m.x231**2 + m.x232**2 + m.x241**2 + m.x242**2 - 2*m.x232*m.x242 - 2*m.x231*m.x241
                          - 1.436936830729*m.b28 - 1.436936830729*m.b43 >= -1.436936830729)

m.c497 = Constraint(expr=m.x231**2 + m.x232**2 + m.x243**2 + m.x244**2 - 2*m.x231*m.x243 - 2*m.x232*m.x244
                          - 1.436936830729*m.b26 - 1.436936830729*m.b44 >= -1.436936830729)

m.c498 = Constraint(expr=m.x231**2 + m.x232**2 + m.x243**2 + m.x244**2 - 2*m.x231*m.x243 - 2*m.x232*m.x244
                          - 1.436936830729*m.b27 - 1.436936830729*m.b45 >= -1.436936830729)

m.c499 = Constraint(expr=m.x231**2 + m.x232**2 + m.x243**2 + m.x244**2 - 2*m.x231*m.x243 - 2*m.x232*m.x244
                          - 1.436936830729*m.b28 - 1.436936830729*m.b46 >= -1.436936830729)

m.c500 = Constraint(expr=m.x231**2 + m.x232**2 + m.x245**2 + m.x246**2 - 2*m.x232*m.x246 - 2*m.x231*m.x245
                          - 1.436936830729*m.b26 - 1.436936830729*m.b47 >= -1.436936830729)

m.c501 = Constraint(expr=m.x231**2 + m.x232**2 + m.x245**2 + m.x246**2 - 2*m.x232*m.x246 - 2*m.x231*m.x245
                          - 1.436936830729*m.b27 - 1.436936830729*m.b48 >= -1.436936830729)

m.c502 = Constraint(expr=m.x231**2 + m.x232**2 + m.x245**2 + m.x246**2 - 2*m.x232*m.x246 - 2*m.x231*m.x245
                          - 1.436936830729*m.b28 - 1.436936830729*m.b49 >= -1.436936830729)

m.c503 = Constraint(expr=m.x231**2 + m.x232**2 + m.x247**2 + m.x248**2 - 2*m.x231*m.x247 - 2*m.x232*m.x248
                          - 3.484990776969*m.b26 - 3.484990776969*m.b50 >= -3.484990776969)

m.c504 = Constraint(expr=m.x231**2 + m.x232**2 + m.x247**2 + m.x248**2 - 2*m.x231*m.x247 - 2*m.x232*m.x248
                          - 3.484990776969*m.b27 - 3.484990776969*m.b51 >= -3.484990776969)

m.c505 = Constraint(expr=m.x231**2 + m.x232**2 + m.x247**2 + m.x248**2 - 2*m.x231*m.x247 - 2*m.x232*m.x248
                          - 3.484990776969*m.b28 - 3.484990776969*m.b52 >= -3.484990776969)

m.c506 = Constraint(expr=m.x231**2 + m.x232**2 + m.x249**2 + m.x250**2 - 2*m.x232*m.x250 - 2*m.x231*m.x249
                          - 3.484990776969*m.b26 - 3.484990776969*m.b53 >= -3.484990776969)

m.c507 = Constraint(expr=m.x231**2 + m.x232**2 + m.x249**2 + m.x250**2 - 2*m.x232*m.x250 - 2*m.x231*m.x249
                          - 3.484990776969*m.b27 - 3.484990776969*m.b54 >= -3.484990776969)

m.c508 = Constraint(expr=m.x231**2 + m.x232**2 + m.x249**2 + m.x250**2 - 2*m.x232*m.x250 - 2*m.x231*m.x249
                          - 3.484990776969*m.b28 - 3.484990776969*m.b55 >= -3.484990776969)

m.c509 = Constraint(expr=m.x231**2 + m.x232**2 + m.x251**2 + m.x252**2 - 2*m.x231*m.x251 - 2*m.x232*m.x252
                          - 5.174182750489*m.b26 - 5.174182750489*m.b56 >= -5.174182750489)

m.c510 = Constraint(expr=m.x231**2 + m.x232**2 + m.x251**2 + m.x252**2 - 2*m.x231*m.x251 - 2*m.x232*m.x252
                          - 5.174182750489*m.b27 - 5.174182750489*m.b57 >= -5.174182750489)

m.c511 = Constraint(expr=m.x231**2 + m.x232**2 + m.x251**2 + m.x252**2 - 2*m.x231*m.x251 - 2*m.x232*m.x252
                          - 5.174182750489*m.b28 - 5.174182750489*m.b58 >= -5.174182750489)

m.c512 = Constraint(expr=m.x231**2 + m.x232**2 + m.x253**2 + m.x254**2 - 2*m.x231*m.x253 - 2*m.x232*m.x254
                          - 5.174182750489*m.b26 - 5.174182750489*m.b59 >= -5.174182750489)

m.c513 = Constraint(expr=m.x231**2 + m.x232**2 + m.x253**2 + m.x254**2 - 2*m.x231*m.x253 - 2*m.x232*m.x254
                          - 5.174182750489*m.b27 - 5.174182750489*m.b60 >= -5.174182750489)

m.c514 = Constraint(expr=m.x231**2 + m.x232**2 + m.x253**2 + m.x254**2 - 2*m.x231*m.x253 - 2*m.x232*m.x254
                          - 5.174182750489*m.b28 - 5.174182750489*m.b61 >= -5.174182750489)

m.c515 = Constraint(expr=m.x215**2 + m.x216**2 + m.x233**2 + m.x234**2 - 2*m.x216*m.x234 - 2*m.x215*m.x233
                          - 0.887203867225*m.b2 - 0.887203867225*m.b29 >= -0.887203867225)

m.c516 = Constraint(expr=m.x215**2 + m.x216**2 + m.x233**2 + m.x234**2 - 2*m.x216*m.x234 - 2*m.x215*m.x233
                          - 0.887203867225*m.b3 - 0.887203867225*m.b30 >= -0.887203867225)

m.c517 = Constraint(expr=m.x215**2 + m.x216**2 + m.x233**2 + m.x234**2 - 2*m.x216*m.x234 - 2*m.x215*m.x233
                          - 0.887203867225*m.b4 - 0.887203867225*m.b31 >= -0.887203867225)

m.c518 = Constraint(expr=m.x217**2 + m.x218**2 + m.x233**2 + m.x234**2 - 2*m.x217*m.x233 - 2*m.x218*m.x234
                          - 0.887203867225*m.b5 - 0.887203867225*m.b29 >= -0.887203867225)

m.c519 = Constraint(expr=m.x217**2 + m.x218**2 + m.x233**2 + m.x234**2 - 2*m.x217*m.x233 - 2*m.x218*m.x234
                          - 0.887203867225*m.b6 - 0.887203867225*m.b30 >= -0.887203867225)

m.c520 = Constraint(expr=m.x217**2 + m.x218**2 + m.x233**2 + m.x234**2 - 2*m.x217*m.x233 - 2*m.x218*m.x234
                          - 0.887203867225*m.b7 - 0.887203867225*m.b31 >= -0.887203867225)

m.c521 = Constraint(expr=m.x219**2 + m.x220**2 + m.x233**2 + m.x234**2 - 2*m.x220*m.x234 - 2*m.x219*m.x233
                          - 0.887203867225*m.b8 - 0.887203867225*m.b29 >= -0.887203867225)

m.c522 = Constraint(expr=m.x219**2 + m.x220**2 + m.x233**2 + m.x234**2 - 2*m.x219*m.x233 - 2*m.x220*m.x234
                          - 0.887203867225*m.b9 - 0.887203867225*m.b30 >= -0.887203867225)

m.c523 = Constraint(expr=m.x219**2 + m.x220**2 + m.x233**2 + m.x234**2 - 2*m.x219*m.x233 - 2*m.x220*m.x234
                          - 0.887203867225*m.b10 - 0.887203867225*m.b31 >= -0.887203867225)

m.c524 = Constraint(expr=m.x221**2 + m.x222**2 + m.x233**2 + m.x234**2 - 2*m.x221*m.x233 - 2*m.x222*m.x234
                          - 0.887203867225*m.b11 - 0.887203867225*m.b29 >= -0.887203867225)

m.c525 = Constraint(expr=m.x221**2 + m.x222**2 + m.x233**2 + m.x234**2 - 2*m.x221*m.x233 - 2*m.x222*m.x234
                          - 0.887203867225*m.b12 - 0.887203867225*m.b30 >= -0.887203867225)

m.c526 = Constraint(expr=m.x221**2 + m.x222**2 + m.x233**2 + m.x234**2 - 2*m.x221*m.x233 - 2*m.x222*m.x234
                          - 0.887203867225*m.b13 - 0.887203867225*m.b31 >= -0.887203867225)

m.c527 = Constraint(expr=m.x223**2 + m.x224**2 + m.x233**2 + m.x234**2 - 2*m.x223*m.x233 - 2*m.x224*m.x234
                          - 0.887203867225*m.b14 - 0.887203867225*m.b29 >= -0.887203867225)

m.c528 = Constraint(expr=m.x223**2 + m.x224**2 + m.x233**2 + m.x234**2 - 2*m.x223*m.x233 - 2*m.x224*m.x234
                          - 0.887203867225*m.b15 - 0.887203867225*m.b30 >= -0.887203867225)

m.c529 = Constraint(expr=m.x223**2 + m.x224**2 + m.x233**2 + m.x234**2 - 2*m.x223*m.x233 - 2*m.x224*m.x234
                          - 0.887203867225*m.b16 - 0.887203867225*m.b31 >= -0.887203867225)

m.c530 = Constraint(expr=m.x225**2 + m.x226**2 + m.x233**2 + m.x234**2 - 2*m.x225*m.x233 - 2*m.x226*m.x234
                          - 0.887203867225*m.b17 - 0.887203867225*m.b29 >= -0.887203867225)

m.c531 = Constraint(expr=m.x225**2 + m.x226**2 + m.x233**2 + m.x234**2 - 2*m.x225*m.x233 - 2*m.x226*m.x234
                          - 0.887203867225*m.b18 - 0.887203867225*m.b30 >= -0.887203867225)

m.c532 = Constraint(expr=m.x225**2 + m.x226**2 + m.x233**2 + m.x234**2 - 2*m.x225*m.x233 - 2*m.x226*m.x234
                          - 0.887203867225*m.b19 - 0.887203867225*m.b31 >= -0.887203867225)

m.c533 = Constraint(expr=m.x227**2 + m.x228**2 + m.x233**2 + m.x234**2 - 2*m.x227*m.x233 - 2*m.x228*m.x234
                          - 0.469370231236*m.b20 - 0.469370231236*m.b29 >= -0.469370231236)

m.c534 = Constraint(expr=m.x227**2 + m.x228**2 + m.x233**2 + m.x234**2 - 2*m.x227*m.x233 - 2*m.x228*m.x234
                          - 0.469370231236*m.b21 - 0.469370231236*m.b30 >= -0.469370231236)

m.c535 = Constraint(expr=m.x227**2 + m.x228**2 + m.x233**2 + m.x234**2 - 2*m.x227*m.x233 - 2*m.x228*m.x234
                          - 0.469370231236*m.b22 - 0.469370231236*m.b31 >= -0.469370231236)

m.c536 = Constraint(expr=m.x229**2 + m.x230**2 + m.x233**2 + m.x234**2 - 2*m.x229*m.x233 - 2*m.x230*m.x234
                          - 0.469370231236*m.b23 - 0.469370231236*m.b29 >= -0.469370231236)

m.c537 = Constraint(expr=m.x229**2 + m.x230**2 + m.x233**2 + m.x234**2 - 2*m.x229*m.x233 - 2*m.x230*m.x234
                          - 0.469370231236*m.b24 - 0.469370231236*m.b30 >= -0.469370231236)

m.c538 = Constraint(expr=m.x229**2 + m.x230**2 + m.x233**2 + m.x234**2 - 2*m.x229*m.x233 - 2*m.x230*m.x234
                          - 0.469370231236*m.b25 - 0.469370231236*m.b31 >= -0.469370231236)

m.c539 = Constraint(expr=m.x231**2 + m.x232**2 + m.x233**2 + m.x234**2 - 2*m.x231*m.x233 - 2*m.x232*m.x234
                          - 0.469370231236*m.b26 - 0.469370231236*m.b29 >= -0.469370231236)

m.c540 = Constraint(expr=m.x231**2 + m.x232**2 + m.x233**2 + m.x234**2 - 2*m.x231*m.x233 - 2*m.x232*m.x234
                          - 0.469370231236*m.b27 - 0.469370231236*m.b30 >= -0.469370231236)

m.c541 = Constraint(expr=m.x231**2 + m.x232**2 + m.x233**2 + m.x234**2 - 2*m.x231*m.x233 - 2*m.x232*m.x234
                          - 0.469370231236*m.b28 - 0.469370231236*m.b31 >= -0.469370231236)

m.c542 = Constraint(expr=m.x233**2 + m.x234**2 + m.x235**2 + m.x236**2 - 2*m.x233*m.x235 - 2*m.x234*m.x236
                          - 0.469370231236*m.b29 - 0.469370231236*m.b32 >= -0.469370231236)

m.c543 = Constraint(expr=m.x233**2 + m.x234**2 + m.x235**2 + m.x236**2 - 2*m.x233*m.x235 - 2*m.x234*m.x236
                          - 0.469370231236*m.b30 - 0.469370231236*m.b33 >= -0.469370231236)

m.c544 = Constraint(expr=m.x233**2 + m.x234**2 + m.x235**2 + m.x236**2 - 2*m.x233*m.x235 - 2*m.x234*m.x236
                          - 0.469370231236*m.b31 - 0.469370231236*m.b34 >= -0.469370231236)

m.c545 = Constraint(expr=m.x233**2 + m.x234**2 + m.x237**2 + m.x238**2 - 2*m.x233*m.x237 - 2*m.x234*m.x238
                          - 1.436936830729*m.b29 - 1.436936830729*m.b35 >= -1.436936830729)

m.c546 = Constraint(expr=m.x233**2 + m.x234**2 + m.x237**2 + m.x238**2 - 2*m.x233*m.x237 - 2*m.x234*m.x238
                          - 1.436936830729*m.b30 - 1.436936830729*m.b36 >= -1.436936830729)

m.c547 = Constraint(expr=m.x233**2 + m.x234**2 + m.x237**2 + m.x238**2 - 2*m.x233*m.x237 - 2*m.x234*m.x238
                          - 1.436936830729*m.b31 - 1.436936830729*m.b37 >= -1.436936830729)

m.c548 = Constraint(expr=m.x233**2 + m.x234**2 + m.x239**2 + m.x240**2 - 2*m.x233*m.x239 - 2*m.x234*m.x240
                          - 1.436936830729*m.b29 - 1.436936830729*m.b38 >= -1.436936830729)

m.c549 = Constraint(expr=m.x233**2 + m.x234**2 + m.x239**2 + m.x240**2 - 2*m.x233*m.x239 - 2*m.x234*m.x240
                          - 1.436936830729*m.b30 - 1.436936830729*m.b39 >= -1.436936830729)

m.c550 = Constraint(expr=m.x233**2 + m.x234**2 + m.x239**2 + m.x240**2 - 2*m.x233*m.x239 - 2*m.x234*m.x240
                          - 1.436936830729*m.b31 - 1.436936830729*m.b40 >= -1.436936830729)

m.c551 = Constraint(expr=m.x233**2 + m.x234**2 + m.x241**2 + m.x242**2 - 2*m.x233*m.x241 - 2*m.x234*m.x242
                          - 1.436936830729*m.b29 - 1.436936830729*m.b41 >= -1.436936830729)

m.c552 = Constraint(expr=m.x233**2 + m.x234**2 + m.x241**2 + m.x242**2 - 2*m.x233*m.x241 - 2*m.x234*m.x242
                          - 1.436936830729*m.b30 - 1.436936830729*m.b42 >= -1.436936830729)

m.c553 = Constraint(expr=m.x233**2 + m.x234**2 + m.x241**2 + m.x242**2 - 2*m.x233*m.x241 - 2*m.x234*m.x242
                          - 1.436936830729*m.b31 - 1.436936830729*m.b43 >= -1.436936830729)

m.c554 = Constraint(expr=m.x233**2 + m.x234**2 + m.x243**2 + m.x244**2 - 2*m.x234*m.x244 - 2*m.x233*m.x243
                          - 1.436936830729*m.b29 - 1.436936830729*m.b44 >= -1.436936830729)

m.c555 = Constraint(expr=m.x233**2 + m.x234**2 + m.x243**2 + m.x244**2 - 2*m.x234*m.x244 - 2*m.x233*m.x243
                          - 1.436936830729*m.b30 - 1.436936830729*m.b45 >= -1.436936830729)

m.c556 = Constraint(expr=m.x233**2 + m.x234**2 + m.x243**2 + m.x244**2 - 2*m.x234*m.x244 - 2*m.x233*m.x243
                          - 1.436936830729*m.b31 - 1.436936830729*m.b46 >= -1.436936830729)

m.c557 = Constraint(expr=m.x233**2 + m.x234**2 + m.x245**2 + m.x246**2 - 2*m.x234*m.x246 - 2*m.x233*m.x245
                          - 1.436936830729*m.b29 - 1.436936830729*m.b47 >= -1.436936830729)

m.c558 = Constraint(expr=m.x233**2 + m.x234**2 + m.x245**2 + m.x246**2 - 2*m.x233*m.x245 - 2*m.x234*m.x246
                          - 1.436936830729*m.b30 - 1.436936830729*m.b48 >= -1.436936830729)

m.c559 = Constraint(expr=m.x233**2 + m.x234**2 + m.x245**2 + m.x246**2 - 2*m.x233*m.x245 - 2*m.x234*m.x246
                          - 1.436936830729*m.b31 - 1.436936830729*m.b49 >= -1.436936830729)

m.c560 = Constraint(expr=m.x233**2 + m.x234**2 + m.x247**2 + m.x248**2 - 2*m.x234*m.x248 - 2*m.x233*m.x247
                          - 3.484990776969*m.b29 - 3.484990776969*m.b50 >= -3.484990776969)

m.c561 = Constraint(expr=m.x233**2 + m.x234**2 + m.x247**2 + m.x248**2 - 2*m.x234*m.x248 - 2*m.x233*m.x247
                          - 3.484990776969*m.b30 - 3.484990776969*m.b51 >= -3.484990776969)

m.c562 = Constraint(expr=m.x233**2 + m.x234**2 + m.x247**2 + m.x248**2 - 2*m.x234*m.x248 - 2*m.x233*m.x247
                          - 3.484990776969*m.b31 - 3.484990776969*m.b52 >= -3.484990776969)

m.c563 = Constraint(expr=m.x233**2 + m.x234**2 + m.x249**2 + m.x250**2 - 2*m.x234*m.x250 - 2*m.x233*m.x249
                          - 3.484990776969*m.b29 - 3.484990776969*m.b53 >= -3.484990776969)

m.c564 = Constraint(expr=m.x233**2 + m.x234**2 + m.x249**2 + m.x250**2 - 2*m.x234*m.x250 - 2*m.x233*m.x249
                          - 3.484990776969*m.b30 - 3.484990776969*m.b54 >= -3.484990776969)

m.c565 = Constraint(expr=m.x233**2 + m.x234**2 + m.x249**2 + m.x250**2 - 2*m.x234*m.x250 - 2*m.x233*m.x249
                          - 3.484990776969*m.b31 - 3.484990776969*m.b55 >= -3.484990776969)

m.c566 = Constraint(expr=m.x233**2 + m.x234**2 + m.x251**2 + m.x252**2 - 2*m.x233*m.x251 - 2*m.x234*m.x252
                          - 5.174182750489*m.b29 - 5.174182750489*m.b56 >= -5.174182750489)

m.c567 = Constraint(expr=m.x233**2 + m.x234**2 + m.x251**2 + m.x252**2 - 2*m.x233*m.x251 - 2*m.x234*m.x252
                          - 5.174182750489*m.b30 - 5.174182750489*m.b57 >= -5.174182750489)

m.c568 = Constraint(expr=m.x233**2 + m.x234**2 + m.x251**2 + m.x252**2 - 2*m.x233*m.x251 - 2*m.x234*m.x252
                          - 5.174182750489*m.b31 - 5.174182750489*m.b58 >= -5.174182750489)

m.c569 = Constraint(expr=m.x233**2 + m.x234**2 + m.x253**2 + m.x254**2 - 2*m.x234*m.x254 - 2*m.x233*m.x253
                          - 5.174182750489*m.b29 - 5.174182750489*m.b59 >= -5.174182750489)

m.c570 = Constraint(expr=m.x233**2 + m.x234**2 + m.x253**2 + m.x254**2 - 2*m.x234*m.x254 - 2*m.x233*m.x253
                          - 5.174182750489*m.b30 - 5.174182750489*m.b60 >= -5.174182750489)

m.c571 = Constraint(expr=m.x233**2 + m.x234**2 + m.x253**2 + m.x254**2 - 2*m.x234*m.x254 - 2*m.x233*m.x253
                          - 5.174182750489*m.b31 - 5.174182750489*m.b61 >= -5.174182750489)

m.c572 = Constraint(expr=m.x215**2 + m.x216**2 + m.x235**2 + m.x236**2 - 2*m.x215*m.x235 - 2*m.x216*m.x236
                          - 0.887203867225*m.b2 - 0.887203867225*m.b32 >= -0.887203867225)

m.c573 = Constraint(expr=m.x215**2 + m.x216**2 + m.x235**2 + m.x236**2 - 2*m.x215*m.x235 - 2*m.x216*m.x236
                          - 0.887203867225*m.b3 - 0.887203867225*m.b33 >= -0.887203867225)

m.c574 = Constraint(expr=m.x215**2 + m.x216**2 + m.x235**2 + m.x236**2 - 2*m.x216*m.x236 - 2*m.x215*m.x235
                          - 0.887203867225*m.b4 - 0.887203867225*m.b34 >= -0.887203867225)

m.c575 = Constraint(expr=m.x217**2 + m.x218**2 + m.x235**2 + m.x236**2 - 2*m.x217*m.x235 - 2*m.x218*m.x236
                          - 0.887203867225*m.b5 - 0.887203867225*m.b32 >= -0.887203867225)

m.c576 = Constraint(expr=m.x217**2 + m.x218**2 + m.x235**2 + m.x236**2 - 2*m.x217*m.x235 - 2*m.x218*m.x236
                          - 0.887203867225*m.b6 - 0.887203867225*m.b33 >= -0.887203867225)

m.c577 = Constraint(expr=m.x217**2 + m.x218**2 + m.x235**2 + m.x236**2 - 2*m.x217*m.x235 - 2*m.x218*m.x236
                          - 0.887203867225*m.b7 - 0.887203867225*m.b34 >= -0.887203867225)

m.c578 = Constraint(expr=m.x219**2 + m.x220**2 + m.x235**2 + m.x236**2 - 2*m.x219*m.x235 - 2*m.x220*m.x236
                          - 0.887203867225*m.b8 - 0.887203867225*m.b32 >= -0.887203867225)

m.c579 = Constraint(expr=m.x219**2 + m.x220**2 + m.x235**2 + m.x236**2 - 2*m.x219*m.x235 - 2*m.x220*m.x236
                          - 0.887203867225*m.b9 - 0.887203867225*m.b33 >= -0.887203867225)

m.c580 = Constraint(expr=m.x219**2 + m.x220**2 + m.x235**2 + m.x236**2 - 2*m.x219*m.x235 - 2*m.x220*m.x236
                          - 0.887203867225*m.b10 - 0.887203867225*m.b34 >= -0.887203867225)

m.c581 = Constraint(expr=m.x221**2 + m.x222**2 + m.x235**2 + m.x236**2 - 2*m.x221*m.x235 - 2*m.x222*m.x236
                          - 0.887203867225*m.b11 - 0.887203867225*m.b32 >= -0.887203867225)

m.c582 = Constraint(expr=m.x221**2 + m.x222**2 + m.x235**2 + m.x236**2 - 2*m.x221*m.x235 - 2*m.x222*m.x236
                          - 0.887203867225*m.b12 - 0.887203867225*m.b33 >= -0.887203867225)

m.c583 = Constraint(expr=m.x221**2 + m.x222**2 + m.x235**2 + m.x236**2 - 2*m.x221*m.x235 - 2*m.x222*m.x236
                          - 0.887203867225*m.b13 - 0.887203867225*m.b34 >= -0.887203867225)

m.c584 = Constraint(expr=m.x223**2 + m.x224**2 + m.x235**2 + m.x236**2 - 2*m.x223*m.x235 - 2*m.x224*m.x236
                          - 0.887203867225*m.b14 - 0.887203867225*m.b32 >= -0.887203867225)

m.c585 = Constraint(expr=m.x223**2 + m.x224**2 + m.x235**2 + m.x236**2 - 2*m.x223*m.x235 - 2*m.x224*m.x236
                          - 0.887203867225*m.b15 - 0.887203867225*m.b33 >= -0.887203867225)

m.c586 = Constraint(expr=m.x223**2 + m.x224**2 + m.x235**2 + m.x236**2 - 2*m.x223*m.x235 - 2*m.x224*m.x236
                          - 0.887203867225*m.b16 - 0.887203867225*m.b34 >= -0.887203867225)

m.c587 = Constraint(expr=m.x225**2 + m.x226**2 + m.x235**2 + m.x236**2 - 2*m.x225*m.x235 - 2*m.x226*m.x236
                          - 0.887203867225*m.b17 - 0.887203867225*m.b32 >= -0.887203867225)

m.c588 = Constraint(expr=m.x225**2 + m.x226**2 + m.x235**2 + m.x236**2 - 2*m.x225*m.x235 - 2*m.x226*m.x236
                          - 0.887203867225*m.b18 - 0.887203867225*m.b33 >= -0.887203867225)

m.c589 = Constraint(expr=m.x225**2 + m.x226**2 + m.x235**2 + m.x236**2 - 2*m.x225*m.x235 - 2*m.x226*m.x236
                          - 0.887203867225*m.b19 - 0.887203867225*m.b34 >= -0.887203867225)

m.c590 = Constraint(expr=m.x227**2 + m.x228**2 + m.x235**2 + m.x236**2 - 2*m.x227*m.x235 - 2*m.x228*m.x236
                          - 0.469370231236*m.b20 - 0.469370231236*m.b32 >= -0.469370231236)

m.c591 = Constraint(expr=m.x227**2 + m.x228**2 + m.x235**2 + m.x236**2 - 2*m.x227*m.x235 - 2*m.x228*m.x236
                          - 0.469370231236*m.b21 - 0.469370231236*m.b33 >= -0.469370231236)

m.c592 = Constraint(expr=m.x227**2 + m.x228**2 + m.x235**2 + m.x236**2 - 2*m.x227*m.x235 - 2*m.x228*m.x236
                          - 0.469370231236*m.b22 - 0.469370231236*m.b34 >= -0.469370231236)

m.c593 = Constraint(expr=m.x229**2 + m.x230**2 + m.x235**2 + m.x236**2 - 2*m.x229*m.x235 - 2*m.x230*m.x236
                          - 0.469370231236*m.b23 - 0.469370231236*m.b32 >= -0.469370231236)

m.c594 = Constraint(expr=m.x229**2 + m.x230**2 + m.x235**2 + m.x236**2 - 2*m.x229*m.x235 - 2*m.x230*m.x236
                          - 0.469370231236*m.b24 - 0.469370231236*m.b33 >= -0.469370231236)

m.c595 = Constraint(expr=m.x229**2 + m.x230**2 + m.x235**2 + m.x236**2 - 2*m.x229*m.x235 - 2*m.x230*m.x236
                          - 0.469370231236*m.b25 - 0.469370231236*m.b34 >= -0.469370231236)

m.c596 = Constraint(expr=m.x231**2 + m.x232**2 + m.x235**2 + m.x236**2 - 2*m.x231*m.x235 - 2*m.x232*m.x236
                          - 0.469370231236*m.b26 - 0.469370231236*m.b32 >= -0.469370231236)

m.c597 = Constraint(expr=m.x231**2 + m.x232**2 + m.x235**2 + m.x236**2 - 2*m.x231*m.x235 - 2*m.x232*m.x236
                          - 0.469370231236*m.b27 - 0.469370231236*m.b33 >= -0.469370231236)

m.c598 = Constraint(expr=m.x231**2 + m.x232**2 + m.x235**2 + m.x236**2 - 2*m.x231*m.x235 - 2*m.x232*m.x236
                          - 0.469370231236*m.b28 - 0.469370231236*m.b34 >= -0.469370231236)

m.c599 = Constraint(expr=m.x233**2 + m.x234**2 + m.x235**2 + m.x236**2 - 2*m.x233*m.x235 - 2*m.x234*m.x236
                          - 0.469370231236*m.b29 - 0.469370231236*m.b32 >= -0.469370231236)

m.c600 = Constraint(expr=m.x233**2 + m.x234**2 + m.x235**2 + m.x236**2 - 2*m.x233*m.x235 - 2*m.x234*m.x236
                          - 0.469370231236*m.b30 - 0.469370231236*m.b33 >= -0.469370231236)

m.c601 = Constraint(expr=m.x233**2 + m.x234**2 + m.x235**2 + m.x236**2 - 2*m.x233*m.x235 - 2*m.x234*m.x236
                          - 0.469370231236*m.b31 - 0.469370231236*m.b34 >= -0.469370231236)

m.c602 = Constraint(expr=m.x235**2 + m.x236**2 + m.x237**2 + m.x238**2 - 2*m.x235*m.x237 - 2*m.x236*m.x238
                          - 1.436936830729*m.b32 - 1.436936830729*m.b35 >= -1.436936830729)

m.c603 = Constraint(expr=m.x235**2 + m.x236**2 + m.x237**2 + m.x238**2 - 2*m.x235*m.x237 - 2*m.x236*m.x238
                          - 1.436936830729*m.b33 - 1.436936830729*m.b36 >= -1.436936830729)

m.c604 = Constraint(expr=m.x235**2 + m.x236**2 + m.x237**2 + m.x238**2 - 2*m.x235*m.x237 - 2*m.x236*m.x238
                          - 1.436936830729*m.b34 - 1.436936830729*m.b37 >= -1.436936830729)

m.c605 = Constraint(expr=m.x235**2 + m.x236**2 + m.x239**2 + m.x240**2 - 2*m.x235*m.x239 - 2*m.x236*m.x240
                          - 1.436936830729*m.b32 - 1.436936830729*m.b38 >= -1.436936830729)

m.c606 = Constraint(expr=m.x235**2 + m.x236**2 + m.x239**2 + m.x240**2 - 2*m.x235*m.x239 - 2*m.x236*m.x240
                          - 1.436936830729*m.b33 - 1.436936830729*m.b39 >= -1.436936830729)

m.c607 = Constraint(expr=m.x235**2 + m.x236**2 + m.x239**2 + m.x240**2 - 2*m.x235*m.x239 - 2*m.x236*m.x240
                          - 1.436936830729*m.b34 - 1.436936830729*m.b40 >= -1.436936830729)

m.c608 = Constraint(expr=m.x235**2 + m.x236**2 + m.x241**2 + m.x242**2 - 2*m.x236*m.x242 - 2*m.x235*m.x241
                          - 1.436936830729*m.b32 - 1.436936830729*m.b41 >= -1.436936830729)

m.c609 = Constraint(expr=m.x235**2 + m.x236**2 + m.x241**2 + m.x242**2 - 2*m.x236*m.x242 - 2*m.x235*m.x241
                          - 1.436936830729*m.b33 - 1.436936830729*m.b42 >= -1.436936830729)

m.c610 = Constraint(expr=m.x235**2 + m.x236**2 + m.x241**2 + m.x242**2 - 2*m.x236*m.x242 - 2*m.x235*m.x241
                          - 1.436936830729*m.b34 - 1.436936830729*m.b43 >= -1.436936830729)

m.c611 = Constraint(expr=m.x235**2 + m.x236**2 + m.x243**2 + m.x244**2 - 2*m.x235*m.x243 - 2*m.x236*m.x244
                          - 1.436936830729*m.b32 - 1.436936830729*m.b44 >= -1.436936830729)

m.c612 = Constraint(expr=m.x235**2 + m.x236**2 + m.x243**2 + m.x244**2 - 2*m.x235*m.x243 - 2*m.x236*m.x244
                          - 1.436936830729*m.b33 - 1.436936830729*m.b45 >= -1.436936830729)

m.c613 = Constraint(expr=m.x235**2 + m.x236**2 + m.x243**2 + m.x244**2 - 2*m.x235*m.x243 - 2*m.x236*m.x244
                          - 1.436936830729*m.b34 - 1.436936830729*m.b46 >= -1.436936830729)

m.c614 = Constraint(expr=m.x235**2 + m.x236**2 + m.x245**2 + m.x246**2 - 2*m.x236*m.x246 - 2*m.x235*m.x245
                          - 1.436936830729*m.b32 - 1.436936830729*m.b47 >= -1.436936830729)

m.c615 = Constraint(expr=m.x235**2 + m.x236**2 + m.x245**2 + m.x246**2 - 2*m.x236*m.x246 - 2*m.x235*m.x245
                          - 1.436936830729*m.b33 - 1.436936830729*m.b48 >= -1.436936830729)

m.c616 = Constraint(expr=m.x235**2 + m.x236**2 + m.x245**2 + m.x246**2 - 2*m.x236*m.x246 - 2*m.x235*m.x245
                          - 1.436936830729*m.b34 - 1.436936830729*m.b49 >= -1.436936830729)

m.c617 = Constraint(expr=m.x235**2 + m.x236**2 + m.x247**2 + m.x248**2 - 2*m.x236*m.x248 - 2*m.x235*m.x247
                          - 3.484990776969*m.b32 - 3.484990776969*m.b50 >= -3.484990776969)

m.c618 = Constraint(expr=m.x235**2 + m.x236**2 + m.x247**2 + m.x248**2 - 2*m.x236*m.x248 - 2*m.x235*m.x247
                          - 3.484990776969*m.b33 - 3.484990776969*m.b51 >= -3.484990776969)

m.c619 = Constraint(expr=m.x235**2 + m.x236**2 + m.x247**2 + m.x248**2 - 2*m.x236*m.x248 - 2*m.x235*m.x247
                          - 3.484990776969*m.b34 - 3.484990776969*m.b52 >= -3.484990776969)

m.c620 = Constraint(expr=m.x235**2 + m.x236**2 + m.x249**2 + m.x250**2 - 2*m.x235*m.x249 - 2*m.x236*m.x250
                          - 3.484990776969*m.b32 - 3.484990776969*m.b53 >= -3.484990776969)

m.c621 = Constraint(expr=m.x235**2 + m.x236**2 + m.x249**2 + m.x250**2 - 2*m.x235*m.x249 - 2*m.x236*m.x250
                          - 3.484990776969*m.b33 - 3.484990776969*m.b54 >= -3.484990776969)

m.c622 = Constraint(expr=m.x235**2 + m.x236**2 + m.x249**2 + m.x250**2 - 2*m.x236*m.x250 - 2*m.x235*m.x249
                          - 3.484990776969*m.b34 - 3.484990776969*m.b55 >= -3.484990776969)

m.c623 = Constraint(expr=m.x235**2 + m.x236**2 + m.x251**2 + m.x252**2 - 2*m.x236*m.x252 - 2*m.x235*m.x251
                          - 5.174182750489*m.b32 - 5.174182750489*m.b56 >= -5.174182750489)

m.c624 = Constraint(expr=m.x235**2 + m.x236**2 + m.x251**2 + m.x252**2 - 2*m.x236*m.x252 - 2*m.x235*m.x251
                          - 5.174182750489*m.b33 - 5.174182750489*m.b57 >= -5.174182750489)

m.c625 = Constraint(expr=m.x235**2 + m.x236**2 + m.x251**2 + m.x252**2 - 2*m.x236*m.x252 - 2*m.x235*m.x251
                          - 5.174182750489*m.b34 - 5.174182750489*m.b58 >= -5.174182750489)

m.c626 = Constraint(expr=m.x235**2 + m.x236**2 + m.x253**2 + m.x254**2 - 2*m.x236*m.x254 - 2*m.x235*m.x253
                          - 5.174182750489*m.b32 - 5.174182750489*m.b59 >= -5.174182750489)

m.c627 = Constraint(expr=m.x235**2 + m.x236**2 + m.x253**2 + m.x254**2 - 2*m.x236*m.x254 - 2*m.x235*m.x253
                          - 5.174182750489*m.b33 - 5.174182750489*m.b60 >= -5.174182750489)

m.c628 = Constraint(expr=m.x235**2 + m.x236**2 + m.x253**2 + m.x254**2 - 2*m.x236*m.x254 - 2*m.x235*m.x253
                          - 5.174182750489*m.b34 - 5.174182750489*m.b61 >= -5.174182750489)

m.c629 = Constraint(expr=m.x215**2 + m.x216**2 + m.x237**2 + m.x238**2 - 2*m.x216*m.x238 - 2*m.x215*m.x237
                          - 2.118573403024*m.b2 - 2.118573403024*m.b35 >= -2.118573403024)

m.c630 = Constraint(expr=m.x215**2 + m.x216**2 + m.x237**2 + m.x238**2 - 2*m.x216*m.x238 - 2*m.x215*m.x237
                          - 2.118573403024*m.b3 - 2.118573403024*m.b36 >= -2.118573403024)

m.c631 = Constraint(expr=m.x215**2 + m.x216**2 + m.x237**2 + m.x238**2 - 2*m.x216*m.x238 - 2*m.x215*m.x237
                          - 2.118573403024*m.b4 - 2.118573403024*m.b37 >= -2.118573403024)

m.c632 = Constraint(expr=m.x217**2 + m.x218**2 + m.x237**2 + m.x238**2 - 2*m.x218*m.x238 - 2*m.x217*m.x237
                          - 2.118573403024*m.b5 - 2.118573403024*m.b35 >= -2.118573403024)

m.c633 = Constraint(expr=m.x217**2 + m.x218**2 + m.x237**2 + m.x238**2 - 2*m.x218*m.x238 - 2*m.x217*m.x237
                          - 2.118573403024*m.b6 - 2.118573403024*m.b36 >= -2.118573403024)

m.c634 = Constraint(expr=m.x217**2 + m.x218**2 + m.x237**2 + m.x238**2 - 2*m.x218*m.x238 - 2*m.x217*m.x237
                          - 2.118573403024*m.b7 - 2.118573403024*m.b37 >= -2.118573403024)

m.c635 = Constraint(expr=m.x219**2 + m.x220**2 + m.x237**2 + m.x238**2 - 2*m.x220*m.x238 - 2*m.x219*m.x237
                          - 2.118573403024*m.b8 - 2.118573403024*m.b35 >= -2.118573403024)

m.c636 = Constraint(expr=m.x219**2 + m.x220**2 + m.x237**2 + m.x238**2 - 2*m.x220*m.x238 - 2*m.x219*m.x237
                          - 2.118573403024*m.b9 - 2.118573403024*m.b36 >= -2.118573403024)

m.c637 = Constraint(expr=m.x219**2 + m.x220**2 + m.x237**2 + m.x238**2 - 2*m.x220*m.x238 - 2*m.x219*m.x237
                          - 2.118573403024*m.b10 - 2.118573403024*m.b37 >= -2.118573403024)

m.c638 = Constraint(expr=m.x221**2 + m.x222**2 + m.x237**2 + m.x238**2 - 2*m.x221*m.x237 - 2*m.x222*m.x238
                          - 2.118573403024*m.b11 - 2.118573403024*m.b35 >= -2.118573403024)

m.c639 = Constraint(expr=m.x221**2 + m.x222**2 + m.x237**2 + m.x238**2 - 2*m.x221*m.x237 - 2*m.x222*m.x238
                          - 2.118573403024*m.b12 - 2.118573403024*m.b36 >= -2.118573403024)

m.c640 = Constraint(expr=m.x221**2 + m.x222**2 + m.x237**2 + m.x238**2 - 2*m.x221*m.x237 - 2*m.x222*m.x238
                          - 2.118573403024*m.b13 - 2.118573403024*m.b37 >= -2.118573403024)

m.c641 = Constraint(expr=m.x223**2 + m.x224**2 + m.x237**2 + m.x238**2 - 2*m.x223*m.x237 - 2*m.x224*m.x238
                          - 2.118573403024*m.b14 - 2.118573403024*m.b35 >= -2.118573403024)

m.c642 = Constraint(expr=m.x223**2 + m.x224**2 + m.x237**2 + m.x238**2 - 2*m.x223*m.x237 - 2*m.x224*m.x238
                          - 2.118573403024*m.b15 - 2.118573403024*m.b36 >= -2.118573403024)

m.c643 = Constraint(expr=m.x223**2 + m.x224**2 + m.x237**2 + m.x238**2 - 2*m.x223*m.x237 - 2*m.x224*m.x238
                          - 2.118573403024*m.b16 - 2.118573403024*m.b37 >= -2.118573403024)

m.c644 = Constraint(expr=m.x225**2 + m.x226**2 + m.x237**2 + m.x238**2 - 2*m.x225*m.x237 - 2*m.x226*m.x238
                          - 2.118573403024*m.b17 - 2.118573403024*m.b35 >= -2.118573403024)

m.c645 = Constraint(expr=m.x225**2 + m.x226**2 + m.x237**2 + m.x238**2 - 2*m.x225*m.x237 - 2*m.x226*m.x238
                          - 2.118573403024*m.b18 - 2.118573403024*m.b36 >= -2.118573403024)

m.c646 = Constraint(expr=m.x225**2 + m.x226**2 + m.x237**2 + m.x238**2 - 2*m.x225*m.x237 - 2*m.x226*m.x238
                          - 2.118573403024*m.b19 - 2.118573403024*m.b37 >= -2.118573403024)

m.c647 = Constraint(expr=m.x227**2 + m.x228**2 + m.x237**2 + m.x238**2 - 2*m.x227*m.x237 - 2*m.x228*m.x238
                          - 1.436936830729*m.b20 - 1.436936830729*m.b35 >= -1.436936830729)

m.c648 = Constraint(expr=m.x227**2 + m.x228**2 + m.x237**2 + m.x238**2 - 2*m.x227*m.x237 - 2*m.x228*m.x238
                          - 1.436936830729*m.b21 - 1.436936830729*m.b36 >= -1.436936830729)

m.c649 = Constraint(expr=m.x227**2 + m.x228**2 + m.x237**2 + m.x238**2 - 2*m.x227*m.x237 - 2*m.x228*m.x238
                          - 1.436936830729*m.b22 - 1.436936830729*m.b37 >= -1.436936830729)

m.c650 = Constraint(expr=m.x229**2 + m.x230**2 + m.x237**2 + m.x238**2 - 2*m.x229*m.x237 - 2*m.x230*m.x238
                          - 1.436936830729*m.b23 - 1.436936830729*m.b35 >= -1.436936830729)

m.c651 = Constraint(expr=m.x229**2 + m.x230**2 + m.x237**2 + m.x238**2 - 2*m.x229*m.x237 - 2*m.x230*m.x238
                          - 1.436936830729*m.b24 - 1.436936830729*m.b36 >= -1.436936830729)

m.c652 = Constraint(expr=m.x229**2 + m.x230**2 + m.x237**2 + m.x238**2 - 2*m.x229*m.x237 - 2*m.x230*m.x238
                          - 1.436936830729*m.b25 - 1.436936830729*m.b37 >= -1.436936830729)

m.c653 = Constraint(expr=m.x231**2 + m.x232**2 + m.x237**2 + m.x238**2 - 2*m.x231*m.x237 - 2*m.x232*m.x238
                          - 1.436936830729*m.b26 - 1.436936830729*m.b35 >= -1.436936830729)

m.c654 = Constraint(expr=m.x231**2 + m.x232**2 + m.x237**2 + m.x238**2 - 2*m.x231*m.x237 - 2*m.x232*m.x238
                          - 1.436936830729*m.b27 - 1.436936830729*m.b36 >= -1.436936830729)

m.c655 = Constraint(expr=m.x231**2 + m.x232**2 + m.x237**2 + m.x238**2 - 2*m.x231*m.x237 - 2*m.x232*m.x238
                          - 1.436936830729*m.b28 - 1.436936830729*m.b37 >= -1.436936830729)

m.c656 = Constraint(expr=m.x233**2 + m.x234**2 + m.x237**2 + m.x238**2 - 2*m.x233*m.x237 - 2*m.x234*m.x238
                          - 1.436936830729*m.b29 - 1.436936830729*m.b35 >= -1.436936830729)

m.c657 = Constraint(expr=m.x233**2 + m.x234**2 + m.x237**2 + m.x238**2 - 2*m.x233*m.x237 - 2*m.x234*m.x238
                          - 1.436936830729*m.b30 - 1.436936830729*m.b36 >= -1.436936830729)

m.c658 = Constraint(expr=m.x233**2 + m.x234**2 + m.x237**2 + m.x238**2 - 2*m.x233*m.x237 - 2*m.x234*m.x238
                          - 1.436936830729*m.b31 - 1.436936830729*m.b37 >= -1.436936830729)

m.c659 = Constraint(expr=m.x235**2 + m.x236**2 + m.x237**2 + m.x238**2 - 2*m.x235*m.x237 - 2*m.x236*m.x238
                          - 1.436936830729*m.b32 - 1.436936830729*m.b35 >= -1.436936830729)

m.c660 = Constraint(expr=m.x235**2 + m.x236**2 + m.x237**2 + m.x238**2 - 2*m.x235*m.x237 - 2*m.x236*m.x238
                          - 1.436936830729*m.b33 - 1.436936830729*m.b36 >= -1.436936830729)

m.c661 = Constraint(expr=m.x235**2 + m.x236**2 + m.x237**2 + m.x238**2 - 2*m.x235*m.x237 - 2*m.x236*m.x238
                          - 1.436936830729*m.b34 - 1.436936830729*m.b37 >= -1.436936830729)

m.c662 = Constraint(expr=m.x237**2 + m.x238**2 + m.x239**2 + m.x240**2 - 2*m.x237*m.x239 - 2*m.x238*m.x240
                          - 2.9321082756*m.b35 - 2.9321082756*m.b38 >= -2.9321082756)

m.c663 = Constraint(expr=m.x237**2 + m.x238**2 + m.x239**2 + m.x240**2 - 2*m.x237*m.x239 - 2*m.x238*m.x240
                          - 2.9321082756*m.b36 - 2.9321082756*m.b39 >= -2.9321082756)

m.c664 = Constraint(expr=m.x237**2 + m.x238**2 + m.x239**2 + m.x240**2 - 2*m.x237*m.x239 - 2*m.x238*m.x240
                          - 2.9321082756*m.b37 - 2.9321082756*m.b40 >= -2.9321082756)

m.c665 = Constraint(expr=m.x237**2 + m.x238**2 + m.x241**2 + m.x242**2 - 2*m.x237*m.x241 - 2*m.x238*m.x242
                          - 2.9321082756*m.b35 - 2.9321082756*m.b41 >= -2.9321082756)

m.c666 = Constraint(expr=m.x237**2 + m.x238**2 + m.x241**2 + m.x242**2 - 2*m.x237*m.x241 - 2*m.x238*m.x242
                          - 2.9321082756*m.b36 - 2.9321082756*m.b42 >= -2.9321082756)

m.c667 = Constraint(expr=m.x237**2 + m.x238**2 + m.x241**2 + m.x242**2 - 2*m.x237*m.x241 - 2*m.x238*m.x242
                          - 2.9321082756*m.b37 - 2.9321082756*m.b43 >= -2.9321082756)

m.c668 = Constraint(expr=m.x237**2 + m.x238**2 + m.x243**2 + m.x244**2 - 2*m.x238*m.x244 - 2*m.x237*m.x243
                          - 2.9321082756*m.b35 - 2.9321082756*m.b44 >= -2.9321082756)

m.c669 = Constraint(expr=m.x237**2 + m.x238**2 + m.x243**2 + m.x244**2 - 2*m.x238*m.x244 - 2*m.x237*m.x243
                          - 2.9321082756*m.b36 - 2.9321082756*m.b45 >= -2.9321082756)

m.c670 = Constraint(expr=m.x237**2 + m.x238**2 + m.x243**2 + m.x244**2 - 2*m.x238*m.x244 - 2*m.x237*m.x243
                          - 2.9321082756*m.b37 - 2.9321082756*m.b46 >= -2.9321082756)

m.c671 = Constraint(expr=m.x237**2 + m.x238**2 + m.x245**2 + m.x246**2 - 2*m.x238*m.x246 - 2*m.x237*m.x245
                          - 2.9321082756*m.b35 - 2.9321082756*m.b47 >= -2.9321082756)

m.c672 = Constraint(expr=m.x237**2 + m.x238**2 + m.x245**2 + m.x246**2 - 2*m.x238*m.x246 - 2*m.x237*m.x245
                          - 2.9321082756*m.b36 - 2.9321082756*m.b48 >= -2.9321082756)

m.c673 = Constraint(expr=m.x237**2 + m.x238**2 + m.x245**2 + m.x246**2 - 2*m.x238*m.x246 - 2*m.x237*m.x245
                          - 2.9321082756*m.b37 - 2.9321082756*m.b49 >= -2.9321082756)

m.c674 = Constraint(expr=m.x237**2 + m.x238**2 + m.x247**2 + m.x248**2 - 2*m.x237*m.x247 - 2*m.x238*m.x248
                          - 5.6664469849*m.b35 - 5.6664469849*m.b50 >= -5.6664469849)

m.c675 = Constraint(expr=m.x237**2 + m.x238**2 + m.x247**2 + m.x248**2 - 2*m.x237*m.x247 - 2*m.x238*m.x248
                          - 5.6664469849*m.b36 - 5.6664469849*m.b51 >= -5.6664469849)

m.c676 = Constraint(expr=m.x237**2 + m.x238**2 + m.x247**2 + m.x248**2 - 2*m.x237*m.x247 - 2*m.x238*m.x248
                          - 5.6664469849*m.b37 - 5.6664469849*m.b52 >= -5.6664469849)

m.c677 = Constraint(expr=m.x237**2 + m.x238**2 + m.x249**2 + m.x250**2 - 2*m.x238*m.x250 - 2*m.x237*m.x249
                          - 5.6664469849*m.b35 - 5.6664469849*m.b53 >= -5.6664469849)

m.c678 = Constraint(expr=m.x237**2 + m.x238**2 + m.x249**2 + m.x250**2 - 2*m.x238*m.x250 - 2*m.x237*m.x249
                          - 5.6664469849*m.b36 - 5.6664469849*m.b54 >= -5.6664469849)

m.c679 = Constraint(expr=m.x237**2 + m.x238**2 + m.x249**2 + m.x250**2 - 2*m.x238*m.x250 - 2*m.x237*m.x249
                          - 5.6664469849*m.b37 - 5.6664469849*m.b55 >= -5.6664469849)

m.c680 = Constraint(expr=m.x237**2 + m.x238**2 + m.x251**2 + m.x252**2 - 2*m.x238*m.x252 - 2*m.x237*m.x251
                          - 7.77461689*m.b35 - 7.77461689*m.b56 >= -7.77461689)

m.c681 = Constraint(expr=m.x237**2 + m.x238**2 + m.x251**2 + m.x252**2 - 2*m.x238*m.x252 - 2*m.x237*m.x251
                          - 7.77461689*m.b36 - 7.77461689*m.b57 >= -7.77461689)

m.c682 = Constraint(expr=m.x237**2 + m.x238**2 + m.x251**2 + m.x252**2 - 2*m.x238*m.x252 - 2*m.x237*m.x251
                          - 7.77461689*m.b37 - 7.77461689*m.b58 >= -7.77461689)

m.c683 = Constraint(expr=m.x237**2 + m.x238**2 + m.x253**2 + m.x254**2 - 2*m.x238*m.x254 - 2*m.x237*m.x253
                          - 7.77461689*m.b35 - 7.77461689*m.b59 >= -7.77461689)

m.c684 = Constraint(expr=m.x237**2 + m.x238**2 + m.x253**2 + m.x254**2 - 2*m.x238*m.x254 - 2*m.x237*m.x253
                          - 7.77461689*m.b36 - 7.77461689*m.b60 >= -7.77461689)

m.c685 = Constraint(expr=m.x237**2 + m.x238**2 + m.x253**2 + m.x254**2 - 2*m.x238*m.x254 - 2*m.x237*m.x253
                          - 7.77461689*m.b37 - 7.77461689*m.b61 >= -7.77461689)

m.c686 = Constraint(expr=m.x215**2 + m.x216**2 + m.x239**2 + m.x240**2 - 2*m.x215*m.x239 - 2*m.x216*m.x240
                          - 2.118573403024*m.b2 - 2.118573403024*m.b38 >= -2.118573403024)

m.c687 = Constraint(expr=m.x215**2 + m.x216**2 + m.x239**2 + m.x240**2 - 2*m.x215*m.x239 - 2*m.x216*m.x240
                          - 2.118573403024*m.b3 - 2.118573403024*m.b39 >= -2.118573403024)

m.c688 = Constraint(expr=m.x215**2 + m.x216**2 + m.x239**2 + m.x240**2 - 2*m.x215*m.x239 - 2*m.x216*m.x240
                          - 2.118573403024*m.b4 - 2.118573403024*m.b40 >= -2.118573403024)

m.c689 = Constraint(expr=m.x217**2 + m.x218**2 + m.x239**2 + m.x240**2 - 2*m.x218*m.x240 - 2*m.x217*m.x239
                          - 2.118573403024*m.b5 - 2.118573403024*m.b38 >= -2.118573403024)

m.c690 = Constraint(expr=m.x217**2 + m.x218**2 + m.x239**2 + m.x240**2 - 2*m.x218*m.x240 - 2*m.x217*m.x239
                          - 2.118573403024*m.b6 - 2.118573403024*m.b39 >= -2.118573403024)

m.c691 = Constraint(expr=m.x217**2 + m.x218**2 + m.x239**2 + m.x240**2 - 2*m.x218*m.x240 - 2*m.x217*m.x239
                          - 2.118573403024*m.b7 - 2.118573403024*m.b40 >= -2.118573403024)

m.c692 = Constraint(expr=m.x219**2 + m.x220**2 + m.x239**2 + m.x240**2 - 2*m.x220*m.x240 - 2*m.x219*m.x239
                          - 2.118573403024*m.b8 - 2.118573403024*m.b38 >= -2.118573403024)

m.c693 = Constraint(expr=m.x219**2 + m.x220**2 + m.x239**2 + m.x240**2 - 2*m.x220*m.x240 - 2*m.x219*m.x239
                          - 2.118573403024*m.b9 - 2.118573403024*m.b39 >= -2.118573403024)

m.c694 = Constraint(expr=m.x219**2 + m.x220**2 + m.x239**2 + m.x240**2 - 2*m.x220*m.x240 - 2*m.x219*m.x239
                          - 2.118573403024*m.b10 - 2.118573403024*m.b40 >= -2.118573403024)

m.c695 = Constraint(expr=m.x221**2 + m.x222**2 + m.x239**2 + m.x240**2 - 2*m.x221*m.x239 - 2*m.x222*m.x240
                          - 2.118573403024*m.b11 - 2.118573403024*m.b38 >= -2.118573403024)

m.c696 = Constraint(expr=m.x221**2 + m.x222**2 + m.x239**2 + m.x240**2 - 2*m.x221*m.x239 - 2*m.x222*m.x240
                          - 2.118573403024*m.b12 - 2.118573403024*m.b39 >= -2.118573403024)

m.c697 = Constraint(expr=m.x221**2 + m.x222**2 + m.x239**2 + m.x240**2 - 2*m.x221*m.x239 - 2*m.x222*m.x240
                          - 2.118573403024*m.b13 - 2.118573403024*m.b40 >= -2.118573403024)

m.c698 = Constraint(expr=m.x223**2 + m.x224**2 + m.x239**2 + m.x240**2 - 2*m.x223*m.x239 - 2*m.x224*m.x240
                          - 2.118573403024*m.b14 - 2.118573403024*m.b38 >= -2.118573403024)

m.c699 = Constraint(expr=m.x223**2 + m.x224**2 + m.x239**2 + m.x240**2 - 2*m.x223*m.x239 - 2*m.x224*m.x240
                          - 2.118573403024*m.b15 - 2.118573403024*m.b39 >= -2.118573403024)

m.c700 = Constraint(expr=m.x223**2 + m.x224**2 + m.x239**2 + m.x240**2 - 2*m.x223*m.x239 - 2*m.x224*m.x240
                          - 2.118573403024*m.b16 - 2.118573403024*m.b40 >= -2.118573403024)

m.c701 = Constraint(expr=m.x225**2 + m.x226**2 + m.x239**2 + m.x240**2 - 2*m.x225*m.x239 - 2*m.x226*m.x240
                          - 2.118573403024*m.b17 - 2.118573403024*m.b38 >= -2.118573403024)

m.c702 = Constraint(expr=m.x225**2 + m.x226**2 + m.x239**2 + m.x240**2 - 2*m.x225*m.x239 - 2*m.x226*m.x240
                          - 2.118573403024*m.b18 - 2.118573403024*m.b39 >= -2.118573403024)

m.c703 = Constraint(expr=m.x225**2 + m.x226**2 + m.x239**2 + m.x240**2 - 2*m.x225*m.x239 - 2*m.x226*m.x240
                          - 2.118573403024*m.b19 - 2.118573403024*m.b40 >= -2.118573403024)

m.c704 = Constraint(expr=m.x227**2 + m.x228**2 + m.x239**2 + m.x240**2 - 2*m.x227*m.x239 - 2*m.x228*m.x240
                          - 1.436936830729*m.b20 - 1.436936830729*m.b38 >= -1.436936830729)

m.c705 = Constraint(expr=m.x227**2 + m.x228**2 + m.x239**2 + m.x240**2 - 2*m.x227*m.x239 - 2*m.x228*m.x240
                          - 1.436936830729*m.b21 - 1.436936830729*m.b39 >= -1.436936830729)

m.c706 = Constraint(expr=m.x227**2 + m.x228**2 + m.x239**2 + m.x240**2 - 2*m.x227*m.x239 - 2*m.x228*m.x240
                          - 1.436936830729*m.b22 - 1.436936830729*m.b40 >= -1.436936830729)

m.c707 = Constraint(expr=m.x229**2 + m.x230**2 + m.x239**2 + m.x240**2 - 2*m.x229*m.x239 - 2*m.x230*m.x240
                          - 1.436936830729*m.b23 - 1.436936830729*m.b38 >= -1.436936830729)

m.c708 = Constraint(expr=m.x229**2 + m.x230**2 + m.x239**2 + m.x240**2 - 2*m.x229*m.x239 - 2*m.x230*m.x240
                          - 1.436936830729*m.b24 - 1.436936830729*m.b39 >= -1.436936830729)

m.c709 = Constraint(expr=m.x229**2 + m.x230**2 + m.x239**2 + m.x240**2 - 2*m.x229*m.x239 - 2*m.x230*m.x240
                          - 1.436936830729*m.b25 - 1.436936830729*m.b40 >= -1.436936830729)

m.c710 = Constraint(expr=m.x231**2 + m.x232**2 + m.x239**2 + m.x240**2 - 2*m.x231*m.x239 - 2*m.x232*m.x240
                          - 1.436936830729*m.b26 - 1.436936830729*m.b38 >= -1.436936830729)

m.c711 = Constraint(expr=m.x231**2 + m.x232**2 + m.x239**2 + m.x240**2 - 2*m.x231*m.x239 - 2*m.x232*m.x240
                          - 1.436936830729*m.b27 - 1.436936830729*m.b39 >= -1.436936830729)

m.c712 = Constraint(expr=m.x231**2 + m.x232**2 + m.x239**2 + m.x240**2 - 2*m.x231*m.x239 - 2*m.x232*m.x240
                          - 1.436936830729*m.b28 - 1.436936830729*m.b40 >= -1.436936830729)

m.c713 = Constraint(expr=m.x233**2 + m.x234**2 + m.x239**2 + m.x240**2 - 2*m.x233*m.x239 - 2*m.x234*m.x240
                          - 1.436936830729*m.b29 - 1.436936830729*m.b38 >= -1.436936830729)

m.c714 = Constraint(expr=m.x233**2 + m.x234**2 + m.x239**2 + m.x240**2 - 2*m.x233*m.x239 - 2*m.x234*m.x240
                          - 1.436936830729*m.b30 - 1.436936830729*m.b39 >= -1.436936830729)

m.c715 = Constraint(expr=m.x233**2 + m.x234**2 + m.x239**2 + m.x240**2 - 2*m.x233*m.x239 - 2*m.x234*m.x240
                          - 1.436936830729*m.b31 - 1.436936830729*m.b40 >= -1.436936830729)

m.c716 = Constraint(expr=m.x235**2 + m.x236**2 + m.x239**2 + m.x240**2 - 2*m.x235*m.x239 - 2*m.x236*m.x240
                          - 1.436936830729*m.b32 - 1.436936830729*m.b38 >= -1.436936830729)

m.c717 = Constraint(expr=m.x235**2 + m.x236**2 + m.x239**2 + m.x240**2 - 2*m.x235*m.x239 - 2*m.x236*m.x240
                          - 1.436936830729*m.b33 - 1.436936830729*m.b39 >= -1.436936830729)

m.c718 = Constraint(expr=m.x235**2 + m.x236**2 + m.x239**2 + m.x240**2 - 2*m.x235*m.x239 - 2*m.x236*m.x240
                          - 1.436936830729*m.b34 - 1.436936830729*m.b40 >= -1.436936830729)

m.c719 = Constraint(expr=m.x237**2 + m.x238**2 + m.x239**2 + m.x240**2 - 2*m.x237*m.x239 - 2*m.x238*m.x240
                          - 2.9321082756*m.b35 - 2.9321082756*m.b38 >= -2.9321082756)

m.c720 = Constraint(expr=m.x237**2 + m.x238**2 + m.x239**2 + m.x240**2 - 2*m.x237*m.x239 - 2*m.x238*m.x240
                          - 2.9321082756*m.b36 - 2.9321082756*m.b39 >= -2.9321082756)

m.c721 = Constraint(expr=m.x237**2 + m.x238**2 + m.x239**2 + m.x240**2 - 2*m.x237*m.x239 - 2*m.x238*m.x240
                          - 2.9321082756*m.b37 - 2.9321082756*m.b40 >= -2.9321082756)

m.c722 = Constraint(expr=m.x239**2 + m.x240**2 + m.x241**2 + m.x242**2 - 2*m.x240*m.x242 - 2*m.x239*m.x241
                          - 2.9321082756*m.b38 - 2.9321082756*m.b41 >= -2.9321082756)

m.c723 = Constraint(expr=m.x239**2 + m.x240**2 + m.x241**2 + m.x242**2 - 2*m.x240*m.x242 - 2*m.x239*m.x241
                          - 2.9321082756*m.b39 - 2.9321082756*m.b42 >= -2.9321082756)

m.c724 = Constraint(expr=m.x239**2 + m.x240**2 + m.x241**2 + m.x242**2 - 2*m.x240*m.x242 - 2*m.x239*m.x241
                          - 2.9321082756*m.b40 - 2.9321082756*m.b43 >= -2.9321082756)

m.c725 = Constraint(expr=m.x239**2 + m.x240**2 + m.x243**2 + m.x244**2 - 2*m.x240*m.x244 - 2*m.x239*m.x243
                          - 2.9321082756*m.b38 - 2.9321082756*m.b44 >= -2.9321082756)

m.c726 = Constraint(expr=m.x239**2 + m.x240**2 + m.x243**2 + m.x244**2 - 2*m.x240*m.x244 - 2*m.x239*m.x243
                          - 2.9321082756*m.b39 - 2.9321082756*m.b45 >= -2.9321082756)

m.c727 = Constraint(expr=m.x239**2 + m.x240**2 + m.x243**2 + m.x244**2 - 2*m.x240*m.x244 - 2*m.x239*m.x243
                          - 2.9321082756*m.b40 - 2.9321082756*m.b46 >= -2.9321082756)

m.c728 = Constraint(expr=m.x239**2 + m.x240**2 + m.x245**2 + m.x246**2 - 2*m.x240*m.x246 - 2*m.x239*m.x245
                          - 2.9321082756*m.b38 - 2.9321082756*m.b47 >= -2.9321082756)

m.c729 = Constraint(expr=m.x239**2 + m.x240**2 + m.x245**2 + m.x246**2 - 2*m.x240*m.x246 - 2*m.x239*m.x245
                          - 2.9321082756*m.b39 - 2.9321082756*m.b48 >= -2.9321082756)

m.c730 = Constraint(expr=m.x239**2 + m.x240**2 + m.x245**2 + m.x246**2 - 2*m.x240*m.x246 - 2*m.x239*m.x245
                          - 2.9321082756*m.b40 - 2.9321082756*m.b49 >= -2.9321082756)

m.c731 = Constraint(expr=m.x239**2 + m.x240**2 + m.x247**2 + m.x248**2 - 2*m.x240*m.x248 - 2*m.x239*m.x247
                          - 5.6664469849*m.b38 - 5.6664469849*m.b50 >= -5.6664469849)

m.c732 = Constraint(expr=m.x239**2 + m.x240**2 + m.x247**2 + m.x248**2 - 2*m.x240*m.x248 - 2*m.x239*m.x247
                          - 5.6664469849*m.b39 - 5.6664469849*m.b51 >= -5.6664469849)

m.c733 = Constraint(expr=m.x239**2 + m.x240**2 + m.x247**2 + m.x248**2 - 2*m.x240*m.x248 - 2*m.x239*m.x247
                          - 5.6664469849*m.b40 - 5.6664469849*m.b52 >= -5.6664469849)

m.c734 = Constraint(expr=m.x239**2 + m.x240**2 + m.x249**2 + m.x250**2 - 2*m.x240*m.x250 - 2*m.x239*m.x249
                          - 5.6664469849*m.b38 - 5.6664469849*m.b53 >= -5.6664469849)

m.c735 = Constraint(expr=m.x239**2 + m.x240**2 + m.x249**2 + m.x250**2 - 2*m.x240*m.x250 - 2*m.x239*m.x249
                          - 5.6664469849*m.b39 - 5.6664469849*m.b54 >= -5.6664469849)

m.c736 = Constraint(expr=m.x239**2 + m.x240**2 + m.x249**2 + m.x250**2 - 2*m.x240*m.x250 - 2*m.x239*m.x249
                          - 5.6664469849*m.b40 - 5.6664469849*m.b55 >= -5.6664469849)

m.c737 = Constraint(expr=m.x239**2 + m.x240**2 + m.x251**2 + m.x252**2 - 2*m.x240*m.x252 - 2*m.x239*m.x251
                          - 7.77461689*m.b38 - 7.77461689*m.b56 >= -7.77461689)

m.c738 = Constraint(expr=m.x239**2 + m.x240**2 + m.x251**2 + m.x252**2 - 2*m.x240*m.x252 - 2*m.x239*m.x251
                          - 7.77461689*m.b39 - 7.77461689*m.b57 >= -7.77461689)

m.c739 = Constraint(expr=m.x239**2 + m.x240**2 + m.x251**2 + m.x252**2 - 2*m.x240*m.x252 - 2*m.x239*m.x251
                          - 7.77461689*m.b40 - 7.77461689*m.b58 >= -7.77461689)

m.c740 = Constraint(expr=m.x239**2 + m.x240**2 + m.x253**2 + m.x254**2 - 2*m.x240*m.x254 - 2*m.x239*m.x253
                          - 7.77461689*m.b38 - 7.77461689*m.b59 >= -7.77461689)

m.c741 = Constraint(expr=m.x239**2 + m.x240**2 + m.x253**2 + m.x254**2 - 2*m.x240*m.x254 - 2*m.x239*m.x253
                          - 7.77461689*m.b39 - 7.77461689*m.b60 >= -7.77461689)

m.c742 = Constraint(expr=m.x239**2 + m.x240**2 + m.x253**2 + m.x254**2 - 2*m.x240*m.x254 - 2*m.x239*m.x253
                          - 7.77461689*m.b40 - 7.77461689*m.b61 >= -7.77461689)

m.c743 = Constraint(expr=m.x215**2 + m.x216**2 + m.x241**2 + m.x242**2 - 2*m.x215*m.x241 - 2*m.x216*m.x242
                          - 2.118573403024*m.b2 - 2.118573403024*m.b41 >= -2.118573403024)

m.c744 = Constraint(expr=m.x215**2 + m.x216**2 + m.x241**2 + m.x242**2 - 2*m.x215*m.x241 - 2*m.x216*m.x242
                          - 2.118573403024*m.b3 - 2.118573403024*m.b42 >= -2.118573403024)

m.c745 = Constraint(expr=m.x215**2 + m.x216**2 + m.x241**2 + m.x242**2 - 2*m.x215*m.x241 - 2*m.x216*m.x242
                          - 2.118573403024*m.b4 - 2.118573403024*m.b43 >= -2.118573403024)

m.c746 = Constraint(expr=m.x217**2 + m.x218**2 + m.x241**2 + m.x242**2 - 2*m.x217*m.x241 - 2*m.x218*m.x242
                          - 2.118573403024*m.b5 - 2.118573403024*m.b41 >= -2.118573403024)

m.c747 = Constraint(expr=m.x217**2 + m.x218**2 + m.x241**2 + m.x242**2 - 2*m.x217*m.x241 - 2*m.x218*m.x242
                          - 2.118573403024*m.b6 - 2.118573403024*m.b42 >= -2.118573403024)

m.c748 = Constraint(expr=m.x217**2 + m.x218**2 + m.x241**2 + m.x242**2 - 2*m.x217*m.x241 - 2*m.x218*m.x242
                          - 2.118573403024*m.b7 - 2.118573403024*m.b43 >= -2.118573403024)

m.c749 = Constraint(expr=m.x219**2 + m.x220**2 + m.x241**2 + m.x242**2 - 2*m.x219*m.x241 - 2*m.x220*m.x242
                          - 2.118573403024*m.b8 - 2.118573403024*m.b41 >= -2.118573403024)

m.c750 = Constraint(expr=m.x219**2 + m.x220**2 + m.x241**2 + m.x242**2 - 2*m.x219*m.x241 - 2*m.x220*m.x242
                          - 2.118573403024*m.b9 - 2.118573403024*m.b42 >= -2.118573403024)

m.c751 = Constraint(expr=m.x219**2 + m.x220**2 + m.x241**2 + m.x242**2 - 2*m.x219*m.x241 - 2*m.x220*m.x242
                          - 2.118573403024*m.b10 - 2.118573403024*m.b43 >= -2.118573403024)

m.c752 = Constraint(expr=m.x221**2 + m.x222**2 + m.x241**2 + m.x242**2 - 2*m.x221*m.x241 - 2*m.x222*m.x242
                          - 2.118573403024*m.b11 - 2.118573403024*m.b41 >= -2.118573403024)

m.c753 = Constraint(expr=m.x221**2 + m.x222**2 + m.x241**2 + m.x242**2 - 2*m.x221*m.x241 - 2*m.x222*m.x242
                          - 2.118573403024*m.b12 - 2.118573403024*m.b42 >= -2.118573403024)

m.c754 = Constraint(expr=m.x221**2 + m.x222**2 + m.x241**2 + m.x242**2 - 2*m.x221*m.x241 - 2*m.x222*m.x242
                          - 2.118573403024*m.b13 - 2.118573403024*m.b43 >= -2.118573403024)

m.c755 = Constraint(expr=m.x223**2 + m.x224**2 + m.x241**2 + m.x242**2 - 2*m.x223*m.x241 - 2*m.x224*m.x242
                          - 2.118573403024*m.b14 - 2.118573403024*m.b41 >= -2.118573403024)

m.c756 = Constraint(expr=m.x223**2 + m.x224**2 + m.x241**2 + m.x242**2 - 2*m.x223*m.x241 - 2*m.x224*m.x242
                          - 2.118573403024*m.b15 - 2.118573403024*m.b42 >= -2.118573403024)

m.c757 = Constraint(expr=m.x223**2 + m.x224**2 + m.x241**2 + m.x242**2 - 2*m.x223*m.x241 - 2*m.x224*m.x242
                          - 2.118573403024*m.b16 - 2.118573403024*m.b43 >= -2.118573403024)

m.c758 = Constraint(expr=m.x225**2 + m.x226**2 + m.x241**2 + m.x242**2 - 2*m.x225*m.x241 - 2*m.x226*m.x242
                          - 2.118573403024*m.b17 - 2.118573403024*m.b41 >= -2.118573403024)

m.c759 = Constraint(expr=m.x225**2 + m.x226**2 + m.x241**2 + m.x242**2 - 2*m.x226*m.x242 - 2*m.x225*m.x241
                          - 2.118573403024*m.b18 - 2.118573403024*m.b42 >= -2.118573403024)

m.c760 = Constraint(expr=m.x225**2 + m.x226**2 + m.x241**2 + m.x242**2 - 2*m.x226*m.x242 - 2*m.x225*m.x241
                          - 2.118573403024*m.b19 - 2.118573403024*m.b43 >= -2.118573403024)

m.c761 = Constraint(expr=m.x227**2 + m.x228**2 + m.x241**2 + m.x242**2 - 2*m.x227*m.x241 - 2*m.x228*m.x242
                          - 1.436936830729*m.b20 - 1.436936830729*m.b41 >= -1.436936830729)

m.c762 = Constraint(expr=m.x227**2 + m.x228**2 + m.x241**2 + m.x242**2 - 2*m.x227*m.x241 - 2*m.x228*m.x242
                          - 1.436936830729*m.b21 - 1.436936830729*m.b42 >= -1.436936830729)

m.c763 = Constraint(expr=m.x227**2 + m.x228**2 + m.x241**2 + m.x242**2 - 2*m.x227*m.x241 - 2*m.x228*m.x242
                          - 1.436936830729*m.b22 - 1.436936830729*m.b43 >= -1.436936830729)

m.c764 = Constraint(expr=m.x229**2 + m.x230**2 + m.x241**2 + m.x242**2 - 2*m.x230*m.x242 - 2*m.x229*m.x241
                          - 1.436936830729*m.b23 - 1.436936830729*m.b41 >= -1.436936830729)

m.c765 = Constraint(expr=m.x229**2 + m.x230**2 + m.x241**2 + m.x242**2 - 2*m.x230*m.x242 - 2*m.x229*m.x241
                          - 1.436936830729*m.b24 - 1.436936830729*m.b42 >= -1.436936830729)

m.c766 = Constraint(expr=m.x229**2 + m.x230**2 + m.x241**2 + m.x242**2 - 2*m.x230*m.x242 - 2*m.x229*m.x241
                          - 1.436936830729*m.b25 - 1.436936830729*m.b43 >= -1.436936830729)

m.c767 = Constraint(expr=m.x231**2 + m.x232**2 + m.x241**2 + m.x242**2 - 2*m.x232*m.x242 - 2*m.x231*m.x241
                          - 1.436936830729*m.b26 - 1.436936830729*m.b41 >= -1.436936830729)

m.c768 = Constraint(expr=m.x231**2 + m.x232**2 + m.x241**2 + m.x242**2 - 2*m.x232*m.x242 - 2*m.x231*m.x241
                          - 1.436936830729*m.b27 - 1.436936830729*m.b42 >= -1.436936830729)

m.c769 = Constraint(expr=m.x231**2 + m.x232**2 + m.x241**2 + m.x242**2 - 2*m.x232*m.x242 - 2*m.x231*m.x241
                          - 1.436936830729*m.b28 - 1.436936830729*m.b43 >= -1.436936830729)

m.c770 = Constraint(expr=m.x233**2 + m.x234**2 + m.x241**2 + m.x242**2 - 2*m.x234*m.x242 - 2*m.x233*m.x241
                          - 1.436936830729*m.b29 - 1.436936830729*m.b41 >= -1.436936830729)

m.c771 = Constraint(expr=m.x233**2 + m.x234**2 + m.x241**2 + m.x242**2 - 2*m.x233*m.x241 - 2*m.x234*m.x242
                          - 1.436936830729*m.b30 - 1.436936830729*m.b42 >= -1.436936830729)

m.c772 = Constraint(expr=m.x233**2 + m.x234**2 + m.x241**2 + m.x242**2 - 2*m.x233*m.x241 - 2*m.x234*m.x242
                          - 1.436936830729*m.b31 - 1.436936830729*m.b43 >= -1.436936830729)

m.c773 = Constraint(expr=m.x235**2 + m.x236**2 + m.x241**2 + m.x242**2 - 2*m.x236*m.x242 - 2*m.x235*m.x241
                          - 1.436936830729*m.b32 - 1.436936830729*m.b41 >= -1.436936830729)

m.c774 = Constraint(expr=m.x235**2 + m.x236**2 + m.x241**2 + m.x242**2 - 2*m.x236*m.x242 - 2*m.x235*m.x241
                          - 1.436936830729*m.b33 - 1.436936830729*m.b42 >= -1.436936830729)

m.c775 = Constraint(expr=m.x235**2 + m.x236**2 + m.x241**2 + m.x242**2 - 2*m.x236*m.x242 - 2*m.x235*m.x241
                          - 1.436936830729*m.b34 - 1.436936830729*m.b43 >= -1.436936830729)

m.c776 = Constraint(expr=m.x237**2 + m.x238**2 + m.x241**2 + m.x242**2 - 2*m.x237*m.x241 - 2*m.x238*m.x242
                          - 2.9321082756*m.b35 - 2.9321082756*m.b41 >= -2.9321082756)

m.c777 = Constraint(expr=m.x237**2 + m.x238**2 + m.x241**2 + m.x242**2 - 2*m.x237*m.x241 - 2*m.x238*m.x242
                          - 2.9321082756*m.b36 - 2.9321082756*m.b42 >= -2.9321082756)

m.c778 = Constraint(expr=m.x237**2 + m.x238**2 + m.x241**2 + m.x242**2 - 2*m.x237*m.x241 - 2*m.x238*m.x242
                          - 2.9321082756*m.b37 - 2.9321082756*m.b43 >= -2.9321082756)

m.c779 = Constraint(expr=m.x239**2 + m.x240**2 + m.x241**2 + m.x242**2 - 2*m.x240*m.x242 - 2*m.x239*m.x241
                          - 2.9321082756*m.b38 - 2.9321082756*m.b41 >= -2.9321082756)

m.c780 = Constraint(expr=m.x239**2 + m.x240**2 + m.x241**2 + m.x242**2 - 2*m.x240*m.x242 - 2*m.x239*m.x241
                          - 2.9321082756*m.b39 - 2.9321082756*m.b42 >= -2.9321082756)

m.c781 = Constraint(expr=m.x239**2 + m.x240**2 + m.x241**2 + m.x242**2 - 2*m.x240*m.x242 - 2*m.x239*m.x241
                          - 2.9321082756*m.b40 - 2.9321082756*m.b43 >= -2.9321082756)

m.c782 = Constraint(expr=m.x241**2 + m.x242**2 + m.x243**2 + m.x244**2 - 2*m.x241*m.x243 - 2*m.x242*m.x244
                          - 2.9321082756*m.b41 - 2.9321082756*m.b44 >= -2.9321082756)

m.c783 = Constraint(expr=m.x241**2 + m.x242**2 + m.x243**2 + m.x244**2 - 2*m.x241*m.x243 - 2*m.x242*m.x244
                          - 2.9321082756*m.b42 - 2.9321082756*m.b45 >= -2.9321082756)

m.c784 = Constraint(expr=m.x241**2 + m.x242**2 + m.x243**2 + m.x244**2 - 2*m.x241*m.x243 - 2*m.x242*m.x244
                          - 2.9321082756*m.b43 - 2.9321082756*m.b46 >= -2.9321082756)

m.c785 = Constraint(expr=m.x241**2 + m.x242**2 + m.x245**2 + m.x246**2 - 2*m.x241*m.x245 - 2*m.x242*m.x246
                          - 2.9321082756*m.b41 - 2.9321082756*m.b47 >= -2.9321082756)

m.c786 = Constraint(expr=m.x241**2 + m.x242**2 + m.x245**2 + m.x246**2 - 2*m.x241*m.x245 - 2*m.x242*m.x246
                          - 2.9321082756*m.b42 - 2.9321082756*m.b48 >= -2.9321082756)

m.c787 = Constraint(expr=m.x241**2 + m.x242**2 + m.x245**2 + m.x246**2 - 2*m.x241*m.x245 - 2*m.x242*m.x246
                          - 2.9321082756*m.b43 - 2.9321082756*m.b49 >= -2.9321082756)

m.c788 = Constraint(expr=m.x241**2 + m.x242**2 + m.x247**2 + m.x248**2 - 2*m.x241*m.x247 - 2*m.x242*m.x248
                          - 5.6664469849*m.b41 - 5.6664469849*m.b50 >= -5.6664469849)

m.c789 = Constraint(expr=m.x241**2 + m.x242**2 + m.x247**2 + m.x248**2 - 2*m.x241*m.x247 - 2*m.x242*m.x248
                          - 5.6664469849*m.b42 - 5.6664469849*m.b51 >= -5.6664469849)

m.c790 = Constraint(expr=m.x241**2 + m.x242**2 + m.x247**2 + m.x248**2 - 2*m.x241*m.x247 - 2*m.x242*m.x248
                          - 5.6664469849*m.b43 - 5.6664469849*m.b52 >= -5.6664469849)

m.c791 = Constraint(expr=m.x241**2 + m.x242**2 + m.x249**2 + m.x250**2 - 2*m.x241*m.x249 - 2*m.x242*m.x250
                          - 5.6664469849*m.b41 - 5.6664469849*m.b53 >= -5.6664469849)

m.c792 = Constraint(expr=m.x241**2 + m.x242**2 + m.x249**2 + m.x250**2 - 2*m.x241*m.x249 - 2*m.x242*m.x250
                          - 5.6664469849*m.b42 - 5.6664469849*m.b54 >= -5.6664469849)

m.c793 = Constraint(expr=m.x241**2 + m.x242**2 + m.x249**2 + m.x250**2 - 2*m.x241*m.x249 - 2*m.x242*m.x250
                          - 5.6664469849*m.b43 - 5.6664469849*m.b55 >= -5.6664469849)

m.c794 = Constraint(expr=m.x241**2 + m.x242**2 + m.x251**2 + m.x252**2 - 2*m.x241*m.x251 - 2*m.x242*m.x252
                          - 7.77461689*m.b41 - 7.77461689*m.b56 >= -7.77461689)

m.c795 = Constraint(expr=m.x241**2 + m.x242**2 + m.x251**2 + m.x252**2 - 2*m.x241*m.x251 - 2*m.x242*m.x252
                          - 7.77461689*m.b42 - 7.77461689*m.b57 >= -7.77461689)

m.c796 = Constraint(expr=m.x241**2 + m.x242**2 + m.x251**2 + m.x252**2 - 2*m.x241*m.x251 - 2*m.x242*m.x252
                          - 7.77461689*m.b43 - 7.77461689*m.b58 >= -7.77461689)

m.c797 = Constraint(expr=m.x241**2 + m.x242**2 + m.x253**2 + m.x254**2 - 2*m.x241*m.x253 - 2*m.x242*m.x254
                          - 7.77461689*m.b41 - 7.77461689*m.b59 >= -7.77461689)

m.c798 = Constraint(expr=m.x241**2 + m.x242**2 + m.x253**2 + m.x254**2 - 2*m.x241*m.x253 - 2*m.x242*m.x254
                          - 7.77461689*m.b42 - 7.77461689*m.b60 >= -7.77461689)

m.c799 = Constraint(expr=m.x241**2 + m.x242**2 + m.x253**2 + m.x254**2 - 2*m.x241*m.x253 - 2*m.x242*m.x254
                          - 7.77461689*m.b43 - 7.77461689*m.b61 >= -7.77461689)

m.c800 = Constraint(expr=m.x215**2 + m.x216**2 + m.x243**2 + m.x244**2 - 2*m.x215*m.x243 - 2*m.x216*m.x244
                          - 2.118573403024*m.b2 - 2.118573403024*m.b44 >= -2.118573403024)

m.c801 = Constraint(expr=m.x215**2 + m.x216**2 + m.x243**2 + m.x244**2 - 2*m.x215*m.x243 - 2*m.x216*m.x244
                          - 2.118573403024*m.b3 - 2.118573403024*m.b45 >= -2.118573403024)

m.c802 = Constraint(expr=m.x215**2 + m.x216**2 + m.x243**2 + m.x244**2 - 2*m.x215*m.x243 - 2*m.x216*m.x244
                          - 2.118573403024*m.b4 - 2.118573403024*m.b46 >= -2.118573403024)

m.c803 = Constraint(expr=m.x217**2 + m.x218**2 + m.x243**2 + m.x244**2 - 2*m.x217*m.x243 - 2*m.x218*m.x244
                          - 2.118573403024*m.b5 - 2.118573403024*m.b44 >= -2.118573403024)

m.c804 = Constraint(expr=m.x217**2 + m.x218**2 + m.x243**2 + m.x244**2 - 2*m.x217*m.x243 - 2*m.x218*m.x244
                          - 2.118573403024*m.b6 - 2.118573403024*m.b45 >= -2.118573403024)

m.c805 = Constraint(expr=m.x217**2 + m.x218**2 + m.x243**2 + m.x244**2 - 2*m.x217*m.x243 - 2*m.x218*m.x244
                          - 2.118573403024*m.b7 - 2.118573403024*m.b46 >= -2.118573403024)

m.c806 = Constraint(expr=m.x219**2 + m.x220**2 + m.x243**2 + m.x244**2 - 2*m.x219*m.x243 - 2*m.x220*m.x244
                          - 2.118573403024*m.b8 - 2.118573403024*m.b44 >= -2.118573403024)

m.c807 = Constraint(expr=m.x219**2 + m.x220**2 + m.x243**2 + m.x244**2 - 2*m.x219*m.x243 - 2*m.x220*m.x244
                          - 2.118573403024*m.b9 - 2.118573403024*m.b45 >= -2.118573403024)

m.c808 = Constraint(expr=m.x219**2 + m.x220**2 + m.x243**2 + m.x244**2 - 2*m.x219*m.x243 - 2*m.x220*m.x244
                          - 2.118573403024*m.b10 - 2.118573403024*m.b46 >= -2.118573403024)

m.c809 = Constraint(expr=m.x221**2 + m.x222**2 + m.x243**2 + m.x244**2 - 2*m.x221*m.x243 - 2*m.x222*m.x244
                          - 2.118573403024*m.b11 - 2.118573403024*m.b44 >= -2.118573403024)

m.c810 = Constraint(expr=m.x221**2 + m.x222**2 + m.x243**2 + m.x244**2 - 2*m.x221*m.x243 - 2*m.x222*m.x244
                          - 2.118573403024*m.b12 - 2.118573403024*m.b45 >= -2.118573403024)

m.c811 = Constraint(expr=m.x221**2 + m.x222**2 + m.x243**2 + m.x244**2 - 2*m.x221*m.x243 - 2*m.x222*m.x244
                          - 2.118573403024*m.b13 - 2.118573403024*m.b46 >= -2.118573403024)

m.c812 = Constraint(expr=m.x223**2 + m.x224**2 + m.x243**2 + m.x244**2 - 2*m.x224*m.x244 - 2*m.x223*m.x243
                          - 2.118573403024*m.b14 - 2.118573403024*m.b44 >= -2.118573403024)

m.c813 = Constraint(expr=m.x223**2 + m.x224**2 + m.x243**2 + m.x244**2 - 2*m.x224*m.x244 - 2*m.x223*m.x243
                          - 2.118573403024*m.b15 - 2.118573403024*m.b45 >= -2.118573403024)

m.c814 = Constraint(expr=m.x223**2 + m.x224**2 + m.x243**2 + m.x244**2 - 2*m.x224*m.x244 - 2*m.x223*m.x243
                          - 2.118573403024*m.b16 - 2.118573403024*m.b46 >= -2.118573403024)

m.c815 = Constraint(expr=m.x225**2 + m.x226**2 + m.x243**2 + m.x244**2 - 2*m.x226*m.x244 - 2*m.x225*m.x243
                          - 2.118573403024*m.b17 - 2.118573403024*m.b44 >= -2.118573403024)

m.c816 = Constraint(expr=m.x225**2 + m.x226**2 + m.x243**2 + m.x244**2 - 2*m.x226*m.x244 - 2*m.x225*m.x243
                          - 2.118573403024*m.b18 - 2.118573403024*m.b45 >= -2.118573403024)

m.c817 = Constraint(expr=m.x225**2 + m.x226**2 + m.x243**2 + m.x244**2 - 2*m.x226*m.x244 - 2*m.x225*m.x243
                          - 2.118573403024*m.b19 - 2.118573403024*m.b46 >= -2.118573403024)

m.c818 = Constraint(expr=m.x227**2 + m.x228**2 + m.x243**2 + m.x244**2 - 2*m.x228*m.x244 - 2*m.x227*m.x243
                          - 1.436936830729*m.b20 - 1.436936830729*m.b44 >= -1.436936830729)

m.c819 = Constraint(expr=m.x227**2 + m.x228**2 + m.x243**2 + m.x244**2 - 2*m.x228*m.x244 - 2*m.x227*m.x243
                          - 1.436936830729*m.b21 - 1.436936830729*m.b45 >= -1.436936830729)

m.c820 = Constraint(expr=m.x227**2 + m.x228**2 + m.x243**2 + m.x244**2 - 2*m.x228*m.x244 - 2*m.x227*m.x243
                          - 1.436936830729*m.b22 - 1.436936830729*m.b46 >= -1.436936830729)

m.c821 = Constraint(expr=m.x229**2 + m.x230**2 + m.x243**2 + m.x244**2 - 2*m.x230*m.x244 - 2*m.x229*m.x243
                          - 1.436936830729*m.b23 - 1.436936830729*m.b44 >= -1.436936830729)

m.c822 = Constraint(expr=m.x229**2 + m.x230**2 + m.x243**2 + m.x244**2 - 2*m.x230*m.x244 - 2*m.x229*m.x243
                          - 1.436936830729*m.b24 - 1.436936830729*m.b45 >= -1.436936830729)

m.c823 = Constraint(expr=m.x229**2 + m.x230**2 + m.x243**2 + m.x244**2 - 2*m.x230*m.x244 - 2*m.x229*m.x243
                          - 1.436936830729*m.b25 - 1.436936830729*m.b46 >= -1.436936830729)

m.c824 = Constraint(expr=m.x231**2 + m.x232**2 + m.x243**2 + m.x244**2 - 2*m.x231*m.x243 - 2*m.x232*m.x244
                          - 1.436936830729*m.b26 - 1.436936830729*m.b44 >= -1.436936830729)

m.c825 = Constraint(expr=m.x231**2 + m.x232**2 + m.x243**2 + m.x244**2 - 2*m.x231*m.x243 - 2*m.x232*m.x244
                          - 1.436936830729*m.b27 - 1.436936830729*m.b45 >= -1.436936830729)

m.c826 = Constraint(expr=m.x231**2 + m.x232**2 + m.x243**2 + m.x244**2 - 2*m.x231*m.x243 - 2*m.x232*m.x244
                          - 1.436936830729*m.b28 - 1.436936830729*m.b46 >= -1.436936830729)

m.c827 = Constraint(expr=m.x233**2 + m.x234**2 + m.x243**2 + m.x244**2 - 2*m.x234*m.x244 - 2*m.x233*m.x243
                          - 1.436936830729*m.b29 - 1.436936830729*m.b44 >= -1.436936830729)

m.c828 = Constraint(expr=m.x233**2 + m.x234**2 + m.x243**2 + m.x244**2 - 2*m.x234*m.x244 - 2*m.x233*m.x243
                          - 1.436936830729*m.b30 - 1.436936830729*m.b45 >= -1.436936830729)

m.c829 = Constraint(expr=m.x233**2 + m.x234**2 + m.x243**2 + m.x244**2 - 2*m.x234*m.x244 - 2*m.x233*m.x243
                          - 1.436936830729*m.b31 - 1.436936830729*m.b46 >= -1.436936830729)

m.c830 = Constraint(expr=m.x235**2 + m.x236**2 + m.x243**2 + m.x244**2 - 2*m.x235*m.x243 - 2*m.x236*m.x244
                          - 1.436936830729*m.b32 - 1.436936830729*m.b44 >= -1.436936830729)

m.c831 = Constraint(expr=m.x235**2 + m.x236**2 + m.x243**2 + m.x244**2 - 2*m.x235*m.x243 - 2*m.x236*m.x244
                          - 1.436936830729*m.b33 - 1.436936830729*m.b45 >= -1.436936830729)

m.c832 = Constraint(expr=m.x235**2 + m.x236**2 + m.x243**2 + m.x244**2 - 2*m.x235*m.x243 - 2*m.x236*m.x244
                          - 1.436936830729*m.b34 - 1.436936830729*m.b46 >= -1.436936830729)

m.c833 = Constraint(expr=m.x237**2 + m.x238**2 + m.x243**2 + m.x244**2 - 2*m.x238*m.x244 - 2*m.x237*m.x243
                          - 2.9321082756*m.b35 - 2.9321082756*m.b44 >= -2.9321082756)

m.c834 = Constraint(expr=m.x237**2 + m.x238**2 + m.x243**2 + m.x244**2 - 2*m.x238*m.x244 - 2*m.x237*m.x243
                          - 2.9321082756*m.b36 - 2.9321082756*m.b45 >= -2.9321082756)

m.c835 = Constraint(expr=m.x237**2 + m.x238**2 + m.x243**2 + m.x244**2 - 2*m.x238*m.x244 - 2*m.x237*m.x243
                          - 2.9321082756*m.b37 - 2.9321082756*m.b46 >= -2.9321082756)

m.c836 = Constraint(expr=m.x239**2 + m.x240**2 + m.x243**2 + m.x244**2 - 2*m.x240*m.x244 - 2*m.x239*m.x243
                          - 2.9321082756*m.b38 - 2.9321082756*m.b44 >= -2.9321082756)

m.c837 = Constraint(expr=m.x239**2 + m.x240**2 + m.x243**2 + m.x244**2 - 2*m.x240*m.x244 - 2*m.x239*m.x243
                          - 2.9321082756*m.b39 - 2.9321082756*m.b45 >= -2.9321082756)

m.c838 = Constraint(expr=m.x239**2 + m.x240**2 + m.x243**2 + m.x244**2 - 2*m.x240*m.x244 - 2*m.x239*m.x243
                          - 2.9321082756*m.b40 - 2.9321082756*m.b46 >= -2.9321082756)

m.c839 = Constraint(expr=m.x241**2 + m.x242**2 + m.x243**2 + m.x244**2 - 2*m.x241*m.x243 - 2*m.x242*m.x244
                          - 2.9321082756*m.b41 - 2.9321082756*m.b44 >= -2.9321082756)

m.c840 = Constraint(expr=m.x241**2 + m.x242**2 + m.x243**2 + m.x244**2 - 2*m.x241*m.x243 - 2*m.x242*m.x244
                          - 2.9321082756*m.b42 - 2.9321082756*m.b45 >= -2.9321082756)

m.c841 = Constraint(expr=m.x241**2 + m.x242**2 + m.x243**2 + m.x244**2 - 2*m.x241*m.x243 - 2*m.x242*m.x244
                          - 2.9321082756*m.b43 - 2.9321082756*m.b46 >= -2.9321082756)

m.c842 = Constraint(expr=m.x243**2 + m.x244**2 + m.x245**2 + m.x246**2 - 2*m.x243*m.x245 - 2*m.x244*m.x246
                          - 2.9321082756*m.b44 - 2.9321082756*m.b47 >= -2.9321082756)

m.c843 = Constraint(expr=m.x243**2 + m.x244**2 + m.x245**2 + m.x246**2 - 2*m.x243*m.x245 - 2*m.x244*m.x246
                          - 2.9321082756*m.b45 - 2.9321082756*m.b48 >= -2.9321082756)

m.c844 = Constraint(expr=m.x243**2 + m.x244**2 + m.x245**2 + m.x246**2 - 2*m.x243*m.x245 - 2*m.x244*m.x246
                          - 2.9321082756*m.b46 - 2.9321082756*m.b49 >= -2.9321082756)

m.c845 = Constraint(expr=m.x243**2 + m.x244**2 + m.x247**2 + m.x248**2 - 2*m.x243*m.x247 - 2*m.x244*m.x248
                          - 5.6664469849*m.b44 - 5.6664469849*m.b50 >= -5.6664469849)

m.c846 = Constraint(expr=m.x243**2 + m.x244**2 + m.x247**2 + m.x248**2 - 2*m.x243*m.x247 - 2*m.x244*m.x248
                          - 5.6664469849*m.b45 - 5.6664469849*m.b51 >= -5.6664469849)

m.c847 = Constraint(expr=m.x243**2 + m.x244**2 + m.x247**2 + m.x248**2 - 2*m.x243*m.x247 - 2*m.x244*m.x248
                          - 5.6664469849*m.b46 - 5.6664469849*m.b52 >= -5.6664469849)

m.c848 = Constraint(expr=m.x243**2 + m.x244**2 + m.x249**2 + m.x250**2 - 2*m.x243*m.x249 - 2*m.x244*m.x250
                          - 5.6664469849*m.b44 - 5.6664469849*m.b53 >= -5.6664469849)

m.c849 = Constraint(expr=m.x243**2 + m.x244**2 + m.x249**2 + m.x250**2 - 2*m.x243*m.x249 - 2*m.x244*m.x250
                          - 5.6664469849*m.b45 - 5.6664469849*m.b54 >= -5.6664469849)

m.c850 = Constraint(expr=m.x243**2 + m.x244**2 + m.x249**2 + m.x250**2 - 2*m.x243*m.x249 - 2*m.x244*m.x250
                          - 5.6664469849*m.b46 - 5.6664469849*m.b55 >= -5.6664469849)

m.c851 = Constraint(expr=m.x243**2 + m.x244**2 + m.x251**2 + m.x252**2 - 2*m.x243*m.x251 - 2*m.x244*m.x252
                          - 7.77461689*m.b44 - 7.77461689*m.b56 >= -7.77461689)

m.c852 = Constraint(expr=m.x243**2 + m.x244**2 + m.x251**2 + m.x252**2 - 2*m.x243*m.x251 - 2*m.x244*m.x252
                          - 7.77461689*m.b45 - 7.77461689*m.b57 >= -7.77461689)

m.c853 = Constraint(expr=m.x243**2 + m.x244**2 + m.x251**2 + m.x252**2 - 2*m.x243*m.x251 - 2*m.x244*m.x252
                          - 7.77461689*m.b46 - 7.77461689*m.b58 >= -7.77461689)

m.c854 = Constraint(expr=m.x243**2 + m.x244**2 + m.x253**2 + m.x254**2 - 2*m.x243*m.x253 - 2*m.x244*m.x254
                          - 7.77461689*m.b44 - 7.77461689*m.b59 >= -7.77461689)

m.c855 = Constraint(expr=m.x243**2 + m.x244**2 + m.x253**2 + m.x254**2 - 2*m.x243*m.x253 - 2*m.x244*m.x254
                          - 7.77461689*m.b45 - 7.77461689*m.b60 >= -7.77461689)

m.c856 = Constraint(expr=m.x243**2 + m.x244**2 + m.x253**2 + m.x254**2 - 2*m.x243*m.x253 - 2*m.x244*m.x254
                          - 7.77461689*m.b46 - 7.77461689*m.b61 >= -7.77461689)

m.c857 = Constraint(expr=m.x215**2 + m.x216**2 + m.x245**2 + m.x246**2 - 2*m.x215*m.x245 - 2*m.x216*m.x246
                          - 2.118573403024*m.b2 - 2.118573403024*m.b47 >= -2.118573403024)

m.c858 = Constraint(expr=m.x215**2 + m.x216**2 + m.x245**2 + m.x246**2 - 2*m.x215*m.x245 - 2*m.x216*m.x246
                          - 2.118573403024*m.b3 - 2.118573403024*m.b48 >= -2.118573403024)

m.c859 = Constraint(expr=m.x215**2 + m.x216**2 + m.x245**2 + m.x246**2 - 2*m.x215*m.x245 - 2*m.x216*m.x246
                          - 2.118573403024*m.b4 - 2.118573403024*m.b49 >= -2.118573403024)

m.c860 = Constraint(expr=m.x217**2 + m.x218**2 + m.x245**2 + m.x246**2 - 2*m.x217*m.x245 - 2*m.x218*m.x246
                          - 2.118573403024*m.b5 - 2.118573403024*m.b47 >= -2.118573403024)

m.c861 = Constraint(expr=m.x217**2 + m.x218**2 + m.x245**2 + m.x246**2 - 2*m.x217*m.x245 - 2*m.x218*m.x246
                          - 2.118573403024*m.b6 - 2.118573403024*m.b48 >= -2.118573403024)

m.c862 = Constraint(expr=m.x217**2 + m.x218**2 + m.x245**2 + m.x246**2 - 2*m.x217*m.x245 - 2*m.x218*m.x246
                          - 2.118573403024*m.b7 - 2.118573403024*m.b49 >= -2.118573403024)

m.c863 = Constraint(expr=m.x219**2 + m.x220**2 + m.x245**2 + m.x246**2 - 2*m.x219*m.x245 - 2*m.x220*m.x246
                          - 2.118573403024*m.b8 - 2.118573403024*m.b47 >= -2.118573403024)

m.c864 = Constraint(expr=m.x219**2 + m.x220**2 + m.x245**2 + m.x246**2 - 2*m.x219*m.x245 - 2*m.x220*m.x246
                          - 2.118573403024*m.b9 - 2.118573403024*m.b48 >= -2.118573403024)

m.c865 = Constraint(expr=m.x219**2 + m.x220**2 + m.x245**2 + m.x246**2 - 2*m.x219*m.x245 - 2*m.x220*m.x246
                          - 2.118573403024*m.b10 - 2.118573403024*m.b49 >= -2.118573403024)

m.c866 = Constraint(expr=m.x221**2 + m.x222**2 + m.x245**2 + m.x246**2 - 2*m.x222*m.x246 - 2*m.x221*m.x245
                          - 2.118573403024*m.b11 - 2.118573403024*m.b47 >= -2.118573403024)

m.c867 = Constraint(expr=m.x221**2 + m.x222**2 + m.x245**2 + m.x246**2 - 2*m.x222*m.x246 - 2*m.x221*m.x245
                          - 2.118573403024*m.b12 - 2.118573403024*m.b48 >= -2.118573403024)

m.c868 = Constraint(expr=m.x221**2 + m.x222**2 + m.x245**2 + m.x246**2 - 2*m.x222*m.x246 - 2*m.x221*m.x245
                          - 2.118573403024*m.b13 - 2.118573403024*m.b49 >= -2.118573403024)

m.c869 = Constraint(expr=m.x223**2 + m.x224**2 + m.x245**2 + m.x246**2 - 2*m.x224*m.x246 - 2*m.x223*m.x245
                          - 2.118573403024*m.b14 - 2.118573403024*m.b47 >= -2.118573403024)

m.c870 = Constraint(expr=m.x223**2 + m.x224**2 + m.x245**2 + m.x246**2 - 2*m.x224*m.x246 - 2*m.x223*m.x245
                          - 2.118573403024*m.b15 - 2.118573403024*m.b48 >= -2.118573403024)

m.c871 = Constraint(expr=m.x223**2 + m.x224**2 + m.x245**2 + m.x246**2 - 2*m.x224*m.x246 - 2*m.x223*m.x245
                          - 2.118573403024*m.b16 - 2.118573403024*m.b49 >= -2.118573403024)

m.c872 = Constraint(expr=m.x225**2 + m.x226**2 + m.x245**2 + m.x246**2 - 2*m.x225*m.x245 - 2*m.x226*m.x246
                          - 2.118573403024*m.b17 - 2.118573403024*m.b47 >= -2.118573403024)

m.c873 = Constraint(expr=m.x225**2 + m.x226**2 + m.x245**2 + m.x246**2 - 2*m.x225*m.x245 - 2*m.x226*m.x246
                          - 2.118573403024*m.b18 - 2.118573403024*m.b48 >= -2.118573403024)

m.c874 = Constraint(expr=m.x225**2 + m.x226**2 + m.x245**2 + m.x246**2 - 2*m.x225*m.x245 - 2*m.x226*m.x246
                          - 2.118573403024*m.b19 - 2.118573403024*m.b49 >= -2.118573403024)

m.c875 = Constraint(expr=m.x227**2 + m.x228**2 + m.x245**2 + m.x246**2 - 2*m.x228*m.x246 - 2*m.x227*m.x245
                          - 1.436936830729*m.b20 - 1.436936830729*m.b47 >= -1.436936830729)

m.c876 = Constraint(expr=m.x227**2 + m.x228**2 + m.x245**2 + m.x246**2 - 2*m.x228*m.x246 - 2*m.x227*m.x245
                          - 1.436936830729*m.b21 - 1.436936830729*m.b48 >= -1.436936830729)

m.c877 = Constraint(expr=m.x227**2 + m.x228**2 + m.x245**2 + m.x246**2 - 2*m.x228*m.x246 - 2*m.x227*m.x245
                          - 1.436936830729*m.b22 - 1.436936830729*m.b49 >= -1.436936830729)

m.c878 = Constraint(expr=m.x229**2 + m.x230**2 + m.x245**2 + m.x246**2 - 2*m.x229*m.x245 - 2*m.x230*m.x246
                          - 1.436936830729*m.b23 - 1.436936830729*m.b47 >= -1.436936830729)

m.c879 = Constraint(expr=m.x229**2 + m.x230**2 + m.x245**2 + m.x246**2 - 2*m.x229*m.x245 - 2*m.x230*m.x246
                          - 1.436936830729*m.b24 - 1.436936830729*m.b48 >= -1.436936830729)

m.c880 = Constraint(expr=m.x229**2 + m.x230**2 + m.x245**2 + m.x246**2 - 2*m.x229*m.x245 - 2*m.x230*m.x246
                          - 1.436936830729*m.b25 - 1.436936830729*m.b49 >= -1.436936830729)

m.c881 = Constraint(expr=m.x231**2 + m.x232**2 + m.x245**2 + m.x246**2 - 2*m.x232*m.x246 - 2*m.x231*m.x245
                          - 1.436936830729*m.b26 - 1.436936830729*m.b47 >= -1.436936830729)

m.c882 = Constraint(expr=m.x231**2 + m.x232**2 + m.x245**2 + m.x246**2 - 2*m.x232*m.x246 - 2*m.x231*m.x245
                          - 1.436936830729*m.b27 - 1.436936830729*m.b48 >= -1.436936830729)

m.c883 = Constraint(expr=m.x231**2 + m.x232**2 + m.x245**2 + m.x246**2 - 2*m.x232*m.x246 - 2*m.x231*m.x245
                          - 1.436936830729*m.b28 - 1.436936830729*m.b49 >= -1.436936830729)

m.c884 = Constraint(expr=m.x233**2 + m.x234**2 + m.x245**2 + m.x246**2 - 2*m.x234*m.x246 - 2*m.x233*m.x245
                          - 1.436936830729*m.b29 - 1.436936830729*m.b47 >= -1.436936830729)

m.c885 = Constraint(expr=m.x233**2 + m.x234**2 + m.x245**2 + m.x246**2 - 2*m.x234*m.x246 - 2*m.x233*m.x245
                          - 1.436936830729*m.b30 - 1.436936830729*m.b48 >= -1.436936830729)

m.c886 = Constraint(expr=m.x233**2 + m.x234**2 + m.x245**2 + m.x246**2 - 2*m.x233*m.x245 - 2*m.x234*m.x246
                          - 1.436936830729*m.b31 - 1.436936830729*m.b49 >= -1.436936830729)

m.c887 = Constraint(expr=m.x235**2 + m.x236**2 + m.x245**2 + m.x246**2 - 2*m.x236*m.x246 - 2*m.x235*m.x245
                          - 1.436936830729*m.b32 - 1.436936830729*m.b47 >= -1.436936830729)

m.c888 = Constraint(expr=m.x235**2 + m.x236**2 + m.x245**2 + m.x246**2 - 2*m.x236*m.x246 - 2*m.x235*m.x245
                          - 1.436936830729*m.b33 - 1.436936830729*m.b48 >= -1.436936830729)

m.c889 = Constraint(expr=m.x235**2 + m.x236**2 + m.x245**2 + m.x246**2 - 2*m.x236*m.x246 - 2*m.x235*m.x245
                          - 1.436936830729*m.b34 - 1.436936830729*m.b49 >= -1.436936830729)

m.c890 = Constraint(expr=m.x237**2 + m.x238**2 + m.x245**2 + m.x246**2 - 2*m.x238*m.x246 - 2*m.x237*m.x245
                          - 2.9321082756*m.b35 - 2.9321082756*m.b47 >= -2.9321082756)

m.c891 = Constraint(expr=m.x237**2 + m.x238**2 + m.x245**2 + m.x246**2 - 2*m.x238*m.x246 - 2*m.x237*m.x245
                          - 2.9321082756*m.b36 - 2.9321082756*m.b48 >= -2.9321082756)

m.c892 = Constraint(expr=m.x237**2 + m.x238**2 + m.x245**2 + m.x246**2 - 2*m.x238*m.x246 - 2*m.x237*m.x245
                          - 2.9321082756*m.b37 - 2.9321082756*m.b49 >= -2.9321082756)

m.c893 = Constraint(expr=m.x239**2 + m.x240**2 + m.x245**2 + m.x246**2 - 2*m.x239*m.x245 - 2*m.x240*m.x246
                          - 2.9321082756*m.b38 - 2.9321082756*m.b47 >= -2.9321082756)

m.c894 = Constraint(expr=m.x239**2 + m.x240**2 + m.x245**2 + m.x246**2 - 2*m.x239*m.x245 - 2*m.x240*m.x246
                          - 2.9321082756*m.b39 - 2.9321082756*m.b48 >= -2.9321082756)

m.c895 = Constraint(expr=m.x239**2 + m.x240**2 + m.x245**2 + m.x246**2 - 2*m.x239*m.x245 - 2*m.x240*m.x246
                          - 2.9321082756*m.b40 - 2.9321082756*m.b49 >= -2.9321082756)

m.c896 = Constraint(expr=m.x241**2 + m.x242**2 + m.x245**2 + m.x246**2 - 2*m.x241*m.x245 - 2*m.x242*m.x246
                          - 2.9321082756*m.b41 - 2.9321082756*m.b47 >= -2.9321082756)

m.c897 = Constraint(expr=m.x241**2 + m.x242**2 + m.x245**2 + m.x246**2 - 2*m.x241*m.x245 - 2*m.x242*m.x246
                          - 2.9321082756*m.b42 - 2.9321082756*m.b48 >= -2.9321082756)

m.c898 = Constraint(expr=m.x241**2 + m.x242**2 + m.x245**2 + m.x246**2 - 2*m.x241*m.x245 - 2*m.x242*m.x246
                          - 2.9321082756*m.b43 - 2.9321082756*m.b49 >= -2.9321082756)

m.c899 = Constraint(expr=m.x243**2 + m.x244**2 + m.x245**2 + m.x246**2 - 2*m.x243*m.x245 - 2*m.x244*m.x246
                          - 2.9321082756*m.b44 - 2.9321082756*m.b47 >= -2.9321082756)

m.c900 = Constraint(expr=m.x243**2 + m.x244**2 + m.x245**2 + m.x246**2 - 2*m.x243*m.x245 - 2*m.x244*m.x246
                          - 2.9321082756*m.b45 - 2.9321082756*m.b48 >= -2.9321082756)

m.c901 = Constraint(expr=m.x243**2 + m.x244**2 + m.x245**2 + m.x246**2 - 2*m.x243*m.x245 - 2*m.x244*m.x246
                          - 2.9321082756*m.b46 - 2.9321082756*m.b49 >= -2.9321082756)

m.c902 = Constraint(expr=m.x245**2 + m.x246**2 + m.x247**2 + m.x248**2 - 2*m.x245*m.x247 - 2*m.x246*m.x248
                          - 5.6664469849*m.b47 - 5.6664469849*m.b50 >= -5.6664469849)

m.c903 = Constraint(expr=m.x245**2 + m.x246**2 + m.x247**2 + m.x248**2 - 2*m.x245*m.x247 - 2*m.x246*m.x248
                          - 5.6664469849*m.b48 - 5.6664469849*m.b51 >= -5.6664469849)

m.c904 = Constraint(expr=m.x245**2 + m.x246**2 + m.x247**2 + m.x248**2 - 2*m.x245*m.x247 - 2*m.x246*m.x248
                          - 5.6664469849*m.b49 - 5.6664469849*m.b52 >= -5.6664469849)

m.c905 = Constraint(expr=m.x245**2 + m.x246**2 + m.x249**2 + m.x250**2 - 2*m.x245*m.x249 - 2*m.x246*m.x250
                          - 5.6664469849*m.b47 - 5.6664469849*m.b53 >= -5.6664469849)

m.c906 = Constraint(expr=m.x245**2 + m.x246**2 + m.x249**2 + m.x250**2 - 2*m.x245*m.x249 - 2*m.x246*m.x250
                          - 5.6664469849*m.b48 - 5.6664469849*m.b54 >= -5.6664469849)

m.c907 = Constraint(expr=m.x245**2 + m.x246**2 + m.x249**2 + m.x250**2 - 2*m.x245*m.x249 - 2*m.x246*m.x250
                          - 5.6664469849*m.b49 - 5.6664469849*m.b55 >= -5.6664469849)

m.c908 = Constraint(expr=m.x245**2 + m.x246**2 + m.x251**2 + m.x252**2 - 2*m.x245*m.x251 - 2*m.x246*m.x252
                          - 7.77461689*m.b47 - 7.77461689*m.b56 >= -7.77461689)

m.c909 = Constraint(expr=m.x245**2 + m.x246**2 + m.x251**2 + m.x252**2 - 2*m.x245*m.x251 - 2*m.x246*m.x252
                          - 7.77461689*m.b48 - 7.77461689*m.b57 >= -7.77461689)

m.c910 = Constraint(expr=m.x245**2 + m.x246**2 + m.x251**2 + m.x252**2 - 2*m.x245*m.x251 - 2*m.x246*m.x252
                          - 7.77461689*m.b49 - 7.77461689*m.b58 >= -7.77461689)

m.c911 = Constraint(expr=m.x245**2 + m.x246**2 + m.x253**2 + m.x254**2 - 2*m.x245*m.x253 - 2*m.x246*m.x254
                          - 7.77461689*m.b47 - 7.77461689*m.b59 >= -7.77461689)

m.c912 = Constraint(expr=m.x245**2 + m.x246**2 + m.x253**2 + m.x254**2 - 2*m.x245*m.x253 - 2*m.x246*m.x254
                          - 7.77461689*m.b48 - 7.77461689*m.b60 >= -7.77461689)

m.c913 = Constraint(expr=m.x245**2 + m.x246**2 + m.x253**2 + m.x254**2 - 2*m.x245*m.x253 - 2*m.x246*m.x254
                          - 7.77461689*m.b49 - 7.77461689*m.b61 >= -7.77461689)

m.c914 = Constraint(expr=m.x215**2 + m.x216**2 + m.x247**2 + m.x248**2 - 2*m.x215*m.x247 - 2*m.x216*m.x248
                          - 4.509770398884*m.b2 - 4.509770398884*m.b50 >= -4.509770398884)

m.c915 = Constraint(expr=m.x215**2 + m.x216**2 + m.x247**2 + m.x248**2 - 2*m.x215*m.x247 - 2*m.x216*m.x248
                          - 4.509770398884*m.b3 - 4.509770398884*m.b51 >= -4.509770398884)

m.c916 = Constraint(expr=m.x215**2 + m.x216**2 + m.x247**2 + m.x248**2 - 2*m.x215*m.x247 - 2*m.x216*m.x248
                          - 4.509770398884*m.b4 - 4.509770398884*m.b52 >= -4.509770398884)

m.c917 = Constraint(expr=m.x217**2 + m.x218**2 + m.x247**2 + m.x248**2 - 2*m.x217*m.x247 - 2*m.x218*m.x248
                          - 4.509770398884*m.b5 - 4.509770398884*m.b50 >= -4.509770398884)

m.c918 = Constraint(expr=m.x217**2 + m.x218**2 + m.x247**2 + m.x248**2 - 2*m.x217*m.x247 - 2*m.x218*m.x248
                          - 4.509770398884*m.b6 - 4.509770398884*m.b51 >= -4.509770398884)

m.c919 = Constraint(expr=m.x217**2 + m.x218**2 + m.x247**2 + m.x248**2 - 2*m.x217*m.x247 - 2*m.x218*m.x248
                          - 4.509770398884*m.b7 - 4.509770398884*m.b52 >= -4.509770398884)

m.c920 = Constraint(expr=m.x219**2 + m.x220**2 + m.x247**2 + m.x248**2 - 2*m.x219*m.x247 - 2*m.x220*m.x248
                          - 4.509770398884*m.b8 - 4.509770398884*m.b50 >= -4.509770398884)

m.c921 = Constraint(expr=m.x219**2 + m.x220**2 + m.x247**2 + m.x248**2 - 2*m.x219*m.x247 - 2*m.x220*m.x248
                          - 4.509770398884*m.b9 - 4.509770398884*m.b51 >= -4.509770398884)

m.c922 = Constraint(expr=m.x219**2 + m.x220**2 + m.x247**2 + m.x248**2 - 2*m.x219*m.x247 - 2*m.x220*m.x248
                          - 4.509770398884*m.b10 - 4.509770398884*m.b52 >= -4.509770398884)

m.c923 = Constraint(expr=m.x221**2 + m.x222**2 + m.x247**2 + m.x248**2 - 2*m.x221*m.x247 - 2*m.x222*m.x248
                          - 4.509770398884*m.b11 - 4.509770398884*m.b50 >= -4.509770398884)

m.c924 = Constraint(expr=m.x221**2 + m.x222**2 + m.x247**2 + m.x248**2 - 2*m.x221*m.x247 - 2*m.x222*m.x248
                          - 4.509770398884*m.b12 - 4.509770398884*m.b51 >= -4.509770398884)

m.c925 = Constraint(expr=m.x221**2 + m.x222**2 + m.x247**2 + m.x248**2 - 2*m.x221*m.x247 - 2*m.x222*m.x248
                          - 4.509770398884*m.b13 - 4.509770398884*m.b52 >= -4.509770398884)

m.c926 = Constraint(expr=m.x223**2 + m.x224**2 + m.x247**2 + m.x248**2 - 2*m.x223*m.x247 - 2*m.x224*m.x248
                          - 4.509770398884*m.b14 - 4.509770398884*m.b50 >= -4.509770398884)

m.c927 = Constraint(expr=m.x223**2 + m.x224**2 + m.x247**2 + m.x248**2 - 2*m.x223*m.x247 - 2*m.x224*m.x248
                          - 4.509770398884*m.b15 - 4.509770398884*m.b51 >= -4.509770398884)

m.c928 = Constraint(expr=m.x223**2 + m.x224**2 + m.x247**2 + m.x248**2 - 2*m.x223*m.x247 - 2*m.x224*m.x248
                          - 4.509770398884*m.b16 - 4.509770398884*m.b52 >= -4.509770398884)

m.c929 = Constraint(expr=m.x225**2 + m.x226**2 + m.x247**2 + m.x248**2 - 2*m.x226*m.x248 - 2*m.x225*m.x247
                          - 4.509770398884*m.b17 - 4.509770398884*m.b50 >= -4.509770398884)

m.c930 = Constraint(expr=m.x225**2 + m.x226**2 + m.x247**2 + m.x248**2 - 2*m.x225*m.x247 - 2*m.x226*m.x248
                          - 4.509770398884*m.b18 - 4.509770398884*m.b51 >= -4.509770398884)

m.c931 = Constraint(expr=m.x225**2 + m.x226**2 + m.x247**2 + m.x248**2 - 2*m.x225*m.x247 - 2*m.x226*m.x248
                          - 4.509770398884*m.b19 - 4.509770398884*m.b52 >= -4.509770398884)

m.c932 = Constraint(expr=m.x227**2 + m.x228**2 + m.x247**2 + m.x248**2 - 2*m.x227*m.x247 - 2*m.x228*m.x248
                          - 3.484990776969*m.b20 - 3.484990776969*m.b50 >= -3.484990776969)

m.c933 = Constraint(expr=m.x227**2 + m.x228**2 + m.x247**2 + m.x248**2 - 2*m.x227*m.x247 - 2*m.x228*m.x248
                          - 3.484990776969*m.b21 - 3.484990776969*m.b51 >= -3.484990776969)

m.c934 = Constraint(expr=m.x227**2 + m.x228**2 + m.x247**2 + m.x248**2 - 2*m.x227*m.x247 - 2*m.x228*m.x248
                          - 3.484990776969*m.b22 - 3.484990776969*m.b52 >= -3.484990776969)

m.c935 = Constraint(expr=m.x229**2 + m.x230**2 + m.x247**2 + m.x248**2 - 2*m.x230*m.x248 - 2*m.x229*m.x247
                          - 3.484990776969*m.b23 - 3.484990776969*m.b50 >= -3.484990776969)

m.c936 = Constraint(expr=m.x229**2 + m.x230**2 + m.x247**2 + m.x248**2 - 2*m.x230*m.x248 - 2*m.x229*m.x247
                          - 3.484990776969*m.b24 - 3.484990776969*m.b51 >= -3.484990776969)

m.c937 = Constraint(expr=m.x229**2 + m.x230**2 + m.x247**2 + m.x248**2 - 2*m.x229*m.x247 - 2*m.x230*m.x248
                          - 3.484990776969*m.b25 - 3.484990776969*m.b52 >= -3.484990776969)

m.c938 = Constraint(expr=m.x231**2 + m.x232**2 + m.x247**2 + m.x248**2 - 2*m.x231*m.x247 - 2*m.x232*m.x248
                          - 3.484990776969*m.b26 - 3.484990776969*m.b50 >= -3.484990776969)

m.c939 = Constraint(expr=m.x231**2 + m.x232**2 + m.x247**2 + m.x248**2 - 2*m.x231*m.x247 - 2*m.x232*m.x248
                          - 3.484990776969*m.b27 - 3.484990776969*m.b51 >= -3.484990776969)

m.c940 = Constraint(expr=m.x231**2 + m.x232**2 + m.x247**2 + m.x248**2 - 2*m.x231*m.x247 - 2*m.x232*m.x248
                          - 3.484990776969*m.b28 - 3.484990776969*m.b52 >= -3.484990776969)

m.c941 = Constraint(expr=m.x233**2 + m.x234**2 + m.x247**2 + m.x248**2 - 2*m.x234*m.x248 - 2*m.x233*m.x247
                          - 3.484990776969*m.b29 - 3.484990776969*m.b50 >= -3.484990776969)

m.c942 = Constraint(expr=m.x233**2 + m.x234**2 + m.x247**2 + m.x248**2 - 2*m.x234*m.x248 - 2*m.x233*m.x247
                          - 3.484990776969*m.b30 - 3.484990776969*m.b51 >= -3.484990776969)

m.c943 = Constraint(expr=m.x233**2 + m.x234**2 + m.x247**2 + m.x248**2 - 2*m.x234*m.x248 - 2*m.x233*m.x247
                          - 3.484990776969*m.b31 - 3.484990776969*m.b52 >= -3.484990776969)

m.c944 = Constraint(expr=m.x235**2 + m.x236**2 + m.x247**2 + m.x248**2 - 2*m.x235*m.x247 - 2*m.x236*m.x248
                          - 3.484990776969*m.b32 - 3.484990776969*m.b50 >= -3.484990776969)

m.c945 = Constraint(expr=m.x235**2 + m.x236**2 + m.x247**2 + m.x248**2 - 2*m.x235*m.x247 - 2*m.x236*m.x248
                          - 3.484990776969*m.b33 - 3.484990776969*m.b51 >= -3.484990776969)

m.c946 = Constraint(expr=m.x235**2 + m.x236**2 + m.x247**2 + m.x248**2 - 2*m.x235*m.x247 - 2*m.x236*m.x248
                          - 3.484990776969*m.b34 - 3.484990776969*m.b52 >= -3.484990776969)

m.c947 = Constraint(expr=m.x237**2 + m.x238**2 + m.x247**2 + m.x248**2 - 2*m.x237*m.x247 - 2*m.x238*m.x248
                          - 5.6664469849*m.b35 - 5.6664469849*m.b50 >= -5.6664469849)

m.c948 = Constraint(expr=m.x237**2 + m.x238**2 + m.x247**2 + m.x248**2 - 2*m.x237*m.x247 - 2*m.x238*m.x248
                          - 5.6664469849*m.b36 - 5.6664469849*m.b51 >= -5.6664469849)

m.c949 = Constraint(expr=m.x237**2 + m.x238**2 + m.x247**2 + m.x248**2 - 2*m.x237*m.x247 - 2*m.x238*m.x248
                          - 5.6664469849*m.b37 - 5.6664469849*m.b52 >= -5.6664469849)

m.c950 = Constraint(expr=m.x239**2 + m.x240**2 + m.x247**2 + m.x248**2 - 2*m.x240*m.x248 - 2*m.x239*m.x247
                          - 5.6664469849*m.b38 - 5.6664469849*m.b50 >= -5.6664469849)

m.c951 = Constraint(expr=m.x239**2 + m.x240**2 + m.x247**2 + m.x248**2 - 2*m.x240*m.x248 - 2*m.x239*m.x247
                          - 5.6664469849*m.b39 - 5.6664469849*m.b51 >= -5.6664469849)

m.c952 = Constraint(expr=m.x239**2 + m.x240**2 + m.x247**2 + m.x248**2 - 2*m.x240*m.x248 - 2*m.x239*m.x247
                          - 5.6664469849*m.b40 - 5.6664469849*m.b52 >= -5.6664469849)

m.c953 = Constraint(expr=m.x241**2 + m.x242**2 + m.x247**2 + m.x248**2 - 2*m.x241*m.x247 - 2*m.x242*m.x248
                          - 5.6664469849*m.b41 - 5.6664469849*m.b50 >= -5.6664469849)

m.c954 = Constraint(expr=m.x241**2 + m.x242**2 + m.x247**2 + m.x248**2 - 2*m.x241*m.x247 - 2*m.x242*m.x248
                          - 5.6664469849*m.b42 - 5.6664469849*m.b51 >= -5.6664469849)

m.c955 = Constraint(expr=m.x241**2 + m.x242**2 + m.x247**2 + m.x248**2 - 2*m.x241*m.x247 - 2*m.x242*m.x248
                          - 5.6664469849*m.b43 - 5.6664469849*m.b52 >= -5.6664469849)

m.c956 = Constraint(expr=m.x243**2 + m.x244**2 + m.x247**2 + m.x248**2 - 2*m.x243*m.x247 - 2*m.x244*m.x248
                          - 5.6664469849*m.b44 - 5.6664469849*m.b50 >= -5.6664469849)

m.c957 = Constraint(expr=m.x243**2 + m.x244**2 + m.x247**2 + m.x248**2 - 2*m.x243*m.x247 - 2*m.x244*m.x248
                          - 5.6664469849*m.b45 - 5.6664469849*m.b51 >= -5.6664469849)

m.c958 = Constraint(expr=m.x243**2 + m.x244**2 + m.x247**2 + m.x248**2 - 2*m.x243*m.x247 - 2*m.x244*m.x248
                          - 5.6664469849*m.b46 - 5.6664469849*m.b52 >= -5.6664469849)

m.c959 = Constraint(expr=m.x245**2 + m.x246**2 + m.x247**2 + m.x248**2 - 2*m.x245*m.x247 - 2*m.x246*m.x248
                          - 5.6664469849*m.b47 - 5.6664469849*m.b50 >= -5.6664469849)

m.c960 = Constraint(expr=m.x245**2 + m.x246**2 + m.x247**2 + m.x248**2 - 2*m.x245*m.x247 - 2*m.x246*m.x248
                          - 5.6664469849*m.b48 - 5.6664469849*m.b51 >= -5.6664469849)

m.c961 = Constraint(expr=m.x245**2 + m.x246**2 + m.x247**2 + m.x248**2 - 2*m.x245*m.x247 - 2*m.x246*m.x248
                          - 5.6664469849*m.b49 - 5.6664469849*m.b52 >= -5.6664469849)

m.c962 = Constraint(expr=m.x247**2 + m.x248**2 + m.x249**2 + m.x250**2 - 2*m.x247*m.x249 - 2*m.x248*m.x250
                          - 9.2934741904*m.b50 - 9.2934741904*m.b53 >= -9.2934741904)

m.c963 = Constraint(expr=m.x247**2 + m.x248**2 + m.x249**2 + m.x250**2 - 2*m.x247*m.x249 - 2*m.x248*m.x250
                          - 9.2934741904*m.b51 - 9.2934741904*m.b54 >= -9.2934741904)

m.c964 = Constraint(expr=m.x247**2 + m.x248**2 + m.x249**2 + m.x250**2 - 2*m.x247*m.x249 - 2*m.x248*m.x250
                          - 9.2934741904*m.b52 - 9.2934741904*m.b55 >= -9.2934741904)

m.c965 = Constraint(expr=m.x247**2 + m.x248**2 + m.x251**2 + m.x252**2 - 2*m.x247*m.x251 - 2*m.x248*m.x252
                          - 11.9466318321*m.b50 - 11.9466318321*m.b56 >= -11.9466318321)

m.c966 = Constraint(expr=m.x247**2 + m.x248**2 + m.x251**2 + m.x252**2 - 2*m.x247*m.x251 - 2*m.x248*m.x252
                          - 11.9466318321*m.b51 - 11.9466318321*m.b57 >= -11.9466318321)

m.c967 = Constraint(expr=m.x247**2 + m.x248**2 + m.x251**2 + m.x252**2 - 2*m.x247*m.x251 - 2*m.x248*m.x252
                          - 11.9466318321*m.b52 - 11.9466318321*m.b58 >= -11.9466318321)

m.c968 = Constraint(expr=m.x247**2 + m.x248**2 + m.x253**2 + m.x254**2 - 2*m.x247*m.x253 - 2*m.x248*m.x254
                          - 11.9466318321*m.b50 - 11.9466318321*m.b59 >= -11.9466318321)

m.c969 = Constraint(expr=m.x247**2 + m.x248**2 + m.x253**2 + m.x254**2 - 2*m.x247*m.x253 - 2*m.x248*m.x254
                          - 11.9466318321*m.b51 - 11.9466318321*m.b60 >= -11.9466318321)

m.c970 = Constraint(expr=m.x247**2 + m.x248**2 + m.x253**2 + m.x254**2 - 2*m.x247*m.x253 - 2*m.x248*m.x254
                          - 11.9466318321*m.b52 - 11.9466318321*m.b61 >= -11.9466318321)

m.c971 = Constraint(expr=m.x215**2 + m.x216**2 + m.x249**2 + m.x250**2 - 2*m.x215*m.x249 - 2*m.x216*m.x250
                          - 4.509770398884*m.b2 - 4.509770398884*m.b53 >= -4.509770398884)

m.c972 = Constraint(expr=m.x215**2 + m.x216**2 + m.x249**2 + m.x250**2 - 2*m.x215*m.x249 - 2*m.x216*m.x250
                          - 4.509770398884*m.b3 - 4.509770398884*m.b54 >= -4.509770398884)

m.c973 = Constraint(expr=m.x215**2 + m.x216**2 + m.x249**2 + m.x250**2 - 2*m.x215*m.x249 - 2*m.x216*m.x250
                          - 4.509770398884*m.b4 - 4.509770398884*m.b55 >= -4.509770398884)

m.c974 = Constraint(expr=m.x217**2 + m.x218**2 + m.x249**2 + m.x250**2 - 2*m.x217*m.x249 - 2*m.x218*m.x250
                          - 4.509770398884*m.b5 - 4.509770398884*m.b53 >= -4.509770398884)

m.c975 = Constraint(expr=m.x217**2 + m.x218**2 + m.x249**2 + m.x250**2 - 2*m.x217*m.x249 - 2*m.x218*m.x250
                          - 4.509770398884*m.b6 - 4.509770398884*m.b54 >= -4.509770398884)

m.c976 = Constraint(expr=m.x217**2 + m.x218**2 + m.x249**2 + m.x250**2 - 2*m.x217*m.x249 - 2*m.x218*m.x250
                          - 4.509770398884*m.b7 - 4.509770398884*m.b55 >= -4.509770398884)

m.c977 = Constraint(expr=m.x219**2 + m.x220**2 + m.x249**2 + m.x250**2 - 2*m.x219*m.x249 - 2*m.x220*m.x250
                          - 4.509770398884*m.b8 - 4.509770398884*m.b53 >= -4.509770398884)

m.c978 = Constraint(expr=m.x219**2 + m.x220**2 + m.x249**2 + m.x250**2 - 2*m.x219*m.x249 - 2*m.x220*m.x250
                          - 4.509770398884*m.b9 - 4.509770398884*m.b54 >= -4.509770398884)

m.c979 = Constraint(expr=m.x219**2 + m.x220**2 + m.x249**2 + m.x250**2 - 2*m.x219*m.x249 - 2*m.x220*m.x250
                          - 4.509770398884*m.b10 - 4.509770398884*m.b55 >= -4.509770398884)

m.c980 = Constraint(expr=m.x221**2 + m.x222**2 + m.x249**2 + m.x250**2 - 2*m.x221*m.x249 - 2*m.x222*m.x250
                          - 4.509770398884*m.b11 - 4.509770398884*m.b53 >= -4.509770398884)

m.c981 = Constraint(expr=m.x221**2 + m.x222**2 + m.x249**2 + m.x250**2 - 2*m.x221*m.x249 - 2*m.x222*m.x250
                          - 4.509770398884*m.b12 - 4.509770398884*m.b54 >= -4.509770398884)

m.c982 = Constraint(expr=m.x221**2 + m.x222**2 + m.x249**2 + m.x250**2 - 2*m.x221*m.x249 - 2*m.x222*m.x250
                          - 4.509770398884*m.b13 - 4.509770398884*m.b55 >= -4.509770398884)

m.c983 = Constraint(expr=m.x223**2 + m.x224**2 + m.x249**2 + m.x250**2 - 2*m.x224*m.x250 - 2*m.x223*m.x249
                          - 4.509770398884*m.b14 - 4.509770398884*m.b53 >= -4.509770398884)

m.c984 = Constraint(expr=m.x223**2 + m.x224**2 + m.x249**2 + m.x250**2 - 2*m.x224*m.x250 - 2*m.x223*m.x249
                          - 4.509770398884*m.b15 - 4.509770398884*m.b54 >= -4.509770398884)

m.c985 = Constraint(expr=m.x223**2 + m.x224**2 + m.x249**2 + m.x250**2 - 2*m.x224*m.x250 - 2*m.x223*m.x249
                          - 4.509770398884*m.b16 - 4.509770398884*m.b55 >= -4.509770398884)

m.c986 = Constraint(expr=m.x225**2 + m.x226**2 + m.x249**2 + m.x250**2 - 2*m.x225*m.x249 - 2*m.x226*m.x250
                          - 4.509770398884*m.b17 - 4.509770398884*m.b53 >= -4.509770398884)

m.c987 = Constraint(expr=m.x225**2 + m.x226**2 + m.x249**2 + m.x250**2 - 2*m.x225*m.x249 - 2*m.x226*m.x250
                          - 4.509770398884*m.b18 - 4.509770398884*m.b54 >= -4.509770398884)

m.c988 = Constraint(expr=m.x225**2 + m.x226**2 + m.x249**2 + m.x250**2 - 2*m.x225*m.x249 - 2*m.x226*m.x250
                          - 4.509770398884*m.b19 - 4.509770398884*m.b55 >= -4.509770398884)

m.c989 = Constraint(expr=m.x227**2 + m.x228**2 + m.x249**2 + m.x250**2 - 2*m.x228*m.x250 - 2*m.x227*m.x249
                          - 3.484990776969*m.b20 - 3.484990776969*m.b53 >= -3.484990776969)

m.c990 = Constraint(expr=m.x227**2 + m.x228**2 + m.x249**2 + m.x250**2 - 2*m.x228*m.x250 - 2*m.x227*m.x249
                          - 3.484990776969*m.b21 - 3.484990776969*m.b54 >= -3.484990776969)

m.c991 = Constraint(expr=m.x227**2 + m.x228**2 + m.x249**2 + m.x250**2 - 2*m.x228*m.x250 - 2*m.x227*m.x249
                          - 3.484990776969*m.b22 - 3.484990776969*m.b55 >= -3.484990776969)

m.c992 = Constraint(expr=m.x229**2 + m.x230**2 + m.x249**2 + m.x250**2 - 2*m.x229*m.x249 - 2*m.x230*m.x250
                          - 3.484990776969*m.b23 - 3.484990776969*m.b53 >= -3.484990776969)

m.c993 = Constraint(expr=m.x229**2 + m.x230**2 + m.x249**2 + m.x250**2 - 2*m.x229*m.x249 - 2*m.x230*m.x250
                          - 3.484990776969*m.b24 - 3.484990776969*m.b54 >= -3.484990776969)

m.c994 = Constraint(expr=m.x229**2 + m.x230**2 + m.x249**2 + m.x250**2 - 2*m.x229*m.x249 - 2*m.x230*m.x250
                          - 3.484990776969*m.b25 - 3.484990776969*m.b55 >= -3.484990776969)

m.c995 = Constraint(expr=m.x231**2 + m.x232**2 + m.x249**2 + m.x250**2 - 2*m.x232*m.x250 - 2*m.x231*m.x249
                          - 3.484990776969*m.b26 - 3.484990776969*m.b53 >= -3.484990776969)

m.c996 = Constraint(expr=m.x231**2 + m.x232**2 + m.x249**2 + m.x250**2 - 2*m.x232*m.x250 - 2*m.x231*m.x249
                          - 3.484990776969*m.b27 - 3.484990776969*m.b54 >= -3.484990776969)

m.c997 = Constraint(expr=m.x231**2 + m.x232**2 + m.x249**2 + m.x250**2 - 2*m.x232*m.x250 - 2*m.x231*m.x249
                          - 3.484990776969*m.b28 - 3.484990776969*m.b55 >= -3.484990776969)

m.c998 = Constraint(expr=m.x233**2 + m.x234**2 + m.x249**2 + m.x250**2 - 2*m.x234*m.x250 - 2*m.x233*m.x249
                          - 3.484990776969*m.b29 - 3.484990776969*m.b53 >= -3.484990776969)

m.c999 = Constraint(expr=m.x233**2 + m.x234**2 + m.x249**2 + m.x250**2 - 2*m.x234*m.x250 - 2*m.x233*m.x249
                          - 3.484990776969*m.b30 - 3.484990776969*m.b54 >= -3.484990776969)

m.c1000 = Constraint(expr=m.x233**2 + m.x234**2 + m.x249**2 + m.x250**2 - 2*m.x234*m.x250 - 2*m.x233*m.x249
                           - 3.484990776969*m.b31 - 3.484990776969*m.b55 >= -3.484990776969)

m.c1001 = Constraint(expr=m.x235**2 + m.x236**2 + m.x249**2 + m.x250**2 - 2*m.x235*m.x249 - 2*m.x236*m.x250
                           - 3.484990776969*m.b32 - 3.484990776969*m.b53 >= -3.484990776969)

m.c1002 = Constraint(expr=m.x235**2 + m.x236**2 + m.x249**2 + m.x250**2 - 2*m.x235*m.x249 - 2*m.x236*m.x250
                           - 3.484990776969*m.b33 - 3.484990776969*m.b54 >= -3.484990776969)

m.c1003 = Constraint(expr=m.x235**2 + m.x236**2 + m.x249**2 + m.x250**2 - 2*m.x235*m.x249 - 2*m.x236*m.x250
                           - 3.484990776969*m.b34 - 3.484990776969*m.b55 >= -3.484990776969)

m.c1004 = Constraint(expr=m.x237**2 + m.x238**2 + m.x249**2 + m.x250**2 - 2*m.x238*m.x250 - 2*m.x237*m.x249
                           - 5.6664469849*m.b35 - 5.6664469849*m.b53 >= -5.6664469849)

m.c1005 = Constraint(expr=m.x237**2 + m.x238**2 + m.x249**2 + m.x250**2 - 2*m.x238*m.x250 - 2*m.x237*m.x249
                           - 5.6664469849*m.b36 - 5.6664469849*m.b54 >= -5.6664469849)

m.c1006 = Constraint(expr=m.x237**2 + m.x238**2 + m.x249**2 + m.x250**2 - 2*m.x238*m.x250 - 2*m.x237*m.x249
                           - 5.6664469849*m.b37 - 5.6664469849*m.b55 >= -5.6664469849)

m.c1007 = Constraint(expr=m.x239**2 + m.x240**2 + m.x249**2 + m.x250**2 - 2*m.x240*m.x250 - 2*m.x239*m.x249
                           - 5.6664469849*m.b38 - 5.6664469849*m.b53 >= -5.6664469849)

m.c1008 = Constraint(expr=m.x239**2 + m.x240**2 + m.x249**2 + m.x250**2 - 2*m.x240*m.x250 - 2*m.x239*m.x249
                           - 5.6664469849*m.b39 - 5.6664469849*m.b54 >= -5.6664469849)

m.c1009 = Constraint(expr=m.x239**2 + m.x240**2 + m.x249**2 + m.x250**2 - 2*m.x240*m.x250 - 2*m.x239*m.x249
                           - 5.6664469849*m.b40 - 5.6664469849*m.b55 >= -5.6664469849)

m.c1010 = Constraint(expr=m.x241**2 + m.x242**2 + m.x249**2 + m.x250**2 - 2*m.x241*m.x249 - 2*m.x242*m.x250
                           - 5.6664469849*m.b41 - 5.6664469849*m.b53 >= -5.6664469849)

m.c1011 = Constraint(expr=m.x241**2 + m.x242**2 + m.x249**2 + m.x250**2 - 2*m.x241*m.x249 - 2*m.x242*m.x250
                           - 5.6664469849*m.b42 - 5.6664469849*m.b54 >= -5.6664469849)

m.c1012 = Constraint(expr=m.x241**2 + m.x242**2 + m.x249**2 + m.x250**2 - 2*m.x241*m.x249 - 2*m.x242*m.x250
                           - 5.6664469849*m.b43 - 5.6664469849*m.b55 >= -5.6664469849)

m.c1013 = Constraint(expr=m.x243**2 + m.x244**2 + m.x249**2 + m.x250**2 - 2*m.x243*m.x249 - 2*m.x244*m.x250
                           - 5.6664469849*m.b44 - 5.6664469849*m.b53 >= -5.6664469849)

m.c1014 = Constraint(expr=m.x243**2 + m.x244**2 + m.x249**2 + m.x250**2 - 2*m.x243*m.x249 - 2*m.x244*m.x250
                           - 5.6664469849*m.b45 - 5.6664469849*m.b54 >= -5.6664469849)

m.c1015 = Constraint(expr=m.x243**2 + m.x244**2 + m.x249**2 + m.x250**2 - 2*m.x243*m.x249 - 2*m.x244*m.x250
                           - 5.6664469849*m.b46 - 5.6664469849*m.b55 >= -5.6664469849)

m.c1016 = Constraint(expr=m.x245**2 + m.x246**2 + m.x249**2 + m.x250**2 - 2*m.x245*m.x249 - 2*m.x246*m.x250
                           - 5.6664469849*m.b47 - 5.6664469849*m.b53 >= -5.6664469849)

m.c1017 = Constraint(expr=m.x245**2 + m.x246**2 + m.x249**2 + m.x250**2 - 2*m.x245*m.x249 - 2*m.x246*m.x250
                           - 5.6664469849*m.b48 - 5.6664469849*m.b54 >= -5.6664469849)

m.c1018 = Constraint(expr=m.x245**2 + m.x246**2 + m.x249**2 + m.x250**2 - 2*m.x245*m.x249 - 2*m.x246*m.x250
                           - 5.6664469849*m.b49 - 5.6664469849*m.b55 >= -5.6664469849)

m.c1019 = Constraint(expr=m.x247**2 + m.x248**2 + m.x249**2 + m.x250**2 - 2*m.x247*m.x249 - 2*m.x248*m.x250
                           - 9.2934741904*m.b50 - 9.2934741904*m.b53 >= -9.2934741904)

m.c1020 = Constraint(expr=m.x247**2 + m.x248**2 + m.x249**2 + m.x250**2 - 2*m.x247*m.x249 - 2*m.x248*m.x250
                           - 9.2934741904*m.b51 - 9.2934741904*m.b54 >= -9.2934741904)

m.c1021 = Constraint(expr=m.x247**2 + m.x248**2 + m.x249**2 + m.x250**2 - 2*m.x247*m.x249 - 2*m.x248*m.x250
                           - 9.2934741904*m.b52 - 9.2934741904*m.b55 >= -9.2934741904)

m.c1022 = Constraint(expr=m.x249**2 + m.x250**2 + m.x251**2 + m.x252**2 - 2*m.x249*m.x251 - 2*m.x250*m.x252
                           - 11.9466318321*m.b53 - 11.9466318321*m.b56 >= -11.9466318321)

m.c1023 = Constraint(expr=m.x249**2 + m.x250**2 + m.x251**2 + m.x252**2 - 2*m.x249*m.x251 - 2*m.x250*m.x252
                           - 11.9466318321*m.b54 - 11.9466318321*m.b57 >= -11.9466318321)

m.c1024 = Constraint(expr=m.x249**2 + m.x250**2 + m.x251**2 + m.x252**2 - 2*m.x249*m.x251 - 2*m.x250*m.x252
                           - 11.9466318321*m.b55 - 11.9466318321*m.b58 >= -11.9466318321)

m.c1025 = Constraint(expr=m.x249**2 + m.x250**2 + m.x253**2 + m.x254**2 - 2*m.x249*m.x253 - 2*m.x250*m.x254
                           - 11.9466318321*m.b53 - 11.9466318321*m.b59 >= -11.9466318321)

m.c1026 = Constraint(expr=m.x249**2 + m.x250**2 + m.x253**2 + m.x254**2 - 2*m.x249*m.x253 - 2*m.x250*m.x254
                           - 11.9466318321*m.b54 - 11.9466318321*m.b60 >= -11.9466318321)

m.c1027 = Constraint(expr=m.x249**2 + m.x250**2 + m.x253**2 + m.x254**2 - 2*m.x249*m.x253 - 2*m.x250*m.x254
                           - 11.9466318321*m.b55 - 11.9466318321*m.b61 >= -11.9466318321)

m.c1028 = Constraint(expr=m.x215**2 + m.x216**2 + m.x251**2 + m.x252**2 - 2*m.x215*m.x251 - 2*m.x216*m.x252
                           - 6.408451746064*m.b2 - 6.408451746064*m.b56 >= -6.408451746064)

m.c1029 = Constraint(expr=m.x215**2 + m.x216**2 + m.x251**2 + m.x252**2 - 2*m.x215*m.x251 - 2*m.x216*m.x252
                           - 6.408451746064*m.b3 - 6.408451746064*m.b57 >= -6.408451746064)

m.c1030 = Constraint(expr=m.x215**2 + m.x216**2 + m.x251**2 + m.x252**2 - 2*m.x215*m.x251 - 2*m.x216*m.x252
                           - 6.408451746064*m.b4 - 6.408451746064*m.b58 >= -6.408451746064)

m.c1031 = Constraint(expr=m.x217**2 + m.x218**2 + m.x251**2 + m.x252**2 - 2*m.x217*m.x251 - 2*m.x218*m.x252
                           - 6.408451746064*m.b5 - 6.408451746064*m.b56 >= -6.408451746064)

m.c1032 = Constraint(expr=m.x217**2 + m.x218**2 + m.x251**2 + m.x252**2 - 2*m.x217*m.x251 - 2*m.x218*m.x252
                           - 6.408451746064*m.b6 - 6.408451746064*m.b57 >= -6.408451746064)

m.c1033 = Constraint(expr=m.x217**2 + m.x218**2 + m.x251**2 + m.x252**2 - 2*m.x217*m.x251 - 2*m.x218*m.x252
                           - 6.408451746064*m.b7 - 6.408451746064*m.b58 >= -6.408451746064)

m.c1034 = Constraint(expr=m.x219**2 + m.x220**2 + m.x251**2 + m.x252**2 - 2*m.x219*m.x251 - 2*m.x220*m.x252
                           - 6.408451746064*m.b8 - 6.408451746064*m.b56 >= -6.408451746064)

m.c1035 = Constraint(expr=m.x219**2 + m.x220**2 + m.x251**2 + m.x252**2 - 2*m.x219*m.x251 - 2*m.x220*m.x252
                           - 6.408451746064*m.b9 - 6.408451746064*m.b57 >= -6.408451746064)

m.c1036 = Constraint(expr=m.x219**2 + m.x220**2 + m.x251**2 + m.x252**2 - 2*m.x219*m.x251 - 2*m.x220*m.x252
                           - 6.408451746064*m.b10 - 6.408451746064*m.b58 >= -6.408451746064)

m.c1037 = Constraint(expr=m.x221**2 + m.x222**2 + m.x251**2 + m.x252**2 - 2*m.x221*m.x251 - 2*m.x222*m.x252
                           - 6.408451746064*m.b11 - 6.408451746064*m.b56 >= -6.408451746064)

m.c1038 = Constraint(expr=m.x221**2 + m.x222**2 + m.x251**2 + m.x252**2 - 2*m.x221*m.x251 - 2*m.x222*m.x252
                           - 6.408451746064*m.b12 - 6.408451746064*m.b57 >= -6.408451746064)

m.c1039 = Constraint(expr=m.x221**2 + m.x222**2 + m.x251**2 + m.x252**2 - 2*m.x221*m.x251 - 2*m.x222*m.x252
                           - 6.408451746064*m.b13 - 6.408451746064*m.b58 >= -6.408451746064)

m.c1040 = Constraint(expr=m.x223**2 + m.x224**2 + m.x251**2 + m.x252**2 - 2*m.x223*m.x251 - 2*m.x224*m.x252
                           - 6.408451746064*m.b14 - 6.408451746064*m.b56 >= -6.408451746064)

m.c1041 = Constraint(expr=m.x223**2 + m.x224**2 + m.x251**2 + m.x252**2 - 2*m.x224*m.x252 - 2*m.x223*m.x251
                           - 6.408451746064*m.b15 - 6.408451746064*m.b57 >= -6.408451746064)

m.c1042 = Constraint(expr=m.x223**2 + m.x224**2 + m.x251**2 + m.x252**2 - 2*m.x223*m.x251 - 2*m.x224*m.x252
                           - 6.408451746064*m.b16 - 6.408451746064*m.b58 >= -6.408451746064)

m.c1043 = Constraint(expr=m.x225**2 + m.x226**2 + m.x251**2 + m.x252**2 - 2*m.x226*m.x252 - 2*m.x225*m.x251
                           - 6.408451746064*m.b17 - 6.408451746064*m.b56 >= -6.408451746064)

m.c1044 = Constraint(expr=m.x225**2 + m.x226**2 + m.x251**2 + m.x252**2 - 2*m.x226*m.x252 - 2*m.x225*m.x251
                           - 6.408451746064*m.b18 - 6.408451746064*m.b57 >= -6.408451746064)

m.c1045 = Constraint(expr=m.x225**2 + m.x226**2 + m.x251**2 + m.x252**2 - 2*m.x226*m.x252 - 2*m.x225*m.x251
                           - 6.408451746064*m.b19 - 6.408451746064*m.b58 >= -6.408451746064)

m.c1046 = Constraint(expr=m.x227**2 + m.x228**2 + m.x251**2 + m.x252**2 - 2*m.x227*m.x251 - 2*m.x228*m.x252
                           - 5.174182750489*m.b20 - 5.174182750489*m.b56 >= -5.174182750489)

m.c1047 = Constraint(expr=m.x227**2 + m.x228**2 + m.x251**2 + m.x252**2 - 2*m.x227*m.x251 - 2*m.x228*m.x252
                           - 5.174182750489*m.b21 - 5.174182750489*m.b57 >= -5.174182750489)

m.c1048 = Constraint(expr=m.x227**2 + m.x228**2 + m.x251**2 + m.x252**2 - 2*m.x227*m.x251 - 2*m.x228*m.x252
                           - 5.174182750489*m.b22 - 5.174182750489*m.b58 >= -5.174182750489)

m.c1049 = Constraint(expr=m.x229**2 + m.x230**2 + m.x251**2 + m.x252**2 - 2*m.x230*m.x252 - 2*m.x229*m.x251
                           - 5.174182750489*m.b23 - 5.174182750489*m.b56 >= -5.174182750489)

m.c1050 = Constraint(expr=m.x229**2 + m.x230**2 + m.x251**2 + m.x252**2 - 2*m.x230*m.x252 - 2*m.x229*m.x251
                           - 5.174182750489*m.b24 - 5.174182750489*m.b57 >= -5.174182750489)

m.c1051 = Constraint(expr=m.x229**2 + m.x230**2 + m.x251**2 + m.x252**2 - 2*m.x230*m.x252 - 2*m.x229*m.x251
                           - 5.174182750489*m.b25 - 5.174182750489*m.b58 >= -5.174182750489)

m.c1052 = Constraint(expr=m.x231**2 + m.x232**2 + m.x251**2 + m.x252**2 - 2*m.x231*m.x251 - 2*m.x232*m.x252
                           - 5.174182750489*m.b26 - 5.174182750489*m.b56 >= -5.174182750489)

m.c1053 = Constraint(expr=m.x231**2 + m.x232**2 + m.x251**2 + m.x252**2 - 2*m.x231*m.x251 - 2*m.x232*m.x252
                           - 5.174182750489*m.b27 - 5.174182750489*m.b57 >= -5.174182750489)

m.c1054 = Constraint(expr=m.x231**2 + m.x232**2 + m.x251**2 + m.x252**2 - 2*m.x231*m.x251 - 2*m.x232*m.x252
                           - 5.174182750489*m.b28 - 5.174182750489*m.b58 >= -5.174182750489)

m.c1055 = Constraint(expr=m.x233**2 + m.x234**2 + m.x251**2 + m.x252**2 - 2*m.x233*m.x251 - 2*m.x234*m.x252
                           - 5.174182750489*m.b29 - 5.174182750489*m.b56 >= -5.174182750489)

m.c1056 = Constraint(expr=m.x233**2 + m.x234**2 + m.x251**2 + m.x252**2 - 2*m.x233*m.x251 - 2*m.x234*m.x252
                           - 5.174182750489*m.b30 - 5.174182750489*m.b57 >= -5.174182750489)

m.c1057 = Constraint(expr=m.x233**2 + m.x234**2 + m.x251**2 + m.x252**2 - 2*m.x233*m.x251 - 2*m.x234*m.x252
                           - 5.174182750489*m.b31 - 5.174182750489*m.b58 >= -5.174182750489)

m.c1058 = Constraint(expr=m.x235**2 + m.x236**2 + m.x251**2 + m.x252**2 - 2*m.x236*m.x252 - 2*m.x235*m.x251
                           - 5.174182750489*m.b32 - 5.174182750489*m.b56 >= -5.174182750489)

m.c1059 = Constraint(expr=m.x235**2 + m.x236**2 + m.x251**2 + m.x252**2 - 2*m.x236*m.x252 - 2*m.x235*m.x251
                           - 5.174182750489*m.b33 - 5.174182750489*m.b57 >= -5.174182750489)

m.c1060 = Constraint(expr=m.x235**2 + m.x236**2 + m.x251**2 + m.x252**2 - 2*m.x236*m.x252 - 2*m.x235*m.x251
                           - 5.174182750489*m.b34 - 5.174182750489*m.b58 >= -5.174182750489)

m.c1061 = Constraint(expr=m.x237**2 + m.x238**2 + m.x251**2 + m.x252**2 - 2*m.x238*m.x252 - 2*m.x237*m.x251
                           - 7.77461689*m.b35 - 7.77461689*m.b56 >= -7.77461689)

m.c1062 = Constraint(expr=m.x237**2 + m.x238**2 + m.x251**2 + m.x252**2 - 2*m.x238*m.x252 - 2*m.x237*m.x251
                           - 7.77461689*m.b36 - 7.77461689*m.b57 >= -7.77461689)

m.c1063 = Constraint(expr=m.x237**2 + m.x238**2 + m.x251**2 + m.x252**2 - 2*m.x238*m.x252 - 2*m.x237*m.x251
                           - 7.77461689*m.b37 - 7.77461689*m.b58 >= -7.77461689)

m.c1064 = Constraint(expr=m.x239**2 + m.x240**2 + m.x251**2 + m.x252**2 - 2*m.x240*m.x252 - 2*m.x239*m.x251
                           - 7.77461689*m.b38 - 7.77461689*m.b56 >= -7.77461689)

m.c1065 = Constraint(expr=m.x239**2 + m.x240**2 + m.x251**2 + m.x252**2 - 2*m.x240*m.x252 - 2*m.x239*m.x251
                           - 7.77461689*m.b39 - 7.77461689*m.b57 >= -7.77461689)

m.c1066 = Constraint(expr=m.x239**2 + m.x240**2 + m.x251**2 + m.x252**2 - 2*m.x240*m.x252 - 2*m.x239*m.x251
                           - 7.77461689*m.b40 - 7.77461689*m.b58 >= -7.77461689)

m.c1067 = Constraint(expr=m.x241**2 + m.x242**2 + m.x251**2 + m.x252**2 - 2*m.x241*m.x251 - 2*m.x242*m.x252
                           - 7.77461689*m.b41 - 7.77461689*m.b56 >= -7.77461689)

m.c1068 = Constraint(expr=m.x241**2 + m.x242**2 + m.x251**2 + m.x252**2 - 2*m.x241*m.x251 - 2*m.x242*m.x252
                           - 7.77461689*m.b42 - 7.77461689*m.b57 >= -7.77461689)

m.c1069 = Constraint(expr=m.x241**2 + m.x242**2 + m.x251**2 + m.x252**2 - 2*m.x241*m.x251 - 2*m.x242*m.x252
                           - 7.77461689*m.b43 - 7.77461689*m.b58 >= -7.77461689)

m.c1070 = Constraint(expr=m.x243**2 + m.x244**2 + m.x251**2 + m.x252**2 - 2*m.x243*m.x251 - 2*m.x244*m.x252
                           - 7.77461689*m.b44 - 7.77461689*m.b56 >= -7.77461689)

m.c1071 = Constraint(expr=m.x243**2 + m.x244**2 + m.x251**2 + m.x252**2 - 2*m.x243*m.x251 - 2*m.x244*m.x252
                           - 7.77461689*m.b45 - 7.77461689*m.b57 >= -7.77461689)

m.c1072 = Constraint(expr=m.x243**2 + m.x244**2 + m.x251**2 + m.x252**2 - 2*m.x243*m.x251 - 2*m.x244*m.x252
                           - 7.77461689*m.b46 - 7.77461689*m.b58 >= -7.77461689)

m.c1073 = Constraint(expr=m.x245**2 + m.x246**2 + m.x251**2 + m.x252**2 - 2*m.x245*m.x251 - 2*m.x246*m.x252
                           - 7.77461689*m.b47 - 7.77461689*m.b56 >= -7.77461689)

m.c1074 = Constraint(expr=m.x245**2 + m.x246**2 + m.x251**2 + m.x252**2 - 2*m.x245*m.x251 - 2*m.x246*m.x252
                           - 7.77461689*m.b48 - 7.77461689*m.b57 >= -7.77461689)

m.c1075 = Constraint(expr=m.x245**2 + m.x246**2 + m.x251**2 + m.x252**2 - 2*m.x245*m.x251 - 2*m.x246*m.x252
                           - 7.77461689*m.b49 - 7.77461689*m.b58 >= -7.77461689)

m.c1076 = Constraint(expr=m.x247**2 + m.x248**2 + m.x251**2 + m.x252**2 - 2*m.x247*m.x251 - 2*m.x248*m.x252
                           - 11.9466318321*m.b50 - 11.9466318321*m.b56 >= -11.9466318321)

m.c1077 = Constraint(expr=m.x247**2 + m.x248**2 + m.x251**2 + m.x252**2 - 2*m.x247*m.x251 - 2*m.x248*m.x252
                           - 11.9466318321*m.b51 - 11.9466318321*m.b57 >= -11.9466318321)

m.c1078 = Constraint(expr=m.x247**2 + m.x248**2 + m.x251**2 + m.x252**2 - 2*m.x247*m.x251 - 2*m.x248*m.x252
                           - 11.9466318321*m.b52 - 11.9466318321*m.b58 >= -11.9466318321)

m.c1079 = Constraint(expr=m.x249**2 + m.x250**2 + m.x251**2 + m.x252**2 - 2*m.x249*m.x251 - 2*m.x250*m.x252
                           - 11.9466318321*m.b53 - 11.9466318321*m.b56 >= -11.9466318321)

m.c1080 = Constraint(expr=m.x249**2 + m.x250**2 + m.x251**2 + m.x252**2 - 2*m.x249*m.x251 - 2*m.x250*m.x252
                           - 11.9466318321*m.b54 - 11.9466318321*m.b57 >= -11.9466318321)

m.c1081 = Constraint(expr=m.x249**2 + m.x250**2 + m.x251**2 + m.x252**2 - 2*m.x249*m.x251 - 2*m.x250*m.x252
                           - 11.9466318321*m.b55 - 11.9466318321*m.b58 >= -11.9466318321)

m.c1082 = Constraint(expr=m.x251**2 + m.x252**2 + m.x253**2 + m.x254**2 - 2*m.x251*m.x253 - 2*m.x252*m.x254
                           - 14.9325053476*m.b56 - 14.9325053476*m.b59 >= -14.9325053476)

m.c1083 = Constraint(expr=m.x251**2 + m.x252**2 + m.x253**2 + m.x254**2 - 2*m.x251*m.x253 - 2*m.x252*m.x254
                           - 14.9325053476*m.b57 - 14.9325053476*m.b60 >= -14.9325053476)

m.c1084 = Constraint(expr=m.x251**2 + m.x252**2 + m.x253**2 + m.x254**2 - 2*m.x251*m.x253 - 2*m.x252*m.x254
                           - 14.9325053476*m.b58 - 14.9325053476*m.b61 >= -14.9325053476)

m.c1085 = Constraint(expr=m.x215**2 + m.x216**2 + m.x253**2 + m.x254**2 - 2*m.x215*m.x253 - 2*m.x216*m.x254
                           - 6.408451746064*m.b2 - 6.408451746064*m.b59 >= -6.408451746064)

m.c1086 = Constraint(expr=m.x215**2 + m.x216**2 + m.x253**2 + m.x254**2 - 2*m.x215*m.x253 - 2*m.x216*m.x254
                           - 6.408451746064*m.b3 - 6.408451746064*m.b60 >= -6.408451746064)

m.c1087 = Constraint(expr=m.x215**2 + m.x216**2 + m.x253**2 + m.x254**2 - 2*m.x215*m.x253 - 2*m.x216*m.x254
                           - 6.408451746064*m.b4 - 6.408451746064*m.b61 >= -6.408451746064)

m.c1088 = Constraint(expr=m.x217**2 + m.x218**2 + m.x253**2 + m.x254**2 - 2*m.x217*m.x253 - 2*m.x218*m.x254
                           - 6.408451746064*m.b5 - 6.408451746064*m.b59 >= -6.408451746064)

m.c1089 = Constraint(expr=m.x217**2 + m.x218**2 + m.x253**2 + m.x254**2 - 2*m.x217*m.x253 - 2*m.x218*m.x254
                           - 6.408451746064*m.b6 - 6.408451746064*m.b60 >= -6.408451746064)

m.c1090 = Constraint(expr=m.x217**2 + m.x218**2 + m.x253**2 + m.x254**2 - 2*m.x217*m.x253 - 2*m.x218*m.x254
                           - 6.408451746064*m.b7 - 6.408451746064*m.b61 >= -6.408451746064)

m.c1091 = Constraint(expr=m.x219**2 + m.x220**2 + m.x253**2 + m.x254**2 - 2*m.x219*m.x253 - 2*m.x220*m.x254
                           - 6.408451746064*m.b8 - 6.408451746064*m.b59 >= -6.408451746064)

m.c1092 = Constraint(expr=m.x219**2 + m.x220**2 + m.x253**2 + m.x254**2 - 2*m.x219*m.x253 - 2*m.x220*m.x254
                           - 6.408451746064*m.b9 - 6.408451746064*m.b60 >= -6.408451746064)

m.c1093 = Constraint(expr=m.x219**2 + m.x220**2 + m.x253**2 + m.x254**2 - 2*m.x219*m.x253 - 2*m.x220*m.x254
                           - 6.408451746064*m.b10 - 6.408451746064*m.b61 >= -6.408451746064)

m.c1094 = Constraint(expr=m.x221**2 + m.x222**2 + m.x253**2 + m.x254**2 - 2*m.x221*m.x253 - 2*m.x222*m.x254
                           - 6.408451746064*m.b11 - 6.408451746064*m.b59 >= -6.408451746064)

m.c1095 = Constraint(expr=m.x221**2 + m.x222**2 + m.x253**2 + m.x254**2 - 2*m.x221*m.x253 - 2*m.x222*m.x254
                           - 6.408451746064*m.b12 - 6.408451746064*m.b60 >= -6.408451746064)

m.c1096 = Constraint(expr=m.x221**2 + m.x222**2 + m.x253**2 + m.x254**2 - 2*m.x221*m.x253 - 2*m.x222*m.x254
                           - 6.408451746064*m.b13 - 6.408451746064*m.b61 >= -6.408451746064)

m.c1097 = Constraint(expr=m.x223**2 + m.x224**2 + m.x253**2 + m.x254**2 - 2*m.x224*m.x254 - 2*m.x223*m.x253
                           - 6.408451746064*m.b14 - 6.408451746064*m.b59 >= -6.408451746064)

m.c1098 = Constraint(expr=m.x223**2 + m.x224**2 + m.x253**2 + m.x254**2 - 2*m.x224*m.x254 - 2*m.x223*m.x253
                           - 6.408451746064*m.b15 - 6.408451746064*m.b60 >= -6.408451746064)

m.c1099 = Constraint(expr=m.x223**2 + m.x224**2 + m.x253**2 + m.x254**2 - 2*m.x224*m.x254 - 2*m.x223*m.x253
                           - 6.408451746064*m.b16 - 6.408451746064*m.b61 >= -6.408451746064)

m.c1100 = Constraint(expr=m.x225**2 + m.x226**2 + m.x253**2 + m.x254**2 - 2*m.x225*m.x253 - 2*m.x226*m.x254
                           - 6.408451746064*m.b17 - 6.408451746064*m.b59 >= -6.408451746064)

m.c1101 = Constraint(expr=m.x225**2 + m.x226**2 + m.x253**2 + m.x254**2 - 2*m.x225*m.x253 - 2*m.x226*m.x254
                           - 6.408451746064*m.b18 - 6.408451746064*m.b60 >= -6.408451746064)

m.c1102 = Constraint(expr=m.x225**2 + m.x226**2 + m.x253**2 + m.x254**2 - 2*m.x225*m.x253 - 2*m.x226*m.x254
                           - 6.408451746064*m.b19 - 6.408451746064*m.b61 >= -6.408451746064)

m.c1103 = Constraint(expr=m.x227**2 + m.x228**2 + m.x253**2 + m.x254**2 - 2*m.x228*m.x254 - 2*m.x227*m.x253
                           - 5.174182750489*m.b20 - 5.174182750489*m.b59 >= -5.174182750489)

m.c1104 = Constraint(expr=m.x227**2 + m.x228**2 + m.x253**2 + m.x254**2 - 2*m.x228*m.x254 - 2*m.x227*m.x253
                           - 5.174182750489*m.b21 - 5.174182750489*m.b60 >= -5.174182750489)

m.c1105 = Constraint(expr=m.x227**2 + m.x228**2 + m.x253**2 + m.x254**2 - 2*m.x228*m.x254 - 2*m.x227*m.x253
                           - 5.174182750489*m.b22 - 5.174182750489*m.b61 >= -5.174182750489)

m.c1106 = Constraint(expr=m.x229**2 + m.x230**2 + m.x253**2 + m.x254**2 - 2*m.x230*m.x254 - 2*m.x229*m.x253
                           - 5.174182750489*m.b23 - 5.174182750489*m.b59 >= -5.174182750489)

m.c1107 = Constraint(expr=m.x229**2 + m.x230**2 + m.x253**2 + m.x254**2 - 2*m.x230*m.x254 - 2*m.x229*m.x253
                           - 5.174182750489*m.b24 - 5.174182750489*m.b60 >= -5.174182750489)

m.c1108 = Constraint(expr=m.x229**2 + m.x230**2 + m.x253**2 + m.x254**2 - 2*m.x230*m.x254 - 2*m.x229*m.x253
                           - 5.174182750489*m.b25 - 5.174182750489*m.b61 >= -5.174182750489)

m.c1109 = Constraint(expr=m.x231**2 + m.x232**2 + m.x253**2 + m.x254**2 - 2*m.x231*m.x253 - 2*m.x232*m.x254
                           - 5.174182750489*m.b26 - 5.174182750489*m.b59 >= -5.174182750489)

m.c1110 = Constraint(expr=m.x231**2 + m.x232**2 + m.x253**2 + m.x254**2 - 2*m.x231*m.x253 - 2*m.x232*m.x254
                           - 5.174182750489*m.b27 - 5.174182750489*m.b60 >= -5.174182750489)

m.c1111 = Constraint(expr=m.x231**2 + m.x232**2 + m.x253**2 + m.x254**2 - 2*m.x231*m.x253 - 2*m.x232*m.x254
                           - 5.174182750489*m.b28 - 5.174182750489*m.b61 >= -5.174182750489)

m.c1112 = Constraint(expr=m.x233**2 + m.x234**2 + m.x253**2 + m.x254**2 - 2*m.x234*m.x254 - 2*m.x233*m.x253
                           - 5.174182750489*m.b29 - 5.174182750489*m.b59 >= -5.174182750489)

m.c1113 = Constraint(expr=m.x233**2 + m.x234**2 + m.x253**2 + m.x254**2 - 2*m.x234*m.x254 - 2*m.x233*m.x253
                           - 5.174182750489*m.b30 - 5.174182750489*m.b60 >= -5.174182750489)

m.c1114 = Constraint(expr=m.x233**2 + m.x234**2 + m.x253**2 + m.x254**2 - 2*m.x234*m.x254 - 2*m.x233*m.x253
                           - 5.174182750489*m.b31 - 5.174182750489*m.b61 >= -5.174182750489)

m.c1115 = Constraint(expr=m.x235**2 + m.x236**2 + m.x253**2 + m.x254**2 - 2*m.x236*m.x254 - 2*m.x235*m.x253
                           - 5.174182750489*m.b32 - 5.174182750489*m.b59 >= -5.174182750489)

m.c1116 = Constraint(expr=m.x235**2 + m.x236**2 + m.x253**2 + m.x254**2 - 2*m.x236*m.x254 - 2*m.x235*m.x253
                           - 5.174182750489*m.b33 - 5.174182750489*m.b60 >= -5.174182750489)

m.c1117 = Constraint(expr=m.x235**2 + m.x236**2 + m.x253**2 + m.x254**2 - 2*m.x236*m.x254 - 2*m.x235*m.x253
                           - 5.174182750489*m.b34 - 5.174182750489*m.b61 >= -5.174182750489)

m.c1118 = Constraint(expr=m.x237**2 + m.x238**2 + m.x253**2 + m.x254**2 - 2*m.x238*m.x254 - 2*m.x237*m.x253
                           - 7.77461689*m.b35 - 7.77461689*m.b59 >= -7.77461689)

m.c1119 = Constraint(expr=m.x237**2 + m.x238**2 + m.x253**2 + m.x254**2 - 2*m.x238*m.x254 - 2*m.x237*m.x253
                           - 7.77461689*m.b36 - 7.77461689*m.b60 >= -7.77461689)

m.c1120 = Constraint(expr=m.x237**2 + m.x238**2 + m.x253**2 + m.x254**2 - 2*m.x238*m.x254 - 2*m.x237*m.x253
                           - 7.77461689*m.b37 - 7.77461689*m.b61 >= -7.77461689)

m.c1121 = Constraint(expr=m.x239**2 + m.x240**2 + m.x253**2 + m.x254**2 - 2*m.x240*m.x254 - 2*m.x239*m.x253
                           - 7.77461689*m.b38 - 7.77461689*m.b59 >= -7.77461689)

m.c1122 = Constraint(expr=m.x239**2 + m.x240**2 + m.x253**2 + m.x254**2 - 2*m.x240*m.x254 - 2*m.x239*m.x253
                           - 7.77461689*m.b39 - 7.77461689*m.b60 >= -7.77461689)

m.c1123 = Constraint(expr=m.x239**2 + m.x240**2 + m.x253**2 + m.x254**2 - 2*m.x240*m.x254 - 2*m.x239*m.x253
                           - 7.77461689*m.b40 - 7.77461689*m.b61 >= -7.77461689)

m.c1124 = Constraint(expr=m.x241**2 + m.x242**2 + m.x253**2 + m.x254**2 - 2*m.x241*m.x253 - 2*m.x242*m.x254
                           - 7.77461689*m.b41 - 7.77461689*m.b59 >= -7.77461689)

m.c1125 = Constraint(expr=m.x241**2 + m.x242**2 + m.x253**2 + m.x254**2 - 2*m.x241*m.x253 - 2*m.x242*m.x254
                           - 7.77461689*m.b42 - 7.77461689*m.b60 >= -7.77461689)

m.c1126 = Constraint(expr=m.x241**2 + m.x242**2 + m.x253**2 + m.x254**2 - 2*m.x241*m.x253 - 2*m.x242*m.x254
                           - 7.77461689*m.b43 - 7.77461689*m.b61 >= -7.77461689)

m.c1127 = Constraint(expr=m.x243**2 + m.x244**2 + m.x253**2 + m.x254**2 - 2*m.x243*m.x253 - 2*m.x244*m.x254
                           - 7.77461689*m.b44 - 7.77461689*m.b59 >= -7.77461689)

m.c1128 = Constraint(expr=m.x243**2 + m.x244**2 + m.x253**2 + m.x254**2 - 2*m.x243*m.x253 - 2*m.x244*m.x254
                           - 7.77461689*m.b45 - 7.77461689*m.b60 >= -7.77461689)

m.c1129 = Constraint(expr=m.x243**2 + m.x244**2 + m.x253**2 + m.x254**2 - 2*m.x243*m.x253 - 2*m.x244*m.x254
                           - 7.77461689*m.b46 - 7.77461689*m.b61 >= -7.77461689)

m.c1130 = Constraint(expr=m.x245**2 + m.x246**2 + m.x253**2 + m.x254**2 - 2*m.x245*m.x253 - 2*m.x246*m.x254
                           - 7.77461689*m.b47 - 7.77461689*m.b59 >= -7.77461689)

m.c1131 = Constraint(expr=m.x245**2 + m.x246**2 + m.x253**2 + m.x254**2 - 2*m.x245*m.x253 - 2*m.x246*m.x254
                           - 7.77461689*m.b48 - 7.77461689*m.b60 >= -7.77461689)

m.c1132 = Constraint(expr=m.x245**2 + m.x246**2 + m.x253**2 + m.x254**2 - 2*m.x245*m.x253 - 2*m.x246*m.x254
                           - 7.77461689*m.b49 - 7.77461689*m.b61 >= -7.77461689)

m.c1133 = Constraint(expr=m.x247**2 + m.x248**2 + m.x253**2 + m.x254**2 - 2*m.x247*m.x253 - 2*m.x248*m.x254
                           - 11.9466318321*m.b50 - 11.9466318321*m.b59 >= -11.9466318321)

m.c1134 = Constraint(expr=m.x247**2 + m.x248**2 + m.x253**2 + m.x254**2 - 2*m.x247*m.x253 - 2*m.x248*m.x254
                           - 11.9466318321*m.b51 - 11.9466318321*m.b60 >= -11.9466318321)

m.c1135 = Constraint(expr=m.x247**2 + m.x248**2 + m.x253**2 + m.x254**2 - 2*m.x247*m.x253 - 2*m.x248*m.x254
                           - 11.9466318321*m.b52 - 11.9466318321*m.b61 >= -11.9466318321)

m.c1136 = Constraint(expr=m.x249**2 + m.x250**2 + m.x253**2 + m.x254**2 - 2*m.x249*m.x253 - 2*m.x250*m.x254
                           - 11.9466318321*m.b53 - 11.9466318321*m.b59 >= -11.9466318321)

m.c1137 = Constraint(expr=m.x249**2 + m.x250**2 + m.x253**2 + m.x254**2 - 2*m.x249*m.x253 - 2*m.x250*m.x254
                           - 11.9466318321*m.b54 - 11.9466318321*m.b60 >= -11.9466318321)

m.c1138 = Constraint(expr=m.x249**2 + m.x250**2 + m.x253**2 + m.x254**2 - 2*m.x249*m.x253 - 2*m.x250*m.x254
                           - 11.9466318321*m.b55 - 11.9466318321*m.b61 >= -11.9466318321)

m.c1139 = Constraint(expr=m.x251**2 + m.x252**2 + m.x253**2 + m.x254**2 - 2*m.x251*m.x253 - 2*m.x252*m.x254
                           - 14.9325053476*m.b56 - 14.9325053476*m.b59 >= -14.9325053476)

m.c1140 = Constraint(expr=m.x251**2 + m.x252**2 + m.x253**2 + m.x254**2 - 2*m.x251*m.x253 - 2*m.x252*m.x254
                           - 14.9325053476*m.b57 - 14.9325053476*m.b60 >= -14.9325053476)

m.c1141 = Constraint(expr=m.x251**2 + m.x252**2 + m.x253**2 + m.x254**2 - 2*m.x251*m.x253 - 2*m.x252*m.x254
                           - 14.9325053476*m.b58 - 14.9325053476*m.b61 >= -14.9325053476)

m.c1142 = Constraint(expr=m.x227**2 + m.x228**2 + m.x229**2 + m.x230**2 - 2*m.x227*m.x229 - 2*m.x228*m.x230
                           - 0.469370231236*m.b116 - 0.469370231236*m.b131 >= -0.469370231236)

m.c1143 = Constraint(expr=m.x227**2 + m.x228**2 + m.x231**2 + m.x232**2 - 2*m.x227*m.x231 - 2*m.x228*m.x232
                           - 0.469370231236*m.b116 - 0.469370231236*m.b146 >= -0.469370231236)

m.c1144 = Constraint(expr=m.x227**2 + m.x228**2 + m.x233**2 + m.x234**2 - 2*m.x227*m.x233 - 2*m.x228*m.x234
                           - 0.469370231236*m.b116 - 0.469370231236*m.b161 >= -0.469370231236)

m.c1145 = Constraint(expr=m.x227**2 + m.x228**2 + m.x235**2 + m.x236**2 - 2*m.x227*m.x235 - 2*m.x228*m.x236
                           - 0.469370231236*m.b116 - 0.469370231236*m.b176 >= -0.469370231236)

m.c1146 = Constraint(expr=m.x227**2 + m.x228**2 + m.x229**2 + m.x230**2 - 2*m.x227*m.x229 - 2*m.x228*m.x230
                           - 0.469370231236*m.b116 - 0.469370231236*m.b131 >= -0.469370231236)

m.c1147 = Constraint(expr=m.x229**2 + m.x230**2 + m.x231**2 + m.x232**2 - 2*m.x229*m.x231 - 2*m.x230*m.x232
                           - 0.469370231236*m.b131 - 0.469370231236*m.b146 >= -0.469370231236)

m.c1148 = Constraint(expr=m.x229**2 + m.x230**2 + m.x233**2 + m.x234**2 - 2*m.x229*m.x233 - 2*m.x230*m.x234
                           - 0.469370231236*m.b131 - 0.469370231236*m.b161 >= -0.469370231236)

m.c1149 = Constraint(expr=m.x229**2 + m.x230**2 + m.x235**2 + m.x236**2 - 2*m.x229*m.x235 - 2*m.x230*m.x236
                           - 0.469370231236*m.b131 - 0.469370231236*m.b176 >= -0.469370231236)

m.c1150 = Constraint(expr=m.x227**2 + m.x228**2 + m.x231**2 + m.x232**2 - 2*m.x227*m.x231 - 2*m.x228*m.x232
                           - 0.469370231236*m.b116 - 0.469370231236*m.b146 >= -0.469370231236)

m.c1151 = Constraint(expr=m.x229**2 + m.x230**2 + m.x231**2 + m.x232**2 - 2*m.x229*m.x231 - 2*m.x230*m.x232
                           - 0.469370231236*m.b131 - 0.469370231236*m.b146 >= -0.469370231236)

m.c1152 = Constraint(expr=m.x231**2 + m.x232**2 + m.x233**2 + m.x234**2 - 2*m.x231*m.x233 - 2*m.x232*m.x234
                           - 0.469370231236*m.b146 - 0.469370231236*m.b161 >= -0.469370231236)

m.c1153 = Constraint(expr=m.x231**2 + m.x232**2 + m.x235**2 + m.x236**2 - 2*m.x231*m.x235 - 2*m.x232*m.x236
                           - 0.469370231236*m.b146 - 0.469370231236*m.b176 >= -0.469370231236)

m.c1154 = Constraint(expr=m.x227**2 + m.x228**2 + m.x233**2 + m.x234**2 - 2*m.x227*m.x233 - 2*m.x228*m.x234
                           - 0.469370231236*m.b116 - 0.469370231236*m.b161 >= -0.469370231236)

m.c1155 = Constraint(expr=m.x229**2 + m.x230**2 + m.x233**2 + m.x234**2 - 2*m.x229*m.x233 - 2*m.x230*m.x234
                           - 0.469370231236*m.b131 - 0.469370231236*m.b161 >= -0.469370231236)

m.c1156 = Constraint(expr=m.x231**2 + m.x232**2 + m.x233**2 + m.x234**2 - 2*m.x231*m.x233 - 2*m.x232*m.x234
                           - 0.469370231236*m.b146 - 0.469370231236*m.b161 >= -0.469370231236)

m.c1157 = Constraint(expr=m.x233**2 + m.x234**2 + m.x235**2 + m.x236**2 - 2*m.x233*m.x235 - 2*m.x234*m.x236
                           - 0.469370231236*m.b161 - 0.469370231236*m.b176 >= -0.469370231236)

m.c1158 = Constraint(expr=m.x227**2 + m.x228**2 + m.x235**2 + m.x236**2 - 2*m.x227*m.x235 - 2*m.x228*m.x236
                           - 0.469370231236*m.b116 - 0.469370231236*m.b176 >= -0.469370231236)

m.c1159 = Constraint(expr=m.x229**2 + m.x230**2 + m.x235**2 + m.x236**2 - 2*m.x229*m.x235 - 2*m.x230*m.x236
                           - 0.469370231236*m.b131 - 0.469370231236*m.b176 >= -0.469370231236)

m.c1160 = Constraint(expr=m.x231**2 + m.x232**2 + m.x235**2 + m.x236**2 - 2*m.x231*m.x235 - 2*m.x232*m.x236
                           - 0.469370231236*m.b146 - 0.469370231236*m.b176 >= -0.469370231236)

m.c1161 = Constraint(expr=m.x233**2 + m.x234**2 + m.x235**2 + m.x236**2 - 2*m.x233*m.x235 - 2*m.x234*m.x236
                           - 0.469370231236*m.b161 - 0.469370231236*m.b176 >= -0.469370231236)

m.c1162 = Constraint(expr=m.x227**2 + m.x228**2 + m.x229**2 + m.x230**2 - 2*m.x227*m.x229 - 2*m.x228*m.x230
                           - 0.469370231236*m.b117 - 0.469370231236*m.b132 >= -0.469370231236)

m.c1163 = Constraint(expr=m.x227**2 + m.x228**2 + m.x231**2 + m.x232**2 - 2*m.x227*m.x231 - 2*m.x228*m.x232
                           - 0.469370231236*m.b117 - 0.469370231236*m.b147 >= -0.469370231236)

m.c1164 = Constraint(expr=m.x227**2 + m.x228**2 + m.x233**2 + m.x234**2 - 2*m.x227*m.x233 - 2*m.x228*m.x234
                           - 0.469370231236*m.b117 - 0.469370231236*m.b162 >= -0.469370231236)

m.c1165 = Constraint(expr=m.x227**2 + m.x228**2 + m.x235**2 + m.x236**2 - 2*m.x227*m.x235 - 2*m.x228*m.x236
                           - 0.469370231236*m.b117 - 0.469370231236*m.b177 >= -0.469370231236)

m.c1166 = Constraint(expr=m.x227**2 + m.x228**2 + m.x229**2 + m.x230**2 - 2*m.x227*m.x229 - 2*m.x228*m.x230
                           - 0.469370231236*m.b117 - 0.469370231236*m.b132 >= -0.469370231236)

m.c1167 = Constraint(expr=m.x229**2 + m.x230**2 + m.x231**2 + m.x232**2 - 2*m.x229*m.x231 - 2*m.x230*m.x232
                           - 0.469370231236*m.b132 - 0.469370231236*m.b147 >= -0.469370231236)

m.c1168 = Constraint(expr=m.x229**2 + m.x230**2 + m.x233**2 + m.x234**2 - 2*m.x229*m.x233 - 2*m.x230*m.x234
                           - 0.469370231236*m.b132 - 0.469370231236*m.b162 >= -0.469370231236)

m.c1169 = Constraint(expr=m.x229**2 + m.x230**2 + m.x235**2 + m.x236**2 - 2*m.x229*m.x235 - 2*m.x230*m.x236
                           - 0.469370231236*m.b132 - 0.469370231236*m.b177 >= -0.469370231236)

m.c1170 = Constraint(expr=m.x227**2 + m.x228**2 + m.x231**2 + m.x232**2 - 2*m.x227*m.x231 - 2*m.x228*m.x232
                           - 0.469370231236*m.b117 - 0.469370231236*m.b147 >= -0.469370231236)

m.c1171 = Constraint(expr=m.x229**2 + m.x230**2 + m.x231**2 + m.x232**2 - 2*m.x229*m.x231 - 2*m.x230*m.x232
                           - 0.469370231236*m.b132 - 0.469370231236*m.b147 >= -0.469370231236)

m.c1172 = Constraint(expr=m.x231**2 + m.x232**2 + m.x233**2 + m.x234**2 - 2*m.x231*m.x233 - 2*m.x232*m.x234
                           - 0.469370231236*m.b147 - 0.469370231236*m.b162 >= -0.469370231236)

m.c1173 = Constraint(expr=m.x231**2 + m.x232**2 + m.x235**2 + m.x236**2 - 2*m.x231*m.x235 - 2*m.x232*m.x236
                           - 0.469370231236*m.b147 - 0.469370231236*m.b177 >= -0.469370231236)

m.c1174 = Constraint(expr=m.x227**2 + m.x228**2 + m.x233**2 + m.x234**2 - 2*m.x227*m.x233 - 2*m.x228*m.x234
                           - 0.469370231236*m.b117 - 0.469370231236*m.b162 >= -0.469370231236)

m.c1175 = Constraint(expr=m.x229**2 + m.x230**2 + m.x233**2 + m.x234**2 - 2*m.x229*m.x233 - 2*m.x230*m.x234
                           - 0.469370231236*m.b132 - 0.469370231236*m.b162 >= -0.469370231236)

m.c1176 = Constraint(expr=m.x231**2 + m.x232**2 + m.x233**2 + m.x234**2 - 2*m.x231*m.x233 - 2*m.x232*m.x234
                           - 0.469370231236*m.b147 - 0.469370231236*m.b162 >= -0.469370231236)

m.c1177 = Constraint(expr=m.x233**2 + m.x234**2 + m.x235**2 + m.x236**2 - 2*m.x233*m.x235 - 2*m.x234*m.x236
                           - 0.469370231236*m.b162 - 0.469370231236*m.b177 >= -0.469370231236)

m.c1178 = Constraint(expr=m.x227**2 + m.x228**2 + m.x235**2 + m.x236**2 - 2*m.x227*m.x235 - 2*m.x228*m.x236
                           - 0.469370231236*m.b117 - 0.469370231236*m.b177 >= -0.469370231236)

m.c1179 = Constraint(expr=m.x229**2 + m.x230**2 + m.x235**2 + m.x236**2 - 2*m.x229*m.x235 - 2*m.x230*m.x236
                           - 0.469370231236*m.b132 - 0.469370231236*m.b177 >= -0.469370231236)

m.c1180 = Constraint(expr=m.x231**2 + m.x232**2 + m.x235**2 + m.x236**2 - 2*m.x231*m.x235 - 2*m.x232*m.x236
                           - 0.469370231236*m.b147 - 0.469370231236*m.b177 >= -0.469370231236)

m.c1181 = Constraint(expr=m.x233**2 + m.x234**2 + m.x235**2 + m.x236**2 - 2*m.x233*m.x235 - 2*m.x234*m.x236
                           - 0.469370231236*m.b162 - 0.469370231236*m.b177 >= -0.469370231236)

m.c1182 = Constraint(expr=m.x227**2 + m.x228**2 + m.x229**2 + m.x230**2 - 2*m.x227*m.x229 - 2*m.x228*m.x230
                           - 0.469370231236*m.b118 - 0.469370231236*m.b133 >= -0.469370231236)

m.c1183 = Constraint(expr=m.x227**2 + m.x228**2 + m.x231**2 + m.x232**2 - 2*m.x227*m.x231 - 2*m.x228*m.x232
                           - 0.469370231236*m.b118 - 0.469370231236*m.b148 >= -0.469370231236)

m.c1184 = Constraint(expr=m.x227**2 + m.x228**2 + m.x233**2 + m.x234**2 - 2*m.x227*m.x233 - 2*m.x228*m.x234
                           - 0.469370231236*m.b118 - 0.469370231236*m.b163 >= -0.469370231236)

m.c1185 = Constraint(expr=m.x227**2 + m.x228**2 + m.x235**2 + m.x236**2 - 2*m.x227*m.x235 - 2*m.x228*m.x236
                           - 0.469370231236*m.b118 - 0.469370231236*m.b178 >= -0.469370231236)

m.c1186 = Constraint(expr=m.x227**2 + m.x228**2 + m.x229**2 + m.x230**2 - 2*m.x227*m.x229 - 2*m.x228*m.x230
                           - 0.469370231236*m.b118 - 0.469370231236*m.b133 >= -0.469370231236)

m.c1187 = Constraint(expr=m.x229**2 + m.x230**2 + m.x231**2 + m.x232**2 - 2*m.x229*m.x231 - 2*m.x230*m.x232
                           - 0.469370231236*m.b133 - 0.469370231236*m.b148 >= -0.469370231236)

m.c1188 = Constraint(expr=m.x229**2 + m.x230**2 + m.x233**2 + m.x234**2 - 2*m.x229*m.x233 - 2*m.x230*m.x234
                           - 0.469370231236*m.b133 - 0.469370231236*m.b163 >= -0.469370231236)

m.c1189 = Constraint(expr=m.x229**2 + m.x230**2 + m.x235**2 + m.x236**2 - 2*m.x229*m.x235 - 2*m.x230*m.x236
                           - 0.469370231236*m.b133 - 0.469370231236*m.b178 >= -0.469370231236)

m.c1190 = Constraint(expr=m.x227**2 + m.x228**2 + m.x231**2 + m.x232**2 - 2*m.x227*m.x231 - 2*m.x228*m.x232
                           - 0.469370231236*m.b118 - 0.469370231236*m.b148 >= -0.469370231236)

m.c1191 = Constraint(expr=m.x229**2 + m.x230**2 + m.x231**2 + m.x232**2 - 2*m.x229*m.x231 - 2*m.x230*m.x232
                           - 0.469370231236*m.b133 - 0.469370231236*m.b148 >= -0.469370231236)

m.c1192 = Constraint(expr=m.x231**2 + m.x232**2 + m.x233**2 + m.x234**2 - 2*m.x231*m.x233 - 2*m.x232*m.x234
                           - 0.469370231236*m.b148 - 0.469370231236*m.b163 >= -0.469370231236)

m.c1193 = Constraint(expr=m.x231**2 + m.x232**2 + m.x235**2 + m.x236**2 - 2*m.x231*m.x235 - 2*m.x232*m.x236
                           - 0.469370231236*m.b148 - 0.469370231236*m.b178 >= -0.469370231236)

m.c1194 = Constraint(expr=m.x227**2 + m.x228**2 + m.x233**2 + m.x234**2 - 2*m.x227*m.x233 - 2*m.x228*m.x234
                           - 0.469370231236*m.b118 - 0.469370231236*m.b163 >= -0.469370231236)

m.c1195 = Constraint(expr=m.x229**2 + m.x230**2 + m.x233**2 + m.x234**2 - 2*m.x229*m.x233 - 2*m.x230*m.x234
                           - 0.469370231236*m.b133 - 0.469370231236*m.b163 >= -0.469370231236)

m.c1196 = Constraint(expr=m.x231**2 + m.x232**2 + m.x233**2 + m.x234**2 - 2*m.x231*m.x233 - 2*m.x232*m.x234
                           - 0.469370231236*m.b148 - 0.469370231236*m.b163 >= -0.469370231236)

m.c1197 = Constraint(expr=m.x233**2 + m.x234**2 + m.x235**2 + m.x236**2 - 2*m.x233*m.x235 - 2*m.x234*m.x236
                           - 0.469370231236*m.b163 - 0.469370231236*m.b178 >= -0.469370231236)

m.c1198 = Constraint(expr=m.x227**2 + m.x228**2 + m.x235**2 + m.x236**2 - 2*m.x227*m.x235 - 2*m.x228*m.x236
                           - 0.469370231236*m.b118 - 0.469370231236*m.b178 >= -0.469370231236)

m.c1199 = Constraint(expr=m.x229**2 + m.x230**2 + m.x235**2 + m.x236**2 - 2*m.x229*m.x235 - 2*m.x230*m.x236
                           - 0.469370231236*m.b133 - 0.469370231236*m.b178 >= -0.469370231236)

m.c1200 = Constraint(expr=m.x231**2 + m.x232**2 + m.x235**2 + m.x236**2 - 2*m.x231*m.x235 - 2*m.x232*m.x236
                           - 0.469370231236*m.b148 - 0.469370231236*m.b178 >= -0.469370231236)

m.c1201 = Constraint(expr=m.x233**2 + m.x234**2 + m.x235**2 + m.x236**2 - 2*m.x233*m.x235 - 2*m.x234*m.x236
                           - 0.469370231236*m.b163 - 0.469370231236*m.b178 >= -0.469370231236)

m.c1202 = Constraint(expr=m.x227**2 + m.x228**2 + m.x229**2 + m.x230**2 - 2*m.x227*m.x229 - 2*m.x228*m.x230
                           - 0.469370231236*m.b119 - 0.469370231236*m.b134 >= -0.469370231236)

m.c1203 = Constraint(expr=m.x227**2 + m.x228**2 + m.x231**2 + m.x232**2 - 2*m.x227*m.x231 - 2*m.x228*m.x232
                           - 0.469370231236*m.b119 - 0.469370231236*m.b149 >= -0.469370231236)

m.c1204 = Constraint(expr=m.x227**2 + m.x228**2 + m.x233**2 + m.x234**2 - 2*m.x227*m.x233 - 2*m.x228*m.x234
                           - 0.469370231236*m.b119 - 0.469370231236*m.b164 >= -0.469370231236)

m.c1205 = Constraint(expr=m.x227**2 + m.x228**2 + m.x235**2 + m.x236**2 - 2*m.x227*m.x235 - 2*m.x228*m.x236
                           - 0.469370231236*m.b119 - 0.469370231236*m.b179 >= -0.469370231236)

m.c1206 = Constraint(expr=m.x227**2 + m.x228**2 + m.x229**2 + m.x230**2 - 2*m.x227*m.x229 - 2*m.x228*m.x230
                           - 0.469370231236*m.b119 - 0.469370231236*m.b134 >= -0.469370231236)

m.c1207 = Constraint(expr=m.x229**2 + m.x230**2 + m.x231**2 + m.x232**2 - 2*m.x229*m.x231 - 2*m.x230*m.x232
                           - 0.469370231236*m.b134 - 0.469370231236*m.b149 >= -0.469370231236)

m.c1208 = Constraint(expr=m.x229**2 + m.x230**2 + m.x233**2 + m.x234**2 - 2*m.x229*m.x233 - 2*m.x230*m.x234
                           - 0.469370231236*m.b134 - 0.469370231236*m.b164 >= -0.469370231236)

m.c1209 = Constraint(expr=m.x229**2 + m.x230**2 + m.x235**2 + m.x236**2 - 2*m.x229*m.x235 - 2*m.x230*m.x236
                           - 0.469370231236*m.b134 - 0.469370231236*m.b179 >= -0.469370231236)

m.c1210 = Constraint(expr=m.x227**2 + m.x228**2 + m.x231**2 + m.x232**2 - 2*m.x227*m.x231 - 2*m.x228*m.x232
                           - 0.469370231236*m.b119 - 0.469370231236*m.b149 >= -0.469370231236)

m.c1211 = Constraint(expr=m.x229**2 + m.x230**2 + m.x231**2 + m.x232**2 - 2*m.x229*m.x231 - 2*m.x230*m.x232
                           - 0.469370231236*m.b134 - 0.469370231236*m.b149 >= -0.469370231236)

m.c1212 = Constraint(expr=m.x231**2 + m.x232**2 + m.x233**2 + m.x234**2 - 2*m.x231*m.x233 - 2*m.x232*m.x234
                           - 0.469370231236*m.b149 - 0.469370231236*m.b164 >= -0.469370231236)

m.c1213 = Constraint(expr=m.x231**2 + m.x232**2 + m.x235**2 + m.x236**2 - 2*m.x231*m.x235 - 2*m.x232*m.x236
                           - 0.469370231236*m.b149 - 0.469370231236*m.b179 >= -0.469370231236)

m.c1214 = Constraint(expr=m.x227**2 + m.x228**2 + m.x233**2 + m.x234**2 - 2*m.x227*m.x233 - 2*m.x228*m.x234
                           - 0.469370231236*m.b119 - 0.469370231236*m.b164 >= -0.469370231236)

m.c1215 = Constraint(expr=m.x229**2 + m.x230**2 + m.x233**2 + m.x234**2 - 2*m.x229*m.x233 - 2*m.x230*m.x234
                           - 0.469370231236*m.b134 - 0.469370231236*m.b164 >= -0.469370231236)

m.c1216 = Constraint(expr=m.x231**2 + m.x232**2 + m.x233**2 + m.x234**2 - 2*m.x231*m.x233 - 2*m.x232*m.x234
                           - 0.469370231236*m.b149 - 0.469370231236*m.b164 >= -0.469370231236)

m.c1217 = Constraint(expr=m.x233**2 + m.x234**2 + m.x235**2 + m.x236**2 - 2*m.x233*m.x235 - 2*m.x234*m.x236
                           - 0.469370231236*m.b164 - 0.469370231236*m.b179 >= -0.469370231236)

m.c1218 = Constraint(expr=m.x227**2 + m.x228**2 + m.x235**2 + m.x236**2 - 2*m.x227*m.x235 - 2*m.x228*m.x236
                           - 0.469370231236*m.b119 - 0.469370231236*m.b179 >= -0.469370231236)

m.c1219 = Constraint(expr=m.x229**2 + m.x230**2 + m.x235**2 + m.x236**2 - 2*m.x229*m.x235 - 2*m.x230*m.x236
                           - 0.469370231236*m.b134 - 0.469370231236*m.b179 >= -0.469370231236)

m.c1220 = Constraint(expr=m.x231**2 + m.x232**2 + m.x235**2 + m.x236**2 - 2*m.x231*m.x235 - 2*m.x232*m.x236
                           - 0.469370231236*m.b149 - 0.469370231236*m.b179 >= -0.469370231236)

m.c1221 = Constraint(expr=m.x233**2 + m.x234**2 + m.x235**2 + m.x236**2 - 2*m.x233*m.x235 - 2*m.x234*m.x236
                           - 0.469370231236*m.b164 - 0.469370231236*m.b179 >= -0.469370231236)

m.c1222 = Constraint(expr=m.x227**2 + m.x228**2 + m.x229**2 + m.x230**2 - 2*m.x227*m.x229 - 2*m.x228*m.x230
                           - 0.469370231236*m.b120 - 0.469370231236*m.b135 >= -0.469370231236)

m.c1223 = Constraint(expr=m.x227**2 + m.x228**2 + m.x231**2 + m.x232**2 - 2*m.x227*m.x231 - 2*m.x228*m.x232
                           - 0.469370231236*m.b120 - 0.469370231236*m.b150 >= -0.469370231236)

m.c1224 = Constraint(expr=m.x227**2 + m.x228**2 + m.x233**2 + m.x234**2 - 2*m.x227*m.x233 - 2*m.x228*m.x234
                           - 0.469370231236*m.b120 - 0.469370231236*m.b165 >= -0.469370231236)

m.c1225 = Constraint(expr=m.x227**2 + m.x228**2 + m.x235**2 + m.x236**2 - 2*m.x227*m.x235 - 2*m.x228*m.x236
                           - 0.469370231236*m.b120 - 0.469370231236*m.b180 >= -0.469370231236)

m.c1226 = Constraint(expr=m.x227**2 + m.x228**2 + m.x229**2 + m.x230**2 - 2*m.x227*m.x229 - 2*m.x228*m.x230
                           - 0.469370231236*m.b120 - 0.469370231236*m.b135 >= -0.469370231236)

m.c1227 = Constraint(expr=m.x229**2 + m.x230**2 + m.x231**2 + m.x232**2 - 2*m.x229*m.x231 - 2*m.x230*m.x232
                           - 0.469370231236*m.b135 - 0.469370231236*m.b150 >= -0.469370231236)

m.c1228 = Constraint(expr=m.x229**2 + m.x230**2 + m.x233**2 + m.x234**2 - 2*m.x229*m.x233 - 2*m.x230*m.x234
                           - 0.469370231236*m.b135 - 0.469370231236*m.b165 >= -0.469370231236)

m.c1229 = Constraint(expr=m.x229**2 + m.x230**2 + m.x235**2 + m.x236**2 - 2*m.x229*m.x235 - 2*m.x230*m.x236
                           - 0.469370231236*m.b135 - 0.469370231236*m.b180 >= -0.469370231236)

m.c1230 = Constraint(expr=m.x227**2 + m.x228**2 + m.x231**2 + m.x232**2 - 2*m.x227*m.x231 - 2*m.x228*m.x232
                           - 0.469370231236*m.b120 - 0.469370231236*m.b150 >= -0.469370231236)

m.c1231 = Constraint(expr=m.x229**2 + m.x230**2 + m.x231**2 + m.x232**2 - 2*m.x229*m.x231 - 2*m.x230*m.x232
                           - 0.469370231236*m.b135 - 0.469370231236*m.b150 >= -0.469370231236)

m.c1232 = Constraint(expr=m.x231**2 + m.x232**2 + m.x233**2 + m.x234**2 - 2*m.x231*m.x233 - 2*m.x232*m.x234
                           - 0.469370231236*m.b150 - 0.469370231236*m.b165 >= -0.469370231236)

m.c1233 = Constraint(expr=m.x231**2 + m.x232**2 + m.x235**2 + m.x236**2 - 2*m.x231*m.x235 - 2*m.x232*m.x236
                           - 0.469370231236*m.b150 - 0.469370231236*m.b180 >= -0.469370231236)

m.c1234 = Constraint(expr=m.x227**2 + m.x228**2 + m.x233**2 + m.x234**2 - 2*m.x227*m.x233 - 2*m.x228*m.x234
                           - 0.469370231236*m.b120 - 0.469370231236*m.b165 >= -0.469370231236)

m.c1235 = Constraint(expr=m.x229**2 + m.x230**2 + m.x233**2 + m.x234**2 - 2*m.x229*m.x233 - 2*m.x230*m.x234
                           - 0.469370231236*m.b135 - 0.469370231236*m.b165 >= -0.469370231236)

m.c1236 = Constraint(expr=m.x231**2 + m.x232**2 + m.x233**2 + m.x234**2 - 2*m.x231*m.x233 - 2*m.x232*m.x234
                           - 0.469370231236*m.b150 - 0.469370231236*m.b165 >= -0.469370231236)

m.c1237 = Constraint(expr=m.x233**2 + m.x234**2 + m.x235**2 + m.x236**2 - 2*m.x233*m.x235 - 2*m.x234*m.x236
                           - 0.469370231236*m.b165 - 0.469370231236*m.b180 >= -0.469370231236)

m.c1238 = Constraint(expr=m.x227**2 + m.x228**2 + m.x235**2 + m.x236**2 - 2*m.x227*m.x235 - 2*m.x228*m.x236
                           - 0.469370231236*m.b120 - 0.469370231236*m.b180 >= -0.469370231236)

m.c1239 = Constraint(expr=m.x229**2 + m.x230**2 + m.x235**2 + m.x236**2 - 2*m.x229*m.x235 - 2*m.x230*m.x236
                           - 0.469370231236*m.b135 - 0.469370231236*m.b180 >= -0.469370231236)

m.c1240 = Constraint(expr=m.x231**2 + m.x232**2 + m.x235**2 + m.x236**2 - 2*m.x231*m.x235 - 2*m.x232*m.x236
                           - 0.469370231236*m.b150 - 0.469370231236*m.b180 >= -0.469370231236)

m.c1241 = Constraint(expr=m.x233**2 + m.x234**2 + m.x235**2 + m.x236**2 - 2*m.x233*m.x235 - 2*m.x234*m.x236
                           - 0.469370231236*m.b165 - 0.469370231236*m.b180 >= -0.469370231236)

m.c1242 = Constraint(expr=m.x227**2 + m.x228**2 + m.x229**2 + m.x230**2 - 2*m.x227*m.x229 - 2*m.x228*m.x230
                           - 0.469370231236*m.b121 - 0.469370231236*m.b136 >= -0.469370231236)

m.c1243 = Constraint(expr=m.x227**2 + m.x228**2 + m.x231**2 + m.x232**2 - 2*m.x227*m.x231 - 2*m.x228*m.x232
                           - 0.469370231236*m.b121 - 0.469370231236*m.b151 >= -0.469370231236)

m.c1244 = Constraint(expr=m.x227**2 + m.x228**2 + m.x233**2 + m.x234**2 - 2*m.x227*m.x233 - 2*m.x228*m.x234
                           - 0.469370231236*m.b121 - 0.469370231236*m.b166 >= -0.469370231236)

m.c1245 = Constraint(expr=m.x227**2 + m.x228**2 + m.x235**2 + m.x236**2 - 2*m.x227*m.x235 - 2*m.x228*m.x236
                           - 0.469370231236*m.b121 - 0.469370231236*m.b181 >= -0.469370231236)

m.c1246 = Constraint(expr=m.x227**2 + m.x228**2 + m.x229**2 + m.x230**2 - 2*m.x227*m.x229 - 2*m.x228*m.x230
                           - 0.469370231236*m.b121 - 0.469370231236*m.b136 >= -0.469370231236)

m.c1247 = Constraint(expr=m.x229**2 + m.x230**2 + m.x231**2 + m.x232**2 - 2*m.x229*m.x231 - 2*m.x230*m.x232
                           - 0.469370231236*m.b136 - 0.469370231236*m.b151 >= -0.469370231236)

m.c1248 = Constraint(expr=m.x229**2 + m.x230**2 + m.x233**2 + m.x234**2 - 2*m.x229*m.x233 - 2*m.x230*m.x234
                           - 0.469370231236*m.b136 - 0.469370231236*m.b166 >= -0.469370231236)

m.c1249 = Constraint(expr=m.x229**2 + m.x230**2 + m.x235**2 + m.x236**2 - 2*m.x229*m.x235 - 2*m.x230*m.x236
                           - 0.469370231236*m.b136 - 0.469370231236*m.b181 >= -0.469370231236)

m.c1250 = Constraint(expr=m.x227**2 + m.x228**2 + m.x231**2 + m.x232**2 - 2*m.x227*m.x231 - 2*m.x228*m.x232
                           - 0.469370231236*m.b121 - 0.469370231236*m.b151 >= -0.469370231236)

m.c1251 = Constraint(expr=m.x229**2 + m.x230**2 + m.x231**2 + m.x232**2 - 2*m.x229*m.x231 - 2*m.x230*m.x232
                           - 0.469370231236*m.b136 - 0.469370231236*m.b151 >= -0.469370231236)

m.c1252 = Constraint(expr=m.x231**2 + m.x232**2 + m.x233**2 + m.x234**2 - 2*m.x231*m.x233 - 2*m.x232*m.x234
                           - 0.469370231236*m.b151 - 0.469370231236*m.b166 >= -0.469370231236)

m.c1253 = Constraint(expr=m.x231**2 + m.x232**2 + m.x235**2 + m.x236**2 - 2*m.x231*m.x235 - 2*m.x232*m.x236
                           - 0.469370231236*m.b151 - 0.469370231236*m.b181 >= -0.469370231236)

m.c1254 = Constraint(expr=m.x227**2 + m.x228**2 + m.x233**2 + m.x234**2 - 2*m.x227*m.x233 - 2*m.x228*m.x234
                           - 0.469370231236*m.b121 - 0.469370231236*m.b166 >= -0.469370231236)

m.c1255 = Constraint(expr=m.x229**2 + m.x230**2 + m.x233**2 + m.x234**2 - 2*m.x229*m.x233 - 2*m.x230*m.x234
                           - 0.469370231236*m.b136 - 0.469370231236*m.b166 >= -0.469370231236)

m.c1256 = Constraint(expr=m.x231**2 + m.x232**2 + m.x233**2 + m.x234**2 - 2*m.x231*m.x233 - 2*m.x232*m.x234
                           - 0.469370231236*m.b151 - 0.469370231236*m.b166 >= -0.469370231236)

m.c1257 = Constraint(expr=m.x233**2 + m.x234**2 + m.x235**2 + m.x236**2 - 2*m.x233*m.x235 - 2*m.x234*m.x236
                           - 0.469370231236*m.b166 - 0.469370231236*m.b181 >= -0.469370231236)

m.c1258 = Constraint(expr=m.x227**2 + m.x228**2 + m.x235**2 + m.x236**2 - 2*m.x227*m.x235 - 2*m.x228*m.x236
                           - 0.469370231236*m.b121 - 0.469370231236*m.b181 >= -0.469370231236)

m.c1259 = Constraint(expr=m.x229**2 + m.x230**2 + m.x235**2 + m.x236**2 - 2*m.x229*m.x235 - 2*m.x230*m.x236
                           - 0.469370231236*m.b136 - 0.469370231236*m.b181 >= -0.469370231236)

m.c1260 = Constraint(expr=m.x231**2 + m.x232**2 + m.x235**2 + m.x236**2 - 2*m.x231*m.x235 - 2*m.x232*m.x236
                           - 0.469370231236*m.b151 - 0.469370231236*m.b181 >= -0.469370231236)

m.c1261 = Constraint(expr=m.x233**2 + m.x234**2 + m.x235**2 + m.x236**2 - 2*m.x233*m.x235 - 2*m.x234*m.x236
                           - 0.469370231236*m.b166 - 0.469370231236*m.b181 >= -0.469370231236)

m.c1262 = Constraint(expr=m.x215**2 + m.x216**2 + m.x217**2 + m.x218**2 - 2*m.x215*m.x217 - 2*m.x216*m.x218
                           - 1.436939228176*m.b62 - 1.436939228176*m.b71 >= -1.436939228176)

m.c1263 = Constraint(expr=m.x215**2 + m.x216**2 + m.x219**2 + m.x220**2 - 2*m.x215*m.x219 - 2*m.x216*m.x220
                           - 1.436939228176*m.b62 - 1.436939228176*m.b80 >= -1.436939228176)

m.c1264 = Constraint(expr=m.x215**2 + m.x216**2 + m.x221**2 + m.x222**2 - 2*m.x216*m.x222 - 2*m.x215*m.x221
                           - 1.436939228176*m.b62 - 1.436939228176*m.b89 >= -1.436939228176)

m.c1265 = Constraint(expr=m.x215**2 + m.x216**2 + m.x223**2 + m.x224**2 - 2*m.x216*m.x224 - 2*m.x215*m.x223
                           - 1.436939228176*m.b62 - 1.436939228176*m.b98 >= -1.436939228176)

m.c1266 = Constraint(expr=m.x215**2 + m.x216**2 + m.x225**2 + m.x226**2 - 2*m.x215*m.x225 - 2*m.x216*m.x226
                           - 1.436939228176*m.b62 - 1.436939228176*m.b107 >= -1.436939228176)

m.c1267 = Constraint(expr=m.x215**2 + m.x216**2 + m.x227**2 + m.x228**2 - 2*m.x216*m.x228 - 2*m.x215*m.x227
                           - 0.887203867225*m.b62 - 0.887203867225*m.b122 >= -0.887203867225)

m.c1268 = Constraint(expr=m.x215**2 + m.x216**2 + m.x229**2 + m.x230**2 - 2*m.x215*m.x229 - 2*m.x216*m.x230
                           - 0.887203867225*m.b62 - 0.887203867225*m.b137 >= -0.887203867225)

m.c1269 = Constraint(expr=m.x215**2 + m.x216**2 + m.x231**2 + m.x232**2 - 2*m.x216*m.x232 - 2*m.x215*m.x231
                           - 0.887203867225*m.b62 - 0.887203867225*m.b152 >= -0.887203867225)

m.c1270 = Constraint(expr=m.x215**2 + m.x216**2 + m.x233**2 + m.x234**2 - 2*m.x216*m.x234 - 2*m.x215*m.x233
                           - 0.887203867225*m.b62 - 0.887203867225*m.b167 >= -0.887203867225)

m.c1271 = Constraint(expr=m.x215**2 + m.x216**2 + m.x235**2 + m.x236**2 - 2*m.x216*m.x236 - 2*m.x215*m.x235
                           - 0.887203867225*m.b62 - 0.887203867225*m.b182 >= -0.887203867225)

m.c1272 = Constraint(expr=m.x215**2 + m.x216**2 + m.x217**2 + m.x218**2 - 2*m.x215*m.x217 - 2*m.x216*m.x218
                           - 1.436939228176*m.b62 - 1.436939228176*m.b71 >= -1.436939228176)

m.c1273 = Constraint(expr=m.x217**2 + m.x218**2 + m.x219**2 + m.x220**2 - 2*m.x217*m.x219 - 2*m.x218*m.x220
                           - 1.436939228176*m.b71 - 1.436939228176*m.b80 >= -1.436939228176)

m.c1274 = Constraint(expr=m.x217**2 + m.x218**2 + m.x221**2 + m.x222**2 - 2*m.x218*m.x222 - 2*m.x217*m.x221
                           - 1.436939228176*m.b71 - 1.436939228176*m.b89 >= -1.436939228176)

m.c1275 = Constraint(expr=m.x217**2 + m.x218**2 + m.x223**2 + m.x224**2 - 2*m.x217*m.x223 - 2*m.x218*m.x224
                           - 1.436939228176*m.b71 - 1.436939228176*m.b98 >= -1.436939228176)

m.c1276 = Constraint(expr=m.x217**2 + m.x218**2 + m.x225**2 + m.x226**2 - 2*m.x218*m.x226 - 2*m.x217*m.x225
                           - 1.436939228176*m.b71 - 1.436939228176*m.b107 >= -1.436939228176)

m.c1277 = Constraint(expr=m.x217**2 + m.x218**2 + m.x227**2 + m.x228**2 - 2*m.x217*m.x227 - 2*m.x218*m.x228
                           - 0.887203867225*m.b71 - 0.887203867225*m.b122 >= -0.887203867225)

m.c1278 = Constraint(expr=m.x217**2 + m.x218**2 + m.x229**2 + m.x230**2 - 2*m.x218*m.x230 - 2*m.x217*m.x229
                           - 0.887203867225*m.b71 - 0.887203867225*m.b137 >= -0.887203867225)

m.c1279 = Constraint(expr=m.x217**2 + m.x218**2 + m.x231**2 + m.x232**2 - 2*m.x218*m.x232 - 2*m.x217*m.x231
                           - 0.887203867225*m.b71 - 0.887203867225*m.b152 >= -0.887203867225)

m.c1280 = Constraint(expr=m.x217**2 + m.x218**2 + m.x233**2 + m.x234**2 - 2*m.x218*m.x234 - 2*m.x217*m.x233
                           - 0.887203867225*m.b71 - 0.887203867225*m.b167 >= -0.887203867225)

m.c1281 = Constraint(expr=m.x217**2 + m.x218**2 + m.x235**2 + m.x236**2 - 2*m.x218*m.x236 - 2*m.x217*m.x235
                           - 0.887203867225*m.b71 - 0.887203867225*m.b182 >= -0.887203867225)

m.c1282 = Constraint(expr=m.x215**2 + m.x216**2 + m.x219**2 + m.x220**2 - 2*m.x215*m.x219 - 2*m.x216*m.x220
                           - 1.436939228176*m.b62 - 1.436939228176*m.b80 >= -1.436939228176)

m.c1283 = Constraint(expr=m.x217**2 + m.x218**2 + m.x219**2 + m.x220**2 - 2*m.x217*m.x219 - 2*m.x218*m.x220
                           - 1.436939228176*m.b71 - 1.436939228176*m.b80 >= -1.436939228176)

m.c1284 = Constraint(expr=m.x219**2 + m.x220**2 + m.x221**2 + m.x222**2 - 2*m.x219*m.x221 - 2*m.x220*m.x222
                           - 1.436939228176*m.b80 - 1.436939228176*m.b89 >= -1.436939228176)

m.c1285 = Constraint(expr=m.x219**2 + m.x220**2 + m.x223**2 + m.x224**2 - 2*m.x220*m.x224 - 2*m.x219*m.x223
                           - 1.436939228176*m.b80 - 1.436939228176*m.b98 >= -1.436939228176)

m.c1286 = Constraint(expr=m.x219**2 + m.x220**2 + m.x225**2 + m.x226**2 - 2*m.x220*m.x226 - 2*m.x219*m.x225
                           - 1.436939228176*m.b80 - 1.436939228176*m.b107 >= -1.436939228176)

m.c1287 = Constraint(expr=m.x219**2 + m.x220**2 + m.x227**2 + m.x228**2 - 2*m.x220*m.x228 - 2*m.x219*m.x227
                           - 0.887203867225*m.b80 - 0.887203867225*m.b122 >= -0.887203867225)

m.c1288 = Constraint(expr=m.x219**2 + m.x220**2 + m.x229**2 + m.x230**2 - 2*m.x220*m.x230 - 2*m.x219*m.x229
                           - 0.887203867225*m.b80 - 0.887203867225*m.b137 >= -0.887203867225)

m.c1289 = Constraint(expr=m.x219**2 + m.x220**2 + m.x231**2 + m.x232**2 - 2*m.x219*m.x231 - 2*m.x220*m.x232
                           - 0.887203867225*m.b80 - 0.887203867225*m.b152 >= -0.887203867225)

m.c1290 = Constraint(expr=m.x219**2 + m.x220**2 + m.x233**2 + m.x234**2 - 2*m.x220*m.x234 - 2*m.x219*m.x233
                           - 0.887203867225*m.b80 - 0.887203867225*m.b167 >= -0.887203867225)

m.c1291 = Constraint(expr=m.x219**2 + m.x220**2 + m.x235**2 + m.x236**2 - 2*m.x219*m.x235 - 2*m.x220*m.x236
                           - 0.887203867225*m.b80 - 0.887203867225*m.b182 >= -0.887203867225)

m.c1292 = Constraint(expr=m.x215**2 + m.x216**2 + m.x221**2 + m.x222**2 - 2*m.x216*m.x222 - 2*m.x215*m.x221
                           - 1.436939228176*m.b62 - 1.436939228176*m.b89 >= -1.436939228176)

m.c1293 = Constraint(expr=m.x217**2 + m.x218**2 + m.x221**2 + m.x222**2 - 2*m.x218*m.x222 - 2*m.x217*m.x221
                           - 1.436939228176*m.b71 - 1.436939228176*m.b89 >= -1.436939228176)

m.c1294 = Constraint(expr=m.x219**2 + m.x220**2 + m.x221**2 + m.x222**2 - 2*m.x219*m.x221 - 2*m.x220*m.x222
                           - 1.436939228176*m.b80 - 1.436939228176*m.b89 >= -1.436939228176)

m.c1295 = Constraint(expr=m.x221**2 + m.x222**2 + m.x223**2 + m.x224**2 - 2*m.x221*m.x223 - 2*m.x222*m.x224
                           - 1.436939228176*m.b89 - 1.436939228176*m.b98 >= -1.436939228176)

m.c1296 = Constraint(expr=m.x221**2 + m.x222**2 + m.x225**2 + m.x226**2 - 2*m.x221*m.x225 - 2*m.x222*m.x226
                           - 1.436939228176*m.b89 - 1.436939228176*m.b107 >= -1.436939228176)

m.c1297 = Constraint(expr=m.x221**2 + m.x222**2 + m.x227**2 + m.x228**2 - 2*m.x221*m.x227 - 2*m.x222*m.x228
                           - 0.887203867225*m.b89 - 0.887203867225*m.b122 >= -0.887203867225)

m.c1298 = Constraint(expr=m.x221**2 + m.x222**2 + m.x229**2 + m.x230**2 - 2*m.x221*m.x229 - 2*m.x222*m.x230
                           - 0.887203867225*m.b89 - 0.887203867225*m.b137 >= -0.887203867225)

m.c1299 = Constraint(expr=m.x221**2 + m.x222**2 + m.x231**2 + m.x232**2 - 2*m.x221*m.x231 - 2*m.x222*m.x232
                           - 0.887203867225*m.b89 - 0.887203867225*m.b152 >= -0.887203867225)

m.c1300 = Constraint(expr=m.x221**2 + m.x222**2 + m.x233**2 + m.x234**2 - 2*m.x221*m.x233 - 2*m.x222*m.x234
                           - 0.887203867225*m.b89 - 0.887203867225*m.b167 >= -0.887203867225)

m.c1301 = Constraint(expr=m.x221**2 + m.x222**2 + m.x235**2 + m.x236**2 - 2*m.x221*m.x235 - 2*m.x222*m.x236
                           - 0.887203867225*m.b89 - 0.887203867225*m.b182 >= -0.887203867225)

m.c1302 = Constraint(expr=m.x215**2 + m.x216**2 + m.x223**2 + m.x224**2 - 2*m.x216*m.x224 - 2*m.x215*m.x223
                           - 1.436939228176*m.b62 - 1.436939228176*m.b98 >= -1.436939228176)

m.c1303 = Constraint(expr=m.x217**2 + m.x218**2 + m.x223**2 + m.x224**2 - 2*m.x217*m.x223 - 2*m.x218*m.x224
                           - 1.436939228176*m.b71 - 1.436939228176*m.b98 >= -1.436939228176)

m.c1304 = Constraint(expr=m.x219**2 + m.x220**2 + m.x223**2 + m.x224**2 - 2*m.x220*m.x224 - 2*m.x219*m.x223
                           - 1.436939228176*m.b80 - 1.436939228176*m.b98 >= -1.436939228176)

m.c1305 = Constraint(expr=m.x221**2 + m.x222**2 + m.x223**2 + m.x224**2 - 2*m.x221*m.x223 - 2*m.x222*m.x224
                           - 1.436939228176*m.b89 - 1.436939228176*m.b98 >= -1.436939228176)

m.c1306 = Constraint(expr=m.x223**2 + m.x224**2 + m.x225**2 + m.x226**2 - 2*m.x223*m.x225 - 2*m.x224*m.x226
                           - 1.436939228176*m.b98 - 1.436939228176*m.b107 >= -1.436939228176)

m.c1307 = Constraint(expr=m.x223**2 + m.x224**2 + m.x227**2 + m.x228**2 - 2*m.x223*m.x227 - 2*m.x224*m.x228
                           - 0.887203867225*m.b98 - 0.887203867225*m.b122 >= -0.887203867225)

m.c1308 = Constraint(expr=m.x223**2 + m.x224**2 + m.x229**2 + m.x230**2 - 2*m.x223*m.x229 - 2*m.x224*m.x230
                           - 0.887203867225*m.b98 - 0.887203867225*m.b137 >= -0.887203867225)

m.c1309 = Constraint(expr=m.x223**2 + m.x224**2 + m.x231**2 + m.x232**2 - 2*m.x223*m.x231 - 2*m.x224*m.x232
                           - 0.887203867225*m.b98 - 0.887203867225*m.b152 >= -0.887203867225)

m.c1310 = Constraint(expr=m.x223**2 + m.x224**2 + m.x233**2 + m.x234**2 - 2*m.x223*m.x233 - 2*m.x224*m.x234
                           - 0.887203867225*m.b98 - 0.887203867225*m.b167 >= -0.887203867225)

m.c1311 = Constraint(expr=m.x223**2 + m.x224**2 + m.x235**2 + m.x236**2 - 2*m.x223*m.x235 - 2*m.x224*m.x236
                           - 0.887203867225*m.b98 - 0.887203867225*m.b182 >= -0.887203867225)

m.c1312 = Constraint(expr=m.x215**2 + m.x216**2 + m.x225**2 + m.x226**2 - 2*m.x215*m.x225 - 2*m.x216*m.x226
                           - 1.436939228176*m.b62 - 1.436939228176*m.b107 >= -1.436939228176)

m.c1313 = Constraint(expr=m.x217**2 + m.x218**2 + m.x225**2 + m.x226**2 - 2*m.x218*m.x226 - 2*m.x217*m.x225
                           - 1.436939228176*m.b71 - 1.436939228176*m.b107 >= -1.436939228176)

m.c1314 = Constraint(expr=m.x219**2 + m.x220**2 + m.x225**2 + m.x226**2 - 2*m.x220*m.x226 - 2*m.x219*m.x225
                           - 1.436939228176*m.b80 - 1.436939228176*m.b107 >= -1.436939228176)

m.c1315 = Constraint(expr=m.x221**2 + m.x222**2 + m.x225**2 + m.x226**2 - 2*m.x221*m.x225 - 2*m.x222*m.x226
                           - 1.436939228176*m.b89 - 1.436939228176*m.b107 >= -1.436939228176)

m.c1316 = Constraint(expr=m.x223**2 + m.x224**2 + m.x225**2 + m.x226**2 - 2*m.x223*m.x225 - 2*m.x224*m.x226
                           - 1.436939228176*m.b98 - 1.436939228176*m.b107 >= -1.436939228176)

m.c1317 = Constraint(expr=m.x225**2 + m.x226**2 + m.x227**2 + m.x228**2 - 2*m.x225*m.x227 - 2*m.x226*m.x228
                           - 0.887203867225*m.b107 - 0.887203867225*m.b122 >= -0.887203867225)

m.c1318 = Constraint(expr=m.x225**2 + m.x226**2 + m.x229**2 + m.x230**2 - 2*m.x225*m.x229 - 2*m.x226*m.x230
                           - 0.887203867225*m.b107 - 0.887203867225*m.b137 >= -0.887203867225)

m.c1319 = Constraint(expr=m.x225**2 + m.x226**2 + m.x231**2 + m.x232**2 - 2*m.x225*m.x231 - 2*m.x226*m.x232
                           - 0.887203867225*m.b107 - 0.887203867225*m.b152 >= -0.887203867225)

m.c1320 = Constraint(expr=m.x225**2 + m.x226**2 + m.x233**2 + m.x234**2 - 2*m.x225*m.x233 - 2*m.x226*m.x234
                           - 0.887203867225*m.b107 - 0.887203867225*m.b167 >= -0.887203867225)

m.c1321 = Constraint(expr=m.x225**2 + m.x226**2 + m.x235**2 + m.x236**2 - 2*m.x225*m.x235 - 2*m.x226*m.x236
                           - 0.887203867225*m.b107 - 0.887203867225*m.b182 >= -0.887203867225)

m.c1322 = Constraint(expr=m.x215**2 + m.x216**2 + m.x227**2 + m.x228**2 - 2*m.x216*m.x228 - 2*m.x215*m.x227
                           - 0.887203867225*m.b62 - 0.887203867225*m.b122 >= -0.887203867225)

m.c1323 = Constraint(expr=m.x217**2 + m.x218**2 + m.x227**2 + m.x228**2 - 2*m.x217*m.x227 - 2*m.x218*m.x228
                           - 0.887203867225*m.b71 - 0.887203867225*m.b122 >= -0.887203867225)

m.c1324 = Constraint(expr=m.x219**2 + m.x220**2 + m.x227**2 + m.x228**2 - 2*m.x220*m.x228 - 2*m.x219*m.x227
                           - 0.887203867225*m.b80 - 0.887203867225*m.b122 >= -0.887203867225)

m.c1325 = Constraint(expr=m.x221**2 + m.x222**2 + m.x227**2 + m.x228**2 - 2*m.x221*m.x227 - 2*m.x222*m.x228
                           - 0.887203867225*m.b89 - 0.887203867225*m.b122 >= -0.887203867225)

m.c1326 = Constraint(expr=m.x223**2 + m.x224**2 + m.x227**2 + m.x228**2 - 2*m.x223*m.x227 - 2*m.x224*m.x228
                           - 0.887203867225*m.b98 - 0.887203867225*m.b122 >= -0.887203867225)

m.c1327 = Constraint(expr=m.x225**2 + m.x226**2 + m.x227**2 + m.x228**2 - 2*m.x225*m.x227 - 2*m.x226*m.x228
                           - 0.887203867225*m.b107 - 0.887203867225*m.b122 >= -0.887203867225)

m.c1328 = Constraint(expr=m.x227**2 + m.x228**2 + m.x229**2 + m.x230**2 - 2*m.x227*m.x229 - 2*m.x228*m.x230
                           - 0.469370231236*m.b122 - 0.469370231236*m.b137 >= -0.469370231236)

m.c1329 = Constraint(expr=m.x227**2 + m.x228**2 + m.x231**2 + m.x232**2 - 2*m.x227*m.x231 - 2*m.x228*m.x232
                           - 0.469370231236*m.b122 - 0.469370231236*m.b152 >= -0.469370231236)

m.c1330 = Constraint(expr=m.x227**2 + m.x228**2 + m.x233**2 + m.x234**2 - 2*m.x227*m.x233 - 2*m.x228*m.x234
                           - 0.469370231236*m.b122 - 0.469370231236*m.b167 >= -0.469370231236)

m.c1331 = Constraint(expr=m.x227**2 + m.x228**2 + m.x235**2 + m.x236**2 - 2*m.x227*m.x235 - 2*m.x228*m.x236
                           - 0.469370231236*m.b122 - 0.469370231236*m.b182 >= -0.469370231236)

m.c1332 = Constraint(expr=m.x215**2 + m.x216**2 + m.x229**2 + m.x230**2 - 2*m.x215*m.x229 - 2*m.x216*m.x230
                           - 0.887203867225*m.b62 - 0.887203867225*m.b137 >= -0.887203867225)

m.c1333 = Constraint(expr=m.x217**2 + m.x218**2 + m.x229**2 + m.x230**2 - 2*m.x218*m.x230 - 2*m.x217*m.x229
                           - 0.887203867225*m.b71 - 0.887203867225*m.b137 >= -0.887203867225)

m.c1334 = Constraint(expr=m.x219**2 + m.x220**2 + m.x229**2 + m.x230**2 - 2*m.x220*m.x230 - 2*m.x219*m.x229
                           - 0.887203867225*m.b80 - 0.887203867225*m.b137 >= -0.887203867225)

m.c1335 = Constraint(expr=m.x221**2 + m.x222**2 + m.x229**2 + m.x230**2 - 2*m.x221*m.x229 - 2*m.x222*m.x230
                           - 0.887203867225*m.b89 - 0.887203867225*m.b137 >= -0.887203867225)

m.c1336 = Constraint(expr=m.x223**2 + m.x224**2 + m.x229**2 + m.x230**2 - 2*m.x223*m.x229 - 2*m.x224*m.x230
                           - 0.887203867225*m.b98 - 0.887203867225*m.b137 >= -0.887203867225)

m.c1337 = Constraint(expr=m.x225**2 + m.x226**2 + m.x229**2 + m.x230**2 - 2*m.x225*m.x229 - 2*m.x226*m.x230
                           - 0.887203867225*m.b107 - 0.887203867225*m.b137 >= -0.887203867225)

m.c1338 = Constraint(expr=m.x227**2 + m.x228**2 + m.x229**2 + m.x230**2 - 2*m.x227*m.x229 - 2*m.x228*m.x230
                           - 0.469370231236*m.b122 - 0.469370231236*m.b137 >= -0.469370231236)

m.c1339 = Constraint(expr=m.x229**2 + m.x230**2 + m.x231**2 + m.x232**2 - 2*m.x229*m.x231 - 2*m.x230*m.x232
                           - 0.469370231236*m.b137 - 0.469370231236*m.b152 >= -0.469370231236)

m.c1340 = Constraint(expr=m.x229**2 + m.x230**2 + m.x233**2 + m.x234**2 - 2*m.x229*m.x233 - 2*m.x230*m.x234
                           - 0.469370231236*m.b137 - 0.469370231236*m.b167 >= -0.469370231236)

m.c1341 = Constraint(expr=m.x229**2 + m.x230**2 + m.x235**2 + m.x236**2 - 2*m.x229*m.x235 - 2*m.x230*m.x236
                           - 0.469370231236*m.b137 - 0.469370231236*m.b182 >= -0.469370231236)

m.c1342 = Constraint(expr=m.x215**2 + m.x216**2 + m.x231**2 + m.x232**2 - 2*m.x216*m.x232 - 2*m.x215*m.x231
                           - 0.887203867225*m.b62 - 0.887203867225*m.b152 >= -0.887203867225)

m.c1343 = Constraint(expr=m.x217**2 + m.x218**2 + m.x231**2 + m.x232**2 - 2*m.x218*m.x232 - 2*m.x217*m.x231
                           - 0.887203867225*m.b71 - 0.887203867225*m.b152 >= -0.887203867225)

m.c1344 = Constraint(expr=m.x219**2 + m.x220**2 + m.x231**2 + m.x232**2 - 2*m.x219*m.x231 - 2*m.x220*m.x232
                           - 0.887203867225*m.b80 - 0.887203867225*m.b152 >= -0.887203867225)

m.c1345 = Constraint(expr=m.x221**2 + m.x222**2 + m.x231**2 + m.x232**2 - 2*m.x221*m.x231 - 2*m.x222*m.x232
                           - 0.887203867225*m.b89 - 0.887203867225*m.b152 >= -0.887203867225)

m.c1346 = Constraint(expr=m.x223**2 + m.x224**2 + m.x231**2 + m.x232**2 - 2*m.x223*m.x231 - 2*m.x224*m.x232
                           - 0.887203867225*m.b98 - 0.887203867225*m.b152 >= -0.887203867225)

m.c1347 = Constraint(expr=m.x225**2 + m.x226**2 + m.x231**2 + m.x232**2 - 2*m.x225*m.x231 - 2*m.x226*m.x232
                           - 0.887203867225*m.b107 - 0.887203867225*m.b152 >= -0.887203867225)

m.c1348 = Constraint(expr=m.x227**2 + m.x228**2 + m.x231**2 + m.x232**2 - 2*m.x227*m.x231 - 2*m.x228*m.x232
                           - 0.469370231236*m.b122 - 0.469370231236*m.b152 >= -0.469370231236)

m.c1349 = Constraint(expr=m.x229**2 + m.x230**2 + m.x231**2 + m.x232**2 - 2*m.x229*m.x231 - 2*m.x230*m.x232
                           - 0.469370231236*m.b137 - 0.469370231236*m.b152 >= -0.469370231236)

m.c1350 = Constraint(expr=m.x231**2 + m.x232**2 + m.x233**2 + m.x234**2 - 2*m.x231*m.x233 - 2*m.x232*m.x234
                           - 0.469370231236*m.b152 - 0.469370231236*m.b167 >= -0.469370231236)

m.c1351 = Constraint(expr=m.x231**2 + m.x232**2 + m.x235**2 + m.x236**2 - 2*m.x231*m.x235 - 2*m.x232*m.x236
                           - 0.469370231236*m.b152 - 0.469370231236*m.b182 >= -0.469370231236)

m.c1352 = Constraint(expr=m.x215**2 + m.x216**2 + m.x233**2 + m.x234**2 - 2*m.x216*m.x234 - 2*m.x215*m.x233
                           - 0.887203867225*m.b62 - 0.887203867225*m.b167 >= -0.887203867225)

m.c1353 = Constraint(expr=m.x217**2 + m.x218**2 + m.x233**2 + m.x234**2 - 2*m.x217*m.x233 - 2*m.x218*m.x234
                           - 0.887203867225*m.b71 - 0.887203867225*m.b167 >= -0.887203867225)

m.c1354 = Constraint(expr=m.x219**2 + m.x220**2 + m.x233**2 + m.x234**2 - 2*m.x219*m.x233 - 2*m.x220*m.x234
                           - 0.887203867225*m.b80 - 0.887203867225*m.b167 >= -0.887203867225)

m.c1355 = Constraint(expr=m.x221**2 + m.x222**2 + m.x233**2 + m.x234**2 - 2*m.x221*m.x233 - 2*m.x222*m.x234
                           - 0.887203867225*m.b89 - 0.887203867225*m.b167 >= -0.887203867225)

m.c1356 = Constraint(expr=m.x223**2 + m.x224**2 + m.x233**2 + m.x234**2 - 2*m.x223*m.x233 - 2*m.x224*m.x234
                           - 0.887203867225*m.b98 - 0.887203867225*m.b167 >= -0.887203867225)

m.c1357 = Constraint(expr=m.x225**2 + m.x226**2 + m.x233**2 + m.x234**2 - 2*m.x225*m.x233 - 2*m.x226*m.x234
                           - 0.887203867225*m.b107 - 0.887203867225*m.b167 >= -0.887203867225)

m.c1358 = Constraint(expr=m.x227**2 + m.x228**2 + m.x233**2 + m.x234**2 - 2*m.x227*m.x233 - 2*m.x228*m.x234
                           - 0.469370231236*m.b122 - 0.469370231236*m.b167 >= -0.469370231236)

m.c1359 = Constraint(expr=m.x229**2 + m.x230**2 + m.x233**2 + m.x234**2 - 2*m.x229*m.x233 - 2*m.x230*m.x234
                           - 0.469370231236*m.b137 - 0.469370231236*m.b167 >= -0.469370231236)

m.c1360 = Constraint(expr=m.x231**2 + m.x232**2 + m.x233**2 + m.x234**2 - 2*m.x231*m.x233 - 2*m.x232*m.x234
                           - 0.469370231236*m.b152 - 0.469370231236*m.b167 >= -0.469370231236)

m.c1361 = Constraint(expr=m.x233**2 + m.x234**2 + m.x235**2 + m.x236**2 - 2*m.x233*m.x235 - 2*m.x234*m.x236
                           - 0.469370231236*m.b167 - 0.469370231236*m.b182 >= -0.469370231236)

m.c1362 = Constraint(expr=m.x215**2 + m.x216**2 + m.x235**2 + m.x236**2 - 2*m.x215*m.x235 - 2*m.x216*m.x236
                           - 0.887203867225*m.b62 - 0.887203867225*m.b182 >= -0.887203867225)

m.c1363 = Constraint(expr=m.x217**2 + m.x218**2 + m.x235**2 + m.x236**2 - 2*m.x217*m.x235 - 2*m.x218*m.x236
                           - 0.887203867225*m.b71 - 0.887203867225*m.b182 >= -0.887203867225)

m.c1364 = Constraint(expr=m.x219**2 + m.x220**2 + m.x235**2 + m.x236**2 - 2*m.x219*m.x235 - 2*m.x220*m.x236
                           - 0.887203867225*m.b80 - 0.887203867225*m.b182 >= -0.887203867225)

m.c1365 = Constraint(expr=m.x221**2 + m.x222**2 + m.x235**2 + m.x236**2 - 2*m.x221*m.x235 - 2*m.x222*m.x236
                           - 0.887203867225*m.b89 - 0.887203867225*m.b182 >= -0.887203867225)

m.c1366 = Constraint(expr=m.x223**2 + m.x224**2 + m.x235**2 + m.x236**2 - 2*m.x223*m.x235 - 2*m.x224*m.x236
                           - 0.887203867225*m.b98 - 0.887203867225*m.b182 >= -0.887203867225)

m.c1367 = Constraint(expr=m.x225**2 + m.x226**2 + m.x235**2 + m.x236**2 - 2*m.x225*m.x235 - 2*m.x226*m.x236
                           - 0.887203867225*m.b107 - 0.887203867225*m.b182 >= -0.887203867225)

m.c1368 = Constraint(expr=m.x227**2 + m.x228**2 + m.x235**2 + m.x236**2 - 2*m.x227*m.x235 - 2*m.x228*m.x236
                           - 0.469370231236*m.b122 - 0.469370231236*m.b182 >= -0.469370231236)

m.c1369 = Constraint(expr=m.x229**2 + m.x230**2 + m.x235**2 + m.x236**2 - 2*m.x229*m.x235 - 2*m.x230*m.x236
                           - 0.469370231236*m.b137 - 0.469370231236*m.b182 >= -0.469370231236)

m.c1370 = Constraint(expr=m.x231**2 + m.x232**2 + m.x235**2 + m.x236**2 - 2*m.x231*m.x235 - 2*m.x232*m.x236
                           - 0.469370231236*m.b152 - 0.469370231236*m.b182 >= -0.469370231236)

m.c1371 = Constraint(expr=m.x233**2 + m.x234**2 + m.x235**2 + m.x236**2 - 2*m.x233*m.x235 - 2*m.x234*m.x236
                           - 0.469370231236*m.b167 - 0.469370231236*m.b182 >= -0.469370231236)

m.c1372 = Constraint(expr=m.x215**2 + m.x216**2 + m.x217**2 + m.x218**2 - 2*m.x215*m.x217 - 2*m.x216*m.x218
                           - 1.436939228176*m.b63 - 1.436939228176*m.b72 >= -1.436939228176)

m.c1373 = Constraint(expr=m.x215**2 + m.x216**2 + m.x219**2 + m.x220**2 - 2*m.x215*m.x219 - 2*m.x216*m.x220
                           - 1.436939228176*m.b63 - 1.436939228176*m.b81 >= -1.436939228176)

m.c1374 = Constraint(expr=m.x215**2 + m.x216**2 + m.x221**2 + m.x222**2 - 2*m.x216*m.x222 - 2*m.x215*m.x221
                           - 1.436939228176*m.b63 - 1.436939228176*m.b90 >= -1.436939228176)

m.c1375 = Constraint(expr=m.x215**2 + m.x216**2 + m.x223**2 + m.x224**2 - 2*m.x216*m.x224 - 2*m.x215*m.x223
                           - 1.436939228176*m.b63 - 1.436939228176*m.b99 >= -1.436939228176)

m.c1376 = Constraint(expr=m.x215**2 + m.x216**2 + m.x225**2 + m.x226**2 - 2*m.x215*m.x225 - 2*m.x216*m.x226
                           - 1.436939228176*m.b63 - 1.436939228176*m.b108 >= -1.436939228176)

m.c1377 = Constraint(expr=m.x215**2 + m.x216**2 + m.x227**2 + m.x228**2 - 2*m.x216*m.x228 - 2*m.x215*m.x227
                           - 0.887203867225*m.b63 - 0.887203867225*m.b123 >= -0.887203867225)

m.c1378 = Constraint(expr=m.x215**2 + m.x216**2 + m.x229**2 + m.x230**2 - 2*m.x215*m.x229 - 2*m.x216*m.x230
                           - 0.887203867225*m.b63 - 0.887203867225*m.b138 >= -0.887203867225)

m.c1379 = Constraint(expr=m.x215**2 + m.x216**2 + m.x231**2 + m.x232**2 - 2*m.x216*m.x232 - 2*m.x215*m.x231
                           - 0.887203867225*m.b63 - 0.887203867225*m.b153 >= -0.887203867225)

m.c1380 = Constraint(expr=m.x215**2 + m.x216**2 + m.x233**2 + m.x234**2 - 2*m.x216*m.x234 - 2*m.x215*m.x233
                           - 0.887203867225*m.b63 - 0.887203867225*m.b168 >= -0.887203867225)

m.c1381 = Constraint(expr=m.x215**2 + m.x216**2 + m.x235**2 + m.x236**2 - 2*m.x216*m.x236 - 2*m.x215*m.x235
                           - 0.887203867225*m.b63 - 0.887203867225*m.b183 >= -0.887203867225)

m.c1382 = Constraint(expr=m.x215**2 + m.x216**2 + m.x217**2 + m.x218**2 - 2*m.x215*m.x217 - 2*m.x216*m.x218
                           - 1.436939228176*m.b63 - 1.436939228176*m.b72 >= -1.436939228176)

m.c1383 = Constraint(expr=m.x217**2 + m.x218**2 + m.x219**2 + m.x220**2 - 2*m.x217*m.x219 - 2*m.x218*m.x220
                           - 1.436939228176*m.b72 - 1.436939228176*m.b81 >= -1.436939228176)

m.c1384 = Constraint(expr=m.x217**2 + m.x218**2 + m.x221**2 + m.x222**2 - 2*m.x218*m.x222 - 2*m.x217*m.x221
                           - 1.436939228176*m.b72 - 1.436939228176*m.b90 >= -1.436939228176)

m.c1385 = Constraint(expr=m.x217**2 + m.x218**2 + m.x223**2 + m.x224**2 - 2*m.x217*m.x223 - 2*m.x218*m.x224
                           - 1.436939228176*m.b72 - 1.436939228176*m.b99 >= -1.436939228176)

m.c1386 = Constraint(expr=m.x217**2 + m.x218**2 + m.x225**2 + m.x226**2 - 2*m.x218*m.x226 - 2*m.x217*m.x225
                           - 1.436939228176*m.b72 - 1.436939228176*m.b108 >= -1.436939228176)

m.c1387 = Constraint(expr=m.x217**2 + m.x218**2 + m.x227**2 + m.x228**2 - 2*m.x217*m.x227 - 2*m.x218*m.x228
                           - 0.887203867225*m.b72 - 0.887203867225*m.b123 >= -0.887203867225)

m.c1388 = Constraint(expr=m.x217**2 + m.x218**2 + m.x229**2 + m.x230**2 - 2*m.x218*m.x230 - 2*m.x217*m.x229
                           - 0.887203867225*m.b72 - 0.887203867225*m.b138 >= -0.887203867225)

m.c1389 = Constraint(expr=m.x217**2 + m.x218**2 + m.x231**2 + m.x232**2 - 2*m.x218*m.x232 - 2*m.x217*m.x231
                           - 0.887203867225*m.b72 - 0.887203867225*m.b153 >= -0.887203867225)

m.c1390 = Constraint(expr=m.x217**2 + m.x218**2 + m.x233**2 + m.x234**2 - 2*m.x217*m.x233 - 2*m.x218*m.x234
                           - 0.887203867225*m.b72 - 0.887203867225*m.b168 >= -0.887203867225)

m.c1391 = Constraint(expr=m.x217**2 + m.x218**2 + m.x235**2 + m.x236**2 - 2*m.x218*m.x236 - 2*m.x217*m.x235
                           - 0.887203867225*m.b72 - 0.887203867225*m.b183 >= -0.887203867225)

m.c1392 = Constraint(expr=m.x215**2 + m.x216**2 + m.x219**2 + m.x220**2 - 2*m.x215*m.x219 - 2*m.x216*m.x220
                           - 1.436939228176*m.b63 - 1.436939228176*m.b81 >= -1.436939228176)

m.c1393 = Constraint(expr=m.x217**2 + m.x218**2 + m.x219**2 + m.x220**2 - 2*m.x217*m.x219 - 2*m.x218*m.x220
                           - 1.436939228176*m.b72 - 1.436939228176*m.b81 >= -1.436939228176)

m.c1394 = Constraint(expr=m.x219**2 + m.x220**2 + m.x221**2 + m.x222**2 - 2*m.x219*m.x221 - 2*m.x220*m.x222
                           - 1.436939228176*m.b81 - 1.436939228176*m.b90 >= -1.436939228176)

m.c1395 = Constraint(expr=m.x219**2 + m.x220**2 + m.x223**2 + m.x224**2 - 2*m.x220*m.x224 - 2*m.x219*m.x223
                           - 1.436939228176*m.b81 - 1.436939228176*m.b99 >= -1.436939228176)

m.c1396 = Constraint(expr=m.x219**2 + m.x220**2 + m.x225**2 + m.x226**2 - 2*m.x220*m.x226 - 2*m.x219*m.x225
                           - 1.436939228176*m.b81 - 1.436939228176*m.b108 >= -1.436939228176)

m.c1397 = Constraint(expr=m.x219**2 + m.x220**2 + m.x227**2 + m.x228**2 - 2*m.x220*m.x228 - 2*m.x219*m.x227
                           - 0.887203867225*m.b81 - 0.887203867225*m.b123 >= -0.887203867225)

m.c1398 = Constraint(expr=m.x219**2 + m.x220**2 + m.x229**2 + m.x230**2 - 2*m.x220*m.x230 - 2*m.x219*m.x229
                           - 0.887203867225*m.b81 - 0.887203867225*m.b138 >= -0.887203867225)

m.c1399 = Constraint(expr=m.x219**2 + m.x220**2 + m.x231**2 + m.x232**2 - 2*m.x219*m.x231 - 2*m.x220*m.x232
                           - 0.887203867225*m.b81 - 0.887203867225*m.b153 >= -0.887203867225)

m.c1400 = Constraint(expr=m.x219**2 + m.x220**2 + m.x233**2 + m.x234**2 - 2*m.x219*m.x233 - 2*m.x220*m.x234
                           - 0.887203867225*m.b81 - 0.887203867225*m.b168 >= -0.887203867225)

m.c1401 = Constraint(expr=m.x219**2 + m.x220**2 + m.x235**2 + m.x236**2 - 2*m.x219*m.x235 - 2*m.x220*m.x236
                           - 0.887203867225*m.b81 - 0.887203867225*m.b183 >= -0.887203867225)

m.c1402 = Constraint(expr=m.x215**2 + m.x216**2 + m.x221**2 + m.x222**2 - 2*m.x216*m.x222 - 2*m.x215*m.x221
                           - 1.436939228176*m.b63 - 1.436939228176*m.b90 >= -1.436939228176)

m.c1403 = Constraint(expr=m.x217**2 + m.x218**2 + m.x221**2 + m.x222**2 - 2*m.x218*m.x222 - 2*m.x217*m.x221
                           - 1.436939228176*m.b72 - 1.436939228176*m.b90 >= -1.436939228176)

m.c1404 = Constraint(expr=m.x219**2 + m.x220**2 + m.x221**2 + m.x222**2 - 2*m.x219*m.x221 - 2*m.x220*m.x222
                           - 1.436939228176*m.b81 - 1.436939228176*m.b90 >= -1.436939228176)

m.c1405 = Constraint(expr=m.x221**2 + m.x222**2 + m.x223**2 + m.x224**2 - 2*m.x221*m.x223 - 2*m.x222*m.x224
                           - 1.436939228176*m.b90 - 1.436939228176*m.b99 >= -1.436939228176)

m.c1406 = Constraint(expr=m.x221**2 + m.x222**2 + m.x225**2 + m.x226**2 - 2*m.x221*m.x225 - 2*m.x222*m.x226
                           - 1.436939228176*m.b90 - 1.436939228176*m.b108 >= -1.436939228176)

m.c1407 = Constraint(expr=m.x221**2 + m.x222**2 + m.x227**2 + m.x228**2 - 2*m.x221*m.x227 - 2*m.x222*m.x228
                           - 0.887203867225*m.b90 - 0.887203867225*m.b123 >= -0.887203867225)

m.c1408 = Constraint(expr=m.x221**2 + m.x222**2 + m.x229**2 + m.x230**2 - 2*m.x221*m.x229 - 2*m.x222*m.x230
                           - 0.887203867225*m.b90 - 0.887203867225*m.b138 >= -0.887203867225)

m.c1409 = Constraint(expr=m.x221**2 + m.x222**2 + m.x231**2 + m.x232**2 - 2*m.x221*m.x231 - 2*m.x222*m.x232
                           - 0.887203867225*m.b90 - 0.887203867225*m.b153 >= -0.887203867225)

m.c1410 = Constraint(expr=m.x221**2 + m.x222**2 + m.x233**2 + m.x234**2 - 2*m.x221*m.x233 - 2*m.x222*m.x234
                           - 0.887203867225*m.b90 - 0.887203867225*m.b168 >= -0.887203867225)

m.c1411 = Constraint(expr=m.x221**2 + m.x222**2 + m.x235**2 + m.x236**2 - 2*m.x221*m.x235 - 2*m.x222*m.x236
                           - 0.887203867225*m.b90 - 0.887203867225*m.b183 >= -0.887203867225)

m.c1412 = Constraint(expr=m.x215**2 + m.x216**2 + m.x223**2 + m.x224**2 - 2*m.x216*m.x224 - 2*m.x215*m.x223
                           - 1.436939228176*m.b63 - 1.436939228176*m.b99 >= -1.436939228176)

m.c1413 = Constraint(expr=m.x217**2 + m.x218**2 + m.x223**2 + m.x224**2 - 2*m.x217*m.x223 - 2*m.x218*m.x224
                           - 1.436939228176*m.b72 - 1.436939228176*m.b99 >= -1.436939228176)

m.c1414 = Constraint(expr=m.x219**2 + m.x220**2 + m.x223**2 + m.x224**2 - 2*m.x220*m.x224 - 2*m.x219*m.x223
                           - 1.436939228176*m.b81 - 1.436939228176*m.b99 >= -1.436939228176)

m.c1415 = Constraint(expr=m.x221**2 + m.x222**2 + m.x223**2 + m.x224**2 - 2*m.x221*m.x223 - 2*m.x222*m.x224
                           - 1.436939228176*m.b90 - 1.436939228176*m.b99 >= -1.436939228176)

m.c1416 = Constraint(expr=m.x223**2 + m.x224**2 + m.x225**2 + m.x226**2 - 2*m.x223*m.x225 - 2*m.x224*m.x226
                           - 1.436939228176*m.b99 - 1.436939228176*m.b108 >= -1.436939228176)

m.c1417 = Constraint(expr=m.x223**2 + m.x224**2 + m.x227**2 + m.x228**2 - 2*m.x223*m.x227 - 2*m.x224*m.x228
                           - 0.887203867225*m.b99 - 0.887203867225*m.b123 >= -0.887203867225)

m.c1418 = Constraint(expr=m.x223**2 + m.x224**2 + m.x229**2 + m.x230**2 - 2*m.x223*m.x229 - 2*m.x224*m.x230
                           - 0.887203867225*m.b99 - 0.887203867225*m.b138 >= -0.887203867225)

m.c1419 = Constraint(expr=m.x223**2 + m.x224**2 + m.x231**2 + m.x232**2 - 2*m.x223*m.x231 - 2*m.x224*m.x232
                           - 0.887203867225*m.b99 - 0.887203867225*m.b153 >= -0.887203867225)

m.c1420 = Constraint(expr=m.x223**2 + m.x224**2 + m.x233**2 + m.x234**2 - 2*m.x223*m.x233 - 2*m.x224*m.x234
                           - 0.887203867225*m.b99 - 0.887203867225*m.b168 >= -0.887203867225)

m.c1421 = Constraint(expr=m.x223**2 + m.x224**2 + m.x235**2 + m.x236**2 - 2*m.x223*m.x235 - 2*m.x224*m.x236
                           - 0.887203867225*m.b99 - 0.887203867225*m.b183 >= -0.887203867225)

m.c1422 = Constraint(expr=m.x215**2 + m.x216**2 + m.x225**2 + m.x226**2 - 2*m.x215*m.x225 - 2*m.x216*m.x226
                           - 1.436939228176*m.b63 - 1.436939228176*m.b108 >= -1.436939228176)

m.c1423 = Constraint(expr=m.x217**2 + m.x218**2 + m.x225**2 + m.x226**2 - 2*m.x218*m.x226 - 2*m.x217*m.x225
                           - 1.436939228176*m.b72 - 1.436939228176*m.b108 >= -1.436939228176)

m.c1424 = Constraint(expr=m.x219**2 + m.x220**2 + m.x225**2 + m.x226**2 - 2*m.x220*m.x226 - 2*m.x219*m.x225
                           - 1.436939228176*m.b81 - 1.436939228176*m.b108 >= -1.436939228176)

m.c1425 = Constraint(expr=m.x221**2 + m.x222**2 + m.x225**2 + m.x226**2 - 2*m.x221*m.x225 - 2*m.x222*m.x226
                           - 1.436939228176*m.b90 - 1.436939228176*m.b108 >= -1.436939228176)

m.c1426 = Constraint(expr=m.x223**2 + m.x224**2 + m.x225**2 + m.x226**2 - 2*m.x223*m.x225 - 2*m.x224*m.x226
                           - 1.436939228176*m.b99 - 1.436939228176*m.b108 >= -1.436939228176)

m.c1427 = Constraint(expr=m.x225**2 + m.x226**2 + m.x227**2 + m.x228**2 - 2*m.x225*m.x227 - 2*m.x226*m.x228
                           - 0.887203867225*m.b108 - 0.887203867225*m.b123 >= -0.887203867225)

m.c1428 = Constraint(expr=m.x225**2 + m.x226**2 + m.x229**2 + m.x230**2 - 2*m.x225*m.x229 - 2*m.x226*m.x230
                           - 0.887203867225*m.b108 - 0.887203867225*m.b138 >= -0.887203867225)

m.c1429 = Constraint(expr=m.x225**2 + m.x226**2 + m.x231**2 + m.x232**2 - 2*m.x225*m.x231 - 2*m.x226*m.x232
                           - 0.887203867225*m.b108 - 0.887203867225*m.b153 >= -0.887203867225)

m.c1430 = Constraint(expr=m.x225**2 + m.x226**2 + m.x233**2 + m.x234**2 - 2*m.x225*m.x233 - 2*m.x226*m.x234
                           - 0.887203867225*m.b108 - 0.887203867225*m.b168 >= -0.887203867225)

m.c1431 = Constraint(expr=m.x225**2 + m.x226**2 + m.x235**2 + m.x236**2 - 2*m.x225*m.x235 - 2*m.x226*m.x236
                           - 0.887203867225*m.b108 - 0.887203867225*m.b183 >= -0.887203867225)

m.c1432 = Constraint(expr=m.x215**2 + m.x216**2 + m.x227**2 + m.x228**2 - 2*m.x216*m.x228 - 2*m.x215*m.x227
                           - 0.887203867225*m.b63 - 0.887203867225*m.b123 >= -0.887203867225)

m.c1433 = Constraint(expr=m.x217**2 + m.x218**2 + m.x227**2 + m.x228**2 - 2*m.x217*m.x227 - 2*m.x218*m.x228
                           - 0.887203867225*m.b72 - 0.887203867225*m.b123 >= -0.887203867225)

m.c1434 = Constraint(expr=m.x219**2 + m.x220**2 + m.x227**2 + m.x228**2 - 2*m.x220*m.x228 - 2*m.x219*m.x227
                           - 0.887203867225*m.b81 - 0.887203867225*m.b123 >= -0.887203867225)

m.c1435 = Constraint(expr=m.x221**2 + m.x222**2 + m.x227**2 + m.x228**2 - 2*m.x221*m.x227 - 2*m.x222*m.x228
                           - 0.887203867225*m.b90 - 0.887203867225*m.b123 >= -0.887203867225)

m.c1436 = Constraint(expr=m.x223**2 + m.x224**2 + m.x227**2 + m.x228**2 - 2*m.x223*m.x227 - 2*m.x224*m.x228
                           - 0.887203867225*m.b99 - 0.887203867225*m.b123 >= -0.887203867225)

m.c1437 = Constraint(expr=m.x225**2 + m.x226**2 + m.x227**2 + m.x228**2 - 2*m.x225*m.x227 - 2*m.x226*m.x228
                           - 0.887203867225*m.b108 - 0.887203867225*m.b123 >= -0.887203867225)

m.c1438 = Constraint(expr=m.x227**2 + m.x228**2 + m.x229**2 + m.x230**2 - 2*m.x227*m.x229 - 2*m.x228*m.x230
                           - 0.469370231236*m.b123 - 0.469370231236*m.b138 >= -0.469370231236)

m.c1439 = Constraint(expr=m.x227**2 + m.x228**2 + m.x231**2 + m.x232**2 - 2*m.x227*m.x231 - 2*m.x228*m.x232
                           - 0.469370231236*m.b123 - 0.469370231236*m.b153 >= -0.469370231236)

m.c1440 = Constraint(expr=m.x227**2 + m.x228**2 + m.x233**2 + m.x234**2 - 2*m.x227*m.x233 - 2*m.x228*m.x234
                           - 0.469370231236*m.b123 - 0.469370231236*m.b168 >= -0.469370231236)

m.c1441 = Constraint(expr=m.x227**2 + m.x228**2 + m.x235**2 + m.x236**2 - 2*m.x227*m.x235 - 2*m.x228*m.x236
                           - 0.469370231236*m.b123 - 0.469370231236*m.b183 >= -0.469370231236)

m.c1442 = Constraint(expr=m.x215**2 + m.x216**2 + m.x229**2 + m.x230**2 - 2*m.x215*m.x229 - 2*m.x216*m.x230
                           - 0.887203867225*m.b63 - 0.887203867225*m.b138 >= -0.887203867225)

m.c1443 = Constraint(expr=m.x217**2 + m.x218**2 + m.x229**2 + m.x230**2 - 2*m.x218*m.x230 - 2*m.x217*m.x229
                           - 0.887203867225*m.b72 - 0.887203867225*m.b138 >= -0.887203867225)

m.c1444 = Constraint(expr=m.x219**2 + m.x220**2 + m.x229**2 + m.x230**2 - 2*m.x220*m.x230 - 2*m.x219*m.x229
                           - 0.887203867225*m.b81 - 0.887203867225*m.b138 >= -0.887203867225)

m.c1445 = Constraint(expr=m.x221**2 + m.x222**2 + m.x229**2 + m.x230**2 - 2*m.x221*m.x229 - 2*m.x222*m.x230
                           - 0.887203867225*m.b90 - 0.887203867225*m.b138 >= -0.887203867225)

m.c1446 = Constraint(expr=m.x223**2 + m.x224**2 + m.x229**2 + m.x230**2 - 2*m.x223*m.x229 - 2*m.x224*m.x230
                           - 0.887203867225*m.b99 - 0.887203867225*m.b138 >= -0.887203867225)

m.c1447 = Constraint(expr=m.x225**2 + m.x226**2 + m.x229**2 + m.x230**2 - 2*m.x225*m.x229 - 2*m.x226*m.x230
                           - 0.887203867225*m.b108 - 0.887203867225*m.b138 >= -0.887203867225)

m.c1448 = Constraint(expr=m.x227**2 + m.x228**2 + m.x229**2 + m.x230**2 - 2*m.x227*m.x229 - 2*m.x228*m.x230
                           - 0.469370231236*m.b123 - 0.469370231236*m.b138 >= -0.469370231236)

m.c1449 = Constraint(expr=m.x229**2 + m.x230**2 + m.x231**2 + m.x232**2 - 2*m.x229*m.x231 - 2*m.x230*m.x232
                           - 0.469370231236*m.b138 - 0.469370231236*m.b153 >= -0.469370231236)

m.c1450 = Constraint(expr=m.x229**2 + m.x230**2 + m.x233**2 + m.x234**2 - 2*m.x229*m.x233 - 2*m.x230*m.x234
                           - 0.469370231236*m.b138 - 0.469370231236*m.b168 >= -0.469370231236)

m.c1451 = Constraint(expr=m.x229**2 + m.x230**2 + m.x235**2 + m.x236**2 - 2*m.x229*m.x235 - 2*m.x230*m.x236
                           - 0.469370231236*m.b138 - 0.469370231236*m.b183 >= -0.469370231236)

m.c1452 = Constraint(expr=m.x215**2 + m.x216**2 + m.x231**2 + m.x232**2 - 2*m.x216*m.x232 - 2*m.x215*m.x231
                           - 0.887203867225*m.b63 - 0.887203867225*m.b153 >= -0.887203867225)

m.c1453 = Constraint(expr=m.x217**2 + m.x218**2 + m.x231**2 + m.x232**2 - 2*m.x218*m.x232 - 2*m.x217*m.x231
                           - 0.887203867225*m.b72 - 0.887203867225*m.b153 >= -0.887203867225)

m.c1454 = Constraint(expr=m.x219**2 + m.x220**2 + m.x231**2 + m.x232**2 - 2*m.x219*m.x231 - 2*m.x220*m.x232
                           - 0.887203867225*m.b81 - 0.887203867225*m.b153 >= -0.887203867225)

m.c1455 = Constraint(expr=m.x221**2 + m.x222**2 + m.x231**2 + m.x232**2 - 2*m.x221*m.x231 - 2*m.x222*m.x232
                           - 0.887203867225*m.b90 - 0.887203867225*m.b153 >= -0.887203867225)

m.c1456 = Constraint(expr=m.x223**2 + m.x224**2 + m.x231**2 + m.x232**2 - 2*m.x223*m.x231 - 2*m.x224*m.x232
                           - 0.887203867225*m.b99 - 0.887203867225*m.b153 >= -0.887203867225)

m.c1457 = Constraint(expr=m.x225**2 + m.x226**2 + m.x231**2 + m.x232**2 - 2*m.x225*m.x231 - 2*m.x226*m.x232
                           - 0.887203867225*m.b108 - 0.887203867225*m.b153 >= -0.887203867225)

m.c1458 = Constraint(expr=m.x227**2 + m.x228**2 + m.x231**2 + m.x232**2 - 2*m.x227*m.x231 - 2*m.x228*m.x232
                           - 0.469370231236*m.b123 - 0.469370231236*m.b153 >= -0.469370231236)

m.c1459 = Constraint(expr=m.x229**2 + m.x230**2 + m.x231**2 + m.x232**2 - 2*m.x229*m.x231 - 2*m.x230*m.x232
                           - 0.469370231236*m.b138 - 0.469370231236*m.b153 >= -0.469370231236)

m.c1460 = Constraint(expr=m.x231**2 + m.x232**2 + m.x233**2 + m.x234**2 - 2*m.x231*m.x233 - 2*m.x232*m.x234
                           - 0.469370231236*m.b153 - 0.469370231236*m.b168 >= -0.469370231236)

m.c1461 = Constraint(expr=m.x231**2 + m.x232**2 + m.x235**2 + m.x236**2 - 2*m.x231*m.x235 - 2*m.x232*m.x236
                           - 0.469370231236*m.b153 - 0.469370231236*m.b183 >= -0.469370231236)

m.c1462 = Constraint(expr=m.x215**2 + m.x216**2 + m.x233**2 + m.x234**2 - 2*m.x216*m.x234 - 2*m.x215*m.x233
                           - 0.887203867225*m.b63 - 0.887203867225*m.b168 >= -0.887203867225)

m.c1463 = Constraint(expr=m.x217**2 + m.x218**2 + m.x233**2 + m.x234**2 - 2*m.x217*m.x233 - 2*m.x218*m.x234
                           - 0.887203867225*m.b72 - 0.887203867225*m.b168 >= -0.887203867225)

m.c1464 = Constraint(expr=m.x219**2 + m.x220**2 + m.x233**2 + m.x234**2 - 2*m.x219*m.x233 - 2*m.x220*m.x234
                           - 0.887203867225*m.b81 - 0.887203867225*m.b168 >= -0.887203867225)

m.c1465 = Constraint(expr=m.x221**2 + m.x222**2 + m.x233**2 + m.x234**2 - 2*m.x221*m.x233 - 2*m.x222*m.x234
                           - 0.887203867225*m.b90 - 0.887203867225*m.b168 >= -0.887203867225)

m.c1466 = Constraint(expr=m.x223**2 + m.x224**2 + m.x233**2 + m.x234**2 - 2*m.x223*m.x233 - 2*m.x224*m.x234
                           - 0.887203867225*m.b99 - 0.887203867225*m.b168 >= -0.887203867225)

m.c1467 = Constraint(expr=m.x225**2 + m.x226**2 + m.x233**2 + m.x234**2 - 2*m.x225*m.x233 - 2*m.x226*m.x234
                           - 0.887203867225*m.b108 - 0.887203867225*m.b168 >= -0.887203867225)

m.c1468 = Constraint(expr=m.x227**2 + m.x228**2 + m.x233**2 + m.x234**2 - 2*m.x227*m.x233 - 2*m.x228*m.x234
                           - 0.469370231236*m.b123 - 0.469370231236*m.b168 >= -0.469370231236)

m.c1469 = Constraint(expr=m.x229**2 + m.x230**2 + m.x233**2 + m.x234**2 - 2*m.x229*m.x233 - 2*m.x230*m.x234
                           - 0.469370231236*m.b138 - 0.469370231236*m.b168 >= -0.469370231236)

m.c1470 = Constraint(expr=m.x231**2 + m.x232**2 + m.x233**2 + m.x234**2 - 2*m.x231*m.x233 - 2*m.x232*m.x234
                           - 0.469370231236*m.b153 - 0.469370231236*m.b168 >= -0.469370231236)

m.c1471 = Constraint(expr=m.x233**2 + m.x234**2 + m.x235**2 + m.x236**2 - 2*m.x233*m.x235 - 2*m.x234*m.x236
                           - 0.469370231236*m.b168 - 0.469370231236*m.b183 >= -0.469370231236)

m.c1472 = Constraint(expr=m.x215**2 + m.x216**2 + m.x235**2 + m.x236**2 - 2*m.x216*m.x236 - 2*m.x215*m.x235
                           - 0.887203867225*m.b63 - 0.887203867225*m.b183 >= -0.887203867225)

m.c1473 = Constraint(expr=m.x217**2 + m.x218**2 + m.x235**2 + m.x236**2 - 2*m.x217*m.x235 - 2*m.x218*m.x236
                           - 0.887203867225*m.b72 - 0.887203867225*m.b183 >= -0.887203867225)

m.c1474 = Constraint(expr=m.x219**2 + m.x220**2 + m.x235**2 + m.x236**2 - 2*m.x219*m.x235 - 2*m.x220*m.x236
                           - 0.887203867225*m.b81 - 0.887203867225*m.b183 >= -0.887203867225)

m.c1475 = Constraint(expr=m.x221**2 + m.x222**2 + m.x235**2 + m.x236**2 - 2*m.x221*m.x235 - 2*m.x222*m.x236
                           - 0.887203867225*m.b90 - 0.887203867225*m.b183 >= -0.887203867225)

m.c1476 = Constraint(expr=m.x223**2 + m.x224**2 + m.x235**2 + m.x236**2 - 2*m.x223*m.x235 - 2*m.x224*m.x236
                           - 0.887203867225*m.b99 - 0.887203867225*m.b183 >= -0.887203867225)

m.c1477 = Constraint(expr=m.x225**2 + m.x226**2 + m.x235**2 + m.x236**2 - 2*m.x225*m.x235 - 2*m.x226*m.x236
                           - 0.887203867225*m.b108 - 0.887203867225*m.b183 >= -0.887203867225)

m.c1478 = Constraint(expr=m.x227**2 + m.x228**2 + m.x235**2 + m.x236**2 - 2*m.x227*m.x235 - 2*m.x228*m.x236
                           - 0.469370231236*m.b123 - 0.469370231236*m.b183 >= -0.469370231236)

m.c1479 = Constraint(expr=m.x229**2 + m.x230**2 + m.x235**2 + m.x236**2 - 2*m.x229*m.x235 - 2*m.x230*m.x236
                           - 0.469370231236*m.b138 - 0.469370231236*m.b183 >= -0.469370231236)

m.c1480 = Constraint(expr=m.x231**2 + m.x232**2 + m.x235**2 + m.x236**2 - 2*m.x231*m.x235 - 2*m.x232*m.x236
                           - 0.469370231236*m.b153 - 0.469370231236*m.b183 >= -0.469370231236)

m.c1481 = Constraint(expr=m.x233**2 + m.x234**2 + m.x235**2 + m.x236**2 - 2*m.x233*m.x235 - 2*m.x234*m.x236
                           - 0.469370231236*m.b168 - 0.469370231236*m.b183 >= -0.469370231236)

m.c1482 = Constraint(expr=m.x215**2 + m.x216**2 + m.x217**2 + m.x218**2 - 2*m.x215*m.x217 - 2*m.x216*m.x218
                           - 1.436939228176*m.b64 - 1.436939228176*m.b73 >= -1.436939228176)

m.c1483 = Constraint(expr=m.x215**2 + m.x216**2 + m.x219**2 + m.x220**2 - 2*m.x215*m.x219 - 2*m.x216*m.x220
                           - 1.436939228176*m.b64 - 1.436939228176*m.b82 >= -1.436939228176)

m.c1484 = Constraint(expr=m.x215**2 + m.x216**2 + m.x221**2 + m.x222**2 - 2*m.x216*m.x222 - 2*m.x215*m.x221
                           - 1.436939228176*m.b64 - 1.436939228176*m.b91 >= -1.436939228176)

m.c1485 = Constraint(expr=m.x215**2 + m.x216**2 + m.x223**2 + m.x224**2 - 2*m.x216*m.x224 - 2*m.x215*m.x223
                           - 1.436939228176*m.b64 - 1.436939228176*m.b100 >= -1.436939228176)

m.c1486 = Constraint(expr=m.x215**2 + m.x216**2 + m.x225**2 + m.x226**2 - 2*m.x215*m.x225 - 2*m.x216*m.x226
                           - 1.436939228176*m.b64 - 1.436939228176*m.b109 >= -1.436939228176)

m.c1487 = Constraint(expr=m.x215**2 + m.x216**2 + m.x227**2 + m.x228**2 - 2*m.x216*m.x228 - 2*m.x215*m.x227
                           - 0.887203867225*m.b64 - 0.887203867225*m.b124 >= -0.887203867225)

m.c1488 = Constraint(expr=m.x215**2 + m.x216**2 + m.x229**2 + m.x230**2 - 2*m.x215*m.x229 - 2*m.x216*m.x230
                           - 0.887203867225*m.b64 - 0.887203867225*m.b139 >= -0.887203867225)

m.c1489 = Constraint(expr=m.x215**2 + m.x216**2 + m.x231**2 + m.x232**2 - 2*m.x216*m.x232 - 2*m.x215*m.x231
                           - 0.887203867225*m.b64 - 0.887203867225*m.b154 >= -0.887203867225)

m.c1490 = Constraint(expr=m.x215**2 + m.x216**2 + m.x233**2 + m.x234**2 - 2*m.x216*m.x234 - 2*m.x215*m.x233
                           - 0.887203867225*m.b64 - 0.887203867225*m.b169 >= -0.887203867225)

m.c1491 = Constraint(expr=m.x215**2 + m.x216**2 + m.x235**2 + m.x236**2 - 2*m.x216*m.x236 - 2*m.x215*m.x235
                           - 0.887203867225*m.b64 - 0.887203867225*m.b184 >= -0.887203867225)

m.c1492 = Constraint(expr=m.x215**2 + m.x216**2 + m.x217**2 + m.x218**2 - 2*m.x215*m.x217 - 2*m.x216*m.x218
                           - 1.436939228176*m.b64 - 1.436939228176*m.b73 >= -1.436939228176)

m.c1493 = Constraint(expr=m.x217**2 + m.x218**2 + m.x219**2 + m.x220**2 - 2*m.x217*m.x219 - 2*m.x218*m.x220
                           - 1.436939228176*m.b73 - 1.436939228176*m.b82 >= -1.436939228176)

m.c1494 = Constraint(expr=m.x217**2 + m.x218**2 + m.x221**2 + m.x222**2 - 2*m.x217*m.x221 - 2*m.x218*m.x222
                           - 1.436939228176*m.b73 - 1.436939228176*m.b91 >= -1.436939228176)

m.c1495 = Constraint(expr=m.x217**2 + m.x218**2 + m.x223**2 + m.x224**2 - 2*m.x217*m.x223 - 2*m.x218*m.x224
                           - 1.436939228176*m.b73 - 1.436939228176*m.b100 >= -1.436939228176)

m.c1496 = Constraint(expr=m.x217**2 + m.x218**2 + m.x225**2 + m.x226**2 - 2*m.x218*m.x226 - 2*m.x217*m.x225
                           - 1.436939228176*m.b73 - 1.436939228176*m.b109 >= -1.436939228176)

m.c1497 = Constraint(expr=m.x217**2 + m.x218**2 + m.x227**2 + m.x228**2 - 2*m.x217*m.x227 - 2*m.x218*m.x228
                           - 0.887203867225*m.b73 - 0.887203867225*m.b124 >= -0.887203867225)

m.c1498 = Constraint(expr=m.x217**2 + m.x218**2 + m.x229**2 + m.x230**2 - 2*m.x218*m.x230 - 2*m.x217*m.x229
                           - 0.887203867225*m.b73 - 0.887203867225*m.b139 >= -0.887203867225)

m.c1499 = Constraint(expr=m.x217**2 + m.x218**2 + m.x231**2 + m.x232**2 - 2*m.x217*m.x231 - 2*m.x218*m.x232
                           - 0.887203867225*m.b73 - 0.887203867225*m.b154 >= -0.887203867225)

m.c1500 = Constraint(expr=m.x217**2 + m.x218**2 + m.x233**2 + m.x234**2 - 2*m.x217*m.x233 - 2*m.x218*m.x234
                           - 0.887203867225*m.b73 - 0.887203867225*m.b169 >= -0.887203867225)

m.c1501 = Constraint(expr=m.x217**2 + m.x218**2 + m.x235**2 + m.x236**2 - 2*m.x217*m.x235 - 2*m.x218*m.x236
                           - 0.887203867225*m.b73 - 0.887203867225*m.b184 >= -0.887203867225)

m.c1502 = Constraint(expr=m.x215**2 + m.x216**2 + m.x219**2 + m.x220**2 - 2*m.x215*m.x219 - 2*m.x216*m.x220
                           - 1.436939228176*m.b64 - 1.436939228176*m.b82 >= -1.436939228176)

m.c1503 = Constraint(expr=m.x217**2 + m.x218**2 + m.x219**2 + m.x220**2 - 2*m.x217*m.x219 - 2*m.x218*m.x220
                           - 1.436939228176*m.b73 - 1.436939228176*m.b82 >= -1.436939228176)

m.c1504 = Constraint(expr=m.x219**2 + m.x220**2 + m.x221**2 + m.x222**2 - 2*m.x219*m.x221 - 2*m.x220*m.x222
                           - 1.436939228176*m.b82 - 1.436939228176*m.b91 >= -1.436939228176)

m.c1505 = Constraint(expr=m.x219**2 + m.x220**2 + m.x223**2 + m.x224**2 - 2*m.x220*m.x224 - 2*m.x219*m.x223
                           - 1.436939228176*m.b82 - 1.436939228176*m.b100 >= -1.436939228176)

m.c1506 = Constraint(expr=m.x219**2 + m.x220**2 + m.x225**2 + m.x226**2 - 2*m.x220*m.x226 - 2*m.x219*m.x225
                           - 1.436939228176*m.b82 - 1.436939228176*m.b109 >= -1.436939228176)

m.c1507 = Constraint(expr=m.x219**2 + m.x220**2 + m.x227**2 + m.x228**2 - 2*m.x220*m.x228 - 2*m.x219*m.x227
                           - 0.887203867225*m.b82 - 0.887203867225*m.b124 >= -0.887203867225)

m.c1508 = Constraint(expr=m.x219**2 + m.x220**2 + m.x229**2 + m.x230**2 - 2*m.x220*m.x230 - 2*m.x219*m.x229
                           - 0.887203867225*m.b82 - 0.887203867225*m.b139 >= -0.887203867225)

m.c1509 = Constraint(expr=m.x219**2 + m.x220**2 + m.x231**2 + m.x232**2 - 2*m.x219*m.x231 - 2*m.x220*m.x232
                           - 0.887203867225*m.b82 - 0.887203867225*m.b154 >= -0.887203867225)

m.c1510 = Constraint(expr=m.x219**2 + m.x220**2 + m.x233**2 + m.x234**2 - 2*m.x220*m.x234 - 2*m.x219*m.x233
                           - 0.887203867225*m.b82 - 0.887203867225*m.b169 >= -0.887203867225)

m.c1511 = Constraint(expr=m.x219**2 + m.x220**2 + m.x235**2 + m.x236**2 - 2*m.x219*m.x235 - 2*m.x220*m.x236
                           - 0.887203867225*m.b82 - 0.887203867225*m.b184 >= -0.887203867225)

m.c1512 = Constraint(expr=m.x215**2 + m.x216**2 + m.x221**2 + m.x222**2 - 2*m.x216*m.x222 - 2*m.x215*m.x221
                           - 1.436939228176*m.b64 - 1.436939228176*m.b91 >= -1.436939228176)

m.c1513 = Constraint(expr=m.x217**2 + m.x218**2 + m.x221**2 + m.x222**2 - 2*m.x217*m.x221 - 2*m.x218*m.x222
                           - 1.436939228176*m.b73 - 1.436939228176*m.b91 >= -1.436939228176)

m.c1514 = Constraint(expr=m.x219**2 + m.x220**2 + m.x221**2 + m.x222**2 - 2*m.x219*m.x221 - 2*m.x220*m.x222
                           - 1.436939228176*m.b82 - 1.436939228176*m.b91 >= -1.436939228176)

m.c1515 = Constraint(expr=m.x221**2 + m.x222**2 + m.x223**2 + m.x224**2 - 2*m.x221*m.x223 - 2*m.x222*m.x224
                           - 1.436939228176*m.b91 - 1.436939228176*m.b100 >= -1.436939228176)

m.c1516 = Constraint(expr=m.x221**2 + m.x222**2 + m.x225**2 + m.x226**2 - 2*m.x221*m.x225 - 2*m.x222*m.x226
                           - 1.436939228176*m.b91 - 1.436939228176*m.b109 >= -1.436939228176)

m.c1517 = Constraint(expr=m.x221**2 + m.x222**2 + m.x227**2 + m.x228**2 - 2*m.x221*m.x227 - 2*m.x222*m.x228
                           - 0.887203867225*m.b91 - 0.887203867225*m.b124 >= -0.887203867225)

m.c1518 = Constraint(expr=m.x221**2 + m.x222**2 + m.x229**2 + m.x230**2 - 2*m.x221*m.x229 - 2*m.x222*m.x230
                           - 0.887203867225*m.b91 - 0.887203867225*m.b139 >= -0.887203867225)

m.c1519 = Constraint(expr=m.x221**2 + m.x222**2 + m.x231**2 + m.x232**2 - 2*m.x221*m.x231 - 2*m.x222*m.x232
                           - 0.887203867225*m.b91 - 0.887203867225*m.b154 >= -0.887203867225)

m.c1520 = Constraint(expr=m.x221**2 + m.x222**2 + m.x233**2 + m.x234**2 - 2*m.x221*m.x233 - 2*m.x222*m.x234
                           - 0.887203867225*m.b91 - 0.887203867225*m.b169 >= -0.887203867225)

m.c1521 = Constraint(expr=m.x221**2 + m.x222**2 + m.x235**2 + m.x236**2 - 2*m.x221*m.x235 - 2*m.x222*m.x236
                           - 0.887203867225*m.b91 - 0.887203867225*m.b184 >= -0.887203867225)

m.c1522 = Constraint(expr=m.x215**2 + m.x216**2 + m.x223**2 + m.x224**2 - 2*m.x216*m.x224 - 2*m.x215*m.x223
                           - 1.436939228176*m.b64 - 1.436939228176*m.b100 >= -1.436939228176)

m.c1523 = Constraint(expr=m.x217**2 + m.x218**2 + m.x223**2 + m.x224**2 - 2*m.x217*m.x223 - 2*m.x218*m.x224
                           - 1.436939228176*m.b73 - 1.436939228176*m.b100 >= -1.436939228176)

m.c1524 = Constraint(expr=m.x219**2 + m.x220**2 + m.x223**2 + m.x224**2 - 2*m.x220*m.x224 - 2*m.x219*m.x223
                           - 1.436939228176*m.b82 - 1.436939228176*m.b100 >= -1.436939228176)

m.c1525 = Constraint(expr=m.x221**2 + m.x222**2 + m.x223**2 + m.x224**2 - 2*m.x221*m.x223 - 2*m.x222*m.x224
                           - 1.436939228176*m.b91 - 1.436939228176*m.b100 >= -1.436939228176)

m.c1526 = Constraint(expr=m.x223**2 + m.x224**2 + m.x225**2 + m.x226**2 - 2*m.x223*m.x225 - 2*m.x224*m.x226
                           - 1.436939228176*m.b100 - 1.436939228176*m.b109 >= -1.436939228176)

m.c1527 = Constraint(expr=m.x223**2 + m.x224**2 + m.x227**2 + m.x228**2 - 2*m.x223*m.x227 - 2*m.x224*m.x228
                           - 0.887203867225*m.b100 - 0.887203867225*m.b124 >= -0.887203867225)

m.c1528 = Constraint(expr=m.x223**2 + m.x224**2 + m.x229**2 + m.x230**2 - 2*m.x223*m.x229 - 2*m.x224*m.x230
                           - 0.887203867225*m.b100 - 0.887203867225*m.b139 >= -0.887203867225)

m.c1529 = Constraint(expr=m.x223**2 + m.x224**2 + m.x231**2 + m.x232**2 - 2*m.x223*m.x231 - 2*m.x224*m.x232
                           - 0.887203867225*m.b100 - 0.887203867225*m.b154 >= -0.887203867225)

m.c1530 = Constraint(expr=m.x223**2 + m.x224**2 + m.x233**2 + m.x234**2 - 2*m.x223*m.x233 - 2*m.x224*m.x234
                           - 0.887203867225*m.b100 - 0.887203867225*m.b169 >= -0.887203867225)

m.c1531 = Constraint(expr=m.x223**2 + m.x224**2 + m.x235**2 + m.x236**2 - 2*m.x223*m.x235 - 2*m.x224*m.x236
                           - 0.887203867225*m.b100 - 0.887203867225*m.b184 >= -0.887203867225)

m.c1532 = Constraint(expr=m.x215**2 + m.x216**2 + m.x225**2 + m.x226**2 - 2*m.x215*m.x225 - 2*m.x216*m.x226
                           - 1.436939228176*m.b64 - 1.436939228176*m.b109 >= -1.436939228176)

m.c1533 = Constraint(expr=m.x217**2 + m.x218**2 + m.x225**2 + m.x226**2 - 2*m.x218*m.x226 - 2*m.x217*m.x225
                           - 1.436939228176*m.b73 - 1.436939228176*m.b109 >= -1.436939228176)

m.c1534 = Constraint(expr=m.x219**2 + m.x220**2 + m.x225**2 + m.x226**2 - 2*m.x220*m.x226 - 2*m.x219*m.x225
                           - 1.436939228176*m.b82 - 1.436939228176*m.b109 >= -1.436939228176)

m.c1535 = Constraint(expr=m.x221**2 + m.x222**2 + m.x225**2 + m.x226**2 - 2*m.x221*m.x225 - 2*m.x222*m.x226
                           - 1.436939228176*m.b91 - 1.436939228176*m.b109 >= -1.436939228176)

m.c1536 = Constraint(expr=m.x223**2 + m.x224**2 + m.x225**2 + m.x226**2 - 2*m.x223*m.x225 - 2*m.x224*m.x226
                           - 1.436939228176*m.b100 - 1.436939228176*m.b109 >= -1.436939228176)

m.c1537 = Constraint(expr=m.x225**2 + m.x226**2 + m.x227**2 + m.x228**2 - 2*m.x225*m.x227 - 2*m.x226*m.x228
                           - 0.887203867225*m.b109 - 0.887203867225*m.b124 >= -0.887203867225)

m.c1538 = Constraint(expr=m.x225**2 + m.x226**2 + m.x229**2 + m.x230**2 - 2*m.x225*m.x229 - 2*m.x226*m.x230
                           - 0.887203867225*m.b109 - 0.887203867225*m.b139 >= -0.887203867225)

m.c1539 = Constraint(expr=m.x225**2 + m.x226**2 + m.x231**2 + m.x232**2 - 2*m.x225*m.x231 - 2*m.x226*m.x232
                           - 0.887203867225*m.b109 - 0.887203867225*m.b154 >= -0.887203867225)

m.c1540 = Constraint(expr=m.x225**2 + m.x226**2 + m.x233**2 + m.x234**2 - 2*m.x225*m.x233 - 2*m.x226*m.x234
                           - 0.887203867225*m.b109 - 0.887203867225*m.b169 >= -0.887203867225)

m.c1541 = Constraint(expr=m.x225**2 + m.x226**2 + m.x235**2 + m.x236**2 - 2*m.x225*m.x235 - 2*m.x226*m.x236
                           - 0.887203867225*m.b109 - 0.887203867225*m.b184 >= -0.887203867225)

m.c1542 = Constraint(expr=m.x215**2 + m.x216**2 + m.x227**2 + m.x228**2 - 2*m.x216*m.x228 - 2*m.x215*m.x227
                           - 0.887203867225*m.b64 - 0.887203867225*m.b124 >= -0.887203867225)

m.c1543 = Constraint(expr=m.x217**2 + m.x218**2 + m.x227**2 + m.x228**2 - 2*m.x217*m.x227 - 2*m.x218*m.x228
                           - 0.887203867225*m.b73 - 0.887203867225*m.b124 >= -0.887203867225)

m.c1544 = Constraint(expr=m.x219**2 + m.x220**2 + m.x227**2 + m.x228**2 - 2*m.x220*m.x228 - 2*m.x219*m.x227
                           - 0.887203867225*m.b82 - 0.887203867225*m.b124 >= -0.887203867225)

m.c1545 = Constraint(expr=m.x221**2 + m.x222**2 + m.x227**2 + m.x228**2 - 2*m.x221*m.x227 - 2*m.x222*m.x228
                           - 0.887203867225*m.b91 - 0.887203867225*m.b124 >= -0.887203867225)

m.c1546 = Constraint(expr=m.x223**2 + m.x224**2 + m.x227**2 + m.x228**2 - 2*m.x223*m.x227 - 2*m.x224*m.x228
                           - 0.887203867225*m.b100 - 0.887203867225*m.b124 >= -0.887203867225)

m.c1547 = Constraint(expr=m.x225**2 + m.x226**2 + m.x227**2 + m.x228**2 - 2*m.x225*m.x227 - 2*m.x226*m.x228
                           - 0.887203867225*m.b109 - 0.887203867225*m.b124 >= -0.887203867225)

m.c1548 = Constraint(expr=m.x227**2 + m.x228**2 + m.x229**2 + m.x230**2 - 2*m.x227*m.x229 - 2*m.x228*m.x230
                           - 0.469370231236*m.b124 - 0.469370231236*m.b139 >= -0.469370231236)

m.c1549 = Constraint(expr=m.x227**2 + m.x228**2 + m.x231**2 + m.x232**2 - 2*m.x227*m.x231 - 2*m.x228*m.x232
                           - 0.469370231236*m.b124 - 0.469370231236*m.b154 >= -0.469370231236)

m.c1550 = Constraint(expr=m.x227**2 + m.x228**2 + m.x233**2 + m.x234**2 - 2*m.x227*m.x233 - 2*m.x228*m.x234
                           - 0.469370231236*m.b124 - 0.469370231236*m.b169 >= -0.469370231236)

m.c1551 = Constraint(expr=m.x227**2 + m.x228**2 + m.x235**2 + m.x236**2 - 2*m.x227*m.x235 - 2*m.x228*m.x236
                           - 0.469370231236*m.b124 - 0.469370231236*m.b184 >= -0.469370231236)

m.c1552 = Constraint(expr=m.x215**2 + m.x216**2 + m.x229**2 + m.x230**2 - 2*m.x215*m.x229 - 2*m.x216*m.x230
                           - 0.887203867225*m.b64 - 0.887203867225*m.b139 >= -0.887203867225)

m.c1553 = Constraint(expr=m.x217**2 + m.x218**2 + m.x229**2 + m.x230**2 - 2*m.x218*m.x230 - 2*m.x217*m.x229
                           - 0.887203867225*m.b73 - 0.887203867225*m.b139 >= -0.887203867225)

m.c1554 = Constraint(expr=m.x219**2 + m.x220**2 + m.x229**2 + m.x230**2 - 2*m.x220*m.x230 - 2*m.x219*m.x229
                           - 0.887203867225*m.b82 - 0.887203867225*m.b139 >= -0.887203867225)

m.c1555 = Constraint(expr=m.x221**2 + m.x222**2 + m.x229**2 + m.x230**2 - 2*m.x221*m.x229 - 2*m.x222*m.x230
                           - 0.887203867225*m.b91 - 0.887203867225*m.b139 >= -0.887203867225)

m.c1556 = Constraint(expr=m.x223**2 + m.x224**2 + m.x229**2 + m.x230**2 - 2*m.x223*m.x229 - 2*m.x224*m.x230
                           - 0.887203867225*m.b100 - 0.887203867225*m.b139 >= -0.887203867225)

m.c1557 = Constraint(expr=m.x225**2 + m.x226**2 + m.x229**2 + m.x230**2 - 2*m.x225*m.x229 - 2*m.x226*m.x230
                           - 0.887203867225*m.b109 - 0.887203867225*m.b139 >= -0.887203867225)

m.c1558 = Constraint(expr=m.x227**2 + m.x228**2 + m.x229**2 + m.x230**2 - 2*m.x227*m.x229 - 2*m.x228*m.x230
                           - 0.469370231236*m.b124 - 0.469370231236*m.b139 >= -0.469370231236)

m.c1559 = Constraint(expr=m.x229**2 + m.x230**2 + m.x231**2 + m.x232**2 - 2*m.x229*m.x231 - 2*m.x230*m.x232
                           - 0.469370231236*m.b139 - 0.469370231236*m.b154 >= -0.469370231236)

m.c1560 = Constraint(expr=m.x229**2 + m.x230**2 + m.x233**2 + m.x234**2 - 2*m.x229*m.x233 - 2*m.x230*m.x234
                           - 0.469370231236*m.b139 - 0.469370231236*m.b169 >= -0.469370231236)

m.c1561 = Constraint(expr=m.x229**2 + m.x230**2 + m.x235**2 + m.x236**2 - 2*m.x229*m.x235 - 2*m.x230*m.x236
                           - 0.469370231236*m.b139 - 0.469370231236*m.b184 >= -0.469370231236)

m.c1562 = Constraint(expr=m.x215**2 + m.x216**2 + m.x231**2 + m.x232**2 - 2*m.x216*m.x232 - 2*m.x215*m.x231
                           - 0.887203867225*m.b64 - 0.887203867225*m.b154 >= -0.887203867225)

m.c1563 = Constraint(expr=m.x217**2 + m.x218**2 + m.x231**2 + m.x232**2 - 2*m.x217*m.x231 - 2*m.x218*m.x232
                           - 0.887203867225*m.b73 - 0.887203867225*m.b154 >= -0.887203867225)

m.c1564 = Constraint(expr=m.x219**2 + m.x220**2 + m.x231**2 + m.x232**2 - 2*m.x219*m.x231 - 2*m.x220*m.x232
                           - 0.887203867225*m.b82 - 0.887203867225*m.b154 >= -0.887203867225)

m.c1565 = Constraint(expr=m.x221**2 + m.x222**2 + m.x231**2 + m.x232**2 - 2*m.x221*m.x231 - 2*m.x222*m.x232
                           - 0.887203867225*m.b91 - 0.887203867225*m.b154 >= -0.887203867225)

m.c1566 = Constraint(expr=m.x223**2 + m.x224**2 + m.x231**2 + m.x232**2 - 2*m.x223*m.x231 - 2*m.x224*m.x232
                           - 0.887203867225*m.b100 - 0.887203867225*m.b154 >= -0.887203867225)

m.c1567 = Constraint(expr=m.x225**2 + m.x226**2 + m.x231**2 + m.x232**2 - 2*m.x225*m.x231 - 2*m.x226*m.x232
                           - 0.887203867225*m.b109 - 0.887203867225*m.b154 >= -0.887203867225)

m.c1568 = Constraint(expr=m.x227**2 + m.x228**2 + m.x231**2 + m.x232**2 - 2*m.x227*m.x231 - 2*m.x228*m.x232
                           - 0.469370231236*m.b124 - 0.469370231236*m.b154 >= -0.469370231236)

m.c1569 = Constraint(expr=m.x229**2 + m.x230**2 + m.x231**2 + m.x232**2 - 2*m.x229*m.x231 - 2*m.x230*m.x232
                           - 0.469370231236*m.b139 - 0.469370231236*m.b154 >= -0.469370231236)

m.c1570 = Constraint(expr=m.x231**2 + m.x232**2 + m.x233**2 + m.x234**2 - 2*m.x231*m.x233 - 2*m.x232*m.x234
                           - 0.469370231236*m.b154 - 0.469370231236*m.b169 >= -0.469370231236)

m.c1571 = Constraint(expr=m.x231**2 + m.x232**2 + m.x235**2 + m.x236**2 - 2*m.x231*m.x235 - 2*m.x232*m.x236
                           - 0.469370231236*m.b154 - 0.469370231236*m.b184 >= -0.469370231236)

m.c1572 = Constraint(expr=m.x215**2 + m.x216**2 + m.x233**2 + m.x234**2 - 2*m.x216*m.x234 - 2*m.x215*m.x233
                           - 0.887203867225*m.b64 - 0.887203867225*m.b169 >= -0.887203867225)

m.c1573 = Constraint(expr=m.x217**2 + m.x218**2 + m.x233**2 + m.x234**2 - 2*m.x217*m.x233 - 2*m.x218*m.x234
                           - 0.887203867225*m.b73 - 0.887203867225*m.b169 >= -0.887203867225)

m.c1574 = Constraint(expr=m.x219**2 + m.x220**2 + m.x233**2 + m.x234**2 - 2*m.x219*m.x233 - 2*m.x220*m.x234
                           - 0.887203867225*m.b82 - 0.887203867225*m.b169 >= -0.887203867225)

m.c1575 = Constraint(expr=m.x221**2 + m.x222**2 + m.x233**2 + m.x234**2 - 2*m.x221*m.x233 - 2*m.x222*m.x234
                           - 0.887203867225*m.b91 - 0.887203867225*m.b169 >= -0.887203867225)

m.c1576 = Constraint(expr=m.x223**2 + m.x224**2 + m.x233**2 + m.x234**2 - 2*m.x223*m.x233 - 2*m.x224*m.x234
                           - 0.887203867225*m.b100 - 0.887203867225*m.b169 >= -0.887203867225)

m.c1577 = Constraint(expr=m.x225**2 + m.x226**2 + m.x233**2 + m.x234**2 - 2*m.x225*m.x233 - 2*m.x226*m.x234
                           - 0.887203867225*m.b109 - 0.887203867225*m.b169 >= -0.887203867225)

m.c1578 = Constraint(expr=m.x227**2 + m.x228**2 + m.x233**2 + m.x234**2 - 2*m.x227*m.x233 - 2*m.x228*m.x234
                           - 0.469370231236*m.b124 - 0.469370231236*m.b169 >= -0.469370231236)

m.c1579 = Constraint(expr=m.x229**2 + m.x230**2 + m.x233**2 + m.x234**2 - 2*m.x229*m.x233 - 2*m.x230*m.x234
                           - 0.469370231236*m.b139 - 0.469370231236*m.b169 >= -0.469370231236)

m.c1580 = Constraint(expr=m.x231**2 + m.x232**2 + m.x233**2 + m.x234**2 - 2*m.x231*m.x233 - 2*m.x232*m.x234
                           - 0.469370231236*m.b154 - 0.469370231236*m.b169 >= -0.469370231236)

m.c1581 = Constraint(expr=m.x233**2 + m.x234**2 + m.x235**2 + m.x236**2 - 2*m.x233*m.x235 - 2*m.x234*m.x236
                           - 0.469370231236*m.b169 - 0.469370231236*m.b184 >= -0.469370231236)

m.c1582 = Constraint(expr=m.x215**2 + m.x216**2 + m.x235**2 + m.x236**2 - 2*m.x216*m.x236 - 2*m.x215*m.x235
                           - 0.887203867225*m.b64 - 0.887203867225*m.b184 >= -0.887203867225)

m.c1583 = Constraint(expr=m.x217**2 + m.x218**2 + m.x235**2 + m.x236**2 - 2*m.x217*m.x235 - 2*m.x218*m.x236
                           - 0.887203867225*m.b73 - 0.887203867225*m.b184 >= -0.887203867225)

m.c1584 = Constraint(expr=m.x219**2 + m.x220**2 + m.x235**2 + m.x236**2 - 2*m.x219*m.x235 - 2*m.x220*m.x236
                           - 0.887203867225*m.b82 - 0.887203867225*m.b184 >= -0.887203867225)

m.c1585 = Constraint(expr=m.x221**2 + m.x222**2 + m.x235**2 + m.x236**2 - 2*m.x221*m.x235 - 2*m.x222*m.x236
                           - 0.887203867225*m.b91 - 0.887203867225*m.b184 >= -0.887203867225)

m.c1586 = Constraint(expr=m.x223**2 + m.x224**2 + m.x235**2 + m.x236**2 - 2*m.x223*m.x235 - 2*m.x224*m.x236
                           - 0.887203867225*m.b100 - 0.887203867225*m.b184 >= -0.887203867225)

m.c1587 = Constraint(expr=m.x225**2 + m.x226**2 + m.x235**2 + m.x236**2 - 2*m.x225*m.x235 - 2*m.x226*m.x236
                           - 0.887203867225*m.b109 - 0.887203867225*m.b184 >= -0.887203867225)

m.c1588 = Constraint(expr=m.x227**2 + m.x228**2 + m.x235**2 + m.x236**2 - 2*m.x227*m.x235 - 2*m.x228*m.x236
                           - 0.469370231236*m.b124 - 0.469370231236*m.b184 >= -0.469370231236)

m.c1589 = Constraint(expr=m.x229**2 + m.x230**2 + m.x235**2 + m.x236**2 - 2*m.x229*m.x235 - 2*m.x230*m.x236
                           - 0.469370231236*m.b139 - 0.469370231236*m.b184 >= -0.469370231236)

m.c1590 = Constraint(expr=m.x231**2 + m.x232**2 + m.x235**2 + m.x236**2 - 2*m.x231*m.x235 - 2*m.x232*m.x236
                           - 0.469370231236*m.b154 - 0.469370231236*m.b184 >= -0.469370231236)

m.c1591 = Constraint(expr=m.x233**2 + m.x234**2 + m.x235**2 + m.x236**2 - 2*m.x233*m.x235 - 2*m.x234*m.x236
                           - 0.469370231236*m.b169 - 0.469370231236*m.b184 >= -0.469370231236)

m.c1592 = Constraint(expr=m.x215**2 + m.x216**2 + m.x217**2 + m.x218**2 - 2*m.x215*m.x217 - 2*m.x216*m.x218
                           - 1.436939228176*m.b65 - 1.436939228176*m.b74 >= -1.436939228176)

m.c1593 = Constraint(expr=m.x215**2 + m.x216**2 + m.x219**2 + m.x220**2 - 2*m.x215*m.x219 - 2*m.x216*m.x220
                           - 1.436939228176*m.b65 - 1.436939228176*m.b83 >= -1.436939228176)

m.c1594 = Constraint(expr=m.x215**2 + m.x216**2 + m.x221**2 + m.x222**2 - 2*m.x216*m.x222 - 2*m.x215*m.x221
                           - 1.436939228176*m.b65 - 1.436939228176*m.b92 >= -1.436939228176)

m.c1595 = Constraint(expr=m.x215**2 + m.x216**2 + m.x223**2 + m.x224**2 - 2*m.x216*m.x224 - 2*m.x215*m.x223
                           - 1.436939228176*m.b65 - 1.436939228176*m.b101 >= -1.436939228176)

m.c1596 = Constraint(expr=m.x215**2 + m.x216**2 + m.x225**2 + m.x226**2 - 2*m.x215*m.x225 - 2*m.x216*m.x226
                           - 1.436939228176*m.b65 - 1.436939228176*m.b110 >= -1.436939228176)

m.c1597 = Constraint(expr=m.x215**2 + m.x216**2 + m.x227**2 + m.x228**2 - 2*m.x216*m.x228 - 2*m.x215*m.x227
                           - 0.887203867225*m.b65 - 0.887203867225*m.b125 >= -0.887203867225)

m.c1598 = Constraint(expr=m.x215**2 + m.x216**2 + m.x229**2 + m.x230**2 - 2*m.x215*m.x229 - 2*m.x216*m.x230
                           - 0.887203867225*m.b65 - 0.887203867225*m.b140 >= -0.887203867225)

m.c1599 = Constraint(expr=m.x215**2 + m.x216**2 + m.x231**2 + m.x232**2 - 2*m.x216*m.x232 - 2*m.x215*m.x231
                           - 0.887203867225*m.b65 - 0.887203867225*m.b155 >= -0.887203867225)

m.c1600 = Constraint(expr=m.x215**2 + m.x216**2 + m.x233**2 + m.x234**2 - 2*m.x216*m.x234 - 2*m.x215*m.x233
                           - 0.887203867225*m.b65 - 0.887203867225*m.b170 >= -0.887203867225)

m.c1601 = Constraint(expr=m.x215**2 + m.x216**2 + m.x235**2 + m.x236**2 - 2*m.x215*m.x235 - 2*m.x216*m.x236
                           - 0.887203867225*m.b65 - 0.887203867225*m.b185 >= -0.887203867225)

m.c1602 = Constraint(expr=m.x215**2 + m.x216**2 + m.x217**2 + m.x218**2 - 2*m.x215*m.x217 - 2*m.x216*m.x218
                           - 1.436939228176*m.b65 - 1.436939228176*m.b74 >= -1.436939228176)

m.c1603 = Constraint(expr=m.x217**2 + m.x218**2 + m.x219**2 + m.x220**2 - 2*m.x217*m.x219 - 2*m.x218*m.x220
                           - 1.436939228176*m.b74 - 1.436939228176*m.b83 >= -1.436939228176)

m.c1604 = Constraint(expr=m.x217**2 + m.x218**2 + m.x221**2 + m.x222**2 - 2*m.x218*m.x222 - 2*m.x217*m.x221
                           - 1.436939228176*m.b74 - 1.436939228176*m.b92 >= -1.436939228176)

m.c1605 = Constraint(expr=m.x217**2 + m.x218**2 + m.x223**2 + m.x224**2 - 2*m.x217*m.x223 - 2*m.x218*m.x224
                           - 1.436939228176*m.b74 - 1.436939228176*m.b101 >= -1.436939228176)

m.c1606 = Constraint(expr=m.x217**2 + m.x218**2 + m.x225**2 + m.x226**2 - 2*m.x218*m.x226 - 2*m.x217*m.x225
                           - 1.436939228176*m.b74 - 1.436939228176*m.b110 >= -1.436939228176)

m.c1607 = Constraint(expr=m.x217**2 + m.x218**2 + m.x227**2 + m.x228**2 - 2*m.x217*m.x227 - 2*m.x218*m.x228
                           - 0.887203867225*m.b74 - 0.887203867225*m.b125 >= -0.887203867225)

m.c1608 = Constraint(expr=m.x217**2 + m.x218**2 + m.x229**2 + m.x230**2 - 2*m.x218*m.x230 - 2*m.x217*m.x229
                           - 0.887203867225*m.b74 - 0.887203867225*m.b140 >= -0.887203867225)

m.c1609 = Constraint(expr=m.x217**2 + m.x218**2 + m.x231**2 + m.x232**2 - 2*m.x218*m.x232 - 2*m.x217*m.x231
                           - 0.887203867225*m.b74 - 0.887203867225*m.b155 >= -0.887203867225)

m.c1610 = Constraint(expr=m.x217**2 + m.x218**2 + m.x233**2 + m.x234**2 - 2*m.x217*m.x233 - 2*m.x218*m.x234
                           - 0.887203867225*m.b74 - 0.887203867225*m.b170 >= -0.887203867225)

m.c1611 = Constraint(expr=m.x217**2 + m.x218**2 + m.x235**2 + m.x236**2 - 2*m.x217*m.x235 - 2*m.x218*m.x236
                           - 0.887203867225*m.b74 - 0.887203867225*m.b185 >= -0.887203867225)

m.c1612 = Constraint(expr=m.x215**2 + m.x216**2 + m.x219**2 + m.x220**2 - 2*m.x215*m.x219 - 2*m.x216*m.x220
                           - 1.436939228176*m.b65 - 1.436939228176*m.b83 >= -1.436939228176)

m.c1613 = Constraint(expr=m.x217**2 + m.x218**2 + m.x219**2 + m.x220**2 - 2*m.x217*m.x219 - 2*m.x218*m.x220
                           - 1.436939228176*m.b74 - 1.436939228176*m.b83 >= -1.436939228176)

m.c1614 = Constraint(expr=m.x219**2 + m.x220**2 + m.x221**2 + m.x222**2 - 2*m.x219*m.x221 - 2*m.x220*m.x222
                           - 1.436939228176*m.b83 - 1.436939228176*m.b92 >= -1.436939228176)

m.c1615 = Constraint(expr=m.x219**2 + m.x220**2 + m.x223**2 + m.x224**2 - 2*m.x220*m.x224 - 2*m.x219*m.x223
                           - 1.436939228176*m.b83 - 1.436939228176*m.b101 >= -1.436939228176)

m.c1616 = Constraint(expr=m.x219**2 + m.x220**2 + m.x225**2 + m.x226**2 - 2*m.x220*m.x226 - 2*m.x219*m.x225
                           - 1.436939228176*m.b83 - 1.436939228176*m.b110 >= -1.436939228176)

m.c1617 = Constraint(expr=m.x219**2 + m.x220**2 + m.x227**2 + m.x228**2 - 2*m.x220*m.x228 - 2*m.x219*m.x227
                           - 0.887203867225*m.b83 - 0.887203867225*m.b125 >= -0.887203867225)

m.c1618 = Constraint(expr=m.x219**2 + m.x220**2 + m.x229**2 + m.x230**2 - 2*m.x220*m.x230 - 2*m.x219*m.x229
                           - 0.887203867225*m.b83 - 0.887203867225*m.b140 >= -0.887203867225)

m.c1619 = Constraint(expr=m.x219**2 + m.x220**2 + m.x231**2 + m.x232**2 - 2*m.x219*m.x231 - 2*m.x220*m.x232
                           - 0.887203867225*m.b83 - 0.887203867225*m.b155 >= -0.887203867225)

m.c1620 = Constraint(expr=m.x219**2 + m.x220**2 + m.x233**2 + m.x234**2 - 2*m.x219*m.x233 - 2*m.x220*m.x234
                           - 0.887203867225*m.b83 - 0.887203867225*m.b170 >= -0.887203867225)

m.c1621 = Constraint(expr=m.x219**2 + m.x220**2 + m.x235**2 + m.x236**2 - 2*m.x219*m.x235 - 2*m.x220*m.x236
                           - 0.887203867225*m.b83 - 0.887203867225*m.b185 >= -0.887203867225)

m.c1622 = Constraint(expr=m.x215**2 + m.x216**2 + m.x221**2 + m.x222**2 - 2*m.x216*m.x222 - 2*m.x215*m.x221
                           - 1.436939228176*m.b65 - 1.436939228176*m.b92 >= -1.436939228176)

m.c1623 = Constraint(expr=m.x217**2 + m.x218**2 + m.x221**2 + m.x222**2 - 2*m.x217*m.x221 - 2*m.x218*m.x222
                           - 1.436939228176*m.b74 - 1.436939228176*m.b92 >= -1.436939228176)

m.c1624 = Constraint(expr=m.x219**2 + m.x220**2 + m.x221**2 + m.x222**2 - 2*m.x219*m.x221 - 2*m.x220*m.x222
                           - 1.436939228176*m.b83 - 1.436939228176*m.b92 >= -1.436939228176)

m.c1625 = Constraint(expr=m.x221**2 + m.x222**2 + m.x223**2 + m.x224**2 - 2*m.x221*m.x223 - 2*m.x222*m.x224
                           - 1.436939228176*m.b92 - 1.436939228176*m.b101 >= -1.436939228176)

m.c1626 = Constraint(expr=m.x221**2 + m.x222**2 + m.x225**2 + m.x226**2 - 2*m.x221*m.x225 - 2*m.x222*m.x226
                           - 1.436939228176*m.b92 - 1.436939228176*m.b110 >= -1.436939228176)

m.c1627 = Constraint(expr=m.x221**2 + m.x222**2 + m.x227**2 + m.x228**2 - 2*m.x221*m.x227 - 2*m.x222*m.x228
                           - 0.887203867225*m.b92 - 0.887203867225*m.b125 >= -0.887203867225)

m.c1628 = Constraint(expr=m.x221**2 + m.x222**2 + m.x229**2 + m.x230**2 - 2*m.x221*m.x229 - 2*m.x222*m.x230
                           - 0.887203867225*m.b92 - 0.887203867225*m.b140 >= -0.887203867225)

m.c1629 = Constraint(expr=m.x221**2 + m.x222**2 + m.x231**2 + m.x232**2 - 2*m.x221*m.x231 - 2*m.x222*m.x232
                           - 0.887203867225*m.b92 - 0.887203867225*m.b155 >= -0.887203867225)

m.c1630 = Constraint(expr=m.x221**2 + m.x222**2 + m.x233**2 + m.x234**2 - 2*m.x221*m.x233 - 2*m.x222*m.x234
                           - 0.887203867225*m.b92 - 0.887203867225*m.b170 >= -0.887203867225)

m.c1631 = Constraint(expr=m.x221**2 + m.x222**2 + m.x235**2 + m.x236**2 - 2*m.x221*m.x235 - 2*m.x222*m.x236
                           - 0.887203867225*m.b92 - 0.887203867225*m.b185 >= -0.887203867225)

m.c1632 = Constraint(expr=m.x215**2 + m.x216**2 + m.x223**2 + m.x224**2 - 2*m.x216*m.x224 - 2*m.x215*m.x223
                           - 1.436939228176*m.b65 - 1.436939228176*m.b101 >= -1.436939228176)

m.c1633 = Constraint(expr=m.x217**2 + m.x218**2 + m.x223**2 + m.x224**2 - 2*m.x217*m.x223 - 2*m.x218*m.x224
                           - 1.436939228176*m.b74 - 1.436939228176*m.b101 >= -1.436939228176)

m.c1634 = Constraint(expr=m.x219**2 + m.x220**2 + m.x223**2 + m.x224**2 - 2*m.x220*m.x224 - 2*m.x219*m.x223
                           - 1.436939228176*m.b83 - 1.436939228176*m.b101 >= -1.436939228176)

m.c1635 = Constraint(expr=m.x221**2 + m.x222**2 + m.x223**2 + m.x224**2 - 2*m.x221*m.x223 - 2*m.x222*m.x224
                           - 1.436939228176*m.b92 - 1.436939228176*m.b101 >= -1.436939228176)

m.c1636 = Constraint(expr=m.x223**2 + m.x224**2 + m.x225**2 + m.x226**2 - 2*m.x223*m.x225 - 2*m.x224*m.x226
                           - 1.436939228176*m.b101 - 1.436939228176*m.b110 >= -1.436939228176)

m.c1637 = Constraint(expr=m.x223**2 + m.x224**2 + m.x227**2 + m.x228**2 - 2*m.x223*m.x227 - 2*m.x224*m.x228
                           - 0.887203867225*m.b101 - 0.887203867225*m.b125 >= -0.887203867225)

m.c1638 = Constraint(expr=m.x223**2 + m.x224**2 + m.x229**2 + m.x230**2 - 2*m.x223*m.x229 - 2*m.x224*m.x230
                           - 0.887203867225*m.b101 - 0.887203867225*m.b140 >= -0.887203867225)

m.c1639 = Constraint(expr=m.x223**2 + m.x224**2 + m.x231**2 + m.x232**2 - 2*m.x223*m.x231 - 2*m.x224*m.x232
                           - 0.887203867225*m.b101 - 0.887203867225*m.b155 >= -0.887203867225)

m.c1640 = Constraint(expr=m.x223**2 + m.x224**2 + m.x233**2 + m.x234**2 - 2*m.x223*m.x233 - 2*m.x224*m.x234
                           - 0.887203867225*m.b101 - 0.887203867225*m.b170 >= -0.887203867225)

m.c1641 = Constraint(expr=m.x223**2 + m.x224**2 + m.x235**2 + m.x236**2 - 2*m.x223*m.x235 - 2*m.x224*m.x236
                           - 0.887203867225*m.b101 - 0.887203867225*m.b185 >= -0.887203867225)

m.c1642 = Constraint(expr=m.x215**2 + m.x216**2 + m.x225**2 + m.x226**2 - 2*m.x215*m.x225 - 2*m.x216*m.x226
                           - 1.436939228176*m.b65 - 1.436939228176*m.b110 >= -1.436939228176)

m.c1643 = Constraint(expr=m.x217**2 + m.x218**2 + m.x225**2 + m.x226**2 - 2*m.x218*m.x226 - 2*m.x217*m.x225
                           - 1.436939228176*m.b74 - 1.436939228176*m.b110 >= -1.436939228176)

m.c1644 = Constraint(expr=m.x219**2 + m.x220**2 + m.x225**2 + m.x226**2 - 2*m.x220*m.x226 - 2*m.x219*m.x225
                           - 1.436939228176*m.b83 - 1.436939228176*m.b110 >= -1.436939228176)

m.c1645 = Constraint(expr=m.x221**2 + m.x222**2 + m.x225**2 + m.x226**2 - 2*m.x221*m.x225 - 2*m.x222*m.x226
                           - 1.436939228176*m.b92 - 1.436939228176*m.b110 >= -1.436939228176)

m.c1646 = Constraint(expr=m.x223**2 + m.x224**2 + m.x225**2 + m.x226**2 - 2*m.x223*m.x225 - 2*m.x224*m.x226
                           - 1.436939228176*m.b101 - 1.436939228176*m.b110 >= -1.436939228176)

m.c1647 = Constraint(expr=m.x225**2 + m.x226**2 + m.x227**2 + m.x228**2 - 2*m.x225*m.x227 - 2*m.x226*m.x228
                           - 0.887203867225*m.b110 - 0.887203867225*m.b125 >= -0.887203867225)

m.c1648 = Constraint(expr=m.x225**2 + m.x226**2 + m.x229**2 + m.x230**2 - 2*m.x225*m.x229 - 2*m.x226*m.x230
                           - 0.887203867225*m.b110 - 0.887203867225*m.b140 >= -0.887203867225)

m.c1649 = Constraint(expr=m.x225**2 + m.x226**2 + m.x231**2 + m.x232**2 - 2*m.x225*m.x231 - 2*m.x226*m.x232
                           - 0.887203867225*m.b110 - 0.887203867225*m.b155 >= -0.887203867225)

m.c1650 = Constraint(expr=m.x225**2 + m.x226**2 + m.x233**2 + m.x234**2 - 2*m.x225*m.x233 - 2*m.x226*m.x234
                           - 0.887203867225*m.b110 - 0.887203867225*m.b170 >= -0.887203867225)

m.c1651 = Constraint(expr=m.x225**2 + m.x226**2 + m.x235**2 + m.x236**2 - 2*m.x225*m.x235 - 2*m.x226*m.x236
                           - 0.887203867225*m.b110 - 0.887203867225*m.b185 >= -0.887203867225)

m.c1652 = Constraint(expr=m.x215**2 + m.x216**2 + m.x227**2 + m.x228**2 - 2*m.x216*m.x228 - 2*m.x215*m.x227
                           - 0.887203867225*m.b65 - 0.887203867225*m.b125 >= -0.887203867225)

m.c1653 = Constraint(expr=m.x217**2 + m.x218**2 + m.x227**2 + m.x228**2 - 2*m.x217*m.x227 - 2*m.x218*m.x228
                           - 0.887203867225*m.b74 - 0.887203867225*m.b125 >= -0.887203867225)

m.c1654 = Constraint(expr=m.x219**2 + m.x220**2 + m.x227**2 + m.x228**2 - 2*m.x220*m.x228 - 2*m.x219*m.x227
                           - 0.887203867225*m.b83 - 0.887203867225*m.b125 >= -0.887203867225)

m.c1655 = Constraint(expr=m.x221**2 + m.x222**2 + m.x227**2 + m.x228**2 - 2*m.x221*m.x227 - 2*m.x222*m.x228
                           - 0.887203867225*m.b92 - 0.887203867225*m.b125 >= -0.887203867225)

m.c1656 = Constraint(expr=m.x223**2 + m.x224**2 + m.x227**2 + m.x228**2 - 2*m.x223*m.x227 - 2*m.x224*m.x228
                           - 0.887203867225*m.b101 - 0.887203867225*m.b125 >= -0.887203867225)

m.c1657 = Constraint(expr=m.x225**2 + m.x226**2 + m.x227**2 + m.x228**2 - 2*m.x225*m.x227 - 2*m.x226*m.x228
                           - 0.887203867225*m.b110 - 0.887203867225*m.b125 >= -0.887203867225)

m.c1658 = Constraint(expr=m.x227**2 + m.x228**2 + m.x229**2 + m.x230**2 - 2*m.x227*m.x229 - 2*m.x228*m.x230
                           - 0.469370231236*m.b125 - 0.469370231236*m.b140 >= -0.469370231236)

m.c1659 = Constraint(expr=m.x227**2 + m.x228**2 + m.x231**2 + m.x232**2 - 2*m.x227*m.x231 - 2*m.x228*m.x232
                           - 0.469370231236*m.b125 - 0.469370231236*m.b155 >= -0.469370231236)

m.c1660 = Constraint(expr=m.x227**2 + m.x228**2 + m.x233**2 + m.x234**2 - 2*m.x227*m.x233 - 2*m.x228*m.x234
                           - 0.469370231236*m.b125 - 0.469370231236*m.b170 >= -0.469370231236)

m.c1661 = Constraint(expr=m.x227**2 + m.x228**2 + m.x235**2 + m.x236**2 - 2*m.x227*m.x235 - 2*m.x228*m.x236
                           - 0.469370231236*m.b125 - 0.469370231236*m.b185 >= -0.469370231236)

m.c1662 = Constraint(expr=m.x215**2 + m.x216**2 + m.x229**2 + m.x230**2 - 2*m.x215*m.x229 - 2*m.x216*m.x230
                           - 0.887203867225*m.b65 - 0.887203867225*m.b140 >= -0.887203867225)

m.c1663 = Constraint(expr=m.x217**2 + m.x218**2 + m.x229**2 + m.x230**2 - 2*m.x218*m.x230 - 2*m.x217*m.x229
                           - 0.887203867225*m.b74 - 0.887203867225*m.b140 >= -0.887203867225)

m.c1664 = Constraint(expr=m.x219**2 + m.x220**2 + m.x229**2 + m.x230**2 - 2*m.x220*m.x230 - 2*m.x219*m.x229
                           - 0.887203867225*m.b83 - 0.887203867225*m.b140 >= -0.887203867225)

m.c1665 = Constraint(expr=m.x221**2 + m.x222**2 + m.x229**2 + m.x230**2 - 2*m.x221*m.x229 - 2*m.x222*m.x230
                           - 0.887203867225*m.b92 - 0.887203867225*m.b140 >= -0.887203867225)

m.c1666 = Constraint(expr=m.x223**2 + m.x224**2 + m.x229**2 + m.x230**2 - 2*m.x223*m.x229 - 2*m.x224*m.x230
                           - 0.887203867225*m.b101 - 0.887203867225*m.b140 >= -0.887203867225)

m.c1667 = Constraint(expr=m.x225**2 + m.x226**2 + m.x229**2 + m.x230**2 - 2*m.x225*m.x229 - 2*m.x226*m.x230
                           - 0.887203867225*m.b110 - 0.887203867225*m.b140 >= -0.887203867225)

m.c1668 = Constraint(expr=m.x227**2 + m.x228**2 + m.x229**2 + m.x230**2 - 2*m.x227*m.x229 - 2*m.x228*m.x230
                           - 0.469370231236*m.b125 - 0.469370231236*m.b140 >= -0.469370231236)

m.c1669 = Constraint(expr=m.x229**2 + m.x230**2 + m.x231**2 + m.x232**2 - 2*m.x229*m.x231 - 2*m.x230*m.x232
                           - 0.469370231236*m.b140 - 0.469370231236*m.b155 >= -0.469370231236)

m.c1670 = Constraint(expr=m.x229**2 + m.x230**2 + m.x233**2 + m.x234**2 - 2*m.x229*m.x233 - 2*m.x230*m.x234
                           - 0.469370231236*m.b140 - 0.469370231236*m.b170 >= -0.469370231236)

m.c1671 = Constraint(expr=m.x229**2 + m.x230**2 + m.x235**2 + m.x236**2 - 2*m.x229*m.x235 - 2*m.x230*m.x236
                           - 0.469370231236*m.b140 - 0.469370231236*m.b185 >= -0.469370231236)

m.c1672 = Constraint(expr=m.x215**2 + m.x216**2 + m.x231**2 + m.x232**2 - 2*m.x216*m.x232 - 2*m.x215*m.x231
                           - 0.887203867225*m.b65 - 0.887203867225*m.b155 >= -0.887203867225)

m.c1673 = Constraint(expr=m.x217**2 + m.x218**2 + m.x231**2 + m.x232**2 - 2*m.x218*m.x232 - 2*m.x217*m.x231
                           - 0.887203867225*m.b74 - 0.887203867225*m.b155 >= -0.887203867225)

m.c1674 = Constraint(expr=m.x219**2 + m.x220**2 + m.x231**2 + m.x232**2 - 2*m.x219*m.x231 - 2*m.x220*m.x232
                           - 0.887203867225*m.b83 - 0.887203867225*m.b155 >= -0.887203867225)

m.c1675 = Constraint(expr=m.x221**2 + m.x222**2 + m.x231**2 + m.x232**2 - 2*m.x221*m.x231 - 2*m.x222*m.x232
                           - 0.887203867225*m.b92 - 0.887203867225*m.b155 >= -0.887203867225)

m.c1676 = Constraint(expr=m.x223**2 + m.x224**2 + m.x231**2 + m.x232**2 - 2*m.x223*m.x231 - 2*m.x224*m.x232
                           - 0.887203867225*m.b101 - 0.887203867225*m.b155 >= -0.887203867225)

m.c1677 = Constraint(expr=m.x225**2 + m.x226**2 + m.x231**2 + m.x232**2 - 2*m.x225*m.x231 - 2*m.x226*m.x232
                           - 0.887203867225*m.b110 - 0.887203867225*m.b155 >= -0.887203867225)

m.c1678 = Constraint(expr=m.x227**2 + m.x228**2 + m.x231**2 + m.x232**2 - 2*m.x227*m.x231 - 2*m.x228*m.x232
                           - 0.469370231236*m.b125 - 0.469370231236*m.b155 >= -0.469370231236)

m.c1679 = Constraint(expr=m.x229**2 + m.x230**2 + m.x231**2 + m.x232**2 - 2*m.x229*m.x231 - 2*m.x230*m.x232
                           - 0.469370231236*m.b140 - 0.469370231236*m.b155 >= -0.469370231236)

m.c1680 = Constraint(expr=m.x231**2 + m.x232**2 + m.x233**2 + m.x234**2 - 2*m.x231*m.x233 - 2*m.x232*m.x234
                           - 0.469370231236*m.b155 - 0.469370231236*m.b170 >= -0.469370231236)

m.c1681 = Constraint(expr=m.x231**2 + m.x232**2 + m.x235**2 + m.x236**2 - 2*m.x231*m.x235 - 2*m.x232*m.x236
                           - 0.469370231236*m.b155 - 0.469370231236*m.b185 >= -0.469370231236)

m.c1682 = Constraint(expr=m.x215**2 + m.x216**2 + m.x233**2 + m.x234**2 - 2*m.x216*m.x234 - 2*m.x215*m.x233
                           - 0.887203867225*m.b65 - 0.887203867225*m.b170 >= -0.887203867225)

m.c1683 = Constraint(expr=m.x217**2 + m.x218**2 + m.x233**2 + m.x234**2 - 2*m.x217*m.x233 - 2*m.x218*m.x234
                           - 0.887203867225*m.b74 - 0.887203867225*m.b170 >= -0.887203867225)

m.c1684 = Constraint(expr=m.x219**2 + m.x220**2 + m.x233**2 + m.x234**2 - 2*m.x219*m.x233 - 2*m.x220*m.x234
                           - 0.887203867225*m.b83 - 0.887203867225*m.b170 >= -0.887203867225)

m.c1685 = Constraint(expr=m.x221**2 + m.x222**2 + m.x233**2 + m.x234**2 - 2*m.x221*m.x233 - 2*m.x222*m.x234
                           - 0.887203867225*m.b92 - 0.887203867225*m.b170 >= -0.887203867225)

m.c1686 = Constraint(expr=m.x223**2 + m.x224**2 + m.x233**2 + m.x234**2 - 2*m.x223*m.x233 - 2*m.x224*m.x234
                           - 0.887203867225*m.b101 - 0.887203867225*m.b170 >= -0.887203867225)

m.c1687 = Constraint(expr=m.x225**2 + m.x226**2 + m.x233**2 + m.x234**2 - 2*m.x225*m.x233 - 2*m.x226*m.x234
                           - 0.887203867225*m.b110 - 0.887203867225*m.b170 >= -0.887203867225)

m.c1688 = Constraint(expr=m.x227**2 + m.x228**2 + m.x233**2 + m.x234**2 - 2*m.x227*m.x233 - 2*m.x228*m.x234
                           - 0.469370231236*m.b125 - 0.469370231236*m.b170 >= -0.469370231236)

m.c1689 = Constraint(expr=m.x229**2 + m.x230**2 + m.x233**2 + m.x234**2 - 2*m.x229*m.x233 - 2*m.x230*m.x234
                           - 0.469370231236*m.b140 - 0.469370231236*m.b170 >= -0.469370231236)

m.c1690 = Constraint(expr=m.x231**2 + m.x232**2 + m.x233**2 + m.x234**2 - 2*m.x231*m.x233 - 2*m.x232*m.x234
                           - 0.469370231236*m.b155 - 0.469370231236*m.b170 >= -0.469370231236)

m.c1691 = Constraint(expr=m.x233**2 + m.x234**2 + m.x235**2 + m.x236**2 - 2*m.x233*m.x235 - 2*m.x234*m.x236
                           - 0.469370231236*m.b170 - 0.469370231236*m.b185 >= -0.469370231236)

m.c1692 = Constraint(expr=m.x215**2 + m.x216**2 + m.x235**2 + m.x236**2 - 2*m.x215*m.x235 - 2*m.x216*m.x236
                           - 0.887203867225*m.b65 - 0.887203867225*m.b185 >= -0.887203867225)

m.c1693 = Constraint(expr=m.x217**2 + m.x218**2 + m.x235**2 + m.x236**2 - 2*m.x217*m.x235 - 2*m.x218*m.x236
                           - 0.887203867225*m.b74 - 0.887203867225*m.b185 >= -0.887203867225)

m.c1694 = Constraint(expr=m.x219**2 + m.x220**2 + m.x235**2 + m.x236**2 - 2*m.x219*m.x235 - 2*m.x220*m.x236
                           - 0.887203867225*m.b83 - 0.887203867225*m.b185 >= -0.887203867225)

m.c1695 = Constraint(expr=m.x221**2 + m.x222**2 + m.x235**2 + m.x236**2 - 2*m.x221*m.x235 - 2*m.x222*m.x236
                           - 0.887203867225*m.b92 - 0.887203867225*m.b185 >= -0.887203867225)

m.c1696 = Constraint(expr=m.x223**2 + m.x224**2 + m.x235**2 + m.x236**2 - 2*m.x223*m.x235 - 2*m.x224*m.x236
                           - 0.887203867225*m.b101 - 0.887203867225*m.b185 >= -0.887203867225)

m.c1697 = Constraint(expr=m.x225**2 + m.x226**2 + m.x235**2 + m.x236**2 - 2*m.x225*m.x235 - 2*m.x226*m.x236
                           - 0.887203867225*m.b110 - 0.887203867225*m.b185 >= -0.887203867225)

m.c1698 = Constraint(expr=m.x227**2 + m.x228**2 + m.x235**2 + m.x236**2 - 2*m.x227*m.x235 - 2*m.x228*m.x236
                           - 0.469370231236*m.b125 - 0.469370231236*m.b185 >= -0.469370231236)

m.c1699 = Constraint(expr=m.x229**2 + m.x230**2 + m.x235**2 + m.x236**2 - 2*m.x229*m.x235 - 2*m.x230*m.x236
                           - 0.469370231236*m.b140 - 0.469370231236*m.b185 >= -0.469370231236)

m.c1700 = Constraint(expr=m.x231**2 + m.x232**2 + m.x235**2 + m.x236**2 - 2*m.x231*m.x235 - 2*m.x232*m.x236
                           - 0.469370231236*m.b155 - 0.469370231236*m.b185 >= -0.469370231236)

m.c1701 = Constraint(expr=m.x233**2 + m.x234**2 + m.x235**2 + m.x236**2 - 2*m.x233*m.x235 - 2*m.x234*m.x236
                           - 0.469370231236*m.b170 - 0.469370231236*m.b185 >= -0.469370231236)

m.c1702 = Constraint(expr=m.x215**2 + m.x216**2 + m.x217**2 + m.x218**2 - 2*m.x215*m.x217 - 2*m.x216*m.x218
                           - 1.436939228176*m.b66 - 1.436939228176*m.b75 >= -1.436939228176)

m.c1703 = Constraint(expr=m.x215**2 + m.x216**2 + m.x219**2 + m.x220**2 - 2*m.x215*m.x219 - 2*m.x216*m.x220
                           - 1.436939228176*m.b66 - 1.436939228176*m.b84 >= -1.436939228176)

m.c1704 = Constraint(expr=m.x215**2 + m.x216**2 + m.x221**2 + m.x222**2 - 2*m.x216*m.x222 - 2*m.x215*m.x221
                           - 1.436939228176*m.b66 - 1.436939228176*m.b93 >= -1.436939228176)

m.c1705 = Constraint(expr=m.x215**2 + m.x216**2 + m.x223**2 + m.x224**2 - 2*m.x216*m.x224 - 2*m.x215*m.x223
                           - 1.436939228176*m.b66 - 1.436939228176*m.b102 >= -1.436939228176)

m.c1706 = Constraint(expr=m.x215**2 + m.x216**2 + m.x225**2 + m.x226**2 - 2*m.x215*m.x225 - 2*m.x216*m.x226
                           - 1.436939228176*m.b66 - 1.436939228176*m.b111 >= -1.436939228176)

m.c1707 = Constraint(expr=m.x215**2 + m.x216**2 + m.x227**2 + m.x228**2 - 2*m.x216*m.x228 - 2*m.x215*m.x227
                           - 0.887203867225*m.b66 - 0.887203867225*m.b126 >= -0.887203867225)

m.c1708 = Constraint(expr=m.x215**2 + m.x216**2 + m.x229**2 + m.x230**2 - 2*m.x215*m.x229 - 2*m.x216*m.x230
                           - 0.887203867225*m.b66 - 0.887203867225*m.b141 >= -0.887203867225)

m.c1709 = Constraint(expr=m.x215**2 + m.x216**2 + m.x231**2 + m.x232**2 - 2*m.x216*m.x232 - 2*m.x215*m.x231
                           - 0.887203867225*m.b66 - 0.887203867225*m.b156 >= -0.887203867225)

m.c1710 = Constraint(expr=m.x215**2 + m.x216**2 + m.x233**2 + m.x234**2 - 2*m.x216*m.x234 - 2*m.x215*m.x233
                           - 0.887203867225*m.b66 - 0.887203867225*m.b171 >= -0.887203867225)

m.c1711 = Constraint(expr=m.x215**2 + m.x216**2 + m.x235**2 + m.x236**2 - 2*m.x215*m.x235 - 2*m.x216*m.x236
                           - 0.887203867225*m.b66 - 0.887203867225*m.b186 >= -0.887203867225)

m.c1712 = Constraint(expr=m.x215**2 + m.x216**2 + m.x217**2 + m.x218**2 - 2*m.x215*m.x217 - 2*m.x216*m.x218
                           - 1.436939228176*m.b66 - 1.436939228176*m.b75 >= -1.436939228176)

m.c1713 = Constraint(expr=m.x217**2 + m.x218**2 + m.x219**2 + m.x220**2 - 2*m.x217*m.x219 - 2*m.x218*m.x220
                           - 1.436939228176*m.b75 - 1.436939228176*m.b84 >= -1.436939228176)

m.c1714 = Constraint(expr=m.x217**2 + m.x218**2 + m.x221**2 + m.x222**2 - 2*m.x218*m.x222 - 2*m.x217*m.x221
                           - 1.436939228176*m.b75 - 1.436939228176*m.b93 >= -1.436939228176)

m.c1715 = Constraint(expr=m.x217**2 + m.x218**2 + m.x223**2 + m.x224**2 - 2*m.x217*m.x223 - 2*m.x218*m.x224
                           - 1.436939228176*m.b75 - 1.436939228176*m.b102 >= -1.436939228176)

m.c1716 = Constraint(expr=m.x217**2 + m.x218**2 + m.x225**2 + m.x226**2 - 2*m.x218*m.x226 - 2*m.x217*m.x225
                           - 1.436939228176*m.b75 - 1.436939228176*m.b111 >= -1.436939228176)

m.c1717 = Constraint(expr=m.x217**2 + m.x218**2 + m.x227**2 + m.x228**2 - 2*m.x217*m.x227 - 2*m.x218*m.x228
                           - 0.887203867225*m.b75 - 0.887203867225*m.b126 >= -0.887203867225)

m.c1718 = Constraint(expr=m.x217**2 + m.x218**2 + m.x229**2 + m.x230**2 - 2*m.x218*m.x230 - 2*m.x217*m.x229
                           - 0.887203867225*m.b75 - 0.887203867225*m.b141 >= -0.887203867225)

m.c1719 = Constraint(expr=m.x217**2 + m.x218**2 + m.x231**2 + m.x232**2 - 2*m.x218*m.x232 - 2*m.x217*m.x231
                           - 0.887203867225*m.b75 - 0.887203867225*m.b156 >= -0.887203867225)

m.c1720 = Constraint(expr=m.x217**2 + m.x218**2 + m.x233**2 + m.x234**2 - 2*m.x217*m.x233 - 2*m.x218*m.x234
                           - 0.887203867225*m.b75 - 0.887203867225*m.b171 >= -0.887203867225)

m.c1721 = Constraint(expr=m.x217**2 + m.x218**2 + m.x235**2 + m.x236**2 - 2*m.x217*m.x235 - 2*m.x218*m.x236
                           - 0.887203867225*m.b75 - 0.887203867225*m.b186 >= -0.887203867225)

m.c1722 = Constraint(expr=m.x215**2 + m.x216**2 + m.x219**2 + m.x220**2 - 2*m.x215*m.x219 - 2*m.x216*m.x220
                           - 1.436939228176*m.b66 - 1.436939228176*m.b84 >= -1.436939228176)

m.c1723 = Constraint(expr=m.x217**2 + m.x218**2 + m.x219**2 + m.x220**2 - 2*m.x217*m.x219 - 2*m.x218*m.x220
                           - 1.436939228176*m.b75 - 1.436939228176*m.b84 >= -1.436939228176)

m.c1724 = Constraint(expr=m.x219**2 + m.x220**2 + m.x221**2 + m.x222**2 - 2*m.x219*m.x221 - 2*m.x220*m.x222
                           - 1.436939228176*m.b84 - 1.436939228176*m.b93 >= -1.436939228176)

m.c1725 = Constraint(expr=m.x219**2 + m.x220**2 + m.x223**2 + m.x224**2 - 2*m.x219*m.x223 - 2*m.x220*m.x224
                           - 1.436939228176*m.b84 - 1.436939228176*m.b102 >= -1.436939228176)

m.c1726 = Constraint(expr=m.x219**2 + m.x220**2 + m.x225**2 + m.x226**2 - 2*m.x220*m.x226 - 2*m.x219*m.x225
                           - 1.436939228176*m.b84 - 1.436939228176*m.b111 >= -1.436939228176)

m.c1727 = Constraint(expr=m.x219**2 + m.x220**2 + m.x227**2 + m.x228**2 - 2*m.x219*m.x227 - 2*m.x220*m.x228
                           - 0.887203867225*m.b84 - 0.887203867225*m.b126 >= -0.887203867225)

m.c1728 = Constraint(expr=m.x219**2 + m.x220**2 + m.x229**2 + m.x230**2 - 2*m.x220*m.x230 - 2*m.x219*m.x229
                           - 0.887203867225*m.b84 - 0.887203867225*m.b141 >= -0.887203867225)

m.c1729 = Constraint(expr=m.x219**2 + m.x220**2 + m.x231**2 + m.x232**2 - 2*m.x219*m.x231 - 2*m.x220*m.x232
                           - 0.887203867225*m.b84 - 0.887203867225*m.b156 >= -0.887203867225)

m.c1730 = Constraint(expr=m.x219**2 + m.x220**2 + m.x233**2 + m.x234**2 - 2*m.x220*m.x234 - 2*m.x219*m.x233
                           - 0.887203867225*m.b84 - 0.887203867225*m.b171 >= -0.887203867225)

m.c1731 = Constraint(expr=m.x219**2 + m.x220**2 + m.x235**2 + m.x236**2 - 2*m.x219*m.x235 - 2*m.x220*m.x236
                           - 0.887203867225*m.b84 - 0.887203867225*m.b186 >= -0.887203867225)

m.c1732 = Constraint(expr=m.x215**2 + m.x216**2 + m.x221**2 + m.x222**2 - 2*m.x216*m.x222 - 2*m.x215*m.x221
                           - 1.436939228176*m.b66 - 1.436939228176*m.b93 >= -1.436939228176)

m.c1733 = Constraint(expr=m.x217**2 + m.x218**2 + m.x221**2 + m.x222**2 - 2*m.x218*m.x222 - 2*m.x217*m.x221
                           - 1.436939228176*m.b75 - 1.436939228176*m.b93 >= -1.436939228176)

m.c1734 = Constraint(expr=m.x219**2 + m.x220**2 + m.x221**2 + m.x222**2 - 2*m.x219*m.x221 - 2*m.x220*m.x222
                           - 1.436939228176*m.b84 - 1.436939228176*m.b93 >= -1.436939228176)

m.c1735 = Constraint(expr=m.x221**2 + m.x222**2 + m.x223**2 + m.x224**2 - 2*m.x221*m.x223 - 2*m.x222*m.x224
                           - 1.436939228176*m.b93 - 1.436939228176*m.b102 >= -1.436939228176)

m.c1736 = Constraint(expr=m.x221**2 + m.x222**2 + m.x225**2 + m.x226**2 - 2*m.x221*m.x225 - 2*m.x222*m.x226
                           - 1.436939228176*m.b93 - 1.436939228176*m.b111 >= -1.436939228176)

m.c1737 = Constraint(expr=m.x221**2 + m.x222**2 + m.x227**2 + m.x228**2 - 2*m.x221*m.x227 - 2*m.x222*m.x228
                           - 0.887203867225*m.b93 - 0.887203867225*m.b126 >= -0.887203867225)

m.c1738 = Constraint(expr=m.x221**2 + m.x222**2 + m.x229**2 + m.x230**2 - 2*m.x221*m.x229 - 2*m.x222*m.x230
                           - 0.887203867225*m.b93 - 0.887203867225*m.b141 >= -0.887203867225)

m.c1739 = Constraint(expr=m.x221**2 + m.x222**2 + m.x231**2 + m.x232**2 - 2*m.x221*m.x231 - 2*m.x222*m.x232
                           - 0.887203867225*m.b93 - 0.887203867225*m.b156 >= -0.887203867225)

m.c1740 = Constraint(expr=m.x221**2 + m.x222**2 + m.x233**2 + m.x234**2 - 2*m.x221*m.x233 - 2*m.x222*m.x234
                           - 0.887203867225*m.b93 - 0.887203867225*m.b171 >= -0.887203867225)

m.c1741 = Constraint(expr=m.x221**2 + m.x222**2 + m.x235**2 + m.x236**2 - 2*m.x221*m.x235 - 2*m.x222*m.x236
                           - 0.887203867225*m.b93 - 0.887203867225*m.b186 >= -0.887203867225)

m.c1742 = Constraint(expr=m.x215**2 + m.x216**2 + m.x223**2 + m.x224**2 - 2*m.x216*m.x224 - 2*m.x215*m.x223
                           - 1.436939228176*m.b66 - 1.436939228176*m.b102 >= -1.436939228176)

m.c1743 = Constraint(expr=m.x217**2 + m.x218**2 + m.x223**2 + m.x224**2 - 2*m.x217*m.x223 - 2*m.x218*m.x224
                           - 1.436939228176*m.b75 - 1.436939228176*m.b102 >= -1.436939228176)

m.c1744 = Constraint(expr=m.x219**2 + m.x220**2 + m.x223**2 + m.x224**2 - 2*m.x219*m.x223 - 2*m.x220*m.x224
                           - 1.436939228176*m.b84 - 1.436939228176*m.b102 >= -1.436939228176)

m.c1745 = Constraint(expr=m.x221**2 + m.x222**2 + m.x223**2 + m.x224**2 - 2*m.x221*m.x223 - 2*m.x222*m.x224
                           - 1.436939228176*m.b93 - 1.436939228176*m.b102 >= -1.436939228176)

m.c1746 = Constraint(expr=m.x223**2 + m.x224**2 + m.x225**2 + m.x226**2 - 2*m.x223*m.x225 - 2*m.x224*m.x226
                           - 1.436939228176*m.b102 - 1.436939228176*m.b111 >= -1.436939228176)

m.c1747 = Constraint(expr=m.x223**2 + m.x224**2 + m.x227**2 + m.x228**2 - 2*m.x223*m.x227 - 2*m.x224*m.x228
                           - 0.887203867225*m.b102 - 0.887203867225*m.b126 >= -0.887203867225)

m.c1748 = Constraint(expr=m.x223**2 + m.x224**2 + m.x229**2 + m.x230**2 - 2*m.x223*m.x229 - 2*m.x224*m.x230
                           - 0.887203867225*m.b102 - 0.887203867225*m.b141 >= -0.887203867225)

m.c1749 = Constraint(expr=m.x223**2 + m.x224**2 + m.x231**2 + m.x232**2 - 2*m.x223*m.x231 - 2*m.x224*m.x232
                           - 0.887203867225*m.b102 - 0.887203867225*m.b156 >= -0.887203867225)

m.c1750 = Constraint(expr=m.x223**2 + m.x224**2 + m.x233**2 + m.x234**2 - 2*m.x223*m.x233 - 2*m.x224*m.x234
                           - 0.887203867225*m.b102 - 0.887203867225*m.b171 >= -0.887203867225)

m.c1751 = Constraint(expr=m.x223**2 + m.x224**2 + m.x235**2 + m.x236**2 - 2*m.x223*m.x235 - 2*m.x224*m.x236
                           - 0.887203867225*m.b102 - 0.887203867225*m.b186 >= -0.887203867225)

m.c1752 = Constraint(expr=m.x215**2 + m.x216**2 + m.x225**2 + m.x226**2 - 2*m.x215*m.x225 - 2*m.x216*m.x226
                           - 1.436939228176*m.b66 - 1.436939228176*m.b111 >= -1.436939228176)

m.c1753 = Constraint(expr=m.x217**2 + m.x218**2 + m.x225**2 + m.x226**2 - 2*m.x218*m.x226 - 2*m.x217*m.x225
                           - 1.436939228176*m.b75 - 1.436939228176*m.b111 >= -1.436939228176)

m.c1754 = Constraint(expr=m.x219**2 + m.x220**2 + m.x225**2 + m.x226**2 - 2*m.x220*m.x226 - 2*m.x219*m.x225
                           - 1.436939228176*m.b84 - 1.436939228176*m.b111 >= -1.436939228176)

m.c1755 = Constraint(expr=m.x221**2 + m.x222**2 + m.x225**2 + m.x226**2 - 2*m.x221*m.x225 - 2*m.x222*m.x226
                           - 1.436939228176*m.b93 - 1.436939228176*m.b111 >= -1.436939228176)

m.c1756 = Constraint(expr=m.x223**2 + m.x224**2 + m.x225**2 + m.x226**2 - 2*m.x223*m.x225 - 2*m.x224*m.x226
                           - 1.436939228176*m.b102 - 1.436939228176*m.b111 >= -1.436939228176)

m.c1757 = Constraint(expr=m.x225**2 + m.x226**2 + m.x227**2 + m.x228**2 - 2*m.x225*m.x227 - 2*m.x226*m.x228
                           - 0.887203867225*m.b111 - 0.887203867225*m.b126 >= -0.887203867225)

m.c1758 = Constraint(expr=m.x225**2 + m.x226**2 + m.x229**2 + m.x230**2 - 2*m.x225*m.x229 - 2*m.x226*m.x230
                           - 0.887203867225*m.b111 - 0.887203867225*m.b141 >= -0.887203867225)

m.c1759 = Constraint(expr=m.x225**2 + m.x226**2 + m.x231**2 + m.x232**2 - 2*m.x225*m.x231 - 2*m.x226*m.x232
                           - 0.887203867225*m.b111 - 0.887203867225*m.b156 >= -0.887203867225)

m.c1760 = Constraint(expr=m.x225**2 + m.x226**2 + m.x233**2 + m.x234**2 - 2*m.x225*m.x233 - 2*m.x226*m.x234
                           - 0.887203867225*m.b111 - 0.887203867225*m.b171 >= -0.887203867225)

m.c1761 = Constraint(expr=m.x225**2 + m.x226**2 + m.x235**2 + m.x236**2 - 2*m.x225*m.x235 - 2*m.x226*m.x236
                           - 0.887203867225*m.b111 - 0.887203867225*m.b186 >= -0.887203867225)

m.c1762 = Constraint(expr=m.x215**2 + m.x216**2 + m.x227**2 + m.x228**2 - 2*m.x216*m.x228 - 2*m.x215*m.x227
                           - 0.887203867225*m.b66 - 0.887203867225*m.b126 >= -0.887203867225)

m.c1763 = Constraint(expr=m.x217**2 + m.x218**2 + m.x227**2 + m.x228**2 - 2*m.x217*m.x227 - 2*m.x218*m.x228
                           - 0.887203867225*m.b75 - 0.887203867225*m.b126 >= -0.887203867225)

m.c1764 = Constraint(expr=m.x219**2 + m.x220**2 + m.x227**2 + m.x228**2 - 2*m.x219*m.x227 - 2*m.x220*m.x228
                           - 0.887203867225*m.b84 - 0.887203867225*m.b126 >= -0.887203867225)

m.c1765 = Constraint(expr=m.x221**2 + m.x222**2 + m.x227**2 + m.x228**2 - 2*m.x221*m.x227 - 2*m.x222*m.x228
                           - 0.887203867225*m.b93 - 0.887203867225*m.b126 >= -0.887203867225)

m.c1766 = Constraint(expr=m.x223**2 + m.x224**2 + m.x227**2 + m.x228**2 - 2*m.x223*m.x227 - 2*m.x224*m.x228
                           - 0.887203867225*m.b102 - 0.887203867225*m.b126 >= -0.887203867225)

m.c1767 = Constraint(expr=m.x225**2 + m.x226**2 + m.x227**2 + m.x228**2 - 2*m.x225*m.x227 - 2*m.x226*m.x228
                           - 0.887203867225*m.b111 - 0.887203867225*m.b126 >= -0.887203867225)

m.c1768 = Constraint(expr=m.x227**2 + m.x228**2 + m.x229**2 + m.x230**2 - 2*m.x227*m.x229 - 2*m.x228*m.x230
                           - 0.469370231236*m.b126 - 0.469370231236*m.b141 >= -0.469370231236)

m.c1769 = Constraint(expr=m.x227**2 + m.x228**2 + m.x231**2 + m.x232**2 - 2*m.x227*m.x231 - 2*m.x228*m.x232
                           - 0.469370231236*m.b126 - 0.469370231236*m.b156 >= -0.469370231236)

m.c1770 = Constraint(expr=m.x227**2 + m.x228**2 + m.x233**2 + m.x234**2 - 2*m.x227*m.x233 - 2*m.x228*m.x234
                           - 0.469370231236*m.b126 - 0.469370231236*m.b171 >= -0.469370231236)

m.c1771 = Constraint(expr=m.x227**2 + m.x228**2 + m.x235**2 + m.x236**2 - 2*m.x227*m.x235 - 2*m.x228*m.x236
                           - 0.469370231236*m.b126 - 0.469370231236*m.b186 >= -0.469370231236)

m.c1772 = Constraint(expr=m.x215**2 + m.x216**2 + m.x229**2 + m.x230**2 - 2*m.x215*m.x229 - 2*m.x216*m.x230
                           - 0.887203867225*m.b66 - 0.887203867225*m.b141 >= -0.887203867225)

m.c1773 = Constraint(expr=m.x217**2 + m.x218**2 + m.x229**2 + m.x230**2 - 2*m.x218*m.x230 - 2*m.x217*m.x229
                           - 0.887203867225*m.b75 - 0.887203867225*m.b141 >= -0.887203867225)

m.c1774 = Constraint(expr=m.x219**2 + m.x220**2 + m.x229**2 + m.x230**2 - 2*m.x220*m.x230 - 2*m.x219*m.x229
                           - 0.887203867225*m.b84 - 0.887203867225*m.b141 >= -0.887203867225)

m.c1775 = Constraint(expr=m.x221**2 + m.x222**2 + m.x229**2 + m.x230**2 - 2*m.x221*m.x229 - 2*m.x222*m.x230
                           - 0.887203867225*m.b93 - 0.887203867225*m.b141 >= -0.887203867225)

m.c1776 = Constraint(expr=m.x223**2 + m.x224**2 + m.x229**2 + m.x230**2 - 2*m.x223*m.x229 - 2*m.x224*m.x230
                           - 0.887203867225*m.b102 - 0.887203867225*m.b141 >= -0.887203867225)

m.c1777 = Constraint(expr=m.x225**2 + m.x226**2 + m.x229**2 + m.x230**2 - 2*m.x225*m.x229 - 2*m.x226*m.x230
                           - 0.887203867225*m.b111 - 0.887203867225*m.b141 >= -0.887203867225)

m.c1778 = Constraint(expr=m.x227**2 + m.x228**2 + m.x229**2 + m.x230**2 - 2*m.x227*m.x229 - 2*m.x228*m.x230
                           - 0.469370231236*m.b126 - 0.469370231236*m.b141 >= -0.469370231236)

m.c1779 = Constraint(expr=m.x229**2 + m.x230**2 + m.x231**2 + m.x232**2 - 2*m.x229*m.x231 - 2*m.x230*m.x232
                           - 0.469370231236*m.b141 - 0.469370231236*m.b156 >= -0.469370231236)

m.c1780 = Constraint(expr=m.x229**2 + m.x230**2 + m.x233**2 + m.x234**2 - 2*m.x229*m.x233 - 2*m.x230*m.x234
                           - 0.469370231236*m.b141 - 0.469370231236*m.b171 >= -0.469370231236)

m.c1781 = Constraint(expr=m.x229**2 + m.x230**2 + m.x235**2 + m.x236**2 - 2*m.x229*m.x235 - 2*m.x230*m.x236
                           - 0.469370231236*m.b141 - 0.469370231236*m.b186 >= -0.469370231236)

m.c1782 = Constraint(expr=m.x215**2 + m.x216**2 + m.x231**2 + m.x232**2 - 2*m.x216*m.x232 - 2*m.x215*m.x231
                           - 0.887203867225*m.b66 - 0.887203867225*m.b156 >= -0.887203867225)

m.c1783 = Constraint(expr=m.x217**2 + m.x218**2 + m.x231**2 + m.x232**2 - 2*m.x218*m.x232 - 2*m.x217*m.x231
                           - 0.887203867225*m.b75 - 0.887203867225*m.b156 >= -0.887203867225)

m.c1784 = Constraint(expr=m.x219**2 + m.x220**2 + m.x231**2 + m.x232**2 - 2*m.x219*m.x231 - 2*m.x220*m.x232
                           - 0.887203867225*m.b84 - 0.887203867225*m.b156 >= -0.887203867225)

m.c1785 = Constraint(expr=m.x221**2 + m.x222**2 + m.x231**2 + m.x232**2 - 2*m.x221*m.x231 - 2*m.x222*m.x232
                           - 0.887203867225*m.b93 - 0.887203867225*m.b156 >= -0.887203867225)

m.c1786 = Constraint(expr=m.x223**2 + m.x224**2 + m.x231**2 + m.x232**2 - 2*m.x223*m.x231 - 2*m.x224*m.x232
                           - 0.887203867225*m.b102 - 0.887203867225*m.b156 >= -0.887203867225)

m.c1787 = Constraint(expr=m.x225**2 + m.x226**2 + m.x231**2 + m.x232**2 - 2*m.x225*m.x231 - 2*m.x226*m.x232
                           - 0.887203867225*m.b111 - 0.887203867225*m.b156 >= -0.887203867225)

m.c1788 = Constraint(expr=m.x227**2 + m.x228**2 + m.x231**2 + m.x232**2 - 2*m.x227*m.x231 - 2*m.x228*m.x232
                           - 0.469370231236*m.b126 - 0.469370231236*m.b156 >= -0.469370231236)

m.c1789 = Constraint(expr=m.x229**2 + m.x230**2 + m.x231**2 + m.x232**2 - 2*m.x229*m.x231 - 2*m.x230*m.x232
                           - 0.469370231236*m.b141 - 0.469370231236*m.b156 >= -0.469370231236)

m.c1790 = Constraint(expr=m.x231**2 + m.x232**2 + m.x233**2 + m.x234**2 - 2*m.x231*m.x233 - 2*m.x232*m.x234
                           - 0.469370231236*m.b156 - 0.469370231236*m.b171 >= -0.469370231236)

m.c1791 = Constraint(expr=m.x231**2 + m.x232**2 + m.x235**2 + m.x236**2 - 2*m.x231*m.x235 - 2*m.x232*m.x236
                           - 0.469370231236*m.b156 - 0.469370231236*m.b186 >= -0.469370231236)

m.c1792 = Constraint(expr=m.x215**2 + m.x216**2 + m.x233**2 + m.x234**2 - 2*m.x216*m.x234 - 2*m.x215*m.x233
                           - 0.887203867225*m.b66 - 0.887203867225*m.b171 >= -0.887203867225)

m.c1793 = Constraint(expr=m.x217**2 + m.x218**2 + m.x233**2 + m.x234**2 - 2*m.x217*m.x233 - 2*m.x218*m.x234
                           - 0.887203867225*m.b75 - 0.887203867225*m.b171 >= -0.887203867225)

m.c1794 = Constraint(expr=m.x219**2 + m.x220**2 + m.x233**2 + m.x234**2 - 2*m.x220*m.x234 - 2*m.x219*m.x233
                           - 0.887203867225*m.b84 - 0.887203867225*m.b171 >= -0.887203867225)

m.c1795 = Constraint(expr=m.x221**2 + m.x222**2 + m.x233**2 + m.x234**2 - 2*m.x221*m.x233 - 2*m.x222*m.x234
                           - 0.887203867225*m.b93 - 0.887203867225*m.b171 >= -0.887203867225)

m.c1796 = Constraint(expr=m.x223**2 + m.x224**2 + m.x233**2 + m.x234**2 - 2*m.x223*m.x233 - 2*m.x224*m.x234
                           - 0.887203867225*m.b102 - 0.887203867225*m.b171 >= -0.887203867225)

m.c1797 = Constraint(expr=m.x225**2 + m.x226**2 + m.x233**2 + m.x234**2 - 2*m.x225*m.x233 - 2*m.x226*m.x234
                           - 0.887203867225*m.b111 - 0.887203867225*m.b171 >= -0.887203867225)

m.c1798 = Constraint(expr=m.x227**2 + m.x228**2 + m.x233**2 + m.x234**2 - 2*m.x227*m.x233 - 2*m.x228*m.x234
                           - 0.469370231236*m.b126 - 0.469370231236*m.b171 >= -0.469370231236)

m.c1799 = Constraint(expr=m.x229**2 + m.x230**2 + m.x233**2 + m.x234**2 - 2*m.x229*m.x233 - 2*m.x230*m.x234
                           - 0.469370231236*m.b141 - 0.469370231236*m.b171 >= -0.469370231236)

m.c1800 = Constraint(expr=m.x231**2 + m.x232**2 + m.x233**2 + m.x234**2 - 2*m.x231*m.x233 - 2*m.x232*m.x234
                           - 0.469370231236*m.b156 - 0.469370231236*m.b171 >= -0.469370231236)

m.c1801 = Constraint(expr=m.x233**2 + m.x234**2 + m.x235**2 + m.x236**2 - 2*m.x233*m.x235 - 2*m.x234*m.x236
                           - 0.469370231236*m.b171 - 0.469370231236*m.b186 >= -0.469370231236)

m.c1802 = Constraint(expr=m.x215**2 + m.x216**2 + m.x235**2 + m.x236**2 - 2*m.x215*m.x235 - 2*m.x216*m.x236
                           - 0.887203867225*m.b66 - 0.887203867225*m.b186 >= -0.887203867225)

m.c1803 = Constraint(expr=m.x217**2 + m.x218**2 + m.x235**2 + m.x236**2 - 2*m.x217*m.x235 - 2*m.x218*m.x236
                           - 0.887203867225*m.b75 - 0.887203867225*m.b186 >= -0.887203867225)

m.c1804 = Constraint(expr=m.x219**2 + m.x220**2 + m.x235**2 + m.x236**2 - 2*m.x219*m.x235 - 2*m.x220*m.x236
                           - 0.887203867225*m.b84 - 0.887203867225*m.b186 >= -0.887203867225)

m.c1805 = Constraint(expr=m.x221**2 + m.x222**2 + m.x235**2 + m.x236**2 - 2*m.x221*m.x235 - 2*m.x222*m.x236
                           - 0.887203867225*m.b93 - 0.887203867225*m.b186 >= -0.887203867225)

m.c1806 = Constraint(expr=m.x223**2 + m.x224**2 + m.x235**2 + m.x236**2 - 2*m.x223*m.x235 - 2*m.x224*m.x236
                           - 0.887203867225*m.b102 - 0.887203867225*m.b186 >= -0.887203867225)

m.c1807 = Constraint(expr=m.x225**2 + m.x226**2 + m.x235**2 + m.x236**2 - 2*m.x225*m.x235 - 2*m.x226*m.x236
                           - 0.887203867225*m.b111 - 0.887203867225*m.b186 >= -0.887203867225)

m.c1808 = Constraint(expr=m.x227**2 + m.x228**2 + m.x235**2 + m.x236**2 - 2*m.x227*m.x235 - 2*m.x228*m.x236
                           - 0.469370231236*m.b126 - 0.469370231236*m.b186 >= -0.469370231236)

m.c1809 = Constraint(expr=m.x229**2 + m.x230**2 + m.x235**2 + m.x236**2 - 2*m.x229*m.x235 - 2*m.x230*m.x236
                           - 0.469370231236*m.b141 - 0.469370231236*m.b186 >= -0.469370231236)

m.c1810 = Constraint(expr=m.x231**2 + m.x232**2 + m.x235**2 + m.x236**2 - 2*m.x231*m.x235 - 2*m.x232*m.x236
                           - 0.469370231236*m.b156 - 0.469370231236*m.b186 >= -0.469370231236)

m.c1811 = Constraint(expr=m.x233**2 + m.x234**2 + m.x235**2 + m.x236**2 - 2*m.x233*m.x235 - 2*m.x234*m.x236
                           - 0.469370231236*m.b171 - 0.469370231236*m.b186 >= -0.469370231236)

m.c1812 = Constraint(expr=m.x215**2 + m.x216**2 + m.x217**2 + m.x218**2 - 2*m.x215*m.x217 - 2*m.x216*m.x218
                           - 1.436939228176*m.b67 - 1.436939228176*m.b76 >= -1.436939228176)

m.c1813 = Constraint(expr=m.x215**2 + m.x216**2 + m.x219**2 + m.x220**2 - 2*m.x215*m.x219 - 2*m.x216*m.x220
                           - 1.436939228176*m.b67 - 1.436939228176*m.b85 >= -1.436939228176)

m.c1814 = Constraint(expr=m.x215**2 + m.x216**2 + m.x221**2 + m.x222**2 - 2*m.x216*m.x222 - 2*m.x215*m.x221
                           - 1.436939228176*m.b67 - 1.436939228176*m.b94 >= -1.436939228176)

m.c1815 = Constraint(expr=m.x215**2 + m.x216**2 + m.x223**2 + m.x224**2 - 2*m.x216*m.x224 - 2*m.x215*m.x223
                           - 1.436939228176*m.b67 - 1.436939228176*m.b103 >= -1.436939228176)

m.c1816 = Constraint(expr=m.x215**2 + m.x216**2 + m.x225**2 + m.x226**2 - 2*m.x215*m.x225 - 2*m.x216*m.x226
                           - 1.436939228176*m.b67 - 1.436939228176*m.b112 >= -1.436939228176)

m.c1817 = Constraint(expr=m.x215**2 + m.x216**2 + m.x227**2 + m.x228**2 - 2*m.x216*m.x228 - 2*m.x215*m.x227
                           - 0.887203867225*m.b67 - 0.887203867225*m.b127 >= -0.887203867225)

m.c1818 = Constraint(expr=m.x215**2 + m.x216**2 + m.x229**2 + m.x230**2 - 2*m.x215*m.x229 - 2*m.x216*m.x230
                           - 0.887203867225*m.b67 - 0.887203867225*m.b142 >= -0.887203867225)

m.c1819 = Constraint(expr=m.x215**2 + m.x216**2 + m.x231**2 + m.x232**2 - 2*m.x216*m.x232 - 2*m.x215*m.x231
                           - 0.887203867225*m.b67 - 0.887203867225*m.b157 >= -0.887203867225)

m.c1820 = Constraint(expr=m.x215**2 + m.x216**2 + m.x233**2 + m.x234**2 - 2*m.x216*m.x234 - 2*m.x215*m.x233
                           - 0.887203867225*m.b67 - 0.887203867225*m.b172 >= -0.887203867225)

m.c1821 = Constraint(expr=m.x215**2 + m.x216**2 + m.x235**2 + m.x236**2 - 2*m.x216*m.x236 - 2*m.x215*m.x235
                           - 0.887203867225*m.b67 - 0.887203867225*m.b187 >= -0.887203867225)

m.c1822 = Constraint(expr=m.x215**2 + m.x216**2 + m.x237**2 + m.x238**2 - 2*m.x216*m.x238 - 2*m.x215*m.x237
                           - 2.118573403024*m.b67 - 2.118573403024*m.b191 >= -2.118573403024)

m.c1823 = Constraint(expr=m.x215**2 + m.x216**2 + m.x239**2 + m.x240**2 - 2*m.x215*m.x239 - 2*m.x216*m.x240
                           - 2.118573403024*m.b67 - 2.118573403024*m.b195 >= -2.118573403024)

m.c1824 = Constraint(expr=m.x215**2 + m.x216**2 + m.x241**2 + m.x242**2 - 2*m.x215*m.x241 - 2*m.x216*m.x242
                           - 2.118573403024*m.b67 - 2.118573403024*m.b199 >= -2.118573403024)

m.c1825 = Constraint(expr=m.x215**2 + m.x216**2 + m.x243**2 + m.x244**2 - 2*m.x215*m.x243 - 2*m.x216*m.x244
                           - 2.118573403024*m.b67 - 2.118573403024*m.b203 >= -2.118573403024)

m.c1826 = Constraint(expr=m.x215**2 + m.x216**2 + m.x245**2 + m.x246**2 - 2*m.x215*m.x245 - 2*m.x216*m.x246
                           - 2.118573403024*m.b67 - 2.118573403024*m.b207 >= -2.118573403024)

m.c1827 = Constraint(expr=m.x215**2 + m.x216**2 + m.x217**2 + m.x218**2 - 2*m.x215*m.x217 - 2*m.x216*m.x218
                           - 1.436939228176*m.b67 - 1.436939228176*m.b76 >= -1.436939228176)

m.c1828 = Constraint(expr=m.x217**2 + m.x218**2 + m.x219**2 + m.x220**2 - 2*m.x217*m.x219 - 2*m.x218*m.x220
                           - 1.436939228176*m.b76 - 1.436939228176*m.b85 >= -1.436939228176)

m.c1829 = Constraint(expr=m.x217**2 + m.x218**2 + m.x221**2 + m.x222**2 - 2*m.x218*m.x222 - 2*m.x217*m.x221
                           - 1.436939228176*m.b76 - 1.436939228176*m.b94 >= -1.436939228176)

m.c1830 = Constraint(expr=m.x217**2 + m.x218**2 + m.x223**2 + m.x224**2 - 2*m.x217*m.x223 - 2*m.x218*m.x224
                           - 1.436939228176*m.b76 - 1.436939228176*m.b103 >= -1.436939228176)

m.c1831 = Constraint(expr=m.x217**2 + m.x218**2 + m.x225**2 + m.x226**2 - 2*m.x218*m.x226 - 2*m.x217*m.x225
                           - 1.436939228176*m.b76 - 1.436939228176*m.b112 >= -1.436939228176)

m.c1832 = Constraint(expr=m.x217**2 + m.x218**2 + m.x227**2 + m.x228**2 - 2*m.x217*m.x227 - 2*m.x218*m.x228
                           - 0.887203867225*m.b76 - 0.887203867225*m.b127 >= -0.887203867225)

m.c1833 = Constraint(expr=m.x217**2 + m.x218**2 + m.x229**2 + m.x230**2 - 2*m.x218*m.x230 - 2*m.x217*m.x229
                           - 0.887203867225*m.b76 - 0.887203867225*m.b142 >= -0.887203867225)

m.c1834 = Constraint(expr=m.x217**2 + m.x218**2 + m.x231**2 + m.x232**2 - 2*m.x218*m.x232 - 2*m.x217*m.x231
                           - 0.887203867225*m.b76 - 0.887203867225*m.b157 >= -0.887203867225)

m.c1835 = Constraint(expr=m.x217**2 + m.x218**2 + m.x233**2 + m.x234**2 - 2*m.x217*m.x233 - 2*m.x218*m.x234
                           - 0.887203867225*m.b76 - 0.887203867225*m.b172 >= -0.887203867225)

m.c1836 = Constraint(expr=m.x217**2 + m.x218**2 + m.x235**2 + m.x236**2 - 2*m.x217*m.x235 - 2*m.x218*m.x236
                           - 0.887203867225*m.b76 - 0.887203867225*m.b187 >= -0.887203867225)

m.c1837 = Constraint(expr=m.x217**2 + m.x218**2 + m.x237**2 + m.x238**2 - 2*m.x218*m.x238 - 2*m.x217*m.x237
                           - 2.118573403024*m.b76 - 2.118573403024*m.b191 >= -2.118573403024)

m.c1838 = Constraint(expr=m.x217**2 + m.x218**2 + m.x239**2 + m.x240**2 - 2*m.x218*m.x240 - 2*m.x217*m.x239
                           - 2.118573403024*m.b76 - 2.118573403024*m.b195 >= -2.118573403024)

m.c1839 = Constraint(expr=m.x217**2 + m.x218**2 + m.x241**2 + m.x242**2 - 2*m.x217*m.x241 - 2*m.x218*m.x242
                           - 2.118573403024*m.b76 - 2.118573403024*m.b199 >= -2.118573403024)

m.c1840 = Constraint(expr=m.x217**2 + m.x218**2 + m.x243**2 + m.x244**2 - 2*m.x217*m.x243 - 2*m.x218*m.x244
                           - 2.118573403024*m.b76 - 2.118573403024*m.b203 >= -2.118573403024)

m.c1841 = Constraint(expr=m.x217**2 + m.x218**2 + m.x245**2 + m.x246**2 - 2*m.x217*m.x245 - 2*m.x218*m.x246
                           - 2.118573403024*m.b76 - 2.118573403024*m.b207 >= -2.118573403024)

m.c1842 = Constraint(expr=m.x215**2 + m.x216**2 + m.x219**2 + m.x220**2 - 2*m.x215*m.x219 - 2*m.x216*m.x220
                           - 1.436939228176*m.b67 - 1.436939228176*m.b85 >= -1.436939228176)

m.c1843 = Constraint(expr=m.x217**2 + m.x218**2 + m.x219**2 + m.x220**2 - 2*m.x217*m.x219 - 2*m.x218*m.x220
                           - 1.436939228176*m.b76 - 1.436939228176*m.b85 >= -1.436939228176)

m.c1844 = Constraint(expr=m.x219**2 + m.x220**2 + m.x221**2 + m.x222**2 - 2*m.x219*m.x221 - 2*m.x220*m.x222
                           - 1.436939228176*m.b85 - 1.436939228176*m.b94 >= -1.436939228176)

m.c1845 = Constraint(expr=m.x219**2 + m.x220**2 + m.x223**2 + m.x224**2 - 2*m.x220*m.x224 - 2*m.x219*m.x223
                           - 1.436939228176*m.b85 - 1.436939228176*m.b103 >= -1.436939228176)

m.c1846 = Constraint(expr=m.x219**2 + m.x220**2 + m.x225**2 + m.x226**2 - 2*m.x220*m.x226 - 2*m.x219*m.x225
                           - 1.436939228176*m.b85 - 1.436939228176*m.b112 >= -1.436939228176)

m.c1847 = Constraint(expr=m.x219**2 + m.x220**2 + m.x227**2 + m.x228**2 - 2*m.x219*m.x227 - 2*m.x220*m.x228
                           - 0.887203867225*m.b85 - 0.887203867225*m.b127 >= -0.887203867225)

m.c1848 = Constraint(expr=m.x219**2 + m.x220**2 + m.x229**2 + m.x230**2 - 2*m.x220*m.x230 - 2*m.x219*m.x229
                           - 0.887203867225*m.b85 - 0.887203867225*m.b142 >= -0.887203867225)

m.c1849 = Constraint(expr=m.x219**2 + m.x220**2 + m.x231**2 + m.x232**2 - 2*m.x219*m.x231 - 2*m.x220*m.x232
                           - 0.887203867225*m.b85 - 0.887203867225*m.b157 >= -0.887203867225)

m.c1850 = Constraint(expr=m.x219**2 + m.x220**2 + m.x233**2 + m.x234**2 - 2*m.x220*m.x234 - 2*m.x219*m.x233
                           - 0.887203867225*m.b85 - 0.887203867225*m.b172 >= -0.887203867225)

m.c1851 = Constraint(expr=m.x219**2 + m.x220**2 + m.x235**2 + m.x236**2 - 2*m.x219*m.x235 - 2*m.x220*m.x236
                           - 0.887203867225*m.b85 - 0.887203867225*m.b187 >= -0.887203867225)

m.c1852 = Constraint(expr=m.x219**2 + m.x220**2 + m.x237**2 + m.x238**2 - 2*m.x220*m.x238 - 2*m.x219*m.x237
                           - 2.118573403024*m.b85 - 2.118573403024*m.b191 >= -2.118573403024)

m.c1853 = Constraint(expr=m.x219**2 + m.x220**2 + m.x239**2 + m.x240**2 - 2*m.x220*m.x240 - 2*m.x219*m.x239
                           - 2.118573403024*m.b85 - 2.118573403024*m.b195 >= -2.118573403024)

m.c1854 = Constraint(expr=m.x219**2 + m.x220**2 + m.x241**2 + m.x242**2 - 2*m.x219*m.x241 - 2*m.x220*m.x242
                           - 2.118573403024*m.b85 - 2.118573403024*m.b199 >= -2.118573403024)

m.c1855 = Constraint(expr=m.x219**2 + m.x220**2 + m.x243**2 + m.x244**2 - 2*m.x219*m.x243 - 2*m.x220*m.x244
                           - 2.118573403024*m.b85 - 2.118573403024*m.b203 >= -2.118573403024)

m.c1856 = Constraint(expr=m.x219**2 + m.x220**2 + m.x245**2 + m.x246**2 - 2*m.x219*m.x245 - 2*m.x220*m.x246
                           - 2.118573403024*m.b85 - 2.118573403024*m.b207 >= -2.118573403024)

m.c1857 = Constraint(expr=m.x215**2 + m.x216**2 + m.x221**2 + m.x222**2 - 2*m.x216*m.x222 - 2*m.x215*m.x221
                           - 1.436939228176*m.b67 - 1.436939228176*m.b94 >= -1.436939228176)

m.c1858 = Constraint(expr=m.x217**2 + m.x218**2 + m.x221**2 + m.x222**2 - 2*m.x218*m.x222 - 2*m.x217*m.x221
                           - 1.436939228176*m.b76 - 1.436939228176*m.b94 >= -1.436939228176)

m.c1859 = Constraint(expr=m.x219**2 + m.x220**2 + m.x221**2 + m.x222**2 - 2*m.x219*m.x221 - 2*m.x220*m.x222
                           - 1.436939228176*m.b85 - 1.436939228176*m.b94 >= -1.436939228176)

m.c1860 = Constraint(expr=m.x221**2 + m.x222**2 + m.x223**2 + m.x224**2 - 2*m.x221*m.x223 - 2*m.x222*m.x224
                           - 1.436939228176*m.b94 - 1.436939228176*m.b103 >= -1.436939228176)

m.c1861 = Constraint(expr=m.x221**2 + m.x222**2 + m.x225**2 + m.x226**2 - 2*m.x221*m.x225 - 2*m.x222*m.x226
                           - 1.436939228176*m.b94 - 1.436939228176*m.b112 >= -1.436939228176)

m.c1862 = Constraint(expr=m.x221**2 + m.x222**2 + m.x227**2 + m.x228**2 - 2*m.x221*m.x227 - 2*m.x222*m.x228
                           - 0.887203867225*m.b94 - 0.887203867225*m.b127 >= -0.887203867225)

m.c1863 = Constraint(expr=m.x221**2 + m.x222**2 + m.x229**2 + m.x230**2 - 2*m.x221*m.x229 - 2*m.x222*m.x230
                           - 0.887203867225*m.b94 - 0.887203867225*m.b142 >= -0.887203867225)

m.c1864 = Constraint(expr=m.x221**2 + m.x222**2 + m.x231**2 + m.x232**2 - 2*m.x221*m.x231 - 2*m.x222*m.x232
                           - 0.887203867225*m.b94 - 0.887203867225*m.b157 >= -0.887203867225)

m.c1865 = Constraint(expr=m.x221**2 + m.x222**2 + m.x233**2 + m.x234**2 - 2*m.x221*m.x233 - 2*m.x222*m.x234
                           - 0.887203867225*m.b94 - 0.887203867225*m.b172 >= -0.887203867225)

m.c1866 = Constraint(expr=m.x221**2 + m.x222**2 + m.x235**2 + m.x236**2 - 2*m.x221*m.x235 - 2*m.x222*m.x236
                           - 0.887203867225*m.b94 - 0.887203867225*m.b187 >= -0.887203867225)

m.c1867 = Constraint(expr=m.x221**2 + m.x222**2 + m.x237**2 + m.x238**2 - 2*m.x221*m.x237 - 2*m.x222*m.x238
                           - 2.118573403024*m.b94 - 2.118573403024*m.b191 >= -2.118573403024)

m.c1868 = Constraint(expr=m.x221**2 + m.x222**2 + m.x239**2 + m.x240**2 - 2*m.x221*m.x239 - 2*m.x222*m.x240
                           - 2.118573403024*m.b94 - 2.118573403024*m.b195 >= -2.118573403024)

m.c1869 = Constraint(expr=m.x221**2 + m.x222**2 + m.x241**2 + m.x242**2 - 2*m.x221*m.x241 - 2*m.x222*m.x242
                           - 2.118573403024*m.b94 - 2.118573403024*m.b199 >= -2.118573403024)

m.c1870 = Constraint(expr=m.x221**2 + m.x222**2 + m.x243**2 + m.x244**2 - 2*m.x221*m.x243 - 2*m.x222*m.x244
                           - 2.118573403024*m.b94 - 2.118573403024*m.b203 >= -2.118573403024)

m.c1871 = Constraint(expr=m.x221**2 + m.x222**2 + m.x245**2 + m.x246**2 - 2*m.x222*m.x246 - 2*m.x221*m.x245
                           - 2.118573403024*m.b94 - 2.118573403024*m.b207 >= -2.118573403024)

m.c1872 = Constraint(expr=m.x215**2 + m.x216**2 + m.x223**2 + m.x224**2 - 2*m.x216*m.x224 - 2*m.x215*m.x223
                           - 1.436939228176*m.b67 - 1.436939228176*m.b103 >= -1.436939228176)

m.c1873 = Constraint(expr=m.x217**2 + m.x218**2 + m.x223**2 + m.x224**2 - 2*m.x217*m.x223 - 2*m.x218*m.x224
                           - 1.436939228176*m.b76 - 1.436939228176*m.b103 >= -1.436939228176)

m.c1874 = Constraint(expr=m.x219**2 + m.x220**2 + m.x223**2 + m.x224**2 - 2*m.x220*m.x224 - 2*m.x219*m.x223
                           - 1.436939228176*m.b85 - 1.436939228176*m.b103 >= -1.436939228176)

m.c1875 = Constraint(expr=m.x221**2 + m.x222**2 + m.x223**2 + m.x224**2 - 2*m.x221*m.x223 - 2*m.x222*m.x224
                           - 1.436939228176*m.b94 - 1.436939228176*m.b103 >= -1.436939228176)

m.c1876 = Constraint(expr=m.x223**2 + m.x224**2 + m.x225**2 + m.x226**2 - 2*m.x223*m.x225 - 2*m.x224*m.x226
                           - 1.436939228176*m.b103 - 1.436939228176*m.b112 >= -1.436939228176)

m.c1877 = Constraint(expr=m.x223**2 + m.x224**2 + m.x227**2 + m.x228**2 - 2*m.x223*m.x227 - 2*m.x224*m.x228
                           - 0.887203867225*m.b103 - 0.887203867225*m.b127 >= -0.887203867225)

m.c1878 = Constraint(expr=m.x223**2 + m.x224**2 + m.x229**2 + m.x230**2 - 2*m.x223*m.x229 - 2*m.x224*m.x230
                           - 0.887203867225*m.b103 - 0.887203867225*m.b142 >= -0.887203867225)

m.c1879 = Constraint(expr=m.x223**2 + m.x224**2 + m.x231**2 + m.x232**2 - 2*m.x223*m.x231 - 2*m.x224*m.x232
                           - 0.887203867225*m.b103 - 0.887203867225*m.b157 >= -0.887203867225)

m.c1880 = Constraint(expr=m.x223**2 + m.x224**2 + m.x233**2 + m.x234**2 - 2*m.x223*m.x233 - 2*m.x224*m.x234
                           - 0.887203867225*m.b103 - 0.887203867225*m.b172 >= -0.887203867225)

m.c1881 = Constraint(expr=m.x223**2 + m.x224**2 + m.x235**2 + m.x236**2 - 2*m.x223*m.x235 - 2*m.x224*m.x236
                           - 0.887203867225*m.b103 - 0.887203867225*m.b187 >= -0.887203867225)

m.c1882 = Constraint(expr=m.x223**2 + m.x224**2 + m.x237**2 + m.x238**2 - 2*m.x223*m.x237 - 2*m.x224*m.x238
                           - 2.118573403024*m.b103 - 2.118573403024*m.b191 >= -2.118573403024)

m.c1883 = Constraint(expr=m.x223**2 + m.x224**2 + m.x239**2 + m.x240**2 - 2*m.x223*m.x239 - 2*m.x224*m.x240
                           - 2.118573403024*m.b103 - 2.118573403024*m.b195 >= -2.118573403024)

m.c1884 = Constraint(expr=m.x223**2 + m.x224**2 + m.x241**2 + m.x242**2 - 2*m.x223*m.x241 - 2*m.x224*m.x242
                           - 2.118573403024*m.b103 - 2.118573403024*m.b199 >= -2.118573403024)

m.c1885 = Constraint(expr=m.x223**2 + m.x224**2 + m.x243**2 + m.x244**2 - 2*m.x224*m.x244 - 2*m.x223*m.x243
                           - 2.118573403024*m.b103 - 2.118573403024*m.b203 >= -2.118573403024)

m.c1886 = Constraint(expr=m.x223**2 + m.x224**2 + m.x245**2 + m.x246**2 - 2*m.x224*m.x246 - 2*m.x223*m.x245
                           - 2.118573403024*m.b103 - 2.118573403024*m.b207 >= -2.118573403024)

m.c1887 = Constraint(expr=m.x215**2 + m.x216**2 + m.x225**2 + m.x226**2 - 2*m.x215*m.x225 - 2*m.x216*m.x226
                           - 1.436939228176*m.b67 - 1.436939228176*m.b112 >= -1.436939228176)

m.c1888 = Constraint(expr=m.x217**2 + m.x218**2 + m.x225**2 + m.x226**2 - 2*m.x218*m.x226 - 2*m.x217*m.x225
                           - 1.436939228176*m.b76 - 1.436939228176*m.b112 >= -1.436939228176)

m.c1889 = Constraint(expr=m.x219**2 + m.x220**2 + m.x225**2 + m.x226**2 - 2*m.x220*m.x226 - 2*m.x219*m.x225
                           - 1.436939228176*m.b85 - 1.436939228176*m.b112 >= -1.436939228176)

m.c1890 = Constraint(expr=m.x221**2 + m.x222**2 + m.x225**2 + m.x226**2 - 2*m.x221*m.x225 - 2*m.x222*m.x226
                           - 1.436939228176*m.b94 - 1.436939228176*m.b112 >= -1.436939228176)

m.c1891 = Constraint(expr=m.x223**2 + m.x224**2 + m.x225**2 + m.x226**2 - 2*m.x223*m.x225 - 2*m.x224*m.x226
                           - 1.436939228176*m.b103 - 1.436939228176*m.b112 >= -1.436939228176)

m.c1892 = Constraint(expr=m.x225**2 + m.x226**2 + m.x227**2 + m.x228**2 - 2*m.x225*m.x227 - 2*m.x226*m.x228
                           - 0.887203867225*m.b112 - 0.887203867225*m.b127 >= -0.887203867225)

m.c1893 = Constraint(expr=m.x225**2 + m.x226**2 + m.x229**2 + m.x230**2 - 2*m.x225*m.x229 - 2*m.x226*m.x230
                           - 0.887203867225*m.b112 - 0.887203867225*m.b142 >= -0.887203867225)

m.c1894 = Constraint(expr=m.x225**2 + m.x226**2 + m.x231**2 + m.x232**2 - 2*m.x225*m.x231 - 2*m.x226*m.x232
                           - 0.887203867225*m.b112 - 0.887203867225*m.b157 >= -0.887203867225)

m.c1895 = Constraint(expr=m.x225**2 + m.x226**2 + m.x233**2 + m.x234**2 - 2*m.x225*m.x233 - 2*m.x226*m.x234
                           - 0.887203867225*m.b112 - 0.887203867225*m.b172 >= -0.887203867225)

m.c1896 = Constraint(expr=m.x225**2 + m.x226**2 + m.x235**2 + m.x236**2 - 2*m.x225*m.x235 - 2*m.x226*m.x236
                           - 0.887203867225*m.b112 - 0.887203867225*m.b187 >= -0.887203867225)

m.c1897 = Constraint(expr=m.x225**2 + m.x226**2 + m.x237**2 + m.x238**2 - 2*m.x225*m.x237 - 2*m.x226*m.x238
                           - 2.118573403024*m.b112 - 2.118573403024*m.b191 >= -2.118573403024)

m.c1898 = Constraint(expr=m.x225**2 + m.x226**2 + m.x239**2 + m.x240**2 - 2*m.x225*m.x239 - 2*m.x226*m.x240
                           - 2.118573403024*m.b112 - 2.118573403024*m.b195 >= -2.118573403024)

m.c1899 = Constraint(expr=m.x225**2 + m.x226**2 + m.x241**2 + m.x242**2 - 2*m.x226*m.x242 - 2*m.x225*m.x241
                           - 2.118573403024*m.b112 - 2.118573403024*m.b199 >= -2.118573403024)

m.c1900 = Constraint(expr=m.x225**2 + m.x226**2 + m.x243**2 + m.x244**2 - 2*m.x226*m.x244 - 2*m.x225*m.x243
                           - 2.118573403024*m.b112 - 2.118573403024*m.b203 >= -2.118573403024)

m.c1901 = Constraint(expr=m.x225**2 + m.x226**2 + m.x245**2 + m.x246**2 - 2*m.x225*m.x245 - 2*m.x226*m.x246
                           - 2.118573403024*m.b112 - 2.118573403024*m.b207 >= -2.118573403024)

m.c1902 = Constraint(expr=m.x215**2 + m.x216**2 + m.x227**2 + m.x228**2 - 2*m.x216*m.x228 - 2*m.x215*m.x227
                           - 0.887203867225*m.b67 - 0.887203867225*m.b127 >= -0.887203867225)

m.c1903 = Constraint(expr=m.x217**2 + m.x218**2 + m.x227**2 + m.x228**2 - 2*m.x217*m.x227 - 2*m.x218*m.x228
                           - 0.887203867225*m.b76 - 0.887203867225*m.b127 >= -0.887203867225)

m.c1904 = Constraint(expr=m.x219**2 + m.x220**2 + m.x227**2 + m.x228**2 - 2*m.x219*m.x227 - 2*m.x220*m.x228
                           - 0.887203867225*m.b85 - 0.887203867225*m.b127 >= -0.887203867225)

m.c1905 = Constraint(expr=m.x221**2 + m.x222**2 + m.x227**2 + m.x228**2 - 2*m.x221*m.x227 - 2*m.x222*m.x228
                           - 0.887203867225*m.b94 - 0.887203867225*m.b127 >= -0.887203867225)

m.c1906 = Constraint(expr=m.x223**2 + m.x224**2 + m.x227**2 + m.x228**2 - 2*m.x223*m.x227 - 2*m.x224*m.x228
                           - 0.887203867225*m.b103 - 0.887203867225*m.b127 >= -0.887203867225)

m.c1907 = Constraint(expr=m.x225**2 + m.x226**2 + m.x227**2 + m.x228**2 - 2*m.x225*m.x227 - 2*m.x226*m.x228
                           - 0.887203867225*m.b112 - 0.887203867225*m.b127 >= -0.887203867225)

m.c1908 = Constraint(expr=m.x227**2 + m.x228**2 + m.x229**2 + m.x230**2 - 2*m.x227*m.x229 - 2*m.x228*m.x230
                           - 0.469370231236*m.b127 - 0.469370231236*m.b142 >= -0.469370231236)

m.c1909 = Constraint(expr=m.x227**2 + m.x228**2 + m.x231**2 + m.x232**2 - 2*m.x227*m.x231 - 2*m.x228*m.x232
                           - 0.469370231236*m.b127 - 0.469370231236*m.b157 >= -0.469370231236)

m.c1910 = Constraint(expr=m.x227**2 + m.x228**2 + m.x233**2 + m.x234**2 - 2*m.x227*m.x233 - 2*m.x228*m.x234
                           - 0.469370231236*m.b127 - 0.469370231236*m.b172 >= -0.469370231236)

m.c1911 = Constraint(expr=m.x227**2 + m.x228**2 + m.x235**2 + m.x236**2 - 2*m.x227*m.x235 - 2*m.x228*m.x236
                           - 0.469370231236*m.b127 - 0.469370231236*m.b187 >= -0.469370231236)

m.c1912 = Constraint(expr=m.x227**2 + m.x228**2 + m.x237**2 + m.x238**2 - 2*m.x227*m.x237 - 2*m.x228*m.x238
                           - 1.436936830729*m.b127 - 1.436936830729*m.b191 >= -1.436936830729)

m.c1913 = Constraint(expr=m.x227**2 + m.x228**2 + m.x239**2 + m.x240**2 - 2*m.x227*m.x239 - 2*m.x228*m.x240
                           - 1.436936830729*m.b127 - 1.436936830729*m.b195 >= -1.436936830729)

m.c1914 = Constraint(expr=m.x227**2 + m.x228**2 + m.x241**2 + m.x242**2 - 2*m.x227*m.x241 - 2*m.x228*m.x242
                           - 1.436936830729*m.b127 - 1.436936830729*m.b199 >= -1.436936830729)

m.c1915 = Constraint(expr=m.x227**2 + m.x228**2 + m.x243**2 + m.x244**2 - 2*m.x228*m.x244 - 2*m.x227*m.x243
                           - 1.436936830729*m.b127 - 1.436936830729*m.b203 >= -1.436936830729)

m.c1916 = Constraint(expr=m.x227**2 + m.x228**2 + m.x245**2 + m.x246**2 - 2*m.x228*m.x246 - 2*m.x227*m.x245
                           - 1.436936830729*m.b127 - 1.436936830729*m.b207 >= -1.436936830729)

m.c1917 = Constraint(expr=m.x215**2 + m.x216**2 + m.x229**2 + m.x230**2 - 2*m.x215*m.x229 - 2*m.x216*m.x230
                           - 0.887203867225*m.b67 - 0.887203867225*m.b142 >= -0.887203867225)

m.c1918 = Constraint(expr=m.x217**2 + m.x218**2 + m.x229**2 + m.x230**2 - 2*m.x218*m.x230 - 2*m.x217*m.x229
                           - 0.887203867225*m.b76 - 0.887203867225*m.b142 >= -0.887203867225)

m.c1919 = Constraint(expr=m.x219**2 + m.x220**2 + m.x229**2 + m.x230**2 - 2*m.x220*m.x230 - 2*m.x219*m.x229
                           - 0.887203867225*m.b85 - 0.887203867225*m.b142 >= -0.887203867225)

m.c1920 = Constraint(expr=m.x221**2 + m.x222**2 + m.x229**2 + m.x230**2 - 2*m.x221*m.x229 - 2*m.x222*m.x230
                           - 0.887203867225*m.b94 - 0.887203867225*m.b142 >= -0.887203867225)

m.c1921 = Constraint(expr=m.x223**2 + m.x224**2 + m.x229**2 + m.x230**2 - 2*m.x223*m.x229 - 2*m.x224*m.x230
                           - 0.887203867225*m.b103 - 0.887203867225*m.b142 >= -0.887203867225)

m.c1922 = Constraint(expr=m.x225**2 + m.x226**2 + m.x229**2 + m.x230**2 - 2*m.x225*m.x229 - 2*m.x226*m.x230
                           - 0.887203867225*m.b112 - 0.887203867225*m.b142 >= -0.887203867225)

m.c1923 = Constraint(expr=m.x227**2 + m.x228**2 + m.x229**2 + m.x230**2 - 2*m.x227*m.x229 - 2*m.x228*m.x230
                           - 0.469370231236*m.b127 - 0.469370231236*m.b142 >= -0.469370231236)

m.c1924 = Constraint(expr=m.x229**2 + m.x230**2 + m.x231**2 + m.x232**2 - 2*m.x229*m.x231 - 2*m.x230*m.x232
                           - 0.469370231236*m.b142 - 0.469370231236*m.b157 >= -0.469370231236)

m.c1925 = Constraint(expr=m.x229**2 + m.x230**2 + m.x233**2 + m.x234**2 - 2*m.x229*m.x233 - 2*m.x230*m.x234
                           - 0.469370231236*m.b142 - 0.469370231236*m.b172 >= -0.469370231236)

m.c1926 = Constraint(expr=m.x229**2 + m.x230**2 + m.x235**2 + m.x236**2 - 2*m.x229*m.x235 - 2*m.x230*m.x236
                           - 0.469370231236*m.b142 - 0.469370231236*m.b187 >= -0.469370231236)

m.c1927 = Constraint(expr=m.x229**2 + m.x230**2 + m.x237**2 + m.x238**2 - 2*m.x229*m.x237 - 2*m.x230*m.x238
                           - 1.436936830729*m.b142 - 1.436936830729*m.b191 >= -1.436936830729)

m.c1928 = Constraint(expr=m.x229**2 + m.x230**2 + m.x239**2 + m.x240**2 - 2*m.x229*m.x239 - 2*m.x230*m.x240
                           - 1.436936830729*m.b142 - 1.436936830729*m.b195 >= -1.436936830729)

m.c1929 = Constraint(expr=m.x229**2 + m.x230**2 + m.x241**2 + m.x242**2 - 2*m.x230*m.x242 - 2*m.x229*m.x241
                           - 1.436936830729*m.b142 - 1.436936830729*m.b199 >= -1.436936830729)

m.c1930 = Constraint(expr=m.x229**2 + m.x230**2 + m.x243**2 + m.x244**2 - 2*m.x230*m.x244 - 2*m.x229*m.x243
                           - 1.436936830729*m.b142 - 1.436936830729*m.b203 >= -1.436936830729)

m.c1931 = Constraint(expr=m.x229**2 + m.x230**2 + m.x245**2 + m.x246**2 - 2*m.x229*m.x245 - 2*m.x230*m.x246
                           - 1.436936830729*m.b142 - 1.436936830729*m.b207 >= -1.436936830729)

m.c1932 = Constraint(expr=m.x215**2 + m.x216**2 + m.x231**2 + m.x232**2 - 2*m.x216*m.x232 - 2*m.x215*m.x231
                           - 0.887203867225*m.b67 - 0.887203867225*m.b157 >= -0.887203867225)

m.c1933 = Constraint(expr=m.x217**2 + m.x218**2 + m.x231**2 + m.x232**2 - 2*m.x218*m.x232 - 2*m.x217*m.x231
                           - 0.887203867225*m.b76 - 0.887203867225*m.b157 >= -0.887203867225)

m.c1934 = Constraint(expr=m.x219**2 + m.x220**2 + m.x231**2 + m.x232**2 - 2*m.x219*m.x231 - 2*m.x220*m.x232
                           - 0.887203867225*m.b85 - 0.887203867225*m.b157 >= -0.887203867225)

m.c1935 = Constraint(expr=m.x221**2 + m.x222**2 + m.x231**2 + m.x232**2 - 2*m.x221*m.x231 - 2*m.x222*m.x232
                           - 0.887203867225*m.b94 - 0.887203867225*m.b157 >= -0.887203867225)

m.c1936 = Constraint(expr=m.x223**2 + m.x224**2 + m.x231**2 + m.x232**2 - 2*m.x223*m.x231 - 2*m.x224*m.x232
                           - 0.887203867225*m.b103 - 0.887203867225*m.b157 >= -0.887203867225)

m.c1937 = Constraint(expr=m.x225**2 + m.x226**2 + m.x231**2 + m.x232**2 - 2*m.x225*m.x231 - 2*m.x226*m.x232
                           - 0.887203867225*m.b112 - 0.887203867225*m.b157 >= -0.887203867225)

m.c1938 = Constraint(expr=m.x227**2 + m.x228**2 + m.x231**2 + m.x232**2 - 2*m.x227*m.x231 - 2*m.x228*m.x232
                           - 0.469370231236*m.b127 - 0.469370231236*m.b157 >= -0.469370231236)

m.c1939 = Constraint(expr=m.x229**2 + m.x230**2 + m.x231**2 + m.x232**2 - 2*m.x229*m.x231 - 2*m.x230*m.x232
                           - 0.469370231236*m.b142 - 0.469370231236*m.b157 >= -0.469370231236)

m.c1940 = Constraint(expr=m.x231**2 + m.x232**2 + m.x233**2 + m.x234**2 - 2*m.x231*m.x233 - 2*m.x232*m.x234
                           - 0.469370231236*m.b157 - 0.469370231236*m.b172 >= -0.469370231236)

m.c1941 = Constraint(expr=m.x231**2 + m.x232**2 + m.x235**2 + m.x236**2 - 2*m.x231*m.x235 - 2*m.x232*m.x236
                           - 0.469370231236*m.b157 - 0.469370231236*m.b187 >= -0.469370231236)

m.c1942 = Constraint(expr=m.x231**2 + m.x232**2 + m.x237**2 + m.x238**2 - 2*m.x231*m.x237 - 2*m.x232*m.x238
                           - 1.436936830729*m.b157 - 1.436936830729*m.b191 >= -1.436936830729)

m.c1943 = Constraint(expr=m.x231**2 + m.x232**2 + m.x239**2 + m.x240**2 - 2*m.x231*m.x239 - 2*m.x232*m.x240
                           - 1.436936830729*m.b157 - 1.436936830729*m.b195 >= -1.436936830729)

m.c1944 = Constraint(expr=m.x231**2 + m.x232**2 + m.x241**2 + m.x242**2 - 2*m.x232*m.x242 - 2*m.x231*m.x241
                           - 1.436936830729*m.b157 - 1.436936830729*m.b199 >= -1.436936830729)

m.c1945 = Constraint(expr=m.x231**2 + m.x232**2 + m.x243**2 + m.x244**2 - 2*m.x231*m.x243 - 2*m.x232*m.x244
                           - 1.436936830729*m.b157 - 1.436936830729*m.b203 >= -1.436936830729)

m.c1946 = Constraint(expr=m.x231**2 + m.x232**2 + m.x245**2 + m.x246**2 - 2*m.x232*m.x246 - 2*m.x231*m.x245
                           - 1.436936830729*m.b157 - 1.436936830729*m.b207 >= -1.436936830729)

m.c1947 = Constraint(expr=m.x215**2 + m.x216**2 + m.x233**2 + m.x234**2 - 2*m.x216*m.x234 - 2*m.x215*m.x233
                           - 0.887203867225*m.b67 - 0.887203867225*m.b172 >= -0.887203867225)

m.c1948 = Constraint(expr=m.x217**2 + m.x218**2 + m.x233**2 + m.x234**2 - 2*m.x217*m.x233 - 2*m.x218*m.x234
                           - 0.887203867225*m.b76 - 0.887203867225*m.b172 >= -0.887203867225)

m.c1949 = Constraint(expr=m.x219**2 + m.x220**2 + m.x233**2 + m.x234**2 - 2*m.x220*m.x234 - 2*m.x219*m.x233
                           - 0.887203867225*m.b85 - 0.887203867225*m.b172 >= -0.887203867225)

m.c1950 = Constraint(expr=m.x221**2 + m.x222**2 + m.x233**2 + m.x234**2 - 2*m.x221*m.x233 - 2*m.x222*m.x234
                           - 0.887203867225*m.b94 - 0.887203867225*m.b172 >= -0.887203867225)

m.c1951 = Constraint(expr=m.x223**2 + m.x224**2 + m.x233**2 + m.x234**2 - 2*m.x223*m.x233 - 2*m.x224*m.x234
                           - 0.887203867225*m.b103 - 0.887203867225*m.b172 >= -0.887203867225)

m.c1952 = Constraint(expr=m.x225**2 + m.x226**2 + m.x233**2 + m.x234**2 - 2*m.x225*m.x233 - 2*m.x226*m.x234
                           - 0.887203867225*m.b112 - 0.887203867225*m.b172 >= -0.887203867225)

m.c1953 = Constraint(expr=m.x227**2 + m.x228**2 + m.x233**2 + m.x234**2 - 2*m.x227*m.x233 - 2*m.x228*m.x234
                           - 0.469370231236*m.b127 - 0.469370231236*m.b172 >= -0.469370231236)

m.c1954 = Constraint(expr=m.x229**2 + m.x230**2 + m.x233**2 + m.x234**2 - 2*m.x229*m.x233 - 2*m.x230*m.x234
                           - 0.469370231236*m.b142 - 0.469370231236*m.b172 >= -0.469370231236)

m.c1955 = Constraint(expr=m.x231**2 + m.x232**2 + m.x233**2 + m.x234**2 - 2*m.x231*m.x233 - 2*m.x232*m.x234
                           - 0.469370231236*m.b157 - 0.469370231236*m.b172 >= -0.469370231236)

m.c1956 = Constraint(expr=m.x233**2 + m.x234**2 + m.x235**2 + m.x236**2 - 2*m.x233*m.x235 - 2*m.x234*m.x236
                           - 0.469370231236*m.b172 - 0.469370231236*m.b187 >= -0.469370231236)

m.c1957 = Constraint(expr=m.x233**2 + m.x234**2 + m.x237**2 + m.x238**2 - 2*m.x233*m.x237 - 2*m.x234*m.x238
                           - 1.436936830729*m.b172 - 1.436936830729*m.b191 >= -1.436936830729)

m.c1958 = Constraint(expr=m.x233**2 + m.x234**2 + m.x239**2 + m.x240**2 - 2*m.x233*m.x239 - 2*m.x234*m.x240
                           - 1.436936830729*m.b172 - 1.436936830729*m.b195 >= -1.436936830729)

m.c1959 = Constraint(expr=m.x233**2 + m.x234**2 + m.x241**2 + m.x242**2 - 2*m.x233*m.x241 - 2*m.x234*m.x242
                           - 1.436936830729*m.b172 - 1.436936830729*m.b199 >= -1.436936830729)

m.c1960 = Constraint(expr=m.x233**2 + m.x234**2 + m.x243**2 + m.x244**2 - 2*m.x234*m.x244 - 2*m.x233*m.x243
                           - 1.436936830729*m.b172 - 1.436936830729*m.b203 >= -1.436936830729)

m.c1961 = Constraint(expr=m.x233**2 + m.x234**2 + m.x245**2 + m.x246**2 - 2*m.x234*m.x246 - 2*m.x233*m.x245
                           - 1.436936830729*m.b172 - 1.436936830729*m.b207 >= -1.436936830729)

m.c1962 = Constraint(expr=m.x215**2 + m.x216**2 + m.x235**2 + m.x236**2 - 2*m.x215*m.x235 - 2*m.x216*m.x236
                           - 0.887203867225*m.b67 - 0.887203867225*m.b187 >= -0.887203867225)

m.c1963 = Constraint(expr=m.x217**2 + m.x218**2 + m.x235**2 + m.x236**2 - 2*m.x217*m.x235 - 2*m.x218*m.x236
                           - 0.887203867225*m.b76 - 0.887203867225*m.b187 >= -0.887203867225)

m.c1964 = Constraint(expr=m.x219**2 + m.x220**2 + m.x235**2 + m.x236**2 - 2*m.x219*m.x235 - 2*m.x220*m.x236
                           - 0.887203867225*m.b85 - 0.887203867225*m.b187 >= -0.887203867225)

m.c1965 = Constraint(expr=m.x221**2 + m.x222**2 + m.x235**2 + m.x236**2 - 2*m.x221*m.x235 - 2*m.x222*m.x236
                           - 0.887203867225*m.b94 - 0.887203867225*m.b187 >= -0.887203867225)

m.c1966 = Constraint(expr=m.x223**2 + m.x224**2 + m.x235**2 + m.x236**2 - 2*m.x223*m.x235 - 2*m.x224*m.x236
                           - 0.887203867225*m.b103 - 0.887203867225*m.b187 >= -0.887203867225)

m.c1967 = Constraint(expr=m.x225**2 + m.x226**2 + m.x235**2 + m.x236**2 - 2*m.x225*m.x235 - 2*m.x226*m.x236
                           - 0.887203867225*m.b112 - 0.887203867225*m.b187 >= -0.887203867225)

m.c1968 = Constraint(expr=m.x227**2 + m.x228**2 + m.x235**2 + m.x236**2 - 2*m.x227*m.x235 - 2*m.x228*m.x236
                           - 0.469370231236*m.b127 - 0.469370231236*m.b187 >= -0.469370231236)

m.c1969 = Constraint(expr=m.x229**2 + m.x230**2 + m.x235**2 + m.x236**2 - 2*m.x229*m.x235 - 2*m.x230*m.x236
                           - 0.469370231236*m.b142 - 0.469370231236*m.b187 >= -0.469370231236)

m.c1970 = Constraint(expr=m.x231**2 + m.x232**2 + m.x235**2 + m.x236**2 - 2*m.x231*m.x235 - 2*m.x232*m.x236
                           - 0.469370231236*m.b157 - 0.469370231236*m.b187 >= -0.469370231236)

m.c1971 = Constraint(expr=m.x233**2 + m.x234**2 + m.x235**2 + m.x236**2 - 2*m.x233*m.x235 - 2*m.x234*m.x236
                           - 0.469370231236*m.b172 - 0.469370231236*m.b187 >= -0.469370231236)

m.c1972 = Constraint(expr=m.x235**2 + m.x236**2 + m.x237**2 + m.x238**2 - 2*m.x235*m.x237 - 2*m.x236*m.x238
                           - 1.436936830729*m.b187 - 1.436936830729*m.b191 >= -1.436936830729)

m.c1973 = Constraint(expr=m.x235**2 + m.x236**2 + m.x239**2 + m.x240**2 - 2*m.x235*m.x239 - 2*m.x236*m.x240
                           - 1.436936830729*m.b187 - 1.436936830729*m.b195 >= -1.436936830729)

m.c1974 = Constraint(expr=m.x235**2 + m.x236**2 + m.x241**2 + m.x242**2 - 2*m.x236*m.x242 - 2*m.x235*m.x241
                           - 1.436936830729*m.b187 - 1.436936830729*m.b199 >= -1.436936830729)

m.c1975 = Constraint(expr=m.x235**2 + m.x236**2 + m.x243**2 + m.x244**2 - 2*m.x235*m.x243 - 2*m.x236*m.x244
                           - 1.436936830729*m.b187 - 1.436936830729*m.b203 >= -1.436936830729)

m.c1976 = Constraint(expr=m.x235**2 + m.x236**2 + m.x245**2 + m.x246**2 - 2*m.x236*m.x246 - 2*m.x235*m.x245
                           - 1.436936830729*m.b187 - 1.436936830729*m.b207 >= -1.436936830729)

m.c1977 = Constraint(expr=m.x215**2 + m.x216**2 + m.x237**2 + m.x238**2 - 2*m.x216*m.x238 - 2*m.x215*m.x237
                           - 2.118573403024*m.b67 - 2.118573403024*m.b191 >= -2.118573403024)

m.c1978 = Constraint(expr=m.x217**2 + m.x218**2 + m.x237**2 + m.x238**2 - 2*m.x218*m.x238 - 2*m.x217*m.x237
                           - 2.118573403024*m.b76 - 2.118573403024*m.b191 >= -2.118573403024)

m.c1979 = Constraint(expr=m.x219**2 + m.x220**2 + m.x237**2 + m.x238**2 - 2*m.x220*m.x238 - 2*m.x219*m.x237
                           - 2.118573403024*m.b85 - 2.118573403024*m.b191 >= -2.118573403024)

m.c1980 = Constraint(expr=m.x221**2 + m.x222**2 + m.x237**2 + m.x238**2 - 2*m.x221*m.x237 - 2*m.x222*m.x238
                           - 2.118573403024*m.b94 - 2.118573403024*m.b191 >= -2.118573403024)

m.c1981 = Constraint(expr=m.x223**2 + m.x224**2 + m.x237**2 + m.x238**2 - 2*m.x223*m.x237 - 2*m.x224*m.x238
                           - 2.118573403024*m.b103 - 2.118573403024*m.b191 >= -2.118573403024)

m.c1982 = Constraint(expr=m.x225**2 + m.x226**2 + m.x237**2 + m.x238**2 - 2*m.x225*m.x237 - 2*m.x226*m.x238
                           - 2.118573403024*m.b112 - 2.118573403024*m.b191 >= -2.118573403024)

m.c1983 = Constraint(expr=m.x227**2 + m.x228**2 + m.x237**2 + m.x238**2 - 2*m.x227*m.x237 - 2*m.x228*m.x238
                           - 1.436936830729*m.b127 - 1.436936830729*m.b191 >= -1.436936830729)

m.c1984 = Constraint(expr=m.x229**2 + m.x230**2 + m.x237**2 + m.x238**2 - 2*m.x229*m.x237 - 2*m.x230*m.x238
                           - 1.436936830729*m.b142 - 1.436936830729*m.b191 >= -1.436936830729)

m.c1985 = Constraint(expr=m.x231**2 + m.x232**2 + m.x237**2 + m.x238**2 - 2*m.x231*m.x237 - 2*m.x232*m.x238
                           - 1.436936830729*m.b157 - 1.436936830729*m.b191 >= -1.436936830729)

m.c1986 = Constraint(expr=m.x233**2 + m.x234**2 + m.x237**2 + m.x238**2 - 2*m.x233*m.x237 - 2*m.x234*m.x238
                           - 1.436936830729*m.b172 - 1.436936830729*m.b191 >= -1.436936830729)

m.c1987 = Constraint(expr=m.x235**2 + m.x236**2 + m.x237**2 + m.x238**2 - 2*m.x235*m.x237 - 2*m.x236*m.x238
                           - 1.436936830729*m.b187 - 1.436936830729*m.b191 >= -1.436936830729)

m.c1988 = Constraint(expr=m.x237**2 + m.x238**2 + m.x239**2 + m.x240**2 - 2*m.x237*m.x239 - 2*m.x238*m.x240
                           - 2.9321082756*m.b191 - 2.9321082756*m.b195 >= -2.9321082756)

m.c1989 = Constraint(expr=m.x237**2 + m.x238**2 + m.x241**2 + m.x242**2 - 2*m.x237*m.x241 - 2*m.x238*m.x242
                           - 2.9321082756*m.b191 - 2.9321082756*m.b199 >= -2.9321082756)

m.c1990 = Constraint(expr=m.x237**2 + m.x238**2 + m.x243**2 + m.x244**2 - 2*m.x238*m.x244 - 2*m.x237*m.x243
                           - 2.9321082756*m.b191 - 2.9321082756*m.b203 >= -2.9321082756)

m.c1991 = Constraint(expr=m.x237**2 + m.x238**2 + m.x245**2 + m.x246**2 - 2*m.x238*m.x246 - 2*m.x237*m.x245
                           - 2.9321082756*m.b191 - 2.9321082756*m.b207 >= -2.9321082756)

m.c1992 = Constraint(expr=m.x215**2 + m.x216**2 + m.x239**2 + m.x240**2 - 2*m.x215*m.x239 - 2*m.x216*m.x240
                           - 2.118573403024*m.b67 - 2.118573403024*m.b195 >= -2.118573403024)

m.c1993 = Constraint(expr=m.x217**2 + m.x218**2 + m.x239**2 + m.x240**2 - 2*m.x218*m.x240 - 2*m.x217*m.x239
                           - 2.118573403024*m.b76 - 2.118573403024*m.b195 >= -2.118573403024)

m.c1994 = Constraint(expr=m.x219**2 + m.x220**2 + m.x239**2 + m.x240**2 - 2*m.x220*m.x240 - 2*m.x219*m.x239
                           - 2.118573403024*m.b85 - 2.118573403024*m.b195 >= -2.118573403024)

m.c1995 = Constraint(expr=m.x221**2 + m.x222**2 + m.x239**2 + m.x240**2 - 2*m.x221*m.x239 - 2*m.x222*m.x240
                           - 2.118573403024*m.b94 - 2.118573403024*m.b195 >= -2.118573403024)

m.c1996 = Constraint(expr=m.x223**2 + m.x224**2 + m.x239**2 + m.x240**2 - 2*m.x223*m.x239 - 2*m.x224*m.x240
                           - 2.118573403024*m.b103 - 2.118573403024*m.b195 >= -2.118573403024)

m.c1997 = Constraint(expr=m.x225**2 + m.x226**2 + m.x239**2 + m.x240**2 - 2*m.x225*m.x239 - 2*m.x226*m.x240
                           - 2.118573403024*m.b112 - 2.118573403024*m.b195 >= -2.118573403024)

m.c1998 = Constraint(expr=m.x227**2 + m.x228**2 + m.x239**2 + m.x240**2 - 2*m.x227*m.x239 - 2*m.x228*m.x240
                           - 1.436936830729*m.b127 - 1.436936830729*m.b195 >= -1.436936830729)

m.c1999 = Constraint(expr=m.x229**2 + m.x230**2 + m.x239**2 + m.x240**2 - 2*m.x229*m.x239 - 2*m.x230*m.x240
                           - 1.436936830729*m.b142 - 1.436936830729*m.b195 >= -1.436936830729)

m.c2000 = Constraint(expr=m.x231**2 + m.x232**2 + m.x239**2 + m.x240**2 - 2*m.x231*m.x239 - 2*m.x232*m.x240
                           - 1.436936830729*m.b157 - 1.436936830729*m.b195 >= -1.436936830729)

m.c2001 = Constraint(expr=m.x233**2 + m.x234**2 + m.x239**2 + m.x240**2 - 2*m.x233*m.x239 - 2*m.x234*m.x240
                           - 1.436936830729*m.b172 - 1.436936830729*m.b195 >= -1.436936830729)

m.c2002 = Constraint(expr=m.x235**2 + m.x236**2 + m.x239**2 + m.x240**2 - 2*m.x235*m.x239 - 2*m.x236*m.x240
                           - 1.436936830729*m.b187 - 1.436936830729*m.b195 >= -1.436936830729)

m.c2003 = Constraint(expr=m.x237**2 + m.x238**2 + m.x239**2 + m.x240**2 - 2*m.x237*m.x239 - 2*m.x238*m.x240
                           - 2.9321082756*m.b191 - 2.9321082756*m.b195 >= -2.9321082756)

m.c2004 = Constraint(expr=m.x239**2 + m.x240**2 + m.x241**2 + m.x242**2 - 2*m.x240*m.x242 - 2*m.x239*m.x241
                           - 2.9321082756*m.b195 - 2.9321082756*m.b199 >= -2.9321082756)

m.c2005 = Constraint(expr=m.x239**2 + m.x240**2 + m.x243**2 + m.x244**2 - 2*m.x240*m.x244 - 2*m.x239*m.x243
                           - 2.9321082756*m.b195 - 2.9321082756*m.b203 >= -2.9321082756)

m.c2006 = Constraint(expr=m.x239**2 + m.x240**2 + m.x245**2 + m.x246**2 - 2*m.x240*m.x246 - 2*m.x239*m.x245
                           - 2.9321082756*m.b195 - 2.9321082756*m.b207 >= -2.9321082756)

m.c2007 = Constraint(expr=m.x215**2 + m.x216**2 + m.x241**2 + m.x242**2 - 2*m.x215*m.x241 - 2*m.x216*m.x242
                           - 2.118573403024*m.b67 - 2.118573403024*m.b199 >= -2.118573403024)

m.c2008 = Constraint(expr=m.x217**2 + m.x218**2 + m.x241**2 + m.x242**2 - 2*m.x217*m.x241 - 2*m.x218*m.x242
                           - 2.118573403024*m.b76 - 2.118573403024*m.b199 >= -2.118573403024)

m.c2009 = Constraint(expr=m.x219**2 + m.x220**2 + m.x241**2 + m.x242**2 - 2*m.x219*m.x241 - 2*m.x220*m.x242
                           - 2.118573403024*m.b85 - 2.118573403024*m.b199 >= -2.118573403024)

m.c2010 = Constraint(expr=m.x221**2 + m.x222**2 + m.x241**2 + m.x242**2 - 2*m.x222*m.x242 - 2*m.x221*m.x241
                           - 2.118573403024*m.b94 - 2.118573403024*m.b199 >= -2.118573403024)

m.c2011 = Constraint(expr=m.x223**2 + m.x224**2 + m.x241**2 + m.x242**2 - 2*m.x223*m.x241 - 2*m.x224*m.x242
                           - 2.118573403024*m.b103 - 2.118573403024*m.b199 >= -2.118573403024)

m.c2012 = Constraint(expr=m.x225**2 + m.x226**2 + m.x241**2 + m.x242**2 - 2*m.x226*m.x242 - 2*m.x225*m.x241
                           - 2.118573403024*m.b112 - 2.118573403024*m.b199 >= -2.118573403024)

m.c2013 = Constraint(expr=m.x227**2 + m.x228**2 + m.x241**2 + m.x242**2 - 2*m.x227*m.x241 - 2*m.x228*m.x242
                           - 1.436936830729*m.b127 - 1.436936830729*m.b199 >= -1.436936830729)

m.c2014 = Constraint(expr=m.x229**2 + m.x230**2 + m.x241**2 + m.x242**2 - 2*m.x230*m.x242 - 2*m.x229*m.x241
                           - 1.436936830729*m.b142 - 1.436936830729*m.b199 >= -1.436936830729)

m.c2015 = Constraint(expr=m.x231**2 + m.x232**2 + m.x241**2 + m.x242**2 - 2*m.x232*m.x242 - 2*m.x231*m.x241
                           - 1.436936830729*m.b157 - 1.436936830729*m.b199 >= -1.436936830729)

m.c2016 = Constraint(expr=m.x233**2 + m.x234**2 + m.x241**2 + m.x242**2 - 2*m.x233*m.x241 - 2*m.x234*m.x242
                           - 1.436936830729*m.b172 - 1.436936830729*m.b199 >= -1.436936830729)

m.c2017 = Constraint(expr=m.x235**2 + m.x236**2 + m.x241**2 + m.x242**2 - 2*m.x236*m.x242 - 2*m.x235*m.x241
                           - 1.436936830729*m.b187 - 1.436936830729*m.b199 >= -1.436936830729)

m.c2018 = Constraint(expr=m.x237**2 + m.x238**2 + m.x241**2 + m.x242**2 - 2*m.x237*m.x241 - 2*m.x238*m.x242
                           - 2.9321082756*m.b191 - 2.9321082756*m.b199 >= -2.9321082756)

m.c2019 = Constraint(expr=m.x239**2 + m.x240**2 + m.x241**2 + m.x242**2 - 2*m.x240*m.x242 - 2*m.x239*m.x241
                           - 2.9321082756*m.b195 - 2.9321082756*m.b199 >= -2.9321082756)

m.c2020 = Constraint(expr=m.x241**2 + m.x242**2 + m.x243**2 + m.x244**2 - 2*m.x241*m.x243 - 2*m.x242*m.x244
                           - 2.9321082756*m.b199 - 2.9321082756*m.b203 >= -2.9321082756)

m.c2021 = Constraint(expr=m.x241**2 + m.x242**2 + m.x245**2 + m.x246**2 - 2*m.x241*m.x245 - 2*m.x242*m.x246
                           - 2.9321082756*m.b199 - 2.9321082756*m.b207 >= -2.9321082756)

m.c2022 = Constraint(expr=m.x215**2 + m.x216**2 + m.x243**2 + m.x244**2 - 2*m.x215*m.x243 - 2*m.x216*m.x244
                           - 2.118573403024*m.b67 - 2.118573403024*m.b203 >= -2.118573403024)

m.c2023 = Constraint(expr=m.x217**2 + m.x218**2 + m.x243**2 + m.x244**2 - 2*m.x217*m.x243 - 2*m.x218*m.x244
                           - 2.118573403024*m.b76 - 2.118573403024*m.b203 >= -2.118573403024)

m.c2024 = Constraint(expr=m.x219**2 + m.x220**2 + m.x243**2 + m.x244**2 - 2*m.x219*m.x243 - 2*m.x220*m.x244
                           - 2.118573403024*m.b85 - 2.118573403024*m.b203 >= -2.118573403024)

m.c2025 = Constraint(expr=m.x221**2 + m.x222**2 + m.x243**2 + m.x244**2 - 2*m.x222*m.x244 - 2*m.x221*m.x243
                           - 2.118573403024*m.b94 - 2.118573403024*m.b203 >= -2.118573403024)

m.c2026 = Constraint(expr=m.x223**2 + m.x224**2 + m.x243**2 + m.x244**2 - 2*m.x224*m.x244 - 2*m.x223*m.x243
                           - 2.118573403024*m.b103 - 2.118573403024*m.b203 >= -2.118573403024)

m.c2027 = Constraint(expr=m.x225**2 + m.x226**2 + m.x243**2 + m.x244**2 - 2*m.x225*m.x243 - 2*m.x226*m.x244
                           - 2.118573403024*m.b112 - 2.118573403024*m.b203 >= -2.118573403024)

m.c2028 = Constraint(expr=m.x227**2 + m.x228**2 + m.x243**2 + m.x244**2 - 2*m.x228*m.x244 - 2*m.x227*m.x243
                           - 1.436936830729*m.b127 - 1.436936830729*m.b203 >= -1.436936830729)

m.c2029 = Constraint(expr=m.x229**2 + m.x230**2 + m.x243**2 + m.x244**2 - 2*m.x229*m.x243 - 2*m.x230*m.x244
                           - 1.436936830729*m.b142 - 1.436936830729*m.b203 >= -1.436936830729)

m.c2030 = Constraint(expr=m.x231**2 + m.x232**2 + m.x243**2 + m.x244**2 - 2*m.x231*m.x243 - 2*m.x232*m.x244
                           - 1.436936830729*m.b157 - 1.436936830729*m.b203 >= -1.436936830729)

m.c2031 = Constraint(expr=m.x233**2 + m.x234**2 + m.x243**2 + m.x244**2 - 2*m.x234*m.x244 - 2*m.x233*m.x243
                           - 1.436936830729*m.b172 - 1.436936830729*m.b203 >= -1.436936830729)

m.c2032 = Constraint(expr=m.x235**2 + m.x236**2 + m.x243**2 + m.x244**2 - 2*m.x235*m.x243 - 2*m.x236*m.x244
                           - 1.436936830729*m.b187 - 1.436936830729*m.b203 >= -1.436936830729)

m.c2033 = Constraint(expr=m.x237**2 + m.x238**2 + m.x243**2 + m.x244**2 - 2*m.x238*m.x244 - 2*m.x237*m.x243
                           - 2.9321082756*m.b191 - 2.9321082756*m.b203 >= -2.9321082756)

m.c2034 = Constraint(expr=m.x239**2 + m.x240**2 + m.x243**2 + m.x244**2 - 2*m.x240*m.x244 - 2*m.x239*m.x243
                           - 2.9321082756*m.b195 - 2.9321082756*m.b203 >= -2.9321082756)

m.c2035 = Constraint(expr=m.x241**2 + m.x242**2 + m.x243**2 + m.x244**2 - 2*m.x241*m.x243 - 2*m.x242*m.x244
                           - 2.9321082756*m.b199 - 2.9321082756*m.b203 >= -2.9321082756)

m.c2036 = Constraint(expr=m.x243**2 + m.x244**2 + m.x245**2 + m.x246**2 - 2*m.x243*m.x245 - 2*m.x244*m.x246
                           - 2.9321082756*m.b203 - 2.9321082756*m.b207 >= -2.9321082756)

m.c2037 = Constraint(expr=m.x215**2 + m.x216**2 + m.x245**2 + m.x246**2 - 2*m.x215*m.x245 - 2*m.x216*m.x246
                           - 2.118573403024*m.b67 - 2.118573403024*m.b207 >= -2.118573403024)

m.c2038 = Constraint(expr=m.x217**2 + m.x218**2 + m.x245**2 + m.x246**2 - 2*m.x217*m.x245 - 2*m.x218*m.x246
                           - 2.118573403024*m.b76 - 2.118573403024*m.b207 >= -2.118573403024)

m.c2039 = Constraint(expr=m.x219**2 + m.x220**2 + m.x245**2 + m.x246**2 - 2*m.x219*m.x245 - 2*m.x220*m.x246
                           - 2.118573403024*m.b85 - 2.118573403024*m.b207 >= -2.118573403024)

m.c2040 = Constraint(expr=m.x221**2 + m.x222**2 + m.x245**2 + m.x246**2 - 2*m.x222*m.x246 - 2*m.x221*m.x245
                           - 2.118573403024*m.b94 - 2.118573403024*m.b207 >= -2.118573403024)

m.c2041 = Constraint(expr=m.x223**2 + m.x224**2 + m.x245**2 + m.x246**2 - 2*m.x224*m.x246 - 2*m.x223*m.x245
                           - 2.118573403024*m.b103 - 2.118573403024*m.b207 >= -2.118573403024)

m.c2042 = Constraint(expr=m.x225**2 + m.x226**2 + m.x245**2 + m.x246**2 - 2*m.x225*m.x245 - 2*m.x226*m.x246
                           - 2.118573403024*m.b112 - 2.118573403024*m.b207 >= -2.118573403024)

m.c2043 = Constraint(expr=m.x227**2 + m.x228**2 + m.x245**2 + m.x246**2 - 2*m.x228*m.x246 - 2*m.x227*m.x245
                           - 1.436936830729*m.b127 - 1.436936830729*m.b207 >= -1.436936830729)

m.c2044 = Constraint(expr=m.x229**2 + m.x230**2 + m.x245**2 + m.x246**2 - 2*m.x229*m.x245 - 2*m.x230*m.x246
                           - 1.436936830729*m.b142 - 1.436936830729*m.b207 >= -1.436936830729)

m.c2045 = Constraint(expr=m.x231**2 + m.x232**2 + m.x245**2 + m.x246**2 - 2*m.x232*m.x246 - 2*m.x231*m.x245
                           - 1.436936830729*m.b157 - 1.436936830729*m.b207 >= -1.436936830729)

m.c2046 = Constraint(expr=m.x233**2 + m.x234**2 + m.x245**2 + m.x246**2 - 2*m.x233*m.x245 - 2*m.x234*m.x246
                           - 1.436936830729*m.b172 - 1.436936830729*m.b207 >= -1.436936830729)

m.c2047 = Constraint(expr=m.x235**2 + m.x236**2 + m.x245**2 + m.x246**2 - 2*m.x236*m.x246 - 2*m.x235*m.x245
                           - 1.436936830729*m.b187 - 1.436936830729*m.b207 >= -1.436936830729)

m.c2048 = Constraint(expr=m.x237**2 + m.x238**2 + m.x245**2 + m.x246**2 - 2*m.x238*m.x246 - 2*m.x237*m.x245
                           - 2.9321082756*m.b191 - 2.9321082756*m.b207 >= -2.9321082756)

m.c2049 = Constraint(expr=m.x239**2 + m.x240**2 + m.x245**2 + m.x246**2 - 2*m.x239*m.x245 - 2*m.x240*m.x246
                           - 2.9321082756*m.b195 - 2.9321082756*m.b207 >= -2.9321082756)

m.c2050 = Constraint(expr=m.x241**2 + m.x242**2 + m.x245**2 + m.x246**2 - 2*m.x241*m.x245 - 2*m.x242*m.x246
                           - 2.9321082756*m.b199 - 2.9321082756*m.b207 >= -2.9321082756)

m.c2051 = Constraint(expr=m.x243**2 + m.x244**2 + m.x245**2 + m.x246**2 - 2*m.x243*m.x245 - 2*m.x244*m.x246
                           - 2.9321082756*m.b203 - 2.9321082756*m.b207 >= -2.9321082756)

m.c2052 = Constraint(expr=m.x215**2 + m.x216**2 + m.x217**2 + m.x218**2 - 2*m.x215*m.x217 - 2*m.x216*m.x218
                           - 1.436939228176*m.b68 - 1.436939228176*m.b77 >= -1.436939228176)

m.c2053 = Constraint(expr=m.x215**2 + m.x216**2 + m.x219**2 + m.x220**2 - 2*m.x215*m.x219 - 2*m.x216*m.x220
                           - 1.436939228176*m.b68 - 1.436939228176*m.b86 >= -1.436939228176)

m.c2054 = Constraint(expr=m.x215**2 + m.x216**2 + m.x221**2 + m.x222**2 - 2*m.x216*m.x222 - 2*m.x215*m.x221
                           - 1.436939228176*m.b68 - 1.436939228176*m.b95 >= -1.436939228176)

m.c2055 = Constraint(expr=m.x215**2 + m.x216**2 + m.x223**2 + m.x224**2 - 2*m.x216*m.x224 - 2*m.x215*m.x223
                           - 1.436939228176*m.b68 - 1.436939228176*m.b104 >= -1.436939228176)

m.c2056 = Constraint(expr=m.x215**2 + m.x216**2 + m.x225**2 + m.x226**2 - 2*m.x215*m.x225 - 2*m.x216*m.x226
                           - 1.436939228176*m.b68 - 1.436939228176*m.b113 >= -1.436939228176)

m.c2057 = Constraint(expr=m.x215**2 + m.x216**2 + m.x227**2 + m.x228**2 - 2*m.x216*m.x228 - 2*m.x215*m.x227
                           - 0.887203867225*m.b68 - 0.887203867225*m.b128 >= -0.887203867225)

m.c2058 = Constraint(expr=m.x215**2 + m.x216**2 + m.x229**2 + m.x230**2 - 2*m.x215*m.x229 - 2*m.x216*m.x230
                           - 0.887203867225*m.b68 - 0.887203867225*m.b143 >= -0.887203867225)

m.c2059 = Constraint(expr=m.x215**2 + m.x216**2 + m.x231**2 + m.x232**2 - 2*m.x216*m.x232 - 2*m.x215*m.x231
                           - 0.887203867225*m.b68 - 0.887203867225*m.b158 >= -0.887203867225)

m.c2060 = Constraint(expr=m.x215**2 + m.x216**2 + m.x233**2 + m.x234**2 - 2*m.x216*m.x234 - 2*m.x215*m.x233
                           - 0.887203867225*m.b68 - 0.887203867225*m.b173 >= -0.887203867225)

m.c2061 = Constraint(expr=m.x215**2 + m.x216**2 + m.x235**2 + m.x236**2 - 2*m.x215*m.x235 - 2*m.x216*m.x236
                           - 0.887203867225*m.b68 - 0.887203867225*m.b188 >= -0.887203867225)

m.c2062 = Constraint(expr=m.x215**2 + m.x216**2 + m.x237**2 + m.x238**2 - 2*m.x216*m.x238 - 2*m.x215*m.x237
                           - 2.118573403024*m.b68 - 2.118573403024*m.b192 >= -2.118573403024)

m.c2063 = Constraint(expr=m.x215**2 + m.x216**2 + m.x239**2 + m.x240**2 - 2*m.x215*m.x239 - 2*m.x216*m.x240
                           - 2.118573403024*m.b68 - 2.118573403024*m.b196 >= -2.118573403024)

m.c2064 = Constraint(expr=m.x215**2 + m.x216**2 + m.x241**2 + m.x242**2 - 2*m.x215*m.x241 - 2*m.x216*m.x242
                           - 2.118573403024*m.b68 - 2.118573403024*m.b200 >= -2.118573403024)

m.c2065 = Constraint(expr=m.x215**2 + m.x216**2 + m.x243**2 + m.x244**2 - 2*m.x215*m.x243 - 2*m.x216*m.x244
                           - 2.118573403024*m.b68 - 2.118573403024*m.b204 >= -2.118573403024)

m.c2066 = Constraint(expr=m.x215**2 + m.x216**2 + m.x245**2 + m.x246**2 - 2*m.x215*m.x245 - 2*m.x216*m.x246
                           - 2.118573403024*m.b68 - 2.118573403024*m.b208 >= -2.118573403024)

m.c2067 = Constraint(expr=m.x215**2 + m.x216**2 + m.x217**2 + m.x218**2 - 2*m.x215*m.x217 - 2*m.x216*m.x218
                           - 1.436939228176*m.b68 - 1.436939228176*m.b77 >= -1.436939228176)

m.c2068 = Constraint(expr=m.x217**2 + m.x218**2 + m.x219**2 + m.x220**2 - 2*m.x217*m.x219 - 2*m.x218*m.x220
                           - 1.436939228176*m.b77 - 1.436939228176*m.b86 >= -1.436939228176)

m.c2069 = Constraint(expr=m.x217**2 + m.x218**2 + m.x221**2 + m.x222**2 - 2*m.x217*m.x221 - 2*m.x218*m.x222
                           - 1.436939228176*m.b77 - 1.436939228176*m.b95 >= -1.436939228176)

m.c2070 = Constraint(expr=m.x217**2 + m.x218**2 + m.x223**2 + m.x224**2 - 2*m.x217*m.x223 - 2*m.x218*m.x224
                           - 1.436939228176*m.b77 - 1.436939228176*m.b104 >= -1.436939228176)

m.c2071 = Constraint(expr=m.x217**2 + m.x218**2 + m.x225**2 + m.x226**2 - 2*m.x218*m.x226 - 2*m.x217*m.x225
                           - 1.436939228176*m.b77 - 1.436939228176*m.b113 >= -1.436939228176)

m.c2072 = Constraint(expr=m.x217**2 + m.x218**2 + m.x227**2 + m.x228**2 - 2*m.x217*m.x227 - 2*m.x218*m.x228
                           - 0.887203867225*m.b77 - 0.887203867225*m.b128 >= -0.887203867225)

m.c2073 = Constraint(expr=m.x217**2 + m.x218**2 + m.x229**2 + m.x230**2 - 2*m.x218*m.x230 - 2*m.x217*m.x229
                           - 0.887203867225*m.b77 - 0.887203867225*m.b143 >= -0.887203867225)

m.c2074 = Constraint(expr=m.x217**2 + m.x218**2 + m.x231**2 + m.x232**2 - 2*m.x218*m.x232 - 2*m.x217*m.x231
                           - 0.887203867225*m.b77 - 0.887203867225*m.b158 >= -0.887203867225)

m.c2075 = Constraint(expr=m.x217**2 + m.x218**2 + m.x233**2 + m.x234**2 - 2*m.x217*m.x233 - 2*m.x218*m.x234
                           - 0.887203867225*m.b77 - 0.887203867225*m.b173 >= -0.887203867225)

m.c2076 = Constraint(expr=m.x217**2 + m.x218**2 + m.x235**2 + m.x236**2 - 2*m.x217*m.x235 - 2*m.x218*m.x236
                           - 0.887203867225*m.b77 - 0.887203867225*m.b188 >= -0.887203867225)

m.c2077 = Constraint(expr=m.x217**2 + m.x218**2 + m.x237**2 + m.x238**2 - 2*m.x218*m.x238 - 2*m.x217*m.x237
                           - 2.118573403024*m.b77 - 2.118573403024*m.b192 >= -2.118573403024)

m.c2078 = Constraint(expr=m.x217**2 + m.x218**2 + m.x239**2 + m.x240**2 - 2*m.x218*m.x240 - 2*m.x217*m.x239
                           - 2.118573403024*m.b77 - 2.118573403024*m.b196 >= -2.118573403024)

m.c2079 = Constraint(expr=m.x217**2 + m.x218**2 + m.x241**2 + m.x242**2 - 2*m.x217*m.x241 - 2*m.x218*m.x242
                           - 2.118573403024*m.b77 - 2.118573403024*m.b200 >= -2.118573403024)

m.c2080 = Constraint(expr=m.x217**2 + m.x218**2 + m.x243**2 + m.x244**2 - 2*m.x217*m.x243 - 2*m.x218*m.x244
                           - 2.118573403024*m.b77 - 2.118573403024*m.b204 >= -2.118573403024)

m.c2081 = Constraint(expr=m.x217**2 + m.x218**2 + m.x245**2 + m.x246**2 - 2*m.x217*m.x245 - 2*m.x218*m.x246
                           - 2.118573403024*m.b77 - 2.118573403024*m.b208 >= -2.118573403024)

m.c2082 = Constraint(expr=m.x215**2 + m.x216**2 + m.x219**2 + m.x220**2 - 2*m.x215*m.x219 - 2*m.x216*m.x220
                           - 1.436939228176*m.b68 - 1.436939228176*m.b86 >= -1.436939228176)

m.c2083 = Constraint(expr=m.x217**2 + m.x218**2 + m.x219**2 + m.x220**2 - 2*m.x217*m.x219 - 2*m.x218*m.x220
                           - 1.436939228176*m.b77 - 1.436939228176*m.b86 >= -1.436939228176)

m.c2084 = Constraint(expr=m.x219**2 + m.x220**2 + m.x221**2 + m.x222**2 - 2*m.x219*m.x221 - 2*m.x220*m.x222
                           - 1.436939228176*m.b86 - 1.436939228176*m.b95 >= -1.436939228176)

m.c2085 = Constraint(expr=m.x219**2 + m.x220**2 + m.x223**2 + m.x224**2 - 2*m.x220*m.x224 - 2*m.x219*m.x223
                           - 1.436939228176*m.b86 - 1.436939228176*m.b104 >= -1.436939228176)

m.c2086 = Constraint(expr=m.x219**2 + m.x220**2 + m.x225**2 + m.x226**2 - 2*m.x220*m.x226 - 2*m.x219*m.x225
                           - 1.436939228176*m.b86 - 1.436939228176*m.b113 >= -1.436939228176)

m.c2087 = Constraint(expr=m.x219**2 + m.x220**2 + m.x227**2 + m.x228**2 - 2*m.x220*m.x228 - 2*m.x219*m.x227
                           - 0.887203867225*m.b86 - 0.887203867225*m.b128 >= -0.887203867225)

m.c2088 = Constraint(expr=m.x219**2 + m.x220**2 + m.x229**2 + m.x230**2 - 2*m.x220*m.x230 - 2*m.x219*m.x229
                           - 0.887203867225*m.b86 - 0.887203867225*m.b143 >= -0.887203867225)

m.c2089 = Constraint(expr=m.x219**2 + m.x220**2 + m.x231**2 + m.x232**2 - 2*m.x219*m.x231 - 2*m.x220*m.x232
                           - 0.887203867225*m.b86 - 0.887203867225*m.b158 >= -0.887203867225)

m.c2090 = Constraint(expr=m.x219**2 + m.x220**2 + m.x233**2 + m.x234**2 - 2*m.x219*m.x233 - 2*m.x220*m.x234
                           - 0.887203867225*m.b86 - 0.887203867225*m.b173 >= -0.887203867225)

m.c2091 = Constraint(expr=m.x219**2 + m.x220**2 + m.x235**2 + m.x236**2 - 2*m.x219*m.x235 - 2*m.x220*m.x236
                           - 0.887203867225*m.b86 - 0.887203867225*m.b188 >= -0.887203867225)

m.c2092 = Constraint(expr=m.x219**2 + m.x220**2 + m.x237**2 + m.x238**2 - 2*m.x220*m.x238 - 2*m.x219*m.x237
                           - 2.118573403024*m.b86 - 2.118573403024*m.b192 >= -2.118573403024)

m.c2093 = Constraint(expr=m.x219**2 + m.x220**2 + m.x239**2 + m.x240**2 - 2*m.x220*m.x240 - 2*m.x219*m.x239
                           - 2.118573403024*m.b86 - 2.118573403024*m.b196 >= -2.118573403024)

m.c2094 = Constraint(expr=m.x219**2 + m.x220**2 + m.x241**2 + m.x242**2 - 2*m.x219*m.x241 - 2*m.x220*m.x242
                           - 2.118573403024*m.b86 - 2.118573403024*m.b200 >= -2.118573403024)

m.c2095 = Constraint(expr=m.x219**2 + m.x220**2 + m.x243**2 + m.x244**2 - 2*m.x219*m.x243 - 2*m.x220*m.x244
                           - 2.118573403024*m.b86 - 2.118573403024*m.b204 >= -2.118573403024)

m.c2096 = Constraint(expr=m.x219**2 + m.x220**2 + m.x245**2 + m.x246**2 - 2*m.x219*m.x245 - 2*m.x220*m.x246
                           - 2.118573403024*m.b86 - 2.118573403024*m.b208 >= -2.118573403024)

m.c2097 = Constraint(expr=m.x215**2 + m.x216**2 + m.x221**2 + m.x222**2 - 2*m.x216*m.x222 - 2*m.x215*m.x221
                           - 1.436939228176*m.b68 - 1.436939228176*m.b95 >= -1.436939228176)

m.c2098 = Constraint(expr=m.x217**2 + m.x218**2 + m.x221**2 + m.x222**2 - 2*m.x217*m.x221 - 2*m.x218*m.x222
                           - 1.436939228176*m.b77 - 1.436939228176*m.b95 >= -1.436939228176)

m.c2099 = Constraint(expr=m.x219**2 + m.x220**2 + m.x221**2 + m.x222**2 - 2*m.x219*m.x221 - 2*m.x220*m.x222
                           - 1.436939228176*m.b86 - 1.436939228176*m.b95 >= -1.436939228176)

m.c2100 = Constraint(expr=m.x221**2 + m.x222**2 + m.x223**2 + m.x224**2 - 2*m.x221*m.x223 - 2*m.x222*m.x224
                           - 1.436939228176*m.b95 - 1.436939228176*m.b104 >= -1.436939228176)

m.c2101 = Constraint(expr=m.x221**2 + m.x222**2 + m.x225**2 + m.x226**2 - 2*m.x221*m.x225 - 2*m.x222*m.x226
                           - 1.436939228176*m.b95 - 1.436939228176*m.b113 >= -1.436939228176)

m.c2102 = Constraint(expr=m.x221**2 + m.x222**2 + m.x227**2 + m.x228**2 - 2*m.x221*m.x227 - 2*m.x222*m.x228
                           - 0.887203867225*m.b95 - 0.887203867225*m.b128 >= -0.887203867225)

m.c2103 = Constraint(expr=m.x221**2 + m.x222**2 + m.x229**2 + m.x230**2 - 2*m.x221*m.x229 - 2*m.x222*m.x230
                           - 0.887203867225*m.b95 - 0.887203867225*m.b143 >= -0.887203867225)

m.c2104 = Constraint(expr=m.x221**2 + m.x222**2 + m.x231**2 + m.x232**2 - 2*m.x221*m.x231 - 2*m.x222*m.x232
                           - 0.887203867225*m.b95 - 0.887203867225*m.b158 >= -0.887203867225)

m.c2105 = Constraint(expr=m.x221**2 + m.x222**2 + m.x233**2 + m.x234**2 - 2*m.x221*m.x233 - 2*m.x222*m.x234
                           - 0.887203867225*m.b95 - 0.887203867225*m.b173 >= -0.887203867225)

m.c2106 = Constraint(expr=m.x221**2 + m.x222**2 + m.x235**2 + m.x236**2 - 2*m.x221*m.x235 - 2*m.x222*m.x236
                           - 0.887203867225*m.b95 - 0.887203867225*m.b188 >= -0.887203867225)

m.c2107 = Constraint(expr=m.x221**2 + m.x222**2 + m.x237**2 + m.x238**2 - 2*m.x221*m.x237 - 2*m.x222*m.x238
                           - 2.118573403024*m.b95 - 2.118573403024*m.b192 >= -2.118573403024)

m.c2108 = Constraint(expr=m.x221**2 + m.x222**2 + m.x239**2 + m.x240**2 - 2*m.x221*m.x239 - 2*m.x222*m.x240
                           - 2.118573403024*m.b95 - 2.118573403024*m.b196 >= -2.118573403024)

m.c2109 = Constraint(expr=m.x221**2 + m.x222**2 + m.x241**2 + m.x242**2 - 2*m.x221*m.x241 - 2*m.x222*m.x242
                           - 2.118573403024*m.b95 - 2.118573403024*m.b200 >= -2.118573403024)

m.c2110 = Constraint(expr=m.x221**2 + m.x222**2 + m.x243**2 + m.x244**2 - 2*m.x221*m.x243 - 2*m.x222*m.x244
                           - 2.118573403024*m.b95 - 2.118573403024*m.b204 >= -2.118573403024)

m.c2111 = Constraint(expr=m.x221**2 + m.x222**2 + m.x245**2 + m.x246**2 - 2*m.x222*m.x246 - 2*m.x221*m.x245
                           - 2.118573403024*m.b95 - 2.118573403024*m.b208 >= -2.118573403024)

m.c2112 = Constraint(expr=m.x215**2 + m.x216**2 + m.x223**2 + m.x224**2 - 2*m.x216*m.x224 - 2*m.x215*m.x223
                           - 1.436939228176*m.b68 - 1.436939228176*m.b104 >= -1.436939228176)

m.c2113 = Constraint(expr=m.x217**2 + m.x218**2 + m.x223**2 + m.x224**2 - 2*m.x217*m.x223 - 2*m.x218*m.x224
                           - 1.436939228176*m.b77 - 1.436939228176*m.b104 >= -1.436939228176)

m.c2114 = Constraint(expr=m.x219**2 + m.x220**2 + m.x223**2 + m.x224**2 - 2*m.x220*m.x224 - 2*m.x219*m.x223
                           - 1.436939228176*m.b86 - 1.436939228176*m.b104 >= -1.436939228176)

m.c2115 = Constraint(expr=m.x221**2 + m.x222**2 + m.x223**2 + m.x224**2 - 2*m.x221*m.x223 - 2*m.x222*m.x224
                           - 1.436939228176*m.b95 - 1.436939228176*m.b104 >= -1.436939228176)

m.c2116 = Constraint(expr=m.x223**2 + m.x224**2 + m.x225**2 + m.x226**2 - 2*m.x223*m.x225 - 2*m.x224*m.x226
                           - 1.436939228176*m.b104 - 1.436939228176*m.b113 >= -1.436939228176)

m.c2117 = Constraint(expr=m.x223**2 + m.x224**2 + m.x227**2 + m.x228**2 - 2*m.x223*m.x227 - 2*m.x224*m.x228
                           - 0.887203867225*m.b104 - 0.887203867225*m.b128 >= -0.887203867225)

m.c2118 = Constraint(expr=m.x223**2 + m.x224**2 + m.x229**2 + m.x230**2 - 2*m.x223*m.x229 - 2*m.x224*m.x230
                           - 0.887203867225*m.b104 - 0.887203867225*m.b143 >= -0.887203867225)

m.c2119 = Constraint(expr=m.x223**2 + m.x224**2 + m.x231**2 + m.x232**2 - 2*m.x223*m.x231 - 2*m.x224*m.x232
                           - 0.887203867225*m.b104 - 0.887203867225*m.b158 >= -0.887203867225)

m.c2120 = Constraint(expr=m.x223**2 + m.x224**2 + m.x233**2 + m.x234**2 - 2*m.x223*m.x233 - 2*m.x224*m.x234
                           - 0.887203867225*m.b104 - 0.887203867225*m.b173 >= -0.887203867225)

m.c2121 = Constraint(expr=m.x223**2 + m.x224**2 + m.x235**2 + m.x236**2 - 2*m.x223*m.x235 - 2*m.x224*m.x236
                           - 0.887203867225*m.b104 - 0.887203867225*m.b188 >= -0.887203867225)

m.c2122 = Constraint(expr=m.x223**2 + m.x224**2 + m.x237**2 + m.x238**2 - 2*m.x223*m.x237 - 2*m.x224*m.x238
                           - 2.118573403024*m.b104 - 2.118573403024*m.b192 >= -2.118573403024)

m.c2123 = Constraint(expr=m.x223**2 + m.x224**2 + m.x239**2 + m.x240**2 - 2*m.x223*m.x239 - 2*m.x224*m.x240
                           - 2.118573403024*m.b104 - 2.118573403024*m.b196 >= -2.118573403024)

m.c2124 = Constraint(expr=m.x223**2 + m.x224**2 + m.x241**2 + m.x242**2 - 2*m.x223*m.x241 - 2*m.x224*m.x242
                           - 2.118573403024*m.b104 - 2.118573403024*m.b200 >= -2.118573403024)

m.c2125 = Constraint(expr=m.x223**2 + m.x224**2 + m.x243**2 + m.x244**2 - 2*m.x224*m.x244 - 2*m.x223*m.x243
                           - 2.118573403024*m.b104 - 2.118573403024*m.b204 >= -2.118573403024)

m.c2126 = Constraint(expr=m.x223**2 + m.x224**2 + m.x245**2 + m.x246**2 - 2*m.x224*m.x246 - 2*m.x223*m.x245
                           - 2.118573403024*m.b104 - 2.118573403024*m.b208 >= -2.118573403024)

m.c2127 = Constraint(expr=m.x215**2 + m.x216**2 + m.x225**2 + m.x226**2 - 2*m.x215*m.x225 - 2*m.x216*m.x226
                           - 1.436939228176*m.b68 - 1.436939228176*m.b113 >= -1.436939228176)

m.c2128 = Constraint(expr=m.x217**2 + m.x218**2 + m.x225**2 + m.x226**2 - 2*m.x218*m.x226 - 2*m.x217*m.x225
                           - 1.436939228176*m.b77 - 1.436939228176*m.b113 >= -1.436939228176)

m.c2129 = Constraint(expr=m.x219**2 + m.x220**2 + m.x225**2 + m.x226**2 - 2*m.x220*m.x226 - 2*m.x219*m.x225
                           - 1.436939228176*m.b86 - 1.436939228176*m.b113 >= -1.436939228176)

m.c2130 = Constraint(expr=m.x221**2 + m.x222**2 + m.x225**2 + m.x226**2 - 2*m.x221*m.x225 - 2*m.x222*m.x226
                           - 1.436939228176*m.b95 - 1.436939228176*m.b113 >= -1.436939228176)

m.c2131 = Constraint(expr=m.x223**2 + m.x224**2 + m.x225**2 + m.x226**2 - 2*m.x223*m.x225 - 2*m.x224*m.x226
                           - 1.436939228176*m.b104 - 1.436939228176*m.b113 >= -1.436939228176)

m.c2132 = Constraint(expr=m.x225**2 + m.x226**2 + m.x227**2 + m.x228**2 - 2*m.x225*m.x227 - 2*m.x226*m.x228
                           - 0.887203867225*m.b113 - 0.887203867225*m.b128 >= -0.887203867225)

m.c2133 = Constraint(expr=m.x225**2 + m.x226**2 + m.x229**2 + m.x230**2 - 2*m.x225*m.x229 - 2*m.x226*m.x230
                           - 0.887203867225*m.b113 - 0.887203867225*m.b143 >= -0.887203867225)

m.c2134 = Constraint(expr=m.x225**2 + m.x226**2 + m.x231**2 + m.x232**2 - 2*m.x225*m.x231 - 2*m.x226*m.x232
                           - 0.887203867225*m.b113 - 0.887203867225*m.b158 >= -0.887203867225)

m.c2135 = Constraint(expr=m.x225**2 + m.x226**2 + m.x233**2 + m.x234**2 - 2*m.x225*m.x233 - 2*m.x226*m.x234
                           - 0.887203867225*m.b113 - 0.887203867225*m.b173 >= -0.887203867225)

m.c2136 = Constraint(expr=m.x225**2 + m.x226**2 + m.x235**2 + m.x236**2 - 2*m.x225*m.x235 - 2*m.x226*m.x236
                           - 0.887203867225*m.b113 - 0.887203867225*m.b188 >= -0.887203867225)

m.c2137 = Constraint(expr=m.x225**2 + m.x226**2 + m.x237**2 + m.x238**2 - 2*m.x225*m.x237 - 2*m.x226*m.x238
                           - 2.118573403024*m.b113 - 2.118573403024*m.b192 >= -2.118573403024)

m.c2138 = Constraint(expr=m.x225**2 + m.x226**2 + m.x239**2 + m.x240**2 - 2*m.x225*m.x239 - 2*m.x226*m.x240
                           - 2.118573403024*m.b113 - 2.118573403024*m.b196 >= -2.118573403024)

m.c2139 = Constraint(expr=m.x225**2 + m.x226**2 + m.x241**2 + m.x242**2 - 2*m.x226*m.x242 - 2*m.x225*m.x241
                           - 2.118573403024*m.b113 - 2.118573403024*m.b200 >= -2.118573403024)

m.c2140 = Constraint(expr=m.x225**2 + m.x226**2 + m.x243**2 + m.x244**2 - 2*m.x226*m.x244 - 2*m.x225*m.x243
                           - 2.118573403024*m.b113 - 2.118573403024*m.b204 >= -2.118573403024)

m.c2141 = Constraint(expr=m.x225**2 + m.x226**2 + m.x245**2 + m.x246**2 - 2*m.x225*m.x245 - 2*m.x226*m.x246
                           - 2.118573403024*m.b113 - 2.118573403024*m.b208 >= -2.118573403024)

m.c2142 = Constraint(expr=m.x215**2 + m.x216**2 + m.x227**2 + m.x228**2 - 2*m.x216*m.x228 - 2*m.x215*m.x227
                           - 0.887203867225*m.b68 - 0.887203867225*m.b128 >= -0.887203867225)

m.c2143 = Constraint(expr=m.x217**2 + m.x218**2 + m.x227**2 + m.x228**2 - 2*m.x217*m.x227 - 2*m.x218*m.x228
                           - 0.887203867225*m.b77 - 0.887203867225*m.b128 >= -0.887203867225)

m.c2144 = Constraint(expr=m.x219**2 + m.x220**2 + m.x227**2 + m.x228**2 - 2*m.x220*m.x228 - 2*m.x219*m.x227
                           - 0.887203867225*m.b86 - 0.887203867225*m.b128 >= -0.887203867225)

m.c2145 = Constraint(expr=m.x221**2 + m.x222**2 + m.x227**2 + m.x228**2 - 2*m.x221*m.x227 - 2*m.x222*m.x228
                           - 0.887203867225*m.b95 - 0.887203867225*m.b128 >= -0.887203867225)

m.c2146 = Constraint(expr=m.x223**2 + m.x224**2 + m.x227**2 + m.x228**2 - 2*m.x223*m.x227 - 2*m.x224*m.x228
                           - 0.887203867225*m.b104 - 0.887203867225*m.b128 >= -0.887203867225)

m.c2147 = Constraint(expr=m.x225**2 + m.x226**2 + m.x227**2 + m.x228**2 - 2*m.x225*m.x227 - 2*m.x226*m.x228
                           - 0.887203867225*m.b113 - 0.887203867225*m.b128 >= -0.887203867225)

m.c2148 = Constraint(expr=m.x227**2 + m.x228**2 + m.x229**2 + m.x230**2 - 2*m.x227*m.x229 - 2*m.x228*m.x230
                           - 0.469370231236*m.b128 - 0.469370231236*m.b143 >= -0.469370231236)

m.c2149 = Constraint(expr=m.x227**2 + m.x228**2 + m.x231**2 + m.x232**2 - 2*m.x227*m.x231 - 2*m.x228*m.x232
                           - 0.469370231236*m.b128 - 0.469370231236*m.b158 >= -0.469370231236)

m.c2150 = Constraint(expr=m.x227**2 + m.x228**2 + m.x233**2 + m.x234**2 - 2*m.x227*m.x233 - 2*m.x228*m.x234
                           - 0.469370231236*m.b128 - 0.469370231236*m.b173 >= -0.469370231236)

m.c2151 = Constraint(expr=m.x227**2 + m.x228**2 + m.x235**2 + m.x236**2 - 2*m.x227*m.x235 - 2*m.x228*m.x236
                           - 0.469370231236*m.b128 - 0.469370231236*m.b188 >= -0.469370231236)

m.c2152 = Constraint(expr=m.x227**2 + m.x228**2 + m.x237**2 + m.x238**2 - 2*m.x227*m.x237 - 2*m.x228*m.x238
                           - 1.436936830729*m.b128 - 1.436936830729*m.b192 >= -1.436936830729)

m.c2153 = Constraint(expr=m.x227**2 + m.x228**2 + m.x239**2 + m.x240**2 - 2*m.x227*m.x239 - 2*m.x228*m.x240
                           - 1.436936830729*m.b128 - 1.436936830729*m.b196 >= -1.436936830729)

m.c2154 = Constraint(expr=m.x227**2 + m.x228**2 + m.x241**2 + m.x242**2 - 2*m.x227*m.x241 - 2*m.x228*m.x242
                           - 1.436936830729*m.b128 - 1.436936830729*m.b200 >= -1.436936830729)

m.c2155 = Constraint(expr=m.x227**2 + m.x228**2 + m.x243**2 + m.x244**2 - 2*m.x228*m.x244 - 2*m.x227*m.x243
                           - 1.436936830729*m.b128 - 1.436936830729*m.b204 >= -1.436936830729)

m.c2156 = Constraint(expr=m.x227**2 + m.x228**2 + m.x245**2 + m.x246**2 - 2*m.x228*m.x246 - 2*m.x227*m.x245
                           - 1.436936830729*m.b128 - 1.436936830729*m.b208 >= -1.436936830729)

m.c2157 = Constraint(expr=m.x215**2 + m.x216**2 + m.x229**2 + m.x230**2 - 2*m.x215*m.x229 - 2*m.x216*m.x230
                           - 0.887203867225*m.b68 - 0.887203867225*m.b143 >= -0.887203867225)

m.c2158 = Constraint(expr=m.x217**2 + m.x218**2 + m.x229**2 + m.x230**2 - 2*m.x218*m.x230 - 2*m.x217*m.x229
                           - 0.887203867225*m.b77 - 0.887203867225*m.b143 >= -0.887203867225)

m.c2159 = Constraint(expr=m.x219**2 + m.x220**2 + m.x229**2 + m.x230**2 - 2*m.x220*m.x230 - 2*m.x219*m.x229
                           - 0.887203867225*m.b86 - 0.887203867225*m.b143 >= -0.887203867225)

m.c2160 = Constraint(expr=m.x221**2 + m.x222**2 + m.x229**2 + m.x230**2 - 2*m.x221*m.x229 - 2*m.x222*m.x230
                           - 0.887203867225*m.b95 - 0.887203867225*m.b143 >= -0.887203867225)

m.c2161 = Constraint(expr=m.x223**2 + m.x224**2 + m.x229**2 + m.x230**2 - 2*m.x223*m.x229 - 2*m.x224*m.x230
                           - 0.887203867225*m.b104 - 0.887203867225*m.b143 >= -0.887203867225)

m.c2162 = Constraint(expr=m.x225**2 + m.x226**2 + m.x229**2 + m.x230**2 - 2*m.x225*m.x229 - 2*m.x226*m.x230
                           - 0.887203867225*m.b113 - 0.887203867225*m.b143 >= -0.887203867225)

m.c2163 = Constraint(expr=m.x227**2 + m.x228**2 + m.x229**2 + m.x230**2 - 2*m.x227*m.x229 - 2*m.x228*m.x230
                           - 0.469370231236*m.b128 - 0.469370231236*m.b143 >= -0.469370231236)

m.c2164 = Constraint(expr=m.x229**2 + m.x230**2 + m.x231**2 + m.x232**2 - 2*m.x229*m.x231 - 2*m.x230*m.x232
                           - 0.469370231236*m.b143 - 0.469370231236*m.b158 >= -0.469370231236)

m.c2165 = Constraint(expr=m.x229**2 + m.x230**2 + m.x233**2 + m.x234**2 - 2*m.x229*m.x233 - 2*m.x230*m.x234
                           - 0.469370231236*m.b143 - 0.469370231236*m.b173 >= -0.469370231236)

m.c2166 = Constraint(expr=m.x229**2 + m.x230**2 + m.x235**2 + m.x236**2 - 2*m.x229*m.x235 - 2*m.x230*m.x236
                           - 0.469370231236*m.b143 - 0.469370231236*m.b188 >= -0.469370231236)

m.c2167 = Constraint(expr=m.x229**2 + m.x230**2 + m.x237**2 + m.x238**2 - 2*m.x229*m.x237 - 2*m.x230*m.x238
                           - 1.436936830729*m.b143 - 1.436936830729*m.b192 >= -1.436936830729)

m.c2168 = Constraint(expr=m.x229**2 + m.x230**2 + m.x239**2 + m.x240**2 - 2*m.x229*m.x239 - 2*m.x230*m.x240
                           - 1.436936830729*m.b143 - 1.436936830729*m.b196 >= -1.436936830729)

m.c2169 = Constraint(expr=m.x229**2 + m.x230**2 + m.x241**2 + m.x242**2 - 2*m.x230*m.x242 - 2*m.x229*m.x241
                           - 1.436936830729*m.b143 - 1.436936830729*m.b200 >= -1.436936830729)

m.c2170 = Constraint(expr=m.x229**2 + m.x230**2 + m.x243**2 + m.x244**2 - 2*m.x230*m.x244 - 2*m.x229*m.x243
                           - 1.436936830729*m.b143 - 1.436936830729*m.b204 >= -1.436936830729)

m.c2171 = Constraint(expr=m.x229**2 + m.x230**2 + m.x245**2 + m.x246**2 - 2*m.x229*m.x245 - 2*m.x230*m.x246
                           - 1.436936830729*m.b143 - 1.436936830729*m.b208 >= -1.436936830729)

m.c2172 = Constraint(expr=m.x215**2 + m.x216**2 + m.x231**2 + m.x232**2 - 2*m.x216*m.x232 - 2*m.x215*m.x231
                           - 0.887203867225*m.b68 - 0.887203867225*m.b158 >= -0.887203867225)

m.c2173 = Constraint(expr=m.x217**2 + m.x218**2 + m.x231**2 + m.x232**2 - 2*m.x218*m.x232 - 2*m.x217*m.x231
                           - 0.887203867225*m.b77 - 0.887203867225*m.b158 >= -0.887203867225)

m.c2174 = Constraint(expr=m.x219**2 + m.x220**2 + m.x231**2 + m.x232**2 - 2*m.x219*m.x231 - 2*m.x220*m.x232
                           - 0.887203867225*m.b86 - 0.887203867225*m.b158 >= -0.887203867225)

m.c2175 = Constraint(expr=m.x221**2 + m.x222**2 + m.x231**2 + m.x232**2 - 2*m.x221*m.x231 - 2*m.x222*m.x232
                           - 0.887203867225*m.b95 - 0.887203867225*m.b158 >= -0.887203867225)

m.c2176 = Constraint(expr=m.x223**2 + m.x224**2 + m.x231**2 + m.x232**2 - 2*m.x223*m.x231 - 2*m.x224*m.x232
                           - 0.887203867225*m.b104 - 0.887203867225*m.b158 >= -0.887203867225)

m.c2177 = Constraint(expr=m.x225**2 + m.x226**2 + m.x231**2 + m.x232**2 - 2*m.x225*m.x231 - 2*m.x226*m.x232
                           - 0.887203867225*m.b113 - 0.887203867225*m.b158 >= -0.887203867225)

m.c2178 = Constraint(expr=m.x227**2 + m.x228**2 + m.x231**2 + m.x232**2 - 2*m.x227*m.x231 - 2*m.x228*m.x232
                           - 0.469370231236*m.b128 - 0.469370231236*m.b158 >= -0.469370231236)

m.c2179 = Constraint(expr=m.x229**2 + m.x230**2 + m.x231**2 + m.x232**2 - 2*m.x229*m.x231 - 2*m.x230*m.x232
                           - 0.469370231236*m.b143 - 0.469370231236*m.b158 >= -0.469370231236)

m.c2180 = Constraint(expr=m.x231**2 + m.x232**2 + m.x233**2 + m.x234**2 - 2*m.x231*m.x233 - 2*m.x232*m.x234
                           - 0.469370231236*m.b158 - 0.469370231236*m.b173 >= -0.469370231236)

m.c2181 = Constraint(expr=m.x231**2 + m.x232**2 + m.x235**2 + m.x236**2 - 2*m.x231*m.x235 - 2*m.x232*m.x236
                           - 0.469370231236*m.b158 - 0.469370231236*m.b188 >= -0.469370231236)

m.c2182 = Constraint(expr=m.x231**2 + m.x232**2 + m.x237**2 + m.x238**2 - 2*m.x231*m.x237 - 2*m.x232*m.x238
                           - 1.436936830729*m.b158 - 1.436936830729*m.b192 >= -1.436936830729)

m.c2183 = Constraint(expr=m.x231**2 + m.x232**2 + m.x239**2 + m.x240**2 - 2*m.x231*m.x239 - 2*m.x232*m.x240
                           - 1.436936830729*m.b158 - 1.436936830729*m.b196 >= -1.436936830729)

m.c2184 = Constraint(expr=m.x231**2 + m.x232**2 + m.x241**2 + m.x242**2 - 2*m.x232*m.x242 - 2*m.x231*m.x241
                           - 1.436936830729*m.b158 - 1.436936830729*m.b200 >= -1.436936830729)

m.c2185 = Constraint(expr=m.x231**2 + m.x232**2 + m.x243**2 + m.x244**2 - 2*m.x231*m.x243 - 2*m.x232*m.x244
                           - 1.436936830729*m.b158 - 1.436936830729*m.b204 >= -1.436936830729)

m.c2186 = Constraint(expr=m.x231**2 + m.x232**2 + m.x245**2 + m.x246**2 - 2*m.x232*m.x246 - 2*m.x231*m.x245
                           - 1.436936830729*m.b158 - 1.436936830729*m.b208 >= -1.436936830729)

m.c2187 = Constraint(expr=m.x215**2 + m.x216**2 + m.x233**2 + m.x234**2 - 2*m.x216*m.x234 - 2*m.x215*m.x233
                           - 0.887203867225*m.b68 - 0.887203867225*m.b173 >= -0.887203867225)

m.c2188 = Constraint(expr=m.x217**2 + m.x218**2 + m.x233**2 + m.x234**2 - 2*m.x217*m.x233 - 2*m.x218*m.x234
                           - 0.887203867225*m.b77 - 0.887203867225*m.b173 >= -0.887203867225)

m.c2189 = Constraint(expr=m.x219**2 + m.x220**2 + m.x233**2 + m.x234**2 - 2*m.x219*m.x233 - 2*m.x220*m.x234
                           - 0.887203867225*m.b86 - 0.887203867225*m.b173 >= -0.887203867225)

m.c2190 = Constraint(expr=m.x221**2 + m.x222**2 + m.x233**2 + m.x234**2 - 2*m.x221*m.x233 - 2*m.x222*m.x234
                           - 0.887203867225*m.b95 - 0.887203867225*m.b173 >= -0.887203867225)

m.c2191 = Constraint(expr=m.x223**2 + m.x224**2 + m.x233**2 + m.x234**2 - 2*m.x223*m.x233 - 2*m.x224*m.x234
                           - 0.887203867225*m.b104 - 0.887203867225*m.b173 >= -0.887203867225)

m.c2192 = Constraint(expr=m.x225**2 + m.x226**2 + m.x233**2 + m.x234**2 - 2*m.x225*m.x233 - 2*m.x226*m.x234
                           - 0.887203867225*m.b113 - 0.887203867225*m.b173 >= -0.887203867225)

m.c2193 = Constraint(expr=m.x227**2 + m.x228**2 + m.x233**2 + m.x234**2 - 2*m.x227*m.x233 - 2*m.x228*m.x234
                           - 0.469370231236*m.b128 - 0.469370231236*m.b173 >= -0.469370231236)

m.c2194 = Constraint(expr=m.x229**2 + m.x230**2 + m.x233**2 + m.x234**2 - 2*m.x229*m.x233 - 2*m.x230*m.x234
                           - 0.469370231236*m.b143 - 0.469370231236*m.b173 >= -0.469370231236)

m.c2195 = Constraint(expr=m.x231**2 + m.x232**2 + m.x233**2 + m.x234**2 - 2*m.x231*m.x233 - 2*m.x232*m.x234
                           - 0.469370231236*m.b158 - 0.469370231236*m.b173 >= -0.469370231236)

m.c2196 = Constraint(expr=m.x233**2 + m.x234**2 + m.x235**2 + m.x236**2 - 2*m.x233*m.x235 - 2*m.x234*m.x236
                           - 0.469370231236*m.b173 - 0.469370231236*m.b188 >= -0.469370231236)

m.c2197 = Constraint(expr=m.x233**2 + m.x234**2 + m.x237**2 + m.x238**2 - 2*m.x233*m.x237 - 2*m.x234*m.x238
                           - 1.436936830729*m.b173 - 1.436936830729*m.b192 >= -1.436936830729)

m.c2198 = Constraint(expr=m.x233**2 + m.x234**2 + m.x239**2 + m.x240**2 - 2*m.x233*m.x239 - 2*m.x234*m.x240
                           - 1.436936830729*m.b173 - 1.436936830729*m.b196 >= -1.436936830729)

m.c2199 = Constraint(expr=m.x233**2 + m.x234**2 + m.x241**2 + m.x242**2 - 2*m.x233*m.x241 - 2*m.x234*m.x242
                           - 1.436936830729*m.b173 - 1.436936830729*m.b200 >= -1.436936830729)

m.c2200 = Constraint(expr=m.x233**2 + m.x234**2 + m.x243**2 + m.x244**2 - 2*m.x234*m.x244 - 2*m.x233*m.x243
                           - 1.436936830729*m.b173 - 1.436936830729*m.b204 >= -1.436936830729)

m.c2201 = Constraint(expr=m.x233**2 + m.x234**2 + m.x245**2 + m.x246**2 - 2*m.x233*m.x245 - 2*m.x234*m.x246
                           - 1.436936830729*m.b173 - 1.436936830729*m.b208 >= -1.436936830729)

m.c2202 = Constraint(expr=m.x215**2 + m.x216**2 + m.x235**2 + m.x236**2 - 2*m.x215*m.x235 - 2*m.x216*m.x236
                           - 0.887203867225*m.b68 - 0.887203867225*m.b188 >= -0.887203867225)

m.c2203 = Constraint(expr=m.x217**2 + m.x218**2 + m.x235**2 + m.x236**2 - 2*m.x217*m.x235 - 2*m.x218*m.x236
                           - 0.887203867225*m.b77 - 0.887203867225*m.b188 >= -0.887203867225)

m.c2204 = Constraint(expr=m.x219**2 + m.x220**2 + m.x235**2 + m.x236**2 - 2*m.x219*m.x235 - 2*m.x220*m.x236
                           - 0.887203867225*m.b86 - 0.887203867225*m.b188 >= -0.887203867225)

m.c2205 = Constraint(expr=m.x221**2 + m.x222**2 + m.x235**2 + m.x236**2 - 2*m.x221*m.x235 - 2*m.x222*m.x236
                           - 0.887203867225*m.b95 - 0.887203867225*m.b188 >= -0.887203867225)

m.c2206 = Constraint(expr=m.x223**2 + m.x224**2 + m.x235**2 + m.x236**2 - 2*m.x223*m.x235 - 2*m.x224*m.x236
                           - 0.887203867225*m.b104 - 0.887203867225*m.b188 >= -0.887203867225)

m.c2207 = Constraint(expr=m.x225**2 + m.x226**2 + m.x235**2 + m.x236**2 - 2*m.x225*m.x235 - 2*m.x226*m.x236
                           - 0.887203867225*m.b113 - 0.887203867225*m.b188 >= -0.887203867225)

m.c2208 = Constraint(expr=m.x227**2 + m.x228**2 + m.x235**2 + m.x236**2 - 2*m.x227*m.x235 - 2*m.x228*m.x236
                           - 0.469370231236*m.b128 - 0.469370231236*m.b188 >= -0.469370231236)

m.c2209 = Constraint(expr=m.x229**2 + m.x230**2 + m.x235**2 + m.x236**2 - 2*m.x229*m.x235 - 2*m.x230*m.x236
                           - 0.469370231236*m.b143 - 0.469370231236*m.b188 >= -0.469370231236)

m.c2210 = Constraint(expr=m.x231**2 + m.x232**2 + m.x235**2 + m.x236**2 - 2*m.x231*m.x235 - 2*m.x232*m.x236
                           - 0.469370231236*m.b158 - 0.469370231236*m.b188 >= -0.469370231236)

m.c2211 = Constraint(expr=m.x233**2 + m.x234**2 + m.x235**2 + m.x236**2 - 2*m.x233*m.x235 - 2*m.x234*m.x236
                           - 0.469370231236*m.b173 - 0.469370231236*m.b188 >= -0.469370231236)

m.c2212 = Constraint(expr=m.x235**2 + m.x236**2 + m.x237**2 + m.x238**2 - 2*m.x235*m.x237 - 2*m.x236*m.x238
                           - 1.436936830729*m.b188 - 1.436936830729*m.b192 >= -1.436936830729)

m.c2213 = Constraint(expr=m.x235**2 + m.x236**2 + m.x239**2 + m.x240**2 - 2*m.x235*m.x239 - 2*m.x236*m.x240
                           - 1.436936830729*m.b188 - 1.436936830729*m.b196 >= -1.436936830729)

m.c2214 = Constraint(expr=m.x235**2 + m.x236**2 + m.x241**2 + m.x242**2 - 2*m.x236*m.x242 - 2*m.x235*m.x241
                           - 1.436936830729*m.b188 - 1.436936830729*m.b200 >= -1.436936830729)

m.c2215 = Constraint(expr=m.x235**2 + m.x236**2 + m.x243**2 + m.x244**2 - 2*m.x235*m.x243 - 2*m.x236*m.x244
                           - 1.436936830729*m.b188 - 1.436936830729*m.b204 >= -1.436936830729)

m.c2216 = Constraint(expr=m.x235**2 + m.x236**2 + m.x245**2 + m.x246**2 - 2*m.x236*m.x246 - 2*m.x235*m.x245
                           - 1.436936830729*m.b188 - 1.436936830729*m.b208 >= -1.436936830729)

m.c2217 = Constraint(expr=m.x215**2 + m.x216**2 + m.x237**2 + m.x238**2 - 2*m.x216*m.x238 - 2*m.x215*m.x237
                           - 2.118573403024*m.b68 - 2.118573403024*m.b192 >= -2.118573403024)

m.c2218 = Constraint(expr=m.x217**2 + m.x218**2 + m.x237**2 + m.x238**2 - 2*m.x218*m.x238 - 2*m.x217*m.x237
                           - 2.118573403024*m.b77 - 2.118573403024*m.b192 >= -2.118573403024)

m.c2219 = Constraint(expr=m.x219**2 + m.x220**2 + m.x237**2 + m.x238**2 - 2*m.x220*m.x238 - 2*m.x219*m.x237
                           - 2.118573403024*m.b86 - 2.118573403024*m.b192 >= -2.118573403024)

m.c2220 = Constraint(expr=m.x221**2 + m.x222**2 + m.x237**2 + m.x238**2 - 2*m.x221*m.x237 - 2*m.x222*m.x238
                           - 2.118573403024*m.b95 - 2.118573403024*m.b192 >= -2.118573403024)

m.c2221 = Constraint(expr=m.x223**2 + m.x224**2 + m.x237**2 + m.x238**2 - 2*m.x223*m.x237 - 2*m.x224*m.x238
                           - 2.118573403024*m.b104 - 2.118573403024*m.b192 >= -2.118573403024)

m.c2222 = Constraint(expr=m.x225**2 + m.x226**2 + m.x237**2 + m.x238**2 - 2*m.x225*m.x237 - 2*m.x226*m.x238
                           - 2.118573403024*m.b113 - 2.118573403024*m.b192 >= -2.118573403024)

m.c2223 = Constraint(expr=m.x227**2 + m.x228**2 + m.x237**2 + m.x238**2 - 2*m.x227*m.x237 - 2*m.x228*m.x238
                           - 1.436936830729*m.b128 - 1.436936830729*m.b192 >= -1.436936830729)

m.c2224 = Constraint(expr=m.x229**2 + m.x230**2 + m.x237**2 + m.x238**2 - 2*m.x229*m.x237 - 2*m.x230*m.x238
                           - 1.436936830729*m.b143 - 1.436936830729*m.b192 >= -1.436936830729)

m.c2225 = Constraint(expr=m.x231**2 + m.x232**2 + m.x237**2 + m.x238**2 - 2*m.x231*m.x237 - 2*m.x232*m.x238
                           - 1.436936830729*m.b158 - 1.436936830729*m.b192 >= -1.436936830729)

m.c2226 = Constraint(expr=m.x233**2 + m.x234**2 + m.x237**2 + m.x238**2 - 2*m.x233*m.x237 - 2*m.x234*m.x238
                           - 1.436936830729*m.b173 - 1.436936830729*m.b192 >= -1.436936830729)

m.c2227 = Constraint(expr=m.x235**2 + m.x236**2 + m.x237**2 + m.x238**2 - 2*m.x235*m.x237 - 2*m.x236*m.x238
                           - 1.436936830729*m.b188 - 1.436936830729*m.b192 >= -1.436936830729)

m.c2228 = Constraint(expr=m.x237**2 + m.x238**2 + m.x239**2 + m.x240**2 - 2*m.x237*m.x239 - 2*m.x238*m.x240
                           - 2.9321082756*m.b192 - 2.9321082756*m.b196 >= -2.9321082756)

m.c2229 = Constraint(expr=m.x237**2 + m.x238**2 + m.x241**2 + m.x242**2 - 2*m.x237*m.x241 - 2*m.x238*m.x242
                           - 2.9321082756*m.b192 - 2.9321082756*m.b200 >= -2.9321082756)

m.c2230 = Constraint(expr=m.x237**2 + m.x238**2 + m.x243**2 + m.x244**2 - 2*m.x238*m.x244 - 2*m.x237*m.x243
                           - 2.9321082756*m.b192 - 2.9321082756*m.b204 >= -2.9321082756)

m.c2231 = Constraint(expr=m.x237**2 + m.x238**2 + m.x245**2 + m.x246**2 - 2*m.x238*m.x246 - 2*m.x237*m.x245
                           - 2.9321082756*m.b192 - 2.9321082756*m.b208 >= -2.9321082756)

m.c2232 = Constraint(expr=m.x215**2 + m.x216**2 + m.x239**2 + m.x240**2 - 2*m.x215*m.x239 - 2*m.x216*m.x240
                           - 2.118573403024*m.b68 - 2.118573403024*m.b196 >= -2.118573403024)

m.c2233 = Constraint(expr=m.x217**2 + m.x218**2 + m.x239**2 + m.x240**2 - 2*m.x218*m.x240 - 2*m.x217*m.x239
                           - 2.118573403024*m.b77 - 2.118573403024*m.b196 >= -2.118573403024)

m.c2234 = Constraint(expr=m.x219**2 + m.x220**2 + m.x239**2 + m.x240**2 - 2*m.x220*m.x240 - 2*m.x219*m.x239
                           - 2.118573403024*m.b86 - 2.118573403024*m.b196 >= -2.118573403024)

m.c2235 = Constraint(expr=m.x221**2 + m.x222**2 + m.x239**2 + m.x240**2 - 2*m.x221*m.x239 - 2*m.x222*m.x240
                           - 2.118573403024*m.b95 - 2.118573403024*m.b196 >= -2.118573403024)

m.c2236 = Constraint(expr=m.x223**2 + m.x224**2 + m.x239**2 + m.x240**2 - 2*m.x223*m.x239 - 2*m.x224*m.x240
                           - 2.118573403024*m.b104 - 2.118573403024*m.b196 >= -2.118573403024)

m.c2237 = Constraint(expr=m.x225**2 + m.x226**2 + m.x239**2 + m.x240**2 - 2*m.x225*m.x239 - 2*m.x226*m.x240
                           - 2.118573403024*m.b113 - 2.118573403024*m.b196 >= -2.118573403024)

m.c2238 = Constraint(expr=m.x227**2 + m.x228**2 + m.x239**2 + m.x240**2 - 2*m.x227*m.x239 - 2*m.x228*m.x240
                           - 1.436936830729*m.b128 - 1.436936830729*m.b196 >= -1.436936830729)

m.c2239 = Constraint(expr=m.x229**2 + m.x230**2 + m.x239**2 + m.x240**2 - 2*m.x229*m.x239 - 2*m.x230*m.x240
                           - 1.436936830729*m.b143 - 1.436936830729*m.b196 >= -1.436936830729)

m.c2240 = Constraint(expr=m.x231**2 + m.x232**2 + m.x239**2 + m.x240**2 - 2*m.x231*m.x239 - 2*m.x232*m.x240
                           - 1.436936830729*m.b158 - 1.436936830729*m.b196 >= -1.436936830729)

m.c2241 = Constraint(expr=m.x233**2 + m.x234**2 + m.x239**2 + m.x240**2 - 2*m.x233*m.x239 - 2*m.x234*m.x240
                           - 1.436936830729*m.b173 - 1.436936830729*m.b196 >= -1.436936830729)

m.c2242 = Constraint(expr=m.x235**2 + m.x236**2 + m.x239**2 + m.x240**2 - 2*m.x235*m.x239 - 2*m.x236*m.x240
                           - 1.436936830729*m.b188 - 1.436936830729*m.b196 >= -1.436936830729)

m.c2243 = Constraint(expr=m.x237**2 + m.x238**2 + m.x239**2 + m.x240**2 - 2*m.x237*m.x239 - 2*m.x238*m.x240
                           - 2.9321082756*m.b192 - 2.9321082756*m.b196 >= -2.9321082756)

m.c2244 = Constraint(expr=m.x239**2 + m.x240**2 + m.x241**2 + m.x242**2 - 2*m.x240*m.x242 - 2*m.x239*m.x241
                           - 2.9321082756*m.b196 - 2.9321082756*m.b200 >= -2.9321082756)

m.c2245 = Constraint(expr=m.x239**2 + m.x240**2 + m.x243**2 + m.x244**2 - 2*m.x240*m.x244 - 2*m.x239*m.x243
                           - 2.9321082756*m.b196 - 2.9321082756*m.b204 >= -2.9321082756)

m.c2246 = Constraint(expr=m.x239**2 + m.x240**2 + m.x245**2 + m.x246**2 - 2*m.x240*m.x246 - 2*m.x239*m.x245
                           - 2.9321082756*m.b196 - 2.9321082756*m.b208 >= -2.9321082756)

m.c2247 = Constraint(expr=m.x215**2 + m.x216**2 + m.x241**2 + m.x242**2 - 2*m.x215*m.x241 - 2*m.x216*m.x242
                           - 2.118573403024*m.b68 - 2.118573403024*m.b200 >= -2.118573403024)

m.c2248 = Constraint(expr=m.x217**2 + m.x218**2 + m.x241**2 + m.x242**2 - 2*m.x217*m.x241 - 2*m.x218*m.x242
                           - 2.118573403024*m.b77 - 2.118573403024*m.b200 >= -2.118573403024)

m.c2249 = Constraint(expr=m.x219**2 + m.x220**2 + m.x241**2 + m.x242**2 - 2*m.x219*m.x241 - 2*m.x220*m.x242
                           - 2.118573403024*m.b86 - 2.118573403024*m.b200 >= -2.118573403024)

m.c2250 = Constraint(expr=m.x221**2 + m.x222**2 + m.x241**2 + m.x242**2 - 2*m.x221*m.x241 - 2*m.x222*m.x242
                           - 2.118573403024*m.b95 - 2.118573403024*m.b200 >= -2.118573403024)

m.c2251 = Constraint(expr=m.x223**2 + m.x224**2 + m.x241**2 + m.x242**2 - 2*m.x223*m.x241 - 2*m.x224*m.x242
                           - 2.118573403024*m.b104 - 2.118573403024*m.b200 >= -2.118573403024)

m.c2252 = Constraint(expr=m.x225**2 + m.x226**2 + m.x241**2 + m.x242**2 - 2*m.x226*m.x242 - 2*m.x225*m.x241
                           - 2.118573403024*m.b113 - 2.118573403024*m.b200 >= -2.118573403024)

m.c2253 = Constraint(expr=m.x227**2 + m.x228**2 + m.x241**2 + m.x242**2 - 2*m.x227*m.x241 - 2*m.x228*m.x242
                           - 1.436936830729*m.b128 - 1.436936830729*m.b200 >= -1.436936830729)

m.c2254 = Constraint(expr=m.x229**2 + m.x230**2 + m.x241**2 + m.x242**2 - 2*m.x230*m.x242 - 2*m.x229*m.x241
                           - 1.436936830729*m.b143 - 1.436936830729*m.b200 >= -1.436936830729)

m.c2255 = Constraint(expr=m.x231**2 + m.x232**2 + m.x241**2 + m.x242**2 - 2*m.x232*m.x242 - 2*m.x231*m.x241
                           - 1.436936830729*m.b158 - 1.436936830729*m.b200 >= -1.436936830729)

m.c2256 = Constraint(expr=m.x233**2 + m.x234**2 + m.x241**2 + m.x242**2 - 2*m.x233*m.x241 - 2*m.x234*m.x242
                           - 1.436936830729*m.b173 - 1.436936830729*m.b200 >= -1.436936830729)

m.c2257 = Constraint(expr=m.x235**2 + m.x236**2 + m.x241**2 + m.x242**2 - 2*m.x236*m.x242 - 2*m.x235*m.x241
                           - 1.436936830729*m.b188 - 1.436936830729*m.b200 >= -1.436936830729)

m.c2258 = Constraint(expr=m.x237**2 + m.x238**2 + m.x241**2 + m.x242**2 - 2*m.x237*m.x241 - 2*m.x238*m.x242
                           - 2.9321082756*m.b192 - 2.9321082756*m.b200 >= -2.9321082756)

m.c2259 = Constraint(expr=m.x239**2 + m.x240**2 + m.x241**2 + m.x242**2 - 2*m.x240*m.x242 - 2*m.x239*m.x241
                           - 2.9321082756*m.b196 - 2.9321082756*m.b200 >= -2.9321082756)

m.c2260 = Constraint(expr=m.x241**2 + m.x242**2 + m.x243**2 + m.x244**2 - 2*m.x241*m.x243 - 2*m.x242*m.x244
                           - 2.9321082756*m.b200 - 2.9321082756*m.b204 >= -2.9321082756)

m.c2261 = Constraint(expr=m.x241**2 + m.x242**2 + m.x245**2 + m.x246**2 - 2*m.x241*m.x245 - 2*m.x242*m.x246
                           - 2.9321082756*m.b200 - 2.9321082756*m.b208 >= -2.9321082756)

m.c2262 = Constraint(expr=m.x215**2 + m.x216**2 + m.x243**2 + m.x244**2 - 2*m.x215*m.x243 - 2*m.x216*m.x244
                           - 2.118573403024*m.b68 - 2.118573403024*m.b204 >= -2.118573403024)

m.c2263 = Constraint(expr=m.x217**2 + m.x218**2 + m.x243**2 + m.x244**2 - 2*m.x217*m.x243 - 2*m.x218*m.x244
                           - 2.118573403024*m.b77 - 2.118573403024*m.b204 >= -2.118573403024)

m.c2264 = Constraint(expr=m.x219**2 + m.x220**2 + m.x243**2 + m.x244**2 - 2*m.x219*m.x243 - 2*m.x220*m.x244
                           - 2.118573403024*m.b86 - 2.118573403024*m.b204 >= -2.118573403024)

m.c2265 = Constraint(expr=m.x221**2 + m.x222**2 + m.x243**2 + m.x244**2 - 2*m.x221*m.x243 - 2*m.x222*m.x244
                           - 2.118573403024*m.b95 - 2.118573403024*m.b204 >= -2.118573403024)

m.c2266 = Constraint(expr=m.x223**2 + m.x224**2 + m.x243**2 + m.x244**2 - 2*m.x224*m.x244 - 2*m.x223*m.x243
                           - 2.118573403024*m.b104 - 2.118573403024*m.b204 >= -2.118573403024)

m.c2267 = Constraint(expr=m.x225**2 + m.x226**2 + m.x243**2 + m.x244**2 - 2*m.x226*m.x244 - 2*m.x225*m.x243
                           - 2.118573403024*m.b113 - 2.118573403024*m.b204 >= -2.118573403024)

m.c2268 = Constraint(expr=m.x227**2 + m.x228**2 + m.x243**2 + m.x244**2 - 2*m.x228*m.x244 - 2*m.x227*m.x243
                           - 1.436936830729*m.b128 - 1.436936830729*m.b204 >= -1.436936830729)

m.c2269 = Constraint(expr=m.x229**2 + m.x230**2 + m.x243**2 + m.x244**2 - 2*m.x230*m.x244 - 2*m.x229*m.x243
                           - 1.436936830729*m.b143 - 1.436936830729*m.b204 >= -1.436936830729)

m.c2270 = Constraint(expr=m.x231**2 + m.x232**2 + m.x243**2 + m.x244**2 - 2*m.x231*m.x243 - 2*m.x232*m.x244
                           - 1.436936830729*m.b158 - 1.436936830729*m.b204 >= -1.436936830729)

m.c2271 = Constraint(expr=m.x233**2 + m.x234**2 + m.x243**2 + m.x244**2 - 2*m.x234*m.x244 - 2*m.x233*m.x243
                           - 1.436936830729*m.b173 - 1.436936830729*m.b204 >= -1.436936830729)

m.c2272 = Constraint(expr=m.x235**2 + m.x236**2 + m.x243**2 + m.x244**2 - 2*m.x235*m.x243 - 2*m.x236*m.x244
                           - 1.436936830729*m.b188 - 1.436936830729*m.b204 >= -1.436936830729)

m.c2273 = Constraint(expr=m.x237**2 + m.x238**2 + m.x243**2 + m.x244**2 - 2*m.x238*m.x244 - 2*m.x237*m.x243
                           - 2.9321082756*m.b192 - 2.9321082756*m.b204 >= -2.9321082756)

m.c2274 = Constraint(expr=m.x239**2 + m.x240**2 + m.x243**2 + m.x244**2 - 2*m.x240*m.x244 - 2*m.x239*m.x243
                           - 2.9321082756*m.b196 - 2.9321082756*m.b204 >= -2.9321082756)

m.c2275 = Constraint(expr=m.x241**2 + m.x242**2 + m.x243**2 + m.x244**2 - 2*m.x241*m.x243 - 2*m.x242*m.x244
                           - 2.9321082756*m.b200 - 2.9321082756*m.b204 >= -2.9321082756)

m.c2276 = Constraint(expr=m.x243**2 + m.x244**2 + m.x245**2 + m.x246**2 - 2*m.x243*m.x245 - 2*m.x244*m.x246
                           - 2.9321082756*m.b204 - 2.9321082756*m.b208 >= -2.9321082756)

m.c2277 = Constraint(expr=m.x215**2 + m.x216**2 + m.x245**2 + m.x246**2 - 2*m.x215*m.x245 - 2*m.x216*m.x246
                           - 2.118573403024*m.b68 - 2.118573403024*m.b208 >= -2.118573403024)

m.c2278 = Constraint(expr=m.x217**2 + m.x218**2 + m.x245**2 + m.x246**2 - 2*m.x217*m.x245 - 2*m.x218*m.x246
                           - 2.118573403024*m.b77 - 2.118573403024*m.b208 >= -2.118573403024)

m.c2279 = Constraint(expr=m.x219**2 + m.x220**2 + m.x245**2 + m.x246**2 - 2*m.x219*m.x245 - 2*m.x220*m.x246
                           - 2.118573403024*m.b86 - 2.118573403024*m.b208 >= -2.118573403024)

m.c2280 = Constraint(expr=m.x221**2 + m.x222**2 + m.x245**2 + m.x246**2 - 2*m.x222*m.x246 - 2*m.x221*m.x245
                           - 2.118573403024*m.b95 - 2.118573403024*m.b208 >= -2.118573403024)

m.c2281 = Constraint(expr=m.x223**2 + m.x224**2 + m.x245**2 + m.x246**2 - 2*m.x224*m.x246 - 2*m.x223*m.x245
                           - 2.118573403024*m.b104 - 2.118573403024*m.b208 >= -2.118573403024)

m.c2282 = Constraint(expr=m.x225**2 + m.x226**2 + m.x245**2 + m.x246**2 - 2*m.x225*m.x245 - 2*m.x226*m.x246
                           - 2.118573403024*m.b113 - 2.118573403024*m.b208 >= -2.118573403024)

m.c2283 = Constraint(expr=m.x227**2 + m.x228**2 + m.x245**2 + m.x246**2 - 2*m.x228*m.x246 - 2*m.x227*m.x245
                           - 1.436936830729*m.b128 - 1.436936830729*m.b208 >= -1.436936830729)

m.c2284 = Constraint(expr=m.x229**2 + m.x230**2 + m.x245**2 + m.x246**2 - 2*m.x229*m.x245 - 2*m.x230*m.x246
                           - 1.436936830729*m.b143 - 1.436936830729*m.b208 >= -1.436936830729)

m.c2285 = Constraint(expr=m.x231**2 + m.x232**2 + m.x245**2 + m.x246**2 - 2*m.x232*m.x246 - 2*m.x231*m.x245
                           - 1.436936830729*m.b158 - 1.436936830729*m.b208 >= -1.436936830729)

m.c2286 = Constraint(expr=m.x233**2 + m.x234**2 + m.x245**2 + m.x246**2 - 2*m.x233*m.x245 - 2*m.x234*m.x246
                           - 1.436936830729*m.b173 - 1.436936830729*m.b208 >= -1.436936830729)

m.c2287 = Constraint(expr=m.x235**2 + m.x236**2 + m.x245**2 + m.x246**2 - 2*m.x236*m.x246 - 2*m.x235*m.x245
                           - 1.436936830729*m.b188 - 1.436936830729*m.b208 >= -1.436936830729)

m.c2288 = Constraint(expr=m.x237**2 + m.x238**2 + m.x245**2 + m.x246**2 - 2*m.x238*m.x246 - 2*m.x237*m.x245
                           - 2.9321082756*m.b192 - 2.9321082756*m.b208 >= -2.9321082756)

m.c2289 = Constraint(expr=m.x239**2 + m.x240**2 + m.x245**2 + m.x246**2 - 2*m.x239*m.x245 - 2*m.x240*m.x246
                           - 2.9321082756*m.b196 - 2.9321082756*m.b208 >= -2.9321082756)

m.c2290 = Constraint(expr=m.x241**2 + m.x242**2 + m.x245**2 + m.x246**2 - 2*m.x241*m.x245 - 2*m.x242*m.x246
                           - 2.9321082756*m.b200 - 2.9321082756*m.b208 >= -2.9321082756)

m.c2291 = Constraint(expr=m.x243**2 + m.x244**2 + m.x245**2 + m.x246**2 - 2*m.x243*m.x245 - 2*m.x244*m.x246
                           - 2.9321082756*m.b204 - 2.9321082756*m.b208 >= -2.9321082756)

m.c2292 = Constraint(expr=m.x215**2 + m.x216**2 + m.x217**2 + m.x218**2 - 2*m.x215*m.x217 - 2*m.x216*m.x218
                           - 1.436939228176*m.b69 - 1.436939228176*m.b78 >= -1.436939228176)

m.c2293 = Constraint(expr=m.x215**2 + m.x216**2 + m.x219**2 + m.x220**2 - 2*m.x215*m.x219 - 2*m.x216*m.x220
                           - 1.436939228176*m.b69 - 1.436939228176*m.b87 >= -1.436939228176)

m.c2294 = Constraint(expr=m.x215**2 + m.x216**2 + m.x221**2 + m.x222**2 - 2*m.x216*m.x222 - 2*m.x215*m.x221
                           - 1.436939228176*m.b69 - 1.436939228176*m.b96 >= -1.436939228176)

m.c2295 = Constraint(expr=m.x215**2 + m.x216**2 + m.x223**2 + m.x224**2 - 2*m.x216*m.x224 - 2*m.x215*m.x223
                           - 1.436939228176*m.b69 - 1.436939228176*m.b105 >= -1.436939228176)

m.c2296 = Constraint(expr=m.x215**2 + m.x216**2 + m.x225**2 + m.x226**2 - 2*m.x215*m.x225 - 2*m.x216*m.x226
                           - 1.436939228176*m.b69 - 1.436939228176*m.b114 >= -1.436939228176)

m.c2297 = Constraint(expr=m.x215**2 + m.x216**2 + m.x227**2 + m.x228**2 - 2*m.x216*m.x228 - 2*m.x215*m.x227
                           - 0.887203867225*m.b69 - 0.887203867225*m.b129 >= -0.887203867225)

m.c2298 = Constraint(expr=m.x215**2 + m.x216**2 + m.x229**2 + m.x230**2 - 2*m.x215*m.x229 - 2*m.x216*m.x230
                           - 0.887203867225*m.b69 - 0.887203867225*m.b144 >= -0.887203867225)

m.c2299 = Constraint(expr=m.x215**2 + m.x216**2 + m.x231**2 + m.x232**2 - 2*m.x216*m.x232 - 2*m.x215*m.x231
                           - 0.887203867225*m.b69 - 0.887203867225*m.b159 >= -0.887203867225)

m.c2300 = Constraint(expr=m.x215**2 + m.x216**2 + m.x233**2 + m.x234**2 - 2*m.x216*m.x234 - 2*m.x215*m.x233
                           - 0.887203867225*m.b69 - 0.887203867225*m.b174 >= -0.887203867225)

m.c2301 = Constraint(expr=m.x215**2 + m.x216**2 + m.x235**2 + m.x236**2 - 2*m.x215*m.x235 - 2*m.x216*m.x236
                           - 0.887203867225*m.b69 - 0.887203867225*m.b189 >= -0.887203867225)

m.c2302 = Constraint(expr=m.x215**2 + m.x216**2 + m.x237**2 + m.x238**2 - 2*m.x216*m.x238 - 2*m.x215*m.x237
                           - 2.118573403024*m.b69 - 2.118573403024*m.b193 >= -2.118573403024)

m.c2303 = Constraint(expr=m.x215**2 + m.x216**2 + m.x239**2 + m.x240**2 - 2*m.x215*m.x239 - 2*m.x216*m.x240
                           - 2.118573403024*m.b69 - 2.118573403024*m.b197 >= -2.118573403024)

m.c2304 = Constraint(expr=m.x215**2 + m.x216**2 + m.x241**2 + m.x242**2 - 2*m.x215*m.x241 - 2*m.x216*m.x242
                           - 2.118573403024*m.b69 - 2.118573403024*m.b201 >= -2.118573403024)

m.c2305 = Constraint(expr=m.x215**2 + m.x216**2 + m.x243**2 + m.x244**2 - 2*m.x215*m.x243 - 2*m.x216*m.x244
                           - 2.118573403024*m.b69 - 2.118573403024*m.b205 >= -2.118573403024)

m.c2306 = Constraint(expr=m.x215**2 + m.x216**2 + m.x245**2 + m.x246**2 - 2*m.x215*m.x245 - 2*m.x216*m.x246
                           - 2.118573403024*m.b69 - 2.118573403024*m.b209 >= -2.118573403024)

m.c2307 = Constraint(expr=m.x215**2 + m.x216**2 + m.x247**2 + m.x248**2 - 2*m.x215*m.x247 - 2*m.x216*m.x248
                           - 4.509770398884*m.b69 - 4.509770398884*m.b211 >= -4.509770398884)

m.c2308 = Constraint(expr=m.x215**2 + m.x216**2 + m.x249**2 + m.x250**2 - 2*m.x215*m.x249 - 2*m.x216*m.x250
                           - 4.509770398884*m.b69 - 4.509770398884*m.b213 >= -4.509770398884)

m.c2309 = Constraint(expr=m.x215**2 + m.x216**2 + m.x217**2 + m.x218**2 - 2*m.x215*m.x217 - 2*m.x216*m.x218
                           - 1.436939228176*m.b69 - 1.436939228176*m.b78 >= -1.436939228176)

m.c2310 = Constraint(expr=m.x217**2 + m.x218**2 + m.x219**2 + m.x220**2 - 2*m.x217*m.x219 - 2*m.x218*m.x220
                           - 1.436939228176*m.b78 - 1.436939228176*m.b87 >= -1.436939228176)

m.c2311 = Constraint(expr=m.x217**2 + m.x218**2 + m.x221**2 + m.x222**2 - 2*m.x218*m.x222 - 2*m.x217*m.x221
                           - 1.436939228176*m.b78 - 1.436939228176*m.b96 >= -1.436939228176)

m.c2312 = Constraint(expr=m.x217**2 + m.x218**2 + m.x223**2 + m.x224**2 - 2*m.x217*m.x223 - 2*m.x218*m.x224
                           - 1.436939228176*m.b78 - 1.436939228176*m.b105 >= -1.436939228176)

m.c2313 = Constraint(expr=m.x217**2 + m.x218**2 + m.x225**2 + m.x226**2 - 2*m.x218*m.x226 - 2*m.x217*m.x225
                           - 1.436939228176*m.b78 - 1.436939228176*m.b114 >= -1.436939228176)

m.c2314 = Constraint(expr=m.x217**2 + m.x218**2 + m.x227**2 + m.x228**2 - 2*m.x217*m.x227 - 2*m.x218*m.x228
                           - 0.887203867225*m.b78 - 0.887203867225*m.b129 >= -0.887203867225)

m.c2315 = Constraint(expr=m.x217**2 + m.x218**2 + m.x229**2 + m.x230**2 - 2*m.x218*m.x230 - 2*m.x217*m.x229
                           - 0.887203867225*m.b78 - 0.887203867225*m.b144 >= -0.887203867225)

m.c2316 = Constraint(expr=m.x217**2 + m.x218**2 + m.x231**2 + m.x232**2 - 2*m.x218*m.x232 - 2*m.x217*m.x231
                           - 0.887203867225*m.b78 - 0.887203867225*m.b159 >= -0.887203867225)

m.c2317 = Constraint(expr=m.x217**2 + m.x218**2 + m.x233**2 + m.x234**2 - 2*m.x217*m.x233 - 2*m.x218*m.x234
                           - 0.887203867225*m.b78 - 0.887203867225*m.b174 >= -0.887203867225)

m.c2318 = Constraint(expr=m.x217**2 + m.x218**2 + m.x235**2 + m.x236**2 - 2*m.x217*m.x235 - 2*m.x218*m.x236
                           - 0.887203867225*m.b78 - 0.887203867225*m.b189 >= -0.887203867225)

m.c2319 = Constraint(expr=m.x217**2 + m.x218**2 + m.x237**2 + m.x238**2 - 2*m.x218*m.x238 - 2*m.x217*m.x237
                           - 2.118573403024*m.b78 - 2.118573403024*m.b193 >= -2.118573403024)

m.c2320 = Constraint(expr=m.x217**2 + m.x218**2 + m.x239**2 + m.x240**2 - 2*m.x218*m.x240 - 2*m.x217*m.x239
                           - 2.118573403024*m.b78 - 2.118573403024*m.b197 >= -2.118573403024)

m.c2321 = Constraint(expr=m.x217**2 + m.x218**2 + m.x241**2 + m.x242**2 - 2*m.x217*m.x241 - 2*m.x218*m.x242
                           - 2.118573403024*m.b78 - 2.118573403024*m.b201 >= -2.118573403024)

m.c2322 = Constraint(expr=m.x217**2 + m.x218**2 + m.x243**2 + m.x244**2 - 2*m.x217*m.x243 - 2*m.x218*m.x244
                           - 2.118573403024*m.b78 - 2.118573403024*m.b205 >= -2.118573403024)

m.c2323 = Constraint(expr=m.x217**2 + m.x218**2 + m.x245**2 + m.x246**2 - 2*m.x217*m.x245 - 2*m.x218*m.x246
                           - 2.118573403024*m.b78 - 2.118573403024*m.b209 >= -2.118573403024)

m.c2324 = Constraint(expr=m.x217**2 + m.x218**2 + m.x247**2 + m.x248**2 - 2*m.x217*m.x247 - 2*m.x218*m.x248
                           - 4.509770398884*m.b78 - 4.509770398884*m.b211 >= -4.509770398884)

m.c2325 = Constraint(expr=m.x217**2 + m.x218**2 + m.x249**2 + m.x250**2 - 2*m.x217*m.x249 - 2*m.x218*m.x250
                           - 4.509770398884*m.b78 - 4.509770398884*m.b213 >= -4.509770398884)

m.c2326 = Constraint(expr=m.x215**2 + m.x216**2 + m.x219**2 + m.x220**2 - 2*m.x215*m.x219 - 2*m.x216*m.x220
                           - 1.436939228176*m.b69 - 1.436939228176*m.b87 >= -1.436939228176)

m.c2327 = Constraint(expr=m.x217**2 + m.x218**2 + m.x219**2 + m.x220**2 - 2*m.x217*m.x219 - 2*m.x218*m.x220
                           - 1.436939228176*m.b78 - 1.436939228176*m.b87 >= -1.436939228176)

m.c2328 = Constraint(expr=m.x219**2 + m.x220**2 + m.x221**2 + m.x222**2 - 2*m.x219*m.x221 - 2*m.x220*m.x222
                           - 1.436939228176*m.b87 - 1.436939228176*m.b96 >= -1.436939228176)

m.c2329 = Constraint(expr=m.x219**2 + m.x220**2 + m.x223**2 + m.x224**2 - 2*m.x220*m.x224 - 2*m.x219*m.x223
                           - 1.436939228176*m.b87 - 1.436939228176*m.b105 >= -1.436939228176)

m.c2330 = Constraint(expr=m.x219**2 + m.x220**2 + m.x225**2 + m.x226**2 - 2*m.x219*m.x225 - 2*m.x220*m.x226
                           - 1.436939228176*m.b87 - 1.436939228176*m.b114 >= -1.436939228176)

m.c2331 = Constraint(expr=m.x219**2 + m.x220**2 + m.x227**2 + m.x228**2 - 2*m.x220*m.x228 - 2*m.x219*m.x227
                           - 0.887203867225*m.b87 - 0.887203867225*m.b129 >= -0.887203867225)

m.c2332 = Constraint(expr=m.x219**2 + m.x220**2 + m.x229**2 + m.x230**2 - 2*m.x219*m.x229 - 2*m.x220*m.x230
                           - 0.887203867225*m.b87 - 0.887203867225*m.b144 >= -0.887203867225)

m.c2333 = Constraint(expr=m.x219**2 + m.x220**2 + m.x231**2 + m.x232**2 - 2*m.x219*m.x231 - 2*m.x220*m.x232
                           - 0.887203867225*m.b87 - 0.887203867225*m.b159 >= -0.887203867225)

m.c2334 = Constraint(expr=m.x219**2 + m.x220**2 + m.x233**2 + m.x234**2 - 2*m.x220*m.x234 - 2*m.x219*m.x233
                           - 0.887203867225*m.b87 - 0.887203867225*m.b174 >= -0.887203867225)

m.c2335 = Constraint(expr=m.x219**2 + m.x220**2 + m.x235**2 + m.x236**2 - 2*m.x219*m.x235 - 2*m.x220*m.x236
                           - 0.887203867225*m.b87 - 0.887203867225*m.b189 >= -0.887203867225)

m.c2336 = Constraint(expr=m.x219**2 + m.x220**2 + m.x237**2 + m.x238**2 - 2*m.x220*m.x238 - 2*m.x219*m.x237
                           - 2.118573403024*m.b87 - 2.118573403024*m.b193 >= -2.118573403024)

m.c2337 = Constraint(expr=m.x219**2 + m.x220**2 + m.x239**2 + m.x240**2 - 2*m.x220*m.x240 - 2*m.x219*m.x239
                           - 2.118573403024*m.b87 - 2.118573403024*m.b197 >= -2.118573403024)

m.c2338 = Constraint(expr=m.x219**2 + m.x220**2 + m.x241**2 + m.x242**2 - 2*m.x219*m.x241 - 2*m.x220*m.x242
                           - 2.118573403024*m.b87 - 2.118573403024*m.b201 >= -2.118573403024)

m.c2339 = Constraint(expr=m.x219**2 + m.x220**2 + m.x243**2 + m.x244**2 - 2*m.x219*m.x243 - 2*m.x220*m.x244
                           - 2.118573403024*m.b87 - 2.118573403024*m.b205 >= -2.118573403024)

m.c2340 = Constraint(expr=m.x219**2 + m.x220**2 + m.x245**2 + m.x246**2 - 2*m.x219*m.x245 - 2*m.x220*m.x246
                           - 2.118573403024*m.b87 - 2.118573403024*m.b209 >= -2.118573403024)

m.c2341 = Constraint(expr=m.x219**2 + m.x220**2 + m.x247**2 + m.x248**2 - 2*m.x219*m.x247 - 2*m.x220*m.x248
                           - 4.509770398884*m.b87 - 4.509770398884*m.b211 >= -4.509770398884)

m.c2342 = Constraint(expr=m.x219**2 + m.x220**2 + m.x249**2 + m.x250**2 - 2*m.x219*m.x249 - 2*m.x220*m.x250
                           - 4.509770398884*m.b87 - 4.509770398884*m.b213 >= -4.509770398884)

m.c2343 = Constraint(expr=m.x215**2 + m.x216**2 + m.x221**2 + m.x222**2 - 2*m.x216*m.x222 - 2*m.x215*m.x221
                           - 1.436939228176*m.b69 - 1.436939228176*m.b96 >= -1.436939228176)

m.c2344 = Constraint(expr=m.x217**2 + m.x218**2 + m.x221**2 + m.x222**2 - 2*m.x218*m.x222 - 2*m.x217*m.x221
                           - 1.436939228176*m.b78 - 1.436939228176*m.b96 >= -1.436939228176)

m.c2345 = Constraint(expr=m.x219**2 + m.x220**2 + m.x221**2 + m.x222**2 - 2*m.x219*m.x221 - 2*m.x220*m.x222
                           - 1.436939228176*m.b87 - 1.436939228176*m.b96 >= -1.436939228176)

m.c2346 = Constraint(expr=m.x221**2 + m.x222**2 + m.x223**2 + m.x224**2 - 2*m.x221*m.x223 - 2*m.x222*m.x224
                           - 1.436939228176*m.b96 - 1.436939228176*m.b105 >= -1.436939228176)

m.c2347 = Constraint(expr=m.x221**2 + m.x222**2 + m.x225**2 + m.x226**2 - 2*m.x221*m.x225 - 2*m.x222*m.x226
                           - 1.436939228176*m.b96 - 1.436939228176*m.b114 >= -1.436939228176)

m.c2348 = Constraint(expr=m.x221**2 + m.x222**2 + m.x227**2 + m.x228**2 - 2*m.x221*m.x227 - 2*m.x222*m.x228
                           - 0.887203867225*m.b96 - 0.887203867225*m.b129 >= -0.887203867225)

m.c2349 = Constraint(expr=m.x221**2 + m.x222**2 + m.x229**2 + m.x230**2 - 2*m.x221*m.x229 - 2*m.x222*m.x230
                           - 0.887203867225*m.b96 - 0.887203867225*m.b144 >= -0.887203867225)

m.c2350 = Constraint(expr=m.x221**2 + m.x222**2 + m.x231**2 + m.x232**2 - 2*m.x221*m.x231 - 2*m.x222*m.x232
                           - 0.887203867225*m.b96 - 0.887203867225*m.b159 >= -0.887203867225)

m.c2351 = Constraint(expr=m.x221**2 + m.x222**2 + m.x233**2 + m.x234**2 - 2*m.x221*m.x233 - 2*m.x222*m.x234
                           - 0.887203867225*m.b96 - 0.887203867225*m.b174 >= -0.887203867225)

m.c2352 = Constraint(expr=m.x221**2 + m.x222**2 + m.x235**2 + m.x236**2 - 2*m.x221*m.x235 - 2*m.x222*m.x236
                           - 0.887203867225*m.b96 - 0.887203867225*m.b189 >= -0.887203867225)

m.c2353 = Constraint(expr=m.x221**2 + m.x222**2 + m.x237**2 + m.x238**2 - 2*m.x221*m.x237 - 2*m.x222*m.x238
                           - 2.118573403024*m.b96 - 2.118573403024*m.b193 >= -2.118573403024)

m.c2354 = Constraint(expr=m.x221**2 + m.x222**2 + m.x239**2 + m.x240**2 - 2*m.x221*m.x239 - 2*m.x222*m.x240
                           - 2.118573403024*m.b96 - 2.118573403024*m.b197 >= -2.118573403024)

m.c2355 = Constraint(expr=m.x221**2 + m.x222**2 + m.x241**2 + m.x242**2 - 2*m.x222*m.x242 - 2*m.x221*m.x241
                           - 2.118573403024*m.b96 - 2.118573403024*m.b201 >= -2.118573403024)

m.c2356 = Constraint(expr=m.x221**2 + m.x222**2 + m.x243**2 + m.x244**2 - 2*m.x221*m.x243 - 2*m.x222*m.x244
                           - 2.118573403024*m.b96 - 2.118573403024*m.b205 >= -2.118573403024)

m.c2357 = Constraint(expr=m.x221**2 + m.x222**2 + m.x245**2 + m.x246**2 - 2*m.x222*m.x246 - 2*m.x221*m.x245
                           - 2.118573403024*m.b96 - 2.118573403024*m.b209 >= -2.118573403024)

m.c2358 = Constraint(expr=m.x221**2 + m.x222**2 + m.x247**2 + m.x248**2 - 2*m.x222*m.x248 - 2*m.x221*m.x247
                           - 4.509770398884*m.b96 - 4.509770398884*m.b211 >= -4.509770398884)

m.c2359 = Constraint(expr=m.x221**2 + m.x222**2 + m.x249**2 + m.x250**2 - 2*m.x221*m.x249 - 2*m.x222*m.x250
                           - 4.509770398884*m.b96 - 4.509770398884*m.b213 >= -4.509770398884)

m.c2360 = Constraint(expr=m.x215**2 + m.x216**2 + m.x223**2 + m.x224**2 - 2*m.x216*m.x224 - 2*m.x215*m.x223
                           - 1.436939228176*m.b69 - 1.436939228176*m.b105 >= -1.436939228176)

m.c2361 = Constraint(expr=m.x217**2 + m.x218**2 + m.x223**2 + m.x224**2 - 2*m.x217*m.x223 - 2*m.x218*m.x224
                           - 1.436939228176*m.b78 - 1.436939228176*m.b105 >= -1.436939228176)

m.c2362 = Constraint(expr=m.x219**2 + m.x220**2 + m.x223**2 + m.x224**2 - 2*m.x220*m.x224 - 2*m.x219*m.x223
                           - 1.436939228176*m.b87 - 1.436939228176*m.b105 >= -1.436939228176)

m.c2363 = Constraint(expr=m.x221**2 + m.x222**2 + m.x223**2 + m.x224**2 - 2*m.x221*m.x223 - 2*m.x222*m.x224
                           - 1.436939228176*m.b96 - 1.436939228176*m.b105 >= -1.436939228176)

m.c2364 = Constraint(expr=m.x223**2 + m.x224**2 + m.x225**2 + m.x226**2 - 2*m.x223*m.x225 - 2*m.x224*m.x226
                           - 1.436939228176*m.b105 - 1.436939228176*m.b114 >= -1.436939228176)

m.c2365 = Constraint(expr=m.x223**2 + m.x224**2 + m.x227**2 + m.x228**2 - 2*m.x223*m.x227 - 2*m.x224*m.x228
                           - 0.887203867225*m.b105 - 0.887203867225*m.b129 >= -0.887203867225)

m.c2366 = Constraint(expr=m.x223**2 + m.x224**2 + m.x229**2 + m.x230**2 - 2*m.x223*m.x229 - 2*m.x224*m.x230
                           - 0.887203867225*m.b105 - 0.887203867225*m.b144 >= -0.887203867225)

m.c2367 = Constraint(expr=m.x223**2 + m.x224**2 + m.x231**2 + m.x232**2 - 2*m.x223*m.x231 - 2*m.x224*m.x232
                           - 0.887203867225*m.b105 - 0.887203867225*m.b159 >= -0.887203867225)

m.c2368 = Constraint(expr=m.x223**2 + m.x224**2 + m.x233**2 + m.x234**2 - 2*m.x223*m.x233 - 2*m.x224*m.x234
                           - 0.887203867225*m.b105 - 0.887203867225*m.b174 >= -0.887203867225)

m.c2369 = Constraint(expr=m.x223**2 + m.x224**2 + m.x235**2 + m.x236**2 - 2*m.x223*m.x235 - 2*m.x224*m.x236
                           - 0.887203867225*m.b105 - 0.887203867225*m.b189 >= -0.887203867225)

m.c2370 = Constraint(expr=m.x223**2 + m.x224**2 + m.x237**2 + m.x238**2 - 2*m.x223*m.x237 - 2*m.x224*m.x238
                           - 2.118573403024*m.b105 - 2.118573403024*m.b193 >= -2.118573403024)

m.c2371 = Constraint(expr=m.x223**2 + m.x224**2 + m.x239**2 + m.x240**2 - 2*m.x223*m.x239 - 2*m.x224*m.x240
                           - 2.118573403024*m.b105 - 2.118573403024*m.b197 >= -2.118573403024)

m.c2372 = Constraint(expr=m.x223**2 + m.x224**2 + m.x241**2 + m.x242**2 - 2*m.x223*m.x241 - 2*m.x224*m.x242
                           - 2.118573403024*m.b105 - 2.118573403024*m.b201 >= -2.118573403024)

m.c2373 = Constraint(expr=m.x223**2 + m.x224**2 + m.x243**2 + m.x244**2 - 2*m.x224*m.x244 - 2*m.x223*m.x243
                           - 2.118573403024*m.b105 - 2.118573403024*m.b205 >= -2.118573403024)

m.c2374 = Constraint(expr=m.x223**2 + m.x224**2 + m.x245**2 + m.x246**2 - 2*m.x224*m.x246 - 2*m.x223*m.x245
                           - 2.118573403024*m.b105 - 2.118573403024*m.b209 >= -2.118573403024)

m.c2375 = Constraint(expr=m.x223**2 + m.x224**2 + m.x247**2 + m.x248**2 - 2*m.x223*m.x247 - 2*m.x224*m.x248
                           - 4.509770398884*m.b105 - 4.509770398884*m.b211 >= -4.509770398884)

m.c2376 = Constraint(expr=m.x223**2 + m.x224**2 + m.x249**2 + m.x250**2 - 2*m.x224*m.x250 - 2*m.x223*m.x249
                           - 4.509770398884*m.b105 - 4.509770398884*m.b213 >= -4.509770398884)

m.c2377 = Constraint(expr=m.x215**2 + m.x216**2 + m.x225**2 + m.x226**2 - 2*m.x215*m.x225 - 2*m.x216*m.x226
                           - 1.436939228176*m.b69 - 1.436939228176*m.b114 >= -1.436939228176)

m.c2378 = Constraint(expr=m.x217**2 + m.x218**2 + m.x225**2 + m.x226**2 - 2*m.x218*m.x226 - 2*m.x217*m.x225
                           - 1.436939228176*m.b78 - 1.436939228176*m.b114 >= -1.436939228176)

m.c2379 = Constraint(expr=m.x219**2 + m.x220**2 + m.x225**2 + m.x226**2 - 2*m.x219*m.x225 - 2*m.x220*m.x226
                           - 1.436939228176*m.b87 - 1.436939228176*m.b114 >= -1.436939228176)

m.c2380 = Constraint(expr=m.x221**2 + m.x222**2 + m.x225**2 + m.x226**2 - 2*m.x221*m.x225 - 2*m.x222*m.x226
                           - 1.436939228176*m.b96 - 1.436939228176*m.b114 >= -1.436939228176)

m.c2381 = Constraint(expr=m.x223**2 + m.x224**2 + m.x225**2 + m.x226**2 - 2*m.x223*m.x225 - 2*m.x224*m.x226
                           - 1.436939228176*m.b105 - 1.436939228176*m.b114 >= -1.436939228176)

m.c2382 = Constraint(expr=m.x225**2 + m.x226**2 + m.x227**2 + m.x228**2 - 2*m.x225*m.x227 - 2*m.x226*m.x228
                           - 0.887203867225*m.b114 - 0.887203867225*m.b129 >= -0.887203867225)

m.c2383 = Constraint(expr=m.x225**2 + m.x226**2 + m.x229**2 + m.x230**2 - 2*m.x225*m.x229 - 2*m.x226*m.x230
                           - 0.887203867225*m.b114 - 0.887203867225*m.b144 >= -0.887203867225)

m.c2384 = Constraint(expr=m.x225**2 + m.x226**2 + m.x231**2 + m.x232**2 - 2*m.x225*m.x231 - 2*m.x226*m.x232
                           - 0.887203867225*m.b114 - 0.887203867225*m.b159 >= -0.887203867225)

m.c2385 = Constraint(expr=m.x225**2 + m.x226**2 + m.x233**2 + m.x234**2 - 2*m.x225*m.x233 - 2*m.x226*m.x234
                           - 0.887203867225*m.b114 - 0.887203867225*m.b174 >= -0.887203867225)

m.c2386 = Constraint(expr=m.x225**2 + m.x226**2 + m.x235**2 + m.x236**2 - 2*m.x225*m.x235 - 2*m.x226*m.x236
                           - 0.887203867225*m.b114 - 0.887203867225*m.b189 >= -0.887203867225)

m.c2387 = Constraint(expr=m.x225**2 + m.x226**2 + m.x237**2 + m.x238**2 - 2*m.x225*m.x237 - 2*m.x226*m.x238
                           - 2.118573403024*m.b114 - 2.118573403024*m.b193 >= -2.118573403024)

m.c2388 = Constraint(expr=m.x225**2 + m.x226**2 + m.x239**2 + m.x240**2 - 2*m.x225*m.x239 - 2*m.x226*m.x240
                           - 2.118573403024*m.b114 - 2.118573403024*m.b197 >= -2.118573403024)

m.c2389 = Constraint(expr=m.x225**2 + m.x226**2 + m.x241**2 + m.x242**2 - 2*m.x226*m.x242 - 2*m.x225*m.x241
                           - 2.118573403024*m.b114 - 2.118573403024*m.b201 >= -2.118573403024)

m.c2390 = Constraint(expr=m.x225**2 + m.x226**2 + m.x243**2 + m.x244**2 - 2*m.x226*m.x244 - 2*m.x225*m.x243
                           - 2.118573403024*m.b114 - 2.118573403024*m.b205 >= -2.118573403024)

m.c2391 = Constraint(expr=m.x225**2 + m.x226**2 + m.x245**2 + m.x246**2 - 2*m.x225*m.x245 - 2*m.x226*m.x246
                           - 2.118573403024*m.b114 - 2.118573403024*m.b209 >= -2.118573403024)

m.c2392 = Constraint(expr=m.x225**2 + m.x226**2 + m.x247**2 + m.x248**2 - 2*m.x226*m.x248 - 2*m.x225*m.x247
                           - 4.509770398884*m.b114 - 4.509770398884*m.b211 >= -4.509770398884)

m.c2393 = Constraint(expr=m.x225**2 + m.x226**2 + m.x249**2 + m.x250**2 - 2*m.x225*m.x249 - 2*m.x226*m.x250
                           - 4.509770398884*m.b114 - 4.509770398884*m.b213 >= -4.509770398884)

m.c2394 = Constraint(expr=m.x215**2 + m.x216**2 + m.x227**2 + m.x228**2 - 2*m.x216*m.x228 - 2*m.x215*m.x227
                           - 0.887203867225*m.b69 - 0.887203867225*m.b129 >= -0.887203867225)

m.c2395 = Constraint(expr=m.x217**2 + m.x218**2 + m.x227**2 + m.x228**2 - 2*m.x217*m.x227 - 2*m.x218*m.x228
                           - 0.887203867225*m.b78 - 0.887203867225*m.b129 >= -0.887203867225)

m.c2396 = Constraint(expr=m.x219**2 + m.x220**2 + m.x227**2 + m.x228**2 - 2*m.x220*m.x228 - 2*m.x219*m.x227
                           - 0.887203867225*m.b87 - 0.887203867225*m.b129 >= -0.887203867225)

m.c2397 = Constraint(expr=m.x221**2 + m.x222**2 + m.x227**2 + m.x228**2 - 2*m.x221*m.x227 - 2*m.x222*m.x228
                           - 0.887203867225*m.b96 - 0.887203867225*m.b129 >= -0.887203867225)

m.c2398 = Constraint(expr=m.x223**2 + m.x224**2 + m.x227**2 + m.x228**2 - 2*m.x223*m.x227 - 2*m.x224*m.x228
                           - 0.887203867225*m.b105 - 0.887203867225*m.b129 >= -0.887203867225)

m.c2399 = Constraint(expr=m.x225**2 + m.x226**2 + m.x227**2 + m.x228**2 - 2*m.x225*m.x227 - 2*m.x226*m.x228
                           - 0.887203867225*m.b114 - 0.887203867225*m.b129 >= -0.887203867225)

m.c2400 = Constraint(expr=m.x227**2 + m.x228**2 + m.x229**2 + m.x230**2 - 2*m.x227*m.x229 - 2*m.x228*m.x230
                           - 0.469370231236*m.b129 - 0.469370231236*m.b144 >= -0.469370231236)

m.c2401 = Constraint(expr=m.x227**2 + m.x228**2 + m.x231**2 + m.x232**2 - 2*m.x227*m.x231 - 2*m.x228*m.x232
                           - 0.469370231236*m.b129 - 0.469370231236*m.b159 >= -0.469370231236)

m.c2402 = Constraint(expr=m.x227**2 + m.x228**2 + m.x233**2 + m.x234**2 - 2*m.x227*m.x233 - 2*m.x228*m.x234
                           - 0.469370231236*m.b129 - 0.469370231236*m.b174 >= -0.469370231236)

m.c2403 = Constraint(expr=m.x227**2 + m.x228**2 + m.x235**2 + m.x236**2 - 2*m.x227*m.x235 - 2*m.x228*m.x236
                           - 0.469370231236*m.b129 - 0.469370231236*m.b189 >= -0.469370231236)

m.c2404 = Constraint(expr=m.x227**2 + m.x228**2 + m.x237**2 + m.x238**2 - 2*m.x227*m.x237 - 2*m.x228*m.x238
                           - 1.436936830729*m.b129 - 1.436936830729*m.b193 >= -1.436936830729)

m.c2405 = Constraint(expr=m.x227**2 + m.x228**2 + m.x239**2 + m.x240**2 - 2*m.x227*m.x239 - 2*m.x228*m.x240
                           - 1.436936830729*m.b129 - 1.436936830729*m.b197 >= -1.436936830729)

m.c2406 = Constraint(expr=m.x227**2 + m.x228**2 + m.x241**2 + m.x242**2 - 2*m.x227*m.x241 - 2*m.x228*m.x242
                           - 1.436936830729*m.b129 - 1.436936830729*m.b201 >= -1.436936830729)

m.c2407 = Constraint(expr=m.x227**2 + m.x228**2 + m.x243**2 + m.x244**2 - 2*m.x228*m.x244 - 2*m.x227*m.x243
                           - 1.436936830729*m.b129 - 1.436936830729*m.b205 >= -1.436936830729)

m.c2408 = Constraint(expr=m.x227**2 + m.x228**2 + m.x245**2 + m.x246**2 - 2*m.x228*m.x246 - 2*m.x227*m.x245
                           - 1.436936830729*m.b129 - 1.436936830729*m.b209 >= -1.436936830729)

m.c2409 = Constraint(expr=m.x227**2 + m.x228**2 + m.x247**2 + m.x248**2 - 2*m.x227*m.x247 - 2*m.x228*m.x248
                           - 3.484990776969*m.b129 - 3.484990776969*m.b211 >= -3.484990776969)

m.c2410 = Constraint(expr=m.x227**2 + m.x228**2 + m.x249**2 + m.x250**2 - 2*m.x228*m.x250 - 2*m.x227*m.x249
                           - 3.484990776969*m.b129 - 3.484990776969*m.b213 >= -3.484990776969)

m.c2411 = Constraint(expr=m.x215**2 + m.x216**2 + m.x229**2 + m.x230**2 - 2*m.x215*m.x229 - 2*m.x216*m.x230
                           - 0.887203867225*m.b69 - 0.887203867225*m.b144 >= -0.887203867225)

m.c2412 = Constraint(expr=m.x217**2 + m.x218**2 + m.x229**2 + m.x230**2 - 2*m.x218*m.x230 - 2*m.x217*m.x229
                           - 0.887203867225*m.b78 - 0.887203867225*m.b144 >= -0.887203867225)

m.c2413 = Constraint(expr=m.x219**2 + m.x220**2 + m.x229**2 + m.x230**2 - 2*m.x219*m.x229 - 2*m.x220*m.x230
                           - 0.887203867225*m.b87 - 0.887203867225*m.b144 >= -0.887203867225)

m.c2414 = Constraint(expr=m.x221**2 + m.x222**2 + m.x229**2 + m.x230**2 - 2*m.x221*m.x229 - 2*m.x222*m.x230
                           - 0.887203867225*m.b96 - 0.887203867225*m.b144 >= -0.887203867225)

m.c2415 = Constraint(expr=m.x223**2 + m.x224**2 + m.x229**2 + m.x230**2 - 2*m.x223*m.x229 - 2*m.x224*m.x230
                           - 0.887203867225*m.b105 - 0.887203867225*m.b144 >= -0.887203867225)

m.c2416 = Constraint(expr=m.x225**2 + m.x226**2 + m.x229**2 + m.x230**2 - 2*m.x225*m.x229 - 2*m.x226*m.x230
                           - 0.887203867225*m.b114 - 0.887203867225*m.b144 >= -0.887203867225)

m.c2417 = Constraint(expr=m.x227**2 + m.x228**2 + m.x229**2 + m.x230**2 - 2*m.x227*m.x229 - 2*m.x228*m.x230
                           - 0.469370231236*m.b129 - 0.469370231236*m.b144 >= -0.469370231236)

m.c2418 = Constraint(expr=m.x229**2 + m.x230**2 + m.x231**2 + m.x232**2 - 2*m.x229*m.x231 - 2*m.x230*m.x232
                           - 0.469370231236*m.b144 - 0.469370231236*m.b159 >= -0.469370231236)

m.c2419 = Constraint(expr=m.x229**2 + m.x230**2 + m.x233**2 + m.x234**2 - 2*m.x229*m.x233 - 2*m.x230*m.x234
                           - 0.469370231236*m.b144 - 0.469370231236*m.b174 >= -0.469370231236)

m.c2420 = Constraint(expr=m.x229**2 + m.x230**2 + m.x235**2 + m.x236**2 - 2*m.x229*m.x235 - 2*m.x230*m.x236
                           - 0.469370231236*m.b144 - 0.469370231236*m.b189 >= -0.469370231236)

m.c2421 = Constraint(expr=m.x229**2 + m.x230**2 + m.x237**2 + m.x238**2 - 2*m.x229*m.x237 - 2*m.x230*m.x238
                           - 1.436936830729*m.b144 - 1.436936830729*m.b193 >= -1.436936830729)

m.c2422 = Constraint(expr=m.x229**2 + m.x230**2 + m.x239**2 + m.x240**2 - 2*m.x229*m.x239 - 2*m.x230*m.x240
                           - 1.436936830729*m.b144 - 1.436936830729*m.b197 >= -1.436936830729)

m.c2423 = Constraint(expr=m.x229**2 + m.x230**2 + m.x241**2 + m.x242**2 - 2*m.x230*m.x242 - 2*m.x229*m.x241
                           - 1.436936830729*m.b144 - 1.436936830729*m.b201 >= -1.436936830729)

m.c2424 = Constraint(expr=m.x229**2 + m.x230**2 + m.x243**2 + m.x244**2 - 2*m.x230*m.x244 - 2*m.x229*m.x243
                           - 1.436936830729*m.b144 - 1.436936830729*m.b205 >= -1.436936830729)

m.c2425 = Constraint(expr=m.x229**2 + m.x230**2 + m.x245**2 + m.x246**2 - 2*m.x229*m.x245 - 2*m.x230*m.x246
                           - 1.436936830729*m.b144 - 1.436936830729*m.b209 >= -1.436936830729)

m.c2426 = Constraint(expr=m.x229**2 + m.x230**2 + m.x247**2 + m.x248**2 - 2*m.x230*m.x248 - 2*m.x229*m.x247
                           - 3.484990776969*m.b144 - 3.484990776969*m.b211 >= -3.484990776969)

m.c2427 = Constraint(expr=m.x229**2 + m.x230**2 + m.x249**2 + m.x250**2 - 2*m.x229*m.x249 - 2*m.x230*m.x250
                           - 3.484990776969*m.b144 - 3.484990776969*m.b213 >= -3.484990776969)

m.c2428 = Constraint(expr=m.x215**2 + m.x216**2 + m.x231**2 + m.x232**2 - 2*m.x216*m.x232 - 2*m.x215*m.x231
                           - 0.887203867225*m.b69 - 0.887203867225*m.b159 >= -0.887203867225)

m.c2429 = Constraint(expr=m.x217**2 + m.x218**2 + m.x231**2 + m.x232**2 - 2*m.x218*m.x232 - 2*m.x217*m.x231
                           - 0.887203867225*m.b78 - 0.887203867225*m.b159 >= -0.887203867225)

m.c2430 = Constraint(expr=m.x219**2 + m.x220**2 + m.x231**2 + m.x232**2 - 2*m.x219*m.x231 - 2*m.x220*m.x232
                           - 0.887203867225*m.b87 - 0.887203867225*m.b159 >= -0.887203867225)

m.c2431 = Constraint(expr=m.x221**2 + m.x222**2 + m.x231**2 + m.x232**2 - 2*m.x221*m.x231 - 2*m.x222*m.x232
                           - 0.887203867225*m.b96 - 0.887203867225*m.b159 >= -0.887203867225)

m.c2432 = Constraint(expr=m.x223**2 + m.x224**2 + m.x231**2 + m.x232**2 - 2*m.x223*m.x231 - 2*m.x224*m.x232
                           - 0.887203867225*m.b105 - 0.887203867225*m.b159 >= -0.887203867225)

m.c2433 = Constraint(expr=m.x225**2 + m.x226**2 + m.x231**2 + m.x232**2 - 2*m.x225*m.x231 - 2*m.x226*m.x232
                           - 0.887203867225*m.b114 - 0.887203867225*m.b159 >= -0.887203867225)

m.c2434 = Constraint(expr=m.x227**2 + m.x228**2 + m.x231**2 + m.x232**2 - 2*m.x227*m.x231 - 2*m.x228*m.x232
                           - 0.469370231236*m.b129 - 0.469370231236*m.b159 >= -0.469370231236)

m.c2435 = Constraint(expr=m.x229**2 + m.x230**2 + m.x231**2 + m.x232**2 - 2*m.x229*m.x231 - 2*m.x230*m.x232
                           - 0.469370231236*m.b144 - 0.469370231236*m.b159 >= -0.469370231236)

m.c2436 = Constraint(expr=m.x231**2 + m.x232**2 + m.x233**2 + m.x234**2 - 2*m.x231*m.x233 - 2*m.x232*m.x234
                           - 0.469370231236*m.b159 - 0.469370231236*m.b174 >= -0.469370231236)

m.c2437 = Constraint(expr=m.x231**2 + m.x232**2 + m.x235**2 + m.x236**2 - 2*m.x231*m.x235 - 2*m.x232*m.x236
                           - 0.469370231236*m.b159 - 0.469370231236*m.b189 >= -0.469370231236)

m.c2438 = Constraint(expr=m.x231**2 + m.x232**2 + m.x237**2 + m.x238**2 - 2*m.x231*m.x237 - 2*m.x232*m.x238
                           - 1.436936830729*m.b159 - 1.436936830729*m.b193 >= -1.436936830729)

m.c2439 = Constraint(expr=m.x231**2 + m.x232**2 + m.x239**2 + m.x240**2 - 2*m.x231*m.x239 - 2*m.x232*m.x240
                           - 1.436936830729*m.b159 - 1.436936830729*m.b197 >= -1.436936830729)

m.c2440 = Constraint(expr=m.x231**2 + m.x232**2 + m.x241**2 + m.x242**2 - 2*m.x232*m.x242 - 2*m.x231*m.x241
                           - 1.436936830729*m.b159 - 1.436936830729*m.b201 >= -1.436936830729)

m.c2441 = Constraint(expr=m.x231**2 + m.x232**2 + m.x243**2 + m.x244**2 - 2*m.x231*m.x243 - 2*m.x232*m.x244
                           - 1.436936830729*m.b159 - 1.436936830729*m.b205 >= -1.436936830729)

m.c2442 = Constraint(expr=m.x231**2 + m.x232**2 + m.x245**2 + m.x246**2 - 2*m.x232*m.x246 - 2*m.x231*m.x245
                           - 1.436936830729*m.b159 - 1.436936830729*m.b209 >= -1.436936830729)

m.c2443 = Constraint(expr=m.x231**2 + m.x232**2 + m.x247**2 + m.x248**2 - 2*m.x231*m.x247 - 2*m.x232*m.x248
                           - 3.484990776969*m.b159 - 3.484990776969*m.b211 >= -3.484990776969)

m.c2444 = Constraint(expr=m.x231**2 + m.x232**2 + m.x249**2 + m.x250**2 - 2*m.x232*m.x250 - 2*m.x231*m.x249
                           - 3.484990776969*m.b159 - 3.484990776969*m.b213 >= -3.484990776969)

m.c2445 = Constraint(expr=m.x215**2 + m.x216**2 + m.x233**2 + m.x234**2 - 2*m.x216*m.x234 - 2*m.x215*m.x233
                           - 0.887203867225*m.b69 - 0.887203867225*m.b174 >= -0.887203867225)

m.c2446 = Constraint(expr=m.x217**2 + m.x218**2 + m.x233**2 + m.x234**2 - 2*m.x217*m.x233 - 2*m.x218*m.x234
                           - 0.887203867225*m.b78 - 0.887203867225*m.b174 >= -0.887203867225)

m.c2447 = Constraint(expr=m.x219**2 + m.x220**2 + m.x233**2 + m.x234**2 - 2*m.x220*m.x234 - 2*m.x219*m.x233
                           - 0.887203867225*m.b87 - 0.887203867225*m.b174 >= -0.887203867225)

m.c2448 = Constraint(expr=m.x221**2 + m.x222**2 + m.x233**2 + m.x234**2 - 2*m.x221*m.x233 - 2*m.x222*m.x234
                           - 0.887203867225*m.b96 - 0.887203867225*m.b174 >= -0.887203867225)

m.c2449 = Constraint(expr=m.x223**2 + m.x224**2 + m.x233**2 + m.x234**2 - 2*m.x223*m.x233 - 2*m.x224*m.x234
                           - 0.887203867225*m.b105 - 0.887203867225*m.b174 >= -0.887203867225)

m.c2450 = Constraint(expr=m.x225**2 + m.x226**2 + m.x233**2 + m.x234**2 - 2*m.x225*m.x233 - 2*m.x226*m.x234
                           - 0.887203867225*m.b114 - 0.887203867225*m.b174 >= -0.887203867225)

m.c2451 = Constraint(expr=m.x227**2 + m.x228**2 + m.x233**2 + m.x234**2 - 2*m.x227*m.x233 - 2*m.x228*m.x234
                           - 0.469370231236*m.b129 - 0.469370231236*m.b174 >= -0.469370231236)

m.c2452 = Constraint(expr=m.x229**2 + m.x230**2 + m.x233**2 + m.x234**2 - 2*m.x229*m.x233 - 2*m.x230*m.x234
                           - 0.469370231236*m.b144 - 0.469370231236*m.b174 >= -0.469370231236)

m.c2453 = Constraint(expr=m.x231**2 + m.x232**2 + m.x233**2 + m.x234**2 - 2*m.x231*m.x233 - 2*m.x232*m.x234
                           - 0.469370231236*m.b159 - 0.469370231236*m.b174 >= -0.469370231236)

m.c2454 = Constraint(expr=m.x233**2 + m.x234**2 + m.x235**2 + m.x236**2 - 2*m.x233*m.x235 - 2*m.x234*m.x236
                           - 0.469370231236*m.b174 - 0.469370231236*m.b189 >= -0.469370231236)

m.c2455 = Constraint(expr=m.x233**2 + m.x234**2 + m.x237**2 + m.x238**2 - 2*m.x233*m.x237 - 2*m.x234*m.x238
                           - 1.436936830729*m.b174 - 1.436936830729*m.b193 >= -1.436936830729)

m.c2456 = Constraint(expr=m.x233**2 + m.x234**2 + m.x239**2 + m.x240**2 - 2*m.x233*m.x239 - 2*m.x234*m.x240
                           - 1.436936830729*m.b174 - 1.436936830729*m.b197 >= -1.436936830729)

m.c2457 = Constraint(expr=m.x233**2 + m.x234**2 + m.x241**2 + m.x242**2 - 2*m.x233*m.x241 - 2*m.x234*m.x242
                           - 1.436936830729*m.b174 - 1.436936830729*m.b201 >= -1.436936830729)

m.c2458 = Constraint(expr=m.x233**2 + m.x234**2 + m.x243**2 + m.x244**2 - 2*m.x234*m.x244 - 2*m.x233*m.x243
                           - 1.436936830729*m.b174 - 1.436936830729*m.b205 >= -1.436936830729)

m.c2459 = Constraint(expr=m.x233**2 + m.x234**2 + m.x245**2 + m.x246**2 - 2*m.x233*m.x245 - 2*m.x234*m.x246
                           - 1.436936830729*m.b174 - 1.436936830729*m.b209 >= -1.436936830729)

m.c2460 = Constraint(expr=m.x233**2 + m.x234**2 + m.x247**2 + m.x248**2 - 2*m.x234*m.x248 - 2*m.x233*m.x247
                           - 3.484990776969*m.b174 - 3.484990776969*m.b211 >= -3.484990776969)

m.c2461 = Constraint(expr=m.x233**2 + m.x234**2 + m.x249**2 + m.x250**2 - 2*m.x234*m.x250 - 2*m.x233*m.x249
                           - 3.484990776969*m.b174 - 3.484990776969*m.b213 >= -3.484990776969)

m.c2462 = Constraint(expr=m.x215**2 + m.x216**2 + m.x235**2 + m.x236**2 - 2*m.x215*m.x235 - 2*m.x216*m.x236
                           - 0.887203867225*m.b69 - 0.887203867225*m.b189 >= -0.887203867225)

m.c2463 = Constraint(expr=m.x217**2 + m.x218**2 + m.x235**2 + m.x236**2 - 2*m.x217*m.x235 - 2*m.x218*m.x236
                           - 0.887203867225*m.b78 - 0.887203867225*m.b189 >= -0.887203867225)

m.c2464 = Constraint(expr=m.x219**2 + m.x220**2 + m.x235**2 + m.x236**2 - 2*m.x219*m.x235 - 2*m.x220*m.x236
                           - 0.887203867225*m.b87 - 0.887203867225*m.b189 >= -0.887203867225)

m.c2465 = Constraint(expr=m.x221**2 + m.x222**2 + m.x235**2 + m.x236**2 - 2*m.x221*m.x235 - 2*m.x222*m.x236
                           - 0.887203867225*m.b96 - 0.887203867225*m.b189 >= -0.887203867225)

m.c2466 = Constraint(expr=m.x223**2 + m.x224**2 + m.x235**2 + m.x236**2 - 2*m.x223*m.x235 - 2*m.x224*m.x236
                           - 0.887203867225*m.b105 - 0.887203867225*m.b189 >= -0.887203867225)

m.c2467 = Constraint(expr=m.x225**2 + m.x226**2 + m.x235**2 + m.x236**2 - 2*m.x225*m.x235 - 2*m.x226*m.x236
                           - 0.887203867225*m.b114 - 0.887203867225*m.b189 >= -0.887203867225)

m.c2468 = Constraint(expr=m.x227**2 + m.x228**2 + m.x235**2 + m.x236**2 - 2*m.x227*m.x235 - 2*m.x228*m.x236
                           - 0.469370231236*m.b129 - 0.469370231236*m.b189 >= -0.469370231236)

m.c2469 = Constraint(expr=m.x229**2 + m.x230**2 + m.x235**2 + m.x236**2 - 2*m.x229*m.x235 - 2*m.x230*m.x236
                           - 0.469370231236*m.b144 - 0.469370231236*m.b189 >= -0.469370231236)

m.c2470 = Constraint(expr=m.x231**2 + m.x232**2 + m.x235**2 + m.x236**2 - 2*m.x231*m.x235 - 2*m.x232*m.x236
                           - 0.469370231236*m.b159 - 0.469370231236*m.b189 >= -0.469370231236)

m.c2471 = Constraint(expr=m.x233**2 + m.x234**2 + m.x235**2 + m.x236**2 - 2*m.x233*m.x235 - 2*m.x234*m.x236
                           - 0.469370231236*m.b174 - 0.469370231236*m.b189 >= -0.469370231236)

m.c2472 = Constraint(expr=m.x235**2 + m.x236**2 + m.x237**2 + m.x238**2 - 2*m.x235*m.x237 - 2*m.x236*m.x238
                           - 1.436936830729*m.b189 - 1.436936830729*m.b193 >= -1.436936830729)

m.c2473 = Constraint(expr=m.x235**2 + m.x236**2 + m.x239**2 + m.x240**2 - 2*m.x235*m.x239 - 2*m.x236*m.x240
                           - 1.436936830729*m.b189 - 1.436936830729*m.b197 >= -1.436936830729)

m.c2474 = Constraint(expr=m.x235**2 + m.x236**2 + m.x241**2 + m.x242**2 - 2*m.x236*m.x242 - 2*m.x235*m.x241
                           - 1.436936830729*m.b189 - 1.436936830729*m.b201 >= -1.436936830729)

m.c2475 = Constraint(expr=m.x235**2 + m.x236**2 + m.x243**2 + m.x244**2 - 2*m.x235*m.x243 - 2*m.x236*m.x244
                           - 1.436936830729*m.b189 - 1.436936830729*m.b205 >= -1.436936830729)

m.c2476 = Constraint(expr=m.x235**2 + m.x236**2 + m.x245**2 + m.x246**2 - 2*m.x236*m.x246 - 2*m.x235*m.x245
                           - 1.436936830729*m.b189 - 1.436936830729*m.b209 >= -1.436936830729)

m.c2477 = Constraint(expr=m.x235**2 + m.x236**2 + m.x247**2 + m.x248**2 - 2*m.x236*m.x248 - 2*m.x235*m.x247
                           - 3.484990776969*m.b189 - 3.484990776969*m.b211 >= -3.484990776969)

m.c2478 = Constraint(expr=m.x235**2 + m.x236**2 + m.x249**2 + m.x250**2 - 2*m.x235*m.x249 - 2*m.x236*m.x250
                           - 3.484990776969*m.b189 - 3.484990776969*m.b213 >= -3.484990776969)

m.c2479 = Constraint(expr=m.x215**2 + m.x216**2 + m.x237**2 + m.x238**2 - 2*m.x216*m.x238 - 2*m.x215*m.x237
                           - 2.118573403024*m.b69 - 2.118573403024*m.b193 >= -2.118573403024)

m.c2480 = Constraint(expr=m.x217**2 + m.x218**2 + m.x237**2 + m.x238**2 - 2*m.x218*m.x238 - 2*m.x217*m.x237
                           - 2.118573403024*m.b78 - 2.118573403024*m.b193 >= -2.118573403024)

m.c2481 = Constraint(expr=m.x219**2 + m.x220**2 + m.x237**2 + m.x238**2 - 2*m.x220*m.x238 - 2*m.x219*m.x237
                           - 2.118573403024*m.b87 - 2.118573403024*m.b193 >= -2.118573403024)

m.c2482 = Constraint(expr=m.x221**2 + m.x222**2 + m.x237**2 + m.x238**2 - 2*m.x221*m.x237 - 2*m.x222*m.x238
                           - 2.118573403024*m.b96 - 2.118573403024*m.b193 >= -2.118573403024)

m.c2483 = Constraint(expr=m.x223**2 + m.x224**2 + m.x237**2 + m.x238**2 - 2*m.x223*m.x237 - 2*m.x224*m.x238
                           - 2.118573403024*m.b105 - 2.118573403024*m.b193 >= -2.118573403024)

m.c2484 = Constraint(expr=m.x225**2 + m.x226**2 + m.x237**2 + m.x238**2 - 2*m.x225*m.x237 - 2*m.x226*m.x238
                           - 2.118573403024*m.b114 - 2.118573403024*m.b193 >= -2.118573403024)

m.c2485 = Constraint(expr=m.x227**2 + m.x228**2 + m.x237**2 + m.x238**2 - 2*m.x227*m.x237 - 2*m.x228*m.x238
                           - 1.436936830729*m.b129 - 1.436936830729*m.b193 >= -1.436936830729)

m.c2486 = Constraint(expr=m.x229**2 + m.x230**2 + m.x237**2 + m.x238**2 - 2*m.x229*m.x237 - 2*m.x230*m.x238
                           - 1.436936830729*m.b144 - 1.436936830729*m.b193 >= -1.436936830729)

m.c2487 = Constraint(expr=m.x231**2 + m.x232**2 + m.x237**2 + m.x238**2 - 2*m.x231*m.x237 - 2*m.x232*m.x238
                           - 1.436936830729*m.b159 - 1.436936830729*m.b193 >= -1.436936830729)

m.c2488 = Constraint(expr=m.x233**2 + m.x234**2 + m.x237**2 + m.x238**2 - 2*m.x233*m.x237 - 2*m.x234*m.x238
                           - 1.436936830729*m.b174 - 1.436936830729*m.b193 >= -1.436936830729)

m.c2489 = Constraint(expr=m.x235**2 + m.x236**2 + m.x237**2 + m.x238**2 - 2*m.x235*m.x237 - 2*m.x236*m.x238
                           - 1.436936830729*m.b189 - 1.436936830729*m.b193 >= -1.436936830729)

m.c2490 = Constraint(expr=m.x237**2 + m.x238**2 + m.x239**2 + m.x240**2 - 2*m.x237*m.x239 - 2*m.x238*m.x240
                           - 2.9321082756*m.b193 - 2.9321082756*m.b197 >= -2.9321082756)

m.c2491 = Constraint(expr=m.x237**2 + m.x238**2 + m.x241**2 + m.x242**2 - 2*m.x237*m.x241 - 2*m.x238*m.x242
                           - 2.9321082756*m.b193 - 2.9321082756*m.b201 >= -2.9321082756)

m.c2492 = Constraint(expr=m.x237**2 + m.x238**2 + m.x243**2 + m.x244**2 - 2*m.x238*m.x244 - 2*m.x237*m.x243
                           - 2.9321082756*m.b193 - 2.9321082756*m.b205 >= -2.9321082756)

m.c2493 = Constraint(expr=m.x237**2 + m.x238**2 + m.x245**2 + m.x246**2 - 2*m.x238*m.x246 - 2*m.x237*m.x245
                           - 2.9321082756*m.b193 - 2.9321082756*m.b209 >= -2.9321082756)

m.c2494 = Constraint(expr=m.x237**2 + m.x238**2 + m.x247**2 + m.x248**2 - 2*m.x237*m.x247 - 2*m.x238*m.x248
                           - 5.6664469849*m.b193 - 5.6664469849*m.b211 >= -5.6664469849)

m.c2495 = Constraint(expr=m.x237**2 + m.x238**2 + m.x249**2 + m.x250**2 - 2*m.x238*m.x250 - 2*m.x237*m.x249
                           - 5.6664469849*m.b193 - 5.6664469849*m.b213 >= -5.6664469849)

m.c2496 = Constraint(expr=m.x215**2 + m.x216**2 + m.x239**2 + m.x240**2 - 2*m.x215*m.x239 - 2*m.x216*m.x240
                           - 2.118573403024*m.b69 - 2.118573403024*m.b197 >= -2.118573403024)

m.c2497 = Constraint(expr=m.x217**2 + m.x218**2 + m.x239**2 + m.x240**2 - 2*m.x218*m.x240 - 2*m.x217*m.x239
                           - 2.118573403024*m.b78 - 2.118573403024*m.b197 >= -2.118573403024)

m.c2498 = Constraint(expr=m.x219**2 + m.x220**2 + m.x239**2 + m.x240**2 - 2*m.x220*m.x240 - 2*m.x219*m.x239
                           - 2.118573403024*m.b87 - 2.118573403024*m.b197 >= -2.118573403024)

m.c2499 = Constraint(expr=m.x221**2 + m.x222**2 + m.x239**2 + m.x240**2 - 2*m.x221*m.x239 - 2*m.x222*m.x240
                           - 2.118573403024*m.b96 - 2.118573403024*m.b197 >= -2.118573403024)

m.c2500 = Constraint(expr=m.x223**2 + m.x224**2 + m.x239**2 + m.x240**2 - 2*m.x223*m.x239 - 2*m.x224*m.x240
                           - 2.118573403024*m.b105 - 2.118573403024*m.b197 >= -2.118573403024)

m.c2501 = Constraint(expr=m.x225**2 + m.x226**2 + m.x239**2 + m.x240**2 - 2*m.x225*m.x239 - 2*m.x226*m.x240
                           - 2.118573403024*m.b114 - 2.118573403024*m.b197 >= -2.118573403024)

m.c2502 = Constraint(expr=m.x227**2 + m.x228**2 + m.x239**2 + m.x240**2 - 2*m.x227*m.x239 - 2*m.x228*m.x240
                           - 1.436936830729*m.b129 - 1.436936830729*m.b197 >= -1.436936830729)

m.c2503 = Constraint(expr=m.x229**2 + m.x230**2 + m.x239**2 + m.x240**2 - 2*m.x229*m.x239 - 2*m.x230*m.x240
                           - 1.436936830729*m.b144 - 1.436936830729*m.b197 >= -1.436936830729)

m.c2504 = Constraint(expr=m.x231**2 + m.x232**2 + m.x239**2 + m.x240**2 - 2*m.x231*m.x239 - 2*m.x232*m.x240
                           - 1.436936830729*m.b159 - 1.436936830729*m.b197 >= -1.436936830729)

m.c2505 = Constraint(expr=m.x233**2 + m.x234**2 + m.x239**2 + m.x240**2 - 2*m.x233*m.x239 - 2*m.x234*m.x240
                           - 1.436936830729*m.b174 - 1.436936830729*m.b197 >= -1.436936830729)

m.c2506 = Constraint(expr=m.x235**2 + m.x236**2 + m.x239**2 + m.x240**2 - 2*m.x235*m.x239 - 2*m.x236*m.x240
                           - 1.436936830729*m.b189 - 1.436936830729*m.b197 >= -1.436936830729)

m.c2507 = Constraint(expr=m.x237**2 + m.x238**2 + m.x239**2 + m.x240**2 - 2*m.x237*m.x239 - 2*m.x238*m.x240
                           - 2.9321082756*m.b193 - 2.9321082756*m.b197 >= -2.9321082756)

m.c2508 = Constraint(expr=m.x239**2 + m.x240**2 + m.x241**2 + m.x242**2 - 2*m.x240*m.x242 - 2*m.x239*m.x241
                           - 2.9321082756*m.b197 - 2.9321082756*m.b201 >= -2.9321082756)

m.c2509 = Constraint(expr=m.x239**2 + m.x240**2 + m.x243**2 + m.x244**2 - 2*m.x240*m.x244 - 2*m.x239*m.x243
                           - 2.9321082756*m.b197 - 2.9321082756*m.b205 >= -2.9321082756)

m.c2510 = Constraint(expr=m.x239**2 + m.x240**2 + m.x245**2 + m.x246**2 - 2*m.x240*m.x246 - 2*m.x239*m.x245
                           - 2.9321082756*m.b197 - 2.9321082756*m.b209 >= -2.9321082756)

m.c2511 = Constraint(expr=m.x239**2 + m.x240**2 + m.x247**2 + m.x248**2 - 2*m.x240*m.x248 - 2*m.x239*m.x247
                           - 5.6664469849*m.b197 - 5.6664469849*m.b211 >= -5.6664469849)

m.c2512 = Constraint(expr=m.x239**2 + m.x240**2 + m.x249**2 + m.x250**2 - 2*m.x240*m.x250 - 2*m.x239*m.x249
                           - 5.6664469849*m.b197 - 5.6664469849*m.b213 >= -5.6664469849)

m.c2513 = Constraint(expr=m.x215**2 + m.x216**2 + m.x241**2 + m.x242**2 - 2*m.x215*m.x241 - 2*m.x216*m.x242
                           - 2.118573403024*m.b69 - 2.118573403024*m.b201 >= -2.118573403024)

m.c2514 = Constraint(expr=m.x217**2 + m.x218**2 + m.x241**2 + m.x242**2 - 2*m.x217*m.x241 - 2*m.x218*m.x242
                           - 2.118573403024*m.b78 - 2.118573403024*m.b201 >= -2.118573403024)

m.c2515 = Constraint(expr=m.x219**2 + m.x220**2 + m.x241**2 + m.x242**2 - 2*m.x219*m.x241 - 2*m.x220*m.x242
                           - 2.118573403024*m.b87 - 2.118573403024*m.b201 >= -2.118573403024)

m.c2516 = Constraint(expr=m.x221**2 + m.x222**2 + m.x241**2 + m.x242**2 - 2*m.x222*m.x242 - 2*m.x221*m.x241
                           - 2.118573403024*m.b96 - 2.118573403024*m.b201 >= -2.118573403024)

m.c2517 = Constraint(expr=m.x223**2 + m.x224**2 + m.x241**2 + m.x242**2 - 2*m.x223*m.x241 - 2*m.x224*m.x242
                           - 2.118573403024*m.b105 - 2.118573403024*m.b201 >= -2.118573403024)

m.c2518 = Constraint(expr=m.x225**2 + m.x226**2 + m.x241**2 + m.x242**2 - 2*m.x225*m.x241 - 2*m.x226*m.x242
                           - 2.118573403024*m.b114 - 2.118573403024*m.b201 >= -2.118573403024)

m.c2519 = Constraint(expr=m.x227**2 + m.x228**2 + m.x241**2 + m.x242**2 - 2*m.x227*m.x241 - 2*m.x228*m.x242
                           - 1.436936830729*m.b129 - 1.436936830729*m.b201 >= -1.436936830729)

m.c2520 = Constraint(expr=m.x229**2 + m.x230**2 + m.x241**2 + m.x242**2 - 2*m.x230*m.x242 - 2*m.x229*m.x241
                           - 1.436936830729*m.b144 - 1.436936830729*m.b201 >= -1.436936830729)

m.c2521 = Constraint(expr=m.x231**2 + m.x232**2 + m.x241**2 + m.x242**2 - 2*m.x232*m.x242 - 2*m.x231*m.x241
                           - 1.436936830729*m.b159 - 1.436936830729*m.b201 >= -1.436936830729)

m.c2522 = Constraint(expr=m.x233**2 + m.x234**2 + m.x241**2 + m.x242**2 - 2*m.x233*m.x241 - 2*m.x234*m.x242
                           - 1.436936830729*m.b174 - 1.436936830729*m.b201 >= -1.436936830729)

m.c2523 = Constraint(expr=m.x235**2 + m.x236**2 + m.x241**2 + m.x242**2 - 2*m.x236*m.x242 - 2*m.x235*m.x241
                           - 1.436936830729*m.b189 - 1.436936830729*m.b201 >= -1.436936830729)

m.c2524 = Constraint(expr=m.x237**2 + m.x238**2 + m.x241**2 + m.x242**2 - 2*m.x237*m.x241 - 2*m.x238*m.x242
                           - 2.9321082756*m.b193 - 2.9321082756*m.b201 >= -2.9321082756)

m.c2525 = Constraint(expr=m.x239**2 + m.x240**2 + m.x241**2 + m.x242**2 - 2*m.x240*m.x242 - 2*m.x239*m.x241
                           - 2.9321082756*m.b197 - 2.9321082756*m.b201 >= -2.9321082756)

m.c2526 = Constraint(expr=m.x241**2 + m.x242**2 + m.x243**2 + m.x244**2 - 2*m.x241*m.x243 - 2*m.x242*m.x244
                           - 2.9321082756*m.b201 - 2.9321082756*m.b205 >= -2.9321082756)

m.c2527 = Constraint(expr=m.x241**2 + m.x242**2 + m.x245**2 + m.x246**2 - 2*m.x241*m.x245 - 2*m.x242*m.x246
                           - 2.9321082756*m.b201 - 2.9321082756*m.b209 >= -2.9321082756)

m.c2528 = Constraint(expr=m.x241**2 + m.x242**2 + m.x247**2 + m.x248**2 - 2*m.x241*m.x247 - 2*m.x242*m.x248
                           - 5.6664469849*m.b201 - 5.6664469849*m.b211 >= -5.6664469849)

m.c2529 = Constraint(expr=m.x241**2 + m.x242**2 + m.x249**2 + m.x250**2 - 2*m.x241*m.x249 - 2*m.x242*m.x250
                           - 5.6664469849*m.b201 - 5.6664469849*m.b213 >= -5.6664469849)

m.c2530 = Constraint(expr=m.x215**2 + m.x216**2 + m.x243**2 + m.x244**2 - 2*m.x215*m.x243 - 2*m.x216*m.x244
                           - 2.118573403024*m.b69 - 2.118573403024*m.b205 >= -2.118573403024)

m.c2531 = Constraint(expr=m.x217**2 + m.x218**2 + m.x243**2 + m.x244**2 - 2*m.x217*m.x243 - 2*m.x218*m.x244
                           - 2.118573403024*m.b78 - 2.118573403024*m.b205 >= -2.118573403024)

m.c2532 = Constraint(expr=m.x219**2 + m.x220**2 + m.x243**2 + m.x244**2 - 2*m.x219*m.x243 - 2*m.x220*m.x244
                           - 2.118573403024*m.b87 - 2.118573403024*m.b205 >= -2.118573403024)

m.c2533 = Constraint(expr=m.x221**2 + m.x222**2 + m.x243**2 + m.x244**2 - 2*m.x221*m.x243 - 2*m.x222*m.x244
                           - 2.118573403024*m.b96 - 2.118573403024*m.b205 >= -2.118573403024)

m.c2534 = Constraint(expr=m.x223**2 + m.x224**2 + m.x243**2 + m.x244**2 - 2*m.x224*m.x244 - 2*m.x223*m.x243
                           - 2.118573403024*m.b105 - 2.118573403024*m.b205 >= -2.118573403024)

m.c2535 = Constraint(expr=m.x225**2 + m.x226**2 + m.x243**2 + m.x244**2 - 2*m.x226*m.x244 - 2*m.x225*m.x243
                           - 2.118573403024*m.b114 - 2.118573403024*m.b205 >= -2.118573403024)

m.c2536 = Constraint(expr=m.x227**2 + m.x228**2 + m.x243**2 + m.x244**2 - 2*m.x228*m.x244 - 2*m.x227*m.x243
                           - 1.436936830729*m.b129 - 1.436936830729*m.b205 >= -1.436936830729)

m.c2537 = Constraint(expr=m.x229**2 + m.x230**2 + m.x243**2 + m.x244**2 - 2*m.x230*m.x244 - 2*m.x229*m.x243
                           - 1.436936830729*m.b144 - 1.436936830729*m.b205 >= -1.436936830729)

m.c2538 = Constraint(expr=m.x231**2 + m.x232**2 + m.x243**2 + m.x244**2 - 2*m.x231*m.x243 - 2*m.x232*m.x244
                           - 1.436936830729*m.b159 - 1.436936830729*m.b205 >= -1.436936830729)

m.c2539 = Constraint(expr=m.x233**2 + m.x234**2 + m.x243**2 + m.x244**2 - 2*m.x234*m.x244 - 2*m.x233*m.x243
                           - 1.436936830729*m.b174 - 1.436936830729*m.b205 >= -1.436936830729)

m.c2540 = Constraint(expr=m.x235**2 + m.x236**2 + m.x243**2 + m.x244**2 - 2*m.x235*m.x243 - 2*m.x236*m.x244
                           - 1.436936830729*m.b189 - 1.436936830729*m.b205 >= -1.436936830729)

m.c2541 = Constraint(expr=m.x237**2 + m.x238**2 + m.x243**2 + m.x244**2 - 2*m.x238*m.x244 - 2*m.x237*m.x243
                           - 2.9321082756*m.b193 - 2.9321082756*m.b205 >= -2.9321082756)

m.c2542 = Constraint(expr=m.x239**2 + m.x240**2 + m.x243**2 + m.x244**2 - 2*m.x240*m.x244 - 2*m.x239*m.x243
                           - 2.9321082756*m.b197 - 2.9321082756*m.b205 >= -2.9321082756)

m.c2543 = Constraint(expr=m.x241**2 + m.x242**2 + m.x243**2 + m.x244**2 - 2*m.x241*m.x243 - 2*m.x242*m.x244
                           - 2.9321082756*m.b201 - 2.9321082756*m.b205 >= -2.9321082756)

m.c2544 = Constraint(expr=m.x243**2 + m.x244**2 + m.x245**2 + m.x246**2 - 2*m.x243*m.x245 - 2*m.x244*m.x246
                           - 2.9321082756*m.b205 - 2.9321082756*m.b209 >= -2.9321082756)

m.c2545 = Constraint(expr=m.x243**2 + m.x244**2 + m.x247**2 + m.x248**2 - 2*m.x243*m.x247 - 2*m.x244*m.x248
                           - 5.6664469849*m.b205 - 5.6664469849*m.b211 >= -5.6664469849)

m.c2546 = Constraint(expr=m.x243**2 + m.x244**2 + m.x249**2 + m.x250**2 - 2*m.x243*m.x249 - 2*m.x244*m.x250
                           - 5.6664469849*m.b205 - 5.6664469849*m.b213 >= -5.6664469849)

m.c2547 = Constraint(expr=m.x215**2 + m.x216**2 + m.x245**2 + m.x246**2 - 2*m.x215*m.x245 - 2*m.x216*m.x246
                           - 2.118573403024*m.b69 - 2.118573403024*m.b209 >= -2.118573403024)

m.c2548 = Constraint(expr=m.x217**2 + m.x218**2 + m.x245**2 + m.x246**2 - 2*m.x217*m.x245 - 2*m.x218*m.x246
                           - 2.118573403024*m.b78 - 2.118573403024*m.b209 >= -2.118573403024)

m.c2549 = Constraint(expr=m.x219**2 + m.x220**2 + m.x245**2 + m.x246**2 - 2*m.x219*m.x245 - 2*m.x220*m.x246
                           - 2.118573403024*m.b87 - 2.118573403024*m.b209 >= -2.118573403024)

m.c2550 = Constraint(expr=m.x221**2 + m.x222**2 + m.x245**2 + m.x246**2 - 2*m.x222*m.x246 - 2*m.x221*m.x245
                           - 2.118573403024*m.b96 - 2.118573403024*m.b209 >= -2.118573403024)

m.c2551 = Constraint(expr=m.x223**2 + m.x224**2 + m.x245**2 + m.x246**2 - 2*m.x224*m.x246 - 2*m.x223*m.x245
                           - 2.118573403024*m.b105 - 2.118573403024*m.b209 >= -2.118573403024)

m.c2552 = Constraint(expr=m.x225**2 + m.x226**2 + m.x245**2 + m.x246**2 - 2*m.x225*m.x245 - 2*m.x226*m.x246
                           - 2.118573403024*m.b114 - 2.118573403024*m.b209 >= -2.118573403024)

m.c2553 = Constraint(expr=m.x227**2 + m.x228**2 + m.x245**2 + m.x246**2 - 2*m.x228*m.x246 - 2*m.x227*m.x245
                           - 1.436936830729*m.b129 - 1.436936830729*m.b209 >= -1.436936830729)

m.c2554 = Constraint(expr=m.x229**2 + m.x230**2 + m.x245**2 + m.x246**2 - 2*m.x229*m.x245 - 2*m.x230*m.x246
                           - 1.436936830729*m.b144 - 1.436936830729*m.b209 >= -1.436936830729)

m.c2555 = Constraint(expr=m.x231**2 + m.x232**2 + m.x245**2 + m.x246**2 - 2*m.x232*m.x246 - 2*m.x231*m.x245
                           - 1.436936830729*m.b159 - 1.436936830729*m.b209 >= -1.436936830729)

m.c2556 = Constraint(expr=m.x233**2 + m.x234**2 + m.x245**2 + m.x246**2 - 2*m.x233*m.x245 - 2*m.x234*m.x246
                           - 1.436936830729*m.b174 - 1.436936830729*m.b209 >= -1.436936830729)

m.c2557 = Constraint(expr=m.x235**2 + m.x236**2 + m.x245**2 + m.x246**2 - 2*m.x236*m.x246 - 2*m.x235*m.x245
                           - 1.436936830729*m.b189 - 1.436936830729*m.b209 >= -1.436936830729)

m.c2558 = Constraint(expr=m.x237**2 + m.x238**2 + m.x245**2 + m.x246**2 - 2*m.x238*m.x246 - 2*m.x237*m.x245
                           - 2.9321082756*m.b193 - 2.9321082756*m.b209 >= -2.9321082756)

m.c2559 = Constraint(expr=m.x239**2 + m.x240**2 + m.x245**2 + m.x246**2 - 2*m.x239*m.x245 - 2*m.x240*m.x246
                           - 2.9321082756*m.b197 - 2.9321082756*m.b209 >= -2.9321082756)

m.c2560 = Constraint(expr=m.x241**2 + m.x242**2 + m.x245**2 + m.x246**2 - 2*m.x241*m.x245 - 2*m.x242*m.x246
                           - 2.9321082756*m.b201 - 2.9321082756*m.b209 >= -2.9321082756)

m.c2561 = Constraint(expr=m.x243**2 + m.x244**2 + m.x245**2 + m.x246**2 - 2*m.x243*m.x245 - 2*m.x244*m.x246
                           - 2.9321082756*m.b205 - 2.9321082756*m.b209 >= -2.9321082756)

m.c2562 = Constraint(expr=m.x245**2 + m.x246**2 + m.x247**2 + m.x248**2 - 2*m.x245*m.x247 - 2*m.x246*m.x248
                           - 5.6664469849*m.b209 - 5.6664469849*m.b211 >= -5.6664469849)

m.c2563 = Constraint(expr=m.x245**2 + m.x246**2 + m.x249**2 + m.x250**2 - 2*m.x245*m.x249 - 2*m.x246*m.x250
                           - 5.6664469849*m.b209 - 5.6664469849*m.b213 >= -5.6664469849)

m.c2564 = Constraint(expr=m.x215**2 + m.x216**2 + m.x247**2 + m.x248**2 - 2*m.x215*m.x247 - 2*m.x216*m.x248
                           - 4.509770398884*m.b69 - 4.509770398884*m.b211 >= -4.509770398884)

m.c2565 = Constraint(expr=m.x217**2 + m.x218**2 + m.x247**2 + m.x248**2 - 2*m.x217*m.x247 - 2*m.x218*m.x248
                           - 4.509770398884*m.b78 - 4.509770398884*m.b211 >= -4.509770398884)

m.c2566 = Constraint(expr=m.x219**2 + m.x220**2 + m.x247**2 + m.x248**2 - 2*m.x219*m.x247 - 2*m.x220*m.x248
                           - 4.509770398884*m.b87 - 4.509770398884*m.b211 >= -4.509770398884)

m.c2567 = Constraint(expr=m.x221**2 + m.x222**2 + m.x247**2 + m.x248**2 - 2*m.x221*m.x247 - 2*m.x222*m.x248
                           - 4.509770398884*m.b96 - 4.509770398884*m.b211 >= -4.509770398884)

m.c2568 = Constraint(expr=m.x223**2 + m.x224**2 + m.x247**2 + m.x248**2 - 2*m.x223*m.x247 - 2*m.x224*m.x248
                           - 4.509770398884*m.b105 - 4.509770398884*m.b211 >= -4.509770398884)

m.c2569 = Constraint(expr=m.x225**2 + m.x226**2 + m.x247**2 + m.x248**2 - 2*m.x226*m.x248 - 2*m.x225*m.x247
                           - 4.509770398884*m.b114 - 4.509770398884*m.b211 >= -4.509770398884)

m.c2570 = Constraint(expr=m.x227**2 + m.x228**2 + m.x247**2 + m.x248**2 - 2*m.x227*m.x247 - 2*m.x228*m.x248
                           - 3.484990776969*m.b129 - 3.484990776969*m.b211 >= -3.484990776969)

m.c2571 = Constraint(expr=m.x229**2 + m.x230**2 + m.x247**2 + m.x248**2 - 2*m.x230*m.x248 - 2*m.x229*m.x247
                           - 3.484990776969*m.b144 - 3.484990776969*m.b211 >= -3.484990776969)

m.c2572 = Constraint(expr=m.x231**2 + m.x232**2 + m.x247**2 + m.x248**2 - 2*m.x231*m.x247 - 2*m.x232*m.x248
                           - 3.484990776969*m.b159 - 3.484990776969*m.b211 >= -3.484990776969)

m.c2573 = Constraint(expr=m.x233**2 + m.x234**2 + m.x247**2 + m.x248**2 - 2*m.x234*m.x248 - 2*m.x233*m.x247
                           - 3.484990776969*m.b174 - 3.484990776969*m.b211 >= -3.484990776969)

m.c2574 = Constraint(expr=m.x235**2 + m.x236**2 + m.x247**2 + m.x248**2 - 2*m.x236*m.x248 - 2*m.x235*m.x247
                           - 3.484990776969*m.b189 - 3.484990776969*m.b211 >= -3.484990776969)

m.c2575 = Constraint(expr=m.x237**2 + m.x238**2 + m.x247**2 + m.x248**2 - 2*m.x237*m.x247 - 2*m.x238*m.x248
                           - 5.6664469849*m.b193 - 5.6664469849*m.b211 >= -5.6664469849)

m.c2576 = Constraint(expr=m.x239**2 + m.x240**2 + m.x247**2 + m.x248**2 - 2*m.x240*m.x248 - 2*m.x239*m.x247
                           - 5.6664469849*m.b197 - 5.6664469849*m.b211 >= -5.6664469849)

m.c2577 = Constraint(expr=m.x241**2 + m.x242**2 + m.x247**2 + m.x248**2 - 2*m.x241*m.x247 - 2*m.x242*m.x248
                           - 5.6664469849*m.b201 - 5.6664469849*m.b211 >= -5.6664469849)

m.c2578 = Constraint(expr=m.x243**2 + m.x244**2 + m.x247**2 + m.x248**2 - 2*m.x243*m.x247 - 2*m.x244*m.x248
                           - 5.6664469849*m.b205 - 5.6664469849*m.b211 >= -5.6664469849)

m.c2579 = Constraint(expr=m.x245**2 + m.x246**2 + m.x247**2 + m.x248**2 - 2*m.x245*m.x247 - 2*m.x246*m.x248
                           - 5.6664469849*m.b209 - 5.6664469849*m.b211 >= -5.6664469849)

m.c2580 = Constraint(expr=m.x247**2 + m.x248**2 + m.x249**2 + m.x250**2 - 2*m.x247*m.x249 - 2*m.x248*m.x250
                           - 9.2934741904*m.b211 - 9.2934741904*m.b213 >= -9.2934741904)

m.c2581 = Constraint(expr=m.x215**2 + m.x216**2 + m.x249**2 + m.x250**2 - 2*m.x215*m.x249 - 2*m.x216*m.x250
                           - 4.509770398884*m.b69 - 4.509770398884*m.b213 >= -4.509770398884)

m.c2582 = Constraint(expr=m.x217**2 + m.x218**2 + m.x249**2 + m.x250**2 - 2*m.x217*m.x249 - 2*m.x218*m.x250
                           - 4.509770398884*m.b78 - 4.509770398884*m.b213 >= -4.509770398884)

m.c2583 = Constraint(expr=m.x219**2 + m.x220**2 + m.x249**2 + m.x250**2 - 2*m.x219*m.x249 - 2*m.x220*m.x250
                           - 4.509770398884*m.b87 - 4.509770398884*m.b213 >= -4.509770398884)

m.c2584 = Constraint(expr=m.x221**2 + m.x222**2 + m.x249**2 + m.x250**2 - 2*m.x221*m.x249 - 2*m.x222*m.x250
                           - 4.509770398884*m.b96 - 4.509770398884*m.b213 >= -4.509770398884)

m.c2585 = Constraint(expr=m.x223**2 + m.x224**2 + m.x249**2 + m.x250**2 - 2*m.x224*m.x250 - 2*m.x223*m.x249
                           - 4.509770398884*m.b105 - 4.509770398884*m.b213 >= -4.509770398884)

m.c2586 = Constraint(expr=m.x225**2 + m.x226**2 + m.x249**2 + m.x250**2 - 2*m.x225*m.x249 - 2*m.x226*m.x250
                           - 4.509770398884*m.b114 - 4.509770398884*m.b213 >= -4.509770398884)

m.c2587 = Constraint(expr=m.x227**2 + m.x228**2 + m.x249**2 + m.x250**2 - 2*m.x228*m.x250 - 2*m.x227*m.x249
                           - 3.484990776969*m.b129 - 3.484990776969*m.b213 >= -3.484990776969)

m.c2588 = Constraint(expr=m.x229**2 + m.x230**2 + m.x249**2 + m.x250**2 - 2*m.x229*m.x249 - 2*m.x230*m.x250
                           - 3.484990776969*m.b144 - 3.484990776969*m.b213 >= -3.484990776969)

m.c2589 = Constraint(expr=m.x231**2 + m.x232**2 + m.x249**2 + m.x250**2 - 2*m.x232*m.x250 - 2*m.x231*m.x249
                           - 3.484990776969*m.b159 - 3.484990776969*m.b213 >= -3.484990776969)

m.c2590 = Constraint(expr=m.x233**2 + m.x234**2 + m.x249**2 + m.x250**2 - 2*m.x234*m.x250 - 2*m.x233*m.x249
                           - 3.484990776969*m.b174 - 3.484990776969*m.b213 >= -3.484990776969)

m.c2591 = Constraint(expr=m.x235**2 + m.x236**2 + m.x249**2 + m.x250**2 - 2*m.x235*m.x249 - 2*m.x236*m.x250
                           - 3.484990776969*m.b189 - 3.484990776969*m.b213 >= -3.484990776969)

m.c2592 = Constraint(expr=m.x237**2 + m.x238**2 + m.x249**2 + m.x250**2 - 2*m.x238*m.x250 - 2*m.x237*m.x249
                           - 5.6664469849*m.b193 - 5.6664469849*m.b213 >= -5.6664469849)

m.c2593 = Constraint(expr=m.x239**2 + m.x240**2 + m.x249**2 + m.x250**2 - 2*m.x240*m.x250 - 2*m.x239*m.x249
                           - 5.6664469849*m.b197 - 5.6664469849*m.b213 >= -5.6664469849)

m.c2594 = Constraint(expr=m.x241**2 + m.x242**2 + m.x249**2 + m.x250**2 - 2*m.x241*m.x249 - 2*m.x242*m.x250
                           - 5.6664469849*m.b201 - 5.6664469849*m.b213 >= -5.6664469849)

m.c2595 = Constraint(expr=m.x243**2 + m.x244**2 + m.x249**2 + m.x250**2 - 2*m.x243*m.x249 - 2*m.x244*m.x250
                           - 5.6664469849*m.b205 - 5.6664469849*m.b213 >= -5.6664469849)

m.c2596 = Constraint(expr=m.x245**2 + m.x246**2 + m.x249**2 + m.x250**2 - 2*m.x245*m.x249 - 2*m.x246*m.x250
                           - 5.6664469849*m.b209 - 5.6664469849*m.b213 >= -5.6664469849)

m.c2597 = Constraint(expr=m.x247**2 + m.x248**2 + m.x249**2 + m.x250**2 - 2*m.x247*m.x249 - 2*m.x248*m.x250
                           - 9.2934741904*m.b211 - 9.2934741904*m.b213 >= -9.2934741904)

m.c2598 = Constraint(expr=m.x215**2 + m.x216**2 + m.x217**2 + m.x218**2 - 2*m.x215*m.x217 - 2*m.x216*m.x218
                           - 1.436939228176*m.b70 - 1.436939228176*m.b79 >= -1.436939228176)

m.c2599 = Constraint(expr=m.x215**2 + m.x216**2 + m.x219**2 + m.x220**2 - 2*m.x215*m.x219 - 2*m.x216*m.x220
                           - 1.436939228176*m.b70 - 1.436939228176*m.b88 >= -1.436939228176)

m.c2600 = Constraint(expr=m.x215**2 + m.x216**2 + m.x221**2 + m.x222**2 - 2*m.x216*m.x222 - 2*m.x215*m.x221
                           - 1.436939228176*m.b70 - 1.436939228176*m.b97 >= -1.436939228176)

m.c2601 = Constraint(expr=m.x215**2 + m.x216**2 + m.x223**2 + m.x224**2 - 2*m.x216*m.x224 - 2*m.x215*m.x223
                           - 1.436939228176*m.b70 - 1.436939228176*m.b106 >= -1.436939228176)

m.c2602 = Constraint(expr=m.x215**2 + m.x216**2 + m.x225**2 + m.x226**2 - 2*m.x215*m.x225 - 2*m.x216*m.x226
                           - 1.436939228176*m.b70 - 1.436939228176*m.b115 >= -1.436939228176)

m.c2603 = Constraint(expr=m.x215**2 + m.x216**2 + m.x227**2 + m.x228**2 - 2*m.x216*m.x228 - 2*m.x215*m.x227
                           - 0.887203867225*m.b70 - 0.887203867225*m.b130 >= -0.887203867225)

m.c2604 = Constraint(expr=m.x215**2 + m.x216**2 + m.x229**2 + m.x230**2 - 2*m.x215*m.x229 - 2*m.x216*m.x230
                           - 0.887203867225*m.b70 - 0.887203867225*m.b145 >= -0.887203867225)

m.c2605 = Constraint(expr=m.x215**2 + m.x216**2 + m.x231**2 + m.x232**2 - 2*m.x216*m.x232 - 2*m.x215*m.x231
                           - 0.887203867225*m.b70 - 0.887203867225*m.b160 >= -0.887203867225)

m.c2606 = Constraint(expr=m.x215**2 + m.x216**2 + m.x233**2 + m.x234**2 - 2*m.x216*m.x234 - 2*m.x215*m.x233
                           - 0.887203867225*m.b70 - 0.887203867225*m.b175 >= -0.887203867225)

m.c2607 = Constraint(expr=m.x215**2 + m.x216**2 + m.x235**2 + m.x236**2 - 2*m.x216*m.x236 - 2*m.x215*m.x235
                           - 0.887203867225*m.b70 - 0.887203867225*m.b190 >= -0.887203867225)

m.c2608 = Constraint(expr=m.x215**2 + m.x216**2 + m.x237**2 + m.x238**2 - 2*m.x216*m.x238 - 2*m.x215*m.x237
                           - 2.118573403024*m.b70 - 2.118573403024*m.b194 >= -2.118573403024)

m.c2609 = Constraint(expr=m.x215**2 + m.x216**2 + m.x239**2 + m.x240**2 - 2*m.x215*m.x239 - 2*m.x216*m.x240
                           - 2.118573403024*m.b70 - 2.118573403024*m.b198 >= -2.118573403024)

m.c2610 = Constraint(expr=m.x215**2 + m.x216**2 + m.x241**2 + m.x242**2 - 2*m.x215*m.x241 - 2*m.x216*m.x242
                           - 2.118573403024*m.b70 - 2.118573403024*m.b202 >= -2.118573403024)

m.c2611 = Constraint(expr=m.x215**2 + m.x216**2 + m.x243**2 + m.x244**2 - 2*m.x215*m.x243 - 2*m.x216*m.x244
                           - 2.118573403024*m.b70 - 2.118573403024*m.b206 >= -2.118573403024)

m.c2612 = Constraint(expr=m.x215**2 + m.x216**2 + m.x245**2 + m.x246**2 - 2*m.x215*m.x245 - 2*m.x216*m.x246
                           - 2.118573403024*m.b70 - 2.118573403024*m.b210 >= -2.118573403024)

m.c2613 = Constraint(expr=m.x215**2 + m.x216**2 + m.x247**2 + m.x248**2 - 2*m.x215*m.x247 - 2*m.x216*m.x248
                           - 4.509770398884*m.b70 - 4.509770398884*m.b212 >= -4.509770398884)

m.c2614 = Constraint(expr=m.x215**2 + m.x216**2 + m.x249**2 + m.x250**2 - 2*m.x215*m.x249 - 2*m.x216*m.x250
                           - 4.509770398884*m.b70 - 4.509770398884*m.b214 >= -4.509770398884)

m.c2615 = Constraint(expr=m.x215**2 + m.x216**2 + m.x217**2 + m.x218**2 - 2*m.x215*m.x217 - 2*m.x216*m.x218
                           - 1.436939228176*m.b70 - 1.436939228176*m.b79 >= -1.436939228176)

m.c2616 = Constraint(expr=m.x217**2 + m.x218**2 + m.x219**2 + m.x220**2 - 2*m.x217*m.x219 - 2*m.x218*m.x220
                           - 1.436939228176*m.b79 - 1.436939228176*m.b88 >= -1.436939228176)

m.c2617 = Constraint(expr=m.x217**2 + m.x218**2 + m.x221**2 + m.x222**2 - 2*m.x218*m.x222 - 2*m.x217*m.x221
                           - 1.436939228176*m.b79 - 1.436939228176*m.b97 >= -1.436939228176)

m.c2618 = Constraint(expr=m.x217**2 + m.x218**2 + m.x223**2 + m.x224**2 - 2*m.x217*m.x223 - 2*m.x218*m.x224
                           - 1.436939228176*m.b79 - 1.436939228176*m.b106 >= -1.436939228176)

m.c2619 = Constraint(expr=m.x217**2 + m.x218**2 + m.x225**2 + m.x226**2 - 2*m.x218*m.x226 - 2*m.x217*m.x225
                           - 1.436939228176*m.b79 - 1.436939228176*m.b115 >= -1.436939228176)

m.c2620 = Constraint(expr=m.x217**2 + m.x218**2 + m.x227**2 + m.x228**2 - 2*m.x217*m.x227 - 2*m.x218*m.x228
                           - 0.887203867225*m.b79 - 0.887203867225*m.b130 >= -0.887203867225)

m.c2621 = Constraint(expr=m.x217**2 + m.x218**2 + m.x229**2 + m.x230**2 - 2*m.x218*m.x230 - 2*m.x217*m.x229
                           - 0.887203867225*m.b79 - 0.887203867225*m.b145 >= -0.887203867225)

m.c2622 = Constraint(expr=m.x217**2 + m.x218**2 + m.x231**2 + m.x232**2 - 2*m.x218*m.x232 - 2*m.x217*m.x231
                           - 0.887203867225*m.b79 - 0.887203867225*m.b160 >= -0.887203867225)

m.c2623 = Constraint(expr=m.x217**2 + m.x218**2 + m.x233**2 + m.x234**2 - 2*m.x218*m.x234 - 2*m.x217*m.x233
                           - 0.887203867225*m.b79 - 0.887203867225*m.b175 >= -0.887203867225)

m.c2624 = Constraint(expr=m.x217**2 + m.x218**2 + m.x235**2 + m.x236**2 - 2*m.x218*m.x236 - 2*m.x217*m.x235
                           - 0.887203867225*m.b79 - 0.887203867225*m.b190 >= -0.887203867225)

m.c2625 = Constraint(expr=m.x217**2 + m.x218**2 + m.x237**2 + m.x238**2 - 2*m.x218*m.x238 - 2*m.x217*m.x237
                           - 2.118573403024*m.b79 - 2.118573403024*m.b194 >= -2.118573403024)

m.c2626 = Constraint(expr=m.x217**2 + m.x218**2 + m.x239**2 + m.x240**2 - 2*m.x218*m.x240 - 2*m.x217*m.x239
                           - 2.118573403024*m.b79 - 2.118573403024*m.b198 >= -2.118573403024)

m.c2627 = Constraint(expr=m.x217**2 + m.x218**2 + m.x241**2 + m.x242**2 - 2*m.x217*m.x241 - 2*m.x218*m.x242
                           - 2.118573403024*m.b79 - 2.118573403024*m.b202 >= -2.118573403024)

m.c2628 = Constraint(expr=m.x217**2 + m.x218**2 + m.x243**2 + m.x244**2 - 2*m.x217*m.x243 - 2*m.x218*m.x244
                           - 2.118573403024*m.b79 - 2.118573403024*m.b206 >= -2.118573403024)

m.c2629 = Constraint(expr=m.x217**2 + m.x218**2 + m.x245**2 + m.x246**2 - 2*m.x217*m.x245 - 2*m.x218*m.x246
                           - 2.118573403024*m.b79 - 2.118573403024*m.b210 >= -2.118573403024)

m.c2630 = Constraint(expr=m.x217**2 + m.x218**2 + m.x247**2 + m.x248**2 - 2*m.x217*m.x247 - 2*m.x218*m.x248
                           - 4.509770398884*m.b79 - 4.509770398884*m.b212 >= -4.509770398884)

m.c2631 = Constraint(expr=m.x217**2 + m.x218**2 + m.x249**2 + m.x250**2 - 2*m.x217*m.x249 - 2*m.x218*m.x250
                           - 4.509770398884*m.b79 - 4.509770398884*m.b214 >= -4.509770398884)

m.c2632 = Constraint(expr=m.x215**2 + m.x216**2 + m.x219**2 + m.x220**2 - 2*m.x215*m.x219 - 2*m.x216*m.x220
                           - 1.436939228176*m.b70 - 1.436939228176*m.b88 >= -1.436939228176)

m.c2633 = Constraint(expr=m.x217**2 + m.x218**2 + m.x219**2 + m.x220**2 - 2*m.x217*m.x219 - 2*m.x218*m.x220
                           - 1.436939228176*m.b79 - 1.436939228176*m.b88 >= -1.436939228176)

m.c2634 = Constraint(expr=m.x219**2 + m.x220**2 + m.x221**2 + m.x222**2 - 2*m.x219*m.x221 - 2*m.x220*m.x222
                           - 1.436939228176*m.b88 - 1.436939228176*m.b97 >= -1.436939228176)

m.c2635 = Constraint(expr=m.x219**2 + m.x220**2 + m.x223**2 + m.x224**2 - 2*m.x220*m.x224 - 2*m.x219*m.x223
                           - 1.436939228176*m.b88 - 1.436939228176*m.b106 >= -1.436939228176)

m.c2636 = Constraint(expr=m.x219**2 + m.x220**2 + m.x225**2 + m.x226**2 - 2*m.x220*m.x226 - 2*m.x219*m.x225
                           - 1.436939228176*m.b88 - 1.436939228176*m.b115 >= -1.436939228176)

m.c2637 = Constraint(expr=m.x219**2 + m.x220**2 + m.x227**2 + m.x228**2 - 2*m.x220*m.x228 - 2*m.x219*m.x227
                           - 0.887203867225*m.b88 - 0.887203867225*m.b130 >= -0.887203867225)

m.c2638 = Constraint(expr=m.x219**2 + m.x220**2 + m.x229**2 + m.x230**2 - 2*m.x220*m.x230 - 2*m.x219*m.x229
                           - 0.887203867225*m.b88 - 0.887203867225*m.b145 >= -0.887203867225)

m.c2639 = Constraint(expr=m.x219**2 + m.x220**2 + m.x231**2 + m.x232**2 - 2*m.x219*m.x231 - 2*m.x220*m.x232
                           - 0.887203867225*m.b88 - 0.887203867225*m.b160 >= -0.887203867225)

m.c2640 = Constraint(expr=m.x219**2 + m.x220**2 + m.x233**2 + m.x234**2 - 2*m.x219*m.x233 - 2*m.x220*m.x234
                           - 0.887203867225*m.b88 - 0.887203867225*m.b175 >= -0.887203867225)

m.c2641 = Constraint(expr=m.x219**2 + m.x220**2 + m.x235**2 + m.x236**2 - 2*m.x219*m.x235 - 2*m.x220*m.x236
                           - 0.887203867225*m.b88 - 0.887203867225*m.b190 >= -0.887203867225)

m.c2642 = Constraint(expr=m.x219**2 + m.x220**2 + m.x237**2 + m.x238**2 - 2*m.x220*m.x238 - 2*m.x219*m.x237
                           - 2.118573403024*m.b88 - 2.118573403024*m.b194 >= -2.118573403024)

m.c2643 = Constraint(expr=m.x219**2 + m.x220**2 + m.x239**2 + m.x240**2 - 2*m.x220*m.x240 - 2*m.x219*m.x239
                           - 2.118573403024*m.b88 - 2.118573403024*m.b198 >= -2.118573403024)

m.c2644 = Constraint(expr=m.x219**2 + m.x220**2 + m.x241**2 + m.x242**2 - 2*m.x219*m.x241 - 2*m.x220*m.x242
                           - 2.118573403024*m.b88 - 2.118573403024*m.b202 >= -2.118573403024)

m.c2645 = Constraint(expr=m.x219**2 + m.x220**2 + m.x243**2 + m.x244**2 - 2*m.x219*m.x243 - 2*m.x220*m.x244
                           - 2.118573403024*m.b88 - 2.118573403024*m.b206 >= -2.118573403024)

m.c2646 = Constraint(expr=m.x219**2 + m.x220**2 + m.x245**2 + m.x246**2 - 2*m.x219*m.x245 - 2*m.x220*m.x246
                           - 2.118573403024*m.b88 - 2.118573403024*m.b210 >= -2.118573403024)

m.c2647 = Constraint(expr=m.x219**2 + m.x220**2 + m.x247**2 + m.x248**2 - 2*m.x219*m.x247 - 2*m.x220*m.x248
                           - 4.509770398884*m.b88 - 4.509770398884*m.b212 >= -4.509770398884)

m.c2648 = Constraint(expr=m.x219**2 + m.x220**2 + m.x249**2 + m.x250**2 - 2*m.x219*m.x249 - 2*m.x220*m.x250
                           - 4.509770398884*m.b88 - 4.509770398884*m.b214 >= -4.509770398884)

m.c2649 = Constraint(expr=m.x215**2 + m.x216**2 + m.x221**2 + m.x222**2 - 2*m.x216*m.x222 - 2*m.x215*m.x221
                           - 1.436939228176*m.b70 - 1.436939228176*m.b97 >= -1.436939228176)

m.c2650 = Constraint(expr=m.x217**2 + m.x218**2 + m.x221**2 + m.x222**2 - 2*m.x218*m.x222 - 2*m.x217*m.x221
                           - 1.436939228176*m.b79 - 1.436939228176*m.b97 >= -1.436939228176)

m.c2651 = Constraint(expr=m.x219**2 + m.x220**2 + m.x221**2 + m.x222**2 - 2*m.x219*m.x221 - 2*m.x220*m.x222
                           - 1.436939228176*m.b88 - 1.436939228176*m.b97 >= -1.436939228176)

m.c2652 = Constraint(expr=m.x221**2 + m.x222**2 + m.x223**2 + m.x224**2 - 2*m.x221*m.x223 - 2*m.x222*m.x224
                           - 1.436939228176*m.b97 - 1.436939228176*m.b106 >= -1.436939228176)

m.c2653 = Constraint(expr=m.x221**2 + m.x222**2 + m.x225**2 + m.x226**2 - 2*m.x221*m.x225 - 2*m.x222*m.x226
                           - 1.436939228176*m.b97 - 1.436939228176*m.b115 >= -1.436939228176)

m.c2654 = Constraint(expr=m.x221**2 + m.x222**2 + m.x227**2 + m.x228**2 - 2*m.x221*m.x227 - 2*m.x222*m.x228
                           - 0.887203867225*m.b97 - 0.887203867225*m.b130 >= -0.887203867225)

m.c2655 = Constraint(expr=m.x221**2 + m.x222**2 + m.x229**2 + m.x230**2 - 2*m.x221*m.x229 - 2*m.x222*m.x230
                           - 0.887203867225*m.b97 - 0.887203867225*m.b145 >= -0.887203867225)

m.c2656 = Constraint(expr=m.x221**2 + m.x222**2 + m.x231**2 + m.x232**2 - 2*m.x221*m.x231 - 2*m.x222*m.x232
                           - 0.887203867225*m.b97 - 0.887203867225*m.b160 >= -0.887203867225)

m.c2657 = Constraint(expr=m.x221**2 + m.x222**2 + m.x233**2 + m.x234**2 - 2*m.x221*m.x233 - 2*m.x222*m.x234
                           - 0.887203867225*m.b97 - 0.887203867225*m.b175 >= -0.887203867225)

m.c2658 = Constraint(expr=m.x221**2 + m.x222**2 + m.x235**2 + m.x236**2 - 2*m.x221*m.x235 - 2*m.x222*m.x236
                           - 0.887203867225*m.b97 - 0.887203867225*m.b190 >= -0.887203867225)

m.c2659 = Constraint(expr=m.x221**2 + m.x222**2 + m.x237**2 + m.x238**2 - 2*m.x221*m.x237 - 2*m.x222*m.x238
                           - 2.118573403024*m.b97 - 2.118573403024*m.b194 >= -2.118573403024)

m.c2660 = Constraint(expr=m.x221**2 + m.x222**2 + m.x239**2 + m.x240**2 - 2*m.x221*m.x239 - 2*m.x222*m.x240
                           - 2.118573403024*m.b97 - 2.118573403024*m.b198 >= -2.118573403024)

m.c2661 = Constraint(expr=m.x221**2 + m.x222**2 + m.x241**2 + m.x242**2 - 2*m.x221*m.x241 - 2*m.x222*m.x242
                           - 2.118573403024*m.b97 - 2.118573403024*m.b202 >= -2.118573403024)

m.c2662 = Constraint(expr=m.x221**2 + m.x222**2 + m.x243**2 + m.x244**2 - 2*m.x222*m.x244 - 2*m.x221*m.x243
                           - 2.118573403024*m.b97 - 2.118573403024*m.b206 >= -2.118573403024)

m.c2663 = Constraint(expr=m.x221**2 + m.x222**2 + m.x245**2 + m.x246**2 - 2*m.x222*m.x246 - 2*m.x221*m.x245
                           - 2.118573403024*m.b97 - 2.118573403024*m.b210 >= -2.118573403024)

m.c2664 = Constraint(expr=m.x221**2 + m.x222**2 + m.x247**2 + m.x248**2 - 2*m.x222*m.x248 - 2*m.x221*m.x247
                           - 4.509770398884*m.b97 - 4.509770398884*m.b212 >= -4.509770398884)

m.c2665 = Constraint(expr=m.x221**2 + m.x222**2 + m.x249**2 + m.x250**2 - 2*m.x221*m.x249 - 2*m.x222*m.x250
                           - 4.509770398884*m.b97 - 4.509770398884*m.b214 >= -4.509770398884)

m.c2666 = Constraint(expr=m.x215**2 + m.x216**2 + m.x223**2 + m.x224**2 - 2*m.x216*m.x224 - 2*m.x215*m.x223
                           - 1.436939228176*m.b70 - 1.436939228176*m.b106 >= -1.436939228176)

m.c2667 = Constraint(expr=m.x217**2 + m.x218**2 + m.x223**2 + m.x224**2 - 2*m.x217*m.x223 - 2*m.x218*m.x224
                           - 1.436939228176*m.b79 - 1.436939228176*m.b106 >= -1.436939228176)

m.c2668 = Constraint(expr=m.x219**2 + m.x220**2 + m.x223**2 + m.x224**2 - 2*m.x220*m.x224 - 2*m.x219*m.x223
                           - 1.436939228176*m.b88 - 1.436939228176*m.b106 >= -1.436939228176)

m.c2669 = Constraint(expr=m.x221**2 + m.x222**2 + m.x223**2 + m.x224**2 - 2*m.x221*m.x223 - 2*m.x222*m.x224
                           - 1.436939228176*m.b97 - 1.436939228176*m.b106 >= -1.436939228176)

m.c2670 = Constraint(expr=m.x223**2 + m.x224**2 + m.x225**2 + m.x226**2 - 2*m.x223*m.x225 - 2*m.x224*m.x226
                           - 1.436939228176*m.b106 - 1.436939228176*m.b115 >= -1.436939228176)

m.c2671 = Constraint(expr=m.x223**2 + m.x224**2 + m.x227**2 + m.x228**2 - 2*m.x223*m.x227 - 2*m.x224*m.x228
                           - 0.887203867225*m.b106 - 0.887203867225*m.b130 >= -0.887203867225)

m.c2672 = Constraint(expr=m.x223**2 + m.x224**2 + m.x229**2 + m.x230**2 - 2*m.x223*m.x229 - 2*m.x224*m.x230
                           - 0.887203867225*m.b106 - 0.887203867225*m.b145 >= -0.887203867225)

m.c2673 = Constraint(expr=m.x223**2 + m.x224**2 + m.x231**2 + m.x232**2 - 2*m.x223*m.x231 - 2*m.x224*m.x232
                           - 0.887203867225*m.b106 - 0.887203867225*m.b160 >= -0.887203867225)

m.c2674 = Constraint(expr=m.x223**2 + m.x224**2 + m.x233**2 + m.x234**2 - 2*m.x223*m.x233 - 2*m.x224*m.x234
                           - 0.887203867225*m.b106 - 0.887203867225*m.b175 >= -0.887203867225)

m.c2675 = Constraint(expr=m.x223**2 + m.x224**2 + m.x235**2 + m.x236**2 - 2*m.x223*m.x235 - 2*m.x224*m.x236
                           - 0.887203867225*m.b106 - 0.887203867225*m.b190 >= -0.887203867225)

m.c2676 = Constraint(expr=m.x223**2 + m.x224**2 + m.x237**2 + m.x238**2 - 2*m.x223*m.x237 - 2*m.x224*m.x238
                           - 2.118573403024*m.b106 - 2.118573403024*m.b194 >= -2.118573403024)

m.c2677 = Constraint(expr=m.x223**2 + m.x224**2 + m.x239**2 + m.x240**2 - 2*m.x223*m.x239 - 2*m.x224*m.x240
                           - 2.118573403024*m.b106 - 2.118573403024*m.b198 >= -2.118573403024)

m.c2678 = Constraint(expr=m.x223**2 + m.x224**2 + m.x241**2 + m.x242**2 - 2*m.x223*m.x241 - 2*m.x224*m.x242
                           - 2.118573403024*m.b106 - 2.118573403024*m.b202 >= -2.118573403024)

m.c2679 = Constraint(expr=m.x223**2 + m.x224**2 + m.x243**2 + m.x244**2 - 2*m.x224*m.x244 - 2*m.x223*m.x243
                           - 2.118573403024*m.b106 - 2.118573403024*m.b206 >= -2.118573403024)

m.c2680 = Constraint(expr=m.x223**2 + m.x224**2 + m.x245**2 + m.x246**2 - 2*m.x224*m.x246 - 2*m.x223*m.x245
                           - 2.118573403024*m.b106 - 2.118573403024*m.b210 >= -2.118573403024)

m.c2681 = Constraint(expr=m.x223**2 + m.x224**2 + m.x247**2 + m.x248**2 - 2*m.x223*m.x247 - 2*m.x224*m.x248
                           - 4.509770398884*m.b106 - 4.509770398884*m.b212 >= -4.509770398884)

m.c2682 = Constraint(expr=m.x223**2 + m.x224**2 + m.x249**2 + m.x250**2 - 2*m.x224*m.x250 - 2*m.x223*m.x249
                           - 4.509770398884*m.b106 - 4.509770398884*m.b214 >= -4.509770398884)

m.c2683 = Constraint(expr=m.x215**2 + m.x216**2 + m.x225**2 + m.x226**2 - 2*m.x215*m.x225 - 2*m.x216*m.x226
                           - 1.436939228176*m.b70 - 1.436939228176*m.b115 >= -1.436939228176)

m.c2684 = Constraint(expr=m.x217**2 + m.x218**2 + m.x225**2 + m.x226**2 - 2*m.x218*m.x226 - 2*m.x217*m.x225
                           - 1.436939228176*m.b79 - 1.436939228176*m.b115 >= -1.436939228176)

m.c2685 = Constraint(expr=m.x219**2 + m.x220**2 + m.x225**2 + m.x226**2 - 2*m.x220*m.x226 - 2*m.x219*m.x225
                           - 1.436939228176*m.b88 - 1.436939228176*m.b115 >= -1.436939228176)

m.c2686 = Constraint(expr=m.x221**2 + m.x222**2 + m.x225**2 + m.x226**2 - 2*m.x221*m.x225 - 2*m.x222*m.x226
                           - 1.436939228176*m.b97 - 1.436939228176*m.b115 >= -1.436939228176)

m.c2687 = Constraint(expr=m.x223**2 + m.x224**2 + m.x225**2 + m.x226**2 - 2*m.x223*m.x225 - 2*m.x224*m.x226
                           - 1.436939228176*m.b106 - 1.436939228176*m.b115 >= -1.436939228176)

m.c2688 = Constraint(expr=m.x225**2 + m.x226**2 + m.x227**2 + m.x228**2 - 2*m.x225*m.x227 - 2*m.x226*m.x228
                           - 0.887203867225*m.b115 - 0.887203867225*m.b130 >= -0.887203867225)

m.c2689 = Constraint(expr=m.x225**2 + m.x226**2 + m.x229**2 + m.x230**2 - 2*m.x225*m.x229 - 2*m.x226*m.x230
                           - 0.887203867225*m.b115 - 0.887203867225*m.b145 >= -0.887203867225)

m.c2690 = Constraint(expr=m.x225**2 + m.x226**2 + m.x231**2 + m.x232**2 - 2*m.x225*m.x231 - 2*m.x226*m.x232
                           - 0.887203867225*m.b115 - 0.887203867225*m.b160 >= -0.887203867225)

m.c2691 = Constraint(expr=m.x225**2 + m.x226**2 + m.x233**2 + m.x234**2 - 2*m.x225*m.x233 - 2*m.x226*m.x234
                           - 0.887203867225*m.b115 - 0.887203867225*m.b175 >= -0.887203867225)

m.c2692 = Constraint(expr=m.x225**2 + m.x226**2 + m.x235**2 + m.x236**2 - 2*m.x225*m.x235 - 2*m.x226*m.x236
                           - 0.887203867225*m.b115 - 0.887203867225*m.b190 >= -0.887203867225)

m.c2693 = Constraint(expr=m.x225**2 + m.x226**2 + m.x237**2 + m.x238**2 - 2*m.x225*m.x237 - 2*m.x226*m.x238
                           - 2.118573403024*m.b115 - 2.118573403024*m.b194 >= -2.118573403024)

m.c2694 = Constraint(expr=m.x225**2 + m.x226**2 + m.x239**2 + m.x240**2 - 2*m.x225*m.x239 - 2*m.x226*m.x240
                           - 2.118573403024*m.b115 - 2.118573403024*m.b198 >= -2.118573403024)

m.c2695 = Constraint(expr=m.x225**2 + m.x226**2 + m.x241**2 + m.x242**2 - 2*m.x226*m.x242 - 2*m.x225*m.x241
                           - 2.118573403024*m.b115 - 2.118573403024*m.b202 >= -2.118573403024)

m.c2696 = Constraint(expr=m.x225**2 + m.x226**2 + m.x243**2 + m.x244**2 - 2*m.x226*m.x244 - 2*m.x225*m.x243
                           - 2.118573403024*m.b115 - 2.118573403024*m.b206 >= -2.118573403024)

m.c2697 = Constraint(expr=m.x225**2 + m.x226**2 + m.x245**2 + m.x246**2 - 2*m.x225*m.x245 - 2*m.x226*m.x246
                           - 2.118573403024*m.b115 - 2.118573403024*m.b210 >= -2.118573403024)

m.c2698 = Constraint(expr=m.x225**2 + m.x226**2 + m.x247**2 + m.x248**2 - 2*m.x226*m.x248 - 2*m.x225*m.x247
                           - 4.509770398884*m.b115 - 4.509770398884*m.b212 >= -4.509770398884)

m.c2699 = Constraint(expr=m.x225**2 + m.x226**2 + m.x249**2 + m.x250**2 - 2*m.x225*m.x249 - 2*m.x226*m.x250
                           - 4.509770398884*m.b115 - 4.509770398884*m.b214 >= -4.509770398884)

m.c2700 = Constraint(expr=m.x215**2 + m.x216**2 + m.x227**2 + m.x228**2 - 2*m.x216*m.x228 - 2*m.x215*m.x227
                           - 0.887203867225*m.b70 - 0.887203867225*m.b130 >= -0.887203867225)

m.c2701 = Constraint(expr=m.x217**2 + m.x218**2 + m.x227**2 + m.x228**2 - 2*m.x217*m.x227 - 2*m.x218*m.x228
                           - 0.887203867225*m.b79 - 0.887203867225*m.b130 >= -0.887203867225)

m.c2702 = Constraint(expr=m.x219**2 + m.x220**2 + m.x227**2 + m.x228**2 - 2*m.x220*m.x228 - 2*m.x219*m.x227
                           - 0.887203867225*m.b88 - 0.887203867225*m.b130 >= -0.887203867225)

m.c2703 = Constraint(expr=m.x221**2 + m.x222**2 + m.x227**2 + m.x228**2 - 2*m.x221*m.x227 - 2*m.x222*m.x228
                           - 0.887203867225*m.b97 - 0.887203867225*m.b130 >= -0.887203867225)

m.c2704 = Constraint(expr=m.x223**2 + m.x224**2 + m.x227**2 + m.x228**2 - 2*m.x223*m.x227 - 2*m.x224*m.x228
                           - 0.887203867225*m.b106 - 0.887203867225*m.b130 >= -0.887203867225)

m.c2705 = Constraint(expr=m.x225**2 + m.x226**2 + m.x227**2 + m.x228**2 - 2*m.x225*m.x227 - 2*m.x226*m.x228
                           - 0.887203867225*m.b115 - 0.887203867225*m.b130 >= -0.887203867225)

m.c2706 = Constraint(expr=m.x227**2 + m.x228**2 + m.x229**2 + m.x230**2 - 2*m.x227*m.x229 - 2*m.x228*m.x230
                           - 0.469370231236*m.b130 - 0.469370231236*m.b145 >= -0.469370231236)

m.c2707 = Constraint(expr=m.x227**2 + m.x228**2 + m.x231**2 + m.x232**2 - 2*m.x227*m.x231 - 2*m.x228*m.x232
                           - 0.469370231236*m.b130 - 0.469370231236*m.b160 >= -0.469370231236)

m.c2708 = Constraint(expr=m.x227**2 + m.x228**2 + m.x233**2 + m.x234**2 - 2*m.x227*m.x233 - 2*m.x228*m.x234
                           - 0.469370231236*m.b130 - 0.469370231236*m.b175 >= -0.469370231236)

m.c2709 = Constraint(expr=m.x227**2 + m.x228**2 + m.x235**2 + m.x236**2 - 2*m.x227*m.x235 - 2*m.x228*m.x236
                           - 0.469370231236*m.b130 - 0.469370231236*m.b190 >= -0.469370231236)

m.c2710 = Constraint(expr=m.x227**2 + m.x228**2 + m.x237**2 + m.x238**2 - 2*m.x227*m.x237 - 2*m.x228*m.x238
                           - 1.436936830729*m.b130 - 1.436936830729*m.b194 >= -1.436936830729)

m.c2711 = Constraint(expr=m.x227**2 + m.x228**2 + m.x239**2 + m.x240**2 - 2*m.x227*m.x239 - 2*m.x228*m.x240
                           - 1.436936830729*m.b130 - 1.436936830729*m.b198 >= -1.436936830729)

m.c2712 = Constraint(expr=m.x227**2 + m.x228**2 + m.x241**2 + m.x242**2 - 2*m.x227*m.x241 - 2*m.x228*m.x242
                           - 1.436936830729*m.b130 - 1.436936830729*m.b202 >= -1.436936830729)

m.c2713 = Constraint(expr=m.x227**2 + m.x228**2 + m.x243**2 + m.x244**2 - 2*m.x228*m.x244 - 2*m.x227*m.x243
                           - 1.436936830729*m.b130 - 1.436936830729*m.b206 >= -1.436936830729)

m.c2714 = Constraint(expr=m.x227**2 + m.x228**2 + m.x245**2 + m.x246**2 - 2*m.x228*m.x246 - 2*m.x227*m.x245
                           - 1.436936830729*m.b130 - 1.436936830729*m.b210 >= -1.436936830729)

m.c2715 = Constraint(expr=m.x227**2 + m.x228**2 + m.x247**2 + m.x248**2 - 2*m.x227*m.x247 - 2*m.x228*m.x248
                           - 3.484990776969*m.b130 - 3.484990776969*m.b212 >= -3.484990776969)

m.c2716 = Constraint(expr=m.x227**2 + m.x228**2 + m.x249**2 + m.x250**2 - 2*m.x228*m.x250 - 2*m.x227*m.x249
                           - 3.484990776969*m.b130 - 3.484990776969*m.b214 >= -3.484990776969)

m.c2717 = Constraint(expr=m.x215**2 + m.x216**2 + m.x229**2 + m.x230**2 - 2*m.x215*m.x229 - 2*m.x216*m.x230
                           - 0.887203867225*m.b70 - 0.887203867225*m.b145 >= -0.887203867225)

m.c2718 = Constraint(expr=m.x217**2 + m.x218**2 + m.x229**2 + m.x230**2 - 2*m.x218*m.x230 - 2*m.x217*m.x229
                           - 0.887203867225*m.b79 - 0.887203867225*m.b145 >= -0.887203867225)

m.c2719 = Constraint(expr=m.x219**2 + m.x220**2 + m.x229**2 + m.x230**2 - 2*m.x220*m.x230 - 2*m.x219*m.x229
                           - 0.887203867225*m.b88 - 0.887203867225*m.b145 >= -0.887203867225)

m.c2720 = Constraint(expr=m.x221**2 + m.x222**2 + m.x229**2 + m.x230**2 - 2*m.x221*m.x229 - 2*m.x222*m.x230
                           - 0.887203867225*m.b97 - 0.887203867225*m.b145 >= -0.887203867225)

m.c2721 = Constraint(expr=m.x223**2 + m.x224**2 + m.x229**2 + m.x230**2 - 2*m.x223*m.x229 - 2*m.x224*m.x230
                           - 0.887203867225*m.b106 - 0.887203867225*m.b145 >= -0.887203867225)

m.c2722 = Constraint(expr=m.x225**2 + m.x226**2 + m.x229**2 + m.x230**2 - 2*m.x225*m.x229 - 2*m.x226*m.x230
                           - 0.887203867225*m.b115 - 0.887203867225*m.b145 >= -0.887203867225)

m.c2723 = Constraint(expr=m.x227**2 + m.x228**2 + m.x229**2 + m.x230**2 - 2*m.x227*m.x229 - 2*m.x228*m.x230
                           - 0.469370231236*m.b130 - 0.469370231236*m.b145 >= -0.469370231236)

m.c2724 = Constraint(expr=m.x229**2 + m.x230**2 + m.x231**2 + m.x232**2 - 2*m.x229*m.x231 - 2*m.x230*m.x232
                           - 0.469370231236*m.b145 - 0.469370231236*m.b160 >= -0.469370231236)

m.c2725 = Constraint(expr=m.x229**2 + m.x230**2 + m.x233**2 + m.x234**2 - 2*m.x229*m.x233 - 2*m.x230*m.x234
                           - 0.469370231236*m.b145 - 0.469370231236*m.b175 >= -0.469370231236)

m.c2726 = Constraint(expr=m.x229**2 + m.x230**2 + m.x235**2 + m.x236**2 - 2*m.x229*m.x235 - 2*m.x230*m.x236
                           - 0.469370231236*m.b145 - 0.469370231236*m.b190 >= -0.469370231236)

m.c2727 = Constraint(expr=m.x229**2 + m.x230**2 + m.x237**2 + m.x238**2 - 2*m.x229*m.x237 - 2*m.x230*m.x238
                           - 1.436936830729*m.b145 - 1.436936830729*m.b194 >= -1.436936830729)

m.c2728 = Constraint(expr=m.x229**2 + m.x230**2 + m.x239**2 + m.x240**2 - 2*m.x229*m.x239 - 2*m.x230*m.x240
                           - 1.436936830729*m.b145 - 1.436936830729*m.b198 >= -1.436936830729)

m.c2729 = Constraint(expr=m.x229**2 + m.x230**2 + m.x241**2 + m.x242**2 - 2*m.x229*m.x241 - 2*m.x230*m.x242
                           - 1.436936830729*m.b145 - 1.436936830729*m.b202 >= -1.436936830729)

m.c2730 = Constraint(expr=m.x229**2 + m.x230**2 + m.x243**2 + m.x244**2 - 2*m.x230*m.x244 - 2*m.x229*m.x243
                           - 1.436936830729*m.b145 - 1.436936830729*m.b206 >= -1.436936830729)

m.c2731 = Constraint(expr=m.x229**2 + m.x230**2 + m.x245**2 + m.x246**2 - 2*m.x229*m.x245 - 2*m.x230*m.x246
                           - 1.436936830729*m.b145 - 1.436936830729*m.b210 >= -1.436936830729)

m.c2732 = Constraint(expr=m.x229**2 + m.x230**2 + m.x247**2 + m.x248**2 - 2*m.x230*m.x248 - 2*m.x229*m.x247
                           - 3.484990776969*m.b145 - 3.484990776969*m.b212 >= -3.484990776969)

m.c2733 = Constraint(expr=m.x229**2 + m.x230**2 + m.x249**2 + m.x250**2 - 2*m.x229*m.x249 - 2*m.x230*m.x250
                           - 3.484990776969*m.b145 - 3.484990776969*m.b214 >= -3.484990776969)

m.c2734 = Constraint(expr=m.x215**2 + m.x216**2 + m.x231**2 + m.x232**2 - 2*m.x216*m.x232 - 2*m.x215*m.x231
                           - 0.887203867225*m.b70 - 0.887203867225*m.b160 >= -0.887203867225)

m.c2735 = Constraint(expr=m.x217**2 + m.x218**2 + m.x231**2 + m.x232**2 - 2*m.x218*m.x232 - 2*m.x217*m.x231
                           - 0.887203867225*m.b79 - 0.887203867225*m.b160 >= -0.887203867225)

m.c2736 = Constraint(expr=m.x219**2 + m.x220**2 + m.x231**2 + m.x232**2 - 2*m.x219*m.x231 - 2*m.x220*m.x232
                           - 0.887203867225*m.b88 - 0.887203867225*m.b160 >= -0.887203867225)

m.c2737 = Constraint(expr=m.x221**2 + m.x222**2 + m.x231**2 + m.x232**2 - 2*m.x221*m.x231 - 2*m.x222*m.x232
                           - 0.887203867225*m.b97 - 0.887203867225*m.b160 >= -0.887203867225)

m.c2738 = Constraint(expr=m.x223**2 + m.x224**2 + m.x231**2 + m.x232**2 - 2*m.x223*m.x231 - 2*m.x224*m.x232
                           - 0.887203867225*m.b106 - 0.887203867225*m.b160 >= -0.887203867225)

m.c2739 = Constraint(expr=m.x225**2 + m.x226**2 + m.x231**2 + m.x232**2 - 2*m.x225*m.x231 - 2*m.x226*m.x232
                           - 0.887203867225*m.b115 - 0.887203867225*m.b160 >= -0.887203867225)

m.c2740 = Constraint(expr=m.x227**2 + m.x228**2 + m.x231**2 + m.x232**2 - 2*m.x227*m.x231 - 2*m.x228*m.x232
                           - 0.469370231236*m.b130 - 0.469370231236*m.b160 >= -0.469370231236)

m.c2741 = Constraint(expr=m.x229**2 + m.x230**2 + m.x231**2 + m.x232**2 - 2*m.x229*m.x231 - 2*m.x230*m.x232
                           - 0.469370231236*m.b145 - 0.469370231236*m.b160 >= -0.469370231236)

m.c2742 = Constraint(expr=m.x231**2 + m.x232**2 + m.x233**2 + m.x234**2 - 2*m.x231*m.x233 - 2*m.x232*m.x234
                           - 0.469370231236*m.b160 - 0.469370231236*m.b175 >= -0.469370231236)

m.c2743 = Constraint(expr=m.x231**2 + m.x232**2 + m.x235**2 + m.x236**2 - 2*m.x231*m.x235 - 2*m.x232*m.x236
                           - 0.469370231236*m.b160 - 0.469370231236*m.b190 >= -0.469370231236)

m.c2744 = Constraint(expr=m.x231**2 + m.x232**2 + m.x237**2 + m.x238**2 - 2*m.x231*m.x237 - 2*m.x232*m.x238
                           - 1.436936830729*m.b160 - 1.436936830729*m.b194 >= -1.436936830729)

m.c2745 = Constraint(expr=m.x231**2 + m.x232**2 + m.x239**2 + m.x240**2 - 2*m.x231*m.x239 - 2*m.x232*m.x240
                           - 1.436936830729*m.b160 - 1.436936830729*m.b198 >= -1.436936830729)

m.c2746 = Constraint(expr=m.x231**2 + m.x232**2 + m.x241**2 + m.x242**2 - 2*m.x232*m.x242 - 2*m.x231*m.x241
                           - 1.436936830729*m.b160 - 1.436936830729*m.b202 >= -1.436936830729)

m.c2747 = Constraint(expr=m.x231**2 + m.x232**2 + m.x243**2 + m.x244**2 - 2*m.x231*m.x243 - 2*m.x232*m.x244
                           - 1.436936830729*m.b160 - 1.436936830729*m.b206 >= -1.436936830729)

m.c2748 = Constraint(expr=m.x231**2 + m.x232**2 + m.x245**2 + m.x246**2 - 2*m.x232*m.x246 - 2*m.x231*m.x245
                           - 1.436936830729*m.b160 - 1.436936830729*m.b210 >= -1.436936830729)

m.c2749 = Constraint(expr=m.x231**2 + m.x232**2 + m.x247**2 + m.x248**2 - 2*m.x231*m.x247 - 2*m.x232*m.x248
                           - 3.484990776969*m.b160 - 3.484990776969*m.b212 >= -3.484990776969)

m.c2750 = Constraint(expr=m.x231**2 + m.x232**2 + m.x249**2 + m.x250**2 - 2*m.x232*m.x250 - 2*m.x231*m.x249
                           - 3.484990776969*m.b160 - 3.484990776969*m.b214 >= -3.484990776969)

m.c2751 = Constraint(expr=m.x215**2 + m.x216**2 + m.x233**2 + m.x234**2 - 2*m.x216*m.x234 - 2*m.x215*m.x233
                           - 0.887203867225*m.b70 - 0.887203867225*m.b175 >= -0.887203867225)

m.c2752 = Constraint(expr=m.x217**2 + m.x218**2 + m.x233**2 + m.x234**2 - 2*m.x217*m.x233 - 2*m.x218*m.x234
                           - 0.887203867225*m.b79 - 0.887203867225*m.b175 >= -0.887203867225)

m.c2753 = Constraint(expr=m.x219**2 + m.x220**2 + m.x233**2 + m.x234**2 - 2*m.x219*m.x233 - 2*m.x220*m.x234
                           - 0.887203867225*m.b88 - 0.887203867225*m.b175 >= -0.887203867225)

m.c2754 = Constraint(expr=m.x221**2 + m.x222**2 + m.x233**2 + m.x234**2 - 2*m.x221*m.x233 - 2*m.x222*m.x234
                           - 0.887203867225*m.b97 - 0.887203867225*m.b175 >= -0.887203867225)

m.c2755 = Constraint(expr=m.x223**2 + m.x224**2 + m.x233**2 + m.x234**2 - 2*m.x223*m.x233 - 2*m.x224*m.x234
                           - 0.887203867225*m.b106 - 0.887203867225*m.b175 >= -0.887203867225)

m.c2756 = Constraint(expr=m.x225**2 + m.x226**2 + m.x233**2 + m.x234**2 - 2*m.x225*m.x233 - 2*m.x226*m.x234
                           - 0.887203867225*m.b115 - 0.887203867225*m.b175 >= -0.887203867225)

m.c2757 = Constraint(expr=m.x227**2 + m.x228**2 + m.x233**2 + m.x234**2 - 2*m.x227*m.x233 - 2*m.x228*m.x234
                           - 0.469370231236*m.b130 - 0.469370231236*m.b175 >= -0.469370231236)

m.c2758 = Constraint(expr=m.x229**2 + m.x230**2 + m.x233**2 + m.x234**2 - 2*m.x229*m.x233 - 2*m.x230*m.x234
                           - 0.469370231236*m.b145 - 0.469370231236*m.b175 >= -0.469370231236)

m.c2759 = Constraint(expr=m.x231**2 + m.x232**2 + m.x233**2 + m.x234**2 - 2*m.x231*m.x233 - 2*m.x232*m.x234
                           - 0.469370231236*m.b160 - 0.469370231236*m.b175 >= -0.469370231236)

m.c2760 = Constraint(expr=m.x233**2 + m.x234**2 + m.x235**2 + m.x236**2 - 2*m.x233*m.x235 - 2*m.x234*m.x236
                           - 0.469370231236*m.b175 - 0.469370231236*m.b190 >= -0.469370231236)

m.c2761 = Constraint(expr=m.x233**2 + m.x234**2 + m.x237**2 + m.x238**2 - 2*m.x233*m.x237 - 2*m.x234*m.x238
                           - 1.436936830729*m.b175 - 1.436936830729*m.b194 >= -1.436936830729)

m.c2762 = Constraint(expr=m.x233**2 + m.x234**2 + m.x239**2 + m.x240**2 - 2*m.x233*m.x239 - 2*m.x234*m.x240
                           - 1.436936830729*m.b175 - 1.436936830729*m.b198 >= -1.436936830729)

m.c2763 = Constraint(expr=m.x233**2 + m.x234**2 + m.x241**2 + m.x242**2 - 2*m.x233*m.x241 - 2*m.x234*m.x242
                           - 1.436936830729*m.b175 - 1.436936830729*m.b202 >= -1.436936830729)

m.c2764 = Constraint(expr=m.x233**2 + m.x234**2 + m.x243**2 + m.x244**2 - 2*m.x234*m.x244 - 2*m.x233*m.x243
                           - 1.436936830729*m.b175 - 1.436936830729*m.b206 >= -1.436936830729)

m.c2765 = Constraint(expr=m.x233**2 + m.x234**2 + m.x245**2 + m.x246**2 - 2*m.x233*m.x245 - 2*m.x234*m.x246
                           - 1.436936830729*m.b175 - 1.436936830729*m.b210 >= -1.436936830729)

m.c2766 = Constraint(expr=m.x233**2 + m.x234**2 + m.x247**2 + m.x248**2 - 2*m.x234*m.x248 - 2*m.x233*m.x247
                           - 3.484990776969*m.b175 - 3.484990776969*m.b212 >= -3.484990776969)

m.c2767 = Constraint(expr=m.x233**2 + m.x234**2 + m.x249**2 + m.x250**2 - 2*m.x234*m.x250 - 2*m.x233*m.x249
                           - 3.484990776969*m.b175 - 3.484990776969*m.b214 >= -3.484990776969)

m.c2768 = Constraint(expr=m.x215**2 + m.x216**2 + m.x235**2 + m.x236**2 - 2*m.x216*m.x236 - 2*m.x215*m.x235
                           - 0.887203867225*m.b70 - 0.887203867225*m.b190 >= -0.887203867225)

m.c2769 = Constraint(expr=m.x217**2 + m.x218**2 + m.x235**2 + m.x236**2 - 2*m.x217*m.x235 - 2*m.x218*m.x236
                           - 0.887203867225*m.b79 - 0.887203867225*m.b190 >= -0.887203867225)

m.c2770 = Constraint(expr=m.x219**2 + m.x220**2 + m.x235**2 + m.x236**2 - 2*m.x219*m.x235 - 2*m.x220*m.x236
                           - 0.887203867225*m.b88 - 0.887203867225*m.b190 >= -0.887203867225)

m.c2771 = Constraint(expr=m.x221**2 + m.x222**2 + m.x235**2 + m.x236**2 - 2*m.x221*m.x235 - 2*m.x222*m.x236
                           - 0.887203867225*m.b97 - 0.887203867225*m.b190 >= -0.887203867225)

m.c2772 = Constraint(expr=m.x223**2 + m.x224**2 + m.x235**2 + m.x236**2 - 2*m.x223*m.x235 - 2*m.x224*m.x236
                           - 0.887203867225*m.b106 - 0.887203867225*m.b190 >= -0.887203867225)

m.c2773 = Constraint(expr=m.x225**2 + m.x226**2 + m.x235**2 + m.x236**2 - 2*m.x225*m.x235 - 2*m.x226*m.x236
                           - 0.887203867225*m.b115 - 0.887203867225*m.b190 >= -0.887203867225)

m.c2774 = Constraint(expr=m.x227**2 + m.x228**2 + m.x235**2 + m.x236**2 - 2*m.x227*m.x235 - 2*m.x228*m.x236
                           - 0.469370231236*m.b130 - 0.469370231236*m.b190 >= -0.469370231236)

m.c2775 = Constraint(expr=m.x229**2 + m.x230**2 + m.x235**2 + m.x236**2 - 2*m.x229*m.x235 - 2*m.x230*m.x236
                           - 0.469370231236*m.b145 - 0.469370231236*m.b190 >= -0.469370231236)

m.c2776 = Constraint(expr=m.x231**2 + m.x232**2 + m.x235**2 + m.x236**2 - 2*m.x231*m.x235 - 2*m.x232*m.x236
                           - 0.469370231236*m.b160 - 0.469370231236*m.b190 >= -0.469370231236)

m.c2777 = Constraint(expr=m.x233**2 + m.x234**2 + m.x235**2 + m.x236**2 - 2*m.x233*m.x235 - 2*m.x234*m.x236
                           - 0.469370231236*m.b175 - 0.469370231236*m.b190 >= -0.469370231236)

m.c2778 = Constraint(expr=m.x235**2 + m.x236**2 + m.x237**2 + m.x238**2 - 2*m.x235*m.x237 - 2*m.x236*m.x238
                           - 1.436936830729*m.b190 - 1.436936830729*m.b194 >= -1.436936830729)

m.c2779 = Constraint(expr=m.x235**2 + m.x236**2 + m.x239**2 + m.x240**2 - 2*m.x235*m.x239 - 2*m.x236*m.x240
                           - 1.436936830729*m.b190 - 1.436936830729*m.b198 >= -1.436936830729)

m.c2780 = Constraint(expr=m.x235**2 + m.x236**2 + m.x241**2 + m.x242**2 - 2*m.x236*m.x242 - 2*m.x235*m.x241
                           - 1.436936830729*m.b190 - 1.436936830729*m.b202 >= -1.436936830729)

m.c2781 = Constraint(expr=m.x235**2 + m.x236**2 + m.x243**2 + m.x244**2 - 2*m.x235*m.x243 - 2*m.x236*m.x244
                           - 1.436936830729*m.b190 - 1.436936830729*m.b206 >= -1.436936830729)

m.c2782 = Constraint(expr=m.x235**2 + m.x236**2 + m.x245**2 + m.x246**2 - 2*m.x236*m.x246 - 2*m.x235*m.x245
                           - 1.436936830729*m.b190 - 1.436936830729*m.b210 >= -1.436936830729)

m.c2783 = Constraint(expr=m.x235**2 + m.x236**2 + m.x247**2 + m.x248**2 - 2*m.x236*m.x248 - 2*m.x235*m.x247
                           - 3.484990776969*m.b190 - 3.484990776969*m.b212 >= -3.484990776969)

m.c2784 = Constraint(expr=m.x235**2 + m.x236**2 + m.x249**2 + m.x250**2 - 2*m.x235*m.x249 - 2*m.x236*m.x250
                           - 3.484990776969*m.b190 - 3.484990776969*m.b214 >= -3.484990776969)

m.c2785 = Constraint(expr=m.x215**2 + m.x216**2 + m.x237**2 + m.x238**2 - 2*m.x216*m.x238 - 2*m.x215*m.x237
                           - 2.118573403024*m.b70 - 2.118573403024*m.b194 >= -2.118573403024)

m.c2786 = Constraint(expr=m.x217**2 + m.x218**2 + m.x237**2 + m.x238**2 - 2*m.x218*m.x238 - 2*m.x217*m.x237
                           - 2.118573403024*m.b79 - 2.118573403024*m.b194 >= -2.118573403024)

m.c2787 = Constraint(expr=m.x219**2 + m.x220**2 + m.x237**2 + m.x238**2 - 2*m.x220*m.x238 - 2*m.x219*m.x237
                           - 2.118573403024*m.b88 - 2.118573403024*m.b194 >= -2.118573403024)

m.c2788 = Constraint(expr=m.x221**2 + m.x222**2 + m.x237**2 + m.x238**2 - 2*m.x221*m.x237 - 2*m.x222*m.x238
                           - 2.118573403024*m.b97 - 2.118573403024*m.b194 >= -2.118573403024)

m.c2789 = Constraint(expr=m.x223**2 + m.x224**2 + m.x237**2 + m.x238**2 - 2*m.x223*m.x237 - 2*m.x224*m.x238
                           - 2.118573403024*m.b106 - 2.118573403024*m.b194 >= -2.118573403024)

m.c2790 = Constraint(expr=m.x225**2 + m.x226**2 + m.x237**2 + m.x238**2 - 2*m.x225*m.x237 - 2*m.x226*m.x238
                           - 2.118573403024*m.b115 - 2.118573403024*m.b194 >= -2.118573403024)

m.c2791 = Constraint(expr=m.x227**2 + m.x228**2 + m.x237**2 + m.x238**2 - 2*m.x227*m.x237 - 2*m.x228*m.x238
                           - 1.436936830729*m.b130 - 1.436936830729*m.b194 >= -1.436936830729)

m.c2792 = Constraint(expr=m.x229**2 + m.x230**2 + m.x237**2 + m.x238**2 - 2*m.x229*m.x237 - 2*m.x230*m.x238
                           - 1.436936830729*m.b145 - 1.436936830729*m.b194 >= -1.436936830729)

m.c2793 = Constraint(expr=m.x231**2 + m.x232**2 + m.x237**2 + m.x238**2 - 2*m.x231*m.x237 - 2*m.x232*m.x238
                           - 1.436936830729*m.b160 - 1.436936830729*m.b194 >= -1.436936830729)

m.c2794 = Constraint(expr=m.x233**2 + m.x234**2 + m.x237**2 + m.x238**2 - 2*m.x233*m.x237 - 2*m.x234*m.x238
                           - 1.436936830729*m.b175 - 1.436936830729*m.b194 >= -1.436936830729)

m.c2795 = Constraint(expr=m.x235**2 + m.x236**2 + m.x237**2 + m.x238**2 - 2*m.x235*m.x237 - 2*m.x236*m.x238
                           - 1.436936830729*m.b190 - 1.436936830729*m.b194 >= -1.436936830729)

m.c2796 = Constraint(expr=m.x237**2 + m.x238**2 + m.x239**2 + m.x240**2 - 2*m.x237*m.x239 - 2*m.x238*m.x240
                           - 2.9321082756*m.b194 - 2.9321082756*m.b198 >= -2.9321082756)

m.c2797 = Constraint(expr=m.x237**2 + m.x238**2 + m.x241**2 + m.x242**2 - 2*m.x237*m.x241 - 2*m.x238*m.x242
                           - 2.9321082756*m.b194 - 2.9321082756*m.b202 >= -2.9321082756)

m.c2798 = Constraint(expr=m.x237**2 + m.x238**2 + m.x243**2 + m.x244**2 - 2*m.x238*m.x244 - 2*m.x237*m.x243
                           - 2.9321082756*m.b194 - 2.9321082756*m.b206 >= -2.9321082756)

m.c2799 = Constraint(expr=m.x237**2 + m.x238**2 + m.x245**2 + m.x246**2 - 2*m.x238*m.x246 - 2*m.x237*m.x245
                           - 2.9321082756*m.b194 - 2.9321082756*m.b210 >= -2.9321082756)

m.c2800 = Constraint(expr=m.x237**2 + m.x238**2 + m.x247**2 + m.x248**2 - 2*m.x237*m.x247 - 2*m.x238*m.x248
                           - 5.6664469849*m.b194 - 5.6664469849*m.b212 >= -5.6664469849)

m.c2801 = Constraint(expr=m.x237**2 + m.x238**2 + m.x249**2 + m.x250**2 - 2*m.x238*m.x250 - 2*m.x237*m.x249
                           - 5.6664469849*m.b194 - 5.6664469849*m.b214 >= -5.6664469849)

m.c2802 = Constraint(expr=m.x215**2 + m.x216**2 + m.x239**2 + m.x240**2 - 2*m.x215*m.x239 - 2*m.x216*m.x240
                           - 2.118573403024*m.b70 - 2.118573403024*m.b198 >= -2.118573403024)

m.c2803 = Constraint(expr=m.x217**2 + m.x218**2 + m.x239**2 + m.x240**2 - 2*m.x218*m.x240 - 2*m.x217*m.x239
                           - 2.118573403024*m.b79 - 2.118573403024*m.b198 >= -2.118573403024)

m.c2804 = Constraint(expr=m.x219**2 + m.x220**2 + m.x239**2 + m.x240**2 - 2*m.x220*m.x240 - 2*m.x219*m.x239
                           - 2.118573403024*m.b88 - 2.118573403024*m.b198 >= -2.118573403024)

m.c2805 = Constraint(expr=m.x221**2 + m.x222**2 + m.x239**2 + m.x240**2 - 2*m.x221*m.x239 - 2*m.x222*m.x240
                           - 2.118573403024*m.b97 - 2.118573403024*m.b198 >= -2.118573403024)

m.c2806 = Constraint(expr=m.x223**2 + m.x224**2 + m.x239**2 + m.x240**2 - 2*m.x223*m.x239 - 2*m.x224*m.x240
                           - 2.118573403024*m.b106 - 2.118573403024*m.b198 >= -2.118573403024)

m.c2807 = Constraint(expr=m.x225**2 + m.x226**2 + m.x239**2 + m.x240**2 - 2*m.x225*m.x239 - 2*m.x226*m.x240
                           - 2.118573403024*m.b115 - 2.118573403024*m.b198 >= -2.118573403024)

m.c2808 = Constraint(expr=m.x227**2 + m.x228**2 + m.x239**2 + m.x240**2 - 2*m.x227*m.x239 - 2*m.x228*m.x240
                           - 1.436936830729*m.b130 - 1.436936830729*m.b198 >= -1.436936830729)

m.c2809 = Constraint(expr=m.x229**2 + m.x230**2 + m.x239**2 + m.x240**2 - 2*m.x229*m.x239 - 2*m.x230*m.x240
                           - 1.436936830729*m.b145 - 1.436936830729*m.b198 >= -1.436936830729)

m.c2810 = Constraint(expr=m.x231**2 + m.x232**2 + m.x239**2 + m.x240**2 - 2*m.x231*m.x239 - 2*m.x232*m.x240
                           - 1.436936830729*m.b160 - 1.436936830729*m.b198 >= -1.436936830729)

m.c2811 = Constraint(expr=m.x233**2 + m.x234**2 + m.x239**2 + m.x240**2 - 2*m.x233*m.x239 - 2*m.x234*m.x240
                           - 1.436936830729*m.b175 - 1.436936830729*m.b198 >= -1.436936830729)

m.c2812 = Constraint(expr=m.x235**2 + m.x236**2 + m.x239**2 + m.x240**2 - 2*m.x235*m.x239 - 2*m.x236*m.x240
                           - 1.436936830729*m.b190 - 1.436936830729*m.b198 >= -1.436936830729)

m.c2813 = Constraint(expr=m.x237**2 + m.x238**2 + m.x239**2 + m.x240**2 - 2*m.x237*m.x239 - 2*m.x238*m.x240
                           - 2.9321082756*m.b194 - 2.9321082756*m.b198 >= -2.9321082756)

m.c2814 = Constraint(expr=m.x239**2 + m.x240**2 + m.x241**2 + m.x242**2 - 2*m.x240*m.x242 - 2*m.x239*m.x241
                           - 2.9321082756*m.b198 - 2.9321082756*m.b202 >= -2.9321082756)

m.c2815 = Constraint(expr=m.x239**2 + m.x240**2 + m.x243**2 + m.x244**2 - 2*m.x240*m.x244 - 2*m.x239*m.x243
                           - 2.9321082756*m.b198 - 2.9321082756*m.b206 >= -2.9321082756)

m.c2816 = Constraint(expr=m.x239**2 + m.x240**2 + m.x245**2 + m.x246**2 - 2*m.x240*m.x246 - 2*m.x239*m.x245
                           - 2.9321082756*m.b198 - 2.9321082756*m.b210 >= -2.9321082756)

m.c2817 = Constraint(expr=m.x239**2 + m.x240**2 + m.x247**2 + m.x248**2 - 2*m.x240*m.x248 - 2*m.x239*m.x247
                           - 5.6664469849*m.b198 - 5.6664469849*m.b212 >= -5.6664469849)

m.c2818 = Constraint(expr=m.x239**2 + m.x240**2 + m.x249**2 + m.x250**2 - 2*m.x240*m.x250 - 2*m.x239*m.x249
                           - 5.6664469849*m.b198 - 5.6664469849*m.b214 >= -5.6664469849)

m.c2819 = Constraint(expr=m.x215**2 + m.x216**2 + m.x241**2 + m.x242**2 - 2*m.x215*m.x241 - 2*m.x216*m.x242
                           - 2.118573403024*m.b70 - 2.118573403024*m.b202 >= -2.118573403024)

m.c2820 = Constraint(expr=m.x217**2 + m.x218**2 + m.x241**2 + m.x242**2 - 2*m.x217*m.x241 - 2*m.x218*m.x242
                           - 2.118573403024*m.b79 - 2.118573403024*m.b202 >= -2.118573403024)

m.c2821 = Constraint(expr=m.x219**2 + m.x220**2 + m.x241**2 + m.x242**2 - 2*m.x219*m.x241 - 2*m.x220*m.x242
                           - 2.118573403024*m.b88 - 2.118573403024*m.b202 >= -2.118573403024)

m.c2822 = Constraint(expr=m.x221**2 + m.x222**2 + m.x241**2 + m.x242**2 - 2*m.x221*m.x241 - 2*m.x222*m.x242
                           - 2.118573403024*m.b97 - 2.118573403024*m.b202 >= -2.118573403024)

m.c2823 = Constraint(expr=m.x223**2 + m.x224**2 + m.x241**2 + m.x242**2 - 2*m.x223*m.x241 - 2*m.x224*m.x242
                           - 2.118573403024*m.b106 - 2.118573403024*m.b202 >= -2.118573403024)

m.c2824 = Constraint(expr=m.x225**2 + m.x226**2 + m.x241**2 + m.x242**2 - 2*m.x225*m.x241 - 2*m.x226*m.x242
                           - 2.118573403024*m.b115 - 2.118573403024*m.b202 >= -2.118573403024)

m.c2825 = Constraint(expr=m.x227**2 + m.x228**2 + m.x241**2 + m.x242**2 - 2*m.x227*m.x241 - 2*m.x228*m.x242
                           - 1.436936830729*m.b130 - 1.436936830729*m.b202 >= -1.436936830729)

m.c2826 = Constraint(expr=m.x229**2 + m.x230**2 + m.x241**2 + m.x242**2 - 2*m.x229*m.x241 - 2*m.x230*m.x242
                           - 1.436936830729*m.b145 - 1.436936830729*m.b202 >= -1.436936830729)

m.c2827 = Constraint(expr=m.x231**2 + m.x232**2 + m.x241**2 + m.x242**2 - 2*m.x232*m.x242 - 2*m.x231*m.x241
                           - 1.436936830729*m.b160 - 1.436936830729*m.b202 >= -1.436936830729)

m.c2828 = Constraint(expr=m.x233**2 + m.x234**2 + m.x241**2 + m.x242**2 - 2*m.x233*m.x241 - 2*m.x234*m.x242
                           - 1.436936830729*m.b175 - 1.436936830729*m.b202 >= -1.436936830729)

m.c2829 = Constraint(expr=m.x235**2 + m.x236**2 + m.x241**2 + m.x242**2 - 2*m.x236*m.x242 - 2*m.x235*m.x241
                           - 1.436936830729*m.b190 - 1.436936830729*m.b202 >= -1.436936830729)

m.c2830 = Constraint(expr=m.x237**2 + m.x238**2 + m.x241**2 + m.x242**2 - 2*m.x237*m.x241 - 2*m.x238*m.x242
                           - 2.9321082756*m.b194 - 2.9321082756*m.b202 >= -2.9321082756)

m.c2831 = Constraint(expr=m.x239**2 + m.x240**2 + m.x241**2 + m.x242**2 - 2*m.x240*m.x242 - 2*m.x239*m.x241
                           - 2.9321082756*m.b198 - 2.9321082756*m.b202 >= -2.9321082756)

m.c2832 = Constraint(expr=m.x241**2 + m.x242**2 + m.x243**2 + m.x244**2 - 2*m.x241*m.x243 - 2*m.x242*m.x244
                           - 2.9321082756*m.b202 - 2.9321082756*m.b206 >= -2.9321082756)

m.c2833 = Constraint(expr=m.x241**2 + m.x242**2 + m.x245**2 + m.x246**2 - 2*m.x241*m.x245 - 2*m.x242*m.x246
                           - 2.9321082756*m.b202 - 2.9321082756*m.b210 >= -2.9321082756)

m.c2834 = Constraint(expr=m.x241**2 + m.x242**2 + m.x247**2 + m.x248**2 - 2*m.x241*m.x247 - 2*m.x242*m.x248
                           - 5.6664469849*m.b202 - 5.6664469849*m.b212 >= -5.6664469849)

m.c2835 = Constraint(expr=m.x241**2 + m.x242**2 + m.x249**2 + m.x250**2 - 2*m.x241*m.x249 - 2*m.x242*m.x250
                           - 5.6664469849*m.b202 - 5.6664469849*m.b214 >= -5.6664469849)

m.c2836 = Constraint(expr=m.x215**2 + m.x216**2 + m.x243**2 + m.x244**2 - 2*m.x215*m.x243 - 2*m.x216*m.x244
                           - 2.118573403024*m.b70 - 2.118573403024*m.b206 >= -2.118573403024)

m.c2837 = Constraint(expr=m.x217**2 + m.x218**2 + m.x243**2 + m.x244**2 - 2*m.x217*m.x243 - 2*m.x218*m.x244
                           - 2.118573403024*m.b79 - 2.118573403024*m.b206 >= -2.118573403024)

m.c2838 = Constraint(expr=m.x219**2 + m.x220**2 + m.x243**2 + m.x244**2 - 2*m.x219*m.x243 - 2*m.x220*m.x244
                           - 2.118573403024*m.b88 - 2.118573403024*m.b206 >= -2.118573403024)

m.c2839 = Constraint(expr=m.x221**2 + m.x222**2 + m.x243**2 + m.x244**2 - 2*m.x221*m.x243 - 2*m.x222*m.x244
                           - 2.118573403024*m.b97 - 2.118573403024*m.b206 >= -2.118573403024)

m.c2840 = Constraint(expr=m.x223**2 + m.x224**2 + m.x243**2 + m.x244**2 - 2*m.x224*m.x244 - 2*m.x223*m.x243
                           - 2.118573403024*m.b106 - 2.118573403024*m.b206 >= -2.118573403024)

m.c2841 = Constraint(expr=m.x225**2 + m.x226**2 + m.x243**2 + m.x244**2 - 2*m.x226*m.x244 - 2*m.x225*m.x243
                           - 2.118573403024*m.b115 - 2.118573403024*m.b206 >= -2.118573403024)

m.c2842 = Constraint(expr=m.x227**2 + m.x228**2 + m.x243**2 + m.x244**2 - 2*m.x228*m.x244 - 2*m.x227*m.x243
                           - 1.436936830729*m.b130 - 1.436936830729*m.b206 >= -1.436936830729)

m.c2843 = Constraint(expr=m.x229**2 + m.x230**2 + m.x243**2 + m.x244**2 - 2*m.x230*m.x244 - 2*m.x229*m.x243
                           - 1.436936830729*m.b145 - 1.436936830729*m.b206 >= -1.436936830729)

m.c2844 = Constraint(expr=m.x231**2 + m.x232**2 + m.x243**2 + m.x244**2 - 2*m.x231*m.x243 - 2*m.x232*m.x244
                           - 1.436936830729*m.b160 - 1.436936830729*m.b206 >= -1.436936830729)

m.c2845 = Constraint(expr=m.x233**2 + m.x234**2 + m.x243**2 + m.x244**2 - 2*m.x234*m.x244 - 2*m.x233*m.x243
                           - 1.436936830729*m.b175 - 1.436936830729*m.b206 >= -1.436936830729)

m.c2846 = Constraint(expr=m.x235**2 + m.x236**2 + m.x243**2 + m.x244**2 - 2*m.x235*m.x243 - 2*m.x236*m.x244
                           - 1.436936830729*m.b190 - 1.436936830729*m.b206 >= -1.436936830729)

m.c2847 = Constraint(expr=m.x237**2 + m.x238**2 + m.x243**2 + m.x244**2 - 2*m.x238*m.x244 - 2*m.x237*m.x243
                           - 2.9321082756*m.b194 - 2.9321082756*m.b206 >= -2.9321082756)

m.c2848 = Constraint(expr=m.x239**2 + m.x240**2 + m.x243**2 + m.x244**2 - 2*m.x240*m.x244 - 2*m.x239*m.x243
                           - 2.9321082756*m.b198 - 2.9321082756*m.b206 >= -2.9321082756)

m.c2849 = Constraint(expr=m.x241**2 + m.x242**2 + m.x243**2 + m.x244**2 - 2*m.x241*m.x243 - 2*m.x242*m.x244
                           - 2.9321082756*m.b202 - 2.9321082756*m.b206 >= -2.9321082756)

m.c2850 = Constraint(expr=m.x243**2 + m.x244**2 + m.x245**2 + m.x246**2 - 2*m.x243*m.x245 - 2*m.x244*m.x246
                           - 2.9321082756*m.b206 - 2.9321082756*m.b210 >= -2.9321082756)

m.c2851 = Constraint(expr=m.x243**2 + m.x244**2 + m.x247**2 + m.x248**2 - 2*m.x243*m.x247 - 2*m.x244*m.x248
                           - 5.6664469849*m.b206 - 5.6664469849*m.b212 >= -5.6664469849)

m.c2852 = Constraint(expr=m.x243**2 + m.x244**2 + m.x249**2 + m.x250**2 - 2*m.x243*m.x249 - 2*m.x244*m.x250
                           - 5.6664469849*m.b206 - 5.6664469849*m.b214 >= -5.6664469849)

m.c2853 = Constraint(expr=m.x215**2 + m.x216**2 + m.x245**2 + m.x246**2 - 2*m.x215*m.x245 - 2*m.x216*m.x246
                           - 2.118573403024*m.b70 - 2.118573403024*m.b210 >= -2.118573403024)

m.c2854 = Constraint(expr=m.x217**2 + m.x218**2 + m.x245**2 + m.x246**2 - 2*m.x217*m.x245 - 2*m.x218*m.x246
                           - 2.118573403024*m.b79 - 2.118573403024*m.b210 >= -2.118573403024)

m.c2855 = Constraint(expr=m.x219**2 + m.x220**2 + m.x245**2 + m.x246**2 - 2*m.x219*m.x245 - 2*m.x220*m.x246
                           - 2.118573403024*m.b88 - 2.118573403024*m.b210 >= -2.118573403024)

m.c2856 = Constraint(expr=m.x221**2 + m.x222**2 + m.x245**2 + m.x246**2 - 2*m.x222*m.x246 - 2*m.x221*m.x245
                           - 2.118573403024*m.b97 - 2.118573403024*m.b210 >= -2.118573403024)

m.c2857 = Constraint(expr=m.x223**2 + m.x224**2 + m.x245**2 + m.x246**2 - 2*m.x224*m.x246 - 2*m.x223*m.x245
                           - 2.118573403024*m.b106 - 2.118573403024*m.b210 >= -2.118573403024)

m.c2858 = Constraint(expr=m.x225**2 + m.x226**2 + m.x245**2 + m.x246**2 - 2*m.x225*m.x245 - 2*m.x226*m.x246
                           - 2.118573403024*m.b115 - 2.118573403024*m.b210 >= -2.118573403024)

m.c2859 = Constraint(expr=m.x227**2 + m.x228**2 + m.x245**2 + m.x246**2 - 2*m.x228*m.x246 - 2*m.x227*m.x245
                           - 1.436936830729*m.b130 - 1.436936830729*m.b210 >= -1.436936830729)

m.c2860 = Constraint(expr=m.x229**2 + m.x230**2 + m.x245**2 + m.x246**2 - 2*m.x229*m.x245 - 2*m.x230*m.x246
                           - 1.436936830729*m.b145 - 1.436936830729*m.b210 >= -1.436936830729)

m.c2861 = Constraint(expr=m.x231**2 + m.x232**2 + m.x245**2 + m.x246**2 - 2*m.x232*m.x246 - 2*m.x231*m.x245
                           - 1.436936830729*m.b160 - 1.436936830729*m.b210 >= -1.436936830729)

m.c2862 = Constraint(expr=m.x233**2 + m.x234**2 + m.x245**2 + m.x246**2 - 2*m.x233*m.x245 - 2*m.x234*m.x246
                           - 1.436936830729*m.b175 - 1.436936830729*m.b210 >= -1.436936830729)

m.c2863 = Constraint(expr=m.x235**2 + m.x236**2 + m.x245**2 + m.x246**2 - 2*m.x236*m.x246 - 2*m.x235*m.x245
                           - 1.436936830729*m.b190 - 1.436936830729*m.b210 >= -1.436936830729)

m.c2864 = Constraint(expr=m.x237**2 + m.x238**2 + m.x245**2 + m.x246**2 - 2*m.x238*m.x246 - 2*m.x237*m.x245
                           - 2.9321082756*m.b194 - 2.9321082756*m.b210 >= -2.9321082756)

m.c2865 = Constraint(expr=m.x239**2 + m.x240**2 + m.x245**2 + m.x246**2 - 2*m.x239*m.x245 - 2*m.x240*m.x246
                           - 2.9321082756*m.b198 - 2.9321082756*m.b210 >= -2.9321082756)

m.c2866 = Constraint(expr=m.x241**2 + m.x242**2 + m.x245**2 + m.x246**2 - 2*m.x241*m.x245 - 2*m.x242*m.x246
                           - 2.9321082756*m.b202 - 2.9321082756*m.b210 >= -2.9321082756)

m.c2867 = Constraint(expr=m.x243**2 + m.x244**2 + m.x245**2 + m.x246**2 - 2*m.x243*m.x245 - 2*m.x244*m.x246
                           - 2.9321082756*m.b206 - 2.9321082756*m.b210 >= -2.9321082756)

m.c2868 = Constraint(expr=m.x245**2 + m.x246**2 + m.x247**2 + m.x248**2 - 2*m.x245*m.x247 - 2*m.x246*m.x248
                           - 5.6664469849*m.b210 - 5.6664469849*m.b212 >= -5.6664469849)

m.c2869 = Constraint(expr=m.x245**2 + m.x246**2 + m.x249**2 + m.x250**2 - 2*m.x245*m.x249 - 2*m.x246*m.x250
                           - 5.6664469849*m.b210 - 5.6664469849*m.b214 >= -5.6664469849)

m.c2870 = Constraint(expr=m.x215**2 + m.x216**2 + m.x247**2 + m.x248**2 - 2*m.x215*m.x247 - 2*m.x216*m.x248
                           - 4.509770398884*m.b70 - 4.509770398884*m.b212 >= -4.509770398884)

m.c2871 = Constraint(expr=m.x217**2 + m.x218**2 + m.x247**2 + m.x248**2 - 2*m.x217*m.x247 - 2*m.x218*m.x248
                           - 4.509770398884*m.b79 - 4.509770398884*m.b212 >= -4.509770398884)

m.c2872 = Constraint(expr=m.x219**2 + m.x220**2 + m.x247**2 + m.x248**2 - 2*m.x219*m.x247 - 2*m.x220*m.x248
                           - 4.509770398884*m.b88 - 4.509770398884*m.b212 >= -4.509770398884)

m.c2873 = Constraint(expr=m.x221**2 + m.x222**2 + m.x247**2 + m.x248**2 - 2*m.x222*m.x248 - 2*m.x221*m.x247
                           - 4.509770398884*m.b97 - 4.509770398884*m.b212 >= -4.509770398884)

m.c2874 = Constraint(expr=m.x223**2 + m.x224**2 + m.x247**2 + m.x248**2 - 2*m.x223*m.x247 - 2*m.x224*m.x248
                           - 4.509770398884*m.b106 - 4.509770398884*m.b212 >= -4.509770398884)

m.c2875 = Constraint(expr=m.x225**2 + m.x226**2 + m.x247**2 + m.x248**2 - 2*m.x226*m.x248 - 2*m.x225*m.x247
                           - 4.509770398884*m.b115 - 4.509770398884*m.b212 >= -4.509770398884)

m.c2876 = Constraint(expr=m.x227**2 + m.x228**2 + m.x247**2 + m.x248**2 - 2*m.x227*m.x247 - 2*m.x228*m.x248
                           - 3.484990776969*m.b130 - 3.484990776969*m.b212 >= -3.484990776969)

m.c2877 = Constraint(expr=m.x229**2 + m.x230**2 + m.x247**2 + m.x248**2 - 2*m.x230*m.x248 - 2*m.x229*m.x247
                           - 3.484990776969*m.b145 - 3.484990776969*m.b212 >= -3.484990776969)

m.c2878 = Constraint(expr=m.x231**2 + m.x232**2 + m.x247**2 + m.x248**2 - 2*m.x231*m.x247 - 2*m.x232*m.x248
                           - 3.484990776969*m.b160 - 3.484990776969*m.b212 >= -3.484990776969)

m.c2879 = Constraint(expr=m.x233**2 + m.x234**2 + m.x247**2 + m.x248**2 - 2*m.x234*m.x248 - 2*m.x233*m.x247
                           - 3.484990776969*m.b175 - 3.484990776969*m.b212 >= -3.484990776969)

m.c2880 = Constraint(expr=m.x235**2 + m.x236**2 + m.x247**2 + m.x248**2 - 2*m.x236*m.x248 - 2*m.x235*m.x247
                           - 3.484990776969*m.b190 - 3.484990776969*m.b212 >= -3.484990776969)

m.c2881 = Constraint(expr=m.x237**2 + m.x238**2 + m.x247**2 + m.x248**2 - 2*m.x237*m.x247 - 2*m.x238*m.x248
                           - 5.6664469849*m.b194 - 5.6664469849*m.b212 >= -5.6664469849)

m.c2882 = Constraint(expr=m.x239**2 + m.x240**2 + m.x247**2 + m.x248**2 - 2*m.x240*m.x248 - 2*m.x239*m.x247
                           - 5.6664469849*m.b198 - 5.6664469849*m.b212 >= -5.6664469849)

m.c2883 = Constraint(expr=m.x241**2 + m.x242**2 + m.x247**2 + m.x248**2 - 2*m.x241*m.x247 - 2*m.x242*m.x248
                           - 5.6664469849*m.b202 - 5.6664469849*m.b212 >= -5.6664469849)

m.c2884 = Constraint(expr=m.x243**2 + m.x244**2 + m.x247**2 + m.x248**2 - 2*m.x243*m.x247 - 2*m.x244*m.x248
                           - 5.6664469849*m.b206 - 5.6664469849*m.b212 >= -5.6664469849)

m.c2885 = Constraint(expr=m.x245**2 + m.x246**2 + m.x247**2 + m.x248**2 - 2*m.x245*m.x247 - 2*m.x246*m.x248
                           - 5.6664469849*m.b210 - 5.6664469849*m.b212 >= -5.6664469849)

m.c2886 = Constraint(expr=m.x247**2 + m.x248**2 + m.x249**2 + m.x250**2 - 2*m.x247*m.x249 - 2*m.x248*m.x250
                           - 9.2934741904*m.b212 - 9.2934741904*m.b214 >= -9.2934741904)

m.c2887 = Constraint(expr=m.x215**2 + m.x216**2 + m.x249**2 + m.x250**2 - 2*m.x215*m.x249 - 2*m.x216*m.x250
                           - 4.509770398884*m.b70 - 4.509770398884*m.b214 >= -4.509770398884)

m.c2888 = Constraint(expr=m.x217**2 + m.x218**2 + m.x249**2 + m.x250**2 - 2*m.x217*m.x249 - 2*m.x218*m.x250
                           - 4.509770398884*m.b79 - 4.509770398884*m.b214 >= -4.509770398884)

m.c2889 = Constraint(expr=m.x219**2 + m.x220**2 + m.x249**2 + m.x250**2 - 2*m.x219*m.x249 - 2*m.x220*m.x250
                           - 4.509770398884*m.b88 - 4.509770398884*m.b214 >= -4.509770398884)

m.c2890 = Constraint(expr=m.x221**2 + m.x222**2 + m.x249**2 + m.x250**2 - 2*m.x221*m.x249 - 2*m.x222*m.x250
                           - 4.509770398884*m.b97 - 4.509770398884*m.b214 >= -4.509770398884)

m.c2891 = Constraint(expr=m.x223**2 + m.x224**2 + m.x249**2 + m.x250**2 - 2*m.x224*m.x250 - 2*m.x223*m.x249
                           - 4.509770398884*m.b106 - 4.509770398884*m.b214 >= -4.509770398884)

m.c2892 = Constraint(expr=m.x225**2 + m.x226**2 + m.x249**2 + m.x250**2 - 2*m.x225*m.x249 - 2*m.x226*m.x250
                           - 4.509770398884*m.b115 - 4.509770398884*m.b214 >= -4.509770398884)

m.c2893 = Constraint(expr=m.x227**2 + m.x228**2 + m.x249**2 + m.x250**2 - 2*m.x228*m.x250 - 2*m.x227*m.x249
                           - 3.484990776969*m.b130 - 3.484990776969*m.b214 >= -3.484990776969)

m.c2894 = Constraint(expr=m.x229**2 + m.x230**2 + m.x249**2 + m.x250**2 - 2*m.x229*m.x249 - 2*m.x230*m.x250
                           - 3.484990776969*m.b145 - 3.484990776969*m.b214 >= -3.484990776969)

m.c2895 = Constraint(expr=m.x231**2 + m.x232**2 + m.x249**2 + m.x250**2 - 2*m.x232*m.x250 - 2*m.x231*m.x249
                           - 3.484990776969*m.b160 - 3.484990776969*m.b214 >= -3.484990776969)

m.c2896 = Constraint(expr=m.x233**2 + m.x234**2 + m.x249**2 + m.x250**2 - 2*m.x234*m.x250 - 2*m.x233*m.x249
                           - 3.484990776969*m.b175 - 3.484990776969*m.b214 >= -3.484990776969)

m.c2897 = Constraint(expr=m.x235**2 + m.x236**2 + m.x249**2 + m.x250**2 - 2*m.x235*m.x249 - 2*m.x236*m.x250
                           - 3.484990776969*m.b190 - 3.484990776969*m.b214 >= -3.484990776969)

m.c2898 = Constraint(expr=m.x237**2 + m.x238**2 + m.x249**2 + m.x250**2 - 2*m.x238*m.x250 - 2*m.x237*m.x249
                           - 5.6664469849*m.b194 - 5.6664469849*m.b214 >= -5.6664469849)

m.c2899 = Constraint(expr=m.x239**2 + m.x240**2 + m.x249**2 + m.x250**2 - 2*m.x240*m.x250 - 2*m.x239*m.x249
                           - 5.6664469849*m.b198 - 5.6664469849*m.b214 >= -5.6664469849)

m.c2900 = Constraint(expr=m.x241**2 + m.x242**2 + m.x249**2 + m.x250**2 - 2*m.x241*m.x249 - 2*m.x242*m.x250
                           - 5.6664469849*m.b202 - 5.6664469849*m.b214 >= -5.6664469849)

m.c2901 = Constraint(expr=m.x243**2 + m.x244**2 + m.x249**2 + m.x250**2 - 2*m.x243*m.x249 - 2*m.x244*m.x250
                           - 5.6664469849*m.b206 - 5.6664469849*m.b214 >= -5.6664469849)

m.c2902 = Constraint(expr=m.x245**2 + m.x246**2 + m.x249**2 + m.x250**2 - 2*m.x245*m.x249 - 2*m.x246*m.x250
                           - 5.6664469849*m.b210 - 5.6664469849*m.b214 >= -5.6664469849)

m.c2903 = Constraint(expr=m.x247**2 + m.x248**2 + m.x249**2 + m.x250**2 - 2*m.x247*m.x249 - 2*m.x248*m.x250
                           - 9.2934741904*m.b212 - 9.2934741904*m.b214 >= -9.2934741904)

m.c2904 = Constraint(expr=m.x215**2 + m.x216**2 + m.x237**2 + m.x238**2 - 2*m.x215*m.x237 - 2*m.x216*m.x238
                           + 146.015866806048*m.b62 <= 146.035526210992)

m.c2905 = Constraint(expr=m.x215**2 + m.x216**2 + m.x239**2 + m.x240**2 - 2*m.x215*m.x239 - 2*m.x216*m.x240
                           + 146.015866806048*m.b63 <= 146.035526210992)

m.c2906 = Constraint(expr=m.x215**2 + m.x216**2 + m.x241**2 + m.x242**2 - 2*m.x215*m.x241 - 2*m.x216*m.x242
                           + 146.015866806048*m.b64 <= 146.035526210992)

m.c2907 = Constraint(expr=m.x215**2 + m.x216**2 + m.x243**2 + m.x244**2 - 2*m.x215*m.x243 - 2*m.x216*m.x244
                           + 146.015866806048*m.b65 <= 146.035526210992)

m.c2908 = Constraint(expr=m.x215**2 + m.x216**2 + m.x245**2 + m.x246**2 - 2*m.x215*m.x245 - 2*m.x216*m.x246
                           + 146.015866806048*m.b66 <= 146.035526210992)

m.c2909 = Constraint(expr=m.x215**2 + m.x216**2 + m.x247**2 + m.x248**2 - 2*m.x215*m.x247 - 2*m.x216*m.x248
                           + 124.074660797768*m.b67 <= 124.688044241112)

m.c2910 = Constraint(expr=m.x215**2 + m.x216**2 + m.x249**2 + m.x250**2 - 2*m.x215*m.x249 - 2*m.x216*m.x250
                           + 124.074660797768*m.b68 <= 124.688044241112)

m.c2911 = Constraint(expr=m.x215**2 + m.x216**2 + m.x251**2 + m.x252**2 - 2*m.x215*m.x251 - 2*m.x216*m.x252
                           + 111.557223492128*m.b69 <= 112.885590384432)

m.c2912 = Constraint(expr=m.x215**2 + m.x216**2 + m.x253**2 + m.x254**2 - 2*m.x215*m.x253 - 2*m.x216*m.x254
                           + 111.557223492128*m.b70 <= 112.885590384432)

m.c2913 = Constraint(expr=m.x217**2 + m.x218**2 + m.x237**2 + m.x238**2 - 2*m.x217*m.x237 - 2*m.x218*m.x238
                           + 146.015866806048*m.b71 <= 146.035526210992)

m.c2914 = Constraint(expr=m.x217**2 + m.x218**2 + m.x239**2 + m.x240**2 - 2*m.x217*m.x239 - 2*m.x218*m.x240
                           + 146.015866806048*m.b72 <= 146.035526210992)

m.c2915 = Constraint(expr=m.x217**2 + m.x218**2 + m.x241**2 + m.x242**2 - 2*m.x217*m.x241 - 2*m.x218*m.x242
                           + 146.015866806048*m.b73 <= 146.035526210992)

m.c2916 = Constraint(expr=m.x217**2 + m.x218**2 + m.x243**2 + m.x244**2 - 2*m.x217*m.x243 - 2*m.x218*m.x244
                           + 146.015866806048*m.b74 <= 146.035526210992)

m.c2917 = Constraint(expr=m.x217**2 + m.x218**2 + m.x245**2 + m.x246**2 - 2*m.x217*m.x245 - 2*m.x218*m.x246
                           + 146.015866806048*m.b75 <= 146.035526210992)

m.c2918 = Constraint(expr=m.x217**2 + m.x218**2 + m.x247**2 + m.x248**2 - 2*m.x217*m.x247 - 2*m.x218*m.x248
                           + 124.074660797768*m.b76 <= 124.688044241112)

m.c2919 = Constraint(expr=m.x217**2 + m.x218**2 + m.x249**2 + m.x250**2 - 2*m.x217*m.x249 - 2*m.x218*m.x250
                           + 124.074660797768*m.b77 <= 124.688044241112)

m.c2920 = Constraint(expr=m.x217**2 + m.x218**2 + m.x251**2 + m.x252**2 - 2*m.x217*m.x251 - 2*m.x218*m.x252
                           + 111.557223492128*m.b78 <= 112.885590384432)

m.c2921 = Constraint(expr=m.x217**2 + m.x218**2 + m.x253**2 + m.x254**2 - 2*m.x217*m.x253 - 2*m.x218*m.x254
                           + 111.557223492128*m.b79 <= 112.885590384432)

m.c2922 = Constraint(expr=m.x219**2 + m.x220**2 + m.x237**2 + m.x238**2 - 2*m.x219*m.x237 - 2*m.x220*m.x238
                           + 146.015866806048*m.b80 <= 146.035526210992)

m.c2923 = Constraint(expr=m.x219**2 + m.x220**2 + m.x239**2 + m.x240**2 - 2*m.x219*m.x239 - 2*m.x220*m.x240
                           + 146.015866806048*m.b81 <= 146.035526210992)

m.c2924 = Constraint(expr=m.x219**2 + m.x220**2 + m.x241**2 + m.x242**2 - 2*m.x219*m.x241 - 2*m.x220*m.x242
                           + 146.015866806048*m.b82 <= 146.035526210992)

m.c2925 = Constraint(expr=m.x219**2 + m.x220**2 + m.x243**2 + m.x244**2 - 2*m.x219*m.x243 - 2*m.x220*m.x244
                           + 146.015866806048*m.b83 <= 146.035526210992)

m.c2926 = Constraint(expr=m.x219**2 + m.x220**2 + m.x245**2 + m.x246**2 - 2*m.x219*m.x245 - 2*m.x220*m.x246
                           + 146.015866806048*m.b84 <= 146.035526210992)

m.c2927 = Constraint(expr=m.x219**2 + m.x220**2 + m.x247**2 + m.x248**2 - 2*m.x219*m.x247 - 2*m.x220*m.x248
                           + 124.074660797768*m.b85 <= 124.688044241112)

m.c2928 = Constraint(expr=m.x219**2 + m.x220**2 + m.x249**2 + m.x250**2 - 2*m.x219*m.x249 - 2*m.x220*m.x250
                           + 124.074660797768*m.b86 <= 124.688044241112)

m.c2929 = Constraint(expr=m.x219**2 + m.x220**2 + m.x251**2 + m.x252**2 - 2*m.x219*m.x251 - 2*m.x220*m.x252
                           + 111.557223492128*m.b87 <= 112.885590384432)

m.c2930 = Constraint(expr=m.x219**2 + m.x220**2 + m.x253**2 + m.x254**2 - 2*m.x219*m.x253 - 2*m.x220*m.x254
                           + 111.557223492128*m.b88 <= 112.885590384432)

m.c2931 = Constraint(expr=m.x221**2 + m.x222**2 + m.x237**2 + m.x238**2 - 2*m.x221*m.x237 - 2*m.x222*m.x238
                           + 146.015866806048*m.b89 <= 146.035526210992)

m.c2932 = Constraint(expr=m.x221**2 + m.x222**2 + m.x239**2 + m.x240**2 - 2*m.x221*m.x239 - 2*m.x222*m.x240
                           + 146.015866806048*m.b90 <= 146.035526210992)

m.c2933 = Constraint(expr=m.x221**2 + m.x222**2 + m.x241**2 + m.x242**2 - 2*m.x221*m.x241 - 2*m.x222*m.x242
                           + 146.015866806048*m.b91 <= 146.035526210992)

m.c2934 = Constraint(expr=m.x221**2 + m.x222**2 + m.x243**2 + m.x244**2 - 2*m.x221*m.x243 - 2*m.x222*m.x244
                           + 146.015866806048*m.b92 <= 146.035526210992)

m.c2935 = Constraint(expr=m.x221**2 + m.x222**2 + m.x245**2 + m.x246**2 - 2*m.x221*m.x245 - 2*m.x222*m.x246
                           + 146.015866806048*m.b93 <= 146.035526210992)

m.c2936 = Constraint(expr=m.x221**2 + m.x222**2 + m.x247**2 + m.x248**2 - 2*m.x221*m.x247 - 2*m.x222*m.x248
                           + 124.074660797768*m.b94 <= 124.688044241112)

m.c2937 = Constraint(expr=m.x221**2 + m.x222**2 + m.x249**2 + m.x250**2 - 2*m.x221*m.x249 - 2*m.x222*m.x250
                           + 124.074660797768*m.b95 <= 124.688044241112)

m.c2938 = Constraint(expr=m.x221**2 + m.x222**2 + m.x251**2 + m.x252**2 - 2*m.x221*m.x251 - 2*m.x222*m.x252
                           + 111.557223492128*m.b96 <= 112.885590384432)

m.c2939 = Constraint(expr=m.x221**2 + m.x222**2 + m.x253**2 + m.x254**2 - 2*m.x221*m.x253 - 2*m.x222*m.x254
                           + 111.557223492128*m.b97 <= 112.885590384432)

m.c2940 = Constraint(expr=m.x223**2 + m.x224**2 + m.x237**2 + m.x238**2 - 2*m.x223*m.x237 - 2*m.x224*m.x238
                           + 146.015866806048*m.b98 <= 146.035526210992)

m.c2941 = Constraint(expr=m.x223**2 + m.x224**2 + m.x239**2 + m.x240**2 - 2*m.x223*m.x239 - 2*m.x224*m.x240
                           + 146.015866806048*m.b99 <= 146.035526210992)

m.c2942 = Constraint(expr=m.x223**2 + m.x224**2 + m.x241**2 + m.x242**2 - 2*m.x223*m.x241 - 2*m.x224*m.x242
                           + 146.015866806048*m.b100 <= 146.035526210992)

m.c2943 = Constraint(expr=m.x223**2 + m.x224**2 + m.x243**2 + m.x244**2 - 2*m.x223*m.x243 - 2*m.x224*m.x244
                           + 146.015866806048*m.b101 <= 146.035526210992)

m.c2944 = Constraint(expr=m.x223**2 + m.x224**2 + m.x245**2 + m.x246**2 - 2*m.x223*m.x245 - 2*m.x224*m.x246
                           + 146.015866806048*m.b102 <= 146.035526210992)

m.c2945 = Constraint(expr=m.x223**2 + m.x224**2 + m.x247**2 + m.x248**2 - 2*m.x223*m.x247 - 2*m.x224*m.x248
                           + 124.074660797768*m.b103 <= 124.688044241112)

m.c2946 = Constraint(expr=m.x223**2 + m.x224**2 + m.x249**2 + m.x250**2 - 2*m.x223*m.x249 - 2*m.x224*m.x250
                           + 124.074660797768*m.b104 <= 124.688044241112)

m.c2947 = Constraint(expr=m.x223**2 + m.x224**2 + m.x251**2 + m.x252**2 - 2*m.x223*m.x251 - 2*m.x224*m.x252
                           + 111.557223492128*m.b105 <= 112.885590384432)

m.c2948 = Constraint(expr=m.x223**2 + m.x224**2 + m.x253**2 + m.x254**2 - 2*m.x223*m.x253 - 2*m.x224*m.x254
                           + 111.557223492128*m.b106 <= 112.885590384432)

m.c2949 = Constraint(expr=m.x225**2 + m.x226**2 + m.x237**2 + m.x238**2 - 2*m.x225*m.x237 - 2*m.x226*m.x238
                           + 146.015866806048*m.b107 <= 146.035526210992)

m.c2950 = Constraint(expr=m.x225**2 + m.x226**2 + m.x239**2 + m.x240**2 - 2*m.x225*m.x239 - 2*m.x226*m.x240
                           + 146.015866806048*m.b108 <= 146.035526210992)

m.c2951 = Constraint(expr=m.x225**2 + m.x226**2 + m.x241**2 + m.x242**2 - 2*m.x225*m.x241 - 2*m.x226*m.x242
                           + 146.015866806048*m.b109 <= 146.035526210992)

m.c2952 = Constraint(expr=m.x225**2 + m.x226**2 + m.x243**2 + m.x244**2 - 2*m.x225*m.x243 - 2*m.x226*m.x244
                           + 146.015866806048*m.b110 <= 146.035526210992)

m.c2953 = Constraint(expr=m.x225**2 + m.x226**2 + m.x245**2 + m.x246**2 - 2*m.x225*m.x245 - 2*m.x226*m.x246
                           + 146.015866806048*m.b111 <= 146.035526210992)

m.c2954 = Constraint(expr=m.x225**2 + m.x226**2 + m.x247**2 + m.x248**2 - 2*m.x225*m.x247 - 2*m.x226*m.x248
                           + 124.074660797768*m.b112 <= 124.688044241112)

m.c2955 = Constraint(expr=m.x225**2 + m.x226**2 + m.x249**2 + m.x250**2 - 2*m.x225*m.x249 - 2*m.x226*m.x250
                           + 124.074660797768*m.b113 <= 124.688044241112)

m.c2956 = Constraint(expr=m.x225**2 + m.x226**2 + m.x251**2 + m.x252**2 - 2*m.x225*m.x251 - 2*m.x226*m.x252
                           + 111.557223492128*m.b114 <= 112.885590384432)

m.c2957 = Constraint(expr=m.x225**2 + m.x226**2 + m.x253**2 + m.x254**2 - 2*m.x225*m.x253 - 2*m.x226*m.x254
                           + 111.557223492128*m.b115 <= 112.885590384432)

m.c2958 = Constraint(expr=m.x215**2 + m.x216**2 + m.x227**2 + m.x228**2 - 2*m.x215*m.x227 - 2*m.x216*m.x228
                           + 164.09780773445*m.b116 <= 164.128395645686)

m.c2959 = Constraint(expr=m.x217**2 + m.x218**2 + m.x227**2 + m.x228**2 - 2*m.x217*m.x227 - 2*m.x218*m.x228
                           + 164.09780773445*m.b117 <= 164.128395645686)

m.c2960 = Constraint(expr=m.x219**2 + m.x220**2 + m.x227**2 + m.x228**2 - 2*m.x219*m.x227 - 2*m.x220*m.x228
                           + 164.09780773445*m.b118 <= 164.128395645686)

m.c2961 = Constraint(expr=m.x221**2 + m.x222**2 + m.x227**2 + m.x228**2 - 2*m.x221*m.x227 - 2*m.x222*m.x228
                           + 164.09780773445*m.b119 <= 164.128395645686)

m.c2962 = Constraint(expr=m.x223**2 + m.x224**2 + m.x227**2 + m.x228**2 - 2*m.x223*m.x227 - 2*m.x224*m.x228
                           + 164.09780773445*m.b120 <= 164.128395645686)

m.c2963 = Constraint(expr=m.x225**2 + m.x226**2 + m.x227**2 + m.x228**2 - 2*m.x225*m.x227 - 2*m.x226*m.x228
                           + 164.09780773445*m.b121 <= 164.128395645686)

m.c2964 = Constraint(expr=m.x227**2 + m.x228**2 + m.x237**2 + m.x238**2 - 2*m.x227*m.x237 - 2*m.x228*m.x238
                           + 154.924953661458*m.b122 <= 155.082579335899)

m.c2965 = Constraint(expr=m.x227**2 + m.x228**2 + m.x239**2 + m.x240**2 - 2*m.x227*m.x239 - 2*m.x228*m.x240
                           + 154.924953661458*m.b123 <= 155.082579335899)

m.c2966 = Constraint(expr=m.x227**2 + m.x228**2 + m.x241**2 + m.x242**2 - 2*m.x227*m.x241 - 2*m.x228*m.x242
                           + 154.924953661458*m.b124 <= 155.082579335899)

m.c2967 = Constraint(expr=m.x227**2 + m.x228**2 + m.x243**2 + m.x244**2 - 2*m.x227*m.x243 - 2*m.x228*m.x244
                           + 154.924953661458*m.b125 <= 155.082579335899)

m.c2968 = Constraint(expr=m.x227**2 + m.x228**2 + m.x245**2 + m.x246**2 - 2*m.x227*m.x245 - 2*m.x228*m.x246
                           + 154.924953661458*m.b126 <= 155.082579335899)

m.c2969 = Constraint(expr=m.x227**2 + m.x228**2 + m.x247**2 + m.x248**2 - 2*m.x227*m.x247 - 2*m.x228*m.x248
                           + 132.297461553938*m.b127 <= 133.379055313947)

m.c2970 = Constraint(expr=m.x227**2 + m.x228**2 + m.x249**2 + m.x250**2 - 2*m.x227*m.x249 - 2*m.x228*m.x250
                           + 132.297461553938*m.b128 <= 133.379055313947)

m.c2971 = Constraint(expr=m.x227**2 + m.x228**2 + m.x251**2 + m.x252**2 - 2*m.x227*m.x251 - 2*m.x228*m.x252
                           + 119.361045500978*m.b129 <= 121.347332654427)

m.c2972 = Constraint(expr=m.x227**2 + m.x228**2 + m.x253**2 + m.x254**2 - 2*m.x227*m.x253 - 2*m.x228*m.x254
                           + 119.361045500978*m.b130 <= 121.347332654427)

m.c2973 = Constraint(expr=m.x215**2 + m.x216**2 + m.x229**2 + m.x230**2 - 2*m.x215*m.x229 - 2*m.x216*m.x230
                           + 164.09780773445*m.b131 <= 164.128395645686)

m.c2974 = Constraint(expr=m.x217**2 + m.x218**2 + m.x229**2 + m.x230**2 - 2*m.x217*m.x229 - 2*m.x218*m.x230
                           + 164.09780773445*m.b132 <= 164.128395645686)

m.c2975 = Constraint(expr=m.x219**2 + m.x220**2 + m.x229**2 + m.x230**2 - 2*m.x219*m.x229 - 2*m.x220*m.x230
                           + 164.09780773445*m.b133 <= 164.128395645686)

m.c2976 = Constraint(expr=m.x221**2 + m.x222**2 + m.x229**2 + m.x230**2 - 2*m.x221*m.x229 - 2*m.x222*m.x230
                           + 164.09780773445*m.b134 <= 164.128395645686)

m.c2977 = Constraint(expr=m.x223**2 + m.x224**2 + m.x229**2 + m.x230**2 - 2*m.x223*m.x229 - 2*m.x224*m.x230
                           + 164.09780773445*m.b135 <= 164.128395645686)

m.c2978 = Constraint(expr=m.x225**2 + m.x226**2 + m.x229**2 + m.x230**2 - 2*m.x225*m.x229 - 2*m.x226*m.x230
                           + 164.09780773445*m.b136 <= 164.128395645686)

m.c2979 = Constraint(expr=m.x229**2 + m.x230**2 + m.x237**2 + m.x238**2 - 2*m.x229*m.x237 - 2*m.x230*m.x238
                           + 154.924953661458*m.b137 <= 155.082579335899)

m.c2980 = Constraint(expr=m.x229**2 + m.x230**2 + m.x239**2 + m.x240**2 - 2*m.x229*m.x239 - 2*m.x230*m.x240
                           + 154.924953661458*m.b138 <= 155.082579335899)

m.c2981 = Constraint(expr=m.x229**2 + m.x230**2 + m.x241**2 + m.x242**2 - 2*m.x229*m.x241 - 2*m.x230*m.x242
                           + 154.924953661458*m.b139 <= 155.082579335899)

m.c2982 = Constraint(expr=m.x229**2 + m.x230**2 + m.x243**2 + m.x244**2 - 2*m.x229*m.x243 - 2*m.x230*m.x244
                           + 154.924953661458*m.b140 <= 155.082579335899)

m.c2983 = Constraint(expr=m.x229**2 + m.x230**2 + m.x245**2 + m.x246**2 - 2*m.x229*m.x245 - 2*m.x230*m.x246
                           + 154.924953661458*m.b141 <= 155.082579335899)

m.c2984 = Constraint(expr=m.x229**2 + m.x230**2 + m.x247**2 + m.x248**2 - 2*m.x229*m.x247 - 2*m.x230*m.x248
                           + 132.297461553938*m.b142 <= 133.379055313947)

m.c2985 = Constraint(expr=m.x229**2 + m.x230**2 + m.x249**2 + m.x250**2 - 2*m.x229*m.x249 - 2*m.x230*m.x250
                           + 132.297461553938*m.b143 <= 133.379055313947)

m.c2986 = Constraint(expr=m.x229**2 + m.x230**2 + m.x251**2 + m.x252**2 - 2*m.x229*m.x251 - 2*m.x230*m.x252
                           + 119.361045500978*m.b144 <= 121.347332654427)

m.c2987 = Constraint(expr=m.x229**2 + m.x230**2 + m.x253**2 + m.x254**2 - 2*m.x229*m.x253 - 2*m.x230*m.x254
                           + 119.361045500978*m.b145 <= 121.347332654427)

m.c2988 = Constraint(expr=m.x215**2 + m.x216**2 + m.x231**2 + m.x232**2 - 2*m.x215*m.x231 - 2*m.x216*m.x232
                           + 164.09780773445*m.b146 <= 164.128395645686)

m.c2989 = Constraint(expr=m.x217**2 + m.x218**2 + m.x231**2 + m.x232**2 - 2*m.x217*m.x231 - 2*m.x218*m.x232
                           + 164.09780773445*m.b147 <= 164.128395645686)

m.c2990 = Constraint(expr=m.x219**2 + m.x220**2 + m.x231**2 + m.x232**2 - 2*m.x219*m.x231 - 2*m.x220*m.x232
                           + 164.09780773445*m.b148 <= 164.128395645686)

m.c2991 = Constraint(expr=m.x221**2 + m.x222**2 + m.x231**2 + m.x232**2 - 2*m.x221*m.x231 - 2*m.x222*m.x232
                           + 164.09780773445*m.b149 <= 164.128395645686)

m.c2992 = Constraint(expr=m.x223**2 + m.x224**2 + m.x231**2 + m.x232**2 - 2*m.x223*m.x231 - 2*m.x224*m.x232
                           + 164.09780773445*m.b150 <= 164.128395645686)

m.c2993 = Constraint(expr=m.x225**2 + m.x226**2 + m.x231**2 + m.x232**2 - 2*m.x225*m.x231 - 2*m.x226*m.x232
                           + 164.09780773445*m.b151 <= 164.128395645686)

m.c2994 = Constraint(expr=m.x231**2 + m.x232**2 + m.x237**2 + m.x238**2 - 2*m.x231*m.x237 - 2*m.x232*m.x238
                           + 154.924953661458*m.b152 <= 155.082579335899)

m.c2995 = Constraint(expr=m.x231**2 + m.x232**2 + m.x239**2 + m.x240**2 - 2*m.x231*m.x239 - 2*m.x232*m.x240
                           + 154.924953661458*m.b153 <= 155.082579335899)

m.c2996 = Constraint(expr=m.x231**2 + m.x232**2 + m.x241**2 + m.x242**2 - 2*m.x231*m.x241 - 2*m.x232*m.x242
                           + 154.924953661458*m.b154 <= 155.082579335899)

m.c2997 = Constraint(expr=m.x231**2 + m.x232**2 + m.x243**2 + m.x244**2 - 2*m.x231*m.x243 - 2*m.x232*m.x244
                           + 154.924953661458*m.b155 <= 155.082579335899)

m.c2998 = Constraint(expr=m.x231**2 + m.x232**2 + m.x245**2 + m.x246**2 - 2*m.x231*m.x245 - 2*m.x232*m.x246
                           + 154.924953661458*m.b156 <= 155.082579335899)

m.c2999 = Constraint(expr=m.x231**2 + m.x232**2 + m.x247**2 + m.x248**2 - 2*m.x231*m.x247 - 2*m.x232*m.x248
                           + 132.297461553938*m.b157 <= 133.379055313947)

m.c3000 = Constraint(expr=m.x231**2 + m.x232**2 + m.x249**2 + m.x250**2 - 2*m.x231*m.x249 - 2*m.x232*m.x250
                           + 132.297461553938*m.b158 <= 133.379055313947)

m.c3001 = Constraint(expr=m.x231**2 + m.x232**2 + m.x251**2 + m.x252**2 - 2*m.x231*m.x251 - 2*m.x232*m.x252
                           + 119.361045500978*m.b159 <= 121.347332654427)

m.c3002 = Constraint(expr=m.x231**2 + m.x232**2 + m.x253**2 + m.x254**2 - 2*m.x231*m.x253 - 2*m.x232*m.x254
                           + 119.361045500978*m.b160 <= 121.347332654427)

m.c3003 = Constraint(expr=m.x215**2 + m.x216**2 + m.x233**2 + m.x234**2 - 2*m.x215*m.x233 - 2*m.x216*m.x234
                           + 164.09780773445*m.b161 <= 164.128395645686)

m.c3004 = Constraint(expr=m.x217**2 + m.x218**2 + m.x233**2 + m.x234**2 - 2*m.x217*m.x233 - 2*m.x218*m.x234
                           + 164.09780773445*m.b162 <= 164.128395645686)

m.c3005 = Constraint(expr=m.x219**2 + m.x220**2 + m.x233**2 + m.x234**2 - 2*m.x219*m.x233 - 2*m.x220*m.x234
                           + 164.09780773445*m.b163 <= 164.128395645686)

m.c3006 = Constraint(expr=m.x221**2 + m.x222**2 + m.x233**2 + m.x234**2 - 2*m.x221*m.x233 - 2*m.x222*m.x234
                           + 164.09780773445*m.b164 <= 164.128395645686)

m.c3007 = Constraint(expr=m.x223**2 + m.x224**2 + m.x233**2 + m.x234**2 - 2*m.x223*m.x233 - 2*m.x224*m.x234
                           + 164.09780773445*m.b165 <= 164.128395645686)

m.c3008 = Constraint(expr=m.x225**2 + m.x226**2 + m.x233**2 + m.x234**2 - 2*m.x225*m.x233 - 2*m.x226*m.x234
                           + 164.09780773445*m.b166 <= 164.128395645686)

m.c3009 = Constraint(expr=m.x233**2 + m.x234**2 + m.x237**2 + m.x238**2 - 2*m.x233*m.x237 - 2*m.x234*m.x238
                           + 154.924953661458*m.b167 <= 155.082579335899)

m.c3010 = Constraint(expr=m.x233**2 + m.x234**2 + m.x239**2 + m.x240**2 - 2*m.x233*m.x239 - 2*m.x234*m.x240
                           + 154.924953661458*m.b168 <= 155.082579335899)

m.c3011 = Constraint(expr=m.x233**2 + m.x234**2 + m.x241**2 + m.x242**2 - 2*m.x233*m.x241 - 2*m.x234*m.x242
                           + 154.924953661458*m.b169 <= 155.082579335899)

m.c3012 = Constraint(expr=m.x233**2 + m.x234**2 + m.x243**2 + m.x244**2 - 2*m.x233*m.x243 - 2*m.x234*m.x244
                           + 154.924953661458*m.b170 <= 155.082579335899)

m.c3013 = Constraint(expr=m.x233**2 + m.x234**2 + m.x245**2 + m.x246**2 - 2*m.x233*m.x245 - 2*m.x234*m.x246
                           + 154.924953661458*m.b171 <= 155.082579335899)

m.c3014 = Constraint(expr=m.x233**2 + m.x234**2 + m.x247**2 + m.x248**2 - 2*m.x233*m.x247 - 2*m.x234*m.x248
                           + 132.297461553938*m.b172 <= 133.379055313947)

m.c3015 = Constraint(expr=m.x233**2 + m.x234**2 + m.x249**2 + m.x250**2 - 2*m.x233*m.x249 - 2*m.x234*m.x250
                           + 132.297461553938*m.b173 <= 133.379055313947)

m.c3016 = Constraint(expr=m.x233**2 + m.x234**2 + m.x251**2 + m.x252**2 - 2*m.x233*m.x251 - 2*m.x234*m.x252
                           + 119.361045500978*m.b174 <= 121.347332654427)

m.c3017 = Constraint(expr=m.x233**2 + m.x234**2 + m.x253**2 + m.x254**2 - 2*m.x233*m.x253 - 2*m.x234*m.x254
                           + 119.361045500978*m.b175 <= 121.347332654427)

m.c3018 = Constraint(expr=m.x215**2 + m.x216**2 + m.x235**2 + m.x236**2 - 2*m.x215*m.x235 - 2*m.x216*m.x236
                           + 164.09780773445*m.b176 <= 164.128395645686)

m.c3019 = Constraint(expr=m.x217**2 + m.x218**2 + m.x235**2 + m.x236**2 - 2*m.x217*m.x235 - 2*m.x218*m.x236
                           + 164.09780773445*m.b177 <= 164.128395645686)

m.c3020 = Constraint(expr=m.x219**2 + m.x220**2 + m.x235**2 + m.x236**2 - 2*m.x219*m.x235 - 2*m.x220*m.x236
                           + 164.09780773445*m.b178 <= 164.128395645686)

m.c3021 = Constraint(expr=m.x221**2 + m.x222**2 + m.x235**2 + m.x236**2 - 2*m.x221*m.x235 - 2*m.x222*m.x236
                           + 164.09780773445*m.b179 <= 164.128395645686)

m.c3022 = Constraint(expr=m.x223**2 + m.x224**2 + m.x235**2 + m.x236**2 - 2*m.x223*m.x235 - 2*m.x224*m.x236
                           + 164.09780773445*m.b180 <= 164.128395645686)

m.c3023 = Constraint(expr=m.x225**2 + m.x226**2 + m.x235**2 + m.x236**2 - 2*m.x225*m.x235 - 2*m.x226*m.x236
                           + 164.09780773445*m.b181 <= 164.128395645686)

m.c3024 = Constraint(expr=m.x235**2 + m.x236**2 + m.x237**2 + m.x238**2 - 2*m.x235*m.x237 - 2*m.x236*m.x238
                           + 154.924953661458*m.b182 <= 155.082579335899)

m.c3025 = Constraint(expr=m.x235**2 + m.x236**2 + m.x239**2 + m.x240**2 - 2*m.x235*m.x239 - 2*m.x236*m.x240
                           + 154.924953661458*m.b183 <= 155.082579335899)

m.c3026 = Constraint(expr=m.x235**2 + m.x236**2 + m.x241**2 + m.x242**2 - 2*m.x235*m.x241 - 2*m.x236*m.x242
                           + 154.924953661458*m.b184 <= 155.082579335899)

m.c3027 = Constraint(expr=m.x235**2 + m.x236**2 + m.x243**2 + m.x244**2 - 2*m.x235*m.x243 - 2*m.x236*m.x244
                           + 154.924953661458*m.b185 <= 155.082579335899)

m.c3028 = Constraint(expr=m.x235**2 + m.x236**2 + m.x245**2 + m.x246**2 - 2*m.x235*m.x245 - 2*m.x236*m.x246
                           + 154.924953661458*m.b186 <= 155.082579335899)

m.c3029 = Constraint(expr=m.x235**2 + m.x236**2 + m.x247**2 + m.x248**2 - 2*m.x235*m.x247 - 2*m.x236*m.x248
                           + 132.297461553938*m.b187 <= 133.379055313947)

m.c3030 = Constraint(expr=m.x235**2 + m.x236**2 + m.x249**2 + m.x250**2 - 2*m.x235*m.x249 - 2*m.x236*m.x250
                           + 132.297461553938*m.b188 <= 133.379055313947)

m.c3031 = Constraint(expr=m.x235**2 + m.x236**2 + m.x251**2 + m.x252**2 - 2*m.x235*m.x251 - 2*m.x236*m.x252
                           + 119.361045500978*m.b189 <= 121.347332654427)

m.c3032 = Constraint(expr=m.x235**2 + m.x236**2 + m.x253**2 + m.x254**2 - 2*m.x235*m.x253 - 2*m.x236*m.x254
                           + 119.361045500978*m.b190 <= 121.347332654427)

m.c3033 = Constraint(expr=m.x237**2 + m.x238**2 + m.x247**2 + m.x248**2 - 2*m.x237*m.x247 - 2*m.x238*m.x248
                           + 116.1156939698*m.b191 <= 116.3927698742)

m.c3034 = Constraint(expr=m.x237**2 + m.x238**2 + m.x249**2 + m.x250**2 - 2*m.x237*m.x249 - 2*m.x238*m.x250
                           + 116.1156939698*m.b192 <= 116.3927698742)

m.c3035 = Constraint(expr=m.x237**2 + m.x238**2 + m.x251**2 + m.x252**2 - 2*m.x237*m.x251 - 2*m.x238*m.x252
                           + 104.01723378*m.b193 <= 104.8195839276)

m.c3036 = Constraint(expr=m.x237**2 + m.x238**2 + m.x253**2 + m.x254**2 - 2*m.x237*m.x253 - 2*m.x238*m.x254
                           + 104.01723378*m.b194 <= 104.8195839276)

m.c3037 = Constraint(expr=m.x239**2 + m.x240**2 + m.x247**2 + m.x248**2 - 2*m.x239*m.x247 - 2*m.x240*m.x248
                           + 116.1156939698*m.b195 <= 116.3927698742)

m.c3038 = Constraint(expr=m.x239**2 + m.x240**2 + m.x249**2 + m.x250**2 - 2*m.x239*m.x249 - 2*m.x240*m.x250
                           + 116.1156939698*m.b196 <= 116.3927698742)

m.c3039 = Constraint(expr=m.x239**2 + m.x240**2 + m.x251**2 + m.x252**2 - 2*m.x239*m.x251 - 2*m.x240*m.x252
                           + 104.01723378*m.b197 <= 104.8195839276)

m.c3040 = Constraint(expr=m.x239**2 + m.x240**2 + m.x253**2 + m.x254**2 - 2*m.x239*m.x253 - 2*m.x240*m.x254
                           + 104.01723378*m.b198 <= 104.8195839276)

m.c3041 = Constraint(expr=m.x241**2 + m.x242**2 + m.x247**2 + m.x248**2 - 2*m.x241*m.x247 - 2*m.x242*m.x248
                           + 116.1156939698*m.b199 <= 116.3927698742)

m.c3042 = Constraint(expr=m.x241**2 + m.x242**2 + m.x249**2 + m.x250**2 - 2*m.x241*m.x249 - 2*m.x242*m.x250
                           + 116.1156939698*m.b200 <= 116.3927698742)

m.c3043 = Constraint(expr=m.x241**2 + m.x242**2 + m.x251**2 + m.x252**2 - 2*m.x241*m.x251 - 2*m.x242*m.x252
                           + 104.01723378*m.b201 <= 104.8195839276)

m.c3044 = Constraint(expr=m.x241**2 + m.x242**2 + m.x253**2 + m.x254**2 - 2*m.x241*m.x253 - 2*m.x242*m.x254
                           + 104.01723378*m.b202 <= 104.8195839276)

m.c3045 = Constraint(expr=m.x243**2 + m.x244**2 + m.x247**2 + m.x248**2 - 2*m.x243*m.x247 - 2*m.x244*m.x248
                           + 116.1156939698*m.b203 <= 116.3927698742)

m.c3046 = Constraint(expr=m.x243**2 + m.x244**2 + m.x249**2 + m.x250**2 - 2*m.x243*m.x249 - 2*m.x244*m.x250
                           + 116.1156939698*m.b204 <= 116.3927698742)

m.c3047 = Constraint(expr=m.x243**2 + m.x244**2 + m.x251**2 + m.x252**2 - 2*m.x243*m.x251 - 2*m.x244*m.x252
                           + 104.01723378*m.b205 <= 104.8195839276)

m.c3048 = Constraint(expr=m.x243**2 + m.x244**2 + m.x253**2 + m.x254**2 - 2*m.x243*m.x253 - 2*m.x244*m.x254
                           + 104.01723378*m.b206 <= 104.8195839276)

m.c3049 = Constraint(expr=m.x245**2 + m.x246**2 + m.x247**2 + m.x248**2 - 2*m.x245*m.x247 - 2*m.x246*m.x248
                           + 116.1156939698*m.b207 <= 116.3927698742)

m.c3050 = Constraint(expr=m.x245**2 + m.x246**2 + m.x249**2 + m.x250**2 - 2*m.x245*m.x249 - 2*m.x246*m.x250
                           + 116.1156939698*m.b208 <= 116.3927698742)

m.c3051 = Constraint(expr=m.x245**2 + m.x246**2 + m.x251**2 + m.x252**2 - 2*m.x245*m.x251 - 2*m.x246*m.x252
                           + 104.01723378*m.b209 <= 104.8195839276)

m.c3052 = Constraint(expr=m.x245**2 + m.x246**2 + m.x253**2 + m.x254**2 - 2*m.x245*m.x253 - 2*m.x246*m.x254
                           + 104.01723378*m.b210 <= 104.8195839276)

m.c3053 = Constraint(expr=m.x247**2 + m.x248**2 + m.x251**2 + m.x252**2 - 2*m.x247*m.x251 - 2*m.x248*m.x252
                           + 85.6376636642*m.b211 <= 85.6894881867)

m.c3054 = Constraint(expr=m.x247**2 + m.x248**2 + m.x253**2 + m.x254**2 - 2*m.x247*m.x253 - 2*m.x248*m.x254
                           + 85.6376636642*m.b212 <= 85.6894881867)

m.c3055 = Constraint(expr=m.x249**2 + m.x250**2 + m.x251**2 + m.x252**2 - 2*m.x249*m.x251 - 2*m.x250*m.x252
                           + 85.6376636642*m.b213 <= 85.6894881867)

m.c3056 = Constraint(expr=m.x249**2 + m.x250**2 + m.x253**2 + m.x254**2 - 2*m.x249*m.x253 - 2*m.x250*m.x254
                           + 85.6376636642*m.b214 <= 85.6894881867)

m.c3057 = Constraint(expr=   m.b2 + m.b3 + m.b4 + m.b62 + m.b63 + m.b64 + m.b65 + m.b66 + m.b67 + m.b68 + m.b69 + m.b70
                           <= 1)

m.c3058 = Constraint(expr=   m.b5 + m.b6 + m.b7 + m.b71 + m.b72 + m.b73 + m.b74 + m.b75 + m.b76 + m.b77 + m.b78 + m.b79
                           <= 1)

m.c3059 = Constraint(expr=   m.b8 + m.b9 + m.b10 + m.b80 + m.b81 + m.b82 + m.b83 + m.b84 + m.b85 + m.b86 + m.b87 + m.b88
                           <= 1)

m.c3060 = Constraint(expr=   m.b11 + m.b12 + m.b13 + m.b89 + m.b90 + m.b91 + m.b92 + m.b93 + m.b94 + m.b95 + m.b96
                           + m.b97 <= 1)

m.c3061 = Constraint(expr=   m.b14 + m.b15 + m.b16 + m.b98 + m.b99 + m.b100 + m.b101 + m.b102 + m.b103 + m.b104 + m.b105
                           + m.b106 <= 1)

m.c3062 = Constraint(expr=   m.b17 + m.b18 + m.b19 + m.b107 + m.b108 + m.b109 + m.b110 + m.b111 + m.b112 + m.b113
                           + m.b114 + m.b115 <= 1)

m.c3063 = Constraint(expr=   m.b20 + m.b21 + m.b22 + m.b116 + m.b117 + m.b118 + m.b119 + m.b120 + m.b121 + m.b122
                           + m.b123 + m.b124 + m.b125 + m.b126 + m.b127 + m.b128 + m.b129 + m.b130 <= 1)

m.c3064 = Constraint(expr=   m.b23 + m.b24 + m.b25 + m.b131 + m.b132 + m.b133 + m.b134 + m.b135 + m.b136 + m.b137
                           + m.b138 + m.b139 + m.b140 + m.b141 + m.b142 + m.b143 + m.b144 + m.b145 <= 1)

m.c3065 = Constraint(expr=   m.b26 + m.b27 + m.b28 + m.b146 + m.b147 + m.b148 + m.b149 + m.b150 + m.b151 + m.b152
                           + m.b153 + m.b154 + m.b155 + m.b156 + m.b157 + m.b158 + m.b159 + m.b160 <= 1)

m.c3066 = Constraint(expr=   m.b29 + m.b30 + m.b31 + m.b161 + m.b162 + m.b163 + m.b164 + m.b165 + m.b166 + m.b167
                           + m.b168 + m.b169 + m.b170 + m.b171 + m.b172 + m.b173 + m.b174 + m.b175 <= 1)

m.c3067 = Constraint(expr=   m.b32 + m.b33 + m.b34 + m.b176 + m.b177 + m.b178 + m.b179 + m.b180 + m.b181 + m.b182
                           + m.b183 + m.b184 + m.b185 + m.b186 + m.b187 + m.b188 + m.b189 + m.b190 <= 1)

m.c3068 = Constraint(expr=   m.b35 + m.b36 + m.b37 + m.b191 + m.b192 + m.b193 + m.b194 <= 1)

m.c3069 = Constraint(expr=   m.b38 + m.b39 + m.b40 + m.b195 + m.b196 + m.b197 + m.b198 <= 1)

m.c3070 = Constraint(expr=   m.b41 + m.b42 + m.b43 + m.b199 + m.b200 + m.b201 + m.b202 <= 1)

m.c3071 = Constraint(expr=   m.b44 + m.b45 + m.b46 + m.b203 + m.b204 + m.b205 + m.b206 <= 1)

m.c3072 = Constraint(expr=   m.b47 + m.b48 + m.b49 + m.b207 + m.b208 + m.b209 + m.b210 <= 1)

m.c3073 = Constraint(expr=   m.b50 + m.b51 + m.b52 + m.b211 + m.b212 <= 1)

m.c3074 = Constraint(expr=   m.b53 + m.b54 + m.b55 + m.b213 + m.b214 <= 1)

m.c3075 = Constraint(expr=   m.b56 + m.b57 + m.b58 <= 1)

m.c3076 = Constraint(expr=   m.b59 + m.b60 + m.b61 <= 1)

m.c3077 = Constraint(expr= - m.b35 - m.b36 - m.b37 + m.b62 <= 0)

m.c3078 = Constraint(expr= - m.b38 - m.b39 - m.b40 + m.b63 <= 0)

m.c3079 = Constraint(expr= - m.b41 - m.b42 - m.b43 + m.b64 <= 0)

m.c3080 = Constraint(expr= - m.b44 - m.b45 - m.b46 + m.b65 <= 0)

m.c3081 = Constraint(expr= - m.b47 - m.b48 - m.b49 + m.b66 <= 0)

m.c3082 = Constraint(expr= - m.b50 - m.b51 - m.b52 + m.b67 <= 0)

m.c3083 = Constraint(expr= - m.b53 - m.b54 - m.b55 + m.b68 <= 0)

m.c3084 = Constraint(expr= - m.b56 - m.b57 - m.b58 + m.b69 <= 0)

m.c3085 = Constraint(expr= - m.b59 - m.b60 - m.b61 + m.b70 <= 0)

m.c3086 = Constraint(expr= - m.b35 - m.b36 - m.b37 + m.b71 <= 0)

m.c3087 = Constraint(expr= - m.b38 - m.b39 - m.b40 + m.b72 <= 0)

m.c3088 = Constraint(expr= - m.b41 - m.b42 - m.b43 + m.b73 <= 0)

m.c3089 = Constraint(expr= - m.b44 - m.b45 - m.b46 + m.b74 <= 0)

m.c3090 = Constraint(expr= - m.b47 - m.b48 - m.b49 + m.b75 <= 0)

m.c3091 = Constraint(expr= - m.b50 - m.b51 - m.b52 + m.b76 <= 0)

m.c3092 = Constraint(expr= - m.b53 - m.b54 - m.b55 + m.b77 <= 0)

m.c3093 = Constraint(expr= - m.b56 - m.b57 - m.b58 + m.b78 <= 0)

m.c3094 = Constraint(expr= - m.b59 - m.b60 - m.b61 + m.b79 <= 0)

m.c3095 = Constraint(expr= - m.b35 - m.b36 - m.b37 + m.b80 <= 0)

m.c3096 = Constraint(expr= - m.b38 - m.b39 - m.b40 + m.b81 <= 0)

m.c3097 = Constraint(expr= - m.b41 - m.b42 - m.b43 + m.b82 <= 0)

m.c3098 = Constraint(expr= - m.b44 - m.b45 - m.b46 + m.b83 <= 0)

m.c3099 = Constraint(expr= - m.b47 - m.b48 - m.b49 + m.b84 <= 0)

m.c3100 = Constraint(expr= - m.b50 - m.b51 - m.b52 + m.b85 <= 0)

m.c3101 = Constraint(expr= - m.b53 - m.b54 - m.b55 + m.b86 <= 0)

m.c3102 = Constraint(expr= - m.b56 - m.b57 - m.b58 + m.b87 <= 0)

m.c3103 = Constraint(expr= - m.b59 - m.b60 - m.b61 + m.b88 <= 0)

m.c3104 = Constraint(expr= - m.b35 - m.b36 - m.b37 + m.b89 <= 0)

m.c3105 = Constraint(expr= - m.b38 - m.b39 - m.b40 + m.b90 <= 0)

m.c3106 = Constraint(expr= - m.b41 - m.b42 - m.b43 + m.b91 <= 0)

m.c3107 = Constraint(expr= - m.b44 - m.b45 - m.b46 + m.b92 <= 0)

m.c3108 = Constraint(expr= - m.b47 - m.b48 - m.b49 + m.b93 <= 0)

m.c3109 = Constraint(expr= - m.b50 - m.b51 - m.b52 + m.b94 <= 0)

m.c3110 = Constraint(expr= - m.b53 - m.b54 - m.b55 + m.b95 <= 0)

m.c3111 = Constraint(expr= - m.b56 - m.b57 - m.b58 + m.b96 <= 0)

m.c3112 = Constraint(expr= - m.b59 - m.b60 - m.b61 + m.b97 <= 0)

m.c3113 = Constraint(expr= - m.b35 - m.b36 - m.b37 + m.b98 <= 0)

m.c3114 = Constraint(expr= - m.b38 - m.b39 - m.b40 + m.b99 <= 0)

m.c3115 = Constraint(expr= - m.b41 - m.b42 - m.b43 + m.b100 <= 0)

m.c3116 = Constraint(expr= - m.b44 - m.b45 - m.b46 + m.b101 <= 0)

m.c3117 = Constraint(expr= - m.b47 - m.b48 - m.b49 + m.b102 <= 0)

m.c3118 = Constraint(expr= - m.b50 - m.b51 - m.b52 + m.b103 <= 0)

m.c3119 = Constraint(expr= - m.b53 - m.b54 - m.b55 + m.b104 <= 0)

m.c3120 = Constraint(expr= - m.b56 - m.b57 - m.b58 + m.b105 <= 0)

m.c3121 = Constraint(expr= - m.b59 - m.b60 - m.b61 + m.b106 <= 0)

m.c3122 = Constraint(expr= - m.b35 - m.b36 - m.b37 + m.b107 <= 0)

m.c3123 = Constraint(expr= - m.b38 - m.b39 - m.b40 + m.b108 <= 0)

m.c3124 = Constraint(expr= - m.b41 - m.b42 - m.b43 + m.b109 <= 0)

m.c3125 = Constraint(expr= - m.b44 - m.b45 - m.b46 + m.b110 <= 0)

m.c3126 = Constraint(expr= - m.b47 - m.b48 - m.b49 + m.b111 <= 0)

m.c3127 = Constraint(expr= - m.b50 - m.b51 - m.b52 + m.b112 <= 0)

m.c3128 = Constraint(expr= - m.b53 - m.b54 - m.b55 + m.b113 <= 0)

m.c3129 = Constraint(expr= - m.b56 - m.b57 - m.b58 + m.b114 <= 0)

m.c3130 = Constraint(expr= - m.b59 - m.b60 - m.b61 + m.b115 <= 0)

m.c3131 = Constraint(expr= - m.b2 - m.b3 - m.b4 + m.b116 <= 0)

m.c3132 = Constraint(expr= - m.b5 - m.b6 - m.b7 + m.b117 <= 0)

m.c3133 = Constraint(expr= - m.b8 - m.b9 - m.b10 + m.b118 <= 0)

m.c3134 = Constraint(expr= - m.b11 - m.b12 - m.b13 + m.b119 <= 0)

m.c3135 = Constraint(expr= - m.b14 - m.b15 - m.b16 + m.b120 <= 0)

m.c3136 = Constraint(expr= - m.b17 - m.b18 - m.b19 + m.b121 <= 0)

m.c3137 = Constraint(expr= - m.b35 - m.b36 - m.b37 + m.b122 <= 0)

m.c3138 = Constraint(expr= - m.b38 - m.b39 - m.b40 + m.b123 <= 0)

m.c3139 = Constraint(expr= - m.b41 - m.b42 - m.b43 + m.b124 <= 0)

m.c3140 = Constraint(expr= - m.b44 - m.b45 - m.b46 + m.b125 <= 0)

m.c3141 = Constraint(expr= - m.b47 - m.b48 - m.b49 + m.b126 <= 0)

m.c3142 = Constraint(expr= - m.b50 - m.b51 - m.b52 + m.b127 <= 0)

m.c3143 = Constraint(expr= - m.b53 - m.b54 - m.b55 + m.b128 <= 0)

m.c3144 = Constraint(expr= - m.b56 - m.b57 - m.b58 + m.b129 <= 0)

m.c3145 = Constraint(expr= - m.b59 - m.b60 - m.b61 + m.b130 <= 0)

m.c3146 = Constraint(expr= - m.b2 - m.b3 - m.b4 + m.b131 <= 0)

m.c3147 = Constraint(expr= - m.b5 - m.b6 - m.b7 + m.b132 <= 0)

m.c3148 = Constraint(expr= - m.b8 - m.b9 - m.b10 + m.b133 <= 0)

m.c3149 = Constraint(expr= - m.b11 - m.b12 - m.b13 + m.b134 <= 0)

m.c3150 = Constraint(expr= - m.b14 - m.b15 - m.b16 + m.b135 <= 0)

m.c3151 = Constraint(expr= - m.b17 - m.b18 - m.b19 + m.b136 <= 0)

m.c3152 = Constraint(expr= - m.b35 - m.b36 - m.b37 + m.b137 <= 0)

m.c3153 = Constraint(expr= - m.b38 - m.b39 - m.b40 + m.b138 <= 0)

m.c3154 = Constraint(expr= - m.b41 - m.b42 - m.b43 + m.b139 <= 0)

m.c3155 = Constraint(expr= - m.b44 - m.b45 - m.b46 + m.b140 <= 0)

m.c3156 = Constraint(expr= - m.b47 - m.b48 - m.b49 + m.b141 <= 0)

m.c3157 = Constraint(expr= - m.b50 - m.b51 - m.b52 + m.b142 <= 0)

m.c3158 = Constraint(expr= - m.b53 - m.b54 - m.b55 + m.b143 <= 0)

m.c3159 = Constraint(expr= - m.b56 - m.b57 - m.b58 + m.b144 <= 0)

m.c3160 = Constraint(expr= - m.b59 - m.b60 - m.b61 + m.b145 <= 0)

m.c3161 = Constraint(expr= - m.b2 - m.b3 - m.b4 + m.b146 <= 0)

m.c3162 = Constraint(expr= - m.b5 - m.b6 - m.b7 + m.b147 <= 0)

m.c3163 = Constraint(expr= - m.b8 - m.b9 - m.b10 + m.b148 <= 0)

m.c3164 = Constraint(expr= - m.b11 - m.b12 - m.b13 + m.b149 <= 0)

m.c3165 = Constraint(expr= - m.b14 - m.b15 - m.b16 + m.b150 <= 0)

m.c3166 = Constraint(expr= - m.b17 - m.b18 - m.b19 + m.b151 <= 0)

m.c3167 = Constraint(expr= - m.b35 - m.b36 - m.b37 + m.b152 <= 0)

m.c3168 = Constraint(expr= - m.b38 - m.b39 - m.b40 + m.b153 <= 0)

m.c3169 = Constraint(expr= - m.b41 - m.b42 - m.b43 + m.b154 <= 0)

m.c3170 = Constraint(expr= - m.b44 - m.b45 - m.b46 + m.b155 <= 0)

m.c3171 = Constraint(expr= - m.b47 - m.b48 - m.b49 + m.b156 <= 0)

m.c3172 = Constraint(expr= - m.b50 - m.b51 - m.b52 + m.b157 <= 0)

m.c3173 = Constraint(expr= - m.b53 - m.b54 - m.b55 + m.b158 <= 0)

m.c3174 = Constraint(expr= - m.b56 - m.b57 - m.b58 + m.b159 <= 0)

m.c3175 = Constraint(expr= - m.b59 - m.b60 - m.b61 + m.b160 <= 0)

m.c3176 = Constraint(expr= - m.b2 - m.b3 - m.b4 + m.b161 <= 0)

m.c3177 = Constraint(expr= - m.b5 - m.b6 - m.b7 + m.b162 <= 0)

m.c3178 = Constraint(expr= - m.b8 - m.b9 - m.b10 + m.b163 <= 0)

m.c3179 = Constraint(expr= - m.b11 - m.b12 - m.b13 + m.b164 <= 0)

m.c3180 = Constraint(expr= - m.b14 - m.b15 - m.b16 + m.b165 <= 0)

m.c3181 = Constraint(expr= - m.b17 - m.b18 - m.b19 + m.b166 <= 0)

m.c3182 = Constraint(expr= - m.b35 - m.b36 - m.b37 + m.b167 <= 0)

m.c3183 = Constraint(expr= - m.b38 - m.b39 - m.b40 + m.b168 <= 0)

m.c3184 = Constraint(expr= - m.b41 - m.b42 - m.b43 + m.b169 <= 0)

m.c3185 = Constraint(expr= - m.b44 - m.b45 - m.b46 + m.b170 <= 0)

m.c3186 = Constraint(expr= - m.b47 - m.b48 - m.b49 + m.b171 <= 0)

m.c3187 = Constraint(expr= - m.b50 - m.b51 - m.b52 + m.b172 <= 0)

m.c3188 = Constraint(expr= - m.b53 - m.b54 - m.b55 + m.b173 <= 0)

m.c3189 = Constraint(expr= - m.b56 - m.b57 - m.b58 + m.b174 <= 0)

m.c3190 = Constraint(expr= - m.b59 - m.b60 - m.b61 + m.b175 <= 0)

m.c3191 = Constraint(expr= - m.b2 - m.b3 - m.b4 + m.b176 <= 0)

m.c3192 = Constraint(expr= - m.b5 - m.b6 - m.b7 + m.b177 <= 0)

m.c3193 = Constraint(expr= - m.b8 - m.b9 - m.b10 + m.b178 <= 0)

m.c3194 = Constraint(expr= - m.b11 - m.b12 - m.b13 + m.b179 <= 0)

m.c3195 = Constraint(expr= - m.b14 - m.b15 - m.b16 + m.b180 <= 0)

m.c3196 = Constraint(expr= - m.b17 - m.b18 - m.b19 + m.b181 <= 0)

m.c3197 = Constraint(expr= - m.b35 - m.b36 - m.b37 + m.b182 <= 0)

m.c3198 = Constraint(expr= - m.b38 - m.b39 - m.b40 + m.b183 <= 0)

m.c3199 = Constraint(expr= - m.b41 - m.b42 - m.b43 + m.b184 <= 0)

m.c3200 = Constraint(expr= - m.b44 - m.b45 - m.b46 + m.b185 <= 0)

m.c3201 = Constraint(expr= - m.b47 - m.b48 - m.b49 + m.b186 <= 0)

m.c3202 = Constraint(expr= - m.b50 - m.b51 - m.b52 + m.b187 <= 0)

m.c3203 = Constraint(expr= - m.b53 - m.b54 - m.b55 + m.b188 <= 0)

m.c3204 = Constraint(expr= - m.b56 - m.b57 - m.b58 + m.b189 <= 0)

m.c3205 = Constraint(expr= - m.b59 - m.b60 - m.b61 + m.b190 <= 0)

m.c3206 = Constraint(expr= - m.b50 - m.b51 - m.b52 + m.b191 <= 0)

m.c3207 = Constraint(expr= - m.b53 - m.b54 - m.b55 + m.b192 <= 0)

m.c3208 = Constraint(expr= - m.b56 - m.b57 - m.b58 + m.b193 <= 0)

m.c3209 = Constraint(expr= - m.b59 - m.b60 - m.b61 + m.b194 <= 0)

m.c3210 = Constraint(expr= - m.b50 - m.b51 - m.b52 + m.b195 <= 0)

m.c3211 = Constraint(expr= - m.b53 - m.b54 - m.b55 + m.b196 <= 0)

m.c3212 = Constraint(expr= - m.b56 - m.b57 - m.b58 + m.b197 <= 0)

m.c3213 = Constraint(expr= - m.b59 - m.b60 - m.b61 + m.b198 <= 0)

m.c3214 = Constraint(expr= - m.b50 - m.b51 - m.b52 + m.b199 <= 0)

m.c3215 = Constraint(expr= - m.b53 - m.b54 - m.b55 + m.b200 <= 0)

m.c3216 = Constraint(expr= - m.b56 - m.b57 - m.b58 + m.b201 <= 0)

m.c3217 = Constraint(expr= - m.b59 - m.b60 - m.b61 + m.b202 <= 0)

m.c3218 = Constraint(expr= - m.b50 - m.b51 - m.b52 + m.b203 <= 0)

m.c3219 = Constraint(expr= - m.b53 - m.b54 - m.b55 + m.b204 <= 0)

m.c3220 = Constraint(expr= - m.b56 - m.b57 - m.b58 + m.b205 <= 0)

m.c3221 = Constraint(expr= - m.b59 - m.b60 - m.b61 + m.b206 <= 0)

m.c3222 = Constraint(expr= - m.b50 - m.b51 - m.b52 + m.b207 <= 0)

m.c3223 = Constraint(expr= - m.b53 - m.b54 - m.b55 + m.b208 <= 0)

m.c3224 = Constraint(expr= - m.b56 - m.b57 - m.b58 + m.b209 <= 0)

m.c3225 = Constraint(expr= - m.b59 - m.b60 - m.b61 + m.b210 <= 0)

m.c3226 = Constraint(expr= - m.b56 - m.b57 - m.b58 + m.b211 <= 0)

m.c3227 = Constraint(expr= - m.b59 - m.b60 - m.b61 + m.b212 <= 0)

m.c3228 = Constraint(expr= - m.b56 - m.b57 - m.b58 + m.b213 <= 0)

m.c3229 = Constraint(expr= - m.b59 - m.b60 - m.b61 + m.b214 <= 0)
