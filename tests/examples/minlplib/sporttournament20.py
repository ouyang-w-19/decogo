#  MINLP written by GAMS Convert at 04/21/18 13:54:17
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          1        0        0        1        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        191        1      190        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        191        1      190        0


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
m.x191 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=m.x191, sense=maximize)

m.c1 = Constraint(expr=2*m.b1*m.b5 - 2*m.b1 - 2*m.b5 + 2*m.b1*m.b8 - 2*m.b8 + 2*m.b1*m.b23 - 4*m.b23 - 2*m.b1*m.b35 + 4*
                       m.b35 + 2*m.b2*m.b3 - 2*m.b2 - 2*m.b3 + 2*m.b2*m.b33 - 4*m.b33 - 2*m.b2*m.b144 + 2*m.b2*m.b150 + 
                       2*m.b3*m.b84 - 2*m.b84 - 2*m.b3*m.b106 + 2*m.b106 + 2*m.b3*m.b140 + 2*m.b4*m.b86 - 2*m.b4 - 2*
                       m.b86 + 2*m.b4*m.b107 - 2*m.b107 + 2*m.b4*m.b140 - 2*m.b4*m.b158 + 2*m.b5*m.b6 - 2*m.b6 + 2*m.b5*
                       m.b136 - 2*m.b5*m.b151 + 2*m.b6*m.b52 - 4*m.b52 + 2*m.b6*m.b72 - 4*m.b72 - 2*m.b6*m.b161 + 2*m.b7
                       *m.b17 - 2*m.b7 - 2*m.b17 + 2*m.b7*m.b103 - 4*m.b103 + 2*m.b8*m.b141 - 2*m.b8*m.b146 + 2*m.b8*
                       m.b162 + 2*m.b9*m.b27 - 2*m.b9 - 4*m.b27 - 2*m.b9*m.b39 - 2*m.b39 + 2*m.b9*m.b72 + 2*m.b9*m.b163
                        + 2*m.b10*m.b49 - 2*m.b10 - 2*m.b49 + 2*m.b10*m.b65 - 2*m.b65 + 2*m.b10*m.b68 - 2*m.b68 - 2*
                       m.b10*m.b133 + 2*m.b11*m.b47 - 2*m.b11 - 4*m.b47 + 2*m.b11*m.b157 + 2*m.b12*m.b32 - 4*m.b12 - 2*
                       m.b32 + 2*m.b12*m.b49 + 2*m.b12*m.b133 + 2*m.b12*m.b165 + 2*m.b13*m.b14 - 2*m.b13 - 4*m.b14 - 2*
                       m.b13*m.b34 + 2*m.b34 + 2*m.b13*m.b136 + 2*m.b13*m.b144 + 2*m.b14*m.b89 - 2*m.b89 + 2*m.b14*
                       m.b113 - 2*m.b113 + 2*m.b14*m.b135 + 2*m.b15*m.b26 - 2*m.b15 - 2*m.b26 + 2*m.b15*m.b38 - 2*m.b38
                        + 2*m.b15*m.b146 - 2*m.b15*m.b175 - 2*m.b16*m.b17 - 2*m.b16 + 2*m.b16*m.b45 - 2*m.b45 + 2*m.b16*
                       m.b62 - 4*m.b62 + 2*m.b16*m.b169 + 2*m.b17*m.b18 - 2*m.b18 + 2*m.b17*m.b61 - 4*m.b61 + 2*m.b18*
                       m.b62 + 2*m.b19*m.b20 - 2*m.b19 - 2*m.b20 + 2*m.b19*m.b21 - 2*m.b21 + 2*m.b19*m.b67 - 4*m.b67 - 2
                       *m.b19*m.b150 + 2*m.b20*m.b23 + 2*m.b20*m.b49 - 2*m.b20*m.b111 + 2*m.b111 + 2*m.b21*m.b23 + 2*
                       m.b21*m.b89 - 2*m.b21*m.b180 - 2*m.b22*m.b24 + 2*m.b22 - 2*m.b24 - 2*m.b22*m.b110 + 4*m.b110 - 2*
                       m.b22*m.b136 + 2*m.b22*m.b139 + 2*m.b23*m.b24 + 2*m.b24*m.b113 + 2*m.b24*m.b166 + 2*m.b25*m.b41
                        - 2*m.b25 - 2*m.b41 + 2*m.b25*m.b146 + 2*m.b25*m.b151 - 2*m.b25*m.b167 + 2*m.b26*m.b55 - 4*m.b55
                        - 2*m.b26*m.b73 - 2*m.b73 + 2*m.b26*m.b75 - 4*m.b75 + 2*m.b27*m.b56 - 4*m.b56 + 2*m.b27*m.b154
                        + 2*m.b27*m.b167 + 2*m.b28*m.b29 - 2*m.b28 - 2*m.b29 - 2*m.b28*m.b44 + 2*m.b44 + 2*m.b28*m.b98
                        - 2*m.b98 + 2*m.b28*m.b171 + 2*m.b29*m.b59 - 2*m.b59 + 2*m.b29*m.b80 - 2*m.b80 - 2*m.b29*m.b157
                        + 2*m.b30*m.b31 - 2*m.b30 - 2*m.b31 + 2*m.b30*m.b124 - 2*m.b124 - 2*m.b30*m.b171 + 2*m.b30*
                       m.b172 + 2*m.b31*m.b80 + 2*m.b32*m.b33 - 2*m.b32*m.b34 + 2*m.b32*m.b108 - 2*m.b108 + 2*m.b33*
                       m.b36 - 4*m.b36 + 2*m.b33*m.b89 + 2*m.b34*m.b36 - 2*m.b34*m.b87 - 2*m.b87 - 2*m.b35*m.b37 - 2*
                       m.b37 - 2*m.b35*m.b88 + 2*m.b88 - 2*m.b35*m.b139 + 2*m.b36*m.b37 + 2*m.b36*m.b141 + 2*m.b37*
                       m.b161 + 2*m.b37*m.b166 + 2*m.b38*m.b40 - 2*m.b40 + 2*m.b38*m.b135 - 2*m.b38*m.b145 + 2*m.b39*
                       m.b54 - 4*m.b54 + 2*m.b39*m.b151 + 2*m.b39*m.b153 + 2*m.b40*m.b54 + 2*m.b40*m.b115 - 2*m.b115 - 2
                       *m.b40*m.b183 - 2*m.b41*m.b53 - 2*m.b53 + 2*m.b41*m.b75 + 2*m.b41*m.b94 - 4*m.b94 + 2*m.b42*
                       m.b152 - 4*m.b42 + 2*m.b42*m.b164 + 2*m.b42*m.b167 + 2*m.b42*m.b175 - 2*m.b43*m.b44 - 2*m.b43 + 2
                       *m.b43*m.b130 + 2*m.b43*m.b131 + 2*m.b43*m.b164 + 2*m.b44*m.b79 - 2*m.b79 - 2*m.b44*m.b184 + 2*
                       m.b45*m.b46 - 4*m.b46 + 2*m.b45*m.b121 - 2*m.b121 - 2*m.b45*m.b178 + 2*m.b46*m.b79 + 2*m.b46*
                       m.b102 - 2*m.b102 + 2*m.b46*m.b157 + 2*m.b47*m.b48 - 2*m.b48 + 2*m.b47*m.b101 - 4*m.b101 + 2*
                       m.b47*m.b171 + 2*m.b48*m.b102 - 2*m.b49*m.b110 - 2*m.b50*m.b141 + 4*m.b50 - 2*m.b50*m.b144 - 2*
                       m.b50*m.b160 - 2*m.b50*m.b182 - 2*m.b51*m.b153 - 2*m.b51 + 2*m.b51*m.b182 + 2*m.b51*m.b183 + 2*
                       m.b51*m.b186 + 2*m.b52*m.b74 - 4*m.b74 + 2*m.b52*m.b115 + 2*m.b52*m.b153 + 2*m.b53*m.b71 - 2*
                       m.b71 + 2*m.b53*m.b74 + 2*m.b53*m.b183 + 2*m.b54*m.b94 + 2*m.b54*m.b116 - 4*m.b116 + 2*m.b55*
                       m.b57 - 4*m.b57 + 2*m.b55*m.b156 + 2*m.b55*m.b175 + 2*m.b56*m.b58 - 4*m.b58 + 2*m.b56*m.b117 - 4*
                       m.b117 + 2*m.b56*m.b149 + 2*m.b57*m.b58 + 2*m.b57*m.b116 + 2*m.b57*m.b148 + 2*m.b58*m.b129 + 2*
                       m.b58*m.b170 + 2*m.b59*m.b61 - 2*m.b59*m.b130 + 2*m.b59*m.b178 - 2*m.b60*m.b80 + 2*m.b60 - 2*
                       m.b60*m.b100 - 2*m.b100 + 2*m.b60*m.b126 - 4*m.b126 - 2*m.b60*m.b128 + 2*m.b61*m.b99 - 2*m.b99 + 
                       2*m.b61*m.b126 + 2*m.b62*m.b63 - 2*m.b63 + 2*m.b62*m.b125 - 4*m.b125 + 2*m.b63*m.b126 - 2*m.b64*
                       m.b66 + 2*m.b64 - 2*m.b66 - 2*m.b64*m.b133 + 2*m.b65*m.b67 + 2*m.b65*m.b173 - 2*m.b65*m.b174 + 2*
                       m.b66*m.b67 + 2*m.b66*m.b150 + 2*m.b66*m.b174 + 2*m.b67*m.b69 - 2*m.b69 - 2*m.b68*m.b88 + 2*m.b68
                       *m.b144 + 2*m.b68*m.b159 + 2*m.b69*m.b85 - 2*m.b85 + 2*m.b69*m.b88 - 2*m.b69*m.b110 + 2*m.b70*
                       m.b71 - 2*m.b70 + 2*m.b70*m.b90 - 2*m.b90 - 2*m.b70*m.b151 + 2*m.b70*m.b186 + 2*m.b71*m.b73 - 2*
                       m.b71*m.b166 + 2*m.b72*m.b93 - 4*m.b93 + 2*m.b72*m.b162 + 2*m.b73*m.b92 - 2*m.b92 + 2*m.b73*m.b93
                        + 2*m.b74*m.b76 - 2*m.b76 + 2*m.b74*m.b116 + 2*m.b75*m.b77 - 4*m.b77 + 2*m.b75*m.b154 + 2*m.b76*
                       m.b77 + 2*m.b76*m.b93 - 2*m.b76*m.b131 + 2*m.b77*m.b119 + 2*m.b119 + 2*m.b77*m.b184 + 2*m.b78*
                       m.b122 - 2*m.b78 - 2*m.b122 - 2*m.b78*m.b143 + 2*m.b78*m.b169 + 2*m.b78*m.b184 + 2*m.b79*m.b124
                        - 2*m.b79*m.b147 + 2*m.b80*m.b188 - 2*m.b81*m.b84 + 2*m.b81 - 2*m.b81*m.b137 + 2*m.b82*m.b84 - 2
                       *m.b82 + 2*m.b82*m.b165 - 2*m.b83*m.b85 + 2*m.b83 - 2*m.b83*m.b134 - 2*m.b83*m.b150 + 2*m.b83*
                       m.b177 + 2*m.b84*m.b85 + 2*m.b85*m.b87 + 2*m.b86*m.b139 + 2*m.b86*m.b159 - 2*m.b86*m.b160 + 2*
                       m.b87*m.b109 - 2*m.b109 + 2*m.b87*m.b160 - 2*m.b88*m.b187 - 2*m.b89*m.b90 + 2*m.b90*m.b91 - 2*
                       m.b91 + 2*m.b90*m.b187 + 2*m.b91*m.b92 + 2*m.b91*m.b112 - 4*m.b112 - 2*m.b91*m.b146 - 2*m.b92*
                       m.b113 + 2*m.b92*m.b176 + 2*m.b93*m.b95 - 2*m.b95 + 2*m.b94*m.b96 - 4*m.b96 + 2*m.b94*m.b152 + 2*
                       m.b95*m.b96 + 2*m.b95*m.b131 - 2*m.b95*m.b190 + 2*m.b96*m.b97 + 2*m.b97 + 2*m.b96*m.b181 - 2*
                       m.b97*m.b98 - 2*m.b97*m.b129 - 2*m.b97*m.b156 + 2*m.b98*m.b100 + 2*m.b98*m.b181 + 2*m.b99*m.b101
                        - 2*m.b99*m.b142 + 2*m.b99*m.b170 + 2*m.b100*m.b101 + 2*m.b100*m.b142 + 2*m.b101*m.b103 + 2*
                       m.b102*m.b104 - 2*m.b104 - 2*m.b102*m.b132 + 2*m.b103*m.b104 + 2*m.b103*m.b132 + 2*m.b105*m.b107
                        - 2*m.b105 + 2*m.b105*m.b158 - 2*m.b106*m.b109 - 2*m.b106*m.b138 + 2*m.b106*m.b179 + 2*m.b107*
                       m.b109 - 2*m.b107*m.b173 + 2*m.b108*m.b137 + 2*m.b108*m.b158 - 2*m.b108*m.b180 + 2*m.b109*m.b180
                        - 2*m.b110*m.b185 + 2*m.b111*m.b112 - 2*m.b111*m.b155 - 2*m.b111*m.b186 + 2*m.b112*m.b145 + 2*
                       m.b112*m.b185 + 2*m.b113*m.b114 - 4*m.b114 + 2*m.b114*m.b145 + 2*m.b114*m.b168 + 2*m.b114*m.b176
                        + 2*m.b115*m.b117 - 2*m.b115*m.b163 + 2*m.b116*m.b118 - 4*m.b118 + 2*m.b117*m.b118 + 2*m.b117*
                       m.b190 + 2*m.b118*m.b120 - 2*m.b120 + 2*m.b118*m.b143 - 2*m.b119*m.b121 - 2*m.b119*m.b142 - 2*
                       m.b119*m.b154 + 2*m.b120*m.b121 - 2*m.b120*m.b156 + 2*m.b120*m.b178 + 2*m.b121*m.b123 - 2*m.b123
                        + 2*m.b122*m.b124 + 2*m.b122*m.b125 - 2*m.b122*m.b129 + 2*m.b123*m.b125 - 2*m.b123*m.b132 + 2*
                       m.b123*m.b147 - 2*m.b124*m.b189 + 2*m.b125*m.b189 + 2*m.b126*m.b127 - 2*m.b127 + 2*m.b127*m.b189
                        + 2*m.b128*m.b129 - 2*m.b128*m.b130 + 2*m.b128*m.b132 + 2*m.b130*m.b148 - 2*m.b131*m.b149 + 2*
                       m.b133*m.b134 - 2*m.b135*m.b136 - 2*m.b135*m.b153 + 2*m.b137*m.b138 - 2*m.b137*m.b159 - 2*m.b139*
                       m.b140 - 2*m.b140*m.b155 - 2*m.b141*m.b145 + 2*m.b142*m.b143 - 2*m.b143*m.b164 - 2*m.b147*m.b148
                        + 2*m.b147*m.b149 - 2*m.b148*m.b152 - 2*m.b149*m.b170 - 2*m.b152*m.b184 - 2*m.b154*m.b181 + 2*
                       m.b155*m.b180 + 2*m.b155*m.b185 + 2*m.b156*m.b163 - 2*m.b157*m.b172 - 2*m.b158*m.b179 - 2*m.b159*
                       m.b165 + 2*m.b160*m.b187 + 2*m.b161*m.b182 - 2*m.b161*m.b183 - 2*m.b162*m.b166 - 2*m.b162*m.b168
                        - 2*m.b163*m.b164 - 2*m.b165*m.b177 - 2*m.b167*m.b168 + 2*m.b168*m.b190 - 2*m.b169*m.b170 - 2*
                       m.b169*m.b171 - 2*m.b175*m.b176 - 2*m.b176*m.b190 - 2*m.b178*m.b181 - 2*m.b182*m.b185 - 2*m.b186*
                       m.b187 - 2*m.b188*m.b189 + m.x191 <= 0)
