#  MINLP written by GAMS Convert at 04/21/18 13:55:16
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        810      417      225      168        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        665      605       60        0        0        0        0        0
#  FX      8        8        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       2185     1953      232        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


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
m.x62 = Var(within=Reals,bounds=(148.299332771269,638.10455381568),initialize=148.299332771269)
m.x63 = Var(within=Reals,bounds=(0,135.302691146811),initialize=0)
m.x64 = Var(within=Reals,bounds=(0.8,1.2),initialize=0.8)
m.x65 = Var(within=Reals,bounds=(148.299332771269,638.10455381568),initialize=148.299332771269)
m.x66 = Var(within=Reals,bounds=(0,135.302691146811),initialize=0)
m.x67 = Var(within=Reals,bounds=(0.8,1.2),initialize=0.8)
m.x68 = Var(within=Reals,bounds=(148.299332771269,638.10455381568),initialize=148.299332771269)
m.x69 = Var(within=Reals,bounds=(0,135.302691146811),initialize=0)
m.x70 = Var(within=Reals,bounds=(0.8,1.2),initialize=0.8)
m.x71 = Var(within=Reals,bounds=(148.299332771269,638.10455381568),initialize=148.299332771269)
m.x72 = Var(within=Reals,bounds=(0,135.302691146811),initialize=0)
m.x73 = Var(within=Reals,bounds=(0.8,1.2),initialize=0.8)
m.x74 = Var(within=Reals,bounds=(148.299332771269,638.10455381568),initialize=148.299332771269)
m.x75 = Var(within=Reals,bounds=(0,135.302691146811),initialize=0)
m.x76 = Var(within=Reals,bounds=(0.8,1.2),initialize=0.8)
m.x77 = Var(within=Reals,bounds=(148.299332771269,638.10455381568),initialize=148.299332771269)
m.x78 = Var(within=Reals,bounds=(0,135.302691146811),initialize=0)
m.x79 = Var(within=Reals,bounds=(0.8,1.2),initialize=0.8)
m.x80 = Var(within=Reals,bounds=(148.299332771269,638.10455381568),initialize=148.299332771269)
m.x81 = Var(within=Reals,bounds=(0,135.302691146811),initialize=0)
m.x82 = Var(within=Reals,bounds=(287.427397827187,413.764247971),initialize=287.427397827187)
m.x83 = Var(within=Reals,bounds=(0,126.336850143813),initialize=0)
m.x84 = Var(within=Reals,bounds=(287.427397827187,413.764247971),initialize=287.427397827187)
m.x85 = Var(within=Reals,bounds=(0,126.336850143813),initialize=0)
m.x86 = Var(within=Reals,bounds=(287.427397827187,413.764247971),initialize=287.427397827187)
m.x87 = Var(within=Reals,bounds=(0,126.336850143813),initialize=0)
m.x88 = Var(within=Reals,bounds=(287.427397827187,413.764247971),initialize=287.427397827187)
m.x89 = Var(within=Reals,bounds=(0,126.336850143813),initialize=0)
m.x90 = Var(within=Reals,bounds=(74.1748123438468,106.777870451),initialize=74.1748123438468)
m.x91 = Var(within=Reals,bounds=(0,32.6030581071532),initialize=0)
m.x92 = Var(within=Reals,bounds=(74.1748123438468,106.777870451),initialize=74.1748123438468)
m.x93 = Var(within=Reals,bounds=(0,32.6030581071532),initialize=0)
m.x94 = Var(within=Reals,bounds=(74.1748123438468,106.777870451),initialize=74.1748123438468)
m.x95 = Var(within=Reals,bounds=(0,32.6030581071532),initialize=0)
m.x96 = Var(within=Reals,bounds=(74.1748123438468,106.777870451),initialize=74.1748123438468)
m.x97 = Var(within=Reals,bounds=(0,32.6030581071532),initialize=0)
m.x98 = Var(within=Reals,bounds=(74.1748123438468,106.777870451),initialize=74.1748123438468)
m.x99 = Var(within=Reals,bounds=(0,32.6030581071532),initialize=0)
m.x100 = Var(within=Reals,bounds=(74.1748123438468,106.777870451),initialize=74.1748123438468)
m.x101 = Var(within=Reals,bounds=(0,32.6030581071532),initialize=0)
m.x102 = Var(within=Reals,bounds=(74.1748123438468,106.777870451),initialize=74.1748123438468)
m.x103 = Var(within=Reals,bounds=(0,32.6030581071532),initialize=0)
m.x104 = Var(within=Reals,bounds=(74.1748123438468,106.777870451),initialize=74.1748123438468)
m.x105 = Var(within=Reals,bounds=(0,32.6030581071532),initialize=0)
m.x106 = Var(within=Reals,bounds=(74.1748123438468,106.777870451),initialize=74.1748123438468)
m.x107 = Var(within=Reals,bounds=(0,32.6030581071532),initialize=0)
m.x108 = Var(within=Reals,bounds=(74.1748123438468,106.777870451),initialize=74.1748123438468)
m.x109 = Var(within=Reals,bounds=(0,32.6030581071532),initialize=0)
m.x110 = Var(within=Reals,bounds=(74.1748123438468,106.777870451),initialize=74.1748123438468)
m.x111 = Var(within=Reals,bounds=(0,32.6030581071532),initialize=0)
m.x112 = Var(within=Reals,bounds=(74.1748123438468,106.777870451),initialize=74.1748123438468)
m.x113 = Var(within=Reals,bounds=(0,32.6030581071532),initialize=0)
m.x114 = Var(within=Reals,bounds=(74.1748123434975,106.777870452),initialize=74.1748123434975)
m.x115 = Var(within=Reals,bounds=(0,32.6030581085025),initialize=0)
m.x116 = Var(within=Reals,bounds=(74.1748123434975,106.777870452),initialize=74.1748123434975)
m.x117 = Var(within=Reals,bounds=(0,32.6030581085025),initialize=0)
m.x118 = Var(within=Reals,bounds=(74.1748123434975,106.777870452),initialize=74.1748123434975)
m.x119 = Var(within=Reals,bounds=(0,32.6030581085025),initialize=0)
m.x120 = Var(within=Reals,bounds=(74.1748123434975,106.777870452),initialize=74.1748123434975)
m.x121 = Var(within=Reals,bounds=(0,32.6030581085025),initialize=0)
m.x122 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x123 = Var(within=Reals,bounds=(0,0.64163),initialize=0)
m.x124 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x125 = Var(within=Reals,bounds=(0,0.64163),initialize=0)
m.x126 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x127 = Var(within=Reals,bounds=(0,0.64163),initialize=0)
m.x128 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x129 = Var(within=Reals,bounds=(0,0.64163),initialize=0)
m.x130 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x131 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x132 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x133 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x134 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x135 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x136 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x137 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x138 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x139 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x140 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x141 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x142 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x143 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x144 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x145 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x146 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x147 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x148 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x149 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x150 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x151 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x152 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x153 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x154 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x155 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x156 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x157 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x158 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x159 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x160 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x161 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x162 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x163 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x164 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x165 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x166 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x167 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x168 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x169 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x170 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x171 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x172 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x173 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x174 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x175 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x176 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x177 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x178 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x179 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x180 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x181 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x182 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x183 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x184 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x185 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x186 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x187 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x188 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x189 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x190 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x191 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x192 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x193 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x194 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x195 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x196 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x197 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x198 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x199 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x200 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x201 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x202 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x203 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x204 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x205 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x206 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x207 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x208 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x209 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x210 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x211 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x212 = Var(within=Reals,bounds=(0,0.429286),initialize=0)
m.x213 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x214 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x215 = Var(within=Reals,bounds=(0,0.429286),initialize=0)
m.x216 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x217 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x218 = Var(within=Reals,bounds=(0,0.429286),initialize=0)
m.x219 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x220 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x221 = Var(within=Reals,bounds=(0,0.429286),initialize=0)
m.x222 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x223 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x224 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x225 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x226 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x227 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x228 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x229 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x230 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x231 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x232 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x233 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x234 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x235 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x236 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x237 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x238 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x239 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x240 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x241 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x242 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x243 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x244 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x245 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x246 = Var(within=Reals,bounds=(6.3,6.3),initialize=6.3)
m.x247 = Var(within=Reals,bounds=(5,10),initialize=5)
m.x248 = Var(within=Reals,bounds=(5,10),initialize=5)
m.x249 = Var(within=Reals,bounds=(5,10),initialize=5)
m.x250 = Var(within=Reals,bounds=(5,10),initialize=5)
m.x251 = Var(within=Reals,bounds=(5,10),initialize=5)
m.x252 = Var(within=Reals,bounds=(5,10),initialize=5)
m.x253 = Var(within=Reals,bounds=(5,10),initialize=5)
m.x254 = Var(within=Reals,bounds=(4.6,4.6),initialize=4.6)
m.x255 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x256 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x257 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x258 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x259 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x260 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x261 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x262 = Var(within=Reals,bounds=(4.6,4.6),initialize=4.6)
m.x263 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x264 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x265 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x266 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x267 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x268 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x269 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x270 = Var(within=Reals,bounds=(10,10),initialize=10)
m.x271 = Var(within=Reals,bounds=(0,16.5),initialize=0)
m.x272 = Var(within=Reals,bounds=(0,16.5),initialize=0)
m.x273 = Var(within=Reals,bounds=(0,16.5),initialize=0)
m.x274 = Var(within=Reals,bounds=(0,16.5),initialize=0)
m.x275 = Var(within=Reals,bounds=(0,16.5),initialize=0)
m.x276 = Var(within=Reals,bounds=(0,16.5),initialize=0)
m.x277 = Var(within=Reals,bounds=(0,16.5),initialize=0)
m.x278 = Var(within=Reals,bounds=(0,0.045826),initialize=0)
m.x279 = Var(within=Reals,bounds=(287.427397827187,413.764247971),initialize=287.427397827187)
m.x280 = Var(within=Reals,bounds=(0,0.045826),initialize=0)
m.x281 = Var(within=Reals,bounds=(0,126.336850143813),initialize=0)
m.x282 = Var(within=Reals,bounds=(0,0.045826),initialize=0)
m.x283 = Var(within=Reals,bounds=(287.427397827187,413.764247971),initialize=287.427397827187)
m.x284 = Var(within=Reals,bounds=(0,0.045826),initialize=0)
m.x285 = Var(within=Reals,bounds=(0,126.336850143813),initialize=0)
m.x286 = Var(within=Reals,bounds=(0,0.091663),initialize=0)
m.x287 = Var(within=Reals,bounds=(287.427397827187,413.764247971),initialize=287.427397827187)
m.x288 = Var(within=Reals,bounds=(0,0.091663),initialize=0)
m.x289 = Var(within=Reals,bounds=(0,126.336850143813),initialize=0)
m.x290 = Var(within=Reals,bounds=(0,0.091663),initialize=0)
m.x291 = Var(within=Reals,bounds=(287.427397827187,413.764247971),initialize=287.427397827187)
m.x292 = Var(within=Reals,bounds=(0,0.091663),initialize=0)
m.x293 = Var(within=Reals,bounds=(0,126.336850143813),initialize=0)
m.x294 = Var(within=Reals,bounds=(0,0.091663),initialize=0)
m.x295 = Var(within=Reals,bounds=(0.8,1.2),initialize=0.8)
m.x296 = Var(within=Reals,bounds=(0,0.091663),initialize=0)
m.x297 = Var(within=Reals,bounds=(148.299332771269,638.10455381568),initialize=148.299332771269)
m.x298 = Var(within=Reals,bounds=(0,0.091663),initialize=0)
m.x299 = Var(within=Reals,bounds=(0,135.302691146811),initialize=0)
m.x300 = Var(within=Reals,bounds=(0,0.091663),initialize=0)
m.x301 = Var(within=Reals,bounds=(0.8,1.2),initialize=0.8)
m.x302 = Var(within=Reals,bounds=(0,0.091663),initialize=0)
m.x303 = Var(within=Reals,bounds=(148.299332771269,638.10455381568),initialize=148.299332771269)
m.x304 = Var(within=Reals,bounds=(0,0.091663),initialize=0)
m.x305 = Var(within=Reals,bounds=(0,135.302691146811),initialize=0)
m.x306 = Var(within=Reals,bounds=(0,0.091663),initialize=0)
m.x307 = Var(within=Reals,bounds=(0.8,1.2),initialize=0.8)
m.x308 = Var(within=Reals,bounds=(0,0.091663),initialize=0)
m.x309 = Var(within=Reals,bounds=(148.299332771269,638.10455381568),initialize=148.299332771269)
m.x310 = Var(within=Reals,bounds=(0,0.091663),initialize=0)
m.x311 = Var(within=Reals,bounds=(0,135.302691146811),initialize=0)
m.x312 = Var(within=Reals,bounds=(0,0.091663),initialize=0)
m.x313 = Var(within=Reals,bounds=(0.8,1.2),initialize=0.8)
m.x314 = Var(within=Reals,bounds=(0,0.091663),initialize=0)
m.x315 = Var(within=Reals,bounds=(148.299332771269,638.10455381568),initialize=148.299332771269)
m.x316 = Var(within=Reals,bounds=(0,0.091663),initialize=0)
m.x317 = Var(within=Reals,bounds=(0,135.302691146811),initialize=0)
m.x318 = Var(within=Reals,bounds=(0,0.091663),initialize=0)
m.x319 = Var(within=Reals,bounds=(0.8,1.2),initialize=0.8)
m.x320 = Var(within=Reals,bounds=(0,0.091663),initialize=0)
m.x321 = Var(within=Reals,bounds=(148.299332771269,638.10455381568),initialize=148.299332771269)
m.x322 = Var(within=Reals,bounds=(0,0.091663),initialize=0)
m.x323 = Var(within=Reals,bounds=(0,135.302691146811),initialize=0)
m.x324 = Var(within=Reals,bounds=(0,0.091663),initialize=0)
m.x325 = Var(within=Reals,bounds=(0.8,1.2),initialize=0.8)
m.x326 = Var(within=Reals,bounds=(0,0.091663),initialize=0)
m.x327 = Var(within=Reals,bounds=(148.299332771269,638.10455381568),initialize=148.299332771269)
m.x328 = Var(within=Reals,bounds=(0,0.091663),initialize=0)
m.x329 = Var(within=Reals,bounds=(0,135.302691146811),initialize=0)
m.x330 = Var(within=Reals,bounds=(0,0.091663),initialize=0)
m.x331 = Var(within=Reals,bounds=(0.8,1.2),initialize=0.8)
m.x332 = Var(within=Reals,bounds=(0,0.091663),initialize=0)
m.x333 = Var(within=Reals,bounds=(148.299332771269,638.10455381568),initialize=148.299332771269)
m.x334 = Var(within=Reals,bounds=(0,0.045826),initialize=0)
m.x335 = Var(within=Reals,bounds=(0,135.302691146811),initialize=0)
m.x336 = Var(within=Reals,bounds=(0,0.045826),initialize=0)
m.x337 = Var(within=Reals,bounds=(0.8,1.2),initialize=0.8)
m.x338 = Var(within=Reals,bounds=(0,0.045826),initialize=0)
m.x339 = Var(within=Reals,bounds=(148.299332771269,638.10455381568),initialize=148.299332771269)
m.x340 = Var(within=Reals,bounds=(0,0.045826),initialize=0)
m.x341 = Var(within=Reals,bounds=(0,135.302691146811),initialize=0)
m.x342 = Var(within=Reals,bounds=(0,0.119163),initialize=0)
m.x343 = Var(within=Reals,bounds=(0.8,1.2),initialize=0.8)
m.x344 = Var(within=Reals,bounds=(0,0.119163),initialize=0)
m.x345 = Var(within=Reals,bounds=(148.299332771269,638.10455381568),initialize=148.299332771269)
m.x346 = Var(within=Reals,bounds=(0,0.119163),initialize=0)
m.x347 = Var(within=Reals,bounds=(0,135.302691146811),initialize=0)
m.x348 = Var(within=Reals,bounds=(0,0.119163),initialize=0)
m.x349 = Var(within=Reals,bounds=(0.8,1.2),initialize=0.8)
m.x350 = Var(within=Reals,bounds=(0,0.119163),initialize=0)
m.x351 = Var(within=Reals,bounds=(148.299332771269,638.10455381568),initialize=148.299332771269)
m.x352 = Var(within=Reals,bounds=(0,0.119163),initialize=0)
m.x353 = Var(within=Reals,bounds=(0,135.302691146811),initialize=0)
m.x354 = Var(within=Reals,bounds=(0,0.119163),initialize=0)
m.x355 = Var(within=Reals,bounds=(0.8,1.2),initialize=0.8)
m.x356 = Var(within=Reals,bounds=(0,0.119163),initialize=0)
m.x357 = Var(within=Reals,bounds=(148.299332771269,638.10455381568),initialize=148.299332771269)
m.x358 = Var(within=Reals,bounds=(0,0.119163),initialize=0)
m.x359 = Var(within=Reals,bounds=(0,135.302691146811),initialize=0)
m.x360 = Var(within=Reals,bounds=(0,0.119163),initialize=0)
m.x361 = Var(within=Reals,bounds=(0.8,1.2),initialize=0.8)
m.x362 = Var(within=Reals,bounds=(0,0.119163),initialize=0)
m.x363 = Var(within=Reals,bounds=(148.299332771269,638.10455381568),initialize=148.299332771269)
m.x364 = Var(within=Reals,bounds=(0,0.119163),initialize=0)
m.x365 = Var(within=Reals,bounds=(0,135.302691146811),initialize=0)
m.x366 = Var(within=Reals,bounds=(0,0.071797),initialize=0)
m.x367 = Var(within=Reals,bounds=(0.8,1.2),initialize=0.8)
m.x368 = Var(within=Reals,bounds=(0,0.071797),initialize=0)
m.x369 = Var(within=Reals,bounds=(148.299332771269,638.10455381568),initialize=148.299332771269)
m.x370 = Var(within=Reals,bounds=(0,0.071797),initialize=0)
m.x371 = Var(within=Reals,bounds=(0,135.302691146811),initialize=0)
m.x372 = Var(within=Reals,bounds=(0,0.071797),initialize=0)
m.x373 = Var(within=Reals,bounds=(0.8,1.2),initialize=0.8)
m.x374 = Var(within=Reals,bounds=(305,310),initialize=305)
m.x375 = Var(within=Reals,bounds=(305,310),initialize=305)
m.x376 = Var(within=Reals,bounds=(305,310),initialize=305)
m.x377 = Var(within=Reals,bounds=(305,310),initialize=305)
m.x378 = Var(within=Reals,bounds=(240,246),initialize=240)
m.x379 = Var(within=Reals,bounds=(240,246),initialize=240)
m.x380 = Var(within=Reals,bounds=(240,246),initialize=240)
m.x381 = Var(within=Reals,bounds=(240,246),initialize=240)
m.x382 = Var(within=Reals,bounds=(240,246),initialize=240)
m.x383 = Var(within=Reals,bounds=(240,246),initialize=240)
m.x384 = Var(within=Reals,bounds=(240,246),initialize=240)
m.x385 = Var(within=Reals,bounds=(240,246),initialize=240)
m.x386 = Var(within=Reals,bounds=(243,259.5),initialize=243)
m.x387 = Var(within=Reals,bounds=(243,259.5),initialize=243)
m.x388 = Var(within=Reals,bounds=(243,259.5),initialize=243)
m.x389 = Var(within=Reals,bounds=(243,259.5),initialize=243)
m.x390 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x391 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x392 = Var(within=Reals,bounds=(-232.35111544525,232.35111544525),initialize=0)
m.x393 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x394 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x395 = Var(within=Reals,bounds=(-232.35111544525,232.35111544525),initialize=0)
m.x396 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x397 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x398 = Var(within=Reals,bounds=(-232.35111544525,232.35111544525),initialize=0)
m.x399 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x400 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x401 = Var(within=Reals,bounds=(-232.35111544525,232.35111544525),initialize=0)
m.x402 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x403 = Var(within=Reals,bounds=(-103800.7251715,103800.7251715),initialize=0)
m.x404 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x405 = Var(within=Reals,bounds=(-103800.7251715,103800.7251715),initialize=0)
m.x406 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x407 = Var(within=Reals,bounds=(-103800.7251715,103800.7251715),initialize=0)
m.x408 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x409 = Var(within=Reals,bounds=(-103800.7251715,103800.7251715),initialize=0)
m.x410 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x411 = Var(within=Reals,bounds=(-22646.161845275,22646.161845275),initialize=0)
m.x412 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x413 = Var(within=Reals,bounds=(-22646.161845275,22646.161845275),initialize=0)
m.x414 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x415 = Var(within=Reals,bounds=(-22646.161845275,22646.161845275),initialize=0)
m.x416 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x417 = Var(within=Reals,bounds=(-22646.161845275,22646.161845275),initialize=0)
m.x418 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x419 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x420 = Var(within=Reals,bounds=(-1693.1005454625,1693.1005454625),initialize=0)
m.x421 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x422 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x423 = Var(within=Reals,bounds=(-1693.1005454625,1693.1005454625),initialize=0)
m.x424 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x425 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x426 = Var(within=Reals,bounds=(-1693.1005454625,1693.1005454625),initialize=0)
m.x427 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x428 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x429 = Var(within=Reals,bounds=(-1693.1005454625,1693.1005454625),initialize=0)
m.x430 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x431 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x432 = Var(within=Reals,bounds=(-1975.896081255,1975.896081255),initialize=0)
m.x433 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x434 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x435 = Var(within=Reals,bounds=(-1975.896081255,1975.896081255),initialize=0)
m.x436 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x437 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x438 = Var(within=Reals,bounds=(-1975.896081255,1975.896081255),initialize=0)
m.x439 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x440 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x441 = Var(within=Reals,bounds=(-1975.896081255,1975.896081255),initialize=0)
m.x442 = Var(within=Reals,bounds=(-35055.017651,35055.017651),initialize=0)
m.x443 = Var(within=Reals,bounds=(-35055.017651,35055.017651),initialize=0)
m.x444 = Var(within=Reals,bounds=(-35055.017651,35055.017651),initialize=0)
m.x445 = Var(within=Reals,bounds=(-35055.017651,35055.017651),initialize=0)
m.x446 = Var(within=Reals,bounds=(-987.9480406275,987.9480406275),initialize=0)
m.x447 = Var(within=Reals,bounds=(-987.9480406275,987.9480406275),initialize=0)
m.x448 = Var(within=Reals,bounds=(-987.9480406275,987.9480406275),initialize=0)
m.x449 = Var(within=Reals,bounds=(-987.9480406275,987.9480406275),initialize=0)
m.x450 = Var(within=Reals,bounds=(-1270.74357642,1270.74357642),initialize=0)
m.x451 = Var(within=Reals,bounds=(-1270.74357642,1270.74357642),initialize=0)
m.x452 = Var(within=Reals,bounds=(-1270.74357642,1270.74357642),initialize=0)
m.x453 = Var(within=Reals,bounds=(-1270.74357642,1270.74357642),initialize=0)
m.x454 = Var(within=Reals,bounds=(-186.06385100525,186.06385100525),initialize=0)
m.x455 = Var(within=Reals,bounds=(-186.06385100525,186.06385100525),initialize=0)
m.x456 = Var(within=Reals,bounds=(-186.06385100525,186.06385100525),initialize=0)
m.x457 = Var(within=Reals,bounds=(-186.06385100525,186.06385100525),initialize=0)
m.x458 = Var(within=Reals,bounds=(-186.06385100525,186.06385100525),initialize=0)
m.x459 = Var(within=Reals,bounds=(-186.06385100525,186.06385100525),initialize=0)
m.x460 = Var(within=Reals,bounds=(-186.06385100525,186.06385100525),initialize=0)
m.x461 = Var(within=Reals,bounds=(-186.06385100525,186.06385100525),initialize=0)
m.x462 = Var(within=Reals,bounds=(214.9,1000),initialize=214.9)
m.x463 = Var(within=Reals,bounds=(-9303.19255025,9303.19255025),initialize=0)
m.x464 = Var(within=Reals,bounds=(214.9,1000),initialize=214.9)
m.x465 = Var(within=Reals,bounds=(-9303.19255025,9303.19255025),initialize=0)
m.x466 = Var(within=Reals,bounds=(214.9,1000),initialize=214.9)
m.x467 = Var(within=Reals,bounds=(-9303.19255025,9303.19255025),initialize=0)
m.x468 = Var(within=Reals,bounds=(214.9,1000),initialize=214.9)
m.x469 = Var(within=Reals,bounds=(-9303.19255025,9303.19255025),initialize=0)
m.x470 = Var(within=Reals,bounds=(231.04,1000),initialize=231.04)
m.x471 = Var(within=Reals,bounds=(-14219.27742075,14219.27742075),initialize=0)
m.x472 = Var(within=Reals,bounds=(231.04,1000),initialize=231.04)
m.x473 = Var(within=Reals,bounds=(-14219.27742075,14219.27742075),initialize=0)
m.x474 = Var(within=Reals,bounds=(231.04,1000),initialize=231.04)
m.x475 = Var(within=Reals,bounds=(-14219.27742075,14219.27742075),initialize=0)
m.x476 = Var(within=Reals,bounds=(231.04,1000),initialize=231.04)
m.x477 = Var(within=Reals,bounds=(-14219.27742075,14219.27742075),initialize=0)
m.x478 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x479 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x480 = Var(within=Reals,bounds=(-1596.630932455,1596.630932455),initialize=0)
m.x481 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x482 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x483 = Var(within=Reals,bounds=(-1596.630932455,1596.630932455),initialize=0)
m.x484 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x485 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x486 = Var(within=Reals,bounds=(-1596.630932455,1596.630932455),initialize=0)
m.x487 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x488 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x489 = Var(within=Reals,bounds=(-1596.630932455,1596.630932455),initialize=0)
m.x490 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x491 = Var(within=Reals,bounds=(300,1000),initialize=300)
m.x492 = Var(within=Reals,bounds=(-62.00958485375,62.00958485375),initialize=0)
m.x493 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x494 = Var(within=Reals,bounds=(300,1000),initialize=300)
m.x495 = Var(within=Reals,bounds=(-62.00958485375,62.00958485375),initialize=0)
m.x496 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x497 = Var(within=Reals,bounds=(300,1000),initialize=300)
m.x498 = Var(within=Reals,bounds=(-62.00958485375,62.00958485375),initialize=0)
m.x499 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x500 = Var(within=Reals,bounds=(300,1000),initialize=300)
m.x501 = Var(within=Reals,bounds=(-62.00958485375,62.00958485375),initialize=0)
m.x502 = Var(within=Reals,bounds=(-62.00958485375,62.00958485375),initialize=0)
m.x503 = Var(within=Reals,bounds=(-62.00958485375,62.00958485375),initialize=0)
m.x504 = Var(within=Reals,bounds=(-62.00958485375,62.00958485375),initialize=0)
m.x505 = Var(within=Reals,bounds=(-62.00958485375,62.00958485375),initialize=0)
m.x506 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x507 = Var(within=Reals,bounds=(-3.100479242675,3.100479242675),initialize=0)
m.x508 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x509 = Var(within=Reals,bounds=(-3.100479242675,3.100479242675),initialize=0)
m.x510 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x511 = Var(within=Reals,bounds=(-3.100479242675,3.100479242675),initialize=0)
m.x512 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x513 = Var(within=Reals,bounds=(-3.100479242675,3.100479242675),initialize=0)
m.x514 = Var(within=Reals,bounds=(-3.100479242675,3.100479242675),initialize=0)
m.x515 = Var(within=Reals,bounds=(-3.100479242675,3.100479242675),initialize=0)
m.x516 = Var(within=Reals,bounds=(-3.100479242675,3.100479242675),initialize=0)
m.x517 = Var(within=Reals,bounds=(-3.100479242675,3.100479242675),initialize=0)
m.x518 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x519 = Var(within=Reals,bounds=(243,1000),initialize=243)
m.x520 = Var(within=Reals,bounds=(-138489.1922805,138489.1922805),initialize=0)
m.x521 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x522 = Var(within=Reals,bounds=(243,1000),initialize=243)
m.x523 = Var(within=Reals,bounds=(-138489.1922805,138489.1922805),initialize=0)
m.x524 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x525 = Var(within=Reals,bounds=(243,1000),initialize=243)
m.x526 = Var(within=Reals,bounds=(-138489.1922805,138489.1922805),initialize=0)
m.x527 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x528 = Var(within=Reals,bounds=(243,1000),initialize=243)
m.x529 = Var(within=Reals,bounds=(-138489.1922805,138489.1922805),initialize=0)
m.x530 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x531 = Var(within=Reals,bounds=(-138489.1922805,138489.1922805),initialize=0)
m.x532 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x533 = Var(within=Reals,bounds=(-138489.1922805,138489.1922805),initialize=0)
m.x534 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x535 = Var(within=Reals,bounds=(-138489.1922805,138489.1922805),initialize=0)
m.x536 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x537 = Var(within=Reals,bounds=(-138489.1922805,138489.1922805),initialize=0)
m.x538 = Var(within=Reals,bounds=(-1846.52256374,1846.52256374),initialize=0)
m.x539 = Var(within=Reals,bounds=(-1846.52256374,1846.52256374),initialize=0)
m.x540 = Var(within=Reals,bounds=(-1846.52256374,1846.52256374),initialize=0)
m.x541 = Var(within=Reals,bounds=(-1846.52256374,1846.52256374),initialize=0)
m.x542 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x543 = Var(within=Reals,bounds=(-538.866468715,538.866468715),initialize=0)
m.x544 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x545 = Var(within=Reals,bounds=(-538.866468715,538.866468715),initialize=0)
m.x546 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x547 = Var(within=Reals,bounds=(-538.866468715,538.866468715),initialize=0)
m.x548 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x549 = Var(within=Reals,bounds=(-538.866468715,538.866468715),initialize=0)
m.x550 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x551 = Var(within=Reals,bounds=(-259.21503776,259.21503776),initialize=0)
m.x552 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x553 = Var(within=Reals,bounds=(-259.21503776,259.21503776),initialize=0)
m.x554 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x555 = Var(within=Reals,bounds=(-259.21503776,259.21503776),initialize=0)
m.x556 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x557 = Var(within=Reals,bounds=(-259.21503776,259.21503776),initialize=0)
m.x558 = Var(within=Reals,bounds=(34.1,34.1),initialize=34.1)
m.x559 = Var(within=Reals,bounds=(-34.1,1000),initialize=0)
m.x560 = Var(within=Reals,bounds=(34.1,34.1),initialize=34.1)
m.x561 = Var(within=Reals,bounds=(-34.1,1000),initialize=0)
m.x562 = Var(within=Reals,bounds=(34.1,34.1),initialize=34.1)
m.x563 = Var(within=Reals,bounds=(-34.1,1000),initialize=0)
m.x564 = Var(within=Reals,bounds=(34.1,34.1),initialize=34.1)
m.x565 = Var(within=Reals,bounds=(-34.1,1000),initialize=0)
m.x566 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x567 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x568 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x569 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x570 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x571 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x572 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x573 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x574 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x575 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x576 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x577 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x578 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x579 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x580 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x581 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x582 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x583 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x584 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x585 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x586 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x587 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x588 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x589 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x590 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x591 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x592 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x593 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x594 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x595 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x596 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x597 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x598 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x599 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x600 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x601 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x602 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x603 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x604 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x605 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x606 = Var(within=Reals,bounds=(148.299332771269,638.10455381568),initialize=148.299332771269)
m.x607 = Var(within=Reals,bounds=(0,135.302691146811),initialize=0)
m.x608 = Var(within=Reals,bounds=(0.8,1.2),initialize=0.8)
m.x609 = Var(within=Reals,bounds=(148.299332771269,638.10455381568),initialize=148.299332771269)
m.x610 = Var(within=Reals,bounds=(0,135.302691146811),initialize=0)
m.x611 = Var(within=Reals,bounds=(0.8,1.2),initialize=0.8)
m.x612 = Var(within=Reals,bounds=(148.299332771269,638.10455381568),initialize=148.299332771269)
m.x613 = Var(within=Reals,bounds=(0,135.302691146811),initialize=0)
m.x614 = Var(within=Reals,bounds=(0.8,1.2),initialize=0.8)
m.x615 = Var(within=Reals,bounds=(148.299332771269,638.10455381568),initialize=148.299332771269)
m.x616 = Var(within=Reals,bounds=(0,135.302691146811),initialize=0)
m.x617 = Var(within=Reals,bounds=(0.8,1.2),initialize=0.8)
m.x618 = Var(within=Reals,bounds=(0,46.5022459484905),initialize=0)
m.x619 = Var(within=Reals,bounds=(0,46.5022459484905),initialize=0)
m.x620 = Var(within=Reals,bounds=(0,46.5022459484905),initialize=0)
m.x621 = Var(within=Reals,bounds=(0,46.5022459484905),initialize=0)
m.x622 = Var(within=Reals,bounds=(0,143.448141849487),initialize=0)
m.x623 = Var(within=Reals,bounds=(0,143.448141849487),initialize=0)
m.x624 = Var(within=Reals,bounds=(0,143.448141849487),initialize=0)
m.x625 = Var(within=Reals,bounds=(0,143.448141849487),initialize=0)
m.x626 = Var(within=Reals,bounds=(0,143.448141849487),initialize=0)
m.x627 = Var(within=Reals,bounds=(0,143.448141849487),initialize=0)
m.x628 = Var(within=Reals,bounds=(0,143.448141849487),initialize=0)
m.x629 = Var(within=Reals,bounds=(0,143.448141849487),initialize=0)
m.x630 = Var(within=Reals,bounds=(0,143.448141849487),initialize=0)
m.x631 = Var(within=Reals,bounds=(0,143.448141849487),initialize=0)
m.x632 = Var(within=Reals,bounds=(0,143.448141849487),initialize=0)
m.x633 = Var(within=Reals,bounds=(0,143.448141849487),initialize=0)
m.x634 = Var(within=Reals,bounds=(0,143.448141849487),initialize=0)
m.x635 = Var(within=Reals,bounds=(0,143.448141849487),initialize=0)
m.x636 = Var(within=Reals,bounds=(0,143.448141849487),initialize=0)
m.x637 = Var(within=Reals,bounds=(0,143.448141849487),initialize=0)
m.x638 = Var(within=Reals,bounds=(0,143.448141849487),initialize=0)
m.x639 = Var(within=Reals,bounds=(0,143.448141849487),initialize=0)
m.x640 = Var(within=Reals,bounds=(0,143.448141849487),initialize=0)
m.x641 = Var(within=Reals,bounds=(0,143.448141849487),initialize=0)
m.x642 = Var(within=Reals,bounds=(0,143.448141849487),initialize=0)
m.x643 = Var(within=Reals,bounds=(0,143.448141849487),initialize=0)
m.x644 = Var(within=Reals,bounds=(0,143.448141849487),initialize=0)
m.x645 = Var(within=Reals,bounds=(0,143.448141849487),initialize=0)
m.x646 = Var(within=Reals,bounds=(0,46.5022459484905),initialize=0)
m.x647 = Var(within=Reals,bounds=(0,46.5022459484905),initialize=0)
m.x648 = Var(within=Reals,bounds=(0,46.5022459484905),initialize=0)
m.x649 = Var(within=Reals,bounds=(0,46.5022459484905),initialize=0)
m.x650 = Var(within=Reals,bounds=(0,31.205539800995),initialize=0)
m.x651 = Var(within=Reals,bounds=(0,31.205539800995),initialize=0)
m.x652 = Var(within=Reals,bounds=(0,31.205539800995),initialize=0)
m.x653 = Var(within=Reals,bounds=(0,31.205539800995),initialize=0)
m.x654 = Var(within=Reals,bounds=(0,31.205539800995),initialize=0)
m.x655 = Var(within=Reals,bounds=(0,31.205539800995),initialize=0)
m.x656 = Var(within=Reals,bounds=(0,31.205539800995),initialize=0)
m.x657 = Var(within=Reals,bounds=(0,31.205539800995),initialize=0)
m.x658 = Var(within=Reals,bounds=(0,31.205539800995),initialize=0)
m.x659 = Var(within=Reals,bounds=(0,31.205539800995),initialize=0)
m.x660 = Var(within=Reals,bounds=(0,31.205539800995),initialize=0)
m.x661 = Var(within=Reals,bounds=(0,31.205539800995),initialize=0)
m.x662 = Var(within=Reals,bounds=(0,18.8016762007756),initialize=0)
m.x663 = Var(within=Reals,bounds=(0,18.8016762007756),initialize=0)
m.x664 = Var(within=Reals,bounds=(0,18.8016762007756),initialize=0)
m.x665 = Var(within=Reals,bounds=(0,18.8016762007756),initialize=0)

m.obj = Objective(expr=   20*m.x570 + 20*m.x571 + 20*m.x572 + 20*m.x573 + 20*m.x574 + 20*m.x575 + 20*m.x576 + 20*m.x577
                        + 20*m.x578 + 20*m.x579 + 20*m.x580 + 20*m.x581 + 20*m.x582 + 20*m.x583 + 20*m.x584 + 20*m.x585
                        + 20*m.x586 + 20*m.x587 + 20*m.x588 + 20*m.x589 + 20*m.x590 + 20*m.x591 + 20*m.x592 + 20*m.x593
                        + 20*m.x594 + 20*m.x595 + 20*m.x596 + 20*m.x597 + 20*m.x598 + 20*m.x599 + 20*m.x600 + 20*m.x601
                        + 20*m.x602 + 20*m.x603 + 20*m.x604 + 20*m.x605 + m.x618 + m.x619 + m.x620 + m.x621 + m.x622
                        + m.x623 + m.x624 + m.x625 + m.x626 + m.x627 + m.x628 + m.x629 + m.x630 + m.x631 + m.x632
                        + m.x633 + m.x634 + m.x635 + m.x636 + m.x637 + m.x638 + m.x639 + m.x640 + m.x641 + m.x642
                        + m.x643 + m.x644 + m.x645 + m.x646 + m.x647 + m.x648 + m.x649 + m.x650 + m.x651 + m.x652
                        + m.x653 + m.x654 + m.x655 + m.x656 + m.x657 + m.x658 + m.x659 + m.x660 + m.x661 + m.x662
                        + m.x663 + m.x664 + m.x665, sense=minimize)

m.c2 = Constraint(expr=   m.x279 + m.x281 == 413.764247971)

m.c3 = Constraint(expr=   m.x283 + m.x285 == 413.764247971)

m.c4 = Constraint(expr=   m.x287 + m.x289 == 413.764247971)

m.c5 = Constraint(expr=   m.x291 + m.x293 == 413.764247971)

m.c6 = Constraint(expr= - 443.128162372*m.x295 + m.x297 + m.x299 == 0)

m.c7 = Constraint(expr= - 443.128162372*m.x301 + m.x303 + m.x305 == 0)

m.c8 = Constraint(expr= - 443.128162372*m.x307 + m.x309 + m.x311 == 0)

m.c9 = Constraint(expr= - 443.128162372*m.x313 + m.x315 + m.x317 == 0)

m.c10 = Constraint(expr= - 443.128162372*m.x319 + m.x321 + m.x323 == 0)

m.c11 = Constraint(expr= - 443.128162372*m.x325 + m.x327 + m.x329 == 0)

m.c12 = Constraint(expr= - 443.128162372*m.x331 + m.x333 + m.x335 == 0)

m.c13 = Constraint(expr= - 443.128162372*m.x337 + m.x339 + m.x341 == 0)

m.c14 = Constraint(expr= - 443.128162372*m.x343 + m.x345 + m.x347 == 0)

m.c15 = Constraint(expr= - 443.128162372*m.x349 + m.x351 + m.x353 == 0)

m.c16 = Constraint(expr= - 443.128162372*m.x355 + m.x357 + m.x359 == 0)

m.c17 = Constraint(expr= - 443.128162372*m.x361 + m.x363 + m.x365 == 0)

m.c18 = Constraint(expr= - 443.128162372*m.x367 + m.x369 + m.x371 == 0)

m.c19 = Constraint(expr= - 443.128162372*m.x373 + m.x606 + m.x607 == 0)

m.c20 = Constraint(expr= - 443.128162372*m.x608 + m.x609 + m.x610 == 0)

m.c21 = Constraint(expr= - 443.128162372*m.x611 + m.x612 + m.x613 == 0)

m.c22 = Constraint(expr= - 443.128162372*m.x614 + m.x615 + m.x616 == 0)

m.c23 = Constraint(expr=   m.x62 + m.x63 - 443.128162372*m.x617 == 0)

m.c24 = Constraint(expr= - 443.128162372*m.x64 + m.x65 + m.x66 == 0)

m.c25 = Constraint(expr= - 443.128162372*m.x67 + m.x68 + m.x69 == 0)

m.c26 = Constraint(expr= - 443.128162372*m.x70 + m.x71 + m.x72 == 0)

m.c27 = Constraint(expr= - 443.128162372*m.x73 + m.x74 + m.x75 == 0)

m.c28 = Constraint(expr= - 443.128162372*m.x76 + m.x77 + m.x78 == 0)

m.c29 = Constraint(expr= - 443.128162372*m.x79 + m.x80 + m.x81 == 0)

m.c30 = Constraint(expr=   m.x82 + m.x83 == 413.764247971)

m.c31 = Constraint(expr=   m.x84 + m.x85 == 413.764247971)

m.c32 = Constraint(expr=   m.x86 + m.x87 == 413.764247971)

m.c33 = Constraint(expr=   m.x88 + m.x89 == 413.764247971)

m.c34 = Constraint(expr=   m.x90 + m.x91 == 106.777870451)

m.c35 = Constraint(expr=   m.x92 + m.x93 == 106.777870451)

m.c36 = Constraint(expr=   m.x94 + m.x95 == 106.777870451)

m.c37 = Constraint(expr=   m.x96 + m.x97 == 106.777870451)

m.c38 = Constraint(expr=   m.x98 + m.x99 == 106.777870451)

m.c39 = Constraint(expr=   m.x100 + m.x101 == 106.777870451)

m.c40 = Constraint(expr=   m.x102 + m.x103 == 106.777870451)

m.c41 = Constraint(expr=   m.x104 + m.x105 == 106.777870451)

m.c42 = Constraint(expr=   m.x106 + m.x107 == 106.777870451)

m.c43 = Constraint(expr=   m.x108 + m.x109 == 106.777870451)

m.c44 = Constraint(expr=   m.x110 + m.x111 == 106.777870451)

m.c45 = Constraint(expr=   m.x112 + m.x113 == 106.777870451)

m.c46 = Constraint(expr=   m.x114 + m.x115 == 106.777870452)

m.c47 = Constraint(expr=   m.x116 + m.x117 == 106.777870452)

m.c48 = Constraint(expr=   m.x118 + m.x119 == 106.777870452)

m.c49 = Constraint(expr=   m.x120 + m.x121 == 106.777870452)

m.c50 = Constraint(expr= - m.x122 + m.x123 == 0)

m.c51 = Constraint(expr= - m.x124 + m.x125 == 0)

m.c52 = Constraint(expr= - m.x126 + m.x127 == 0)

m.c53 = Constraint(expr= - m.x128 + m.x129 == 0)

m.c54 = Constraint(expr=   m.x122 - m.x130 - m.x131 - m.x132 == 0)

m.c55 = Constraint(expr=   m.x124 - m.x133 - m.x134 - m.x135 == 0)

m.c56 = Constraint(expr=   m.x126 - m.x136 - m.x137 - m.x138 == 0)

m.c57 = Constraint(expr=   m.x128 - m.x139 - m.x140 - m.x141 == 0)

m.c58 = Constraint(expr=   m.x142 == 0.025)

m.c59 = Constraint(expr=   m.x143 == 0.025)

m.c60 = Constraint(expr=   m.x144 == 0.025)

m.c61 = Constraint(expr=   m.x145 == 0.025)

m.c62 = Constraint(expr=   m.x146 == 0.013)

m.c63 = Constraint(expr=   m.x147 == 0.012)

m.c64 = Constraint(expr=   m.x148 == 0.007)

m.c65 = Constraint(expr=   m.x149 == 0.001)

m.c66 = Constraint(expr=   m.x150 + m.x151 - m.x152 == 0)

m.c67 = Constraint(expr=   m.x153 + m.x154 - m.x155 == 0)

m.c68 = Constraint(expr=   m.x156 + m.x157 - m.x158 == 0)

m.c69 = Constraint(expr=   m.x159 + m.x160 - m.x161 == 0)

m.c70 = Constraint(expr=   m.x132 - m.x150 + m.x162 - m.x163 == 0)

m.c71 = Constraint(expr=   m.x135 - m.x153 + m.x164 - m.x165 == 0)

m.c72 = Constraint(expr=   m.x138 - m.x156 + m.x166 - m.x167 == 0)

m.c73 = Constraint(expr=   m.x141 - m.x159 + m.x168 - m.x169 == 0)

m.c74 = Constraint(expr=   m.x131 - m.x170 == 0)

m.c75 = Constraint(expr=   m.x134 - m.x171 == 0)

m.c76 = Constraint(expr=   m.x137 - m.x172 == 0)

m.c77 = Constraint(expr=   m.x140 - m.x173 == 0)

m.c78 = Constraint(expr=   m.x152 + m.x174 + m.x175 + m.x176 - m.x177 - m.x178 == 0)

m.c79 = Constraint(expr=   m.x155 + m.x179 + m.x180 + m.x181 - m.x182 - m.x183 == 0)

m.c80 = Constraint(expr=   m.x158 + m.x184 + m.x185 + m.x186 - m.x187 - m.x188 == 0)

m.c81 = Constraint(expr=   m.x161 + m.x189 + m.x190 + m.x191 - m.x192 - m.x193 == 0)

m.c82 = Constraint(expr= - m.x142 + m.x163 + m.x170 - m.x194 == 0)

m.c83 = Constraint(expr= - m.x143 + m.x165 + m.x171 - m.x195 == 0)

m.c84 = Constraint(expr= - m.x144 + m.x167 + m.x172 - m.x196 == 0)

m.c85 = Constraint(expr= - m.x145 + m.x169 + m.x173 - m.x197 == 0)

m.c86 = Constraint(expr= - m.x146 - m.x151 + m.x194 == 0)

m.c87 = Constraint(expr= - m.x147 - m.x154 + m.x195 == 0)

m.c88 = Constraint(expr= - m.x148 - m.x157 + m.x196 == 0)

m.c89 = Constraint(expr= - m.x149 - m.x160 + m.x197 == 0)

m.c90 = Constraint(expr=   m.x130 - m.x162 == 0)

m.c91 = Constraint(expr=   m.x133 - m.x164 == 0)

m.c92 = Constraint(expr=   m.x136 - m.x166 == 0)

m.c93 = Constraint(expr=   m.x139 - m.x168 == 0)

m.c94 = Constraint(expr= - m.x198 == 0.1624)

m.c95 = Constraint(expr= - m.x199 == 0.1616)

m.c96 = Constraint(expr= - m.x200 == 0.0912)

m.c97 = Constraint(expr= - m.x201 == 0.0952)

m.c98 = Constraint(expr=   m.x198 - m.x202 + m.x203 == 0)

m.c99 = Constraint(expr=   m.x199 - m.x204 + m.x205 == 0)

m.c100 = Constraint(expr=   m.x200 - m.x206 + m.x207 == 0)

m.c101 = Constraint(expr=   m.x201 - m.x208 + m.x209 == 0)

m.c102 = Constraint(expr=   m.x210 + m.x211 - m.x212 == 0)

m.c103 = Constraint(expr=   m.x213 + m.x214 - m.x215 == 0)

m.c104 = Constraint(expr=   m.x216 + m.x217 - m.x218 == 0)

m.c105 = Constraint(expr=   m.x219 + m.x220 - m.x221 == 0)

m.c106 = Constraint(expr=   m.x212 + m.x222 - m.x223 == 0)

m.c107 = Constraint(expr=   m.x215 + m.x224 - m.x225 == 0)

m.c108 = Constraint(expr=   m.x218 + m.x226 - m.x227 == 0)

m.c109 = Constraint(expr=   m.x221 + m.x228 - m.x229 == 0)

m.c110 = Constraint(expr= - m.x222 - m.x230 == 0.0138888888888889)

m.c111 = Constraint(expr= - m.x224 - m.x231 == 0.0138888888888889)

m.c112 = Constraint(expr= - m.x226 - m.x232 == 0.0138888888888889)

m.c113 = Constraint(expr= - m.x228 - m.x233 == 0.0138888888888889)

m.c114 = Constraint(expr= - m.x175 + m.x230 - m.x234 == 0)

m.c115 = Constraint(expr= - m.x180 + m.x231 - m.x235 == 0)

m.c116 = Constraint(expr= - m.x185 + m.x232 - m.x236 == 0)

m.c117 = Constraint(expr= - m.x190 + m.x233 - m.x237 == 0)

m.c118 = Constraint(expr=   m.x238 == 0)

m.c119 = Constraint(expr=   m.x239 == 0)

m.c120 = Constraint(expr=   m.x240 == 0)

m.c121 = Constraint(expr=   m.x241 == 0)

m.c122 = Constraint(expr= - m.x176 + m.x223 == 0)

m.c123 = Constraint(expr= - m.x181 + m.x225 == 0)

m.c124 = Constraint(expr= - m.x186 + m.x227 == 0)

m.c125 = Constraint(expr= - m.x191 + m.x229 == 0)

m.c126 = Constraint(expr= - m.x174 - m.x203 == 0)

m.c127 = Constraint(expr= - m.x179 - m.x205 == 0)

m.c128 = Constraint(expr= - m.x184 - m.x207 == 0)

m.c129 = Constraint(expr= - m.x189 - m.x209 == 0)

m.c130 = Constraint(expr= - m.x123 + m.x242 == 0)

m.c131 = Constraint(expr= - m.x125 + m.x243 == 0)

m.c132 = Constraint(expr= - m.x127 + m.x244 == 0)

m.c133 = Constraint(expr= - m.x129 + m.x245 == 0)

m.c134 = Constraint(expr=   3600*m.x202 + 239.978718892*m.x246 - 239.978718892*m.x247 == 0)

m.c135 = Constraint(expr=   3600*m.x204 + 239.978718892*m.x248 - 239.978718892*m.x249 == 0)

m.c136 = Constraint(expr=   3600*m.x206 + 239.978718892*m.x250 - 239.978718892*m.x251 == 0)

m.c137 = Constraint(expr=   3600*m.x208 + 239.978718892*m.x252 - 239.978718892*m.x253 == 0)

m.c138 = Constraint(expr=   3600*m.x177 - 3600*m.x210 + 416.560177655*m.x254 - 416.560177655*m.x255 == 0)

m.c139 = Constraint(expr=   3600*m.x182 - 3600*m.x213 + 416.560177655*m.x256 - 416.560177655*m.x257 == 0)

m.c140 = Constraint(expr=   3600*m.x187 - 3600*m.x216 + 416.560177655*m.x258 - 416.560177655*m.x259 == 0)

m.c141 = Constraint(expr=   3600*m.x192 - 3600*m.x219 + 416.560177655*m.x260 - 416.560177655*m.x261 == 0)

m.c142 = Constraint(expr=   3600*m.x178 - 3600*m.x211 + 416.560177655*m.x262 - 416.560177655*m.x263 == 0)

m.c143 = Constraint(expr=   3600*m.x183 - 3600*m.x214 + 416.560177655*m.x264 - 416.560177655*m.x265 == 0)

m.c144 = Constraint(expr=   3600*m.x188 - 3600*m.x217 + 416.560177655*m.x266 - 416.560177655*m.x267 == 0)

m.c145 = Constraint(expr=   3600*m.x193 - 3600*m.x220 + 416.560177655*m.x268 - 416.560177655*m.x269 == 0)

m.c146 = Constraint(expr=   3600*m.x234 - 3600*m.x238 + 165.129961038*m.x270 - 165.129961038*m.x271 == 0)

m.c147 = Constraint(expr=   3600*m.x235 - 3600*m.x239 + 165.129961038*m.x272 - 165.129961038*m.x273 == 0)

m.c148 = Constraint(expr=   3600*m.x236 - 3600*m.x240 + 165.129961038*m.x274 - 165.129961038*m.x275 == 0)

m.c149 = Constraint(expr=   3600*m.x237 - 3600*m.x241 + 165.129961038*m.x276 - 165.129961038*m.x277 == 0)

m.c150 = Constraint(expr= - m.x247 + m.x248 == 0)

m.c151 = Constraint(expr= - m.x249 + m.x250 == 0)

m.c152 = Constraint(expr= - m.x251 + m.x252 == 0)

m.c153 = Constraint(expr= - m.x255 + m.x256 == 0)

m.c154 = Constraint(expr= - m.x257 + m.x258 == 0)

m.c155 = Constraint(expr= - m.x259 + m.x260 == 0)

m.c156 = Constraint(expr= - m.x263 + m.x264 == 0)

m.c157 = Constraint(expr= - m.x265 + m.x266 == 0)

m.c158 = Constraint(expr= - m.x267 + m.x268 == 0)

m.c159 = Constraint(expr= - m.x271 + m.x272 == 0)

m.c160 = Constraint(expr= - m.x273 + m.x274 == 0)

m.c161 = Constraint(expr= - m.x275 + m.x276 == 0)

m.c162 = Constraint(expr= - 0.037494*m.b2 + m.x278 >= 0)

m.c163 = Constraint(expr= - 0.037494*m.b3 + m.x280 >= 0)

m.c164 = Constraint(expr= - 0.037494*m.b4 + m.x282 >= 0)

m.c165 = Constraint(expr= - 0.037494*m.b5 + m.x284 >= 0)

m.c166 = Constraint(expr= - 0.074997*m.b6 + m.x286 >= 0)

m.c167 = Constraint(expr= - 0.074997*m.b7 + m.x288 >= 0)

m.c168 = Constraint(expr= - 0.074997*m.b8 + m.x290 >= 0)

m.c169 = Constraint(expr= - 0.074997*m.b9 + m.x292 >= 0)

m.c170 = Constraint(expr= - 0.074997*m.b10 + m.x294 >= 0)

m.c171 = Constraint(expr= - 0.074997*m.b11 + m.x296 >= 0)

m.c172 = Constraint(expr= - 0.074997*m.b12 + m.x298 >= 0)

m.c173 = Constraint(expr= - 0.074997*m.b13 + m.x300 >= 0)

m.c174 = Constraint(expr= - 0.074997*m.b14 + m.x302 >= 0)

m.c175 = Constraint(expr= - 0.074997*m.b15 + m.x304 >= 0)

m.c176 = Constraint(expr= - 0.074997*m.b16 + m.x306 >= 0)

m.c177 = Constraint(expr= - 0.074997*m.b17 + m.x308 >= 0)

m.c178 = Constraint(expr= - 0.074997*m.b18 + m.x310 >= 0)

m.c179 = Constraint(expr= - 0.074997*m.b19 + m.x312 >= 0)

m.c180 = Constraint(expr= - 0.074997*m.b20 + m.x314 >= 0)

m.c181 = Constraint(expr= - 0.074997*m.b21 + m.x316 >= 0)

m.c182 = Constraint(expr= - 0.074997*m.b22 + m.x318 >= 0)

m.c183 = Constraint(expr= - 0.074997*m.b23 + m.x320 >= 0)

m.c184 = Constraint(expr= - 0.074997*m.b24 + m.x322 >= 0)

m.c185 = Constraint(expr= - 0.074997*m.b25 + m.x324 >= 0)

m.c186 = Constraint(expr= - 0.074997*m.b26 + m.x326 >= 0)

m.c187 = Constraint(expr= - 0.074997*m.b27 + m.x328 >= 0)

m.c188 = Constraint(expr= - 0.074997*m.b28 + m.x330 >= 0)

m.c189 = Constraint(expr= - 0.074997*m.b29 + m.x332 >= 0)

m.c190 = Constraint(expr= - 0.037494*m.b30 + m.x334 >= 0)

m.c191 = Constraint(expr= - 0.037494*m.b31 + m.x336 >= 0)

m.c192 = Constraint(expr= - 0.037494*m.b32 + m.x338 >= 0)

m.c193 = Constraint(expr= - 0.037494*m.b33 + m.x340 >= 0)

m.c194 = Constraint(expr= - 0.097497*m.b34 + m.x342 >= 0)

m.c195 = Constraint(expr= - 0.097497*m.b35 + m.x344 >= 0)

m.c196 = Constraint(expr= - 0.097497*m.b36 + m.x346 >= 0)

m.c197 = Constraint(expr= - 0.097497*m.b37 + m.x348 >= 0)

m.c198 = Constraint(expr= - 0.097497*m.b38 + m.x350 >= 0)

m.c199 = Constraint(expr= - 0.097497*m.b39 + m.x352 >= 0)

m.c200 = Constraint(expr= - 0.097497*m.b40 + m.x354 >= 0)

m.c201 = Constraint(expr= - 0.097497*m.b41 + m.x356 >= 0)

m.c202 = Constraint(expr= - 0.097497*m.b42 + m.x358 >= 0)

m.c203 = Constraint(expr= - 0.097497*m.b43 + m.x360 >= 0)

m.c204 = Constraint(expr= - 0.097497*m.b44 + m.x362 >= 0)

m.c205 = Constraint(expr= - 0.097497*m.b45 + m.x364 >= 0)

m.c206 = Constraint(expr= - 0.058743*m.b46 + m.x366 >= 0)

m.c207 = Constraint(expr= - 0.058743*m.b47 + m.x368 >= 0)

m.c208 = Constraint(expr= - 0.058743*m.b48 + m.x370 >= 0)

m.c209 = Constraint(expr= - 0.058743*m.b49 + m.x372 >= 0)

m.c210 = Constraint(expr= - 0.045826*m.b2 + m.x278 <= 0)

m.c211 = Constraint(expr= - 0.045826*m.b3 + m.x280 <= 0)

m.c212 = Constraint(expr= - 0.045826*m.b4 + m.x282 <= 0)

m.c213 = Constraint(expr= - 0.045826*m.b5 + m.x284 <= 0)

m.c214 = Constraint(expr= - 0.091663*m.b6 + m.x286 <= 0)

m.c215 = Constraint(expr= - 0.091663*m.b7 + m.x288 <= 0)

m.c216 = Constraint(expr= - 0.091663*m.b8 + m.x290 <= 0)

m.c217 = Constraint(expr= - 0.091663*m.b9 + m.x292 <= 0)

m.c218 = Constraint(expr= - 0.091663*m.b10 + m.x294 <= 0)

m.c219 = Constraint(expr= - 0.091663*m.b11 + m.x296 <= 0)

m.c220 = Constraint(expr= - 0.091663*m.b12 + m.x298 <= 0)

m.c221 = Constraint(expr= - 0.091663*m.b13 + m.x300 <= 0)

m.c222 = Constraint(expr= - 0.091663*m.b14 + m.x302 <= 0)

m.c223 = Constraint(expr= - 0.091663*m.b15 + m.x304 <= 0)

m.c224 = Constraint(expr= - 0.091663*m.b16 + m.x306 <= 0)

m.c225 = Constraint(expr= - 0.091663*m.b17 + m.x308 <= 0)

m.c226 = Constraint(expr= - 0.091663*m.b18 + m.x310 <= 0)

m.c227 = Constraint(expr= - 0.091663*m.b19 + m.x312 <= 0)

m.c228 = Constraint(expr= - 0.091663*m.b20 + m.x314 <= 0)

m.c229 = Constraint(expr= - 0.091663*m.b21 + m.x316 <= 0)

m.c230 = Constraint(expr= - 0.091663*m.b22 + m.x318 <= 0)

m.c231 = Constraint(expr= - 0.091663*m.b23 + m.x320 <= 0)

m.c232 = Constraint(expr= - 0.091663*m.b24 + m.x322 <= 0)

m.c233 = Constraint(expr= - 0.091663*m.b25 + m.x324 <= 0)

m.c234 = Constraint(expr= - 0.091663*m.b26 + m.x326 <= 0)

m.c235 = Constraint(expr= - 0.091663*m.b27 + m.x328 <= 0)

m.c236 = Constraint(expr= - 0.091663*m.b28 + m.x330 <= 0)

m.c237 = Constraint(expr= - 0.091663*m.b29 + m.x332 <= 0)

m.c238 = Constraint(expr= - 0.045826*m.b30 + m.x334 <= 0)

m.c239 = Constraint(expr= - 0.045826*m.b31 + m.x336 <= 0)

m.c240 = Constraint(expr= - 0.045826*m.b32 + m.x338 <= 0)

m.c241 = Constraint(expr= - 0.045826*m.b33 + m.x340 <= 0)

m.c242 = Constraint(expr= - 0.119163*m.b34 + m.x342 <= 0)

m.c243 = Constraint(expr= - 0.119163*m.b35 + m.x344 <= 0)

m.c244 = Constraint(expr= - 0.119163*m.b36 + m.x346 <= 0)

m.c245 = Constraint(expr= - 0.119163*m.b37 + m.x348 <= 0)

m.c246 = Constraint(expr= - 0.119163*m.b38 + m.x350 <= 0)

m.c247 = Constraint(expr= - 0.119163*m.b39 + m.x352 <= 0)

m.c248 = Constraint(expr= - 0.119163*m.b40 + m.x354 <= 0)

m.c249 = Constraint(expr= - 0.119163*m.b41 + m.x356 <= 0)

m.c250 = Constraint(expr= - 0.119163*m.b42 + m.x358 <= 0)

m.c251 = Constraint(expr= - 0.119163*m.b43 + m.x360 <= 0)

m.c252 = Constraint(expr= - 0.119163*m.b44 + m.x362 <= 0)

m.c253 = Constraint(expr= - 0.119163*m.b45 + m.x364 <= 0)

m.c254 = Constraint(expr= - 0.071797*m.b46 + m.x366 <= 0)

m.c255 = Constraint(expr= - 0.071797*m.b47 + m.x368 <= 0)

m.c256 = Constraint(expr= - 0.071797*m.b48 + m.x370 <= 0)

m.c257 = Constraint(expr= - 0.071797*m.b49 + m.x372 <= 0)

m.c258 = Constraint(expr= - m.x246 + m.x374 == 300)

m.c259 = Constraint(expr= - m.x248 + m.x375 == 300)

m.c260 = Constraint(expr= - m.x250 + m.x376 == 300)

m.c261 = Constraint(expr= - m.x252 + m.x377 == 300)

m.c262 = Constraint(expr= - m.x254 + m.x378 == 240)

m.c263 = Constraint(expr= - m.x256 + m.x379 == 240)

m.c264 = Constraint(expr= - m.x258 + m.x380 == 240)

m.c265 = Constraint(expr= - m.x260 + m.x381 == 240)

m.c266 = Constraint(expr= - m.x262 + m.x382 == 240)

m.c267 = Constraint(expr= - m.x264 + m.x383 == 240)

m.c268 = Constraint(expr= - m.x266 + m.x384 == 240)

m.c269 = Constraint(expr= - m.x268 + m.x385 == 240)

m.c270 = Constraint(expr= - m.x270 + m.x386 == 243)

m.c271 = Constraint(expr= - m.x272 + m.x387 == 243)

m.c272 = Constraint(expr= - m.x274 + m.x388 == 243)

m.c273 = Constraint(expr= - m.x276 + m.x389 == 243)

m.c274 = Constraint(expr=   m.x390 - m.x391 - m.x392 == 0)

m.c275 = Constraint(expr=   m.x393 - m.x394 - m.x395 == 0)

m.c276 = Constraint(expr=   m.x396 - m.x397 - m.x398 == 0)

m.c277 = Constraint(expr=   m.x399 - m.x400 - m.x401 == 0)

m.c278 = Constraint(expr=   m.x391 - m.x402 - m.x403 == 0)

m.c279 = Constraint(expr=   m.x394 - m.x404 - m.x405 == 0)

m.c280 = Constraint(expr=   m.x397 - m.x406 - m.x407 == 0)

m.c281 = Constraint(expr=   m.x400 - m.x408 - m.x409 == 0)

m.c282 = Constraint(expr=   m.x391 - m.x410 - m.x411 == 0)

m.c283 = Constraint(expr=   m.x394 - m.x412 - m.x413 == 0)

m.c284 = Constraint(expr=   m.x397 - m.x414 - m.x415 == 0)

m.c285 = Constraint(expr=   m.x400 - m.x416 - m.x417 == 0)

m.c286 = Constraint(expr=   m.x418 - m.x419 - m.x420 == 0)

m.c287 = Constraint(expr=   m.x421 - m.x422 - m.x423 == 0)

m.c288 = Constraint(expr=   m.x424 - m.x425 - m.x426 == 0)

m.c289 = Constraint(expr=   m.x427 - m.x428 - m.x429 == 0)

m.c290 = Constraint(expr= - m.x430 + m.x431 - m.x432 == 0)

m.c291 = Constraint(expr= - m.x433 + m.x434 - m.x435 == 0)

m.c292 = Constraint(expr= - m.x436 + m.x437 - m.x438 == 0)

m.c293 = Constraint(expr= - m.x439 + m.x440 - m.x441 == 0)

m.c294 = Constraint(expr=   m.x410 - m.x430 - m.x442 == 0)

m.c295 = Constraint(expr=   m.x412 - m.x433 - m.x443 == 0)

m.c296 = Constraint(expr=   m.x414 - m.x436 - m.x444 == 0)

m.c297 = Constraint(expr=   m.x416 - m.x439 - m.x445 == 0)

m.c298 = Constraint(expr=   m.x391 - m.x418 - m.x446 == 0)

m.c299 = Constraint(expr=   m.x394 - m.x421 - m.x447 == 0)

m.c300 = Constraint(expr=   m.x397 - m.x424 - m.x448 == 0)

m.c301 = Constraint(expr=   m.x400 - m.x427 - m.x449 == 0)

m.c302 = Constraint(expr=   m.x419 - m.x431 - m.x450 == 0)

m.c303 = Constraint(expr=   m.x422 - m.x434 - m.x451 == 0)

m.c304 = Constraint(expr=   m.x425 - m.x437 - m.x452 == 0)

m.c305 = Constraint(expr=   m.x428 - m.x440 - m.x453 == 0)

m.c306 = Constraint(expr=   m.x402 - m.x410 - m.x454 == 0)

m.c307 = Constraint(expr=   m.x404 - m.x412 - m.x455 == 0)

m.c308 = Constraint(expr=   m.x406 - m.x414 - m.x456 == 0)

m.c309 = Constraint(expr=   m.x408 - m.x416 - m.x457 == 0)

m.c310 = Constraint(expr=   m.x410 - m.x419 - m.x458 == 0)

m.c311 = Constraint(expr=   m.x412 - m.x422 - m.x459 == 0)

m.c312 = Constraint(expr=   m.x414 - m.x425 - m.x460 == 0)

m.c313 = Constraint(expr=   m.x416 - m.x428 - m.x461 == 0)

m.c314 = Constraint(expr=   m.x419 - m.x462 - m.x463 == 0)

m.c315 = Constraint(expr=   m.x422 - m.x464 - m.x465 == 0)

m.c316 = Constraint(expr=   m.x425 - m.x466 - m.x467 == 0)

m.c317 = Constraint(expr=   m.x428 - m.x468 - m.x469 == 0)

m.c318 = Constraint(expr=   m.x431 - m.x470 - m.x471 == 0)

m.c319 = Constraint(expr=   m.x434 - m.x472 - m.x473 == 0)

m.c320 = Constraint(expr=   m.x437 - m.x474 - m.x475 == 0)

m.c321 = Constraint(expr=   m.x440 - m.x476 - m.x477 == 0)

m.c322 = Constraint(expr= - m.x478 + m.x479 - m.x480 == 0)

m.c323 = Constraint(expr= - m.x481 + m.x482 - m.x483 == 0)

m.c324 = Constraint(expr= - m.x484 + m.x485 - m.x486 == 0)

m.c325 = Constraint(expr= - m.x487 + m.x488 - m.x489 == 0)

m.c326 = Constraint(expr= - m.x490 + m.x491 - m.x492 == 0)

m.c327 = Constraint(expr= - m.x493 + m.x494 - m.x495 == 0)

m.c328 = Constraint(expr= - m.x496 + m.x497 - m.x498 == 0)

m.c329 = Constraint(expr= - m.x499 + m.x500 - m.x501 == 0)

m.c330 = Constraint(expr= - m.x374 + m.x490 - m.x502 == 0)

m.c331 = Constraint(expr= - m.x375 + m.x493 - m.x503 == 0)

m.c332 = Constraint(expr= - m.x376 + m.x496 - m.x504 == 0)

m.c333 = Constraint(expr= - m.x377 + m.x499 - m.x505 == 0)

m.c334 = Constraint(expr=   m.x378 - m.x506 - m.x507 == 0)

m.c335 = Constraint(expr=   m.x379 - m.x508 - m.x509 == 0)

m.c336 = Constraint(expr=   m.x380 - m.x510 - m.x511 == 0)

m.c337 = Constraint(expr=   m.x381 - m.x512 - m.x513 == 0)

m.c338 = Constraint(expr=   m.x382 - m.x506 - m.x514 == 0)

m.c339 = Constraint(expr=   m.x383 - m.x508 - m.x515 == 0)

m.c340 = Constraint(expr=   m.x384 - m.x510 - m.x516 == 0)

m.c341 = Constraint(expr=   m.x385 - m.x512 - m.x517 == 0)

m.c342 = Constraint(expr= - m.x518 + m.x519 - m.x520 == 0)

m.c343 = Constraint(expr= - m.x521 + m.x522 - m.x523 == 0)

m.c344 = Constraint(expr= - m.x524 + m.x525 - m.x526 == 0)

m.c345 = Constraint(expr= - m.x527 + m.x528 - m.x529 == 0)

m.c346 = Constraint(expr= - m.x478 + m.x530 - m.x531 == 0)

m.c347 = Constraint(expr= - m.x481 + m.x532 - m.x533 == 0)

m.c348 = Constraint(expr= - m.x484 + m.x534 - m.x535 == 0)

m.c349 = Constraint(expr= - m.x487 + m.x536 - m.x537 == 0)

m.c350 = Constraint(expr=   m.x519 - m.x530 - m.x538 == 0)

m.c351 = Constraint(expr=   m.x522 - m.x532 - m.x539 == 0)

m.c352 = Constraint(expr=   m.x525 - m.x534 - m.x540 == 0)

m.c353 = Constraint(expr=   m.x528 - m.x536 - m.x541 == 0)

m.c354 = Constraint(expr= - m.x478 + m.x542 - m.x543 == 0)

m.c355 = Constraint(expr= - m.x481 + m.x544 - m.x545 == 0)

m.c356 = Constraint(expr= - m.x484 + m.x546 - m.x547 == 0)

m.c357 = Constraint(expr= - m.x487 + m.x548 - m.x549 == 0)

m.c358 = Constraint(expr=   m.x386 - m.x550 - m.x551 == 0)

m.c359 = Constraint(expr=   m.x387 - m.x552 - m.x553 == 0)

m.c360 = Constraint(expr=   m.x388 - m.x554 - m.x555 == 0)

m.c361 = Constraint(expr=   m.x389 - m.x556 - m.x557 == 0)

m.c362 = Constraint(expr=   m.x390 - m.x558 - m.x559 == 0)

m.c363 = Constraint(expr=   m.x393 - m.x560 - m.x561 == 0)

m.c364 = Constraint(expr=   m.x396 - m.x562 - m.x563 == 0)

m.c365 = Constraint(expr=   m.x399 - m.x564 - m.x565 == 0)

m.c366 = Constraint(expr= - m.x506 + m.x518 - m.x566 == 0)

m.c367 = Constraint(expr= - m.x508 + m.x521 - m.x567 == 0)

m.c368 = Constraint(expr= - m.x510 + m.x524 - m.x568 == 0)

m.c369 = Constraint(expr= - m.x512 + m.x527 - m.x569 == 0)

m.c370 = Constraint(expr= - 239.978718892*m.x246 + 239.978718892*m.x253 - 416.560177655*m.x254 + 416.560177655*m.x261
                          - 416.560177655*m.x262 + 416.560177655*m.x269 - 165.129961038*m.x270 + 165.129961038*m.x277
                          >= 0)

m.c371 = Constraint(expr=   m.b2 - m.b30 >= 0)

m.c372 = Constraint(expr=   m.b3 - m.b31 >= 0)

m.c373 = Constraint(expr=   m.b4 - m.b32 >= 0)

m.c374 = Constraint(expr=   m.b5 - m.b33 >= 0)

m.c375 = Constraint(expr=   m.b6 - m.b10 >= 0)

m.c376 = Constraint(expr=   m.b7 - m.b11 >= 0)

m.c377 = Constraint(expr=   m.b8 - m.b12 >= 0)

m.c378 = Constraint(expr=   m.b9 - m.b13 >= 0)

m.c379 = Constraint(expr=   m.b10 - m.b14 >= 0)

m.c380 = Constraint(expr=   m.b11 - m.b15 >= 0)

m.c381 = Constraint(expr=   m.b12 - m.b16 >= 0)

m.c382 = Constraint(expr=   m.b13 - m.b17 >= 0)

m.c383 = Constraint(expr=   m.b14 - m.b18 >= 0)

m.c384 = Constraint(expr=   m.b15 - m.b19 >= 0)

m.c385 = Constraint(expr=   m.b16 - m.b20 >= 0)

m.c386 = Constraint(expr=   m.b17 - m.b21 >= 0)

m.c387 = Constraint(expr=   m.b18 - m.b22 >= 0)

m.c388 = Constraint(expr=   m.b19 - m.b23 >= 0)

m.c389 = Constraint(expr=   m.b20 - m.b24 >= 0)

m.c390 = Constraint(expr=   m.b21 - m.b25 >= 0)

m.c391 = Constraint(expr=   m.b22 - m.b26 >= 0)

m.c392 = Constraint(expr=   m.b23 - m.b27 >= 0)

m.c393 = Constraint(expr=   m.b24 - m.b28 >= 0)

m.c394 = Constraint(expr=   m.b25 - m.b29 >= 0)

m.c395 = Constraint(expr=   m.b34 - m.b38 >= 0)

m.c396 = Constraint(expr=   m.b35 - m.b39 >= 0)

m.c397 = Constraint(expr=   m.b36 - m.b40 >= 0)

m.c398 = Constraint(expr=   m.b37 - m.b41 >= 0)

m.c399 = Constraint(expr=   m.b38 - m.b42 >= 0)

m.c400 = Constraint(expr=   m.b39 - m.b43 >= 0)

m.c401 = Constraint(expr=   m.b40 - m.b44 >= 0)

m.c402 = Constraint(expr=   m.b41 - m.b45 >= 0)

m.c403 = Constraint(expr=   m.x123 - m.x278 - m.x286 - m.x294 - m.x302 - m.x310 - m.x318 - m.x326 - m.x334 == 0)

m.c404 = Constraint(expr=   m.x125 - m.x280 - m.x288 - m.x296 - m.x304 - m.x312 - m.x320 - m.x328 - m.x336 == 0)

m.c405 = Constraint(expr=   m.x127 - m.x282 - m.x290 - m.x298 - m.x306 - m.x314 - m.x322 - m.x330 - m.x338 == 0)

m.c406 = Constraint(expr=   m.x129 - m.x284 - m.x292 - m.x300 - m.x308 - m.x316 - m.x324 - m.x332 - m.x340 == 0)

m.c407 = Constraint(expr=   m.x212 - m.x342 - m.x350 - m.x358 - m.x366 == 0)

m.c408 = Constraint(expr=   m.x215 - m.x344 - m.x352 - m.x360 - m.x368 == 0)

m.c409 = Constraint(expr=   m.x218 - m.x346 - m.x354 - m.x362 - m.x370 == 0)

m.c410 = Constraint(expr=   m.x221 - m.x348 - m.x356 - m.x364 - m.x372 == 0)

m.c411 = Constraint(expr= - 712.572602172813*m.b2 + m.x279 - m.x559 >= -712.572602172813)

m.c412 = Constraint(expr= - 712.572602172813*m.b3 + m.x283 - m.x561 >= -712.572602172813)

m.c413 = Constraint(expr= - 712.572602172813*m.b4 + m.x287 - m.x563 >= -712.572602172813)

m.c414 = Constraint(expr= - 712.572602172813*m.b5 + m.x291 - m.x565 >= -712.572602172813)

m.c415 = Constraint(expr= - 851.700667228731*m.b6 + m.x297 - m.x559 >= -851.700667228731)

m.c416 = Constraint(expr= - 851.700667228731*m.b7 + m.x303 - m.x561 >= -851.700667228731)

m.c417 = Constraint(expr= - 851.700667228731*m.b8 + m.x309 - m.x563 >= -851.700667228731)

m.c418 = Constraint(expr= - 851.700667228731*m.b9 + m.x315 - m.x565 >= -851.700667228731)

m.c419 = Constraint(expr= - 851.700667228731*m.b10 + m.x321 - m.x559 >= -851.700667228731)

m.c420 = Constraint(expr= - 851.700667228731*m.b11 + m.x327 - m.x561 >= -851.700667228731)

m.c421 = Constraint(expr= - 851.700667228731*m.b12 + m.x333 - m.x563 >= -851.700667228731)

m.c422 = Constraint(expr= - 851.700667228731*m.b13 + m.x339 - m.x565 >= -851.700667228731)

m.c423 = Constraint(expr= - 851.700667228731*m.b14 + m.x345 - m.x559 >= -851.700667228731)

m.c424 = Constraint(expr= - 851.700667228731*m.b15 + m.x351 - m.x561 >= -851.700667228731)

m.c425 = Constraint(expr= - 851.700667228731*m.b16 + m.x357 - m.x563 >= -851.700667228731)

m.c426 = Constraint(expr= - 851.700667228731*m.b17 + m.x363 - m.x565 >= -851.700667228731)

m.c427 = Constraint(expr= - 851.700667228731*m.b18 + m.x369 - m.x559 >= -851.700667228731)

m.c428 = Constraint(expr= - 851.700667228731*m.b19 - m.x561 + m.x606 >= -851.700667228731)

m.c429 = Constraint(expr= - 851.700667228731*m.b20 - m.x563 + m.x609 >= -851.700667228731)

m.c430 = Constraint(expr= - 851.700667228731*m.b21 - m.x565 + m.x612 >= -851.700667228731)

m.c431 = Constraint(expr= - 851.700667228731*m.b22 - m.x559 + m.x615 >= -851.700667228731)

m.c432 = Constraint(expr= - 851.700667228731*m.b23 + m.x62 - m.x561 >= -851.700667228731)

m.c433 = Constraint(expr= - 851.700667228731*m.b24 + m.x65 - m.x563 >= -851.700667228731)

m.c434 = Constraint(expr= - 851.700667228731*m.b25 + m.x68 - m.x565 >= -851.700667228731)

m.c435 = Constraint(expr= - 851.700667228731*m.b26 + m.x71 - m.x559 >= -851.700667228731)

m.c436 = Constraint(expr= - 851.700667228731*m.b27 + m.x74 - m.x561 >= -851.700667228731)

m.c437 = Constraint(expr= - 851.700667228731*m.b28 + m.x77 - m.x563 >= -851.700667228731)

m.c438 = Constraint(expr= - 851.700667228731*m.b29 + m.x80 - m.x565 >= -851.700667228731)

m.c439 = Constraint(expr= - 712.572602172813*m.b30 + m.x82 - m.x559 >= -712.572602172813)

m.c440 = Constraint(expr= - 712.572602172813*m.b31 + m.x84 - m.x561 >= -712.572602172813)

m.c441 = Constraint(expr= - 712.572602172813*m.b32 + m.x86 - m.x563 >= -712.572602172813)

m.c442 = Constraint(expr= - 712.572602172813*m.b33 + m.x88 - m.x565 >= -712.572602172813)

m.c443 = Constraint(expr= - 925.825187656153*m.b34 + m.x90 - m.x566 >= -925.825187656153)

m.c444 = Constraint(expr= - 925.825187656153*m.b35 + m.x92 - m.x567 >= -925.825187656153)

m.c445 = Constraint(expr= - 925.825187656153*m.b36 + m.x94 - m.x568 >= -925.825187656153)

m.c446 = Constraint(expr= - 925.825187656153*m.b37 + m.x96 - m.x569 >= -925.825187656153)

m.c447 = Constraint(expr= - 925.825187656153*m.b38 + m.x98 - m.x566 >= -925.825187656153)

m.c448 = Constraint(expr= - 925.825187656153*m.b39 + m.x100 - m.x567 >= -925.825187656153)

m.c449 = Constraint(expr= - 925.825187656153*m.b40 + m.x102 - m.x568 >= -925.825187656153)

m.c450 = Constraint(expr= - 925.825187656153*m.b41 + m.x104 - m.x569 >= -925.825187656153)

m.c451 = Constraint(expr= - 925.825187656153*m.b42 + m.x106 - m.x566 >= -925.825187656153)

m.c452 = Constraint(expr= - 925.825187656153*m.b43 + m.x108 - m.x567 >= -925.825187656153)

m.c453 = Constraint(expr= - 925.825187656153*m.b44 + m.x110 - m.x568 >= -925.825187656153)

m.c454 = Constraint(expr= - 925.825187656153*m.b45 + m.x112 - m.x569 >= -925.825187656153)

m.c455 = Constraint(expr= - 925.825187656502*m.b46 + m.x114 - m.x566 >= -925.825187656502)

m.c456 = Constraint(expr= - 925.825187656502*m.b47 + m.x116 - m.x567 >= -925.825187656502)

m.c457 = Constraint(expr= - 925.825187656502*m.b48 + m.x118 - m.x568 >= -925.825187656502)

m.c458 = Constraint(expr= - 925.825187656502*m.b49 + m.x120 - m.x569 >= -925.825187656502)

m.c459 = Constraint(expr=   447.864247971*m.b2 + m.x279 - m.x559 <= 447.864247971)

m.c460 = Constraint(expr=   447.864247971*m.b3 + m.x283 - m.x561 <= 447.864247971)

m.c461 = Constraint(expr=   447.864247971*m.b4 + m.x287 - m.x563 <= 447.864247971)

m.c462 = Constraint(expr=   447.864247971*m.b5 + m.x291 - m.x565 <= 447.864247971)

m.c463 = Constraint(expr=   672.20455381568*m.b6 + m.x297 - m.x559 <= 672.20455381568)

m.c464 = Constraint(expr=   672.20455381568*m.b7 + m.x303 - m.x561 <= 672.20455381568)

m.c465 = Constraint(expr=   672.20455381568*m.b8 + m.x309 - m.x563 <= 672.20455381568)

m.c466 = Constraint(expr=   672.20455381568*m.b9 + m.x315 - m.x565 <= 672.20455381568)

m.c467 = Constraint(expr=   672.20455381568*m.b10 + m.x321 - m.x559 <= 672.20455381568)

m.c468 = Constraint(expr=   672.20455381568*m.b11 + m.x327 - m.x561 <= 672.20455381568)

m.c469 = Constraint(expr=   672.20455381568*m.b12 + m.x333 - m.x563 <= 672.20455381568)

m.c470 = Constraint(expr=   672.20455381568*m.b13 + m.x339 - m.x565 <= 672.20455381568)

m.c471 = Constraint(expr=   672.20455381568*m.b14 + m.x345 - m.x559 <= 672.20455381568)

m.c472 = Constraint(expr=   672.20455381568*m.b15 + m.x351 - m.x561 <= 672.20455381568)

m.c473 = Constraint(expr=   672.20455381568*m.b16 + m.x357 - m.x563 <= 672.20455381568)

m.c474 = Constraint(expr=   672.20455381568*m.b17 + m.x363 - m.x565 <= 672.20455381568)

m.c475 = Constraint(expr=   672.20455381568*m.b18 + m.x369 - m.x559 <= 672.20455381568)

m.c476 = Constraint(expr=   672.20455381568*m.b19 - m.x561 + m.x606 <= 672.20455381568)

m.c477 = Constraint(expr=   672.20455381568*m.b20 - m.x563 + m.x609 <= 672.20455381568)

m.c478 = Constraint(expr=   672.20455381568*m.b21 - m.x565 + m.x612 <= 672.20455381568)

m.c479 = Constraint(expr=   672.20455381568*m.b22 - m.x559 + m.x615 <= 672.20455381568)

m.c480 = Constraint(expr=   672.20455381568*m.b23 + m.x62 - m.x561 <= 672.20455381568)

m.c481 = Constraint(expr=   672.20455381568*m.b24 + m.x65 - m.x563 <= 672.20455381568)

m.c482 = Constraint(expr=   672.20455381568*m.b25 + m.x68 - m.x565 <= 672.20455381568)

m.c483 = Constraint(expr=   672.20455381568*m.b26 + m.x71 - m.x559 <= 672.20455381568)

m.c484 = Constraint(expr=   672.20455381568*m.b27 + m.x74 - m.x561 <= 672.20455381568)

m.c485 = Constraint(expr=   672.20455381568*m.b28 + m.x77 - m.x563 <= 672.20455381568)

m.c486 = Constraint(expr=   672.20455381568*m.b29 + m.x80 - m.x565 <= 672.20455381568)

m.c487 = Constraint(expr=   447.864247971*m.b30 + m.x82 - m.x559 <= 447.864247971)

m.c488 = Constraint(expr=   447.864247971*m.b31 + m.x84 - m.x561 <= 447.864247971)

m.c489 = Constraint(expr=   447.864247971*m.b32 + m.x86 - m.x563 <= 447.864247971)

m.c490 = Constraint(expr=   447.864247971*m.b33 + m.x88 - m.x565 <= 447.864247971)

m.c491 = Constraint(expr=   1106.777870451*m.b34 + m.x90 - m.x566 <= 1106.777870451)

m.c492 = Constraint(expr=   1106.777870451*m.b35 + m.x92 - m.x567 <= 1106.777870451)

m.c493 = Constraint(expr=   1106.777870451*m.b36 + m.x94 - m.x568 <= 1106.777870451)

m.c494 = Constraint(expr=   1106.777870451*m.b37 + m.x96 - m.x569 <= 1106.777870451)

m.c495 = Constraint(expr=   1106.777870451*m.b38 + m.x98 - m.x566 <= 1106.777870451)

m.c496 = Constraint(expr=   1106.777870451*m.b39 + m.x100 - m.x567 <= 1106.777870451)

m.c497 = Constraint(expr=   1106.777870451*m.b40 + m.x102 - m.x568 <= 1106.777870451)

m.c498 = Constraint(expr=   1106.777870451*m.b41 + m.x104 - m.x569 <= 1106.777870451)

m.c499 = Constraint(expr=   1106.777870451*m.b42 + m.x106 - m.x566 <= 1106.777870451)

m.c500 = Constraint(expr=   1106.777870451*m.b43 + m.x108 - m.x567 <= 1106.777870451)

m.c501 = Constraint(expr=   1106.777870451*m.b44 + m.x110 - m.x568 <= 1106.777870451)

m.c502 = Constraint(expr=   1106.777870451*m.b45 + m.x112 - m.x569 <= 1106.777870451)

m.c503 = Constraint(expr=   1106.777870452*m.b46 + m.x114 - m.x566 <= 1106.777870452)

m.c504 = Constraint(expr=   1106.777870452*m.b47 + m.x116 - m.x567 <= 1106.777870452)

m.c505 = Constraint(expr=   1106.777870452*m.b48 + m.x118 - m.x568 <= 1106.777870452)

m.c506 = Constraint(expr=   1106.777870452*m.b49 + m.x120 - m.x569 <= 1106.777870452)

m.c507 = Constraint(expr=   m.b2 - m.b3 + m.x570 >= 0)

m.c508 = Constraint(expr=   m.b3 - m.b4 + m.x571 >= 0)

m.c509 = Constraint(expr=   m.b4 - m.b5 + m.x572 >= 0)

m.c510 = Constraint(expr=   m.b6 - m.b7 + m.x573 >= 0)

m.c511 = Constraint(expr=   m.b7 - m.b8 + m.x574 >= 0)

m.c512 = Constraint(expr=   m.b8 - m.b9 + m.x575 >= 0)

m.c513 = Constraint(expr=   m.b10 - m.b11 + m.x576 >= 0)

m.c514 = Constraint(expr=   m.b11 - m.b12 + m.x577 >= 0)

m.c515 = Constraint(expr=   m.b12 - m.b13 + m.x578 >= 0)

m.c516 = Constraint(expr=   m.b14 - m.b15 + m.x579 >= 0)

m.c517 = Constraint(expr=   m.b15 - m.b16 + m.x580 >= 0)

m.c518 = Constraint(expr=   m.b16 - m.b17 + m.x581 >= 0)

m.c519 = Constraint(expr=   m.b18 - m.b19 + m.x582 >= 0)

m.c520 = Constraint(expr=   m.b19 - m.b20 + m.x583 >= 0)

m.c521 = Constraint(expr=   m.b20 - m.b21 + m.x584 >= 0)

m.c522 = Constraint(expr=   m.b22 - m.b23 + m.x585 >= 0)

m.c523 = Constraint(expr=   m.b23 - m.b24 + m.x586 >= 0)

m.c524 = Constraint(expr=   m.b24 - m.b25 + m.x587 >= 0)

m.c525 = Constraint(expr=   m.b26 - m.b27 + m.x588 >= 0)

m.c526 = Constraint(expr=   m.b27 - m.b28 + m.x589 >= 0)

m.c527 = Constraint(expr=   m.b28 - m.b29 + m.x590 >= 0)

m.c528 = Constraint(expr=   m.b30 - m.b31 + m.x591 >= 0)

m.c529 = Constraint(expr=   m.b31 - m.b32 + m.x592 >= 0)

m.c530 = Constraint(expr=   m.b32 - m.b33 + m.x593 >= 0)

m.c531 = Constraint(expr=   m.b34 - m.b35 + m.x594 >= 0)

m.c532 = Constraint(expr=   m.b35 - m.b36 + m.x595 >= 0)

m.c533 = Constraint(expr=   m.b36 - m.b37 + m.x596 >= 0)

m.c534 = Constraint(expr=   m.b38 - m.b39 + m.x597 >= 0)

m.c535 = Constraint(expr=   m.b39 - m.b40 + m.x598 >= 0)

m.c536 = Constraint(expr=   m.b40 - m.b41 + m.x599 >= 0)

m.c537 = Constraint(expr=   m.b42 - m.b43 + m.x600 >= 0)

m.c538 = Constraint(expr=   m.b43 - m.b44 + m.x601 >= 0)

m.c539 = Constraint(expr=   m.b44 - m.b45 + m.x602 >= 0)

m.c540 = Constraint(expr=   m.b46 - m.b47 + m.x603 >= 0)

m.c541 = Constraint(expr=   m.b47 - m.b48 + m.x604 >= 0)

m.c542 = Constraint(expr=   m.b48 - m.b49 + m.x605 >= 0)

m.c543 = Constraint(expr= - m.b2 + m.b3 + m.x570 >= 0)

m.c544 = Constraint(expr= - m.b3 + m.b4 + m.x571 >= 0)

m.c545 = Constraint(expr= - m.b4 + m.b5 + m.x572 >= 0)

m.c546 = Constraint(expr= - m.b6 + m.b7 + m.x573 >= 0)

m.c547 = Constraint(expr= - m.b7 + m.b8 + m.x574 >= 0)

m.c548 = Constraint(expr= - m.b8 + m.b9 + m.x575 >= 0)

m.c549 = Constraint(expr= - m.b10 + m.b11 + m.x576 >= 0)

m.c550 = Constraint(expr= - m.b11 + m.b12 + m.x577 >= 0)

m.c551 = Constraint(expr= - m.b12 + m.b13 + m.x578 >= 0)

m.c552 = Constraint(expr= - m.b14 + m.b15 + m.x579 >= 0)

m.c553 = Constraint(expr= - m.b15 + m.b16 + m.x580 >= 0)

m.c554 = Constraint(expr= - m.b16 + m.b17 + m.x581 >= 0)

m.c555 = Constraint(expr= - m.b18 + m.b19 + m.x582 >= 0)

m.c556 = Constraint(expr= - m.b19 + m.b20 + m.x583 >= 0)

m.c557 = Constraint(expr= - m.b20 + m.b21 + m.x584 >= 0)

m.c558 = Constraint(expr= - m.b22 + m.b23 + m.x585 >= 0)

m.c559 = Constraint(expr= - m.b23 + m.b24 + m.x586 >= 0)

m.c560 = Constraint(expr= - m.b24 + m.b25 + m.x587 >= 0)

m.c561 = Constraint(expr= - m.b26 + m.b27 + m.x588 >= 0)

m.c562 = Constraint(expr= - m.b27 + m.b28 + m.x589 >= 0)

m.c563 = Constraint(expr= - m.b28 + m.b29 + m.x590 >= 0)

m.c564 = Constraint(expr= - m.b30 + m.b31 + m.x591 >= 0)

m.c565 = Constraint(expr= - m.b31 + m.b32 + m.x592 >= 0)

m.c566 = Constraint(expr= - m.b32 + m.b33 + m.x593 >= 0)

m.c567 = Constraint(expr= - m.b34 + m.b35 + m.x594 >= 0)

m.c568 = Constraint(expr= - m.b35 + m.b36 + m.x595 >= 0)

m.c569 = Constraint(expr= - m.b36 + m.b37 + m.x596 >= 0)

m.c570 = Constraint(expr= - m.b38 + m.b39 + m.x597 >= 0)

m.c571 = Constraint(expr= - m.b39 + m.b40 + m.x598 >= 0)

m.c572 = Constraint(expr= - m.b40 + m.b41 + m.x599 >= 0)

m.c573 = Constraint(expr= - m.b42 + m.b43 + m.x600 >= 0)

m.c574 = Constraint(expr= - m.b43 + m.b44 + m.x601 >= 0)

m.c575 = Constraint(expr= - m.b44 + m.b45 + m.x602 >= 0)

m.c576 = Constraint(expr= - m.b46 + m.b47 + m.x603 >= 0)

m.c577 = Constraint(expr= - m.b47 + m.b48 + m.x604 >= 0)

m.c578 = Constraint(expr= - m.b48 + m.b49 + m.x605 >= 0)

m.c579 = Constraint(expr= - 5*m.b50 + m.x152 <= 0)

m.c580 = Constraint(expr= - 5*m.b51 + m.x155 <= 0)

m.c581 = Constraint(expr= - 5*m.b52 + m.x158 <= 0)

m.c582 = Constraint(expr= - 5*m.b53 + m.x161 <= 0)

m.c583 = Constraint(expr= - 5*m.b54 + m.x223 <= 0)

m.c584 = Constraint(expr= - 5*m.b55 + m.x225 <= 0)

m.c585 = Constraint(expr= - 5*m.b56 + m.x227 <= 0)

m.c586 = Constraint(expr= - 5*m.b57 + m.x229 <= 0)

m.c587 = Constraint(expr= - 5*m.b58 + m.x203 <= 0)

m.c588 = Constraint(expr= - 5*m.b59 + m.x205 <= 0)

m.c589 = Constraint(expr= - 5*m.b60 + m.x207 <= 0)

m.c590 = Constraint(expr= - 5*m.b61 + m.x209 <= 0)

m.c591 = Constraint(expr= - 1000*m.b50 + m.x430 - m.x478 >= -1000)

m.c592 = Constraint(expr= - 1000*m.b51 + m.x433 - m.x481 >= -1000)

m.c593 = Constraint(expr= - 1000*m.b52 + m.x436 - m.x484 >= -1000)

m.c594 = Constraint(expr= - 1000*m.b53 + m.x439 - m.x487 >= -1000)

m.c595 = Constraint(expr= - 1000*m.b54 + m.x518 - m.x542 >= -1000)

m.c596 = Constraint(expr= - 1000*m.b55 + m.x521 - m.x544 >= -1000)

m.c597 = Constraint(expr= - 1000*m.b56 + m.x524 - m.x546 >= -1000)

m.c598 = Constraint(expr= - 1000*m.b57 + m.x527 - m.x548 >= -1000)

m.c599 = Constraint(expr= - 1000*m.b58 + m.x479 - m.x490 >= -1000)

m.c600 = Constraint(expr= - 1000*m.b59 + m.x482 - m.x493 >= -1000)

m.c601 = Constraint(expr= - 1000*m.b60 + m.x485 - m.x496 >= -1000)

m.c602 = Constraint(expr= - 1000*m.b61 + m.x488 - m.x499 >= -1000)

m.c603 = Constraint(expr= - 1000*m.b50 + m.x430 - m.x478 <= 0)

m.c604 = Constraint(expr= - 1000*m.b51 + m.x433 - m.x481 <= 0)

m.c605 = Constraint(expr= - 1000*m.b52 + m.x436 - m.x484 <= 0)

m.c606 = Constraint(expr= - 1000*m.b53 + m.x439 - m.x487 <= 0)

m.c607 = Constraint(expr= - 1000*m.b54 + m.x518 - m.x542 <= 0)

m.c608 = Constraint(expr= - 1000*m.b55 + m.x521 - m.x544 <= 0)

m.c609 = Constraint(expr= - 1000*m.b56 + m.x524 - m.x546 <= 0)

m.c610 = Constraint(expr= - 1000*m.b57 + m.x527 - m.x548 <= 0)

m.c611 = Constraint(expr= - 1000*m.b58 + m.x479 - m.x490 <= 0)

m.c612 = Constraint(expr= - 1000*m.b59 + m.x482 - m.x493 <= 0)

m.c613 = Constraint(expr= - 1000*m.b60 + m.x485 - m.x496 <= 0)

m.c614 = Constraint(expr= - 1000*m.b61 + m.x488 - m.x499 <= 0)

m.c615 = Constraint(expr= - m.x378 + m.x478 >= 60)

m.c616 = Constraint(expr= - m.x379 + m.x481 >= 60)

m.c617 = Constraint(expr= - m.x380 + m.x484 >= 60)

m.c618 = Constraint(expr= - m.x381 + m.x487 >= 60)

m.c619 = Constraint(expr= - m.x382 + m.x478 >= 60)

m.c620 = Constraint(expr= - m.x383 + m.x481 >= 60)

m.c621 = Constraint(expr= - m.x384 + m.x484 >= 60)

m.c622 = Constraint(expr= - m.x385 + m.x487 >= 60)

m.c623 = Constraint(expr= - m.x386 + m.x530 >= 50)

m.c624 = Constraint(expr= - m.x387 + m.x532 >= 50)

m.c625 = Constraint(expr= - m.x388 + m.x534 >= 50)

m.c626 = Constraint(expr= - m.x389 + m.x536 >= 50)

m.c627 = Constraint(expr=60159.7666785*m.x278**2 - m.x281 == 0)

m.c628 = Constraint(expr=60159.7666785*m.x280**2 - m.x285 == 0)

m.c629 = Constraint(expr=60159.7666785*m.x282**2 - m.x289 == 0)

m.c630 = Constraint(expr=60159.7666785*m.x284**2 - m.x293 == 0)

m.c631 = Constraint(expr=16103.4266989*m.x286**2 - m.x299 == 0)

m.c632 = Constraint(expr=16103.4266989*m.x288**2 - m.x305 == 0)

m.c633 = Constraint(expr=16103.4266989*m.x290**2 - m.x311 == 0)

m.c634 = Constraint(expr=16103.4266989*m.x292**2 - m.x317 == 0)

m.c635 = Constraint(expr=16103.4266989*m.x294**2 - m.x323 == 0)

m.c636 = Constraint(expr=16103.4266989*m.x296**2 - m.x329 == 0)

m.c637 = Constraint(expr=16103.4266989*m.x298**2 - m.x335 == 0)

m.c638 = Constraint(expr=16103.4266989*m.x300**2 - m.x341 == 0)

m.c639 = Constraint(expr=16103.4266989*m.x302**2 - m.x347 == 0)

m.c640 = Constraint(expr=16103.4266989*m.x304**2 - m.x353 == 0)

m.c641 = Constraint(expr=16103.4266989*m.x306**2 - m.x359 == 0)

m.c642 = Constraint(expr=16103.4266989*m.x308**2 - m.x365 == 0)

m.c643 = Constraint(expr=16103.4266989*m.x310**2 - m.x371 == 0)

m.c644 = Constraint(expr=16103.4266989*m.x312**2 - m.x607 == 0)

m.c645 = Constraint(expr=16103.4266989*m.x314**2 - m.x610 == 0)

m.c646 = Constraint(expr=16103.4266989*m.x316**2 - m.x613 == 0)

m.c647 = Constraint(expr=16103.4266989*m.x318**2 - m.x616 == 0)

m.c648 = Constraint(expr=16103.4266989*m.x320**2 - m.x63 == 0)

m.c649 = Constraint(expr=16103.4266989*m.x322**2 - m.x66 == 0)

m.c650 = Constraint(expr=16103.4266989*m.x324**2 - m.x69 == 0)

m.c651 = Constraint(expr=16103.4266989*m.x326**2 - m.x72 == 0)

m.c652 = Constraint(expr=16103.4266989*m.x328**2 - m.x75 == 0)

m.c653 = Constraint(expr=16103.4266989*m.x330**2 - m.x78 == 0)

m.c654 = Constraint(expr=16103.4266989*m.x332**2 - m.x81 == 0)

m.c655 = Constraint(expr=60159.7666785*m.x334**2 - m.x83 == 0)

m.c656 = Constraint(expr=60159.7666785*m.x336**2 - m.x85 == 0)

m.c657 = Constraint(expr=60159.7666785*m.x338**2 - m.x87 == 0)

m.c658 = Constraint(expr=60159.7666785*m.x340**2 - m.x89 == 0)

m.c659 = Constraint(expr=2296.01902001*m.x342**2 - m.x91 == 0)

m.c660 = Constraint(expr=2296.01902001*m.x344**2 - m.x93 == 0)

m.c661 = Constraint(expr=2296.01902001*m.x346**2 - m.x95 == 0)

m.c662 = Constraint(expr=2296.01902001*m.x348**2 - m.x97 == 0)

m.c663 = Constraint(expr=2296.01902001*m.x350**2 - m.x99 == 0)

m.c664 = Constraint(expr=2296.01902001*m.x352**2 - m.x101 == 0)

m.c665 = Constraint(expr=2296.01902001*m.x354**2 - m.x103 == 0)

m.c666 = Constraint(expr=2296.01902001*m.x356**2 - m.x105 == 0)

m.c667 = Constraint(expr=2296.01902001*m.x358**2 - m.x107 == 0)

m.c668 = Constraint(expr=2296.01902001*m.x360**2 - m.x109 == 0)

m.c669 = Constraint(expr=2296.01902001*m.x362**2 - m.x111 == 0)

m.c670 = Constraint(expr=2296.01902001*m.x364**2 - m.x113 == 0)

m.c671 = Constraint(expr=6324.78464025*m.x366**2 - m.x115 == 0)

m.c672 = Constraint(expr=6324.78464025*m.x368**2 - m.x117 == 0)

m.c673 = Constraint(expr=6324.78464025*m.x370**2 - m.x119 == 0)

m.c674 = Constraint(expr=6324.78464025*m.x372**2 - m.x121 == 0)

m.c675 = Constraint(expr=2.4525*m.x278*m.x279 - m.x618 <= 0)

m.c676 = Constraint(expr=2.4525*m.x280*m.x283 - m.x619 <= 0)

m.c677 = Constraint(expr=2.4525*m.x282*m.x287 - m.x620 <= 0)

m.c678 = Constraint(expr=2.4525*m.x284*m.x291 - m.x621 <= 0)

m.c679 = Constraint(expr=2.4525*m.x286*m.x297 - m.x622 <= 0)

m.c680 = Constraint(expr=2.4525*m.x288*m.x303 - m.x623 <= 0)

m.c681 = Constraint(expr=2.4525*m.x290*m.x309 - m.x624 <= 0)

m.c682 = Constraint(expr=2.4525*m.x292*m.x315 - m.x625 <= 0)

m.c683 = Constraint(expr=2.4525*m.x294*m.x321 - m.x626 <= 0)

m.c684 = Constraint(expr=2.4525*m.x296*m.x327 - m.x627 <= 0)

m.c685 = Constraint(expr=2.4525*m.x298*m.x333 - m.x628 <= 0)

m.c686 = Constraint(expr=2.4525*m.x300*m.x339 - m.x629 <= 0)

m.c687 = Constraint(expr=2.4525*m.x302*m.x345 - m.x630 <= 0)

m.c688 = Constraint(expr=2.4525*m.x304*m.x351 - m.x631 <= 0)

m.c689 = Constraint(expr=2.4525*m.x306*m.x357 - m.x632 <= 0)

m.c690 = Constraint(expr=2.4525*m.x308*m.x363 - m.x633 <= 0)

m.c691 = Constraint(expr=2.4525*m.x310*m.x369 - m.x634 <= 0)

m.c692 = Constraint(expr=2.4525*m.x312*m.x606 - m.x635 <= 0)

m.c693 = Constraint(expr=2.4525*m.x314*m.x609 - m.x636 <= 0)

m.c694 = Constraint(expr=2.4525*m.x316*m.x612 - m.x637 <= 0)

m.c695 = Constraint(expr=2.4525*m.x318*m.x615 - m.x638 <= 0)

m.c696 = Constraint(expr=2.4525*m.x62*m.x320 - m.x639 <= 0)

m.c697 = Constraint(expr=2.4525*m.x65*m.x322 - m.x640 <= 0)

m.c698 = Constraint(expr=2.4525*m.x68*m.x324 - m.x641 <= 0)

m.c699 = Constraint(expr=2.4525*m.x71*m.x326 - m.x642 <= 0)

m.c700 = Constraint(expr=2.4525*m.x74*m.x328 - m.x643 <= 0)

m.c701 = Constraint(expr=2.4525*m.x77*m.x330 - m.x644 <= 0)

m.c702 = Constraint(expr=2.4525*m.x80*m.x332 - m.x645 <= 0)

m.c703 = Constraint(expr=2.4525*m.x82*m.x334 - m.x646 <= 0)

m.c704 = Constraint(expr=2.4525*m.x84*m.x336 - m.x647 <= 0)

m.c705 = Constraint(expr=2.4525*m.x86*m.x338 - m.x648 <= 0)

m.c706 = Constraint(expr=2.4525*m.x88*m.x340 - m.x649 <= 0)

m.c707 = Constraint(expr=2.4525*m.x90*m.x342 - m.x650 <= 0)

m.c708 = Constraint(expr=2.4525*m.x92*m.x344 - m.x651 <= 0)

m.c709 = Constraint(expr=2.4525*m.x94*m.x346 - m.x652 <= 0)

m.c710 = Constraint(expr=2.4525*m.x96*m.x348 - m.x653 <= 0)

m.c711 = Constraint(expr=2.4525*m.x98*m.x350 - m.x654 <= 0)

m.c712 = Constraint(expr=2.4525*m.x100*m.x352 - m.x655 <= 0)

m.c713 = Constraint(expr=2.4525*m.x102*m.x354 - m.x656 <= 0)

m.c714 = Constraint(expr=2.4525*m.x104*m.x356 - m.x657 <= 0)

m.c715 = Constraint(expr=2.4525*m.x106*m.x358 - m.x658 <= 0)

m.c716 = Constraint(expr=2.4525*m.x108*m.x360 - m.x659 <= 0)

m.c717 = Constraint(expr=2.4525*m.x110*m.x362 - m.x660 <= 0)

m.c718 = Constraint(expr=2.4525*m.x112*m.x364 - m.x661 <= 0)

m.c719 = Constraint(expr=2.4525*m.x114*m.x366 - m.x662 <= 0)

m.c720 = Constraint(expr=2.4525*m.x116*m.x368 - m.x663 <= 0)

m.c721 = Constraint(expr=2.4525*m.x118*m.x370 - m.x664 <= 0)

m.c722 = Constraint(expr=2.4525*m.x120*m.x372 - m.x665 <= 0)

m.c723 = Constraint(expr=SignPower(m.x122,2) - 0.107595782151047*m.x392 == 0)

m.c724 = Constraint(expr=SignPower(m.x124,2) - 0.107595782151047*m.x395 == 0)

m.c725 = Constraint(expr=SignPower(m.x126,2) - 0.107595782151047*m.x398 == 0)

m.c726 = Constraint(expr=SignPower(m.x128,2) - 0.107595782151047*m.x401 == 0)

m.c727 = Constraint(expr=SignPower(m.x130,2) - 0.000240846101592208*m.x403 == 0)

m.c728 = Constraint(expr=SignPower(m.x133,2) - 0.000240846101592208*m.x405 == 0)

m.c729 = Constraint(expr=SignPower(m.x136,2) - 0.000240846101592208*m.x407 == 0)

m.c730 = Constraint(expr=SignPower(m.x139,2) - 0.000240846101592208*m.x409 == 0)

m.c731 = Constraint(expr=SignPower(m.x132,2) - 0.0011039398274554*m.x411 == 0)

m.c732 = Constraint(expr=SignPower(m.x135,2) - 0.0011039398274554*m.x413 == 0)

m.c733 = Constraint(expr=SignPower(m.x138,2) - 0.0011039398274554*m.x415 == 0)

m.c734 = Constraint(expr=SignPower(m.x141,2) - 0.0011039398274554*m.x417 == 0)

m.c735 = Constraint(expr=SignPower(m.x170,2) - 0.0147658094299242*m.x420 == 0)

m.c736 = Constraint(expr=SignPower(m.x171,2) - 0.0147658094299242*m.x423 == 0)

m.c737 = Constraint(expr=SignPower(m.x172,2) - 0.0147658094299242*m.x426 == 0)

m.c738 = Constraint(expr=SignPower(m.x173,2) - 0.0147658094299242*m.x429 == 0)

m.c739 = Constraint(expr=SignPower(m.x151,2) - 0.0126524872624481*m.x432 == 0)

m.c740 = Constraint(expr=SignPower(m.x154,2) - 0.0126524872624481*m.x435 == 0)

m.c741 = Constraint(expr=SignPower(m.x157,2) - 0.0126524872624481*m.x438 == 0)

m.c742 = Constraint(expr=SignPower(m.x160,2) - 0.0126524872624481*m.x441 == 0)

m.c743 = Constraint(expr=SignPower(m.x150,2) - 0.000713164667292268*m.x442 == 0)

m.c744 = Constraint(expr=SignPower(m.x153,2) - 0.000713164667292268*m.x443 == 0)

m.c745 = Constraint(expr=SignPower(m.x156,2) - 0.000713164667292268*m.x444 == 0)

m.c746 = Constraint(expr=SignPower(m.x159,2) - 0.000713164667292268*m.x445 == 0)

m.c747 = Constraint(expr=SignPower(m.x131,2) - 0.0253049745248962*m.x446 == 0)

m.c748 = Constraint(expr=SignPower(m.x134,2) - 0.0253049745248962*m.x447 == 0)

m.c749 = Constraint(expr=SignPower(m.x137,2) - 0.0253049745248962*m.x448 == 0)

m.c750 = Constraint(expr=SignPower(m.x140,2) - 0.0253049745248962*m.x449 == 0)

m.c751 = Constraint(expr=SignPower(m.x194,2) - 0.0196735206566467*m.x450 == 0)

m.c752 = Constraint(expr=SignPower(m.x195,2) - 0.0196735206566467*m.x451 == 0)

m.c753 = Constraint(expr=SignPower(m.x196,2) - 0.0196735206566467*m.x452 == 0)

m.c754 = Constraint(expr=SignPower(m.x197,2) - 0.0196735206566467*m.x453 == 0)

m.c755 = Constraint(expr=SignPower(m.x162,2) - 0.13436247753087*m.x454 == 0)

m.c756 = Constraint(expr=SignPower(m.x164,2) - 0.13436247753087*m.x455 == 0)

m.c757 = Constraint(expr=SignPower(m.x166,2) - 0.13436247753087*m.x456 == 0)

m.c758 = Constraint(expr=SignPower(m.x168,2) - 0.13436247753087*m.x457 == 0)

m.c759 = Constraint(expr=SignPower(m.x163,2) - 0.13436247753087*m.x458 == 0)

m.c760 = Constraint(expr=SignPower(m.x165,2) - 0.13436247753087*m.x459 == 0)

m.c761 = Constraint(expr=SignPower(m.x167,2) - 0.13436247753087*m.x460 == 0)

m.c762 = Constraint(expr=SignPower(m.x169,2) - 0.13436247753087*m.x461 == 0)

m.c763 = Constraint(expr=SignPower(m.x142,2) - 0.00268724955062101*m.x463 == 0)

m.c764 = Constraint(expr=SignPower(m.x143,2) - 0.00268724955062101*m.x465 == 0)

m.c765 = Constraint(expr=SignPower(m.x144,2) - 0.00268724955062101*m.x467 == 0)

m.c766 = Constraint(expr=SignPower(m.x145,2) - 0.00268724955062101*m.x469 == 0)

m.c767 = Constraint(expr=SignPower(m.x146,2) - 0.00175817654162355*m.x471 == 0)

m.c768 = Constraint(expr=SignPower(m.x147,2) - 0.00175817654162355*m.x473 == 0)

m.c769 = Constraint(expr=SignPower(m.x148,2) - 0.00175817654162355*m.x475 == 0)

m.c770 = Constraint(expr=SignPower(m.x149,2) - 0.00175817654162355*m.x477 == 0)

m.c771 = Constraint(expr=SignPower(m.x174,2) - 0.0156579704750926*m.x480 == 0)

m.c772 = Constraint(expr=SignPower(m.x179,2) - 0.0156579704750926*m.x483 == 0)

m.c773 = Constraint(expr=SignPower(m.x184,2) - 0.0156579704750926*m.x486 == 0)

m.c774 = Constraint(expr=SignPower(m.x189,2) - 0.0156579704750926*m.x489 == 0)

m.c775 = Constraint(expr=SignPower(m.x198,2) - 0.4031634796292*m.x492 == 0)

m.c776 = Constraint(expr=SignPower(m.x199,2) - 0.4031634796292*m.x495 == 0)

m.c777 = Constraint(expr=SignPower(m.x200,2) - 0.4031634796292*m.x498 == 0)

m.c778 = Constraint(expr=SignPower(m.x201,2) - 0.4031634796292*m.x501 == 0)

m.c779 = Constraint(expr=SignPower(m.x202,2) - 0.4031634796292*m.x502 == 0)

m.c780 = Constraint(expr=SignPower(m.x204,2) - 0.4031634796292*m.x503 == 0)

m.c781 = Constraint(expr=SignPower(m.x206,2) - 0.4031634796292*m.x504 == 0)

m.c782 = Constraint(expr=SignPower(m.x208,2) - 0.4031634796292*m.x505 == 0)

m.c783 = Constraint(expr=SignPower(m.x210,2) - 8.06326959261651*m.x507 == 0)

m.c784 = Constraint(expr=SignPower(m.x213,2) - 8.06326959261651*m.x509 == 0)

m.c785 = Constraint(expr=SignPower(m.x216,2) - 8.06326959261651*m.x511 == 0)

m.c786 = Constraint(expr=SignPower(m.x219,2) - 8.06326959261651*m.x513 == 0)

m.c787 = Constraint(expr=SignPower(m.x211,2) - 8.06326959261651*m.x514 == 0)

m.c788 = Constraint(expr=SignPower(m.x214,2) - 8.06326959261651*m.x515 == 0)

m.c789 = Constraint(expr=SignPower(m.x217,2) - 8.06326959261651*m.x516 == 0)

m.c790 = Constraint(expr=SignPower(m.x220,2) - 8.06326959261651*m.x517 == 0)

m.c791 = Constraint(expr=SignPower(m.x222,2) - 0.000180519501834947*m.x520 == 0)

m.c792 = Constraint(expr=SignPower(m.x224,2) - 0.000180519501834947*m.x523 == 0)

m.c793 = Constraint(expr=SignPower(m.x226,2) - 0.000180519501834947*m.x526 == 0)

m.c794 = Constraint(expr=SignPower(m.x228,2) - 0.000180519501834947*m.x529 == 0)

m.c795 = Constraint(expr=SignPower(m.x175,2) - 0.000180519501834947*m.x531 == 0)

m.c796 = Constraint(expr=SignPower(m.x180,2) - 0.000180519501834947*m.x533 == 0)

m.c797 = Constraint(expr=SignPower(m.x185,2) - 0.000180519501834947*m.x535 == 0)

m.c798 = Constraint(expr=SignPower(m.x190,2) - 0.000180519501834947*m.x537 == 0)

m.c799 = Constraint(expr=SignPower(m.x230,2) - 0.013538962637621*m.x538 == 0)

m.c800 = Constraint(expr=SignPower(m.x231,2) - 0.013538962637621*m.x539 == 0)

m.c801 = Constraint(expr=SignPower(m.x232,2) - 0.013538962637621*m.x540 == 0)

m.c802 = Constraint(expr=SignPower(m.x233,2) - 0.013538962637621*m.x541 == 0)

m.c803 = Constraint(expr=SignPower(m.x176,2) - 0.0463936827608069*m.x543 == 0)

m.c804 = Constraint(expr=SignPower(m.x181,2) - 0.0463936827608069*m.x545 == 0)

m.c805 = Constraint(expr=SignPower(m.x186,2) - 0.0463936827608069*m.x547 == 0)

m.c806 = Constraint(expr=SignPower(m.x191,2) - 0.0463936827608069*m.x549 == 0)

m.c807 = Constraint(expr=SignPower(m.x238,2) - 0.0964450219247959*m.x551 == 0)

m.c808 = Constraint(expr=SignPower(m.x239,2) - 0.0964450219247959*m.x553 == 0)

m.c809 = Constraint(expr=SignPower(m.x240,2) - 0.0964450219247959*m.x555 == 0)

m.c810 = Constraint(expr=SignPower(m.x241,2) - 0.0964450219247959*m.x557 == 0)
