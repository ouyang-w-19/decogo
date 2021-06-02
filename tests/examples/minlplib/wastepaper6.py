#  MINLP written by GAMS Convert at 04/21/18 13:55:05
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         55       54        0        1        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        137       47       90        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        529      169      360        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(0.1,0.9),initialize=0.1)
m.x3 = Var(within=Reals,bounds=(0.1,0.9),initialize=0.1)
m.x4 = Var(within=Reals,bounds=(0.1,0.9),initialize=0.1)
m.x5 = Var(within=Reals,bounds=(0.1,0.9),initialize=0.1)
m.x6 = Var(within=Reals,bounds=(0.1,0.9),initialize=0.1)
m.x7 = Var(within=Reals,bounds=(0.1,0.9),initialize=0.1)
m.x8 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x34 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x35 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x36 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x37 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x38 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x39 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x40 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x41 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x42 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x43 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x44 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x45 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x46 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x47 = Var(within=Reals,bounds=(0,10),initialize=0)
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

m.obj = Objective(expr=   m.x29, sense=minimize)

m.c2 = Constraint(expr=   m.x8 <= 0.0675)

m.c3 = Constraint(expr=   m.x10 - m.x11 + m.x12 == 0)

m.c4 = Constraint(expr=   m.x13 - m.x14 + m.x15 == 0)

m.c5 = Constraint(expr=   m.x16 - m.x17 + m.x18 == 0)

m.c6 = Constraint(expr=   m.x19 - m.x20 + m.x21 == 0)

m.c7 = Constraint(expr=   m.x22 - m.x23 + m.x24 == 0)

m.c8 = Constraint(expr=   m.x25 - m.x26 + m.x27 == 0)

m.c9 = Constraint(expr=   m.x30 - m.x31 + m.x32 == 0)

m.c10 = Constraint(expr=   m.x33 - m.x34 + m.x35 == 0)

m.c11 = Constraint(expr=   m.x36 - m.x37 + m.x38 == 0)

m.c12 = Constraint(expr=   m.x39 - m.x40 + m.x41 == 0)

m.c13 = Constraint(expr=   m.x42 - m.x43 + m.x44 == 0)

m.c14 = Constraint(expr=   m.x45 - m.x46 + m.x47 == 0)

m.c15 = Constraint(expr=m.x2**0.29*m.x11 - m.x12 == 0)

m.c16 = Constraint(expr=m.x3**0.13*m.x14 - m.x15 == 0)

m.c17 = Constraint(expr=m.x4**0.06*m.x17 - m.x18 == 0)

m.c18 = Constraint(expr=m.x5**0.15*m.x20 - m.x21 == 0)

m.c19 = Constraint(expr=m.x6**0.2*m.x23 - m.x24 == 0)

m.c20 = Constraint(expr=m.x7**0.17*m.x26 - m.x27 == 0)

m.c21 = Constraint(expr=m.x2**0.74*m.x31 - m.x32 == 0)

m.c22 = Constraint(expr=m.x3**0.79*m.x34 - m.x35 == 0)

m.c23 = Constraint(expr=m.x4**0.71*m.x37 - m.x38 == 0)

m.c24 = Constraint(expr=m.x5**0.8*m.x40 - m.x41 == 0)

m.c25 = Constraint(expr=m.x6**0.7*m.x43 - m.x44 == 0)

m.c26 = Constraint(expr=m.x7**0.85*m.x46 - m.x47 == 0)

m.c27 = Constraint(expr=m.b48*m.x10 + m.b54*m.x12 + m.b60*m.x13 + m.b66*m.x15 + m.b72*m.x16 + m.b78*m.x18 + m.b84*m.x19
                         + m.b90*m.x21 + m.b96*m.x22 + m.b102*m.x24 + m.b108*m.x25 + m.b114*m.x27 - m.x11 + 0.675*m.b120
                         == 0)

m.c28 = Constraint(expr=m.b49*m.x10 + m.b55*m.x12 + m.b61*m.x13 + m.b67*m.x15 + m.b73*m.x16 + m.b79*m.x18 + m.b85*m.x19
                         + m.b91*m.x21 + m.b97*m.x22 + m.b103*m.x24 + m.b109*m.x25 + m.b115*m.x27 - m.x14 + 0.675*m.b121
                         == 0)

m.c29 = Constraint(expr=m.b50*m.x10 + m.b56*m.x12 + m.b62*m.x13 + m.b68*m.x15 + m.b74*m.x16 + m.b80*m.x18 + m.b86*m.x19
                         + m.b92*m.x21 + m.b98*m.x22 + m.b104*m.x24 + m.b110*m.x25 + m.b116*m.x27 - m.x17 + 0.675*m.b122
                         == 0)

m.c30 = Constraint(expr=m.b51*m.x10 + m.b57*m.x12 + m.b63*m.x13 + m.b69*m.x15 + m.b75*m.x16 + m.b81*m.x18 + m.b87*m.x19
                         + m.b93*m.x21 + m.b99*m.x22 + m.b105*m.x24 + m.b111*m.x25 + m.b117*m.x27 - m.x20 + 0.675*m.b123
                         == 0)

m.c31 = Constraint(expr=m.b52*m.x10 + m.b58*m.x12 + m.b64*m.x13 + m.b70*m.x15 + m.b76*m.x16 + m.b82*m.x18 + m.b88*m.x19
                         + m.b94*m.x21 + m.b100*m.x22 + m.b106*m.x24 + m.b112*m.x25 + m.b118*m.x27 - m.x23
                         + 0.675*m.b124 == 0)

m.c32 = Constraint(expr=m.b53*m.x10 + m.b59*m.x12 + m.b65*m.x13 + m.b71*m.x15 + m.b77*m.x16 + m.b83*m.x18 + m.b89*m.x19
                         + m.b95*m.x21 + m.b101*m.x22 + m.b107*m.x24 + m.b113*m.x25 + m.b119*m.x27 - m.x26
                         + 0.675*m.b125 == 0)

m.c33 = Constraint(expr=m.b48*m.x30 + m.b54*m.x32 + m.b60*m.x33 + m.b66*m.x35 + m.b72*m.x36 + m.b78*m.x38 + m.b84*m.x39
                         + m.b90*m.x41 + m.b96*m.x42 + m.b102*m.x44 + m.b108*m.x45 + m.b114*m.x47 - m.x31 + 0.649*m.b120
                         == 0)

m.c34 = Constraint(expr=m.b49*m.x30 + m.b55*m.x32 + m.b61*m.x33 + m.b67*m.x35 + m.b73*m.x36 + m.b79*m.x38 + m.b85*m.x39
                         + m.b91*m.x41 + m.b97*m.x42 + m.b103*m.x44 + m.b109*m.x45 + m.b115*m.x47 - m.x34 + 0.649*m.b121
                         == 0)

m.c35 = Constraint(expr=m.b50*m.x30 + m.b56*m.x32 + m.b62*m.x33 + m.b68*m.x35 + m.b74*m.x36 + m.b80*m.x38 + m.b86*m.x39
                         + m.b92*m.x41 + m.b98*m.x42 + m.b104*m.x44 + m.b110*m.x45 + m.b116*m.x47 - m.x37 + 0.649*m.b122
                         == 0)

m.c36 = Constraint(expr=m.b51*m.x30 + m.b57*m.x32 + m.b63*m.x33 + m.b69*m.x35 + m.b75*m.x36 + m.b81*m.x38 + m.b87*m.x39
                         + m.b93*m.x41 + m.b99*m.x42 + m.b105*m.x44 + m.b111*m.x45 + m.b117*m.x47 - m.x40 + 0.649*m.b123
                         == 0)

m.c37 = Constraint(expr=m.b52*m.x30 + m.b58*m.x32 + m.b64*m.x33 + m.b70*m.x35 + m.b76*m.x36 + m.b82*m.x38 + m.b88*m.x39
                         + m.b94*m.x41 + m.b100*m.x42 + m.b106*m.x44 + m.b112*m.x45 + m.b118*m.x47 - m.x43
                         + 0.649*m.b124 == 0)

m.c38 = Constraint(expr=m.b53*m.x30 + m.b59*m.x32 + m.b65*m.x33 + m.b71*m.x35 + m.b77*m.x36 + m.b83*m.x38 + m.b89*m.x39
                         + m.b95*m.x41 + m.b101*m.x42 + m.b107*m.x44 + m.b113*m.x45 + m.b119*m.x47 - m.x46
                         + 0.649*m.b125 == 0)

m.c39 = Constraint(expr=m.b126*m.x10 + m.b127*m.x13 + m.b128*m.x16 + m.b129*m.x19 + m.b130*m.x22 + m.b131*m.x25 - m.x8
                         == 0)

m.c40 = Constraint(expr=m.b126*m.x30 + m.b127*m.x33 + m.b128*m.x36 + m.b129*m.x39 + m.b130*m.x42 + m.b131*m.x45 - m.x28
                         == 0)

m.c41 = Constraint(expr=m.b132*m.x12 + m.b133*m.x15 + m.b134*m.x18 + m.b135*m.x21 + m.b136*m.x24 + m.b137*m.x27 - m.x9
                         == 0)

m.c42 = Constraint(expr=m.b132*m.x32 + m.b133*m.x35 + m.b134*m.x38 + m.b135*m.x41 + m.b136*m.x44 + m.b137*m.x47 - m.x29
                         == 0)

m.c43 = Constraint(expr=   m.b48 + m.b49 + m.b50 + m.b51 + m.b52 + m.b53 + m.b126 == 1)

m.c44 = Constraint(expr=   m.b60 + m.b61 + m.b62 + m.b63 + m.b64 + m.b65 + m.b127 == 1)

m.c45 = Constraint(expr=   m.b72 + m.b73 + m.b74 + m.b75 + m.b76 + m.b77 + m.b128 == 1)

m.c46 = Constraint(expr=   m.b84 + m.b85 + m.b86 + m.b87 + m.b88 + m.b89 + m.b129 == 1)

m.c47 = Constraint(expr=   m.b96 + m.b97 + m.b98 + m.b99 + m.b100 + m.b101 + m.b130 == 1)

m.c48 = Constraint(expr=   m.b108 + m.b109 + m.b110 + m.b111 + m.b112 + m.b113 + m.b131 == 1)

m.c49 = Constraint(expr=   m.b54 + m.b55 + m.b56 + m.b57 + m.b58 + m.b59 + m.b132 == 1)

m.c50 = Constraint(expr=   m.b66 + m.b67 + m.b68 + m.b69 + m.b70 + m.b71 + m.b133 == 1)

m.c51 = Constraint(expr=   m.b78 + m.b79 + m.b80 + m.b81 + m.b82 + m.b83 + m.b134 == 1)

m.c52 = Constraint(expr=   m.b90 + m.b91 + m.b92 + m.b93 + m.b94 + m.b95 + m.b135 == 1)

m.c53 = Constraint(expr=   m.b102 + m.b103 + m.b104 + m.b105 + m.b106 + m.b107 + m.b136 == 1)

m.c54 = Constraint(expr=   m.b114 + m.b115 + m.b116 + m.b117 + m.b118 + m.b119 + m.b137 == 1)

m.c55 = Constraint(expr=   m.b120 + m.b121 + m.b122 + m.b123 + m.b124 + m.b125 == 1)
