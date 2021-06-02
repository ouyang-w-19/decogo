#  MINLP written by GAMS Convert at 04/21/18 13:54:27
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        281       81       10      190        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        231      161       70        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1006      991       15        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.b1 = Var(within=Binary,bounds=(0,1),initialize=0)
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
m.b62 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b63 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b64 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b65 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b66 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b67 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b68 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b69 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b70 = Var(within=Binary,bounds=(0,1),initialize=0)
m.x71 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x72 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x73 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x74 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x75 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x76 = Var(within=Reals,bounds=(1,14),initialize=1)
m.x77 = Var(within=Reals,bounds=(1,12),initialize=1)
m.x78 = Var(within=Reals,bounds=(1,13),initialize=1)
m.x79 = Var(within=Reals,bounds=(1,14),initialize=1)
m.x80 = Var(within=Reals,bounds=(1,13),initialize=1)
m.x81 = Var(within=Reals,bounds=(1,14),initialize=1)
m.x82 = Var(within=Reals,bounds=(1,12),initialize=1)
m.x83 = Var(within=Reals,bounds=(1,13),initialize=1)
m.x84 = Var(within=Reals,bounds=(1,13),initialize=1)
m.x85 = Var(within=Reals,bounds=(1,14),initialize=1)
m.x87 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x88 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x89 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x90 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x91 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x92 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x93 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x94 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x95 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x96 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x97 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x98 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x99 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x100 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x101 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x102 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x103 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x104 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x105 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x106 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x107 = Var(within=Reals,bounds=(0,109669.003926881),initialize=0)
m.x108 = Var(within=Reals,bounds=(0,99699.094478983),initialize=0)
m.x109 = Var(within=Reals,bounds=(0,109669.003926881),initialize=0)
m.x110 = Var(within=Reals,bounds=(0,69789.3661352881),initialize=0)
m.x111 = Var(within=Reals,bounds=(0,99699.094478983),initialize=0)
m.x112 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x113 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x114 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x115 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x116 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x117 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x118 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x119 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x120 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x121 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x122 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x123 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x124 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x125 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x126 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x127 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x128 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x129 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x130 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x131 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x132 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x133 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x134 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x135 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x136 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x137 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x138 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x139 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x140 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x141 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x142 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x143 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x144 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x145 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x146 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x147 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x148 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x149 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x150 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x151 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x152 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x153 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x154 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x155 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x156 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x157 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x158 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x159 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x160 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x161 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x162 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x163 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x164 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x165 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x166 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x167 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x168 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x169 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x170 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x171 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x172 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x173 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x174 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x175 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x176 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x177 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x178 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x179 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x180 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x181 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x182 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x183 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x184 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x185 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x186 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x187 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x188 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x189 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x190 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x191 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x192 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x193 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x194 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x195 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x196 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x197 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x198 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x199 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x200 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x201 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x202 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x203 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x204 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x205 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x206 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x207 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x208 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x209 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x210 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x211 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x212 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x213 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x214 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x215 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x216 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x217 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x218 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x219 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x220 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x221 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x222 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x223 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x224 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x225 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x226 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x227 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x228 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x229 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x230 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x231 = Var(within=Reals,bounds=(0,None),initialize=0)

m.obj = Objective(expr=88.85300006996*sqrt(1e-8 + m.x107) + 192.23073994166*sqrt(1e-8 + m.x108) + 127.63233374696*sqrt(
                       1e-8 + m.x109) + 419.48235478268*sqrt(1e-8 + m.x110) + 153.22284111554*sqrt(1e-8 + m.x111) + 
                       11812.8060023653*sqrt(1e-8 + m.x76) + 1350.11753695442*sqrt(1e-8 + m.x77) + 13367.9894872554*
                       sqrt(1e-8 + m.x78) + 22271.0227712868*sqrt(1e-8 + m.x79) + 3005.94387692899*sqrt(1e-8 + m.x80) + 
                       8081.13134168897*sqrt(1e-8 + m.x81) + 2725.40259637536*sqrt(1e-8 + m.x82) + 17834.6321864598*
                       sqrt(1e-8 + m.x83) + 11090.3708869987*sqrt(1e-8 + m.x84) + 34135.3450147183*sqrt(1e-8 + m.x85)
                        + 151717.47132*m.b16 + 158432.66708*m.b17 + 155503.75356*m.b18 + 153011.37904*m.b19
                        + 152922.12117*m.b20 + 31172.917964017*m.b21 + 50366.2988612629*m.b22 + 25232.3015865842*m.b23
                        + 13875.2777716691*m.b24 + 12894.0919466219*m.b25 + 104246.200740246*m.b26
                        + 23030.4692996671*m.b27 + 34080.9619919892*m.b28 + 23691.1338892398*m.b29
                        + 71485.9325093983*m.b30 + 20595.4230163802*m.b31 + 100964.014716159*m.b32
                        + 47584.642753328*m.b33 + 8366.15399075336*m.b34 + 12512.1539989574*m.b35
                        + 35986.4763418661*m.b36 + 46834.267934517*m.b37 + 35500.2352632821*m.b38
                        + 24409.7766590388*m.b39 + 48282.6225705813*m.b40 + 31041.4817687302*m.b41
                        + 53037.2328896265*m.b42 + 51459.7461120258*m.b43 + 22667.2580628975*m.b44
                        + 25228.9882448255*m.b45 + 37408.8375498868*m.b46 + 25200.7856772603*m.b47
                        + 36902.8071939517*m.b48 + 26504.6681149691*m.b49 + 49522.8366523017*m.b50
                        + 9271.93442865272*m.b51 + 144904.131180845*m.b52 + 24247.3790621604*m.b53
                        + 7667.40116108732*m.b54 + 22073.8762813933*m.b55 + 107488.43411253*m.b56
                        + 23226.4417178111*m.b57 + 34704.48655633*m.b58 + 25058.2307095212*m.b59
                        + 47407.2067673463*m.b60 + 21614.5566697948*m.b61 + 101949.658248026*m.b62
                        + 25381.2261639692*m.b63 + 8426.19414871674*m.b64 + 13579.8855675766*m.b65
                        + 107491.687838232*m.b66 + 43784.7477537411*m.b67 + 107221.380878763*m.b68
                        + 13362.229690641*m.b69 + 25676.6925875457*m.b70 + 772.8645240165*m.x87 + 109.73384215925*m.x88
                        + 332.64598234875*m.x89 + 226.514334935*m.x90 + 159.627138782*m.x91 + 621.33045502625*m.x92
                        + 444.925267275*m.x93 + 198.06301532475*m.x94 + 357.5965626135*m.x95 + 80.6766666775*m.x96
                        + 242.0437770305*m.x97 + 630.31461703875*m.x98 + 485.8539167745*m.x99 + 239.8308926255*m.x100
                        + 408.49173769875*m.x101, sense=minimize)

m.c2 = Constraint(expr=   m.b1 + m.b6 + m.b11 - m.b16 == 0)

m.c3 = Constraint(expr=   m.b2 + m.b7 + m.b12 - m.b17 == 0)

m.c4 = Constraint(expr=   m.b3 + m.b8 + m.b13 - m.b18 == 0)

m.c5 = Constraint(expr=   m.b4 + m.b9 + m.b14 - m.b19 == 0)

m.c6 = Constraint(expr=   m.b5 + m.b10 + m.b15 - m.b20 == 0)

m.c7 = Constraint(expr= - m.b16 + m.b21 <= 0)

m.c8 = Constraint(expr= - m.b16 + m.b22 <= 0)

m.c9 = Constraint(expr= - m.b16 + m.b23 <= 0)

m.c10 = Constraint(expr= - m.b16 + m.b24 <= 0)

m.c11 = Constraint(expr= - m.b16 + m.b25 <= 0)

m.c12 = Constraint(expr= - m.b16 + m.b26 <= 0)

m.c13 = Constraint(expr= - m.b16 + m.b27 <= 0)

m.c14 = Constraint(expr= - m.b16 + m.b28 <= 0)

m.c15 = Constraint(expr= - m.b16 + m.b29 <= 0)

m.c16 = Constraint(expr= - m.b16 + m.b30 <= 0)

m.c17 = Constraint(expr= - m.b17 + m.b31 <= 0)

m.c18 = Constraint(expr= - m.b17 + m.b32 <= 0)

m.c19 = Constraint(expr= - m.b17 + m.b33 <= 0)

m.c20 = Constraint(expr= - m.b17 + m.b34 <= 0)

m.c21 = Constraint(expr= - m.b17 + m.b35 <= 0)

m.c22 = Constraint(expr= - m.b17 + m.b36 <= 0)

m.c23 = Constraint(expr= - m.b17 + m.b37 <= 0)

m.c24 = Constraint(expr= - m.b17 + m.b38 <= 0)

m.c25 = Constraint(expr= - m.b17 + m.b39 <= 0)

m.c26 = Constraint(expr= - m.b17 + m.b40 <= 0)

m.c27 = Constraint(expr= - m.b18 + m.b41 <= 0)

m.c28 = Constraint(expr= - m.b18 + m.b42 <= 0)

m.c29 = Constraint(expr= - m.b18 + m.b43 <= 0)

m.c30 = Constraint(expr= - m.b18 + m.b44 <= 0)

m.c31 = Constraint(expr= - m.b18 + m.b45 <= 0)

m.c32 = Constraint(expr= - m.b18 + m.b46 <= 0)

m.c33 = Constraint(expr= - m.b18 + m.b47 <= 0)

m.c34 = Constraint(expr= - m.b18 + m.b48 <= 0)

m.c35 = Constraint(expr= - m.b18 + m.b49 <= 0)

m.c36 = Constraint(expr= - m.b18 + m.b50 <= 0)

m.c37 = Constraint(expr= - m.b19 + m.b51 <= 0)

m.c38 = Constraint(expr= - m.b19 + m.b52 <= 0)

m.c39 = Constraint(expr= - m.b19 + m.b53 <= 0)

m.c40 = Constraint(expr= - m.b19 + m.b54 <= 0)

m.c41 = Constraint(expr= - m.b19 + m.b55 <= 0)

m.c42 = Constraint(expr= - m.b19 + m.b56 <= 0)

m.c43 = Constraint(expr= - m.b19 + m.b57 <= 0)

m.c44 = Constraint(expr= - m.b19 + m.b58 <= 0)

m.c45 = Constraint(expr= - m.b19 + m.b59 <= 0)

m.c46 = Constraint(expr= - m.b19 + m.b60 <= 0)

m.c47 = Constraint(expr= - m.b20 + m.b61 <= 0)

m.c48 = Constraint(expr= - m.b20 + m.b62 <= 0)

m.c49 = Constraint(expr= - m.b20 + m.b63 <= 0)

m.c50 = Constraint(expr= - m.b20 + m.b64 <= 0)

m.c51 = Constraint(expr= - m.b20 + m.b65 <= 0)

m.c52 = Constraint(expr= - m.b20 + m.b66 <= 0)

m.c53 = Constraint(expr= - m.b20 + m.b67 <= 0)

m.c54 = Constraint(expr= - m.b20 + m.b68 <= 0)

m.c55 = Constraint(expr= - m.b20 + m.b69 <= 0)

m.c56 = Constraint(expr= - m.b20 + m.b70 <= 0)

m.c57 = Constraint(expr=   m.b21 + m.b31 + m.b41 + m.b51 + m.b61 == 1)

m.c58 = Constraint(expr=   m.b22 + m.b32 + m.b42 + m.b52 + m.b62 == 1)

m.c59 = Constraint(expr=   m.b23 + m.b33 + m.b43 + m.b53 + m.b63 == 1)

m.c60 = Constraint(expr=   m.b24 + m.b34 + m.b44 + m.b54 + m.b64 == 1)

m.c61 = Constraint(expr=   m.b25 + m.b35 + m.b45 + m.b55 + m.b65 == 1)

m.c62 = Constraint(expr=   m.b26 + m.b36 + m.b46 + m.b56 + m.b66 == 1)

m.c63 = Constraint(expr=   m.b27 + m.b37 + m.b47 + m.b57 + m.b67 == 1)

m.c64 = Constraint(expr=   m.b28 + m.b38 + m.b48 + m.b58 + m.b68 == 1)

m.c65 = Constraint(expr=   m.b29 + m.b39 + m.b49 + m.b59 + m.b69 == 1)

m.c66 = Constraint(expr=   m.b30 + m.b40 + m.b50 + m.b60 + m.b70 == 1)

m.c67 = Constraint(expr= - 3*m.b21 - 2*m.b31 - 3*m.b41 - m.b51 - 2*m.b61 + m.x76 - m.x112 - m.x122 - m.x132 - m.x142
                         - m.x152 >= 0)

m.c68 = Constraint(expr= - m.b22 - 2*m.b32 - m.b42 - 3*m.b52 - 2*m.b62 + m.x77 - m.x113 - m.x123 - m.x133 - m.x143
                         - m.x153 >= 0)

m.c69 = Constraint(expr= - m.b23 - 2*m.b33 - 2*m.b43 - m.b53 - m.b63 + m.x78 - m.x114 - m.x124 - m.x134 - m.x144
                         - m.x154 >= 0)

m.c70 = Constraint(expr= - 2*m.b24 - m.b34 - 3*m.b44 - m.b54 - m.b64 + m.x79 - m.x115 - m.x125 - m.x135 - m.x145
                         - m.x155 >= 0)

m.c71 = Constraint(expr= - m.b25 - m.b35 - 2*m.b45 - 2*m.b55 - m.b65 + m.x80 - m.x116 - m.x126 - m.x136 - m.x146
                         - m.x156 >= 0)

m.c72 = Constraint(expr= - 3*m.b26 - m.b36 - m.b46 - 3*m.b56 - 3*m.b66 + m.x81 - m.x117 - m.x127 - m.x137 - m.x147
                         - m.x157 >= 0)

m.c73 = Constraint(expr= - m.b27 - 2*m.b37 - m.b47 - m.b57 - 2*m.b67 + m.x82 - m.x118 - m.x128 - m.x138 - m.x148
                         - m.x158 >= 0)

m.c74 = Constraint(expr= - m.b28 - m.b38 - m.b48 - m.b58 - 3*m.b68 + m.x83 - m.x119 - m.x129 - m.x139 - m.x149 - m.x159
                         >= 0)

m.c75 = Constraint(expr= - 2*m.b29 - 2*m.b39 - 2*m.b49 - 2*m.b59 - m.b69 + m.x84 - m.x120 - m.x130 - m.x140 - m.x150
                         - m.x160 >= 0)

m.c76 = Constraint(expr= - 3*m.b30 - 2*m.b40 - 2*m.b50 - 2*m.b60 - m.b70 + m.x85 - m.x121 - m.x131 - m.x141 - m.x151
                         - m.x161 >= 0)

m.c77 = Constraint(expr= - 133.258309275*m.b21 - 144.933884175*m.b22 - 90.093117225*m.b23 - 97.285204275*m.b24
                         - 89.79206385*m.b25 - 93.475928775*m.b26 - 123.485735475*m.b27 - 130.122945825*m.b28
                         - 81.4077558*m.b29 - 86.2760787*m.b30 + m.x87 + m.x92 + m.x97 + m.x102 == 0)

m.c78 = Constraint(expr= - 133.258309275*m.b31 - 144.933884175*m.b32 - 90.093117225*m.b33 - 97.285204275*m.b34
                         - 89.79206385*m.b35 - 93.475928775*m.b36 - 123.485735475*m.b37 - 130.122945825*m.b38
                         - 81.4077558*m.b39 - 86.2760787*m.b40 + m.x88 + m.x93 + m.x98 + m.x103 == 0)

m.c79 = Constraint(expr= - 133.258309275*m.b41 - 144.933884175*m.b42 - 90.093117225*m.b43 - 97.285204275*m.b44
                         - 89.79206385*m.b45 - 93.475928775*m.b46 - 123.485735475*m.b47 - 130.122945825*m.b48
                         - 81.4077558*m.b49 - 86.2760787*m.b50 + m.x89 + m.x94 + m.x99 + m.x104 == 0)

m.c80 = Constraint(expr= - 133.258309275*m.b51 - 144.933884175*m.b52 - 90.093117225*m.b53 - 97.285204275*m.b54
                         - 89.79206385*m.b55 - 93.475928775*m.b56 - 123.485735475*m.b57 - 130.122945825*m.b58
                         - 81.4077558*m.b59 - 86.2760787*m.b60 + m.x90 + m.x95 + m.x100 + m.x105 == 0)

m.c81 = Constraint(expr= - 133.258309275*m.b61 - 144.933884175*m.b62 - 90.093117225*m.b63 - 97.285204275*m.b64
                         - 89.79206385*m.b65 - 93.475928775*m.b66 - 123.485735475*m.b67 - 130.122945825*m.b68
                         - 81.4077558*m.b69 - 86.2760787*m.b70 + m.x91 + m.x96 + m.x101 + m.x106 == 0)

m.c82 = Constraint(expr= - 1070.131023375*m.b1 + m.x87 <= 0)

m.c83 = Constraint(expr= - 1070.131023375*m.b2 + m.x88 <= 0)

m.c84 = Constraint(expr= - 1070.131023375*m.b3 + m.x89 <= 0)

m.c85 = Constraint(expr= - 1070.131023375*m.b4 + m.x90 <= 0)

m.c86 = Constraint(expr= - 1070.131023375*m.b5 + m.x91 <= 0)

m.c87 = Constraint(expr= - 1070.131023375*m.b6 + m.x92 <= 0)

m.c88 = Constraint(expr= - 1070.131023375*m.b7 + m.x93 <= 0)

m.c89 = Constraint(expr= - 1070.131023375*m.b8 + m.x94 <= 0)

m.c90 = Constraint(expr= - 1070.131023375*m.b9 + m.x95 <= 0)

m.c91 = Constraint(expr= - 1070.131023375*m.b10 + m.x96 <= 0)

m.c92 = Constraint(expr= - 1070.131023375*m.b11 + m.x97 <= 0)

m.c93 = Constraint(expr= - 1070.131023375*m.b12 + m.x98 <= 0)

m.c94 = Constraint(expr= - 1070.131023375*m.b13 + m.x99 <= 0)

m.c95 = Constraint(expr= - 1070.131023375*m.b14 + m.x100 <= 0)

m.c96 = Constraint(expr= - 1070.131023375*m.b15 + m.x101 <= 0)

m.c97 = Constraint(expr=   1070.131023375*m.b16 + m.x102 <= 1070.131023375)

m.c98 = Constraint(expr=   1070.131023375*m.b17 + m.x103 <= 1070.131023375)

m.c99 = Constraint(expr=   1070.131023375*m.b18 + m.x104 <= 1070.131023375)

m.c100 = Constraint(expr=   1070.131023375*m.b19 + m.x105 <= 1070.131023375)

m.c101 = Constraint(expr=   1070.131023375*m.b20 + m.x106 <= 1070.131023375)

m.c102 = Constraint(expr= - m.x71 + m.x112 + m.x162 == 0)

m.c103 = Constraint(expr= - m.x71 + m.x113 + m.x163 == 0)

m.c104 = Constraint(expr= - m.x71 + m.x114 + m.x164 == 0)

m.c105 = Constraint(expr= - m.x71 + m.x115 + m.x165 == 0)

m.c106 = Constraint(expr= - m.x71 + m.x116 + m.x166 == 0)

m.c107 = Constraint(expr= - m.x71 + m.x117 + m.x167 == 0)

m.c108 = Constraint(expr= - m.x71 + m.x118 + m.x168 == 0)

m.c109 = Constraint(expr= - m.x71 + m.x119 + m.x169 == 0)

m.c110 = Constraint(expr= - m.x71 + m.x120 + m.x170 == 0)

m.c111 = Constraint(expr= - m.x71 + m.x121 + m.x171 == 0)

m.c112 = Constraint(expr= - m.x72 + m.x122 + m.x172 == 0)

m.c113 = Constraint(expr= - m.x72 + m.x123 + m.x173 == 0)

m.c114 = Constraint(expr= - m.x72 + m.x124 + m.x174 == 0)

m.c115 = Constraint(expr= - m.x72 + m.x125 + m.x175 == 0)

m.c116 = Constraint(expr= - m.x72 + m.x126 + m.x176 == 0)

m.c117 = Constraint(expr= - m.x72 + m.x127 + m.x177 == 0)

m.c118 = Constraint(expr= - m.x72 + m.x128 + m.x178 == 0)

m.c119 = Constraint(expr= - m.x72 + m.x129 + m.x179 == 0)

m.c120 = Constraint(expr= - m.x72 + m.x130 + m.x180 == 0)

m.c121 = Constraint(expr= - m.x72 + m.x131 + m.x181 == 0)

m.c122 = Constraint(expr= - m.x73 + m.x132 + m.x182 == 0)

m.c123 = Constraint(expr= - m.x73 + m.x133 + m.x183 == 0)

m.c124 = Constraint(expr= - m.x73 + m.x134 + m.x184 == 0)

m.c125 = Constraint(expr= - m.x73 + m.x135 + m.x185 == 0)

m.c126 = Constraint(expr= - m.x73 + m.x136 + m.x186 == 0)

m.c127 = Constraint(expr= - m.x73 + m.x137 + m.x187 == 0)

m.c128 = Constraint(expr= - m.x73 + m.x138 + m.x188 == 0)

m.c129 = Constraint(expr= - m.x73 + m.x139 + m.x189 == 0)

m.c130 = Constraint(expr= - m.x73 + m.x140 + m.x190 == 0)

m.c131 = Constraint(expr= - m.x73 + m.x141 + m.x191 == 0)

m.c132 = Constraint(expr= - m.x74 + m.x142 + m.x192 == 0)

m.c133 = Constraint(expr= - m.x74 + m.x143 + m.x193 == 0)

m.c134 = Constraint(expr= - m.x74 + m.x144 + m.x194 == 0)

m.c135 = Constraint(expr= - m.x74 + m.x145 + m.x195 == 0)

m.c136 = Constraint(expr= - m.x74 + m.x146 + m.x196 == 0)

m.c137 = Constraint(expr= - m.x74 + m.x147 + m.x197 == 0)

m.c138 = Constraint(expr= - m.x74 + m.x148 + m.x198 == 0)

m.c139 = Constraint(expr= - m.x74 + m.x149 + m.x199 == 0)

m.c140 = Constraint(expr= - m.x74 + m.x150 + m.x200 == 0)

m.c141 = Constraint(expr= - m.x74 + m.x151 + m.x201 == 0)

m.c142 = Constraint(expr= - m.x75 + m.x152 + m.x202 == 0)

m.c143 = Constraint(expr= - m.x75 + m.x153 + m.x203 == 0)

m.c144 = Constraint(expr= - m.x75 + m.x154 + m.x204 == 0)

m.c145 = Constraint(expr= - m.x75 + m.x155 + m.x205 == 0)

m.c146 = Constraint(expr= - m.x75 + m.x156 + m.x206 == 0)

m.c147 = Constraint(expr= - m.x75 + m.x157 + m.x207 == 0)

m.c148 = Constraint(expr= - m.x75 + m.x158 + m.x208 == 0)

m.c149 = Constraint(expr= - m.x75 + m.x159 + m.x209 == 0)

m.c150 = Constraint(expr= - m.x75 + m.x160 + m.x210 == 0)

m.c151 = Constraint(expr= - m.x75 + m.x161 + m.x211 == 0)

m.c152 = Constraint(expr= - 11*m.b21 + m.x112 <= 0)

m.c153 = Constraint(expr= - 11*m.b22 + m.x113 <= 0)

m.c154 = Constraint(expr= - 11*m.b23 + m.x114 <= 0)

m.c155 = Constraint(expr= - 11*m.b24 + m.x115 <= 0)

m.c156 = Constraint(expr= - 11*m.b25 + m.x116 <= 0)

m.c157 = Constraint(expr= - 11*m.b26 + m.x117 <= 0)

m.c158 = Constraint(expr= - 11*m.b27 + m.x118 <= 0)

m.c159 = Constraint(expr= - 11*m.b28 + m.x119 <= 0)

m.c160 = Constraint(expr= - 11*m.b29 + m.x120 <= 0)

m.c161 = Constraint(expr= - 11*m.b30 + m.x121 <= 0)

m.c162 = Constraint(expr= - 10*m.b31 + m.x122 <= 0)

m.c163 = Constraint(expr= - 10*m.b32 + m.x123 <= 0)

m.c164 = Constraint(expr= - 10*m.b33 + m.x124 <= 0)

m.c165 = Constraint(expr= - 10*m.b34 + m.x125 <= 0)

m.c166 = Constraint(expr= - 10*m.b35 + m.x126 <= 0)

m.c167 = Constraint(expr= - 10*m.b36 + m.x127 <= 0)

m.c168 = Constraint(expr= - 10*m.b37 + m.x128 <= 0)

m.c169 = Constraint(expr= - 10*m.b38 + m.x129 <= 0)

m.c170 = Constraint(expr= - 10*m.b39 + m.x130 <= 0)

m.c171 = Constraint(expr= - 10*m.b40 + m.x131 <= 0)

m.c172 = Constraint(expr= - 11*m.b41 + m.x132 <= 0)

m.c173 = Constraint(expr= - 11*m.b42 + m.x133 <= 0)

m.c174 = Constraint(expr= - 11*m.b43 + m.x134 <= 0)

m.c175 = Constraint(expr= - 11*m.b44 + m.x135 <= 0)

m.c176 = Constraint(expr= - 11*m.b45 + m.x136 <= 0)

m.c177 = Constraint(expr= - 11*m.b46 + m.x137 <= 0)

m.c178 = Constraint(expr= - 11*m.b47 + m.x138 <= 0)

m.c179 = Constraint(expr= - 11*m.b48 + m.x139 <= 0)

m.c180 = Constraint(expr= - 11*m.b49 + m.x140 <= 0)

m.c181 = Constraint(expr= - 11*m.b50 + m.x141 <= 0)

m.c182 = Constraint(expr= - 7*m.b51 + m.x142 <= 0)

m.c183 = Constraint(expr= - 7*m.b52 + m.x143 <= 0)

m.c184 = Constraint(expr= - 7*m.b53 + m.x144 <= 0)

m.c185 = Constraint(expr= - 7*m.b54 + m.x145 <= 0)

m.c186 = Constraint(expr= - 7*m.b55 + m.x146 <= 0)

m.c187 = Constraint(expr= - 7*m.b56 + m.x147 <= 0)

m.c188 = Constraint(expr= - 7*m.b57 + m.x148 <= 0)

m.c189 = Constraint(expr= - 7*m.b58 + m.x149 <= 0)

m.c190 = Constraint(expr= - 7*m.b59 + m.x150 <= 0)

m.c191 = Constraint(expr= - 7*m.b60 + m.x151 <= 0)

m.c192 = Constraint(expr= - 10*m.b61 + m.x152 <= 0)

m.c193 = Constraint(expr= - 10*m.b62 + m.x153 <= 0)

m.c194 = Constraint(expr= - 10*m.b63 + m.x154 <= 0)

m.c195 = Constraint(expr= - 10*m.b64 + m.x155 <= 0)

m.c196 = Constraint(expr= - 10*m.b65 + m.x156 <= 0)

m.c197 = Constraint(expr= - 10*m.b66 + m.x157 <= 0)

m.c198 = Constraint(expr= - 10*m.b67 + m.x158 <= 0)

m.c199 = Constraint(expr= - 10*m.b68 + m.x159 <= 0)

m.c200 = Constraint(expr= - 10*m.b69 + m.x160 <= 0)

m.c201 = Constraint(expr= - 10*m.b70 + m.x161 <= 0)

m.c202 = Constraint(expr=   11*m.b21 + m.x162 <= 11)

m.c203 = Constraint(expr=   11*m.b22 + m.x163 <= 11)

m.c204 = Constraint(expr=   11*m.b23 + m.x164 <= 11)

m.c205 = Constraint(expr=   11*m.b24 + m.x165 <= 11)

m.c206 = Constraint(expr=   11*m.b25 + m.x166 <= 11)

m.c207 = Constraint(expr=   11*m.b26 + m.x167 <= 11)

m.c208 = Constraint(expr=   11*m.b27 + m.x168 <= 11)

m.c209 = Constraint(expr=   11*m.b28 + m.x169 <= 11)

m.c210 = Constraint(expr=   11*m.b29 + m.x170 <= 11)

m.c211 = Constraint(expr=   11*m.b30 + m.x171 <= 11)

m.c212 = Constraint(expr=   10*m.b31 + m.x172 <= 10)

m.c213 = Constraint(expr=   10*m.b32 + m.x173 <= 10)

m.c214 = Constraint(expr=   10*m.b33 + m.x174 <= 10)

m.c215 = Constraint(expr=   10*m.b34 + m.x175 <= 10)

m.c216 = Constraint(expr=   10*m.b35 + m.x176 <= 10)

m.c217 = Constraint(expr=   10*m.b36 + m.x177 <= 10)

m.c218 = Constraint(expr=   10*m.b37 + m.x178 <= 10)

m.c219 = Constraint(expr=   10*m.b38 + m.x179 <= 10)

m.c220 = Constraint(expr=   10*m.b39 + m.x180 <= 10)

m.c221 = Constraint(expr=   10*m.b40 + m.x181 <= 10)

m.c222 = Constraint(expr=   11*m.b41 + m.x182 <= 11)

m.c223 = Constraint(expr=   11*m.b42 + m.x183 <= 11)

m.c224 = Constraint(expr=   11*m.b43 + m.x184 <= 11)

m.c225 = Constraint(expr=   11*m.b44 + m.x185 <= 11)

m.c226 = Constraint(expr=   11*m.b45 + m.x186 <= 11)

m.c227 = Constraint(expr=   11*m.b46 + m.x187 <= 11)

m.c228 = Constraint(expr=   11*m.b47 + m.x188 <= 11)

m.c229 = Constraint(expr=   11*m.b48 + m.x189 <= 11)

m.c230 = Constraint(expr=   11*m.b49 + m.x190 <= 11)

m.c231 = Constraint(expr=   11*m.b50 + m.x191 <= 11)

m.c232 = Constraint(expr=   7*m.b51 + m.x192 <= 7)

m.c233 = Constraint(expr=   7*m.b52 + m.x193 <= 7)

m.c234 = Constraint(expr=   7*m.b53 + m.x194 <= 7)

m.c235 = Constraint(expr=   7*m.b54 + m.x195 <= 7)

m.c236 = Constraint(expr=   7*m.b55 + m.x196 <= 7)

m.c237 = Constraint(expr=   7*m.b56 + m.x197 <= 7)

m.c238 = Constraint(expr=   7*m.b57 + m.x198 <= 7)

m.c239 = Constraint(expr=   7*m.b58 + m.x199 <= 7)

m.c240 = Constraint(expr=   7*m.b59 + m.x200 <= 7)

m.c241 = Constraint(expr=   7*m.b60 + m.x201 <= 7)

m.c242 = Constraint(expr=   10*m.b61 + m.x202 <= 10)

m.c243 = Constraint(expr=   10*m.b62 + m.x203 <= 10)

m.c244 = Constraint(expr=   10*m.b63 + m.x204 <= 10)

m.c245 = Constraint(expr=   10*m.b64 + m.x205 <= 10)

m.c246 = Constraint(expr=   10*m.b65 + m.x206 <= 10)

m.c247 = Constraint(expr=   10*m.b66 + m.x207 <= 10)

m.c248 = Constraint(expr=   10*m.b67 + m.x208 <= 10)

m.c249 = Constraint(expr=   10*m.b68 + m.x209 <= 10)

m.c250 = Constraint(expr=   10*m.b69 + m.x210 <= 10)

m.c251 = Constraint(expr=   10*m.b70 + m.x211 <= 10)

m.c252 = Constraint(expr= - 471.299114292143*m.b21 - 87.3644508144726*m.b22 - 1199.55883169351*m.b23
                          - 1455.32236178753*m.b24 - 59.9123555503718*m.b25 - 379.038814816129*m.b26
                          - 1209.04864109044*m.b27 - 1788.49473840444*m.b28 - 938.567397231442*m.b29
                          - 2381.30274221782*m.b30 + m.x212 + m.x217 + m.x222 + m.x227 == 0)

m.c253 = Constraint(expr= - 471.299114292143*m.b31 - 87.3644508144726*m.b32 - 1199.55883169351*m.b33
                          - 1455.32236178753*m.b34 - 59.9123555503718*m.b35 - 379.038814816129*m.b36
                          - 1209.04864109044*m.b37 - 1788.49473840444*m.b38 - 938.567397231442*m.b39
                          - 2381.30274221782*m.b40 + m.x213 + m.x218 + m.x223 + m.x228 == 0)

m.c254 = Constraint(expr= - 471.299114292143*m.b41 - 87.3644508144726*m.b42 - 1199.55883169351*m.b43
                          - 1455.32236178753*m.b44 - 59.9123555503718*m.b45 - 379.038814816129*m.b46
                          - 1209.04864109044*m.b47 - 1788.49473840444*m.b48 - 938.567397231442*m.b49
                          - 2381.30274221782*m.b50 + m.x214 + m.x219 + m.x224 + m.x229 == 0)

m.c255 = Constraint(expr= - 471.299114292143*m.b51 - 87.3644508144726*m.b52 - 1199.55883169351*m.b53
                          - 1455.32236178753*m.b54 - 59.9123555503718*m.b55 - 379.038814816129*m.b56
                          - 1209.04864109044*m.b57 - 1788.49473840444*m.b58 - 938.567397231442*m.b59
                          - 2381.30274221782*m.b60 + m.x215 + m.x220 + m.x225 + m.x230 == 0)

m.c256 = Constraint(expr= - 471.299114292143*m.b61 - 87.3644508144726*m.b62 - 1199.55883169351*m.b63
                          - 1455.32236178753*m.b64 - 59.9123555503718*m.b65 - 379.038814816129*m.b66
                          - 1209.04864109044*m.b67 - 1788.49473840444*m.b68 - 938.567397231442*m.b69
                          - 2381.30274221782*m.b70 + m.x216 + m.x221 + m.x226 + m.x231 == 0)

m.c257 = Constraint(expr= - 9969.9094478983*m.b1 + m.x212 <= 0)

m.c258 = Constraint(expr= - 9969.9094478983*m.b2 + m.x213 <= 0)

m.c259 = Constraint(expr= - 9969.9094478983*m.b3 + m.x214 <= 0)

m.c260 = Constraint(expr= - 9969.9094478983*m.b4 + m.x215 <= 0)

m.c261 = Constraint(expr= - 9969.9094478983*m.b5 + m.x216 <= 0)

m.c262 = Constraint(expr= - 9969.9094478983*m.b6 + m.x217 <= 0)

m.c263 = Constraint(expr= - 9969.9094478983*m.b7 + m.x218 <= 0)

m.c264 = Constraint(expr= - 9969.9094478983*m.b8 + m.x219 <= 0)

m.c265 = Constraint(expr= - 9969.9094478983*m.b9 + m.x220 <= 0)

m.c266 = Constraint(expr= - 9969.9094478983*m.b10 + m.x221 <= 0)

m.c267 = Constraint(expr= - 9969.9094478983*m.b11 + m.x222 <= 0)

m.c268 = Constraint(expr= - 9969.9094478983*m.b12 + m.x223 <= 0)

m.c269 = Constraint(expr= - 9969.9094478983*m.b13 + m.x224 <= 0)

m.c270 = Constraint(expr= - 9969.9094478983*m.b14 + m.x225 <= 0)

m.c271 = Constraint(expr= - 9969.9094478983*m.b15 + m.x226 <= 0)

m.c272 = Constraint(expr=   9969.9094478983*m.b16 + m.x227 <= 9969.9094478983)

m.c273 = Constraint(expr=   9969.9094478983*m.b17 + m.x228 <= 9969.9094478983)

m.c274 = Constraint(expr=   9969.9094478983*m.b18 + m.x229 <= 9969.9094478983)

m.c275 = Constraint(expr=   9969.9094478983*m.b19 + m.x230 <= 9969.9094478983)

m.c276 = Constraint(expr=   9969.9094478983*m.b20 + m.x231 <= 9969.9094478983)

m.c277 = Constraint(expr=   m.x107 + 471.299114292143*m.x112 + 87.3644508144726*m.x113 + 1199.55883169351*m.x114
                          + 1455.32236178753*m.x115 + 59.9123555503718*m.x116 + 379.038814816129*m.x117
                          + 1209.04864109044*m.x118 + 1788.49473840444*m.x119 + 938.567397231442*m.x120
                          + 2381.30274221782*m.x121 - 11*m.x212 - 8*m.x217 - 7*m.x222 == 0)

m.c278 = Constraint(expr=   m.x108 + 471.299114292143*m.x122 + 87.3644508144726*m.x123 + 1199.55883169351*m.x124
                          + 1455.32236178753*m.x125 + 59.9123555503718*m.x126 + 379.038814816129*m.x127
                          + 1209.04864109044*m.x128 + 1788.49473840444*m.x129 + 938.567397231442*m.x130
                          + 2381.30274221782*m.x131 - 6*m.x213 - 7*m.x218 - 10*m.x223 == 0)

m.c279 = Constraint(expr=   m.x109 + 471.299114292143*m.x132 + 87.3644508144726*m.x133 + 1199.55883169351*m.x134
                          + 1455.32236178753*m.x135 + 59.9123555503718*m.x136 + 379.038814816129*m.x137
                          + 1209.04864109044*m.x138 + 1788.49473840444*m.x139 + 938.567397231442*m.x140
                          + 2381.30274221782*m.x141 - 10*m.x214 - 6*m.x219 - 11*m.x224 == 0)

m.c280 = Constraint(expr=   m.x110 + 471.299114292143*m.x142 + 87.3644508144726*m.x143 + 1199.55883169351*m.x144
                          + 1455.32236178753*m.x145 + 59.9123555503718*m.x146 + 379.038814816129*m.x147
                          + 1209.04864109044*m.x148 + 1788.49473840444*m.x149 + 938.567397231442*m.x150
                          + 2381.30274221782*m.x151 - 7*m.x215 - 6*m.x220 - 7*m.x225 == 0)

m.c281 = Constraint(expr=   m.x111 + 471.299114292143*m.x152 + 87.3644508144726*m.x153 + 1199.55883169351*m.x154
                          + 1455.32236178753*m.x155 + 59.9123555503718*m.x156 + 379.038814816129*m.x157
                          + 1209.04864109044*m.x158 + 1788.49473840444*m.x159 + 938.567397231442*m.x160
                          + 2381.30274221782*m.x161 - 7*m.x216 - 4*m.x221 - 10*m.x226 == 0)
