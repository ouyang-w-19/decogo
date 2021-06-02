#  NLP written by GAMS Convert at 04/21/18 13:55:04
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        191       55      136        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        170      170        0        0        0        0        0        0
#  FX      6        6        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1494      354     1140        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(1000,1000),initialize=1000)
m.x2 = Var(within=Reals,bounds=(1000,1000),initialize=1000)
m.x3 = Var(within=Reals,bounds=(0,2000),initialize=1100.750712)
m.x4 = Var(within=Reals,bounds=(0,2000),initialize=602.275808)
m.x5 = Var(within=Reals,bounds=(0,2000),initialize=584.424234)
m.x6 = Var(within=Reals,bounds=(0,2000),initialize=448.105734)
m.x7 = Var(within=Reals,bounds=(0,2000),initialize=699.661008)
m.x8 = Var(within=Reals,bounds=(0,2000),initialize=1712.540694)
m.x9 = Var(within=Reals,bounds=(0,2000),initialize=134.227446)
m.x10 = Var(within=Reals,bounds=(0,2000),initialize=1000.421338)
m.x11 = Var(within=Reals,bounds=(0,2000),initialize=1996.235254)
m.x12 = Var(within=Reals,bounds=(0,2000),initialize=1157.466756)
m.x13 = Var(within=Reals,bounds=(0,2000),initialize=1982.266078)
m.x14 = Var(within=Reals,bounds=(0,2000),initialize=1524.500934)
m.x15 = Var(within=Reals,bounds=(0,2000),initialize=261.384966)
m.x16 = Var(within=Reals,bounds=(0,2000),initialize=1279.437518)
m.x17 = Var(within=Reals,bounds=(0,2000),initialize=319.035728)
m.x18 = Var(within=Reals,bounds=(0,2000),initialize=500.161066)
m.x19 = Var(within=Reals,bounds=(1500,1500),initialize=1500)
m.x20 = Var(within=Reals,bounds=(2000,2000),initialize=2000)
m.x21 = Var(within=Reals,bounds=(0,2000),initialize=719.400532)
m.x22 = Var(within=Reals,bounds=(0,2000),initialize=702.882736)
m.x23 = Var(within=Reals,bounds=(0,2000),initialize=262.98318)
m.x24 = Var(within=Reals,bounds=(0,2000),initialize=300.203576)
m.x25 = Var(within=Reals,bounds=(0,2000),initialize=1178.2273)
m.x26 = Var(within=Reals,bounds=(0,2000),initialize=1661.785624)
m.x27 = Var(within=Reals,bounds=(0,2000),initialize=461.631476)
m.x28 = Var(within=Reals,bounds=(0,2000),initialize=1331.46892)
m.x29 = Var(within=Reals,bounds=(0,2000),initialize=1551.715212)
m.x30 = Var(within=Reals,bounds=(0,2000),initialize=607.316954)
m.x31 = Var(within=Reals,bounds=(0,2000),initialize=220.984582)
m.x32 = Var(within=Reals,bounds=(0,2000),initialize=1004.769732)
m.x33 = Var(within=Reals,bounds=(0,2000),initialize=320.345524)
m.x34 = Var(within=Reals,bounds=(0,2000),initialize=1744.924622)
m.x35 = Var(within=Reals,bounds=(0,2000),initialize=530.22909)
m.x36 = Var(within=Reals,bounds=(0,2000),initialize=571.628644)
m.x37 = Var(within=Reals,bounds=(0,2000),initialize=1187.911844)
m.x38 = Var(within=Reals,bounds=(0,2000),initialize=1445.438142)
m.x39 = Var(within=Reals,bounds=(2000,2000),initialize=2000)
m.x40 = Var(within=Reals,bounds=(1000,1000),initialize=1000)
m.x41 = Var(within=Reals,bounds=(0.1,None),initialize=100)
m.x42 = Var(within=Reals,bounds=(0.1,None),initialize=100)
m.x43 = Var(within=Reals,bounds=(0.1,None),initialize=100)
m.x44 = Var(within=Reals,bounds=(0.1,None),initialize=100)
m.x45 = Var(within=Reals,bounds=(0.1,None),initialize=100)
m.x46 = Var(within=Reals,bounds=(0.1,None),initialize=100)
m.x47 = Var(within=Reals,bounds=(0.1,None),initialize=100)
m.x48 = Var(within=Reals,bounds=(0.1,None),initialize=100)
m.x49 = Var(within=Reals,bounds=(0.1,None),initialize=100)
m.x50 = Var(within=Reals,bounds=(0.1,None),initialize=100)
m.x51 = Var(within=Reals,bounds=(0.1,None),initialize=100)
m.x52 = Var(within=Reals,bounds=(0.1,None),initialize=100)
m.x53 = Var(within=Reals,bounds=(0.1,None),initialize=100)
m.x54 = Var(within=Reals,bounds=(0.1,None),initialize=100)
m.x55 = Var(within=Reals,bounds=(0.1,None),initialize=100)
m.x56 = Var(within=Reals,bounds=(0.1,None),initialize=100)
m.x57 = Var(within=Reals,bounds=(0.1,None),initialize=100)
m.x58 = Var(within=Reals,bounds=(0.1,None),initialize=100)
m.x59 = Var(within=Reals,bounds=(0.1,None),initialize=100)
m.x60 = Var(within=Reals,bounds=(0.1,None),initialize=100)
m.x61 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x62 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x63 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x64 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x65 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x66 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x67 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x68 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x69 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x70 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x71 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x72 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x73 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x74 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x75 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x76 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x77 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x78 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x79 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x80 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x81 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x82 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x83 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x84 = Var(within=Reals,bounds=(0,None),initialize=0)
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
m.x149 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x150 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x151 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x152 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x153 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x154 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x155 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x156 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x157 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x158 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x159 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x160 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x161 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x162 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x163 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x164 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x165 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x166 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x167 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x168 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x169 = Var(within=Reals,bounds=(0,None),initialize=0)

m.obj = Objective(expr=   m.x61 + m.x62 + m.x63 + m.x64 + m.x65 + m.x66 + m.x67 + m.x68 + m.x69 + m.x70 + m.x71 + m.x72
                        + m.x73 + m.x74 + m.x75 + m.x76 + m.x77 + m.x78 + m.x79 + m.x80 + m.x81 + m.x82 + m.x83 + m.x84
                        + m.x85 + m.x86 + m.x87 + m.x88 + m.x89 + m.x90 + m.x91 + m.x92 + m.x93 + m.x94 + m.x95 + m.x96
                        + m.x97 + m.x98 + m.x99 + m.x100 + m.x101 + m.x102 + m.x103 + m.x104 + m.x105 + m.x106 + m.x107
                        + m.x108 + m.x109 + m.x110 + m.x111 + m.x112 + m.x113 + m.x114 + m.x115 + m.x116 + m.x117
                        + m.x118 + m.x119 + m.x120 + m.x121 + m.x122 + m.x123 + m.x124 + m.x125 + m.x126 + m.x127
                        + m.x128 + m.x129 + m.x130 + m.x131 + m.x132 + m.x133 + m.x134 + m.x135 + m.x136 + m.x137
                        + m.x138 + m.x139 + m.x140 + m.x141 + m.x142 + m.x143 + m.x144 + m.x145 + m.x146 + m.x147
                        + m.x148 + m.x149 + m.x150 + m.x151 + m.x152 + m.x153 + m.x154 + m.x155 + m.x156 + m.x157
                        + m.x158 + m.x159 + m.x160 + m.x161 + m.x162 + m.x163 + m.x164 + m.x165 + m.x166 + m.x167
                        + m.x168 + 100*m.x169, sense=minimize)

m.c2 = Constraint(expr=(m.x1 - m.x3)**2 + (m.x2 - m.x4)**2 - (m.x41 + m.x42)**2 - m.x61 + m.x115 == 0)

m.c3 = Constraint(expr=(m.x1 - m.x5)**2 + (m.x2 - m.x6)**2 - (m.x41 + m.x43)**2 - m.x62 + m.x116 == 0)

m.c4 = Constraint(expr=(m.x1 - m.x7)**2 + (m.x2 - m.x8)**2 - (m.x41 + m.x44)**2 - m.x63 + m.x117 == 0)

m.c5 = Constraint(expr=(m.x1 - m.x11)**2 + (m.x2 - m.x12)**2 - (m.x41 + m.x46)**2 - m.x64 + m.x118 == 0)

m.c6 = Constraint(expr=(m.x1 - m.x13)**2 + (m.x2 - m.x14)**2 - (m.x41 + m.x47)**2 - m.x65 + m.x119 == 0)

m.c7 = Constraint(expr=(m.x1 - m.x15)**2 + (m.x2 - m.x16)**2 - (m.x41 + m.x48)**2 - m.x66 + m.x120 == 0)

m.c8 = Constraint(expr=(m.x1 - m.x19)**2 + (m.x2 - m.x20)**2 - (m.x41 + m.x50)**2 - m.x67 + m.x121 == 0)

m.c9 = Constraint(expr=(m.x1 - m.x23)**2 + (m.x2 - m.x24)**2 - (m.x41 + m.x52)**2 - m.x68 + m.x122 == 0)

m.c10 = Constraint(expr=(m.x1 - m.x39)**2 + (m.x2 - m.x40)**2 - (m.x41 + m.x60)**2 - m.x69 + m.x123 == 0)

m.c11 = Constraint(expr=(m.x3 - m.x5)**2 + (m.x4 - m.x6)**2 - (m.x42 + m.x43)**2 - m.x70 + m.x124 == 0)

m.c12 = Constraint(expr=(m.x3 - m.x7)**2 + (m.x4 - m.x8)**2 - (m.x42 + m.x44)**2 - m.x71 + m.x125 == 0)

m.c13 = Constraint(expr=(m.x5 - m.x7)**2 + (m.x6 - m.x8)**2 - (m.x43 + m.x44)**2 - m.x72 + m.x126 == 0)

m.c14 = Constraint(expr=(m.x5 - m.x9)**2 + (m.x6 - m.x10)**2 - (m.x43 + m.x45)**2 - m.x73 + m.x127 == 0)

m.c15 = Constraint(expr=(m.x5 - m.x15)**2 + (m.x6 - m.x16)**2 - (m.x43 + m.x48)**2 - m.x74 + m.x128 == 0)

m.c16 = Constraint(expr=(m.x7 - m.x9)**2 + (m.x8 - m.x10)**2 - (m.x44 + m.x45)**2 - m.x75 + m.x129 == 0)

m.c17 = Constraint(expr=(m.x7 - m.x11)**2 + (m.x8 - m.x12)**2 - (m.x44 + m.x46)**2 - m.x76 + m.x130 == 0)

m.c18 = Constraint(expr=(m.x9 - m.x11)**2 + (m.x10 - m.x12)**2 - (m.x45 + m.x46)**2 - m.x77 + m.x131 == 0)

m.c19 = Constraint(expr=(m.x9 - m.x13)**2 + (m.x10 - m.x14)**2 - (m.x45 + m.x47)**2 - m.x78 + m.x132 == 0)

m.c20 = Constraint(expr=(m.x9 - m.x15)**2 + (m.x10 - m.x16)**2 - (m.x45 + m.x48)**2 - m.x79 + m.x133 == 0)

m.c21 = Constraint(expr=(m.x11 - m.x13)**2 + (m.x12 - m.x14)**2 - (m.x46 + m.x47)**2 - m.x80 + m.x134 == 0)

m.c22 = Constraint(expr=(m.x13 - m.x15)**2 + (m.x14 - m.x16)**2 - (m.x47 + m.x48)**2 - m.x81 + m.x135 == 0)

m.c23 = Constraint(expr=(m.x13 - m.x17)**2 + (m.x14 - m.x18)**2 - (m.x47 + m.x49)**2 - m.x82 + m.x136 == 0)

m.c24 = Constraint(expr=(m.x13 - m.x21)**2 + (m.x14 - m.x22)**2 - (m.x47 + m.x51)**2 - m.x83 + m.x137 == 0)

m.c25 = Constraint(expr=(m.x13 - m.x23)**2 + (m.x14 - m.x24)**2 - (m.x47 + m.x52)**2 - m.x84 + m.x138 == 0)

m.c26 = Constraint(expr=(m.x15 - m.x17)**2 + (m.x16 - m.x18)**2 - (m.x48 + m.x49)**2 - m.x85 + m.x139 == 0)

m.c27 = Constraint(expr=(m.x15 - m.x19)**2 + (m.x16 - m.x20)**2 - (m.x48 + m.x50)**2 - m.x86 + m.x140 == 0)

m.c28 = Constraint(expr=(m.x17 - m.x19)**2 + (m.x18 - m.x20)**2 - (m.x49 + m.x50)**2 - m.x87 + m.x141 == 0)

m.c29 = Constraint(expr=(m.x17 - m.x21)**2 + (m.x18 - m.x22)**2 - (m.x49 + m.x51)**2 - m.x88 + m.x142 == 0)

m.c30 = Constraint(expr=(m.x19 - m.x21)**2 + (m.x20 - m.x22)**2 - (m.x50 + m.x51)**2 - m.x89 + m.x143 == 0)

m.c31 = Constraint(expr=(m.x19 - m.x23)**2 + (m.x20 - m.x24)**2 - (m.x50 + m.x52)**2 - m.x90 + m.x144 == 0)

m.c32 = Constraint(expr=(m.x19 - m.x25)**2 + (m.x20 - m.x26)**2 - (m.x50 + m.x53)**2 - m.x91 + m.x145 == 0)

m.c33 = Constraint(expr=(m.x19 - m.x27)**2 + (m.x20 - m.x28)**2 - (m.x50 + m.x54)**2 - m.x92 + m.x146 == 0)

m.c34 = Constraint(expr=(m.x19 - m.x29)**2 + (m.x20 - m.x30)**2 - (m.x50 + m.x55)**2 - m.x93 + m.x147 == 0)

m.c35 = Constraint(expr=(m.x19 - m.x31)**2 + (m.x20 - m.x32)**2 - (m.x50 + m.x56)**2 - m.x94 + m.x148 == 0)

m.c36 = Constraint(expr=(m.x19 - m.x37)**2 + (m.x20 - m.x38)**2 - (m.x50 + m.x59)**2 - m.x95 + m.x149 == 0)

m.c37 = Constraint(expr=(m.x19 - m.x39)**2 + (m.x20 - m.x40)**2 - (m.x50 + m.x60)**2 - m.x96 + m.x150 == 0)

m.c38 = Constraint(expr=(m.x21 - m.x23)**2 + (m.x22 - m.x24)**2 - (m.x51 + m.x52)**2 - m.x97 + m.x151 == 0)

m.c39 = Constraint(expr=(m.x23 - m.x25)**2 + (m.x24 - m.x26)**2 - (m.x52 + m.x53)**2 - m.x98 + m.x152 == 0)

m.c40 = Constraint(expr=(m.x23 - m.x27)**2 + (m.x24 - m.x28)**2 - (m.x52 + m.x54)**2 - m.x99 + m.x153 == 0)

m.c41 = Constraint(expr=(m.x23 - m.x29)**2 + (m.x24 - m.x30)**2 - (m.x52 + m.x55)**2 - m.x100 + m.x154 == 0)

m.c42 = Constraint(expr=(m.x23 - m.x33)**2 + (m.x24 - m.x34)**2 - (m.x52 + m.x57)**2 - m.x101 + m.x155 == 0)

m.c43 = Constraint(expr=(m.x23 - m.x35)**2 + (m.x24 - m.x36)**2 - (m.x52 + m.x58)**2 - m.x102 + m.x156 == 0)

m.c44 = Constraint(expr=(m.x23 - m.x39)**2 + (m.x24 - m.x40)**2 - (m.x52 + m.x60)**2 - m.x103 + m.x157 == 0)

m.c45 = Constraint(expr=(m.x25 - m.x27)**2 + (m.x26 - m.x28)**2 - (m.x53 + m.x54)**2 - m.x104 + m.x158 == 0)

m.c46 = Constraint(expr=(m.x27 - m.x29)**2 + (m.x28 - m.x30)**2 - (m.x54 + m.x55)**2 - m.x105 + m.x159 == 0)

m.c47 = Constraint(expr=(m.x29 - m.x31)**2 + (m.x30 - m.x32)**2 - (m.x55 + m.x56)**2 - m.x106 + m.x160 == 0)

m.c48 = Constraint(expr=(m.x29 - m.x33)**2 + (m.x30 - m.x34)**2 - (m.x55 + m.x57)**2 - m.x107 + m.x161 == 0)

m.c49 = Constraint(expr=(m.x31 - m.x33)**2 + (m.x32 - m.x34)**2 - (m.x56 + m.x57)**2 - m.x108 + m.x162 == 0)

m.c50 = Constraint(expr=(m.x31 - m.x35)**2 + (m.x32 - m.x36)**2 - (m.x56 + m.x58)**2 - m.x109 + m.x163 == 0)

m.c51 = Constraint(expr=(m.x31 - m.x37)**2 + (m.x32 - m.x38)**2 - (m.x56 + m.x59)**2 - m.x110 + m.x164 == 0)

m.c52 = Constraint(expr=(m.x33 - m.x35)**2 + (m.x34 - m.x36)**2 - (m.x57 + m.x58)**2 - m.x111 + m.x165 == 0)

m.c53 = Constraint(expr=(m.x35 - m.x37)**2 + (m.x36 - m.x38)**2 - (m.x58 + m.x59)**2 - m.x112 + m.x166 == 0)

m.c54 = Constraint(expr=(m.x35 - m.x39)**2 + (m.x36 - m.x40)**2 - (m.x58 + m.x60)**2 - m.x113 + m.x167 == 0)

m.c55 = Constraint(expr=(m.x37 - m.x39)**2 + (m.x38 - m.x40)**2 - (m.x59 + m.x60)**2 - m.x114 + m.x168 == 0)

m.c56 = Constraint(expr=(m.x1 - m.x9)**2 + (m.x2 - m.x10)**2 - (m.x41 + m.x45)**2 + m.x169 >= 0)

m.c57 = Constraint(expr=(m.x1 - m.x17)**2 + (m.x2 - m.x18)**2 - (m.x41 + m.x49)**2 + m.x169 >= 0)

m.c58 = Constraint(expr=(m.x1 - m.x21)**2 + (m.x2 - m.x22)**2 - (m.x41 + m.x51)**2 + m.x169 >= 0)

m.c59 = Constraint(expr=(m.x1 - m.x25)**2 + (m.x2 - m.x26)**2 - (m.x41 + m.x53)**2 + m.x169 >= 0)

m.c60 = Constraint(expr=(m.x1 - m.x27)**2 + (m.x2 - m.x28)**2 - (m.x41 + m.x54)**2 + m.x169 >= 0)

m.c61 = Constraint(expr=(m.x1 - m.x29)**2 + (m.x2 - m.x30)**2 - (m.x41 + m.x55)**2 + m.x169 >= 0)

m.c62 = Constraint(expr=(m.x1 - m.x31)**2 + (m.x2 - m.x32)**2 - (m.x41 + m.x56)**2 + m.x169 >= 0)

m.c63 = Constraint(expr=(m.x1 - m.x33)**2 + (m.x2 - m.x34)**2 - (m.x41 + m.x57)**2 + m.x169 >= 0)

m.c64 = Constraint(expr=(m.x1 - m.x35)**2 + (m.x2 - m.x36)**2 - (m.x41 + m.x58)**2 + m.x169 >= 0)

m.c65 = Constraint(expr=(m.x1 - m.x37)**2 + (m.x2 - m.x38)**2 - (m.x41 + m.x59)**2 + m.x169 >= 0)

m.c66 = Constraint(expr=(m.x3 - m.x9)**2 + (m.x4 - m.x10)**2 - (m.x42 + m.x45)**2 + m.x169 >= 0)

m.c67 = Constraint(expr=(m.x3 - m.x11)**2 + (m.x4 - m.x12)**2 - (m.x42 + m.x46)**2 + m.x169 >= 0)

m.c68 = Constraint(expr=(m.x3 - m.x13)**2 + (m.x4 - m.x14)**2 - (m.x42 + m.x47)**2 + m.x169 >= 0)

m.c69 = Constraint(expr=(m.x3 - m.x15)**2 + (m.x4 - m.x16)**2 - (m.x42 + m.x48)**2 + m.x169 >= 0)

m.c70 = Constraint(expr=(m.x3 - m.x17)**2 + (m.x4 - m.x18)**2 - (m.x42 + m.x49)**2 + m.x169 >= 0)

m.c71 = Constraint(expr=(m.x3 - m.x19)**2 + (m.x4 - m.x20)**2 - (m.x42 + m.x50)**2 + m.x169 >= 0)

m.c72 = Constraint(expr=(m.x3 - m.x21)**2 + (m.x4 - m.x22)**2 - (m.x42 + m.x51)**2 + m.x169 >= 0)

m.c73 = Constraint(expr=(m.x3 - m.x23)**2 + (m.x4 - m.x24)**2 - (m.x42 + m.x52)**2 + m.x169 >= 0)

m.c74 = Constraint(expr=(m.x3 - m.x25)**2 + (m.x4 - m.x26)**2 - (m.x42 + m.x53)**2 + m.x169 >= 0)

m.c75 = Constraint(expr=(m.x3 - m.x27)**2 + (m.x4 - m.x28)**2 - (m.x42 + m.x54)**2 + m.x169 >= 0)

m.c76 = Constraint(expr=(m.x3 - m.x29)**2 + (m.x4 - m.x30)**2 - (m.x42 + m.x55)**2 + m.x169 >= 0)

m.c77 = Constraint(expr=(m.x3 - m.x31)**2 + (m.x4 - m.x32)**2 - (m.x42 + m.x56)**2 + m.x169 >= 0)

m.c78 = Constraint(expr=(m.x3 - m.x33)**2 + (m.x4 - m.x34)**2 - (m.x42 + m.x57)**2 + m.x169 >= 0)

m.c79 = Constraint(expr=(m.x3 - m.x35)**2 + (m.x4 - m.x36)**2 - (m.x42 + m.x58)**2 + m.x169 >= 0)

m.c80 = Constraint(expr=(m.x3 - m.x37)**2 + (m.x4 - m.x38)**2 - (m.x42 + m.x59)**2 + m.x169 >= 0)

m.c81 = Constraint(expr=(m.x3 - m.x39)**2 + (m.x4 - m.x40)**2 - (m.x42 + m.x60)**2 + m.x169 >= 0)

m.c82 = Constraint(expr=(m.x5 - m.x11)**2 + (m.x6 - m.x12)**2 - (m.x43 + m.x46)**2 + m.x169 >= 0)

m.c83 = Constraint(expr=(m.x5 - m.x13)**2 + (m.x6 - m.x14)**2 - (m.x43 + m.x47)**2 + m.x169 >= 0)

m.c84 = Constraint(expr=(m.x5 - m.x17)**2 + (m.x6 - m.x18)**2 - (m.x43 + m.x49)**2 + m.x169 >= 0)

m.c85 = Constraint(expr=(m.x5 - m.x19)**2 + (m.x6 - m.x20)**2 - (m.x43 + m.x50)**2 + m.x169 >= 0)

m.c86 = Constraint(expr=(m.x5 - m.x21)**2 + (m.x6 - m.x22)**2 - (m.x43 + m.x51)**2 + m.x169 >= 0)

m.c87 = Constraint(expr=(m.x5 - m.x23)**2 + (m.x6 - m.x24)**2 - (m.x43 + m.x52)**2 + m.x169 >= 0)

m.c88 = Constraint(expr=(m.x5 - m.x25)**2 + (m.x6 - m.x26)**2 - (m.x43 + m.x53)**2 + m.x169 >= 0)

m.c89 = Constraint(expr=(m.x5 - m.x27)**2 + (m.x6 - m.x28)**2 - (m.x43 + m.x54)**2 + m.x169 >= 0)

m.c90 = Constraint(expr=(m.x5 - m.x29)**2 + (m.x6 - m.x30)**2 - (m.x43 + m.x55)**2 + m.x169 >= 0)

m.c91 = Constraint(expr=(m.x5 - m.x31)**2 + (m.x6 - m.x32)**2 - (m.x43 + m.x56)**2 + m.x169 >= 0)

m.c92 = Constraint(expr=(m.x5 - m.x33)**2 + (m.x6 - m.x34)**2 - (m.x43 + m.x57)**2 + m.x169 >= 0)

m.c93 = Constraint(expr=(m.x5 - m.x35)**2 + (m.x6 - m.x36)**2 - (m.x43 + m.x58)**2 + m.x169 >= 0)

m.c94 = Constraint(expr=(m.x5 - m.x37)**2 + (m.x6 - m.x38)**2 - (m.x43 + m.x59)**2 + m.x169 >= 0)

m.c95 = Constraint(expr=(m.x5 - m.x39)**2 + (m.x6 - m.x40)**2 - (m.x43 + m.x60)**2 + m.x169 >= 0)

m.c96 = Constraint(expr=(m.x7 - m.x13)**2 + (m.x8 - m.x14)**2 - (m.x44 + m.x47)**2 + m.x169 >= 0)

m.c97 = Constraint(expr=(m.x7 - m.x15)**2 + (m.x8 - m.x16)**2 - (m.x44 + m.x48)**2 + m.x169 >= 0)

m.c98 = Constraint(expr=(m.x7 - m.x17)**2 + (m.x8 - m.x18)**2 - (m.x44 + m.x49)**2 + m.x169 >= 0)

m.c99 = Constraint(expr=(m.x7 - m.x19)**2 + (m.x8 - m.x20)**2 - (m.x44 + m.x50)**2 + m.x169 >= 0)

m.c100 = Constraint(expr=(m.x7 - m.x21)**2 + (m.x8 - m.x22)**2 - (m.x44 + m.x51)**2 + m.x169 >= 0)

m.c101 = Constraint(expr=(m.x7 - m.x23)**2 + (m.x8 - m.x24)**2 - (m.x44 + m.x52)**2 + m.x169 >= 0)

m.c102 = Constraint(expr=(m.x7 - m.x25)**2 + (m.x8 - m.x26)**2 - (m.x44 + m.x53)**2 + m.x169 >= 0)

m.c103 = Constraint(expr=(m.x7 - m.x27)**2 + (m.x8 - m.x28)**2 - (m.x44 + m.x54)**2 + m.x169 >= 0)

m.c104 = Constraint(expr=(m.x7 - m.x29)**2 + (m.x8 - m.x30)**2 - (m.x44 + m.x55)**2 + m.x169 >= 0)

m.c105 = Constraint(expr=(m.x7 - m.x31)**2 + (m.x8 - m.x32)**2 - (m.x44 + m.x56)**2 + m.x169 >= 0)

m.c106 = Constraint(expr=(m.x7 - m.x33)**2 + (m.x8 - m.x34)**2 - (m.x44 + m.x57)**2 + m.x169 >= 0)

m.c107 = Constraint(expr=(m.x7 - m.x35)**2 + (m.x8 - m.x36)**2 - (m.x44 + m.x58)**2 + m.x169 >= 0)

m.c108 = Constraint(expr=(m.x7 - m.x37)**2 + (m.x8 - m.x38)**2 - (m.x44 + m.x59)**2 + m.x169 >= 0)

m.c109 = Constraint(expr=(m.x7 - m.x39)**2 + (m.x8 - m.x40)**2 - (m.x44 + m.x60)**2 + m.x169 >= 0)

m.c110 = Constraint(expr=(m.x9 - m.x17)**2 + (m.x10 - m.x18)**2 - (m.x45 + m.x49)**2 + m.x169 >= 0)

m.c111 = Constraint(expr=(m.x9 - m.x19)**2 + (m.x10 - m.x20)**2 - (m.x45 + m.x50)**2 + m.x169 >= 0)

m.c112 = Constraint(expr=(m.x9 - m.x21)**2 + (m.x10 - m.x22)**2 - (m.x45 + m.x51)**2 + m.x169 >= 0)

m.c113 = Constraint(expr=(m.x9 - m.x23)**2 + (m.x10 - m.x24)**2 - (m.x45 + m.x52)**2 + m.x169 >= 0)

m.c114 = Constraint(expr=(m.x9 - m.x25)**2 + (m.x10 - m.x26)**2 - (m.x45 + m.x53)**2 + m.x169 >= 0)

m.c115 = Constraint(expr=(m.x9 - m.x27)**2 + (m.x10 - m.x28)**2 - (m.x45 + m.x54)**2 + m.x169 >= 0)

m.c116 = Constraint(expr=(m.x9 - m.x29)**2 + (m.x10 - m.x30)**2 - (m.x45 + m.x55)**2 + m.x169 >= 0)

m.c117 = Constraint(expr=(m.x9 - m.x31)**2 + (m.x10 - m.x32)**2 - (m.x45 + m.x56)**2 + m.x169 >= 0)

m.c118 = Constraint(expr=(m.x9 - m.x33)**2 + (m.x10 - m.x34)**2 - (m.x45 + m.x57)**2 + m.x169 >= 0)

m.c119 = Constraint(expr=(m.x9 - m.x35)**2 + (m.x10 - m.x36)**2 - (m.x45 + m.x58)**2 + m.x169 >= 0)

m.c120 = Constraint(expr=(m.x9 - m.x37)**2 + (m.x10 - m.x38)**2 - (m.x45 + m.x59)**2 + m.x169 >= 0)

m.c121 = Constraint(expr=(m.x9 - m.x39)**2 + (m.x10 - m.x40)**2 - (m.x45 + m.x60)**2 + m.x169 >= 0)

m.c122 = Constraint(expr=(m.x11 - m.x15)**2 + (m.x12 - m.x16)**2 - (m.x46 + m.x48)**2 + m.x169 >= 0)

m.c123 = Constraint(expr=(m.x11 - m.x17)**2 + (m.x12 - m.x18)**2 - (m.x46 + m.x49)**2 + m.x169 >= 0)

m.c124 = Constraint(expr=(m.x11 - m.x19)**2 + (m.x12 - m.x20)**2 - (m.x46 + m.x50)**2 + m.x169 >= 0)

m.c125 = Constraint(expr=(m.x11 - m.x21)**2 + (m.x12 - m.x22)**2 - (m.x46 + m.x51)**2 + m.x169 >= 0)

m.c126 = Constraint(expr=(m.x11 - m.x23)**2 + (m.x12 - m.x24)**2 - (m.x46 + m.x52)**2 + m.x169 >= 0)

m.c127 = Constraint(expr=(m.x11 - m.x25)**2 + (m.x12 - m.x26)**2 - (m.x46 + m.x53)**2 + m.x169 >= 0)

m.c128 = Constraint(expr=(m.x11 - m.x27)**2 + (m.x12 - m.x28)**2 - (m.x46 + m.x54)**2 + m.x169 >= 0)

m.c129 = Constraint(expr=(m.x11 - m.x29)**2 + (m.x12 - m.x30)**2 - (m.x46 + m.x55)**2 + m.x169 >= 0)

m.c130 = Constraint(expr=(m.x11 - m.x31)**2 + (m.x12 - m.x32)**2 - (m.x46 + m.x56)**2 + m.x169 >= 0)

m.c131 = Constraint(expr=(m.x11 - m.x33)**2 + (m.x12 - m.x34)**2 - (m.x46 + m.x57)**2 + m.x169 >= 0)

m.c132 = Constraint(expr=(m.x11 - m.x35)**2 + (m.x12 - m.x36)**2 - (m.x46 + m.x58)**2 + m.x169 >= 0)

m.c133 = Constraint(expr=(m.x11 - m.x37)**2 + (m.x12 - m.x38)**2 - (m.x46 + m.x59)**2 + m.x169 >= 0)

m.c134 = Constraint(expr=(m.x11 - m.x39)**2 + (m.x12 - m.x40)**2 - (m.x46 + m.x60)**2 + m.x169 >= 0)

m.c135 = Constraint(expr=(m.x13 - m.x19)**2 + (m.x14 - m.x20)**2 - (m.x47 + m.x50)**2 + m.x169 >= 0)

m.c136 = Constraint(expr=(m.x13 - m.x25)**2 + (m.x14 - m.x26)**2 - (m.x47 + m.x53)**2 + m.x169 >= 0)

m.c137 = Constraint(expr=(m.x13 - m.x27)**2 + (m.x14 - m.x28)**2 - (m.x47 + m.x54)**2 + m.x169 >= 0)

m.c138 = Constraint(expr=(m.x13 - m.x29)**2 + (m.x14 - m.x30)**2 - (m.x47 + m.x55)**2 + m.x169 >= 0)

m.c139 = Constraint(expr=(m.x13 - m.x31)**2 + (m.x14 - m.x32)**2 - (m.x47 + m.x56)**2 + m.x169 >= 0)

m.c140 = Constraint(expr=(m.x13 - m.x33)**2 + (m.x14 - m.x34)**2 - (m.x47 + m.x57)**2 + m.x169 >= 0)

m.c141 = Constraint(expr=(m.x13 - m.x35)**2 + (m.x14 - m.x36)**2 - (m.x47 + m.x58)**2 + m.x169 >= 0)

m.c142 = Constraint(expr=(m.x13 - m.x37)**2 + (m.x14 - m.x38)**2 - (m.x47 + m.x59)**2 + m.x169 >= 0)

m.c143 = Constraint(expr=(m.x13 - m.x39)**2 + (m.x14 - m.x40)**2 - (m.x47 + m.x60)**2 + m.x169 >= 0)

m.c144 = Constraint(expr=(m.x15 - m.x21)**2 + (m.x16 - m.x22)**2 - (m.x48 + m.x51)**2 + m.x169 >= 0)

m.c145 = Constraint(expr=(m.x15 - m.x23)**2 + (m.x16 - m.x24)**2 - (m.x48 + m.x52)**2 + m.x169 >= 0)

m.c146 = Constraint(expr=(m.x15 - m.x25)**2 + (m.x16 - m.x26)**2 - (m.x48 + m.x53)**2 + m.x169 >= 0)

m.c147 = Constraint(expr=(m.x15 - m.x27)**2 + (m.x16 - m.x28)**2 - (m.x48 + m.x54)**2 + m.x169 >= 0)

m.c148 = Constraint(expr=(m.x15 - m.x29)**2 + (m.x16 - m.x30)**2 - (m.x48 + m.x55)**2 + m.x169 >= 0)

m.c149 = Constraint(expr=(m.x15 - m.x31)**2 + (m.x16 - m.x32)**2 - (m.x48 + m.x56)**2 + m.x169 >= 0)

m.c150 = Constraint(expr=(m.x15 - m.x33)**2 + (m.x16 - m.x34)**2 - (m.x48 + m.x57)**2 + m.x169 >= 0)

m.c151 = Constraint(expr=(m.x15 - m.x35)**2 + (m.x16 - m.x36)**2 - (m.x48 + m.x58)**2 + m.x169 >= 0)

m.c152 = Constraint(expr=(m.x15 - m.x37)**2 + (m.x16 - m.x38)**2 - (m.x48 + m.x59)**2 + m.x169 >= 0)

m.c153 = Constraint(expr=(m.x15 - m.x39)**2 + (m.x16 - m.x40)**2 - (m.x48 + m.x60)**2 + m.x169 >= 0)

m.c154 = Constraint(expr=(m.x17 - m.x23)**2 + (m.x18 - m.x24)**2 - (m.x49 + m.x52)**2 + m.x169 >= 0)

m.c155 = Constraint(expr=(m.x17 - m.x25)**2 + (m.x18 - m.x26)**2 - (m.x49 + m.x53)**2 + m.x169 >= 0)

m.c156 = Constraint(expr=(m.x17 - m.x27)**2 + (m.x18 - m.x28)**2 - (m.x49 + m.x54)**2 + m.x169 >= 0)

m.c157 = Constraint(expr=(m.x17 - m.x29)**2 + (m.x18 - m.x30)**2 - (m.x49 + m.x55)**2 + m.x169 >= 0)

m.c158 = Constraint(expr=(m.x17 - m.x31)**2 + (m.x18 - m.x32)**2 - (m.x49 + m.x56)**2 + m.x169 >= 0)

m.c159 = Constraint(expr=(m.x17 - m.x33)**2 + (m.x18 - m.x34)**2 - (m.x49 + m.x57)**2 + m.x169 >= 0)

m.c160 = Constraint(expr=(m.x17 - m.x35)**2 + (m.x18 - m.x36)**2 - (m.x49 + m.x58)**2 + m.x169 >= 0)

m.c161 = Constraint(expr=(m.x17 - m.x37)**2 + (m.x18 - m.x38)**2 - (m.x49 + m.x59)**2 + m.x169 >= 0)

m.c162 = Constraint(expr=(m.x17 - m.x39)**2 + (m.x18 - m.x40)**2 - (m.x49 + m.x60)**2 + m.x169 >= 0)

m.c163 = Constraint(expr=(m.x19 - m.x33)**2 + (m.x20 - m.x34)**2 - (m.x50 + m.x57)**2 + m.x169 >= 0)

m.c164 = Constraint(expr=(m.x19 - m.x35)**2 + (m.x20 - m.x36)**2 - (m.x50 + m.x58)**2 + m.x169 >= 0)

m.c165 = Constraint(expr=(m.x21 - m.x25)**2 + (m.x22 - m.x26)**2 - (m.x51 + m.x53)**2 + m.x169 >= 0)

m.c166 = Constraint(expr=(m.x21 - m.x27)**2 + (m.x22 - m.x28)**2 - (m.x51 + m.x54)**2 + m.x169 >= 0)

m.c167 = Constraint(expr=(m.x21 - m.x29)**2 + (m.x22 - m.x30)**2 - (m.x51 + m.x55)**2 + m.x169 >= 0)

m.c168 = Constraint(expr=(m.x21 - m.x31)**2 + (m.x22 - m.x32)**2 - (m.x51 + m.x56)**2 + m.x169 >= 0)

m.c169 = Constraint(expr=(m.x21 - m.x33)**2 + (m.x22 - m.x34)**2 - (m.x51 + m.x57)**2 + m.x169 >= 0)

m.c170 = Constraint(expr=(m.x21 - m.x35)**2 + (m.x22 - m.x36)**2 - (m.x51 + m.x58)**2 + m.x169 >= 0)

m.c171 = Constraint(expr=(m.x21 - m.x37)**2 + (m.x22 - m.x38)**2 - (m.x51 + m.x59)**2 + m.x169 >= 0)

m.c172 = Constraint(expr=(m.x21 - m.x39)**2 + (m.x22 - m.x40)**2 - (m.x51 + m.x60)**2 + m.x169 >= 0)

m.c173 = Constraint(expr=(m.x23 - m.x31)**2 + (m.x24 - m.x32)**2 - (m.x52 + m.x56)**2 + m.x169 >= 0)

m.c174 = Constraint(expr=(m.x23 - m.x37)**2 + (m.x24 - m.x38)**2 - (m.x52 + m.x59)**2 + m.x169 >= 0)

m.c175 = Constraint(expr=(m.x25 - m.x29)**2 + (m.x26 - m.x30)**2 - (m.x53 + m.x55)**2 + m.x169 >= 0)

m.c176 = Constraint(expr=(m.x25 - m.x31)**2 + (m.x26 - m.x32)**2 - (m.x53 + m.x56)**2 + m.x169 >= 0)

m.c177 = Constraint(expr=(m.x25 - m.x33)**2 + (m.x26 - m.x34)**2 - (m.x53 + m.x57)**2 + m.x169 >= 0)

m.c178 = Constraint(expr=(m.x25 - m.x35)**2 + (m.x26 - m.x36)**2 - (m.x53 + m.x58)**2 + m.x169 >= 0)

m.c179 = Constraint(expr=(m.x25 - m.x37)**2 + (m.x26 - m.x38)**2 - (m.x53 + m.x59)**2 + m.x169 >= 0)

m.c180 = Constraint(expr=(m.x25 - m.x39)**2 + (m.x26 - m.x40)**2 - (m.x53 + m.x60)**2 + m.x169 >= 0)

m.c181 = Constraint(expr=(m.x27 - m.x31)**2 + (m.x28 - m.x32)**2 - (m.x54 + m.x56)**2 + m.x169 >= 0)

m.c182 = Constraint(expr=(m.x27 - m.x33)**2 + (m.x28 - m.x34)**2 - (m.x54 + m.x57)**2 + m.x169 >= 0)

m.c183 = Constraint(expr=(m.x27 - m.x35)**2 + (m.x28 - m.x36)**2 - (m.x54 + m.x58)**2 + m.x169 >= 0)

m.c184 = Constraint(expr=(m.x27 - m.x37)**2 + (m.x28 - m.x38)**2 - (m.x54 + m.x59)**2 + m.x169 >= 0)

m.c185 = Constraint(expr=(m.x27 - m.x39)**2 + (m.x28 - m.x40)**2 - (m.x54 + m.x60)**2 + m.x169 >= 0)

m.c186 = Constraint(expr=(m.x29 - m.x35)**2 + (m.x30 - m.x36)**2 - (m.x55 + m.x58)**2 + m.x169 >= 0)

m.c187 = Constraint(expr=(m.x29 - m.x37)**2 + (m.x30 - m.x38)**2 - (m.x55 + m.x59)**2 + m.x169 >= 0)

m.c188 = Constraint(expr=(m.x29 - m.x39)**2 + (m.x30 - m.x40)**2 - (m.x55 + m.x60)**2 + m.x169 >= 0)

m.c189 = Constraint(expr=(m.x31 - m.x39)**2 + (m.x32 - m.x40)**2 - (m.x56 + m.x60)**2 + m.x169 >= 0)

m.c190 = Constraint(expr=(m.x33 - m.x37)**2 + (m.x34 - m.x38)**2 - (m.x57 + m.x59)**2 + m.x169 >= 0)

m.c191 = Constraint(expr=(m.x33 - m.x39)**2 + (m.x34 - m.x40)**2 - (m.x57 + m.x60)**2 + m.x169 >= 0)
