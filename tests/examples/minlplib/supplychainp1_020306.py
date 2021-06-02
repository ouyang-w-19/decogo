#  MINLP written by GAMS Convert at 04/21/18 13:54:26
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        256       49       45      162        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        151      124       27        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        709      700        9        0
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
m.x28 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,12),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,12),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x34 = Var(within=Reals,bounds=(0,14),initialize=0)
m.x35 = Var(within=Reals,bounds=(0,14),initialize=0)
m.x36 = Var(within=Reals,bounds=(0,14),initialize=0)
m.x37 = Var(within=Reals,bounds=(0,13),initialize=0)
m.x38 = Var(within=Reals,bounds=(0,14),initialize=0)
m.x39 = Var(within=Reals,bounds=(0,15),initialize=0)
m.x41 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x42 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x43 = Var(within=Reals,bounds=(0,1),initialize=0)
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
m.x63 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x64 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x65 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x66 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x67 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x68 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x69 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x70 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x71 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x72 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x73 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x74 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x75 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x76 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x77 = Var(within=Reals,bounds=(0,40007.5009381706),initialize=0)
m.x78 = Var(within=Reals,bounds=(0,48009.0011258047),initialize=0)
m.x79 = Var(within=Reals,bounds=(0,44008.2510319877),initialize=0)
m.x80 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x81 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x82 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x83 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x84 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x85 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x86 = Var(within=Reals,bounds=(0,12),initialize=0)
m.x87 = Var(within=Reals,bounds=(0,12),initialize=0)
m.x88 = Var(within=Reals,bounds=(0,12),initialize=0)
m.x89 = Var(within=Reals,bounds=(0,12),initialize=0)
m.x90 = Var(within=Reals,bounds=(0,12),initialize=0)
m.x91 = Var(within=Reals,bounds=(0,12),initialize=0)
m.x92 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x93 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x94 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x95 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x96 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x97 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x98 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x99 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x100 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x101 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x102 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x103 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x104 = Var(within=Reals,bounds=(0,12),initialize=0)
m.x105 = Var(within=Reals,bounds=(0,12),initialize=0)
m.x106 = Var(within=Reals,bounds=(0,12),initialize=0)
m.x107 = Var(within=Reals,bounds=(0,12),initialize=0)
m.x108 = Var(within=Reals,bounds=(0,12),initialize=0)
m.x109 = Var(within=Reals,bounds=(0,12),initialize=0)
m.x110 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x111 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x112 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x113 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x114 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x115 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x116 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x117 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x118 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x119 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x120 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x121 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x122 = Var(within=Reals,bounds=(0,12),initialize=0)
m.x123 = Var(within=Reals,bounds=(0,12),initialize=0)
m.x124 = Var(within=Reals,bounds=(0,12),initialize=0)
m.x125 = Var(within=Reals,bounds=(0,12),initialize=0)
m.x126 = Var(within=Reals,bounds=(0,12),initialize=0)
m.x127 = Var(within=Reals,bounds=(0,12),initialize=0)
m.x128 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x129 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x130 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x131 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x132 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x133 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x134 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x135 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x136 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x137 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x138 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x139 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x140 = Var(within=Reals,bounds=(0,12),initialize=0)
m.x141 = Var(within=Reals,bounds=(0,12),initialize=0)
m.x142 = Var(within=Reals,bounds=(0,12),initialize=0)
m.x143 = Var(within=Reals,bounds=(0,12),initialize=0)
m.x144 = Var(within=Reals,bounds=(0,12),initialize=0)
m.x145 = Var(within=Reals,bounds=(0,12),initialize=0)
m.x146 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x147 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x148 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x149 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x150 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x151 = Var(within=Reals,bounds=(0,11),initialize=0)

m.obj = Objective(expr=322.234552934*sqrt(1e-6 + m.x77) + 302.50169455058*sqrt(1e-6 + m.x78) + 228.02026850162*sqrt(1e-6
                        + m.x79) + 6050.05692401735*sqrt(1e-6 + m.x34) + 5835.32285968594*sqrt(1e-6 + m.x35) + 
                       5989.86353513014*sqrt(1e-6 + m.x36) + 539.712349032506*sqrt(1e-6 + m.x37) + 16850.0288492985*
                       sqrt(1e-6 + m.x38) + 8222.60184978362*sqrt(1e-6 + m.x39) + 151717.47132*m.b7 + 158432.66708*m.b8
                        + 155503.75356*m.b9 + 17986.4749305945*m.b10 + 16608.1293312542*m.b11 + 12718.9428305151*m.b12
                        + 31542.1682444641*m.b13 + 27684.4467382033*m.b14 + 21088.788254886*m.b15
                        + 32968.2805196111*m.b16 + 15382.4826683217*m.b17 + 13024.4125650671*m.b18
                        + 32589.6848153206*m.b19 + 20134.3014301096*m.b20 + 32223.2266900764*m.b21
                        + 17748.5846986448*m.b22 + 17549.9907064495*m.b23 + 36772.5625416759*m.b24
                        + 31609.4271891265*m.b25 + 9416.32984942185*m.b26 + 21045.6190121083*m.b27
                        + 12173.2900202663*m.x41 + 11461.683166994*m.x42 + 7650.9016787939*m.x43
                        + 13294.0811055533*m.x44 + 7956.7979482407*m.x45 + 8719.97128915194*m.x46
                        + 155924.233130298*m.x47 + 146809.461963092*m.x48 + 97998.2383591604*m.x49
                        + 170280.129538065*m.x50 + 101916.377264214*m.x51 + 111691.649004965*m.x52
                        + 70941.2467141159*m.x53 + 66794.2759890772*m.x54 + 44586.508879453*m.x55
                        + 77472.7855802693*m.x56 + 46369.154547438*m.x57 + 50816.6349059184*m.x58
                        + 62277.6953743628*m.x59 + 58637.1647732989*m.x60 + 39141.4747613728*m.x61
                        + 68011.5837210299*m.x62 + 40706.4185566037*m.x63 + 44610.7596808173*m.x64
                        + 268487.828840519*m.x65 + 252792.993779081*m.x66 + 168744.355633672*m.x67
                        + 293207.42104374*m.x68 + 175491.046552681*m.x69 + 192323.205565495*m.x70
                        + 66974.7313782537*m.x71 + 63059.6289067364*m.x72 + 42093.5576073164*m.x73
                        + 73141.0743917914*m.x74 + 43776.5307757616*m.x75 + 47975.3405812849*m.x76, sense=minimize)

m.c2 = Constraint(expr=   m.b1 + m.b4 - m.b7 == 0)

m.c3 = Constraint(expr=   m.b2 + m.b5 - m.b8 == 0)

m.c4 = Constraint(expr=   m.b3 + m.b6 - m.b9 == 0)

m.c5 = Constraint(expr= - m.b7 + m.b10 <= 0)

m.c6 = Constraint(expr= - m.b7 + m.b11 <= 0)

m.c7 = Constraint(expr= - m.b7 + m.b12 <= 0)

m.c8 = Constraint(expr= - m.b7 + m.b13 <= 0)

m.c9 = Constraint(expr= - m.b7 + m.b14 <= 0)

m.c10 = Constraint(expr= - m.b7 + m.b15 <= 0)

m.c11 = Constraint(expr= - m.b8 + m.b16 <= 0)

m.c12 = Constraint(expr= - m.b8 + m.b17 <= 0)

m.c13 = Constraint(expr= - m.b8 + m.b18 <= 0)

m.c14 = Constraint(expr= - m.b8 + m.b19 <= 0)

m.c15 = Constraint(expr= - m.b8 + m.b20 <= 0)

m.c16 = Constraint(expr= - m.b8 + m.b21 <= 0)

m.c17 = Constraint(expr= - m.b9 + m.b22 <= 0)

m.c18 = Constraint(expr= - m.b9 + m.b23 <= 0)

m.c19 = Constraint(expr= - m.b9 + m.b24 <= 0)

m.c20 = Constraint(expr= - m.b9 + m.b25 <= 0)

m.c21 = Constraint(expr= - m.b9 + m.b26 <= 0)

m.c22 = Constraint(expr= - m.b9 + m.b27 <= 0)

m.c23 = Constraint(expr=   m.b10 + m.b16 + m.b22 == 1)

m.c24 = Constraint(expr=   m.b11 + m.b17 + m.b23 == 1)

m.c25 = Constraint(expr=   m.b12 + m.b18 + m.b24 == 1)

m.c26 = Constraint(expr=   m.b13 + m.b19 + m.b25 == 1)

m.c27 = Constraint(expr=   m.b14 + m.b20 + m.b26 == 1)

m.c28 = Constraint(expr=   m.b15 + m.b21 + m.b27 == 1)

m.c29 = Constraint(expr= - 3*m.b1 - 10*m.b4 + m.x28 + m.x31 >= 0)

m.c30 = Constraint(expr= - 6*m.b2 - 12*m.b5 + m.x29 + m.x32 >= 0)

m.c31 = Constraint(expr= - 9*m.b3 - 11*m.b6 + m.x30 + m.x33 >= 0)

m.c32 = Constraint(expr= - m.b10 - 2*m.b16 - m.b22 + m.x34 - m.x116 - m.x122 - m.x128 >= 0)

m.c33 = Constraint(expr= - 2*m.b11 - 2*m.b17 - 2*m.b23 + m.x35 - m.x117 - m.x123 - m.x129 >= 0)

m.c34 = Constraint(expr= - m.b12 - m.b18 - 3*m.b24 + m.x36 - m.x118 - m.x124 - m.x130 >= 0)

m.c35 = Constraint(expr= - m.b13 - m.b19 - m.b25 + m.x37 - m.x119 - m.x125 - m.x131 >= 0)

m.c36 = Constraint(expr= - 3*m.b14 - 2*m.b20 - m.b26 + m.x38 - m.x120 - m.x126 - m.x132 >= 0)

m.c37 = Constraint(expr= - 2*m.b15 - 3*m.b21 - 2*m.b27 + m.x39 - m.x121 - m.x127 - m.x133 >= 0)

m.c38 = Constraint(expr= - m.b1 + m.x41 <= 0)

m.c39 = Constraint(expr= - m.b1 + m.x42 <= 0)

m.c40 = Constraint(expr= - m.b1 + m.x43 <= 0)

m.c41 = Constraint(expr= - m.b1 + m.x44 <= 0)

m.c42 = Constraint(expr= - m.b1 + m.x45 <= 0)

m.c43 = Constraint(expr= - m.b1 + m.x46 <= 0)

m.c44 = Constraint(expr= - m.b2 + m.x47 <= 0)

m.c45 = Constraint(expr= - m.b2 + m.x48 <= 0)

m.c46 = Constraint(expr= - m.b2 + m.x49 <= 0)

m.c47 = Constraint(expr= - m.b2 + m.x50 <= 0)

m.c48 = Constraint(expr= - m.b2 + m.x51 <= 0)

m.c49 = Constraint(expr= - m.b2 + m.x52 <= 0)

m.c50 = Constraint(expr= - m.b3 + m.x53 <= 0)

m.c51 = Constraint(expr= - m.b3 + m.x54 <= 0)

m.c52 = Constraint(expr= - m.b3 + m.x55 <= 0)

m.c53 = Constraint(expr= - m.b3 + m.x56 <= 0)

m.c54 = Constraint(expr= - m.b3 + m.x57 <= 0)

m.c55 = Constraint(expr= - m.b3 + m.x58 <= 0)

m.c56 = Constraint(expr= - m.b4 + m.x59 <= 0)

m.c57 = Constraint(expr= - m.b4 + m.x60 <= 0)

m.c58 = Constraint(expr= - m.b4 + m.x61 <= 0)

m.c59 = Constraint(expr= - m.b4 + m.x62 <= 0)

m.c60 = Constraint(expr= - m.b4 + m.x63 <= 0)

m.c61 = Constraint(expr= - m.b4 + m.x64 <= 0)

m.c62 = Constraint(expr= - m.b5 + m.x65 <= 0)

m.c63 = Constraint(expr= - m.b5 + m.x66 <= 0)

m.c64 = Constraint(expr= - m.b5 + m.x67 <= 0)

m.c65 = Constraint(expr= - m.b5 + m.x68 <= 0)

m.c66 = Constraint(expr= - m.b5 + m.x69 <= 0)

m.c67 = Constraint(expr= - m.b5 + m.x70 <= 0)

m.c68 = Constraint(expr= - m.b6 + m.x71 <= 0)

m.c69 = Constraint(expr= - m.b6 + m.x72 <= 0)

m.c70 = Constraint(expr= - m.b6 + m.x73 <= 0)

m.c71 = Constraint(expr= - m.b6 + m.x74 <= 0)

m.c72 = Constraint(expr= - m.b6 + m.x75 <= 0)

m.c73 = Constraint(expr= - m.b6 + m.x76 <= 0)

m.c74 = Constraint(expr= - m.b10 + m.x41 <= 0)

m.c75 = Constraint(expr= - m.b11 + m.x42 <= 0)

m.c76 = Constraint(expr= - m.b12 + m.x43 <= 0)

m.c77 = Constraint(expr= - m.b13 + m.x44 <= 0)

m.c78 = Constraint(expr= - m.b14 + m.x45 <= 0)

m.c79 = Constraint(expr= - m.b15 + m.x46 <= 0)

m.c80 = Constraint(expr= - m.b16 + m.x47 <= 0)

m.c81 = Constraint(expr= - m.b17 + m.x48 <= 0)

m.c82 = Constraint(expr= - m.b18 + m.x49 <= 0)

m.c83 = Constraint(expr= - m.b19 + m.x50 <= 0)

m.c84 = Constraint(expr= - m.b20 + m.x51 <= 0)

m.c85 = Constraint(expr= - m.b21 + m.x52 <= 0)

m.c86 = Constraint(expr= - m.b22 + m.x53 <= 0)

m.c87 = Constraint(expr= - m.b23 + m.x54 <= 0)

m.c88 = Constraint(expr= - m.b24 + m.x55 <= 0)

m.c89 = Constraint(expr= - m.b25 + m.x56 <= 0)

m.c90 = Constraint(expr= - m.b26 + m.x57 <= 0)

m.c91 = Constraint(expr= - m.b27 + m.x58 <= 0)

m.c92 = Constraint(expr= - m.b10 + m.x59 <= 0)

m.c93 = Constraint(expr= - m.b11 + m.x60 <= 0)

m.c94 = Constraint(expr= - m.b12 + m.x61 <= 0)

m.c95 = Constraint(expr= - m.b13 + m.x62 <= 0)

m.c96 = Constraint(expr= - m.b14 + m.x63 <= 0)

m.c97 = Constraint(expr= - m.b15 + m.x64 <= 0)

m.c98 = Constraint(expr= - m.b16 + m.x65 <= 0)

m.c99 = Constraint(expr= - m.b17 + m.x66 <= 0)

m.c100 = Constraint(expr= - m.b18 + m.x67 <= 0)

m.c101 = Constraint(expr= - m.b19 + m.x68 <= 0)

m.c102 = Constraint(expr= - m.b20 + m.x69 <= 0)

m.c103 = Constraint(expr= - m.b21 + m.x70 <= 0)

m.c104 = Constraint(expr= - m.b22 + m.x71 <= 0)

m.c105 = Constraint(expr= - m.b23 + m.x72 <= 0)

m.c106 = Constraint(expr= - m.b24 + m.x73 <= 0)

m.c107 = Constraint(expr= - m.b25 + m.x74 <= 0)

m.c108 = Constraint(expr= - m.b26 + m.x75 <= 0)

m.c109 = Constraint(expr= - m.b27 + m.x76 <= 0)

m.c110 = Constraint(expr= - m.b1 - m.b10 + m.x41 >= -1)

m.c111 = Constraint(expr= - m.b1 - m.b11 + m.x42 >= -1)

m.c112 = Constraint(expr= - m.b1 - m.b12 + m.x43 >= -1)

m.c113 = Constraint(expr= - m.b1 - m.b13 + m.x44 >= -1)

m.c114 = Constraint(expr= - m.b1 - m.b14 + m.x45 >= -1)

m.c115 = Constraint(expr= - m.b1 - m.b15 + m.x46 >= -1)

m.c116 = Constraint(expr= - m.b2 - m.b16 + m.x47 >= -1)

m.c117 = Constraint(expr= - m.b2 - m.b17 + m.x48 >= -1)

m.c118 = Constraint(expr= - m.b2 - m.b18 + m.x49 >= -1)

m.c119 = Constraint(expr= - m.b2 - m.b19 + m.x50 >= -1)

m.c120 = Constraint(expr= - m.b2 - m.b20 + m.x51 >= -1)

m.c121 = Constraint(expr= - m.b2 - m.b21 + m.x52 >= -1)

m.c122 = Constraint(expr= - m.b3 - m.b22 + m.x53 >= -1)

m.c123 = Constraint(expr= - m.b3 - m.b23 + m.x54 >= -1)

m.c124 = Constraint(expr= - m.b3 - m.b24 + m.x55 >= -1)

m.c125 = Constraint(expr= - m.b3 - m.b25 + m.x56 >= -1)

m.c126 = Constraint(expr= - m.b3 - m.b26 + m.x57 >= -1)

m.c127 = Constraint(expr= - m.b3 - m.b27 + m.x58 >= -1)

m.c128 = Constraint(expr= - m.b4 - m.b10 + m.x59 >= -1)

m.c129 = Constraint(expr= - m.b4 - m.b11 + m.x60 >= -1)

m.c130 = Constraint(expr= - m.b4 - m.b12 + m.x61 >= -1)

m.c131 = Constraint(expr= - m.b4 - m.b13 + m.x62 >= -1)

m.c132 = Constraint(expr= - m.b4 - m.b14 + m.x63 >= -1)

m.c133 = Constraint(expr= - m.b4 - m.b15 + m.x64 >= -1)

m.c134 = Constraint(expr= - m.b5 - m.b16 + m.x65 >= -1)

m.c135 = Constraint(expr= - m.b5 - m.b17 + m.x66 >= -1)

m.c136 = Constraint(expr= - m.b5 - m.b18 + m.x67 >= -1)

m.c137 = Constraint(expr= - m.b5 - m.b19 + m.x68 >= -1)

m.c138 = Constraint(expr= - m.b5 - m.b20 + m.x69 >= -1)

m.c139 = Constraint(expr= - m.b5 - m.b21 + m.x70 >= -1)

m.c140 = Constraint(expr= - m.b6 - m.b22 + m.x71 >= -1)

m.c141 = Constraint(expr= - m.b6 - m.b23 + m.x72 >= -1)

m.c142 = Constraint(expr= - m.b6 - m.b24 + m.x73 >= -1)

m.c143 = Constraint(expr= - m.b6 - m.b25 + m.x74 >= -1)

m.c144 = Constraint(expr= - m.b6 - m.b26 + m.x75 >= -1)

m.c145 = Constraint(expr= - m.b6 - m.b27 + m.x76 >= -1)

m.c146 = Constraint(expr= - m.x28 + m.x116 + m.x134 == 0)

m.c147 = Constraint(expr= - m.x28 + m.x117 + m.x135 == 0)

m.c148 = Constraint(expr= - m.x28 + m.x118 + m.x136 == 0)

m.c149 = Constraint(expr= - m.x28 + m.x119 + m.x137 == 0)

m.c150 = Constraint(expr= - m.x28 + m.x120 + m.x138 == 0)

m.c151 = Constraint(expr= - m.x28 + m.x121 + m.x139 == 0)

m.c152 = Constraint(expr= - m.x29 + m.x122 + m.x140 == 0)

m.c153 = Constraint(expr= - m.x29 + m.x123 + m.x141 == 0)

m.c154 = Constraint(expr= - m.x29 + m.x124 + m.x142 == 0)

m.c155 = Constraint(expr= - m.x29 + m.x125 + m.x143 == 0)

m.c156 = Constraint(expr= - m.x29 + m.x126 + m.x144 == 0)

m.c157 = Constraint(expr= - m.x29 + m.x127 + m.x145 == 0)

m.c158 = Constraint(expr= - m.x30 + m.x128 + m.x146 == 0)

m.c159 = Constraint(expr= - m.x30 + m.x129 + m.x147 == 0)

m.c160 = Constraint(expr= - m.x30 + m.x130 + m.x148 == 0)

m.c161 = Constraint(expr= - m.x30 + m.x131 + m.x149 == 0)

m.c162 = Constraint(expr= - m.x30 + m.x132 + m.x150 == 0)

m.c163 = Constraint(expr= - m.x30 + m.x133 + m.x151 == 0)

m.c164 = Constraint(expr= - 10*m.b10 + m.x116 <= 0)

m.c165 = Constraint(expr= - 10*m.b11 + m.x117 <= 0)

m.c166 = Constraint(expr= - 10*m.b12 + m.x118 <= 0)

m.c167 = Constraint(expr= - 10*m.b13 + m.x119 <= 0)

m.c168 = Constraint(expr= - 10*m.b14 + m.x120 <= 0)

m.c169 = Constraint(expr= - 10*m.b15 + m.x121 <= 0)

m.c170 = Constraint(expr= - 12*m.b16 + m.x122 <= 0)

m.c171 = Constraint(expr= - 12*m.b17 + m.x123 <= 0)

m.c172 = Constraint(expr= - 12*m.b18 + m.x124 <= 0)

m.c173 = Constraint(expr= - 12*m.b19 + m.x125 <= 0)

m.c174 = Constraint(expr= - 12*m.b20 + m.x126 <= 0)

m.c175 = Constraint(expr= - 12*m.b21 + m.x127 <= 0)

m.c176 = Constraint(expr= - 11*m.b22 + m.x128 <= 0)

m.c177 = Constraint(expr= - 11*m.b23 + m.x129 <= 0)

m.c178 = Constraint(expr= - 11*m.b24 + m.x130 <= 0)

m.c179 = Constraint(expr= - 11*m.b25 + m.x131 <= 0)

m.c180 = Constraint(expr= - 11*m.b26 + m.x132 <= 0)

m.c181 = Constraint(expr= - 11*m.b27 + m.x133 <= 0)

m.c182 = Constraint(expr=   10*m.b10 + m.x134 <= 10)

m.c183 = Constraint(expr=   10*m.b11 + m.x135 <= 10)

m.c184 = Constraint(expr=   10*m.b12 + m.x136 <= 10)

m.c185 = Constraint(expr=   10*m.b13 + m.x137 <= 10)

m.c186 = Constraint(expr=   10*m.b14 + m.x138 <= 10)

m.c187 = Constraint(expr=   10*m.b15 + m.x139 <= 10)

m.c188 = Constraint(expr=   12*m.b16 + m.x140 <= 12)

m.c189 = Constraint(expr=   12*m.b17 + m.x141 <= 12)

m.c190 = Constraint(expr=   12*m.b18 + m.x142 <= 12)

m.c191 = Constraint(expr=   12*m.b19 + m.x143 <= 12)

m.c192 = Constraint(expr=   12*m.b20 + m.x144 <= 12)

m.c193 = Constraint(expr=   12*m.b21 + m.x145 <= 12)

m.c194 = Constraint(expr=   11*m.b22 + m.x146 <= 11)

m.c195 = Constraint(expr=   11*m.b23 + m.x147 <= 11)

m.c196 = Constraint(expr=   11*m.b24 + m.x148 <= 11)

m.c197 = Constraint(expr=   11*m.b25 + m.x149 <= 11)

m.c198 = Constraint(expr=   11*m.b26 + m.x150 <= 11)

m.c199 = Constraint(expr=   11*m.b27 + m.x151 <= 11)

m.c200 = Constraint(expr= - m.x31 + m.x80 + m.x98 == 0)

m.c201 = Constraint(expr= - m.x31 + m.x81 + m.x99 == 0)

m.c202 = Constraint(expr= - m.x31 + m.x82 + m.x100 == 0)

m.c203 = Constraint(expr= - m.x31 + m.x83 + m.x101 == 0)

m.c204 = Constraint(expr= - m.x31 + m.x84 + m.x102 == 0)

m.c205 = Constraint(expr= - m.x31 + m.x85 + m.x103 == 0)

m.c206 = Constraint(expr= - m.x32 + m.x86 + m.x104 == 0)

m.c207 = Constraint(expr= - m.x32 + m.x87 + m.x105 == 0)

m.c208 = Constraint(expr= - m.x32 + m.x88 + m.x106 == 0)

m.c209 = Constraint(expr= - m.x32 + m.x89 + m.x107 == 0)

m.c210 = Constraint(expr= - m.x32 + m.x90 + m.x108 == 0)

m.c211 = Constraint(expr= - m.x32 + m.x91 + m.x109 == 0)

m.c212 = Constraint(expr= - m.x33 + m.x92 + m.x110 == 0)

m.c213 = Constraint(expr= - m.x33 + m.x93 + m.x111 == 0)

m.c214 = Constraint(expr= - m.x33 + m.x94 + m.x112 == 0)

m.c215 = Constraint(expr= - m.x33 + m.x95 + m.x113 == 0)

m.c216 = Constraint(expr= - m.x33 + m.x96 + m.x114 == 0)

m.c217 = Constraint(expr= - m.x33 + m.x97 + m.x115 == 0)

m.c218 = Constraint(expr= - 10*m.b10 + m.x80 <= 0)

m.c219 = Constraint(expr= - 10*m.b11 + m.x81 <= 0)

m.c220 = Constraint(expr= - 10*m.b12 + m.x82 <= 0)

m.c221 = Constraint(expr= - 10*m.b13 + m.x83 <= 0)

m.c222 = Constraint(expr= - 10*m.b14 + m.x84 <= 0)

m.c223 = Constraint(expr= - 10*m.b15 + m.x85 <= 0)

m.c224 = Constraint(expr= - 12*m.b16 + m.x86 <= 0)

m.c225 = Constraint(expr= - 12*m.b17 + m.x87 <= 0)

m.c226 = Constraint(expr= - 12*m.b18 + m.x88 <= 0)

m.c227 = Constraint(expr= - 12*m.b19 + m.x89 <= 0)

m.c228 = Constraint(expr= - 12*m.b20 + m.x90 <= 0)

m.c229 = Constraint(expr= - 12*m.b21 + m.x91 <= 0)

m.c230 = Constraint(expr= - 11*m.b22 + m.x92 <= 0)

m.c231 = Constraint(expr= - 11*m.b23 + m.x93 <= 0)

m.c232 = Constraint(expr= - 11*m.b24 + m.x94 <= 0)

m.c233 = Constraint(expr= - 11*m.b25 + m.x95 <= 0)

m.c234 = Constraint(expr= - 11*m.b26 + m.x96 <= 0)

m.c235 = Constraint(expr= - 11*m.b27 + m.x97 <= 0)

m.c236 = Constraint(expr=   10*m.b10 + m.x98 <= 10)

m.c237 = Constraint(expr=   10*m.b11 + m.x99 <= 10)

m.c238 = Constraint(expr=   10*m.b12 + m.x100 <= 10)

m.c239 = Constraint(expr=   10*m.b13 + m.x101 <= 10)

m.c240 = Constraint(expr=   10*m.b14 + m.x102 <= 10)

m.c241 = Constraint(expr=   10*m.b15 + m.x103 <= 10)

m.c242 = Constraint(expr=   12*m.b16 + m.x104 <= 12)

m.c243 = Constraint(expr=   12*m.b17 + m.x105 <= 12)

m.c244 = Constraint(expr=   12*m.b18 + m.x106 <= 12)

m.c245 = Constraint(expr=   12*m.b19 + m.x107 <= 12)

m.c246 = Constraint(expr=   12*m.b20 + m.x108 <= 12)

m.c247 = Constraint(expr=   12*m.b21 + m.x109 <= 12)

m.c248 = Constraint(expr=   11*m.b22 + m.x110 <= 11)

m.c249 = Constraint(expr=   11*m.b23 + m.x111 <= 11)

m.c250 = Constraint(expr=   11*m.b24 + m.x112 <= 11)

m.c251 = Constraint(expr=   11*m.b25 + m.x113 <= 11)

m.c252 = Constraint(expr=   11*m.b26 + m.x114 <= 11)

m.c253 = Constraint(expr=   11*m.b27 + m.x115 <= 11)

m.c254 = Constraint(expr=   m.x77 - 690.72410962302*m.x80 - 1407.02886656603*m.x81 - 79.3201437228845*m.x82
                          - 2.91401731263049*m.x83 - 855.94622404089*m.x84 - 964.816732551601*m.x85 == 0)

m.c255 = Constraint(expr=   m.x78 - 690.72410962302*m.x86 - 1407.02886656603*m.x87 - 79.3201437228845*m.x88
                          - 2.91401731263049*m.x89 - 855.94622404089*m.x90 - 964.816732551601*m.x91 == 0)

m.c256 = Constraint(expr=   m.x79 - 690.72410962302*m.x92 - 1407.02886656603*m.x93 - 79.3201437228845*m.x94
                          - 2.91401731263049*m.x95 - 855.94622404089*m.x96 - 964.816732551601*m.x97 == 0)
