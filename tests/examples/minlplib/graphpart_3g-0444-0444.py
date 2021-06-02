#  MINLP written by GAMS Convert at 04/21/18 13:52:22
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         65       65        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        193        1      192        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        385      193      192        0
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

m.obj = Objective(expr=66001*m.b1*m.b10 - 98417*m.b1*m.b4 + 120652*m.b1*m.b13 + 57159*m.b1*m.b37 - 32487*m.b1*m.b49 + 
                       53052*m.b1*m.b145 - 98417*m.b2*m.b5 + 66001*m.b2*m.b11 + 120652*m.b2*m.b14 + 57159*m.b2*m.b38 - 
                       32487*m.b2*m.b50 + 53052*m.b2*m.b146 - 98417*m.b3*m.b6 + 66001*m.b3*m.b12 + 120652*m.b3*m.b15 + 
                       57159*m.b3*m.b39 - 32487*m.b3*m.b51 + 53052*m.b3*m.b147 - 60453*m.b4*m.b7 - 39384*m.b4*m.b16 - 
                       11074*m.b4*m.b40 - 111697*m.b4*m.b52 + 25207*m.b4*m.b148 - 60453*m.b5*m.b8 - 39384*m.b5*m.b17 - 
                       11074*m.b5*m.b41 - 111697*m.b5*m.b53 + 25207*m.b5*m.b149 - 60453*m.b6*m.b9 - 39384*m.b6*m.b18 - 
                       11074*m.b6*m.b42 - 111697*m.b6*m.b54 + 25207*m.b6*m.b150 - 177822*m.b7*m.b10 + 28848*m.b7*m.b19
                        + 24866*m.b7*m.b43 + 149301*m.b7*m.b55 - 10288*m.b7*m.b151 - 177822*m.b8*m.b11 + 28848*m.b8*
                       m.b20 + 24866*m.b8*m.b44 + 149301*m.b8*m.b56 - 10288*m.b8*m.b152 - 177822*m.b9*m.b12 + 28848*m.b9
                       *m.b21 + 24866*m.b9*m.b45 + 149301*m.b9*m.b57 - 10288*m.b9*m.b153 - 73711*m.b10*m.b22 - 257438*
                       m.b10*m.b46 - 53779*m.b10*m.b58 - 75949*m.b10*m.b154 - 73711*m.b11*m.b23 - 257438*m.b11*m.b47 - 
                       53779*m.b11*m.b59 - 75949*m.b11*m.b155 - 73711*m.b12*m.b24 - 257438*m.b12*m.b48 - 53779*m.b12*
                       m.b60 - 75949*m.b12*m.b156 - 15553*m.b13*m.b16 + 58384*m.b13*m.b22 + 119758*m.b13*m.b25 + 146126*
                       m.b13*m.b61 - 136368*m.b13*m.b157 - 15553*m.b14*m.b17 + 58384*m.b14*m.b23 + 119758*m.b14*m.b26 + 
                       146126*m.b14*m.b62 - 136368*m.b14*m.b158 - 15553*m.b15*m.b18 + 58384*m.b15*m.b24 + 119758*m.b15*
                       m.b27 + 146126*m.b15*m.b63 - 136368*m.b15*m.b159 + 79902*m.b16*m.b19 + 43015*m.b16*m.b28 - 101587
                       *m.b16*m.b64 - 6527*m.b16*m.b160 + 79902*m.b17*m.b20 + 43015*m.b17*m.b29 - 101587*m.b17*m.b65 - 
                       6527*m.b17*m.b161 + 79902*m.b18*m.b21 + 43015*m.b18*m.b30 - 101587*m.b18*m.b66 - 6527*m.b18*
                       m.b162 - 179565*m.b19*m.b22 + 99803*m.b19*m.b31 - 128370*m.b19*m.b67 + 74783*m.b19*m.b163 - 
                       179565*m.b20*m.b23 + 99803*m.b20*m.b32 - 128370*m.b20*m.b68 + 74783*m.b20*m.b164 - 179565*m.b21*
                       m.b24 + 99803*m.b21*m.b33 - 128370*m.b21*m.b69 + 74783*m.b21*m.b165 - 170972*m.b22*m.b34 - 34569*
                       m.b22*m.b70 - 77131*m.b22*m.b166 - 170972*m.b23*m.b35 - 34569*m.b23*m.b71 - 77131*m.b23*m.b167 - 
                       170972*m.b24*m.b36 - 34569*m.b24*m.b72 - 77131*m.b24*m.b168 - 40738*m.b25*m.b28 - 103362*m.b25*
                       m.b34 - 22400*m.b25*m.b37 - 34794*m.b25*m.b73 + 175355*m.b25*m.b169 - 40738*m.b26*m.b29 - 103362*
                       m.b26*m.b35 - 22400*m.b26*m.b38 - 34794*m.b26*m.b74 + 175355*m.b26*m.b170 - 40738*m.b27*m.b30 - 
                       103362*m.b27*m.b36 - 22400*m.b27*m.b39 - 34794*m.b27*m.b75 + 175355*m.b27*m.b171 + 178545*m.b28*
                       m.b31 - 44649*m.b28*m.b40 + 306756*m.b28*m.b76 + 175429*m.b28*m.b172 + 178545*m.b29*m.b32 - 44649
                       *m.b29*m.b41 + 306756*m.b29*m.b77 + 175429*m.b29*m.b173 + 178545*m.b30*m.b33 - 44649*m.b30*m.b42
                        + 306756*m.b30*m.b78 + 175429*m.b30*m.b174 - 31957*m.b31*m.b34 - 10370*m.b31*m.b43 - 123251*
                       m.b31*m.b79 - 155018*m.b31*m.b175 - 31957*m.b32*m.b35 - 10370*m.b32*m.b44 - 123251*m.b32*m.b80 - 
                       155018*m.b32*m.b176 - 31957*m.b33*m.b36 - 10370*m.b33*m.b45 - 123251*m.b33*m.b81 - 155018*m.b33*
                       m.b177 + 25701*m.b34*m.b46 + 98283*m.b34*m.b82 + 10995*m.b34*m.b178 + 25701*m.b35*m.b47 + 98283*
                       m.b35*m.b83 + 10995*m.b35*m.b179 + 25701*m.b36*m.b48 + 98283*m.b36*m.b84 + 10995*m.b36*m.b180 + 
                       6802*m.b37*m.b40 - 10028*m.b37*m.b46 + 5925*m.b37*m.b85 - 59274*m.b37*m.b181 + 6802*m.b38*m.b41
                        - 10028*m.b38*m.b47 + 5925*m.b38*m.b86 - 59274*m.b38*m.b182 + 6802*m.b39*m.b42 - 10028*m.b39*
                       m.b48 + 5925*m.b39*m.b87 - 59274*m.b39*m.b183 + 239529*m.b40*m.b43 + 172990*m.b40*m.b88 + 66126*
                       m.b40*m.b184 + 239529*m.b41*m.b44 + 172990*m.b41*m.b89 + 66126*m.b41*m.b185 + 239529*m.b42*m.b45
                        + 172990*m.b42*m.b90 + 66126*m.b42*m.b186 - 210013*m.b43*m.b46 + 21530*m.b43*m.b91 - 263520*
                       m.b43*m.b187 - 210013*m.b44*m.b47 + 21530*m.b44*m.b92 - 263520*m.b44*m.b188 - 210013*m.b45*m.b48
                        + 21530*m.b45*m.b93 - 263520*m.b45*m.b189 - 161687*m.b46*m.b94 + 71160*m.b46*m.b190 - 161687*
                       m.b47*m.b95 + 71160*m.b47*m.b191 - 161687*m.b48*m.b96 + 71160*m.b48*m.b192 + 518*m.b49*m.b52 - 
                       199442*m.b49*m.b58 - 85329*m.b49*m.b61 + 249503*m.b49*m.b85 + 21544*m.b49*m.b97 + 518*m.b50*m.b53
                        - 199442*m.b50*m.b59 - 85329*m.b50*m.b62 + 249503*m.b50*m.b86 + 21544*m.b50*m.b98 + 518*m.b51*
                       m.b54 - 199442*m.b51*m.b60 - 85329*m.b51*m.b63 + 249503*m.b51*m.b87 + 21544*m.b51*m.b99 + 3516*
                       m.b52*m.b55 - 123113*m.b52*m.b64 - 129423*m.b52*m.b88 + 27293*m.b52*m.b100 + 3516*m.b53*m.b56 - 
                       123113*m.b53*m.b65 - 129423*m.b53*m.b89 + 27293*m.b53*m.b101 + 3516*m.b54*m.b57 - 123113*m.b54*
                       m.b66 - 129423*m.b54*m.b90 + 27293*m.b54*m.b102 + 7210*m.b55*m.b58 + 57520*m.b55*m.b67 + 16931*
                       m.b55*m.b91 + 4095*m.b55*m.b103 + 7210*m.b56*m.b59 + 57520*m.b56*m.b68 + 16931*m.b56*m.b92 + 4095
                       *m.b56*m.b104 + 7210*m.b57*m.b60 + 57520*m.b57*m.b69 + 16931*m.b57*m.b93 + 4095*m.b57*m.b105 - 
                       213217*m.b58*m.b70 + 5736*m.b58*m.b94 + 69132*m.b58*m.b106 - 213217*m.b59*m.b71 + 5736*m.b59*
                       m.b95 + 69132*m.b59*m.b107 - 213217*m.b60*m.b72 + 5736*m.b60*m.b96 + 69132*m.b60*m.b108 - 7205*
                       m.b61*m.b64 - 71813*m.b61*m.b70 - 48799*m.b61*m.b73 + 80120*m.b61*m.b109 - 7205*m.b62*m.b65 - 
                       71813*m.b62*m.b71 - 48799*m.b62*m.b74 + 80120*m.b62*m.b110 - 7205*m.b63*m.b66 - 71813*m.b63*m.b72
                        - 48799*m.b63*m.b75 + 80120*m.b63*m.b111 - 35730*m.b64*m.b67 - 145007*m.b64*m.b76 - 20447*m.b64*
                       m.b112 - 35730*m.b65*m.b68 - 145007*m.b65*m.b77 - 20447*m.b65*m.b113 - 35730*m.b66*m.b69 - 145007
                       *m.b66*m.b78 - 20447*m.b66*m.b114 - 35840*m.b67*m.b70 - 106982*m.b67*m.b79 - 50522*m.b67*m.b115
                        - 35840*m.b68*m.b71 - 106982*m.b68*m.b80 - 50522*m.b68*m.b116 - 35840*m.b69*m.b72 - 106982*m.b69
                       *m.b81 - 50522*m.b69*m.b117 - 59739*m.b70*m.b82 + 199401*m.b70*m.b118 - 59739*m.b71*m.b83 + 
                       199401*m.b71*m.b119 - 59739*m.b72*m.b84 + 199401*m.b72*m.b120 - 32739*m.b73*m.b76 + 57198*m.b73*
                       m.b82 + 53863*m.b73*m.b85 - 19814*m.b73*m.b121 - 32739*m.b74*m.b77 + 57198*m.b74*m.b83 + 53863*
                       m.b74*m.b86 - 19814*m.b74*m.b122 - 32739*m.b75*m.b78 + 57198*m.b75*m.b84 + 53863*m.b75*m.b87 - 
                       19814*m.b75*m.b123 - 33479*m.b76*m.b79 + 44396*m.b76*m.b88 - 123350*m.b76*m.b124 - 33479*m.b77*
                       m.b80 + 44396*m.b77*m.b89 - 123350*m.b77*m.b125 - 33479*m.b78*m.b81 + 44396*m.b78*m.b90 - 123350*
                       m.b78*m.b126 - 159143*m.b79*m.b82 - 3415*m.b79*m.b91 - 10639*m.b79*m.b127 - 159143*m.b80*m.b83 - 
                       3415*m.b80*m.b92 - 10639*m.b80*m.b128 - 159143*m.b81*m.b84 - 3415*m.b81*m.b93 - 10639*m.b81*
                       m.b129 - 66393*m.b82*m.b94 - 211055*m.b82*m.b130 - 66393*m.b83*m.b95 - 211055*m.b83*m.b131 - 
                       66393*m.b84*m.b96 - 211055*m.b84*m.b132 - 46127*m.b85*m.b88 - 38270*m.b85*m.b94 - 118666*m.b85*
                       m.b133 - 46127*m.b86*m.b89 - 38270*m.b86*m.b95 - 118666*m.b86*m.b134 - 46127*m.b87*m.b90 - 38270*
                       m.b87*m.b96 - 118666*m.b87*m.b135 + 87214*m.b88*m.b91 - 87308*m.b88*m.b136 + 87214*m.b89*m.b92 - 
                       87308*m.b89*m.b137 + 87214*m.b90*m.b93 - 87308*m.b90*m.b138 - 142766*m.b91*m.b94 + 358*m.b91*
                       m.b139 - 142766*m.b92*m.b95 + 358*m.b92*m.b140 - 142766*m.b93*m.b96 + 358*m.b93*m.b141 - 18589*
                       m.b94*m.b142 - 18589*m.b95*m.b143 - 18589*m.b96*m.b144 - 60620*m.b97*m.b100 - 6182*m.b97*m.b106
                        - 55818*m.b97*m.b109 + 45445*m.b97*m.b133 + 66153*m.b97*m.b145 - 60620*m.b98*m.b101 - 6182*m.b98
                       *m.b107 - 55818*m.b98*m.b110 + 45445*m.b98*m.b134 + 66153*m.b98*m.b146 - 60620*m.b99*m.b102 - 
                       6182*m.b99*m.b108 - 55818*m.b99*m.b111 + 45445*m.b99*m.b135 + 66153*m.b99*m.b147 - 118726*m.b100*
                       m.b103 + 65347*m.b100*m.b112 + 145409*m.b100*m.b136 + 43018*m.b100*m.b148 - 118726*m.b101*m.b104
                        + 65347*m.b101*m.b113 + 145409*m.b101*m.b137 + 43018*m.b101*m.b149 - 118726*m.b102*m.b105 + 
                       65347*m.b102*m.b114 + 145409*m.b102*m.b138 + 43018*m.b102*m.b150 - 107024*m.b103*m.b106 - 134486*
                       m.b103*m.b115 + 157746*m.b103*m.b139 - 32135*m.b103*m.b151 - 107024*m.b104*m.b107 - 134486*m.b104
                       *m.b116 + 157746*m.b104*m.b140 - 32135*m.b104*m.b152 - 107024*m.b105*m.b108 - 134486*m.b105*
                       m.b117 + 157746*m.b105*m.b141 - 32135*m.b105*m.b153 + 217460*m.b106*m.b118 - 168382*m.b106*m.b142
                        - 145081*m.b106*m.b154 + 217460*m.b107*m.b119 - 168382*m.b107*m.b143 - 145081*m.b107*m.b155 + 
                       217460*m.b108*m.b120 - 168382*m.b108*m.b144 - 145081*m.b108*m.b156 - 200801*m.b109*m.b112 + 11955
                       *m.b109*m.b118 - 37270*m.b109*m.b121 + 57154*m.b109*m.b157 - 200801*m.b110*m.b113 + 11955*m.b110*
                       m.b119 - 37270*m.b110*m.b122 + 57154*m.b110*m.b158 - 200801*m.b111*m.b114 + 11955*m.b111*m.b120
                        - 37270*m.b111*m.b123 + 57154*m.b111*m.b159 + 10401*m.b112*m.b115 - 26462*m.b112*m.b124 - 142806
                       *m.b112*m.b160 + 10401*m.b113*m.b116 - 26462*m.b113*m.b125 - 142806*m.b113*m.b161 + 10401*m.b114*
                       m.b117 - 26462*m.b114*m.b126 - 142806*m.b114*m.b162 + 220165*m.b115*m.b118 - 121903*m.b115*m.b127
                        + 26088*m.b115*m.b163 + 220165*m.b116*m.b119 - 121903*m.b116*m.b128 + 26088*m.b116*m.b164 + 
                       220165*m.b117*m.b120 - 121903*m.b117*m.b129 + 26088*m.b117*m.b165 - 35760*m.b118*m.b130 - 152879*
                       m.b118*m.b166 - 35760*m.b119*m.b131 - 152879*m.b119*m.b167 - 35760*m.b120*m.b132 - 152879*m.b120*
                       m.b168 + 18941*m.b121*m.b124 + 44031*m.b121*m.b130 + 42768*m.b121*m.b133 + 114432*m.b121*m.b169
                        + 18941*m.b122*m.b125 + 44031*m.b122*m.b131 + 42768*m.b122*m.b134 + 114432*m.b122*m.b170 + 18941
                       *m.b123*m.b126 + 44031*m.b123*m.b132 + 42768*m.b123*m.b135 + 114432*m.b123*m.b171 - 91520*m.b124*
                       m.b127 + 78481*m.b124*m.b136 + 92873*m.b124*m.b172 - 91520*m.b125*m.b128 + 78481*m.b125*m.b137 + 
                       92873*m.b125*m.b173 - 91520*m.b126*m.b129 + 78481*m.b126*m.b138 + 92873*m.b126*m.b174 - 8014*
                       m.b127*m.b130 - 167760*m.b127*m.b139 + 176922*m.b127*m.b175 - 8014*m.b128*m.b131 - 167760*m.b128*
                       m.b140 + 176922*m.b128*m.b176 - 8014*m.b129*m.b132 - 167760*m.b129*m.b141 + 176922*m.b129*m.b177
                        + 135461*m.b130*m.b142 + 197916*m.b130*m.b178 + 135461*m.b131*m.b143 + 197916*m.b131*m.b179 + 
                       135461*m.b132*m.b144 + 197916*m.b132*m.b180 - 57916*m.b133*m.b136 - 15708*m.b133*m.b142 + 65118*
                       m.b133*m.b181 - 57916*m.b134*m.b137 - 15708*m.b134*m.b143 + 65118*m.b134*m.b182 - 57916*m.b135*
                       m.b138 - 15708*m.b135*m.b144 + 65118*m.b135*m.b183 - 12970*m.b136*m.b139 + 160862*m.b136*m.b184
                        - 12970*m.b137*m.b140 + 160862*m.b137*m.b185 - 12970*m.b138*m.b141 + 160862*m.b138*m.b186 + 3757
                       *m.b139*m.b142 - 153795*m.b139*m.b187 + 3757*m.b140*m.b143 - 153795*m.b140*m.b188 + 3757*m.b141*
                       m.b144 - 153795*m.b141*m.b189 - 138372*m.b142*m.b190 - 138372*m.b143*m.b191 - 138372*m.b144*
                       m.b192 + 70330*m.b145*m.b148 + 117426*m.b145*m.b154 - 814*m.b145*m.b157 - 95897*m.b145*m.b181 + 
                       70330*m.b146*m.b149 + 117426*m.b146*m.b155 - 814*m.b146*m.b158 - 95897*m.b146*m.b182 + 70330*
                       m.b147*m.b150 + 117426*m.b147*m.b156 - 814*m.b147*m.b159 - 95897*m.b147*m.b183 - 52404*m.b148*
                       m.b151 - 15513*m.b148*m.b160 - 76326*m.b148*m.b184 - 52404*m.b149*m.b152 - 15513*m.b149*m.b161 - 
                       76326*m.b149*m.b185 - 52404*m.b150*m.b153 - 15513*m.b150*m.b162 - 76326*m.b150*m.b186 + 49257*
                       m.b151*m.b154 - 47833*m.b151*m.b163 + 109660*m.b151*m.b187 + 49257*m.b152*m.b155 - 47833*m.b152*
                       m.b164 + 109660*m.b152*m.b188 + 49257*m.b153*m.b156 - 47833*m.b153*m.b165 + 109660*m.b153*m.b189
                        - 92699*m.b154*m.b166 - 117166*m.b154*m.b190 - 92699*m.b155*m.b167 - 117166*m.b155*m.b191 - 
                       92699*m.b156*m.b168 - 117166*m.b156*m.b192 - 147014*m.b157*m.b160 - 10849*m.b157*m.b166 - 73902*
                       m.b157*m.b169 - 147014*m.b158*m.b161 - 10849*m.b158*m.b167 - 73902*m.b158*m.b170 - 147014*m.b159*
                       m.b162 - 10849*m.b159*m.b168 - 73902*m.b159*m.b171 + 60835*m.b160*m.b163 - 210805*m.b160*m.b172
                        + 60835*m.b161*m.b164 - 210805*m.b161*m.b173 + 60835*m.b162*m.b165 - 210805*m.b162*m.b174 - 
                       232629*m.b163*m.b166 - 82260*m.b163*m.b175 - 232629*m.b164*m.b167 - 82260*m.b164*m.b176 - 232629*
                       m.b165*m.b168 - 82260*m.b165*m.b177 + 182737*m.b166*m.b178 + 182737*m.b167*m.b179 + 182737*m.b168
                       *m.b180 + 159594*m.b169*m.b172 - 16941*m.b169*m.b178 + 43367*m.b169*m.b181 + 159594*m.b170*m.b173
                        - 16941*m.b170*m.b179 + 43367*m.b170*m.b182 + 159594*m.b171*m.b174 - 16941*m.b171*m.b180 + 43367
                       *m.b171*m.b183 + 42222*m.b172*m.b175 - 112735*m.b172*m.b184 + 42222*m.b173*m.b176 - 112735*m.b173
                       *m.b185 + 42222*m.b174*m.b177 - 112735*m.b174*m.b186 + 98331*m.b175*m.b178 + 103757*m.b175*m.b187
                        + 98331*m.b176*m.b179 + 103757*m.b176*m.b188 + 98331*m.b177*m.b180 + 103757*m.b177*m.b189 - 
                       116766*m.b178*m.b190 - 116766*m.b179*m.b191 - 116766*m.b180*m.b192 - 81425*m.b181*m.b184 + 96345*
                       m.b181*m.b190 - 81425*m.b182*m.b185 + 96345*m.b182*m.b191 - 81425*m.b183*m.b186 + 96345*m.b183*
                       m.b192 - 100988*m.b184*m.b187 - 100988*m.b185*m.b188 - 100988*m.b186*m.b189 + 98051*m.b187*m.b190
                        + 98051*m.b188*m.b191 + 98051*m.b189*m.b192, sense=minimize)

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
