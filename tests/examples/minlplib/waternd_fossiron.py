#  MINLP written by GAMS Convert at 04/21/18 13:55:13
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        327      211       58       58        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        908      154      754        0        0        0        0        0
#  FX      1        1        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       2900     2668      232        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(105.15,121),initialize=105.15)
m.x2 = Var(within=Reals,bounds=(104.4,121),initialize=104.4)
m.x3 = Var(within=Reals,bounds=(103.35,121),initialize=103.35)
m.x4 = Var(within=Reals,bounds=(102.5,121),initialize=102.5)
m.x5 = Var(within=Reals,bounds=(101.24,121),initialize=101.24)
m.x6 = Var(within=Reals,bounds=(105.4,121),initialize=105.4)
m.x7 = Var(within=Reals,bounds=(107.9,121),initialize=107.9)
m.x8 = Var(within=Reals,bounds=(106.5,121),initialize=106.5)
m.x9 = Var(within=Reals,bounds=(106,121),initialize=106)
m.x10 = Var(within=Reals,bounds=(104.17,121),initialize=104.17)
m.x11 = Var(within=Reals,bounds=(103.7,121),initialize=103.7)
m.x12 = Var(within=Reals,bounds=(102.64,121),initialize=102.64)
m.x13 = Var(within=Reals,bounds=(101.9,121),initialize=101.9)
m.x14 = Var(within=Reals,bounds=(102.6,121),initialize=102.6)
m.x15 = Var(within=Reals,bounds=(103.5,121),initialize=103.5)
m.x16 = Var(within=Reals,bounds=(104.3,121),initialize=104.3)
m.x17 = Var(within=Reals,bounds=(105.5,121),initialize=105.5)
m.x18 = Var(within=Reals,bounds=(104.1,121),initialize=104.1)
m.x19 = Var(within=Reals,bounds=(102.9,121),initialize=102.9)
m.x20 = Var(within=Reals,bounds=(102.83,121),initialize=102.83)
m.x21 = Var(within=Reals,bounds=(102.8,121),initialize=102.8)
m.x22 = Var(within=Reals,bounds=(103.9,121),initialize=103.9)
m.x23 = Var(within=Reals,bounds=(104.2,121),initialize=104.2)
m.x24 = Var(within=Reals,bounds=(107.5,121),initialize=107.5)
m.x25 = Var(within=Reals,bounds=(104.4,121),initialize=104.4)
m.x26 = Var(within=Reals,bounds=(103.4,121),initialize=103.4)
m.x27 = Var(within=Reals,bounds=(103.9,121),initialize=103.9)
m.x28 = Var(within=Reals,bounds=(105.65,121),initialize=105.65)
m.x29 = Var(within=Reals,bounds=(104.5,121),initialize=104.5)
m.x30 = Var(within=Reals,bounds=(104.1,121),initialize=104.1)
m.x31 = Var(within=Reals,bounds=(104.4,121),initialize=104.4)
m.x32 = Var(within=Reals,bounds=(104.2,121),initialize=104.2)
m.x33 = Var(within=Reals,bounds=(104.6,121),initialize=104.6)
m.x34 = Var(within=Reals,bounds=(104.7,121),initialize=104.7)
m.x35 = Var(within=Reals,bounds=(105.43,121),initialize=105.43)
m.x36 = Var(within=Reals,bounds=(105.9,121),initialize=105.9)
m.x37 = Var(within=Reals,bounds=(121,121),initialize=121)
m.x38 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x39 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x40 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x41 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x42 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x43 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x44 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x45 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x46 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x47 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x48 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x49 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x50 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x51 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x52 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x53 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x54 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x55 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x56 = Var(within=Reals,bounds=(None,None),initialize=0)
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
m.x96 = Var(within=Reals,bounds=(0.00282743338823081,0.282743338823081),initialize=0.00282743338823081)
m.x97 = Var(within=Reals,bounds=(0.00282743338823081,0.282743338823081),initialize=0.00282743338823081)
m.x98 = Var(within=Reals,bounds=(0.00282743338823081,0.282743338823081),initialize=0.00282743338823081)
m.x99 = Var(within=Reals,bounds=(0.00282743338823081,0.282743338823081),initialize=0.00282743338823081)
m.x100 = Var(within=Reals,bounds=(0.00282743338823081,0.282743338823081),initialize=0.00282743338823081)
m.x101 = Var(within=Reals,bounds=(0.00282743338823081,0.282743338823081),initialize=0.00282743338823081)
m.x102 = Var(within=Reals,bounds=(0.00282743338823081,0.282743338823081),initialize=0.00282743338823081)
m.x103 = Var(within=Reals,bounds=(0.00282743338823081,0.282743338823081),initialize=0.00282743338823081)
m.x104 = Var(within=Reals,bounds=(0.00282743338823081,0.282743338823081),initialize=0.00282743338823081)
m.x105 = Var(within=Reals,bounds=(0.00282743338823081,0.282743338823081),initialize=0.00282743338823081)
m.x106 = Var(within=Reals,bounds=(0.00282743338823081,0.282743338823081),initialize=0.00282743338823081)
m.x107 = Var(within=Reals,bounds=(0.00282743338823081,0.282743338823081),initialize=0.00282743338823081)
m.x108 = Var(within=Reals,bounds=(0.00282743338823081,0.282743338823081),initialize=0.00282743338823081)
m.x109 = Var(within=Reals,bounds=(0.00282743338823081,0.282743338823081),initialize=0.00282743338823081)
m.x110 = Var(within=Reals,bounds=(0.00282743338823081,0.282743338823081),initialize=0.00282743338823081)
m.x111 = Var(within=Reals,bounds=(0.00282743338823081,0.282743338823081),initialize=0.00282743338823081)
m.x112 = Var(within=Reals,bounds=(0.00282743338823081,0.282743338823081),initialize=0.00282743338823081)
m.x113 = Var(within=Reals,bounds=(0.00282743338823081,0.282743338823081),initialize=0.00282743338823081)
m.x114 = Var(within=Reals,bounds=(0.00282743338823081,0.282743338823081),initialize=0.00282743338823081)
m.x115 = Var(within=Reals,bounds=(0.00282743338823081,0.282743338823081),initialize=0.00282743338823081)
m.x116 = Var(within=Reals,bounds=(0.00282743338823081,0.282743338823081),initialize=0.00282743338823081)
m.x117 = Var(within=Reals,bounds=(0.00282743338823081,0.282743338823081),initialize=0.00282743338823081)
m.x118 = Var(within=Reals,bounds=(0.00282743338823081,0.282743338823081),initialize=0.00282743338823081)
m.x119 = Var(within=Reals,bounds=(0.00282743338823081,0.282743338823081),initialize=0.00282743338823081)
m.x120 = Var(within=Reals,bounds=(0.00282743338823081,0.282743338823081),initialize=0.00282743338823081)
m.x121 = Var(within=Reals,bounds=(0.00282743338823081,0.282743338823081),initialize=0.00282743338823081)
m.x122 = Var(within=Reals,bounds=(0.00282743338823081,0.282743338823081),initialize=0.00282743338823081)
m.x123 = Var(within=Reals,bounds=(0.00282743338823081,0.282743338823081),initialize=0.00282743338823081)
m.x124 = Var(within=Reals,bounds=(0.00282743338823081,0.282743338823081),initialize=0.00282743338823081)
m.x125 = Var(within=Reals,bounds=(0.00282743338823081,0.282743338823081),initialize=0.00282743338823081)
m.x126 = Var(within=Reals,bounds=(0.00282743338823081,0.282743338823081),initialize=0.00282743338823081)
m.x127 = Var(within=Reals,bounds=(0.00282743338823081,0.282743338823081),initialize=0.00282743338823081)
m.x128 = Var(within=Reals,bounds=(0.00282743338823081,0.282743338823081),initialize=0.00282743338823081)
m.x129 = Var(within=Reals,bounds=(0.00282743338823081,0.282743338823081),initialize=0.00282743338823081)
m.x130 = Var(within=Reals,bounds=(0.00282743338823081,0.282743338823081),initialize=0.00282743338823081)
m.x131 = Var(within=Reals,bounds=(0.00282743338823081,0.282743338823081),initialize=0.00282743338823081)
m.x132 = Var(within=Reals,bounds=(0.00282743338823081,0.282743338823081),initialize=0.00282743338823081)
m.x133 = Var(within=Reals,bounds=(0.00282743338823081,0.282743338823081),initialize=0.00282743338823081)
m.x134 = Var(within=Reals,bounds=(0.00282743338823081,0.282743338823081),initialize=0.00282743338823081)
m.x135 = Var(within=Reals,bounds=(0.00282743338823081,0.282743338823081),initialize=0.00282743338823081)
m.x136 = Var(within=Reals,bounds=(0.00282743338823081,0.282743338823081),initialize=0.00282743338823081)
m.x137 = Var(within=Reals,bounds=(0.00282743338823081,0.282743338823081),initialize=0.00282743338823081)
m.x138 = Var(within=Reals,bounds=(0.00282743338823081,0.282743338823081),initialize=0.00282743338823081)
m.x139 = Var(within=Reals,bounds=(0.00282743338823081,0.282743338823081),initialize=0.00282743338823081)
m.x140 = Var(within=Reals,bounds=(0.00282743338823081,0.282743338823081),initialize=0.00282743338823081)
m.x141 = Var(within=Reals,bounds=(0.00282743338823081,0.282743338823081),initialize=0.00282743338823081)
m.x142 = Var(within=Reals,bounds=(0.00282743338823081,0.282743338823081),initialize=0.00282743338823081)
m.x143 = Var(within=Reals,bounds=(0.00282743338823081,0.282743338823081),initialize=0.00282743338823081)
m.x144 = Var(within=Reals,bounds=(0.00282743338823081,0.282743338823081),initialize=0.00282743338823081)
m.x145 = Var(within=Reals,bounds=(0.00282743338823081,0.282743338823081),initialize=0.00282743338823081)
m.x146 = Var(within=Reals,bounds=(0.00282743338823081,0.282743338823081),initialize=0.00282743338823081)
m.x147 = Var(within=Reals,bounds=(0.00282743338823081,0.282743338823081),initialize=0.00282743338823081)
m.x148 = Var(within=Reals,bounds=(0.00282743338823081,0.282743338823081),initialize=0.00282743338823081)
m.x149 = Var(within=Reals,bounds=(0.00282743338823081,0.282743338823081),initialize=0.00282743338823081)
m.x150 = Var(within=Reals,bounds=(0.00282743338823081,0.282743338823081),initialize=0.00282743338823081)
m.x151 = Var(within=Reals,bounds=(0.00282743338823081,0.282743338823081),initialize=0.00282743338823081)
m.x152 = Var(within=Reals,bounds=(0.00282743338823081,0.282743338823081),initialize=0.00282743338823081)
m.x153 = Var(within=Reals,bounds=(0.00282743338823081,0.282743338823081),initialize=0.00282743338823081)
m.b154 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b155 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b156 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b157 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b158 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b159 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b160 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b161 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b162 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b163 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b164 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b165 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b166 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b167 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b168 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b169 = Var(within=Binary,bounds=(0,1),initialize=0)
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
m.b306 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b307 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b308 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b309 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b310 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b311 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b312 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b313 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b314 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b315 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b316 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b317 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b318 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b319 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b320 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b321 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b322 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b323 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b324 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b325 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b326 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b327 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b328 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b329 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b330 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b331 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b332 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b333 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b334 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b335 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b336 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b337 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b338 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b339 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b340 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b341 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b342 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b343 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b344 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b345 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b346 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b347 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b348 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b349 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b350 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b351 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b352 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b353 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b354 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b355 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b356 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b357 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b358 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b359 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b360 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b361 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b362 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b363 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b364 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b365 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b366 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b367 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b368 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b369 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b370 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b371 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b372 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b373 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b374 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b375 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b376 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b377 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b378 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b379 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b380 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b381 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b382 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b383 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b384 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b385 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b386 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b387 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b388 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b389 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b390 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b391 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b392 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b393 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b394 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b395 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b396 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b397 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b398 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b399 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b400 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b401 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b402 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b403 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b404 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b405 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b406 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b407 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b408 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b409 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b410 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b411 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b412 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b413 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b414 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b415 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b416 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b417 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b418 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b419 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b420 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b421 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b422 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b423 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b424 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b425 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b426 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b427 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b428 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b429 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b430 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b431 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b432 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b433 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b434 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b435 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b436 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b437 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b438 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b439 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b440 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b441 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b442 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b443 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b444 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b445 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b446 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b447 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b448 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b449 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b450 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b451 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b452 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b453 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b454 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b455 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b456 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b457 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b458 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b459 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b460 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b461 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b462 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b463 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b464 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b465 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b466 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b467 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b468 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b469 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b470 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b471 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b472 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b473 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b474 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b475 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b476 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b477 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b478 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b479 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b480 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b481 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b482 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b483 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b484 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b485 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b486 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b487 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b488 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b489 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b490 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b491 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b492 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b493 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b494 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b495 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b496 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b497 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b498 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b499 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b500 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b501 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b502 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b503 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b504 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b505 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b506 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b507 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b508 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b509 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b510 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b511 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b512 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b513 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b514 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b515 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b516 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b517 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b518 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b519 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b520 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b521 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b522 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b523 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b524 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b525 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b526 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b527 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b528 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b529 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b530 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b531 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b532 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b533 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b534 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b535 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b536 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b537 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b538 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b539 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b540 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b541 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b542 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b543 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b544 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b545 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b546 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b547 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b548 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b549 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b550 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b551 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b552 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b553 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b554 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b555 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b556 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b557 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b558 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b559 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b560 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b561 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b562 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b563 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b564 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b565 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b566 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b567 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b568 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b569 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b570 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b571 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b572 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b573 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b574 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b575 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b576 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b577 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b578 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b579 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b580 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b581 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b582 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b583 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b584 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b585 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b586 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b587 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b588 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b589 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b590 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b591 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b592 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b593 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b594 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b595 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b596 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b597 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b598 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b599 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b600 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b601 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b602 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b603 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b604 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b605 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b606 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b607 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b608 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b609 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b610 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b611 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b612 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b613 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b614 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b615 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b616 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b617 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b618 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b619 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b620 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b621 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b622 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b623 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b624 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b625 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b626 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b627 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b628 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b629 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b630 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b631 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b632 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b633 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b634 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b635 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b636 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b637 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b638 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b639 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b640 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b641 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b642 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b643 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b644 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b645 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b646 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b647 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b648 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b649 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b650 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b651 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b652 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b653 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b654 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b655 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b656 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b657 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b658 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b659 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b660 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b661 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b662 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b663 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b664 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b665 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b666 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b667 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b668 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b669 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b670 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b671 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b672 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b673 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b674 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b675 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b676 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b677 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b678 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b679 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b680 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b681 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b682 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b683 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b684 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b685 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b686 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b687 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b688 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b689 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b690 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b691 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b692 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b693 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b694 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b695 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b696 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b697 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b698 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b699 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b700 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b701 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b702 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b703 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b704 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b705 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b706 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b707 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b708 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b709 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b710 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b711 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b712 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b713 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b714 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b715 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b716 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b717 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b718 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b719 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b720 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b721 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b722 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b723 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b724 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b725 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b726 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b727 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b728 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b729 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b730 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b731 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b732 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b733 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b734 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b735 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b736 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b737 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b738 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b739 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b740 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b741 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b742 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b743 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b744 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b745 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b746 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b747 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b748 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b749 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b750 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b751 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b752 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b753 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b754 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b755 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b756 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b757 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b758 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b759 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b760 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b761 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b762 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b763 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b764 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b765 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b766 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b767 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b768 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b769 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b770 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b771 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b772 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b773 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b774 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b775 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b776 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b777 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b778 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b779 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b780 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b781 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b782 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b783 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b784 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b785 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b786 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b787 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b788 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b789 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b790 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b791 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b792 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b793 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b794 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b795 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b796 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b797 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b798 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b799 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b800 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b801 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b802 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b803 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b804 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b805 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b806 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b807 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b808 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b809 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b810 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b811 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b812 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b813 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b814 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b815 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b816 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b817 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b818 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b819 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b820 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b821 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b822 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b823 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b824 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b825 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b826 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b827 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b828 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b829 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b830 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b831 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b832 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b833 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b834 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b835 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b836 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b837 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b838 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b839 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b840 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b841 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b842 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b843 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b844 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b845 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b846 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b847 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b848 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b849 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b850 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b851 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b852 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b853 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b854 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b855 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b856 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b857 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b858 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b859 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b860 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b861 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b862 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b863 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b864 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b865 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b866 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b867 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b868 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b869 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b870 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b871 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b872 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b873 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b874 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b875 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b876 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b877 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b878 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b879 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b880 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b881 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b882 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b883 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b884 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b885 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b886 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b887 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b888 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b889 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b890 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b891 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b892 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b893 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b894 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b895 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b896 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b897 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b898 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b899 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b900 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b901 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b902 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b903 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b904 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b905 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b906 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b907 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=   2628.648*m.b154 + 3252.62*m.b155 + 3611.072*m.b156 + 4912.12*m.b157 + 5230.744*m.b158
                        + 7222.144*m.b159 + 9678.204*m.b160 + 12041.332*m.b161 + 15864.82*m.b162 + 18466.916*m.b163
                        + 21825.744*m.b164 + 24693.36*m.b165 + 32034.988*m.b166 + 1493.118*m.b167 + 1847.545*m.b168
                        + 2051.152*m.b169 + 2790.17*m.b170 + 2971.154*m.b171 + 4102.304*m.b172 + 5497.389*m.b173
                        + 6839.687*m.b174 + 9011.495*m.b175 + 10489.531*m.b176 + 12397.404*m.b177 + 14026.26*m.b178
                        + 18196.433*m.b179 + 2370.852*m.b180 + 2933.63*m.b181 + 3256.928*m.b182 + 4430.38*m.b183
                        + 4717.756*m.b184 + 6513.856*m.b185 + 8729.046*m.b186 + 10860.418*m.b187 + 14308.93*m.b188
                        + 16655.834*m.b189 + 19685.256*m.b190 + 22271.64*m.b191 + 28893.262*m.b192 + 3226.806*m.b193
                        + 3992.765*m.b194 + 4432.784*m.b195 + 6029.89*m.b196 + 6421.018*m.b197 + 8865.568*m.b198
                        + 11880.513*m.b199 + 14781.379*m.b200 + 19474.915*m.b201 + 22669.127*m.b202 + 26792.268*m.b203
                        + 30312.42*m.b204 + 39324.661*m.b205 + 6191.856*m.b206 + 7661.64*m.b207 + 8505.984*m.b208
                        + 11570.64*m.b209 + 12321.168*m.b210 + 17011.968*m.b211 + 22797.288*m.b212 + 28363.704*m.b213
                        + 37370.04*m.b214 + 43499.352*m.b215 + 51411.168*m.b216 + 58165.92*m.b217 + 75459.336*m.b218
                        + 3906.936*m.b219 + 4834.34*m.b220 + 5367.104*m.b221 + 7300.84*m.b222 + 7774.408*m.b223
                        + 10734.208*m.b224 + 14384.628*m.b225 + 17896.924*m.b226 + 23579.74*m.b227 + 27447.212*m.b228
                        + 32439.408*m.b229 + 36701.52*m.b230 + 47613.316*m.b231 + 5723.982*m.b232 + 7082.705*m.b233
                        + 7863.248*m.b234 + 10696.33*m.b235 + 11390.146*m.b236 + 15726.496*m.b237 + 21074.661*m.b238
                        + 26220.463*m.b239 + 34546.255*m.b240 + 40212.419*m.b241 + 47526.396*m.b242 + 53770.74*m.b243
                        + 69757.417*m.b244 + 6659.334*m.b245 + 8240.085*m.b246 + 9148.176*m.b247 + 12444.21*m.b248
                        + 13251.402*m.b249 + 18296.352*m.b250 + 24518.457*m.b251 + 30505.131*m.b252 + 40191.435*m.b253
                        + 46783.503*m.b254 + 55292.652*m.b255 + 62557.38*m.b256 + 81156.429*m.b257 + 1532.322*m.b258
                        + 1896.055*m.b259 + 2105.008*m.b260 + 2863.43*m.b261 + 3049.166*m.b262 + 4210.016*m.b263
                        + 5641.731*m.b264 + 7019.273*m.b265 + 9248.105*m.b266 + 10764.949*m.b267 + 12722.916*m.b268
                        + 14394.54*m.b269 + 18674.207*m.b270 + 2689.038*m.b271 + 3327.345*m.b272 + 3694.032*m.b273
                        + 5024.97*m.b274 + 5350.914*m.b275 + 7388.064*m.b276 + 9900.549*m.b277 + 12317.967*m.b278
                        + 16229.295*m.b279 + 18891.171*m.b280 + 22327.164*m.b281 + 25260.66*m.b282 + 32770.953*m.b283
                        + 3984.948*m.b284 + 4930.87*m.b285 + 5474.272*m.b286 + 7446.62*m.b287 + 7929.644*m.b288
                        + 10948.544*m.b289 + 14671.854*m.b290 + 18254.282*m.b291 + 24050.57*m.b292 + 27995.266*m.b293
                        + 33087.144*m.b294 + 37434.36*m.b295 + 48564.038*m.b296 + 2864.268*m.b297 + 3544.17*m.b298
                        + 3934.752*m.b299 + 5352.42*m.b300 + 5699.604*m.b301 + 7869.504*m.b302 + 10545.714*m.b303
                        + 13120.662*m.b304 + 17286.87*m.b305 + 20122.206*m.b306 + 23782.104*m.b307 + 26906.76*m.b308
                        + 34906.458*m.b309 + 2220.966*m.b310 + 2748.165*m.b311 + 3051.024*m.b312 + 4150.29*m.b313
                        + 4419.498*m.b314 + 6102.048*m.b315 + 8177.193*m.b316 + 10173.819*m.b317 + 13404.315*m.b318
                        + 15602.847*m.b319 + 18440.748*m.b320 + 20863.62*m.b321 + 27066.621*m.b322 + 2909.808*m.b323
                        + 3600.52*m.b324 + 3997.312*m.b325 + 5437.52*m.b326 + 5790.224*m.b327 + 7994.624*m.b328
                        + 10713.384*m.b329 + 13329.272*m.b330 + 17561.72*m.b331 + 20442.136*m.b332 + 24160.224*m.b333
                        + 27334.56*m.b334 + 35461.448*m.b335 + 986.436*m.b336 + 1220.59*m.b337 + 1355.104*m.b338
                        + 1843.34*m.b339 + 1962.908*m.b340 + 2710.208*m.b341 + 3631.878*m.b342 + 4518.674*m.b343
                        + 5953.49*m.b344 + 6929.962*m.b345 + 8190.408*m.b346 + 9266.52*m.b347 + 12021.566*m.b348
                        + 3221.262*m.b349 + 3985.905*m.b350 + 4425.168*m.b351 + 6019.53*m.b352 + 6409.986*m.b353
                        + 8850.336*m.b354 + 11860.101*m.b355 + 14755.983*m.b356 + 19441.455*m.b357 + 22630.179*m.b358
                        + 26746.236*m.b359 + 30260.34*m.b360 + 39257.097*m.b361 + 1649.34*m.b362 + 2040.85*m.b363
                        + 2265.76*m.b364 + 3082.1*m.b365 + 3282.02*m.b366 + 4531.52*m.b367 + 6072.57*m.b368
                        + 7555.31*m.b369 + 9954.35*m.b370 + 11587.03*m.b371 + 13694.52*m.b372 + 15493.8*m.b373
                        + 20100.29*m.b374 + 1049.004*m.b375 + 1298.01*m.b376 + 1441.056*m.b377 + 1960.26*m.b378
                        + 2087.412*m.b379 + 2882.112*m.b380 + 3862.242*m.b381 + 4805.286*m.b382 + 6331.11*m.b383
                        + 7369.518*m.b384 + 8709.912*m.b385 + 9854.28*m.b386 + 12784.074*m.b387 + 4035.834*m.b388
                        + 4993.835*m.b389 + 5544.176*m.b390 + 7541.71*m.b391 + 8030.902*m.b392 + 11088.352*m.b393
                        + 14859.207*m.b394 + 18487.381*m.b395 + 24357.685*m.b396 + 28352.753*m.b397 + 33509.652*m.b398
                        + 37912.38*m.b399 + 49184.179*m.b400 + 2224.926*m.b401 + 2753.065*m.b402 + 3056.464*m.b403
                        + 4157.69*m.b404 + 4427.378*m.b405 + 6112.928*m.b406 + 8191.773*m.b407 + 10191.959*m.b408
                        + 13428.215*m.b409 + 15630.667*m.b410 + 18473.628*m.b411 + 20900.82*m.b412 + 27114.881*m.b413
                        + 739.332*m.b414 + 914.83*m.b415 + 1015.648*m.b416 + 1381.58*m.b417 + 1471.196*m.b418
                        + 2031.296*m.b419 + 2722.086*m.b420 + 3386.738*m.b421 + 4462.13*m.b422 + 5193.994*m.b423
                        + 6138.696*m.b424 + 6945.24*m.b425 + 9010.142*m.b426 + 1290.762*m.b427 + 1597.155*m.b428
                        + 1773.168*m.b429 + 2412.03*m.b430 + 2568.486*m.b431 + 3546.336*m.b432 + 4752.351*m.b433
                        + 5912.733*m.b434 + 7790.205*m.b435 + 9067.929*m.b436 + 10717.236*m.b437 + 12125.34*m.b438
                        + 15730.347*m.b439 + 3619.836*m.b440 + 4479.09*m.b441 + 4972.704*m.b442 + 6764.34*m.b443
                        + 7203.108*m.b444 + 9945.408*m.b445 + 13327.578*m.b446 + 16581.774*m.b447 + 21846.99*m.b448
                        + 25430.262*m.b449 + 30055.608*m.b450 + 34004.52*m.b451 + 44114.466*m.b452 + 1600.236*m.b453
                        + 1980.09*m.b454 + 2198.304*m.b455 + 2990.34*m.b456 + 3184.308*m.b457 + 4396.608*m.b458
                        + 5891.778*m.b459 + 7330.374*m.b460 + 9657.99*m.b461 + 11242.062*m.b462 + 13286.808*m.b463
                        + 15032.52*m.b464 + 19501.866*m.b465 + 1629.342*m.b466 + 2016.105*m.b467 + 2238.288*m.b468
                        + 3044.73*m.b469 + 3242.226*m.b470 + 4476.576*m.b471 + 5998.941*m.b472 + 7463.703*m.b473
                        + 9833.655*m.b474 + 11446.539*m.b475 + 13528.476*m.b476 + 15305.94*m.b477 + 19856.577*m.b478
                        + 2693.196*m.b479 + 3332.49*m.b480 + 3699.744*m.b481 + 5032.74*m.b482 + 5359.188*m.b483
                        + 7399.488*m.b484 + 9915.858*m.b485 + 12337.014*m.b486 + 16254.39*m.b487 + 18920.382*m.b488
                        + 22361.688*m.b489 + 25299.72*m.b490 + 32821.626*m.b491 + 7418.664*m.b492 + 9179.66*m.b493
                        + 10191.296*m.b494 + 13863.16*m.b495 + 14762.392*m.b496 + 20382.592*m.b497 + 27314.172*m.b498
                        + 33983.476*m.b499 + 44774.26*m.b500 + 52117.988*m.b501 + 61597.392*m.b502 + 69690.48*m.b503
                        + 90410.284*m.b504 + 4645.08*m.b505 + 5747.7*m.b506 + 6381.12*m.b507 + 8680.2*m.b508
                        + 9243.24*m.b509 + 12762.24*m.b510 + 17102.34*m.b511 + 21278.22*m.b512 + 28034.7*m.b513
                        + 32632.86*m.b514 + 38568.24*m.b515 + 43635.6*m.b516 + 56608.98*m.b517 + 1662.408*m.b518
                        + 2057.02*m.b519 + 2283.712*m.b520 + 3106.52*m.b521 + 3308.024*m.b522 + 4567.424*m.b523
                        + 6120.684*m.b524 + 7615.172*m.b525 + 10033.22*m.b526 + 11678.836*m.b527 + 13803.024*m.b528
                        + 15616.56*m.b529 + 20259.548*m.b530 + 1972.872*m.b531 + 2441.18*m.b532 + 2710.208*m.b533
                        + 3686.68*m.b534 + 3925.816*m.b535 + 5420.416*m.b536 + 7263.756*m.b537 + 9037.348*m.b538
                        + 11906.98*m.b539 + 13859.924*m.b540 + 16380.816*m.b541 + 18533.04*m.b542 + 24043.132*m.b543
                        + 4911.39*m.b544 + 6077.225*m.b545 + 6746.96*m.b546 + 9177.85*m.b547 + 9773.17*m.b548
                        + 13493.92*m.b549 + 18082.845*m.b550 + 22498.135*m.b551 + 29641.975*m.b552 + 34503.755*m.b553
                        + 40779.42*m.b554 + 46137.3*m.b555 + 59854.465*m.b556 + 2155.23*m.b557 + 2666.825*m.b558
                        + 2960.72*m.b559 + 4027.45*m.b560 + 4288.69*m.b561 + 5921.44*m.b562 + 7935.165*m.b563
                        + 9872.695*m.b564 + 13007.575*m.b565 + 15141.035*m.b566 + 17894.94*m.b567 + 20246.1*m.b568
                        + 26265.505*m.b569 + 4159.782*m.b570 + 5147.205*m.b571 + 5714.448*m.b572 + 7773.33*m.b573
                        + 8277.546*m.b574 + 11428.896*m.b575 + 15315.561*m.b576 + 19055.163*m.b577 + 25105.755*m.b578
                        + 29223.519*m.b579 + 34538.796*m.b580 + 39076.74*m.b581 + 50694.717*m.b582 + 2921.886*m.b583
                        + 3615.465*m.b584 + 4013.904*m.b585 + 5460.09*m.b586 + 5814.258*m.b587 + 8027.808*m.b588
                        + 10757.853*m.b589 + 13384.599*m.b590 + 17634.615*m.b591 + 20526.987*m.b592 + 24260.508*m.b593
                        + 27448.02*m.b594 + 35608.641*m.b595 + 6751.206*m.b596 + 8353.765*m.b597 + 9274.384*m.b598
                        + 12615.89*m.b599 + 13434.218*m.b600 + 18548.768*m.b601 + 24856.713*m.b602 + 30925.979*m.b603
                        + 40745.915*m.b604 + 47428.927*m.b605 + 56055.468*m.b606 + 63420.42*m.b607 + 82276.061*m.b608
                        + 2055.24*m.b609 + 2543.1*m.b610 + 2823.36*m.b611 + 3840.6*m.b612 + 4089.72*m.b613
                        + 5646.72*m.b614 + 7567.02*m.b615 + 9414.66*m.b616 + 12404.1*m.b617 + 14438.58*m.b618
                        + 17064.72*m.b619 + 19306.8*m.b620 + 25046.94*m.b621 + 1486.584*m.b622 + 1839.46*m.b623
                        + 2042.176*m.b624 + 2777.96*m.b625 + 2958.152*m.b626 + 4084.352*m.b627 + 5473.332*m.b628
                        + 6809.756*m.b629 + 8972.06*m.b630 + 10443.628*m.b631 + 12343.152*m.b632 + 13964.88*m.b633
                        + 18116.804*m.b634 + 2624.094*m.b635 + 3246.985*m.b636 + 3604.816*m.b637 + 4903.61*m.b638
                        + 5221.682*m.b639 + 7209.632*m.b640 + 9661.437*m.b641 + 12020.471*m.b642 + 15837.335*m.b643
                        + 18434.923*m.b644 + 21787.932*m.b645 + 24650.58*m.b646 + 31979.489*m.b647 + 4176.81*m.b648
                        + 5168.275*m.b649 + 5737.84*m.b650 + 7805.15*m.b651 + 8311.43*m.b652 + 11475.68*m.b653
                        + 15378.255*m.b654 + 19133.165*m.b655 + 25208.525*m.b656 + 29343.145*m.b657 + 34680.18*m.b658
                        + 39236.7*m.b659 + 50902.235*m.b660 + 2920.302*m.b661 + 3613.505*m.b662 + 4011.728*m.b663
                        + 5457.13*m.b664 + 5811.106*m.b665 + 8023.456*m.b666 + 10752.021*m.b667 + 13377.343*m.b668
                        + 17625.055*m.b669 + 20515.859*m.b670 + 24247.356*m.b671 + 27433.14*m.b672 + 35589.337*m.b673
                        + 2253.24*m.b674 + 2788.1*m.b675 + 3095.36*m.b676 + 4210.6*m.b677 + 4483.72*m.b678
                        + 6190.72*m.b679 + 8296.02*m.b680 + 10321.66*m.b681 + 13599.1*m.b682 + 15829.58*m.b683
                        + 18708.72*m.b684 + 21166.8*m.b685 + 27459.94*m.b686 + 3569.742*m.b687 + 4417.105*m.b688
                        + 4903.888*m.b689 + 6670.73*m.b690 + 7103.426*m.b691 + 9807.776*m.b692 + 13143.141*m.b693
                        + 16352.303*m.b694 + 21544.655*m.b695 + 25078.339*m.b696 + 29639.676*m.b697 + 33533.94*m.b698
                        + 43503.977*m.b699 + 1965.546*m.b700 + 2432.115*m.b701 + 2700.144*m.b702 + 3672.99*m.b703
                        + 3911.238*m.b704 + 5400.288*m.b705 + 7236.783*m.b706 + 9003.789*m.b707 + 11862.765*m.b708
                        + 13808.457*m.b709 + 16319.988*m.b710 + 18464.22*m.b711 + 23953.851*m.b712 + 3479.256*m.b713
                        + 4305.14*m.b714 + 4779.584*m.b715 + 6501.64*m.b716 + 6923.368*m.b717 + 9559.168*m.b718
                        + 12809.988*m.b719 + 15937.804*m.b720 + 20998.54*m.b721 + 24442.652*m.b722 + 28888.368*m.b723
                        + 32683.92*m.b724 + 42401.236*m.b725 + 2951.19*m.b726 + 3651.725*m.b727 + 4054.16*m.b728
                        + 5514.85*m.b729 + 5872.57*m.b730 + 8108.32*m.b731 + 10865.745*m.b732 + 13518.835*m.b733
                        + 17811.475*m.b734 + 20732.855*m.b735 + 24503.82*m.b736 + 27723.3*m.b737 + 35965.765*m.b738
                        + 1122.66*m.b739 + 1389.15*m.b740 + 1542.24*m.b741 + 2097.9*m.b742 + 2233.98*m.b743
                        + 3084.48*m.b744 + 4133.43*m.b745 + 5142.69*m.b746 + 6775.65*m.b747 + 7886.97*m.b748
                        + 9321.48*m.b749 + 10546.2*m.b750 + 13681.71*m.b751 + 4257.99*m.b752 + 5268.725*m.b753
                        + 5849.36*m.b754 + 7956.85*m.b755 + 8472.97*m.b756 + 11698.72*m.b757 + 15677.145*m.b758
                        + 19505.035*m.b759 + 25698.475*m.b760 + 29913.455*m.b761 + 35354.22*m.b762 + 39999.3*m.b763
                        + 51891.565*m.b764 + 2456.784*m.b765 + 3039.96*m.b766 + 3374.976*m.b767 + 4590.96*m.b768
                        + 4888.752*m.b769 + 6749.952*m.b770 + 9045.432*m.b771 + 11254.056*m.b772 + 14827.56*m.b773
                        + 17259.528*m.b774 + 20398.752*m.b775 + 23078.88*m.b776 + 29940.504*m.b777 + 2375.406*m.b778
                        + 2939.265*m.b779 + 3263.184*m.b780 + 4438.89*m.b781 + 4726.818*m.b782 + 6526.368*m.b783
                        + 8745.813*m.b784 + 10881.279*m.b785 + 14336.415*m.b786 + 16687.827*m.b787 + 19723.068*m.b788
                        + 22314.42*m.b789 + 28948.761*m.b790 + 3592.116*m.b791 + 4444.79*m.b792 + 4934.624*m.b793
                        + 6712.54*m.b794 + 7147.948*m.b795 + 9869.248*m.b796 + 13225.518*m.b797 + 16454.794*m.b798
                        + 21679.69*m.b799 + 25235.522*m.b800 + 29825.448*m.b801 + 33744.12*m.b802 + 43776.646*m.b803
                        + 1186.614*m.b804 + 1468.285*m.b805 + 1630.096*m.b806 + 2217.41*m.b807 + 2361.242*m.b808
                        + 3260.192*m.b809 + 4368.897*m.b810 + 5435.651*m.b811 + 7161.635*m.b812 + 8336.263*m.b813
                        + 9852.492*m.b814 + 11146.98*m.b815 + 14461.109*m.b816 + 1554.3*m.b817 + 1923.25*m.b818
                        + 2135.2*m.b819 + 2904.5*m.b820 + 3092.9*m.b821 + 4270.4*m.b822 + 5722.65*m.b823
                        + 7119.95*m.b824 + 9380.75*m.b825 + 10919.35*m.b826 + 12905.4*m.b827 + 14601*m.b828
                        + 18942.05*m.b829 + 2859.912*m.b830 + 3538.78*m.b831 + 3928.768*m.b832 + 5344.28*m.b833
                        + 5690.936*m.b834 + 7857.536*m.b835 + 10529.676*m.b836 + 13100.708*m.b837 + 17260.58*m.b838
                        + 20091.604*m.b839 + 23745.936*m.b840 + 26865.84*m.b841 + 34853.372*m.b842 + 687.852*m.b843
                        + 851.13*m.b844 + 944.928*m.b845 + 1285.38*m.b846 + 1368.756*m.b847 + 1889.856*m.b848
                        + 2532.546*m.b849 + 3150.918*m.b850 + 4151.43*m.b851 + 4832.334*m.b852 + 5711.256*m.b853
                        + 6461.64*m.b854 + 8382.762*m.b855 + 3280.266*m.b856 + 4058.915*m.b857 + 4506.224*m.b858
                        + 6129.79*m.b859 + 6527.398*m.b860 + 9012.448*m.b861 + 12077.343*m.b862 + 15026.269*m.b863
                        + 19797.565*m.b864 + 23044.697*m.b865 + 27236.148*m.b866 + 30814.62*m.b867 + 39976.171*m.b868
                        + 1646.766*m.b869 + 2037.665*m.b870 + 2262.224*m.b871 + 3077.29*m.b872 + 3276.898*m.b873
                        + 4524.448*m.b874 + 6063.093*m.b875 + 7543.519*m.b876 + 9938.815*m.b877 + 11568.947*m.b878
                        + 13673.148*m.b879 + 15469.62*m.b880 + 20068.921*m.b881 + 4172.652*m.b882 + 5163.13*m.b883
                        + 5732.128*m.b884 + 7797.38*m.b885 + 8303.156*m.b886 + 11464.256*m.b887 + 15362.946*m.b888
                        + 19114.118*m.b889 + 25183.43*m.b890 + 29313.934*m.b891 + 34645.656*m.b892 + 39197.64*m.b893
                        + 50851.562*m.b894 + 19.8*m.b895 + 24.5*m.b896 + 27.2*m.b897 + 37*m.b898 + 39.4*m.b899
                        + 54.4*m.b900 + 72.9*m.b901 + 90.7*m.b902 + 119.5*m.b903 + 139.1*m.b904 + 164.4*m.b905
                        + 186*m.b906 + 241.3*m.b907, sense=minimize)

m.c2 = Constraint(expr=   m.x38 + m.x39 - m.x94 - m.x95 == -0.00049)

m.c3 = Constraint(expr=   m.x40 + m.x41 - m.x64 == -0.00104)

m.c4 = Constraint(expr= - m.x40 + m.x42 + m.x43 == -0.00102)

m.c5 = Constraint(expr= - m.x42 + m.x44 - m.x55 == -0.00081)

m.c6 = Constraint(expr= - m.x44 + m.x45 + m.x46 == -0.00063)

m.c7 = Constraint(expr= - m.x45 + m.x47 - m.x70 == -0.00079)

m.c8 = Constraint(expr= - m.x47 + m.x48 - m.x72 == -0.00026)

m.c9 = Constraint(expr=   m.x49 - m.x75 - m.x77 == -0.00058)

m.c10 = Constraint(expr=   m.x50 - m.x81 - m.x85 == -0.00054)

m.c11 = Constraint(expr=   m.x51 + m.x52 - m.x66 - m.x87 == -0.00111)

m.c12 = Constraint(expr= - m.x43 - m.x51 + m.x53 + m.x54 == -0.00175)

m.c13 = Constraint(expr=   m.x55 + m.x56 - m.x67 == -0.00091)

m.c14 = Constraint(expr= - m.x46 - m.x56 + m.x57 == -0.00116)

m.c15 = Constraint(expr= - m.x57 + m.x58 + m.x59 == -0.00054)

m.c16 = Constraint(expr=   m.x60 + m.x61 - m.x69 - m.x78 == -0.0011)

m.c17 = Constraint(expr= - m.x60 + m.x62 + m.x63 - m.x80 == -0.00121)

m.c18 = Constraint(expr= - m.x38 + m.x64 + m.x65 == -0.00127)

m.c19 = Constraint(expr= - m.x41 - m.x65 + m.x66 == -0.00202)

m.c20 = Constraint(expr= - m.x53 + m.x67 + m.x68 == -0.00188)

m.c21 = Constraint(expr= - m.x58 - m.x68 + m.x69 == -0.00093)

m.c22 = Constraint(expr= - m.x59 + m.x70 + m.x71 == -0.00096)

m.c23 = Constraint(expr= - m.x61 - m.x71 + m.x72 + m.x73 == -0.00097)

m.c24 = Constraint(expr= - m.x73 + m.x74 - m.x76 == -0.00086)

m.c25 = Constraint(expr= - m.x48 + m.x75 + m.x76 == -0.00067)

m.c26 = Constraint(expr= - m.x62 - m.x74 + m.x77 == -0.00077)

m.c27 = Constraint(expr= - m.x54 + m.x78 + m.x79 == -0.00169)

m.c28 = Constraint(expr= - m.x79 + m.x80 - m.x89 == -0.00142)

m.c29 = Constraint(expr= - m.x49 + m.x81 + m.x82 == -0.0003)

m.c30 = Constraint(expr= - m.x63 - m.x82 + m.x83 + m.x84 == -0.00062)

m.c31 = Constraint(expr= - m.x83 + m.x85 + m.x86 == -0.00054)

m.c32 = Constraint(expr= - m.x39 + m.x87 + m.x88 == -0.0009)

m.c33 = Constraint(expr= - m.x52 + m.x89 + m.x90 == -0.00103)

m.c34 = Constraint(expr= - m.x84 - m.x90 + m.x91 == -0.00077)

m.c35 = Constraint(expr= - m.x88 - m.x91 + m.x92 == -0.00074)

m.c36 = Constraint(expr= - m.x86 - m.x92 + m.x93 == -0.00116)

m.c37 = Constraint(expr= - m.x50 - m.x93 + m.x94 == -0.00047)

m.c38 = Constraint(expr=SignPower(m.x38,1.852) - 5.78858036381102*(1.27323954473516*m.x96)**2.435*(m.x1 - m.x17) == 0)

m.c39 = Constraint(expr=SignPower(m.x39,1.852) - 10.1908490796917*(1.27323954473516*m.x97)**2.435*(m.x1 - m.x31) == 0)

m.c40 = Constraint(expr=SignPower(m.x40,1.852) - 6.4180050868511*(1.27323954473516*m.x98)**2.435*(m.x2 - m.x3) == 0)

m.c41 = Constraint(expr=SignPower(m.x41,1.852) - 4.71554230287507*(1.27323954473516*m.x99)**2.435*(m.x2 - m.x18) == 0)

m.c42 = Constraint(expr=SignPower(m.x42,1.852) - 2.45744413244932*(1.27323954473516*m.x100)**2.435*(m.x3 - m.x4) == 0)

m.c43 = Constraint(expr=SignPower(m.x43,1.852) - 3.89464792772932*(1.27323954473516*m.x101)**2.435*(m.x3 - m.x11) == 0)

m.c44 = Constraint(expr=SignPower(m.x44,1.852) - 2.65831377460151*(1.27323954473516*m.x102)**2.435*(m.x4 - m.x5) == 0)

m.c45 = Constraint(expr=SignPower(m.x45,1.852) - 2.28493422858368*(1.27323954473516*m.x103)**2.435*(m.x5 - m.x6) == 0)

m.c46 = Constraint(expr=SignPower(m.x46,1.852) - 9.93011925441983*(1.27323954473516*m.x104)**2.435*(m.x5 - m.x13) == 0)

m.c47 = Constraint(expr=SignPower(m.x47,1.852) - 5.65858132022348*(1.27323954473516*m.x105)**2.435*(m.x6 - m.x7) == 0)

m.c48 = Constraint(expr=SignPower(m.x48,1.852) - 3.81840370217405*(1.27323954473516*m.x106)**2.435*(m.x7 - m.x24) == 0)

m.c49 = Constraint(expr=SignPower(m.x49,1.852) - 5.31240100303851*(1.27323954473516*m.x107)**2.435*(m.x8 - m.x28) == 0)

m.c50 = Constraint(expr=SignPower(m.x50,1.852) - 6.85113603547785*(1.27323954473516*m.x108)**2.435*(m.x9 - m.x36) == 0)

m.c51 = Constraint(expr=SignPower(m.x51,1.852) - 5.22925918004593*(1.27323954473516*m.x109)**2.435*(m.x10 - m.x11) == 0)

m.c52 = Constraint(expr=SignPower(m.x52,1.852) - 15.4253699136803*(1.27323954473516*m.x110)**2.435*(m.x10 - m.x32) == 0)

m.c53 = Constraint(expr=SignPower(m.x53,1.852) - 4.7236580558089*(1.27323954473516*m.x111)**2.435*(m.x11 - m.x19) == 0)

m.c54 = Constraint(expr=SignPower(m.x54,1.852) - 9.22559338654922*(1.27323954473516*m.x112)**2.435*(m.x11 - m.x26) == 0)

m.c55 = Constraint(expr=SignPower(m.x55,1.852) - 14.5053214250576*(1.27323954473516*m.x113)**2.435*(m.x12 - m.x4) == 0)

m.c56 = Constraint(expr=SignPower(m.x56,1.852) - 3.7702591821594*(1.27323954473516*m.x114)**2.435*(m.x12 - m.x13) == 0)

m.c57 = Constraint(expr=SignPower(m.x57,1.852) - 6.83894214736629*(1.27323954473516*m.x115)**2.435*(m.x13 - m.x14) == 0)

m.c58 = Constraint(expr=SignPower(m.x58,1.852) - 20.5809300776527*(1.27323954473516*m.x116)**2.435*(m.x14 - m.x20) == 0)

m.c59 = Constraint(expr=SignPower(m.x59,1.852) - 11.7884940803735*(1.27323954473516*m.x117)**2.435*(m.x14 - m.x21) == 0)

m.c60 = Constraint(expr=SignPower(m.x60,1.852) - 4.20354408215485*(1.27323954473516*m.x118)**2.435*(m.x15 - m.x16) == 0)

m.c61 = Constraint(expr=SignPower(m.x61,1.852) - 9.50868509155593*(1.27323954473516*m.x119)**2.435*(m.x15 - m.x22) == 0)

m.c62 = Constraint(expr=SignPower(m.x62,1.852) - 9.33882524121461*(1.27323954473516*m.x120)**2.435*(m.x16 - m.x25) == 0)

m.c63 = Constraint(expr=SignPower(m.x63,1.852) - 5.64984508968939*(1.27323954473516*m.x121)**2.435*(m.x16 - m.x29) == 0)

m.c64 = Constraint(expr=SignPower(m.x64,1.852) - 2.0510620505486*(1.27323954473516*m.x122)**2.435*(m.x17 - m.x2) == 0)

m.c65 = Constraint(expr=SignPower(m.x65,1.852) - 3.27575417348487*(1.27323954473516*m.x123)**2.435*(m.x17 - m.x18) == 0)

m.c66 = Constraint(expr=SignPower(m.x66,1.852) - 9.15307204739817*(1.27323954473516*m.x124)**2.435*(m.x18 - m.x10) == 0)

m.c67 = Constraint(expr=SignPower(m.x67,1.852) - 7.71268495684013*(1.27323954473516*m.x125)**2.435*(m.x19 - m.x12) == 0)

m.c68 = Constraint(expr=SignPower(m.x68,1.852) - 3.09813315500726*(1.27323954473516*m.x126)**2.435*(m.x19 - m.x20) == 0)

m.c69 = Constraint(expr=SignPower(m.x69,1.852) - 7.06010040514056*(1.27323954473516*m.x127)**2.435*(m.x20 - m.x15) == 0)

m.c70 = Constraint(expr=SignPower(m.x70,1.852) - 3.65791769765125*(1.27323954473516*m.x128)**2.435*(m.x21 - m.x6) == 0)

m.c71 = Constraint(expr=SignPower(m.x71,1.852) - 5.20764334959375*(1.27323954473516*m.x129)**2.435*(m.x21 - m.x22) == 0)

m.c72 = Constraint(expr=SignPower(m.x72,1.852) - 2.25384030589069*(1.27323954473516*m.x130)**2.435*(m.x22 - m.x7) == 0)

m.c73 = Constraint(expr=SignPower(m.x73,1.852) - 7.40358313198025*(1.27323954473516*m.x131)**2.435*(m.x22 - m.x23) == 0)

m.c74 = Constraint(expr=SignPower(m.x74,1.852) - 10.2356410375539*(1.27323954473516*m.x132)**2.435*(m.x23 - m.x25) == 0)

m.c75 = Constraint(expr=SignPower(m.x75,1.852) - 5.79862619104769*(1.27323954473516*m.x133)**2.435*(m.x24 - m.x8) == 0)

m.c76 = Constraint(expr=SignPower(m.x76,1.852) - 3.64300511542807*(1.27323954473516*m.x134)**2.435*(m.x24 - m.x23) == 0)

m.c77 = Constraint(expr=SignPower(m.x77,1.852) - 5.21046802562581*(1.27323954473516*m.x135)**2.435*(m.x25 - m.x8) == 0)

m.c78 = Constraint(expr=SignPower(m.x78,1.852) - 6.75300464938093*(1.27323954473516*m.x136)**2.435*(m.x26 - m.x15) == 0)

m.c79 = Constraint(expr=SignPower(m.x79,1.852) - 4.26253219313079*(1.27323954473516*m.x137)**2.435*(m.x26 - m.x27) == 0)

m.c80 = Constraint(expr=SignPower(m.x80,1.852) - 7.74143174271734*(1.27323954473516*m.x138)**2.435*(m.x27 - m.x16) == 0)

m.c81 = Constraint(expr=SignPower(m.x81,1.852) - 4.37338907978346*(1.27323954473516*m.x139)**2.435*(m.x28 - m.x9) == 0)

m.c82 = Constraint(expr=SignPower(m.x82,1.852) - 5.15593377456927*(1.27323954473516*m.x140)**2.435*(m.x28 - m.x29) == 0)

m.c83 = Constraint(expr=SignPower(m.x83,1.852) - 13.5536495432019*(1.27323954473516*m.x141)**2.435*(m.x29 - m.x30) == 0)

m.c84 = Constraint(expr=SignPower(m.x84,1.852) - 3.57355000743804*(1.27323954473516*m.x142)**2.435*(m.x29 - m.x33) == 0)

m.c85 = Constraint(expr=SignPower(m.x85,1.852) - 6.19351973806859*(1.27323954473516*m.x143)**2.435*(m.x30 - m.x9) == 0)

m.c86 = Constraint(expr=SignPower(m.x86,1.852) - 6.40570083437151*(1.27323954473516*m.x144)**2.435*(m.x30 - m.x35) == 0)

m.c87 = Constraint(expr=SignPower(m.x87,1.852) - 4.23598241152877*(1.27323954473516*m.x145)**2.435*(m.x31 - m.x10) == 0)

m.c88 = Constraint(expr=SignPower(m.x88,1.852) - 12.8231591706916*(1.27323954473516*m.x146)**2.435*(m.x31 - m.x34) == 0)

m.c89 = Constraint(expr=SignPower(m.x89,1.852) - 9.78970610317898*(1.27323954473516*m.x147)**2.435*(m.x32 - m.x27) == 0)

m.c90 = Constraint(expr=SignPower(m.x90,1.852) - 5.32049244737988*(1.27323954473516*m.x148)**2.435*(m.x32 - m.x33) == 0)

m.c91 = Constraint(expr=SignPower(m.x91,1.852) - 22.121241482428*(1.27323954473516*m.x149)**2.435*(m.x33 - m.x34) == 0)

m.c92 = Constraint(expr=SignPower(m.x92,1.852) - 4.63869094645712*(1.27323954473516*m.x150)**2.435*(m.x34 - m.x35) == 0)

m.c93 = Constraint(expr=SignPower(m.x93,1.852) - 9.24001357580318*(1.27323954473516*m.x151)**2.435*(m.x35 - m.x36) == 0)

m.c94 = Constraint(expr=SignPower(m.x94,1.852) - 3.64663532836457*(1.27323954473516*m.x152)**2.435*(m.x36 - m.x1) == 0)

m.c95 = Constraint(expr=SignPower(m.x95,1.852) - 768.49192909955*(1.27323954473516*m.x153)**2.435*(m.x37 - m.x1) == 0)

m.c96 = Constraint(expr=   m.x38 - m.x96 <= 0)

m.c97 = Constraint(expr=   m.x39 - m.x97 <= 0)

m.c98 = Constraint(expr=   m.x40 - m.x98 <= 0)

m.c99 = Constraint(expr=   m.x41 - m.x99 <= 0)

m.c100 = Constraint(expr=   m.x42 - m.x100 <= 0)

m.c101 = Constraint(expr=   m.x43 - m.x101 <= 0)

m.c102 = Constraint(expr=   m.x44 - m.x102 <= 0)

m.c103 = Constraint(expr=   m.x45 - m.x103 <= 0)

m.c104 = Constraint(expr=   m.x46 - m.x104 <= 0)

m.c105 = Constraint(expr=   m.x47 - m.x105 <= 0)

m.c106 = Constraint(expr=   m.x48 - m.x106 <= 0)

m.c107 = Constraint(expr=   m.x49 - m.x107 <= 0)

m.c108 = Constraint(expr=   m.x50 - m.x108 <= 0)

m.c109 = Constraint(expr=   m.x51 - m.x109 <= 0)

m.c110 = Constraint(expr=   m.x52 - m.x110 <= 0)

m.c111 = Constraint(expr=   m.x53 - m.x111 <= 0)

m.c112 = Constraint(expr=   m.x54 - m.x112 <= 0)

m.c113 = Constraint(expr=   m.x55 - m.x113 <= 0)

m.c114 = Constraint(expr=   m.x56 - m.x114 <= 0)

m.c115 = Constraint(expr=   m.x57 - m.x115 <= 0)

m.c116 = Constraint(expr=   m.x58 - m.x116 <= 0)

m.c117 = Constraint(expr=   m.x59 - m.x117 <= 0)

m.c118 = Constraint(expr=   m.x60 - m.x118 <= 0)

m.c119 = Constraint(expr=   m.x61 - m.x119 <= 0)

m.c120 = Constraint(expr=   m.x62 - m.x120 <= 0)

m.c121 = Constraint(expr=   m.x63 - m.x121 <= 0)

m.c122 = Constraint(expr=   m.x64 - m.x122 <= 0)

m.c123 = Constraint(expr=   m.x65 - m.x123 <= 0)

m.c124 = Constraint(expr=   m.x66 - m.x124 <= 0)

m.c125 = Constraint(expr=   m.x67 - m.x125 <= 0)

m.c126 = Constraint(expr=   m.x68 - m.x126 <= 0)

m.c127 = Constraint(expr=   m.x69 - m.x127 <= 0)

m.c128 = Constraint(expr=   m.x70 - m.x128 <= 0)

m.c129 = Constraint(expr=   m.x71 - m.x129 <= 0)

m.c130 = Constraint(expr=   m.x72 - m.x130 <= 0)

m.c131 = Constraint(expr=   m.x73 - m.x131 <= 0)

m.c132 = Constraint(expr=   m.x74 - m.x132 <= 0)

m.c133 = Constraint(expr=   m.x75 - m.x133 <= 0)

m.c134 = Constraint(expr=   m.x76 - m.x134 <= 0)

m.c135 = Constraint(expr=   m.x77 - m.x135 <= 0)

m.c136 = Constraint(expr=   m.x78 - m.x136 <= 0)

m.c137 = Constraint(expr=   m.x79 - m.x137 <= 0)

m.c138 = Constraint(expr=   m.x80 - m.x138 <= 0)

m.c139 = Constraint(expr=   m.x81 - m.x139 <= 0)

m.c140 = Constraint(expr=   m.x82 - m.x140 <= 0)

m.c141 = Constraint(expr=   m.x83 - m.x141 <= 0)

m.c142 = Constraint(expr=   m.x84 - m.x142 <= 0)

m.c143 = Constraint(expr=   m.x85 - m.x143 <= 0)

m.c144 = Constraint(expr=   m.x86 - m.x144 <= 0)

m.c145 = Constraint(expr=   m.x87 - m.x145 <= 0)

m.c146 = Constraint(expr=   m.x88 - m.x146 <= 0)

m.c147 = Constraint(expr=   m.x89 - m.x147 <= 0)

m.c148 = Constraint(expr=   m.x90 - m.x148 <= 0)

m.c149 = Constraint(expr=   m.x91 - m.x149 <= 0)

m.c150 = Constraint(expr=   m.x92 - m.x150 <= 0)

m.c151 = Constraint(expr=   m.x93 - m.x151 <= 0)

m.c152 = Constraint(expr=   m.x94 - m.x152 <= 0)

m.c153 = Constraint(expr=   m.x95 - m.x153 <= 0)

m.c154 = Constraint(expr=   m.x38 + m.x96 >= 0)

m.c155 = Constraint(expr=   m.x39 + m.x97 >= 0)

m.c156 = Constraint(expr=   m.x40 + m.x98 >= 0)

m.c157 = Constraint(expr=   m.x41 + m.x99 >= 0)

m.c158 = Constraint(expr=   m.x42 + m.x100 >= 0)

m.c159 = Constraint(expr=   m.x43 + m.x101 >= 0)

m.c160 = Constraint(expr=   m.x44 + m.x102 >= 0)

m.c161 = Constraint(expr=   m.x45 + m.x103 >= 0)

m.c162 = Constraint(expr=   m.x46 + m.x104 >= 0)

m.c163 = Constraint(expr=   m.x47 + m.x105 >= 0)

m.c164 = Constraint(expr=   m.x48 + m.x106 >= 0)

m.c165 = Constraint(expr=   m.x49 + m.x107 >= 0)

m.c166 = Constraint(expr=   m.x50 + m.x108 >= 0)

m.c167 = Constraint(expr=   m.x51 + m.x109 >= 0)

m.c168 = Constraint(expr=   m.x52 + m.x110 >= 0)

m.c169 = Constraint(expr=   m.x53 + m.x111 >= 0)

m.c170 = Constraint(expr=   m.x54 + m.x112 >= 0)

m.c171 = Constraint(expr=   m.x55 + m.x113 >= 0)

m.c172 = Constraint(expr=   m.x56 + m.x114 >= 0)

m.c173 = Constraint(expr=   m.x57 + m.x115 >= 0)

m.c174 = Constraint(expr=   m.x58 + m.x116 >= 0)

m.c175 = Constraint(expr=   m.x59 + m.x117 >= 0)

m.c176 = Constraint(expr=   m.x60 + m.x118 >= 0)

m.c177 = Constraint(expr=   m.x61 + m.x119 >= 0)

m.c178 = Constraint(expr=   m.x62 + m.x120 >= 0)

m.c179 = Constraint(expr=   m.x63 + m.x121 >= 0)

m.c180 = Constraint(expr=   m.x64 + m.x122 >= 0)

m.c181 = Constraint(expr=   m.x65 + m.x123 >= 0)

m.c182 = Constraint(expr=   m.x66 + m.x124 >= 0)

m.c183 = Constraint(expr=   m.x67 + m.x125 >= 0)

m.c184 = Constraint(expr=   m.x68 + m.x126 >= 0)

m.c185 = Constraint(expr=   m.x69 + m.x127 >= 0)

m.c186 = Constraint(expr=   m.x70 + m.x128 >= 0)

m.c187 = Constraint(expr=   m.x71 + m.x129 >= 0)

m.c188 = Constraint(expr=   m.x72 + m.x130 >= 0)

m.c189 = Constraint(expr=   m.x73 + m.x131 >= 0)

m.c190 = Constraint(expr=   m.x74 + m.x132 >= 0)

m.c191 = Constraint(expr=   m.x75 + m.x133 >= 0)

m.c192 = Constraint(expr=   m.x76 + m.x134 >= 0)

m.c193 = Constraint(expr=   m.x77 + m.x135 >= 0)

m.c194 = Constraint(expr=   m.x78 + m.x136 >= 0)

m.c195 = Constraint(expr=   m.x79 + m.x137 >= 0)

m.c196 = Constraint(expr=   m.x80 + m.x138 >= 0)

m.c197 = Constraint(expr=   m.x81 + m.x139 >= 0)

m.c198 = Constraint(expr=   m.x82 + m.x140 >= 0)

m.c199 = Constraint(expr=   m.x83 + m.x141 >= 0)

m.c200 = Constraint(expr=   m.x84 + m.x142 >= 0)

m.c201 = Constraint(expr=   m.x85 + m.x143 >= 0)

m.c202 = Constraint(expr=   m.x86 + m.x144 >= 0)

m.c203 = Constraint(expr=   m.x87 + m.x145 >= 0)

m.c204 = Constraint(expr=   m.x88 + m.x146 >= 0)

m.c205 = Constraint(expr=   m.x89 + m.x147 >= 0)

m.c206 = Constraint(expr=   m.x90 + m.x148 >= 0)

m.c207 = Constraint(expr=   m.x91 + m.x149 >= 0)

m.c208 = Constraint(expr=   m.x92 + m.x150 >= 0)

m.c209 = Constraint(expr=   m.x93 + m.x151 >= 0)

m.c210 = Constraint(expr=   m.x94 + m.x152 >= 0)

m.c211 = Constraint(expr=   m.x95 + m.x153 >= 0)

m.c212 = Constraint(expr=   m.x96 - 0.00282743338823081*m.b154 - 0.00502654824574367*m.b155 - 0.00785398163397448*m.b156
                          - 0.0122718463030851*m.b157 - 0.0176714586764426*m.b158 - 0.0314159265358979*m.b159
                          - 0.0490873852123405*m.b160 - 0.0706858347057703*m.b161 - 0.0962112750161874*m.b162
                          - 0.125663706143592*m.b163 - 0.159043128087983*m.b164 - 0.196349540849362*m.b165
                          - 0.282743338823081*m.b166 == 0)

m.c213 = Constraint(expr=   m.x97 - 0.00282743338823081*m.b167 - 0.00502654824574367*m.b168 - 0.00785398163397448*m.b169
                          - 0.0122718463030851*m.b170 - 0.0176714586764426*m.b171 - 0.0314159265358979*m.b172
                          - 0.0490873852123405*m.b173 - 0.0706858347057703*m.b174 - 0.0962112750161874*m.b175
                          - 0.125663706143592*m.b176 - 0.159043128087983*m.b177 - 0.196349540849362*m.b178
                          - 0.282743338823081*m.b179 == 0)

m.c214 = Constraint(expr=   m.x98 - 0.00282743338823081*m.b180 - 0.00502654824574367*m.b181 - 0.00785398163397448*m.b182
                          - 0.0122718463030851*m.b183 - 0.0176714586764426*m.b184 - 0.0314159265358979*m.b185
                          - 0.0490873852123405*m.b186 - 0.0706858347057703*m.b187 - 0.0962112750161874*m.b188
                          - 0.125663706143592*m.b189 - 0.159043128087983*m.b190 - 0.196349540849362*m.b191
                          - 0.282743338823081*m.b192 == 0)

m.c215 = Constraint(expr=   m.x99 - 0.00282743338823081*m.b193 - 0.00502654824574367*m.b194 - 0.00785398163397448*m.b195
                          - 0.0122718463030851*m.b196 - 0.0176714586764426*m.b197 - 0.0314159265358979*m.b198
                          - 0.0490873852123405*m.b199 - 0.0706858347057703*m.b200 - 0.0962112750161874*m.b201
                          - 0.125663706143592*m.b202 - 0.159043128087983*m.b203 - 0.196349540849362*m.b204
                          - 0.282743338823081*m.b205 == 0)

m.c216 = Constraint(expr=   m.x100 - 0.00282743338823081*m.b206 - 0.00502654824574367*m.b207
                          - 0.00785398163397448*m.b208 - 0.0122718463030851*m.b209 - 0.0176714586764426*m.b210
                          - 0.0314159265358979*m.b211 - 0.0490873852123405*m.b212 - 0.0706858347057703*m.b213
                          - 0.0962112750161874*m.b214 - 0.125663706143592*m.b215 - 0.159043128087983*m.b216
                          - 0.196349540849362*m.b217 - 0.282743338823081*m.b218 == 0)

m.c217 = Constraint(expr=   m.x101 - 0.00282743338823081*m.b219 - 0.00502654824574367*m.b220
                          - 0.00785398163397448*m.b221 - 0.0122718463030851*m.b222 - 0.0176714586764426*m.b223
                          - 0.0314159265358979*m.b224 - 0.0490873852123405*m.b225 - 0.0706858347057703*m.b226
                          - 0.0962112750161874*m.b227 - 0.125663706143592*m.b228 - 0.159043128087983*m.b229
                          - 0.196349540849362*m.b230 - 0.282743338823081*m.b231 == 0)

m.c218 = Constraint(expr=   m.x102 - 0.00282743338823081*m.b232 - 0.00502654824574367*m.b233
                          - 0.00785398163397448*m.b234 - 0.0122718463030851*m.b235 - 0.0176714586764426*m.b236
                          - 0.0314159265358979*m.b237 - 0.0490873852123405*m.b238 - 0.0706858347057703*m.b239
                          - 0.0962112750161874*m.b240 - 0.125663706143592*m.b241 - 0.159043128087983*m.b242
                          - 0.196349540849362*m.b243 - 0.282743338823081*m.b244 == 0)

m.c219 = Constraint(expr=   m.x103 - 0.00282743338823081*m.b245 - 0.00502654824574367*m.b246
                          - 0.00785398163397448*m.b247 - 0.0122718463030851*m.b248 - 0.0176714586764426*m.b249
                          - 0.0314159265358979*m.b250 - 0.0490873852123405*m.b251 - 0.0706858347057703*m.b252
                          - 0.0962112750161874*m.b253 - 0.125663706143592*m.b254 - 0.159043128087983*m.b255
                          - 0.196349540849362*m.b256 - 0.282743338823081*m.b257 == 0)

m.c220 = Constraint(expr=   m.x104 - 0.00282743338823081*m.b258 - 0.00502654824574367*m.b259
                          - 0.00785398163397448*m.b260 - 0.0122718463030851*m.b261 - 0.0176714586764426*m.b262
                          - 0.0314159265358979*m.b263 - 0.0490873852123405*m.b264 - 0.0706858347057703*m.b265
                          - 0.0962112750161874*m.b266 - 0.125663706143592*m.b267 - 0.159043128087983*m.b268
                          - 0.196349540849362*m.b269 - 0.282743338823081*m.b270 == 0)

m.c221 = Constraint(expr=   m.x105 - 0.00282743338823081*m.b271 - 0.00502654824574367*m.b272
                          - 0.00785398163397448*m.b273 - 0.0122718463030851*m.b274 - 0.0176714586764426*m.b275
                          - 0.0314159265358979*m.b276 - 0.0490873852123405*m.b277 - 0.0706858347057703*m.b278
                          - 0.0962112750161874*m.b279 - 0.125663706143592*m.b280 - 0.159043128087983*m.b281
                          - 0.196349540849362*m.b282 - 0.282743338823081*m.b283 == 0)

m.c222 = Constraint(expr=   m.x106 - 0.00282743338823081*m.b284 - 0.00502654824574367*m.b285
                          - 0.00785398163397448*m.b286 - 0.0122718463030851*m.b287 - 0.0176714586764426*m.b288
                          - 0.0314159265358979*m.b289 - 0.0490873852123405*m.b290 - 0.0706858347057703*m.b291
                          - 0.0962112750161874*m.b292 - 0.125663706143592*m.b293 - 0.159043128087983*m.b294
                          - 0.196349540849362*m.b295 - 0.282743338823081*m.b296 == 0)

m.c223 = Constraint(expr=   m.x107 - 0.00282743338823081*m.b297 - 0.00502654824574367*m.b298
                          - 0.00785398163397448*m.b299 - 0.0122718463030851*m.b300 - 0.0176714586764426*m.b301
                          - 0.0314159265358979*m.b302 - 0.0490873852123405*m.b303 - 0.0706858347057703*m.b304
                          - 0.0962112750161874*m.b305 - 0.125663706143592*m.b306 - 0.159043128087983*m.b307
                          - 0.196349540849362*m.b308 - 0.282743338823081*m.b309 == 0)

m.c224 = Constraint(expr=   m.x108 - 0.00282743338823081*m.b310 - 0.00502654824574367*m.b311
                          - 0.00785398163397448*m.b312 - 0.0122718463030851*m.b313 - 0.0176714586764426*m.b314
                          - 0.0314159265358979*m.b315 - 0.0490873852123405*m.b316 - 0.0706858347057703*m.b317
                          - 0.0962112750161874*m.b318 - 0.125663706143592*m.b319 - 0.159043128087983*m.b320
                          - 0.196349540849362*m.b321 - 0.282743338823081*m.b322 == 0)

m.c225 = Constraint(expr=   m.x109 - 0.00282743338823081*m.b323 - 0.00502654824574367*m.b324
                          - 0.00785398163397448*m.b325 - 0.0122718463030851*m.b326 - 0.0176714586764426*m.b327
                          - 0.0314159265358979*m.b328 - 0.0490873852123405*m.b329 - 0.0706858347057703*m.b330
                          - 0.0962112750161874*m.b331 - 0.125663706143592*m.b332 - 0.159043128087983*m.b333
                          - 0.196349540849362*m.b334 - 0.282743338823081*m.b335 == 0)

m.c226 = Constraint(expr=   m.x110 - 0.00282743338823081*m.b336 - 0.00502654824574367*m.b337
                          - 0.00785398163397448*m.b338 - 0.0122718463030851*m.b339 - 0.0176714586764426*m.b340
                          - 0.0314159265358979*m.b341 - 0.0490873852123405*m.b342 - 0.0706858347057703*m.b343
                          - 0.0962112750161874*m.b344 - 0.125663706143592*m.b345 - 0.159043128087983*m.b346
                          - 0.196349540849362*m.b347 - 0.282743338823081*m.b348 == 0)

m.c227 = Constraint(expr=   m.x111 - 0.00282743338823081*m.b349 - 0.00502654824574367*m.b350
                          - 0.00785398163397448*m.b351 - 0.0122718463030851*m.b352 - 0.0176714586764426*m.b353
                          - 0.0314159265358979*m.b354 - 0.0490873852123405*m.b355 - 0.0706858347057703*m.b356
                          - 0.0962112750161874*m.b357 - 0.125663706143592*m.b358 - 0.159043128087983*m.b359
                          - 0.196349540849362*m.b360 - 0.282743338823081*m.b361 == 0)

m.c228 = Constraint(expr=   m.x112 - 0.00282743338823081*m.b362 - 0.00502654824574367*m.b363
                          - 0.00785398163397448*m.b364 - 0.0122718463030851*m.b365 - 0.0176714586764426*m.b366
                          - 0.0314159265358979*m.b367 - 0.0490873852123405*m.b368 - 0.0706858347057703*m.b369
                          - 0.0962112750161874*m.b370 - 0.125663706143592*m.b371 - 0.159043128087983*m.b372
                          - 0.196349540849362*m.b373 - 0.282743338823081*m.b374 == 0)

m.c229 = Constraint(expr=   m.x113 - 0.00282743338823081*m.b375 - 0.00502654824574367*m.b376
                          - 0.00785398163397448*m.b377 - 0.0122718463030851*m.b378 - 0.0176714586764426*m.b379
                          - 0.0314159265358979*m.b380 - 0.0490873852123405*m.b381 - 0.0706858347057703*m.b382
                          - 0.0962112750161874*m.b383 - 0.125663706143592*m.b384 - 0.159043128087983*m.b385
                          - 0.196349540849362*m.b386 - 0.282743338823081*m.b387 == 0)

m.c230 = Constraint(expr=   m.x114 - 0.00282743338823081*m.b388 - 0.00502654824574367*m.b389
                          - 0.00785398163397448*m.b390 - 0.0122718463030851*m.b391 - 0.0176714586764426*m.b392
                          - 0.0314159265358979*m.b393 - 0.0490873852123405*m.b394 - 0.0706858347057703*m.b395
                          - 0.0962112750161874*m.b396 - 0.125663706143592*m.b397 - 0.159043128087983*m.b398
                          - 0.196349540849362*m.b399 - 0.282743338823081*m.b400 == 0)

m.c231 = Constraint(expr=   m.x115 - 0.00282743338823081*m.b401 - 0.00502654824574367*m.b402
                          - 0.00785398163397448*m.b403 - 0.0122718463030851*m.b404 - 0.0176714586764426*m.b405
                          - 0.0314159265358979*m.b406 - 0.0490873852123405*m.b407 - 0.0706858347057703*m.b408
                          - 0.0962112750161874*m.b409 - 0.125663706143592*m.b410 - 0.159043128087983*m.b411
                          - 0.196349540849362*m.b412 - 0.282743338823081*m.b413 == 0)

m.c232 = Constraint(expr=   m.x116 - 0.00282743338823081*m.b414 - 0.00502654824574367*m.b415
                          - 0.00785398163397448*m.b416 - 0.0122718463030851*m.b417 - 0.0176714586764426*m.b418
                          - 0.0314159265358979*m.b419 - 0.0490873852123405*m.b420 - 0.0706858347057703*m.b421
                          - 0.0962112750161874*m.b422 - 0.125663706143592*m.b423 - 0.159043128087983*m.b424
                          - 0.196349540849362*m.b425 - 0.282743338823081*m.b426 == 0)

m.c233 = Constraint(expr=   m.x117 - 0.00282743338823081*m.b427 - 0.00502654824574367*m.b428
                          - 0.00785398163397448*m.b429 - 0.0122718463030851*m.b430 - 0.0176714586764426*m.b431
                          - 0.0314159265358979*m.b432 - 0.0490873852123405*m.b433 - 0.0706858347057703*m.b434
                          - 0.0962112750161874*m.b435 - 0.125663706143592*m.b436 - 0.159043128087983*m.b437
                          - 0.196349540849362*m.b438 - 0.282743338823081*m.b439 == 0)

m.c234 = Constraint(expr=   m.x118 - 0.00282743338823081*m.b440 - 0.00502654824574367*m.b441
                          - 0.00785398163397448*m.b442 - 0.0122718463030851*m.b443 - 0.0176714586764426*m.b444
                          - 0.0314159265358979*m.b445 - 0.0490873852123405*m.b446 - 0.0706858347057703*m.b447
                          - 0.0962112750161874*m.b448 - 0.125663706143592*m.b449 - 0.159043128087983*m.b450
                          - 0.196349540849362*m.b451 - 0.282743338823081*m.b452 == 0)

m.c235 = Constraint(expr=   m.x119 - 0.00282743338823081*m.b453 - 0.00502654824574367*m.b454
                          - 0.00785398163397448*m.b455 - 0.0122718463030851*m.b456 - 0.0176714586764426*m.b457
                          - 0.0314159265358979*m.b458 - 0.0490873852123405*m.b459 - 0.0706858347057703*m.b460
                          - 0.0962112750161874*m.b461 - 0.125663706143592*m.b462 - 0.159043128087983*m.b463
                          - 0.196349540849362*m.b464 - 0.282743338823081*m.b465 == 0)

m.c236 = Constraint(expr=   m.x120 - 0.00282743338823081*m.b466 - 0.00502654824574367*m.b467
                          - 0.00785398163397448*m.b468 - 0.0122718463030851*m.b469 - 0.0176714586764426*m.b470
                          - 0.0314159265358979*m.b471 - 0.0490873852123405*m.b472 - 0.0706858347057703*m.b473
                          - 0.0962112750161874*m.b474 - 0.125663706143592*m.b475 - 0.159043128087983*m.b476
                          - 0.196349540849362*m.b477 - 0.282743338823081*m.b478 == 0)

m.c237 = Constraint(expr=   m.x121 - 0.00282743338823081*m.b479 - 0.00502654824574367*m.b480
                          - 0.00785398163397448*m.b481 - 0.0122718463030851*m.b482 - 0.0176714586764426*m.b483
                          - 0.0314159265358979*m.b484 - 0.0490873852123405*m.b485 - 0.0706858347057703*m.b486
                          - 0.0962112750161874*m.b487 - 0.125663706143592*m.b488 - 0.159043128087983*m.b489
                          - 0.196349540849362*m.b490 - 0.282743338823081*m.b491 == 0)

m.c238 = Constraint(expr=   m.x122 - 0.00282743338823081*m.b492 - 0.00502654824574367*m.b493
                          - 0.00785398163397448*m.b494 - 0.0122718463030851*m.b495 - 0.0176714586764426*m.b496
                          - 0.0314159265358979*m.b497 - 0.0490873852123405*m.b498 - 0.0706858347057703*m.b499
                          - 0.0962112750161874*m.b500 - 0.125663706143592*m.b501 - 0.159043128087983*m.b502
                          - 0.196349540849362*m.b503 - 0.282743338823081*m.b504 == 0)

m.c239 = Constraint(expr=   m.x123 - 0.00282743338823081*m.b505 - 0.00502654824574367*m.b506
                          - 0.00785398163397448*m.b507 - 0.0122718463030851*m.b508 - 0.0176714586764426*m.b509
                          - 0.0314159265358979*m.b510 - 0.0490873852123405*m.b511 - 0.0706858347057703*m.b512
                          - 0.0962112750161874*m.b513 - 0.125663706143592*m.b514 - 0.159043128087983*m.b515
                          - 0.196349540849362*m.b516 - 0.282743338823081*m.b517 == 0)

m.c240 = Constraint(expr=   m.x124 - 0.00282743338823081*m.b518 - 0.00502654824574367*m.b519
                          - 0.00785398163397448*m.b520 - 0.0122718463030851*m.b521 - 0.0176714586764426*m.b522
                          - 0.0314159265358979*m.b523 - 0.0490873852123405*m.b524 - 0.0706858347057703*m.b525
                          - 0.0962112750161874*m.b526 - 0.125663706143592*m.b527 - 0.159043128087983*m.b528
                          - 0.196349540849362*m.b529 - 0.282743338823081*m.b530 == 0)

m.c241 = Constraint(expr=   m.x125 - 0.00282743338823081*m.b531 - 0.00502654824574367*m.b532
                          - 0.00785398163397448*m.b533 - 0.0122718463030851*m.b534 - 0.0176714586764426*m.b535
                          - 0.0314159265358979*m.b536 - 0.0490873852123405*m.b537 - 0.0706858347057703*m.b538
                          - 0.0962112750161874*m.b539 - 0.125663706143592*m.b540 - 0.159043128087983*m.b541
                          - 0.196349540849362*m.b542 - 0.282743338823081*m.b543 == 0)

m.c242 = Constraint(expr=   m.x126 - 0.00282743338823081*m.b544 - 0.00502654824574367*m.b545
                          - 0.00785398163397448*m.b546 - 0.0122718463030851*m.b547 - 0.0176714586764426*m.b548
                          - 0.0314159265358979*m.b549 - 0.0490873852123405*m.b550 - 0.0706858347057703*m.b551
                          - 0.0962112750161874*m.b552 - 0.125663706143592*m.b553 - 0.159043128087983*m.b554
                          - 0.196349540849362*m.b555 - 0.282743338823081*m.b556 == 0)

m.c243 = Constraint(expr=   m.x127 - 0.00282743338823081*m.b557 - 0.00502654824574367*m.b558
                          - 0.00785398163397448*m.b559 - 0.0122718463030851*m.b560 - 0.0176714586764426*m.b561
                          - 0.0314159265358979*m.b562 - 0.0490873852123405*m.b563 - 0.0706858347057703*m.b564
                          - 0.0962112750161874*m.b565 - 0.125663706143592*m.b566 - 0.159043128087983*m.b567
                          - 0.196349540849362*m.b568 - 0.282743338823081*m.b569 == 0)

m.c244 = Constraint(expr=   m.x128 - 0.00282743338823081*m.b570 - 0.00502654824574367*m.b571
                          - 0.00785398163397448*m.b572 - 0.0122718463030851*m.b573 - 0.0176714586764426*m.b574
                          - 0.0314159265358979*m.b575 - 0.0490873852123405*m.b576 - 0.0706858347057703*m.b577
                          - 0.0962112750161874*m.b578 - 0.125663706143592*m.b579 - 0.159043128087983*m.b580
                          - 0.196349540849362*m.b581 - 0.282743338823081*m.b582 == 0)

m.c245 = Constraint(expr=   m.x129 - 0.00282743338823081*m.b583 - 0.00502654824574367*m.b584
                          - 0.00785398163397448*m.b585 - 0.0122718463030851*m.b586 - 0.0176714586764426*m.b587
                          - 0.0314159265358979*m.b588 - 0.0490873852123405*m.b589 - 0.0706858347057703*m.b590
                          - 0.0962112750161874*m.b591 - 0.125663706143592*m.b592 - 0.159043128087983*m.b593
                          - 0.196349540849362*m.b594 - 0.282743338823081*m.b595 == 0)

m.c246 = Constraint(expr=   m.x130 - 0.00282743338823081*m.b596 - 0.00502654824574367*m.b597
                          - 0.00785398163397448*m.b598 - 0.0122718463030851*m.b599 - 0.0176714586764426*m.b600
                          - 0.0314159265358979*m.b601 - 0.0490873852123405*m.b602 - 0.0706858347057703*m.b603
                          - 0.0962112750161874*m.b604 - 0.125663706143592*m.b605 - 0.159043128087983*m.b606
                          - 0.196349540849362*m.b607 - 0.282743338823081*m.b608 == 0)

m.c247 = Constraint(expr=   m.x131 - 0.00282743338823081*m.b609 - 0.00502654824574367*m.b610
                          - 0.00785398163397448*m.b611 - 0.0122718463030851*m.b612 - 0.0176714586764426*m.b613
                          - 0.0314159265358979*m.b614 - 0.0490873852123405*m.b615 - 0.0706858347057703*m.b616
                          - 0.0962112750161874*m.b617 - 0.125663706143592*m.b618 - 0.159043128087983*m.b619
                          - 0.196349540849362*m.b620 - 0.282743338823081*m.b621 == 0)

m.c248 = Constraint(expr=   m.x132 - 0.00282743338823081*m.b622 - 0.00502654824574367*m.b623
                          - 0.00785398163397448*m.b624 - 0.0122718463030851*m.b625 - 0.0176714586764426*m.b626
                          - 0.0314159265358979*m.b627 - 0.0490873852123405*m.b628 - 0.0706858347057703*m.b629
                          - 0.0962112750161874*m.b630 - 0.125663706143592*m.b631 - 0.159043128087983*m.b632
                          - 0.196349540849362*m.b633 - 0.282743338823081*m.b634 == 0)

m.c249 = Constraint(expr=   m.x133 - 0.00282743338823081*m.b635 - 0.00502654824574367*m.b636
                          - 0.00785398163397448*m.b637 - 0.0122718463030851*m.b638 - 0.0176714586764426*m.b639
                          - 0.0314159265358979*m.b640 - 0.0490873852123405*m.b641 - 0.0706858347057703*m.b642
                          - 0.0962112750161874*m.b643 - 0.125663706143592*m.b644 - 0.159043128087983*m.b645
                          - 0.196349540849362*m.b646 - 0.282743338823081*m.b647 == 0)

m.c250 = Constraint(expr=   m.x134 - 0.00282743338823081*m.b648 - 0.00502654824574367*m.b649
                          - 0.00785398163397448*m.b650 - 0.0122718463030851*m.b651 - 0.0176714586764426*m.b652
                          - 0.0314159265358979*m.b653 - 0.0490873852123405*m.b654 - 0.0706858347057703*m.b655
                          - 0.0962112750161874*m.b656 - 0.125663706143592*m.b657 - 0.159043128087983*m.b658
                          - 0.196349540849362*m.b659 - 0.282743338823081*m.b660 == 0)

m.c251 = Constraint(expr=   m.x135 - 0.00282743338823081*m.b661 - 0.00502654824574367*m.b662
                          - 0.00785398163397448*m.b663 - 0.0122718463030851*m.b664 - 0.0176714586764426*m.b665
                          - 0.0314159265358979*m.b666 - 0.0490873852123405*m.b667 - 0.0706858347057703*m.b668
                          - 0.0962112750161874*m.b669 - 0.125663706143592*m.b670 - 0.159043128087983*m.b671
                          - 0.196349540849362*m.b672 - 0.282743338823081*m.b673 == 0)

m.c252 = Constraint(expr=   m.x136 - 0.00282743338823081*m.b674 - 0.00502654824574367*m.b675
                          - 0.00785398163397448*m.b676 - 0.0122718463030851*m.b677 - 0.0176714586764426*m.b678
                          - 0.0314159265358979*m.b679 - 0.0490873852123405*m.b680 - 0.0706858347057703*m.b681
                          - 0.0962112750161874*m.b682 - 0.125663706143592*m.b683 - 0.159043128087983*m.b684
                          - 0.196349540849362*m.b685 - 0.282743338823081*m.b686 == 0)

m.c253 = Constraint(expr=   m.x137 - 0.00282743338823081*m.b687 - 0.00502654824574367*m.b688
                          - 0.00785398163397448*m.b689 - 0.0122718463030851*m.b690 - 0.0176714586764426*m.b691
                          - 0.0314159265358979*m.b692 - 0.0490873852123405*m.b693 - 0.0706858347057703*m.b694
                          - 0.0962112750161874*m.b695 - 0.125663706143592*m.b696 - 0.159043128087983*m.b697
                          - 0.196349540849362*m.b698 - 0.282743338823081*m.b699 == 0)

m.c254 = Constraint(expr=   m.x138 - 0.00282743338823081*m.b700 - 0.00502654824574367*m.b701
                          - 0.00785398163397448*m.b702 - 0.0122718463030851*m.b703 - 0.0176714586764426*m.b704
                          - 0.0314159265358979*m.b705 - 0.0490873852123405*m.b706 - 0.0706858347057703*m.b707
                          - 0.0962112750161874*m.b708 - 0.125663706143592*m.b709 - 0.159043128087983*m.b710
                          - 0.196349540849362*m.b711 - 0.282743338823081*m.b712 == 0)

m.c255 = Constraint(expr=   m.x139 - 0.00282743338823081*m.b713 - 0.00502654824574367*m.b714
                          - 0.00785398163397448*m.b715 - 0.0122718463030851*m.b716 - 0.0176714586764426*m.b717
                          - 0.0314159265358979*m.b718 - 0.0490873852123405*m.b719 - 0.0706858347057703*m.b720
                          - 0.0962112750161874*m.b721 - 0.125663706143592*m.b722 - 0.159043128087983*m.b723
                          - 0.196349540849362*m.b724 - 0.282743338823081*m.b725 == 0)

m.c256 = Constraint(expr=   m.x140 - 0.00282743338823081*m.b726 - 0.00502654824574367*m.b727
                          - 0.00785398163397448*m.b728 - 0.0122718463030851*m.b729 - 0.0176714586764426*m.b730
                          - 0.0314159265358979*m.b731 - 0.0490873852123405*m.b732 - 0.0706858347057703*m.b733
                          - 0.0962112750161874*m.b734 - 0.125663706143592*m.b735 - 0.159043128087983*m.b736
                          - 0.196349540849362*m.b737 - 0.282743338823081*m.b738 == 0)

m.c257 = Constraint(expr=   m.x141 - 0.00282743338823081*m.b739 - 0.00502654824574367*m.b740
                          - 0.00785398163397448*m.b741 - 0.0122718463030851*m.b742 - 0.0176714586764426*m.b743
                          - 0.0314159265358979*m.b744 - 0.0490873852123405*m.b745 - 0.0706858347057703*m.b746
                          - 0.0962112750161874*m.b747 - 0.125663706143592*m.b748 - 0.159043128087983*m.b749
                          - 0.196349540849362*m.b750 - 0.282743338823081*m.b751 == 0)

m.c258 = Constraint(expr=   m.x142 - 0.00282743338823081*m.b752 - 0.00502654824574367*m.b753
                          - 0.00785398163397448*m.b754 - 0.0122718463030851*m.b755 - 0.0176714586764426*m.b756
                          - 0.0314159265358979*m.b757 - 0.0490873852123405*m.b758 - 0.0706858347057703*m.b759
                          - 0.0962112750161874*m.b760 - 0.125663706143592*m.b761 - 0.159043128087983*m.b762
                          - 0.196349540849362*m.b763 - 0.282743338823081*m.b764 == 0)

m.c259 = Constraint(expr=   m.x143 - 0.00282743338823081*m.b765 - 0.00502654824574367*m.b766
                          - 0.00785398163397448*m.b767 - 0.0122718463030851*m.b768 - 0.0176714586764426*m.b769
                          - 0.0314159265358979*m.b770 - 0.0490873852123405*m.b771 - 0.0706858347057703*m.b772
                          - 0.0962112750161874*m.b773 - 0.125663706143592*m.b774 - 0.159043128087983*m.b775
                          - 0.196349540849362*m.b776 - 0.282743338823081*m.b777 == 0)

m.c260 = Constraint(expr=   m.x144 - 0.00282743338823081*m.b778 - 0.00502654824574367*m.b779
                          - 0.00785398163397448*m.b780 - 0.0122718463030851*m.b781 - 0.0176714586764426*m.b782
                          - 0.0314159265358979*m.b783 - 0.0490873852123405*m.b784 - 0.0706858347057703*m.b785
                          - 0.0962112750161874*m.b786 - 0.125663706143592*m.b787 - 0.159043128087983*m.b788
                          - 0.196349540849362*m.b789 - 0.282743338823081*m.b790 == 0)

m.c261 = Constraint(expr=   m.x145 - 0.00282743338823081*m.b791 - 0.00502654824574367*m.b792
                          - 0.00785398163397448*m.b793 - 0.0122718463030851*m.b794 - 0.0176714586764426*m.b795
                          - 0.0314159265358979*m.b796 - 0.0490873852123405*m.b797 - 0.0706858347057703*m.b798
                          - 0.0962112750161874*m.b799 - 0.125663706143592*m.b800 - 0.159043128087983*m.b801
                          - 0.196349540849362*m.b802 - 0.282743338823081*m.b803 == 0)

m.c262 = Constraint(expr=   m.x146 - 0.00282743338823081*m.b804 - 0.00502654824574367*m.b805
                          - 0.00785398163397448*m.b806 - 0.0122718463030851*m.b807 - 0.0176714586764426*m.b808
                          - 0.0314159265358979*m.b809 - 0.0490873852123405*m.b810 - 0.0706858347057703*m.b811
                          - 0.0962112750161874*m.b812 - 0.125663706143592*m.b813 - 0.159043128087983*m.b814
                          - 0.196349540849362*m.b815 - 0.282743338823081*m.b816 == 0)

m.c263 = Constraint(expr=   m.x147 - 0.00282743338823081*m.b817 - 0.00502654824574367*m.b818
                          - 0.00785398163397448*m.b819 - 0.0122718463030851*m.b820 - 0.0176714586764426*m.b821
                          - 0.0314159265358979*m.b822 - 0.0490873852123405*m.b823 - 0.0706858347057703*m.b824
                          - 0.0962112750161874*m.b825 - 0.125663706143592*m.b826 - 0.159043128087983*m.b827
                          - 0.196349540849362*m.b828 - 0.282743338823081*m.b829 == 0)

m.c264 = Constraint(expr=   m.x148 - 0.00282743338823081*m.b830 - 0.00502654824574367*m.b831
                          - 0.00785398163397448*m.b832 - 0.0122718463030851*m.b833 - 0.0176714586764426*m.b834
                          - 0.0314159265358979*m.b835 - 0.0490873852123405*m.b836 - 0.0706858347057703*m.b837
                          - 0.0962112750161874*m.b838 - 0.125663706143592*m.b839 - 0.159043128087983*m.b840
                          - 0.196349540849362*m.b841 - 0.282743338823081*m.b842 == 0)

m.c265 = Constraint(expr=   m.x149 - 0.00282743338823081*m.b843 - 0.00502654824574367*m.b844
                          - 0.00785398163397448*m.b845 - 0.0122718463030851*m.b846 - 0.0176714586764426*m.b847
                          - 0.0314159265358979*m.b848 - 0.0490873852123405*m.b849 - 0.0706858347057703*m.b850
                          - 0.0962112750161874*m.b851 - 0.125663706143592*m.b852 - 0.159043128087983*m.b853
                          - 0.196349540849362*m.b854 - 0.282743338823081*m.b855 == 0)

m.c266 = Constraint(expr=   m.x150 - 0.00282743338823081*m.b856 - 0.00502654824574367*m.b857
                          - 0.00785398163397448*m.b858 - 0.0122718463030851*m.b859 - 0.0176714586764426*m.b860
                          - 0.0314159265358979*m.b861 - 0.0490873852123405*m.b862 - 0.0706858347057703*m.b863
                          - 0.0962112750161874*m.b864 - 0.125663706143592*m.b865 - 0.159043128087983*m.b866
                          - 0.196349540849362*m.b867 - 0.282743338823081*m.b868 == 0)

m.c267 = Constraint(expr=   m.x151 - 0.00282743338823081*m.b869 - 0.00502654824574367*m.b870
                          - 0.00785398163397448*m.b871 - 0.0122718463030851*m.b872 - 0.0176714586764426*m.b873
                          - 0.0314159265358979*m.b874 - 0.0490873852123405*m.b875 - 0.0706858347057703*m.b876
                          - 0.0962112750161874*m.b877 - 0.125663706143592*m.b878 - 0.159043128087983*m.b879
                          - 0.196349540849362*m.b880 - 0.282743338823081*m.b881 == 0)

m.c268 = Constraint(expr=   m.x152 - 0.00282743338823081*m.b882 - 0.00502654824574367*m.b883
                          - 0.00785398163397448*m.b884 - 0.0122718463030851*m.b885 - 0.0176714586764426*m.b886
                          - 0.0314159265358979*m.b887 - 0.0490873852123405*m.b888 - 0.0706858347057703*m.b889
                          - 0.0962112750161874*m.b890 - 0.125663706143592*m.b891 - 0.159043128087983*m.b892
                          - 0.196349540849362*m.b893 - 0.282743338823081*m.b894 == 0)

m.c269 = Constraint(expr=   m.x153 - 0.00282743338823081*m.b895 - 0.00502654824574367*m.b896
                          - 0.00785398163397448*m.b897 - 0.0122718463030851*m.b898 - 0.0176714586764426*m.b899
                          - 0.0314159265358979*m.b900 - 0.0490873852123405*m.b901 - 0.0706858347057703*m.b902
                          - 0.0962112750161874*m.b903 - 0.125663706143592*m.b904 - 0.159043128087983*m.b905
                          - 0.196349540849362*m.b906 - 0.282743338823081*m.b907 == 0)

m.c270 = Constraint(expr=   m.b154 + m.b155 + m.b156 + m.b157 + m.b158 + m.b159 + m.b160 + m.b161 + m.b162 + m.b163
                          + m.b164 + m.b165 + m.b166 == 1)

m.c271 = Constraint(expr=   m.b167 + m.b168 + m.b169 + m.b170 + m.b171 + m.b172 + m.b173 + m.b174 + m.b175 + m.b176
                          + m.b177 + m.b178 + m.b179 == 1)

m.c272 = Constraint(expr=   m.b180 + m.b181 + m.b182 + m.b183 + m.b184 + m.b185 + m.b186 + m.b187 + m.b188 + m.b189
                          + m.b190 + m.b191 + m.b192 == 1)

m.c273 = Constraint(expr=   m.b193 + m.b194 + m.b195 + m.b196 + m.b197 + m.b198 + m.b199 + m.b200 + m.b201 + m.b202
                          + m.b203 + m.b204 + m.b205 == 1)

m.c274 = Constraint(expr=   m.b206 + m.b207 + m.b208 + m.b209 + m.b210 + m.b211 + m.b212 + m.b213 + m.b214 + m.b215
                          + m.b216 + m.b217 + m.b218 == 1)

m.c275 = Constraint(expr=   m.b219 + m.b220 + m.b221 + m.b222 + m.b223 + m.b224 + m.b225 + m.b226 + m.b227 + m.b228
                          + m.b229 + m.b230 + m.b231 == 1)

m.c276 = Constraint(expr=   m.b232 + m.b233 + m.b234 + m.b235 + m.b236 + m.b237 + m.b238 + m.b239 + m.b240 + m.b241
                          + m.b242 + m.b243 + m.b244 == 1)

m.c277 = Constraint(expr=   m.b245 + m.b246 + m.b247 + m.b248 + m.b249 + m.b250 + m.b251 + m.b252 + m.b253 + m.b254
                          + m.b255 + m.b256 + m.b257 == 1)

m.c278 = Constraint(expr=   m.b258 + m.b259 + m.b260 + m.b261 + m.b262 + m.b263 + m.b264 + m.b265 + m.b266 + m.b267
                          + m.b268 + m.b269 + m.b270 == 1)

m.c279 = Constraint(expr=   m.b271 + m.b272 + m.b273 + m.b274 + m.b275 + m.b276 + m.b277 + m.b278 + m.b279 + m.b280
                          + m.b281 + m.b282 + m.b283 == 1)

m.c280 = Constraint(expr=   m.b284 + m.b285 + m.b286 + m.b287 + m.b288 + m.b289 + m.b290 + m.b291 + m.b292 + m.b293
                          + m.b294 + m.b295 + m.b296 == 1)

m.c281 = Constraint(expr=   m.b297 + m.b298 + m.b299 + m.b300 + m.b301 + m.b302 + m.b303 + m.b304 + m.b305 + m.b306
                          + m.b307 + m.b308 + m.b309 == 1)

m.c282 = Constraint(expr=   m.b310 + m.b311 + m.b312 + m.b313 + m.b314 + m.b315 + m.b316 + m.b317 + m.b318 + m.b319
                          + m.b320 + m.b321 + m.b322 == 1)

m.c283 = Constraint(expr=   m.b323 + m.b324 + m.b325 + m.b326 + m.b327 + m.b328 + m.b329 + m.b330 + m.b331 + m.b332
                          + m.b333 + m.b334 + m.b335 == 1)

m.c284 = Constraint(expr=   m.b336 + m.b337 + m.b338 + m.b339 + m.b340 + m.b341 + m.b342 + m.b343 + m.b344 + m.b345
                          + m.b346 + m.b347 + m.b348 == 1)

m.c285 = Constraint(expr=   m.b349 + m.b350 + m.b351 + m.b352 + m.b353 + m.b354 + m.b355 + m.b356 + m.b357 + m.b358
                          + m.b359 + m.b360 + m.b361 == 1)

m.c286 = Constraint(expr=   m.b362 + m.b363 + m.b364 + m.b365 + m.b366 + m.b367 + m.b368 + m.b369 + m.b370 + m.b371
                          + m.b372 + m.b373 + m.b374 == 1)

m.c287 = Constraint(expr=   m.b375 + m.b376 + m.b377 + m.b378 + m.b379 + m.b380 + m.b381 + m.b382 + m.b383 + m.b384
                          + m.b385 + m.b386 + m.b387 == 1)

m.c288 = Constraint(expr=   m.b388 + m.b389 + m.b390 + m.b391 + m.b392 + m.b393 + m.b394 + m.b395 + m.b396 + m.b397
                          + m.b398 + m.b399 + m.b400 == 1)

m.c289 = Constraint(expr=   m.b401 + m.b402 + m.b403 + m.b404 + m.b405 + m.b406 + m.b407 + m.b408 + m.b409 + m.b410
                          + m.b411 + m.b412 + m.b413 == 1)

m.c290 = Constraint(expr=   m.b414 + m.b415 + m.b416 + m.b417 + m.b418 + m.b419 + m.b420 + m.b421 + m.b422 + m.b423
                          + m.b424 + m.b425 + m.b426 == 1)

m.c291 = Constraint(expr=   m.b427 + m.b428 + m.b429 + m.b430 + m.b431 + m.b432 + m.b433 + m.b434 + m.b435 + m.b436
                          + m.b437 + m.b438 + m.b439 == 1)

m.c292 = Constraint(expr=   m.b440 + m.b441 + m.b442 + m.b443 + m.b444 + m.b445 + m.b446 + m.b447 + m.b448 + m.b449
                          + m.b450 + m.b451 + m.b452 == 1)

m.c293 = Constraint(expr=   m.b453 + m.b454 + m.b455 + m.b456 + m.b457 + m.b458 + m.b459 + m.b460 + m.b461 + m.b462
                          + m.b463 + m.b464 + m.b465 == 1)

m.c294 = Constraint(expr=   m.b466 + m.b467 + m.b468 + m.b469 + m.b470 + m.b471 + m.b472 + m.b473 + m.b474 + m.b475
                          + m.b476 + m.b477 + m.b478 == 1)

m.c295 = Constraint(expr=   m.b479 + m.b480 + m.b481 + m.b482 + m.b483 + m.b484 + m.b485 + m.b486 + m.b487 + m.b488
                          + m.b489 + m.b490 + m.b491 == 1)

m.c296 = Constraint(expr=   m.b492 + m.b493 + m.b494 + m.b495 + m.b496 + m.b497 + m.b498 + m.b499 + m.b500 + m.b501
                          + m.b502 + m.b503 + m.b504 == 1)

m.c297 = Constraint(expr=   m.b505 + m.b506 + m.b507 + m.b508 + m.b509 + m.b510 + m.b511 + m.b512 + m.b513 + m.b514
                          + m.b515 + m.b516 + m.b517 == 1)

m.c298 = Constraint(expr=   m.b518 + m.b519 + m.b520 + m.b521 + m.b522 + m.b523 + m.b524 + m.b525 + m.b526 + m.b527
                          + m.b528 + m.b529 + m.b530 == 1)

m.c299 = Constraint(expr=   m.b531 + m.b532 + m.b533 + m.b534 + m.b535 + m.b536 + m.b537 + m.b538 + m.b539 + m.b540
                          + m.b541 + m.b542 + m.b543 == 1)

m.c300 = Constraint(expr=   m.b544 + m.b545 + m.b546 + m.b547 + m.b548 + m.b549 + m.b550 + m.b551 + m.b552 + m.b553
                          + m.b554 + m.b555 + m.b556 == 1)

m.c301 = Constraint(expr=   m.b557 + m.b558 + m.b559 + m.b560 + m.b561 + m.b562 + m.b563 + m.b564 + m.b565 + m.b566
                          + m.b567 + m.b568 + m.b569 == 1)

m.c302 = Constraint(expr=   m.b570 + m.b571 + m.b572 + m.b573 + m.b574 + m.b575 + m.b576 + m.b577 + m.b578 + m.b579
                          + m.b580 + m.b581 + m.b582 == 1)

m.c303 = Constraint(expr=   m.b583 + m.b584 + m.b585 + m.b586 + m.b587 + m.b588 + m.b589 + m.b590 + m.b591 + m.b592
                          + m.b593 + m.b594 + m.b595 == 1)

m.c304 = Constraint(expr=   m.b596 + m.b597 + m.b598 + m.b599 + m.b600 + m.b601 + m.b602 + m.b603 + m.b604 + m.b605
                          + m.b606 + m.b607 + m.b608 == 1)

m.c305 = Constraint(expr=   m.b609 + m.b610 + m.b611 + m.b612 + m.b613 + m.b614 + m.b615 + m.b616 + m.b617 + m.b618
                          + m.b619 + m.b620 + m.b621 == 1)

m.c306 = Constraint(expr=   m.b622 + m.b623 + m.b624 + m.b625 + m.b626 + m.b627 + m.b628 + m.b629 + m.b630 + m.b631
                          + m.b632 + m.b633 + m.b634 == 1)

m.c307 = Constraint(expr=   m.b635 + m.b636 + m.b637 + m.b638 + m.b639 + m.b640 + m.b641 + m.b642 + m.b643 + m.b644
                          + m.b645 + m.b646 + m.b647 == 1)

m.c308 = Constraint(expr=   m.b648 + m.b649 + m.b650 + m.b651 + m.b652 + m.b653 + m.b654 + m.b655 + m.b656 + m.b657
                          + m.b658 + m.b659 + m.b660 == 1)

m.c309 = Constraint(expr=   m.b661 + m.b662 + m.b663 + m.b664 + m.b665 + m.b666 + m.b667 + m.b668 + m.b669 + m.b670
                          + m.b671 + m.b672 + m.b673 == 1)

m.c310 = Constraint(expr=   m.b674 + m.b675 + m.b676 + m.b677 + m.b678 + m.b679 + m.b680 + m.b681 + m.b682 + m.b683
                          + m.b684 + m.b685 + m.b686 == 1)

m.c311 = Constraint(expr=   m.b687 + m.b688 + m.b689 + m.b690 + m.b691 + m.b692 + m.b693 + m.b694 + m.b695 + m.b696
                          + m.b697 + m.b698 + m.b699 == 1)

m.c312 = Constraint(expr=   m.b700 + m.b701 + m.b702 + m.b703 + m.b704 + m.b705 + m.b706 + m.b707 + m.b708 + m.b709
                          + m.b710 + m.b711 + m.b712 == 1)

m.c313 = Constraint(expr=   m.b713 + m.b714 + m.b715 + m.b716 + m.b717 + m.b718 + m.b719 + m.b720 + m.b721 + m.b722
                          + m.b723 + m.b724 + m.b725 == 1)

m.c314 = Constraint(expr=   m.b726 + m.b727 + m.b728 + m.b729 + m.b730 + m.b731 + m.b732 + m.b733 + m.b734 + m.b735
                          + m.b736 + m.b737 + m.b738 == 1)

m.c315 = Constraint(expr=   m.b739 + m.b740 + m.b741 + m.b742 + m.b743 + m.b744 + m.b745 + m.b746 + m.b747 + m.b748
                          + m.b749 + m.b750 + m.b751 == 1)

m.c316 = Constraint(expr=   m.b752 + m.b753 + m.b754 + m.b755 + m.b756 + m.b757 + m.b758 + m.b759 + m.b760 + m.b761
                          + m.b762 + m.b763 + m.b764 == 1)

m.c317 = Constraint(expr=   m.b765 + m.b766 + m.b767 + m.b768 + m.b769 + m.b770 + m.b771 + m.b772 + m.b773 + m.b774
                          + m.b775 + m.b776 + m.b777 == 1)

m.c318 = Constraint(expr=   m.b778 + m.b779 + m.b780 + m.b781 + m.b782 + m.b783 + m.b784 + m.b785 + m.b786 + m.b787
                          + m.b788 + m.b789 + m.b790 == 1)

m.c319 = Constraint(expr=   m.b791 + m.b792 + m.b793 + m.b794 + m.b795 + m.b796 + m.b797 + m.b798 + m.b799 + m.b800
                          + m.b801 + m.b802 + m.b803 == 1)

m.c320 = Constraint(expr=   m.b804 + m.b805 + m.b806 + m.b807 + m.b808 + m.b809 + m.b810 + m.b811 + m.b812 + m.b813
                          + m.b814 + m.b815 + m.b816 == 1)

m.c321 = Constraint(expr=   m.b817 + m.b818 + m.b819 + m.b820 + m.b821 + m.b822 + m.b823 + m.b824 + m.b825 + m.b826
                          + m.b827 + m.b828 + m.b829 == 1)

m.c322 = Constraint(expr=   m.b830 + m.b831 + m.b832 + m.b833 + m.b834 + m.b835 + m.b836 + m.b837 + m.b838 + m.b839
                          + m.b840 + m.b841 + m.b842 == 1)

m.c323 = Constraint(expr=   m.b843 + m.b844 + m.b845 + m.b846 + m.b847 + m.b848 + m.b849 + m.b850 + m.b851 + m.b852
                          + m.b853 + m.b854 + m.b855 == 1)

m.c324 = Constraint(expr=   m.b856 + m.b857 + m.b858 + m.b859 + m.b860 + m.b861 + m.b862 + m.b863 + m.b864 + m.b865
                          + m.b866 + m.b867 + m.b868 == 1)

m.c325 = Constraint(expr=   m.b869 + m.b870 + m.b871 + m.b872 + m.b873 + m.b874 + m.b875 + m.b876 + m.b877 + m.b878
                          + m.b879 + m.b880 + m.b881 == 1)

m.c326 = Constraint(expr=   m.b882 + m.b883 + m.b884 + m.b885 + m.b886 + m.b887 + m.b888 + m.b889 + m.b890 + m.b891
                          + m.b892 + m.b893 + m.b894 == 1)

m.c327 = Constraint(expr=   m.b895 + m.b896 + m.b897 + m.b898 + m.b899 + m.b900 + m.b901 + m.b902 + m.b903 + m.b904
                          + m.b905 + m.b906 + m.b907 == 1)
