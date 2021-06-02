#  NLP written by GAMS Convert at 04/21/18 13:52:23
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        112       41       41       30        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         78       78        0        0        0        0        0        0
#  FX      5        5        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        369      325       44        0


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(12.735,12.735),initialize=12.735)
m.x2 = Var(within=Reals,bounds=(0,140),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,140),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,140),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,140),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,140),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,140),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,140),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,140),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,140),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,140),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,140),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,140),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,140),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,140),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,140),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,140),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,140),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,140),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,140),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,140),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,140),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,140),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,140),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,140),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,140),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,140),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,140),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,140),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,140),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,140),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,140),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,140),initialize=0)
m.x34 = Var(within=Reals,bounds=(0.1,0.1),initialize=0.1)
m.x35 = Var(within=Reals,bounds=(0.1,10000),initialize=0.1)
m.x36 = Var(within=Reals,bounds=(0.1,10000),initialize=0.1)
m.x37 = Var(within=Reals,bounds=(0.1,10000),initialize=0.1)
m.x38 = Var(within=Reals,bounds=(0.1,10000),initialize=0.1)
m.x39 = Var(within=Reals,bounds=(0.1,10000),initialize=0.1)
m.x40 = Var(within=Reals,bounds=(0.1,10000),initialize=0.1)
m.x41 = Var(within=Reals,bounds=(0.1,10000),initialize=0.1)
m.x42 = Var(within=Reals,bounds=(0.1,10000),initialize=0.1)
m.x43 = Var(within=Reals,bounds=(0.1,10000),initialize=0.1)
m.x44 = Var(within=Reals,bounds=(0.1,10000),initialize=0.1)
m.x45 = Var(within=Reals,bounds=(0.2,0.2),initialize=0.2)
m.x46 = Var(within=Reals,bounds=(0.2,10000),initialize=0.2)
m.x47 = Var(within=Reals,bounds=(0.2,10000),initialize=0.2)
m.x48 = Var(within=Reals,bounds=(0.2,10000),initialize=0.2)
m.x49 = Var(within=Reals,bounds=(0.2,10000),initialize=0.2)
m.x50 = Var(within=Reals,bounds=(0.2,10000),initialize=0.2)
m.x51 = Var(within=Reals,bounds=(0.2,10000),initialize=0.2)
m.x52 = Var(within=Reals,bounds=(0.2,10000),initialize=0.2)
m.x53 = Var(within=Reals,bounds=(0.2,10000),initialize=0.2)
m.x54 = Var(within=Reals,bounds=(0.2,10000),initialize=0.2)
m.x55 = Var(within=Reals,bounds=(0.2,10000),initialize=0.2)
m.x56 = Var(within=Reals,bounds=(0.01,0.01),initialize=0.01)
m.x57 = Var(within=Reals,bounds=(0.01,10000),initialize=0.01)
m.x58 = Var(within=Reals,bounds=(0.01,10000),initialize=0.01)
m.x59 = Var(within=Reals,bounds=(0.01,10000),initialize=0.01)
m.x60 = Var(within=Reals,bounds=(0.01,10000),initialize=0.01)
m.x61 = Var(within=Reals,bounds=(0.01,10000),initialize=0.01)
m.x62 = Var(within=Reals,bounds=(0.01,10000),initialize=0.01)
m.x63 = Var(within=Reals,bounds=(0.01,10000),initialize=0.01)
m.x64 = Var(within=Reals,bounds=(0.01,10000),initialize=0.01)
m.x65 = Var(within=Reals,bounds=(0.01,10000),initialize=0.01)
m.x66 = Var(within=Reals,bounds=(0.01,10000),initialize=0.01)
m.x67 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x68 = Var(within=Reals,bounds=(0,400),initialize=0)
m.x69 = Var(within=Reals,bounds=(0,400),initialize=0)
m.x70 = Var(within=Reals,bounds=(0,400),initialize=0)
m.x71 = Var(within=Reals,bounds=(0,400),initialize=0)
m.x72 = Var(within=Reals,bounds=(0,400),initialize=0)
m.x73 = Var(within=Reals,bounds=(0,400),initialize=0)
m.x74 = Var(within=Reals,bounds=(0,400),initialize=0)
m.x75 = Var(within=Reals,bounds=(0,400),initialize=0)
m.x76 = Var(within=Reals,bounds=(0,400),initialize=0)
m.x77 = Var(within=Reals,bounds=(0,400),initialize=0)
m.x78 = Var(within=Reals,bounds=(0,30000),initialize=0)

m.obj = Objective(expr=m.x78, sense=minimize)

m.c1 = Constraint(expr=   m.x1 + m.x12 + m.x23 >= 12.735)

m.c2 = Constraint(expr=   m.x2 + m.x13 + m.x24 >= 18.523)

m.c3 = Constraint(expr=   m.x3 + m.x14 + m.x25 >= 24.42)

m.c4 = Constraint(expr=   m.x4 + m.x15 + m.x26 >= 30.729)

m.c5 = Constraint(expr=   m.x5 + m.x16 + m.x27 >= 41.698)

m.c6 = Constraint(expr=   m.x6 + m.x17 + m.x28 >= 52.802)

m.c7 = Constraint(expr=   m.x7 + m.x18 + m.x29 >= 65.155)

m.c8 = Constraint(expr=   m.x8 + m.x19 + m.x30 >= 81.675)

m.c9 = Constraint(expr=   m.x9 + m.x20 + m.x31 >= 98.667)

m.c10 = Constraint(expr=   m.x10 + m.x21 + m.x32 >= 115.501)

m.c11 = Constraint(expr=   m.x11 + m.x22 + m.x33 >= 133.561)

m.c12 = Constraint(expr= - 0.744093914896725*m.x1 + m.x2 >= 0)

m.c13 = Constraint(expr= - 0.744093914896725*m.x2 + m.x3 >= 0)

m.c14 = Constraint(expr= - 0.744093914896725*m.x3 + m.x4 >= 0)

m.c15 = Constraint(expr= - 0.744093914896725*m.x4 + m.x5 >= 0)

m.c16 = Constraint(expr= - 0.744093914896725*m.x5 + m.x6 >= 0)

m.c17 = Constraint(expr= - 0.744093914896725*m.x6 + m.x7 >= 0)

m.c18 = Constraint(expr= - 0.744093914896725*m.x7 + m.x8 >= 0)

m.c19 = Constraint(expr= - 0.744093914896725*m.x8 + m.x9 >= 0)

m.c20 = Constraint(expr= - 0.744093914896725*m.x9 + m.x10 >= 0)

m.c21 = Constraint(expr= - 0.744093914896725*m.x10 + m.x11 >= 0)

m.c22 = Constraint(expr= - 0.744093914896725*m.x12 + m.x13 >= 0)

m.c23 = Constraint(expr= - 0.744093914896725*m.x13 + m.x14 >= 0)

m.c24 = Constraint(expr= - 0.744093914896725*m.x14 + m.x15 >= 0)

m.c25 = Constraint(expr= - 0.744093914896725*m.x15 + m.x16 >= 0)

m.c26 = Constraint(expr= - 0.744093914896725*m.x16 + m.x17 >= 0)

m.c27 = Constraint(expr= - 0.744093914896725*m.x17 + m.x18 >= 0)

m.c28 = Constraint(expr= - 0.744093914896725*m.x18 + m.x19 >= 0)

m.c29 = Constraint(expr= - 0.744093914896725*m.x19 + m.x20 >= 0)

m.c30 = Constraint(expr= - 0.744093914896725*m.x20 + m.x21 >= 0)

m.c31 = Constraint(expr= - 0.744093914896725*m.x21 + m.x22 >= 0)

m.c32 = Constraint(expr= - 0.744093914896725*m.x23 + m.x24 >= 0)

m.c33 = Constraint(expr= - 0.744093914896725*m.x24 + m.x25 >= 0)

m.c34 = Constraint(expr= - 0.744093914896725*m.x25 + m.x26 >= 0)

m.c35 = Constraint(expr= - 0.744093914896725*m.x26 + m.x27 >= 0)

m.c36 = Constraint(expr= - 0.744093914896725*m.x27 + m.x28 >= 0)

m.c37 = Constraint(expr= - 0.744093914896725*m.x28 + m.x29 >= 0)

m.c38 = Constraint(expr= - 0.744093914896725*m.x29 + m.x30 >= 0)

m.c39 = Constraint(expr= - 0.744093914896725*m.x30 + m.x31 >= 0)

m.c40 = Constraint(expr= - 0.744093914896725*m.x31 + m.x32 >= 0)

m.c41 = Constraint(expr= - 0.744093914896725*m.x32 + m.x33 >= 0)

m.c42 = Constraint(expr= - 4*m.x1 + m.x2 <= 0.18523)

m.c43 = Constraint(expr= - 4*m.x2 + m.x3 <= 0.2442)

m.c44 = Constraint(expr= - 4*m.x3 + m.x4 <= 0.30729)

m.c45 = Constraint(expr= - 4*m.x4 + m.x5 <= 0.41698)

m.c46 = Constraint(expr= - 4*m.x5 + m.x6 <= 0.52802)

m.c47 = Constraint(expr= - 4*m.x6 + m.x7 <= 0.65155)

m.c48 = Constraint(expr= - 4*m.x7 + m.x8 <= 0.81675)

m.c49 = Constraint(expr= - 4*m.x8 + m.x9 <= 0.98667)

m.c50 = Constraint(expr= - 4*m.x9 + m.x10 <= 1.15501)

m.c51 = Constraint(expr= - 4*m.x10 + m.x11 <= 1.33561)

m.c52 = Constraint(expr= - 4*m.x12 + m.x13 <= 0.18523)

m.c53 = Constraint(expr= - 4*m.x13 + m.x14 <= 0.2442)

m.c54 = Constraint(expr= - 4*m.x14 + m.x15 <= 0.30729)

m.c55 = Constraint(expr= - 4*m.x15 + m.x16 <= 0.41698)

m.c56 = Constraint(expr= - 4*m.x16 + m.x17 <= 0.52802)

m.c57 = Constraint(expr= - 4*m.x17 + m.x18 <= 0.65155)

m.c58 = Constraint(expr= - 4*m.x18 + m.x19 <= 0.81675)

m.c59 = Constraint(expr= - 4*m.x19 + m.x20 <= 0.98667)

m.c60 = Constraint(expr= - 4*m.x20 + m.x21 <= 1.15501)

m.c61 = Constraint(expr= - 4*m.x21 + m.x22 <= 1.33561)

m.c62 = Constraint(expr= - 4*m.x23 + m.x24 <= 0.18523)

m.c63 = Constraint(expr= - 4*m.x24 + m.x25 <= 0.2442)

m.c64 = Constraint(expr= - 4*m.x25 + m.x26 <= 0.30729)

m.c65 = Constraint(expr= - 4*m.x26 + m.x27 <= 0.41698)

m.c66 = Constraint(expr= - 4*m.x27 + m.x28 <= 0.52802)

m.c67 = Constraint(expr= - 4*m.x28 + m.x29 <= 0.65155)

m.c68 = Constraint(expr= - 4*m.x29 + m.x30 <= 0.81675)

m.c69 = Constraint(expr= - 4*m.x30 + m.x31 <= 0.98667)

m.c70 = Constraint(expr= - 4*m.x31 + m.x32 <= 1.15501)

m.c71 = Constraint(expr= - 4*m.x32 + m.x33 <= 1.33561)

m.c72 = Constraint(expr= - 5*m.x1 - 5*m.x2 - m.x34 + m.x35 == 0)

m.c73 = Constraint(expr= - 5*m.x2 - 5*m.x3 - m.x35 + m.x36 == 0)

m.c74 = Constraint(expr= - 5*m.x3 - 5*m.x4 - m.x36 + m.x37 == 0)

m.c75 = Constraint(expr= - 5*m.x4 - 5*m.x5 - m.x37 + m.x38 == 0)

m.c76 = Constraint(expr= - 5*m.x5 - 5*m.x6 - m.x38 + m.x39 == 0)

m.c77 = Constraint(expr= - 5*m.x6 - 5*m.x7 - m.x39 + m.x40 == 0)

m.c78 = Constraint(expr= - 5*m.x7 - 5*m.x8 - m.x40 + m.x41 == 0)

m.c79 = Constraint(expr= - 5*m.x8 - 5*m.x9 - m.x41 + m.x42 == 0)

m.c80 = Constraint(expr= - 5*m.x9 - 5*m.x10 - m.x42 + m.x43 == 0)

m.c81 = Constraint(expr= - 5*m.x10 - 5*m.x11 - m.x43 + m.x44 == 0)

m.c82 = Constraint(expr= - 5*m.x12 - 5*m.x13 - m.x45 + m.x46 == 0)

m.c83 = Constraint(expr= - 5*m.x13 - 5*m.x14 - m.x46 + m.x47 == 0)

m.c84 = Constraint(expr= - 5*m.x14 - 5*m.x15 - m.x47 + m.x48 == 0)

m.c85 = Constraint(expr= - 5*m.x15 - 5*m.x16 - m.x48 + m.x49 == 0)

m.c86 = Constraint(expr= - 5*m.x16 - 5*m.x17 - m.x49 + m.x50 == 0)

m.c87 = Constraint(expr= - 5*m.x17 - 5*m.x18 - m.x50 + m.x51 == 0)

m.c88 = Constraint(expr= - 5*m.x18 - 5*m.x19 - m.x51 + m.x52 == 0)

m.c89 = Constraint(expr= - 5*m.x19 - 5*m.x20 - m.x52 + m.x53 == 0)

m.c90 = Constraint(expr= - 5*m.x20 - 5*m.x21 - m.x53 + m.x54 == 0)

m.c91 = Constraint(expr= - 5*m.x21 - 5*m.x22 - m.x54 + m.x55 == 0)

m.c92 = Constraint(expr= - 5*m.x23 - 5*m.x24 - m.x56 + m.x57 == 0)

m.c93 = Constraint(expr= - 5*m.x24 - 5*m.x25 - m.x57 + m.x58 == 0)

m.c94 = Constraint(expr= - 5*m.x25 - 5*m.x26 - m.x58 + m.x59 == 0)

m.c95 = Constraint(expr= - 5*m.x26 - 5*m.x27 - m.x59 + m.x60 == 0)

m.c96 = Constraint(expr= - 5*m.x27 - 5*m.x28 - m.x60 + m.x61 == 0)

m.c97 = Constraint(expr= - 5*m.x28 - 5*m.x29 - m.x61 + m.x62 == 0)

m.c98 = Constraint(expr= - 5*m.x29 - 5*m.x30 - m.x62 + m.x63 == 0)

m.c99 = Constraint(expr= - 5*m.x30 - 5*m.x31 - m.x63 + m.x64 == 0)

m.c100 = Constraint(expr= - 5*m.x31 - 5*m.x32 - m.x64 + m.x65 == 0)

m.c101 = Constraint(expr= - 5*m.x32 - 5*m.x33 - m.x65 + m.x66 == 0)

m.c102 = Constraint(expr= - 0.850412249705536*m.x1 - 0.850412249705536*m.x2 - m.x67 + m.x68 == 0)

m.c103 = Constraint(expr= - 0.850412249705536*m.x2 - 0.850412249705536*m.x3 - m.x68 + m.x69 == 0)

m.c104 = Constraint(expr= - 0.850412249705536*m.x3 - 0.850412249705536*m.x4 - m.x69 + m.x70 == 0)

m.c105 = Constraint(expr= - 0.850412249705536*m.x4 - 0.850412249705536*m.x5 - m.x70 + m.x71 == 0)

m.c106 = Constraint(expr= - 0.850412249705536*m.x5 - 0.850412249705536*m.x6 - m.x71 + m.x72 == 0)

m.c107 = Constraint(expr= - 0.850412249705536*m.x6 - 0.850412249705536*m.x7 - m.x72 + m.x73 == 0)

m.c108 = Constraint(expr= - 0.850412249705536*m.x7 - 0.850412249705536*m.x8 - m.x73 + m.x74 == 0)

m.c109 = Constraint(expr= - 0.850412249705536*m.x8 - 0.850412249705536*m.x9 - m.x74 + m.x75 == 0)

m.c110 = Constraint(expr= - 0.850412249705536*m.x9 - 0.850412249705536*m.x10 - m.x75 + m.x76 == 0)

m.c111 = Constraint(expr= - 0.850412249705536*m.x10 - 0.850412249705536*m.x11 - m.x76 + m.x77 == 0)

m.c112 = Constraint(expr=-(15*(5*m.x45)**(-0.1)*m.x12 + 130*(100*m.x56)**(-0.3)*m.x23 + 30*m.x12 + 30*m.x23 + 
                         0.613913253540759*(15*(5*m.x46)**(-0.1)*m.x13 + 130*(100*m.x57)**(-0.3)*m.x24 + 30*m.x13 + 30*
                         m.x24) + 0.376889482873*(15*(5*m.x47)**(-0.1)*m.x14 + 130*(100*m.x58)**(-0.3)*m.x25 + 30*m.x14
                          + 30*m.x25) + 0.231377448655858*(15*(5*m.x48)**(-0.1)*m.x15 + 130*(100*m.x59)**(-0.3)*m.x26 + 
                         30*m.x15 + 30*m.x26) + 0.142045682300278*(15*(5*m.x49)**(-0.1)*m.x16 + 130*(100*m.x60)**(-0.3)*
                         m.x27 + 30*m.x16 + 30*m.x27) + 0.0872037269723804*(15*(5*m.x50)**(-0.1)*m.x17 + 130*(100*m.x61)
                         **(-0.3)*m.x28 + 30*m.x17 + 30*m.x28) + 0.0535355237464941*(15*(5*m.x51)**(-0.1)*m.x18 + 130*(
                         100*m.x62)**(-0.3)*m.x29 + 30*m.x18 + 30*m.x29) + 0.0328661675632188*(15*(5*m.x52)**(-0.1)*
                         m.x19 + 130*(100*m.x63)**(-0.3)*m.x30 + 30*m.x19 + 30*m.x30) + 0.0201769758601514*(15*(5*m.x53)
                         **(-0.1)*m.x20 + 130*(100*m.x64)**(-0.3)*m.x31 + 30*m.x20 + 30*m.x31) + 0.0123869128969189*(15*
                         (5*m.x54)**(-0.1)*m.x21 + 130*(100*m.x65)**(-0.3)*m.x32 + 30*m.x21 + 30*m.x32) + 
                         0.00760448999787347*(15*(5*m.x55)**(-0.1)*m.x22 + 130*(100*m.x66)**(-0.3)*m.x33 + 30*m.x22 + 30
                         *m.x33)) - 40*m.x1 - 24.5565301416304*m.x2 - 15.07557931492*m.x3 - 9.25509794623431*m.x4
                          - 5.6818272920111*m.x5 - 3.48814907889522*m.x6 - 2.14142094985976*m.x7 - 1.31464670252875*m.x8
                          - 0.807079034406055*m.x9 - 0.495476515876756*m.x10 - 0.304179599914939*m.x11 + m.x78 == 0)
