#  MINLP written by GAMS Convert at 04/21/18 13:53:10
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        341       96       64      181        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        215      185       30        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1155      898      257        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x15 = Var(within=Reals,bounds=(100,200),initialize=100)
m.x16 = Var(within=Reals,bounds=(100,200),initialize=100)
m.x17 = Var(within=Reals,bounds=(0.3,4),initialize=0.3)
m.x18 = Var(within=Reals,bounds=(50,500),initialize=50)
m.x19 = Var(within=Reals,bounds=(6.4,10),initialize=6.4)
m.x20 = Var(within=Reals,bounds=(30,70),initialize=30)
m.x21 = Var(within=Reals,bounds=(70,100),initialize=70)
m.x22 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,15),initialize=0)
m.x25 = Var(within=Reals,bounds=(0.1,4),initialize=0.1)
m.x26 = Var(within=Reals,bounds=(0.1,4),initialize=0.1)
m.x27 = Var(within=Reals,bounds=(0.1,4),initialize=0.1)
m.x28 = Var(within=Reals,bounds=(0.3,4),initialize=0.3)
m.x29 = Var(within=Reals,bounds=(50,250),initialize=50)
m.x30 = Var(within=Reals,bounds=(6.4,8),initialize=6.4)
m.x31 = Var(within=Reals,bounds=(30,60),initialize=30)
m.x32 = Var(within=Reals,bounds=(70,85),initialize=70)
m.x33 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x34 = Var(within=Reals,bounds=(0,0.5),initialize=0)
m.x35 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x36 = Var(within=Reals,bounds=(0.1,4),initialize=0.1)
m.x37 = Var(within=Reals,bounds=(0.1,4),initialize=0.1)
m.x38 = Var(within=Reals,bounds=(0.1,4),initialize=0.1)
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
m.x70 = Var(within=Reals,bounds=(0,0.3707916),initialize=0)
m.x71 = Var(within=Reals,bounds=(0,0.22428),initialize=0)
m.x72 = Var(within=Reals,bounds=(0,0.2010816),initialize=0)
m.x73 = Var(within=Reals,bounds=(0,0.16128),initialize=0)
m.x74 = Var(within=Reals,bounds=(0,0.3707916),initialize=0)
m.x75 = Var(within=Reals,bounds=(0,0.22428),initialize=0)
m.x76 = Var(within=Reals,bounds=(0,0.2010816),initialize=0)
m.x77 = Var(within=Reals,bounds=(0,0.16128),initialize=0)
m.x78 = Var(within=Reals,bounds=(0,0.3707916),initialize=0)
m.x79 = Var(within=Reals,bounds=(0,0.22428),initialize=0)
m.x80 = Var(within=Reals,bounds=(0,0.2010816),initialize=0)
m.x81 = Var(within=Reals,bounds=(0,0.16128),initialize=0)
m.x82 = Var(within=Reals,bounds=(0,0.3707916),initialize=0)
m.x83 = Var(within=Reals,bounds=(0,0.22428),initialize=0)
m.x84 = Var(within=Reals,bounds=(0,0.2010816),initialize=0)
m.x85 = Var(within=Reals,bounds=(0,0.16128),initialize=0)
m.x86 = Var(within=Reals,bounds=(0,0.3707916),initialize=0)
m.x87 = Var(within=Reals,bounds=(0,0.22428),initialize=0)
m.x88 = Var(within=Reals,bounds=(0,0.2010816),initialize=0)
m.x89 = Var(within=Reals,bounds=(0,0.16128),initialize=0)
m.x90 = Var(within=Reals,bounds=(0,0.3707916),initialize=0)
m.x91 = Var(within=Reals,bounds=(0,0.22428),initialize=0)
m.x92 = Var(within=Reals,bounds=(0,0.2010816),initialize=0)
m.x93 = Var(within=Reals,bounds=(0,0.16128),initialize=0)
m.x94 = Var(within=Reals,bounds=(0,0.122376),initialize=0)
m.x95 = Var(within=Reals,bounds=(0,0.126564),initialize=0)
m.x96 = Var(within=Reals,bounds=(0,0.10198),initialize=0)
m.x97 = Var(within=Reals,bounds=(0,0.10547),initialize=0)
m.x98 = Var(within=Reals,bounds=(0,0.122376),initialize=0)
m.x99 = Var(within=Reals,bounds=(0,0.126564),initialize=0)
m.x100 = Var(within=Reals,bounds=(0,0.10198),initialize=0)
m.x101 = Var(within=Reals,bounds=(0,0.10547),initialize=0)
m.x102 = Var(within=Reals,bounds=(0,0.122376),initialize=0)
m.x103 = Var(within=Reals,bounds=(0,0.126564),initialize=0)
m.x104 = Var(within=Reals,bounds=(0,0.10198),initialize=0)
m.x105 = Var(within=Reals,bounds=(0,0.10547),initialize=0)
m.x106 = Var(within=Reals,bounds=(0,0.122376),initialize=0)
m.x107 = Var(within=Reals,bounds=(0,0.126564),initialize=0)
m.x108 = Var(within=Reals,bounds=(0,0.10198),initialize=0)
m.x109 = Var(within=Reals,bounds=(0,0.10547),initialize=0)
m.x110 = Var(within=Reals,bounds=(0,0.122376),initialize=0)
m.x111 = Var(within=Reals,bounds=(0,0.126564),initialize=0)
m.x112 = Var(within=Reals,bounds=(0,0.10198),initialize=0)
m.x113 = Var(within=Reals,bounds=(0,0.10547),initialize=0)
m.x114 = Var(within=Reals,bounds=(0,0.122376),initialize=0)
m.x115 = Var(within=Reals,bounds=(0,0.126564),initialize=0)
m.x116 = Var(within=Reals,bounds=(0,0.10198),initialize=0)
m.x117 = Var(within=Reals,bounds=(0,0.10547),initialize=0)
m.x118 = Var(within=Reals,bounds=(0,0.211907),initialize=0)
m.x119 = Var(within=Reals,bounds=(0,0.212173),initialize=0)
m.x120 = Var(within=Reals,bounds=(0,0.211907),initialize=0)
m.x121 = Var(within=Reals,bounds=(0,0.212173),initialize=0)
m.x122 = Var(within=Reals,bounds=(0,0.211907),initialize=0)
m.x123 = Var(within=Reals,bounds=(0,0.212173),initialize=0)
m.x124 = Var(within=Reals,bounds=(0,0.211907),initialize=0)
m.x125 = Var(within=Reals,bounds=(0,0.212173),initialize=0)
m.x126 = Var(within=Reals,bounds=(0,0.211907),initialize=0)
m.x127 = Var(within=Reals,bounds=(0,0.212173),initialize=0)
m.x128 = Var(within=Reals,bounds=(0,0.211907),initialize=0)
m.x129 = Var(within=Reals,bounds=(0,0.212173),initialize=0)
m.x130 = Var(within=Reals,bounds=(0,0.211907),initialize=0)
m.x131 = Var(within=Reals,bounds=(0,0.212173),initialize=0)
m.x132 = Var(within=Reals,bounds=(0,0.211907),initialize=0)
m.x133 = Var(within=Reals,bounds=(0,0.212173),initialize=0)
m.x134 = Var(within=Reals,bounds=(0,0.295792),initialize=0)
m.x135 = Var(within=Reals,bounds=(0,0.26032),initialize=0)
m.x136 = Var(within=Reals,bounds=(0,0.221844),initialize=0)
m.x137 = Var(within=Reals,bounds=(0,0.19524),initialize=0)
m.x138 = Var(within=Reals,bounds=(0,0.295792),initialize=0)
m.x139 = Var(within=Reals,bounds=(0,0.26032),initialize=0)
m.x140 = Var(within=Reals,bounds=(0,0.221844),initialize=0)
m.x141 = Var(within=Reals,bounds=(0,0.19524),initialize=0)
m.x142 = Var(within=Reals,bounds=(0,0.295792),initialize=0)
m.x143 = Var(within=Reals,bounds=(0,0.26032),initialize=0)
m.x144 = Var(within=Reals,bounds=(0,0.221844),initialize=0)
m.x145 = Var(within=Reals,bounds=(0,0.19524),initialize=0)
m.x146 = Var(within=Reals,bounds=(0,0.295792),initialize=0)
m.x147 = Var(within=Reals,bounds=(0,0.26032),initialize=0)
m.x148 = Var(within=Reals,bounds=(0,0.221844),initialize=0)
m.x149 = Var(within=Reals,bounds=(0,0.19524),initialize=0)
m.x150 = Var(within=Reals,bounds=(-0.03816,0.3326316),initialize=0)
m.x151 = Var(within=Reals,bounds=(-0.1008,0.12348),initialize=0)
m.x152 = Var(within=Reals,bounds=(-0.03816,0.1629216),initialize=0)
m.x153 = Var(within=Reals,bounds=(-0.1008,0.06048),initialize=0)
m.x154 = Var(within=Reals,bounds=(-0.0734256,0.0489504),initialize=0)
m.x155 = Var(within=Reals,bounds=(-0.0759384,0.0506256),initialize=0)
m.x156 = Var(within=Reals,bounds=(-0.0734256,0.0285544),initialize=0)
m.x157 = Var(within=Reals,bounds=(-0.0759384,0.0295316),initialize=0)
m.x158 = Var(within=Reals,bounds=(-0.211907,0),initialize=0)
m.x159 = Var(within=Reals,bounds=(-0.212173,0),initialize=0)
m.x160 = Var(within=Reals,bounds=(-0.211907,0),initialize=0)
m.x161 = Var(within=Reals,bounds=(-0.212173,0),initialize=0)
m.x162 = Var(within=Reals,bounds=(-0.2736076,0.0221844),initialize=0)
m.x163 = Var(within=Reals,bounds=(-0.240796,0.019524),initialize=0)
m.x164 = Var(within=Reals,bounds=(-0.1996596,0.0221844),initialize=0)
m.x165 = Var(within=Reals,bounds=(-0.175716,0.019524),initialize=0)
m.x166 = Var(within=Reals,bounds=(6.4,10),initialize=6.4)
m.x167 = Var(within=Reals,bounds=(6.4,8),initialize=6.4)
m.x168 = Var(within=Reals,bounds=(33,65.52),initialize=33)
m.x169 = Var(within=Reals,bounds=(33,60),initialize=33)
m.x170 = Var(within=Reals,bounds=(18,30),initialize=18)
m.x171 = Var(within=Reals,bounds=(18,25),initialize=18)
m.x172 = Var(within=Reals,bounds=(83.6,91.3),initialize=83.6)
m.x173 = Var(within=Reals,bounds=(83.6,89.375),initialize=83.6)
m.x174 = Var(within=Reals,bounds=(72,94),initialize=72)
m.x175 = Var(within=Reals,bounds=(72,85),initialize=72)
m.x176 = Var(within=Reals,bounds=(50,450),initialize=50)
m.x177 = Var(within=Reals,bounds=(50,250),initialize=50)
m.x178 = Var(within=Reals,bounds=(70,95),initialize=70)
m.x179 = Var(within=Reals,bounds=(70,85),initialize=70)
m.x180 = Var(within=Reals,bounds=(18,30),initialize=18)
m.x181 = Var(within=Reals,bounds=(18,25),initialize=18)
m.x182 = Var(within=Reals,bounds=(3.77,15),initialize=3.77)
m.x183 = Var(within=Reals,bounds=(3.77,10),initialize=3.77)
m.x184 = Var(within=Reals,bounds=(10,30),initialize=10)
m.x185 = Var(within=Reals,bounds=(10,25),initialize=10)
m.x186 = Var(within=Reals,bounds=(70,95),initialize=70)
m.x187 = Var(within=Reals,bounds=(70,85),initialize=70)
m.x188 = Var(within=Reals,bounds=(-8,0),initialize=0)
m.x189 = Var(within=Reals,bounds=(-8,0),initialize=0)
m.x190 = Var(within=Reals,bounds=(-2,1),initialize=0)
m.x191 = Var(within=Reals,bounds=(-2,0),initialize=0)
m.x192 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x193 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x194 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x195 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x196 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x197 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x198 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x199 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x200 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x201 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x202 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x203 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x204 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x205 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x206 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x207 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x208 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x209 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x210 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x211 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x212 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x213 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x214 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x215 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=2*m.x1*m.x5 + 2*m.x1*m.x6 + 8*m.x2*m.x5 + 8*m.x2*m.x6 + 10*m.x3*m.x5 + 10*m.x3*m.x6 + 16*m.x4*
                       m.x5 + 16*m.x4*m.x6 - 6*m.x5 - 12*m.x6 + 10*m.x7 + 4*m.x8 - 4*m.x9 - 10*m.x10 - 4*m.x11
                        - 10*m.x12 - m.x13 - 7*m.x14, sense=minimize)

m.c2 = Constraint(expr=m.x1*m.x5 + m.x1*m.x6 <= 400)

m.c3 = Constraint(expr=m.x2*m.x5 + m.x2*m.x6 <= 200)

m.c4 = Constraint(expr=m.x3*m.x5 + m.x3*m.x6 <= 200)

m.c5 = Constraint(expr=m.x4*m.x5 + m.x4*m.x6 + m.x7 + m.x8 <= 100)

m.c6 = Constraint(expr=   m.x9 + m.x10 <= 10)

m.c7 = Constraint(expr=   m.x11 + m.x12 <= 10)

m.c8 = Constraint(expr=   m.x13 + m.x14 <= 50)

m.c9 = Constraint(expr=-(m.x1*m.x5 + m.x1*m.x6) <= -50)

m.c10 = Constraint(expr=   m.x5 + m.x6 <= 300)

m.c11 = Constraint(expr=   m.x1 + m.x2 + m.x3 + m.x4 == 1)

m.c12 = Constraint(expr=m.x1*m.x5 + m.x2*m.x5 + m.x3*m.x5 + m.x4*m.x5 - m.x5 == 0)

m.c13 = Constraint(expr=m.x1*m.x6 + m.x2*m.x6 + m.x3*m.x6 + m.x4*m.x6 - m.x6 == 0)

m.c14 = Constraint(expr= - m.x5 - m.x7 - m.x9 - m.x11 - m.x13 + m.x15 == 0)

m.c15 = Constraint(expr= - m.x6 - m.x8 - m.x10 - m.x12 - m.x14 + m.x16 == 0)

m.c16 = Constraint(expr=m.x17*m.x15 - (0.1*m.x1*m.x5 + 0.2*m.x2*m.x5 + 0.4*m.x3*m.x5 + 0.7*m.x4*m.x5) - 0.7*m.x7
                         - 18.15*m.x9 - 15.66*m.x11 - 34.73*m.x13 == 0)

m.c17 = Constraint(expr=m.x18*m.x15 - (800*m.x1*m.x5 + 400*m.x2*m.x5 + 200*m.x3*m.x5 + 100*m.x4*m.x5) - 100*m.x7 == 0)

m.c18 = Constraint(expr=m.x20*m.x15 - (20*m.x1*m.x5 + 60*m.x2*m.x5 + 55*m.x3*m.x5 + 50*m.x4*m.x5) - 50*m.x7 - 100*m.x9
                         - 100*m.x11 - 100*m.x13 == 0)

m.c19 = Constraint(expr=m.x21*m.x15 - (70*m.x1*m.x5 + 85*m.x2*m.x5 + 80*m.x3*m.x5 + 75*m.x4*m.x5) - 75*m.x7 - 100*m.x9
                         - 100*m.x11 - 100*m.x13 == 0)

m.c20 = Constraint(expr=m.x22*m.x15 - (50*m.x1*m.x5 + 30*m.x2*m.x5 + 25*m.x3*m.x5 + 10*m.x4*m.x5) - 10*m.x7 == 0)

m.c21 = Constraint(expr=m.x23*m.x15 - (0.8*m.x2*m.x5 + m.x3*m.x5 + 0.2*m.x4*m.x5) - 0.2*m.x7 == 0)

m.c22 = Constraint(expr=m.x24*m.x15 - (10*m.x1*m.x5 + 15*m.x2*m.x5 + 15*m.x3*m.x5 + 5*m.x4*m.x5) - 5*m.x7 == 0)

m.c23 = Constraint(expr=m.x25*m.x15 - 18.15*m.x9 == 0)

m.c24 = Constraint(expr=m.x26*m.x15 - 15.66*m.x11 == 0)

m.c25 = Constraint(expr=m.x27*m.x15 - 34.73*m.x13 == 0)

m.c26 = Constraint(expr=m.x28*m.x16 - (0.1*m.x1*m.x6 + 0.2*m.x2*m.x6 + 0.4*m.x3*m.x6 + 0.7*m.x4*m.x6) - 0.7*m.x8
                         - 18.15*m.x10 - 15.66*m.x12 - 34.73*m.x14 == 0)

m.c27 = Constraint(expr=m.x29*m.x16 - (800*m.x1*m.x6 + 400*m.x2*m.x6 + 200*m.x3*m.x6 + 100*m.x4*m.x6) - 100*m.x8 == 0)

m.c28 = Constraint(expr=m.x31*m.x16 - (20*m.x1*m.x6 + 60*m.x2*m.x6 + 55*m.x3*m.x6 + 50*m.x4*m.x6) - 50*m.x8 - 100*m.x10
                         - 100*m.x12 - 100*m.x14 == 0)

m.c29 = Constraint(expr=m.x32*m.x16 - (70*m.x1*m.x6 + 85*m.x2*m.x6 + 80*m.x3*m.x6 + 75*m.x4*m.x6) - 75*m.x8 - 100*m.x10
                         - 100*m.x12 - 100*m.x14 == 0)

m.c30 = Constraint(expr=m.x33*m.x16 - (50*m.x1*m.x6 + 30*m.x2*m.x6 + 25*m.x3*m.x6 + 10*m.x4*m.x6) - 10*m.x8 == 0)

m.c31 = Constraint(expr=m.x34*m.x16 - (0.8*m.x2*m.x6 + m.x3*m.x6 + 0.2*m.x4*m.x6) - 0.2*m.x8 == 0)

m.c32 = Constraint(expr=m.x35*m.x16 - (10*m.x1*m.x6 + 15*m.x2*m.x6 + 15*m.x3*m.x6 + 5*m.x4*m.x6) - 5*m.x8 == 0)

m.c33 = Constraint(expr=m.x36*m.x16 - 18.15*m.x10 == 0)

m.c34 = Constraint(expr=m.x37*m.x16 - 15.66*m.x12 == 0)

m.c35 = Constraint(expr=m.x38*m.x16 - 34.73*m.x14 == 0)

m.c36 = Constraint(expr=m.x19**1.25*m.x15 - (9.39050748043972*m.x1*m.x5 + 15.1566541273553*m.x2*m.x5 + 13.4543426440594*
                        m.x3*m.x5 + 13.4543426440594*m.x4*m.x5) - 13.4543426440594*m.x7 - 14.3004303656297*m.x9
                         - 13.4543426440594*m.x11 - 16.8981453464332*m.x13 == 0)

m.c37 = Constraint(expr=m.x30**1.25*m.x16 - (9.39050748043972*m.x1*m.x6 + 15.1566541273553*m.x2*m.x6 + 13.4543426440594*
                        m.x3*m.x6 + 13.4543426440594*m.x4*m.x6) - 13.4543426440594*m.x8 - 14.3004303656297*m.x10
                         - 13.4543426440594*m.x12 - 16.8981453464332*m.x14 == 0)

m.c38 = Constraint(expr=-53.54*(0.444*exp((-1.26152) + 0.0006197*m.x18 + 0.22239*m.x23 + 0.02655*m.x184 - 0.003376*
                        m.x186) + 0.556*exp((-1.76845) - 0.096047*m.x17 + 0.000337*m.x18 + 0.222318*m.x23 + 0.011882*
                        m.x184 + 0.011251*m.x186)) + m.x206 == 0)

m.c39 = Constraint(expr=-53.54*(0.444*exp((-1.26152) + 0.0006197*m.x29 + 0.22239*m.x34 + 0.02655*m.x185 - 0.003376*
                        m.x187) + 0.556*exp((-1.76845) - 0.096047*m.x28 + 0.000337*m.x29 + 0.222318*m.x34 + 0.011882*
                        m.x185 + 0.011251*m.x187)) + m.x207 == 0)

m.c40 = Constraint(expr=-9.7*(0.444*exp(1.07807 + 0.0462131*m.x25 - 0.007166*m.x184 - 0.010226*m.x186) + 0.556*exp(
                        1.36651 - 0.031352*m.x24 + 0.0462131*m.x25 - 0.007166*m.x184 - 0.010226*m.x186)) + m.x208 == 0)

m.c41 = Constraint(expr=-9.7*(0.444*exp(1.07807 + 0.0462131*m.x36 - 0.007166*m.x185 - 0.010226*m.x187) + 0.556*exp(
                        1.36651 - 0.031352*m.x35 + 0.0462131*m.x36 - 0.007166*m.x185 - 0.010226*m.x187)) + m.x209 == 0)

m.c42 = Constraint(expr=-4.44*(0.444*exp(0.751747 + 0.0002631*m.x18 + 0.039786*m.x19 - 0.009594*m.x25 + 0.31658*m.x26 + 
                        0.24925*m.x27 - 0.005525*m.x184 - 0.012172*m.x186) + 0.556*exp(1.09751 + 0.0002627*m.x18 - 
                        0.05598*m.x25 + 0.3164665*m.x26 + 0.2493259*m.x27 - 0.005548*m.x184 - 0.012157*m.x186)) + m.x210
                         == 0)

m.c43 = Constraint(expr=-4.44*(0.444*exp(0.751747 + 0.0002631*m.x29 + 0.039786*m.x30 - 0.009594*m.x36 + 0.31658*m.x37 + 
                        0.24925*m.x38 - 0.005525*m.x185 - 0.012172*m.x187) + 0.556*exp(1.09751 + 0.0002627*m.x29 - 
                        0.05598*m.x36 + 0.3164665*m.x37 + 0.2493259*m.x38 - 0.005548*m.x185 - 0.012157*m.x187)) + m.x211
                         == 0)

m.c44 = Constraint(expr=-9.38*(0.444*exp(1.34704 + 0.0001552*m.x18 - 0.007253*m.x20 + 0.028235*m.x24 - 0.004005*m.x184
                         - 0.014866*m.x186) + 0.556*exp(0.694224 - 0.060771*m.x17 - 0.007311*m.x20 + 0.043696*m.x24 - 
                        0.004005*m.x184 - 0.008052*m.x186)) + m.x212 == 0)

m.c45 = Constraint(expr=-9.38*(0.444*exp(1.34704 + 0.0001552*m.x29 - 0.007253*m.x31 + 0.028235*m.x35 - 0.004005*m.x185
                         - 0.014866*m.x187) + 0.556*exp(0.694224 - 0.060771*m.x28 - 0.007311*m.x31 + 0.043696*m.x35 - 
                        0.004005*m.x185 - 0.008052*m.x187)) + m.x213 == 0)

m.c46 = Constraint(expr=-10*(1.75021*m.x23 - 0.603184*m.x19*m.x23 - 0.0402619*m.x25*m.x23 + 0.0738116*m.x19*m.x19*m.x23
                         + 0.0116427*m.x19*m.x25*m.x23 - 0.00255327*m.x19*m.x19*m.x19*m.x23 - 0.0010494*m.x19*m.x19*
                        m.x25*m.x23) + m.x214 == 0)

m.c47 = Constraint(expr=-10*(1.75021*m.x34 - 0.603184*m.x30*m.x34 - 0.0402619*m.x36*m.x34 + 0.0738116*m.x30*m.x30*m.x34
                         + 0.0116427*m.x30*m.x36*m.x34 - 0.00255327*m.x30*m.x30*m.x30*m.x34 - 0.0010494*m.x30*m.x30*
                        m.x36*m.x34) + m.x215 == 0)

m.c48 = Constraint(expr=   0.003355*m.x192 + m.x206 + m.x208 + m.x210 + m.x212 + m.x214 <= 90)

m.c49 = Constraint(expr=   0.003355*m.x193 + m.x207 + m.x209 + m.x211 + m.x213 + m.x215 <= 90)

m.c50 = Constraint(expr= - m.x178 + m.x186 == 0)

m.c51 = Constraint(expr= - m.x179 + m.x187 == 0)

m.c52 = Constraint(expr=   20*m.b42 + m.x184 <= 30)

m.c53 = Constraint(expr=   15*m.b43 + m.x185 <= 25)

m.c54 = Constraint(expr=   10*m.b42 - m.x184 <= 0)

m.c55 = Constraint(expr=   10*m.b43 - m.x185 <= 0)

m.c56 = Constraint(expr= - m.x22 - 30*m.b42 + m.x184 <= 0)

m.c57 = Constraint(expr= - m.x33 - 25*m.b43 + m.x185 <= 0)

m.c58 = Constraint(expr=   m.x22 - 30*m.b42 - m.x184 <= 0)

m.c59 = Constraint(expr=   m.x33 - 25*m.b43 - m.x185 <= 0)

m.c60 = Constraint(expr=-1340*(0.738*exp((-0.497032) + 0.0006921*m.x18 - 6.63e-7*m.x18**2 - 0.000119*m.x180**2 + 
                        0.0083632*m.x180 + 0.0003665*m.x182**2 - 0.002774*m.x182 + 0.0018571*m.x17 + 0.0090744*m.x19 + 
                        0.000931*m.x20 + 0.000846*m.x178)*m.x202 + 0.262*exp(0.179906 + 0.007097*m.x180 - 7.995e-5*
                        m.x180**2 + 0.0003665*m.x182**2 - 0.00276*m.x182 - 0.00913*m.x17 + 0.000252*m.x18 - 0.01397*
                        m.x19 + 0.000931*m.x20 - 0.00401*m.x178)*m.x203) + m.x200 == 0)

m.c61 = Constraint(expr=-1340*(0.738*exp((-0.497032) + 0.0006921*m.x29 - 6.63e-7*m.x29**2 - 0.000119*m.x181**2 + 
                        0.0083632*m.x181 + 0.0003665*m.x183**2 - 0.002774*m.x183 + 0.0018571*m.x28 + 0.0090744*m.x30 + 
                        0.000931*m.x31 + 0.000846*m.x179)*m.x204 + 0.262*exp(0.179906 + 0.007097*m.x181 - 7.995e-5*
                        m.x181**2 + 0.0003665*m.x183**2 - 0.00276*m.x183 - 0.00913*m.x28 + 0.000252*m.x29 - 0.01397*
                        m.x30 + 0.000931*m.x31 - 0.00401*m.x179)*m.x205) + m.x201 == 0)

m.c62 = Constraint(expr=   m.x200 <= 1300)

m.c63 = Constraint(expr=   m.x201 <= 1300)

m.c64 = Constraint(expr= - m.x150 - m.x154 - m.x158 + m.x202 == 1)

m.c65 = Constraint(expr= - m.x151 - m.x155 - m.x159 + m.x203 == 1)

m.c66 = Constraint(expr= - m.x152 - m.x156 - m.x160 + m.x204 == 1)

m.c67 = Constraint(expr= - m.x153 - m.x157 - m.x161 + m.x205 == 1)

m.c68 = Constraint(expr=   490*m.b58 + m.x176 <= 500)

m.c69 = Constraint(expr=   240*m.b59 + m.x177 <= 250)

m.c70 = Constraint(expr=   40*m.b58 + m.x176 >= 50)

m.c71 = Constraint(expr=   40*m.b59 + m.x177 >= 50)

m.c72 = Constraint(expr= - m.x18 - 450*m.b58 + 450*m.b60 + m.x176 <= 450)

m.c73 = Constraint(expr= - m.x29 - 200*m.b59 + 200*m.b61 + m.x177 <= 200)

m.c74 = Constraint(expr= - m.x18 + 450*m.b58 - 450*m.b60 + m.x176 >= -450)

m.c75 = Constraint(expr= - m.x29 + 200*m.b59 - 200*m.b61 + m.x177 >= -200)

m.c76 = Constraint(expr= - 50*m.b60 + m.x176 <= 450)

m.c77 = Constraint(expr=   200*m.b61 + m.x177 <= 450)

m.c78 = Constraint(expr=   400*m.b60 + m.x176 >= 450)

m.c79 = Constraint(expr=   400*m.b61 + m.x177 >= 450)

m.c80 = Constraint(expr= - 5*m.b40 + m.x178 <= 95)

m.c81 = Constraint(expr=   10*m.b41 + m.x179 <= 95)

m.c82 = Constraint(expr= - 25*m.b40 - m.x178 <= -95)

m.c83 = Constraint(expr= - 25*m.b41 - m.x179 <= -95)

m.c84 = Constraint(expr= - m.x21 + 30*m.b40 + m.x178 <= 30)

m.c85 = Constraint(expr= - m.x32 + 15*m.b41 + m.x179 <= 15)

m.c86 = Constraint(expr=   m.x21 + 30*m.b40 - m.x178 <= 30)

m.c87 = Constraint(expr=   m.x32 + 15*m.b41 - m.x179 <= 15)

m.c88 = Constraint(expr=   12*m.b62 + m.x180 <= 30)

m.c89 = Constraint(expr=   7*m.b63 + m.x181 <= 25)

m.c90 = Constraint(expr= - 18*m.b62 + m.x180 >= 0)

m.c91 = Constraint(expr= - 18*m.b63 + m.x181 >= 0)

m.c92 = Constraint(expr= - m.x22 - 30*m.b62 + 30*m.b64 + m.x180 <= 30)

m.c93 = Constraint(expr= - m.x33 - 25*m.b63 + 25*m.b65 + m.x181 <= 25)

m.c94 = Constraint(expr= - m.x22 + 30*m.b62 - 30*m.b64 + m.x180 >= -30)

m.c95 = Constraint(expr= - m.x33 + 25*m.b63 - 25*m.b65 + m.x181 >= -25)

m.c96 = Constraint(expr=   6.8*m.b64 + m.x180 <= 36.8)

m.c97 = Constraint(expr=   11.8*m.b65 + m.x181 <= 36.8)

m.c98 = Constraint(expr=   36.8*m.b64 + m.x180 >= 36.8)

m.c99 = Constraint(expr=   36.8*m.b65 + m.x181 >= 36.8)

m.c100 = Constraint(expr=   11.23*m.b66 + m.x182 <= 15)

m.c101 = Constraint(expr=   6.23*m.b67 + m.x183 <= 10)

m.c102 = Constraint(expr= - 3.77*m.b66 + m.x182 >= 0)

m.c103 = Constraint(expr= - 3.77*m.b67 + m.x183 >= 0)

m.c104 = Constraint(expr= - m.x24 - 15*m.b66 + 15*m.b68 + m.x182 <= 15)

m.c105 = Constraint(expr= - m.x35 - 10*m.b67 + 10*m.b69 + m.x183 <= 10)

m.c106 = Constraint(expr= - m.x24 + 15*m.b66 - 15*m.b68 + m.x182 >= -15)

m.c107 = Constraint(expr= - m.x35 + 10*m.b67 - 10*m.b69 + m.x183 >= -10)

m.c108 = Constraint(expr=   4*m.b68 + m.x182 <= 19)

m.c109 = Constraint(expr=   9*m.b69 + m.x183 <= 19)

m.c110 = Constraint(expr=   19*m.b68 + m.x182 >= 19)

m.c111 = Constraint(expr=   19*m.b69 + m.x183 >= 19)

m.c112 = Constraint(expr=   0.3707916*m.b58 + m.x86 + m.x90 <= 0.3707916)

m.c113 = Constraint(expr=   0.22428*m.b58 + m.x87 + m.x91 <= 0.22428)

m.c114 = Constraint(expr=   0.2010816*m.b59 + m.x88 + m.x92 <= 0.2010816)

m.c115 = Constraint(expr=   0.16128*m.b59 + m.x89 + m.x93 <= 0.16128)

m.c116 = Constraint(expr= - 0.3707916*m.b58 + 0.3707916*m.b60 + m.x78 + m.x82 <= 0.3707916)

m.c117 = Constraint(expr= - 0.22428*m.b58 + 0.22428*m.b60 + m.x79 + m.x83 <= 0.22428)

m.c118 = Constraint(expr= - 0.2010816*m.b59 + 0.2010816*m.b61 + m.x80 + m.x84 <= 0.2010816)

m.c119 = Constraint(expr= - 0.16128*m.b59 + 0.16128*m.b61 + m.x81 + m.x85 <= 0.16128)

m.c120 = Constraint(expr= - 0.3707916*m.b60 + m.x70 + m.x74 <= 0)

m.c121 = Constraint(expr= - 0.22428*m.b60 + m.x71 + m.x75 <= 0)

m.c122 = Constraint(expr= - 0.2010816*m.b61 + m.x72 + m.x76 <= 0)

m.c123 = Constraint(expr= - 0.16128*m.b61 + m.x73 + m.x77 <= 0)

m.c124 = Constraint(expr= - 0.00067884*m.x18 + m.x86 - m.x90 + m.x150 == -0.0067884)

m.c125 = Constraint(expr= - 0.000252*m.x18 + m.x87 - m.x91 + m.x151 == -0.00252)

m.c126 = Constraint(expr= - 0.00067884*m.x29 + m.x88 - m.x92 + m.x152 == -0.0067884)

m.c127 = Constraint(expr= - 0.000252*m.x29 + m.x89 - m.x93 + m.x153 == -0.00252)

m.c128 = Constraint(expr=   m.x78 - m.x82 + m.x150 == 0)

m.c129 = Constraint(expr=   m.x79 - m.x83 + m.x151 == 0)

m.c130 = Constraint(expr=   m.x80 - m.x84 + m.x152 == 0)

m.c131 = Constraint(expr=   m.x81 - m.x85 + m.x153 == 0)

m.c132 = Constraint(expr= - 9.53999999999999E-5*m.x18 + m.x70 - m.x74 + m.x150 == -0.04293)

m.c133 = Constraint(expr= - 0.000252*m.x18 + m.x71 - m.x75 + m.x151 == -0.1134)

m.c134 = Constraint(expr= - 9.53999999999999E-5*m.x29 + m.x72 - m.x76 + m.x152 == -0.04293)

m.c135 = Constraint(expr= - 0.000252*m.x29 + m.x73 - m.x77 + m.x153 == -0.1134)

m.c136 = Constraint(expr=   0.122376*m.b42 + m.x110 + m.x114 <= 0.122376)

m.c137 = Constraint(expr=   0.126564*m.b42 + m.x111 + m.x115 <= 0.126564)

m.c138 = Constraint(expr=   0.10198*m.b43 + m.x112 + m.x116 <= 0.10198)

m.c139 = Constraint(expr=   0.10547*m.b43 + m.x113 + m.x117 <= 0.10547)

m.c140 = Constraint(expr= - 0.122376*m.b42 + 0.122376*m.b62 + m.x102 + m.x106 <= 0.122376)

m.c141 = Constraint(expr= - 0.126564*m.b42 + 0.126564*m.b62 + m.x103 + m.x107 <= 0.126564)

m.c142 = Constraint(expr= - 0.10198*m.b43 + 0.10198*m.b63 + m.x104 + m.x108 <= 0.10198)

m.c143 = Constraint(expr= - 0.10547*m.b43 + 0.10547*m.b63 + m.x105 + m.x109 <= 0.10547)

m.c144 = Constraint(expr= - 0.122376*m.b62 + m.x94 + m.x98 <= 0)

m.c145 = Constraint(expr= - 0.126564*m.b62 + m.x95 + m.x99 <= 0)

m.c146 = Constraint(expr= - 0.10198*m.b63 + m.x96 + m.x100 <= 0)

m.c147 = Constraint(expr= - 0.10547*m.b63 + m.x97 + m.x101 <= 0)

m.c148 = Constraint(expr=   m.x110 - m.x114 + m.x154 == -0.0326336)

m.c149 = Constraint(expr=   m.x111 - m.x115 + m.x155 == -0.0337504)

m.c150 = Constraint(expr=   m.x112 - m.x116 + m.x156 == -0.0326336)

m.c151 = Constraint(expr=   m.x113 - m.x117 + m.x157 == -0.0337504)

m.c152 = Constraint(expr= - 0.0040792*m.x22 + m.x102 - m.x106 + m.x154 == -0.0734256)

m.c153 = Constraint(expr= - 0.0042188*m.x22 + m.x103 - m.x107 + m.x155 == -0.0759384)

m.c154 = Constraint(expr= - 0.0040792*m.x33 + m.x104 - m.x108 + m.x156 == -0.0734256)

m.c155 = Constraint(expr= - 0.0042188*m.x33 + m.x105 - m.x109 + m.x157 == -0.0759384)

m.c156 = Constraint(expr=   m.x94 - m.x98 + m.x154 == 0)

m.c157 = Constraint(expr=   m.x95 - m.x99 + m.x155 == 0)

m.c158 = Constraint(expr=   m.x96 - m.x100 + m.x156 == 0)

m.c159 = Constraint(expr=   m.x97 - m.x101 + m.x157 == 0)

m.c160 = Constraint(expr=   0.211907*m.b68 + m.x126 + m.x130 <= 0.211907)

m.c161 = Constraint(expr=   0.212173*m.b68 + m.x127 + m.x131 <= 0.212173)

m.c162 = Constraint(expr=   0.211907*m.b69 + m.x128 + m.x132 <= 0.211907)

m.c163 = Constraint(expr=   0.212173*m.b69 + m.x129 + m.x133 <= 0.212173)

m.c164 = Constraint(expr= - 0.211907*m.b68 + m.x118 + m.x122 <= 0)

m.c165 = Constraint(expr= - 0.212173*m.b68 + m.x119 + m.x123 <= 0)

m.c166 = Constraint(expr= - 0.211907*m.b69 + m.x120 + m.x124 <= 0)

m.c167 = Constraint(expr= - 0.212173*m.b69 + m.x121 + m.x125 <= 0)

m.c168 = Constraint(expr=   m.x126 - m.x130 + m.x158 == 0)

m.c169 = Constraint(expr=   m.x127 - m.x131 + m.x159 == 0)

m.c170 = Constraint(expr=   m.x128 - m.x132 + m.x160 == 0)

m.c171 = Constraint(expr=   m.x129 - m.x133 + m.x161 == 0)

m.c172 = Constraint(expr= - 0.011153*m.x24 + m.x118 - m.x122 + m.x158 == -0.211907)

m.c173 = Constraint(expr= - 0.011167*m.x24 + m.x119 - m.x123 + m.x159 == -0.212173)

m.c174 = Constraint(expr= - 0.011153*m.x35 + m.x120 - m.x124 + m.x160 == -0.211907)

m.c175 = Constraint(expr= - 0.011167*m.x35 + m.x121 - m.x125 + m.x161 == -0.212173)

m.c176 = Constraint(expr=-907*(0.444*exp(2.77929 + 0.0001072*m.x168**2 - 0.01447*m.x168 + 0.0004087*m.x174**2 - 0.068624
                         *m.x174 - 0.0003481*m.x170*m.x174 + 0.0323712*m.x170 - 0.003641*m.x17 + 0.0005219*m.x18 + 
                         0.0289749*m.x19 - 0.002858*m.x24)*m.x196 + 0.556*exp(2.26558 + 0.000106*m.x168**2 - 0.013504*
                         m.x168 + 0.000408*m.x174**2 - 0.062327*m.x174 - 0.000287*m.x170*m.x174 + 0.0282042*m.x170 - 
                         0.003626*m.x17 - 5.4e-5*m.x18 + 0.043295*m.x19 - 0.002858*m.x24)*m.x197) + m.x192 == 0)

m.c177 = Constraint(expr=-907*(0.444*exp(2.77929 + 0.0001072*m.x169**2 - 0.01447*m.x169 + 0.0004087*m.x175**2 - 0.068624
                         *m.x175 - 0.0003481*m.x171*m.x175 + 0.0323712*m.x171 - 0.003641*m.x28 + 0.0005219*m.x29 + 
                         0.0289749*m.x30 - 0.002858*m.x35)*m.x198 + 0.556*exp(2.26558 + 0.000106*m.x169**2 - 0.013504*
                         m.x169 + 0.000408*m.x175**2 - 0.062327*m.x175 - 0.000287*m.x171*m.x175 + 0.0282042*m.x171 - 
                         0.003626*m.x28 - 5.4e-5*m.x29 + 0.043295*m.x30 - 0.002858*m.x35)*m.x199) + m.x193 == 0)

m.c178 = Constraint(expr=-1000*(0.0318*m.x166**2 - 0.3534*m.x166) + m.x194 == 1226.9)

m.c179 = Constraint(expr=-1000*(0.0318*m.x167**2 - 0.3534*m.x167) + m.x195 == 1226.9)

m.c180 = Constraint(expr=   m.x192 + m.x194 <= 1200)

m.c181 = Constraint(expr=   m.x193 + m.x195 <= 1200)

m.c182 = Constraint(expr=-((0.0323712 - 0.0003481*m.x174)*m.x188 + (-0.068624 - 0.0003481*m.x170 + 0.0008174*m.x174)*
                         m.x190) - m.x162 + m.x196 == 1)

m.c183 = Constraint(expr=-((0.0282042 - 0.000287*m.x174)*m.x188 + (-0.062327 - 0.000287*m.x170 + 0.000816*m.x174)*m.x190
                         ) - m.x163 + m.x197 == 1)

m.c184 = Constraint(expr=-((0.0323712 - 0.0003481*m.x175)*m.x189 + (-0.068624 - 0.0003481*m.x171 + 0.0008174*m.x175)*
                         m.x191) - m.x164 + m.x198 == 1)

m.c185 = Constraint(expr=-((0.0282042 - 0.000287*m.x175)*m.x189 + (-0.062327 - 0.000287*m.x171 + 0.000816*m.x175)*m.x191
                         ) - m.x165 + m.x199 == 1)

m.c186 = Constraint(expr=   28*m.b48 + m.x174 <= 100)

m.c187 = Constraint(expr=   13*m.b49 + m.x175 <= 85)

m.c188 = Constraint(expr= - 2*m.b48 + m.x174 >= 70)

m.c189 = Constraint(expr= - 2*m.b49 + m.x175 >= 70)

m.c190 = Constraint(expr= - m.x21 - 30*m.b48 + 30*m.b56 + m.x174 <= 30)

m.c191 = Constraint(expr= - m.x32 - 15*m.b49 + 15*m.b57 + m.x175 <= 15)

m.c192 = Constraint(expr= - m.x21 + 30*m.b48 - 30*m.b56 + m.x174 >= -30)

m.c193 = Constraint(expr= - m.x32 + 15*m.b49 - 15*m.b57 + m.x175 >= -15)

m.c194 = Constraint(expr= - 16.4*m.b56 - m.x172 + m.x174 <= 0)

m.c195 = Constraint(expr= - 1.40000000000001*m.b57 - m.x173 + m.x175 <= 0)

m.c196 = Constraint(expr=   21.3*m.b56 - m.x172 + m.x174 >= 0)

m.c197 = Constraint(expr=   19.375*m.b57 - m.x173 + m.x175 >= 0)

m.c198 = Constraint(expr= - m.x21 + 3*m.b48 + m.x190 <= -69)

m.c199 = Constraint(expr= - m.x32 + 2*m.b49 + m.x191 <= -70)

m.c200 = Constraint(expr= - m.x21 - 30*m.b48 + m.x190 >= -102)

m.c201 = Constraint(expr= - m.x32 - 15*m.b49 + m.x191 >= -87)

m.c202 = Constraint(expr=   2*m.b48 - 2*m.b56 + m.x190 >= -2)

m.c203 = Constraint(expr=   2*m.b49 - 2*m.b57 + m.x191 >= -2)

m.c204 = Constraint(expr= - m.b48 + m.b56 + m.x190 <= 1)

m.c205 = Constraint(expr=   m.x191 <= 0)

m.c206 = Constraint(expr=   2*m.b48 + 2*m.b54 + m.x190 >= 0)

m.c207 = Constraint(expr=   2*m.b49 + 2*m.b55 + m.x191 >= 0)

m.c208 = Constraint(expr= - m.b48 - m.b54 + m.x190 <= 0)

m.c209 = Constraint(expr=   m.x191 <= 0)

m.c210 = Constraint(expr= - m.x21 - 3*m.b54 + 3*m.b56 + m.x190 >= -97)

m.c211 = Constraint(expr= - m.x32 - 3*m.b55 + 3*m.b57 + m.x191 >= -97)

m.c212 = Constraint(expr= - m.x21 + 23*m.b54 - 23*m.b56 + m.x190 <= -71)

m.c213 = Constraint(expr= - m.x32 + 22*m.b55 - 22*m.b57 + m.x191 <= -72)

m.c214 = Constraint(expr=   7.7*m.b42 - 7.7*m.b54 + m.x172 <= 91.3)

m.c215 = Constraint(expr=   5.775*m.b43 - 5.775*m.b55 + m.x173 <= 89.375)

m.c216 = Constraint(expr= - 3.85*m.b42 + 3.85*m.b54 + m.x172 >= 79.75)

m.c217 = Constraint(expr= - 3.85*m.b43 + 3.85*m.b55 + m.x173 >= 79.75)

m.c218 = Constraint(expr= - 0.385*m.x22 - 11.55*m.b42 - 11.55*m.b54 + m.x172 <= 79.75)

m.c219 = Constraint(expr= - 0.385*m.x33 - 9.625*m.b43 - 9.625*m.b55 + m.x173 <= 79.75)

m.c220 = Constraint(expr= - 0.385*m.x22 + 11.55*m.b42 + 11.55*m.b54 + m.x172 >= 79.75)

m.c221 = Constraint(expr= - 0.385*m.x33 + 9.625*m.b43 + 9.625*m.b55 + m.x173 >= 79.75)

m.c222 = Constraint(expr= - 2.7*m.b54 + m.x172 <= 91.3)

m.c223 = Constraint(expr= - 4.625*m.b55 + m.x173 <= 89.375)

m.c224 = Constraint(expr= - 14.25*m.b54 + m.x172 >= 79.75)

m.c225 = Constraint(expr= - 14.25*m.b55 + m.x173 >= 79.75)

m.c226 = Constraint(expr=   m.x21 + 21.3*m.b56 - m.x172 >= 0)

m.c227 = Constraint(expr=   m.x32 + 19.375*m.b57 - m.x173 >= 0)

m.c228 = Constraint(expr=   m.x21 + 16.4*m.b56 - m.x172 <= 16.4)

m.c229 = Constraint(expr=   m.x32 + 1.40000000000001*m.b57 - m.x173 <= 1.40000000000001)

m.c230 = Constraint(expr=   32.52*m.b44 + m.x168 <= 65.52)

m.c231 = Constraint(expr=   27*m.b45 + m.x169 <= 60)

m.c232 = Constraint(expr=   m.x168 >= 33)

m.c233 = Constraint(expr=   m.x169 >= 33)

m.c234 = Constraint(expr= - m.x20 - 35.52*m.b44 + 35.52*m.b46 + m.x168 <= 35.52)

m.c235 = Constraint(expr= - m.x31 - 30*m.b45 + 30*m.b47 + m.x169 <= 30)

m.c236 = Constraint(expr= - m.x20 + 37*m.b44 - 37*m.b46 + m.x168 >= -37)

m.c237 = Constraint(expr= - m.x31 + 27*m.b45 - 27*m.b47 + m.x169 >= -27)

m.c238 = Constraint(expr=   m.x168 <= 65.52)

m.c239 = Constraint(expr=   5.52*m.b47 + m.x169 <= 65.52)

m.c240 = Constraint(expr=   32.52*m.b46 + m.x168 >= 65.52)

m.c241 = Constraint(expr=   32.52*m.b47 + m.x169 >= 65.52)

m.c242 = Constraint(expr=   0.295792*m.b44 + m.x142 + m.x146 <= 0.295792)

m.c243 = Constraint(expr=   0.26032*m.b44 + m.x143 + m.x147 <= 0.26032)

m.c244 = Constraint(expr=   0.221844*m.b45 + m.x144 + m.x148 <= 0.221844)

m.c245 = Constraint(expr=   0.19524*m.b45 + m.x145 + m.x149 <= 0.19524)

m.c246 = Constraint(expr= - 0.295792*m.b44 + m.x134 + m.x138 <= 0)

m.c247 = Constraint(expr= - 0.26032*m.b44 + m.x135 + m.x139 <= 0)

m.c248 = Constraint(expr= - 0.221844*m.b45 + m.x136 + m.x140 <= 0)

m.c249 = Constraint(expr= - 0.19524*m.b45 + m.x137 + m.x141 <= 0)

m.c250 = Constraint(expr=   0.0073948*m.x20 + m.x142 - m.x146 + m.x162 == 0.2440284)

m.c251 = Constraint(expr=   0.006508*m.x20 + m.x143 - m.x147 + m.x163 == 0.214764)

m.c252 = Constraint(expr=   0.0073948*m.x31 + m.x144 - m.x148 + m.x164 == 0.2440284)

m.c253 = Constraint(expr=   0.006508*m.x31 + m.x145 - m.x149 + m.x165 == 0.214764)

m.c254 = Constraint(expr=   m.x134 - m.x138 + m.x162 == 0)

m.c255 = Constraint(expr=   m.x135 - m.x139 + m.x163 == 0)

m.c256 = Constraint(expr=   m.x136 - m.x140 + m.x164 == 0)

m.c257 = Constraint(expr=   m.x137 - m.x141 + m.x165 == 0)

m.c258 = Constraint(expr=   8*m.b42 + m.x188 <= 0)

m.c259 = Constraint(expr=   8*m.b43 + m.x189 <= 0)

m.c260 = Constraint(expr=   m.x188 >= -8)

m.c261 = Constraint(expr=   m.x189 >= -8)

m.c262 = Constraint(expr= - m.x22 - 18*m.b42 + 18*m.b50 + m.x188 <= 0)

m.c263 = Constraint(expr= - m.x33 - 18*m.b43 + 18*m.b51 + m.x189 <= 0)

m.c264 = Constraint(expr= - m.x22 + 20*m.b42 - 20*m.b50 + m.x188 >= -38)

m.c265 = Constraint(expr= - m.x33 + 15*m.b43 - 15*m.b51 + m.x189 >= -33)

m.c266 = Constraint(expr=   m.x188 <= 0)

m.c267 = Constraint(expr=   m.x189 <= 0)

m.c268 = Constraint(expr=   8*m.b50 - 8*m.b52 + m.x188 >= -8)

m.c269 = Constraint(expr=   8*m.b51 - 8*m.b53 + m.x189 >= -8)

m.c270 = Constraint(expr= - m.x22 - 46*m.b52 + m.x188 <= -46)

m.c271 = Constraint(expr= - m.x33 - 46*m.b53 + m.x189 <= -46)

m.c272 = Constraint(expr= - m.x22 - 8*m.b52 + m.x188 >= -46)

m.c273 = Constraint(expr= - m.x33 - 13*m.b53 + m.x189 >= -46)

m.c274 = Constraint(expr=   12*m.b50 + m.x170 <= 30)

m.c275 = Constraint(expr=   7*m.b51 + m.x171 <= 25)

m.c276 = Constraint(expr= - 18*m.b50 + m.x170 >= 0)

m.c277 = Constraint(expr= - 18*m.b51 + m.x171 >= 0)

m.c278 = Constraint(expr= - m.x22 - 30*m.b50 + 30*m.b52 + m.x170 <= 30)

m.c279 = Constraint(expr= - m.x33 - 25*m.b51 + 25*m.b53 + m.x171 <= 25)

m.c280 = Constraint(expr= - m.x22 + 30*m.b50 - 30*m.b52 + m.x170 >= -30)

m.c281 = Constraint(expr= - m.x33 + 25*m.b51 - 25*m.b53 + m.x171 >= -25)

m.c282 = Constraint(expr=   16*m.b52 + m.x170 <= 46)

m.c283 = Constraint(expr=   21*m.b53 + m.x171 <= 46)

m.c284 = Constraint(expr=   46*m.b52 + m.x170 >= 46)

m.c285 = Constraint(expr=   46*m.b53 + m.x171 >= 46)

m.c286 = Constraint(expr=   m.x17 - m.x25 - m.x26 - m.x27 >= 0)

m.c287 = Constraint(expr=   m.x28 - m.x36 - m.x37 - m.x38 >= 0)

m.c288 = Constraint(expr= - m.x21 - 25*m.b40 <= -95)

m.c289 = Constraint(expr= - m.x32 - 25*m.b41 <= -95)

m.c290 = Constraint(expr=   m.x21 + 5*m.b40 <= 100)

m.c291 = Constraint(expr=   m.x32 - 10*m.b41 <= 85)

m.c292 = Constraint(expr= - m.x22 - 10*m.b42 <= -10)

m.c293 = Constraint(expr= - m.x33 - 10*m.b43 <= -10)

m.c294 = Constraint(expr=   m.x22 + 20*m.b42 <= 30)

m.c295 = Constraint(expr=   m.x33 + 15*m.b43 <= 25)

m.c296 = Constraint(expr= - m.x20 - 3*m.b44 <= -33)

m.c297 = Constraint(expr= - m.x31 - 3*m.b45 <= -33)

m.c298 = Constraint(expr=   m.x20 + 37*m.b44 <= 70)

m.c299 = Constraint(expr=   m.x31 + 27*m.b45 <= 60)

m.c300 = Constraint(expr= - m.x20 - 35.52*m.b46 <= -65.52)

m.c301 = Constraint(expr= - m.x31 - 35.52*m.b47 <= -65.52)

m.c302 = Constraint(expr=   m.x20 + 4.48*m.b46 <= 70)

m.c303 = Constraint(expr=   m.x31 - 5.52*m.b47 <= 60)

m.c304 = Constraint(expr= - m.x21 - 2*m.b48 <= -72)

m.c305 = Constraint(expr= - m.x32 - 2*m.b49 <= -72)

m.c306 = Constraint(expr=   m.x21 + 28*m.b48 <= 100)

m.c307 = Constraint(expr=   m.x32 + 13*m.b49 <= 85)

m.c308 = Constraint(expr= - m.x22 - 18*m.b50 <= -18)

m.c309 = Constraint(expr= - m.x33 - 18*m.b51 <= -18)

m.c310 = Constraint(expr=   m.x22 + 12*m.b50 <= 30)

m.c311 = Constraint(expr=   m.x33 + 7*m.b51 <= 25)

m.c312 = Constraint(expr= - m.x22 - 46*m.b52 <= -46)

m.c313 = Constraint(expr= - m.x33 - 46*m.b53 <= -46)

m.c314 = Constraint(expr=   m.x22 - 16*m.b52 <= 30)

m.c315 = Constraint(expr=   m.x33 - 21*m.b53 <= 25)

m.c316 = Constraint(expr=   0.385*m.x22 + 2.7*m.b54 <= 14.25)

m.c317 = Constraint(expr=   0.385*m.x33 + 4.625*m.b55 <= 14.25)

m.c318 = Constraint(expr=   0.385*m.x22 - 14.25*m.b54 >= 0)

m.c319 = Constraint(expr=   0.385*m.x33 - 14.25*m.b55 >= 0)

m.c320 = Constraint(expr= - m.x18 + 40*m.b58 <= -10)

m.c321 = Constraint(expr= - m.x29 + 40*m.b59 <= -10)

m.c322 = Constraint(expr=   m.x18 + 490*m.b58 <= 500)

m.c323 = Constraint(expr=   m.x29 + 240*m.b59 <= 250)

m.c324 = Constraint(expr= - m.x18 - 400*m.b60 <= -450)

m.c325 = Constraint(expr= - m.x29 - 400*m.b61 <= -450)

m.c326 = Constraint(expr=   m.x18 + 50*m.b60 <= 500)

m.c327 = Constraint(expr=   m.x29 - 200*m.b61 <= 250)

m.c328 = Constraint(expr= - m.b50 + m.b62 == 0)

m.c329 = Constraint(expr= - m.b51 + m.b63 == 0)

m.c330 = Constraint(expr= - m.x22 - 36.8*m.b64 <= -36.8)

m.c331 = Constraint(expr= - m.x33 - 36.8*m.b65 <= -36.8)

m.c332 = Constraint(expr=   m.x22 - 6.8*m.b64 <= 30)

m.c333 = Constraint(expr=   m.x33 - 11.8*m.b65 <= 25)

m.c334 = Constraint(expr= - m.x24 - 3.77*m.b66 <= -3.77)

m.c335 = Constraint(expr= - m.x35 - 3.77*m.b67 <= -3.77)

m.c336 = Constraint(expr=   m.x24 + 11.23*m.b66 <= 15)

m.c337 = Constraint(expr=   m.x35 + 6.23*m.b67 <= 10)

m.c338 = Constraint(expr= - m.x24 - 19*m.b68 <= -19)

m.c339 = Constraint(expr= - m.x35 - 19*m.b69 <= -19)

m.c340 = Constraint(expr=   m.x24 - 4*m.b68 <= 15)

m.c341 = Constraint(expr=   m.x35 - 9*m.b69 <= 10)
