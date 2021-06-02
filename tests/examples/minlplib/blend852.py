#  MINLP written by GAMS Convert at 04/21/18 13:51:13
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        861       65      208      588        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        305      185      120        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       2413     2037      376        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x34 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x35 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x36 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x37 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x38 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x39 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x40 = Var(within=Reals,bounds=(0,1),initialize=0)
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
m.x77 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x78 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x79 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x80 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x81 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x82 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x83 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x84 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x85 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x86 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x87 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x88 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x89 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x90 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x91 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x92 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x93 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x94 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x95 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x96 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x97 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x98 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x99 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x100 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x101 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x102 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x103 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x104 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x105 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x106 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x107 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x108 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x109 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x110 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x111 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x112 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x113 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x114 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x115 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x116 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x117 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x118 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x119 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x120 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x121 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x122 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x123 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x124 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x125 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x126 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x127 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x128 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x129 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x130 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x131 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x132 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x133 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x134 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x135 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x136 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x137 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x138 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x139 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x140 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x141 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x142 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x143 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x144 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x145 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x146 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x147 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x148 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x149 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x150 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x151 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x152 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x153 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x154 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x155 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x156 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x157 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x158 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x159 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x160 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x161 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x162 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x163 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x164 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x165 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x166 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x167 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x168 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x169 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x170 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x171 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x172 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x173 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x174 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x175 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x176 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x177 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x178 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x179 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x180 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x181 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x182 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x183 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x184 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x185 = Var(within=Reals,bounds=(0,2),initialize=0)
m.b186 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b187 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b188 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b189 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b190 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b191 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b192 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b193 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b194 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b195 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b196 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b197 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b198 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b199 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b200 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b201 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b202 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b203 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b204 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b205 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b206 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b207 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b208 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b209 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b210 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b211 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b212 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b213 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b214 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b215 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b216 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b217 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b218 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b219 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b220 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b221 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b222 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b223 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b224 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b225 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b226 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b227 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b228 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b229 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b230 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b231 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b232 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b233 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b234 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b235 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b236 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b237 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b238 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b239 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b240 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b241 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b242 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b243 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b244 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b245 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b246 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b247 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b248 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b249 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b250 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b251 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b252 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b253 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b254 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b255 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b256 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b257 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b258 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b259 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b260 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b261 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b262 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b263 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b264 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b265 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b266 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b267 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b268 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b269 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b270 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b271 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b272 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b273 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b274 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b275 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b276 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b277 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b278 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b279 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b280 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b281 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b282 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b283 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b284 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b285 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b286 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b287 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b288 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b289 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b290 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b291 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b292 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b293 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b294 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b295 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b296 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b297 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b298 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b299 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b300 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b301 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b302 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b303 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b304 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b305 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr= - 1.03*m.x2 - 1.03*m.x3 - 1.03*m.x4 - 1.03*m.x5 - 0.75*m.x6 - 0.75*m.x7 - 0.75*m.x8 - 0.75*m.x9
                        - 0.49*m.x10 - 0.49*m.x11 - 0.49*m.x12 - 0.49*m.x13 - 0.95*m.x14 - 0.95*m.x15 - 0.95*m.x16
                        - 0.95*m.x17 + 8.83*m.x18 + 8.83*m.x19 + 8.83*m.x20 + 8.83*m.x21 - 1.05*m.x22 - 1.05*m.x23
                        - 1.05*m.x24 - 1.05*m.x25 - 1.78*m.x26 - 1.78*m.x27 - 1.78*m.x28 - 1.78*m.x29 - 1.13*m.x30
                        - 1.13*m.x31 - 1.13*m.x32 - 1.13*m.x33 + 8.13*m.x34 + 8.13*m.x35 + 8.13*m.x36 + 8.13*m.x37
                        + 8.26*m.x38 + 8.26*m.x39 + 8.26*m.x40 + 8.26*m.x41 - 0.79*m.x42 - 0.79*m.x43 - 0.79*m.x44
                        - 0.79*m.x45 - 0.53*m.x46 - 0.53*m.x47 - 0.53*m.x48 - 0.53*m.x49 - 0.6*m.x50 - 0.6*m.x51
                        - 0.6*m.x52 - 0.6*m.x53 + 8.95*m.x54 + 8.95*m.x55 + 8.95*m.x56 + 8.95*m.x57 + 8.85*m.x58
                        + 8.85*m.x59 + 8.85*m.x60 + 8.85*m.x61 - 0.08*m.x62 - 0.08*m.x63 - 0.08*m.x64 - 0.08*m.x65
                        - 0.91*m.x66 - 0.91*m.x67 - 0.91*m.x68 - 0.91*m.x69 - 0.83*m.x70 - 0.83*m.x71 - 0.83*m.x72
                        - 0.83*m.x73 + 8.6*m.x74 + 8.6*m.x75 + 8.6*m.x76 + 8.6*m.x77 + 9.16*m.x78 + 9.16*m.x79
                        + 9.16*m.x80 + 9.16*m.x81 - 0.96*m.x82 - 0.96*m.x83 - 0.96*m.x84 - 0.96*m.x85 - 0.77*m.x86
                        - 0.77*m.x87 - 0.77*m.x88 - 0.77*m.x89 - 0.87*m.x90 - 0.87*m.x91 - 0.87*m.x92 - 0.87*m.x93
                        + 9.2*m.x94 + 9.2*m.x95 + 9.2*m.x96 + 9.2*m.x97 + 8.8*m.x98 + 8.8*m.x99 + 8.8*m.x100
                        + 8.8*m.x101 - 0.91*m.x102 - 0.91*m.x103 - 0.91*m.x104 - 0.91*m.x105 - 0.26*m.x106 - 0.26*m.x107
                        - 0.26*m.x108 - 0.26*m.x109 - 0.14*m.x110 - 0.14*m.x111 - 0.14*m.x112 - 0.14*m.x113
                        + 9.02*m.x114 + 9.02*m.x115 + 9.02*m.x116 + 9.02*m.x117 + 9.46*m.x118 + 9.46*m.x119
                        + 9.46*m.x120 + 9.46*m.x121 - 0.35*m.b186 - 0.35*m.b187 - 0.35*m.b188 - 0.35*m.b189
                        - 0.59*m.b190 - 0.59*m.b191 - 0.59*m.b192 - 0.59*m.b193 - 0.92*m.b194 - 0.92*m.b195
                        - 0.92*m.b196 - 0.92*m.b197 - 0.76*m.b198 - 0.76*m.b199 - 0.76*m.b200 - 0.76*m.b201
                        - 0.38*m.b202 - 0.38*m.b203 - 0.38*m.b204 - 0.38*m.b205 - 0.08*m.b206 - 0.08*m.b207
                        - 0.08*m.b208 - 0.08*m.b209 - 0.53*m.b210 - 0.53*m.b211 - 0.53*m.b212 - 0.53*m.b213
                        - 0.93*m.b214 - 0.93*m.b215 - 0.93*m.b216 - 0.93*m.b217 - 0.57*m.b218 - 0.57*m.b219
                        - 0.57*m.b220 - 0.57*m.b221 - 0.01*m.b222 - 0.01*m.b223 - 0.01*m.b224 - 0.01*m.b225
                        - 0.16*m.b226 - 0.16*m.b227 - 0.16*m.b228 - 0.16*m.b229 - 0.31*m.b230 - 0.31*m.b231
                        - 0.31*m.b232 - 0.31*m.b233 - 0.17*m.b234 - 0.17*m.b235 - 0.17*m.b236 - 0.17*m.b237
                        - 0.26*m.b238 - 0.26*m.b239 - 0.26*m.b240 - 0.26*m.b241 - 0.69*m.b242 - 0.69*m.b243
                        - 0.69*m.b244 - 0.69*m.b245 - 0.45*m.b246 - 0.45*m.b247 - 0.45*m.b248 - 0.45*m.b249
                        - 0.23*m.b250 - 0.23*m.b251 - 0.23*m.b252 - 0.23*m.b253 - 0.15*m.b254 - 0.15*m.b255
                        - 0.15*m.b256 - 0.15*m.b257 - 0.54*m.b258 - 0.54*m.b259 - 0.54*m.b260 - 0.54*m.b261
                        - 0.08*m.b262 - 0.08*m.b263 - 0.08*m.b264 - 0.08*m.b265 - 0.11*m.b266 - 0.11*m.b267
                        - 0.11*m.b268 - 0.11*m.b269 - 0.82*m.b274 - 0.82*m.b275 - 0.82*m.b276 - 0.82*m.b277
                        - 0.08*m.b278 - 0.08*m.b279 - 0.08*m.b280 - 0.08*m.b281 - 0.26*m.b282 - 0.26*m.b283
                        - 0.26*m.b284 - 0.26*m.b285 - 0.43*m.b286 - 0.43*m.b287 - 0.43*m.b288 - 0.43*m.b289
                        - 0.18*m.b290 - 0.18*m.b291 - 0.18*m.b292 - 0.18*m.b293 - 0.15*m.b294 - 0.15*m.b295
                        - 0.15*m.b296 - 0.15*m.b297 - 0.87*m.b298 - 0.87*m.b299 - 0.87*m.b300 - 0.87*m.b301
                        - 0.55*m.b302 - 0.55*m.b303 - 0.55*m.b304 - 0.55*m.b305, sense=maximize)

m.c2 = Constraint(expr=   m.x2 + m.x6 + m.x10 + m.x14 + m.x18 + m.x154 == 1.9)

m.c3 = Constraint(expr=   m.x22 + m.x26 + m.x30 + m.x34 + m.x38 + m.x158 == 1.8)

m.c4 = Constraint(expr= - m.x2 + m.x42 + m.x46 + m.x50 + m.x54 + m.x58 - m.x62 - m.x82 - m.x102 + m.x162 == 0.3)

m.c5 = Constraint(expr= - m.x6 - m.x22 - m.x42 + m.x62 + m.x66 + m.x70 + m.x74 + m.x78 - m.x86 - m.x106 + m.x166 == 1.8)

m.c6 = Constraint(expr= - m.x10 - m.x26 - m.x46 - m.x66 + m.x82 + m.x86 + m.x90 + m.x94 + m.x98 - m.x110 + m.x170
                        == 1.3)

m.c7 = Constraint(expr= - m.x14 - m.x30 - m.x50 - m.x70 - m.x90 + m.x102 + m.x106 + m.x110 + m.x114 + m.x118 + m.x174
                        == 0.2)

m.c8 = Constraint(expr= - m.x18 - m.x34 - m.x54 - m.x74 - m.x94 - m.x114 + m.x178 == 0.16)

m.c9 = Constraint(expr= - m.x38 - m.x58 - m.x78 - m.x98 - m.x118 + m.x182 == 0.72)

m.c10 = Constraint(expr=m.x122*m.x162 - 0.7*m.x2 + 0.7*m.x42 + 0.7*m.x46 + 0.7*m.x50 + 0.7*m.x54 + 0.7*m.x58 - 0.8*m.x62
                         - 0.7*m.x82 - 0.7*m.x102 == 0.21)

m.c11 = Constraint(expr=m.x126*m.x166 - 0.7*m.x6 - 0.9*m.x22 - 0.7*m.x42 + 0.8*m.x62 + 0.8*m.x66 + 0.8*m.x70 + 0.8*m.x74
                         + 0.8*m.x78 - 0.7*m.x86 - 0.7*m.x106 == 1.44)

m.c12 = Constraint(expr=m.x130*m.x170 - 0.7*m.x10 - 0.9*m.x26 - 0.7*m.x46 - 0.8*m.x66 + 0.7*m.x82 + 0.7*m.x86
                         + 0.7*m.x90 + 0.7*m.x94 + 0.7*m.x98 - 0.7*m.x110 == 0.91)

m.c13 = Constraint(expr=m.x134*m.x174 - 0.7*m.x14 - 0.9*m.x30 - 0.7*m.x50 - 0.8*m.x70 - 0.7*m.x90 + 0.7*m.x102
                         + 0.7*m.x106 + 0.7*m.x110 + 0.7*m.x114 + 0.7*m.x118 == 0.14)

m.c14 = Constraint(expr=m.x138*m.x162 - 0.2*m.x2 - 0.9*m.x62 - 0.8*m.x82 - 0.4*m.x102 == 0)

m.c15 = Constraint(expr=m.x142*m.x166 - 0.2*m.x6 - 0.8*m.x22 + 0.9*m.x62 + 0.9*m.x66 + 0.9*m.x70 + 0.9*m.x74 + 0.9*m.x78
                         - 0.8*m.x86 - 0.4*m.x106 == 1.62)

m.c16 = Constraint(expr=m.x146*m.x170 - 0.2*m.x10 - 0.8*m.x26 - 0.9*m.x66 + 0.8*m.x82 + 0.8*m.x86 + 0.8*m.x90
                         + 0.8*m.x94 + 0.8*m.x98 - 0.4*m.x110 == 1.04)

m.c17 = Constraint(expr=m.x150*m.x174 - 0.2*m.x14 - 0.8*m.x30 - 0.9*m.x70 - 0.8*m.x90 + 0.4*m.x102 + 0.4*m.x106
                         + 0.4*m.x110 + 0.4*m.x114 + 0.4*m.x118 == 0.08)

m.c18 = Constraint(expr=   m.x3 + m.x7 + m.x11 + m.x15 + m.x19 - m.x154 + m.x155 == 0.1)

m.c19 = Constraint(expr=   m.x4 + m.x8 + m.x12 + m.x16 + m.x20 - m.x155 + m.x156 == 0.7)

m.c20 = Constraint(expr=   m.x5 + m.x9 + m.x13 + m.x17 + m.x21 - m.x156 + m.x157 == 1)

m.c21 = Constraint(expr=   m.x23 + m.x27 + m.x31 + m.x35 + m.x39 - m.x158 + m.x159 == 0.8)

m.c22 = Constraint(expr=   m.x24 + m.x28 + m.x32 + m.x36 + m.x40 - m.x159 + m.x160 == 0.3)

m.c23 = Constraint(expr=   m.x25 + m.x29 + m.x33 + m.x37 + m.x41 - m.x160 + m.x161 == 0)

m.c24 = Constraint(expr= - m.x3 + m.x43 + m.x47 + m.x51 + m.x55 + m.x59 - m.x63 - m.x83 - m.x103 - m.x162 + m.x163 == 0)

m.c25 = Constraint(expr= - m.x4 + m.x44 + m.x48 + m.x52 + m.x56 + m.x60 - m.x64 - m.x84 - m.x104 - m.x163 + m.x164 == 0)

m.c26 = Constraint(expr= - m.x5 + m.x45 + m.x49 + m.x53 + m.x57 + m.x61 - m.x65 - m.x85 - m.x105 - m.x164 + m.x165 == 0)

m.c27 = Constraint(expr= - m.x7 - m.x23 - m.x43 + m.x63 + m.x67 + m.x71 + m.x75 + m.x79 - m.x87 - m.x107 - m.x166
                         + m.x167 == 0)

m.c28 = Constraint(expr= - m.x8 - m.x24 - m.x44 + m.x64 + m.x68 + m.x72 + m.x76 + m.x80 - m.x88 - m.x108 - m.x167
                         + m.x168 == 0)

m.c29 = Constraint(expr= - m.x9 - m.x25 - m.x45 + m.x65 + m.x69 + m.x73 + m.x77 + m.x81 - m.x89 - m.x109 - m.x168
                         + m.x169 == 0)

m.c30 = Constraint(expr= - m.x11 - m.x27 - m.x47 - m.x67 + m.x83 + m.x87 + m.x91 + m.x95 + m.x99 - m.x111 - m.x170
                         + m.x171 == 0)

m.c31 = Constraint(expr= - m.x12 - m.x28 - m.x48 - m.x68 + m.x84 + m.x88 + m.x92 + m.x96 + m.x100 - m.x112 - m.x171
                         + m.x172 == 0)

m.c32 = Constraint(expr= - m.x13 - m.x29 - m.x49 - m.x69 + m.x85 + m.x89 + m.x93 + m.x97 + m.x101 - m.x113 - m.x172
                         + m.x173 == 0)

m.c33 = Constraint(expr= - m.x15 - m.x31 - m.x51 - m.x71 - m.x91 + m.x103 + m.x107 + m.x111 + m.x115 + m.x119 - m.x174
                         + m.x175 == 0)

m.c34 = Constraint(expr= - m.x16 - m.x32 - m.x52 - m.x72 - m.x92 + m.x104 + m.x108 + m.x112 + m.x116 + m.x120 - m.x175
                         + m.x176 == 0)

m.c35 = Constraint(expr= - m.x17 - m.x33 - m.x53 - m.x73 - m.x93 + m.x105 + m.x109 + m.x113 + m.x117 + m.x121 - m.x176
                         + m.x177 == 0)

m.c36 = Constraint(expr= - m.x19 - m.x35 - m.x55 - m.x75 - m.x95 - m.x115 - m.x178 + m.x179 == -0.77)

m.c37 = Constraint(expr= - m.x20 - m.x36 - m.x56 - m.x76 - m.x96 - m.x116 - m.x179 + m.x180 == -0.19)

m.c38 = Constraint(expr= - m.x21 - m.x37 - m.x57 - m.x77 - m.x97 - m.x117 - m.x180 + m.x181 == -0.45)

m.c39 = Constraint(expr= - m.x39 - m.x59 - m.x79 - m.x99 - m.x119 - m.x182 + m.x183 == -0.8)

m.c40 = Constraint(expr= - m.x40 - m.x60 - m.x80 - m.x100 - m.x120 - m.x183 + m.x184 == -0.49)

m.c41 = Constraint(expr= - m.x41 - m.x61 - m.x81 - m.x101 - m.x121 - m.x184 + m.x185 == -0.65)

m.c42 = Constraint(expr=m.x123*m.x163 - (m.x122*m.x162 + m.x126*m.x63 + m.x130*m.x83 + m.x134*m.x103 - (m.x122*m.x43 + 
                        m.x122*m.x47 + m.x122*m.x51 + m.x122*m.x55 + m.x122*m.x59)) - 0.7*m.x3 == 0)

m.c43 = Constraint(expr=m.x124*m.x164 - (m.x123*m.x163 + m.x127*m.x64 + m.x131*m.x84 + m.x135*m.x104 - (m.x123*m.x44 + 
                        m.x123*m.x48 + m.x123*m.x52 + m.x123*m.x56 + m.x123*m.x60)) - 0.7*m.x4 == 0)

m.c44 = Constraint(expr=m.x125*m.x165 - (m.x124*m.x164 + m.x128*m.x65 + m.x132*m.x85 + m.x136*m.x105 - (m.x124*m.x45 + 
                        m.x124*m.x49 + m.x124*m.x53 + m.x124*m.x57 + m.x124*m.x61)) - 0.7*m.x5 == 0)

m.c45 = Constraint(expr=m.x127*m.x167 - (m.x126*m.x166 + m.x122*m.x43 + m.x130*m.x87 + m.x134*m.x107 - (m.x126*m.x63 + 
                        m.x126*m.x67 + m.x126*m.x71 + m.x126*m.x75 + m.x126*m.x79)) - 0.7*m.x7 - 0.9*m.x23 == 0)

m.c46 = Constraint(expr=m.x128*m.x168 - (m.x127*m.x167 + m.x123*m.x44 + m.x131*m.x88 + m.x135*m.x108 - (m.x127*m.x64 + 
                        m.x127*m.x68 + m.x127*m.x72 + m.x127*m.x76 + m.x127*m.x80)) - 0.7*m.x8 - 0.9*m.x24 == 0)

m.c47 = Constraint(expr=m.x129*m.x169 - (m.x128*m.x168 + m.x124*m.x45 + m.x132*m.x89 + m.x136*m.x109 - (m.x128*m.x65 + 
                        m.x128*m.x69 + m.x128*m.x73 + m.x128*m.x77 + m.x128*m.x81)) - 0.7*m.x9 - 0.9*m.x25 == 0)

m.c48 = Constraint(expr=m.x131*m.x171 - (m.x130*m.x170 + m.x122*m.x47 + m.x126*m.x67 + m.x134*m.x111 - (m.x130*m.x83 + 
                        m.x130*m.x87 + m.x130*m.x91 + m.x130*m.x95 + m.x130*m.x99)) - 0.7*m.x11 - 0.9*m.x27 == 0)

m.c49 = Constraint(expr=m.x132*m.x172 - (m.x131*m.x171 + m.x123*m.x48 + m.x127*m.x68 + m.x135*m.x112 - (m.x131*m.x84 + 
                        m.x131*m.x88 + m.x131*m.x92 + m.x131*m.x96 + m.x131*m.x100)) - 0.7*m.x12 - 0.9*m.x28 == 0)

m.c50 = Constraint(expr=m.x133*m.x173 - (m.x132*m.x172 + m.x124*m.x49 + m.x128*m.x69 + m.x136*m.x113 - (m.x132*m.x85 + 
                        m.x132*m.x89 + m.x132*m.x93 + m.x132*m.x97 + m.x132*m.x101)) - 0.7*m.x13 - 0.9*m.x29 == 0)

m.c51 = Constraint(expr=m.x135*m.x175 - (m.x134*m.x174 + m.x122*m.x51 + m.x126*m.x71 + m.x130*m.x91 - (m.x134*m.x103 + 
                        m.x134*m.x107 + m.x134*m.x111 + m.x134*m.x115 + m.x134*m.x119)) - 0.7*m.x15 - 0.9*m.x31 == 0)

m.c52 = Constraint(expr=m.x136*m.x176 - (m.x135*m.x175 + m.x123*m.x52 + m.x127*m.x72 + m.x131*m.x92 - (m.x135*m.x104 + 
                        m.x135*m.x108 + m.x135*m.x112 + m.x135*m.x116 + m.x135*m.x120)) - 0.7*m.x16 - 0.9*m.x32 == 0)

m.c53 = Constraint(expr=m.x137*m.x177 - (m.x136*m.x176 + m.x124*m.x53 + m.x128*m.x73 + m.x132*m.x93 - (m.x136*m.x105 + 
                        m.x136*m.x109 + m.x136*m.x113 + m.x136*m.x117 + m.x136*m.x121)) - 0.7*m.x17 - 0.9*m.x33 == 0)

m.c54 = Constraint(expr=m.x139*m.x163 - (m.x138*m.x162 + m.x142*m.x63 + m.x146*m.x83 + m.x150*m.x103 - (m.x138*m.x43 + 
                        m.x138*m.x47 + m.x138*m.x51 + m.x138*m.x55 + m.x138*m.x59)) - 0.2*m.x3 == 0)

m.c55 = Constraint(expr=m.x140*m.x164 - (m.x139*m.x163 + m.x143*m.x64 + m.x147*m.x84 + m.x151*m.x104 - (m.x139*m.x44 + 
                        m.x139*m.x48 + m.x139*m.x52 + m.x139*m.x56 + m.x139*m.x60)) - 0.2*m.x4 == 0)

m.c56 = Constraint(expr=m.x141*m.x165 - (m.x140*m.x164 + m.x144*m.x65 + m.x148*m.x85 + m.x152*m.x105 - (m.x140*m.x45 + 
                        m.x140*m.x49 + m.x140*m.x53 + m.x140*m.x57 + m.x140*m.x61)) - 0.2*m.x5 == 0)

m.c57 = Constraint(expr=m.x143*m.x167 - (m.x142*m.x166 + m.x138*m.x43 + m.x146*m.x87 + m.x150*m.x107 - (m.x142*m.x63 + 
                        m.x142*m.x67 + m.x142*m.x71 + m.x142*m.x75 + m.x142*m.x79)) - 0.2*m.x7 - 0.8*m.x23 == 0)

m.c58 = Constraint(expr=m.x144*m.x168 - (m.x143*m.x167 + m.x139*m.x44 + m.x147*m.x88 + m.x151*m.x108 - (m.x143*m.x64 + 
                        m.x143*m.x68 + m.x143*m.x72 + m.x143*m.x76 + m.x143*m.x80)) - 0.2*m.x8 - 0.8*m.x24 == 0)

m.c59 = Constraint(expr=m.x145*m.x169 - (m.x144*m.x168 + m.x140*m.x45 + m.x148*m.x89 + m.x152*m.x109 - (m.x144*m.x65 + 
                        m.x144*m.x69 + m.x144*m.x73 + m.x144*m.x77 + m.x144*m.x81)) - 0.2*m.x9 - 0.8*m.x25 == 0)

m.c60 = Constraint(expr=m.x147*m.x171 - (m.x146*m.x170 + m.x138*m.x47 + m.x142*m.x67 + m.x150*m.x111 - (m.x146*m.x83 + 
                        m.x146*m.x87 + m.x146*m.x91 + m.x146*m.x95 + m.x146*m.x99)) - 0.2*m.x11 - 0.8*m.x27 == 0)

m.c61 = Constraint(expr=m.x148*m.x172 - (m.x147*m.x171 + m.x139*m.x48 + m.x143*m.x68 + m.x151*m.x112 - (m.x147*m.x84 + 
                        m.x147*m.x88 + m.x147*m.x92 + m.x147*m.x96 + m.x147*m.x100)) - 0.2*m.x12 - 0.8*m.x28 == 0)

m.c62 = Constraint(expr=m.x149*m.x173 - (m.x148*m.x172 + m.x140*m.x49 + m.x144*m.x69 + m.x152*m.x113 - (m.x148*m.x85 + 
                        m.x148*m.x89 + m.x148*m.x93 + m.x148*m.x97 + m.x148*m.x101)) - 0.2*m.x13 - 0.8*m.x29 == 0)

m.c63 = Constraint(expr=m.x151*m.x175 - (m.x150*m.x174 + m.x138*m.x51 + m.x142*m.x71 + m.x146*m.x91 - (m.x150*m.x103 + 
                        m.x150*m.x107 + m.x150*m.x111 + m.x150*m.x115 + m.x150*m.x119)) - 0.2*m.x15 - 0.8*m.x31 == 0)

m.c64 = Constraint(expr=m.x152*m.x176 - (m.x151*m.x175 + m.x139*m.x52 + m.x143*m.x72 + m.x147*m.x92 - (m.x151*m.x104 + 
                        m.x151*m.x108 + m.x151*m.x112 + m.x151*m.x116 + m.x151*m.x120)) - 0.2*m.x16 - 0.8*m.x32 == 0)

m.c65 = Constraint(expr=m.x153*m.x177 - (m.x152*m.x176 + m.x140*m.x53 + m.x144*m.x73 + m.x148*m.x93 - (m.x152*m.x105 + 
                        m.x152*m.x109 + m.x152*m.x113 + m.x152*m.x117 + m.x152*m.x121)) - 0.2*m.x17 - 0.8*m.x33 == 0)

m.c66 = Constraint(expr=   m.x2 - m.b186 <= 0)

m.c67 = Constraint(expr=   m.x3 - m.b187 <= 0)

m.c68 = Constraint(expr=   m.x4 - m.b188 <= 0)

m.c69 = Constraint(expr=   m.x5 - m.b189 <= 0)

m.c70 = Constraint(expr=   m.x6 - m.b190 <= 0)

m.c71 = Constraint(expr=   m.x7 - m.b191 <= 0)

m.c72 = Constraint(expr=   m.x8 - m.b192 <= 0)

m.c73 = Constraint(expr=   m.x9 - m.b193 <= 0)

m.c74 = Constraint(expr=   m.x10 - m.b194 <= 0)

m.c75 = Constraint(expr=   m.x11 - m.b195 <= 0)

m.c76 = Constraint(expr=   m.x12 - m.b196 <= 0)

m.c77 = Constraint(expr=   m.x13 - m.b197 <= 0)

m.c78 = Constraint(expr=   m.x14 - m.b198 <= 0)

m.c79 = Constraint(expr=   m.x15 - m.b199 <= 0)

m.c80 = Constraint(expr=   m.x16 - m.b200 <= 0)

m.c81 = Constraint(expr=   m.x17 - m.b201 <= 0)

m.c82 = Constraint(expr=   m.x18 - m.b202 <= 0)

m.c83 = Constraint(expr=   m.x19 - m.b203 <= 0)

m.c84 = Constraint(expr=   m.x20 - m.b204 <= 0)

m.c85 = Constraint(expr=   m.x21 - m.b205 <= 0)

m.c86 = Constraint(expr=   m.x22 - m.b206 <= 0)

m.c87 = Constraint(expr=   m.x23 - m.b207 <= 0)

m.c88 = Constraint(expr=   m.x24 - m.b208 <= 0)

m.c89 = Constraint(expr=   m.x25 - m.b209 <= 0)

m.c90 = Constraint(expr=   m.x26 - m.b210 <= 0)

m.c91 = Constraint(expr=   m.x27 - m.b211 <= 0)

m.c92 = Constraint(expr=   m.x28 - m.b212 <= 0)

m.c93 = Constraint(expr=   m.x29 - m.b213 <= 0)

m.c94 = Constraint(expr=   m.x30 - m.b214 <= 0)

m.c95 = Constraint(expr=   m.x31 - m.b215 <= 0)

m.c96 = Constraint(expr=   m.x32 - m.b216 <= 0)

m.c97 = Constraint(expr=   m.x33 - m.b217 <= 0)

m.c98 = Constraint(expr=   m.x34 - m.b218 <= 0)

m.c99 = Constraint(expr=   m.x35 - m.b219 <= 0)

m.c100 = Constraint(expr=   m.x36 - m.b220 <= 0)

m.c101 = Constraint(expr=   m.x37 - m.b221 <= 0)

m.c102 = Constraint(expr=   m.x38 - m.b222 <= 0)

m.c103 = Constraint(expr=   m.x39 - m.b223 <= 0)

m.c104 = Constraint(expr=   m.x40 - m.b224 <= 0)

m.c105 = Constraint(expr=   m.x41 - m.b225 <= 0)

m.c106 = Constraint(expr=   m.x42 - m.b226 <= 0)

m.c107 = Constraint(expr=   m.x43 - m.b227 <= 0)

m.c108 = Constraint(expr=   m.x44 - m.b228 <= 0)

m.c109 = Constraint(expr=   m.x45 - m.b229 <= 0)

m.c110 = Constraint(expr=   m.x46 - m.b230 <= 0)

m.c111 = Constraint(expr=   m.x47 - m.b231 <= 0)

m.c112 = Constraint(expr=   m.x48 - m.b232 <= 0)

m.c113 = Constraint(expr=   m.x49 - m.b233 <= 0)

m.c114 = Constraint(expr=   m.x50 - m.b234 <= 0)

m.c115 = Constraint(expr=   m.x51 - m.b235 <= 0)

m.c116 = Constraint(expr=   m.x52 - m.b236 <= 0)

m.c117 = Constraint(expr=   m.x53 - m.b237 <= 0)

m.c118 = Constraint(expr=   m.x54 - m.b238 <= 0)

m.c119 = Constraint(expr=   m.x55 - m.b239 <= 0)

m.c120 = Constraint(expr=   m.x56 - m.b240 <= 0)

m.c121 = Constraint(expr=   m.x57 - m.b241 <= 0)

m.c122 = Constraint(expr=   m.x58 - m.b242 <= 0)

m.c123 = Constraint(expr=   m.x59 - m.b243 <= 0)

m.c124 = Constraint(expr=   m.x60 - m.b244 <= 0)

m.c125 = Constraint(expr=   m.x61 - m.b245 <= 0)

m.c126 = Constraint(expr=   m.x62 - m.b246 <= 0)

m.c127 = Constraint(expr=   m.x63 - m.b247 <= 0)

m.c128 = Constraint(expr=   m.x64 - m.b248 <= 0)

m.c129 = Constraint(expr=   m.x65 - m.b249 <= 0)

m.c130 = Constraint(expr=   m.x66 - m.b250 <= 0)

m.c131 = Constraint(expr=   m.x67 - m.b251 <= 0)

m.c132 = Constraint(expr=   m.x68 - m.b252 <= 0)

m.c133 = Constraint(expr=   m.x69 - m.b253 <= 0)

m.c134 = Constraint(expr=   m.x70 - m.b254 <= 0)

m.c135 = Constraint(expr=   m.x71 - m.b255 <= 0)

m.c136 = Constraint(expr=   m.x72 - m.b256 <= 0)

m.c137 = Constraint(expr=   m.x73 - m.b257 <= 0)

m.c138 = Constraint(expr=   m.x74 - m.b258 <= 0)

m.c139 = Constraint(expr=   m.x75 - m.b259 <= 0)

m.c140 = Constraint(expr=   m.x76 - m.b260 <= 0)

m.c141 = Constraint(expr=   m.x77 - m.b261 <= 0)

m.c142 = Constraint(expr=   m.x78 - m.b262 <= 0)

m.c143 = Constraint(expr=   m.x79 - m.b263 <= 0)

m.c144 = Constraint(expr=   m.x80 - m.b264 <= 0)

m.c145 = Constraint(expr=   m.x81 - m.b265 <= 0)

m.c146 = Constraint(expr=   m.x82 - m.b266 <= 0)

m.c147 = Constraint(expr=   m.x83 - m.b267 <= 0)

m.c148 = Constraint(expr=   m.x84 - m.b268 <= 0)

m.c149 = Constraint(expr=   m.x85 - m.b269 <= 0)

m.c150 = Constraint(expr=   m.x86 - m.b270 <= 0)

m.c151 = Constraint(expr=   m.x87 - m.b271 <= 0)

m.c152 = Constraint(expr=   m.x88 - m.b272 <= 0)

m.c153 = Constraint(expr=   m.x89 - m.b273 <= 0)

m.c154 = Constraint(expr=   m.x90 - m.b274 <= 0)

m.c155 = Constraint(expr=   m.x91 - m.b275 <= 0)

m.c156 = Constraint(expr=   m.x92 - m.b276 <= 0)

m.c157 = Constraint(expr=   m.x93 - m.b277 <= 0)

m.c158 = Constraint(expr=   m.x94 - m.b278 <= 0)

m.c159 = Constraint(expr=   m.x95 - m.b279 <= 0)

m.c160 = Constraint(expr=   m.x96 - m.b280 <= 0)

m.c161 = Constraint(expr=   m.x97 - m.b281 <= 0)

m.c162 = Constraint(expr=   m.x98 - m.b282 <= 0)

m.c163 = Constraint(expr=   m.x99 - m.b283 <= 0)

m.c164 = Constraint(expr=   m.x100 - m.b284 <= 0)

m.c165 = Constraint(expr=   m.x101 - m.b285 <= 0)

m.c166 = Constraint(expr=   m.x102 - m.b286 <= 0)

m.c167 = Constraint(expr=   m.x103 - m.b287 <= 0)

m.c168 = Constraint(expr=   m.x104 - m.b288 <= 0)

m.c169 = Constraint(expr=   m.x105 - m.b289 <= 0)

m.c170 = Constraint(expr=   m.x106 - m.b290 <= 0)

m.c171 = Constraint(expr=   m.x107 - m.b291 <= 0)

m.c172 = Constraint(expr=   m.x108 - m.b292 <= 0)

m.c173 = Constraint(expr=   m.x109 - m.b293 <= 0)

m.c174 = Constraint(expr=   m.x110 - m.b294 <= 0)

m.c175 = Constraint(expr=   m.x111 - m.b295 <= 0)

m.c176 = Constraint(expr=   m.x112 - m.b296 <= 0)

m.c177 = Constraint(expr=   m.x113 - m.b297 <= 0)

m.c178 = Constraint(expr=   m.x114 - m.b298 <= 0)

m.c179 = Constraint(expr=   m.x115 - m.b299 <= 0)

m.c180 = Constraint(expr=   m.x116 - m.b300 <= 0)

m.c181 = Constraint(expr=   m.x117 - m.b301 <= 0)

m.c182 = Constraint(expr=   m.x118 - m.b302 <= 0)

m.c183 = Constraint(expr=   m.x119 - m.b303 <= 0)

m.c184 = Constraint(expr=   m.x120 - m.b304 <= 0)

m.c185 = Constraint(expr=   m.x121 - m.b305 <= 0)

m.c186 = Constraint(expr=   m.x2 >= 0)

m.c187 = Constraint(expr=   m.x3 >= 0)

m.c188 = Constraint(expr=   m.x4 >= 0)

m.c189 = Constraint(expr=   m.x5 >= 0)

m.c190 = Constraint(expr=   m.x6 >= 0)

m.c191 = Constraint(expr=   m.x7 >= 0)

m.c192 = Constraint(expr=   m.x8 >= 0)

m.c193 = Constraint(expr=   m.x9 >= 0)

m.c194 = Constraint(expr=   m.x10 >= 0)

m.c195 = Constraint(expr=   m.x11 >= 0)

m.c196 = Constraint(expr=   m.x12 >= 0)

m.c197 = Constraint(expr=   m.x13 >= 0)

m.c198 = Constraint(expr=   m.x14 >= 0)

m.c199 = Constraint(expr=   m.x15 >= 0)

m.c200 = Constraint(expr=   m.x16 >= 0)

m.c201 = Constraint(expr=   m.x17 >= 0)

m.c202 = Constraint(expr=   m.x18 >= 0)

m.c203 = Constraint(expr=   m.x19 >= 0)

m.c204 = Constraint(expr=   m.x20 >= 0)

m.c205 = Constraint(expr=   m.x21 >= 0)

m.c206 = Constraint(expr=   m.x22 >= 0)

m.c207 = Constraint(expr=   m.x23 >= 0)

m.c208 = Constraint(expr=   m.x24 >= 0)

m.c209 = Constraint(expr=   m.x25 >= 0)

m.c210 = Constraint(expr=   m.x26 >= 0)

m.c211 = Constraint(expr=   m.x27 >= 0)

m.c212 = Constraint(expr=   m.x28 >= 0)

m.c213 = Constraint(expr=   m.x29 >= 0)

m.c214 = Constraint(expr=   m.x30 >= 0)

m.c215 = Constraint(expr=   m.x31 >= 0)

m.c216 = Constraint(expr=   m.x32 >= 0)

m.c217 = Constraint(expr=   m.x33 >= 0)

m.c218 = Constraint(expr=   m.x34 >= 0)

m.c219 = Constraint(expr=   m.x35 >= 0)

m.c220 = Constraint(expr=   m.x36 >= 0)

m.c221 = Constraint(expr=   m.x37 >= 0)

m.c222 = Constraint(expr=   m.x38 >= 0)

m.c223 = Constraint(expr=   m.x39 >= 0)

m.c224 = Constraint(expr=   m.x40 >= 0)

m.c225 = Constraint(expr=   m.x41 >= 0)

m.c226 = Constraint(expr=   m.x42 >= 0)

m.c227 = Constraint(expr=   m.x43 >= 0)

m.c228 = Constraint(expr=   m.x44 >= 0)

m.c229 = Constraint(expr=   m.x45 >= 0)

m.c230 = Constraint(expr=   m.x46 >= 0)

m.c231 = Constraint(expr=   m.x47 >= 0)

m.c232 = Constraint(expr=   m.x48 >= 0)

m.c233 = Constraint(expr=   m.x49 >= 0)

m.c234 = Constraint(expr=   m.x50 >= 0)

m.c235 = Constraint(expr=   m.x51 >= 0)

m.c236 = Constraint(expr=   m.x52 >= 0)

m.c237 = Constraint(expr=   m.x53 >= 0)

m.c238 = Constraint(expr=   m.x54 >= 0)

m.c239 = Constraint(expr=   m.x55 >= 0)

m.c240 = Constraint(expr=   m.x56 >= 0)

m.c241 = Constraint(expr=   m.x57 >= 0)

m.c242 = Constraint(expr=   m.x58 >= 0)

m.c243 = Constraint(expr=   m.x59 >= 0)

m.c244 = Constraint(expr=   m.x60 >= 0)

m.c245 = Constraint(expr=   m.x61 >= 0)

m.c246 = Constraint(expr=   m.x62 >= 0)

m.c247 = Constraint(expr=   m.x63 >= 0)

m.c248 = Constraint(expr=   m.x64 >= 0)

m.c249 = Constraint(expr=   m.x65 >= 0)

m.c250 = Constraint(expr=   m.x66 >= 0)

m.c251 = Constraint(expr=   m.x67 >= 0)

m.c252 = Constraint(expr=   m.x68 >= 0)

m.c253 = Constraint(expr=   m.x69 >= 0)

m.c254 = Constraint(expr=   m.x70 >= 0)

m.c255 = Constraint(expr=   m.x71 >= 0)

m.c256 = Constraint(expr=   m.x72 >= 0)

m.c257 = Constraint(expr=   m.x73 >= 0)

m.c258 = Constraint(expr=   m.x74 >= 0)

m.c259 = Constraint(expr=   m.x75 >= 0)

m.c260 = Constraint(expr=   m.x76 >= 0)

m.c261 = Constraint(expr=   m.x77 >= 0)

m.c262 = Constraint(expr=   m.x78 >= 0)

m.c263 = Constraint(expr=   m.x79 >= 0)

m.c264 = Constraint(expr=   m.x80 >= 0)

m.c265 = Constraint(expr=   m.x81 >= 0)

m.c266 = Constraint(expr=   m.x82 >= 0)

m.c267 = Constraint(expr=   m.x83 >= 0)

m.c268 = Constraint(expr=   m.x84 >= 0)

m.c269 = Constraint(expr=   m.x85 >= 0)

m.c270 = Constraint(expr=   m.x86 >= 0)

m.c271 = Constraint(expr=   m.x87 >= 0)

m.c272 = Constraint(expr=   m.x88 >= 0)

m.c273 = Constraint(expr=   m.x89 >= 0)

m.c274 = Constraint(expr=   m.x90 >= 0)

m.c275 = Constraint(expr=   m.x91 >= 0)

m.c276 = Constraint(expr=   m.x92 >= 0)

m.c277 = Constraint(expr=   m.x93 >= 0)

m.c278 = Constraint(expr=   m.x94 >= 0)

m.c279 = Constraint(expr=   m.x95 >= 0)

m.c280 = Constraint(expr=   m.x96 >= 0)

m.c281 = Constraint(expr=   m.x97 >= 0)

m.c282 = Constraint(expr=   m.x98 >= 0)

m.c283 = Constraint(expr=   m.x99 >= 0)

m.c284 = Constraint(expr=   m.x100 >= 0)

m.c285 = Constraint(expr=   m.x101 >= 0)

m.c286 = Constraint(expr=   m.x102 >= 0)

m.c287 = Constraint(expr=   m.x103 >= 0)

m.c288 = Constraint(expr=   m.x104 >= 0)

m.c289 = Constraint(expr=   m.x105 >= 0)

m.c290 = Constraint(expr=   m.x106 >= 0)

m.c291 = Constraint(expr=   m.x107 >= 0)

m.c292 = Constraint(expr=   m.x108 >= 0)

m.c293 = Constraint(expr=   m.x109 >= 0)

m.c294 = Constraint(expr=   m.x110 >= 0)

m.c295 = Constraint(expr=   m.x111 >= 0)

m.c296 = Constraint(expr=   m.x112 >= 0)

m.c297 = Constraint(expr=   m.x113 >= 0)

m.c298 = Constraint(expr=   m.x114 >= 0)

m.c299 = Constraint(expr=   m.x115 >= 0)

m.c300 = Constraint(expr=   m.x116 >= 0)

m.c301 = Constraint(expr=   m.x117 >= 0)

m.c302 = Constraint(expr=   m.x118 >= 0)

m.c303 = Constraint(expr=   m.x119 >= 0)

m.c304 = Constraint(expr=   m.x120 >= 0)

m.c305 = Constraint(expr=   m.x121 >= 0)

m.c306 = Constraint(expr=   m.b202 <= 1.1)

m.c307 = Constraint(expr=   m.b203 <= 1.1)

m.c308 = Constraint(expr=   m.b204 <= 1.1)

m.c309 = Constraint(expr=   m.b205 <= 1.1)

m.c310 = Constraint(expr=   m.b218 <= 1.3)

m.c311 = Constraint(expr=   m.b219 <= 1.3)

m.c312 = Constraint(expr=   m.b220 <= 1.3)

m.c313 = Constraint(expr=   m.b221 <= 1.3)

m.c314 = Constraint(expr=   m.b222 <= 1.1)

m.c315 = Constraint(expr=   m.b223 <= 1.1)

m.c316 = Constraint(expr=   m.b224 <= 1.1)

m.c317 = Constraint(expr=   m.b225 <= 1.1)

m.c318 = Constraint(expr=   m.b202 <= 0.7)

m.c319 = Constraint(expr=   m.b203 <= 0.7)

m.c320 = Constraint(expr=   m.b204 <= 0.7)

m.c321 = Constraint(expr=   m.b205 <= 0.7)

m.c322 = Constraint(expr=   m.b218 <= 1.3)

m.c323 = Constraint(expr=   m.b219 <= 1.3)

m.c324 = Constraint(expr=   m.b220 <= 1.3)

m.c325 = Constraint(expr=   m.b221 <= 1.3)

m.c326 = Constraint(expr=   m.b222 <= 1.7)

m.c327 = Constraint(expr=   m.b223 <= 1.7)

m.c328 = Constraint(expr=   m.b224 <= 1.7)

m.c329 = Constraint(expr=   m.b225 <= 1.7)

m.c330 = Constraint(expr= - m.b202 >= -1.3)

m.c331 = Constraint(expr= - m.b203 >= -1.3)

m.c332 = Constraint(expr= - m.b204 >= -1.3)

m.c333 = Constraint(expr= - m.b205 >= -1.3)

m.c334 = Constraint(expr= - m.b218 >= -1.1)

m.c335 = Constraint(expr= - m.b219 >= -1.1)

m.c336 = Constraint(expr= - m.b220 >= -1.1)

m.c337 = Constraint(expr= - m.b221 >= -1.1)

m.c338 = Constraint(expr= - m.b222 >= -1.1)

m.c339 = Constraint(expr= - m.b223 >= -1.1)

m.c340 = Constraint(expr= - m.b224 >= -1.1)

m.c341 = Constraint(expr= - m.b225 >= -1.1)

m.c342 = Constraint(expr= - m.b202 >= -1.7)

m.c343 = Constraint(expr= - m.b203 >= -1.7)

m.c344 = Constraint(expr= - m.b204 >= -1.7)

m.c345 = Constraint(expr= - m.b205 >= -1.7)

m.c346 = Constraint(expr= - m.b218 >= -1.1)

m.c347 = Constraint(expr= - m.b219 >= -1.1)

m.c348 = Constraint(expr= - m.b220 >= -1.1)

m.c349 = Constraint(expr= - m.b221 >= -1.1)

m.c350 = Constraint(expr= - m.b222 >= -1.2)

m.c351 = Constraint(expr= - m.b223 >= -1.2)

m.c352 = Constraint(expr= - m.b224 >= -1.2)

m.c353 = Constraint(expr= - m.b225 >= -1.2)

m.c354 = Constraint(expr= - m.x122 + m.b239 <= 0.4)

m.c355 = Constraint(expr= - m.x123 + m.b240 <= 0.4)

m.c356 = Constraint(expr= - m.x124 + m.b241 <= 0.4)

m.c357 = Constraint(expr= - m.x122 + m.b243 <= 0.2)

m.c358 = Constraint(expr= - m.x123 + m.b244 <= 0.2)

m.c359 = Constraint(expr= - m.x124 + m.b245 <= 0.2)

m.c360 = Constraint(expr= - m.x126 + m.b259 <= 0.4)

m.c361 = Constraint(expr= - m.x127 + m.b260 <= 0.4)

m.c362 = Constraint(expr= - m.x128 + m.b261 <= 0.4)

m.c363 = Constraint(expr= - m.x126 + m.b263 <= 0.2)

m.c364 = Constraint(expr= - m.x127 + m.b264 <= 0.2)

m.c365 = Constraint(expr= - m.x128 + m.b265 <= 0.2)

m.c366 = Constraint(expr= - m.x130 + m.b279 <= 0.4)

m.c367 = Constraint(expr= - m.x131 + m.b280 <= 0.4)

m.c368 = Constraint(expr= - m.x132 + m.b281 <= 0.4)

m.c369 = Constraint(expr= - m.x130 + m.b283 <= 0.2)

m.c370 = Constraint(expr= - m.x131 + m.b284 <= 0.2)

m.c371 = Constraint(expr= - m.x132 + m.b285 <= 0.2)

m.c372 = Constraint(expr= - m.x134 + m.b299 <= 0.4)

m.c373 = Constraint(expr= - m.x135 + m.b300 <= 0.4)

m.c374 = Constraint(expr= - m.x136 + m.b301 <= 0.4)

m.c375 = Constraint(expr= - m.x134 + m.b303 <= 0.2)

m.c376 = Constraint(expr= - m.x135 + m.b304 <= 0.2)

m.c377 = Constraint(expr= - m.x136 + m.b305 <= 0.2)

m.c378 = Constraint(expr= - m.x138 + m.b239 <= 0.5)

m.c379 = Constraint(expr= - m.x139 + m.b240 <= 0.5)

m.c380 = Constraint(expr= - m.x140 + m.b241 <= 0.5)

m.c381 = Constraint(expr= - m.x138 + m.b243 <= 0.9)

m.c382 = Constraint(expr= - m.x139 + m.b244 <= 0.9)

m.c383 = Constraint(expr= - m.x140 + m.b245 <= 0.9)

m.c384 = Constraint(expr= - m.x142 + m.b259 <= 0.5)

m.c385 = Constraint(expr= - m.x143 + m.b260 <= 0.5)

m.c386 = Constraint(expr= - m.x144 + m.b261 <= 0.5)

m.c387 = Constraint(expr= - m.x142 + m.b263 <= 0.9)

m.c388 = Constraint(expr= - m.x143 + m.b264 <= 0.9)

m.c389 = Constraint(expr= - m.x144 + m.b265 <= 0.9)

m.c390 = Constraint(expr= - m.x146 + m.b279 <= 0.5)

m.c391 = Constraint(expr= - m.x147 + m.b280 <= 0.5)

m.c392 = Constraint(expr= - m.x148 + m.b281 <= 0.5)

m.c393 = Constraint(expr= - m.x146 + m.b283 <= 0.9)

m.c394 = Constraint(expr= - m.x147 + m.b284 <= 0.9)

m.c395 = Constraint(expr= - m.x148 + m.b285 <= 0.9)

m.c396 = Constraint(expr= - m.x150 + m.b299 <= 0.5)

m.c397 = Constraint(expr= - m.x151 + m.b300 <= 0.5)

m.c398 = Constraint(expr= - m.x152 + m.b301 <= 0.5)

m.c399 = Constraint(expr= - m.x150 + m.b303 <= 0.9)

m.c400 = Constraint(expr= - m.x151 + m.b304 <= 0.9)

m.c401 = Constraint(expr= - m.x152 + m.b305 <= 0.9)

m.c402 = Constraint(expr= - m.x122 - m.b239 >= -2)

m.c403 = Constraint(expr= - m.x123 - m.b240 >= -2)

m.c404 = Constraint(expr= - m.x124 - m.b241 >= -2)

m.c405 = Constraint(expr= - m.x122 - m.b243 >= -2)

m.c406 = Constraint(expr= - m.x123 - m.b244 >= -2)

m.c407 = Constraint(expr= - m.x124 - m.b245 >= -2)

m.c408 = Constraint(expr= - m.x126 - m.b259 >= -2)

m.c409 = Constraint(expr= - m.x127 - m.b260 >= -2)

m.c410 = Constraint(expr= - m.x128 - m.b261 >= -2)

m.c411 = Constraint(expr= - m.x126 - m.b263 >= -2)

m.c412 = Constraint(expr= - m.x127 - m.b264 >= -2)

m.c413 = Constraint(expr= - m.x128 - m.b265 >= -2)

m.c414 = Constraint(expr= - m.x130 - m.b279 >= -2)

m.c415 = Constraint(expr= - m.x131 - m.b280 >= -2)

m.c416 = Constraint(expr= - m.x132 - m.b281 >= -2)

m.c417 = Constraint(expr= - m.x130 - m.b283 >= -2)

m.c418 = Constraint(expr= - m.x131 - m.b284 >= -2)

m.c419 = Constraint(expr= - m.x132 - m.b285 >= -2)

m.c420 = Constraint(expr= - m.x134 - m.b299 >= -2)

m.c421 = Constraint(expr= - m.x135 - m.b300 >= -2)

m.c422 = Constraint(expr= - m.x136 - m.b301 >= -2)

m.c423 = Constraint(expr= - m.x134 - m.b303 >= -2)

m.c424 = Constraint(expr= - m.x135 - m.b304 >= -2)

m.c425 = Constraint(expr= - m.x136 - m.b305 >= -2)

m.c426 = Constraint(expr= - m.x138 - m.b239 >= -1.9)

m.c427 = Constraint(expr= - m.x139 - m.b240 >= -1.9)

m.c428 = Constraint(expr= - m.x140 - m.b241 >= -1.9)

m.c429 = Constraint(expr= - m.x138 - m.b243 >= -2)

m.c430 = Constraint(expr= - m.x139 - m.b244 >= -2)

m.c431 = Constraint(expr= - m.x140 - m.b245 >= -2)

m.c432 = Constraint(expr= - m.x142 - m.b259 >= -1.9)

m.c433 = Constraint(expr= - m.x143 - m.b260 >= -1.9)

m.c434 = Constraint(expr= - m.x144 - m.b261 >= -1.9)

m.c435 = Constraint(expr= - m.x142 - m.b263 >= -2)

m.c436 = Constraint(expr= - m.x143 - m.b264 >= -2)

m.c437 = Constraint(expr= - m.x144 - m.b265 >= -2)

m.c438 = Constraint(expr= - m.x146 - m.b279 >= -1.9)

m.c439 = Constraint(expr= - m.x147 - m.b280 >= -1.9)

m.c440 = Constraint(expr= - m.x148 - m.b281 >= -1.9)

m.c441 = Constraint(expr= - m.x146 - m.b283 >= -2)

m.c442 = Constraint(expr= - m.x147 - m.b284 >= -2)

m.c443 = Constraint(expr= - m.x148 - m.b285 >= -2)

m.c444 = Constraint(expr= - m.x150 - m.b299 >= -1.9)

m.c445 = Constraint(expr= - m.x151 - m.b300 >= -1.9)

m.c446 = Constraint(expr= - m.x152 - m.b301 >= -1.9)

m.c447 = Constraint(expr= - m.x150 - m.b303 >= -2)

m.c448 = Constraint(expr= - m.x151 - m.b304 >= -2)

m.c449 = Constraint(expr= - m.x152 - m.b305 >= -2)

m.c450 = Constraint(expr=   m.b238 <= 1.1)

m.c451 = Constraint(expr=   m.b242 <= 0.9)

m.c452 = Constraint(expr=   m.b258 <= 1.2)

m.c453 = Constraint(expr=   m.b262 <= 1)

m.c454 = Constraint(expr=   m.b278 <= 1.1)

m.c455 = Constraint(expr=   m.b282 <= 0.9)

m.c456 = Constraint(expr=   m.b298 <= 1.1)

m.c457 = Constraint(expr=   m.b302 <= 0.9)

m.c458 = Constraint(expr=   m.b238 <= 0.5)

m.c459 = Constraint(expr=   m.b242 <= 0.9)

m.c460 = Constraint(expr=   m.b258 <= 1.4)

m.c461 = Constraint(expr=   m.b262 <= 1.8)

m.c462 = Constraint(expr=   m.b278 <= 1.3)

m.c463 = Constraint(expr=   m.b282 <= 1.7)

m.c464 = Constraint(expr=   m.b298 <= 0.9)

m.c465 = Constraint(expr=   m.b302 <= 1.3)

m.c466 = Constraint(expr= - m.b238 >= -1.3)

m.c467 = Constraint(expr= - m.b242 >= -1.3)

m.c468 = Constraint(expr= - m.b258 >= -1.2)

m.c469 = Constraint(expr= - m.b262 >= -1.2)

m.c470 = Constraint(expr= - m.b278 >= -1.3)

m.c471 = Constraint(expr= - m.b282 >= -1.3)

m.c472 = Constraint(expr= - m.b298 >= -1.3)

m.c473 = Constraint(expr= - m.b302 >= -1.3)

m.c474 = Constraint(expr= - m.b238 >= -1.9)

m.c475 = Constraint(expr= - m.b242 >= -2)

m.c476 = Constraint(expr= - m.b258 >= -1)

m.c477 = Constraint(expr= - m.b262 >= -1.1)

m.c478 = Constraint(expr= - m.b278 >= -1.1)

m.c479 = Constraint(expr= - m.b282 >= -1.2)

m.c480 = Constraint(expr= - m.b298 >= -1.5)

m.c481 = Constraint(expr= - m.b302 >= -1.6)

m.c482 = Constraint(expr=   m.b186 + m.b226 <= 1)

m.c483 = Constraint(expr=   m.b187 + m.b227 <= 1)

m.c484 = Constraint(expr=   m.b188 + m.b228 <= 1)

m.c485 = Constraint(expr=   m.b189 + m.b229 <= 1)

m.c486 = Constraint(expr=   m.b186 + m.b230 <= 1)

m.c487 = Constraint(expr=   m.b187 + m.b231 <= 1)

m.c488 = Constraint(expr=   m.b188 + m.b232 <= 1)

m.c489 = Constraint(expr=   m.b189 + m.b233 <= 1)

m.c490 = Constraint(expr=   m.b186 + m.b234 <= 1)

m.c491 = Constraint(expr=   m.b187 + m.b235 <= 1)

m.c492 = Constraint(expr=   m.b188 + m.b236 <= 1)

m.c493 = Constraint(expr=   m.b189 + m.b237 <= 1)

m.c494 = Constraint(expr=   m.b186 + m.b238 <= 1)

m.c495 = Constraint(expr=   m.b187 + m.b239 <= 1)

m.c496 = Constraint(expr=   m.b188 + m.b240 <= 1)

m.c497 = Constraint(expr=   m.b189 + m.b241 <= 1)

m.c498 = Constraint(expr=   m.b186 + m.b242 <= 1)

m.c499 = Constraint(expr=   m.b187 + m.b243 <= 1)

m.c500 = Constraint(expr=   m.b188 + m.b244 <= 1)

m.c501 = Constraint(expr=   m.b189 + m.b245 <= 1)

m.c502 = Constraint(expr=   m.b226 + m.b246 <= 1)

m.c503 = Constraint(expr=   m.b227 + m.b247 <= 1)

m.c504 = Constraint(expr=   m.b228 + m.b248 <= 1)

m.c505 = Constraint(expr=   m.b229 + m.b249 <= 1)

m.c506 = Constraint(expr=   m.b230 + m.b246 <= 1)

m.c507 = Constraint(expr=   m.b231 + m.b247 <= 1)

m.c508 = Constraint(expr=   m.b232 + m.b248 <= 1)

m.c509 = Constraint(expr=   m.b233 + m.b249 <= 1)

m.c510 = Constraint(expr=   m.b234 + m.b246 <= 1)

m.c511 = Constraint(expr=   m.b235 + m.b247 <= 1)

m.c512 = Constraint(expr=   m.b236 + m.b248 <= 1)

m.c513 = Constraint(expr=   m.b237 + m.b249 <= 1)

m.c514 = Constraint(expr=   m.b238 + m.b246 <= 1)

m.c515 = Constraint(expr=   m.b239 + m.b247 <= 1)

m.c516 = Constraint(expr=   m.b240 + m.b248 <= 1)

m.c517 = Constraint(expr=   m.b241 + m.b249 <= 1)

m.c518 = Constraint(expr=   m.b242 + m.b246 <= 1)

m.c519 = Constraint(expr=   m.b243 + m.b247 <= 1)

m.c520 = Constraint(expr=   m.b244 + m.b248 <= 1)

m.c521 = Constraint(expr=   m.b245 + m.b249 <= 1)

m.c522 = Constraint(expr=   m.b226 + m.b266 <= 1)

m.c523 = Constraint(expr=   m.b227 + m.b267 <= 1)

m.c524 = Constraint(expr=   m.b228 + m.b268 <= 1)

m.c525 = Constraint(expr=   m.b229 + m.b269 <= 1)

m.c526 = Constraint(expr=   m.b230 + m.b266 <= 1)

m.c527 = Constraint(expr=   m.b231 + m.b267 <= 1)

m.c528 = Constraint(expr=   m.b232 + m.b268 <= 1)

m.c529 = Constraint(expr=   m.b233 + m.b269 <= 1)

m.c530 = Constraint(expr=   m.b234 + m.b266 <= 1)

m.c531 = Constraint(expr=   m.b235 + m.b267 <= 1)

m.c532 = Constraint(expr=   m.b236 + m.b268 <= 1)

m.c533 = Constraint(expr=   m.b237 + m.b269 <= 1)

m.c534 = Constraint(expr=   m.b238 + m.b266 <= 1)

m.c535 = Constraint(expr=   m.b239 + m.b267 <= 1)

m.c536 = Constraint(expr=   m.b240 + m.b268 <= 1)

m.c537 = Constraint(expr=   m.b241 + m.b269 <= 1)

m.c538 = Constraint(expr=   m.b242 + m.b266 <= 1)

m.c539 = Constraint(expr=   m.b243 + m.b267 <= 1)

m.c540 = Constraint(expr=   m.b244 + m.b268 <= 1)

m.c541 = Constraint(expr=   m.b245 + m.b269 <= 1)

m.c542 = Constraint(expr=   m.b226 + m.b286 <= 1)

m.c543 = Constraint(expr=   m.b227 + m.b287 <= 1)

m.c544 = Constraint(expr=   m.b228 + m.b288 <= 1)

m.c545 = Constraint(expr=   m.b229 + m.b289 <= 1)

m.c546 = Constraint(expr=   m.b230 + m.b286 <= 1)

m.c547 = Constraint(expr=   m.b231 + m.b287 <= 1)

m.c548 = Constraint(expr=   m.b232 + m.b288 <= 1)

m.c549 = Constraint(expr=   m.b233 + m.b289 <= 1)

m.c550 = Constraint(expr=   m.b234 + m.b286 <= 1)

m.c551 = Constraint(expr=   m.b235 + m.b287 <= 1)

m.c552 = Constraint(expr=   m.b236 + m.b288 <= 1)

m.c553 = Constraint(expr=   m.b237 + m.b289 <= 1)

m.c554 = Constraint(expr=   m.b238 + m.b286 <= 1)

m.c555 = Constraint(expr=   m.b239 + m.b287 <= 1)

m.c556 = Constraint(expr=   m.b240 + m.b288 <= 1)

m.c557 = Constraint(expr=   m.b241 + m.b289 <= 1)

m.c558 = Constraint(expr=   m.b242 + m.b286 <= 1)

m.c559 = Constraint(expr=   m.b243 + m.b287 <= 1)

m.c560 = Constraint(expr=   m.b244 + m.b288 <= 1)

m.c561 = Constraint(expr=   m.b245 + m.b289 <= 1)

m.c562 = Constraint(expr=   m.b190 + m.b246 <= 1)

m.c563 = Constraint(expr=   m.b191 + m.b247 <= 1)

m.c564 = Constraint(expr=   m.b192 + m.b248 <= 1)

m.c565 = Constraint(expr=   m.b193 + m.b249 <= 1)

m.c566 = Constraint(expr=   m.b190 + m.b250 <= 1)

m.c567 = Constraint(expr=   m.b191 + m.b251 <= 1)

m.c568 = Constraint(expr=   m.b192 + m.b252 <= 1)

m.c569 = Constraint(expr=   m.b193 + m.b253 <= 1)

m.c570 = Constraint(expr=   m.b190 + m.b254 <= 1)

m.c571 = Constraint(expr=   m.b191 + m.b255 <= 1)

m.c572 = Constraint(expr=   m.b192 + m.b256 <= 1)

m.c573 = Constraint(expr=   m.b193 + m.b257 <= 1)

m.c574 = Constraint(expr=   m.b190 + m.b258 <= 1)

m.c575 = Constraint(expr=   m.b191 + m.b259 <= 1)

m.c576 = Constraint(expr=   m.b192 + m.b260 <= 1)

m.c577 = Constraint(expr=   m.b193 + m.b261 <= 1)

m.c578 = Constraint(expr=   m.b190 + m.b262 <= 1)

m.c579 = Constraint(expr=   m.b191 + m.b263 <= 1)

m.c580 = Constraint(expr=   m.b192 + m.b264 <= 1)

m.c581 = Constraint(expr=   m.b193 + m.b265 <= 1)

m.c582 = Constraint(expr=   m.b206 + m.b246 <= 1)

m.c583 = Constraint(expr=   m.b207 + m.b247 <= 1)

m.c584 = Constraint(expr=   m.b208 + m.b248 <= 1)

m.c585 = Constraint(expr=   m.b209 + m.b249 <= 1)

m.c586 = Constraint(expr=   m.b206 + m.b250 <= 1)

m.c587 = Constraint(expr=   m.b207 + m.b251 <= 1)

m.c588 = Constraint(expr=   m.b208 + m.b252 <= 1)

m.c589 = Constraint(expr=   m.b209 + m.b253 <= 1)

m.c590 = Constraint(expr=   m.b206 + m.b254 <= 1)

m.c591 = Constraint(expr=   m.b207 + m.b255 <= 1)

m.c592 = Constraint(expr=   m.b208 + m.b256 <= 1)

m.c593 = Constraint(expr=   m.b209 + m.b257 <= 1)

m.c594 = Constraint(expr=   m.b206 + m.b258 <= 1)

m.c595 = Constraint(expr=   m.b207 + m.b259 <= 1)

m.c596 = Constraint(expr=   m.b208 + m.b260 <= 1)

m.c597 = Constraint(expr=   m.b209 + m.b261 <= 1)

m.c598 = Constraint(expr=   m.b206 + m.b262 <= 1)

m.c599 = Constraint(expr=   m.b207 + m.b263 <= 1)

m.c600 = Constraint(expr=   m.b208 + m.b264 <= 1)

m.c601 = Constraint(expr=   m.b209 + m.b265 <= 1)

m.c602 = Constraint(expr=   m.b226 + m.b246 <= 1)

m.c603 = Constraint(expr=   m.b227 + m.b247 <= 1)

m.c604 = Constraint(expr=   m.b228 + m.b248 <= 1)

m.c605 = Constraint(expr=   m.b229 + m.b249 <= 1)

m.c606 = Constraint(expr=   m.b226 + m.b250 <= 1)

m.c607 = Constraint(expr=   m.b227 + m.b251 <= 1)

m.c608 = Constraint(expr=   m.b228 + m.b252 <= 1)

m.c609 = Constraint(expr=   m.b229 + m.b253 <= 1)

m.c610 = Constraint(expr=   m.b226 + m.b254 <= 1)

m.c611 = Constraint(expr=   m.b227 + m.b255 <= 1)

m.c612 = Constraint(expr=   m.b228 + m.b256 <= 1)

m.c613 = Constraint(expr=   m.b229 + m.b257 <= 1)

m.c614 = Constraint(expr=   m.b226 + m.b258 <= 1)

m.c615 = Constraint(expr=   m.b227 + m.b259 <= 1)

m.c616 = Constraint(expr=   m.b228 + m.b260 <= 1)

m.c617 = Constraint(expr=   m.b229 + m.b261 <= 1)

m.c618 = Constraint(expr=   m.b226 + m.b262 <= 1)

m.c619 = Constraint(expr=   m.b227 + m.b263 <= 1)

m.c620 = Constraint(expr=   m.b228 + m.b264 <= 1)

m.c621 = Constraint(expr=   m.b229 + m.b265 <= 1)

m.c622 = Constraint(expr=   m.b246 + m.b270 <= 1)

m.c623 = Constraint(expr=   m.b247 + m.b271 <= 1)

m.c624 = Constraint(expr=   m.b248 + m.b272 <= 1)

m.c625 = Constraint(expr=   m.b249 + m.b273 <= 1)

m.c626 = Constraint(expr=   m.b250 + m.b270 <= 1)

m.c627 = Constraint(expr=   m.b251 + m.b271 <= 1)

m.c628 = Constraint(expr=   m.b252 + m.b272 <= 1)

m.c629 = Constraint(expr=   m.b253 + m.b273 <= 1)

m.c630 = Constraint(expr=   m.b254 + m.b270 <= 1)

m.c631 = Constraint(expr=   m.b255 + m.b271 <= 1)

m.c632 = Constraint(expr=   m.b256 + m.b272 <= 1)

m.c633 = Constraint(expr=   m.b257 + m.b273 <= 1)

m.c634 = Constraint(expr=   m.b258 + m.b270 <= 1)

m.c635 = Constraint(expr=   m.b259 + m.b271 <= 1)

m.c636 = Constraint(expr=   m.b260 + m.b272 <= 1)

m.c637 = Constraint(expr=   m.b261 + m.b273 <= 1)

m.c638 = Constraint(expr=   m.b262 + m.b270 <= 1)

m.c639 = Constraint(expr=   m.b263 + m.b271 <= 1)

m.c640 = Constraint(expr=   m.b264 + m.b272 <= 1)

m.c641 = Constraint(expr=   m.b265 + m.b273 <= 1)

m.c642 = Constraint(expr=   m.b246 + m.b290 <= 1)

m.c643 = Constraint(expr=   m.b247 + m.b291 <= 1)

m.c644 = Constraint(expr=   m.b248 + m.b292 <= 1)

m.c645 = Constraint(expr=   m.b249 + m.b293 <= 1)

m.c646 = Constraint(expr=   m.b250 + m.b290 <= 1)

m.c647 = Constraint(expr=   m.b251 + m.b291 <= 1)

m.c648 = Constraint(expr=   m.b252 + m.b292 <= 1)

m.c649 = Constraint(expr=   m.b253 + m.b293 <= 1)

m.c650 = Constraint(expr=   m.b254 + m.b290 <= 1)

m.c651 = Constraint(expr=   m.b255 + m.b291 <= 1)

m.c652 = Constraint(expr=   m.b256 + m.b292 <= 1)

m.c653 = Constraint(expr=   m.b257 + m.b293 <= 1)

m.c654 = Constraint(expr=   m.b258 + m.b290 <= 1)

m.c655 = Constraint(expr=   m.b259 + m.b291 <= 1)

m.c656 = Constraint(expr=   m.b260 + m.b292 <= 1)

m.c657 = Constraint(expr=   m.b261 + m.b293 <= 1)

m.c658 = Constraint(expr=   m.b262 + m.b290 <= 1)

m.c659 = Constraint(expr=   m.b263 + m.b291 <= 1)

m.c660 = Constraint(expr=   m.b264 + m.b292 <= 1)

m.c661 = Constraint(expr=   m.b265 + m.b293 <= 1)

m.c662 = Constraint(expr=   m.b194 + m.b266 <= 1)

m.c663 = Constraint(expr=   m.b195 + m.b267 <= 1)

m.c664 = Constraint(expr=   m.b196 + m.b268 <= 1)

m.c665 = Constraint(expr=   m.b197 + m.b269 <= 1)

m.c666 = Constraint(expr=   m.b194 + m.b270 <= 1)

m.c667 = Constraint(expr=   m.b195 + m.b271 <= 1)

m.c668 = Constraint(expr=   m.b196 + m.b272 <= 1)

m.c669 = Constraint(expr=   m.b197 + m.b273 <= 1)

m.c670 = Constraint(expr=   m.b194 + m.b274 <= 1)

m.c671 = Constraint(expr=   m.b195 + m.b275 <= 1)

m.c672 = Constraint(expr=   m.b196 + m.b276 <= 1)

m.c673 = Constraint(expr=   m.b197 + m.b277 <= 1)

m.c674 = Constraint(expr=   m.b194 + m.b278 <= 1)

m.c675 = Constraint(expr=   m.b195 + m.b279 <= 1)

m.c676 = Constraint(expr=   m.b196 + m.b280 <= 1)

m.c677 = Constraint(expr=   m.b197 + m.b281 <= 1)

m.c678 = Constraint(expr=   m.b194 + m.b282 <= 1)

m.c679 = Constraint(expr=   m.b195 + m.b283 <= 1)

m.c680 = Constraint(expr=   m.b196 + m.b284 <= 1)

m.c681 = Constraint(expr=   m.b197 + m.b285 <= 1)

m.c682 = Constraint(expr=   m.b210 + m.b266 <= 1)

m.c683 = Constraint(expr=   m.b211 + m.b267 <= 1)

m.c684 = Constraint(expr=   m.b212 + m.b268 <= 1)

m.c685 = Constraint(expr=   m.b213 + m.b269 <= 1)

m.c686 = Constraint(expr=   m.b210 + m.b270 <= 1)

m.c687 = Constraint(expr=   m.b211 + m.b271 <= 1)

m.c688 = Constraint(expr=   m.b212 + m.b272 <= 1)

m.c689 = Constraint(expr=   m.b213 + m.b273 <= 1)

m.c690 = Constraint(expr=   m.b210 + m.b274 <= 1)

m.c691 = Constraint(expr=   m.b211 + m.b275 <= 1)

m.c692 = Constraint(expr=   m.b212 + m.b276 <= 1)

m.c693 = Constraint(expr=   m.b213 + m.b277 <= 1)

m.c694 = Constraint(expr=   m.b210 + m.b278 <= 1)

m.c695 = Constraint(expr=   m.b211 + m.b279 <= 1)

m.c696 = Constraint(expr=   m.b212 + m.b280 <= 1)

m.c697 = Constraint(expr=   m.b213 + m.b281 <= 1)

m.c698 = Constraint(expr=   m.b210 + m.b282 <= 1)

m.c699 = Constraint(expr=   m.b211 + m.b283 <= 1)

m.c700 = Constraint(expr=   m.b212 + m.b284 <= 1)

m.c701 = Constraint(expr=   m.b213 + m.b285 <= 1)

m.c702 = Constraint(expr=   m.b230 + m.b266 <= 1)

m.c703 = Constraint(expr=   m.b231 + m.b267 <= 1)

m.c704 = Constraint(expr=   m.b232 + m.b268 <= 1)

m.c705 = Constraint(expr=   m.b233 + m.b269 <= 1)

m.c706 = Constraint(expr=   m.b230 + m.b270 <= 1)

m.c707 = Constraint(expr=   m.b231 + m.b271 <= 1)

m.c708 = Constraint(expr=   m.b232 + m.b272 <= 1)

m.c709 = Constraint(expr=   m.b233 + m.b273 <= 1)

m.c710 = Constraint(expr=   m.b230 + m.b274 <= 1)

m.c711 = Constraint(expr=   m.b231 + m.b275 <= 1)

m.c712 = Constraint(expr=   m.b232 + m.b276 <= 1)

m.c713 = Constraint(expr=   m.b233 + m.b277 <= 1)

m.c714 = Constraint(expr=   m.b230 + m.b278 <= 1)

m.c715 = Constraint(expr=   m.b231 + m.b279 <= 1)

m.c716 = Constraint(expr=   m.b232 + m.b280 <= 1)

m.c717 = Constraint(expr=   m.b233 + m.b281 <= 1)

m.c718 = Constraint(expr=   m.b230 + m.b282 <= 1)

m.c719 = Constraint(expr=   m.b231 + m.b283 <= 1)

m.c720 = Constraint(expr=   m.b232 + m.b284 <= 1)

m.c721 = Constraint(expr=   m.b233 + m.b285 <= 1)

m.c722 = Constraint(expr=   m.b250 + m.b266 <= 1)

m.c723 = Constraint(expr=   m.b251 + m.b267 <= 1)

m.c724 = Constraint(expr=   m.b252 + m.b268 <= 1)

m.c725 = Constraint(expr=   m.b253 + m.b269 <= 1)

m.c726 = Constraint(expr=   m.b250 + m.b270 <= 1)

m.c727 = Constraint(expr=   m.b251 + m.b271 <= 1)

m.c728 = Constraint(expr=   m.b252 + m.b272 <= 1)

m.c729 = Constraint(expr=   m.b253 + m.b273 <= 1)

m.c730 = Constraint(expr=   m.b250 + m.b274 <= 1)

m.c731 = Constraint(expr=   m.b251 + m.b275 <= 1)

m.c732 = Constraint(expr=   m.b252 + m.b276 <= 1)

m.c733 = Constraint(expr=   m.b253 + m.b277 <= 1)

m.c734 = Constraint(expr=   m.b250 + m.b278 <= 1)

m.c735 = Constraint(expr=   m.b251 + m.b279 <= 1)

m.c736 = Constraint(expr=   m.b252 + m.b280 <= 1)

m.c737 = Constraint(expr=   m.b253 + m.b281 <= 1)

m.c738 = Constraint(expr=   m.b250 + m.b282 <= 1)

m.c739 = Constraint(expr=   m.b251 + m.b283 <= 1)

m.c740 = Constraint(expr=   m.b252 + m.b284 <= 1)

m.c741 = Constraint(expr=   m.b253 + m.b285 <= 1)

m.c742 = Constraint(expr=   m.b266 + m.b294 <= 1)

m.c743 = Constraint(expr=   m.b267 + m.b295 <= 1)

m.c744 = Constraint(expr=   m.b268 + m.b296 <= 1)

m.c745 = Constraint(expr=   m.b269 + m.b297 <= 1)

m.c746 = Constraint(expr=   m.b270 + m.b294 <= 1)

m.c747 = Constraint(expr=   m.b271 + m.b295 <= 1)

m.c748 = Constraint(expr=   m.b272 + m.b296 <= 1)

m.c749 = Constraint(expr=   m.b273 + m.b297 <= 1)

m.c750 = Constraint(expr=   m.b274 + m.b294 <= 1)

m.c751 = Constraint(expr=   m.b275 + m.b295 <= 1)

m.c752 = Constraint(expr=   m.b276 + m.b296 <= 1)

m.c753 = Constraint(expr=   m.b277 + m.b297 <= 1)

m.c754 = Constraint(expr=   m.b278 + m.b294 <= 1)

m.c755 = Constraint(expr=   m.b279 + m.b295 <= 1)

m.c756 = Constraint(expr=   m.b280 + m.b296 <= 1)

m.c757 = Constraint(expr=   m.b281 + m.b297 <= 1)

m.c758 = Constraint(expr=   m.b282 + m.b294 <= 1)

m.c759 = Constraint(expr=   m.b283 + m.b295 <= 1)

m.c760 = Constraint(expr=   m.b284 + m.b296 <= 1)

m.c761 = Constraint(expr=   m.b285 + m.b297 <= 1)

m.c762 = Constraint(expr=   m.b198 + m.b286 <= 1)

m.c763 = Constraint(expr=   m.b199 + m.b287 <= 1)

m.c764 = Constraint(expr=   m.b200 + m.b288 <= 1)

m.c765 = Constraint(expr=   m.b201 + m.b289 <= 1)

m.c766 = Constraint(expr=   m.b198 + m.b290 <= 1)

m.c767 = Constraint(expr=   m.b199 + m.b291 <= 1)

m.c768 = Constraint(expr=   m.b200 + m.b292 <= 1)

m.c769 = Constraint(expr=   m.b201 + m.b293 <= 1)

m.c770 = Constraint(expr=   m.b198 + m.b294 <= 1)

m.c771 = Constraint(expr=   m.b199 + m.b295 <= 1)

m.c772 = Constraint(expr=   m.b200 + m.b296 <= 1)

m.c773 = Constraint(expr=   m.b201 + m.b297 <= 1)

m.c774 = Constraint(expr=   m.b198 + m.b298 <= 1)

m.c775 = Constraint(expr=   m.b199 + m.b299 <= 1)

m.c776 = Constraint(expr=   m.b200 + m.b300 <= 1)

m.c777 = Constraint(expr=   m.b201 + m.b301 <= 1)

m.c778 = Constraint(expr=   m.b198 + m.b302 <= 1)

m.c779 = Constraint(expr=   m.b199 + m.b303 <= 1)

m.c780 = Constraint(expr=   m.b200 + m.b304 <= 1)

m.c781 = Constraint(expr=   m.b201 + m.b305 <= 1)

m.c782 = Constraint(expr=   m.b214 + m.b286 <= 1)

m.c783 = Constraint(expr=   m.b215 + m.b287 <= 1)

m.c784 = Constraint(expr=   m.b216 + m.b288 <= 1)

m.c785 = Constraint(expr=   m.b217 + m.b289 <= 1)

m.c786 = Constraint(expr=   m.b214 + m.b290 <= 1)

m.c787 = Constraint(expr=   m.b215 + m.b291 <= 1)

m.c788 = Constraint(expr=   m.b216 + m.b292 <= 1)

m.c789 = Constraint(expr=   m.b217 + m.b293 <= 1)

m.c790 = Constraint(expr=   m.b214 + m.b294 <= 1)

m.c791 = Constraint(expr=   m.b215 + m.b295 <= 1)

m.c792 = Constraint(expr=   m.b216 + m.b296 <= 1)

m.c793 = Constraint(expr=   m.b217 + m.b297 <= 1)

m.c794 = Constraint(expr=   m.b214 + m.b298 <= 1)

m.c795 = Constraint(expr=   m.b215 + m.b299 <= 1)

m.c796 = Constraint(expr=   m.b216 + m.b300 <= 1)

m.c797 = Constraint(expr=   m.b217 + m.b301 <= 1)

m.c798 = Constraint(expr=   m.b214 + m.b302 <= 1)

m.c799 = Constraint(expr=   m.b215 + m.b303 <= 1)

m.c800 = Constraint(expr=   m.b216 + m.b304 <= 1)

m.c801 = Constraint(expr=   m.b217 + m.b305 <= 1)

m.c802 = Constraint(expr=   m.b234 + m.b286 <= 1)

m.c803 = Constraint(expr=   m.b235 + m.b287 <= 1)

m.c804 = Constraint(expr=   m.b236 + m.b288 <= 1)

m.c805 = Constraint(expr=   m.b237 + m.b289 <= 1)

m.c806 = Constraint(expr=   m.b234 + m.b290 <= 1)

m.c807 = Constraint(expr=   m.b235 + m.b291 <= 1)

m.c808 = Constraint(expr=   m.b236 + m.b292 <= 1)

m.c809 = Constraint(expr=   m.b237 + m.b293 <= 1)

m.c810 = Constraint(expr=   m.b234 + m.b294 <= 1)

m.c811 = Constraint(expr=   m.b235 + m.b295 <= 1)

m.c812 = Constraint(expr=   m.b236 + m.b296 <= 1)

m.c813 = Constraint(expr=   m.b237 + m.b297 <= 1)

m.c814 = Constraint(expr=   m.b234 + m.b298 <= 1)

m.c815 = Constraint(expr=   m.b235 + m.b299 <= 1)

m.c816 = Constraint(expr=   m.b236 + m.b300 <= 1)

m.c817 = Constraint(expr=   m.b237 + m.b301 <= 1)

m.c818 = Constraint(expr=   m.b234 + m.b302 <= 1)

m.c819 = Constraint(expr=   m.b235 + m.b303 <= 1)

m.c820 = Constraint(expr=   m.b236 + m.b304 <= 1)

m.c821 = Constraint(expr=   m.b237 + m.b305 <= 1)

m.c822 = Constraint(expr=   m.b254 + m.b286 <= 1)

m.c823 = Constraint(expr=   m.b255 + m.b287 <= 1)

m.c824 = Constraint(expr=   m.b256 + m.b288 <= 1)

m.c825 = Constraint(expr=   m.b257 + m.b289 <= 1)

m.c826 = Constraint(expr=   m.b254 + m.b290 <= 1)

m.c827 = Constraint(expr=   m.b255 + m.b291 <= 1)

m.c828 = Constraint(expr=   m.b256 + m.b292 <= 1)

m.c829 = Constraint(expr=   m.b257 + m.b293 <= 1)

m.c830 = Constraint(expr=   m.b254 + m.b294 <= 1)

m.c831 = Constraint(expr=   m.b255 + m.b295 <= 1)

m.c832 = Constraint(expr=   m.b256 + m.b296 <= 1)

m.c833 = Constraint(expr=   m.b257 + m.b297 <= 1)

m.c834 = Constraint(expr=   m.b254 + m.b298 <= 1)

m.c835 = Constraint(expr=   m.b255 + m.b299 <= 1)

m.c836 = Constraint(expr=   m.b256 + m.b300 <= 1)

m.c837 = Constraint(expr=   m.b257 + m.b301 <= 1)

m.c838 = Constraint(expr=   m.b254 + m.b302 <= 1)

m.c839 = Constraint(expr=   m.b255 + m.b303 <= 1)

m.c840 = Constraint(expr=   m.b256 + m.b304 <= 1)

m.c841 = Constraint(expr=   m.b257 + m.b305 <= 1)

m.c842 = Constraint(expr=   m.b274 + m.b286 <= 1)

m.c843 = Constraint(expr=   m.b275 + m.b287 <= 1)

m.c844 = Constraint(expr=   m.b276 + m.b288 <= 1)

m.c845 = Constraint(expr=   m.b277 + m.b289 <= 1)

m.c846 = Constraint(expr=   m.b274 + m.b290 <= 1)

m.c847 = Constraint(expr=   m.b275 + m.b291 <= 1)

m.c848 = Constraint(expr=   m.b276 + m.b292 <= 1)

m.c849 = Constraint(expr=   m.b277 + m.b293 <= 1)

m.c850 = Constraint(expr=   m.b274 + m.b294 <= 1)

m.c851 = Constraint(expr=   m.b275 + m.b295 <= 1)

m.c852 = Constraint(expr=   m.b276 + m.b296 <= 1)

m.c853 = Constraint(expr=   m.b277 + m.b297 <= 1)

m.c854 = Constraint(expr=   m.b274 + m.b298 <= 1)

m.c855 = Constraint(expr=   m.b275 + m.b299 <= 1)

m.c856 = Constraint(expr=   m.b276 + m.b300 <= 1)

m.c857 = Constraint(expr=   m.b277 + m.b301 <= 1)

m.c858 = Constraint(expr=   m.b274 + m.b302 <= 1)

m.c859 = Constraint(expr=   m.b275 + m.b303 <= 1)

m.c860 = Constraint(expr=   m.b276 + m.b304 <= 1)

m.c861 = Constraint(expr=   m.b277 + m.b305 <= 1)
