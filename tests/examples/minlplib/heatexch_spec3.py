#  MINLP written by GAMS Convert at 04/21/18 13:52:23
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        251       51       30      170        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        261      201       60        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1101      931      170        0
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
m.b28 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b29 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b30 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b31 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b32 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b33 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b34 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b35 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b36 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b37 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b38 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b39 = Var(within=Binary,bounds=(0,1),initialize=0)
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
m.x61 = Var(within=Reals,bounds=(93.3,160),initialize=160)
m.x62 = Var(within=Reals,bounds=(93.3,160),initialize=160)
m.x63 = Var(within=Reals,bounds=(93.3,160),initialize=160)
m.x64 = Var(within=Reals,bounds=(137.8,248.9),initialize=248.9)
m.x65 = Var(within=Reals,bounds=(137.8,248.9),initialize=248.9)
m.x66 = Var(within=Reals,bounds=(137.8,248.9),initialize=248.9)
m.x67 = Var(within=Reals,bounds=(65.6,226.7),initialize=226.7)
m.x68 = Var(within=Reals,bounds=(65.6,226.7),initialize=226.7)
m.x69 = Var(within=Reals,bounds=(65.6,226.7),initialize=226.7)
m.x70 = Var(within=Reals,bounds=(148.9,271.1),initialize=271.1)
m.x71 = Var(within=Reals,bounds=(148.9,271.1),initialize=271.1)
m.x72 = Var(within=Reals,bounds=(148.9,271.1),initialize=271.1)
m.x73 = Var(within=Reals,bounds=(65.6,198.9),initialize=198.9)
m.x74 = Var(within=Reals,bounds=(65.6,198.9),initialize=198.9)
m.x75 = Var(within=Reals,bounds=(65.6,198.9),initialize=198.9)
m.x76 = Var(within=Reals,bounds=(60,160),initialize=60)
m.x77 = Var(within=Reals,bounds=(60,160),initialize=60)
m.x78 = Var(within=Reals,bounds=(60,160),initialize=60)
m.x79 = Var(within=Reals,bounds=(115.6,221.7),initialize=115.6)
m.x80 = Var(within=Reals,bounds=(115.6,221.7),initialize=115.6)
m.x81 = Var(within=Reals,bounds=(115.6,221.7),initialize=115.6)
m.x82 = Var(within=Reals,bounds=(37.8,221.1),initialize=37.8)
m.x83 = Var(within=Reals,bounds=(37.8,221.1),initialize=37.8)
m.x84 = Var(within=Reals,bounds=(37.8,221.1),initialize=37.8)
m.x85 = Var(within=Reals,bounds=(82.2,176.7),initialize=82.2)
m.x86 = Var(within=Reals,bounds=(82.2,176.7),initialize=82.2)
m.x87 = Var(within=Reals,bounds=(82.2,176.7),initialize=82.2)
m.x88 = Var(within=Reals,bounds=(93.3,204.4),initialize=93.3)
m.x89 = Var(within=Reals,bounds=(93.3,204.4),initialize=93.3)
m.x90 = Var(within=Reals,bounds=(93.3,204.4),initialize=93.3)
m.x91 = Var(within=Reals,bounds=(0,None),initialize=586.96)
m.x92 = Var(within=Reals,bounds=(0,None),initialize=586.96)
m.x93 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x94 = Var(within=Reals,bounds=(0,None),initialize=586.96)
m.x95 = Var(within=Reals,bounds=(0,None),initialize=586.96)
m.x96 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x97 = Var(within=Reals,bounds=(0,None),initialize=586.96)
m.x98 = Var(within=Reals,bounds=(0,None),initialize=586.96)
m.x99 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x100 = Var(within=Reals,bounds=(0,None),initialize=586.96)
m.x101 = Var(within=Reals,bounds=(0,None),initialize=586.96)
m.x102 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x103 = Var(within=Reals,bounds=(0,None),initialize=586.96)
m.x104 = Var(within=Reals,bounds=(0,None),initialize=586.96)
m.x105 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x106 = Var(within=Reals,bounds=(0,None),initialize=760)
m.x107 = Var(within=Reals,bounds=(0,None),initialize=760)
m.x108 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x109 = Var(within=Reals,bounds=(0,None),initialize=647.21)
m.x110 = Var(within=Reals,bounds=(0,None),initialize=647.21)
m.x111 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x112 = Var(within=Reals,bounds=(0,None),initialize=1177.66)
m.x113 = Var(within=Reals,bounds=(0,None),initialize=1177.66)
m.x114 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x115 = Var(within=Reals,bounds=(0,None),initialize=1177.66)
m.x116 = Var(within=Reals,bounds=(0,None),initialize=1177.66)
m.x117 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x118 = Var(within=Reals,bounds=(0,None),initialize=1177.66)
m.x119 = Var(within=Reals,bounds=(0,None),initialize=1177.66)
m.x120 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x121 = Var(within=Reals,bounds=(0,None),initialize=760)
m.x122 = Var(within=Reals,bounds=(0,None),initialize=760)
m.x123 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x124 = Var(within=Reals,bounds=(0,None),initialize=647.21)
m.x125 = Var(within=Reals,bounds=(0,None),initialize=647.21)
m.x126 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x127 = Var(within=Reals,bounds=(0,None),initialize=1539.72)
m.x128 = Var(within=Reals,bounds=(0,None),initialize=1539.72)
m.x129 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x130 = Var(within=Reals,bounds=(0,None),initialize=1634.85)
m.x131 = Var(within=Reals,bounds=(0,None),initialize=1634.85)
m.x132 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x133 = Var(within=Reals,bounds=(0,None),initialize=1544.29)
m.x134 = Var(within=Reals,bounds=(0,None),initialize=1544.29)
m.x135 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x136 = Var(within=Reals,bounds=(0,None),initialize=760)
m.x137 = Var(within=Reals,bounds=(0,None),initialize=760)
m.x138 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x139 = Var(within=Reals,bounds=(0,None),initialize=647.21)
m.x140 = Var(within=Reals,bounds=(0,None),initialize=647.21)
m.x141 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x142 = Var(within=Reals,bounds=(0,None),initialize=1539.72)
m.x143 = Var(within=Reals,bounds=(0,None),initialize=1539.72)
m.x144 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x145 = Var(within=Reals,bounds=(0,None),initialize=1539.72)
m.x146 = Var(within=Reals,bounds=(0,None),initialize=1539.72)
m.x147 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x148 = Var(within=Reals,bounds=(0,None),initialize=1539.72)
m.x149 = Var(within=Reals,bounds=(0,None),initialize=1539.72)
m.x150 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x151 = Var(within=Reals,bounds=(0,None),initialize=760)
m.x152 = Var(within=Reals,bounds=(0,None),initialize=760)
m.x153 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x154 = Var(within=Reals,bounds=(0,None),initialize=647.21)
m.x155 = Var(within=Reals,bounds=(0,None),initialize=647.21)
m.x156 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x157 = Var(within=Reals,bounds=(0,None),initialize=1539.72)
m.x158 = Var(within=Reals,bounds=(0,None),initialize=1539.72)
m.x159 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x160 = Var(within=Reals,bounds=(0,None),initialize=1634.85)
m.x161 = Var(within=Reals,bounds=(0,None),initialize=1634.85)
m.x162 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x163 = Var(within=Reals,bounds=(0,None),initialize=1544.29)
m.x164 = Var(within=Reals,bounds=(0,None),initialize=1544.29)
m.x165 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x166 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x167 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x168 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x169 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x170 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x171 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x172 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x173 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x174 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x175 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x176 = Var(within=Reals,bounds=(10,None),initialize=100)
m.x177 = Var(within=Reals,bounds=(10,None),initialize=100)
m.x178 = Var(within=Reals,bounds=(10,None),initialize=100)
m.x179 = Var(within=Reals,bounds=(10,None),initialize=44.4)
m.x180 = Var(within=Reals,bounds=(10,None),initialize=44.4)
m.x181 = Var(within=Reals,bounds=(10,None),initialize=44.4)
m.x182 = Var(within=Reals,bounds=(10,None),initialize=122.2)
m.x183 = Var(within=Reals,bounds=(10,None),initialize=122.2)
m.x184 = Var(within=Reals,bounds=(10,None),initialize=122.2)
m.x185 = Var(within=Reals,bounds=(10,None),initialize=77.8)
m.x186 = Var(within=Reals,bounds=(10,None),initialize=77.8)
m.x187 = Var(within=Reals,bounds=(10,None),initialize=77.8)
m.x188 = Var(within=Reals,bounds=(10,None),initialize=66.7)
m.x189 = Var(within=Reals,bounds=(10,None),initialize=66.7)
m.x190 = Var(within=Reals,bounds=(10,None),initialize=66.7)
m.x191 = Var(within=Reals,bounds=(10,None),initialize=188.9)
m.x192 = Var(within=Reals,bounds=(10,None),initialize=188.9)
m.x193 = Var(within=Reals,bounds=(10,None),initialize=188.9)
m.x194 = Var(within=Reals,bounds=(10,None),initialize=133.3)
m.x195 = Var(within=Reals,bounds=(10,None),initialize=133.3)
m.x196 = Var(within=Reals,bounds=(10,None),initialize=133.3)
m.x197 = Var(within=Reals,bounds=(10,None),initialize=211.1)
m.x198 = Var(within=Reals,bounds=(10,None),initialize=211.1)
m.x199 = Var(within=Reals,bounds=(10,None),initialize=211.1)
m.x200 = Var(within=Reals,bounds=(10,None),initialize=166.7)
m.x201 = Var(within=Reals,bounds=(10,None),initialize=166.7)
m.x202 = Var(within=Reals,bounds=(10,None),initialize=166.7)
m.x203 = Var(within=Reals,bounds=(10,None),initialize=155.6)
m.x204 = Var(within=Reals,bounds=(10,None),initialize=155.6)
m.x205 = Var(within=Reals,bounds=(10,None),initialize=155.6)
m.x206 = Var(within=Reals,bounds=(10,None),initialize=166.7)
m.x207 = Var(within=Reals,bounds=(10,None),initialize=166.7)
m.x208 = Var(within=Reals,bounds=(10,None),initialize=166.7)
m.x209 = Var(within=Reals,bounds=(10,None),initialize=111.1)
m.x210 = Var(within=Reals,bounds=(10,None),initialize=111.1)
m.x211 = Var(within=Reals,bounds=(10,None),initialize=111.1)
m.x212 = Var(within=Reals,bounds=(10,None),initialize=188.9)
m.x213 = Var(within=Reals,bounds=(10,None),initialize=188.9)
m.x214 = Var(within=Reals,bounds=(10,None),initialize=188.9)
m.x215 = Var(within=Reals,bounds=(10,None),initialize=144.5)
m.x216 = Var(within=Reals,bounds=(10,None),initialize=144.5)
m.x217 = Var(within=Reals,bounds=(10,None),initialize=144.5)
m.x218 = Var(within=Reals,bounds=(10,None),initialize=133.4)
m.x219 = Var(within=Reals,bounds=(10,None),initialize=133.4)
m.x220 = Var(within=Reals,bounds=(10,None),initialize=133.4)
m.x221 = Var(within=Reals,bounds=(10,None),initialize=211.1)
m.x222 = Var(within=Reals,bounds=(10,None),initialize=211.1)
m.x223 = Var(within=Reals,bounds=(10,None),initialize=211.1)
m.x224 = Var(within=Reals,bounds=(10,None),initialize=155.5)
m.x225 = Var(within=Reals,bounds=(10,None),initialize=155.5)
m.x226 = Var(within=Reals,bounds=(10,None),initialize=155.5)
m.x227 = Var(within=Reals,bounds=(10,None),initialize=233.3)
m.x228 = Var(within=Reals,bounds=(10,None),initialize=233.3)
m.x229 = Var(within=Reals,bounds=(10,None),initialize=233.3)
m.x230 = Var(within=Reals,bounds=(10,None),initialize=188.9)
m.x231 = Var(within=Reals,bounds=(10,None),initialize=188.9)
m.x232 = Var(within=Reals,bounds=(10,None),initialize=188.9)
m.x233 = Var(within=Reals,bounds=(10,None),initialize=177.8)
m.x234 = Var(within=Reals,bounds=(10,None),initialize=177.8)
m.x235 = Var(within=Reals,bounds=(10,None),initialize=177.8)
m.x236 = Var(within=Reals,bounds=(10,None),initialize=138.9)
m.x237 = Var(within=Reals,bounds=(10,None),initialize=138.9)
m.x238 = Var(within=Reals,bounds=(10,None),initialize=138.9)
m.x239 = Var(within=Reals,bounds=(10,None),initialize=83.3)
m.x240 = Var(within=Reals,bounds=(10,None),initialize=83.3)
m.x241 = Var(within=Reals,bounds=(10,None),initialize=83.3)
m.x242 = Var(within=Reals,bounds=(10,None),initialize=161.1)
m.x243 = Var(within=Reals,bounds=(10,None),initialize=161.1)
m.x244 = Var(within=Reals,bounds=(10,None),initialize=161.1)
m.x245 = Var(within=Reals,bounds=(10,None),initialize=116.7)
m.x246 = Var(within=Reals,bounds=(10,None),initialize=116.7)
m.x247 = Var(within=Reals,bounds=(10,None),initialize=116.7)
m.x248 = Var(within=Reals,bounds=(10,None),initialize=105.6)
m.x249 = Var(within=Reals,bounds=(10,None),initialize=105.6)
m.x250 = Var(within=Reals,bounds=(10,None),initialize=105.6)
m.x251 = Var(within=Reals,bounds=(10,None),initialize=120)
m.x252 = Var(within=Reals,bounds=(10,None),initialize=208.9)
m.x253 = Var(within=Reals,bounds=(10,None),initialize=186.7)
m.x254 = Var(within=Reals,bounds=(10,None),initialize=231.1)
m.x255 = Var(within=Reals,bounds=(10,None),initialize=158.9)
m.x256 = Var(within=Reals,bounds=(10,None),initialize=180)
m.x257 = Var(within=Reals,bounds=(10,None),initialize=124.4)
m.x258 = Var(within=Reals,bounds=(10,None),initialize=202.2)
m.x259 = Var(within=Reals,bounds=(10,None),initialize=157.8)
m.x260 = Var(within=Reals,bounds=(10,None),initialize=146.7)

m.obj = Objective(expr=146*((1e-6 + 1.17647058823529*m.x91/(1e-6 + (1e-6 + 0.5*m.x176*m.x177*(m.x176 + m.x177))**0.33333
                       ))**0.6 + (1e-6 + 1.17647058823529*m.x92/(1e-6 + (1e-6 + 0.5*m.x177*m.x178*(m.x177 + m.x178))**
                       0.33333))**0.6 + (1e-6 + 117.629878654828*m.x93)**0.6 + (1e-6 + 1.17647058823529*m.x94/(1e-6 + (
                       1e-6 + 0.5*m.x179*m.x180*(m.x179 + m.x180))**0.33333))**0.6 + (1e-6 + 1.17647058823529*m.x95/(
                       1e-6 + (1e-6 + 0.5*m.x180*m.x181*(m.x180 + m.x181))**0.33333))**0.6 + (1e-6 + 117.629878654828*
                       m.x96)**0.6 + (1e-6 + 1.17647058823529*m.x97/(1e-6 + (1e-6 + 0.5*m.x182*m.x183*(m.x182 + m.x183))
                       **0.33333))**0.6 + (1e-6 + 1.17647058823529*m.x98/(1e-6 + (1e-6 + 0.5*m.x183*m.x184*(m.x183 + 
                       m.x184))**0.33333))**0.6 + (1e-6 + 117.629878654828*m.x99)**0.6 + (1e-6 + 1.17647058823529*m.x100
                       /(1e-6 + (1e-6 + 0.5*m.x185*m.x186*(m.x185 + m.x186))**0.33333))**0.6 + (1e-6 + 1.17647058823529*
                       m.x101/(1e-6 + (1e-6 + 0.5*m.x186*m.x187*(m.x186 + m.x187))**0.33333))**0.6 + (1e-6 + 
                       117.629878654828*m.x102)**0.6 + (1e-6 + 1.17647058823529*m.x103/(1e-6 + (1e-6 + 0.5*m.x188*m.x189
                       *(m.x188 + m.x189))**0.33333))**0.6 + (1e-6 + 1.17647058823529*m.x104/(1e-6 + (1e-6 + 0.5*m.x189*
                       m.x190*(m.x189 + m.x190))**0.33333))**0.6 + (1e-6 + 117.629878654828*m.x105)**0.6 + (1e-6 + 
                       1.17647058823529*m.x106/(1e-6 + (1e-6 + 0.5*m.x191*m.x192*(m.x191 + m.x192))**0.33333))**0.6 + (
                       1e-6 + 1.17647058823529*m.x107/(1e-6 + (1e-6 + 0.5*m.x192*m.x193*(m.x192 + m.x193))**0.33333))**
                       0.6 + (1e-6 + 117.629878654828*m.x108)**0.6 + (1e-6 + 1.17647058823529*m.x109/(1e-6 + (1e-6 + 0.5
                       *m.x194*m.x195*(m.x194 + m.x195))**0.33333))**0.6 + (1e-6 + 1.17647058823529*m.x110/(1e-6 + (1e-6
                        + 0.5*m.x195*m.x196*(m.x195 + m.x196))**0.33333))**0.6 + (1e-6 + 117.629878654828*m.x111)**0.6
                        + (1e-6 + 1.17647058823529*m.x112/(1e-6 + (1e-6 + 0.5*m.x197*m.x198*(m.x197 + m.x198))**0.33333)
                       )**0.6 + (1e-6 + 1.17647058823529*m.x113/(1e-6 + (1e-6 + 0.5*m.x198*m.x199*(m.x198 + m.x199))**
                       0.33333))**0.6 + (1e-6 + 117.629878654828*m.x114)**0.6 + (1e-6 + 1.17647058823529*m.x115/(1e-6 + 
                       (1e-6 + 0.5*m.x200*m.x201*(m.x200 + m.x201))**0.33333))**0.6 + (1e-6 + 1.17647058823529*m.x116/(
                       1e-6 + (1e-6 + 0.5*m.x201*m.x202*(m.x201 + m.x202))**0.33333))**0.6 + (1e-6 + 117.629878654828*
                       m.x117)**0.6 + (1e-6 + 1.17647058823529*m.x118/(1e-6 + (1e-6 + 0.5*m.x203*m.x204*(m.x203 + m.x204
                       ))**0.33333))**0.6 + (1e-6 + 1.17647058823529*m.x119/(1e-6 + (1e-6 + 0.5*m.x204*m.x205*(m.x204 + 
                       m.x205))**0.33333))**0.6 + (1e-6 + 117.629878654828*m.x120)**0.6 + (1e-6 + 1.17647058823529*
                       m.x121/(1e-6 + (1e-6 + 0.5*m.x206*m.x207*(m.x206 + m.x207))**0.33333))**0.6 + (1e-6 + 
                       1.17647058823529*m.x122/(1e-6 + (1e-6 + 0.5*m.x207*m.x208*(m.x207 + m.x208))**0.33333))**0.6 + (
                       1e-6 + 117.629878654828*m.x123)**0.6 + (1e-6 + 1.17647058823529*m.x124/(1e-6 + (1e-6 + 0.5*m.x209
                       *m.x210*(m.x209 + m.x210))**0.33333))**0.6 + (1e-6 + 1.17647058823529*m.x125/(1e-6 + (1e-6 + 0.5*
                       m.x210*m.x211*(m.x210 + m.x211))**0.33333))**0.6 + (1e-6 + 117.629878654828*m.x126)**0.6 + (1e-6
                        + 1.17647058823529*m.x127/(1e-6 + (1e-6 + 0.5*m.x212*m.x213*(m.x212 + m.x213))**0.33333))**0.6
                        + (1e-6 + 1.17647058823529*m.x128/(1e-6 + (1e-6 + 0.5*m.x213*m.x214*(m.x213 + m.x214))**0.33333)
                       )**0.6 + (1e-6 + 117.629878654828*m.x129)**0.6 + (1e-6 + 1.17647058823529*m.x130/(1e-6 + (1e-6 + 
                       0.5*m.x215*m.x216*(m.x215 + m.x216))**0.33333))**0.6 + (1e-6 + 1.17647058823529*m.x131/(1e-6 + (
                       1e-6 + 0.5*m.x216*m.x217*(m.x216 + m.x217))**0.33333))**0.6 + (1e-6 + 117.629878654828*m.x132)**
                       0.6 + (1e-6 + 1.17647058823529*m.x133/(1e-6 + (1e-6 + 0.5*m.x218*m.x219*(m.x218 + m.x219))**
                       0.33333))**0.6 + (1e-6 + 1.17647058823529*m.x134/(1e-6 + (1e-6 + 0.5*m.x219*m.x220*(m.x219 + 
                       m.x220))**0.33333))**0.6 + (1e-6 + 117.629878654828*m.x135)**0.6 + (1e-6 + 1.17647058823529*
                       m.x136/(1e-6 + (1e-6 + 0.5*m.x221*m.x222*(m.x221 + m.x222))**0.33333))**0.6 + (1e-6 + 
                       1.17647058823529*m.x137/(1e-6 + (1e-6 + 0.5*m.x222*m.x223*(m.x222 + m.x223))**0.33333))**0.6 + (
                       1e-6 + 117.629878654828*m.x138)**0.6 + (1e-6 + 1.17647058823529*m.x139/(1e-6 + (1e-6 + 0.5*m.x224
                       *m.x225*(m.x224 + m.x225))**0.33333))**0.6 + (1e-6 + 1.17647058823529*m.x140/(1e-6 + (1e-6 + 0.5*
                       m.x225*m.x226*(m.x225 + m.x226))**0.33333))**0.6 + (1e-6 + 117.629878654828*m.x141)**0.6 + (1e-6
                        + 1.17647058823529*m.x142/(1e-6 + (1e-6 + 0.5*m.x227*m.x228*(m.x227 + m.x228))**0.33333))**0.6
                        + (1e-6 + 1.17647058823529*m.x143/(1e-6 + (1e-6 + 0.5*m.x228*m.x229*(m.x228 + m.x229))**0.33333)
                       )**0.6 + (1e-6 + 117.629878654828*m.x144)**0.6 + (1e-6 + 1.17647058823529*m.x145/(1e-6 + (1e-6 + 
                       0.5*m.x230*m.x231*(m.x230 + m.x231))**0.33333))**0.6 + (1e-6 + 1.17647058823529*m.x146/(1e-6 + (
                       1e-6 + 0.5*m.x231*m.x232*(m.x231 + m.x232))**0.33333))**0.6 + (1e-6 + 117.629878654828*m.x147)**
                       0.6 + (1e-6 + 1.17647058823529*m.x148/(1e-6 + (1e-6 + 0.5*m.x233*m.x234*(m.x233 + m.x234))**
                       0.33333))**0.6 + (1e-6 + 1.17647058823529*m.x149/(1e-6 + (1e-6 + 0.5*m.x234*m.x235*(m.x234 + 
                       m.x235))**0.33333))**0.6 + (1e-6 + 117.629878654828*m.x150)**0.6 + (1e-6 + 1.17647058823529*
                       m.x151/(1e-6 + (1e-6 + 0.5*m.x236*m.x237*(m.x236 + m.x237))**0.33333))**0.6 + (1e-6 + 
                       1.17647058823529*m.x152/(1e-6 + (1e-6 + 0.5*m.x237*m.x238*(m.x237 + m.x238))**0.33333))**0.6 + (
                       1e-6 + 117.629878654828*m.x153)**0.6 + (1e-6 + 1.17647058823529*m.x154/(1e-6 + (1e-6 + 0.5*m.x239
                       *m.x240*(m.x239 + m.x240))**0.33333))**0.6 + (1e-6 + 1.17647058823529*m.x155/(1e-6 + (1e-6 + 0.5*
                       m.x240*m.x241*(m.x240 + m.x241))**0.33333))**0.6 + (1e-6 + 117.629878654828*m.x156)**0.6 + (1e-6
                        + 1.17647058823529*m.x157/(1e-6 + (1e-6 + 0.5*m.x242*m.x243*(m.x242 + m.x243))**0.33333))**0.6
                        + (1e-6 + 1.17647058823529*m.x158/(1e-6 + (1e-6 + 0.5*m.x243*m.x244*(m.x243 + m.x244))**0.33333)
                       )**0.6 + (1e-6 + 117.629878654828*m.x159)**0.6 + (1e-6 + 1.17647058823529*m.x160/(1e-6 + (1e-6 + 
                       0.5*m.x245*m.x246*(m.x245 + m.x246))**0.33333))**0.6 + (1e-6 + 1.17647058823529*m.x161/(1e-6 + (
                       1e-6 + 0.5*m.x246*m.x247*(m.x246 + m.x247))**0.33333))**0.6 + (1e-6 + 117.629878654828*m.x162)**
                       0.6 + (1e-6 + 1.17647058823529*m.x163/(1e-6 + (1e-6 + 0.5*m.x248*m.x249*(m.x248 + m.x249))**
                       0.33333))**0.6 + (1e-6 + 1.17647058823529*m.x164/(1e-6 + (1e-6 + 0.5*m.x249*m.x250*(m.x249 + 
                       m.x250))**0.33333))**0.6 + (1e-6 + 117.629878654828*m.x165)**0.6) + 146*(5e-6 + 0.882352941176471
                       *m.x171/(1e-6 + 80*m.x256*(40 + 0.5*m.x256))**0.33333 + 0.882352941176471*m.x172/(1e-6 + 18.3*
                       m.x257*(9.15000000000001 + 0.5*m.x257))**0.33333 + 0.882352941176471*m.x173/(1e-6 + 18.9*m.x258*(
                       9.45 + 0.5*m.x258))**0.33333 + 0.882352941176471*m.x174/(1e-6 + 63.3*m.x259*(31.65 + 0.5*m.x259))
                       **0.33333 + 0.882352941176471*m.x175/(1e-6 + 35.6*m.x260*(17.8 + 0.5*m.x260))**0.33333)**0.6 + 
                       200*m.x171 + 200*m.x172 + 200*m.x173 + 200*m.x174 + 200*m.x175 + 146*((1e-6 + 1.17647058823529*
                       m.x166/(1e-6 + 34.15*m.x251*(68.3 + m.x251))**0.33333)**0.6 + (1e-6 + 1.17647058823529*m.x167/(
                       1e-6 + 56.4*m.x252*(112.8 + m.x252))**0.33333)**0.6 + (1e-6 + 1.17647058823529*m.x168/(1e-6 + 
                       20.3*m.x253*(40.6 + m.x253))**0.33333)**0.6 + (1e-6 + 1.17647058823529*m.x169/(1e-6 + 61.95*
                       m.x254*(123.9 + m.x254))**0.33333)**0.6 + (1e-6 + 1.17647058823529*m.x170/(1e-6 + 20.3*m.x255*(
                       40.6 + m.x255))**0.33333)**0.6) + 10*m.x166 + 10*m.x167 + 10*m.x168 + 10*m.x169 + 10*m.x170
                        + 4000*m.b1 + 4000*m.b2 + 4000*m.b3 + 4000*m.b4 + 4000*m.b5 + 4000*m.b6 + 4000*m.b7 + 4000*m.b8
                        + 4000*m.b9 + 4000*m.b10 + 4000*m.b11 + 4000*m.b12 + 4000*m.b13 + 4000*m.b14 + 4000*m.b15
                        + 4000*m.b16 + 4000*m.b17 + 4000*m.b18 + 4000*m.b19 + 4000*m.b20 + 4000*m.b21 + 4000*m.b22
                        + 4000*m.b23 + 4000*m.b24 + 4000*m.b25 + 4000*m.b26 + 4000*m.b27 + 4000*m.b28 + 4000*m.b29
                        + 4000*m.b30 + 4000*m.b31 + 4000*m.b32 + 4000*m.b33 + 4000*m.b34 + 4000*m.b35 + 4000*m.b36
                        + 4000*m.b37 + 4000*m.b38 + 4000*m.b39 + 4000*m.b40 + 4000*m.b41 + 4000*m.b42 + 4000*m.b43
                        + 4000*m.b44 + 4000*m.b45 + 4000*m.b46 + 4000*m.b47 + 4000*m.b48 + 4000*m.b49 + 4000*m.b50
                        + 4000*m.b51 + 4000*m.b52 + 4000*m.b53 + 4000*m.b54 + 4000*m.b55 + 4000*m.b56 + 4000*m.b57
                        + 4000*m.b58 + 4000*m.b59 + 4000*m.b60, sense=minimize)

m.c1 = Constraint(expr=   8.8*m.x61 - 8.8*m.x62 - m.x91 - m.x94 - m.x97 - m.x100 - m.x103 == 0)

m.c2 = Constraint(expr=   8.8*m.x62 - 8.8*m.x63 - m.x92 - m.x95 - m.x98 - m.x101 - m.x104 == 0)

m.c3 = Constraint(expr=   10.6*m.x64 - 10.6*m.x65 - m.x106 - m.x109 - m.x112 - m.x115 - m.x118 == 0)

m.c4 = Constraint(expr=   10.6*m.x65 - 10.6*m.x66 - m.x107 - m.x110 - m.x113 - m.x116 - m.x119 == 0)

m.c5 = Constraint(expr=   14.8*m.x67 - 14.8*m.x68 - m.x121 - m.x124 - m.x127 - m.x130 - m.x133 == 0)

m.c6 = Constraint(expr=   14.8*m.x68 - 14.8*m.x69 - m.x122 - m.x125 - m.x128 - m.x131 - m.x134 == 0)

m.c7 = Constraint(expr=   12.6*m.x70 - 12.6*m.x71 - m.x136 - m.x139 - m.x142 - m.x145 - m.x148 == 0)

m.c8 = Constraint(expr=   12.6*m.x71 - 12.6*m.x72 - m.x137 - m.x140 - m.x143 - m.x146 - m.x149 == 0)

m.c9 = Constraint(expr=   17.7*m.x73 - 17.7*m.x74 - m.x151 - m.x154 - m.x157 - m.x160 - m.x163 == 0)

m.c10 = Constraint(expr=   17.7*m.x74 - 17.7*m.x75 - m.x152 - m.x155 - m.x158 - m.x161 - m.x164 == 0)

m.c11 = Constraint(expr=   7.6*m.x76 - 7.6*m.x77 - m.x91 - m.x106 - m.x121 - m.x136 - m.x151 == 0)

m.c12 = Constraint(expr=   7.6*m.x77 - 7.6*m.x78 - m.x92 - m.x107 - m.x122 - m.x137 - m.x152 == 0)

m.c13 = Constraint(expr=   6.1*m.x79 - 6.1*m.x80 - m.x94 - m.x109 - m.x124 - m.x139 - m.x154 == 0)

m.c14 = Constraint(expr=   6.1*m.x80 - 6.1*m.x81 - m.x95 - m.x110 - m.x125 - m.x140 - m.x155 == 0)

m.c15 = Constraint(expr=   8.4*m.x82 - 8.4*m.x83 - m.x97 - m.x112 - m.x127 - m.x142 - m.x157 == 0)

m.c16 = Constraint(expr=   8.4*m.x83 - 8.4*m.x84 - m.x98 - m.x113 - m.x128 - m.x143 - m.x158 == 0)

m.c17 = Constraint(expr=   17.3*m.x85 - 17.3*m.x86 - m.x100 - m.x115 - m.x130 - m.x145 - m.x160 == 0)

m.c18 = Constraint(expr=   17.3*m.x86 - 17.3*m.x87 - m.x101 - m.x116 - m.x131 - m.x146 - m.x161 == 0)

m.c19 = Constraint(expr=   13.9*m.x88 - 13.9*m.x89 - m.x103 - m.x118 - m.x133 - m.x148 - m.x163 == 0)

m.c20 = Constraint(expr=   13.9*m.x89 - 13.9*m.x90 - m.x104 - m.x119 - m.x134 - m.x149 - m.x164 == 0)

m.c21 = Constraint(expr=   8.8*m.x63 - m.x166 == 821.04)

m.c22 = Constraint(expr=   10.6*m.x66 - m.x167 == 1460.68)

m.c23 = Constraint(expr=   14.8*m.x69 - m.x168 == 970.88)

m.c24 = Constraint(expr=   12.6*m.x72 - m.x169 == 1876.14)

m.c25 = Constraint(expr=   17.7*m.x75 - m.x170 == 1161.12)

m.c26 = Constraint(expr= - m.x91 - m.x92 - m.x94 - m.x95 - m.x97 - m.x98 - m.x100 - m.x101 - m.x103 - m.x104 - m.x166
                         == -586.96)

m.c27 = Constraint(expr= - m.x106 - m.x107 - m.x109 - m.x110 - m.x112 - m.x113 - m.x115 - m.x116 - m.x118 - m.x119
                         - m.x167 == -1177.66)

m.c28 = Constraint(expr= - m.x121 - m.x122 - m.x124 - m.x125 - m.x127 - m.x128 - m.x130 - m.x131 - m.x133 - m.x134
                         - m.x168 == -2384.28)

m.c29 = Constraint(expr= - m.x136 - m.x137 - m.x139 - m.x140 - m.x142 - m.x143 - m.x145 - m.x146 - m.x148 - m.x149
                         - m.x169 == -1539.72)

m.c30 = Constraint(expr= - m.x151 - m.x152 - m.x154 - m.x155 - m.x157 - m.x158 - m.x160 - m.x161 - m.x163 - m.x164
                         - m.x170 == -2359.41)

m.c31 = Constraint(expr= - 7.6*m.x76 - m.x171 == -1216)

m.c32 = Constraint(expr= - 6.1*m.x79 - m.x172 == -1352.37)

m.c33 = Constraint(expr= - 8.4*m.x82 - m.x173 == -1857.24)

m.c34 = Constraint(expr= - 17.3*m.x85 - m.x174 == -3056.91)

m.c35 = Constraint(expr= - 13.9*m.x88 - m.x175 == -2841.16)

m.c36 = Constraint(expr= - m.x91 - m.x92 - m.x106 - m.x107 - m.x121 - m.x122 - m.x136 - m.x137 - m.x151 - m.x152
                         - m.x171 == -760)

m.c37 = Constraint(expr= - m.x94 - m.x95 - m.x109 - m.x110 - m.x124 - m.x125 - m.x139 - m.x140 - m.x154 - m.x155
                         - m.x172 == -647.21)

m.c38 = Constraint(expr= - m.x97 - m.x98 - m.x112 - m.x113 - m.x127 - m.x128 - m.x142 - m.x143 - m.x157 - m.x158
                         - m.x173 == -1539.72)

m.c39 = Constraint(expr= - m.x100 - m.x101 - m.x115 - m.x116 - m.x130 - m.x131 - m.x145 - m.x146 - m.x160 - m.x161
                         - m.x174 == -1634.85)

m.c40 = Constraint(expr= - m.x103 - m.x104 - m.x118 - m.x119 - m.x133 - m.x134 - m.x148 - m.x149 - m.x163 - m.x164
                         - m.x175 == -1544.29)

m.c41 = Constraint(expr=   m.x61 - m.x62 >= 0)

m.c42 = Constraint(expr=   m.x62 - m.x63 >= 0)

m.c43 = Constraint(expr=   m.x64 - m.x65 >= 0)

m.c44 = Constraint(expr=   m.x65 - m.x66 >= 0)

m.c45 = Constraint(expr=   m.x67 - m.x68 >= 0)

m.c46 = Constraint(expr=   m.x68 - m.x69 >= 0)

m.c47 = Constraint(expr=   m.x70 - m.x71 >= 0)

m.c48 = Constraint(expr=   m.x71 - m.x72 >= 0)

m.c49 = Constraint(expr=   m.x73 - m.x74 >= 0)

m.c50 = Constraint(expr=   m.x74 - m.x75 >= 0)

m.c51 = Constraint(expr=   m.x76 - m.x77 >= 0)

m.c52 = Constraint(expr=   m.x77 - m.x78 >= 0)

m.c53 = Constraint(expr=   m.x79 - m.x80 >= 0)

m.c54 = Constraint(expr=   m.x80 - m.x81 >= 0)

m.c55 = Constraint(expr=   m.x82 - m.x83 >= 0)

m.c56 = Constraint(expr=   m.x83 - m.x84 >= 0)

m.c57 = Constraint(expr=   m.x85 - m.x86 >= 0)

m.c58 = Constraint(expr=   m.x86 - m.x87 >= 0)

m.c59 = Constraint(expr=   m.x88 - m.x89 >= 0)

m.c60 = Constraint(expr=   m.x89 - m.x90 >= 0)

m.c61 = Constraint(expr=   m.x63 >= 93.3)

m.c62 = Constraint(expr=   m.x66 >= 137.8)

m.c63 = Constraint(expr=   m.x69 >= 65.6)

m.c64 = Constraint(expr=   m.x72 >= 148.9)

m.c65 = Constraint(expr=   m.x75 >= 65.6)

m.c66 = Constraint(expr= - m.x76 >= -160)

m.c67 = Constraint(expr= - m.x79 >= -221.7)

m.c68 = Constraint(expr= - m.x82 >= -221.1)

m.c69 = Constraint(expr= - m.x85 >= -176.7)

m.c70 = Constraint(expr= - m.x88 >= -204.4)

m.c71 = Constraint(expr= - m.x61 == -160)

m.c72 = Constraint(expr= - m.x64 == -248.9)

m.c73 = Constraint(expr= - m.x67 == -226.7)

m.c74 = Constraint(expr= - m.x70 == -271.1)

m.c75 = Constraint(expr= - m.x73 == -198.9)

m.c76 = Constraint(expr= - m.x78 == -60)

m.c77 = Constraint(expr= - m.x81 == -115.6)

m.c78 = Constraint(expr= - m.x84 == -37.8)

m.c79 = Constraint(expr= - m.x87 == -82.2)

m.c80 = Constraint(expr= - m.x90 == -93.3)

m.c81 = Constraint(expr= - 586.96*m.b1 + m.x91 <= 0)

m.c82 = Constraint(expr= - 586.96*m.b2 + m.x92 <= 0)

m.c83 = Constraint(expr= - 586.96*m.b3 + m.x94 <= 0)

m.c84 = Constraint(expr= - 586.96*m.b4 + m.x95 <= 0)

m.c85 = Constraint(expr= - 586.96*m.b5 + m.x97 <= 0)

m.c86 = Constraint(expr= - 586.96*m.b6 + m.x98 <= 0)

m.c87 = Constraint(expr= - 586.96*m.b7 + m.x100 <= 0)

m.c88 = Constraint(expr= - 586.96*m.b8 + m.x101 <= 0)

m.c89 = Constraint(expr= - 586.96*m.b9 + m.x103 <= 0)

m.c90 = Constraint(expr= - 586.96*m.b10 + m.x104 <= 0)

m.c91 = Constraint(expr= - 760*m.b11 + m.x106 <= 0)

m.c92 = Constraint(expr= - 760*m.b12 + m.x107 <= 0)

m.c93 = Constraint(expr= - 647.21*m.b13 + m.x109 <= 0)

m.c94 = Constraint(expr= - 647.21*m.b14 + m.x110 <= 0)

m.c95 = Constraint(expr= - 1177.66*m.b15 + m.x112 <= 0)

m.c96 = Constraint(expr= - 1177.66*m.b16 + m.x113 <= 0)

m.c97 = Constraint(expr= - 1177.66*m.b17 + m.x115 <= 0)

m.c98 = Constraint(expr= - 1177.66*m.b18 + m.x116 <= 0)

m.c99 = Constraint(expr= - 1177.66*m.b19 + m.x118 <= 0)

m.c100 = Constraint(expr= - 1177.66*m.b20 + m.x119 <= 0)

m.c101 = Constraint(expr= - 760*m.b21 + m.x121 <= 0)

m.c102 = Constraint(expr= - 760*m.b22 + m.x122 <= 0)

m.c103 = Constraint(expr= - 647.21*m.b23 + m.x124 <= 0)

m.c104 = Constraint(expr= - 647.21*m.b24 + m.x125 <= 0)

m.c105 = Constraint(expr= - 1539.72*m.b25 + m.x127 <= 0)

m.c106 = Constraint(expr= - 1539.72*m.b26 + m.x128 <= 0)

m.c107 = Constraint(expr= - 1634.85*m.b27 + m.x130 <= 0)

m.c108 = Constraint(expr= - 1634.85*m.b28 + m.x131 <= 0)

m.c109 = Constraint(expr= - 1544.29*m.b29 + m.x133 <= 0)

m.c110 = Constraint(expr= - 1544.29*m.b30 + m.x134 <= 0)

m.c111 = Constraint(expr= - 760*m.b31 + m.x136 <= 0)

m.c112 = Constraint(expr= - 760*m.b32 + m.x137 <= 0)

m.c113 = Constraint(expr= - 647.21*m.b33 + m.x139 <= 0)

m.c114 = Constraint(expr= - 647.21*m.b34 + m.x140 <= 0)

m.c115 = Constraint(expr= - 1539.72*m.b35 + m.x142 <= 0)

m.c116 = Constraint(expr= - 1539.72*m.b36 + m.x143 <= 0)

m.c117 = Constraint(expr= - 1539.72*m.b37 + m.x145 <= 0)

m.c118 = Constraint(expr= - 1539.72*m.b38 + m.x146 <= 0)

m.c119 = Constraint(expr= - 1539.72*m.b39 + m.x148 <= 0)

m.c120 = Constraint(expr= - 1539.72*m.b40 + m.x149 <= 0)

m.c121 = Constraint(expr= - 760*m.b41 + m.x151 <= 0)

m.c122 = Constraint(expr= - 760*m.b42 + m.x152 <= 0)

m.c123 = Constraint(expr= - 647.21*m.b43 + m.x154 <= 0)

m.c124 = Constraint(expr= - 647.21*m.b44 + m.x155 <= 0)

m.c125 = Constraint(expr= - 1539.72*m.b45 + m.x157 <= 0)

m.c126 = Constraint(expr= - 1539.72*m.b46 + m.x158 <= 0)

m.c127 = Constraint(expr= - 1634.85*m.b47 + m.x160 <= 0)

m.c128 = Constraint(expr= - 1634.85*m.b48 + m.x161 <= 0)

m.c129 = Constraint(expr= - 1544.29*m.b49 + m.x163 <= 0)

m.c130 = Constraint(expr= - 1544.29*m.b50 + m.x164 <= 0)

m.c131 = Constraint(expr= - 760*m.b56 + m.x171 <= 0)

m.c132 = Constraint(expr= - 647.21*m.b57 + m.x172 <= 0)

m.c133 = Constraint(expr= - 1539.72*m.b58 + m.x173 <= 0)

m.c134 = Constraint(expr= - 1634.85*m.b59 + m.x174 <= 0)

m.c135 = Constraint(expr= - 1544.29*m.b60 + m.x175 <= 0)

m.c136 = Constraint(expr= - 586.96*m.b51 + m.x166 <= 0)

m.c137 = Constraint(expr= - 1177.66*m.b52 + m.x167 <= 0)

m.c138 = Constraint(expr= - 2384.28*m.b53 + m.x168 <= 0)

m.c139 = Constraint(expr= - 1539.72*m.b54 + m.x169 <= 0)

m.c140 = Constraint(expr= - 2359.41*m.b55 + m.x170 <= 0)

m.c141 = Constraint(expr=   66.7*m.b1 - m.x61 + m.x76 + m.x176 <= 66.7)

m.c142 = Constraint(expr=   66.7*m.b2 - m.x62 + m.x77 + m.x177 <= 66.7)

m.c143 = Constraint(expr=   128.4*m.b3 - m.x61 + m.x79 + m.x179 <= 128.4)

m.c144 = Constraint(expr=   128.4*m.b4 - m.x62 + m.x80 + m.x180 <= 128.4)

m.c145 = Constraint(expr=   127.8*m.b5 - m.x61 + m.x82 + m.x182 <= 127.8)

m.c146 = Constraint(expr=   127.8*m.b6 - m.x62 + m.x83 + m.x183 <= 127.8)

m.c147 = Constraint(expr=   83.4*m.b7 - m.x61 + m.x85 + m.x185 <= 83.4)

m.c148 = Constraint(expr=   83.4*m.b8 - m.x62 + m.x86 + m.x186 <= 83.4)

m.c149 = Constraint(expr=   111.1*m.b9 - m.x61 + m.x88 + m.x188 <= 111.1)

m.c150 = Constraint(expr=   111.1*m.b10 - m.x62 + m.x89 + m.x189 <= 111.1)

m.c151 = Constraint(expr=   22.2*m.b11 - m.x64 + m.x76 + m.x191 <= 22.2)

m.c152 = Constraint(expr=   22.2*m.b12 - m.x65 + m.x77 + m.x192 <= 22.2)

m.c153 = Constraint(expr=   83.9*m.b13 - m.x64 + m.x79 + m.x194 <= 83.9)

m.c154 = Constraint(expr=   83.9*m.b14 - m.x65 + m.x80 + m.x195 <= 83.9)

m.c155 = Constraint(expr=   83.3*m.b15 - m.x64 + m.x82 + m.x197 <= 83.3)

m.c156 = Constraint(expr=   83.3*m.b16 - m.x65 + m.x83 + m.x198 <= 83.3)

m.c157 = Constraint(expr=   38.9*m.b17 - m.x64 + m.x85 + m.x200 <= 38.9)

m.c158 = Constraint(expr=   38.9*m.b18 - m.x65 + m.x86 + m.x201 <= 38.9)

m.c159 = Constraint(expr=   66.6*m.b19 - m.x64 + m.x88 + m.x203 <= 66.6)

m.c160 = Constraint(expr=   66.6*m.b20 - m.x65 + m.x89 + m.x204 <= 66.6)

m.c161 = Constraint(expr=   94.4*m.b21 - m.x67 + m.x76 + m.x206 <= 94.4)

m.c162 = Constraint(expr=   94.4*m.b22 - m.x68 + m.x77 + m.x207 <= 94.4)

m.c163 = Constraint(expr=   156.1*m.b23 - m.x67 + m.x79 + m.x209 <= 156.1)

m.c164 = Constraint(expr=   156.1*m.b24 - m.x68 + m.x80 + m.x210 <= 156.1)

m.c165 = Constraint(expr=   155.5*m.b25 - m.x67 + m.x82 + m.x212 <= 155.5)

m.c166 = Constraint(expr=   155.5*m.b26 - m.x68 + m.x83 + m.x213 <= 155.5)

m.c167 = Constraint(expr=   111.1*m.b27 - m.x67 + m.x85 + m.x215 <= 111.1)

m.c168 = Constraint(expr=   111.1*m.b28 - m.x68 + m.x86 + m.x216 <= 111.1)

m.c169 = Constraint(expr=   138.8*m.b29 - m.x67 + m.x88 + m.x218 <= 138.8)

m.c170 = Constraint(expr=   138.8*m.b30 - m.x68 + m.x89 + m.x219 <= 138.8)

m.c171 = Constraint(expr=   11.1*m.b31 - m.x70 + m.x76 + m.x221 <= 11.1)

m.c172 = Constraint(expr=   11.1*m.b32 - m.x71 + m.x77 + m.x222 <= 11.1)

m.c173 = Constraint(expr=   72.8*m.b33 - m.x70 + m.x79 + m.x224 <= 72.8)

m.c174 = Constraint(expr=   72.8*m.b34 - m.x71 + m.x80 + m.x225 <= 72.8)

m.c175 = Constraint(expr=   72.2*m.b35 - m.x70 + m.x82 + m.x227 <= 72.2)

m.c176 = Constraint(expr=   72.2*m.b36 - m.x71 + m.x83 + m.x228 <= 72.2)

m.c177 = Constraint(expr=   27.8*m.b37 - m.x70 + m.x85 + m.x230 <= 27.8)

m.c178 = Constraint(expr=   27.8*m.b38 - m.x71 + m.x86 + m.x231 <= 27.8)

m.c179 = Constraint(expr=   55.5*m.b39 - m.x70 + m.x88 + m.x233 <= 55.5)

m.c180 = Constraint(expr=   55.5*m.b40 - m.x71 + m.x89 + m.x234 <= 55.5)

m.c181 = Constraint(expr=   94.4*m.b41 - m.x73 + m.x76 + m.x236 <= 94.4)

m.c182 = Constraint(expr=   94.4*m.b42 - m.x74 + m.x77 + m.x237 <= 94.4)

m.c183 = Constraint(expr=   156.1*m.b43 - m.x73 + m.x79 + m.x239 <= 156.1)

m.c184 = Constraint(expr=   156.1*m.b44 - m.x74 + m.x80 + m.x240 <= 156.1)

m.c185 = Constraint(expr=   155.5*m.b45 - m.x73 + m.x82 + m.x242 <= 155.5)

m.c186 = Constraint(expr=   155.5*m.b46 - m.x74 + m.x83 + m.x243 <= 155.5)

m.c187 = Constraint(expr=   111.1*m.b47 - m.x73 + m.x85 + m.x245 <= 111.1)

m.c188 = Constraint(expr=   111.1*m.b48 - m.x74 + m.x86 + m.x246 <= 111.1)

m.c189 = Constraint(expr=   138.8*m.b49 - m.x73 + m.x88 + m.x248 <= 138.8)

m.c190 = Constraint(expr=   138.8*m.b50 - m.x74 + m.x89 + m.x249 <= 138.8)

m.c191 = Constraint(expr=   66.7*m.b1 - m.x62 + m.x77 + m.x177 <= 66.7)

m.c192 = Constraint(expr=   66.7*m.b2 - m.x63 + m.x78 + m.x178 <= 66.7)

m.c193 = Constraint(expr=   128.4*m.b3 - m.x62 + m.x80 + m.x180 <= 128.4)

m.c194 = Constraint(expr=   128.4*m.b4 - m.x63 + m.x81 + m.x181 <= 128.4)

m.c195 = Constraint(expr=   127.8*m.b5 - m.x62 + m.x83 + m.x183 <= 127.8)

m.c196 = Constraint(expr=   127.8*m.b6 - m.x63 + m.x84 + m.x184 <= 127.8)

m.c197 = Constraint(expr=   83.4*m.b7 - m.x62 + m.x86 + m.x186 <= 83.4)

m.c198 = Constraint(expr=   83.4*m.b8 - m.x63 + m.x87 + m.x187 <= 83.4)

m.c199 = Constraint(expr=   111.1*m.b9 - m.x62 + m.x89 + m.x189 <= 111.1)

m.c200 = Constraint(expr=   111.1*m.b10 - m.x63 + m.x90 + m.x190 <= 111.1)

m.c201 = Constraint(expr=   22.2*m.b11 - m.x65 + m.x77 + m.x192 <= 22.2)

m.c202 = Constraint(expr=   22.2*m.b12 - m.x66 + m.x78 + m.x193 <= 22.2)

m.c203 = Constraint(expr=   83.9*m.b13 - m.x65 + m.x80 + m.x195 <= 83.9)

m.c204 = Constraint(expr=   83.9*m.b14 - m.x66 + m.x81 + m.x196 <= 83.9)

m.c205 = Constraint(expr=   83.3*m.b15 - m.x65 + m.x83 + m.x198 <= 83.3)

m.c206 = Constraint(expr=   83.3*m.b16 - m.x66 + m.x84 + m.x199 <= 83.3)

m.c207 = Constraint(expr=   38.9*m.b17 - m.x65 + m.x86 + m.x201 <= 38.9)

m.c208 = Constraint(expr=   38.9*m.b18 - m.x66 + m.x87 + m.x202 <= 38.9)

m.c209 = Constraint(expr=   66.6*m.b19 - m.x65 + m.x89 + m.x204 <= 66.6)

m.c210 = Constraint(expr=   66.6*m.b20 - m.x66 + m.x90 + m.x205 <= 66.6)

m.c211 = Constraint(expr=   94.4*m.b21 - m.x68 + m.x77 + m.x207 <= 94.4)

m.c212 = Constraint(expr=   94.4*m.b22 - m.x69 + m.x78 + m.x208 <= 94.4)

m.c213 = Constraint(expr=   156.1*m.b23 - m.x68 + m.x80 + m.x210 <= 156.1)

m.c214 = Constraint(expr=   156.1*m.b24 - m.x69 + m.x81 + m.x211 <= 156.1)

m.c215 = Constraint(expr=   155.5*m.b25 - m.x68 + m.x83 + m.x213 <= 155.5)

m.c216 = Constraint(expr=   155.5*m.b26 - m.x69 + m.x84 + m.x214 <= 155.5)

m.c217 = Constraint(expr=   111.1*m.b27 - m.x68 + m.x86 + m.x216 <= 111.1)

m.c218 = Constraint(expr=   111.1*m.b28 - m.x69 + m.x87 + m.x217 <= 111.1)

m.c219 = Constraint(expr=   138.8*m.b29 - m.x68 + m.x89 + m.x219 <= 138.8)

m.c220 = Constraint(expr=   138.8*m.b30 - m.x69 + m.x90 + m.x220 <= 138.8)

m.c221 = Constraint(expr=   11.1*m.b31 - m.x71 + m.x77 + m.x222 <= 11.1)

m.c222 = Constraint(expr=   11.1*m.b32 - m.x72 + m.x78 + m.x223 <= 11.1)

m.c223 = Constraint(expr=   72.8*m.b33 - m.x71 + m.x80 + m.x225 <= 72.8)

m.c224 = Constraint(expr=   72.8*m.b34 - m.x72 + m.x81 + m.x226 <= 72.8)

m.c225 = Constraint(expr=   72.2*m.b35 - m.x71 + m.x83 + m.x228 <= 72.2)

m.c226 = Constraint(expr=   72.2*m.b36 - m.x72 + m.x84 + m.x229 <= 72.2)

m.c227 = Constraint(expr=   27.8*m.b37 - m.x71 + m.x86 + m.x231 <= 27.8)

m.c228 = Constraint(expr=   27.8*m.b38 - m.x72 + m.x87 + m.x232 <= 27.8)

m.c229 = Constraint(expr=   55.5*m.b39 - m.x71 + m.x89 + m.x234 <= 55.5)

m.c230 = Constraint(expr=   55.5*m.b40 - m.x72 + m.x90 + m.x235 <= 55.5)

m.c231 = Constraint(expr=   94.4*m.b41 - m.x74 + m.x77 + m.x237 <= 94.4)

m.c232 = Constraint(expr=   94.4*m.b42 - m.x75 + m.x78 + m.x238 <= 94.4)

m.c233 = Constraint(expr=   156.1*m.b43 - m.x74 + m.x80 + m.x240 <= 156.1)

m.c234 = Constraint(expr=   156.1*m.b44 - m.x75 + m.x81 + m.x241 <= 156.1)

m.c235 = Constraint(expr=   155.5*m.b45 - m.x74 + m.x83 + m.x243 <= 155.5)

m.c236 = Constraint(expr=   155.5*m.b46 - m.x75 + m.x84 + m.x244 <= 155.5)

m.c237 = Constraint(expr=   111.1*m.b47 - m.x74 + m.x86 + m.x246 <= 111.1)

m.c238 = Constraint(expr=   111.1*m.b48 - m.x75 + m.x87 + m.x247 <= 111.1)

m.c239 = Constraint(expr=   138.8*m.b49 - m.x74 + m.x89 + m.x249 <= 138.8)

m.c240 = Constraint(expr=   138.8*m.b50 - m.x75 + m.x90 + m.x250 <= 138.8)

m.c241 = Constraint(expr= - m.x63 + m.x251 <= -40)

m.c242 = Constraint(expr= - m.x66 + m.x252 <= -40)

m.c243 = Constraint(expr= - m.x69 + m.x253 <= -40)

m.c244 = Constraint(expr= - m.x72 + m.x254 <= -40)

m.c245 = Constraint(expr= - m.x75 + m.x255 <= -40)

m.c246 = Constraint(expr=   m.x76 + m.x256 <= 240)

m.c247 = Constraint(expr=   m.x79 + m.x257 <= 240)

m.c248 = Constraint(expr=   m.x82 + m.x258 <= 240)

m.c249 = Constraint(expr=   m.x85 + m.x259 <= 240)

m.c250 = Constraint(expr=   m.x88 + m.x260 <= 240)
