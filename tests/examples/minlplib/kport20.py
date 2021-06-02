#  MINLP written by GAMS Convert at 04/21/18 13:52:28
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         28       22        2        4        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        102       62        2       38        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        190       74      116        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x3 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x4 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x5 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x6 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x7 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x8 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x9 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x10 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x11 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x12 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x13 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x14 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x15 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x16 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x17 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x18 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x19 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x20 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x21 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x22 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x23 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x24 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x25 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x26 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x27 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x28 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x29 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x30 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x31 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x32 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x33 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x34 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x35 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x36 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x37 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x38 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x39 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x40 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x41 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x42 = Var(within=Reals,bounds=(102.14,None),initialize=102.14)
m.x43 = Var(within=Reals,bounds=(176.07,None),initialize=176.07)
m.x44 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x45 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x46 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x47 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x48 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x49 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x50 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x51 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x52 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x53 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x54 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x55 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x56 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x57 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x58 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x59 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x60 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x61 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x62 = Var(within=Reals,bounds=(0,1),initialize=0)
m.b63 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b64 = Var(within=Binary,bounds=(0,1),initialize=0)
m.i65 = Var(within=Integers,bounds=(0,28),initialize=0)
m.i66 = Var(within=Integers,bounds=(0,28),initialize=0)
m.i67 = Var(within=Integers,bounds=(0,28),initialize=0)
m.i68 = Var(within=Integers,bounds=(0,25),initialize=0)
m.i69 = Var(within=Integers,bounds=(0,25),initialize=0)
m.i70 = Var(within=Integers,bounds=(0,13),initialize=0)
m.i71 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i72 = Var(within=Integers,bounds=(0,11),initialize=0)
m.i73 = Var(within=Integers,bounds=(0,7),initialize=0)
m.i74 = Var(within=Integers,bounds=(0,4),initialize=0)
m.i75 = Var(within=Integers,bounds=(0,3),initialize=0)
m.i76 = Var(within=Integers,bounds=(0,19),initialize=0)
m.i77 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i78 = Var(within=Integers,bounds=(0,7),initialize=0)
m.i79 = Var(within=Integers,bounds=(0,4),initialize=0)
m.i80 = Var(within=Integers,bounds=(0,3),initialize=0)
m.i81 = Var(within=Integers,bounds=(0,2),initialize=0)
m.i82 = Var(within=Integers,bounds=(0,2),initialize=0)
m.i83 = Var(within=Integers,bounds=(0,2),initialize=0)
m.i84 = Var(within=Integers,bounds=(0,28),initialize=0)
m.i85 = Var(within=Integers,bounds=(0,28),initialize=0)
m.i86 = Var(within=Integers,bounds=(0,28),initialize=0)
m.i87 = Var(within=Integers,bounds=(0,15),initialize=0)
m.i88 = Var(within=Integers,bounds=(0,15),initialize=0)
m.i89 = Var(within=Integers,bounds=(0,7),initialize=0)
m.i90 = Var(within=Integers,bounds=(0,7),initialize=0)
m.i91 = Var(within=Integers,bounds=(0,6),initialize=0)
m.i92 = Var(within=Integers,bounds=(0,4),initialize=0)
m.i93 = Var(within=Integers,bounds=(0,2),initialize=0)
m.i94 = Var(within=Integers,bounds=(0,1),initialize=0)
m.i95 = Var(within=Integers,bounds=(0,11),initialize=0)
m.i96 = Var(within=Integers,bounds=(0,7),initialize=0)
m.i97 = Var(within=Integers,bounds=(0,4),initialize=0)
m.i98 = Var(within=Integers,bounds=(0,2),initialize=0)
m.i99 = Var(within=Integers,bounds=(0,1),initialize=0)
m.i100 = Var(within=Integers,bounds=(0,1),initialize=0)
m.i101 = Var(within=Integers,bounds=(0,1),initialize=0)
m.i102 = Var(within=Integers,bounds=(0,1),initialize=0)

m.obj = Objective(expr=   m.x2 + m.x3, sense=minimize)

m.c2 = Constraint(expr=   m.x3 - 2.45*m.b63 - 2.45*m.b64 == 0)

m.c3 = Constraint(expr=-(0.98488578017961*m.x42**0.5 + 0.98488578017961*m.x43**0.5) + m.x2 == 0)

m.c4 = Constraint(expr= - 168*m.b63 + 6*m.i65 + 6*m.i66 + 6*m.i67 + 6*m.i68 + 6*m.i69 + 6*m.i70 + 6*m.i71 + 6*m.i72
                        + 6*m.i73 + 6*m.i74 + 6*m.i75 + 6*m.i76 + 6*m.i77 + 6*m.i78 + 6*m.i79 + 6*m.i80 + 6*m.i81
                        + 6*m.i82 + 6*m.i83 <= 0)

m.c5 = Constraint(expr= - 168*m.b64 + 6*m.i84 + 6*m.i85 + 6*m.i86 + 6*m.i87 + 6*m.i88 + 6*m.i89 + 6*m.i90 + 6*m.i91
                        + 6*m.i92 + 6*m.i93 + 6*m.i94 + 6*m.i95 + 6*m.i96 + 6*m.i97 + 6*m.i98 + 6*m.i99 + 6*m.i100
                        + 6*m.i101 + 6*m.i102 <= 0)

m.c6 = Constraint(expr=-0.000384615384615385*(m.i65*m.x4*m.x42 + m.i84*m.x23*m.x43) + m.x44 == -1)

m.c7 = Constraint(expr=-0.000434782608695652*(m.i66*m.x5*m.x42 + m.i85*m.x24*m.x43) + m.x45 == -1)

m.c8 = Constraint(expr=-0.000588235294117647*(m.i67*m.x6*m.x42 + m.i86*m.x25*m.x43) + m.x46 == -1)

m.c9 = Constraint(expr=-0.00188679245283019*(m.i68*m.x7*m.x42 + m.i87*m.x26*m.x43) + m.x47 == -1)

m.c10 = Constraint(expr=-0.00188679245283019*(m.i69*m.x8*m.x42 + m.i88*m.x27*m.x43) + m.x48 == -1)

m.c11 = Constraint(expr=-0.00357142857142857*(m.i70*m.x9*m.x42 + m.i89*m.x28*m.x43) + m.x49 == -1)

m.c12 = Constraint(expr=-0.004*(m.i71*m.x10*m.x42 + m.i90*m.x29*m.x43) + m.x50 == -1)

m.c13 = Constraint(expr=-0.00434782608695652*(m.i72*m.x11*m.x42 + m.i91*m.x30*m.x43) + m.x51 == -1)

m.c14 = Constraint(expr=-0.00625*(m.i73*m.x12*m.x42 + m.i92*m.x31*m.x43) + m.x52 == -1)

m.c15 = Constraint(expr=-0.0111111111111111*(m.i74*m.x13*m.x42 + m.i93*m.x32*m.x43) + m.x53 == -1)

m.c16 = Constraint(expr=-0.0142857142857143*(m.i75*m.x14*m.x42 + m.i94*m.x33*m.x43) + m.x54 == -1)

m.c17 = Constraint(expr=-0.00256410256410256*(m.i76*m.x15*m.x42 + m.i95*m.x34*m.x43) + m.x55 == -1)

m.c18 = Constraint(expr=-0.004*(m.i77*m.x16*m.x42 + m.i96*m.x35*m.x43) + m.x56 == -1)

m.c19 = Constraint(expr=-0.00625*(m.i78*m.x17*m.x42 + m.i97*m.x36*m.x43) + m.x57 == -1)

m.c20 = Constraint(expr=-0.01*(m.i79*m.x18*m.x42 + m.i98*m.x37*m.x43) + m.x58 == -1)

m.c21 = Constraint(expr=-0.0142857142857143*(m.i80*m.x19*m.x42 + m.i99*m.x38*m.x43) + m.x59 == -1)

m.c22 = Constraint(expr=-0.02*(m.i81*m.x20*m.x42 + m.i100*m.x39*m.x43) + m.x60 == -1)

m.c23 = Constraint(expr=-0.02*(m.i82*m.x21*m.x42 + m.i101*m.x40*m.x43) + m.x61 == -1)

m.c24 = Constraint(expr=-0.02*(m.i83*m.x22*m.x42 + m.i102*m.x41*m.x43) + m.x62 == -1)

m.c25 = Constraint(expr=   m.x42 - 102.14*m.b63 >= 0)

m.c26 = Constraint(expr=   m.x43 - 176.07*m.b64 >= 0)

m.c27 = Constraint(expr=   m.x42 - 250*m.b63 <= 0)

m.c28 = Constraint(expr=   m.x43 - 250*m.b64 <= 0)
