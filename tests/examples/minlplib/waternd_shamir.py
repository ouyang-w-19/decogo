#  MINLP written by GAMS Convert at 04/21/18 13:55:15
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         47       31        8        8        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        136       24      112        0        0        0        0        0
#  FX      1        1        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        424      392       32        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(210,210),initialize=210)
m.x2 = Var(within=Reals,bounds=(180,210),initialize=180)
m.x3 = Var(within=Reals,bounds=(190,210),initialize=190)
m.x4 = Var(within=Reals,bounds=(185,210),initialize=185)
m.x5 = Var(within=Reals,bounds=(180,210),initialize=180)
m.x6 = Var(within=Reals,bounds=(195,210),initialize=195)
m.x7 = Var(within=Reals,bounds=(190,210),initialize=190)
m.x8 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x9 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x10 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x11 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x12 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x13 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x14 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x15 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x16 = Var(within=Reals,bounds=(0.000506707479097498,0.291863507960159),initialize=0.000506707479097498)
m.x17 = Var(within=Reals,bounds=(0.000506707479097498,0.291863507960159),initialize=0.000506707479097498)
m.x18 = Var(within=Reals,bounds=(0.000506707479097498,0.291863507960159),initialize=0.000506707479097498)
m.x19 = Var(within=Reals,bounds=(0.000506707479097498,0.291863507960159),initialize=0.000506707479097498)
m.x20 = Var(within=Reals,bounds=(0.000506707479097498,0.291863507960159),initialize=0.000506707479097498)
m.x21 = Var(within=Reals,bounds=(0.000506707479097498,0.291863507960159),initialize=0.000506707479097498)
m.x22 = Var(within=Reals,bounds=(0.000506707479097498,0.291863507960159),initialize=0.000506707479097498)
m.x23 = Var(within=Reals,bounds=(0.000506707479097498,0.291863507960159),initialize=0.000506707479097498)
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

m.obj = Objective(expr=   2000*m.b24 + 5000*m.b25 + 8000*m.b26 + 11000*m.b27 + 16000*m.b28 + 23000*m.b29 + 32000*m.b30
                        + 50000*m.b31 + 60000*m.b32 + 90000*m.b33 + 130000*m.b34 + 170000*m.b35 + 300000*m.b36
                        + 550000*m.b37 + 2000*m.b38 + 5000*m.b39 + 8000*m.b40 + 11000*m.b41 + 16000*m.b42 + 23000*m.b43
                        + 32000*m.b44 + 50000*m.b45 + 60000*m.b46 + 90000*m.b47 + 130000*m.b48 + 170000*m.b49
                        + 300000*m.b50 + 550000*m.b51 + 2000*m.b52 + 5000*m.b53 + 8000*m.b54 + 11000*m.b55 + 16000*m.b56
                        + 23000*m.b57 + 32000*m.b58 + 50000*m.b59 + 60000*m.b60 + 90000*m.b61 + 130000*m.b62
                        + 170000*m.b63 + 300000*m.b64 + 550000*m.b65 + 2000*m.b66 + 5000*m.b67 + 8000*m.b68
                        + 11000*m.b69 + 16000*m.b70 + 23000*m.b71 + 32000*m.b72 + 50000*m.b73 + 60000*m.b74
                        + 90000*m.b75 + 130000*m.b76 + 170000*m.b77 + 300000*m.b78 + 550000*m.b79 + 2000*m.b80
                        + 5000*m.b81 + 8000*m.b82 + 11000*m.b83 + 16000*m.b84 + 23000*m.b85 + 32000*m.b86 + 50000*m.b87
                        + 60000*m.b88 + 90000*m.b89 + 130000*m.b90 + 170000*m.b91 + 300000*m.b92 + 550000*m.b93
                        + 2000*m.b94 + 5000*m.b95 + 8000*m.b96 + 11000*m.b97 + 16000*m.b98 + 23000*m.b99 + 32000*m.b100
                        + 50000*m.b101 + 60000*m.b102 + 90000*m.b103 + 130000*m.b104 + 170000*m.b105 + 300000*m.b106
                        + 550000*m.b107 + 2000*m.b108 + 5000*m.b109 + 8000*m.b110 + 11000*m.b111 + 16000*m.b112
                        + 23000*m.b113 + 32000*m.b114 + 50000*m.b115 + 60000*m.b116 + 90000*m.b117 + 130000*m.b118
                        + 170000*m.b119 + 300000*m.b120 + 550000*m.b121 + 2000*m.b122 + 5000*m.b123 + 8000*m.b124
                        + 11000*m.b125 + 16000*m.b126 + 23000*m.b127 + 32000*m.b128 + 50000*m.b129 + 60000*m.b130
                        + 90000*m.b131 + 130000*m.b132 + 170000*m.b133 + 300000*m.b134 + 550000*m.b135, sense=minimize)

m.c2 = Constraint(expr= - m.x8 + m.x9 + m.x10 == -0.02777)

m.c3 = Constraint(expr= - m.x9 + m.x11 == -0.02777)

m.c4 = Constraint(expr= - m.x10 + m.x12 + m.x13 == -0.03333)

m.c5 = Constraint(expr= - m.x11 - m.x12 + m.x14 == -0.075)

m.c6 = Constraint(expr= - m.x13 + m.x15 == -0.09167)

m.c7 = Constraint(expr= - m.x14 - m.x15 == -0.05555)

m.c8 = Constraint(expr=SignPower(m.x8,1.852) - 0.76849192909955*(1.27323954473516*m.x16)**2.435*(m.x1 - m.x2) == 0)

m.c9 = Constraint(expr=SignPower(m.x9,1.852) - 0.76849192909955*(1.27323954473516*m.x17)**2.435*(m.x2 - m.x3) == 0)

m.c10 = Constraint(expr=SignPower(m.x10,1.852) - 0.76849192909955*(1.27323954473516*m.x18)**2.435*(m.x2 - m.x4) == 0)

m.c11 = Constraint(expr=SignPower(m.x11,1.852) - 0.76849192909955*(1.27323954473516*m.x19)**2.435*(m.x3 - m.x5) == 0)

m.c12 = Constraint(expr=SignPower(m.x12,1.852) - 0.76849192909955*(1.27323954473516*m.x20)**2.435*(m.x4 - m.x5) == 0)

m.c13 = Constraint(expr=SignPower(m.x13,1.852) - 0.76849192909955*(1.27323954473516*m.x21)**2.435*(m.x4 - m.x6) == 0)

m.c14 = Constraint(expr=SignPower(m.x14,1.852) - 0.76849192909955*(1.27323954473516*m.x22)**2.435*(m.x5 - m.x7) == 0)

m.c15 = Constraint(expr=SignPower(m.x15,1.852) - 0.76849192909955*(1.27323954473516*m.x23)**2.435*(m.x6 - m.x7) == 0)

m.c16 = Constraint(expr=   m.x8 - 2*m.x16 <= 0)

m.c17 = Constraint(expr=   m.x9 - 2*m.x17 <= 0)

m.c18 = Constraint(expr=   m.x10 - 2*m.x18 <= 0)

m.c19 = Constraint(expr=   m.x11 - 2*m.x19 <= 0)

m.c20 = Constraint(expr=   m.x12 - 2*m.x20 <= 0)

m.c21 = Constraint(expr=   m.x13 - 2*m.x21 <= 0)

m.c22 = Constraint(expr=   m.x14 - 2*m.x22 <= 0)

m.c23 = Constraint(expr=   m.x15 - 2*m.x23 <= 0)

m.c24 = Constraint(expr=   m.x8 + 2*m.x16 >= 0)

m.c25 = Constraint(expr=   m.x9 + 2*m.x17 >= 0)

m.c26 = Constraint(expr=   m.x10 + 2*m.x18 >= 0)

m.c27 = Constraint(expr=   m.x11 + 2*m.x19 >= 0)

m.c28 = Constraint(expr=   m.x12 + 2*m.x20 >= 0)

m.c29 = Constraint(expr=   m.x13 + 2*m.x21 >= 0)

m.c30 = Constraint(expr=   m.x14 + 2*m.x22 >= 0)

m.c31 = Constraint(expr=   m.x15 + 2*m.x23 >= 0)

m.c32 = Constraint(expr=   m.x16 - 0.000506707479097498*m.b24 - 0.00202682991638999*m.b25 - 0.00456036731187748*m.b26
                         - 0.00810731966555996*m.b27 - 0.0182414692475099*m.b28 - 0.0324292786622399*m.b29
                         - 0.0506707479097498*m.b30 - 0.0729658769900397*m.b31 - 0.0993146659031096*m.b32
                         - 0.129717114648959*m.b33 - 0.164173223227589*m.b34 - 0.202682991638999*m.b35
                         - 0.245246419883189*m.b36 - 0.291863507960159*m.b37 == 0)

m.c33 = Constraint(expr=   m.x17 - 0.000506707479097498*m.b38 - 0.00202682991638999*m.b39 - 0.00456036731187748*m.b40
                         - 0.00810731966555996*m.b41 - 0.0182414692475099*m.b42 - 0.0324292786622399*m.b43
                         - 0.0506707479097498*m.b44 - 0.0729658769900397*m.b45 - 0.0993146659031096*m.b46
                         - 0.129717114648959*m.b47 - 0.164173223227589*m.b48 - 0.202682991638999*m.b49
                         - 0.245246419883189*m.b50 - 0.291863507960159*m.b51 == 0)

m.c34 = Constraint(expr=   m.x18 - 0.000506707479097498*m.b52 - 0.00202682991638999*m.b53 - 0.00456036731187748*m.b54
                         - 0.00810731966555996*m.b55 - 0.0182414692475099*m.b56 - 0.0324292786622399*m.b57
                         - 0.0506707479097498*m.b58 - 0.0729658769900397*m.b59 - 0.0993146659031096*m.b60
                         - 0.129717114648959*m.b61 - 0.164173223227589*m.b62 - 0.202682991638999*m.b63
                         - 0.245246419883189*m.b64 - 0.291863507960159*m.b65 == 0)

m.c35 = Constraint(expr=   m.x19 - 0.000506707479097498*m.b66 - 0.00202682991638999*m.b67 - 0.00456036731187748*m.b68
                         - 0.00810731966555996*m.b69 - 0.0182414692475099*m.b70 - 0.0324292786622399*m.b71
                         - 0.0506707479097498*m.b72 - 0.0729658769900397*m.b73 - 0.0993146659031096*m.b74
                         - 0.129717114648959*m.b75 - 0.164173223227589*m.b76 - 0.202682991638999*m.b77
                         - 0.245246419883189*m.b78 - 0.291863507960159*m.b79 == 0)

m.c36 = Constraint(expr=   m.x20 - 0.000506707479097498*m.b80 - 0.00202682991638999*m.b81 - 0.00456036731187748*m.b82
                         - 0.00810731966555996*m.b83 - 0.0182414692475099*m.b84 - 0.0324292786622399*m.b85
                         - 0.0506707479097498*m.b86 - 0.0729658769900397*m.b87 - 0.0993146659031096*m.b88
                         - 0.129717114648959*m.b89 - 0.164173223227589*m.b90 - 0.202682991638999*m.b91
                         - 0.245246419883189*m.b92 - 0.291863507960159*m.b93 == 0)

m.c37 = Constraint(expr=   m.x21 - 0.000506707479097498*m.b94 - 0.00202682991638999*m.b95 - 0.00456036731187748*m.b96
                         - 0.00810731966555996*m.b97 - 0.0182414692475099*m.b98 - 0.0324292786622399*m.b99
                         - 0.0506707479097498*m.b100 - 0.0729658769900397*m.b101 - 0.0993146659031096*m.b102
                         - 0.129717114648959*m.b103 - 0.164173223227589*m.b104 - 0.202682991638999*m.b105
                         - 0.245246419883189*m.b106 - 0.291863507960159*m.b107 == 0)

m.c38 = Constraint(expr=   m.x22 - 0.000506707479097498*m.b108 - 0.00202682991638999*m.b109 - 0.00456036731187748*m.b110
                         - 0.00810731966555996*m.b111 - 0.0182414692475099*m.b112 - 0.0324292786622399*m.b113
                         - 0.0506707479097498*m.b114 - 0.0729658769900397*m.b115 - 0.0993146659031096*m.b116
                         - 0.129717114648959*m.b117 - 0.164173223227589*m.b118 - 0.202682991638999*m.b119
                         - 0.245246419883189*m.b120 - 0.291863507960159*m.b121 == 0)

m.c39 = Constraint(expr=   m.x23 - 0.000506707479097498*m.b122 - 0.00202682991638999*m.b123 - 0.00456036731187748*m.b124
                         - 0.00810731966555996*m.b125 - 0.0182414692475099*m.b126 - 0.0324292786622399*m.b127
                         - 0.0506707479097498*m.b128 - 0.0729658769900397*m.b129 - 0.0993146659031096*m.b130
                         - 0.129717114648959*m.b131 - 0.164173223227589*m.b132 - 0.202682991638999*m.b133
                         - 0.245246419883189*m.b134 - 0.291863507960159*m.b135 == 0)

m.c40 = Constraint(expr=   m.b24 + m.b25 + m.b26 + m.b27 + m.b28 + m.b29 + m.b30 + m.b31 + m.b32 + m.b33 + m.b34 + m.b35
                         + m.b36 + m.b37 == 1)

m.c41 = Constraint(expr=   m.b38 + m.b39 + m.b40 + m.b41 + m.b42 + m.b43 + m.b44 + m.b45 + m.b46 + m.b47 + m.b48 + m.b49
                         + m.b50 + m.b51 == 1)

m.c42 = Constraint(expr=   m.b52 + m.b53 + m.b54 + m.b55 + m.b56 + m.b57 + m.b58 + m.b59 + m.b60 + m.b61 + m.b62 + m.b63
                         + m.b64 + m.b65 == 1)

m.c43 = Constraint(expr=   m.b66 + m.b67 + m.b68 + m.b69 + m.b70 + m.b71 + m.b72 + m.b73 + m.b74 + m.b75 + m.b76 + m.b77
                         + m.b78 + m.b79 == 1)

m.c44 = Constraint(expr=   m.b80 + m.b81 + m.b82 + m.b83 + m.b84 + m.b85 + m.b86 + m.b87 + m.b88 + m.b89 + m.b90 + m.b91
                         + m.b92 + m.b93 == 1)

m.c45 = Constraint(expr=   m.b94 + m.b95 + m.b96 + m.b97 + m.b98 + m.b99 + m.b100 + m.b101 + m.b102 + m.b103 + m.b104
                         + m.b105 + m.b106 + m.b107 == 1)

m.c46 = Constraint(expr=   m.b108 + m.b109 + m.b110 + m.b111 + m.b112 + m.b113 + m.b114 + m.b115 + m.b116 + m.b117
                         + m.b118 + m.b119 + m.b120 + m.b121 == 1)

m.c47 = Constraint(expr=   m.b122 + m.b123 + m.b124 + m.b125 + m.b126 + m.b127 + m.b128 + m.b129 + m.b130 + m.b131
                         + m.b132 + m.b133 + m.b134 + m.b135 == 1)
