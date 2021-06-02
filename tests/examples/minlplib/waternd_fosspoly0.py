#  MINLP written by GAMS Convert at 04/21/18 13:55:14
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        327      211       58       58        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        560      154      406        0        0        0        0        0
#  FX      1        1        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1856     1624      232        0
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
m.x96 = Var(within=Reals,bounds=(0.00282743338823081,0.0706858347057703),initialize=0.00282743338823081)
m.x97 = Var(within=Reals,bounds=(0.00282743338823081,0.0706858347057703),initialize=0.00282743338823081)
m.x98 = Var(within=Reals,bounds=(0.00282743338823081,0.0706858347057703),initialize=0.00282743338823081)
m.x99 = Var(within=Reals,bounds=(0.00282743338823081,0.0706858347057703),initialize=0.00282743338823081)
m.x100 = Var(within=Reals,bounds=(0.00282743338823081,0.0706858347057703),initialize=0.00282743338823081)
m.x101 = Var(within=Reals,bounds=(0.00282743338823081,0.0706858347057703),initialize=0.00282743338823081)
m.x102 = Var(within=Reals,bounds=(0.00282743338823081,0.0706858347057703),initialize=0.00282743338823081)
m.x103 = Var(within=Reals,bounds=(0.00282743338823081,0.0706858347057703),initialize=0.00282743338823081)
m.x104 = Var(within=Reals,bounds=(0.00282743338823081,0.0706858347057703),initialize=0.00282743338823081)
m.x105 = Var(within=Reals,bounds=(0.00282743338823081,0.0706858347057703),initialize=0.00282743338823081)
m.x106 = Var(within=Reals,bounds=(0.00282743338823081,0.0706858347057703),initialize=0.00282743338823081)
m.x107 = Var(within=Reals,bounds=(0.00282743338823081,0.0706858347057703),initialize=0.00282743338823081)
m.x108 = Var(within=Reals,bounds=(0.00282743338823081,0.0706858347057703),initialize=0.00282743338823081)
m.x109 = Var(within=Reals,bounds=(0.00282743338823081,0.0706858347057703),initialize=0.00282743338823081)
m.x110 = Var(within=Reals,bounds=(0.00282743338823081,0.0706858347057703),initialize=0.00282743338823081)
m.x111 = Var(within=Reals,bounds=(0.00282743338823081,0.0706858347057703),initialize=0.00282743338823081)
m.x112 = Var(within=Reals,bounds=(0.00282743338823081,0.0706858347057703),initialize=0.00282743338823081)
m.x113 = Var(within=Reals,bounds=(0.00282743338823081,0.0706858347057703),initialize=0.00282743338823081)
m.x114 = Var(within=Reals,bounds=(0.00282743338823081,0.0706858347057703),initialize=0.00282743338823081)
m.x115 = Var(within=Reals,bounds=(0.00282743338823081,0.0706858347057703),initialize=0.00282743338823081)
m.x116 = Var(within=Reals,bounds=(0.00282743338823081,0.0706858347057703),initialize=0.00282743338823081)
m.x117 = Var(within=Reals,bounds=(0.00282743338823081,0.0706858347057703),initialize=0.00282743338823081)
m.x118 = Var(within=Reals,bounds=(0.00282743338823081,0.0706858347057703),initialize=0.00282743338823081)
m.x119 = Var(within=Reals,bounds=(0.00282743338823081,0.0706858347057703),initialize=0.00282743338823081)
m.x120 = Var(within=Reals,bounds=(0.00282743338823081,0.0706858347057703),initialize=0.00282743338823081)
m.x121 = Var(within=Reals,bounds=(0.00282743338823081,0.0706858347057703),initialize=0.00282743338823081)
m.x122 = Var(within=Reals,bounds=(0.00282743338823081,0.0706858347057703),initialize=0.00282743338823081)
m.x123 = Var(within=Reals,bounds=(0.00282743338823081,0.0706858347057703),initialize=0.00282743338823081)
m.x124 = Var(within=Reals,bounds=(0.00282743338823081,0.0706858347057703),initialize=0.00282743338823081)
m.x125 = Var(within=Reals,bounds=(0.00282743338823081,0.0706858347057703),initialize=0.00282743338823081)
m.x126 = Var(within=Reals,bounds=(0.00282743338823081,0.0706858347057703),initialize=0.00282743338823081)
m.x127 = Var(within=Reals,bounds=(0.00282743338823081,0.0706858347057703),initialize=0.00282743338823081)
m.x128 = Var(within=Reals,bounds=(0.00282743338823081,0.0706858347057703),initialize=0.00282743338823081)
m.x129 = Var(within=Reals,bounds=(0.00282743338823081,0.0706858347057703),initialize=0.00282743338823081)
m.x130 = Var(within=Reals,bounds=(0.00282743338823081,0.0706858347057703),initialize=0.00282743338823081)
m.x131 = Var(within=Reals,bounds=(0.00282743338823081,0.0706858347057703),initialize=0.00282743338823081)
m.x132 = Var(within=Reals,bounds=(0.00282743338823081,0.0706858347057703),initialize=0.00282743338823081)
m.x133 = Var(within=Reals,bounds=(0.00282743338823081,0.0706858347057703),initialize=0.00282743338823081)
m.x134 = Var(within=Reals,bounds=(0.00282743338823081,0.0706858347057703),initialize=0.00282743338823081)
m.x135 = Var(within=Reals,bounds=(0.00282743338823081,0.0706858347057703),initialize=0.00282743338823081)
m.x136 = Var(within=Reals,bounds=(0.00282743338823081,0.0706858347057703),initialize=0.00282743338823081)
m.x137 = Var(within=Reals,bounds=(0.00282743338823081,0.0706858347057703),initialize=0.00282743338823081)
m.x138 = Var(within=Reals,bounds=(0.00282743338823081,0.0706858347057703),initialize=0.00282743338823081)
m.x139 = Var(within=Reals,bounds=(0.00282743338823081,0.0706858347057703),initialize=0.00282743338823081)
m.x140 = Var(within=Reals,bounds=(0.00282743338823081,0.0706858347057703),initialize=0.00282743338823081)
m.x141 = Var(within=Reals,bounds=(0.00282743338823081,0.0706858347057703),initialize=0.00282743338823081)
m.x142 = Var(within=Reals,bounds=(0.00282743338823081,0.0706858347057703),initialize=0.00282743338823081)
m.x143 = Var(within=Reals,bounds=(0.00282743338823081,0.0706858347057703),initialize=0.00282743338823081)
m.x144 = Var(within=Reals,bounds=(0.00282743338823081,0.0706858347057703),initialize=0.00282743338823081)
m.x145 = Var(within=Reals,bounds=(0.00282743338823081,0.0706858347057703),initialize=0.00282743338823081)
m.x146 = Var(within=Reals,bounds=(0.00282743338823081,0.0706858347057703),initialize=0.00282743338823081)
m.x147 = Var(within=Reals,bounds=(0.00282743338823081,0.0706858347057703),initialize=0.00282743338823081)
m.x148 = Var(within=Reals,bounds=(0.00282743338823081,0.0706858347057703),initialize=0.00282743338823081)
m.x149 = Var(within=Reals,bounds=(0.00282743338823081,0.0706858347057703),initialize=0.00282743338823081)
m.x150 = Var(within=Reals,bounds=(0.00282743338823081,0.0706858347057703),initialize=0.00282743338823081)
m.x151 = Var(within=Reals,bounds=(0.00282743338823081,0.0706858347057703),initialize=0.00282743338823081)
m.x152 = Var(within=Reals,bounds=(0.00282743338823081,0.0706858347057703),initialize=0.00282743338823081)
m.x153 = Var(within=Reals,bounds=(0.00282743338823081,0.0706858347057703),initialize=0.00282743338823081)
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

m.obj = Objective(expr=   914716.4*m.b154 + 1324944.8*m.b155 + 2550319.6*m.b156 + 3996076*m.b157 + 8070480.4*m.b158
                        + 9265320.4*m.b159 + 14703170*m.b160 + 519574.9*m.b161 + 752591.8*m.b162 + 1448626.1*m.b163
                        + 2269841*m.b164 + 4584173.9*m.b165 + 5262863.9*m.b166 + 8351657.5*m.b167 + 825008.6*m.b168
                        + 1195005.2*m.b169 + 2300205.4*m.b170 + 3604174*m.b171 + 7278994.6*m.b172 + 8356654.6*m.b173
                        + 13261205*m.b174 + 1122863.3*m.b175 + 1626440.6*m.b176 + 3130653.7*m.b177 + 4905397*m.b178
                        + 9906946.3*m.b179 + 11373676.3*m.b180 + 18048927.5*m.b181 + 2154640.8*m.b182 + 3120945.6*m.b183
                        + 6007351.2*m.b184 + 9412872*m.b185 + 19010248.8*m.b186 + 21824728.8*m.b187 + 34633740*m.b188
                        + 1359534.8*m.b189 + 1969253.6*m.b190 + 3790517.2*m.b191 + 5939332*m.b192 + 11995082.8*m.b193
                        + 13770962.8*m.b194 + 21853190*m.b195 + 1991830.1*m.b196 + 2885118.2*m.b197 + 5553418.9*m.b198
                        + 8701609*m.b199 + 17573781.1*m.b200 + 20175591.1*m.b201 + 32016717.5*m.b202 + 2317313.7*m.b203
                        + 3356573.4*m.b204 + 6460899.3*m.b205 + 10123533*m.b206 + 20445500.7*m.b207 + 23472470.7*m.b208
                        + 37248547.5*m.b209 + 533217.1*m.b210 + 772352.2*m.b211 + 1486661.9*m.b212 + 2329439*m.b213
                        + 4704538.1*m.b214 + 5401048.1*m.b215 + 8570942.5*m.b216 + 935730.9*m.b217 + 1355383.8*m.b218
                        + 2608910.1*m.b219 + 4087881*m.b220 + 8255889.9*m.b221 + 9478179.9*m.b222 + 15040957.5*m.b223
                        + 1386681.4*m.b224 + 2008574.8*m.b225 + 3866204.6*m.b226 + 6057926*m.b227 + 12234595.4*m.b228
                        + 14045935.4*m.b229 + 22289545*m.b230 + 996707.4*m.b231 + 1443706.8*m.b232 + 2778918.6*m.b233
                        + 4354266*m.b234 + 8793881.4*m.b235 + 10095821.4*m.b236 + 16021095*m.b237 + 772851.3*m.b238
                        + 1119456.6*m.b239 + 2154785.7*m.b240 + 3376317*m.b241 + 6818814.3*m.b242 + 7828344.3*m.b243
                        + 12422827.5*m.b244 + 1012554.4*m.b245 + 1466660.8*m.b246 + 2823101.6*m.b247 + 4423496*m.b248
                        + 8933698.4*m.b249 + 10256338.4*m.b250 + 16275820*m.b251 + 343259.8*m.b252 + 497203.6*m.b253
                        + 957042.2*m.b254 + 1499582*m.b255 + 3028557.8*m.b256 + 3476937.8*m.b257 + 5517565*m.b258
                        + 1120934.1*m.b259 + 1623646.2*m.b260 + 3125274.9*m.b261 + 4896969*m.b262 + 9889925.1*m.b263
                        + 11354135.1*m.b264 + 18017917.5*m.b265 + 573937*m.b266 + 831334*m.b267 + 1600193*m.b268
                        + 2507330*m.b269 + 5063807*m.b270 + 5813507*m.b271 + 9225475*m.b272 + 365032.2*m.b273
                        + 528740.4*m.b274 + 1017745.8*m.b275 + 1594698*m.b276 + 3220654.2*m.b277 + 3697474.2*m.b278
                        + 5867535*m.b279 + 1404388.7*m.b280 + 2034223.4*m.b281 + 3915574.3*m.b282 + 6135283*m.b283
                        + 12390825.7*m.b284 + 14225295.7*m.b285 + 22574172.5*m.b286 + 774229.3*m.b287 + 1121452.6*m.b288
                        + 2158627.7*m.b289 + 3382337*m.b290 + 6830972.3*m.b291 + 7842302.3*m.b292 + 12444977.5*m.b293
                        + 257272.6*m.b294 + 372653.2*m.b295 + 717301.4*m.b296 + 1123934*m.b297 + 2269898.6*m.b298
                        + 2605958.6*m.b299 + 4135405*m.b300 + 449159.1*m.b301 + 650596.2*m.b302 + 1252299.9*m.b303
                        + 1962219*m.b304 + 3962900.1*m.b305 + 4549610.1*m.b306 + 7219792.5*m.b307 + 1259629.8*m.b308
                        + 1824543.6*m.b309 + 3511972.2*m.b310 + 5502882*m.b311 + 11113627.8*m.b312 + 12759007.8*m.b313
                        + 20247315*m.b314 + 556849.8*m.b315 + 806583.6*m.b316 + 1552552.2*m.b317 + 2432682*m.b318
                        + 4913047.8*m.b319 + 5640427.8*m.b320 + 8950815*m.b321 + 566978.1*m.b322 + 821254.2*m.b323
                        + 1580790.9*m.b324 + 2476929*m.b325 + 5002409.1*m.b326 + 5743019.1*m.b327 + 9113617.5*m.b328
                        + 937177.8*m.b329 + 1357479.6*m.b330 + 2612944.2*m.b331 + 4094202*m.b332 + 8268655.8*m.b333
                        + 9492835.8*m.b334 + 15064215*m.b335 + 2581545.2*m.b336 + 3739306.4*m.b337 + 7197602.8*m.b338
                        + 11277868*m.b339 + 22776797.2*m.b340 + 26148917.2*m.b341 + 41495810*m.b342 + 1616394*m.b343
                        + 2341308*m.b344 + 4506666*m.b345 + 7061460*m.b346 + 14261334*m.b347 + 16372734*m.b348
                        + 25981950*m.b349 + 578484.4*m.b350 + 837920.8*m.b351 + 1612871.6*m.b352 + 2527196*m.b353
                        + 5103928.4*m.b354 + 5859568.4*m.b355 + 9298570*m.b356 + 686519.6*m.b357 + 994407.2*m.b358
                        + 1914084.4*m.b359 + 2999164*m.b360 + 6057115.6*m.b361 + 6953875.6*m.b362 + 11035130*m.b363
                        + 1709064.5*m.b364 + 2475539*m.b365 + 4765040.5*m.b366 + 7466305*m.b367 + 15078959.5*m.b368
                        + 17311409.5*m.b369 + 27471537.5*m.b370 + 749976.5*m.b371 + 1086323*m.b372 + 2091008.5*m.b373
                        + 3276385*m.b374 + 6616991.5*m.b375 + 7596641.5*m.b376 + 12055137.5*m.b377 + 1447520.1*m.b378
                        + 2096698.2*m.b379 + 4035828.9*m.b380 + 6323709*m.b381 + 12771371.1*m.b382 + 14662181.1*m.b383
                        + 23267467.5*m.b384 + 1016757.3*m.b385 + 1472748.6*m.b386 + 2834819.7*m.b387 + 4441857*m.b388
                        + 8970780.3*m.b389 + 10298910.3*m.b390 + 16343377.5*m.b391 + 2349283.3*m.b392 + 3402880.6*m.b393
                        + 6550033.7*m.b394 + 10263197*m.b395 + 20727566.3*m.b396 + 23796296.3*m.b397 + 37762427.5*m.b398
                        + 715182*m.b399 + 1035924*m.b400 + 1993998*m.b401 + 3124380*m.b402 + 6310002*m.b403
                        + 7244202*m.b404 + 11495850*m.b405 + 517301.2*m.b406 + 749298.4*m.b407 + 1442286.8*m.b408
                        + 2259908*m.b409 + 4564113.2*m.b410 + 5239833.2*m.b411 + 8315110*m.b412 + 913131.7*m.b413
                        + 1322649.4*m.b414 + 2545901.3*m.b415 + 3989153*m.b416 + 8056498.7*m.b417 + 9249268.7*m.b418
                        + 14677697.5*m.b419 + 1453445.5*m.b420 + 2105281*m.b421 + 4052349.5*m.b422 + 6349595*m.b423
                        + 12823650.5*m.b424 + 14722200.5*m.b425 + 23362712.5*m.b426 + 1016206.1*m.b427
                        + 1471950.2*m.b428 + 2833282.9*m.b429 + 4439449*m.b430 + 8965917.1*m.b431 + 10293327.1*m.b432
                        + 16334517.5*m.b433 + 784082*m.b434 + 1135724*m.b435 + 2186098*m.b436 + 3425380*m.b437
                        + 6917902*m.b438 + 7942102*m.b439 + 12603350*m.b440 + 1242198.1*m.b441 + 1799294.2*m.b442
                        + 3463370.9*m.b443 + 5426729*m.b444 + 10959829.1*m.b445 + 12582439.1*m.b446 + 19967117.5*m.b447
                        + 683970.3*m.b448 + 990714.6*m.b449 + 1906976.7*m.b450 + 2988027*m.b451 + 6034623.3*m.b452
                        + 6928053.3*m.b453 + 10994152.5*m.b454 + 1210710.8*m.b455 + 1753685.6*m.b456 + 3375581.2*m.b457
                        + 5289172*m.b458 + 10682018.8*m.b459 + 12263498.8*m.b460 + 19460990*m.b461 + 1026954.5*m.b462
                        + 1487519*m.b463 + 2863250.5*m.b464 + 4486405*m.b465 + 9060749.5*m.b466 + 10402199.5*m.b467
                        + 16507287.5*m.b468 + 390663*m.b469 + 565866*m.b470 + 1089207*m.b471 + 1706670*m.b472
                        + 3446793*m.b473 + 3957093*m.b474 + 6279525*m.b475 + 1481694.5*m.b476 + 2146199*m.b477
                        + 4131110.5*m.b478 + 6473005*m.b479 + 13072889.5*m.b480 + 15008339.5*m.b481 + 23816787.5*m.b482
                        + 854911.2*m.b483 + 1238318.4*m.b484 + 2383576.8*m.b485 + 3734808*m.b486 + 7542823.2*m.b487
                        + 8659543.2*m.b488 + 13741860*m.b489 + 826593.3*m.b490 + 1197300.6*m.b491 + 2304623.7*m.b492
                        + 3611097*m.b493 + 7292976.3*m.b494 + 8372706.3*m.b495 + 13286677.5*m.b496 + 1249983.8*m.b497
                        + 1810571.6*m.b498 + 3485078.2*m.b499 + 5460742*m.b500 + 11028521.8*m.b501 + 12661301.8*m.b502
                        + 20092265*m.b503 + 412917.7*m.b504 + 598101.4*m.b505 + 1151255.3*m.b506 + 1803893*m.b507
                        + 3643144.7*m.b508 + 4182514.7*m.b509 + 6637247.5*m.b510 + 540865*m.b511 + 783430*m.b512
                        + 1507985*m.b513 + 2362850*m.b514 + 4772015*m.b515 + 5478515*m.b516 + 8693875*m.b517
                        + 995191.6*m.b518 + 1441511.2*m.b519 + 2774692.4*m.b520 + 4347644*m.b521 + 8780507.6*m.b522
                        + 10080467.6*m.b523 + 15996730*m.b524 + 239358.6*m.b525 + 346705.2*m.b526 + 667355.4*m.b527
                        + 1045674*m.b528 + 2111844.6*m.b529 + 2424504.6*m.b530 + 3847455*m.b531 + 1141466.3*m.b532
                        + 1653386.6*m.b533 + 3182520.7*m.b534 + 4986667*m.b535 + 10071079.3*m.b536 + 11562109.3*m.b537
                        + 18347952.5*m.b538 + 573041.3*m.b539 + 830036.6*m.b540 + 1597695.7*m.b541 + 2503417*m.b542
                        + 5055904.3*m.b543 + 5804434.3*m.b544 + 9211077.5*m.b545 + 1451998.6*m.b546 + 2103185.2*m.b547
                        + 4048315.4*m.b548 + 6343274*m.b549 + 12810884.6*m.b550 + 14707544.6*m.b551 + 23339455*m.b552
                        + 6890*m.b553 + 9980*m.b554 + 19210*m.b555 + 30100*m.b556 + 60790*m.b557 + 69790*m.b558
                        + 110750*m.b559, sense=minimize)

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

m.c38 = Constraint(expr=SignPower(m.x38,1.852) - 3.56081145657482*(1.27323954473516*m.x96)**2.435*(m.x1 - m.x17) == 0)

m.c39 = Constraint(expr=SignPower(m.x39,1.852) - 6.26884138675074*(1.27323954473516*m.x97)**2.435*(m.x1 - m.x31) == 0)

m.c40 = Constraint(expr=SignPower(m.x40,1.852) - 3.94799840466739*(1.27323954473516*m.x98)**2.435*(m.x2 - m.x3) == 0)

m.c41 = Constraint(expr=SignPower(m.x41,1.852) - 2.9007383504625*(1.27323954473516*m.x99)**2.435*(m.x2 - m.x18) == 0)

m.c42 = Constraint(expr=SignPower(m.x42,1.852) - 1.51168242829008*(1.27323954473516*m.x100)**2.435*(m.x3 - m.x4) == 0)

m.c43 = Constraint(expr=SignPower(m.x43,1.852) - 2.39576996237013*(1.27323954473516*m.x101)**2.435*(m.x3 - m.x11) == 0)

m.c44 = Constraint(expr=SignPower(m.x44,1.852) - 1.63524621735402*(1.27323954473516*m.x102)**2.435*(m.x4 - m.x5) == 0)

m.c45 = Constraint(expr=SignPower(m.x45,1.852) - 1.40556396686253*(1.27323954473516*m.x103)**2.435*(m.x5 - m.x6) == 0)

m.c46 = Constraint(expr=SignPower(m.x46,1.852) - 6.10845495509592*(1.27323954473516*m.x104)**2.435*(m.x5 - m.x13) == 0)

m.c47 = Constraint(expr=SignPower(m.x47,1.852) - 3.48084330295909*(1.27323954473516*m.x105)**2.435*(m.x6 - m.x7) == 0)

m.c48 = Constraint(expr=SignPower(m.x48,1.852) - 2.3488687716132*(1.27323954473516*m.x106)**2.435*(m.x7 - m.x24) == 0)

m.c49 = Constraint(expr=SignPower(m.x49,1.852) - 3.26789249948067*(1.27323954473516*m.x107)**2.435*(m.x8 - m.x28) == 0)

m.c50 = Constraint(expr=SignPower(m.x50,1.852) - 4.2144363820529*(1.27323954473516*m.x108)**2.435*(m.x9 - m.x36) == 0)

m.c51 = Constraint(expr=SignPower(m.x51,1.852) - 3.21674829188128*(1.27323954473516*m.x109)**2.435*(m.x10 - m.x11) == 0)

m.c52 = Constraint(expr=SignPower(m.x52,1.852) - 9.48882635437321*(1.27323954473516*m.x110)**2.435*(m.x10 - m.x32) == 0)

m.c53 = Constraint(expr=SignPower(m.x53,1.852) - 2.90573070855537*(1.27323954473516*m.x111)**2.435*(m.x11 - m.x19) == 0)

m.c54 = Constraint(expr=SignPower(m.x54,1.852) - 5.67506997568876*(1.27323954473516*m.x112)**2.435*(m.x11 - m.x26) == 0)

m.c55 = Constraint(expr=SignPower(m.x55,1.852) - 8.92286389156047*(1.27323954473516*m.x113)**2.435*(m.x12 - m.x4) == 0)

m.c56 = Constraint(expr=SignPower(m.x56,1.852) - 2.3192529508653*(1.27323954473516*m.x114)**2.435*(m.x12 - m.x13) == 0)

m.c57 = Constraint(expr=SignPower(m.x57,1.852) - 4.20693538288577*(1.27323954473516*m.x115)**2.435*(m.x13 - m.x14) == 0)

m.c58 = Constraint(expr=SignPower(m.x58,1.852) - 12.6602391262687*(1.27323954473516*m.x116)**2.435*(m.x14 - m.x20) == 0)

m.c59 = Constraint(expr=SignPower(m.x59,1.852) - 7.25162339277303*(1.27323954473516*m.x117)**2.435*(m.x14 - m.x21) == 0)

m.c60 = Constraint(expr=SignPower(m.x60,1.852) - 2.58578563053754*(1.27323954473516*m.x118)**2.435*(m.x15 - m.x16) == 0)

m.c61 = Constraint(expr=SignPower(m.x61,1.852) - 5.84921218726644*(1.27323954473516*m.x119)**2.435*(m.x15 - m.x22) == 0)

m.c62 = Constraint(expr=SignPower(m.x62,1.852) - 5.74472389081144*(1.27323954473516*m.x120)**2.435*(m.x16 - m.x25) == 0)

m.c63 = Constraint(expr=SignPower(m.x63,1.852) - 3.47546926168853*(1.27323954473516*m.x121)**2.435*(m.x16 - m.x29) == 0)

m.c64 = Constraint(expr=SignPower(m.x64,1.852) - 1.26169886029378*(1.27323954473516*m.x122)**2.435*(m.x17 - m.x2) == 0)

m.c65 = Constraint(expr=SignPower(m.x65,1.852) - 2.01506107832427*(1.27323954473516*m.x123)**2.435*(m.x17 - m.x18) == 0)

m.c66 = Constraint(expr=SignPower(m.x66,1.852) - 5.63045889679459*(1.27323954473516*m.x124)**2.435*(m.x18 - m.x10) == 0)

m.c67 = Constraint(expr=SignPower(m.x67,1.852) - 4.74441317718661*(1.27323954473516*m.x125)**2.435*(m.x19 - m.x12) == 0)

m.c68 = Constraint(expr=SignPower(m.x68,1.852) - 1.90579854454696*(1.27323954473516*m.x126)**2.435*(m.x19 - m.x20) == 0)

m.c69 = Constraint(expr=SignPower(m.x69,1.852) - 4.34297959554316*(1.27323954473516*m.x127)**2.435*(m.x20 - m.x15) == 0)

m.c70 = Constraint(expr=SignPower(m.x70,1.852) - 2.25014674175293*(1.27323954473516*m.x128)**2.435*(m.x21 - m.x6) == 0)

m.c71 = Constraint(expr=SignPower(m.x71,1.852) - 3.20345143982431*(1.27323954473516*m.x129)**2.435*(m.x21 - m.x22) == 0)

m.c72 = Constraint(expr=SignPower(m.x72,1.852) - 1.38643672163203*(1.27323954473516*m.x130)**2.435*(m.x22 - m.x7) == 0)

m.c73 = Constraint(expr=SignPower(m.x73,1.852) - 4.5542709920508*(1.27323954473516*m.x131)**2.435*(m.x22 - m.x23) == 0)

m.c74 = Constraint(expr=SignPower(m.x74,1.852) - 6.29639489843998*(1.27323954473516*m.x132)**2.435*(m.x23 - m.x25) == 0)

m.c75 = Constraint(expr=SignPower(m.x75,1.852) - 3.56699108862049*(1.27323954473516*m.x133)**2.435*(m.x24 - m.x8) == 0)

m.c76 = Constraint(expr=SignPower(m.x76,1.852) - 2.24097335375622*(1.27323954473516*m.x134)**2.435*(m.x24 - m.x23) == 0)

m.c77 = Constraint(expr=SignPower(m.x77,1.852) - 3.20518902281425*(1.27323954473516*m.x135)**2.435*(m.x25 - m.x8) == 0)

m.c78 = Constraint(expr=SignPower(m.x78,1.852) - 4.15407143211664*(1.27323954473516*m.x136)**2.435*(m.x26 - m.x15) == 0)

m.c79 = Constraint(expr=SignPower(m.x79,1.852) - 2.62207182303441*(1.27323954473516*m.x137)**2.435*(m.x26 - m.x27) == 0)

m.c80 = Constraint(expr=SignPower(m.x80,1.852) - 4.76209659489144*(1.27323954473516*m.x138)**2.435*(m.x27 - m.x16) == 0)

m.c81 = Constraint(expr=SignPower(m.x81,1.852) - 2.69026479043292*(1.27323954473516*m.x139)**2.435*(m.x28 - m.x9) == 0)

m.c82 = Constraint(expr=SignPower(m.x82,1.852) - 3.17164259627557*(1.27323954473516*m.x140)**2.435*(m.x28 - m.x29) == 0)

m.c83 = Constraint(expr=SignPower(m.x83,1.852) - 8.337448482802*(1.27323954473516*m.x141)**2.435*(m.x29 - m.x30) == 0)

m.c84 = Constraint(expr=SignPower(m.x84,1.852) - 2.19824844908102*(1.27323954473516*m.x142)**2.435*(m.x29 - m.x33) == 0)

m.c85 = Constraint(expr=SignPower(m.x85,1.852) - 3.80990755137712*(1.27323954473516*m.x143)**2.435*(m.x30 - m.x9) == 0)

m.c86 = Constraint(expr=SignPower(m.x86,1.852) - 3.94042951550282*(1.27323954473516*m.x144)**2.435*(m.x30 - m.x35) == 0)

m.c87 = Constraint(expr=SignPower(m.x87,1.852) - 2.60573987969834*(1.27323954473516*m.x145)**2.435*(m.x31 - m.x10) == 0)

m.c88 = Constraint(expr=SignPower(m.x88,1.852) - 7.88809158976929*(1.27323954473516*m.x146)**2.435*(m.x31 - m.x34) == 0)

m.c89 = Constraint(expr=SignPower(m.x89,1.852) - 6.02208062388374*(1.27323954473516*m.x147)**2.435*(m.x32 - m.x27) == 0)

m.c90 = Constraint(expr=SignPower(m.x90,1.852) - 3.27286990428464*(1.27323954473516*m.x148)**2.435*(m.x32 - m.x33) == 0)

m.c91 = Constraint(expr=SignPower(m.x91,1.852) - 13.6077527050913*(1.27323954473516*m.x149)**2.435*(m.x33 - m.x34) == 0)

m.c92 = Constraint(expr=SignPower(m.x92,1.852) - 2.85346368669568*(1.27323954473516*m.x150)**2.435*(m.x34 - m.x35) == 0)

m.c93 = Constraint(expr=SignPower(m.x93,1.852) - 5.68394047102168*(1.27323954473516*m.x151)**2.435*(m.x35 - m.x36) == 0)

m.c94 = Constraint(expr=SignPower(m.x94,1.852) - 2.2432064580757*(1.27323954473516*m.x152)**2.435*(m.x36 - m.x1) == 0)

m.c95 = Constraint(expr=SignPower(m.x95,1.852) - 472.733328974874*(1.27323954473516*m.x153)**2.435*(m.x37 - m.x1) == 0)

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

m.c212 = Constraint(expr=   m.x96 - 0.00282743338823081*m.b154 - 0.00502654824574367*m.b155 - 0.0122718463030851*m.b156
                          - 0.0176714586764426*m.b157 - 0.0314159265358979*m.b158 - 0.0490873852123405*m.b159
                          - 0.0706858347057703*m.b160 == 0)

m.c213 = Constraint(expr=   m.x97 - 0.00282743338823081*m.b161 - 0.00502654824574367*m.b162 - 0.0122718463030851*m.b163
                          - 0.0176714586764426*m.b164 - 0.0314159265358979*m.b165 - 0.0490873852123405*m.b166
                          - 0.0706858347057703*m.b167 == 0)

m.c214 = Constraint(expr=   m.x98 - 0.00282743338823081*m.b168 - 0.00502654824574367*m.b169 - 0.0122718463030851*m.b170
                          - 0.0176714586764426*m.b171 - 0.0314159265358979*m.b172 - 0.0490873852123405*m.b173
                          - 0.0706858347057703*m.b174 == 0)

m.c215 = Constraint(expr=   m.x99 - 0.00282743338823081*m.b175 - 0.00502654824574367*m.b176 - 0.0122718463030851*m.b177
                          - 0.0176714586764426*m.b178 - 0.0314159265358979*m.b179 - 0.0490873852123405*m.b180
                          - 0.0706858347057703*m.b181 == 0)

m.c216 = Constraint(expr=   m.x100 - 0.00282743338823081*m.b182 - 0.00502654824574367*m.b183 - 0.0122718463030851*m.b184
                          - 0.0176714586764426*m.b185 - 0.0314159265358979*m.b186 - 0.0490873852123405*m.b187
                          - 0.0706858347057703*m.b188 == 0)

m.c217 = Constraint(expr=   m.x101 - 0.00282743338823081*m.b189 - 0.00502654824574367*m.b190 - 0.0122718463030851*m.b191
                          - 0.0176714586764426*m.b192 - 0.0314159265358979*m.b193 - 0.0490873852123405*m.b194
                          - 0.0706858347057703*m.b195 == 0)

m.c218 = Constraint(expr=   m.x102 - 0.00282743338823081*m.b196 - 0.00502654824574367*m.b197 - 0.0122718463030851*m.b198
                          - 0.0176714586764426*m.b199 - 0.0314159265358979*m.b200 - 0.0490873852123405*m.b201
                          - 0.0706858347057703*m.b202 == 0)

m.c219 = Constraint(expr=   m.x103 - 0.00282743338823081*m.b203 - 0.00502654824574367*m.b204 - 0.0122718463030851*m.b205
                          - 0.0176714586764426*m.b206 - 0.0314159265358979*m.b207 - 0.0490873852123405*m.b208
                          - 0.0706858347057703*m.b209 == 0)

m.c220 = Constraint(expr=   m.x104 - 0.00282743338823081*m.b210 - 0.00502654824574367*m.b211 - 0.0122718463030851*m.b212
                          - 0.0176714586764426*m.b213 - 0.0314159265358979*m.b214 - 0.0490873852123405*m.b215
                          - 0.0706858347057703*m.b216 == 0)

m.c221 = Constraint(expr=   m.x105 - 0.00282743338823081*m.b217 - 0.00502654824574367*m.b218 - 0.0122718463030851*m.b219
                          - 0.0176714586764426*m.b220 - 0.0314159265358979*m.b221 - 0.0490873852123405*m.b222
                          - 0.0706858347057703*m.b223 == 0)

m.c222 = Constraint(expr=   m.x106 - 0.00282743338823081*m.b224 - 0.00502654824574367*m.b225 - 0.0122718463030851*m.b226
                          - 0.0176714586764426*m.b227 - 0.0314159265358979*m.b228 - 0.0490873852123405*m.b229
                          - 0.0706858347057703*m.b230 == 0)

m.c223 = Constraint(expr=   m.x107 - 0.00282743338823081*m.b231 - 0.00502654824574367*m.b232 - 0.0122718463030851*m.b233
                          - 0.0176714586764426*m.b234 - 0.0314159265358979*m.b235 - 0.0490873852123405*m.b236
                          - 0.0706858347057703*m.b237 == 0)

m.c224 = Constraint(expr=   m.x108 - 0.00282743338823081*m.b238 - 0.00502654824574367*m.b239 - 0.0122718463030851*m.b240
                          - 0.0176714586764426*m.b241 - 0.0314159265358979*m.b242 - 0.0490873852123405*m.b243
                          - 0.0706858347057703*m.b244 == 0)

m.c225 = Constraint(expr=   m.x109 - 0.00282743338823081*m.b245 - 0.00502654824574367*m.b246 - 0.0122718463030851*m.b247
                          - 0.0176714586764426*m.b248 - 0.0314159265358979*m.b249 - 0.0490873852123405*m.b250
                          - 0.0706858347057703*m.b251 == 0)

m.c226 = Constraint(expr=   m.x110 - 0.00282743338823081*m.b252 - 0.00502654824574367*m.b253 - 0.0122718463030851*m.b254
                          - 0.0176714586764426*m.b255 - 0.0314159265358979*m.b256 - 0.0490873852123405*m.b257
                          - 0.0706858347057703*m.b258 == 0)

m.c227 = Constraint(expr=   m.x111 - 0.00282743338823081*m.b259 - 0.00502654824574367*m.b260 - 0.0122718463030851*m.b261
                          - 0.0176714586764426*m.b262 - 0.0314159265358979*m.b263 - 0.0490873852123405*m.b264
                          - 0.0706858347057703*m.b265 == 0)

m.c228 = Constraint(expr=   m.x112 - 0.00282743338823081*m.b266 - 0.00502654824574367*m.b267 - 0.0122718463030851*m.b268
                          - 0.0176714586764426*m.b269 - 0.0314159265358979*m.b270 - 0.0490873852123405*m.b271
                          - 0.0706858347057703*m.b272 == 0)

m.c229 = Constraint(expr=   m.x113 - 0.00282743338823081*m.b273 - 0.00502654824574367*m.b274 - 0.0122718463030851*m.b275
                          - 0.0176714586764426*m.b276 - 0.0314159265358979*m.b277 - 0.0490873852123405*m.b278
                          - 0.0706858347057703*m.b279 == 0)

m.c230 = Constraint(expr=   m.x114 - 0.00282743338823081*m.b280 - 0.00502654824574367*m.b281 - 0.0122718463030851*m.b282
                          - 0.0176714586764426*m.b283 - 0.0314159265358979*m.b284 - 0.0490873852123405*m.b285
                          - 0.0706858347057703*m.b286 == 0)

m.c231 = Constraint(expr=   m.x115 - 0.00282743338823081*m.b287 - 0.00502654824574367*m.b288 - 0.0122718463030851*m.b289
                          - 0.0176714586764426*m.b290 - 0.0314159265358979*m.b291 - 0.0490873852123405*m.b292
                          - 0.0706858347057703*m.b293 == 0)

m.c232 = Constraint(expr=   m.x116 - 0.00282743338823081*m.b294 - 0.00502654824574367*m.b295 - 0.0122718463030851*m.b296
                          - 0.0176714586764426*m.b297 - 0.0314159265358979*m.b298 - 0.0490873852123405*m.b299
                          - 0.0706858347057703*m.b300 == 0)

m.c233 = Constraint(expr=   m.x117 - 0.00282743338823081*m.b301 - 0.00502654824574367*m.b302 - 0.0122718463030851*m.b303
                          - 0.0176714586764426*m.b304 - 0.0314159265358979*m.b305 - 0.0490873852123405*m.b306
                          - 0.0706858347057703*m.b307 == 0)

m.c234 = Constraint(expr=   m.x118 - 0.00282743338823081*m.b308 - 0.00502654824574367*m.b309 - 0.0122718463030851*m.b310
                          - 0.0176714586764426*m.b311 - 0.0314159265358979*m.b312 - 0.0490873852123405*m.b313
                          - 0.0706858347057703*m.b314 == 0)

m.c235 = Constraint(expr=   m.x119 - 0.00282743338823081*m.b315 - 0.00502654824574367*m.b316 - 0.0122718463030851*m.b317
                          - 0.0176714586764426*m.b318 - 0.0314159265358979*m.b319 - 0.0490873852123405*m.b320
                          - 0.0706858347057703*m.b321 == 0)

m.c236 = Constraint(expr=   m.x120 - 0.00282743338823081*m.b322 - 0.00502654824574367*m.b323 - 0.0122718463030851*m.b324
                          - 0.0176714586764426*m.b325 - 0.0314159265358979*m.b326 - 0.0490873852123405*m.b327
                          - 0.0706858347057703*m.b328 == 0)

m.c237 = Constraint(expr=   m.x121 - 0.00282743338823081*m.b329 - 0.00502654824574367*m.b330 - 0.0122718463030851*m.b331
                          - 0.0176714586764426*m.b332 - 0.0314159265358979*m.b333 - 0.0490873852123405*m.b334
                          - 0.0706858347057703*m.b335 == 0)

m.c238 = Constraint(expr=   m.x122 - 0.00282743338823081*m.b336 - 0.00502654824574367*m.b337 - 0.0122718463030851*m.b338
                          - 0.0176714586764426*m.b339 - 0.0314159265358979*m.b340 - 0.0490873852123405*m.b341
                          - 0.0706858347057703*m.b342 == 0)

m.c239 = Constraint(expr=   m.x123 - 0.00282743338823081*m.b343 - 0.00502654824574367*m.b344 - 0.0122718463030851*m.b345
                          - 0.0176714586764426*m.b346 - 0.0314159265358979*m.b347 - 0.0490873852123405*m.b348
                          - 0.0706858347057703*m.b349 == 0)

m.c240 = Constraint(expr=   m.x124 - 0.00282743338823081*m.b350 - 0.00502654824574367*m.b351 - 0.0122718463030851*m.b352
                          - 0.0176714586764426*m.b353 - 0.0314159265358979*m.b354 - 0.0490873852123405*m.b355
                          - 0.0706858347057703*m.b356 == 0)

m.c241 = Constraint(expr=   m.x125 - 0.00282743338823081*m.b357 - 0.00502654824574367*m.b358 - 0.0122718463030851*m.b359
                          - 0.0176714586764426*m.b360 - 0.0314159265358979*m.b361 - 0.0490873852123405*m.b362
                          - 0.0706858347057703*m.b363 == 0)

m.c242 = Constraint(expr=   m.x126 - 0.00282743338823081*m.b364 - 0.00502654824574367*m.b365 - 0.0122718463030851*m.b366
                          - 0.0176714586764426*m.b367 - 0.0314159265358979*m.b368 - 0.0490873852123405*m.b369
                          - 0.0706858347057703*m.b370 == 0)

m.c243 = Constraint(expr=   m.x127 - 0.00282743338823081*m.b371 - 0.00502654824574367*m.b372 - 0.0122718463030851*m.b373
                          - 0.0176714586764426*m.b374 - 0.0314159265358979*m.b375 - 0.0490873852123405*m.b376
                          - 0.0706858347057703*m.b377 == 0)

m.c244 = Constraint(expr=   m.x128 - 0.00282743338823081*m.b378 - 0.00502654824574367*m.b379 - 0.0122718463030851*m.b380
                          - 0.0176714586764426*m.b381 - 0.0314159265358979*m.b382 - 0.0490873852123405*m.b383
                          - 0.0706858347057703*m.b384 == 0)

m.c245 = Constraint(expr=   m.x129 - 0.00282743338823081*m.b385 - 0.00502654824574367*m.b386 - 0.0122718463030851*m.b387
                          - 0.0176714586764426*m.b388 - 0.0314159265358979*m.b389 - 0.0490873852123405*m.b390
                          - 0.0706858347057703*m.b391 == 0)

m.c246 = Constraint(expr=   m.x130 - 0.00282743338823081*m.b392 - 0.00502654824574367*m.b393 - 0.0122718463030851*m.b394
                          - 0.0176714586764426*m.b395 - 0.0314159265358979*m.b396 - 0.0490873852123405*m.b397
                          - 0.0706858347057703*m.b398 == 0)

m.c247 = Constraint(expr=   m.x131 - 0.00282743338823081*m.b399 - 0.00502654824574367*m.b400 - 0.0122718463030851*m.b401
                          - 0.0176714586764426*m.b402 - 0.0314159265358979*m.b403 - 0.0490873852123405*m.b404
                          - 0.0706858347057703*m.b405 == 0)

m.c248 = Constraint(expr=   m.x132 - 0.00282743338823081*m.b406 - 0.00502654824574367*m.b407 - 0.0122718463030851*m.b408
                          - 0.0176714586764426*m.b409 - 0.0314159265358979*m.b410 - 0.0490873852123405*m.b411
                          - 0.0706858347057703*m.b412 == 0)

m.c249 = Constraint(expr=   m.x133 - 0.00282743338823081*m.b413 - 0.00502654824574367*m.b414 - 0.0122718463030851*m.b415
                          - 0.0176714586764426*m.b416 - 0.0314159265358979*m.b417 - 0.0490873852123405*m.b418
                          - 0.0706858347057703*m.b419 == 0)

m.c250 = Constraint(expr=   m.x134 - 0.00282743338823081*m.b420 - 0.00502654824574367*m.b421 - 0.0122718463030851*m.b422
                          - 0.0176714586764426*m.b423 - 0.0314159265358979*m.b424 - 0.0490873852123405*m.b425
                          - 0.0706858347057703*m.b426 == 0)

m.c251 = Constraint(expr=   m.x135 - 0.00282743338823081*m.b427 - 0.00502654824574367*m.b428 - 0.0122718463030851*m.b429
                          - 0.0176714586764426*m.b430 - 0.0314159265358979*m.b431 - 0.0490873852123405*m.b432
                          - 0.0706858347057703*m.b433 == 0)

m.c252 = Constraint(expr=   m.x136 - 0.00282743338823081*m.b434 - 0.00502654824574367*m.b435 - 0.0122718463030851*m.b436
                          - 0.0176714586764426*m.b437 - 0.0314159265358979*m.b438 - 0.0490873852123405*m.b439
                          - 0.0706858347057703*m.b440 == 0)

m.c253 = Constraint(expr=   m.x137 - 0.00282743338823081*m.b441 - 0.00502654824574367*m.b442 - 0.0122718463030851*m.b443
                          - 0.0176714586764426*m.b444 - 0.0314159265358979*m.b445 - 0.0490873852123405*m.b446
                          - 0.0706858347057703*m.b447 == 0)

m.c254 = Constraint(expr=   m.x138 - 0.00282743338823081*m.b448 - 0.00502654824574367*m.b449 - 0.0122718463030851*m.b450
                          - 0.0176714586764426*m.b451 - 0.0314159265358979*m.b452 - 0.0490873852123405*m.b453
                          - 0.0706858347057703*m.b454 == 0)

m.c255 = Constraint(expr=   m.x139 - 0.00282743338823081*m.b455 - 0.00502654824574367*m.b456 - 0.0122718463030851*m.b457
                          - 0.0176714586764426*m.b458 - 0.0314159265358979*m.b459 - 0.0490873852123405*m.b460
                          - 0.0706858347057703*m.b461 == 0)

m.c256 = Constraint(expr=   m.x140 - 0.00282743338823081*m.b462 - 0.00502654824574367*m.b463 - 0.0122718463030851*m.b464
                          - 0.0176714586764426*m.b465 - 0.0314159265358979*m.b466 - 0.0490873852123405*m.b467
                          - 0.0706858347057703*m.b468 == 0)

m.c257 = Constraint(expr=   m.x141 - 0.00282743338823081*m.b469 - 0.00502654824574367*m.b470 - 0.0122718463030851*m.b471
                          - 0.0176714586764426*m.b472 - 0.0314159265358979*m.b473 - 0.0490873852123405*m.b474
                          - 0.0706858347057703*m.b475 == 0)

m.c258 = Constraint(expr=   m.x142 - 0.00282743338823081*m.b476 - 0.00502654824574367*m.b477 - 0.0122718463030851*m.b478
                          - 0.0176714586764426*m.b479 - 0.0314159265358979*m.b480 - 0.0490873852123405*m.b481
                          - 0.0706858347057703*m.b482 == 0)

m.c259 = Constraint(expr=   m.x143 - 0.00282743338823081*m.b483 - 0.00502654824574367*m.b484 - 0.0122718463030851*m.b485
                          - 0.0176714586764426*m.b486 - 0.0314159265358979*m.b487 - 0.0490873852123405*m.b488
                          - 0.0706858347057703*m.b489 == 0)

m.c260 = Constraint(expr=   m.x144 - 0.00282743338823081*m.b490 - 0.00502654824574367*m.b491 - 0.0122718463030851*m.b492
                          - 0.0176714586764426*m.b493 - 0.0314159265358979*m.b494 - 0.0490873852123405*m.b495
                          - 0.0706858347057703*m.b496 == 0)

m.c261 = Constraint(expr=   m.x145 - 0.00282743338823081*m.b497 - 0.00502654824574367*m.b498 - 0.0122718463030851*m.b499
                          - 0.0176714586764426*m.b500 - 0.0314159265358979*m.b501 - 0.0490873852123405*m.b502
                          - 0.0706858347057703*m.b503 == 0)

m.c262 = Constraint(expr=   m.x146 - 0.00282743338823081*m.b504 - 0.00502654824574367*m.b505 - 0.0122718463030851*m.b506
                          - 0.0176714586764426*m.b507 - 0.0314159265358979*m.b508 - 0.0490873852123405*m.b509
                          - 0.0706858347057703*m.b510 == 0)

m.c263 = Constraint(expr=   m.x147 - 0.00282743338823081*m.b511 - 0.00502654824574367*m.b512 - 0.0122718463030851*m.b513
                          - 0.0176714586764426*m.b514 - 0.0314159265358979*m.b515 - 0.0490873852123405*m.b516
                          - 0.0706858347057703*m.b517 == 0)

m.c264 = Constraint(expr=   m.x148 - 0.00282743338823081*m.b518 - 0.00502654824574367*m.b519 - 0.0122718463030851*m.b520
                          - 0.0176714586764426*m.b521 - 0.0314159265358979*m.b522 - 0.0490873852123405*m.b523
                          - 0.0706858347057703*m.b524 == 0)

m.c265 = Constraint(expr=   m.x149 - 0.00282743338823081*m.b525 - 0.00502654824574367*m.b526 - 0.0122718463030851*m.b527
                          - 0.0176714586764426*m.b528 - 0.0314159265358979*m.b529 - 0.0490873852123405*m.b530
                          - 0.0706858347057703*m.b531 == 0)

m.c266 = Constraint(expr=   m.x150 - 0.00282743338823081*m.b532 - 0.00502654824574367*m.b533 - 0.0122718463030851*m.b534
                          - 0.0176714586764426*m.b535 - 0.0314159265358979*m.b536 - 0.0490873852123405*m.b537
                          - 0.0706858347057703*m.b538 == 0)

m.c267 = Constraint(expr=   m.x151 - 0.00282743338823081*m.b539 - 0.00502654824574367*m.b540 - 0.0122718463030851*m.b541
                          - 0.0176714586764426*m.b542 - 0.0314159265358979*m.b543 - 0.0490873852123405*m.b544
                          - 0.0706858347057703*m.b545 == 0)

m.c268 = Constraint(expr=   m.x152 - 0.00282743338823081*m.b546 - 0.00502654824574367*m.b547 - 0.0122718463030851*m.b548
                          - 0.0176714586764426*m.b549 - 0.0314159265358979*m.b550 - 0.0490873852123405*m.b551
                          - 0.0706858347057703*m.b552 == 0)

m.c269 = Constraint(expr=   m.x153 - 0.00282743338823081*m.b553 - 0.00502654824574367*m.b554 - 0.0122718463030851*m.b555
                          - 0.0176714586764426*m.b556 - 0.0314159265358979*m.b557 - 0.0490873852123405*m.b558
                          - 0.0706858347057703*m.b559 == 0)

m.c270 = Constraint(expr=   m.b154 + m.b155 + m.b156 + m.b157 + m.b158 + m.b159 + m.b160 == 1)

m.c271 = Constraint(expr=   m.b161 + m.b162 + m.b163 + m.b164 + m.b165 + m.b166 + m.b167 == 1)

m.c272 = Constraint(expr=   m.b168 + m.b169 + m.b170 + m.b171 + m.b172 + m.b173 + m.b174 == 1)

m.c273 = Constraint(expr=   m.b175 + m.b176 + m.b177 + m.b178 + m.b179 + m.b180 + m.b181 == 1)

m.c274 = Constraint(expr=   m.b182 + m.b183 + m.b184 + m.b185 + m.b186 + m.b187 + m.b188 == 1)

m.c275 = Constraint(expr=   m.b189 + m.b190 + m.b191 + m.b192 + m.b193 + m.b194 + m.b195 == 1)

m.c276 = Constraint(expr=   m.b196 + m.b197 + m.b198 + m.b199 + m.b200 + m.b201 + m.b202 == 1)

m.c277 = Constraint(expr=   m.b203 + m.b204 + m.b205 + m.b206 + m.b207 + m.b208 + m.b209 == 1)

m.c278 = Constraint(expr=   m.b210 + m.b211 + m.b212 + m.b213 + m.b214 + m.b215 + m.b216 == 1)

m.c279 = Constraint(expr=   m.b217 + m.b218 + m.b219 + m.b220 + m.b221 + m.b222 + m.b223 == 1)

m.c280 = Constraint(expr=   m.b224 + m.b225 + m.b226 + m.b227 + m.b228 + m.b229 + m.b230 == 1)

m.c281 = Constraint(expr=   m.b231 + m.b232 + m.b233 + m.b234 + m.b235 + m.b236 + m.b237 == 1)

m.c282 = Constraint(expr=   m.b238 + m.b239 + m.b240 + m.b241 + m.b242 + m.b243 + m.b244 == 1)

m.c283 = Constraint(expr=   m.b245 + m.b246 + m.b247 + m.b248 + m.b249 + m.b250 + m.b251 == 1)

m.c284 = Constraint(expr=   m.b252 + m.b253 + m.b254 + m.b255 + m.b256 + m.b257 + m.b258 == 1)

m.c285 = Constraint(expr=   m.b259 + m.b260 + m.b261 + m.b262 + m.b263 + m.b264 + m.b265 == 1)

m.c286 = Constraint(expr=   m.b266 + m.b267 + m.b268 + m.b269 + m.b270 + m.b271 + m.b272 == 1)

m.c287 = Constraint(expr=   m.b273 + m.b274 + m.b275 + m.b276 + m.b277 + m.b278 + m.b279 == 1)

m.c288 = Constraint(expr=   m.b280 + m.b281 + m.b282 + m.b283 + m.b284 + m.b285 + m.b286 == 1)

m.c289 = Constraint(expr=   m.b287 + m.b288 + m.b289 + m.b290 + m.b291 + m.b292 + m.b293 == 1)

m.c290 = Constraint(expr=   m.b294 + m.b295 + m.b296 + m.b297 + m.b298 + m.b299 + m.b300 == 1)

m.c291 = Constraint(expr=   m.b301 + m.b302 + m.b303 + m.b304 + m.b305 + m.b306 + m.b307 == 1)

m.c292 = Constraint(expr=   m.b308 + m.b309 + m.b310 + m.b311 + m.b312 + m.b313 + m.b314 == 1)

m.c293 = Constraint(expr=   m.b315 + m.b316 + m.b317 + m.b318 + m.b319 + m.b320 + m.b321 == 1)

m.c294 = Constraint(expr=   m.b322 + m.b323 + m.b324 + m.b325 + m.b326 + m.b327 + m.b328 == 1)

m.c295 = Constraint(expr=   m.b329 + m.b330 + m.b331 + m.b332 + m.b333 + m.b334 + m.b335 == 1)

m.c296 = Constraint(expr=   m.b336 + m.b337 + m.b338 + m.b339 + m.b340 + m.b341 + m.b342 == 1)

m.c297 = Constraint(expr=   m.b343 + m.b344 + m.b345 + m.b346 + m.b347 + m.b348 + m.b349 == 1)

m.c298 = Constraint(expr=   m.b350 + m.b351 + m.b352 + m.b353 + m.b354 + m.b355 + m.b356 == 1)

m.c299 = Constraint(expr=   m.b357 + m.b358 + m.b359 + m.b360 + m.b361 + m.b362 + m.b363 == 1)

m.c300 = Constraint(expr=   m.b364 + m.b365 + m.b366 + m.b367 + m.b368 + m.b369 + m.b370 == 1)

m.c301 = Constraint(expr=   m.b371 + m.b372 + m.b373 + m.b374 + m.b375 + m.b376 + m.b377 == 1)

m.c302 = Constraint(expr=   m.b378 + m.b379 + m.b380 + m.b381 + m.b382 + m.b383 + m.b384 == 1)

m.c303 = Constraint(expr=   m.b385 + m.b386 + m.b387 + m.b388 + m.b389 + m.b390 + m.b391 == 1)

m.c304 = Constraint(expr=   m.b392 + m.b393 + m.b394 + m.b395 + m.b396 + m.b397 + m.b398 == 1)

m.c305 = Constraint(expr=   m.b399 + m.b400 + m.b401 + m.b402 + m.b403 + m.b404 + m.b405 == 1)

m.c306 = Constraint(expr=   m.b406 + m.b407 + m.b408 + m.b409 + m.b410 + m.b411 + m.b412 == 1)

m.c307 = Constraint(expr=   m.b413 + m.b414 + m.b415 + m.b416 + m.b417 + m.b418 + m.b419 == 1)

m.c308 = Constraint(expr=   m.b420 + m.b421 + m.b422 + m.b423 + m.b424 + m.b425 + m.b426 == 1)

m.c309 = Constraint(expr=   m.b427 + m.b428 + m.b429 + m.b430 + m.b431 + m.b432 + m.b433 == 1)

m.c310 = Constraint(expr=   m.b434 + m.b435 + m.b436 + m.b437 + m.b438 + m.b439 + m.b440 == 1)

m.c311 = Constraint(expr=   m.b441 + m.b442 + m.b443 + m.b444 + m.b445 + m.b446 + m.b447 == 1)

m.c312 = Constraint(expr=   m.b448 + m.b449 + m.b450 + m.b451 + m.b452 + m.b453 + m.b454 == 1)

m.c313 = Constraint(expr=   m.b455 + m.b456 + m.b457 + m.b458 + m.b459 + m.b460 + m.b461 == 1)

m.c314 = Constraint(expr=   m.b462 + m.b463 + m.b464 + m.b465 + m.b466 + m.b467 + m.b468 == 1)

m.c315 = Constraint(expr=   m.b469 + m.b470 + m.b471 + m.b472 + m.b473 + m.b474 + m.b475 == 1)

m.c316 = Constraint(expr=   m.b476 + m.b477 + m.b478 + m.b479 + m.b480 + m.b481 + m.b482 == 1)

m.c317 = Constraint(expr=   m.b483 + m.b484 + m.b485 + m.b486 + m.b487 + m.b488 + m.b489 == 1)

m.c318 = Constraint(expr=   m.b490 + m.b491 + m.b492 + m.b493 + m.b494 + m.b495 + m.b496 == 1)

m.c319 = Constraint(expr=   m.b497 + m.b498 + m.b499 + m.b500 + m.b501 + m.b502 + m.b503 == 1)

m.c320 = Constraint(expr=   m.b504 + m.b505 + m.b506 + m.b507 + m.b508 + m.b509 + m.b510 == 1)

m.c321 = Constraint(expr=   m.b511 + m.b512 + m.b513 + m.b514 + m.b515 + m.b516 + m.b517 == 1)

m.c322 = Constraint(expr=   m.b518 + m.b519 + m.b520 + m.b521 + m.b522 + m.b523 + m.b524 == 1)

m.c323 = Constraint(expr=   m.b525 + m.b526 + m.b527 + m.b528 + m.b529 + m.b530 + m.b531 == 1)

m.c324 = Constraint(expr=   m.b532 + m.b533 + m.b534 + m.b535 + m.b536 + m.b537 + m.b538 == 1)

m.c325 = Constraint(expr=   m.b539 + m.b540 + m.b541 + m.b542 + m.b543 + m.b544 + m.b545 == 1)

m.c326 = Constraint(expr=   m.b546 + m.b547 + m.b548 + m.b549 + m.b550 + m.b551 + m.b552 == 1)

m.c327 = Constraint(expr=   m.b553 + m.b554 + m.b555 + m.b556 + m.b557 + m.b558 + m.b559 == 1)
