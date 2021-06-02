#  MINLP written by GAMS Convert at 04/21/18 13:51:43
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         75       31        6       38        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        131       31      100        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        347      297       50        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,5),initialize=0)
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
m.x106 = Var(within=Reals,bounds=(0,15),initialize=0)
m.x107 = Var(within=Reals,bounds=(0,12),initialize=0)
m.x108 = Var(within=Reals,bounds=(0,9),initialize=0)
m.x109 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x110 = Var(within=Reals,bounds=(0,6),initialize=0)
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

m.obj = Objective(expr=   0.1*m.b101 + 0.2*m.b102 + 0.3*m.b103 + 0.4*m.b104 + 0.5*m.b105 + m.x106 + m.x107 + m.x108
                        + m.x109 + m.x110, sense=minimize)

m.c2 = Constraint(expr=m.x106*m.x1 + m.x107*m.x2 + m.x108*m.x3 + m.x109*m.x4 + m.x110*m.x5 >= 12)

m.c3 = Constraint(expr=m.x106*m.x6 + m.x107*m.x7 + m.x108*m.x8 + m.x109*m.x9 + m.x110*m.x10 >= 6)

m.c4 = Constraint(expr=m.x106*m.x11 + m.x107*m.x12 + m.x108*m.x13 + m.x109*m.x14 + m.x110*m.x15 >= 15)

m.c5 = Constraint(expr=m.x106*m.x16 + m.x107*m.x17 + m.x108*m.x18 + m.x109*m.x19 + m.x110*m.x20 >= 6)

m.c6 = Constraint(expr=m.x106*m.x21 + m.x107*m.x22 + m.x108*m.x23 + m.x109*m.x24 + m.x110*m.x25 >= 9)

m.c7 = Constraint(expr= - 330*m.x1 - 360*m.x6 - 370*m.x11 - 415*m.x16 - 435*m.x21 + 1800*m.b101 <= 0)

m.c8 = Constraint(expr= - 330*m.x2 - 360*m.x7 - 370*m.x12 - 415*m.x17 - 435*m.x22 + 1800*m.b102 <= 0)

m.c9 = Constraint(expr= - 330*m.x3 - 360*m.x8 - 370*m.x13 - 415*m.x18 - 435*m.x23 + 1800*m.b103 <= 0)

m.c10 = Constraint(expr= - 330*m.x4 - 360*m.x9 - 370*m.x14 - 415*m.x19 - 435*m.x24 + 1800*m.b104 <= 0)

m.c11 = Constraint(expr= - 330*m.x5 - 360*m.x10 - 370*m.x15 - 415*m.x20 - 435*m.x25 + 1800*m.b105 <= 0)

m.c12 = Constraint(expr=   330*m.x1 + 360*m.x6 + 370*m.x11 + 415*m.x16 + 435*m.x21 - 2000*m.b101 <= 0)

m.c13 = Constraint(expr=   330*m.x2 + 360*m.x7 + 370*m.x12 + 415*m.x17 + 435*m.x22 - 2000*m.b102 <= 0)

m.c14 = Constraint(expr=   330*m.x3 + 360*m.x8 + 370*m.x13 + 415*m.x18 + 435*m.x23 - 2000*m.b103 <= 0)

m.c15 = Constraint(expr=   330*m.x4 + 360*m.x9 + 370*m.x14 + 415*m.x19 + 435*m.x24 - 2000*m.b104 <= 0)

m.c16 = Constraint(expr=   330*m.x5 + 360*m.x10 + 370*m.x15 + 415*m.x20 + 435*m.x25 - 2000*m.b105 <= 0)

m.c17 = Constraint(expr= - m.x1 - m.x6 - m.x11 - m.x16 - m.x21 + m.b101 <= 0)

m.c18 = Constraint(expr= - m.x2 - m.x7 - m.x12 - m.x17 - m.x22 + m.b102 <= 0)

m.c19 = Constraint(expr= - m.x3 - m.x8 - m.x13 - m.x18 - m.x23 + m.b103 <= 0)

m.c20 = Constraint(expr= - m.x4 - m.x9 - m.x14 - m.x19 - m.x24 + m.b104 <= 0)

m.c21 = Constraint(expr= - m.x5 - m.x10 - m.x15 - m.x20 - m.x25 + m.b105 <= 0)

m.c22 = Constraint(expr=   m.x1 + m.x6 + m.x11 + m.x16 + m.x21 - 5*m.b101 <= 0)

m.c23 = Constraint(expr=   m.x2 + m.x7 + m.x12 + m.x17 + m.x22 - 5*m.b102 <= 0)

m.c24 = Constraint(expr=   m.x3 + m.x8 + m.x13 + m.x18 + m.x23 - 5*m.b103 <= 0)

m.c25 = Constraint(expr=   m.x4 + m.x9 + m.x14 + m.x19 + m.x24 - 5*m.b104 <= 0)

m.c26 = Constraint(expr=   m.x5 + m.x10 + m.x15 + m.x20 + m.x25 - 5*m.b105 <= 0)

m.c27 = Constraint(expr=   m.b101 - m.x106 <= 0)

m.c28 = Constraint(expr=   m.b102 - m.x107 <= 0)

m.c29 = Constraint(expr=   m.b103 - m.x108 <= 0)

m.c30 = Constraint(expr=   m.b104 - m.x109 <= 0)

m.c31 = Constraint(expr=   m.b105 - m.x110 <= 0)

m.c32 = Constraint(expr= - 15*m.b101 + m.x106 <= 0)

m.c33 = Constraint(expr= - 12*m.b102 + m.x107 <= 0)

m.c34 = Constraint(expr= - 9*m.b103 + m.x108 <= 0)

m.c35 = Constraint(expr= - 6*m.b104 + m.x109 <= 0)

m.c36 = Constraint(expr= - 6*m.b105 + m.x110 <= 0)

m.c37 = Constraint(expr=   m.x106 + m.x107 + m.x108 + m.x109 + m.x110 >= 10)

m.c38 = Constraint(expr= - m.b101 + m.b102 <= 0)

m.c39 = Constraint(expr= - m.b102 + m.b103 <= 0)

m.c40 = Constraint(expr= - m.b103 + m.b104 <= 0)

m.c41 = Constraint(expr= - m.b104 + m.b105 <= 0)

m.c42 = Constraint(expr= - m.x106 + m.x107 <= 0)

m.c43 = Constraint(expr= - m.x107 + m.x108 <= 0)

m.c44 = Constraint(expr= - m.x108 + m.x109 <= 0)

m.c45 = Constraint(expr= - m.x109 + m.x110 <= 0)

m.c46 = Constraint(expr=   m.x1 - m.b26 - 2*m.b27 - 4*m.b28 == 0)

m.c47 = Constraint(expr=   m.x2 - m.b29 - 2*m.b30 - 4*m.b31 == 0)

m.c48 = Constraint(expr=   m.x3 - m.b32 - 2*m.b33 - 4*m.b34 == 0)

m.c49 = Constraint(expr=   m.x4 - m.b35 - 2*m.b36 - 4*m.b37 == 0)

m.c50 = Constraint(expr=   m.x5 - m.b38 - 2*m.b39 - 4*m.b40 == 0)

m.c51 = Constraint(expr=   m.x6 - m.b41 - 2*m.b42 - 4*m.b43 == 0)

m.c52 = Constraint(expr=   m.x7 - m.b44 - 2*m.b45 - 4*m.b46 == 0)

m.c53 = Constraint(expr=   m.x8 - m.b47 - 2*m.b48 - 4*m.b49 == 0)

m.c54 = Constraint(expr=   m.x9 - m.b50 - 2*m.b51 - 4*m.b52 == 0)

m.c55 = Constraint(expr=   m.x10 - m.b53 - 2*m.b54 - 4*m.b55 == 0)

m.c56 = Constraint(expr=   m.x11 - m.b56 - 2*m.b57 - 4*m.b58 == 0)

m.c57 = Constraint(expr=   m.x12 - m.b59 - 2*m.b60 - 4*m.b61 == 0)

m.c58 = Constraint(expr=   m.x13 - m.b62 - 2*m.b63 - 4*m.b64 == 0)

m.c59 = Constraint(expr=   m.x14 - m.b65 - 2*m.b66 - 4*m.b67 == 0)

m.c60 = Constraint(expr=   m.x15 - m.b68 - 2*m.b69 - 4*m.b70 == 0)

m.c61 = Constraint(expr=   m.x16 - m.b71 - 2*m.b72 - 4*m.b73 == 0)

m.c62 = Constraint(expr=   m.x17 - m.b74 - 2*m.b75 - 4*m.b76 == 0)

m.c63 = Constraint(expr=   m.x18 - m.b77 - 2*m.b78 - 4*m.b79 == 0)

m.c64 = Constraint(expr=   m.x19 - m.b80 - 2*m.b81 - 4*m.b82 == 0)

m.c65 = Constraint(expr=   m.x20 - m.b83 - 2*m.b84 - 4*m.b85 == 0)

m.c66 = Constraint(expr=   m.x21 - m.b86 - 2*m.b87 - 4*m.b88 == 0)

m.c67 = Constraint(expr=   m.x22 - m.b89 - 2*m.b90 - 4*m.b91 == 0)

m.c68 = Constraint(expr=   m.x23 - m.b92 - 2*m.b93 - 4*m.b94 == 0)

m.c69 = Constraint(expr=   m.x24 - m.b95 - 2*m.b96 - 4*m.b97 == 0)

m.c70 = Constraint(expr=   m.x25 - m.b98 - 2*m.b99 - 4*m.b100 == 0)

m.c71 = Constraint(expr=   m.x106 - m.b111 - 2*m.b112 - 4*m.b113 - 8*m.b114 == 0)

m.c72 = Constraint(expr=   m.x107 - m.b115 - 2*m.b116 - 4*m.b117 - 8*m.b118 == 0)

m.c73 = Constraint(expr=   m.x108 - m.b119 - 2*m.b120 - 4*m.b121 - 8*m.b122 == 0)

m.c74 = Constraint(expr=   m.x109 - m.b123 - 2*m.b124 - 4*m.b125 - 8*m.b126 == 0)

m.c75 = Constraint(expr=   m.x110 - m.b127 - 2*m.b128 - 4*m.b129 - 8*m.b130 == 0)
