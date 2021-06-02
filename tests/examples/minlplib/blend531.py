#  MINLP written by GAMS Convert at 04/21/18 13:51:12
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        737       65      184      488        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        273      169      104        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       2107     1749      358        0
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
m.x138 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x139 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x140 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x141 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x142 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x143 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x144 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x145 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x146 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x147 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x148 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x149 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x150 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x151 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x152 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x153 = Var(within=Reals,bounds=(0,2),initialize=0)
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
m.b170 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b171 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b172 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b173 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b174 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b175 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b176 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b177 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b178 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b179 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b180 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b181 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b182 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b183 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b184 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b185 = Var(within=Binary,bounds=(0,1),initialize=0)
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

m.obj = Objective(expr= - 0.87*m.x2 - 0.87*m.x3 - 0.87*m.x4 - 0.87*m.x5 + 7.42*m.x6 + 7.42*m.x7 + 7.42*m.x8 + 7.42*m.x9
                        - 1.06*m.x10 - 1.06*m.x11 - 1.06*m.x12 - 1.06*m.x13 - 0.58*m.x14 - 0.58*m.x15 - 0.58*m.x16
                        - 0.58*m.x17 - 0.63*m.x18 - 0.63*m.x19 - 0.63*m.x20 - 0.63*m.x21 - 0.32*m.x22 - 0.32*m.x23
                        - 0.32*m.x24 - 0.32*m.x25 - 0.13*m.x26 - 0.13*m.x27 - 0.13*m.x28 - 0.13*m.x29 - 0.58*m.x30
                        - 0.58*m.x31 - 0.58*m.x32 - 0.58*m.x33 - 0.29*m.x34 - 0.29*m.x35 - 0.29*m.x36 - 0.29*m.x37
                        - 0.27*m.x38 - 0.27*m.x39 - 0.27*m.x40 - 0.27*m.x41 + 7.92*m.x42 + 7.92*m.x43 + 7.92*m.x44
                        + 7.92*m.x45 - 0.04*m.x46 - 0.04*m.x47 - 0.04*m.x48 - 0.04*m.x49 - 0.11*m.x50 - 0.11*m.x51
                        - 0.11*m.x52 - 0.11*m.x53 - 0.88*m.x54 - 0.88*m.x55 - 0.88*m.x56 - 0.88*m.x57 - 0.26*m.x58
                        - 0.26*m.x59 - 0.26*m.x60 - 0.26*m.x61 + 8.88*m.x62 + 8.88*m.x63 + 8.88*m.x64 + 8.88*m.x65
                        - 0.01*m.x66 - 0.01*m.x67 - 0.01*m.x68 - 0.01*m.x69 - 0.18*m.x70 - 0.18*m.x71 - 0.18*m.x72
                        - 0.18*m.x73 - 0.09*m.x74 - 0.09*m.x75 - 0.09*m.x76 - 0.09*m.x77 - 0.47*m.x78 - 0.47*m.x79
                        - 0.47*m.x80 - 0.47*m.x81 + 8.2*m.x82 + 8.2*m.x83 + 8.2*m.x84 + 8.2*m.x85 + 0.27*m.x86
                        + 0.27*m.x87 + 0.27*m.x88 + 0.27*m.x89 - 0.32*m.x90 - 0.32*m.x91 - 0.32*m.x92 - 0.32*m.x93
                        - 0.65*m.x94 - 0.65*m.x95 - 0.65*m.x96 - 0.65*m.x97 + 8.08*m.x98 + 8.08*m.x99 + 8.08*m.x100
                        + 8.08*m.x101 - 0.67*m.x102 - 0.67*m.x103 - 0.67*m.x104 - 0.67*m.x105 - 0.19*m.b170
                        - 0.19*m.b171 - 0.19*m.b172 - 0.19*m.b173 - 0.46*m.b174 - 0.46*m.b175 - 0.46*m.b176
                        - 0.46*m.b177 - 0.16*m.b178 - 0.16*m.b179 - 0.16*m.b180 - 0.16*m.b181 - 0.64*m.b182
                        - 0.64*m.b183 - 0.64*m.b184 - 0.64*m.b185 - 0.19*m.b186 - 0.19*m.b187 - 0.19*m.b188
                        - 0.19*m.b189 - 0.48*m.b190 - 0.48*m.b191 - 0.48*m.b192 - 0.48*m.b193 - 0.59*m.b194
                        - 0.59*m.b195 - 0.59*m.b196 - 0.59*m.b197 - 0.38*m.b198 - 0.38*m.b199 - 0.38*m.b200
                        - 0.38*m.b201 - 0.25*m.b202 - 0.25*m.b203 - 0.25*m.b204 - 0.25*m.b205 - 0.62*m.b206
                        - 0.62*m.b207 - 0.62*m.b208 - 0.62*m.b209 - 0.82*m.b210 - 0.82*m.b211 - 0.82*m.b212
                        - 0.82*m.b213 - 0.73*m.b214 - 0.73*m.b215 - 0.73*m.b216 - 0.73*m.b217 - 0.58*m.b218
                        - 0.58*m.b219 - 0.58*m.b220 - 0.58*m.b221 - 0.91*m.b222 - 0.91*m.b223 - 0.91*m.b224
                        - 0.91*m.b225 - 0.82*m.b226 - 0.82*m.b227 - 0.82*m.b228 - 0.82*m.b229 - 0.59*m.b230
                        - 0.59*m.b231 - 0.59*m.b232 - 0.59*m.b233 - 0.43*m.b234 - 0.43*m.b235 - 0.43*m.b236
                        - 0.43*m.b237 - 0.16*m.b238 - 0.16*m.b239 - 0.16*m.b240 - 0.16*m.b241 - 0.42*m.b242
                        - 0.42*m.b243 - 0.42*m.b244 - 0.42*m.b245 - 0.6*m.b246 - 0.6*m.b247 - 0.6*m.b248 - 0.6*m.b249
                        - 0.7*m.b250 - 0.7*m.b251 - 0.7*m.b252 - 0.7*m.b253 - 0.64*m.b254 - 0.64*m.b255 - 0.64*m.b256
                        - 0.64*m.b257 - 0.07*m.b258 - 0.07*m.b259 - 0.07*m.b260 - 0.07*m.b261 - 0.53*m.b262
                        - 0.53*m.b263 - 0.53*m.b264 - 0.53*m.b265 - 0.41*m.b266 - 0.41*m.b267 - 0.41*m.b268
                        - 0.41*m.b269 - 0.72*m.b270 - 0.72*m.b271 - 0.72*m.b272 - 0.72*m.b273, sense=maximize)

m.c2 = Constraint(expr=   m.x2 + m.x6 + m.x138 == 2.2)

m.c3 = Constraint(expr=   m.x10 + m.x14 + m.x18 + m.x22 + m.x26 + m.x142 == 2)

m.c4 = Constraint(expr= - m.x10 + m.x30 + m.x34 + m.x38 + m.x42 + m.x46 - m.x50 - m.x70 - m.x90 + m.x146 == 1.2)

m.c5 = Constraint(expr= - m.x2 - m.x14 - m.x30 + m.x50 + m.x54 + m.x58 + m.x62 + m.x66 - m.x74 + m.x150 == 1.7)

m.c6 = Constraint(expr= - m.x18 - m.x34 - m.x54 + m.x70 + m.x74 + m.x78 + m.x82 + m.x86 - m.x94 + m.x154 == 1.6)

m.c7 = Constraint(expr= - m.x22 - m.x38 - m.x58 - m.x78 + m.x90 + m.x94 + m.x98 + m.x102 + m.x158 == 1.2)

m.c8 = Constraint(expr= - m.x6 - m.x42 - m.x62 - m.x82 - m.x98 + m.x162 == 0.34)

m.c9 = Constraint(expr= - m.x26 - m.x46 - m.x66 - m.x86 - m.x102 + m.x166 == 0.1)

m.c10 = Constraint(expr=m.x106*m.x146 - 0.6*m.x10 + 0.5*m.x30 + 0.5*m.x34 + 0.5*m.x38 + 0.5*m.x42 + 0.5*m.x46
                         - 0.8*m.x50 - 0.7*m.x70 - 0.7*m.x90 == 0.6)

m.c11 = Constraint(expr=m.x110*m.x150 - m.x2 - 0.6*m.x14 - 0.5*m.x30 + 0.8*m.x50 + 0.8*m.x54 + 0.8*m.x58 + 0.8*m.x62
                         + 0.8*m.x66 - 0.7*m.x74 == 1.36)

m.c12 = Constraint(expr=m.x114*m.x154 - 0.6*m.x18 - 0.5*m.x34 - 0.8*m.x54 + 0.7*m.x70 + 0.7*m.x74 + 0.7*m.x78
                         + 0.7*m.x82 + 0.7*m.x86 - 0.7*m.x94 == 1.12)

m.c13 = Constraint(expr=m.x118*m.x158 - 0.6*m.x22 - 0.5*m.x38 - 0.8*m.x58 - 0.7*m.x78 + 0.7*m.x90 + 0.7*m.x94
                         + 0.7*m.x98 + 0.7*m.x102 == 0.84)

m.c14 = Constraint(expr=m.x122*m.x146 - 0.9*m.x10 + 0.1*m.x30 + 0.1*m.x34 + 0.1*m.x38 + 0.1*m.x42 + 0.1*m.x46
                         - 0.8*m.x50 - 0.1*m.x70 - 0.5*m.x90 == 0.12)

m.c15 = Constraint(expr=m.x126*m.x150 - 0.6*m.x2 - 0.9*m.x14 - 0.1*m.x30 + 0.8*m.x50 + 0.8*m.x54 + 0.8*m.x58 + 0.8*m.x62
                         + 0.8*m.x66 - 0.1*m.x74 == 1.36)

m.c16 = Constraint(expr=m.x130*m.x154 - 0.9*m.x18 - 0.1*m.x34 - 0.8*m.x54 + 0.1*m.x70 + 0.1*m.x74 + 0.1*m.x78
                         + 0.1*m.x82 + 0.1*m.x86 - 0.5*m.x94 == 0.16)

m.c17 = Constraint(expr=m.x134*m.x158 - 0.9*m.x22 - 0.1*m.x38 - 0.8*m.x58 - 0.1*m.x78 + 0.5*m.x90 + 0.5*m.x94
                         + 0.5*m.x98 + 0.5*m.x102 == 0.6)

m.c18 = Constraint(expr=   m.x3 + m.x7 - m.x138 + m.x139 == 0.1)

m.c19 = Constraint(expr=   m.x4 + m.x8 - m.x139 + m.x140 == 0.2)

m.c20 = Constraint(expr=   m.x5 + m.x9 - m.x140 + m.x141 == 0.8)

m.c21 = Constraint(expr=   m.x11 + m.x15 + m.x19 + m.x23 + m.x27 - m.x142 + m.x143 == 0.1)

m.c22 = Constraint(expr=   m.x12 + m.x16 + m.x20 + m.x24 + m.x28 - m.x143 + m.x144 == 0.4)

m.c23 = Constraint(expr=   m.x13 + m.x17 + m.x21 + m.x25 + m.x29 - m.x144 + m.x145 == 0.8)

m.c24 = Constraint(expr= - m.x11 + m.x31 + m.x35 + m.x39 + m.x43 + m.x47 - m.x51 - m.x71 - m.x91 - m.x146 + m.x147 == 0)

m.c25 = Constraint(expr= - m.x12 + m.x32 + m.x36 + m.x40 + m.x44 + m.x48 - m.x52 - m.x72 - m.x92 - m.x147 + m.x148 == 0)

m.c26 = Constraint(expr= - m.x13 + m.x33 + m.x37 + m.x41 + m.x45 + m.x49 - m.x53 - m.x73 - m.x93 - m.x148 + m.x149 == 0)

m.c27 = Constraint(expr= - m.x3 - m.x15 - m.x31 + m.x51 + m.x55 + m.x59 + m.x63 + m.x67 - m.x75 - m.x150 + m.x151 == 0)

m.c28 = Constraint(expr= - m.x4 - m.x16 - m.x32 + m.x52 + m.x56 + m.x60 + m.x64 + m.x68 - m.x76 - m.x151 + m.x152 == 0)

m.c29 = Constraint(expr= - m.x5 - m.x17 - m.x33 + m.x53 + m.x57 + m.x61 + m.x65 + m.x69 - m.x77 - m.x152 + m.x153 == 0)

m.c30 = Constraint(expr= - m.x19 - m.x35 - m.x55 + m.x71 + m.x75 + m.x79 + m.x83 + m.x87 - m.x95 - m.x154 + m.x155 == 0)

m.c31 = Constraint(expr= - m.x20 - m.x36 - m.x56 + m.x72 + m.x76 + m.x80 + m.x84 + m.x88 - m.x96 - m.x155 + m.x156 == 0)

m.c32 = Constraint(expr= - m.x21 - m.x37 - m.x57 + m.x73 + m.x77 + m.x81 + m.x85 + m.x89 - m.x97 - m.x156 + m.x157 == 0)

m.c33 = Constraint(expr= - m.x23 - m.x39 - m.x59 - m.x79 + m.x91 + m.x95 + m.x99 + m.x103 - m.x158 + m.x159 == 0)

m.c34 = Constraint(expr= - m.x24 - m.x40 - m.x60 - m.x80 + m.x92 + m.x96 + m.x100 + m.x104 - m.x159 + m.x160 == 0)

m.c35 = Constraint(expr= - m.x25 - m.x41 - m.x61 - m.x81 + m.x93 + m.x97 + m.x101 + m.x105 - m.x160 + m.x161 == 0)

m.c36 = Constraint(expr= - m.x7 - m.x43 - m.x63 - m.x83 - m.x99 - m.x162 + m.x163 == -0.53)

m.c37 = Constraint(expr= - m.x8 - m.x44 - m.x64 - m.x84 - m.x100 - m.x163 + m.x164 == -0.66)

m.c38 = Constraint(expr= - m.x9 - m.x45 - m.x65 - m.x85 - m.x101 - m.x164 + m.x165 == -0.29)

m.c39 = Constraint(expr= - m.x27 - m.x47 - m.x67 - m.x87 - m.x103 - m.x166 + m.x167 == -0.42)

m.c40 = Constraint(expr= - m.x28 - m.x48 - m.x68 - m.x88 - m.x104 - m.x167 + m.x168 == -0.63)

m.c41 = Constraint(expr= - m.x29 - m.x49 - m.x69 - m.x89 - m.x105 - m.x168 + m.x169 == -0.43)

m.c42 = Constraint(expr=m.x107*m.x147 - (m.x106*m.x146 + m.x110*m.x51 + m.x114*m.x71 + m.x118*m.x91 - (m.x106*m.x31 + 
                        m.x106*m.x35 + m.x106*m.x39 + m.x106*m.x43 + m.x106*m.x47)) - 0.6*m.x11 == 0)

m.c43 = Constraint(expr=m.x108*m.x148 - (m.x107*m.x147 + m.x111*m.x52 + m.x115*m.x72 + m.x119*m.x92 - (m.x107*m.x32 + 
                        m.x107*m.x36 + m.x107*m.x40 + m.x107*m.x44 + m.x107*m.x48)) - 0.6*m.x12 == 0)

m.c44 = Constraint(expr=m.x109*m.x149 - (m.x108*m.x148 + m.x112*m.x53 + m.x116*m.x73 + m.x120*m.x93 - (m.x108*m.x33 + 
                        m.x108*m.x37 + m.x108*m.x41 + m.x108*m.x45 + m.x108*m.x49)) - 0.6*m.x13 == 0)

m.c45 = Constraint(expr=m.x111*m.x151 - (m.x110*m.x150 + m.x106*m.x31 + m.x114*m.x75 - (m.x110*m.x51 + m.x110*m.x55 + 
                        m.x110*m.x59 + m.x110*m.x63 + m.x110*m.x67)) - m.x3 - 0.6*m.x15 == 0)

m.c46 = Constraint(expr=m.x112*m.x152 - (m.x111*m.x151 + m.x107*m.x32 + m.x115*m.x76 - (m.x111*m.x52 + m.x111*m.x56 + 
                        m.x111*m.x60 + m.x111*m.x64 + m.x111*m.x68)) - m.x4 - 0.6*m.x16 == 0)

m.c47 = Constraint(expr=m.x113*m.x153 - (m.x112*m.x152 + m.x108*m.x33 + m.x116*m.x77 - (m.x112*m.x53 + m.x112*m.x57 + 
                        m.x112*m.x61 + m.x112*m.x65 + m.x112*m.x69)) - m.x5 - 0.6*m.x17 == 0)

m.c48 = Constraint(expr=m.x115*m.x155 - (m.x114*m.x154 + m.x106*m.x35 + m.x110*m.x55 + m.x118*m.x95 - (m.x114*m.x71 + 
                        m.x114*m.x75 + m.x114*m.x79 + m.x114*m.x83 + m.x114*m.x87)) - 0.6*m.x19 == 0)

m.c49 = Constraint(expr=m.x116*m.x156 - (m.x115*m.x155 + m.x107*m.x36 + m.x111*m.x56 + m.x119*m.x96 - (m.x115*m.x72 + 
                        m.x115*m.x76 + m.x115*m.x80 + m.x115*m.x84 + m.x115*m.x88)) - 0.6*m.x20 == 0)

m.c50 = Constraint(expr=m.x117*m.x157 - (m.x116*m.x156 + m.x108*m.x37 + m.x112*m.x57 + m.x120*m.x97 - (m.x116*m.x73 + 
                        m.x116*m.x77 + m.x116*m.x81 + m.x116*m.x85 + m.x116*m.x89)) - 0.6*m.x21 == 0)

m.c51 = Constraint(expr=m.x119*m.x159 - (m.x118*m.x158 + m.x106*m.x39 + m.x110*m.x59 + m.x114*m.x79 - (m.x118*m.x91 + 
                        m.x118*m.x95 + m.x118*m.x99 + m.x118*m.x103)) - 0.6*m.x23 == 0)

m.c52 = Constraint(expr=m.x120*m.x160 - (m.x119*m.x159 + m.x107*m.x40 + m.x111*m.x60 + m.x115*m.x80 - (m.x119*m.x92 + 
                        m.x119*m.x96 + m.x119*m.x100 + m.x119*m.x104)) - 0.6*m.x24 == 0)

m.c53 = Constraint(expr=m.x121*m.x161 - (m.x120*m.x160 + m.x108*m.x41 + m.x112*m.x61 + m.x116*m.x81 - (m.x120*m.x93 + 
                        m.x120*m.x97 + m.x120*m.x101 + m.x120*m.x105)) - 0.6*m.x25 == 0)

m.c54 = Constraint(expr=m.x123*m.x147 - (m.x122*m.x146 + m.x126*m.x51 + m.x130*m.x71 + m.x134*m.x91 - (m.x122*m.x31 + 
                        m.x122*m.x35 + m.x122*m.x39 + m.x122*m.x43 + m.x122*m.x47)) - 0.9*m.x11 == 0)

m.c55 = Constraint(expr=m.x124*m.x148 - (m.x123*m.x147 + m.x127*m.x52 + m.x131*m.x72 + m.x135*m.x92 - (m.x123*m.x32 + 
                        m.x123*m.x36 + m.x123*m.x40 + m.x123*m.x44 + m.x123*m.x48)) - 0.9*m.x12 == 0)

m.c56 = Constraint(expr=m.x125*m.x149 - (m.x124*m.x148 + m.x128*m.x53 + m.x132*m.x73 + m.x136*m.x93 - (m.x124*m.x33 + 
                        m.x124*m.x37 + m.x124*m.x41 + m.x124*m.x45 + m.x124*m.x49)) - 0.9*m.x13 == 0)

m.c57 = Constraint(expr=m.x127*m.x151 - (m.x126*m.x150 + m.x122*m.x31 + m.x130*m.x75 - (m.x126*m.x51 + m.x126*m.x55 + 
                        m.x126*m.x59 + m.x126*m.x63 + m.x126*m.x67)) - 0.6*m.x3 - 0.9*m.x15 == 0)

m.c58 = Constraint(expr=m.x128*m.x152 - (m.x127*m.x151 + m.x123*m.x32 + m.x131*m.x76 - (m.x127*m.x52 + m.x127*m.x56 + 
                        m.x127*m.x60 + m.x127*m.x64 + m.x127*m.x68)) - 0.6*m.x4 - 0.9*m.x16 == 0)

m.c59 = Constraint(expr=m.x129*m.x153 - (m.x128*m.x152 + m.x124*m.x33 + m.x132*m.x77 - (m.x128*m.x53 + m.x128*m.x57 + 
                        m.x128*m.x61 + m.x128*m.x65 + m.x128*m.x69)) - 0.6*m.x5 - 0.9*m.x17 == 0)

m.c60 = Constraint(expr=m.x131*m.x155 - (m.x130*m.x154 + m.x122*m.x35 + m.x126*m.x55 + m.x134*m.x95 - (m.x130*m.x71 + 
                        m.x130*m.x75 + m.x130*m.x79 + m.x130*m.x83 + m.x130*m.x87)) - 0.9*m.x19 == 0)

m.c61 = Constraint(expr=m.x132*m.x156 - (m.x131*m.x155 + m.x123*m.x36 + m.x127*m.x56 + m.x135*m.x96 - (m.x131*m.x72 + 
                        m.x131*m.x76 + m.x131*m.x80 + m.x131*m.x84 + m.x131*m.x88)) - 0.9*m.x20 == 0)

m.c62 = Constraint(expr=m.x133*m.x157 - (m.x132*m.x156 + m.x124*m.x37 + m.x128*m.x57 + m.x136*m.x97 - (m.x132*m.x73 + 
                        m.x132*m.x77 + m.x132*m.x81 + m.x132*m.x85 + m.x132*m.x89)) - 0.9*m.x21 == 0)

m.c63 = Constraint(expr=m.x135*m.x159 - (m.x134*m.x158 + m.x122*m.x39 + m.x126*m.x59 + m.x130*m.x79 - (m.x134*m.x91 + 
                        m.x134*m.x95 + m.x134*m.x99 + m.x134*m.x103)) - 0.9*m.x23 == 0)

m.c64 = Constraint(expr=m.x136*m.x160 - (m.x135*m.x159 + m.x123*m.x40 + m.x127*m.x60 + m.x131*m.x80 - (m.x135*m.x92 + 
                        m.x135*m.x96 + m.x135*m.x100 + m.x135*m.x104)) - 0.9*m.x24 == 0)

m.c65 = Constraint(expr=m.x137*m.x161 - (m.x136*m.x160 + m.x124*m.x41 + m.x128*m.x61 + m.x132*m.x81 - (m.x136*m.x93 + 
                        m.x136*m.x97 + m.x136*m.x101 + m.x136*m.x105)) - 0.9*m.x25 == 0)

m.c66 = Constraint(expr=   m.x2 - m.b170 <= 0)

m.c67 = Constraint(expr=   m.x3 - m.b171 <= 0)

m.c68 = Constraint(expr=   m.x4 - m.b172 <= 0)

m.c69 = Constraint(expr=   m.x5 - m.b173 <= 0)

m.c70 = Constraint(expr=   m.x6 - m.b174 <= 0)

m.c71 = Constraint(expr=   m.x7 - m.b175 <= 0)

m.c72 = Constraint(expr=   m.x8 - m.b176 <= 0)

m.c73 = Constraint(expr=   m.x9 - m.b177 <= 0)

m.c74 = Constraint(expr=   m.x10 - m.b178 <= 0)

m.c75 = Constraint(expr=   m.x11 - m.b179 <= 0)

m.c76 = Constraint(expr=   m.x12 - m.b180 <= 0)

m.c77 = Constraint(expr=   m.x13 - m.b181 <= 0)

m.c78 = Constraint(expr=   m.x14 - m.b182 <= 0)

m.c79 = Constraint(expr=   m.x15 - m.b183 <= 0)

m.c80 = Constraint(expr=   m.x16 - m.b184 <= 0)

m.c81 = Constraint(expr=   m.x17 - m.b185 <= 0)

m.c82 = Constraint(expr=   m.x18 - m.b186 <= 0)

m.c83 = Constraint(expr=   m.x19 - m.b187 <= 0)

m.c84 = Constraint(expr=   m.x20 - m.b188 <= 0)

m.c85 = Constraint(expr=   m.x21 - m.b189 <= 0)

m.c86 = Constraint(expr=   m.x22 - m.b190 <= 0)

m.c87 = Constraint(expr=   m.x23 - m.b191 <= 0)

m.c88 = Constraint(expr=   m.x24 - m.b192 <= 0)

m.c89 = Constraint(expr=   m.x25 - m.b193 <= 0)

m.c90 = Constraint(expr=   m.x26 - m.b194 <= 0)

m.c91 = Constraint(expr=   m.x27 - m.b195 <= 0)

m.c92 = Constraint(expr=   m.x28 - m.b196 <= 0)

m.c93 = Constraint(expr=   m.x29 - m.b197 <= 0)

m.c94 = Constraint(expr=   m.x30 - m.b198 <= 0)

m.c95 = Constraint(expr=   m.x31 - m.b199 <= 0)

m.c96 = Constraint(expr=   m.x32 - m.b200 <= 0)

m.c97 = Constraint(expr=   m.x33 - m.b201 <= 0)

m.c98 = Constraint(expr=   m.x34 - m.b202 <= 0)

m.c99 = Constraint(expr=   m.x35 - m.b203 <= 0)

m.c100 = Constraint(expr=   m.x36 - m.b204 <= 0)

m.c101 = Constraint(expr=   m.x37 - m.b205 <= 0)

m.c102 = Constraint(expr=   m.x38 - m.b206 <= 0)

m.c103 = Constraint(expr=   m.x39 - m.b207 <= 0)

m.c104 = Constraint(expr=   m.x40 - m.b208 <= 0)

m.c105 = Constraint(expr=   m.x41 - m.b209 <= 0)

m.c106 = Constraint(expr=   m.x42 - m.b210 <= 0)

m.c107 = Constraint(expr=   m.x43 - m.b211 <= 0)

m.c108 = Constraint(expr=   m.x44 - m.b212 <= 0)

m.c109 = Constraint(expr=   m.x45 - m.b213 <= 0)

m.c110 = Constraint(expr=   m.x46 - m.b214 <= 0)

m.c111 = Constraint(expr=   m.x47 - m.b215 <= 0)

m.c112 = Constraint(expr=   m.x48 - m.b216 <= 0)

m.c113 = Constraint(expr=   m.x49 - m.b217 <= 0)

m.c114 = Constraint(expr=   m.x50 - m.b218 <= 0)

m.c115 = Constraint(expr=   m.x51 - m.b219 <= 0)

m.c116 = Constraint(expr=   m.x52 - m.b220 <= 0)

m.c117 = Constraint(expr=   m.x53 - m.b221 <= 0)

m.c118 = Constraint(expr=   m.x54 - m.b222 <= 0)

m.c119 = Constraint(expr=   m.x55 - m.b223 <= 0)

m.c120 = Constraint(expr=   m.x56 - m.b224 <= 0)

m.c121 = Constraint(expr=   m.x57 - m.b225 <= 0)

m.c122 = Constraint(expr=   m.x58 - m.b226 <= 0)

m.c123 = Constraint(expr=   m.x59 - m.b227 <= 0)

m.c124 = Constraint(expr=   m.x60 - m.b228 <= 0)

m.c125 = Constraint(expr=   m.x61 - m.b229 <= 0)

m.c126 = Constraint(expr=   m.x62 - m.b230 <= 0)

m.c127 = Constraint(expr=   m.x63 - m.b231 <= 0)

m.c128 = Constraint(expr=   m.x64 - m.b232 <= 0)

m.c129 = Constraint(expr=   m.x65 - m.b233 <= 0)

m.c130 = Constraint(expr=   m.x66 - m.b234 <= 0)

m.c131 = Constraint(expr=   m.x67 - m.b235 <= 0)

m.c132 = Constraint(expr=   m.x68 - m.b236 <= 0)

m.c133 = Constraint(expr=   m.x69 - m.b237 <= 0)

m.c134 = Constraint(expr=   m.x70 - m.b238 <= 0)

m.c135 = Constraint(expr=   m.x71 - m.b239 <= 0)

m.c136 = Constraint(expr=   m.x72 - m.b240 <= 0)

m.c137 = Constraint(expr=   m.x73 - m.b241 <= 0)

m.c138 = Constraint(expr=   m.x74 - m.b242 <= 0)

m.c139 = Constraint(expr=   m.x75 - m.b243 <= 0)

m.c140 = Constraint(expr=   m.x76 - m.b244 <= 0)

m.c141 = Constraint(expr=   m.x77 - m.b245 <= 0)

m.c142 = Constraint(expr=   m.x78 - m.b246 <= 0)

m.c143 = Constraint(expr=   m.x79 - m.b247 <= 0)

m.c144 = Constraint(expr=   m.x80 - m.b248 <= 0)

m.c145 = Constraint(expr=   m.x81 - m.b249 <= 0)

m.c146 = Constraint(expr=   m.x82 - m.b250 <= 0)

m.c147 = Constraint(expr=   m.x83 - m.b251 <= 0)

m.c148 = Constraint(expr=   m.x84 - m.b252 <= 0)

m.c149 = Constraint(expr=   m.x85 - m.b253 <= 0)

m.c150 = Constraint(expr=   m.x86 - m.b254 <= 0)

m.c151 = Constraint(expr=   m.x87 - m.b255 <= 0)

m.c152 = Constraint(expr=   m.x88 - m.b256 <= 0)

m.c153 = Constraint(expr=   m.x89 - m.b257 <= 0)

m.c154 = Constraint(expr=   m.x90 - m.b258 <= 0)

m.c155 = Constraint(expr=   m.x91 - m.b259 <= 0)

m.c156 = Constraint(expr=   m.x92 - m.b260 <= 0)

m.c157 = Constraint(expr=   m.x93 - m.b261 <= 0)

m.c158 = Constraint(expr=   m.x94 - m.b262 <= 0)

m.c159 = Constraint(expr=   m.x95 - m.b263 <= 0)

m.c160 = Constraint(expr=   m.x96 - m.b264 <= 0)

m.c161 = Constraint(expr=   m.x97 - m.b265 <= 0)

m.c162 = Constraint(expr=   m.x98 - m.b266 <= 0)

m.c163 = Constraint(expr=   m.x99 - m.b267 <= 0)

m.c164 = Constraint(expr=   m.x100 - m.b268 <= 0)

m.c165 = Constraint(expr=   m.x101 - m.b269 <= 0)

m.c166 = Constraint(expr=   m.x102 - m.b270 <= 0)

m.c167 = Constraint(expr=   m.x103 - m.b271 <= 0)

m.c168 = Constraint(expr=   m.x104 - m.b272 <= 0)

m.c169 = Constraint(expr=   m.x105 - m.b273 <= 0)

m.c170 = Constraint(expr=   m.x2 >= 0)

m.c171 = Constraint(expr=   m.x3 >= 0)

m.c172 = Constraint(expr=   m.x4 >= 0)

m.c173 = Constraint(expr=   m.x5 >= 0)

m.c174 = Constraint(expr=   m.x6 >= 0)

m.c175 = Constraint(expr=   m.x7 >= 0)

m.c176 = Constraint(expr=   m.x8 >= 0)

m.c177 = Constraint(expr=   m.x9 >= 0)

m.c178 = Constraint(expr=   m.x10 >= 0)

m.c179 = Constraint(expr=   m.x11 >= 0)

m.c180 = Constraint(expr=   m.x12 >= 0)

m.c181 = Constraint(expr=   m.x13 >= 0)

m.c182 = Constraint(expr=   m.x14 >= 0)

m.c183 = Constraint(expr=   m.x15 >= 0)

m.c184 = Constraint(expr=   m.x16 >= 0)

m.c185 = Constraint(expr=   m.x17 >= 0)

m.c186 = Constraint(expr=   m.x18 >= 0)

m.c187 = Constraint(expr=   m.x19 >= 0)

m.c188 = Constraint(expr=   m.x20 >= 0)

m.c189 = Constraint(expr=   m.x21 >= 0)

m.c190 = Constraint(expr=   m.x22 >= 0)

m.c191 = Constraint(expr=   m.x23 >= 0)

m.c192 = Constraint(expr=   m.x24 >= 0)

m.c193 = Constraint(expr=   m.x25 >= 0)

m.c194 = Constraint(expr=   m.x26 >= 0)

m.c195 = Constraint(expr=   m.x27 >= 0)

m.c196 = Constraint(expr=   m.x28 >= 0)

m.c197 = Constraint(expr=   m.x29 >= 0)

m.c198 = Constraint(expr=   m.x30 >= 0)

m.c199 = Constraint(expr=   m.x31 >= 0)

m.c200 = Constraint(expr=   m.x32 >= 0)

m.c201 = Constraint(expr=   m.x33 >= 0)

m.c202 = Constraint(expr=   m.x34 >= 0)

m.c203 = Constraint(expr=   m.x35 >= 0)

m.c204 = Constraint(expr=   m.x36 >= 0)

m.c205 = Constraint(expr=   m.x37 >= 0)

m.c206 = Constraint(expr=   m.x38 >= 0)

m.c207 = Constraint(expr=   m.x39 >= 0)

m.c208 = Constraint(expr=   m.x40 >= 0)

m.c209 = Constraint(expr=   m.x41 >= 0)

m.c210 = Constraint(expr=   m.x42 >= 0)

m.c211 = Constraint(expr=   m.x43 >= 0)

m.c212 = Constraint(expr=   m.x44 >= 0)

m.c213 = Constraint(expr=   m.x45 >= 0)

m.c214 = Constraint(expr=   m.x46 >= 0)

m.c215 = Constraint(expr=   m.x47 >= 0)

m.c216 = Constraint(expr=   m.x48 >= 0)

m.c217 = Constraint(expr=   m.x49 >= 0)

m.c218 = Constraint(expr=   m.x50 >= 0)

m.c219 = Constraint(expr=   m.x51 >= 0)

m.c220 = Constraint(expr=   m.x52 >= 0)

m.c221 = Constraint(expr=   m.x53 >= 0)

m.c222 = Constraint(expr=   m.x54 >= 0)

m.c223 = Constraint(expr=   m.x55 >= 0)

m.c224 = Constraint(expr=   m.x56 >= 0)

m.c225 = Constraint(expr=   m.x57 >= 0)

m.c226 = Constraint(expr=   m.x58 >= 0)

m.c227 = Constraint(expr=   m.x59 >= 0)

m.c228 = Constraint(expr=   m.x60 >= 0)

m.c229 = Constraint(expr=   m.x61 >= 0)

m.c230 = Constraint(expr=   m.x62 >= 0)

m.c231 = Constraint(expr=   m.x63 >= 0)

m.c232 = Constraint(expr=   m.x64 >= 0)

m.c233 = Constraint(expr=   m.x65 >= 0)

m.c234 = Constraint(expr=   m.x66 >= 0)

m.c235 = Constraint(expr=   m.x67 >= 0)

m.c236 = Constraint(expr=   m.x68 >= 0)

m.c237 = Constraint(expr=   m.x69 >= 0)

m.c238 = Constraint(expr=   m.x70 >= 0)

m.c239 = Constraint(expr=   m.x71 >= 0)

m.c240 = Constraint(expr=   m.x72 >= 0)

m.c241 = Constraint(expr=   m.x73 >= 0)

m.c242 = Constraint(expr=   m.x74 >= 0)

m.c243 = Constraint(expr=   m.x75 >= 0)

m.c244 = Constraint(expr=   m.x76 >= 0)

m.c245 = Constraint(expr=   m.x77 >= 0)

m.c246 = Constraint(expr=   m.x78 >= 0)

m.c247 = Constraint(expr=   m.x79 >= 0)

m.c248 = Constraint(expr=   m.x80 >= 0)

m.c249 = Constraint(expr=   m.x81 >= 0)

m.c250 = Constraint(expr=   m.x82 >= 0)

m.c251 = Constraint(expr=   m.x83 >= 0)

m.c252 = Constraint(expr=   m.x84 >= 0)

m.c253 = Constraint(expr=   m.x85 >= 0)

m.c254 = Constraint(expr=   m.x86 >= 0)

m.c255 = Constraint(expr=   m.x87 >= 0)

m.c256 = Constraint(expr=   m.x88 >= 0)

m.c257 = Constraint(expr=   m.x89 >= 0)

m.c258 = Constraint(expr=   m.x90 >= 0)

m.c259 = Constraint(expr=   m.x91 >= 0)

m.c260 = Constraint(expr=   m.x92 >= 0)

m.c261 = Constraint(expr=   m.x93 >= 0)

m.c262 = Constraint(expr=   m.x94 >= 0)

m.c263 = Constraint(expr=   m.x95 >= 0)

m.c264 = Constraint(expr=   m.x96 >= 0)

m.c265 = Constraint(expr=   m.x97 >= 0)

m.c266 = Constraint(expr=   m.x98 >= 0)

m.c267 = Constraint(expr=   m.x99 >= 0)

m.c268 = Constraint(expr=   m.x100 >= 0)

m.c269 = Constraint(expr=   m.x101 >= 0)

m.c270 = Constraint(expr=   m.x102 >= 0)

m.c271 = Constraint(expr=   m.x103 >= 0)

m.c272 = Constraint(expr=   m.x104 >= 0)

m.c273 = Constraint(expr=   m.x105 >= 0)

m.c274 = Constraint(expr=   m.b174 <= 1.4)

m.c275 = Constraint(expr=   m.b175 <= 1.4)

m.c276 = Constraint(expr=   m.b176 <= 1.4)

m.c277 = Constraint(expr=   m.b177 <= 1.4)

m.c278 = Constraint(expr=   m.b194 <= 1.1)

m.c279 = Constraint(expr=   m.b195 <= 1.1)

m.c280 = Constraint(expr=   m.b196 <= 1.1)

m.c281 = Constraint(expr=   m.b197 <= 1.1)

m.c282 = Constraint(expr=   m.b174 <= 0.9)

m.c283 = Constraint(expr=   m.b175 <= 0.9)

m.c284 = Constraint(expr=   m.b176 <= 0.9)

m.c285 = Constraint(expr=   m.b177 <= 0.9)

m.c286 = Constraint(expr=   m.b194 <= 1.7)

m.c287 = Constraint(expr=   m.b195 <= 1.7)

m.c288 = Constraint(expr=   m.b196 <= 1.7)

m.c289 = Constraint(expr=   m.b197 <= 1.7)

m.c290 = Constraint(expr= - m.b174 >= -1)

m.c291 = Constraint(expr= - m.b175 >= -1)

m.c292 = Constraint(expr= - m.b176 >= -1)

m.c293 = Constraint(expr= - m.b177 >= -1)

m.c294 = Constraint(expr= - m.b194 >= -1.3)

m.c295 = Constraint(expr= - m.b195 >= -1.3)

m.c296 = Constraint(expr= - m.b196 >= -1.3)

m.c297 = Constraint(expr= - m.b197 >= -1.3)

m.c298 = Constraint(expr= - m.b174 >= -1.4)

m.c299 = Constraint(expr= - m.b175 >= -1.4)

m.c300 = Constraint(expr= - m.b176 >= -1.4)

m.c301 = Constraint(expr= - m.b177 >= -1.4)

m.c302 = Constraint(expr= - m.b194 >= -0.7)

m.c303 = Constraint(expr= - m.b195 >= -0.7)

m.c304 = Constraint(expr= - m.b196 >= -0.7)

m.c305 = Constraint(expr= - m.b197 >= -0.7)

m.c306 = Constraint(expr= - m.x106 + m.b211 <= 0.4)

m.c307 = Constraint(expr= - m.x107 + m.b212 <= 0.4)

m.c308 = Constraint(expr= - m.x108 + m.b213 <= 0.4)

m.c309 = Constraint(expr= - m.x106 + m.b215 <= 0.5)

m.c310 = Constraint(expr= - m.x107 + m.b216 <= 0.5)

m.c311 = Constraint(expr= - m.x108 + m.b217 <= 0.5)

m.c312 = Constraint(expr= - m.x110 + m.b231 <= 0.4)

m.c313 = Constraint(expr= - m.x111 + m.b232 <= 0.4)

m.c314 = Constraint(expr= - m.x112 + m.b233 <= 0.4)

m.c315 = Constraint(expr= - m.x110 + m.b235 <= 0.5)

m.c316 = Constraint(expr= - m.x111 + m.b236 <= 0.5)

m.c317 = Constraint(expr= - m.x112 + m.b237 <= 0.5)

m.c318 = Constraint(expr= - m.x114 + m.b251 <= 0.4)

m.c319 = Constraint(expr= - m.x115 + m.b252 <= 0.4)

m.c320 = Constraint(expr= - m.x116 + m.b253 <= 0.4)

m.c321 = Constraint(expr= - m.x114 + m.b255 <= 0.5)

m.c322 = Constraint(expr= - m.x115 + m.b256 <= 0.5)

m.c323 = Constraint(expr= - m.x116 + m.b257 <= 0.5)

m.c324 = Constraint(expr= - m.x118 + m.b267 <= 0.4)

m.c325 = Constraint(expr= - m.x119 + m.b268 <= 0.4)

m.c326 = Constraint(expr= - m.x120 + m.b269 <= 0.4)

m.c327 = Constraint(expr= - m.x118 + m.b271 <= 0.5)

m.c328 = Constraint(expr= - m.x119 + m.b272 <= 0.5)

m.c329 = Constraint(expr= - m.x120 + m.b273 <= 0.5)

m.c330 = Constraint(expr= - m.x122 + m.b211 <= 0.3)

m.c331 = Constraint(expr= - m.x123 + m.b212 <= 0.3)

m.c332 = Constraint(expr= - m.x124 + m.b213 <= 0.3)

m.c333 = Constraint(expr= - m.x122 + m.b215 <= 0.8)

m.c334 = Constraint(expr= - m.x123 + m.b216 <= 0.8)

m.c335 = Constraint(expr= - m.x124 + m.b217 <= 0.8)

m.c336 = Constraint(expr= - m.x126 + m.b231 <= 0.3)

m.c337 = Constraint(expr= - m.x127 + m.b232 <= 0.3)

m.c338 = Constraint(expr= - m.x128 + m.b233 <= 0.3)

m.c339 = Constraint(expr= - m.x126 + m.b235 <= 0.8)

m.c340 = Constraint(expr= - m.x127 + m.b236 <= 0.8)

m.c341 = Constraint(expr= - m.x128 + m.b237 <= 0.8)

m.c342 = Constraint(expr= - m.x130 + m.b251 <= 0.3)

m.c343 = Constraint(expr= - m.x131 + m.b252 <= 0.3)

m.c344 = Constraint(expr= - m.x132 + m.b253 <= 0.3)

m.c345 = Constraint(expr= - m.x130 + m.b255 <= 0.8)

m.c346 = Constraint(expr= - m.x131 + m.b256 <= 0.8)

m.c347 = Constraint(expr= - m.x132 + m.b257 <= 0.8)

m.c348 = Constraint(expr= - m.x134 + m.b267 <= 0.3)

m.c349 = Constraint(expr= - m.x135 + m.b268 <= 0.3)

m.c350 = Constraint(expr= - m.x136 + m.b269 <= 0.3)

m.c351 = Constraint(expr= - m.x134 + m.b271 <= 0.8)

m.c352 = Constraint(expr= - m.x135 + m.b272 <= 0.8)

m.c353 = Constraint(expr= - m.x136 + m.b273 <= 0.8)

m.c354 = Constraint(expr= - m.x106 - m.b211 >= -2)

m.c355 = Constraint(expr= - m.x107 - m.b212 >= -2)

m.c356 = Constraint(expr= - m.x108 - m.b213 >= -2)

m.c357 = Constraint(expr= - m.x106 - m.b215 >= -1.9)

m.c358 = Constraint(expr= - m.x107 - m.b216 >= -1.9)

m.c359 = Constraint(expr= - m.x108 - m.b217 >= -1.9)

m.c360 = Constraint(expr= - m.x110 - m.b231 >= -2)

m.c361 = Constraint(expr= - m.x111 - m.b232 >= -2)

m.c362 = Constraint(expr= - m.x112 - m.b233 >= -2)

m.c363 = Constraint(expr= - m.x110 - m.b235 >= -1.9)

m.c364 = Constraint(expr= - m.x111 - m.b236 >= -1.9)

m.c365 = Constraint(expr= - m.x112 - m.b237 >= -1.9)

m.c366 = Constraint(expr= - m.x114 - m.b251 >= -2)

m.c367 = Constraint(expr= - m.x115 - m.b252 >= -2)

m.c368 = Constraint(expr= - m.x116 - m.b253 >= -2)

m.c369 = Constraint(expr= - m.x114 - m.b255 >= -1.9)

m.c370 = Constraint(expr= - m.x115 - m.b256 >= -1.9)

m.c371 = Constraint(expr= - m.x116 - m.b257 >= -1.9)

m.c372 = Constraint(expr= - m.x118 - m.b267 >= -2)

m.c373 = Constraint(expr= - m.x119 - m.b268 >= -2)

m.c374 = Constraint(expr= - m.x120 - m.b269 >= -2)

m.c375 = Constraint(expr= - m.x118 - m.b271 >= -1.9)

m.c376 = Constraint(expr= - m.x119 - m.b272 >= -1.9)

m.c377 = Constraint(expr= - m.x120 - m.b273 >= -1.9)

m.c378 = Constraint(expr= - m.x122 - m.b211 >= -2)

m.c379 = Constraint(expr= - m.x123 - m.b212 >= -2)

m.c380 = Constraint(expr= - m.x124 - m.b213 >= -2)

m.c381 = Constraint(expr= - m.x122 - m.b215 >= -1.6)

m.c382 = Constraint(expr= - m.x123 - m.b216 >= -1.6)

m.c383 = Constraint(expr= - m.x124 - m.b217 >= -1.6)

m.c384 = Constraint(expr= - m.x126 - m.b231 >= -2)

m.c385 = Constraint(expr= - m.x127 - m.b232 >= -2)

m.c386 = Constraint(expr= - m.x128 - m.b233 >= -2)

m.c387 = Constraint(expr= - m.x126 - m.b235 >= -1.6)

m.c388 = Constraint(expr= - m.x127 - m.b236 >= -1.6)

m.c389 = Constraint(expr= - m.x128 - m.b237 >= -1.6)

m.c390 = Constraint(expr= - m.x130 - m.b251 >= -2)

m.c391 = Constraint(expr= - m.x131 - m.b252 >= -2)

m.c392 = Constraint(expr= - m.x132 - m.b253 >= -2)

m.c393 = Constraint(expr= - m.x130 - m.b255 >= -1.6)

m.c394 = Constraint(expr= - m.x131 - m.b256 >= -1.6)

m.c395 = Constraint(expr= - m.x132 - m.b257 >= -1.6)

m.c396 = Constraint(expr= - m.x134 - m.b267 >= -2)

m.c397 = Constraint(expr= - m.x135 - m.b268 >= -2)

m.c398 = Constraint(expr= - m.x136 - m.b269 >= -2)

m.c399 = Constraint(expr= - m.x134 - m.b271 >= -1.6)

m.c400 = Constraint(expr= - m.x135 - m.b272 >= -1.6)

m.c401 = Constraint(expr= - m.x136 - m.b273 >= -1.6)

m.c402 = Constraint(expr=   m.b210 <= 0.9)

m.c403 = Constraint(expr=   m.b214 <= 1)

m.c404 = Constraint(expr=   m.b230 <= 1.2)

m.c405 = Constraint(expr=   m.b234 <= 1.3)

m.c406 = Constraint(expr=   m.b250 <= 1.1)

m.c407 = Constraint(expr=   m.b254 <= 1.2)

m.c408 = Constraint(expr=   m.b266 <= 1.1)

m.c409 = Constraint(expr=   m.b270 <= 1.2)

m.c410 = Constraint(expr=   m.b210 <= 0.4)

m.c411 = Constraint(expr=   m.b214 <= 0.9)

m.c412 = Constraint(expr=   m.b230 <= 1.1)

m.c413 = Constraint(expr=   m.b234 <= 1.6)

m.c414 = Constraint(expr=   m.b250 <= 0.4)

m.c415 = Constraint(expr=   m.b254 <= 0.9)

m.c416 = Constraint(expr=   m.b266 <= 0.8)

m.c417 = Constraint(expr=   m.b270 <= 1.3)

m.c418 = Constraint(expr= - m.b210 >= -1.5)

m.c419 = Constraint(expr= - m.b214 >= -1.4)

m.c420 = Constraint(expr= - m.b230 >= -1.2)

m.c421 = Constraint(expr= - m.b234 >= -1.1)

m.c422 = Constraint(expr= - m.b250 >= -1.3)

m.c423 = Constraint(expr= - m.b254 >= -1.2)

m.c424 = Constraint(expr= - m.b266 >= -1.3)

m.c425 = Constraint(expr= - m.b270 >= -1.2)

m.c426 = Constraint(expr= - m.b210 >= -1.9)

m.c427 = Constraint(expr= - m.b214 >= -1.5)

m.c428 = Constraint(expr= - m.b230 >= -1.2)

m.c429 = Constraint(expr= - m.b234 >= -0.8)

m.c430 = Constraint(expr= - m.b250 >= -1.9)

m.c431 = Constraint(expr= - m.b254 >= -1.5)

m.c432 = Constraint(expr= - m.b266 >= -1.5)

m.c433 = Constraint(expr= - m.b270 >= -1.1)

m.c434 = Constraint(expr=   m.b178 + m.b198 <= 1)

m.c435 = Constraint(expr=   m.b179 + m.b199 <= 1)

m.c436 = Constraint(expr=   m.b180 + m.b200 <= 1)

m.c437 = Constraint(expr=   m.b181 + m.b201 <= 1)

m.c438 = Constraint(expr=   m.b178 + m.b202 <= 1)

m.c439 = Constraint(expr=   m.b179 + m.b203 <= 1)

m.c440 = Constraint(expr=   m.b180 + m.b204 <= 1)

m.c441 = Constraint(expr=   m.b181 + m.b205 <= 1)

m.c442 = Constraint(expr=   m.b178 + m.b206 <= 1)

m.c443 = Constraint(expr=   m.b179 + m.b207 <= 1)

m.c444 = Constraint(expr=   m.b180 + m.b208 <= 1)

m.c445 = Constraint(expr=   m.b181 + m.b209 <= 1)

m.c446 = Constraint(expr=   m.b178 + m.b210 <= 1)

m.c447 = Constraint(expr=   m.b179 + m.b211 <= 1)

m.c448 = Constraint(expr=   m.b180 + m.b212 <= 1)

m.c449 = Constraint(expr=   m.b181 + m.b213 <= 1)

m.c450 = Constraint(expr=   m.b178 + m.b214 <= 1)

m.c451 = Constraint(expr=   m.b179 + m.b215 <= 1)

m.c452 = Constraint(expr=   m.b180 + m.b216 <= 1)

m.c453 = Constraint(expr=   m.b181 + m.b217 <= 1)

m.c454 = Constraint(expr=   m.b198 + m.b218 <= 1)

m.c455 = Constraint(expr=   m.b199 + m.b219 <= 1)

m.c456 = Constraint(expr=   m.b200 + m.b220 <= 1)

m.c457 = Constraint(expr=   m.b201 + m.b221 <= 1)

m.c458 = Constraint(expr=   m.b202 + m.b218 <= 1)

m.c459 = Constraint(expr=   m.b203 + m.b219 <= 1)

m.c460 = Constraint(expr=   m.b204 + m.b220 <= 1)

m.c461 = Constraint(expr=   m.b205 + m.b221 <= 1)

m.c462 = Constraint(expr=   m.b206 + m.b218 <= 1)

m.c463 = Constraint(expr=   m.b207 + m.b219 <= 1)

m.c464 = Constraint(expr=   m.b208 + m.b220 <= 1)

m.c465 = Constraint(expr=   m.b209 + m.b221 <= 1)

m.c466 = Constraint(expr=   m.b210 + m.b218 <= 1)

m.c467 = Constraint(expr=   m.b211 + m.b219 <= 1)

m.c468 = Constraint(expr=   m.b212 + m.b220 <= 1)

m.c469 = Constraint(expr=   m.b213 + m.b221 <= 1)

m.c470 = Constraint(expr=   m.b214 + m.b218 <= 1)

m.c471 = Constraint(expr=   m.b215 + m.b219 <= 1)

m.c472 = Constraint(expr=   m.b216 + m.b220 <= 1)

m.c473 = Constraint(expr=   m.b217 + m.b221 <= 1)

m.c474 = Constraint(expr=   m.b198 + m.b238 <= 1)

m.c475 = Constraint(expr=   m.b199 + m.b239 <= 1)

m.c476 = Constraint(expr=   m.b200 + m.b240 <= 1)

m.c477 = Constraint(expr=   m.b201 + m.b241 <= 1)

m.c478 = Constraint(expr=   m.b202 + m.b238 <= 1)

m.c479 = Constraint(expr=   m.b203 + m.b239 <= 1)

m.c480 = Constraint(expr=   m.b204 + m.b240 <= 1)

m.c481 = Constraint(expr=   m.b205 + m.b241 <= 1)

m.c482 = Constraint(expr=   m.b206 + m.b238 <= 1)

m.c483 = Constraint(expr=   m.b207 + m.b239 <= 1)

m.c484 = Constraint(expr=   m.b208 + m.b240 <= 1)

m.c485 = Constraint(expr=   m.b209 + m.b241 <= 1)

m.c486 = Constraint(expr=   m.b210 + m.b238 <= 1)

m.c487 = Constraint(expr=   m.b211 + m.b239 <= 1)

m.c488 = Constraint(expr=   m.b212 + m.b240 <= 1)

m.c489 = Constraint(expr=   m.b213 + m.b241 <= 1)

m.c490 = Constraint(expr=   m.b214 + m.b238 <= 1)

m.c491 = Constraint(expr=   m.b215 + m.b239 <= 1)

m.c492 = Constraint(expr=   m.b216 + m.b240 <= 1)

m.c493 = Constraint(expr=   m.b217 + m.b241 <= 1)

m.c494 = Constraint(expr=   m.b198 + m.b258 <= 1)

m.c495 = Constraint(expr=   m.b199 + m.b259 <= 1)

m.c496 = Constraint(expr=   m.b200 + m.b260 <= 1)

m.c497 = Constraint(expr=   m.b201 + m.b261 <= 1)

m.c498 = Constraint(expr=   m.b202 + m.b258 <= 1)

m.c499 = Constraint(expr=   m.b203 + m.b259 <= 1)

m.c500 = Constraint(expr=   m.b204 + m.b260 <= 1)

m.c501 = Constraint(expr=   m.b205 + m.b261 <= 1)

m.c502 = Constraint(expr=   m.b206 + m.b258 <= 1)

m.c503 = Constraint(expr=   m.b207 + m.b259 <= 1)

m.c504 = Constraint(expr=   m.b208 + m.b260 <= 1)

m.c505 = Constraint(expr=   m.b209 + m.b261 <= 1)

m.c506 = Constraint(expr=   m.b210 + m.b258 <= 1)

m.c507 = Constraint(expr=   m.b211 + m.b259 <= 1)

m.c508 = Constraint(expr=   m.b212 + m.b260 <= 1)

m.c509 = Constraint(expr=   m.b213 + m.b261 <= 1)

m.c510 = Constraint(expr=   m.b214 + m.b258 <= 1)

m.c511 = Constraint(expr=   m.b215 + m.b259 <= 1)

m.c512 = Constraint(expr=   m.b216 + m.b260 <= 1)

m.c513 = Constraint(expr=   m.b217 + m.b261 <= 1)

m.c514 = Constraint(expr=   m.b170 + m.b218 <= 1)

m.c515 = Constraint(expr=   m.b171 + m.b219 <= 1)

m.c516 = Constraint(expr=   m.b172 + m.b220 <= 1)

m.c517 = Constraint(expr=   m.b173 + m.b221 <= 1)

m.c518 = Constraint(expr=   m.b170 + m.b222 <= 1)

m.c519 = Constraint(expr=   m.b171 + m.b223 <= 1)

m.c520 = Constraint(expr=   m.b172 + m.b224 <= 1)

m.c521 = Constraint(expr=   m.b173 + m.b225 <= 1)

m.c522 = Constraint(expr=   m.b170 + m.b226 <= 1)

m.c523 = Constraint(expr=   m.b171 + m.b227 <= 1)

m.c524 = Constraint(expr=   m.b172 + m.b228 <= 1)

m.c525 = Constraint(expr=   m.b173 + m.b229 <= 1)

m.c526 = Constraint(expr=   m.b170 + m.b230 <= 1)

m.c527 = Constraint(expr=   m.b171 + m.b231 <= 1)

m.c528 = Constraint(expr=   m.b172 + m.b232 <= 1)

m.c529 = Constraint(expr=   m.b173 + m.b233 <= 1)

m.c530 = Constraint(expr=   m.b170 + m.b234 <= 1)

m.c531 = Constraint(expr=   m.b171 + m.b235 <= 1)

m.c532 = Constraint(expr=   m.b172 + m.b236 <= 1)

m.c533 = Constraint(expr=   m.b173 + m.b237 <= 1)

m.c534 = Constraint(expr=   m.b182 + m.b218 <= 1)

m.c535 = Constraint(expr=   m.b183 + m.b219 <= 1)

m.c536 = Constraint(expr=   m.b184 + m.b220 <= 1)

m.c537 = Constraint(expr=   m.b185 + m.b221 <= 1)

m.c538 = Constraint(expr=   m.b182 + m.b222 <= 1)

m.c539 = Constraint(expr=   m.b183 + m.b223 <= 1)

m.c540 = Constraint(expr=   m.b184 + m.b224 <= 1)

m.c541 = Constraint(expr=   m.b185 + m.b225 <= 1)

m.c542 = Constraint(expr=   m.b182 + m.b226 <= 1)

m.c543 = Constraint(expr=   m.b183 + m.b227 <= 1)

m.c544 = Constraint(expr=   m.b184 + m.b228 <= 1)

m.c545 = Constraint(expr=   m.b185 + m.b229 <= 1)

m.c546 = Constraint(expr=   m.b182 + m.b230 <= 1)

m.c547 = Constraint(expr=   m.b183 + m.b231 <= 1)

m.c548 = Constraint(expr=   m.b184 + m.b232 <= 1)

m.c549 = Constraint(expr=   m.b185 + m.b233 <= 1)

m.c550 = Constraint(expr=   m.b182 + m.b234 <= 1)

m.c551 = Constraint(expr=   m.b183 + m.b235 <= 1)

m.c552 = Constraint(expr=   m.b184 + m.b236 <= 1)

m.c553 = Constraint(expr=   m.b185 + m.b237 <= 1)

m.c554 = Constraint(expr=   m.b198 + m.b218 <= 1)

m.c555 = Constraint(expr=   m.b199 + m.b219 <= 1)

m.c556 = Constraint(expr=   m.b200 + m.b220 <= 1)

m.c557 = Constraint(expr=   m.b201 + m.b221 <= 1)

m.c558 = Constraint(expr=   m.b198 + m.b222 <= 1)

m.c559 = Constraint(expr=   m.b199 + m.b223 <= 1)

m.c560 = Constraint(expr=   m.b200 + m.b224 <= 1)

m.c561 = Constraint(expr=   m.b201 + m.b225 <= 1)

m.c562 = Constraint(expr=   m.b198 + m.b226 <= 1)

m.c563 = Constraint(expr=   m.b199 + m.b227 <= 1)

m.c564 = Constraint(expr=   m.b200 + m.b228 <= 1)

m.c565 = Constraint(expr=   m.b201 + m.b229 <= 1)

m.c566 = Constraint(expr=   m.b198 + m.b230 <= 1)

m.c567 = Constraint(expr=   m.b199 + m.b231 <= 1)

m.c568 = Constraint(expr=   m.b200 + m.b232 <= 1)

m.c569 = Constraint(expr=   m.b201 + m.b233 <= 1)

m.c570 = Constraint(expr=   m.b198 + m.b234 <= 1)

m.c571 = Constraint(expr=   m.b199 + m.b235 <= 1)

m.c572 = Constraint(expr=   m.b200 + m.b236 <= 1)

m.c573 = Constraint(expr=   m.b201 + m.b237 <= 1)

m.c574 = Constraint(expr=   m.b218 + m.b242 <= 1)

m.c575 = Constraint(expr=   m.b219 + m.b243 <= 1)

m.c576 = Constraint(expr=   m.b220 + m.b244 <= 1)

m.c577 = Constraint(expr=   m.b221 + m.b245 <= 1)

m.c578 = Constraint(expr=   m.b222 + m.b242 <= 1)

m.c579 = Constraint(expr=   m.b223 + m.b243 <= 1)

m.c580 = Constraint(expr=   m.b224 + m.b244 <= 1)

m.c581 = Constraint(expr=   m.b225 + m.b245 <= 1)

m.c582 = Constraint(expr=   m.b226 + m.b242 <= 1)

m.c583 = Constraint(expr=   m.b227 + m.b243 <= 1)

m.c584 = Constraint(expr=   m.b228 + m.b244 <= 1)

m.c585 = Constraint(expr=   m.b229 + m.b245 <= 1)

m.c586 = Constraint(expr=   m.b230 + m.b242 <= 1)

m.c587 = Constraint(expr=   m.b231 + m.b243 <= 1)

m.c588 = Constraint(expr=   m.b232 + m.b244 <= 1)

m.c589 = Constraint(expr=   m.b233 + m.b245 <= 1)

m.c590 = Constraint(expr=   m.b234 + m.b242 <= 1)

m.c591 = Constraint(expr=   m.b235 + m.b243 <= 1)

m.c592 = Constraint(expr=   m.b236 + m.b244 <= 1)

m.c593 = Constraint(expr=   m.b237 + m.b245 <= 1)

m.c594 = Constraint(expr=   m.b186 + m.b238 <= 1)

m.c595 = Constraint(expr=   m.b187 + m.b239 <= 1)

m.c596 = Constraint(expr=   m.b188 + m.b240 <= 1)

m.c597 = Constraint(expr=   m.b189 + m.b241 <= 1)

m.c598 = Constraint(expr=   m.b186 + m.b242 <= 1)

m.c599 = Constraint(expr=   m.b187 + m.b243 <= 1)

m.c600 = Constraint(expr=   m.b188 + m.b244 <= 1)

m.c601 = Constraint(expr=   m.b189 + m.b245 <= 1)

m.c602 = Constraint(expr=   m.b186 + m.b246 <= 1)

m.c603 = Constraint(expr=   m.b187 + m.b247 <= 1)

m.c604 = Constraint(expr=   m.b188 + m.b248 <= 1)

m.c605 = Constraint(expr=   m.b189 + m.b249 <= 1)

m.c606 = Constraint(expr=   m.b186 + m.b250 <= 1)

m.c607 = Constraint(expr=   m.b187 + m.b251 <= 1)

m.c608 = Constraint(expr=   m.b188 + m.b252 <= 1)

m.c609 = Constraint(expr=   m.b189 + m.b253 <= 1)

m.c610 = Constraint(expr=   m.b186 + m.b254 <= 1)

m.c611 = Constraint(expr=   m.b187 + m.b255 <= 1)

m.c612 = Constraint(expr=   m.b188 + m.b256 <= 1)

m.c613 = Constraint(expr=   m.b189 + m.b257 <= 1)

m.c614 = Constraint(expr=   m.b202 + m.b238 <= 1)

m.c615 = Constraint(expr=   m.b203 + m.b239 <= 1)

m.c616 = Constraint(expr=   m.b204 + m.b240 <= 1)

m.c617 = Constraint(expr=   m.b205 + m.b241 <= 1)

m.c618 = Constraint(expr=   m.b202 + m.b242 <= 1)

m.c619 = Constraint(expr=   m.b203 + m.b243 <= 1)

m.c620 = Constraint(expr=   m.b204 + m.b244 <= 1)

m.c621 = Constraint(expr=   m.b205 + m.b245 <= 1)

m.c622 = Constraint(expr=   m.b202 + m.b246 <= 1)

m.c623 = Constraint(expr=   m.b203 + m.b247 <= 1)

m.c624 = Constraint(expr=   m.b204 + m.b248 <= 1)

m.c625 = Constraint(expr=   m.b205 + m.b249 <= 1)

m.c626 = Constraint(expr=   m.b202 + m.b250 <= 1)

m.c627 = Constraint(expr=   m.b203 + m.b251 <= 1)

m.c628 = Constraint(expr=   m.b204 + m.b252 <= 1)

m.c629 = Constraint(expr=   m.b205 + m.b253 <= 1)

m.c630 = Constraint(expr=   m.b202 + m.b254 <= 1)

m.c631 = Constraint(expr=   m.b203 + m.b255 <= 1)

m.c632 = Constraint(expr=   m.b204 + m.b256 <= 1)

m.c633 = Constraint(expr=   m.b205 + m.b257 <= 1)

m.c634 = Constraint(expr=   m.b222 + m.b238 <= 1)

m.c635 = Constraint(expr=   m.b223 + m.b239 <= 1)

m.c636 = Constraint(expr=   m.b224 + m.b240 <= 1)

m.c637 = Constraint(expr=   m.b225 + m.b241 <= 1)

m.c638 = Constraint(expr=   m.b222 + m.b242 <= 1)

m.c639 = Constraint(expr=   m.b223 + m.b243 <= 1)

m.c640 = Constraint(expr=   m.b224 + m.b244 <= 1)

m.c641 = Constraint(expr=   m.b225 + m.b245 <= 1)

m.c642 = Constraint(expr=   m.b222 + m.b246 <= 1)

m.c643 = Constraint(expr=   m.b223 + m.b247 <= 1)

m.c644 = Constraint(expr=   m.b224 + m.b248 <= 1)

m.c645 = Constraint(expr=   m.b225 + m.b249 <= 1)

m.c646 = Constraint(expr=   m.b222 + m.b250 <= 1)

m.c647 = Constraint(expr=   m.b223 + m.b251 <= 1)

m.c648 = Constraint(expr=   m.b224 + m.b252 <= 1)

m.c649 = Constraint(expr=   m.b225 + m.b253 <= 1)

m.c650 = Constraint(expr=   m.b222 + m.b254 <= 1)

m.c651 = Constraint(expr=   m.b223 + m.b255 <= 1)

m.c652 = Constraint(expr=   m.b224 + m.b256 <= 1)

m.c653 = Constraint(expr=   m.b225 + m.b257 <= 1)

m.c654 = Constraint(expr=   m.b238 + m.b262 <= 1)

m.c655 = Constraint(expr=   m.b239 + m.b263 <= 1)

m.c656 = Constraint(expr=   m.b240 + m.b264 <= 1)

m.c657 = Constraint(expr=   m.b241 + m.b265 <= 1)

m.c658 = Constraint(expr=   m.b242 + m.b262 <= 1)

m.c659 = Constraint(expr=   m.b243 + m.b263 <= 1)

m.c660 = Constraint(expr=   m.b244 + m.b264 <= 1)

m.c661 = Constraint(expr=   m.b245 + m.b265 <= 1)

m.c662 = Constraint(expr=   m.b246 + m.b262 <= 1)

m.c663 = Constraint(expr=   m.b247 + m.b263 <= 1)

m.c664 = Constraint(expr=   m.b248 + m.b264 <= 1)

m.c665 = Constraint(expr=   m.b249 + m.b265 <= 1)

m.c666 = Constraint(expr=   m.b250 + m.b262 <= 1)

m.c667 = Constraint(expr=   m.b251 + m.b263 <= 1)

m.c668 = Constraint(expr=   m.b252 + m.b264 <= 1)

m.c669 = Constraint(expr=   m.b253 + m.b265 <= 1)

m.c670 = Constraint(expr=   m.b254 + m.b262 <= 1)

m.c671 = Constraint(expr=   m.b255 + m.b263 <= 1)

m.c672 = Constraint(expr=   m.b256 + m.b264 <= 1)

m.c673 = Constraint(expr=   m.b257 + m.b265 <= 1)

m.c674 = Constraint(expr=   m.b190 + m.b258 <= 1)

m.c675 = Constraint(expr=   m.b191 + m.b259 <= 1)

m.c676 = Constraint(expr=   m.b192 + m.b260 <= 1)

m.c677 = Constraint(expr=   m.b193 + m.b261 <= 1)

m.c678 = Constraint(expr=   m.b190 + m.b262 <= 1)

m.c679 = Constraint(expr=   m.b191 + m.b263 <= 1)

m.c680 = Constraint(expr=   m.b192 + m.b264 <= 1)

m.c681 = Constraint(expr=   m.b193 + m.b265 <= 1)

m.c682 = Constraint(expr=   m.b190 + m.b266 <= 1)

m.c683 = Constraint(expr=   m.b191 + m.b267 <= 1)

m.c684 = Constraint(expr=   m.b192 + m.b268 <= 1)

m.c685 = Constraint(expr=   m.b193 + m.b269 <= 1)

m.c686 = Constraint(expr=   m.b190 + m.b270 <= 1)

m.c687 = Constraint(expr=   m.b191 + m.b271 <= 1)

m.c688 = Constraint(expr=   m.b192 + m.b272 <= 1)

m.c689 = Constraint(expr=   m.b193 + m.b273 <= 1)

m.c690 = Constraint(expr=   m.b206 + m.b258 <= 1)

m.c691 = Constraint(expr=   m.b207 + m.b259 <= 1)

m.c692 = Constraint(expr=   m.b208 + m.b260 <= 1)

m.c693 = Constraint(expr=   m.b209 + m.b261 <= 1)

m.c694 = Constraint(expr=   m.b206 + m.b262 <= 1)

m.c695 = Constraint(expr=   m.b207 + m.b263 <= 1)

m.c696 = Constraint(expr=   m.b208 + m.b264 <= 1)

m.c697 = Constraint(expr=   m.b209 + m.b265 <= 1)

m.c698 = Constraint(expr=   m.b206 + m.b266 <= 1)

m.c699 = Constraint(expr=   m.b207 + m.b267 <= 1)

m.c700 = Constraint(expr=   m.b208 + m.b268 <= 1)

m.c701 = Constraint(expr=   m.b209 + m.b269 <= 1)

m.c702 = Constraint(expr=   m.b206 + m.b270 <= 1)

m.c703 = Constraint(expr=   m.b207 + m.b271 <= 1)

m.c704 = Constraint(expr=   m.b208 + m.b272 <= 1)

m.c705 = Constraint(expr=   m.b209 + m.b273 <= 1)

m.c706 = Constraint(expr=   m.b226 + m.b258 <= 1)

m.c707 = Constraint(expr=   m.b227 + m.b259 <= 1)

m.c708 = Constraint(expr=   m.b228 + m.b260 <= 1)

m.c709 = Constraint(expr=   m.b229 + m.b261 <= 1)

m.c710 = Constraint(expr=   m.b226 + m.b262 <= 1)

m.c711 = Constraint(expr=   m.b227 + m.b263 <= 1)

m.c712 = Constraint(expr=   m.b228 + m.b264 <= 1)

m.c713 = Constraint(expr=   m.b229 + m.b265 <= 1)

m.c714 = Constraint(expr=   m.b226 + m.b266 <= 1)

m.c715 = Constraint(expr=   m.b227 + m.b267 <= 1)

m.c716 = Constraint(expr=   m.b228 + m.b268 <= 1)

m.c717 = Constraint(expr=   m.b229 + m.b269 <= 1)

m.c718 = Constraint(expr=   m.b226 + m.b270 <= 1)

m.c719 = Constraint(expr=   m.b227 + m.b271 <= 1)

m.c720 = Constraint(expr=   m.b228 + m.b272 <= 1)

m.c721 = Constraint(expr=   m.b229 + m.b273 <= 1)

m.c722 = Constraint(expr=   m.b246 + m.b258 <= 1)

m.c723 = Constraint(expr=   m.b247 + m.b259 <= 1)

m.c724 = Constraint(expr=   m.b248 + m.b260 <= 1)

m.c725 = Constraint(expr=   m.b249 + m.b261 <= 1)

m.c726 = Constraint(expr=   m.b246 + m.b262 <= 1)

m.c727 = Constraint(expr=   m.b247 + m.b263 <= 1)

m.c728 = Constraint(expr=   m.b248 + m.b264 <= 1)

m.c729 = Constraint(expr=   m.b249 + m.b265 <= 1)

m.c730 = Constraint(expr=   m.b246 + m.b266 <= 1)

m.c731 = Constraint(expr=   m.b247 + m.b267 <= 1)

m.c732 = Constraint(expr=   m.b248 + m.b268 <= 1)

m.c733 = Constraint(expr=   m.b249 + m.b269 <= 1)

m.c734 = Constraint(expr=   m.b246 + m.b270 <= 1)

m.c735 = Constraint(expr=   m.b247 + m.b271 <= 1)

m.c736 = Constraint(expr=   m.b248 + m.b272 <= 1)

m.c737 = Constraint(expr=   m.b249 + m.b273 <= 1)
