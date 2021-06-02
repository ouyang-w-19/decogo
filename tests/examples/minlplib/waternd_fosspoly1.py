#  MINLP written by GAMS Convert at 04/21/18 13:55:14
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        327      211       58       58        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#       1430      154     1276        0        0        0        0        0
#  FX      1        1        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       4466     4234      232        0
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
m.x96 = Var(within=Reals,bounds=(0.000201061929829747,0.131510712726747),initialize=0.000201061929829747)
m.x97 = Var(within=Reals,bounds=(0.000201061929829747,0.131510712726747),initialize=0.000201061929829747)
m.x98 = Var(within=Reals,bounds=(0.000201061929829747,0.131510712726747),initialize=0.000201061929829747)
m.x99 = Var(within=Reals,bounds=(0.000201061929829747,0.131510712726747),initialize=0.000201061929829747)
m.x100 = Var(within=Reals,bounds=(0.000201061929829747,0.131510712726747),initialize=0.000201061929829747)
m.x101 = Var(within=Reals,bounds=(0.000201061929829747,0.131510712726747),initialize=0.000201061929829747)
m.x102 = Var(within=Reals,bounds=(0.000201061929829747,0.131510712726747),initialize=0.000201061929829747)
m.x103 = Var(within=Reals,bounds=(0.000201061929829747,0.131510712726747),initialize=0.000201061929829747)
m.x104 = Var(within=Reals,bounds=(0.000201061929829747,0.131510712726747),initialize=0.000201061929829747)
m.x105 = Var(within=Reals,bounds=(0.000201061929829747,0.131510712726747),initialize=0.000201061929829747)
m.x106 = Var(within=Reals,bounds=(0.000201061929829747,0.131510712726747),initialize=0.000201061929829747)
m.x107 = Var(within=Reals,bounds=(0.000201061929829747,0.131510712726747),initialize=0.000201061929829747)
m.x108 = Var(within=Reals,bounds=(0.000201061929829747,0.131510712726747),initialize=0.000201061929829747)
m.x109 = Var(within=Reals,bounds=(0.000201061929829747,0.131510712726747),initialize=0.000201061929829747)
m.x110 = Var(within=Reals,bounds=(0.000201061929829747,0.131510712726747),initialize=0.000201061929829747)
m.x111 = Var(within=Reals,bounds=(0.000201061929829747,0.131510712726747),initialize=0.000201061929829747)
m.x112 = Var(within=Reals,bounds=(0.000201061929829747,0.131510712726747),initialize=0.000201061929829747)
m.x113 = Var(within=Reals,bounds=(0.000201061929829747,0.131510712726747),initialize=0.000201061929829747)
m.x114 = Var(within=Reals,bounds=(0.000201061929829747,0.131510712726747),initialize=0.000201061929829747)
m.x115 = Var(within=Reals,bounds=(0.000201061929829747,0.131510712726747),initialize=0.000201061929829747)
m.x116 = Var(within=Reals,bounds=(0.000201061929829747,0.131510712726747),initialize=0.000201061929829747)
m.x117 = Var(within=Reals,bounds=(0.000201061929829747,0.131510712726747),initialize=0.000201061929829747)
m.x118 = Var(within=Reals,bounds=(0.000201061929829747,0.131510712726747),initialize=0.000201061929829747)
m.x119 = Var(within=Reals,bounds=(0.000201061929829747,0.131510712726747),initialize=0.000201061929829747)
m.x120 = Var(within=Reals,bounds=(0.000201061929829747,0.131510712726747),initialize=0.000201061929829747)
m.x121 = Var(within=Reals,bounds=(0.000201061929829747,0.131510712726747),initialize=0.000201061929829747)
m.x122 = Var(within=Reals,bounds=(0.000201061929829747,0.131510712726747),initialize=0.000201061929829747)
m.x123 = Var(within=Reals,bounds=(0.000201061929829747,0.131510712726747),initialize=0.000201061929829747)
m.x124 = Var(within=Reals,bounds=(0.000201061929829747,0.131510712726747),initialize=0.000201061929829747)
m.x125 = Var(within=Reals,bounds=(0.000201061929829747,0.131510712726747),initialize=0.000201061929829747)
m.x126 = Var(within=Reals,bounds=(0.000201061929829747,0.131510712726747),initialize=0.000201061929829747)
m.x127 = Var(within=Reals,bounds=(0.000201061929829747,0.131510712726747),initialize=0.000201061929829747)
m.x128 = Var(within=Reals,bounds=(0.000201061929829747,0.131510712726747),initialize=0.000201061929829747)
m.x129 = Var(within=Reals,bounds=(0.000201061929829747,0.131510712726747),initialize=0.000201061929829747)
m.x130 = Var(within=Reals,bounds=(0.000201061929829747,0.131510712726747),initialize=0.000201061929829747)
m.x131 = Var(within=Reals,bounds=(0.000201061929829747,0.131510712726747),initialize=0.000201061929829747)
m.x132 = Var(within=Reals,bounds=(0.000201061929829747,0.131510712726747),initialize=0.000201061929829747)
m.x133 = Var(within=Reals,bounds=(0.000201061929829747,0.131510712726747),initialize=0.000201061929829747)
m.x134 = Var(within=Reals,bounds=(0.000201061929829747,0.131510712726747),initialize=0.000201061929829747)
m.x135 = Var(within=Reals,bounds=(0.000201061929829747,0.131510712726747),initialize=0.000201061929829747)
m.x136 = Var(within=Reals,bounds=(0.000201061929829747,0.131510712726747),initialize=0.000201061929829747)
m.x137 = Var(within=Reals,bounds=(0.000201061929829747,0.131510712726747),initialize=0.000201061929829747)
m.x138 = Var(within=Reals,bounds=(0.000201061929829747,0.131510712726747),initialize=0.000201061929829747)
m.x139 = Var(within=Reals,bounds=(0.000201061929829747,0.131510712726747),initialize=0.000201061929829747)
m.x140 = Var(within=Reals,bounds=(0.000201061929829747,0.131510712726747),initialize=0.000201061929829747)
m.x141 = Var(within=Reals,bounds=(0.000201061929829747,0.131510712726747),initialize=0.000201061929829747)
m.x142 = Var(within=Reals,bounds=(0.000201061929829747,0.131510712726747),initialize=0.000201061929829747)
m.x143 = Var(within=Reals,bounds=(0.000201061929829747,0.131510712726747),initialize=0.000201061929829747)
m.x144 = Var(within=Reals,bounds=(0.000201061929829747,0.131510712726747),initialize=0.000201061929829747)
m.x145 = Var(within=Reals,bounds=(0.000201061929829747,0.131510712726747),initialize=0.000201061929829747)
m.x146 = Var(within=Reals,bounds=(0.000201061929829747,0.131510712726747),initialize=0.000201061929829747)
m.x147 = Var(within=Reals,bounds=(0.000201061929829747,0.131510712726747),initialize=0.000201061929829747)
m.x148 = Var(within=Reals,bounds=(0.000201061929829747,0.131510712726747),initialize=0.000201061929829747)
m.x149 = Var(within=Reals,bounds=(0.000201061929829747,0.131510712726747),initialize=0.000201061929829747)
m.x150 = Var(within=Reals,bounds=(0.000201061929829747,0.131510712726747),initialize=0.000201061929829747)
m.x151 = Var(within=Reals,bounds=(0.000201061929829747,0.131510712726747),initialize=0.000201061929829747)
m.x152 = Var(within=Reals,bounds=(0.000201061929829747,0.131510712726747),initialize=0.000201061929829747)
m.x153 = Var(within=Reals,bounds=(0.000201061929829747,0.131510712726747),initialize=0.000201061929829747)
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
m.b908 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b909 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b910 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b911 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b912 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b913 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b914 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b915 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b916 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b917 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b918 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b919 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b920 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b921 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b922 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b923 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b924 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b925 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b926 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b927 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b928 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b929 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b930 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b931 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b932 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b933 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b934 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b935 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b936 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b937 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b938 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b939 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b940 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b941 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b942 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b943 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b944 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b945 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b946 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b947 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b948 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b949 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b950 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b951 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b952 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b953 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b954 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b955 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b956 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b957 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b958 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b959 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b960 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b961 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b962 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b963 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b964 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b965 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b966 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b967 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b968 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b969 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b970 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b971 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b972 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b973 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b974 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b975 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b976 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b977 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b978 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b979 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b980 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b981 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b982 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b983 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b984 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b985 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b986 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b987 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b988 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b989 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b990 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b991 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b992 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b993 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b994 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b995 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b996 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b997 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b998 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b999 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1000 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1001 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1002 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1003 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1004 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1005 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1006 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1007 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1008 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1009 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1010 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1011 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1012 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1013 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1014 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1015 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1016 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1017 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1018 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1019 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1020 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1021 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1022 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1023 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1024 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1025 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1026 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1027 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1028 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1029 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1030 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1031 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1032 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1033 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1034 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1035 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1036 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1037 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1038 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1039 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1040 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1041 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1042 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1043 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1044 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1045 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1046 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1047 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1048 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1049 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1050 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1051 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1052 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1053 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1054 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1055 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1056 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1057 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1058 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1059 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1060 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1061 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1062 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1063 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1064 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1065 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1066 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1067 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1068 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1069 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1070 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1071 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1072 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1073 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1074 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1075 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1076 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1077 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1078 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1079 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1080 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1081 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1082 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1083 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1084 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1085 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1086 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1087 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1088 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1089 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1090 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1091 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1092 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1093 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1094 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1095 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1096 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1097 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1098 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1099 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1100 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1101 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1102 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1103 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1104 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1105 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1106 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1107 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1108 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1109 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1110 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1111 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1112 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1113 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1114 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1115 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1116 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1117 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1118 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1119 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1120 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1121 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1122 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1123 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1124 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1125 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1126 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1127 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1128 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1129 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1130 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1131 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1132 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1133 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1134 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1135 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1136 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1137 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1138 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1139 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1140 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1141 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1142 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1143 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1144 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1145 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1146 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1147 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1148 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1149 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1150 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1151 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1152 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1153 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1154 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1155 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1156 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1157 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1158 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1159 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1160 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1161 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1162 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1163 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1164 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1165 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1166 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1167 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1168 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1169 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1170 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1171 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1172 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1173 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1174 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1175 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1176 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1177 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1178 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1179 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1180 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1181 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1182 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1183 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1184 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1185 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1186 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1187 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1188 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1189 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1190 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1191 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1192 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1193 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1194 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1195 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1196 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1197 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1198 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1199 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1200 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1201 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1202 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1203 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1204 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1205 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1206 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1207 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1208 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1209 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1210 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1211 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1212 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1213 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1214 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1215 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1216 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1217 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1218 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1219 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1220 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1221 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1222 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1223 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1224 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1225 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1226 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1227 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1228 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1229 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1230 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1231 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1232 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1233 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1234 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1235 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1236 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1237 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1238 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1239 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1240 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1241 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1242 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1243 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1244 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1245 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1246 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1247 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1248 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1249 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1250 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1251 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1252 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1253 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1254 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1255 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1256 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1257 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1258 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1259 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1260 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1261 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1262 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1263 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1264 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1265 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1266 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1267 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1268 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1269 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1270 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1271 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1272 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1273 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1274 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1275 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1276 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1277 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1278 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1279 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1280 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1281 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1282 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1283 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1284 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1285 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1286 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1287 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1288 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1289 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1290 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1291 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1292 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1293 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1294 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1295 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1296 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1297 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1298 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1299 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1300 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1301 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1302 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1303 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1304 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1305 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1306 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1307 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1308 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1309 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1310 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1311 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1312 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1313 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1314 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1315 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1316 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1317 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1318 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1319 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1320 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1321 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1322 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1323 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1324 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1325 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1326 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1327 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1328 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1329 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1330 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1331 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1332 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1333 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1334 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1335 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1336 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1337 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1338 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1339 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1340 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1341 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1342 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1343 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1344 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1345 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1346 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1347 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1348 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1349 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1350 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1351 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1352 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1353 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1354 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1355 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1356 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1357 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1358 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1359 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1360 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1361 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1362 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1363 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1364 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1365 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1366 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1367 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1368 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1369 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1370 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1371 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1372 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1373 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1374 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1375 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1376 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1377 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1378 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1379 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1380 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1381 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1382 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1383 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1384 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1385 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1386 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1387 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1388 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1389 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1390 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1391 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1392 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1393 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1394 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1395 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1396 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1397 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1398 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1399 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1400 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1401 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1402 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1403 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1404 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1405 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1406 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1407 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1408 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1409 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1410 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1411 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1412 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1413 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1414 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1415 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1416 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1417 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1418 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1419 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1420 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1421 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1422 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1423 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1424 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1425 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1426 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1427 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1428 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1429 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=   50.4488*m.b154 + 74.3456*m.b155 + 116.8288*m.b156 + 179.226*m.b157 + 268.1752*m.b158
                        + 426.1596*m.b159 + 589.4544*m.b160 + 856.302*m.b161 + 1273.1684*m.b162 + 1590.4648*m.b163
                        + 1982.1068*m.b164 + 2603.4236*m.b165 + 3289.7928*m.b166 + 4055.818*m.b167 + 5139.1396*m.b168
                        + 6323.3588*m.b169 + 7925.772*m.b170 + 10037.9836*m.b171 + 13220.2408*m.b172 + 16791.4848*m.b173
                        + 21280.1004*m.b174 + 26247.9796*m.b175 + 28.6558*m.b176 + 42.2296*m.b177 + 66.3608*m.b178
                        + 101.8035*m.b179 + 152.3282*m.b180 + 242.0661*m.b181 + 334.8204*m.b182 + 486.3945*m.b183
                        + 723.1819*m.b184 + 903.4118*m.b185 + 1125.8713*m.b186 + 1478.7901*m.b187 + 1868.6598*m.b188
                        + 2303.7755*m.b189 + 2919.1211*m.b190 + 3591.7783*m.b191 + 4501.977*m.b192 + 5701.7501*m.b193
                        + 7509.3278*m.b194 + 9537.8568*m.b195 + 12087.4689*m.b196 + 14909.3111*m.b197 + 45.5012*m.b198
                        + 67.0544*m.b199 + 105.3712*m.b200 + 161.649*m.b201 + 241.8748*m.b202 + 384.3654*m.b203
                        + 531.6456*m.b204 + 772.323*m.b205 + 1148.3066*m.b206 + 1434.4852*m.b207 + 1787.7182*m.b208
                        + 2348.1014*m.b209 + 2967.1572*m.b210 + 3658.057*m.b211 + 4635.1354*m.b212 + 5703.2162*m.b213
                        + 7148.478*m.b214 + 9053.5414*m.b215 + 11923.7092*m.b216 + 15144.7152*m.b217 + 19193.1246*m.b218
                        + 23673.7954*m.b219 + 61.9286*m.b220 + 91.2632*m.b221 + 143.4136*m.b222 + 220.0095*m.b223
                        + 329.1994*m.b224 + 523.1337*m.b225 + 723.5868*m.b226 + 1051.1565*m.b227 + 1562.8823*m.b228
                        + 1952.3806*m.b229 + 2433.1421*m.b230 + 3195.8417*m.b231 + 4038.3966*m.b232 + 4978.7335*m.b233
                        + 6308.5687*m.b234 + 7762.2611*m.b235 + 9729.309*m.b236 + 12322.1617*m.b237 + 16228.5526*m.b238
                        + 20612.4456*m.b239 + 26122.4613*m.b240 + 32220.7987*m.b241 + 118.8336*m.b242 + 175.1232*m.b243
                        + 275.1936*m.b244 + 422.172*m.b245 + 631.6944*m.b246 + 1003.8312*m.b247 + 1388.4768*m.b248
                        + 2017.044*m.b249 + 2998.9848*m.b250 + 3746.3856*m.b251 + 4668.9096*m.b252 + 6132.4392*m.b253
                        + 7749.2016*m.b254 + 9553.596*m.b255 + 12105.3912*m.b256 + 14894.8536*m.b257 + 18669.384*m.b258
                        + 23644.7592*m.b259 + 31140.6576*m.b260 + 39552.8256*m.b261 + 50125.8888*m.b262
                        + 61827.8712*m.b263 + 74.9816*m.b264 + 110.4992*m.b265 + 173.6416*m.b266 + 266.382*m.b267
                        + 398.5864*m.b268 + 633.3972*m.b269 + 876.1008*m.b270 + 1272.714*m.b271 + 1892.2988*m.b272
                        + 2363.8936*m.b273 + 2945.9876*m.b274 + 3869.4452*m.b275 + 4889.5896*m.b276 + 6028.126*m.b277
                        + 7638.2572*m.b278 + 9398.3516*m.b279 + 11780.004*m.b280 + 14919.3652*m.b281 + 19649.1256*m.b282
                        + 24957.0336*m.b283 + 31628.4228*m.b284 + 39012.1372*m.b285 + 109.8542*m.b286 + 161.8904*m.b287
                        + 254.3992*m.b288 + 390.2715*m.b289 + 583.9618*m.b290 + 927.9789*m.b291 + 1283.5596*m.b292
                        + 1864.6305*m.b293 + 2772.3731*m.b294 + 3463.2982*m.b295 + 4316.1137*m.b296 + 5669.0549*m.b297
                        + 7163.6502*m.b298 + 8831.6995*m.b299 + 11190.6739*m.b300 + 13769.3567*m.b301 + 17258.673*m.b302
                        + 21858.0949*m.b303 + 28787.5822*m.b304 + 36564.1032*m.b305 + 46338.2361*m.b306
                        + 57155.9839*m.b307 + 127.8054*m.b308 + 188.3448*m.b309 + 295.9704*m.b310 + 454.0455*m.b311
                        + 679.3866*m.b312 + 1079.6193*m.b313 + 1493.3052*m.b314 + 2169.3285*m.b315 + 3225.4047*m.b316
                        + 4029.2334*m.b317 + 5021.4069*m.b318 + 6595.4313*m.b319 + 8334.2574*m.b320 + 10274.8815*m.b321
                        + 13019.3343*m.b322 + 16019.3979*m.b323 + 20078.901*m.b324 + 25429.9113*m.b325
                        + 33491.7414*m.b326 + 42539.0184*m.b327 + 53910.3357*m.b328 + 66495.8043*m.b329 + 29.4082*m.b330
                        + 43.3384*m.b331 + 68.1032*m.b332 + 104.4765*m.b333 + 156.3278*m.b334 + 248.4219*m.b335
                        + 343.6116*m.b336 + 499.1655*m.b337 + 742.1701*m.b338 + 927.1322*m.b339 + 1155.4327*m.b340
                        + 1517.6179*m.b341 + 1917.7242*m.b342 + 2364.2645*m.b343 + 2995.7669*m.b344 + 3686.0857*m.b345
                        + 4620.183*m.b346 + 5851.4579*m.b347 + 7706.4962*m.b348 + 9788.2872*m.b349 + 12404.8431*m.b350
                        + 15300.7769*m.b351 + 51.6078*m.b352 + 76.0536*m.b353 + 119.5128*m.b354 + 183.3435*m.b355
                        + 274.3362*m.b356 + 435.9501*m.b357 + 602.9964*m.b358 + 875.9745*m.b359 + 1302.4179*m.b360
                        + 1627.0038*m.b361 + 2027.6433*m.b362 + 2663.2341*m.b363 + 3365.3718*m.b364 + 4148.9955*m.b365
                        + 5257.2051*m.b366 + 6468.6303*m.b367 + 8107.857*m.b368 + 10268.5941*m.b369 + 13523.9598*m.b370
                        + 17177.2488*m.b371 + 21768.9849*m.b372 + 26850.9951*m.b373 + 76.4788*m.b374 + 112.7056*m.b375
                        + 177.1088*m.b376 + 271.701*m.b377 + 406.5452*m.b378 + 646.0446*m.b379 + 893.5944*m.b380
                        + 1298.127*m.b381 + 1930.0834*m.b382 + 2411.0948*m.b383 + 3004.8118*m.b384 + 3946.7086*m.b385
                        + 4987.2228*m.b386 + 6148.493*m.b387 + 7790.7746*m.b388 + 9586.0138*m.b389 + 12015.222*m.b390
                        + 15217.2686*m.b391 + 20041.4708*m.b392 + 25455.3648*m.b393 + 32259.9654*m.b394
                        + 39791.1146*m.b395 + 54.9708*m.b396 + 81.0096*m.b397 + 127.3008*m.b398 + 195.291*m.b399
                        + 292.2132*m.b400 + 464.3586*m.b401 + 642.2904*m.b402 + 933.057*m.b403 + 1387.2894*m.b404
                        + 1733.0268*m.b405 + 2159.7738*m.b406 + 2836.7826*m.b407 + 3584.6748*m.b408 + 4419.363*m.b409
                        + 5599.7886*m.b410 + 6890.1558*m.b411 + 8636.202*m.b412 + 10937.7426*m.b413 + 14405.2428*m.b414
                        + 18296.5968*m.b415 + 23187.5514*m.b416 + 28600.7286*m.b417 + 42.6246*m.b418 + 62.8152*m.b419
                        + 98.7096*m.b420 + 151.4295*m.b421 + 226.5834*m.b422 + 360.0657*m.b423 + 498.0348*m.b424
                        + 723.4965*m.b425 + 1075.7103*m.b426 + 1343.7966*m.b427 + 1674.6981*m.b428 + 2199.6537*m.b429
                        + 2779.5726*m.b430 + 3426.7935*m.b431 + 4342.1007*m.b432 + 5342.6571*m.b433 + 6696.549*m.b434
                        + 8481.1737*m.b435 + 11169.8886*m.b436 + 14187.2616*m.b437 + 17979.7293*m.b438
                        + 22177.1307*m.b439 + 55.8448*m.b440 + 82.2976*m.b441 + 129.3248*m.b442 + 198.396*m.b443
                        + 296.8592*m.b444 + 471.7416*m.b445 + 652.5024*m.b446 + 947.892*m.b447 + 1409.3464*m.b448
                        + 1760.5808*m.b449 + 2194.1128*m.b450 + 2881.8856*m.b451 + 3641.6688*m.b452 + 4489.628*m.b453
                        + 5688.8216*m.b454 + 6999.7048*m.b455 + 8773.512*m.b456 + 11111.6456*m.b457 + 14634.2768*m.b458
                        + 18587.5008*m.b459 + 23556.2184*m.b460 + 29055.4616*m.b461 + 18.9316*m.b462 + 27.8992*m.b463
                        + 43.8416*m.b464 + 67.257*m.b465 + 100.6364*m.b466 + 159.9222*m.b467 + 221.2008*m.b468
                        + 321.339*m.b469 + 477.7738*m.b470 + 596.8436*m.b471 + 743.8126*m.b472 + 976.9702*m.b473
                        + 1234.5396*m.b474 + 1522.001*m.b475 + 1928.5322*m.b476 + 2372.9266*m.b477 + 2974.254*m.b478
                        + 3766.8902*m.b479 + 4961.0756*m.b480 + 6301.2336*m.b481 + 7985.6478*m.b482 + 9849.9122*m.b483
                        + 61.8222*m.b484 + 91.1064*m.b485 + 143.1672*m.b486 + 219.6315*m.b487 + 328.6338*m.b488
                        + 522.2349*m.b489 + 722.3436*m.b490 + 1049.3505*m.b491 + 1560.1971*m.b492 + 1949.0262*m.b493
                        + 2428.9617*m.b494 + 3190.3509*m.b495 + 4031.4582*m.b496 + 4970.1795*m.b497 + 6297.7299*m.b498
                        + 7748.9247*m.b499 + 9712.593*m.b500 + 12300.9909*m.b501 + 16200.6702*m.b502 + 20577.0312*m.b503
                        + 26077.5801*m.b504 + 32165.4399*m.b505 + 31.654*m.b506 + 46.648*m.b507 + 73.304*m.b508
                        + 112.455*m.b509 + 168.266*m.b510 + 267.393*m.b511 + 369.852*m.b512 + 537.285*m.b513
                        + 798.847*m.b514 + 997.934*m.b515 + 1243.669*m.b516 + 1633.513*m.b517 + 2064.174*m.b518
                        + 2544.815*m.b519 + 3224.543*m.b520 + 3967.579*m.b521 + 4973.01*m.b522 + 6298.313*m.b523
                        + 8295.014*m.b524 + 10535.784*m.b525 + 13352.157*m.b526 + 16469.243*m.b527 + 20.1324*m.b528
                        + 29.6688*m.b529 + 46.6224*m.b530 + 71.523*m.b531 + 107.0196*m.b532 + 170.0658*m.b533
                        + 235.2312*m.b534 + 341.721*m.b535 + 508.0782*m.b536 + 634.7004*m.b537 + 790.9914*m.b538
                        + 1038.9378*m.b539 + 1312.8444*m.b540 + 1618.539*m.b541 + 2050.8558*m.b542 + 2523.4374*m.b543
                        + 3162.906*m.b544 + 4005.8178*m.b545 + 5275.7484*m.b546 + 6700.9104*m.b547 + 8492.1642*m.b548
                        + 10474.6758*m.b549 + 77.4554*m.b550 + 114.1448*m.b551 + 179.3704*m.b552 + 275.1705*m.b553
                        + 411.7366*m.b554 + 654.2943*m.b555 + 905.0052*m.b556 + 1314.7035*m.b557 + 1954.7297*m.b558
                        + 2441.8834*m.b559 + 3043.1819*m.b560 + 3997.1063*m.b561 + 5050.9074*m.b562 + 6227.0065*m.b563
                        + 7890.2593*m.b564 + 9708.4229*m.b565 + 12168.651*m.b566 + 15411.5863*m.b567 + 20297.3914*m.b568
                        + 25780.4184*m.b569 + 32671.9107*m.b570 + 40299.2293*m.b571 + 42.7006*m.b572 + 62.9272*m.b573
                        + 98.8856*m.b574 + 151.6995*m.b575 + 226.9874*m.b576 + 360.7077*m.b577 + 498.9228*m.b578
                        + 724.7865*m.b579 + 1077.6283*m.b580 + 1346.1926*m.b581 + 1677.6841*m.b582 + 2203.5757*m.b583
                        + 2784.5286*m.b584 + 3432.9035*m.b585 + 4349.8427*m.b586 + 5352.1831*m.b587 + 6708.489*m.b588
                        + 8496.2957*m.b589 + 11189.8046*m.b590 + 14212.5576*m.b591 + 18011.7873*m.b592
                        + 22216.6727*m.b593 + 14.1892*m.b594 + 20.9104*m.b595 + 32.8592*m.b596 + 50.409*m.b597
                        + 75.4268*m.b598 + 119.8614*m.b599 + 165.7896*m.b600 + 240.843*m.b601 + 358.0906*m.b602
                        + 447.3332*m.b603 + 557.4862*m.b604 + 732.2374*m.b605 + 925.2852*m.b606 + 1140.737*m.b607
                        + 1445.4314*m.b608 + 1778.5042*m.b609 + 2229.198*m.b610 + 2823.2774*m.b611 + 3718.3172*m.b612
                        + 4722.7632*m.b613 + 5985.2286*m.b614 + 7382.4914*m.b615 + 24.7722*m.b616 + 36.5064*m.b617
                        + 57.3672*m.b618 + 88.0065*m.b619 + 131.6838*m.b620 + 209.2599*m.b621 + 289.4436*m.b622
                        + 420.4755*m.b623 + 625.1721*m.b624 + 780.9762*m.b625 + 973.2867*m.b626 + 1278.3759*m.b627
                        + 1615.4082*m.b628 + 1991.5545*m.b629 + 2523.5049*m.b630 + 3104.9997*m.b631 + 3891.843*m.b632
                        + 4929.0159*m.b633 + 6491.6202*m.b634 + 8245.2312*m.b635 + 10449.3051*m.b636 + 12888.7149*m.b637
                        + 69.4716*m.b638 + 102.3792*m.b639 + 160.8816*m.b640 + 246.807*m.b641 + 369.2964*m.b642
                        + 586.8522*m.b643 + 811.7208*m.b644 + 1179.189*m.b645 + 1753.2438*m.b646 + 2190.1836*m.b647
                        + 2729.5026*m.b648 + 3585.1002*m.b649 + 4530.2796*m.b650 + 5585.151*m.b651 + 7076.9622*m.b652
                        + 8707.7166*m.b653 + 10914.354*m.b654 + 13823.0202*m.b655 + 18205.2156*m.b656
                        + 23123.0736*m.b657 + 29304.2178*m.b658 + 36145.3422*m.b659 + 30.7116*m.b660 + 45.2592*m.b661
                        + 71.1216*m.b662 + 109.107*m.b663 + 163.2564*m.b664 + 259.4322*m.b665 + 358.8408*m.b666
                        + 521.289*m.b667 + 775.0638*m.b668 + 968.2236*m.b669 + 1206.6426*m.b670 + 1584.8802*m.b671
                        + 2002.7196*m.b672 + 2469.051*m.b673 + 3128.5422*m.b674 + 3849.4566*m.b675 + 4824.954*m.b676
                        + 6110.8002*m.b677 + 8048.0556*m.b678 + 10222.1136*m.b679 + 12954.6378*m.b680
                        + 15978.9222*m.b681 + 31.2702*m.b682 + 46.0824*m.b683 + 72.4152*m.b684 + 111.0915*m.b685
                        + 166.2258*m.b686 + 264.1509*m.b687 + 365.3676*m.b688 + 530.7705*m.b689 + 789.1611*m.b690
                        + 985.8342*m.b691 + 1228.5897*m.b692 + 1613.7069*m.b693 + 2039.1462*m.b694 + 2513.9595*m.b695
                        + 3185.4459*m.b696 + 3919.4727*m.b697 + 4912.713*m.b698 + 6221.9469*m.b699 + 8194.4382*m.b700
                        + 10408.0392*m.b701 + 13190.2641*m.b702 + 16269.5559*m.b703 + 51.6876*m.b704 + 76.1712*m.b705
                        + 119.6976*m.b706 + 183.627*m.b707 + 274.7604*m.b708 + 436.6242*m.b709 + 603.9288*m.b710
                        + 877.329*m.b711 + 1304.4318*m.b712 + 1629.5196*m.b713 + 2030.7786*m.b714 + 2667.3522*m.b715
                        + 3370.5756*m.b716 + 4155.411*m.b717 + 5265.3342*m.b718 + 6478.6326*m.b719 + 8120.394*m.b720
                        + 10284.4722*m.b721 + 13544.8716*m.b722 + 17203.8096*m.b723 + 21802.6458*m.b724
                        + 26892.5142*m.b725 + 142.3784*m.b726 + 209.8208*m.b727 + 329.7184*m.b728 + 505.818*m.b729
                        + 756.8536*m.b730 + 1202.7228*m.b731 + 1663.5792*m.b732 + 2416.686*m.b733 + 3593.1812*m.b734
                        + 4488.6664*m.b735 + 5593.9724*m.b736 + 7347.4748*m.b737 + 9284.5704*m.b738 + 11446.474*m.b739
                        + 14503.8628*m.b740 + 17846.0084*m.b741 + 22368.396*m.b742 + 28329.5548*m.b743
                        + 37310.6344*m.b744 + 47389.5264*m.b745 + 60057.4572*m.b746 + 74077.9828*m.b747 + 89.148*m.b748
                        + 131.376*m.b749 + 206.448*m.b750 + 316.71*m.b751 + 473.892*m.b752 + 753.066*m.b753
                        + 1041.624*m.b754 + 1513.17*m.b755 + 2249.814*m.b756 + 2810.508*m.b757 + 3502.578*m.b758
                        + 4600.506*m.b759 + 5813.388*m.b760 + 7167.03*m.b761 + 9081.366*m.b762 + 11173.998*m.b763
                        + 14005.62*m.b764 + 17738.106*m.b765 + 23361.468*m.b766 + 29672.208*m.b767 + 37604.034*m.b768
                        + 46382.766*m.b769 + 31.9048*m.b770 + 47.0176*m.b771 + 73.8848*m.b772 + 113.346*m.b773
                        + 169.5992*m.b774 + 269.5116*m.b775 + 372.7824*m.b776 + 541.542*m.b777 + 805.1764*m.b778
                        + 1005.8408*m.b779 + 1253.5228*m.b780 + 1646.4556*m.b781 + 2080.5288*m.b782 + 2564.978*m.b783
                        + 3250.0916*m.b784 + 3999.0148*m.b785 + 5012.412*m.b786 + 6348.2156*m.b787 + 8360.7368*m.b788
                        + 10619.2608*m.b789 + 13457.9484*m.b790 + 16599.7316*m.b791 + 37.8632*m.b792 + 55.7984*m.b793
                        + 87.6832*m.b794 + 134.514*m.b795 + 201.2728*m.b796 + 319.8444*m.b797 + 442.4016*m.b798
                        + 642.678*m.b799 + 955.5476*m.b800 + 1193.6872*m.b801 + 1487.6252*m.b802 + 1953.9404*m.b803
                        + 2469.0792*m.b804 + 3044.002*m.b805 + 3857.0644*m.b806 + 4745.8532*m.b807 + 5948.508*m.b808
                        + 7533.7804*m.b809 + 9922.1512*m.b810 + 12602.4672*m.b811 + 15971.2956*m.b812
                        + 19699.8244*m.b813 + 94.259*m.b814 + 138.908*m.b815 + 218.284*m.b816 + 334.8675*m.b817
                        + 501.061*m.b818 + 796.2405*m.b819 + 1101.342*m.b820 + 1599.9225*m.b821 + 2378.7995*m.b822
                        + 2971.639*m.b823 + 3703.3865*m.b824 + 4864.2605*m.b825 + 6146.679*m.b826 + 7577.9275*m.b827
                        + 9602.0155*m.b828 + 11814.6215*m.b829 + 14808.585*m.b830 + 18755.0605*m.b831 + 24700.819*m.b832
                        + 31373.364*m.b833 + 39759.9345*m.b834 + 49041.9655*m.b835 + 41.363*m.b836 + 60.956*m.b837
                        + 95.788*m.b838 + 146.9475*m.b839 + 219.877*m.b840 + 349.4085*m.b841 + 483.294*m.b842
                        + 702.0825*m.b843 + 1043.8715*m.b844 + 1304.023*m.b845 + 1625.1305*m.b846 + 2134.5485*m.b847
                        + 2697.303*m.b848 + 3325.3675*m.b849 + 4213.5835*m.b850 + 5184.5255*m.b851 + 6498.345*m.b852
                        + 8230.1485*m.b853 + 10839.283*m.b854 + 13767.348*m.b855 + 17447.5665*m.b856 + 21520.7335*m.b857
                        + 79.8342*m.b858 + 117.6504*m.b859 + 184.8792*m.b860 + 283.6215*m.b861 + 424.3818*m.b862
                        + 674.3889*m.b863 + 932.7996*m.b864 + 1355.0805*m.b865 + 2014.7631*m.b866 + 2516.8782*m.b867
                        + 3136.6437*m.b868 + 4119.8649*m.b869 + 5206.0302*m.b870 + 6418.2495*m.b871 + 8132.5839*m.b872
                        + 10006.5867*m.b873 + 12542.373*m.b874 + 15884.9049*m.b875 + 20920.7622*m.b876
                        + 26572.1832*m.b877 + 33675.3261*m.b878 + 41536.8939*m.b879 + 56.0766*m.b880 + 82.6392*m.b881
                        + 129.8616*m.b882 + 199.2195*m.b883 + 298.0914*m.b884 + 473.6997*m.b885 + 655.2108*m.b886
                        + 951.8265*m.b887 + 1415.1963*m.b888 + 1767.8886*m.b889 + 2203.2201*m.b890 + 2893.8477*m.b891
                        + 3656.7846*m.b892 + 4508.2635*m.b893 + 5712.4347*m.b894 + 7028.7591*m.b895 + 8809.929*m.b896
                        + 11157.7677*m.b897 + 14695.0206*m.b898 + 18664.6536*m.b899 + 23653.9953*m.b900
                        + 29176.0647*m.b901 + 129.5686*m.b902 + 190.9432*m.b903 + 300.0536*m.b904 + 460.3095*m.b905
                        + 688.7594*m.b906 + 1094.5137*m.b907 + 1513.9068*m.b908 + 2199.2565*m.b909 + 3269.9023*m.b910
                        + 4084.8206*m.b911 + 5090.6821*m.b912 + 6686.4217*m.b913 + 8449.2366*m.b914 + 10416.6335*m.b915
                        + 13198.9487*m.b916 + 16240.4011*m.b917 + 20355.909*m.b918 + 25780.7417*m.b919
                        + 33953.7926*m.b920 + 43125.8856*m.b921 + 54654.0813*m.b922 + 67413.1787*m.b923 + 39.444*m.b924
                        + 58.128*m.b925 + 91.344*m.b926 + 140.13*m.b927 + 209.676*m.b928 + 333.198*m.b929
                        + 460.872*m.b930 + 669.51*m.b931 + 995.442*m.b932 + 1243.524*m.b933 + 1549.734*m.b934
                        + 2035.518*m.b935 + 2572.164*m.b936 + 3171.09*m.b937 + 4018.098*m.b938 + 4943.994*m.b939
                        + 6196.86*m.b940 + 7848.318*m.b941 + 10336.404*m.b942 + 13128.624*m.b943 + 16638.102*m.b944
                        + 20522.298*m.b945 + 28.5304*m.b946 + 42.0448*m.b947 + 66.0704*m.b948 + 101.358*m.b949
                        + 151.6616*m.b950 + 241.0068*m.b951 + 333.3552*m.b952 + 484.266*m.b953 + 720.0172*m.b954
                        + 899.4584*m.b955 + 1120.9444*m.b956 + 1472.3188*m.b957 + 1860.4824*m.b958 + 2293.694*m.b959
                        + 2906.3468*m.b960 + 3576.0604*m.b961 + 4482.276*m.b962 + 5676.7988*m.b963 + 7476.4664*m.b964
                        + 9496.1184*m.b965 + 12034.5732*m.b966 + 14844.0668*m.b967 + 50.3614*m.b968 + 74.2168*m.b969
                        + 116.6264*m.b970 + 178.9155*m.b971 + 267.7106*m.b972 + 425.4213*m.b973 + 588.4332*m.b974
                        + 854.8185*m.b975 + 1270.9627*m.b976 + 1587.7094*m.b977 + 1978.6729*m.b978 + 2598.9133*m.b979
                        + 3284.0934*m.b980 + 4048.7915*m.b981 + 5130.2363*m.b982 + 6312.4039*m.b983 + 7912.041*m.b984
                        + 10020.5933*m.b985 + 13197.3374*m.b986 + 16762.3944*m.b987 + 21243.2337*m.b988
                        + 26202.5063*m.b989 + 80.161*m.b990 + 118.132*m.b991 + 185.636*m.b992 + 284.7825*m.b993
                        + 426.119*m.b994 + 677.1495*m.b995 + 936.618*m.b996 + 1360.6275*m.b997 + 2023.0105*m.b998
                        + 2527.181*m.b999 + 3149.4835*m.b1000 + 4136.7295*m.b1001 + 5227.341*m.b1002 + 6444.5225*m.b1003
                        + 8165.8745*m.b1004 + 10047.5485*m.b1005 + 12593.715*m.b1006 + 15949.9295*m.b1007
                        + 21006.401*m.b1008 + 26680.956*m.b1009 + 33813.1755*m.b1010 + 41706.9245*m.b1011
                        + 56.0462*m.b1012 + 82.5944*m.b1013 + 129.7912*m.b1014 + 199.1115*m.b1015 + 297.9298*m.b1016
                        + 473.4429*m.b1017 + 654.8556*m.b1018 + 951.3105*m.b1019 + 1414.4291*m.b1020 + 1766.9302*m.b1021
                        + 2202.0257*m.b1022 + 2892.2789*m.b1023 + 3654.8022*m.b1024 + 4505.8195*m.b1025
                        + 5709.3379*m.b1026 + 7024.9487*m.b1027 + 8805.153*m.b1028 + 11151.7189*m.b1029
                        + 14687.0542*m.b1030 + 18654.5352*m.b1031 + 23641.1721*m.b1032 + 29160.2479*m.b1033
                        + 43.244*m.b1034 + 63.728*m.b1035 + 100.144*m.b1036 + 153.63*m.b1037 + 229.876*m.b1038
                        + 365.298*m.b1039 + 505.272*m.b1040 + 734.01*m.b1041 + 1091.342*m.b1042 + 1363.324*m.b1043
                        + 1699.034*m.b1044 + 2231.618*m.b1045 + 2819.964*m.b1046 + 3476.59*m.b1047 + 4405.198*m.b1048
                        + 5420.294*m.b1049 + 6793.86*m.b1050 + 8604.418*m.b1051 + 11332.204*m.b1052 + 14393.424*m.b1053
                        + 18241.002*m.b1054 + 22499.398*m.b1055 + 68.5102*m.b1056 + 100.9624*m.b1057 + 158.6552*m.b1058
                        + 243.3915*m.b1059 + 364.1858*m.b1060 + 578.7309*m.b1061 + 800.4876*m.b1062 + 1162.8705*m.b1063
                        + 1728.9811*m.b1064 + 2159.8742*m.b1065 + 2691.7297*m.b1066 + 3535.4869*m.b1067
                        + 4467.5862*m.b1068 + 5507.8595*m.b1069 + 6979.0259*m.b1070 + 8587.2127*m.b1071
                        + 10763.313*m.b1072 + 13631.7269*m.b1073 + 17953.2782*m.b1074 + 22803.0792*m.b1075
                        + 28898.6841*m.b1076 + 35645.1359*m.b1077 + 37.7226*m.b1078 + 55.5912*m.b1079 + 87.3576*m.b1080
                        + 134.0145*m.b1081 + 200.5254*m.b1082 + 318.6567*m.b1083 + 440.7588*m.b1084 + 640.2915*m.b1085
                        + 951.9993*m.b1086 + 1189.2546*m.b1087 + 1482.1011*m.b1088 + 1946.6847*m.b1089
                        + 2459.9106*m.b1090 + 3032.6985*m.b1091 + 3842.7417*m.b1092 + 4728.2301*m.b1093
                        + 5926.419*m.b1094 + 7505.8047*m.b1095 + 9885.3066*m.b1096 + 12555.6696*m.b1097
                        + 15911.9883*m.b1098 + 19626.6717*m.b1099 + 66.7736*m.b1100 + 98.4032*m.b1101 + 154.6336*m.b1102
                        + 237.222*m.b1103 + 354.9544*m.b1104 + 564.0612*m.b1105 + 780.1968*m.b1106 + 1133.394*m.b1107
                        + 1685.1548*m.b1108 + 2105.1256*m.b1109 + 2623.4996*m.b1110 + 3445.8692*m.b1111
                        + 4354.3416*m.b1112 + 5368.246*m.b1113 + 6802.1212*m.b1114 + 8369.5436*m.b1115
                        + 10490.484*m.b1116 + 13286.1892*m.b1117 + 17498.1976*m.b1118 + 22225.0656*m.b1119
                        + 28166.1588*m.b1120 + 34741.6012*m.b1121 + 56.639*m.b1122 + 83.468*m.b1123 + 131.164*m.b1124
                        + 201.2175*m.b1125 + 301.081*m.b1126 + 478.4505*m.b1127 + 661.782*m.b1128 + 961.3725*m.b1129
                        + 1429.3895*m.b1130 + 1785.619*m.b1131 + 2225.3165*m.b1132 + 2922.8705*m.b1133
                        + 3693.459*m.b1134 + 4553.4775*m.b1135 + 5769.7255*m.b1136 + 7099.2515*m.b1137
                        + 8898.285*m.b1138 + 11269.6705*m.b1139 + 14842.399*m.b1140 + 18851.844*m.b1141
                        + 23891.2245*m.b1142 + 29468.6755*m.b1143 + 21.546*m.b1144 + 31.752*m.b1145 + 49.896*m.b1146
                        + 76.545*m.b1147 + 114.534*m.b1148 + 182.007*m.b1149 + 251.748*m.b1150 + 365.715*m.b1151
                        + 543.753*m.b1152 + 679.266*m.b1153 + 846.531*m.b1154 + 1111.887*m.b1155 + 1405.026*m.b1156
                        + 1732.185*m.b1157 + 2194.857*m.b1158 + 2700.621*m.b1159 + 3384.99*m.b1160 + 4287.087*m.b1161
                        + 5646.186*m.b1162 + 7171.416*m.b1163 + 9088.443*m.b1164 + 11210.157*m.b1165 + 81.719*m.b1166
                        + 120.428*m.b1167 + 189.244*m.b1168 + 290.3175*m.b1169 + 434.401*m.b1170 + 690.3105*m.b1171
                        + 954.822*m.b1172 + 1387.0725*m.b1173 + 2062.3295*m.b1174 + 2576.299*m.b1175 + 3210.6965*m.b1176
                        + 4217.1305*m.b1177 + 5328.939*m.b1178 + 6569.7775*m.b1179 + 8324.5855*m.b1180
                        + 10242.8315*m.b1181 + 12838.485*m.b1182 + 16259.9305*m.b1183 + 21414.679*m.b1184
                        + 27199.524*m.b1185 + 34470.3645*m.b1186 + 42517.5355*m.b1187 + 47.1504*m.b1188
                        + 69.4848*m.b1189 + 109.1904*m.b1190 + 167.508*m.b1191 + 250.6416*m.b1192 + 398.2968*m.b1193
                        + 550.9152*m.b1194 + 800.316*m.b1195 + 1189.9272*m.b1196 + 1486.4784*m.b1197 + 1852.5144*m.b1198
                        + 2433.2088*m.b1199 + 3074.7024*m.b1200 + 3790.644*m.b1201 + 4803.1368*m.b1202
                        + 5909.9304*m.b1203 + 7407.576*m.b1204 + 9381.6888*m.b1205 + 12355.8864*m.b1206
                        + 15693.6384*m.b1207 + 19888.7832*m.b1208 + 24531.8568*m.b1209 + 45.5886*m.b1210
                        + 67.1832*m.b1211 + 105.5736*m.b1212 + 161.9595*m.b1213 + 242.3394*m.b1214 + 385.1037*m.b1215
                        + 532.6668*m.b1216 + 773.8065*m.b1217 + 1150.5123*m.b1218 + 1437.2406*m.b1219
                        + 1791.1521*m.b1220 + 2352.6117*m.b1221 + 2972.8566*m.b1222 + 3665.0835*m.b1223
                        + 4644.0387*m.b1224 + 5714.1711*m.b1225 + 7162.209*m.b1226 + 9070.9317*m.b1227
                        + 11946.6126*m.b1228 + 15173.8056*m.b1229 + 19229.9913*m.b1230 + 23719.2687*m.b1231
                        + 68.9396*m.b1232 + 101.5952*m.b1233 + 159.6496*m.b1234 + 244.917*m.b1235 + 366.4684*m.b1236
                        + 582.3582*m.b1237 + 805.5048*m.b1238 + 1170.159*m.b1239 + 1739.8178*m.b1240 + 2173.4116*m.b1241
                        + 2708.6006*m.b1242 + 3557.6462*m.b1243 + 4495.5876*m.b1244 + 5542.381*m.b1245
                        + 7022.7682*m.b1246 + 8641.0346*m.b1247 + 10830.774*m.b1248 + 13717.1662*m.b1249
                        + 18065.8036*m.b1250 + 22946.0016*m.b1251 + 29079.8118*m.b1252 + 35868.5482*m.b1253
                        + 22.7734*m.b1254 + 33.5608*m.b1255 + 52.7384*m.b1256 + 80.9055*m.b1257 + 121.0586*m.b1258
                        + 192.3753*m.b1259 + 266.0892*m.b1260 + 386.5485*m.b1261 + 574.7287*m.b1262 + 717.9614*m.b1263
                        + 894.7549*m.b1264 + 1175.2273*m.b1265 + 1485.0654*m.b1266 + 1830.8615*m.b1267
                        + 2319.8903*m.b1268 + 2854.4659*m.b1269 + 3577.821*m.b1270 + 4531.3073*m.b1271
                        + 5967.8294*m.b1272 + 7579.9464*m.b1273 + 9606.1797*m.b1274 + 11848.7603*m.b1275 + 29.83*m.b1276
                        + 43.96*m.b1277 + 69.08*m.b1278 + 105.975*m.b1279 + 158.57*m.b1280 + 251.985*m.b1281
                        + 348.54*m.b1282 + 506.325*m.b1283 + 752.815*m.b1284 + 940.43*m.b1285 + 1172.005*m.b1286
                        + 1539.385*m.b1287 + 1945.23*m.b1288 + 2398.175*m.b1289 + 3038.735*m.b1290 + 3738.955*m.b1291
                        + 4686.45*m.b1292 + 5935.385*m.b1293 + 7817.03*m.b1294 + 9928.68*m.b1295 + 12582.765*m.b1296
                        + 15520.235*m.b1297 + 54.8872*m.b1298 + 80.8864*m.b1299 + 127.1072*m.b1300 + 194.994*m.b1301
                        + 291.7688*m.b1302 + 463.6524*m.b1303 + 641.3136*m.b1304 + 931.638*m.b1305 + 1385.1796*m.b1306
                        + 1730.3912*m.b1307 + 2156.4892*m.b1308 + 2832.4684*m.b1309 + 3579.2232*m.b1310
                        + 4412.642*m.b1311 + 5591.2724*m.b1312 + 6879.6772*m.b1313 + 8623.068*m.b1314
                        + 10921.1084*m.b1315 + 14383.3352*m.b1316 + 18268.7712*m.b1317 + 23152.2876*m.b1318
                        + 28557.2324*m.b1319 + 13.2012*m.b1320 + 19.4544*m.b1321 + 30.5712*m.b1322 + 46.899*m.b1323
                        + 70.1748*m.b1324 + 111.5154*m.b1325 + 154.2456*m.b1326 + 224.073*m.b1327 + 333.1566*m.b1328
                        + 416.1852*m.b1329 + 518.6682*m.b1330 + 681.2514*m.b1331 + 860.8572*m.b1332 + 1061.307*m.b1333
                        + 1344.7854*m.b1334 + 1654.6662*m.b1335 + 2073.978*m.b1336 + 2626.6914*m.b1337
                        + 3459.4092*m.b1338 + 4393.9152*m.b1339 + 5568.4746*m.b1340 + 6868.4454*m.b1341
                        + 62.9546*m.b1342 + 92.7752*m.b1343 + 145.7896*m.b1344 + 223.6545*m.b1345 + 334.6534*m.b1346
                        + 531.8007*m.b1347 + 735.5748*m.b1348 + 1068.5715*m.b1349 + 1588.7753*m.b1350
                        + 1984.7266*m.b1351 + 2473.4531*m.b1352 + 3248.7887*m.b1353 + 4105.3026*m.b1354
                        + 5061.2185*m.b1355 + 6413.0857*m.b1356 + 7890.8621*m.b1357 + 9890.499*m.b1358
                        + 12526.3087*m.b1359 + 16497.4186*m.b1360 + 20953.9416*m.b1361 + 26555.2443*m.b1362
                        + 32754.6157*m.b1363 + 31.6046*m.b1364 + 46.5752*m.b1365 + 73.1896*m.b1366 + 112.2795*m.b1367
                        + 168.0034*m.b1368 + 266.9757*m.b1369 + 369.2748*m.b1370 + 536.4465*m.b1371 + 797.6003*m.b1372
                        + 996.3766*m.b1373 + 1241.7281*m.b1374 + 1630.9637*m.b1375 + 2060.9526*m.b1376
                        + 2540.8435*m.b1377 + 3219.5107*m.b1378 + 3961.3871*m.b1379 + 4965.249*m.b1380
                        + 6288.4837*m.b1381 + 8282.0686*m.b1382 + 10519.3416*m.b1383 + 13331.3193*m.b1384
                        + 16443.5407*m.b1385 + 80.0812*m.b1386 + 118.0144*m.b1387 + 185.4512*m.b1388 + 284.499*m.b1389
                        + 425.6948*m.b1390 + 676.4754*m.b1391 + 935.6856*m.b1392 + 1359.273*m.b1393 + 2020.9966*m.b1394
                        + 2524.6652*m.b1395 + 3146.3482*m.b1396 + 4132.6114*m.b1397 + 5222.1372*m.b1398
                        + 6438.107*m.b1399 + 8157.7454*m.b1400 + 10037.5462*m.b1401 + 12581.178*m.b1402
                        + 15934.0514*m.b1403 + 20985.4892*m.b1404 + 26654.3952*m.b1405 + 33779.5146*m.b1406
                        + 41665.4054*m.b1407 + 0.38*m.b1408 + 0.56*m.b1409 + 0.88*m.b1410 + 1.35*m.b1411 + 2.02*m.b1412
                        + 3.21*m.b1413 + 4.44*m.b1414 + 6.45*m.b1415 + 9.59*m.b1416 + 11.98*m.b1417 + 14.93*m.b1418
                        + 19.61*m.b1419 + 24.78*m.b1420 + 30.55*m.b1421 + 38.71*m.b1422 + 47.63*m.b1423 + 59.7*m.b1424
                        + 75.61*m.b1425 + 99.58*m.b1426 + 126.48*m.b1427 + 160.29*m.b1428 + 197.71*m.b1429
                       , sense=minimize)

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

m.c38 = Constraint(expr=SignPower(m.x38,1.852) - 7.54518669674666*(1.27323954473516*m.x96)**2.435*(m.x1 - m.x17) == 0)

m.c39 = Constraint(expr=SignPower(m.x39,1.852) - 13.2833707182083*(1.27323954473516*m.x97)**2.435*(m.x1 - m.x31) == 0)

m.c40 = Constraint(expr=SignPower(m.x40,1.852) - 8.36561705244769*(1.27323954473516*m.x98)**2.435*(m.x2 - m.x3) == 0)

m.c41 = Constraint(expr=SignPower(m.x41,1.852) - 6.14652381334041*(1.27323954473516*m.x99)**2.435*(m.x2 - m.x18) == 0)

m.c42 = Constraint(expr=SignPower(m.x42,1.852) - 3.20318171482504*(1.27323954473516*m.x100)**2.435*(m.x3 - m.x4) == 0)

m.c43 = Constraint(expr=SignPower(m.x43,1.852) - 5.07652030133837*(1.27323954473516*m.x101)**2.435*(m.x3 - m.x11) == 0)

m.c44 = Constraint(expr=SignPower(m.x44,1.852) - 3.4650073882185*(1.27323954473516*m.x102)**2.435*(m.x4 - m.x5) == 0)

m.c45 = Constraint(expr=SignPower(m.x45,1.852) - 2.97832184420089*(1.27323954473516*m.x103)**2.435*(m.x5 - m.x6) == 0)

m.c46 = Constraint(expr=SignPower(m.x46,1.852) - 12.9435196518941*(1.27323954473516*m.x104)**2.435*(m.x5 - m.x13) == 0)

m.c47 = Constraint(expr=SignPower(m.x47,1.852) - 7.37573805949552*(1.27323954473516*m.x105)**2.435*(m.x6 - m.x7) == 0)

m.c48 = Constraint(expr=SignPower(m.x48,1.852) - 4.97713895389092*(1.27323954473516*m.x106)**2.435*(m.x7 - m.x24) == 0)

m.c49 = Constraint(expr=SignPower(m.x49,1.852) - 6.92450563984575*(1.27323954473516*m.x107)**2.435*(m.x8 - m.x28) == 0)

m.c50 = Constraint(expr=SignPower(m.x50,1.852) - 8.93018619827125*(1.27323954473516*m.x108)**2.435*(m.x9 - m.x36) == 0)

m.c51 = Constraint(expr=SignPower(m.x51,1.852) - 6.81613354559123*(1.27323954473516*m.x109)**2.435*(m.x10 - m.x11) == 0)

m.c52 = Constraint(expr=SignPower(m.x52,1.852) - 20.1063626226433*(1.27323954473516*m.x110)**2.435*(m.x10 - m.x32) == 0)

m.c53 = Constraint(expr=SignPower(m.x53,1.852) - 6.15710237789715*(1.27323954473516*m.x111)**2.435*(m.x11 - m.x19) == 0)

m.c54 = Constraint(expr=SignPower(m.x54,1.852) - 12.0251979094848*(1.27323954473516*m.x112)**2.435*(m.x11 - m.x26) == 0)

m.c55 = Constraint(expr=SignPower(m.x55,1.852) - 18.9071156258982*(1.27323954473516*m.x113)**2.435*(m.x12 - m.x4) == 0)

m.c56 = Constraint(expr=SignPower(m.x56,1.852) - 4.91438446676194*(1.27323954473516*m.x114)**2.435*(m.x12 - m.x13) == 0)

m.c57 = Constraint(expr=SignPower(m.x57,1.852) - 8.91429194500389*(1.27323954473516*m.x115)**2.435*(m.x13 - m.x14) == 0)

m.c58 = Constraint(expr=SignPower(m.x58,1.852) - 26.8264324011807*(1.27323954473516*m.x116)**2.435*(m.x14 - m.x20) == 0)

m.c59 = Constraint(expr=SignPower(m.x59,1.852) - 15.3658381018574*(1.27323954473516*m.x117)**2.435*(m.x14 - m.x21) == 0)

m.c60 = Constraint(expr=SignPower(m.x60,1.852) - 5.47915428213591*(1.27323954473516*m.x118)**2.435*(m.x15 - m.x16) == 0)

m.c61 = Constraint(expr=SignPower(m.x61,1.852) - 12.3941968059897*(1.27323954473516*m.x119)**2.435*(m.x15 - m.x22) == 0)

m.c62 = Constraint(expr=SignPower(m.x62,1.852) - 12.1727911758426*(1.27323954473516*m.x120)**2.435*(m.x16 - m.x25) == 0)

m.c63 = Constraint(expr=SignPower(m.x63,1.852) - 7.36435072680552*(1.27323954473516*m.x121)**2.435*(m.x16 - m.x29) == 0)

m.c64 = Constraint(expr=SignPower(m.x64,1.852) - 2.67347866408692*(1.27323954473516*m.x122)**2.435*(m.x17 - m.x2) == 0)

m.c65 = Constraint(expr=SignPower(m.x65,1.852) - 4.26981664901998*(1.27323954473516*m.x123)**2.435*(m.x17 - m.x18) == 0)

m.c66 = Constraint(expr=SignPower(m.x66,1.852) - 11.9306691979524*(1.27323954473516*m.x124)**2.435*(m.x18 - m.x10) == 0)

m.c67 = Constraint(expr=SignPower(m.x67,1.852) - 10.0531813113216*(1.27323954473516*m.x125)**2.435*(m.x19 - m.x12) == 0)

m.c68 = Constraint(expr=SignPower(m.x68,1.852) - 4.03829464164518*(1.27323954473516*m.x126)**2.435*(m.x19 - m.x20) == 0)

m.c69 = Constraint(expr=SignPower(m.x69,1.852) - 9.20256303040962*(1.27323954473516*m.x127)**2.435*(m.x20 - m.x15) == 0)

m.c70 = Constraint(expr=SignPower(m.x70,1.852) - 4.76795176286395*(1.27323954473516*m.x128)**2.435*(m.x21 - m.x6) == 0)

m.c71 = Constraint(expr=SignPower(m.x71,1.852) - 6.78795816127998*(1.27323954473516*m.x129)**2.435*(m.x21 - m.x22) == 0)

m.c72 = Constraint(expr=SignPower(m.x72,1.852) - 2.93779213966064*(1.27323954473516*m.x130)**2.435*(m.x22 - m.x7) == 0)

m.c73 = Constraint(expr=SignPower(m.x73,1.852) - 9.650279247207*(1.27323954473516*m.x131)**2.435*(m.x22 - m.x23) == 0)

m.c74 = Constraint(expr=SignPower(m.x74,1.852) - 13.3417552725105*(1.27323954473516*m.x132)**2.435*(m.x23 - m.x25) == 0)

m.c75 = Constraint(expr=SignPower(m.x75,1.852) - 7.55828103719978*(1.27323954473516*m.x133)**2.435*(m.x24 - m.x8) == 0)

m.c76 = Constraint(expr=SignPower(m.x76,1.852) - 4.7485137988153*(1.27323954473516*m.x134)**2.435*(m.x24 - m.x23) == 0)

m.c77 = Constraint(expr=SignPower(m.x77,1.852) - 6.79164001532366*(1.27323954473516*m.x135)**2.435*(m.x25 - m.x8) == 0)

m.c78 = Constraint(expr=SignPower(m.x78,1.852) - 8.80227579841904*(1.27323954473516*m.x136)**2.435*(m.x26 - m.x15) == 0)

m.c79 = Constraint(expr=SignPower(m.x79,1.852) - 5.55604296333733*(1.27323954473516*m.x137)**2.435*(m.x26 - m.x27) == 0)

m.c80 = Constraint(expr=SignPower(m.x80,1.852) - 10.0906516153932*(1.27323954473516*m.x138)**2.435*(m.x27 - m.x16) == 0)

m.c81 = Constraint(expr=SignPower(m.x81,1.852) - 5.70054055235651*(1.27323954473516*m.x139)**2.435*(m.x28 - m.x9) == 0)

m.c82 = Constraint(expr=SignPower(m.x82,1.852) - 6.72055676524714*(1.27323954473516*m.x140)**2.435*(m.x28 - m.x29) == 0)

m.c83 = Constraint(expr=SignPower(m.x83,1.852) - 17.6666487806012*(1.27323954473516*m.x141)**2.435*(m.x29 - m.x30) == 0)

m.c84 = Constraint(expr=SignPower(m.x84,1.852) - 4.65798179893088*(1.27323954473516*m.x142)**2.435*(m.x29 - m.x33) == 0)

m.c85 = Constraint(expr=SignPower(m.x85,1.852) - 8.07300923484918*(1.27323954473516*m.x143)**2.435*(m.x30 - m.x9) == 0)

m.c86 = Constraint(expr=SignPower(m.x86,1.852) - 8.34957894356995*(1.27323954473516*m.x144)**2.435*(m.x30 - m.x35) == 0)

m.c87 = Constraint(expr=SignPower(m.x87,1.852) - 5.52143636787613*(1.27323954473516*m.x145)**2.435*(m.x31 - m.x10) == 0)

m.c88 = Constraint(expr=SignPower(m.x88,1.852) - 16.7144833282177*(1.27323954473516*m.x146)**2.435*(m.x31 - m.x34) == 0)

m.c89 = Constraint(expr=SignPower(m.x89,1.852) - 12.7604966351603*(1.27323954473516*m.x147)**2.435*(m.x32 - m.x27) == 0)

m.c90 = Constraint(expr=SignPower(m.x90,1.852) - 6.93505251910888*(1.27323954473516*m.x148)**2.435*(m.x32 - m.x33) == 0)

m.c91 = Constraint(expr=SignPower(m.x91,1.852) - 28.8341676989087*(1.27323954473516*m.x149)**2.435*(m.x33 - m.x34) == 0)

m.c92 = Constraint(expr=SignPower(m.x92,1.852) - 6.04635109470687*(1.27323954473516*m.x150)**2.435*(m.x34 - m.x35) == 0)

m.c93 = Constraint(expr=SignPower(m.x93,1.852) - 12.043994058676*(1.27323954473516*m.x151)**2.435*(m.x35 - m.x36) == 0)

m.c94 = Constraint(expr=SignPower(m.x94,1.852) - 4.75324563851232*(1.27323954473516*m.x152)**2.435*(m.x36 - m.x1) == 0)

m.c95 = Constraint(expr=SignPower(m.x95,1.852) - 1001.69898586009*(1.27323954473516*m.x153)**2.435*(m.x37 - m.x1) == 0)

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

m.c212 = Constraint(expr=   m.x96 - 0.000201061929829747*m.b154 - 0.000326851299679482*m.b155
                          - 0.000530929158456675*m.b156 - 0.000834689752132272*m.b157 - 0.00130740519871793*m.b158
                          - 0.00207499053176952*m.b159 - 0.00296091966008184*m.b160 - 0.00425447043519744*m.b161
                          - 0.00636172512351933*m.b162 - 0.0082033581529802*m.b163 - 0.0103147597436048*m.b164
                          - 0.0134370944342281*m.b165 - 0.0170178817407898*m.b166 - 0.0210211504274062*m.b167
                          - 0.026590440219984*m.b168 - 0.0328776781816867*m.b169 - 0.0412590389744193*m.b170
                          - 0.0521982216738517*m.b171 - 0.0663255868459265*m.b172 - 0.0841874260371767*m.b173
                          - 0.106477402905515*m.b174 - 0.131510712726747*m.b175 == 0)

m.c213 = Constraint(expr=   m.x97 - 0.000201061929829747*m.b176 - 0.000326851299679482*m.b177
                          - 0.000530929158456675*m.b178 - 0.000834689752132272*m.b179 - 0.00130740519871793*m.b180
                          - 0.00207499053176952*m.b181 - 0.00296091966008184*m.b182 - 0.00425447043519744*m.b183
                          - 0.00636172512351933*m.b184 - 0.0082033581529802*m.b185 - 0.0103147597436048*m.b186
                          - 0.0134370944342281*m.b187 - 0.0170178817407898*m.b188 - 0.0210211504274062*m.b189
                          - 0.026590440219984*m.b190 - 0.0328776781816867*m.b191 - 0.0412590389744193*m.b192
                          - 0.0521982216738517*m.b193 - 0.0663255868459265*m.b194 - 0.0841874260371767*m.b195
                          - 0.106477402905515*m.b196 - 0.131510712726747*m.b197 == 0)

m.c214 = Constraint(expr=   m.x98 - 0.000201061929829747*m.b198 - 0.000326851299679482*m.b199
                          - 0.000530929158456675*m.b200 - 0.000834689752132272*m.b201 - 0.00130740519871793*m.b202
                          - 0.00207499053176952*m.b203 - 0.00296091966008184*m.b204 - 0.00425447043519744*m.b205
                          - 0.00636172512351933*m.b206 - 0.0082033581529802*m.b207 - 0.0103147597436048*m.b208
                          - 0.0134370944342281*m.b209 - 0.0170178817407898*m.b210 - 0.0210211504274062*m.b211
                          - 0.026590440219984*m.b212 - 0.0328776781816867*m.b213 - 0.0412590389744193*m.b214
                          - 0.0521982216738517*m.b215 - 0.0663255868459265*m.b216 - 0.0841874260371767*m.b217
                          - 0.106477402905515*m.b218 - 0.131510712726747*m.b219 == 0)

m.c215 = Constraint(expr=   m.x99 - 0.000201061929829747*m.b220 - 0.000326851299679482*m.b221
                          - 0.000530929158456675*m.b222 - 0.000834689752132272*m.b223 - 0.00130740519871793*m.b224
                          - 0.00207499053176952*m.b225 - 0.00296091966008184*m.b226 - 0.00425447043519744*m.b227
                          - 0.00636172512351933*m.b228 - 0.0082033581529802*m.b229 - 0.0103147597436048*m.b230
                          - 0.0134370944342281*m.b231 - 0.0170178817407898*m.b232 - 0.0210211504274062*m.b233
                          - 0.026590440219984*m.b234 - 0.0328776781816867*m.b235 - 0.0412590389744193*m.b236
                          - 0.0521982216738517*m.b237 - 0.0663255868459265*m.b238 - 0.0841874260371767*m.b239
                          - 0.106477402905515*m.b240 - 0.131510712726747*m.b241 == 0)

m.c216 = Constraint(expr=   m.x100 - 0.000201061929829747*m.b242 - 0.000326851299679482*m.b243
                          - 0.000530929158456675*m.b244 - 0.000834689752132272*m.b245 - 0.00130740519871793*m.b246
                          - 0.00207499053176952*m.b247 - 0.00296091966008184*m.b248 - 0.00425447043519744*m.b249
                          - 0.00636172512351933*m.b250 - 0.0082033581529802*m.b251 - 0.0103147597436048*m.b252
                          - 0.0134370944342281*m.b253 - 0.0170178817407898*m.b254 - 0.0210211504274062*m.b255
                          - 0.026590440219984*m.b256 - 0.0328776781816867*m.b257 - 0.0412590389744193*m.b258
                          - 0.0521982216738517*m.b259 - 0.0663255868459265*m.b260 - 0.0841874260371767*m.b261
                          - 0.106477402905515*m.b262 - 0.131510712726747*m.b263 == 0)

m.c217 = Constraint(expr=   m.x101 - 0.000201061929829747*m.b264 - 0.000326851299679482*m.b265
                          - 0.000530929158456675*m.b266 - 0.000834689752132272*m.b267 - 0.00130740519871793*m.b268
                          - 0.00207499053176952*m.b269 - 0.00296091966008184*m.b270 - 0.00425447043519744*m.b271
                          - 0.00636172512351933*m.b272 - 0.0082033581529802*m.b273 - 0.0103147597436048*m.b274
                          - 0.0134370944342281*m.b275 - 0.0170178817407898*m.b276 - 0.0210211504274062*m.b277
                          - 0.026590440219984*m.b278 - 0.0328776781816867*m.b279 - 0.0412590389744193*m.b280
                          - 0.0521982216738517*m.b281 - 0.0663255868459265*m.b282 - 0.0841874260371767*m.b283
                          - 0.106477402905515*m.b284 - 0.131510712726747*m.b285 == 0)

m.c218 = Constraint(expr=   m.x102 - 0.000201061929829747*m.b286 - 0.000326851299679482*m.b287
                          - 0.000530929158456675*m.b288 - 0.000834689752132272*m.b289 - 0.00130740519871793*m.b290
                          - 0.00207499053176952*m.b291 - 0.00296091966008184*m.b292 - 0.00425447043519744*m.b293
                          - 0.00636172512351933*m.b294 - 0.0082033581529802*m.b295 - 0.0103147597436048*m.b296
                          - 0.0134370944342281*m.b297 - 0.0170178817407898*m.b298 - 0.0210211504274062*m.b299
                          - 0.026590440219984*m.b300 - 0.0328776781816867*m.b301 - 0.0412590389744193*m.b302
                          - 0.0521982216738517*m.b303 - 0.0663255868459265*m.b304 - 0.0841874260371767*m.b305
                          - 0.106477402905515*m.b306 - 0.131510712726747*m.b307 == 0)

m.c219 = Constraint(expr=   m.x103 - 0.000201061929829747*m.b308 - 0.000326851299679482*m.b309
                          - 0.000530929158456675*m.b310 - 0.000834689752132272*m.b311 - 0.00130740519871793*m.b312
                          - 0.00207499053176952*m.b313 - 0.00296091966008184*m.b314 - 0.00425447043519744*m.b315
                          - 0.00636172512351933*m.b316 - 0.0082033581529802*m.b317 - 0.0103147597436048*m.b318
                          - 0.0134370944342281*m.b319 - 0.0170178817407898*m.b320 - 0.0210211504274062*m.b321
                          - 0.026590440219984*m.b322 - 0.0328776781816867*m.b323 - 0.0412590389744193*m.b324
                          - 0.0521982216738517*m.b325 - 0.0663255868459265*m.b326 - 0.0841874260371767*m.b327
                          - 0.106477402905515*m.b328 - 0.131510712726747*m.b329 == 0)

m.c220 = Constraint(expr=   m.x104 - 0.000201061929829747*m.b330 - 0.000326851299679482*m.b331
                          - 0.000530929158456675*m.b332 - 0.000834689752132272*m.b333 - 0.00130740519871793*m.b334
                          - 0.00207499053176952*m.b335 - 0.00296091966008184*m.b336 - 0.00425447043519744*m.b337
                          - 0.00636172512351933*m.b338 - 0.0082033581529802*m.b339 - 0.0103147597436048*m.b340
                          - 0.0134370944342281*m.b341 - 0.0170178817407898*m.b342 - 0.0210211504274062*m.b343
                          - 0.026590440219984*m.b344 - 0.0328776781816867*m.b345 - 0.0412590389744193*m.b346
                          - 0.0521982216738517*m.b347 - 0.0663255868459265*m.b348 - 0.0841874260371767*m.b349
                          - 0.106477402905515*m.b350 - 0.131510712726747*m.b351 == 0)

m.c221 = Constraint(expr=   m.x105 - 0.000201061929829747*m.b352 - 0.000326851299679482*m.b353
                          - 0.000530929158456675*m.b354 - 0.000834689752132272*m.b355 - 0.00130740519871793*m.b356
                          - 0.00207499053176952*m.b357 - 0.00296091966008184*m.b358 - 0.00425447043519744*m.b359
                          - 0.00636172512351933*m.b360 - 0.0082033581529802*m.b361 - 0.0103147597436048*m.b362
                          - 0.0134370944342281*m.b363 - 0.0170178817407898*m.b364 - 0.0210211504274062*m.b365
                          - 0.026590440219984*m.b366 - 0.0328776781816867*m.b367 - 0.0412590389744193*m.b368
                          - 0.0521982216738517*m.b369 - 0.0663255868459265*m.b370 - 0.0841874260371767*m.b371
                          - 0.106477402905515*m.b372 - 0.131510712726747*m.b373 == 0)

m.c222 = Constraint(expr=   m.x106 - 0.000201061929829747*m.b374 - 0.000326851299679482*m.b375
                          - 0.000530929158456675*m.b376 - 0.000834689752132272*m.b377 - 0.00130740519871793*m.b378
                          - 0.00207499053176952*m.b379 - 0.00296091966008184*m.b380 - 0.00425447043519744*m.b381
                          - 0.00636172512351933*m.b382 - 0.0082033581529802*m.b383 - 0.0103147597436048*m.b384
                          - 0.0134370944342281*m.b385 - 0.0170178817407898*m.b386 - 0.0210211504274062*m.b387
                          - 0.026590440219984*m.b388 - 0.0328776781816867*m.b389 - 0.0412590389744193*m.b390
                          - 0.0521982216738517*m.b391 - 0.0663255868459265*m.b392 - 0.0841874260371767*m.b393
                          - 0.106477402905515*m.b394 - 0.131510712726747*m.b395 == 0)

m.c223 = Constraint(expr=   m.x107 - 0.000201061929829747*m.b396 - 0.000326851299679482*m.b397
                          - 0.000530929158456675*m.b398 - 0.000834689752132272*m.b399 - 0.00130740519871793*m.b400
                          - 0.00207499053176952*m.b401 - 0.00296091966008184*m.b402 - 0.00425447043519744*m.b403
                          - 0.00636172512351933*m.b404 - 0.0082033581529802*m.b405 - 0.0103147597436048*m.b406
                          - 0.0134370944342281*m.b407 - 0.0170178817407898*m.b408 - 0.0210211504274062*m.b409
                          - 0.026590440219984*m.b410 - 0.0328776781816867*m.b411 - 0.0412590389744193*m.b412
                          - 0.0521982216738517*m.b413 - 0.0663255868459265*m.b414 - 0.0841874260371767*m.b415
                          - 0.106477402905515*m.b416 - 0.131510712726747*m.b417 == 0)

m.c224 = Constraint(expr=   m.x108 - 0.000201061929829747*m.b418 - 0.000326851299679482*m.b419
                          - 0.000530929158456675*m.b420 - 0.000834689752132272*m.b421 - 0.00130740519871793*m.b422
                          - 0.00207499053176952*m.b423 - 0.00296091966008184*m.b424 - 0.00425447043519744*m.b425
                          - 0.00636172512351933*m.b426 - 0.0082033581529802*m.b427 - 0.0103147597436048*m.b428
                          - 0.0134370944342281*m.b429 - 0.0170178817407898*m.b430 - 0.0210211504274062*m.b431
                          - 0.026590440219984*m.b432 - 0.0328776781816867*m.b433 - 0.0412590389744193*m.b434
                          - 0.0521982216738517*m.b435 - 0.0663255868459265*m.b436 - 0.0841874260371767*m.b437
                          - 0.106477402905515*m.b438 - 0.131510712726747*m.b439 == 0)

m.c225 = Constraint(expr=   m.x109 - 0.000201061929829747*m.b440 - 0.000326851299679482*m.b441
                          - 0.000530929158456675*m.b442 - 0.000834689752132272*m.b443 - 0.00130740519871793*m.b444
                          - 0.00207499053176952*m.b445 - 0.00296091966008184*m.b446 - 0.00425447043519744*m.b447
                          - 0.00636172512351933*m.b448 - 0.0082033581529802*m.b449 - 0.0103147597436048*m.b450
                          - 0.0134370944342281*m.b451 - 0.0170178817407898*m.b452 - 0.0210211504274062*m.b453
                          - 0.026590440219984*m.b454 - 0.0328776781816867*m.b455 - 0.0412590389744193*m.b456
                          - 0.0521982216738517*m.b457 - 0.0663255868459265*m.b458 - 0.0841874260371767*m.b459
                          - 0.106477402905515*m.b460 - 0.131510712726747*m.b461 == 0)

m.c226 = Constraint(expr=   m.x110 - 0.000201061929829747*m.b462 - 0.000326851299679482*m.b463
                          - 0.000530929158456675*m.b464 - 0.000834689752132272*m.b465 - 0.00130740519871793*m.b466
                          - 0.00207499053176952*m.b467 - 0.00296091966008184*m.b468 - 0.00425447043519744*m.b469
                          - 0.00636172512351933*m.b470 - 0.0082033581529802*m.b471 - 0.0103147597436048*m.b472
                          - 0.0134370944342281*m.b473 - 0.0170178817407898*m.b474 - 0.0210211504274062*m.b475
                          - 0.026590440219984*m.b476 - 0.0328776781816867*m.b477 - 0.0412590389744193*m.b478
                          - 0.0521982216738517*m.b479 - 0.0663255868459265*m.b480 - 0.0841874260371767*m.b481
                          - 0.106477402905515*m.b482 - 0.131510712726747*m.b483 == 0)

m.c227 = Constraint(expr=   m.x111 - 0.000201061929829747*m.b484 - 0.000326851299679482*m.b485
                          - 0.000530929158456675*m.b486 - 0.000834689752132272*m.b487 - 0.00130740519871793*m.b488
                          - 0.00207499053176952*m.b489 - 0.00296091966008184*m.b490 - 0.00425447043519744*m.b491
                          - 0.00636172512351933*m.b492 - 0.0082033581529802*m.b493 - 0.0103147597436048*m.b494
                          - 0.0134370944342281*m.b495 - 0.0170178817407898*m.b496 - 0.0210211504274062*m.b497
                          - 0.026590440219984*m.b498 - 0.0328776781816867*m.b499 - 0.0412590389744193*m.b500
                          - 0.0521982216738517*m.b501 - 0.0663255868459265*m.b502 - 0.0841874260371767*m.b503
                          - 0.106477402905515*m.b504 - 0.131510712726747*m.b505 == 0)

m.c228 = Constraint(expr=   m.x112 - 0.000201061929829747*m.b506 - 0.000326851299679482*m.b507
                          - 0.000530929158456675*m.b508 - 0.000834689752132272*m.b509 - 0.00130740519871793*m.b510
                          - 0.00207499053176952*m.b511 - 0.00296091966008184*m.b512 - 0.00425447043519744*m.b513
                          - 0.00636172512351933*m.b514 - 0.0082033581529802*m.b515 - 0.0103147597436048*m.b516
                          - 0.0134370944342281*m.b517 - 0.0170178817407898*m.b518 - 0.0210211504274062*m.b519
                          - 0.026590440219984*m.b520 - 0.0328776781816867*m.b521 - 0.0412590389744193*m.b522
                          - 0.0521982216738517*m.b523 - 0.0663255868459265*m.b524 - 0.0841874260371767*m.b525
                          - 0.106477402905515*m.b526 - 0.131510712726747*m.b527 == 0)

m.c229 = Constraint(expr=   m.x113 - 0.000201061929829747*m.b528 - 0.000326851299679482*m.b529
                          - 0.000530929158456675*m.b530 - 0.000834689752132272*m.b531 - 0.00130740519871793*m.b532
                          - 0.00207499053176952*m.b533 - 0.00296091966008184*m.b534 - 0.00425447043519744*m.b535
                          - 0.00636172512351933*m.b536 - 0.0082033581529802*m.b537 - 0.0103147597436048*m.b538
                          - 0.0134370944342281*m.b539 - 0.0170178817407898*m.b540 - 0.0210211504274062*m.b541
                          - 0.026590440219984*m.b542 - 0.0328776781816867*m.b543 - 0.0412590389744193*m.b544
                          - 0.0521982216738517*m.b545 - 0.0663255868459265*m.b546 - 0.0841874260371767*m.b547
                          - 0.106477402905515*m.b548 - 0.131510712726747*m.b549 == 0)

m.c230 = Constraint(expr=   m.x114 - 0.000201061929829747*m.b550 - 0.000326851299679482*m.b551
                          - 0.000530929158456675*m.b552 - 0.000834689752132272*m.b553 - 0.00130740519871793*m.b554
                          - 0.00207499053176952*m.b555 - 0.00296091966008184*m.b556 - 0.00425447043519744*m.b557
                          - 0.00636172512351933*m.b558 - 0.0082033581529802*m.b559 - 0.0103147597436048*m.b560
                          - 0.0134370944342281*m.b561 - 0.0170178817407898*m.b562 - 0.0210211504274062*m.b563
                          - 0.026590440219984*m.b564 - 0.0328776781816867*m.b565 - 0.0412590389744193*m.b566
                          - 0.0521982216738517*m.b567 - 0.0663255868459265*m.b568 - 0.0841874260371767*m.b569
                          - 0.106477402905515*m.b570 - 0.131510712726747*m.b571 == 0)

m.c231 = Constraint(expr=   m.x115 - 0.000201061929829747*m.b572 - 0.000326851299679482*m.b573
                          - 0.000530929158456675*m.b574 - 0.000834689752132272*m.b575 - 0.00130740519871793*m.b576
                          - 0.00207499053176952*m.b577 - 0.00296091966008184*m.b578 - 0.00425447043519744*m.b579
                          - 0.00636172512351933*m.b580 - 0.0082033581529802*m.b581 - 0.0103147597436048*m.b582
                          - 0.0134370944342281*m.b583 - 0.0170178817407898*m.b584 - 0.0210211504274062*m.b585
                          - 0.026590440219984*m.b586 - 0.0328776781816867*m.b587 - 0.0412590389744193*m.b588
                          - 0.0521982216738517*m.b589 - 0.0663255868459265*m.b590 - 0.0841874260371767*m.b591
                          - 0.106477402905515*m.b592 - 0.131510712726747*m.b593 == 0)

m.c232 = Constraint(expr=   m.x116 - 0.000201061929829747*m.b594 - 0.000326851299679482*m.b595
                          - 0.000530929158456675*m.b596 - 0.000834689752132272*m.b597 - 0.00130740519871793*m.b598
                          - 0.00207499053176952*m.b599 - 0.00296091966008184*m.b600 - 0.00425447043519744*m.b601
                          - 0.00636172512351933*m.b602 - 0.0082033581529802*m.b603 - 0.0103147597436048*m.b604
                          - 0.0134370944342281*m.b605 - 0.0170178817407898*m.b606 - 0.0210211504274062*m.b607
                          - 0.026590440219984*m.b608 - 0.0328776781816867*m.b609 - 0.0412590389744193*m.b610
                          - 0.0521982216738517*m.b611 - 0.0663255868459265*m.b612 - 0.0841874260371767*m.b613
                          - 0.106477402905515*m.b614 - 0.131510712726747*m.b615 == 0)

m.c233 = Constraint(expr=   m.x117 - 0.000201061929829747*m.b616 - 0.000326851299679482*m.b617
                          - 0.000530929158456675*m.b618 - 0.000834689752132272*m.b619 - 0.00130740519871793*m.b620
                          - 0.00207499053176952*m.b621 - 0.00296091966008184*m.b622 - 0.00425447043519744*m.b623
                          - 0.00636172512351933*m.b624 - 0.0082033581529802*m.b625 - 0.0103147597436048*m.b626
                          - 0.0134370944342281*m.b627 - 0.0170178817407898*m.b628 - 0.0210211504274062*m.b629
                          - 0.026590440219984*m.b630 - 0.0328776781816867*m.b631 - 0.0412590389744193*m.b632
                          - 0.0521982216738517*m.b633 - 0.0663255868459265*m.b634 - 0.0841874260371767*m.b635
                          - 0.106477402905515*m.b636 - 0.131510712726747*m.b637 == 0)

m.c234 = Constraint(expr=   m.x118 - 0.000201061929829747*m.b638 - 0.000326851299679482*m.b639
                          - 0.000530929158456675*m.b640 - 0.000834689752132272*m.b641 - 0.00130740519871793*m.b642
                          - 0.00207499053176952*m.b643 - 0.00296091966008184*m.b644 - 0.00425447043519744*m.b645
                          - 0.00636172512351933*m.b646 - 0.0082033581529802*m.b647 - 0.0103147597436048*m.b648
                          - 0.0134370944342281*m.b649 - 0.0170178817407898*m.b650 - 0.0210211504274062*m.b651
                          - 0.026590440219984*m.b652 - 0.0328776781816867*m.b653 - 0.0412590389744193*m.b654
                          - 0.0521982216738517*m.b655 - 0.0663255868459265*m.b656 - 0.0841874260371767*m.b657
                          - 0.106477402905515*m.b658 - 0.131510712726747*m.b659 == 0)

m.c235 = Constraint(expr=   m.x119 - 0.000201061929829747*m.b660 - 0.000326851299679482*m.b661
                          - 0.000530929158456675*m.b662 - 0.000834689752132272*m.b663 - 0.00130740519871793*m.b664
                          - 0.00207499053176952*m.b665 - 0.00296091966008184*m.b666 - 0.00425447043519744*m.b667
                          - 0.00636172512351933*m.b668 - 0.0082033581529802*m.b669 - 0.0103147597436048*m.b670
                          - 0.0134370944342281*m.b671 - 0.0170178817407898*m.b672 - 0.0210211504274062*m.b673
                          - 0.026590440219984*m.b674 - 0.0328776781816867*m.b675 - 0.0412590389744193*m.b676
                          - 0.0521982216738517*m.b677 - 0.0663255868459265*m.b678 - 0.0841874260371767*m.b679
                          - 0.106477402905515*m.b680 - 0.131510712726747*m.b681 == 0)

m.c236 = Constraint(expr=   m.x120 - 0.000201061929829747*m.b682 - 0.000326851299679482*m.b683
                          - 0.000530929158456675*m.b684 - 0.000834689752132272*m.b685 - 0.00130740519871793*m.b686
                          - 0.00207499053176952*m.b687 - 0.00296091966008184*m.b688 - 0.00425447043519744*m.b689
                          - 0.00636172512351933*m.b690 - 0.0082033581529802*m.b691 - 0.0103147597436048*m.b692
                          - 0.0134370944342281*m.b693 - 0.0170178817407898*m.b694 - 0.0210211504274062*m.b695
                          - 0.026590440219984*m.b696 - 0.0328776781816867*m.b697 - 0.0412590389744193*m.b698
                          - 0.0521982216738517*m.b699 - 0.0663255868459265*m.b700 - 0.0841874260371767*m.b701
                          - 0.106477402905515*m.b702 - 0.131510712726747*m.b703 == 0)

m.c237 = Constraint(expr=   m.x121 - 0.000201061929829747*m.b704 - 0.000326851299679482*m.b705
                          - 0.000530929158456675*m.b706 - 0.000834689752132272*m.b707 - 0.00130740519871793*m.b708
                          - 0.00207499053176952*m.b709 - 0.00296091966008184*m.b710 - 0.00425447043519744*m.b711
                          - 0.00636172512351933*m.b712 - 0.0082033581529802*m.b713 - 0.0103147597436048*m.b714
                          - 0.0134370944342281*m.b715 - 0.0170178817407898*m.b716 - 0.0210211504274062*m.b717
                          - 0.026590440219984*m.b718 - 0.0328776781816867*m.b719 - 0.0412590389744193*m.b720
                          - 0.0521982216738517*m.b721 - 0.0663255868459265*m.b722 - 0.0841874260371767*m.b723
                          - 0.106477402905515*m.b724 - 0.131510712726747*m.b725 == 0)

m.c238 = Constraint(expr=   m.x122 - 0.000201061929829747*m.b726 - 0.000326851299679482*m.b727
                          - 0.000530929158456675*m.b728 - 0.000834689752132272*m.b729 - 0.00130740519871793*m.b730
                          - 0.00207499053176952*m.b731 - 0.00296091966008184*m.b732 - 0.00425447043519744*m.b733
                          - 0.00636172512351933*m.b734 - 0.0082033581529802*m.b735 - 0.0103147597436048*m.b736
                          - 0.0134370944342281*m.b737 - 0.0170178817407898*m.b738 - 0.0210211504274062*m.b739
                          - 0.026590440219984*m.b740 - 0.0328776781816867*m.b741 - 0.0412590389744193*m.b742
                          - 0.0521982216738517*m.b743 - 0.0663255868459265*m.b744 - 0.0841874260371767*m.b745
                          - 0.106477402905515*m.b746 - 0.131510712726747*m.b747 == 0)

m.c239 = Constraint(expr=   m.x123 - 0.000201061929829747*m.b748 - 0.000326851299679482*m.b749
                          - 0.000530929158456675*m.b750 - 0.000834689752132272*m.b751 - 0.00130740519871793*m.b752
                          - 0.00207499053176952*m.b753 - 0.00296091966008184*m.b754 - 0.00425447043519744*m.b755
                          - 0.00636172512351933*m.b756 - 0.0082033581529802*m.b757 - 0.0103147597436048*m.b758
                          - 0.0134370944342281*m.b759 - 0.0170178817407898*m.b760 - 0.0210211504274062*m.b761
                          - 0.026590440219984*m.b762 - 0.0328776781816867*m.b763 - 0.0412590389744193*m.b764
                          - 0.0521982216738517*m.b765 - 0.0663255868459265*m.b766 - 0.0841874260371767*m.b767
                          - 0.106477402905515*m.b768 - 0.131510712726747*m.b769 == 0)

m.c240 = Constraint(expr=   m.x124 - 0.000201061929829747*m.b770 - 0.000326851299679482*m.b771
                          - 0.000530929158456675*m.b772 - 0.000834689752132272*m.b773 - 0.00130740519871793*m.b774
                          - 0.00207499053176952*m.b775 - 0.00296091966008184*m.b776 - 0.00425447043519744*m.b777
                          - 0.00636172512351933*m.b778 - 0.0082033581529802*m.b779 - 0.0103147597436048*m.b780
                          - 0.0134370944342281*m.b781 - 0.0170178817407898*m.b782 - 0.0210211504274062*m.b783
                          - 0.026590440219984*m.b784 - 0.0328776781816867*m.b785 - 0.0412590389744193*m.b786
                          - 0.0521982216738517*m.b787 - 0.0663255868459265*m.b788 - 0.0841874260371767*m.b789
                          - 0.106477402905515*m.b790 - 0.131510712726747*m.b791 == 0)

m.c241 = Constraint(expr=   m.x125 - 0.000201061929829747*m.b792 - 0.000326851299679482*m.b793
                          - 0.000530929158456675*m.b794 - 0.000834689752132272*m.b795 - 0.00130740519871793*m.b796
                          - 0.00207499053176952*m.b797 - 0.00296091966008184*m.b798 - 0.00425447043519744*m.b799
                          - 0.00636172512351933*m.b800 - 0.0082033581529802*m.b801 - 0.0103147597436048*m.b802
                          - 0.0134370944342281*m.b803 - 0.0170178817407898*m.b804 - 0.0210211504274062*m.b805
                          - 0.026590440219984*m.b806 - 0.0328776781816867*m.b807 - 0.0412590389744193*m.b808
                          - 0.0521982216738517*m.b809 - 0.0663255868459265*m.b810 - 0.0841874260371767*m.b811
                          - 0.106477402905515*m.b812 - 0.131510712726747*m.b813 == 0)

m.c242 = Constraint(expr=   m.x126 - 0.000201061929829747*m.b814 - 0.000326851299679482*m.b815
                          - 0.000530929158456675*m.b816 - 0.000834689752132272*m.b817 - 0.00130740519871793*m.b818
                          - 0.00207499053176952*m.b819 - 0.00296091966008184*m.b820 - 0.00425447043519744*m.b821
                          - 0.00636172512351933*m.b822 - 0.0082033581529802*m.b823 - 0.0103147597436048*m.b824
                          - 0.0134370944342281*m.b825 - 0.0170178817407898*m.b826 - 0.0210211504274062*m.b827
                          - 0.026590440219984*m.b828 - 0.0328776781816867*m.b829 - 0.0412590389744193*m.b830
                          - 0.0521982216738517*m.b831 - 0.0663255868459265*m.b832 - 0.0841874260371767*m.b833
                          - 0.106477402905515*m.b834 - 0.131510712726747*m.b835 == 0)

m.c243 = Constraint(expr=   m.x127 - 0.000201061929829747*m.b836 - 0.000326851299679482*m.b837
                          - 0.000530929158456675*m.b838 - 0.000834689752132272*m.b839 - 0.00130740519871793*m.b840
                          - 0.00207499053176952*m.b841 - 0.00296091966008184*m.b842 - 0.00425447043519744*m.b843
                          - 0.00636172512351933*m.b844 - 0.0082033581529802*m.b845 - 0.0103147597436048*m.b846
                          - 0.0134370944342281*m.b847 - 0.0170178817407898*m.b848 - 0.0210211504274062*m.b849
                          - 0.026590440219984*m.b850 - 0.0328776781816867*m.b851 - 0.0412590389744193*m.b852
                          - 0.0521982216738517*m.b853 - 0.0663255868459265*m.b854 - 0.0841874260371767*m.b855
                          - 0.106477402905515*m.b856 - 0.131510712726747*m.b857 == 0)

m.c244 = Constraint(expr=   m.x128 - 0.000201061929829747*m.b858 - 0.000326851299679482*m.b859
                          - 0.000530929158456675*m.b860 - 0.000834689752132272*m.b861 - 0.00130740519871793*m.b862
                          - 0.00207499053176952*m.b863 - 0.00296091966008184*m.b864 - 0.00425447043519744*m.b865
                          - 0.00636172512351933*m.b866 - 0.0082033581529802*m.b867 - 0.0103147597436048*m.b868
                          - 0.0134370944342281*m.b869 - 0.0170178817407898*m.b870 - 0.0210211504274062*m.b871
                          - 0.026590440219984*m.b872 - 0.0328776781816867*m.b873 - 0.0412590389744193*m.b874
                          - 0.0521982216738517*m.b875 - 0.0663255868459265*m.b876 - 0.0841874260371767*m.b877
                          - 0.106477402905515*m.b878 - 0.131510712726747*m.b879 == 0)

m.c245 = Constraint(expr=   m.x129 - 0.000201061929829747*m.b880 - 0.000326851299679482*m.b881
                          - 0.000530929158456675*m.b882 - 0.000834689752132272*m.b883 - 0.00130740519871793*m.b884
                          - 0.00207499053176952*m.b885 - 0.00296091966008184*m.b886 - 0.00425447043519744*m.b887
                          - 0.00636172512351933*m.b888 - 0.0082033581529802*m.b889 - 0.0103147597436048*m.b890
                          - 0.0134370944342281*m.b891 - 0.0170178817407898*m.b892 - 0.0210211504274062*m.b893
                          - 0.026590440219984*m.b894 - 0.0328776781816867*m.b895 - 0.0412590389744193*m.b896
                          - 0.0521982216738517*m.b897 - 0.0663255868459265*m.b898 - 0.0841874260371767*m.b899
                          - 0.106477402905515*m.b900 - 0.131510712726747*m.b901 == 0)

m.c246 = Constraint(expr=   m.x130 - 0.000201061929829747*m.b902 - 0.000326851299679482*m.b903
                          - 0.000530929158456675*m.b904 - 0.000834689752132272*m.b905 - 0.00130740519871793*m.b906
                          - 0.00207499053176952*m.b907 - 0.00296091966008184*m.b908 - 0.00425447043519744*m.b909
                          - 0.00636172512351933*m.b910 - 0.0082033581529802*m.b911 - 0.0103147597436048*m.b912
                          - 0.0134370944342281*m.b913 - 0.0170178817407898*m.b914 - 0.0210211504274062*m.b915
                          - 0.026590440219984*m.b916 - 0.0328776781816867*m.b917 - 0.0412590389744193*m.b918
                          - 0.0521982216738517*m.b919 - 0.0663255868459265*m.b920 - 0.0841874260371767*m.b921
                          - 0.106477402905515*m.b922 - 0.131510712726747*m.b923 == 0)

m.c247 = Constraint(expr=   m.x131 - 0.000201061929829747*m.b924 - 0.000326851299679482*m.b925
                          - 0.000530929158456675*m.b926 - 0.000834689752132272*m.b927 - 0.00130740519871793*m.b928
                          - 0.00207499053176952*m.b929 - 0.00296091966008184*m.b930 - 0.00425447043519744*m.b931
                          - 0.00636172512351933*m.b932 - 0.0082033581529802*m.b933 - 0.0103147597436048*m.b934
                          - 0.0134370944342281*m.b935 - 0.0170178817407898*m.b936 - 0.0210211504274062*m.b937
                          - 0.026590440219984*m.b938 - 0.0328776781816867*m.b939 - 0.0412590389744193*m.b940
                          - 0.0521982216738517*m.b941 - 0.0663255868459265*m.b942 - 0.0841874260371767*m.b943
                          - 0.106477402905515*m.b944 - 0.131510712726747*m.b945 == 0)

m.c248 = Constraint(expr=   m.x132 - 0.000201061929829747*m.b946 - 0.000326851299679482*m.b947
                          - 0.000530929158456675*m.b948 - 0.000834689752132272*m.b949 - 0.00130740519871793*m.b950
                          - 0.00207499053176952*m.b951 - 0.00296091966008184*m.b952 - 0.00425447043519744*m.b953
                          - 0.00636172512351933*m.b954 - 0.0082033581529802*m.b955 - 0.0103147597436048*m.b956
                          - 0.0134370944342281*m.b957 - 0.0170178817407898*m.b958 - 0.0210211504274062*m.b959
                          - 0.026590440219984*m.b960 - 0.0328776781816867*m.b961 - 0.0412590389744193*m.b962
                          - 0.0521982216738517*m.b963 - 0.0663255868459265*m.b964 - 0.0841874260371767*m.b965
                          - 0.106477402905515*m.b966 - 0.131510712726747*m.b967 == 0)

m.c249 = Constraint(expr=   m.x133 - 0.000201061929829747*m.b968 - 0.000326851299679482*m.b969
                          - 0.000530929158456675*m.b970 - 0.000834689752132272*m.b971 - 0.00130740519871793*m.b972
                          - 0.00207499053176952*m.b973 - 0.00296091966008184*m.b974 - 0.00425447043519744*m.b975
                          - 0.00636172512351933*m.b976 - 0.0082033581529802*m.b977 - 0.0103147597436048*m.b978
                          - 0.0134370944342281*m.b979 - 0.0170178817407898*m.b980 - 0.0210211504274062*m.b981
                          - 0.026590440219984*m.b982 - 0.0328776781816867*m.b983 - 0.0412590389744193*m.b984
                          - 0.0521982216738517*m.b985 - 0.0663255868459265*m.b986 - 0.0841874260371767*m.b987
                          - 0.106477402905515*m.b988 - 0.131510712726747*m.b989 == 0)

m.c250 = Constraint(expr=   m.x134 - 0.000201061929829747*m.b990 - 0.000326851299679482*m.b991
                          - 0.000530929158456675*m.b992 - 0.000834689752132272*m.b993 - 0.00130740519871793*m.b994
                          - 0.00207499053176952*m.b995 - 0.00296091966008184*m.b996 - 0.00425447043519744*m.b997
                          - 0.00636172512351933*m.b998 - 0.0082033581529802*m.b999 - 0.0103147597436048*m.b1000
                          - 0.0134370944342281*m.b1001 - 0.0170178817407898*m.b1002 - 0.0210211504274062*m.b1003
                          - 0.026590440219984*m.b1004 - 0.0328776781816867*m.b1005 - 0.0412590389744193*m.b1006
                          - 0.0521982216738517*m.b1007 - 0.0663255868459265*m.b1008 - 0.0841874260371767*m.b1009
                          - 0.106477402905515*m.b1010 - 0.131510712726747*m.b1011 == 0)

m.c251 = Constraint(expr=   m.x135 - 0.000201061929829747*m.b1012 - 0.000326851299679482*m.b1013
                          - 0.000530929158456675*m.b1014 - 0.000834689752132272*m.b1015 - 0.00130740519871793*m.b1016
                          - 0.00207499053176952*m.b1017 - 0.00296091966008184*m.b1018 - 0.00425447043519744*m.b1019
                          - 0.00636172512351933*m.b1020 - 0.0082033581529802*m.b1021 - 0.0103147597436048*m.b1022
                          - 0.0134370944342281*m.b1023 - 0.0170178817407898*m.b1024 - 0.0210211504274062*m.b1025
                          - 0.026590440219984*m.b1026 - 0.0328776781816867*m.b1027 - 0.0412590389744193*m.b1028
                          - 0.0521982216738517*m.b1029 - 0.0663255868459265*m.b1030 - 0.0841874260371767*m.b1031
                          - 0.106477402905515*m.b1032 - 0.131510712726747*m.b1033 == 0)

m.c252 = Constraint(expr=   m.x136 - 0.000201061929829747*m.b1034 - 0.000326851299679482*m.b1035
                          - 0.000530929158456675*m.b1036 - 0.000834689752132272*m.b1037 - 0.00130740519871793*m.b1038
                          - 0.00207499053176952*m.b1039 - 0.00296091966008184*m.b1040 - 0.00425447043519744*m.b1041
                          - 0.00636172512351933*m.b1042 - 0.0082033581529802*m.b1043 - 0.0103147597436048*m.b1044
                          - 0.0134370944342281*m.b1045 - 0.0170178817407898*m.b1046 - 0.0210211504274062*m.b1047
                          - 0.026590440219984*m.b1048 - 0.0328776781816867*m.b1049 - 0.0412590389744193*m.b1050
                          - 0.0521982216738517*m.b1051 - 0.0663255868459265*m.b1052 - 0.0841874260371767*m.b1053
                          - 0.106477402905515*m.b1054 - 0.131510712726747*m.b1055 == 0)

m.c253 = Constraint(expr=   m.x137 - 0.000201061929829747*m.b1056 - 0.000326851299679482*m.b1057
                          - 0.000530929158456675*m.b1058 - 0.000834689752132272*m.b1059 - 0.00130740519871793*m.b1060
                          - 0.00207499053176952*m.b1061 - 0.00296091966008184*m.b1062 - 0.00425447043519744*m.b1063
                          - 0.00636172512351933*m.b1064 - 0.0082033581529802*m.b1065 - 0.0103147597436048*m.b1066
                          - 0.0134370944342281*m.b1067 - 0.0170178817407898*m.b1068 - 0.0210211504274062*m.b1069
                          - 0.026590440219984*m.b1070 - 0.0328776781816867*m.b1071 - 0.0412590389744193*m.b1072
                          - 0.0521982216738517*m.b1073 - 0.0663255868459265*m.b1074 - 0.0841874260371767*m.b1075
                          - 0.106477402905515*m.b1076 - 0.131510712726747*m.b1077 == 0)

m.c254 = Constraint(expr=   m.x138 - 0.000201061929829747*m.b1078 - 0.000326851299679482*m.b1079
                          - 0.000530929158456675*m.b1080 - 0.000834689752132272*m.b1081 - 0.00130740519871793*m.b1082
                          - 0.00207499053176952*m.b1083 - 0.00296091966008184*m.b1084 - 0.00425447043519744*m.b1085
                          - 0.00636172512351933*m.b1086 - 0.0082033581529802*m.b1087 - 0.0103147597436048*m.b1088
                          - 0.0134370944342281*m.b1089 - 0.0170178817407898*m.b1090 - 0.0210211504274062*m.b1091
                          - 0.026590440219984*m.b1092 - 0.0328776781816867*m.b1093 - 0.0412590389744193*m.b1094
                          - 0.0521982216738517*m.b1095 - 0.0663255868459265*m.b1096 - 0.0841874260371767*m.b1097
                          - 0.106477402905515*m.b1098 - 0.131510712726747*m.b1099 == 0)

m.c255 = Constraint(expr=   m.x139 - 0.000201061929829747*m.b1100 - 0.000326851299679482*m.b1101
                          - 0.000530929158456675*m.b1102 - 0.000834689752132272*m.b1103 - 0.00130740519871793*m.b1104
                          - 0.00207499053176952*m.b1105 - 0.00296091966008184*m.b1106 - 0.00425447043519744*m.b1107
                          - 0.00636172512351933*m.b1108 - 0.0082033581529802*m.b1109 - 0.0103147597436048*m.b1110
                          - 0.0134370944342281*m.b1111 - 0.0170178817407898*m.b1112 - 0.0210211504274062*m.b1113
                          - 0.026590440219984*m.b1114 - 0.0328776781816867*m.b1115 - 0.0412590389744193*m.b1116
                          - 0.0521982216738517*m.b1117 - 0.0663255868459265*m.b1118 - 0.0841874260371767*m.b1119
                          - 0.106477402905515*m.b1120 - 0.131510712726747*m.b1121 == 0)

m.c256 = Constraint(expr=   m.x140 - 0.000201061929829747*m.b1122 - 0.000326851299679482*m.b1123
                          - 0.000530929158456675*m.b1124 - 0.000834689752132272*m.b1125 - 0.00130740519871793*m.b1126
                          - 0.00207499053176952*m.b1127 - 0.00296091966008184*m.b1128 - 0.00425447043519744*m.b1129
                          - 0.00636172512351933*m.b1130 - 0.0082033581529802*m.b1131 - 0.0103147597436048*m.b1132
                          - 0.0134370944342281*m.b1133 - 0.0170178817407898*m.b1134 - 0.0210211504274062*m.b1135
                          - 0.026590440219984*m.b1136 - 0.0328776781816867*m.b1137 - 0.0412590389744193*m.b1138
                          - 0.0521982216738517*m.b1139 - 0.0663255868459265*m.b1140 - 0.0841874260371767*m.b1141
                          - 0.106477402905515*m.b1142 - 0.131510712726747*m.b1143 == 0)

m.c257 = Constraint(expr=   m.x141 - 0.000201061929829747*m.b1144 - 0.000326851299679482*m.b1145
                          - 0.000530929158456675*m.b1146 - 0.000834689752132272*m.b1147 - 0.00130740519871793*m.b1148
                          - 0.00207499053176952*m.b1149 - 0.00296091966008184*m.b1150 - 0.00425447043519744*m.b1151
                          - 0.00636172512351933*m.b1152 - 0.0082033581529802*m.b1153 - 0.0103147597436048*m.b1154
                          - 0.0134370944342281*m.b1155 - 0.0170178817407898*m.b1156 - 0.0210211504274062*m.b1157
                          - 0.026590440219984*m.b1158 - 0.0328776781816867*m.b1159 - 0.0412590389744193*m.b1160
                          - 0.0521982216738517*m.b1161 - 0.0663255868459265*m.b1162 - 0.0841874260371767*m.b1163
                          - 0.106477402905515*m.b1164 - 0.131510712726747*m.b1165 == 0)

m.c258 = Constraint(expr=   m.x142 - 0.000201061929829747*m.b1166 - 0.000326851299679482*m.b1167
                          - 0.000530929158456675*m.b1168 - 0.000834689752132272*m.b1169 - 0.00130740519871793*m.b1170
                          - 0.00207499053176952*m.b1171 - 0.00296091966008184*m.b1172 - 0.00425447043519744*m.b1173
                          - 0.00636172512351933*m.b1174 - 0.0082033581529802*m.b1175 - 0.0103147597436048*m.b1176
                          - 0.0134370944342281*m.b1177 - 0.0170178817407898*m.b1178 - 0.0210211504274062*m.b1179
                          - 0.026590440219984*m.b1180 - 0.0328776781816867*m.b1181 - 0.0412590389744193*m.b1182
                          - 0.0521982216738517*m.b1183 - 0.0663255868459265*m.b1184 - 0.0841874260371767*m.b1185
                          - 0.106477402905515*m.b1186 - 0.131510712726747*m.b1187 == 0)

m.c259 = Constraint(expr=   m.x143 - 0.000201061929829747*m.b1188 - 0.000326851299679482*m.b1189
                          - 0.000530929158456675*m.b1190 - 0.000834689752132272*m.b1191 - 0.00130740519871793*m.b1192
                          - 0.00207499053176952*m.b1193 - 0.00296091966008184*m.b1194 - 0.00425447043519744*m.b1195
                          - 0.00636172512351933*m.b1196 - 0.0082033581529802*m.b1197 - 0.0103147597436048*m.b1198
                          - 0.0134370944342281*m.b1199 - 0.0170178817407898*m.b1200 - 0.0210211504274062*m.b1201
                          - 0.026590440219984*m.b1202 - 0.0328776781816867*m.b1203 - 0.0412590389744193*m.b1204
                          - 0.0521982216738517*m.b1205 - 0.0663255868459265*m.b1206 - 0.0841874260371767*m.b1207
                          - 0.106477402905515*m.b1208 - 0.131510712726747*m.b1209 == 0)

m.c260 = Constraint(expr=   m.x144 - 0.000201061929829747*m.b1210 - 0.000326851299679482*m.b1211
                          - 0.000530929158456675*m.b1212 - 0.000834689752132272*m.b1213 - 0.00130740519871793*m.b1214
                          - 0.00207499053176952*m.b1215 - 0.00296091966008184*m.b1216 - 0.00425447043519744*m.b1217
                          - 0.00636172512351933*m.b1218 - 0.0082033581529802*m.b1219 - 0.0103147597436048*m.b1220
                          - 0.0134370944342281*m.b1221 - 0.0170178817407898*m.b1222 - 0.0210211504274062*m.b1223
                          - 0.026590440219984*m.b1224 - 0.0328776781816867*m.b1225 - 0.0412590389744193*m.b1226
                          - 0.0521982216738517*m.b1227 - 0.0663255868459265*m.b1228 - 0.0841874260371767*m.b1229
                          - 0.106477402905515*m.b1230 - 0.131510712726747*m.b1231 == 0)

m.c261 = Constraint(expr=   m.x145 - 0.000201061929829747*m.b1232 - 0.000326851299679482*m.b1233
                          - 0.000530929158456675*m.b1234 - 0.000834689752132272*m.b1235 - 0.00130740519871793*m.b1236
                          - 0.00207499053176952*m.b1237 - 0.00296091966008184*m.b1238 - 0.00425447043519744*m.b1239
                          - 0.00636172512351933*m.b1240 - 0.0082033581529802*m.b1241 - 0.0103147597436048*m.b1242
                          - 0.0134370944342281*m.b1243 - 0.0170178817407898*m.b1244 - 0.0210211504274062*m.b1245
                          - 0.026590440219984*m.b1246 - 0.0328776781816867*m.b1247 - 0.0412590389744193*m.b1248
                          - 0.0521982216738517*m.b1249 - 0.0663255868459265*m.b1250 - 0.0841874260371767*m.b1251
                          - 0.106477402905515*m.b1252 - 0.131510712726747*m.b1253 == 0)

m.c262 = Constraint(expr=   m.x146 - 0.000201061929829747*m.b1254 - 0.000326851299679482*m.b1255
                          - 0.000530929158456675*m.b1256 - 0.000834689752132272*m.b1257 - 0.00130740519871793*m.b1258
                          - 0.00207499053176952*m.b1259 - 0.00296091966008184*m.b1260 - 0.00425447043519744*m.b1261
                          - 0.00636172512351933*m.b1262 - 0.0082033581529802*m.b1263 - 0.0103147597436048*m.b1264
                          - 0.0134370944342281*m.b1265 - 0.0170178817407898*m.b1266 - 0.0210211504274062*m.b1267
                          - 0.026590440219984*m.b1268 - 0.0328776781816867*m.b1269 - 0.0412590389744193*m.b1270
                          - 0.0521982216738517*m.b1271 - 0.0663255868459265*m.b1272 - 0.0841874260371767*m.b1273
                          - 0.106477402905515*m.b1274 - 0.131510712726747*m.b1275 == 0)

m.c263 = Constraint(expr=   m.x147 - 0.000201061929829747*m.b1276 - 0.000326851299679482*m.b1277
                          - 0.000530929158456675*m.b1278 - 0.000834689752132272*m.b1279 - 0.00130740519871793*m.b1280
                          - 0.00207499053176952*m.b1281 - 0.00296091966008184*m.b1282 - 0.00425447043519744*m.b1283
                          - 0.00636172512351933*m.b1284 - 0.0082033581529802*m.b1285 - 0.0103147597436048*m.b1286
                          - 0.0134370944342281*m.b1287 - 0.0170178817407898*m.b1288 - 0.0210211504274062*m.b1289
                          - 0.026590440219984*m.b1290 - 0.0328776781816867*m.b1291 - 0.0412590389744193*m.b1292
                          - 0.0521982216738517*m.b1293 - 0.0663255868459265*m.b1294 - 0.0841874260371767*m.b1295
                          - 0.106477402905515*m.b1296 - 0.131510712726747*m.b1297 == 0)

m.c264 = Constraint(expr=   m.x148 - 0.000201061929829747*m.b1298 - 0.000326851299679482*m.b1299
                          - 0.000530929158456675*m.b1300 - 0.000834689752132272*m.b1301 - 0.00130740519871793*m.b1302
                          - 0.00207499053176952*m.b1303 - 0.00296091966008184*m.b1304 - 0.00425447043519744*m.b1305
                          - 0.00636172512351933*m.b1306 - 0.0082033581529802*m.b1307 - 0.0103147597436048*m.b1308
                          - 0.0134370944342281*m.b1309 - 0.0170178817407898*m.b1310 - 0.0210211504274062*m.b1311
                          - 0.026590440219984*m.b1312 - 0.0328776781816867*m.b1313 - 0.0412590389744193*m.b1314
                          - 0.0521982216738517*m.b1315 - 0.0663255868459265*m.b1316 - 0.0841874260371767*m.b1317
                          - 0.106477402905515*m.b1318 - 0.131510712726747*m.b1319 == 0)

m.c265 = Constraint(expr=   m.x149 - 0.000201061929829747*m.b1320 - 0.000326851299679482*m.b1321
                          - 0.000530929158456675*m.b1322 - 0.000834689752132272*m.b1323 - 0.00130740519871793*m.b1324
                          - 0.00207499053176952*m.b1325 - 0.00296091966008184*m.b1326 - 0.00425447043519744*m.b1327
                          - 0.00636172512351933*m.b1328 - 0.0082033581529802*m.b1329 - 0.0103147597436048*m.b1330
                          - 0.0134370944342281*m.b1331 - 0.0170178817407898*m.b1332 - 0.0210211504274062*m.b1333
                          - 0.026590440219984*m.b1334 - 0.0328776781816867*m.b1335 - 0.0412590389744193*m.b1336
                          - 0.0521982216738517*m.b1337 - 0.0663255868459265*m.b1338 - 0.0841874260371767*m.b1339
                          - 0.106477402905515*m.b1340 - 0.131510712726747*m.b1341 == 0)

m.c266 = Constraint(expr=   m.x150 - 0.000201061929829747*m.b1342 - 0.000326851299679482*m.b1343
                          - 0.000530929158456675*m.b1344 - 0.000834689752132272*m.b1345 - 0.00130740519871793*m.b1346
                          - 0.00207499053176952*m.b1347 - 0.00296091966008184*m.b1348 - 0.00425447043519744*m.b1349
                          - 0.00636172512351933*m.b1350 - 0.0082033581529802*m.b1351 - 0.0103147597436048*m.b1352
                          - 0.0134370944342281*m.b1353 - 0.0170178817407898*m.b1354 - 0.0210211504274062*m.b1355
                          - 0.026590440219984*m.b1356 - 0.0328776781816867*m.b1357 - 0.0412590389744193*m.b1358
                          - 0.0521982216738517*m.b1359 - 0.0663255868459265*m.b1360 - 0.0841874260371767*m.b1361
                          - 0.106477402905515*m.b1362 - 0.131510712726747*m.b1363 == 0)

m.c267 = Constraint(expr=   m.x151 - 0.000201061929829747*m.b1364 - 0.000326851299679482*m.b1365
                          - 0.000530929158456675*m.b1366 - 0.000834689752132272*m.b1367 - 0.00130740519871793*m.b1368
                          - 0.00207499053176952*m.b1369 - 0.00296091966008184*m.b1370 - 0.00425447043519744*m.b1371
                          - 0.00636172512351933*m.b1372 - 0.0082033581529802*m.b1373 - 0.0103147597436048*m.b1374
                          - 0.0134370944342281*m.b1375 - 0.0170178817407898*m.b1376 - 0.0210211504274062*m.b1377
                          - 0.026590440219984*m.b1378 - 0.0328776781816867*m.b1379 - 0.0412590389744193*m.b1380
                          - 0.0521982216738517*m.b1381 - 0.0663255868459265*m.b1382 - 0.0841874260371767*m.b1383
                          - 0.106477402905515*m.b1384 - 0.131510712726747*m.b1385 == 0)

m.c268 = Constraint(expr=   m.x152 - 0.000201061929829747*m.b1386 - 0.000326851299679482*m.b1387
                          - 0.000530929158456675*m.b1388 - 0.000834689752132272*m.b1389 - 0.00130740519871793*m.b1390
                          - 0.00207499053176952*m.b1391 - 0.00296091966008184*m.b1392 - 0.00425447043519744*m.b1393
                          - 0.00636172512351933*m.b1394 - 0.0082033581529802*m.b1395 - 0.0103147597436048*m.b1396
                          - 0.0134370944342281*m.b1397 - 0.0170178817407898*m.b1398 - 0.0210211504274062*m.b1399
                          - 0.026590440219984*m.b1400 - 0.0328776781816867*m.b1401 - 0.0412590389744193*m.b1402
                          - 0.0521982216738517*m.b1403 - 0.0663255868459265*m.b1404 - 0.0841874260371767*m.b1405
                          - 0.106477402905515*m.b1406 - 0.131510712726747*m.b1407 == 0)

m.c269 = Constraint(expr=   m.x153 - 0.000201061929829747*m.b1408 - 0.000326851299679482*m.b1409
                          - 0.000530929158456675*m.b1410 - 0.000834689752132272*m.b1411 - 0.00130740519871793*m.b1412
                          - 0.00207499053176952*m.b1413 - 0.00296091966008184*m.b1414 - 0.00425447043519744*m.b1415
                          - 0.00636172512351933*m.b1416 - 0.0082033581529802*m.b1417 - 0.0103147597436048*m.b1418
                          - 0.0134370944342281*m.b1419 - 0.0170178817407898*m.b1420 - 0.0210211504274062*m.b1421
                          - 0.026590440219984*m.b1422 - 0.0328776781816867*m.b1423 - 0.0412590389744193*m.b1424
                          - 0.0521982216738517*m.b1425 - 0.0663255868459265*m.b1426 - 0.0841874260371767*m.b1427
                          - 0.106477402905515*m.b1428 - 0.131510712726747*m.b1429 == 0)

m.c270 = Constraint(expr=   m.b154 + m.b155 + m.b156 + m.b157 + m.b158 + m.b159 + m.b160 + m.b161 + m.b162 + m.b163
                          + m.b164 + m.b165 + m.b166 + m.b167 + m.b168 + m.b169 + m.b170 + m.b171 + m.b172 + m.b173
                          + m.b174 + m.b175 == 1)

m.c271 = Constraint(expr=   m.b176 + m.b177 + m.b178 + m.b179 + m.b180 + m.b181 + m.b182 + m.b183 + m.b184 + m.b185
                          + m.b186 + m.b187 + m.b188 + m.b189 + m.b190 + m.b191 + m.b192 + m.b193 + m.b194 + m.b195
                          + m.b196 + m.b197 == 1)

m.c272 = Constraint(expr=   m.b198 + m.b199 + m.b200 + m.b201 + m.b202 + m.b203 + m.b204 + m.b205 + m.b206 + m.b207
                          + m.b208 + m.b209 + m.b210 + m.b211 + m.b212 + m.b213 + m.b214 + m.b215 + m.b216 + m.b217
                          + m.b218 + m.b219 == 1)

m.c273 = Constraint(expr=   m.b220 + m.b221 + m.b222 + m.b223 + m.b224 + m.b225 + m.b226 + m.b227 + m.b228 + m.b229
                          + m.b230 + m.b231 + m.b232 + m.b233 + m.b234 + m.b235 + m.b236 + m.b237 + m.b238 + m.b239
                          + m.b240 + m.b241 == 1)

m.c274 = Constraint(expr=   m.b242 + m.b243 + m.b244 + m.b245 + m.b246 + m.b247 + m.b248 + m.b249 + m.b250 + m.b251
                          + m.b252 + m.b253 + m.b254 + m.b255 + m.b256 + m.b257 + m.b258 + m.b259 + m.b260 + m.b261
                          + m.b262 + m.b263 == 1)

m.c275 = Constraint(expr=   m.b264 + m.b265 + m.b266 + m.b267 + m.b268 + m.b269 + m.b270 + m.b271 + m.b272 + m.b273
                          + m.b274 + m.b275 + m.b276 + m.b277 + m.b278 + m.b279 + m.b280 + m.b281 + m.b282 + m.b283
                          + m.b284 + m.b285 == 1)

m.c276 = Constraint(expr=   m.b286 + m.b287 + m.b288 + m.b289 + m.b290 + m.b291 + m.b292 + m.b293 + m.b294 + m.b295
                          + m.b296 + m.b297 + m.b298 + m.b299 + m.b300 + m.b301 + m.b302 + m.b303 + m.b304 + m.b305
                          + m.b306 + m.b307 == 1)

m.c277 = Constraint(expr=   m.b308 + m.b309 + m.b310 + m.b311 + m.b312 + m.b313 + m.b314 + m.b315 + m.b316 + m.b317
                          + m.b318 + m.b319 + m.b320 + m.b321 + m.b322 + m.b323 + m.b324 + m.b325 + m.b326 + m.b327
                          + m.b328 + m.b329 == 1)

m.c278 = Constraint(expr=   m.b330 + m.b331 + m.b332 + m.b333 + m.b334 + m.b335 + m.b336 + m.b337 + m.b338 + m.b339
                          + m.b340 + m.b341 + m.b342 + m.b343 + m.b344 + m.b345 + m.b346 + m.b347 + m.b348 + m.b349
                          + m.b350 + m.b351 == 1)

m.c279 = Constraint(expr=   m.b352 + m.b353 + m.b354 + m.b355 + m.b356 + m.b357 + m.b358 + m.b359 + m.b360 + m.b361
                          + m.b362 + m.b363 + m.b364 + m.b365 + m.b366 + m.b367 + m.b368 + m.b369 + m.b370 + m.b371
                          + m.b372 + m.b373 == 1)

m.c280 = Constraint(expr=   m.b374 + m.b375 + m.b376 + m.b377 + m.b378 + m.b379 + m.b380 + m.b381 + m.b382 + m.b383
                          + m.b384 + m.b385 + m.b386 + m.b387 + m.b388 + m.b389 + m.b390 + m.b391 + m.b392 + m.b393
                          + m.b394 + m.b395 == 1)

m.c281 = Constraint(expr=   m.b396 + m.b397 + m.b398 + m.b399 + m.b400 + m.b401 + m.b402 + m.b403 + m.b404 + m.b405
                          + m.b406 + m.b407 + m.b408 + m.b409 + m.b410 + m.b411 + m.b412 + m.b413 + m.b414 + m.b415
                          + m.b416 + m.b417 == 1)

m.c282 = Constraint(expr=   m.b418 + m.b419 + m.b420 + m.b421 + m.b422 + m.b423 + m.b424 + m.b425 + m.b426 + m.b427
                          + m.b428 + m.b429 + m.b430 + m.b431 + m.b432 + m.b433 + m.b434 + m.b435 + m.b436 + m.b437
                          + m.b438 + m.b439 == 1)

m.c283 = Constraint(expr=   m.b440 + m.b441 + m.b442 + m.b443 + m.b444 + m.b445 + m.b446 + m.b447 + m.b448 + m.b449
                          + m.b450 + m.b451 + m.b452 + m.b453 + m.b454 + m.b455 + m.b456 + m.b457 + m.b458 + m.b459
                          + m.b460 + m.b461 == 1)

m.c284 = Constraint(expr=   m.b462 + m.b463 + m.b464 + m.b465 + m.b466 + m.b467 + m.b468 + m.b469 + m.b470 + m.b471
                          + m.b472 + m.b473 + m.b474 + m.b475 + m.b476 + m.b477 + m.b478 + m.b479 + m.b480 + m.b481
                          + m.b482 + m.b483 == 1)

m.c285 = Constraint(expr=   m.b484 + m.b485 + m.b486 + m.b487 + m.b488 + m.b489 + m.b490 + m.b491 + m.b492 + m.b493
                          + m.b494 + m.b495 + m.b496 + m.b497 + m.b498 + m.b499 + m.b500 + m.b501 + m.b502 + m.b503
                          + m.b504 + m.b505 == 1)

m.c286 = Constraint(expr=   m.b506 + m.b507 + m.b508 + m.b509 + m.b510 + m.b511 + m.b512 + m.b513 + m.b514 + m.b515
                          + m.b516 + m.b517 + m.b518 + m.b519 + m.b520 + m.b521 + m.b522 + m.b523 + m.b524 + m.b525
                          + m.b526 + m.b527 == 1)

m.c287 = Constraint(expr=   m.b528 + m.b529 + m.b530 + m.b531 + m.b532 + m.b533 + m.b534 + m.b535 + m.b536 + m.b537
                          + m.b538 + m.b539 + m.b540 + m.b541 + m.b542 + m.b543 + m.b544 + m.b545 + m.b546 + m.b547
                          + m.b548 + m.b549 == 1)

m.c288 = Constraint(expr=   m.b550 + m.b551 + m.b552 + m.b553 + m.b554 + m.b555 + m.b556 + m.b557 + m.b558 + m.b559
                          + m.b560 + m.b561 + m.b562 + m.b563 + m.b564 + m.b565 + m.b566 + m.b567 + m.b568 + m.b569
                          + m.b570 + m.b571 == 1)

m.c289 = Constraint(expr=   m.b572 + m.b573 + m.b574 + m.b575 + m.b576 + m.b577 + m.b578 + m.b579 + m.b580 + m.b581
                          + m.b582 + m.b583 + m.b584 + m.b585 + m.b586 + m.b587 + m.b588 + m.b589 + m.b590 + m.b591
                          + m.b592 + m.b593 == 1)

m.c290 = Constraint(expr=   m.b594 + m.b595 + m.b596 + m.b597 + m.b598 + m.b599 + m.b600 + m.b601 + m.b602 + m.b603
                          + m.b604 + m.b605 + m.b606 + m.b607 + m.b608 + m.b609 + m.b610 + m.b611 + m.b612 + m.b613
                          + m.b614 + m.b615 == 1)

m.c291 = Constraint(expr=   m.b616 + m.b617 + m.b618 + m.b619 + m.b620 + m.b621 + m.b622 + m.b623 + m.b624 + m.b625
                          + m.b626 + m.b627 + m.b628 + m.b629 + m.b630 + m.b631 + m.b632 + m.b633 + m.b634 + m.b635
                          + m.b636 + m.b637 == 1)

m.c292 = Constraint(expr=   m.b638 + m.b639 + m.b640 + m.b641 + m.b642 + m.b643 + m.b644 + m.b645 + m.b646 + m.b647
                          + m.b648 + m.b649 + m.b650 + m.b651 + m.b652 + m.b653 + m.b654 + m.b655 + m.b656 + m.b657
                          + m.b658 + m.b659 == 1)

m.c293 = Constraint(expr=   m.b660 + m.b661 + m.b662 + m.b663 + m.b664 + m.b665 + m.b666 + m.b667 + m.b668 + m.b669
                          + m.b670 + m.b671 + m.b672 + m.b673 + m.b674 + m.b675 + m.b676 + m.b677 + m.b678 + m.b679
                          + m.b680 + m.b681 == 1)

m.c294 = Constraint(expr=   m.b682 + m.b683 + m.b684 + m.b685 + m.b686 + m.b687 + m.b688 + m.b689 + m.b690 + m.b691
                          + m.b692 + m.b693 + m.b694 + m.b695 + m.b696 + m.b697 + m.b698 + m.b699 + m.b700 + m.b701
                          + m.b702 + m.b703 == 1)

m.c295 = Constraint(expr=   m.b704 + m.b705 + m.b706 + m.b707 + m.b708 + m.b709 + m.b710 + m.b711 + m.b712 + m.b713
                          + m.b714 + m.b715 + m.b716 + m.b717 + m.b718 + m.b719 + m.b720 + m.b721 + m.b722 + m.b723
                          + m.b724 + m.b725 == 1)

m.c296 = Constraint(expr=   m.b726 + m.b727 + m.b728 + m.b729 + m.b730 + m.b731 + m.b732 + m.b733 + m.b734 + m.b735
                          + m.b736 + m.b737 + m.b738 + m.b739 + m.b740 + m.b741 + m.b742 + m.b743 + m.b744 + m.b745
                          + m.b746 + m.b747 == 1)

m.c297 = Constraint(expr=   m.b748 + m.b749 + m.b750 + m.b751 + m.b752 + m.b753 + m.b754 + m.b755 + m.b756 + m.b757
                          + m.b758 + m.b759 + m.b760 + m.b761 + m.b762 + m.b763 + m.b764 + m.b765 + m.b766 + m.b767
                          + m.b768 + m.b769 == 1)

m.c298 = Constraint(expr=   m.b770 + m.b771 + m.b772 + m.b773 + m.b774 + m.b775 + m.b776 + m.b777 + m.b778 + m.b779
                          + m.b780 + m.b781 + m.b782 + m.b783 + m.b784 + m.b785 + m.b786 + m.b787 + m.b788 + m.b789
                          + m.b790 + m.b791 == 1)

m.c299 = Constraint(expr=   m.b792 + m.b793 + m.b794 + m.b795 + m.b796 + m.b797 + m.b798 + m.b799 + m.b800 + m.b801
                          + m.b802 + m.b803 + m.b804 + m.b805 + m.b806 + m.b807 + m.b808 + m.b809 + m.b810 + m.b811
                          + m.b812 + m.b813 == 1)

m.c300 = Constraint(expr=   m.b814 + m.b815 + m.b816 + m.b817 + m.b818 + m.b819 + m.b820 + m.b821 + m.b822 + m.b823
                          + m.b824 + m.b825 + m.b826 + m.b827 + m.b828 + m.b829 + m.b830 + m.b831 + m.b832 + m.b833
                          + m.b834 + m.b835 == 1)

m.c301 = Constraint(expr=   m.b836 + m.b837 + m.b838 + m.b839 + m.b840 + m.b841 + m.b842 + m.b843 + m.b844 + m.b845
                          + m.b846 + m.b847 + m.b848 + m.b849 + m.b850 + m.b851 + m.b852 + m.b853 + m.b854 + m.b855
                          + m.b856 + m.b857 == 1)

m.c302 = Constraint(expr=   m.b858 + m.b859 + m.b860 + m.b861 + m.b862 + m.b863 + m.b864 + m.b865 + m.b866 + m.b867
                          + m.b868 + m.b869 + m.b870 + m.b871 + m.b872 + m.b873 + m.b874 + m.b875 + m.b876 + m.b877
                          + m.b878 + m.b879 == 1)

m.c303 = Constraint(expr=   m.b880 + m.b881 + m.b882 + m.b883 + m.b884 + m.b885 + m.b886 + m.b887 + m.b888 + m.b889
                          + m.b890 + m.b891 + m.b892 + m.b893 + m.b894 + m.b895 + m.b896 + m.b897 + m.b898 + m.b899
                          + m.b900 + m.b901 == 1)

m.c304 = Constraint(expr=   m.b902 + m.b903 + m.b904 + m.b905 + m.b906 + m.b907 + m.b908 + m.b909 + m.b910 + m.b911
                          + m.b912 + m.b913 + m.b914 + m.b915 + m.b916 + m.b917 + m.b918 + m.b919 + m.b920 + m.b921
                          + m.b922 + m.b923 == 1)

m.c305 = Constraint(expr=   m.b924 + m.b925 + m.b926 + m.b927 + m.b928 + m.b929 + m.b930 + m.b931 + m.b932 + m.b933
                          + m.b934 + m.b935 + m.b936 + m.b937 + m.b938 + m.b939 + m.b940 + m.b941 + m.b942 + m.b943
                          + m.b944 + m.b945 == 1)

m.c306 = Constraint(expr=   m.b946 + m.b947 + m.b948 + m.b949 + m.b950 + m.b951 + m.b952 + m.b953 + m.b954 + m.b955
                          + m.b956 + m.b957 + m.b958 + m.b959 + m.b960 + m.b961 + m.b962 + m.b963 + m.b964 + m.b965
                          + m.b966 + m.b967 == 1)

m.c307 = Constraint(expr=   m.b968 + m.b969 + m.b970 + m.b971 + m.b972 + m.b973 + m.b974 + m.b975 + m.b976 + m.b977
                          + m.b978 + m.b979 + m.b980 + m.b981 + m.b982 + m.b983 + m.b984 + m.b985 + m.b986 + m.b987
                          + m.b988 + m.b989 == 1)

m.c308 = Constraint(expr=   m.b990 + m.b991 + m.b992 + m.b993 + m.b994 + m.b995 + m.b996 + m.b997 + m.b998 + m.b999
                          + m.b1000 + m.b1001 + m.b1002 + m.b1003 + m.b1004 + m.b1005 + m.b1006 + m.b1007 + m.b1008
                          + m.b1009 + m.b1010 + m.b1011 == 1)

m.c309 = Constraint(expr=   m.b1012 + m.b1013 + m.b1014 + m.b1015 + m.b1016 + m.b1017 + m.b1018 + m.b1019 + m.b1020
                          + m.b1021 + m.b1022 + m.b1023 + m.b1024 + m.b1025 + m.b1026 + m.b1027 + m.b1028 + m.b1029
                          + m.b1030 + m.b1031 + m.b1032 + m.b1033 == 1)

m.c310 = Constraint(expr=   m.b1034 + m.b1035 + m.b1036 + m.b1037 + m.b1038 + m.b1039 + m.b1040 + m.b1041 + m.b1042
                          + m.b1043 + m.b1044 + m.b1045 + m.b1046 + m.b1047 + m.b1048 + m.b1049 + m.b1050 + m.b1051
                          + m.b1052 + m.b1053 + m.b1054 + m.b1055 == 1)

m.c311 = Constraint(expr=   m.b1056 + m.b1057 + m.b1058 + m.b1059 + m.b1060 + m.b1061 + m.b1062 + m.b1063 + m.b1064
                          + m.b1065 + m.b1066 + m.b1067 + m.b1068 + m.b1069 + m.b1070 + m.b1071 + m.b1072 + m.b1073
                          + m.b1074 + m.b1075 + m.b1076 + m.b1077 == 1)

m.c312 = Constraint(expr=   m.b1078 + m.b1079 + m.b1080 + m.b1081 + m.b1082 + m.b1083 + m.b1084 + m.b1085 + m.b1086
                          + m.b1087 + m.b1088 + m.b1089 + m.b1090 + m.b1091 + m.b1092 + m.b1093 + m.b1094 + m.b1095
                          + m.b1096 + m.b1097 + m.b1098 + m.b1099 == 1)

m.c313 = Constraint(expr=   m.b1100 + m.b1101 + m.b1102 + m.b1103 + m.b1104 + m.b1105 + m.b1106 + m.b1107 + m.b1108
                          + m.b1109 + m.b1110 + m.b1111 + m.b1112 + m.b1113 + m.b1114 + m.b1115 + m.b1116 + m.b1117
                          + m.b1118 + m.b1119 + m.b1120 + m.b1121 == 1)

m.c314 = Constraint(expr=   m.b1122 + m.b1123 + m.b1124 + m.b1125 + m.b1126 + m.b1127 + m.b1128 + m.b1129 + m.b1130
                          + m.b1131 + m.b1132 + m.b1133 + m.b1134 + m.b1135 + m.b1136 + m.b1137 + m.b1138 + m.b1139
                          + m.b1140 + m.b1141 + m.b1142 + m.b1143 == 1)

m.c315 = Constraint(expr=   m.b1144 + m.b1145 + m.b1146 + m.b1147 + m.b1148 + m.b1149 + m.b1150 + m.b1151 + m.b1152
                          + m.b1153 + m.b1154 + m.b1155 + m.b1156 + m.b1157 + m.b1158 + m.b1159 + m.b1160 + m.b1161
                          + m.b1162 + m.b1163 + m.b1164 + m.b1165 == 1)

m.c316 = Constraint(expr=   m.b1166 + m.b1167 + m.b1168 + m.b1169 + m.b1170 + m.b1171 + m.b1172 + m.b1173 + m.b1174
                          + m.b1175 + m.b1176 + m.b1177 + m.b1178 + m.b1179 + m.b1180 + m.b1181 + m.b1182 + m.b1183
                          + m.b1184 + m.b1185 + m.b1186 + m.b1187 == 1)

m.c317 = Constraint(expr=   m.b1188 + m.b1189 + m.b1190 + m.b1191 + m.b1192 + m.b1193 + m.b1194 + m.b1195 + m.b1196
                          + m.b1197 + m.b1198 + m.b1199 + m.b1200 + m.b1201 + m.b1202 + m.b1203 + m.b1204 + m.b1205
                          + m.b1206 + m.b1207 + m.b1208 + m.b1209 == 1)

m.c318 = Constraint(expr=   m.b1210 + m.b1211 + m.b1212 + m.b1213 + m.b1214 + m.b1215 + m.b1216 + m.b1217 + m.b1218
                          + m.b1219 + m.b1220 + m.b1221 + m.b1222 + m.b1223 + m.b1224 + m.b1225 + m.b1226 + m.b1227
                          + m.b1228 + m.b1229 + m.b1230 + m.b1231 == 1)

m.c319 = Constraint(expr=   m.b1232 + m.b1233 + m.b1234 + m.b1235 + m.b1236 + m.b1237 + m.b1238 + m.b1239 + m.b1240
                          + m.b1241 + m.b1242 + m.b1243 + m.b1244 + m.b1245 + m.b1246 + m.b1247 + m.b1248 + m.b1249
                          + m.b1250 + m.b1251 + m.b1252 + m.b1253 == 1)

m.c320 = Constraint(expr=   m.b1254 + m.b1255 + m.b1256 + m.b1257 + m.b1258 + m.b1259 + m.b1260 + m.b1261 + m.b1262
                          + m.b1263 + m.b1264 + m.b1265 + m.b1266 + m.b1267 + m.b1268 + m.b1269 + m.b1270 + m.b1271
                          + m.b1272 + m.b1273 + m.b1274 + m.b1275 == 1)

m.c321 = Constraint(expr=   m.b1276 + m.b1277 + m.b1278 + m.b1279 + m.b1280 + m.b1281 + m.b1282 + m.b1283 + m.b1284
                          + m.b1285 + m.b1286 + m.b1287 + m.b1288 + m.b1289 + m.b1290 + m.b1291 + m.b1292 + m.b1293
                          + m.b1294 + m.b1295 + m.b1296 + m.b1297 == 1)

m.c322 = Constraint(expr=   m.b1298 + m.b1299 + m.b1300 + m.b1301 + m.b1302 + m.b1303 + m.b1304 + m.b1305 + m.b1306
                          + m.b1307 + m.b1308 + m.b1309 + m.b1310 + m.b1311 + m.b1312 + m.b1313 + m.b1314 + m.b1315
                          + m.b1316 + m.b1317 + m.b1318 + m.b1319 == 1)

m.c323 = Constraint(expr=   m.b1320 + m.b1321 + m.b1322 + m.b1323 + m.b1324 + m.b1325 + m.b1326 + m.b1327 + m.b1328
                          + m.b1329 + m.b1330 + m.b1331 + m.b1332 + m.b1333 + m.b1334 + m.b1335 + m.b1336 + m.b1337
                          + m.b1338 + m.b1339 + m.b1340 + m.b1341 == 1)

m.c324 = Constraint(expr=   m.b1342 + m.b1343 + m.b1344 + m.b1345 + m.b1346 + m.b1347 + m.b1348 + m.b1349 + m.b1350
                          + m.b1351 + m.b1352 + m.b1353 + m.b1354 + m.b1355 + m.b1356 + m.b1357 + m.b1358 + m.b1359
                          + m.b1360 + m.b1361 + m.b1362 + m.b1363 == 1)

m.c325 = Constraint(expr=   m.b1364 + m.b1365 + m.b1366 + m.b1367 + m.b1368 + m.b1369 + m.b1370 + m.b1371 + m.b1372
                          + m.b1373 + m.b1374 + m.b1375 + m.b1376 + m.b1377 + m.b1378 + m.b1379 + m.b1380 + m.b1381
                          + m.b1382 + m.b1383 + m.b1384 + m.b1385 == 1)

m.c326 = Constraint(expr=   m.b1386 + m.b1387 + m.b1388 + m.b1389 + m.b1390 + m.b1391 + m.b1392 + m.b1393 + m.b1394
                          + m.b1395 + m.b1396 + m.b1397 + m.b1398 + m.b1399 + m.b1400 + m.b1401 + m.b1402 + m.b1403
                          + m.b1404 + m.b1405 + m.b1406 + m.b1407 == 1)

m.c327 = Constraint(expr=   m.b1408 + m.b1409 + m.b1410 + m.b1411 + m.b1412 + m.b1413 + m.b1414 + m.b1415 + m.b1416
                          + m.b1417 + m.b1418 + m.b1419 + m.b1420 + m.b1421 + m.b1422 + m.b1423 + m.b1424 + m.b1425
                          + m.b1426 + m.b1427 + m.b1428 + m.b1429 == 1)
