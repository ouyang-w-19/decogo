#  MINLP written by GAMS Convert at 04/21/18 13:55:15
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        392      207      101       84        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        327      297       30        0        0        0        0        0
#  FX      6        6        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1051      935      116        0
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
m.x32 = Var(within=Reals,bounds=(0,135.302691146811),initialize=0)
m.x33 = Var(within=Reals,bounds=(0.8,1.2),initialize=0.8)
m.x34 = Var(within=Reals,bounds=(148.299332771269,638.10455381568),initialize=148.299332771269)
m.x35 = Var(within=Reals,bounds=(0,135.302691146811),initialize=0)
m.x36 = Var(within=Reals,bounds=(0.8,1.2),initialize=0.8)
m.x37 = Var(within=Reals,bounds=(148.299332771269,638.10455381568),initialize=148.299332771269)
m.x38 = Var(within=Reals,bounds=(0,135.302691146811),initialize=0)
m.x39 = Var(within=Reals,bounds=(0.8,1.2),initialize=0.8)
m.x40 = Var(within=Reals,bounds=(148.299332771269,638.10455381568),initialize=148.299332771269)
m.x41 = Var(within=Reals,bounds=(0,135.302691146811),initialize=0)
m.x42 = Var(within=Reals,bounds=(287.427397827187,413.764247971),initialize=287.427397827187)
m.x43 = Var(within=Reals,bounds=(0,126.336850143813),initialize=0)
m.x44 = Var(within=Reals,bounds=(287.427397827187,413.764247971),initialize=287.427397827187)
m.x45 = Var(within=Reals,bounds=(0,126.336850143813),initialize=0)
m.x46 = Var(within=Reals,bounds=(74.1748123438468,106.777870451),initialize=74.1748123438468)
m.x47 = Var(within=Reals,bounds=(0,32.6030581071532),initialize=0)
m.x48 = Var(within=Reals,bounds=(74.1748123438468,106.777870451),initialize=74.1748123438468)
m.x49 = Var(within=Reals,bounds=(0,32.6030581071532),initialize=0)
m.x50 = Var(within=Reals,bounds=(74.1748123438468,106.777870451),initialize=74.1748123438468)
m.x51 = Var(within=Reals,bounds=(0,32.6030581071532),initialize=0)
m.x52 = Var(within=Reals,bounds=(74.1748123438468,106.777870451),initialize=74.1748123438468)
m.x53 = Var(within=Reals,bounds=(0,32.6030581071532),initialize=0)
m.x54 = Var(within=Reals,bounds=(74.1748123438468,106.777870451),initialize=74.1748123438468)
m.x55 = Var(within=Reals,bounds=(0,32.6030581071532),initialize=0)
m.x56 = Var(within=Reals,bounds=(74.1748123438468,106.777870451),initialize=74.1748123438468)
m.x57 = Var(within=Reals,bounds=(0,32.6030581071532),initialize=0)
m.x58 = Var(within=Reals,bounds=(74.1748123434975,106.777870452),initialize=74.1748123434975)
m.x59 = Var(within=Reals,bounds=(0,32.6030581085025),initialize=0)
m.x60 = Var(within=Reals,bounds=(74.1748123434975,106.777870452),initialize=74.1748123434975)
m.x61 = Var(within=Reals,bounds=(0,32.6030581085025),initialize=0)
m.x62 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x63 = Var(within=Reals,bounds=(0,0.64163),initialize=0)
m.x64 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x65 = Var(within=Reals,bounds=(0,0.64163),initialize=0)
m.x66 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x67 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x68 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x69 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x70 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x71 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x72 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x73 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x74 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x75 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x76 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x77 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x78 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x79 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x80 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x81 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x82 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x83 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x84 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x85 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x86 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x87 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x88 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x89 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x90 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x91 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x92 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x93 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x94 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x95 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x96 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x97 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x98 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x99 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x100 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x101 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x102 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x103 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x104 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x105 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x106 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x107 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x108 = Var(within=Reals,bounds=(0,0.429286),initialize=0)
m.x109 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x110 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x111 = Var(within=Reals,bounds=(0,0.429286),initialize=0)
m.x112 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x113 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x114 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x115 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x116 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x117 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x118 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x119 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x120 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x121 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x122 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x123 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x124 = Var(within=Reals,bounds=(6.3,6.3),initialize=6.3)
m.x125 = Var(within=Reals,bounds=(5,10),initialize=5)
m.x126 = Var(within=Reals,bounds=(5,10),initialize=5)
m.x127 = Var(within=Reals,bounds=(5,10),initialize=5)
m.x128 = Var(within=Reals,bounds=(4.6,4.6),initialize=4.6)
m.x129 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x130 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x131 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x132 = Var(within=Reals,bounds=(4.6,4.6),initialize=4.6)
m.x133 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x134 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x135 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x136 = Var(within=Reals,bounds=(10,10),initialize=10)
m.x137 = Var(within=Reals,bounds=(0,16.5),initialize=0)
m.x138 = Var(within=Reals,bounds=(0,16.5),initialize=0)
m.x139 = Var(within=Reals,bounds=(0,16.5),initialize=0)
m.x140 = Var(within=Reals,bounds=(0,0.045826),initialize=0)
m.x141 = Var(within=Reals,bounds=(287.427397827187,413.764247971),initialize=287.427397827187)
m.x142 = Var(within=Reals,bounds=(0,0.045826),initialize=0)
m.x143 = Var(within=Reals,bounds=(0,126.336850143813),initialize=0)
m.x144 = Var(within=Reals,bounds=(0,0.091663),initialize=0)
m.x145 = Var(within=Reals,bounds=(287.427397827187,413.764247971),initialize=287.427397827187)
m.x146 = Var(within=Reals,bounds=(0,0.091663),initialize=0)
m.x147 = Var(within=Reals,bounds=(0,126.336850143813),initialize=0)
m.x148 = Var(within=Reals,bounds=(0,0.091663),initialize=0)
m.x149 = Var(within=Reals,bounds=(0.8,1.2),initialize=0.8)
m.x150 = Var(within=Reals,bounds=(0,0.091663),initialize=0)
m.x151 = Var(within=Reals,bounds=(148.299332771269,638.10455381568),initialize=148.299332771269)
m.x152 = Var(within=Reals,bounds=(0,0.091663),initialize=0)
m.x153 = Var(within=Reals,bounds=(0,135.302691146811),initialize=0)
m.x154 = Var(within=Reals,bounds=(0,0.091663),initialize=0)
m.x155 = Var(within=Reals,bounds=(0.8,1.2),initialize=0.8)
m.x156 = Var(within=Reals,bounds=(0,0.091663),initialize=0)
m.x157 = Var(within=Reals,bounds=(148.299332771269,638.10455381568),initialize=148.299332771269)
m.x158 = Var(within=Reals,bounds=(0,0.091663),initialize=0)
m.x159 = Var(within=Reals,bounds=(0,135.302691146811),initialize=0)
m.x160 = Var(within=Reals,bounds=(0,0.091663),initialize=0)
m.x161 = Var(within=Reals,bounds=(0.8,1.2),initialize=0.8)
m.x162 = Var(within=Reals,bounds=(0,0.091663),initialize=0)
m.x163 = Var(within=Reals,bounds=(148.299332771269,638.10455381568),initialize=148.299332771269)
m.x164 = Var(within=Reals,bounds=(0,0.091663),initialize=0)
m.x165 = Var(within=Reals,bounds=(0,135.302691146811),initialize=0)
m.x166 = Var(within=Reals,bounds=(0,0.091663),initialize=0)
m.x167 = Var(within=Reals,bounds=(0.8,1.2),initialize=0.8)
m.x168 = Var(within=Reals,bounds=(0,0.045826),initialize=0)
m.x169 = Var(within=Reals,bounds=(148.299332771269,638.10455381568),initialize=148.299332771269)
m.x170 = Var(within=Reals,bounds=(0,0.045826),initialize=0)
m.x171 = Var(within=Reals,bounds=(0,135.302691146811),initialize=0)
m.x172 = Var(within=Reals,bounds=(0,0.119163),initialize=0)
m.x173 = Var(within=Reals,bounds=(0.8,1.2),initialize=0.8)
m.x174 = Var(within=Reals,bounds=(0,0.119163),initialize=0)
m.x175 = Var(within=Reals,bounds=(148.299332771269,638.10455381568),initialize=148.299332771269)
m.x176 = Var(within=Reals,bounds=(0,0.119163),initialize=0)
m.x177 = Var(within=Reals,bounds=(0,135.302691146811),initialize=0)
m.x178 = Var(within=Reals,bounds=(0,0.119163),initialize=0)
m.x179 = Var(within=Reals,bounds=(0.8,1.2),initialize=0.8)
m.x180 = Var(within=Reals,bounds=(0,0.119163),initialize=0)
m.x181 = Var(within=Reals,bounds=(148.299332771269,638.10455381568),initialize=148.299332771269)
m.x182 = Var(within=Reals,bounds=(0,0.119163),initialize=0)
m.x183 = Var(within=Reals,bounds=(0,135.302691146811),initialize=0)
m.x184 = Var(within=Reals,bounds=(0,0.071797),initialize=0)
m.x185 = Var(within=Reals,bounds=(0.8,1.2),initialize=0.8)
m.x186 = Var(within=Reals,bounds=(0,0.071797),initialize=0)
m.x187 = Var(within=Reals,bounds=(148.299332771269,638.10455381568),initialize=148.299332771269)
m.x188 = Var(within=Reals,bounds=(305,310),initialize=305)
m.x189 = Var(within=Reals,bounds=(305,310),initialize=305)
m.x190 = Var(within=Reals,bounds=(240,246),initialize=240)
m.x191 = Var(within=Reals,bounds=(240,246),initialize=240)
m.x192 = Var(within=Reals,bounds=(240,246),initialize=240)
m.x193 = Var(within=Reals,bounds=(240,246),initialize=240)
m.x194 = Var(within=Reals,bounds=(243,259.5),initialize=243)
m.x195 = Var(within=Reals,bounds=(243,259.5),initialize=243)
m.x196 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x197 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x198 = Var(within=Reals,bounds=(-232.35111544525,232.35111544525),initialize=0)
m.x199 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x200 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x201 = Var(within=Reals,bounds=(-232.35111544525,232.35111544525),initialize=0)
m.x202 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x203 = Var(within=Reals,bounds=(-103800.7251715,103800.7251715),initialize=0)
m.x204 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x205 = Var(within=Reals,bounds=(-103800.7251715,103800.7251715),initialize=0)
m.x206 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x207 = Var(within=Reals,bounds=(-22646.161845275,22646.161845275),initialize=0)
m.x208 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x209 = Var(within=Reals,bounds=(-22646.161845275,22646.161845275),initialize=0)
m.x210 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x211 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x212 = Var(within=Reals,bounds=(-1693.1005454625,1693.1005454625),initialize=0)
m.x213 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x214 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x215 = Var(within=Reals,bounds=(-1693.1005454625,1693.1005454625),initialize=0)
m.x216 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x217 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x218 = Var(within=Reals,bounds=(-1975.896081255,1975.896081255),initialize=0)
m.x219 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x220 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x221 = Var(within=Reals,bounds=(-1975.896081255,1975.896081255),initialize=0)
m.x222 = Var(within=Reals,bounds=(-35055.017651,35055.017651),initialize=0)
m.x223 = Var(within=Reals,bounds=(-35055.017651,35055.017651),initialize=0)
m.x224 = Var(within=Reals,bounds=(-987.9480406275,987.9480406275),initialize=0)
m.x225 = Var(within=Reals,bounds=(-987.9480406275,987.9480406275),initialize=0)
m.x226 = Var(within=Reals,bounds=(-1270.74357642,1270.74357642),initialize=0)
m.x227 = Var(within=Reals,bounds=(-1270.74357642,1270.74357642),initialize=0)
m.x228 = Var(within=Reals,bounds=(-186.06385100525,186.06385100525),initialize=0)
m.x229 = Var(within=Reals,bounds=(-186.06385100525,186.06385100525),initialize=0)
m.x230 = Var(within=Reals,bounds=(-186.06385100525,186.06385100525),initialize=0)
m.x231 = Var(within=Reals,bounds=(-186.06385100525,186.06385100525),initialize=0)
m.x232 = Var(within=Reals,bounds=(214.9,1000),initialize=214.9)
m.x233 = Var(within=Reals,bounds=(-9303.19255025,9303.19255025),initialize=0)
m.x234 = Var(within=Reals,bounds=(214.9,1000),initialize=214.9)
m.x235 = Var(within=Reals,bounds=(-9303.19255025,9303.19255025),initialize=0)
m.x236 = Var(within=Reals,bounds=(231.04,1000),initialize=231.04)
m.x237 = Var(within=Reals,bounds=(-14219.27742075,14219.27742075),initialize=0)
m.x238 = Var(within=Reals,bounds=(231.04,1000),initialize=231.04)
m.x239 = Var(within=Reals,bounds=(-14219.27742075,14219.27742075),initialize=0)
m.x240 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x241 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x242 = Var(within=Reals,bounds=(-1596.630932455,1596.630932455),initialize=0)
m.x243 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x244 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x245 = Var(within=Reals,bounds=(-1596.630932455,1596.630932455),initialize=0)
m.x246 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x247 = Var(within=Reals,bounds=(300,1000),initialize=300)
m.x248 = Var(within=Reals,bounds=(-62.00958485375,62.00958485375),initialize=0)
m.x249 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x250 = Var(within=Reals,bounds=(300,1000),initialize=300)
m.x251 = Var(within=Reals,bounds=(-62.00958485375,62.00958485375),initialize=0)
m.x252 = Var(within=Reals,bounds=(-62.00958485375,62.00958485375),initialize=0)
m.x253 = Var(within=Reals,bounds=(-62.00958485375,62.00958485375),initialize=0)
m.x254 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x255 = Var(within=Reals,bounds=(-3.100479242675,3.100479242675),initialize=0)
m.x256 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x257 = Var(within=Reals,bounds=(-3.100479242675,3.100479242675),initialize=0)
m.x258 = Var(within=Reals,bounds=(-3.100479242675,3.100479242675),initialize=0)
m.x259 = Var(within=Reals,bounds=(-3.100479242675,3.100479242675),initialize=0)
m.x260 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x261 = Var(within=Reals,bounds=(243,1000),initialize=243)
m.x262 = Var(within=Reals,bounds=(-138489.1922805,138489.1922805),initialize=0)
m.x263 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x264 = Var(within=Reals,bounds=(243,1000),initialize=243)
m.x265 = Var(within=Reals,bounds=(-138489.1922805,138489.1922805),initialize=0)
m.x266 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x267 = Var(within=Reals,bounds=(-138489.1922805,138489.1922805),initialize=0)
m.x268 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x269 = Var(within=Reals,bounds=(-138489.1922805,138489.1922805),initialize=0)
m.x270 = Var(within=Reals,bounds=(-1846.52256374,1846.52256374),initialize=0)
m.x271 = Var(within=Reals,bounds=(-1846.52256374,1846.52256374),initialize=0)
m.x272 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x273 = Var(within=Reals,bounds=(-538.866468715,538.866468715),initialize=0)
m.x274 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x275 = Var(within=Reals,bounds=(-538.866468715,538.866468715),initialize=0)
m.x276 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x277 = Var(within=Reals,bounds=(-259.21503776,259.21503776),initialize=0)
m.x278 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x279 = Var(within=Reals,bounds=(-259.21503776,259.21503776),initialize=0)
m.x280 = Var(within=Reals,bounds=(34.1,34.1),initialize=34.1)
m.x281 = Var(within=Reals,bounds=(-34.1,1000),initialize=0)
m.x282 = Var(within=Reals,bounds=(34.1,34.1),initialize=34.1)
m.x283 = Var(within=Reals,bounds=(-34.1,1000),initialize=0)
m.x284 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x285 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x286 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x287 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x288 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x289 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x290 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x291 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x292 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x293 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x294 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x295 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x296 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x297 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x298 = Var(within=Reals,bounds=(0,135.302691146811),initialize=0)
m.x299 = Var(within=Reals,bounds=(0.8,1.2),initialize=0.8)
m.x300 = Var(within=Reals,bounds=(148.299332771269,638.10455381568),initialize=148.299332771269)
m.x301 = Var(within=Reals,bounds=(0,135.302691146811),initialize=0)
m.x302 = Var(within=Reals,bounds=(0.8,1.2),initialize=0.8)
m.x303 = Var(within=Reals,bounds=(148.299332771269,638.10455381568),initialize=148.299332771269)
m.x304 = Var(within=Reals,bounds=(0,46.5022459484905),initialize=0)
m.x305 = Var(within=Reals,bounds=(0,46.5022459484905),initialize=0)
m.x306 = Var(within=Reals,bounds=(0,143.448141849487),initialize=0)
m.x307 = Var(within=Reals,bounds=(0,143.448141849487),initialize=0)
m.x308 = Var(within=Reals,bounds=(0,143.448141849487),initialize=0)
m.x309 = Var(within=Reals,bounds=(0,143.448141849487),initialize=0)
m.x310 = Var(within=Reals,bounds=(0,143.448141849487),initialize=0)
m.x311 = Var(within=Reals,bounds=(0,143.448141849487),initialize=0)
m.x312 = Var(within=Reals,bounds=(0,143.448141849487),initialize=0)
m.x313 = Var(within=Reals,bounds=(0,143.448141849487),initialize=0)
m.x314 = Var(within=Reals,bounds=(0,143.448141849487),initialize=0)
m.x315 = Var(within=Reals,bounds=(0,143.448141849487),initialize=0)
m.x316 = Var(within=Reals,bounds=(0,143.448141849487),initialize=0)
m.x317 = Var(within=Reals,bounds=(0,143.448141849487),initialize=0)
m.x318 = Var(within=Reals,bounds=(0,46.5022459484905),initialize=0)
m.x319 = Var(within=Reals,bounds=(0,46.5022459484905),initialize=0)
m.x320 = Var(within=Reals,bounds=(0,31.205539800995),initialize=0)
m.x321 = Var(within=Reals,bounds=(0,31.205539800995),initialize=0)
m.x322 = Var(within=Reals,bounds=(0,31.205539800995),initialize=0)
m.x323 = Var(within=Reals,bounds=(0,31.205539800995),initialize=0)
m.x324 = Var(within=Reals,bounds=(0,31.205539800995),initialize=0)
m.x325 = Var(within=Reals,bounds=(0,31.205539800995),initialize=0)
m.x326 = Var(within=Reals,bounds=(0,18.8016762007756),initialize=0)
m.x327 = Var(within=Reals,bounds=(0,18.8016762007756),initialize=0)

m.obj = Objective(expr=   20*m.x286 + 20*m.x287 + 20*m.x288 + 20*m.x289 + 20*m.x290 + 20*m.x291 + 20*m.x292 + 20*m.x293
                        + 20*m.x294 + 20*m.x295 + 20*m.x296 + 20*m.x297 + m.x304 + m.x305 + m.x306 + m.x307 + m.x308
                        + m.x309 + m.x310 + m.x311 + m.x312 + m.x313 + m.x314 + m.x315 + m.x316 + m.x317 + m.x318
                        + m.x319 + m.x320 + m.x321 + m.x322 + m.x323 + m.x324 + m.x325 + m.x326 + m.x327
                       , sense=minimize)

m.c2 = Constraint(expr=   m.x141 + m.x143 == 413.764247971)

m.c3 = Constraint(expr=   m.x145 + m.x147 == 413.764247971)

m.c4 = Constraint(expr= - 443.128162372*m.x149 + m.x151 + m.x153 == 0)

m.c5 = Constraint(expr= - 443.128162372*m.x155 + m.x157 + m.x159 == 0)

m.c6 = Constraint(expr= - 443.128162372*m.x161 + m.x163 + m.x165 == 0)

m.c7 = Constraint(expr= - 443.128162372*m.x167 + m.x169 + m.x171 == 0)

m.c8 = Constraint(expr= - 443.128162372*m.x173 + m.x175 + m.x177 == 0)

m.c9 = Constraint(expr= - 443.128162372*m.x179 + m.x181 + m.x183 == 0)

m.c10 = Constraint(expr= - 443.128162372*m.x185 + m.x187 + m.x298 == 0)

m.c11 = Constraint(expr= - 443.128162372*m.x299 + m.x300 + m.x301 == 0)

m.c12 = Constraint(expr=   m.x32 - 443.128162372*m.x302 + m.x303 == 0)

m.c13 = Constraint(expr= - 443.128162372*m.x33 + m.x34 + m.x35 == 0)

m.c14 = Constraint(expr= - 443.128162372*m.x36 + m.x37 + m.x38 == 0)

m.c15 = Constraint(expr= - 443.128162372*m.x39 + m.x40 + m.x41 == 0)

m.c16 = Constraint(expr=   m.x42 + m.x43 == 413.764247971)

m.c17 = Constraint(expr=   m.x44 + m.x45 == 413.764247971)

m.c18 = Constraint(expr=   m.x46 + m.x47 == 106.777870451)

m.c19 = Constraint(expr=   m.x48 + m.x49 == 106.777870451)

m.c20 = Constraint(expr=   m.x50 + m.x51 == 106.777870451)

m.c21 = Constraint(expr=   m.x52 + m.x53 == 106.777870451)

m.c22 = Constraint(expr=   m.x54 + m.x55 == 106.777870451)

m.c23 = Constraint(expr=   m.x56 + m.x57 == 106.777870451)

m.c24 = Constraint(expr=   m.x58 + m.x59 == 106.777870452)

m.c25 = Constraint(expr=   m.x60 + m.x61 == 106.777870452)

m.c26 = Constraint(expr= - m.x62 + m.x63 == 0)

m.c27 = Constraint(expr= - m.x64 + m.x65 == 0)

m.c28 = Constraint(expr=   m.x62 - m.x66 - m.x67 - m.x68 == 0)

m.c29 = Constraint(expr=   m.x64 - m.x69 - m.x70 - m.x71 == 0)

m.c30 = Constraint(expr=   m.x72 == 0.025)

m.c31 = Constraint(expr=   m.x73 == 0.025)

m.c32 = Constraint(expr=   m.x74 == 0.013)

m.c33 = Constraint(expr=   m.x75 == 0.012)

m.c34 = Constraint(expr=   m.x76 + m.x77 - m.x78 == 0)

m.c35 = Constraint(expr=   m.x79 + m.x80 - m.x81 == 0)

m.c36 = Constraint(expr=   m.x68 - m.x76 + m.x82 - m.x83 == 0)

m.c37 = Constraint(expr=   m.x71 - m.x79 + m.x84 - m.x85 == 0)

m.c38 = Constraint(expr=   m.x67 - m.x86 == 0)

m.c39 = Constraint(expr=   m.x70 - m.x87 == 0)

m.c40 = Constraint(expr=   m.x78 + m.x88 + m.x89 + m.x90 - m.x91 - m.x92 == 0)

m.c41 = Constraint(expr=   m.x81 + m.x93 + m.x94 + m.x95 - m.x96 - m.x97 == 0)

m.c42 = Constraint(expr= - m.x72 + m.x83 + m.x86 - m.x98 == 0)

m.c43 = Constraint(expr= - m.x73 + m.x85 + m.x87 - m.x99 == 0)

m.c44 = Constraint(expr= - m.x74 - m.x77 + m.x98 == 0)

m.c45 = Constraint(expr= - m.x75 - m.x80 + m.x99 == 0)

m.c46 = Constraint(expr=   m.x66 - m.x82 == 0)

m.c47 = Constraint(expr=   m.x69 - m.x84 == 0)

m.c48 = Constraint(expr= - m.x100 == 0.1624)

m.c49 = Constraint(expr= - m.x101 == 0.1616)

m.c50 = Constraint(expr=   m.x100 - m.x102 + m.x103 == 0)

m.c51 = Constraint(expr=   m.x101 - m.x104 + m.x105 == 0)

m.c52 = Constraint(expr=   m.x106 + m.x107 - m.x108 == 0)

m.c53 = Constraint(expr=   m.x109 + m.x110 - m.x111 == 0)

m.c54 = Constraint(expr=   m.x108 + m.x112 - m.x113 == 0)

m.c55 = Constraint(expr=   m.x111 + m.x114 - m.x115 == 0)

m.c56 = Constraint(expr= - m.x112 - m.x116 == 0.0138888888888889)

m.c57 = Constraint(expr= - m.x114 - m.x117 == 0.0138888888888889)

m.c58 = Constraint(expr= - m.x89 + m.x116 - m.x118 == 0)

m.c59 = Constraint(expr= - m.x94 + m.x117 - m.x119 == 0)

m.c60 = Constraint(expr=   m.x120 == 0)

m.c61 = Constraint(expr=   m.x121 == 0)

m.c62 = Constraint(expr= - m.x90 + m.x113 == 0)

m.c63 = Constraint(expr= - m.x95 + m.x115 == 0)

m.c64 = Constraint(expr= - m.x88 - m.x103 == 0)

m.c65 = Constraint(expr= - m.x93 - m.x105 == 0)

m.c66 = Constraint(expr= - m.x63 + m.x122 == 0)

m.c67 = Constraint(expr= - m.x65 + m.x123 == 0)

m.c68 = Constraint(expr=   3600*m.x102 + 239.978718892*m.x124 - 239.978718892*m.x125 == 0)

m.c69 = Constraint(expr=   3600*m.x104 + 239.978718892*m.x126 - 239.978718892*m.x127 == 0)

m.c70 = Constraint(expr=   3600*m.x91 - 3600*m.x106 + 416.560177655*m.x128 - 416.560177655*m.x129 == 0)

m.c71 = Constraint(expr=   3600*m.x96 - 3600*m.x109 + 416.560177655*m.x130 - 416.560177655*m.x131 == 0)

m.c72 = Constraint(expr=   3600*m.x92 - 3600*m.x107 + 416.560177655*m.x132 - 416.560177655*m.x133 == 0)

m.c73 = Constraint(expr=   3600*m.x97 - 3600*m.x110 + 416.560177655*m.x134 - 416.560177655*m.x135 == 0)

m.c74 = Constraint(expr=   3600*m.x118 - 3600*m.x120 + 165.129961038*m.x136 - 165.129961038*m.x137 == 0)

m.c75 = Constraint(expr=   3600*m.x119 - 3600*m.x121 + 165.129961038*m.x138 - 165.129961038*m.x139 == 0)

m.c76 = Constraint(expr= - m.x125 + m.x126 == 0)

m.c77 = Constraint(expr= - m.x129 + m.x130 == 0)

m.c78 = Constraint(expr= - m.x133 + m.x134 == 0)

m.c79 = Constraint(expr= - m.x137 + m.x138 == 0)

m.c80 = Constraint(expr= - 0.037494*m.b2 + m.x140 >= 0)

m.c81 = Constraint(expr= - 0.037494*m.b3 + m.x142 >= 0)

m.c82 = Constraint(expr= - 0.074997*m.b4 + m.x144 >= 0)

m.c83 = Constraint(expr= - 0.074997*m.b5 + m.x146 >= 0)

m.c84 = Constraint(expr= - 0.074997*m.b6 + m.x148 >= 0)

m.c85 = Constraint(expr= - 0.074997*m.b7 + m.x150 >= 0)

m.c86 = Constraint(expr= - 0.074997*m.b8 + m.x152 >= 0)

m.c87 = Constraint(expr= - 0.074997*m.b9 + m.x154 >= 0)

m.c88 = Constraint(expr= - 0.074997*m.b10 + m.x156 >= 0)

m.c89 = Constraint(expr= - 0.074997*m.b11 + m.x158 >= 0)

m.c90 = Constraint(expr= - 0.074997*m.b12 + m.x160 >= 0)

m.c91 = Constraint(expr= - 0.074997*m.b13 + m.x162 >= 0)

m.c92 = Constraint(expr= - 0.074997*m.b14 + m.x164 >= 0)

m.c93 = Constraint(expr= - 0.074997*m.b15 + m.x166 >= 0)

m.c94 = Constraint(expr= - 0.037494*m.b16 + m.x168 >= 0)

m.c95 = Constraint(expr= - 0.037494*m.b17 + m.x170 >= 0)

m.c96 = Constraint(expr= - 0.097497*m.b18 + m.x172 >= 0)

m.c97 = Constraint(expr= - 0.097497*m.b19 + m.x174 >= 0)

m.c98 = Constraint(expr= - 0.097497*m.b20 + m.x176 >= 0)

m.c99 = Constraint(expr= - 0.097497*m.b21 + m.x178 >= 0)

m.c100 = Constraint(expr= - 0.097497*m.b22 + m.x180 >= 0)

m.c101 = Constraint(expr= - 0.097497*m.b23 + m.x182 >= 0)

m.c102 = Constraint(expr= - 0.058743*m.b24 + m.x184 >= 0)

m.c103 = Constraint(expr= - 0.058743*m.b25 + m.x186 >= 0)

m.c104 = Constraint(expr= - 0.045826*m.b2 + m.x140 <= 0)

m.c105 = Constraint(expr= - 0.045826*m.b3 + m.x142 <= 0)

m.c106 = Constraint(expr= - 0.091663*m.b4 + m.x144 <= 0)

m.c107 = Constraint(expr= - 0.091663*m.b5 + m.x146 <= 0)

m.c108 = Constraint(expr= - 0.091663*m.b6 + m.x148 <= 0)

m.c109 = Constraint(expr= - 0.091663*m.b7 + m.x150 <= 0)

m.c110 = Constraint(expr= - 0.091663*m.b8 + m.x152 <= 0)

m.c111 = Constraint(expr= - 0.091663*m.b9 + m.x154 <= 0)

m.c112 = Constraint(expr= - 0.091663*m.b10 + m.x156 <= 0)

m.c113 = Constraint(expr= - 0.091663*m.b11 + m.x158 <= 0)

m.c114 = Constraint(expr= - 0.091663*m.b12 + m.x160 <= 0)

m.c115 = Constraint(expr= - 0.091663*m.b13 + m.x162 <= 0)

m.c116 = Constraint(expr= - 0.091663*m.b14 + m.x164 <= 0)

m.c117 = Constraint(expr= - 0.091663*m.b15 + m.x166 <= 0)

m.c118 = Constraint(expr= - 0.045826*m.b16 + m.x168 <= 0)

m.c119 = Constraint(expr= - 0.045826*m.b17 + m.x170 <= 0)

m.c120 = Constraint(expr= - 0.119163*m.b18 + m.x172 <= 0)

m.c121 = Constraint(expr= - 0.119163*m.b19 + m.x174 <= 0)

m.c122 = Constraint(expr= - 0.119163*m.b20 + m.x176 <= 0)

m.c123 = Constraint(expr= - 0.119163*m.b21 + m.x178 <= 0)

m.c124 = Constraint(expr= - 0.119163*m.b22 + m.x180 <= 0)

m.c125 = Constraint(expr= - 0.119163*m.b23 + m.x182 <= 0)

m.c126 = Constraint(expr= - 0.071797*m.b24 + m.x184 <= 0)

m.c127 = Constraint(expr= - 0.071797*m.b25 + m.x186 <= 0)

m.c128 = Constraint(expr= - m.x124 + m.x188 == 300)

m.c129 = Constraint(expr= - m.x126 + m.x189 == 300)

m.c130 = Constraint(expr= - m.x128 + m.x190 == 240)

m.c131 = Constraint(expr= - m.x130 + m.x191 == 240)

m.c132 = Constraint(expr= - m.x132 + m.x192 == 240)

m.c133 = Constraint(expr= - m.x134 + m.x193 == 240)

m.c134 = Constraint(expr= - m.x136 + m.x194 == 243)

m.c135 = Constraint(expr= - m.x138 + m.x195 == 243)

m.c136 = Constraint(expr=   m.x196 - m.x197 - m.x198 == 0)

m.c137 = Constraint(expr=   m.x199 - m.x200 - m.x201 == 0)

m.c138 = Constraint(expr=   m.x197 - m.x202 - m.x203 == 0)

m.c139 = Constraint(expr=   m.x200 - m.x204 - m.x205 == 0)

m.c140 = Constraint(expr=   m.x197 - m.x206 - m.x207 == 0)

m.c141 = Constraint(expr=   m.x200 - m.x208 - m.x209 == 0)

m.c142 = Constraint(expr=   m.x210 - m.x211 - m.x212 == 0)

m.c143 = Constraint(expr=   m.x213 - m.x214 - m.x215 == 0)

m.c144 = Constraint(expr= - m.x216 + m.x217 - m.x218 == 0)

m.c145 = Constraint(expr= - m.x219 + m.x220 - m.x221 == 0)

m.c146 = Constraint(expr=   m.x206 - m.x216 - m.x222 == 0)

m.c147 = Constraint(expr=   m.x208 - m.x219 - m.x223 == 0)

m.c148 = Constraint(expr=   m.x197 - m.x210 - m.x224 == 0)

m.c149 = Constraint(expr=   m.x200 - m.x213 - m.x225 == 0)

m.c150 = Constraint(expr=   m.x211 - m.x217 - m.x226 == 0)

m.c151 = Constraint(expr=   m.x214 - m.x220 - m.x227 == 0)

m.c152 = Constraint(expr=   m.x202 - m.x206 - m.x228 == 0)

m.c153 = Constraint(expr=   m.x204 - m.x208 - m.x229 == 0)

m.c154 = Constraint(expr=   m.x206 - m.x211 - m.x230 == 0)

m.c155 = Constraint(expr=   m.x208 - m.x214 - m.x231 == 0)

m.c156 = Constraint(expr=   m.x211 - m.x232 - m.x233 == 0)

m.c157 = Constraint(expr=   m.x214 - m.x234 - m.x235 == 0)

m.c158 = Constraint(expr=   m.x217 - m.x236 - m.x237 == 0)

m.c159 = Constraint(expr=   m.x220 - m.x238 - m.x239 == 0)

m.c160 = Constraint(expr= - m.x240 + m.x241 - m.x242 == 0)

m.c161 = Constraint(expr= - m.x243 + m.x244 - m.x245 == 0)

m.c162 = Constraint(expr= - m.x246 + m.x247 - m.x248 == 0)

m.c163 = Constraint(expr= - m.x249 + m.x250 - m.x251 == 0)

m.c164 = Constraint(expr= - m.x188 + m.x246 - m.x252 == 0)

m.c165 = Constraint(expr= - m.x189 + m.x249 - m.x253 == 0)

m.c166 = Constraint(expr=   m.x190 - m.x254 - m.x255 == 0)

m.c167 = Constraint(expr=   m.x191 - m.x256 - m.x257 == 0)

m.c168 = Constraint(expr=   m.x192 - m.x254 - m.x258 == 0)

m.c169 = Constraint(expr=   m.x193 - m.x256 - m.x259 == 0)

m.c170 = Constraint(expr= - m.x260 + m.x261 - m.x262 == 0)

m.c171 = Constraint(expr= - m.x263 + m.x264 - m.x265 == 0)

m.c172 = Constraint(expr= - m.x240 + m.x266 - m.x267 == 0)

m.c173 = Constraint(expr= - m.x243 + m.x268 - m.x269 == 0)

m.c174 = Constraint(expr=   m.x261 - m.x266 - m.x270 == 0)

m.c175 = Constraint(expr=   m.x264 - m.x268 - m.x271 == 0)

m.c176 = Constraint(expr= - m.x240 + m.x272 - m.x273 == 0)

m.c177 = Constraint(expr= - m.x243 + m.x274 - m.x275 == 0)

m.c178 = Constraint(expr=   m.x194 - m.x276 - m.x277 == 0)

m.c179 = Constraint(expr=   m.x195 - m.x278 - m.x279 == 0)

m.c180 = Constraint(expr=   m.x196 - m.x280 - m.x281 == 0)

m.c181 = Constraint(expr=   m.x199 - m.x282 - m.x283 == 0)

m.c182 = Constraint(expr= - m.x254 + m.x260 - m.x284 == 0)

m.c183 = Constraint(expr= - m.x256 + m.x263 - m.x285 == 0)

m.c184 = Constraint(expr= - 239.978718892*m.x124 + 239.978718892*m.x127 - 416.560177655*m.x128 + 416.560177655*m.x131
                          - 416.560177655*m.x132 + 416.560177655*m.x135 - 165.129961038*m.x136 + 165.129961038*m.x139
                          >= 0)

m.c185 = Constraint(expr=   m.b2 - m.b16 >= 0)

m.c186 = Constraint(expr=   m.b3 - m.b17 >= 0)

m.c187 = Constraint(expr=   m.b4 - m.b6 >= 0)

m.c188 = Constraint(expr=   m.b5 - m.b7 >= 0)

m.c189 = Constraint(expr=   m.b6 - m.b8 >= 0)

m.c190 = Constraint(expr=   m.b7 - m.b9 >= 0)

m.c191 = Constraint(expr=   m.b8 - m.b10 >= 0)

m.c192 = Constraint(expr=   m.b9 - m.b11 >= 0)

m.c193 = Constraint(expr=   m.b10 - m.b12 >= 0)

m.c194 = Constraint(expr=   m.b11 - m.b13 >= 0)

m.c195 = Constraint(expr=   m.b12 - m.b14 >= 0)

m.c196 = Constraint(expr=   m.b13 - m.b15 >= 0)

m.c197 = Constraint(expr=   m.b18 - m.b20 >= 0)

m.c198 = Constraint(expr=   m.b19 - m.b21 >= 0)

m.c199 = Constraint(expr=   m.b20 - m.b22 >= 0)

m.c200 = Constraint(expr=   m.b21 - m.b23 >= 0)

m.c201 = Constraint(expr=   m.x63 - m.x140 - m.x144 - m.x148 - m.x152 - m.x156 - m.x160 - m.x164 - m.x168 == 0)

m.c202 = Constraint(expr=   m.x65 - m.x142 - m.x146 - m.x150 - m.x154 - m.x158 - m.x162 - m.x166 - m.x170 == 0)

m.c203 = Constraint(expr=   m.x108 - m.x172 - m.x176 - m.x180 - m.x184 == 0)

m.c204 = Constraint(expr=   m.x111 - m.x174 - m.x178 - m.x182 - m.x186 == 0)

m.c205 = Constraint(expr= - 712.572602172813*m.b2 + m.x141 - m.x281 >= -712.572602172813)

m.c206 = Constraint(expr= - 712.572602172813*m.b3 + m.x145 - m.x283 >= -712.572602172813)

m.c207 = Constraint(expr= - 851.700667228731*m.b4 + m.x151 - m.x281 >= -851.700667228731)

m.c208 = Constraint(expr= - 851.700667228731*m.b5 + m.x157 - m.x283 >= -851.700667228731)

m.c209 = Constraint(expr= - 851.700667228731*m.b6 + m.x163 - m.x281 >= -851.700667228731)

m.c210 = Constraint(expr= - 851.700667228731*m.b7 + m.x169 - m.x283 >= -851.700667228731)

m.c211 = Constraint(expr= - 851.700667228731*m.b8 + m.x175 - m.x281 >= -851.700667228731)

m.c212 = Constraint(expr= - 851.700667228731*m.b9 + m.x181 - m.x283 >= -851.700667228731)

m.c213 = Constraint(expr= - 851.700667228731*m.b10 + m.x187 - m.x281 >= -851.700667228731)

m.c214 = Constraint(expr= - 851.700667228731*m.b11 - m.x283 + m.x300 >= -851.700667228731)

m.c215 = Constraint(expr= - 851.700667228731*m.b12 - m.x281 + m.x303 >= -851.700667228731)

m.c216 = Constraint(expr= - 851.700667228731*m.b13 + m.x34 - m.x283 >= -851.700667228731)

m.c217 = Constraint(expr= - 851.700667228731*m.b14 + m.x37 - m.x281 >= -851.700667228731)

m.c218 = Constraint(expr= - 851.700667228731*m.b15 + m.x40 - m.x283 >= -851.700667228731)

m.c219 = Constraint(expr= - 712.572602172813*m.b16 + m.x42 - m.x281 >= -712.572602172813)

m.c220 = Constraint(expr= - 712.572602172813*m.b17 + m.x44 - m.x283 >= -712.572602172813)

m.c221 = Constraint(expr= - 925.825187656153*m.b18 + m.x46 - m.x284 >= -925.825187656153)

m.c222 = Constraint(expr= - 925.825187656153*m.b19 + m.x48 - m.x285 >= -925.825187656153)

m.c223 = Constraint(expr= - 925.825187656153*m.b20 + m.x50 - m.x284 >= -925.825187656153)

m.c224 = Constraint(expr= - 925.825187656153*m.b21 + m.x52 - m.x285 >= -925.825187656153)

m.c225 = Constraint(expr= - 925.825187656153*m.b22 + m.x54 - m.x284 >= -925.825187656153)

m.c226 = Constraint(expr= - 925.825187656153*m.b23 + m.x56 - m.x285 >= -925.825187656153)

m.c227 = Constraint(expr= - 925.825187656502*m.b24 + m.x58 - m.x284 >= -925.825187656502)

m.c228 = Constraint(expr= - 925.825187656502*m.b25 + m.x60 - m.x285 >= -925.825187656502)

m.c229 = Constraint(expr=   447.864247971*m.b2 + m.x141 - m.x281 <= 447.864247971)

m.c230 = Constraint(expr=   447.864247971*m.b3 + m.x145 - m.x283 <= 447.864247971)

m.c231 = Constraint(expr=   672.20455381568*m.b4 + m.x151 - m.x281 <= 672.20455381568)

m.c232 = Constraint(expr=   672.20455381568*m.b5 + m.x157 - m.x283 <= 672.20455381568)

m.c233 = Constraint(expr=   672.20455381568*m.b6 + m.x163 - m.x281 <= 672.20455381568)

m.c234 = Constraint(expr=   672.20455381568*m.b7 + m.x169 - m.x283 <= 672.20455381568)

m.c235 = Constraint(expr=   672.20455381568*m.b8 + m.x175 - m.x281 <= 672.20455381568)

m.c236 = Constraint(expr=   672.20455381568*m.b9 + m.x181 - m.x283 <= 672.20455381568)

m.c237 = Constraint(expr=   672.20455381568*m.b10 + m.x187 - m.x281 <= 672.20455381568)

m.c238 = Constraint(expr=   672.20455381568*m.b11 - m.x283 + m.x300 <= 672.20455381568)

m.c239 = Constraint(expr=   672.20455381568*m.b12 - m.x281 + m.x303 <= 672.20455381568)

m.c240 = Constraint(expr=   672.20455381568*m.b13 + m.x34 - m.x283 <= 672.20455381568)

m.c241 = Constraint(expr=   672.20455381568*m.b14 + m.x37 - m.x281 <= 672.20455381568)

m.c242 = Constraint(expr=   672.20455381568*m.b15 + m.x40 - m.x283 <= 672.20455381568)

m.c243 = Constraint(expr=   447.864247971*m.b16 + m.x42 - m.x281 <= 447.864247971)

m.c244 = Constraint(expr=   447.864247971*m.b17 + m.x44 - m.x283 <= 447.864247971)

m.c245 = Constraint(expr=   1106.777870451*m.b18 + m.x46 - m.x284 <= 1106.777870451)

m.c246 = Constraint(expr=   1106.777870451*m.b19 + m.x48 - m.x285 <= 1106.777870451)

m.c247 = Constraint(expr=   1106.777870451*m.b20 + m.x50 - m.x284 <= 1106.777870451)

m.c248 = Constraint(expr=   1106.777870451*m.b21 + m.x52 - m.x285 <= 1106.777870451)

m.c249 = Constraint(expr=   1106.777870451*m.b22 + m.x54 - m.x284 <= 1106.777870451)

m.c250 = Constraint(expr=   1106.777870451*m.b23 + m.x56 - m.x285 <= 1106.777870451)

m.c251 = Constraint(expr=   1106.777870452*m.b24 + m.x58 - m.x284 <= 1106.777870452)

m.c252 = Constraint(expr=   1106.777870452*m.b25 + m.x60 - m.x285 <= 1106.777870452)

m.c253 = Constraint(expr=   m.b2 - m.b3 + m.x286 >= 0)

m.c254 = Constraint(expr=   m.b4 - m.b5 + m.x287 >= 0)

m.c255 = Constraint(expr=   m.b6 - m.b7 + m.x288 >= 0)

m.c256 = Constraint(expr=   m.b8 - m.b9 + m.x289 >= 0)

m.c257 = Constraint(expr=   m.b10 - m.b11 + m.x290 >= 0)

m.c258 = Constraint(expr=   m.b12 - m.b13 + m.x291 >= 0)

m.c259 = Constraint(expr=   m.b14 - m.b15 + m.x292 >= 0)

m.c260 = Constraint(expr=   m.b16 - m.b17 + m.x293 >= 0)

m.c261 = Constraint(expr=   m.b18 - m.b19 + m.x294 >= 0)

m.c262 = Constraint(expr=   m.b20 - m.b21 + m.x295 >= 0)

m.c263 = Constraint(expr=   m.b22 - m.b23 + m.x296 >= 0)

m.c264 = Constraint(expr=   m.b24 - m.b25 + m.x297 >= 0)

m.c265 = Constraint(expr= - m.b2 + m.b3 + m.x286 >= 0)

m.c266 = Constraint(expr= - m.b4 + m.b5 + m.x287 >= 0)

m.c267 = Constraint(expr= - m.b6 + m.b7 + m.x288 >= 0)

m.c268 = Constraint(expr= - m.b8 + m.b9 + m.x289 >= 0)

m.c269 = Constraint(expr= - m.b10 + m.b11 + m.x290 >= 0)

m.c270 = Constraint(expr= - m.b12 + m.b13 + m.x291 >= 0)

m.c271 = Constraint(expr= - m.b14 + m.b15 + m.x292 >= 0)

m.c272 = Constraint(expr= - m.b16 + m.b17 + m.x293 >= 0)

m.c273 = Constraint(expr= - m.b18 + m.b19 + m.x294 >= 0)

m.c274 = Constraint(expr= - m.b20 + m.b21 + m.x295 >= 0)

m.c275 = Constraint(expr= - m.b22 + m.b23 + m.x296 >= 0)

m.c276 = Constraint(expr= - m.b24 + m.b25 + m.x297 >= 0)

m.c277 = Constraint(expr= - 5*m.b26 + m.x78 <= 0)

m.c278 = Constraint(expr= - 5*m.b27 + m.x81 <= 0)

m.c279 = Constraint(expr= - 5*m.b28 + m.x113 <= 0)

m.c280 = Constraint(expr= - 5*m.b29 + m.x115 <= 0)

m.c281 = Constraint(expr= - 5*m.b30 + m.x103 <= 0)

m.c282 = Constraint(expr= - 5*m.b31 + m.x105 <= 0)

m.c283 = Constraint(expr= - 1000*m.b26 + m.x216 - m.x240 >= -1000)

m.c284 = Constraint(expr= - 1000*m.b27 + m.x219 - m.x243 >= -1000)

m.c285 = Constraint(expr= - 1000*m.b28 + m.x260 - m.x272 >= -1000)

m.c286 = Constraint(expr= - 1000*m.b29 + m.x263 - m.x274 >= -1000)

m.c287 = Constraint(expr= - 1000*m.b30 + m.x241 - m.x246 >= -1000)

m.c288 = Constraint(expr= - 1000*m.b31 + m.x244 - m.x249 >= -1000)

m.c289 = Constraint(expr= - 1000*m.b26 + m.x216 - m.x240 <= 0)

m.c290 = Constraint(expr= - 1000*m.b27 + m.x219 - m.x243 <= 0)

m.c291 = Constraint(expr= - 1000*m.b28 + m.x260 - m.x272 <= 0)

m.c292 = Constraint(expr= - 1000*m.b29 + m.x263 - m.x274 <= 0)

m.c293 = Constraint(expr= - 1000*m.b30 + m.x241 - m.x246 <= 0)

m.c294 = Constraint(expr= - 1000*m.b31 + m.x244 - m.x249 <= 0)

m.c295 = Constraint(expr= - m.x190 + m.x240 >= 60)

m.c296 = Constraint(expr= - m.x191 + m.x243 >= 60)

m.c297 = Constraint(expr= - m.x192 + m.x240 >= 60)

m.c298 = Constraint(expr= - m.x193 + m.x243 >= 60)

m.c299 = Constraint(expr= - m.x194 + m.x266 >= 50)

m.c300 = Constraint(expr= - m.x195 + m.x268 >= 50)

m.c301 = Constraint(expr=60159.7666785*m.x140**2 - m.x143 == 0)

m.c302 = Constraint(expr=60159.7666785*m.x142**2 - m.x147 == 0)

m.c303 = Constraint(expr=16103.4266989*m.x144**2 - m.x153 == 0)

m.c304 = Constraint(expr=16103.4266989*m.x146**2 - m.x159 == 0)

m.c305 = Constraint(expr=16103.4266989*m.x148**2 - m.x165 == 0)

m.c306 = Constraint(expr=16103.4266989*m.x150**2 - m.x171 == 0)

m.c307 = Constraint(expr=16103.4266989*m.x152**2 - m.x177 == 0)

m.c308 = Constraint(expr=16103.4266989*m.x154**2 - m.x183 == 0)

m.c309 = Constraint(expr=16103.4266989*m.x156**2 - m.x298 == 0)

m.c310 = Constraint(expr=16103.4266989*m.x158**2 - m.x301 == 0)

m.c311 = Constraint(expr=16103.4266989*m.x160**2 - m.x32 == 0)

m.c312 = Constraint(expr=16103.4266989*m.x162**2 - m.x35 == 0)

m.c313 = Constraint(expr=16103.4266989*m.x164**2 - m.x38 == 0)

m.c314 = Constraint(expr=16103.4266989*m.x166**2 - m.x41 == 0)

m.c315 = Constraint(expr=60159.7666785*m.x168**2 - m.x43 == 0)

m.c316 = Constraint(expr=60159.7666785*m.x170**2 - m.x45 == 0)

m.c317 = Constraint(expr=2296.01902001*m.x172**2 - m.x47 == 0)

m.c318 = Constraint(expr=2296.01902001*m.x174**2 - m.x49 == 0)

m.c319 = Constraint(expr=2296.01902001*m.x176**2 - m.x51 == 0)

m.c320 = Constraint(expr=2296.01902001*m.x178**2 - m.x53 == 0)

m.c321 = Constraint(expr=2296.01902001*m.x180**2 - m.x55 == 0)

m.c322 = Constraint(expr=2296.01902001*m.x182**2 - m.x57 == 0)

m.c323 = Constraint(expr=6324.78464025*m.x184**2 - m.x59 == 0)

m.c324 = Constraint(expr=6324.78464025*m.x186**2 - m.x61 == 0)

m.c325 = Constraint(expr=2.4525*m.x140*m.x141 - m.x304 <= 0)

m.c326 = Constraint(expr=2.4525*m.x142*m.x145 - m.x305 <= 0)

m.c327 = Constraint(expr=2.4525*m.x144*m.x151 - m.x306 <= 0)

m.c328 = Constraint(expr=2.4525*m.x146*m.x157 - m.x307 <= 0)

m.c329 = Constraint(expr=2.4525*m.x148*m.x163 - m.x308 <= 0)

m.c330 = Constraint(expr=2.4525*m.x150*m.x169 - m.x309 <= 0)

m.c331 = Constraint(expr=2.4525*m.x152*m.x175 - m.x310 <= 0)

m.c332 = Constraint(expr=2.4525*m.x154*m.x181 - m.x311 <= 0)

m.c333 = Constraint(expr=2.4525*m.x156*m.x187 - m.x312 <= 0)

m.c334 = Constraint(expr=2.4525*m.x158*m.x300 - m.x313 <= 0)

m.c335 = Constraint(expr=2.4525*m.x160*m.x303 - m.x314 <= 0)

m.c336 = Constraint(expr=2.4525*m.x34*m.x162 - m.x315 <= 0)

m.c337 = Constraint(expr=2.4525*m.x37*m.x164 - m.x316 <= 0)

m.c338 = Constraint(expr=2.4525*m.x40*m.x166 - m.x317 <= 0)

m.c339 = Constraint(expr=2.4525*m.x42*m.x168 - m.x318 <= 0)

m.c340 = Constraint(expr=2.4525*m.x44*m.x170 - m.x319 <= 0)

m.c341 = Constraint(expr=2.4525*m.x46*m.x172 - m.x320 <= 0)

m.c342 = Constraint(expr=2.4525*m.x48*m.x174 - m.x321 <= 0)

m.c343 = Constraint(expr=2.4525*m.x50*m.x176 - m.x322 <= 0)

m.c344 = Constraint(expr=2.4525*m.x52*m.x178 - m.x323 <= 0)

m.c345 = Constraint(expr=2.4525*m.x54*m.x180 - m.x324 <= 0)

m.c346 = Constraint(expr=2.4525*m.x56*m.x182 - m.x325 <= 0)

m.c347 = Constraint(expr=2.4525*m.x58*m.x184 - m.x326 <= 0)

m.c348 = Constraint(expr=2.4525*m.x60*m.x186 - m.x327 <= 0)

m.c349 = Constraint(expr=SignPower(m.x62,2) - 0.107595782151047*m.x198 == 0)

m.c350 = Constraint(expr=SignPower(m.x64,2) - 0.107595782151047*m.x201 == 0)

m.c351 = Constraint(expr=SignPower(m.x66,2) - 0.000240846101592208*m.x203 == 0)

m.c352 = Constraint(expr=SignPower(m.x69,2) - 0.000240846101592208*m.x205 == 0)

m.c353 = Constraint(expr=SignPower(m.x68,2) - 0.0011039398274554*m.x207 == 0)

m.c354 = Constraint(expr=SignPower(m.x71,2) - 0.0011039398274554*m.x209 == 0)

m.c355 = Constraint(expr=SignPower(m.x86,2) - 0.0147658094299242*m.x212 == 0)

m.c356 = Constraint(expr=SignPower(m.x87,2) - 0.0147658094299242*m.x215 == 0)

m.c357 = Constraint(expr=SignPower(m.x77,2) - 0.0126524872624481*m.x218 == 0)

m.c358 = Constraint(expr=SignPower(m.x80,2) - 0.0126524872624481*m.x221 == 0)

m.c359 = Constraint(expr=SignPower(m.x76,2) - 0.000713164667292268*m.x222 == 0)

m.c360 = Constraint(expr=SignPower(m.x79,2) - 0.000713164667292268*m.x223 == 0)

m.c361 = Constraint(expr=SignPower(m.x67,2) - 0.0253049745248962*m.x224 == 0)

m.c362 = Constraint(expr=SignPower(m.x70,2) - 0.0253049745248962*m.x225 == 0)

m.c363 = Constraint(expr=SignPower(m.x98,2) - 0.0196735206566467*m.x226 == 0)

m.c364 = Constraint(expr=SignPower(m.x99,2) - 0.0196735206566467*m.x227 == 0)

m.c365 = Constraint(expr=SignPower(m.x82,2) - 0.13436247753087*m.x228 == 0)

m.c366 = Constraint(expr=SignPower(m.x84,2) - 0.13436247753087*m.x229 == 0)

m.c367 = Constraint(expr=SignPower(m.x83,2) - 0.13436247753087*m.x230 == 0)

m.c368 = Constraint(expr=SignPower(m.x85,2) - 0.13436247753087*m.x231 == 0)

m.c369 = Constraint(expr=SignPower(m.x72,2) - 0.00268724955062101*m.x233 == 0)

m.c370 = Constraint(expr=SignPower(m.x73,2) - 0.00268724955062101*m.x235 == 0)

m.c371 = Constraint(expr=SignPower(m.x74,2) - 0.00175817654162355*m.x237 == 0)

m.c372 = Constraint(expr=SignPower(m.x75,2) - 0.00175817654162355*m.x239 == 0)

m.c373 = Constraint(expr=SignPower(m.x88,2) - 0.0156579704750926*m.x242 == 0)

m.c374 = Constraint(expr=SignPower(m.x93,2) - 0.0156579704750926*m.x245 == 0)

m.c375 = Constraint(expr=SignPower(m.x100,2) - 0.4031634796292*m.x248 == 0)

m.c376 = Constraint(expr=SignPower(m.x101,2) - 0.4031634796292*m.x251 == 0)

m.c377 = Constraint(expr=SignPower(m.x102,2) - 0.4031634796292*m.x252 == 0)

m.c378 = Constraint(expr=SignPower(m.x104,2) - 0.4031634796292*m.x253 == 0)

m.c379 = Constraint(expr=SignPower(m.x106,2) - 8.06326959261651*m.x255 == 0)

m.c380 = Constraint(expr=SignPower(m.x109,2) - 8.06326959261651*m.x257 == 0)

m.c381 = Constraint(expr=SignPower(m.x107,2) - 8.06326959261651*m.x258 == 0)

m.c382 = Constraint(expr=SignPower(m.x110,2) - 8.06326959261651*m.x259 == 0)

m.c383 = Constraint(expr=SignPower(m.x112,2) - 0.000180519501834947*m.x262 == 0)

m.c384 = Constraint(expr=SignPower(m.x114,2) - 0.000180519501834947*m.x265 == 0)

m.c385 = Constraint(expr=SignPower(m.x89,2) - 0.000180519501834947*m.x267 == 0)

m.c386 = Constraint(expr=SignPower(m.x94,2) - 0.000180519501834947*m.x269 == 0)

m.c387 = Constraint(expr=SignPower(m.x116,2) - 0.013538962637621*m.x270 == 0)

m.c388 = Constraint(expr=SignPower(m.x117,2) - 0.013538962637621*m.x271 == 0)

m.c389 = Constraint(expr=SignPower(m.x90,2) - 0.0463936827608069*m.x273 == 0)

m.c390 = Constraint(expr=SignPower(m.x95,2) - 0.0463936827608069*m.x275 == 0)

m.c391 = Constraint(expr=SignPower(m.x120,2) - 0.0964450219247959*m.x277 == 0)

m.c392 = Constraint(expr=SignPower(m.x121,2) - 0.0964450219247959*m.x279 == 0)
