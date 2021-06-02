#  MINLP written by GAMS Convert at 04/21/18 13:55:05
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        143       85       43       15        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        157       73       30       54        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        533      293      240        0
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
m.b19 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b20 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b21 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b22 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b23 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b24 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b25 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b26 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b27 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b28 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b29 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b30 = Var(within=Binary,bounds=(0,1),initialize=1)
m.i31 = Var(within=Integers,bounds=(0,2147483647),initialize=0)
m.i32 = Var(within=Integers,bounds=(0,2147483647),initialize=0)
m.i33 = Var(within=Integers,bounds=(0,2147483647),initialize=0)
m.i34 = Var(within=Integers,bounds=(0,2147483647),initialize=0)
m.i35 = Var(within=Integers,bounds=(0,2147483647),initialize=0)
m.i36 = Var(within=Integers,bounds=(0,2147483647),initialize=0)
m.i37 = Var(within=Integers,bounds=(0,2147483647),initialize=0)
m.i38 = Var(within=Integers,bounds=(0,2147483647),initialize=0)
m.i39 = Var(within=Integers,bounds=(0,2147483647),initialize=0)
m.i40 = Var(within=Integers,bounds=(0,2147483647),initialize=0)
m.i41 = Var(within=Integers,bounds=(0,2147483647),initialize=0)
m.i42 = Var(within=Integers,bounds=(0,2147483647),initialize=0)
m.i43 = Var(within=Integers,bounds=(0,2147483647),initialize=0)
m.i44 = Var(within=Integers,bounds=(0,2147483647),initialize=0)
m.i45 = Var(within=Integers,bounds=(0,2147483647),initialize=0)
m.i46 = Var(within=Integers,bounds=(0,2147483647),initialize=0)
m.i47 = Var(within=Integers,bounds=(1,None),initialize=1)
m.i48 = Var(within=Integers,bounds=(1,None),initialize=1)
m.i49 = Var(within=Integers,bounds=(1,None),initialize=1)
m.i50 = Var(within=Integers,bounds=(1,None),initialize=1)
m.i51 = Var(within=Integers,bounds=(1,None),initialize=1)
m.i52 = Var(within=Integers,bounds=(1,None),initialize=1)
m.i53 = Var(within=Integers,bounds=(1,None),initialize=1)
m.i54 = Var(within=Integers,bounds=(1,None),initialize=1)
m.i55 = Var(within=Integers,bounds=(0,None),initialize=0)
m.i56 = Var(within=Integers,bounds=(0,None),initialize=0)
m.i57 = Var(within=Integers,bounds=(0,None),initialize=0)
m.i58 = Var(within=Integers,bounds=(0,None),initialize=0)
m.i59 = Var(within=Integers,bounds=(0,None),initialize=0)
m.i60 = Var(within=Integers,bounds=(0,None),initialize=0)
m.i61 = Var(within=Integers,bounds=(0,None),initialize=0)
m.i62 = Var(within=Integers,bounds=(0,None),initialize=0)
m.i63 = Var(within=Integers,bounds=(0,None),initialize=0)
m.i64 = Var(within=Integers,bounds=(0,None),initialize=0)
m.i65 = Var(within=Integers,bounds=(0,None),initialize=0)
m.i66 = Var(within=Integers,bounds=(0,None),initialize=0)
m.i67 = Var(within=Integers,bounds=(0,2147483647),initialize=0)
m.i68 = Var(within=Integers,bounds=(0,2147483647),initialize=0)
m.i69 = Var(within=Integers,bounds=(0,2147483647),initialize=0)
m.i70 = Var(within=Integers,bounds=(0,2147483647),initialize=0)
m.i71 = Var(within=Integers,bounds=(0,2147483647),initialize=0)
m.i72 = Var(within=Integers,bounds=(0,2147483647),initialize=0)
m.i73 = Var(within=Integers,bounds=(0,None),initialize=0)
m.i74 = Var(within=Integers,bounds=(0,None),initialize=0)
m.i75 = Var(within=Integers,bounds=(0,None),initialize=0)
m.i76 = Var(within=Integers,bounds=(0,None),initialize=0)
m.i77 = Var(within=Integers,bounds=(0,None),initialize=0)
m.i78 = Var(within=Integers,bounds=(0,None),initialize=0)
m.i79 = Var(within=Integers,bounds=(0,None),initialize=0)
m.i80 = Var(within=Integers,bounds=(0,None),initialize=0)
m.i81 = Var(within=Integers,bounds=(0,None),initialize=0)
m.i82 = Var(within=Integers,bounds=(0,None),initialize=0)
m.i83 = Var(within=Integers,bounds=(0,None),initialize=0)
m.i84 = Var(within=Integers,bounds=(0,None),initialize=0)
m.x85 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x86 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x87 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x88 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x89 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x90 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x91 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x92 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x93 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x94 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x95 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x96 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x97 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x98 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x99 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x100 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x101 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x102 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x103 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x104 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x105 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x106 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x107 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x108 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x109 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x110 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x111 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x112 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x113 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x114 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x115 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x116 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x117 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x118 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x119 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x120 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x121 = Var(within=Reals,bounds=(-12000,12000),initialize=0)
m.x122 = Var(within=Reals,bounds=(-12000,12000),initialize=0)
m.x123 = Var(within=Reals,bounds=(-12000,12000),initialize=0)
m.x124 = Var(within=Reals,bounds=(-12000,12000),initialize=0)
m.x125 = Var(within=Reals,bounds=(-12000,12000),initialize=0)
m.x126 = Var(within=Reals,bounds=(-12000,12000),initialize=0)
m.x127 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x128 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x129 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x130 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x131 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x132 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x133 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x134 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x135 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x136 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x137 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x138 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x139 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x140 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x141 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x142 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x143 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x144 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x145 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x146 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x147 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x148 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x149 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x150 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x151 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x152 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x153 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x154 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x155 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x156 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=   0.0009231163463866*m.x127 + 0.0008521437889662*m.x128 + 0.0007866278610666*m.x129
                        + 0.0009231163463866*m.x130 + 0.0008521437889662*m.x131 + 0.0007866278610666*m.x132
                       , sense=minimize)

m.c1 = Constraint(expr=   m.b2 + m.b8 + m.b14 == 1)

m.c2 = Constraint(expr=   m.b3 + m.b9 + m.b15 == 1)

m.c3 = Constraint(expr=   m.b4 + m.b10 + m.b16 == 1)

m.c4 = Constraint(expr=   m.b5 + m.b11 + m.b17 == 1)

m.c5 = Constraint(expr=   m.b6 + m.b12 + m.b18 == 1)

m.c6 = Constraint(expr=   m.b25 + m.b28 == 1)

m.c7 = Constraint(expr=   m.b26 + m.b29 == 1)

m.c8 = Constraint(expr=   m.b27 + m.b30 == 1)

m.c9 = Constraint(expr=   m.b19 + m.b22 == 1)

m.c10 = Constraint(expr=   m.b20 + m.b23 == 1)

m.c11 = Constraint(expr=   m.b21 + m.b24 == 1)

m.c12 = Constraint(expr=-1.11111111111111*m.x91*(2025*m.b1 + 4420*m.b7 + 7050*m.b13)/m.i48 + m.x151 == -2100)

m.c13 = Constraint(expr=-1.11111111111111*m.x92*(2025*m.b2 + 4420*m.b8 + 7050*m.b14)/m.i49 + m.x152 == -2100)

m.c14 = Constraint(expr=-1.11111111111111*m.x93*(2025*m.b3 + 4420*m.b9 + 7050*m.b15)/m.i50 + m.x153 == -2100)

m.c15 = Constraint(expr=-1.11111111111111*m.x94*(2025*m.b4 + 4420*m.b10 + 7050*m.b16)/m.i52 + m.x154 == -2100)

m.c16 = Constraint(expr=-1.11111111111111*m.x95*(2025*m.b5 + 4420*m.b11 + 7050*m.b17)/m.i53 + m.x155 == -2100)

m.c17 = Constraint(expr=-1.11111111111111*m.x96*(2025*m.b6 + 4420*m.b12 + 7050*m.b18)/m.i54 + m.x156 == -2100)

m.c18 = Constraint(expr=-(480*m.b25 + 360*m.b28)*(1 + 0.1*m.b1 + 0.1*m.b7 + 0.1*m.b13)*(1 + m.x85) + m.x91 == 0)

m.c19 = Constraint(expr=-(480*m.b26 + 360*m.b29)*(1 + 0.1*m.b2 + 0.1*m.b8 + 0.1*m.b14)*(1 + m.x86) + m.x92 == 0)

m.c20 = Constraint(expr=-(480*m.b27 + 360*m.b30)*(1 + 0.1*m.b3 + 0.1*m.b9 + 0.1*m.b15)*(1 + m.x87) + m.x93 == 0)

m.c21 = Constraint(expr=-(450*m.b19 + 400*m.b22)*(1 + 0.1*m.b4 + 0.1*m.b10 + 0.1*m.b16)*(1 + m.x88) + m.x94 == 0)

m.c22 = Constraint(expr=-(450*m.b20 + 400*m.b23)*(1 + 0.1*m.b5 + 0.1*m.b11 + 0.1*m.b17)*(1 + m.x89) + m.x95 == 0)

m.c23 = Constraint(expr=-(450*m.b21 + 400*m.b24)*(1 + 0.1*m.b6 + 0.1*m.b12 + 0.1*m.b18)*(1 + m.x90) + m.x96 == 0)

m.c24 = Constraint(expr=   m.x121 - m.x151 == 0)

m.c25 = Constraint(expr=(-m.x121*m.i48/m.i49) - (m.x121*m.i56 + m.x124*m.i62)/m.i49 + (m.x121*m.i56 + m.x121*m.i59)/
                        m.i49 + m.x122 - m.x152 == 0)

m.c26 = Constraint(expr=(-m.x122*m.i49/m.i50) - (m.x122*m.i57 + m.x125*m.i63)/m.i50 + (m.x122*m.i57 + m.x122*m.i60)/
                        m.i50 + m.x123 - m.x153 == 0)

m.c27 = Constraint(expr=   m.x124 - m.x154 == 0)

m.c28 = Constraint(expr=(-m.x124*m.i52/m.i53) - (m.x121*m.i59 + m.x124*m.i65)/m.i53 + (m.x124*m.i62 + m.x124*m.i65)/
                        m.i53 + m.x125 - m.x155 == 0)

m.c29 = Constraint(expr=(-m.x125*m.i53/m.i54) - (m.x122*m.i60 + m.x125*m.i66)/m.i54 + (m.x125*m.i63 + m.x125*m.i66)/
                        m.i54 + m.x126 - m.x156 == 0)

m.c30 = Constraint(expr=   m.i31 == 1100)

m.c31 = Constraint(expr= - m.i31 + m.i32 + m.i58 - m.i61 - m.i73 == 0)

m.c32 = Constraint(expr= - m.i32 + m.i33 + m.i59 - m.i62 - m.i74 == 0)

m.c33 = Constraint(expr= - m.i33 + m.i34 + m.i60 - m.i63 - m.i75 == 0)

m.c34 = Constraint(expr=   m.i35 == 2200)

m.c35 = Constraint(expr= - m.i35 + m.i36 - m.i58 + m.i61 - m.i76 == 0)

m.c36 = Constraint(expr= - m.i36 + m.i37 - m.i59 + m.i62 - m.i77 == 0)

m.c37 = Constraint(expr= - m.i37 + m.i38 - m.i60 + m.i63 - m.i78 == 0)

m.c38 = Constraint(expr=   m.i39 == 150)

m.c39 = Constraint(expr= - m.i39 + m.i40 - m.i79 == 0)

m.c40 = Constraint(expr= - m.i40 + m.i41 - m.i80 == 0)

m.c41 = Constraint(expr= - m.i41 + m.i42 - m.i81 == 0)

m.c42 = Constraint(expr=   m.i43 == 100)

m.c43 = Constraint(expr= - m.i43 + m.i44 - m.i82 == 0)

m.c44 = Constraint(expr= - m.i44 + m.i45 - m.i83 == 0)

m.c45 = Constraint(expr= - m.i45 + m.i46 - m.i84 == 0)

m.c46 = Constraint(expr= - m.i31 - m.i39 + m.i47 == 0)

m.c47 = Constraint(expr= - m.i32 - m.i40 + m.i48 == 0)

m.c48 = Constraint(expr= - m.i33 - m.i41 + m.i49 == 0)

m.c49 = Constraint(expr= - m.i34 - m.i42 + m.i50 == 0)

m.c50 = Constraint(expr= - m.i35 - m.i43 + m.i51 == 0)

m.c51 = Constraint(expr= - m.i36 - m.i44 + m.i52 == 0)

m.c52 = Constraint(expr= - m.i37 - m.i45 + m.i53 == 0)

m.c53 = Constraint(expr= - m.i38 - m.i46 + m.i54 == 0)

m.c54 = Constraint(expr=(-1.11111111111*m.x91*m.b1) - 2.22222222222*m.x91*m.b7 - 3.33333333333*m.x91*m.b13 + m.i48 >= 0)

m.c55 = Constraint(expr=(-1.11111111111*m.x92*m.b2) - 2.22222222222*m.x92*m.b8 - 3.33333333333*m.x92*m.b14 + m.i49 >= 0)

m.c56 = Constraint(expr=(-1.11111111111*m.x93*m.b3) - 2.22222222222*m.x93*m.b9 - 3.33333333333*m.x93*m.b15 + m.i50 >= 0)

m.c57 = Constraint(expr=(-1.11111111111*m.x94*m.b4) - 2.22222222222*m.x94*m.b10 - 3.33333333333*m.x94*m.b16 + m.i52
                         >= 0)

m.c58 = Constraint(expr=(-1.11111111111*m.x95*m.b5) - 2.22222222222*m.x95*m.b11 - 3.33333333333*m.x95*m.b17 + m.i53
                         >= 0)

m.c59 = Constraint(expr=(-1.11111111111*m.x96*m.b6) - 2.22222222222*m.x96*m.b12 - 3.33333333333*m.x96*m.b18 + m.i54
                         >= 0)

m.c60 = Constraint(expr=   m.i73 >= 0)

m.c61 = Constraint(expr=   m.i74 >= 0)

m.c62 = Constraint(expr=   m.i75 >= 0)

m.c63 = Constraint(expr=   m.i76 >= 0)

m.c64 = Constraint(expr=   m.i77 >= 0)

m.c65 = Constraint(expr=   m.i78 >= 0)

m.c66 = Constraint(expr= - m.i73 + m.x115 >= 0)

m.c67 = Constraint(expr= - m.i74 + m.x116 >= 0)

m.c68 = Constraint(expr= - m.i75 + m.x117 >= 0)

m.c69 = Constraint(expr= - m.i76 + m.x118 >= 0)

m.c70 = Constraint(expr= - m.i77 + m.x119 >= 0)

m.c71 = Constraint(expr= - m.i78 + m.x120 >= 0)

m.c72 = Constraint(expr= - m.i79 + m.x109 >= 0)

m.c73 = Constraint(expr= - m.i80 + m.x110 >= 0)

m.c74 = Constraint(expr= - m.i81 + m.x111 >= 0)

m.c75 = Constraint(expr= - m.i82 + m.x112 >= 0)

m.c76 = Constraint(expr= - m.i83 + m.x113 >= 0)

m.c77 = Constraint(expr= - m.i84 + m.x114 >= 0)

m.c78 = Constraint(expr= - m.x109 - m.x112 - m.x115 - m.x118 >= -100)

m.c79 = Constraint(expr= - m.x110 - m.x113 - m.x116 - m.x119 >= -100)

m.c80 = Constraint(expr= - m.x111 - m.x114 - m.x117 - m.x120 >= -100)

m.c81 = Constraint(expr=   m.i40 - 0.2*m.i48 <= 0)

m.c82 = Constraint(expr=   m.i41 - 0.2*m.i49 <= 0)

m.c83 = Constraint(expr=   m.i42 - 0.2*m.i50 <= 0)

m.c84 = Constraint(expr=   m.i44 - 0.2*m.i52 <= 0)

m.c85 = Constraint(expr=   m.i45 - 0.2*m.i53 <= 0)

m.c86 = Constraint(expr=   m.i46 - 0.2*m.i54 <= 0)

m.c87 = Constraint(expr=   m.i55 == 0)

m.c88 = Constraint(expr=   m.i56 == 0)

m.c89 = Constraint(expr=   m.i57 == 0)

m.c90 = Constraint(expr=   m.i64 == 0)

m.c91 = Constraint(expr=   m.i65 == 0)

m.c92 = Constraint(expr=   m.i66 == 0)

m.c93 = Constraint(expr=   m.i67 + m.i70 <= 2739)

m.c94 = Constraint(expr=   m.i68 + m.i71 <= 2739)

m.c95 = Constraint(expr=   m.i69 + m.i72 <= 2607)

m.c96 = Constraint(expr=   m.i67 + m.i70 >= 2241)

m.c97 = Constraint(expr=   m.i68 + m.i71 >= 2241)

m.c98 = Constraint(expr=   m.i69 + m.i72 >= 2133)

m.c99 = Constraint(expr=   m.i67 + m.i68 + m.i69 + m.i70 + m.i71 + m.i72 >= 7350)

m.c100 = Constraint(expr=-(1950*m.b1 + 4200*m.b7 + 6600*m.b13)/(4*m.b25 + 7*m.b28) + m.i67 <= 0)

m.c101 = Constraint(expr=-(1950*m.b2 + 4200*m.b8 + 6600*m.b14)/(4*m.b26 + 7*m.b29) + m.i68 <= 0)

m.c102 = Constraint(expr=-(1950*m.b3 + 4200*m.b9 + 6600*m.b15)/(4*m.b27 + 7*m.b30) + m.i69 <= 0)

m.c103 = Constraint(expr=-(1950*m.b4 + 4200*m.b10 + 6600*m.b16)/(5*m.b19 + 6*m.b22) + m.i70 <= 0)

m.c104 = Constraint(expr=-(1950*m.b5 + 4200*m.b11 + 6600*m.b17)/(5*m.b20 + 6*m.b23) + m.i71 <= 0)

m.c105 = Constraint(expr=-(1950*m.b6 + 4200*m.b12 + 6600*m.b18)/(5*m.b21 + 6*m.b24) + m.i72 <= 0)

m.c106 = Constraint(expr=(m.b1 - m.b2 + 2*m.b7 - 2*m.b8 + 3*m.b13 - 3*m.b14)**2*m.x97 - 10000*(m.b1 - m.b2 + 2*m.b7 - 2*
                         m.b8 + 3*m.b13 - 3*m.b14)**2 >= 0)

m.c107 = Constraint(expr=(m.b2 - m.b3 + 2*m.b8 - 2*m.b9 + 3*m.b14 - 3*m.b15)**2*m.x98 - 10000*(m.b2 - m.b3 + 2*m.b8 - 2*
                         m.b9 + 3*m.b14 - 3*m.b15)**2 >= 0)

m.c108 = Constraint(expr=(m.b3 + 2*m.b9 + 3*m.b15)**2*m.x99 - 10000*(m.b3 + 2*m.b9 + 3*m.b15)**2 >= 0)

m.c109 = Constraint(expr=(m.b4 - m.b5 + 2*m.b10 - 2*m.b11 + 3*m.b16 - 3*m.b17)**2*m.x100 - 10000*(m.b4 - m.b5 + 2*m.b10
                          - 2*m.b11 + 3*m.b16 - 3*m.b17)**2 >= 0)

m.c110 = Constraint(expr=(m.b5 - m.b6 + 2*m.b11 - 2*m.b12 + 3*m.b17 - 3*m.b18)**2*m.x101 - 10000*(m.b5 - m.b6 + 2*m.b11
                          - 2*m.b12 + 3*m.b17 - 3*m.b18)**2 >= 0)

m.c111 = Constraint(expr=(m.b6 + 2*m.b12 + 3*m.b18)**2*m.x102 - 10000*(m.b6 + 2*m.b12 + 3*m.b18)**2 >= 0)

m.c112 = Constraint(expr=(4*m.b25 - 4*m.b26 + 7*m.b28 - 7*m.b29)**2*m.x103 - (4*m.b25 - 4*m.b26 + 7*m.b28 - 7*m.b29)**2*
                         (1000000 + 1000*m.i48) >= 0)

m.c113 = Constraint(expr=(4*m.b26 - 4*m.b27 + 7*m.b29 - 7*m.b30)**2*m.x104 - (4*m.b26 - 4*m.b27 + 7*m.b29 - 7*m.b30)**2*
                         (1000000 + 1000*m.i49) >= 0)

m.c114 = Constraint(expr=(4*m.b27 + 7*m.b30)**2*m.x105 - (4*m.b27 + 7*m.b30)**2*(1000000 + 1000*m.i50) >= 0)

m.c115 = Constraint(expr=(5*m.b19 - 5*m.b20 + 6*m.b22 - 6*m.b23)**2*m.x106 - (5*m.b19 - 5*m.b20 + 6*m.b22 - 6*m.b23)**2*
                         (1000000 + 1000*m.i52) >= 0)

m.c116 = Constraint(expr=(5*m.b20 - 5*m.b21 + 6*m.b23 - 6*m.b24)**2*m.x107 - (5*m.b20 - 5*m.b21 + 6*m.b23 - 6*m.b24)**2*
                         (1000000 + 1000*m.i53) >= 0)

m.c117 = Constraint(expr=(5*m.b21 + 6*m.b24)**2*m.x108 - (5*m.b21 + 6*m.b24)**2*(1000000 + 1000*m.i54) >= 0)

m.c118 = Constraint(expr=   m.x145 == 0)

m.c119 = Constraint(expr=   m.x146 == 0)

m.c120 = Constraint(expr=   m.x147 == 0)

m.c121 = Constraint(expr=   m.x148 == 0)

m.c122 = Constraint(expr=   m.x149 == 0)

m.c123 = Constraint(expr=   m.x150 == 0)

m.c124 = Constraint(expr=   m.x139 == 0)

m.c125 = Constraint(expr=   m.x140 == 0)

m.c126 = Constraint(expr=   m.x141 == 0)

m.c127 = Constraint(expr=   m.x142 == 0)

m.c128 = Constraint(expr=   m.x143 == 0)

m.c129 = Constraint(expr=   m.x144 == 0)

m.c130 = Constraint(expr= - 1000*m.i55 - 1000*m.i61 + m.x133 == 0)

m.c131 = Constraint(expr= - 1000*m.i56 - 1000*m.i62 + m.x134 == 0)

m.c132 = Constraint(expr= - 1000*m.i57 - 1000*m.i63 + m.x135 == 0)

m.c133 = Constraint(expr= - 1000*m.i58 - 1000*m.i64 + m.x136 == 0)

m.c134 = Constraint(expr= - 1000*m.i59 - 1000*m.i65 + m.x137 == 0)

m.c135 = Constraint(expr= - 1000*m.i60 - 1000*m.i66 + m.x138 == 0)

m.c136 = Constraint(expr= - m.x97 - m.x100 - m.x103 - m.x106 + m.x130 - m.x133 - m.x136 - m.x139 - m.x142 - m.x145
                          - m.x148 == 0)

m.c137 = Constraint(expr= - m.x98 - m.x101 - m.x104 - m.x107 + m.x131 - m.x134 - m.x137 - m.x140 - m.x143 - m.x146
                          - m.x149 == 0)

m.c138 = Constraint(expr= - m.x99 - m.x102 - m.x105 - m.x108 + m.x132 - m.x135 - m.x138 - m.x141 - m.x144 - m.x147
                          - m.x150 == 0)

m.c139 = Constraint(expr=(-315*m.i40*m.b7) - 2100*m.i40 - 420*m.i40*m.b13 - 315*m.i44*m.b10 - 2100*m.i44 - 420*m.i44*
                         m.b16 - 210*m.i32*m.b7 - 1400*m.i32 - 280*m.i32*m.b13 - 210*m.i36*m.b10 - 1400*m.i36 - 280*
                         m.i36*m.b16 + m.x127 == 0)

m.c140 = Constraint(expr=(-315*m.i41*m.b8) - 2100*m.i41 - 420*m.i41*m.b14 - 315*m.i45*m.b11 - 2100*m.i45 - 420*m.i45*
                         m.b17 - 210*m.i33*m.b8 - 1400*m.i33 - 280*m.i33*m.b14 - 210*m.i37*m.b11 - 1400*m.i37 - 280*
                         m.i37*m.b17 + m.x128 == 0)

m.c141 = Constraint(expr=(-315*m.i42*m.b9) - 2100*m.i42 - 420*m.i42*m.b15 - 315*m.i46*m.b12 - 2100*m.i46 - 420*m.i46*
                         m.b18 - 210*m.i34*m.b9 - 1400*m.i34 - 280*m.i34*m.b15 - 210*m.i38*m.b12 - 1400*m.i38 - 280*
                         m.i38*m.b18 + m.x129 == 0)

m.c142 = Constraint(expr=   m.b1 + m.b7 + m.b13 == 1)
