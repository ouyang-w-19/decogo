#  MINLP written by GAMS Convert at 04/21/18 13:52:14
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        310      142       48      120        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        237      164       73        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1014      836      178        0
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
m.b71 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b72 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b73 = Var(within=Binary,bounds=(0,1),initialize=0)
m.x74 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x75 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x76 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x77 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x78 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x79 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x80 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x81 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x82 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x83 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x84 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x85 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x86 = Var(within=Reals,bounds=(0,None),initialize=0)
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
m.x107 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x108 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x109 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x110 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x111 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x112 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x113 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x114 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x115 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x116 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x117 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x118 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x119 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x120 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x121 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x122 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x123 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x124 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x125 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x126 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x127 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x128 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x129 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x130 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x131 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x132 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x133 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x134 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x135 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x136 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x137 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x138 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x139 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x140 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x141 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x142 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x143 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x144 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x145 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x146 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x147 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x148 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x149 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x150 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x151 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x152 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x153 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x154 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x155 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x156 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x157 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x158 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x159 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x160 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x161 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x162 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x163 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x164 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x165 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x166 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x167 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x168 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x169 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x170 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x171 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x172 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x173 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x174 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x175 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x176 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x177 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x178 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x179 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x180 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x181 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x182 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x183 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x184 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x185 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x186 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x187 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x188 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x189 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x190 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x191 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x192 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x193 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x194 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x195 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x196 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x197 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x198 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x199 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x200 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x201 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x202 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x203 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x204 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x205 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x206 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x207 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x208 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x209 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x210 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x211 = Var(within=Reals,bounds=(0,None),initialize=0)
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
m.x230 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x231 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x232 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x233 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x234 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x235 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x236 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr= - m.x230 - m.x231 - m.x232 - m.x234 + m.x235 + m.x236, sense=maximize)

m.c1 = Constraint(expr=   m.x75 == 7791.10108432975)

m.c2 = Constraint(expr=   m.x76 == 9249.06867273578)

m.c3 = Constraint(expr=   m.x77 == 10096.0784145717)

m.c4 = Constraint(expr=   m.x78 == 10051.6451166393)

m.c5 = Constraint(expr=   m.x79 == 9637.86002964406)

m.c6 = Constraint(expr=   m.x80 == 10330.741769277)

m.c7 = Constraint(expr=   m.x81 == 11612.3647065139)

m.c8 = Constraint(expr=   m.x82 == 11152.7577810259)

m.c9 = Constraint(expr=   m.x83 == 11005.572481625)

m.c10 = Constraint(expr=   m.x84 == 11165.2546460694)

m.c11 = Constraint(expr=   m.x85 == 8811.67839621397)

m.c12 = Constraint(expr=   m.x86 == 7295.54964171257)

m.c13 = Constraint(expr=   m.x87 == 8264.56262094388)

m.c14 = Constraint(expr=   m.x88 == 11772.1524347523)

m.c15 = Constraint(expr=   m.x89 == 9638.4603939449)

m.c16 = Constraint(expr=   m.x90 == 9595.2613887519)

m.c17 = Constraint(expr=   m.x91 == 9200.54106679229)

m.c18 = Constraint(expr=   m.x92 == 10682.8598724346)

m.c19 = Constraint(expr=   m.x93 == 12008.4764043375)

m.c20 = Constraint(expr=   m.x94 == 11533.2873472145)

m.c21 = Constraint(expr=   m.x95 == 11380.8202700627)

m.c22 = Constraint(expr=   m.x96 == 8881.20724409107)

m.c23 = Constraint(expr=   m.x97 == 7010.09739171175)

m.c24 = Constraint(expr=   m.x98 == 10282.2488966628)

m.c25 = Constraint(expr=   m.x99 == 8735.60231062138)

m.c26 = Constraint(expr=   m.x100 == 10369.3707213156)

m.c27 = Constraint(expr=   m.x101 == 9988.09563923272)

m.c28 = Constraint(expr=   m.x102 == 9943.12953618609)

m.c29 = Constraint(expr=   m.x103 == 9534.68743351253)

m.c30 = Constraint(expr=   m.x104 == 10218.5469173467)

m.c31 = Constraint(expr=   m.x105 == 11486.9657407871)

m.c32 = Constraint(expr=   m.x106 == 11031.6839474399)

m.c33 = Constraint(expr=   m.x107 == 10886.4809063518)

m.c34 = Constraint(expr=   m.x108 == 9387.61080479751)

m.c35 = Constraint(expr=   m.x109 == 7409.10227074579)

m.c36 = Constraint(expr=   m.x110 == 1118.55473503165)

m.c37 = Constraint(expr=   m.x111 == 950.53653428635)

m.c38 = Constraint(expr=   m.x112 == 1127.95435465377)

m.c39 = Constraint(expr=   m.x113 == 923.51262787277)

m.c40 = Constraint(expr=   m.x114 == 919.4002942881)

m.c41 = Constraint(expr=   m.x115 == 881.80181579964)

m.c42 = Constraint(expr=   m.x116 == 945.24924824891)

m.c43 = Constraint(expr=   m.x117 == 1062.15701729896)

m.c44 = Constraint(expr=   m.x118 == 1020.44620522583)

m.c45 = Constraint(expr=   m.x119 == 1006.93425201904)

m.c46 = Constraint(expr=   m.x120 == 1021.62115767859)

m.c47 = Constraint(expr=   m.x121 == 806.01738259634)

m.c48 = Constraint(expr=   m.x122 == 0)

m.c49 = Constraint(expr=   m.x123 == 0)

m.c50 = Constraint(expr=   m.x124 == 0)

m.c51 = Constraint(expr=   m.x125 == 628.45542857142)

m.c52 = Constraint(expr=   m.x126 == 628.45542857142)

m.c53 = Constraint(expr=   m.x127 == 628.45542857142)

m.c54 = Constraint(expr=   m.x128 == 628.45542857142)

m.c55 = Constraint(expr=   m.x129 == 628.45542857142)

m.c56 = Constraint(expr=   m.x130 == 628.45542857142)

m.c57 = Constraint(expr=   m.x131 == 628.45542857142)

m.c58 = Constraint(expr=   m.x132 == 0)

m.c59 = Constraint(expr=   m.x133 == 0)

m.c60 = Constraint(expr=   m.x134 <= 6000)

m.c61 = Constraint(expr=   m.x135 <= 6000)

m.c62 = Constraint(expr=   m.x136 <= 6000)

m.c63 = Constraint(expr=   m.x137 <= 6000)

m.c64 = Constraint(expr=   m.x138 <= 6000)

m.c65 = Constraint(expr=   m.x139 <= 6000)

m.c66 = Constraint(expr=   m.x140 <= 6000)

m.c67 = Constraint(expr=   m.x141 <= 6000)

m.c68 = Constraint(expr=   m.x142 <= 6000)

m.c69 = Constraint(expr=   m.x143 <= 6000)

m.c70 = Constraint(expr=   m.x144 <= 6000)

m.c71 = Constraint(expr=   m.x145 <= 6000)

m.c72 = Constraint(expr=   m.x146 <= 20800)

m.c73 = Constraint(expr=   m.x147 <= 20800)

m.c74 = Constraint(expr=   m.x148 <= 20800)

m.c75 = Constraint(expr=   m.x149 <= 0)

m.c76 = Constraint(expr=   m.x150 <= 0)

m.c77 = Constraint(expr=   m.x151 <= 0)

m.c78 = Constraint(expr=   m.x152 <= 20800)

m.c79 = Constraint(expr=   m.x153 <= 20800)

m.c80 = Constraint(expr=   m.x154 <= 20800)

m.c81 = Constraint(expr=   m.x155 <= 20800)

m.c82 = Constraint(expr=   m.x156 <= 20800)

m.c83 = Constraint(expr=   m.x157 <= 20800)

m.c84 = Constraint(expr=   m.x158 <= 238)

m.c85 = Constraint(expr=   m.x159 <= 202)

m.c86 = Constraint(expr=   m.x160 <= 240)

m.c87 = Constraint(expr=   m.x161 <= 197)

m.c88 = Constraint(expr=   m.x162 <= 196)

m.c89 = Constraint(expr=   m.x163 <= 188)

m.c90 = Constraint(expr=   m.x164 <= 201)

m.c91 = Constraint(expr=   m.x165 <= 226)

m.c92 = Constraint(expr=   m.x166 <= 217)

m.c93 = Constraint(expr=   m.x167 <= 214)

m.c94 = Constraint(expr=   m.x168 <= 217)

m.c95 = Constraint(expr=   m.x169 <= 172)

m.c96 = Constraint(expr=   m.x170 <= 500)

m.c97 = Constraint(expr=   m.x171 <= 500)

m.c98 = Constraint(expr=   m.x172 <= 500)

m.c99 = Constraint(expr=   m.x173 <= 500)

m.c100 = Constraint(expr=   m.x174 <= 500)

m.c101 = Constraint(expr=   m.x175 <= 500)

m.c102 = Constraint(expr=   m.x176 <= 500)

m.c103 = Constraint(expr=   m.x177 <= 500)

m.c104 = Constraint(expr=   m.x178 <= 500)

m.c105 = Constraint(expr=   m.x179 <= 500)

m.c106 = Constraint(expr=   m.x180 <= 500)

m.c107 = Constraint(expr=   m.x181 <= 500)

m.c108 = Constraint(expr=   m.x182 <= 230000)

m.c109 = Constraint(expr=   m.x183 <= 230000)

m.c110 = Constraint(expr=   m.x184 <= 230000)

m.c111 = Constraint(expr=   m.x185 <= 230000)

m.c112 = Constraint(expr=   m.x186 <= 230000)

m.c113 = Constraint(expr=   m.x187 <= 230000)

m.c114 = Constraint(expr=   m.x188 <= 230000)

m.c115 = Constraint(expr=   m.x189 <= 230000)

m.c116 = Constraint(expr=   m.x190 <= 230000)

m.c117 = Constraint(expr=   m.x191 <= 230000)

m.c118 = Constraint(expr=   m.x192 <= 230000)

m.c119 = Constraint(expr=   m.x193 <= 230000)

m.c120 = Constraint(expr= - m.x74 - m.x86 - m.x98 - m.x110 - m.x122 - m.x134 - m.x146 - m.x158 - m.x170 + m.x182
                          + m.x194 == 80000)

m.c121 = Constraint(expr= - m.x75 - m.x87 - m.x99 - m.x111 - m.x123 - m.x135 - m.x147 - m.x159 - m.x171 - m.x182
                          + m.x183 + m.x195 == 0)

m.c122 = Constraint(expr= - m.x76 - m.x88 - m.x100 - m.x112 - m.x124 - m.x136 - m.x148 - m.x160 - m.x172 - m.x183
                          + m.x184 + m.x196 == 0)

m.c123 = Constraint(expr= - m.x77 - m.x89 - m.x101 - m.x113 - m.x125 - m.x137 - m.x149 - m.x161 - m.x173 - m.x184
                          + m.x185 + m.x197 == 0)

m.c124 = Constraint(expr= - m.x78 - m.x90 - m.x102 - m.x114 - m.x126 - m.x138 - m.x150 - m.x162 - m.x174 - m.x185
                          + m.x186 + m.x198 == 0)

m.c125 = Constraint(expr= - m.x79 - m.x91 - m.x103 - m.x115 - m.x127 - m.x139 - m.x151 - m.x163 - m.x175 - m.x186
                          + m.x187 + m.x199 == 0)

m.c126 = Constraint(expr= - m.x80 - m.x92 - m.x104 - m.x116 - m.x128 - m.x140 - m.x152 - m.x164 - m.x176 - m.x187
                          + m.x188 + m.x200 == 0)

m.c127 = Constraint(expr= - m.x81 - m.x93 - m.x105 - m.x117 - m.x129 - m.x141 - m.x153 - m.x165 - m.x177 - m.x188
                          + m.x189 + m.x201 == 0)

m.c128 = Constraint(expr= - m.x82 - m.x94 - m.x106 - m.x118 - m.x130 - m.x142 - m.x154 - m.x166 - m.x178 - m.x189
                          + m.x190 + m.x202 == 0)

m.c129 = Constraint(expr= - m.x83 - m.x95 - m.x107 - m.x119 - m.x131 - m.x143 - m.x155 - m.x167 - m.x179 - m.x190
                          + m.x191 + m.x203 == 0)

m.c130 = Constraint(expr= - m.x84 - m.x96 - m.x108 - m.x120 - m.x132 - m.x144 - m.x156 - m.x168 - m.x180 - m.x191
                          + m.x192 + m.x204 == 0)

m.c131 = Constraint(expr= - m.x85 - m.x97 - m.x109 - m.x121 - m.x133 - m.x145 - m.x157 - m.x169 - m.x181 - m.x192
                          + m.x193 + m.x205 == 0)

m.c132 = Constraint(expr=0.018*m.x218*m.x206 - 0.3*m.x194*m.x218 == -49104)

m.c133 = Constraint(expr=0.018*m.x219*m.x207 - 0.3*m.x195*m.x219 == -44352)

m.c134 = Constraint(expr=0.018*m.x220*m.x208 - 0.3*m.x196*m.x220 == -49104)

m.c135 = Constraint(expr=0.018*m.x221*m.x209 - 0.3*m.x197*m.x221 == -47520)

m.c136 = Constraint(expr=0.018*m.x222*m.x210 - 0.3*m.x198*m.x222 == -28512)

m.c137 = Constraint(expr=0.018*m.x223*m.x211 - 0.3*m.x199*m.x223 == -47520)

m.c138 = Constraint(expr=0.018*m.x224*m.x212 - 0.3*m.x200*m.x224 == -49104)

m.c139 = Constraint(expr=0.018*m.x225*m.x213 - 0.3*m.x201*m.x225 == -49104)

m.c140 = Constraint(expr=0.018*m.x226*m.x214 - 0.3*m.x202*m.x226 == -45936)

m.c141 = Constraint(expr=0.018*m.x227*m.x215 - 0.3*m.x203*m.x227 + 14360*m.b73 == -34744)

m.c142 = Constraint(expr=0.018*m.x228*m.x216 - 0.3*m.x204*m.x228 + 47520*m.b73 == 0)

m.c143 = Constraint(expr=0.018*m.x229*m.x217 - 0.3*m.x205*m.x229 + 49104*m.b73 == 0)

m.c144 = Constraint(expr=   10000000000*m.b49 + m.x182 >= 120000)

m.c145 = Constraint(expr=   10000000000*m.b50 + m.x183 >= 120000)

m.c146 = Constraint(expr=   10000000000*m.b51 + m.x184 >= 120000)

m.c147 = Constraint(expr=   10000000000*m.b52 + m.x185 >= 120000)

m.c148 = Constraint(expr=   10000000000*m.b53 + m.x186 >= 120000)

m.c149 = Constraint(expr=   10000000000*m.b54 + m.x187 >= 120000)

m.c150 = Constraint(expr=   10000000000*m.b55 + m.x188 >= 120000)

m.c151 = Constraint(expr=   10000000000*m.b56 + m.x189 >= 120000)

m.c152 = Constraint(expr=   10000000000*m.b57 + m.x190 >= 120000)

m.c153 = Constraint(expr=   10000000000*m.b58 + m.x191 >= 120000)

m.c154 = Constraint(expr=   10000000000*m.b59 + m.x192 >= 120000)

m.c155 = Constraint(expr=   10000000000*m.b60 + m.x193 >= 120000)

m.c156 = Constraint(expr=   m.b49 + m.b61 == 1)

m.c157 = Constraint(expr=   m.b50 + m.b62 == 1)

m.c158 = Constraint(expr=   m.b51 + m.b63 == 1)

m.c159 = Constraint(expr=   m.b52 + m.b64 == 1)

m.c160 = Constraint(expr=   m.b53 + m.b65 == 1)

m.c161 = Constraint(expr=   m.b54 + m.b66 == 1)

m.c162 = Constraint(expr=   m.b55 + m.b67 == 1)

m.c163 = Constraint(expr=   m.b56 + m.b68 == 1)

m.c164 = Constraint(expr=   m.b57 + m.b69 == 1)

m.c165 = Constraint(expr=   m.b58 + m.b70 == 1)

m.c166 = Constraint(expr=   m.b59 + m.b71 == 1)

m.c167 = Constraint(expr=   m.b60 + m.b72 == 1)

m.c168 = Constraint(expr=   10000000000*m.b49 + m.x182 <= 10000120000)

m.c169 = Constraint(expr=   10000000000*m.b50 + m.x183 <= 10000120000)

m.c170 = Constraint(expr=   10000000000*m.b51 + m.x184 <= 10000120000)

m.c171 = Constraint(expr=   10000000000*m.b52 + m.x185 <= 10000120000)

m.c172 = Constraint(expr=   10000000000*m.b53 + m.x186 <= 10000120000)

m.c173 = Constraint(expr=   10000000000*m.b54 + m.x187 <= 10000120000)

m.c174 = Constraint(expr=   10000000000*m.b55 + m.x188 <= 10000120000)

m.c175 = Constraint(expr=   10000000000*m.b56 + m.x189 <= 10000120000)

m.c176 = Constraint(expr=   10000000000*m.b57 + m.x190 <= 10000120000)

m.c177 = Constraint(expr=   10000000000*m.b58 + m.x191 <= 10000120000)

m.c178 = Constraint(expr=   10000000000*m.b59 + m.x192 <= 10000120000)

m.c179 = Constraint(expr=   10000000000*m.b60 + m.x193 <= 10000120000)

m.c180 = Constraint(expr=   10000000000*m.b25 + m.x182 >= 180000)

m.c181 = Constraint(expr=   10000000000*m.b26 + m.x183 >= 180000)

m.c182 = Constraint(expr=   10000000000*m.b27 + m.x184 >= 180000)

m.c183 = Constraint(expr=   10000000000*m.b28 + m.x185 >= 180000)

m.c184 = Constraint(expr=   10000000000*m.b29 + m.x186 >= 180000)

m.c185 = Constraint(expr=   10000000000*m.b30 + m.x187 >= 180000)

m.c186 = Constraint(expr=   10000000000*m.b31 + m.x188 >= 180000)

m.c187 = Constraint(expr=   10000000000*m.b32 + m.x189 >= 180000)

m.c188 = Constraint(expr=   10000000000*m.b33 + m.x190 >= 180000)

m.c189 = Constraint(expr=   10000000000*m.b34 + m.x191 >= 180000)

m.c190 = Constraint(expr=   10000000000*m.b35 + m.x192 >= 180000)

m.c191 = Constraint(expr=   10000000000*m.b36 + m.x193 >= 180000)

m.c192 = Constraint(expr=   m.b25 + m.b37 == 1)

m.c193 = Constraint(expr=   m.b26 + m.b38 == 1)

m.c194 = Constraint(expr=   m.b27 + m.b39 == 1)

m.c195 = Constraint(expr=   m.b28 + m.b40 == 1)

m.c196 = Constraint(expr=   m.b29 + m.b41 == 1)

m.c197 = Constraint(expr=   m.b30 + m.b42 == 1)

m.c198 = Constraint(expr=   m.b31 + m.b43 == 1)

m.c199 = Constraint(expr=   m.b32 + m.b44 == 1)

m.c200 = Constraint(expr=   m.b33 + m.b45 == 1)

m.c201 = Constraint(expr=   m.b34 + m.b46 == 1)

m.c202 = Constraint(expr=   m.b35 + m.b47 == 1)

m.c203 = Constraint(expr=   m.b36 + m.b48 == 1)

m.c204 = Constraint(expr=   10000000000*m.b25 + m.x182 <= 10000180000)

m.c205 = Constraint(expr=   10000000000*m.b26 + m.x183 <= 10000180000)

m.c206 = Constraint(expr=   10000000000*m.b27 + m.x184 <= 10000180000)

m.c207 = Constraint(expr=   10000000000*m.b28 + m.x185 <= 10000180000)

m.c208 = Constraint(expr=   10000000000*m.b29 + m.x186 <= 10000180000)

m.c209 = Constraint(expr=   10000000000*m.b30 + m.x187 <= 10000180000)

m.c210 = Constraint(expr=   10000000000*m.b31 + m.x188 <= 10000180000)

m.c211 = Constraint(expr=   10000000000*m.b32 + m.x189 <= 10000180000)

m.c212 = Constraint(expr=   10000000000*m.b33 + m.x190 <= 10000180000)

m.c213 = Constraint(expr=   10000000000*m.b34 + m.x191 <= 10000180000)

m.c214 = Constraint(expr=   10000000000*m.b35 + m.x192 <= 10000180000)

m.c215 = Constraint(expr=   10000000000*m.b36 + m.x193 <= 10000180000)

m.c216 = Constraint(expr=   100000000*m.b1 - m.x182 >= -50000)

m.c217 = Constraint(expr=   100000000*m.b2 - m.x183 >= -50000)

m.c218 = Constraint(expr=   100000000*m.b3 - m.x184 >= -50000)

m.c219 = Constraint(expr=   100000000*m.b4 - m.x185 >= -50000)

m.c220 = Constraint(expr=   100000000*m.b5 - m.x186 >= -50000)

m.c221 = Constraint(expr=   100000000*m.b6 - m.x187 >= -50000)

m.c222 = Constraint(expr=   100000000*m.b7 - m.x188 >= -50000)

m.c223 = Constraint(expr=   100000000*m.b8 - m.x189 >= -50000)

m.c224 = Constraint(expr=   100000000*m.b9 - m.x190 >= -50000)

m.c225 = Constraint(expr=   100000000*m.b10 - m.x191 >= -50000)

m.c226 = Constraint(expr=   100000000*m.b11 - m.x192 >= -50000)

m.c227 = Constraint(expr=   100000000*m.b12 - m.x193 >= -50000)

m.c228 = Constraint(expr=   m.b1 + m.b13 == 1)

m.c229 = Constraint(expr=   m.b2 + m.b14 == 1)

m.c230 = Constraint(expr=   m.b3 + m.b15 == 1)

m.c231 = Constraint(expr=   m.b4 + m.b16 == 1)

m.c232 = Constraint(expr=   m.b5 + m.b17 == 1)

m.c233 = Constraint(expr=   m.b6 + m.b18 == 1)

m.c234 = Constraint(expr=   m.b7 + m.b19 == 1)

m.c235 = Constraint(expr=   m.b8 + m.b20 == 1)

m.c236 = Constraint(expr=   m.b9 + m.b21 == 1)

m.c237 = Constraint(expr=   m.b10 + m.b22 == 1)

m.c238 = Constraint(expr=   m.b11 + m.b23 == 1)

m.c239 = Constraint(expr=   m.b12 + m.b24 == 1)

m.c240 = Constraint(expr=   100000000*m.b1 - m.x182 <= 99950000)

m.c241 = Constraint(expr=   100000000*m.b2 - m.x183 <= 99950000)

m.c242 = Constraint(expr=   100000000*m.b3 - m.x184 <= 99950000)

m.c243 = Constraint(expr=   100000000*m.b4 - m.x185 <= 99950000)

m.c244 = Constraint(expr=   100000000*m.b5 - m.x186 <= 99950000)

m.c245 = Constraint(expr=   100000000*m.b6 - m.x187 <= 99950000)

m.c246 = Constraint(expr=   100000000*m.b7 - m.x188 <= 99950000)

m.c247 = Constraint(expr=   100000000*m.b8 - m.x189 <= 99950000)

m.c248 = Constraint(expr=   100000000*m.b9 - m.x190 <= 99950000)

m.c249 = Constraint(expr=   100000000*m.b10 - m.x191 <= 99950000)

m.c250 = Constraint(expr=   100000000*m.b11 - m.x192 <= 99950000)

m.c251 = Constraint(expr=   100000000*m.b12 - m.x193 <= 99950000)

m.c252 = Constraint(expr=   m.x193 == 50000)

m.c253 = Constraint(expr= - 100000000*m.b13 + m.x206 <= 0)

m.c254 = Constraint(expr= - 100000000*m.b14 + m.x207 <= 0)

m.c255 = Constraint(expr= - 100000000*m.b15 + m.x208 <= 0)

m.c256 = Constraint(expr= - 100000000*m.b16 + m.x209 <= 0)

m.c257 = Constraint(expr= - 100000000*m.b17 + m.x210 <= 0)

m.c258 = Constraint(expr= - 100000000*m.b18 + m.x211 <= 0)

m.c259 = Constraint(expr= - 100000000*m.b19 + m.x212 <= 0)

m.c260 = Constraint(expr= - 100000000*m.b20 + m.x213 <= 0)

m.c261 = Constraint(expr= - 100000000*m.b21 + m.x214 <= 0)

m.c262 = Constraint(expr= - 100000000*m.b22 + m.x215 <= 0)

m.c263 = Constraint(expr= - 100000000*m.b23 + m.x216 <= 0)

m.c264 = Constraint(expr= - 100000000*m.b24 + m.x217 <= 0)

m.c265 = Constraint(expr= - m.x194 + m.x206 <= 0)

m.c266 = Constraint(expr= - m.x195 + m.x207 <= 0)

m.c267 = Constraint(expr= - m.x196 + m.x208 <= 0)

m.c268 = Constraint(expr= - m.x197 + m.x209 <= 0)

m.c269 = Constraint(expr= - m.x198 + m.x210 <= 0)

m.c270 = Constraint(expr= - m.x199 + m.x211 <= 0)

m.c271 = Constraint(expr= - m.x200 + m.x212 <= 0)

m.c272 = Constraint(expr= - m.x201 + m.x213 <= 0)

m.c273 = Constraint(expr= - m.x202 + m.x214 <= 0)

m.c274 = Constraint(expr= - m.x203 + m.x215 <= 0)

m.c275 = Constraint(expr= - m.x204 + m.x216 <= 0)

m.c276 = Constraint(expr= - m.x205 + m.x217 <= 0)

m.c277 = Constraint(expr= - 100000000*m.b13 - m.x194 + m.x206 >= -100000000)

m.c278 = Constraint(expr= - 100000000*m.b14 - m.x195 + m.x207 >= -100000000)

m.c279 = Constraint(expr= - 100000000*m.b15 - m.x196 + m.x208 >= -100000000)

m.c280 = Constraint(expr= - 100000000*m.b16 - m.x197 + m.x209 >= -100000000)

m.c281 = Constraint(expr= - 100000000*m.b17 - m.x198 + m.x210 >= -100000000)

m.c282 = Constraint(expr= - 100000000*m.b18 - m.x199 + m.x211 >= -100000000)

m.c283 = Constraint(expr= - 100000000*m.b19 - m.x200 + m.x212 >= -100000000)

m.c284 = Constraint(expr= - 100000000*m.b20 - m.x201 + m.x213 >= -100000000)

m.c285 = Constraint(expr= - 100000000*m.b21 - m.x202 + m.x214 >= -100000000)

m.c286 = Constraint(expr= - 100000000*m.b22 - m.x203 + m.x215 >= -100000000)

m.c287 = Constraint(expr= - 100000000*m.b23 - m.x204 + m.x216 >= -100000000)

m.c288 = Constraint(expr= - 100000000*m.b24 - m.x205 + m.x217 >= -100000000)

m.c289 = Constraint(expr=(m.x75 + m.x87 + m.x99 + m.x111 + m.x123 + m.x135 + m.x147 + m.x159 + m.x171 + m.x182)*m.x219
                          - m.x182*m.x218 - 3.45306900938*m.x75 - 2.89465224642*m.x87 - 3.3907445128*m.x99 - 
                         2.92984041218*m.x111 - 1.99104678785*m.x123 - 3.20721402214*m.x135 - 3.23089372607*m.x147 - 
                         2.72277689967*m.x159 - 3.98576673328*m.x171 == 0)

m.c290 = Constraint(expr=(m.x76 + m.x88 + m.x100 + m.x112 + m.x124 + m.x136 + m.x148 + m.x160 + m.x172 + m.x183)*m.x220
                          - m.x183*m.x219 - 3.71204918508*m.x76 - 3.13873771232*m.x88 - 3.84462369955*m.x100 - 
                         2.92984041218*m.x112 - 3.72025957148*m.x124 - 3.19346390844*m.x136 - 3.32339415853*m.x148 - 
                         4.17259954891*m.x160 - 3.98576673328*m.x172 == 0)

m.c291 = Constraint(expr=(m.x77 + m.x89 + m.x101 + m.x113 + m.x125 + m.x137 + m.x149 + m.x161 + m.x173 + m.x184)*m.x221
                          - m.x184*m.x220 - 3.30072772955*m.x77 - 3.25387105584*m.x89 - 3.76719725005*m.x101 - 
                         2.92984041218*m.x113 - 4.04067067003*m.x125 - 3.00611860918*m.x137 - 2.70045260066*m.x149 - 
                         4.33701242665*m.x161 - 3.98576673328*m.x173 == 0)

m.c292 = Constraint(expr=(m.x78 + m.x90 + m.x102 + m.x114 + m.x126 + m.x138 + m.x150 + m.x162 + m.x174 + m.x185)*m.x222
                          - m.x185*m.x221 - 3.30072772955*m.x78 - 3.30782679041*m.x90 - 3.47084083987*m.x102 - 
                         2.92984041218*m.x114 - 3.19872785585*m.x126 - 2.99064973126*m.x138 - 3.22433875168*m.x150 - 
                         3.29323976337*m.x162 - 3.98576673328*m.x174 == 0)

m.c293 = Constraint(expr=(m.x79 + m.x91 + m.x103 + m.x115 + m.x127 + m.x139 + m.x151 + m.x163 + m.x175 + m.x186)*m.x223
                          - m.x186*m.x222 - 4.12337064061*m.x79 - 3.18484660261*m.x91 - 2.91550630549*m.x103 - 
                         2.92984041218*m.x115 - 3.6817655639*m.x127 - 2.97861838176*m.x139 - 3.69558826155*m.x151 - 
                         3.67853054759*m.x163 - 3.98576673328*m.x175 == 0)

m.c294 = Constraint(expr=(m.x80 + m.x92 + m.x104 + m.x116 + m.x128 + m.x140 + m.x152 + m.x164 + m.x176 + m.x187)*m.x224
                          - m.x187*m.x223 - 3.2626424096*m.x80 - 3.26650933601*m.x92 - 3.36226581873*m.x104 - 
                         2.92984041218*m.x116 - 4.39438760391*m.x128 - 3.17111997366*m.x140 - 3.78307381649*m.x152 - 
                         3.57473453891*m.x164 - 3.98576673328*m.x176 == 0)

m.c295 = Constraint(expr=(m.x81 + m.x93 + m.x105 + m.x117 + m.x129 + m.x141 + m.x153 + m.x165 + m.x177 + m.x188)*m.x225
                          - m.x188*m.x224 - 3.76452229258*m.x81 - 3.09556849526*m.x93 - 3.34535659412*m.x105 - 
                         2.92984041218*m.x117 - 4.20801589981*m.x129 - 3.41862202039*m.x141 - 3.9128590882*m.x153 - 
                         3.53653760772*m.x165 - 3.98576673328*m.x177 == 0)

m.c296 = Constraint(expr=(m.x82 + m.x94 + m.x106 + m.x118 + m.x130 + m.x142 + m.x154 + m.x166 + m.x178 + m.x189)*m.x226
                          - m.x189*m.x225 - 3.41752271075*m.x82 - 3.15592438453*m.x94 - 3.56695643236*m.x106 - 
                         2.92984041218*m.x118 - 3.98773617096*m.x130 - 3.44870039412*m.x142 - 3.74366715891*m.x154 - 
                         4.09537531845*m.x166 - 3.98576673328*m.x178 == 0)

m.c297 = Constraint(expr=(m.x83 + m.x95 + m.x107 + m.x119 + m.x131 + m.x143 + m.x155 + m.x167 + m.x179 + m.x190)*m.x227
                          - m.x190*m.x226 - 3.3794373908*m.x83 - 3.43664003059*m.x95 - 3.52423839126*m.x107 - 
                         2.92984041218*m.x119 - 4.46282139516*m.x131 - 3.24158930641*m.x143 - 3.47930953913*m.x155 - 
                         3.66989471967*m.x167 - 3.98576673328*m.x179 == 0)

m.c298 = Constraint(expr=(m.x84 + m.x96 + m.x108 + m.x120 + m.x132 + m.x144 + m.x156 + m.x168 + m.x180 + m.x191)*m.x228
                          - m.x191*m.x227 - 3.30072772955*m.x84 - 3.17901355022*m.x96 - 3.47084083987*m.x108 - 
                         2.92984041218*m.x120 - 3.97357497622*m.x132 - 3.09635373038*m.x144 - 3.55421340859*m.x156 - 
                         3.93594464912*m.x168 - 3.98576673328*m.x180 == 0)

m.c299 = Constraint(expr=(m.x85 + m.x97 + m.x109 + m.x121 + m.x133 + m.x145 + m.x157 + m.x169 + m.x181 + m.x192)*m.x229
                          - m.x192*m.x228 - 3.30072772955*m.x85 - 3.15957004227*m.x97 - 3.43025870082*m.x109 - 
                         2.92984041218*m.x121 - 3.7252265402*m.x133 - 3.85175060216*m.x145 - 3.19457562475*m.x157 - 
                         3.68683422829*m.x169 - 3.98576673328*m.x181 == 0)

m.c300 = Constraint(expr=(80000 + m.x74 + m.x86 + m.x98 + m.x110 + m.x122 + m.x134 + m.x146 + m.x158 + m.x170)*m.x218 - 
                         3.63080050251*m.x74 - 2.86305654599*m.x86 - 3.41744328849*m.x98 - 2.92984041218*m.x110 - 
                         3.48432855727*m.x122 - 3.23041733902*m.x134 - 3.6417311747*m.x146 - 4.28469923828*m.x158 - 
                         3.98576673328*m.x170 == 260000)

m.c301 = Constraint(expr=   m.b73 == 1)

m.c302 = Constraint(expr=   m.x236 == 21546900)

m.c303 = Constraint(expr= - 4716820*m.b73 + m.x235 == 0)

m.c304 = Constraint(expr= - 15.6863186*m.x74 - 15.6863186*m.x75 - 15.6863186*m.x76 - 15.6863186*m.x77 - 15.6863186*m.x78
                          - 15.6863186*m.x79 - 15.6863186*m.x80 - 15.6863186*m.x81 - 15.6863186*m.x82 - 15.6863186*m.x83
                          - 15.6863186*m.x84 - 15.6863186*m.x85 - 2.1*m.x86 - 2.1*m.x87 - 2.1*m.x88 - 2.1*m.x89
                          - 2.1*m.x90 - 2.1*m.x91 - 2.1*m.x92 - 2.1*m.x93 - 2.1*m.x94 - 2.1*m.x95 - 2.1*m.x96
                          - 2.1*m.x97 - 14.2418893*m.x98 - 14.2418893*m.x99 - 14.2418893*m.x100 - 14.2418893*m.x101
                          - 14.2418893*m.x102 - 14.2418893*m.x103 - 14.2418893*m.x104 - 14.2418893*m.x105
                          - 14.2418893*m.x106 - 14.2418893*m.x107 - 14.2418893*m.x108 - 14.2418893*m.x109 - 2.1*m.x110
                          - 2.1*m.x111 - 2.1*m.x112 - 2.1*m.x113 - 2.1*m.x114 - 2.1*m.x115 - 2.1*m.x116 - 2.1*m.x117
                          - 2.1*m.x118 - 2.1*m.x119 - 2.1*m.x120 - 2.1*m.x121 - 24.630475*m.x122 - 24.630475*m.x123
                          - 24.630475*m.x124 - 24.630475*m.x125 - 24.630475*m.x126 - 24.630475*m.x127 - 24.630475*m.x128
                          - 24.630475*m.x129 - 24.630475*m.x130 - 24.630475*m.x131 - 24.630475*m.x132 - 24.630475*m.x133
                          - 23.7441195*m.x134 - 23.707386*m.x135 - 23.685618*m.x136 - 23.389029*m.x137 - 23.36454*m.x138
                          - 23.345493*m.x139 - 23.650245*m.x140 - 24.042069*m.x141 - 24.0896865*m.x142
                          - 23.761806*m.x143 - 23.5318815*m.x144 - 24.727761*m.x145 - 60.18757142857*m.x146
                          - 54.63853571428*m.x147 - 55.88790625*m.x148 - 47.47405555555*m.x149 - 54.55*m.x150
                          - 60.915*m.x151 - 62.09663636363*m.x152 - 63.8496*m.x153 - 61.56438461538*m.x154
                          - 57.9938*m.x155 - 59.0055*m.x156 - 54.148*m.x157 - 15*m.x158 - 15*m.x159 - 15*m.x160
                          - 15*m.x161 - 15*m.x162 - 15*m.x163 - 15*m.x164 - 15*m.x165 - 15*m.x166 - 15*m.x167
                          - 15*m.x168 - 15*m.x169 - 42*m.x170 - 42*m.x171 - 42*m.x172 - 42*m.x173 - 42*m.x174
                          - 42*m.x175 - 42*m.x176 - 42*m.x177 - 42*m.x178 - 42*m.x179 - 42*m.x180 - 42*m.x181 + m.x234
                          == 0)

m.c305 = Constraint(expr= - 2.1*m.x74 - 2.1*m.x75 - 2.1*m.x76 - 2.1*m.x77 - 2.1*m.x78 - 2.1*m.x79 - 2.1*m.x80
                          - 2.1*m.x81 - 2.1*m.x82 - 2.1*m.x83 - 2.1*m.x84 - 2.1*m.x85 - 2.1*m.x86 - 2.1*m.x87
                          - 2.1*m.x88 - 2.1*m.x89 - 2.1*m.x90 - 2.1*m.x91 - 2.1*m.x92 - 2.1*m.x93 - 2.1*m.x94
                          - 2.1*m.x95 - 2.1*m.x96 - 2.1*m.x97 - 2.1*m.x98 - 2.1*m.x99 - 2.1*m.x100 - 2.1*m.x101
                          - 2.1*m.x102 - 2.1*m.x103 - 2.1*m.x104 - 2.1*m.x105 - 2.1*m.x106 - 2.1*m.x107 - 2.1*m.x108
                          - 2.1*m.x109 - 2.1*m.x110 - 2.1*m.x111 - 2.1*m.x112 - 2.1*m.x113 - 2.1*m.x114 - 2.1*m.x115
                          - 2.1*m.x116 - 2.1*m.x117 - 2.1*m.x118 - 2.1*m.x119 - 2.1*m.x120 - 2.1*m.x121 - 18.63*m.x122
                          - 18.63*m.x123 - 18.63*m.x124 - 18.63*m.x125 - 18.63*m.x126 - 18.63*m.x127 - 18.63*m.x128
                          - 18.63*m.x129 - 18.63*m.x130 - 18.63*m.x131 - 18.63*m.x132 - 18.63*m.x133 - 18.63*m.x134
                          - 18.63*m.x135 - 18.63*m.x136 - 18.63*m.x137 - 18.63*m.x138 - 18.63*m.x139 - 18.63*m.x140
                          - 18.63*m.x141 - 18.63*m.x142 - 18.63*m.x143 - 18.63*m.x144 - 18.63*m.x145 - 11*m.x146
                          - 11*m.x147 - 11*m.x148 - 11*m.x149 - 11*m.x150 - 11*m.x151 - 11*m.x152 - 11*m.x153
                          - 11*m.x154 - 11*m.x155 - 11*m.x156 - 11*m.x157 - 15*m.x158 - 15*m.x159 - 15*m.x160
                          - 15*m.x161 - 15*m.x162 - 15*m.x163 - 15*m.x164 - 15*m.x165 - 15*m.x166 - 15*m.x167
                          - 15*m.x168 - 15*m.x169 - 30*m.x170 - 30*m.x171 - 30*m.x172 - 30*m.x173 - 30*m.x174
                          - 30*m.x175 - 30*m.x176 - 30*m.x177 - 30*m.x178 - 30*m.x179 - 30*m.x180 - 30*m.x181 + m.x233
                          == 0)

m.c306 = Constraint(expr= - 0.580146*m.x194 - 0.580146*m.x195 - 0.580146*m.x196 - 0.580146*m.x197 - 0.580146*m.x198
                          - 0.580146*m.x199 - 0.580146*m.x200 - 0.580146*m.x201 - 0.580146*m.x202 - 0.580146*m.x203
                          - 0.580146*m.x204 - 0.580146*m.x205 + m.x232 == 0)

m.c307 = Constraint(expr= - 329622.48*m.b73 + m.x231 == 1321650)

m.c308 = Constraint(expr=   m.x74 == 9171.31040135413)

m.c309 = Constraint(expr= - 150000*m.b37 - 150000*m.b38 - 150000*m.b39 - 150000*m.b40 - 150000*m.b41 - 150000*m.b42
                          - 150000*m.b43 - 150000*m.b44 - 150000*m.b45 - 150000*m.b46 - 150000*m.b47 - 150000*m.b48
                          - 150000*m.b61 - 150000*m.b62 - 150000*m.b63 - 150000*m.b64 - 150000*m.b65 - 150000*m.b66
                          - 150000*m.b67 - 150000*m.b68 - 150000*m.b69 - 150000*m.b70 - 150000*m.b71 - 150000*m.b72
                          + m.x230 == 0)
