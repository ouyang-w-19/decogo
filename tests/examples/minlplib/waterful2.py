#  MINLP written by GAMS Convert at 04/21/18 13:55:13
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        384      180       64      140        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        630      182       56        0      392        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       2479     2363      116        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x34 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x35 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x36 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x37 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x38 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x39 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x40 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x41 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x42 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x43 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x44 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x45 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x46 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x47 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x48 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x49 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x50 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x51 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x52 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x53 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x54 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x55 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x56 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x57 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x58 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x59 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x60 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x61 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x62 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x63 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x64 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x65 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x66 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x67 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x68 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x69 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x70 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x71 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x72 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x73 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x74 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x75 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x76 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x77 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x78 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x79 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x80 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x81 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x82 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x83 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x84 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x85 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x86 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x87 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x88 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x89 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x90 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x91 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x92 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x93 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x94 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x95 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x96 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x97 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x98 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x99 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x100 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x101 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x102 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x103 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x104 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x105 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x106 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x107 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x108 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x109 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x110 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x111 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x112 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x113 = Var(within=Reals,bounds=(6.5,None),initialize=11.5)
m.x114 = Var(within=Reals,bounds=(3.25,None),initialize=8.25)
m.x115 = Var(within=Reals,bounds=(16.58,None),initialize=21.58)
m.x116 = Var(within=Reals,bounds=(14.92,None),initialize=19.92)
m.x117 = Var(within=Reals,bounds=(12.925,None),initialize=17.925)
m.x118 = Var(within=Reals,bounds=(12.26,None),initialize=17.26)
m.x119 = Var(within=Reals,bounds=(8.76,None),initialize=13.76)
m.x120 = Var(within=Reals,bounds=(16.08,None),initialize=21.08)
m.x121 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x122 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x123 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x124 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x125 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x126 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x127 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x128 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x129 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x130 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x131 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x132 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x133 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x134 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x135 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x136 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x137 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x138 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x139 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x140 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x141 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x142 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x143 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x144 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x145 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x146 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x147 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x148 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x149 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x150 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x151 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x152 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x153 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x154 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x155 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x156 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x157 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x158 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x159 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x160 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x161 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x162 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x163 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x164 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x165 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x166 = Var(within=Reals,bounds=(None,None),initialize=0)
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
m.x177 = Var(within=Reals,bounds=(0,2.5),initialize=0.961470588235294)
m.x178 = Var(within=Reals,bounds=(0,6),initialize=2.30752941176471)
m.x179 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x180 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x181 = Var(within=Reals,bounds=(None,None),initialize=0)
m.b183 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b184 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b185 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b186 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b187 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b188 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b189 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b190 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b191 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b192 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b193 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b194 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b195 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b196 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b197 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b198 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b199 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b200 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b201 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b202 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b203 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b204 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b205 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b206 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b207 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b208 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b209 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b210 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b211 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b212 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b213 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b214 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b215 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b216 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b217 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b218 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b219 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b220 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b221 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b222 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b223 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b224 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b225 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b226 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b227 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b228 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b229 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b230 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b231 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b232 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b233 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b234 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b235 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b236 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b237 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b238 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.s1s239 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s240 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s241 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s242 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s243 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s244 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s245 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s246 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s247 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s248 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s249 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s250 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s251 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s252 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s253 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s254 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s255 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s256 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s257 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s258 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s259 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s260 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s261 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s262 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s263 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s264 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s265 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s266 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s267 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s268 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s269 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s270 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s271 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s272 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s273 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s274 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s275 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s276 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s277 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s278 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s279 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s280 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s281 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s282 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s283 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s284 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s285 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s286 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s287 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s288 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s289 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s290 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s291 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s292 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s293 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s294 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s295 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s296 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s297 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s298 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s299 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s300 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s301 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s302 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s303 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s304 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s305 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s306 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s307 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s308 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s309 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s310 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s311 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s312 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s313 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s314 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s315 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s316 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s317 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s318 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s319 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s320 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s321 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s322 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s323 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s324 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s325 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s326 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s327 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s328 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s329 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s330 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s331 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s332 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s333 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s334 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s335 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s336 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s337 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s338 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s339 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s340 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s341 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s342 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s343 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s344 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s345 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s346 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s347 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s348 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s349 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s350 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s351 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s352 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s353 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s354 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s355 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s356 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s357 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s358 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s359 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s360 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s361 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s362 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s363 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s364 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s365 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s366 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s367 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s368 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s369 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s370 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s371 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s372 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s373 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s374 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s375 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s376 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s377 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s378 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s379 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s380 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s381 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s382 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s383 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s384 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s385 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s386 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s387 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s388 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s389 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s390 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s391 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s392 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s393 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s394 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s395 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s396 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s397 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s398 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s399 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s400 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s401 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s402 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s403 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s404 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s405 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s406 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s407 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s408 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s409 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s410 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s411 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s412 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s413 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s414 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s415 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s416 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s417 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s418 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s419 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s420 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s421 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s422 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s423 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s424 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s425 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s426 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s427 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s428 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s429 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s430 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s431 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s432 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s433 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s434 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s435 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s436 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s437 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s438 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s439 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s440 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s441 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s442 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s443 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s444 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s445 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s446 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s447 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s448 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s449 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s450 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s451 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s452 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s453 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s454 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s455 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s456 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s457 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s458 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s459 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s460 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s461 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s462 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s463 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s464 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s465 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s466 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s467 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s468 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s469 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s470 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s471 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s472 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s473 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s474 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s475 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s476 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s477 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s478 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s479 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s480 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s481 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s482 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s483 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s484 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s485 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s486 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s487 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s488 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s489 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s490 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s491 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s492 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s493 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s494 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s495 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s496 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s497 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s498 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s499 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s500 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s501 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s502 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s503 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s504 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s505 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s506 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s507 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s508 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s509 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s510 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s511 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s512 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s513 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s514 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s515 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s516 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s517 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s518 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s519 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s520 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s521 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s522 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s523 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s524 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s525 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s526 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s527 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s528 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s529 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s530 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s531 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s532 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s533 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s534 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s535 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s536 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s537 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s538 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s539 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s540 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s541 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s542 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s543 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s544 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s545 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s546 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s547 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s548 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s549 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s550 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s551 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s552 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s553 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s554 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s555 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s556 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s557 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s558 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s559 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s560 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s561 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s562 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s563 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s564 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s565 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s566 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s567 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s568 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s569 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s570 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s571 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s572 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s573 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s574 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s575 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s576 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s577 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s578 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s579 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s580 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s581 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s582 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s583 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s584 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s585 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s586 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s587 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s588 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s589 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s590 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s591 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s592 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s593 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s594 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s595 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s596 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s597 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s598 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s599 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s600 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s601 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s602 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s603 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s604 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s605 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s606 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s607 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s608 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s609 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s610 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s611 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s612 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s613 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s614 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s615 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s616 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s617 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s618 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s619 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s620 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s621 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s622 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s623 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s624 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s625 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s626 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s627 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s628 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s629 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s630 = Var(within=CannotHandle,bounds=(0,None),initialize=0)

suffix sosno integer IN;
suffix ref integer IN;
let m.s1s239.sosno := 1;
let m.s1s239.ref   := 1;
let m.s1s240.sosno := 1;
let m.s1s240.ref   := 2;
let m.s1s241.sosno := 1;
let m.s1s241.ref   := 3;
let m.s1s242.sosno := 1;
let m.s1s242.ref   := 4;
let m.s1s243.sosno := 1;
let m.s1s243.ref   := 5;
let m.s1s244.sosno := 1;
let m.s1s244.ref   := 6;
let m.s1s245.sosno := 1;
let m.s1s245.ref   := 7;
let m.s1s246.sosno := 2;
let m.s1s246.ref   := 1;
let m.s1s247.sosno := 2;
let m.s1s247.ref   := 2;
let m.s1s248.sosno := 2;
let m.s1s248.ref   := 3;
let m.s1s249.sosno := 2;
let m.s1s249.ref   := 4;
let m.s1s250.sosno := 2;
let m.s1s250.ref   := 5;
let m.s1s251.sosno := 2;
let m.s1s251.ref   := 6;
let m.s1s252.sosno := 2;
let m.s1s252.ref   := 7;
let m.s1s253.sosno := 3;
let m.s1s253.ref   := 1;
let m.s1s254.sosno := 3;
let m.s1s254.ref   := 2;
let m.s1s255.sosno := 3;
let m.s1s255.ref   := 3;
let m.s1s256.sosno := 3;
let m.s1s256.ref   := 4;
let m.s1s257.sosno := 3;
let m.s1s257.ref   := 5;
let m.s1s258.sosno := 3;
let m.s1s258.ref   := 6;
let m.s1s259.sosno := 3;
let m.s1s259.ref   := 7;
let m.s1s260.sosno := 4;
let m.s1s260.ref   := 1;
let m.s1s261.sosno := 4;
let m.s1s261.ref   := 2;
let m.s1s262.sosno := 4;
let m.s1s262.ref   := 3;
let m.s1s263.sosno := 4;
let m.s1s263.ref   := 4;
let m.s1s264.sosno := 4;
let m.s1s264.ref   := 5;
let m.s1s265.sosno := 4;
let m.s1s265.ref   := 6;
let m.s1s266.sosno := 4;
let m.s1s266.ref   := 7;
let m.s1s267.sosno := 5;
let m.s1s267.ref   := 1;
let m.s1s268.sosno := 5;
let m.s1s268.ref   := 2;
let m.s1s269.sosno := 5;
let m.s1s269.ref   := 3;
let m.s1s270.sosno := 5;
let m.s1s270.ref   := 4;
let m.s1s271.sosno := 5;
let m.s1s271.ref   := 5;
let m.s1s272.sosno := 5;
let m.s1s272.ref   := 6;
let m.s1s273.sosno := 5;
let m.s1s273.ref   := 7;
let m.s1s274.sosno := 6;
let m.s1s274.ref   := 1;
let m.s1s275.sosno := 6;
let m.s1s275.ref   := 2;
let m.s1s276.sosno := 6;
let m.s1s276.ref   := 3;
let m.s1s277.sosno := 6;
let m.s1s277.ref   := 4;
let m.s1s278.sosno := 6;
let m.s1s278.ref   := 5;
let m.s1s279.sosno := 6;
let m.s1s279.ref   := 6;
let m.s1s280.sosno := 6;
let m.s1s280.ref   := 7;
let m.s1s281.sosno := 7;
let m.s1s281.ref   := 1;
let m.s1s282.sosno := 7;
let m.s1s282.ref   := 2;
let m.s1s283.sosno := 7;
let m.s1s283.ref   := 3;
let m.s1s284.sosno := 7;
let m.s1s284.ref   := 4;
let m.s1s285.sosno := 7;
let m.s1s285.ref   := 5;
let m.s1s286.sosno := 7;
let m.s1s286.ref   := 6;
let m.s1s287.sosno := 7;
let m.s1s287.ref   := 7;
let m.s1s288.sosno := 8;
let m.s1s288.ref   := 1;
let m.s1s289.sosno := 8;
let m.s1s289.ref   := 2;
let m.s1s290.sosno := 8;
let m.s1s290.ref   := 3;
let m.s1s291.sosno := 8;
let m.s1s291.ref   := 4;
let m.s1s292.sosno := 8;
let m.s1s292.ref   := 5;
let m.s1s293.sosno := 8;
let m.s1s293.ref   := 6;
let m.s1s294.sosno := 8;
let m.s1s294.ref   := 7;
let m.s1s295.sosno := 9;
let m.s1s295.ref   := 1;
let m.s1s296.sosno := 9;
let m.s1s296.ref   := 2;
let m.s1s297.sosno := 9;
let m.s1s297.ref   := 3;
let m.s1s298.sosno := 9;
let m.s1s298.ref   := 4;
let m.s1s299.sosno := 9;
let m.s1s299.ref   := 5;
let m.s1s300.sosno := 9;
let m.s1s300.ref   := 6;
let m.s1s301.sosno := 9;
let m.s1s301.ref   := 7;
let m.s1s302.sosno := 10;
let m.s1s302.ref   := 1;
let m.s1s303.sosno := 10;
let m.s1s303.ref   := 2;
let m.s1s304.sosno := 10;
let m.s1s304.ref   := 3;
let m.s1s305.sosno := 10;
let m.s1s305.ref   := 4;
let m.s1s306.sosno := 10;
let m.s1s306.ref   := 5;
let m.s1s307.sosno := 10;
let m.s1s307.ref   := 6;
let m.s1s308.sosno := 10;
let m.s1s308.ref   := 7;
let m.s1s309.sosno := 11;
let m.s1s309.ref   := 1;
let m.s1s310.sosno := 11;
let m.s1s310.ref   := 2;
let m.s1s311.sosno := 11;
let m.s1s311.ref   := 3;
let m.s1s312.sosno := 11;
let m.s1s312.ref   := 4;
let m.s1s313.sosno := 11;
let m.s1s313.ref   := 5;
let m.s1s314.sosno := 11;
let m.s1s314.ref   := 6;
let m.s1s315.sosno := 11;
let m.s1s315.ref   := 7;
let m.s1s316.sosno := 12;
let m.s1s316.ref   := 1;
let m.s1s317.sosno := 12;
let m.s1s317.ref   := 2;
let m.s1s318.sosno := 12;
let m.s1s318.ref   := 3;
let m.s1s319.sosno := 12;
let m.s1s319.ref   := 4;
let m.s1s320.sosno := 12;
let m.s1s320.ref   := 5;
let m.s1s321.sosno := 12;
let m.s1s321.ref   := 6;
let m.s1s322.sosno := 12;
let m.s1s322.ref   := 7;
let m.s1s323.sosno := 13;
let m.s1s323.ref   := 1;
let m.s1s324.sosno := 13;
let m.s1s324.ref   := 2;
let m.s1s325.sosno := 13;
let m.s1s325.ref   := 3;
let m.s1s326.sosno := 13;
let m.s1s326.ref   := 4;
let m.s1s327.sosno := 13;
let m.s1s327.ref   := 5;
let m.s1s328.sosno := 13;
let m.s1s328.ref   := 6;
let m.s1s329.sosno := 13;
let m.s1s329.ref   := 7;
let m.s1s330.sosno := 14;
let m.s1s330.ref   := 1;
let m.s1s331.sosno := 14;
let m.s1s331.ref   := 2;
let m.s1s332.sosno := 14;
let m.s1s332.ref   := 3;
let m.s1s333.sosno := 14;
let m.s1s333.ref   := 4;
let m.s1s334.sosno := 14;
let m.s1s334.ref   := 5;
let m.s1s335.sosno := 14;
let m.s1s335.ref   := 6;
let m.s1s336.sosno := 14;
let m.s1s336.ref   := 7;
let m.s1s337.sosno := 15;
let m.s1s337.ref   := 1;
let m.s1s338.sosno := 15;
let m.s1s338.ref   := 2;
let m.s1s339.sosno := 15;
let m.s1s339.ref   := 3;
let m.s1s340.sosno := 15;
let m.s1s340.ref   := 4;
let m.s1s341.sosno := 15;
let m.s1s341.ref   := 5;
let m.s1s342.sosno := 15;
let m.s1s342.ref   := 6;
let m.s1s343.sosno := 15;
let m.s1s343.ref   := 7;
let m.s1s344.sosno := 16;
let m.s1s344.ref   := 1;
let m.s1s345.sosno := 16;
let m.s1s345.ref   := 2;
let m.s1s346.sosno := 16;
let m.s1s346.ref   := 3;
let m.s1s347.sosno := 16;
let m.s1s347.ref   := 4;
let m.s1s348.sosno := 16;
let m.s1s348.ref   := 5;
let m.s1s349.sosno := 16;
let m.s1s349.ref   := 6;
let m.s1s350.sosno := 16;
let m.s1s350.ref   := 7;
let m.s1s351.sosno := 17;
let m.s1s351.ref   := 1;
let m.s1s352.sosno := 17;
let m.s1s352.ref   := 2;
let m.s1s353.sosno := 17;
let m.s1s353.ref   := 3;
let m.s1s354.sosno := 17;
let m.s1s354.ref   := 4;
let m.s1s355.sosno := 17;
let m.s1s355.ref   := 5;
let m.s1s356.sosno := 17;
let m.s1s356.ref   := 6;
let m.s1s357.sosno := 17;
let m.s1s357.ref   := 7;
let m.s1s358.sosno := 18;
let m.s1s358.ref   := 1;
let m.s1s359.sosno := 18;
let m.s1s359.ref   := 2;
let m.s1s360.sosno := 18;
let m.s1s360.ref   := 3;
let m.s1s361.sosno := 18;
let m.s1s361.ref   := 4;
let m.s1s362.sosno := 18;
let m.s1s362.ref   := 5;
let m.s1s363.sosno := 18;
let m.s1s363.ref   := 6;
let m.s1s364.sosno := 18;
let m.s1s364.ref   := 7;
let m.s1s365.sosno := 19;
let m.s1s365.ref   := 1;
let m.s1s366.sosno := 19;
let m.s1s366.ref   := 2;
let m.s1s367.sosno := 19;
let m.s1s367.ref   := 3;
let m.s1s368.sosno := 19;
let m.s1s368.ref   := 4;
let m.s1s369.sosno := 19;
let m.s1s369.ref   := 5;
let m.s1s370.sosno := 19;
let m.s1s370.ref   := 6;
let m.s1s371.sosno := 19;
let m.s1s371.ref   := 7;
let m.s1s372.sosno := 20;
let m.s1s372.ref   := 1;
let m.s1s373.sosno := 20;
let m.s1s373.ref   := 2;
let m.s1s374.sosno := 20;
let m.s1s374.ref   := 3;
let m.s1s375.sosno := 20;
let m.s1s375.ref   := 4;
let m.s1s376.sosno := 20;
let m.s1s376.ref   := 5;
let m.s1s377.sosno := 20;
let m.s1s377.ref   := 6;
let m.s1s378.sosno := 20;
let m.s1s378.ref   := 7;
let m.s1s379.sosno := 21;
let m.s1s379.ref   := 1;
let m.s1s380.sosno := 21;
let m.s1s380.ref   := 2;
let m.s1s381.sosno := 21;
let m.s1s381.ref   := 3;
let m.s1s382.sosno := 21;
let m.s1s382.ref   := 4;
let m.s1s383.sosno := 21;
let m.s1s383.ref   := 5;
let m.s1s384.sosno := 21;
let m.s1s384.ref   := 6;
let m.s1s385.sosno := 21;
let m.s1s385.ref   := 7;
let m.s1s386.sosno := 22;
let m.s1s386.ref   := 1;
let m.s1s387.sosno := 22;
let m.s1s387.ref   := 2;
let m.s1s388.sosno := 22;
let m.s1s388.ref   := 3;
let m.s1s389.sosno := 22;
let m.s1s389.ref   := 4;
let m.s1s390.sosno := 22;
let m.s1s390.ref   := 5;
let m.s1s391.sosno := 22;
let m.s1s391.ref   := 6;
let m.s1s392.sosno := 22;
let m.s1s392.ref   := 7;
let m.s1s393.sosno := 23;
let m.s1s393.ref   := 1;
let m.s1s394.sosno := 23;
let m.s1s394.ref   := 2;
let m.s1s395.sosno := 23;
let m.s1s395.ref   := 3;
let m.s1s396.sosno := 23;
let m.s1s396.ref   := 4;
let m.s1s397.sosno := 23;
let m.s1s397.ref   := 5;
let m.s1s398.sosno := 23;
let m.s1s398.ref   := 6;
let m.s1s399.sosno := 23;
let m.s1s399.ref   := 7;
let m.s1s400.sosno := 24;
let m.s1s400.ref   := 1;
let m.s1s401.sosno := 24;
let m.s1s401.ref   := 2;
let m.s1s402.sosno := 24;
let m.s1s402.ref   := 3;
let m.s1s403.sosno := 24;
let m.s1s403.ref   := 4;
let m.s1s404.sosno := 24;
let m.s1s404.ref   := 5;
let m.s1s405.sosno := 24;
let m.s1s405.ref   := 6;
let m.s1s406.sosno := 24;
let m.s1s406.ref   := 7;
let m.s1s407.sosno := 25;
let m.s1s407.ref   := 1;
let m.s1s408.sosno := 25;
let m.s1s408.ref   := 2;
let m.s1s409.sosno := 25;
let m.s1s409.ref   := 3;
let m.s1s410.sosno := 25;
let m.s1s410.ref   := 4;
let m.s1s411.sosno := 25;
let m.s1s411.ref   := 5;
let m.s1s412.sosno := 25;
let m.s1s412.ref   := 6;
let m.s1s413.sosno := 25;
let m.s1s413.ref   := 7;
let m.s1s414.sosno := 26;
let m.s1s414.ref   := 1;
let m.s1s415.sosno := 26;
let m.s1s415.ref   := 2;
let m.s1s416.sosno := 26;
let m.s1s416.ref   := 3;
let m.s1s417.sosno := 26;
let m.s1s417.ref   := 4;
let m.s1s418.sosno := 26;
let m.s1s418.ref   := 5;
let m.s1s419.sosno := 26;
let m.s1s419.ref   := 6;
let m.s1s420.sosno := 26;
let m.s1s420.ref   := 7;
let m.s1s421.sosno := 27;
let m.s1s421.ref   := 1;
let m.s1s422.sosno := 27;
let m.s1s422.ref   := 2;
let m.s1s423.sosno := 27;
let m.s1s423.ref   := 3;
let m.s1s424.sosno := 27;
let m.s1s424.ref   := 4;
let m.s1s425.sosno := 27;
let m.s1s425.ref   := 5;
let m.s1s426.sosno := 27;
let m.s1s426.ref   := 6;
let m.s1s427.sosno := 27;
let m.s1s427.ref   := 7;
let m.s1s428.sosno := 28;
let m.s1s428.ref   := 1;
let m.s1s429.sosno := 28;
let m.s1s429.ref   := 2;
let m.s1s430.sosno := 28;
let m.s1s430.ref   := 3;
let m.s1s431.sosno := 28;
let m.s1s431.ref   := 4;
let m.s1s432.sosno := 28;
let m.s1s432.ref   := 5;
let m.s1s433.sosno := 28;
let m.s1s433.ref   := 6;
let m.s1s434.sosno := 28;
let m.s1s434.ref   := 7;
let m.s1s435.sosno := 29;
let m.s1s435.ref   := 1;
let m.s1s436.sosno := 29;
let m.s1s436.ref   := 2;
let m.s1s437.sosno := 29;
let m.s1s437.ref   := 3;
let m.s1s438.sosno := 29;
let m.s1s438.ref   := 4;
let m.s1s439.sosno := 29;
let m.s1s439.ref   := 5;
let m.s1s440.sosno := 29;
let m.s1s440.ref   := 6;
let m.s1s441.sosno := 29;
let m.s1s441.ref   := 7;
let m.s1s442.sosno := 30;
let m.s1s442.ref   := 1;
let m.s1s443.sosno := 30;
let m.s1s443.ref   := 2;
let m.s1s444.sosno := 30;
let m.s1s444.ref   := 3;
let m.s1s445.sosno := 30;
let m.s1s445.ref   := 4;
let m.s1s446.sosno := 30;
let m.s1s446.ref   := 5;
let m.s1s447.sosno := 30;
let m.s1s447.ref   := 6;
let m.s1s448.sosno := 30;
let m.s1s448.ref   := 7;
let m.s1s449.sosno := 31;
let m.s1s449.ref   := 1;
let m.s1s450.sosno := 31;
let m.s1s450.ref   := 2;
let m.s1s451.sosno := 31;
let m.s1s451.ref   := 3;
let m.s1s452.sosno := 31;
let m.s1s452.ref   := 4;
let m.s1s453.sosno := 31;
let m.s1s453.ref   := 5;
let m.s1s454.sosno := 31;
let m.s1s454.ref   := 6;
let m.s1s455.sosno := 31;
let m.s1s455.ref   := 7;
let m.s1s456.sosno := 32;
let m.s1s456.ref   := 1;
let m.s1s457.sosno := 32;
let m.s1s457.ref   := 2;
let m.s1s458.sosno := 32;
let m.s1s458.ref   := 3;
let m.s1s459.sosno := 32;
let m.s1s459.ref   := 4;
let m.s1s460.sosno := 32;
let m.s1s460.ref   := 5;
let m.s1s461.sosno := 32;
let m.s1s461.ref   := 6;
let m.s1s462.sosno := 32;
let m.s1s462.ref   := 7;
let m.s1s463.sosno := 33;
let m.s1s463.ref   := 1;
let m.s1s464.sosno := 33;
let m.s1s464.ref   := 2;
let m.s1s465.sosno := 33;
let m.s1s465.ref   := 3;
let m.s1s466.sosno := 33;
let m.s1s466.ref   := 4;
let m.s1s467.sosno := 33;
let m.s1s467.ref   := 5;
let m.s1s468.sosno := 33;
let m.s1s468.ref   := 6;
let m.s1s469.sosno := 33;
let m.s1s469.ref   := 7;
let m.s1s470.sosno := 34;
let m.s1s470.ref   := 1;
let m.s1s471.sosno := 34;
let m.s1s471.ref   := 2;
let m.s1s472.sosno := 34;
let m.s1s472.ref   := 3;
let m.s1s473.sosno := 34;
let m.s1s473.ref   := 4;
let m.s1s474.sosno := 34;
let m.s1s474.ref   := 5;
let m.s1s475.sosno := 34;
let m.s1s475.ref   := 6;
let m.s1s476.sosno := 34;
let m.s1s476.ref   := 7;
let m.s1s477.sosno := 35;
let m.s1s477.ref   := 1;
let m.s1s478.sosno := 35;
let m.s1s478.ref   := 2;
let m.s1s479.sosno := 35;
let m.s1s479.ref   := 3;
let m.s1s480.sosno := 35;
let m.s1s480.ref   := 4;
let m.s1s481.sosno := 35;
let m.s1s481.ref   := 5;
let m.s1s482.sosno := 35;
let m.s1s482.ref   := 6;
let m.s1s483.sosno := 35;
let m.s1s483.ref   := 7;
let m.s1s484.sosno := 36;
let m.s1s484.ref   := 1;
let m.s1s485.sosno := 36;
let m.s1s485.ref   := 2;
let m.s1s486.sosno := 36;
let m.s1s486.ref   := 3;
let m.s1s487.sosno := 36;
let m.s1s487.ref   := 4;
let m.s1s488.sosno := 36;
let m.s1s488.ref   := 5;
let m.s1s489.sosno := 36;
let m.s1s489.ref   := 6;
let m.s1s490.sosno := 36;
let m.s1s490.ref   := 7;
let m.s1s491.sosno := 37;
let m.s1s491.ref   := 1;
let m.s1s492.sosno := 37;
let m.s1s492.ref   := 2;
let m.s1s493.sosno := 37;
let m.s1s493.ref   := 3;
let m.s1s494.sosno := 37;
let m.s1s494.ref   := 4;
let m.s1s495.sosno := 37;
let m.s1s495.ref   := 5;
let m.s1s496.sosno := 37;
let m.s1s496.ref   := 6;
let m.s1s497.sosno := 37;
let m.s1s497.ref   := 7;
let m.s1s498.sosno := 38;
let m.s1s498.ref   := 1;
let m.s1s499.sosno := 38;
let m.s1s499.ref   := 2;
let m.s1s500.sosno := 38;
let m.s1s500.ref   := 3;
let m.s1s501.sosno := 38;
let m.s1s501.ref   := 4;
let m.s1s502.sosno := 38;
let m.s1s502.ref   := 5;
let m.s1s503.sosno := 38;
let m.s1s503.ref   := 6;
let m.s1s504.sosno := 38;
let m.s1s504.ref   := 7;
let m.s1s505.sosno := 39;
let m.s1s505.ref   := 1;
let m.s1s506.sosno := 39;
let m.s1s506.ref   := 2;
let m.s1s507.sosno := 39;
let m.s1s507.ref   := 3;
let m.s1s508.sosno := 39;
let m.s1s508.ref   := 4;
let m.s1s509.sosno := 39;
let m.s1s509.ref   := 5;
let m.s1s510.sosno := 39;
let m.s1s510.ref   := 6;
let m.s1s511.sosno := 39;
let m.s1s511.ref   := 7;
let m.s1s512.sosno := 40;
let m.s1s512.ref   := 1;
let m.s1s513.sosno := 40;
let m.s1s513.ref   := 2;
let m.s1s514.sosno := 40;
let m.s1s514.ref   := 3;
let m.s1s515.sosno := 40;
let m.s1s515.ref   := 4;
let m.s1s516.sosno := 40;
let m.s1s516.ref   := 5;
let m.s1s517.sosno := 40;
let m.s1s517.ref   := 6;
let m.s1s518.sosno := 40;
let m.s1s518.ref   := 7;
let m.s1s519.sosno := 41;
let m.s1s519.ref   := 1;
let m.s1s520.sosno := 41;
let m.s1s520.ref   := 2;
let m.s1s521.sosno := 41;
let m.s1s521.ref   := 3;
let m.s1s522.sosno := 41;
let m.s1s522.ref   := 4;
let m.s1s523.sosno := 41;
let m.s1s523.ref   := 5;
let m.s1s524.sosno := 41;
let m.s1s524.ref   := 6;
let m.s1s525.sosno := 41;
let m.s1s525.ref   := 7;
let m.s1s526.sosno := 42;
let m.s1s526.ref   := 1;
let m.s1s527.sosno := 42;
let m.s1s527.ref   := 2;
let m.s1s528.sosno := 42;
let m.s1s528.ref   := 3;
let m.s1s529.sosno := 42;
let m.s1s529.ref   := 4;
let m.s1s530.sosno := 42;
let m.s1s530.ref   := 5;
let m.s1s531.sosno := 42;
let m.s1s531.ref   := 6;
let m.s1s532.sosno := 42;
let m.s1s532.ref   := 7;
let m.s1s533.sosno := 43;
let m.s1s533.ref   := 1;
let m.s1s534.sosno := 43;
let m.s1s534.ref   := 2;
let m.s1s535.sosno := 43;
let m.s1s535.ref   := 3;
let m.s1s536.sosno := 43;
let m.s1s536.ref   := 4;
let m.s1s537.sosno := 43;
let m.s1s537.ref   := 5;
let m.s1s538.sosno := 43;
let m.s1s538.ref   := 6;
let m.s1s539.sosno := 43;
let m.s1s539.ref   := 7;
let m.s1s540.sosno := 44;
let m.s1s540.ref   := 1;
let m.s1s541.sosno := 44;
let m.s1s541.ref   := 2;
let m.s1s542.sosno := 44;
let m.s1s542.ref   := 3;
let m.s1s543.sosno := 44;
let m.s1s543.ref   := 4;
let m.s1s544.sosno := 44;
let m.s1s544.ref   := 5;
let m.s1s545.sosno := 44;
let m.s1s545.ref   := 6;
let m.s1s546.sosno := 44;
let m.s1s546.ref   := 7;
let m.s1s547.sosno := 45;
let m.s1s547.ref   := 1;
let m.s1s548.sosno := 45;
let m.s1s548.ref   := 2;
let m.s1s549.sosno := 45;
let m.s1s549.ref   := 3;
let m.s1s550.sosno := 45;
let m.s1s550.ref   := 4;
let m.s1s551.sosno := 45;
let m.s1s551.ref   := 5;
let m.s1s552.sosno := 45;
let m.s1s552.ref   := 6;
let m.s1s553.sosno := 45;
let m.s1s553.ref   := 7;
let m.s1s554.sosno := 46;
let m.s1s554.ref   := 1;
let m.s1s555.sosno := 46;
let m.s1s555.ref   := 2;
let m.s1s556.sosno := 46;
let m.s1s556.ref   := 3;
let m.s1s557.sosno := 46;
let m.s1s557.ref   := 4;
let m.s1s558.sosno := 46;
let m.s1s558.ref   := 5;
let m.s1s559.sosno := 46;
let m.s1s559.ref   := 6;
let m.s1s560.sosno := 46;
let m.s1s560.ref   := 7;
let m.s1s561.sosno := 47;
let m.s1s561.ref   := 1;
let m.s1s562.sosno := 47;
let m.s1s562.ref   := 2;
let m.s1s563.sosno := 47;
let m.s1s563.ref   := 3;
let m.s1s564.sosno := 47;
let m.s1s564.ref   := 4;
let m.s1s565.sosno := 47;
let m.s1s565.ref   := 5;
let m.s1s566.sosno := 47;
let m.s1s566.ref   := 6;
let m.s1s567.sosno := 47;
let m.s1s567.ref   := 7;
let m.s1s568.sosno := 48;
let m.s1s568.ref   := 1;
let m.s1s569.sosno := 48;
let m.s1s569.ref   := 2;
let m.s1s570.sosno := 48;
let m.s1s570.ref   := 3;
let m.s1s571.sosno := 48;
let m.s1s571.ref   := 4;
let m.s1s572.sosno := 48;
let m.s1s572.ref   := 5;
let m.s1s573.sosno := 48;
let m.s1s573.ref   := 6;
let m.s1s574.sosno := 48;
let m.s1s574.ref   := 7;
let m.s1s575.sosno := 49;
let m.s1s575.ref   := 1;
let m.s1s576.sosno := 49;
let m.s1s576.ref   := 2;
let m.s1s577.sosno := 49;
let m.s1s577.ref   := 3;
let m.s1s578.sosno := 49;
let m.s1s578.ref   := 4;
let m.s1s579.sosno := 49;
let m.s1s579.ref   := 5;
let m.s1s580.sosno := 49;
let m.s1s580.ref   := 6;
let m.s1s581.sosno := 49;
let m.s1s581.ref   := 7;
let m.s1s582.sosno := 50;
let m.s1s582.ref   := 1;
let m.s1s583.sosno := 50;
let m.s1s583.ref   := 2;
let m.s1s584.sosno := 50;
let m.s1s584.ref   := 3;
let m.s1s585.sosno := 50;
let m.s1s585.ref   := 4;
let m.s1s586.sosno := 50;
let m.s1s586.ref   := 5;
let m.s1s587.sosno := 50;
let m.s1s587.ref   := 6;
let m.s1s588.sosno := 50;
let m.s1s588.ref   := 7;
let m.s1s589.sosno := 51;
let m.s1s589.ref   := 1;
let m.s1s590.sosno := 51;
let m.s1s590.ref   := 2;
let m.s1s591.sosno := 51;
let m.s1s591.ref   := 3;
let m.s1s592.sosno := 51;
let m.s1s592.ref   := 4;
let m.s1s593.sosno := 51;
let m.s1s593.ref   := 5;
let m.s1s594.sosno := 51;
let m.s1s594.ref   := 6;
let m.s1s595.sosno := 51;
let m.s1s595.ref   := 7;
let m.s1s596.sosno := 52;
let m.s1s596.ref   := 1;
let m.s1s597.sosno := 52;
let m.s1s597.ref   := 2;
let m.s1s598.sosno := 52;
let m.s1s598.ref   := 3;
let m.s1s599.sosno := 52;
let m.s1s599.ref   := 4;
let m.s1s600.sosno := 52;
let m.s1s600.ref   := 5;
let m.s1s601.sosno := 52;
let m.s1s601.ref   := 6;
let m.s1s602.sosno := 52;
let m.s1s602.ref   := 7;
let m.s1s603.sosno := 53;
let m.s1s603.ref   := 1;
let m.s1s604.sosno := 53;
let m.s1s604.ref   := 2;
let m.s1s605.sosno := 53;
let m.s1s605.ref   := 3;
let m.s1s606.sosno := 53;
let m.s1s606.ref   := 4;
let m.s1s607.sosno := 53;
let m.s1s607.ref   := 5;
let m.s1s608.sosno := 53;
let m.s1s608.ref   := 6;
let m.s1s609.sosno := 53;
let m.s1s609.ref   := 7;
let m.s1s610.sosno := 54;
let m.s1s610.ref   := 1;
let m.s1s611.sosno := 54;
let m.s1s611.ref   := 2;
let m.s1s612.sosno := 54;
let m.s1s612.ref   := 3;
let m.s1s613.sosno := 54;
let m.s1s613.ref   := 4;
let m.s1s614.sosno := 54;
let m.s1s614.ref   := 5;
let m.s1s615.sosno := 54;
let m.s1s615.ref   := 6;
let m.s1s616.sosno := 54;
let m.s1s616.ref   := 7;
let m.s1s617.sosno := 55;
let m.s1s617.ref   := 1;
let m.s1s618.sosno := 55;
let m.s1s618.ref   := 2;
let m.s1s619.sosno := 55;
let m.s1s619.ref   := 3;
let m.s1s620.sosno := 55;
let m.s1s620.ref   := 4;
let m.s1s621.sosno := 55;
let m.s1s621.ref   := 5;
let m.s1s622.sosno := 55;
let m.s1s622.ref   := 6;
let m.s1s623.sosno := 55;
let m.s1s623.ref   := 7;
let m.s1s624.sosno := 56;
let m.s1s624.ref   := 1;
let m.s1s625.sosno := 56;
let m.s1s625.ref   := 2;
let m.s1s626.sosno := 56;
let m.s1s626.ref   := 3;
let m.s1s627.sosno := 56;
let m.s1s627.ref   := 4;
let m.s1s628.sosno := 56;
let m.s1s628.ref   := 5;
let m.s1s629.sosno := 56;
let m.s1s629.ref   := 6;
let m.s1s630.sosno := 56;
let m.s1s630.ref   := 7;

m.obj = Objective(expr=   10*m.x179 + m.x180 + 10*m.x181, sense=minimize)

m.c1 = Constraint(expr= - m.x1 - m.x2 - m.x3 - m.x4 - m.x5 - m.x6 - m.x7 + m.x8 + m.x15 + m.x22 + m.x29 + m.x36 + m.x43
                        + m.x50 + m.x177 == 0)

m.c2 = Constraint(expr=   m.x1 - m.x8 - m.x9 - m.x10 - m.x11 - m.x12 - m.x13 - m.x14 + m.x16 + m.x23 + m.x30 + m.x37
                        + m.x44 + m.x51 + m.x178 == 0)

m.c3 = Constraint(expr=   m.x2 + m.x9 - m.x15 - m.x16 - m.x17 - m.x18 - m.x19 - m.x20 - m.x21 + m.x24 + m.x31 + m.x38
                        + m.x45 + m.x52 == 1.212)

m.c4 = Constraint(expr=   m.x3 + m.x10 + m.x17 - m.x22 - m.x23 - m.x24 - m.x25 - m.x26 - m.x27 - m.x28 + m.x32 + m.x39
                        + m.x46 + m.x53 == 0.452)

m.c5 = Constraint(expr=   m.x4 + m.x11 + m.x18 + m.x25 - m.x29 - m.x30 - m.x31 - m.x32 - m.x33 - m.x34 - m.x35 + m.x40
                        + m.x47 + m.x54 == 0.245)

m.c6 = Constraint(expr=   m.x5 + m.x12 + m.x19 + m.x26 + m.x33 - m.x36 - m.x37 - m.x38 - m.x39 - m.x40 - m.x41 - m.x42
                        + m.x48 + m.x55 == 0.652)

m.c7 = Constraint(expr=   m.x6 + m.x13 + m.x20 + m.x27 + m.x34 + m.x41 - m.x43 - m.x44 - m.x45 - m.x46 - m.x47 - m.x48
                        - m.x49 + m.x56 == 0.252)

m.c8 = Constraint(expr=   m.x7 + m.x14 + m.x21 + m.x28 + m.x35 + m.x42 + m.x49 - m.x50 - m.x51 - m.x52 - m.x53 - m.x54
                        - m.x55 - m.x56 == 0.456)

m.c9 = Constraint(expr=   m.x57 - 79411.582707283*m.s1s239 - 5217.11027198889*m.s1s240 - 426.059750561967*m.s1s241
                        - 49.0799484616014*m.s1s242 - 3.2244100235547*m.s1s243 - 0.37143587857431*m.s1s244
                        - 0.0801604941350881*m.s1s245 == 0)

m.c10 = Constraint(expr=   m.x58 - 38721.1970117411*m.s1s246 - 2543.8701482414*m.s1s247 - 207.747320703761*m.s1s248
                         - 23.9314504121258*m.s1s249 - 1.5722267648148*m.s1s250 - 0.181112645550961*m.s1s251
                         - 0.0390863672545667*m.s1s252 == 0)

m.c11 = Constraint(expr=   m.x59 - 32510.4890865135*m.s1s253 - 2135.84468132099*m.s1s254 - 174.425573683688*m.s1s255
                         - 20.0929521164322*m.s1s256 - 1.32004857865156*m.s1s257 - 0.152062982061963*m.s1s258
                         - 0.0328170876451919*m.s1s259 == 0)

m.c12 = Constraint(expr=   m.x60 - 61354.8285678982*m.s1s260 - 4030.83398472982*m.s1s261 - 329.181487941979*m.s1s262
                         - 37.9200580233072*m.s1s263 - 2.49123764422425*m.s1s264 - 0.286978094088577*m.s1s265
                         - 0.0619334511151265*m.s1s266 == 0)

m.c13 = Constraint(expr=   m.x61 - 69005.9713947913*m.s1s267 - 4533.49183984114*m.s1s268 - 370.231469483791*m.s1s269
                         - 42.6488102130281*m.s1s270 - 2.8019029247995*m.s1s271 - 0.32276517780003*m.s1s272
                         - 0.0696567500193006*m.s1s273 == 0)

m.c14 = Constraint(expr=   m.x62 - 98671.1700093743*m.s1s274 - 6482.40920348584*m.s1s275 - 529.391464678563*m.s1s276
                         - 60.9832441768203*m.s1s277 - 4.00642196978801*m.s1s278 - 0.461519736453078*m.s1s279
                         - 0.0996017139463627*m.s1s280 == 0)

m.c15 = Constraint(expr=   m.x63 - 63468.4628982673*m.s1s281 - 4169.69361956223*m.s1s282 - 340.521578201805*m.s1s283
                         - 39.2263796008983*m.s1s284 - 2.57705917665854*m.s1s285 - 0.296864304610023*m.s1s286
                         - 0.0640670186196026*m.s1s287 == 0)

m.c16 = Constraint(expr=   m.x64 - 79411.582707283*m.s1s288 - 5217.11027198889*m.s1s289 - 426.059750561967*m.s1s290
                         - 49.0799484616014*m.s1s291 - 3.2244100235547*m.s1s292 - 0.37143587857431*m.s1s293
                         - 0.0801604941350881*m.s1s294 == 0)

m.c17 = Constraint(expr=   m.x65 - 50797.5773435889*m.s1s295 - 3337.25325093014*m.s1s296 - 272.539627020641*m.s1s297
                         - 31.3951994533022*m.s1s298 - 2.06257339263358*m.s1s299 - 0.237598120158509*m.s1s300
                         - 0.0512766370081929*m.s1s301 == 0)

m.c18 = Constraint(expr=   m.x66 - 82599.0313850111*m.s1s302 - 5426.51638972501*m.s1s303 - 443.161079389119*m.s1s304
                         - 51.0499358550468*m.s1s305 - 3.35383247196398*m.s1s306 - 0.386344696150538*m.s1s307
                         - 0.0833780028702903*m.s1s308 == 0)

m.c19 = Constraint(expr=   m.x67 - 82628.2406856418*m.s1s309 - 5428.43535591562*m.s1s310 - 443.317793396277*m.s1s311
                         - 51.0679885234445*m.s1s312 - 3.35501847982988*m.s1s313 - 0.386481318314113*m.s1s314
                         - 0.0834074876367699*m.s1s315 == 0)

m.c20 = Constraint(expr=   m.x68 - 59165.7349698592*m.s1s316 - 3887.01689524085*m.s1s317 - 317.436542928413*m.s1s318
                         - 36.5670992066393*m.s1s319 - 2.40235218067626*m.s1s320 - 0.27673893405488*m.s1s321
                         - 0.0597237127048799*m.s1s322 == 0)

m.c21 = Constraint(expr=   m.x69 - 32977.2294678044*m.s1s323 - 2166.50816836621*m.s1s324 - 176.929733450444*m.s1s325
                         - 20.3814187742893*m.s1s326 - 1.339*m.s1s327 - 0.154246090843839*m.s1s328
                         - 0.0332882297421199*m.s1s329 == 0)

m.c22 = Constraint(expr=   m.x70 - 33843.9321019273*m.s1s330 - 2223.4480134252*m.s1s331 - 181.579774357788*m.s1s332
                         - 20.9170801874496*m.s1s333 - 1.37419139860501*m.s1s334 - 0.158299963634093*m.s1s335
                         - 0.0341631060391402*m.s1s336 == 0)

m.c23 = Constraint(expr=   m.x71 - 38721.1970117411*m.s1s337 - 2543.8701482414*m.s1s338 - 207.747320703761*m.s1s339
                         - 23.9314504121258*m.s1s340 - 1.5722267648148*m.s1s341 - 0.181112645550961*m.s1s342
                         - 0.0390863672545667*m.s1s343 == 0)

m.c24 = Constraint(expr=   m.x72 - 50797.5773435889*m.s1s344 - 3337.25325093014*m.s1s345 - 272.539627020641*m.s1s346
                         - 31.3951994533022*m.s1s347 - 2.06257339263358*m.s1s348 - 0.237598120158509*m.s1s349
                         - 0.0512766370081929*m.s1s350 == 0)

m.c25 = Constraint(expr=   m.x73 - 31810.181054648*m.s1s351 - 2089.8364782095*m.s1s352 - 170.668274619734*m.s1s353
                         - 19.660130090483*m.s1s354 - 1.2916134290104*m.s1s355 - 0.148787395299671*m.s1s356
                         - 0.0321101751776739*m.s1s357 == 0)

m.c26 = Constraint(expr=   m.x74 - 39461.9459070343*m.s1s358 - 2592.53519858857*m.s1s359 - 211.721593458417*m.s1s360
                         - 24.3892667200816*m.s1s361 - 1.60230396616872*m.s1s362 - 0.184577388442944*m.s1s363
                         - 0.0398341019735132*m.s1s364 == 0)

m.c27 = Constraint(expr=   m.x75 - 32977.2294678044*m.s1s365 - 2166.50816836621*m.s1s366 - 176.929733450444*m.s1s367
                         - 20.3814187742893*m.s1s368 - 1.339*m.s1s369 - 0.154246090843839*m.s1s370
                         - 0.0332882297421199*m.s1s371 == 0)

m.c28 = Constraint(expr=   m.x76 - 61928.9823925488*m.s1s372 - 4068.554222939*m.s1s373 - 332.261943298429*m.s1s374
                         - 38.2749110455263*m.s1s375 - 2.51455045684114*m.s1s376 - 0.289663613291512*m.s1s377
                         - 0.0625130196456165*m.s1s378 == 0)

m.c29 = Constraint(expr=   m.x77 - 52785.5148814787*m.s1s379 - 3467.85497167945*m.s1s380 - 283.205327698691*m.s1s381
                         - 32.6238347301504*m.s1s382 - 2.14329116080854*m.s1s383 - 0.246896402610059*m.s1s384
                         - 0.0532833223041444*m.s1s385 == 0)

m.c30 = Constraint(expr=   m.x78 - 32510.4890865135*m.s1s386 - 2135.84468132099*m.s1s387 - 174.425573683688*m.s1s388
                         - 20.0929521164322*m.s1s389 - 1.32004857865156*m.s1s390 - 0.152062982061963*m.s1s391
                         - 0.0328170876451919*m.s1s392 == 0)

m.c31 = Constraint(expr=   m.x79 - 82599.0313850111*m.s1s393 - 5426.51638972501*m.s1s394 - 443.161079389119*m.s1s395
                         - 51.0499358550468*m.s1s396 - 3.35383247196398*m.s1s397 - 0.386344696150538*m.s1s398
                         - 0.0833780028702903*m.s1s399 == 0)

m.c32 = Constraint(expr=   m.x80 - 31810.181054648*m.s1s400 - 2089.8364782095*m.s1s401 - 170.668274619734*m.s1s402
                         - 19.660130090483*m.s1s403 - 1.2916134290104*m.s1s404 - 0.148787395299671*m.s1s405
                         - 0.0321101751776739*m.s1s406 == 0)

m.c33 = Constraint(expr=   m.x81 - 30677.4142839491*m.s1s407 - 2015.41699236491*m.s1s408 - 164.590743970989*m.s1s409
                         - 18.9600290116536*m.s1s410 - 1.24561882211213*m.s1s411 - 0.143489047044288*m.s1s412
                         - 0.0309667255575633*m.s1s413 == 0)

m.c34 = Constraint(expr=   m.x82 - 47609.7953674264*m.s1s414 - 3127.8252364552*m.s1s415 - 255.436509977676*m.s1s416
                         - 29.4250060663552*m.s1s417 - 1.93313741104972*m.s1s418 - 0.222687743628377*m.s1s419
                         - 0.0480587918312993*m.s1s420 == 0)

m.c35 = Constraint(expr=   m.x83 - 90800.3982081977*m.s1s421 - 5965.32236284499*m.s1s422 - 487.1631277532*m.s1s423
                         - 56.1187513511491*m.s1s424 - 3.68683892379366*m.s1s425 - 0.424705370848452*m.s1s426
                         - 0.0916567148001743*m.s1s427 == 0)

m.c36 = Constraint(expr=   m.x84 - 79866.0883229559*m.s1s428 - 5246.96997047827*m.s1s429 - 428.498268252218*m.s1s430
                         - 49.3608534811495*m.s1s431 - 3.24286466723482*m.s1s432 - 0.373561761057936*m.s1s433
                         - 0.0806192860832829*m.s1s434 == 0)

m.c37 = Constraint(expr=   m.x85 - 61354.8285678982*m.s1s435 - 4030.83398472982*m.s1s436 - 329.181487941979*m.s1s437
                         - 37.9200580233072*m.s1s438 - 2.49123764422425*m.s1s439 - 0.286978094088577*m.s1s440
                         - 0.0619334511151265*m.s1s441 == 0)

m.c38 = Constraint(expr=   m.x86 - 82628.2406856418*m.s1s442 - 5428.43535591562*m.s1s443 - 443.317793396277*m.s1s444
                         - 51.0679885234445*m.s1s445 - 3.35501847982988*m.s1s446 - 0.386481318314113*m.s1s447
                         - 0.0834074876367699*m.s1s448 == 0)

m.c39 = Constraint(expr=   m.x87 - 39461.9459070343*m.s1s449 - 2592.53519858857*m.s1s450 - 211.721593458417*m.s1s451
                         - 24.3892667200816*m.s1s452 - 1.60230396616872*m.s1s453 - 0.184577388442944*m.s1s454
                         - 0.0398341019735132*m.s1s455 == 0)

m.c40 = Constraint(expr=   m.x88 - 30677.4142839491*m.s1s456 - 2015.41699236491*m.s1s457 - 164.590743970989*m.s1s458
                         - 18.9600290116536*m.s1s459 - 1.24561882211213*m.s1s460 - 0.143489047044288*m.s1s461
                         - 0.0309667255575633*m.s1s462 == 0)

m.c41 = Constraint(expr=   m.x89 - 28361.2795383154*m.s1s463 - 1863.25366856746*m.s1s464 - 152.164196629274*m.s1s465
                         - 17.5285530220005*m.s1s466 - 1.15157500841239*m.s1s467 - 0.132655670919396*m.s1s468
                         - 0.0286287479053886*m.s1s469 == 0)

m.c42 = Constraint(expr=   m.x90 - 79005.3826894827*m.s1s470 - 5190.42411093907*m.s1s471 - 423.880402507663*m.s1s472
                         - 48.8288984855264*m.s1s473 - 3.20791676949387*m.s1s474 - 0.369535938347143*m.s1s475
                         - 0.0797504633431748*m.s1s476 == 0)

m.c43 = Constraint(expr=   m.x91 - 91918.5525763874*m.s1s477 - 6038.78185629766*m.s1s478 - 493.162259806225*m.s1s479
                         - 56.8098213045733*m.s1s480 - 3.73224021199065*m.s1s481 - 0.429935371762313*m.s1s482
                         - 0.0927854142117423*m.s1s483 == 0)

m.c44 = Constraint(expr=   m.x92 - 69005.9713947913*m.s1s484 - 4533.49183984114*m.s1s485 - 370.231469483791*m.s1s486
                         - 42.6488102130281*m.s1s487 - 2.8019029247995*m.s1s488 - 0.32276517780003*m.s1s489
                         - 0.0696567500193006*m.s1s490 == 0)

m.c45 = Constraint(expr=   m.x93 - 59165.7349698592*m.s1s491 - 3887.01689524085*m.s1s492 - 317.436542928413*m.s1s493
                         - 36.5670992066393*m.s1s494 - 2.40235218067626*m.s1s495 - 0.27673893405488*m.s1s496
                         - 0.0597237127048799*m.s1s497 == 0)

m.c46 = Constraint(expr=   m.x94 - 32977.2294678044*m.s1s498 - 2166.50816836621*m.s1s499 - 176.929733450444*m.s1s500
                         - 20.3814187742893*m.s1s501 - 1.339*m.s1s502 - 0.154246090843839*m.s1s503
                         - 0.0332882297421199*m.s1s504 == 0)

m.c47 = Constraint(expr=   m.x95 - 47609.7953674264*m.s1s505 - 3127.8252364552*m.s1s506 - 255.436509977676*m.s1s507
                         - 29.4250060663552*m.s1s508 - 1.93313741104972*m.s1s509 - 0.222687743628377*m.s1s510
                         - 0.0480587918312993*m.s1s511 == 0)

m.c48 = Constraint(expr=   m.x96 - 28361.2795383154*m.s1s512 - 1863.25366856746*m.s1s513 - 152.164196629274*m.s1s514
                         - 17.5285530220005*m.s1s515 - 1.15157500841239*m.s1s516 - 0.132655670919396*m.s1s517
                         - 0.0286287479053886*m.s1s518 == 0)

m.c49 = Constraint(expr=   m.x97 - 50797.5773435889*m.s1s519 - 3337.25325093014*m.s1s520 - 272.539627020641*m.s1s521
                         - 31.3951994533022*m.s1s522 - 2.06257339263358*m.s1s523 - 0.237598120158509*m.s1s524
                         - 0.0512766370081929*m.s1s525 == 0)

m.c50 = Constraint(expr=   m.x98 - 76690.9136638299*m.s1s526 - 5038.370220105*m.s1s527 - 411.462792102039*m.s1s528
                         - 47.3984519861318*m.s1s529 - 3.11394059031318*m.s1s530 - 0.358710353379957*m.s1s531
                         - 0.0774141671199832*m.s1s532 == 0)

m.c51 = Constraint(expr=   m.x99 - 98671.1700093743*m.s1s533 - 6482.40920348584*m.s1s534 - 529.391464678563*m.s1s535
                         - 60.9832441768203*m.s1s536 - 4.00642196978801*m.s1s537 - 0.461519736453078*m.s1s538
                         - 0.0996017139463627*m.s1s539 == 0)

m.c52 = Constraint(expr=   m.x100 - 32977.2294678044*m.s1s540 - 2166.50816836621*m.s1s541 - 176.929733450444*m.s1s542
                         - 20.3814187742893*m.s1s543 - 1.339*m.s1s544 - 0.154246090843839*m.s1s545
                         - 0.0332882297421199*m.s1s546 == 0)

m.c53 = Constraint(expr=   m.x101 - 61928.9823925488*m.s1s547 - 4068.554222939*m.s1s548 - 332.261943298429*m.s1s549
                         - 38.2749110455263*m.s1s550 - 2.51455045684114*m.s1s551 - 0.289663613291512*m.s1s552
                         - 0.0625130196456165*m.s1s553 == 0)

m.c54 = Constraint(expr=   m.x102 - 90800.3982081977*m.s1s554 - 5965.32236284499*m.s1s555 - 487.1631277532*m.s1s556
                         - 56.1187513511491*m.s1s557 - 3.68683892379366*m.s1s558 - 0.424705370848452*m.s1s559
                         - 0.0916567148001743*m.s1s560 == 0)

m.c55 = Constraint(expr=   m.x103 - 79005.3826894827*m.s1s561 - 5190.42411093907*m.s1s562 - 423.880402507663*m.s1s563
                         - 48.8288984855264*m.s1s564 - 3.20791676949387*m.s1s565 - 0.369535938347143*m.s1s566
                         - 0.0797504633431748*m.s1s567 == 0)

m.c56 = Constraint(expr=   m.x104 - 50797.5773435889*m.s1s568 - 3337.25325093014*m.s1s569 - 272.539627020641*m.s1s570
                         - 31.3951994533022*m.s1s571 - 2.06257339263358*m.s1s572 - 0.237598120158509*m.s1s573
                         - 0.0512766370081929*m.s1s574 == 0)

m.c57 = Constraint(expr=   m.x105 - 66392.0532160028*m.s1s575 - 4361.76500962592*m.s1s576 - 356.207251740277*m.s1s577
                         - 41.0332905983307*m.s1s578 - 2.69576797963029*m.s1s579 - 0.310538963913342*m.s1s580
                         - 0.0670181806104433*m.s1s581 == 0)

m.c58 = Constraint(expr=   m.x106 - 63468.4628982673*m.s1s582 - 4169.69361956223*m.s1s583 - 340.521578201805*m.s1s584
                         - 39.2263796008983*m.s1s585 - 2.57705917665854*m.s1s586 - 0.296864304610023*m.s1s587
                         - 0.0640670186196026*m.s1s588 == 0)

m.c59 = Constraint(expr=   m.x107 - 33843.9321019273*m.s1s589 - 2223.4480134252*m.s1s590 - 181.579774357788*m.s1s591
                         - 20.9170801874496*m.s1s592 - 1.37419139860501*m.s1s593 - 0.158299963634093*m.s1s594
                         - 0.0341631060391402*m.s1s595 == 0)

m.c60 = Constraint(expr=   m.x108 - 52785.5148814787*m.s1s596 - 3467.85497167945*m.s1s597 - 283.205327698691*m.s1s598
                         - 32.6238347301504*m.s1s599 - 2.14329116080854*m.s1s600 - 0.246896402610059*m.s1s601
                         - 0.0532833223041444*m.s1s602 == 0)

m.c61 = Constraint(expr=   m.x109 - 79866.0883229559*m.s1s603 - 5246.96997047827*m.s1s604 - 428.498268252218*m.s1s605
                         - 49.3608534811495*m.s1s606 - 3.24286466723482*m.s1s607 - 0.373561761057936*m.s1s608
                         - 0.0806192860832829*m.s1s609 == 0)

m.c62 = Constraint(expr=   m.x110 - 91918.5525763874*m.s1s610 - 6038.78185629766*m.s1s611 - 493.162259806225*m.s1s612
                         - 56.8098213045733*m.s1s613 - 3.73224021199065*m.s1s614 - 0.429935371762313*m.s1s615
                         - 0.0927854142117423*m.s1s616 == 0)

m.c63 = Constraint(expr=   m.x111 - 76690.9136638299*m.s1s617 - 5038.370220105*m.s1s618 - 411.462792102039*m.s1s619
                         - 47.3984519861318*m.s1s620 - 3.11394059031318*m.s1s621 - 0.358710353379957*m.s1s622
                         - 0.0774141671199832*m.s1s623 == 0)

m.c64 = Constraint(expr=   m.x112 - 66392.0532160028*m.s1s624 - 4361.76500962592*m.s1s625 - 356.207251740277*m.s1s626
                         - 41.0332905983307*m.s1s627 - 2.69576797963029*m.s1s628 - 0.310538963913342*m.s1s629
                         - 0.0670181806104433*m.s1s630 == 0)

m.c65 = Constraint(expr=-m.x1**2*m.x57 + m.x113 - m.x114 - m.x121 == 0)

m.c66 = Constraint(expr=-m.x2**2*m.x58 + m.x113 - m.x115 - m.x122 == 0)

m.c67 = Constraint(expr=-m.x3**2*m.x59 + m.x113 - m.x116 - m.x123 == 0)

m.c68 = Constraint(expr=-m.x4**2*m.x60 + m.x113 - m.x117 - m.x124 == 0)

m.c69 = Constraint(expr=-m.x5**2*m.x61 + m.x113 - m.x118 - m.x125 == 0)

m.c70 = Constraint(expr=-m.x6**2*m.x62 + m.x113 - m.x119 - m.x126 == 0)

m.c71 = Constraint(expr=-m.x7**2*m.x63 + m.x113 - m.x120 - m.x127 == 0)

m.c72 = Constraint(expr=-m.x8**2*m.x64 - m.x113 + m.x114 - m.x128 == 0)

m.c73 = Constraint(expr=-m.x9**2*m.x65 + m.x114 - m.x115 - m.x129 == 0)

m.c74 = Constraint(expr=-m.x10**2*m.x66 + m.x114 - m.x116 - m.x130 == 0)

m.c75 = Constraint(expr=-m.x11**2*m.x67 + m.x114 - m.x117 - m.x131 == 0)

m.c76 = Constraint(expr=-m.x12**2*m.x68 + m.x114 - m.x118 - m.x132 == 0)

m.c77 = Constraint(expr=-m.x13**2*m.x69 + m.x114 - m.x119 - m.x133 == 0)

m.c78 = Constraint(expr=-m.x14**2*m.x70 + m.x114 - m.x120 - m.x134 == 0)

m.c79 = Constraint(expr=-m.x15**2*m.x71 - m.x113 + m.x115 - m.x135 == 0)

m.c80 = Constraint(expr=-m.x16**2*m.x72 - m.x114 + m.x115 - m.x136 == 0)

m.c81 = Constraint(expr=-m.x17**2*m.x73 + m.x115 - m.x116 - m.x137 == 0)

m.c82 = Constraint(expr=-m.x18**2*m.x74 + m.x115 - m.x117 - m.x138 == 0)

m.c83 = Constraint(expr=-m.x19**2*m.x75 + m.x115 - m.x118 - m.x139 == 0)

m.c84 = Constraint(expr=-m.x20**2*m.x76 + m.x115 - m.x119 - m.x140 == 0)

m.c85 = Constraint(expr=-m.x21**2*m.x77 + m.x115 - m.x120 - m.x141 == 0)

m.c86 = Constraint(expr=-m.x22**2*m.x78 - m.x113 + m.x116 - m.x142 == 0)

m.c87 = Constraint(expr=-m.x23**2*m.x79 - m.x114 + m.x116 - m.x143 == 0)

m.c88 = Constraint(expr=-m.x24**2*m.x80 - m.x115 + m.x116 - m.x144 == 0)

m.c89 = Constraint(expr=-m.x25**2*m.x81 + m.x116 - m.x117 - m.x145 == 0)

m.c90 = Constraint(expr=-m.x26**2*m.x82 + m.x116 - m.x118 - m.x146 == 0)

m.c91 = Constraint(expr=-m.x27**2*m.x83 + m.x116 - m.x119 - m.x147 == 0)

m.c92 = Constraint(expr=-m.x28**2*m.x84 + m.x116 - m.x120 - m.x148 == 0)

m.c93 = Constraint(expr=-m.x29**2*m.x85 - m.x113 + m.x117 - m.x149 == 0)

m.c94 = Constraint(expr=-m.x30**2*m.x86 - m.x114 + m.x117 - m.x150 == 0)

m.c95 = Constraint(expr=-m.x31**2*m.x87 - m.x115 + m.x117 - m.x151 == 0)

m.c96 = Constraint(expr=-m.x32**2*m.x88 - m.x116 + m.x117 - m.x152 == 0)

m.c97 = Constraint(expr=-m.x33**2*m.x89 + m.x117 - m.x118 - m.x153 == 0)

m.c98 = Constraint(expr=-m.x34**2*m.x90 + m.x117 - m.x119 - m.x154 == 0)

m.c99 = Constraint(expr=-m.x35**2*m.x91 + m.x117 - m.x120 - m.x155 == 0)

m.c100 = Constraint(expr=-m.x36**2*m.x92 - m.x113 + m.x118 - m.x156 == 0)

m.c101 = Constraint(expr=-m.x37**2*m.x93 - m.x114 + m.x118 - m.x157 == 0)

m.c102 = Constraint(expr=-m.x38**2*m.x94 - m.x115 + m.x118 - m.x158 == 0)

m.c103 = Constraint(expr=-m.x39**2*m.x95 - m.x116 + m.x118 - m.x159 == 0)

m.c104 = Constraint(expr=-m.x40**2*m.x96 - m.x117 + m.x118 - m.x160 == 0)

m.c105 = Constraint(expr=-m.x41**2*m.x97 + m.x118 - m.x119 - m.x161 == 0)

m.c106 = Constraint(expr=-m.x42**2*m.x98 + m.x118 - m.x120 - m.x162 == 0)

m.c107 = Constraint(expr=-m.x43**2*m.x99 - m.x113 + m.x119 - m.x163 == 0)

m.c108 = Constraint(expr=-m.x44**2*m.x100 - m.x114 + m.x119 - m.x164 == 0)

m.c109 = Constraint(expr=-m.x45**2*m.x101 - m.x115 + m.x119 - m.x165 == 0)

m.c110 = Constraint(expr=-m.x46**2*m.x102 - m.x116 + m.x119 - m.x166 == 0)

m.c111 = Constraint(expr=-m.x47**2*m.x103 - m.x117 + m.x119 - m.x167 == 0)

m.c112 = Constraint(expr=-m.x48**2*m.x104 - m.x118 + m.x119 - m.x168 == 0)

m.c113 = Constraint(expr=-m.x49**2*m.x105 + m.x119 - m.x120 - m.x169 == 0)

m.c114 = Constraint(expr=-m.x50**2*m.x106 - m.x113 + m.x120 - m.x170 == 0)

m.c115 = Constraint(expr=-m.x51**2*m.x107 - m.x114 + m.x120 - m.x171 == 0)

m.c116 = Constraint(expr=-m.x52**2*m.x108 - m.x115 + m.x120 - m.x172 == 0)

m.c117 = Constraint(expr=-m.x53**2*m.x109 - m.x116 + m.x120 - m.x173 == 0)

m.c118 = Constraint(expr=-m.x54**2*m.x110 - m.x117 + m.x120 - m.x174 == 0)

m.c119 = Constraint(expr=-m.x55**2*m.x111 - m.x118 + m.x120 - m.x175 == 0)

m.c120 = Constraint(expr=-m.x56**2*m.x112 - m.x119 + m.x120 - m.x176 == 0)

m.c121 = Constraint(expr=   m.x121 + 12*m.b183 <= 12)

m.c122 = Constraint(expr=   m.x122 + 12*m.b184 <= 12)

m.c123 = Constraint(expr=   m.x123 + 12*m.b185 <= 12)

m.c124 = Constraint(expr=   m.x124 + 12*m.b186 <= 12)

m.c125 = Constraint(expr=   m.x125 + 12*m.b187 <= 12)

m.c126 = Constraint(expr=   m.x126 + 12*m.b188 <= 12)

m.c127 = Constraint(expr=   m.x127 + 12*m.b189 <= 12)

m.c128 = Constraint(expr=   m.x128 + 12*m.b190 <= 12)

m.c129 = Constraint(expr=   m.x129 + 12*m.b191 <= 12)

m.c130 = Constraint(expr=   m.x130 + 12*m.b192 <= 12)

m.c131 = Constraint(expr=   m.x131 + 12*m.b193 <= 12)

m.c132 = Constraint(expr=   m.x132 + 12*m.b194 <= 12)

m.c133 = Constraint(expr=   m.x133 + 12*m.b195 <= 12)

m.c134 = Constraint(expr=   m.x134 + 12*m.b196 <= 12)

m.c135 = Constraint(expr=   m.x135 + 12*m.b197 <= 12)

m.c136 = Constraint(expr=   m.x136 + 12*m.b198 <= 12)

m.c137 = Constraint(expr=   m.x137 + 12*m.b199 <= 12)

m.c138 = Constraint(expr=   m.x138 + 12*m.b200 <= 12)

m.c139 = Constraint(expr=   m.x139 + 12*m.b201 <= 12)

m.c140 = Constraint(expr=   m.x140 + 12*m.b202 <= 12)

m.c141 = Constraint(expr=   m.x141 + 12*m.b203 <= 12)

m.c142 = Constraint(expr=   m.x142 + 12*m.b204 <= 12)

m.c143 = Constraint(expr=   m.x143 + 12*m.b205 <= 12)

m.c144 = Constraint(expr=   m.x144 + 12*m.b206 <= 12)

m.c145 = Constraint(expr=   m.x145 + 12*m.b207 <= 12)

m.c146 = Constraint(expr=   m.x146 + 12*m.b208 <= 12)

m.c147 = Constraint(expr=   m.x147 + 12*m.b209 <= 12)

m.c148 = Constraint(expr=   m.x148 + 12*m.b210 <= 12)

m.c149 = Constraint(expr=   m.x149 + 12*m.b211 <= 12)

m.c150 = Constraint(expr=   m.x150 + 12*m.b212 <= 12)

m.c151 = Constraint(expr=   m.x151 + 12*m.b213 <= 12)

m.c152 = Constraint(expr=   m.x152 + 12*m.b214 <= 12)

m.c153 = Constraint(expr=   m.x153 + 12*m.b215 <= 12)

m.c154 = Constraint(expr=   m.x154 + 12*m.b216 <= 12)

m.c155 = Constraint(expr=   m.x155 + 12*m.b217 <= 12)

m.c156 = Constraint(expr=   m.x156 + 12*m.b218 <= 12)

m.c157 = Constraint(expr=   m.x157 + 12*m.b219 <= 12)

m.c158 = Constraint(expr=   m.x158 + 12*m.b220 <= 12)

m.c159 = Constraint(expr=   m.x159 + 12*m.b221 <= 12)

m.c160 = Constraint(expr=   m.x160 + 12*m.b222 <= 12)

m.c161 = Constraint(expr=   m.x161 + 12*m.b223 <= 12)

m.c162 = Constraint(expr=   m.x162 + 12*m.b224 <= 12)

m.c163 = Constraint(expr=   m.x163 + 12*m.b225 <= 12)

m.c164 = Constraint(expr=   m.x164 + 12*m.b226 <= 12)

m.c165 = Constraint(expr=   m.x165 + 12*m.b227 <= 12)

m.c166 = Constraint(expr=   m.x166 + 12*m.b228 <= 12)

m.c167 = Constraint(expr=   m.x167 + 12*m.b229 <= 12)

m.c168 = Constraint(expr=   m.x168 + 12*m.b230 <= 12)

m.c169 = Constraint(expr=   m.x169 + 12*m.b231 <= 12)

m.c170 = Constraint(expr=   m.x170 + 12*m.b232 <= 12)

m.c171 = Constraint(expr=   m.x171 + 12*m.b233 <= 12)

m.c172 = Constraint(expr=   m.x172 + 12*m.b234 <= 12)

m.c173 = Constraint(expr=   m.x173 + 12*m.b235 <= 12)

m.c174 = Constraint(expr=   m.x174 + 12*m.b236 <= 12)

m.c175 = Constraint(expr=   m.x175 + 12*m.b237 <= 12)

m.c176 = Constraint(expr=   m.x176 + 12*m.b238 <= 12)

m.c177 = Constraint(expr=   m.x121 - 12*m.b183 >= -12)

m.c178 = Constraint(expr=   m.x122 - 12*m.b184 >= -12)

m.c179 = Constraint(expr=   m.x123 - 12*m.b185 >= -12)

m.c180 = Constraint(expr=   m.x124 - 12*m.b186 >= -12)

m.c181 = Constraint(expr=   m.x125 - 12*m.b187 >= -12)

m.c182 = Constraint(expr=   m.x126 - 12*m.b188 >= -12)

m.c183 = Constraint(expr=   m.x127 - 12*m.b189 >= -12)

m.c184 = Constraint(expr=   m.x128 - 12*m.b190 >= -12)

m.c185 = Constraint(expr=   m.x129 - 12*m.b191 >= -12)

m.c186 = Constraint(expr=   m.x130 - 12*m.b192 >= -12)

m.c187 = Constraint(expr=   m.x131 - 12*m.b193 >= -12)

m.c188 = Constraint(expr=   m.x132 - 12*m.b194 >= -12)

m.c189 = Constraint(expr=   m.x133 - 12*m.b195 >= -12)

m.c190 = Constraint(expr=   m.x134 - 12*m.b196 >= -12)

m.c191 = Constraint(expr=   m.x135 - 12*m.b197 >= -12)

m.c192 = Constraint(expr=   m.x136 - 12*m.b198 >= -12)

m.c193 = Constraint(expr=   m.x137 - 12*m.b199 >= -12)

m.c194 = Constraint(expr=   m.x138 - 12*m.b200 >= -12)

m.c195 = Constraint(expr=   m.x139 - 12*m.b201 >= -12)

m.c196 = Constraint(expr=   m.x140 - 12*m.b202 >= -12)

m.c197 = Constraint(expr=   m.x141 - 12*m.b203 >= -12)

m.c198 = Constraint(expr=   m.x142 - 12*m.b204 >= -12)

m.c199 = Constraint(expr=   m.x143 - 12*m.b205 >= -12)

m.c200 = Constraint(expr=   m.x144 - 12*m.b206 >= -12)

m.c201 = Constraint(expr=   m.x145 - 12*m.b207 >= -12)

m.c202 = Constraint(expr=   m.x146 - 12*m.b208 >= -12)

m.c203 = Constraint(expr=   m.x147 - 12*m.b209 >= -12)

m.c204 = Constraint(expr=   m.x148 - 12*m.b210 >= -12)

m.c205 = Constraint(expr=   m.x149 - 12*m.b211 >= -12)

m.c206 = Constraint(expr=   m.x150 - 12*m.b212 >= -12)

m.c207 = Constraint(expr=   m.x151 - 12*m.b213 >= -12)

m.c208 = Constraint(expr=   m.x152 - 12*m.b214 >= -12)

m.c209 = Constraint(expr=   m.x153 - 12*m.b215 >= -12)

m.c210 = Constraint(expr=   m.x154 - 12*m.b216 >= -12)

m.c211 = Constraint(expr=   m.x155 - 12*m.b217 >= -12)

m.c212 = Constraint(expr=   m.x156 - 12*m.b218 >= -12)

m.c213 = Constraint(expr=   m.x157 - 12*m.b219 >= -12)

m.c214 = Constraint(expr=   m.x158 - 12*m.b220 >= -12)

m.c215 = Constraint(expr=   m.x159 - 12*m.b221 >= -12)

m.c216 = Constraint(expr=   m.x160 - 12*m.b222 >= -12)

m.c217 = Constraint(expr=   m.x161 - 12*m.b223 >= -12)

m.c218 = Constraint(expr=   m.x162 - 12*m.b224 >= -12)

m.c219 = Constraint(expr=   m.x163 - 12*m.b225 >= -12)

m.c220 = Constraint(expr=   m.x164 - 12*m.b226 >= -12)

m.c221 = Constraint(expr=   m.x165 - 12*m.b227 >= -12)

m.c222 = Constraint(expr=   m.x166 - 12*m.b228 >= -12)

m.c223 = Constraint(expr=   m.x167 - 12*m.b229 >= -12)

m.c224 = Constraint(expr=   m.x168 - 12*m.b230 >= -12)

m.c225 = Constraint(expr=   m.x169 - 12*m.b231 >= -12)

m.c226 = Constraint(expr=   m.x170 - 12*m.b232 >= -12)

m.c227 = Constraint(expr=   m.x171 - 12*m.b233 >= -12)

m.c228 = Constraint(expr=   m.x172 - 12*m.b234 >= -12)

m.c229 = Constraint(expr=   m.x173 - 12*m.b235 >= -12)

m.c230 = Constraint(expr=   m.x174 - 12*m.b236 >= -12)

m.c231 = Constraint(expr=   m.x175 - 12*m.b237 >= -12)

m.c232 = Constraint(expr=   m.x176 - 12*m.b238 >= -12)

m.c233 = Constraint(expr=-(1.02*m.x177*(-6.5 + m.x113) + 1.02*m.x178*(-3.25 + m.x114)) + m.x179 == 0)

m.c234 = Constraint(expr=   m.x180 - 18.6904540877619*m.s1s239 - 36.1247408097722*m.s1s240 - 66.2398770083886*m.s1s241
                          - 111.757644998947*m.s1s242 - 216.00416662648*m.s1s243 - 364.434809700482*m.s1s244
                          - 528.190788533686*m.s1s245 - 9.11349113439539*m.s1s246 - 17.6144733325531*m.s1s247
                          - 32.2986551864818*m.s1s248 - 54.4931814987685*m.s1s249 - 105.323928905069*m.s1s250
                          - 177.698914733437*m.s1s251 - 257.546555368226*m.s1s252 - 7.65172765642961*m.s1s253
                          - 14.7891900880288*m.s1s254 - 27.118094428506*m.s1s255 - 45.7527173518919*m.s1s256
                          - 88.4304387640365*m.s1s257 - 149.196798497086*m.s1s258 - 216.237232413786*m.s1s259
                          - 14.4405836946709*m.s1s260 - 27.9106297076743*m.s1s261 - 51.1781299358943*m.s1s262
                          - 86.3459827433152*m.s1s263 - 166.88873538978*m.s1s264 - 281.568941344082*m.s1s265
                          - 408.089779561278*m.s1s266 - 16.2413705427568*m.s1s267 - 31.3911742592025*m.s1s268
                          - 57.5602059825984*m.s1s269 - 97.1136022105662*m.s1s270 - 187.700293020549*m.s1s271
                          - 316.681486454637*m.s1s272 - 458.979876763054*m.s1s273 - 23.2234254748939*m.s1s274
                          - 44.8860269555956*m.s1s275 - 82.3049477528588*m.s1s276 - 138.862080487498*m.s1s277
                          - 268.391374675119*m.s1s278 - 452.820707501052*m.s1s279 - 656.292209725887*m.s1s280
                          - 14.9380525029139*m.s1s281 - 28.8721329260735*m.s1s282 - 52.941183552398*m.s1s283
                          - 89.3205462402005*m.s1s284 - 172.637944844116*m.s1s285 - 291.268810037089*m.s1s286
                          - 422.148209648796*m.s1s287 - 18.6904540877619*m.s1s288 - 36.1247408097722*m.s1s289
                          - 66.2398770083886*m.s1s290 - 111.757644998947*m.s1s291 - 216.00416662648*m.s1s292
                          - 364.434809700482*m.s1s293 - 528.190788533686*m.s1s294 - 11.9558099050809*m.s1s295
                          - 23.1080813747994*m.s1s296 - 42.3719709499612*m.s1s297 - 71.4885338137291*m.s1s298
                          - 138.172392322055*m.s1s299 - 233.119713791557*m.s1s300 - 337.870264236031*m.s1s301
                          - 19.4406577877407*m.s1s302 - 37.5747277436911*m.s1s303 - 68.8986353555371*m.s1s304
                          - 116.243410747892*m.s1s305 - 224.674214141276*m.s1s306 - 379.062616031703*m.s1s307
                          - 549.391487135874*m.s1s308 - 19.4475325416967*m.s1s309 - 37.5880152060303*m.s1s310
                          - 68.922999817437*m.s1s311 - 116.284517631036*m.s1s312 - 224.753665153652*m.s1s313
                          - 379.196663050462*m.s1s314 - 549.585767151543*m.s1s315 - 13.9253546563734*m.s1s316
                          - 26.9147996770731*m.s1s317 - 49.3521332015331*m.s1s318 - 83.2652237802191*m.s1s319
                          - 160.93427229773*m.s1s320 - 271.522775764452*m.s1s321 - 393.529446744536*m.s1s322
                          - 7.76158051882097*m.s1s323 - 15.0015127080393*m.s1s324 - 27.5074183079396*m.s1s325
                          - 46.4095712271164*m.s1s326 - 89.7*m.s1s327 - 151.338758602103*m.s1s328
                          - 219.341665817957*m.s1s329 - 7.96556922221359*m.s1s330 - 15.3957802311063*m.s1s331
                          - 28.2303641796868*m.s1s332 - 47.6293006671023*m.s1s333 - 92.0574820424717*m.s1s334
                          - 155.316221319321*m.s1s335 - 225.10637081608*m.s1s336 - 9.11349113439539*m.s1s337
                          - 17.6144733325531*m.s1s338 - 32.2986551864818*m.s1s339 - 54.4931814987685*m.s1s340
                          - 105.323928905069*m.s1s341 - 177.698914733437*m.s1s342 - 257.546555368226*m.s1s343
                          - 11.9558099050809*m.s1s344 - 23.1080813747994*m.s1s345 - 42.3719709499612*m.s1s346
                          - 71.4885338137291*m.s1s347 - 138.172392322055*m.s1s348 - 233.119713791557*m.s1s349
                          - 337.870264236031*m.s1s350 - 7.48690188831565*m.s1s351 - 14.4706163324673*m.s1s352
                          - 26.5339439013751*m.s1s353 - 44.7671586494086*m.s1s354 - 86.5255598074927*m.s1s355
                          - 145.982952158506*m.s1s356 - 211.579268940989*m.s1s357 - 9.28783513744935*m.s1s358
                          - 17.9514438466182*m.s1s359 - 32.916538800503*m.s1s360 - 55.5356535066454*m.s1s361
                          - 107.338809384118*m.s1s362 - 181.098351861986*m.s1s363 - 262.473503425068*m.s1s364
                          - 7.76158051882097*m.s1s365 - 15.0015127080393*m.s1s366 - 27.5074183079396*m.s1s367
                          - 46.4095712271164*m.s1s368 - 89.7*m.s1s369 - 151.338758602103*m.s1s370
                          - 219.341665817957*m.s1s371 - 14.5757175798436*m.s1s372 - 28.1718152601258*m.s1s373
                          - 51.657050987864*m.s1s374 - 87.154001890177*m.s1s375 - 168.450467497125*m.s1s376
                          - 284.203842106564*m.s1s377 - 411.908652716088*m.s1s378 - 12.4236944883441*m.s1s379
                          - 24.0124044704238*m.s1s380 - 44.0301766363479*m.s1s381 - 74.2862014846846*m.s1s382
                          - 143.579699122125*m.s1s383 - 242.242736071415*m.s1s384 - 351.092646411238*m.s1s385
                          - 7.65172765642961*m.s1s386 - 14.7891900880288*m.s1s387 - 27.118094428506*m.s1s388
                          - 45.7527173518919*m.s1s389 - 88.4304387640365*m.s1s390 - 149.196798497086*m.s1s391
                          - 216.237232413786*m.s1s392 - 19.4406577877407*m.s1s393 - 37.5747277436911*m.s1s394
                          - 68.8986353555371*m.s1s395 - 116.243410747892*m.s1s396 - 224.674214141276*m.s1s397
                          - 379.062616031703*m.s1s398 - 549.391487135874*m.s1s399 - 7.48690188831565*m.s1s400
                          - 14.4706163324673*m.s1s401 - 26.5339439013751*m.s1s402 - 44.7671586494086*m.s1s403
                          - 86.5255598074927*m.s1s404 - 145.982952158506*m.s1s405 - 211.579268940989*m.s1s406
                          - 7.22029184733547*m.s1s407 - 13.9553148538372*m.s1s408 - 25.5890649679471*m.s1s409
                          - 43.1729913716576*m.s1s410 - 83.44436769489*m.s1s411 - 140.784470672041*m.s1s412
                          - 204.044889780639*m.s1s413 - 11.2055277593782*m.s1s414 - 21.6579428216942*m.s1s415
                          - 39.7129345873577*m.s1s416 - 67.0022990066581*m.s1s417 - 129.501438215952*m.s1s418
                          - 218.490377890626*m.s1s419 - 316.667348763747*m.s1s420 - 21.3709463532097*m.s1s421
                          - 41.3055720446486*m.s1s422 - 75.7396717780329*m.s1s423 - 127.785372394852*m.s1s424
                          - 246.982413341517*m.s1s425 - 416.700243385248*m.s1s426 - 603.94129286586*m.s1s427
                          - 18.7974273535344*m.s1s428 - 36.3314977714524*m.s1s429 - 66.6189954575545*m.s1s430
                          - 112.397280622803*m.s1s431 - 217.24044858175*m.s1s432 - 366.520622146333*m.s1s433
                          - 531.213844759881*m.s1s434 - 14.4405836946709*m.s1s435 - 27.9106297076743*m.s1s436
                          - 51.1781299358943*m.s1s437 - 86.3459827433152*m.s1s438 - 166.88873538978*m.s1s439
                          - 281.568941344082*m.s1s440 - 408.089779561278*m.s1s441 - 19.4475325416967*m.s1s442
                          - 37.5880152060303*m.s1s443 - 68.922999817437*m.s1s444 - 116.284517631036*m.s1s445
                          - 224.753665153652*m.s1s446 - 379.196663050462*m.s1s447 - 549.585767151543*m.s1s448
                          - 9.28783513744935*m.s1s449 - 17.9514438466182*m.s1s450 - 32.916538800503*m.s1s451
                          - 55.5356535066454*m.s1s452 - 107.338809384118*m.s1s453 - 181.098351861986*m.s1s454
                          - 262.473503425068*m.s1s455 - 7.22029184733547*m.s1s456 - 13.9553148538372*m.s1s457
                          - 25.5890649679471*m.s1s458 - 43.1729913716576*m.s1s459 - 83.44436769489*m.s1s460
                          - 140.784470672041*m.s1s461 - 204.044889780639*m.s1s462 - 6.67516217420068*m.s1s463
                          - 12.9016931463472*m.s1s464 - 23.6570989315674*m.s1s465 - 39.913444642481*m.s1s466
                          - 77.1443452237428*m.s1s467 - 130.155289178744*m.s1s468 - 188.639567333459*m.s1s469
                          - 18.5948501150879*m.s1s470 - 35.9399583150819*m.s1s471 - 65.9010518861256*m.s1s472
                          - 111.185990892074*m.s1s473 - 214.899278733085*m.s1s474 - 362.570680802145*m.s1s475
                          - 525.489027652088*m.s1s476 - 21.6341171926414*m.s1s477 - 41.8142262655959*m.s1s478
                          - 76.6723620141448*m.s1s479 - 129.358975321201*m.s1s480 - 250.023858861509*m.s1s481
                          - 421.831665786045*m.s1s482 - 611.378480456157*m.s1s483 - 16.2413705427568*m.s1s484
                          - 31.3911742592025*m.s1s485 - 57.5602059825984*m.s1s486 - 97.1136022105662*m.s1s487
                          - 187.700293020549*m.s1s488 - 316.681486454637*m.s1s489 - 458.979876763054*m.s1s490
                          - 13.9253546563734*m.s1s491 - 26.9147996770731*m.s1s492 - 49.3521332015331*m.s1s493
                          - 83.2652237802191*m.s1s494 - 160.93427229773*m.s1s495 - 271.522775764452*m.s1s496
                          - 393.529446744536*m.s1s497 - 7.76158051882097*m.s1s498 - 15.0015127080393*m.s1s499
                          - 27.5074183079396*m.s1s500 - 46.4095712271164*m.s1s501 - 89.7*m.s1s502
                          - 151.338758602103*m.s1s503 - 219.341665817957*m.s1s504 - 11.2055277593782*m.s1s505
                          - 21.6579428216942*m.s1s506 - 39.7129345873577*m.s1s507 - 67.0022990066581*m.s1s508
                          - 129.501438215952*m.s1s509 - 218.490377890626*m.s1s510 - 316.667348763747*m.s1s511
                          - 6.67516217420068*m.s1s512 - 12.9016931463472*m.s1s513 - 23.6570989315674*m.s1s514
                          - 39.913444642481*m.s1s515 - 77.1443452237428*m.s1s516 - 130.155289178744*m.s1s517
                          - 188.639567333459*m.s1s518 - 11.9558099050809*m.s1s519 - 23.1080813747994*m.s1s520
                          - 42.3719709499612*m.s1s521 - 71.4885338137291*m.s1s522 - 138.172392322055*m.s1s523
                          - 233.119713791557*m.s1s524 - 337.870264236031*m.s1s525 - 18.050112488828*m.s1s526
                          - 34.8870943522498*m.s1s527 - 63.9704752829104*m.s1s528 - 107.928788366802*m.s1s529
                          - 208.603787118067*m.s1s530 - 351.949143613665*m.s1s531 - 510.094784419302*m.s1s532
                          - 23.2234254748939*m.s1s533 - 44.8860269555956*m.s1s534 - 82.3049477528588*m.s1s535
                          - 138.862080487498*m.s1s536 - 268.391374675119*m.s1s537 - 452.820707501052*m.s1s538
                          - 656.292209725887*m.s1s539 - 7.76158051882097*m.s1s540 - 15.0015127080393*m.s1s541
                          - 27.5074183079396*m.s1s542 - 46.4095712271164*m.s1s543 - 89.7*m.s1s544
                          - 151.338758602103*m.s1s545 - 219.341665817957*m.s1s546 - 14.5757175798436*m.s1s547
                          - 28.1718152601258*m.s1s548 - 51.657050987864*m.s1s549 - 87.154001890177*m.s1s550
                          - 168.450467497125*m.s1s551 - 284.203842106564*m.s1s552 - 411.908652716088*m.s1s553
                          - 21.3709463532097*m.s1s554 - 41.3055720446486*m.s1s555 - 75.7396717780329*m.s1s556
                          - 127.785372394852*m.s1s557 - 246.982413341517*m.s1s558 - 416.700243385248*m.s1s559
                          - 603.94129286586*m.s1s560 - 18.5948501150879*m.s1s561 - 35.9399583150819*m.s1s562
                          - 65.9010518861256*m.s1s563 - 111.185990892074*m.s1s564 - 214.899278733085*m.s1s565
                          - 362.570680802145*m.s1s566 - 525.489027652088*m.s1s567 - 11.9558099050809*m.s1s568
                          - 23.1080813747994*m.s1s569 - 42.3719709499612*m.s1s570 - 71.4885338137291*m.s1s571
                          - 138.172392322055*m.s1s572 - 233.119713791557*m.s1s573 - 337.870264236031*m.s1s574
                          - 15.6261540208811*m.s1s575 - 30.2020893236365*m.s1s576 - 55.3798487504404*m.s1s577
                          - 93.434978388672*m.s1s578 - 180.590282130573*m.s1s579 - 304.685720326026*m.s1s580
                          - 441.593905385226*m.s1s581 - 14.9380525029139*m.s1s582 - 28.8721329260735*m.s1s583
                          - 52.941183552398*m.s1s584 - 89.3205462402005*m.s1s585 - 172.637944844116*m.s1s586
                          - 291.268810037089*m.s1s587 - 422.148209648796*m.s1s588 - 7.96556922221359*m.s1s589
                          - 15.3957802311063*m.s1s590 - 28.2303641796868*m.s1s591 - 47.6293006671023*m.s1s592
                          - 92.0574820424717*m.s1s593 - 155.316221319321*m.s1s594 - 225.10637081608*m.s1s595
                          - 12.4236944883441*m.s1s596 - 24.0124044704238*m.s1s597 - 44.0301766363479*m.s1s598
                          - 74.2862014846846*m.s1s599 - 143.579699122125*m.s1s600 - 242.242736071415*m.s1s601
                          - 351.092646411238*m.s1s602 - 18.7974273535344*m.s1s603 - 36.3314977714524*m.s1s604
                          - 66.6189954575545*m.s1s605 - 112.397280622803*m.s1s606 - 217.24044858175*m.s1s607
                          - 366.520622146333*m.s1s608 - 531.213844759881*m.s1s609 - 21.6341171926414*m.s1s610
                          - 41.8142262655959*m.s1s611 - 76.6723620141448*m.s1s612 - 129.358975321201*m.s1s613
                          - 250.023858861509*m.s1s614 - 421.831665786045*m.s1s615 - 611.378480456157*m.s1s616
                          - 18.050112488828*m.s1s617 - 34.8870943522498*m.s1s618 - 63.9704752829104*m.s1s619
                          - 107.928788366802*m.s1s620 - 208.603787118067*m.s1s621 - 351.949143613665*m.s1s622
                          - 510.094784419302*m.s1s623 - 15.6261540208811*m.s1s624 - 30.2020893236365*m.s1s625
                          - 55.3798487504404*m.s1s626 - 93.434978388672*m.s1s627 - 180.590282130573*m.s1s628
                          - 304.685720326026*m.s1s629 - 441.593905385226*m.s1s630 == 0)

m.c235 = Constraint(expr= - 0.2*m.x177 - 0.17*m.x178 + m.x181 == 0)

m.c237 = Constraint(expr= - m.b183 + m.s1s239 + m.s1s240 + m.s1s241 + m.s1s242 + m.s1s243 + m.s1s244 + m.s1s245 == 0)

m.c238 = Constraint(expr= - m.b184 + m.s1s246 + m.s1s247 + m.s1s248 + m.s1s249 + m.s1s250 + m.s1s251 + m.s1s252 == 0)

m.c239 = Constraint(expr= - m.b185 + m.s1s253 + m.s1s254 + m.s1s255 + m.s1s256 + m.s1s257 + m.s1s258 + m.s1s259 == 0)

m.c240 = Constraint(expr= - m.b186 + m.s1s260 + m.s1s261 + m.s1s262 + m.s1s263 + m.s1s264 + m.s1s265 + m.s1s266 == 0)

m.c241 = Constraint(expr= - m.b187 + m.s1s267 + m.s1s268 + m.s1s269 + m.s1s270 + m.s1s271 + m.s1s272 + m.s1s273 == 0)

m.c242 = Constraint(expr= - m.b188 + m.s1s274 + m.s1s275 + m.s1s276 + m.s1s277 + m.s1s278 + m.s1s279 + m.s1s280 == 0)

m.c243 = Constraint(expr= - m.b189 + m.s1s281 + m.s1s282 + m.s1s283 + m.s1s284 + m.s1s285 + m.s1s286 + m.s1s287 == 0)

m.c244 = Constraint(expr= - m.b190 + m.s1s288 + m.s1s289 + m.s1s290 + m.s1s291 + m.s1s292 + m.s1s293 + m.s1s294 == 0)

m.c245 = Constraint(expr= - m.b191 + m.s1s295 + m.s1s296 + m.s1s297 + m.s1s298 + m.s1s299 + m.s1s300 + m.s1s301 == 0)

m.c246 = Constraint(expr= - m.b192 + m.s1s302 + m.s1s303 + m.s1s304 + m.s1s305 + m.s1s306 + m.s1s307 + m.s1s308 == 0)

m.c247 = Constraint(expr= - m.b193 + m.s1s309 + m.s1s310 + m.s1s311 + m.s1s312 + m.s1s313 + m.s1s314 + m.s1s315 == 0)

m.c248 = Constraint(expr= - m.b194 + m.s1s316 + m.s1s317 + m.s1s318 + m.s1s319 + m.s1s320 + m.s1s321 + m.s1s322 == 0)

m.c249 = Constraint(expr= - m.b195 + m.s1s323 + m.s1s324 + m.s1s325 + m.s1s326 + m.s1s327 + m.s1s328 + m.s1s329 == 0)

m.c250 = Constraint(expr= - m.b196 + m.s1s330 + m.s1s331 + m.s1s332 + m.s1s333 + m.s1s334 + m.s1s335 + m.s1s336 == 0)

m.c251 = Constraint(expr= - m.b197 + m.s1s337 + m.s1s338 + m.s1s339 + m.s1s340 + m.s1s341 + m.s1s342 + m.s1s343 == 0)

m.c252 = Constraint(expr= - m.b198 + m.s1s344 + m.s1s345 + m.s1s346 + m.s1s347 + m.s1s348 + m.s1s349 + m.s1s350 == 0)

m.c253 = Constraint(expr= - m.b199 + m.s1s351 + m.s1s352 + m.s1s353 + m.s1s354 + m.s1s355 + m.s1s356 + m.s1s357 == 0)

m.c254 = Constraint(expr= - m.b200 + m.s1s358 + m.s1s359 + m.s1s360 + m.s1s361 + m.s1s362 + m.s1s363 + m.s1s364 == 0)

m.c255 = Constraint(expr= - m.b201 + m.s1s365 + m.s1s366 + m.s1s367 + m.s1s368 + m.s1s369 + m.s1s370 + m.s1s371 == 0)

m.c256 = Constraint(expr= - m.b202 + m.s1s372 + m.s1s373 + m.s1s374 + m.s1s375 + m.s1s376 + m.s1s377 + m.s1s378 == 0)

m.c257 = Constraint(expr= - m.b203 + m.s1s379 + m.s1s380 + m.s1s381 + m.s1s382 + m.s1s383 + m.s1s384 + m.s1s385 == 0)

m.c258 = Constraint(expr= - m.b204 + m.s1s386 + m.s1s387 + m.s1s388 + m.s1s389 + m.s1s390 + m.s1s391 + m.s1s392 == 0)

m.c259 = Constraint(expr= - m.b205 + m.s1s393 + m.s1s394 + m.s1s395 + m.s1s396 + m.s1s397 + m.s1s398 + m.s1s399 == 0)

m.c260 = Constraint(expr= - m.b206 + m.s1s400 + m.s1s401 + m.s1s402 + m.s1s403 + m.s1s404 + m.s1s405 + m.s1s406 == 0)

m.c261 = Constraint(expr= - m.b207 + m.s1s407 + m.s1s408 + m.s1s409 + m.s1s410 + m.s1s411 + m.s1s412 + m.s1s413 == 0)

m.c262 = Constraint(expr= - m.b208 + m.s1s414 + m.s1s415 + m.s1s416 + m.s1s417 + m.s1s418 + m.s1s419 + m.s1s420 == 0)

m.c263 = Constraint(expr= - m.b209 + m.s1s421 + m.s1s422 + m.s1s423 + m.s1s424 + m.s1s425 + m.s1s426 + m.s1s427 == 0)

m.c264 = Constraint(expr= - m.b210 + m.s1s428 + m.s1s429 + m.s1s430 + m.s1s431 + m.s1s432 + m.s1s433 + m.s1s434 == 0)

m.c265 = Constraint(expr= - m.b211 + m.s1s435 + m.s1s436 + m.s1s437 + m.s1s438 + m.s1s439 + m.s1s440 + m.s1s441 == 0)

m.c266 = Constraint(expr= - m.b212 + m.s1s442 + m.s1s443 + m.s1s444 + m.s1s445 + m.s1s446 + m.s1s447 + m.s1s448 == 0)

m.c267 = Constraint(expr= - m.b213 + m.s1s449 + m.s1s450 + m.s1s451 + m.s1s452 + m.s1s453 + m.s1s454 + m.s1s455 == 0)

m.c268 = Constraint(expr= - m.b214 + m.s1s456 + m.s1s457 + m.s1s458 + m.s1s459 + m.s1s460 + m.s1s461 + m.s1s462 == 0)

m.c269 = Constraint(expr= - m.b215 + m.s1s463 + m.s1s464 + m.s1s465 + m.s1s466 + m.s1s467 + m.s1s468 + m.s1s469 == 0)

m.c270 = Constraint(expr= - m.b216 + m.s1s470 + m.s1s471 + m.s1s472 + m.s1s473 + m.s1s474 + m.s1s475 + m.s1s476 == 0)

m.c271 = Constraint(expr= - m.b217 + m.s1s477 + m.s1s478 + m.s1s479 + m.s1s480 + m.s1s481 + m.s1s482 + m.s1s483 == 0)

m.c272 = Constraint(expr= - m.b218 + m.s1s484 + m.s1s485 + m.s1s486 + m.s1s487 + m.s1s488 + m.s1s489 + m.s1s490 == 0)

m.c273 = Constraint(expr= - m.b219 + m.s1s491 + m.s1s492 + m.s1s493 + m.s1s494 + m.s1s495 + m.s1s496 + m.s1s497 == 0)

m.c274 = Constraint(expr= - m.b220 + m.s1s498 + m.s1s499 + m.s1s500 + m.s1s501 + m.s1s502 + m.s1s503 + m.s1s504 == 0)

m.c275 = Constraint(expr= - m.b221 + m.s1s505 + m.s1s506 + m.s1s507 + m.s1s508 + m.s1s509 + m.s1s510 + m.s1s511 == 0)

m.c276 = Constraint(expr= - m.b222 + m.s1s512 + m.s1s513 + m.s1s514 + m.s1s515 + m.s1s516 + m.s1s517 + m.s1s518 == 0)

m.c277 = Constraint(expr= - m.b223 + m.s1s519 + m.s1s520 + m.s1s521 + m.s1s522 + m.s1s523 + m.s1s524 + m.s1s525 == 0)

m.c278 = Constraint(expr= - m.b224 + m.s1s526 + m.s1s527 + m.s1s528 + m.s1s529 + m.s1s530 + m.s1s531 + m.s1s532 == 0)

m.c279 = Constraint(expr= - m.b225 + m.s1s533 + m.s1s534 + m.s1s535 + m.s1s536 + m.s1s537 + m.s1s538 + m.s1s539 == 0)

m.c280 = Constraint(expr= - m.b226 + m.s1s540 + m.s1s541 + m.s1s542 + m.s1s543 + m.s1s544 + m.s1s545 + m.s1s546 == 0)

m.c281 = Constraint(expr= - m.b227 + m.s1s547 + m.s1s548 + m.s1s549 + m.s1s550 + m.s1s551 + m.s1s552 + m.s1s553 == 0)

m.c282 = Constraint(expr= - m.b228 + m.s1s554 + m.s1s555 + m.s1s556 + m.s1s557 + m.s1s558 + m.s1s559 + m.s1s560 == 0)

m.c283 = Constraint(expr= - m.b229 + m.s1s561 + m.s1s562 + m.s1s563 + m.s1s564 + m.s1s565 + m.s1s566 + m.s1s567 == 0)

m.c284 = Constraint(expr= - m.b230 + m.s1s568 + m.s1s569 + m.s1s570 + m.s1s571 + m.s1s572 + m.s1s573 + m.s1s574 == 0)

m.c285 = Constraint(expr= - m.b231 + m.s1s575 + m.s1s576 + m.s1s577 + m.s1s578 + m.s1s579 + m.s1s580 + m.s1s581 == 0)

m.c286 = Constraint(expr= - m.b232 + m.s1s582 + m.s1s583 + m.s1s584 + m.s1s585 + m.s1s586 + m.s1s587 + m.s1s588 == 0)

m.c287 = Constraint(expr= - m.b233 + m.s1s589 + m.s1s590 + m.s1s591 + m.s1s592 + m.s1s593 + m.s1s594 + m.s1s595 == 0)

m.c288 = Constraint(expr= - m.b234 + m.s1s596 + m.s1s597 + m.s1s598 + m.s1s599 + m.s1s600 + m.s1s601 + m.s1s602 == 0)

m.c289 = Constraint(expr= - m.b235 + m.s1s603 + m.s1s604 + m.s1s605 + m.s1s606 + m.s1s607 + m.s1s608 + m.s1s609 == 0)

m.c290 = Constraint(expr= - m.b236 + m.s1s610 + m.s1s611 + m.s1s612 + m.s1s613 + m.s1s614 + m.s1s615 + m.s1s616 == 0)

m.c291 = Constraint(expr= - m.b237 + m.s1s617 + m.s1s618 + m.s1s619 + m.s1s620 + m.s1s621 + m.s1s622 + m.s1s623 == 0)

m.c292 = Constraint(expr= - m.b238 + m.s1s624 + m.s1s625 + m.s1s626 + m.s1s627 + m.s1s628 + m.s1s629 + m.s1s630 == 0)

m.c293 = Constraint(expr=   m.x1 - 0.0122927400295263*m.s1s239 - 0.047959606911495*m.s1s240 - 0.167824502578647*m.s1s241
                          - 0.494468436052303*m.s1s242 - 1.92914775438588*m.s1s243 - 2*m.s1s244 - 2*m.s1s245 <= 0)

m.c294 = Constraint(expr=   m.x2 - 0.0176041976445841*m.s1s246 - 0.0686820348432157*m.s1s247
                          - 0.240338257044582*m.s1s248 - 0.708118780382974*m.s1s249 - 2*m.s1s250 - 2*m.s1s251
                          - 2*m.s1s252 <= 0)

m.c295 = Constraint(expr=   m.x3 - 0.0192122784105588*m.s1s253 - 0.0749558941482069*m.s1s254
                          - 0.262292300976835*m.s1s255 - 0.772802909347502*m.s1s256 - 2*m.s1s257 - 2*m.s1s258
                          - 2*m.s1s259 <= 0)

m.c296 = Constraint(expr=   m.x4 - 0.0139851216849881*m.s1s260 - 0.0545623625823394*m.s1s261
                          - 0.190929449792929*m.s1s262 - 0.56254352007505*m.s1s263 - 2*m.s1s264 - 2*m.s1s265
                          - 2*m.s1s266 <= 0)

m.c297 = Constraint(expr=   m.x5 - 0.0131870388642087*m.s1s267 - 0.0514486761076021*m.s1s268
                          - 0.180033762412234*m.s1s269 - 0.530441095124783*m.s1s270 - 2*m.s1s271 - 2*m.s1s272
                          - 2*m.s1s273 <= 0)

m.c298 = Constraint(expr=   m.x6 - 0.0110279676651009*m.s1s274 - 0.0430251508598196*m.s1s275 - 0.15055741709363*m.s1s276
                          - 0.443593691162434*m.s1s277 - 1.7306620822916*m.s1s278 - 2*m.s1s279 - 2*m.s1s280 <= 0)

m.c299 = Constraint(expr=   m.x7 - 0.0137502828767635*m.s1s281 - 0.0536461488738445*m.s1s282
                          - 0.187723353667753*m.s1s283 - 0.553097263345606*m.s1s284 - 2*m.s1s285 - 2*m.s1s286
                          - 2*m.s1s287 <= 0)

m.c300 = Constraint(expr=   m.x8 - 0.0122927400295263*m.s1s288 - 0.047959606911495*m.s1s289 - 0.167824502578647*m.s1s290
                          - 0.494468436052303*m.s1s291 - 1.92914775438588*m.s1s292 - 2*m.s1s293 - 2*m.s1s294 <= 0)

m.c301 = Constraint(expr=   m.x9 - 0.0153698320860398*m.s1s295 - 0.0599647518268192*m.s1s296
                          - 0.209833968534382*m.s1s297 - 0.618242703881818*m.s1s298 - 2*m.s1s299 - 2*m.s1s300
                          - 2*m.s1s301 <= 0)

m.c302 = Constraint(expr=   m.x10 - 0.0120532217270583*m.s1s302 - 0.0470251363535167*m.s1s303 - 0.1645545204694*m.s1s304
                          - 0.484833949343662*m.s1s305 - 1.89155921072266*m.s1s306 - 2*m.s1s307 - 2*m.s1s308 <= 0)

m.c303 = Constraint(expr=   m.x11 - 0.0120510911159401*m.s1s309 - 0.0470168238640743*m.s1s310
                          - 0.164525432670402*m.s1s311 - 0.484748246730172*m.s1s312 - 1.89122484558971*m.s1s313
                          - 2*m.s1s314 - 2*m.s1s315 <= 0)

m.c304 = Constraint(expr=   m.x12 - 0.0142414920290718*m.s1s316 - 0.0555625806701283*m.s1s317
                          - 0.194429501479406*m.s1s318 - 0.572855870518057*m.s1s319 - 2*m.s1s320 - 2*m.s1s321
                          - 2*m.s1s322 <= 0)

m.c305 = Constraint(expr=   m.x13 - 0.0190758342372385*m.s1s323 - 0.0744235629590588*m.s1s324
                          - 0.260429520550158*m.s1s325 - 0.767314520523847*m.s1s326 - 2*m.s1s327 - 2*m.s1s328
                          - 2*m.s1s329 <= 0)

m.c306 = Constraint(expr=   m.x14 - 0.0188299954674205*m.s1s330 - 0.0734644333642121*m.s1s331
                          - 0.257073249355929*m.s1s332 - 0.757425796631457*m.s1s333 - 2*m.s1s334 - 2*m.s1s335
                          - 2*m.s1s336 <= 0)

m.c307 = Constraint(expr=   m.x15 - 0.0176041976445841*m.s1s337 - 0.0686820348432157*m.s1s338
                          - 0.240338257044582*m.s1s339 - 0.708118780382974*m.s1s340 - 2*m.s1s341 - 2*m.s1s342
                          - 2*m.s1s343 <= 0)

m.c308 = Constraint(expr=   m.x16 - 0.0153698320860398*m.s1s344 - 0.0599647518268192*m.s1s345
                          - 0.209833968534382*m.s1s346 - 0.618242703881818*m.s1s347 - 2*m.s1s348 - 2*m.s1s349
                          - 2*m.s1s350 <= 0)

m.c309 = Constraint(expr=   m.x17 - 0.0194226083350049*m.s1s351 - 0.0757764874800376*m.s1s352
                          - 0.265163793814297*m.s1s353 - 0.781263310246409*m.s1s354 - 2*m.s1s355 - 2*m.s1s356
                          - 2*m.s1s357 <= 0)

m.c310 = Constraint(expr=   m.x18 - 0.0174381887671401*m.s1s358 - 0.0680343582075014*m.s1s359
                          - 0.238071849619242*m.s1s360 - 0.701441168247406*m.s1s361 - 2*m.s1s362 - 2*m.s1s363
                          - 2*m.s1s364 <= 0)

m.c311 = Constraint(expr=   m.x19 - 0.0190758342372385*m.s1s365 - 0.0744235629590588*m.s1s366
                          - 0.260429520550158*m.s1s367 - 0.767314520523847*m.s1s368 - 2*m.s1s369 - 2*m.s1s370
                          - 2*m.s1s371 <= 0)

m.c312 = Constraint(expr=   m.x20 - 0.0139201415373155*m.s1s372 - 0.0543088452760314*m.s1s373
                          - 0.190042319589699*m.s1s374 - 0.559929730804558*m.s1s375 - 2*m.s1s376 - 2*m.s1s377
                          - 2*m.s1s378 <= 0)

m.c313 = Constraint(expr=   m.x21 - 0.0150776355652448*m.s1s379 - 0.0588247594211735*m.s1s380
                          - 0.205844806180028*m.s1s381 - 0.606489265973719*m.s1s382 - 2*m.s1s383 - 2*m.s1s384
                          - 2*m.s1s385 <= 0)

m.c314 = Constraint(expr=   m.x22 - 0.0192122784105588*m.s1s386 - 0.0749558941482069*m.s1s387
                          - 0.262292300976835*m.s1s388 - 0.772802909347502*m.s1s389 - 2*m.s1s390 - 2*m.s1s391
                          - 2*m.s1s392 <= 0)

m.c315 = Constraint(expr=   m.x23 - 0.0120532217270583*m.s1s393 - 0.0470251363535167*m.s1s394 - 0.1645545204694*m.s1s395
                          - 0.484833949343662*m.s1s396 - 1.89155921072266*m.s1s397 - 2*m.s1s398 - 2*m.s1s399 <= 0)

m.c316 = Constraint(expr=   m.x24 - 0.0194226083350049*m.s1s400 - 0.0757764874800376*m.s1s401
                          - 0.265163793814297*m.s1s402 - 0.781263310246409*m.s1s403 - 2*m.s1s404 - 2*m.s1s405
                          - 2*m.s1s406 <= 0)

m.c317 = Constraint(expr=   m.x25 - 0.0197779487583483*m.s1s407 - 0.0771628331590627*m.s1s408
                          - 0.270015017353593*m.s1s409 - 0.795556675515238*m.s1s410 - 2*m.s1s411 - 2*m.s1s412
                          - 2*m.s1s413 <= 0)

m.c318 = Constraint(expr=   m.x26 - 0.015876050278038*m.s1s414 - 0.0619397407586086*m.s1s415
                          - 0.216745024658915*m.s1s416 - 0.638605041090392*m.s1s417 - 2*m.s1s418 - 2*m.s1s419
                          - 2*m.s1s420 <= 0)

m.c319 = Constraint(expr=   m.x27 - 0.0114959997704606*m.s1s421 - 0.0448511583846756*m.s1s422
                          - 0.156947144289045*m.s1s423 - 0.462420014879005*m.s1s424 - 1.80411219047469*m.s1s425
                          - 2*m.s1s426 - 2*m.s1s427 <= 0)

m.c320 = Constraint(expr=   m.x28 - 0.0122577120780475*m.s1s428 - 0.0478229468357263*m.s1s429
                          - 0.167346289542402*m.s1s430 - 0.493059456740591*m.s1s431 - 1.92365068100974*m.s1s432
                          - 2*m.s1s433 - 2*m.s1s434 <= 0)

m.c321 = Constraint(expr=   m.x29 - 0.0139851216849881*m.s1s435 - 0.0545623625823394*m.s1s436
                          - 0.190929449792929*m.s1s437 - 0.56254352007505*m.s1s438 - 2*m.s1s439 - 2*m.s1s440
                          - 2*m.s1s441 <= 0)

m.c322 = Constraint(expr=   m.x30 - 0.0120510911159401*m.s1s442 - 0.0470168238640743*m.s1s443
                          - 0.164525432670402*m.s1s444 - 0.484748246730172*m.s1s445 - 1.89122484558971*m.s1s446
                          - 2*m.s1s447 - 2*m.s1s448 <= 0)

m.c323 = Constraint(expr=   m.x31 - 0.0174381887671401*m.s1s449 - 0.0680343582075014*m.s1s450
                          - 0.238071849619242*m.s1s451 - 0.701441168247406*m.s1s452 - 2*m.s1s453 - 2*m.s1s454
                          - 2*m.s1s455 <= 0)

m.c324 = Constraint(expr=   m.x32 - 0.0197779487583483*m.s1s456 - 0.0771628331590627*m.s1s457
                          - 0.270015017353593*m.s1s458 - 0.795556675515238*m.s1s459 - 2*m.s1s460 - 2*m.s1s461
                          - 2*m.s1s462 <= 0)

m.c325 = Constraint(expr=   m.x33 - 0.02056968839856*m.s1s463 - 0.0802517719822704*m.s1s464 - 0.280824105561038*m.s1s465
                          - 0.827403949655566*m.s1s466 - 2*m.s1s467 - 2*m.s1s468 - 2*m.s1s469 <= 0)

m.c326 = Constraint(expr=   m.x34 - 0.0123243005973977*m.s1s470 - 0.0480827391363186*m.s1s471
                          - 0.168255377761185*m.s1s472 - 0.495737941841801*m.s1s473 - 1.93410067769589*m.s1s474
                          - 2*m.s1s475 - 2*m.s1s476 <= 0)

m.c327 = Constraint(expr=   m.x35 - 0.0114258635818418*m.s1s477 - 0.0445775250020163*m.s1s478
                          - 0.155989622130483*m.s1s479 - 0.459598826810784*m.s1s480 - 1.7931054441797*m.s1s481
                          - 2*m.s1s482 - 2*m.s1s483 <= 0)

m.c328 = Constraint(expr=   m.x36 - 0.0131870388642087*m.s1s484 - 0.0514486761076021*m.s1s485
                          - 0.180033762412234*m.s1s486 - 0.530441095124783*m.s1s487 - 2*m.s1s488 - 2*m.s1s489
                          - 2*m.s1s490 <= 0)

m.c329 = Constraint(expr=   m.x37 - 0.0142414920290718*m.s1s491 - 0.0555625806701283*m.s1s492
                          - 0.194429501479406*m.s1s493 - 0.572855870518057*m.s1s494 - 2*m.s1s495 - 2*m.s1s496
                          - 2*m.s1s497 <= 0)

m.c330 = Constraint(expr=   m.x38 - 0.0190758342372385*m.s1s498 - 0.0744235629590588*m.s1s499
                          - 0.260429520550158*m.s1s500 - 0.767314520523847*m.s1s501 - 2*m.s1s502 - 2*m.s1s503
                          - 2*m.s1s504 <= 0)

m.c331 = Constraint(expr=   m.x39 - 0.015876050278038*m.s1s505 - 0.0619397407586086*m.s1s506
                          - 0.216745024658915*m.s1s507 - 0.638605041090392*m.s1s508 - 2*m.s1s509 - 2*m.s1s510
                          - 2*m.s1s511 <= 0)

m.c332 = Constraint(expr=   m.x40 - 0.02056968839856*m.s1s512 - 0.0802517719822704*m.s1s513 - 0.280824105561038*m.s1s514
                          - 0.827403949655566*m.s1s515 - 2*m.s1s516 - 2*m.s1s517 - 2*m.s1s518 <= 0)

m.c333 = Constraint(expr=   m.x41 - 0.0153698320860398*m.s1s519 - 0.0599647518268192*m.s1s520
                          - 0.209833968534382*m.s1s521 - 0.618242703881818*m.s1s522 - 2*m.s1s523 - 2*m.s1s524
                          - 2*m.s1s525 <= 0)

m.c334 = Constraint(expr=   m.x42 - 0.012508886937106*m.s1s526 - 0.048802894957753*m.s1s527 - 0.170775410770095*m.s1s528
                          - 0.503162821770358*m.s1s529 - 1.96306853367294*m.s1s530 - 2*m.s1s531 - 2*m.s1s532 <= 0)

m.c335 = Constraint(expr=   m.x43 - 0.0110279676651009*m.s1s533 - 0.0430251508598196*m.s1s534
                          - 0.15055741709363*m.s1s535 - 0.443593691162434*m.s1s536 - 1.7306620822916*m.s1s537
                          - 2*m.s1s538 - 2*m.s1s539 <= 0)

m.c336 = Constraint(expr=   m.x44 - 0.0190758342372385*m.s1s540 - 0.0744235629590588*m.s1s541
                          - 0.260429520550158*m.s1s542 - 0.767314520523847*m.s1s543 - 2*m.s1s544 - 2*m.s1s545
                          - 2*m.s1s546 <= 0)

m.c337 = Constraint(expr=   m.x45 - 0.0139201415373155*m.s1s547 - 0.0543088452760314*m.s1s548
                          - 0.190042319589699*m.s1s549 - 0.559929730804558*m.s1s550 - 2*m.s1s551 - 2*m.s1s552
                          - 2*m.s1s553 <= 0)

m.c338 = Constraint(expr=   m.x46 - 0.0114959997704606*m.s1s554 - 0.0448511583846756*m.s1s555
                          - 0.156947144289045*m.s1s556 - 0.462420014879005*m.s1s557 - 1.80411219047469*m.s1s558
                          - 2*m.s1s559 - 2*m.s1s560 <= 0)

m.c339 = Constraint(expr=   m.x47 - 0.0123243005973977*m.s1s561 - 0.0480827391363186*m.s1s562
                          - 0.168255377761185*m.s1s563 - 0.495737941841801*m.s1s564 - 1.93410067769589*m.s1s565
                          - 2*m.s1s566 - 2*m.s1s567 <= 0)

m.c340 = Constraint(expr=   m.x48 - 0.0153698320860398*m.s1s568 - 0.0599647518268192*m.s1s569
                          - 0.209833968534382*m.s1s570 - 0.618242703881818*m.s1s571 - 2*m.s1s572 - 2*m.s1s573
                          - 2*m.s1s574 <= 0)

m.c341 = Constraint(expr=   m.x49 - 0.0134441259722562*m.s1s575 - 0.0524516906197741*m.s1s576
                          - 0.183543599594492*m.s1s577 - 0.540782276988236*m.s1s578 - 2*m.s1s579 - 2*m.s1s580
                          - 2*m.s1s581 <= 0)

m.c342 = Constraint(expr=   m.x50 - 0.0137502828767635*m.s1s582 - 0.0536461488738445*m.s1s583
                          - 0.187723353667753*m.s1s584 - 0.553097263345606*m.s1s585 - 2*m.s1s586 - 2*m.s1s587
                          - 2*m.s1s588 <= 0)

m.c343 = Constraint(expr=   m.x51 - 0.0188299954674205*m.s1s589 - 0.0734644333642121*m.s1s590
                          - 0.257073249355929*m.s1s591 - 0.757425796631457*m.s1s592 - 2*m.s1s593 - 2*m.s1s594
                          - 2*m.s1s595 <= 0)

m.c344 = Constraint(expr=   m.x52 - 0.0150776355652448*m.s1s596 - 0.0588247594211735*m.s1s597
                          - 0.205844806180028*m.s1s598 - 0.606489265973719*m.s1s599 - 2*m.s1s600 - 2*m.s1s601
                          - 2*m.s1s602 <= 0)

m.c345 = Constraint(expr=   m.x53 - 0.0122577120780475*m.s1s603 - 0.0478229468357263*m.s1s604
                          - 0.167346289542402*m.s1s605 - 0.493059456740591*m.s1s606 - 1.92365068100974*m.s1s607
                          - 2*m.s1s608 - 2*m.s1s609 <= 0)

m.c346 = Constraint(expr=   m.x54 - 0.0114258635818418*m.s1s610 - 0.0445775250020163*m.s1s611
                          - 0.155989622130483*m.s1s612 - 0.459598826810784*m.s1s613 - 1.7931054441797*m.s1s614
                          - 2*m.s1s615 - 2*m.s1s616 <= 0)

m.c347 = Constraint(expr=   m.x55 - 0.012508886937106*m.s1s617 - 0.048802894957753*m.s1s618 - 0.170775410770095*m.s1s619
                          - 0.503162821770358*m.s1s620 - 1.96306853367294*m.s1s621 - 2*m.s1s622 - 2*m.s1s623 <= 0)

m.c348 = Constraint(expr=   m.x56 - 0.0134441259722562*m.s1s624 - 0.0524516906197741*m.s1s625
                          - 0.183543599594492*m.s1s626 - 0.540782276988236*m.s1s627 - 2*m.s1s628 - 2*m.s1s629
                          - 2*m.s1s630 <= 0)

m.c349 = Constraint(expr=   m.b183 + m.b190 <= 1)

m.c350 = Constraint(expr=   m.b184 + m.b197 <= 1)

m.c351 = Constraint(expr=   m.b185 + m.b204 <= 1)

m.c352 = Constraint(expr=   m.b186 + m.b211 <= 1)

m.c353 = Constraint(expr=   m.b187 + m.b218 <= 1)

m.c354 = Constraint(expr=   m.b188 + m.b225 <= 1)

m.c355 = Constraint(expr=   m.b189 + m.b232 <= 1)

m.c356 = Constraint(expr=   m.b191 + m.b198 <= 1)

m.c357 = Constraint(expr=   m.b192 + m.b205 <= 1)

m.c358 = Constraint(expr=   m.b193 + m.b212 <= 1)

m.c359 = Constraint(expr=   m.b194 + m.b219 <= 1)

m.c360 = Constraint(expr=   m.b195 + m.b226 <= 1)

m.c361 = Constraint(expr=   m.b196 + m.b233 <= 1)

m.c362 = Constraint(expr=   m.b199 + m.b206 <= 1)

m.c363 = Constraint(expr=   m.b200 + m.b213 <= 1)

m.c364 = Constraint(expr=   m.b201 + m.b220 <= 1)

m.c365 = Constraint(expr=   m.b202 + m.b227 <= 1)

m.c366 = Constraint(expr=   m.b203 + m.b234 <= 1)

m.c367 = Constraint(expr=   m.b207 + m.b214 <= 1)

m.c368 = Constraint(expr=   m.b208 + m.b221 <= 1)

m.c369 = Constraint(expr=   m.b209 + m.b228 <= 1)

m.c370 = Constraint(expr=   m.b210 + m.b235 <= 1)

m.c371 = Constraint(expr=   m.b215 + m.b222 <= 1)

m.c372 = Constraint(expr=   m.b216 + m.b229 <= 1)

m.c373 = Constraint(expr=   m.b217 + m.b236 <= 1)

m.c374 = Constraint(expr=   m.b223 + m.b230 <= 1)

m.c375 = Constraint(expr=   m.b224 + m.b237 <= 1)

m.c376 = Constraint(expr=   m.b231 + m.b238 <= 1)

m.c377 = Constraint(expr=   m.b183 + m.b184 + m.b185 + m.b186 + m.b187 + m.b188 + m.b189 >= 2)

m.c378 = Constraint(expr=   m.b183 + m.b191 + m.b192 + m.b193 + m.b194 + m.b195 + m.b196 >= 2)

m.c379 = Constraint(expr=   m.b184 + m.b191 + m.b199 + m.b200 + m.b201 + m.b202 + m.b203 >= 2)

m.c380 = Constraint(expr=   m.b185 + m.b192 + m.b199 + m.b207 + m.b208 + m.b209 + m.b210 >= 2)

m.c381 = Constraint(expr=   m.b186 + m.b193 + m.b200 + m.b207 + m.b215 + m.b216 + m.b217 >= 2)

m.c382 = Constraint(expr=   m.b187 + m.b194 + m.b201 + m.b208 + m.b215 + m.b223 + m.b224 >= 2)

m.c383 = Constraint(expr=   m.b188 + m.b195 + m.b202 + m.b209 + m.b216 + m.b223 + m.b231 >= 2)

m.c384 = Constraint(expr=   m.b189 + m.b196 + m.b203 + m.b210 + m.b217 + m.b224 + m.b231 >= 2)
