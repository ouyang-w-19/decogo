#  MINLP written by GAMS Convert at 04/21/18 13:51:12
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        214       31       78      105        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        103       67       36        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        543      479       64        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x34 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x35 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x36 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x37 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x38 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x39 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x40 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x41 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x42 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x43 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x44 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x45 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x46 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x47 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x48 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x49 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x50 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x51 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x52 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x53 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x54 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x55 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x56 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x57 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x58 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x59 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x60 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x61 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x62 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x63 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x64 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x65 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x66 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x67 = Var(within=Reals,bounds=(0,2),initialize=0)
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

m.obj = Objective(expr= - 1.74*m.x2 - 1.74*m.x3 - 1.74*m.x4 - 1.45*m.x5 - 1.45*m.x6 - 1.45*m.x7 + 7.38*m.x8 + 7.38*m.x9
                        + 7.38*m.x10 + 5.6*m.x11 + 5.6*m.x12 + 5.6*m.x13 - 1.7*m.x14 - 1.7*m.x15 - 1.7*m.x16
                        - 1.18*m.x17 - 1.18*m.x18 - 1.18*m.x19 + 7.21*m.x20 + 7.21*m.x21 + 7.21*m.x22 + 5.45*m.x23
                        + 5.45*m.x24 + 5.45*m.x25 - 0.3*m.x26 - 0.3*m.x27 - 0.3*m.x28 + 7.71*m.x29 + 7.71*m.x30
                        + 7.71*m.x31 + 6.28*m.x32 + 6.28*m.x33 + 6.28*m.x34 + 7.74*m.x35 + 7.74*m.x36 + 7.74*m.x37
                        - 0.84*m.b68 - 0.84*m.b69 - 0.84*m.b70 - 0.05*m.b71 - 0.05*m.b72 - 0.05*m.b73 - 0.94*m.b74
                        - 0.94*m.b75 - 0.94*m.b76 - 0.81*m.b77 - 0.81*m.b78 - 0.81*m.b79 - 0.79*m.b80 - 0.79*m.b81
                        - 0.79*m.b82 - 0.05*m.b83 - 0.05*m.b84 - 0.05*m.b85 - 0.65*m.b86 - 0.65*m.b87 - 0.65*m.b88
                        - 0.97*m.b89 - 0.97*m.b90 - 0.97*m.b91 - 0.57*m.b92 - 0.57*m.b93 - 0.57*m.b94 - 0.26*m.b95
                        - 0.26*m.b96 - 0.26*m.b97 - 0.45*m.b98 - 0.45*m.b99 - 0.45*m.b100 - 0.1*m.b101 - 0.1*m.b102
                        - 0.1*m.b103, sense=maximize)

m.c2 = Constraint(expr=   m.x2 + m.x5 + m.x8 + m.x11 + m.x50 == 1)

m.c3 = Constraint(expr=   m.x14 + m.x17 + m.x20 + m.x23 + m.x53 == 1.1)

m.c4 = Constraint(expr= - m.x2 - m.x14 + m.x26 + m.x29 + m.x32 + m.x56 == 0.2)

m.c5 = Constraint(expr= - m.x5 - m.x17 - m.x26 + m.x35 + m.x59 == 0.1)

m.c6 = Constraint(expr= - m.x8 - m.x20 - m.x29 - m.x35 + m.x62 == 1.55)

m.c7 = Constraint(expr= - m.x11 - m.x23 - m.x32 + m.x65 == 0.49)

m.c8 = Constraint(expr=m.x38*m.x56 - 0.6*m.x2 - 0.2*m.x14 + 0.2*m.x26 + 0.2*m.x29 + 0.2*m.x32 == 0.04)

m.c9 = Constraint(expr=m.x41*m.x59 - 0.6*m.x5 - 0.2*m.x17 - 0.2*m.x26 + 0.7*m.x35 == 0.07)

m.c10 = Constraint(expr=m.x44*m.x56 - 0.4*m.x2 - 0.4*m.x14 + 0.5*m.x26 + 0.5*m.x29 + 0.5*m.x32 == 0.1)

m.c11 = Constraint(expr=m.x47*m.x59 - 0.4*m.x5 - 0.4*m.x17 - 0.5*m.x26 + 0.6*m.x35 == 0.06)

m.c12 = Constraint(expr=   m.x3 + m.x6 + m.x9 + m.x12 - m.x50 + m.x51 == 1)

m.c13 = Constraint(expr=   m.x4 + m.x7 + m.x10 + m.x13 - m.x51 + m.x52 == 0)

m.c14 = Constraint(expr=   m.x15 + m.x18 + m.x21 + m.x24 - m.x53 + m.x54 == 0.1)

m.c15 = Constraint(expr=   m.x16 + m.x19 + m.x22 + m.x25 - m.x54 + m.x55 == 0.9)

m.c16 = Constraint(expr= - m.x3 - m.x15 + m.x27 + m.x30 + m.x33 - m.x56 + m.x57 == 0)

m.c17 = Constraint(expr= - m.x4 - m.x16 + m.x28 + m.x31 + m.x34 - m.x57 + m.x58 == 0)

m.c18 = Constraint(expr= - m.x6 - m.x18 - m.x27 + m.x36 - m.x59 + m.x60 == 0)

m.c19 = Constraint(expr= - m.x7 - m.x19 - m.x28 + m.x37 - m.x60 + m.x61 == 0)

m.c20 = Constraint(expr= - m.x9 - m.x21 - m.x30 - m.x36 - m.x62 + m.x63 == -0.81)

m.c21 = Constraint(expr= - m.x10 - m.x22 - m.x31 - m.x37 - m.x63 + m.x64 == -0.88)

m.c22 = Constraint(expr= - m.x12 - m.x24 - m.x33 - m.x65 + m.x66 == -0.14)

m.c23 = Constraint(expr= - m.x13 - m.x25 - m.x34 - m.x66 + m.x67 == -0.1)

m.c24 = Constraint(expr=m.x39*m.x57 - (m.x38*m.x56 - (m.x38*m.x27 + m.x38*m.x30 + m.x38*m.x33)) - 0.6*m.x3 - 0.2*m.x15
                         == 0)

m.c25 = Constraint(expr=m.x40*m.x58 - (m.x39*m.x57 - (m.x39*m.x28 + m.x39*m.x31 + m.x39*m.x34)) - 0.6*m.x4 - 0.2*m.x16
                         == 0)

m.c26 = Constraint(expr=m.x42*m.x60 - (m.x41*m.x59 + m.x38*m.x27 - m.x41*m.x36) - 0.6*m.x6 - 0.2*m.x18 == 0)

m.c27 = Constraint(expr=m.x43*m.x61 - (m.x42*m.x60 + m.x39*m.x28 - m.x42*m.x37) - 0.6*m.x7 - 0.2*m.x19 == 0)

m.c28 = Constraint(expr=m.x45*m.x57 - (m.x44*m.x56 - (m.x44*m.x27 + m.x44*m.x30 + m.x44*m.x33)) - 0.4*m.x3 - 0.4*m.x15
                         == 0)

m.c29 = Constraint(expr=m.x46*m.x58 - (m.x45*m.x57 - (m.x45*m.x28 + m.x45*m.x31 + m.x45*m.x34)) - 0.4*m.x4 - 0.4*m.x16
                         == 0)

m.c30 = Constraint(expr=m.x48*m.x60 - (m.x47*m.x59 + m.x44*m.x27 - m.x47*m.x36) - 0.4*m.x6 - 0.4*m.x18 == 0)

m.c31 = Constraint(expr=m.x49*m.x61 - (m.x48*m.x60 + m.x45*m.x28 - m.x48*m.x37) - 0.4*m.x7 - 0.4*m.x19 == 0)

m.c32 = Constraint(expr=   m.x2 - m.b68 <= 0)

m.c33 = Constraint(expr=   m.x3 - m.b69 <= 0)

m.c34 = Constraint(expr=   m.x4 - m.b70 <= 0)

m.c35 = Constraint(expr=   m.x5 - m.b71 <= 0)

m.c36 = Constraint(expr=   m.x6 - m.b72 <= 0)

m.c37 = Constraint(expr=   m.x7 - m.b73 <= 0)

m.c38 = Constraint(expr=   m.x8 - m.b74 <= 0)

m.c39 = Constraint(expr=   m.x9 - m.b75 <= 0)

m.c40 = Constraint(expr=   m.x10 - m.b76 <= 0)

m.c41 = Constraint(expr=   m.x11 - m.b77 <= 0)

m.c42 = Constraint(expr=   m.x12 - m.b78 <= 0)

m.c43 = Constraint(expr=   m.x13 - m.b79 <= 0)

m.c44 = Constraint(expr=   m.x14 - m.b80 <= 0)

m.c45 = Constraint(expr=   m.x15 - m.b81 <= 0)

m.c46 = Constraint(expr=   m.x16 - m.b82 <= 0)

m.c47 = Constraint(expr=   m.x17 - m.b83 <= 0)

m.c48 = Constraint(expr=   m.x18 - m.b84 <= 0)

m.c49 = Constraint(expr=   m.x19 - m.b85 <= 0)

m.c50 = Constraint(expr=   m.x20 - m.b86 <= 0)

m.c51 = Constraint(expr=   m.x21 - m.b87 <= 0)

m.c52 = Constraint(expr=   m.x22 - m.b88 <= 0)

m.c53 = Constraint(expr=   m.x23 - m.b89 <= 0)

m.c54 = Constraint(expr=   m.x24 - m.b90 <= 0)

m.c55 = Constraint(expr=   m.x25 - m.b91 <= 0)

m.c56 = Constraint(expr=   m.x26 - m.b92 <= 0)

m.c57 = Constraint(expr=   m.x27 - m.b93 <= 0)

m.c58 = Constraint(expr=   m.x28 - m.b94 <= 0)

m.c59 = Constraint(expr=   m.x29 - m.b95 <= 0)

m.c60 = Constraint(expr=   m.x30 - m.b96 <= 0)

m.c61 = Constraint(expr=   m.x31 - m.b97 <= 0)

m.c62 = Constraint(expr=   m.x32 - m.b98 <= 0)

m.c63 = Constraint(expr=   m.x33 - m.b99 <= 0)

m.c64 = Constraint(expr=   m.x34 - m.b100 <= 0)

m.c65 = Constraint(expr=   m.x35 - m.b101 <= 0)

m.c66 = Constraint(expr=   m.x36 - m.b102 <= 0)

m.c67 = Constraint(expr=   m.x37 - m.b103 <= 0)

m.c68 = Constraint(expr=   m.x2 >= 0)

m.c69 = Constraint(expr=   m.x3 >= 0)

m.c70 = Constraint(expr=   m.x4 >= 0)

m.c71 = Constraint(expr=   m.x5 >= 0)

m.c72 = Constraint(expr=   m.x6 >= 0)

m.c73 = Constraint(expr=   m.x7 >= 0)

m.c74 = Constraint(expr=   m.x8 >= 0)

m.c75 = Constraint(expr=   m.x9 >= 0)

m.c76 = Constraint(expr=   m.x10 >= 0)

m.c77 = Constraint(expr=   m.x11 >= 0)

m.c78 = Constraint(expr=   m.x12 >= 0)

m.c79 = Constraint(expr=   m.x13 >= 0)

m.c80 = Constraint(expr=   m.x14 >= 0)

m.c81 = Constraint(expr=   m.x15 >= 0)

m.c82 = Constraint(expr=   m.x16 >= 0)

m.c83 = Constraint(expr=   m.x17 >= 0)

m.c84 = Constraint(expr=   m.x18 >= 0)

m.c85 = Constraint(expr=   m.x19 >= 0)

m.c86 = Constraint(expr=   m.x20 >= 0)

m.c87 = Constraint(expr=   m.x21 >= 0)

m.c88 = Constraint(expr=   m.x22 >= 0)

m.c89 = Constraint(expr=   m.x23 >= 0)

m.c90 = Constraint(expr=   m.x24 >= 0)

m.c91 = Constraint(expr=   m.x25 >= 0)

m.c92 = Constraint(expr=   m.x26 >= 0)

m.c93 = Constraint(expr=   m.x27 >= 0)

m.c94 = Constraint(expr=   m.x28 >= 0)

m.c95 = Constraint(expr=   m.x29 >= 0)

m.c96 = Constraint(expr=   m.x30 >= 0)

m.c97 = Constraint(expr=   m.x31 >= 0)

m.c98 = Constraint(expr=   m.x32 >= 0)

m.c99 = Constraint(expr=   m.x33 >= 0)

m.c100 = Constraint(expr=   m.x34 >= 0)

m.c101 = Constraint(expr=   m.x35 >= 0)

m.c102 = Constraint(expr=   m.x36 >= 0)

m.c103 = Constraint(expr=   m.x37 >= 0)

m.c104 = Constraint(expr=   m.b74 <= 1.5)

m.c105 = Constraint(expr=   m.b75 <= 1.5)

m.c106 = Constraint(expr=   m.b76 <= 1.5)

m.c107 = Constraint(expr=   m.b77 <= 0.6)

m.c108 = Constraint(expr=   m.b78 <= 0.6)

m.c109 = Constraint(expr=   m.b79 <= 0.6)

m.c110 = Constraint(expr=   m.b86 <= 1.1)

m.c111 = Constraint(expr=   m.b87 <= 1.1)

m.c112 = Constraint(expr=   m.b88 <= 1.1)

m.c113 = Constraint(expr=   m.b89 <= 0.2)

m.c114 = Constraint(expr=   m.b90 <= 0.2)

m.c115 = Constraint(expr=   m.b91 <= 0.2)

m.c116 = Constraint(expr=   m.b74 <= 1)

m.c117 = Constraint(expr=   m.b75 <= 1)

m.c118 = Constraint(expr=   m.b76 <= 1)

m.c119 = Constraint(expr=   m.b77 <= 0.8)

m.c120 = Constraint(expr=   m.b78 <= 0.8)

m.c121 = Constraint(expr=   m.b79 <= 0.8)

m.c122 = Constraint(expr=   m.b86 <= 1)

m.c123 = Constraint(expr=   m.b87 <= 1)

m.c124 = Constraint(expr=   m.b88 <= 1)

m.c125 = Constraint(expr=   m.b89 <= 0.8)

m.c126 = Constraint(expr=   m.b90 <= 0.8)

m.c127 = Constraint(expr=   m.b91 <= 0.8)

m.c128 = Constraint(expr= - m.b74 >= -1.3)

m.c129 = Constraint(expr= - m.b75 >= -1.3)

m.c130 = Constraint(expr= - m.b76 >= -1.3)

m.c131 = Constraint(expr= - m.b77 >= -1.4)

m.c132 = Constraint(expr= - m.b78 >= -1.4)

m.c133 = Constraint(expr= - m.b79 >= -1.4)

m.c134 = Constraint(expr= - m.b86 >= -1.7)

m.c135 = Constraint(expr= - m.b87 >= -1.7)

m.c136 = Constraint(expr= - m.b88 >= -1.7)

m.c137 = Constraint(expr= - m.b89 >= -1.8)

m.c138 = Constraint(expr= - m.b90 >= -1.8)

m.c139 = Constraint(expr= - m.b91 >= -1.8)

m.c140 = Constraint(expr= - m.b74 >= -1)

m.c141 = Constraint(expr= - m.b75 >= -1)

m.c142 = Constraint(expr= - m.b76 >= -1)

m.c143 = Constraint(expr= - m.b77 >= -1.4)

m.c144 = Constraint(expr= - m.b78 >= -1.4)

m.c145 = Constraint(expr= - m.b79 >= -1.4)

m.c146 = Constraint(expr= - m.b86 >= -1)

m.c147 = Constraint(expr= - m.b87 >= -1)

m.c148 = Constraint(expr= - m.b88 >= -1)

m.c149 = Constraint(expr= - m.b89 >= -1.4)

m.c150 = Constraint(expr= - m.b90 >= -1.4)

m.c151 = Constraint(expr= - m.b91 >= -1.4)

m.c152 = Constraint(expr= - m.x38 + m.b96 <= 0.9)

m.c153 = Constraint(expr= - m.x39 + m.b97 <= 0.9)

m.c154 = Constraint(expr= - m.x38 + m.b99 <= 0)

m.c155 = Constraint(expr= - m.x39 + m.b100 <= 0)

m.c156 = Constraint(expr= - m.x41 + m.b102 <= 0.9)

m.c157 = Constraint(expr= - m.x42 + m.b103 <= 0.9)

m.c158 = Constraint(expr= - m.x44 + m.b96 <= 0.6)

m.c159 = Constraint(expr= - m.x45 + m.b97 <= 0.6)

m.c160 = Constraint(expr= - m.x44 + m.b99 <= 0.4)

m.c161 = Constraint(expr= - m.x45 + m.b100 <= 0.4)

m.c162 = Constraint(expr= - m.x47 + m.b102 <= 0.6)

m.c163 = Constraint(expr= - m.x48 + m.b103 <= 0.6)

m.c164 = Constraint(expr= - m.x38 - m.b96 >= -1.9)

m.c165 = Constraint(expr= - m.x39 - m.b97 >= -1.9)

m.c166 = Constraint(expr= - m.x38 - m.b99 >= -2)

m.c167 = Constraint(expr= - m.x39 - m.b100 >= -2)

m.c168 = Constraint(expr= - m.x41 - m.b102 >= -1.9)

m.c169 = Constraint(expr= - m.x42 - m.b103 >= -1.9)

m.c170 = Constraint(expr= - m.x44 - m.b96 >= -1.4)

m.c171 = Constraint(expr= - m.x45 - m.b97 >= -1.4)

m.c172 = Constraint(expr= - m.x44 - m.b99 >= -1.8)

m.c173 = Constraint(expr= - m.x45 - m.b100 >= -1.8)

m.c174 = Constraint(expr= - m.x47 - m.b102 >= -1.4)

m.c175 = Constraint(expr= - m.x48 - m.b103 >= -1.4)

m.c176 = Constraint(expr=   m.b95 <= 1.1)

m.c177 = Constraint(expr=   m.b98 <= 0.2)

m.c178 = Constraint(expr=   m.b101 <= 1.6)

m.c179 = Constraint(expr=   m.b95 <= 1.1)

m.c180 = Constraint(expr=   m.b98 <= 0.9)

m.c181 = Constraint(expr=   m.b101 <= 1.2)

m.c182 = Constraint(expr= - m.b95 >= -1.7)

m.c183 = Constraint(expr= - m.b98 >= -1.8)

m.c184 = Constraint(expr= - m.b101 >= -1.2)

m.c185 = Constraint(expr= - m.b95 >= -0.9)

m.c186 = Constraint(expr= - m.b98 >= -1.3)

m.c187 = Constraint(expr= - m.b101 >= -0.8)

m.c188 = Constraint(expr=   m.b68 + m.b92 <= 1)

m.c189 = Constraint(expr=   m.b69 + m.b93 <= 1)

m.c190 = Constraint(expr=   m.b70 + m.b94 <= 1)

m.c191 = Constraint(expr=   m.b68 + m.b95 <= 1)

m.c192 = Constraint(expr=   m.b69 + m.b96 <= 1)

m.c193 = Constraint(expr=   m.b70 + m.b97 <= 1)

m.c194 = Constraint(expr=   m.b68 + m.b98 <= 1)

m.c195 = Constraint(expr=   m.b69 + m.b99 <= 1)

m.c196 = Constraint(expr=   m.b70 + m.b100 <= 1)

m.c197 = Constraint(expr=   m.b80 + m.b92 <= 1)

m.c198 = Constraint(expr=   m.b81 + m.b93 <= 1)

m.c199 = Constraint(expr=   m.b82 + m.b94 <= 1)

m.c200 = Constraint(expr=   m.b80 + m.b95 <= 1)

m.c201 = Constraint(expr=   m.b81 + m.b96 <= 1)

m.c202 = Constraint(expr=   m.b82 + m.b97 <= 1)

m.c203 = Constraint(expr=   m.b80 + m.b98 <= 1)

m.c204 = Constraint(expr=   m.b81 + m.b99 <= 1)

m.c205 = Constraint(expr=   m.b82 + m.b100 <= 1)

m.c206 = Constraint(expr=   m.b71 + m.b101 <= 1)

m.c207 = Constraint(expr=   m.b72 + m.b102 <= 1)

m.c208 = Constraint(expr=   m.b73 + m.b103 <= 1)

m.c209 = Constraint(expr=   m.b83 + m.b101 <= 1)

m.c210 = Constraint(expr=   m.b84 + m.b102 <= 1)

m.c211 = Constraint(expr=   m.b85 + m.b103 <= 1)

m.c212 = Constraint(expr=   m.b92 + m.b101 <= 1)

m.c213 = Constraint(expr=   m.b93 + m.b102 <= 1)

m.c214 = Constraint(expr=   m.b94 + m.b103 <= 1)
