#  MINLP written by GAMS Convert at 04/21/18 13:55:05
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         47       46        0        1        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        105       40       65        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        392      132      260        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(0.1,0.9),initialize=0.1)
m.x3 = Var(within=Reals,bounds=(0.1,0.9),initialize=0.1)
m.x4 = Var(within=Reals,bounds=(0.1,0.9),initialize=0.1)
m.x5 = Var(within=Reals,bounds=(0.1,0.9),initialize=0.1)
m.x6 = Var(within=Reals,bounds=(0.1,0.9),initialize=0.1)
m.x7 = Var(within=Reals,bounds=(0,10),initialize=0)
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

m.obj = Objective(expr=   m.x25, sense=minimize)

m.c2 = Constraint(expr=   m.x7 <= 0.0675)

m.c3 = Constraint(expr=   m.x9 - m.x10 + m.x11 == 0)

m.c4 = Constraint(expr=   m.x12 - m.x13 + m.x14 == 0)

m.c5 = Constraint(expr=   m.x15 - m.x16 + m.x17 == 0)

m.c6 = Constraint(expr=   m.x18 - m.x19 + m.x20 == 0)

m.c7 = Constraint(expr=   m.x21 - m.x22 + m.x23 == 0)

m.c8 = Constraint(expr=   m.x26 - m.x27 + m.x28 == 0)

m.c9 = Constraint(expr=   m.x29 - m.x30 + m.x31 == 0)

m.c10 = Constraint(expr=   m.x32 - m.x33 + m.x34 == 0)

m.c11 = Constraint(expr=   m.x35 - m.x36 + m.x37 == 0)

m.c12 = Constraint(expr=   m.x38 - m.x39 + m.x40 == 0)

m.c13 = Constraint(expr=m.x2**0.29*m.x10 - m.x11 == 0)

m.c14 = Constraint(expr=m.x3**0.13*m.x13 - m.x14 == 0)

m.c15 = Constraint(expr=m.x4**0.06*m.x16 - m.x17 == 0)

m.c16 = Constraint(expr=m.x5**0.15*m.x19 - m.x20 == 0)

m.c17 = Constraint(expr=m.x6**0.2*m.x22 - m.x23 == 0)

m.c18 = Constraint(expr=m.x2**0.74*m.x27 - m.x28 == 0)

m.c19 = Constraint(expr=m.x3**0.79*m.x30 - m.x31 == 0)

m.c20 = Constraint(expr=m.x4**0.71*m.x33 - m.x34 == 0)

m.c21 = Constraint(expr=m.x5**0.8*m.x36 - m.x37 == 0)

m.c22 = Constraint(expr=m.x6**0.7*m.x39 - m.x40 == 0)

m.c23 = Constraint(expr=m.b41*m.x9 + m.b46*m.x11 + m.b51*m.x12 + m.b56*m.x14 + m.b61*m.x15 + m.b66*m.x17 + m.b71*m.x18
                         + m.b76*m.x20 + m.b81*m.x21 + m.b86*m.x23 - m.x10 + 0.675*m.b91 == 0)

m.c24 = Constraint(expr=m.b42*m.x9 + m.b47*m.x11 + m.b52*m.x12 + m.b57*m.x14 + m.b62*m.x15 + m.b67*m.x17 + m.b72*m.x18
                         + m.b77*m.x20 + m.b82*m.x21 + m.b87*m.x23 - m.x13 + 0.675*m.b92 == 0)

m.c25 = Constraint(expr=m.b43*m.x9 + m.b48*m.x11 + m.b53*m.x12 + m.b58*m.x14 + m.b63*m.x15 + m.b68*m.x17 + m.b73*m.x18
                         + m.b78*m.x20 + m.b83*m.x21 + m.b88*m.x23 - m.x16 + 0.675*m.b93 == 0)

m.c26 = Constraint(expr=m.b44*m.x9 + m.b49*m.x11 + m.b54*m.x12 + m.b59*m.x14 + m.b64*m.x15 + m.b69*m.x17 + m.b74*m.x18
                         + m.b79*m.x20 + m.b84*m.x21 + m.b89*m.x23 - m.x19 + 0.675*m.b94 == 0)

m.c27 = Constraint(expr=m.b45*m.x9 + m.b50*m.x11 + m.b55*m.x12 + m.b60*m.x14 + m.b65*m.x15 + m.b70*m.x17 + m.b75*m.x18
                         + m.b80*m.x20 + m.b85*m.x21 + m.b90*m.x23 - m.x22 + 0.675*m.b95 == 0)

m.c28 = Constraint(expr=m.b41*m.x26 + m.b46*m.x28 + m.b51*m.x29 + m.b56*m.x31 + m.b61*m.x32 + m.b66*m.x34 + m.b71*m.x35
                         + m.b76*m.x37 + m.b81*m.x38 + m.b86*m.x40 - m.x27 + 0.649*m.b91 == 0)

m.c29 = Constraint(expr=m.b42*m.x26 + m.b47*m.x28 + m.b52*m.x29 + m.b57*m.x31 + m.b62*m.x32 + m.b67*m.x34 + m.b72*m.x35
                         + m.b77*m.x37 + m.b82*m.x38 + m.b87*m.x40 - m.x30 + 0.649*m.b92 == 0)

m.c30 = Constraint(expr=m.b43*m.x26 + m.b48*m.x28 + m.b53*m.x29 + m.b58*m.x31 + m.b63*m.x32 + m.b68*m.x34 + m.b73*m.x35
                         + m.b78*m.x37 + m.b83*m.x38 + m.b88*m.x40 - m.x33 + 0.649*m.b93 == 0)

m.c31 = Constraint(expr=m.b44*m.x26 + m.b49*m.x28 + m.b54*m.x29 + m.b59*m.x31 + m.b64*m.x32 + m.b69*m.x34 + m.b74*m.x35
                         + m.b79*m.x37 + m.b84*m.x38 + m.b89*m.x40 - m.x36 + 0.649*m.b94 == 0)

m.c32 = Constraint(expr=m.b45*m.x26 + m.b50*m.x28 + m.b55*m.x29 + m.b60*m.x31 + m.b65*m.x32 + m.b70*m.x34 + m.b75*m.x35
                         + m.b80*m.x37 + m.b85*m.x38 + m.b90*m.x40 - m.x39 + 0.649*m.b95 == 0)

m.c33 = Constraint(expr=m.b96*m.x9 + m.b97*m.x12 + m.b98*m.x15 + m.b99*m.x18 + m.b100*m.x21 - m.x7 == 0)

m.c34 = Constraint(expr=m.b96*m.x26 + m.b97*m.x29 + m.b98*m.x32 + m.b99*m.x35 + m.b100*m.x38 - m.x24 == 0)

m.c35 = Constraint(expr=m.b101*m.x11 + m.b102*m.x14 + m.b103*m.x17 + m.b104*m.x20 + m.b105*m.x23 - m.x8 == 0)

m.c36 = Constraint(expr=m.b101*m.x28 + m.b102*m.x31 + m.b103*m.x34 + m.b104*m.x37 + m.b105*m.x40 - m.x25 == 0)

m.c37 = Constraint(expr=   m.b41 + m.b42 + m.b43 + m.b44 + m.b45 + m.b96 == 1)

m.c38 = Constraint(expr=   m.b51 + m.b52 + m.b53 + m.b54 + m.b55 + m.b97 == 1)

m.c39 = Constraint(expr=   m.b61 + m.b62 + m.b63 + m.b64 + m.b65 + m.b98 == 1)

m.c40 = Constraint(expr=   m.b71 + m.b72 + m.b73 + m.b74 + m.b75 + m.b99 == 1)

m.c41 = Constraint(expr=   m.b81 + m.b82 + m.b83 + m.b84 + m.b85 + m.b100 == 1)

m.c42 = Constraint(expr=   m.b46 + m.b47 + m.b48 + m.b49 + m.b50 + m.b101 == 1)

m.c43 = Constraint(expr=   m.b56 + m.b57 + m.b58 + m.b59 + m.b60 + m.b102 == 1)

m.c44 = Constraint(expr=   m.b66 + m.b67 + m.b68 + m.b69 + m.b70 + m.b103 == 1)

m.c45 = Constraint(expr=   m.b76 + m.b77 + m.b78 + m.b79 + m.b80 + m.b104 == 1)

m.c46 = Constraint(expr=   m.b86 + m.b87 + m.b88 + m.b89 + m.b90 + m.b105 == 1)

m.c47 = Constraint(expr=   m.b91 + m.b92 + m.b93 + m.b94 + m.b95 == 1)
