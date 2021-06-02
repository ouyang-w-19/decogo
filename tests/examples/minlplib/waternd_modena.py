#  MINLP written by GAMS Convert at 04/21/18 13:55:14
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#       1854     1220      317      317        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#       5028      907     4121        0        0        0        0        0
#  FX      4        4        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#      15847    14579     1268        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(59.493,74.5),initialize=59.493)
m.x2 = Var(within=Reals,bounds=(59.625,74.5),initialize=59.625)
m.x3 = Var(within=Reals,bounds=(58.703,74.5),initialize=58.703)
m.x4 = Var(within=Reals,bounds=(57.246,74.5),initialize=57.246)
m.x5 = Var(within=Reals,bounds=(56.265,74.5),initialize=56.265)
m.x6 = Var(within=Reals,bounds=(55.955,74.5),initialize=55.955)
m.x7 = Var(within=Reals,bounds=(55.955,74.5),initialize=55.955)
m.x8 = Var(within=Reals,bounds=(56.087,74.5),initialize=56.087)
m.x9 = Var(within=Reals,bounds=(56.179,72.5),initialize=56.179)
m.x10 = Var(within=Reals,bounds=(57.003,74.5),initialize=57.003)
m.x11 = Var(within=Reals,bounds=(56.5,74.5),initialize=56.5)
m.x12 = Var(within=Reals,bounds=(57.388,74.5),initialize=57.388)
m.x13 = Var(within=Reals,bounds=(58.074,74.5),initialize=58.074)
m.x14 = Var(within=Reals,bounds=(57.019,74.5),initialize=57.019)
m.x15 = Var(within=Reals,bounds=(61.257,74.5),initialize=61.257)
m.x16 = Var(within=Reals,bounds=(59.35,74.5),initialize=59.35)
m.x17 = Var(within=Reals,bounds=(59.529,74.5),initialize=59.529)
m.x18 = Var(within=Reals,bounds=(56.594,74.5),initialize=56.594)
m.x19 = Var(within=Reals,bounds=(56.761,74.5),initialize=56.761)
m.x20 = Var(within=Reals,bounds=(57.715,74.5),initialize=57.715)
m.x21 = Var(within=Reals,bounds=(57.312,74.5),initialize=57.312)
m.x22 = Var(within=Reals,bounds=(57.623,74.5),initialize=57.623)
m.x23 = Var(within=Reals,bounds=(56.987,74.5),initialize=56.987)
m.x24 = Var(within=Reals,bounds=(55.205,74.5),initialize=55.205)
m.x25 = Var(within=Reals,bounds=(55.113,74.5),initialize=55.113)
m.x26 = Var(within=Reals,bounds=(54.654,74.5),initialize=54.654)
m.x27 = Var(within=Reals,bounds=(54.325,74.5),initialize=54.325)
m.x28 = Var(within=Reals,bounds=(56.145,74.5),initialize=56.145)
m.x29 = Var(within=Reals,bounds=(56.296,74.5),initialize=56.296)
m.x30 = Var(within=Reals,bounds=(56.097,74.5),initialize=56.097)
m.x31 = Var(within=Reals,bounds=(56.139,74.5),initialize=56.139)
m.x32 = Var(within=Reals,bounds=(55.8,74.5),initialize=55.8)
m.x33 = Var(within=Reals,bounds=(53.261,74.5),initialize=53.261)
m.x34 = Var(within=Reals,bounds=(53.337,74.5),initialize=53.337)
m.x35 = Var(within=Reals,bounds=(53.513,74.5),initialize=53.513)
m.x36 = Var(within=Reals,bounds=(52.7,74.5),initialize=52.7)
m.x37 = Var(within=Reals,bounds=(52.647,74.5),initialize=52.647)
m.x38 = Var(within=Reals,bounds=(52.565,74.5),initialize=52.565)
m.x39 = Var(within=Reals,bounds=(53.565,74.5),initialize=53.565)
m.x40 = Var(within=Reals,bounds=(51.595,74.5),initialize=51.595)
m.x41 = Var(within=Reals,bounds=(51.381,74.5),initialize=51.381)
m.x42 = Var(within=Reals,bounds=(52.667,74.5),initialize=52.667)
m.x43 = Var(within=Reals,bounds=(53.499,74.5),initialize=53.499)
m.x44 = Var(within=Reals,bounds=(53.571,74.5),initialize=53.571)
m.x45 = Var(within=Reals,bounds=(53.774,74.5),initialize=53.774)
m.x46 = Var(within=Reals,bounds=(54.137,74.5),initialize=54.137)
m.x47 = Var(within=Reals,bounds=(53.68,74.5),initialize=53.68)
m.x48 = Var(within=Reals,bounds=(53.706,74.5),initialize=53.706)
m.x49 = Var(within=Reals,bounds=(51.677,74.5),initialize=51.677)
m.x50 = Var(within=Reals,bounds=(53.345,74.5),initialize=53.345)
m.x51 = Var(within=Reals,bounds=(52.832,74.5),initialize=52.832)
m.x52 = Var(within=Reals,bounds=(52.778,74.5),initialize=52.778)
m.x53 = Var(within=Reals,bounds=(59.276,74.5),initialize=59.276)
m.x54 = Var(within=Reals,bounds=(57.123,74.5),initialize=57.123)
m.x55 = Var(within=Reals,bounds=(56.484,74.5),initialize=56.484)
m.x56 = Var(within=Reals,bounds=(56.416,74.5),initialize=56.416)
m.x57 = Var(within=Reals,bounds=(56.135,74.5),initialize=56.135)
m.x58 = Var(within=Reals,bounds=(56.049,74.5),initialize=56.049)
m.x59 = Var(within=Reals,bounds=(56.765,74.5),initialize=56.765)
m.x60 = Var(within=Reals,bounds=(55.484,74.5),initialize=55.484)
m.x61 = Var(within=Reals,bounds=(55.049,74.5),initialize=55.049)
m.x62 = Var(within=Reals,bounds=(55.105,74.5),initialize=55.105)
m.x63 = Var(within=Reals,bounds=(57.951,74.5),initialize=57.951)
m.x64 = Var(within=Reals,bounds=(58.442,74.5),initialize=58.442)
m.x65 = Var(within=Reals,bounds=(57.807,74.5),initialize=57.807)
m.x66 = Var(within=Reals,bounds=(58.218,74.5),initialize=58.218)
m.x67 = Var(within=Reals,bounds=(58.727,74.5),initialize=58.727)
m.x68 = Var(within=Reals,bounds=(58.953,74.5),initialize=58.953)
m.x69 = Var(within=Reals,bounds=(59.701,74.5),initialize=59.701)
m.x70 = Var(within=Reals,bounds=(60.589,74.5),initialize=60.589)
m.x71 = Var(within=Reals,bounds=(60.812,74.5),initialize=60.812)
m.x72 = Var(within=Reals,bounds=(61.064,74.5),initialize=61.064)
m.x73 = Var(within=Reals,bounds=(61.453,74.5),initialize=61.453)
m.x74 = Var(within=Reals,bounds=(61.83,74.5),initialize=61.83)
m.x75 = Var(within=Reals,bounds=(61.435,74.5),initialize=61.435)
m.x76 = Var(within=Reals,bounds=(61.092,74.5),initialize=61.092)
m.x77 = Var(within=Reals,bounds=(60.743,74.5),initialize=60.743)
m.x78 = Var(within=Reals,bounds=(58.605,74.5),initialize=58.605)
m.x79 = Var(within=Reals,bounds=(56.915,74.5),initialize=56.915)
m.x80 = Var(within=Reals,bounds=(56.749,74.5),initialize=56.749)
m.x81 = Var(within=Reals,bounds=(56.813,74.5),initialize=56.813)
m.x82 = Var(within=Reals,bounds=(57.045,74.5),initialize=57.045)
m.x83 = Var(within=Reals,bounds=(55.883,74.5),initialize=55.883)
m.x84 = Var(within=Reals,bounds=(56.454,74.5),initialize=56.454)
m.x85 = Var(within=Reals,bounds=(56.161,74.5),initialize=56.161)
m.x86 = Var(within=Reals,bounds=(54.991,74.5),initialize=54.991)
m.x87 = Var(within=Reals,bounds=(55.612,74.5),initialize=55.612)
m.x88 = Var(within=Reals,bounds=(54.892,74.5),initialize=54.892)
m.x89 = Var(within=Reals,bounds=(55.586,74.5),initialize=55.586)
m.x90 = Var(within=Reals,bounds=(55.7,74.5),initialize=55.7)
m.x91 = Var(within=Reals,bounds=(55.195,74.5),initialize=55.195)
m.x92 = Var(within=Reals,bounds=(55.64,74.5),initialize=55.64)
m.x93 = Var(within=Reals,bounds=(55.929,74.5),initialize=55.929)
m.x94 = Var(within=Reals,bounds=(57.639,74.5),initialize=57.639)
m.x95 = Var(within=Reals,bounds=(57.168,74.5),initialize=57.168)
m.x96 = Var(within=Reals,bounds=(57.105,74.5),initialize=57.105)
m.x97 = Var(within=Reals,bounds=(56.971,74.5),initialize=56.971)
m.x98 = Var(within=Reals,bounds=(56.997,74.5),initialize=56.997)
m.x99 = Var(within=Reals,bounds=(56.739,74.5),initialize=56.739)
m.x100 = Var(within=Reals,bounds=(54.776,74.5),initialize=54.776)
m.x101 = Var(within=Reals,bounds=(54.257,74.5),initialize=54.257)
m.x102 = Var(within=Reals,bounds=(53.66,74.5),initialize=53.66)
m.x103 = Var(within=Reals,bounds=(53.784,74.5),initialize=53.784)
m.x104 = Var(within=Reals,bounds=(53.746,74.5),initialize=53.746)
m.x105 = Var(within=Reals,bounds=(53.377,74.5),initialize=53.377)
m.x106 = Var(within=Reals,bounds=(54.85,74.5),initialize=54.85)
m.x107 = Var(within=Reals,bounds=(54.273,74.5),initialize=54.273)
m.x108 = Var(within=Reals,bounds=(54.297,74.5),initialize=54.297)
m.x109 = Var(within=Reals,bounds=(53.954,74.5),initialize=53.954)
m.x110 = Var(within=Reals,bounds=(53.92,74.5),initialize=53.92)
m.x111 = Var(within=Reals,bounds=(52.317,74.5),initialize=52.317)
m.x112 = Var(within=Reals,bounds=(54.758,74.5),initialize=54.758)
m.x113 = Var(within=Reals,bounds=(54.213,74.5),initialize=54.213)
m.x114 = Var(within=Reals,bounds=(54.924,74.5),initialize=54.924)
m.x115 = Var(within=Reals,bounds=(52.956,71.5),initialize=52.956)
m.x116 = Var(within=Reals,bounds=(50.689,74.5),initialize=50.689)
m.x117 = Var(within=Reals,bounds=(50.595,74.5),initialize=50.595)
m.x118 = Var(within=Reals,bounds=(50.731,74.5),initialize=50.731)
m.x119 = Var(within=Reals,bounds=(50.703,74.5),initialize=50.703)
m.x120 = Var(within=Reals,bounds=(51.02,74.5),initialize=51.02)
m.x121 = Var(within=Reals,bounds=(51.032,74.5),initialize=51.032)
m.x122 = Var(within=Reals,bounds=(51.745,74.5),initialize=51.745)
m.x123 = Var(within=Reals,bounds=(52,74.5),initialize=52)
m.x124 = Var(within=Reals,bounds=(52.048,74.5),initialize=52.048)
m.x125 = Var(within=Reals,bounds=(52.098,74.5),initialize=52.098)
m.x126 = Var(within=Reals,bounds=(53.76,74.5),initialize=53.76)
m.x127 = Var(within=Reals,bounds=(52.271,74.5),initialize=52.271)
m.x128 = Var(within=Reals,bounds=(51.86,74.5),initialize=51.86)
m.x129 = Var(within=Reals,bounds=(52.417,74.5),initialize=52.417)
m.x130 = Var(within=Reals,bounds=(53.002,74.5),initialize=53.002)
m.x131 = Var(within=Reals,bounds=(53.626,74.5),initialize=53.626)
m.x132 = Var(within=Reals,bounds=(56.366,74.5),initialize=56.366)
m.x133 = Var(within=Reals,bounds=(55.694,74.5),initialize=55.694)
m.x134 = Var(within=Reals,bounds=(55.524,74.5),initialize=55.524)
m.x135 = Var(within=Reals,bounds=(55.56,74.5),initialize=55.56)
m.x136 = Var(within=Reals,bounds=(55.917,74.5),initialize=55.917)
m.x137 = Var(within=Reals,bounds=(55.367,74.5),initialize=55.367)
m.x138 = Var(within=Reals,bounds=(55.057,74.5),initialize=55.057)
m.x139 = Var(within=Reals,bounds=(54.125,74.5),initialize=54.125)
m.x140 = Var(within=Reals,bounds=(59.35,74.5),initialize=59.35)
m.x141 = Var(within=Reals,bounds=(59.104,74.5),initialize=59.104)
m.x142 = Var(within=Reals,bounds=(59.841,74.5),initialize=59.841)
m.x143 = Var(within=Reals,bounds=(59.841,74.5),initialize=59.841)
m.x144 = Var(within=Reals,bounds=(59.449,74.5),initialize=59.449)
m.x145 = Var(within=Reals,bounds=(59.705,74.5),initialize=59.705)
m.x146 = Var(within=Reals,bounds=(57.951,74.5),initialize=57.951)
m.x147 = Var(within=Reals,bounds=(57.61,74.5),initialize=57.61)
m.x148 = Var(within=Reals,bounds=(57.951,74.5),initialize=57.951)
m.x149 = Var(within=Reals,bounds=(55.686,74.5),initialize=55.686)
m.x150 = Var(within=Reals,bounds=(55.317,74.5),initialize=55.317)
m.x151 = Var(within=Reals,bounds=(55.81,74.5),initialize=55.81)
m.x152 = Var(within=Reals,bounds=(55.812,74.5),initialize=55.812)
m.x153 = Var(within=Reals,bounds=(56.019,74.5),initialize=56.019)
m.x154 = Var(within=Reals,bounds=(58.254,74.5),initialize=58.254)
m.x155 = Var(within=Reals,bounds=(57.504,74.5),initialize=57.504)
m.x156 = Var(within=Reals,bounds=(57.536,74.5),initialize=57.536)
m.x157 = Var(within=Reals,bounds=(57.079,74.5),initialize=57.079)
m.x158 = Var(within=Reals,bounds=(56.755,74.5),initialize=56.755)
m.x159 = Var(within=Reals,bounds=(55.885,74.5),initialize=55.885)
m.x160 = Var(within=Reals,bounds=(55.768,74.5),initialize=55.768)
m.x161 = Var(within=Reals,bounds=(54.704,74.5),initialize=54.704)
m.x162 = Var(within=Reals,bounds=(55.369,74.5),initialize=55.369)
m.x163 = Var(within=Reals,bounds=(54.993,74.5),initialize=54.993)
m.x164 = Var(within=Reals,bounds=(55.927,74.5),initialize=55.927)
m.x165 = Var(within=Reals,bounds=(56.265,74.5),initialize=56.265)
m.x166 = Var(within=Reals,bounds=(52.667,74.5),initialize=52.667)
m.x167 = Var(within=Reals,bounds=(52.754,74.5),initialize=52.754)
m.x168 = Var(within=Reals,bounds=(52.884,74.5),initialize=52.884)
m.x169 = Var(within=Reals,bounds=(54.085,74.5),initialize=54.085)
m.x170 = Var(within=Reals,bounds=(56.093,74.5),initialize=56.093)
m.x171 = Var(within=Reals,bounds=(56.049,74.5),initialize=56.049)
m.x172 = Var(within=Reals,bounds=(56.041,74.5),initialize=56.041)
m.x173 = Var(within=Reals,bounds=(56.017,74.5),initialize=56.017)
m.x174 = Var(within=Reals,bounds=(51.757,74.5),initialize=51.757)
m.x175 = Var(within=Reals,bounds=(51.91,74.5),initialize=51.91)
m.x176 = Var(within=Reals,bounds=(51.799,74.5),initialize=51.799)
m.x177 = Var(within=Reals,bounds=(51.483,74.5),initialize=51.483)
m.x178 = Var(within=Reals,bounds=(51.116,74.5),initialize=51.116)
m.x179 = Var(within=Reals,bounds=(51.096,74.5),initialize=51.096)
m.x180 = Var(within=Reals,bounds=(51.194,74.5),initialize=51.194)
m.x181 = Var(within=Reals,bounds=(50.392,74.5),initialize=50.392)
m.x182 = Var(within=Reals,bounds=(50.547,74.5),initialize=50.547)
m.x183 = Var(within=Reals,bounds=(51.134,74.5),initialize=51.134)
m.x184 = Var(within=Reals,bounds=(51.81,74.5),initialize=51.81)
m.x185 = Var(within=Reals,bounds=(52.345,74.5),initialize=52.345)
m.x186 = Var(within=Reals,bounds=(52.826,74.5),initialize=52.826)
m.x187 = Var(within=Reals,bounds=(53.694,74.5),initialize=53.694)
m.x188 = Var(within=Reals,bounds=(53.175,74.5),initialize=53.175)
m.x189 = Var(within=Reals,bounds=(53.229,74.5),initialize=53.229)
m.x190 = Var(within=Reals,bounds=(53.343,74.5),initialize=53.343)
m.x191 = Var(within=Reals,bounds=(53.772,74.5),initialize=53.772)
m.x192 = Var(within=Reals,bounds=(53.768,74.5),initialize=53.768)
m.x193 = Var(within=Reals,bounds=(52.204,74.5),initialize=52.204)
m.x194 = Var(within=Reals,bounds=(54.405,74.5),initialize=54.405)
m.x195 = Var(within=Reals,bounds=(53.389,74.5),initialize=53.389)
m.x196 = Var(within=Reals,bounds=(54.345,74.5),initialize=54.345)
m.x197 = Var(within=Reals,bounds=(55.027,74.5),initialize=55.027)
m.x198 = Var(within=Reals,bounds=(54.439,74.5),initialize=54.439)
m.x199 = Var(within=Reals,bounds=(54.534,74.5),initialize=54.534)
m.x200 = Var(within=Reals,bounds=(54.935,74.5),initialize=54.935)
m.x201 = Var(within=Reals,bounds=(54.704,74.5),initialize=54.704)
m.x202 = Var(within=Reals,bounds=(56.7,74.5),initialize=56.7)
m.x203 = Var(within=Reals,bounds=(56.203,74.5),initialize=56.203)
m.x204 = Var(within=Reals,bounds=(55.031,74.5),initialize=55.031)
m.x205 = Var(within=Reals,bounds=(56.765,74.5),initialize=56.765)
m.x206 = Var(within=Reals,bounds=(56.197,74.5),initialize=56.197)
m.x207 = Var(within=Reals,bounds=(57.879,74.5),initialize=57.879)
m.x208 = Var(within=Reals,bounds=(58.035,74.5),initialize=58.035)
m.x209 = Var(within=Reals,bounds=(56.863,74.5),initialize=56.863)
m.x210 = Var(within=Reals,bounds=(57.238,74.5),initialize=57.238)
m.x211 = Var(within=Reals,bounds=(56.658,74.5),initialize=56.658)
m.x212 = Var(within=Reals,bounds=(56.49,74.5),initialize=56.49)
m.x213 = Var(within=Reals,bounds=(57.3,74.5),initialize=57.3)
m.x214 = Var(within=Reals,bounds=(60.299,74.5),initialize=60.299)
m.x215 = Var(within=Reals,bounds=(59.849,74.5),initialize=59.849)
m.x216 = Var(within=Reals,bounds=(60.998,74.5),initialize=60.998)
m.x217 = Var(within=Reals,bounds=(61.16,74.5),initialize=61.16)
m.x218 = Var(within=Reals,bounds=(55.049,74.5),initialize=55.049)
m.x219 = Var(within=Reals,bounds=(53.92,74.5),initialize=53.92)
m.x220 = Var(within=Reals,bounds=(52.144,74.5),initialize=52.144)
m.x221 = Var(within=Reals,bounds=(54.167,74.5),initialize=54.167)
m.x222 = Var(within=Reals,bounds=(55.097,74.5),initialize=55.097)
m.x223 = Var(within=Reals,bounds=(51.549,74.5),initialize=51.549)
m.x224 = Var(within=Reals,bounds=(51.745,74.5),initialize=51.745)
m.x225 = Var(within=Reals,bounds=(52.066,74.5),initialize=52.066)
m.x226 = Var(within=Reals,bounds=(51.944,74.5),initialize=51.944)
m.x227 = Var(within=Reals,bounds=(51.657,74.5),initialize=51.657)
m.x228 = Var(within=Reals,bounds=(51.04,74.5),initialize=51.04)
m.x229 = Var(within=Reals,bounds=(51.05,74.5),initialize=51.05)
m.x230 = Var(within=Reals,bounds=(58.492,74.5),initialize=58.492)
m.x231 = Var(within=Reals,bounds=(55.684,74.5),initialize=55.684)
m.x232 = Var(within=Reals,bounds=(55.39,74.5),initialize=55.39)
m.x233 = Var(within=Reals,bounds=(54.888,74.5),initialize=54.888)
m.x234 = Var(within=Reals,bounds=(54.858,74.5),initialize=54.858)
m.x235 = Var(within=Reals,bounds=(54.995,74.5),initialize=54.995)
m.x236 = Var(within=Reals,bounds=(52.541,74.5),initialize=52.541)
m.x237 = Var(within=Reals,bounds=(54.413,74.5),initialize=54.413)
m.x238 = Var(within=Reals,bounds=(56.157,74.5),initialize=56.157)
m.x239 = Var(within=Reals,bounds=(55.305,74.5),initialize=55.305)
m.x240 = Var(within=Reals,bounds=(55.171,74.5),initialize=55.171)
m.x241 = Var(within=Reals,bounds=(52.918,74.5),initialize=52.918)
m.x242 = Var(within=Reals,bounds=(53.066,74.5),initialize=53.066)
m.x243 = Var(within=Reals,bounds=(51.91,74.5),initialize=51.91)
m.x244 = Var(within=Reals,bounds=(52.002,74.5),initialize=52.002)
m.x245 = Var(within=Reals,bounds=(52.048,74.5),initialize=52.048)
m.x246 = Var(within=Reals,bounds=(52.054,74.5),initialize=52.054)
m.x247 = Var(within=Reals,bounds=(50.705,74.5),initialize=50.705)
m.x248 = Var(within=Reals,bounds=(51.332,74.5),initialize=51.332)
m.x249 = Var(within=Reals,bounds=(56.296,74.5),initialize=56.296)
m.x250 = Var(within=Reals,bounds=(55.831,74.5),initialize=55.831)
m.x251 = Var(within=Reals,bounds=(56.945,74.5),initialize=56.945)
m.x252 = Var(within=Reals,bounds=(58.013,74.5),initialize=58.013)
m.x253 = Var(within=Reals,bounds=(56.65,74.5),initialize=56.65)
m.x254 = Var(within=Reals,bounds=(56.905,74.5),initialize=56.905)
m.x255 = Var(within=Reals,bounds=(56.773,74.5),initialize=56.773)
m.x256 = Var(within=Reals,bounds=(51.497,74.5),initialize=51.497)
m.x257 = Var(within=Reals,bounds=(58.651,74.5),initialize=58.651)
m.x258 = Var(within=Reals,bounds=(59.543,74.5),initialize=59.543)
m.x259 = Var(within=Reals,bounds=(59.581,74.5),initialize=59.581)
m.x260 = Var(within=Reals,bounds=(59.581,74.5),initialize=59.581)
m.x261 = Var(within=Reals,bounds=(60.551,74.5),initialize=60.551)
m.x262 = Var(within=Reals,bounds=(60.786,74.5),initialize=60.786)
m.x263 = Var(within=Reals,bounds=(60.954,74.5),initialize=60.954)
m.x264 = Var(within=Reals,bounds=(57.755,74.5),initialize=57.755)
m.x265 = Var(within=Reals,bounds=(55.963,74.5),initialize=55.963)
m.x266 = Var(within=Reals,bounds=(56.809,74.5),initialize=56.809)
m.x267 = Var(within=Reals,bounds=(56.211,74.5),initialize=56.211)
m.x268 = Var(within=Reals,bounds=(55.612,74.5),initialize=55.612)
m.x269 = Var(within=Reals,bounds=(72,72),initialize=72)
m.x270 = Var(within=Reals,bounds=(73.8,73.8),initialize=73.8)
m.x271 = Var(within=Reals,bounds=(73,73),initialize=73)
m.x272 = Var(within=Reals,bounds=(74.5,74.5),initialize=74.5)
m.x273 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x274 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x275 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x276 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x277 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x278 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x279 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x280 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x281 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x282 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x283 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x284 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x285 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x286 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x287 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x288 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x289 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x290 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x291 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x292 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x293 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x294 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x295 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x296 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x297 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x298 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x299 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x300 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x301 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x302 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x303 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x304 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x305 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x306 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x307 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x308 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x309 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x310 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x311 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x312 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x313 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x314 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x315 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x316 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x317 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x318 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x319 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x320 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x321 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x322 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x323 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x324 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x325 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x326 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x327 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x328 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x329 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x330 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x331 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x332 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x333 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x334 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x335 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x336 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x337 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x338 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x339 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x340 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x341 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x342 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x343 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x344 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x345 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x346 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x347 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x348 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x349 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x350 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x351 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x352 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x353 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x354 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x355 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x356 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x357 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x358 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x359 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x360 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x361 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x362 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x363 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x364 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x365 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x366 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x367 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x368 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x369 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x370 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x371 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x372 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x373 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x374 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x375 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x376 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x377 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x378 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x379 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x380 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x381 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x382 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x383 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x384 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x385 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x386 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x387 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x388 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x389 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x390 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x391 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x392 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x393 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x394 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x395 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x396 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x397 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x398 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x399 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x400 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x401 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x402 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x403 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x404 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x405 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x406 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x407 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x408 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x409 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x410 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x411 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x412 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x413 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x414 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x415 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x416 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x417 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x418 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x419 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x420 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x421 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x422 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x423 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x424 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x425 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x426 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x427 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x428 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x429 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x430 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x431 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x432 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x433 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x434 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x435 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x436 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x437 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x438 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x439 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x440 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x441 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x442 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x443 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x444 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x445 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x446 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x447 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x448 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x449 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x450 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x451 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x452 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x453 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x454 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x455 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x456 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x457 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x458 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x459 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x460 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x461 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x462 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x463 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x464 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x465 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x466 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x467 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x468 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x469 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x470 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x471 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x472 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x473 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x474 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x475 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x476 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x477 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x478 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x479 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x480 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x481 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x482 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x483 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x484 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x485 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x486 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x487 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x488 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x489 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x490 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x491 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x492 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x493 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x494 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x495 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x496 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x497 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x498 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x499 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x500 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x501 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x502 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x503 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x504 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x505 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x506 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x507 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x508 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x509 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x510 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x511 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x512 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x513 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x514 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x515 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x516 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x517 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x518 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x519 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x520 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x521 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x522 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x523 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x524 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x525 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x526 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x527 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x528 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x529 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x530 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x531 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x532 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x533 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x534 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x535 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x536 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x537 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x538 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x539 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x540 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x541 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x542 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x543 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x544 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x545 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x546 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x547 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x548 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x549 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x550 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x551 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x552 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x553 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x554 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x555 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x556 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x557 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x558 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x559 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x560 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x561 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x562 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x563 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x564 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x565 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x566 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x567 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x568 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x569 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x570 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x571 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x572 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x573 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x574 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x575 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x576 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x577 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x578 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x579 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x580 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x581 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x582 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x583 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x584 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x585 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x586 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x587 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x588 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x589 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x590 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x591 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x592 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x593 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x594 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x595 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x596 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x597 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x598 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x599 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x600 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x601 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x602 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x603 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x604 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x605 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x606 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x607 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x608 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x609 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x610 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x611 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x612 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x613 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x614 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x615 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x616 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x617 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x618 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x619 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x620 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x621 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x622 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x623 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x624 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x625 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x626 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x627 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x628 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x629 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x630 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x631 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x632 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x633 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x634 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x635 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x636 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x637 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x638 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x639 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x640 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x641 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x642 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x643 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x644 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x645 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x646 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x647 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x648 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x649 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x650 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x651 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x652 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x653 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x654 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x655 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x656 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x657 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x658 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x659 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x660 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x661 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x662 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x663 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x664 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x665 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x666 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x667 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x668 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x669 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x670 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x671 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x672 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x673 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x674 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x675 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x676 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x677 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x678 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x679 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x680 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x681 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x682 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x683 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x684 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x685 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x686 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x687 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x688 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x689 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x690 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x691 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x692 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x693 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x694 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x695 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x696 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x697 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x698 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x699 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x700 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x701 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x702 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x703 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x704 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x705 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x706 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x707 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x708 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x709 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x710 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x711 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x712 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x713 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x714 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x715 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x716 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x717 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x718 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x719 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x720 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x721 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x722 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x723 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x724 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x725 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x726 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x727 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x728 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x729 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x730 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x731 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x732 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x733 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x734 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x735 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x736 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x737 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x738 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x739 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x740 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x741 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x742 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x743 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x744 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x745 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x746 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x747 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x748 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x749 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x750 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x751 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x752 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x753 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x754 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x755 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x756 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x757 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x758 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x759 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x760 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x761 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x762 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x763 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x764 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x765 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x766 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x767 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x768 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x769 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x770 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x771 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x772 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x773 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x774 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x775 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x776 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x777 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x778 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x779 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x780 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x781 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x782 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x783 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x784 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x785 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x786 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x787 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x788 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x789 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x790 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x791 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x792 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x793 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x794 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x795 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x796 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x797 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x798 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x799 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x800 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x801 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x802 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x803 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x804 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x805 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x806 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x807 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x808 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x809 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x810 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x811 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x812 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x813 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x814 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x815 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x816 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x817 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x818 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x819 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x820 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x821 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x822 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x823 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x824 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x825 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x826 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x827 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x828 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x829 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x830 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x831 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x832 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x833 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x834 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x835 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x836 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x837 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x838 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x839 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x840 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x841 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x842 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x843 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x844 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x845 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x846 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x847 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x848 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x849 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x850 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x851 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x852 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x853 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x854 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x855 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x856 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x857 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x858 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x859 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x860 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x861 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x862 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x863 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x864 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x865 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x866 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x867 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x868 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x869 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x870 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x871 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x872 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x873 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x874 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x875 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x876 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x877 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x878 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x879 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x880 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x881 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x882 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x883 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x884 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x885 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x886 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x887 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x888 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x889 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x890 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x891 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x892 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x893 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x894 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x895 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x896 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x897 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x898 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x899 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x900 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x901 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x902 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x903 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x904 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x905 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
m.x906 = Var(within=Reals,bounds=(0.00785398163397448,0.502654824574367),initialize=0.00785398163397448)
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
m.b1430 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1431 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1432 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1433 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1434 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1435 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1436 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1437 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1438 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1439 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1440 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1441 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1442 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1443 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1444 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1445 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1446 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1447 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1448 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1449 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1450 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1451 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1452 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1453 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1454 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1455 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1456 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1457 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1458 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1459 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1460 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1461 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1462 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1463 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1464 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1465 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1466 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1467 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1468 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1469 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1470 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1471 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1472 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1473 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1474 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1475 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1476 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1477 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1478 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1479 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1480 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1481 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1482 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1483 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1484 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1485 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1486 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1487 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1488 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1489 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1490 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1491 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1492 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1493 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1494 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1495 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1496 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1497 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1498 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1499 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1500 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1501 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1502 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1503 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1504 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1505 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1506 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1507 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1508 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1509 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1510 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1511 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1512 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1513 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1514 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1515 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1516 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1517 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1518 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1519 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1520 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1521 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1522 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1523 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1524 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1525 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1526 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1527 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1528 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1529 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1530 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1531 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1532 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1533 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1534 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1535 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1536 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1537 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1538 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1539 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1540 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1541 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1542 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1543 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1544 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1545 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1546 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1547 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1548 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1549 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1550 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1551 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1552 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1553 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1554 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1555 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1556 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1557 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1558 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1559 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1560 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1561 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1562 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1563 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1564 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1565 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1566 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1567 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1568 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1569 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1570 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1571 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1572 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1573 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1574 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1575 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1576 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1577 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1578 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1579 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1580 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1581 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1582 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1583 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1584 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1585 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1586 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1587 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1588 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1589 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1590 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1591 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1592 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1593 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1594 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1595 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1596 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1597 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1598 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1599 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1600 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1601 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1602 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1603 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1604 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1605 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1606 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1607 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1608 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1609 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1610 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1611 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1612 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1613 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1614 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1615 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1616 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1617 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1618 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1619 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1620 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1621 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1622 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1623 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1624 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1625 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1626 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1627 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1628 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1629 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1630 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1631 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1632 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1633 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1634 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1635 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1636 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1637 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1638 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1639 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1640 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1641 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1642 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1643 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1644 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1645 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1646 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1647 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1648 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1649 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1650 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1651 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1652 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1653 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1654 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1655 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1656 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1657 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1658 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1659 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1660 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1661 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1662 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1663 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1664 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1665 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1666 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1667 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1668 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1669 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1670 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1671 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1672 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1673 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1674 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1675 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1676 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1677 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1678 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1679 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1680 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1681 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1682 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1683 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1684 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1685 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1686 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1687 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1688 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1689 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1690 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1691 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1692 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1693 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1694 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1695 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1696 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1697 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1698 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1699 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1700 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1701 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1702 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1703 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1704 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1705 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1706 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1707 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1708 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1709 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1710 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1711 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1712 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1713 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1714 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1715 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1716 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1717 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1718 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1719 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1720 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1721 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1722 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1723 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1724 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1725 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1726 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1727 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1728 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1729 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1730 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1731 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1732 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1733 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1734 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1735 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1736 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1737 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1738 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1739 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1740 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1741 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1742 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1743 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1744 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1745 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1746 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1747 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1748 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1749 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1750 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1751 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1752 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1753 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1754 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1755 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1756 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1757 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1758 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1759 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1760 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1761 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1762 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1763 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1764 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1765 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1766 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1767 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1768 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1769 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1770 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1771 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1772 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1773 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1774 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1775 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1776 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1777 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1778 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1779 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1780 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1781 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1782 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1783 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1784 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1785 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1786 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1787 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1788 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1789 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1790 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1791 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1792 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1793 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1794 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1795 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1796 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1797 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1798 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1799 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1800 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1801 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1802 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1803 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1804 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1805 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1806 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1807 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1808 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1809 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1810 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1811 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1812 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1813 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1814 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1815 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1816 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1817 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1818 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1819 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1820 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1821 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1822 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1823 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1824 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1825 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1826 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1827 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1828 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1829 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1830 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1831 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1832 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1833 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1834 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1835 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1836 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1837 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1838 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1839 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1840 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1841 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1842 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1843 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1844 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1845 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1846 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1847 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1848 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1849 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1850 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1851 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1852 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1853 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1854 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1855 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1856 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1857 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1858 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1859 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1860 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1861 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1862 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1863 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1864 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1865 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1866 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1867 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1868 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1869 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1870 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1871 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1872 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1873 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1874 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1875 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1876 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1877 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1878 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1879 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1880 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1881 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1882 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1883 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1884 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1885 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1886 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1887 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1888 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1889 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1890 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1891 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1892 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1893 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1894 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1895 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1896 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1897 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1898 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1899 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1900 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1901 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1902 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1903 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1904 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1905 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1906 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1907 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1908 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1909 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1910 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1911 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1912 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1913 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1914 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1915 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1916 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1917 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1918 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1919 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1920 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1921 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1922 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1923 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1924 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1925 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1926 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1927 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1928 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1929 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1930 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1931 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1932 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1933 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1934 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1935 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1936 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1937 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1938 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1939 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1940 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1941 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1942 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1943 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1944 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1945 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1946 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1947 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1948 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1949 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1950 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1951 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1952 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1953 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1954 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1955 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1956 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1957 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1958 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1959 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1960 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1961 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1962 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1963 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1964 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1965 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1966 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1967 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1968 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1969 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1970 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1971 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1972 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1973 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1974 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1975 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1976 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1977 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1978 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1979 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1980 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1981 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1982 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1983 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1984 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1985 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1986 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1987 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1988 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1989 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1990 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1991 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1992 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1993 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1994 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1995 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1996 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1997 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1998 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1999 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2000 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2001 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2002 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2003 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2004 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2005 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2006 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2007 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2008 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2009 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2010 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2011 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2012 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2013 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2014 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2015 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2016 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2017 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2018 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2019 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2020 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2021 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2022 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2023 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2024 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2025 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2026 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2027 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2028 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2029 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2030 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2031 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2032 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2033 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2034 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2035 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2036 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2037 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2038 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2039 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2040 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2041 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2042 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2043 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2044 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2045 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2046 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2047 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2048 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2049 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2050 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2051 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2052 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2053 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2054 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2055 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2056 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2057 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2058 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2059 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2060 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2061 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2062 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2063 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2064 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2065 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2066 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2067 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2068 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2069 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2070 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2071 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2072 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2073 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2074 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2075 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2076 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2077 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2078 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2079 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2080 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2081 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2082 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2083 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2084 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2085 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2086 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2087 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2088 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2089 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2090 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2091 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2092 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2093 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2094 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2095 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2096 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2097 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2098 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2099 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2100 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2101 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2102 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2103 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2104 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2105 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2106 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2107 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2108 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2109 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2110 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2111 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2112 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2113 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2114 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2115 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2116 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2117 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2118 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2119 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2120 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2121 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2122 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2123 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2124 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2125 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2126 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2127 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2128 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2129 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2130 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2131 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2132 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2133 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2134 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2135 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2136 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2137 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2138 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2139 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2140 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2141 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2142 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2143 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2144 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2145 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2146 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2147 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2148 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2149 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2150 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2151 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2152 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2153 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2154 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2155 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2156 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2157 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2158 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2159 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2160 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2161 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2162 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2163 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2164 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2165 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2166 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2167 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2168 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2169 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2170 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2171 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2172 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2173 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2174 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2175 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2176 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2177 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2178 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2179 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2180 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2181 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2182 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2183 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2184 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2185 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2186 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2187 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2188 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2189 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2190 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2191 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2192 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2193 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2194 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2195 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2196 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2197 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2198 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2199 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2200 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2201 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2202 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2203 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2204 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2205 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2206 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2207 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2208 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2209 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2210 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2211 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2212 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2213 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2214 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2215 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2216 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2217 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2218 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2219 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2220 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2221 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2222 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2223 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2224 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2225 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2226 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2227 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2228 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2229 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2230 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2231 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2232 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2233 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2234 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2235 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2236 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2237 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2238 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2239 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2240 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2241 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2242 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2243 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2244 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2245 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2246 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2247 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2248 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2249 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2250 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2251 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2252 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2253 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2254 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2255 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2256 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2257 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2258 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2259 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2260 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2261 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2262 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2263 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2264 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2265 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2266 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2267 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2268 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2269 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2270 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2271 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2272 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2273 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2274 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2275 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2276 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2277 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2278 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2279 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2280 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2281 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2282 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2283 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2284 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2285 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2286 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2287 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2288 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2289 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2290 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2291 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2292 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2293 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2294 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2295 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2296 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2297 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2298 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2299 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2300 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2301 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2302 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2303 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2304 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2305 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2306 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2307 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2308 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2309 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2310 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2311 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2312 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2313 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2314 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2315 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2316 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2317 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2318 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2319 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2320 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2321 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2322 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2323 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2324 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2325 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2326 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2327 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2328 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2329 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2330 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2331 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2332 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2333 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2334 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2335 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2336 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2337 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2338 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2339 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2340 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2341 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2342 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2343 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2344 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2345 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2346 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2347 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2348 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2349 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2350 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2351 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2352 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2353 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2354 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2355 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2356 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2357 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2358 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2359 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2360 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2361 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2362 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2363 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2364 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2365 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2366 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2367 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2368 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2369 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2370 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2371 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2372 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2373 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2374 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2375 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2376 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2377 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2378 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2379 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2380 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2381 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2382 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2383 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2384 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2385 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2386 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2387 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2388 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2389 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2390 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2391 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2392 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2393 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2394 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2395 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2396 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2397 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2398 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2399 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2400 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2401 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2402 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2403 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2404 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2405 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2406 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2407 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2408 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2409 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2410 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2411 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2412 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2413 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2414 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2415 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2416 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2417 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2418 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2419 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2420 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2421 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2422 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2423 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2424 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2425 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2426 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2427 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2428 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2429 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2430 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2431 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2432 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2433 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2434 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2435 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2436 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2437 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2438 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2439 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2440 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2441 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2442 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2443 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2444 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2445 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2446 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2447 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2448 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2449 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2450 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2451 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2452 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2453 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2454 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2455 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2456 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2457 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2458 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2459 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2460 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2461 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2462 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2463 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2464 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2465 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2466 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2467 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2468 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2469 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2470 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2471 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2472 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2473 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2474 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2475 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2476 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2477 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2478 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2479 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2480 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2481 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2482 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2483 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2484 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2485 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2486 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2487 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2488 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2489 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2490 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2491 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2492 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2493 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2494 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2495 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2496 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2497 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2498 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2499 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2500 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2501 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2502 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2503 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2504 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2505 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2506 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2507 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2508 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2509 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2510 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2511 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2512 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2513 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2514 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2515 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2516 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2517 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2518 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2519 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2520 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2521 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2522 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2523 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2524 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2525 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2526 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2527 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2528 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2529 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2530 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2531 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2532 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2533 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2534 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2535 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2536 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2537 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2538 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2539 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2540 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2541 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2542 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2543 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2544 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2545 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2546 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2547 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2548 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2549 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2550 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2551 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2552 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2553 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2554 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2555 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2556 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2557 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2558 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2559 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2560 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2561 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2562 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2563 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2564 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2565 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2566 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2567 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2568 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2569 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2570 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2571 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2572 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2573 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2574 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2575 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2576 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2577 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2578 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2579 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2580 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2581 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2582 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2583 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2584 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2585 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2586 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2587 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2588 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2589 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2590 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2591 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2592 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2593 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2594 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2595 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2596 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2597 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2598 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2599 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2600 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2601 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2602 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2603 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2604 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2605 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2606 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2607 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2608 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2609 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2610 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2611 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2612 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2613 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2614 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2615 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2616 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2617 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2618 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2619 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2620 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2621 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2622 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2623 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2624 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2625 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2626 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2627 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2628 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2629 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2630 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2631 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2632 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2633 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2634 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2635 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2636 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2637 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2638 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2639 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2640 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2641 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2642 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2643 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2644 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2645 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2646 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2647 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2648 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2649 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2650 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2651 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2652 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2653 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2654 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2655 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2656 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2657 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2658 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2659 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2660 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2661 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2662 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2663 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2664 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2665 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2666 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2667 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2668 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2669 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2670 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2671 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2672 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2673 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2674 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2675 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2676 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2677 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2678 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2679 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2680 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2681 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2682 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2683 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2684 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2685 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2686 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2687 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2688 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2689 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2690 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2691 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2692 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2693 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2694 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2695 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2696 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2697 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2698 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2699 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2700 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2701 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2702 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2703 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2704 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2705 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2706 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2707 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2708 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2709 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2710 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2711 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2712 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2713 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2714 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2715 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2716 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2717 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2718 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2719 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2720 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2721 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2722 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2723 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2724 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2725 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2726 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2727 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2728 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2729 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2730 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2731 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2732 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2733 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2734 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2735 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2736 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2737 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2738 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2739 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2740 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2741 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2742 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2743 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2744 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2745 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2746 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2747 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2748 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2749 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2750 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2751 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2752 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2753 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2754 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2755 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2756 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2757 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2758 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2759 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2760 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2761 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2762 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2763 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2764 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2765 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2766 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2767 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2768 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2769 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2770 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2771 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2772 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2773 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2774 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2775 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2776 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2777 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2778 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2779 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2780 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2781 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2782 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2783 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2784 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2785 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2786 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2787 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2788 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2789 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2790 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2791 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2792 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2793 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2794 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2795 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2796 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2797 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2798 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2799 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2800 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2801 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2802 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2803 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2804 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2805 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2806 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2807 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2808 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2809 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2810 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2811 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2812 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2813 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2814 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2815 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2816 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2817 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2818 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2819 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2820 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2821 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2822 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2823 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2824 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2825 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2826 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2827 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2828 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2829 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2830 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2831 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2832 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2833 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2834 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2835 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2836 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2837 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2838 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2839 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2840 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2841 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2842 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2843 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2844 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2845 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2846 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2847 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2848 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2849 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2850 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2851 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2852 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2853 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2854 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2855 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2856 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2857 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2858 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2859 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2860 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2861 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2862 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2863 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2864 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2865 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2866 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2867 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2868 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2869 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2870 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2871 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2872 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2873 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2874 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2875 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2876 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2877 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2878 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2879 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2880 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2881 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2882 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2883 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2884 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2885 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2886 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2887 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2888 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2889 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2890 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2891 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2892 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2893 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2894 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2895 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2896 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2897 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2898 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2899 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2900 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2901 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2902 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2903 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2904 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2905 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2906 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2907 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2908 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2909 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2910 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2911 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2912 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2913 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2914 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2915 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2916 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2917 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2918 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2919 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2920 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2921 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2922 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2923 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2924 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2925 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2926 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2927 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2928 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2929 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2930 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2931 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2932 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2933 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2934 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2935 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2936 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2937 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2938 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2939 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2940 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2941 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2942 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2943 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2944 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2945 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2946 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2947 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2948 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2949 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2950 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2951 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2952 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2953 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2954 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2955 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2956 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2957 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2958 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2959 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2960 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2961 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2962 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2963 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2964 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2965 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2966 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2967 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2968 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2969 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2970 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2971 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2972 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2973 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2974 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2975 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2976 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2977 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2978 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2979 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2980 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2981 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2982 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2983 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2984 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2985 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2986 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2987 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2988 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2989 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2990 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2991 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2992 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2993 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2994 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2995 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2996 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2997 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2998 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2999 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3000 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3001 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3002 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3003 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3004 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3005 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3006 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3007 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3008 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3009 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3010 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3011 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3012 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3013 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3014 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3015 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3016 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3017 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3018 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3019 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3020 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3021 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3022 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3023 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3024 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3025 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3026 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3027 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3028 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3029 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3030 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3031 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3032 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3033 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3034 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3035 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3036 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3037 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3038 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3039 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3040 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3041 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3042 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3043 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3044 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3045 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3046 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3047 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3048 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3049 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3050 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3051 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3052 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3053 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3054 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3055 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3056 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3057 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3058 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3059 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3060 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3061 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3062 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3063 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3064 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3065 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3066 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3067 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3068 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3069 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3070 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3071 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3072 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3073 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3074 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3075 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3076 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3077 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3078 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3079 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3080 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3081 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3082 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3083 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3084 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3085 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3086 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3087 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3088 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3089 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3090 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3091 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3092 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3093 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3094 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3095 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3096 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3097 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3098 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3099 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3100 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3101 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3102 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3103 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3104 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3105 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3106 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3107 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3108 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3109 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3110 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3111 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3112 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3113 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3114 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3115 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3116 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3117 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3118 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3119 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3120 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3121 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3122 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3123 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3124 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3125 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3126 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3127 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3128 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3129 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3130 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3131 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3132 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3133 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3134 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3135 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3136 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3137 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3138 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3139 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3140 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3141 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3142 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3143 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3144 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3145 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3146 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3147 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3148 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3149 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3150 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3151 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3152 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3153 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3154 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3155 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3156 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3157 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3158 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3159 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3160 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3161 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3162 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3163 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3164 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3165 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3166 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3167 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3168 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3169 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3170 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3171 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3172 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3173 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3174 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3175 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3176 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3177 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3178 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3179 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3180 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3181 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3182 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3183 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3184 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3185 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3186 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3187 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3188 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3189 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3190 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3191 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3192 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3193 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3194 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3195 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3196 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3197 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3198 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3199 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3200 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3201 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3202 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3203 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3204 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3205 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3206 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3207 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3208 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3209 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3210 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3211 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3212 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3213 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3214 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3215 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3216 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3217 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3218 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3219 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3220 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3221 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3222 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3223 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3224 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3225 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3226 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3227 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3228 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3229 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3230 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3231 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3232 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3233 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3234 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3235 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3236 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3237 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3238 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3239 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3240 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3241 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3242 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3243 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3244 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3245 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3246 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3247 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3248 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3249 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3250 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3251 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3252 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3253 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3254 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3255 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3256 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3257 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3258 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3259 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3260 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3261 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3262 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3263 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3264 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3265 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3266 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3267 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3268 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3269 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3270 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3271 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3272 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3273 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3274 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3275 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3276 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3277 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3278 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3279 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3280 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3281 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3282 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3283 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3284 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3285 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3286 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3287 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3288 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3289 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3290 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3291 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3292 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3293 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3294 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3295 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3296 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3297 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3298 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3299 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3300 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3301 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3302 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3303 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3304 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3305 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3306 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3307 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3308 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3309 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3310 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3311 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3312 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3313 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3314 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3315 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3316 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3317 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3318 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3319 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3320 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3321 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3322 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3323 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3324 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3325 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3326 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3327 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3328 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3329 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3330 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3331 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3332 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3333 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3334 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3335 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3336 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3337 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3338 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3339 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3340 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3341 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3342 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3343 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3344 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3345 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3346 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3347 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3348 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3349 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3350 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3351 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3352 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3353 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3354 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3355 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3356 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3357 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3358 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3359 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3360 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3361 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3362 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3363 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3364 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3365 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3366 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3367 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3368 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3369 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3370 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3371 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3372 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3373 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3374 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3375 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3376 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3377 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3378 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3379 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3380 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3381 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3382 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3383 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3384 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3385 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3386 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3387 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3388 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3389 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3390 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3391 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3392 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3393 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3394 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3395 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3396 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3397 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3398 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3399 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3400 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3401 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3402 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3403 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3404 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3405 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3406 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3407 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3408 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3409 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3410 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3411 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3412 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3413 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3414 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3415 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3416 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3417 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3418 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3419 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3420 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3421 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3422 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3423 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3424 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3425 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3426 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3427 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3428 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3429 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3430 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3431 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3432 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3433 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3434 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3435 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3436 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3437 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3438 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3439 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3440 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3441 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3442 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3443 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3444 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3445 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3446 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3447 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3448 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3449 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3450 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3451 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3452 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3453 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3454 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3455 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3456 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3457 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3458 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3459 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3460 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3461 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3462 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3463 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3464 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3465 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3466 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3467 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3468 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3469 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3470 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3471 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3472 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3473 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3474 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3475 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3476 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3477 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3478 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3479 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3480 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3481 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3482 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3483 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3484 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3485 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3486 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3487 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3488 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3489 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3490 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3491 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3492 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3493 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3494 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3495 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3496 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3497 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3498 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3499 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3500 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3501 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3502 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3503 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3504 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3505 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3506 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3507 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3508 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3509 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3510 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3511 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3512 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3513 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3514 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3515 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3516 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3517 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3518 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3519 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3520 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3521 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3522 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3523 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3524 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3525 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3526 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3527 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3528 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3529 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3530 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3531 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3532 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3533 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3534 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3535 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3536 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3537 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3538 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3539 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3540 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3541 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3542 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3543 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3544 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3545 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3546 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3547 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3548 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3549 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3550 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3551 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3552 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3553 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3554 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3555 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3556 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3557 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3558 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3559 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3560 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3561 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3562 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3563 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3564 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3565 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3566 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3567 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3568 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3569 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3570 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3571 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3572 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3573 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3574 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3575 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3576 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3577 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3578 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3579 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3580 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3581 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3582 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3583 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3584 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3585 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3586 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3587 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3588 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3589 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3590 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3591 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3592 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3593 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3594 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3595 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3596 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3597 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3598 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3599 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3600 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3601 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3602 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3603 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3604 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3605 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3606 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3607 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3608 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3609 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3610 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3611 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3612 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3613 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3614 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3615 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3616 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3617 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3618 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3619 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3620 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3621 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3622 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3623 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3624 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3625 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3626 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3627 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3628 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3629 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3630 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3631 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3632 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3633 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3634 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3635 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3636 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3637 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3638 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3639 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3640 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3641 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3642 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3643 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3644 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3645 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3646 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3647 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3648 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3649 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3650 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3651 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3652 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3653 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3654 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3655 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3656 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3657 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3658 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3659 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3660 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3661 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3662 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3663 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3664 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3665 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3666 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3667 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3668 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3669 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3670 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3671 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3672 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3673 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3674 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3675 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3676 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3677 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3678 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3679 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3680 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3681 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3682 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3683 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3684 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3685 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3686 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3687 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3688 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3689 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3690 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3691 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3692 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3693 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3694 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3695 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3696 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3697 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3698 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3699 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3700 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3701 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3702 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3703 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3704 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3705 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3706 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3707 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3708 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3709 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3710 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3711 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3712 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3713 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3714 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3715 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3716 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3717 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3718 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3719 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3720 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3721 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3722 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3723 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3724 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3725 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3726 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3727 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3728 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3729 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3730 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3731 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3732 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3733 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3734 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3735 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3736 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3737 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3738 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3739 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3740 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3741 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3742 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3743 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3744 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3745 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3746 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3747 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3748 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3749 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3750 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3751 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3752 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3753 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3754 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3755 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3756 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3757 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3758 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3759 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3760 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3761 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3762 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3763 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3764 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3765 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3766 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3767 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3768 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3769 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3770 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3771 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3772 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3773 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3774 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3775 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3776 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3777 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3778 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3779 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3780 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3781 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3782 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3783 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3784 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3785 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3786 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3787 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3788 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3789 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3790 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3791 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3792 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3793 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3794 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3795 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3796 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3797 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3798 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3799 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3800 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3801 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3802 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3803 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3804 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3805 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3806 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3807 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3808 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3809 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3810 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3811 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3812 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3813 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3814 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3815 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3816 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3817 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3818 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3819 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3820 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3821 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3822 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3823 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3824 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3825 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3826 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3827 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3828 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3829 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3830 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3831 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3832 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3833 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3834 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3835 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3836 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3837 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3838 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3839 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3840 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3841 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3842 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3843 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3844 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3845 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3846 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3847 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3848 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3849 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3850 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3851 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3852 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3853 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3854 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3855 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3856 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3857 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3858 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3859 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3860 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3861 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3862 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3863 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3864 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3865 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3866 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3867 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3868 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3869 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3870 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3871 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3872 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3873 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3874 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3875 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3876 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3877 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3878 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3879 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3880 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3881 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3882 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3883 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3884 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3885 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3886 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3887 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3888 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3889 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3890 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3891 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3892 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3893 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3894 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3895 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3896 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3897 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3898 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3899 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3900 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3901 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3902 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3903 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3904 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3905 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3906 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3907 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3908 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3909 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3910 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3911 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3912 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3913 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3914 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3915 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3916 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3917 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3918 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3919 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3920 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3921 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3922 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3923 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3924 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3925 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3926 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3927 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3928 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3929 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3930 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3931 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3932 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3933 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3934 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3935 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3936 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3937 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3938 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3939 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3940 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3941 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3942 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3943 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3944 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3945 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3946 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3947 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3948 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3949 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3950 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3951 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3952 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3953 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3954 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3955 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3956 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3957 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3958 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3959 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3960 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3961 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3962 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3963 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3964 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3965 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3966 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3967 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3968 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3969 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3970 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3971 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3972 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3973 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3974 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3975 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3976 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3977 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3978 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3979 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3980 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3981 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3982 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3983 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3984 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3985 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3986 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3987 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3988 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3989 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3990 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3991 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3992 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3993 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3994 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3995 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3996 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3997 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3998 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3999 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4000 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4001 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4002 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4003 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4004 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4005 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4006 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4007 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4008 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4009 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4010 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4011 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4012 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4013 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4014 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4015 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4016 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4017 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4018 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4019 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4020 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4021 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4022 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4023 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4024 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4025 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4026 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4027 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4028 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4029 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4030 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4031 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4032 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4033 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4034 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4035 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4036 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4037 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4038 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4039 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4040 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4041 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4042 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4043 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4044 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4045 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4046 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4047 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4048 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4049 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4050 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4051 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4052 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4053 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4054 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4055 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4056 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4057 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4058 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4059 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4060 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4061 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4062 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4063 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4064 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4065 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4066 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4067 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4068 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4069 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4070 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4071 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4072 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4073 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4074 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4075 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4076 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4077 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4078 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4079 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4080 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4081 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4082 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4083 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4084 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4085 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4086 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4087 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4088 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4089 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4090 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4091 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4092 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4093 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4094 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4095 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4096 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4097 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4098 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4099 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4100 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4101 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4102 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4103 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4104 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4105 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4106 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4107 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4108 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4109 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4110 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4111 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4112 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4113 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4114 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4115 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4116 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4117 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4118 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4119 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4120 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4121 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4122 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4123 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4124 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4125 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4126 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4127 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4128 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4129 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4130 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4131 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4132 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4133 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4134 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4135 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4136 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4137 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4138 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4139 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4140 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4141 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4142 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4143 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4144 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4145 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4146 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4147 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4148 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4149 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4150 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4151 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4152 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4153 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4154 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4155 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4156 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4157 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4158 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4159 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4160 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4161 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4162 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4163 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4164 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4165 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4166 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4167 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4168 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4169 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4170 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4171 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4172 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4173 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4174 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4175 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4176 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4177 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4178 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4179 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4180 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4181 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4182 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4183 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4184 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4185 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4186 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4187 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4188 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4189 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4190 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4191 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4192 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4193 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4194 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4195 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4196 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4197 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4198 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4199 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4200 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4201 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4202 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4203 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4204 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4205 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4206 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4207 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4208 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4209 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4210 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4211 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4212 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4213 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4214 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4215 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4216 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4217 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4218 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4219 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4220 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4221 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4222 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4223 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4224 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4225 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4226 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4227 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4228 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4229 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4230 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4231 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4232 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4233 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4234 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4235 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4236 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4237 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4238 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4239 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4240 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4241 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4242 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4243 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4244 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4245 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4246 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4247 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4248 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4249 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4250 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4251 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4252 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4253 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4254 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4255 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4256 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4257 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4258 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4259 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4260 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4261 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4262 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4263 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4264 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4265 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4266 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4267 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4268 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4269 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4270 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4271 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4272 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4273 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4274 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4275 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4276 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4277 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4278 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4279 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4280 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4281 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4282 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4283 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4284 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4285 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4286 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4287 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4288 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4289 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4290 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4291 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4292 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4293 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4294 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4295 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4296 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4297 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4298 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4299 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4300 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4301 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4302 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4303 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4304 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4305 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4306 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4307 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4308 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4309 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4310 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4311 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4312 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4313 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4314 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4315 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4316 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4317 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4318 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4319 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4320 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4321 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4322 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4323 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4324 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4325 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4326 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4327 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4328 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4329 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4330 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4331 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4332 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4333 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4334 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4335 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4336 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4337 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4338 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4339 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4340 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4341 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4342 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4343 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4344 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4345 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4346 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4347 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4348 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4349 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4350 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4351 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4352 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4353 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4354 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4355 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4356 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4357 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4358 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4359 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4360 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4361 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4362 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4363 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4364 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4365 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4366 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4367 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4368 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4369 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4370 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4371 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4372 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4373 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4374 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4375 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4376 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4377 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4378 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4379 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4380 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4381 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4382 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4383 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4384 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4385 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4386 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4387 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4388 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4389 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4390 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4391 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4392 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4393 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4394 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4395 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4396 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4397 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4398 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4399 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4400 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4401 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4402 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4403 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4404 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4405 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4406 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4407 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4408 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4409 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4410 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4411 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4412 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4413 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4414 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4415 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4416 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4417 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4418 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4419 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4420 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4421 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4422 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4423 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4424 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4425 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4426 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4427 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4428 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4429 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4430 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4431 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4432 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4433 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4434 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4435 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4436 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4437 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4438 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4439 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4440 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4441 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4442 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4443 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4444 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4445 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4446 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4447 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4448 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4449 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4450 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4451 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4452 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4453 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4454 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4455 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4456 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4457 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4458 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4459 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4460 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4461 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4462 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4463 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4464 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4465 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4466 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4467 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4468 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4469 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4470 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4471 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4472 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4473 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4474 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4475 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4476 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4477 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4478 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4479 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4480 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4481 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4482 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4483 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4484 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4485 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4486 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4487 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4488 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4489 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4490 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4491 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4492 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4493 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4494 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4495 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4496 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4497 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4498 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4499 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4500 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4501 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4502 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4503 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4504 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4505 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4506 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4507 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4508 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4509 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4510 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4511 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4512 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4513 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4514 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4515 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4516 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4517 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4518 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4519 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4520 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4521 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4522 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4523 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4524 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4525 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4526 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4527 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4528 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4529 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4530 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4531 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4532 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4533 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4534 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4535 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4536 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4537 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4538 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4539 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4540 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4541 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4542 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4543 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4544 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4545 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4546 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4547 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4548 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4549 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4550 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4551 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4552 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4553 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4554 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4555 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4556 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4557 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4558 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4559 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4560 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4561 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4562 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4563 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4564 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4565 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4566 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4567 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4568 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4569 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4570 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4571 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4572 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4573 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4574 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4575 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4576 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4577 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4578 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4579 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4580 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4581 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4582 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4583 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4584 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4585 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4586 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4587 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4588 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4589 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4590 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4591 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4592 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4593 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4594 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4595 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4596 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4597 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4598 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4599 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4600 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4601 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4602 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4603 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4604 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4605 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4606 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4607 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4608 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4609 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4610 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4611 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4612 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4613 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4614 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4615 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4616 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4617 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4618 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4619 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4620 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4621 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4622 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4623 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4624 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4625 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4626 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4627 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4628 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4629 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4630 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4631 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4632 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4633 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4634 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4635 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4636 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4637 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4638 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4639 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4640 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4641 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4642 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4643 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4644 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4645 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4646 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4647 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4648 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4649 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4650 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4651 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4652 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4653 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4654 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4655 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4656 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4657 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4658 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4659 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4660 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4661 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4662 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4663 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4664 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4665 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4666 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4667 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4668 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4669 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4670 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4671 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4672 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4673 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4674 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4675 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4676 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4677 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4678 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4679 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4680 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4681 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4682 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4683 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4684 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4685 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4686 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4687 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4688 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4689 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4690 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4691 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4692 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4693 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4694 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4695 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4696 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4697 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4698 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4699 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4700 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4701 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4702 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4703 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4704 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4705 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4706 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4707 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4708 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4709 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4710 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4711 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4712 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4713 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4714 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4715 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4716 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4717 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4718 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4719 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4720 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4721 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4722 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4723 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4724 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4725 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4726 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4727 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4728 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4729 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4730 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4731 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4732 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4733 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4734 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4735 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4736 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4737 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4738 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4739 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4740 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4741 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4742 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4743 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4744 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4745 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4746 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4747 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4748 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4749 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4750 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4751 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4752 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4753 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4754 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4755 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4756 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4757 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4758 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4759 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4760 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4761 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4762 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4763 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4764 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4765 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4766 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4767 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4768 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4769 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4770 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4771 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4772 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4773 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4774 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4775 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4776 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4777 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4778 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4779 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4780 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4781 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4782 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4783 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4784 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4785 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4786 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4787 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4788 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4789 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4790 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4791 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4792 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4793 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4794 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4795 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4796 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4797 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4798 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4799 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4800 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4801 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4802 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4803 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4804 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4805 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4806 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4807 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4808 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4809 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4810 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4811 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4812 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4813 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4814 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4815 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4816 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4817 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4818 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4819 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4820 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4821 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4822 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4823 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4824 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4825 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4826 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4827 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4828 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4829 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4830 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4831 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4832 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4833 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4834 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4835 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4836 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4837 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4838 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4839 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4840 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4841 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4842 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4843 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4844 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4845 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4846 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4847 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4848 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4849 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4850 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4851 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4852 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4853 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4854 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4855 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4856 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4857 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4858 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4859 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4860 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4861 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4862 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4863 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4864 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4865 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4866 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4867 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4868 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4869 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4870 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4871 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4872 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4873 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4874 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4875 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4876 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4877 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4878 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4879 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4880 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4881 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4882 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4883 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4884 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4885 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4886 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4887 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4888 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4889 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4890 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4891 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4892 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4893 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4894 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4895 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4896 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4897 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4898 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4899 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4900 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4901 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4902 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4903 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4904 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4905 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4906 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4907 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4908 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4909 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4910 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4911 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4912 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4913 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4914 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4915 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4916 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4917 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4918 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4919 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4920 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4921 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4922 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4923 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4924 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4925 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4926 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4927 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4928 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4929 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4930 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4931 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4932 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4933 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4934 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4935 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4936 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4937 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4938 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4939 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4940 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4941 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4942 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4943 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4944 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4945 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4946 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4947 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4948 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4949 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4950 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4951 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4952 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4953 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4954 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4955 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4956 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4957 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4958 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4959 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4960 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4961 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4962 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4963 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4964 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4965 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4966 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4967 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4968 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4969 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4970 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4971 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4972 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4973 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4974 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4975 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4976 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4977 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4978 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4979 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4980 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4981 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4982 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4983 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4984 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4985 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4986 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4987 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4988 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4989 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4990 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4991 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4992 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4993 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4994 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4995 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4996 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4997 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4998 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4999 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b5000 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b5001 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b5002 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b5003 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b5004 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b5005 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b5006 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b5007 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b5008 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b5009 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b5010 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b5011 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b5012 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b5013 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b5014 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b5015 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b5016 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b5017 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b5018 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b5019 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b5020 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b5021 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b5022 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b5023 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b5024 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b5025 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b5026 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b5027 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=   1297.5511*m.b907 + 1780.034*m.b908 + 1897.1415*m.b909 + 2595.1022*m.b910 + 3513.225*m.b911
                        + 4328.2932*m.b912 + 5766.3733*m.b913 + 6647.0217*m.b914 + 7930.5199*m.b915 + 8970.4345*m.b916
                        + 11523.378*m.b917 + 14971.0228*m.b918 + 18320.2973*m.b919 + 1105.4516*m.b920 + 1516.504*m.b921
                        + 1616.274*m.b922 + 2210.9032*m.b923 + 2993.1*m.b924 + 3687.4992*m.b925 + 4912.6748*m.b926
                        + 5662.9452*m.b927 + 6756.4244*m.b928 + 7642.382*m.b929 + 9817.368*m.b930 + 12754.5968*m.b931
                        + 15608.0188*m.b932 + 1580.7005*m.b933 + 2168.47*m.b934 + 2311.1325*m.b935 + 3161.401*m.b936
                        + 4279.875*m.b937 + 5272.806*m.b938 + 7024.7015*m.b939 + 8097.5235*m.b940 + 9661.1045*m.b941
                        + 10927.9475*m.b942 + 14037.99*m.b943 + 18237.974*m.b944 + 22318.1215*m.b945 + 1160.7962*m.b946
                        + 1592.428*m.b947 + 1697.193*m.b948 + 2321.5924*m.b949 + 3142.95*m.b950 + 3872.1144*m.b951
                        + 5158.6286*m.b952 + 5946.4614*m.b953 + 7094.6858*m.b954 + 8024.999*m.b955 + 10308.876*m.b956
                        + 13393.1576*m.b957 + 16389.4366*m.b958 + 14987.5005*m.b959 + 20560.47*m.b960
                        + 21913.1325*m.b961 + 29975.001*m.b962 + 40579.875*m.b963 + 49994.406*m.b964 + 66605.1015*m.b965
                        + 76777.1235*m.b966 + 91602.3045*m.b967 + 103613.9475*m.b968 + 133101.99*m.b969
                        + 172924.374*m.b970 + 211610.5215*m.b971 + 15021.5438*m.b972 + 20607.172*m.b973
                        + 21962.907*m.b974 + 30043.0876*m.b975 + 40672.05*m.b976 + 50107.9656*m.b977 + 66756.3914*m.b978
                        + 76951.5186*m.b979 + 91810.3742*m.b980 + 103849.301*m.b981 + 133404.324*m.b982
                        + 173317.1624*m.b983 + 212091.1834*m.b984 + 16966.2777*m.b985 + 23275.038*m.b986
                        + 24806.2905*m.b987 + 33932.5554*m.b988 + 45937.575*m.b989 + 56595.0924*m.b990
                        + 75398.8731*m.b991 + 86913.8919*m.b992 + 103696.4193*m.b993 + 117293.9415*m.b994
                        + 150675.246*m.b995 + 195755.3196*m.b996 + 239549.1411*m.b997 + 11210.6332*m.b998
                        + 15379.208*m.b999 + 16390.998*m.b1000 + 22421.2664*m.b1001 + 30353.7*m.b1002
                        + 37395.7584*m.b1003 + 49820.5396*m.b1004 + 57429.2004*m.b1005 + 68518.4188*m.b1006
                        + 77503.114*m.b1007 + 99560.136*m.b1008 + 129347.2336*m.b1009 + 158284.4276*m.b1010
                        + 5750.6585*m.b1011 + 7888.99*m.b1012 + 8408.0025*m.b1013 + 11501.317*m.b1014
                        + 15570.375*m.b1015 + 19182.702*m.b1016 + 25556.1755*m.b1017 + 29459.1495*m.b1018
                        + 35147.5265*m.b1019 + 39756.3575*m.b1020 + 51070.83*m.b1021 + 66350.558*m.b1022
                        + 81194.3155*m.b1023 + 4201.3144*m.b1024 + 5763.536*m.b1025 + 6142.716*m.b1026
                        + 8402.6288*m.b1027 + 11375.4*m.b1028 + 14014.4928*m.b1029 + 18670.8232*m.b1030
                        + 21522.2568*m.b1031 + 25678.0696*m.b1032 + 29045.188*m.b1033 + 37311.312*m.b1034
                        + 48474.3712*m.b1035 + 59318.9192*m.b1036 + 14590.6426*m.b1037 + 20016.044*m.b1038
                        + 21332.889*m.b1039 + 29181.2852*m.b1040 + 39505.35*m.b1041 + 48670.5912*m.b1042
                        + 64841.4478*m.b1043 + 74744.1222*m.b1044 + 89176.7434*m.b1045 + 100870.327*m.b1046
                        + 129577.548*m.b1047 + 168345.4648*m.b1048 + 206007.2318*m.b1049 + 653.1937*m.b1050
                        + 896.078*m.b1051 + 955.0305*m.b1052 + 1306.3874*m.b1053 + 1768.575*m.b1054 + 2178.8844*m.b1055
                        + 2902.8211*m.b1056 + 3346.1439*m.b1057 + 3992.2633*m.b1058 + 4515.7615*m.b1059
                        + 5800.926*m.b1060 + 7536.4876*m.b1061 + 9222.5291*m.b1062 + 7365.9009*m.b1063
                        + 10104.846*m.b1064 + 10769.6385*m.b1065 + 14731.8018*m.b1066 + 19943.775*m.b1067
                        + 24570.7308*m.b1068 + 32734.3827*m.b1069 + 37733.6223*m.b1070 + 45019.7481*m.b1071
                        + 50923.1055*m.b1072 + 65415.582*m.b1073 + 84987.0732*m.b1074 + 104000.1387*m.b1075
                        + 9847.7655*m.b1076 + 13509.57*m.b1077 + 14398.3575*m.b1078 + 19695.531*m.b1079
                        + 26663.625*m.b1080 + 32849.586*m.b1081 + 43763.8965*m.b1082 + 50447.5785*m.b1083
                        + 60188.6895*m.b1084 + 68081.1225*m.b1085 + 87456.69*m.b1086 + 113622.594*m.b1087
                        + 139041.9165*m.b1088 + 10997.5094*m.b1089 + 15086.836*m.b1090 + 16079.391*m.b1091
                        + 21995.0188*m.b1092 + 29776.65*m.b1093 + 36684.8328*m.b1094 + 48873.4082*m.b1095
                        + 56337.4218*m.b1096 + 67215.8246*m.b1097 + 76029.713*m.b1098 + 97667.412*m.b1099
                        + 126888.2312*m.b1100 + 155275.3042*m.b1101 + 14372.6159*m.b1102 + 19716.946*m.b1103
                        + 21014.1135*m.b1104 + 28745.2318*m.b1105 + 38915.025*m.b1106 + 47943.3108*m.b1107
                        + 63872.5277*m.b1108 + 73627.2273*m.b1109 + 87844.1831*m.b1110 + 99363.0305*m.b1111
                        + 127641.282*m.b1112 + 165829.8932*m.b1113 + 202928.8837*m.b1114 + 7553.2914*m.b1115
                        + 10361.916*m.b1116 + 11043.621*m.b1117 + 15106.5828*m.b1118 + 20451.15*m.b1119
                        + 25195.8168*m.b1120 + 33567.1542*m.b1121 + 38693.5758*m.b1122 + 46165.0626*m.b1123
                        + 52218.603*m.b1124 + 67079.772*m.b1125 + 87149.1672*m.b1126 + 106645.9302*m.b1127
                        + 11269.6342*m.b1128 + 15460.148*m.b1129 + 16477.263*m.b1130 + 22539.2684*m.b1131
                        + 30513.45*m.b1132 + 37592.5704*m.b1133 + 50082.7426*m.b1134 + 57731.4474*m.b1135
                        + 68879.0278*m.b1136 + 77911.009*m.b1137 + 100084.116*m.b1138 + 130027.9816*m.b1139
                        + 159117.4706*m.b1140 + 15379.8156*m.b1141 + 21098.664*m.b1142 + 22486.734*m.b1143
                        + 30759.6312*m.b1144 + 41642.1*m.b1145 + 51303.0672*m.b1146 + 68348.5668*m.b1147
                        + 78786.8532*m.b1148 + 94000.1004*m.b1149 + 106326.162*m.b1150 + 136586.088*m.b1151
                        + 177450.8688*m.b1152 + 217149.6708*m.b1153 + 14728.4501*m.b1154 + 20205.094*m.b1155
                        + 21534.3765*m.b1156 + 29456.9002*m.b1157 + 39878.475*m.b1158 + 49130.2812*m.b1159
                        + 65453.8703*m.b1160 + 75450.0747*m.b1161 + 90019.0109*m.b1162 + 101823.0395*m.b1163
                        + 130801.398*m.b1164 + 169935.4748*m.b1165 + 207952.9543*m.b1166 + 4445.85*m.b1167
                        + 6099*m.b1168 + 6500.25*m.b1169 + 8891.7*m.b1170 + 12037.5*m.b1171 + 14830.2*m.b1172
                        + 19757.55*m.b1173 + 22774.95*m.b1174 + 27172.65*m.b1175 + 30735.75*m.b1176 + 39483*m.b1177
                        + 51295.8*m.b1178 + 62771.55*m.b1179 + 3275.9128*m.b1180 + 4494.032*m.b1181 + 4789.692*m.b1182
                        + 6551.8256*m.b1183 + 8869.8*m.b1184 + 10927.5936*m.b1185 + 14558.2984*m.b1186
                        + 16781.6616*m.b1187 + 20022.0952*m.b1188 + 22647.556*m.b1189 + 29092.944*m.b1190
                        + 37797.1744*m.b1191 + 46253.0504*m.b1192 + 9027.5408*m.b1193 + 12384.352*m.b1194
                        + 13199.112*m.b1195 + 18055.0816*m.b1196 + 24442.8*m.b1197 + 30113.5296*m.b1198
                        + 40118.7824*m.b1199 + 46245.7776*m.b1200 + 55175.5472*m.b1201 + 62410.616*m.b1202
                        + 80172.384*m.b1203 + 104158.9184*m.b1204 + 127461.0544*m.b1205 + 7414.6529*m.b1206
                        + 10171.726*m.b1207 + 10840.9185*m.b1208 + 14829.3058*m.b1209 + 20075.775*m.b1210
                        + 24733.3548*m.b1211 + 32951.0387*m.b1212 + 37983.3663*m.b1213 + 45317.7161*m.b1214
                        + 51260.1455*m.b1215 + 65848.542*m.b1216 + 85549.5692*m.b1217 + 104688.4747*m.b1218
                        + 810.8067*m.b1219 + 1112.298*m.b1220 + 1185.4755*m.b1221 + 1621.6134*m.b1222 + 2195.325*m.b1223
                        + 2704.6404*m.b1224 + 3603.2601*m.b1225 + 4153.5549*m.b1226 + 4955.5803*m.b1227
                        + 5605.3965*m.b1228 + 7200.666*m.b1229 + 9355.0116*m.b1230 + 11447.8881*m.b1231
                        + 4735.0103*m.b1232 + 6495.682*m.b1233 + 6923.0295*m.b1234 + 9470.0206*m.b1235
                        + 12820.425*m.b1236 + 15794.7636*m.b1237 + 21042.5909*m.b1238 + 24256.2441*m.b1239
                        + 28939.9727*m.b1240 + 32734.8185*m.b1241 + 42050.994*m.b1242 + 54632.1044*m.b1243
                        + 66854.2429*m.b1244 + 3568.3971*m.b1245 + 4895.274*m.b1246 + 5217.3315*m.b1247
                        + 7136.7942*m.b1248 + 9661.725*m.b1249 + 11903.2452*m.b1250 + 15858.1113*m.b1251
                        + 18279.9837*m.b1252 + 21809.7339*m.b1253 + 24669.6045*m.b1254 + 31690.458*m.b1255
                        + 41171.8308*m.b1256 + 50382.6753*m.b1257 + 1177.804*m.b1258 + 1615.76*m.b1259 + 1722.06*m.b1260
                        + 2355.608*m.b1261 + 3189*m.b1262 + 3928.848*m.b1263 + 5234.212*m.b1264 + 6033.588*m.b1265
                        + 7198.636*m.b1266 + 8142.58*m.b1267 + 10459.92*m.b1268 + 13589.392*m.b1269 + 16629.572*m.b1270
                        + 5129.3198*m.b1271 + 7036.612*m.b1272 + 7499.547*m.b1273 + 10258.6396*m.b1274
                        + 13888.05*m.b1275 + 17110.0776*m.b1276 + 22794.9194*m.b1277 + 26276.1906*m.b1278
                        + 31349.9582*m.b1279 + 35460.821*m.b1280 + 45552.804*m.b1281 + 59181.6104*m.b1282
                        + 72421.5514*m.b1283 + 6191.4486*m.b1284 + 8493.684*m.b1285 + 9052.479*m.b1286
                        + 12382.8972*m.b1287 + 16763.85*m.b1288 + 20653.0632*m.b1289 + 27515.0658*m.b1290
                        + 31717.2042*m.b1291 + 37841.5974*m.b1292 + 42803.697*m.b1293 + 54985.428*m.b1294
                        + 71436.3528*m.b1295 + 87417.8898*m.b1296 + 10006.4311*m.b1297 + 13727.234*m.b1298
                        + 14630.3415*m.b1299 + 20012.8622*m.b1300 + 27093.225*m.b1301 + 33378.8532*m.b1302
                        + 44469.0133*m.b1303 + 51260.3817*m.b1304 + 61158.4399*m.b1305 + 69178.0345*m.b1306
                        + 88865.778*m.b1307 + 115453.2628*m.b1308 + 141282.1373*m.b1309 + 5256.8229*m.b1310
                        + 7211.526*m.b1311 + 7685.9685*m.b1312 + 10513.6458*m.b1313 + 14233.275*m.b1314
                        + 17535.3948*m.b1315 + 23361.5487*m.b1316 + 26929.3563*m.b1317 + 32129.2461*m.b1318
                        + 36342.2955*m.b1319 + 46685.142*m.b1320 + 60652.7292*m.b1321 + 74221.7847*m.b1322
                        + 6665.8388*m.b1323 + 9144.472*m.b1324 + 9746.082*m.b1325 + 13331.6776*m.b1326 + 18048.3*m.b1327
                        + 22235.5056*m.b1328 + 29623.2764*m.b1329 + 34147.3836*m.b1330 + 40741.0292*m.b1331
                        + 46083.326*m.b1332 + 59198.424*m.b1333 + 76909.8224*m.b1334 + 94115.8684*m.b1335
                        + 6402.024*m.b1336 + 8782.56*m.b1337 + 9360.36*m.b1338 + 12804.048*m.b1339 + 17334*m.b1340
                        + 21355.488*m.b1341 + 28450.872*m.b1342 + 32795.928*m.b1343 + 39128.616*m.b1344
                        + 44259.48*m.b1345 + 56855.52*m.b1346 + 73865.952*m.b1347 + 90391.032*m.b1348
                        + 18678.7471*m.b1349 + 25624.274*m.b1350 + 27310.0815*m.b1351 + 37357.4942*m.b1352
                        + 50574.225*m.b1353 + 62307.4452*m.b1354 + 83009.1613*m.b1355 + 95686.4337*m.b1356
                        + 114162.8839*m.b1357 + 129132.8545*m.b1358 + 165883.458*m.b1359 + 215513.6308*m.b1360
                        + 263727.7253*m.b1361 + 3837.4472*m.b1362 + 5264.368*m.b1363 + 5610.708*m.b1364
                        + 7674.8944*m.b1365 + 10390.2*m.b1366 + 12800.7264*m.b1367 + 17053.7816*m.b1368
                        + 19658.2584*m.b1369 + 23454.1448*m.b1370 + 26529.644*m.b1371 + 34079.856*m.b1372
                        + 44276.1056*m.b1373 + 54181.4296*m.b1374 + 1292.482*m.b1375 + 1773.08*m.b1376 + 1889.73*m.b1377
                        + 2584.964*m.b1378 + 3499.5*m.b1379 + 4311.384*m.b1380 + 5743.846*m.b1381 + 6621.054*m.b1382
                        + 7899.538*m.b1383 + 8935.39*m.b1384 + 11478.36*m.b1385 + 14912.536*m.b1386 + 18248.726*m.b1387
                        + 13869.9163*m.b1388 + 19027.322*m.b1389 + 20279.1195*m.b1390 + 27739.8326*m.b1391
                        + 37553.925*m.b1392 + 46266.4356*m.b1393 + 61638.5089*m.b1394 + 71052.0261*m.b1395
                        + 84771.7267*m.b1396 + 95887.6885*m.b1397 + 123176.874*m.b1398 + 160029.7924*m.b1399
                        + 195831.2009*m.b1400 + 1700.5307*m.b1401 + 2332.858*m.b1402 + 2486.3355*m.b1403
                        + 3401.0614*m.b1404 + 4604.325*m.b1405 + 5672.5284*m.b1406 + 7557.2321*m.b1407
                        + 8711.3829*m.b1408 + 10393.4963*m.b1409 + 11756.3765*m.b1410 + 15102.186*m.b1411
                        + 19620.5636*m.b1412 + 24010.0201*m.b1413 + 2042.2102*m.b1414 + 2801.588*m.b1415
                        + 2985.903*m.b1416 + 4084.4204*m.b1417 + 5529.45*m.b1418 + 6812.2824*m.b1419 + 9075.6706*m.b1420
                        + 10461.7194*m.b1421 + 12481.8118*m.b1422 + 14118.529*m.b1423 + 18136.596*m.b1424
                        + 23562.8296*m.b1425 + 28834.2386*m.b1426 + 2303.6428*m.b1427 + 3160.232*m.b1428
                        + 3368.142*m.b1429 + 4607.2856*m.b1430 + 6237.3*m.b1431 + 7684.3536*m.b1432 + 10237.4884*m.b1433
                        + 11800.9716*m.b1434 + 14079.6652*m.b1435 + 15925.906*m.b1436 + 20458.344*m.b1437
                        + 26579.2144*m.b1438 + 32525.4404*m.b1439 + 17612.1863*m.b1440 + 24161.122*m.b1441
                        + 25750.6695*m.b1442 + 35224.3726*m.b1443 + 47686.425*m.b1444 + 58749.6756*m.b1445
                        + 78269.3189*m.b1446 + 90222.7161*m.b1447 + 107644.1567*m.b1448 + 121759.3385*m.b1449
                        + 156411.474*m.b1450 + 203207.7524*m.b1451 + 248668.8109*m.b1452 + 11515.6656*m.b1453
                        + 15797.664*m.b1454 + 16836.984*m.b1455 + 23031.3312*m.b1456 + 31179.6*m.b1457
                        + 38413.2672*m.b1458 + 51176.1168*m.b1459 + 58991.8032*m.b1460 + 70382.7504*m.b1461
                        + 79611.912*m.b1462 + 102269.088*m.b1463 + 132866.6688*m.b1464 + 162591.2208*m.b1465
                        + 3396.0754*m.b1466 + 4658.876*m.b1467 + 4965.381*m.b1468 + 6792.1508*m.b1469 + 9195.15*m.b1470
                        + 11328.4248*m.b1471 + 15092.3062*m.b1472 + 17397.2238*m.b1473 + 20756.5186*m.b1474
                        + 23478.283*m.b1475 + 30160.092*m.b1476 + 39183.5992*m.b1477 + 47949.6422*m.b1478
                        + 3070.6835*m.b1479 + 4212.49*m.b1480 + 4489.6275*m.b1481 + 6141.367*m.b1482 + 8314.125*m.b1483
                        + 10243.002*m.b1484 + 13646.2505*m.b1485 + 15730.3245*m.b1486 + 18767.7515*m.b1487
                        + 21228.7325*m.b1488 + 27270.33*m.b1489 + 35429.258*m.b1490 + 43355.3905*m.b1491
                        + 15440.4786*m.b1492 + 21181.884*m.b1493 + 22575.429*m.b1494 + 30880.9572*m.b1495
                        + 41806.35*m.b1496 + 51505.4232*m.b1497 + 68618.1558*m.b1498 + 79097.6142*m.b1499
                        + 94370.8674*m.b1500 + 106745.547*m.b1501 + 137124.828*m.b1502 + 178150.7928*m.b1503
                        + 218006.1798*m.b1504 + 11203.6251*m.b1505 + 15369.594*m.b1506 + 16380.7515*m.b1507
                        + 22407.2502*m.b1508 + 30334.725*m.b1509 + 37372.3812*m.b1510 + 49789.3953*m.b1511
                        + 57393.2997*m.b1512 + 68475.5859*m.b1513 + 77454.6645*m.b1514 + 99497.898*m.b1515
                        + 129266.3748*m.b1516 + 158185.4793*m.b1517 + 19405.8721*m.b1518 + 26621.774*m.b1519
                        + 28373.2065*m.b1520 + 38811.7442*m.b1521 + 52542.975*m.b1522 + 64732.9452*m.b1523
                        + 86240.5363*m.b1524 + 99411.3087*m.b1525 + 118607.0089*m.b1526 + 134159.7295*m.b1527
                        + 172340.958*m.b1528 + 223903.1308*m.b1529 + 273994.1003*m.b1530 + 9907.4867*m.b1531
                        + 13591.498*m.b1532 + 14485.6755*m.b1533 + 19814.9734*m.b1534 + 26825.325*m.b1535
                        + 33048.8004*m.b1536 + 44029.3001*m.b1537 + 50753.5149*m.b1538 + 60553.7003*m.b1539
                        + 68493.9965*m.b1540 + 87987.066*m.b1541 + 114311.6516*m.b1542 + 139885.1281*m.b1543
                        + 15693.8782*m.b1544 + 21529.508*m.b1545 + 22945.923*m.b1546 + 31387.7564*m.b1547
                        + 42492.45*m.b1548 + 52350.6984*m.b1549 + 69744.2746*m.b1550 + 80395.7154*m.b1551
                        + 95919.6238*m.b1552 + 108497.389*m.b1553 + 139375.236*m.b1554 + 181074.4936*m.b1555
                        + 221583.9626*m.b1556 + 8129.119*m.b1557 + 11151.86*m.b1558 + 11885.535*m.b1559
                        + 16258.238*m.b1560 + 22010.25*m.b1561 + 27116.628*m.b1562 + 36126.157*m.b1563
                        + 41643.393*m.b1564 + 49684.471*m.b1565 + 56199.505*m.b1566 + 72193.62*m.b1567
                        + 93793.012*m.b1568 + 114776.117*m.b1569 + 13331.2344*m.b1570 + 18288.336*m.b1571
                        + 19491.516*m.b1572 + 26662.4688*m.b1573 + 36095.4*m.b1574 + 44469.5328*m.b1575
                        + 59244.5832*m.b1576 + 68292.4968*m.b1577 + 81479.3496*m.b1578 + 92163.588*m.b1579
                        + 118392.912*m.b1580 + 153814.5312*m.b1581 + 188225.4792*m.b1582 + 12853.4371*m.b1583
                        + 17632.874*m.b1584 + 18792.9315*m.b1585 + 25706.8742*m.b1586 + 34801.725*m.b1587
                        + 42875.7252*m.b1588 + 57121.2313*m.b1589 + 65844.8637*m.b1590 + 78559.0939*m.b1591
                        + 88860.4045*m.b1592 + 114149.658*m.b1593 + 148301.7508*m.b1594 + 181479.3953*m.b1595
                        + 4250.7312*m.b1596 + 5831.328*m.b1597 + 6214.968*m.b1598 + 8501.4624*m.b1599 + 11509.2*m.b1600
                        + 14179.3344*m.b1601 + 18890.4336*m.b1602 + 21775.4064*m.b1603 + 25980.1008*m.b1604
                        + 29386.824*m.b1605 + 37750.176*m.b1606 + 49044.5376*m.b1607 + 60016.6416*m.b1608
                        + 2507.4317*m.b1609 + 3439.798*m.b1610 + 3666.1005*m.b1611 + 5014.8634*m.b1612
                        + 6789.075*m.b1613 + 8364.1404*m.b1614 + 11143.1351*m.b1615 + 12844.9299*m.b1616
                        + 15325.2053*m.b1617 + 17334.7715*m.b1618 + 22268.166*m.b1619 + 28930.5116*m.b1620
                        + 35402.7631*m.b1621 + 5114.528*m.b1622 + 7016.32*m.b1623 + 7477.92*m.b1624 + 10229.056*m.b1625
                        + 13848*m.b1626 + 17060.736*m.b1627 + 22729.184*m.b1628 + 26200.416*m.b1629 + 31259.552*m.b1630
                        + 35358.56*m.b1631 + 45421.44*m.b1632 + 59010.944*m.b1633 + 72212.704*m.b1634
                        + 8071.3091*m.b1635 + 11072.554*m.b1636 + 11801.0115*m.b1637 + 16142.6182*m.b1638
                        + 21853.725*m.b1639 + 26923.7892*m.b1640 + 35869.2473*m.b1641 + 41347.2477*m.b1642
                        + 49331.1419*m.b1643 + 55799.8445*m.b1644 + 71680.218*m.b1645 + 93126.0068*m.b1646
                        + 113959.8913*m.b1647 + 787.9542*m.b1648 + 1080.948*m.b1649 + 1152.063*m.b1650
                        + 1575.9084*m.b1651 + 2133.45*m.b1652 + 2628.4104*m.b1653 + 3501.7026*m.b1654
                        + 4036.4874*m.b1655 + 4815.9078*m.b1656 + 5447.409*m.b1657 + 6997.716*m.b1658
                        + 9091.3416*m.b1659 + 11125.2306*m.b1660 + 3127.0807*m.b1661 + 4289.858*m.b1662
                        + 4572.0855*m.b1663 + 6254.1614*m.b1664 + 8466.825*m.b1665 + 10431.1284*m.b1666
                        + 13896.8821*m.b1667 + 16019.2329*m.b1668 + 19112.4463*m.b1669 + 21618.6265*m.b1670
                        + 27771.186*m.b1671 + 36079.9636*m.b1672 + 44151.6701*m.b1673 + 11746.8498*m.b1674
                        + 16114.812*m.b1675 + 17174.997*m.b1676 + 23493.6996*m.b1677 + 31805.55*m.b1678
                        + 39184.4376*m.b1679 + 52203.5094*m.b1680 + 60176.1006*m.b1681 + 71795.7282*m.b1682
                        + 81210.171*m.b1683 + 104322.204*m.b1684 + 135534.0504*m.b1685 + 165855.3414*m.b1686
                        + 5242.6682*m.b1687 + 7192.108*m.b1688 + 7665.273*m.b1689 + 10485.3364*m.b1690
                        + 14194.95*m.b1691 + 17488.1784*m.b1692 + 23298.6446*m.b1693 + 26856.8454*m.b1694
                        + 32042.7338*m.b1695 + 36244.439*m.b1696 + 46559.436*m.b1697 + 60489.4136*m.b1698
                        + 74021.9326*m.b1699 + 5936.7748*m.b1700 + 8144.312*m.b1701 + 8680.122*m.b1702
                        + 11873.5496*m.b1703 + 16074.3*m.b1704 + 19803.5376*m.b1705 + 26383.2844*m.b1706
                        + 30412.5756*m.b1707 + 36285.0532*m.b1708 + 41043.046*m.b1709 + 52723.704*m.b1710
                        + 68497.9504*m.b1711 + 83822.1164*m.b1712 + 7209.756*m.b1713 + 9890.64*m.b1714
                        + 10541.34*m.b1715 + 14419.512*m.b1716 + 19521*m.b1717 + 24049.872*m.b1718 + 32040.468*m.b1719
                        + 36933.732*m.b1720 + 44065.404*m.b1721 + 49843.62*m.b1722 + 64028.88*m.b1723
                        + 83185.488*m.b1724 + 101795.508*m.b1725 + 1070.1895*m.b1726 + 1468.13*m.b1727
                        + 1564.7175*m.b1728 + 2140.379*m.b1729 + 2897.625*m.b1730 + 3569.874*m.b1731 + 4755.9685*m.b1732
                        + 5482.3065*m.b1733 + 6540.9055*m.b1734 + 7398.6025*m.b1735 + 9504.21*m.b1736
                        + 12347.746*m.b1737 + 15110.1485*m.b1738 + 11697.156*m.b1739 + 16046.64*m.b1740
                        + 17102.34*m.b1741 + 23394.312*m.b1742 + 31671*m.b1743 + 39018.672*m.b1744 + 51982.668*m.b1745
                        + 59921.532*m.b1746 + 71492.004*m.b1747 + 80866.62*m.b1748 + 103880.88*m.b1749
                        + 134960.688*m.b1750 + 165153.708*m.b1751 + 4310.8956*m.b1752 + 5913.864*m.b1753
                        + 6302.934*m.b1754 + 8621.7912*m.b1755 + 11672.1*m.b1756 + 14380.0272*m.b1757
                        + 19157.8068*m.b1758 + 22083.6132*m.b1759 + 26347.8204*m.b1760 + 29802.762*m.b1761
                        + 38284.488*m.b1762 + 49738.7088*m.b1763 + 60866.1108*m.b1764 + 7751.6511*m.b1765
                        + 10634.034*m.b1766 + 11333.6415*m.b1767 + 15503.3022*m.b1768 + 20988.225*m.b1769
                        + 25857.4932*m.b1770 + 34448.6733*m.b1771 + 39709.7217*m.b1772 + 47377.4199*m.b1773
                        + 53589.9345*m.b1774 + 68841.378*m.b1775 + 89437.8228*m.b1776 + 109446.5973*m.b1777
                        + 7914.8041*m.b1778 + 10857.854*m.b1779 + 11572.1865*m.b1780 + 15829.6082*m.b1781
                        + 21429.975*m.b1782 + 26401.7292*m.b1783 + 35173.7323*m.b1784 + 40545.5127*m.b1785
                        + 48374.5969*m.b1786 + 54717.8695*m.b1787 + 70290.318*m.b1788 + 91320.2668*m.b1789
                        + 111750.1763*m.b1790 + 8939.2609*m.b1791 + 12263.246*m.b1792 + 13070.0385*m.b1793
                        + 17878.5218*m.b1794 + 24203.775*m.b1795 + 29819.0508*m.b1796 + 39726.4627*m.b1797
                        + 45793.5423*m.b1798 + 54635.9881*m.b1799 + 61800.3055*m.b1800 + 79388.382*m.b1801
                        + 103140.3532*m.b1802 + 126214.6187*m.b1803 + 7343.547*m.b1804 + 10074.18*m.b1805
                        + 10736.955*m.b1806 + 14687.094*m.b1807 + 19883.25*m.b1808 + 24496.164*m.b1809
                        + 32635.041*m.b1810 + 37619.109*m.b1811 + 44883.123*m.b1812 + 50768.565*m.b1813
                        + 65217.06*m.b1814 + 84729.156*m.b1815 + 103684.521*m.b1816 + 2246.4146*m.b1817
                        + 3081.724*m.b1818 + 3284.469*m.b1819 + 4492.8292*m.b1820 + 6082.35*m.b1821 + 7493.4552*m.b1822
                        + 9983.1638*m.b1823 + 11507.8062*m.b1824 + 13729.8914*m.b1825 + 15530.267*m.b1826
                        + 19950.108*m.b1827 + 25918.9208*m.b1828 + 31717.4278*m.b1829 + 15239.6536*m.b1830
                        + 20906.384*m.b1831 + 22281.804*m.b1832 + 30479.3072*m.b1833 + 41262.6*m.b1834
                        + 50835.5232*m.b1835 + 67725.6808*m.b1836 + 78068.8392*m.b1837 + 93143.4424*m.b1838
                        + 105357.172*m.b1839 + 135341.328*m.b1840 + 175833.6928*m.b1841 + 215170.7048*m.b1842
                        + 13665.0471*m.b1843 + 18746.274*m.b1844 + 19979.5815*m.b1845 + 27330.0942*m.b1846
                        + 36999.225*m.b1847 + 45583.0452*m.b1848 + 60728.0613*m.b1849 + 70002.5337*m.b1850
                        + 83519.5839*m.b1851 + 94471.3545*m.b1852 + 121357.458*m.b1853 + 157666.0308*m.b1854
                        + 192938.6253*m.b1855 + 8749.7652*m.b1856 + 12003.288*m.b1857 + 12792.978*m.b1858
                        + 17499.5304*m.b1859 + 23690.7*m.b1860 + 29186.9424*m.b1861 + 38884.3356*m.b1862
                        + 44822.8044*m.b1863 + 53477.8068*m.b1864 + 60490.254*m.b1865 + 77705.496*m.b1866
                        + 100953.9696*m.b1867 + 123539.1036*m.b1868 + 7862.4511*m.b1869 + 10786.034*m.b1870
                        + 11495.6415*m.b1871 + 15724.9022*m.b1872 + 21288.225*m.b1873 + 26227.0932*m.b1874
                        + 34941.0733*m.b1875 + 40277.3217*m.b1876 + 48054.6199*m.b1877 + 54355.9345*m.b1878
                        + 69825.378*m.b1879 + 90716.2228*m.b1880 + 111010.9973*m.b1881 + 936.3431*m.b1882
                        + 1284.514*m.b1883 + 1369.0215*m.b1884 + 1872.6862*m.b1885 + 2535.225*m.b1886
                        + 3123.3972*m.b1887 + 4161.1493*m.b1888 + 4796.6457*m.b1889 + 5722.8479*m.b1890
                        + 6473.2745*m.b1891 + 8315.538*m.b1892 + 10803.4388*m.b1893 + 13220.3533*m.b1894
                        + 9957.4575*m.b1895 + 13660.05*m.b1896 + 14558.7375*m.b1897 + 19914.915*m.b1898
                        + 26960.625*m.b1899 + 33215.49*m.b1900 + 44251.3725*m.b1901 + 51009.5025*m.b1902
                        + 60859.1175*m.b1903 + 68839.4625*m.b1904 + 88430.85*m.b1905 + 114888.21*m.b1906
                        + 140590.6725*m.b1907 + 3885.7006*m.b1908 + 5330.564*m.b1909 + 5681.259*m.b1910
                        + 7771.4012*m.b1911 + 10520.85*m.b1912 + 12961.6872*m.b1913 + 17268.2218*m.b1914
                        + 19905.4482*m.b1915 + 23749.0654*m.b1916 + 26863.237*m.b1917 + 34508.388*m.b1918
                        + 44832.8488*m.b1919 + 54862.7258*m.b1920 + 5528.5876*m.b1921 + 7584.344*m.b1922
                        + 8083.314*m.b1923 + 11057.1752*m.b1924 + 14969.1*m.b1925 + 18441.9312*m.b1926
                        + 24569.2828*m.b1927 + 28321.5372*m.b1928 + 33790.2484*m.b1929 + 38221.102*m.b1930
                        + 49098.648*m.b1931 + 63788.3248*m.b1932 + 78058.8668*m.b1933 + 6249.5355*m.b1934
                        + 8573.37*m.b1935 + 9137.4075*m.b1936 + 12499.071*m.b1937 + 16921.125*m.b1938
                        + 20846.826*m.b1939 + 27773.2065*m.b1940 + 32014.7685*m.b1941 + 38196.6195*m.b1942
                        + 43205.2725*m.b1943 + 55501.29*m.b1944 + 72106.554*m.b1945 + 88238.0265*m.b1946
                        + 8786.0245*m.b1947 + 12053.03*m.b1948 + 12845.9925*m.b1949 + 17572.049*m.b1950
                        + 23788.875*m.b1951 + 29307.894*m.b1952 + 39045.4735*m.b1953 + 45008.5515*m.b1954
                        + 53699.4205*m.b1955 + 60740.9275*m.b1956 + 78027.51*m.b1957 + 101372.326*m.b1958
                        + 124051.0535*m.b1959 + 8348.0321*m.b1960 + 11452.174*m.b1961 + 12205.6065*m.b1962
                        + 16696.0642*m.b1963 + 22602.975*m.b1964 + 27846.8652*m.b1965 + 37099.0163*m.b1966
                        + 42764.8287*m.b1967 + 51022.4489*m.b1968 + 57712.9295*m.b1969 + 74137.758*m.b1970
                        + 96318.8108*m.b1971 + 117866.9803*m.b1972 + 10191.4117*m.b1973 + 13980.998*m.b1974
                        + 14900.8005*m.b1975 + 20382.8234*m.b1976 + 27594.075*m.b1977 + 33995.9004*m.b1978
                        + 45291.0751*m.b1979 + 52207.9899*m.b1980 + 62289.0253*m.b1981 + 70456.8715*m.b1982
                        + 90508.566*m.b1983 + 117587.5516*m.b1984 + 143893.9031*m.b1985 + 2827.2282*m.b1986
                        + 3878.508*m.b1987 + 4133.673*m.b1988 + 5654.4564*m.b1989 + 7654.95*m.b1990 + 9430.8984*m.b1991
                        + 12564.3246*m.b1992 + 14483.1654*m.b1993 + 17279.7738*m.b1994 + 19545.639*m.b1995
                        + 25108.236*m.b1996 + 32620.2936*m.b1997 + 39918.0126*m.b1998 + 5532.6318*m.b1999
                        + 7589.892*m.b2000 + 8089.227*m.b2001 + 11065.2636*m.b2002 + 14980.05*m.b2003
                        + 18455.4216*m.b2004 + 24587.2554*m.b2005 + 28342.2546*m.b2006 + 33814.9662*m.b2007
                        + 38249.061*m.b2008 + 49134.564*m.b2009 + 63834.9864*m.b2010 + 78115.9674*m.b2011
                        + 30324.021*m.b2012 + 41599.74*m.b2013 + 44336.565*m.b2014 + 60648.042*m.b2015
                        + 82104.75*m.b2016 + 101153.052*m.b2017 + 134761.263*m.b2018 + 155342.187*m.b2019
                        + 185337.789*m.b2020 + 209640.795*m.b2021 + 269303.58*m.b2022 + 349875.708*m.b2023
                        + 428148.903*m.b2024 + 4448.2599*m.b2025 + 6102.306*m.b2026 + 6503.7735*m.b2027
                        + 8896.5198*m.b2028 + 12044.025*m.b2029 + 14838.2388*m.b2030 + 19768.2597*m.b2031
                        + 22787.2953*m.b2032 + 27187.3791*m.b2033 + 30752.4105*m.b2034 + 39504.402*m.b2035
                        + 51323.6052*m.b2036 + 62805.5757*m.b2037 + 2285.0838*m.b2038 + 3134.772*m.b2039
                        + 3341.007*m.b2040 + 4570.1676*m.b2041 + 6187.05*m.b2042 + 7622.4456*m.b2043
                        + 10155.0114*m.b2044 + 11705.8986*m.b2045 + 13966.2342*m.b2046 + 15797.601*m.b2047
                        + 20293.524*m.b2048 + 26365.0824*m.b2049 + 32263.4034*m.b2050 + 7998.7628*m.b2051
                        + 10973.032*m.b2052 + 11694.942*m.b2053 + 15997.5256*m.b2054 + 21657.3*m.b2055
                        + 26681.7936*m.b2056 + 35546.8484*m.b2057 + 40975.6116*m.b2058 + 48887.7452*m.b2059
                        + 55298.306*m.b2060 + 71035.944*m.b2061 + 92288.9744*m.b2062 + 112935.6004*m.b2063
                        + 5003.7003*m.b2064 + 6864.282*m.b2065 + 7315.8795*m.b2066 + 10007.4006*m.b2067
                        + 13547.925*m.b2068 + 16691.0436*m.b2069 + 22236.6609*m.b2070 + 25632.6741*m.b2071
                        + 30582.1827*m.b2072 + 34592.3685*m.b2073 + 44437.194*m.b2074 + 57732.2244*m.b2075
                        + 70647.9129*m.b2076 + 5524.0448*m.b2077 + 7578.112*m.b2078 + 8076.672*m.b2079
                        + 11048.0896*m.b2080 + 14956.8*m.b2081 + 18426.7776*m.b2082 + 24549.0944*m.b2083
                        + 28298.2656*m.b2084 + 33762.4832*m.b2085 + 38189.696*m.b2086 + 49058.304*m.b2087
                        + 63735.9104*m.b2088 + 77994.7264*m.b2089 + 2928.3609*m.b2090 + 4017.246*m.b2091
                        + 4281.5385*m.b2092 + 5856.7218*m.b2093 + 7928.775*m.b2094 + 9768.2508*m.b2095
                        + 13013.7627*m.b2096 + 15001.2423*m.b2097 + 17897.8881*m.b2098 + 20244.8055*m.b2099
                        + 26006.382*m.b2100 + 33787.1532*m.b2101 + 41345.9187*m.b2102 + 3125.3079*m.b2103
                        + 4287.426*m.b2104 + 4569.4935*m.b2105 + 6250.6158*m.b2106 + 8462.025*m.b2107
                        + 10425.2148*m.b2108 + 13889.0037*m.b2109 + 16010.1513*m.b2110 + 19101.6111*m.b2111
                        + 21606.3705*m.b2112 + 27755.442*m.b2113 + 36059.5092*m.b2114 + 44126.6397*m.b2115
                        + 1951.6035*m.b2116 + 2677.29*m.b2117 + 2853.4275*m.b2118 + 3903.207*m.b2119 + 5284.125*m.b2120
                        + 6510.042*m.b2121 + 8673.0105*m.b2122 + 9997.5645*m.b2123 + 11928.0315*m.b2124
                        + 13492.1325*m.b2125 + 17331.93*m.b2126 + 22517.418*m.b2127 + 27554.9505*m.b2128
                        + 6711.5438*m.b2129 + 9207.172*m.b2130 + 9812.907*m.b2131 + 13423.0876*m.b2132
                        + 18172.05*m.b2133 + 22387.9656*m.b2134 + 29826.3914*m.b2135 + 34381.5186*m.b2136
                        + 41020.3742*m.b2137 + 46399.301*m.b2138 + 59604.324*m.b2139 + 77437.1624*m.b2140
                        + 94761.1834*m.b2141 + 998.8343*m.b2142 + 1370.242*m.b2143 + 1460.3895*m.b2144
                        + 1997.6686*m.b2145 + 2704.425*m.b2146 + 3331.8516*m.b2147 + 4438.8629*m.b2148
                        + 5116.7721*m.b2149 + 6104.7887*m.b2150 + 6905.2985*m.b2151 + 8870.514*m.b2152
                        + 11524.4564*m.b2153 + 14102.6749*m.b2154 + 6118.93*m.b2155 + 8394.2*m.b2156 + 8946.45*m.b2157
                        + 12237.86*m.b2158 + 16567.5*m.b2159 + 20411.16*m.b2160 + 27192.79*m.b2161 + 31345.71*m.b2162
                        + 37398.37*m.b2163 + 42302.35*m.b2164 + 54341.4*m.b2165 + 70599.64*m.b2166 + 86393.99*m.b2167
                        + 1244.2286*m.b2168 + 1706.884*m.b2169 + 1819.179*m.b2170 + 2488.4572*m.b2171 + 3368.85*m.b2172
                        + 4150.4232*m.b2173 + 5529.4058*m.b2174 + 6373.8642*m.b2175 + 7604.6174*m.b2176
                        + 8601.797*m.b2177 + 11049.828*m.b2178 + 14355.7928*m.b2179 + 17567.4298*m.b2180
                        + 1918.5297*m.b2181 + 2631.918*m.b2182 + 2805.0705*m.b2183 + 3837.0594*m.b2184
                        + 5194.575*m.b2185 + 6399.7164*m.b2186 + 8526.0291*m.b2187 + 9828.1359*m.b2188
                        + 11725.8873*m.b2189 + 13263.4815*m.b2190 + 17038.206*m.b2191 + 22135.8156*m.b2192
                        + 27087.9771*m.b2193 + 6450.0558*m.b2194 + 8848.452*m.b2195 + 9430.587*m.b2196
                        + 12900.1116*m.b2197 + 17464.05*m.b2198 + 21515.7096*m.b2199 + 28664.3274*m.b2200
                        + 33041.9826*m.b2201 + 39422.1822*m.b2202 + 44591.541*m.b2203 + 57282.084*m.b2204
                        + 74420.1384*m.b2205 + 91069.1994*m.b2206 + 10824.5783*m.b2207 + 14849.602*m.b2208
                        + 15826.5495*m.b2209 + 21649.1566*m.b2210 + 29308.425*m.b2211 + 36107.9796*m.b2212
                        + 48104.8949*m.b2213 + 55451.5401*m.b2214 + 66158.8847*m.b2215 + 74834.1785*m.b2216
                        + 96131.634*m.b2217 + 124892.9684*m.b2218 + 152833.6669*m.b2219 + 7765.5842*m.b2220
                        + 10653.148*m.b2221 + 11354.013*m.b2222 + 15531.1684*m.b2223 + 21025.95*m.b2224
                        + 25903.9704*m.b2225 + 34510.5926*m.b2226 + 39781.0974*m.b2227 + 47462.5778*m.b2228
                        + 53686.259*m.b2229 + 68965.116*m.b2230 + 89598.5816*m.b2231 + 109643.3206*m.b2232
                        + 3806.5063*m.b2233 + 5221.922*m.b2234 + 5565.4695*m.b2235 + 7613.0126*m.b2236
                        + 10306.425*m.b2237 + 12697.5156*m.b2238 + 16916.2789*m.b2239 + 19499.7561*m.b2240
                        + 23265.0367*m.b2241 + 26315.7385*m.b2242 + 33805.074*m.b2243 + 43919.1124*m.b2244
                        + 53744.5709*m.b2245 + 1383.3934*m.b2246 + 1897.796*m.b2247 + 2022.651*m.b2248
                        + 2766.7868*m.b2249 + 3745.65*m.b2250 + 4614.6408*m.b2251 + 6147.8602*m.b2252
                        + 7086.7698*m.b2253 + 8455.1806*m.b2254 + 9563.893*m.b2255 + 12285.732*m.b2256
                        + 15961.4632*m.b2257 + 19532.3162*m.b2258 + 5832.8721*m.b2259 + 8001.774*m.b2260
                        + 8528.2065*m.b2261 + 11665.7442*m.b2262 + 15792.975*m.b2263 + 19456.9452*m.b2264
                        + 25921.5363*m.b2265 + 29880.3087*m.b2266 + 35650.0089*m.b2267 + 40324.7295*m.b2268
                        + 51800.958*m.b2269 + 67299.1308*m.b2270 + 82355.1003*m.b2271 + 9169.8911*m.b2272
                        + 12579.634*m.b2273 + 13407.2415*m.b2274 + 18339.7822*m.b2275 + 24828.225*m.b2276
                        + 30588.3732*m.b2277 + 40751.3933*m.b2278 + 46975.0017*m.b2279 + 56045.5799*m.b2280
                        + 63394.7345*m.b2281 + 81436.578*m.b2282 + 105801.3428*m.b2283 + 129470.9173*m.b2284
                        + 4030.2392*m.b2285 + 5528.848*m.b2286 + 5892.588*m.b2287 + 8060.4784*m.b2288 + 10912.2*m.b2289
                        + 13443.8304*m.b2290 + 17910.5576*m.b2291 + 20645.8824*m.b2292 + 24632.4728*m.b2293
                        + 27862.484*m.b2294 + 35792.016*m.b2295 + 46500.5216*m.b2296 + 56903.4856*m.b2297
                        + 3085.1983*m.b2298 + 4232.402*m.b2299 + 4510.8495*m.b2300 + 6170.3966*m.b2301
                        + 8353.425*m.b2302 + 10291.4196*m.b2303 + 13710.7549*m.b2304 + 15804.6801*m.b2305
                        + 18856.4647*m.b2306 + 21329.0785*m.b2307 + 27399.234*m.b2308 + 35596.7284*m.b2309
                        + 43560.3269*m.b2310 + 9396.4494*m.b2311 + 12890.436*m.b2312 + 13738.491*m.b2313
                        + 18792.8988*m.b2314 + 25441.65*m.b2315 + 31344.1128*m.b2316 + 41758.2282*m.b2317
                        + 48135.6018*m.b2318 + 57430.2846*m.b2319 + 64961.013*m.b2320 + 83448.612*m.b2321
                        + 108415.3512*m.b2322 + 132669.7242*m.b2323 + 16219.5965*m.b2324 + 22250.71*m.b2325
                        + 23714.5725*m.b2326 + 32439.193*m.b2327 + 43915.875*m.b2328 + 54104.358*m.b2329
                        + 72080.5895*m.b2330 + 83088.8355*m.b2331 + 99132.7685*m.b2332 + 112131.8675*m.b2333
                        + 144044.07*m.b2334 + 187140.182*m.b2335 + 229006.6495*m.b2336 + 8097.8457*m.b2337
                        + 11108.958*m.b2338 + 11839.8105*m.b2339 + 16195.6914*m.b2340 + 21925.575*m.b2341
                        + 27012.3084*m.b2342 + 35987.1771*m.b2343 + 41483.1879*m.b2344 + 49493.3313*m.b2345
                        + 55983.3015*m.b2346 + 71915.886*m.b2347 + 93432.1836*m.b2348 + 114334.5651*m.b2349
                        + 5199.1238*m.b2350 + 7132.372*m.b2351 + 7601.607*m.b2352 + 10398.2476*m.b2353
                        + 14077.05*m.b2354 + 17342.9256*m.b2355 + 23105.1314*m.b2356 + 26633.7786*m.b2357
                        + 31776.5942*m.b2358 + 35943.401*m.b2359 + 46172.724*m.b2360 + 59987.0024*m.b2361
                        + 73407.1234*m.b2362 + 8149.0353*m.b2363 + 11179.182*m.b2364 + 11914.6545*m.b2365
                        + 16298.0706*m.b2366 + 22064.175*m.b2367 + 27183.0636*m.b2368 + 36214.6659*m.b2369
                        + 41745.4191*m.b2370 + 49806.1977*m.b2371 + 56337.1935*m.b2372 + 72370.494*m.b2373
                        + 94022.8044*m.b2374 + 115057.3179*m.b2375 + 17427.9259*m.b2376 + 23908.346*m.b2377
                        + 25481.2635*m.b2378 + 34855.8518*m.b2379 + 47187.525*m.b2380 + 58135.0308*m.b2381
                        + 77450.4577*m.b2382 + 89278.7973*m.b2383 + 106517.9731*m.b2384 + 120485.4805*m.b2385
                        + 154775.082*m.b2386 + 201081.7732*m.b2387 + 246067.2137*m.b2388 + 4372.9436*m.b2389
                        + 5998.984*m.b2390 + 6393.654*m.b2391 + 8745.8872*m.b2392 + 11840.1*m.b2393 + 14587.0032*m.b2394
                        + 19433.5508*m.b2395 + 22401.4692*m.b2396 + 26727.0524*m.b2397 + 30231.722*m.b2398
                        + 38835.528*m.b2399 + 50454.6128*m.b2400 + 61742.1748*m.b2401 + 3691.8283*m.b2402
                        + 5064.602*m.b2403 + 5397.7995*m.b2404 + 7383.6566*m.b2405 + 9995.925*m.b2406
                        + 12314.9796*m.b2407 + 16406.6449*m.b2408 + 18912.2901*m.b2409 + 22564.1347*m.b2410
                        + 25522.9285*m.b2411 + 32786.634*m.b2412 + 42595.9684*m.b2413 + 52125.4169*m.b2414
                        + 8715.0848*m.b2415 + 11955.712*m.b2416 + 12742.272*m.b2417 + 17430.1696*m.b2418
                        + 23596.8*m.b2419 + 29071.2576*m.b2420 + 38730.2144*m.b2421 + 44645.1456*m.b2422
                        + 53265.8432*m.b2423 + 60250.496*m.b2424 + 77397.504*m.b2425 + 100553.8304*m.b2426
                        + 123049.4464*m.b2427 + 9640.8742*m.b2428 + 13225.748*m.b2429 + 14095.863*m.b2430
                        + 19281.7484*m.b2431 + 26103.45*m.b2432 + 32159.4504*m.b2433 + 42844.4626*m.b2434
                        + 49387.7274*m.b2435 + 58924.1878*m.b2436 + 66650.809*m.b2437 + 85619.316*m.b2438
                        + 111235.5016*m.b2439 + 136120.7906*m.b2440 + 3715.124*m.b2441 + 5096.56*m.b2442
                        + 5431.86*m.b2443 + 7430.248*m.b2444 + 10059*m.b2445 + 12392.688*m.b2446 + 16510.172*m.b2447
                        + 19031.628*m.b2448 + 22706.516*m.b2449 + 25683.98*m.b2450 + 32993.52*m.b2451
                        + 42864.752*m.b2452 + 52454.332*m.b2453 + 8113.053*m.b2454 + 11129.82*m.b2455
                        + 11862.045*m.b2456 + 16226.106*m.b2457 + 21966.75*m.b2458 + 27063.036*m.b2459
                        + 36054.759*m.b2460 + 41561.091*m.b2461 + 49586.277*m.b2462 + 56088.435*m.b2463
                        + 72050.94*m.b2464 + 93607.644*m.b2465 + 114549.279*m.b2466 + 4353.886*m.b2467 + 5972.84*m.b2468
                        + 6365.79*m.b2469 + 8707.772*m.b2470 + 11788.5*m.b2471 + 14523.432*m.b2472 + 19348.858*m.b2473
                        + 22303.842*m.b2474 + 26610.574*m.b2475 + 30099.97*m.b2476 + 38666.28*m.b2477
                        + 50234.728*m.b2478 + 61473.098*m.b2479 + 2861.964*m.b2480 + 3926.16*m.b2481 + 4184.46*m.b2482
                        + 5723.928*m.b2483 + 7749*m.b2484 + 9546.768*m.b2485 + 12718.692*m.b2486 + 14661.108*m.b2487
                        + 17492.076*m.b2488 + 19785.78*m.b2489 + 25416.72*m.b2490 + 33021.072*m.b2491
                        + 40408.452*m.b2492 + 3344.9689*m.b2493 + 4588.766*m.b2494 + 4890.6585*m.b2495
                        + 6689.9378*m.b2496 + 9056.775*m.b2497 + 11157.9468*m.b2498 + 14865.1867*m.b2499
                        + 17135.4183*m.b2500 + 20444.1601*m.b2501 + 23124.9655*m.b2502 + 29706.222*m.b2503
                        + 38593.9372*m.b2504 + 47228.0627*m.b2505 + 4121.9262*m.b2506 + 5654.628*m.b2507
                        + 6026.643*m.b2508 + 8243.8524*m.b2509 + 11160.45*m.b2510 + 13749.6744*m.b2511
                        + 18318.0186*m.b2512 + 21115.5714*m.b2513 + 25192.8558*m.b2514 + 28496.349*m.b2515
                        + 36606.276*m.b2516 + 47558.3976*m.b2517 + 58198.0266*m.b2518 + 6846.332*m.b2519
                        + 9392.08*m.b2520 + 10009.98*m.b2521 + 13692.664*m.b2522 + 18537*m.b2523 + 22837.584*m.b2524
                        + 30425.396*m.b2525 + 35072.004*m.b2526 + 41844.188*m.b2527 + 47331.14*m.b2528
                        + 60801.36*m.b2529 + 78992.336*m.b2530 + 96664.276*m.b2531 + 1157.1952*m.b2532
                        + 1587.488*m.b2533 + 1691.928*m.b2534 + 2314.3904*m.b2535 + 3133.2*m.b2536 + 3860.1024*m.b2537
                        + 5142.6256*m.b2538 + 5928.0144*m.b2539 + 7072.6768*m.b2540 + 8000.104*m.b2541
                        + 10276.896*m.b2542 + 13351.6096*m.b2543 + 16338.5936*m.b2544 + 10191.7718*m.b2545
                        + 13981.492*m.b2546 + 14901.327*m.b2547 + 20383.5436*m.b2548 + 27595.05*m.b2549
                        + 33997.1016*m.b2550 + 45292.6754*m.b2551 + 52209.8346*m.b2552 + 62291.2262*m.b2553
                        + 70459.361*m.b2554 + 90511.764*m.b2555 + 117591.7064*m.b2556 + 143898.9874*m.b2557
                        + 2821.4943*m.b2558 + 3870.642*m.b2559 + 4125.2895*m.b2560 + 5642.9886*m.b2561
                        + 7639.425*m.b2562 + 9411.7716*m.b2563 + 12538.8429*m.b2564 + 14453.7921*m.b2565
                        + 17244.7287*m.b2566 + 19505.9985*m.b2567 + 25057.314*m.b2568 + 32554.1364*m.b2569
                        + 39837.0549*m.b2570 + 19383.352*m.b2571 + 26590.88*m.b2572 + 28340.28*m.b2573
                        + 38766.704*m.b2574 + 52482*m.b2575 + 64657.824*m.b2576 + 86140.456*m.b2577 + 99295.944*m.b2578
                        + 118469.368*m.b2579 + 134004.04*m.b2580 + 172140.96*m.b2581 + 223643.296*m.b2582
                        + 273676.136*m.b2583 + 10739.7332*m.b2584 + 14733.208*m.b2585 + 15702.498*m.b2586
                        + 21479.4664*m.b2587 + 29078.7*m.b2588 + 35824.9584*m.b2589 + 47727.8396*m.b2590
                        + 55016.9004*m.b2591 + 65640.3188*m.b2592 + 74247.614*m.b2593 + 95378.136*m.b2594
                        + 123914.0336*m.b2595 + 151635.7276*m.b2596 + 2204.6153*m.b2597 + 3024.382*m.b2598
                        + 3223.3545*m.b2599 + 4409.2306*m.b2600 + 5969.175*m.b2601 + 7354.0236*m.b2602
                        + 9797.4059*m.b2603 + 11293.6791*m.b2604 + 13474.4177*m.b2605 + 15241.2935*m.b2606
                        + 19578.894*m.b2607 + 25436.6444*m.b2608 + 31127.2579*m.b2609 + 473.1991*m.b2610
                        + 649.154*m.b2611 + 691.8615*m.b2612 + 946.3982*m.b2613 + 1281.225*m.b2614 + 1578.4692*m.b2615
                        + 2102.9173*m.b2616 + 2424.0777*m.b2617 + 2892.1519*m.b2618 + 3271.3945*m.b2619
                        + 4202.418*m.b2620 + 5459.7268*m.b2621 + 6681.1613*m.b2622 + 6424.3502*m.b2623
                        + 8813.188*m.b2624 + 9393.003*m.b2625 + 12848.7004*m.b2626 + 17394.45*m.b2627
                        + 21429.9624*m.b2628 + 28550.0906*m.b2629 + 32910.2994*m.b2630 + 39265.0718*m.b2631
                        + 44413.829*m.b2632 + 57053.796*m.b2633 + 74123.5496*m.b2634 + 90706.2586*m.b2635
                        + 7227.5671*m.b2636 + 9915.074*m.b2637 + 10567.3815*m.b2638 + 14455.1342*m.b2639
                        + 19569.225*m.b2640 + 24109.2852*m.b2641 + 32119.6213*m.b2642 + 37024.9737*m.b2643
                        + 44174.2639*m.b2644 + 49966.7545*m.b2645 + 64187.058*m.b2646 + 83390.9908*m.b2647
                        + 102046.9853*m.b2648 + 5978.2417*m.b2649 + 8201.198*m.b2650 + 8740.7505*m.b2651
                        + 11956.4834*m.b2652 + 16186.575*m.b2653 + 19941.8604*m.b2654 + 26567.5651*m.b2655
                        + 30624.9999*m.b2656 + 36538.4953*m.b2657 + 41329.7215*m.b2658 + 53091.966*m.b2659
                        + 68976.3916*m.b2660 + 84407.5931*m.b2661 + 6497.9491*m.b2662 + 8914.154*m.b2663
                        + 9500.6115*m.b2664 + 12995.8982*m.b2665 + 17593.725*m.b2666 + 21675.4692*m.b2667
                        + 28877.1673*m.b2668 + 33287.3277*m.b2669 + 39714.9019*m.b2670 + 44922.6445*m.b2671
                        + 57707.418*m.b2672 + 74972.7268*m.b2673 + 91745.4113*m.b2674 + 4543.2432*m.b2675
                        + 6232.608*m.b2676 + 6642.648*m.b2677 + 9086.4864*m.b2678 + 12301.2*m.b2679 + 15155.0784*m.b2680
                        + 20190.3696*m.b2681 + 23273.8704*m.b2682 + 27767.9088*m.b2683 + 31409.064*m.b2684
                        + 40347.936*m.b2685 + 52419.5136*m.b2686 + 64146.6576*m.b2687 + 4531.2768*m.b2688
                        + 6216.192*m.b2689 + 6625.152*m.b2690 + 9062.5536*m.b2691 + 12268.8*m.b2692 + 15115.1616*m.b2693
                        + 20137.1904*m.b2694 + 23212.5696*m.b2695 + 27694.7712*m.b2696 + 31326.336*m.b2697
                        + 40241.664*m.b2698 + 52281.4464*m.b2699 + 63977.7024*m.b2700 + 8144.9911*m.b2701
                        + 11173.634*m.b2702 + 11908.7415*m.b2703 + 16289.9822*m.b2704 + 22053.225*m.b2705
                        + 27169.5732*m.b2706 + 36196.6933*m.b2707 + 41724.7017*m.b2708 + 49781.4799*m.b2709
                        + 56309.2345*m.b2710 + 72334.578*m.b2711 + 93976.1428*m.b2712 + 115000.2173*m.b2713
                        + 3097.7741*m.b2714 + 4249.654*m.b2715 + 4529.2365*m.b2716 + 6195.5482*m.b2717
                        + 8387.475*m.b2718 + 10333.3692*m.b2719 + 13766.6423*m.b2720 + 15869.1027*m.b2721
                        + 18933.3269*m.b2722 + 21416.0195*m.b2723 + 27510.918*m.b2724 + 35741.8268*m.b2725
                        + 43737.8863*m.b2726 + 4810.4097*m.b2727 + 6599.118*m.b2728 + 7033.2705*m.b2729
                        + 9620.8194*m.b2730 + 13024.575*m.b2731 + 16046.2764*m.b2732 + 21377.6691*m.b2733
                        + 24642.4959*m.b2734 + 29400.8073*m.b2735 + 33256.0815*m.b2736 + 42720.606*m.b2737
                        + 55502.0556*m.b2738 + 67918.8171*m.b2739 + 2757.4242*m.b2740 + 3782.748*m.b2741
                        + 4031.613*m.b2742 + 5514.8484*m.b2743 + 7465.95*m.b2744 + 9198.0504*m.b2745
                        + 12254.1126*m.b2746 + 14125.5774*m.b2747 + 16853.1378*m.b2748 + 19063.059*m.b2749
                        + 24488.316*m.b2750 + 31814.9016*m.b2751 + 38932.4406*m.b2752 + 12684.7441*m.b2753
                        + 17401.454*m.b2754 + 18546.2865*m.b2755 + 25369.4882*m.b2756 + 34344.975*m.b2757
                        + 42313.0092*m.b2758 + 56371.5523*m.b2759 + 64980.6927*m.b2760 + 77528.0569*m.b2761
                        + 87694.1695*m.b2762 + 112651.518*m.b2763 + 146355.3868*m.b2764 + 179097.5963*m.b2765
                        + 8529.2455*m.b2766 + 11700.77*m.b2767 + 12470.5575*m.b2768 + 17058.491*m.b2769
                        + 23093.625*m.b2770 + 28451.346*m.b2771 + 37904.3365*m.b2772 + 43693.1385*m.b2773
                        + 52130.0095*m.b2774 + 58965.7225*m.b2775 + 75747.09*m.b2776 + 98409.634*m.b2777
                        + 120425.5565*m.b2778 + 1198.0527*m.b2779 + 1643.538*m.b2780 + 1751.6655*m.b2781
                        + 2396.1054*m.b2782 + 3243.825*m.b2783 + 3996.3924*m.b2784 + 5324.1981*m.b2785
                        + 6137.3169*m.b2786 + 7322.3943*m.b2787 + 8282.5665*m.b2788 + 10639.746*m.b2789
                        + 13823.0196*m.b2790 + 16915.4661*m.b2791 + 16839.9657*m.b2792 + 23101.758*m.b2793
                        + 24621.6105*m.b2794 + 33679.9314*m.b2795 + 45595.575*m.b2796 + 56173.7484*m.b2797
                        + 74837.5371*m.b2798 + 86266.8279*m.b2799 + 102924.4113*m.b2800 + 116420.7015*m.b2801
                        + 149553.486*m.b2802 + 194297.9436*m.b2803 + 237765.7251*m.b2804 + 6402.0517*m.b2805
                        + 8782.598*m.b2806 + 9360.4005*m.b2807 + 12804.1034*m.b2808 + 17334.075*m.b2809
                        + 21355.5804*m.b2810 + 28450.9951*m.b2811 + 32796.0699*m.b2812 + 39128.7853*m.b2813
                        + 44259.6715*m.b2814 + 56855.766*m.b2815 + 73866.2716*m.b2816 + 90391.4231*m.b2817
                        + 10381.129*m.b2818 + 14241.26*m.b2819 + 15178.185*m.b2820 + 20762.258*m.b2821
                        + 28107.75*m.b2822 + 34628.748*m.b2823 + 46134.187*m.b2824 + 53179.863*m.b2825
                        + 63448.561*m.b2826 + 71768.455*m.b2827 + 92193.42*m.b2828 + 119776.492*m.b2829
                        + 146572.547*m.b2830 + 17525.3468*m.b2831 + 24041.992*m.b2832 + 25623.702*m.b2833
                        + 35050.6936*m.b2834 + 47451.3*m.b2835 + 58460.0016*m.b2836 + 77883.4004*m.b2837
                        + 89777.8596*m.b2838 + 107113.4012*m.b2839 + 121158.986*m.b2840 + 155640.264*m.b2841
                        + 202205.8064*m.b2842 + 247442.7124*m.b2843 + 10579.9596*m.b2844 + 14514.024*m.b2845
                        + 15468.894*m.b2846 + 21159.9192*m.b2847 + 28646.1*m.b2848 + 35291.9952*m.b2849
                        + 47017.7988*m.b2850 + 54198.4212*m.b2851 + 64663.7964*m.b2852 + 73143.042*m.b2853
                        + 93959.208*m.b2854 + 122070.5808*m.b2855 + 149379.8628*m.b2856 + 8824.8599*m.b2857
                        + 12106.306*m.b2858 + 12902.7735*m.b2859 + 17649.7198*m.b2860 + 23894.025*m.b2861
                        + 29437.4388*m.b2862 + 39218.0597*m.b2863 + 45207.4953*m.b2864 + 53936.7791*m.b2865
                        + 61009.4105*m.b2866 + 78372.402*m.b2867 + 101820.4052*m.b2868 + 124599.3757*m.b2869
                        + 2424.8026*m.b2870 + 3326.444*m.b2871 + 3545.289*m.b2872 + 4849.6052*m.b2873 + 6565.35*m.b2874
                        + 8088.5112*m.b2875 + 10775.9278*m.b2876 + 12421.6422*m.b2877 + 14820.1834*m.b2878
                        + 16763.527*m.b2879 + 21534.348*m.b2880 + 27977.1448*m.b2881 + 34236.1118*m.b2882
                        + 2786.9524*m.b2883 + 3823.256*m.b2884 + 4074.786*m.b2885 + 5573.9048*m.b2886 + 7545.9*m.b2887
                        + 9296.5488*m.b2888 + 12385.3372*m.b2889 + 14276.8428*m.b2890 + 17033.6116*m.b2891
                        + 19267.198*m.b2892 + 24750.552*m.b2893 + 32155.5952*m.b2894 + 39349.3532*m.b2895
                        + 3228.9613*m.b2896 + 4429.622*m.b2897 + 4721.0445*m.b2898 + 6457.9226*m.b2899
                        + 8742.675*m.b2900 + 10770.9756*m.b2901 + 14349.6439*m.b2902 + 16541.1411*m.b2903
                        + 19735.1317*m.b2904 + 22322.9635*m.b2905 + 28675.974*m.b2906 + 37255.4524*m.b2907
                        + 45590.1359*m.b2908 + 5689.026*m.b2909 + 7804.44*m.b2910 + 8317.89*m.b2911 + 11378.052*m.b2912
                        + 15403.5*m.b2913 + 18977.112*m.b2914 + 25282.278*m.b2915 + 29143.422*m.b2916
                        + 34770.834*m.b2917 + 39330.27*m.b2918 + 50523.48*m.b2919 + 65639.448*m.b2920
                        + 80324.118*m.b2921 + 3077.3038*m.b2922 + 4221.572*m.b2923 + 4499.307*m.b2924
                        + 6154.6076*m.b2925 + 8332.05*m.b2926 + 10265.0856*m.b2927 + 13675.6714*m.b2928
                        + 15764.2386*m.b2929 + 18808.2142*m.b2930 + 21274.501*m.b2931 + 27329.124*m.b2932
                        + 35505.6424*m.b2933 + 43448.8634*m.b2934 + 1536.796*m.b2935 + 2108.24*m.b2936 + 2246.94*m.b2937
                        + 3073.592*m.b2938 + 4161*m.b2939 + 5126.352*m.b2940 + 6829.588*m.b2941 + 7872.612*m.b2942
                        + 9392.764*m.b2943 + 10624.42*m.b2944 + 13648.08*m.b2945 + 17731.408*m.b2946 + 21698.228*m.b2947
                        + 6097.0193*m.b2948 + 8364.142*m.b2949 + 8914.4145*m.b2950 + 12194.0386*m.b2951
                        + 16508.175*m.b2952 + 20338.0716*m.b2953 + 27095.4179*m.b2954 + 31233.4671*m.b2955
                        + 37264.4537*m.b2956 + 42150.8735*m.b2957 + 54146.814*m.b2958 + 70346.8364*m.b2959
                        + 86084.6299*m.b2960 + 5674.7882*m.b2961 + 7784.908*m.b2962 + 8297.073*m.b2963
                        + 11349.5764*m.b2964 + 15364.95*m.b2965 + 18929.6184*m.b2966 + 25219.0046*m.b2967
                        + 29070.4854*m.b2968 + 34683.8138*m.b2969 + 39231.839*m.b2970 + 50397.036*m.b2971
                        + 65475.1736*m.b2972 + 80123.0926*m.b2973 + 11732.9998*m.b2974 + 16095.812*m.b2975
                        + 17154.747*m.b2976 + 23465.9996*m.b2977 + 31768.05*m.b2978 + 39138.2376*m.b2979
                        + 52141.9594*m.b2980 + 60105.1506*m.b2981 + 71711.0782*m.b2982 + 81114.421*m.b2983
                        + 104199.204*m.b2984 + 135374.2504*m.b2985 + 165659.7914*m.b2986 + 10712.5872*m.b2987
                        + 14695.968*m.b2988 + 15662.808*m.b2989 + 21425.1744*m.b2990 + 29005.2*m.b2991
                        + 35734.4064*m.b2992 + 47607.2016*m.b2993 + 54877.8384*m.b2994 + 65474.4048*m.b2995
                        + 74059.944*m.b2996 + 95137.056*m.b2997 + 123600.8256*m.b2998 + 151252.4496*m.b2999
                        + 2949.8007*m.b3000 + 4046.658*m.b3001 + 4312.8855*m.b3002 + 5899.6014*m.b3003
                        + 7986.825*m.b3004 + 9839.7684*m.b3005 + 13109.0421*m.b3006 + 15111.0729*m.b3007
                        + 18028.9263*m.b3008 + 20393.0265*m.b3009 + 26196.786*m.b3010 + 34034.5236*m.b3011
                        + 41648.6301*m.b3012 + 2201.3467*m.b3013 + 3019.898*m.b3014 + 3218.5755*m.b3015
                        + 4402.6934*m.b3016 + 5960.325*m.b3017 + 7343.1204*m.b3018 + 9782.8801*m.b3019
                        + 11276.9349*m.b3020 + 13454.4403*m.b3021 + 15218.6965*m.b3022 + 19549.866*m.b3023
                        + 25398.9316*m.b3024 + 31081.1081*m.b3025 + 1966.2291*m.b3026 + 2697.354*m.b3027
                        + 2874.8115*m.b3028 + 3932.4582*m.b3029 + 5323.725*m.b3030 + 6558.8292*m.b3031
                        + 8738.0073*m.b3032 + 10072.4877*m.b3033 + 12017.4219*m.b3034 + 13593.2445*m.b3035
                        + 17461.818*m.b3036 + 22686.1668*m.b3037 + 27761.4513*m.b3038 + 8725.6385*m.b3039
                        + 11970.19*m.b3040 + 12757.7025*m.b3041 + 17451.277*m.b3042 + 23625.375*m.b3043
                        + 29106.462*m.b3044 + 38777.1155*m.b3045 + 44699.2095*m.b3046 + 53330.3465*m.b3047
                        + 60323.4575*m.b3048 + 77491.23*m.b3049 + 100675.598*m.b3050 + 123198.4555*m.b3051
                        + 3413.6372*m.b3052 + 4682.968*m.b3053 + 4991.058*m.b3054 + 6827.2744*m.b3055 + 9242.7*m.b3056
                        + 11387.0064*m.b3057 + 15170.3516*m.b3058 + 17487.1884*m.b3059 + 20863.8548*m.b3060
                        + 23599.694*m.b3061 + 30316.056*m.b3062 + 39386.2256*m.b3063 + 48197.5996*m.b3064
                        + 10598.6848*m.b3065 + 14539.712*m.b3066 + 15496.272*m.b3067 + 21197.3696*m.b3068
                        + 28696.8*m.b3069 + 35354.4576*m.b3070 + 47101.0144*m.b3071 + 54294.3456*m.b3072
                        + 64778.2432*m.b3073 + 73272.496*m.b3074 + 94125.504*m.b3075 + 122286.6304*m.b3076
                        + 149644.2464*m.b3077 + 5274.9941*m.b3078 + 7236.454*m.b3079 + 7712.5365*m.b3080
                        + 10549.9882*m.b3081 + 14282.475*m.b3082 + 17596.0092*m.b3083 + 23442.3023*m.b3084
                        + 27022.4427*m.b3085 + 32240.3069*m.b3086 + 36467.9195*m.b3087 + 46846.518*m.b3088
                        + 60862.3868*m.b3089 + 74478.3463*m.b3090 + 3139.2964*m.b3091 + 4306.616*m.b3092
                        + 4589.946*m.b3093 + 6278.5928*m.b3094 + 8499.9*m.b3095 + 10471.8768*m.b3096
                        + 13951.1692*m.b3097 + 16081.8108*m.b3098 + 19187.1076*m.b3099 + 21703.078*m.b3100
                        + 27879.672*m.b3101 + 36220.9072*m.b3102 + 44324.1452*m.b3103 + 12292.9553*m.b3104
                        + 16863.982*m.b3105 + 17973.4545*m.b3106 + 24585.9106*m.b3107 + 33284.175*m.b3108
                        + 41006.1036*m.b3109 + 54630.4259*m.b3110 + 62973.6591*m.b3111 + 75133.4777*m.b3112
                        + 84985.5935*m.b3113 + 109172.094*m.b3114 + 141834.9644*m.b3115 + 173565.8779*m.b3116
                        + 7822.6739*m.b3117 + 10731.466*m.b3118 + 11437.4835*m.b3119 + 15645.3478*m.b3120
                        + 21180.525*m.b3121 + 26094.4068*m.b3122 + 34764.3017*m.b3123 + 40073.5533*m.b3124
                        + 47811.5051*m.b3125 + 54080.9405*m.b3126 + 69472.122*m.b3127 + 90257.2772*m.b3128
                        + 110449.3777*m.b3129 + 9880.8116*m.b3130 + 13554.904*m.b3131 + 14446.674*m.b3132
                        + 19761.6232*m.b3133 + 26753.1*m.b3134 + 32959.8192*m.b3135 + 43910.7548*m.b3136
                        + 50616.8652*m.b3137 + 60390.6644*m.b3138 + 68309.582*m.b3139 + 87750.168*m.b3140
                        + 114003.8768*m.b3141 + 139508.4988*m.b3142 + 5679.8573*m.b3143 + 7791.862*m.b3144
                        + 8304.4845*m.b3145 + 11359.7146*m.b3146 + 15378.675*m.b3147 + 18946.5276*m.b3148
                        + 25241.5319*m.b3149 + 29096.4531*m.b3150 + 34714.7957*m.b3151 + 39266.8835*m.b3152
                        + 50442.054*m.b3153 + 65533.6604*m.b3154 + 80194.6639*m.b3155 + 25110.5486*m.b3156
                        + 34447.684*m.b3157 + 36713.979*m.b3158 + 50221.0972*m.b3159 + 67988.85*m.b3160
                        + 83762.2632*m.b3161 + 111592.3658*m.b3162 + 128634.9042*m.b3163 + 153473.4974*m.b3164
                        + 173598.197*m.b3165 + 223003.428*m.b3166 + 289723.1528*m.b3167 + 354539.1898*m.b3168
                        + 3022.3747*m.b3169 + 4146.218*m.b3170 + 4418.9955*m.b3171 + 6044.7494*m.b3172
                        + 8183.325*m.b3173 + 10081.8564*m.b3174 + 13431.5641*m.b3175 + 15482.8509*m.b3176
                        + 18472.4923*m.b3177 + 20894.7565*m.b3178 + 26841.306*m.b3179 + 34871.8756*m.b3180
                        + 42673.3121*m.b3181 + 4895.3656*m.b3182 + 6715.664*m.b3183 + 7157.484*m.b3184
                        + 9790.7312*m.b3185 + 13254.6*m.b3186 + 16329.6672*m.b3187 + 21755.2168*m.b3188
                        + 25077.7032*m.b3189 + 29920.0504*m.b3190 + 33843.412*m.b3191 + 43475.088*m.b3192
                        + 56482.2688*m.b3193 + 69118.3208*m.b3194 + 3165.8053*m.b3195 + 4342.982*m.b3196
                        + 4628.7045*m.b3197 + 6331.6106*m.b3198 + 8571.675*m.b3199 + 10560.3036*m.b3200
                        + 14068.9759*m.b3201 + 16217.6091*m.b3202 + 19349.1277*m.b3203 + 21886.3435*m.b3204
                        + 28115.094*m.b3205 + 36526.7644*m.b3206 + 44698.4279*m.b3207 + 6228.899*m.b3208
                        + 8545.06*m.b3209 + 9107.235*m.b3210 + 12457.798*m.b3211 + 16865.25*m.b3212 + 20777.988*m.b3213
                        + 27681.497*m.b3214 + 31909.053*m.b3215 + 38070.491*m.b3216 + 43062.605*m.b3217
                        + 55318.02*m.b3218 + 71868.452*m.b3219 + 87946.657*m.b3220 + 4856.7518*m.b3221
                        + 6662.692*m.b3222 + 7101.027*m.b3223 + 9713.5036*m.b3224 + 13150.05*m.b3225
                        + 16200.8616*m.b3226 + 21583.6154*m.b3227 + 24879.8946*m.b3228 + 29684.0462*m.b3229
                        + 33576.461*m.b3230 + 43132.164*m.b3231 + 56036.7464*m.b3232 + 68573.1274*m.b3233
                        + 8029.5652*m.b3234 + 11015.288*m.b3235 + 11739.978*m.b3236 + 16059.1304*m.b3237
                        + 21740.7*m.b3238 + 26784.5424*m.b3239 + 35683.7356*m.b3240 + 41133.4044*m.b3241
                        + 49076.0068*m.b3242 + 55511.254*m.b3243 + 71309.496*m.b3244 + 92644.3696*m.b3245
                        + 113370.5036*m.b3246 + 7087.0173*m.b3247 + 9722.262*m.b3248 + 10361.8845*m.b3249
                        + 14174.0346*m.b3250 + 19188.675*m.b3251 + 23640.4476*m.b3252 + 31495.0119*m.b3253
                        + 36304.9731*m.b3254 + 43315.2357*m.b3255 + 48995.0835*m.b3256 + 62938.854*m.b3257
                        + 81769.3404*m.b3258 + 100062.5439*m.b3259 + 3753.3223*m.b3260 + 5148.962*m.b3261
                        + 5487.7095*m.b3262 + 7506.6446*m.b3263 + 10162.425*m.b3264 + 12520.1076*m.b3265
                        + 16679.9269*m.b3266 + 19227.3081*m.b3267 + 22939.9807*m.b3268 + 25948.0585*m.b3269
                        + 33332.754*m.b3270 + 43305.4804*m.b3271 + 52993.6589*m.b3272 + 7471.4933*m.b3273
                        + 10249.702*m.b3274 + 10924.0245*m.b3275 + 14942.9866*m.b3276 + 20229.675*m.b3277
                        + 24922.9596*m.b3278 + 33203.6399*m.b3279 + 38274.5451*m.b3280 + 45665.1197*m.b3281
                        + 51653.1035*m.b3282 + 66353.334*m.b3283 + 86205.3884*m.b3284 + 105491.0119*m.b3285
                        + 6188.5678*m.b3286 + 8489.732*m.b3287 + 9048.267*m.b3288 + 12377.1356*m.b3289
                        + 16756.05*m.b3290 + 20643.4536*m.b3291 + 27502.2634*m.b3292 + 31702.4466*m.b3293
                        + 37823.9902*m.b3294 + 42783.781*m.b3295 + 54959.844*m.b3296 + 71403.1144*m.b3297
                        + 87377.2154*m.b3298 + 1302.8418*m.b3299 + 1787.292*m.b3300 + 1904.877*m.b3301
                        + 2605.6836*m.b3302 + 3527.55*m.b3303 + 4345.9416*m.b3304 + 5789.8854*m.b3305
                        + 6674.1246*m.b3306 + 7962.8562*m.b3307 + 9007.011*m.b3308 + 11570.364*m.b3309
                        + 15032.0664*m.b3310 + 18394.9974*m.b3311 + 1271.9009*m.b3312 + 1744.846*m.b3313
                        + 1859.6385*m.b3314 + 2543.8018*m.b3315 + 3443.775*m.b3316 + 4242.7308*m.b3317
                        + 5652.3827*m.b3318 + 6515.6223*m.b3319 + 7773.7481*m.b3320 + 8793.1055*m.b3321
                        + 11295.582*m.b3322 + 14675.0732*m.b3323 + 17958.1387*m.b3324 + 21679.959*m.b3325
                        + 29741.46*m.b3326 + 31698.135*m.b3327 + 43359.918*m.b3328 + 58700.25*m.b3329
                        + 72318.708*m.b3330 + 96346.677*m.b3331 + 111060.873*m.b3332 + 132506.031*m.b3333
                        + 149881.305*m.b3334 + 192536.82*m.b3335 + 250141.332*m.b3336 + 306102.237*m.b3337
                        + 24655.4376*m.b3338 + 33823.344*m.b3339 + 36048.564*m.b3340 + 49310.8752*m.b3341
                        + 66756.6*m.b3342 + 82244.1312*m.b3343 + 109569.8328*m.b3344 + 126303.4872*m.b3345
                        + 150691.8984*m.b3346 + 170451.852*m.b3347 + 218961.648*m.b3348 + 284472.1248*m.b3349
                        + 348113.4168*m.b3350 + 935.9553*m.b3351 + 1283.982*m.b3352 + 1368.4545*m.b3353
                        + 1871.9106*m.b3354 + 2534.175*m.b3355 + 3122.1036*m.b3356 + 4159.4259*m.b3357
                        + 4794.6591*m.b3358 + 5720.4777*m.b3359 + 6470.5935*m.b3360 + 8312.094*m.b3361
                        + 10798.9644*m.b3362 + 13214.8779*m.b3363 + 1109.7174*m.b3364 + 1522.356*m.b3365
                        + 1622.511*m.b3366 + 2219.4348*m.b3367 + 3004.65*m.b3368 + 3701.7288*m.b3369 + 4931.6322*m.b3370
                        + 5684.7978*m.b3371 + 6782.4966*m.b3372 + 7671.873*m.b3373 + 9855.252*m.b3374
                        + 12803.8152*m.b3375 + 15668.2482*m.b3376 + 166.9756*m.b3377 + 229.064*m.b3378 + 244.134*m.b3379
                        + 333.9512*m.b3380 + 452.1*m.b3381 + 556.9872*m.b3382 + 742.0468*m.b3383 + 855.3732*m.b3384
                        + 1020.5404*m.b3385 + 1154.362*m.b3386 + 1482.888*m.b3387 + 1926.5488*m.b3388
                        + 2357.5508*m.b3389 + 2705.1266*m.b3390 + 3711.004*m.b3391 + 3955.149*m.b3392
                        + 5410.2532*m.b3393 + 7324.35*m.b3394 + 9023.5992*m.b3395 + 12021.6998*m.b3396
                        + 13857.6702*m.b3397 + 16533.4994*m.b3398 + 18701.507*m.b3399 + 24023.868*m.b3400
                        + 31211.4968*m.b3401 + 38194.0438*m.b3402 + 8924.8015*m.b3403 + 12243.41*m.b3404
                        + 13048.8975*m.b3405 + 17849.603*m.b3406 + 24164.625*m.b3407 + 29770.818*m.b3408
                        + 39662.2045*m.b3409 + 45719.4705*m.b3410 + 54547.6135*m.b3411 + 61700.3425*m.b3412
                        + 79259.97*m.b3413 + 102973.522*m.b3414 + 126010.4645*m.b3415 + 5412.4415*m.b3416
                        + 7425.01*m.b3417 + 7913.4975*m.b3418 + 10824.883*m.b3419 + 14654.625*m.b3420
                        + 18054.498*m.b3421 + 24053.1245*m.b3422 + 27726.5505*m.b3423 + 33080.3735*m.b3424
                        + 37418.1425*m.b3425 + 48067.17*m.b3426 + 62448.242*m.b3427 + 76418.9845*m.b3428
                        + 4850.8517*m.b3429 + 6654.598*m.b3430 + 7092.4005*m.b3431 + 9701.7034*m.b3432
                        + 13134.075*m.b3433 + 16181.1804*m.b3434 + 21557.3951*m.b3435 + 24849.6699*m.b3436
                        + 29647.9853*m.b3437 + 33535.6715*m.b3438 + 43079.766*m.b3439 + 55968.6716*m.b3440
                        + 68489.8231*m.b3441 + 3663.5189*m.b3442 + 5025.766*m.b3443 + 5356.4085*m.b3444
                        + 7327.0378*m.b3445 + 9919.275*m.b3446 + 12220.5468*m.b3447 + 16280.8367*m.b3448
                        + 18767.2683*m.b3449 + 22391.1101*m.b3450 + 25327.2155*m.b3451 + 32535.222*m.b3452
                        + 42269.3372*m.b3453 + 51725.7127*m.b3454 + 19900.9265*m.b3455 + 27300.91*m.b3456
                        + 29097.0225*m.b3457 + 39801.853*m.b3458 + 53883.375*m.b3459 + 66384.318*m.b3460
                        + 88440.5795*m.b3461 + 101947.3455*m.b3462 + 121632.7385*m.b3463 + 137582.2175*m.b3464
                        + 176737.47*m.b3465 + 229615.022*m.b3466 + 280983.8395*m.b3467 + 664.9108*m.b3468
                        + 912.152*m.b3469 + 972.162*m.b3470 + 1329.8216*m.b3471 + 1800.3*m.b3472 + 2217.9696*m.b3473
                        + 2954.8924*m.b3474 + 3406.1676*m.b3475 + 4063.8772*m.b3476 + 4596.766*m.b3477
                        + 5904.984*m.b3478 + 7671.6784*m.b3479 + 9387.9644*m.b3480 + 13975.2871*m.b3481
                        + 19171.874*m.b3482 + 20433.1815*m.b3483 + 27950.5742*m.b3484 + 37839.225*m.b3485
                        + 46617.9252*m.b3486 + 62106.7813*m.b3487 + 71591.8137*m.b3488 + 85415.7439*m.b3489
                        + 96616.1545*m.b3490 + 124112.658*m.b3491 + 161245.5508*m.b3492 + 197318.9453*m.b3493
                        + 3472.472*m.b3494 + 4763.68*m.b3495 + 5077.08*m.b3496 + 6944.944*m.b3497 + 9402*m.b3498
                        + 11583.264*m.b3499 + 15431.816*m.b3500 + 17788.584*m.b3501 + 21223.448*m.b3502
                        + 24006.44*m.b3503 + 30838.56*m.b3504 + 40065.056*m.b3505 + 49028.296*m.b3506
                        + 12411.0958*m.b3507 + 17026.052*m.b3508 + 18146.187*m.b3509 + 24822.1916*m.b3510
                        + 33604.05*m.b3511 + 41400.1896*m.b3512 + 55155.4474*m.b3513 + 63578.8626*m.b3514
                        + 75855.5422*m.b3515 + 85802.341*m.b3516 + 110221.284*m.b3517 + 143198.0584*m.b3518
                        + 175233.9194*m.b3519 + 5465.3208*m.b3520 + 7497.552*m.b3521 + 7990.812*m.b3522
                        + 10930.6416*m.b3523 + 14797.8*m.b3524 + 18230.8896*m.b3525 + 24288.1224*m.b3526
                        + 27997.4376*m.b3527 + 33403.5672*m.b3528 + 37783.716*m.b3529 + 48536.784*m.b3530
                        + 63058.3584*m.b3531 + 77165.5944*m.b3532 + 6536.646*m.b3533 + 8967.24*m.b3534 + 9557.19*m.b3535
                        + 13073.292*m.b3536 + 17698.5*m.b3537 + 21804.552*m.b3538 + 29049.138*m.b3539
                        + 33485.562*m.b3540 + 39951.414*m.b3541 + 45190.17*m.b3542 + 58051.08*m.b3543
                        + 75419.208*m.b3544 + 92291.778*m.b3545 + 9887.3488*m.b3546 + 13563.872*m.b3547
                        + 14456.232*m.b3548 + 19774.6976*m.b3549 + 26770.8*m.b3550 + 32981.6256*m.b3551
                        + 43939.8064*m.b3552 + 50650.3536*m.b3553 + 60430.6192*m.b3554 + 68354.776*m.b3555
                        + 87808.224*m.b3556 + 114079.3024*m.b3557 + 139600.7984*m.b3558 + 7258.4803*m.b3559
                        + 9957.482*m.b3560 + 10612.5795*m.b3561 + 14516.9606*m.b3562 + 19652.925*m.b3563
                        + 24212.4036*m.b3564 + 32257.0009*m.b3565 + 37183.3341*m.b3566 + 44363.2027*m.b3567
                        + 50180.4685*m.b3568 + 64461.594*m.b3569 + 83747.6644*m.b3570 + 102483.4529*m.b3571
                        + 4226.2444*m.b3572 + 5797.736*m.b3573 + 6179.166*m.b3574 + 8452.4888*m.b3575 + 11442.9*m.b3576
                        + 14097.6528*m.b3577 + 18781.6132*m.b3578 + 21649.9668*m.b3579 + 25830.4396*m.b3580
                        + 29217.538*m.b3581 + 37532.712*m.b3582 + 48762.0112*m.b3583 + 59670.9092*m.b3584
                        + 4302.9734*m.b3585 + 5902.996*m.b3586 + 6291.351*m.b3587 + 8605.9468*m.b3588 + 11650.65*m.b3589
                        + 14353.6008*m.b3590 + 19122.6002*m.b3591 + 22043.0298*m.b3592 + 26299.4006*m.b3593
                        + 29747.993*m.b3594 + 38214.132*m.b3595 + 49647.3032*m.b3596 + 60754.2562*m.b3597
                        + 1930.2191*m.b3598 + 2647.954*m.b3599 + 2822.1615*m.b3600 + 3860.4382*m.b3601
                        + 5226.225*m.b3602 + 6438.7092*m.b3603 + 8577.9773*m.b3604 + 9888.0177*m.b3605
                        + 11797.3319*m.b3606 + 13344.2945*m.b3607 + 17142.018*m.b3608 + 22270.6868*m.b3609
                        + 27253.0213*m.b3610 + 5767.6386*m.b3611 + 7912.284*m.b3612 + 8432.829*m.b3613
                        + 11535.2772*m.b3614 + 15616.35*m.b3615 + 19239.3432*m.b3616 + 25631.6358*m.b3617
                        + 29546.1342*m.b3618 + 35251.3074*m.b3619 + 39873.747*m.b3620 + 51221.628*m.b3621
                        + 66546.4728*m.b3622 + 81434.0598*m.b3623 + 1530.2311*m.b3624 + 2099.234*m.b3625
                        + 2237.3415*m.b3626 + 3060.4622*m.b3627 + 4143.225*m.b3628 + 5104.4532*m.b3629
                        + 6800.4133*m.b3630 + 7838.9817*m.b3631 + 9352.6399*m.b3632 + 10579.0345*m.b3633
                        + 13589.778*m.b3634 + 17655.6628*m.b3635 + 21605.5373*m.b3636 + 4017.5249*m.b3637
                        + 5511.406*m.b3638 + 5873.9985*m.b3639 + 8035.0498*m.b3640 + 10877.775*m.b3641
                        + 13401.4188*m.b3642 + 17854.0547*m.b3643 + 20580.7503*m.b3644 + 24554.7641*m.b3645
                        + 27774.5855*m.b3646 + 35679.102*m.b3647 + 46353.8252*m.b3648 + 56723.9707*m.b3649
                        + 5100.8996*m.b3650 + 6997.624*m.b3651 + 7457.994*m.b3652 + 10201.7992*m.b3653 + 13811.1*m.b3654
                        + 17015.2752*m.b3655 + 22668.6188*m.b3656 + 26130.6012*m.b3657 + 31176.2564*m.b3658
                        + 35264.342*m.b3659 + 45300.408*m.b3660 + 58853.7008*m.b3661 + 72020.2828*m.b3662
                        + 6598.6386*m.b3663 + 9052.284*m.b3664 + 9647.829*m.b3665 + 13197.2772*m.b3666
                        + 17866.35*m.b3667 + 22011.3432*m.b3668 + 29324.6358*m.b3669 + 33803.1342*m.b3670
                        + 40330.3074*m.b3671 + 45618.747*m.b3672 + 58601.628*m.b3673 + 76134.4728*m.b3674
                        + 93167.0598*m.b3675 + 2788.9468*m.b3676 + 3825.992*m.b3677 + 4077.702*m.b3678
                        + 5577.8936*m.b3679 + 7551.3*m.b3680 + 9303.2016*m.b3681 + 12394.2004*m.b3682
                        + 14287.0596*m.b3683 + 17045.8012*m.b3684 + 19280.986*m.b3685 + 24768.264*m.b3686
                        + 32178.6064*m.b3687 + 39377.5124*m.b3688 + 8976.7667*m.b3689 + 12314.698*m.b3690
                        + 13124.8755*m.b3691 + 17953.5334*m.b3692 + 24305.325*m.b3693 + 29944.1604*m.b3694
                        + 39893.1401*m.b3695 + 45985.6749*m.b3696 + 54865.2203*m.b3697 + 62059.5965*m.b3698
                        + 79721.466*m.b3699 + 103573.0916*m.b3700 + 126744.1681*m.b3701 + 1312.6753*m.b3702
                        + 1800.782*m.b3703 + 1919.2545*m.b3704 + 2625.3506*m.b3705 + 3554.175*m.b3706
                        + 4378.7436*m.b3707 + 5833.5859*m.b3708 + 6724.4991*m.b3709 + 8022.9577*m.b3710
                        + 9074.9935*m.b3711 + 11657.694*m.b3712 + 15145.5244*m.b3713 + 18533.8379*m.b3714
                        + 5929.5728*m.b3715 + 8134.432*m.b3716 + 8669.592*m.b3717 + 11859.1456*m.b3718 + 16054.8*m.b3719
                        + 19779.5136*m.b3720 + 26351.2784*m.b3721 + 30375.6816*m.b3722 + 36241.0352*m.b3723
                        + 40993.256*m.b3724 + 52659.744*m.b3725 + 68414.8544*m.b3726 + 83720.4304*m.b3727
                        + 2372.3665*m.b3728 + 3254.51*m.b3729 + 3468.6225*m.b3730 + 4744.733*m.b3731 + 6423.375*m.b3732
                        + 7913.598*m.b3733 + 10542.8995*m.b3734 + 12153.0255*m.b3735 + 14499.6985*m.b3736
                        + 16401.0175*m.b3737 + 21068.67*m.b3738 + 27372.142*m.b3739 + 33495.7595*m.b3740
                        + 2383.0033*m.b3741 + 3269.102*m.b3742 + 3484.1745*m.b3743 + 4766.0066*m.b3744
                        + 6452.175*m.b3745 + 7949.0796*m.b3746 + 10590.1699*m.b3747 + 12207.5151*m.b3748
                        + 14564.7097*m.b3749 + 16474.5535*m.b3750 + 21163.134*m.b3751 + 27494.8684*m.b3752
                        + 33645.9419*m.b3753 + 3082.9823*m.b3754 + 4229.362*m.b3755 + 4507.6095*m.b3756
                        + 6165.9646*m.b3757 + 8347.425*m.b3758 + 10284.0276*m.b3759 + 13700.9069*m.b3760
                        + 15793.3281*m.b3761 + 18842.9207*m.b3762 + 21313.7585*m.b3763 + 27379.554*m.b3764
                        + 35571.1604*m.b3765 + 43529.0389*m.b3766 + 5436.7067*m.b3767 + 7458.298*m.b3768
                        + 7948.9755*m.b3769 + 10873.4134*m.b3770 + 14720.325*m.b3771 + 18135.4404*m.b3772
                        + 24160.9601*m.b3773 + 27850.8549*m.b3774 + 33228.6803*m.b3775 + 37585.8965*m.b3776
                        + 48282.666*m.b3777 + 62728.2116*m.b3778 + 76761.5881*m.b3779 + 5497.2866*m.b3780
                        + 7541.404*m.b3781 + 8037.549*m.b3782 + 10994.5732*m.b3783 + 14884.35*m.b3784
                        + 18337.5192*m.b3785 + 24430.1798*m.b3786 + 28161.1902*m.b3787 + 33598.9394*m.b3788
                        + 38004.707*m.b3789 + 48820.668*m.b3790 + 63427.1768*m.b3791 + 77616.9238*m.b3792
                        + 3417.2936*m.b3793 + 4687.984*m.b3794 + 4996.404*m.b3795 + 6834.5872*m.b3796 + 9252.6*m.b3797
                        + 11399.2032*m.b3798 + 15186.6008*m.b3799 + 17505.9192*m.b3800 + 20886.2024*m.b3801
                        + 23624.972*m.b3802 + 30348.528*m.b3803 + 39428.4128*m.b3804 + 48249.2248*m.b3805
                        + 4566.1234*m.b3806 + 6263.996*m.b3807 + 6676.101*m.b3808 + 9132.2468*m.b3809 + 12363.15*m.b3810
                        + 15231.4008*m.b3811 + 20292.0502*m.b3812 + 23391.0798*m.b3813 + 27907.7506*m.b3814
                        + 31567.243*m.b3815 + 40551.132*m.b3816 + 52683.5032*m.b3817 + 64469.7062*m.b3818
                        + 1315.3899*m.b3819 + 1804.506*m.b3820 + 1923.2235*m.b3821 + 2630.7798*m.b3822
                        + 3561.525*m.b3823 + 4387.7988*m.b3824 + 5845.6497*m.b3825 + 6738.4053*m.b3826
                        + 8039.5491*m.b3827 + 9093.7605*m.b3828 + 11681.802*m.b3829 + 15176.8452*m.b3830
                        + 18572.1657*m.b3831 + 5201.6445*m.b3832 + 7135.83*m.b3833 + 7605.2925*m.b3834
                        + 10403.289*m.b3835 + 14083.875*m.b3836 + 17351.334*m.b3837 + 23116.3335*m.b3838
                        + 26646.6915*m.b3839 + 31792.0005*m.b3840 + 35960.8275*m.b3841 + 46195.11*m.b3842
                        + 60016.086*m.b3843 + 73442.7135*m.b3844 + 6780.9323*m.b3845 + 9302.362*m.b3846
                        + 9914.3595*m.b3847 + 13561.8646*m.b3848 + 18359.925*m.b3849 + 22619.4276*m.b3850
                        + 30134.7569*m.b3851 + 34736.9781*m.b3852 + 41444.4707*m.b3853 + 46879.0085*m.b3854
                        + 60220.554*m.b3855 + 78237.7604*m.b3856 + 95740.8889*m.b3857 + 10624.335*m.b3858
                        + 14574.9*m.b3859 + 15533.775*m.b3860 + 21248.67*m.b3861 + 28766.25*m.b3862 + 35440.02*m.b3863
                        + 47215.005*m.b3864 + 54425.745*m.b3865 + 64935.015*m.b3866 + 73449.825*m.b3867
                        + 94353.3*m.b3868 + 122582.58*m.b3869 + 150006.405*m.b3870 + 2668.0917*m.b3871
                        + 3660.198*m.b3872 + 3901.0005*m.b3873 + 5336.1834*m.b3874 + 7224.075*m.b3875
                        + 8900.0604*m.b3876 + 11857.1151*m.b3877 + 13667.9499*m.b3878 + 16307.1453*m.b3879
                        + 18445.4715*m.b3880 + 23694.966*m.b3881 + 30784.1916*m.b3882 + 37671.1431*m.b3883
                        + 2156.1403*m.b3884 + 2957.882*m.b3885 + 3152.4795*m.b3886 + 4312.2806*m.b3887
                        + 5837.925*m.b3888 + 7192.3236*m.b3889 + 9581.9809*m.b3890 + 11045.3541*m.b3891
                        + 13178.1427*m.b3892 + 14906.1685*m.b3893 + 19148.394*m.b3894 + 24877.3444*m.b3895
                        + 30442.8329*m.b3896 + 4589.1975*m.b3897 + 6295.65*m.b3898 + 6709.8375*m.b3899
                        + 9178.395*m.b3900 + 12425.625*m.b3901 + 15308.37*m.b3902 + 20394.5925*m.b3903
                        + 23509.2825*m.b3904 + 28048.7775*m.b3905 + 31726.7625*m.b3906 + 40756.05*m.b3907
                        + 52949.73*m.b3908 + 64795.4925*m.b3909 + 5342.3328*m.b3910 + 7328.832*m.b3911
                        + 7810.992*m.b3912 + 10684.6656*m.b3913 + 14464.8*m.b3914 + 17820.6336*m.b3915
                        + 23741.5584*m.b3916 + 27367.4016*m.b3917 + 32651.8752*m.b3918 + 36933.456*m.b3919
                        + 47444.544*m.b3920 + 61639.3344*m.b3921 + 75429.1104*m.b3922 + 1585.3264*m.b3923
                        + 2174.816*m.b3924 + 2317.896*m.b3925 + 3170.6528*m.b3926 + 4292.4*m.b3927 + 5288.2368*m.b3928
                        + 7045.2592*m.b3929 + 8121.2208*m.b3930 + 9689.3776*m.b3931 + 10959.928*m.b3932
                        + 14079.072*m.b3933 + 18291.3472*m.b3934 + 22383.4352*m.b3935 + 3775.1499*m.b3936
                        + 5178.906*m.b3937 + 5519.6235*m.b3938 + 7550.2998*m.b3939 + 10221.525*m.b3940
                        + 12592.9188*m.b3941 + 16776.9297*m.b3942 + 19339.1253*m.b3943 + 23073.3891*m.b3944
                        + 26098.9605*m.b3945 + 33526.602*m.b3946 + 43557.3252*m.b3947 + 53301.8457*m.b3948
                        + 1125.8942*m.b3949 + 1544.548*m.b3950 + 1646.163*m.b3951 + 2251.7884*m.b3952 + 3048.45*m.b3953
                        + 3755.6904*m.b3954 + 5003.5226*m.b3955 + 5767.6674*m.b3956 + 6881.3678*m.b3957
                        + 7783.709*m.b3958 + 9998.916*m.b3959 + 12990.4616*m.b3960 + 15896.6506*m.b3961
                        + 4455.9328*m.b3962 + 6112.832*m.b3963 + 6514.992*m.b3964 + 8911.8656*m.b3965 + 12064.8*m.b3966
                        + 14863.8336*m.b3967 + 19802.3584*m.b3968 + 22826.6016*m.b3969 + 27234.2752*m.b3970
                        + 30805.456*m.b3971 + 39572.544*m.b3972 + 51412.1344*m.b3973 + 62913.9104*m.b3974
                        + 3518.3155*m.b3975 + 4826.57*m.b3976 + 5144.1075*m.b3977 + 7036.631*m.b3978 + 9526.125*m.b3979
                        + 11736.186*m.b3980 + 15635.5465*m.b3981 + 18023.4285*m.b3982 + 21503.6395*m.b3983
                        + 24323.3725*m.b3984 + 31245.69*m.b3985 + 40593.994*m.b3986 + 49675.5665*m.b3987
                        + 1405.9966*m.b3988 + 1928.804*m.b3989 + 2055.699*m.b3990 + 2811.9932*m.b3991 + 3806.85*m.b3992
                        + 4690.0392*m.b3993 + 6248.3098*m.b3994 + 7202.5602*m.b3995 + 8593.3294*m.b3996
                        + 9720.157*m.b3997 + 12486.468*m.b3998 + 16222.2568*m.b3999 + 19851.4538*m.b4000
                        + 5521.441*m.b4001 + 7574.54*m.b4002 + 8072.865*m.b4003 + 11042.882*m.b4004 + 14949.75*m.b4005
                        + 18418.092*m.b4006 + 24537.523*m.b4007 + 28284.927*m.b4008 + 33746.569*m.b4009
                        + 38171.695*m.b4010 + 49035.18*m.b4011 + 63705.868*m.b4012 + 77957.963*m.b4013
                        + 8232.8001*m.b4014 + 11294.094*m.b4015 + 12037.1265*m.b4016 + 16465.6002*m.b4017
                        + 22290.975*m.b4018 + 27462.4812*m.b4019 + 36586.9203*m.b4020 + 42174.5247*m.b4021
                        + 50318.1609*m.b4022 + 56916.2895*m.b4023 + 73114.398*m.b4024 + 94989.2748*m.b4025
                        + 116240.0043*m.b4026 + 3496.9865*m.b4027 + 4797.31*m.b4028 + 5112.9225*m.b4029
                        + 6993.973*m.b4030 + 9468.375*m.b4031 + 11665.038*m.b4032 + 15540.7595*m.b4033
                        + 17914.1655*m.b4034 + 21373.2785*m.b4035 + 24175.9175*m.b4036 + 31056.27*m.b4037
                        + 40347.902*m.b4038 + 49374.4195*m.b4039 + 1091.6293*m.b4040 + 1497.542*m.b4041
                        + 1596.0645*m.b4042 + 2183.2586*m.b4043 + 2955.675*m.b4044 + 3641.3916*m.b4045
                        + 4851.2479*m.b4046 + 5592.1371*m.b4047 + 6671.9437*m.b4048 + 7546.8235*m.b4049
                        + 9694.614*m.b4050 + 12595.1164*m.b4051 + 15412.8599*m.b4052 + 1614.079*m.b4053
                        + 2214.26*m.b4054 + 2359.935*m.b4055 + 3228.158*m.b4056 + 4370.25*m.b4057 + 5384.148*m.b4058
                        + 7173.037*m.b4059 + 8268.513*m.b4060 + 9865.111*m.b4061 + 11158.705*m.b4062 + 14334.42*m.b4063
                        + 18623.092*m.b4064 + 22789.397*m.b4065 + 2805.6499*m.b4066 + 3848.906*m.b4067
                        + 4102.1235*m.b4068 + 5611.2998*m.b4069 + 7596.525*m.b4070 + 9358.9188*m.b4071
                        + 12468.4297*m.b4072 + 14372.6253*m.b4073 + 17147.8891*m.b4074 + 19396.4605*m.b4075
                        + 24916.602*m.b4076 + 32371.3252*m.b4077 + 39613.3457*m.b4078 + 2712.6056*m.b4079
                        + 3721.264*m.b4080 + 3966.084*m.b4081 + 5425.2112*m.b4082 + 7344.6*m.b4083 + 9048.5472*m.b4084
                        + 12054.9368*m.b4085 + 13895.9832*m.b4086 + 16579.2104*m.b4087 + 18753.212*m.b4088
                        + 24090.288*m.b4089 + 31297.7888*m.b4090 + 38299.6408*m.b4091 + 7892.561*m.b4092
                        + 10827.34*m.b4093 + 11539.665*m.b4094 + 15785.122*m.b4095 + 21369.75*m.b4096
                        + 26327.532*m.b4097 + 35074.883*m.b4098 + 40431.567*m.b4099 + 48238.649*m.b4100
                        + 54564.095*m.b4101 + 70092.78*m.b4102 + 91063.628*m.b4103 + 111436.123*m.b4104
                        + 3919.273*m.b4105 + 5376.62*m.b4106 + 5730.345*m.b4107 + 7838.546*m.b4108 + 10611.75*m.b4109
                        + 13073.676*m.b4110 + 17417.419*m.b4111 + 20077.431*m.b4112 + 23954.257*m.b4113
                        + 27095.335*m.b4114 + 34806.54*m.b4115 + 45220.204*m.b4116 + 55336.739*m.b4117
                        + 10446.2794*m.b4118 + 14330.636*m.b4119 + 15273.441*m.b4120 + 20892.5588*m.b4121
                        + 28284.15*m.b4122 + 34846.0728*m.b4123 + 46423.7182*m.b4124 + 53513.6118*m.b4125
                        + 63846.7546*m.b4126 + 72218.863*m.b4127 + 92772.012*m.b4128 + 120528.1912*m.b4129
                        + 147492.4142*m.b4130 + 9461.4613*m.b4131 + 12979.622*m.b4132 + 13833.5445*m.b4133
                        + 18922.9226*m.b4134 + 25617.675*m.b4135 + 31560.9756*m.b4136 + 42047.1439*m.b4137
                        + 48468.6411*m.b4138 + 57827.6317*m.b4139 + 65410.4635*m.b4140 + 84025.974*m.b4141
                        + 109165.4524*m.b4142 + 133587.6359*m.b4143 + 780.5306*m.b4144 + 1070.764*m.b4145
                        + 1141.209*m.b4146 + 1561.0612*m.b4147 + 2113.35*m.b4148 + 2603.6472*m.b4149 + 3468.7118*m.b4150
                        + 3998.4582*m.b4151 + 4770.5354*m.b4152 + 5396.087*m.b4153 + 6931.788*m.b4154
                        + 9005.6888*m.b4155 + 11020.4158*m.b4156 + 3582.718*m.b4157 + 4914.92*m.b4158 + 5238.27*m.b4159
                        + 7165.436*m.b4160 + 9700.5*m.b4161 + 11951.016*m.b4162 + 15921.754*m.b4163 + 18353.346*m.b4164
                        + 21897.262*m.b4165 + 24768.61*m.b4166 + 31817.64*m.b4167 + 41337.064*m.b4168
                        + 50584.874*m.b4169 + 961.5224*m.b4170 + 1319.056*m.b4171 + 1405.836*m.b4172 + 1923.0448*m.b4173
                        + 2603.4*m.b4174 + 3207.3888*m.b4175 + 4273.0472*m.b4176 + 4925.6328*m.b4177 + 5876.7416*m.b4178
                        + 6647.348*m.b4179 + 8539.152*m.b4180 + 11093.9552*m.b4181 + 13575.8632*m.b4182
                        + 4292.0596*m.b4183 + 5888.024*m.b4184 + 6275.394*m.b4185 + 8584.1192*m.b4186 + 11621.1*m.b4187
                        + 14317.1952*m.b4188 + 19074.0988*m.b4189 + 21987.1212*m.b4190 + 26232.6964*m.b4191
                        + 29672.542*m.b4192 + 38117.208*m.b4193 + 49521.3808*m.b4194 + 60600.1628*m.b4195
                        + 3896.2543*m.b4196 + 5345.042*m.b4197 + 5696.6895*m.b4198 + 7792.5086*m.b4199
                        + 10549.425*m.b4200 + 12996.8916*m.b4201 + 17315.1229*m.b4202 + 19959.5121*m.b4203
                        + 23813.5687*m.b4204 + 26936.1985*m.b4205 + 34602.114*m.b4206 + 44954.6164*m.b4207
                        + 55011.7349*m.b4208 + 3138.8532*m.b4209 + 4306.008*m.b4210 + 4589.298*m.b4211
                        + 6277.7064*m.b4212 + 8498.7*m.b4213 + 10470.3984*m.b4214 + 13949.1996*m.b4215
                        + 16079.5404*m.b4216 + 19184.3988*m.b4217 + 21700.014*m.b4218 + 27875.736*m.b4219
                        + 36215.7936*m.b4220 + 44317.8876*m.b4221 + 9722.3953*m.b4222 + 13337.582*m.b4223
                        + 14215.0545*m.b4224 + 19444.7906*m.b4225 + 26324.175*m.b4226 + 32431.3836*m.b4227
                        + 43206.7459*m.b4228 + 49805.3391*m.b4229 + 59422.4377*m.b4230 + 67214.3935*m.b4231
                        + 86343.294*m.b4232 + 112176.0844*m.b4233 + 137271.7979*m.b4234 + 7000.8149*m.b4235
                        + 9604.006*m.b4236 + 10235.8485*m.b4237 + 14001.6298*m.b4238 + 18955.275*m.b4239
                        + 23352.8988*m.b4240 + 31111.9247*m.b4241 + 35863.3803*m.b4242 + 42788.3741*m.b4243
                        + 48399.1355*m.b4244 + 62173.302*m.b4245 + 80774.7452*m.b4246 + 98845.4407*m.b4247
                        + 2642.4969*m.b4248 + 3625.086*m.b4249 + 3863.5785*m.b4250 + 5284.9938*m.b4251
                        + 7154.775*m.b4252 + 8814.6828*m.b4253 + 11743.3707*m.b4254 + 13536.8343*m.b4255
                        + 16150.7121*m.b4256 + 18268.5255*m.b4257 + 23467.662*m.b4258 + 30488.8812*m.b4259
                        + 37309.7667*m.b4260 + 1570.0914*m.b4261 + 2153.916*m.b4262 + 2295.621*m.b4263
                        + 3140.1828*m.b4264 + 4251.15*m.b4265 + 5237.4168*m.b4266 + 6977.5542*m.b4267
                        + 8043.1758*m.b4268 + 9596.2626*m.b4269 + 10854.603*m.b4270 + 13943.772*m.b4271
                        + 18115.5672*m.b4272 + 22168.3302*m.b4273 + 1873.8496*m.b4274 + 2570.624*m.b4275
                        + 2739.744*m.b4276 + 3747.6992*m.b4277 + 5073.6*m.b4278 + 6250.6752*m.b4279 + 8327.4688*m.b4280
                        + 9599.2512*m.b4281 + 11452.8064*m.b4282 + 12954.592*m.b4283 + 16641.408*m.b4284
                        + 21620.3008*m.b4285 + 26457.1328*m.b4286 + 1506.0767*m.b4287 + 2066.098*m.b4288
                        + 2202.0255*m.b4289 + 3012.1534*m.b4290 + 4077.825*m.b4291 + 5023.8804*m.b4292
                        + 6693.0701*m.b4293 + 7715.2449*m.b4294 + 9205.0103*m.b4295 + 10412.0465*m.b4296
                        + 13375.266*m.b4297 + 17376.9716*m.b4298 + 21264.4981*m.b4299 + 4476.1261*m.b4300
                        + 6140.534*m.b4301 + 6544.5165*m.b4302 + 8952.2522*m.b4303 + 12119.475*m.b4304
                        + 14931.1932*m.b4305 + 19892.0983*m.b4306 + 22930.0467*m.b4307 + 27357.6949*m.b4308
                        + 30945.0595*m.b4309 + 39751.878*m.b4310 + 51645.1228*m.b4311 + 63199.0223*m.b4312
                        + 11270.1882*m.b4313 + 15460.908*m.b4314 + 16478.073*m.b4315 + 22540.3764*m.b4316
                        + 30514.95*m.b4317 + 37594.4184*m.b4318 + 50085.2046*m.b4319 + 57734.2854*m.b4320
                        + 68882.4138*m.b4321 + 77914.839*m.b4322 + 100089.036*m.b4323 + 130034.3736*m.b4324
                        + 159125.2926*m.b4325 + 1609.5362*m.b4326 + 2208.028*m.b4327 + 2353.293*m.b4328
                        + 3219.0724*m.b4329 + 4357.95*m.b4330 + 5368.9944*m.b4331 + 7152.8486*m.b4332
                        + 8245.2414*m.b4333 + 9837.3458*m.b4334 + 11127.299*m.b4335 + 14294.076*m.b4336
                        + 18570.6776*m.b4337 + 22725.2566*m.b4338 + 2117.3326*m.b4339 + 2904.644*m.b4340
                        + 3095.739*m.b4341 + 4234.6652*m.b4342 + 5732.85*m.b4343 + 7062.8712*m.b4344 + 9409.5178*m.b4345
                        + 10846.5522*m.b4346 + 12940.9534*m.b4347 + 14637.877*m.b4348 + 18803.748*m.b4349
                        + 24429.5848*m.b4350 + 29894.9018*m.b4351 + 3257.9355*m.b4352 + 4469.37*m.b4353
                        + 4763.4075*m.b4354 + 6515.871*m.b4355 + 8821.125*m.b4356 + 10867.626*m.b4357
                        + 14478.4065*m.b4358 + 16689.5685*m.b4359 + 19912.2195*m.b4360 + 22523.2725*m.b4361
                        + 28933.29*m.b4362 + 37589.754*m.b4363 + 45999.2265*m.b4364 + 5629.6095*m.b4365
                        + 7722.93*m.b4366 + 8231.0175*m.b4367 + 11259.219*m.b4368 + 15242.625*m.b4369
                        + 18778.914*m.b4370 + 25018.2285*m.b4371 + 28839.0465*m.b4372 + 34407.6855*m.b4373
                        + 38919.5025*m.b4374 + 49995.81*m.b4375 + 64953.906*m.b4376 + 79485.2085*m.b4377
                        + 7700.4061*m.b4378 + 10563.734*m.b4379 + 11258.7165*m.b4380 + 15400.8122*m.b4381
                        + 20849.475*m.b4382 + 25686.5532*m.b4383 + 34220.9383*m.b4384 + 39447.2067*m.b4385
                        + 47064.2149*m.b4386 + 53235.6595*m.b4387 + 68386.278*m.b4388 + 88846.5628*m.b4389
                        + 108723.0623*m.b4390 + 2635.4611*m.b4391 + 3615.434*m.b4392 + 3853.2915*m.b4393
                        + 5270.9222*m.b4394 + 7135.725*m.b4395 + 8791.2132*m.b4396 + 11712.1033*m.b4397
                        + 13500.7917*m.b4398 + 16107.7099*m.b4399 + 18219.8845*m.b4400 + 23405.178*m.b4401
                        + 30407.7028*m.b4402 + 37210.4273*m.b4403 + 8206.2635*m.b4404 + 11257.69*m.b4405
                        + 11998.3275*m.b4406 + 16412.527*m.b4407 + 22219.125*m.b4408 + 27373.962*m.b4409
                        + 36468.9905*m.b4410 + 42038.5845*m.b4411 + 50155.9715*m.b4412 + 56732.8325*m.b4413
                        + 72878.73*m.b4414 + 94683.098*m.b4415 + 115865.3305*m.b4416 + 2094.6186*m.b4417
                        + 2873.484*m.b4418 + 3062.529*m.b4419 + 4189.2372*m.b4420 + 5671.35*m.b4421 + 6987.1032*m.b4422
                        + 9308.5758*m.b4423 + 10730.1942*m.b4424 + 12802.1274*m.b4425 + 14480.847*m.b4426
                        + 18602.028*m.b4427 + 24167.5128*m.b4428 + 29574.1998*m.b4429 + 3050.9611*m.b4430
                        + 4185.434*m.b4431 + 4460.7915*m.b4432 + 6101.9222*m.b4433 + 8260.725*m.b4434
                        + 10177.2132*m.b4435 + 13558.6033*m.b4436 + 15629.2917*m.b4437 + 18647.2099*m.b4438
                        + 21092.3845*m.b4439 + 27095.178*m.b4440 + 35201.7028*m.b4441 + 43076.9273*m.b4442
                        + 9911.3924*m.b4443 + 13596.856*m.b4444 + 14491.386*m.b4445 + 19822.7848*m.b4446
                        + 26835.9*m.b4447 + 33061.8288*m.b4448 + 44046.6572*m.b4449 + 50773.5228*m.b4450
                        + 60577.5716*m.b4451 + 68520.998*m.b4452 + 88021.752*m.b4453 + 114356.7152*m.b4454
                        + 139940.2732*m.b4455 + 4804.3434*m.b4456 + 6590.796*m.b4457 + 7024.401*m.b4458
                        + 9608.6868*m.b4459 + 13008.15*m.b4460 + 16026.0408*m.b4461 + 21350.7102*m.b4462
                        + 24611.4198*m.b4463 + 29363.7306*m.b4464 + 33214.143*m.b4465 + 42666.732*m.b4466
                        + 55432.0632*m.b4467 + 67833.1662*m.b4468 + 5181.6728*m.b4469 + 7108.432*m.b4470
                        + 7576.092*m.b4471 + 10363.3456*m.b4472 + 14029.8*m.b4473 + 17284.7136*m.b4474
                        + 23027.5784*m.b4475 + 26544.3816*m.b4476 + 31669.9352*m.b4477 + 35822.756*m.b4478
                        + 46017.744*m.b4479 + 59785.6544*m.b4480 + 73160.7304*m.b4481 + 6755.6699*m.b4482
                        + 9267.706*m.b4483 + 9877.4235*m.b4484 + 13511.3398*m.b4485 + 18291.525*m.b4486
                        + 22535.1588*m.b4487 + 30022.4897*m.b4488 + 34607.5653*m.b4489 + 41290.0691*m.b4490
                        + 46704.3605*m.b4491 + 59996.202*m.b4492 + 77946.2852*m.b4493 + 95384.2057*m.b4494
                        + 13544.9676*m.b4495 + 18581.544*m.b4496 + 19804.014*m.b4497 + 27089.9352*m.b4498
                        + 36674.1*m.b4499 + 45182.4912*m.b4500 + 60194.4228*m.b4501 + 69387.3972*m.b4502
                        + 82785.6684*m.b4503 + 93641.202*m.b4504 + 120291.048*m.b4505 + 156280.5648*m.b4506
                        + 191243.2068*m.b4507 + 13482.2548*m.b4508 + 18495.512*m.b4509 + 19712.322*m.b4510
                        + 26964.5096*m.b4511 + 36504.3*m.b4512 + 44973.2976*m.b4513 + 59915.7244*m.b4514
                        + 69066.1356*m.b4515 + 82402.3732*m.b4516 + 93207.646*m.b4517 + 119734.104*m.b4518
                        + 155556.9904*m.b4519 + 190357.7564*m.b4520 + 2901.1041*m.b4521 + 3979.854*m.b4522
                        + 4241.6865*m.b4523 + 5802.2082*m.b4524 + 7854.975*m.b4525 + 9677.3292*m.b4526
                        + 12892.6323*m.b4527 + 14861.6127*m.b4528 + 17731.2969*m.b4529 + 20056.3695*m.b4530
                        + 25764.318*m.b4531 + 33472.6668*m.b4532 + 40961.0763*m.b4533 + 11246.7817*m.b4534
                        + 15428.798*m.b4535 + 16443.8505*m.b4536 + 22493.5634*m.b4537 + 30451.575*m.b4538
                        + 37516.3404*m.b4539 + 49981.1851*m.b4540 + 57614.3799*m.b4541 + 68739.3553*m.b4542
                        + 77753.0215*m.b4543 + 99881.166*m.b4544 + 129764.3116*m.b4545 + 158794.8131*m.b4546
                        + 8537.5001*m.b4547 + 11712.094*m.b4548 + 12482.6265*m.b4549 + 17075.0002*m.b4550
                        + 23115.975*m.b4551 + 28478.8812*m.b4552 + 37941.0203*m.b4553 + 43735.4247*m.b4554
                        + 52180.4609*m.b4555 + 59022.7895*m.b4556 + 75820.398*m.b4557 + 98504.8748*m.b4558
                        + 120542.1043*m.b4559 + 6501.7163*m.b4560 + 8919.322*m.b4561 + 9506.1195*m.b4562
                        + 13003.4326*m.b4563 + 17603.925*m.b4564 + 21688.0356*m.b4565 + 28893.9089*m.b4566
                        + 33306.6261*m.b4567 + 39737.9267*m.b4568 + 44948.6885*m.b4569 + 57740.874*m.b4570
                        + 75016.1924*m.b4571 + 91798.6009*m.b4572 + 6654.4541*m.b4573 + 9128.854*m.b4574
                        + 9729.4365*m.b4575 + 13308.9082*m.b4576 + 18017.475*m.b4577 + 22197.5292*m.b4578
                        + 29572.6823*m.b4579 + 34089.0627*m.b4580 + 40671.4469*m.b4581 + 46004.6195*m.b4582
                        + 59097.318*m.b4583 + 76778.4668*m.b4584 + 93955.1263*m.b4585 + 719.0643*m.b4586
                        + 986.442*m.b4587 + 1051.3395*m.b4588 + 1438.1286*m.b4589 + 1946.925*m.b4590 + 2398.6116*m.b4591
                        + 3195.5529*m.b4592 + 3683.5821*m.b4593 + 4394.8587*m.b4594 + 4971.1485*m.b4595
                        + 6385.914*m.b4596 + 8296.4964*m.b4597 + 10152.5649*m.b4598 + 569.235*m.b4599 + 780.9*m.b4600
                        + 832.275*m.b4601 + 1138.47*m.b4602 + 1541.25*m.b4603 + 1898.82*m.b4604 + 2529.705*m.b4605
                        + 2916.045*m.b4606 + 3479.115*m.b4607 + 3935.325*m.b4608 + 5055.3*m.b4609 + 6567.78*m.b4610
                        + 8037.105*m.b4611 + 3888.4429*m.b4612 + 5334.326*m.b4613 + 5685.2685*m.b4614
                        + 7776.8858*m.b4615 + 10528.275*m.b4616 + 12970.8348*m.b4617 + 17280.4087*m.b4618
                        + 19919.4963*m.b4619 + 23765.8261*m.b4620 + 26882.1955*m.b4621 + 34532.742*m.b4622
                        + 44864.4892*m.b4623 + 54901.4447*m.b4624 + 1870.7472*m.b4625 + 2566.368*m.b4626
                        + 2735.208*m.b4627 + 3741.4944*m.b4628 + 5065.2*m.b4629 + 6240.3264*m.b4630 + 8313.6816*m.b4631
                        + 9583.3584*m.b4632 + 11433.8448*m.b4633 + 12933.144*m.b4634 + 16613.856*m.b4635
                        + 21584.5056*m.b4636 + 26413.3296*m.b4637 + 942.7418*m.b4638 + 1293.292*m.b4639
                        + 1378.377*m.b4640 + 1885.4836*m.b4641 + 2552.55*m.b4642 + 3144.7416*m.b4643 + 4189.5854*m.b4644
                        + 4829.4246*m.b4645 + 5761.9562*m.b4646 + 6517.511*m.b4647 + 8372.364*m.b4648
                        + 10877.2664*m.b4649 + 13310.6974*m.b4650 + 1441.5634*m.b4651 + 1977.596*m.b4652
                        + 2107.701*m.b4653 + 2883.1268*m.b4654 + 3903.15*m.b4655 + 4808.6808*m.b4656 + 6406.3702*m.b4657
                        + 7384.7598*m.b4658 + 8810.7106*m.b4659 + 9966.043*m.b4660 + 12802.332*m.b4661
                        + 16632.6232*m.b4662 + 20353.6262*m.b4663 + 6884.7519*m.b4664 + 9444.786*m.b4665
                        + 10066.1535*m.b4666 + 13769.5038*m.b4667 + 18641.025*m.b4668 + 22965.7428*m.b4669
                        + 30596.1357*m.b4670 + 35268.8193*m.b4671 + 42079.0071*m.b4672 + 47596.7505*m.b4673
                        + 61142.562*m.b4674 + 79435.6212*m.b4675 + 97206.7317*m.b4676 + 8549.2726*m.b4677
                        + 11728.244*m.b4678 + 12499.839*m.b4679 + 17098.5452*m.b4680 + 23147.85*m.b4681
                        + 28518.1512*m.b4682 + 37993.3378*m.b4683 + 43795.7322*m.b4684 + 52252.4134*m.b4685
                        + 59104.177*m.b4686 + 75924.948*m.b4687 + 98640.7048*m.b4688 + 120708.3218*m.b4689
                        + 423.5053*m.b4690 + 580.982*m.b4691 + 619.2045*m.b4692 + 847.0106*m.b4693 + 1146.675*m.b4694
                        + 1412.7036*m.b4695 + 1882.0759*m.b4696 + 2169.5091*m.b4697 + 2588.4277*m.b4698
                        + 2927.8435*m.b4699 + 3761.094*m.b4700 + 4886.3644*m.b4701 + 5979.5279*m.b4702
                        + 3274.5555*m.b4703 + 4492.17*m.b4704 + 4787.7075*m.b4705 + 6549.111*m.b4706 + 8866.125*m.b4707
                        + 10923.066*m.b4708 + 14552.2665*m.b4709 + 16774.7085*m.b4710 + 20013.7995*m.b4711
                        + 22638.1725*m.b4712 + 29080.89*m.b4713 + 37781.514*m.b4714 + 46233.8865*m.b4715
                        + 4035.9731*m.b4716 + 5536.714*m.b4717 + 5900.9715*m.b4718 + 8071.9462*m.b4719
                        + 10927.725*m.b4720 + 13462.9572*m.b4721 + 17936.0393*m.b4722 + 20675.2557*m.b4723
                        + 24667.5179*m.b4724 + 27902.1245*m.b4725 + 35842.938*m.b4726 + 46566.6788*m.b4727
                        + 56984.4433*m.b4728 + 7404.7086*m.b4729 + 10158.084*m.b4730 + 10826.379*m.b4731
                        + 14809.4172*m.b4732 + 20048.85*m.b4733 + 24700.1832*m.b4734 + 32906.8458*m.b4735
                        + 37932.4242*m.b4736 + 45256.9374*m.b4737 + 51191.397*m.b4738 + 65760.228*m.b4739
                        + 85434.8328*m.b4740 + 104548.0698*m.b4741 + 9873.6096*m.b4742 + 13545.024*m.b4743
                        + 14436.144*m.b4744 + 19747.2192*m.b4745 + 26733.6*m.b4746 + 32935.7952*m.b4747
                        + 43878.7488*m.b4748 + 50579.9712*m.b4749 + 60346.6464*m.b4750 + 68259.792*m.b4751
                        + 87686.208*m.b4752 + 113920.7808*m.b4753 + 139406.8128*m.b4754 + 2829.4165*m.b4755
                        + 3881.51*m.b4756 + 4136.8725*m.b4757 + 5658.833*m.b4758 + 7660.875*m.b4759 + 9438.198*m.b4760
                        + 12574.0495*m.b4761 + 14494.3755*m.b4762 + 17293.1485*m.b4763 + 19560.7675*m.b4764
                        + 25127.67*m.b4765 + 32645.542*m.b4766 + 39948.9095*m.b4767 + 8005.5216*m.b4768
                        + 10982.304*m.b4769 + 11704.824*m.b4770 + 16011.0432*m.b4771 + 21675.6*m.b4772
                        + 26704.3392*m.b4773 + 35576.8848*m.b4774 + 41010.2352*m.b4775 + 48929.0544*m.b4776
                        + 55345.032*m.b4777 + 71095.968*m.b4778 + 92366.9568*m.b4779 + 113031.0288*m.b4780
                        + 6744.6176*m.b4781 + 9252.544*m.b4782 + 9861.264*m.b4783 + 13489.2352*m.b4784 + 18261.6*m.b4785
                        + 22498.2912*m.b4786 + 29973.3728*m.b4787 + 34550.9472*m.b4788 + 41222.5184*m.b4789
                        + 46627.952*m.b4790 + 59898.048*m.b4791 + 77818.7648*m.b4792 + 95228.1568*m.b4793
                        + 6422.8267*m.b4794 + 8811.098*m.b4795 + 9390.7755*m.b4796 + 12845.6534*m.b4797
                        + 17390.325*m.b4798 + 21424.8804*m.b4799 + 28543.3201*m.b4800 + 32902.4949*m.b4801
                        + 39255.7603*m.b4802 + 44403.2965*m.b4803 + 57040.266*m.b4804 + 74105.9716*m.b4805
                        + 90684.7481*m.b4806 + 3382.8902*m.b4807 + 4640.788*m.b4808 + 4946.103*m.b4809
                        + 6765.7804*m.b4810 + 9159.45*m.b4811 + 11284.4424*m.b4812 + 15033.7106*m.b4813
                        + 17329.6794*m.b4814 + 20675.9318*m.b4815 + 23387.129*m.b4816 + 30042.996*m.b4817
                        + 39031.4696*m.b4818 + 47763.4786*m.b4819 + 2637.4555*m.b4820 + 3618.17*m.b4821
                        + 3856.2075*m.b4822 + 5274.911*m.b4823 + 7141.125*m.b4824 + 8797.866*m.b4825
                        + 11720.9665*m.b4826 + 13511.0085*m.b4827 + 16119.8995*m.b4828 + 18233.6725*m.b4829
                        + 23422.89*m.b4830 + 30430.714*m.b4831 + 37238.5865*m.b4832 + 696.0179*m.b4833 + 954.826*m.b4834
                        + 1017.6435*m.b4835 + 1392.0358*m.b4836 + 1884.525*m.b4837 + 2321.7348*m.b4838
                        + 3093.1337*m.b4839 + 3565.5213*m.b4840 + 4254.0011*m.b4841 + 4811.8205*m.b4842
                        + 6181.242*m.b4843 + 8030.5892*m.b4844 + 9827.1697*m.b4845 + 4380.0348*m.b4846
                        + 6008.712*m.b4847 + 6404.022*m.b4848 + 8760.0696*m.b4849 + 11859.3*m.b4850 + 14610.6576*m.b4851
                        + 19465.0644*m.b4852 + 22437.7956*m.b4853 + 26770.3932*m.b4854 + 30280.746*m.b4855
                        + 38898.504*m.b4856 + 50536.4304*m.b4857 + 61842.2964*m.b4858 + 1465.884*m.b4859
                        + 2010.96*m.b4860 + 2143.26*m.b4861 + 2931.768*m.b4862 + 3969*m.b4863 + 4889.808*m.b4864
                        + 6514.452*m.b4865 + 7509.348*m.b4866 + 8959.356*m.b4867 + 10134.18*m.b4868 + 13018.32*m.b4869
                        + 16913.232*m.b4870 + 20697.012*m.b4871 + 3519.1465*m.b4872 + 4827.71*m.b4873
                        + 5145.3225*m.b4874 + 7038.293*m.b4875 + 9528.375*m.b4876 + 11738.958*m.b4877
                        + 15639.2395*m.b4878 + 18027.6855*m.b4879 + 21508.7185*m.b4880 + 24329.1175*m.b4881
                        + 31253.07*m.b4882 + 40603.582*m.b4883 + 49687.2995*m.b4884 + 5021.6776*m.b4885
                        + 6888.944*m.b4886 + 7342.164*m.b4887 + 10043.3552*m.b4888 + 13596.6*m.b4889
                        + 16751.0112*m.b4890 + 22316.5528*m.b4891 + 25724.7672*m.b4892 + 30692.0584*m.b4893
                        + 34716.652*m.b4894 + 44596.848*m.b4895 + 57939.6448*m.b4896 + 70901.7368*m.b4897
                        + 862.6057*m.b4898 + 1183.358*m.b4899 + 1261.2105*m.b4900 + 1725.2114*m.b4901 + 2335.575*m.b4902
                        + 2877.4284*m.b4903 + 3833.4571*m.b4904 + 4418.9079*m.b4905 + 5272.1713*m.b4906
                        + 5963.5015*m.b4907 + 7660.686*m.b4908 + 9952.6636*m.b4909 + 12179.2451*m.b4910
                        + 818.9228*m.b4911 + 1123.432*m.b4912 + 1197.342*m.b4913 + 1637.8456*m.b4914 + 2217.3*m.b4915
                        + 2731.7136*m.b4916 + 3639.3284*m.b4917 + 4195.1316*m.b4918 + 5005.1852*m.b4919
                        + 5661.506*m.b4920 + 7272.744*m.b4921 + 9448.6544*m.b4922 + 11562.4804*m.b4923
                        + 7283.4103*m.b4924 + 9991.682*m.b4925 + 10649.0295*m.b4926 + 14566.8206*m.b4927
                        + 19720.425*m.b4928 + 24295.5636*m.b4929 + 32367.7909*m.b4930 + 37311.0441*m.b4931
                        + 44515.5727*m.b4932 + 50352.8185*m.b4933 + 64682.994*m.b4934 + 84035.3044*m.b4935
                        + 102835.4429*m.b4936 + 6354.7678*m.b4937 + 8717.732*m.b4938 + 9291.267*m.b4939
                        + 12709.5356*m.b4940 + 17206.05*m.b4941 + 21197.8536*m.b4942 + 28240.8634*m.b4943
                        + 32553.8466*m.b4944 + 38839.7902*m.b4945 + 43932.781*m.b4946 + 56435.844*m.b4947
                        + 73320.7144*m.b4948 + 89723.8154*m.b4949 + 2910.7437*m.b4950 + 3993.078*m.b4951
                        + 4255.7805*m.b4952 + 5821.4874*m.b4953 + 7881.075*m.b4954 + 9709.4844*m.b4955
                        + 12935.4711*m.b4956 + 14910.9939*m.b4957 + 17790.2133*m.b4958 + 20123.0115*m.b4959
                        + 25849.926*m.b4960 + 33583.8876*m.b4961 + 41097.1791*m.b4962 + 5195.5782*m.b4963
                        + 7127.508*m.b4964 + 7596.423*m.b4965 + 10391.1564*m.b4966 + 14067.45*m.b4967
                        + 17331.0984*m.b4968 + 23089.3746*m.b4969 + 26615.6154*m.b4970 + 31754.9238*m.b4971
                        + 35918.889*m.b4972 + 46141.236*m.b4973 + 59946.0936*m.b4974 + 73357.0626*m.b4975 + 27.7*m.b4976
                        + 38*m.b4977 + 40.5*m.b4978 + 55.4*m.b4979 + 75*m.b4980 + 92.4*m.b4981 + 123.1*m.b4982
                        + 141.9*m.b4983 + 169.3*m.b4984 + 191.5*m.b4985 + 246*m.b4986 + 319.6*m.b4987 + 391.1*m.b4988
                        + 27.7*m.b4989 + 38*m.b4990 + 40.5*m.b4991 + 55.4*m.b4992 + 75*m.b4993 + 92.4*m.b4994
                        + 123.1*m.b4995 + 141.9*m.b4996 + 169.3*m.b4997 + 191.5*m.b4998 + 246*m.b4999 + 319.6*m.b5000
                        + 391.1*m.b5001 + 27700*m.b5002 + 38000*m.b5003 + 40500*m.b5004 + 55400*m.b5005 + 75000*m.b5006
                        + 92400*m.b5007 + 123100*m.b5008 + 141900*m.b5009 + 169300*m.b5010 + 191500*m.b5011
                        + 246000*m.b5012 + 319600*m.b5013 + 391100*m.b5014 + 2770*m.b5015 + 3800*m.b5016 + 4050*m.b5017
                        + 5540*m.b5018 + 7500*m.b5019 + 9240*m.b5020 + 12310*m.b5021 + 14190*m.b5022 + 16930*m.b5023
                        + 19150*m.b5024 + 24600*m.b5025 + 31960*m.b5026 + 39110*m.b5027, sense=minimize)

m.c2 = Constraint(expr=   m.x273 + m.x274 + m.x275 + m.x276 - m.x588 == -6E-5)

m.c3 = Constraint(expr=   m.x277 - m.x296 == -0.00145)

m.c4 = Constraint(expr= - m.x277 + m.x278 + m.x279 - m.x567 == -0.00513)

m.c5 = Constraint(expr= - m.x278 + m.x280 + m.x281 - m.x289 == -0.00276)

m.c6 = Constraint(expr= - m.x280 + m.x282 - m.x287 == -0.00096)

m.c7 = Constraint(expr=   m.x283 - m.x284 - m.x521 == -0.00078)

m.c8 = Constraint(expr=   m.x284 + m.x285 - m.x546 == -0.00103)

m.c9 = Constraint(expr= - m.x285 + m.x286 - m.x288 == -0.00212)

m.c10 = Constraint(expr=   m.x287 + m.x288 - m.x290 == -0.00116)

m.c11 = Constraint(expr=   m.x289 + m.x290 - m.x291 == -0.00178)

m.c12 = Constraint(expr=   m.x291 - m.x292 - m.x527 == -0.00044)

m.c13 = Constraint(expr=   m.x292 - m.x293 - m.x294 == -3E-5)

m.c14 = Constraint(expr= - m.x279 + m.x293 == -0.00057)

m.c15 = Constraint(expr=   m.x294 - m.x528 == -0.00036)

m.c16 = Constraint(expr=   m.x295 - m.x529 == -0.0033)

m.c17 = Constraint(expr= - m.x273 + m.x296 + m.x297 == -3E-5)

m.c18 = Constraint(expr= - m.x297 + m.x298 == -0.0021)

m.c19 = Constraint(expr=   m.x299 - m.x568 == -0.00467)

m.c20 = Constraint(expr=   m.x300 - m.x524 == 0)

m.c21 = Constraint(expr=   m.x301 - m.x580 == -0.00153)

m.c22 = Constraint(expr=   m.x302 - m.x303 == -0.00461)

m.c23 = Constraint(expr=   m.x303 - m.x523 == -0.00106)

m.c24 = Constraint(expr= - m.x286 + m.x304 == -0.00132)

m.c25 = Constraint(expr=   m.x305 - m.x547 == -0.00274)

m.c26 = Constraint(expr=   m.x306 - m.x511 == -0.00059)

m.c27 = Constraint(expr=   m.x307 + m.x308 - m.x309 == -0.00045)

m.c28 = Constraint(expr=   m.x309 - m.x509 == -0.00064)

m.c29 = Constraint(expr= - m.x283 + m.x310 == -0.00711)

m.c30 = Constraint(expr=   m.x311 - m.x564 == -0.00093)

m.c31 = Constraint(expr= - m.x311 + m.x312 == -4E-5)

m.c32 = Constraint(expr= - m.x312 + m.x313 - m.x517 - m.x581 == -2E-5)

m.c33 = Constraint(expr=   m.x314 - m.x582 == -0.00293)

m.c34 = Constraint(expr= - m.x314 + m.x315 - m.x510 == -0.00234)

m.c35 = Constraint(expr= - m.x315 + m.x316 == -0.00194)

m.c36 = Constraint(expr= - m.x316 + m.x317 - m.x504 == -0.00119)

m.c37 = Constraint(expr=   m.x318 - m.x508 == -0.00141)

m.c38 = Constraint(expr=   m.x319 - m.x320 == -0.00298)

m.c39 = Constraint(expr=   m.x320 - m.x321 == -0.00211)

m.c40 = Constraint(expr=   m.x321 - m.x322 == -0.00774)

m.c41 = Constraint(expr=   m.x322 - m.x563 == -0.00429)

m.c42 = Constraint(expr=   m.x323 - m.x324 - m.x499 == -0.00778)

m.c43 = Constraint(expr=   m.x324 - m.x325 == -0.00375)

m.c44 = Constraint(expr=   m.x325 - m.x326 == -0.00237)

m.c45 = Constraint(expr=   m.x326 + m.x327 - m.x502 == -0.00142)

m.c46 = Constraint(expr= - m.x327 + m.x328 == -0.00032)

m.c47 = Constraint(expr= - m.x328 + m.x329 == -0.00114)

m.c48 = Constraint(expr= - m.x317 + m.x330 + m.x331 == -0.00123)

m.c49 = Constraint(expr= - m.x330 + m.x332 == -0.00137)

m.c50 = Constraint(expr=   m.x333 + m.x334 - m.x498 == -0.00118)

m.c51 = Constraint(expr= - m.x329 + m.x335 == -0.00181)

m.c52 = Constraint(expr= - m.x335 + m.x336 - m.x503 == -0.00097)

m.c53 = Constraint(expr= - m.x336 + m.x337 - m.x501 - m.x586 == -0.00055)

m.c54 = Constraint(expr=   m.x338 + m.x339 - m.x572 == -0.00277)

m.c55 = Constraint(expr= - m.x281 + m.x340 == -0.00065)

m.c56 = Constraint(expr= - m.x340 + m.x341 == -0.00138)

m.c57 = Constraint(expr= - m.x341 + m.x342 == -0.00828)

m.c58 = Constraint(expr= - m.x342 + m.x343 - m.x566 == -0.00122)

m.c59 = Constraint(expr= - m.x343 + m.x344 + m.x345 == -0.00385)

m.c60 = Constraint(expr= - m.x344 + m.x346 + m.x347 + m.x348 == -0.00262)

m.c61 = Constraint(expr= - m.x345 + m.x349 + m.x350 - m.x465 == -0.00278)

m.c62 = Constraint(expr= - m.x349 + m.x351 == -0.00156)

m.c63 = Constraint(expr=   m.x352 + m.x353 - m.x378 - m.x533 == -0.00116)

m.c64 = Constraint(expr=   m.x354 + m.x355 - m.x462 - m.x463 == -0.00122)

m.c65 = Constraint(expr= - m.x354 + m.x356 == -0.00293)

m.c66 = Constraint(expr= - m.x356 + m.x357 + m.x358 == -0.00113)

m.c67 = Constraint(expr= - m.x357 + m.x359 == -0.00112)

m.c68 = Constraint(expr= - m.x359 + m.x360 == -0.00048)

m.c69 = Constraint(expr= - m.x360 + m.x361 - m.x362 == -0.00137)

m.c70 = Constraint(expr=   m.x362 - m.x363 == -0.00226)

m.c71 = Constraint(expr=   m.x363 - m.x364 == -0.00131)

m.c72 = Constraint(expr=   m.x364 - m.x365 == -0.00106)

m.c73 = Constraint(expr=   m.x365 - m.x366 == -0.00038)

m.c74 = Constraint(expr=   m.x366 - m.x367 == -0.00176)

m.c75 = Constraint(expr=   m.x367 - m.x368 == -0.00056)

m.c76 = Constraint(expr=   m.x368 - m.x532 == 0)

m.c77 = Constraint(expr=   m.x369 - m.x579 == -0.00464)

m.c78 = Constraint(expr=   m.x370 - m.x577 == -0.00103)

m.c79 = Constraint(expr= - m.x361 + m.x371 == -0.00308)

m.c80 = Constraint(expr=   m.x372 + m.x373 - m.x469 == -0.0016)

m.c81 = Constraint(expr= - m.x358 + m.x374 + m.x375 - m.x376 == -0.00449)

m.c82 = Constraint(expr=   m.x376 - m.x377 == -0.00125)

m.c83 = Constraint(expr= - m.x372 + m.x377 == -0.00087)

m.c84 = Constraint(expr= - m.x374 + m.x378 + m.x379 - m.x467 == -0.00072)

m.c85 = Constraint(expr=   m.x380 - m.x468 - m.x583 == -0.00049)

m.c86 = Constraint(expr=   m.x381 + m.x382 + m.x383 - m.x584 == -0.00392)

m.c87 = Constraint(expr= - m.x352 + m.x384 == -0.00094)

m.c88 = Constraint(expr= - m.x353 - m.x381 + m.x385 == -0.00333)

m.c89 = Constraint(expr= - m.x384 + m.x386 + m.x387 - m.x520 == -0.00417)

m.c90 = Constraint(expr= - m.x386 + m.x388 + m.x389 == -0.00144)

m.c91 = Constraint(expr= - m.x388 + m.x390 == -0.00184)

m.c92 = Constraint(expr= - m.x390 + m.x391 + m.x392 - m.x410 == -0.002)

m.c93 = Constraint(expr= - m.x389 + m.x393 - m.x418 - m.x485 - m.x487 == -0.00224)

m.c94 = Constraint(expr= - m.x393 + m.x394 + m.x395 == -0.0002)

m.c95 = Constraint(expr= - m.x382 + m.x396 - m.x397 == -0.00227)

m.c96 = Constraint(expr=   m.x397 + m.x398 - m.x471 == -0.00144)

m.c97 = Constraint(expr= - m.x398 + m.x399 == -0.00267)

m.c98 = Constraint(expr= - m.x399 + m.x400 == -0.0006)

m.c99 = Constraint(expr=   m.x401 - m.x472 == -0.00276)

m.c100 = Constraint(expr=   m.x402 - m.x569 == -5E-5)

m.c101 = Constraint(expr=   m.x403 - m.x515 - m.x516 == -0.00206)

m.c102 = Constraint(expr=   m.x404 - m.x512 - m.x513 == -0.00319)

m.c103 = Constraint(expr=   m.x405 + m.x406 - m.x534 == -0.00469)

m.c104 = Constraint(expr= - m.x405 - m.x407 == -0.0017)

m.c105 = Constraint(expr=   m.x407 - m.x408 == -2E-5)

m.c106 = Constraint(expr=   m.x408 + m.x409 - m.x505 == -0.0001)

m.c107 = Constraint(expr= - m.x406 + m.x410 + m.x411 == -0.00111)

m.c108 = Constraint(expr=   m.x412 - m.x552 == -0.00102)

m.c109 = Constraint(expr= - m.x332 - m.x412 + m.x413 == -0.00088)

m.c110 = Constraint(expr= - m.x413 + m.x414 + m.x415 - m.x549 == -0.00233)

m.c111 = Constraint(expr= - m.x414 + m.x416 - m.x550 == -0.00031)

m.c112 = Constraint(expr= - m.x416 + m.x417 - m.x551 == -0.00045)

m.c113 = Constraint(expr=   m.x418 + m.x419 - m.x451 == -0.00296)

m.c114 = Constraint(expr= - m.x419 + m.x420 + m.x421 - m.x422 == -0.00812)

m.c115 = Constraint(expr=   m.x422 - m.x585 == -0.00176)

m.c116 = Constraint(expr= - m.x420 + m.x423 == -0.00596)

m.c117 = Constraint(expr=   m.x424 - m.x427 - m.x497 == 0)

m.c118 = Constraint(expr=   m.x425 - m.x426 - m.x428 == -0.00634)

m.c119 = Constraint(expr=   m.x426 - m.x429 - m.x430 - m.x432 == 0)

m.c120 = Constraint(expr=   m.x427 + m.x428 + m.x429 - m.x431 == 0)

m.c121 = Constraint(expr=   m.x430 + m.x431 - m.x571 == -0.00303)

m.c122 = Constraint(expr=   m.x432 - m.x544 == -0.00185)

m.c123 = Constraint(expr=   m.x433 - m.x535 == -0.00177)

m.c124 = Constraint(expr= - m.x433 + m.x434 == -0.00148)

m.c125 = Constraint(expr=   m.x435 - m.x539 - m.x560 == 0)

m.c126 = Constraint(expr=   m.x436 - m.x440 == -0.00132)

m.c127 = Constraint(expr=   m.x437 - m.x446 - m.x484 == -0.00224)

m.c128 = Constraint(expr= - m.x437 + m.x438 == -0.00126)

m.c129 = Constraint(expr=   m.x439 - m.x558 == -0.00539)

m.c130 = Constraint(expr= - m.x439 + m.x440 - m.x481 == -0.001)

m.c131 = Constraint(expr=   m.x441 - m.x557 == -0.00161)

m.c132 = Constraint(expr=   m.x442 - m.x476 == -0.00471)

m.c133 = Constraint(expr=   m.x443 + m.x444 - m.x570 == -0.00264)

m.c134 = Constraint(expr= - m.x443 + m.x445 - m.x553 == -0.00211)

m.c135 = Constraint(expr=   m.x446 + m.x447 - m.x479 - m.x554 == -0.00151)

m.c136 = Constraint(expr=   m.x448 - m.x450 - m.x555 == -0.00084)

m.c137 = Constraint(expr=   m.x449 - m.x473 - m.x589 == -0.00105)

m.c138 = Constraint(expr=   m.x450 - m.x475 == -0.00116)

m.c139 = Constraint(expr= - m.x391 + m.x451 + m.x452 == -0.00245)

m.c140 = Constraint(expr=   m.x453 + m.x454 - m.x536 == -0.00166)

m.c141 = Constraint(expr= - m.x274 + m.x455 == 0)

m.c142 = Constraint(expr= - m.x275 + m.x456 == 0)

m.c143 = Constraint(expr= - m.x456 + m.x457 == 0)

m.c144 = Constraint(expr= - m.x455 + m.x458 == -0.0008)

m.c145 = Constraint(expr= - m.x457 + m.x459 == -0.00033)

m.c146 = Constraint(expr= - m.x458 + m.x460 == -0.00034)

m.c147 = Constraint(expr= - m.x460 + m.x461 == -0.00102)

m.c148 = Constraint(expr=   m.x462 - m.x573 == -0.00123)

m.c149 = Constraint(expr= - m.x461 + m.x463 == -9E-5)

m.c150 = Constraint(expr= - m.x355 + m.x464 == -0.00043)

m.c151 = Constraint(expr= - m.x464 + m.x465 == -0.00156)

m.c152 = Constraint(expr= - m.x350 + m.x466 == -0.0008)

m.c153 = Constraint(expr= - m.x466 + m.x467 == -0.00138)

m.c154 = Constraint(expr= - m.x379 + m.x468 == -0.00053)

m.c155 = Constraint(expr= - m.x371 + m.x469 == -0.00059)

m.c156 = Constraint(expr= - m.x373 + m.x470 == -0.00233)

m.c157 = Constraint(expr= - m.x470 + m.x471 == -3E-5)

m.c158 = Constraint(expr= - m.x400 + m.x472 == -0.00031)

m.c159 = Constraint(expr= - m.x401 + m.x473 == -0.00849)

m.c160 = Constraint(expr= - m.x449 + m.x474 == -0.00032)

m.c161 = Constraint(expr= - m.x474 + m.x475 == -0.00021)

m.c162 = Constraint(expr=   m.x476 - m.x537 == -2E-5)

m.c163 = Constraint(expr= - m.x447 + m.x477 == -0.00123)

m.c164 = Constraint(expr= - m.x477 + m.x478 == -0.00099)

m.c165 = Constraint(expr=   m.x479 - m.x480 == -0.00055)

m.c166 = Constraint(expr= - m.x444 + m.x480 == -0.00078)

m.c167 = Constraint(expr=   m.x481 - m.x482 == -0.00027)

m.c168 = Constraint(expr=   m.x482 - m.x483 == -0.00027)

m.c169 = Constraint(expr=   m.x483 - m.x556 == -7E-5)

m.c170 = Constraint(expr= - m.x421 + m.x484 == -0.00947)

m.c171 = Constraint(expr=   m.x485 - m.x486 == -0.00264)

m.c172 = Constraint(expr= - m.x385 + m.x486 == -0.00102)

m.c173 = Constraint(expr=   m.x487 - m.x488 == -0.00088)

m.c174 = Constraint(expr= - m.x383 + m.x488 == -0.00049)

m.c175 = Constraint(expr=   m.x489 - m.x490 == 0)

m.c176 = Constraint(expr= - m.x434 + m.x490 == -0.00112)

m.c177 = Constraint(expr=   m.x491 - m.x541 == 0)

m.c178 = Constraint(expr=   m.x492 - m.x542 == 0)

m.c179 = Constraint(expr=   m.x493 - m.x495 == -1E-5)

m.c180 = Constraint(expr= - m.x493 + m.x494 == 0)

m.c181 = Constraint(expr= - m.x492 + m.x495 == 0)

m.c182 = Constraint(expr= - m.x425 + m.x496 == 0)

m.c183 = Constraint(expr= - m.x496 + m.x497 == -1E-5)

m.c184 = Constraint(expr=   m.x498 - m.x562 == -0.00184)

m.c185 = Constraint(expr= - m.x333 + m.x499 == -4E-5)

m.c186 = Constraint(expr= - m.x334 + m.x500 == -0.00168)

m.c187 = Constraint(expr= - m.x500 + m.x501 == -0.00237)

m.c188 = Constraint(expr= - m.x331 + m.x502 == -9E-5)

m.c189 = Constraint(expr= - m.x415 + m.x503 == -0.00123)

m.c190 = Constraint(expr= - m.x409 + m.x504 == -0.0039)

m.c191 = Constraint(expr=   m.x505 - m.x506 == -0.00117)

m.c192 = Constraint(expr=   m.x506 - m.x507 == -0.0017)

m.c193 = Constraint(expr= - m.x453 + m.x507 == -0.00215)

m.c194 = Constraint(expr= - m.x319 + m.x508 == -0.004)

m.c195 = Constraint(expr= - m.x318 + m.x509 == -0.00446)

m.c196 = Constraint(expr= - m.x307 + m.x510 == -5E-5)

m.c197 = Constraint(expr= - m.x308 + m.x511 == -1E-5)

m.c198 = Constraint(expr=   m.x512 - m.x565 == -0.00412)

m.c199 = Constraint(expr=   m.x513 - m.x514 == -0.00039)

m.c200 = Constraint(expr= - m.x403 + m.x514 == -0.00015)

m.c201 = Constraint(expr=   m.x515 - m.x519 == -0.00182)

m.c202 = Constraint(expr=   m.x516 - m.x548 == -0.00343)

m.c203 = Constraint(expr=   m.x517 - m.x518 == -0.00062)

m.c204 = Constraint(expr= - m.x346 + m.x518 == -0.00417)

m.c205 = Constraint(expr= - m.x347 + m.x519 == -0.00226)

m.c206 = Constraint(expr= - m.x348 + m.x520 == -0.00101)

m.c207 = Constraint(expr= - m.x282 + m.x521 == -0.00054)

m.c208 = Constraint(expr= - m.x304 + m.x522 == -0.00077)

m.c209 = Constraint(expr= - m.x522 + m.x523 == -0.00033)

m.c210 = Constraint(expr=   m.x524 - m.x525 - m.x587 == -0.00115)

m.c211 = Constraint(expr= - m.x301 + m.x525 == -0.00153)

m.c212 = Constraint(expr= - m.x299 + m.x526 == 0)

m.c213 = Constraint(expr= - m.x526 + m.x527 == -0.0003)

m.c214 = Constraint(expr= - m.x295 + m.x528 == -0.00032)

m.c215 = Constraint(expr= - m.x298 + m.x529 == -0.00056)

m.c216 = Constraint(expr=   m.x530 - m.x576 == 0)

m.c217 = Constraint(expr=   m.x531 - m.x578 == -0.00019)

m.c218 = Constraint(expr= - m.x369 + m.x532 == -0.00142)

m.c219 = Constraint(expr= - m.x351 + m.x533 == -0.00059)

m.c220 = Constraint(expr= - m.x454 + m.x534 == -0.00148)

m.c221 = Constraint(expr= - m.x417 + m.x535 == -0.00092)

m.c222 = Constraint(expr= - m.x404 + m.x536 == -0.00033)

m.c223 = Constraint(expr= - m.x448 + m.x537 == -6E-5)

m.c224 = Constraint(expr= - m.x489 + m.x538 == -0.00046)

m.c225 = Constraint(expr= - m.x538 + m.x539 == -0.00072)

m.c226 = Constraint(expr= - m.x435 + m.x540 == 0)

m.c227 = Constraint(expr= - m.x540 + m.x541 == 0)

m.c228 = Constraint(expr= - m.x491 + m.x542 == -0.0002)

m.c229 = Constraint(expr= - m.x494 + m.x543 == -8E-5)

m.c230 = Constraint(expr= - m.x543 + m.x544 == -0.0013)

m.c231 = Constraint(expr= - m.x338 + m.x545 == -0.00107)

m.c232 = Constraint(expr= - m.x305 + m.x546 == -0.00103)

m.c233 = Constraint(expr= - m.x306 + m.x547 == -3E-5)

m.c234 = Constraint(expr= - m.x387 + m.x548 == -0.00115)

m.c235 = Constraint(expr= - m.x392 + m.x549 == -0.00143)

m.c236 = Constraint(expr= - m.x452 + m.x550 == -0.00486)

m.c237 = Constraint(expr= - m.x423 + m.x551 == -0.00471)

m.c238 = Constraint(expr= - m.x411 + m.x552 == -0.00134)

m.c239 = Constraint(expr= - m.x394 + m.x553 == -0.00187)

m.c240 = Constraint(expr= - m.x445 + m.x554 == -0.00082)

m.c241 = Constraint(expr= - m.x478 + m.x555 == -0.00094)

m.c242 = Constraint(expr= - m.x441 + m.x556 == -9E-5)

m.c243 = Constraint(expr= - m.x442 + m.x557 == -0.00128)

m.c244 = Constraint(expr=   m.x558 - m.x559 == -0.00043)

m.c245 = Constraint(expr= - m.x438 + m.x559 == -0.00051)

m.c246 = Constraint(expr=   m.x560 - m.x561 == 0)

m.c247 = Constraint(expr= - m.x436 + m.x561 == -1E-5)

m.c248 = Constraint(expr= - m.x424 + m.x562 == -1E-5)

m.c249 = Constraint(expr= - m.x323 + m.x563 == 0)

m.c250 = Constraint(expr= - m.x310 + m.x564 == -0.00175)

m.c251 = Constraint(expr= - m.x313 + m.x565 == -0.00103)

m.c252 = Constraint(expr= - m.x339 + m.x566 == -0.00126)

m.c253 = Constraint(expr= - m.x545 + m.x567 == -0.00136)

m.c254 = Constraint(expr= - m.x300 + m.x568 == -0.00014)

m.c255 = Constraint(expr= - m.x396 + m.x569 == 0)

m.c256 = Constraint(expr= - m.x402 + m.x570 == -0.00196)

m.c257 = Constraint(expr= - m.x337 + m.x571 == -0.00221)

m.c258 = Constraint(expr= - m.x459 + m.x572 + m.x573 == -0.00062)

m.c259 = Constraint(expr= - m.x276 + m.x574 == 0)

m.c260 = Constraint(expr= - m.x574 + m.x575 == -0.0005)

m.c261 = Constraint(expr= - m.x575 + m.x576 == -0.00011)

m.c262 = Constraint(expr= - m.x530 + m.x577 == -0.00012)

m.c263 = Constraint(expr= - m.x370 + m.x578 == -0.00022)

m.c264 = Constraint(expr= - m.x531 + m.x579 == -0.00128)

m.c265 = Constraint(expr= - m.x302 + m.x580 == -0.00019)

m.c266 = Constraint(expr=   m.x581 + m.x582 == -0.00022)

m.c267 = Constraint(expr= - m.x375 + m.x583 == -0.00119)

m.c268 = Constraint(expr= - m.x380 + m.x584 == -0.00169)

m.c269 = Constraint(expr= - m.x395 + m.x585 == -0.00043)

m.c270 = Constraint(expr=SignPower(m.x273,1.852) - 16.4056941079681*(1.27323954473516*m.x590)**2.435*(m.x1 - m.x16)
                          == 0)

m.c271 = Constraint(expr=SignPower(m.x274,1.852) - 19.2565883807645*(1.27323954473516*m.x591)**2.435*(m.x1 - m.x140)
                          == 0)

m.c272 = Constraint(expr=SignPower(m.x275,1.852) - 13.4669574888206*(1.27323954473516*m.x592)**2.435*(m.x1 - m.x141)
                          == 0)

m.c273 = Constraint(expr=SignPower(m.x276,1.852) - 18.3384701259855*(1.27323954473516*m.x593)**2.435*(m.x1 - m.x258)
                          == 0)

m.c274 = Constraint(expr=SignPower(m.x277,1.852) - 1.4203319917192*(1.27323954473516*m.x594)**2.435*(m.x2 - m.x3) == 0)

m.c275 = Constraint(expr=SignPower(m.x278,1.852) - 1.41711309566315*(1.27323954473516*m.x595)**2.435*(m.x3 - m.x4) == 0)

m.c276 = Constraint(expr=SignPower(m.x279,1.852) - 1.25467865211575*(1.27323954473516*m.x596)**2.435*(m.x3 - m.x13)
                          == 0)

m.c277 = Constraint(expr=SignPower(m.x280,1.852) - 1.89884247002725*(1.27323954473516*m.x597)**2.435*(m.x4 - m.x5) == 0)

m.c278 = Constraint(expr=SignPower(m.x281,1.852) - 3.70170241130777*(1.27323954473516*m.x598)**2.435*(m.x4 - m.x54)
                          == 0)

m.c279 = Constraint(expr=SignPower(m.x282,1.852) - 5.06680157906239*(1.27323954473516*m.x599)**2.435*(m.x5 - m.x206)
                          == 0)

m.c280 = Constraint(expr=SignPower(m.x283,1.852) - 1.45896428414041*(1.27323954473516*m.x600)**2.435*(m.x6 - m.x28)
                          == 0)

m.c281 = Constraint(expr=SignPower(m.x284,1.852) - 32.5894546075039*(1.27323954473516*m.x601)**2.435*(m.x7 - m.x6) == 0)

m.c282 = Constraint(expr=SignPower(m.x285,1.852) - 2.88996915992415*(1.27323954473516*m.x602)**2.435*(m.x7 - m.x8) == 0)

m.c283 = Constraint(expr=SignPower(m.x286,1.852) - 2.16163011152708*(1.27323954473516*m.x603)**2.435*(m.x8 - m.x23)
                          == 0)

m.c284 = Constraint(expr=SignPower(m.x287,1.852) - 1.93564066751855*(1.27323954473516*m.x604)**2.435*(m.x9 - m.x5) == 0)

m.c285 = Constraint(expr=SignPower(m.x288,1.852) - 1.48109617512686*(1.27323954473516*m.x605)**2.435*(m.x9 - m.x8) == 0)

m.c286 = Constraint(expr=SignPower(m.x289,1.852) - 2.81827157311282*(1.27323954473516*m.x606)**2.435*(m.x10 - m.x4)
                          == 0)

m.c287 = Constraint(expr=SignPower(m.x290,1.852) - 1.88890127738641*(1.27323954473516*m.x607)**2.435*(m.x10 - m.x9)
                          == 0)

m.c288 = Constraint(expr=SignPower(m.x291,1.852) - 1.38410153864638*(1.27323954473516*m.x608)**2.435*(m.x11 - m.x10)
                          == 0)

m.c289 = Constraint(expr=SignPower(m.x292,1.852) - 1.445313409865*(1.27323954473516*m.x609)**2.435*(m.x12 - m.x11) == 0)

m.c290 = Constraint(expr=SignPower(m.x293,1.852) - 4.78811170778536*(1.27323954473516*m.x610)**2.435*(m.x13 - m.x12)
                          == 0)

m.c291 = Constraint(expr=SignPower(m.x294,1.852) - 6.49810533298003*(1.27323954473516*m.x611)**2.435*(m.x14 - m.x12)
                          == 0)

m.c292 = Constraint(expr=SignPower(m.x295,1.852) - 2.35803159549914*(1.27323954473516*m.x612)**2.435*(m.x15 - m.x213)
                          == 0)

m.c293 = Constraint(expr=SignPower(m.x296,1.852) - 2.87096735655118*(1.27323954473516*m.x613)**2.435*(m.x16 - m.x2)
                          == 0)

m.c294 = Constraint(expr=SignPower(m.x297,1.852) - 26.2543790475061*(1.27323954473516*m.x614)**2.435*(m.x16 - m.x17)
                          == 0)

m.c295 = Constraint(expr=SignPower(m.x298,1.852) - 4.49570858083615*(1.27323954473516*m.x615)**2.435*(m.x17 - m.x214)
                          == 0)

m.c296 = Constraint(expr=SignPower(m.x299,1.852) - 5.96548697902976*(1.27323954473516*m.x616)**2.435*(m.x18 - m.x211)
                          == 0)

m.c297 = Constraint(expr=SignPower(m.x300,1.852) - 18.0736577869132*(1.27323954473516*m.x617)**2.435*(m.x19 - m.x253)
                          == 0)

m.c298 = Constraint(expr=SignPower(m.x301,1.852) - 4.15010708360542*(1.27323954473516*m.x618)**2.435*(m.x20 - m.x210)
                          == 0)

m.c299 = Constraint(expr=SignPower(m.x302,1.852) - 3.43816573653822*(1.27323954473516*m.x619)**2.435*(m.x21 - m.x264)
                          == 0)

m.c300 = Constraint(expr=SignPower(m.x303,1.852) - 2.12735452063999*(1.27323954473516*m.x620)**2.435*(m.x22 - m.x21)
                          == 0)

m.c301 = Constraint(expr=SignPower(m.x304,1.852) - 4.04944713584655*(1.27323954473516*m.x621)**2.435*(m.x23 - m.x207)
                          == 0)

m.c302 = Constraint(expr=SignPower(m.x305,1.852) - 3.19348053182107*(1.27323954473516*m.x622)**2.435*(m.x24 - m.x231)
                          == 0)

m.c303 = Constraint(expr=SignPower(m.x306,1.852) - 3.32507757485094*(1.27323954473516*m.x623)**2.435*(m.x25 - m.x232)
                          == 0)

m.c304 = Constraint(expr=SignPower(m.x307,1.852) - 1.13964958795644*(1.27323954473516*m.x624)**2.435*(m.x26 - m.x195)
                          == 0)

m.c305 = Constraint(expr=SignPower(m.x308,1.852) - 5.54723630752693*(1.27323954473516*m.x625)**2.435*(m.x26 - m.x196)
                          == 0)

m.c306 = Constraint(expr=SignPower(m.x309,1.852) - 16.4700370574271*(1.27323954473516*m.x626)**2.435*(m.x27 - m.x26)
                          == 0)

m.c307 = Constraint(expr=SignPower(m.x310,1.852) - 1.53477684909011*(1.27323954473516*m.x627)**2.435*(m.x28 - m.x249)
                          == 0)

m.c308 = Constraint(expr=SignPower(m.x311,1.852) - 12.5179900816007*(1.27323954473516*m.x628)**2.435*(m.x29 - m.x30)
                          == 0)

m.c309 = Constraint(expr=SignPower(m.x312,1.852) - 10.4236216409347*(1.27323954473516*m.x629)**2.435*(m.x30 - m.x31)
                          == 0)

m.c310 = Constraint(expr=SignPower(m.x313,1.852) - 9.24068021138413*(1.27323954473516*m.x630)**2.435*(m.x31 - m.x250)
                          == 0)

m.c311 = Constraint(expr=SignPower(m.x314,1.852) - 1.20866461854639*(1.27323954473516*m.x631)**2.435*(m.x32 - m.x33)
                          == 0)

m.c312 = Constraint(expr=SignPower(m.x315,1.852) - 1.84854503208721*(1.27323954473516*m.x632)**2.435*(m.x33 - m.x34)
                          == 0)

m.c313 = Constraint(expr=SignPower(m.x316,1.852) - 6.26818428002439*(1.27323954473516*m.x633)**2.435*(m.x34 - m.x35)
                          == 0)

m.c314 = Constraint(expr=SignPower(m.x317,1.852) - 6.93240655901448*(1.27323954473516*m.x634)**2.435*(m.x35 - m.x47)
                          == 0)

m.c315 = Constraint(expr=SignPower(m.x318,1.852) - 1.37866364039114*(1.27323954473516*m.x635)**2.435*(m.x36 - m.x194)
                          == 0)

m.c316 = Constraint(expr=SignPower(m.x319,1.852) - 1.90003023539743*(1.27323954473516*m.x636)**2.435*(m.x37 - m.x193)
                          == 0)

m.c317 = Constraint(expr=SignPower(m.x320,1.852) - 1.09694768296744*(1.27323954473516*m.x637)**2.435*(m.x38 - m.x37)
                          == 0)

m.c318 = Constraint(expr=SignPower(m.x321,1.852) - 2.14860005172225*(1.27323954473516*m.x638)**2.435*(m.x39 - m.x38)
                          == 0)

m.c319 = Constraint(expr=SignPower(m.x322,1.852) - 1.35640318885982*(1.27323954473516*m.x639)**2.435*(m.x40 - m.x39)
                          == 0)

m.c320 = Constraint(expr=SignPower(m.x323,1.852) - 2.61863880157955*(1.27323954473516*m.x640)**2.435*(m.x41 - m.x248)
                          == 0)

m.c321 = Constraint(expr=SignPower(m.x324,1.852) - 1.59679334991346*(1.27323954473516*m.x641)**2.435*(m.x42 - m.x41)
                          == 0)

m.c322 = Constraint(expr=SignPower(m.x325,1.852) - 1.65615051215037*(1.27323954473516*m.x642)**2.435*(m.x43 - m.x42)
                          == 0)

m.c323 = Constraint(expr=SignPower(m.x326,1.852) - 5.00789756737795*(1.27323954473516*m.x643)**2.435*(m.x44 - m.x43)
                          == 0)

m.c324 = Constraint(expr=SignPower(m.x327,1.852) - 8.48965355110472*(1.27323954473516*m.x644)**2.435*(m.x44 - m.x45)
                          == 0)

m.c325 = Constraint(expr=SignPower(m.x328,1.852) - 4.16210966800016*(1.27323954473516*m.x645)**2.435*(m.x45 - m.x46)
                          == 0)

m.c326 = Constraint(expr=SignPower(m.x329,1.852) - 2.63739452576008*(1.27323954473516*m.x646)**2.435*(m.x46 - m.x50)
                          == 0)

m.c327 = Constraint(expr=SignPower(m.x330,1.852) - 27.0158169549163*(1.27323954473516*m.x647)**2.435*(m.x47 - m.x48)
                          == 0)

m.c328 = Constraint(expr=SignPower(m.x331,1.852) - 6.80737994259551*(1.27323954473516*m.x648)**2.435*(m.x47 - m.x187)
                          == 0)

m.c329 = Constraint(expr=SignPower(m.x332,1.852) - 1.8121646908312*(1.27323954473516*m.x649)**2.435*(m.x48 - m.x108)
                          == 0)

m.c330 = Constraint(expr=SignPower(m.x333,1.852) - 4.06038025371461*(1.27323954473516*m.x650)**2.435*(m.x49 - m.x184)
                          == 0)

m.c331 = Constraint(expr=SignPower(m.x334,1.852) - 3.58565503209883*(1.27323954473516*m.x651)**2.435*(m.x49 - m.x185)
                          == 0)

m.c332 = Constraint(expr=SignPower(m.x335,1.852) - 2.95255851044856*(1.27323954473516*m.x652)**2.435*(m.x50 - m.x51)
                          == 0)

m.c333 = Constraint(expr=SignPower(m.x336,1.852) - 19.8910813795665*(1.27323954473516*m.x653)**2.435*(m.x51 - m.x52)
                          == 0)

m.c334 = Constraint(expr=SignPower(m.x337,1.852) - 1.81986342971382*(1.27323954473516*m.x654)**2.435*(m.x52 - m.x256)
                          == 0)

m.c335 = Constraint(expr=SignPower(m.x338,1.852) - 4.93800555876546*(1.27323954473516*m.x655)**2.435*(m.x53 - m.x230)
                          == 0)

m.c336 = Constraint(expr=SignPower(m.x339,1.852) - 2.74615384018736*(1.27323954473516*m.x656)**2.435*(m.x53 - m.x251)
                          == 0)

m.c337 = Constraint(expr=SignPower(m.x340,1.852) - 2.6895455866125*(1.27323954473516*m.x657)**2.435*(m.x54 - m.x55)
                          == 0)

m.c338 = Constraint(expr=SignPower(m.x341,1.852) - 2.38131839692223*(1.27323954473516*m.x658)**2.435*(m.x55 - m.x56)
                          == 0)

m.c339 = Constraint(expr=SignPower(m.x342,1.852) - 2.89876628229622*(1.27323954473516*m.x659)**2.435*(m.x56 - m.x57)
                          == 0)

m.c340 = Constraint(expr=SignPower(m.x343,1.852) - 9.47608978149338*(1.27323954473516*m.x660)**2.435*(m.x57 - m.x58)
                          == 0)

m.c341 = Constraint(expr=SignPower(m.x344,1.852) - 1.39683138441267*(1.27323954473516*m.x661)**2.435*(m.x58 - m.x59)
                          == 0)

m.c342 = Constraint(expr=SignPower(m.x345,1.852) - 1.55778653964958*(1.27323954473516*m.x662)**2.435*(m.x58 - m.x60)
                          == 0)

m.c343 = Constraint(expr=SignPower(m.x346,1.852) - 2.43289116330316*(1.27323954473516*m.x663)**2.435*(m.x59 - m.x203)
                          == 0)

m.c344 = Constraint(expr=SignPower(m.x347,1.852) - 2.70745422328382*(1.27323954473516*m.x664)**2.435*(m.x59 - m.x204)
                          == 0)

m.c345 = Constraint(expr=SignPower(m.x348,1.852) - 22.7344297577005*(1.27323954473516*m.x665)**2.435*(m.x59 - m.x205)
                          == 0)

m.c346 = Constraint(expr=SignPower(m.x349,1.852) - 2.13781745350734*(1.27323954473516*m.x666)**2.435*(m.x60 - m.x61)
                          == 0)

m.c347 = Constraint(expr=SignPower(m.x350,1.852) - 5.47834962787857*(1.27323954473516*m.x667)**2.435*(m.x60 - m.x151)
                          == 0)

m.c348 = Constraint(expr=SignPower(m.x351,1.852) - 3.85039145188864*(1.27323954473516*m.x668)**2.435*(m.x61 - m.x218)
                          == 0)

m.c349 = Constraint(expr=SignPower(m.x352,1.852) - 3.40620937925027*(1.27323954473516*m.x669)**2.435*(m.x62 - m.x86)
                          == 0)

m.c350 = Constraint(expr=SignPower(m.x353,1.852) - 2.42285079401469*(1.27323954473516*m.x670)**2.435*(m.x62 - m.x87)
                          == 0)

m.c351 = Constraint(expr=SignPower(m.x354,1.852) - 2.54996940369426*(1.27323954473516*m.x671)**2.435*(m.x63 - m.x64)
                          == 0)

m.c352 = Constraint(expr=SignPower(m.x355,1.852) - 2.08874168394723*(1.27323954473516*m.x672)**2.435*(m.x63 - m.x149)
                          == 0)

m.c353 = Constraint(expr=SignPower(m.x356,1.852) - 7.52936265847148*(1.27323954473516*m.x673)**2.435*(m.x64 - m.x65)
                          == 0)

m.c354 = Constraint(expr=SignPower(m.x357,1.852) - 3.84757692280508*(1.27323954473516*m.x674)**2.435*(m.x65 - m.x66)
                          == 0)

m.c355 = Constraint(expr=SignPower(m.x358,1.852) - 0.701992207301846*(1.27323954473516*m.x675)**2.435*(m.x65 - m.x80)
                          == 0)

m.c356 = Constraint(expr=SignPower(m.x359,1.852) - 4.78551768885122*(1.27323954473516*m.x676)**2.435*(m.x66 - m.x67)
                          == 0)

m.c357 = Constraint(expr=SignPower(m.x360,1.852) - 9.31573119377834*(1.27323954473516*m.x677)**2.435*(m.x67 - m.x68)
                          == 0)

m.c358 = Constraint(expr=SignPower(m.x361,1.852) - 2.6613148768529*(1.27323954473516*m.x678)**2.435*(m.x68 - m.x78)
                          == 0)

m.c359 = Constraint(expr=SignPower(m.x362,1.852) - 4.25429685228301*(1.27323954473516*m.x679)**2.435*(m.x69 - m.x68)
                          == 0)

m.c360 = Constraint(expr=SignPower(m.x363,1.852) - 3.85355789222737*(1.27323954473516*m.x680)**2.435*(m.x70 - m.x69)
                          == 0)

m.c361 = Constraint(expr=SignPower(m.x364,1.852) - 7.26933160323837*(1.27323954473516*m.x681)**2.435*(m.x71 - m.x70)
                          == 0)

m.c362 = Constraint(expr=SignPower(m.x365,1.852) - 6.81124136154954*(1.27323954473516*m.x682)**2.435*(m.x72 - m.x71)
                          == 0)

m.c363 = Constraint(expr=SignPower(m.x366,1.852) - 10.9075570094323*(1.27323954473516*m.x683)**2.435*(m.x73 - m.x72)
                          == 0)

m.c364 = Constraint(expr=SignPower(m.x367,1.852) - 3.17173322120874*(1.27323954473516*m.x684)**2.435*(m.x74 - m.x73)
                          == 0)

m.c365 = Constraint(expr=SignPower(m.x368,1.852) - 21.3120699159586*(1.27323954473516*m.x685)**2.435*(m.x75 - m.x74)
                          == 0)

m.c366 = Constraint(expr=SignPower(m.x369,1.852) - 3.4789132145747*(1.27323954473516*m.x686)**2.435*(m.x76 - m.x217)
                          == 0)

m.c367 = Constraint(expr=SignPower(m.x370,1.852) - 17.1087744133655*(1.27323954473516*m.x687)**2.435*(m.x77 - m.x262)
                          == 0)

m.c368 = Constraint(expr=SignPower(m.x371,1.852) - 11.0955938998794*(1.27323954473516*m.x688)**2.435*(m.x78 - m.x154)
                          == 0)

m.c369 = Constraint(expr=SignPower(m.x372,1.852) - 3.30031663230844*(1.27323954473516*m.x689)**2.435*(m.x79 - m.x82)
                          == 0)

m.c370 = Constraint(expr=SignPower(m.x373,1.852) - 1.96656404028761*(1.27323954473516*m.x690)**2.435*(m.x79 - m.x155)
                          == 0)

m.c371 = Constraint(expr=SignPower(m.x374,1.852) - 2.7412266595548*(1.27323954473516*m.x691)**2.435*(m.x80 - m.x83)
                          == 0)

m.c372 = Constraint(expr=SignPower(m.x375,1.852) - 5.59232660039405*(1.27323954473516*m.x692)**2.435*(m.x80 - m.x266)
                          == 0)

m.c373 = Constraint(expr=SignPower(m.x376,1.852) - 15.3876883004195*(1.27323954473516*m.x693)**2.435*(m.x81 - m.x80)
                          == 0)

m.c374 = Constraint(expr=SignPower(m.x377,1.852) - 3.64952738052623*(1.27323954473516*m.x694)**2.435*(m.x82 - m.x81)
                          == 0)

m.c375 = Constraint(expr=SignPower(m.x378,1.852) - 2.32142630745719*(1.27323954473516*m.x695)**2.435*(m.x83 - m.x62)
                          == 0)

m.c376 = Constraint(expr=SignPower(m.x379,1.852) - 5.28187667770626*(1.27323954473516*m.x696)**2.435*(m.x83 - m.x153)
                          == 0)

m.c377 = Constraint(expr=SignPower(m.x380,1.852) - 6.89979196347202*(1.27323954473516*m.x697)**2.435*(m.x84 - m.x267)
                          == 0)

m.c378 = Constraint(expr=SignPower(m.x381,1.852) - 2.26545427212725*(1.27323954473516*m.x698)**2.435*(m.x85 - m.x87)
                          == 0)

m.c379 = Constraint(expr=SignPower(m.x382,1.852) - 1.31243871794576*(1.27323954473516*m.x699)**2.435*(m.x85 - m.x94)
                          == 0)

m.c380 = Constraint(expr=SignPower(m.x383,1.852) - 2.62875179704369*(1.27323954473516*m.x700)**2.435*(m.x85 - m.x173)
                          == 0)

m.c381 = Constraint(expr=SignPower(m.x384,1.852) - 4.09438729580887*(1.27323954473516*m.x701)**2.435*(m.x86 - m.x88)
                          == 0)

m.c382 = Constraint(expr=SignPower(m.x385,1.852) - 2.61223882979836*(1.27323954473516*m.x702)**2.435*(m.x87 - m.x171)
                          == 0)

m.c383 = Constraint(expr=SignPower(m.x386,1.852) - 1.22144347859877*(1.27323954473516*m.x703)**2.435*(m.x88 - m.x89)
                          == 0)

m.c384 = Constraint(expr=SignPower(m.x387,1.852) - 4.86793985544601*(1.27323954473516*m.x704)**2.435*(m.x88 - m.x233)
                          == 0)

m.c385 = Constraint(expr=SignPower(m.x388,1.852) - 5.76603912919177*(1.27323954473516*m.x705)**2.435*(m.x89 - m.x90)
                          == 0)

m.c386 = Constraint(expr=SignPower(m.x389,1.852) - 2.4425724963752*(1.27323954473516*m.x706)**2.435*(m.x89 - m.x92)
                          == 0)

m.c387 = Constraint(expr=SignPower(m.x390,1.852) - 2.20801827660582*(1.27323954473516*m.x707)**2.435*(m.x90 - m.x91)
                          == 0)

m.c388 = Constraint(expr=SignPower(m.x391,1.852) - 5.72988315761669*(1.27323954473516*m.x708)**2.435*(m.x91 - m.x138)
                          == 0)

m.c389 = Constraint(expr=SignPower(m.x392,1.852) - 2.62382440199239*(1.27323954473516*m.x709)**2.435*(m.x91 - m.x234)
                          == 0)

m.c390 = Constraint(expr=SignPower(m.x393,1.852) - 4.88924754485017*(1.27323954473516*m.x710)**2.435*(m.x92 - m.x93)
                          == 0)

m.c391 = Constraint(expr=SignPower(m.x394,1.852) - 7.43797840785473*(1.27323954473516*m.x711)**2.435*(m.x93 - m.x238)
                          == 0)

m.c392 = Constraint(expr=SignPower(m.x395,1.852) - 6.36395346936037*(1.27323954473516*m.x712)**2.435*(m.x93 - m.x268)
                          == 0)

m.c393 = Constraint(expr=SignPower(m.x396,1.852) - 5.16438805625815*(1.27323954473516*m.x713)**2.435*(m.x94 - m.x254)
                          == 0)

m.c394 = Constraint(expr=SignPower(m.x397,1.852) - 3.10928924218947*(1.27323954473516*m.x714)**2.435*(m.x95 - m.x94)
                          == 0)

m.c395 = Constraint(expr=SignPower(m.x398,1.852) - 18.3955364108471*(1.27323954473516*m.x715)**2.435*(m.x95 - m.x96)
                          == 0)

m.c396 = Constraint(expr=SignPower(m.x399,1.852) - 2.08866788364095*(1.27323954473516*m.x716)**2.435*(m.x96 - m.x97)
                          == 0)

m.c397 = Constraint(expr=SignPower(m.x400,1.852) - 7.54466398746847*(1.27323954473516*m.x717)**2.435*(m.x97 - m.x157)
                          == 0)

m.c398 = Constraint(expr=SignPower(m.x401,1.852) - 1.09822214630666*(1.27323954473516*m.x718)**2.435*(m.x98 - m.x158)
                          == 0)

m.c399 = Constraint(expr=SignPower(m.x402,1.852) - 1.98210011735278*(1.27323954473516*m.x719)**2.435*(m.x99 - m.x255)
                          == 0)

m.c400 = Constraint(expr=SignPower(m.x403,1.852) - 9.65575555792321*(1.27323954473516*m.x720)**2.435*(m.x100 - m.x199)
                          == 0)

m.c401 = Constraint(expr=SignPower(m.x404,1.852) - 44.9857711818504*(1.27323954473516*m.x721)**2.435*(m.x101 - m.x221)
                          == 0)

m.c402 = Constraint(expr=SignPower(m.x405,1.852) - 3.31352211093*(1.27323954473516*m.x722)**2.435*(m.x102 - m.x103)
                          == 0)

m.c403 = Constraint(expr=SignPower(m.x406,1.852) - 2.94528243619593*(1.27323954473516*m.x723)**2.435*(m.x102 - m.x106)
                          == 0)

m.c404 = Constraint(expr=SignPower(m.x407,1.852) - 3.56078383984668*(1.27323954473516*m.x724)**2.435*(m.x104 - m.x103)
                          == 0)

m.c405 = Constraint(expr=SignPower(m.x408,1.852) - 3.27599156417793*(1.27323954473516*m.x725)**2.435*(m.x105 - m.x104)
                          == 0)

m.c406 = Constraint(expr=SignPower(m.x409,1.852) - 4.68546927799453*(1.27323954473516*m.x726)**2.435*(m.x105 - m.x189)
                          == 0)

m.c407 = Constraint(expr=SignPower(m.x410,1.852) - 4.69784287643993*(1.27323954473516*m.x727)**2.435*(m.x106 - m.x91)
                          == 0)

m.c408 = Constraint(expr=SignPower(m.x411,1.852) - 2.61353587434338*(1.27323954473516*m.x728)**2.435*(m.x106 - m.x237)
                          == 0)

m.c409 = Constraint(expr=SignPower(m.x412,1.852) - 6.87178139815216*(1.27323954473516*m.x729)**2.435*(m.x107 - m.x108)
                          == 0)

m.c410 = Constraint(expr=SignPower(m.x413,1.852) - 4.42524187410847*(1.27323954473516*m.x730)**2.435*(m.x108 - m.x109)
                          == 0)

m.c411 = Constraint(expr=SignPower(m.x414,1.852) - 7.71996794546793*(1.27323954473516*m.x731)**2.435*(m.x109 - m.x110)
                          == 0)

m.c412 = Constraint(expr=SignPower(m.x415,1.852) - 1.67817547348531*(1.27323954473516*m.x732)**2.435*(m.x109 - m.x188)
                          == 0)

m.c413 = Constraint(expr=SignPower(m.x416,1.852) - 2.49579243979524*(1.27323954473516*m.x733)**2.435*(m.x110 - m.x111)
                          == 0)

m.c414 = Constraint(expr=SignPower(m.x417,1.852) - 17.7681886915805*(1.27323954473516*m.x734)**2.435*(m.x111 - m.x220)
                          == 0)

m.c415 = Constraint(expr=SignPower(m.x418,1.852) - 1.26408965524541*(1.27323954473516*m.x735)**2.435*(m.x112 - m.x92)
                          == 0)

m.c416 = Constraint(expr=SignPower(m.x419,1.852) - 3.32506318811164*(1.27323954473516*m.x736)**2.435*(m.x112 - m.x113)
                          == 0)

m.c417 = Constraint(expr=SignPower(m.x420,1.852) - 2.05056949355485*(1.27323954473516*m.x737)**2.435*(m.x113 - m.x115)
                          == 0)

m.c418 = Constraint(expr=SignPower(m.x421,1.852) - 1.21465364874021*(1.27323954473516*m.x738)**2.435*(m.x113 - m.x169)
                          == 0)

m.c419 = Constraint(expr=SignPower(m.x422,1.852) - 2.01203286599105*(1.27323954473516*m.x739)**2.435*(m.x114 - m.x113)
                          == 0)

m.c420 = Constraint(expr=SignPower(m.x423,1.852) - 2.41218859871731*(1.27323954473516*m.x740)**2.435*(m.x115 - m.x236)
                          == 0)

m.c421 = Constraint(expr=SignPower(m.x424,1.852) - 8.77895233041137*(1.27323954473516*m.x741)**2.435*(m.x116 - m.x247)
                          == 0)

m.c422 = Constraint(expr=SignPower(m.x425,1.852) - 7.63817366814645*(1.27323954473516*m.x742)**2.435*(m.x117 - m.x181)
                          == 0)

m.c423 = Constraint(expr=SignPower(m.x426,1.852) - 6.59259261981788*(1.27323954473516*m.x743)**2.435*(m.x118 - m.x117)
                          == 0)

m.c424 = Constraint(expr=SignPower(m.x427,1.852) - 3.74180508861403*(1.27323954473516*m.x744)**2.435*(m.x119 - m.x116)
                          == 0)

m.c425 = Constraint(expr=SignPower(m.x428,1.852) - 6.91749265576494*(1.27323954473516*m.x745)**2.435*(m.x119 - m.x117)
                          == 0)

m.c426 = Constraint(expr=SignPower(m.x429,1.852) - 13.8516930263077*(1.27323954473516*m.x746)**2.435*(m.x119 - m.x118)
                          == 0)

m.c427 = Constraint(expr=SignPower(m.x430,1.852) - 3.49141529469286*(1.27323954473516*m.x747)**2.435*(m.x120 - m.x118)
                          == 0)

m.c428 = Constraint(expr=SignPower(m.x431,1.852) - 3.75119311696206*(1.27323954473516*m.x748)**2.435*(m.x120 - m.x119)
                          == 0)

m.c429 = Constraint(expr=SignPower(m.x432,1.852) - 1.81430382672107*(1.27323954473516*m.x749)**2.435*(m.x121 - m.x118)
                          == 0)

m.c430 = Constraint(expr=SignPower(m.x433,1.852) - 1.98712281530437*(1.27323954473516*m.x750)**2.435*(m.x122 - m.x123)
                          == 0)

m.c431 = Constraint(expr=SignPower(m.x434,1.852) - 7.21649650298664*(1.27323954473516*m.x751)**2.435*(m.x123 - m.x175)
                          == 0)

m.c432 = Constraint(expr=SignPower(m.x435,1.852) - 9.67009260106895*(1.27323954473516*m.x752)**2.435*(m.x124 - m.x225)
                          == 0)

m.c433 = Constraint(expr=SignPower(m.x436,1.852) - 10.8264222292598*(1.27323954473516*m.x753)**2.435*(m.x125 - m.x246)
                          == 0)

m.c434 = Constraint(expr=SignPower(m.x437,1.852) - 2.43961819367804*(1.27323954473516*m.x754)**2.435*(m.x126 - m.x127)
                          == 0)

m.c435 = Constraint(expr=SignPower(m.x438,1.852) - 6.23593697539315*(1.27323954473516*m.x755)**2.435*(m.x127 - m.x244)
                          == 0)

m.c436 = Constraint(expr=SignPower(m.x439,1.852) - 2.00847811193117*(1.27323954473516*m.x756)**2.435*(m.x128 - m.x129)
                          == 0)

m.c437 = Constraint(expr=SignPower(m.x440,1.852) - 4.03549767687087*(1.27323954473516*m.x757)**2.435*(m.x129 - m.x125)
                          == 0)

m.c438 = Constraint(expr=SignPower(m.x441,1.852) - 6.78089091430091*(1.27323954473516*m.x758)**2.435*(m.x130 - m.x241)
                          == 0)

m.c439 = Constraint(expr=SignPower(m.x442,1.852) - 1.73166060695409*(1.27323954473516*m.x759)**2.435*(m.x131 - m.x242)
                          == 0)

m.c440 = Constraint(expr=SignPower(m.x443,1.852) - 2.72122124840939*(1.27323954473516*m.x760)**2.435*(m.x132 - m.x133)
                          == 0)

m.c441 = Constraint(expr=SignPower(m.x444,1.852) - 2.15440059964887*(1.27323954473516*m.x761)**2.435*(m.x132 - m.x165)
                          == 0)

m.c442 = Constraint(expr=SignPower(m.x445,1.852) - 3.74784529112334*(1.27323954473516*m.x762)**2.435*(m.x133 - m.x239)
                          == 0)

m.c443 = Constraint(expr=SignPower(m.x446,1.852) - 0.847740396880757*(1.27323954473516*m.x763)**2.435*(m.x134 - m.x126)
                          == 0)

m.c444 = Constraint(expr=SignPower(m.x447,1.852) - 7.04321222516108*(1.27323954473516*m.x764)**2.435*(m.x134 - m.x162)
                          == 0)

m.c445 = Constraint(expr=SignPower(m.x448,1.852) - 4.34844466694327*(1.27323954473516*m.x765)**2.435*(m.x135 - m.x222)
                          == 0)

m.c446 = Constraint(expr=SignPower(m.x449,1.852) - 6.72411106142805*(1.27323954473516*m.x766)**2.435*(m.x136 - m.x159)
                          == 0)

m.c447 = Constraint(expr=SignPower(m.x450,1.852) - 3.41749423711278*(1.27323954473516*m.x767)**2.435*(m.x137 - m.x135)
                          == 0)

m.c448 = Constraint(expr=SignPower(m.x451,1.852) - 4.38301715069268*(1.27323954473516*m.x768)**2.435*(m.x138 - m.x112)
                          == 0)

m.c449 = Constraint(expr=SignPower(m.x452,1.852) - 2.65110574555862*(1.27323954473516*m.x769)**2.435*(m.x138 - m.x235)
                          == 0)

m.c450 = Constraint(expr=SignPower(m.x453,1.852) - 3.00369330776962*(1.27323954473516*m.x770)**2.435*(m.x139 - m.x192)
                          == 0)

m.c451 = Constraint(expr=SignPower(m.x454,1.852) - 5.67156900862405*(1.27323954473516*m.x771)**2.435*(m.x139 - m.x219)
                          == 0)

m.c452 = Constraint(expr=SignPower(m.x455,1.852) - 2.84912608247371*(1.27323954473516*m.x772)**2.435*(m.x140 - m.x143)
                          == 0)

m.c453 = Constraint(expr=SignPower(m.x456,1.852) - 3.43976621473833*(1.27323954473516*m.x773)**2.435*(m.x141 - m.x142)
                          == 0)

m.c454 = Constraint(expr=SignPower(m.x457,1.852) - 16.3390723540322*(1.27323954473516*m.x774)**2.435*(m.x142 - m.x144)
                          == 0)

m.c455 = Constraint(expr=SignPower(m.x458,1.852) - 16.7365448330586*(1.27323954473516*m.x775)**2.435*(m.x143 - m.x145)
                          == 0)

m.c456 = Constraint(expr=SignPower(m.x459,1.852) - 0.981884995080366*(1.27323954473516*m.x776)**2.435*(m.x144 - m.x257)
                          == 0)

m.c457 = Constraint(expr=SignPower(m.x460,1.852) - 0.86338870886873*(1.27323954473516*m.x777)**2.435*(m.x145 - m.x146)
                          == 0)

m.c458 = Constraint(expr=SignPower(m.x461,1.852) - 22.7438494509915*(1.27323954473516*m.x778)**2.435*(m.x146 - m.x148)
                          == 0)

m.c459 = Constraint(expr=SignPower(m.x462,1.852) - 19.1825652513492*(1.27323954473516*m.x779)**2.435*(m.x147 - m.x63)
                          == 0)

m.c460 = Constraint(expr=SignPower(m.x463,1.852) - 127.487048623018*(1.27323954473516*m.x780)**2.435*(m.x148 - m.x63)
                          == 0)

m.c461 = Constraint(expr=SignPower(m.x464,1.852) - 7.86921633762262*(1.27323954473516*m.x781)**2.435*(m.x149 - m.x150)
                          == 0)

m.c462 = Constraint(expr=SignPower(m.x465,1.852) - 2.38517645866494*(1.27323954473516*m.x782)**2.435*(m.x150 - m.x60)
                          == 0)

m.c463 = Constraint(expr=SignPower(m.x466,1.852) - 3.93301737045242*(1.27323954473516*m.x783)**2.435*(m.x151 - m.x152)
                          == 0)

m.c464 = Constraint(expr=SignPower(m.x467,1.852) - 4.38834822265491*(1.27323954473516*m.x784)**2.435*(m.x152 - m.x83)
                          == 0)

m.c465 = Constraint(expr=SignPower(m.x468,1.852) - 5.8105955004238*(1.27323954473516*m.x785)**2.435*(m.x153 - m.x84)
                          == 0)

m.c466 = Constraint(expr=SignPower(m.x469,1.852) - 1.06966007015088*(1.27323954473516*m.x786)**2.435*(m.x154 - m.x79)
                          == 0)

m.c467 = Constraint(expr=SignPower(m.x470,1.852) - 32.015161185617*(1.27323954473516*m.x787)**2.435*(m.x155 - m.x156)
                          == 0)

m.c468 = Constraint(expr=SignPower(m.x471,1.852) - 1.52320494625528*(1.27323954473516*m.x788)**2.435*(m.x156 - m.x95)
                          == 0)

m.c469 = Constraint(expr=SignPower(m.x472,1.852) - 6.13028022574625*(1.27323954473516*m.x789)**2.435*(m.x157 - m.x98)
                          == 0)

m.c470 = Constraint(expr=SignPower(m.x473,1.852) - 1.71517703022303*(1.27323954473516*m.x790)**2.435*(m.x158 - m.x136)
                          == 0)

m.c471 = Constraint(expr=SignPower(m.x474,1.852) - 3.89496375694132*(1.27323954473516*m.x791)**2.435*(m.x159 - m.x160)
                          == 0)

m.c472 = Constraint(expr=SignPower(m.x475,1.852) - 3.25659771632999*(1.27323954473516*m.x792)**2.435*(m.x160 - m.x137)
                          == 0)

m.c473 = Constraint(expr=SignPower(m.x476,1.852) - 2.15297617861499*(1.27323954473516*m.x793)**2.435*(m.x161 - m.x131)
                          == 0)

m.c474 = Constraint(expr=SignPower(m.x477,1.852) - 2.93273874919211*(1.27323954473516*m.x794)**2.435*(m.x162 - m.x163)
                          == 0)

m.c475 = Constraint(expr=SignPower(m.x478,1.852) - 5.03691325472269*(1.27323954473516*m.x795)**2.435*(m.x163 - m.x240)
                          == 0)

m.c476 = Constraint(expr=SignPower(m.x479,1.852) - 4.94709691583442*(1.27323954473516*m.x796)**2.435*(m.x164 - m.x134)
                          == 0)

m.c477 = Constraint(expr=SignPower(m.x480,1.852) - 11.0283990227107*(1.27323954473516*m.x797)**2.435*(m.x165 - m.x164)
                          == 0)

m.c478 = Constraint(expr=SignPower(m.x481,1.852) - 3.69080448904298*(1.27323954473516*m.x798)**2.435*(m.x166 - m.x129)
                          == 0)

m.c479 = Constraint(expr=SignPower(m.x482,1.852) - 13.9111186774714*(1.27323954473516*m.x799)**2.435*(m.x167 - m.x166)
                          == 0)

m.c480 = Constraint(expr=SignPower(m.x483,1.852) - 5.29859228403476*(1.27323954473516*m.x800)**2.435*(m.x168 - m.x167)
                          == 0)

m.c481 = Constraint(expr=SignPower(m.x484,1.852) - 4.17322984284136*(1.27323954473516*m.x801)**2.435*(m.x169 - m.x126)
                          == 0)

m.c482 = Constraint(expr=SignPower(m.x485,1.852) - 3.22600277518722*(1.27323954473516*m.x802)**2.435*(m.x170 - m.x92)
                          == 0)

m.c483 = Constraint(expr=SignPower(m.x486,1.852) - 7.63271154403431*(1.27323954473516*m.x803)**2.435*(m.x171 - m.x170)
                          == 0)

m.c484 = Constraint(expr=SignPower(m.x487,1.852) - 2.37136901820758*(1.27323954473516*m.x804)**2.435*(m.x172 - m.x92)
                          == 0)

m.c485 = Constraint(expr=SignPower(m.x488,1.852) - 16.2166732596077*(1.27323954473516*m.x805)**2.435*(m.x173 - m.x172)
                          == 0)

m.c486 = Constraint(expr=SignPower(m.x489,1.852) - 3.59001013294879*(1.27323954473516*m.x806)**2.435*(m.x174 - m.x223)
                          == 0)

m.c487 = Constraint(expr=SignPower(m.x490,1.852) - 8.97299234163758*(1.27323954473516*m.x807)**2.435*(m.x175 - m.x174)
                          == 0)

m.c488 = Constraint(expr=SignPower(m.x491,1.852) - 8.9329403933505*(1.27323954473516*m.x808)**2.435*(m.x176 - m.x227)
                          == 0)

m.c489 = Constraint(expr=SignPower(m.x492,1.852) - 6.9047514272325*(1.27323954473516*m.x809)**2.435*(m.x177 - m.x180)
                          == 0)

m.c490 = Constraint(expr=SignPower(m.x493,1.852) - 3.91546346174193*(1.27323954473516*m.x810)**2.435*(m.x178 - m.x179)
                          == 0)

m.c491 = Constraint(expr=SignPower(m.x494,1.852) - 3.87231519565626*(1.27323954473516*m.x811)**2.435*(m.x179 - m.x228)
                          == 0)

m.c492 = Constraint(expr=SignPower(m.x495,1.852) - 6.22926471288787*(1.27323954473516*m.x812)**2.435*(m.x180 - m.x178)
                          == 0)

m.c493 = Constraint(expr=SignPower(m.x496,1.852) - 4.66199105264162*(1.27323954473516*m.x813)**2.435*(m.x181 - m.x182)
                          == 0)

m.c494 = Constraint(expr=SignPower(m.x497,1.852) - 16.1832065428338*(1.27323954473516*m.x814)**2.435*(m.x182 - m.x116)
                          == 0)

m.c495 = Constraint(expr=SignPower(m.x498,1.852) - 4.09240316904732*(1.27323954473516*m.x815)**2.435*(m.x183 - m.x49)
                          == 0)

m.c496 = Constraint(expr=SignPower(m.x499,1.852) - 3.13927724010127*(1.27323954473516*m.x816)**2.435*(m.x184 - m.x41)
                          == 0)

m.c497 = Constraint(expr=SignPower(m.x500,1.852) - 2.00362906817768*(1.27323954473516*m.x817)**2.435*(m.x185 - m.x186)
                          == 0)

m.c498 = Constraint(expr=SignPower(m.x501,1.852) - 7.97844633153259*(1.27323954473516*m.x818)**2.435*(m.x186 - m.x52)
                          == 0)

m.c499 = Constraint(expr=SignPower(m.x502,1.852) - 9.87283918215227*(1.27323954473516*m.x819)**2.435*(m.x187 - m.x44)
                          == 0)

m.c500 = Constraint(expr=SignPower(m.x503,1.852) - 4.63855095276626*(1.27323954473516*m.x820)**2.435*(m.x188 - m.x51)
                          == 0)

m.c501 = Constraint(expr=SignPower(m.x504,1.852) - 3.98463128992217*(1.27323954473516*m.x821)**2.435*(m.x189 - m.x35)
                          == 0)

m.c502 = Constraint(expr=SignPower(m.x505,1.852) - 13.427661607135*(1.27323954473516*m.x822)**2.435*(m.x190 - m.x105)
                          == 0)

m.c503 = Constraint(expr=SignPower(m.x506,1.852) - 5.63877647244088*(1.27323954473516*m.x823)**2.435*(m.x191 - m.x190)
                          == 0)

m.c504 = Constraint(expr=SignPower(m.x507,1.852) - 18.906950969334*(1.27323954473516*m.x824)**2.435*(m.x192 - m.x191)
                          == 0)

m.c505 = Constraint(expr=SignPower(m.x508,1.852) - 4.77727725966997*(1.27323954473516*m.x825)**2.435*(m.x193 - m.x36)
                          == 0)

m.c506 = Constraint(expr=SignPower(m.x509,1.852) - 6.05040293744479*(1.27323954473516*m.x826)**2.435*(m.x194 - m.x27)
                          == 0)

m.c507 = Constraint(expr=SignPower(m.x510,1.852) - 15.1403114602536*(1.27323954473516*m.x827)**2.435*(m.x195 - m.x33)
                          == 0)

m.c508 = Constraint(expr=SignPower(m.x511,1.852) - 3.85537515225781*(1.27323954473516*m.x828)**2.435*(m.x196 - m.x25)
                          == 0)

m.c509 = Constraint(expr=SignPower(m.x512,1.852) - 2.58566055017631*(1.27323954473516*m.x829)**2.435*(m.x197 - m.x101)
                          == 0)

m.c510 = Constraint(expr=SignPower(m.x513,1.852) - 6.08730586636738*(1.27323954473516*m.x830)**2.435*(m.x198 - m.x101)
                          == 0)

m.c511 = Constraint(expr=SignPower(m.x514,1.852) - 19.5004168869941*(1.27323954473516*m.x831)**2.435*(m.x199 - m.x198)
                          == 0)

m.c512 = Constraint(expr=SignPower(m.x515,1.852) - 13.1884662622198*(1.27323954473516*m.x832)**2.435*(m.x200 - m.x100)
                          == 0)

m.c513 = Constraint(expr=SignPower(m.x516,1.852) - 7.58727111178681*(1.27323954473516*m.x833)**2.435*(m.x201 - m.x100)
                          == 0)

m.c514 = Constraint(expr=SignPower(m.x517,1.852) - 7.84751990339382*(1.27323954473516*m.x834)**2.435*(m.x202 - m.x31)
                          == 0)

m.c515 = Constraint(expr=SignPower(m.x518,1.852) - 2.69712536096427*(1.27323954473516*m.x835)**2.435*(m.x203 - m.x202)
                          == 0)

m.c516 = Constraint(expr=SignPower(m.x519,1.852) - 5.43142221428758*(1.27323954473516*m.x836)**2.435*(m.x204 - m.x200)
                          == 0)

m.c517 = Constraint(expr=SignPower(m.x520,1.852) - 2.03778068927177*(1.27323954473516*m.x837)**2.435*(m.x205 - m.x88)
                          == 0)

m.c518 = Constraint(expr=SignPower(m.x521,1.852) - 2.24988780919682*(1.27323954473516*m.x838)**2.435*(m.x206 - m.x6)
                          == 0)

m.c519 = Constraint(expr=SignPower(m.x522,1.852) - 27.2727634714866*(1.27323954473516*m.x839)**2.435*(m.x207 - m.x208)
                          == 0)

m.c520 = Constraint(expr=SignPower(m.x523,1.852) - 5.94164163522151*(1.27323954473516*m.x840)**2.435*(m.x208 - m.x22)
                          == 0)

m.c521 = Constraint(expr=SignPower(m.x524,1.852) - 22.1390853047808*(1.27323954473516*m.x841)**2.435*(m.x209 - m.x19)
                          == 0)

m.c522 = Constraint(expr=SignPower(m.x525,1.852) - 4.95967633721991*(1.27323954473516*m.x842)**2.435*(m.x210 - m.x209)
                          == 0)

m.c523 = Constraint(expr=SignPower(m.x526,1.852) - 5.46351054038171*(1.27323954473516*m.x843)**2.435*(m.x211 - m.x212)
                          == 0)

m.c524 = Constraint(expr=SignPower(m.x527,1.852) - 6.78184836298096*(1.27323954473516*m.x844)**2.435*(m.x212 - m.x11)
                          == 0)

m.c525 = Constraint(expr=SignPower(m.x528,1.852) - 2.18950431238458*(1.27323954473516*m.x845)**2.435*(m.x213 - m.x14)
                          == 0)

m.c526 = Constraint(expr=SignPower(m.x529,1.852) - 3.04067836960774*(1.27323954473516*m.x846)**2.435*(m.x214 - m.x15)
                          == 0)

m.c527 = Constraint(expr=SignPower(m.x530,1.852) - 8.05572427958479*(1.27323954473516*m.x847)**2.435*(m.x215 - m.x261)
                          == 0)

m.c528 = Constraint(expr=SignPower(m.x531,1.852) - 13.5579536554735*(1.27323954473516*m.x848)**2.435*(m.x216 - m.x263)
                          == 0)

m.c529 = Constraint(expr=SignPower(m.x532,1.852) - 11.3601574192814*(1.27323954473516*m.x849)**2.435*(m.x217 - m.x75)
                          == 0)

m.c530 = Constraint(expr=SignPower(m.x533,1.852) - 14.1342246620358*(1.27323954473516*m.x850)**2.435*(m.x218 - m.x62)
                          == 0)

m.c531 = Constraint(expr=SignPower(m.x534,1.852) - 4.75572536619501*(1.27323954473516*m.x851)**2.435*(m.x219 - m.x102)
                          == 0)

m.c532 = Constraint(expr=SignPower(m.x535,1.852) - 1.88880842611462*(1.27323954473516*m.x852)**2.435*(m.x220 - m.x122)
                          == 0)

m.c533 = Constraint(expr=SignPower(m.x536,1.852) - 13.2256897583649*(1.27323954473516*m.x853)**2.435*(m.x221 - m.x139)
                          == 0)

m.c534 = Constraint(expr=SignPower(m.x537,1.852) - 10.0537943051826*(1.27323954473516*m.x854)**2.435*(m.x222 - m.x161)
                          == 0)

m.c535 = Constraint(expr=SignPower(m.x538,1.852) - 6.53396190196446*(1.27323954473516*m.x855)**2.435*(m.x223 - m.x224)
                          == 0)

m.c536 = Constraint(expr=SignPower(m.x539,1.852) - 3.78129716387212*(1.27323954473516*m.x856)**2.435*(m.x224 - m.x124)
                          == 0)

m.c537 = Constraint(expr=SignPower(m.x540,1.852) - 2.76442906511873*(1.27323954473516*m.x857)**2.435*(m.x225 - m.x226)
                          == 0)

m.c538 = Constraint(expr=SignPower(m.x541,1.852) - 8.07723037006979*(1.27323954473516*m.x858)**2.435*(m.x226 - m.x176)
                          == 0)

m.c539 = Constraint(expr=SignPower(m.x542,1.852) - 2.59402180249971*(1.27323954473516*m.x859)**2.435*(m.x227 - m.x177)
                          == 0)

m.c540 = Constraint(expr=SignPower(m.x543,1.852) - 10.1628174389636*(1.27323954473516*m.x860)**2.435*(m.x228 - m.x229)
                          == 0)

m.c541 = Constraint(expr=SignPower(m.x544,1.852) - 6.97721987869906*(1.27323954473516*m.x861)**2.435*(m.x229 - m.x121)
                          == 0)

m.c542 = Constraint(expr=SignPower(m.x545,1.852) - 2.14775337076328*(1.27323954473516*m.x862)**2.435*(m.x230 - m.x252)
                          == 0)

m.c543 = Constraint(expr=SignPower(m.x546,1.852) - 4.43082949400693*(1.27323954473516*m.x863)**2.435*(m.x231 - m.x7)
                          == 0)

m.c544 = Constraint(expr=SignPower(m.x547,1.852) - 4.10817650162271*(1.27323954473516*m.x864)**2.435*(m.x232 - m.x24)
                          == 0)

m.c545 = Constraint(expr=SignPower(m.x548,1.852) - 3.15101636864429*(1.27323954473516*m.x865)**2.435*(m.x233 - m.x201)
                          == 0)

m.c546 = Constraint(expr=SignPower(m.x549,1.852) - 1.57159670400818*(1.27323954473516*m.x866)**2.435*(m.x234 - m.x109)
                          == 0)

m.c547 = Constraint(expr=SignPower(m.x550,1.852) - 1.57890699677754*(1.27323954473516*m.x867)**2.435*(m.x235 - m.x110)
                          == 0)

m.c548 = Constraint(expr=SignPower(m.x551,1.852) - 7.33762929639703*(1.27323954473516*m.x868)**2.435*(m.x236 - m.x111)
                          == 0)

m.c549 = Constraint(expr=SignPower(m.x552,1.852) - 1.89273936348009*(1.27323954473516*m.x869)**2.435*(m.x237 - m.x107)
                          == 0)

m.c550 = Constraint(expr=SignPower(m.x553,1.852) - 2.49337934837126*(1.27323954473516*m.x870)**2.435*(m.x238 - m.x133)
                          == 0)

m.c551 = Constraint(expr=SignPower(m.x554,1.852) - 3.27409340146963*(1.27323954473516*m.x871)**2.435*(m.x239 - m.x134)
                          == 0)

m.c552 = Constraint(expr=SignPower(m.x555,1.852) - 3.19894406305358*(1.27323954473516*m.x872)**2.435*(m.x240 - m.x135)
                          == 0)

m.c553 = Constraint(expr=SignPower(m.x556,1.852) - 29.6040652220636*(1.27323954473516*m.x873)**2.435*(m.x241 - m.x168)
                          == 0)

m.c554 = Constraint(expr=SignPower(m.x557,1.852) - 37.3962009294185*(1.27323954473516*m.x874)**2.435*(m.x242 - m.x130)
                          == 0)

m.c555 = Constraint(expr=SignPower(m.x558,1.852) - 5.4744860561171*(1.27323954473516*m.x875)**2.435*(m.x243 - m.x128)
                          == 0)

m.c556 = Constraint(expr=SignPower(m.x559,1.852) - 11.3789968179867*(1.27323954473516*m.x876)**2.435*(m.x244 - m.x243)
                          == 0)

m.c557 = Constraint(expr=SignPower(m.x560,1.852) - 22.5801236733722*(1.27323954473516*m.x877)**2.435*(m.x245 - m.x124)
                          == 0)

m.c558 = Constraint(expr=SignPower(m.x561,1.852) - 14.7667639425762*(1.27323954473516*m.x878)**2.435*(m.x246 - m.x245)
                          == 0)

m.c559 = Constraint(expr=SignPower(m.x562,1.852) - 3.09193806040528*(1.27323954473516*m.x879)**2.435*(m.x247 - m.x183)
                          == 0)

m.c560 = Constraint(expr=SignPower(m.x563,1.852) - 2.489945920786*(1.27323954473516*m.x880)**2.435*(m.x248 - m.x40)
                          == 0)

m.c561 = Constraint(expr=SignPower(m.x564,1.852) - 50.2643684413337*(1.27323954473516*m.x881)**2.435*(m.x249 - m.x29)
                          == 0)

m.c562 = Constraint(expr=SignPower(m.x565,1.852) - 6.50079879118175*(1.27323954473516*m.x882)**2.435*(m.x250 - m.x197)
                          == 0)

m.c563 = Constraint(expr=SignPower(m.x566,1.852) - 5.27437272464912*(1.27323954473516*m.x883)**2.435*(m.x251 - m.x57)
                          == 0)

m.c564 = Constraint(expr=SignPower(m.x567,1.852) - 2.87482297899711*(1.27323954473516*m.x884)**2.435*(m.x252 - m.x3)
                          == 0)

m.c565 = Constraint(expr=SignPower(m.x568,1.852) - 2.15597206072008*(1.27323954473516*m.x885)**2.435*(m.x253 - m.x18)
                          == 0)

m.c566 = Constraint(expr=SignPower(m.x569,1.852) - 7.52353937147731*(1.27323954473516*m.x886)**2.435*(m.x254 - m.x99)
                          == 0)

m.c567 = Constraint(expr=SignPower(m.x570,1.852) - 2.65906801576271*(1.27323954473516*m.x887)**2.435*(m.x255 - m.x132)
                          == 0)

m.c568 = Constraint(expr=SignPower(m.x571,1.852) - 3.15617989017755*(1.27323954473516*m.x888)**2.435*(m.x256 - m.x120)
                          == 0)

m.c569 = Constraint(expr=SignPower(m.x572,1.852) - 3.31430808121563*(1.27323954473516*m.x889)**2.435*(m.x257 - m.x53)
                          == 0)

m.c570 = Constraint(expr=SignPower(m.x573,1.852) - 6.29261524245083*(1.27323954473516*m.x890)**2.435*(m.x257 - m.x147)
                          == 0)

m.c571 = Constraint(expr=SignPower(m.x574,1.852) - 8.07112250275219*(1.27323954473516*m.x891)**2.435*(m.x258 - m.x259)
                          == 0)

m.c572 = Constraint(expr=SignPower(m.x575,1.852) - 30.5843088748975*(1.27323954473516*m.x892)**2.435*(m.x259 - m.x260)
                          == 0)

m.c573 = Constraint(expr=SignPower(m.x576,1.852) - 4.86005874566511*(1.27323954473516*m.x893)**2.435*(m.x260 - m.x215)
                          == 0)

m.c574 = Constraint(expr=SignPower(m.x577,1.852) - 14.5217673677164*(1.27323954473516*m.x894)**2.435*(m.x261 - m.x77)
                          == 0)

m.c575 = Constraint(expr=SignPower(m.x578,1.852) - 6.04897421464481*(1.27323954473516*m.x895)**2.435*(m.x262 - m.x216)
                          == 0)

m.c576 = Constraint(expr=SignPower(m.x579,1.852) - 4.23906672862821*(1.27323954473516*m.x896)**2.435*(m.x263 - m.x76)
                          == 0)

m.c577 = Constraint(expr=SignPower(m.x580,1.852) - 24.6778179602309*(1.27323954473516*m.x897)**2.435*(m.x264 - m.x20)
                          == 0)

m.c578 = Constraint(expr=SignPower(m.x581,1.852) - 25.9941797151789*(1.27323954473516*m.x898)**2.435*(m.x265 - m.x31)
                          == 0)

m.c579 = Constraint(expr=SignPower(m.x582,1.852) - 2.92270043279829*(1.27323954473516*m.x899)**2.435*(m.x265 - m.x32)
                          == 0)

m.c580 = Constraint(expr=SignPower(m.x583,1.852) - 3.34980397490803*(1.27323954473516*m.x900)**2.435*(m.x266 - m.x84)
                          == 0)

m.c581 = Constraint(expr=SignPower(m.x584,1.852) - 7.31332904235352*(1.27323954473516*m.x901)**2.435*(m.x267 - m.x85)
                          == 0)

m.c582 = Constraint(expr=SignPower(m.x585,1.852) - 4.09718141400654*(1.27323954473516*m.x902)**2.435*(m.x268 - m.x114)
                          == 0)

m.c583 = Constraint(expr=SignPower(m.x586,1.852) - 768.49192909955*(1.27323954473516*m.x903)**2.435*(m.x269 - m.x52)
                          == 0)

m.c584 = Constraint(expr=SignPower(m.x587,1.852) - 768.49192909955*(1.27323954473516*m.x904)**2.435*(m.x270 - m.x209)
                          == 0)

m.c585 = Constraint(expr=SignPower(m.x588,1.852) - 0.76849192909955*(1.27323954473516*m.x905)**2.435*(m.x271 - m.x1)
                          == 0)

m.c586 = Constraint(expr=SignPower(m.x589,1.852) - 7.6849192909955*(1.27323954473516*m.x906)**2.435*(m.x272 - m.x136)
                          == 0)

m.c587 = Constraint(expr=   m.x273 - 2*m.x590 <= 0)

m.c588 = Constraint(expr=   m.x274 - 2*m.x591 <= 0)

m.c589 = Constraint(expr=   m.x275 - 2*m.x592 <= 0)

m.c590 = Constraint(expr=   m.x276 - 2*m.x593 <= 0)

m.c591 = Constraint(expr=   m.x277 - 2*m.x594 <= 0)

m.c592 = Constraint(expr=   m.x278 - 2*m.x595 <= 0)

m.c593 = Constraint(expr=   m.x279 - 2*m.x596 <= 0)

m.c594 = Constraint(expr=   m.x280 - 2*m.x597 <= 0)

m.c595 = Constraint(expr=   m.x281 - 2*m.x598 <= 0)

m.c596 = Constraint(expr=   m.x282 - 2*m.x599 <= 0)

m.c597 = Constraint(expr=   m.x283 - 2*m.x600 <= 0)

m.c598 = Constraint(expr=   m.x284 - 2*m.x601 <= 0)

m.c599 = Constraint(expr=   m.x285 - 2*m.x602 <= 0)

m.c600 = Constraint(expr=   m.x286 - 2*m.x603 <= 0)

m.c601 = Constraint(expr=   m.x287 - 2*m.x604 <= 0)

m.c602 = Constraint(expr=   m.x288 - 2*m.x605 <= 0)

m.c603 = Constraint(expr=   m.x289 - 2*m.x606 <= 0)

m.c604 = Constraint(expr=   m.x290 - 2*m.x607 <= 0)

m.c605 = Constraint(expr=   m.x291 - 2*m.x608 <= 0)

m.c606 = Constraint(expr=   m.x292 - 2*m.x609 <= 0)

m.c607 = Constraint(expr=   m.x293 - 2*m.x610 <= 0)

m.c608 = Constraint(expr=   m.x294 - 2*m.x611 <= 0)

m.c609 = Constraint(expr=   m.x295 - 2*m.x612 <= 0)

m.c610 = Constraint(expr=   m.x296 - 2*m.x613 <= 0)

m.c611 = Constraint(expr=   m.x297 - 2*m.x614 <= 0)

m.c612 = Constraint(expr=   m.x298 - 2*m.x615 <= 0)

m.c613 = Constraint(expr=   m.x299 - 2*m.x616 <= 0)

m.c614 = Constraint(expr=   m.x300 - 2*m.x617 <= 0)

m.c615 = Constraint(expr=   m.x301 - 2*m.x618 <= 0)

m.c616 = Constraint(expr=   m.x302 - 2*m.x619 <= 0)

m.c617 = Constraint(expr=   m.x303 - 2*m.x620 <= 0)

m.c618 = Constraint(expr=   m.x304 - 2*m.x621 <= 0)

m.c619 = Constraint(expr=   m.x305 - 2*m.x622 <= 0)

m.c620 = Constraint(expr=   m.x306 - 2*m.x623 <= 0)

m.c621 = Constraint(expr=   m.x307 - 2*m.x624 <= 0)

m.c622 = Constraint(expr=   m.x308 - 2*m.x625 <= 0)

m.c623 = Constraint(expr=   m.x309 - 2*m.x626 <= 0)

m.c624 = Constraint(expr=   m.x310 - 2*m.x627 <= 0)

m.c625 = Constraint(expr=   m.x311 - 2*m.x628 <= 0)

m.c626 = Constraint(expr=   m.x312 - 2*m.x629 <= 0)

m.c627 = Constraint(expr=   m.x313 - 2*m.x630 <= 0)

m.c628 = Constraint(expr=   m.x314 - 2*m.x631 <= 0)

m.c629 = Constraint(expr=   m.x315 - 2*m.x632 <= 0)

m.c630 = Constraint(expr=   m.x316 - 2*m.x633 <= 0)

m.c631 = Constraint(expr=   m.x317 - 2*m.x634 <= 0)

m.c632 = Constraint(expr=   m.x318 - 2*m.x635 <= 0)

m.c633 = Constraint(expr=   m.x319 - 2*m.x636 <= 0)

m.c634 = Constraint(expr=   m.x320 - 2*m.x637 <= 0)

m.c635 = Constraint(expr=   m.x321 - 2*m.x638 <= 0)

m.c636 = Constraint(expr=   m.x322 - 2*m.x639 <= 0)

m.c637 = Constraint(expr=   m.x323 - 2*m.x640 <= 0)

m.c638 = Constraint(expr=   m.x324 - 2*m.x641 <= 0)

m.c639 = Constraint(expr=   m.x325 - 2*m.x642 <= 0)

m.c640 = Constraint(expr=   m.x326 - 2*m.x643 <= 0)

m.c641 = Constraint(expr=   m.x327 - 2*m.x644 <= 0)

m.c642 = Constraint(expr=   m.x328 - 2*m.x645 <= 0)

m.c643 = Constraint(expr=   m.x329 - 2*m.x646 <= 0)

m.c644 = Constraint(expr=   m.x330 - 2*m.x647 <= 0)

m.c645 = Constraint(expr=   m.x331 - 2*m.x648 <= 0)

m.c646 = Constraint(expr=   m.x332 - 2*m.x649 <= 0)

m.c647 = Constraint(expr=   m.x333 - 2*m.x650 <= 0)

m.c648 = Constraint(expr=   m.x334 - 2*m.x651 <= 0)

m.c649 = Constraint(expr=   m.x335 - 2*m.x652 <= 0)

m.c650 = Constraint(expr=   m.x336 - 2*m.x653 <= 0)

m.c651 = Constraint(expr=   m.x337 - 2*m.x654 <= 0)

m.c652 = Constraint(expr=   m.x338 - 2*m.x655 <= 0)

m.c653 = Constraint(expr=   m.x339 - 2*m.x656 <= 0)

m.c654 = Constraint(expr=   m.x340 - 2*m.x657 <= 0)

m.c655 = Constraint(expr=   m.x341 - 2*m.x658 <= 0)

m.c656 = Constraint(expr=   m.x342 - 2*m.x659 <= 0)

m.c657 = Constraint(expr=   m.x343 - 2*m.x660 <= 0)

m.c658 = Constraint(expr=   m.x344 - 2*m.x661 <= 0)

m.c659 = Constraint(expr=   m.x345 - 2*m.x662 <= 0)

m.c660 = Constraint(expr=   m.x346 - 2*m.x663 <= 0)

m.c661 = Constraint(expr=   m.x347 - 2*m.x664 <= 0)

m.c662 = Constraint(expr=   m.x348 - 2*m.x665 <= 0)

m.c663 = Constraint(expr=   m.x349 - 2*m.x666 <= 0)

m.c664 = Constraint(expr=   m.x350 - 2*m.x667 <= 0)

m.c665 = Constraint(expr=   m.x351 - 2*m.x668 <= 0)

m.c666 = Constraint(expr=   m.x352 - 2*m.x669 <= 0)

m.c667 = Constraint(expr=   m.x353 - 2*m.x670 <= 0)

m.c668 = Constraint(expr=   m.x354 - 2*m.x671 <= 0)

m.c669 = Constraint(expr=   m.x355 - 2*m.x672 <= 0)

m.c670 = Constraint(expr=   m.x356 - 2*m.x673 <= 0)

m.c671 = Constraint(expr=   m.x357 - 2*m.x674 <= 0)

m.c672 = Constraint(expr=   m.x358 - 2*m.x675 <= 0)

m.c673 = Constraint(expr=   m.x359 - 2*m.x676 <= 0)

m.c674 = Constraint(expr=   m.x360 - 2*m.x677 <= 0)

m.c675 = Constraint(expr=   m.x361 - 2*m.x678 <= 0)

m.c676 = Constraint(expr=   m.x362 - 2*m.x679 <= 0)

m.c677 = Constraint(expr=   m.x363 - 2*m.x680 <= 0)

m.c678 = Constraint(expr=   m.x364 - 2*m.x681 <= 0)

m.c679 = Constraint(expr=   m.x365 - 2*m.x682 <= 0)

m.c680 = Constraint(expr=   m.x366 - 2*m.x683 <= 0)

m.c681 = Constraint(expr=   m.x367 - 2*m.x684 <= 0)

m.c682 = Constraint(expr=   m.x368 - 2*m.x685 <= 0)

m.c683 = Constraint(expr=   m.x369 - 2*m.x686 <= 0)

m.c684 = Constraint(expr=   m.x370 - 2*m.x687 <= 0)

m.c685 = Constraint(expr=   m.x371 - 2*m.x688 <= 0)

m.c686 = Constraint(expr=   m.x372 - 2*m.x689 <= 0)

m.c687 = Constraint(expr=   m.x373 - 2*m.x690 <= 0)

m.c688 = Constraint(expr=   m.x374 - 2*m.x691 <= 0)

m.c689 = Constraint(expr=   m.x375 - 2*m.x692 <= 0)

m.c690 = Constraint(expr=   m.x376 - 2*m.x693 <= 0)

m.c691 = Constraint(expr=   m.x377 - 2*m.x694 <= 0)

m.c692 = Constraint(expr=   m.x378 - 2*m.x695 <= 0)

m.c693 = Constraint(expr=   m.x379 - 2*m.x696 <= 0)

m.c694 = Constraint(expr=   m.x380 - 2*m.x697 <= 0)

m.c695 = Constraint(expr=   m.x381 - 2*m.x698 <= 0)

m.c696 = Constraint(expr=   m.x382 - 2*m.x699 <= 0)

m.c697 = Constraint(expr=   m.x383 - 2*m.x700 <= 0)

m.c698 = Constraint(expr=   m.x384 - 2*m.x701 <= 0)

m.c699 = Constraint(expr=   m.x385 - 2*m.x702 <= 0)

m.c700 = Constraint(expr=   m.x386 - 2*m.x703 <= 0)

m.c701 = Constraint(expr=   m.x387 - 2*m.x704 <= 0)

m.c702 = Constraint(expr=   m.x388 - 2*m.x705 <= 0)

m.c703 = Constraint(expr=   m.x389 - 2*m.x706 <= 0)

m.c704 = Constraint(expr=   m.x390 - 2*m.x707 <= 0)

m.c705 = Constraint(expr=   m.x391 - 2*m.x708 <= 0)

m.c706 = Constraint(expr=   m.x392 - 2*m.x709 <= 0)

m.c707 = Constraint(expr=   m.x393 - 2*m.x710 <= 0)

m.c708 = Constraint(expr=   m.x394 - 2*m.x711 <= 0)

m.c709 = Constraint(expr=   m.x395 - 2*m.x712 <= 0)

m.c710 = Constraint(expr=   m.x396 - 2*m.x713 <= 0)

m.c711 = Constraint(expr=   m.x397 - 2*m.x714 <= 0)

m.c712 = Constraint(expr=   m.x398 - 2*m.x715 <= 0)

m.c713 = Constraint(expr=   m.x399 - 2*m.x716 <= 0)

m.c714 = Constraint(expr=   m.x400 - 2*m.x717 <= 0)

m.c715 = Constraint(expr=   m.x401 - 2*m.x718 <= 0)

m.c716 = Constraint(expr=   m.x402 - 2*m.x719 <= 0)

m.c717 = Constraint(expr=   m.x403 - 2*m.x720 <= 0)

m.c718 = Constraint(expr=   m.x404 - 2*m.x721 <= 0)

m.c719 = Constraint(expr=   m.x405 - 2*m.x722 <= 0)

m.c720 = Constraint(expr=   m.x406 - 2*m.x723 <= 0)

m.c721 = Constraint(expr=   m.x407 - 2*m.x724 <= 0)

m.c722 = Constraint(expr=   m.x408 - 2*m.x725 <= 0)

m.c723 = Constraint(expr=   m.x409 - 2*m.x726 <= 0)

m.c724 = Constraint(expr=   m.x410 - 2*m.x727 <= 0)

m.c725 = Constraint(expr=   m.x411 - 2*m.x728 <= 0)

m.c726 = Constraint(expr=   m.x412 - 2*m.x729 <= 0)

m.c727 = Constraint(expr=   m.x413 - 2*m.x730 <= 0)

m.c728 = Constraint(expr=   m.x414 - 2*m.x731 <= 0)

m.c729 = Constraint(expr=   m.x415 - 2*m.x732 <= 0)

m.c730 = Constraint(expr=   m.x416 - 2*m.x733 <= 0)

m.c731 = Constraint(expr=   m.x417 - 2*m.x734 <= 0)

m.c732 = Constraint(expr=   m.x418 - 2*m.x735 <= 0)

m.c733 = Constraint(expr=   m.x419 - 2*m.x736 <= 0)

m.c734 = Constraint(expr=   m.x420 - 2*m.x737 <= 0)

m.c735 = Constraint(expr=   m.x421 - 2*m.x738 <= 0)

m.c736 = Constraint(expr=   m.x422 - 2*m.x739 <= 0)

m.c737 = Constraint(expr=   m.x423 - 2*m.x740 <= 0)

m.c738 = Constraint(expr=   m.x424 - 2*m.x741 <= 0)

m.c739 = Constraint(expr=   m.x425 - 2*m.x742 <= 0)

m.c740 = Constraint(expr=   m.x426 - 2*m.x743 <= 0)

m.c741 = Constraint(expr=   m.x427 - 2*m.x744 <= 0)

m.c742 = Constraint(expr=   m.x428 - 2*m.x745 <= 0)

m.c743 = Constraint(expr=   m.x429 - 2*m.x746 <= 0)

m.c744 = Constraint(expr=   m.x430 - 2*m.x747 <= 0)

m.c745 = Constraint(expr=   m.x431 - 2*m.x748 <= 0)

m.c746 = Constraint(expr=   m.x432 - 2*m.x749 <= 0)

m.c747 = Constraint(expr=   m.x433 - 2*m.x750 <= 0)

m.c748 = Constraint(expr=   m.x434 - 2*m.x751 <= 0)

m.c749 = Constraint(expr=   m.x435 - 2*m.x752 <= 0)

m.c750 = Constraint(expr=   m.x436 - 2*m.x753 <= 0)

m.c751 = Constraint(expr=   m.x437 - 2*m.x754 <= 0)

m.c752 = Constraint(expr=   m.x438 - 2*m.x755 <= 0)

m.c753 = Constraint(expr=   m.x439 - 2*m.x756 <= 0)

m.c754 = Constraint(expr=   m.x440 - 2*m.x757 <= 0)

m.c755 = Constraint(expr=   m.x441 - 2*m.x758 <= 0)

m.c756 = Constraint(expr=   m.x442 - 2*m.x759 <= 0)

m.c757 = Constraint(expr=   m.x443 - 2*m.x760 <= 0)

m.c758 = Constraint(expr=   m.x444 - 2*m.x761 <= 0)

m.c759 = Constraint(expr=   m.x445 - 2*m.x762 <= 0)

m.c760 = Constraint(expr=   m.x446 - 2*m.x763 <= 0)

m.c761 = Constraint(expr=   m.x447 - 2*m.x764 <= 0)

m.c762 = Constraint(expr=   m.x448 - 2*m.x765 <= 0)

m.c763 = Constraint(expr=   m.x449 - 2*m.x766 <= 0)

m.c764 = Constraint(expr=   m.x450 - 2*m.x767 <= 0)

m.c765 = Constraint(expr=   m.x451 - 2*m.x768 <= 0)

m.c766 = Constraint(expr=   m.x452 - 2*m.x769 <= 0)

m.c767 = Constraint(expr=   m.x453 - 2*m.x770 <= 0)

m.c768 = Constraint(expr=   m.x454 - 2*m.x771 <= 0)

m.c769 = Constraint(expr=   m.x455 - 2*m.x772 <= 0)

m.c770 = Constraint(expr=   m.x456 - 2*m.x773 <= 0)

m.c771 = Constraint(expr=   m.x457 - 2*m.x774 <= 0)

m.c772 = Constraint(expr=   m.x458 - 2*m.x775 <= 0)

m.c773 = Constraint(expr=   m.x459 - 2*m.x776 <= 0)

m.c774 = Constraint(expr=   m.x460 - 2*m.x777 <= 0)

m.c775 = Constraint(expr=   m.x461 - 2*m.x778 <= 0)

m.c776 = Constraint(expr=   m.x462 - 2*m.x779 <= 0)

m.c777 = Constraint(expr=   m.x463 - 2*m.x780 <= 0)

m.c778 = Constraint(expr=   m.x464 - 2*m.x781 <= 0)

m.c779 = Constraint(expr=   m.x465 - 2*m.x782 <= 0)

m.c780 = Constraint(expr=   m.x466 - 2*m.x783 <= 0)

m.c781 = Constraint(expr=   m.x467 - 2*m.x784 <= 0)

m.c782 = Constraint(expr=   m.x468 - 2*m.x785 <= 0)

m.c783 = Constraint(expr=   m.x469 - 2*m.x786 <= 0)

m.c784 = Constraint(expr=   m.x470 - 2*m.x787 <= 0)

m.c785 = Constraint(expr=   m.x471 - 2*m.x788 <= 0)

m.c786 = Constraint(expr=   m.x472 - 2*m.x789 <= 0)

m.c787 = Constraint(expr=   m.x473 - 2*m.x790 <= 0)

m.c788 = Constraint(expr=   m.x474 - 2*m.x791 <= 0)

m.c789 = Constraint(expr=   m.x475 - 2*m.x792 <= 0)

m.c790 = Constraint(expr=   m.x476 - 2*m.x793 <= 0)

m.c791 = Constraint(expr=   m.x477 - 2*m.x794 <= 0)

m.c792 = Constraint(expr=   m.x478 - 2*m.x795 <= 0)

m.c793 = Constraint(expr=   m.x479 - 2*m.x796 <= 0)

m.c794 = Constraint(expr=   m.x480 - 2*m.x797 <= 0)

m.c795 = Constraint(expr=   m.x481 - 2*m.x798 <= 0)

m.c796 = Constraint(expr=   m.x482 - 2*m.x799 <= 0)

m.c797 = Constraint(expr=   m.x483 - 2*m.x800 <= 0)

m.c798 = Constraint(expr=   m.x484 - 2*m.x801 <= 0)

m.c799 = Constraint(expr=   m.x485 - 2*m.x802 <= 0)

m.c800 = Constraint(expr=   m.x486 - 2*m.x803 <= 0)

m.c801 = Constraint(expr=   m.x487 - 2*m.x804 <= 0)

m.c802 = Constraint(expr=   m.x488 - 2*m.x805 <= 0)

m.c803 = Constraint(expr=   m.x489 - 2*m.x806 <= 0)

m.c804 = Constraint(expr=   m.x490 - 2*m.x807 <= 0)

m.c805 = Constraint(expr=   m.x491 - 2*m.x808 <= 0)

m.c806 = Constraint(expr=   m.x492 - 2*m.x809 <= 0)

m.c807 = Constraint(expr=   m.x493 - 2*m.x810 <= 0)

m.c808 = Constraint(expr=   m.x494 - 2*m.x811 <= 0)

m.c809 = Constraint(expr=   m.x495 - 2*m.x812 <= 0)

m.c810 = Constraint(expr=   m.x496 - 2*m.x813 <= 0)

m.c811 = Constraint(expr=   m.x497 - 2*m.x814 <= 0)

m.c812 = Constraint(expr=   m.x498 - 2*m.x815 <= 0)

m.c813 = Constraint(expr=   m.x499 - 2*m.x816 <= 0)

m.c814 = Constraint(expr=   m.x500 - 2*m.x817 <= 0)

m.c815 = Constraint(expr=   m.x501 - 2*m.x818 <= 0)

m.c816 = Constraint(expr=   m.x502 - 2*m.x819 <= 0)

m.c817 = Constraint(expr=   m.x503 - 2*m.x820 <= 0)

m.c818 = Constraint(expr=   m.x504 - 2*m.x821 <= 0)

m.c819 = Constraint(expr=   m.x505 - 2*m.x822 <= 0)

m.c820 = Constraint(expr=   m.x506 - 2*m.x823 <= 0)

m.c821 = Constraint(expr=   m.x507 - 2*m.x824 <= 0)

m.c822 = Constraint(expr=   m.x508 - 2*m.x825 <= 0)

m.c823 = Constraint(expr=   m.x509 - 2*m.x826 <= 0)

m.c824 = Constraint(expr=   m.x510 - 2*m.x827 <= 0)

m.c825 = Constraint(expr=   m.x511 - 2*m.x828 <= 0)

m.c826 = Constraint(expr=   m.x512 - 2*m.x829 <= 0)

m.c827 = Constraint(expr=   m.x513 - 2*m.x830 <= 0)

m.c828 = Constraint(expr=   m.x514 - 2*m.x831 <= 0)

m.c829 = Constraint(expr=   m.x515 - 2*m.x832 <= 0)

m.c830 = Constraint(expr=   m.x516 - 2*m.x833 <= 0)

m.c831 = Constraint(expr=   m.x517 - 2*m.x834 <= 0)

m.c832 = Constraint(expr=   m.x518 - 2*m.x835 <= 0)

m.c833 = Constraint(expr=   m.x519 - 2*m.x836 <= 0)

m.c834 = Constraint(expr=   m.x520 - 2*m.x837 <= 0)

m.c835 = Constraint(expr=   m.x521 - 2*m.x838 <= 0)

m.c836 = Constraint(expr=   m.x522 - 2*m.x839 <= 0)

m.c837 = Constraint(expr=   m.x523 - 2*m.x840 <= 0)

m.c838 = Constraint(expr=   m.x524 - 2*m.x841 <= 0)

m.c839 = Constraint(expr=   m.x525 - 2*m.x842 <= 0)

m.c840 = Constraint(expr=   m.x526 - 2*m.x843 <= 0)

m.c841 = Constraint(expr=   m.x527 - 2*m.x844 <= 0)

m.c842 = Constraint(expr=   m.x528 - 2*m.x845 <= 0)

m.c843 = Constraint(expr=   m.x529 - 2*m.x846 <= 0)

m.c844 = Constraint(expr=   m.x530 - 2*m.x847 <= 0)

m.c845 = Constraint(expr=   m.x531 - 2*m.x848 <= 0)

m.c846 = Constraint(expr=   m.x532 - 2*m.x849 <= 0)

m.c847 = Constraint(expr=   m.x533 - 2*m.x850 <= 0)

m.c848 = Constraint(expr=   m.x534 - 2*m.x851 <= 0)

m.c849 = Constraint(expr=   m.x535 - 2*m.x852 <= 0)

m.c850 = Constraint(expr=   m.x536 - 2*m.x853 <= 0)

m.c851 = Constraint(expr=   m.x537 - 2*m.x854 <= 0)

m.c852 = Constraint(expr=   m.x538 - 2*m.x855 <= 0)

m.c853 = Constraint(expr=   m.x539 - 2*m.x856 <= 0)

m.c854 = Constraint(expr=   m.x540 - 2*m.x857 <= 0)

m.c855 = Constraint(expr=   m.x541 - 2*m.x858 <= 0)

m.c856 = Constraint(expr=   m.x542 - 2*m.x859 <= 0)

m.c857 = Constraint(expr=   m.x543 - 2*m.x860 <= 0)

m.c858 = Constraint(expr=   m.x544 - 2*m.x861 <= 0)

m.c859 = Constraint(expr=   m.x545 - 2*m.x862 <= 0)

m.c860 = Constraint(expr=   m.x546 - 2*m.x863 <= 0)

m.c861 = Constraint(expr=   m.x547 - 2*m.x864 <= 0)

m.c862 = Constraint(expr=   m.x548 - 2*m.x865 <= 0)

m.c863 = Constraint(expr=   m.x549 - 2*m.x866 <= 0)

m.c864 = Constraint(expr=   m.x550 - 2*m.x867 <= 0)

m.c865 = Constraint(expr=   m.x551 - 2*m.x868 <= 0)

m.c866 = Constraint(expr=   m.x552 - 2*m.x869 <= 0)

m.c867 = Constraint(expr=   m.x553 - 2*m.x870 <= 0)

m.c868 = Constraint(expr=   m.x554 - 2*m.x871 <= 0)

m.c869 = Constraint(expr=   m.x555 - 2*m.x872 <= 0)

m.c870 = Constraint(expr=   m.x556 - 2*m.x873 <= 0)

m.c871 = Constraint(expr=   m.x557 - 2*m.x874 <= 0)

m.c872 = Constraint(expr=   m.x558 - 2*m.x875 <= 0)

m.c873 = Constraint(expr=   m.x559 - 2*m.x876 <= 0)

m.c874 = Constraint(expr=   m.x560 - 2*m.x877 <= 0)

m.c875 = Constraint(expr=   m.x561 - 2*m.x878 <= 0)

m.c876 = Constraint(expr=   m.x562 - 2*m.x879 <= 0)

m.c877 = Constraint(expr=   m.x563 - 2*m.x880 <= 0)

m.c878 = Constraint(expr=   m.x564 - 2*m.x881 <= 0)

m.c879 = Constraint(expr=   m.x565 - 2*m.x882 <= 0)

m.c880 = Constraint(expr=   m.x566 - 2*m.x883 <= 0)

m.c881 = Constraint(expr=   m.x567 - 2*m.x884 <= 0)

m.c882 = Constraint(expr=   m.x568 - 2*m.x885 <= 0)

m.c883 = Constraint(expr=   m.x569 - 2*m.x886 <= 0)

m.c884 = Constraint(expr=   m.x570 - 2*m.x887 <= 0)

m.c885 = Constraint(expr=   m.x571 - 2*m.x888 <= 0)

m.c886 = Constraint(expr=   m.x572 - 2*m.x889 <= 0)

m.c887 = Constraint(expr=   m.x573 - 2*m.x890 <= 0)

m.c888 = Constraint(expr=   m.x574 - 2*m.x891 <= 0)

m.c889 = Constraint(expr=   m.x575 - 2*m.x892 <= 0)

m.c890 = Constraint(expr=   m.x576 - 2*m.x893 <= 0)

m.c891 = Constraint(expr=   m.x577 - 2*m.x894 <= 0)

m.c892 = Constraint(expr=   m.x578 - 2*m.x895 <= 0)

m.c893 = Constraint(expr=   m.x579 - 2*m.x896 <= 0)

m.c894 = Constraint(expr=   m.x580 - 2*m.x897 <= 0)

m.c895 = Constraint(expr=   m.x581 - 2*m.x898 <= 0)

m.c896 = Constraint(expr=   m.x582 - 2*m.x899 <= 0)

m.c897 = Constraint(expr=   m.x583 - 2*m.x900 <= 0)

m.c898 = Constraint(expr=   m.x584 - 2*m.x901 <= 0)

m.c899 = Constraint(expr=   m.x585 - 2*m.x902 <= 0)

m.c900 = Constraint(expr=   m.x586 - 2*m.x903 <= 0)

m.c901 = Constraint(expr=   m.x587 - 2*m.x904 <= 0)

m.c902 = Constraint(expr=   m.x588 - 2*m.x905 <= 0)

m.c903 = Constraint(expr=   m.x589 - 2*m.x906 <= 0)

m.c904 = Constraint(expr=   m.x273 + 2*m.x590 >= 0)

m.c905 = Constraint(expr=   m.x274 + 2*m.x591 >= 0)

m.c906 = Constraint(expr=   m.x275 + 2*m.x592 >= 0)

m.c907 = Constraint(expr=   m.x276 + 2*m.x593 >= 0)

m.c908 = Constraint(expr=   m.x277 + 2*m.x594 >= 0)

m.c909 = Constraint(expr=   m.x278 + 2*m.x595 >= 0)

m.c910 = Constraint(expr=   m.x279 + 2*m.x596 >= 0)

m.c911 = Constraint(expr=   m.x280 + 2*m.x597 >= 0)

m.c912 = Constraint(expr=   m.x281 + 2*m.x598 >= 0)

m.c913 = Constraint(expr=   m.x282 + 2*m.x599 >= 0)

m.c914 = Constraint(expr=   m.x283 + 2*m.x600 >= 0)

m.c915 = Constraint(expr=   m.x284 + 2*m.x601 >= 0)

m.c916 = Constraint(expr=   m.x285 + 2*m.x602 >= 0)

m.c917 = Constraint(expr=   m.x286 + 2*m.x603 >= 0)

m.c918 = Constraint(expr=   m.x287 + 2*m.x604 >= 0)

m.c919 = Constraint(expr=   m.x288 + 2*m.x605 >= 0)

m.c920 = Constraint(expr=   m.x289 + 2*m.x606 >= 0)

m.c921 = Constraint(expr=   m.x290 + 2*m.x607 >= 0)

m.c922 = Constraint(expr=   m.x291 + 2*m.x608 >= 0)

m.c923 = Constraint(expr=   m.x292 + 2*m.x609 >= 0)

m.c924 = Constraint(expr=   m.x293 + 2*m.x610 >= 0)

m.c925 = Constraint(expr=   m.x294 + 2*m.x611 >= 0)

m.c926 = Constraint(expr=   m.x295 + 2*m.x612 >= 0)

m.c927 = Constraint(expr=   m.x296 + 2*m.x613 >= 0)

m.c928 = Constraint(expr=   m.x297 + 2*m.x614 >= 0)

m.c929 = Constraint(expr=   m.x298 + 2*m.x615 >= 0)

m.c930 = Constraint(expr=   m.x299 + 2*m.x616 >= 0)

m.c931 = Constraint(expr=   m.x300 + 2*m.x617 >= 0)

m.c932 = Constraint(expr=   m.x301 + 2*m.x618 >= 0)

m.c933 = Constraint(expr=   m.x302 + 2*m.x619 >= 0)

m.c934 = Constraint(expr=   m.x303 + 2*m.x620 >= 0)

m.c935 = Constraint(expr=   m.x304 + 2*m.x621 >= 0)

m.c936 = Constraint(expr=   m.x305 + 2*m.x622 >= 0)

m.c937 = Constraint(expr=   m.x306 + 2*m.x623 >= 0)

m.c938 = Constraint(expr=   m.x307 + 2*m.x624 >= 0)

m.c939 = Constraint(expr=   m.x308 + 2*m.x625 >= 0)

m.c940 = Constraint(expr=   m.x309 + 2*m.x626 >= 0)

m.c941 = Constraint(expr=   m.x310 + 2*m.x627 >= 0)

m.c942 = Constraint(expr=   m.x311 + 2*m.x628 >= 0)

m.c943 = Constraint(expr=   m.x312 + 2*m.x629 >= 0)

m.c944 = Constraint(expr=   m.x313 + 2*m.x630 >= 0)

m.c945 = Constraint(expr=   m.x314 + 2*m.x631 >= 0)

m.c946 = Constraint(expr=   m.x315 + 2*m.x632 >= 0)

m.c947 = Constraint(expr=   m.x316 + 2*m.x633 >= 0)

m.c948 = Constraint(expr=   m.x317 + 2*m.x634 >= 0)

m.c949 = Constraint(expr=   m.x318 + 2*m.x635 >= 0)

m.c950 = Constraint(expr=   m.x319 + 2*m.x636 >= 0)

m.c951 = Constraint(expr=   m.x320 + 2*m.x637 >= 0)

m.c952 = Constraint(expr=   m.x321 + 2*m.x638 >= 0)

m.c953 = Constraint(expr=   m.x322 + 2*m.x639 >= 0)

m.c954 = Constraint(expr=   m.x323 + 2*m.x640 >= 0)

m.c955 = Constraint(expr=   m.x324 + 2*m.x641 >= 0)

m.c956 = Constraint(expr=   m.x325 + 2*m.x642 >= 0)

m.c957 = Constraint(expr=   m.x326 + 2*m.x643 >= 0)

m.c958 = Constraint(expr=   m.x327 + 2*m.x644 >= 0)

m.c959 = Constraint(expr=   m.x328 + 2*m.x645 >= 0)

m.c960 = Constraint(expr=   m.x329 + 2*m.x646 >= 0)

m.c961 = Constraint(expr=   m.x330 + 2*m.x647 >= 0)

m.c962 = Constraint(expr=   m.x331 + 2*m.x648 >= 0)

m.c963 = Constraint(expr=   m.x332 + 2*m.x649 >= 0)

m.c964 = Constraint(expr=   m.x333 + 2*m.x650 >= 0)

m.c965 = Constraint(expr=   m.x334 + 2*m.x651 >= 0)

m.c966 = Constraint(expr=   m.x335 + 2*m.x652 >= 0)

m.c967 = Constraint(expr=   m.x336 + 2*m.x653 >= 0)

m.c968 = Constraint(expr=   m.x337 + 2*m.x654 >= 0)

m.c969 = Constraint(expr=   m.x338 + 2*m.x655 >= 0)

m.c970 = Constraint(expr=   m.x339 + 2*m.x656 >= 0)

m.c971 = Constraint(expr=   m.x340 + 2*m.x657 >= 0)

m.c972 = Constraint(expr=   m.x341 + 2*m.x658 >= 0)

m.c973 = Constraint(expr=   m.x342 + 2*m.x659 >= 0)

m.c974 = Constraint(expr=   m.x343 + 2*m.x660 >= 0)

m.c975 = Constraint(expr=   m.x344 + 2*m.x661 >= 0)

m.c976 = Constraint(expr=   m.x345 + 2*m.x662 >= 0)

m.c977 = Constraint(expr=   m.x346 + 2*m.x663 >= 0)

m.c978 = Constraint(expr=   m.x347 + 2*m.x664 >= 0)

m.c979 = Constraint(expr=   m.x348 + 2*m.x665 >= 0)

m.c980 = Constraint(expr=   m.x349 + 2*m.x666 >= 0)

m.c981 = Constraint(expr=   m.x350 + 2*m.x667 >= 0)

m.c982 = Constraint(expr=   m.x351 + 2*m.x668 >= 0)

m.c983 = Constraint(expr=   m.x352 + 2*m.x669 >= 0)

m.c984 = Constraint(expr=   m.x353 + 2*m.x670 >= 0)

m.c985 = Constraint(expr=   m.x354 + 2*m.x671 >= 0)

m.c986 = Constraint(expr=   m.x355 + 2*m.x672 >= 0)

m.c987 = Constraint(expr=   m.x356 + 2*m.x673 >= 0)

m.c988 = Constraint(expr=   m.x357 + 2*m.x674 >= 0)

m.c989 = Constraint(expr=   m.x358 + 2*m.x675 >= 0)

m.c990 = Constraint(expr=   m.x359 + 2*m.x676 >= 0)

m.c991 = Constraint(expr=   m.x360 + 2*m.x677 >= 0)

m.c992 = Constraint(expr=   m.x361 + 2*m.x678 >= 0)

m.c993 = Constraint(expr=   m.x362 + 2*m.x679 >= 0)

m.c994 = Constraint(expr=   m.x363 + 2*m.x680 >= 0)

m.c995 = Constraint(expr=   m.x364 + 2*m.x681 >= 0)

m.c996 = Constraint(expr=   m.x365 + 2*m.x682 >= 0)

m.c997 = Constraint(expr=   m.x366 + 2*m.x683 >= 0)

m.c998 = Constraint(expr=   m.x367 + 2*m.x684 >= 0)

m.c999 = Constraint(expr=   m.x368 + 2*m.x685 >= 0)

m.c1000 = Constraint(expr=   m.x369 + 2*m.x686 >= 0)

m.c1001 = Constraint(expr=   m.x370 + 2*m.x687 >= 0)

m.c1002 = Constraint(expr=   m.x371 + 2*m.x688 >= 0)

m.c1003 = Constraint(expr=   m.x372 + 2*m.x689 >= 0)

m.c1004 = Constraint(expr=   m.x373 + 2*m.x690 >= 0)

m.c1005 = Constraint(expr=   m.x374 + 2*m.x691 >= 0)

m.c1006 = Constraint(expr=   m.x375 + 2*m.x692 >= 0)

m.c1007 = Constraint(expr=   m.x376 + 2*m.x693 >= 0)

m.c1008 = Constraint(expr=   m.x377 + 2*m.x694 >= 0)

m.c1009 = Constraint(expr=   m.x378 + 2*m.x695 >= 0)

m.c1010 = Constraint(expr=   m.x379 + 2*m.x696 >= 0)

m.c1011 = Constraint(expr=   m.x380 + 2*m.x697 >= 0)

m.c1012 = Constraint(expr=   m.x381 + 2*m.x698 >= 0)

m.c1013 = Constraint(expr=   m.x382 + 2*m.x699 >= 0)

m.c1014 = Constraint(expr=   m.x383 + 2*m.x700 >= 0)

m.c1015 = Constraint(expr=   m.x384 + 2*m.x701 >= 0)

m.c1016 = Constraint(expr=   m.x385 + 2*m.x702 >= 0)

m.c1017 = Constraint(expr=   m.x386 + 2*m.x703 >= 0)

m.c1018 = Constraint(expr=   m.x387 + 2*m.x704 >= 0)

m.c1019 = Constraint(expr=   m.x388 + 2*m.x705 >= 0)

m.c1020 = Constraint(expr=   m.x389 + 2*m.x706 >= 0)

m.c1021 = Constraint(expr=   m.x390 + 2*m.x707 >= 0)

m.c1022 = Constraint(expr=   m.x391 + 2*m.x708 >= 0)

m.c1023 = Constraint(expr=   m.x392 + 2*m.x709 >= 0)

m.c1024 = Constraint(expr=   m.x393 + 2*m.x710 >= 0)

m.c1025 = Constraint(expr=   m.x394 + 2*m.x711 >= 0)

m.c1026 = Constraint(expr=   m.x395 + 2*m.x712 >= 0)

m.c1027 = Constraint(expr=   m.x396 + 2*m.x713 >= 0)

m.c1028 = Constraint(expr=   m.x397 + 2*m.x714 >= 0)

m.c1029 = Constraint(expr=   m.x398 + 2*m.x715 >= 0)

m.c1030 = Constraint(expr=   m.x399 + 2*m.x716 >= 0)

m.c1031 = Constraint(expr=   m.x400 + 2*m.x717 >= 0)

m.c1032 = Constraint(expr=   m.x401 + 2*m.x718 >= 0)

m.c1033 = Constraint(expr=   m.x402 + 2*m.x719 >= 0)

m.c1034 = Constraint(expr=   m.x403 + 2*m.x720 >= 0)

m.c1035 = Constraint(expr=   m.x404 + 2*m.x721 >= 0)

m.c1036 = Constraint(expr=   m.x405 + 2*m.x722 >= 0)

m.c1037 = Constraint(expr=   m.x406 + 2*m.x723 >= 0)

m.c1038 = Constraint(expr=   m.x407 + 2*m.x724 >= 0)

m.c1039 = Constraint(expr=   m.x408 + 2*m.x725 >= 0)

m.c1040 = Constraint(expr=   m.x409 + 2*m.x726 >= 0)

m.c1041 = Constraint(expr=   m.x410 + 2*m.x727 >= 0)

m.c1042 = Constraint(expr=   m.x411 + 2*m.x728 >= 0)

m.c1043 = Constraint(expr=   m.x412 + 2*m.x729 >= 0)

m.c1044 = Constraint(expr=   m.x413 + 2*m.x730 >= 0)

m.c1045 = Constraint(expr=   m.x414 + 2*m.x731 >= 0)

m.c1046 = Constraint(expr=   m.x415 + 2*m.x732 >= 0)

m.c1047 = Constraint(expr=   m.x416 + 2*m.x733 >= 0)

m.c1048 = Constraint(expr=   m.x417 + 2*m.x734 >= 0)

m.c1049 = Constraint(expr=   m.x418 + 2*m.x735 >= 0)

m.c1050 = Constraint(expr=   m.x419 + 2*m.x736 >= 0)

m.c1051 = Constraint(expr=   m.x420 + 2*m.x737 >= 0)

m.c1052 = Constraint(expr=   m.x421 + 2*m.x738 >= 0)

m.c1053 = Constraint(expr=   m.x422 + 2*m.x739 >= 0)

m.c1054 = Constraint(expr=   m.x423 + 2*m.x740 >= 0)

m.c1055 = Constraint(expr=   m.x424 + 2*m.x741 >= 0)

m.c1056 = Constraint(expr=   m.x425 + 2*m.x742 >= 0)

m.c1057 = Constraint(expr=   m.x426 + 2*m.x743 >= 0)

m.c1058 = Constraint(expr=   m.x427 + 2*m.x744 >= 0)

m.c1059 = Constraint(expr=   m.x428 + 2*m.x745 >= 0)

m.c1060 = Constraint(expr=   m.x429 + 2*m.x746 >= 0)

m.c1061 = Constraint(expr=   m.x430 + 2*m.x747 >= 0)

m.c1062 = Constraint(expr=   m.x431 + 2*m.x748 >= 0)

m.c1063 = Constraint(expr=   m.x432 + 2*m.x749 >= 0)

m.c1064 = Constraint(expr=   m.x433 + 2*m.x750 >= 0)

m.c1065 = Constraint(expr=   m.x434 + 2*m.x751 >= 0)

m.c1066 = Constraint(expr=   m.x435 + 2*m.x752 >= 0)

m.c1067 = Constraint(expr=   m.x436 + 2*m.x753 >= 0)

m.c1068 = Constraint(expr=   m.x437 + 2*m.x754 >= 0)

m.c1069 = Constraint(expr=   m.x438 + 2*m.x755 >= 0)

m.c1070 = Constraint(expr=   m.x439 + 2*m.x756 >= 0)

m.c1071 = Constraint(expr=   m.x440 + 2*m.x757 >= 0)

m.c1072 = Constraint(expr=   m.x441 + 2*m.x758 >= 0)

m.c1073 = Constraint(expr=   m.x442 + 2*m.x759 >= 0)

m.c1074 = Constraint(expr=   m.x443 + 2*m.x760 >= 0)

m.c1075 = Constraint(expr=   m.x444 + 2*m.x761 >= 0)

m.c1076 = Constraint(expr=   m.x445 + 2*m.x762 >= 0)

m.c1077 = Constraint(expr=   m.x446 + 2*m.x763 >= 0)

m.c1078 = Constraint(expr=   m.x447 + 2*m.x764 >= 0)

m.c1079 = Constraint(expr=   m.x448 + 2*m.x765 >= 0)

m.c1080 = Constraint(expr=   m.x449 + 2*m.x766 >= 0)

m.c1081 = Constraint(expr=   m.x450 + 2*m.x767 >= 0)

m.c1082 = Constraint(expr=   m.x451 + 2*m.x768 >= 0)

m.c1083 = Constraint(expr=   m.x452 + 2*m.x769 >= 0)

m.c1084 = Constraint(expr=   m.x453 + 2*m.x770 >= 0)

m.c1085 = Constraint(expr=   m.x454 + 2*m.x771 >= 0)

m.c1086 = Constraint(expr=   m.x455 + 2*m.x772 >= 0)

m.c1087 = Constraint(expr=   m.x456 + 2*m.x773 >= 0)

m.c1088 = Constraint(expr=   m.x457 + 2*m.x774 >= 0)

m.c1089 = Constraint(expr=   m.x458 + 2*m.x775 >= 0)

m.c1090 = Constraint(expr=   m.x459 + 2*m.x776 >= 0)

m.c1091 = Constraint(expr=   m.x460 + 2*m.x777 >= 0)

m.c1092 = Constraint(expr=   m.x461 + 2*m.x778 >= 0)

m.c1093 = Constraint(expr=   m.x462 + 2*m.x779 >= 0)

m.c1094 = Constraint(expr=   m.x463 + 2*m.x780 >= 0)

m.c1095 = Constraint(expr=   m.x464 + 2*m.x781 >= 0)

m.c1096 = Constraint(expr=   m.x465 + 2*m.x782 >= 0)

m.c1097 = Constraint(expr=   m.x466 + 2*m.x783 >= 0)

m.c1098 = Constraint(expr=   m.x467 + 2*m.x784 >= 0)

m.c1099 = Constraint(expr=   m.x468 + 2*m.x785 >= 0)

m.c1100 = Constraint(expr=   m.x469 + 2*m.x786 >= 0)

m.c1101 = Constraint(expr=   m.x470 + 2*m.x787 >= 0)

m.c1102 = Constraint(expr=   m.x471 + 2*m.x788 >= 0)

m.c1103 = Constraint(expr=   m.x472 + 2*m.x789 >= 0)

m.c1104 = Constraint(expr=   m.x473 + 2*m.x790 >= 0)

m.c1105 = Constraint(expr=   m.x474 + 2*m.x791 >= 0)

m.c1106 = Constraint(expr=   m.x475 + 2*m.x792 >= 0)

m.c1107 = Constraint(expr=   m.x476 + 2*m.x793 >= 0)

m.c1108 = Constraint(expr=   m.x477 + 2*m.x794 >= 0)

m.c1109 = Constraint(expr=   m.x478 + 2*m.x795 >= 0)

m.c1110 = Constraint(expr=   m.x479 + 2*m.x796 >= 0)

m.c1111 = Constraint(expr=   m.x480 + 2*m.x797 >= 0)

m.c1112 = Constraint(expr=   m.x481 + 2*m.x798 >= 0)

m.c1113 = Constraint(expr=   m.x482 + 2*m.x799 >= 0)

m.c1114 = Constraint(expr=   m.x483 + 2*m.x800 >= 0)

m.c1115 = Constraint(expr=   m.x484 + 2*m.x801 >= 0)

m.c1116 = Constraint(expr=   m.x485 + 2*m.x802 >= 0)

m.c1117 = Constraint(expr=   m.x486 + 2*m.x803 >= 0)

m.c1118 = Constraint(expr=   m.x487 + 2*m.x804 >= 0)

m.c1119 = Constraint(expr=   m.x488 + 2*m.x805 >= 0)

m.c1120 = Constraint(expr=   m.x489 + 2*m.x806 >= 0)

m.c1121 = Constraint(expr=   m.x490 + 2*m.x807 >= 0)

m.c1122 = Constraint(expr=   m.x491 + 2*m.x808 >= 0)

m.c1123 = Constraint(expr=   m.x492 + 2*m.x809 >= 0)

m.c1124 = Constraint(expr=   m.x493 + 2*m.x810 >= 0)

m.c1125 = Constraint(expr=   m.x494 + 2*m.x811 >= 0)

m.c1126 = Constraint(expr=   m.x495 + 2*m.x812 >= 0)

m.c1127 = Constraint(expr=   m.x496 + 2*m.x813 >= 0)

m.c1128 = Constraint(expr=   m.x497 + 2*m.x814 >= 0)

m.c1129 = Constraint(expr=   m.x498 + 2*m.x815 >= 0)

m.c1130 = Constraint(expr=   m.x499 + 2*m.x816 >= 0)

m.c1131 = Constraint(expr=   m.x500 + 2*m.x817 >= 0)

m.c1132 = Constraint(expr=   m.x501 + 2*m.x818 >= 0)

m.c1133 = Constraint(expr=   m.x502 + 2*m.x819 >= 0)

m.c1134 = Constraint(expr=   m.x503 + 2*m.x820 >= 0)

m.c1135 = Constraint(expr=   m.x504 + 2*m.x821 >= 0)

m.c1136 = Constraint(expr=   m.x505 + 2*m.x822 >= 0)

m.c1137 = Constraint(expr=   m.x506 + 2*m.x823 >= 0)

m.c1138 = Constraint(expr=   m.x507 + 2*m.x824 >= 0)

m.c1139 = Constraint(expr=   m.x508 + 2*m.x825 >= 0)

m.c1140 = Constraint(expr=   m.x509 + 2*m.x826 >= 0)

m.c1141 = Constraint(expr=   m.x510 + 2*m.x827 >= 0)

m.c1142 = Constraint(expr=   m.x511 + 2*m.x828 >= 0)

m.c1143 = Constraint(expr=   m.x512 + 2*m.x829 >= 0)

m.c1144 = Constraint(expr=   m.x513 + 2*m.x830 >= 0)

m.c1145 = Constraint(expr=   m.x514 + 2*m.x831 >= 0)

m.c1146 = Constraint(expr=   m.x515 + 2*m.x832 >= 0)

m.c1147 = Constraint(expr=   m.x516 + 2*m.x833 >= 0)

m.c1148 = Constraint(expr=   m.x517 + 2*m.x834 >= 0)

m.c1149 = Constraint(expr=   m.x518 + 2*m.x835 >= 0)

m.c1150 = Constraint(expr=   m.x519 + 2*m.x836 >= 0)

m.c1151 = Constraint(expr=   m.x520 + 2*m.x837 >= 0)

m.c1152 = Constraint(expr=   m.x521 + 2*m.x838 >= 0)

m.c1153 = Constraint(expr=   m.x522 + 2*m.x839 >= 0)

m.c1154 = Constraint(expr=   m.x523 + 2*m.x840 >= 0)

m.c1155 = Constraint(expr=   m.x524 + 2*m.x841 >= 0)

m.c1156 = Constraint(expr=   m.x525 + 2*m.x842 >= 0)

m.c1157 = Constraint(expr=   m.x526 + 2*m.x843 >= 0)

m.c1158 = Constraint(expr=   m.x527 + 2*m.x844 >= 0)

m.c1159 = Constraint(expr=   m.x528 + 2*m.x845 >= 0)

m.c1160 = Constraint(expr=   m.x529 + 2*m.x846 >= 0)

m.c1161 = Constraint(expr=   m.x530 + 2*m.x847 >= 0)

m.c1162 = Constraint(expr=   m.x531 + 2*m.x848 >= 0)

m.c1163 = Constraint(expr=   m.x532 + 2*m.x849 >= 0)

m.c1164 = Constraint(expr=   m.x533 + 2*m.x850 >= 0)

m.c1165 = Constraint(expr=   m.x534 + 2*m.x851 >= 0)

m.c1166 = Constraint(expr=   m.x535 + 2*m.x852 >= 0)

m.c1167 = Constraint(expr=   m.x536 + 2*m.x853 >= 0)

m.c1168 = Constraint(expr=   m.x537 + 2*m.x854 >= 0)

m.c1169 = Constraint(expr=   m.x538 + 2*m.x855 >= 0)

m.c1170 = Constraint(expr=   m.x539 + 2*m.x856 >= 0)

m.c1171 = Constraint(expr=   m.x540 + 2*m.x857 >= 0)

m.c1172 = Constraint(expr=   m.x541 + 2*m.x858 >= 0)

m.c1173 = Constraint(expr=   m.x542 + 2*m.x859 >= 0)

m.c1174 = Constraint(expr=   m.x543 + 2*m.x860 >= 0)

m.c1175 = Constraint(expr=   m.x544 + 2*m.x861 >= 0)

m.c1176 = Constraint(expr=   m.x545 + 2*m.x862 >= 0)

m.c1177 = Constraint(expr=   m.x546 + 2*m.x863 >= 0)

m.c1178 = Constraint(expr=   m.x547 + 2*m.x864 >= 0)

m.c1179 = Constraint(expr=   m.x548 + 2*m.x865 >= 0)

m.c1180 = Constraint(expr=   m.x549 + 2*m.x866 >= 0)

m.c1181 = Constraint(expr=   m.x550 + 2*m.x867 >= 0)

m.c1182 = Constraint(expr=   m.x551 + 2*m.x868 >= 0)

m.c1183 = Constraint(expr=   m.x552 + 2*m.x869 >= 0)

m.c1184 = Constraint(expr=   m.x553 + 2*m.x870 >= 0)

m.c1185 = Constraint(expr=   m.x554 + 2*m.x871 >= 0)

m.c1186 = Constraint(expr=   m.x555 + 2*m.x872 >= 0)

m.c1187 = Constraint(expr=   m.x556 + 2*m.x873 >= 0)

m.c1188 = Constraint(expr=   m.x557 + 2*m.x874 >= 0)

m.c1189 = Constraint(expr=   m.x558 + 2*m.x875 >= 0)

m.c1190 = Constraint(expr=   m.x559 + 2*m.x876 >= 0)

m.c1191 = Constraint(expr=   m.x560 + 2*m.x877 >= 0)

m.c1192 = Constraint(expr=   m.x561 + 2*m.x878 >= 0)

m.c1193 = Constraint(expr=   m.x562 + 2*m.x879 >= 0)

m.c1194 = Constraint(expr=   m.x563 + 2*m.x880 >= 0)

m.c1195 = Constraint(expr=   m.x564 + 2*m.x881 >= 0)

m.c1196 = Constraint(expr=   m.x565 + 2*m.x882 >= 0)

m.c1197 = Constraint(expr=   m.x566 + 2*m.x883 >= 0)

m.c1198 = Constraint(expr=   m.x567 + 2*m.x884 >= 0)

m.c1199 = Constraint(expr=   m.x568 + 2*m.x885 >= 0)

m.c1200 = Constraint(expr=   m.x569 + 2*m.x886 >= 0)

m.c1201 = Constraint(expr=   m.x570 + 2*m.x887 >= 0)

m.c1202 = Constraint(expr=   m.x571 + 2*m.x888 >= 0)

m.c1203 = Constraint(expr=   m.x572 + 2*m.x889 >= 0)

m.c1204 = Constraint(expr=   m.x573 + 2*m.x890 >= 0)

m.c1205 = Constraint(expr=   m.x574 + 2*m.x891 >= 0)

m.c1206 = Constraint(expr=   m.x575 + 2*m.x892 >= 0)

m.c1207 = Constraint(expr=   m.x576 + 2*m.x893 >= 0)

m.c1208 = Constraint(expr=   m.x577 + 2*m.x894 >= 0)

m.c1209 = Constraint(expr=   m.x578 + 2*m.x895 >= 0)

m.c1210 = Constraint(expr=   m.x579 + 2*m.x896 >= 0)

m.c1211 = Constraint(expr=   m.x580 + 2*m.x897 >= 0)

m.c1212 = Constraint(expr=   m.x581 + 2*m.x898 >= 0)

m.c1213 = Constraint(expr=   m.x582 + 2*m.x899 >= 0)

m.c1214 = Constraint(expr=   m.x583 + 2*m.x900 >= 0)

m.c1215 = Constraint(expr=   m.x584 + 2*m.x901 >= 0)

m.c1216 = Constraint(expr=   m.x585 + 2*m.x902 >= 0)

m.c1217 = Constraint(expr=   m.x586 + 2*m.x903 >= 0)

m.c1218 = Constraint(expr=   m.x587 + 2*m.x904 >= 0)

m.c1219 = Constraint(expr=   m.x588 + 2*m.x905 >= 0)

m.c1220 = Constraint(expr=   m.x589 + 2*m.x906 >= 0)

m.c1221 = Constraint(expr=   m.x590 - 0.00785398163397448*m.b907 - 0.0122718463030851*m.b908 - 0.0176714586764426*m.b909
                           - 0.0314159265358979*m.b910 - 0.0490873852123405*m.b911 - 0.0706858347057703*m.b912
                           - 0.0962112750161874*m.b913 - 0.125663706143592*m.b914 - 0.159043128087983*m.b915
                           - 0.196349540849362*m.b916 - 0.282743338823081*m.b917 - 0.38484510006475*m.b918
                           - 0.502654824574367*m.b919 == 0)

m.c1222 = Constraint(expr=   m.x591 - 0.00785398163397448*m.b920 - 0.0122718463030851*m.b921 - 0.0176714586764426*m.b922
                           - 0.0314159265358979*m.b923 - 0.0490873852123405*m.b924 - 0.0706858347057703*m.b925
                           - 0.0962112750161874*m.b926 - 0.125663706143592*m.b927 - 0.159043128087983*m.b928
                           - 0.196349540849362*m.b929 - 0.282743338823081*m.b930 - 0.38484510006475*m.b931
                           - 0.502654824574367*m.b932 == 0)

m.c1223 = Constraint(expr=   m.x592 - 0.00785398163397448*m.b933 - 0.0122718463030851*m.b934 - 0.0176714586764426*m.b935
                           - 0.0314159265358979*m.b936 - 0.0490873852123405*m.b937 - 0.0706858347057703*m.b938
                           - 0.0962112750161874*m.b939 - 0.125663706143592*m.b940 - 0.159043128087983*m.b941
                           - 0.196349540849362*m.b942 - 0.282743338823081*m.b943 - 0.38484510006475*m.b944
                           - 0.502654824574367*m.b945 == 0)

m.c1224 = Constraint(expr=   m.x593 - 0.00785398163397448*m.b946 - 0.0122718463030851*m.b947 - 0.0176714586764426*m.b948
                           - 0.0314159265358979*m.b949 - 0.0490873852123405*m.b950 - 0.0706858347057703*m.b951
                           - 0.0962112750161874*m.b952 - 0.125663706143592*m.b953 - 0.159043128087983*m.b954
                           - 0.196349540849362*m.b955 - 0.282743338823081*m.b956 - 0.38484510006475*m.b957
                           - 0.502654824574367*m.b958 == 0)

m.c1225 = Constraint(expr=   m.x594 - 0.00785398163397448*m.b959 - 0.0122718463030851*m.b960 - 0.0176714586764426*m.b961
                           - 0.0314159265358979*m.b962 - 0.0490873852123405*m.b963 - 0.0706858347057703*m.b964
                           - 0.0962112750161874*m.b965 - 0.125663706143592*m.b966 - 0.159043128087983*m.b967
                           - 0.196349540849362*m.b968 - 0.282743338823081*m.b969 - 0.38484510006475*m.b970
                           - 0.502654824574367*m.b971 == 0)

m.c1226 = Constraint(expr=   m.x595 - 0.00785398163397448*m.b972 - 0.0122718463030851*m.b973 - 0.0176714586764426*m.b974
                           - 0.0314159265358979*m.b975 - 0.0490873852123405*m.b976 - 0.0706858347057703*m.b977
                           - 0.0962112750161874*m.b978 - 0.125663706143592*m.b979 - 0.159043128087983*m.b980
                           - 0.196349540849362*m.b981 - 0.282743338823081*m.b982 - 0.38484510006475*m.b983
                           - 0.502654824574367*m.b984 == 0)

m.c1227 = Constraint(expr=   m.x596 - 0.00785398163397448*m.b985 - 0.0122718463030851*m.b986 - 0.0176714586764426*m.b987
                           - 0.0314159265358979*m.b988 - 0.0490873852123405*m.b989 - 0.0706858347057703*m.b990
                           - 0.0962112750161874*m.b991 - 0.125663706143592*m.b992 - 0.159043128087983*m.b993
                           - 0.196349540849362*m.b994 - 0.282743338823081*m.b995 - 0.38484510006475*m.b996
                           - 0.502654824574367*m.b997 == 0)

m.c1228 = Constraint(expr=   m.x597 - 0.00785398163397448*m.b998 - 0.0122718463030851*m.b999
                           - 0.0176714586764426*m.b1000 - 0.0314159265358979*m.b1001 - 0.0490873852123405*m.b1002
                           - 0.0706858347057703*m.b1003 - 0.0962112750161874*m.b1004 - 0.125663706143592*m.b1005
                           - 0.159043128087983*m.b1006 - 0.196349540849362*m.b1007 - 0.282743338823081*m.b1008
                           - 0.38484510006475*m.b1009 - 0.502654824574367*m.b1010 == 0)

m.c1229 = Constraint(expr=   m.x598 - 0.00785398163397448*m.b1011 - 0.0122718463030851*m.b1012
                           - 0.0176714586764426*m.b1013 - 0.0314159265358979*m.b1014 - 0.0490873852123405*m.b1015
                           - 0.0706858347057703*m.b1016 - 0.0962112750161874*m.b1017 - 0.125663706143592*m.b1018
                           - 0.159043128087983*m.b1019 - 0.196349540849362*m.b1020 - 0.282743338823081*m.b1021
                           - 0.38484510006475*m.b1022 - 0.502654824574367*m.b1023 == 0)

m.c1230 = Constraint(expr=   m.x599 - 0.00785398163397448*m.b1024 - 0.0122718463030851*m.b1025
                           - 0.0176714586764426*m.b1026 - 0.0314159265358979*m.b1027 - 0.0490873852123405*m.b1028
                           - 0.0706858347057703*m.b1029 - 0.0962112750161874*m.b1030 - 0.125663706143592*m.b1031
                           - 0.159043128087983*m.b1032 - 0.196349540849362*m.b1033 - 0.282743338823081*m.b1034
                           - 0.38484510006475*m.b1035 - 0.502654824574367*m.b1036 == 0)

m.c1231 = Constraint(expr=   m.x600 - 0.00785398163397448*m.b1037 - 0.0122718463030851*m.b1038
                           - 0.0176714586764426*m.b1039 - 0.0314159265358979*m.b1040 - 0.0490873852123405*m.b1041
                           - 0.0706858347057703*m.b1042 - 0.0962112750161874*m.b1043 - 0.125663706143592*m.b1044
                           - 0.159043128087983*m.b1045 - 0.196349540849362*m.b1046 - 0.282743338823081*m.b1047
                           - 0.38484510006475*m.b1048 - 0.502654824574367*m.b1049 == 0)

m.c1232 = Constraint(expr=   m.x601 - 0.00785398163397448*m.b1050 - 0.0122718463030851*m.b1051
                           - 0.0176714586764426*m.b1052 - 0.0314159265358979*m.b1053 - 0.0490873852123405*m.b1054
                           - 0.0706858347057703*m.b1055 - 0.0962112750161874*m.b1056 - 0.125663706143592*m.b1057
                           - 0.159043128087983*m.b1058 - 0.196349540849362*m.b1059 - 0.282743338823081*m.b1060
                           - 0.38484510006475*m.b1061 - 0.502654824574367*m.b1062 == 0)

m.c1233 = Constraint(expr=   m.x602 - 0.00785398163397448*m.b1063 - 0.0122718463030851*m.b1064
                           - 0.0176714586764426*m.b1065 - 0.0314159265358979*m.b1066 - 0.0490873852123405*m.b1067
                           - 0.0706858347057703*m.b1068 - 0.0962112750161874*m.b1069 - 0.125663706143592*m.b1070
                           - 0.159043128087983*m.b1071 - 0.196349540849362*m.b1072 - 0.282743338823081*m.b1073
                           - 0.38484510006475*m.b1074 - 0.502654824574367*m.b1075 == 0)

m.c1234 = Constraint(expr=   m.x603 - 0.00785398163397448*m.b1076 - 0.0122718463030851*m.b1077
                           - 0.0176714586764426*m.b1078 - 0.0314159265358979*m.b1079 - 0.0490873852123405*m.b1080
                           - 0.0706858347057703*m.b1081 - 0.0962112750161874*m.b1082 - 0.125663706143592*m.b1083
                           - 0.159043128087983*m.b1084 - 0.196349540849362*m.b1085 - 0.282743338823081*m.b1086
                           - 0.38484510006475*m.b1087 - 0.502654824574367*m.b1088 == 0)

m.c1235 = Constraint(expr=   m.x604 - 0.00785398163397448*m.b1089 - 0.0122718463030851*m.b1090
                           - 0.0176714586764426*m.b1091 - 0.0314159265358979*m.b1092 - 0.0490873852123405*m.b1093
                           - 0.0706858347057703*m.b1094 - 0.0962112750161874*m.b1095 - 0.125663706143592*m.b1096
                           - 0.159043128087983*m.b1097 - 0.196349540849362*m.b1098 - 0.282743338823081*m.b1099
                           - 0.38484510006475*m.b1100 - 0.502654824574367*m.b1101 == 0)

m.c1236 = Constraint(expr=   m.x605 - 0.00785398163397448*m.b1102 - 0.0122718463030851*m.b1103
                           - 0.0176714586764426*m.b1104 - 0.0314159265358979*m.b1105 - 0.0490873852123405*m.b1106
                           - 0.0706858347057703*m.b1107 - 0.0962112750161874*m.b1108 - 0.125663706143592*m.b1109
                           - 0.159043128087983*m.b1110 - 0.196349540849362*m.b1111 - 0.282743338823081*m.b1112
                           - 0.38484510006475*m.b1113 - 0.502654824574367*m.b1114 == 0)

m.c1237 = Constraint(expr=   m.x606 - 0.00785398163397448*m.b1115 - 0.0122718463030851*m.b1116
                           - 0.0176714586764426*m.b1117 - 0.0314159265358979*m.b1118 - 0.0490873852123405*m.b1119
                           - 0.0706858347057703*m.b1120 - 0.0962112750161874*m.b1121 - 0.125663706143592*m.b1122
                           - 0.159043128087983*m.b1123 - 0.196349540849362*m.b1124 - 0.282743338823081*m.b1125
                           - 0.38484510006475*m.b1126 - 0.502654824574367*m.b1127 == 0)

m.c1238 = Constraint(expr=   m.x607 - 0.00785398163397448*m.b1128 - 0.0122718463030851*m.b1129
                           - 0.0176714586764426*m.b1130 - 0.0314159265358979*m.b1131 - 0.0490873852123405*m.b1132
                           - 0.0706858347057703*m.b1133 - 0.0962112750161874*m.b1134 - 0.125663706143592*m.b1135
                           - 0.159043128087983*m.b1136 - 0.196349540849362*m.b1137 - 0.282743338823081*m.b1138
                           - 0.38484510006475*m.b1139 - 0.502654824574367*m.b1140 == 0)

m.c1239 = Constraint(expr=   m.x608 - 0.00785398163397448*m.b1141 - 0.0122718463030851*m.b1142
                           - 0.0176714586764426*m.b1143 - 0.0314159265358979*m.b1144 - 0.0490873852123405*m.b1145
                           - 0.0706858347057703*m.b1146 - 0.0962112750161874*m.b1147 - 0.125663706143592*m.b1148
                           - 0.159043128087983*m.b1149 - 0.196349540849362*m.b1150 - 0.282743338823081*m.b1151
                           - 0.38484510006475*m.b1152 - 0.502654824574367*m.b1153 == 0)

m.c1240 = Constraint(expr=   m.x609 - 0.00785398163397448*m.b1154 - 0.0122718463030851*m.b1155
                           - 0.0176714586764426*m.b1156 - 0.0314159265358979*m.b1157 - 0.0490873852123405*m.b1158
                           - 0.0706858347057703*m.b1159 - 0.0962112750161874*m.b1160 - 0.125663706143592*m.b1161
                           - 0.159043128087983*m.b1162 - 0.196349540849362*m.b1163 - 0.282743338823081*m.b1164
                           - 0.38484510006475*m.b1165 - 0.502654824574367*m.b1166 == 0)

m.c1241 = Constraint(expr=   m.x610 - 0.00785398163397448*m.b1167 - 0.0122718463030851*m.b1168
                           - 0.0176714586764426*m.b1169 - 0.0314159265358979*m.b1170 - 0.0490873852123405*m.b1171
                           - 0.0706858347057703*m.b1172 - 0.0962112750161874*m.b1173 - 0.125663706143592*m.b1174
                           - 0.159043128087983*m.b1175 - 0.196349540849362*m.b1176 - 0.282743338823081*m.b1177
                           - 0.38484510006475*m.b1178 - 0.502654824574367*m.b1179 == 0)

m.c1242 = Constraint(expr=   m.x611 - 0.00785398163397448*m.b1180 - 0.0122718463030851*m.b1181
                           - 0.0176714586764426*m.b1182 - 0.0314159265358979*m.b1183 - 0.0490873852123405*m.b1184
                           - 0.0706858347057703*m.b1185 - 0.0962112750161874*m.b1186 - 0.125663706143592*m.b1187
                           - 0.159043128087983*m.b1188 - 0.196349540849362*m.b1189 - 0.282743338823081*m.b1190
                           - 0.38484510006475*m.b1191 - 0.502654824574367*m.b1192 == 0)

m.c1243 = Constraint(expr=   m.x612 - 0.00785398163397448*m.b1193 - 0.0122718463030851*m.b1194
                           - 0.0176714586764426*m.b1195 - 0.0314159265358979*m.b1196 - 0.0490873852123405*m.b1197
                           - 0.0706858347057703*m.b1198 - 0.0962112750161874*m.b1199 - 0.125663706143592*m.b1200
                           - 0.159043128087983*m.b1201 - 0.196349540849362*m.b1202 - 0.282743338823081*m.b1203
                           - 0.38484510006475*m.b1204 - 0.502654824574367*m.b1205 == 0)

m.c1244 = Constraint(expr=   m.x613 - 0.00785398163397448*m.b1206 - 0.0122718463030851*m.b1207
                           - 0.0176714586764426*m.b1208 - 0.0314159265358979*m.b1209 - 0.0490873852123405*m.b1210
                           - 0.0706858347057703*m.b1211 - 0.0962112750161874*m.b1212 - 0.125663706143592*m.b1213
                           - 0.159043128087983*m.b1214 - 0.196349540849362*m.b1215 - 0.282743338823081*m.b1216
                           - 0.38484510006475*m.b1217 - 0.502654824574367*m.b1218 == 0)

m.c1245 = Constraint(expr=   m.x614 - 0.00785398163397448*m.b1219 - 0.0122718463030851*m.b1220
                           - 0.0176714586764426*m.b1221 - 0.0314159265358979*m.b1222 - 0.0490873852123405*m.b1223
                           - 0.0706858347057703*m.b1224 - 0.0962112750161874*m.b1225 - 0.125663706143592*m.b1226
                           - 0.159043128087983*m.b1227 - 0.196349540849362*m.b1228 - 0.282743338823081*m.b1229
                           - 0.38484510006475*m.b1230 - 0.502654824574367*m.b1231 == 0)

m.c1246 = Constraint(expr=   m.x615 - 0.00785398163397448*m.b1232 - 0.0122718463030851*m.b1233
                           - 0.0176714586764426*m.b1234 - 0.0314159265358979*m.b1235 - 0.0490873852123405*m.b1236
                           - 0.0706858347057703*m.b1237 - 0.0962112750161874*m.b1238 - 0.125663706143592*m.b1239
                           - 0.159043128087983*m.b1240 - 0.196349540849362*m.b1241 - 0.282743338823081*m.b1242
                           - 0.38484510006475*m.b1243 - 0.502654824574367*m.b1244 == 0)

m.c1247 = Constraint(expr=   m.x616 - 0.00785398163397448*m.b1245 - 0.0122718463030851*m.b1246
                           - 0.0176714586764426*m.b1247 - 0.0314159265358979*m.b1248 - 0.0490873852123405*m.b1249
                           - 0.0706858347057703*m.b1250 - 0.0962112750161874*m.b1251 - 0.125663706143592*m.b1252
                           - 0.159043128087983*m.b1253 - 0.196349540849362*m.b1254 - 0.282743338823081*m.b1255
                           - 0.38484510006475*m.b1256 - 0.502654824574367*m.b1257 == 0)

m.c1248 = Constraint(expr=   m.x617 - 0.00785398163397448*m.b1258 - 0.0122718463030851*m.b1259
                           - 0.0176714586764426*m.b1260 - 0.0314159265358979*m.b1261 - 0.0490873852123405*m.b1262
                           - 0.0706858347057703*m.b1263 - 0.0962112750161874*m.b1264 - 0.125663706143592*m.b1265
                           - 0.159043128087983*m.b1266 - 0.196349540849362*m.b1267 - 0.282743338823081*m.b1268
                           - 0.38484510006475*m.b1269 - 0.502654824574367*m.b1270 == 0)

m.c1249 = Constraint(expr=   m.x618 - 0.00785398163397448*m.b1271 - 0.0122718463030851*m.b1272
                           - 0.0176714586764426*m.b1273 - 0.0314159265358979*m.b1274 - 0.0490873852123405*m.b1275
                           - 0.0706858347057703*m.b1276 - 0.0962112750161874*m.b1277 - 0.125663706143592*m.b1278
                           - 0.159043128087983*m.b1279 - 0.196349540849362*m.b1280 - 0.282743338823081*m.b1281
                           - 0.38484510006475*m.b1282 - 0.502654824574367*m.b1283 == 0)

m.c1250 = Constraint(expr=   m.x619 - 0.00785398163397448*m.b1284 - 0.0122718463030851*m.b1285
                           - 0.0176714586764426*m.b1286 - 0.0314159265358979*m.b1287 - 0.0490873852123405*m.b1288
                           - 0.0706858347057703*m.b1289 - 0.0962112750161874*m.b1290 - 0.125663706143592*m.b1291
                           - 0.159043128087983*m.b1292 - 0.196349540849362*m.b1293 - 0.282743338823081*m.b1294
                           - 0.38484510006475*m.b1295 - 0.502654824574367*m.b1296 == 0)

m.c1251 = Constraint(expr=   m.x620 - 0.00785398163397448*m.b1297 - 0.0122718463030851*m.b1298
                           - 0.0176714586764426*m.b1299 - 0.0314159265358979*m.b1300 - 0.0490873852123405*m.b1301
                           - 0.0706858347057703*m.b1302 - 0.0962112750161874*m.b1303 - 0.125663706143592*m.b1304
                           - 0.159043128087983*m.b1305 - 0.196349540849362*m.b1306 - 0.282743338823081*m.b1307
                           - 0.38484510006475*m.b1308 - 0.502654824574367*m.b1309 == 0)

m.c1252 = Constraint(expr=   m.x621 - 0.00785398163397448*m.b1310 - 0.0122718463030851*m.b1311
                           - 0.0176714586764426*m.b1312 - 0.0314159265358979*m.b1313 - 0.0490873852123405*m.b1314
                           - 0.0706858347057703*m.b1315 - 0.0962112750161874*m.b1316 - 0.125663706143592*m.b1317
                           - 0.159043128087983*m.b1318 - 0.196349540849362*m.b1319 - 0.282743338823081*m.b1320
                           - 0.38484510006475*m.b1321 - 0.502654824574367*m.b1322 == 0)

m.c1253 = Constraint(expr=   m.x622 - 0.00785398163397448*m.b1323 - 0.0122718463030851*m.b1324
                           - 0.0176714586764426*m.b1325 - 0.0314159265358979*m.b1326 - 0.0490873852123405*m.b1327
                           - 0.0706858347057703*m.b1328 - 0.0962112750161874*m.b1329 - 0.125663706143592*m.b1330
                           - 0.159043128087983*m.b1331 - 0.196349540849362*m.b1332 - 0.282743338823081*m.b1333
                           - 0.38484510006475*m.b1334 - 0.502654824574367*m.b1335 == 0)

m.c1254 = Constraint(expr=   m.x623 - 0.00785398163397448*m.b1336 - 0.0122718463030851*m.b1337
                           - 0.0176714586764426*m.b1338 - 0.0314159265358979*m.b1339 - 0.0490873852123405*m.b1340
                           - 0.0706858347057703*m.b1341 - 0.0962112750161874*m.b1342 - 0.125663706143592*m.b1343
                           - 0.159043128087983*m.b1344 - 0.196349540849362*m.b1345 - 0.282743338823081*m.b1346
                           - 0.38484510006475*m.b1347 - 0.502654824574367*m.b1348 == 0)

m.c1255 = Constraint(expr=   m.x624 - 0.00785398163397448*m.b1349 - 0.0122718463030851*m.b1350
                           - 0.0176714586764426*m.b1351 - 0.0314159265358979*m.b1352 - 0.0490873852123405*m.b1353
                           - 0.0706858347057703*m.b1354 - 0.0962112750161874*m.b1355 - 0.125663706143592*m.b1356
                           - 0.159043128087983*m.b1357 - 0.196349540849362*m.b1358 - 0.282743338823081*m.b1359
                           - 0.38484510006475*m.b1360 - 0.502654824574367*m.b1361 == 0)

m.c1256 = Constraint(expr=   m.x625 - 0.00785398163397448*m.b1362 - 0.0122718463030851*m.b1363
                           - 0.0176714586764426*m.b1364 - 0.0314159265358979*m.b1365 - 0.0490873852123405*m.b1366
                           - 0.0706858347057703*m.b1367 - 0.0962112750161874*m.b1368 - 0.125663706143592*m.b1369
                           - 0.159043128087983*m.b1370 - 0.196349540849362*m.b1371 - 0.282743338823081*m.b1372
                           - 0.38484510006475*m.b1373 - 0.502654824574367*m.b1374 == 0)

m.c1257 = Constraint(expr=   m.x626 - 0.00785398163397448*m.b1375 - 0.0122718463030851*m.b1376
                           - 0.0176714586764426*m.b1377 - 0.0314159265358979*m.b1378 - 0.0490873852123405*m.b1379
                           - 0.0706858347057703*m.b1380 - 0.0962112750161874*m.b1381 - 0.125663706143592*m.b1382
                           - 0.159043128087983*m.b1383 - 0.196349540849362*m.b1384 - 0.282743338823081*m.b1385
                           - 0.38484510006475*m.b1386 - 0.502654824574367*m.b1387 == 0)

m.c1258 = Constraint(expr=   m.x627 - 0.00785398163397448*m.b1388 - 0.0122718463030851*m.b1389
                           - 0.0176714586764426*m.b1390 - 0.0314159265358979*m.b1391 - 0.0490873852123405*m.b1392
                           - 0.0706858347057703*m.b1393 - 0.0962112750161874*m.b1394 - 0.125663706143592*m.b1395
                           - 0.159043128087983*m.b1396 - 0.196349540849362*m.b1397 - 0.282743338823081*m.b1398
                           - 0.38484510006475*m.b1399 - 0.502654824574367*m.b1400 == 0)

m.c1259 = Constraint(expr=   m.x628 - 0.00785398163397448*m.b1401 - 0.0122718463030851*m.b1402
                           - 0.0176714586764426*m.b1403 - 0.0314159265358979*m.b1404 - 0.0490873852123405*m.b1405
                           - 0.0706858347057703*m.b1406 - 0.0962112750161874*m.b1407 - 0.125663706143592*m.b1408
                           - 0.159043128087983*m.b1409 - 0.196349540849362*m.b1410 - 0.282743338823081*m.b1411
                           - 0.38484510006475*m.b1412 - 0.502654824574367*m.b1413 == 0)

m.c1260 = Constraint(expr=   m.x629 - 0.00785398163397448*m.b1414 - 0.0122718463030851*m.b1415
                           - 0.0176714586764426*m.b1416 - 0.0314159265358979*m.b1417 - 0.0490873852123405*m.b1418
                           - 0.0706858347057703*m.b1419 - 0.0962112750161874*m.b1420 - 0.125663706143592*m.b1421
                           - 0.159043128087983*m.b1422 - 0.196349540849362*m.b1423 - 0.282743338823081*m.b1424
                           - 0.38484510006475*m.b1425 - 0.502654824574367*m.b1426 == 0)

m.c1261 = Constraint(expr=   m.x630 - 0.00785398163397448*m.b1427 - 0.0122718463030851*m.b1428
                           - 0.0176714586764426*m.b1429 - 0.0314159265358979*m.b1430 - 0.0490873852123405*m.b1431
                           - 0.0706858347057703*m.b1432 - 0.0962112750161874*m.b1433 - 0.125663706143592*m.b1434
                           - 0.159043128087983*m.b1435 - 0.196349540849362*m.b1436 - 0.282743338823081*m.b1437
                           - 0.38484510006475*m.b1438 - 0.502654824574367*m.b1439 == 0)

m.c1262 = Constraint(expr=   m.x631 - 0.00785398163397448*m.b1440 - 0.0122718463030851*m.b1441
                           - 0.0176714586764426*m.b1442 - 0.0314159265358979*m.b1443 - 0.0490873852123405*m.b1444
                           - 0.0706858347057703*m.b1445 - 0.0962112750161874*m.b1446 - 0.125663706143592*m.b1447
                           - 0.159043128087983*m.b1448 - 0.196349540849362*m.b1449 - 0.282743338823081*m.b1450
                           - 0.38484510006475*m.b1451 - 0.502654824574367*m.b1452 == 0)

m.c1263 = Constraint(expr=   m.x632 - 0.00785398163397448*m.b1453 - 0.0122718463030851*m.b1454
                           - 0.0176714586764426*m.b1455 - 0.0314159265358979*m.b1456 - 0.0490873852123405*m.b1457
                           - 0.0706858347057703*m.b1458 - 0.0962112750161874*m.b1459 - 0.125663706143592*m.b1460
                           - 0.159043128087983*m.b1461 - 0.196349540849362*m.b1462 - 0.282743338823081*m.b1463
                           - 0.38484510006475*m.b1464 - 0.502654824574367*m.b1465 == 0)

m.c1264 = Constraint(expr=   m.x633 - 0.00785398163397448*m.b1466 - 0.0122718463030851*m.b1467
                           - 0.0176714586764426*m.b1468 - 0.0314159265358979*m.b1469 - 0.0490873852123405*m.b1470
                           - 0.0706858347057703*m.b1471 - 0.0962112750161874*m.b1472 - 0.125663706143592*m.b1473
                           - 0.159043128087983*m.b1474 - 0.196349540849362*m.b1475 - 0.282743338823081*m.b1476
                           - 0.38484510006475*m.b1477 - 0.502654824574367*m.b1478 == 0)

m.c1265 = Constraint(expr=   m.x634 - 0.00785398163397448*m.b1479 - 0.0122718463030851*m.b1480
                           - 0.0176714586764426*m.b1481 - 0.0314159265358979*m.b1482 - 0.0490873852123405*m.b1483
                           - 0.0706858347057703*m.b1484 - 0.0962112750161874*m.b1485 - 0.125663706143592*m.b1486
                           - 0.159043128087983*m.b1487 - 0.196349540849362*m.b1488 - 0.282743338823081*m.b1489
                           - 0.38484510006475*m.b1490 - 0.502654824574367*m.b1491 == 0)

m.c1266 = Constraint(expr=   m.x635 - 0.00785398163397448*m.b1492 - 0.0122718463030851*m.b1493
                           - 0.0176714586764426*m.b1494 - 0.0314159265358979*m.b1495 - 0.0490873852123405*m.b1496
                           - 0.0706858347057703*m.b1497 - 0.0962112750161874*m.b1498 - 0.125663706143592*m.b1499
                           - 0.159043128087983*m.b1500 - 0.196349540849362*m.b1501 - 0.282743338823081*m.b1502
                           - 0.38484510006475*m.b1503 - 0.502654824574367*m.b1504 == 0)

m.c1267 = Constraint(expr=   m.x636 - 0.00785398163397448*m.b1505 - 0.0122718463030851*m.b1506
                           - 0.0176714586764426*m.b1507 - 0.0314159265358979*m.b1508 - 0.0490873852123405*m.b1509
                           - 0.0706858347057703*m.b1510 - 0.0962112750161874*m.b1511 - 0.125663706143592*m.b1512
                           - 0.159043128087983*m.b1513 - 0.196349540849362*m.b1514 - 0.282743338823081*m.b1515
                           - 0.38484510006475*m.b1516 - 0.502654824574367*m.b1517 == 0)

m.c1268 = Constraint(expr=   m.x637 - 0.00785398163397448*m.b1518 - 0.0122718463030851*m.b1519
                           - 0.0176714586764426*m.b1520 - 0.0314159265358979*m.b1521 - 0.0490873852123405*m.b1522
                           - 0.0706858347057703*m.b1523 - 0.0962112750161874*m.b1524 - 0.125663706143592*m.b1525
                           - 0.159043128087983*m.b1526 - 0.196349540849362*m.b1527 - 0.282743338823081*m.b1528
                           - 0.38484510006475*m.b1529 - 0.502654824574367*m.b1530 == 0)

m.c1269 = Constraint(expr=   m.x638 - 0.00785398163397448*m.b1531 - 0.0122718463030851*m.b1532
                           - 0.0176714586764426*m.b1533 - 0.0314159265358979*m.b1534 - 0.0490873852123405*m.b1535
                           - 0.0706858347057703*m.b1536 - 0.0962112750161874*m.b1537 - 0.125663706143592*m.b1538
                           - 0.159043128087983*m.b1539 - 0.196349540849362*m.b1540 - 0.282743338823081*m.b1541
                           - 0.38484510006475*m.b1542 - 0.502654824574367*m.b1543 == 0)

m.c1270 = Constraint(expr=   m.x639 - 0.00785398163397448*m.b1544 - 0.0122718463030851*m.b1545
                           - 0.0176714586764426*m.b1546 - 0.0314159265358979*m.b1547 - 0.0490873852123405*m.b1548
                           - 0.0706858347057703*m.b1549 - 0.0962112750161874*m.b1550 - 0.125663706143592*m.b1551
                           - 0.159043128087983*m.b1552 - 0.196349540849362*m.b1553 - 0.282743338823081*m.b1554
                           - 0.38484510006475*m.b1555 - 0.502654824574367*m.b1556 == 0)

m.c1271 = Constraint(expr=   m.x640 - 0.00785398163397448*m.b1557 - 0.0122718463030851*m.b1558
                           - 0.0176714586764426*m.b1559 - 0.0314159265358979*m.b1560 - 0.0490873852123405*m.b1561
                           - 0.0706858347057703*m.b1562 - 0.0962112750161874*m.b1563 - 0.125663706143592*m.b1564
                           - 0.159043128087983*m.b1565 - 0.196349540849362*m.b1566 - 0.282743338823081*m.b1567
                           - 0.38484510006475*m.b1568 - 0.502654824574367*m.b1569 == 0)

m.c1272 = Constraint(expr=   m.x641 - 0.00785398163397448*m.b1570 - 0.0122718463030851*m.b1571
                           - 0.0176714586764426*m.b1572 - 0.0314159265358979*m.b1573 - 0.0490873852123405*m.b1574
                           - 0.0706858347057703*m.b1575 - 0.0962112750161874*m.b1576 - 0.125663706143592*m.b1577
                           - 0.159043128087983*m.b1578 - 0.196349540849362*m.b1579 - 0.282743338823081*m.b1580
                           - 0.38484510006475*m.b1581 - 0.502654824574367*m.b1582 == 0)

m.c1273 = Constraint(expr=   m.x642 - 0.00785398163397448*m.b1583 - 0.0122718463030851*m.b1584
                           - 0.0176714586764426*m.b1585 - 0.0314159265358979*m.b1586 - 0.0490873852123405*m.b1587
                           - 0.0706858347057703*m.b1588 - 0.0962112750161874*m.b1589 - 0.125663706143592*m.b1590
                           - 0.159043128087983*m.b1591 - 0.196349540849362*m.b1592 - 0.282743338823081*m.b1593
                           - 0.38484510006475*m.b1594 - 0.502654824574367*m.b1595 == 0)

m.c1274 = Constraint(expr=   m.x643 - 0.00785398163397448*m.b1596 - 0.0122718463030851*m.b1597
                           - 0.0176714586764426*m.b1598 - 0.0314159265358979*m.b1599 - 0.0490873852123405*m.b1600
                           - 0.0706858347057703*m.b1601 - 0.0962112750161874*m.b1602 - 0.125663706143592*m.b1603
                           - 0.159043128087983*m.b1604 - 0.196349540849362*m.b1605 - 0.282743338823081*m.b1606
                           - 0.38484510006475*m.b1607 - 0.502654824574367*m.b1608 == 0)

m.c1275 = Constraint(expr=   m.x644 - 0.00785398163397448*m.b1609 - 0.0122718463030851*m.b1610
                           - 0.0176714586764426*m.b1611 - 0.0314159265358979*m.b1612 - 0.0490873852123405*m.b1613
                           - 0.0706858347057703*m.b1614 - 0.0962112750161874*m.b1615 - 0.125663706143592*m.b1616
                           - 0.159043128087983*m.b1617 - 0.196349540849362*m.b1618 - 0.282743338823081*m.b1619
                           - 0.38484510006475*m.b1620 - 0.502654824574367*m.b1621 == 0)

m.c1276 = Constraint(expr=   m.x645 - 0.00785398163397448*m.b1622 - 0.0122718463030851*m.b1623
                           - 0.0176714586764426*m.b1624 - 0.0314159265358979*m.b1625 - 0.0490873852123405*m.b1626
                           - 0.0706858347057703*m.b1627 - 0.0962112750161874*m.b1628 - 0.125663706143592*m.b1629
                           - 0.159043128087983*m.b1630 - 0.196349540849362*m.b1631 - 0.282743338823081*m.b1632
                           - 0.38484510006475*m.b1633 - 0.502654824574367*m.b1634 == 0)

m.c1277 = Constraint(expr=   m.x646 - 0.00785398163397448*m.b1635 - 0.0122718463030851*m.b1636
                           - 0.0176714586764426*m.b1637 - 0.0314159265358979*m.b1638 - 0.0490873852123405*m.b1639
                           - 0.0706858347057703*m.b1640 - 0.0962112750161874*m.b1641 - 0.125663706143592*m.b1642
                           - 0.159043128087983*m.b1643 - 0.196349540849362*m.b1644 - 0.282743338823081*m.b1645
                           - 0.38484510006475*m.b1646 - 0.502654824574367*m.b1647 == 0)

m.c1278 = Constraint(expr=   m.x647 - 0.00785398163397448*m.b1648 - 0.0122718463030851*m.b1649
                           - 0.0176714586764426*m.b1650 - 0.0314159265358979*m.b1651 - 0.0490873852123405*m.b1652
                           - 0.0706858347057703*m.b1653 - 0.0962112750161874*m.b1654 - 0.125663706143592*m.b1655
                           - 0.159043128087983*m.b1656 - 0.196349540849362*m.b1657 - 0.282743338823081*m.b1658
                           - 0.38484510006475*m.b1659 - 0.502654824574367*m.b1660 == 0)

m.c1279 = Constraint(expr=   m.x648 - 0.00785398163397448*m.b1661 - 0.0122718463030851*m.b1662
                           - 0.0176714586764426*m.b1663 - 0.0314159265358979*m.b1664 - 0.0490873852123405*m.b1665
                           - 0.0706858347057703*m.b1666 - 0.0962112750161874*m.b1667 - 0.125663706143592*m.b1668
                           - 0.159043128087983*m.b1669 - 0.196349540849362*m.b1670 - 0.282743338823081*m.b1671
                           - 0.38484510006475*m.b1672 - 0.502654824574367*m.b1673 == 0)

m.c1280 = Constraint(expr=   m.x649 - 0.00785398163397448*m.b1674 - 0.0122718463030851*m.b1675
                           - 0.0176714586764426*m.b1676 - 0.0314159265358979*m.b1677 - 0.0490873852123405*m.b1678
                           - 0.0706858347057703*m.b1679 - 0.0962112750161874*m.b1680 - 0.125663706143592*m.b1681
                           - 0.159043128087983*m.b1682 - 0.196349540849362*m.b1683 - 0.282743338823081*m.b1684
                           - 0.38484510006475*m.b1685 - 0.502654824574367*m.b1686 == 0)

m.c1281 = Constraint(expr=   m.x650 - 0.00785398163397448*m.b1687 - 0.0122718463030851*m.b1688
                           - 0.0176714586764426*m.b1689 - 0.0314159265358979*m.b1690 - 0.0490873852123405*m.b1691
                           - 0.0706858347057703*m.b1692 - 0.0962112750161874*m.b1693 - 0.125663706143592*m.b1694
                           - 0.159043128087983*m.b1695 - 0.196349540849362*m.b1696 - 0.282743338823081*m.b1697
                           - 0.38484510006475*m.b1698 - 0.502654824574367*m.b1699 == 0)

m.c1282 = Constraint(expr=   m.x651 - 0.00785398163397448*m.b1700 - 0.0122718463030851*m.b1701
                           - 0.0176714586764426*m.b1702 - 0.0314159265358979*m.b1703 - 0.0490873852123405*m.b1704
                           - 0.0706858347057703*m.b1705 - 0.0962112750161874*m.b1706 - 0.125663706143592*m.b1707
                           - 0.159043128087983*m.b1708 - 0.196349540849362*m.b1709 - 0.282743338823081*m.b1710
                           - 0.38484510006475*m.b1711 - 0.502654824574367*m.b1712 == 0)

m.c1283 = Constraint(expr=   m.x652 - 0.00785398163397448*m.b1713 - 0.0122718463030851*m.b1714
                           - 0.0176714586764426*m.b1715 - 0.0314159265358979*m.b1716 - 0.0490873852123405*m.b1717
                           - 0.0706858347057703*m.b1718 - 0.0962112750161874*m.b1719 - 0.125663706143592*m.b1720
                           - 0.159043128087983*m.b1721 - 0.196349540849362*m.b1722 - 0.282743338823081*m.b1723
                           - 0.38484510006475*m.b1724 - 0.502654824574367*m.b1725 == 0)

m.c1284 = Constraint(expr=   m.x653 - 0.00785398163397448*m.b1726 - 0.0122718463030851*m.b1727
                           - 0.0176714586764426*m.b1728 - 0.0314159265358979*m.b1729 - 0.0490873852123405*m.b1730
                           - 0.0706858347057703*m.b1731 - 0.0962112750161874*m.b1732 - 0.125663706143592*m.b1733
                           - 0.159043128087983*m.b1734 - 0.196349540849362*m.b1735 - 0.282743338823081*m.b1736
                           - 0.38484510006475*m.b1737 - 0.502654824574367*m.b1738 == 0)

m.c1285 = Constraint(expr=   m.x654 - 0.00785398163397448*m.b1739 - 0.0122718463030851*m.b1740
                           - 0.0176714586764426*m.b1741 - 0.0314159265358979*m.b1742 - 0.0490873852123405*m.b1743
                           - 0.0706858347057703*m.b1744 - 0.0962112750161874*m.b1745 - 0.125663706143592*m.b1746
                           - 0.159043128087983*m.b1747 - 0.196349540849362*m.b1748 - 0.282743338823081*m.b1749
                           - 0.38484510006475*m.b1750 - 0.502654824574367*m.b1751 == 0)

m.c1286 = Constraint(expr=   m.x655 - 0.00785398163397448*m.b1752 - 0.0122718463030851*m.b1753
                           - 0.0176714586764426*m.b1754 - 0.0314159265358979*m.b1755 - 0.0490873852123405*m.b1756
                           - 0.0706858347057703*m.b1757 - 0.0962112750161874*m.b1758 - 0.125663706143592*m.b1759
                           - 0.159043128087983*m.b1760 - 0.196349540849362*m.b1761 - 0.282743338823081*m.b1762
                           - 0.38484510006475*m.b1763 - 0.502654824574367*m.b1764 == 0)

m.c1287 = Constraint(expr=   m.x656 - 0.00785398163397448*m.b1765 - 0.0122718463030851*m.b1766
                           - 0.0176714586764426*m.b1767 - 0.0314159265358979*m.b1768 - 0.0490873852123405*m.b1769
                           - 0.0706858347057703*m.b1770 - 0.0962112750161874*m.b1771 - 0.125663706143592*m.b1772
                           - 0.159043128087983*m.b1773 - 0.196349540849362*m.b1774 - 0.282743338823081*m.b1775
                           - 0.38484510006475*m.b1776 - 0.502654824574367*m.b1777 == 0)

m.c1288 = Constraint(expr=   m.x657 - 0.00785398163397448*m.b1778 - 0.0122718463030851*m.b1779
                           - 0.0176714586764426*m.b1780 - 0.0314159265358979*m.b1781 - 0.0490873852123405*m.b1782
                           - 0.0706858347057703*m.b1783 - 0.0962112750161874*m.b1784 - 0.125663706143592*m.b1785
                           - 0.159043128087983*m.b1786 - 0.196349540849362*m.b1787 - 0.282743338823081*m.b1788
                           - 0.38484510006475*m.b1789 - 0.502654824574367*m.b1790 == 0)

m.c1289 = Constraint(expr=   m.x658 - 0.00785398163397448*m.b1791 - 0.0122718463030851*m.b1792
                           - 0.0176714586764426*m.b1793 - 0.0314159265358979*m.b1794 - 0.0490873852123405*m.b1795
                           - 0.0706858347057703*m.b1796 - 0.0962112750161874*m.b1797 - 0.125663706143592*m.b1798
                           - 0.159043128087983*m.b1799 - 0.196349540849362*m.b1800 - 0.282743338823081*m.b1801
                           - 0.38484510006475*m.b1802 - 0.502654824574367*m.b1803 == 0)

m.c1290 = Constraint(expr=   m.x659 - 0.00785398163397448*m.b1804 - 0.0122718463030851*m.b1805
                           - 0.0176714586764426*m.b1806 - 0.0314159265358979*m.b1807 - 0.0490873852123405*m.b1808
                           - 0.0706858347057703*m.b1809 - 0.0962112750161874*m.b1810 - 0.125663706143592*m.b1811
                           - 0.159043128087983*m.b1812 - 0.196349540849362*m.b1813 - 0.282743338823081*m.b1814
                           - 0.38484510006475*m.b1815 - 0.502654824574367*m.b1816 == 0)

m.c1291 = Constraint(expr=   m.x660 - 0.00785398163397448*m.b1817 - 0.0122718463030851*m.b1818
                           - 0.0176714586764426*m.b1819 - 0.0314159265358979*m.b1820 - 0.0490873852123405*m.b1821
                           - 0.0706858347057703*m.b1822 - 0.0962112750161874*m.b1823 - 0.125663706143592*m.b1824
                           - 0.159043128087983*m.b1825 - 0.196349540849362*m.b1826 - 0.282743338823081*m.b1827
                           - 0.38484510006475*m.b1828 - 0.502654824574367*m.b1829 == 0)

m.c1292 = Constraint(expr=   m.x661 - 0.00785398163397448*m.b1830 - 0.0122718463030851*m.b1831
                           - 0.0176714586764426*m.b1832 - 0.0314159265358979*m.b1833 - 0.0490873852123405*m.b1834
                           - 0.0706858347057703*m.b1835 - 0.0962112750161874*m.b1836 - 0.125663706143592*m.b1837
                           - 0.159043128087983*m.b1838 - 0.196349540849362*m.b1839 - 0.282743338823081*m.b1840
                           - 0.38484510006475*m.b1841 - 0.502654824574367*m.b1842 == 0)

m.c1293 = Constraint(expr=   m.x662 - 0.00785398163397448*m.b1843 - 0.0122718463030851*m.b1844
                           - 0.0176714586764426*m.b1845 - 0.0314159265358979*m.b1846 - 0.0490873852123405*m.b1847
                           - 0.0706858347057703*m.b1848 - 0.0962112750161874*m.b1849 - 0.125663706143592*m.b1850
                           - 0.159043128087983*m.b1851 - 0.196349540849362*m.b1852 - 0.282743338823081*m.b1853
                           - 0.38484510006475*m.b1854 - 0.502654824574367*m.b1855 == 0)

m.c1294 = Constraint(expr=   m.x663 - 0.00785398163397448*m.b1856 - 0.0122718463030851*m.b1857
                           - 0.0176714586764426*m.b1858 - 0.0314159265358979*m.b1859 - 0.0490873852123405*m.b1860
                           - 0.0706858347057703*m.b1861 - 0.0962112750161874*m.b1862 - 0.125663706143592*m.b1863
                           - 0.159043128087983*m.b1864 - 0.196349540849362*m.b1865 - 0.282743338823081*m.b1866
                           - 0.38484510006475*m.b1867 - 0.502654824574367*m.b1868 == 0)

m.c1295 = Constraint(expr=   m.x664 - 0.00785398163397448*m.b1869 - 0.0122718463030851*m.b1870
                           - 0.0176714586764426*m.b1871 - 0.0314159265358979*m.b1872 - 0.0490873852123405*m.b1873
                           - 0.0706858347057703*m.b1874 - 0.0962112750161874*m.b1875 - 0.125663706143592*m.b1876
                           - 0.159043128087983*m.b1877 - 0.196349540849362*m.b1878 - 0.282743338823081*m.b1879
                           - 0.38484510006475*m.b1880 - 0.502654824574367*m.b1881 == 0)

m.c1296 = Constraint(expr=   m.x665 - 0.00785398163397448*m.b1882 - 0.0122718463030851*m.b1883
                           - 0.0176714586764426*m.b1884 - 0.0314159265358979*m.b1885 - 0.0490873852123405*m.b1886
                           - 0.0706858347057703*m.b1887 - 0.0962112750161874*m.b1888 - 0.125663706143592*m.b1889
                           - 0.159043128087983*m.b1890 - 0.196349540849362*m.b1891 - 0.282743338823081*m.b1892
                           - 0.38484510006475*m.b1893 - 0.502654824574367*m.b1894 == 0)

m.c1297 = Constraint(expr=   m.x666 - 0.00785398163397448*m.b1895 - 0.0122718463030851*m.b1896
                           - 0.0176714586764426*m.b1897 - 0.0314159265358979*m.b1898 - 0.0490873852123405*m.b1899
                           - 0.0706858347057703*m.b1900 - 0.0962112750161874*m.b1901 - 0.125663706143592*m.b1902
                           - 0.159043128087983*m.b1903 - 0.196349540849362*m.b1904 - 0.282743338823081*m.b1905
                           - 0.38484510006475*m.b1906 - 0.502654824574367*m.b1907 == 0)

m.c1298 = Constraint(expr=   m.x667 - 0.00785398163397448*m.b1908 - 0.0122718463030851*m.b1909
                           - 0.0176714586764426*m.b1910 - 0.0314159265358979*m.b1911 - 0.0490873852123405*m.b1912
                           - 0.0706858347057703*m.b1913 - 0.0962112750161874*m.b1914 - 0.125663706143592*m.b1915
                           - 0.159043128087983*m.b1916 - 0.196349540849362*m.b1917 - 0.282743338823081*m.b1918
                           - 0.38484510006475*m.b1919 - 0.502654824574367*m.b1920 == 0)

m.c1299 = Constraint(expr=   m.x668 - 0.00785398163397448*m.b1921 - 0.0122718463030851*m.b1922
                           - 0.0176714586764426*m.b1923 - 0.0314159265358979*m.b1924 - 0.0490873852123405*m.b1925
                           - 0.0706858347057703*m.b1926 - 0.0962112750161874*m.b1927 - 0.125663706143592*m.b1928
                           - 0.159043128087983*m.b1929 - 0.196349540849362*m.b1930 - 0.282743338823081*m.b1931
                           - 0.38484510006475*m.b1932 - 0.502654824574367*m.b1933 == 0)

m.c1300 = Constraint(expr=   m.x669 - 0.00785398163397448*m.b1934 - 0.0122718463030851*m.b1935
                           - 0.0176714586764426*m.b1936 - 0.0314159265358979*m.b1937 - 0.0490873852123405*m.b1938
                           - 0.0706858347057703*m.b1939 - 0.0962112750161874*m.b1940 - 0.125663706143592*m.b1941
                           - 0.159043128087983*m.b1942 - 0.196349540849362*m.b1943 - 0.282743338823081*m.b1944
                           - 0.38484510006475*m.b1945 - 0.502654824574367*m.b1946 == 0)

m.c1301 = Constraint(expr=   m.x670 - 0.00785398163397448*m.b1947 - 0.0122718463030851*m.b1948
                           - 0.0176714586764426*m.b1949 - 0.0314159265358979*m.b1950 - 0.0490873852123405*m.b1951
                           - 0.0706858347057703*m.b1952 - 0.0962112750161874*m.b1953 - 0.125663706143592*m.b1954
                           - 0.159043128087983*m.b1955 - 0.196349540849362*m.b1956 - 0.282743338823081*m.b1957
                           - 0.38484510006475*m.b1958 - 0.502654824574367*m.b1959 == 0)

m.c1302 = Constraint(expr=   m.x671 - 0.00785398163397448*m.b1960 - 0.0122718463030851*m.b1961
                           - 0.0176714586764426*m.b1962 - 0.0314159265358979*m.b1963 - 0.0490873852123405*m.b1964
                           - 0.0706858347057703*m.b1965 - 0.0962112750161874*m.b1966 - 0.125663706143592*m.b1967
                           - 0.159043128087983*m.b1968 - 0.196349540849362*m.b1969 - 0.282743338823081*m.b1970
                           - 0.38484510006475*m.b1971 - 0.502654824574367*m.b1972 == 0)

m.c1303 = Constraint(expr=   m.x672 - 0.00785398163397448*m.b1973 - 0.0122718463030851*m.b1974
                           - 0.0176714586764426*m.b1975 - 0.0314159265358979*m.b1976 - 0.0490873852123405*m.b1977
                           - 0.0706858347057703*m.b1978 - 0.0962112750161874*m.b1979 - 0.125663706143592*m.b1980
                           - 0.159043128087983*m.b1981 - 0.196349540849362*m.b1982 - 0.282743338823081*m.b1983
                           - 0.38484510006475*m.b1984 - 0.502654824574367*m.b1985 == 0)

m.c1304 = Constraint(expr=   m.x673 - 0.00785398163397448*m.b1986 - 0.0122718463030851*m.b1987
                           - 0.0176714586764426*m.b1988 - 0.0314159265358979*m.b1989 - 0.0490873852123405*m.b1990
                           - 0.0706858347057703*m.b1991 - 0.0962112750161874*m.b1992 - 0.125663706143592*m.b1993
                           - 0.159043128087983*m.b1994 - 0.196349540849362*m.b1995 - 0.282743338823081*m.b1996
                           - 0.38484510006475*m.b1997 - 0.502654824574367*m.b1998 == 0)

m.c1305 = Constraint(expr=   m.x674 - 0.00785398163397448*m.b1999 - 0.0122718463030851*m.b2000
                           - 0.0176714586764426*m.b2001 - 0.0314159265358979*m.b2002 - 0.0490873852123405*m.b2003
                           - 0.0706858347057703*m.b2004 - 0.0962112750161874*m.b2005 - 0.125663706143592*m.b2006
                           - 0.159043128087983*m.b2007 - 0.196349540849362*m.b2008 - 0.282743338823081*m.b2009
                           - 0.38484510006475*m.b2010 - 0.502654824574367*m.b2011 == 0)

m.c1306 = Constraint(expr=   m.x675 - 0.00785398163397448*m.b2012 - 0.0122718463030851*m.b2013
                           - 0.0176714586764426*m.b2014 - 0.0314159265358979*m.b2015 - 0.0490873852123405*m.b2016
                           - 0.0706858347057703*m.b2017 - 0.0962112750161874*m.b2018 - 0.125663706143592*m.b2019
                           - 0.159043128087983*m.b2020 - 0.196349540849362*m.b2021 - 0.282743338823081*m.b2022
                           - 0.38484510006475*m.b2023 - 0.502654824574367*m.b2024 == 0)

m.c1307 = Constraint(expr=   m.x676 - 0.00785398163397448*m.b2025 - 0.0122718463030851*m.b2026
                           - 0.0176714586764426*m.b2027 - 0.0314159265358979*m.b2028 - 0.0490873852123405*m.b2029
                           - 0.0706858347057703*m.b2030 - 0.0962112750161874*m.b2031 - 0.125663706143592*m.b2032
                           - 0.159043128087983*m.b2033 - 0.196349540849362*m.b2034 - 0.282743338823081*m.b2035
                           - 0.38484510006475*m.b2036 - 0.502654824574367*m.b2037 == 0)

m.c1308 = Constraint(expr=   m.x677 - 0.00785398163397448*m.b2038 - 0.0122718463030851*m.b2039
                           - 0.0176714586764426*m.b2040 - 0.0314159265358979*m.b2041 - 0.0490873852123405*m.b2042
                           - 0.0706858347057703*m.b2043 - 0.0962112750161874*m.b2044 - 0.125663706143592*m.b2045
                           - 0.159043128087983*m.b2046 - 0.196349540849362*m.b2047 - 0.282743338823081*m.b2048
                           - 0.38484510006475*m.b2049 - 0.502654824574367*m.b2050 == 0)

m.c1309 = Constraint(expr=   m.x678 - 0.00785398163397448*m.b2051 - 0.0122718463030851*m.b2052
                           - 0.0176714586764426*m.b2053 - 0.0314159265358979*m.b2054 - 0.0490873852123405*m.b2055
                           - 0.0706858347057703*m.b2056 - 0.0962112750161874*m.b2057 - 0.125663706143592*m.b2058
                           - 0.159043128087983*m.b2059 - 0.196349540849362*m.b2060 - 0.282743338823081*m.b2061
                           - 0.38484510006475*m.b2062 - 0.502654824574367*m.b2063 == 0)

m.c1310 = Constraint(expr=   m.x679 - 0.00785398163397448*m.b2064 - 0.0122718463030851*m.b2065
                           - 0.0176714586764426*m.b2066 - 0.0314159265358979*m.b2067 - 0.0490873852123405*m.b2068
                           - 0.0706858347057703*m.b2069 - 0.0962112750161874*m.b2070 - 0.125663706143592*m.b2071
                           - 0.159043128087983*m.b2072 - 0.196349540849362*m.b2073 - 0.282743338823081*m.b2074
                           - 0.38484510006475*m.b2075 - 0.502654824574367*m.b2076 == 0)

m.c1311 = Constraint(expr=   m.x680 - 0.00785398163397448*m.b2077 - 0.0122718463030851*m.b2078
                           - 0.0176714586764426*m.b2079 - 0.0314159265358979*m.b2080 - 0.0490873852123405*m.b2081
                           - 0.0706858347057703*m.b2082 - 0.0962112750161874*m.b2083 - 0.125663706143592*m.b2084
                           - 0.159043128087983*m.b2085 - 0.196349540849362*m.b2086 - 0.282743338823081*m.b2087
                           - 0.38484510006475*m.b2088 - 0.502654824574367*m.b2089 == 0)

m.c1312 = Constraint(expr=   m.x681 - 0.00785398163397448*m.b2090 - 0.0122718463030851*m.b2091
                           - 0.0176714586764426*m.b2092 - 0.0314159265358979*m.b2093 - 0.0490873852123405*m.b2094
                           - 0.0706858347057703*m.b2095 - 0.0962112750161874*m.b2096 - 0.125663706143592*m.b2097
                           - 0.159043128087983*m.b2098 - 0.196349540849362*m.b2099 - 0.282743338823081*m.b2100
                           - 0.38484510006475*m.b2101 - 0.502654824574367*m.b2102 == 0)

m.c1313 = Constraint(expr=   m.x682 - 0.00785398163397448*m.b2103 - 0.0122718463030851*m.b2104
                           - 0.0176714586764426*m.b2105 - 0.0314159265358979*m.b2106 - 0.0490873852123405*m.b2107
                           - 0.0706858347057703*m.b2108 - 0.0962112750161874*m.b2109 - 0.125663706143592*m.b2110
                           - 0.159043128087983*m.b2111 - 0.196349540849362*m.b2112 - 0.282743338823081*m.b2113
                           - 0.38484510006475*m.b2114 - 0.502654824574367*m.b2115 == 0)

m.c1314 = Constraint(expr=   m.x683 - 0.00785398163397448*m.b2116 - 0.0122718463030851*m.b2117
                           - 0.0176714586764426*m.b2118 - 0.0314159265358979*m.b2119 - 0.0490873852123405*m.b2120
                           - 0.0706858347057703*m.b2121 - 0.0962112750161874*m.b2122 - 0.125663706143592*m.b2123
                           - 0.159043128087983*m.b2124 - 0.196349540849362*m.b2125 - 0.282743338823081*m.b2126
                           - 0.38484510006475*m.b2127 - 0.502654824574367*m.b2128 == 0)

m.c1315 = Constraint(expr=   m.x684 - 0.00785398163397448*m.b2129 - 0.0122718463030851*m.b2130
                           - 0.0176714586764426*m.b2131 - 0.0314159265358979*m.b2132 - 0.0490873852123405*m.b2133
                           - 0.0706858347057703*m.b2134 - 0.0962112750161874*m.b2135 - 0.125663706143592*m.b2136
                           - 0.159043128087983*m.b2137 - 0.196349540849362*m.b2138 - 0.282743338823081*m.b2139
                           - 0.38484510006475*m.b2140 - 0.502654824574367*m.b2141 == 0)

m.c1316 = Constraint(expr=   m.x685 - 0.00785398163397448*m.b2142 - 0.0122718463030851*m.b2143
                           - 0.0176714586764426*m.b2144 - 0.0314159265358979*m.b2145 - 0.0490873852123405*m.b2146
                           - 0.0706858347057703*m.b2147 - 0.0962112750161874*m.b2148 - 0.125663706143592*m.b2149
                           - 0.159043128087983*m.b2150 - 0.196349540849362*m.b2151 - 0.282743338823081*m.b2152
                           - 0.38484510006475*m.b2153 - 0.502654824574367*m.b2154 == 0)

m.c1317 = Constraint(expr=   m.x686 - 0.00785398163397448*m.b2155 - 0.0122718463030851*m.b2156
                           - 0.0176714586764426*m.b2157 - 0.0314159265358979*m.b2158 - 0.0490873852123405*m.b2159
                           - 0.0706858347057703*m.b2160 - 0.0962112750161874*m.b2161 - 0.125663706143592*m.b2162
                           - 0.159043128087983*m.b2163 - 0.196349540849362*m.b2164 - 0.282743338823081*m.b2165
                           - 0.38484510006475*m.b2166 - 0.502654824574367*m.b2167 == 0)

m.c1318 = Constraint(expr=   m.x687 - 0.00785398163397448*m.b2168 - 0.0122718463030851*m.b2169
                           - 0.0176714586764426*m.b2170 - 0.0314159265358979*m.b2171 - 0.0490873852123405*m.b2172
                           - 0.0706858347057703*m.b2173 - 0.0962112750161874*m.b2174 - 0.125663706143592*m.b2175
                           - 0.159043128087983*m.b2176 - 0.196349540849362*m.b2177 - 0.282743338823081*m.b2178
                           - 0.38484510006475*m.b2179 - 0.502654824574367*m.b2180 == 0)

m.c1319 = Constraint(expr=   m.x688 - 0.00785398163397448*m.b2181 - 0.0122718463030851*m.b2182
                           - 0.0176714586764426*m.b2183 - 0.0314159265358979*m.b2184 - 0.0490873852123405*m.b2185
                           - 0.0706858347057703*m.b2186 - 0.0962112750161874*m.b2187 - 0.125663706143592*m.b2188
                           - 0.159043128087983*m.b2189 - 0.196349540849362*m.b2190 - 0.282743338823081*m.b2191
                           - 0.38484510006475*m.b2192 - 0.502654824574367*m.b2193 == 0)

m.c1320 = Constraint(expr=   m.x689 - 0.00785398163397448*m.b2194 - 0.0122718463030851*m.b2195
                           - 0.0176714586764426*m.b2196 - 0.0314159265358979*m.b2197 - 0.0490873852123405*m.b2198
                           - 0.0706858347057703*m.b2199 - 0.0962112750161874*m.b2200 - 0.125663706143592*m.b2201
                           - 0.159043128087983*m.b2202 - 0.196349540849362*m.b2203 - 0.282743338823081*m.b2204
                           - 0.38484510006475*m.b2205 - 0.502654824574367*m.b2206 == 0)

m.c1321 = Constraint(expr=   m.x690 - 0.00785398163397448*m.b2207 - 0.0122718463030851*m.b2208
                           - 0.0176714586764426*m.b2209 - 0.0314159265358979*m.b2210 - 0.0490873852123405*m.b2211
                           - 0.0706858347057703*m.b2212 - 0.0962112750161874*m.b2213 - 0.125663706143592*m.b2214
                           - 0.159043128087983*m.b2215 - 0.196349540849362*m.b2216 - 0.282743338823081*m.b2217
                           - 0.38484510006475*m.b2218 - 0.502654824574367*m.b2219 == 0)

m.c1322 = Constraint(expr=   m.x691 - 0.00785398163397448*m.b2220 - 0.0122718463030851*m.b2221
                           - 0.0176714586764426*m.b2222 - 0.0314159265358979*m.b2223 - 0.0490873852123405*m.b2224
                           - 0.0706858347057703*m.b2225 - 0.0962112750161874*m.b2226 - 0.125663706143592*m.b2227
                           - 0.159043128087983*m.b2228 - 0.196349540849362*m.b2229 - 0.282743338823081*m.b2230
                           - 0.38484510006475*m.b2231 - 0.502654824574367*m.b2232 == 0)

m.c1323 = Constraint(expr=   m.x692 - 0.00785398163397448*m.b2233 - 0.0122718463030851*m.b2234
                           - 0.0176714586764426*m.b2235 - 0.0314159265358979*m.b2236 - 0.0490873852123405*m.b2237
                           - 0.0706858347057703*m.b2238 - 0.0962112750161874*m.b2239 - 0.125663706143592*m.b2240
                           - 0.159043128087983*m.b2241 - 0.196349540849362*m.b2242 - 0.282743338823081*m.b2243
                           - 0.38484510006475*m.b2244 - 0.502654824574367*m.b2245 == 0)

m.c1324 = Constraint(expr=   m.x693 - 0.00785398163397448*m.b2246 - 0.0122718463030851*m.b2247
                           - 0.0176714586764426*m.b2248 - 0.0314159265358979*m.b2249 - 0.0490873852123405*m.b2250
                           - 0.0706858347057703*m.b2251 - 0.0962112750161874*m.b2252 - 0.125663706143592*m.b2253
                           - 0.159043128087983*m.b2254 - 0.196349540849362*m.b2255 - 0.282743338823081*m.b2256
                           - 0.38484510006475*m.b2257 - 0.502654824574367*m.b2258 == 0)

m.c1325 = Constraint(expr=   m.x694 - 0.00785398163397448*m.b2259 - 0.0122718463030851*m.b2260
                           - 0.0176714586764426*m.b2261 - 0.0314159265358979*m.b2262 - 0.0490873852123405*m.b2263
                           - 0.0706858347057703*m.b2264 - 0.0962112750161874*m.b2265 - 0.125663706143592*m.b2266
                           - 0.159043128087983*m.b2267 - 0.196349540849362*m.b2268 - 0.282743338823081*m.b2269
                           - 0.38484510006475*m.b2270 - 0.502654824574367*m.b2271 == 0)

m.c1326 = Constraint(expr=   m.x695 - 0.00785398163397448*m.b2272 - 0.0122718463030851*m.b2273
                           - 0.0176714586764426*m.b2274 - 0.0314159265358979*m.b2275 - 0.0490873852123405*m.b2276
                           - 0.0706858347057703*m.b2277 - 0.0962112750161874*m.b2278 - 0.125663706143592*m.b2279
                           - 0.159043128087983*m.b2280 - 0.196349540849362*m.b2281 - 0.282743338823081*m.b2282
                           - 0.38484510006475*m.b2283 - 0.502654824574367*m.b2284 == 0)

m.c1327 = Constraint(expr=   m.x696 - 0.00785398163397448*m.b2285 - 0.0122718463030851*m.b2286
                           - 0.0176714586764426*m.b2287 - 0.0314159265358979*m.b2288 - 0.0490873852123405*m.b2289
                           - 0.0706858347057703*m.b2290 - 0.0962112750161874*m.b2291 - 0.125663706143592*m.b2292
                           - 0.159043128087983*m.b2293 - 0.196349540849362*m.b2294 - 0.282743338823081*m.b2295
                           - 0.38484510006475*m.b2296 - 0.502654824574367*m.b2297 == 0)

m.c1328 = Constraint(expr=   m.x697 - 0.00785398163397448*m.b2298 - 0.0122718463030851*m.b2299
                           - 0.0176714586764426*m.b2300 - 0.0314159265358979*m.b2301 - 0.0490873852123405*m.b2302
                           - 0.0706858347057703*m.b2303 - 0.0962112750161874*m.b2304 - 0.125663706143592*m.b2305
                           - 0.159043128087983*m.b2306 - 0.196349540849362*m.b2307 - 0.282743338823081*m.b2308
                           - 0.38484510006475*m.b2309 - 0.502654824574367*m.b2310 == 0)

m.c1329 = Constraint(expr=   m.x698 - 0.00785398163397448*m.b2311 - 0.0122718463030851*m.b2312
                           - 0.0176714586764426*m.b2313 - 0.0314159265358979*m.b2314 - 0.0490873852123405*m.b2315
                           - 0.0706858347057703*m.b2316 - 0.0962112750161874*m.b2317 - 0.125663706143592*m.b2318
                           - 0.159043128087983*m.b2319 - 0.196349540849362*m.b2320 - 0.282743338823081*m.b2321
                           - 0.38484510006475*m.b2322 - 0.502654824574367*m.b2323 == 0)

m.c1330 = Constraint(expr=   m.x699 - 0.00785398163397448*m.b2324 - 0.0122718463030851*m.b2325
                           - 0.0176714586764426*m.b2326 - 0.0314159265358979*m.b2327 - 0.0490873852123405*m.b2328
                           - 0.0706858347057703*m.b2329 - 0.0962112750161874*m.b2330 - 0.125663706143592*m.b2331
                           - 0.159043128087983*m.b2332 - 0.196349540849362*m.b2333 - 0.282743338823081*m.b2334
                           - 0.38484510006475*m.b2335 - 0.502654824574367*m.b2336 == 0)

m.c1331 = Constraint(expr=   m.x700 - 0.00785398163397448*m.b2337 - 0.0122718463030851*m.b2338
                           - 0.0176714586764426*m.b2339 - 0.0314159265358979*m.b2340 - 0.0490873852123405*m.b2341
                           - 0.0706858347057703*m.b2342 - 0.0962112750161874*m.b2343 - 0.125663706143592*m.b2344
                           - 0.159043128087983*m.b2345 - 0.196349540849362*m.b2346 - 0.282743338823081*m.b2347
                           - 0.38484510006475*m.b2348 - 0.502654824574367*m.b2349 == 0)

m.c1332 = Constraint(expr=   m.x701 - 0.00785398163397448*m.b2350 - 0.0122718463030851*m.b2351
                           - 0.0176714586764426*m.b2352 - 0.0314159265358979*m.b2353 - 0.0490873852123405*m.b2354
                           - 0.0706858347057703*m.b2355 - 0.0962112750161874*m.b2356 - 0.125663706143592*m.b2357
                           - 0.159043128087983*m.b2358 - 0.196349540849362*m.b2359 - 0.282743338823081*m.b2360
                           - 0.38484510006475*m.b2361 - 0.502654824574367*m.b2362 == 0)

m.c1333 = Constraint(expr=   m.x702 - 0.00785398163397448*m.b2363 - 0.0122718463030851*m.b2364
                           - 0.0176714586764426*m.b2365 - 0.0314159265358979*m.b2366 - 0.0490873852123405*m.b2367
                           - 0.0706858347057703*m.b2368 - 0.0962112750161874*m.b2369 - 0.125663706143592*m.b2370
                           - 0.159043128087983*m.b2371 - 0.196349540849362*m.b2372 - 0.282743338823081*m.b2373
                           - 0.38484510006475*m.b2374 - 0.502654824574367*m.b2375 == 0)

m.c1334 = Constraint(expr=   m.x703 - 0.00785398163397448*m.b2376 - 0.0122718463030851*m.b2377
                           - 0.0176714586764426*m.b2378 - 0.0314159265358979*m.b2379 - 0.0490873852123405*m.b2380
                           - 0.0706858347057703*m.b2381 - 0.0962112750161874*m.b2382 - 0.125663706143592*m.b2383
                           - 0.159043128087983*m.b2384 - 0.196349540849362*m.b2385 - 0.282743338823081*m.b2386
                           - 0.38484510006475*m.b2387 - 0.502654824574367*m.b2388 == 0)

m.c1335 = Constraint(expr=   m.x704 - 0.00785398163397448*m.b2389 - 0.0122718463030851*m.b2390
                           - 0.0176714586764426*m.b2391 - 0.0314159265358979*m.b2392 - 0.0490873852123405*m.b2393
                           - 0.0706858347057703*m.b2394 - 0.0962112750161874*m.b2395 - 0.125663706143592*m.b2396
                           - 0.159043128087983*m.b2397 - 0.196349540849362*m.b2398 - 0.282743338823081*m.b2399
                           - 0.38484510006475*m.b2400 - 0.502654824574367*m.b2401 == 0)

m.c1336 = Constraint(expr=   m.x705 - 0.00785398163397448*m.b2402 - 0.0122718463030851*m.b2403
                           - 0.0176714586764426*m.b2404 - 0.0314159265358979*m.b2405 - 0.0490873852123405*m.b2406
                           - 0.0706858347057703*m.b2407 - 0.0962112750161874*m.b2408 - 0.125663706143592*m.b2409
                           - 0.159043128087983*m.b2410 - 0.196349540849362*m.b2411 - 0.282743338823081*m.b2412
                           - 0.38484510006475*m.b2413 - 0.502654824574367*m.b2414 == 0)

m.c1337 = Constraint(expr=   m.x706 - 0.00785398163397448*m.b2415 - 0.0122718463030851*m.b2416
                           - 0.0176714586764426*m.b2417 - 0.0314159265358979*m.b2418 - 0.0490873852123405*m.b2419
                           - 0.0706858347057703*m.b2420 - 0.0962112750161874*m.b2421 - 0.125663706143592*m.b2422
                           - 0.159043128087983*m.b2423 - 0.196349540849362*m.b2424 - 0.282743338823081*m.b2425
                           - 0.38484510006475*m.b2426 - 0.502654824574367*m.b2427 == 0)

m.c1338 = Constraint(expr=   m.x707 - 0.00785398163397448*m.b2428 - 0.0122718463030851*m.b2429
                           - 0.0176714586764426*m.b2430 - 0.0314159265358979*m.b2431 - 0.0490873852123405*m.b2432
                           - 0.0706858347057703*m.b2433 - 0.0962112750161874*m.b2434 - 0.125663706143592*m.b2435
                           - 0.159043128087983*m.b2436 - 0.196349540849362*m.b2437 - 0.282743338823081*m.b2438
                           - 0.38484510006475*m.b2439 - 0.502654824574367*m.b2440 == 0)

m.c1339 = Constraint(expr=   m.x708 - 0.00785398163397448*m.b2441 - 0.0122718463030851*m.b2442
                           - 0.0176714586764426*m.b2443 - 0.0314159265358979*m.b2444 - 0.0490873852123405*m.b2445
                           - 0.0706858347057703*m.b2446 - 0.0962112750161874*m.b2447 - 0.125663706143592*m.b2448
                           - 0.159043128087983*m.b2449 - 0.196349540849362*m.b2450 - 0.282743338823081*m.b2451
                           - 0.38484510006475*m.b2452 - 0.502654824574367*m.b2453 == 0)

m.c1340 = Constraint(expr=   m.x709 - 0.00785398163397448*m.b2454 - 0.0122718463030851*m.b2455
                           - 0.0176714586764426*m.b2456 - 0.0314159265358979*m.b2457 - 0.0490873852123405*m.b2458
                           - 0.0706858347057703*m.b2459 - 0.0962112750161874*m.b2460 - 0.125663706143592*m.b2461
                           - 0.159043128087983*m.b2462 - 0.196349540849362*m.b2463 - 0.282743338823081*m.b2464
                           - 0.38484510006475*m.b2465 - 0.502654824574367*m.b2466 == 0)

m.c1341 = Constraint(expr=   m.x710 - 0.00785398163397448*m.b2467 - 0.0122718463030851*m.b2468
                           - 0.0176714586764426*m.b2469 - 0.0314159265358979*m.b2470 - 0.0490873852123405*m.b2471
                           - 0.0706858347057703*m.b2472 - 0.0962112750161874*m.b2473 - 0.125663706143592*m.b2474
                           - 0.159043128087983*m.b2475 - 0.196349540849362*m.b2476 - 0.282743338823081*m.b2477
                           - 0.38484510006475*m.b2478 - 0.502654824574367*m.b2479 == 0)

m.c1342 = Constraint(expr=   m.x711 - 0.00785398163397448*m.b2480 - 0.0122718463030851*m.b2481
                           - 0.0176714586764426*m.b2482 - 0.0314159265358979*m.b2483 - 0.0490873852123405*m.b2484
                           - 0.0706858347057703*m.b2485 - 0.0962112750161874*m.b2486 - 0.125663706143592*m.b2487
                           - 0.159043128087983*m.b2488 - 0.196349540849362*m.b2489 - 0.282743338823081*m.b2490
                           - 0.38484510006475*m.b2491 - 0.502654824574367*m.b2492 == 0)

m.c1343 = Constraint(expr=   m.x712 - 0.00785398163397448*m.b2493 - 0.0122718463030851*m.b2494
                           - 0.0176714586764426*m.b2495 - 0.0314159265358979*m.b2496 - 0.0490873852123405*m.b2497
                           - 0.0706858347057703*m.b2498 - 0.0962112750161874*m.b2499 - 0.125663706143592*m.b2500
                           - 0.159043128087983*m.b2501 - 0.196349540849362*m.b2502 - 0.282743338823081*m.b2503
                           - 0.38484510006475*m.b2504 - 0.502654824574367*m.b2505 == 0)

m.c1344 = Constraint(expr=   m.x713 - 0.00785398163397448*m.b2506 - 0.0122718463030851*m.b2507
                           - 0.0176714586764426*m.b2508 - 0.0314159265358979*m.b2509 - 0.0490873852123405*m.b2510
                           - 0.0706858347057703*m.b2511 - 0.0962112750161874*m.b2512 - 0.125663706143592*m.b2513
                           - 0.159043128087983*m.b2514 - 0.196349540849362*m.b2515 - 0.282743338823081*m.b2516
                           - 0.38484510006475*m.b2517 - 0.502654824574367*m.b2518 == 0)

m.c1345 = Constraint(expr=   m.x714 - 0.00785398163397448*m.b2519 - 0.0122718463030851*m.b2520
                           - 0.0176714586764426*m.b2521 - 0.0314159265358979*m.b2522 - 0.0490873852123405*m.b2523
                           - 0.0706858347057703*m.b2524 - 0.0962112750161874*m.b2525 - 0.125663706143592*m.b2526
                           - 0.159043128087983*m.b2527 - 0.196349540849362*m.b2528 - 0.282743338823081*m.b2529
                           - 0.38484510006475*m.b2530 - 0.502654824574367*m.b2531 == 0)

m.c1346 = Constraint(expr=   m.x715 - 0.00785398163397448*m.b2532 - 0.0122718463030851*m.b2533
                           - 0.0176714586764426*m.b2534 - 0.0314159265358979*m.b2535 - 0.0490873852123405*m.b2536
                           - 0.0706858347057703*m.b2537 - 0.0962112750161874*m.b2538 - 0.125663706143592*m.b2539
                           - 0.159043128087983*m.b2540 - 0.196349540849362*m.b2541 - 0.282743338823081*m.b2542
                           - 0.38484510006475*m.b2543 - 0.502654824574367*m.b2544 == 0)

m.c1347 = Constraint(expr=   m.x716 - 0.00785398163397448*m.b2545 - 0.0122718463030851*m.b2546
                           - 0.0176714586764426*m.b2547 - 0.0314159265358979*m.b2548 - 0.0490873852123405*m.b2549
                           - 0.0706858347057703*m.b2550 - 0.0962112750161874*m.b2551 - 0.125663706143592*m.b2552
                           - 0.159043128087983*m.b2553 - 0.196349540849362*m.b2554 - 0.282743338823081*m.b2555
                           - 0.38484510006475*m.b2556 - 0.502654824574367*m.b2557 == 0)

m.c1348 = Constraint(expr=   m.x717 - 0.00785398163397448*m.b2558 - 0.0122718463030851*m.b2559
                           - 0.0176714586764426*m.b2560 - 0.0314159265358979*m.b2561 - 0.0490873852123405*m.b2562
                           - 0.0706858347057703*m.b2563 - 0.0962112750161874*m.b2564 - 0.125663706143592*m.b2565
                           - 0.159043128087983*m.b2566 - 0.196349540849362*m.b2567 - 0.282743338823081*m.b2568
                           - 0.38484510006475*m.b2569 - 0.502654824574367*m.b2570 == 0)

m.c1349 = Constraint(expr=   m.x718 - 0.00785398163397448*m.b2571 - 0.0122718463030851*m.b2572
                           - 0.0176714586764426*m.b2573 - 0.0314159265358979*m.b2574 - 0.0490873852123405*m.b2575
                           - 0.0706858347057703*m.b2576 - 0.0962112750161874*m.b2577 - 0.125663706143592*m.b2578
                           - 0.159043128087983*m.b2579 - 0.196349540849362*m.b2580 - 0.282743338823081*m.b2581
                           - 0.38484510006475*m.b2582 - 0.502654824574367*m.b2583 == 0)

m.c1350 = Constraint(expr=   m.x719 - 0.00785398163397448*m.b2584 - 0.0122718463030851*m.b2585
                           - 0.0176714586764426*m.b2586 - 0.0314159265358979*m.b2587 - 0.0490873852123405*m.b2588
                           - 0.0706858347057703*m.b2589 - 0.0962112750161874*m.b2590 - 0.125663706143592*m.b2591
                           - 0.159043128087983*m.b2592 - 0.196349540849362*m.b2593 - 0.282743338823081*m.b2594
                           - 0.38484510006475*m.b2595 - 0.502654824574367*m.b2596 == 0)

m.c1351 = Constraint(expr=   m.x720 - 0.00785398163397448*m.b2597 - 0.0122718463030851*m.b2598
                           - 0.0176714586764426*m.b2599 - 0.0314159265358979*m.b2600 - 0.0490873852123405*m.b2601
                           - 0.0706858347057703*m.b2602 - 0.0962112750161874*m.b2603 - 0.125663706143592*m.b2604
                           - 0.159043128087983*m.b2605 - 0.196349540849362*m.b2606 - 0.282743338823081*m.b2607
                           - 0.38484510006475*m.b2608 - 0.502654824574367*m.b2609 == 0)

m.c1352 = Constraint(expr=   m.x721 - 0.00785398163397448*m.b2610 - 0.0122718463030851*m.b2611
                           - 0.0176714586764426*m.b2612 - 0.0314159265358979*m.b2613 - 0.0490873852123405*m.b2614
                           - 0.0706858347057703*m.b2615 - 0.0962112750161874*m.b2616 - 0.125663706143592*m.b2617
                           - 0.159043128087983*m.b2618 - 0.196349540849362*m.b2619 - 0.282743338823081*m.b2620
                           - 0.38484510006475*m.b2621 - 0.502654824574367*m.b2622 == 0)

m.c1353 = Constraint(expr=   m.x722 - 0.00785398163397448*m.b2623 - 0.0122718463030851*m.b2624
                           - 0.0176714586764426*m.b2625 - 0.0314159265358979*m.b2626 - 0.0490873852123405*m.b2627
                           - 0.0706858347057703*m.b2628 - 0.0962112750161874*m.b2629 - 0.125663706143592*m.b2630
                           - 0.159043128087983*m.b2631 - 0.196349540849362*m.b2632 - 0.282743338823081*m.b2633
                           - 0.38484510006475*m.b2634 - 0.502654824574367*m.b2635 == 0)

m.c1354 = Constraint(expr=   m.x723 - 0.00785398163397448*m.b2636 - 0.0122718463030851*m.b2637
                           - 0.0176714586764426*m.b2638 - 0.0314159265358979*m.b2639 - 0.0490873852123405*m.b2640
                           - 0.0706858347057703*m.b2641 - 0.0962112750161874*m.b2642 - 0.125663706143592*m.b2643
                           - 0.159043128087983*m.b2644 - 0.196349540849362*m.b2645 - 0.282743338823081*m.b2646
                           - 0.38484510006475*m.b2647 - 0.502654824574367*m.b2648 == 0)

m.c1355 = Constraint(expr=   m.x724 - 0.00785398163397448*m.b2649 - 0.0122718463030851*m.b2650
                           - 0.0176714586764426*m.b2651 - 0.0314159265358979*m.b2652 - 0.0490873852123405*m.b2653
                           - 0.0706858347057703*m.b2654 - 0.0962112750161874*m.b2655 - 0.125663706143592*m.b2656
                           - 0.159043128087983*m.b2657 - 0.196349540849362*m.b2658 - 0.282743338823081*m.b2659
                           - 0.38484510006475*m.b2660 - 0.502654824574367*m.b2661 == 0)

m.c1356 = Constraint(expr=   m.x725 - 0.00785398163397448*m.b2662 - 0.0122718463030851*m.b2663
                           - 0.0176714586764426*m.b2664 - 0.0314159265358979*m.b2665 - 0.0490873852123405*m.b2666
                           - 0.0706858347057703*m.b2667 - 0.0962112750161874*m.b2668 - 0.125663706143592*m.b2669
                           - 0.159043128087983*m.b2670 - 0.196349540849362*m.b2671 - 0.282743338823081*m.b2672
                           - 0.38484510006475*m.b2673 - 0.502654824574367*m.b2674 == 0)

m.c1357 = Constraint(expr=   m.x726 - 0.00785398163397448*m.b2675 - 0.0122718463030851*m.b2676
                           - 0.0176714586764426*m.b2677 - 0.0314159265358979*m.b2678 - 0.0490873852123405*m.b2679
                           - 0.0706858347057703*m.b2680 - 0.0962112750161874*m.b2681 - 0.125663706143592*m.b2682
                           - 0.159043128087983*m.b2683 - 0.196349540849362*m.b2684 - 0.282743338823081*m.b2685
                           - 0.38484510006475*m.b2686 - 0.502654824574367*m.b2687 == 0)

m.c1358 = Constraint(expr=   m.x727 - 0.00785398163397448*m.b2688 - 0.0122718463030851*m.b2689
                           - 0.0176714586764426*m.b2690 - 0.0314159265358979*m.b2691 - 0.0490873852123405*m.b2692
                           - 0.0706858347057703*m.b2693 - 0.0962112750161874*m.b2694 - 0.125663706143592*m.b2695
                           - 0.159043128087983*m.b2696 - 0.196349540849362*m.b2697 - 0.282743338823081*m.b2698
                           - 0.38484510006475*m.b2699 - 0.502654824574367*m.b2700 == 0)

m.c1359 = Constraint(expr=   m.x728 - 0.00785398163397448*m.b2701 - 0.0122718463030851*m.b2702
                           - 0.0176714586764426*m.b2703 - 0.0314159265358979*m.b2704 - 0.0490873852123405*m.b2705
                           - 0.0706858347057703*m.b2706 - 0.0962112750161874*m.b2707 - 0.125663706143592*m.b2708
                           - 0.159043128087983*m.b2709 - 0.196349540849362*m.b2710 - 0.282743338823081*m.b2711
                           - 0.38484510006475*m.b2712 - 0.502654824574367*m.b2713 == 0)

m.c1360 = Constraint(expr=   m.x729 - 0.00785398163397448*m.b2714 - 0.0122718463030851*m.b2715
                           - 0.0176714586764426*m.b2716 - 0.0314159265358979*m.b2717 - 0.0490873852123405*m.b2718
                           - 0.0706858347057703*m.b2719 - 0.0962112750161874*m.b2720 - 0.125663706143592*m.b2721
                           - 0.159043128087983*m.b2722 - 0.196349540849362*m.b2723 - 0.282743338823081*m.b2724
                           - 0.38484510006475*m.b2725 - 0.502654824574367*m.b2726 == 0)

m.c1361 = Constraint(expr=   m.x730 - 0.00785398163397448*m.b2727 - 0.0122718463030851*m.b2728
                           - 0.0176714586764426*m.b2729 - 0.0314159265358979*m.b2730 - 0.0490873852123405*m.b2731
                           - 0.0706858347057703*m.b2732 - 0.0962112750161874*m.b2733 - 0.125663706143592*m.b2734
                           - 0.159043128087983*m.b2735 - 0.196349540849362*m.b2736 - 0.282743338823081*m.b2737
                           - 0.38484510006475*m.b2738 - 0.502654824574367*m.b2739 == 0)

m.c1362 = Constraint(expr=   m.x731 - 0.00785398163397448*m.b2740 - 0.0122718463030851*m.b2741
                           - 0.0176714586764426*m.b2742 - 0.0314159265358979*m.b2743 - 0.0490873852123405*m.b2744
                           - 0.0706858347057703*m.b2745 - 0.0962112750161874*m.b2746 - 0.125663706143592*m.b2747
                           - 0.159043128087983*m.b2748 - 0.196349540849362*m.b2749 - 0.282743338823081*m.b2750
                           - 0.38484510006475*m.b2751 - 0.502654824574367*m.b2752 == 0)

m.c1363 = Constraint(expr=   m.x732 - 0.00785398163397448*m.b2753 - 0.0122718463030851*m.b2754
                           - 0.0176714586764426*m.b2755 - 0.0314159265358979*m.b2756 - 0.0490873852123405*m.b2757
                           - 0.0706858347057703*m.b2758 - 0.0962112750161874*m.b2759 - 0.125663706143592*m.b2760
                           - 0.159043128087983*m.b2761 - 0.196349540849362*m.b2762 - 0.282743338823081*m.b2763
                           - 0.38484510006475*m.b2764 - 0.502654824574367*m.b2765 == 0)

m.c1364 = Constraint(expr=   m.x733 - 0.00785398163397448*m.b2766 - 0.0122718463030851*m.b2767
                           - 0.0176714586764426*m.b2768 - 0.0314159265358979*m.b2769 - 0.0490873852123405*m.b2770
                           - 0.0706858347057703*m.b2771 - 0.0962112750161874*m.b2772 - 0.125663706143592*m.b2773
                           - 0.159043128087983*m.b2774 - 0.196349540849362*m.b2775 - 0.282743338823081*m.b2776
                           - 0.38484510006475*m.b2777 - 0.502654824574367*m.b2778 == 0)

m.c1365 = Constraint(expr=   m.x734 - 0.00785398163397448*m.b2779 - 0.0122718463030851*m.b2780
                           - 0.0176714586764426*m.b2781 - 0.0314159265358979*m.b2782 - 0.0490873852123405*m.b2783
                           - 0.0706858347057703*m.b2784 - 0.0962112750161874*m.b2785 - 0.125663706143592*m.b2786
                           - 0.159043128087983*m.b2787 - 0.196349540849362*m.b2788 - 0.282743338823081*m.b2789
                           - 0.38484510006475*m.b2790 - 0.502654824574367*m.b2791 == 0)

m.c1366 = Constraint(expr=   m.x735 - 0.00785398163397448*m.b2792 - 0.0122718463030851*m.b2793
                           - 0.0176714586764426*m.b2794 - 0.0314159265358979*m.b2795 - 0.0490873852123405*m.b2796
                           - 0.0706858347057703*m.b2797 - 0.0962112750161874*m.b2798 - 0.125663706143592*m.b2799
                           - 0.159043128087983*m.b2800 - 0.196349540849362*m.b2801 - 0.282743338823081*m.b2802
                           - 0.38484510006475*m.b2803 - 0.502654824574367*m.b2804 == 0)

m.c1367 = Constraint(expr=   m.x736 - 0.00785398163397448*m.b2805 - 0.0122718463030851*m.b2806
                           - 0.0176714586764426*m.b2807 - 0.0314159265358979*m.b2808 - 0.0490873852123405*m.b2809
                           - 0.0706858347057703*m.b2810 - 0.0962112750161874*m.b2811 - 0.125663706143592*m.b2812
                           - 0.159043128087983*m.b2813 - 0.196349540849362*m.b2814 - 0.282743338823081*m.b2815
                           - 0.38484510006475*m.b2816 - 0.502654824574367*m.b2817 == 0)

m.c1368 = Constraint(expr=   m.x737 - 0.00785398163397448*m.b2818 - 0.0122718463030851*m.b2819
                           - 0.0176714586764426*m.b2820 - 0.0314159265358979*m.b2821 - 0.0490873852123405*m.b2822
                           - 0.0706858347057703*m.b2823 - 0.0962112750161874*m.b2824 - 0.125663706143592*m.b2825
                           - 0.159043128087983*m.b2826 - 0.196349540849362*m.b2827 - 0.282743338823081*m.b2828
                           - 0.38484510006475*m.b2829 - 0.502654824574367*m.b2830 == 0)

m.c1369 = Constraint(expr=   m.x738 - 0.00785398163397448*m.b2831 - 0.0122718463030851*m.b2832
                           - 0.0176714586764426*m.b2833 - 0.0314159265358979*m.b2834 - 0.0490873852123405*m.b2835
                           - 0.0706858347057703*m.b2836 - 0.0962112750161874*m.b2837 - 0.125663706143592*m.b2838
                           - 0.159043128087983*m.b2839 - 0.196349540849362*m.b2840 - 0.282743338823081*m.b2841
                           - 0.38484510006475*m.b2842 - 0.502654824574367*m.b2843 == 0)

m.c1370 = Constraint(expr=   m.x739 - 0.00785398163397448*m.b2844 - 0.0122718463030851*m.b2845
                           - 0.0176714586764426*m.b2846 - 0.0314159265358979*m.b2847 - 0.0490873852123405*m.b2848
                           - 0.0706858347057703*m.b2849 - 0.0962112750161874*m.b2850 - 0.125663706143592*m.b2851
                           - 0.159043128087983*m.b2852 - 0.196349540849362*m.b2853 - 0.282743338823081*m.b2854
                           - 0.38484510006475*m.b2855 - 0.502654824574367*m.b2856 == 0)

m.c1371 = Constraint(expr=   m.x740 - 0.00785398163397448*m.b2857 - 0.0122718463030851*m.b2858
                           - 0.0176714586764426*m.b2859 - 0.0314159265358979*m.b2860 - 0.0490873852123405*m.b2861
                           - 0.0706858347057703*m.b2862 - 0.0962112750161874*m.b2863 - 0.125663706143592*m.b2864
                           - 0.159043128087983*m.b2865 - 0.196349540849362*m.b2866 - 0.282743338823081*m.b2867
                           - 0.38484510006475*m.b2868 - 0.502654824574367*m.b2869 == 0)

m.c1372 = Constraint(expr=   m.x741 - 0.00785398163397448*m.b2870 - 0.0122718463030851*m.b2871
                           - 0.0176714586764426*m.b2872 - 0.0314159265358979*m.b2873 - 0.0490873852123405*m.b2874
                           - 0.0706858347057703*m.b2875 - 0.0962112750161874*m.b2876 - 0.125663706143592*m.b2877
                           - 0.159043128087983*m.b2878 - 0.196349540849362*m.b2879 - 0.282743338823081*m.b2880
                           - 0.38484510006475*m.b2881 - 0.502654824574367*m.b2882 == 0)

m.c1373 = Constraint(expr=   m.x742 - 0.00785398163397448*m.b2883 - 0.0122718463030851*m.b2884
                           - 0.0176714586764426*m.b2885 - 0.0314159265358979*m.b2886 - 0.0490873852123405*m.b2887
                           - 0.0706858347057703*m.b2888 - 0.0962112750161874*m.b2889 - 0.125663706143592*m.b2890
                           - 0.159043128087983*m.b2891 - 0.196349540849362*m.b2892 - 0.282743338823081*m.b2893
                           - 0.38484510006475*m.b2894 - 0.502654824574367*m.b2895 == 0)

m.c1374 = Constraint(expr=   m.x743 - 0.00785398163397448*m.b2896 - 0.0122718463030851*m.b2897
                           - 0.0176714586764426*m.b2898 - 0.0314159265358979*m.b2899 - 0.0490873852123405*m.b2900
                           - 0.0706858347057703*m.b2901 - 0.0962112750161874*m.b2902 - 0.125663706143592*m.b2903
                           - 0.159043128087983*m.b2904 - 0.196349540849362*m.b2905 - 0.282743338823081*m.b2906
                           - 0.38484510006475*m.b2907 - 0.502654824574367*m.b2908 == 0)

m.c1375 = Constraint(expr=   m.x744 - 0.00785398163397448*m.b2909 - 0.0122718463030851*m.b2910
                           - 0.0176714586764426*m.b2911 - 0.0314159265358979*m.b2912 - 0.0490873852123405*m.b2913
                           - 0.0706858347057703*m.b2914 - 0.0962112750161874*m.b2915 - 0.125663706143592*m.b2916
                           - 0.159043128087983*m.b2917 - 0.196349540849362*m.b2918 - 0.282743338823081*m.b2919
                           - 0.38484510006475*m.b2920 - 0.502654824574367*m.b2921 == 0)

m.c1376 = Constraint(expr=   m.x745 - 0.00785398163397448*m.b2922 - 0.0122718463030851*m.b2923
                           - 0.0176714586764426*m.b2924 - 0.0314159265358979*m.b2925 - 0.0490873852123405*m.b2926
                           - 0.0706858347057703*m.b2927 - 0.0962112750161874*m.b2928 - 0.125663706143592*m.b2929
                           - 0.159043128087983*m.b2930 - 0.196349540849362*m.b2931 - 0.282743338823081*m.b2932
                           - 0.38484510006475*m.b2933 - 0.502654824574367*m.b2934 == 0)

m.c1377 = Constraint(expr=   m.x746 - 0.00785398163397448*m.b2935 - 0.0122718463030851*m.b2936
                           - 0.0176714586764426*m.b2937 - 0.0314159265358979*m.b2938 - 0.0490873852123405*m.b2939
                           - 0.0706858347057703*m.b2940 - 0.0962112750161874*m.b2941 - 0.125663706143592*m.b2942
                           - 0.159043128087983*m.b2943 - 0.196349540849362*m.b2944 - 0.282743338823081*m.b2945
                           - 0.38484510006475*m.b2946 - 0.502654824574367*m.b2947 == 0)

m.c1378 = Constraint(expr=   m.x747 - 0.00785398163397448*m.b2948 - 0.0122718463030851*m.b2949
                           - 0.0176714586764426*m.b2950 - 0.0314159265358979*m.b2951 - 0.0490873852123405*m.b2952
                           - 0.0706858347057703*m.b2953 - 0.0962112750161874*m.b2954 - 0.125663706143592*m.b2955
                           - 0.159043128087983*m.b2956 - 0.196349540849362*m.b2957 - 0.282743338823081*m.b2958
                           - 0.38484510006475*m.b2959 - 0.502654824574367*m.b2960 == 0)

m.c1379 = Constraint(expr=   m.x748 - 0.00785398163397448*m.b2961 - 0.0122718463030851*m.b2962
                           - 0.0176714586764426*m.b2963 - 0.0314159265358979*m.b2964 - 0.0490873852123405*m.b2965
                           - 0.0706858347057703*m.b2966 - 0.0962112750161874*m.b2967 - 0.125663706143592*m.b2968
                           - 0.159043128087983*m.b2969 - 0.196349540849362*m.b2970 - 0.282743338823081*m.b2971
                           - 0.38484510006475*m.b2972 - 0.502654824574367*m.b2973 == 0)

m.c1380 = Constraint(expr=   m.x749 - 0.00785398163397448*m.b2974 - 0.0122718463030851*m.b2975
                           - 0.0176714586764426*m.b2976 - 0.0314159265358979*m.b2977 - 0.0490873852123405*m.b2978
                           - 0.0706858347057703*m.b2979 - 0.0962112750161874*m.b2980 - 0.125663706143592*m.b2981
                           - 0.159043128087983*m.b2982 - 0.196349540849362*m.b2983 - 0.282743338823081*m.b2984
                           - 0.38484510006475*m.b2985 - 0.502654824574367*m.b2986 == 0)

m.c1381 = Constraint(expr=   m.x750 - 0.00785398163397448*m.b2987 - 0.0122718463030851*m.b2988
                           - 0.0176714586764426*m.b2989 - 0.0314159265358979*m.b2990 - 0.0490873852123405*m.b2991
                           - 0.0706858347057703*m.b2992 - 0.0962112750161874*m.b2993 - 0.125663706143592*m.b2994
                           - 0.159043128087983*m.b2995 - 0.196349540849362*m.b2996 - 0.282743338823081*m.b2997
                           - 0.38484510006475*m.b2998 - 0.502654824574367*m.b2999 == 0)

m.c1382 = Constraint(expr=   m.x751 - 0.00785398163397448*m.b3000 - 0.0122718463030851*m.b3001
                           - 0.0176714586764426*m.b3002 - 0.0314159265358979*m.b3003 - 0.0490873852123405*m.b3004
                           - 0.0706858347057703*m.b3005 - 0.0962112750161874*m.b3006 - 0.125663706143592*m.b3007
                           - 0.159043128087983*m.b3008 - 0.196349540849362*m.b3009 - 0.282743338823081*m.b3010
                           - 0.38484510006475*m.b3011 - 0.502654824574367*m.b3012 == 0)

m.c1383 = Constraint(expr=   m.x752 - 0.00785398163397448*m.b3013 - 0.0122718463030851*m.b3014
                           - 0.0176714586764426*m.b3015 - 0.0314159265358979*m.b3016 - 0.0490873852123405*m.b3017
                           - 0.0706858347057703*m.b3018 - 0.0962112750161874*m.b3019 - 0.125663706143592*m.b3020
                           - 0.159043128087983*m.b3021 - 0.196349540849362*m.b3022 - 0.282743338823081*m.b3023
                           - 0.38484510006475*m.b3024 - 0.502654824574367*m.b3025 == 0)

m.c1384 = Constraint(expr=   m.x753 - 0.00785398163397448*m.b3026 - 0.0122718463030851*m.b3027
                           - 0.0176714586764426*m.b3028 - 0.0314159265358979*m.b3029 - 0.0490873852123405*m.b3030
                           - 0.0706858347057703*m.b3031 - 0.0962112750161874*m.b3032 - 0.125663706143592*m.b3033
                           - 0.159043128087983*m.b3034 - 0.196349540849362*m.b3035 - 0.282743338823081*m.b3036
                           - 0.38484510006475*m.b3037 - 0.502654824574367*m.b3038 == 0)

m.c1385 = Constraint(expr=   m.x754 - 0.00785398163397448*m.b3039 - 0.0122718463030851*m.b3040
                           - 0.0176714586764426*m.b3041 - 0.0314159265358979*m.b3042 - 0.0490873852123405*m.b3043
                           - 0.0706858347057703*m.b3044 - 0.0962112750161874*m.b3045 - 0.125663706143592*m.b3046
                           - 0.159043128087983*m.b3047 - 0.196349540849362*m.b3048 - 0.282743338823081*m.b3049
                           - 0.38484510006475*m.b3050 - 0.502654824574367*m.b3051 == 0)

m.c1386 = Constraint(expr=   m.x755 - 0.00785398163397448*m.b3052 - 0.0122718463030851*m.b3053
                           - 0.0176714586764426*m.b3054 - 0.0314159265358979*m.b3055 - 0.0490873852123405*m.b3056
                           - 0.0706858347057703*m.b3057 - 0.0962112750161874*m.b3058 - 0.125663706143592*m.b3059
                           - 0.159043128087983*m.b3060 - 0.196349540849362*m.b3061 - 0.282743338823081*m.b3062
                           - 0.38484510006475*m.b3063 - 0.502654824574367*m.b3064 == 0)

m.c1387 = Constraint(expr=   m.x756 - 0.00785398163397448*m.b3065 - 0.0122718463030851*m.b3066
                           - 0.0176714586764426*m.b3067 - 0.0314159265358979*m.b3068 - 0.0490873852123405*m.b3069
                           - 0.0706858347057703*m.b3070 - 0.0962112750161874*m.b3071 - 0.125663706143592*m.b3072
                           - 0.159043128087983*m.b3073 - 0.196349540849362*m.b3074 - 0.282743338823081*m.b3075
                           - 0.38484510006475*m.b3076 - 0.502654824574367*m.b3077 == 0)

m.c1388 = Constraint(expr=   m.x757 - 0.00785398163397448*m.b3078 - 0.0122718463030851*m.b3079
                           - 0.0176714586764426*m.b3080 - 0.0314159265358979*m.b3081 - 0.0490873852123405*m.b3082
                           - 0.0706858347057703*m.b3083 - 0.0962112750161874*m.b3084 - 0.125663706143592*m.b3085
                           - 0.159043128087983*m.b3086 - 0.196349540849362*m.b3087 - 0.282743338823081*m.b3088
                           - 0.38484510006475*m.b3089 - 0.502654824574367*m.b3090 == 0)

m.c1389 = Constraint(expr=   m.x758 - 0.00785398163397448*m.b3091 - 0.0122718463030851*m.b3092
                           - 0.0176714586764426*m.b3093 - 0.0314159265358979*m.b3094 - 0.0490873852123405*m.b3095
                           - 0.0706858347057703*m.b3096 - 0.0962112750161874*m.b3097 - 0.125663706143592*m.b3098
                           - 0.159043128087983*m.b3099 - 0.196349540849362*m.b3100 - 0.282743338823081*m.b3101
                           - 0.38484510006475*m.b3102 - 0.502654824574367*m.b3103 == 0)

m.c1390 = Constraint(expr=   m.x759 - 0.00785398163397448*m.b3104 - 0.0122718463030851*m.b3105
                           - 0.0176714586764426*m.b3106 - 0.0314159265358979*m.b3107 - 0.0490873852123405*m.b3108
                           - 0.0706858347057703*m.b3109 - 0.0962112750161874*m.b3110 - 0.125663706143592*m.b3111
                           - 0.159043128087983*m.b3112 - 0.196349540849362*m.b3113 - 0.282743338823081*m.b3114
                           - 0.38484510006475*m.b3115 - 0.502654824574367*m.b3116 == 0)

m.c1391 = Constraint(expr=   m.x760 - 0.00785398163397448*m.b3117 - 0.0122718463030851*m.b3118
                           - 0.0176714586764426*m.b3119 - 0.0314159265358979*m.b3120 - 0.0490873852123405*m.b3121
                           - 0.0706858347057703*m.b3122 - 0.0962112750161874*m.b3123 - 0.125663706143592*m.b3124
                           - 0.159043128087983*m.b3125 - 0.196349540849362*m.b3126 - 0.282743338823081*m.b3127
                           - 0.38484510006475*m.b3128 - 0.502654824574367*m.b3129 == 0)

m.c1392 = Constraint(expr=   m.x761 - 0.00785398163397448*m.b3130 - 0.0122718463030851*m.b3131
                           - 0.0176714586764426*m.b3132 - 0.0314159265358979*m.b3133 - 0.0490873852123405*m.b3134
                           - 0.0706858347057703*m.b3135 - 0.0962112750161874*m.b3136 - 0.125663706143592*m.b3137
                           - 0.159043128087983*m.b3138 - 0.196349540849362*m.b3139 - 0.282743338823081*m.b3140
                           - 0.38484510006475*m.b3141 - 0.502654824574367*m.b3142 == 0)

m.c1393 = Constraint(expr=   m.x762 - 0.00785398163397448*m.b3143 - 0.0122718463030851*m.b3144
                           - 0.0176714586764426*m.b3145 - 0.0314159265358979*m.b3146 - 0.0490873852123405*m.b3147
                           - 0.0706858347057703*m.b3148 - 0.0962112750161874*m.b3149 - 0.125663706143592*m.b3150
                           - 0.159043128087983*m.b3151 - 0.196349540849362*m.b3152 - 0.282743338823081*m.b3153
                           - 0.38484510006475*m.b3154 - 0.502654824574367*m.b3155 == 0)

m.c1394 = Constraint(expr=   m.x763 - 0.00785398163397448*m.b3156 - 0.0122718463030851*m.b3157
                           - 0.0176714586764426*m.b3158 - 0.0314159265358979*m.b3159 - 0.0490873852123405*m.b3160
                           - 0.0706858347057703*m.b3161 - 0.0962112750161874*m.b3162 - 0.125663706143592*m.b3163
                           - 0.159043128087983*m.b3164 - 0.196349540849362*m.b3165 - 0.282743338823081*m.b3166
                           - 0.38484510006475*m.b3167 - 0.502654824574367*m.b3168 == 0)

m.c1395 = Constraint(expr=   m.x764 - 0.00785398163397448*m.b3169 - 0.0122718463030851*m.b3170
                           - 0.0176714586764426*m.b3171 - 0.0314159265358979*m.b3172 - 0.0490873852123405*m.b3173
                           - 0.0706858347057703*m.b3174 - 0.0962112750161874*m.b3175 - 0.125663706143592*m.b3176
                           - 0.159043128087983*m.b3177 - 0.196349540849362*m.b3178 - 0.282743338823081*m.b3179
                           - 0.38484510006475*m.b3180 - 0.502654824574367*m.b3181 == 0)

m.c1396 = Constraint(expr=   m.x765 - 0.00785398163397448*m.b3182 - 0.0122718463030851*m.b3183
                           - 0.0176714586764426*m.b3184 - 0.0314159265358979*m.b3185 - 0.0490873852123405*m.b3186
                           - 0.0706858347057703*m.b3187 - 0.0962112750161874*m.b3188 - 0.125663706143592*m.b3189
                           - 0.159043128087983*m.b3190 - 0.196349540849362*m.b3191 - 0.282743338823081*m.b3192
                           - 0.38484510006475*m.b3193 - 0.502654824574367*m.b3194 == 0)

m.c1397 = Constraint(expr=   m.x766 - 0.00785398163397448*m.b3195 - 0.0122718463030851*m.b3196
                           - 0.0176714586764426*m.b3197 - 0.0314159265358979*m.b3198 - 0.0490873852123405*m.b3199
                           - 0.0706858347057703*m.b3200 - 0.0962112750161874*m.b3201 - 0.125663706143592*m.b3202
                           - 0.159043128087983*m.b3203 - 0.196349540849362*m.b3204 - 0.282743338823081*m.b3205
                           - 0.38484510006475*m.b3206 - 0.502654824574367*m.b3207 == 0)

m.c1398 = Constraint(expr=   m.x767 - 0.00785398163397448*m.b3208 - 0.0122718463030851*m.b3209
                           - 0.0176714586764426*m.b3210 - 0.0314159265358979*m.b3211 - 0.0490873852123405*m.b3212
                           - 0.0706858347057703*m.b3213 - 0.0962112750161874*m.b3214 - 0.125663706143592*m.b3215
                           - 0.159043128087983*m.b3216 - 0.196349540849362*m.b3217 - 0.282743338823081*m.b3218
                           - 0.38484510006475*m.b3219 - 0.502654824574367*m.b3220 == 0)

m.c1399 = Constraint(expr=   m.x768 - 0.00785398163397448*m.b3221 - 0.0122718463030851*m.b3222
                           - 0.0176714586764426*m.b3223 - 0.0314159265358979*m.b3224 - 0.0490873852123405*m.b3225
                           - 0.0706858347057703*m.b3226 - 0.0962112750161874*m.b3227 - 0.125663706143592*m.b3228
                           - 0.159043128087983*m.b3229 - 0.196349540849362*m.b3230 - 0.282743338823081*m.b3231
                           - 0.38484510006475*m.b3232 - 0.502654824574367*m.b3233 == 0)

m.c1400 = Constraint(expr=   m.x769 - 0.00785398163397448*m.b3234 - 0.0122718463030851*m.b3235
                           - 0.0176714586764426*m.b3236 - 0.0314159265358979*m.b3237 - 0.0490873852123405*m.b3238
                           - 0.0706858347057703*m.b3239 - 0.0962112750161874*m.b3240 - 0.125663706143592*m.b3241
                           - 0.159043128087983*m.b3242 - 0.196349540849362*m.b3243 - 0.282743338823081*m.b3244
                           - 0.38484510006475*m.b3245 - 0.502654824574367*m.b3246 == 0)

m.c1401 = Constraint(expr=   m.x770 - 0.00785398163397448*m.b3247 - 0.0122718463030851*m.b3248
                           - 0.0176714586764426*m.b3249 - 0.0314159265358979*m.b3250 - 0.0490873852123405*m.b3251
                           - 0.0706858347057703*m.b3252 - 0.0962112750161874*m.b3253 - 0.125663706143592*m.b3254
                           - 0.159043128087983*m.b3255 - 0.196349540849362*m.b3256 - 0.282743338823081*m.b3257
                           - 0.38484510006475*m.b3258 - 0.502654824574367*m.b3259 == 0)

m.c1402 = Constraint(expr=   m.x771 - 0.00785398163397448*m.b3260 - 0.0122718463030851*m.b3261
                           - 0.0176714586764426*m.b3262 - 0.0314159265358979*m.b3263 - 0.0490873852123405*m.b3264
                           - 0.0706858347057703*m.b3265 - 0.0962112750161874*m.b3266 - 0.125663706143592*m.b3267
                           - 0.159043128087983*m.b3268 - 0.196349540849362*m.b3269 - 0.282743338823081*m.b3270
                           - 0.38484510006475*m.b3271 - 0.502654824574367*m.b3272 == 0)

m.c1403 = Constraint(expr=   m.x772 - 0.00785398163397448*m.b3273 - 0.0122718463030851*m.b3274
                           - 0.0176714586764426*m.b3275 - 0.0314159265358979*m.b3276 - 0.0490873852123405*m.b3277
                           - 0.0706858347057703*m.b3278 - 0.0962112750161874*m.b3279 - 0.125663706143592*m.b3280
                           - 0.159043128087983*m.b3281 - 0.196349540849362*m.b3282 - 0.282743338823081*m.b3283
                           - 0.38484510006475*m.b3284 - 0.502654824574367*m.b3285 == 0)

m.c1404 = Constraint(expr=   m.x773 - 0.00785398163397448*m.b3286 - 0.0122718463030851*m.b3287
                           - 0.0176714586764426*m.b3288 - 0.0314159265358979*m.b3289 - 0.0490873852123405*m.b3290
                           - 0.0706858347057703*m.b3291 - 0.0962112750161874*m.b3292 - 0.125663706143592*m.b3293
                           - 0.159043128087983*m.b3294 - 0.196349540849362*m.b3295 - 0.282743338823081*m.b3296
                           - 0.38484510006475*m.b3297 - 0.502654824574367*m.b3298 == 0)

m.c1405 = Constraint(expr=   m.x774 - 0.00785398163397448*m.b3299 - 0.0122718463030851*m.b3300
                           - 0.0176714586764426*m.b3301 - 0.0314159265358979*m.b3302 - 0.0490873852123405*m.b3303
                           - 0.0706858347057703*m.b3304 - 0.0962112750161874*m.b3305 - 0.125663706143592*m.b3306
                           - 0.159043128087983*m.b3307 - 0.196349540849362*m.b3308 - 0.282743338823081*m.b3309
                           - 0.38484510006475*m.b3310 - 0.502654824574367*m.b3311 == 0)

m.c1406 = Constraint(expr=   m.x775 - 0.00785398163397448*m.b3312 - 0.0122718463030851*m.b3313
                           - 0.0176714586764426*m.b3314 - 0.0314159265358979*m.b3315 - 0.0490873852123405*m.b3316
                           - 0.0706858347057703*m.b3317 - 0.0962112750161874*m.b3318 - 0.125663706143592*m.b3319
                           - 0.159043128087983*m.b3320 - 0.196349540849362*m.b3321 - 0.282743338823081*m.b3322
                           - 0.38484510006475*m.b3323 - 0.502654824574367*m.b3324 == 0)

m.c1407 = Constraint(expr=   m.x776 - 0.00785398163397448*m.b3325 - 0.0122718463030851*m.b3326
                           - 0.0176714586764426*m.b3327 - 0.0314159265358979*m.b3328 - 0.0490873852123405*m.b3329
                           - 0.0706858347057703*m.b3330 - 0.0962112750161874*m.b3331 - 0.125663706143592*m.b3332
                           - 0.159043128087983*m.b3333 - 0.196349540849362*m.b3334 - 0.282743338823081*m.b3335
                           - 0.38484510006475*m.b3336 - 0.502654824574367*m.b3337 == 0)

m.c1408 = Constraint(expr=   m.x777 - 0.00785398163397448*m.b3338 - 0.0122718463030851*m.b3339
                           - 0.0176714586764426*m.b3340 - 0.0314159265358979*m.b3341 - 0.0490873852123405*m.b3342
                           - 0.0706858347057703*m.b3343 - 0.0962112750161874*m.b3344 - 0.125663706143592*m.b3345
                           - 0.159043128087983*m.b3346 - 0.196349540849362*m.b3347 - 0.282743338823081*m.b3348
                           - 0.38484510006475*m.b3349 - 0.502654824574367*m.b3350 == 0)

m.c1409 = Constraint(expr=   m.x778 - 0.00785398163397448*m.b3351 - 0.0122718463030851*m.b3352
                           - 0.0176714586764426*m.b3353 - 0.0314159265358979*m.b3354 - 0.0490873852123405*m.b3355
                           - 0.0706858347057703*m.b3356 - 0.0962112750161874*m.b3357 - 0.125663706143592*m.b3358
                           - 0.159043128087983*m.b3359 - 0.196349540849362*m.b3360 - 0.282743338823081*m.b3361
                           - 0.38484510006475*m.b3362 - 0.502654824574367*m.b3363 == 0)

m.c1410 = Constraint(expr=   m.x779 - 0.00785398163397448*m.b3364 - 0.0122718463030851*m.b3365
                           - 0.0176714586764426*m.b3366 - 0.0314159265358979*m.b3367 - 0.0490873852123405*m.b3368
                           - 0.0706858347057703*m.b3369 - 0.0962112750161874*m.b3370 - 0.125663706143592*m.b3371
                           - 0.159043128087983*m.b3372 - 0.196349540849362*m.b3373 - 0.282743338823081*m.b3374
                           - 0.38484510006475*m.b3375 - 0.502654824574367*m.b3376 == 0)

m.c1411 = Constraint(expr=   m.x780 - 0.00785398163397448*m.b3377 - 0.0122718463030851*m.b3378
                           - 0.0176714586764426*m.b3379 - 0.0314159265358979*m.b3380 - 0.0490873852123405*m.b3381
                           - 0.0706858347057703*m.b3382 - 0.0962112750161874*m.b3383 - 0.125663706143592*m.b3384
                           - 0.159043128087983*m.b3385 - 0.196349540849362*m.b3386 - 0.282743338823081*m.b3387
                           - 0.38484510006475*m.b3388 - 0.502654824574367*m.b3389 == 0)

m.c1412 = Constraint(expr=   m.x781 - 0.00785398163397448*m.b3390 - 0.0122718463030851*m.b3391
                           - 0.0176714586764426*m.b3392 - 0.0314159265358979*m.b3393 - 0.0490873852123405*m.b3394
                           - 0.0706858347057703*m.b3395 - 0.0962112750161874*m.b3396 - 0.125663706143592*m.b3397
                           - 0.159043128087983*m.b3398 - 0.196349540849362*m.b3399 - 0.282743338823081*m.b3400
                           - 0.38484510006475*m.b3401 - 0.502654824574367*m.b3402 == 0)

m.c1413 = Constraint(expr=   m.x782 - 0.00785398163397448*m.b3403 - 0.0122718463030851*m.b3404
                           - 0.0176714586764426*m.b3405 - 0.0314159265358979*m.b3406 - 0.0490873852123405*m.b3407
                           - 0.0706858347057703*m.b3408 - 0.0962112750161874*m.b3409 - 0.125663706143592*m.b3410
                           - 0.159043128087983*m.b3411 - 0.196349540849362*m.b3412 - 0.282743338823081*m.b3413
                           - 0.38484510006475*m.b3414 - 0.502654824574367*m.b3415 == 0)

m.c1414 = Constraint(expr=   m.x783 - 0.00785398163397448*m.b3416 - 0.0122718463030851*m.b3417
                           - 0.0176714586764426*m.b3418 - 0.0314159265358979*m.b3419 - 0.0490873852123405*m.b3420
                           - 0.0706858347057703*m.b3421 - 0.0962112750161874*m.b3422 - 0.125663706143592*m.b3423
                           - 0.159043128087983*m.b3424 - 0.196349540849362*m.b3425 - 0.282743338823081*m.b3426
                           - 0.38484510006475*m.b3427 - 0.502654824574367*m.b3428 == 0)

m.c1415 = Constraint(expr=   m.x784 - 0.00785398163397448*m.b3429 - 0.0122718463030851*m.b3430
                           - 0.0176714586764426*m.b3431 - 0.0314159265358979*m.b3432 - 0.0490873852123405*m.b3433
                           - 0.0706858347057703*m.b3434 - 0.0962112750161874*m.b3435 - 0.125663706143592*m.b3436
                           - 0.159043128087983*m.b3437 - 0.196349540849362*m.b3438 - 0.282743338823081*m.b3439
                           - 0.38484510006475*m.b3440 - 0.502654824574367*m.b3441 == 0)

m.c1416 = Constraint(expr=   m.x785 - 0.00785398163397448*m.b3442 - 0.0122718463030851*m.b3443
                           - 0.0176714586764426*m.b3444 - 0.0314159265358979*m.b3445 - 0.0490873852123405*m.b3446
                           - 0.0706858347057703*m.b3447 - 0.0962112750161874*m.b3448 - 0.125663706143592*m.b3449
                           - 0.159043128087983*m.b3450 - 0.196349540849362*m.b3451 - 0.282743338823081*m.b3452
                           - 0.38484510006475*m.b3453 - 0.502654824574367*m.b3454 == 0)

m.c1417 = Constraint(expr=   m.x786 - 0.00785398163397448*m.b3455 - 0.0122718463030851*m.b3456
                           - 0.0176714586764426*m.b3457 - 0.0314159265358979*m.b3458 - 0.0490873852123405*m.b3459
                           - 0.0706858347057703*m.b3460 - 0.0962112750161874*m.b3461 - 0.125663706143592*m.b3462
                           - 0.159043128087983*m.b3463 - 0.196349540849362*m.b3464 - 0.282743338823081*m.b3465
                           - 0.38484510006475*m.b3466 - 0.502654824574367*m.b3467 == 0)

m.c1418 = Constraint(expr=   m.x787 - 0.00785398163397448*m.b3468 - 0.0122718463030851*m.b3469
                           - 0.0176714586764426*m.b3470 - 0.0314159265358979*m.b3471 - 0.0490873852123405*m.b3472
                           - 0.0706858347057703*m.b3473 - 0.0962112750161874*m.b3474 - 0.125663706143592*m.b3475
                           - 0.159043128087983*m.b3476 - 0.196349540849362*m.b3477 - 0.282743338823081*m.b3478
                           - 0.38484510006475*m.b3479 - 0.502654824574367*m.b3480 == 0)

m.c1419 = Constraint(expr=   m.x788 - 0.00785398163397448*m.b3481 - 0.0122718463030851*m.b3482
                           - 0.0176714586764426*m.b3483 - 0.0314159265358979*m.b3484 - 0.0490873852123405*m.b3485
                           - 0.0706858347057703*m.b3486 - 0.0962112750161874*m.b3487 - 0.125663706143592*m.b3488
                           - 0.159043128087983*m.b3489 - 0.196349540849362*m.b3490 - 0.282743338823081*m.b3491
                           - 0.38484510006475*m.b3492 - 0.502654824574367*m.b3493 == 0)

m.c1420 = Constraint(expr=   m.x789 - 0.00785398163397448*m.b3494 - 0.0122718463030851*m.b3495
                           - 0.0176714586764426*m.b3496 - 0.0314159265358979*m.b3497 - 0.0490873852123405*m.b3498
                           - 0.0706858347057703*m.b3499 - 0.0962112750161874*m.b3500 - 0.125663706143592*m.b3501
                           - 0.159043128087983*m.b3502 - 0.196349540849362*m.b3503 - 0.282743338823081*m.b3504
                           - 0.38484510006475*m.b3505 - 0.502654824574367*m.b3506 == 0)

m.c1421 = Constraint(expr=   m.x790 - 0.00785398163397448*m.b3507 - 0.0122718463030851*m.b3508
                           - 0.0176714586764426*m.b3509 - 0.0314159265358979*m.b3510 - 0.0490873852123405*m.b3511
                           - 0.0706858347057703*m.b3512 - 0.0962112750161874*m.b3513 - 0.125663706143592*m.b3514
                           - 0.159043128087983*m.b3515 - 0.196349540849362*m.b3516 - 0.282743338823081*m.b3517
                           - 0.38484510006475*m.b3518 - 0.502654824574367*m.b3519 == 0)

m.c1422 = Constraint(expr=   m.x791 - 0.00785398163397448*m.b3520 - 0.0122718463030851*m.b3521
                           - 0.0176714586764426*m.b3522 - 0.0314159265358979*m.b3523 - 0.0490873852123405*m.b3524
                           - 0.0706858347057703*m.b3525 - 0.0962112750161874*m.b3526 - 0.125663706143592*m.b3527
                           - 0.159043128087983*m.b3528 - 0.196349540849362*m.b3529 - 0.282743338823081*m.b3530
                           - 0.38484510006475*m.b3531 - 0.502654824574367*m.b3532 == 0)

m.c1423 = Constraint(expr=   m.x792 - 0.00785398163397448*m.b3533 - 0.0122718463030851*m.b3534
                           - 0.0176714586764426*m.b3535 - 0.0314159265358979*m.b3536 - 0.0490873852123405*m.b3537
                           - 0.0706858347057703*m.b3538 - 0.0962112750161874*m.b3539 - 0.125663706143592*m.b3540
                           - 0.159043128087983*m.b3541 - 0.196349540849362*m.b3542 - 0.282743338823081*m.b3543
                           - 0.38484510006475*m.b3544 - 0.502654824574367*m.b3545 == 0)

m.c1424 = Constraint(expr=   m.x793 - 0.00785398163397448*m.b3546 - 0.0122718463030851*m.b3547
                           - 0.0176714586764426*m.b3548 - 0.0314159265358979*m.b3549 - 0.0490873852123405*m.b3550
                           - 0.0706858347057703*m.b3551 - 0.0962112750161874*m.b3552 - 0.125663706143592*m.b3553
                           - 0.159043128087983*m.b3554 - 0.196349540849362*m.b3555 - 0.282743338823081*m.b3556
                           - 0.38484510006475*m.b3557 - 0.502654824574367*m.b3558 == 0)

m.c1425 = Constraint(expr=   m.x794 - 0.00785398163397448*m.b3559 - 0.0122718463030851*m.b3560
                           - 0.0176714586764426*m.b3561 - 0.0314159265358979*m.b3562 - 0.0490873852123405*m.b3563
                           - 0.0706858347057703*m.b3564 - 0.0962112750161874*m.b3565 - 0.125663706143592*m.b3566
                           - 0.159043128087983*m.b3567 - 0.196349540849362*m.b3568 - 0.282743338823081*m.b3569
                           - 0.38484510006475*m.b3570 - 0.502654824574367*m.b3571 == 0)

m.c1426 = Constraint(expr=   m.x795 - 0.00785398163397448*m.b3572 - 0.0122718463030851*m.b3573
                           - 0.0176714586764426*m.b3574 - 0.0314159265358979*m.b3575 - 0.0490873852123405*m.b3576
                           - 0.0706858347057703*m.b3577 - 0.0962112750161874*m.b3578 - 0.125663706143592*m.b3579
                           - 0.159043128087983*m.b3580 - 0.196349540849362*m.b3581 - 0.282743338823081*m.b3582
                           - 0.38484510006475*m.b3583 - 0.502654824574367*m.b3584 == 0)

m.c1427 = Constraint(expr=   m.x796 - 0.00785398163397448*m.b3585 - 0.0122718463030851*m.b3586
                           - 0.0176714586764426*m.b3587 - 0.0314159265358979*m.b3588 - 0.0490873852123405*m.b3589
                           - 0.0706858347057703*m.b3590 - 0.0962112750161874*m.b3591 - 0.125663706143592*m.b3592
                           - 0.159043128087983*m.b3593 - 0.196349540849362*m.b3594 - 0.282743338823081*m.b3595
                           - 0.38484510006475*m.b3596 - 0.502654824574367*m.b3597 == 0)

m.c1428 = Constraint(expr=   m.x797 - 0.00785398163397448*m.b3598 - 0.0122718463030851*m.b3599
                           - 0.0176714586764426*m.b3600 - 0.0314159265358979*m.b3601 - 0.0490873852123405*m.b3602
                           - 0.0706858347057703*m.b3603 - 0.0962112750161874*m.b3604 - 0.125663706143592*m.b3605
                           - 0.159043128087983*m.b3606 - 0.196349540849362*m.b3607 - 0.282743338823081*m.b3608
                           - 0.38484510006475*m.b3609 - 0.502654824574367*m.b3610 == 0)

m.c1429 = Constraint(expr=   m.x798 - 0.00785398163397448*m.b3611 - 0.0122718463030851*m.b3612
                           - 0.0176714586764426*m.b3613 - 0.0314159265358979*m.b3614 - 0.0490873852123405*m.b3615
                           - 0.0706858347057703*m.b3616 - 0.0962112750161874*m.b3617 - 0.125663706143592*m.b3618
                           - 0.159043128087983*m.b3619 - 0.196349540849362*m.b3620 - 0.282743338823081*m.b3621
                           - 0.38484510006475*m.b3622 - 0.502654824574367*m.b3623 == 0)

m.c1430 = Constraint(expr=   m.x799 - 0.00785398163397448*m.b3624 - 0.0122718463030851*m.b3625
                           - 0.0176714586764426*m.b3626 - 0.0314159265358979*m.b3627 - 0.0490873852123405*m.b3628
                           - 0.0706858347057703*m.b3629 - 0.0962112750161874*m.b3630 - 0.125663706143592*m.b3631
                           - 0.159043128087983*m.b3632 - 0.196349540849362*m.b3633 - 0.282743338823081*m.b3634
                           - 0.38484510006475*m.b3635 - 0.502654824574367*m.b3636 == 0)

m.c1431 = Constraint(expr=   m.x800 - 0.00785398163397448*m.b3637 - 0.0122718463030851*m.b3638
                           - 0.0176714586764426*m.b3639 - 0.0314159265358979*m.b3640 - 0.0490873852123405*m.b3641
                           - 0.0706858347057703*m.b3642 - 0.0962112750161874*m.b3643 - 0.125663706143592*m.b3644
                           - 0.159043128087983*m.b3645 - 0.196349540849362*m.b3646 - 0.282743338823081*m.b3647
                           - 0.38484510006475*m.b3648 - 0.502654824574367*m.b3649 == 0)

m.c1432 = Constraint(expr=   m.x801 - 0.00785398163397448*m.b3650 - 0.0122718463030851*m.b3651
                           - 0.0176714586764426*m.b3652 - 0.0314159265358979*m.b3653 - 0.0490873852123405*m.b3654
                           - 0.0706858347057703*m.b3655 - 0.0962112750161874*m.b3656 - 0.125663706143592*m.b3657
                           - 0.159043128087983*m.b3658 - 0.196349540849362*m.b3659 - 0.282743338823081*m.b3660
                           - 0.38484510006475*m.b3661 - 0.502654824574367*m.b3662 == 0)

m.c1433 = Constraint(expr=   m.x802 - 0.00785398163397448*m.b3663 - 0.0122718463030851*m.b3664
                           - 0.0176714586764426*m.b3665 - 0.0314159265358979*m.b3666 - 0.0490873852123405*m.b3667
                           - 0.0706858347057703*m.b3668 - 0.0962112750161874*m.b3669 - 0.125663706143592*m.b3670
                           - 0.159043128087983*m.b3671 - 0.196349540849362*m.b3672 - 0.282743338823081*m.b3673
                           - 0.38484510006475*m.b3674 - 0.502654824574367*m.b3675 == 0)

m.c1434 = Constraint(expr=   m.x803 - 0.00785398163397448*m.b3676 - 0.0122718463030851*m.b3677
                           - 0.0176714586764426*m.b3678 - 0.0314159265358979*m.b3679 - 0.0490873852123405*m.b3680
                           - 0.0706858347057703*m.b3681 - 0.0962112750161874*m.b3682 - 0.125663706143592*m.b3683
                           - 0.159043128087983*m.b3684 - 0.196349540849362*m.b3685 - 0.282743338823081*m.b3686
                           - 0.38484510006475*m.b3687 - 0.502654824574367*m.b3688 == 0)

m.c1435 = Constraint(expr=   m.x804 - 0.00785398163397448*m.b3689 - 0.0122718463030851*m.b3690
                           - 0.0176714586764426*m.b3691 - 0.0314159265358979*m.b3692 - 0.0490873852123405*m.b3693
                           - 0.0706858347057703*m.b3694 - 0.0962112750161874*m.b3695 - 0.125663706143592*m.b3696
                           - 0.159043128087983*m.b3697 - 0.196349540849362*m.b3698 - 0.282743338823081*m.b3699
                           - 0.38484510006475*m.b3700 - 0.502654824574367*m.b3701 == 0)

m.c1436 = Constraint(expr=   m.x805 - 0.00785398163397448*m.b3702 - 0.0122718463030851*m.b3703
                           - 0.0176714586764426*m.b3704 - 0.0314159265358979*m.b3705 - 0.0490873852123405*m.b3706
                           - 0.0706858347057703*m.b3707 - 0.0962112750161874*m.b3708 - 0.125663706143592*m.b3709
                           - 0.159043128087983*m.b3710 - 0.196349540849362*m.b3711 - 0.282743338823081*m.b3712
                           - 0.38484510006475*m.b3713 - 0.502654824574367*m.b3714 == 0)

m.c1437 = Constraint(expr=   m.x806 - 0.00785398163397448*m.b3715 - 0.0122718463030851*m.b3716
                           - 0.0176714586764426*m.b3717 - 0.0314159265358979*m.b3718 - 0.0490873852123405*m.b3719
                           - 0.0706858347057703*m.b3720 - 0.0962112750161874*m.b3721 - 0.125663706143592*m.b3722
                           - 0.159043128087983*m.b3723 - 0.196349540849362*m.b3724 - 0.282743338823081*m.b3725
                           - 0.38484510006475*m.b3726 - 0.502654824574367*m.b3727 == 0)

m.c1438 = Constraint(expr=   m.x807 - 0.00785398163397448*m.b3728 - 0.0122718463030851*m.b3729
                           - 0.0176714586764426*m.b3730 - 0.0314159265358979*m.b3731 - 0.0490873852123405*m.b3732
                           - 0.0706858347057703*m.b3733 - 0.0962112750161874*m.b3734 - 0.125663706143592*m.b3735
                           - 0.159043128087983*m.b3736 - 0.196349540849362*m.b3737 - 0.282743338823081*m.b3738
                           - 0.38484510006475*m.b3739 - 0.502654824574367*m.b3740 == 0)

m.c1439 = Constraint(expr=   m.x808 - 0.00785398163397448*m.b3741 - 0.0122718463030851*m.b3742
                           - 0.0176714586764426*m.b3743 - 0.0314159265358979*m.b3744 - 0.0490873852123405*m.b3745
                           - 0.0706858347057703*m.b3746 - 0.0962112750161874*m.b3747 - 0.125663706143592*m.b3748
                           - 0.159043128087983*m.b3749 - 0.196349540849362*m.b3750 - 0.282743338823081*m.b3751
                           - 0.38484510006475*m.b3752 - 0.502654824574367*m.b3753 == 0)

m.c1440 = Constraint(expr=   m.x809 - 0.00785398163397448*m.b3754 - 0.0122718463030851*m.b3755
                           - 0.0176714586764426*m.b3756 - 0.0314159265358979*m.b3757 - 0.0490873852123405*m.b3758
                           - 0.0706858347057703*m.b3759 - 0.0962112750161874*m.b3760 - 0.125663706143592*m.b3761
                           - 0.159043128087983*m.b3762 - 0.196349540849362*m.b3763 - 0.282743338823081*m.b3764
                           - 0.38484510006475*m.b3765 - 0.502654824574367*m.b3766 == 0)

m.c1441 = Constraint(expr=   m.x810 - 0.00785398163397448*m.b3767 - 0.0122718463030851*m.b3768
                           - 0.0176714586764426*m.b3769 - 0.0314159265358979*m.b3770 - 0.0490873852123405*m.b3771
                           - 0.0706858347057703*m.b3772 - 0.0962112750161874*m.b3773 - 0.125663706143592*m.b3774
                           - 0.159043128087983*m.b3775 - 0.196349540849362*m.b3776 - 0.282743338823081*m.b3777
                           - 0.38484510006475*m.b3778 - 0.502654824574367*m.b3779 == 0)

m.c1442 = Constraint(expr=   m.x811 - 0.00785398163397448*m.b3780 - 0.0122718463030851*m.b3781
                           - 0.0176714586764426*m.b3782 - 0.0314159265358979*m.b3783 - 0.0490873852123405*m.b3784
                           - 0.0706858347057703*m.b3785 - 0.0962112750161874*m.b3786 - 0.125663706143592*m.b3787
                           - 0.159043128087983*m.b3788 - 0.196349540849362*m.b3789 - 0.282743338823081*m.b3790
                           - 0.38484510006475*m.b3791 - 0.502654824574367*m.b3792 == 0)

m.c1443 = Constraint(expr=   m.x812 - 0.00785398163397448*m.b3793 - 0.0122718463030851*m.b3794
                           - 0.0176714586764426*m.b3795 - 0.0314159265358979*m.b3796 - 0.0490873852123405*m.b3797
                           - 0.0706858347057703*m.b3798 - 0.0962112750161874*m.b3799 - 0.125663706143592*m.b3800
                           - 0.159043128087983*m.b3801 - 0.196349540849362*m.b3802 - 0.282743338823081*m.b3803
                           - 0.38484510006475*m.b3804 - 0.502654824574367*m.b3805 == 0)

m.c1444 = Constraint(expr=   m.x813 - 0.00785398163397448*m.b3806 - 0.0122718463030851*m.b3807
                           - 0.0176714586764426*m.b3808 - 0.0314159265358979*m.b3809 - 0.0490873852123405*m.b3810
                           - 0.0706858347057703*m.b3811 - 0.0962112750161874*m.b3812 - 0.125663706143592*m.b3813
                           - 0.159043128087983*m.b3814 - 0.196349540849362*m.b3815 - 0.282743338823081*m.b3816
                           - 0.38484510006475*m.b3817 - 0.502654824574367*m.b3818 == 0)

m.c1445 = Constraint(expr=   m.x814 - 0.00785398163397448*m.b3819 - 0.0122718463030851*m.b3820
                           - 0.0176714586764426*m.b3821 - 0.0314159265358979*m.b3822 - 0.0490873852123405*m.b3823
                           - 0.0706858347057703*m.b3824 - 0.0962112750161874*m.b3825 - 0.125663706143592*m.b3826
                           - 0.159043128087983*m.b3827 - 0.196349540849362*m.b3828 - 0.282743338823081*m.b3829
                           - 0.38484510006475*m.b3830 - 0.502654824574367*m.b3831 == 0)

m.c1446 = Constraint(expr=   m.x815 - 0.00785398163397448*m.b3832 - 0.0122718463030851*m.b3833
                           - 0.0176714586764426*m.b3834 - 0.0314159265358979*m.b3835 - 0.0490873852123405*m.b3836
                           - 0.0706858347057703*m.b3837 - 0.0962112750161874*m.b3838 - 0.125663706143592*m.b3839
                           - 0.159043128087983*m.b3840 - 0.196349540849362*m.b3841 - 0.282743338823081*m.b3842
                           - 0.38484510006475*m.b3843 - 0.502654824574367*m.b3844 == 0)

m.c1447 = Constraint(expr=   m.x816 - 0.00785398163397448*m.b3845 - 0.0122718463030851*m.b3846
                           - 0.0176714586764426*m.b3847 - 0.0314159265358979*m.b3848 - 0.0490873852123405*m.b3849
                           - 0.0706858347057703*m.b3850 - 0.0962112750161874*m.b3851 - 0.125663706143592*m.b3852
                           - 0.159043128087983*m.b3853 - 0.196349540849362*m.b3854 - 0.282743338823081*m.b3855
                           - 0.38484510006475*m.b3856 - 0.502654824574367*m.b3857 == 0)

m.c1448 = Constraint(expr=   m.x817 - 0.00785398163397448*m.b3858 - 0.0122718463030851*m.b3859
                           - 0.0176714586764426*m.b3860 - 0.0314159265358979*m.b3861 - 0.0490873852123405*m.b3862
                           - 0.0706858347057703*m.b3863 - 0.0962112750161874*m.b3864 - 0.125663706143592*m.b3865
                           - 0.159043128087983*m.b3866 - 0.196349540849362*m.b3867 - 0.282743338823081*m.b3868
                           - 0.38484510006475*m.b3869 - 0.502654824574367*m.b3870 == 0)

m.c1449 = Constraint(expr=   m.x818 - 0.00785398163397448*m.b3871 - 0.0122718463030851*m.b3872
                           - 0.0176714586764426*m.b3873 - 0.0314159265358979*m.b3874 - 0.0490873852123405*m.b3875
                           - 0.0706858347057703*m.b3876 - 0.0962112750161874*m.b3877 - 0.125663706143592*m.b3878
                           - 0.159043128087983*m.b3879 - 0.196349540849362*m.b3880 - 0.282743338823081*m.b3881
                           - 0.38484510006475*m.b3882 - 0.502654824574367*m.b3883 == 0)

m.c1450 = Constraint(expr=   m.x819 - 0.00785398163397448*m.b3884 - 0.0122718463030851*m.b3885
                           - 0.0176714586764426*m.b3886 - 0.0314159265358979*m.b3887 - 0.0490873852123405*m.b3888
                           - 0.0706858347057703*m.b3889 - 0.0962112750161874*m.b3890 - 0.125663706143592*m.b3891
                           - 0.159043128087983*m.b3892 - 0.196349540849362*m.b3893 - 0.282743338823081*m.b3894
                           - 0.38484510006475*m.b3895 - 0.502654824574367*m.b3896 == 0)

m.c1451 = Constraint(expr=   m.x820 - 0.00785398163397448*m.b3897 - 0.0122718463030851*m.b3898
                           - 0.0176714586764426*m.b3899 - 0.0314159265358979*m.b3900 - 0.0490873852123405*m.b3901
                           - 0.0706858347057703*m.b3902 - 0.0962112750161874*m.b3903 - 0.125663706143592*m.b3904
                           - 0.159043128087983*m.b3905 - 0.196349540849362*m.b3906 - 0.282743338823081*m.b3907
                           - 0.38484510006475*m.b3908 - 0.502654824574367*m.b3909 == 0)

m.c1452 = Constraint(expr=   m.x821 - 0.00785398163397448*m.b3910 - 0.0122718463030851*m.b3911
                           - 0.0176714586764426*m.b3912 - 0.0314159265358979*m.b3913 - 0.0490873852123405*m.b3914
                           - 0.0706858347057703*m.b3915 - 0.0962112750161874*m.b3916 - 0.125663706143592*m.b3917
                           - 0.159043128087983*m.b3918 - 0.196349540849362*m.b3919 - 0.282743338823081*m.b3920
                           - 0.38484510006475*m.b3921 - 0.502654824574367*m.b3922 == 0)

m.c1453 = Constraint(expr=   m.x822 - 0.00785398163397448*m.b3923 - 0.0122718463030851*m.b3924
                           - 0.0176714586764426*m.b3925 - 0.0314159265358979*m.b3926 - 0.0490873852123405*m.b3927
                           - 0.0706858347057703*m.b3928 - 0.0962112750161874*m.b3929 - 0.125663706143592*m.b3930
                           - 0.159043128087983*m.b3931 - 0.196349540849362*m.b3932 - 0.282743338823081*m.b3933
                           - 0.38484510006475*m.b3934 - 0.502654824574367*m.b3935 == 0)

m.c1454 = Constraint(expr=   m.x823 - 0.00785398163397448*m.b3936 - 0.0122718463030851*m.b3937
                           - 0.0176714586764426*m.b3938 - 0.0314159265358979*m.b3939 - 0.0490873852123405*m.b3940
                           - 0.0706858347057703*m.b3941 - 0.0962112750161874*m.b3942 - 0.125663706143592*m.b3943
                           - 0.159043128087983*m.b3944 - 0.196349540849362*m.b3945 - 0.282743338823081*m.b3946
                           - 0.38484510006475*m.b3947 - 0.502654824574367*m.b3948 == 0)

m.c1455 = Constraint(expr=   m.x824 - 0.00785398163397448*m.b3949 - 0.0122718463030851*m.b3950
                           - 0.0176714586764426*m.b3951 - 0.0314159265358979*m.b3952 - 0.0490873852123405*m.b3953
                           - 0.0706858347057703*m.b3954 - 0.0962112750161874*m.b3955 - 0.125663706143592*m.b3956
                           - 0.159043128087983*m.b3957 - 0.196349540849362*m.b3958 - 0.282743338823081*m.b3959
                           - 0.38484510006475*m.b3960 - 0.502654824574367*m.b3961 == 0)

m.c1456 = Constraint(expr=   m.x825 - 0.00785398163397448*m.b3962 - 0.0122718463030851*m.b3963
                           - 0.0176714586764426*m.b3964 - 0.0314159265358979*m.b3965 - 0.0490873852123405*m.b3966
                           - 0.0706858347057703*m.b3967 - 0.0962112750161874*m.b3968 - 0.125663706143592*m.b3969
                           - 0.159043128087983*m.b3970 - 0.196349540849362*m.b3971 - 0.282743338823081*m.b3972
                           - 0.38484510006475*m.b3973 - 0.502654824574367*m.b3974 == 0)

m.c1457 = Constraint(expr=   m.x826 - 0.00785398163397448*m.b3975 - 0.0122718463030851*m.b3976
                           - 0.0176714586764426*m.b3977 - 0.0314159265358979*m.b3978 - 0.0490873852123405*m.b3979
                           - 0.0706858347057703*m.b3980 - 0.0962112750161874*m.b3981 - 0.125663706143592*m.b3982
                           - 0.159043128087983*m.b3983 - 0.196349540849362*m.b3984 - 0.282743338823081*m.b3985
                           - 0.38484510006475*m.b3986 - 0.502654824574367*m.b3987 == 0)

m.c1458 = Constraint(expr=   m.x827 - 0.00785398163397448*m.b3988 - 0.0122718463030851*m.b3989
                           - 0.0176714586764426*m.b3990 - 0.0314159265358979*m.b3991 - 0.0490873852123405*m.b3992
                           - 0.0706858347057703*m.b3993 - 0.0962112750161874*m.b3994 - 0.125663706143592*m.b3995
                           - 0.159043128087983*m.b3996 - 0.196349540849362*m.b3997 - 0.282743338823081*m.b3998
                           - 0.38484510006475*m.b3999 - 0.502654824574367*m.b4000 == 0)

m.c1459 = Constraint(expr=   m.x828 - 0.00785398163397448*m.b4001 - 0.0122718463030851*m.b4002
                           - 0.0176714586764426*m.b4003 - 0.0314159265358979*m.b4004 - 0.0490873852123405*m.b4005
                           - 0.0706858347057703*m.b4006 - 0.0962112750161874*m.b4007 - 0.125663706143592*m.b4008
                           - 0.159043128087983*m.b4009 - 0.196349540849362*m.b4010 - 0.282743338823081*m.b4011
                           - 0.38484510006475*m.b4012 - 0.502654824574367*m.b4013 == 0)

m.c1460 = Constraint(expr=   m.x829 - 0.00785398163397448*m.b4014 - 0.0122718463030851*m.b4015
                           - 0.0176714586764426*m.b4016 - 0.0314159265358979*m.b4017 - 0.0490873852123405*m.b4018
                           - 0.0706858347057703*m.b4019 - 0.0962112750161874*m.b4020 - 0.125663706143592*m.b4021
                           - 0.159043128087983*m.b4022 - 0.196349540849362*m.b4023 - 0.282743338823081*m.b4024
                           - 0.38484510006475*m.b4025 - 0.502654824574367*m.b4026 == 0)

m.c1461 = Constraint(expr=   m.x830 - 0.00785398163397448*m.b4027 - 0.0122718463030851*m.b4028
                           - 0.0176714586764426*m.b4029 - 0.0314159265358979*m.b4030 - 0.0490873852123405*m.b4031
                           - 0.0706858347057703*m.b4032 - 0.0962112750161874*m.b4033 - 0.125663706143592*m.b4034
                           - 0.159043128087983*m.b4035 - 0.196349540849362*m.b4036 - 0.282743338823081*m.b4037
                           - 0.38484510006475*m.b4038 - 0.502654824574367*m.b4039 == 0)

m.c1462 = Constraint(expr=   m.x831 - 0.00785398163397448*m.b4040 - 0.0122718463030851*m.b4041
                           - 0.0176714586764426*m.b4042 - 0.0314159265358979*m.b4043 - 0.0490873852123405*m.b4044
                           - 0.0706858347057703*m.b4045 - 0.0962112750161874*m.b4046 - 0.125663706143592*m.b4047
                           - 0.159043128087983*m.b4048 - 0.196349540849362*m.b4049 - 0.282743338823081*m.b4050
                           - 0.38484510006475*m.b4051 - 0.502654824574367*m.b4052 == 0)

m.c1463 = Constraint(expr=   m.x832 - 0.00785398163397448*m.b4053 - 0.0122718463030851*m.b4054
                           - 0.0176714586764426*m.b4055 - 0.0314159265358979*m.b4056 - 0.0490873852123405*m.b4057
                           - 0.0706858347057703*m.b4058 - 0.0962112750161874*m.b4059 - 0.125663706143592*m.b4060
                           - 0.159043128087983*m.b4061 - 0.196349540849362*m.b4062 - 0.282743338823081*m.b4063
                           - 0.38484510006475*m.b4064 - 0.502654824574367*m.b4065 == 0)

m.c1464 = Constraint(expr=   m.x833 - 0.00785398163397448*m.b4066 - 0.0122718463030851*m.b4067
                           - 0.0176714586764426*m.b4068 - 0.0314159265358979*m.b4069 - 0.0490873852123405*m.b4070
                           - 0.0706858347057703*m.b4071 - 0.0962112750161874*m.b4072 - 0.125663706143592*m.b4073
                           - 0.159043128087983*m.b4074 - 0.196349540849362*m.b4075 - 0.282743338823081*m.b4076
                           - 0.38484510006475*m.b4077 - 0.502654824574367*m.b4078 == 0)

m.c1465 = Constraint(expr=   m.x834 - 0.00785398163397448*m.b4079 - 0.0122718463030851*m.b4080
                           - 0.0176714586764426*m.b4081 - 0.0314159265358979*m.b4082 - 0.0490873852123405*m.b4083
                           - 0.0706858347057703*m.b4084 - 0.0962112750161874*m.b4085 - 0.125663706143592*m.b4086
                           - 0.159043128087983*m.b4087 - 0.196349540849362*m.b4088 - 0.282743338823081*m.b4089
                           - 0.38484510006475*m.b4090 - 0.502654824574367*m.b4091 == 0)

m.c1466 = Constraint(expr=   m.x835 - 0.00785398163397448*m.b4092 - 0.0122718463030851*m.b4093
                           - 0.0176714586764426*m.b4094 - 0.0314159265358979*m.b4095 - 0.0490873852123405*m.b4096
                           - 0.0706858347057703*m.b4097 - 0.0962112750161874*m.b4098 - 0.125663706143592*m.b4099
                           - 0.159043128087983*m.b4100 - 0.196349540849362*m.b4101 - 0.282743338823081*m.b4102
                           - 0.38484510006475*m.b4103 - 0.502654824574367*m.b4104 == 0)

m.c1467 = Constraint(expr=   m.x836 - 0.00785398163397448*m.b4105 - 0.0122718463030851*m.b4106
                           - 0.0176714586764426*m.b4107 - 0.0314159265358979*m.b4108 - 0.0490873852123405*m.b4109
                           - 0.0706858347057703*m.b4110 - 0.0962112750161874*m.b4111 - 0.125663706143592*m.b4112
                           - 0.159043128087983*m.b4113 - 0.196349540849362*m.b4114 - 0.282743338823081*m.b4115
                           - 0.38484510006475*m.b4116 - 0.502654824574367*m.b4117 == 0)

m.c1468 = Constraint(expr=   m.x837 - 0.00785398163397448*m.b4118 - 0.0122718463030851*m.b4119
                           - 0.0176714586764426*m.b4120 - 0.0314159265358979*m.b4121 - 0.0490873852123405*m.b4122
                           - 0.0706858347057703*m.b4123 - 0.0962112750161874*m.b4124 - 0.125663706143592*m.b4125
                           - 0.159043128087983*m.b4126 - 0.196349540849362*m.b4127 - 0.282743338823081*m.b4128
                           - 0.38484510006475*m.b4129 - 0.502654824574367*m.b4130 == 0)

m.c1469 = Constraint(expr=   m.x838 - 0.00785398163397448*m.b4131 - 0.0122718463030851*m.b4132
                           - 0.0176714586764426*m.b4133 - 0.0314159265358979*m.b4134 - 0.0490873852123405*m.b4135
                           - 0.0706858347057703*m.b4136 - 0.0962112750161874*m.b4137 - 0.125663706143592*m.b4138
                           - 0.159043128087983*m.b4139 - 0.196349540849362*m.b4140 - 0.282743338823081*m.b4141
                           - 0.38484510006475*m.b4142 - 0.502654824574367*m.b4143 == 0)

m.c1470 = Constraint(expr=   m.x839 - 0.00785398163397448*m.b4144 - 0.0122718463030851*m.b4145
                           - 0.0176714586764426*m.b4146 - 0.0314159265358979*m.b4147 - 0.0490873852123405*m.b4148
                           - 0.0706858347057703*m.b4149 - 0.0962112750161874*m.b4150 - 0.125663706143592*m.b4151
                           - 0.159043128087983*m.b4152 - 0.196349540849362*m.b4153 - 0.282743338823081*m.b4154
                           - 0.38484510006475*m.b4155 - 0.502654824574367*m.b4156 == 0)

m.c1471 = Constraint(expr=   m.x840 - 0.00785398163397448*m.b4157 - 0.0122718463030851*m.b4158
                           - 0.0176714586764426*m.b4159 - 0.0314159265358979*m.b4160 - 0.0490873852123405*m.b4161
                           - 0.0706858347057703*m.b4162 - 0.0962112750161874*m.b4163 - 0.125663706143592*m.b4164
                           - 0.159043128087983*m.b4165 - 0.196349540849362*m.b4166 - 0.282743338823081*m.b4167
                           - 0.38484510006475*m.b4168 - 0.502654824574367*m.b4169 == 0)

m.c1472 = Constraint(expr=   m.x841 - 0.00785398163397448*m.b4170 - 0.0122718463030851*m.b4171
                           - 0.0176714586764426*m.b4172 - 0.0314159265358979*m.b4173 - 0.0490873852123405*m.b4174
                           - 0.0706858347057703*m.b4175 - 0.0962112750161874*m.b4176 - 0.125663706143592*m.b4177
                           - 0.159043128087983*m.b4178 - 0.196349540849362*m.b4179 - 0.282743338823081*m.b4180
                           - 0.38484510006475*m.b4181 - 0.502654824574367*m.b4182 == 0)

m.c1473 = Constraint(expr=   m.x842 - 0.00785398163397448*m.b4183 - 0.0122718463030851*m.b4184
                           - 0.0176714586764426*m.b4185 - 0.0314159265358979*m.b4186 - 0.0490873852123405*m.b4187
                           - 0.0706858347057703*m.b4188 - 0.0962112750161874*m.b4189 - 0.125663706143592*m.b4190
                           - 0.159043128087983*m.b4191 - 0.196349540849362*m.b4192 - 0.282743338823081*m.b4193
                           - 0.38484510006475*m.b4194 - 0.502654824574367*m.b4195 == 0)

m.c1474 = Constraint(expr=   m.x843 - 0.00785398163397448*m.b4196 - 0.0122718463030851*m.b4197
                           - 0.0176714586764426*m.b4198 - 0.0314159265358979*m.b4199 - 0.0490873852123405*m.b4200
                           - 0.0706858347057703*m.b4201 - 0.0962112750161874*m.b4202 - 0.125663706143592*m.b4203
                           - 0.159043128087983*m.b4204 - 0.196349540849362*m.b4205 - 0.282743338823081*m.b4206
                           - 0.38484510006475*m.b4207 - 0.502654824574367*m.b4208 == 0)

m.c1475 = Constraint(expr=   m.x844 - 0.00785398163397448*m.b4209 - 0.0122718463030851*m.b4210
                           - 0.0176714586764426*m.b4211 - 0.0314159265358979*m.b4212 - 0.0490873852123405*m.b4213
                           - 0.0706858347057703*m.b4214 - 0.0962112750161874*m.b4215 - 0.125663706143592*m.b4216
                           - 0.159043128087983*m.b4217 - 0.196349540849362*m.b4218 - 0.282743338823081*m.b4219
                           - 0.38484510006475*m.b4220 - 0.502654824574367*m.b4221 == 0)

m.c1476 = Constraint(expr=   m.x845 - 0.00785398163397448*m.b4222 - 0.0122718463030851*m.b4223
                           - 0.0176714586764426*m.b4224 - 0.0314159265358979*m.b4225 - 0.0490873852123405*m.b4226
                           - 0.0706858347057703*m.b4227 - 0.0962112750161874*m.b4228 - 0.125663706143592*m.b4229
                           - 0.159043128087983*m.b4230 - 0.196349540849362*m.b4231 - 0.282743338823081*m.b4232
                           - 0.38484510006475*m.b4233 - 0.502654824574367*m.b4234 == 0)

m.c1477 = Constraint(expr=   m.x846 - 0.00785398163397448*m.b4235 - 0.0122718463030851*m.b4236
                           - 0.0176714586764426*m.b4237 - 0.0314159265358979*m.b4238 - 0.0490873852123405*m.b4239
                           - 0.0706858347057703*m.b4240 - 0.0962112750161874*m.b4241 - 0.125663706143592*m.b4242
                           - 0.159043128087983*m.b4243 - 0.196349540849362*m.b4244 - 0.282743338823081*m.b4245
                           - 0.38484510006475*m.b4246 - 0.502654824574367*m.b4247 == 0)

m.c1478 = Constraint(expr=   m.x847 - 0.00785398163397448*m.b4248 - 0.0122718463030851*m.b4249
                           - 0.0176714586764426*m.b4250 - 0.0314159265358979*m.b4251 - 0.0490873852123405*m.b4252
                           - 0.0706858347057703*m.b4253 - 0.0962112750161874*m.b4254 - 0.125663706143592*m.b4255
                           - 0.159043128087983*m.b4256 - 0.196349540849362*m.b4257 - 0.282743338823081*m.b4258
                           - 0.38484510006475*m.b4259 - 0.502654824574367*m.b4260 == 0)

m.c1479 = Constraint(expr=   m.x848 - 0.00785398163397448*m.b4261 - 0.0122718463030851*m.b4262
                           - 0.0176714586764426*m.b4263 - 0.0314159265358979*m.b4264 - 0.0490873852123405*m.b4265
                           - 0.0706858347057703*m.b4266 - 0.0962112750161874*m.b4267 - 0.125663706143592*m.b4268
                           - 0.159043128087983*m.b4269 - 0.196349540849362*m.b4270 - 0.282743338823081*m.b4271
                           - 0.38484510006475*m.b4272 - 0.502654824574367*m.b4273 == 0)

m.c1480 = Constraint(expr=   m.x849 - 0.00785398163397448*m.b4274 - 0.0122718463030851*m.b4275
                           - 0.0176714586764426*m.b4276 - 0.0314159265358979*m.b4277 - 0.0490873852123405*m.b4278
                           - 0.0706858347057703*m.b4279 - 0.0962112750161874*m.b4280 - 0.125663706143592*m.b4281
                           - 0.159043128087983*m.b4282 - 0.196349540849362*m.b4283 - 0.282743338823081*m.b4284
                           - 0.38484510006475*m.b4285 - 0.502654824574367*m.b4286 == 0)

m.c1481 = Constraint(expr=   m.x850 - 0.00785398163397448*m.b4287 - 0.0122718463030851*m.b4288
                           - 0.0176714586764426*m.b4289 - 0.0314159265358979*m.b4290 - 0.0490873852123405*m.b4291
                           - 0.0706858347057703*m.b4292 - 0.0962112750161874*m.b4293 - 0.125663706143592*m.b4294
                           - 0.159043128087983*m.b4295 - 0.196349540849362*m.b4296 - 0.282743338823081*m.b4297
                           - 0.38484510006475*m.b4298 - 0.502654824574367*m.b4299 == 0)

m.c1482 = Constraint(expr=   m.x851 - 0.00785398163397448*m.b4300 - 0.0122718463030851*m.b4301
                           - 0.0176714586764426*m.b4302 - 0.0314159265358979*m.b4303 - 0.0490873852123405*m.b4304
                           - 0.0706858347057703*m.b4305 - 0.0962112750161874*m.b4306 - 0.125663706143592*m.b4307
                           - 0.159043128087983*m.b4308 - 0.196349540849362*m.b4309 - 0.282743338823081*m.b4310
                           - 0.38484510006475*m.b4311 - 0.502654824574367*m.b4312 == 0)

m.c1483 = Constraint(expr=   m.x852 - 0.00785398163397448*m.b4313 - 0.0122718463030851*m.b4314
                           - 0.0176714586764426*m.b4315 - 0.0314159265358979*m.b4316 - 0.0490873852123405*m.b4317
                           - 0.0706858347057703*m.b4318 - 0.0962112750161874*m.b4319 - 0.125663706143592*m.b4320
                           - 0.159043128087983*m.b4321 - 0.196349540849362*m.b4322 - 0.282743338823081*m.b4323
                           - 0.38484510006475*m.b4324 - 0.502654824574367*m.b4325 == 0)

m.c1484 = Constraint(expr=   m.x853 - 0.00785398163397448*m.b4326 - 0.0122718463030851*m.b4327
                           - 0.0176714586764426*m.b4328 - 0.0314159265358979*m.b4329 - 0.0490873852123405*m.b4330
                           - 0.0706858347057703*m.b4331 - 0.0962112750161874*m.b4332 - 0.125663706143592*m.b4333
                           - 0.159043128087983*m.b4334 - 0.196349540849362*m.b4335 - 0.282743338823081*m.b4336
                           - 0.38484510006475*m.b4337 - 0.502654824574367*m.b4338 == 0)

m.c1485 = Constraint(expr=   m.x854 - 0.00785398163397448*m.b4339 - 0.0122718463030851*m.b4340
                           - 0.0176714586764426*m.b4341 - 0.0314159265358979*m.b4342 - 0.0490873852123405*m.b4343
                           - 0.0706858347057703*m.b4344 - 0.0962112750161874*m.b4345 - 0.125663706143592*m.b4346
                           - 0.159043128087983*m.b4347 - 0.196349540849362*m.b4348 - 0.282743338823081*m.b4349
                           - 0.38484510006475*m.b4350 - 0.502654824574367*m.b4351 == 0)

m.c1486 = Constraint(expr=   m.x855 - 0.00785398163397448*m.b4352 - 0.0122718463030851*m.b4353
                           - 0.0176714586764426*m.b4354 - 0.0314159265358979*m.b4355 - 0.0490873852123405*m.b4356
                           - 0.0706858347057703*m.b4357 - 0.0962112750161874*m.b4358 - 0.125663706143592*m.b4359
                           - 0.159043128087983*m.b4360 - 0.196349540849362*m.b4361 - 0.282743338823081*m.b4362
                           - 0.38484510006475*m.b4363 - 0.502654824574367*m.b4364 == 0)

m.c1487 = Constraint(expr=   m.x856 - 0.00785398163397448*m.b4365 - 0.0122718463030851*m.b4366
                           - 0.0176714586764426*m.b4367 - 0.0314159265358979*m.b4368 - 0.0490873852123405*m.b4369
                           - 0.0706858347057703*m.b4370 - 0.0962112750161874*m.b4371 - 0.125663706143592*m.b4372
                           - 0.159043128087983*m.b4373 - 0.196349540849362*m.b4374 - 0.282743338823081*m.b4375
                           - 0.38484510006475*m.b4376 - 0.502654824574367*m.b4377 == 0)

m.c1488 = Constraint(expr=   m.x857 - 0.00785398163397448*m.b4378 - 0.0122718463030851*m.b4379
                           - 0.0176714586764426*m.b4380 - 0.0314159265358979*m.b4381 - 0.0490873852123405*m.b4382
                           - 0.0706858347057703*m.b4383 - 0.0962112750161874*m.b4384 - 0.125663706143592*m.b4385
                           - 0.159043128087983*m.b4386 - 0.196349540849362*m.b4387 - 0.282743338823081*m.b4388
                           - 0.38484510006475*m.b4389 - 0.502654824574367*m.b4390 == 0)

m.c1489 = Constraint(expr=   m.x858 - 0.00785398163397448*m.b4391 - 0.0122718463030851*m.b4392
                           - 0.0176714586764426*m.b4393 - 0.0314159265358979*m.b4394 - 0.0490873852123405*m.b4395
                           - 0.0706858347057703*m.b4396 - 0.0962112750161874*m.b4397 - 0.125663706143592*m.b4398
                           - 0.159043128087983*m.b4399 - 0.196349540849362*m.b4400 - 0.282743338823081*m.b4401
                           - 0.38484510006475*m.b4402 - 0.502654824574367*m.b4403 == 0)

m.c1490 = Constraint(expr=   m.x859 - 0.00785398163397448*m.b4404 - 0.0122718463030851*m.b4405
                           - 0.0176714586764426*m.b4406 - 0.0314159265358979*m.b4407 - 0.0490873852123405*m.b4408
                           - 0.0706858347057703*m.b4409 - 0.0962112750161874*m.b4410 - 0.125663706143592*m.b4411
                           - 0.159043128087983*m.b4412 - 0.196349540849362*m.b4413 - 0.282743338823081*m.b4414
                           - 0.38484510006475*m.b4415 - 0.502654824574367*m.b4416 == 0)

m.c1491 = Constraint(expr=   m.x860 - 0.00785398163397448*m.b4417 - 0.0122718463030851*m.b4418
                           - 0.0176714586764426*m.b4419 - 0.0314159265358979*m.b4420 - 0.0490873852123405*m.b4421
                           - 0.0706858347057703*m.b4422 - 0.0962112750161874*m.b4423 - 0.125663706143592*m.b4424
                           - 0.159043128087983*m.b4425 - 0.196349540849362*m.b4426 - 0.282743338823081*m.b4427
                           - 0.38484510006475*m.b4428 - 0.502654824574367*m.b4429 == 0)

m.c1492 = Constraint(expr=   m.x861 - 0.00785398163397448*m.b4430 - 0.0122718463030851*m.b4431
                           - 0.0176714586764426*m.b4432 - 0.0314159265358979*m.b4433 - 0.0490873852123405*m.b4434
                           - 0.0706858347057703*m.b4435 - 0.0962112750161874*m.b4436 - 0.125663706143592*m.b4437
                           - 0.159043128087983*m.b4438 - 0.196349540849362*m.b4439 - 0.282743338823081*m.b4440
                           - 0.38484510006475*m.b4441 - 0.502654824574367*m.b4442 == 0)

m.c1493 = Constraint(expr=   m.x862 - 0.00785398163397448*m.b4443 - 0.0122718463030851*m.b4444
                           - 0.0176714586764426*m.b4445 - 0.0314159265358979*m.b4446 - 0.0490873852123405*m.b4447
                           - 0.0706858347057703*m.b4448 - 0.0962112750161874*m.b4449 - 0.125663706143592*m.b4450
                           - 0.159043128087983*m.b4451 - 0.196349540849362*m.b4452 - 0.282743338823081*m.b4453
                           - 0.38484510006475*m.b4454 - 0.502654824574367*m.b4455 == 0)

m.c1494 = Constraint(expr=   m.x863 - 0.00785398163397448*m.b4456 - 0.0122718463030851*m.b4457
                           - 0.0176714586764426*m.b4458 - 0.0314159265358979*m.b4459 - 0.0490873852123405*m.b4460
                           - 0.0706858347057703*m.b4461 - 0.0962112750161874*m.b4462 - 0.125663706143592*m.b4463
                           - 0.159043128087983*m.b4464 - 0.196349540849362*m.b4465 - 0.282743338823081*m.b4466
                           - 0.38484510006475*m.b4467 - 0.502654824574367*m.b4468 == 0)

m.c1495 = Constraint(expr=   m.x864 - 0.00785398163397448*m.b4469 - 0.0122718463030851*m.b4470
                           - 0.0176714586764426*m.b4471 - 0.0314159265358979*m.b4472 - 0.0490873852123405*m.b4473
                           - 0.0706858347057703*m.b4474 - 0.0962112750161874*m.b4475 - 0.125663706143592*m.b4476
                           - 0.159043128087983*m.b4477 - 0.196349540849362*m.b4478 - 0.282743338823081*m.b4479
                           - 0.38484510006475*m.b4480 - 0.502654824574367*m.b4481 == 0)

m.c1496 = Constraint(expr=   m.x865 - 0.00785398163397448*m.b4482 - 0.0122718463030851*m.b4483
                           - 0.0176714586764426*m.b4484 - 0.0314159265358979*m.b4485 - 0.0490873852123405*m.b4486
                           - 0.0706858347057703*m.b4487 - 0.0962112750161874*m.b4488 - 0.125663706143592*m.b4489
                           - 0.159043128087983*m.b4490 - 0.196349540849362*m.b4491 - 0.282743338823081*m.b4492
                           - 0.38484510006475*m.b4493 - 0.502654824574367*m.b4494 == 0)

m.c1497 = Constraint(expr=   m.x866 - 0.00785398163397448*m.b4495 - 0.0122718463030851*m.b4496
                           - 0.0176714586764426*m.b4497 - 0.0314159265358979*m.b4498 - 0.0490873852123405*m.b4499
                           - 0.0706858347057703*m.b4500 - 0.0962112750161874*m.b4501 - 0.125663706143592*m.b4502
                           - 0.159043128087983*m.b4503 - 0.196349540849362*m.b4504 - 0.282743338823081*m.b4505
                           - 0.38484510006475*m.b4506 - 0.502654824574367*m.b4507 == 0)

m.c1498 = Constraint(expr=   m.x867 - 0.00785398163397448*m.b4508 - 0.0122718463030851*m.b4509
                           - 0.0176714586764426*m.b4510 - 0.0314159265358979*m.b4511 - 0.0490873852123405*m.b4512
                           - 0.0706858347057703*m.b4513 - 0.0962112750161874*m.b4514 - 0.125663706143592*m.b4515
                           - 0.159043128087983*m.b4516 - 0.196349540849362*m.b4517 - 0.282743338823081*m.b4518
                           - 0.38484510006475*m.b4519 - 0.502654824574367*m.b4520 == 0)

m.c1499 = Constraint(expr=   m.x868 - 0.00785398163397448*m.b4521 - 0.0122718463030851*m.b4522
                           - 0.0176714586764426*m.b4523 - 0.0314159265358979*m.b4524 - 0.0490873852123405*m.b4525
                           - 0.0706858347057703*m.b4526 - 0.0962112750161874*m.b4527 - 0.125663706143592*m.b4528
                           - 0.159043128087983*m.b4529 - 0.196349540849362*m.b4530 - 0.282743338823081*m.b4531
                           - 0.38484510006475*m.b4532 - 0.502654824574367*m.b4533 == 0)

m.c1500 = Constraint(expr=   m.x869 - 0.00785398163397448*m.b4534 - 0.0122718463030851*m.b4535
                           - 0.0176714586764426*m.b4536 - 0.0314159265358979*m.b4537 - 0.0490873852123405*m.b4538
                           - 0.0706858347057703*m.b4539 - 0.0962112750161874*m.b4540 - 0.125663706143592*m.b4541
                           - 0.159043128087983*m.b4542 - 0.196349540849362*m.b4543 - 0.282743338823081*m.b4544
                           - 0.38484510006475*m.b4545 - 0.502654824574367*m.b4546 == 0)

m.c1501 = Constraint(expr=   m.x870 - 0.00785398163397448*m.b4547 - 0.0122718463030851*m.b4548
                           - 0.0176714586764426*m.b4549 - 0.0314159265358979*m.b4550 - 0.0490873852123405*m.b4551
                           - 0.0706858347057703*m.b4552 - 0.0962112750161874*m.b4553 - 0.125663706143592*m.b4554
                           - 0.159043128087983*m.b4555 - 0.196349540849362*m.b4556 - 0.282743338823081*m.b4557
                           - 0.38484510006475*m.b4558 - 0.502654824574367*m.b4559 == 0)

m.c1502 = Constraint(expr=   m.x871 - 0.00785398163397448*m.b4560 - 0.0122718463030851*m.b4561
                           - 0.0176714586764426*m.b4562 - 0.0314159265358979*m.b4563 - 0.0490873852123405*m.b4564
                           - 0.0706858347057703*m.b4565 - 0.0962112750161874*m.b4566 - 0.125663706143592*m.b4567
                           - 0.159043128087983*m.b4568 - 0.196349540849362*m.b4569 - 0.282743338823081*m.b4570
                           - 0.38484510006475*m.b4571 - 0.502654824574367*m.b4572 == 0)

m.c1503 = Constraint(expr=   m.x872 - 0.00785398163397448*m.b4573 - 0.0122718463030851*m.b4574
                           - 0.0176714586764426*m.b4575 - 0.0314159265358979*m.b4576 - 0.0490873852123405*m.b4577
                           - 0.0706858347057703*m.b4578 - 0.0962112750161874*m.b4579 - 0.125663706143592*m.b4580
                           - 0.159043128087983*m.b4581 - 0.196349540849362*m.b4582 - 0.282743338823081*m.b4583
                           - 0.38484510006475*m.b4584 - 0.502654824574367*m.b4585 == 0)

m.c1504 = Constraint(expr=   m.x873 - 0.00785398163397448*m.b4586 - 0.0122718463030851*m.b4587
                           - 0.0176714586764426*m.b4588 - 0.0314159265358979*m.b4589 - 0.0490873852123405*m.b4590
                           - 0.0706858347057703*m.b4591 - 0.0962112750161874*m.b4592 - 0.125663706143592*m.b4593
                           - 0.159043128087983*m.b4594 - 0.196349540849362*m.b4595 - 0.282743338823081*m.b4596
                           - 0.38484510006475*m.b4597 - 0.502654824574367*m.b4598 == 0)

m.c1505 = Constraint(expr=   m.x874 - 0.00785398163397448*m.b4599 - 0.0122718463030851*m.b4600
                           - 0.0176714586764426*m.b4601 - 0.0314159265358979*m.b4602 - 0.0490873852123405*m.b4603
                           - 0.0706858347057703*m.b4604 - 0.0962112750161874*m.b4605 - 0.125663706143592*m.b4606
                           - 0.159043128087983*m.b4607 - 0.196349540849362*m.b4608 - 0.282743338823081*m.b4609
                           - 0.38484510006475*m.b4610 - 0.502654824574367*m.b4611 == 0)

m.c1506 = Constraint(expr=   m.x875 - 0.00785398163397448*m.b4612 - 0.0122718463030851*m.b4613
                           - 0.0176714586764426*m.b4614 - 0.0314159265358979*m.b4615 - 0.0490873852123405*m.b4616
                           - 0.0706858347057703*m.b4617 - 0.0962112750161874*m.b4618 - 0.125663706143592*m.b4619
                           - 0.159043128087983*m.b4620 - 0.196349540849362*m.b4621 - 0.282743338823081*m.b4622
                           - 0.38484510006475*m.b4623 - 0.502654824574367*m.b4624 == 0)

m.c1507 = Constraint(expr=   m.x876 - 0.00785398163397448*m.b4625 - 0.0122718463030851*m.b4626
                           - 0.0176714586764426*m.b4627 - 0.0314159265358979*m.b4628 - 0.0490873852123405*m.b4629
                           - 0.0706858347057703*m.b4630 - 0.0962112750161874*m.b4631 - 0.125663706143592*m.b4632
                           - 0.159043128087983*m.b4633 - 0.196349540849362*m.b4634 - 0.282743338823081*m.b4635
                           - 0.38484510006475*m.b4636 - 0.502654824574367*m.b4637 == 0)

m.c1508 = Constraint(expr=   m.x877 - 0.00785398163397448*m.b4638 - 0.0122718463030851*m.b4639
                           - 0.0176714586764426*m.b4640 - 0.0314159265358979*m.b4641 - 0.0490873852123405*m.b4642
                           - 0.0706858347057703*m.b4643 - 0.0962112750161874*m.b4644 - 0.125663706143592*m.b4645
                           - 0.159043128087983*m.b4646 - 0.196349540849362*m.b4647 - 0.282743338823081*m.b4648
                           - 0.38484510006475*m.b4649 - 0.502654824574367*m.b4650 == 0)

m.c1509 = Constraint(expr=   m.x878 - 0.00785398163397448*m.b4651 - 0.0122718463030851*m.b4652
                           - 0.0176714586764426*m.b4653 - 0.0314159265358979*m.b4654 - 0.0490873852123405*m.b4655
                           - 0.0706858347057703*m.b4656 - 0.0962112750161874*m.b4657 - 0.125663706143592*m.b4658
                           - 0.159043128087983*m.b4659 - 0.196349540849362*m.b4660 - 0.282743338823081*m.b4661
                           - 0.38484510006475*m.b4662 - 0.502654824574367*m.b4663 == 0)

m.c1510 = Constraint(expr=   m.x879 - 0.00785398163397448*m.b4664 - 0.0122718463030851*m.b4665
                           - 0.0176714586764426*m.b4666 - 0.0314159265358979*m.b4667 - 0.0490873852123405*m.b4668
                           - 0.0706858347057703*m.b4669 - 0.0962112750161874*m.b4670 - 0.125663706143592*m.b4671
                           - 0.159043128087983*m.b4672 - 0.196349540849362*m.b4673 - 0.282743338823081*m.b4674
                           - 0.38484510006475*m.b4675 - 0.502654824574367*m.b4676 == 0)

m.c1511 = Constraint(expr=   m.x880 - 0.00785398163397448*m.b4677 - 0.0122718463030851*m.b4678
                           - 0.0176714586764426*m.b4679 - 0.0314159265358979*m.b4680 - 0.0490873852123405*m.b4681
                           - 0.0706858347057703*m.b4682 - 0.0962112750161874*m.b4683 - 0.125663706143592*m.b4684
                           - 0.159043128087983*m.b4685 - 0.196349540849362*m.b4686 - 0.282743338823081*m.b4687
                           - 0.38484510006475*m.b4688 - 0.502654824574367*m.b4689 == 0)

m.c1512 = Constraint(expr=   m.x881 - 0.00785398163397448*m.b4690 - 0.0122718463030851*m.b4691
                           - 0.0176714586764426*m.b4692 - 0.0314159265358979*m.b4693 - 0.0490873852123405*m.b4694
                           - 0.0706858347057703*m.b4695 - 0.0962112750161874*m.b4696 - 0.125663706143592*m.b4697
                           - 0.159043128087983*m.b4698 - 0.196349540849362*m.b4699 - 0.282743338823081*m.b4700
                           - 0.38484510006475*m.b4701 - 0.502654824574367*m.b4702 == 0)

m.c1513 = Constraint(expr=   m.x882 - 0.00785398163397448*m.b4703 - 0.0122718463030851*m.b4704
                           - 0.0176714586764426*m.b4705 - 0.0314159265358979*m.b4706 - 0.0490873852123405*m.b4707
                           - 0.0706858347057703*m.b4708 - 0.0962112750161874*m.b4709 - 0.125663706143592*m.b4710
                           - 0.159043128087983*m.b4711 - 0.196349540849362*m.b4712 - 0.282743338823081*m.b4713
                           - 0.38484510006475*m.b4714 - 0.502654824574367*m.b4715 == 0)

m.c1514 = Constraint(expr=   m.x883 - 0.00785398163397448*m.b4716 - 0.0122718463030851*m.b4717
                           - 0.0176714586764426*m.b4718 - 0.0314159265358979*m.b4719 - 0.0490873852123405*m.b4720
                           - 0.0706858347057703*m.b4721 - 0.0962112750161874*m.b4722 - 0.125663706143592*m.b4723
                           - 0.159043128087983*m.b4724 - 0.196349540849362*m.b4725 - 0.282743338823081*m.b4726
                           - 0.38484510006475*m.b4727 - 0.502654824574367*m.b4728 == 0)

m.c1515 = Constraint(expr=   m.x884 - 0.00785398163397448*m.b4729 - 0.0122718463030851*m.b4730
                           - 0.0176714586764426*m.b4731 - 0.0314159265358979*m.b4732 - 0.0490873852123405*m.b4733
                           - 0.0706858347057703*m.b4734 - 0.0962112750161874*m.b4735 - 0.125663706143592*m.b4736
                           - 0.159043128087983*m.b4737 - 0.196349540849362*m.b4738 - 0.282743338823081*m.b4739
                           - 0.38484510006475*m.b4740 - 0.502654824574367*m.b4741 == 0)

m.c1516 = Constraint(expr=   m.x885 - 0.00785398163397448*m.b4742 - 0.0122718463030851*m.b4743
                           - 0.0176714586764426*m.b4744 - 0.0314159265358979*m.b4745 - 0.0490873852123405*m.b4746
                           - 0.0706858347057703*m.b4747 - 0.0962112750161874*m.b4748 - 0.125663706143592*m.b4749
                           - 0.159043128087983*m.b4750 - 0.196349540849362*m.b4751 - 0.282743338823081*m.b4752
                           - 0.38484510006475*m.b4753 - 0.502654824574367*m.b4754 == 0)

m.c1517 = Constraint(expr=   m.x886 - 0.00785398163397448*m.b4755 - 0.0122718463030851*m.b4756
                           - 0.0176714586764426*m.b4757 - 0.0314159265358979*m.b4758 - 0.0490873852123405*m.b4759
                           - 0.0706858347057703*m.b4760 - 0.0962112750161874*m.b4761 - 0.125663706143592*m.b4762
                           - 0.159043128087983*m.b4763 - 0.196349540849362*m.b4764 - 0.282743338823081*m.b4765
                           - 0.38484510006475*m.b4766 - 0.502654824574367*m.b4767 == 0)

m.c1518 = Constraint(expr=   m.x887 - 0.00785398163397448*m.b4768 - 0.0122718463030851*m.b4769
                           - 0.0176714586764426*m.b4770 - 0.0314159265358979*m.b4771 - 0.0490873852123405*m.b4772
                           - 0.0706858347057703*m.b4773 - 0.0962112750161874*m.b4774 - 0.125663706143592*m.b4775
                           - 0.159043128087983*m.b4776 - 0.196349540849362*m.b4777 - 0.282743338823081*m.b4778
                           - 0.38484510006475*m.b4779 - 0.502654824574367*m.b4780 == 0)

m.c1519 = Constraint(expr=   m.x888 - 0.00785398163397448*m.b4781 - 0.0122718463030851*m.b4782
                           - 0.0176714586764426*m.b4783 - 0.0314159265358979*m.b4784 - 0.0490873852123405*m.b4785
                           - 0.0706858347057703*m.b4786 - 0.0962112750161874*m.b4787 - 0.125663706143592*m.b4788
                           - 0.159043128087983*m.b4789 - 0.196349540849362*m.b4790 - 0.282743338823081*m.b4791
                           - 0.38484510006475*m.b4792 - 0.502654824574367*m.b4793 == 0)

m.c1520 = Constraint(expr=   m.x889 - 0.00785398163397448*m.b4794 - 0.0122718463030851*m.b4795
                           - 0.0176714586764426*m.b4796 - 0.0314159265358979*m.b4797 - 0.0490873852123405*m.b4798
                           - 0.0706858347057703*m.b4799 - 0.0962112750161874*m.b4800 - 0.125663706143592*m.b4801
                           - 0.159043128087983*m.b4802 - 0.196349540849362*m.b4803 - 0.282743338823081*m.b4804
                           - 0.38484510006475*m.b4805 - 0.502654824574367*m.b4806 == 0)

m.c1521 = Constraint(expr=   m.x890 - 0.00785398163397448*m.b4807 - 0.0122718463030851*m.b4808
                           - 0.0176714586764426*m.b4809 - 0.0314159265358979*m.b4810 - 0.0490873852123405*m.b4811
                           - 0.0706858347057703*m.b4812 - 0.0962112750161874*m.b4813 - 0.125663706143592*m.b4814
                           - 0.159043128087983*m.b4815 - 0.196349540849362*m.b4816 - 0.282743338823081*m.b4817
                           - 0.38484510006475*m.b4818 - 0.502654824574367*m.b4819 == 0)

m.c1522 = Constraint(expr=   m.x891 - 0.00785398163397448*m.b4820 - 0.0122718463030851*m.b4821
                           - 0.0176714586764426*m.b4822 - 0.0314159265358979*m.b4823 - 0.0490873852123405*m.b4824
                           - 0.0706858347057703*m.b4825 - 0.0962112750161874*m.b4826 - 0.125663706143592*m.b4827
                           - 0.159043128087983*m.b4828 - 0.196349540849362*m.b4829 - 0.282743338823081*m.b4830
                           - 0.38484510006475*m.b4831 - 0.502654824574367*m.b4832 == 0)

m.c1523 = Constraint(expr=   m.x892 - 0.00785398163397448*m.b4833 - 0.0122718463030851*m.b4834
                           - 0.0176714586764426*m.b4835 - 0.0314159265358979*m.b4836 - 0.0490873852123405*m.b4837
                           - 0.0706858347057703*m.b4838 - 0.0962112750161874*m.b4839 - 0.125663706143592*m.b4840
                           - 0.159043128087983*m.b4841 - 0.196349540849362*m.b4842 - 0.282743338823081*m.b4843
                           - 0.38484510006475*m.b4844 - 0.502654824574367*m.b4845 == 0)

m.c1524 = Constraint(expr=   m.x893 - 0.00785398163397448*m.b4846 - 0.0122718463030851*m.b4847
                           - 0.0176714586764426*m.b4848 - 0.0314159265358979*m.b4849 - 0.0490873852123405*m.b4850
                           - 0.0706858347057703*m.b4851 - 0.0962112750161874*m.b4852 - 0.125663706143592*m.b4853
                           - 0.159043128087983*m.b4854 - 0.196349540849362*m.b4855 - 0.282743338823081*m.b4856
                           - 0.38484510006475*m.b4857 - 0.502654824574367*m.b4858 == 0)

m.c1525 = Constraint(expr=   m.x894 - 0.00785398163397448*m.b4859 - 0.0122718463030851*m.b4860
                           - 0.0176714586764426*m.b4861 - 0.0314159265358979*m.b4862 - 0.0490873852123405*m.b4863
                           - 0.0706858347057703*m.b4864 - 0.0962112750161874*m.b4865 - 0.125663706143592*m.b4866
                           - 0.159043128087983*m.b4867 - 0.196349540849362*m.b4868 - 0.282743338823081*m.b4869
                           - 0.38484510006475*m.b4870 - 0.502654824574367*m.b4871 == 0)

m.c1526 = Constraint(expr=   m.x895 - 0.00785398163397448*m.b4872 - 0.0122718463030851*m.b4873
                           - 0.0176714586764426*m.b4874 - 0.0314159265358979*m.b4875 - 0.0490873852123405*m.b4876
                           - 0.0706858347057703*m.b4877 - 0.0962112750161874*m.b4878 - 0.125663706143592*m.b4879
                           - 0.159043128087983*m.b4880 - 0.196349540849362*m.b4881 - 0.282743338823081*m.b4882
                           - 0.38484510006475*m.b4883 - 0.502654824574367*m.b4884 == 0)

m.c1527 = Constraint(expr=   m.x896 - 0.00785398163397448*m.b4885 - 0.0122718463030851*m.b4886
                           - 0.0176714586764426*m.b4887 - 0.0314159265358979*m.b4888 - 0.0490873852123405*m.b4889
                           - 0.0706858347057703*m.b4890 - 0.0962112750161874*m.b4891 - 0.125663706143592*m.b4892
                           - 0.159043128087983*m.b4893 - 0.196349540849362*m.b4894 - 0.282743338823081*m.b4895
                           - 0.38484510006475*m.b4896 - 0.502654824574367*m.b4897 == 0)

m.c1528 = Constraint(expr=   m.x897 - 0.00785398163397448*m.b4898 - 0.0122718463030851*m.b4899
                           - 0.0176714586764426*m.b4900 - 0.0314159265358979*m.b4901 - 0.0490873852123405*m.b4902
                           - 0.0706858347057703*m.b4903 - 0.0962112750161874*m.b4904 - 0.125663706143592*m.b4905
                           - 0.159043128087983*m.b4906 - 0.196349540849362*m.b4907 - 0.282743338823081*m.b4908
                           - 0.38484510006475*m.b4909 - 0.502654824574367*m.b4910 == 0)

m.c1529 = Constraint(expr=   m.x898 - 0.00785398163397448*m.b4911 - 0.0122718463030851*m.b4912
                           - 0.0176714586764426*m.b4913 - 0.0314159265358979*m.b4914 - 0.0490873852123405*m.b4915
                           - 0.0706858347057703*m.b4916 - 0.0962112750161874*m.b4917 - 0.125663706143592*m.b4918
                           - 0.159043128087983*m.b4919 - 0.196349540849362*m.b4920 - 0.282743338823081*m.b4921
                           - 0.38484510006475*m.b4922 - 0.502654824574367*m.b4923 == 0)

m.c1530 = Constraint(expr=   m.x899 - 0.00785398163397448*m.b4924 - 0.0122718463030851*m.b4925
                           - 0.0176714586764426*m.b4926 - 0.0314159265358979*m.b4927 - 0.0490873852123405*m.b4928
                           - 0.0706858347057703*m.b4929 - 0.0962112750161874*m.b4930 - 0.125663706143592*m.b4931
                           - 0.159043128087983*m.b4932 - 0.196349540849362*m.b4933 - 0.282743338823081*m.b4934
                           - 0.38484510006475*m.b4935 - 0.502654824574367*m.b4936 == 0)

m.c1531 = Constraint(expr=   m.x900 - 0.00785398163397448*m.b4937 - 0.0122718463030851*m.b4938
                           - 0.0176714586764426*m.b4939 - 0.0314159265358979*m.b4940 - 0.0490873852123405*m.b4941
                           - 0.0706858347057703*m.b4942 - 0.0962112750161874*m.b4943 - 0.125663706143592*m.b4944
                           - 0.159043128087983*m.b4945 - 0.196349540849362*m.b4946 - 0.282743338823081*m.b4947
                           - 0.38484510006475*m.b4948 - 0.502654824574367*m.b4949 == 0)

m.c1532 = Constraint(expr=   m.x901 - 0.00785398163397448*m.b4950 - 0.0122718463030851*m.b4951
                           - 0.0176714586764426*m.b4952 - 0.0314159265358979*m.b4953 - 0.0490873852123405*m.b4954
                           - 0.0706858347057703*m.b4955 - 0.0962112750161874*m.b4956 - 0.125663706143592*m.b4957
                           - 0.159043128087983*m.b4958 - 0.196349540849362*m.b4959 - 0.282743338823081*m.b4960
                           - 0.38484510006475*m.b4961 - 0.502654824574367*m.b4962 == 0)

m.c1533 = Constraint(expr=   m.x902 - 0.00785398163397448*m.b4963 - 0.0122718463030851*m.b4964
                           - 0.0176714586764426*m.b4965 - 0.0314159265358979*m.b4966 - 0.0490873852123405*m.b4967
                           - 0.0706858347057703*m.b4968 - 0.0962112750161874*m.b4969 - 0.125663706143592*m.b4970
                           - 0.159043128087983*m.b4971 - 0.196349540849362*m.b4972 - 0.282743338823081*m.b4973
                           - 0.38484510006475*m.b4974 - 0.502654824574367*m.b4975 == 0)

m.c1534 = Constraint(expr=   m.x903 - 0.00785398163397448*m.b4976 - 0.0122718463030851*m.b4977
                           - 0.0176714586764426*m.b4978 - 0.0314159265358979*m.b4979 - 0.0490873852123405*m.b4980
                           - 0.0706858347057703*m.b4981 - 0.0962112750161874*m.b4982 - 0.125663706143592*m.b4983
                           - 0.159043128087983*m.b4984 - 0.196349540849362*m.b4985 - 0.282743338823081*m.b4986
                           - 0.38484510006475*m.b4987 - 0.502654824574367*m.b4988 == 0)

m.c1535 = Constraint(expr=   m.x904 - 0.00785398163397448*m.b4989 - 0.0122718463030851*m.b4990
                           - 0.0176714586764426*m.b4991 - 0.0314159265358979*m.b4992 - 0.0490873852123405*m.b4993
                           - 0.0706858347057703*m.b4994 - 0.0962112750161874*m.b4995 - 0.125663706143592*m.b4996
                           - 0.159043128087983*m.b4997 - 0.196349540849362*m.b4998 - 0.282743338823081*m.b4999
                           - 0.38484510006475*m.b5000 - 0.502654824574367*m.b5001 == 0)

m.c1536 = Constraint(expr=   m.x905 - 0.00785398163397448*m.b5002 - 0.0122718463030851*m.b5003
                           - 0.0176714586764426*m.b5004 - 0.0314159265358979*m.b5005 - 0.0490873852123405*m.b5006
                           - 0.0706858347057703*m.b5007 - 0.0962112750161874*m.b5008 - 0.125663706143592*m.b5009
                           - 0.159043128087983*m.b5010 - 0.196349540849362*m.b5011 - 0.282743338823081*m.b5012
                           - 0.38484510006475*m.b5013 - 0.502654824574367*m.b5014 == 0)

m.c1537 = Constraint(expr=   m.x906 - 0.00785398163397448*m.b5015 - 0.0122718463030851*m.b5016
                           - 0.0176714586764426*m.b5017 - 0.0314159265358979*m.b5018 - 0.0490873852123405*m.b5019
                           - 0.0706858347057703*m.b5020 - 0.0962112750161874*m.b5021 - 0.125663706143592*m.b5022
                           - 0.159043128087983*m.b5023 - 0.196349540849362*m.b5024 - 0.282743338823081*m.b5025
                           - 0.38484510006475*m.b5026 - 0.502654824574367*m.b5027 == 0)

m.c1538 = Constraint(expr=   m.b907 + m.b908 + m.b909 + m.b910 + m.b911 + m.b912 + m.b913 + m.b914 + m.b915 + m.b916
                           + m.b917 + m.b918 + m.b919 == 1)

m.c1539 = Constraint(expr=   m.b920 + m.b921 + m.b922 + m.b923 + m.b924 + m.b925 + m.b926 + m.b927 + m.b928 + m.b929
                           + m.b930 + m.b931 + m.b932 == 1)

m.c1540 = Constraint(expr=   m.b933 + m.b934 + m.b935 + m.b936 + m.b937 + m.b938 + m.b939 + m.b940 + m.b941 + m.b942
                           + m.b943 + m.b944 + m.b945 == 1)

m.c1541 = Constraint(expr=   m.b946 + m.b947 + m.b948 + m.b949 + m.b950 + m.b951 + m.b952 + m.b953 + m.b954 + m.b955
                           + m.b956 + m.b957 + m.b958 == 1)

m.c1542 = Constraint(expr=   m.b959 + m.b960 + m.b961 + m.b962 + m.b963 + m.b964 + m.b965 + m.b966 + m.b967 + m.b968
                           + m.b969 + m.b970 + m.b971 == 1)

m.c1543 = Constraint(expr=   m.b972 + m.b973 + m.b974 + m.b975 + m.b976 + m.b977 + m.b978 + m.b979 + m.b980 + m.b981
                           + m.b982 + m.b983 + m.b984 == 1)

m.c1544 = Constraint(expr=   m.b985 + m.b986 + m.b987 + m.b988 + m.b989 + m.b990 + m.b991 + m.b992 + m.b993 + m.b994
                           + m.b995 + m.b996 + m.b997 == 1)

m.c1545 = Constraint(expr=   m.b998 + m.b999 + m.b1000 + m.b1001 + m.b1002 + m.b1003 + m.b1004 + m.b1005 + m.b1006
                           + m.b1007 + m.b1008 + m.b1009 + m.b1010 == 1)

m.c1546 = Constraint(expr=   m.b1011 + m.b1012 + m.b1013 + m.b1014 + m.b1015 + m.b1016 + m.b1017 + m.b1018 + m.b1019
                           + m.b1020 + m.b1021 + m.b1022 + m.b1023 == 1)

m.c1547 = Constraint(expr=   m.b1024 + m.b1025 + m.b1026 + m.b1027 + m.b1028 + m.b1029 + m.b1030 + m.b1031 + m.b1032
                           + m.b1033 + m.b1034 + m.b1035 + m.b1036 == 1)

m.c1548 = Constraint(expr=   m.b1037 + m.b1038 + m.b1039 + m.b1040 + m.b1041 + m.b1042 + m.b1043 + m.b1044 + m.b1045
                           + m.b1046 + m.b1047 + m.b1048 + m.b1049 == 1)

m.c1549 = Constraint(expr=   m.b1050 + m.b1051 + m.b1052 + m.b1053 + m.b1054 + m.b1055 + m.b1056 + m.b1057 + m.b1058
                           + m.b1059 + m.b1060 + m.b1061 + m.b1062 == 1)

m.c1550 = Constraint(expr=   m.b1063 + m.b1064 + m.b1065 + m.b1066 + m.b1067 + m.b1068 + m.b1069 + m.b1070 + m.b1071
                           + m.b1072 + m.b1073 + m.b1074 + m.b1075 == 1)

m.c1551 = Constraint(expr=   m.b1076 + m.b1077 + m.b1078 + m.b1079 + m.b1080 + m.b1081 + m.b1082 + m.b1083 + m.b1084
                           + m.b1085 + m.b1086 + m.b1087 + m.b1088 == 1)

m.c1552 = Constraint(expr=   m.b1089 + m.b1090 + m.b1091 + m.b1092 + m.b1093 + m.b1094 + m.b1095 + m.b1096 + m.b1097
                           + m.b1098 + m.b1099 + m.b1100 + m.b1101 == 1)

m.c1553 = Constraint(expr=   m.b1102 + m.b1103 + m.b1104 + m.b1105 + m.b1106 + m.b1107 + m.b1108 + m.b1109 + m.b1110
                           + m.b1111 + m.b1112 + m.b1113 + m.b1114 == 1)

m.c1554 = Constraint(expr=   m.b1115 + m.b1116 + m.b1117 + m.b1118 + m.b1119 + m.b1120 + m.b1121 + m.b1122 + m.b1123
                           + m.b1124 + m.b1125 + m.b1126 + m.b1127 == 1)

m.c1555 = Constraint(expr=   m.b1128 + m.b1129 + m.b1130 + m.b1131 + m.b1132 + m.b1133 + m.b1134 + m.b1135 + m.b1136
                           + m.b1137 + m.b1138 + m.b1139 + m.b1140 == 1)

m.c1556 = Constraint(expr=   m.b1141 + m.b1142 + m.b1143 + m.b1144 + m.b1145 + m.b1146 + m.b1147 + m.b1148 + m.b1149
                           + m.b1150 + m.b1151 + m.b1152 + m.b1153 == 1)

m.c1557 = Constraint(expr=   m.b1154 + m.b1155 + m.b1156 + m.b1157 + m.b1158 + m.b1159 + m.b1160 + m.b1161 + m.b1162
                           + m.b1163 + m.b1164 + m.b1165 + m.b1166 == 1)

m.c1558 = Constraint(expr=   m.b1167 + m.b1168 + m.b1169 + m.b1170 + m.b1171 + m.b1172 + m.b1173 + m.b1174 + m.b1175
                           + m.b1176 + m.b1177 + m.b1178 + m.b1179 == 1)

m.c1559 = Constraint(expr=   m.b1180 + m.b1181 + m.b1182 + m.b1183 + m.b1184 + m.b1185 + m.b1186 + m.b1187 + m.b1188
                           + m.b1189 + m.b1190 + m.b1191 + m.b1192 == 1)

m.c1560 = Constraint(expr=   m.b1193 + m.b1194 + m.b1195 + m.b1196 + m.b1197 + m.b1198 + m.b1199 + m.b1200 + m.b1201
                           + m.b1202 + m.b1203 + m.b1204 + m.b1205 == 1)

m.c1561 = Constraint(expr=   m.b1206 + m.b1207 + m.b1208 + m.b1209 + m.b1210 + m.b1211 + m.b1212 + m.b1213 + m.b1214
                           + m.b1215 + m.b1216 + m.b1217 + m.b1218 == 1)

m.c1562 = Constraint(expr=   m.b1219 + m.b1220 + m.b1221 + m.b1222 + m.b1223 + m.b1224 + m.b1225 + m.b1226 + m.b1227
                           + m.b1228 + m.b1229 + m.b1230 + m.b1231 == 1)

m.c1563 = Constraint(expr=   m.b1232 + m.b1233 + m.b1234 + m.b1235 + m.b1236 + m.b1237 + m.b1238 + m.b1239 + m.b1240
                           + m.b1241 + m.b1242 + m.b1243 + m.b1244 == 1)

m.c1564 = Constraint(expr=   m.b1245 + m.b1246 + m.b1247 + m.b1248 + m.b1249 + m.b1250 + m.b1251 + m.b1252 + m.b1253
                           + m.b1254 + m.b1255 + m.b1256 + m.b1257 == 1)

m.c1565 = Constraint(expr=   m.b1258 + m.b1259 + m.b1260 + m.b1261 + m.b1262 + m.b1263 + m.b1264 + m.b1265 + m.b1266
                           + m.b1267 + m.b1268 + m.b1269 + m.b1270 == 1)

m.c1566 = Constraint(expr=   m.b1271 + m.b1272 + m.b1273 + m.b1274 + m.b1275 + m.b1276 + m.b1277 + m.b1278 + m.b1279
                           + m.b1280 + m.b1281 + m.b1282 + m.b1283 == 1)

m.c1567 = Constraint(expr=   m.b1284 + m.b1285 + m.b1286 + m.b1287 + m.b1288 + m.b1289 + m.b1290 + m.b1291 + m.b1292
                           + m.b1293 + m.b1294 + m.b1295 + m.b1296 == 1)

m.c1568 = Constraint(expr=   m.b1297 + m.b1298 + m.b1299 + m.b1300 + m.b1301 + m.b1302 + m.b1303 + m.b1304 + m.b1305
                           + m.b1306 + m.b1307 + m.b1308 + m.b1309 == 1)

m.c1569 = Constraint(expr=   m.b1310 + m.b1311 + m.b1312 + m.b1313 + m.b1314 + m.b1315 + m.b1316 + m.b1317 + m.b1318
                           + m.b1319 + m.b1320 + m.b1321 + m.b1322 == 1)

m.c1570 = Constraint(expr=   m.b1323 + m.b1324 + m.b1325 + m.b1326 + m.b1327 + m.b1328 + m.b1329 + m.b1330 + m.b1331
                           + m.b1332 + m.b1333 + m.b1334 + m.b1335 == 1)

m.c1571 = Constraint(expr=   m.b1336 + m.b1337 + m.b1338 + m.b1339 + m.b1340 + m.b1341 + m.b1342 + m.b1343 + m.b1344
                           + m.b1345 + m.b1346 + m.b1347 + m.b1348 == 1)

m.c1572 = Constraint(expr=   m.b1349 + m.b1350 + m.b1351 + m.b1352 + m.b1353 + m.b1354 + m.b1355 + m.b1356 + m.b1357
                           + m.b1358 + m.b1359 + m.b1360 + m.b1361 == 1)

m.c1573 = Constraint(expr=   m.b1362 + m.b1363 + m.b1364 + m.b1365 + m.b1366 + m.b1367 + m.b1368 + m.b1369 + m.b1370
                           + m.b1371 + m.b1372 + m.b1373 + m.b1374 == 1)

m.c1574 = Constraint(expr=   m.b1375 + m.b1376 + m.b1377 + m.b1378 + m.b1379 + m.b1380 + m.b1381 + m.b1382 + m.b1383
                           + m.b1384 + m.b1385 + m.b1386 + m.b1387 == 1)

m.c1575 = Constraint(expr=   m.b1388 + m.b1389 + m.b1390 + m.b1391 + m.b1392 + m.b1393 + m.b1394 + m.b1395 + m.b1396
                           + m.b1397 + m.b1398 + m.b1399 + m.b1400 == 1)

m.c1576 = Constraint(expr=   m.b1401 + m.b1402 + m.b1403 + m.b1404 + m.b1405 + m.b1406 + m.b1407 + m.b1408 + m.b1409
                           + m.b1410 + m.b1411 + m.b1412 + m.b1413 == 1)

m.c1577 = Constraint(expr=   m.b1414 + m.b1415 + m.b1416 + m.b1417 + m.b1418 + m.b1419 + m.b1420 + m.b1421 + m.b1422
                           + m.b1423 + m.b1424 + m.b1425 + m.b1426 == 1)

m.c1578 = Constraint(expr=   m.b1427 + m.b1428 + m.b1429 + m.b1430 + m.b1431 + m.b1432 + m.b1433 + m.b1434 + m.b1435
                           + m.b1436 + m.b1437 + m.b1438 + m.b1439 == 1)

m.c1579 = Constraint(expr=   m.b1440 + m.b1441 + m.b1442 + m.b1443 + m.b1444 + m.b1445 + m.b1446 + m.b1447 + m.b1448
                           + m.b1449 + m.b1450 + m.b1451 + m.b1452 == 1)

m.c1580 = Constraint(expr=   m.b1453 + m.b1454 + m.b1455 + m.b1456 + m.b1457 + m.b1458 + m.b1459 + m.b1460 + m.b1461
                           + m.b1462 + m.b1463 + m.b1464 + m.b1465 == 1)

m.c1581 = Constraint(expr=   m.b1466 + m.b1467 + m.b1468 + m.b1469 + m.b1470 + m.b1471 + m.b1472 + m.b1473 + m.b1474
                           + m.b1475 + m.b1476 + m.b1477 + m.b1478 == 1)

m.c1582 = Constraint(expr=   m.b1479 + m.b1480 + m.b1481 + m.b1482 + m.b1483 + m.b1484 + m.b1485 + m.b1486 + m.b1487
                           + m.b1488 + m.b1489 + m.b1490 + m.b1491 == 1)

m.c1583 = Constraint(expr=   m.b1492 + m.b1493 + m.b1494 + m.b1495 + m.b1496 + m.b1497 + m.b1498 + m.b1499 + m.b1500
                           + m.b1501 + m.b1502 + m.b1503 + m.b1504 == 1)

m.c1584 = Constraint(expr=   m.b1505 + m.b1506 + m.b1507 + m.b1508 + m.b1509 + m.b1510 + m.b1511 + m.b1512 + m.b1513
                           + m.b1514 + m.b1515 + m.b1516 + m.b1517 == 1)

m.c1585 = Constraint(expr=   m.b1518 + m.b1519 + m.b1520 + m.b1521 + m.b1522 + m.b1523 + m.b1524 + m.b1525 + m.b1526
                           + m.b1527 + m.b1528 + m.b1529 + m.b1530 == 1)

m.c1586 = Constraint(expr=   m.b1531 + m.b1532 + m.b1533 + m.b1534 + m.b1535 + m.b1536 + m.b1537 + m.b1538 + m.b1539
                           + m.b1540 + m.b1541 + m.b1542 + m.b1543 == 1)

m.c1587 = Constraint(expr=   m.b1544 + m.b1545 + m.b1546 + m.b1547 + m.b1548 + m.b1549 + m.b1550 + m.b1551 + m.b1552
                           + m.b1553 + m.b1554 + m.b1555 + m.b1556 == 1)

m.c1588 = Constraint(expr=   m.b1557 + m.b1558 + m.b1559 + m.b1560 + m.b1561 + m.b1562 + m.b1563 + m.b1564 + m.b1565
                           + m.b1566 + m.b1567 + m.b1568 + m.b1569 == 1)

m.c1589 = Constraint(expr=   m.b1570 + m.b1571 + m.b1572 + m.b1573 + m.b1574 + m.b1575 + m.b1576 + m.b1577 + m.b1578
                           + m.b1579 + m.b1580 + m.b1581 + m.b1582 == 1)

m.c1590 = Constraint(expr=   m.b1583 + m.b1584 + m.b1585 + m.b1586 + m.b1587 + m.b1588 + m.b1589 + m.b1590 + m.b1591
                           + m.b1592 + m.b1593 + m.b1594 + m.b1595 == 1)

m.c1591 = Constraint(expr=   m.b1596 + m.b1597 + m.b1598 + m.b1599 + m.b1600 + m.b1601 + m.b1602 + m.b1603 + m.b1604
                           + m.b1605 + m.b1606 + m.b1607 + m.b1608 == 1)

m.c1592 = Constraint(expr=   m.b1609 + m.b1610 + m.b1611 + m.b1612 + m.b1613 + m.b1614 + m.b1615 + m.b1616 + m.b1617
                           + m.b1618 + m.b1619 + m.b1620 + m.b1621 == 1)

m.c1593 = Constraint(expr=   m.b1622 + m.b1623 + m.b1624 + m.b1625 + m.b1626 + m.b1627 + m.b1628 + m.b1629 + m.b1630
                           + m.b1631 + m.b1632 + m.b1633 + m.b1634 == 1)

m.c1594 = Constraint(expr=   m.b1635 + m.b1636 + m.b1637 + m.b1638 + m.b1639 + m.b1640 + m.b1641 + m.b1642 + m.b1643
                           + m.b1644 + m.b1645 + m.b1646 + m.b1647 == 1)

m.c1595 = Constraint(expr=   m.b1648 + m.b1649 + m.b1650 + m.b1651 + m.b1652 + m.b1653 + m.b1654 + m.b1655 + m.b1656
                           + m.b1657 + m.b1658 + m.b1659 + m.b1660 == 1)

m.c1596 = Constraint(expr=   m.b1661 + m.b1662 + m.b1663 + m.b1664 + m.b1665 + m.b1666 + m.b1667 + m.b1668 + m.b1669
                           + m.b1670 + m.b1671 + m.b1672 + m.b1673 == 1)

m.c1597 = Constraint(expr=   m.b1674 + m.b1675 + m.b1676 + m.b1677 + m.b1678 + m.b1679 + m.b1680 + m.b1681 + m.b1682
                           + m.b1683 + m.b1684 + m.b1685 + m.b1686 == 1)

m.c1598 = Constraint(expr=   m.b1687 + m.b1688 + m.b1689 + m.b1690 + m.b1691 + m.b1692 + m.b1693 + m.b1694 + m.b1695
                           + m.b1696 + m.b1697 + m.b1698 + m.b1699 == 1)

m.c1599 = Constraint(expr=   m.b1700 + m.b1701 + m.b1702 + m.b1703 + m.b1704 + m.b1705 + m.b1706 + m.b1707 + m.b1708
                           + m.b1709 + m.b1710 + m.b1711 + m.b1712 == 1)

m.c1600 = Constraint(expr=   m.b1713 + m.b1714 + m.b1715 + m.b1716 + m.b1717 + m.b1718 + m.b1719 + m.b1720 + m.b1721
                           + m.b1722 + m.b1723 + m.b1724 + m.b1725 == 1)

m.c1601 = Constraint(expr=   m.b1726 + m.b1727 + m.b1728 + m.b1729 + m.b1730 + m.b1731 + m.b1732 + m.b1733 + m.b1734
                           + m.b1735 + m.b1736 + m.b1737 + m.b1738 == 1)

m.c1602 = Constraint(expr=   m.b1739 + m.b1740 + m.b1741 + m.b1742 + m.b1743 + m.b1744 + m.b1745 + m.b1746 + m.b1747
                           + m.b1748 + m.b1749 + m.b1750 + m.b1751 == 1)

m.c1603 = Constraint(expr=   m.b1752 + m.b1753 + m.b1754 + m.b1755 + m.b1756 + m.b1757 + m.b1758 + m.b1759 + m.b1760
                           + m.b1761 + m.b1762 + m.b1763 + m.b1764 == 1)

m.c1604 = Constraint(expr=   m.b1765 + m.b1766 + m.b1767 + m.b1768 + m.b1769 + m.b1770 + m.b1771 + m.b1772 + m.b1773
                           + m.b1774 + m.b1775 + m.b1776 + m.b1777 == 1)

m.c1605 = Constraint(expr=   m.b1778 + m.b1779 + m.b1780 + m.b1781 + m.b1782 + m.b1783 + m.b1784 + m.b1785 + m.b1786
                           + m.b1787 + m.b1788 + m.b1789 + m.b1790 == 1)

m.c1606 = Constraint(expr=   m.b1791 + m.b1792 + m.b1793 + m.b1794 + m.b1795 + m.b1796 + m.b1797 + m.b1798 + m.b1799
                           + m.b1800 + m.b1801 + m.b1802 + m.b1803 == 1)

m.c1607 = Constraint(expr=   m.b1804 + m.b1805 + m.b1806 + m.b1807 + m.b1808 + m.b1809 + m.b1810 + m.b1811 + m.b1812
                           + m.b1813 + m.b1814 + m.b1815 + m.b1816 == 1)

m.c1608 = Constraint(expr=   m.b1817 + m.b1818 + m.b1819 + m.b1820 + m.b1821 + m.b1822 + m.b1823 + m.b1824 + m.b1825
                           + m.b1826 + m.b1827 + m.b1828 + m.b1829 == 1)

m.c1609 = Constraint(expr=   m.b1830 + m.b1831 + m.b1832 + m.b1833 + m.b1834 + m.b1835 + m.b1836 + m.b1837 + m.b1838
                           + m.b1839 + m.b1840 + m.b1841 + m.b1842 == 1)

m.c1610 = Constraint(expr=   m.b1843 + m.b1844 + m.b1845 + m.b1846 + m.b1847 + m.b1848 + m.b1849 + m.b1850 + m.b1851
                           + m.b1852 + m.b1853 + m.b1854 + m.b1855 == 1)

m.c1611 = Constraint(expr=   m.b1856 + m.b1857 + m.b1858 + m.b1859 + m.b1860 + m.b1861 + m.b1862 + m.b1863 + m.b1864
                           + m.b1865 + m.b1866 + m.b1867 + m.b1868 == 1)

m.c1612 = Constraint(expr=   m.b1869 + m.b1870 + m.b1871 + m.b1872 + m.b1873 + m.b1874 + m.b1875 + m.b1876 + m.b1877
                           + m.b1878 + m.b1879 + m.b1880 + m.b1881 == 1)

m.c1613 = Constraint(expr=   m.b1882 + m.b1883 + m.b1884 + m.b1885 + m.b1886 + m.b1887 + m.b1888 + m.b1889 + m.b1890
                           + m.b1891 + m.b1892 + m.b1893 + m.b1894 == 1)

m.c1614 = Constraint(expr=   m.b1895 + m.b1896 + m.b1897 + m.b1898 + m.b1899 + m.b1900 + m.b1901 + m.b1902 + m.b1903
                           + m.b1904 + m.b1905 + m.b1906 + m.b1907 == 1)

m.c1615 = Constraint(expr=   m.b1908 + m.b1909 + m.b1910 + m.b1911 + m.b1912 + m.b1913 + m.b1914 + m.b1915 + m.b1916
                           + m.b1917 + m.b1918 + m.b1919 + m.b1920 == 1)

m.c1616 = Constraint(expr=   m.b1921 + m.b1922 + m.b1923 + m.b1924 + m.b1925 + m.b1926 + m.b1927 + m.b1928 + m.b1929
                           + m.b1930 + m.b1931 + m.b1932 + m.b1933 == 1)

m.c1617 = Constraint(expr=   m.b1934 + m.b1935 + m.b1936 + m.b1937 + m.b1938 + m.b1939 + m.b1940 + m.b1941 + m.b1942
                           + m.b1943 + m.b1944 + m.b1945 + m.b1946 == 1)

m.c1618 = Constraint(expr=   m.b1947 + m.b1948 + m.b1949 + m.b1950 + m.b1951 + m.b1952 + m.b1953 + m.b1954 + m.b1955
                           + m.b1956 + m.b1957 + m.b1958 + m.b1959 == 1)

m.c1619 = Constraint(expr=   m.b1960 + m.b1961 + m.b1962 + m.b1963 + m.b1964 + m.b1965 + m.b1966 + m.b1967 + m.b1968
                           + m.b1969 + m.b1970 + m.b1971 + m.b1972 == 1)

m.c1620 = Constraint(expr=   m.b1973 + m.b1974 + m.b1975 + m.b1976 + m.b1977 + m.b1978 + m.b1979 + m.b1980 + m.b1981
                           + m.b1982 + m.b1983 + m.b1984 + m.b1985 == 1)

m.c1621 = Constraint(expr=   m.b1986 + m.b1987 + m.b1988 + m.b1989 + m.b1990 + m.b1991 + m.b1992 + m.b1993 + m.b1994
                           + m.b1995 + m.b1996 + m.b1997 + m.b1998 == 1)

m.c1622 = Constraint(expr=   m.b1999 + m.b2000 + m.b2001 + m.b2002 + m.b2003 + m.b2004 + m.b2005 + m.b2006 + m.b2007
                           + m.b2008 + m.b2009 + m.b2010 + m.b2011 == 1)

m.c1623 = Constraint(expr=   m.b2012 + m.b2013 + m.b2014 + m.b2015 + m.b2016 + m.b2017 + m.b2018 + m.b2019 + m.b2020
                           + m.b2021 + m.b2022 + m.b2023 + m.b2024 == 1)

m.c1624 = Constraint(expr=   m.b2025 + m.b2026 + m.b2027 + m.b2028 + m.b2029 + m.b2030 + m.b2031 + m.b2032 + m.b2033
                           + m.b2034 + m.b2035 + m.b2036 + m.b2037 == 1)

m.c1625 = Constraint(expr=   m.b2038 + m.b2039 + m.b2040 + m.b2041 + m.b2042 + m.b2043 + m.b2044 + m.b2045 + m.b2046
                           + m.b2047 + m.b2048 + m.b2049 + m.b2050 == 1)

m.c1626 = Constraint(expr=   m.b2051 + m.b2052 + m.b2053 + m.b2054 + m.b2055 + m.b2056 + m.b2057 + m.b2058 + m.b2059
                           + m.b2060 + m.b2061 + m.b2062 + m.b2063 == 1)

m.c1627 = Constraint(expr=   m.b2064 + m.b2065 + m.b2066 + m.b2067 + m.b2068 + m.b2069 + m.b2070 + m.b2071 + m.b2072
                           + m.b2073 + m.b2074 + m.b2075 + m.b2076 == 1)

m.c1628 = Constraint(expr=   m.b2077 + m.b2078 + m.b2079 + m.b2080 + m.b2081 + m.b2082 + m.b2083 + m.b2084 + m.b2085
                           + m.b2086 + m.b2087 + m.b2088 + m.b2089 == 1)

m.c1629 = Constraint(expr=   m.b2090 + m.b2091 + m.b2092 + m.b2093 + m.b2094 + m.b2095 + m.b2096 + m.b2097 + m.b2098
                           + m.b2099 + m.b2100 + m.b2101 + m.b2102 == 1)

m.c1630 = Constraint(expr=   m.b2103 + m.b2104 + m.b2105 + m.b2106 + m.b2107 + m.b2108 + m.b2109 + m.b2110 + m.b2111
                           + m.b2112 + m.b2113 + m.b2114 + m.b2115 == 1)

m.c1631 = Constraint(expr=   m.b2116 + m.b2117 + m.b2118 + m.b2119 + m.b2120 + m.b2121 + m.b2122 + m.b2123 + m.b2124
                           + m.b2125 + m.b2126 + m.b2127 + m.b2128 == 1)

m.c1632 = Constraint(expr=   m.b2129 + m.b2130 + m.b2131 + m.b2132 + m.b2133 + m.b2134 + m.b2135 + m.b2136 + m.b2137
                           + m.b2138 + m.b2139 + m.b2140 + m.b2141 == 1)

m.c1633 = Constraint(expr=   m.b2142 + m.b2143 + m.b2144 + m.b2145 + m.b2146 + m.b2147 + m.b2148 + m.b2149 + m.b2150
                           + m.b2151 + m.b2152 + m.b2153 + m.b2154 == 1)

m.c1634 = Constraint(expr=   m.b2155 + m.b2156 + m.b2157 + m.b2158 + m.b2159 + m.b2160 + m.b2161 + m.b2162 + m.b2163
                           + m.b2164 + m.b2165 + m.b2166 + m.b2167 == 1)

m.c1635 = Constraint(expr=   m.b2168 + m.b2169 + m.b2170 + m.b2171 + m.b2172 + m.b2173 + m.b2174 + m.b2175 + m.b2176
                           + m.b2177 + m.b2178 + m.b2179 + m.b2180 == 1)

m.c1636 = Constraint(expr=   m.b2181 + m.b2182 + m.b2183 + m.b2184 + m.b2185 + m.b2186 + m.b2187 + m.b2188 + m.b2189
                           + m.b2190 + m.b2191 + m.b2192 + m.b2193 == 1)

m.c1637 = Constraint(expr=   m.b2194 + m.b2195 + m.b2196 + m.b2197 + m.b2198 + m.b2199 + m.b2200 + m.b2201 + m.b2202
                           + m.b2203 + m.b2204 + m.b2205 + m.b2206 == 1)

m.c1638 = Constraint(expr=   m.b2207 + m.b2208 + m.b2209 + m.b2210 + m.b2211 + m.b2212 + m.b2213 + m.b2214 + m.b2215
                           + m.b2216 + m.b2217 + m.b2218 + m.b2219 == 1)

m.c1639 = Constraint(expr=   m.b2220 + m.b2221 + m.b2222 + m.b2223 + m.b2224 + m.b2225 + m.b2226 + m.b2227 + m.b2228
                           + m.b2229 + m.b2230 + m.b2231 + m.b2232 == 1)

m.c1640 = Constraint(expr=   m.b2233 + m.b2234 + m.b2235 + m.b2236 + m.b2237 + m.b2238 + m.b2239 + m.b2240 + m.b2241
                           + m.b2242 + m.b2243 + m.b2244 + m.b2245 == 1)

m.c1641 = Constraint(expr=   m.b2246 + m.b2247 + m.b2248 + m.b2249 + m.b2250 + m.b2251 + m.b2252 + m.b2253 + m.b2254
                           + m.b2255 + m.b2256 + m.b2257 + m.b2258 == 1)

m.c1642 = Constraint(expr=   m.b2259 + m.b2260 + m.b2261 + m.b2262 + m.b2263 + m.b2264 + m.b2265 + m.b2266 + m.b2267
                           + m.b2268 + m.b2269 + m.b2270 + m.b2271 == 1)

m.c1643 = Constraint(expr=   m.b2272 + m.b2273 + m.b2274 + m.b2275 + m.b2276 + m.b2277 + m.b2278 + m.b2279 + m.b2280
                           + m.b2281 + m.b2282 + m.b2283 + m.b2284 == 1)

m.c1644 = Constraint(expr=   m.b2285 + m.b2286 + m.b2287 + m.b2288 + m.b2289 + m.b2290 + m.b2291 + m.b2292 + m.b2293
                           + m.b2294 + m.b2295 + m.b2296 + m.b2297 == 1)

m.c1645 = Constraint(expr=   m.b2298 + m.b2299 + m.b2300 + m.b2301 + m.b2302 + m.b2303 + m.b2304 + m.b2305 + m.b2306
                           + m.b2307 + m.b2308 + m.b2309 + m.b2310 == 1)

m.c1646 = Constraint(expr=   m.b2311 + m.b2312 + m.b2313 + m.b2314 + m.b2315 + m.b2316 + m.b2317 + m.b2318 + m.b2319
                           + m.b2320 + m.b2321 + m.b2322 + m.b2323 == 1)

m.c1647 = Constraint(expr=   m.b2324 + m.b2325 + m.b2326 + m.b2327 + m.b2328 + m.b2329 + m.b2330 + m.b2331 + m.b2332
                           + m.b2333 + m.b2334 + m.b2335 + m.b2336 == 1)

m.c1648 = Constraint(expr=   m.b2337 + m.b2338 + m.b2339 + m.b2340 + m.b2341 + m.b2342 + m.b2343 + m.b2344 + m.b2345
                           + m.b2346 + m.b2347 + m.b2348 + m.b2349 == 1)

m.c1649 = Constraint(expr=   m.b2350 + m.b2351 + m.b2352 + m.b2353 + m.b2354 + m.b2355 + m.b2356 + m.b2357 + m.b2358
                           + m.b2359 + m.b2360 + m.b2361 + m.b2362 == 1)

m.c1650 = Constraint(expr=   m.b2363 + m.b2364 + m.b2365 + m.b2366 + m.b2367 + m.b2368 + m.b2369 + m.b2370 + m.b2371
                           + m.b2372 + m.b2373 + m.b2374 + m.b2375 == 1)

m.c1651 = Constraint(expr=   m.b2376 + m.b2377 + m.b2378 + m.b2379 + m.b2380 + m.b2381 + m.b2382 + m.b2383 + m.b2384
                           + m.b2385 + m.b2386 + m.b2387 + m.b2388 == 1)

m.c1652 = Constraint(expr=   m.b2389 + m.b2390 + m.b2391 + m.b2392 + m.b2393 + m.b2394 + m.b2395 + m.b2396 + m.b2397
                           + m.b2398 + m.b2399 + m.b2400 + m.b2401 == 1)

m.c1653 = Constraint(expr=   m.b2402 + m.b2403 + m.b2404 + m.b2405 + m.b2406 + m.b2407 + m.b2408 + m.b2409 + m.b2410
                           + m.b2411 + m.b2412 + m.b2413 + m.b2414 == 1)

m.c1654 = Constraint(expr=   m.b2415 + m.b2416 + m.b2417 + m.b2418 + m.b2419 + m.b2420 + m.b2421 + m.b2422 + m.b2423
                           + m.b2424 + m.b2425 + m.b2426 + m.b2427 == 1)

m.c1655 = Constraint(expr=   m.b2428 + m.b2429 + m.b2430 + m.b2431 + m.b2432 + m.b2433 + m.b2434 + m.b2435 + m.b2436
                           + m.b2437 + m.b2438 + m.b2439 + m.b2440 == 1)

m.c1656 = Constraint(expr=   m.b2441 + m.b2442 + m.b2443 + m.b2444 + m.b2445 + m.b2446 + m.b2447 + m.b2448 + m.b2449
                           + m.b2450 + m.b2451 + m.b2452 + m.b2453 == 1)

m.c1657 = Constraint(expr=   m.b2454 + m.b2455 + m.b2456 + m.b2457 + m.b2458 + m.b2459 + m.b2460 + m.b2461 + m.b2462
                           + m.b2463 + m.b2464 + m.b2465 + m.b2466 == 1)

m.c1658 = Constraint(expr=   m.b2467 + m.b2468 + m.b2469 + m.b2470 + m.b2471 + m.b2472 + m.b2473 + m.b2474 + m.b2475
                           + m.b2476 + m.b2477 + m.b2478 + m.b2479 == 1)

m.c1659 = Constraint(expr=   m.b2480 + m.b2481 + m.b2482 + m.b2483 + m.b2484 + m.b2485 + m.b2486 + m.b2487 + m.b2488
                           + m.b2489 + m.b2490 + m.b2491 + m.b2492 == 1)

m.c1660 = Constraint(expr=   m.b2493 + m.b2494 + m.b2495 + m.b2496 + m.b2497 + m.b2498 + m.b2499 + m.b2500 + m.b2501
                           + m.b2502 + m.b2503 + m.b2504 + m.b2505 == 1)

m.c1661 = Constraint(expr=   m.b2506 + m.b2507 + m.b2508 + m.b2509 + m.b2510 + m.b2511 + m.b2512 + m.b2513 + m.b2514
                           + m.b2515 + m.b2516 + m.b2517 + m.b2518 == 1)

m.c1662 = Constraint(expr=   m.b2519 + m.b2520 + m.b2521 + m.b2522 + m.b2523 + m.b2524 + m.b2525 + m.b2526 + m.b2527
                           + m.b2528 + m.b2529 + m.b2530 + m.b2531 == 1)

m.c1663 = Constraint(expr=   m.b2532 + m.b2533 + m.b2534 + m.b2535 + m.b2536 + m.b2537 + m.b2538 + m.b2539 + m.b2540
                           + m.b2541 + m.b2542 + m.b2543 + m.b2544 == 1)

m.c1664 = Constraint(expr=   m.b2545 + m.b2546 + m.b2547 + m.b2548 + m.b2549 + m.b2550 + m.b2551 + m.b2552 + m.b2553
                           + m.b2554 + m.b2555 + m.b2556 + m.b2557 == 1)

m.c1665 = Constraint(expr=   m.b2558 + m.b2559 + m.b2560 + m.b2561 + m.b2562 + m.b2563 + m.b2564 + m.b2565 + m.b2566
                           + m.b2567 + m.b2568 + m.b2569 + m.b2570 == 1)

m.c1666 = Constraint(expr=   m.b2571 + m.b2572 + m.b2573 + m.b2574 + m.b2575 + m.b2576 + m.b2577 + m.b2578 + m.b2579
                           + m.b2580 + m.b2581 + m.b2582 + m.b2583 == 1)

m.c1667 = Constraint(expr=   m.b2584 + m.b2585 + m.b2586 + m.b2587 + m.b2588 + m.b2589 + m.b2590 + m.b2591 + m.b2592
                           + m.b2593 + m.b2594 + m.b2595 + m.b2596 == 1)

m.c1668 = Constraint(expr=   m.b2597 + m.b2598 + m.b2599 + m.b2600 + m.b2601 + m.b2602 + m.b2603 + m.b2604 + m.b2605
                           + m.b2606 + m.b2607 + m.b2608 + m.b2609 == 1)

m.c1669 = Constraint(expr=   m.b2610 + m.b2611 + m.b2612 + m.b2613 + m.b2614 + m.b2615 + m.b2616 + m.b2617 + m.b2618
                           + m.b2619 + m.b2620 + m.b2621 + m.b2622 == 1)

m.c1670 = Constraint(expr=   m.b2623 + m.b2624 + m.b2625 + m.b2626 + m.b2627 + m.b2628 + m.b2629 + m.b2630 + m.b2631
                           + m.b2632 + m.b2633 + m.b2634 + m.b2635 == 1)

m.c1671 = Constraint(expr=   m.b2636 + m.b2637 + m.b2638 + m.b2639 + m.b2640 + m.b2641 + m.b2642 + m.b2643 + m.b2644
                           + m.b2645 + m.b2646 + m.b2647 + m.b2648 == 1)

m.c1672 = Constraint(expr=   m.b2649 + m.b2650 + m.b2651 + m.b2652 + m.b2653 + m.b2654 + m.b2655 + m.b2656 + m.b2657
                           + m.b2658 + m.b2659 + m.b2660 + m.b2661 == 1)

m.c1673 = Constraint(expr=   m.b2662 + m.b2663 + m.b2664 + m.b2665 + m.b2666 + m.b2667 + m.b2668 + m.b2669 + m.b2670
                           + m.b2671 + m.b2672 + m.b2673 + m.b2674 == 1)

m.c1674 = Constraint(expr=   m.b2675 + m.b2676 + m.b2677 + m.b2678 + m.b2679 + m.b2680 + m.b2681 + m.b2682 + m.b2683
                           + m.b2684 + m.b2685 + m.b2686 + m.b2687 == 1)

m.c1675 = Constraint(expr=   m.b2688 + m.b2689 + m.b2690 + m.b2691 + m.b2692 + m.b2693 + m.b2694 + m.b2695 + m.b2696
                           + m.b2697 + m.b2698 + m.b2699 + m.b2700 == 1)

m.c1676 = Constraint(expr=   m.b2701 + m.b2702 + m.b2703 + m.b2704 + m.b2705 + m.b2706 + m.b2707 + m.b2708 + m.b2709
                           + m.b2710 + m.b2711 + m.b2712 + m.b2713 == 1)

m.c1677 = Constraint(expr=   m.b2714 + m.b2715 + m.b2716 + m.b2717 + m.b2718 + m.b2719 + m.b2720 + m.b2721 + m.b2722
                           + m.b2723 + m.b2724 + m.b2725 + m.b2726 == 1)

m.c1678 = Constraint(expr=   m.b2727 + m.b2728 + m.b2729 + m.b2730 + m.b2731 + m.b2732 + m.b2733 + m.b2734 + m.b2735
                           + m.b2736 + m.b2737 + m.b2738 + m.b2739 == 1)

m.c1679 = Constraint(expr=   m.b2740 + m.b2741 + m.b2742 + m.b2743 + m.b2744 + m.b2745 + m.b2746 + m.b2747 + m.b2748
                           + m.b2749 + m.b2750 + m.b2751 + m.b2752 == 1)

m.c1680 = Constraint(expr=   m.b2753 + m.b2754 + m.b2755 + m.b2756 + m.b2757 + m.b2758 + m.b2759 + m.b2760 + m.b2761
                           + m.b2762 + m.b2763 + m.b2764 + m.b2765 == 1)

m.c1681 = Constraint(expr=   m.b2766 + m.b2767 + m.b2768 + m.b2769 + m.b2770 + m.b2771 + m.b2772 + m.b2773 + m.b2774
                           + m.b2775 + m.b2776 + m.b2777 + m.b2778 == 1)

m.c1682 = Constraint(expr=   m.b2779 + m.b2780 + m.b2781 + m.b2782 + m.b2783 + m.b2784 + m.b2785 + m.b2786 + m.b2787
                           + m.b2788 + m.b2789 + m.b2790 + m.b2791 == 1)

m.c1683 = Constraint(expr=   m.b2792 + m.b2793 + m.b2794 + m.b2795 + m.b2796 + m.b2797 + m.b2798 + m.b2799 + m.b2800
                           + m.b2801 + m.b2802 + m.b2803 + m.b2804 == 1)

m.c1684 = Constraint(expr=   m.b2805 + m.b2806 + m.b2807 + m.b2808 + m.b2809 + m.b2810 + m.b2811 + m.b2812 + m.b2813
                           + m.b2814 + m.b2815 + m.b2816 + m.b2817 == 1)

m.c1685 = Constraint(expr=   m.b2818 + m.b2819 + m.b2820 + m.b2821 + m.b2822 + m.b2823 + m.b2824 + m.b2825 + m.b2826
                           + m.b2827 + m.b2828 + m.b2829 + m.b2830 == 1)

m.c1686 = Constraint(expr=   m.b2831 + m.b2832 + m.b2833 + m.b2834 + m.b2835 + m.b2836 + m.b2837 + m.b2838 + m.b2839
                           + m.b2840 + m.b2841 + m.b2842 + m.b2843 == 1)

m.c1687 = Constraint(expr=   m.b2844 + m.b2845 + m.b2846 + m.b2847 + m.b2848 + m.b2849 + m.b2850 + m.b2851 + m.b2852
                           + m.b2853 + m.b2854 + m.b2855 + m.b2856 == 1)

m.c1688 = Constraint(expr=   m.b2857 + m.b2858 + m.b2859 + m.b2860 + m.b2861 + m.b2862 + m.b2863 + m.b2864 + m.b2865
                           + m.b2866 + m.b2867 + m.b2868 + m.b2869 == 1)

m.c1689 = Constraint(expr=   m.b2870 + m.b2871 + m.b2872 + m.b2873 + m.b2874 + m.b2875 + m.b2876 + m.b2877 + m.b2878
                           + m.b2879 + m.b2880 + m.b2881 + m.b2882 == 1)

m.c1690 = Constraint(expr=   m.b2883 + m.b2884 + m.b2885 + m.b2886 + m.b2887 + m.b2888 + m.b2889 + m.b2890 + m.b2891
                           + m.b2892 + m.b2893 + m.b2894 + m.b2895 == 1)

m.c1691 = Constraint(expr=   m.b2896 + m.b2897 + m.b2898 + m.b2899 + m.b2900 + m.b2901 + m.b2902 + m.b2903 + m.b2904
                           + m.b2905 + m.b2906 + m.b2907 + m.b2908 == 1)

m.c1692 = Constraint(expr=   m.b2909 + m.b2910 + m.b2911 + m.b2912 + m.b2913 + m.b2914 + m.b2915 + m.b2916 + m.b2917
                           + m.b2918 + m.b2919 + m.b2920 + m.b2921 == 1)

m.c1693 = Constraint(expr=   m.b2922 + m.b2923 + m.b2924 + m.b2925 + m.b2926 + m.b2927 + m.b2928 + m.b2929 + m.b2930
                           + m.b2931 + m.b2932 + m.b2933 + m.b2934 == 1)

m.c1694 = Constraint(expr=   m.b2935 + m.b2936 + m.b2937 + m.b2938 + m.b2939 + m.b2940 + m.b2941 + m.b2942 + m.b2943
                           + m.b2944 + m.b2945 + m.b2946 + m.b2947 == 1)

m.c1695 = Constraint(expr=   m.b2948 + m.b2949 + m.b2950 + m.b2951 + m.b2952 + m.b2953 + m.b2954 + m.b2955 + m.b2956
                           + m.b2957 + m.b2958 + m.b2959 + m.b2960 == 1)

m.c1696 = Constraint(expr=   m.b2961 + m.b2962 + m.b2963 + m.b2964 + m.b2965 + m.b2966 + m.b2967 + m.b2968 + m.b2969
                           + m.b2970 + m.b2971 + m.b2972 + m.b2973 == 1)

m.c1697 = Constraint(expr=   m.b2974 + m.b2975 + m.b2976 + m.b2977 + m.b2978 + m.b2979 + m.b2980 + m.b2981 + m.b2982
                           + m.b2983 + m.b2984 + m.b2985 + m.b2986 == 1)

m.c1698 = Constraint(expr=   m.b2987 + m.b2988 + m.b2989 + m.b2990 + m.b2991 + m.b2992 + m.b2993 + m.b2994 + m.b2995
                           + m.b2996 + m.b2997 + m.b2998 + m.b2999 == 1)

m.c1699 = Constraint(expr=   m.b3000 + m.b3001 + m.b3002 + m.b3003 + m.b3004 + m.b3005 + m.b3006 + m.b3007 + m.b3008
                           + m.b3009 + m.b3010 + m.b3011 + m.b3012 == 1)

m.c1700 = Constraint(expr=   m.b3013 + m.b3014 + m.b3015 + m.b3016 + m.b3017 + m.b3018 + m.b3019 + m.b3020 + m.b3021
                           + m.b3022 + m.b3023 + m.b3024 + m.b3025 == 1)

m.c1701 = Constraint(expr=   m.b3026 + m.b3027 + m.b3028 + m.b3029 + m.b3030 + m.b3031 + m.b3032 + m.b3033 + m.b3034
                           + m.b3035 + m.b3036 + m.b3037 + m.b3038 == 1)

m.c1702 = Constraint(expr=   m.b3039 + m.b3040 + m.b3041 + m.b3042 + m.b3043 + m.b3044 + m.b3045 + m.b3046 + m.b3047
                           + m.b3048 + m.b3049 + m.b3050 + m.b3051 == 1)

m.c1703 = Constraint(expr=   m.b3052 + m.b3053 + m.b3054 + m.b3055 + m.b3056 + m.b3057 + m.b3058 + m.b3059 + m.b3060
                           + m.b3061 + m.b3062 + m.b3063 + m.b3064 == 1)

m.c1704 = Constraint(expr=   m.b3065 + m.b3066 + m.b3067 + m.b3068 + m.b3069 + m.b3070 + m.b3071 + m.b3072 + m.b3073
                           + m.b3074 + m.b3075 + m.b3076 + m.b3077 == 1)

m.c1705 = Constraint(expr=   m.b3078 + m.b3079 + m.b3080 + m.b3081 + m.b3082 + m.b3083 + m.b3084 + m.b3085 + m.b3086
                           + m.b3087 + m.b3088 + m.b3089 + m.b3090 == 1)

m.c1706 = Constraint(expr=   m.b3091 + m.b3092 + m.b3093 + m.b3094 + m.b3095 + m.b3096 + m.b3097 + m.b3098 + m.b3099
                           + m.b3100 + m.b3101 + m.b3102 + m.b3103 == 1)

m.c1707 = Constraint(expr=   m.b3104 + m.b3105 + m.b3106 + m.b3107 + m.b3108 + m.b3109 + m.b3110 + m.b3111 + m.b3112
                           + m.b3113 + m.b3114 + m.b3115 + m.b3116 == 1)

m.c1708 = Constraint(expr=   m.b3117 + m.b3118 + m.b3119 + m.b3120 + m.b3121 + m.b3122 + m.b3123 + m.b3124 + m.b3125
                           + m.b3126 + m.b3127 + m.b3128 + m.b3129 == 1)

m.c1709 = Constraint(expr=   m.b3130 + m.b3131 + m.b3132 + m.b3133 + m.b3134 + m.b3135 + m.b3136 + m.b3137 + m.b3138
                           + m.b3139 + m.b3140 + m.b3141 + m.b3142 == 1)

m.c1710 = Constraint(expr=   m.b3143 + m.b3144 + m.b3145 + m.b3146 + m.b3147 + m.b3148 + m.b3149 + m.b3150 + m.b3151
                           + m.b3152 + m.b3153 + m.b3154 + m.b3155 == 1)

m.c1711 = Constraint(expr=   m.b3156 + m.b3157 + m.b3158 + m.b3159 + m.b3160 + m.b3161 + m.b3162 + m.b3163 + m.b3164
                           + m.b3165 + m.b3166 + m.b3167 + m.b3168 == 1)

m.c1712 = Constraint(expr=   m.b3169 + m.b3170 + m.b3171 + m.b3172 + m.b3173 + m.b3174 + m.b3175 + m.b3176 + m.b3177
                           + m.b3178 + m.b3179 + m.b3180 + m.b3181 == 1)

m.c1713 = Constraint(expr=   m.b3182 + m.b3183 + m.b3184 + m.b3185 + m.b3186 + m.b3187 + m.b3188 + m.b3189 + m.b3190
                           + m.b3191 + m.b3192 + m.b3193 + m.b3194 == 1)

m.c1714 = Constraint(expr=   m.b3195 + m.b3196 + m.b3197 + m.b3198 + m.b3199 + m.b3200 + m.b3201 + m.b3202 + m.b3203
                           + m.b3204 + m.b3205 + m.b3206 + m.b3207 == 1)

m.c1715 = Constraint(expr=   m.b3208 + m.b3209 + m.b3210 + m.b3211 + m.b3212 + m.b3213 + m.b3214 + m.b3215 + m.b3216
                           + m.b3217 + m.b3218 + m.b3219 + m.b3220 == 1)

m.c1716 = Constraint(expr=   m.b3221 + m.b3222 + m.b3223 + m.b3224 + m.b3225 + m.b3226 + m.b3227 + m.b3228 + m.b3229
                           + m.b3230 + m.b3231 + m.b3232 + m.b3233 == 1)

m.c1717 = Constraint(expr=   m.b3234 + m.b3235 + m.b3236 + m.b3237 + m.b3238 + m.b3239 + m.b3240 + m.b3241 + m.b3242
                           + m.b3243 + m.b3244 + m.b3245 + m.b3246 == 1)

m.c1718 = Constraint(expr=   m.b3247 + m.b3248 + m.b3249 + m.b3250 + m.b3251 + m.b3252 + m.b3253 + m.b3254 + m.b3255
                           + m.b3256 + m.b3257 + m.b3258 + m.b3259 == 1)

m.c1719 = Constraint(expr=   m.b3260 + m.b3261 + m.b3262 + m.b3263 + m.b3264 + m.b3265 + m.b3266 + m.b3267 + m.b3268
                           + m.b3269 + m.b3270 + m.b3271 + m.b3272 == 1)

m.c1720 = Constraint(expr=   m.b3273 + m.b3274 + m.b3275 + m.b3276 + m.b3277 + m.b3278 + m.b3279 + m.b3280 + m.b3281
                           + m.b3282 + m.b3283 + m.b3284 + m.b3285 == 1)

m.c1721 = Constraint(expr=   m.b3286 + m.b3287 + m.b3288 + m.b3289 + m.b3290 + m.b3291 + m.b3292 + m.b3293 + m.b3294
                           + m.b3295 + m.b3296 + m.b3297 + m.b3298 == 1)

m.c1722 = Constraint(expr=   m.b3299 + m.b3300 + m.b3301 + m.b3302 + m.b3303 + m.b3304 + m.b3305 + m.b3306 + m.b3307
                           + m.b3308 + m.b3309 + m.b3310 + m.b3311 == 1)

m.c1723 = Constraint(expr=   m.b3312 + m.b3313 + m.b3314 + m.b3315 + m.b3316 + m.b3317 + m.b3318 + m.b3319 + m.b3320
                           + m.b3321 + m.b3322 + m.b3323 + m.b3324 == 1)

m.c1724 = Constraint(expr=   m.b3325 + m.b3326 + m.b3327 + m.b3328 + m.b3329 + m.b3330 + m.b3331 + m.b3332 + m.b3333
                           + m.b3334 + m.b3335 + m.b3336 + m.b3337 == 1)

m.c1725 = Constraint(expr=   m.b3338 + m.b3339 + m.b3340 + m.b3341 + m.b3342 + m.b3343 + m.b3344 + m.b3345 + m.b3346
                           + m.b3347 + m.b3348 + m.b3349 + m.b3350 == 1)

m.c1726 = Constraint(expr=   m.b3351 + m.b3352 + m.b3353 + m.b3354 + m.b3355 + m.b3356 + m.b3357 + m.b3358 + m.b3359
                           + m.b3360 + m.b3361 + m.b3362 + m.b3363 == 1)

m.c1727 = Constraint(expr=   m.b3364 + m.b3365 + m.b3366 + m.b3367 + m.b3368 + m.b3369 + m.b3370 + m.b3371 + m.b3372
                           + m.b3373 + m.b3374 + m.b3375 + m.b3376 == 1)

m.c1728 = Constraint(expr=   m.b3377 + m.b3378 + m.b3379 + m.b3380 + m.b3381 + m.b3382 + m.b3383 + m.b3384 + m.b3385
                           + m.b3386 + m.b3387 + m.b3388 + m.b3389 == 1)

m.c1729 = Constraint(expr=   m.b3390 + m.b3391 + m.b3392 + m.b3393 + m.b3394 + m.b3395 + m.b3396 + m.b3397 + m.b3398
                           + m.b3399 + m.b3400 + m.b3401 + m.b3402 == 1)

m.c1730 = Constraint(expr=   m.b3403 + m.b3404 + m.b3405 + m.b3406 + m.b3407 + m.b3408 + m.b3409 + m.b3410 + m.b3411
                           + m.b3412 + m.b3413 + m.b3414 + m.b3415 == 1)

m.c1731 = Constraint(expr=   m.b3416 + m.b3417 + m.b3418 + m.b3419 + m.b3420 + m.b3421 + m.b3422 + m.b3423 + m.b3424
                           + m.b3425 + m.b3426 + m.b3427 + m.b3428 == 1)

m.c1732 = Constraint(expr=   m.b3429 + m.b3430 + m.b3431 + m.b3432 + m.b3433 + m.b3434 + m.b3435 + m.b3436 + m.b3437
                           + m.b3438 + m.b3439 + m.b3440 + m.b3441 == 1)

m.c1733 = Constraint(expr=   m.b3442 + m.b3443 + m.b3444 + m.b3445 + m.b3446 + m.b3447 + m.b3448 + m.b3449 + m.b3450
                           + m.b3451 + m.b3452 + m.b3453 + m.b3454 == 1)

m.c1734 = Constraint(expr=   m.b3455 + m.b3456 + m.b3457 + m.b3458 + m.b3459 + m.b3460 + m.b3461 + m.b3462 + m.b3463
                           + m.b3464 + m.b3465 + m.b3466 + m.b3467 == 1)

m.c1735 = Constraint(expr=   m.b3468 + m.b3469 + m.b3470 + m.b3471 + m.b3472 + m.b3473 + m.b3474 + m.b3475 + m.b3476
                           + m.b3477 + m.b3478 + m.b3479 + m.b3480 == 1)

m.c1736 = Constraint(expr=   m.b3481 + m.b3482 + m.b3483 + m.b3484 + m.b3485 + m.b3486 + m.b3487 + m.b3488 + m.b3489
                           + m.b3490 + m.b3491 + m.b3492 + m.b3493 == 1)

m.c1737 = Constraint(expr=   m.b3494 + m.b3495 + m.b3496 + m.b3497 + m.b3498 + m.b3499 + m.b3500 + m.b3501 + m.b3502
                           + m.b3503 + m.b3504 + m.b3505 + m.b3506 == 1)

m.c1738 = Constraint(expr=   m.b3507 + m.b3508 + m.b3509 + m.b3510 + m.b3511 + m.b3512 + m.b3513 + m.b3514 + m.b3515
                           + m.b3516 + m.b3517 + m.b3518 + m.b3519 == 1)

m.c1739 = Constraint(expr=   m.b3520 + m.b3521 + m.b3522 + m.b3523 + m.b3524 + m.b3525 + m.b3526 + m.b3527 + m.b3528
                           + m.b3529 + m.b3530 + m.b3531 + m.b3532 == 1)

m.c1740 = Constraint(expr=   m.b3533 + m.b3534 + m.b3535 + m.b3536 + m.b3537 + m.b3538 + m.b3539 + m.b3540 + m.b3541
                           + m.b3542 + m.b3543 + m.b3544 + m.b3545 == 1)

m.c1741 = Constraint(expr=   m.b3546 + m.b3547 + m.b3548 + m.b3549 + m.b3550 + m.b3551 + m.b3552 + m.b3553 + m.b3554
                           + m.b3555 + m.b3556 + m.b3557 + m.b3558 == 1)

m.c1742 = Constraint(expr=   m.b3559 + m.b3560 + m.b3561 + m.b3562 + m.b3563 + m.b3564 + m.b3565 + m.b3566 + m.b3567
                           + m.b3568 + m.b3569 + m.b3570 + m.b3571 == 1)

m.c1743 = Constraint(expr=   m.b3572 + m.b3573 + m.b3574 + m.b3575 + m.b3576 + m.b3577 + m.b3578 + m.b3579 + m.b3580
                           + m.b3581 + m.b3582 + m.b3583 + m.b3584 == 1)

m.c1744 = Constraint(expr=   m.b3585 + m.b3586 + m.b3587 + m.b3588 + m.b3589 + m.b3590 + m.b3591 + m.b3592 + m.b3593
                           + m.b3594 + m.b3595 + m.b3596 + m.b3597 == 1)

m.c1745 = Constraint(expr=   m.b3598 + m.b3599 + m.b3600 + m.b3601 + m.b3602 + m.b3603 + m.b3604 + m.b3605 + m.b3606
                           + m.b3607 + m.b3608 + m.b3609 + m.b3610 == 1)

m.c1746 = Constraint(expr=   m.b3611 + m.b3612 + m.b3613 + m.b3614 + m.b3615 + m.b3616 + m.b3617 + m.b3618 + m.b3619
                           + m.b3620 + m.b3621 + m.b3622 + m.b3623 == 1)

m.c1747 = Constraint(expr=   m.b3624 + m.b3625 + m.b3626 + m.b3627 + m.b3628 + m.b3629 + m.b3630 + m.b3631 + m.b3632
                           + m.b3633 + m.b3634 + m.b3635 + m.b3636 == 1)

m.c1748 = Constraint(expr=   m.b3637 + m.b3638 + m.b3639 + m.b3640 + m.b3641 + m.b3642 + m.b3643 + m.b3644 + m.b3645
                           + m.b3646 + m.b3647 + m.b3648 + m.b3649 == 1)

m.c1749 = Constraint(expr=   m.b3650 + m.b3651 + m.b3652 + m.b3653 + m.b3654 + m.b3655 + m.b3656 + m.b3657 + m.b3658
                           + m.b3659 + m.b3660 + m.b3661 + m.b3662 == 1)

m.c1750 = Constraint(expr=   m.b3663 + m.b3664 + m.b3665 + m.b3666 + m.b3667 + m.b3668 + m.b3669 + m.b3670 + m.b3671
                           + m.b3672 + m.b3673 + m.b3674 + m.b3675 == 1)

m.c1751 = Constraint(expr=   m.b3676 + m.b3677 + m.b3678 + m.b3679 + m.b3680 + m.b3681 + m.b3682 + m.b3683 + m.b3684
                           + m.b3685 + m.b3686 + m.b3687 + m.b3688 == 1)

m.c1752 = Constraint(expr=   m.b3689 + m.b3690 + m.b3691 + m.b3692 + m.b3693 + m.b3694 + m.b3695 + m.b3696 + m.b3697
                           + m.b3698 + m.b3699 + m.b3700 + m.b3701 == 1)

m.c1753 = Constraint(expr=   m.b3702 + m.b3703 + m.b3704 + m.b3705 + m.b3706 + m.b3707 + m.b3708 + m.b3709 + m.b3710
                           + m.b3711 + m.b3712 + m.b3713 + m.b3714 == 1)

m.c1754 = Constraint(expr=   m.b3715 + m.b3716 + m.b3717 + m.b3718 + m.b3719 + m.b3720 + m.b3721 + m.b3722 + m.b3723
                           + m.b3724 + m.b3725 + m.b3726 + m.b3727 == 1)

m.c1755 = Constraint(expr=   m.b3728 + m.b3729 + m.b3730 + m.b3731 + m.b3732 + m.b3733 + m.b3734 + m.b3735 + m.b3736
                           + m.b3737 + m.b3738 + m.b3739 + m.b3740 == 1)

m.c1756 = Constraint(expr=   m.b3741 + m.b3742 + m.b3743 + m.b3744 + m.b3745 + m.b3746 + m.b3747 + m.b3748 + m.b3749
                           + m.b3750 + m.b3751 + m.b3752 + m.b3753 == 1)

m.c1757 = Constraint(expr=   m.b3754 + m.b3755 + m.b3756 + m.b3757 + m.b3758 + m.b3759 + m.b3760 + m.b3761 + m.b3762
                           + m.b3763 + m.b3764 + m.b3765 + m.b3766 == 1)

m.c1758 = Constraint(expr=   m.b3767 + m.b3768 + m.b3769 + m.b3770 + m.b3771 + m.b3772 + m.b3773 + m.b3774 + m.b3775
                           + m.b3776 + m.b3777 + m.b3778 + m.b3779 == 1)

m.c1759 = Constraint(expr=   m.b3780 + m.b3781 + m.b3782 + m.b3783 + m.b3784 + m.b3785 + m.b3786 + m.b3787 + m.b3788
                           + m.b3789 + m.b3790 + m.b3791 + m.b3792 == 1)

m.c1760 = Constraint(expr=   m.b3793 + m.b3794 + m.b3795 + m.b3796 + m.b3797 + m.b3798 + m.b3799 + m.b3800 + m.b3801
                           + m.b3802 + m.b3803 + m.b3804 + m.b3805 == 1)

m.c1761 = Constraint(expr=   m.b3806 + m.b3807 + m.b3808 + m.b3809 + m.b3810 + m.b3811 + m.b3812 + m.b3813 + m.b3814
                           + m.b3815 + m.b3816 + m.b3817 + m.b3818 == 1)

m.c1762 = Constraint(expr=   m.b3819 + m.b3820 + m.b3821 + m.b3822 + m.b3823 + m.b3824 + m.b3825 + m.b3826 + m.b3827
                           + m.b3828 + m.b3829 + m.b3830 + m.b3831 == 1)

m.c1763 = Constraint(expr=   m.b3832 + m.b3833 + m.b3834 + m.b3835 + m.b3836 + m.b3837 + m.b3838 + m.b3839 + m.b3840
                           + m.b3841 + m.b3842 + m.b3843 + m.b3844 == 1)

m.c1764 = Constraint(expr=   m.b3845 + m.b3846 + m.b3847 + m.b3848 + m.b3849 + m.b3850 + m.b3851 + m.b3852 + m.b3853
                           + m.b3854 + m.b3855 + m.b3856 + m.b3857 == 1)

m.c1765 = Constraint(expr=   m.b3858 + m.b3859 + m.b3860 + m.b3861 + m.b3862 + m.b3863 + m.b3864 + m.b3865 + m.b3866
                           + m.b3867 + m.b3868 + m.b3869 + m.b3870 == 1)

m.c1766 = Constraint(expr=   m.b3871 + m.b3872 + m.b3873 + m.b3874 + m.b3875 + m.b3876 + m.b3877 + m.b3878 + m.b3879
                           + m.b3880 + m.b3881 + m.b3882 + m.b3883 == 1)

m.c1767 = Constraint(expr=   m.b3884 + m.b3885 + m.b3886 + m.b3887 + m.b3888 + m.b3889 + m.b3890 + m.b3891 + m.b3892
                           + m.b3893 + m.b3894 + m.b3895 + m.b3896 == 1)

m.c1768 = Constraint(expr=   m.b3897 + m.b3898 + m.b3899 + m.b3900 + m.b3901 + m.b3902 + m.b3903 + m.b3904 + m.b3905
                           + m.b3906 + m.b3907 + m.b3908 + m.b3909 == 1)

m.c1769 = Constraint(expr=   m.b3910 + m.b3911 + m.b3912 + m.b3913 + m.b3914 + m.b3915 + m.b3916 + m.b3917 + m.b3918
                           + m.b3919 + m.b3920 + m.b3921 + m.b3922 == 1)

m.c1770 = Constraint(expr=   m.b3923 + m.b3924 + m.b3925 + m.b3926 + m.b3927 + m.b3928 + m.b3929 + m.b3930 + m.b3931
                           + m.b3932 + m.b3933 + m.b3934 + m.b3935 == 1)

m.c1771 = Constraint(expr=   m.b3936 + m.b3937 + m.b3938 + m.b3939 + m.b3940 + m.b3941 + m.b3942 + m.b3943 + m.b3944
                           + m.b3945 + m.b3946 + m.b3947 + m.b3948 == 1)

m.c1772 = Constraint(expr=   m.b3949 + m.b3950 + m.b3951 + m.b3952 + m.b3953 + m.b3954 + m.b3955 + m.b3956 + m.b3957
                           + m.b3958 + m.b3959 + m.b3960 + m.b3961 == 1)

m.c1773 = Constraint(expr=   m.b3962 + m.b3963 + m.b3964 + m.b3965 + m.b3966 + m.b3967 + m.b3968 + m.b3969 + m.b3970
                           + m.b3971 + m.b3972 + m.b3973 + m.b3974 == 1)

m.c1774 = Constraint(expr=   m.b3975 + m.b3976 + m.b3977 + m.b3978 + m.b3979 + m.b3980 + m.b3981 + m.b3982 + m.b3983
                           + m.b3984 + m.b3985 + m.b3986 + m.b3987 == 1)

m.c1775 = Constraint(expr=   m.b3988 + m.b3989 + m.b3990 + m.b3991 + m.b3992 + m.b3993 + m.b3994 + m.b3995 + m.b3996
                           + m.b3997 + m.b3998 + m.b3999 + m.b4000 == 1)

m.c1776 = Constraint(expr=   m.b4001 + m.b4002 + m.b4003 + m.b4004 + m.b4005 + m.b4006 + m.b4007 + m.b4008 + m.b4009
                           + m.b4010 + m.b4011 + m.b4012 + m.b4013 == 1)

m.c1777 = Constraint(expr=   m.b4014 + m.b4015 + m.b4016 + m.b4017 + m.b4018 + m.b4019 + m.b4020 + m.b4021 + m.b4022
                           + m.b4023 + m.b4024 + m.b4025 + m.b4026 == 1)

m.c1778 = Constraint(expr=   m.b4027 + m.b4028 + m.b4029 + m.b4030 + m.b4031 + m.b4032 + m.b4033 + m.b4034 + m.b4035
                           + m.b4036 + m.b4037 + m.b4038 + m.b4039 == 1)

m.c1779 = Constraint(expr=   m.b4040 + m.b4041 + m.b4042 + m.b4043 + m.b4044 + m.b4045 + m.b4046 + m.b4047 + m.b4048
                           + m.b4049 + m.b4050 + m.b4051 + m.b4052 == 1)

m.c1780 = Constraint(expr=   m.b4053 + m.b4054 + m.b4055 + m.b4056 + m.b4057 + m.b4058 + m.b4059 + m.b4060 + m.b4061
                           + m.b4062 + m.b4063 + m.b4064 + m.b4065 == 1)

m.c1781 = Constraint(expr=   m.b4066 + m.b4067 + m.b4068 + m.b4069 + m.b4070 + m.b4071 + m.b4072 + m.b4073 + m.b4074
                           + m.b4075 + m.b4076 + m.b4077 + m.b4078 == 1)

m.c1782 = Constraint(expr=   m.b4079 + m.b4080 + m.b4081 + m.b4082 + m.b4083 + m.b4084 + m.b4085 + m.b4086 + m.b4087
                           + m.b4088 + m.b4089 + m.b4090 + m.b4091 == 1)

m.c1783 = Constraint(expr=   m.b4092 + m.b4093 + m.b4094 + m.b4095 + m.b4096 + m.b4097 + m.b4098 + m.b4099 + m.b4100
                           + m.b4101 + m.b4102 + m.b4103 + m.b4104 == 1)

m.c1784 = Constraint(expr=   m.b4105 + m.b4106 + m.b4107 + m.b4108 + m.b4109 + m.b4110 + m.b4111 + m.b4112 + m.b4113
                           + m.b4114 + m.b4115 + m.b4116 + m.b4117 == 1)

m.c1785 = Constraint(expr=   m.b4118 + m.b4119 + m.b4120 + m.b4121 + m.b4122 + m.b4123 + m.b4124 + m.b4125 + m.b4126
                           + m.b4127 + m.b4128 + m.b4129 + m.b4130 == 1)

m.c1786 = Constraint(expr=   m.b4131 + m.b4132 + m.b4133 + m.b4134 + m.b4135 + m.b4136 + m.b4137 + m.b4138 + m.b4139
                           + m.b4140 + m.b4141 + m.b4142 + m.b4143 == 1)

m.c1787 = Constraint(expr=   m.b4144 + m.b4145 + m.b4146 + m.b4147 + m.b4148 + m.b4149 + m.b4150 + m.b4151 + m.b4152
                           + m.b4153 + m.b4154 + m.b4155 + m.b4156 == 1)

m.c1788 = Constraint(expr=   m.b4157 + m.b4158 + m.b4159 + m.b4160 + m.b4161 + m.b4162 + m.b4163 + m.b4164 + m.b4165
                           + m.b4166 + m.b4167 + m.b4168 + m.b4169 == 1)

m.c1789 = Constraint(expr=   m.b4170 + m.b4171 + m.b4172 + m.b4173 + m.b4174 + m.b4175 + m.b4176 + m.b4177 + m.b4178
                           + m.b4179 + m.b4180 + m.b4181 + m.b4182 == 1)

m.c1790 = Constraint(expr=   m.b4183 + m.b4184 + m.b4185 + m.b4186 + m.b4187 + m.b4188 + m.b4189 + m.b4190 + m.b4191
                           + m.b4192 + m.b4193 + m.b4194 + m.b4195 == 1)

m.c1791 = Constraint(expr=   m.b4196 + m.b4197 + m.b4198 + m.b4199 + m.b4200 + m.b4201 + m.b4202 + m.b4203 + m.b4204
                           + m.b4205 + m.b4206 + m.b4207 + m.b4208 == 1)

m.c1792 = Constraint(expr=   m.b4209 + m.b4210 + m.b4211 + m.b4212 + m.b4213 + m.b4214 + m.b4215 + m.b4216 + m.b4217
                           + m.b4218 + m.b4219 + m.b4220 + m.b4221 == 1)

m.c1793 = Constraint(expr=   m.b4222 + m.b4223 + m.b4224 + m.b4225 + m.b4226 + m.b4227 + m.b4228 + m.b4229 + m.b4230
                           + m.b4231 + m.b4232 + m.b4233 + m.b4234 == 1)

m.c1794 = Constraint(expr=   m.b4235 + m.b4236 + m.b4237 + m.b4238 + m.b4239 + m.b4240 + m.b4241 + m.b4242 + m.b4243
                           + m.b4244 + m.b4245 + m.b4246 + m.b4247 == 1)

m.c1795 = Constraint(expr=   m.b4248 + m.b4249 + m.b4250 + m.b4251 + m.b4252 + m.b4253 + m.b4254 + m.b4255 + m.b4256
                           + m.b4257 + m.b4258 + m.b4259 + m.b4260 == 1)

m.c1796 = Constraint(expr=   m.b4261 + m.b4262 + m.b4263 + m.b4264 + m.b4265 + m.b4266 + m.b4267 + m.b4268 + m.b4269
                           + m.b4270 + m.b4271 + m.b4272 + m.b4273 == 1)

m.c1797 = Constraint(expr=   m.b4274 + m.b4275 + m.b4276 + m.b4277 + m.b4278 + m.b4279 + m.b4280 + m.b4281 + m.b4282
                           + m.b4283 + m.b4284 + m.b4285 + m.b4286 == 1)

m.c1798 = Constraint(expr=   m.b4287 + m.b4288 + m.b4289 + m.b4290 + m.b4291 + m.b4292 + m.b4293 + m.b4294 + m.b4295
                           + m.b4296 + m.b4297 + m.b4298 + m.b4299 == 1)

m.c1799 = Constraint(expr=   m.b4300 + m.b4301 + m.b4302 + m.b4303 + m.b4304 + m.b4305 + m.b4306 + m.b4307 + m.b4308
                           + m.b4309 + m.b4310 + m.b4311 + m.b4312 == 1)

m.c1800 = Constraint(expr=   m.b4313 + m.b4314 + m.b4315 + m.b4316 + m.b4317 + m.b4318 + m.b4319 + m.b4320 + m.b4321
                           + m.b4322 + m.b4323 + m.b4324 + m.b4325 == 1)

m.c1801 = Constraint(expr=   m.b4326 + m.b4327 + m.b4328 + m.b4329 + m.b4330 + m.b4331 + m.b4332 + m.b4333 + m.b4334
                           + m.b4335 + m.b4336 + m.b4337 + m.b4338 == 1)

m.c1802 = Constraint(expr=   m.b4339 + m.b4340 + m.b4341 + m.b4342 + m.b4343 + m.b4344 + m.b4345 + m.b4346 + m.b4347
                           + m.b4348 + m.b4349 + m.b4350 + m.b4351 == 1)

m.c1803 = Constraint(expr=   m.b4352 + m.b4353 + m.b4354 + m.b4355 + m.b4356 + m.b4357 + m.b4358 + m.b4359 + m.b4360
                           + m.b4361 + m.b4362 + m.b4363 + m.b4364 == 1)

m.c1804 = Constraint(expr=   m.b4365 + m.b4366 + m.b4367 + m.b4368 + m.b4369 + m.b4370 + m.b4371 + m.b4372 + m.b4373
                           + m.b4374 + m.b4375 + m.b4376 + m.b4377 == 1)

m.c1805 = Constraint(expr=   m.b4378 + m.b4379 + m.b4380 + m.b4381 + m.b4382 + m.b4383 + m.b4384 + m.b4385 + m.b4386
                           + m.b4387 + m.b4388 + m.b4389 + m.b4390 == 1)

m.c1806 = Constraint(expr=   m.b4391 + m.b4392 + m.b4393 + m.b4394 + m.b4395 + m.b4396 + m.b4397 + m.b4398 + m.b4399
                           + m.b4400 + m.b4401 + m.b4402 + m.b4403 == 1)

m.c1807 = Constraint(expr=   m.b4404 + m.b4405 + m.b4406 + m.b4407 + m.b4408 + m.b4409 + m.b4410 + m.b4411 + m.b4412
                           + m.b4413 + m.b4414 + m.b4415 + m.b4416 == 1)

m.c1808 = Constraint(expr=   m.b4417 + m.b4418 + m.b4419 + m.b4420 + m.b4421 + m.b4422 + m.b4423 + m.b4424 + m.b4425
                           + m.b4426 + m.b4427 + m.b4428 + m.b4429 == 1)

m.c1809 = Constraint(expr=   m.b4430 + m.b4431 + m.b4432 + m.b4433 + m.b4434 + m.b4435 + m.b4436 + m.b4437 + m.b4438
                           + m.b4439 + m.b4440 + m.b4441 + m.b4442 == 1)

m.c1810 = Constraint(expr=   m.b4443 + m.b4444 + m.b4445 + m.b4446 + m.b4447 + m.b4448 + m.b4449 + m.b4450 + m.b4451
                           + m.b4452 + m.b4453 + m.b4454 + m.b4455 == 1)

m.c1811 = Constraint(expr=   m.b4456 + m.b4457 + m.b4458 + m.b4459 + m.b4460 + m.b4461 + m.b4462 + m.b4463 + m.b4464
                           + m.b4465 + m.b4466 + m.b4467 + m.b4468 == 1)

m.c1812 = Constraint(expr=   m.b4469 + m.b4470 + m.b4471 + m.b4472 + m.b4473 + m.b4474 + m.b4475 + m.b4476 + m.b4477
                           + m.b4478 + m.b4479 + m.b4480 + m.b4481 == 1)

m.c1813 = Constraint(expr=   m.b4482 + m.b4483 + m.b4484 + m.b4485 + m.b4486 + m.b4487 + m.b4488 + m.b4489 + m.b4490
                           + m.b4491 + m.b4492 + m.b4493 + m.b4494 == 1)

m.c1814 = Constraint(expr=   m.b4495 + m.b4496 + m.b4497 + m.b4498 + m.b4499 + m.b4500 + m.b4501 + m.b4502 + m.b4503
                           + m.b4504 + m.b4505 + m.b4506 + m.b4507 == 1)

m.c1815 = Constraint(expr=   m.b4508 + m.b4509 + m.b4510 + m.b4511 + m.b4512 + m.b4513 + m.b4514 + m.b4515 + m.b4516
                           + m.b4517 + m.b4518 + m.b4519 + m.b4520 == 1)

m.c1816 = Constraint(expr=   m.b4521 + m.b4522 + m.b4523 + m.b4524 + m.b4525 + m.b4526 + m.b4527 + m.b4528 + m.b4529
                           + m.b4530 + m.b4531 + m.b4532 + m.b4533 == 1)

m.c1817 = Constraint(expr=   m.b4534 + m.b4535 + m.b4536 + m.b4537 + m.b4538 + m.b4539 + m.b4540 + m.b4541 + m.b4542
                           + m.b4543 + m.b4544 + m.b4545 + m.b4546 == 1)

m.c1818 = Constraint(expr=   m.b4547 + m.b4548 + m.b4549 + m.b4550 + m.b4551 + m.b4552 + m.b4553 + m.b4554 + m.b4555
                           + m.b4556 + m.b4557 + m.b4558 + m.b4559 == 1)

m.c1819 = Constraint(expr=   m.b4560 + m.b4561 + m.b4562 + m.b4563 + m.b4564 + m.b4565 + m.b4566 + m.b4567 + m.b4568
                           + m.b4569 + m.b4570 + m.b4571 + m.b4572 == 1)

m.c1820 = Constraint(expr=   m.b4573 + m.b4574 + m.b4575 + m.b4576 + m.b4577 + m.b4578 + m.b4579 + m.b4580 + m.b4581
                           + m.b4582 + m.b4583 + m.b4584 + m.b4585 == 1)

m.c1821 = Constraint(expr=   m.b4586 + m.b4587 + m.b4588 + m.b4589 + m.b4590 + m.b4591 + m.b4592 + m.b4593 + m.b4594
                           + m.b4595 + m.b4596 + m.b4597 + m.b4598 == 1)

m.c1822 = Constraint(expr=   m.b4599 + m.b4600 + m.b4601 + m.b4602 + m.b4603 + m.b4604 + m.b4605 + m.b4606 + m.b4607
                           + m.b4608 + m.b4609 + m.b4610 + m.b4611 == 1)

m.c1823 = Constraint(expr=   m.b4612 + m.b4613 + m.b4614 + m.b4615 + m.b4616 + m.b4617 + m.b4618 + m.b4619 + m.b4620
                           + m.b4621 + m.b4622 + m.b4623 + m.b4624 == 1)

m.c1824 = Constraint(expr=   m.b4625 + m.b4626 + m.b4627 + m.b4628 + m.b4629 + m.b4630 + m.b4631 + m.b4632 + m.b4633
                           + m.b4634 + m.b4635 + m.b4636 + m.b4637 == 1)

m.c1825 = Constraint(expr=   m.b4638 + m.b4639 + m.b4640 + m.b4641 + m.b4642 + m.b4643 + m.b4644 + m.b4645 + m.b4646
                           + m.b4647 + m.b4648 + m.b4649 + m.b4650 == 1)

m.c1826 = Constraint(expr=   m.b4651 + m.b4652 + m.b4653 + m.b4654 + m.b4655 + m.b4656 + m.b4657 + m.b4658 + m.b4659
                           + m.b4660 + m.b4661 + m.b4662 + m.b4663 == 1)

m.c1827 = Constraint(expr=   m.b4664 + m.b4665 + m.b4666 + m.b4667 + m.b4668 + m.b4669 + m.b4670 + m.b4671 + m.b4672
                           + m.b4673 + m.b4674 + m.b4675 + m.b4676 == 1)

m.c1828 = Constraint(expr=   m.b4677 + m.b4678 + m.b4679 + m.b4680 + m.b4681 + m.b4682 + m.b4683 + m.b4684 + m.b4685
                           + m.b4686 + m.b4687 + m.b4688 + m.b4689 == 1)

m.c1829 = Constraint(expr=   m.b4690 + m.b4691 + m.b4692 + m.b4693 + m.b4694 + m.b4695 + m.b4696 + m.b4697 + m.b4698
                           + m.b4699 + m.b4700 + m.b4701 + m.b4702 == 1)

m.c1830 = Constraint(expr=   m.b4703 + m.b4704 + m.b4705 + m.b4706 + m.b4707 + m.b4708 + m.b4709 + m.b4710 + m.b4711
                           + m.b4712 + m.b4713 + m.b4714 + m.b4715 == 1)

m.c1831 = Constraint(expr=   m.b4716 + m.b4717 + m.b4718 + m.b4719 + m.b4720 + m.b4721 + m.b4722 + m.b4723 + m.b4724
                           + m.b4725 + m.b4726 + m.b4727 + m.b4728 == 1)

m.c1832 = Constraint(expr=   m.b4729 + m.b4730 + m.b4731 + m.b4732 + m.b4733 + m.b4734 + m.b4735 + m.b4736 + m.b4737
                           + m.b4738 + m.b4739 + m.b4740 + m.b4741 == 1)

m.c1833 = Constraint(expr=   m.b4742 + m.b4743 + m.b4744 + m.b4745 + m.b4746 + m.b4747 + m.b4748 + m.b4749 + m.b4750
                           + m.b4751 + m.b4752 + m.b4753 + m.b4754 == 1)

m.c1834 = Constraint(expr=   m.b4755 + m.b4756 + m.b4757 + m.b4758 + m.b4759 + m.b4760 + m.b4761 + m.b4762 + m.b4763
                           + m.b4764 + m.b4765 + m.b4766 + m.b4767 == 1)

m.c1835 = Constraint(expr=   m.b4768 + m.b4769 + m.b4770 + m.b4771 + m.b4772 + m.b4773 + m.b4774 + m.b4775 + m.b4776
                           + m.b4777 + m.b4778 + m.b4779 + m.b4780 == 1)

m.c1836 = Constraint(expr=   m.b4781 + m.b4782 + m.b4783 + m.b4784 + m.b4785 + m.b4786 + m.b4787 + m.b4788 + m.b4789
                           + m.b4790 + m.b4791 + m.b4792 + m.b4793 == 1)

m.c1837 = Constraint(expr=   m.b4794 + m.b4795 + m.b4796 + m.b4797 + m.b4798 + m.b4799 + m.b4800 + m.b4801 + m.b4802
                           + m.b4803 + m.b4804 + m.b4805 + m.b4806 == 1)

m.c1838 = Constraint(expr=   m.b4807 + m.b4808 + m.b4809 + m.b4810 + m.b4811 + m.b4812 + m.b4813 + m.b4814 + m.b4815
                           + m.b4816 + m.b4817 + m.b4818 + m.b4819 == 1)

m.c1839 = Constraint(expr=   m.b4820 + m.b4821 + m.b4822 + m.b4823 + m.b4824 + m.b4825 + m.b4826 + m.b4827 + m.b4828
                           + m.b4829 + m.b4830 + m.b4831 + m.b4832 == 1)

m.c1840 = Constraint(expr=   m.b4833 + m.b4834 + m.b4835 + m.b4836 + m.b4837 + m.b4838 + m.b4839 + m.b4840 + m.b4841
                           + m.b4842 + m.b4843 + m.b4844 + m.b4845 == 1)

m.c1841 = Constraint(expr=   m.b4846 + m.b4847 + m.b4848 + m.b4849 + m.b4850 + m.b4851 + m.b4852 + m.b4853 + m.b4854
                           + m.b4855 + m.b4856 + m.b4857 + m.b4858 == 1)

m.c1842 = Constraint(expr=   m.b4859 + m.b4860 + m.b4861 + m.b4862 + m.b4863 + m.b4864 + m.b4865 + m.b4866 + m.b4867
                           + m.b4868 + m.b4869 + m.b4870 + m.b4871 == 1)

m.c1843 = Constraint(expr=   m.b4872 + m.b4873 + m.b4874 + m.b4875 + m.b4876 + m.b4877 + m.b4878 + m.b4879 + m.b4880
                           + m.b4881 + m.b4882 + m.b4883 + m.b4884 == 1)

m.c1844 = Constraint(expr=   m.b4885 + m.b4886 + m.b4887 + m.b4888 + m.b4889 + m.b4890 + m.b4891 + m.b4892 + m.b4893
                           + m.b4894 + m.b4895 + m.b4896 + m.b4897 == 1)

m.c1845 = Constraint(expr=   m.b4898 + m.b4899 + m.b4900 + m.b4901 + m.b4902 + m.b4903 + m.b4904 + m.b4905 + m.b4906
                           + m.b4907 + m.b4908 + m.b4909 + m.b4910 == 1)

m.c1846 = Constraint(expr=   m.b4911 + m.b4912 + m.b4913 + m.b4914 + m.b4915 + m.b4916 + m.b4917 + m.b4918 + m.b4919
                           + m.b4920 + m.b4921 + m.b4922 + m.b4923 == 1)

m.c1847 = Constraint(expr=   m.b4924 + m.b4925 + m.b4926 + m.b4927 + m.b4928 + m.b4929 + m.b4930 + m.b4931 + m.b4932
                           + m.b4933 + m.b4934 + m.b4935 + m.b4936 == 1)

m.c1848 = Constraint(expr=   m.b4937 + m.b4938 + m.b4939 + m.b4940 + m.b4941 + m.b4942 + m.b4943 + m.b4944 + m.b4945
                           + m.b4946 + m.b4947 + m.b4948 + m.b4949 == 1)

m.c1849 = Constraint(expr=   m.b4950 + m.b4951 + m.b4952 + m.b4953 + m.b4954 + m.b4955 + m.b4956 + m.b4957 + m.b4958
                           + m.b4959 + m.b4960 + m.b4961 + m.b4962 == 1)

m.c1850 = Constraint(expr=   m.b4963 + m.b4964 + m.b4965 + m.b4966 + m.b4967 + m.b4968 + m.b4969 + m.b4970 + m.b4971
                           + m.b4972 + m.b4973 + m.b4974 + m.b4975 == 1)

m.c1851 = Constraint(expr=   m.b4976 + m.b4977 + m.b4978 + m.b4979 + m.b4980 + m.b4981 + m.b4982 + m.b4983 + m.b4984
                           + m.b4985 + m.b4986 + m.b4987 + m.b4988 == 1)

m.c1852 = Constraint(expr=   m.b4989 + m.b4990 + m.b4991 + m.b4992 + m.b4993 + m.b4994 + m.b4995 + m.b4996 + m.b4997
                           + m.b4998 + m.b4999 + m.b5000 + m.b5001 == 1)

m.c1853 = Constraint(expr=   m.b5002 + m.b5003 + m.b5004 + m.b5005 + m.b5006 + m.b5007 + m.b5008 + m.b5009 + m.b5010
                           + m.b5011 + m.b5012 + m.b5013 + m.b5014 == 1)

m.c1854 = Constraint(expr=   m.b5015 + m.b5016 + m.b5017 + m.b5018 + m.b5019 + m.b5020 + m.b5021 + m.b5022 + m.b5023
                           + m.b5024 + m.b5025 + m.b5026 + m.b5027 == 1)
