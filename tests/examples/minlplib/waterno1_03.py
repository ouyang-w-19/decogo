#  MINLP written by GAMS Convert at 04/21/18 13:55:15
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        601      312      163      126        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        496      451       45        0        0        0        0        0
#  FX      7        7        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1618     1444      174        0
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
m.x47 = Var(within=Reals,bounds=(0.8,1.2),initialize=0.8)
m.x48 = Var(within=Reals,bounds=(148.299332771269,638.10455381568),initialize=148.299332771269)
m.x49 = Var(within=Reals,bounds=(0,135.302691146811),initialize=0)
m.x50 = Var(within=Reals,bounds=(0.8,1.2),initialize=0.8)
m.x51 = Var(within=Reals,bounds=(148.299332771269,638.10455381568),initialize=148.299332771269)
m.x52 = Var(within=Reals,bounds=(0,135.302691146811),initialize=0)
m.x53 = Var(within=Reals,bounds=(0.8,1.2),initialize=0.8)
m.x54 = Var(within=Reals,bounds=(148.299332771269,638.10455381568),initialize=148.299332771269)
m.x55 = Var(within=Reals,bounds=(0,135.302691146811),initialize=0)
m.x56 = Var(within=Reals,bounds=(0.8,1.2),initialize=0.8)
m.x57 = Var(within=Reals,bounds=(148.299332771269,638.10455381568),initialize=148.299332771269)
m.x58 = Var(within=Reals,bounds=(0,135.302691146811),initialize=0)
m.x59 = Var(within=Reals,bounds=(0.8,1.2),initialize=0.8)
m.x60 = Var(within=Reals,bounds=(148.299332771269,638.10455381568),initialize=148.299332771269)
m.x61 = Var(within=Reals,bounds=(0,135.302691146811),initialize=0)
m.x62 = Var(within=Reals,bounds=(287.427397827187,413.764247971),initialize=287.427397827187)
m.x63 = Var(within=Reals,bounds=(0,126.336850143813),initialize=0)
m.x64 = Var(within=Reals,bounds=(287.427397827187,413.764247971),initialize=287.427397827187)
m.x65 = Var(within=Reals,bounds=(0,126.336850143813),initialize=0)
m.x66 = Var(within=Reals,bounds=(287.427397827187,413.764247971),initialize=287.427397827187)
m.x67 = Var(within=Reals,bounds=(0,126.336850143813),initialize=0)
m.x68 = Var(within=Reals,bounds=(74.1748123438468,106.777870451),initialize=74.1748123438468)
m.x69 = Var(within=Reals,bounds=(0,32.6030581071532),initialize=0)
m.x70 = Var(within=Reals,bounds=(74.1748123438468,106.777870451),initialize=74.1748123438468)
m.x71 = Var(within=Reals,bounds=(0,32.6030581071532),initialize=0)
m.x72 = Var(within=Reals,bounds=(74.1748123438468,106.777870451),initialize=74.1748123438468)
m.x73 = Var(within=Reals,bounds=(0,32.6030581071532),initialize=0)
m.x74 = Var(within=Reals,bounds=(74.1748123438468,106.777870451),initialize=74.1748123438468)
m.x75 = Var(within=Reals,bounds=(0,32.6030581071532),initialize=0)
m.x76 = Var(within=Reals,bounds=(74.1748123438468,106.777870451),initialize=74.1748123438468)
m.x77 = Var(within=Reals,bounds=(0,32.6030581071532),initialize=0)
m.x78 = Var(within=Reals,bounds=(74.1748123438468,106.777870451),initialize=74.1748123438468)
m.x79 = Var(within=Reals,bounds=(0,32.6030581071532),initialize=0)
m.x80 = Var(within=Reals,bounds=(74.1748123438468,106.777870451),initialize=74.1748123438468)
m.x81 = Var(within=Reals,bounds=(0,32.6030581071532),initialize=0)
m.x82 = Var(within=Reals,bounds=(74.1748123438468,106.777870451),initialize=74.1748123438468)
m.x83 = Var(within=Reals,bounds=(0,32.6030581071532),initialize=0)
m.x84 = Var(within=Reals,bounds=(74.1748123438468,106.777870451),initialize=74.1748123438468)
m.x85 = Var(within=Reals,bounds=(0,32.6030581071532),initialize=0)
m.x86 = Var(within=Reals,bounds=(74.1748123434975,106.777870452),initialize=74.1748123434975)
m.x87 = Var(within=Reals,bounds=(0,32.6030581085025),initialize=0)
m.x88 = Var(within=Reals,bounds=(74.1748123434975,106.777870452),initialize=74.1748123434975)
m.x89 = Var(within=Reals,bounds=(0,32.6030581085025),initialize=0)
m.x90 = Var(within=Reals,bounds=(74.1748123434975,106.777870452),initialize=74.1748123434975)
m.x91 = Var(within=Reals,bounds=(0,32.6030581085025),initialize=0)
m.x92 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x93 = Var(within=Reals,bounds=(0,0.64163),initialize=0)
m.x94 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x95 = Var(within=Reals,bounds=(0,0.64163),initialize=0)
m.x96 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x97 = Var(within=Reals,bounds=(0,0.64163),initialize=0)
m.x98 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x99 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x100 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x101 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x102 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x103 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x104 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x105 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x106 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x107 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x108 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x109 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x110 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x111 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x112 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x113 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x114 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x115 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x116 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x117 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x118 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x119 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x120 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x121 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x122 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x123 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x124 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x125 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x126 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x127 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x128 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x129 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x130 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x131 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x132 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x133 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x134 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x135 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x136 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x137 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x138 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x139 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x140 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x141 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x142 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x143 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x144 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x145 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x146 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x147 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x148 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x149 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x150 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x151 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x152 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x153 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x154 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x155 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x156 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x157 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x158 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x159 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x160 = Var(within=Reals,bounds=(0,0.429286),initialize=0)
m.x161 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x162 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x163 = Var(within=Reals,bounds=(0,0.429286),initialize=0)
m.x164 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x165 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x166 = Var(within=Reals,bounds=(0,0.429286),initialize=0)
m.x167 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x168 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x169 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x170 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x171 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x172 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x173 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x174 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x175 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x176 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x177 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x178 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x179 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x180 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x181 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x182 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x183 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x184 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x185 = Var(within=Reals,bounds=(6.3,6.3),initialize=6.3)
m.x186 = Var(within=Reals,bounds=(5,10),initialize=5)
m.x187 = Var(within=Reals,bounds=(5,10),initialize=5)
m.x188 = Var(within=Reals,bounds=(5,10),initialize=5)
m.x189 = Var(within=Reals,bounds=(5,10),initialize=5)
m.x190 = Var(within=Reals,bounds=(5,10),initialize=5)
m.x191 = Var(within=Reals,bounds=(4.6,4.6),initialize=4.6)
m.x192 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x193 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x194 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x195 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x196 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x197 = Var(within=Reals,bounds=(4.6,4.6),initialize=4.6)
m.x198 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x199 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x200 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x201 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x202 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x203 = Var(within=Reals,bounds=(10,10),initialize=10)
m.x204 = Var(within=Reals,bounds=(0,16.5),initialize=0)
m.x205 = Var(within=Reals,bounds=(0,16.5),initialize=0)
m.x206 = Var(within=Reals,bounds=(0,16.5),initialize=0)
m.x207 = Var(within=Reals,bounds=(0,16.5),initialize=0)
m.x208 = Var(within=Reals,bounds=(0,16.5),initialize=0)
m.x209 = Var(within=Reals,bounds=(0,0.045826),initialize=0)
m.x210 = Var(within=Reals,bounds=(287.427397827187,413.764247971),initialize=287.427397827187)
m.x211 = Var(within=Reals,bounds=(0,0.045826),initialize=0)
m.x212 = Var(within=Reals,bounds=(0,126.336850143813),initialize=0)
m.x213 = Var(within=Reals,bounds=(0,0.045826),initialize=0)
m.x214 = Var(within=Reals,bounds=(287.427397827187,413.764247971),initialize=287.427397827187)
m.x215 = Var(within=Reals,bounds=(0,0.091663),initialize=0)
m.x216 = Var(within=Reals,bounds=(0,126.336850143813),initialize=0)
m.x217 = Var(within=Reals,bounds=(0,0.091663),initialize=0)
m.x218 = Var(within=Reals,bounds=(287.427397827187,413.764247971),initialize=287.427397827187)
m.x219 = Var(within=Reals,bounds=(0,0.091663),initialize=0)
m.x220 = Var(within=Reals,bounds=(0,126.336850143813),initialize=0)
m.x221 = Var(within=Reals,bounds=(0,0.091663),initialize=0)
m.x222 = Var(within=Reals,bounds=(0.8,1.2),initialize=0.8)
m.x223 = Var(within=Reals,bounds=(0,0.091663),initialize=0)
m.x224 = Var(within=Reals,bounds=(148.299332771269,638.10455381568),initialize=148.299332771269)
m.x225 = Var(within=Reals,bounds=(0,0.091663),initialize=0)
m.x226 = Var(within=Reals,bounds=(0,135.302691146811),initialize=0)
m.x227 = Var(within=Reals,bounds=(0,0.091663),initialize=0)
m.x228 = Var(within=Reals,bounds=(0.8,1.2),initialize=0.8)
m.x229 = Var(within=Reals,bounds=(0,0.091663),initialize=0)
m.x230 = Var(within=Reals,bounds=(148.299332771269,638.10455381568),initialize=148.299332771269)
m.x231 = Var(within=Reals,bounds=(0,0.091663),initialize=0)
m.x232 = Var(within=Reals,bounds=(0,135.302691146811),initialize=0)
m.x233 = Var(within=Reals,bounds=(0,0.091663),initialize=0)
m.x234 = Var(within=Reals,bounds=(0.8,1.2),initialize=0.8)
m.x235 = Var(within=Reals,bounds=(0,0.091663),initialize=0)
m.x236 = Var(within=Reals,bounds=(148.299332771269,638.10455381568),initialize=148.299332771269)
m.x237 = Var(within=Reals,bounds=(0,0.091663),initialize=0)
m.x238 = Var(within=Reals,bounds=(0,135.302691146811),initialize=0)
m.x239 = Var(within=Reals,bounds=(0,0.091663),initialize=0)
m.x240 = Var(within=Reals,bounds=(0.8,1.2),initialize=0.8)
m.x241 = Var(within=Reals,bounds=(0,0.091663),initialize=0)
m.x242 = Var(within=Reals,bounds=(148.299332771269,638.10455381568),initialize=148.299332771269)
m.x243 = Var(within=Reals,bounds=(0,0.091663),initialize=0)
m.x244 = Var(within=Reals,bounds=(0,135.302691146811),initialize=0)
m.x245 = Var(within=Reals,bounds=(0,0.091663),initialize=0)
m.x246 = Var(within=Reals,bounds=(0.8,1.2),initialize=0.8)
m.x247 = Var(within=Reals,bounds=(0,0.091663),initialize=0)
m.x248 = Var(within=Reals,bounds=(148.299332771269,638.10455381568),initialize=148.299332771269)
m.x249 = Var(within=Reals,bounds=(0,0.091663),initialize=0)
m.x250 = Var(within=Reals,bounds=(0,135.302691146811),initialize=0)
m.x251 = Var(within=Reals,bounds=(0,0.045826),initialize=0)
m.x252 = Var(within=Reals,bounds=(0.8,1.2),initialize=0.8)
m.x253 = Var(within=Reals,bounds=(0,0.045826),initialize=0)
m.x254 = Var(within=Reals,bounds=(148.299332771269,638.10455381568),initialize=148.299332771269)
m.x255 = Var(within=Reals,bounds=(0,0.045826),initialize=0)
m.x256 = Var(within=Reals,bounds=(0,135.302691146811),initialize=0)
m.x257 = Var(within=Reals,bounds=(0,0.119163),initialize=0)
m.x258 = Var(within=Reals,bounds=(0.8,1.2),initialize=0.8)
m.x259 = Var(within=Reals,bounds=(0,0.119163),initialize=0)
m.x260 = Var(within=Reals,bounds=(148.299332771269,638.10455381568),initialize=148.299332771269)
m.x261 = Var(within=Reals,bounds=(0,0.119163),initialize=0)
m.x262 = Var(within=Reals,bounds=(0,135.302691146811),initialize=0)
m.x263 = Var(within=Reals,bounds=(0,0.119163),initialize=0)
m.x264 = Var(within=Reals,bounds=(0.8,1.2),initialize=0.8)
m.x265 = Var(within=Reals,bounds=(0,0.119163),initialize=0)
m.x266 = Var(within=Reals,bounds=(148.299332771269,638.10455381568),initialize=148.299332771269)
m.x267 = Var(within=Reals,bounds=(0,0.119163),initialize=0)
m.x268 = Var(within=Reals,bounds=(0,135.302691146811),initialize=0)
m.x269 = Var(within=Reals,bounds=(0,0.119163),initialize=0)
m.x270 = Var(within=Reals,bounds=(0.8,1.2),initialize=0.8)
m.x271 = Var(within=Reals,bounds=(0,0.119163),initialize=0)
m.x272 = Var(within=Reals,bounds=(148.299332771269,638.10455381568),initialize=148.299332771269)
m.x273 = Var(within=Reals,bounds=(0,0.119163),initialize=0)
m.x274 = Var(within=Reals,bounds=(0,135.302691146811),initialize=0)
m.x275 = Var(within=Reals,bounds=(0,0.071797),initialize=0)
m.x276 = Var(within=Reals,bounds=(0.8,1.2),initialize=0.8)
m.x277 = Var(within=Reals,bounds=(0,0.071797),initialize=0)
m.x278 = Var(within=Reals,bounds=(148.299332771269,638.10455381568),initialize=148.299332771269)
m.x279 = Var(within=Reals,bounds=(0,0.071797),initialize=0)
m.x280 = Var(within=Reals,bounds=(0,135.302691146811),initialize=0)
m.x281 = Var(within=Reals,bounds=(305,310),initialize=305)
m.x282 = Var(within=Reals,bounds=(305,310),initialize=305)
m.x283 = Var(within=Reals,bounds=(305,310),initialize=305)
m.x284 = Var(within=Reals,bounds=(240,246),initialize=240)
m.x285 = Var(within=Reals,bounds=(240,246),initialize=240)
m.x286 = Var(within=Reals,bounds=(240,246),initialize=240)
m.x287 = Var(within=Reals,bounds=(240,246),initialize=240)
m.x288 = Var(within=Reals,bounds=(240,246),initialize=240)
m.x289 = Var(within=Reals,bounds=(240,246),initialize=240)
m.x290 = Var(within=Reals,bounds=(243,259.5),initialize=243)
m.x291 = Var(within=Reals,bounds=(243,259.5),initialize=243)
m.x292 = Var(within=Reals,bounds=(243,259.5),initialize=243)
m.x293 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x294 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x295 = Var(within=Reals,bounds=(-232.35111544525,232.35111544525),initialize=0)
m.x296 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x297 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x298 = Var(within=Reals,bounds=(-232.35111544525,232.35111544525),initialize=0)
m.x299 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x300 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x301 = Var(within=Reals,bounds=(-232.35111544525,232.35111544525),initialize=0)
m.x302 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x303 = Var(within=Reals,bounds=(-103800.7251715,103800.7251715),initialize=0)
m.x304 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x305 = Var(within=Reals,bounds=(-103800.7251715,103800.7251715),initialize=0)
m.x306 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x307 = Var(within=Reals,bounds=(-103800.7251715,103800.7251715),initialize=0)
m.x308 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x309 = Var(within=Reals,bounds=(-22646.161845275,22646.161845275),initialize=0)
m.x310 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x311 = Var(within=Reals,bounds=(-22646.161845275,22646.161845275),initialize=0)
m.x312 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x313 = Var(within=Reals,bounds=(-22646.161845275,22646.161845275),initialize=0)
m.x314 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x315 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x316 = Var(within=Reals,bounds=(-1693.1005454625,1693.1005454625),initialize=0)
m.x317 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x318 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x319 = Var(within=Reals,bounds=(-1693.1005454625,1693.1005454625),initialize=0)
m.x320 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x321 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x322 = Var(within=Reals,bounds=(-1693.1005454625,1693.1005454625),initialize=0)
m.x323 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x324 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x325 = Var(within=Reals,bounds=(-1975.896081255,1975.896081255),initialize=0)
m.x326 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x327 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x328 = Var(within=Reals,bounds=(-1975.896081255,1975.896081255),initialize=0)
m.x329 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x330 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x331 = Var(within=Reals,bounds=(-1975.896081255,1975.896081255),initialize=0)
m.x332 = Var(within=Reals,bounds=(-35055.017651,35055.017651),initialize=0)
m.x333 = Var(within=Reals,bounds=(-35055.017651,35055.017651),initialize=0)
m.x334 = Var(within=Reals,bounds=(-35055.017651,35055.017651),initialize=0)
m.x335 = Var(within=Reals,bounds=(-987.9480406275,987.9480406275),initialize=0)
m.x336 = Var(within=Reals,bounds=(-987.9480406275,987.9480406275),initialize=0)
m.x337 = Var(within=Reals,bounds=(-987.9480406275,987.9480406275),initialize=0)
m.x338 = Var(within=Reals,bounds=(-1270.74357642,1270.74357642),initialize=0)
m.x339 = Var(within=Reals,bounds=(-1270.74357642,1270.74357642),initialize=0)
m.x340 = Var(within=Reals,bounds=(-1270.74357642,1270.74357642),initialize=0)
m.x341 = Var(within=Reals,bounds=(-186.06385100525,186.06385100525),initialize=0)
m.x342 = Var(within=Reals,bounds=(-186.06385100525,186.06385100525),initialize=0)
m.x343 = Var(within=Reals,bounds=(-186.06385100525,186.06385100525),initialize=0)
m.x344 = Var(within=Reals,bounds=(-186.06385100525,186.06385100525),initialize=0)
m.x345 = Var(within=Reals,bounds=(-186.06385100525,186.06385100525),initialize=0)
m.x346 = Var(within=Reals,bounds=(-186.06385100525,186.06385100525),initialize=0)
m.x347 = Var(within=Reals,bounds=(214.9,1000),initialize=214.9)
m.x348 = Var(within=Reals,bounds=(-9303.19255025,9303.19255025),initialize=0)
m.x349 = Var(within=Reals,bounds=(214.9,1000),initialize=214.9)
m.x350 = Var(within=Reals,bounds=(-9303.19255025,9303.19255025),initialize=0)
m.x351 = Var(within=Reals,bounds=(214.9,1000),initialize=214.9)
m.x352 = Var(within=Reals,bounds=(-9303.19255025,9303.19255025),initialize=0)
m.x353 = Var(within=Reals,bounds=(231.04,1000),initialize=231.04)
m.x354 = Var(within=Reals,bounds=(-14219.27742075,14219.27742075),initialize=0)
m.x355 = Var(within=Reals,bounds=(231.04,1000),initialize=231.04)
m.x356 = Var(within=Reals,bounds=(-14219.27742075,14219.27742075),initialize=0)
m.x357 = Var(within=Reals,bounds=(231.04,1000),initialize=231.04)
m.x358 = Var(within=Reals,bounds=(-14219.27742075,14219.27742075),initialize=0)
m.x359 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x360 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x361 = Var(within=Reals,bounds=(-1596.630932455,1596.630932455),initialize=0)
m.x362 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x363 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x364 = Var(within=Reals,bounds=(-1596.630932455,1596.630932455),initialize=0)
m.x365 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x366 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x367 = Var(within=Reals,bounds=(-1596.630932455,1596.630932455),initialize=0)
m.x368 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x369 = Var(within=Reals,bounds=(300,1000),initialize=300)
m.x370 = Var(within=Reals,bounds=(-62.00958485375,62.00958485375),initialize=0)
m.x371 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x372 = Var(within=Reals,bounds=(300,1000),initialize=300)
m.x373 = Var(within=Reals,bounds=(-62.00958485375,62.00958485375),initialize=0)
m.x374 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x375 = Var(within=Reals,bounds=(300,1000),initialize=300)
m.x376 = Var(within=Reals,bounds=(-62.00958485375,62.00958485375),initialize=0)
m.x377 = Var(within=Reals,bounds=(-62.00958485375,62.00958485375),initialize=0)
m.x378 = Var(within=Reals,bounds=(-62.00958485375,62.00958485375),initialize=0)
m.x379 = Var(within=Reals,bounds=(-62.00958485375,62.00958485375),initialize=0)
m.x380 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x381 = Var(within=Reals,bounds=(-3.100479242675,3.100479242675),initialize=0)
m.x382 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x383 = Var(within=Reals,bounds=(-3.100479242675,3.100479242675),initialize=0)
m.x384 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x385 = Var(within=Reals,bounds=(-3.100479242675,3.100479242675),initialize=0)
m.x386 = Var(within=Reals,bounds=(-3.100479242675,3.100479242675),initialize=0)
m.x387 = Var(within=Reals,bounds=(-3.100479242675,3.100479242675),initialize=0)
m.x388 = Var(within=Reals,bounds=(-3.100479242675,3.100479242675),initialize=0)
m.x389 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x390 = Var(within=Reals,bounds=(243,1000),initialize=243)
m.x391 = Var(within=Reals,bounds=(-138489.1922805,138489.1922805),initialize=0)
m.x392 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x393 = Var(within=Reals,bounds=(243,1000),initialize=243)
m.x394 = Var(within=Reals,bounds=(-138489.1922805,138489.1922805),initialize=0)
m.x395 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x396 = Var(within=Reals,bounds=(243,1000),initialize=243)
m.x397 = Var(within=Reals,bounds=(-138489.1922805,138489.1922805),initialize=0)
m.x398 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x399 = Var(within=Reals,bounds=(-138489.1922805,138489.1922805),initialize=0)
m.x400 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x401 = Var(within=Reals,bounds=(-138489.1922805,138489.1922805),initialize=0)
m.x402 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x403 = Var(within=Reals,bounds=(-138489.1922805,138489.1922805),initialize=0)
m.x404 = Var(within=Reals,bounds=(-1846.52256374,1846.52256374),initialize=0)
m.x405 = Var(within=Reals,bounds=(-1846.52256374,1846.52256374),initialize=0)
m.x406 = Var(within=Reals,bounds=(-1846.52256374,1846.52256374),initialize=0)
m.x407 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x408 = Var(within=Reals,bounds=(-538.866468715,538.866468715),initialize=0)
m.x409 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x410 = Var(within=Reals,bounds=(-538.866468715,538.866468715),initialize=0)
m.x411 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x412 = Var(within=Reals,bounds=(-538.866468715,538.866468715),initialize=0)
m.x413 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x414 = Var(within=Reals,bounds=(-259.21503776,259.21503776),initialize=0)
m.x415 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x416 = Var(within=Reals,bounds=(-259.21503776,259.21503776),initialize=0)
m.x417 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x418 = Var(within=Reals,bounds=(-259.21503776,259.21503776),initialize=0)
m.x419 = Var(within=Reals,bounds=(34.1,34.1),initialize=34.1)
m.x420 = Var(within=Reals,bounds=(-34.1,1000),initialize=0)
m.x421 = Var(within=Reals,bounds=(34.1,34.1),initialize=34.1)
m.x422 = Var(within=Reals,bounds=(-34.1,1000),initialize=0)
m.x423 = Var(within=Reals,bounds=(34.1,34.1),initialize=34.1)
m.x424 = Var(within=Reals,bounds=(-34.1,1000),initialize=0)
m.x425 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x426 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x427 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x428 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x429 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x430 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x431 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x432 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x433 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x434 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x435 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x436 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x437 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x438 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x439 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x440 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x441 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x442 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x443 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x444 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x445 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x446 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x447 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x448 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x449 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x450 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x451 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x452 = Var(within=Reals,bounds=(0.8,1.2),initialize=0.8)
m.x453 = Var(within=Reals,bounds=(148.299332771269,638.10455381568),initialize=148.299332771269)
m.x454 = Var(within=Reals,bounds=(0,135.302691146811),initialize=0)
m.x455 = Var(within=Reals,bounds=(0.8,1.2),initialize=0.8)
m.x456 = Var(within=Reals,bounds=(148.299332771269,638.10455381568),initialize=148.299332771269)
m.x457 = Var(within=Reals,bounds=(0,135.302691146811),initialize=0)
m.x458 = Var(within=Reals,bounds=(0.8,1.2),initialize=0.8)
m.x459 = Var(within=Reals,bounds=(148.299332771269,638.10455381568),initialize=148.299332771269)
m.x460 = Var(within=Reals,bounds=(0,135.302691146811),initialize=0)
m.x461 = Var(within=Reals,bounds=(0,46.5022459484905),initialize=0)
m.x462 = Var(within=Reals,bounds=(0,46.5022459484905),initialize=0)
m.x463 = Var(within=Reals,bounds=(0,46.5022459484905),initialize=0)
m.x464 = Var(within=Reals,bounds=(0,143.448141849487),initialize=0)
m.x465 = Var(within=Reals,bounds=(0,143.448141849487),initialize=0)
m.x466 = Var(within=Reals,bounds=(0,143.448141849487),initialize=0)
m.x467 = Var(within=Reals,bounds=(0,143.448141849487),initialize=0)
m.x468 = Var(within=Reals,bounds=(0,143.448141849487),initialize=0)
m.x469 = Var(within=Reals,bounds=(0,143.448141849487),initialize=0)
m.x470 = Var(within=Reals,bounds=(0,143.448141849487),initialize=0)
m.x471 = Var(within=Reals,bounds=(0,143.448141849487),initialize=0)
m.x472 = Var(within=Reals,bounds=(0,143.448141849487),initialize=0)
m.x473 = Var(within=Reals,bounds=(0,143.448141849487),initialize=0)
m.x474 = Var(within=Reals,bounds=(0,143.448141849487),initialize=0)
m.x475 = Var(within=Reals,bounds=(0,143.448141849487),initialize=0)
m.x476 = Var(within=Reals,bounds=(0,143.448141849487),initialize=0)
m.x477 = Var(within=Reals,bounds=(0,143.448141849487),initialize=0)
m.x478 = Var(within=Reals,bounds=(0,143.448141849487),initialize=0)
m.x479 = Var(within=Reals,bounds=(0,143.448141849487),initialize=0)
m.x480 = Var(within=Reals,bounds=(0,143.448141849487),initialize=0)
m.x481 = Var(within=Reals,bounds=(0,143.448141849487),initialize=0)
m.x482 = Var(within=Reals,bounds=(0,46.5022459484905),initialize=0)
m.x483 = Var(within=Reals,bounds=(0,46.5022459484905),initialize=0)
m.x484 = Var(within=Reals,bounds=(0,46.5022459484905),initialize=0)
m.x485 = Var(within=Reals,bounds=(0,31.205539800995),initialize=0)
m.x486 = Var(within=Reals,bounds=(0,31.205539800995),initialize=0)
m.x487 = Var(within=Reals,bounds=(0,31.205539800995),initialize=0)
m.x488 = Var(within=Reals,bounds=(0,31.205539800995),initialize=0)
m.x489 = Var(within=Reals,bounds=(0,31.205539800995),initialize=0)
m.x490 = Var(within=Reals,bounds=(0,31.205539800995),initialize=0)
m.x491 = Var(within=Reals,bounds=(0,31.205539800995),initialize=0)
m.x492 = Var(within=Reals,bounds=(0,31.205539800995),initialize=0)
m.x493 = Var(within=Reals,bounds=(0,31.205539800995),initialize=0)
m.x494 = Var(within=Reals,bounds=(0,18.8016762007756),initialize=0)
m.x495 = Var(within=Reals,bounds=(0,18.8016762007756),initialize=0)
m.x496 = Var(within=Reals,bounds=(0,18.8016762007756),initialize=0)

m.obj = Objective(expr=   20*m.x428 + 20*m.x429 + 20*m.x430 + 20*m.x431 + 20*m.x432 + 20*m.x433 + 20*m.x434 + 20*m.x435
                        + 20*m.x436 + 20*m.x437 + 20*m.x438 + 20*m.x439 + 20*m.x440 + 20*m.x441 + 20*m.x442 + 20*m.x443
                        + 20*m.x444 + 20*m.x445 + 20*m.x446 + 20*m.x447 + 20*m.x448 + 20*m.x449 + 20*m.x450 + 20*m.x451
                        + m.x461 + m.x462 + m.x463 + m.x464 + m.x465 + m.x466 + m.x467 + m.x468 + m.x469 + m.x470
                        + m.x471 + m.x472 + m.x473 + m.x474 + m.x475 + m.x476 + m.x477 + m.x478 + m.x479 + m.x480
                        + m.x481 + m.x482 + m.x483 + m.x484 + m.x485 + m.x486 + m.x487 + m.x488 + m.x489 + m.x490
                        + m.x491 + m.x492 + m.x493 + m.x494 + m.x495 + m.x496, sense=minimize)

m.c2 = Constraint(expr=   m.x210 + m.x212 == 413.764247971)

m.c3 = Constraint(expr=   m.x214 + m.x216 == 413.764247971)

m.c4 = Constraint(expr=   m.x218 + m.x220 == 413.764247971)

m.c5 = Constraint(expr= - 443.128162372*m.x222 + m.x224 + m.x226 == 0)

m.c6 = Constraint(expr= - 443.128162372*m.x228 + m.x230 + m.x232 == 0)

m.c7 = Constraint(expr= - 443.128162372*m.x234 + m.x236 + m.x238 == 0)

m.c8 = Constraint(expr= - 443.128162372*m.x240 + m.x242 + m.x244 == 0)

m.c9 = Constraint(expr= - 443.128162372*m.x246 + m.x248 + m.x250 == 0)

m.c10 = Constraint(expr= - 443.128162372*m.x252 + m.x254 + m.x256 == 0)

m.c11 = Constraint(expr= - 443.128162372*m.x258 + m.x260 + m.x262 == 0)

m.c12 = Constraint(expr= - 443.128162372*m.x264 + m.x266 + m.x268 == 0)

m.c13 = Constraint(expr= - 443.128162372*m.x270 + m.x272 + m.x274 == 0)

m.c14 = Constraint(expr= - 443.128162372*m.x276 + m.x278 + m.x280 == 0)

m.c15 = Constraint(expr= - 443.128162372*m.x452 + m.x453 + m.x454 == 0)

m.c16 = Constraint(expr= - 443.128162372*m.x455 + m.x456 + m.x457 == 0)

m.c17 = Constraint(expr= - 443.128162372*m.x458 + m.x459 + m.x460 == 0)

m.c18 = Constraint(expr= - 443.128162372*m.x47 + m.x48 + m.x49 == 0)

m.c19 = Constraint(expr= - 443.128162372*m.x50 + m.x51 + m.x52 == 0)

m.c20 = Constraint(expr= - 443.128162372*m.x53 + m.x54 + m.x55 == 0)

m.c21 = Constraint(expr= - 443.128162372*m.x56 + m.x57 + m.x58 == 0)

m.c22 = Constraint(expr= - 443.128162372*m.x59 + m.x60 + m.x61 == 0)

m.c23 = Constraint(expr=   m.x62 + m.x63 == 413.764247971)

m.c24 = Constraint(expr=   m.x64 + m.x65 == 413.764247971)

m.c25 = Constraint(expr=   m.x66 + m.x67 == 413.764247971)

m.c26 = Constraint(expr=   m.x68 + m.x69 == 106.777870451)

m.c27 = Constraint(expr=   m.x70 + m.x71 == 106.777870451)

m.c28 = Constraint(expr=   m.x72 + m.x73 == 106.777870451)

m.c29 = Constraint(expr=   m.x74 + m.x75 == 106.777870451)

m.c30 = Constraint(expr=   m.x76 + m.x77 == 106.777870451)

m.c31 = Constraint(expr=   m.x78 + m.x79 == 106.777870451)

m.c32 = Constraint(expr=   m.x80 + m.x81 == 106.777870451)

m.c33 = Constraint(expr=   m.x82 + m.x83 == 106.777870451)

m.c34 = Constraint(expr=   m.x84 + m.x85 == 106.777870451)

m.c35 = Constraint(expr=   m.x86 + m.x87 == 106.777870452)

m.c36 = Constraint(expr=   m.x88 + m.x89 == 106.777870452)

m.c37 = Constraint(expr=   m.x90 + m.x91 == 106.777870452)

m.c38 = Constraint(expr= - m.x92 + m.x93 == 0)

m.c39 = Constraint(expr= - m.x94 + m.x95 == 0)

m.c40 = Constraint(expr= - m.x96 + m.x97 == 0)

m.c41 = Constraint(expr=   m.x92 - m.x98 - m.x99 - m.x100 == 0)

m.c42 = Constraint(expr=   m.x94 - m.x101 - m.x102 - m.x103 == 0)

m.c43 = Constraint(expr=   m.x96 - m.x104 - m.x105 - m.x106 == 0)

m.c44 = Constraint(expr=   m.x107 == 0.025)

m.c45 = Constraint(expr=   m.x108 == 0.025)

m.c46 = Constraint(expr=   m.x109 == 0.025)

m.c47 = Constraint(expr=   m.x110 == 0.013)

m.c48 = Constraint(expr=   m.x111 == 0.012)

m.c49 = Constraint(expr=   m.x112 == 0.007)

m.c50 = Constraint(expr=   m.x113 + m.x114 - m.x115 == 0)

m.c51 = Constraint(expr=   m.x116 + m.x117 - m.x118 == 0)

m.c52 = Constraint(expr=   m.x119 + m.x120 - m.x121 == 0)

m.c53 = Constraint(expr=   m.x100 - m.x113 + m.x122 - m.x123 == 0)

m.c54 = Constraint(expr=   m.x103 - m.x116 + m.x124 - m.x125 == 0)

m.c55 = Constraint(expr=   m.x106 - m.x119 + m.x126 - m.x127 == 0)

m.c56 = Constraint(expr=   m.x99 - m.x128 == 0)

m.c57 = Constraint(expr=   m.x102 - m.x129 == 0)

m.c58 = Constraint(expr=   m.x105 - m.x130 == 0)

m.c59 = Constraint(expr=   m.x115 + m.x131 + m.x132 + m.x133 - m.x134 - m.x135 == 0)

m.c60 = Constraint(expr=   m.x118 + m.x136 + m.x137 + m.x138 - m.x139 - m.x140 == 0)

m.c61 = Constraint(expr=   m.x121 + m.x141 + m.x142 + m.x143 - m.x144 - m.x145 == 0)

m.c62 = Constraint(expr= - m.x107 + m.x123 + m.x128 - m.x146 == 0)

m.c63 = Constraint(expr= - m.x108 + m.x125 + m.x129 - m.x147 == 0)

m.c64 = Constraint(expr= - m.x109 + m.x127 + m.x130 - m.x148 == 0)

m.c65 = Constraint(expr= - m.x110 - m.x114 + m.x146 == 0)

m.c66 = Constraint(expr= - m.x111 - m.x117 + m.x147 == 0)

m.c67 = Constraint(expr= - m.x112 - m.x120 + m.x148 == 0)

m.c68 = Constraint(expr=   m.x98 - m.x122 == 0)

m.c69 = Constraint(expr=   m.x101 - m.x124 == 0)

m.c70 = Constraint(expr=   m.x104 - m.x126 == 0)

m.c71 = Constraint(expr= - m.x149 == 0.1624)

m.c72 = Constraint(expr= - m.x150 == 0.1616)

m.c73 = Constraint(expr= - m.x151 == 0.0912)

m.c74 = Constraint(expr=   m.x149 - m.x152 + m.x153 == 0)

m.c75 = Constraint(expr=   m.x150 - m.x154 + m.x155 == 0)

m.c76 = Constraint(expr=   m.x151 - m.x156 + m.x157 == 0)

m.c77 = Constraint(expr=   m.x158 + m.x159 - m.x160 == 0)

m.c78 = Constraint(expr=   m.x161 + m.x162 - m.x163 == 0)

m.c79 = Constraint(expr=   m.x164 + m.x165 - m.x166 == 0)

m.c80 = Constraint(expr=   m.x160 + m.x167 - m.x168 == 0)

m.c81 = Constraint(expr=   m.x163 + m.x169 - m.x170 == 0)

m.c82 = Constraint(expr=   m.x166 + m.x171 - m.x172 == 0)

m.c83 = Constraint(expr= - m.x167 - m.x173 == 0.0138888888888889)

m.c84 = Constraint(expr= - m.x169 - m.x174 == 0.0138888888888889)

m.c85 = Constraint(expr= - m.x171 - m.x175 == 0.0138888888888889)

m.c86 = Constraint(expr= - m.x132 + m.x173 - m.x176 == 0)

m.c87 = Constraint(expr= - m.x137 + m.x174 - m.x177 == 0)

m.c88 = Constraint(expr= - m.x142 + m.x175 - m.x178 == 0)

m.c89 = Constraint(expr=   m.x179 == 0)

m.c90 = Constraint(expr=   m.x180 == 0)

m.c91 = Constraint(expr=   m.x181 == 0)

m.c92 = Constraint(expr= - m.x133 + m.x168 == 0)

m.c93 = Constraint(expr= - m.x138 + m.x170 == 0)

m.c94 = Constraint(expr= - m.x143 + m.x172 == 0)

m.c95 = Constraint(expr= - m.x131 - m.x153 == 0)

m.c96 = Constraint(expr= - m.x136 - m.x155 == 0)

m.c97 = Constraint(expr= - m.x141 - m.x157 == 0)

m.c98 = Constraint(expr= - m.x93 + m.x182 == 0)

m.c99 = Constraint(expr= - m.x95 + m.x183 == 0)

m.c100 = Constraint(expr= - m.x97 + m.x184 == 0)

m.c101 = Constraint(expr=   3600*m.x152 + 239.978718892*m.x185 - 239.978718892*m.x186 == 0)

m.c102 = Constraint(expr=   3600*m.x154 + 239.978718892*m.x187 - 239.978718892*m.x188 == 0)

m.c103 = Constraint(expr=   3600*m.x156 + 239.978718892*m.x189 - 239.978718892*m.x190 == 0)

m.c104 = Constraint(expr=   3600*m.x134 - 3600*m.x158 + 416.560177655*m.x191 - 416.560177655*m.x192 == 0)

m.c105 = Constraint(expr=   3600*m.x139 - 3600*m.x161 + 416.560177655*m.x193 - 416.560177655*m.x194 == 0)

m.c106 = Constraint(expr=   3600*m.x144 - 3600*m.x164 + 416.560177655*m.x195 - 416.560177655*m.x196 == 0)

m.c107 = Constraint(expr=   3600*m.x135 - 3600*m.x159 + 416.560177655*m.x197 - 416.560177655*m.x198 == 0)

m.c108 = Constraint(expr=   3600*m.x140 - 3600*m.x162 + 416.560177655*m.x199 - 416.560177655*m.x200 == 0)

m.c109 = Constraint(expr=   3600*m.x145 - 3600*m.x165 + 416.560177655*m.x201 - 416.560177655*m.x202 == 0)

m.c110 = Constraint(expr=   3600*m.x176 - 3600*m.x179 + 165.129961038*m.x203 - 165.129961038*m.x204 == 0)

m.c111 = Constraint(expr=   3600*m.x177 - 3600*m.x180 + 165.129961038*m.x205 - 165.129961038*m.x206 == 0)

m.c112 = Constraint(expr=   3600*m.x178 - 3600*m.x181 + 165.129961038*m.x207 - 165.129961038*m.x208 == 0)

m.c113 = Constraint(expr= - m.x186 + m.x187 == 0)

m.c114 = Constraint(expr= - m.x188 + m.x189 == 0)

m.c115 = Constraint(expr= - m.x192 + m.x193 == 0)

m.c116 = Constraint(expr= - m.x194 + m.x195 == 0)

m.c117 = Constraint(expr= - m.x198 + m.x199 == 0)

m.c118 = Constraint(expr= - m.x200 + m.x201 == 0)

m.c119 = Constraint(expr= - m.x204 + m.x205 == 0)

m.c120 = Constraint(expr= - m.x206 + m.x207 == 0)

m.c121 = Constraint(expr= - 0.037494*m.b2 + m.x209 >= 0)

m.c122 = Constraint(expr= - 0.037494*m.b3 + m.x211 >= 0)

m.c123 = Constraint(expr= - 0.037494*m.b4 + m.x213 >= 0)

m.c124 = Constraint(expr= - 0.074997*m.b5 + m.x215 >= 0)

m.c125 = Constraint(expr= - 0.074997*m.b6 + m.x217 >= 0)

m.c126 = Constraint(expr= - 0.074997*m.b7 + m.x219 >= 0)

m.c127 = Constraint(expr= - 0.074997*m.b8 + m.x221 >= 0)

m.c128 = Constraint(expr= - 0.074997*m.b9 + m.x223 >= 0)

m.c129 = Constraint(expr= - 0.074997*m.b10 + m.x225 >= 0)

m.c130 = Constraint(expr= - 0.074997*m.b11 + m.x227 >= 0)

m.c131 = Constraint(expr= - 0.074997*m.b12 + m.x229 >= 0)

m.c132 = Constraint(expr= - 0.074997*m.b13 + m.x231 >= 0)

m.c133 = Constraint(expr= - 0.074997*m.b14 + m.x233 >= 0)

m.c134 = Constraint(expr= - 0.074997*m.b15 + m.x235 >= 0)

m.c135 = Constraint(expr= - 0.074997*m.b16 + m.x237 >= 0)

m.c136 = Constraint(expr= - 0.074997*m.b17 + m.x239 >= 0)

m.c137 = Constraint(expr= - 0.074997*m.b18 + m.x241 >= 0)

m.c138 = Constraint(expr= - 0.074997*m.b19 + m.x243 >= 0)

m.c139 = Constraint(expr= - 0.074997*m.b20 + m.x245 >= 0)

m.c140 = Constraint(expr= - 0.074997*m.b21 + m.x247 >= 0)

m.c141 = Constraint(expr= - 0.074997*m.b22 + m.x249 >= 0)

m.c142 = Constraint(expr= - 0.037494*m.b23 + m.x251 >= 0)

m.c143 = Constraint(expr= - 0.037494*m.b24 + m.x253 >= 0)

m.c144 = Constraint(expr= - 0.037494*m.b25 + m.x255 >= 0)

m.c145 = Constraint(expr= - 0.097497*m.b26 + m.x257 >= 0)

m.c146 = Constraint(expr= - 0.097497*m.b27 + m.x259 >= 0)

m.c147 = Constraint(expr= - 0.097497*m.b28 + m.x261 >= 0)

m.c148 = Constraint(expr= - 0.097497*m.b29 + m.x263 >= 0)

m.c149 = Constraint(expr= - 0.097497*m.b30 + m.x265 >= 0)

m.c150 = Constraint(expr= - 0.097497*m.b31 + m.x267 >= 0)

m.c151 = Constraint(expr= - 0.097497*m.b32 + m.x269 >= 0)

m.c152 = Constraint(expr= - 0.097497*m.b33 + m.x271 >= 0)

m.c153 = Constraint(expr= - 0.097497*m.b34 + m.x273 >= 0)

m.c154 = Constraint(expr= - 0.058743*m.b35 + m.x275 >= 0)

m.c155 = Constraint(expr= - 0.058743*m.b36 + m.x277 >= 0)

m.c156 = Constraint(expr= - 0.058743*m.b37 + m.x279 >= 0)

m.c157 = Constraint(expr= - 0.045826*m.b2 + m.x209 <= 0)

m.c158 = Constraint(expr= - 0.045826*m.b3 + m.x211 <= 0)

m.c159 = Constraint(expr= - 0.045826*m.b4 + m.x213 <= 0)

m.c160 = Constraint(expr= - 0.091663*m.b5 + m.x215 <= 0)

m.c161 = Constraint(expr= - 0.091663*m.b6 + m.x217 <= 0)

m.c162 = Constraint(expr= - 0.091663*m.b7 + m.x219 <= 0)

m.c163 = Constraint(expr= - 0.091663*m.b8 + m.x221 <= 0)

m.c164 = Constraint(expr= - 0.091663*m.b9 + m.x223 <= 0)

m.c165 = Constraint(expr= - 0.091663*m.b10 + m.x225 <= 0)

m.c166 = Constraint(expr= - 0.091663*m.b11 + m.x227 <= 0)

m.c167 = Constraint(expr= - 0.091663*m.b12 + m.x229 <= 0)

m.c168 = Constraint(expr= - 0.091663*m.b13 + m.x231 <= 0)

m.c169 = Constraint(expr= - 0.091663*m.b14 + m.x233 <= 0)

m.c170 = Constraint(expr= - 0.091663*m.b15 + m.x235 <= 0)

m.c171 = Constraint(expr= - 0.091663*m.b16 + m.x237 <= 0)

m.c172 = Constraint(expr= - 0.091663*m.b17 + m.x239 <= 0)

m.c173 = Constraint(expr= - 0.091663*m.b18 + m.x241 <= 0)

m.c174 = Constraint(expr= - 0.091663*m.b19 + m.x243 <= 0)

m.c175 = Constraint(expr= - 0.091663*m.b20 + m.x245 <= 0)

m.c176 = Constraint(expr= - 0.091663*m.b21 + m.x247 <= 0)

m.c177 = Constraint(expr= - 0.091663*m.b22 + m.x249 <= 0)

m.c178 = Constraint(expr= - 0.045826*m.b23 + m.x251 <= 0)

m.c179 = Constraint(expr= - 0.045826*m.b24 + m.x253 <= 0)

m.c180 = Constraint(expr= - 0.045826*m.b25 + m.x255 <= 0)

m.c181 = Constraint(expr= - 0.119163*m.b26 + m.x257 <= 0)

m.c182 = Constraint(expr= - 0.119163*m.b27 + m.x259 <= 0)

m.c183 = Constraint(expr= - 0.119163*m.b28 + m.x261 <= 0)

m.c184 = Constraint(expr= - 0.119163*m.b29 + m.x263 <= 0)

m.c185 = Constraint(expr= - 0.119163*m.b30 + m.x265 <= 0)

m.c186 = Constraint(expr= - 0.119163*m.b31 + m.x267 <= 0)

m.c187 = Constraint(expr= - 0.119163*m.b32 + m.x269 <= 0)

m.c188 = Constraint(expr= - 0.119163*m.b33 + m.x271 <= 0)

m.c189 = Constraint(expr= - 0.119163*m.b34 + m.x273 <= 0)

m.c190 = Constraint(expr= - 0.071797*m.b35 + m.x275 <= 0)

m.c191 = Constraint(expr= - 0.071797*m.b36 + m.x277 <= 0)

m.c192 = Constraint(expr= - 0.071797*m.b37 + m.x279 <= 0)

m.c193 = Constraint(expr= - m.x185 + m.x281 == 300)

m.c194 = Constraint(expr= - m.x187 + m.x282 == 300)

m.c195 = Constraint(expr= - m.x189 + m.x283 == 300)

m.c196 = Constraint(expr= - m.x191 + m.x284 == 240)

m.c197 = Constraint(expr= - m.x193 + m.x285 == 240)

m.c198 = Constraint(expr= - m.x195 + m.x286 == 240)

m.c199 = Constraint(expr= - m.x197 + m.x287 == 240)

m.c200 = Constraint(expr= - m.x199 + m.x288 == 240)

m.c201 = Constraint(expr= - m.x201 + m.x289 == 240)

m.c202 = Constraint(expr= - m.x203 + m.x290 == 243)

m.c203 = Constraint(expr= - m.x205 + m.x291 == 243)

m.c204 = Constraint(expr= - m.x207 + m.x292 == 243)

m.c205 = Constraint(expr=   m.x293 - m.x294 - m.x295 == 0)

m.c206 = Constraint(expr=   m.x296 - m.x297 - m.x298 == 0)

m.c207 = Constraint(expr=   m.x299 - m.x300 - m.x301 == 0)

m.c208 = Constraint(expr=   m.x294 - m.x302 - m.x303 == 0)

m.c209 = Constraint(expr=   m.x297 - m.x304 - m.x305 == 0)

m.c210 = Constraint(expr=   m.x300 - m.x306 - m.x307 == 0)

m.c211 = Constraint(expr=   m.x294 - m.x308 - m.x309 == 0)

m.c212 = Constraint(expr=   m.x297 - m.x310 - m.x311 == 0)

m.c213 = Constraint(expr=   m.x300 - m.x312 - m.x313 == 0)

m.c214 = Constraint(expr=   m.x314 - m.x315 - m.x316 == 0)

m.c215 = Constraint(expr=   m.x317 - m.x318 - m.x319 == 0)

m.c216 = Constraint(expr=   m.x320 - m.x321 - m.x322 == 0)

m.c217 = Constraint(expr= - m.x323 + m.x324 - m.x325 == 0)

m.c218 = Constraint(expr= - m.x326 + m.x327 - m.x328 == 0)

m.c219 = Constraint(expr= - m.x329 + m.x330 - m.x331 == 0)

m.c220 = Constraint(expr=   m.x308 - m.x323 - m.x332 == 0)

m.c221 = Constraint(expr=   m.x310 - m.x326 - m.x333 == 0)

m.c222 = Constraint(expr=   m.x312 - m.x329 - m.x334 == 0)

m.c223 = Constraint(expr=   m.x294 - m.x314 - m.x335 == 0)

m.c224 = Constraint(expr=   m.x297 - m.x317 - m.x336 == 0)

m.c225 = Constraint(expr=   m.x300 - m.x320 - m.x337 == 0)

m.c226 = Constraint(expr=   m.x315 - m.x324 - m.x338 == 0)

m.c227 = Constraint(expr=   m.x318 - m.x327 - m.x339 == 0)

m.c228 = Constraint(expr=   m.x321 - m.x330 - m.x340 == 0)

m.c229 = Constraint(expr=   m.x302 - m.x308 - m.x341 == 0)

m.c230 = Constraint(expr=   m.x304 - m.x310 - m.x342 == 0)

m.c231 = Constraint(expr=   m.x306 - m.x312 - m.x343 == 0)

m.c232 = Constraint(expr=   m.x308 - m.x315 - m.x344 == 0)

m.c233 = Constraint(expr=   m.x310 - m.x318 - m.x345 == 0)

m.c234 = Constraint(expr=   m.x312 - m.x321 - m.x346 == 0)

m.c235 = Constraint(expr=   m.x315 - m.x347 - m.x348 == 0)

m.c236 = Constraint(expr=   m.x318 - m.x349 - m.x350 == 0)

m.c237 = Constraint(expr=   m.x321 - m.x351 - m.x352 == 0)

m.c238 = Constraint(expr=   m.x324 - m.x353 - m.x354 == 0)

m.c239 = Constraint(expr=   m.x327 - m.x355 - m.x356 == 0)

m.c240 = Constraint(expr=   m.x330 - m.x357 - m.x358 == 0)

m.c241 = Constraint(expr= - m.x359 + m.x360 - m.x361 == 0)

m.c242 = Constraint(expr= - m.x362 + m.x363 - m.x364 == 0)

m.c243 = Constraint(expr= - m.x365 + m.x366 - m.x367 == 0)

m.c244 = Constraint(expr= - m.x368 + m.x369 - m.x370 == 0)

m.c245 = Constraint(expr= - m.x371 + m.x372 - m.x373 == 0)

m.c246 = Constraint(expr= - m.x374 + m.x375 - m.x376 == 0)

m.c247 = Constraint(expr= - m.x281 + m.x368 - m.x377 == 0)

m.c248 = Constraint(expr= - m.x282 + m.x371 - m.x378 == 0)

m.c249 = Constraint(expr= - m.x283 + m.x374 - m.x379 == 0)

m.c250 = Constraint(expr=   m.x284 - m.x380 - m.x381 == 0)

m.c251 = Constraint(expr=   m.x285 - m.x382 - m.x383 == 0)

m.c252 = Constraint(expr=   m.x286 - m.x384 - m.x385 == 0)

m.c253 = Constraint(expr=   m.x287 - m.x380 - m.x386 == 0)

m.c254 = Constraint(expr=   m.x288 - m.x382 - m.x387 == 0)

m.c255 = Constraint(expr=   m.x289 - m.x384 - m.x388 == 0)

m.c256 = Constraint(expr= - m.x389 + m.x390 - m.x391 == 0)

m.c257 = Constraint(expr= - m.x392 + m.x393 - m.x394 == 0)

m.c258 = Constraint(expr= - m.x395 + m.x396 - m.x397 == 0)

m.c259 = Constraint(expr= - m.x359 + m.x398 - m.x399 == 0)

m.c260 = Constraint(expr= - m.x362 + m.x400 - m.x401 == 0)

m.c261 = Constraint(expr= - m.x365 + m.x402 - m.x403 == 0)

m.c262 = Constraint(expr=   m.x390 - m.x398 - m.x404 == 0)

m.c263 = Constraint(expr=   m.x393 - m.x400 - m.x405 == 0)

m.c264 = Constraint(expr=   m.x396 - m.x402 - m.x406 == 0)

m.c265 = Constraint(expr= - m.x359 + m.x407 - m.x408 == 0)

m.c266 = Constraint(expr= - m.x362 + m.x409 - m.x410 == 0)

m.c267 = Constraint(expr= - m.x365 + m.x411 - m.x412 == 0)

m.c268 = Constraint(expr=   m.x290 - m.x413 - m.x414 == 0)

m.c269 = Constraint(expr=   m.x291 - m.x415 - m.x416 == 0)

m.c270 = Constraint(expr=   m.x292 - m.x417 - m.x418 == 0)

m.c271 = Constraint(expr=   m.x293 - m.x419 - m.x420 == 0)

m.c272 = Constraint(expr=   m.x296 - m.x421 - m.x422 == 0)

m.c273 = Constraint(expr=   m.x299 - m.x423 - m.x424 == 0)

m.c274 = Constraint(expr= - m.x380 + m.x389 - m.x425 == 0)

m.c275 = Constraint(expr= - m.x382 + m.x392 - m.x426 == 0)

m.c276 = Constraint(expr= - m.x384 + m.x395 - m.x427 == 0)

m.c277 = Constraint(expr= - 239.978718892*m.x185 + 239.978718892*m.x190 - 416.560177655*m.x191 + 416.560177655*m.x196
                          - 416.560177655*m.x197 + 416.560177655*m.x202 - 165.129961038*m.x203 + 165.129961038*m.x208
                          >= 0)

m.c278 = Constraint(expr=   m.b2 - m.b23 >= 0)

m.c279 = Constraint(expr=   m.b3 - m.b24 >= 0)

m.c280 = Constraint(expr=   m.b4 - m.b25 >= 0)

m.c281 = Constraint(expr=   m.b5 - m.b8 >= 0)

m.c282 = Constraint(expr=   m.b6 - m.b9 >= 0)

m.c283 = Constraint(expr=   m.b7 - m.b10 >= 0)

m.c284 = Constraint(expr=   m.b8 - m.b11 >= 0)

m.c285 = Constraint(expr=   m.b9 - m.b12 >= 0)

m.c286 = Constraint(expr=   m.b10 - m.b13 >= 0)

m.c287 = Constraint(expr=   m.b11 - m.b14 >= 0)

m.c288 = Constraint(expr=   m.b12 - m.b15 >= 0)

m.c289 = Constraint(expr=   m.b13 - m.b16 >= 0)

m.c290 = Constraint(expr=   m.b14 - m.b17 >= 0)

m.c291 = Constraint(expr=   m.b15 - m.b18 >= 0)

m.c292 = Constraint(expr=   m.b16 - m.b19 >= 0)

m.c293 = Constraint(expr=   m.b17 - m.b20 >= 0)

m.c294 = Constraint(expr=   m.b18 - m.b21 >= 0)

m.c295 = Constraint(expr=   m.b19 - m.b22 >= 0)

m.c296 = Constraint(expr=   m.b26 - m.b29 >= 0)

m.c297 = Constraint(expr=   m.b27 - m.b30 >= 0)

m.c298 = Constraint(expr=   m.b28 - m.b31 >= 0)

m.c299 = Constraint(expr=   m.b29 - m.b32 >= 0)

m.c300 = Constraint(expr=   m.b30 - m.b33 >= 0)

m.c301 = Constraint(expr=   m.b31 - m.b34 >= 0)

m.c302 = Constraint(expr=   m.x93 - m.x209 - m.x215 - m.x221 - m.x227 - m.x233 - m.x239 - m.x245 - m.x251 == 0)

m.c303 = Constraint(expr=   m.x95 - m.x211 - m.x217 - m.x223 - m.x229 - m.x235 - m.x241 - m.x247 - m.x253 == 0)

m.c304 = Constraint(expr=   m.x97 - m.x213 - m.x219 - m.x225 - m.x231 - m.x237 - m.x243 - m.x249 - m.x255 == 0)

m.c305 = Constraint(expr=   m.x160 - m.x257 - m.x263 - m.x269 - m.x275 == 0)

m.c306 = Constraint(expr=   m.x163 - m.x259 - m.x265 - m.x271 - m.x277 == 0)

m.c307 = Constraint(expr=   m.x166 - m.x261 - m.x267 - m.x273 - m.x279 == 0)

m.c308 = Constraint(expr= - 712.572602172813*m.b2 + m.x210 - m.x420 >= -712.572602172813)

m.c309 = Constraint(expr= - 712.572602172813*m.b3 + m.x214 - m.x422 >= -712.572602172813)

m.c310 = Constraint(expr= - 712.572602172813*m.b4 + m.x218 - m.x424 >= -712.572602172813)

m.c311 = Constraint(expr= - 851.700667228731*m.b5 + m.x224 - m.x420 >= -851.700667228731)

m.c312 = Constraint(expr= - 851.700667228731*m.b6 + m.x230 - m.x422 >= -851.700667228731)

m.c313 = Constraint(expr= - 851.700667228731*m.b7 + m.x236 - m.x424 >= -851.700667228731)

m.c314 = Constraint(expr= - 851.700667228731*m.b8 + m.x242 - m.x420 >= -851.700667228731)

m.c315 = Constraint(expr= - 851.700667228731*m.b9 + m.x248 - m.x422 >= -851.700667228731)

m.c316 = Constraint(expr= - 851.700667228731*m.b10 + m.x254 - m.x424 >= -851.700667228731)

m.c317 = Constraint(expr= - 851.700667228731*m.b11 + m.x260 - m.x420 >= -851.700667228731)

m.c318 = Constraint(expr= - 851.700667228731*m.b12 + m.x266 - m.x422 >= -851.700667228731)

m.c319 = Constraint(expr= - 851.700667228731*m.b13 + m.x272 - m.x424 >= -851.700667228731)

m.c320 = Constraint(expr= - 851.700667228731*m.b14 + m.x278 - m.x420 >= -851.700667228731)

m.c321 = Constraint(expr= - 851.700667228731*m.b15 - m.x422 + m.x453 >= -851.700667228731)

m.c322 = Constraint(expr= - 851.700667228731*m.b16 - m.x424 + m.x456 >= -851.700667228731)

m.c323 = Constraint(expr= - 851.700667228731*m.b17 - m.x420 + m.x459 >= -851.700667228731)

m.c324 = Constraint(expr= - 851.700667228731*m.b18 + m.x48 - m.x422 >= -851.700667228731)

m.c325 = Constraint(expr= - 851.700667228731*m.b19 + m.x51 - m.x424 >= -851.700667228731)

m.c326 = Constraint(expr= - 851.700667228731*m.b20 + m.x54 - m.x420 >= -851.700667228731)

m.c327 = Constraint(expr= - 851.700667228731*m.b21 + m.x57 - m.x422 >= -851.700667228731)

m.c328 = Constraint(expr= - 851.700667228731*m.b22 + m.x60 - m.x424 >= -851.700667228731)

m.c329 = Constraint(expr= - 712.572602172813*m.b23 + m.x62 - m.x420 >= -712.572602172813)

m.c330 = Constraint(expr= - 712.572602172813*m.b24 + m.x64 - m.x422 >= -712.572602172813)

m.c331 = Constraint(expr= - 712.572602172813*m.b25 + m.x66 - m.x424 >= -712.572602172813)

m.c332 = Constraint(expr= - 925.825187656153*m.b26 + m.x68 - m.x425 >= -925.825187656153)

m.c333 = Constraint(expr= - 925.825187656153*m.b27 + m.x70 - m.x426 >= -925.825187656153)

m.c334 = Constraint(expr= - 925.825187656153*m.b28 + m.x72 - m.x427 >= -925.825187656153)

m.c335 = Constraint(expr= - 925.825187656153*m.b29 + m.x74 - m.x425 >= -925.825187656153)

m.c336 = Constraint(expr= - 925.825187656153*m.b30 + m.x76 - m.x426 >= -925.825187656153)

m.c337 = Constraint(expr= - 925.825187656153*m.b31 + m.x78 - m.x427 >= -925.825187656153)

m.c338 = Constraint(expr= - 925.825187656153*m.b32 + m.x80 - m.x425 >= -925.825187656153)

m.c339 = Constraint(expr= - 925.825187656153*m.b33 + m.x82 - m.x426 >= -925.825187656153)

m.c340 = Constraint(expr= - 925.825187656153*m.b34 + m.x84 - m.x427 >= -925.825187656153)

m.c341 = Constraint(expr= - 925.825187656502*m.b35 + m.x86 - m.x425 >= -925.825187656502)

m.c342 = Constraint(expr= - 925.825187656502*m.b36 + m.x88 - m.x426 >= -925.825187656502)

m.c343 = Constraint(expr= - 925.825187656502*m.b37 + m.x90 - m.x427 >= -925.825187656502)

m.c344 = Constraint(expr=   447.864247971*m.b2 + m.x210 - m.x420 <= 447.864247971)

m.c345 = Constraint(expr=   447.864247971*m.b3 + m.x214 - m.x422 <= 447.864247971)

m.c346 = Constraint(expr=   447.864247971*m.b4 + m.x218 - m.x424 <= 447.864247971)

m.c347 = Constraint(expr=   672.20455381568*m.b5 + m.x224 - m.x420 <= 672.20455381568)

m.c348 = Constraint(expr=   672.20455381568*m.b6 + m.x230 - m.x422 <= 672.20455381568)

m.c349 = Constraint(expr=   672.20455381568*m.b7 + m.x236 - m.x424 <= 672.20455381568)

m.c350 = Constraint(expr=   672.20455381568*m.b8 + m.x242 - m.x420 <= 672.20455381568)

m.c351 = Constraint(expr=   672.20455381568*m.b9 + m.x248 - m.x422 <= 672.20455381568)

m.c352 = Constraint(expr=   672.20455381568*m.b10 + m.x254 - m.x424 <= 672.20455381568)

m.c353 = Constraint(expr=   672.20455381568*m.b11 + m.x260 - m.x420 <= 672.20455381568)

m.c354 = Constraint(expr=   672.20455381568*m.b12 + m.x266 - m.x422 <= 672.20455381568)

m.c355 = Constraint(expr=   672.20455381568*m.b13 + m.x272 - m.x424 <= 672.20455381568)

m.c356 = Constraint(expr=   672.20455381568*m.b14 + m.x278 - m.x420 <= 672.20455381568)

m.c357 = Constraint(expr=   672.20455381568*m.b15 - m.x422 + m.x453 <= 672.20455381568)

m.c358 = Constraint(expr=   672.20455381568*m.b16 - m.x424 + m.x456 <= 672.20455381568)

m.c359 = Constraint(expr=   672.20455381568*m.b17 - m.x420 + m.x459 <= 672.20455381568)

m.c360 = Constraint(expr=   672.20455381568*m.b18 + m.x48 - m.x422 <= 672.20455381568)

m.c361 = Constraint(expr=   672.20455381568*m.b19 + m.x51 - m.x424 <= 672.20455381568)

m.c362 = Constraint(expr=   672.20455381568*m.b20 + m.x54 - m.x420 <= 672.20455381568)

m.c363 = Constraint(expr=   672.20455381568*m.b21 + m.x57 - m.x422 <= 672.20455381568)

m.c364 = Constraint(expr=   672.20455381568*m.b22 + m.x60 - m.x424 <= 672.20455381568)

m.c365 = Constraint(expr=   447.864247971*m.b23 + m.x62 - m.x420 <= 447.864247971)

m.c366 = Constraint(expr=   447.864247971*m.b24 + m.x64 - m.x422 <= 447.864247971)

m.c367 = Constraint(expr=   447.864247971*m.b25 + m.x66 - m.x424 <= 447.864247971)

m.c368 = Constraint(expr=   1106.777870451*m.b26 + m.x68 - m.x425 <= 1106.777870451)

m.c369 = Constraint(expr=   1106.777870451*m.b27 + m.x70 - m.x426 <= 1106.777870451)

m.c370 = Constraint(expr=   1106.777870451*m.b28 + m.x72 - m.x427 <= 1106.777870451)

m.c371 = Constraint(expr=   1106.777870451*m.b29 + m.x74 - m.x425 <= 1106.777870451)

m.c372 = Constraint(expr=   1106.777870451*m.b30 + m.x76 - m.x426 <= 1106.777870451)

m.c373 = Constraint(expr=   1106.777870451*m.b31 + m.x78 - m.x427 <= 1106.777870451)

m.c374 = Constraint(expr=   1106.777870451*m.b32 + m.x80 - m.x425 <= 1106.777870451)

m.c375 = Constraint(expr=   1106.777870451*m.b33 + m.x82 - m.x426 <= 1106.777870451)

m.c376 = Constraint(expr=   1106.777870451*m.b34 + m.x84 - m.x427 <= 1106.777870451)

m.c377 = Constraint(expr=   1106.777870452*m.b35 + m.x86 - m.x425 <= 1106.777870452)

m.c378 = Constraint(expr=   1106.777870452*m.b36 + m.x88 - m.x426 <= 1106.777870452)

m.c379 = Constraint(expr=   1106.777870452*m.b37 + m.x90 - m.x427 <= 1106.777870452)

m.c380 = Constraint(expr=   m.b2 - m.b3 + m.x428 >= 0)

m.c381 = Constraint(expr=   m.b3 - m.b4 + m.x429 >= 0)

m.c382 = Constraint(expr=   m.b5 - m.b6 + m.x430 >= 0)

m.c383 = Constraint(expr=   m.b6 - m.b7 + m.x431 >= 0)

m.c384 = Constraint(expr=   m.b8 - m.b9 + m.x432 >= 0)

m.c385 = Constraint(expr=   m.b9 - m.b10 + m.x433 >= 0)

m.c386 = Constraint(expr=   m.b11 - m.b12 + m.x434 >= 0)

m.c387 = Constraint(expr=   m.b12 - m.b13 + m.x435 >= 0)

m.c388 = Constraint(expr=   m.b14 - m.b15 + m.x436 >= 0)

m.c389 = Constraint(expr=   m.b15 - m.b16 + m.x437 >= 0)

m.c390 = Constraint(expr=   m.b17 - m.b18 + m.x438 >= 0)

m.c391 = Constraint(expr=   m.b18 - m.b19 + m.x439 >= 0)

m.c392 = Constraint(expr=   m.b20 - m.b21 + m.x440 >= 0)

m.c393 = Constraint(expr=   m.b21 - m.b22 + m.x441 >= 0)

m.c394 = Constraint(expr=   m.b23 - m.b24 + m.x442 >= 0)

m.c395 = Constraint(expr=   m.b24 - m.b25 + m.x443 >= 0)

m.c396 = Constraint(expr=   m.b26 - m.b27 + m.x444 >= 0)

m.c397 = Constraint(expr=   m.b27 - m.b28 + m.x445 >= 0)

m.c398 = Constraint(expr=   m.b29 - m.b30 + m.x446 >= 0)

m.c399 = Constraint(expr=   m.b30 - m.b31 + m.x447 >= 0)

m.c400 = Constraint(expr=   m.b32 - m.b33 + m.x448 >= 0)

m.c401 = Constraint(expr=   m.b33 - m.b34 + m.x449 >= 0)

m.c402 = Constraint(expr=   m.b35 - m.b36 + m.x450 >= 0)

m.c403 = Constraint(expr=   m.b36 - m.b37 + m.x451 >= 0)

m.c404 = Constraint(expr= - m.b2 + m.b3 + m.x428 >= 0)

m.c405 = Constraint(expr= - m.b3 + m.b4 + m.x429 >= 0)

m.c406 = Constraint(expr= - m.b5 + m.b6 + m.x430 >= 0)

m.c407 = Constraint(expr= - m.b6 + m.b7 + m.x431 >= 0)

m.c408 = Constraint(expr= - m.b8 + m.b9 + m.x432 >= 0)

m.c409 = Constraint(expr= - m.b9 + m.b10 + m.x433 >= 0)

m.c410 = Constraint(expr= - m.b11 + m.b12 + m.x434 >= 0)

m.c411 = Constraint(expr= - m.b12 + m.b13 + m.x435 >= 0)

m.c412 = Constraint(expr= - m.b14 + m.b15 + m.x436 >= 0)

m.c413 = Constraint(expr= - m.b15 + m.b16 + m.x437 >= 0)

m.c414 = Constraint(expr= - m.b17 + m.b18 + m.x438 >= 0)

m.c415 = Constraint(expr= - m.b18 + m.b19 + m.x439 >= 0)

m.c416 = Constraint(expr= - m.b20 + m.b21 + m.x440 >= 0)

m.c417 = Constraint(expr= - m.b21 + m.b22 + m.x441 >= 0)

m.c418 = Constraint(expr= - m.b23 + m.b24 + m.x442 >= 0)

m.c419 = Constraint(expr= - m.b24 + m.b25 + m.x443 >= 0)

m.c420 = Constraint(expr= - m.b26 + m.b27 + m.x444 >= 0)

m.c421 = Constraint(expr= - m.b27 + m.b28 + m.x445 >= 0)

m.c422 = Constraint(expr= - m.b29 + m.b30 + m.x446 >= 0)

m.c423 = Constraint(expr= - m.b30 + m.b31 + m.x447 >= 0)

m.c424 = Constraint(expr= - m.b32 + m.b33 + m.x448 >= 0)

m.c425 = Constraint(expr= - m.b33 + m.b34 + m.x449 >= 0)

m.c426 = Constraint(expr= - m.b35 + m.b36 + m.x450 >= 0)

m.c427 = Constraint(expr= - m.b36 + m.b37 + m.x451 >= 0)

m.c428 = Constraint(expr= - 5*m.b38 + m.x115 <= 0)

m.c429 = Constraint(expr= - 5*m.b39 + m.x118 <= 0)

m.c430 = Constraint(expr= - 5*m.b40 + m.x121 <= 0)

m.c431 = Constraint(expr= - 5*m.b41 + m.x168 <= 0)

m.c432 = Constraint(expr= - 5*m.b42 + m.x170 <= 0)

m.c433 = Constraint(expr= - 5*m.b43 + m.x172 <= 0)

m.c434 = Constraint(expr= - 5*m.b44 + m.x153 <= 0)

m.c435 = Constraint(expr= - 5*m.b45 + m.x155 <= 0)

m.c436 = Constraint(expr= - 5*m.b46 + m.x157 <= 0)

m.c437 = Constraint(expr= - 1000*m.b38 + m.x323 - m.x359 >= -1000)

m.c438 = Constraint(expr= - 1000*m.b39 + m.x326 - m.x362 >= -1000)

m.c439 = Constraint(expr= - 1000*m.b40 + m.x329 - m.x365 >= -1000)

m.c440 = Constraint(expr= - 1000*m.b41 + m.x389 - m.x407 >= -1000)

m.c441 = Constraint(expr= - 1000*m.b42 + m.x392 - m.x409 >= -1000)

m.c442 = Constraint(expr= - 1000*m.b43 + m.x395 - m.x411 >= -1000)

m.c443 = Constraint(expr= - 1000*m.b44 + m.x360 - m.x368 >= -1000)

m.c444 = Constraint(expr= - 1000*m.b45 + m.x363 - m.x371 >= -1000)

m.c445 = Constraint(expr= - 1000*m.b46 + m.x366 - m.x374 >= -1000)

m.c446 = Constraint(expr= - 1000*m.b38 + m.x323 - m.x359 <= 0)

m.c447 = Constraint(expr= - 1000*m.b39 + m.x326 - m.x362 <= 0)

m.c448 = Constraint(expr= - 1000*m.b40 + m.x329 - m.x365 <= 0)

m.c449 = Constraint(expr= - 1000*m.b41 + m.x389 - m.x407 <= 0)

m.c450 = Constraint(expr= - 1000*m.b42 + m.x392 - m.x409 <= 0)

m.c451 = Constraint(expr= - 1000*m.b43 + m.x395 - m.x411 <= 0)

m.c452 = Constraint(expr= - 1000*m.b44 + m.x360 - m.x368 <= 0)

m.c453 = Constraint(expr= - 1000*m.b45 + m.x363 - m.x371 <= 0)

m.c454 = Constraint(expr= - 1000*m.b46 + m.x366 - m.x374 <= 0)

m.c455 = Constraint(expr= - m.x284 + m.x359 >= 60)

m.c456 = Constraint(expr= - m.x285 + m.x362 >= 60)

m.c457 = Constraint(expr= - m.x286 + m.x365 >= 60)

m.c458 = Constraint(expr= - m.x287 + m.x359 >= 60)

m.c459 = Constraint(expr= - m.x288 + m.x362 >= 60)

m.c460 = Constraint(expr= - m.x289 + m.x365 >= 60)

m.c461 = Constraint(expr= - m.x290 + m.x398 >= 50)

m.c462 = Constraint(expr= - m.x291 + m.x400 >= 50)

m.c463 = Constraint(expr= - m.x292 + m.x402 >= 50)

m.c464 = Constraint(expr=60159.7666785*m.x209**2 - m.x212 == 0)

m.c465 = Constraint(expr=60159.7666785*m.x211**2 - m.x216 == 0)

m.c466 = Constraint(expr=60159.7666785*m.x213**2 - m.x220 == 0)

m.c467 = Constraint(expr=16103.4266989*m.x215**2 - m.x226 == 0)

m.c468 = Constraint(expr=16103.4266989*m.x217**2 - m.x232 == 0)

m.c469 = Constraint(expr=16103.4266989*m.x219**2 - m.x238 == 0)

m.c470 = Constraint(expr=16103.4266989*m.x221**2 - m.x244 == 0)

m.c471 = Constraint(expr=16103.4266989*m.x223**2 - m.x250 == 0)

m.c472 = Constraint(expr=16103.4266989*m.x225**2 - m.x256 == 0)

m.c473 = Constraint(expr=16103.4266989*m.x227**2 - m.x262 == 0)

m.c474 = Constraint(expr=16103.4266989*m.x229**2 - m.x268 == 0)

m.c475 = Constraint(expr=16103.4266989*m.x231**2 - m.x274 == 0)

m.c476 = Constraint(expr=16103.4266989*m.x233**2 - m.x280 == 0)

m.c477 = Constraint(expr=16103.4266989*m.x235**2 - m.x454 == 0)

m.c478 = Constraint(expr=16103.4266989*m.x237**2 - m.x457 == 0)

m.c479 = Constraint(expr=16103.4266989*m.x239**2 - m.x460 == 0)

m.c480 = Constraint(expr=16103.4266989*m.x241**2 - m.x49 == 0)

m.c481 = Constraint(expr=16103.4266989*m.x243**2 - m.x52 == 0)

m.c482 = Constraint(expr=16103.4266989*m.x245**2 - m.x55 == 0)

m.c483 = Constraint(expr=16103.4266989*m.x247**2 - m.x58 == 0)

m.c484 = Constraint(expr=16103.4266989*m.x249**2 - m.x61 == 0)

m.c485 = Constraint(expr=60159.7666785*m.x251**2 - m.x63 == 0)

m.c486 = Constraint(expr=60159.7666785*m.x253**2 - m.x65 == 0)

m.c487 = Constraint(expr=60159.7666785*m.x255**2 - m.x67 == 0)

m.c488 = Constraint(expr=2296.01902001*m.x257**2 - m.x69 == 0)

m.c489 = Constraint(expr=2296.01902001*m.x259**2 - m.x71 == 0)

m.c490 = Constraint(expr=2296.01902001*m.x261**2 - m.x73 == 0)

m.c491 = Constraint(expr=2296.01902001*m.x263**2 - m.x75 == 0)

m.c492 = Constraint(expr=2296.01902001*m.x265**2 - m.x77 == 0)

m.c493 = Constraint(expr=2296.01902001*m.x267**2 - m.x79 == 0)

m.c494 = Constraint(expr=2296.01902001*m.x269**2 - m.x81 == 0)

m.c495 = Constraint(expr=2296.01902001*m.x271**2 - m.x83 == 0)

m.c496 = Constraint(expr=2296.01902001*m.x273**2 - m.x85 == 0)

m.c497 = Constraint(expr=6324.78464025*m.x275**2 - m.x87 == 0)

m.c498 = Constraint(expr=6324.78464025*m.x277**2 - m.x89 == 0)

m.c499 = Constraint(expr=6324.78464025*m.x279**2 - m.x91 == 0)

m.c500 = Constraint(expr=2.4525*m.x209*m.x210 - m.x461 <= 0)

m.c501 = Constraint(expr=2.4525*m.x211*m.x214 - m.x462 <= 0)

m.c502 = Constraint(expr=2.4525*m.x213*m.x218 - m.x463 <= 0)

m.c503 = Constraint(expr=2.4525*m.x215*m.x224 - m.x464 <= 0)

m.c504 = Constraint(expr=2.4525*m.x217*m.x230 - m.x465 <= 0)

m.c505 = Constraint(expr=2.4525*m.x219*m.x236 - m.x466 <= 0)

m.c506 = Constraint(expr=2.4525*m.x221*m.x242 - m.x467 <= 0)

m.c507 = Constraint(expr=2.4525*m.x223*m.x248 - m.x468 <= 0)

m.c508 = Constraint(expr=2.4525*m.x225*m.x254 - m.x469 <= 0)

m.c509 = Constraint(expr=2.4525*m.x227*m.x260 - m.x470 <= 0)

m.c510 = Constraint(expr=2.4525*m.x229*m.x266 - m.x471 <= 0)

m.c511 = Constraint(expr=2.4525*m.x231*m.x272 - m.x472 <= 0)

m.c512 = Constraint(expr=2.4525*m.x233*m.x278 - m.x473 <= 0)

m.c513 = Constraint(expr=2.4525*m.x235*m.x453 - m.x474 <= 0)

m.c514 = Constraint(expr=2.4525*m.x237*m.x456 - m.x475 <= 0)

m.c515 = Constraint(expr=2.4525*m.x239*m.x459 - m.x476 <= 0)

m.c516 = Constraint(expr=2.4525*m.x48*m.x241 - m.x477 <= 0)

m.c517 = Constraint(expr=2.4525*m.x51*m.x243 - m.x478 <= 0)

m.c518 = Constraint(expr=2.4525*m.x54*m.x245 - m.x479 <= 0)

m.c519 = Constraint(expr=2.4525*m.x57*m.x247 - m.x480 <= 0)

m.c520 = Constraint(expr=2.4525*m.x60*m.x249 - m.x481 <= 0)

m.c521 = Constraint(expr=2.4525*m.x62*m.x251 - m.x482 <= 0)

m.c522 = Constraint(expr=2.4525*m.x64*m.x253 - m.x483 <= 0)

m.c523 = Constraint(expr=2.4525*m.x66*m.x255 - m.x484 <= 0)

m.c524 = Constraint(expr=2.4525*m.x68*m.x257 - m.x485 <= 0)

m.c525 = Constraint(expr=2.4525*m.x70*m.x259 - m.x486 <= 0)

m.c526 = Constraint(expr=2.4525*m.x72*m.x261 - m.x487 <= 0)

m.c527 = Constraint(expr=2.4525*m.x74*m.x263 - m.x488 <= 0)

m.c528 = Constraint(expr=2.4525*m.x76*m.x265 - m.x489 <= 0)

m.c529 = Constraint(expr=2.4525*m.x78*m.x267 - m.x490 <= 0)

m.c530 = Constraint(expr=2.4525*m.x80*m.x269 - m.x491 <= 0)

m.c531 = Constraint(expr=2.4525*m.x82*m.x271 - m.x492 <= 0)

m.c532 = Constraint(expr=2.4525*m.x84*m.x273 - m.x493 <= 0)

m.c533 = Constraint(expr=2.4525*m.x86*m.x275 - m.x494 <= 0)

m.c534 = Constraint(expr=2.4525*m.x88*m.x277 - m.x495 <= 0)

m.c535 = Constraint(expr=2.4525*m.x90*m.x279 - m.x496 <= 0)

m.c536 = Constraint(expr=SignPower(m.x92,2) - 0.107595782151047*m.x295 == 0)

m.c537 = Constraint(expr=SignPower(m.x94,2) - 0.107595782151047*m.x298 == 0)

m.c538 = Constraint(expr=SignPower(m.x96,2) - 0.107595782151047*m.x301 == 0)

m.c539 = Constraint(expr=SignPower(m.x98,2) - 0.000240846101592208*m.x303 == 0)

m.c540 = Constraint(expr=SignPower(m.x101,2) - 0.000240846101592208*m.x305 == 0)

m.c541 = Constraint(expr=SignPower(m.x104,2) - 0.000240846101592208*m.x307 == 0)

m.c542 = Constraint(expr=SignPower(m.x100,2) - 0.0011039398274554*m.x309 == 0)

m.c543 = Constraint(expr=SignPower(m.x103,2) - 0.0011039398274554*m.x311 == 0)

m.c544 = Constraint(expr=SignPower(m.x106,2) - 0.0011039398274554*m.x313 == 0)

m.c545 = Constraint(expr=SignPower(m.x128,2) - 0.0147658094299242*m.x316 == 0)

m.c546 = Constraint(expr=SignPower(m.x129,2) - 0.0147658094299242*m.x319 == 0)

m.c547 = Constraint(expr=SignPower(m.x130,2) - 0.0147658094299242*m.x322 == 0)

m.c548 = Constraint(expr=SignPower(m.x114,2) - 0.0126524872624481*m.x325 == 0)

m.c549 = Constraint(expr=SignPower(m.x117,2) - 0.0126524872624481*m.x328 == 0)

m.c550 = Constraint(expr=SignPower(m.x120,2) - 0.0126524872624481*m.x331 == 0)

m.c551 = Constraint(expr=SignPower(m.x113,2) - 0.000713164667292268*m.x332 == 0)

m.c552 = Constraint(expr=SignPower(m.x116,2) - 0.000713164667292268*m.x333 == 0)

m.c553 = Constraint(expr=SignPower(m.x119,2) - 0.000713164667292268*m.x334 == 0)

m.c554 = Constraint(expr=SignPower(m.x99,2) - 0.0253049745248962*m.x335 == 0)

m.c555 = Constraint(expr=SignPower(m.x102,2) - 0.0253049745248962*m.x336 == 0)

m.c556 = Constraint(expr=SignPower(m.x105,2) - 0.0253049745248962*m.x337 == 0)

m.c557 = Constraint(expr=SignPower(m.x146,2) - 0.0196735206566467*m.x338 == 0)

m.c558 = Constraint(expr=SignPower(m.x147,2) - 0.0196735206566467*m.x339 == 0)

m.c559 = Constraint(expr=SignPower(m.x148,2) - 0.0196735206566467*m.x340 == 0)

m.c560 = Constraint(expr=SignPower(m.x122,2) - 0.13436247753087*m.x341 == 0)

m.c561 = Constraint(expr=SignPower(m.x124,2) - 0.13436247753087*m.x342 == 0)

m.c562 = Constraint(expr=SignPower(m.x126,2) - 0.13436247753087*m.x343 == 0)

m.c563 = Constraint(expr=SignPower(m.x123,2) - 0.13436247753087*m.x344 == 0)

m.c564 = Constraint(expr=SignPower(m.x125,2) - 0.13436247753087*m.x345 == 0)

m.c565 = Constraint(expr=SignPower(m.x127,2) - 0.13436247753087*m.x346 == 0)

m.c566 = Constraint(expr=SignPower(m.x107,2) - 0.00268724955062101*m.x348 == 0)

m.c567 = Constraint(expr=SignPower(m.x108,2) - 0.00268724955062101*m.x350 == 0)

m.c568 = Constraint(expr=SignPower(m.x109,2) - 0.00268724955062101*m.x352 == 0)

m.c569 = Constraint(expr=SignPower(m.x110,2) - 0.00175817654162355*m.x354 == 0)

m.c570 = Constraint(expr=SignPower(m.x111,2) - 0.00175817654162355*m.x356 == 0)

m.c571 = Constraint(expr=SignPower(m.x112,2) - 0.00175817654162355*m.x358 == 0)

m.c572 = Constraint(expr=SignPower(m.x131,2) - 0.0156579704750926*m.x361 == 0)

m.c573 = Constraint(expr=SignPower(m.x136,2) - 0.0156579704750926*m.x364 == 0)

m.c574 = Constraint(expr=SignPower(m.x141,2) - 0.0156579704750926*m.x367 == 0)

m.c575 = Constraint(expr=SignPower(m.x149,2) - 0.4031634796292*m.x370 == 0)

m.c576 = Constraint(expr=SignPower(m.x150,2) - 0.4031634796292*m.x373 == 0)

m.c577 = Constraint(expr=SignPower(m.x151,2) - 0.4031634796292*m.x376 == 0)

m.c578 = Constraint(expr=SignPower(m.x152,2) - 0.4031634796292*m.x377 == 0)

m.c579 = Constraint(expr=SignPower(m.x154,2) - 0.4031634796292*m.x378 == 0)

m.c580 = Constraint(expr=SignPower(m.x156,2) - 0.4031634796292*m.x379 == 0)

m.c581 = Constraint(expr=SignPower(m.x158,2) - 8.06326959261651*m.x381 == 0)

m.c582 = Constraint(expr=SignPower(m.x161,2) - 8.06326959261651*m.x383 == 0)

m.c583 = Constraint(expr=SignPower(m.x164,2) - 8.06326959261651*m.x385 == 0)

m.c584 = Constraint(expr=SignPower(m.x159,2) - 8.06326959261651*m.x386 == 0)

m.c585 = Constraint(expr=SignPower(m.x162,2) - 8.06326959261651*m.x387 == 0)

m.c586 = Constraint(expr=SignPower(m.x165,2) - 8.06326959261651*m.x388 == 0)

m.c587 = Constraint(expr=SignPower(m.x167,2) - 0.000180519501834947*m.x391 == 0)

m.c588 = Constraint(expr=SignPower(m.x169,2) - 0.000180519501834947*m.x394 == 0)

m.c589 = Constraint(expr=SignPower(m.x171,2) - 0.000180519501834947*m.x397 == 0)

m.c590 = Constraint(expr=SignPower(m.x132,2) - 0.000180519501834947*m.x399 == 0)

m.c591 = Constraint(expr=SignPower(m.x137,2) - 0.000180519501834947*m.x401 == 0)

m.c592 = Constraint(expr=SignPower(m.x142,2) - 0.000180519501834947*m.x403 == 0)

m.c593 = Constraint(expr=SignPower(m.x173,2) - 0.013538962637621*m.x404 == 0)

m.c594 = Constraint(expr=SignPower(m.x174,2) - 0.013538962637621*m.x405 == 0)

m.c595 = Constraint(expr=SignPower(m.x175,2) - 0.013538962637621*m.x406 == 0)

m.c596 = Constraint(expr=SignPower(m.x133,2) - 0.0463936827608069*m.x408 == 0)

m.c597 = Constraint(expr=SignPower(m.x138,2) - 0.0463936827608069*m.x410 == 0)

m.c598 = Constraint(expr=SignPower(m.x143,2) - 0.0463936827608069*m.x412 == 0)

m.c599 = Constraint(expr=SignPower(m.x179,2) - 0.0964450219247959*m.x414 == 0)

m.c600 = Constraint(expr=SignPower(m.x180,2) - 0.0964450219247959*m.x416 == 0)

m.c601 = Constraint(expr=SignPower(m.x181,2) - 0.0964450219247959*m.x418 == 0)
