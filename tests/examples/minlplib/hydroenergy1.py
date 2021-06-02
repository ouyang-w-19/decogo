#  MINLP written by GAMS Convert at 04/21/18 13:52:24
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        429       97      144      188        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        289      193       96        0        0        0        0        0
#  FX      2        2        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1213     1093      120        0
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
m.b61 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b62 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b63 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b64 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b65 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b66 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b67 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b68 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b69 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b70 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b71 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b72 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b73 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b74 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b75 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b76 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b77 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b78 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b79 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b80 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b81 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b82 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b83 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b84 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b85 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b86 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b87 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b88 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b89 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b90 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b91 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b92 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b93 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b94 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b95 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b96 = Var(within=Binary,bounds=(0,1),initialize=0)
m.x97 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x98 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x99 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x100 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x101 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x102 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x103 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x104 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x105 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x106 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x107 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x108 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x109 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x110 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x111 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x112 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x113 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x114 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x115 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x116 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x117 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x118 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x119 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x120 = Var(within=Reals,bounds=(0,188.08),initialize=0)
m.x121 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x122 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x123 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x124 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x125 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x126 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x127 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x128 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x129 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x130 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x131 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x132 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x133 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x134 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x135 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x136 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x137 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x138 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x139 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x140 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x141 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x142 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x143 = Var(within=Reals,bounds=(0,237.14),initialize=0)
m.x144 = Var(within=Reals,bounds=(0,237.14),initialize=0)
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
m.x170 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x171 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x172 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x173 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x174 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x175 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x176 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x177 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x178 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x179 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x180 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x181 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x182 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x183 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x184 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x185 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x186 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x187 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x188 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x189 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x190 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x191 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x192 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x193 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x194 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x195 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x196 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x197 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x198 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x199 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x200 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x201 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x202 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x203 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x204 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x205 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x206 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x207 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x208 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x209 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x210 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x211 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x212 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x213 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x214 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x215 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x216 = Var(within=Reals,bounds=(0,4.1202),initialize=0)
m.x217 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x218 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x219 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x220 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x221 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x222 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x223 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x224 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x225 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x226 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x227 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x228 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x229 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x230 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x231 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x232 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x233 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x234 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x235 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x236 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x237 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x238 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x239 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x240 = Var(within=Reals,bounds=(0,3.888),initialize=0)
m.x241 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x242 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x243 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x244 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x245 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x246 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x247 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x248 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x249 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x250 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x251 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x252 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x253 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x254 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x255 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x256 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x257 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x258 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x259 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x260 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x261 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x262 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x263 = Var(within=Reals,bounds=(5.18,12.94),initialize=5.18)
m.x264 = Var(within=Reals,bounds=(10.35,10.35),initialize=10.35)
m.x265 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x266 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x267 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x268 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x269 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x270 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x271 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x272 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x273 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x274 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x275 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x276 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x277 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x278 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x279 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x280 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x281 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x282 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x283 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x284 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x285 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x286 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x287 = Var(within=Reals,bounds=(5.32,13.3),initialize=5.32)
m.x288 = Var(within=Reals,bounds=(10.64,10.64),initialize=10.64)

m.obj = Objective(expr= - 470.2*m.b49 - 470.2*m.b50 - 470.2*m.b51 - 470.2*m.b52 - 470.2*m.b53 - 470.2*m.b54
                        - 470.2*m.b55 - 470.2*m.b56 - 470.2*m.b57 - 470.2*m.b58 - 470.2*m.b59 - 470.2*m.b60
                        - 470.2*m.b61 - 470.2*m.b62 - 470.2*m.b63 - 470.2*m.b64 - 470.2*m.b65 - 470.2*m.b66
                        - 470.2*m.b67 - 470.2*m.b68 - 470.2*m.b69 - 470.2*m.b70 - 470.2*m.b71 - 470.2*m.b72
                        - 592.85*m.b73 - 592.85*m.b74 - 592.85*m.b75 - 592.85*m.b76 - 592.85*m.b77 - 592.85*m.b78
                        - 592.85*m.b79 - 592.85*m.b80 - 592.85*m.b81 - 592.85*m.b82 - 592.85*m.b83 - 592.85*m.b84
                        - 592.85*m.b85 - 592.85*m.b86 - 592.85*m.b87 - 592.85*m.b88 - 592.85*m.b89 - 592.85*m.b90
                        - 592.85*m.b91 - 592.85*m.b92 - 592.85*m.b93 - 592.85*m.b94 - 592.85*m.b95 - 592.85*m.b96
                        + 50.4*m.x97 + 46.287*m.x98 + 44.187*m.x99 + 44.787*m.x100 + 45.477*m.x101 + 47.523*m.x102
                        + 58.359*m.x103 + 68.487*m.x104 + 87.441*m.x105 + 91.395*m.x106 + 93.846*m.x107 + 94.995*m.x108
                        + 86.187*m.x109 + 92.295*m.x110 + 93.495*m.x111 + 92.259*m.x112 + 93.795*m.x113 + 103.254*m.x114
                        + 103.359*m.x115 + 100.623*m.x116 + 95.418*m.x117 + 92.136*m.x118 + 82.305*m.x119
                        + 68.946*m.x120 + 50.4*m.x121 + 46.287*m.x122 + 44.187*m.x123 + 44.787*m.x124 + 45.477*m.x125
                        + 47.523*m.x126 + 58.359*m.x127 + 68.487*m.x128 + 87.441*m.x129 + 91.395*m.x130 + 93.846*m.x131
                        + 94.995*m.x132 + 86.187*m.x133 + 92.295*m.x134 + 93.495*m.x135 + 92.259*m.x136 + 93.795*m.x137
                        + 103.254*m.x138 + 103.359*m.x139 + 100.623*m.x140 + 95.418*m.x141 + 92.136*m.x142
                        + 82.305*m.x143 + 68.946*m.x144, sense=maximize)

m.c2 = Constraint(expr=   m.x145 + m.x193 + m.x241 == 10.4208)

m.c3 = Constraint(expr=   m.x146 + m.x194 - m.x241 + m.x242 == 0.0708)

m.c4 = Constraint(expr=   m.x147 + m.x195 - m.x242 + m.x243 == 0.0708)

m.c5 = Constraint(expr=   m.x148 + m.x196 - m.x243 + m.x244 == 0.0708)

m.c6 = Constraint(expr=   m.x149 + m.x197 - m.x244 + m.x245 == 0.0708)

m.c7 = Constraint(expr=   m.x150 + m.x198 - m.x245 + m.x246 == 0.0708)

m.c8 = Constraint(expr=   m.x151 + m.x199 - m.x246 + m.x247 == 0.7374)

m.c9 = Constraint(expr=   m.x152 + m.x200 - m.x247 + m.x248 == 0.7374)

m.c10 = Constraint(expr=   m.x153 + m.x201 - m.x248 + m.x249 == 0.7374)

m.c11 = Constraint(expr=   m.x154 + m.x202 - m.x249 + m.x250 == 0.7374)

m.c12 = Constraint(expr=   m.x155 + m.x203 - m.x250 + m.x251 == 0.7374)

m.c13 = Constraint(expr=   m.x156 + m.x204 - m.x251 + m.x252 == 0.7374)

m.c14 = Constraint(expr=   m.x157 + m.x205 - m.x252 + m.x253 == 0.7374)

m.c15 = Constraint(expr=   m.x158 + m.x206 - m.x253 + m.x254 == 0.7374)

m.c16 = Constraint(expr=   m.x159 + m.x207 - m.x254 + m.x255 == 0.7374)

m.c17 = Constraint(expr=   m.x160 + m.x208 - m.x255 + m.x256 == 0.7374)

m.c18 = Constraint(expr=   m.x161 + m.x209 - m.x256 + m.x257 == 0.7374)

m.c19 = Constraint(expr=   m.x162 + m.x210 - m.x257 + m.x258 == 0.7374)

m.c20 = Constraint(expr=   m.x163 + m.x211 - m.x258 + m.x259 == 0.7374)

m.c21 = Constraint(expr=   m.x164 + m.x212 - m.x259 + m.x260 == 0.7374)

m.c22 = Constraint(expr=   m.x165 + m.x213 - m.x260 + m.x261 == 0.7374)

m.c23 = Constraint(expr=   m.x166 + m.x214 - m.x261 + m.x262 == 0.7374)

m.c24 = Constraint(expr=   m.x167 + m.x215 - m.x262 + m.x263 == 0.7374)

m.c25 = Constraint(expr=   m.x168 + m.x216 - m.x263 + m.x264 == 0.7374)

m.c26 = Constraint(expr= - m.x145 + m.x169 - m.x193 + m.x217 + m.x265 == 10.7948)

m.c27 = Constraint(expr= - m.x146 + m.x170 - m.x194 + m.x218 - m.x265 + m.x266 == 0.1548)

m.c28 = Constraint(expr= - m.x147 + m.x171 - m.x195 + m.x219 - m.x266 + m.x267 == 0.1548)

m.c29 = Constraint(expr= - m.x148 + m.x172 - m.x196 + m.x220 - m.x267 + m.x268 == 0.1548)

m.c30 = Constraint(expr= - m.x149 + m.x173 - m.x197 + m.x221 - m.x268 + m.x269 == 0.1548)

m.c31 = Constraint(expr= - m.x150 + m.x174 - m.x198 + m.x222 - m.x269 + m.x270 == 0.1548)

m.c32 = Constraint(expr= - m.x151 + m.x175 - m.x199 + m.x223 - m.x270 + m.x271 == 0.1548)

m.c33 = Constraint(expr= - m.x152 + m.x176 - m.x200 + m.x224 - m.x271 + m.x272 == 0.1548)

m.c34 = Constraint(expr= - m.x153 + m.x177 - m.x201 + m.x225 - m.x272 + m.x273 == 0.1548)

m.c35 = Constraint(expr= - m.x154 + m.x178 - m.x202 + m.x226 - m.x273 + m.x274 == 0.1548)

m.c36 = Constraint(expr= - m.x155 + m.x179 - m.x203 + m.x227 - m.x274 + m.x275 == 0.1548)

m.c37 = Constraint(expr= - m.x156 + m.x180 - m.x204 + m.x228 - m.x275 + m.x276 == 0.1548)

m.c38 = Constraint(expr= - m.x157 + m.x181 - m.x205 + m.x229 - m.x276 + m.x277 == 0.1548)

m.c39 = Constraint(expr= - m.x158 + m.x182 - m.x206 + m.x230 - m.x277 + m.x278 == 0.1548)

m.c40 = Constraint(expr= - m.x159 + m.x183 - m.x207 + m.x231 - m.x278 + m.x279 == 0.1548)

m.c41 = Constraint(expr= - m.x160 + m.x184 - m.x208 + m.x232 - m.x279 + m.x280 == 0.1548)

m.c42 = Constraint(expr= - m.x161 + m.x185 - m.x209 + m.x233 - m.x280 + m.x281 == 0.1548)

m.c43 = Constraint(expr= - m.x162 + m.x186 - m.x210 + m.x234 - m.x281 + m.x282 == 0.1548)

m.c44 = Constraint(expr= - m.x163 + m.x187 - m.x211 + m.x235 - m.x282 + m.x283 == 0.1548)

m.c45 = Constraint(expr= - m.x164 + m.x188 - m.x212 + m.x236 - m.x283 + m.x284 == 0.1548)

m.c46 = Constraint(expr= - m.x165 + m.x189 - m.x213 + m.x237 - m.x284 + m.x285 == 0.1548)

m.c47 = Constraint(expr= - m.x166 + m.x190 - m.x214 + m.x238 - m.x285 + m.x286 == 0.1548)

m.c48 = Constraint(expr= - m.x167 + m.x191 - m.x215 + m.x239 - m.x286 + m.x287 == 0.1548)

m.c49 = Constraint(expr= - m.x168 + m.x192 - m.x216 + m.x240 - m.x287 + m.x288 == 0.1548)

m.c50 = Constraint(expr= - 4.1202*m.b1 + m.x193 <= 0)

m.c51 = Constraint(expr= - 4.1202*m.b2 + m.x194 <= 0)

m.c52 = Constraint(expr= - 4.1202*m.b3 + m.x195 <= 0)

m.c53 = Constraint(expr= - 4.1202*m.b4 + m.x196 <= 0)

m.c54 = Constraint(expr= - 4.1202*m.b5 + m.x197 <= 0)

m.c55 = Constraint(expr= - 4.1202*m.b6 + m.x198 <= 0)

m.c56 = Constraint(expr= - 4.1202*m.b7 + m.x199 <= 0)

m.c57 = Constraint(expr= - 4.1202*m.b8 + m.x200 <= 0)

m.c58 = Constraint(expr= - 4.1202*m.b9 + m.x201 <= 0)

m.c59 = Constraint(expr= - 4.1202*m.b10 + m.x202 <= 0)

m.c60 = Constraint(expr= - 4.1202*m.b11 + m.x203 <= 0)

m.c61 = Constraint(expr= - 4.1202*m.b12 + m.x204 <= 0)

m.c62 = Constraint(expr= - 4.1202*m.b13 + m.x205 <= 0)

m.c63 = Constraint(expr= - 4.1202*m.b14 + m.x206 <= 0)

m.c64 = Constraint(expr= - 4.1202*m.b15 + m.x207 <= 0)

m.c65 = Constraint(expr= - 4.1202*m.b16 + m.x208 <= 0)

m.c66 = Constraint(expr= - 4.1202*m.b17 + m.x209 <= 0)

m.c67 = Constraint(expr= - 4.1202*m.b18 + m.x210 <= 0)

m.c68 = Constraint(expr= - 4.1202*m.b19 + m.x211 <= 0)

m.c69 = Constraint(expr= - 4.1202*m.b20 + m.x212 <= 0)

m.c70 = Constraint(expr= - 4.1202*m.b21 + m.x213 <= 0)

m.c71 = Constraint(expr= - 4.1202*m.b22 + m.x214 <= 0)

m.c72 = Constraint(expr= - 4.1202*m.b23 + m.x215 <= 0)

m.c73 = Constraint(expr= - 4.1202*m.b24 + m.x216 <= 0)

m.c74 = Constraint(expr= - 3.888*m.b25 + m.x217 <= 0)

m.c75 = Constraint(expr= - 3.888*m.b26 + m.x218 <= 0)

m.c76 = Constraint(expr= - 3.888*m.b27 + m.x219 <= 0)

m.c77 = Constraint(expr= - 3.888*m.b28 + m.x220 <= 0)

m.c78 = Constraint(expr= - 3.888*m.b29 + m.x221 <= 0)

m.c79 = Constraint(expr= - 3.888*m.b30 + m.x222 <= 0)

m.c80 = Constraint(expr= - 3.888*m.b31 + m.x223 <= 0)

m.c81 = Constraint(expr= - 3.888*m.b32 + m.x224 <= 0)

m.c82 = Constraint(expr= - 3.888*m.b33 + m.x225 <= 0)

m.c83 = Constraint(expr= - 3.888*m.b34 + m.x226 <= 0)

m.c84 = Constraint(expr= - 3.888*m.b35 + m.x227 <= 0)

m.c85 = Constraint(expr= - 3.888*m.b36 + m.x228 <= 0)

m.c86 = Constraint(expr= - 3.888*m.b37 + m.x229 <= 0)

m.c87 = Constraint(expr= - 3.888*m.b38 + m.x230 <= 0)

m.c88 = Constraint(expr= - 3.888*m.b39 + m.x231 <= 0)

m.c89 = Constraint(expr= - 3.888*m.b40 + m.x232 <= 0)

m.c90 = Constraint(expr= - 3.888*m.b41 + m.x233 <= 0)

m.c91 = Constraint(expr= - 3.888*m.b42 + m.x234 <= 0)

m.c92 = Constraint(expr= - 3.888*m.b43 + m.x235 <= 0)

m.c93 = Constraint(expr= - 3.888*m.b44 + m.x236 <= 0)

m.c94 = Constraint(expr= - 3.888*m.b45 + m.x237 <= 0)

m.c95 = Constraint(expr= - 3.888*m.b46 + m.x238 <= 0)

m.c96 = Constraint(expr= - 3.888*m.b47 + m.x239 <= 0)

m.c97 = Constraint(expr= - 3.888*m.b48 + m.x240 <= 0)

m.c98 = Constraint(expr= - 0.605268*m.b1 + m.x193 >= 0)

m.c99 = Constraint(expr= - 0.605268*m.b2 + m.x194 >= 0)

m.c100 = Constraint(expr= - 0.605268*m.b3 + m.x195 >= 0)

m.c101 = Constraint(expr= - 0.605268*m.b4 + m.x196 >= 0)

m.c102 = Constraint(expr= - 0.605268*m.b5 + m.x197 >= 0)

m.c103 = Constraint(expr= - 0.605268*m.b6 + m.x198 >= 0)

m.c104 = Constraint(expr= - 0.605268*m.b7 + m.x199 >= 0)

m.c105 = Constraint(expr= - 0.605268*m.b8 + m.x200 >= 0)

m.c106 = Constraint(expr= - 0.605268*m.b9 + m.x201 >= 0)

m.c107 = Constraint(expr= - 0.605268*m.b10 + m.x202 >= 0)

m.c108 = Constraint(expr= - 0.605268*m.b11 + m.x203 >= 0)

m.c109 = Constraint(expr= - 0.605268*m.b12 + m.x204 >= 0)

m.c110 = Constraint(expr= - 0.605268*m.b13 + m.x205 >= 0)

m.c111 = Constraint(expr= - 0.605268*m.b14 + m.x206 >= 0)

m.c112 = Constraint(expr= - 0.605268*m.b15 + m.x207 >= 0)

m.c113 = Constraint(expr= - 0.605268*m.b16 + m.x208 >= 0)

m.c114 = Constraint(expr= - 0.605268*m.b17 + m.x209 >= 0)

m.c115 = Constraint(expr= - 0.605268*m.b18 + m.x210 >= 0)

m.c116 = Constraint(expr= - 0.605268*m.b19 + m.x211 >= 0)

m.c117 = Constraint(expr= - 0.605268*m.b20 + m.x212 >= 0)

m.c118 = Constraint(expr= - 0.605268*m.b21 + m.x213 >= 0)

m.c119 = Constraint(expr= - 0.605268*m.b22 + m.x214 >= 0)

m.c120 = Constraint(expr= - 0.605268*m.b23 + m.x215 >= 0)

m.c121 = Constraint(expr= - 0.605268*m.b24 + m.x216 >= 0)

m.c122 = Constraint(expr= - 0.37692*m.b25 + m.x217 >= 0)

m.c123 = Constraint(expr= - 0.37692*m.b26 + m.x218 >= 0)

m.c124 = Constraint(expr= - 0.37692*m.b27 + m.x219 >= 0)

m.c125 = Constraint(expr= - 0.37692*m.b28 + m.x220 >= 0)

m.c126 = Constraint(expr= - 0.37692*m.b29 + m.x221 >= 0)

m.c127 = Constraint(expr= - 0.37692*m.b30 + m.x222 >= 0)

m.c128 = Constraint(expr= - 0.37692*m.b31 + m.x223 >= 0)

m.c129 = Constraint(expr= - 0.37692*m.b32 + m.x224 >= 0)

m.c130 = Constraint(expr= - 0.37692*m.b33 + m.x225 >= 0)

m.c131 = Constraint(expr= - 0.37692*m.b34 + m.x226 >= 0)

m.c132 = Constraint(expr= - 0.37692*m.b35 + m.x227 >= 0)

m.c133 = Constraint(expr= - 0.37692*m.b36 + m.x228 >= 0)

m.c134 = Constraint(expr= - 0.37692*m.b37 + m.x229 >= 0)

m.c135 = Constraint(expr= - 0.37692*m.b38 + m.x230 >= 0)

m.c136 = Constraint(expr= - 0.37692*m.b39 + m.x231 >= 0)

m.c137 = Constraint(expr= - 0.37692*m.b40 + m.x232 >= 0)

m.c138 = Constraint(expr= - 0.37692*m.b41 + m.x233 >= 0)

m.c139 = Constraint(expr= - 0.37692*m.b42 + m.x234 >= 0)

m.c140 = Constraint(expr= - 0.37692*m.b43 + m.x235 >= 0)

m.c141 = Constraint(expr= - 0.37692*m.b44 + m.x236 >= 0)

m.c142 = Constraint(expr= - 0.37692*m.b45 + m.x237 >= 0)

m.c143 = Constraint(expr= - 0.37692*m.b46 + m.x238 >= 0)

m.c144 = Constraint(expr= - 0.37692*m.b47 + m.x239 >= 0)

m.c145 = Constraint(expr= - 0.37692*m.b48 + m.x240 >= 0)

m.c146 = Constraint(expr= - 28*m.b1 + m.x97 >= 0)

m.c147 = Constraint(expr= - 28*m.b2 + m.x98 >= 0)

m.c148 = Constraint(expr= - 28*m.b3 + m.x99 >= 0)

m.c149 = Constraint(expr= - 28*m.b4 + m.x100 >= 0)

m.c150 = Constraint(expr= - 28*m.b5 + m.x101 >= 0)

m.c151 = Constraint(expr= - 28*m.b6 + m.x102 >= 0)

m.c152 = Constraint(expr= - 28*m.b7 + m.x103 >= 0)

m.c153 = Constraint(expr= - 28*m.b8 + m.x104 >= 0)

m.c154 = Constraint(expr= - 28*m.b9 + m.x105 >= 0)

m.c155 = Constraint(expr= - 28*m.b10 + m.x106 >= 0)

m.c156 = Constraint(expr= - 28*m.b11 + m.x107 >= 0)

m.c157 = Constraint(expr= - 28*m.b12 + m.x108 >= 0)

m.c158 = Constraint(expr= - 28*m.b13 + m.x109 >= 0)

m.c159 = Constraint(expr= - 28*m.b14 + m.x110 >= 0)

m.c160 = Constraint(expr= - 28*m.b15 + m.x111 >= 0)

m.c161 = Constraint(expr= - 28*m.b16 + m.x112 >= 0)

m.c162 = Constraint(expr= - 28*m.b17 + m.x113 >= 0)

m.c163 = Constraint(expr= - 28*m.b18 + m.x114 >= 0)

m.c164 = Constraint(expr= - 28*m.b19 + m.x115 >= 0)

m.c165 = Constraint(expr= - 28*m.b20 + m.x116 >= 0)

m.c166 = Constraint(expr= - 28*m.b21 + m.x117 >= 0)

m.c167 = Constraint(expr= - 28*m.b22 + m.x118 >= 0)

m.c168 = Constraint(expr= - 28*m.b23 + m.x119 >= 0)

m.c169 = Constraint(expr= - 28*m.b24 + m.x120 >= 0)

m.c170 = Constraint(expr= - 29.99*m.b25 + m.x121 >= 0)

m.c171 = Constraint(expr= - 29.99*m.b26 + m.x122 >= 0)

m.c172 = Constraint(expr= - 29.99*m.b27 + m.x123 >= 0)

m.c173 = Constraint(expr= - 29.99*m.b28 + m.x124 >= 0)

m.c174 = Constraint(expr= - 29.99*m.b29 + m.x125 >= 0)

m.c175 = Constraint(expr= - 29.99*m.b30 + m.x126 >= 0)

m.c176 = Constraint(expr= - 29.99*m.b31 + m.x127 >= 0)

m.c177 = Constraint(expr= - 29.99*m.b32 + m.x128 >= 0)

m.c178 = Constraint(expr= - 29.99*m.b33 + m.x129 >= 0)

m.c179 = Constraint(expr= - 29.99*m.b34 + m.x130 >= 0)

m.c180 = Constraint(expr= - 29.99*m.b35 + m.x131 >= 0)

m.c181 = Constraint(expr= - 29.99*m.b36 + m.x132 >= 0)

m.c182 = Constraint(expr= - 29.99*m.b37 + m.x133 >= 0)

m.c183 = Constraint(expr= - 29.99*m.b38 + m.x134 >= 0)

m.c184 = Constraint(expr= - 29.99*m.b39 + m.x135 >= 0)

m.c185 = Constraint(expr= - 29.99*m.b40 + m.x136 >= 0)

m.c186 = Constraint(expr= - 29.99*m.b41 + m.x137 >= 0)

m.c187 = Constraint(expr= - 29.99*m.b42 + m.x138 >= 0)

m.c188 = Constraint(expr= - 29.99*m.b43 + m.x139 >= 0)

m.c189 = Constraint(expr= - 29.99*m.b44 + m.x140 >= 0)

m.c190 = Constraint(expr= - 29.99*m.b45 + m.x141 >= 0)

m.c191 = Constraint(expr= - 29.99*m.b46 + m.x142 >= 0)

m.c192 = Constraint(expr= - 29.99*m.b47 + m.x143 >= 0)

m.c193 = Constraint(expr= - 29.99*m.b48 + m.x144 >= 0)

m.c194 = Constraint(expr= - 188.08*m.b1 + m.x97 <= 0)

m.c195 = Constraint(expr= - 188.08*m.b2 + m.x98 <= 0)

m.c196 = Constraint(expr= - 188.08*m.b3 + m.x99 <= 0)

m.c197 = Constraint(expr= - 188.08*m.b4 + m.x100 <= 0)

m.c198 = Constraint(expr= - 188.08*m.b5 + m.x101 <= 0)

m.c199 = Constraint(expr= - 188.08*m.b6 + m.x102 <= 0)

m.c200 = Constraint(expr= - 188.08*m.b7 + m.x103 <= 0)

m.c201 = Constraint(expr= - 188.08*m.b8 + m.x104 <= 0)

m.c202 = Constraint(expr= - 188.08*m.b9 + m.x105 <= 0)

m.c203 = Constraint(expr= - 188.08*m.b10 + m.x106 <= 0)

m.c204 = Constraint(expr= - 188.08*m.b11 + m.x107 <= 0)

m.c205 = Constraint(expr= - 188.08*m.b12 + m.x108 <= 0)

m.c206 = Constraint(expr= - 188.08*m.b13 + m.x109 <= 0)

m.c207 = Constraint(expr= - 188.08*m.b14 + m.x110 <= 0)

m.c208 = Constraint(expr= - 188.08*m.b15 + m.x111 <= 0)

m.c209 = Constraint(expr= - 188.08*m.b16 + m.x112 <= 0)

m.c210 = Constraint(expr= - 188.08*m.b17 + m.x113 <= 0)

m.c211 = Constraint(expr= - 188.08*m.b18 + m.x114 <= 0)

m.c212 = Constraint(expr= - 188.08*m.b19 + m.x115 <= 0)

m.c213 = Constraint(expr= - 188.08*m.b20 + m.x116 <= 0)

m.c214 = Constraint(expr= - 188.08*m.b21 + m.x117 <= 0)

m.c215 = Constraint(expr= - 188.08*m.b22 + m.x118 <= 0)

m.c216 = Constraint(expr= - 188.08*m.b23 + m.x119 <= 0)

m.c217 = Constraint(expr= - 188.08*m.b24 + m.x120 <= 0)

m.c218 = Constraint(expr= - 237.14*m.b25 + m.x121 <= 0)

m.c219 = Constraint(expr= - 237.14*m.b26 + m.x122 <= 0)

m.c220 = Constraint(expr= - 237.14*m.b27 + m.x123 <= 0)

m.c221 = Constraint(expr= - 237.14*m.b28 + m.x124 <= 0)

m.c222 = Constraint(expr= - 237.14*m.b29 + m.x125 <= 0)

m.c223 = Constraint(expr= - 237.14*m.b30 + m.x126 <= 0)

m.c224 = Constraint(expr= - 237.14*m.b31 + m.x127 <= 0)

m.c225 = Constraint(expr= - 237.14*m.b32 + m.x128 <= 0)

m.c226 = Constraint(expr= - 237.14*m.b33 + m.x129 <= 0)

m.c227 = Constraint(expr= - 237.14*m.b34 + m.x130 <= 0)

m.c228 = Constraint(expr= - 237.14*m.b35 + m.x131 <= 0)

m.c229 = Constraint(expr= - 237.14*m.b36 + m.x132 <= 0)

m.c230 = Constraint(expr= - 237.14*m.b37 + m.x133 <= 0)

m.c231 = Constraint(expr= - 237.14*m.b38 + m.x134 <= 0)

m.c232 = Constraint(expr= - 237.14*m.b39 + m.x135 <= 0)

m.c233 = Constraint(expr= - 237.14*m.b40 + m.x136 <= 0)

m.c234 = Constraint(expr= - 237.14*m.b41 + m.x137 <= 0)

m.c235 = Constraint(expr= - 237.14*m.b42 + m.x138 <= 0)

m.c236 = Constraint(expr= - 237.14*m.b43 + m.x139 <= 0)

m.c237 = Constraint(expr= - 237.14*m.b44 + m.x140 <= 0)

m.c238 = Constraint(expr= - 237.14*m.b45 + m.x141 <= 0)

m.c239 = Constraint(expr= - 237.14*m.b46 + m.x142 <= 0)

m.c240 = Constraint(expr= - 237.14*m.b47 + m.x143 <= 0)

m.c241 = Constraint(expr= - 237.14*m.b48 + m.x144 <= 0)

m.c242 = Constraint(expr=   m.x193 - m.x194 <= 2.0601)

m.c243 = Constraint(expr=   m.x194 - m.x195 <= 2.0601)

m.c244 = Constraint(expr=   m.x195 - m.x196 <= 2.0601)

m.c245 = Constraint(expr=   m.x196 - m.x197 <= 2.0601)

m.c246 = Constraint(expr=   m.x197 - m.x198 <= 2.0601)

m.c247 = Constraint(expr=   m.x198 - m.x199 <= 2.0601)

m.c248 = Constraint(expr=   m.x199 - m.x200 <= 2.0601)

m.c249 = Constraint(expr=   m.x200 - m.x201 <= 2.0601)

m.c250 = Constraint(expr=   m.x201 - m.x202 <= 2.0601)

m.c251 = Constraint(expr=   m.x202 - m.x203 <= 2.0601)

m.c252 = Constraint(expr=   m.x203 - m.x204 <= 2.0601)

m.c253 = Constraint(expr=   m.x204 - m.x205 <= 2.0601)

m.c254 = Constraint(expr=   m.x205 - m.x206 <= 2.0601)

m.c255 = Constraint(expr=   m.x206 - m.x207 <= 2.0601)

m.c256 = Constraint(expr=   m.x207 - m.x208 <= 2.0601)

m.c257 = Constraint(expr=   m.x208 - m.x209 <= 2.0601)

m.c258 = Constraint(expr=   m.x209 - m.x210 <= 2.0601)

m.c259 = Constraint(expr=   m.x210 - m.x211 <= 2.0601)

m.c260 = Constraint(expr=   m.x211 - m.x212 <= 2.0601)

m.c261 = Constraint(expr=   m.x212 - m.x213 <= 2.0601)

m.c262 = Constraint(expr=   m.x213 - m.x214 <= 2.0601)

m.c263 = Constraint(expr=   m.x214 - m.x215 <= 2.0601)

m.c264 = Constraint(expr=   m.x215 - m.x216 <= 2.0601)

m.c265 = Constraint(expr=   m.x217 - m.x218 <= 1.944)

m.c266 = Constraint(expr=   m.x218 - m.x219 <= 1.944)

m.c267 = Constraint(expr=   m.x219 - m.x220 <= 1.944)

m.c268 = Constraint(expr=   m.x220 - m.x221 <= 1.944)

m.c269 = Constraint(expr=   m.x221 - m.x222 <= 1.944)

m.c270 = Constraint(expr=   m.x222 - m.x223 <= 1.944)

m.c271 = Constraint(expr=   m.x223 - m.x224 <= 1.944)

m.c272 = Constraint(expr=   m.x224 - m.x225 <= 1.944)

m.c273 = Constraint(expr=   m.x225 - m.x226 <= 1.944)

m.c274 = Constraint(expr=   m.x226 - m.x227 <= 1.944)

m.c275 = Constraint(expr=   m.x227 - m.x228 <= 1.944)

m.c276 = Constraint(expr=   m.x228 - m.x229 <= 1.944)

m.c277 = Constraint(expr=   m.x229 - m.x230 <= 1.944)

m.c278 = Constraint(expr=   m.x230 - m.x231 <= 1.944)

m.c279 = Constraint(expr=   m.x231 - m.x232 <= 1.944)

m.c280 = Constraint(expr=   m.x232 - m.x233 <= 1.944)

m.c281 = Constraint(expr=   m.x233 - m.x234 <= 1.944)

m.c282 = Constraint(expr=   m.x234 - m.x235 <= 1.944)

m.c283 = Constraint(expr=   m.x235 - m.x236 <= 1.944)

m.c284 = Constraint(expr=   m.x236 - m.x237 <= 1.944)

m.c285 = Constraint(expr=   m.x237 - m.x238 <= 1.944)

m.c286 = Constraint(expr=   m.x238 - m.x239 <= 1.944)

m.c287 = Constraint(expr=   m.x239 - m.x240 <= 1.944)

m.c288 = Constraint(expr= - m.x193 + m.x194 <= 2.0601)

m.c289 = Constraint(expr= - m.x194 + m.x195 <= 2.0601)

m.c290 = Constraint(expr= - m.x195 + m.x196 <= 2.0601)

m.c291 = Constraint(expr= - m.x196 + m.x197 <= 2.0601)

m.c292 = Constraint(expr= - m.x197 + m.x198 <= 2.0601)

m.c293 = Constraint(expr= - m.x198 + m.x199 <= 2.0601)

m.c294 = Constraint(expr= - m.x199 + m.x200 <= 2.0601)

m.c295 = Constraint(expr= - m.x200 + m.x201 <= 2.0601)

m.c296 = Constraint(expr= - m.x201 + m.x202 <= 2.0601)

m.c297 = Constraint(expr= - m.x202 + m.x203 <= 2.0601)

m.c298 = Constraint(expr= - m.x203 + m.x204 <= 2.0601)

m.c299 = Constraint(expr= - m.x204 + m.x205 <= 2.0601)

m.c300 = Constraint(expr= - m.x205 + m.x206 <= 2.0601)

m.c301 = Constraint(expr= - m.x206 + m.x207 <= 2.0601)

m.c302 = Constraint(expr= - m.x207 + m.x208 <= 2.0601)

m.c303 = Constraint(expr= - m.x208 + m.x209 <= 2.0601)

m.c304 = Constraint(expr= - m.x209 + m.x210 <= 2.0601)

m.c305 = Constraint(expr= - m.x210 + m.x211 <= 2.0601)

m.c306 = Constraint(expr= - m.x211 + m.x212 <= 2.0601)

m.c307 = Constraint(expr= - m.x212 + m.x213 <= 2.0601)

m.c308 = Constraint(expr= - m.x213 + m.x214 <= 2.0601)

m.c309 = Constraint(expr= - m.x214 + m.x215 <= 2.0601)

m.c310 = Constraint(expr= - m.x215 + m.x216 <= 2.0601)

m.c311 = Constraint(expr= - m.x217 + m.x218 <= 1.944)

m.c312 = Constraint(expr= - m.x218 + m.x219 <= 1.944)

m.c313 = Constraint(expr= - m.x219 + m.x220 <= 1.944)

m.c314 = Constraint(expr= - m.x220 + m.x221 <= 1.944)

m.c315 = Constraint(expr= - m.x221 + m.x222 <= 1.944)

m.c316 = Constraint(expr= - m.x222 + m.x223 <= 1.944)

m.c317 = Constraint(expr= - m.x223 + m.x224 <= 1.944)

m.c318 = Constraint(expr= - m.x224 + m.x225 <= 1.944)

m.c319 = Constraint(expr= - m.x225 + m.x226 <= 1.944)

m.c320 = Constraint(expr= - m.x226 + m.x227 <= 1.944)

m.c321 = Constraint(expr= - m.x227 + m.x228 <= 1.944)

m.c322 = Constraint(expr= - m.x228 + m.x229 <= 1.944)

m.c323 = Constraint(expr= - m.x229 + m.x230 <= 1.944)

m.c324 = Constraint(expr= - m.x230 + m.x231 <= 1.944)

m.c325 = Constraint(expr= - m.x231 + m.x232 <= 1.944)

m.c326 = Constraint(expr= - m.x232 + m.x233 <= 1.944)

m.c327 = Constraint(expr= - m.x233 + m.x234 <= 1.944)

m.c328 = Constraint(expr= - m.x234 + m.x235 <= 1.944)

m.c329 = Constraint(expr= - m.x235 + m.x236 <= 1.944)

m.c330 = Constraint(expr= - m.x236 + m.x237 <= 1.944)

m.c331 = Constraint(expr= - m.x237 + m.x238 <= 1.944)

m.c332 = Constraint(expr= - m.x238 + m.x239 <= 1.944)

m.c333 = Constraint(expr= - m.x239 + m.x240 <= 1.944)

m.c334 = Constraint(expr= - m.b1 + m.b49 >= 0)

m.c335 = Constraint(expr=   m.b1 - m.b2 + m.b50 >= 0)

m.c336 = Constraint(expr=   m.b2 - m.b3 + m.b51 >= 0)

m.c337 = Constraint(expr=   m.b3 - m.b4 + m.b52 >= 0)

m.c338 = Constraint(expr=   m.b4 - m.b5 + m.b53 >= 0)

m.c339 = Constraint(expr=   m.b5 - m.b6 + m.b54 >= 0)

m.c340 = Constraint(expr=   m.b6 - m.b7 + m.b55 >= 0)

m.c341 = Constraint(expr=   m.b7 - m.b8 + m.b56 >= 0)

m.c342 = Constraint(expr=   m.b8 - m.b9 + m.b57 >= 0)

m.c343 = Constraint(expr=   m.b9 - m.b10 + m.b58 >= 0)

m.c344 = Constraint(expr=   m.b10 - m.b11 + m.b59 >= 0)

m.c345 = Constraint(expr=   m.b11 - m.b12 + m.b60 >= 0)

m.c346 = Constraint(expr=   m.b12 - m.b13 + m.b61 >= 0)

m.c347 = Constraint(expr=   m.b13 - m.b14 + m.b62 >= 0)

m.c348 = Constraint(expr=   m.b14 - m.b15 + m.b63 >= 0)

m.c349 = Constraint(expr=   m.b15 - m.b16 + m.b64 >= 0)

m.c350 = Constraint(expr=   m.b16 - m.b17 + m.b65 >= 0)

m.c351 = Constraint(expr=   m.b17 - m.b18 + m.b66 >= 0)

m.c352 = Constraint(expr=   m.b18 - m.b19 + m.b67 >= 0)

m.c353 = Constraint(expr=   m.b19 - m.b20 + m.b68 >= 0)

m.c354 = Constraint(expr=   m.b20 - m.b21 + m.b69 >= 0)

m.c355 = Constraint(expr=   m.b21 - m.b22 + m.b70 >= 0)

m.c356 = Constraint(expr=   m.b22 - m.b23 + m.b71 >= 0)

m.c357 = Constraint(expr=   m.b23 - m.b24 + m.b72 >= 0)

m.c358 = Constraint(expr= - m.b25 + m.b73 >= 0)

m.c359 = Constraint(expr=   m.b25 - m.b26 + m.b74 >= 0)

m.c360 = Constraint(expr=   m.b26 - m.b27 + m.b75 >= 0)

m.c361 = Constraint(expr=   m.b27 - m.b28 + m.b76 >= 0)

m.c362 = Constraint(expr=   m.b28 - m.b29 + m.b77 >= 0)

m.c363 = Constraint(expr=   m.b29 - m.b30 + m.b78 >= 0)

m.c364 = Constraint(expr=   m.b30 - m.b31 + m.b79 >= 0)

m.c365 = Constraint(expr=   m.b31 - m.b32 + m.b80 >= 0)

m.c366 = Constraint(expr=   m.b32 - m.b33 + m.b81 >= 0)

m.c367 = Constraint(expr=   m.b33 - m.b34 + m.b82 >= 0)

m.c368 = Constraint(expr=   m.b34 - m.b35 + m.b83 >= 0)

m.c369 = Constraint(expr=   m.b35 - m.b36 + m.b84 >= 0)

m.c370 = Constraint(expr=   m.b36 - m.b37 + m.b85 >= 0)

m.c371 = Constraint(expr=   m.b37 - m.b38 + m.b86 >= 0)

m.c372 = Constraint(expr=   m.b38 - m.b39 + m.b87 >= 0)

m.c373 = Constraint(expr=   m.b39 - m.b40 + m.b88 >= 0)

m.c374 = Constraint(expr=   m.b40 - m.b41 + m.b89 >= 0)

m.c375 = Constraint(expr=   m.b41 - m.b42 + m.b90 >= 0)

m.c376 = Constraint(expr=   m.b42 - m.b43 + m.b91 >= 0)

m.c377 = Constraint(expr=   m.b43 - m.b44 + m.b92 >= 0)

m.c378 = Constraint(expr=   m.b44 - m.b45 + m.b93 >= 0)

m.c379 = Constraint(expr=   m.b45 - m.b46 + m.b94 >= 0)

m.c380 = Constraint(expr=   m.b46 - m.b47 + m.b95 >= 0)

m.c381 = Constraint(expr=   m.b47 - m.b48 + m.b96 >= 0)

m.c382 = Constraint(expr=-(0.5061084326298*m.x193*m.x241 + 50.09702*m.x193 - 0.5580651303227*m.x265*m.x193) + m.x97
                          == 0)

m.c383 = Constraint(expr=-(0.5061084326298*m.x194*m.x242 + 50.09702*m.x194 - 0.5580651303227*m.x266*m.x194) + m.x98
                          == 0)

m.c384 = Constraint(expr=-(0.5061084326298*m.x195*m.x243 + 50.09702*m.x195 - 0.5580651303227*m.x267*m.x195) + m.x99
                          == 0)

m.c385 = Constraint(expr=-(0.5061084326298*m.x196*m.x244 + 50.09702*m.x196 - 0.5580651303227*m.x268*m.x196) + m.x100
                          == 0)

m.c386 = Constraint(expr=-(0.5061084326298*m.x197*m.x245 + 50.09702*m.x197 - 0.5580651303227*m.x269*m.x197) + m.x101
                          == 0)

m.c387 = Constraint(expr=-(0.5061084326298*m.x198*m.x246 + 50.09702*m.x198 - 0.5580651303227*m.x270*m.x198) + m.x102
                          == 0)

m.c388 = Constraint(expr=-(0.5061084326298*m.x199*m.x247 + 50.09702*m.x199 - 0.5580651303227*m.x271*m.x199) + m.x103
                          == 0)

m.c389 = Constraint(expr=-(0.5061084326298*m.x200*m.x248 + 50.09702*m.x200 - 0.5580651303227*m.x272*m.x200) + m.x104
                          == 0)

m.c390 = Constraint(expr=-(0.5061084326298*m.x201*m.x249 + 50.09702*m.x201 - 0.5580651303227*m.x273*m.x201) + m.x105
                          == 0)

m.c391 = Constraint(expr=-(0.5061084326298*m.x202*m.x250 + 50.09702*m.x202 - 0.5580651303227*m.x274*m.x202) + m.x106
                          == 0)

m.c392 = Constraint(expr=-(0.5061084326298*m.x203*m.x251 + 50.09702*m.x203 - 0.5580651303227*m.x275*m.x203) + m.x107
                          == 0)

m.c393 = Constraint(expr=-(0.5061084326298*m.x204*m.x252 + 50.09702*m.x204 - 0.5580651303227*m.x276*m.x204) + m.x108
                          == 0)

m.c394 = Constraint(expr=-(0.5061084326298*m.x205*m.x253 + 50.09702*m.x205 - 0.5580651303227*m.x277*m.x205) + m.x109
                          == 0)

m.c395 = Constraint(expr=-(0.5061084326298*m.x206*m.x254 + 50.09702*m.x206 - 0.5580651303227*m.x278*m.x206) + m.x110
                          == 0)

m.c396 = Constraint(expr=-(0.5061084326298*m.x207*m.x255 + 50.09702*m.x207 - 0.5580651303227*m.x279*m.x207) + m.x111
                          == 0)

m.c397 = Constraint(expr=-(0.5061084326298*m.x208*m.x256 + 50.09702*m.x208 - 0.5580651303227*m.x280*m.x208) + m.x112
                          == 0)

m.c398 = Constraint(expr=-(0.5061084326298*m.x209*m.x257 + 50.09702*m.x209 - 0.5580651303227*m.x281*m.x209) + m.x113
                          == 0)

m.c399 = Constraint(expr=-(0.5061084326298*m.x210*m.x258 + 50.09702*m.x210 - 0.5580651303227*m.x282*m.x210) + m.x114
                          == 0)

m.c400 = Constraint(expr=-(0.5061084326298*m.x211*m.x259 + 50.09702*m.x211 - 0.5580651303227*m.x283*m.x211) + m.x115
                          == 0)

m.c401 = Constraint(expr=-(0.5061084326298*m.x212*m.x260 + 50.09702*m.x212 - 0.5580651303227*m.x284*m.x212) + m.x116
                          == 0)

m.c402 = Constraint(expr=-(0.5061084326298*m.x213*m.x261 + 50.09702*m.x213 - 0.5580651303227*m.x285*m.x213) + m.x117
                          == 0)

m.c403 = Constraint(expr=-(0.5061084326298*m.x214*m.x262 + 50.09702*m.x214 - 0.5580651303227*m.x286*m.x214) + m.x118
                          == 0)

m.c404 = Constraint(expr=-(0.5061084326298*m.x215*m.x263 + 50.09702*m.x215 - 0.5580651303227*m.x287*m.x215) + m.x119
                          == 0)

m.c405 = Constraint(expr=-(0.5061084326298*m.x216*m.x264 + 50.09702*m.x216 - 0.5580651303227*m.x288*m.x216) + m.x120
                          == 0)

m.c406 = Constraint(expr=-(0.5623466695665*m.x217*m.x265 + 78.54163*m.x217) + m.x121 == 0)

m.c407 = Constraint(expr=-(0.5623466695665*m.x218*m.x266 + 78.54163*m.x218) + m.x122 == 0)

m.c408 = Constraint(expr=-(0.5623466695665*m.x219*m.x267 + 78.54163*m.x219) + m.x123 == 0)

m.c409 = Constraint(expr=-(0.5623466695665*m.x220*m.x268 + 78.54163*m.x220) + m.x124 == 0)

m.c410 = Constraint(expr=-(0.5623466695665*m.x221*m.x269 + 78.54163*m.x221) + m.x125 == 0)

m.c411 = Constraint(expr=-(0.5623466695665*m.x222*m.x270 + 78.54163*m.x222) + m.x126 == 0)

m.c412 = Constraint(expr=-(0.5623466695665*m.x223*m.x271 + 78.54163*m.x223) + m.x127 == 0)

m.c413 = Constraint(expr=-(0.5623466695665*m.x224*m.x272 + 78.54163*m.x224) + m.x128 == 0)

m.c414 = Constraint(expr=-(0.5623466695665*m.x225*m.x273 + 78.54163*m.x225) + m.x129 == 0)

m.c415 = Constraint(expr=-(0.5623466695665*m.x226*m.x274 + 78.54163*m.x226) + m.x130 == 0)

m.c416 = Constraint(expr=-(0.5623466695665*m.x227*m.x275 + 78.54163*m.x227) + m.x131 == 0)

m.c417 = Constraint(expr=-(0.5623466695665*m.x228*m.x276 + 78.54163*m.x228) + m.x132 == 0)

m.c418 = Constraint(expr=-(0.5623466695665*m.x229*m.x277 + 78.54163*m.x229) + m.x133 == 0)

m.c419 = Constraint(expr=-(0.5623466695665*m.x230*m.x278 + 78.54163*m.x230) + m.x134 == 0)

m.c420 = Constraint(expr=-(0.5623466695665*m.x231*m.x279 + 78.54163*m.x231) + m.x135 == 0)

m.c421 = Constraint(expr=-(0.5623466695665*m.x232*m.x280 + 78.54163*m.x232) + m.x136 == 0)

m.c422 = Constraint(expr=-(0.5623466695665*m.x233*m.x281 + 78.54163*m.x233) + m.x137 == 0)

m.c423 = Constraint(expr=-(0.5623466695665*m.x234*m.x282 + 78.54163*m.x234) + m.x138 == 0)

m.c424 = Constraint(expr=-(0.5623466695665*m.x235*m.x283 + 78.54163*m.x235) + m.x139 == 0)

m.c425 = Constraint(expr=-(0.5623466695665*m.x236*m.x284 + 78.54163*m.x236) + m.x140 == 0)

m.c426 = Constraint(expr=-(0.5623466695665*m.x237*m.x285 + 78.54163*m.x237) + m.x141 == 0)

m.c427 = Constraint(expr=-(0.5623466695665*m.x238*m.x286 + 78.54163*m.x238) + m.x142 == 0)

m.c428 = Constraint(expr=-(0.5623466695665*m.x239*m.x287 + 78.54163*m.x239) + m.x143 == 0)

m.c429 = Constraint(expr=-(0.5623466695665*m.x240*m.x288 + 78.54163*m.x240) + m.x144 == 0)
