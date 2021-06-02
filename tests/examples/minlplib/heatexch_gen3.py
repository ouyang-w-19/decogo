#  MINLP written by GAMS Convert at 04/21/18 13:52:23
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        511      311       30      170        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        581      521       60        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       2096     1281      815        0
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
m.x93 = Var(within=Reals,bounds=(0,None),initialize=586.96)
m.x94 = Var(within=Reals,bounds=(0,None),initialize=586.96)
m.x95 = Var(within=Reals,bounds=(0,None),initialize=586.96)
m.x96 = Var(within=Reals,bounds=(0,None),initialize=586.96)
m.x97 = Var(within=Reals,bounds=(0,None),initialize=586.96)
m.x98 = Var(within=Reals,bounds=(0,None),initialize=586.96)
m.x99 = Var(within=Reals,bounds=(0,None),initialize=586.96)
m.x100 = Var(within=Reals,bounds=(0,None),initialize=586.96)
m.x101 = Var(within=Reals,bounds=(0,None),initialize=760)
m.x102 = Var(within=Reals,bounds=(0,None),initialize=760)
m.x103 = Var(within=Reals,bounds=(0,None),initialize=647.21)
m.x104 = Var(within=Reals,bounds=(0,None),initialize=647.21)
m.x105 = Var(within=Reals,bounds=(0,None),initialize=1177.66)
m.x106 = Var(within=Reals,bounds=(0,None),initialize=1177.66)
m.x107 = Var(within=Reals,bounds=(0,None),initialize=1177.66)
m.x108 = Var(within=Reals,bounds=(0,None),initialize=1177.66)
m.x109 = Var(within=Reals,bounds=(0,None),initialize=1177.66)
m.x110 = Var(within=Reals,bounds=(0,None),initialize=1177.66)
m.x111 = Var(within=Reals,bounds=(0,None),initialize=760)
m.x112 = Var(within=Reals,bounds=(0,None),initialize=760)
m.x113 = Var(within=Reals,bounds=(0,None),initialize=647.21)
m.x114 = Var(within=Reals,bounds=(0,None),initialize=647.21)
m.x115 = Var(within=Reals,bounds=(0,None),initialize=1539.72)
m.x116 = Var(within=Reals,bounds=(0,None),initialize=1539.72)
m.x117 = Var(within=Reals,bounds=(0,None),initialize=1634.85)
m.x118 = Var(within=Reals,bounds=(0,None),initialize=1634.85)
m.x119 = Var(within=Reals,bounds=(0,None),initialize=1544.29)
m.x120 = Var(within=Reals,bounds=(0,None),initialize=1544.29)
m.x121 = Var(within=Reals,bounds=(0,None),initialize=760)
m.x122 = Var(within=Reals,bounds=(0,None),initialize=760)
m.x123 = Var(within=Reals,bounds=(0,None),initialize=647.21)
m.x124 = Var(within=Reals,bounds=(0,None),initialize=647.21)
m.x125 = Var(within=Reals,bounds=(0,None),initialize=1539.72)
m.x126 = Var(within=Reals,bounds=(0,None),initialize=1539.72)
m.x127 = Var(within=Reals,bounds=(0,None),initialize=1539.72)
m.x128 = Var(within=Reals,bounds=(0,None),initialize=1539.72)
m.x129 = Var(within=Reals,bounds=(0,None),initialize=1539.72)
m.x130 = Var(within=Reals,bounds=(0,None),initialize=1539.72)
m.x131 = Var(within=Reals,bounds=(0,None),initialize=760)
m.x132 = Var(within=Reals,bounds=(0,None),initialize=760)
m.x133 = Var(within=Reals,bounds=(0,None),initialize=647.21)
m.x134 = Var(within=Reals,bounds=(0,None),initialize=647.21)
m.x135 = Var(within=Reals,bounds=(0,None),initialize=1539.72)
m.x136 = Var(within=Reals,bounds=(0,None),initialize=1539.72)
m.x137 = Var(within=Reals,bounds=(0,None),initialize=1634.85)
m.x138 = Var(within=Reals,bounds=(0,None),initialize=1634.85)
m.x139 = Var(within=Reals,bounds=(0,None),initialize=1544.29)
m.x140 = Var(within=Reals,bounds=(0,None),initialize=1544.29)
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
m.x151 = Var(within=Reals,bounds=(10,None),initialize=100)
m.x152 = Var(within=Reals,bounds=(10,None),initialize=100)
m.x153 = Var(within=Reals,bounds=(10,None),initialize=100)
m.x154 = Var(within=Reals,bounds=(10,None),initialize=44.4)
m.x155 = Var(within=Reals,bounds=(10,None),initialize=44.4)
m.x156 = Var(within=Reals,bounds=(10,None),initialize=44.4)
m.x157 = Var(within=Reals,bounds=(10,None),initialize=122.2)
m.x158 = Var(within=Reals,bounds=(10,None),initialize=122.2)
m.x159 = Var(within=Reals,bounds=(10,None),initialize=122.2)
m.x160 = Var(within=Reals,bounds=(10,None),initialize=77.8)
m.x161 = Var(within=Reals,bounds=(10,None),initialize=77.8)
m.x162 = Var(within=Reals,bounds=(10,None),initialize=77.8)
m.x163 = Var(within=Reals,bounds=(10,None),initialize=66.7)
m.x164 = Var(within=Reals,bounds=(10,None),initialize=66.7)
m.x165 = Var(within=Reals,bounds=(10,None),initialize=66.7)
m.x166 = Var(within=Reals,bounds=(10,None),initialize=188.9)
m.x167 = Var(within=Reals,bounds=(10,None),initialize=188.9)
m.x168 = Var(within=Reals,bounds=(10,None),initialize=188.9)
m.x169 = Var(within=Reals,bounds=(10,None),initialize=133.3)
m.x170 = Var(within=Reals,bounds=(10,None),initialize=133.3)
m.x171 = Var(within=Reals,bounds=(10,None),initialize=133.3)
m.x172 = Var(within=Reals,bounds=(10,None),initialize=211.1)
m.x173 = Var(within=Reals,bounds=(10,None),initialize=211.1)
m.x174 = Var(within=Reals,bounds=(10,None),initialize=211.1)
m.x175 = Var(within=Reals,bounds=(10,None),initialize=166.7)
m.x176 = Var(within=Reals,bounds=(10,None),initialize=166.7)
m.x177 = Var(within=Reals,bounds=(10,None),initialize=166.7)
m.x178 = Var(within=Reals,bounds=(10,None),initialize=155.6)
m.x179 = Var(within=Reals,bounds=(10,None),initialize=155.6)
m.x180 = Var(within=Reals,bounds=(10,None),initialize=155.6)
m.x181 = Var(within=Reals,bounds=(10,None),initialize=166.7)
m.x182 = Var(within=Reals,bounds=(10,None),initialize=166.7)
m.x183 = Var(within=Reals,bounds=(10,None),initialize=166.7)
m.x184 = Var(within=Reals,bounds=(10,None),initialize=111.1)
m.x185 = Var(within=Reals,bounds=(10,None),initialize=111.1)
m.x186 = Var(within=Reals,bounds=(10,None),initialize=111.1)
m.x187 = Var(within=Reals,bounds=(10,None),initialize=188.9)
m.x188 = Var(within=Reals,bounds=(10,None),initialize=188.9)
m.x189 = Var(within=Reals,bounds=(10,None),initialize=188.9)
m.x190 = Var(within=Reals,bounds=(10,None),initialize=144.5)
m.x191 = Var(within=Reals,bounds=(10,None),initialize=144.5)
m.x192 = Var(within=Reals,bounds=(10,None),initialize=144.5)
m.x193 = Var(within=Reals,bounds=(10,None),initialize=133.4)
m.x194 = Var(within=Reals,bounds=(10,None),initialize=133.4)
m.x195 = Var(within=Reals,bounds=(10,None),initialize=133.4)
m.x196 = Var(within=Reals,bounds=(10,None),initialize=211.1)
m.x197 = Var(within=Reals,bounds=(10,None),initialize=211.1)
m.x198 = Var(within=Reals,bounds=(10,None),initialize=211.1)
m.x199 = Var(within=Reals,bounds=(10,None),initialize=155.5)
m.x200 = Var(within=Reals,bounds=(10,None),initialize=155.5)
m.x201 = Var(within=Reals,bounds=(10,None),initialize=155.5)
m.x202 = Var(within=Reals,bounds=(10,None),initialize=233.3)
m.x203 = Var(within=Reals,bounds=(10,None),initialize=233.3)
m.x204 = Var(within=Reals,bounds=(10,None),initialize=233.3)
m.x205 = Var(within=Reals,bounds=(10,None),initialize=188.9)
m.x206 = Var(within=Reals,bounds=(10,None),initialize=188.9)
m.x207 = Var(within=Reals,bounds=(10,None),initialize=188.9)
m.x208 = Var(within=Reals,bounds=(10,None),initialize=177.8)
m.x209 = Var(within=Reals,bounds=(10,None),initialize=177.8)
m.x210 = Var(within=Reals,bounds=(10,None),initialize=177.8)
m.x211 = Var(within=Reals,bounds=(10,None),initialize=138.9)
m.x212 = Var(within=Reals,bounds=(10,None),initialize=138.9)
m.x213 = Var(within=Reals,bounds=(10,None),initialize=138.9)
m.x214 = Var(within=Reals,bounds=(10,None),initialize=83.3)
m.x215 = Var(within=Reals,bounds=(10,None),initialize=83.3)
m.x216 = Var(within=Reals,bounds=(10,None),initialize=83.3)
m.x217 = Var(within=Reals,bounds=(10,None),initialize=161.1)
m.x218 = Var(within=Reals,bounds=(10,None),initialize=161.1)
m.x219 = Var(within=Reals,bounds=(10,None),initialize=161.1)
m.x220 = Var(within=Reals,bounds=(10,None),initialize=116.7)
m.x221 = Var(within=Reals,bounds=(10,None),initialize=116.7)
m.x222 = Var(within=Reals,bounds=(10,None),initialize=116.7)
m.x223 = Var(within=Reals,bounds=(10,None),initialize=105.6)
m.x224 = Var(within=Reals,bounds=(10,None),initialize=105.6)
m.x225 = Var(within=Reals,bounds=(10,None),initialize=105.6)
m.x226 = Var(within=Reals,bounds=(10,None),initialize=120)
m.x227 = Var(within=Reals,bounds=(10,None),initialize=208.9)
m.x228 = Var(within=Reals,bounds=(10,None),initialize=186.7)
m.x229 = Var(within=Reals,bounds=(10,None),initialize=231.1)
m.x230 = Var(within=Reals,bounds=(10,None),initialize=158.9)
m.x231 = Var(within=Reals,bounds=(10,None),initialize=180)
m.x232 = Var(within=Reals,bounds=(10,None),initialize=124.4)
m.x233 = Var(within=Reals,bounds=(10,None),initialize=202.2)
m.x234 = Var(within=Reals,bounds=(10,None),initialize=157.8)
m.x235 = Var(within=Reals,bounds=(10,None),initialize=146.7)
m.x236 = Var(within=Reals,bounds=(0,8.8),initialize=8.8)
m.x237 = Var(within=Reals,bounds=(0,8.8),initialize=8.8)
m.x238 = Var(within=Reals,bounds=(0,8.8),initialize=8.8)
m.x239 = Var(within=Reals,bounds=(0,8.8),initialize=8.8)
m.x240 = Var(within=Reals,bounds=(0,8.8),initialize=8.8)
m.x241 = Var(within=Reals,bounds=(0,8.8),initialize=8.8)
m.x242 = Var(within=Reals,bounds=(0,8.8),initialize=8.8)
m.x243 = Var(within=Reals,bounds=(0,8.8),initialize=8.8)
m.x244 = Var(within=Reals,bounds=(0,8.8),initialize=8.8)
m.x245 = Var(within=Reals,bounds=(0,8.8),initialize=8.8)
m.x246 = Var(within=Reals,bounds=(0,10.6),initialize=10.6)
m.x247 = Var(within=Reals,bounds=(0,10.6),initialize=10.6)
m.x248 = Var(within=Reals,bounds=(0,10.6),initialize=10.6)
m.x249 = Var(within=Reals,bounds=(0,10.6),initialize=10.6)
m.x250 = Var(within=Reals,bounds=(0,10.6),initialize=10.6)
m.x251 = Var(within=Reals,bounds=(0,10.6),initialize=10.6)
m.x252 = Var(within=Reals,bounds=(0,10.6),initialize=10.6)
m.x253 = Var(within=Reals,bounds=(0,10.6),initialize=10.6)
m.x254 = Var(within=Reals,bounds=(0,10.6),initialize=10.6)
m.x255 = Var(within=Reals,bounds=(0,10.6),initialize=10.6)
m.x256 = Var(within=Reals,bounds=(0,14.8),initialize=14.8)
m.x257 = Var(within=Reals,bounds=(0,14.8),initialize=14.8)
m.x258 = Var(within=Reals,bounds=(0,14.8),initialize=14.8)
m.x259 = Var(within=Reals,bounds=(0,14.8),initialize=14.8)
m.x260 = Var(within=Reals,bounds=(0,14.8),initialize=14.8)
m.x261 = Var(within=Reals,bounds=(0,14.8),initialize=14.8)
m.x262 = Var(within=Reals,bounds=(0,14.8),initialize=14.8)
m.x263 = Var(within=Reals,bounds=(0,14.8),initialize=14.8)
m.x264 = Var(within=Reals,bounds=(0,14.8),initialize=14.8)
m.x265 = Var(within=Reals,bounds=(0,14.8),initialize=14.8)
m.x266 = Var(within=Reals,bounds=(0,12.6),initialize=12.6)
m.x267 = Var(within=Reals,bounds=(0,12.6),initialize=12.6)
m.x268 = Var(within=Reals,bounds=(0,12.6),initialize=12.6)
m.x269 = Var(within=Reals,bounds=(0,12.6),initialize=12.6)
m.x270 = Var(within=Reals,bounds=(0,12.6),initialize=12.6)
m.x271 = Var(within=Reals,bounds=(0,12.6),initialize=12.6)
m.x272 = Var(within=Reals,bounds=(0,12.6),initialize=12.6)
m.x273 = Var(within=Reals,bounds=(0,12.6),initialize=12.6)
m.x274 = Var(within=Reals,bounds=(0,12.6),initialize=12.6)
m.x275 = Var(within=Reals,bounds=(0,12.6),initialize=12.6)
m.x276 = Var(within=Reals,bounds=(0,17.7),initialize=17.7)
m.x277 = Var(within=Reals,bounds=(0,17.7),initialize=17.7)
m.x278 = Var(within=Reals,bounds=(0,17.7),initialize=17.7)
m.x279 = Var(within=Reals,bounds=(0,17.7),initialize=17.7)
m.x280 = Var(within=Reals,bounds=(0,17.7),initialize=17.7)
m.x281 = Var(within=Reals,bounds=(0,17.7),initialize=17.7)
m.x282 = Var(within=Reals,bounds=(0,17.7),initialize=17.7)
m.x283 = Var(within=Reals,bounds=(0,17.7),initialize=17.7)
m.x284 = Var(within=Reals,bounds=(0,17.7),initialize=17.7)
m.x285 = Var(within=Reals,bounds=(0,17.7),initialize=17.7)
m.x286 = Var(within=Reals,bounds=(0,7.6),initialize=7.6)
m.x287 = Var(within=Reals,bounds=(0,7.6),initialize=7.6)
m.x288 = Var(within=Reals,bounds=(0,6.1),initialize=6.1)
m.x289 = Var(within=Reals,bounds=(0,6.1),initialize=6.1)
m.x290 = Var(within=Reals,bounds=(0,8.4),initialize=8.4)
m.x291 = Var(within=Reals,bounds=(0,8.4),initialize=8.4)
m.x292 = Var(within=Reals,bounds=(0,17.3),initialize=17.3)
m.x293 = Var(within=Reals,bounds=(0,17.3),initialize=17.3)
m.x294 = Var(within=Reals,bounds=(0,13.9),initialize=13.9)
m.x295 = Var(within=Reals,bounds=(0,13.9),initialize=13.9)
m.x296 = Var(within=Reals,bounds=(0,7.6),initialize=7.6)
m.x297 = Var(within=Reals,bounds=(0,7.6),initialize=7.6)
m.x298 = Var(within=Reals,bounds=(0,6.1),initialize=6.1)
m.x299 = Var(within=Reals,bounds=(0,6.1),initialize=6.1)
m.x300 = Var(within=Reals,bounds=(0,8.4),initialize=8.4)
m.x301 = Var(within=Reals,bounds=(0,8.4),initialize=8.4)
m.x302 = Var(within=Reals,bounds=(0,17.3),initialize=17.3)
m.x303 = Var(within=Reals,bounds=(0,17.3),initialize=17.3)
m.x304 = Var(within=Reals,bounds=(0,13.9),initialize=13.9)
m.x305 = Var(within=Reals,bounds=(0,13.9),initialize=13.9)
m.x306 = Var(within=Reals,bounds=(0,7.6),initialize=7.6)
m.x307 = Var(within=Reals,bounds=(0,7.6),initialize=7.6)
m.x308 = Var(within=Reals,bounds=(0,6.1),initialize=6.1)
m.x309 = Var(within=Reals,bounds=(0,6.1),initialize=6.1)
m.x310 = Var(within=Reals,bounds=(0,8.4),initialize=8.4)
m.x311 = Var(within=Reals,bounds=(0,8.4),initialize=8.4)
m.x312 = Var(within=Reals,bounds=(0,17.3),initialize=17.3)
m.x313 = Var(within=Reals,bounds=(0,17.3),initialize=17.3)
m.x314 = Var(within=Reals,bounds=(0,13.9),initialize=13.9)
m.x315 = Var(within=Reals,bounds=(0,13.9),initialize=13.9)
m.x316 = Var(within=Reals,bounds=(0,7.6),initialize=7.6)
m.x317 = Var(within=Reals,bounds=(0,7.6),initialize=7.6)
m.x318 = Var(within=Reals,bounds=(0,6.1),initialize=6.1)
m.x319 = Var(within=Reals,bounds=(0,6.1),initialize=6.1)
m.x320 = Var(within=Reals,bounds=(0,8.4),initialize=8.4)
m.x321 = Var(within=Reals,bounds=(0,8.4),initialize=8.4)
m.x322 = Var(within=Reals,bounds=(0,17.3),initialize=17.3)
m.x323 = Var(within=Reals,bounds=(0,17.3),initialize=17.3)
m.x324 = Var(within=Reals,bounds=(0,13.9),initialize=13.9)
m.x325 = Var(within=Reals,bounds=(0,13.9),initialize=13.9)
m.x326 = Var(within=Reals,bounds=(0,7.6),initialize=7.6)
m.x327 = Var(within=Reals,bounds=(0,7.6),initialize=7.6)
m.x328 = Var(within=Reals,bounds=(0,6.1),initialize=6.1)
m.x329 = Var(within=Reals,bounds=(0,6.1),initialize=6.1)
m.x330 = Var(within=Reals,bounds=(0,8.4),initialize=8.4)
m.x331 = Var(within=Reals,bounds=(0,8.4),initialize=8.4)
m.x332 = Var(within=Reals,bounds=(0,17.3),initialize=17.3)
m.x333 = Var(within=Reals,bounds=(0,17.3),initialize=17.3)
m.x334 = Var(within=Reals,bounds=(0,13.9),initialize=13.9)
m.x335 = Var(within=Reals,bounds=(0,13.9),initialize=13.9)
m.x336 = Var(within=Reals,bounds=(93.3,160),initialize=160)
m.x337 = Var(within=Reals,bounds=(93.3,160),initialize=160)
m.x338 = Var(within=Reals,bounds=(93.3,160),initialize=160)
m.x339 = Var(within=Reals,bounds=(93.3,160),initialize=160)
m.x340 = Var(within=Reals,bounds=(93.3,160),initialize=160)
m.x341 = Var(within=Reals,bounds=(93.3,160),initialize=160)
m.x342 = Var(within=Reals,bounds=(93.3,160),initialize=160)
m.x343 = Var(within=Reals,bounds=(93.3,160),initialize=160)
m.x344 = Var(within=Reals,bounds=(93.3,160),initialize=160)
m.x345 = Var(within=Reals,bounds=(93.3,160),initialize=160)
m.x346 = Var(within=Reals,bounds=(137.8,248.9),initialize=248.9)
m.x347 = Var(within=Reals,bounds=(137.8,248.9),initialize=248.9)
m.x348 = Var(within=Reals,bounds=(137.8,248.9),initialize=248.9)
m.x349 = Var(within=Reals,bounds=(137.8,248.9),initialize=248.9)
m.x350 = Var(within=Reals,bounds=(137.8,248.9),initialize=248.9)
m.x351 = Var(within=Reals,bounds=(137.8,248.9),initialize=248.9)
m.x352 = Var(within=Reals,bounds=(137.8,248.9),initialize=248.9)
m.x353 = Var(within=Reals,bounds=(137.8,248.9),initialize=248.9)
m.x354 = Var(within=Reals,bounds=(137.8,248.9),initialize=248.9)
m.x355 = Var(within=Reals,bounds=(137.8,248.9),initialize=248.9)
m.x356 = Var(within=Reals,bounds=(65.6,226.7),initialize=226.7)
m.x357 = Var(within=Reals,bounds=(65.6,226.7),initialize=226.7)
m.x358 = Var(within=Reals,bounds=(65.6,226.7),initialize=226.7)
m.x359 = Var(within=Reals,bounds=(65.6,226.7),initialize=226.7)
m.x360 = Var(within=Reals,bounds=(65.6,226.7),initialize=226.7)
m.x361 = Var(within=Reals,bounds=(65.6,226.7),initialize=226.7)
m.x362 = Var(within=Reals,bounds=(65.6,226.7),initialize=226.7)
m.x363 = Var(within=Reals,bounds=(65.6,226.7),initialize=226.7)
m.x364 = Var(within=Reals,bounds=(65.6,226.7),initialize=226.7)
m.x365 = Var(within=Reals,bounds=(65.6,226.7),initialize=226.7)
m.x366 = Var(within=Reals,bounds=(148.9,271.1),initialize=271.1)
m.x367 = Var(within=Reals,bounds=(148.9,271.1),initialize=271.1)
m.x368 = Var(within=Reals,bounds=(148.9,271.1),initialize=271.1)
m.x369 = Var(within=Reals,bounds=(148.9,271.1),initialize=271.1)
m.x370 = Var(within=Reals,bounds=(148.9,271.1),initialize=271.1)
m.x371 = Var(within=Reals,bounds=(148.9,271.1),initialize=271.1)
m.x372 = Var(within=Reals,bounds=(148.9,271.1),initialize=271.1)
m.x373 = Var(within=Reals,bounds=(148.9,271.1),initialize=271.1)
m.x374 = Var(within=Reals,bounds=(148.9,271.1),initialize=271.1)
m.x375 = Var(within=Reals,bounds=(148.9,271.1),initialize=271.1)
m.x376 = Var(within=Reals,bounds=(65.6,198.9),initialize=198.9)
m.x377 = Var(within=Reals,bounds=(65.6,198.9),initialize=198.9)
m.x378 = Var(within=Reals,bounds=(65.6,198.9),initialize=198.9)
m.x379 = Var(within=Reals,bounds=(65.6,198.9),initialize=198.9)
m.x380 = Var(within=Reals,bounds=(65.6,198.9),initialize=198.9)
m.x381 = Var(within=Reals,bounds=(65.6,198.9),initialize=198.9)
m.x382 = Var(within=Reals,bounds=(65.6,198.9),initialize=198.9)
m.x383 = Var(within=Reals,bounds=(65.6,198.9),initialize=198.9)
m.x384 = Var(within=Reals,bounds=(65.6,198.9),initialize=198.9)
m.x385 = Var(within=Reals,bounds=(65.6,198.9),initialize=198.9)
m.x386 = Var(within=Reals,bounds=(60,160),initialize=60)
m.x387 = Var(within=Reals,bounds=(60,160),initialize=60)
m.x388 = Var(within=Reals,bounds=(115.6,221.7),initialize=115.6)
m.x389 = Var(within=Reals,bounds=(115.6,221.7),initialize=115.6)
m.x390 = Var(within=Reals,bounds=(37.8,221.1),initialize=37.8)
m.x391 = Var(within=Reals,bounds=(37.8,221.1),initialize=37.8)
m.x392 = Var(within=Reals,bounds=(82.2,176.7),initialize=82.2)
m.x393 = Var(within=Reals,bounds=(82.2,176.7),initialize=82.2)
m.x394 = Var(within=Reals,bounds=(93.3,204.4),initialize=93.3)
m.x395 = Var(within=Reals,bounds=(93.3,204.4),initialize=93.3)
m.x396 = Var(within=Reals,bounds=(60,160),initialize=60)
m.x397 = Var(within=Reals,bounds=(60,160),initialize=60)
m.x398 = Var(within=Reals,bounds=(115.6,221.7),initialize=115.6)
m.x399 = Var(within=Reals,bounds=(115.6,221.7),initialize=115.6)
m.x400 = Var(within=Reals,bounds=(37.8,221.1),initialize=37.8)
m.x401 = Var(within=Reals,bounds=(37.8,221.1),initialize=37.8)
m.x402 = Var(within=Reals,bounds=(82.2,176.7),initialize=82.2)
m.x403 = Var(within=Reals,bounds=(82.2,176.7),initialize=82.2)
m.x404 = Var(within=Reals,bounds=(93.3,204.4),initialize=93.3)
m.x405 = Var(within=Reals,bounds=(93.3,204.4),initialize=93.3)
m.x406 = Var(within=Reals,bounds=(60,160),initialize=60)
m.x407 = Var(within=Reals,bounds=(60,160),initialize=60)
m.x408 = Var(within=Reals,bounds=(115.6,221.7),initialize=115.6)
m.x409 = Var(within=Reals,bounds=(115.6,221.7),initialize=115.6)
m.x410 = Var(within=Reals,bounds=(37.8,221.1),initialize=37.8)
m.x411 = Var(within=Reals,bounds=(37.8,221.1),initialize=37.8)
m.x412 = Var(within=Reals,bounds=(82.2,176.7),initialize=82.2)
m.x413 = Var(within=Reals,bounds=(82.2,176.7),initialize=82.2)
m.x414 = Var(within=Reals,bounds=(93.3,204.4),initialize=93.3)
m.x415 = Var(within=Reals,bounds=(93.3,204.4),initialize=93.3)
m.x416 = Var(within=Reals,bounds=(60,160),initialize=60)
m.x417 = Var(within=Reals,bounds=(60,160),initialize=60)
m.x418 = Var(within=Reals,bounds=(115.6,221.7),initialize=115.6)
m.x419 = Var(within=Reals,bounds=(115.6,221.7),initialize=115.6)
m.x420 = Var(within=Reals,bounds=(37.8,221.1),initialize=37.8)
m.x421 = Var(within=Reals,bounds=(37.8,221.1),initialize=37.8)
m.x422 = Var(within=Reals,bounds=(82.2,176.7),initialize=82.2)
m.x423 = Var(within=Reals,bounds=(82.2,176.7),initialize=82.2)
m.x424 = Var(within=Reals,bounds=(93.3,204.4),initialize=93.3)
m.x425 = Var(within=Reals,bounds=(93.3,204.4),initialize=93.3)
m.x426 = Var(within=Reals,bounds=(60,160),initialize=60)
m.x427 = Var(within=Reals,bounds=(60,160),initialize=60)
m.x428 = Var(within=Reals,bounds=(115.6,221.7),initialize=115.6)
m.x429 = Var(within=Reals,bounds=(115.6,221.7),initialize=115.6)
m.x430 = Var(within=Reals,bounds=(37.8,221.1),initialize=37.8)
m.x431 = Var(within=Reals,bounds=(37.8,221.1),initialize=37.8)
m.x432 = Var(within=Reals,bounds=(82.2,176.7),initialize=82.2)
m.x433 = Var(within=Reals,bounds=(82.2,176.7),initialize=82.2)
m.x434 = Var(within=Reals,bounds=(93.3,204.4),initialize=93.3)
m.x435 = Var(within=Reals,bounds=(93.3,204.4),initialize=93.3)
m.x436 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x437 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x438 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x439 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x440 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x441 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x442 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x443 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x444 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x445 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x446 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x447 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x448 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x449 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x450 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x451 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x452 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x453 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x454 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x455 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x456 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x457 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x458 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x459 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x460 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x461 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x462 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x463 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x464 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x465 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x466 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x467 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x468 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x469 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x470 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x471 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x472 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x473 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x474 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x475 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x476 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x477 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x478 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x479 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x480 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x481 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x482 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x483 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x484 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x485 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x486 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x487 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x488 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x489 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x490 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x491 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x492 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x493 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x494 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x495 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x496 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x497 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x498 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x499 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x500 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x501 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x502 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x503 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x504 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x505 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x506 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x507 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x508 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x509 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x510 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x511 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x512 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x513 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x514 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x515 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x516 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x517 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x518 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x519 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x520 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x521 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x522 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x523 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x524 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x525 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x526 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x527 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x528 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x529 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x530 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x531 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x532 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x533 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x534 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x535 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x536 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x537 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x538 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x539 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x540 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x541 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x542 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x543 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x544 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x545 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x546 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x547 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x548 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x549 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x550 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x551 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x552 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x553 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x554 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x555 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x556 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x557 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x558 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x559 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x560 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x561 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x562 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x563 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x564 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x565 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x566 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x567 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x568 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x569 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x570 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x571 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x572 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x573 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x574 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x575 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x576 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x577 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x578 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x579 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x580 = Var(within=Reals,bounds=(0,None),initialize=0)

m.obj = Objective(expr=146*(0.01 + m.x496)**0.6 + 146*(0.01 + m.x497)**0.6 + 146*(0.01 + m.x498)**0.6 + 146*(0.01 + 
                       m.x499)**0.6 + 146*(0.01 + m.x500)**0.6 + 146*(0.01 + m.x501)**0.6 + 146*(0.01 + m.x502)**0.6 + 
                       146*(0.01 + m.x503)**0.6 + 146*(0.01 + m.x504)**0.6 + 146*(0.01 + m.x505)**0.6 + 146*(0.01 + 
                       m.x506)**0.6 + 146*(0.01 + m.x507)**0.6 + 146*(0.01 + m.x508)**0.6 + 146*(0.01 + m.x509)**0.6 + 
                       146*(0.01 + m.x510)**0.6 + 146*(0.01 + m.x511)**0.6 + 146*(0.01 + m.x512)**0.6 + 146*(0.01 + 
                       m.x513)**0.6 + 146*(0.01 + m.x514)**0.6 + 146*(0.01 + m.x515)**0.6 + 146*(0.01 + m.x516)**0.6 + 
                       146*(0.01 + m.x517)**0.6 + 146*(0.01 + m.x518)**0.6 + 146*(0.01 + m.x519)**0.6 + 146*(0.01 + 
                       m.x520)**0.6 + 146*(0.01 + m.x521)**0.6 + 146*(0.01 + m.x522)**0.6 + 146*(0.01 + m.x523)**0.6 + 
                       146*(0.01 + m.x524)**0.6 + 146*(0.01 + m.x525)**0.6 + 146*(0.01 + m.x526)**0.6 + 146*(0.01 + 
                       m.x527)**0.6 + 146*(0.01 + m.x528)**0.6 + 146*(0.01 + m.x529)**0.6 + 146*(0.01 + m.x530)**0.6 + 
                       146*(0.01 + m.x531)**0.6 + 146*(0.01 + m.x532)**0.6 + 146*(0.01 + m.x533)**0.6 + 146*(0.01 + 
                       m.x534)**0.6 + 146*(0.01 + m.x535)**0.6 + 146*(0.01 + m.x536)**0.6 + 146*(0.01 + m.x537)**0.6 + 
                       146*(0.01 + m.x538)**0.6 + 146*(0.01 + m.x539)**0.6 + 146*(0.01 + m.x540)**0.6 + 146*(0.01 + 
                       m.x541)**0.6 + 146*(0.01 + m.x542)**0.6 + 146*(0.01 + m.x543)**0.6 + 146*(0.01 + m.x544)**0.6 + 
                       146*(0.01 + m.x545)**0.6 + 146*(0.01 + m.x546)**0.6 + 146*(0.01 + m.x547)**0.6 + 146*(0.01 + 
                       m.x548)**0.6 + 146*(0.01 + m.x549)**0.6 + 146*(0.01 + m.x550)**0.6 + 146*(0.01 + m.x551)**0.6 + 
                       146*(0.01 + m.x552)**0.6 + 146*(0.01 + m.x553)**0.6 + 146*(0.01 + m.x554)**0.6 + 146*(0.01 + 
                       m.x555)**0.6 + 146*(0.01 + m.x556)**0.6 + 146*(0.01 + m.x557)**0.6 + 146*(0.01 + m.x558)**0.6 + 
                       146*(0.01 + m.x559)**0.6 + 146*(0.01 + m.x560)**0.6 + 146*(0.01 + m.x561)**0.6 + 146*(0.01 + 
                       m.x562)**0.6 + 146*(0.01 + m.x563)**0.6 + 146*(0.01 + m.x564)**0.6 + 146*(0.01 + m.x565)**0.6 + 
                       146*(0.01 + m.x566)**0.6 + 146*(0.01 + m.x567)**0.6 + 146*(0.01 + m.x568)**0.6 + 146*(0.01 + 
                       m.x569)**0.6 + 146*(0.01 + m.x570)**0.6 + 146*(0.01 + m.x571)**0.6 + 146*(0.01 + m.x572)**0.6 + 
                       146*(0.01 + m.x573)**0.6 + 146*(0.01 + m.x574)**0.6 + 146*(0.01 + m.x575)**0.6 + 146*(0.01 + 
                       m.x576)**0.6 + 146*(0.01 + m.x577)**0.6 + 146*(0.01 + m.x578)**0.6 + 146*(0.01 + m.x579)**0.6 + 
                       146*(0.01 + m.x580)**0.6 + 4000*m.b1 + 4000*m.b2 + 4000*m.b3 + 4000*m.b4 + 4000*m.b5 + 4000*m.b6
                        + 4000*m.b7 + 4000*m.b8 + 4000*m.b9 + 4000*m.b10 + 4000*m.b11 + 4000*m.b12 + 4000*m.b13
                        + 4000*m.b14 + 4000*m.b15 + 4000*m.b16 + 4000*m.b17 + 4000*m.b18 + 4000*m.b19 + 4000*m.b20
                        + 4000*m.b21 + 4000*m.b22 + 4000*m.b23 + 4000*m.b24 + 4000*m.b25 + 4000*m.b26 + 4000*m.b27
                        + 4000*m.b28 + 4000*m.b29 + 4000*m.b30 + 4000*m.b31 + 4000*m.b32 + 4000*m.b33 + 4000*m.b34
                        + 4000*m.b35 + 4000*m.b36 + 4000*m.b37 + 4000*m.b38 + 4000*m.b39 + 4000*m.b40 + 4000*m.b41
                        + 4000*m.b42 + 4000*m.b43 + 4000*m.b44 + 4000*m.b45 + 4000*m.b46 + 4000*m.b47 + 4000*m.b48
                        + 4000*m.b49 + 4000*m.b50 + 4000*m.b51 + 4000*m.b52 + 4000*m.b53 + 4000*m.b54 + 4000*m.b55
                        + 4000*m.b56 + 4000*m.b57 + 4000*m.b58 + 4000*m.b59 + 4000*m.b60 + 10*m.x141 + 10*m.x142
                        + 10*m.x143 + 10*m.x144 + 10*m.x145 + 200*m.x146 + 200*m.x147 + 200*m.x148 + 200*m.x149
                        + 200*m.x150, sense=minimize)

m.c1 = Constraint(expr=   8.8*m.x61 - 8.8*m.x62 - m.x91 - m.x93 - m.x95 - m.x97 - m.x99 == 0)

m.c2 = Constraint(expr=   8.8*m.x62 - 8.8*m.x63 - m.x92 - m.x94 - m.x96 - m.x98 - m.x100 == 0)

m.c3 = Constraint(expr=   10.6*m.x64 - 10.6*m.x65 - m.x101 - m.x103 - m.x105 - m.x107 - m.x109 == 0)

m.c4 = Constraint(expr=   10.6*m.x65 - 10.6*m.x66 - m.x102 - m.x104 - m.x106 - m.x108 - m.x110 == 0)

m.c5 = Constraint(expr=   14.8*m.x67 - 14.8*m.x68 - m.x111 - m.x113 - m.x115 - m.x117 - m.x119 == 0)

m.c6 = Constraint(expr=   14.8*m.x68 - 14.8*m.x69 - m.x112 - m.x114 - m.x116 - m.x118 - m.x120 == 0)

m.c7 = Constraint(expr=   12.6*m.x70 - 12.6*m.x71 - m.x121 - m.x123 - m.x125 - m.x127 - m.x129 == 0)

m.c8 = Constraint(expr=   12.6*m.x71 - 12.6*m.x72 - m.x122 - m.x124 - m.x126 - m.x128 - m.x130 == 0)

m.c9 = Constraint(expr=   17.7*m.x73 - 17.7*m.x74 - m.x131 - m.x133 - m.x135 - m.x137 - m.x139 == 0)

m.c10 = Constraint(expr=   17.7*m.x74 - 17.7*m.x75 - m.x132 - m.x134 - m.x136 - m.x138 - m.x140 == 0)

m.c11 = Constraint(expr=   7.6*m.x76 - 7.6*m.x77 - m.x91 - m.x101 - m.x111 - m.x121 - m.x131 == 0)

m.c12 = Constraint(expr=   7.6*m.x77 - 7.6*m.x78 - m.x92 - m.x102 - m.x112 - m.x122 - m.x132 == 0)

m.c13 = Constraint(expr=   6.1*m.x79 - 6.1*m.x80 - m.x93 - m.x103 - m.x113 - m.x123 - m.x133 == 0)

m.c14 = Constraint(expr=   6.1*m.x80 - 6.1*m.x81 - m.x94 - m.x104 - m.x114 - m.x124 - m.x134 == 0)

m.c15 = Constraint(expr=   8.4*m.x82 - 8.4*m.x83 - m.x95 - m.x105 - m.x115 - m.x125 - m.x135 == 0)

m.c16 = Constraint(expr=   8.4*m.x83 - 8.4*m.x84 - m.x96 - m.x106 - m.x116 - m.x126 - m.x136 == 0)

m.c17 = Constraint(expr=   17.3*m.x85 - 17.3*m.x86 - m.x97 - m.x107 - m.x117 - m.x127 - m.x137 == 0)

m.c18 = Constraint(expr=   17.3*m.x86 - 17.3*m.x87 - m.x98 - m.x108 - m.x118 - m.x128 - m.x138 == 0)

m.c19 = Constraint(expr=   13.9*m.x88 - 13.9*m.x89 - m.x99 - m.x109 - m.x119 - m.x129 - m.x139 == 0)

m.c20 = Constraint(expr=   13.9*m.x89 - 13.9*m.x90 - m.x100 - m.x110 - m.x120 - m.x130 - m.x140 == 0)

m.c21 = Constraint(expr=   8.8*m.x63 - m.x141 == 821.04)

m.c22 = Constraint(expr=   10.6*m.x66 - m.x142 == 1460.68)

m.c23 = Constraint(expr=   14.8*m.x69 - m.x143 == 970.88)

m.c24 = Constraint(expr=   12.6*m.x72 - m.x144 == 1876.14)

m.c25 = Constraint(expr=   17.7*m.x75 - m.x145 == 1161.12)

m.c26 = Constraint(expr= - m.x91 - m.x92 - m.x93 - m.x94 - m.x95 - m.x96 - m.x97 - m.x98 - m.x99 - m.x100 - m.x141
                         == -586.96)

m.c27 = Constraint(expr= - m.x101 - m.x102 - m.x103 - m.x104 - m.x105 - m.x106 - m.x107 - m.x108 - m.x109 - m.x110
                         - m.x142 == -1177.66)

m.c28 = Constraint(expr= - m.x111 - m.x112 - m.x113 - m.x114 - m.x115 - m.x116 - m.x117 - m.x118 - m.x119 - m.x120
                         - m.x143 == -2384.28)

m.c29 = Constraint(expr= - m.x121 - m.x122 - m.x123 - m.x124 - m.x125 - m.x126 - m.x127 - m.x128 - m.x129 - m.x130
                         - m.x144 == -1539.72)

m.c30 = Constraint(expr= - m.x131 - m.x132 - m.x133 - m.x134 - m.x135 - m.x136 - m.x137 - m.x138 - m.x139 - m.x140
                         - m.x145 == -2359.41)

m.c31 = Constraint(expr= - 7.6*m.x76 - m.x146 == -1216)

m.c32 = Constraint(expr= - 6.1*m.x79 - m.x147 == -1352.37)

m.c33 = Constraint(expr= - 8.4*m.x82 - m.x148 == -1857.24)

m.c34 = Constraint(expr= - 17.3*m.x85 - m.x149 == -3056.91)

m.c35 = Constraint(expr= - 13.9*m.x88 - m.x150 == -2841.16)

m.c36 = Constraint(expr= - m.x91 - m.x92 - m.x101 - m.x102 - m.x111 - m.x112 - m.x121 - m.x122 - m.x131 - m.x132
                         - m.x146 == -760)

m.c37 = Constraint(expr= - m.x93 - m.x94 - m.x103 - m.x104 - m.x113 - m.x114 - m.x123 - m.x124 - m.x133 - m.x134
                         - m.x147 == -647.21)

m.c38 = Constraint(expr= - m.x95 - m.x96 - m.x105 - m.x106 - m.x115 - m.x116 - m.x125 - m.x126 - m.x135 - m.x136
                         - m.x148 == -1539.72)

m.c39 = Constraint(expr= - m.x97 - m.x98 - m.x107 - m.x108 - m.x117 - m.x118 - m.x127 - m.x128 - m.x137 - m.x138
                         - m.x149 == -1634.85)

m.c40 = Constraint(expr= - m.x99 - m.x100 - m.x109 - m.x110 - m.x119 - m.x120 - m.x129 - m.x130 - m.x139 - m.x140
                         - m.x150 == -1544.29)

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

m.c81 = Constraint(expr= - m.x236 - m.x238 - m.x240 - m.x242 - m.x244 == -8.8)

m.c82 = Constraint(expr= - m.x237 - m.x239 - m.x241 - m.x243 - m.x245 == -8.8)

m.c83 = Constraint(expr= - m.x246 - m.x248 - m.x250 - m.x252 - m.x254 == -10.6)

m.c84 = Constraint(expr= - m.x247 - m.x249 - m.x251 - m.x253 - m.x255 == -10.6)

m.c85 = Constraint(expr= - m.x256 - m.x258 - m.x260 - m.x262 - m.x264 == -14.8)

m.c86 = Constraint(expr= - m.x257 - m.x259 - m.x261 - m.x263 - m.x265 == -14.8)

m.c87 = Constraint(expr= - m.x266 - m.x268 - m.x270 - m.x272 - m.x274 == -12.6)

m.c88 = Constraint(expr= - m.x267 - m.x269 - m.x271 - m.x273 - m.x275 == -12.6)

m.c89 = Constraint(expr= - m.x276 - m.x278 - m.x280 - m.x282 - m.x284 == -17.7)

m.c90 = Constraint(expr= - m.x277 - m.x279 - m.x281 - m.x283 - m.x285 == -17.7)

m.c91 = Constraint(expr= - m.x286 - m.x296 - m.x306 - m.x316 - m.x326 == -7.6)

m.c92 = Constraint(expr= - m.x287 - m.x297 - m.x307 - m.x317 - m.x327 == -7.6)

m.c93 = Constraint(expr= - m.x288 - m.x298 - m.x308 - m.x318 - m.x328 == -6.1)

m.c94 = Constraint(expr= - m.x289 - m.x299 - m.x309 - m.x319 - m.x329 == -6.1)

m.c95 = Constraint(expr= - m.x290 - m.x300 - m.x310 - m.x320 - m.x330 == -8.4)

m.c96 = Constraint(expr= - m.x291 - m.x301 - m.x311 - m.x321 - m.x331 == -8.4)

m.c97 = Constraint(expr= - m.x292 - m.x302 - m.x312 - m.x322 - m.x332 == -17.3)

m.c98 = Constraint(expr= - m.x293 - m.x303 - m.x313 - m.x323 - m.x333 == -17.3)

m.c99 = Constraint(expr= - m.x294 - m.x304 - m.x314 - m.x324 - m.x334 == -13.9)

m.c100 = Constraint(expr= - m.x295 - m.x305 - m.x315 - m.x325 - m.x335 == -13.9)

m.c101 = Constraint(expr=-m.x236*(m.x61 - m.x336) + m.x91 == 0)

m.c102 = Constraint(expr=-m.x237*(m.x62 - m.x337) + m.x92 == 0)

m.c103 = Constraint(expr=-m.x238*(m.x61 - m.x338) + m.x93 == 0)

m.c104 = Constraint(expr=-m.x239*(m.x62 - m.x339) + m.x94 == 0)

m.c105 = Constraint(expr=-m.x240*(m.x61 - m.x340) + m.x95 == 0)

m.c106 = Constraint(expr=-m.x241*(m.x62 - m.x341) + m.x96 == 0)

m.c107 = Constraint(expr=-m.x242*(m.x61 - m.x342) + m.x97 == 0)

m.c108 = Constraint(expr=-m.x243*(m.x62 - m.x343) + m.x98 == 0)

m.c109 = Constraint(expr=-m.x244*(m.x61 - m.x344) + m.x99 == 0)

m.c110 = Constraint(expr=-m.x245*(m.x62 - m.x345) + m.x100 == 0)

m.c111 = Constraint(expr=-m.x246*(m.x64 - m.x346) + m.x101 == 0)

m.c112 = Constraint(expr=-m.x247*(m.x65 - m.x347) + m.x102 == 0)

m.c113 = Constraint(expr=-m.x248*(m.x64 - m.x348) + m.x103 == 0)

m.c114 = Constraint(expr=-m.x249*(m.x65 - m.x349) + m.x104 == 0)

m.c115 = Constraint(expr=-m.x250*(m.x64 - m.x350) + m.x105 == 0)

m.c116 = Constraint(expr=-m.x251*(m.x65 - m.x351) + m.x106 == 0)

m.c117 = Constraint(expr=-m.x252*(m.x64 - m.x352) + m.x107 == 0)

m.c118 = Constraint(expr=-m.x253*(m.x65 - m.x353) + m.x108 == 0)

m.c119 = Constraint(expr=-m.x254*(m.x64 - m.x354) + m.x109 == 0)

m.c120 = Constraint(expr=-m.x255*(m.x65 - m.x355) + m.x110 == 0)

m.c121 = Constraint(expr=-m.x256*(m.x67 - m.x356) + m.x111 == 0)

m.c122 = Constraint(expr=-m.x257*(m.x68 - m.x357) + m.x112 == 0)

m.c123 = Constraint(expr=-m.x258*(m.x67 - m.x358) + m.x113 == 0)

m.c124 = Constraint(expr=-m.x259*(m.x68 - m.x359) + m.x114 == 0)

m.c125 = Constraint(expr=-m.x260*(m.x67 - m.x360) + m.x115 == 0)

m.c126 = Constraint(expr=-m.x261*(m.x68 - m.x361) + m.x116 == 0)

m.c127 = Constraint(expr=-m.x262*(m.x67 - m.x362) + m.x117 == 0)

m.c128 = Constraint(expr=-m.x263*(m.x68 - m.x363) + m.x118 == 0)

m.c129 = Constraint(expr=-m.x264*(m.x67 - m.x364) + m.x119 == 0)

m.c130 = Constraint(expr=-m.x265*(m.x68 - m.x365) + m.x120 == 0)

m.c131 = Constraint(expr=-m.x266*(m.x70 - m.x366) + m.x121 == 0)

m.c132 = Constraint(expr=-m.x267*(m.x71 - m.x367) + m.x122 == 0)

m.c133 = Constraint(expr=-m.x268*(m.x70 - m.x368) + m.x123 == 0)

m.c134 = Constraint(expr=-m.x269*(m.x71 - m.x369) + m.x124 == 0)

m.c135 = Constraint(expr=-m.x270*(m.x70 - m.x370) + m.x125 == 0)

m.c136 = Constraint(expr=-m.x271*(m.x71 - m.x371) + m.x126 == 0)

m.c137 = Constraint(expr=-m.x272*(m.x70 - m.x372) + m.x127 == 0)

m.c138 = Constraint(expr=-m.x273*(m.x71 - m.x373) + m.x128 == 0)

m.c139 = Constraint(expr=-m.x274*(m.x70 - m.x374) + m.x129 == 0)

m.c140 = Constraint(expr=-m.x275*(m.x71 - m.x375) + m.x130 == 0)

m.c141 = Constraint(expr=-m.x276*(m.x73 - m.x376) + m.x131 == 0)

m.c142 = Constraint(expr=-m.x277*(m.x74 - m.x377) + m.x132 == 0)

m.c143 = Constraint(expr=-m.x278*(m.x73 - m.x378) + m.x133 == 0)

m.c144 = Constraint(expr=-m.x279*(m.x74 - m.x379) + m.x134 == 0)

m.c145 = Constraint(expr=-m.x280*(m.x73 - m.x380) + m.x135 == 0)

m.c146 = Constraint(expr=-m.x281*(m.x74 - m.x381) + m.x136 == 0)

m.c147 = Constraint(expr=-m.x282*(m.x73 - m.x382) + m.x137 == 0)

m.c148 = Constraint(expr=-m.x283*(m.x74 - m.x383) + m.x138 == 0)

m.c149 = Constraint(expr=-m.x284*(m.x73 - m.x384) + m.x139 == 0)

m.c150 = Constraint(expr=-m.x285*(m.x74 - m.x385) + m.x140 == 0)

m.c151 = Constraint(expr=-m.x286*(m.x386 - m.x77) + m.x91 == 0)

m.c152 = Constraint(expr=-m.x287*(m.x387 - m.x78) + m.x92 == 0)

m.c153 = Constraint(expr=-m.x288*(m.x388 - m.x80) + m.x93 == 0)

m.c154 = Constraint(expr=-m.x289*(m.x389 - m.x81) + m.x94 == 0)

m.c155 = Constraint(expr=-m.x290*(m.x390 - m.x83) + m.x95 == 0)

m.c156 = Constraint(expr=-m.x291*(m.x391 - m.x84) + m.x96 == 0)

m.c157 = Constraint(expr=-m.x292*(m.x392 - m.x86) + m.x97 == 0)

m.c158 = Constraint(expr=-m.x293*(m.x393 - m.x87) + m.x98 == 0)

m.c159 = Constraint(expr=-m.x294*(m.x394 - m.x89) + m.x99 == 0)

m.c160 = Constraint(expr=-m.x295*(m.x395 - m.x90) + m.x100 == 0)

m.c161 = Constraint(expr=-m.x296*(m.x396 - m.x77) + m.x101 == 0)

m.c162 = Constraint(expr=-m.x297*(m.x397 - m.x78) + m.x102 == 0)

m.c163 = Constraint(expr=-m.x298*(m.x398 - m.x80) + m.x103 == 0)

m.c164 = Constraint(expr=-m.x299*(m.x399 - m.x81) + m.x104 == 0)

m.c165 = Constraint(expr=-m.x300*(m.x400 - m.x83) + m.x105 == 0)

m.c166 = Constraint(expr=-m.x301*(m.x401 - m.x84) + m.x106 == 0)

m.c167 = Constraint(expr=-m.x302*(m.x402 - m.x86) + m.x107 == 0)

m.c168 = Constraint(expr=-m.x303*(m.x403 - m.x87) + m.x108 == 0)

m.c169 = Constraint(expr=-m.x304*(m.x404 - m.x89) + m.x109 == 0)

m.c170 = Constraint(expr=-m.x305*(m.x405 - m.x90) + m.x110 == 0)

m.c171 = Constraint(expr=-m.x306*(m.x406 - m.x77) + m.x111 == 0)

m.c172 = Constraint(expr=-m.x307*(m.x407 - m.x78) + m.x112 == 0)

m.c173 = Constraint(expr=-m.x308*(m.x408 - m.x80) + m.x113 == 0)

m.c174 = Constraint(expr=-m.x309*(m.x409 - m.x81) + m.x114 == 0)

m.c175 = Constraint(expr=-m.x310*(m.x410 - m.x83) + m.x115 == 0)

m.c176 = Constraint(expr=-m.x311*(m.x411 - m.x84) + m.x116 == 0)

m.c177 = Constraint(expr=-m.x312*(m.x412 - m.x86) + m.x117 == 0)

m.c178 = Constraint(expr=-m.x313*(m.x413 - m.x87) + m.x118 == 0)

m.c179 = Constraint(expr=-m.x314*(m.x414 - m.x89) + m.x119 == 0)

m.c180 = Constraint(expr=-m.x315*(m.x415 - m.x90) + m.x120 == 0)

m.c181 = Constraint(expr=-m.x316*(m.x416 - m.x77) + m.x121 == 0)

m.c182 = Constraint(expr=-m.x317*(m.x417 - m.x78) + m.x122 == 0)

m.c183 = Constraint(expr=-m.x318*(m.x418 - m.x80) + m.x123 == 0)

m.c184 = Constraint(expr=-m.x319*(m.x419 - m.x81) + m.x124 == 0)

m.c185 = Constraint(expr=-m.x320*(m.x420 - m.x83) + m.x125 == 0)

m.c186 = Constraint(expr=-m.x321*(m.x421 - m.x84) + m.x126 == 0)

m.c187 = Constraint(expr=-m.x322*(m.x422 - m.x86) + m.x127 == 0)

m.c188 = Constraint(expr=-m.x323*(m.x423 - m.x87) + m.x128 == 0)

m.c189 = Constraint(expr=-m.x324*(m.x424 - m.x89) + m.x129 == 0)

m.c190 = Constraint(expr=-m.x325*(m.x425 - m.x90) + m.x130 == 0)

m.c191 = Constraint(expr=-m.x326*(m.x426 - m.x77) + m.x131 == 0)

m.c192 = Constraint(expr=-m.x327*(m.x427 - m.x78) + m.x132 == 0)

m.c193 = Constraint(expr=-m.x328*(m.x428 - m.x80) + m.x133 == 0)

m.c194 = Constraint(expr=-m.x329*(m.x429 - m.x81) + m.x134 == 0)

m.c195 = Constraint(expr=-m.x330*(m.x430 - m.x83) + m.x135 == 0)

m.c196 = Constraint(expr=-m.x331*(m.x431 - m.x84) + m.x136 == 0)

m.c197 = Constraint(expr=-m.x332*(m.x432 - m.x86) + m.x137 == 0)

m.c198 = Constraint(expr=-m.x333*(m.x433 - m.x87) + m.x138 == 0)

m.c199 = Constraint(expr=-m.x334*(m.x434 - m.x89) + m.x139 == 0)

m.c200 = Constraint(expr=-m.x335*(m.x435 - m.x90) + m.x140 == 0)

m.c201 = Constraint(expr=-(m.x236*m.x336 + m.x238*m.x338 + m.x240*m.x340 + m.x242*m.x342 + m.x244*m.x344) + 8.8*m.x62
                          == 0)

m.c202 = Constraint(expr=-(m.x237*m.x337 + m.x239*m.x339 + m.x241*m.x341 + m.x243*m.x343 + m.x245*m.x345) + 8.8*m.x63
                          == 0)

m.c203 = Constraint(expr=-(m.x246*m.x346 + m.x248*m.x348 + m.x250*m.x350 + m.x252*m.x352 + m.x254*m.x354) + 10.6*m.x65
                          == 0)

m.c204 = Constraint(expr=-(m.x247*m.x347 + m.x249*m.x349 + m.x251*m.x351 + m.x253*m.x353 + m.x255*m.x355) + 10.6*m.x66
                          == 0)

m.c205 = Constraint(expr=-(m.x256*m.x356 + m.x258*m.x358 + m.x260*m.x360 + m.x262*m.x362 + m.x264*m.x364) + 14.8*m.x68
                          == 0)

m.c206 = Constraint(expr=-(m.x257*m.x357 + m.x259*m.x359 + m.x261*m.x361 + m.x263*m.x363 + m.x265*m.x365) + 14.8*m.x69
                          == 0)

m.c207 = Constraint(expr=-(m.x266*m.x366 + m.x268*m.x368 + m.x270*m.x370 + m.x272*m.x372 + m.x274*m.x374) + 12.6*m.x71
                          == 0)

m.c208 = Constraint(expr=-(m.x267*m.x367 + m.x269*m.x369 + m.x271*m.x371 + m.x273*m.x373 + m.x275*m.x375) + 12.6*m.x72
                          == 0)

m.c209 = Constraint(expr=-(m.x276*m.x376 + m.x278*m.x378 + m.x280*m.x380 + m.x282*m.x382 + m.x284*m.x384) + 17.7*m.x74
                          == 0)

m.c210 = Constraint(expr=-(m.x277*m.x377 + m.x279*m.x379 + m.x281*m.x381 + m.x283*m.x383 + m.x285*m.x385) + 17.7*m.x75
                          == 0)

m.c211 = Constraint(expr=-(m.x286*m.x386 + m.x296*m.x396 + m.x306*m.x406 + m.x316*m.x416 + m.x326*m.x426) + 7.6*m.x76
                          == 0)

m.c212 = Constraint(expr=-(m.x287*m.x387 + m.x297*m.x397 + m.x307*m.x407 + m.x317*m.x417 + m.x327*m.x427) + 7.6*m.x77
                          == 0)

m.c213 = Constraint(expr=-(m.x288*m.x388 + m.x298*m.x398 + m.x308*m.x408 + m.x318*m.x418 + m.x328*m.x428) + 6.1*m.x79
                          == 0)

m.c214 = Constraint(expr=-(m.x289*m.x389 + m.x299*m.x399 + m.x309*m.x409 + m.x319*m.x419 + m.x329*m.x429) + 6.1*m.x80
                          == 0)

m.c215 = Constraint(expr=-(m.x290*m.x390 + m.x300*m.x400 + m.x310*m.x410 + m.x320*m.x420 + m.x330*m.x430) + 8.4*m.x82
                          == 0)

m.c216 = Constraint(expr=-(m.x291*m.x391 + m.x301*m.x401 + m.x311*m.x411 + m.x321*m.x421 + m.x331*m.x431) + 8.4*m.x83
                          == 0)

m.c217 = Constraint(expr=-(m.x292*m.x392 + m.x302*m.x402 + m.x312*m.x412 + m.x322*m.x422 + m.x332*m.x432) + 17.3*m.x85
                          == 0)

m.c218 = Constraint(expr=-(m.x293*m.x393 + m.x303*m.x403 + m.x313*m.x413 + m.x323*m.x423 + m.x333*m.x433) + 17.3*m.x86
                          == 0)

m.c219 = Constraint(expr=-(m.x294*m.x394 + m.x304*m.x404 + m.x314*m.x414 + m.x324*m.x424 + m.x334*m.x434) + 13.9*m.x88
                          == 0)

m.c220 = Constraint(expr=-(m.x295*m.x395 + m.x305*m.x405 + m.x315*m.x415 + m.x325*m.x425 + m.x335*m.x435) + 13.9*m.x89
                          == 0)

m.c221 = Constraint(expr=-(m.x151 - m.x152)/log(m.x151/(1e-6 + m.x152)) + m.x436 == 0)

m.c222 = Constraint(expr=-(m.x152 - m.x153)/log(m.x152/(1e-6 + m.x153)) + m.x437 == 0)

m.c223 = Constraint(expr=-(m.x154 - m.x155)/log(m.x154/(1e-6 + m.x155)) + m.x438 == 0)

m.c224 = Constraint(expr=-(m.x155 - m.x156)/log(m.x155/(1e-6 + m.x156)) + m.x439 == 0)

m.c225 = Constraint(expr=-(m.x157 - m.x158)/log(m.x157/(1e-6 + m.x158)) + m.x440 == 0)

m.c226 = Constraint(expr=-(m.x158 - m.x159)/log(m.x158/(1e-6 + m.x159)) + m.x441 == 0)

m.c227 = Constraint(expr=-(m.x160 - m.x161)/log(m.x160/(1e-6 + m.x161)) + m.x442 == 0)

m.c228 = Constraint(expr=-(m.x161 - m.x162)/log(m.x161/(1e-6 + m.x162)) + m.x443 == 0)

m.c229 = Constraint(expr=-(m.x163 - m.x164)/log(m.x163/(1e-6 + m.x164)) + m.x444 == 0)

m.c230 = Constraint(expr=-(m.x164 - m.x165)/log(m.x164/(1e-6 + m.x165)) + m.x445 == 0)

m.c231 = Constraint(expr=-(m.x166 - m.x167)/log(m.x166/(1e-6 + m.x167)) + m.x446 == 0)

m.c232 = Constraint(expr=-(m.x167 - m.x168)/log(m.x167/(1e-6 + m.x168)) + m.x447 == 0)

m.c233 = Constraint(expr=-(m.x169 - m.x170)/log(m.x169/(1e-6 + m.x170)) + m.x448 == 0)

m.c234 = Constraint(expr=-(m.x170 - m.x171)/log(m.x170/(1e-6 + m.x171)) + m.x449 == 0)

m.c235 = Constraint(expr=-(m.x172 - m.x173)/log(m.x172/(1e-6 + m.x173)) + m.x450 == 0)

m.c236 = Constraint(expr=-(m.x173 - m.x174)/log(m.x173/(1e-6 + m.x174)) + m.x451 == 0)

m.c237 = Constraint(expr=-(m.x175 - m.x176)/log(m.x175/(1e-6 + m.x176)) + m.x452 == 0)

m.c238 = Constraint(expr=-(m.x176 - m.x177)/log(m.x176/(1e-6 + m.x177)) + m.x453 == 0)

m.c239 = Constraint(expr=-(m.x178 - m.x179)/log(m.x178/(1e-6 + m.x179)) + m.x454 == 0)

m.c240 = Constraint(expr=-(m.x179 - m.x180)/log(m.x179/(1e-6 + m.x180)) + m.x455 == 0)

m.c241 = Constraint(expr=-(m.x181 - m.x182)/log(m.x181/(1e-6 + m.x182)) + m.x456 == 0)

m.c242 = Constraint(expr=-(m.x182 - m.x183)/log(m.x182/(1e-6 + m.x183)) + m.x457 == 0)

m.c243 = Constraint(expr=-(m.x184 - m.x185)/log(m.x184/(1e-6 + m.x185)) + m.x458 == 0)

m.c244 = Constraint(expr=-(m.x185 - m.x186)/log(m.x185/(1e-6 + m.x186)) + m.x459 == 0)

m.c245 = Constraint(expr=-(m.x187 - m.x188)/log(m.x187/(1e-6 + m.x188)) + m.x460 == 0)

m.c246 = Constraint(expr=-(m.x188 - m.x189)/log(m.x188/(1e-6 + m.x189)) + m.x461 == 0)

m.c247 = Constraint(expr=-(m.x190 - m.x191)/log(m.x190/(1e-6 + m.x191)) + m.x462 == 0)

m.c248 = Constraint(expr=-(m.x191 - m.x192)/log(m.x191/(1e-6 + m.x192)) + m.x463 == 0)

m.c249 = Constraint(expr=-(m.x193 - m.x194)/log(m.x193/(1e-6 + m.x194)) + m.x464 == 0)

m.c250 = Constraint(expr=-(m.x194 - m.x195)/log(m.x194/(1e-6 + m.x195)) + m.x465 == 0)

m.c251 = Constraint(expr=-(m.x196 - m.x197)/log(m.x196/(1e-6 + m.x197)) + m.x466 == 0)

m.c252 = Constraint(expr=-(m.x197 - m.x198)/log(m.x197/(1e-6 + m.x198)) + m.x467 == 0)

m.c253 = Constraint(expr=-(m.x199 - m.x200)/log(m.x199/(1e-6 + m.x200)) + m.x468 == 0)

m.c254 = Constraint(expr=-(m.x200 - m.x201)/log(m.x200/(1e-6 + m.x201)) + m.x469 == 0)

m.c255 = Constraint(expr=-(m.x202 - m.x203)/log(m.x202/(1e-6 + m.x203)) + m.x470 == 0)

m.c256 = Constraint(expr=-(m.x203 - m.x204)/log(m.x203/(1e-6 + m.x204)) + m.x471 == 0)

m.c257 = Constraint(expr=-(m.x205 - m.x206)/log(m.x205/(1e-6 + m.x206)) + m.x472 == 0)

m.c258 = Constraint(expr=-(m.x206 - m.x207)/log(m.x206/(1e-6 + m.x207)) + m.x473 == 0)

m.c259 = Constraint(expr=-(m.x208 - m.x209)/log(m.x208/(1e-6 + m.x209)) + m.x474 == 0)

m.c260 = Constraint(expr=-(m.x209 - m.x210)/log(m.x209/(1e-6 + m.x210)) + m.x475 == 0)

m.c261 = Constraint(expr=-(m.x211 - m.x212)/log(m.x211/(1e-6 + m.x212)) + m.x476 == 0)

m.c262 = Constraint(expr=-(m.x212 - m.x213)/log(m.x212/(1e-6 + m.x213)) + m.x477 == 0)

m.c263 = Constraint(expr=-(m.x214 - m.x215)/log(m.x214/(1e-6 + m.x215)) + m.x478 == 0)

m.c264 = Constraint(expr=-(m.x215 - m.x216)/log(m.x215/(1e-6 + m.x216)) + m.x479 == 0)

m.c265 = Constraint(expr=-(m.x217 - m.x218)/log(m.x217/(1e-6 + m.x218)) + m.x480 == 0)

m.c266 = Constraint(expr=-(m.x218 - m.x219)/log(m.x218/(1e-6 + m.x219)) + m.x481 == 0)

m.c267 = Constraint(expr=-(m.x220 - m.x221)/log(m.x220/(1e-6 + m.x221)) + m.x482 == 0)

m.c268 = Constraint(expr=-(m.x221 - m.x222)/log(m.x221/(1e-6 + m.x222)) + m.x483 == 0)

m.c269 = Constraint(expr=-(m.x223 - m.x224)/log(m.x223/(1e-6 + m.x224)) + m.x484 == 0)

m.c270 = Constraint(expr=-(m.x224 - m.x225)/log(m.x224/(1e-6 + m.x225)) + m.x485 == 0)

m.c271 = Constraint(expr=-1.17647058823529*m.x91/(0.01 + m.x436) + m.x496 == 0)

m.c272 = Constraint(expr=-1.17647058823529*m.x92/(0.01 + m.x437) + m.x497 == 0)

m.c273 = Constraint(expr=-1.17647058823529*m.x93/(0.01 + m.x438) + m.x499 == 0)

m.c274 = Constraint(expr=-1.17647058823529*m.x94/(0.01 + m.x439) + m.x500 == 0)

m.c275 = Constraint(expr=-1.17647058823529*m.x95/(0.01 + m.x440) + m.x502 == 0)

m.c276 = Constraint(expr=-1.17647058823529*m.x96/(0.01 + m.x441) + m.x503 == 0)

m.c277 = Constraint(expr=-1.17647058823529*m.x97/(0.01 + m.x442) + m.x505 == 0)

m.c278 = Constraint(expr=-1.17647058823529*m.x98/(0.01 + m.x443) + m.x506 == 0)

m.c279 = Constraint(expr=-1.17647058823529*m.x99/(0.01 + m.x444) + m.x508 == 0)

m.c280 = Constraint(expr=-1.17647058823529*m.x100/(0.01 + m.x445) + m.x509 == 0)

m.c281 = Constraint(expr=-1.17647058823529*m.x101/(0.01 + m.x446) + m.x511 == 0)

m.c282 = Constraint(expr=-1.17647058823529*m.x102/(0.01 + m.x447) + m.x512 == 0)

m.c283 = Constraint(expr=-1.17647058823529*m.x103/(0.01 + m.x448) + m.x514 == 0)

m.c284 = Constraint(expr=-1.17647058823529*m.x104/(0.01 + m.x449) + m.x515 == 0)

m.c285 = Constraint(expr=-1.17647058823529*m.x105/(0.01 + m.x450) + m.x517 == 0)

m.c286 = Constraint(expr=-1.17647058823529*m.x106/(0.01 + m.x451) + m.x518 == 0)

m.c287 = Constraint(expr=-1.17647058823529*m.x107/(0.01 + m.x452) + m.x520 == 0)

m.c288 = Constraint(expr=-1.17647058823529*m.x108/(0.01 + m.x453) + m.x521 == 0)

m.c289 = Constraint(expr=-1.17647058823529*m.x109/(0.01 + m.x454) + m.x523 == 0)

m.c290 = Constraint(expr=-1.17647058823529*m.x110/(0.01 + m.x455) + m.x524 == 0)

m.c291 = Constraint(expr=-1.17647058823529*m.x111/(0.01 + m.x456) + m.x526 == 0)

m.c292 = Constraint(expr=-1.17647058823529*m.x112/(0.01 + m.x457) + m.x527 == 0)

m.c293 = Constraint(expr=-1.17647058823529*m.x113/(0.01 + m.x458) + m.x529 == 0)

m.c294 = Constraint(expr=-1.17647058823529*m.x114/(0.01 + m.x459) + m.x530 == 0)

m.c295 = Constraint(expr=-1.17647058823529*m.x115/(0.01 + m.x460) + m.x532 == 0)

m.c296 = Constraint(expr=-1.17647058823529*m.x116/(0.01 + m.x461) + m.x533 == 0)

m.c297 = Constraint(expr=-1.17647058823529*m.x117/(0.01 + m.x462) + m.x535 == 0)

m.c298 = Constraint(expr=-1.17647058823529*m.x118/(0.01 + m.x463) + m.x536 == 0)

m.c299 = Constraint(expr=-1.17647058823529*m.x119/(0.01 + m.x464) + m.x538 == 0)

m.c300 = Constraint(expr=-1.17647058823529*m.x120/(0.01 + m.x465) + m.x539 == 0)

m.c301 = Constraint(expr=-1.17647058823529*m.x121/(0.01 + m.x466) + m.x541 == 0)

m.c302 = Constraint(expr=-1.17647058823529*m.x122/(0.01 + m.x467) + m.x542 == 0)

m.c303 = Constraint(expr=-1.17647058823529*m.x123/(0.01 + m.x468) + m.x544 == 0)

m.c304 = Constraint(expr=-1.17647058823529*m.x124/(0.01 + m.x469) + m.x545 == 0)

m.c305 = Constraint(expr=-1.17647058823529*m.x125/(0.01 + m.x470) + m.x547 == 0)

m.c306 = Constraint(expr=-1.17647058823529*m.x126/(0.01 + m.x471) + m.x548 == 0)

m.c307 = Constraint(expr=-1.17647058823529*m.x127/(0.01 + m.x472) + m.x550 == 0)

m.c308 = Constraint(expr=-1.17647058823529*m.x128/(0.01 + m.x473) + m.x551 == 0)

m.c309 = Constraint(expr=-1.17647058823529*m.x129/(0.01 + m.x474) + m.x553 == 0)

m.c310 = Constraint(expr=-1.17647058823529*m.x130/(0.01 + m.x475) + m.x554 == 0)

m.c311 = Constraint(expr=-1.17647058823529*m.x131/(0.01 + m.x476) + m.x556 == 0)

m.c312 = Constraint(expr=-1.17647058823529*m.x132/(0.01 + m.x477) + m.x557 == 0)

m.c313 = Constraint(expr=-1.17647058823529*m.x133/(0.01 + m.x478) + m.x559 == 0)

m.c314 = Constraint(expr=-1.17647058823529*m.x134/(0.01 + m.x479) + m.x560 == 0)

m.c315 = Constraint(expr=-1.17647058823529*m.x135/(0.01 + m.x480) + m.x562 == 0)

m.c316 = Constraint(expr=-1.17647058823529*m.x136/(0.01 + m.x481) + m.x563 == 0)

m.c317 = Constraint(expr=-1.17647058823529*m.x137/(0.01 + m.x482) + m.x565 == 0)

m.c318 = Constraint(expr=-1.17647058823529*m.x138/(0.01 + m.x483) + m.x566 == 0)

m.c319 = Constraint(expr=-1.17647058823529*m.x139/(0.01 + m.x484) + m.x568 == 0)

m.c320 = Constraint(expr=-1.17647058823529*m.x140/(0.01 + m.x485) + m.x569 == 0)

m.c321 = Constraint(expr=-(-68.3 + m.x226)/log(0.0146412882190148*m.x226) + m.x486 == 0)

m.c322 = Constraint(expr=-(-112.8 + m.x227)/log(0.00886524814835773*m.x227) + m.x487 == 0)

m.c323 = Constraint(expr=-(-40.6 + m.x228)/log(0.0246305412652576*m.x228) + m.x488 == 0)

m.c324 = Constraint(expr=-(-123.9 + m.x229)/log(0.00807102495503612*m.x229) + m.x489 == 0)

m.c325 = Constraint(expr=-(-40.6 + m.x230)/log(0.0246305412652576*m.x230) + m.x490 == 0)

m.c326 = Constraint(expr=-(-80 + m.x231)/log(0.01249999984375*m.x231) + m.x491 == 0)

m.c327 = Constraint(expr=-(-18.3 + m.x232)/log(0.0546448057571144*m.x232) + m.x492 == 0)

m.c328 = Constraint(expr=-(-18.9 + m.x233)/log(0.0529100501105793*m.x233) + m.x493 == 0)

m.c329 = Constraint(expr=-(-63.3 + m.x234)/log(0.0157977880600665*m.x234) + m.x494 == 0)

m.c330 = Constraint(expr=-(-35.6 + m.x235)/log(0.0280898868514077*m.x235) + m.x495 == 0)

m.c331 = Constraint(expr=-1.17647058823529*m.x141/(0.01 + m.x486) + m.x571 == 0)

m.c332 = Constraint(expr=-1.17647058823529*m.x142/(0.01 + m.x487) + m.x572 == 0)

m.c333 = Constraint(expr=-1.17647058823529*m.x143/(0.01 + m.x488) + m.x573 == 0)

m.c334 = Constraint(expr=-1.17647058823529*m.x144/(0.01 + m.x489) + m.x574 == 0)

m.c335 = Constraint(expr=-1.17647058823529*m.x145/(0.01 + m.x490) + m.x575 == 0)

m.c336 = Constraint(expr=-0.882352941176471*m.x146/(0.01 + m.x491) + m.x576 == 0)

m.c337 = Constraint(expr=-0.882352941176471*m.x147/(0.01 + m.x492) + m.x577 == 0)

m.c338 = Constraint(expr=-0.882352941176471*m.x148/(0.01 + m.x493) + m.x578 == 0)

m.c339 = Constraint(expr=-0.882352941176471*m.x149/(0.01 + m.x494) + m.x579 == 0)

m.c340 = Constraint(expr=-0.882352941176471*m.x150/(0.01 + m.x495) + m.x580 == 0)

m.c341 = Constraint(expr= - 586.96*m.b1 + m.x91 <= 0)

m.c342 = Constraint(expr= - 586.96*m.b2 + m.x92 <= 0)

m.c343 = Constraint(expr= - 586.96*m.b3 + m.x93 <= 0)

m.c344 = Constraint(expr= - 586.96*m.b4 + m.x94 <= 0)

m.c345 = Constraint(expr= - 586.96*m.b5 + m.x95 <= 0)

m.c346 = Constraint(expr= - 586.96*m.b6 + m.x96 <= 0)

m.c347 = Constraint(expr= - 586.96*m.b7 + m.x97 <= 0)

m.c348 = Constraint(expr= - 586.96*m.b8 + m.x98 <= 0)

m.c349 = Constraint(expr= - 586.96*m.b9 + m.x99 <= 0)

m.c350 = Constraint(expr= - 586.96*m.b10 + m.x100 <= 0)

m.c351 = Constraint(expr= - 760*m.b11 + m.x101 <= 0)

m.c352 = Constraint(expr= - 760*m.b12 + m.x102 <= 0)

m.c353 = Constraint(expr= - 647.21*m.b13 + m.x103 <= 0)

m.c354 = Constraint(expr= - 647.21*m.b14 + m.x104 <= 0)

m.c355 = Constraint(expr= - 1177.66*m.b15 + m.x105 <= 0)

m.c356 = Constraint(expr= - 1177.66*m.b16 + m.x106 <= 0)

m.c357 = Constraint(expr= - 1177.66*m.b17 + m.x107 <= 0)

m.c358 = Constraint(expr= - 1177.66*m.b18 + m.x108 <= 0)

m.c359 = Constraint(expr= - 1177.66*m.b19 + m.x109 <= 0)

m.c360 = Constraint(expr= - 1177.66*m.b20 + m.x110 <= 0)

m.c361 = Constraint(expr= - 760*m.b21 + m.x111 <= 0)

m.c362 = Constraint(expr= - 760*m.b22 + m.x112 <= 0)

m.c363 = Constraint(expr= - 647.21*m.b23 + m.x113 <= 0)

m.c364 = Constraint(expr= - 647.21*m.b24 + m.x114 <= 0)

m.c365 = Constraint(expr= - 1539.72*m.b25 + m.x115 <= 0)

m.c366 = Constraint(expr= - 1539.72*m.b26 + m.x116 <= 0)

m.c367 = Constraint(expr= - 1634.85*m.b27 + m.x117 <= 0)

m.c368 = Constraint(expr= - 1634.85*m.b28 + m.x118 <= 0)

m.c369 = Constraint(expr= - 1544.29*m.b29 + m.x119 <= 0)

m.c370 = Constraint(expr= - 1544.29*m.b30 + m.x120 <= 0)

m.c371 = Constraint(expr= - 760*m.b31 + m.x121 <= 0)

m.c372 = Constraint(expr= - 760*m.b32 + m.x122 <= 0)

m.c373 = Constraint(expr= - 647.21*m.b33 + m.x123 <= 0)

m.c374 = Constraint(expr= - 647.21*m.b34 + m.x124 <= 0)

m.c375 = Constraint(expr= - 1539.72*m.b35 + m.x125 <= 0)

m.c376 = Constraint(expr= - 1539.72*m.b36 + m.x126 <= 0)

m.c377 = Constraint(expr= - 1539.72*m.b37 + m.x127 <= 0)

m.c378 = Constraint(expr= - 1539.72*m.b38 + m.x128 <= 0)

m.c379 = Constraint(expr= - 1539.72*m.b39 + m.x129 <= 0)

m.c380 = Constraint(expr= - 1539.72*m.b40 + m.x130 <= 0)

m.c381 = Constraint(expr= - 760*m.b41 + m.x131 <= 0)

m.c382 = Constraint(expr= - 760*m.b42 + m.x132 <= 0)

m.c383 = Constraint(expr= - 647.21*m.b43 + m.x133 <= 0)

m.c384 = Constraint(expr= - 647.21*m.b44 + m.x134 <= 0)

m.c385 = Constraint(expr= - 1539.72*m.b45 + m.x135 <= 0)

m.c386 = Constraint(expr= - 1539.72*m.b46 + m.x136 <= 0)

m.c387 = Constraint(expr= - 1634.85*m.b47 + m.x137 <= 0)

m.c388 = Constraint(expr= - 1634.85*m.b48 + m.x138 <= 0)

m.c389 = Constraint(expr= - 1544.29*m.b49 + m.x139 <= 0)

m.c390 = Constraint(expr= - 1544.29*m.b50 + m.x140 <= 0)

m.c391 = Constraint(expr= - 760*m.b56 + m.x146 <= 0)

m.c392 = Constraint(expr= - 647.21*m.b57 + m.x147 <= 0)

m.c393 = Constraint(expr= - 1539.72*m.b58 + m.x148 <= 0)

m.c394 = Constraint(expr= - 1634.85*m.b59 + m.x149 <= 0)

m.c395 = Constraint(expr= - 1544.29*m.b60 + m.x150 <= 0)

m.c396 = Constraint(expr= - 586.96*m.b51 + m.x141 <= 0)

m.c397 = Constraint(expr= - 1177.66*m.b52 + m.x142 <= 0)

m.c398 = Constraint(expr= - 2384.28*m.b53 + m.x143 <= 0)

m.c399 = Constraint(expr= - 1539.72*m.b54 + m.x144 <= 0)

m.c400 = Constraint(expr= - 2359.41*m.b55 + m.x145 <= 0)

m.c401 = Constraint(expr=   66.7*m.b1 - m.x61 + m.x76 + m.x151 <= 66.7)

m.c402 = Constraint(expr=   66.7*m.b2 - m.x62 + m.x77 + m.x152 <= 66.7)

m.c403 = Constraint(expr=   128.4*m.b3 - m.x61 + m.x79 + m.x154 <= 128.4)

m.c404 = Constraint(expr=   128.4*m.b4 - m.x62 + m.x80 + m.x155 <= 128.4)

m.c405 = Constraint(expr=   127.8*m.b5 - m.x61 + m.x82 + m.x157 <= 127.8)

m.c406 = Constraint(expr=   127.8*m.b6 - m.x62 + m.x83 + m.x158 <= 127.8)

m.c407 = Constraint(expr=   83.4*m.b7 - m.x61 + m.x85 + m.x160 <= 83.4)

m.c408 = Constraint(expr=   83.4*m.b8 - m.x62 + m.x86 + m.x161 <= 83.4)

m.c409 = Constraint(expr=   111.1*m.b9 - m.x61 + m.x88 + m.x163 <= 111.1)

m.c410 = Constraint(expr=   111.1*m.b10 - m.x62 + m.x89 + m.x164 <= 111.1)

m.c411 = Constraint(expr=   22.2*m.b11 - m.x64 + m.x76 + m.x166 <= 22.2)

m.c412 = Constraint(expr=   22.2*m.b12 - m.x65 + m.x77 + m.x167 <= 22.2)

m.c413 = Constraint(expr=   83.9*m.b13 - m.x64 + m.x79 + m.x169 <= 83.9)

m.c414 = Constraint(expr=   83.9*m.b14 - m.x65 + m.x80 + m.x170 <= 83.9)

m.c415 = Constraint(expr=   83.3*m.b15 - m.x64 + m.x82 + m.x172 <= 83.3)

m.c416 = Constraint(expr=   83.3*m.b16 - m.x65 + m.x83 + m.x173 <= 83.3)

m.c417 = Constraint(expr=   38.9*m.b17 - m.x64 + m.x85 + m.x175 <= 38.9)

m.c418 = Constraint(expr=   38.9*m.b18 - m.x65 + m.x86 + m.x176 <= 38.9)

m.c419 = Constraint(expr=   66.6*m.b19 - m.x64 + m.x88 + m.x178 <= 66.6)

m.c420 = Constraint(expr=   66.6*m.b20 - m.x65 + m.x89 + m.x179 <= 66.6)

m.c421 = Constraint(expr=   94.4*m.b21 - m.x67 + m.x76 + m.x181 <= 94.4)

m.c422 = Constraint(expr=   94.4*m.b22 - m.x68 + m.x77 + m.x182 <= 94.4)

m.c423 = Constraint(expr=   156.1*m.b23 - m.x67 + m.x79 + m.x184 <= 156.1)

m.c424 = Constraint(expr=   156.1*m.b24 - m.x68 + m.x80 + m.x185 <= 156.1)

m.c425 = Constraint(expr=   155.5*m.b25 - m.x67 + m.x82 + m.x187 <= 155.5)

m.c426 = Constraint(expr=   155.5*m.b26 - m.x68 + m.x83 + m.x188 <= 155.5)

m.c427 = Constraint(expr=   111.1*m.b27 - m.x67 + m.x85 + m.x190 <= 111.1)

m.c428 = Constraint(expr=   111.1*m.b28 - m.x68 + m.x86 + m.x191 <= 111.1)

m.c429 = Constraint(expr=   138.8*m.b29 - m.x67 + m.x88 + m.x193 <= 138.8)

m.c430 = Constraint(expr=   138.8*m.b30 - m.x68 + m.x89 + m.x194 <= 138.8)

m.c431 = Constraint(expr=   11.1*m.b31 - m.x70 + m.x76 + m.x196 <= 11.1)

m.c432 = Constraint(expr=   11.1*m.b32 - m.x71 + m.x77 + m.x197 <= 11.1)

m.c433 = Constraint(expr=   72.8*m.b33 - m.x70 + m.x79 + m.x199 <= 72.8)

m.c434 = Constraint(expr=   72.8*m.b34 - m.x71 + m.x80 + m.x200 <= 72.8)

m.c435 = Constraint(expr=   72.2*m.b35 - m.x70 + m.x82 + m.x202 <= 72.2)

m.c436 = Constraint(expr=   72.2*m.b36 - m.x71 + m.x83 + m.x203 <= 72.2)

m.c437 = Constraint(expr=   27.8*m.b37 - m.x70 + m.x85 + m.x205 <= 27.8)

m.c438 = Constraint(expr=   27.8*m.b38 - m.x71 + m.x86 + m.x206 <= 27.8)

m.c439 = Constraint(expr=   55.5*m.b39 - m.x70 + m.x88 + m.x208 <= 55.5)

m.c440 = Constraint(expr=   55.5*m.b40 - m.x71 + m.x89 + m.x209 <= 55.5)

m.c441 = Constraint(expr=   94.4*m.b41 - m.x73 + m.x76 + m.x211 <= 94.4)

m.c442 = Constraint(expr=   94.4*m.b42 - m.x74 + m.x77 + m.x212 <= 94.4)

m.c443 = Constraint(expr=   156.1*m.b43 - m.x73 + m.x79 + m.x214 <= 156.1)

m.c444 = Constraint(expr=   156.1*m.b44 - m.x74 + m.x80 + m.x215 <= 156.1)

m.c445 = Constraint(expr=   155.5*m.b45 - m.x73 + m.x82 + m.x217 <= 155.5)

m.c446 = Constraint(expr=   155.5*m.b46 - m.x74 + m.x83 + m.x218 <= 155.5)

m.c447 = Constraint(expr=   111.1*m.b47 - m.x73 + m.x85 + m.x220 <= 111.1)

m.c448 = Constraint(expr=   111.1*m.b48 - m.x74 + m.x86 + m.x221 <= 111.1)

m.c449 = Constraint(expr=   138.8*m.b49 - m.x73 + m.x88 + m.x223 <= 138.8)

m.c450 = Constraint(expr=   138.8*m.b50 - m.x74 + m.x89 + m.x224 <= 138.8)

m.c451 = Constraint(expr=   66.7*m.b1 - m.x62 + m.x77 + m.x152 <= 66.7)

m.c452 = Constraint(expr=   66.7*m.b2 - m.x63 + m.x78 + m.x153 <= 66.7)

m.c453 = Constraint(expr=   128.4*m.b3 - m.x62 + m.x80 + m.x155 <= 128.4)

m.c454 = Constraint(expr=   128.4*m.b4 - m.x63 + m.x81 + m.x156 <= 128.4)

m.c455 = Constraint(expr=   127.8*m.b5 - m.x62 + m.x83 + m.x158 <= 127.8)

m.c456 = Constraint(expr=   127.8*m.b6 - m.x63 + m.x84 + m.x159 <= 127.8)

m.c457 = Constraint(expr=   83.4*m.b7 - m.x62 + m.x86 + m.x161 <= 83.4)

m.c458 = Constraint(expr=   83.4*m.b8 - m.x63 + m.x87 + m.x162 <= 83.4)

m.c459 = Constraint(expr=   111.1*m.b9 - m.x62 + m.x89 + m.x164 <= 111.1)

m.c460 = Constraint(expr=   111.1*m.b10 - m.x63 + m.x90 + m.x165 <= 111.1)

m.c461 = Constraint(expr=   22.2*m.b11 - m.x65 + m.x77 + m.x167 <= 22.2)

m.c462 = Constraint(expr=   22.2*m.b12 - m.x66 + m.x78 + m.x168 <= 22.2)

m.c463 = Constraint(expr=   83.9*m.b13 - m.x65 + m.x80 + m.x170 <= 83.9)

m.c464 = Constraint(expr=   83.9*m.b14 - m.x66 + m.x81 + m.x171 <= 83.9)

m.c465 = Constraint(expr=   83.3*m.b15 - m.x65 + m.x83 + m.x173 <= 83.3)

m.c466 = Constraint(expr=   83.3*m.b16 - m.x66 + m.x84 + m.x174 <= 83.3)

m.c467 = Constraint(expr=   38.9*m.b17 - m.x65 + m.x86 + m.x176 <= 38.9)

m.c468 = Constraint(expr=   38.9*m.b18 - m.x66 + m.x87 + m.x177 <= 38.9)

m.c469 = Constraint(expr=   66.6*m.b19 - m.x65 + m.x89 + m.x179 <= 66.6)

m.c470 = Constraint(expr=   66.6*m.b20 - m.x66 + m.x90 + m.x180 <= 66.6)

m.c471 = Constraint(expr=   94.4*m.b21 - m.x68 + m.x77 + m.x182 <= 94.4)

m.c472 = Constraint(expr=   94.4*m.b22 - m.x69 + m.x78 + m.x183 <= 94.4)

m.c473 = Constraint(expr=   156.1*m.b23 - m.x68 + m.x80 + m.x185 <= 156.1)

m.c474 = Constraint(expr=   156.1*m.b24 - m.x69 + m.x81 + m.x186 <= 156.1)

m.c475 = Constraint(expr=   155.5*m.b25 - m.x68 + m.x83 + m.x188 <= 155.5)

m.c476 = Constraint(expr=   155.5*m.b26 - m.x69 + m.x84 + m.x189 <= 155.5)

m.c477 = Constraint(expr=   111.1*m.b27 - m.x68 + m.x86 + m.x191 <= 111.1)

m.c478 = Constraint(expr=   111.1*m.b28 - m.x69 + m.x87 + m.x192 <= 111.1)

m.c479 = Constraint(expr=   138.8*m.b29 - m.x68 + m.x89 + m.x194 <= 138.8)

m.c480 = Constraint(expr=   138.8*m.b30 - m.x69 + m.x90 + m.x195 <= 138.8)

m.c481 = Constraint(expr=   11.1*m.b31 - m.x71 + m.x77 + m.x197 <= 11.1)

m.c482 = Constraint(expr=   11.1*m.b32 - m.x72 + m.x78 + m.x198 <= 11.1)

m.c483 = Constraint(expr=   72.8*m.b33 - m.x71 + m.x80 + m.x200 <= 72.8)

m.c484 = Constraint(expr=   72.8*m.b34 - m.x72 + m.x81 + m.x201 <= 72.8)

m.c485 = Constraint(expr=   72.2*m.b35 - m.x71 + m.x83 + m.x203 <= 72.2)

m.c486 = Constraint(expr=   72.2*m.b36 - m.x72 + m.x84 + m.x204 <= 72.2)

m.c487 = Constraint(expr=   27.8*m.b37 - m.x71 + m.x86 + m.x206 <= 27.8)

m.c488 = Constraint(expr=   27.8*m.b38 - m.x72 + m.x87 + m.x207 <= 27.8)

m.c489 = Constraint(expr=   55.5*m.b39 - m.x71 + m.x89 + m.x209 <= 55.5)

m.c490 = Constraint(expr=   55.5*m.b40 - m.x72 + m.x90 + m.x210 <= 55.5)

m.c491 = Constraint(expr=   94.4*m.b41 - m.x74 + m.x77 + m.x212 <= 94.4)

m.c492 = Constraint(expr=   94.4*m.b42 - m.x75 + m.x78 + m.x213 <= 94.4)

m.c493 = Constraint(expr=   156.1*m.b43 - m.x74 + m.x80 + m.x215 <= 156.1)

m.c494 = Constraint(expr=   156.1*m.b44 - m.x75 + m.x81 + m.x216 <= 156.1)

m.c495 = Constraint(expr=   155.5*m.b45 - m.x74 + m.x83 + m.x218 <= 155.5)

m.c496 = Constraint(expr=   155.5*m.b46 - m.x75 + m.x84 + m.x219 <= 155.5)

m.c497 = Constraint(expr=   111.1*m.b47 - m.x74 + m.x86 + m.x221 <= 111.1)

m.c498 = Constraint(expr=   111.1*m.b48 - m.x75 + m.x87 + m.x222 <= 111.1)

m.c499 = Constraint(expr=   138.8*m.b49 - m.x74 + m.x89 + m.x224 <= 138.8)

m.c500 = Constraint(expr=   138.8*m.b50 - m.x75 + m.x90 + m.x225 <= 138.8)

m.c501 = Constraint(expr= - m.x63 + m.x226 <= -40)

m.c502 = Constraint(expr= - m.x66 + m.x227 <= -40)

m.c503 = Constraint(expr= - m.x69 + m.x228 <= -40)

m.c504 = Constraint(expr= - m.x72 + m.x229 <= -40)

m.c505 = Constraint(expr= - m.x75 + m.x230 <= -40)

m.c506 = Constraint(expr=   m.x76 + m.x231 <= 240)

m.c507 = Constraint(expr=   m.x79 + m.x232 <= 240)

m.c508 = Constraint(expr=   m.x82 + m.x233 <= 240)

m.c509 = Constraint(expr=   m.x85 + m.x234 <= 240)

m.c510 = Constraint(expr=   m.x88 + m.x235 <= 240)
