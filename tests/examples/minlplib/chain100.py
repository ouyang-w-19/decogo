#  NLP written by GAMS Convert at 04/21/18 13:51:14
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        102      102        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        203      203        0        0        0        0        0        0
#  FX      2        2        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        704      401      303        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(1,1),initialize=1)
m.x2 = Var(within=Reals,bounds=(None,None),initialize=0.9804)
m.x3 = Var(within=Reals,bounds=(None,None),initialize=0.9616)
m.x4 = Var(within=Reals,bounds=(None,None),initialize=0.9436)
m.x5 = Var(within=Reals,bounds=(None,None),initialize=0.9264)
m.x6 = Var(within=Reals,bounds=(None,None),initialize=0.91)
m.x7 = Var(within=Reals,bounds=(None,None),initialize=0.8944)
m.x8 = Var(within=Reals,bounds=(None,None),initialize=0.8796)
m.x9 = Var(within=Reals,bounds=(None,None),initialize=0.8656)
m.x10 = Var(within=Reals,bounds=(None,None),initialize=0.8524)
m.x11 = Var(within=Reals,bounds=(None,None),initialize=0.84)
m.x12 = Var(within=Reals,bounds=(None,None),initialize=0.8284)
m.x13 = Var(within=Reals,bounds=(None,None),initialize=0.8176)
m.x14 = Var(within=Reals,bounds=(None,None),initialize=0.8076)
m.x15 = Var(within=Reals,bounds=(None,None),initialize=0.7984)
m.x16 = Var(within=Reals,bounds=(None,None),initialize=0.79)
m.x17 = Var(within=Reals,bounds=(None,None),initialize=0.7824)
m.x18 = Var(within=Reals,bounds=(None,None),initialize=0.7756)
m.x19 = Var(within=Reals,bounds=(None,None),initialize=0.7696)
m.x20 = Var(within=Reals,bounds=(None,None),initialize=0.7644)
m.x21 = Var(within=Reals,bounds=(None,None),initialize=0.76)
m.x22 = Var(within=Reals,bounds=(None,None),initialize=0.7564)
m.x23 = Var(within=Reals,bounds=(None,None),initialize=0.7536)
m.x24 = Var(within=Reals,bounds=(None,None),initialize=0.7516)
m.x25 = Var(within=Reals,bounds=(None,None),initialize=0.7504)
m.x26 = Var(within=Reals,bounds=(None,None),initialize=0.75)
m.x27 = Var(within=Reals,bounds=(None,None),initialize=0.7504)
m.x28 = Var(within=Reals,bounds=(None,None),initialize=0.7516)
m.x29 = Var(within=Reals,bounds=(None,None),initialize=0.7536)
m.x30 = Var(within=Reals,bounds=(None,None),initialize=0.7564)
m.x31 = Var(within=Reals,bounds=(None,None),initialize=0.76)
m.x32 = Var(within=Reals,bounds=(None,None),initialize=0.7644)
m.x33 = Var(within=Reals,bounds=(None,None),initialize=0.7696)
m.x34 = Var(within=Reals,bounds=(None,None),initialize=0.7756)
m.x35 = Var(within=Reals,bounds=(None,None),initialize=0.7824)
m.x36 = Var(within=Reals,bounds=(None,None),initialize=0.79)
m.x37 = Var(within=Reals,bounds=(None,None),initialize=0.7984)
m.x38 = Var(within=Reals,bounds=(None,None),initialize=0.8076)
m.x39 = Var(within=Reals,bounds=(None,None),initialize=0.8176)
m.x40 = Var(within=Reals,bounds=(None,None),initialize=0.8284)
m.x41 = Var(within=Reals,bounds=(None,None),initialize=0.84)
m.x42 = Var(within=Reals,bounds=(None,None),initialize=0.8524)
m.x43 = Var(within=Reals,bounds=(None,None),initialize=0.8656)
m.x44 = Var(within=Reals,bounds=(None,None),initialize=0.8796)
m.x45 = Var(within=Reals,bounds=(None,None),initialize=0.8944)
m.x46 = Var(within=Reals,bounds=(None,None),initialize=0.91)
m.x47 = Var(within=Reals,bounds=(None,None),initialize=0.9264)
m.x48 = Var(within=Reals,bounds=(None,None),initialize=0.9436)
m.x49 = Var(within=Reals,bounds=(None,None),initialize=0.9616)
m.x50 = Var(within=Reals,bounds=(None,None),initialize=0.9804)
m.x51 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x52 = Var(within=Reals,bounds=(None,None),initialize=1.0204)
m.x53 = Var(within=Reals,bounds=(None,None),initialize=1.0416)
m.x54 = Var(within=Reals,bounds=(None,None),initialize=1.0636)
m.x55 = Var(within=Reals,bounds=(None,None),initialize=1.0864)
m.x56 = Var(within=Reals,bounds=(None,None),initialize=1.11)
m.x57 = Var(within=Reals,bounds=(None,None),initialize=1.1344)
m.x58 = Var(within=Reals,bounds=(None,None),initialize=1.1596)
m.x59 = Var(within=Reals,bounds=(None,None),initialize=1.1856)
m.x60 = Var(within=Reals,bounds=(None,None),initialize=1.2124)
m.x61 = Var(within=Reals,bounds=(None,None),initialize=1.24)
m.x62 = Var(within=Reals,bounds=(None,None),initialize=1.2684)
m.x63 = Var(within=Reals,bounds=(None,None),initialize=1.2976)
m.x64 = Var(within=Reals,bounds=(None,None),initialize=1.3276)
m.x65 = Var(within=Reals,bounds=(None,None),initialize=1.3584)
m.x66 = Var(within=Reals,bounds=(None,None),initialize=1.39)
m.x67 = Var(within=Reals,bounds=(None,None),initialize=1.4224)
m.x68 = Var(within=Reals,bounds=(None,None),initialize=1.4556)
m.x69 = Var(within=Reals,bounds=(None,None),initialize=1.4896)
m.x70 = Var(within=Reals,bounds=(None,None),initialize=1.5244)
m.x71 = Var(within=Reals,bounds=(None,None),initialize=1.56)
m.x72 = Var(within=Reals,bounds=(None,None),initialize=1.5964)
m.x73 = Var(within=Reals,bounds=(None,None),initialize=1.6336)
m.x74 = Var(within=Reals,bounds=(None,None),initialize=1.6716)
m.x75 = Var(within=Reals,bounds=(None,None),initialize=1.7104)
m.x76 = Var(within=Reals,bounds=(None,None),initialize=1.75)
m.x77 = Var(within=Reals,bounds=(None,None),initialize=1.7904)
m.x78 = Var(within=Reals,bounds=(None,None),initialize=1.8316)
m.x79 = Var(within=Reals,bounds=(None,None),initialize=1.8736)
m.x80 = Var(within=Reals,bounds=(None,None),initialize=1.9164)
m.x81 = Var(within=Reals,bounds=(None,None),initialize=1.96)
m.x82 = Var(within=Reals,bounds=(None,None),initialize=2.0044)
m.x83 = Var(within=Reals,bounds=(None,None),initialize=2.0496)
m.x84 = Var(within=Reals,bounds=(None,None),initialize=2.0956)
m.x85 = Var(within=Reals,bounds=(None,None),initialize=2.1424)
m.x86 = Var(within=Reals,bounds=(None,None),initialize=2.19)
m.x87 = Var(within=Reals,bounds=(None,None),initialize=2.2384)
m.x88 = Var(within=Reals,bounds=(None,None),initialize=2.2876)
m.x89 = Var(within=Reals,bounds=(None,None),initialize=2.3376)
m.x90 = Var(within=Reals,bounds=(None,None),initialize=2.3884)
m.x91 = Var(within=Reals,bounds=(None,None),initialize=2.44)
m.x92 = Var(within=Reals,bounds=(None,None),initialize=2.4924)
m.x93 = Var(within=Reals,bounds=(None,None),initialize=2.5456)
m.x94 = Var(within=Reals,bounds=(None,None),initialize=2.5996)
m.x95 = Var(within=Reals,bounds=(None,None),initialize=2.6544)
m.x96 = Var(within=Reals,bounds=(None,None),initialize=2.71)
m.x97 = Var(within=Reals,bounds=(None,None),initialize=2.7664)
m.x98 = Var(within=Reals,bounds=(None,None),initialize=2.8236)
m.x99 = Var(within=Reals,bounds=(None,None),initialize=2.8816)
m.x100 = Var(within=Reals,bounds=(None,None),initialize=2.9404)
m.x101 = Var(within=Reals,bounds=(3,3),initialize=3)
m.x102 = Var(within=Reals,bounds=(None,None),initialize=-2)
m.x103 = Var(within=Reals,bounds=(None,None),initialize=-1.92)
m.x104 = Var(within=Reals,bounds=(None,None),initialize=-1.84)
m.x105 = Var(within=Reals,bounds=(None,None),initialize=-1.76)
m.x106 = Var(within=Reals,bounds=(None,None),initialize=-1.68)
m.x107 = Var(within=Reals,bounds=(None,None),initialize=-1.6)
m.x108 = Var(within=Reals,bounds=(None,None),initialize=-1.52)
m.x109 = Var(within=Reals,bounds=(None,None),initialize=-1.44)
m.x110 = Var(within=Reals,bounds=(None,None),initialize=-1.36)
m.x111 = Var(within=Reals,bounds=(None,None),initialize=-1.28)
m.x112 = Var(within=Reals,bounds=(None,None),initialize=-1.2)
m.x113 = Var(within=Reals,bounds=(None,None),initialize=-1.12)
m.x114 = Var(within=Reals,bounds=(None,None),initialize=-1.04)
m.x115 = Var(within=Reals,bounds=(None,None),initialize=-0.96)
m.x116 = Var(within=Reals,bounds=(None,None),initialize=-0.88)
m.x117 = Var(within=Reals,bounds=(None,None),initialize=-0.8)
m.x118 = Var(within=Reals,bounds=(None,None),initialize=-0.72)
m.x119 = Var(within=Reals,bounds=(None,None),initialize=-0.64)
m.x120 = Var(within=Reals,bounds=(None,None),initialize=-0.56)
m.x121 = Var(within=Reals,bounds=(None,None),initialize=-0.48)
m.x122 = Var(within=Reals,bounds=(None,None),initialize=-0.4)
m.x123 = Var(within=Reals,bounds=(None,None),initialize=-0.32)
m.x124 = Var(within=Reals,bounds=(None,None),initialize=-0.24)
m.x125 = Var(within=Reals,bounds=(None,None),initialize=-0.16)
m.x126 = Var(within=Reals,bounds=(None,None),initialize=-0.0800000000000001)
m.x127 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x128 = Var(within=Reals,bounds=(None,None),initialize=0.0800000000000001)
m.x129 = Var(within=Reals,bounds=(None,None),initialize=0.16)
m.x130 = Var(within=Reals,bounds=(None,None),initialize=0.24)
m.x131 = Var(within=Reals,bounds=(None,None),initialize=0.32)
m.x132 = Var(within=Reals,bounds=(None,None),initialize=0.4)
m.x133 = Var(within=Reals,bounds=(None,None),initialize=0.48)
m.x134 = Var(within=Reals,bounds=(None,None),initialize=0.56)
m.x135 = Var(within=Reals,bounds=(None,None),initialize=0.64)
m.x136 = Var(within=Reals,bounds=(None,None),initialize=0.72)
m.x137 = Var(within=Reals,bounds=(None,None),initialize=0.8)
m.x138 = Var(within=Reals,bounds=(None,None),initialize=0.88)
m.x139 = Var(within=Reals,bounds=(None,None),initialize=0.96)
m.x140 = Var(within=Reals,bounds=(None,None),initialize=1.04)
m.x141 = Var(within=Reals,bounds=(None,None),initialize=1.12)
m.x142 = Var(within=Reals,bounds=(None,None),initialize=1.2)
m.x143 = Var(within=Reals,bounds=(None,None),initialize=1.28)
m.x144 = Var(within=Reals,bounds=(None,None),initialize=1.36)
m.x145 = Var(within=Reals,bounds=(None,None),initialize=1.44)
m.x146 = Var(within=Reals,bounds=(None,None),initialize=1.52)
m.x147 = Var(within=Reals,bounds=(None,None),initialize=1.6)
m.x148 = Var(within=Reals,bounds=(None,None),initialize=1.68)
m.x149 = Var(within=Reals,bounds=(None,None),initialize=1.76)
m.x150 = Var(within=Reals,bounds=(None,None),initialize=1.84)
m.x151 = Var(within=Reals,bounds=(None,None),initialize=1.92)
m.x152 = Var(within=Reals,bounds=(None,None),initialize=2)
m.x153 = Var(within=Reals,bounds=(None,None),initialize=2.08)
m.x154 = Var(within=Reals,bounds=(None,None),initialize=2.16)
m.x155 = Var(within=Reals,bounds=(None,None),initialize=2.24)
m.x156 = Var(within=Reals,bounds=(None,None),initialize=2.32)
m.x157 = Var(within=Reals,bounds=(None,None),initialize=2.4)
m.x158 = Var(within=Reals,bounds=(None,None),initialize=2.48)
m.x159 = Var(within=Reals,bounds=(None,None),initialize=2.56)
m.x160 = Var(within=Reals,bounds=(None,None),initialize=2.64)
m.x161 = Var(within=Reals,bounds=(None,None),initialize=2.72)
m.x162 = Var(within=Reals,bounds=(None,None),initialize=2.8)
m.x163 = Var(within=Reals,bounds=(None,None),initialize=2.88)
m.x164 = Var(within=Reals,bounds=(None,None),initialize=2.96)
m.x165 = Var(within=Reals,bounds=(None,None),initialize=3.04)
m.x166 = Var(within=Reals,bounds=(None,None),initialize=3.12)
m.x167 = Var(within=Reals,bounds=(None,None),initialize=3.2)
m.x168 = Var(within=Reals,bounds=(None,None),initialize=3.28)
m.x169 = Var(within=Reals,bounds=(None,None),initialize=3.36)
m.x170 = Var(within=Reals,bounds=(None,None),initialize=3.44)
m.x171 = Var(within=Reals,bounds=(None,None),initialize=3.52)
m.x172 = Var(within=Reals,bounds=(None,None),initialize=3.6)
m.x173 = Var(within=Reals,bounds=(None,None),initialize=3.68)
m.x174 = Var(within=Reals,bounds=(None,None),initialize=3.76)
m.x175 = Var(within=Reals,bounds=(None,None),initialize=3.84)
m.x176 = Var(within=Reals,bounds=(None,None),initialize=3.92)
m.x177 = Var(within=Reals,bounds=(None,None),initialize=4)
m.x178 = Var(within=Reals,bounds=(None,None),initialize=4.08)
m.x179 = Var(within=Reals,bounds=(None,None),initialize=4.16)
m.x180 = Var(within=Reals,bounds=(None,None),initialize=4.24)
m.x181 = Var(within=Reals,bounds=(None,None),initialize=4.32)
m.x182 = Var(within=Reals,bounds=(None,None),initialize=4.4)
m.x183 = Var(within=Reals,bounds=(None,None),initialize=4.48)
m.x184 = Var(within=Reals,bounds=(None,None),initialize=4.56)
m.x185 = Var(within=Reals,bounds=(None,None),initialize=4.64)
m.x186 = Var(within=Reals,bounds=(None,None),initialize=4.72)
m.x187 = Var(within=Reals,bounds=(None,None),initialize=4.8)
m.x188 = Var(within=Reals,bounds=(None,None),initialize=4.88)
m.x189 = Var(within=Reals,bounds=(None,None),initialize=4.96)
m.x190 = Var(within=Reals,bounds=(None,None),initialize=5.04)
m.x191 = Var(within=Reals,bounds=(None,None),initialize=5.12)
m.x192 = Var(within=Reals,bounds=(None,None),initialize=5.2)
m.x193 = Var(within=Reals,bounds=(None,None),initialize=5.28)
m.x194 = Var(within=Reals,bounds=(None,None),initialize=5.36)
m.x195 = Var(within=Reals,bounds=(None,None),initialize=5.44)
m.x196 = Var(within=Reals,bounds=(None,None),initialize=5.52)
m.x197 = Var(within=Reals,bounds=(None,None),initialize=5.6)
m.x198 = Var(within=Reals,bounds=(None,None),initialize=5.68)
m.x199 = Var(within=Reals,bounds=(None,None),initialize=5.76)
m.x200 = Var(within=Reals,bounds=(None,None),initialize=5.84)
m.x201 = Var(within=Reals,bounds=(None,None),initialize=5.92)
m.x202 = Var(within=Reals,bounds=(None,None),initialize=6)

m.obj = Objective(expr=0.005*(sqrt(1 + m.x102**2)*m.x1 + sqrt(1 + m.x103**2)*m.x2 + sqrt(1 + m.x103**2)*m.x2 + sqrt(1 + 
                       m.x104**2)*m.x3 + sqrt(1 + m.x104**2)*m.x3 + sqrt(1 + m.x105**2)*m.x4 + sqrt(1 + m.x105**2)*m.x4
                        + sqrt(1 + m.x106**2)*m.x5 + sqrt(1 + m.x106**2)*m.x5 + sqrt(1 + m.x107**2)*m.x6 + sqrt(1 + 
                       m.x107**2)*m.x6 + sqrt(1 + m.x108**2)*m.x7 + sqrt(1 + m.x108**2)*m.x7 + sqrt(1 + m.x109**2)*m.x8
                        + sqrt(1 + m.x109**2)*m.x8 + sqrt(1 + m.x110**2)*m.x9 + sqrt(1 + m.x110**2)*m.x9 + sqrt(1 + 
                       m.x111**2)*m.x10 + sqrt(1 + m.x111**2)*m.x10 + sqrt(1 + m.x112**2)*m.x11 + sqrt(1 + m.x112**2)*
                       m.x11 + sqrt(1 + m.x113**2)*m.x12 + sqrt(1 + m.x113**2)*m.x12 + sqrt(1 + m.x114**2)*m.x13 + sqrt(
                       1 + m.x114**2)*m.x13 + sqrt(1 + m.x115**2)*m.x14 + sqrt(1 + m.x115**2)*m.x14 + sqrt(1 + m.x116**2
                       )*m.x15 + sqrt(1 + m.x116**2)*m.x15 + sqrt(1 + m.x117**2)*m.x16 + sqrt(1 + m.x117**2)*m.x16 + 
                       sqrt(1 + m.x118**2)*m.x17 + sqrt(1 + m.x118**2)*m.x17 + sqrt(1 + m.x119**2)*m.x18 + sqrt(1 + 
                       m.x119**2)*m.x18 + sqrt(1 + m.x120**2)*m.x19 + sqrt(1 + m.x120**2)*m.x19 + sqrt(1 + m.x121**2)*
                       m.x20 + sqrt(1 + m.x121**2)*m.x20 + sqrt(1 + m.x122**2)*m.x21 + sqrt(1 + m.x122**2)*m.x21 + sqrt(
                       1 + m.x123**2)*m.x22 + sqrt(1 + m.x123**2)*m.x22 + sqrt(1 + m.x124**2)*m.x23 + sqrt(1 + m.x124**2
                       )*m.x23 + sqrt(1 + m.x125**2)*m.x24 + sqrt(1 + m.x125**2)*m.x24 + sqrt(1 + m.x126**2)*m.x25 + 
                       sqrt(1 + m.x126**2)*m.x25 + sqrt(1 + m.x127**2)*m.x26 + sqrt(1 + m.x127**2)*m.x26 + sqrt(1 + 
                       m.x128**2)*m.x27 + sqrt(1 + m.x128**2)*m.x27 + sqrt(1 + m.x129**2)*m.x28 + sqrt(1 + m.x129**2)*
                       m.x28 + sqrt(1 + m.x130**2)*m.x29 + sqrt(1 + m.x130**2)*m.x29 + sqrt(1 + m.x131**2)*m.x30 + sqrt(
                       1 + m.x131**2)*m.x30 + sqrt(1 + m.x132**2)*m.x31 + sqrt(1 + m.x132**2)*m.x31 + sqrt(1 + m.x133**2
                       )*m.x32 + sqrt(1 + m.x133**2)*m.x32 + sqrt(1 + m.x134**2)*m.x33 + sqrt(1 + m.x134**2)*m.x33 + 
                       sqrt(1 + m.x135**2)*m.x34 + sqrt(1 + m.x135**2)*m.x34 + sqrt(1 + m.x136**2)*m.x35 + sqrt(1 + 
                       m.x136**2)*m.x35 + sqrt(1 + m.x137**2)*m.x36 + sqrt(1 + m.x137**2)*m.x36 + sqrt(1 + m.x138**2)*
                       m.x37 + sqrt(1 + m.x138**2)*m.x37 + sqrt(1 + m.x139**2)*m.x38 + sqrt(1 + m.x139**2)*m.x38 + sqrt(
                       1 + m.x140**2)*m.x39 + sqrt(1 + m.x140**2)*m.x39 + sqrt(1 + m.x141**2)*m.x40 + sqrt(1 + m.x141**2
                       )*m.x40 + sqrt(1 + m.x142**2)*m.x41 + sqrt(1 + m.x142**2)*m.x41 + sqrt(1 + m.x143**2)*m.x42 + 
                       sqrt(1 + m.x143**2)*m.x42 + sqrt(1 + m.x144**2)*m.x43 + sqrt(1 + m.x144**2)*m.x43 + sqrt(1 + 
                       m.x145**2)*m.x44 + sqrt(1 + m.x145**2)*m.x44 + sqrt(1 + m.x146**2)*m.x45 + sqrt(1 + m.x146**2)*
                       m.x45 + sqrt(1 + m.x147**2)*m.x46 + sqrt(1 + m.x147**2)*m.x46 + sqrt(1 + m.x148**2)*m.x47 + sqrt(
                       1 + m.x148**2)*m.x47 + sqrt(1 + m.x149**2)*m.x48 + sqrt(1 + m.x149**2)*m.x48 + sqrt(1 + m.x150**2
                       )*m.x49 + sqrt(1 + m.x150**2)*m.x49 + sqrt(1 + m.x151**2)*m.x50 + sqrt(1 + m.x151**2)*m.x50 + 
                       sqrt(1 + m.x152**2)*m.x51 + sqrt(1 + m.x152**2)*m.x51 + sqrt(1 + m.x153**2)*m.x52 + sqrt(1 + 
                       m.x153**2)*m.x52 + sqrt(1 + m.x154**2)*m.x53 + sqrt(1 + m.x154**2)*m.x53 + sqrt(1 + m.x155**2)*
                       m.x54 + sqrt(1 + m.x155**2)*m.x54 + sqrt(1 + m.x156**2)*m.x55 + sqrt(1 + m.x156**2)*m.x55 + sqrt(
                       1 + m.x157**2)*m.x56 + sqrt(1 + m.x157**2)*m.x56 + sqrt(1 + m.x158**2)*m.x57 + sqrt(1 + m.x158**2
                       )*m.x57 + sqrt(1 + m.x159**2)*m.x58 + sqrt(1 + m.x159**2)*m.x58 + sqrt(1 + m.x160**2)*m.x59 + 
                       sqrt(1 + m.x160**2)*m.x59 + sqrt(1 + m.x161**2)*m.x60 + sqrt(1 + m.x161**2)*m.x60 + sqrt(1 + 
                       m.x162**2)*m.x61 + sqrt(1 + m.x162**2)*m.x61 + sqrt(1 + m.x163**2)*m.x62 + sqrt(1 + m.x163**2)*
                       m.x62 + sqrt(1 + m.x164**2)*m.x63 + sqrt(1 + m.x164**2)*m.x63 + sqrt(1 + m.x165**2)*m.x64 + sqrt(
                       1 + m.x165**2)*m.x64 + sqrt(1 + m.x166**2)*m.x65 + sqrt(1 + m.x166**2)*m.x65 + sqrt(1 + m.x167**2
                       )*m.x66 + sqrt(1 + m.x167**2)*m.x66 + sqrt(1 + m.x168**2)*m.x67 + sqrt(1 + m.x168**2)*m.x67 + 
                       sqrt(1 + m.x169**2)*m.x68 + sqrt(1 + m.x169**2)*m.x68 + sqrt(1 + m.x170**2)*m.x69 + sqrt(1 + 
                       m.x170**2)*m.x69 + sqrt(1 + m.x171**2)*m.x70 + sqrt(1 + m.x171**2)*m.x70 + sqrt(1 + m.x172**2)*
                       m.x71 + sqrt(1 + m.x172**2)*m.x71 + sqrt(1 + m.x173**2)*m.x72 + sqrt(1 + m.x173**2)*m.x72 + sqrt(
                       1 + m.x174**2)*m.x73 + sqrt(1 + m.x174**2)*m.x73 + sqrt(1 + m.x175**2)*m.x74 + sqrt(1 + m.x175**2
                       )*m.x74 + sqrt(1 + m.x176**2)*m.x75 + sqrt(1 + m.x176**2)*m.x75 + sqrt(1 + m.x177**2)*m.x76 + 
                       sqrt(1 + m.x177**2)*m.x76 + sqrt(1 + m.x178**2)*m.x77 + sqrt(1 + m.x178**2)*m.x77 + sqrt(1 + 
                       m.x179**2)*m.x78 + sqrt(1 + m.x179**2)*m.x78 + sqrt(1 + m.x180**2)*m.x79 + sqrt(1 + m.x180**2)*
                       m.x79 + sqrt(1 + m.x181**2)*m.x80 + sqrt(1 + m.x181**2)*m.x80 + sqrt(1 + m.x182**2)*m.x81 + sqrt(
                       1 + m.x182**2)*m.x81 + sqrt(1 + m.x183**2)*m.x82 + sqrt(1 + m.x183**2)*m.x82 + sqrt(1 + m.x184**2
                       )*m.x83 + sqrt(1 + m.x184**2)*m.x83 + sqrt(1 + m.x185**2)*m.x84 + sqrt(1 + m.x185**2)*m.x84 + 
                       sqrt(1 + m.x186**2)*m.x85 + sqrt(1 + m.x186**2)*m.x85 + sqrt(1 + m.x187**2)*m.x86 + sqrt(1 + 
                       m.x187**2)*m.x86 + sqrt(1 + m.x188**2)*m.x87 + sqrt(1 + m.x188**2)*m.x87 + sqrt(1 + m.x189**2)*
                       m.x88 + sqrt(1 + m.x189**2)*m.x88 + sqrt(1 + m.x190**2)*m.x89 + sqrt(1 + m.x190**2)*m.x89 + sqrt(
                       1 + m.x191**2)*m.x90 + sqrt(1 + m.x191**2)*m.x90 + sqrt(1 + m.x192**2)*m.x91 + sqrt(1 + m.x192**2
                       )*m.x91 + sqrt(1 + m.x193**2)*m.x92 + sqrt(1 + m.x193**2)*m.x92 + sqrt(1 + m.x194**2)*m.x93 + 
                       sqrt(1 + m.x194**2)*m.x93 + sqrt(1 + m.x195**2)*m.x94 + sqrt(1 + m.x195**2)*m.x94 + sqrt(1 + 
                       m.x196**2)*m.x95 + sqrt(1 + m.x196**2)*m.x95 + sqrt(1 + m.x197**2)*m.x96 + sqrt(1 + m.x197**2)*
                       m.x96 + sqrt(1 + m.x198**2)*m.x97 + sqrt(1 + m.x198**2)*m.x97 + sqrt(1 + m.x199**2)*m.x98 + sqrt(
                       1 + m.x199**2)*m.x98 + sqrt(1 + m.x200**2)*m.x99 + sqrt(1 + m.x200**2)*m.x99 + sqrt(1 + m.x201**2
                       )*m.x100 + sqrt(1 + m.x201**2)*m.x100 + sqrt(1 + m.x202**2)*m.x101), sense=minimize)

m.c2 = Constraint(expr= - m.x1 + m.x2 - 0.005*m.x102 - 0.005*m.x103 == 0)

m.c3 = Constraint(expr= - m.x2 + m.x3 - 0.005*m.x103 - 0.005*m.x104 == 0)

m.c4 = Constraint(expr= - m.x3 + m.x4 - 0.005*m.x104 - 0.005*m.x105 == 0)

m.c5 = Constraint(expr= - m.x4 + m.x5 - 0.005*m.x105 - 0.005*m.x106 == 0)

m.c6 = Constraint(expr= - m.x5 + m.x6 - 0.005*m.x106 - 0.005*m.x107 == 0)

m.c7 = Constraint(expr= - m.x6 + m.x7 - 0.005*m.x107 - 0.005*m.x108 == 0)

m.c8 = Constraint(expr= - m.x7 + m.x8 - 0.005*m.x108 - 0.005*m.x109 == 0)

m.c9 = Constraint(expr= - m.x8 + m.x9 - 0.005*m.x109 - 0.005*m.x110 == 0)

m.c10 = Constraint(expr= - m.x9 + m.x10 - 0.005*m.x110 - 0.005*m.x111 == 0)

m.c11 = Constraint(expr= - m.x10 + m.x11 - 0.005*m.x111 - 0.005*m.x112 == 0)

m.c12 = Constraint(expr= - m.x11 + m.x12 - 0.005*m.x112 - 0.005*m.x113 == 0)

m.c13 = Constraint(expr= - m.x12 + m.x13 - 0.005*m.x113 - 0.005*m.x114 == 0)

m.c14 = Constraint(expr= - m.x13 + m.x14 - 0.005*m.x114 - 0.005*m.x115 == 0)

m.c15 = Constraint(expr= - m.x14 + m.x15 - 0.005*m.x115 - 0.005*m.x116 == 0)

m.c16 = Constraint(expr= - m.x15 + m.x16 - 0.005*m.x116 - 0.005*m.x117 == 0)

m.c17 = Constraint(expr= - m.x16 + m.x17 - 0.005*m.x117 - 0.005*m.x118 == 0)

m.c18 = Constraint(expr= - m.x17 + m.x18 - 0.005*m.x118 - 0.005*m.x119 == 0)

m.c19 = Constraint(expr= - m.x18 + m.x19 - 0.005*m.x119 - 0.005*m.x120 == 0)

m.c20 = Constraint(expr= - m.x19 + m.x20 - 0.005*m.x120 - 0.005*m.x121 == 0)

m.c21 = Constraint(expr= - m.x20 + m.x21 - 0.005*m.x121 - 0.005*m.x122 == 0)

m.c22 = Constraint(expr= - m.x21 + m.x22 - 0.005*m.x122 - 0.005*m.x123 == 0)

m.c23 = Constraint(expr= - m.x22 + m.x23 - 0.005*m.x123 - 0.005*m.x124 == 0)

m.c24 = Constraint(expr= - m.x23 + m.x24 - 0.005*m.x124 - 0.005*m.x125 == 0)

m.c25 = Constraint(expr= - m.x24 + m.x25 - 0.005*m.x125 - 0.005*m.x126 == 0)

m.c26 = Constraint(expr= - m.x25 + m.x26 - 0.005*m.x126 - 0.005*m.x127 == 0)

m.c27 = Constraint(expr= - m.x26 + m.x27 - 0.005*m.x127 - 0.005*m.x128 == 0)

m.c28 = Constraint(expr= - m.x27 + m.x28 - 0.005*m.x128 - 0.005*m.x129 == 0)

m.c29 = Constraint(expr= - m.x28 + m.x29 - 0.005*m.x129 - 0.005*m.x130 == 0)

m.c30 = Constraint(expr= - m.x29 + m.x30 - 0.005*m.x130 - 0.005*m.x131 == 0)

m.c31 = Constraint(expr= - m.x30 + m.x31 - 0.005*m.x131 - 0.005*m.x132 == 0)

m.c32 = Constraint(expr= - m.x31 + m.x32 - 0.005*m.x132 - 0.005*m.x133 == 0)

m.c33 = Constraint(expr= - m.x32 + m.x33 - 0.005*m.x133 - 0.005*m.x134 == 0)

m.c34 = Constraint(expr= - m.x33 + m.x34 - 0.005*m.x134 - 0.005*m.x135 == 0)

m.c35 = Constraint(expr= - m.x34 + m.x35 - 0.005*m.x135 - 0.005*m.x136 == 0)

m.c36 = Constraint(expr= - m.x35 + m.x36 - 0.005*m.x136 - 0.005*m.x137 == 0)

m.c37 = Constraint(expr= - m.x36 + m.x37 - 0.005*m.x137 - 0.005*m.x138 == 0)

m.c38 = Constraint(expr= - m.x37 + m.x38 - 0.005*m.x138 - 0.005*m.x139 == 0)

m.c39 = Constraint(expr= - m.x38 + m.x39 - 0.005*m.x139 - 0.005*m.x140 == 0)

m.c40 = Constraint(expr= - m.x39 + m.x40 - 0.005*m.x140 - 0.005*m.x141 == 0)

m.c41 = Constraint(expr= - m.x40 + m.x41 - 0.005*m.x141 - 0.005*m.x142 == 0)

m.c42 = Constraint(expr= - m.x41 + m.x42 - 0.005*m.x142 - 0.005*m.x143 == 0)

m.c43 = Constraint(expr= - m.x42 + m.x43 - 0.005*m.x143 - 0.005*m.x144 == 0)

m.c44 = Constraint(expr= - m.x43 + m.x44 - 0.005*m.x144 - 0.005*m.x145 == 0)

m.c45 = Constraint(expr= - m.x44 + m.x45 - 0.005*m.x145 - 0.005*m.x146 == 0)

m.c46 = Constraint(expr= - m.x45 + m.x46 - 0.005*m.x146 - 0.005*m.x147 == 0)

m.c47 = Constraint(expr= - m.x46 + m.x47 - 0.005*m.x147 - 0.005*m.x148 == 0)

m.c48 = Constraint(expr= - m.x47 + m.x48 - 0.005*m.x148 - 0.005*m.x149 == 0)

m.c49 = Constraint(expr= - m.x48 + m.x49 - 0.005*m.x149 - 0.005*m.x150 == 0)

m.c50 = Constraint(expr= - m.x49 + m.x50 - 0.005*m.x150 - 0.005*m.x151 == 0)

m.c51 = Constraint(expr= - m.x50 + m.x51 - 0.005*m.x151 - 0.005*m.x152 == 0)

m.c52 = Constraint(expr= - m.x51 + m.x52 - 0.005*m.x152 - 0.005*m.x153 == 0)

m.c53 = Constraint(expr= - m.x52 + m.x53 - 0.005*m.x153 - 0.005*m.x154 == 0)

m.c54 = Constraint(expr= - m.x53 + m.x54 - 0.005*m.x154 - 0.005*m.x155 == 0)

m.c55 = Constraint(expr= - m.x54 + m.x55 - 0.005*m.x155 - 0.005*m.x156 == 0)

m.c56 = Constraint(expr= - m.x55 + m.x56 - 0.005*m.x156 - 0.005*m.x157 == 0)

m.c57 = Constraint(expr= - m.x56 + m.x57 - 0.005*m.x157 - 0.005*m.x158 == 0)

m.c58 = Constraint(expr= - m.x57 + m.x58 - 0.005*m.x158 - 0.005*m.x159 == 0)

m.c59 = Constraint(expr= - m.x58 + m.x59 - 0.005*m.x159 - 0.005*m.x160 == 0)

m.c60 = Constraint(expr= - m.x59 + m.x60 - 0.005*m.x160 - 0.005*m.x161 == 0)

m.c61 = Constraint(expr= - m.x60 + m.x61 - 0.005*m.x161 - 0.005*m.x162 == 0)

m.c62 = Constraint(expr= - m.x61 + m.x62 - 0.005*m.x162 - 0.005*m.x163 == 0)

m.c63 = Constraint(expr= - m.x62 + m.x63 - 0.005*m.x163 - 0.005*m.x164 == 0)

m.c64 = Constraint(expr= - m.x63 + m.x64 - 0.005*m.x164 - 0.005*m.x165 == 0)

m.c65 = Constraint(expr= - m.x64 + m.x65 - 0.005*m.x165 - 0.005*m.x166 == 0)

m.c66 = Constraint(expr= - m.x65 + m.x66 - 0.005*m.x166 - 0.005*m.x167 == 0)

m.c67 = Constraint(expr= - m.x66 + m.x67 - 0.005*m.x167 - 0.005*m.x168 == 0)

m.c68 = Constraint(expr= - m.x67 + m.x68 - 0.005*m.x168 - 0.005*m.x169 == 0)

m.c69 = Constraint(expr= - m.x68 + m.x69 - 0.005*m.x169 - 0.005*m.x170 == 0)

m.c70 = Constraint(expr= - m.x69 + m.x70 - 0.005*m.x170 - 0.005*m.x171 == 0)

m.c71 = Constraint(expr= - m.x70 + m.x71 - 0.005*m.x171 - 0.005*m.x172 == 0)

m.c72 = Constraint(expr= - m.x71 + m.x72 - 0.005*m.x172 - 0.005*m.x173 == 0)

m.c73 = Constraint(expr= - m.x72 + m.x73 - 0.005*m.x173 - 0.005*m.x174 == 0)

m.c74 = Constraint(expr= - m.x73 + m.x74 - 0.005*m.x174 - 0.005*m.x175 == 0)

m.c75 = Constraint(expr= - m.x74 + m.x75 - 0.005*m.x175 - 0.005*m.x176 == 0)

m.c76 = Constraint(expr= - m.x75 + m.x76 - 0.005*m.x176 - 0.005*m.x177 == 0)

m.c77 = Constraint(expr= - m.x76 + m.x77 - 0.005*m.x177 - 0.005*m.x178 == 0)

m.c78 = Constraint(expr= - m.x77 + m.x78 - 0.005*m.x178 - 0.005*m.x179 == 0)

m.c79 = Constraint(expr= - m.x78 + m.x79 - 0.005*m.x179 - 0.005*m.x180 == 0)

m.c80 = Constraint(expr= - m.x79 + m.x80 - 0.005*m.x180 - 0.005*m.x181 == 0)

m.c81 = Constraint(expr= - m.x80 + m.x81 - 0.005*m.x181 - 0.005*m.x182 == 0)

m.c82 = Constraint(expr= - m.x81 + m.x82 - 0.005*m.x182 - 0.005*m.x183 == 0)

m.c83 = Constraint(expr= - m.x82 + m.x83 - 0.005*m.x183 - 0.005*m.x184 == 0)

m.c84 = Constraint(expr= - m.x83 + m.x84 - 0.005*m.x184 - 0.005*m.x185 == 0)

m.c85 = Constraint(expr= - m.x84 + m.x85 - 0.005*m.x185 - 0.005*m.x186 == 0)

m.c86 = Constraint(expr= - m.x85 + m.x86 - 0.005*m.x186 - 0.005*m.x187 == 0)

m.c87 = Constraint(expr= - m.x86 + m.x87 - 0.005*m.x187 - 0.005*m.x188 == 0)

m.c88 = Constraint(expr= - m.x87 + m.x88 - 0.005*m.x188 - 0.005*m.x189 == 0)

m.c89 = Constraint(expr= - m.x88 + m.x89 - 0.005*m.x189 - 0.005*m.x190 == 0)

m.c90 = Constraint(expr= - m.x89 + m.x90 - 0.005*m.x190 - 0.005*m.x191 == 0)

m.c91 = Constraint(expr= - m.x90 + m.x91 - 0.005*m.x191 - 0.005*m.x192 == 0)

m.c92 = Constraint(expr= - m.x91 + m.x92 - 0.005*m.x192 - 0.005*m.x193 == 0)

m.c93 = Constraint(expr= - m.x92 + m.x93 - 0.005*m.x193 - 0.005*m.x194 == 0)

m.c94 = Constraint(expr= - m.x93 + m.x94 - 0.005*m.x194 - 0.005*m.x195 == 0)

m.c95 = Constraint(expr= - m.x94 + m.x95 - 0.005*m.x195 - 0.005*m.x196 == 0)

m.c96 = Constraint(expr= - m.x95 + m.x96 - 0.005*m.x196 - 0.005*m.x197 == 0)

m.c97 = Constraint(expr= - m.x96 + m.x97 - 0.005*m.x197 - 0.005*m.x198 == 0)

m.c98 = Constraint(expr= - m.x97 + m.x98 - 0.005*m.x198 - 0.005*m.x199 == 0)

m.c99 = Constraint(expr= - m.x98 + m.x99 - 0.005*m.x199 - 0.005*m.x200 == 0)

m.c100 = Constraint(expr= - m.x99 + m.x100 - 0.005*m.x200 - 0.005*m.x201 == 0)

m.c101 = Constraint(expr= - m.x100 + m.x101 - 0.005*m.x201 - 0.005*m.x202 == 0)

m.c102 = Constraint(expr=0.005*(sqrt(1 + m.x102**2) + sqrt(1 + m.x103**2) + sqrt(1 + m.x103**2) + sqrt(1 + m.x104**2) + 
                         sqrt(1 + m.x104**2) + sqrt(1 + m.x105**2) + sqrt(1 + m.x105**2) + sqrt(1 + m.x106**2) + sqrt(1
                          + m.x106**2) + sqrt(1 + m.x107**2) + sqrt(1 + m.x107**2) + sqrt(1 + m.x108**2) + sqrt(1 + 
                         m.x108**2) + sqrt(1 + m.x109**2) + sqrt(1 + m.x109**2) + sqrt(1 + m.x110**2) + sqrt(1 + m.x110
                         **2) + sqrt(1 + m.x111**2) + sqrt(1 + m.x111**2) + sqrt(1 + m.x112**2) + sqrt(1 + m.x112**2) + 
                         sqrt(1 + m.x113**2) + sqrt(1 + m.x113**2) + sqrt(1 + m.x114**2) + sqrt(1 + m.x114**2) + sqrt(1
                          + m.x115**2) + sqrt(1 + m.x115**2) + sqrt(1 + m.x116**2) + sqrt(1 + m.x116**2) + sqrt(1 + 
                         m.x117**2) + sqrt(1 + m.x117**2) + sqrt(1 + m.x118**2) + sqrt(1 + m.x118**2) + sqrt(1 + m.x119
                         **2) + sqrt(1 + m.x119**2) + sqrt(1 + m.x120**2) + sqrt(1 + m.x120**2) + sqrt(1 + m.x121**2) + 
                         sqrt(1 + m.x121**2) + sqrt(1 + m.x122**2) + sqrt(1 + m.x122**2) + sqrt(1 + m.x123**2) + sqrt(1
                          + m.x123**2) + sqrt(1 + m.x124**2) + sqrt(1 + m.x124**2) + sqrt(1 + m.x125**2) + sqrt(1 + 
                         m.x125**2) + sqrt(1 + m.x126**2) + sqrt(1 + m.x126**2) + sqrt(1 + m.x127**2) + sqrt(1 + m.x127
                         **2) + sqrt(1 + m.x128**2) + sqrt(1 + m.x128**2) + sqrt(1 + m.x129**2) + sqrt(1 + m.x129**2) + 
                         sqrt(1 + m.x130**2) + sqrt(1 + m.x130**2) + sqrt(1 + m.x131**2) + sqrt(1 + m.x131**2) + sqrt(1
                          + m.x132**2) + sqrt(1 + m.x132**2) + sqrt(1 + m.x133**2) + sqrt(1 + m.x133**2) + sqrt(1 + 
                         m.x134**2) + sqrt(1 + m.x134**2) + sqrt(1 + m.x135**2) + sqrt(1 + m.x135**2) + sqrt(1 + m.x136
                         **2) + sqrt(1 + m.x136**2) + sqrt(1 + m.x137**2) + sqrt(1 + m.x137**2) + sqrt(1 + m.x138**2) + 
                         sqrt(1 + m.x138**2) + sqrt(1 + m.x139**2) + sqrt(1 + m.x139**2) + sqrt(1 + m.x140**2) + sqrt(1
                          + m.x140**2) + sqrt(1 + m.x141**2) + sqrt(1 + m.x141**2) + sqrt(1 + m.x142**2) + sqrt(1 + 
                         m.x142**2) + sqrt(1 + m.x143**2) + sqrt(1 + m.x143**2) + sqrt(1 + m.x144**2) + sqrt(1 + m.x144
                         **2) + sqrt(1 + m.x145**2) + sqrt(1 + m.x145**2) + sqrt(1 + m.x146**2) + sqrt(1 + m.x146**2) + 
                         sqrt(1 + m.x147**2) + sqrt(1 + m.x147**2) + sqrt(1 + m.x148**2) + sqrt(1 + m.x148**2) + sqrt(1
                          + m.x149**2) + sqrt(1 + m.x149**2) + sqrt(1 + m.x150**2) + sqrt(1 + m.x150**2) + sqrt(1 + 
                         m.x151**2) + sqrt(1 + m.x151**2) + sqrt(1 + m.x152**2) + sqrt(1 + m.x152**2) + sqrt(1 + m.x153
                         **2) + sqrt(1 + m.x153**2) + sqrt(1 + m.x154**2) + sqrt(1 + m.x154**2) + sqrt(1 + m.x155**2) + 
                         sqrt(1 + m.x155**2) + sqrt(1 + m.x156**2) + sqrt(1 + m.x156**2) + sqrt(1 + m.x157**2) + sqrt(1
                          + m.x157**2) + sqrt(1 + m.x158**2) + sqrt(1 + m.x158**2) + sqrt(1 + m.x159**2) + sqrt(1 + 
                         m.x159**2) + sqrt(1 + m.x160**2) + sqrt(1 + m.x160**2) + sqrt(1 + m.x161**2) + sqrt(1 + m.x161
                         **2) + sqrt(1 + m.x162**2) + sqrt(1 + m.x162**2) + sqrt(1 + m.x163**2) + sqrt(1 + m.x163**2) + 
                         sqrt(1 + m.x164**2) + sqrt(1 + m.x164**2) + sqrt(1 + m.x165**2) + sqrt(1 + m.x165**2) + sqrt(1
                          + m.x166**2) + sqrt(1 + m.x166**2) + sqrt(1 + m.x167**2) + sqrt(1 + m.x167**2) + sqrt(1 + 
                         m.x168**2) + sqrt(1 + m.x168**2) + sqrt(1 + m.x169**2) + sqrt(1 + m.x169**2) + sqrt(1 + m.x170
                         **2) + sqrt(1 + m.x170**2) + sqrt(1 + m.x171**2) + sqrt(1 + m.x171**2) + sqrt(1 + m.x172**2) + 
                         sqrt(1 + m.x172**2) + sqrt(1 + m.x173**2) + sqrt(1 + m.x173**2) + sqrt(1 + m.x174**2) + sqrt(1
                          + m.x174**2) + sqrt(1 + m.x175**2) + sqrt(1 + m.x175**2) + sqrt(1 + m.x176**2) + sqrt(1 + 
                         m.x176**2) + sqrt(1 + m.x177**2) + sqrt(1 + m.x177**2) + sqrt(1 + m.x178**2) + sqrt(1 + m.x178
                         **2) + sqrt(1 + m.x179**2) + sqrt(1 + m.x179**2) + sqrt(1 + m.x180**2) + sqrt(1 + m.x180**2) + 
                         sqrt(1 + m.x181**2) + sqrt(1 + m.x181**2) + sqrt(1 + m.x182**2) + sqrt(1 + m.x182**2) + sqrt(1
                          + m.x183**2) + sqrt(1 + m.x183**2) + sqrt(1 + m.x184**2) + sqrt(1 + m.x184**2) + sqrt(1 + 
                         m.x185**2) + sqrt(1 + m.x185**2) + sqrt(1 + m.x186**2) + sqrt(1 + m.x186**2) + sqrt(1 + m.x187
                         **2) + sqrt(1 + m.x187**2) + sqrt(1 + m.x188**2) + sqrt(1 + m.x188**2) + sqrt(1 + m.x189**2) + 
                         sqrt(1 + m.x189**2) + sqrt(1 + m.x190**2) + sqrt(1 + m.x190**2) + sqrt(1 + m.x191**2) + sqrt(1
                          + m.x191**2) + sqrt(1 + m.x192**2) + sqrt(1 + m.x192**2) + sqrt(1 + m.x193**2) + sqrt(1 + 
                         m.x193**2) + sqrt(1 + m.x194**2) + sqrt(1 + m.x194**2) + sqrt(1 + m.x195**2) + sqrt(1 + m.x195
                         **2) + sqrt(1 + m.x196**2) + sqrt(1 + m.x196**2) + sqrt(1 + m.x197**2) + sqrt(1 + m.x197**2) + 
                         sqrt(1 + m.x198**2) + sqrt(1 + m.x198**2) + sqrt(1 + m.x199**2) + sqrt(1 + m.x199**2) + sqrt(1
                          + m.x200**2) + sqrt(1 + m.x200**2) + sqrt(1 + m.x201**2) + sqrt(1 + m.x201**2) + sqrt(1 + 
                         m.x202**2)) == 4)
