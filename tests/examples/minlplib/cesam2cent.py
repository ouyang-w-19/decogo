#  NLP written by GAMS Convert at 04/21/18 13:51:14
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        166      166        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        317      317        0        0        0        0        0        0
#  FX     53       53        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        821      595      226        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(None,None),initialize=0.714277270296959)
m.x2 = Var(within=Reals,bounds=(None,None),initialize=0.213455359357076)
m.x3 = Var(within=Reals,bounds=(None,None),initialize=-0.000257460042516337)
m.x4 = Var(within=Reals,bounds=(None,None),initialize=0.267446625046681)
m.x5 = Var(within=Reals,bounds=(None,None),initialize=0.428981457932639)
m.x6 = Var(within=Reals,bounds=(None,None),initialize=0.706421402256235)
m.x7 = Var(within=Reals,bounds=(None,None),initialize=1.23179277222266)
m.x8 = Var(within=Reals,bounds=(None,None),initialize=1.1923022297969)
m.x9 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x10 = Var(within=Reals,bounds=(None,None),initialize=0.531271066405917)
m.x11 = Var(within=Reals,bounds=(None,None),initialize=0.37852116602787)
m.x12 = Var(within=Reals,bounds=(None,None),initialize=0.0259822061255019)
m.x13 = Var(within=Reals,bounds=(None,None),initialize=0.613866884603052)
m.x14 = Var(within=Reals,bounds=(None,None),initialize=0.912812569152467)
m.x15 = Var(within=Reals,bounds=(None,None),initialize=0.0233052515549957)
m.x16 = Var(within=Reals,bounds=(None,None),initialize=0.0359433346141142)
m.x17 = Var(within=Reals,bounds=(None,None),initialize=0.0397474756614438)
m.x18 = Var(within=Reals,bounds=(None,None),initialize=0.0172169283352343)
m.x19 = Var(within=Reals,bounds=(None,None),initialize=0.00761194936907785)
m.x20 = Var(within=Reals,bounds=(None,None),initialize=0.0456959504315114)
m.x21 = Var(within=Reals,bounds=(None,None),initialize=0.0141724551070975)
m.x22 = Var(within=Reals,bounds=(None,None),initialize=0.307728859298738)
m.x23 = Var(within=Reals,bounds=(None,None),initialize=0.0414914804160212)
m.x24 = Var(within=Reals,bounds=(None,None),initialize=0.0659507832795914)
m.x25 = Var(within=Reals,bounds=(None,None),initialize=-0.280822769860641)
m.x26 = Var(within=Reals,bounds=(None,None),initialize=-0.192302229796904)
m.x27 = Var(within=Reals,bounds=(None,None),initialize=0.388881181040466)
m.x28 = Var(within=Reals,bounds=(None,None),initialize=0.268505801367806)
m.x29 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x30 = Var(within=Reals,bounds=(None,None),initialize=14.827424)
m.x31 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x33 = Var(within=Reals,bounds=(None,None),initialize=2.101049)
m.x34 = Var(within=Reals,bounds=(None,None),initialize=-0.000327)
m.x35 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x36 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x37 = Var(within=Reals,bounds=(None,None),initialize=1.488157)
m.x38 = Var(within=Reals,bounds=(None,None),initialize=7.917504)
m.x39 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x40 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x41 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x42 = Var(within=Reals,bounds=(None,None),initialize=6.953332)
m.x43 = Var(within=Reals,bounds=(None,None),initialize=1.5645)
m.x44 = Var(within=Reals,bounds=(None,None),initialize=2.5185)
m.x45 = Var(within=Reals,bounds=(None,None),initialize=2.597798)
m.x46 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x47 = Var(within=Reals,bounds=(None,None),initialize=9.805414)
m.x48 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x49 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x50 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x51 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x52 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x53 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x54 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x55 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x56 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x57 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x58 = Var(within=Reals,bounds=(None,None),initialize=3.699706)
m.x59 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x60 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x61 = Var(within=Reals,bounds=(None,None),initialize=0.033)
m.x62 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x63 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x64 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x65 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x66 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x67 = Var(within=Reals,bounds=(None,None),initialize=6)
m.x68 = Var(within=Reals,bounds=(None,None),initialize=3.3)
m.x69 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x70 = Var(within=Reals,bounds=(None,None),initialize=0.0296)
m.x71 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x72 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x73 = Var(within=Reals,bounds=(None,None),initialize=0.2)
m.x74 = Var(within=Reals,bounds=(None,None),initialize=0.7336)
m.x75 = Var(within=Reals,bounds=(None,None),initialize=0.3574)
m.x76 = Var(within=Reals,bounds=(None,None),initialize=0.0744)
m.x77 = Var(within=Reals,bounds=(None,None),initialize=0.1652)
m.x78 = Var(within=Reals,bounds=(None,None),initialize=0.1395)
m.x79 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x80 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x81 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x82 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x83 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x84 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x85 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x86 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x87 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x88 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x89 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x90 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x91 = Var(within=Reals,bounds=(None,None),initialize=1.7123)
m.x92 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x93 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x94 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x95 = Var(within=Reals,bounds=(None,None),initialize=0.15)
m.x96 = Var(within=Reals,bounds=(None,None),initialize=0.649156)
m.x97 = Var(within=Reals,bounds=(None,None),initialize=-0.356673)
m.x98 = Var(within=Reals,bounds=(None,None),initialize=-0.4062)
m.x99 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x100 = Var(within=Reals,bounds=(None,None),initialize=2.163857)
m.x101 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x102 = Var(within=Reals,bounds=(None,None),initialize=5.573815)
m.x103 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x104 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x105 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x106 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x107 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x108 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x109 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x110 = Var(within=Reals,bounds=(None,None),initialize=9.805414)
m.x111 = Var(within=Reals,bounds=(None,None),initialize=10.896741)
m.x112 = Var(within=Reals,bounds=(None,None),initialize=18.4364105)
m.x113 = Var(within=Reals,bounds=(None,None),initialize=21.1551365)
m.x114 = Var(within=Reals,bounds=(None,None),initialize=9.78976)
m.x115 = Var(within=Reals,bounds=(None,None),initialize=3.673953)
m.x116 = Var(within=Reals,bounds=(None,None),initialize=9.6863185)
m.x117 = Var(within=Reals,bounds=(None,None),initialize=1.3701)
m.x118 = Var(within=Reals,bounds=(None,None),initialize=1.9123)
m.x119 = Var(within=Reals,bounds=(None,None),initialize=2.398969)
m.x120 = Var(within=Reals,bounds=(None,None),initialize=5.5690645)
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
m.x160 = Var(within=Reals,bounds=(0,1),initialize=0.142857142857143)
m.x161 = Var(within=Reals,bounds=(0,1),initialize=0.142857142857143)
m.x162 = Var(within=Reals,bounds=(0,1),initialize=0.142857142857143)
m.x163 = Var(within=Reals,bounds=(0,1),initialize=0.142857142857143)
m.x164 = Var(within=Reals,bounds=(0,1),initialize=0.142857142857143)
m.x165 = Var(within=Reals,bounds=(0,1),initialize=0.142857142857143)
m.x166 = Var(within=Reals,bounds=(0,1),initialize=0.142857142857143)
m.x167 = Var(within=Reals,bounds=(0,1),initialize=0.142857142857143)
m.x168 = Var(within=Reals,bounds=(0,1),initialize=0.142857142857143)
m.x169 = Var(within=Reals,bounds=(0,1),initialize=0.142857142857143)
m.x170 = Var(within=Reals,bounds=(0,1),initialize=0.142857142857143)
m.x171 = Var(within=Reals,bounds=(0,1),initialize=0.142857142857143)
m.x172 = Var(within=Reals,bounds=(0,1),initialize=0.142857142857143)
m.x173 = Var(within=Reals,bounds=(0,1),initialize=0.142857142857143)
m.x174 = Var(within=Reals,bounds=(0,1),initialize=0.142857142857143)
m.x175 = Var(within=Reals,bounds=(0,1),initialize=0.142857142857143)
m.x176 = Var(within=Reals,bounds=(0,1),initialize=0.142857142857143)
m.x177 = Var(within=Reals,bounds=(0,1),initialize=0.142857142857143)
m.x178 = Var(within=Reals,bounds=(0,1),initialize=0.142857142857143)
m.x179 = Var(within=Reals,bounds=(0,1),initialize=0.142857142857143)
m.x180 = Var(within=Reals,bounds=(0,1),initialize=0.142857142857143)
m.x181 = Var(within=Reals,bounds=(0,1),initialize=0.142857142857143)
m.x182 = Var(within=Reals,bounds=(0,1),initialize=0.142857142857143)
m.x183 = Var(within=Reals,bounds=(0,1),initialize=0.142857142857143)
m.x184 = Var(within=Reals,bounds=(0,1),initialize=0.142857142857143)
m.x185 = Var(within=Reals,bounds=(0,1),initialize=0.142857142857143)
m.x186 = Var(within=Reals,bounds=(0,1),initialize=0.142857142857143)
m.x187 = Var(within=Reals,bounds=(0,1),initialize=0.142857142857143)
m.x188 = Var(within=Reals,bounds=(0,1),initialize=0.142857142857143)
m.x189 = Var(within=Reals,bounds=(0,1),initialize=0.142857142857143)
m.x190 = Var(within=Reals,bounds=(0,1),initialize=0.142857142857143)
m.x191 = Var(within=Reals,bounds=(0,1),initialize=0.142857142857143)
m.x192 = Var(within=Reals,bounds=(0,1),initialize=0.142857142857143)
m.x193 = Var(within=Reals,bounds=(0,1),initialize=0.142857142857143)
m.x194 = Var(within=Reals,bounds=(0,1),initialize=0.142857142857143)
m.x195 = Var(within=Reals,bounds=(0,1),initialize=0.142857142857143)
m.x196 = Var(within=Reals,bounds=(0,1),initialize=0.142857142857143)
m.x197 = Var(within=Reals,bounds=(0,1),initialize=0.142857142857143)
m.x198 = Var(within=Reals,bounds=(0,1),initialize=0.142857142857143)
m.x199 = Var(within=Reals,bounds=(0,1),initialize=0.142857142857143)
m.x200 = Var(within=Reals,bounds=(0,1),initialize=0.142857142857143)
m.x201 = Var(within=Reals,bounds=(0,1),initialize=0.142857142857143)
m.x202 = Var(within=Reals,bounds=(0,1),initialize=0.142857142857143)
m.x203 = Var(within=Reals,bounds=(0,1),initialize=0.142857142857143)
m.x204 = Var(within=Reals,bounds=(0,1),initialize=0.142857142857143)
m.x205 = Var(within=Reals,bounds=(0,1),initialize=0.142857142857143)
m.x206 = Var(within=Reals,bounds=(0,1),initialize=0.142857142857143)
m.x207 = Var(within=Reals,bounds=(0,1),initialize=0.142857142857143)
m.x208 = Var(within=Reals,bounds=(0,1),initialize=0.142857142857143)
m.x209 = Var(within=Reals,bounds=(0,1),initialize=0.142857142857143)
m.x210 = Var(within=Reals,bounds=(0,1),initialize=0.142857142857143)
m.x211 = Var(within=Reals,bounds=(0,1),initialize=0.142857142857143)
m.x212 = Var(within=Reals,bounds=(0,1),initialize=0.142857142857143)
m.x213 = Var(within=Reals,bounds=(0,1),initialize=0.142857142857143)
m.x214 = Var(within=Reals,bounds=(0,1),initialize=0.142857142857143)
m.x215 = Var(within=Reals,bounds=(0,1),initialize=0.142857142857143)
m.x216 = Var(within=Reals,bounds=(0,1),initialize=0.142857142857143)
m.x217 = Var(within=Reals,bounds=(0,1),initialize=0.142857142857143)
m.x218 = Var(within=Reals,bounds=(0,1),initialize=0.142857142857143)
m.x219 = Var(within=Reals,bounds=(0,1),initialize=0.142857142857143)
m.x220 = Var(within=Reals,bounds=(0,1),initialize=0.142857142857143)
m.x221 = Var(within=Reals,bounds=(0,1),initialize=0.142857142857143)
m.x222 = Var(within=Reals,bounds=(0,1),initialize=0.142857142857143)
m.x223 = Var(within=Reals,bounds=(0,1),initialize=0.00617283950617284)
m.x224 = Var(within=Reals,bounds=(0,1),initialize=0.197530864197531)
m.x225 = Var(within=Reals,bounds=(0,1),initialize=0.592592592592593)
m.x226 = Var(within=Reals,bounds=(0,1),initialize=0.197530864197531)
m.x227 = Var(within=Reals,bounds=(0,1),initialize=0.00617283950617284)
m.x228 = Var(within=Reals,bounds=(0,1),initialize=0.00617283950617284)
m.x229 = Var(within=Reals,bounds=(0,1),initialize=0.197530864197531)
m.x230 = Var(within=Reals,bounds=(0,1),initialize=0.592592592592593)
m.x231 = Var(within=Reals,bounds=(0,1),initialize=0.197530864197531)
m.x232 = Var(within=Reals,bounds=(0,1),initialize=0.00617283950617284)
m.x233 = Var(within=Reals,bounds=(0,1),initialize=0.0555555555555556)
m.x234 = Var(within=Reals,bounds=(0,1),initialize=0.888888888888889)
m.x235 = Var(within=Reals,bounds=(0,1),initialize=0.0555555555555556)
m.x236 = Var(within=Reals,bounds=(0,1),initialize=0.0555555555555556)
m.x237 = Var(within=Reals,bounds=(0,1),initialize=0.888888888888889)
m.x238 = Var(within=Reals,bounds=(0,1),initialize=0.0555555555555556)
m.x239 = Var(within=Reals,bounds=(0,1),initialize=0.0555555555555556)
m.x240 = Var(within=Reals,bounds=(0,1),initialize=0.888888888888889)
m.x241 = Var(within=Reals,bounds=(0,1),initialize=0.0555555555555556)
m.x242 = Var(within=Reals,bounds=(0,1),initialize=0.0555555555555556)
m.x243 = Var(within=Reals,bounds=(0,1),initialize=0.888888888888889)
m.x244 = Var(within=Reals,bounds=(0,1),initialize=0.0555555555555556)
m.x245 = Var(within=Reals,bounds=(0,1),initialize=0.0555555555555556)
m.x246 = Var(within=Reals,bounds=(0,1),initialize=0.888888888888889)
m.x247 = Var(within=Reals,bounds=(0,1),initialize=0.0555555555555556)
m.x248 = Var(within=Reals,bounds=(0,1),initialize=0.0555555555555556)
m.x249 = Var(within=Reals,bounds=(0,1),initialize=0.888888888888889)
m.x250 = Var(within=Reals,bounds=(0,1),initialize=0.0555555555555556)
m.x251 = Var(within=Reals,bounds=(0,1),initialize=0.0555555555555556)
m.x252 = Var(within=Reals,bounds=(0,1),initialize=0.888888888888889)
m.x253 = Var(within=Reals,bounds=(0,1),initialize=0.0555555555555556)
m.x254 = Var(within=Reals,bounds=(0,1),initialize=0.0555555555555556)
m.x255 = Var(within=Reals,bounds=(0,1),initialize=0.888888888888889)
m.x256 = Var(within=Reals,bounds=(0,1),initialize=0.0555555555555556)
m.x257 = Var(within=Reals,bounds=(0,1),initialize=0.0555555555555556)
m.x258 = Var(within=Reals,bounds=(0,1),initialize=0.888888888888889)
m.x259 = Var(within=Reals,bounds=(0,1),initialize=0.0555555555555556)
m.x260 = Var(within=Reals,bounds=(0,1),initialize=0.0555555555555556)
m.x261 = Var(within=Reals,bounds=(0,1),initialize=0.888888888888889)
m.x262 = Var(within=Reals,bounds=(0,1),initialize=0.0555555555555556)
m.x263 = Var(within=Reals,bounds=(0,1),initialize=0.0555555555555556)
m.x264 = Var(within=Reals,bounds=(0,1),initialize=0.888888888888889)
m.x265 = Var(within=Reals,bounds=(0,1),initialize=0.0555555555555556)
m.x266 = Var(within=Reals,bounds=(0,1),initialize=0.0555555555555556)
m.x267 = Var(within=Reals,bounds=(0,1),initialize=0.888888888888889)
m.x268 = Var(within=Reals,bounds=(0,1),initialize=0.0555555555555556)
m.x269 = Var(within=Reals,bounds=(0,1),initialize=0.0555555555555556)
m.x270 = Var(within=Reals,bounds=(0,1),initialize=0.888888888888889)
m.x271 = Var(within=Reals,bounds=(0,1),initialize=0.0555555555555556)
m.x272 = Var(within=Reals,bounds=(0,1),initialize=0.0555555555555556)
m.x273 = Var(within=Reals,bounds=(0,1),initialize=0.888888888888889)
m.x274 = Var(within=Reals,bounds=(0,1),initialize=0.0555555555555556)
m.x275 = Var(within=Reals,bounds=(0,1),initialize=0.0555555555555556)
m.x276 = Var(within=Reals,bounds=(0,1),initialize=0.888888888888889)
m.x277 = Var(within=Reals,bounds=(0,1),initialize=0.0555555555555556)
m.x278 = Var(within=Reals,bounds=(0,1),initialize=0.0555555555555556)
m.x279 = Var(within=Reals,bounds=(0,1),initialize=0.888888888888889)
m.x280 = Var(within=Reals,bounds=(0,1),initialize=0.0555555555555556)
m.x281 = Var(within=Reals,bounds=(0,1),initialize=0.0555555555555556)
m.x282 = Var(within=Reals,bounds=(0,1),initialize=0.888888888888889)
m.x283 = Var(within=Reals,bounds=(0,1),initialize=0.0555555555555556)
m.x284 = Var(within=Reals,bounds=(0,1),initialize=0.0555555555555556)
m.x285 = Var(within=Reals,bounds=(0,1),initialize=0.888888888888889)
m.x286 = Var(within=Reals,bounds=(0,1),initialize=0.0555555555555556)
m.x287 = Var(within=Reals,bounds=(0,1),initialize=0.0555555555555556)
m.x288 = Var(within=Reals,bounds=(0,1),initialize=0.888888888888889)
m.x289 = Var(within=Reals,bounds=(0,1),initialize=0.0555555555555556)
m.x290 = Var(within=Reals,bounds=(0,1),initialize=0.0555555555555556)
m.x291 = Var(within=Reals,bounds=(0,1),initialize=0.888888888888889)
m.x292 = Var(within=Reals,bounds=(0,1),initialize=0.0555555555555556)
m.x293 = Var(within=Reals,bounds=(0,1),initialize=0.0555555555555556)
m.x294 = Var(within=Reals,bounds=(0,1),initialize=0.888888888888889)
m.x295 = Var(within=Reals,bounds=(0,1),initialize=0.0555555555555556)
m.x296 = Var(within=Reals,bounds=(0,1),initialize=0.0555555555555556)
m.x297 = Var(within=Reals,bounds=(0,1),initialize=0.888888888888889)
m.x298 = Var(within=Reals,bounds=(0,1),initialize=0.0555555555555556)
m.x299 = Var(within=Reals,bounds=(0,1),initialize=0.0555555555555556)
m.x300 = Var(within=Reals,bounds=(0,1),initialize=0.888888888888889)
m.x301 = Var(within=Reals,bounds=(0,1),initialize=0.0555555555555556)
m.x302 = Var(within=Reals,bounds=(0,1),initialize=0.0555555555555556)
m.x303 = Var(within=Reals,bounds=(0,1),initialize=0.888888888888889)
m.x304 = Var(within=Reals,bounds=(0,1),initialize=0.0555555555555556)
m.x305 = Var(within=Reals,bounds=(0,1),initialize=0.0555555555555556)
m.x306 = Var(within=Reals,bounds=(0,1),initialize=0.888888888888889)
m.x307 = Var(within=Reals,bounds=(0,1),initialize=0.0555555555555556)
m.x308 = Var(within=Reals,bounds=(0,1),initialize=0.0555555555555556)
m.x309 = Var(within=Reals,bounds=(0,1),initialize=0.888888888888889)
m.x310 = Var(within=Reals,bounds=(0,1),initialize=0.0555555555555556)
m.x311 = Var(within=Reals,bounds=(0,1),initialize=0.0555555555555556)
m.x312 = Var(within=Reals,bounds=(0,1),initialize=0.888888888888889)
m.x313 = Var(within=Reals,bounds=(0,1),initialize=0.0555555555555556)
m.x314 = Var(within=Reals,bounds=(0,1),initialize=0.0555555555555556)
m.x315 = Var(within=Reals,bounds=(0,1),initialize=0.888888888888889)
m.x316 = Var(within=Reals,bounds=(0,1),initialize=0.0555555555555556)

m.obj = Objective(expr=Centropy(m.x233,0.0555555555555556) + Centropy(m.x234,0.888888888888889) + Centropy(m.x235,
                       0.0555555555555556) + Centropy(m.x236,0.0555555555555556) + Centropy(m.x237,0.888888888888889) + 
                       Centropy(m.x238,0.0555555555555556) + Centropy(m.x239,0.0555555555555556) + Centropy(m.x240,
                       0.888888888888889) + Centropy(m.x241,0.0555555555555556) + Centropy(m.x242,0.0555555555555556) + 
                       Centropy(m.x243,0.888888888888889) + Centropy(m.x244,0.0555555555555556) + Centropy(m.x245,
                       0.0555555555555556) + Centropy(m.x246,0.888888888888889) + Centropy(m.x247,0.0555555555555556) + 
                       Centropy(m.x248,0.0555555555555556) + Centropy(m.x249,0.888888888888889) + Centropy(m.x250,
                       0.0555555555555556) + Centropy(m.x251,0.0555555555555556) + Centropy(m.x252,0.888888888888889) + 
                       Centropy(m.x253,0.0555555555555556) + Centropy(m.x254,0.0555555555555556) + Centropy(m.x255,
                       0.888888888888889) + Centropy(m.x256,0.0555555555555556) + Centropy(m.x257,0.0555555555555556) + 
                       Centropy(m.x258,0.888888888888889) + Centropy(m.x259,0.0555555555555556) + Centropy(m.x260,
                       0.0555555555555556) + Centropy(m.x261,0.888888888888889) + Centropy(m.x262,0.0555555555555556) + 
                       Centropy(m.x263,0.0555555555555556) + Centropy(m.x264,0.888888888888889) + Centropy(m.x265,
                       0.0555555555555556) + Centropy(m.x266,0.0555555555555556) + Centropy(m.x267,0.888888888888889) + 
                       Centropy(m.x268,0.0555555555555556) + Centropy(m.x269,0.0555555555555556) + Centropy(m.x270,
                       0.888888888888889) + Centropy(m.x271,0.0555555555555556) + Centropy(m.x272,0.0555555555555556) + 
                       Centropy(m.x273,0.888888888888889) + Centropy(m.x274,0.0555555555555556) + Centropy(m.x275,
                       0.0555555555555556) + Centropy(m.x276,0.888888888888889) + Centropy(m.x277,0.0555555555555556) + 
                       Centropy(m.x278,0.0555555555555556) + Centropy(m.x279,0.888888888888889) + Centropy(m.x280,
                       0.0555555555555556) + Centropy(m.x281,0.0555555555555556) + Centropy(m.x282,0.888888888888889) + 
                       Centropy(m.x283,0.0555555555555556) + Centropy(m.x284,0.0555555555555556) + Centropy(m.x285,
                       0.888888888888889) + Centropy(m.x286,0.0555555555555556) + Centropy(m.x287,0.0555555555555556) + 
                       Centropy(m.x288,0.888888888888889) + Centropy(m.x289,0.0555555555555556) + Centropy(m.x290,
                       0.0555555555555556) + Centropy(m.x291,0.888888888888889) + Centropy(m.x292,0.0555555555555556) + 
                       Centropy(m.x293,0.0555555555555556) + Centropy(m.x294,0.888888888888889) + Centropy(m.x295,
                       0.0555555555555556) + Centropy(m.x296,0.0555555555555556) + Centropy(m.x297,0.888888888888889) + 
                       Centropy(m.x298,0.0555555555555556) + Centropy(m.x299,0.0555555555555556) + Centropy(m.x300,
                       0.888888888888889) + Centropy(m.x301,0.0555555555555556) + Centropy(m.x302,0.0555555555555556) + 
                       Centropy(m.x303,0.888888888888889) + Centropy(m.x304,0.0555555555555556) + Centropy(m.x305,
                       0.0555555555555556) + Centropy(m.x306,0.888888888888889) + Centropy(m.x307,0.0555555555555556) + 
                       Centropy(m.x308,0.0555555555555556) + Centropy(m.x309,0.888888888888889) + Centropy(m.x310,
                       0.0555555555555556) + Centropy(m.x311,0.0555555555555556) + Centropy(m.x312,0.888888888888889) + 
                       Centropy(m.x313,0.0555555555555556) + Centropy(m.x314,0.0555555555555556) + Centropy(m.x315,
                       0.888888888888889) + Centropy(m.x316,0.0555555555555556) + Centropy(m.x160,0.142857142857143) + 
                       Centropy(m.x161,0.142857142857143) + Centropy(m.x162,0.142857142857143) + Centropy(m.x163,
                       0.142857142857143) + Centropy(m.x164,0.142857142857143) + Centropy(m.x165,0.142857142857143) + 
                       Centropy(m.x166,0.142857142857143) + Centropy(m.x167,0.142857142857143) + Centropy(m.x168,
                       0.142857142857143) + Centropy(m.x169,0.142857142857143) + Centropy(m.x170,0.142857142857143) + 
                       Centropy(m.x171,0.142857142857143) + Centropy(m.x172,0.142857142857143) + Centropy(m.x173,
                       0.142857142857143) + Centropy(m.x174,0.142857142857143) + Centropy(m.x175,0.142857142857143) + 
                       Centropy(m.x176,0.142857142857143) + Centropy(m.x177,0.142857142857143) + Centropy(m.x178,
                       0.142857142857143) + Centropy(m.x179,0.142857142857143) + Centropy(m.x180,0.142857142857143) + 
                       Centropy(m.x181,0.142857142857143) + Centropy(m.x182,0.142857142857143) + Centropy(m.x183,
                       0.142857142857143) + Centropy(m.x184,0.142857142857143) + Centropy(m.x185,0.142857142857143) + 
                       Centropy(m.x186,0.142857142857143) + Centropy(m.x187,0.142857142857143) + Centropy(m.x188,
                       0.142857142857143) + Centropy(m.x189,0.142857142857143) + Centropy(m.x190,0.142857142857143) + 
                       Centropy(m.x191,0.142857142857143) + Centropy(m.x192,0.142857142857143) + Centropy(m.x193,
                       0.142857142857143) + Centropy(m.x194,0.142857142857143) + Centropy(m.x195,0.142857142857143) + 
                       Centropy(m.x196,0.142857142857143) + Centropy(m.x197,0.142857142857143) + Centropy(m.x198,
                       0.142857142857143) + Centropy(m.x199,0.142857142857143) + Centropy(m.x200,0.142857142857143) + 
                       Centropy(m.x201,0.142857142857143) + Centropy(m.x202,0.142857142857143) + Centropy(m.x203,
                       0.142857142857143) + Centropy(m.x204,0.142857142857143) + Centropy(m.x205,0.142857142857143) + 
                       Centropy(m.x206,0.142857142857143) + Centropy(m.x207,0.142857142857143) + Centropy(m.x208,
                       0.142857142857143) + Centropy(m.x209,0.142857142857143) + Centropy(m.x210,0.142857142857143) + 
                       Centropy(m.x211,0.142857142857143) + Centropy(m.x212,0.142857142857143) + Centropy(m.x213,
                       0.142857142857143) + Centropy(m.x214,0.142857142857143) + Centropy(m.x215,0.142857142857143) + 
                       Centropy(m.x216,0.142857142857143) + Centropy(m.x217,0.142857142857143) + Centropy(m.x218,
                       0.142857142857143) + Centropy(m.x219,0.142857142857143) + Centropy(m.x220,0.142857142857143) + 
                       Centropy(m.x221,0.142857142857143) + Centropy(m.x222,0.142857142857143) + Centropy(m.x223,
                       0.00617283950617284) + Centropy(m.x224,0.197530864197531) + Centropy(m.x225,0.592592592592593) + 
                       Centropy(m.x226,0.197530864197531) + Centropy(m.x227,0.00617283950617284) + Centropy(m.x228,
                       0.00617283950617284) + Centropy(m.x229,0.197530864197531) + Centropy(m.x230,0.592592592592593) + 
                       Centropy(m.x231,0.197530864197531) + Centropy(m.x232,0.00617283950617284), sense=minimize)

m.c1 = Constraint(expr=   m.x112 - m.x121 == 18.4364105)

m.c2 = Constraint(expr=   m.x113 - m.x122 == 21.1551365)

m.c3 = Constraint(expr=   m.x114 - m.x123 == 9.78976)

m.c4 = Constraint(expr=   m.x115 - m.x124 == 3.673953)

m.c5 = Constraint(expr=   m.x116 - m.x125 == 9.6863185)

m.c6 = Constraint(expr=   m.x117 - m.x126 == 1.3701)

m.c7 = Constraint(expr=   m.x118 - m.x127 == 1.9123)

m.c8 = Constraint(expr=   m.x119 - m.x128 == 2.398969)

m.c9 = Constraint(expr=   m.x120 - m.x129 == 5.5690645)

m.c10 = Constraint(expr=   m.x29 + m.x30 + m.x31 + m.x32 + m.x33 + m.x34 + m.x35 + m.x36 + m.x37 - m.x112 == 0)

m.c11 = Constraint(expr=   m.x38 + m.x39 + m.x40 + m.x41 + m.x42 + m.x43 + m.x44 + m.x45 + m.x46 - m.x113 == 0)

m.c12 = Constraint(expr=   m.x47 + m.x48 + m.x49 + m.x50 + m.x51 + m.x52 + m.x53 + m.x54 + m.x55 - m.x114 == 0)

m.c13 = Constraint(expr=   m.x56 + m.x57 + m.x58 + m.x59 + m.x60 + m.x61 + m.x62 + m.x63 + m.x64 - m.x115 == 0)

m.c14 = Constraint(expr=   m.x65 + m.x66 + m.x67 + m.x68 + m.x69 + m.x70 + m.x71 + m.x72 + m.x73 - m.x116 == 0)

m.c15 = Constraint(expr=   m.x74 + m.x75 + m.x76 + m.x77 + m.x78 + m.x79 + m.x80 + m.x81 + m.x82 - m.x117 == 0)

m.c16 = Constraint(expr=   m.x83 + m.x84 + m.x85 + m.x86 + m.x87 + m.x88 + m.x89 + m.x90 + m.x91 - m.x118 == 0)

m.c17 = Constraint(expr=   m.x92 + m.x93 + m.x94 + m.x95 + m.x96 + m.x97 + m.x98 + m.x99 + m.x100 - m.x119 == 0)

m.c18 = Constraint(expr=   m.x101 + m.x102 + m.x103 + m.x104 + m.x105 + m.x106 + m.x107 + m.x108 + m.x109 - m.x120 == 0)

m.c19 = Constraint(expr=   m.x29 + m.x38 + m.x47 + m.x56 + m.x65 + m.x74 + m.x83 + m.x92 + m.x101 - m.x112 == 0)

m.c20 = Constraint(expr=   m.x30 + m.x39 + m.x48 + m.x57 + m.x66 + m.x75 + m.x84 + m.x93 + m.x102 - m.x113 == 0)

m.c21 = Constraint(expr=   m.x31 + m.x40 + m.x49 + m.x58 + m.x67 + m.x76 + m.x85 + m.x94 + m.x103 - m.x114 == 0)

m.c22 = Constraint(expr=   m.x32 + m.x41 + m.x50 + m.x59 + m.x68 + m.x77 + m.x86 + m.x95 + m.x104 - m.x115 == 0)

m.c23 = Constraint(expr=   m.x33 + m.x42 + m.x51 + m.x60 + m.x69 + m.x78 + m.x87 + m.x96 + m.x105 - m.x116 == 0)

m.c24 = Constraint(expr=   m.x34 + m.x43 + m.x52 + m.x61 + m.x70 + m.x79 + m.x88 + m.x97 + m.x106 - m.x117 == 0)

m.c25 = Constraint(expr=   m.x35 + m.x44 + m.x53 + m.x62 + m.x71 + m.x80 + m.x89 + m.x98 + m.x107 - m.x118 == 0)

m.c26 = Constraint(expr=   m.x36 + m.x45 + m.x54 + m.x63 + m.x72 + m.x81 + m.x90 + m.x99 + m.x108 - m.x119 == 0)

m.c27 = Constraint(expr=   m.x37 + m.x46 + m.x55 + m.x64 + m.x73 + m.x82 + m.x91 + m.x100 + m.x109 - m.x120 == 0)

m.c28 = Constraint(expr=-m.x1*m.x113 + m.x30 == 0)

m.c29 = Constraint(expr=-m.x2*m.x116 + m.x33 == 0)

m.c30 = Constraint(expr=-m.x3*m.x117 + m.x34 == 0)

m.c31 = Constraint(expr=-m.x4*m.x120 + m.x37 == 0)

m.c32 = Constraint(expr=-m.x5*m.x112 + m.x38 == 0)

m.c33 = Constraint(expr=-m.x6*m.x116 + m.x42 == 0)

m.c34 = Constraint(expr=-m.x7*m.x117 + m.x43 == 0)

m.c35 = Constraint(expr=-m.x8*m.x118 + m.x44 == 0)

m.c36 = Constraint(expr=-m.x9*m.x119 + m.x45 == 0)

m.c37 = Constraint(expr=-m.x10*m.x112 + m.x47 == 0)

m.c38 = Constraint(expr=-m.x11*m.x114 + m.x58 == 0)

m.c39 = Constraint(expr=-m.x12*m.x117 + m.x61 == 0)

m.c40 = Constraint(expr=-m.x13*m.x114 + m.x67 == 0)

m.c41 = Constraint(expr=-m.x14*m.x115 + m.x68 == 0)

m.c42 = Constraint(expr=-m.x15*m.x117 + m.x70 == 0)

m.c43 = Constraint(expr=-m.x16*m.x120 + m.x73 == 0)

m.c44 = Constraint(expr=-m.x17*m.x112 + m.x74 == 0)

m.c45 = Constraint(expr=-m.x18*m.x113 + m.x75 == 0)

m.c46 = Constraint(expr=-m.x19*m.x114 + m.x76 == 0)

m.c47 = Constraint(expr=-m.x20*m.x115 + m.x77 == 0)

m.c48 = Constraint(expr=-m.x21*m.x116 + m.x78 == 0)

m.c49 = Constraint(expr=-m.x22*m.x120 + m.x91 == 0)

m.c50 = Constraint(expr=-m.x23*m.x115 + m.x95 == 0)

m.c51 = Constraint(expr=-m.x24*m.x116 + m.x96 == 0)

m.c52 = Constraint(expr=-m.x25*m.x117 + m.x97 == 0)

m.c53 = Constraint(expr=-m.x26*m.x118 + m.x98 == 0)

m.c54 = Constraint(expr=-m.x27*m.x120 + m.x100 == 0)

m.c55 = Constraint(expr=-m.x28*m.x113 + m.x102 == 0)

m.c56 = Constraint(expr=   m.x30 - m.x132 == 14.827424)

m.c57 = Constraint(expr=   m.x34 - m.x134 == -0.000327)

m.c58 = Constraint(expr=   m.x37 - m.x135 == 1.488157)

m.c59 = Constraint(expr=   m.x43 - m.x138 == 1.5645)

m.c60 = Constraint(expr=   m.x44 - m.x139 == 2.5185)

m.c61 = Constraint(expr=   m.x45 - m.x140 == 2.597798)

m.c62 = Constraint(expr=   m.x61 - m.x143 == 0.033)

m.c63 = Constraint(expr=   m.x70 - m.x146 == 0.0296)

m.c64 = Constraint(expr=   m.x73 - m.x147 == 0.2)

m.c65 = Constraint(expr=   m.x75 - m.x149 == 0.3574)

m.c66 = Constraint(expr=   m.x91 - m.x153 == 1.7123)

m.c67 = Constraint(expr=   m.x97 - m.x156 == -0.356673)

m.c68 = Constraint(expr=   m.x98 - m.x157 == -0.4062)

m.c69 = Constraint(expr=   m.x100 - m.x158 == 2.163857)

m.c70 = Constraint(expr=   m.x102 - m.x159 == 5.573815)

m.c71 = Constraint(expr=-0.213455359357076*exp(m.x133) + m.x2 == 0)

m.c72 = Constraint(expr=-0.428981457932639*exp(m.x136) + m.x5 == 0)

m.c73 = Constraint(expr=-0.706421402256235*exp(m.x137) + m.x6 == 0)

m.c74 = Constraint(expr=-0.531271066405917*exp(m.x141) + m.x10 == 0)

m.c75 = Constraint(expr=-0.37852116602787*exp(m.x142) + m.x11 == 0)

m.c76 = Constraint(expr=-0.613866884603052*exp(m.x144) + m.x13 == 0)

m.c77 = Constraint(expr=-0.912812569152467*exp(m.x145) + m.x14 == 0)

m.c78 = Constraint(expr=-0.0397474756614438*exp(m.x148) + m.x17 == 0)

m.c79 = Constraint(expr=-0.00761194936907785*exp(m.x150) + m.x19 == 0)

m.c80 = Constraint(expr=-0.0456959504315114*exp(m.x151) + m.x20 == 0)

m.c81 = Constraint(expr=-0.0141724551070975*exp(m.x152) + m.x21 == 0)

m.c82 = Constraint(expr=-0.0414914804160212*exp(m.x154) + m.x23 == 0)

m.c83 = Constraint(expr=-0.0659507832795914*exp(m.x155) + m.x24 == 0)

m.c84 = Constraint(expr= - m.x47 + m.x110 == 0)

m.c85 = Constraint(expr=   m.x34 - m.x47 - m.x74 - m.x75 + m.x111 == 0)

m.c86 = Constraint(expr=   m.x110 - m.x130 == 9.805414)

m.c87 = Constraint(expr=   m.x111 - m.x131 == 10.896741)

m.c88 = Constraint(expr=   m.x121 + 2.765461575*m.x160 + 1.84364105*m.x161 + 0.921820525*m.x162 - 0.921820525*m.x164
                         - 1.84364105*m.x165 - 2.765461575*m.x166 == 0)

m.c89 = Constraint(expr=   m.x122 + 3.173270475*m.x167 + 2.11551365*m.x168 + 1.057756825*m.x169 - 1.057756825*m.x171
                         - 2.11551365*m.x172 - 3.173270475*m.x173 == 0)

m.c90 = Constraint(expr=   m.x123 + 1.468464*m.x174 + 0.978976*m.x175 + 0.489488*m.x176 - 0.489488*m.x178
                         - 0.978976*m.x179 - 1.468464*m.x180 == 0)

m.c91 = Constraint(expr=   m.x124 + 0.55109295*m.x181 + 0.3673953*m.x182 + 0.18369765*m.x183 - 0.18369765*m.x185
                         - 0.3673953*m.x186 - 0.55109295*m.x187 == 0)

m.c92 = Constraint(expr=   m.x125 + 1.452947775*m.x188 + 0.96863185*m.x189 + 0.484315925*m.x190 - 0.484315925*m.x192
                         - 0.96863185*m.x193 - 1.452947775*m.x194 == 0)

m.c93 = Constraint(expr=   m.x126 + 0.205515*m.x195 + 0.13701*m.x196 + 0.068505*m.x197 - 0.068505*m.x199
                         - 0.13701*m.x200 - 0.205515*m.x201 == 0)

m.c94 = Constraint(expr=   m.x127 + 0.286845*m.x202 + 0.19123*m.x203 + 0.095615*m.x204 - 0.095615*m.x206
                         - 0.19123*m.x207 - 0.286845*m.x208 == 0)

m.c95 = Constraint(expr=   m.x128 + 0.35984535*m.x209 + 0.2398969*m.x210 + 0.11994845*m.x211 - 0.11994845*m.x213
                         - 0.2398969*m.x214 - 0.35984535*m.x215 == 0)

m.c96 = Constraint(expr=   m.x129 + 0.835359675*m.x216 + 0.55690645*m.x217 + 0.278453225*m.x218 - 0.278453225*m.x220
                         - 0.55690645*m.x221 - 0.835359675*m.x222 == 0)

m.c97 = Constraint(expr=   m.x130 + 1.4708121*m.x223 + 0.73540605*m.x224 - 0.73540605*m.x226 - 1.4708121*m.x227 == 0)

m.c98 = Constraint(expr=   m.x131 + 1.63451115*m.x228 + 0.817255575*m.x229 - 0.817255575*m.x231 - 1.63451115*m.x232
                         == 0)

m.c99 = Constraint(expr=   m.x132 + 11.120568*m.x233 - 11.120568*m.x235 == 0)

m.c100 = Constraint(expr=   m.x133 + 0.75*m.x236 - 0.75*m.x238 == 0)

m.c101 = Constraint(expr=   m.x134 + 0.00024525*m.x239 - 0.00024525*m.x241 == 0)

m.c102 = Constraint(expr=   m.x135 + 1.11611775*m.x242 - 1.11611775*m.x244 == 0)

m.c103 = Constraint(expr=   m.x136 + 0.75*m.x245 - 0.75*m.x247 == 0)

m.c104 = Constraint(expr=   m.x137 + 0.75*m.x248 - 0.75*m.x250 == 0)

m.c105 = Constraint(expr=   m.x138 + 1.173375*m.x251 - 1.173375*m.x253 == 0)

m.c106 = Constraint(expr=   m.x139 + 1.888875*m.x254 - 1.888875*m.x256 == 0)

m.c107 = Constraint(expr=   m.x140 + 1.9483485*m.x257 - 1.9483485*m.x259 == 0)

m.c108 = Constraint(expr=   m.x141 + 0.75*m.x260 - 0.75*m.x262 == 0)

m.c109 = Constraint(expr=   m.x142 + 0.75*m.x263 - 0.75*m.x265 == 0)

m.c110 = Constraint(expr=   m.x143 + 0.02475*m.x266 - 0.02475*m.x268 == 0)

m.c111 = Constraint(expr=   m.x144 + 0.75*m.x269 - 0.75*m.x271 == 0)

m.c112 = Constraint(expr=   m.x145 + 0.75*m.x272 - 0.75*m.x274 == 0)

m.c113 = Constraint(expr=   m.x146 + 0.0222*m.x275 - 0.0222*m.x277 == 0)

m.c114 = Constraint(expr=   m.x147 + 0.15*m.x278 - 0.15*m.x280 == 0)

m.c115 = Constraint(expr=   m.x148 + 0.75*m.x281 - 0.75*m.x283 == 0)

m.c116 = Constraint(expr=   m.x149 + 0.26805*m.x284 - 0.26805*m.x286 == 0)

m.c117 = Constraint(expr=   m.x150 + 0.75*m.x287 - 0.75*m.x289 == 0)

m.c118 = Constraint(expr=   m.x151 + 0.75*m.x290 - 0.75*m.x292 == 0)

m.c119 = Constraint(expr=   m.x152 + 0.75*m.x293 - 0.75*m.x295 == 0)

m.c120 = Constraint(expr=   m.x153 + 1.284225*m.x296 - 1.284225*m.x298 == 0)

m.c121 = Constraint(expr=   m.x154 + 0.75*m.x299 - 0.75*m.x301 == 0)

m.c122 = Constraint(expr=   m.x155 + 0.75*m.x302 - 0.75*m.x304 == 0)

m.c123 = Constraint(expr=   m.x156 + 0.26750475*m.x305 - 0.26750475*m.x307 == 0)

m.c124 = Constraint(expr=   m.x157 + 0.30465*m.x308 - 0.30465*m.x310 == 0)

m.c125 = Constraint(expr=   m.x158 + 1.62289275*m.x311 - 1.62289275*m.x313 == 0)

m.c126 = Constraint(expr=   m.x159 + 4.18036125*m.x314 - 4.18036125*m.x316 == 0)

m.c127 = Constraint(expr=   m.x160 + m.x161 + m.x162 + m.x163 + m.x164 + m.x165 + m.x166 == 1)

m.c128 = Constraint(expr=   m.x167 + m.x168 + m.x169 + m.x170 + m.x171 + m.x172 + m.x173 == 1)

m.c129 = Constraint(expr=   m.x174 + m.x175 + m.x176 + m.x177 + m.x178 + m.x179 + m.x180 == 1)

m.c130 = Constraint(expr=   m.x181 + m.x182 + m.x183 + m.x184 + m.x185 + m.x186 + m.x187 == 1)

m.c131 = Constraint(expr=   m.x188 + m.x189 + m.x190 + m.x191 + m.x192 + m.x193 + m.x194 == 1)

m.c132 = Constraint(expr=   m.x195 + m.x196 + m.x197 + m.x198 + m.x199 + m.x200 + m.x201 == 1)

m.c133 = Constraint(expr=   m.x202 + m.x203 + m.x204 + m.x205 + m.x206 + m.x207 + m.x208 == 1)

m.c134 = Constraint(expr=   m.x209 + m.x210 + m.x211 + m.x212 + m.x213 + m.x214 + m.x215 == 1)

m.c135 = Constraint(expr=   m.x216 + m.x217 + m.x218 + m.x219 + m.x220 + m.x221 + m.x222 == 1)

m.c136 = Constraint(expr=   m.x223 + m.x224 + m.x225 + m.x226 + m.x227 == 1)

m.c137 = Constraint(expr=   m.x228 + m.x229 + m.x230 + m.x231 + m.x232 == 1)

m.c138 = Constraint(expr=   m.x233 + m.x234 + m.x235 == 1)

m.c139 = Constraint(expr=   m.x236 + m.x237 + m.x238 == 1)

m.c140 = Constraint(expr=   m.x239 + m.x240 + m.x241 == 1)

m.c141 = Constraint(expr=   m.x242 + m.x243 + m.x244 == 1)

m.c142 = Constraint(expr=   m.x245 + m.x246 + m.x247 == 1)

m.c143 = Constraint(expr=   m.x248 + m.x249 + m.x250 == 1)

m.c144 = Constraint(expr=   m.x251 + m.x252 + m.x253 == 1)

m.c145 = Constraint(expr=   m.x254 + m.x255 + m.x256 == 1)

m.c146 = Constraint(expr=   m.x257 + m.x258 + m.x259 == 1)

m.c147 = Constraint(expr=   m.x260 + m.x261 + m.x262 == 1)

m.c148 = Constraint(expr=   m.x263 + m.x264 + m.x265 == 1)

m.c149 = Constraint(expr=   m.x266 + m.x267 + m.x268 == 1)

m.c150 = Constraint(expr=   m.x269 + m.x270 + m.x271 == 1)

m.c151 = Constraint(expr=   m.x272 + m.x273 + m.x274 == 1)

m.c152 = Constraint(expr=   m.x275 + m.x276 + m.x277 == 1)

m.c153 = Constraint(expr=   m.x278 + m.x279 + m.x280 == 1)

m.c154 = Constraint(expr=   m.x281 + m.x282 + m.x283 == 1)

m.c155 = Constraint(expr=   m.x284 + m.x285 + m.x286 == 1)

m.c156 = Constraint(expr=   m.x287 + m.x288 + m.x289 == 1)

m.c157 = Constraint(expr=   m.x290 + m.x291 + m.x292 == 1)

m.c158 = Constraint(expr=   m.x293 + m.x294 + m.x295 == 1)

m.c159 = Constraint(expr=   m.x296 + m.x297 + m.x298 == 1)

m.c160 = Constraint(expr=   m.x299 + m.x300 + m.x301 == 1)

m.c161 = Constraint(expr=   m.x302 + m.x303 + m.x304 == 1)

m.c162 = Constraint(expr=   m.x305 + m.x306 + m.x307 == 1)

m.c163 = Constraint(expr=   m.x308 + m.x309 + m.x310 == 1)

m.c164 = Constraint(expr=   m.x311 + m.x312 + m.x313 == 1)

m.c165 = Constraint(expr=   m.x314 + m.x315 + m.x316 == 1)
