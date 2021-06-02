#  MINLP written by GAMS Convert at 04/21/18 13:52:23
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        167      107       18       42        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        149      133       16        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        528      349      179        0
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
m.x17 = Var(within=Reals,bounds=(320,500),initialize=500)
m.x18 = Var(within=Reals,bounds=(320,500),initialize=500)
m.x19 = Var(within=Reals,bounds=(320,500),initialize=500)
m.x20 = Var(within=Reals,bounds=(380,480),initialize=480)
m.x21 = Var(within=Reals,bounds=(380,480),initialize=480)
m.x22 = Var(within=Reals,bounds=(380,480),initialize=480)
m.x23 = Var(within=Reals,bounds=(360,460),initialize=460)
m.x24 = Var(within=Reals,bounds=(360,460),initialize=460)
m.x25 = Var(within=Reals,bounds=(360,460),initialize=460)
m.x26 = Var(within=Reals,bounds=(360,380),initialize=380)
m.x27 = Var(within=Reals,bounds=(360,380),initialize=380)
m.x28 = Var(within=Reals,bounds=(360,380),initialize=380)
m.x29 = Var(within=Reals,bounds=(320,380),initialize=380)
m.x30 = Var(within=Reals,bounds=(320,380),initialize=380)
m.x31 = Var(within=Reals,bounds=(320,380),initialize=380)
m.x32 = Var(within=Reals,bounds=(290,660),initialize=290)
m.x33 = Var(within=Reals,bounds=(290,660),initialize=290)
m.x34 = Var(within=Reals,bounds=(290,660),initialize=290)
m.x35 = Var(within=Reals,bounds=(0,None),initialize=1080)
m.x36 = Var(within=Reals,bounds=(0,None),initialize=1080)
m.x37 = Var(within=Reals,bounds=(0,None),initialize=400)
m.x38 = Var(within=Reals,bounds=(0,None),initialize=400)
m.x39 = Var(within=Reals,bounds=(0,None),initialize=600)
m.x40 = Var(within=Reals,bounds=(0,None),initialize=600)
m.x41 = Var(within=Reals,bounds=(0,None),initialize=400)
m.x42 = Var(within=Reals,bounds=(0,None),initialize=400)
m.x43 = Var(within=Reals,bounds=(0,None),initialize=720)
m.x44 = Var(within=Reals,bounds=(0,None),initialize=720)
m.x45 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x46 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x47 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x48 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x49 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x50 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x51 = Var(within=Reals,bounds=(10,None),initialize=210)
m.x52 = Var(within=Reals,bounds=(10,None),initialize=210)
m.x53 = Var(within=Reals,bounds=(10,None),initialize=210)
m.x54 = Var(within=Reals,bounds=(10,None),initialize=190)
m.x55 = Var(within=Reals,bounds=(10,None),initialize=190)
m.x56 = Var(within=Reals,bounds=(10,None),initialize=190)
m.x57 = Var(within=Reals,bounds=(10,None),initialize=170)
m.x58 = Var(within=Reals,bounds=(10,None),initialize=170)
m.x59 = Var(within=Reals,bounds=(10,None),initialize=170)
m.x60 = Var(within=Reals,bounds=(10,None),initialize=90)
m.x61 = Var(within=Reals,bounds=(10,None),initialize=90)
m.x62 = Var(within=Reals,bounds=(10,None),initialize=90)
m.x63 = Var(within=Reals,bounds=(10,None),initialize=90)
m.x64 = Var(within=Reals,bounds=(10,None),initialize=90)
m.x65 = Var(within=Reals,bounds=(10,None),initialize=90)
m.x66 = Var(within=Reals,bounds=(10,None),initialize=180)
m.x67 = Var(within=Reals,bounds=(10,None),initialize=160)
m.x68 = Var(within=Reals,bounds=(10,None),initialize=140)
m.x69 = Var(within=Reals,bounds=(10,None),initialize=60)
m.x70 = Var(within=Reals,bounds=(10,None),initialize=60)
m.x71 = Var(within=Reals,bounds=(10,None),initialize=410)
m.x72 = Var(within=Reals,bounds=(0,6),initialize=6)
m.x73 = Var(within=Reals,bounds=(0,6),initialize=6)
m.x74 = Var(within=Reals,bounds=(0,4),initialize=4)
m.x75 = Var(within=Reals,bounds=(0,4),initialize=4)
m.x76 = Var(within=Reals,bounds=(0,6),initialize=6)
m.x77 = Var(within=Reals,bounds=(0,6),initialize=6)
m.x78 = Var(within=Reals,bounds=(0,20),initialize=20)
m.x79 = Var(within=Reals,bounds=(0,20),initialize=20)
m.x80 = Var(within=Reals,bounds=(0,12),initialize=12)
m.x81 = Var(within=Reals,bounds=(0,12),initialize=12)
m.x82 = Var(within=Reals,bounds=(0,18),initialize=18)
m.x83 = Var(within=Reals,bounds=(0,18),initialize=18)
m.x84 = Var(within=Reals,bounds=(0,18),initialize=18)
m.x85 = Var(within=Reals,bounds=(0,18),initialize=18)
m.x86 = Var(within=Reals,bounds=(0,18),initialize=18)
m.x87 = Var(within=Reals,bounds=(0,18),initialize=18)
m.x88 = Var(within=Reals,bounds=(0,18),initialize=18)
m.x89 = Var(within=Reals,bounds=(0,18),initialize=18)
m.x90 = Var(within=Reals,bounds=(0,18),initialize=18)
m.x91 = Var(within=Reals,bounds=(0,18),initialize=18)
m.x92 = Var(within=Reals,bounds=(320,500),initialize=500)
m.x93 = Var(within=Reals,bounds=(320,500),initialize=500)
m.x94 = Var(within=Reals,bounds=(380,480),initialize=480)
m.x95 = Var(within=Reals,bounds=(380,480),initialize=480)
m.x96 = Var(within=Reals,bounds=(360,460),initialize=460)
m.x97 = Var(within=Reals,bounds=(360,460),initialize=460)
m.x98 = Var(within=Reals,bounds=(360,380),initialize=380)
m.x99 = Var(within=Reals,bounds=(360,380),initialize=380)
m.x100 = Var(within=Reals,bounds=(320,380),initialize=380)
m.x101 = Var(within=Reals,bounds=(320,380),initialize=380)
m.x102 = Var(within=Reals,bounds=(290,660),initialize=290)
m.x103 = Var(within=Reals,bounds=(290,660),initialize=290)
m.x104 = Var(within=Reals,bounds=(290,660),initialize=290)
m.x105 = Var(within=Reals,bounds=(290,660),initialize=290)
m.x106 = Var(within=Reals,bounds=(290,660),initialize=290)
m.x107 = Var(within=Reals,bounds=(290,660),initialize=290)
m.x108 = Var(within=Reals,bounds=(290,660),initialize=290)
m.x109 = Var(within=Reals,bounds=(290,660),initialize=290)
m.x110 = Var(within=Reals,bounds=(290,660),initialize=290)
m.x111 = Var(within=Reals,bounds=(290,660),initialize=290)
m.x112 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x113 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x114 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x115 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x116 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x117 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x118 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x119 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x120 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x121 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x122 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x123 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x124 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x125 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x126 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x127 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x128 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x129 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x130 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x131 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x132 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x133 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x134 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x135 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x136 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x137 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x138 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x139 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x140 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x141 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x142 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x143 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x144 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x145 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x146 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x147 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x148 = Var(within=Reals,bounds=(0,None),initialize=0)

m.obj = Objective(expr=1200*(0.01 + m.x128)**0.6 + 1200*(0.01 + m.x129)**0.6 + 1200*(0.01 + m.x130)**0.6 + 1200*(0.01 + 
                       m.x131)**0.6 + 1200*(0.01 + m.x132)**0.6 + 1200*(0.01 + m.x133)**0.6 + 1200*(0.01 + m.x134)**0.6
                        + 1200*(0.01 + m.x135)**0.6 + 1200*(0.01 + m.x136)**0.6 + 1200*(0.01 + m.x137)**0.6 + 1200*(0.01
                        + m.x138)**0.6 + 1200*(0.01 + m.x139)**0.6 + 1200*(0.01 + m.x140)**0.6 + 1200*(0.01 + m.x141)**
                       0.6 + 1200*(0.01 + m.x142)**0.6 + 1200*(0.01 + m.x143)**0.6 + 1200*(0.01 + m.x144)**0.6 + 1200*(
                       0.01 + m.x145)**0.6 + 1200*(0.01 + m.x146)**0.6 + 1200*(0.01 + m.x147)**0.6 + 1200*(0.01 + m.x148
                       )**0.6 + 5500*m.b1 + 5500*m.b2 + 5500*m.b3 + 5500*m.b4 + 5500*m.b5 + 5500*m.b6 + 5500*m.b7
                        + 5500*m.b8 + 5500*m.b9 + 5500*m.b10 + 5500*m.b11 + 5500*m.b12 + 5500*m.b13 + 5500*m.b14
                        + 5500*m.b15 + 5500*m.b16 + 10*m.x45 + 10*m.x46 + 10*m.x47 + 10*m.x48 + 10*m.x49 + 140*m.x50
                       , sense=minimize)

m.c1 = Constraint(expr=   6*m.x17 - 6*m.x18 - m.x35 == 0)

m.c2 = Constraint(expr=   6*m.x18 - 6*m.x19 - m.x36 == 0)

m.c3 = Constraint(expr=   4*m.x20 - 4*m.x21 - m.x37 == 0)

m.c4 = Constraint(expr=   4*m.x21 - 4*m.x22 - m.x38 == 0)

m.c5 = Constraint(expr=   6*m.x23 - 6*m.x24 - m.x39 == 0)

m.c6 = Constraint(expr=   6*m.x24 - 6*m.x25 - m.x40 == 0)

m.c7 = Constraint(expr=   20*m.x26 - 20*m.x27 - m.x41 == 0)

m.c8 = Constraint(expr=   20*m.x27 - 20*m.x28 - m.x42 == 0)

m.c9 = Constraint(expr=   12*m.x29 - 12*m.x30 - m.x43 == 0)

m.c10 = Constraint(expr=   12*m.x30 - 12*m.x31 - m.x44 == 0)

m.c11 = Constraint(expr=   18*m.x32 - 18*m.x33 - m.x35 - m.x37 - m.x39 - m.x41 - m.x43 == 0)

m.c12 = Constraint(expr=   18*m.x33 - 18*m.x34 - m.x36 - m.x38 - m.x40 - m.x42 - m.x44 == 0)

m.c13 = Constraint(expr=   6*m.x19 - m.x45 == 1920)

m.c14 = Constraint(expr=   4*m.x22 - m.x46 == 1520)

m.c15 = Constraint(expr=   6*m.x25 - m.x47 == 2160)

m.c16 = Constraint(expr=   20*m.x28 - m.x48 == 7200)

m.c17 = Constraint(expr=   12*m.x31 - m.x49 == 3840)

m.c18 = Constraint(expr= - m.x35 - m.x36 - m.x45 == -1080)

m.c19 = Constraint(expr= - m.x37 - m.x38 - m.x46 == -400)

m.c20 = Constraint(expr= - m.x39 - m.x40 - m.x47 == -600)

m.c21 = Constraint(expr= - m.x41 - m.x42 - m.x48 == -400)

m.c22 = Constraint(expr= - m.x43 - m.x44 - m.x49 == -720)

m.c23 = Constraint(expr= - 18*m.x32 - m.x50 == -11880)

m.c24 = Constraint(expr= - m.x35 - m.x36 - m.x37 - m.x38 - m.x39 - m.x40 - m.x41 - m.x42 - m.x43 - m.x44 - m.x50
                         == -6660)

m.c25 = Constraint(expr=   m.x17 - m.x18 >= 0)

m.c26 = Constraint(expr=   m.x18 - m.x19 >= 0)

m.c27 = Constraint(expr=   m.x20 - m.x21 >= 0)

m.c28 = Constraint(expr=   m.x21 - m.x22 >= 0)

m.c29 = Constraint(expr=   m.x23 - m.x24 >= 0)

m.c30 = Constraint(expr=   m.x24 - m.x25 >= 0)

m.c31 = Constraint(expr=   m.x26 - m.x27 >= 0)

m.c32 = Constraint(expr=   m.x27 - m.x28 >= 0)

m.c33 = Constraint(expr=   m.x29 - m.x30 >= 0)

m.c34 = Constraint(expr=   m.x30 - m.x31 >= 0)

m.c35 = Constraint(expr=   m.x32 - m.x33 >= 0)

m.c36 = Constraint(expr=   m.x33 - m.x34 >= 0)

m.c37 = Constraint(expr=   m.x19 >= 320)

m.c38 = Constraint(expr=   m.x22 >= 380)

m.c39 = Constraint(expr=   m.x25 >= 360)

m.c40 = Constraint(expr=   m.x28 >= 360)

m.c41 = Constraint(expr=   m.x31 >= 320)

m.c42 = Constraint(expr= - m.x32 >= -660)

m.c43 = Constraint(expr= - m.x17 == -500)

m.c44 = Constraint(expr= - m.x20 == -480)

m.c45 = Constraint(expr= - m.x23 == -460)

m.c46 = Constraint(expr= - m.x26 == -380)

m.c47 = Constraint(expr= - m.x29 == -380)

m.c48 = Constraint(expr= - m.x34 == -290)

m.c49 = Constraint(expr= - m.x72 == -6)

m.c50 = Constraint(expr= - m.x73 == -6)

m.c51 = Constraint(expr= - m.x74 == -4)

m.c52 = Constraint(expr= - m.x75 == -4)

m.c53 = Constraint(expr= - m.x76 == -6)

m.c54 = Constraint(expr= - m.x77 == -6)

m.c55 = Constraint(expr= - m.x78 == -20)

m.c56 = Constraint(expr= - m.x79 == -20)

m.c57 = Constraint(expr= - m.x80 == -12)

m.c58 = Constraint(expr= - m.x81 == -12)

m.c59 = Constraint(expr= - m.x82 - m.x84 - m.x86 - m.x88 - m.x90 == -18)

m.c60 = Constraint(expr= - m.x83 - m.x85 - m.x87 - m.x89 - m.x91 == -18)

m.c61 = Constraint(expr=-m.x72*(m.x17 - m.x92) + m.x35 == 0)

m.c62 = Constraint(expr=-m.x73*(m.x18 - m.x93) + m.x36 == 0)

m.c63 = Constraint(expr=-m.x74*(m.x20 - m.x94) + m.x37 == 0)

m.c64 = Constraint(expr=-m.x75*(m.x21 - m.x95) + m.x38 == 0)

m.c65 = Constraint(expr=-m.x76*(m.x23 - m.x96) + m.x39 == 0)

m.c66 = Constraint(expr=-m.x77*(m.x24 - m.x97) + m.x40 == 0)

m.c67 = Constraint(expr=-m.x78*(m.x26 - m.x98) + m.x41 == 0)

m.c68 = Constraint(expr=-m.x79*(m.x27 - m.x99) + m.x42 == 0)

m.c69 = Constraint(expr=-m.x80*(m.x29 - m.x100) + m.x43 == 0)

m.c70 = Constraint(expr=-m.x81*(m.x30 - m.x101) + m.x44 == 0)

m.c71 = Constraint(expr=-m.x82*(m.x102 - m.x33) + m.x35 == 0)

m.c72 = Constraint(expr=-m.x83*(m.x103 - m.x34) + m.x36 == 0)

m.c73 = Constraint(expr=-m.x84*(m.x104 - m.x33) + m.x37 == 0)

m.c74 = Constraint(expr=-m.x85*(m.x105 - m.x34) + m.x38 == 0)

m.c75 = Constraint(expr=-m.x86*(m.x106 - m.x33) + m.x39 == 0)

m.c76 = Constraint(expr=-m.x87*(m.x107 - m.x34) + m.x40 == 0)

m.c77 = Constraint(expr=-m.x88*(m.x108 - m.x33) + m.x41 == 0)

m.c78 = Constraint(expr=-m.x89*(m.x109 - m.x34) + m.x42 == 0)

m.c79 = Constraint(expr=-m.x90*(m.x110 - m.x33) + m.x43 == 0)

m.c80 = Constraint(expr=-m.x91*(m.x111 - m.x34) + m.x44 == 0)

m.c81 = Constraint(expr=-m.x72*m.x92 + 6*m.x18 == 0)

m.c82 = Constraint(expr=-m.x73*m.x93 + 6*m.x19 == 0)

m.c83 = Constraint(expr=-m.x74*m.x94 + 4*m.x21 == 0)

m.c84 = Constraint(expr=-m.x75*m.x95 + 4*m.x22 == 0)

m.c85 = Constraint(expr=-m.x76*m.x96 + 6*m.x24 == 0)

m.c86 = Constraint(expr=-m.x77*m.x97 + 6*m.x25 == 0)

m.c87 = Constraint(expr=-m.x78*m.x98 + 20*m.x27 == 0)

m.c88 = Constraint(expr=-m.x79*m.x99 + 20*m.x28 == 0)

m.c89 = Constraint(expr=-m.x80*m.x100 + 12*m.x30 == 0)

m.c90 = Constraint(expr=-m.x81*m.x101 + 12*m.x31 == 0)

m.c91 = Constraint(expr=-(m.x82*m.x102 + m.x84*m.x104 + m.x86*m.x106 + m.x88*m.x108 + m.x90*m.x110) + 18*m.x32 == 0)

m.c92 = Constraint(expr=-(m.x83*m.x103 + m.x85*m.x105 + m.x87*m.x107 + m.x89*m.x109 + m.x91*m.x111) + 18*m.x33 == 0)

m.c93 = Constraint(expr=-(m.x51 - m.x52)/log(m.x51/(1e-6 + m.x52)) + m.x112 == 0)

m.c94 = Constraint(expr=-(m.x52 - m.x53)/log(m.x52/(1e-6 + m.x53)) + m.x113 == 0)

m.c95 = Constraint(expr=-(m.x54 - m.x55)/log(m.x54/(1e-6 + m.x55)) + m.x114 == 0)

m.c96 = Constraint(expr=-(m.x55 - m.x56)/log(m.x55/(1e-6 + m.x56)) + m.x115 == 0)

m.c97 = Constraint(expr=-(m.x57 - m.x58)/log(m.x57/(1e-6 + m.x58)) + m.x116 == 0)

m.c98 = Constraint(expr=-(m.x58 - m.x59)/log(m.x58/(1e-6 + m.x59)) + m.x117 == 0)

m.c99 = Constraint(expr=-(m.x60 - m.x61)/log(m.x60/(1e-6 + m.x61)) + m.x118 == 0)

m.c100 = Constraint(expr=-(m.x61 - m.x62)/log(m.x61/(1e-6 + m.x62)) + m.x119 == 0)

m.c101 = Constraint(expr=-(m.x63 - m.x64)/log(m.x63/(1e-6 + m.x64)) + m.x120 == 0)

m.c102 = Constraint(expr=-(m.x64 - m.x65)/log(m.x64/(1e-6 + m.x65)) + m.x121 == 0)

m.c103 = Constraint(expr=-m.x35/(0.01 + m.x112) + m.x128 == 0)

m.c104 = Constraint(expr=-m.x36/(0.01 + m.x113) + m.x129 == 0)

m.c105 = Constraint(expr=-m.x37/(0.01 + m.x114) + m.x131 == 0)

m.c106 = Constraint(expr=-m.x38/(0.01 + m.x115) + m.x132 == 0)

m.c107 = Constraint(expr=-m.x39/(0.01 + m.x116) + m.x134 == 0)

m.c108 = Constraint(expr=-m.x40/(0.01 + m.x117) + m.x135 == 0)

m.c109 = Constraint(expr=-m.x41/(0.01 + m.x118) + m.x137 == 0)

m.c110 = Constraint(expr=-m.x42/(0.01 + m.x119) + m.x138 == 0)

m.c111 = Constraint(expr=-m.x43/(0.01 + m.x120) + m.x140 == 0)

m.c112 = Constraint(expr=-m.x44/(0.01 + m.x121) + m.x141 == 0)

m.c113 = Constraint(expr=-(-20 + m.x66)/log(0.0499999975000001*m.x66) + m.x122 == 0)

m.c114 = Constraint(expr=-(-80 + m.x67)/log(0.01249999984375*m.x67) + m.x123 == 0)

m.c115 = Constraint(expr=-(-60 + m.x68)/log(0.0166666663888889*m.x68) + m.x124 == 0)

m.c116 = Constraint(expr=-(-60 + m.x69)/log(0.0166666663888889*m.x69) + m.x125 == 0)

m.c117 = Constraint(expr=-(-20 + m.x70)/log(0.0499999975000001*m.x70) + m.x126 == 0)

m.c118 = Constraint(expr=-(-40 + m.x71)/log(0.024999999375*m.x71) + m.x127 == 0)

m.c119 = Constraint(expr=-m.x45/(0.01 + m.x122) + m.x143 == 0)

m.c120 = Constraint(expr=-m.x46/(0.01 + m.x123) + m.x144 == 0)

m.c121 = Constraint(expr=-m.x47/(0.01 + m.x124) + m.x145 == 0)

m.c122 = Constraint(expr=-m.x48/(0.01 + m.x125) + m.x146 == 0)

m.c123 = Constraint(expr=-m.x49/(0.01 + m.x126) + m.x147 == 0)

m.c124 = Constraint(expr=-m.x50/(0.01 + m.x127) + m.x148 == 0)

m.c125 = Constraint(expr= - 1080*m.b1 + m.x35 <= 0)

m.c126 = Constraint(expr= - 1080*m.b2 + m.x36 <= 0)

m.c127 = Constraint(expr= - 400*m.b3 + m.x37 <= 0)

m.c128 = Constraint(expr= - 400*m.b4 + m.x38 <= 0)

m.c129 = Constraint(expr= - 600*m.b5 + m.x39 <= 0)

m.c130 = Constraint(expr= - 600*m.b6 + m.x40 <= 0)

m.c131 = Constraint(expr= - 400*m.b7 + m.x41 <= 0)

m.c132 = Constraint(expr= - 400*m.b8 + m.x42 <= 0)

m.c133 = Constraint(expr= - 720*m.b9 + m.x43 <= 0)

m.c134 = Constraint(expr= - 720*m.b10 + m.x44 <= 0)

m.c135 = Constraint(expr= - 6660*m.b16 + m.x50 <= 0)

m.c136 = Constraint(expr= - 1080*m.b11 + m.x45 <= 0)

m.c137 = Constraint(expr= - 400*m.b12 + m.x46 <= 0)

m.c138 = Constraint(expr= - 600*m.b13 + m.x47 <= 0)

m.c139 = Constraint(expr= - 400*m.b14 + m.x48 <= 0)

m.c140 = Constraint(expr= - 720*m.b15 + m.x49 <= 0)

m.c141 = Constraint(expr=   340*m.b1 - m.x17 + m.x32 + m.x51 <= 340)

m.c142 = Constraint(expr=   340*m.b2 - m.x18 + m.x33 + m.x52 <= 340)

m.c143 = Constraint(expr=   280*m.b3 - m.x20 + m.x32 + m.x54 <= 280)

m.c144 = Constraint(expr=   280*m.b4 - m.x21 + m.x33 + m.x55 <= 280)

m.c145 = Constraint(expr=   300*m.b5 - m.x23 + m.x32 + m.x57 <= 300)

m.c146 = Constraint(expr=   300*m.b6 - m.x24 + m.x33 + m.x58 <= 300)

m.c147 = Constraint(expr=   300*m.b7 - m.x26 + m.x32 + m.x60 <= 300)

m.c148 = Constraint(expr=   300*m.b8 - m.x27 + m.x33 + m.x61 <= 300)

m.c149 = Constraint(expr=   340*m.b9 - m.x29 + m.x32 + m.x63 <= 340)

m.c150 = Constraint(expr=   340*m.b10 - m.x30 + m.x33 + m.x64 <= 340)

m.c151 = Constraint(expr=   340*m.b1 - m.x18 + m.x33 + m.x52 <= 340)

m.c152 = Constraint(expr=   340*m.b2 - m.x19 + m.x34 + m.x53 <= 340)

m.c153 = Constraint(expr=   280*m.b3 - m.x21 + m.x33 + m.x55 <= 280)

m.c154 = Constraint(expr=   280*m.b4 - m.x22 + m.x34 + m.x56 <= 280)

m.c155 = Constraint(expr=   300*m.b5 - m.x24 + m.x33 + m.x58 <= 300)

m.c156 = Constraint(expr=   300*m.b6 - m.x25 + m.x34 + m.x59 <= 300)

m.c157 = Constraint(expr=   300*m.b7 - m.x27 + m.x33 + m.x61 <= 300)

m.c158 = Constraint(expr=   300*m.b8 - m.x28 + m.x34 + m.x62 <= 300)

m.c159 = Constraint(expr=   340*m.b9 - m.x30 + m.x33 + m.x64 <= 340)

m.c160 = Constraint(expr=   340*m.b10 - m.x31 + m.x34 + m.x65 <= 340)

m.c161 = Constraint(expr= - m.x19 + m.x66 <= -320)

m.c162 = Constraint(expr= - m.x22 + m.x67 <= -320)

m.c163 = Constraint(expr= - m.x25 + m.x68 <= -320)

m.c164 = Constraint(expr= - m.x28 + m.x69 <= -320)

m.c165 = Constraint(expr= - m.x31 + m.x70 <= -320)

m.c166 = Constraint(expr=   m.x32 + m.x71 <= 700)
