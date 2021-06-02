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

m.obj = Objective(expr=67634*m.b1*m.b22 - 83602*m.b1*m.b4 + 61711*m.b1*m.b25 - 59956*m.b1*m.b169 - 83602*m.b2*m.b5 + 
                       67634*m.b2*m.b23 + 61711*m.b2*m.b26 - 59956*m.b2*m.b170 - 83602*m.b3*m.b6 + 67634*m.b3*m.b24 + 
                       61711*m.b3*m.b27 - 59956*m.b3*m.b171 + 127500*m.b4*m.b7 + 35260*m.b4*m.b28 - 110030*m.b4*m.b172
                        + 127500*m.b5*m.b8 + 35260*m.b5*m.b29 - 110030*m.b5*m.b173 + 127500*m.b6*m.b9 + 35260*m.b6*m.b30
                        - 110030*m.b6*m.b174 - 68458*m.b7*m.b10 - 22985*m.b7*m.b31 - 35743*m.b7*m.b175 - 68458*m.b8*
                       m.b11 - 22985*m.b8*m.b32 - 35743*m.b8*m.b176 - 68458*m.b9*m.b12 - 22985*m.b9*m.b33 - 35743*m.b9*
                       m.b177 + 173612*m.b10*m.b13 + 199680*m.b10*m.b34 + 92582*m.b10*m.b178 + 173612*m.b11*m.b14 + 
                       199680*m.b11*m.b35 + 92582*m.b11*m.b179 + 173612*m.b12*m.b15 + 199680*m.b12*m.b36 + 92582*m.b12*
                       m.b180 + 117135*m.b13*m.b16 - 147716*m.b13*m.b37 + 130308*m.b13*m.b181 + 117135*m.b14*m.b17 - 
                       147716*m.b14*m.b38 + 130308*m.b14*m.b182 + 117135*m.b15*m.b18 - 147716*m.b15*m.b39 + 130308*m.b15
                       *m.b183 + 91667*m.b16*m.b19 + 153955*m.b16*m.b40 - 21093*m.b16*m.b184 + 91667*m.b17*m.b20 + 
                       153955*m.b17*m.b41 - 21093*m.b17*m.b185 + 91667*m.b18*m.b21 + 153955*m.b18*m.b42 - 21093*m.b18*
                       m.b186 + 74165*m.b19*m.b22 - 220722*m.b19*m.b43 - 162288*m.b19*m.b187 + 74165*m.b20*m.b23 - 
                       220722*m.b20*m.b44 - 162288*m.b20*m.b188 + 74165*m.b21*m.b24 - 220722*m.b21*m.b45 - 162288*m.b21*
                       m.b189 + 35287*m.b22*m.b46 - 73662*m.b22*m.b190 + 35287*m.b23*m.b47 - 73662*m.b23*m.b191 + 35287*
                       m.b24*m.b48 - 73662*m.b24*m.b192 + 47953*m.b25*m.b28 + 2925*m.b25*m.b46 - 24145*m.b25*m.b49 + 
                       47953*m.b26*m.b29 + 2925*m.b26*m.b47 - 24145*m.b26*m.b50 + 47953*m.b27*m.b30 + 2925*m.b27*m.b48
                        - 24145*m.b27*m.b51 - 122136*m.b28*m.b31 - 77871*m.b28*m.b52 - 122136*m.b29*m.b32 - 77871*m.b29*
                       m.b53 - 122136*m.b30*m.b33 - 77871*m.b30*m.b54 - 129158*m.b31*m.b34 - 45165*m.b31*m.b55 - 129158*
                       m.b32*m.b35 - 45165*m.b32*m.b56 - 129158*m.b33*m.b36 - 45165*m.b33*m.b57 - 44654*m.b34*m.b37 + 
                       18064*m.b34*m.b58 - 44654*m.b35*m.b38 + 18064*m.b35*m.b59 - 44654*m.b36*m.b39 + 18064*m.b36*m.b60
                        - 164293*m.b37*m.b40 - 62562*m.b37*m.b61 - 164293*m.b38*m.b41 - 62562*m.b38*m.b62 - 164293*m.b39
                       *m.b42 - 62562*m.b39*m.b63 + 15254*m.b40*m.b43 - 73788*m.b40*m.b64 + 15254*m.b41*m.b44 - 73788*
                       m.b41*m.b65 + 15254*m.b42*m.b45 - 73788*m.b42*m.b66 + 67357*m.b43*m.b46 + 145724*m.b43*m.b67 + 
                       67357*m.b44*m.b47 + 145724*m.b44*m.b68 + 67357*m.b45*m.b48 + 145724*m.b45*m.b69 + 77518*m.b46*
                       m.b70 + 77518*m.b47*m.b71 + 77518*m.b48*m.b72 + 73006*m.b49*m.b52 - 97425*m.b49*m.b70 - 36871*
                       m.b49*m.b73 + 73006*m.b50*m.b53 - 97425*m.b50*m.b71 - 36871*m.b50*m.b74 + 73006*m.b51*m.b54 - 
                       97425*m.b51*m.b72 - 36871*m.b51*m.b75 - 85230*m.b52*m.b55 - 63550*m.b52*m.b76 - 85230*m.b53*m.b56
                        - 63550*m.b53*m.b77 - 85230*m.b54*m.b57 - 63550*m.b54*m.b78 - 153638*m.b55*m.b58 + 84496*m.b55*
                       m.b79 - 153638*m.b56*m.b59 + 84496*m.b56*m.b80 - 153638*m.b57*m.b60 + 84496*m.b57*m.b81 + 7440*
                       m.b58*m.b61 - 67520*m.b58*m.b82 + 7440*m.b59*m.b62 - 67520*m.b59*m.b83 + 7440*m.b60*m.b63 - 67520
                       *m.b60*m.b84 + 97476*m.b61*m.b64 - 234690*m.b61*m.b85 + 97476*m.b62*m.b65 - 234690*m.b62*m.b86 + 
                       97476*m.b63*m.b66 - 234690*m.b63*m.b87 + 114707*m.b64*m.b67 + 218718*m.b64*m.b88 + 114707*m.b65*
                       m.b68 + 218718*m.b65*m.b89 + 114707*m.b66*m.b69 + 218718*m.b66*m.b90 - 72968*m.b67*m.b70 + 54754*
                       m.b67*m.b91 - 72968*m.b68*m.b71 + 54754*m.b68*m.b92 - 72968*m.b69*m.b72 + 54754*m.b69*m.b93 - 
                       169837*m.b70*m.b94 - 169837*m.b71*m.b95 - 169837*m.b72*m.b96 - 18652*m.b73*m.b76 + 114918*m.b73*
                       m.b94 - 6803*m.b73*m.b97 - 18652*m.b74*m.b77 + 114918*m.b74*m.b95 - 6803*m.b74*m.b98 - 18652*
                       m.b75*m.b78 + 114918*m.b75*m.b96 - 6803*m.b75*m.b99 - 35802*m.b76*m.b79 - 95280*m.b76*m.b100 - 
                       35802*m.b77*m.b80 - 95280*m.b77*m.b101 - 35802*m.b78*m.b81 - 95280*m.b78*m.b102 + 70821*m.b79*
                       m.b82 - 58023*m.b79*m.b103 + 70821*m.b80*m.b83 - 58023*m.b80*m.b104 + 70821*m.b81*m.b84 - 58023*
                       m.b81*m.b105 - 61946*m.b82*m.b85 - 264072*m.b82*m.b106 - 61946*m.b83*m.b86 - 264072*m.b83*m.b107
                        - 61946*m.b84*m.b87 - 264072*m.b84*m.b108 - 92130*m.b85*m.b88 + 16108*m.b85*m.b109 - 92130*m.b86
                       *m.b89 + 16108*m.b86*m.b110 - 92130*m.b87*m.b90 + 16108*m.b87*m.b111 + 159379*m.b88*m.b91 + 
                       204734*m.b88*m.b112 + 159379*m.b89*m.b92 + 204734*m.b89*m.b113 + 159379*m.b90*m.b93 + 204734*
                       m.b90*m.b114 - 189099*m.b91*m.b94 - 64588*m.b91*m.b115 - 189099*m.b92*m.b95 - 64588*m.b92*m.b116
                        - 189099*m.b93*m.b96 - 64588*m.b93*m.b117 + 130590*m.b94*m.b118 + 130590*m.b95*m.b119 + 130590*
                       m.b96*m.b120 - 8447*m.b97*m.b100 + 90736*m.b97*m.b118 + 38420*m.b97*m.b121 - 8447*m.b98*m.b101 + 
                       90736*m.b98*m.b119 + 38420*m.b98*m.b122 - 8447*m.b99*m.b102 + 90736*m.b99*m.b120 + 38420*m.b99*
                       m.b123 + 22308*m.b100*m.b103 + 177432*m.b100*m.b124 + 22308*m.b101*m.b104 + 177432*m.b101*m.b125
                        + 22308*m.b102*m.b105 + 177432*m.b102*m.b126 - 14134*m.b103*m.b106 - 28668*m.b103*m.b127 - 14134
                       *m.b104*m.b107 - 28668*m.b104*m.b128 - 14134*m.b105*m.b108 - 28668*m.b105*m.b129 - 61805*m.b106*
                       m.b109 - 22047*m.b106*m.b130 - 61805*m.b107*m.b110 - 22047*m.b107*m.b131 - 61805*m.b108*m.b111 - 
                       22047*m.b108*m.b132 + 29936*m.b109*m.b112 - 36716*m.b109*m.b133 + 29936*m.b110*m.b113 - 36716*
                       m.b110*m.b134 + 29936*m.b111*m.b114 - 36716*m.b111*m.b135 - 189188*m.b112*m.b115 + 56108*m.b112*
                       m.b136 - 189188*m.b113*m.b116 + 56108*m.b113*m.b137 - 189188*m.b114*m.b117 + 56108*m.b114*m.b138
                        + 87321*m.b115*m.b118 + 43200*m.b115*m.b139 + 87321*m.b116*m.b119 + 43200*m.b116*m.b140 + 87321*
                       m.b117*m.b120 + 43200*m.b117*m.b141 - 105343*m.b118*m.b142 - 105343*m.b119*m.b143 - 105343*m.b120
                       *m.b144 + 1787*m.b121*m.b124 - 39963*m.b121*m.b142 - 49240*m.b121*m.b145 + 1787*m.b122*m.b125 - 
                       39963*m.b122*m.b143 - 49240*m.b122*m.b146 + 1787*m.b123*m.b126 - 39963*m.b123*m.b144 - 49240*
                       m.b123*m.b147 - 19759*m.b124*m.b127 - 51266*m.b124*m.b148 - 19759*m.b125*m.b128 - 51266*m.b125*
                       m.b149 - 19759*m.b126*m.b129 - 51266*m.b126*m.b150 - 156795*m.b127*m.b130 - 90008*m.b127*m.b151
                        - 156795*m.b128*m.b131 - 90008*m.b128*m.b152 - 156795*m.b129*m.b132 - 90008*m.b129*m.b153 + 
                       76764*m.b130*m.b133 - 54058*m.b130*m.b154 + 76764*m.b131*m.b134 - 54058*m.b131*m.b155 + 76764*
                       m.b132*m.b135 - 54058*m.b132*m.b156 - 20555*m.b133*m.b136 - 275957*m.b133*m.b157 - 20555*m.b134*
                       m.b137 - 275957*m.b134*m.b158 - 20555*m.b135*m.b138 - 275957*m.b135*m.b159 + 17070*m.b136*m.b139
                        - 154864*m.b136*m.b160 + 17070*m.b137*m.b140 - 154864*m.b137*m.b161 + 17070*m.b138*m.b141 - 
                       154864*m.b138*m.b162 - 162791*m.b139*m.b142 - 8148*m.b139*m.b163 - 162791*m.b140*m.b143 - 8148*
                       m.b140*m.b164 - 162791*m.b141*m.b144 - 8148*m.b141*m.b165 - 3896*m.b142*m.b166 - 3896*m.b143*
                       m.b167 - 3896*m.b144*m.b168 - 105352*m.b145*m.b148 + 45364*m.b145*m.b166 - 37043*m.b145*m.b169 - 
                       105352*m.b146*m.b149 + 45364*m.b146*m.b167 - 37043*m.b146*m.b170 - 105352*m.b147*m.b150 + 45364*
                       m.b147*m.b168 - 37043*m.b147*m.b171 + 211004*m.b148*m.b151 - 65416*m.b148*m.b172 + 211004*m.b149*
                       m.b152 - 65416*m.b149*m.b173 + 211004*m.b150*m.b153 - 65416*m.b150*m.b174 - 12091*m.b151*m.b154
                        + 47044*m.b151*m.b175 - 12091*m.b152*m.b155 + 47044*m.b152*m.b176 - 12091*m.b153*m.b156 + 47044*
                       m.b153*m.b177 - 64916*m.b154*m.b157 - 158531*m.b154*m.b178 - 64916*m.b155*m.b158 - 158531*m.b155*
                       m.b179 - 64916*m.b156*m.b159 - 158531*m.b156*m.b180 - 19908*m.b157*m.b160 + 66609*m.b157*m.b181
                        - 19908*m.b158*m.b161 + 66609*m.b158*m.b182 - 19908*m.b159*m.b162 + 66609*m.b159*m.b183 - 22331*
                       m.b160*m.b163 - 32557*m.b160*m.b184 - 22331*m.b161*m.b164 - 32557*m.b161*m.b185 - 22331*m.b162*
                       m.b165 - 32557*m.b162*m.b186 - 218808*m.b163*m.b166 - 85264*m.b163*m.b187 - 218808*m.b164*m.b167
                        - 85264*m.b164*m.b188 - 218808*m.b165*m.b168 - 85264*m.b165*m.b189 - 75908*m.b166*m.b190 - 75908
                       *m.b167*m.b191 - 75908*m.b168*m.b192 - 75258*m.b169*m.b172 + 15236*m.b169*m.b190 - 75258*m.b170*
                       m.b173 + 15236*m.b170*m.b191 - 75258*m.b171*m.b174 + 15236*m.b171*m.b192 - 72030*m.b172*m.b175 - 
                       72030*m.b173*m.b176 - 72030*m.b174*m.b177 - 3058*m.b175*m.b178 - 3058*m.b176*m.b179 - 3058*m.b177
                       *m.b180 + 33988*m.b178*m.b181 + 33988*m.b179*m.b182 + 33988*m.b180*m.b183 + 116509*m.b181*m.b184
                        + 116509*m.b182*m.b185 + 116509*m.b183*m.b186 + 59421*m.b184*m.b187 + 59421*m.b185*m.b188 + 
                       59421*m.b186*m.b189 - 277077*m.b187*m.b190 - 277077*m.b188*m.b191 - 277077*m.b189*m.b192
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
