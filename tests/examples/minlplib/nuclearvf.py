#  MINLP written by GAMS Convert at 04/21/18 13:52:42
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        318      234        0       84        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        352      184      168        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       3385      521     2864        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x2 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x3 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x4 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x5 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x6 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x7 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x8 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x9 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x10 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x11 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x12 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x13 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x14 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x15 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x16 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x17 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x18 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x19 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x20 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x21 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x22 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x23 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x24 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x25 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x26 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x27 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x28 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x29 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x30 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x31 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x32 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x33 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x34 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x35 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x36 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x37 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x38 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x39 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x40 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x41 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x42 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x43 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x44 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x45 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x46 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x47 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x48 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x49 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x50 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x51 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x52 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x53 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x54 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x55 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x56 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x57 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x58 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x59 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x60 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x61 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x62 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x63 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x64 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x65 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x66 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x67 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x68 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x69 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x70 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x71 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x72 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x73 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x74 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x75 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x76 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x77 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x78 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x79 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x80 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x81 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x82 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x83 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x84 = Var(within=Reals,bounds=(0,None),initialize=0.0892857142857143)
m.x85 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x86 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x87 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x88 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x89 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x90 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x91 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x92 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x93 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x94 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x95 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x96 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x97 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x98 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x99 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x100 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x101 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x102 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x103 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x104 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x105 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x106 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x107 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x108 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x109 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x110 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x111 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x112 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x113 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x114 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x115 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x116 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x117 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x118 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x119 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x120 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x121 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x122 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x123 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x124 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x125 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x126 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x127 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x128 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x129 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x130 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x131 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x132 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x133 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x134 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x135 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x136 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x137 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x138 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x139 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x140 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x141 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x142 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x143 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x144 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x145 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x146 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x147 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x148 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x149 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x150 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x151 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x152 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x153 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x154 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x155 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x156 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x157 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x158 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x159 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x160 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x161 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x162 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x163 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x164 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x165 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x166 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x167 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x168 = Var(within=Reals,bounds=(0,None),initialize=1.25)
m.x169 = Var(within=Reals,bounds=(0,None),initialize=0.956145)
m.x170 = Var(within=Reals,bounds=(0,None),initialize=0.956145)
m.x171 = Var(within=Reals,bounds=(0,None),initialize=0.956145)
m.x172 = Var(within=Reals,bounds=(0,None),initialize=0.956145)
m.x173 = Var(within=Reals,bounds=(0,None),initialize=0.956145)
m.x174 = Var(within=Reals,bounds=(0,None),initialize=0.956145)
m.b175 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b176 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b177 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b178 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b179 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b180 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b181 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b182 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b183 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b184 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b185 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b186 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b187 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b188 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b189 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b190 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b191 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b192 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b193 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b194 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b195 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b196 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b197 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b198 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b199 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b200 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b201 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b202 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b203 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b204 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b205 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b206 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b207 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b208 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b209 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b210 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b211 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b212 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b213 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b214 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b215 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b216 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b217 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b218 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b219 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b220 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b221 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b222 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b223 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b224 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b225 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b226 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b227 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b228 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b229 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b230 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b231 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b232 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b233 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b234 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b235 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b236 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b237 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b238 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b239 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b240 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b241 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b242 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b243 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b244 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b245 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b246 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b247 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b248 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b249 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b250 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b251 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b252 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b253 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b254 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b255 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b256 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b257 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b258 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b259 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b260 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b261 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b262 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b263 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b264 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b265 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b266 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b267 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b268 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b269 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b270 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b271 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b272 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b273 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b274 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b275 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b276 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b277 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b278 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b279 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b280 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b281 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b282 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b283 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b284 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b285 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b286 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b287 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b288 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b289 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b290 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b291 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b292 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b293 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b294 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b295 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b296 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b297 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b298 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b299 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b300 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b301 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b302 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b303 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b304 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b305 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b306 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b307 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b308 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b309 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b310 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b311 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b312 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b313 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b314 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b315 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b316 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b317 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b318 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b319 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b320 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b321 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b322 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b323 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b324 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b325 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b326 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b327 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b328 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b329 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b330 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b331 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b332 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b333 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b334 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b335 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b336 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b337 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b338 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b339 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b340 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b341 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.b342 = Var(within=Binary,bounds=(0,1),initialize=0.0714285714285714)
m.x344 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x345 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x346 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x347 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x348 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x349 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x350 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x351 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x352 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr= - m.x174, sense=minimize)

m.c2 = Constraint(expr=   0.5*m.b175 + m.b187 + m.b199 + m.b211 + m.b223 + m.b235 + 0.5*m.b247 + m.b259 + m.b271
                        + m.b283 + 0.5*m.b295 + m.b307 + m.b319 + 0.5*m.b331 == 1)

m.c3 = Constraint(expr=   0.5*m.b176 + m.b188 + m.b200 + m.b212 + m.b224 + m.b236 + 0.5*m.b248 + m.b260 + m.b272
                        + m.b284 + 0.5*m.b296 + m.b308 + m.b320 + 0.5*m.b332 == 1)

m.c4 = Constraint(expr=   0.5*m.b177 + m.b189 + m.b201 + m.b213 + m.b225 + m.b237 + 0.5*m.b249 + m.b261 + m.b273
                        + m.b285 + 0.5*m.b297 + m.b309 + m.b321 + 0.5*m.b333 == 1)

m.c5 = Constraint(expr=   0.5*m.b178 + m.b190 + m.b202 + m.b214 + m.b226 + m.b238 + 0.5*m.b250 + m.b262 + m.b274
                        + m.b286 + 0.5*m.b298 + m.b310 + m.b322 + 0.5*m.b334 == 1)

m.c6 = Constraint(expr=   0.5*m.b179 + m.b191 + m.b203 + m.b215 + m.b227 + m.b239 + 0.5*m.b251 + m.b263 + m.b275
                        + m.b287 + 0.5*m.b299 + m.b311 + m.b323 + 0.5*m.b335 == 1)

m.c7 = Constraint(expr=   0.5*m.b180 + m.b192 + m.b204 + m.b216 + m.b228 + m.b240 + 0.5*m.b252 + m.b264 + m.b276
                        + m.b288 + 0.5*m.b300 + m.b312 + m.b324 + 0.5*m.b336 == 1)

m.c8 = Constraint(expr=   0.5*m.b181 + m.b193 + m.b205 + m.b217 + m.b229 + m.b241 + 0.5*m.b253 + m.b265 + m.b277
                        + m.b289 + 0.5*m.b301 + m.b313 + m.b325 + 0.5*m.b337 == 1)

m.c9 = Constraint(expr=   0.5*m.b182 + m.b194 + m.b206 + m.b218 + m.b230 + m.b242 + 0.5*m.b254 + m.b266 + m.b278
                        + m.b290 + 0.5*m.b302 + m.b314 + m.b326 + 0.5*m.b338 == 1)

m.c10 = Constraint(expr=   0.5*m.b183 + m.b195 + m.b207 + m.b219 + m.b231 + m.b243 + 0.5*m.b255 + m.b267 + m.b279
                         + m.b291 + 0.5*m.b303 + m.b315 + m.b327 + 0.5*m.b339 == 1)

m.c11 = Constraint(expr=   0.5*m.b184 + m.b196 + m.b208 + m.b220 + m.b232 + m.b244 + 0.5*m.b256 + m.b268 + m.b280
                         + m.b292 + 0.5*m.b304 + m.b316 + m.b328 + 0.5*m.b340 == 1)

m.c12 = Constraint(expr=   0.5*m.b185 + m.b197 + m.b209 + m.b221 + m.b233 + m.b245 + 0.5*m.b257 + m.b269 + m.b281
                         + m.b293 + 0.5*m.b305 + m.b317 + m.b329 + 0.5*m.b341 == 1)

m.c13 = Constraint(expr=   0.5*m.b186 + m.b198 + m.b210 + m.b222 + m.b234 + m.b246 + 0.5*m.b258 + m.b270 + m.b282
                         + m.b294 + 0.5*m.b306 + m.b318 + m.b330 + 0.5*m.b342 == 1)

m.c14 = Constraint(expr=   m.b175 + m.b176 + m.b177 + m.b178 + m.b179 + m.b180 + m.b181 + m.b182 + m.b183 + m.b184
                         + m.b185 + m.b186 == 1)

m.c15 = Constraint(expr=   m.b187 + m.b188 + m.b189 + m.b190 + m.b191 + m.b192 + m.b193 + m.b194 + m.b195 + m.b196
                         + m.b197 + m.b198 == 1)

m.c16 = Constraint(expr=   m.b199 + m.b200 + m.b201 + m.b202 + m.b203 + m.b204 + m.b205 + m.b206 + m.b207 + m.b208
                         + m.b209 + m.b210 == 1)

m.c17 = Constraint(expr=   m.b211 + m.b212 + m.b213 + m.b214 + m.b215 + m.b216 + m.b217 + m.b218 + m.b219 + m.b220
                         + m.b221 + m.b222 == 1)

m.c18 = Constraint(expr=   m.b223 + m.b224 + m.b225 + m.b226 + m.b227 + m.b228 + m.b229 + m.b230 + m.b231 + m.b232
                         + m.b233 + m.b234 == 1)

m.c19 = Constraint(expr=   m.b235 + m.b236 + m.b237 + m.b238 + m.b239 + m.b240 + m.b241 + m.b242 + m.b243 + m.b244
                         + m.b245 + m.b246 == 1)

m.c20 = Constraint(expr=   m.b247 + m.b248 + m.b249 + m.b250 + m.b251 + m.b252 + m.b253 + m.b254 + m.b255 + m.b256
                         + m.b257 + m.b258 == 1)

m.c21 = Constraint(expr=   m.b259 + m.b260 + m.b261 + m.b262 + m.b263 + m.b264 + m.b265 + m.b266 + m.b267 + m.b268
                         + m.b269 + m.b270 == 1)

m.c22 = Constraint(expr=   m.b271 + m.b272 + m.b273 + m.b274 + m.b275 + m.b276 + m.b277 + m.b278 + m.b279 + m.b280
                         + m.b281 + m.b282 == 1)

m.c23 = Constraint(expr=   m.b283 + m.b284 + m.b285 + m.b286 + m.b287 + m.b288 + m.b289 + m.b290 + m.b291 + m.b292
                         + m.b293 + m.b294 == 1)

m.c24 = Constraint(expr=   m.b295 + m.b296 + m.b297 + m.b298 + m.b299 + m.b300 + m.b301 + m.b302 + m.b303 + m.b304
                         + m.b305 + m.b306 == 1)

m.c25 = Constraint(expr=   m.b307 + m.b308 + m.b309 + m.b310 + m.b311 + m.b312 + m.b313 + m.b314 + m.b315 + m.b316
                         + m.b317 + m.b318 == 1)

m.c26 = Constraint(expr=   m.b319 + m.b320 + m.b321 + m.b322 + m.b323 + m.b324 + m.b325 + m.b326 + m.b327 + m.b328
                         + m.b329 + m.b330 == 1)

m.c27 = Constraint(expr=   m.b331 + m.b332 + m.b333 + m.b334 + m.b335 + m.b336 + m.b337 + m.b338 + m.b339 + m.b340
                         + m.b341 + m.b342 == 1)

m.c28 = Constraint(expr=-(m.b178*m.x344 + m.b179*m.x345 + m.b180*m.x346 + m.b181*m.x347 + m.b182*m.x348 + m.b183*m.x349
                         + m.b184*m.x350 + m.b185*m.x351 + m.b186*m.x352) + m.x85 - 1.25*m.b175 - 1.25*m.b176
                         - 1.25*m.b177 == 0)

m.c29 = Constraint(expr=-(m.b190*m.x344 + m.b191*m.x345 + m.b192*m.x346 + m.b193*m.x347 + m.b194*m.x348 + m.b195*m.x349
                         + m.b196*m.x350 + m.b197*m.x351 + m.b198*m.x352) + m.x91 - 1.25*m.b187 - 1.25*m.b188
                         - 1.25*m.b189 == 0)

m.c30 = Constraint(expr=-(m.b202*m.x344 + m.b203*m.x345 + m.b204*m.x346 + m.b205*m.x347 + m.b206*m.x348 + m.b207*m.x349
                         + m.b208*m.x350 + m.b209*m.x351 + m.b210*m.x352) + m.x97 - 1.25*m.b199 - 1.25*m.b200
                         - 1.25*m.b201 == 0)

m.c31 = Constraint(expr=-(m.b214*m.x344 + m.b215*m.x345 + m.b216*m.x346 + m.b217*m.x347 + m.b218*m.x348 + m.b219*m.x349
                         + m.b220*m.x350 + m.b221*m.x351 + m.b222*m.x352) + m.x103 - 1.25*m.b211 - 1.25*m.b212
                         - 1.25*m.b213 == 0)

m.c32 = Constraint(expr=-(m.b226*m.x344 + m.b227*m.x345 + m.b228*m.x346 + m.b229*m.x347 + m.b230*m.x348 + m.b231*m.x349
                         + m.b232*m.x350 + m.b233*m.x351 + m.b234*m.x352) + m.x109 - 1.25*m.b223 - 1.25*m.b224
                         - 1.25*m.b225 == 0)

m.c33 = Constraint(expr=-(m.b238*m.x344 + m.b239*m.x345 + m.b240*m.x346 + m.b241*m.x347 + m.b242*m.x348 + m.b243*m.x349
                         + m.b244*m.x350 + m.b245*m.x351 + m.b246*m.x352) + m.x115 - 1.25*m.b235 - 1.25*m.b236
                         - 1.25*m.b237 == 0)

m.c34 = Constraint(expr=-(m.b250*m.x344 + m.b251*m.x345 + m.b252*m.x346 + m.b253*m.x347 + m.b254*m.x348 + m.b255*m.x349
                         + m.b256*m.x350 + m.b257*m.x351 + m.b258*m.x352) + m.x121 - 1.25*m.b247 - 1.25*m.b248
                         - 1.25*m.b249 == 0)

m.c35 = Constraint(expr=-(m.b262*m.x344 + m.b263*m.x345 + m.b264*m.x346 + m.b265*m.x347 + m.b266*m.x348 + m.b267*m.x349
                         + m.b268*m.x350 + m.b269*m.x351 + m.b270*m.x352) + m.x127 - 1.25*m.b259 - 1.25*m.b260
                         - 1.25*m.b261 == 0)

m.c36 = Constraint(expr=-(m.b274*m.x344 + m.b275*m.x345 + m.b276*m.x346 + m.b277*m.x347 + m.b278*m.x348 + m.b279*m.x349
                         + m.b280*m.x350 + m.b281*m.x351 + m.b282*m.x352) + m.x133 - 1.25*m.b271 - 1.25*m.b272
                         - 1.25*m.b273 == 0)

m.c37 = Constraint(expr=-(m.b286*m.x344 + m.b287*m.x345 + m.b288*m.x346 + m.b289*m.x347 + m.b290*m.x348 + m.b291*m.x349
                         + m.b292*m.x350 + m.b293*m.x351 + m.b294*m.x352) + m.x139 - 1.25*m.b283 - 1.25*m.b284
                         - 1.25*m.b285 == 0)

m.c38 = Constraint(expr=-(m.b298*m.x344 + m.b299*m.x345 + m.b300*m.x346 + m.b301*m.x347 + m.b302*m.x348 + m.b303*m.x349
                         + m.b304*m.x350 + m.b305*m.x351 + m.b306*m.x352) + m.x145 - 1.25*m.b295 - 1.25*m.b296
                         - 1.25*m.b297 == 0)

m.c39 = Constraint(expr=-(m.b310*m.x344 + m.b311*m.x345 + m.b312*m.x346 + m.b313*m.x347 + m.b314*m.x348 + m.b315*m.x349
                         + m.b316*m.x350 + m.b317*m.x351 + m.b318*m.x352) + m.x151 - 1.25*m.b307 - 1.25*m.b308
                         - 1.25*m.b309 == 0)

m.c40 = Constraint(expr=-(m.b322*m.x344 + m.b323*m.x345 + m.b324*m.x346 + m.b325*m.x347 + m.b326*m.x348 + m.b327*m.x349
                         + m.b328*m.x350 + m.b329*m.x351 + m.b330*m.x352) + m.x157 - 1.25*m.b319 - 1.25*m.b320
                         - 1.25*m.b321 == 0)

m.c41 = Constraint(expr=-(m.b334*m.x344 + m.b335*m.x345 + m.b336*m.x346 + m.b337*m.x347 + m.b338*m.x348 + m.b339*m.x349
                         + m.b340*m.x350 + m.b341*m.x351 + m.b342*m.x352) + m.x163 - 1.25*m.b331 - 1.25*m.b332
                         - 1.25*m.b333 == 0)

m.c42 = Constraint(expr=0.63*m.x85*m.x1 + 0.26*m.x91*m.x7 + 0.023*m.x97*m.x13 + 0.007*m.x103*m.x19 + 0.05*m.x121*m.x37
                         + 0.02*m.x127*m.x43 + 0.003*m.x145*m.x61 - m.x1*m.x169 == 0)

m.c43 = Constraint(expr=0.63*m.x86*m.x2 + 0.26*m.x92*m.x8 + 0.023*m.x98*m.x14 + 0.007*m.x104*m.x20 + 0.05*m.x122*m.x38
                         + 0.02*m.x128*m.x44 + 0.003*m.x146*m.x62 - m.x2*m.x170 == 0)

m.c44 = Constraint(expr=0.63*m.x87*m.x3 + 0.26*m.x93*m.x9 + 0.023*m.x99*m.x15 + 0.007*m.x105*m.x21 + 0.05*m.x123*m.x39
                         + 0.02*m.x129*m.x45 + 0.003*m.x147*m.x63 - m.x3*m.x171 == 0)

m.c45 = Constraint(expr=0.63*m.x88*m.x4 + 0.26*m.x94*m.x10 + 0.023*m.x100*m.x16 + 0.007*m.x106*m.x22 + 0.05*m.x124*m.x40
                         + 0.02*m.x130*m.x46 + 0.003*m.x148*m.x64 - m.x4*m.x172 == 0)

m.c46 = Constraint(expr=0.63*m.x89*m.x5 + 0.26*m.x95*m.x11 + 0.023*m.x101*m.x17 + 0.007*m.x107*m.x23 + 0.05*m.x125*m.x41
                         + 0.02*m.x131*m.x47 + 0.003*m.x149*m.x65 - m.x5*m.x173 == 0)

m.c47 = Constraint(expr=0.63*m.x90*m.x6 + 0.26*m.x96*m.x12 + 0.023*m.x102*m.x18 + 0.007*m.x108*m.x24 + 0.05*m.x126*m.x42
                         + 0.02*m.x132*m.x48 + 0.003*m.x150*m.x66 - m.x6*m.x174 == 0)

m.c48 = Constraint(expr=0.13*m.x85*m.x1 + 0.572*m.x91*m.x7 + 0.118*m.x97*m.x13 + 0.015*m.x103*m.x19 + 0.007*m.x109*m.x25
                         + 0.09*m.x121*m.x37 + 0.048*m.x127*m.x43 + 0.01*m.x133*m.x49 + 0.007*m.x145*m.x61 + 0.003*
                        m.x151*m.x67 - m.x7*m.x169 == 0)

m.c49 = Constraint(expr=0.13*m.x86*m.x2 + 0.572*m.x92*m.x8 + 0.118*m.x98*m.x14 + 0.015*m.x104*m.x20 + 0.007*m.x110*m.x26
                         + 0.09*m.x122*m.x38 + 0.048*m.x128*m.x44 + 0.01*m.x134*m.x50 + 0.007*m.x146*m.x62 + 0.003*
                        m.x152*m.x68 - m.x8*m.x170 == 0)

m.c50 = Constraint(expr=0.13*m.x87*m.x3 + 0.572*m.x93*m.x9 + 0.118*m.x99*m.x15 + 0.015*m.x105*m.x21 + 0.007*m.x111*m.x27
                         + 0.09*m.x123*m.x39 + 0.048*m.x129*m.x45 + 0.01*m.x135*m.x51 + 0.007*m.x147*m.x63 + 0.003*
                        m.x153*m.x69 - m.x9*m.x171 == 0)

m.c51 = Constraint(expr=0.13*m.x88*m.x4 + 0.572*m.x94*m.x10 + 0.118*m.x100*m.x16 + 0.015*m.x106*m.x22 + 0.007*m.x112*
                        m.x28 + 0.09*m.x124*m.x40 + 0.048*m.x130*m.x46 + 0.01*m.x136*m.x52 + 0.007*m.x148*m.x64 + 0.003*
                        m.x154*m.x70 - m.x10*m.x172 == 0)

m.c52 = Constraint(expr=0.13*m.x89*m.x5 + 0.572*m.x95*m.x11 + 0.118*m.x101*m.x17 + 0.015*m.x107*m.x23 + 0.007*m.x113*
                        m.x29 + 0.09*m.x125*m.x41 + 0.048*m.x131*m.x47 + 0.01*m.x137*m.x53 + 0.007*m.x149*m.x65 + 0.003*
                        m.x155*m.x71 - m.x11*m.x173 == 0)

m.c53 = Constraint(expr=0.13*m.x90*m.x6 + 0.572*m.x96*m.x12 + 0.118*m.x102*m.x18 + 0.015*m.x108*m.x24 + 0.007*m.x114*
                        m.x30 + 0.09*m.x126*m.x42 + 0.048*m.x132*m.x48 + 0.01*m.x138*m.x54 + 0.007*m.x150*m.x66 + 0.003*
                        m.x156*m.x72 - m.x12*m.x174 == 0)

m.c54 = Constraint(expr=0.015*m.x85*m.x1 + 0.132*m.x91*m.x7 + 0.518*m.x97*m.x13 + 0.115*m.x103*m.x19 + 0.015*m.x109*
                        m.x25 + 0.007*m.x115*m.x31 + 0.047*m.x121*m.x37 + 0.083*m.x127*m.x43 + 0.04*m.x133*m.x49 + 0.01*
                        m.x139*m.x55 + 0.008*m.x145*m.x61 + 0.007*m.x151*m.x67 + 0.003*m.x157*m.x73 - m.x13*m.x169 == 0)

m.c55 = Constraint(expr=0.015*m.x86*m.x2 + 0.132*m.x92*m.x8 + 0.518*m.x98*m.x14 + 0.115*m.x104*m.x20 + 0.015*m.x110*
                        m.x26 + 0.007*m.x116*m.x32 + 0.047*m.x122*m.x38 + 0.083*m.x128*m.x44 + 0.04*m.x134*m.x50 + 0.01*
                        m.x140*m.x56 + 0.008*m.x146*m.x62 + 0.007*m.x152*m.x68 + 0.003*m.x158*m.x74 - m.x14*m.x170 == 0)

m.c56 = Constraint(expr=0.015*m.x87*m.x3 + 0.132*m.x93*m.x9 + 0.518*m.x99*m.x15 + 0.115*m.x105*m.x21 + 0.015*m.x111*
                        m.x27 + 0.007*m.x117*m.x33 + 0.047*m.x123*m.x39 + 0.083*m.x129*m.x45 + 0.04*m.x135*m.x51 + 0.01*
                        m.x141*m.x57 + 0.008*m.x147*m.x63 + 0.007*m.x153*m.x69 + 0.003*m.x159*m.x75 - m.x15*m.x171 == 0)

m.c57 = Constraint(expr=0.015*m.x88*m.x4 + 0.132*m.x94*m.x10 + 0.518*m.x100*m.x16 + 0.115*m.x106*m.x22 + 0.015*m.x112*
                        m.x28 + 0.007*m.x118*m.x34 + 0.047*m.x124*m.x40 + 0.083*m.x130*m.x46 + 0.04*m.x136*m.x52 + 0.01*
                        m.x142*m.x58 + 0.008*m.x148*m.x64 + 0.007*m.x154*m.x70 + 0.003*m.x160*m.x76 - m.x16*m.x172 == 0)

m.c58 = Constraint(expr=0.015*m.x89*m.x5 + 0.132*m.x95*m.x11 + 0.518*m.x101*m.x17 + 0.115*m.x107*m.x23 + 0.015*m.x113*
                        m.x29 + 0.007*m.x119*m.x35 + 0.047*m.x125*m.x41 + 0.083*m.x131*m.x47 + 0.04*m.x137*m.x53 + 0.01*
                        m.x143*m.x59 + 0.008*m.x149*m.x65 + 0.007*m.x155*m.x71 + 0.003*m.x161*m.x77 - m.x17*m.x173 == 0)

m.c59 = Constraint(expr=0.015*m.x90*m.x6 + 0.132*m.x96*m.x12 + 0.518*m.x102*m.x18 + 0.115*m.x108*m.x24 + 0.015*m.x114*
                        m.x30 + 0.007*m.x120*m.x36 + 0.047*m.x126*m.x42 + 0.083*m.x132*m.x48 + 0.04*m.x138*m.x54 + 0.01*
                        m.x144*m.x60 + 0.008*m.x150*m.x66 + 0.007*m.x156*m.x72 + 0.003*m.x162*m.x78 - m.x18*m.x174 == 0)

m.c60 = Constraint(expr=0.022*m.x91*m.x7 + 0.115*m.x97*m.x13 + 0.515*m.x103*m.x19 + 0.115*m.x109*m.x25 + 0.015*m.x115*
                        m.x31 + 0.01*m.x121*m.x37 + 0.05*m.x127*m.x43 + 0.083*m.x133*m.x49 + 0.04*m.x139*m.x55 + 0.008*
                        m.x151*m.x67 + 0.007*m.x157*m.x73 - m.x19*m.x169 == 0)

m.c61 = Constraint(expr=0.022*m.x92*m.x8 + 0.115*m.x98*m.x14 + 0.515*m.x104*m.x20 + 0.115*m.x110*m.x26 + 0.015*m.x116*
                        m.x32 + 0.01*m.x122*m.x38 + 0.05*m.x128*m.x44 + 0.083*m.x134*m.x50 + 0.04*m.x140*m.x56 + 0.008*
                        m.x152*m.x68 + 0.007*m.x158*m.x74 - m.x20*m.x170 == 0)

m.c62 = Constraint(expr=0.022*m.x93*m.x9 + 0.115*m.x99*m.x15 + 0.515*m.x105*m.x21 + 0.115*m.x111*m.x27 + 0.015*m.x117*
                        m.x33 + 0.01*m.x123*m.x39 + 0.05*m.x129*m.x45 + 0.083*m.x135*m.x51 + 0.04*m.x141*m.x57 + 0.008*
                        m.x153*m.x69 + 0.007*m.x159*m.x75 - m.x21*m.x171 == 0)

m.c63 = Constraint(expr=0.022*m.x94*m.x10 + 0.115*m.x100*m.x16 + 0.515*m.x106*m.x22 + 0.115*m.x112*m.x28 + 0.015*m.x118*
                        m.x34 + 0.01*m.x124*m.x40 + 0.05*m.x130*m.x46 + 0.083*m.x136*m.x52 + 0.04*m.x142*m.x58 + 0.008*
                        m.x154*m.x70 + 0.007*m.x160*m.x76 - m.x22*m.x172 == 0)

m.c64 = Constraint(expr=0.022*m.x95*m.x11 + 0.115*m.x101*m.x17 + 0.515*m.x107*m.x23 + 0.115*m.x113*m.x29 + 0.015*m.x119*
                        m.x35 + 0.01*m.x125*m.x41 + 0.05*m.x131*m.x47 + 0.083*m.x137*m.x53 + 0.04*m.x143*m.x59 + 0.008*
                        m.x155*m.x71 + 0.007*m.x161*m.x77 - m.x23*m.x173 == 0)

m.c65 = Constraint(expr=0.022*m.x96*m.x12 + 0.115*m.x102*m.x18 + 0.515*m.x108*m.x24 + 0.115*m.x114*m.x30 + 0.015*m.x120*
                        m.x36 + 0.01*m.x126*m.x42 + 0.05*m.x132*m.x48 + 0.083*m.x138*m.x54 + 0.04*m.x144*m.x60 + 0.008*
                        m.x156*m.x72 + 0.007*m.x162*m.x78 - m.x24*m.x174 == 0)

m.c66 = Constraint(expr=0.015*m.x97*m.x13 + 0.115*m.x103*m.x19 + 0.515*m.x109*m.x25 + 0.115*m.x115*m.x31 + 0.007*m.x121*
                        m.x37 + 0.01*m.x127*m.x43 + 0.047*m.x133*m.x49 + 0.083*m.x139*m.x55 + 0.003*m.x145*m.x61 + 0.008
                        *m.x157*m.x73 - m.x25*m.x169 == 0)

m.c67 = Constraint(expr=0.015*m.x98*m.x14 + 0.115*m.x104*m.x20 + 0.515*m.x110*m.x26 + 0.115*m.x116*m.x32 + 0.007*m.x122*
                        m.x38 + 0.01*m.x128*m.x44 + 0.047*m.x134*m.x50 + 0.083*m.x140*m.x56 + 0.003*m.x146*m.x62 + 0.008
                        *m.x158*m.x74 - m.x26*m.x170 == 0)

m.c68 = Constraint(expr=0.015*m.x99*m.x15 + 0.115*m.x105*m.x21 + 0.515*m.x111*m.x27 + 0.115*m.x117*m.x33 + 0.007*m.x123*
                        m.x39 + 0.01*m.x129*m.x45 + 0.047*m.x135*m.x51 + 0.083*m.x141*m.x57 + 0.003*m.x147*m.x63 + 0.008
                        *m.x159*m.x75 - m.x27*m.x171 == 0)

m.c69 = Constraint(expr=0.015*m.x100*m.x16 + 0.115*m.x106*m.x22 + 0.515*m.x112*m.x28 + 0.115*m.x118*m.x34 + 0.007*m.x124
                        *m.x40 + 0.01*m.x130*m.x46 + 0.047*m.x136*m.x52 + 0.083*m.x142*m.x58 + 0.003*m.x148*m.x64 + 
                        0.008*m.x160*m.x76 - m.x28*m.x172 == 0)

m.c70 = Constraint(expr=0.015*m.x101*m.x17 + 0.115*m.x107*m.x23 + 0.515*m.x113*m.x29 + 0.115*m.x119*m.x35 + 0.007*m.x125
                        *m.x41 + 0.01*m.x131*m.x47 + 0.047*m.x137*m.x53 + 0.083*m.x143*m.x59 + 0.003*m.x149*m.x65 + 
                        0.008*m.x161*m.x77 - m.x29*m.x173 == 0)

m.c71 = Constraint(expr=0.015*m.x102*m.x18 + 0.115*m.x108*m.x24 + 0.515*m.x114*m.x30 + 0.115*m.x120*m.x36 + 0.007*m.x126
                        *m.x42 + 0.01*m.x132*m.x48 + 0.047*m.x138*m.x54 + 0.083*m.x144*m.x60 + 0.003*m.x150*m.x66 + 
                        0.008*m.x162*m.x78 - m.x30*m.x174 == 0)

m.c72 = Constraint(expr=0.015*m.x103*m.x19 + 0.115*m.x109*m.x25 + 0.515*m.x115*m.x31 + 0.007*m.x127*m.x43 + 0.01*m.x133*
                        m.x49 + 0.047*m.x139*m.x55 + 0.003*m.x151*m.x67 - m.x31*m.x169 == 0)

m.c73 = Constraint(expr=0.015*m.x104*m.x20 + 0.115*m.x110*m.x26 + 0.515*m.x116*m.x32 + 0.007*m.x128*m.x44 + 0.01*m.x134*
                        m.x50 + 0.047*m.x140*m.x56 + 0.003*m.x152*m.x68 - m.x32*m.x170 == 0)

m.c74 = Constraint(expr=0.015*m.x105*m.x21 + 0.115*m.x111*m.x27 + 0.515*m.x117*m.x33 + 0.007*m.x129*m.x45 + 0.01*m.x135*
                        m.x51 + 0.047*m.x141*m.x57 + 0.003*m.x153*m.x69 - m.x33*m.x171 == 0)

m.c75 = Constraint(expr=0.015*m.x106*m.x22 + 0.115*m.x112*m.x28 + 0.515*m.x118*m.x34 + 0.007*m.x130*m.x46 + 0.01*m.x136*
                        m.x52 + 0.047*m.x142*m.x58 + 0.003*m.x154*m.x70 - m.x34*m.x172 == 0)

m.c76 = Constraint(expr=0.015*m.x107*m.x23 + 0.115*m.x113*m.x29 + 0.515*m.x119*m.x35 + 0.007*m.x131*m.x47 + 0.01*m.x137*
                        m.x53 + 0.047*m.x143*m.x59 + 0.003*m.x155*m.x71 - m.x35*m.x173 == 0)

m.c77 = Constraint(expr=0.015*m.x108*m.x24 + 0.115*m.x114*m.x30 + 0.515*m.x120*m.x36 + 0.007*m.x132*m.x48 + 0.01*m.x138*
                        m.x54 + 0.047*m.x144*m.x60 + 0.003*m.x156*m.x72 - m.x36*m.x174 == 0)

m.c78 = Constraint(expr=0.057*m.x85*m.x1 + 0.166*m.x91*m.x7 + 0.087*m.x97*m.x13 + 0.013*m.x103*m.x19 + 0.007*m.x109*
                        m.x25 + 0.44*m.x121*m.x37 + 0.157*m.x127*m.x43 + 0.016*m.x133*m.x49 + 0.04*m.x145*m.x61 + 0.014*
                        m.x151*m.x67 + 0.003*m.x163*m.x79 - m.x37*m.x169 == 0)

m.c79 = Constraint(expr=0.057*m.x86*m.x2 + 0.166*m.x92*m.x8 + 0.087*m.x98*m.x14 + 0.013*m.x104*m.x20 + 0.007*m.x110*
                        m.x26 + 0.44*m.x122*m.x38 + 0.157*m.x128*m.x44 + 0.016*m.x134*m.x50 + 0.04*m.x146*m.x62 + 0.014*
                        m.x152*m.x68 + 0.003*m.x164*m.x80 - m.x38*m.x170 == 0)

m.c80 = Constraint(expr=0.057*m.x87*m.x3 + 0.166*m.x93*m.x9 + 0.087*m.x99*m.x15 + 0.013*m.x105*m.x21 + 0.007*m.x111*
                        m.x27 + 0.44*m.x123*m.x39 + 0.157*m.x129*m.x45 + 0.016*m.x135*m.x51 + 0.04*m.x147*m.x63 + 0.014*
                        m.x153*m.x69 + 0.003*m.x165*m.x81 - m.x39*m.x171 == 0)

m.c81 = Constraint(expr=0.057*m.x88*m.x4 + 0.166*m.x94*m.x10 + 0.087*m.x100*m.x16 + 0.013*m.x106*m.x22 + 0.007*m.x112*
                        m.x28 + 0.44*m.x124*m.x40 + 0.157*m.x130*m.x46 + 0.016*m.x136*m.x52 + 0.04*m.x148*m.x64 + 0.014*
                        m.x154*m.x70 + 0.003*m.x166*m.x82 - m.x40*m.x172 == 0)

m.c82 = Constraint(expr=0.057*m.x89*m.x5 + 0.166*m.x95*m.x11 + 0.087*m.x101*m.x17 + 0.013*m.x107*m.x23 + 0.007*m.x113*
                        m.x29 + 0.44*m.x125*m.x41 + 0.157*m.x131*m.x47 + 0.016*m.x137*m.x53 + 0.04*m.x149*m.x65 + 0.014*
                        m.x155*m.x71 + 0.003*m.x167*m.x83 - m.x41*m.x173 == 0)

m.c83 = Constraint(expr=0.057*m.x90*m.x6 + 0.166*m.x96*m.x12 + 0.087*m.x102*m.x18 + 0.013*m.x108*m.x24 + 0.007*m.x114*
                        m.x30 + 0.44*m.x126*m.x42 + 0.157*m.x132*m.x48 + 0.016*m.x138*m.x54 + 0.04*m.x150*m.x66 + 0.014*
                        m.x156*m.x72 + 0.003*m.x168*m.x84 - m.x42*m.x174 == 0)

m.c84 = Constraint(expr=0.01*m.x85*m.x1 + 0.055*m.x91*m.x7 + 0.097*m.x97*m.x13 + 0.043*m.x103*m.x19 + 0.01*m.x109*m.x25
                         + 0.007*m.x115*m.x31 + 0.075*m.x121*m.x37 + 0.48*m.x127*m.x43 + 0.075*m.x133*m.x49 + 0.008*
                        m.x139*m.x55 + 0.075*m.x145*m.x61 + 0.048*m.x151*m.x67 + 0.007*m.x157*m.x73 + 0.007*m.x163*m.x79
                         - m.x43*m.x169 == 0)

m.c85 = Constraint(expr=0.01*m.x86*m.x2 + 0.055*m.x92*m.x8 + 0.097*m.x98*m.x14 + 0.043*m.x104*m.x20 + 0.01*m.x110*m.x26
                         + 0.007*m.x116*m.x32 + 0.075*m.x122*m.x38 + 0.48*m.x128*m.x44 + 0.075*m.x134*m.x50 + 0.008*
                        m.x140*m.x56 + 0.075*m.x146*m.x62 + 0.048*m.x152*m.x68 + 0.007*m.x158*m.x74 + 0.007*m.x164*m.x80
                         - m.x44*m.x170 == 0)

m.c86 = Constraint(expr=0.01*m.x87*m.x3 + 0.055*m.x93*m.x9 + 0.097*m.x99*m.x15 + 0.043*m.x105*m.x21 + 0.01*m.x111*m.x27
                         + 0.007*m.x117*m.x33 + 0.075*m.x123*m.x39 + 0.48*m.x129*m.x45 + 0.075*m.x135*m.x51 + 0.008*
                        m.x141*m.x57 + 0.075*m.x147*m.x63 + 0.048*m.x153*m.x69 + 0.007*m.x159*m.x75 + 0.007*m.x165*m.x81
                         - m.x45*m.x171 == 0)

m.c87 = Constraint(expr=0.01*m.x88*m.x4 + 0.055*m.x94*m.x10 + 0.097*m.x100*m.x16 + 0.043*m.x106*m.x22 + 0.01*m.x112*
                        m.x28 + 0.007*m.x118*m.x34 + 0.075*m.x124*m.x40 + 0.48*m.x130*m.x46 + 0.075*m.x136*m.x52 + 0.008
                        *m.x142*m.x58 + 0.075*m.x148*m.x64 + 0.048*m.x154*m.x70 + 0.007*m.x160*m.x76 + 0.007*m.x166*
                        m.x82 - m.x46*m.x172 == 0)

m.c88 = Constraint(expr=0.01*m.x89*m.x5 + 0.055*m.x95*m.x11 + 0.097*m.x101*m.x17 + 0.043*m.x107*m.x23 + 0.01*m.x113*
                        m.x29 + 0.007*m.x119*m.x35 + 0.075*m.x125*m.x41 + 0.48*m.x131*m.x47 + 0.075*m.x137*m.x53 + 0.008
                        *m.x143*m.x59 + 0.075*m.x149*m.x65 + 0.048*m.x155*m.x71 + 0.007*m.x161*m.x77 + 0.007*m.x167*
                        m.x83 - m.x47*m.x173 == 0)

m.c89 = Constraint(expr=0.01*m.x90*m.x6 + 0.055*m.x96*m.x12 + 0.097*m.x102*m.x18 + 0.043*m.x108*m.x24 + 0.01*m.x114*
                        m.x30 + 0.007*m.x120*m.x36 + 0.075*m.x126*m.x42 + 0.48*m.x132*m.x48 + 0.075*m.x138*m.x54 + 0.008
                        *m.x144*m.x60 + 0.075*m.x150*m.x66 + 0.048*m.x156*m.x72 + 0.007*m.x162*m.x78 + 0.007*m.x168*
                        m.x84 - m.x48*m.x174 == 0)

m.c90 = Constraint(expr=0.01*m.x91*m.x7 + 0.054*m.x97*m.x13 + 0.083*m.x103*m.x19 + 0.04*m.x109*m.x25 + 0.01*m.x115*m.x31
                         + 0.008*m.x121*m.x37 + 0.082*m.x127*m.x43 + 0.443*m.x133*m.x49 + 0.075*m.x139*m.x55 + 0.04*
                        m.x145*m.x61 + 0.075*m.x151*m.x67 + 0.04*m.x157*m.x73 + 0.008*m.x163*m.x79 - m.x49*m.x169 == 0)

m.c91 = Constraint(expr=0.01*m.x92*m.x8 + 0.054*m.x98*m.x14 + 0.083*m.x104*m.x20 + 0.04*m.x110*m.x26 + 0.01*m.x116*m.x32
                         + 0.008*m.x122*m.x38 + 0.082*m.x128*m.x44 + 0.443*m.x134*m.x50 + 0.075*m.x140*m.x56 + 0.04*
                        m.x146*m.x62 + 0.075*m.x152*m.x68 + 0.04*m.x158*m.x74 + 0.008*m.x164*m.x80 - m.x50*m.x170 == 0)

m.c92 = Constraint(expr=0.01*m.x93*m.x9 + 0.054*m.x99*m.x15 + 0.083*m.x105*m.x21 + 0.04*m.x111*m.x27 + 0.01*m.x117*m.x33
                         + 0.008*m.x123*m.x39 + 0.082*m.x129*m.x45 + 0.443*m.x135*m.x51 + 0.075*m.x141*m.x57 + 0.04*
                        m.x147*m.x63 + 0.075*m.x153*m.x69 + 0.04*m.x159*m.x75 + 0.008*m.x165*m.x81 - m.x51*m.x171 == 0)

m.c93 = Constraint(expr=0.01*m.x94*m.x10 + 0.054*m.x100*m.x16 + 0.083*m.x106*m.x22 + 0.04*m.x112*m.x28 + 0.01*m.x118*
                        m.x34 + 0.008*m.x124*m.x40 + 0.082*m.x130*m.x46 + 0.443*m.x136*m.x52 + 0.075*m.x142*m.x58 + 0.04
                        *m.x148*m.x64 + 0.075*m.x154*m.x70 + 0.04*m.x160*m.x76 + 0.008*m.x166*m.x82 - m.x52*m.x172 == 0)

m.c94 = Constraint(expr=0.01*m.x95*m.x11 + 0.054*m.x101*m.x17 + 0.083*m.x107*m.x23 + 0.04*m.x113*m.x29 + 0.01*m.x119*
                        m.x35 + 0.008*m.x125*m.x41 + 0.082*m.x131*m.x47 + 0.443*m.x137*m.x53 + 0.075*m.x143*m.x59 + 0.04
                        *m.x149*m.x65 + 0.075*m.x155*m.x71 + 0.04*m.x161*m.x77 + 0.008*m.x167*m.x83 - m.x53*m.x173 == 0)

m.c95 = Constraint(expr=0.01*m.x96*m.x12 + 0.054*m.x102*m.x18 + 0.083*m.x108*m.x24 + 0.04*m.x114*m.x30 + 0.01*m.x120*
                        m.x36 + 0.008*m.x126*m.x42 + 0.082*m.x132*m.x48 + 0.443*m.x138*m.x54 + 0.075*m.x144*m.x60 + 0.04
                        *m.x150*m.x66 + 0.075*m.x156*m.x72 + 0.04*m.x162*m.x78 + 0.008*m.x168*m.x84 - m.x54*m.x174 == 0)

m.c96 = Constraint(expr=0.01*m.x97*m.x13 + 0.047*m.x103*m.x19 + 0.083*m.x109*m.x25 + 0.04*m.x115*m.x31 + 0.015*m.x127*
                        m.x43 + 0.075*m.x133*m.x49 + 0.44*m.x139*m.x55 + 0.007*m.x145*m.x61 + 0.043*m.x151*m.x67 + 0.075
                        *m.x157*m.x73 - m.x55*m.x169 == 0)

m.c97 = Constraint(expr=0.01*m.x98*m.x14 + 0.047*m.x104*m.x20 + 0.083*m.x110*m.x26 + 0.04*m.x116*m.x32 + 0.015*m.x128*
                        m.x44 + 0.075*m.x134*m.x50 + 0.44*m.x140*m.x56 + 0.007*m.x146*m.x62 + 0.043*m.x152*m.x68 + 0.075
                        *m.x158*m.x74 - m.x56*m.x170 == 0)

m.c98 = Constraint(expr=0.01*m.x99*m.x15 + 0.047*m.x105*m.x21 + 0.083*m.x111*m.x27 + 0.04*m.x117*m.x33 + 0.015*m.x129*
                        m.x45 + 0.075*m.x135*m.x51 + 0.44*m.x141*m.x57 + 0.007*m.x147*m.x63 + 0.043*m.x153*m.x69 + 0.075
                        *m.x159*m.x75 - m.x57*m.x171 == 0)

m.c99 = Constraint(expr=0.01*m.x100*m.x16 + 0.047*m.x106*m.x22 + 0.083*m.x112*m.x28 + 0.04*m.x118*m.x34 + 0.015*m.x130*
                        m.x46 + 0.075*m.x136*m.x52 + 0.44*m.x142*m.x58 + 0.007*m.x148*m.x64 + 0.043*m.x154*m.x70 + 0.075
                        *m.x160*m.x76 - m.x58*m.x172 == 0)

m.c100 = Constraint(expr=0.01*m.x101*m.x17 + 0.047*m.x107*m.x23 + 0.083*m.x113*m.x29 + 0.04*m.x119*m.x35 + 0.015*m.x131*
                         m.x47 + 0.075*m.x137*m.x53 + 0.44*m.x143*m.x59 + 0.007*m.x149*m.x65 + 0.043*m.x155*m.x71 + 
                         0.075*m.x161*m.x77 - m.x59*m.x173 == 0)

m.c101 = Constraint(expr=0.01*m.x102*m.x18 + 0.047*m.x108*m.x24 + 0.083*m.x114*m.x30 + 0.04*m.x120*m.x36 + 0.015*m.x132*
                         m.x48 + 0.075*m.x138*m.x54 + 0.44*m.x144*m.x60 + 0.007*m.x150*m.x66 + 0.043*m.x156*m.x72 + 
                         0.075*m.x162*m.x78 - m.x60*m.x174 == 0)

m.c102 = Constraint(expr=0.003*m.x85*m.x1 + 0.014*m.x91*m.x7 + 0.016*m.x97*m.x13 + 0.014*m.x103*m.x19 + 0.006*m.x109*
                         m.x25 + 0.04*m.x121*m.x37 + 0.15*m.x127*m.x43 + 0.08*m.x133*m.x49 + 0.007*m.x139*m.x55 + 0.44*
                         m.x145*m.x61 + 0.15*m.x151*m.x67 + 0.016*m.x157*m.x73 + 0.04*m.x163*m.x79 - m.x61*m.x169 == 0)

m.c103 = Constraint(expr=0.003*m.x86*m.x2 + 0.014*m.x92*m.x8 + 0.016*m.x98*m.x14 + 0.014*m.x104*m.x20 + 0.006*m.x110*
                         m.x26 + 0.04*m.x122*m.x38 + 0.15*m.x128*m.x44 + 0.08*m.x134*m.x50 + 0.007*m.x140*m.x56 + 0.44*
                         m.x146*m.x62 + 0.15*m.x152*m.x68 + 0.016*m.x158*m.x74 + 0.04*m.x164*m.x80 - m.x62*m.x170 == 0)

m.c104 = Constraint(expr=0.003*m.x87*m.x3 + 0.014*m.x93*m.x9 + 0.016*m.x99*m.x15 + 0.014*m.x105*m.x21 + 0.006*m.x111*
                         m.x27 + 0.04*m.x123*m.x39 + 0.15*m.x129*m.x45 + 0.08*m.x135*m.x51 + 0.007*m.x141*m.x57 + 0.44*
                         m.x147*m.x63 + 0.15*m.x153*m.x69 + 0.016*m.x159*m.x75 + 0.04*m.x165*m.x81 - m.x63*m.x171 == 0)

m.c105 = Constraint(expr=0.003*m.x88*m.x4 + 0.014*m.x94*m.x10 + 0.016*m.x100*m.x16 + 0.014*m.x106*m.x22 + 0.006*m.x112*
                         m.x28 + 0.04*m.x124*m.x40 + 0.15*m.x130*m.x46 + 0.08*m.x136*m.x52 + 0.007*m.x142*m.x58 + 0.44*
                         m.x148*m.x64 + 0.15*m.x154*m.x70 + 0.016*m.x160*m.x76 + 0.04*m.x166*m.x82 - m.x64*m.x172 == 0)

m.c106 = Constraint(expr=0.003*m.x89*m.x5 + 0.014*m.x95*m.x11 + 0.016*m.x101*m.x17 + 0.014*m.x107*m.x23 + 0.006*m.x113*
                         m.x29 + 0.04*m.x125*m.x41 + 0.15*m.x131*m.x47 + 0.08*m.x137*m.x53 + 0.007*m.x143*m.x59 + 0.44*
                         m.x149*m.x65 + 0.15*m.x155*m.x71 + 0.016*m.x161*m.x77 + 0.04*m.x167*m.x83 - m.x65*m.x173 == 0)

m.c107 = Constraint(expr=0.003*m.x90*m.x6 + 0.014*m.x96*m.x12 + 0.016*m.x102*m.x18 + 0.014*m.x108*m.x24 + 0.006*m.x114*
                         m.x30 + 0.04*m.x126*m.x42 + 0.15*m.x132*m.x48 + 0.08*m.x138*m.x54 + 0.007*m.x144*m.x60 + 0.44*
                         m.x150*m.x66 + 0.15*m.x156*m.x72 + 0.016*m.x162*m.x78 + 0.04*m.x168*m.x84 - m.x66*m.x174 == 0)

m.c108 = Constraint(expr=0.003*m.x91*m.x7 + 0.007*m.x97*m.x13 + 0.015*m.x103*m.x19 + 0.003*m.x115*m.x31 + 0.007*m.x121*
                         m.x37 + 0.048*m.x127*m.x43 + 0.082*m.x133*m.x49 + 0.043*m.x139*m.x55 + 0.075*m.x145*m.x61 + 
                         0.48*m.x151*m.x67 + 0.075*m.x157*m.x73 + 0.075*m.x163*m.x79 - m.x67*m.x169 == 0)

m.c109 = Constraint(expr=0.003*m.x92*m.x8 + 0.007*m.x98*m.x14 + 0.015*m.x104*m.x20 + 0.003*m.x116*m.x32 + 0.007*m.x122*
                         m.x38 + 0.048*m.x128*m.x44 + 0.082*m.x134*m.x50 + 0.043*m.x140*m.x56 + 0.075*m.x146*m.x62 + 
                         0.48*m.x152*m.x68 + 0.075*m.x158*m.x74 + 0.075*m.x164*m.x80 - m.x68*m.x170 == 0)

m.c110 = Constraint(expr=0.003*m.x93*m.x9 + 0.007*m.x99*m.x15 + 0.015*m.x105*m.x21 + 0.003*m.x117*m.x33 + 0.007*m.x123*
                         m.x39 + 0.048*m.x129*m.x45 + 0.082*m.x135*m.x51 + 0.043*m.x141*m.x57 + 0.075*m.x147*m.x63 + 
                         0.48*m.x153*m.x69 + 0.075*m.x159*m.x75 + 0.075*m.x165*m.x81 - m.x69*m.x171 == 0)

m.c111 = Constraint(expr=0.003*m.x94*m.x10 + 0.007*m.x100*m.x16 + 0.015*m.x106*m.x22 + 0.003*m.x118*m.x34 + 0.007*m.x124
                         *m.x40 + 0.048*m.x130*m.x46 + 0.082*m.x136*m.x52 + 0.043*m.x142*m.x58 + 0.075*m.x148*m.x64 + 
                         0.48*m.x154*m.x70 + 0.075*m.x160*m.x76 + 0.075*m.x166*m.x82 - m.x70*m.x172 == 0)

m.c112 = Constraint(expr=0.003*m.x95*m.x11 + 0.007*m.x101*m.x17 + 0.015*m.x107*m.x23 + 0.003*m.x119*m.x35 + 0.007*m.x125
                         *m.x41 + 0.048*m.x131*m.x47 + 0.082*m.x137*m.x53 + 0.043*m.x143*m.x59 + 0.075*m.x149*m.x65 + 
                         0.48*m.x155*m.x71 + 0.075*m.x161*m.x77 + 0.075*m.x167*m.x83 - m.x71*m.x173 == 0)

m.c113 = Constraint(expr=0.003*m.x96*m.x12 + 0.007*m.x102*m.x18 + 0.015*m.x108*m.x24 + 0.003*m.x120*m.x36 + 0.007*m.x126
                         *m.x42 + 0.048*m.x132*m.x48 + 0.082*m.x138*m.x54 + 0.043*m.x144*m.x60 + 0.075*m.x150*m.x66 + 
                         0.48*m.x156*m.x72 + 0.075*m.x162*m.x78 + 0.075*m.x168*m.x84 - m.x72*m.x174 == 0)

m.c114 = Constraint(expr=0.003*m.x97*m.x13 + 0.007*m.x103*m.x19 + 0.008*m.x109*m.x25 + 0.007*m.x127*m.x43 + 0.047*m.x133
                         *m.x49 + 0.075*m.x139*m.x55 + 0.008*m.x145*m.x61 + 0.082*m.x151*m.x67 + 0.443*m.x157*m.x73 + 
                         0.04*m.x163*m.x79 - m.x73*m.x169 == 0)

m.c115 = Constraint(expr=0.003*m.x98*m.x14 + 0.007*m.x104*m.x20 + 0.008*m.x110*m.x26 + 0.007*m.x128*m.x44 + 0.047*m.x134
                         *m.x50 + 0.075*m.x140*m.x56 + 0.008*m.x146*m.x62 + 0.082*m.x152*m.x68 + 0.443*m.x158*m.x74 + 
                         0.04*m.x164*m.x80 - m.x74*m.x170 == 0)

m.c116 = Constraint(expr=0.003*m.x99*m.x15 + 0.007*m.x105*m.x21 + 0.008*m.x111*m.x27 + 0.007*m.x129*m.x45 + 0.047*m.x135
                         *m.x51 + 0.075*m.x141*m.x57 + 0.008*m.x147*m.x63 + 0.082*m.x153*m.x69 + 0.443*m.x159*m.x75 + 
                         0.04*m.x165*m.x81 - m.x75*m.x171 == 0)

m.c117 = Constraint(expr=0.003*m.x100*m.x16 + 0.007*m.x106*m.x22 + 0.008*m.x112*m.x28 + 0.007*m.x130*m.x46 + 0.047*
                         m.x136*m.x52 + 0.075*m.x142*m.x58 + 0.008*m.x148*m.x64 + 0.082*m.x154*m.x70 + 0.443*m.x160*
                         m.x76 + 0.04*m.x166*m.x82 - m.x76*m.x172 == 0)

m.c118 = Constraint(expr=0.003*m.x101*m.x17 + 0.007*m.x107*m.x23 + 0.008*m.x113*m.x29 + 0.007*m.x131*m.x47 + 0.047*
                         m.x137*m.x53 + 0.075*m.x143*m.x59 + 0.008*m.x149*m.x65 + 0.082*m.x155*m.x71 + 0.443*m.x161*
                         m.x77 + 0.04*m.x167*m.x83 - m.x77*m.x173 == 0)

m.c119 = Constraint(expr=0.003*m.x102*m.x18 + 0.007*m.x108*m.x24 + 0.008*m.x114*m.x30 + 0.007*m.x132*m.x48 + 0.047*
                         m.x138*m.x54 + 0.075*m.x144*m.x60 + 0.008*m.x150*m.x66 + 0.082*m.x156*m.x72 + 0.443*m.x162*
                         m.x78 + 0.04*m.x168*m.x84 - m.x78*m.x174 == 0)

m.c120 = Constraint(expr=0.007*m.x109*m.x25 + 0.003*m.x121*m.x37 + 0.014*m.x127*m.x43 + 0.016*m.x133*m.x49 + 0.007*
                         m.x139*m.x55 + 0.04*m.x145*m.x61 + 0.15*m.x151*m.x67 + 0.08*m.x157*m.x73 + 0.44*m.x163*m.x79 - 
                         m.x79*m.x169 == 0)

m.c121 = Constraint(expr=0.007*m.x110*m.x26 + 0.003*m.x122*m.x38 + 0.014*m.x128*m.x44 + 0.016*m.x134*m.x50 + 0.007*
                         m.x140*m.x56 + 0.04*m.x146*m.x62 + 0.15*m.x152*m.x68 + 0.08*m.x158*m.x74 + 0.44*m.x164*m.x80 - 
                         m.x80*m.x170 == 0)

m.c122 = Constraint(expr=0.007*m.x111*m.x27 + 0.003*m.x123*m.x39 + 0.014*m.x129*m.x45 + 0.016*m.x135*m.x51 + 0.007*
                         m.x141*m.x57 + 0.04*m.x147*m.x63 + 0.15*m.x153*m.x69 + 0.08*m.x159*m.x75 + 0.44*m.x165*m.x81 - 
                         m.x81*m.x171 == 0)

m.c123 = Constraint(expr=0.007*m.x112*m.x28 + 0.003*m.x124*m.x40 + 0.014*m.x130*m.x46 + 0.016*m.x136*m.x52 + 0.007*
                         m.x142*m.x58 + 0.04*m.x148*m.x64 + 0.15*m.x154*m.x70 + 0.08*m.x160*m.x76 + 0.44*m.x166*m.x82 - 
                         m.x82*m.x172 == 0)

m.c124 = Constraint(expr=0.007*m.x113*m.x29 + 0.003*m.x125*m.x41 + 0.014*m.x131*m.x47 + 0.016*m.x137*m.x53 + 0.007*
                         m.x143*m.x59 + 0.04*m.x149*m.x65 + 0.15*m.x155*m.x71 + 0.08*m.x161*m.x77 + 0.44*m.x167*m.x83 - 
                         m.x83*m.x173 == 0)

m.c125 = Constraint(expr=0.007*m.x114*m.x30 + 0.003*m.x126*m.x42 + 0.014*m.x132*m.x48 + 0.016*m.x138*m.x54 + 0.007*
                         m.x144*m.x60 + 0.04*m.x150*m.x66 + 0.15*m.x156*m.x72 + 0.08*m.x162*m.x78 + 0.44*m.x168*m.x84 - 
                         m.x84*m.x174 == 0)

m.c126 = Constraint(expr=-(m.x85 - 0.1596*m.x85*m.x1) + m.x86 == 0)

m.c127 = Constraint(expr=-(m.x86 - 0.1596*m.x86*m.x2) + m.x87 == 0)

m.c128 = Constraint(expr=-(m.x87 - 0.1596*m.x87*m.x3) + m.x88 == 0)

m.c129 = Constraint(expr=-(m.x88 - 0.1596*m.x88*m.x4) + m.x89 == 0)

m.c130 = Constraint(expr=-(m.x89 - 0.1596*m.x89*m.x5) + m.x90 == 0)

m.c131 = Constraint(expr=-(m.x91 - 0.1596*m.x91*m.x7) + m.x92 == 0)

m.c132 = Constraint(expr=-(m.x92 - 0.1596*m.x92*m.x8) + m.x93 == 0)

m.c133 = Constraint(expr=-(m.x93 - 0.1596*m.x93*m.x9) + m.x94 == 0)

m.c134 = Constraint(expr=-(m.x94 - 0.1596*m.x94*m.x10) + m.x95 == 0)

m.c135 = Constraint(expr=-(m.x95 - 0.1596*m.x95*m.x11) + m.x96 == 0)

m.c136 = Constraint(expr=-(m.x97 - 0.1596*m.x97*m.x13) + m.x98 == 0)

m.c137 = Constraint(expr=-(m.x98 - 0.1596*m.x98*m.x14) + m.x99 == 0)

m.c138 = Constraint(expr=-(m.x99 - 0.1596*m.x99*m.x15) + m.x100 == 0)

m.c139 = Constraint(expr=-(m.x100 - 0.1596*m.x100*m.x16) + m.x101 == 0)

m.c140 = Constraint(expr=-(m.x101 - 0.1596*m.x101*m.x17) + m.x102 == 0)

m.c141 = Constraint(expr=-(m.x103 - 0.1596*m.x103*m.x19) + m.x104 == 0)

m.c142 = Constraint(expr=-(m.x104 - 0.1596*m.x104*m.x20) + m.x105 == 0)

m.c143 = Constraint(expr=-(m.x105 - 0.1596*m.x105*m.x21) + m.x106 == 0)

m.c144 = Constraint(expr=-(m.x106 - 0.1596*m.x106*m.x22) + m.x107 == 0)

m.c145 = Constraint(expr=-(m.x107 - 0.1596*m.x107*m.x23) + m.x108 == 0)

m.c146 = Constraint(expr=-(m.x109 - 0.1596*m.x109*m.x25) + m.x110 == 0)

m.c147 = Constraint(expr=-(m.x110 - 0.1596*m.x110*m.x26) + m.x111 == 0)

m.c148 = Constraint(expr=-(m.x111 - 0.1596*m.x111*m.x27) + m.x112 == 0)

m.c149 = Constraint(expr=-(m.x112 - 0.1596*m.x112*m.x28) + m.x113 == 0)

m.c150 = Constraint(expr=-(m.x113 - 0.1596*m.x113*m.x29) + m.x114 == 0)

m.c151 = Constraint(expr=-(m.x115 - 0.1596*m.x115*m.x31) + m.x116 == 0)

m.c152 = Constraint(expr=-(m.x116 - 0.1596*m.x116*m.x32) + m.x117 == 0)

m.c153 = Constraint(expr=-(m.x117 - 0.1596*m.x117*m.x33) + m.x118 == 0)

m.c154 = Constraint(expr=-(m.x118 - 0.1596*m.x118*m.x34) + m.x119 == 0)

m.c155 = Constraint(expr=-(m.x119 - 0.1596*m.x119*m.x35) + m.x120 == 0)

m.c156 = Constraint(expr=-(m.x121 - 0.1596*m.x121*m.x37) + m.x122 == 0)

m.c157 = Constraint(expr=-(m.x122 - 0.1596*m.x122*m.x38) + m.x123 == 0)

m.c158 = Constraint(expr=-(m.x123 - 0.1596*m.x123*m.x39) + m.x124 == 0)

m.c159 = Constraint(expr=-(m.x124 - 0.1596*m.x124*m.x40) + m.x125 == 0)

m.c160 = Constraint(expr=-(m.x125 - 0.1596*m.x125*m.x41) + m.x126 == 0)

m.c161 = Constraint(expr=-(m.x127 - 0.1596*m.x127*m.x43) + m.x128 == 0)

m.c162 = Constraint(expr=-(m.x128 - 0.1596*m.x128*m.x44) + m.x129 == 0)

m.c163 = Constraint(expr=-(m.x129 - 0.1596*m.x129*m.x45) + m.x130 == 0)

m.c164 = Constraint(expr=-(m.x130 - 0.1596*m.x130*m.x46) + m.x131 == 0)

m.c165 = Constraint(expr=-(m.x131 - 0.1596*m.x131*m.x47) + m.x132 == 0)

m.c166 = Constraint(expr=-(m.x133 - 0.1596*m.x133*m.x49) + m.x134 == 0)

m.c167 = Constraint(expr=-(m.x134 - 0.1596*m.x134*m.x50) + m.x135 == 0)

m.c168 = Constraint(expr=-(m.x135 - 0.1596*m.x135*m.x51) + m.x136 == 0)

m.c169 = Constraint(expr=-(m.x136 - 0.1596*m.x136*m.x52) + m.x137 == 0)

m.c170 = Constraint(expr=-(m.x137 - 0.1596*m.x137*m.x53) + m.x138 == 0)

m.c171 = Constraint(expr=-(m.x139 - 0.1596*m.x139*m.x55) + m.x140 == 0)

m.c172 = Constraint(expr=-(m.x140 - 0.1596*m.x140*m.x56) + m.x141 == 0)

m.c173 = Constraint(expr=-(m.x141 - 0.1596*m.x141*m.x57) + m.x142 == 0)

m.c174 = Constraint(expr=-(m.x142 - 0.1596*m.x142*m.x58) + m.x143 == 0)

m.c175 = Constraint(expr=-(m.x143 - 0.1596*m.x143*m.x59) + m.x144 == 0)

m.c176 = Constraint(expr=-(m.x145 - 0.1596*m.x145*m.x61) + m.x146 == 0)

m.c177 = Constraint(expr=-(m.x146 - 0.1596*m.x146*m.x62) + m.x147 == 0)

m.c178 = Constraint(expr=-(m.x147 - 0.1596*m.x147*m.x63) + m.x148 == 0)

m.c179 = Constraint(expr=-(m.x148 - 0.1596*m.x148*m.x64) + m.x149 == 0)

m.c180 = Constraint(expr=-(m.x149 - 0.1596*m.x149*m.x65) + m.x150 == 0)

m.c181 = Constraint(expr=-(m.x151 - 0.1596*m.x151*m.x67) + m.x152 == 0)

m.c182 = Constraint(expr=-(m.x152 - 0.1596*m.x152*m.x68) + m.x153 == 0)

m.c183 = Constraint(expr=-(m.x153 - 0.1596*m.x153*m.x69) + m.x154 == 0)

m.c184 = Constraint(expr=-(m.x154 - 0.1596*m.x154*m.x70) + m.x155 == 0)

m.c185 = Constraint(expr=-(m.x155 - 0.1596*m.x155*m.x71) + m.x156 == 0)

m.c186 = Constraint(expr=-(m.x157 - 0.1596*m.x157*m.x73) + m.x158 == 0)

m.c187 = Constraint(expr=-(m.x158 - 0.1596*m.x158*m.x74) + m.x159 == 0)

m.c188 = Constraint(expr=-(m.x159 - 0.1596*m.x159*m.x75) + m.x160 == 0)

m.c189 = Constraint(expr=-(m.x160 - 0.1596*m.x160*m.x76) + m.x161 == 0)

m.c190 = Constraint(expr=-(m.x161 - 0.1596*m.x161*m.x77) + m.x162 == 0)

m.c191 = Constraint(expr=-(m.x163 - 0.1596*m.x163*m.x79) + m.x164 == 0)

m.c192 = Constraint(expr=-(m.x164 - 0.1596*m.x164*m.x80) + m.x165 == 0)

m.c193 = Constraint(expr=-(m.x165 - 0.1596*m.x165*m.x81) + m.x166 == 0)

m.c194 = Constraint(expr=-(m.x166 - 0.1596*m.x166*m.x82) + m.x167 == 0)

m.c195 = Constraint(expr=-(m.x167 - 0.1596*m.x167*m.x83) + m.x168 == 0)

m.c196 = Constraint(expr=0.5*m.x85*m.x1 + m.x91*m.x7 + m.x97*m.x13 + m.x103*m.x19 + m.x109*m.x25 + m.x115*m.x31 + 0.5*
                         m.x121*m.x37 + m.x127*m.x43 + m.x133*m.x49 + m.x139*m.x55 + 0.5*m.x145*m.x61 + m.x151*m.x67 + 
                         m.x157*m.x73 + 0.5*m.x163*m.x79 == 1)

m.c197 = Constraint(expr=0.5*m.x86*m.x2 + m.x92*m.x8 + m.x98*m.x14 + m.x104*m.x20 + m.x110*m.x26 + m.x116*m.x32 + 0.5*
                         m.x122*m.x38 + m.x128*m.x44 + m.x134*m.x50 + m.x140*m.x56 + 0.5*m.x146*m.x62 + m.x152*m.x68 + 
                         m.x158*m.x74 + 0.5*m.x164*m.x80 == 1)

m.c198 = Constraint(expr=0.5*m.x87*m.x3 + m.x93*m.x9 + m.x99*m.x15 + m.x105*m.x21 + m.x111*m.x27 + m.x117*m.x33 + 0.5*
                         m.x123*m.x39 + m.x129*m.x45 + m.x135*m.x51 + m.x141*m.x57 + 0.5*m.x147*m.x63 + m.x153*m.x69 + 
                         m.x159*m.x75 + 0.5*m.x165*m.x81 == 1)

m.c199 = Constraint(expr=0.5*m.x88*m.x4 + m.x94*m.x10 + m.x100*m.x16 + m.x106*m.x22 + m.x112*m.x28 + m.x118*m.x34 + 0.5*
                         m.x124*m.x40 + m.x130*m.x46 + m.x136*m.x52 + m.x142*m.x58 + 0.5*m.x148*m.x64 + m.x154*m.x70 + 
                         m.x160*m.x76 + 0.5*m.x166*m.x82 == 1)

m.c200 = Constraint(expr=0.5*m.x89*m.x5 + m.x95*m.x11 + m.x101*m.x17 + m.x107*m.x23 + m.x113*m.x29 + m.x119*m.x35 + 0.5*
                         m.x125*m.x41 + m.x131*m.x47 + m.x137*m.x53 + m.x143*m.x59 + 0.5*m.x149*m.x65 + m.x155*m.x71 + 
                         m.x161*m.x77 + 0.5*m.x167*m.x83 == 1)

m.c201 = Constraint(expr=0.5*m.x90*m.x6 + m.x96*m.x12 + m.x102*m.x18 + m.x108*m.x24 + m.x114*m.x30 + m.x120*m.x36 + 0.5*
                         m.x126*m.x42 + m.x132*m.x48 + m.x138*m.x54 + m.x144*m.x60 + 0.5*m.x150*m.x66 + m.x156*m.x72 + 
                         m.x162*m.x78 + 0.5*m.x168*m.x84 == 1)

m.c202 = Constraint(expr=m.x85*m.x1 <= 0.15)

m.c203 = Constraint(expr=m.x86*m.x2 <= 0.15)

m.c204 = Constraint(expr=m.x87*m.x3 <= 0.15)

m.c205 = Constraint(expr=m.x88*m.x4 <= 0.15)

m.c206 = Constraint(expr=m.x89*m.x5 <= 0.15)

m.c207 = Constraint(expr=m.x90*m.x6 <= 0.15)

m.c208 = Constraint(expr=m.x91*m.x7 <= 0.15)

m.c209 = Constraint(expr=m.x92*m.x8 <= 0.15)

m.c210 = Constraint(expr=m.x93*m.x9 <= 0.15)

m.c211 = Constraint(expr=m.x94*m.x10 <= 0.15)

m.c212 = Constraint(expr=m.x95*m.x11 <= 0.15)

m.c213 = Constraint(expr=m.x96*m.x12 <= 0.15)

m.c214 = Constraint(expr=m.x97*m.x13 <= 0.15)

m.c215 = Constraint(expr=m.x98*m.x14 <= 0.15)

m.c216 = Constraint(expr=m.x99*m.x15 <= 0.15)

m.c217 = Constraint(expr=m.x100*m.x16 <= 0.15)

m.c218 = Constraint(expr=m.x101*m.x17 <= 0.15)

m.c219 = Constraint(expr=m.x102*m.x18 <= 0.15)

m.c220 = Constraint(expr=m.x103*m.x19 <= 0.15)

m.c221 = Constraint(expr=m.x104*m.x20 <= 0.15)

m.c222 = Constraint(expr=m.x105*m.x21 <= 0.15)

m.c223 = Constraint(expr=m.x106*m.x22 <= 0.15)

m.c224 = Constraint(expr=m.x107*m.x23 <= 0.15)

m.c225 = Constraint(expr=m.x108*m.x24 <= 0.15)

m.c226 = Constraint(expr=m.x109*m.x25 <= 0.15)

m.c227 = Constraint(expr=m.x110*m.x26 <= 0.15)

m.c228 = Constraint(expr=m.x111*m.x27 <= 0.15)

m.c229 = Constraint(expr=m.x112*m.x28 <= 0.15)

m.c230 = Constraint(expr=m.x113*m.x29 <= 0.15)

m.c231 = Constraint(expr=m.x114*m.x30 <= 0.15)

m.c232 = Constraint(expr=m.x115*m.x31 <= 0.15)

m.c233 = Constraint(expr=m.x116*m.x32 <= 0.15)

m.c234 = Constraint(expr=m.x117*m.x33 <= 0.15)

m.c235 = Constraint(expr=m.x118*m.x34 <= 0.15)

m.c236 = Constraint(expr=m.x119*m.x35 <= 0.15)

m.c237 = Constraint(expr=m.x120*m.x36 <= 0.15)

m.c238 = Constraint(expr=m.x121*m.x37 <= 0.15)

m.c239 = Constraint(expr=m.x122*m.x38 <= 0.15)

m.c240 = Constraint(expr=m.x123*m.x39 <= 0.15)

m.c241 = Constraint(expr=m.x124*m.x40 <= 0.15)

m.c242 = Constraint(expr=m.x125*m.x41 <= 0.15)

m.c243 = Constraint(expr=m.x126*m.x42 <= 0.15)

m.c244 = Constraint(expr=m.x127*m.x43 <= 0.15)

m.c245 = Constraint(expr=m.x128*m.x44 <= 0.15)

m.c246 = Constraint(expr=m.x129*m.x45 <= 0.15)

m.c247 = Constraint(expr=m.x130*m.x46 <= 0.15)

m.c248 = Constraint(expr=m.x131*m.x47 <= 0.15)

m.c249 = Constraint(expr=m.x132*m.x48 <= 0.15)

m.c250 = Constraint(expr=m.x133*m.x49 <= 0.15)

m.c251 = Constraint(expr=m.x134*m.x50 <= 0.15)

m.c252 = Constraint(expr=m.x135*m.x51 <= 0.15)

m.c253 = Constraint(expr=m.x136*m.x52 <= 0.15)

m.c254 = Constraint(expr=m.x137*m.x53 <= 0.15)

m.c255 = Constraint(expr=m.x138*m.x54 <= 0.15)

m.c256 = Constraint(expr=m.x139*m.x55 <= 0.15)

m.c257 = Constraint(expr=m.x140*m.x56 <= 0.15)

m.c258 = Constraint(expr=m.x141*m.x57 <= 0.15)

m.c259 = Constraint(expr=m.x142*m.x58 <= 0.15)

m.c260 = Constraint(expr=m.x143*m.x59 <= 0.15)

m.c261 = Constraint(expr=m.x144*m.x60 <= 0.15)

m.c262 = Constraint(expr=m.x145*m.x61 <= 0.15)

m.c263 = Constraint(expr=m.x146*m.x62 <= 0.15)

m.c264 = Constraint(expr=m.x147*m.x63 <= 0.15)

m.c265 = Constraint(expr=m.x148*m.x64 <= 0.15)

m.c266 = Constraint(expr=m.x149*m.x65 <= 0.15)

m.c267 = Constraint(expr=m.x150*m.x66 <= 0.15)

m.c268 = Constraint(expr=m.x151*m.x67 <= 0.15)

m.c269 = Constraint(expr=m.x152*m.x68 <= 0.15)

m.c270 = Constraint(expr=m.x153*m.x69 <= 0.15)

m.c271 = Constraint(expr=m.x154*m.x70 <= 0.15)

m.c272 = Constraint(expr=m.x155*m.x71 <= 0.15)

m.c273 = Constraint(expr=m.x156*m.x72 <= 0.15)

m.c274 = Constraint(expr=m.x157*m.x73 <= 0.15)

m.c275 = Constraint(expr=m.x158*m.x74 <= 0.15)

m.c276 = Constraint(expr=m.x159*m.x75 <= 0.15)

m.c277 = Constraint(expr=m.x160*m.x76 <= 0.15)

m.c278 = Constraint(expr=m.x161*m.x77 <= 0.15)

m.c279 = Constraint(expr=m.x162*m.x78 <= 0.15)

m.c280 = Constraint(expr=m.x163*m.x79 <= 0.15)

m.c281 = Constraint(expr=m.x164*m.x80 <= 0.15)

m.c282 = Constraint(expr=m.x165*m.x81 <= 0.15)

m.c283 = Constraint(expr=m.x166*m.x82 <= 0.15)

m.c284 = Constraint(expr=m.x167*m.x83 <= 0.15)

m.c285 = Constraint(expr=m.x168*m.x84 <= 0.15)

m.c286 = Constraint(expr=-(0.5*m.b175*m.x90 + m.b187*m.x96 + m.b199*m.x102 + m.b211*m.x108 + m.b223*m.x114 + m.b235*
                         m.x120 + 0.5*m.b247*m.x126 + m.b259*m.x132 + m.b271*m.x138 + m.b283*m.x144 + 0.5*m.b295*m.x150
                          + m.b307*m.x156 + m.b319*m.x162 + 0.5*m.b331*m.x168) + m.x344 == 0)

m.c287 = Constraint(expr=-(0.5*m.b176*m.x90 + m.b188*m.x96 + m.b200*m.x102 + m.b212*m.x108 + m.b224*m.x114 + m.b236*
                         m.x120 + 0.5*m.b248*m.x126 + m.b260*m.x132 + m.b272*m.x138 + m.b284*m.x144 + 0.5*m.b296*m.x150
                          + m.b308*m.x156 + m.b320*m.x162 + 0.5*m.b332*m.x168) + m.x345 == 0)

m.c288 = Constraint(expr=-(0.5*m.b177*m.x90 + m.b189*m.x96 + m.b201*m.x102 + m.b213*m.x108 + m.b225*m.x114 + m.b237*
                         m.x120 + 0.5*m.b249*m.x126 + m.b261*m.x132 + m.b273*m.x138 + m.b285*m.x144 + 0.5*m.b297*m.x150
                          + m.b309*m.x156 + m.b321*m.x162 + 0.5*m.b333*m.x168) + m.x346 == 0)

m.c289 = Constraint(expr=-(0.5*m.b178*m.x90 + m.b190*m.x96 + m.b202*m.x102 + m.b214*m.x108 + m.b226*m.x114 + m.b238*
                         m.x120 + 0.5*m.b250*m.x126 + m.b262*m.x132 + m.b274*m.x138 + m.b286*m.x144 + 0.5*m.b298*m.x150
                          + m.b310*m.x156 + m.b322*m.x162 + 0.5*m.b334*m.x168) + m.x347 == 0)

m.c290 = Constraint(expr=-(0.5*m.b179*m.x90 + m.b191*m.x96 + m.b203*m.x102 + m.b215*m.x108 + m.b227*m.x114 + m.b239*
                         m.x120 + 0.5*m.b251*m.x126 + m.b263*m.x132 + m.b275*m.x138 + m.b287*m.x144 + 0.5*m.b299*m.x150
                          + m.b311*m.x156 + m.b323*m.x162 + 0.5*m.b335*m.x168) + m.x348 == 0)

m.c291 = Constraint(expr=-(0.5*m.b180*m.x90 + m.b192*m.x96 + m.b204*m.x102 + m.b216*m.x108 + m.b228*m.x114 + m.b240*
                         m.x120 + 0.5*m.b252*m.x126 + m.b264*m.x132 + m.b276*m.x138 + m.b288*m.x144 + 0.5*m.b300*m.x150
                          + m.b312*m.x156 + m.b324*m.x162 + 0.5*m.b336*m.x168) + m.x349 == 0)

m.c292 = Constraint(expr=-(0.5*m.b181*m.x90 + m.b193*m.x96 + m.b205*m.x102 + m.b217*m.x108 + m.b229*m.x114 + m.b241*
                         m.x120 + 0.5*m.b253*m.x126 + m.b265*m.x132 + m.b277*m.x138 + m.b289*m.x144 + 0.5*m.b301*m.x150
                          + m.b313*m.x156 + m.b325*m.x162 + 0.5*m.b337*m.x168) + m.x350 == 0)

m.c293 = Constraint(expr=-(0.5*m.b182*m.x90 + m.b194*m.x96 + m.b206*m.x102 + m.b218*m.x108 + m.b230*m.x114 + m.b242*
                         m.x120 + 0.5*m.b254*m.x126 + m.b266*m.x132 + m.b278*m.x138 + m.b290*m.x144 + 0.5*m.b302*m.x150
                          + m.b314*m.x156 + m.b326*m.x162 + 0.5*m.b338*m.x168) + m.x351 == 0)

m.c294 = Constraint(expr=-(0.5*m.b183*m.x90 + m.b195*m.x96 + m.b207*m.x102 + m.b219*m.x108 + m.b231*m.x114 + m.b243*
                         m.x120 + 0.5*m.b255*m.x126 + m.b267*m.x132 + m.b279*m.x138 + m.b291*m.x144 + 0.5*m.b303*m.x150
                          + m.b315*m.x156 + m.b327*m.x162 + 0.5*m.b339*m.x168) + m.x352 == 0)

m.c295 = Constraint(expr=   m.b175 - m.b247 == 0)

m.c296 = Constraint(expr=   m.b176 - m.b248 == 0)

m.c297 = Constraint(expr=   m.b177 - m.b249 == 0)

m.c298 = Constraint(expr=   m.b178 - m.b250 == 0)

m.c299 = Constraint(expr=   m.b179 - m.b251 == 0)

m.c300 = Constraint(expr=   m.b180 - m.b252 == 0)

m.c301 = Constraint(expr=   m.b181 - m.b253 == 0)

m.c302 = Constraint(expr=   m.b182 - m.b254 == 0)

m.c303 = Constraint(expr=   m.b183 - m.b255 == 0)

m.c304 = Constraint(expr=   m.b184 - m.b256 == 0)

m.c305 = Constraint(expr=   m.b185 - m.b257 == 0)

m.c306 = Constraint(expr=   m.b186 - m.b258 == 0)

m.c307 = Constraint(expr=   m.b295 - m.b331 == 0)

m.c308 = Constraint(expr=   m.b296 - m.b332 == 0)

m.c309 = Constraint(expr=   m.b297 - m.b333 == 0)

m.c310 = Constraint(expr=   m.b298 - m.b334 == 0)

m.c311 = Constraint(expr=   m.b299 - m.b335 == 0)

m.c312 = Constraint(expr=   m.b300 - m.b336 == 0)

m.c313 = Constraint(expr=   m.b301 - m.b337 == 0)

m.c314 = Constraint(expr=   m.b302 - m.b338 == 0)

m.c315 = Constraint(expr=   m.b303 - m.b339 == 0)

m.c316 = Constraint(expr=   m.b304 - m.b340 == 0)

m.c317 = Constraint(expr=   m.b305 - m.b341 == 0)

m.c318 = Constraint(expr=   m.b306 - m.b342 == 0)
