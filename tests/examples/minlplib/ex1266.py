#  MINLP written by GAMS Convert at 04/21/18 13:51:43
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         96       43        7       46        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        181       43      138        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        476      404       72        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,5),initialize=1)
m.x2 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,5),initialize=2)
m.x8 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,5),initialize=2)
m.x15 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,5),initialize=1)
m.x21 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,5),initialize=2)
m.x27 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,5),initialize=1)
m.x32 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x34 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x35 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x36 = Var(within=Reals,bounds=(0,5),initialize=0)
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
m.x151 = Var(within=Reals,bounds=(0,15),initialize=8)
m.x152 = Var(within=Reals,bounds=(0,12),initialize=7)
m.x153 = Var(within=Reals,bounds=(0,8),initialize=0)
m.x154 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x155 = Var(within=Reals,bounds=(0,4),initialize=0)
m.x156 = Var(within=Reals,bounds=(0,2),initialize=0)
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

m.obj = Objective(expr=   0.1*m.b145 + 0.2*m.b146 + 0.3*m.b147 + 0.4*m.b148 + 0.5*m.b149 + m.x151 + m.x152 + m.x153
                        + m.x154 + m.x155 + m.x156, sense=minimize)

m.c2 = Constraint(expr=m.x151*m.x1 + m.x152*m.x2 + m.x153*m.x3 + m.x154*m.x4 + m.x155*m.x5 + m.x156*m.x6 >= 8)

m.c3 = Constraint(expr=m.x151*m.x7 + m.x152*m.x8 + m.x153*m.x9 + m.x154*m.x10 + m.x155*m.x11 + m.x156*m.x12 >= 16)

m.c4 = Constraint(expr=m.x151*m.x13 + m.x152*m.x14 + m.x153*m.x15 + m.x154*m.x16 + m.x155*m.x17 + m.x156*m.x18 >= 12)

m.c5 = Constraint(expr=m.x151*m.x19 + m.x152*m.x20 + m.x153*m.x21 + m.x154*m.x22 + m.x155*m.x23 + m.x156*m.x24 >= 7)

m.c6 = Constraint(expr=m.x151*m.x25 + m.x152*m.x26 + m.x153*m.x27 + m.x154*m.x28 + m.x155*m.x29 + m.x156*m.x30 >= 14)

m.c7 = Constraint(expr=m.x151*m.x31 + m.x152*m.x32 + m.x153*m.x33 + m.x154*m.x34 + m.x155*m.x35 + m.x156*m.x36 >= 16)

m.c8 = Constraint(expr= - 330*m.x1 - 360*m.x7 - 380*m.x13 - 430*m.x19 - 490*m.x25 - 530*m.x31 + 2100*m.b145 <= 0)

m.c9 = Constraint(expr= - 330*m.x2 - 360*m.x8 - 380*m.x14 - 430*m.x20 - 490*m.x26 - 530*m.x32 + 2100*m.b146 <= 0)

m.c10 = Constraint(expr= - 330*m.x3 - 360*m.x9 - 380*m.x15 - 430*m.x21 - 490*m.x27 - 530*m.x33 + 2100*m.b147 <= 0)

m.c11 = Constraint(expr= - 330*m.x4 - 360*m.x10 - 380*m.x16 - 430*m.x22 - 490*m.x28 - 530*m.x34 + 2100*m.b148 <= 0)

m.c12 = Constraint(expr= - 330*m.x5 - 360*m.x11 - 380*m.x17 - 430*m.x23 - 490*m.x29 - 530*m.x35 + 2100*m.b149 <= 0)

m.c13 = Constraint(expr= - 330*m.x6 - 360*m.x12 - 380*m.x18 - 430*m.x24 - 490*m.x30 - 530*m.x36 + 2100*m.b150 <= 0)

m.c14 = Constraint(expr=   330*m.x1 + 360*m.x7 + 380*m.x13 + 430*m.x19 + 490*m.x25 + 530*m.x31 - 2200*m.b145 <= 0)

m.c15 = Constraint(expr=   330*m.x2 + 360*m.x8 + 380*m.x14 + 430*m.x20 + 490*m.x26 + 530*m.x32 - 2200*m.b146 <= 0)

m.c16 = Constraint(expr=   330*m.x3 + 360*m.x9 + 380*m.x15 + 430*m.x21 + 490*m.x27 + 530*m.x33 - 2200*m.b147 <= 0)

m.c17 = Constraint(expr=   330*m.x4 + 360*m.x10 + 380*m.x16 + 430*m.x22 + 490*m.x28 + 530*m.x34 - 2200*m.b148 <= 0)

m.c18 = Constraint(expr=   330*m.x5 + 360*m.x11 + 380*m.x17 + 430*m.x23 + 490*m.x29 + 530*m.x35 - 2200*m.b149 <= 0)

m.c19 = Constraint(expr=   330*m.x6 + 360*m.x12 + 380*m.x18 + 430*m.x24 + 490*m.x30 + 530*m.x36 - 2200*m.b150 <= 0)

m.c20 = Constraint(expr= - m.x1 - m.x7 - m.x13 - m.x19 - m.x25 - m.x31 + m.b145 <= 0)

m.c21 = Constraint(expr= - m.x2 - m.x8 - m.x14 - m.x20 - m.x26 - m.x32 + m.b146 <= 0)

m.c22 = Constraint(expr= - m.x3 - m.x9 - m.x15 - m.x21 - m.x27 - m.x33 + m.b147 <= 0)

m.c23 = Constraint(expr= - m.x4 - m.x10 - m.x16 - m.x22 - m.x28 - m.x34 + m.b148 <= 0)

m.c24 = Constraint(expr= - m.x5 - m.x11 - m.x17 - m.x23 - m.x29 - m.x35 + m.b149 <= 0)

m.c25 = Constraint(expr= - m.x6 - m.x12 - m.x18 - m.x24 - m.x30 - m.x36 + m.b150 <= 0)

m.c26 = Constraint(expr=   m.x1 + m.x7 + m.x13 + m.x19 + m.x25 + m.x31 - 5*m.b145 <= 0)

m.c27 = Constraint(expr=   m.x2 + m.x8 + m.x14 + m.x20 + m.x26 + m.x32 - 5*m.b146 <= 0)

m.c28 = Constraint(expr=   m.x3 + m.x9 + m.x15 + m.x21 + m.x27 + m.x33 - 5*m.b147 <= 0)

m.c29 = Constraint(expr=   m.x4 + m.x10 + m.x16 + m.x22 + m.x28 + m.x34 - 5*m.b148 <= 0)

m.c30 = Constraint(expr=   m.x5 + m.x11 + m.x17 + m.x23 + m.x29 + m.x35 - 5*m.b149 <= 0)

m.c31 = Constraint(expr=   m.x6 + m.x12 + m.x18 + m.x24 + m.x30 + m.x36 - 5*m.b150 <= 0)

m.c32 = Constraint(expr=   m.b145 - m.x151 <= 0)

m.c33 = Constraint(expr=   m.b146 - m.x152 <= 0)

m.c34 = Constraint(expr=   m.b147 - m.x153 <= 0)

m.c35 = Constraint(expr=   m.b148 - m.x154 <= 0)

m.c36 = Constraint(expr=   m.b149 - m.x155 <= 0)

m.c37 = Constraint(expr=   m.b150 - m.x156 <= 0)

m.c38 = Constraint(expr= - 15*m.b145 + m.x151 <= 0)

m.c39 = Constraint(expr= - 12*m.b146 + m.x152 <= 0)

m.c40 = Constraint(expr= - 8*m.b147 + m.x153 <= 0)

m.c41 = Constraint(expr= - 7*m.b148 + m.x154 <= 0)

m.c42 = Constraint(expr= - 4*m.b149 + m.x155 <= 0)

m.c43 = Constraint(expr= - 2*m.b150 + m.x156 <= 0)

m.c44 = Constraint(expr=   m.x151 + m.x152 + m.x153 + m.x154 + m.x155 + m.x156 >= 16)

m.c45 = Constraint(expr= - m.b145 + m.b146 <= 0)

m.c46 = Constraint(expr= - m.b146 + m.b147 <= 0)

m.c47 = Constraint(expr= - m.b147 + m.b148 <= 0)

m.c48 = Constraint(expr= - m.b148 + m.b149 <= 0)

m.c49 = Constraint(expr= - m.b149 + m.b150 <= 0)

m.c50 = Constraint(expr= - m.x151 + m.x152 <= 0)

m.c51 = Constraint(expr= - m.x152 + m.x153 <= 0)

m.c52 = Constraint(expr= - m.x153 + m.x154 <= 0)

m.c53 = Constraint(expr= - m.x154 + m.x155 <= 0)

m.c54 = Constraint(expr= - m.x155 + m.x156 <= 0)

m.c55 = Constraint(expr=   m.x1 - m.b37 - 2*m.b38 - 4*m.b39 == 0)

m.c56 = Constraint(expr=   m.x2 - m.b40 - 2*m.b41 - 4*m.b42 == 0)

m.c57 = Constraint(expr=   m.x3 - m.b43 - 2*m.b44 - 4*m.b45 == 0)

m.c58 = Constraint(expr=   m.x4 - m.b46 - 2*m.b47 - 4*m.b48 == 0)

m.c59 = Constraint(expr=   m.x5 - m.b49 - 2*m.b50 - 4*m.b51 == 0)

m.c60 = Constraint(expr=   m.x6 - m.b52 - 2*m.b53 - 4*m.b54 == 0)

m.c61 = Constraint(expr=   m.x7 - m.b55 - 2*m.b56 - 4*m.b57 == 0)

m.c62 = Constraint(expr=   m.x8 - m.b58 - 2*m.b59 - 4*m.b60 == 0)

m.c63 = Constraint(expr=   m.x9 - m.b61 - 2*m.b62 - 4*m.b63 == 0)

m.c64 = Constraint(expr=   m.x10 - m.b64 - 2*m.b65 - 4*m.b66 == 0)

m.c65 = Constraint(expr=   m.x11 - m.b67 - 2*m.b68 - 4*m.b69 == 0)

m.c66 = Constraint(expr=   m.x12 - m.b70 - 2*m.b71 - 4*m.b72 == 0)

m.c67 = Constraint(expr=   m.x13 - m.b73 - 2*m.b74 - 4*m.b75 == 0)

m.c68 = Constraint(expr=   m.x14 - m.b76 - 2*m.b77 - 4*m.b78 == 0)

m.c69 = Constraint(expr=   m.x15 - m.b79 - 2*m.b80 - 4*m.b81 == 0)

m.c70 = Constraint(expr=   m.x16 - m.b82 - 2*m.b83 - 4*m.b84 == 0)

m.c71 = Constraint(expr=   m.x17 - m.b85 - 2*m.b86 - 4*m.b87 == 0)

m.c72 = Constraint(expr=   m.x18 - m.b88 - 2*m.b89 - 4*m.b90 == 0)

m.c73 = Constraint(expr=   m.x19 - m.b91 - 2*m.b92 - 4*m.b93 == 0)

m.c74 = Constraint(expr=   m.x20 - m.b94 - 2*m.b95 - 4*m.b96 == 0)

m.c75 = Constraint(expr=   m.x21 - m.b97 - 2*m.b98 - 4*m.b99 == 0)

m.c76 = Constraint(expr=   m.x22 - m.b100 - 2*m.b101 - 4*m.b102 == 0)

m.c77 = Constraint(expr=   m.x23 - m.b103 - 2*m.b104 - 4*m.b105 == 0)

m.c78 = Constraint(expr=   m.x24 - m.b106 - 2*m.b107 - 4*m.b108 == 0)

m.c79 = Constraint(expr=   m.x25 - m.b109 - 2*m.b110 - 4*m.b111 == 0)

m.c80 = Constraint(expr=   m.x26 - m.b112 - 2*m.b113 - 4*m.b114 == 0)

m.c81 = Constraint(expr=   m.x27 - m.b115 - 2*m.b116 - 4*m.b117 == 0)

m.c82 = Constraint(expr=   m.x28 - m.b118 - 2*m.b119 - 4*m.b120 == 0)

m.c83 = Constraint(expr=   m.x29 - m.b121 - 2*m.b122 - 4*m.b123 == 0)

m.c84 = Constraint(expr=   m.x30 - m.b124 - 2*m.b125 - 4*m.b126 == 0)

m.c85 = Constraint(expr=   m.x31 - m.b127 - 2*m.b128 - 4*m.b129 == 0)

m.c86 = Constraint(expr=   m.x32 - m.b130 - 2*m.b131 - 4*m.b132 == 0)

m.c87 = Constraint(expr=   m.x33 - m.b133 - 2*m.b134 - 4*m.b135 == 0)

m.c88 = Constraint(expr=   m.x34 - m.b136 - 2*m.b137 - 4*m.b138 == 0)

m.c89 = Constraint(expr=   m.x35 - m.b139 - 2*m.b140 - 4*m.b141 == 0)

m.c90 = Constraint(expr=   m.x36 - m.b142 - 2*m.b143 - 4*m.b144 == 0)

m.c91 = Constraint(expr=   m.x151 - m.b157 - 2*m.b158 - 4*m.b159 - 8*m.b160 == 0)

m.c92 = Constraint(expr=   m.x152 - m.b161 - 2*m.b162 - 4*m.b163 - 8*m.b164 == 0)

m.c93 = Constraint(expr=   m.x153 - m.b165 - 2*m.b166 - 4*m.b167 - 8*m.b168 == 0)

m.c94 = Constraint(expr=   m.x154 - m.b169 - 2*m.b170 - 4*m.b171 - 8*m.b172 == 0)

m.c95 = Constraint(expr=   m.x155 - m.b173 - 2*m.b174 - 4*m.b175 - 8*m.b176 == 0)

m.c96 = Constraint(expr=   m.x156 - m.b177 - 2*m.b178 - 4*m.b179 - 8*m.b180 == 0)
