#  MINLP written by GAMS Convert at 04/21/18 13:51:13
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        360      200      132       28        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        332      266       66        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1454     1014      440        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x2 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x3 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x4 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x5 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x6 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x7 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x8 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x9 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x10 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x11 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x12 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x13 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x14 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x15 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x16 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x17 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x18 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x19 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x20 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x21 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x22 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x23 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x24 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x25 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x26 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x27 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x28 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x29 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x30 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x31 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x32 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x33 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x34 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x35 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x36 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x37 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x38 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x39 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x40 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x41 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x42 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x43 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x44 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x45 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x46 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x47 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x48 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x49 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x50 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x51 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x52 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x53 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x54 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x55 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x56 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x57 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x58 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x59 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x60 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x61 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x62 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x63 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x64 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x65 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x66 = Var(within=Reals,bounds=(0,None),initialize=10)
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
m.b97 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b98 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b99 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b100 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b101 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b102 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b103 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b104 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b105 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b106 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b107 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b108 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b109 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b110 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b111 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b112 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b113 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b114 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b115 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b116 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b117 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b118 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b119 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b120 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b121 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b122 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b123 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b124 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b125 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b126 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b127 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b128 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b129 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b130 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b131 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b132 = Var(within=Binary,bounds=(0,1),initialize=0)
m.x133 = Var(within=Reals,bounds=(0,None),initialize=100)
m.x134 = Var(within=Reals,bounds=(0,None),initialize=100)
m.x135 = Var(within=Reals,bounds=(0,None),initialize=100)
m.x136 = Var(within=Reals,bounds=(0,None),initialize=100)
m.x137 = Var(within=Reals,bounds=(0,None),initialize=100)
m.x138 = Var(within=Reals,bounds=(0,None),initialize=100)
m.x139 = Var(within=Reals,bounds=(0,None),initialize=100)
m.x140 = Var(within=Reals,bounds=(0,None),initialize=100)
m.x141 = Var(within=Reals,bounds=(0,None),initialize=100)
m.x142 = Var(within=Reals,bounds=(0,None),initialize=100)
m.x143 = Var(within=Reals,bounds=(0,None),initialize=100)
m.x144 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x145 = Var(within=Reals,bounds=(0,None),initialize=14)
m.x146 = Var(within=Reals,bounds=(0,None),initialize=14)
m.x147 = Var(within=Reals,bounds=(0,None),initialize=14)
m.x148 = Var(within=Reals,bounds=(0,None),initialize=14)
m.x149 = Var(within=Reals,bounds=(0,None),initialize=14)
m.x150 = Var(within=Reals,bounds=(0,None),initialize=14)
m.x151 = Var(within=Reals,bounds=(0,None),initialize=14)
m.x152 = Var(within=Reals,bounds=(0,None),initialize=14)
m.x153 = Var(within=Reals,bounds=(0,None),initialize=14)
m.x154 = Var(within=Reals,bounds=(0,None),initialize=14)
m.x155 = Var(within=Reals,bounds=(0,None),initialize=14)
m.x156 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x157 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x158 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x159 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x160 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x161 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x162 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x163 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x164 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x165 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x166 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x167 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x168 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x169 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x170 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x171 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x172 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x173 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x174 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x175 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x176 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x177 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x178 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x179 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x180 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x181 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x182 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x183 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x184 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x185 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x186 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x187 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x188 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x189 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x190 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x191 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x192 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x193 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x194 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x195 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x196 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x197 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x198 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x199 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x200 = Var(within=Reals,bounds=(0,1),initialize=0.5)
m.x201 = Var(within=Reals,bounds=(0,1),initialize=0.5)
m.x202 = Var(within=Reals,bounds=(0,1),initialize=0.5)
m.x203 = Var(within=Reals,bounds=(0,1),initialize=0.5)
m.x204 = Var(within=Reals,bounds=(0,1),initialize=0.5)
m.x205 = Var(within=Reals,bounds=(0,1),initialize=0.5)
m.x206 = Var(within=Reals,bounds=(0,1),initialize=0.5)
m.x207 = Var(within=Reals,bounds=(0,1),initialize=0.5)
m.x208 = Var(within=Reals,bounds=(0,1),initialize=0.5)
m.x209 = Var(within=Reals,bounds=(0,1),initialize=0.5)
m.x210 = Var(within=Reals,bounds=(0,1),initialize=0.5)
m.x211 = Var(within=Reals,bounds=(0,1),initialize=0.5)
m.x212 = Var(within=Reals,bounds=(0,1),initialize=0.5)
m.x213 = Var(within=Reals,bounds=(0,1),initialize=0.5)
m.x214 = Var(within=Reals,bounds=(0,1),initialize=0.5)
m.x215 = Var(within=Reals,bounds=(0,1),initialize=0.5)
m.x216 = Var(within=Reals,bounds=(0,1),initialize=0.5)
m.x217 = Var(within=Reals,bounds=(0,1),initialize=0.5)
m.x218 = Var(within=Reals,bounds=(0,1),initialize=0.5)
m.x219 = Var(within=Reals,bounds=(0,1),initialize=0.5)
m.x220 = Var(within=Reals,bounds=(0,1),initialize=0.5)
m.x221 = Var(within=Reals,bounds=(0,1),initialize=0.5)
m.x222 = Var(within=Reals,bounds=(0,1),initialize=0.5)
m.x223 = Var(within=Reals,bounds=(0,1),initialize=0.5)
m.x224 = Var(within=Reals,bounds=(0,1),initialize=0.5)
m.x225 = Var(within=Reals,bounds=(0,1),initialize=0.5)
m.x226 = Var(within=Reals,bounds=(0,1),initialize=0.5)
m.x227 = Var(within=Reals,bounds=(0,1),initialize=0.5)
m.x228 = Var(within=Reals,bounds=(0,1),initialize=0.5)
m.x229 = Var(within=Reals,bounds=(0,1),initialize=0.5)
m.x230 = Var(within=Reals,bounds=(0,1),initialize=0.5)
m.x231 = Var(within=Reals,bounds=(0,1),initialize=0.5)
m.x232 = Var(within=Reals,bounds=(0,1),initialize=0.5)
m.x233 = Var(within=Reals,bounds=(0,1),initialize=0.5)
m.x234 = Var(within=Reals,bounds=(0,1),initialize=0.5)
m.x235 = Var(within=Reals,bounds=(0,1),initialize=0.5)
m.x236 = Var(within=Reals,bounds=(0,1),initialize=0.5)
m.x237 = Var(within=Reals,bounds=(0,1),initialize=0.5)
m.x238 = Var(within=Reals,bounds=(0,1),initialize=0.5)
m.x239 = Var(within=Reals,bounds=(0,1),initialize=0.5)
m.x240 = Var(within=Reals,bounds=(0,1),initialize=0.5)
m.x241 = Var(within=Reals,bounds=(0,1),initialize=0.5)
m.x242 = Var(within=Reals,bounds=(0,1),initialize=0.5)
m.x243 = Var(within=Reals,bounds=(0,1),initialize=0.5)
m.x244 = Var(within=Reals,bounds=(0,1),initialize=0.5)
m.x245 = Var(within=Reals,bounds=(0,1),initialize=0.5)
m.x246 = Var(within=Reals,bounds=(0,1),initialize=0.5)
m.x247 = Var(within=Reals,bounds=(0,1),initialize=0.5)
m.x248 = Var(within=Reals,bounds=(0,1),initialize=0.5)
m.x249 = Var(within=Reals,bounds=(0,1),initialize=0.5)
m.x250 = Var(within=Reals,bounds=(0,1),initialize=0.5)
m.x251 = Var(within=Reals,bounds=(0,1),initialize=0.5)
m.x252 = Var(within=Reals,bounds=(0,1),initialize=0.5)
m.x253 = Var(within=Reals,bounds=(0,1),initialize=0.5)
m.x254 = Var(within=Reals,bounds=(0,1),initialize=0.5)
m.x255 = Var(within=Reals,bounds=(0,1),initialize=0.5)
m.x256 = Var(within=Reals,bounds=(0,1),initialize=0.5)
m.x257 = Var(within=Reals,bounds=(0,1),initialize=0.5)
m.x258 = Var(within=Reals,bounds=(0,1),initialize=0.5)
m.x259 = Var(within=Reals,bounds=(0,1),initialize=0.5)
m.x260 = Var(within=Reals,bounds=(0,1),initialize=0.5)
m.x261 = Var(within=Reals,bounds=(0,1),initialize=0.5)
m.x262 = Var(within=Reals,bounds=(0,1),initialize=0.5)
m.x263 = Var(within=Reals,bounds=(0,1),initialize=0.5)
m.x264 = Var(within=Reals,bounds=(0,1),initialize=0.5)
m.x265 = Var(within=Reals,bounds=(0,1),initialize=0.5)
m.x266 = Var(within=Reals,bounds=(None,None),initialize=-1.5)
m.x267 = Var(within=Reals,bounds=(None,None),initialize=-1.5)
m.x268 = Var(within=Reals,bounds=(None,None),initialize=-1.5)
m.x269 = Var(within=Reals,bounds=(None,None),initialize=-1.5)
m.x270 = Var(within=Reals,bounds=(None,None),initialize=-1.5)
m.x271 = Var(within=Reals,bounds=(None,None),initialize=-1.5)
m.x272 = Var(within=Reals,bounds=(None,None),initialize=-1.5)
m.x273 = Var(within=Reals,bounds=(None,None),initialize=-1.5)
m.x274 = Var(within=Reals,bounds=(None,None),initialize=-1.5)
m.x275 = Var(within=Reals,bounds=(None,None),initialize=-1.5)
m.x276 = Var(within=Reals,bounds=(None,None),initialize=-1.5)
m.x277 = Var(within=Reals,bounds=(None,None),initialize=-1.5)
m.x278 = Var(within=Reals,bounds=(None,None),initialize=-1.5)
m.x279 = Var(within=Reals,bounds=(None,None),initialize=-1.5)
m.x280 = Var(within=Reals,bounds=(None,None),initialize=-1.5)
m.x281 = Var(within=Reals,bounds=(None,None),initialize=-1.5)
m.x282 = Var(within=Reals,bounds=(None,None),initialize=-1.5)
m.x283 = Var(within=Reals,bounds=(None,None),initialize=-1.5)
m.x284 = Var(within=Reals,bounds=(None,None),initialize=-1.5)
m.x285 = Var(within=Reals,bounds=(None,None),initialize=-1.5)
m.x286 = Var(within=Reals,bounds=(None,None),initialize=-1.5)
m.x287 = Var(within=Reals,bounds=(None,None),initialize=-1.5)
m.x288 = Var(within=Reals,bounds=(None,None),initialize=-1.5)
m.x289 = Var(within=Reals,bounds=(None,None),initialize=-1.5)
m.x290 = Var(within=Reals,bounds=(None,None),initialize=-1.5)
m.x291 = Var(within=Reals,bounds=(None,None),initialize=-1.5)
m.x292 = Var(within=Reals,bounds=(None,None),initialize=-1.5)
m.x293 = Var(within=Reals,bounds=(None,None),initialize=-1.5)
m.x294 = Var(within=Reals,bounds=(None,None),initialize=-1.5)
m.x295 = Var(within=Reals,bounds=(None,None),initialize=-1.5)
m.x296 = Var(within=Reals,bounds=(None,None),initialize=-1.5)
m.x297 = Var(within=Reals,bounds=(None,None),initialize=-1.5)
m.x298 = Var(within=Reals,bounds=(None,None),initialize=-1.5)
m.x299 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x300 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x301 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x302 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x303 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x304 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x305 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x306 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x307 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x308 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x309 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x310 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x311 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x312 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x313 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x314 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x315 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x316 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x317 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x318 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x319 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x320 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x321 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x322 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x323 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x324 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x325 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x326 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x327 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x328 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x329 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x330 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x331 = Var(within=Reals,bounds=(None,None),initialize=1.5)

m.obj = Objective(expr=-((4 - 0.2*m.x201 + 0.3*m.x235)*m.x133 + (4 - 0.2*m.x204 + 0.3*m.x238)*m.x134 + (4 - 0.2*m.x207
                        + 0.3*m.x241)*m.x135 + (4 - 0.2*m.x210 + 0.3*m.x244)*m.x136 + (4 - 0.2*m.x213 + 0.3*m.x247)*
                       m.x137 + (4 - 0.2*m.x216 + 0.3*m.x250)*m.x138 + (4 - 0.2*m.x219 + 0.3*m.x253)*m.x139 + (4 - 0.2*
                       m.x222 + 0.3*m.x256)*m.x140 + (4 - 0.2*m.x225 + 0.3*m.x259)*m.x141 + (4 - 0.2*m.x228 + 0.3*m.x262
                       )*m.x142 + (4 - 0.2*m.x231 + 0.3*m.x265)*m.x143) + 0.01*m.b67 + 0.01*m.b68 + 0.01*m.b69
                        + 0.01*m.b70 + 0.01*m.b71 + 0.01*m.b72 + 0.01*m.b73 + 0.01*m.b74 + 0.01*m.b75 + 0.01*m.b76
                        + 0.01*m.b77 + 0.01*m.b78 + 0.01*m.b79 + 0.01*m.b80 + 0.01*m.b81 + 0.01*m.b82 + 0.01*m.b83
                        + 0.01*m.b84 + 0.01*m.b85 + 0.01*m.b86 + 0.01*m.b87 + 0.01*m.b88 + 0.01*m.b89 + 0.01*m.b90
                        + 0.01*m.b91 + 0.01*m.b92 + 0.01*m.b93 + 0.01*m.b94 + 0.01*m.b95 + 0.01*m.b96 + 0.01*m.b97
                        + 0.01*m.b98 + 0.01*m.b99 + 0.01*m.b100 + 0.01*m.b101 + 0.01*m.b102 + 0.01*m.b103 + 0.01*m.b104
                        + 0.01*m.b105 + 0.01*m.b106 + 0.01*m.b107 + 0.01*m.b108 + 0.01*m.b109 + 0.01*m.b110
                        + 0.01*m.b111 + 0.01*m.b112 + 0.01*m.b113 + 0.01*m.b114 + 0.01*m.b115 + 0.01*m.b116
                        + 0.01*m.b117 + 0.01*m.b118 + 0.01*m.b119 + 0.01*m.b120 + 0.01*m.b121 + 0.01*m.b122
                        + 0.01*m.b123 + 0.01*m.b124 + 0.01*m.b125 + 0.01*m.b126 + 0.01*m.b127 + 0.01*m.b128
                        + 0.01*m.b129 + 0.01*m.b130 + 0.01*m.b131 + 0.01*m.b132, sense=minimize)

m.c1 = Constraint(expr=   m.x1 + m.x2 + m.x3 + m.x4 + m.x5 + m.x6 + m.x7 + m.x8 + m.x9 + m.x10 + m.x11 <= 800)

m.c2 = Constraint(expr=   m.x12 + m.x13 + m.x14 + m.x15 + m.x16 + m.x17 + m.x18 + m.x19 + m.x20 + m.x21 + m.x22 <= 800)

m.c3 = Constraint(expr=   m.x23 + m.x24 + m.x25 + m.x26 + m.x27 + m.x28 + m.x29 + m.x30 + m.x31 + m.x32 + m.x33 <= 800)

m.c4 = Constraint(expr=   m.x34 + m.x35 + m.x36 + m.x37 + m.x38 + m.x39 + m.x40 + m.x41 + m.x42 + m.x43 + m.x44 <= 800)

m.c5 = Constraint(expr=   m.x45 + m.x46 + m.x47 + m.x48 + m.x49 + m.x50 + m.x51 + m.x52 + m.x53 + m.x54 + m.x55 <= 800)

m.c6 = Constraint(expr=   m.x56 + m.x57 + m.x58 + m.x59 + m.x60 + m.x61 + m.x62 + m.x63 + m.x64 + m.x65 + m.x66 <= 800)

m.c7 = Constraint(expr= - m.x1 - m.x12 - m.x23 - m.x34 - m.x45 - m.x56 + m.x133 == 0)

m.c8 = Constraint(expr= - m.x2 - m.x13 - m.x24 - m.x35 - m.x46 - m.x57 + m.x134 == 0)

m.c9 = Constraint(expr= - m.x3 - m.x14 - m.x25 - m.x36 - m.x47 - m.x58 + m.x135 == 0)

m.c10 = Constraint(expr= - m.x4 - m.x15 - m.x26 - m.x37 - m.x48 - m.x59 + m.x136 == 0)

m.c11 = Constraint(expr= - m.x5 - m.x16 - m.x27 - m.x38 - m.x49 - m.x60 + m.x137 == 0)

m.c12 = Constraint(expr= - m.x6 - m.x17 - m.x28 - m.x39 - m.x50 - m.x61 + m.x138 == 0)

m.c13 = Constraint(expr= - m.x7 - m.x18 - m.x29 - m.x40 - m.x51 - m.x62 + m.x139 == 0)

m.c14 = Constraint(expr= - m.x8 - m.x19 - m.x30 - m.x41 - m.x52 - m.x63 + m.x140 == 0)

m.c15 = Constraint(expr= - m.x9 - m.x20 - m.x31 - m.x42 - m.x53 - m.x64 + m.x141 == 0)

m.c16 = Constraint(expr= - m.x10 - m.x21 - m.x32 - m.x43 - m.x54 - m.x65 + m.x142 == 0)

m.c17 = Constraint(expr= - m.x11 - m.x22 - m.x33 - m.x44 - m.x55 - m.x66 + m.x143 == 0)

m.c18 = Constraint(expr= - m.x133 - m.x134 - m.x135 - m.x136 - m.x137 - m.x138 - m.x139 - m.x140 - m.x141 - m.x142
                         - m.x143 + m.x144 == 0)

m.c19 = Constraint(expr=m.x145*m.x133 - 13.1*m.x1 - 13.9*m.x12 - 12.8*m.x23 - 14.6*m.x34 - 15.9*m.x45 - 14.1*m.x56 == 0)

m.c20 = Constraint(expr=m.x146*m.x134 - 13.1*m.x2 - 13.9*m.x13 - 12.8*m.x24 - 14.6*m.x35 - 15.9*m.x46 - 14.1*m.x57 == 0)

m.c21 = Constraint(expr=m.x147*m.x135 - 13.1*m.x3 - 13.9*m.x14 - 12.8*m.x25 - 14.6*m.x36 - 15.9*m.x47 - 14.1*m.x58 == 0)

m.c22 = Constraint(expr=m.x148*m.x136 - 13.1*m.x4 - 13.9*m.x15 - 12.8*m.x26 - 14.6*m.x37 - 15.9*m.x48 - 14.1*m.x59 == 0)

m.c23 = Constraint(expr=m.x149*m.x137 - 13.1*m.x5 - 13.9*m.x16 - 12.8*m.x27 - 14.6*m.x38 - 15.9*m.x49 - 14.1*m.x60 == 0)

m.c24 = Constraint(expr=m.x150*m.x138 - 13.1*m.x6 - 13.9*m.x17 - 12.8*m.x28 - 14.6*m.x39 - 15.9*m.x50 - 14.1*m.x61 == 0)

m.c25 = Constraint(expr=m.x151*m.x139 - 13.1*m.x7 - 13.9*m.x18 - 12.8*m.x29 - 14.6*m.x40 - 15.9*m.x51 - 14.1*m.x62 == 0)

m.c26 = Constraint(expr=m.x152*m.x140 - 13.1*m.x8 - 13.9*m.x19 - 12.8*m.x30 - 14.6*m.x41 - 15.9*m.x52 - 14.1*m.x63 == 0)

m.c27 = Constraint(expr=m.x153*m.x141 - 13.1*m.x9 - 13.9*m.x20 - 12.8*m.x31 - 14.6*m.x42 - 15.9*m.x53 - 14.1*m.x64 == 0)

m.c28 = Constraint(expr=m.x154*m.x142 - 13.1*m.x10 - 13.9*m.x21 - 12.8*m.x32 - 14.6*m.x43 - 15.9*m.x54 - 14.1*m.x65
                         == 0)

m.c29 = Constraint(expr=m.x155*m.x143 - 13.1*m.x11 - 13.9*m.x22 - 12.8*m.x33 - 14.6*m.x44 - 15.9*m.x55 - 14.1*m.x66
                         == 0)

m.c30 = Constraint(expr=m.x156**2*m.x133**2 - (m.x1**2 + m.x12**2 + m.x23**2 + m.x34**2 + m.x45**2 + m.x56**2) == 0)

m.c31 = Constraint(expr=m.x157**2*m.x134**2 - (m.x2**2 + m.x13**2 + m.x24**2 + m.x35**2 + m.x46**2 + m.x57**2) == 0)

m.c32 = Constraint(expr=m.x158**2*m.x135**2 - (m.x3**2 + m.x14**2 + m.x25**2 + m.x36**2 + m.x47**2 + m.x58**2) == 0)

m.c33 = Constraint(expr=m.x159**2*m.x136**2 - (m.x4**2 + m.x15**2 + m.x26**2 + m.x37**2 + m.x48**2 + m.x59**2) == 0)

m.c34 = Constraint(expr=m.x160**2*m.x137**2 - (m.x5**2 + m.x16**2 + m.x27**2 + m.x38**2 + m.x49**2 + m.x60**2) == 0)

m.c35 = Constraint(expr=m.x161**2*m.x138**2 - (m.x6**2 + m.x17**2 + m.x28**2 + m.x39**2 + m.x50**2 + m.x61**2) == 0)

m.c36 = Constraint(expr=m.x162**2*m.x139**2 - (m.x7**2 + m.x18**2 + m.x29**2 + m.x40**2 + m.x51**2 + m.x62**2) == 0)

m.c37 = Constraint(expr=m.x163**2*m.x140**2 - (m.x8**2 + m.x19**2 + m.x30**2 + m.x41**2 + m.x52**2 + m.x63**2) == 0)

m.c38 = Constraint(expr=m.x164**2*m.x141**2 - (m.x9**2 + m.x20**2 + m.x31**2 + m.x42**2 + m.x53**2 + m.x64**2) == 0)

m.c39 = Constraint(expr=m.x165**2*m.x142**2 - (m.x10**2 + m.x21**2 + m.x32**2 + m.x43**2 + m.x54**2 + m.x65**2) == 0)

m.c40 = Constraint(expr=m.x166**2*m.x143**2 - (m.x11**2 + m.x22**2 + m.x33**2 + m.x44**2 + m.x55**2 + m.x66**2) == 0)

m.c41 = Constraint(expr=   m.b67 + m.b78 + m.b89 <= 1)

m.c42 = Constraint(expr=   m.b68 + m.b79 + m.b90 <= 1)

m.c43 = Constraint(expr=   m.b69 + m.b80 + m.b91 <= 1)

m.c44 = Constraint(expr=   m.b70 + m.b81 + m.b92 <= 1)

m.c45 = Constraint(expr=   m.b71 + m.b82 + m.b93 <= 1)

m.c46 = Constraint(expr=   m.b72 + m.b83 + m.b94 <= 1)

m.c47 = Constraint(expr=   m.b73 + m.b84 + m.b95 <= 1)

m.c48 = Constraint(expr=   m.b74 + m.b85 + m.b96 <= 1)

m.c49 = Constraint(expr=   m.b75 + m.b86 + m.b97 <= 1)

m.c50 = Constraint(expr=   m.b76 + m.b87 + m.b98 <= 1)

m.c51 = Constraint(expr=   m.b77 + m.b88 + m.b99 <= 1)

m.c52 = Constraint(expr=   m.b100 + m.b111 + m.b122 <= 1)

m.c53 = Constraint(expr=   m.b101 + m.b112 + m.b123 <= 1)

m.c54 = Constraint(expr=   m.b102 + m.b113 + m.b124 <= 1)

m.c55 = Constraint(expr=   m.b103 + m.b114 + m.b125 <= 1)

m.c56 = Constraint(expr=   m.b104 + m.b115 + m.b126 <= 1)

m.c57 = Constraint(expr=   m.b105 + m.b116 + m.b127 <= 1)

m.c58 = Constraint(expr=   m.b106 + m.b117 + m.b128 <= 1)

m.c59 = Constraint(expr=   m.b107 + m.b118 + m.b129 <= 1)

m.c60 = Constraint(expr=   m.b108 + m.b119 + m.b130 <= 1)

m.c61 = Constraint(expr=   m.b109 + m.b120 + m.b131 <= 1)

m.c62 = Constraint(expr=   m.b110 + m.b121 + m.b132 <= 1)

m.c63 = Constraint(expr= - m.x1 + 1000*m.b67 >= 0)

m.c64 = Constraint(expr= - m.x2 + 1000*m.b68 >= 0)

m.c65 = Constraint(expr= - m.x3 + 1000*m.b69 >= 0)

m.c66 = Constraint(expr= - m.x4 + 1000*m.b70 >= 0)

m.c67 = Constraint(expr= - m.x5 + 1000*m.b71 >= 0)

m.c68 = Constraint(expr= - m.x6 + 1000*m.b72 >= 0)

m.c69 = Constraint(expr= - m.x7 + 1000*m.b73 >= 0)

m.c70 = Constraint(expr= - m.x8 + 1000*m.b74 >= 0)

m.c71 = Constraint(expr= - m.x9 + 1000*m.b75 >= 0)

m.c72 = Constraint(expr= - m.x10 + 1000*m.b76 >= 0)

m.c73 = Constraint(expr= - m.x11 + 1000*m.b77 >= 0)

m.c74 = Constraint(expr= - m.x12 + 1000*m.b78 >= 0)

m.c75 = Constraint(expr= - m.x13 + 1000*m.b79 >= 0)

m.c76 = Constraint(expr= - m.x14 + 1000*m.b80 >= 0)

m.c77 = Constraint(expr= - m.x15 + 1000*m.b81 >= 0)

m.c78 = Constraint(expr= - m.x16 + 1000*m.b82 >= 0)

m.c79 = Constraint(expr= - m.x17 + 1000*m.b83 >= 0)

m.c80 = Constraint(expr= - m.x18 + 1000*m.b84 >= 0)

m.c81 = Constraint(expr= - m.x19 + 1000*m.b85 >= 0)

m.c82 = Constraint(expr= - m.x20 + 1000*m.b86 >= 0)

m.c83 = Constraint(expr= - m.x21 + 1000*m.b87 >= 0)

m.c84 = Constraint(expr= - m.x22 + 1000*m.b88 >= 0)

m.c85 = Constraint(expr= - m.x23 + 1000*m.b89 >= 0)

m.c86 = Constraint(expr= - m.x24 + 1000*m.b90 >= 0)

m.c87 = Constraint(expr= - m.x25 + 1000*m.b91 >= 0)

m.c88 = Constraint(expr= - m.x26 + 1000*m.b92 >= 0)

m.c89 = Constraint(expr= - m.x27 + 1000*m.b93 >= 0)

m.c90 = Constraint(expr= - m.x28 + 1000*m.b94 >= 0)

m.c91 = Constraint(expr= - m.x29 + 1000*m.b95 >= 0)

m.c92 = Constraint(expr= - m.x30 + 1000*m.b96 >= 0)

m.c93 = Constraint(expr= - m.x31 + 1000*m.b97 >= 0)

m.c94 = Constraint(expr= - m.x32 + 1000*m.b98 >= 0)

m.c95 = Constraint(expr= - m.x33 + 1000*m.b99 >= 0)

m.c96 = Constraint(expr= - m.x34 + 1000*m.b100 >= 0)

m.c97 = Constraint(expr= - m.x35 + 1000*m.b101 >= 0)

m.c98 = Constraint(expr= - m.x36 + 1000*m.b102 >= 0)

m.c99 = Constraint(expr= - m.x37 + 1000*m.b103 >= 0)

m.c100 = Constraint(expr= - m.x38 + 1000*m.b104 >= 0)

m.c101 = Constraint(expr= - m.x39 + 1000*m.b105 >= 0)

m.c102 = Constraint(expr= - m.x40 + 1000*m.b106 >= 0)

m.c103 = Constraint(expr= - m.x41 + 1000*m.b107 >= 0)

m.c104 = Constraint(expr= - m.x42 + 1000*m.b108 >= 0)

m.c105 = Constraint(expr= - m.x43 + 1000*m.b109 >= 0)

m.c106 = Constraint(expr= - m.x44 + 1000*m.b110 >= 0)

m.c107 = Constraint(expr= - m.x45 + 1000*m.b111 >= 0)

m.c108 = Constraint(expr= - m.x46 + 1000*m.b112 >= 0)

m.c109 = Constraint(expr= - m.x47 + 1000*m.b113 >= 0)

m.c110 = Constraint(expr= - m.x48 + 1000*m.b114 >= 0)

m.c111 = Constraint(expr= - m.x49 + 1000*m.b115 >= 0)

m.c112 = Constraint(expr= - m.x50 + 1000*m.b116 >= 0)

m.c113 = Constraint(expr= - m.x51 + 1000*m.b117 >= 0)

m.c114 = Constraint(expr= - m.x52 + 1000*m.b118 >= 0)

m.c115 = Constraint(expr= - m.x53 + 1000*m.b119 >= 0)

m.c116 = Constraint(expr= - m.x54 + 1000*m.b120 >= 0)

m.c117 = Constraint(expr= - m.x55 + 1000*m.b121 >= 0)

m.c118 = Constraint(expr= - m.x56 + 1000*m.b122 >= 0)

m.c119 = Constraint(expr= - m.x57 + 1000*m.b123 >= 0)

m.c120 = Constraint(expr= - m.x58 + 1000*m.b124 >= 0)

m.c121 = Constraint(expr= - m.x59 + 1000*m.b125 >= 0)

m.c122 = Constraint(expr= - m.x60 + 1000*m.b126 >= 0)

m.c123 = Constraint(expr= - m.x61 + 1000*m.b127 >= 0)

m.c124 = Constraint(expr= - m.x62 + 1000*m.b128 >= 0)

m.c125 = Constraint(expr= - m.x63 + 1000*m.b129 >= 0)

m.c126 = Constraint(expr= - m.x64 + 1000*m.b130 >= 0)

m.c127 = Constraint(expr= - m.x65 + 1000*m.b131 >= 0)

m.c128 = Constraint(expr= - m.x66 + 1000*m.b132 >= 0)

m.c129 = Constraint(expr= - 800*m.b78 >= 0)

m.c130 = Constraint(expr=   m.x1 - 800*m.b79 >= 0)

m.c131 = Constraint(expr=   m.x1 + m.x2 - 800*m.b80 >= 0)

m.c132 = Constraint(expr=   m.x1 + m.x2 + m.x3 - 800*m.b81 >= 0)

m.c133 = Constraint(expr=   m.x1 + m.x2 + m.x3 + m.x4 - 800*m.b82 >= 0)

m.c134 = Constraint(expr=   m.x1 + m.x2 + m.x3 + m.x4 + m.x5 - 800*m.b83 >= 0)

m.c135 = Constraint(expr=   m.x1 + m.x2 + m.x3 + m.x4 + m.x5 + m.x6 - 800*m.b84 >= 0)

m.c136 = Constraint(expr=   m.x1 + m.x2 + m.x3 + m.x4 + m.x5 + m.x6 + m.x7 - 800*m.b85 >= 0)

m.c137 = Constraint(expr=   m.x1 + m.x2 + m.x3 + m.x4 + m.x5 + m.x6 + m.x7 + m.x8 - 800*m.b86 >= 0)

m.c138 = Constraint(expr=   m.x1 + m.x2 + m.x3 + m.x4 + m.x5 + m.x6 + m.x7 + m.x8 + m.x9 - 800*m.b87 >= 0)

m.c139 = Constraint(expr=   m.x1 + m.x2 + m.x3 + m.x4 + m.x5 + m.x6 + m.x7 + m.x8 + m.x9 + m.x10 - 800*m.b88 >= 0)

m.c140 = Constraint(expr= - 800*m.b89 >= 0)

m.c141 = Constraint(expr=   m.x1 - 800*m.b90 >= 0)

m.c142 = Constraint(expr=   m.x1 + m.x2 - 800*m.b91 >= 0)

m.c143 = Constraint(expr=   m.x1 + m.x2 + m.x3 - 800*m.b92 >= 0)

m.c144 = Constraint(expr=   m.x1 + m.x2 + m.x3 + m.x4 - 800*m.b93 >= 0)

m.c145 = Constraint(expr=   m.x1 + m.x2 + m.x3 + m.x4 + m.x5 - 800*m.b94 >= 0)

m.c146 = Constraint(expr=   m.x1 + m.x2 + m.x3 + m.x4 + m.x5 + m.x6 - 800*m.b95 >= 0)

m.c147 = Constraint(expr=   m.x1 + m.x2 + m.x3 + m.x4 + m.x5 + m.x6 + m.x7 - 800*m.b96 >= 0)

m.c148 = Constraint(expr=   m.x1 + m.x2 + m.x3 + m.x4 + m.x5 + m.x6 + m.x7 + m.x8 - 800*m.b97 >= 0)

m.c149 = Constraint(expr=   m.x1 + m.x2 + m.x3 + m.x4 + m.x5 + m.x6 + m.x7 + m.x8 + m.x9 - 800*m.b98 >= 0)

m.c150 = Constraint(expr=   m.x1 + m.x2 + m.x3 + m.x4 + m.x5 + m.x6 + m.x7 + m.x8 + m.x9 + m.x10 - 800*m.b99 >= 0)

m.c151 = Constraint(expr= - 800*m.b89 >= 0)

m.c152 = Constraint(expr=   m.x12 - 800*m.b90 >= 0)

m.c153 = Constraint(expr=   m.x12 + m.x13 - 800*m.b91 >= 0)

m.c154 = Constraint(expr=   m.x12 + m.x13 + m.x14 - 800*m.b92 >= 0)

m.c155 = Constraint(expr=   m.x12 + m.x13 + m.x14 + m.x15 - 800*m.b93 >= 0)

m.c156 = Constraint(expr=   m.x12 + m.x13 + m.x14 + m.x15 + m.x16 - 800*m.b94 >= 0)

m.c157 = Constraint(expr=   m.x12 + m.x13 + m.x14 + m.x15 + m.x16 + m.x17 - 800*m.b95 >= 0)

m.c158 = Constraint(expr=   m.x12 + m.x13 + m.x14 + m.x15 + m.x16 + m.x17 + m.x18 - 800*m.b96 >= 0)

m.c159 = Constraint(expr=   m.x12 + m.x13 + m.x14 + m.x15 + m.x16 + m.x17 + m.x18 + m.x19 - 800*m.b97 >= 0)

m.c160 = Constraint(expr=   m.x12 + m.x13 + m.x14 + m.x15 + m.x16 + m.x17 + m.x18 + m.x19 + m.x20 - 800*m.b98 >= 0)

m.c161 = Constraint(expr=   m.x12 + m.x13 + m.x14 + m.x15 + m.x16 + m.x17 + m.x18 + m.x19 + m.x20 + m.x21 - 800*m.b99
                          >= 0)

m.c162 = Constraint(expr= - 800*m.b111 >= 0)

m.c163 = Constraint(expr=   m.x34 - 800*m.b112 >= 0)

m.c164 = Constraint(expr=   m.x34 + m.x35 - 800*m.b113 >= 0)

m.c165 = Constraint(expr=   m.x34 + m.x35 + m.x36 - 800*m.b114 >= 0)

m.c166 = Constraint(expr=   m.x34 + m.x35 + m.x36 + m.x37 - 800*m.b115 >= 0)

m.c167 = Constraint(expr=   m.x34 + m.x35 + m.x36 + m.x37 + m.x38 - 800*m.b116 >= 0)

m.c168 = Constraint(expr=   m.x34 + m.x35 + m.x36 + m.x37 + m.x38 + m.x39 - 800*m.b117 >= 0)

m.c169 = Constraint(expr=   m.x34 + m.x35 + m.x36 + m.x37 + m.x38 + m.x39 + m.x40 - 800*m.b118 >= 0)

m.c170 = Constraint(expr=   m.x34 + m.x35 + m.x36 + m.x37 + m.x38 + m.x39 + m.x40 + m.x41 - 800*m.b119 >= 0)

m.c171 = Constraint(expr=   m.x34 + m.x35 + m.x36 + m.x37 + m.x38 + m.x39 + m.x40 + m.x41 + m.x42 - 800*m.b120 >= 0)

m.c172 = Constraint(expr=   m.x34 + m.x35 + m.x36 + m.x37 + m.x38 + m.x39 + m.x40 + m.x41 + m.x42 + m.x43 - 800*m.b121
                          >= 0)

m.c173 = Constraint(expr= - 800*m.b122 >= 0)

m.c174 = Constraint(expr=   m.x34 - 800*m.b123 >= 0)

m.c175 = Constraint(expr=   m.x34 + m.x35 - 800*m.b124 >= 0)

m.c176 = Constraint(expr=   m.x34 + m.x35 + m.x36 - 800*m.b125 >= 0)

m.c177 = Constraint(expr=   m.x34 + m.x35 + m.x36 + m.x37 - 800*m.b126 >= 0)

m.c178 = Constraint(expr=   m.x34 + m.x35 + m.x36 + m.x37 + m.x38 - 800*m.b127 >= 0)

m.c179 = Constraint(expr=   m.x34 + m.x35 + m.x36 + m.x37 + m.x38 + m.x39 - 800*m.b128 >= 0)

m.c180 = Constraint(expr=   m.x34 + m.x35 + m.x36 + m.x37 + m.x38 + m.x39 + m.x40 - 800*m.b129 >= 0)

m.c181 = Constraint(expr=   m.x34 + m.x35 + m.x36 + m.x37 + m.x38 + m.x39 + m.x40 + m.x41 - 800*m.b130 >= 0)

m.c182 = Constraint(expr=   m.x34 + m.x35 + m.x36 + m.x37 + m.x38 + m.x39 + m.x40 + m.x41 + m.x42 - 800*m.b131 >= 0)

m.c183 = Constraint(expr=   m.x34 + m.x35 + m.x36 + m.x37 + m.x38 + m.x39 + m.x40 + m.x41 + m.x42 + m.x43 - 800*m.b132
                          >= 0)

m.c184 = Constraint(expr= - 800*m.b122 >= 0)

m.c185 = Constraint(expr=   m.x45 - 800*m.b123 >= 0)

m.c186 = Constraint(expr=   m.x45 + m.x46 - 800*m.b124 >= 0)

m.c187 = Constraint(expr=   m.x45 + m.x46 + m.x47 - 800*m.b125 >= 0)

m.c188 = Constraint(expr=   m.x45 + m.x46 + m.x47 + m.x48 - 800*m.b126 >= 0)

m.c189 = Constraint(expr=   m.x45 + m.x46 + m.x47 + m.x48 + m.x49 - 800*m.b127 >= 0)

m.c190 = Constraint(expr=   m.x45 + m.x46 + m.x47 + m.x48 + m.x49 + m.x50 - 800*m.b128 >= 0)

m.c191 = Constraint(expr=   m.x45 + m.x46 + m.x47 + m.x48 + m.x49 + m.x50 + m.x51 - 800*m.b129 >= 0)

m.c192 = Constraint(expr=   m.x45 + m.x46 + m.x47 + m.x48 + m.x49 + m.x50 + m.x51 + m.x52 - 800*m.b130 >= 0)

m.c193 = Constraint(expr=   m.x45 + m.x46 + m.x47 + m.x48 + m.x49 + m.x50 + m.x51 + m.x52 + m.x53 - 800*m.b131 >= 0)

m.c194 = Constraint(expr=   m.x45 + m.x46 + m.x47 + m.x48 + m.x49 + m.x50 + m.x51 + m.x52 + m.x53 + m.x54 - 800*m.b132
                          >= 0)

m.c195 = Constraint(expr=m.x167*m.x156 + m.x145 == 13)

m.c196 = Constraint(expr=m.x168*m.x156 + m.x145 == 14)

m.c197 = Constraint(expr=m.x169*m.x156 + m.x145 == 15)

m.c198 = Constraint(expr=m.x170*m.x157 + m.x146 == 13)

m.c199 = Constraint(expr=m.x171*m.x157 + m.x146 == 14)

m.c200 = Constraint(expr=m.x172*m.x157 + m.x146 == 15)

m.c201 = Constraint(expr=m.x173*m.x158 + m.x147 == 13)

m.c202 = Constraint(expr=m.x174*m.x158 + m.x147 == 14)

m.c203 = Constraint(expr=m.x175*m.x158 + m.x147 == 15)

m.c204 = Constraint(expr=m.x176*m.x159 + m.x148 == 13)

m.c205 = Constraint(expr=m.x177*m.x159 + m.x148 == 14)

m.c206 = Constraint(expr=m.x178*m.x159 + m.x148 == 15)

m.c207 = Constraint(expr=m.x179*m.x160 + m.x149 == 13)

m.c208 = Constraint(expr=m.x180*m.x160 + m.x149 == 14)

m.c209 = Constraint(expr=m.x181*m.x160 + m.x149 == 15)

m.c210 = Constraint(expr=m.x182*m.x161 + m.x150 == 13)

m.c211 = Constraint(expr=m.x183*m.x161 + m.x150 == 14)

m.c212 = Constraint(expr=m.x184*m.x161 + m.x150 == 15)

m.c213 = Constraint(expr=m.x185*m.x162 + m.x151 == 13)

m.c214 = Constraint(expr=m.x186*m.x162 + m.x151 == 14)

m.c215 = Constraint(expr=m.x187*m.x162 + m.x151 == 15)

m.c216 = Constraint(expr=m.x188*m.x163 + m.x152 == 13)

m.c217 = Constraint(expr=m.x189*m.x163 + m.x152 == 14)

m.c218 = Constraint(expr=m.x190*m.x163 + m.x152 == 15)

m.c219 = Constraint(expr=m.x191*m.x164 + m.x153 == 13)

m.c220 = Constraint(expr=m.x192*m.x164 + m.x153 == 14)

m.c221 = Constraint(expr=m.x193*m.x164 + m.x153 == 15)

m.c222 = Constraint(expr=m.x194*m.x165 + m.x154 == 13)

m.c223 = Constraint(expr=m.x195*m.x165 + m.x154 == 14)

m.c224 = Constraint(expr=m.x196*m.x165 + m.x154 == 15)

m.c225 = Constraint(expr=m.x197*m.x166 + m.x155 == 13)

m.c226 = Constraint(expr=m.x198*m.x166 + m.x155 == 14)

m.c227 = Constraint(expr=m.x199*m.x166 + m.x155 == 15)

m.c228 = Constraint(expr=-errorf(m.x167) + m.x200 == 0)

m.c229 = Constraint(expr=-errorf(m.x168) + m.x201 == 0)

m.c230 = Constraint(expr=-errorf(m.x169) + m.x202 == 0)

m.c231 = Constraint(expr=-errorf(m.x170) + m.x203 == 0)

m.c232 = Constraint(expr=-errorf(m.x171) + m.x204 == 0)

m.c233 = Constraint(expr=-errorf(m.x172) + m.x205 == 0)

m.c234 = Constraint(expr=-errorf(m.x173) + m.x206 == 0)

m.c235 = Constraint(expr=-errorf(m.x174) + m.x207 == 0)

m.c236 = Constraint(expr=-errorf(m.x175) + m.x208 == 0)

m.c237 = Constraint(expr=-errorf(m.x176) + m.x209 == 0)

m.c238 = Constraint(expr=-errorf(m.x177) + m.x210 == 0)

m.c239 = Constraint(expr=-errorf(m.x178) + m.x211 == 0)

m.c240 = Constraint(expr=-errorf(m.x179) + m.x212 == 0)

m.c241 = Constraint(expr=-errorf(m.x180) + m.x213 == 0)

m.c242 = Constraint(expr=-errorf(m.x181) + m.x214 == 0)

m.c243 = Constraint(expr=-errorf(m.x182) + m.x215 == 0)

m.c244 = Constraint(expr=-errorf(m.x183) + m.x216 == 0)

m.c245 = Constraint(expr=-errorf(m.x184) + m.x217 == 0)

m.c246 = Constraint(expr=-errorf(m.x185) + m.x218 == 0)

m.c247 = Constraint(expr=-errorf(m.x186) + m.x219 == 0)

m.c248 = Constraint(expr=-errorf(m.x187) + m.x220 == 0)

m.c249 = Constraint(expr=-errorf(m.x188) + m.x221 == 0)

m.c250 = Constraint(expr=-errorf(m.x189) + m.x222 == 0)

m.c251 = Constraint(expr=-errorf(m.x190) + m.x223 == 0)

m.c252 = Constraint(expr=-errorf(m.x191) + m.x224 == 0)

m.c253 = Constraint(expr=-errorf(m.x192) + m.x225 == 0)

m.c254 = Constraint(expr=-errorf(m.x193) + m.x226 == 0)

m.c255 = Constraint(expr=-errorf(m.x194) + m.x227 == 0)

m.c256 = Constraint(expr=-errorf(m.x195) + m.x228 == 0)

m.c257 = Constraint(expr=-errorf(m.x196) + m.x229 == 0)

m.c258 = Constraint(expr=-errorf(m.x197) + m.x230 == 0)

m.c259 = Constraint(expr=-errorf(m.x198) + m.x231 == 0)

m.c260 = Constraint(expr=-errorf(m.x199) + m.x232 == 0)

m.c261 = Constraint(expr=   m.x200 + m.x233 == 1)

m.c262 = Constraint(expr=   m.x201 + m.x234 == 1)

m.c263 = Constraint(expr=   m.x202 + m.x235 == 1)

m.c264 = Constraint(expr=   m.x203 + m.x236 == 1)

m.c265 = Constraint(expr=   m.x204 + m.x237 == 1)

m.c266 = Constraint(expr=   m.x205 + m.x238 == 1)

m.c267 = Constraint(expr=   m.x206 + m.x239 == 1)

m.c268 = Constraint(expr=   m.x207 + m.x240 == 1)

m.c269 = Constraint(expr=   m.x208 + m.x241 == 1)

m.c270 = Constraint(expr=   m.x209 + m.x242 == 1)

m.c271 = Constraint(expr=   m.x210 + m.x243 == 1)

m.c272 = Constraint(expr=   m.x211 + m.x244 == 1)

m.c273 = Constraint(expr=   m.x212 + m.x245 == 1)

m.c274 = Constraint(expr=   m.x213 + m.x246 == 1)

m.c275 = Constraint(expr=   m.x214 + m.x247 == 1)

m.c276 = Constraint(expr=   m.x215 + m.x248 == 1)

m.c277 = Constraint(expr=   m.x216 + m.x249 == 1)

m.c278 = Constraint(expr=   m.x217 + m.x250 == 1)

m.c279 = Constraint(expr=   m.x218 + m.x251 == 1)

m.c280 = Constraint(expr=   m.x219 + m.x252 == 1)

m.c281 = Constraint(expr=   m.x220 + m.x253 == 1)

m.c282 = Constraint(expr=   m.x221 + m.x254 == 1)

m.c283 = Constraint(expr=   m.x222 + m.x255 == 1)

m.c284 = Constraint(expr=   m.x223 + m.x256 == 1)

m.c285 = Constraint(expr=   m.x224 + m.x257 == 1)

m.c286 = Constraint(expr=   m.x225 + m.x258 == 1)

m.c287 = Constraint(expr=   m.x226 + m.x259 == 1)

m.c288 = Constraint(expr=   m.x227 + m.x260 == 1)

m.c289 = Constraint(expr=   m.x228 + m.x261 == 1)

m.c290 = Constraint(expr=   m.x229 + m.x262 == 1)

m.c291 = Constraint(expr=   m.x230 + m.x263 == 1)

m.c292 = Constraint(expr=   m.x231 + m.x264 == 1)

m.c293 = Constraint(expr=   m.x232 + m.x265 == 1)

m.c294 = Constraint(expr=m.x266*m.x200 + 0.398942280401432*exp(-0.5*m.x167**2) == 0)

m.c295 = Constraint(expr=m.x267*m.x201 + 0.398942280401432*exp(-0.5*m.x168**2) == 0)

m.c296 = Constraint(expr=m.x268*m.x202 + 0.398942280401432*exp(-0.5*m.x169**2) == 0)

m.c297 = Constraint(expr=m.x269*m.x203 + 0.398942280401432*exp(-0.5*m.x170**2) == 0)

m.c298 = Constraint(expr=m.x270*m.x204 + 0.398942280401432*exp(-0.5*m.x171**2) == 0)

m.c299 = Constraint(expr=m.x271*m.x205 + 0.398942280401432*exp(-0.5*m.x172**2) == 0)

m.c300 = Constraint(expr=m.x272*m.x206 + 0.398942280401432*exp(-0.5*m.x173**2) == 0)

m.c301 = Constraint(expr=m.x273*m.x207 + 0.398942280401432*exp(-0.5*m.x174**2) == 0)

m.c302 = Constraint(expr=m.x274*m.x208 + 0.398942280401432*exp(-0.5*m.x175**2) == 0)

m.c303 = Constraint(expr=m.x275*m.x209 + 0.398942280401432*exp(-0.5*m.x176**2) == 0)

m.c304 = Constraint(expr=m.x276*m.x210 + 0.398942280401432*exp(-0.5*m.x177**2) == 0)

m.c305 = Constraint(expr=m.x277*m.x211 + 0.398942280401432*exp(-0.5*m.x178**2) == 0)

m.c306 = Constraint(expr=m.x278*m.x212 + 0.398942280401432*exp(-0.5*m.x179**2) == 0)

m.c307 = Constraint(expr=m.x279*m.x213 + 0.398942280401432*exp(-0.5*m.x180**2) == 0)

m.c308 = Constraint(expr=m.x280*m.x214 + 0.398942280401432*exp(-0.5*m.x181**2) == 0)

m.c309 = Constraint(expr=m.x281*m.x215 + 0.398942280401432*exp(-0.5*m.x182**2) == 0)

m.c310 = Constraint(expr=m.x282*m.x216 + 0.398942280401432*exp(-0.5*m.x183**2) == 0)

m.c311 = Constraint(expr=m.x283*m.x217 + 0.398942280401432*exp(-0.5*m.x184**2) == 0)

m.c312 = Constraint(expr=m.x284*m.x218 + 0.398942280401432*exp(-0.5*m.x185**2) == 0)

m.c313 = Constraint(expr=m.x285*m.x219 + 0.398942280401432*exp(-0.5*m.x186**2) == 0)

m.c314 = Constraint(expr=m.x286*m.x220 + 0.398942280401432*exp(-0.5*m.x187**2) == 0)

m.c315 = Constraint(expr=m.x287*m.x221 + 0.398942280401432*exp(-0.5*m.x188**2) == 0)

m.c316 = Constraint(expr=m.x288*m.x222 + 0.398942280401432*exp(-0.5*m.x189**2) == 0)

m.c317 = Constraint(expr=m.x289*m.x223 + 0.398942280401432*exp(-0.5*m.x190**2) == 0)

m.c318 = Constraint(expr=m.x290*m.x224 + 0.398942280401432*exp(-0.5*m.x191**2) == 0)

m.c319 = Constraint(expr=m.x291*m.x225 + 0.398942280401432*exp(-0.5*m.x192**2) == 0)

m.c320 = Constraint(expr=m.x292*m.x226 + 0.398942280401432*exp(-0.5*m.x193**2) == 0)

m.c321 = Constraint(expr=m.x293*m.x227 + 0.398942280401432*exp(-0.5*m.x194**2) == 0)

m.c322 = Constraint(expr=m.x294*m.x228 + 0.398942280401432*exp(-0.5*m.x195**2) == 0)

m.c323 = Constraint(expr=m.x295*m.x229 + 0.398942280401432*exp(-0.5*m.x196**2) == 0)

m.c324 = Constraint(expr=m.x296*m.x230 + 0.398942280401432*exp(-0.5*m.x197**2) == 0)

m.c325 = Constraint(expr=m.x297*m.x231 + 0.398942280401432*exp(-0.5*m.x198**2) == 0)

m.c326 = Constraint(expr=m.x298*m.x232 + 0.398942280401432*exp(-0.5*m.x199**2) == 0)

m.c327 = Constraint(expr=m.x299*m.x233 - 0.398942280401432*exp(-0.5*m.x167**2) == 0)

m.c328 = Constraint(expr=m.x300*m.x234 - 0.398942280401432*exp(-0.5*m.x168**2) == 0)

m.c329 = Constraint(expr=m.x301*m.x235 - 0.398942280401432*exp(-0.5*m.x169**2) == 0)

m.c330 = Constraint(expr=m.x302*m.x236 - 0.398942280401432*exp(-0.5*m.x170**2) == 0)

m.c331 = Constraint(expr=m.x303*m.x237 - 0.398942280401432*exp(-0.5*m.x171**2) == 0)

m.c332 = Constraint(expr=m.x304*m.x238 - 0.398942280401432*exp(-0.5*m.x172**2) == 0)

m.c333 = Constraint(expr=m.x305*m.x239 - 0.398942280401432*exp(-0.5*m.x173**2) == 0)

m.c334 = Constraint(expr=m.x306*m.x240 - 0.398942280401432*exp(-0.5*m.x174**2) == 0)

m.c335 = Constraint(expr=m.x307*m.x241 - 0.398942280401432*exp(-0.5*m.x175**2) == 0)

m.c336 = Constraint(expr=m.x308*m.x242 - 0.398942280401432*exp(-0.5*m.x176**2) == 0)

m.c337 = Constraint(expr=m.x309*m.x243 - 0.398942280401432*exp(-0.5*m.x177**2) == 0)

m.c338 = Constraint(expr=m.x310*m.x244 - 0.398942280401432*exp(-0.5*m.x178**2) == 0)

m.c339 = Constraint(expr=m.x311*m.x245 - 0.398942280401432*exp(-0.5*m.x179**2) == 0)

m.c340 = Constraint(expr=m.x312*m.x246 - 0.398942280401432*exp(-0.5*m.x180**2) == 0)

m.c341 = Constraint(expr=m.x313*m.x247 - 0.398942280401432*exp(-0.5*m.x181**2) == 0)

m.c342 = Constraint(expr=m.x314*m.x248 - 0.398942280401432*exp(-0.5*m.x182**2) == 0)

m.c343 = Constraint(expr=m.x315*m.x249 - 0.398942280401432*exp(-0.5*m.x183**2) == 0)

m.c344 = Constraint(expr=m.x316*m.x250 - 0.398942280401432*exp(-0.5*m.x184**2) == 0)

m.c345 = Constraint(expr=m.x317*m.x251 - 0.398942280401432*exp(-0.5*m.x185**2) == 0)

m.c346 = Constraint(expr=m.x318*m.x252 - 0.398942280401432*exp(-0.5*m.x186**2) == 0)

m.c347 = Constraint(expr=m.x319*m.x253 - 0.398942280401432*exp(-0.5*m.x187**2) == 0)

m.c348 = Constraint(expr=m.x320*m.x254 - 0.398942280401432*exp(-0.5*m.x188**2) == 0)

m.c349 = Constraint(expr=m.x321*m.x255 - 0.398942280401432*exp(-0.5*m.x189**2) == 0)

m.c350 = Constraint(expr=m.x322*m.x256 - 0.398942280401432*exp(-0.5*m.x190**2) == 0)

m.c351 = Constraint(expr=m.x323*m.x257 - 0.398942280401432*exp(-0.5*m.x191**2) == 0)

m.c352 = Constraint(expr=m.x324*m.x258 - 0.398942280401432*exp(-0.5*m.x192**2) == 0)

m.c353 = Constraint(expr=m.x325*m.x259 - 0.398942280401432*exp(-0.5*m.x193**2) == 0)

m.c354 = Constraint(expr=m.x326*m.x260 - 0.398942280401432*exp(-0.5*m.x194**2) == 0)

m.c355 = Constraint(expr=m.x327*m.x261 - 0.398942280401432*exp(-0.5*m.x195**2) == 0)

m.c356 = Constraint(expr=m.x328*m.x262 - 0.398942280401432*exp(-0.5*m.x196**2) == 0)

m.c357 = Constraint(expr=m.x329*m.x263 - 0.398942280401432*exp(-0.5*m.x197**2) == 0)

m.c358 = Constraint(expr=m.x330*m.x264 - 0.398942280401432*exp(-0.5*m.x198**2) == 0)

m.c359 = Constraint(expr=m.x331*m.x265 - 0.398942280401432*exp(-0.5*m.x199**2) == 0)
