#  MINLP written by GAMS Convert at 04/21/18 13:55:13
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        250      105        0      145        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        233      161       72        0        0        0        0        0
#  FX     11       11        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1151      626      525        0
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
m.x74 = Var(within=Reals,bounds=(40,300),initialize=40)
m.x75 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x76 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x77 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x78 = Var(within=Reals,bounds=(0,70),initialize=0)
m.x79 = Var(within=Reals,bounds=(0,80),initialize=0)
m.x80 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x81 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x82 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x83 = Var(within=Reals,bounds=(40,40),initialize=40)
m.x84 = Var(within=Reals,bounds=(50,50),initialize=50)
m.x85 = Var(within=Reals,bounds=(60,60),initialize=60)
m.x86 = Var(within=Reals,bounds=(70,70),initialize=70)
m.x87 = Var(within=Reals,bounds=(80,80),initialize=80)
m.x88 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x89 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x90 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x91 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x92 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x93 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x94 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x95 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x96 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x97 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x98 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x99 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x100 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x101 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x102 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x103 = Var(within=Reals,bounds=(0,70),initialize=0)
m.x104 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x105 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x106 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x107 = Var(within=Reals,bounds=(0,70),initialize=0)
m.x108 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x109 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x110 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x111 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x112 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x113 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x114 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x115 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x116 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x117 = Var(within=Reals,bounds=(0,70),initialize=0)
m.x118 = Var(within=Reals,bounds=(0,70),initialize=0)
m.x119 = Var(within=Reals,bounds=(0,70),initialize=0)
m.x120 = Var(within=Reals,bounds=(0,80),initialize=0)
m.x121 = Var(within=Reals,bounds=(0,80),initialize=0)
m.x122 = Var(within=Reals,bounds=(0,80),initialize=0)
m.x123 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x124 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x125 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x126 = Var(within=Reals,bounds=(0,70),initialize=0)
m.x127 = Var(within=Reals,bounds=(0,80),initialize=0)
m.x128 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x129 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x130 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x131 = Var(within=Reals,bounds=(0,70),initialize=0)
m.x132 = Var(within=Reals,bounds=(0,80),initialize=0)
m.x133 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x134 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x135 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x136 = Var(within=Reals,bounds=(0,70),initialize=0)
m.x137 = Var(within=Reals,bounds=(0,80),initialize=0)
m.x138 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x139 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x140 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x141 = Var(within=Reals,bounds=(0,70),initialize=0)
m.x142 = Var(within=Reals,bounds=(0,80),initialize=0)
m.x143 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x144 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x145 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x146 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x147 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x148 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x149 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x150 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x151 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x152 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x153 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x154 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x155 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x156 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x157 = Var(within=Reals,bounds=(0,300),initialize=0)
m.x158 = Var(within=Reals,bounds=(40,300),initialize=40)
m.x159 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x160 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x161 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x162 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x163 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x164 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x165 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x166 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x167 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x168 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x169 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x170 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x171 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x172 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x173 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x174 = Var(within=Reals,bounds=(25,25),initialize=25)
m.x175 = Var(within=Reals,bounds=(37.5,37.5),initialize=37.5)
m.x176 = Var(within=Reals,bounds=(25,25),initialize=25)
m.x177 = Var(within=Reals,bounds=(20,70),initialize=20)
m.x178 = Var(within=Reals,bounds=(20,70),initialize=20)
m.x179 = Var(within=Reals,bounds=(20,70),initialize=20)
m.x180 = Var(within=Reals,bounds=(16.6666666666667,66.6666666666667),initialize=16.6666666666667)
m.x181 = Var(within=Reals,bounds=(16.6666666666667,66.6666666666667),initialize=16.6666666666667)
m.x182 = Var(within=Reals,bounds=(16.6666666666667,66.6666666666667),initialize=16.6666666666667)
m.x183 = Var(within=Reals,bounds=(28.5714285714286,78.5714285714286),initialize=28.5714285714286)
m.x184 = Var(within=Reals,bounds=(28.5714285714286,78.5714285714286),initialize=28.5714285714286)
m.x185 = Var(within=Reals,bounds=(28.5714285714286,78.5714285714286),initialize=28.5714285714286)
m.x186 = Var(within=Reals,bounds=(12.5,37.5),initialize=12.5)
m.x187 = Var(within=Reals,bounds=(12.5,37.5),initialize=12.5)
m.x188 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x189 = Var(within=Reals,bounds=(0,78.5714285714286),initialize=0)
m.x190 = Var(within=Reals,bounds=(0,78.5714285714286),initialize=0)
m.x191 = Var(within=Reals,bounds=(0,78.5714285714286),initialize=0)
m.x192 = Var(within=Reals,bounds=(0,78.5714285714286),initialize=0)
m.x193 = Var(within=Reals,bounds=(0,78.5714285714286),initialize=0)
m.x194 = Var(within=Reals,bounds=(0,78.5714285714286),initialize=0)
m.x195 = Var(within=Reals,bounds=(0,78.5714285714286),initialize=0)
m.x196 = Var(within=Reals,bounds=(0,78.5714285714286),initialize=0)
m.x197 = Var(within=Reals,bounds=(0,78.5714285714286),initialize=0)
m.x198 = Var(within=Reals,bounds=(0,3.92857142857142),initialize=0)
m.x199 = Var(within=Reals,bounds=(0,78.5714285714286),initialize=0)
m.x200 = Var(within=Reals,bounds=(0,78.5714285714286),initialize=0)
m.x201 = Var(within=Reals,bounds=(0,78.5714285714286),initialize=0)
m.x202 = Var(within=Reals,bounds=(0,78.5714285714286),initialize=0)
m.x203 = Var(within=Reals,bounds=(0,3.92857142857142),initialize=0)
m.x204 = Var(within=Reals,bounds=(0,78.5714285714286),initialize=0)
m.x205 = Var(within=Reals,bounds=(0,3.92857142857142),initialize=0)
m.x206 = Var(within=Reals,bounds=(0,78.5714285714286),initialize=0)
m.x207 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x208 = Var(within=Reals,bounds=(0,37.5),initialize=0)
m.x209 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x210 = Var(within=Reals,bounds=(0,70),initialize=0)
m.x211 = Var(within=Reals,bounds=(0,70),initialize=0)
m.x212 = Var(within=Reals,bounds=(0,70),initialize=0)
m.x213 = Var(within=Reals,bounds=(0,66.6666666666667),initialize=0)
m.x214 = Var(within=Reals,bounds=(0,66.6666666666667),initialize=0)
m.x215 = Var(within=Reals,bounds=(0,66.6666666666667),initialize=0)
m.x216 = Var(within=Reals,bounds=(0,78.5714285714286),initialize=0)
m.x217 = Var(within=Reals,bounds=(0,78.5714285714286),initialize=0)
m.x218 = Var(within=Reals,bounds=(0,78.5714285714286),initialize=0)
m.x219 = Var(within=Reals,bounds=(0,37.5),initialize=0)
m.x220 = Var(within=Reals,bounds=(0,37.5),initialize=0)
m.x221 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x222 = Var(within=Reals,bounds=(0,3.92857142857142),initialize=0)
m.x223 = Var(within=Reals,bounds=(0,78.5714285714286),initialize=0)
m.x224 = Var(within=Reals,bounds=(0,78.5714285714286),initialize=0)
m.x225 = Var(within=Reals,bounds=(0,78.5714285714286),initialize=0)
m.x226 = Var(within=Reals,bounds=(0,78.5714285714286),initialize=0)
m.x227 = Var(within=Reals,bounds=(0,3.92857142857142),initialize=0)
m.x228 = Var(within=Reals,bounds=(0,78.5714285714286),initialize=0)
m.x229 = Var(within=Reals,bounds=(0,3.92857142857142),initialize=0)
m.x230 = Var(within=Reals,bounds=(0,78.5714285714286),initialize=0)
m.x231 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x232 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x233 = Var(within=Reals,bounds=(0,10),initialize=0)

m.obj = Objective(expr=0.1*(16800*(0.001 + m.x155)**0.7 + 9500*(0.001 + m.x156)**0.7 + 12600*(0.001 + m.x157)**0.7) + 
                       8000*m.x155 + 320*m.x156 + 53.6*m.x157 + 0.1*(100*(0.001 + m.x75)**0.6 + 100*(0.001 + m.x76)**0.6
                        + 100*(0.001 + m.x77)**0.6 + 100*(0.001 + m.x78)**0.6 + 100*(0.001 + m.x79)**0.6 + 100*(0.001 + 
                       m.x80)**0.6 + 100*(0.001 + m.x81)**0.6 + 100*(0.001 + m.x82)**0.6 + 100*(0.001 + m.x88)**0.6 + 
                       100*(0.001 + m.x89)**0.6 + 100*(0.001 + m.x90)**0.6 + 100*(0.001 + m.x91)**0.6 + 100*(0.001 + 
                       m.x92)**0.6 + 100*(0.001 + m.x93)**0.6 + 100*(0.001 + m.x94)**0.6 + 100*(0.001 + m.x95)**0.6 + 
                       100*(0.001 + m.x96)**0.6 + 100*(0.001 + m.x97)**0.6 + 100*(0.001 + m.x98)**0.6 + 100*(0.001 + 
                       m.x99)**0.6 + 100*(0.001 + m.x100)**0.6 + 100*(0.001 + m.x101)**0.6 + 100*(0.001 + m.x102)**0.6
                        + 100*(0.001 + m.x103)**0.6 + 100*(0.001 + m.x104)**0.6 + 100*(0.001 + m.x105)**0.6 + 100*(0.001
                        + m.x106)**0.6 + 100*(0.001 + m.x107)**0.6 + 100*(0.001 + m.x108)**0.6 + 100*(0.001 + m.x109)**
                       0.6 + 100*(0.001 + m.x110)**0.6 + 100*(0.001 + m.x111)**0.6 + 100*(0.001 + m.x112)**0.6 + 100*(
                       0.001 + m.x113)**0.6 + 100*(0.001 + m.x114)**0.6 + 100*(0.001 + m.x115)**0.6 + 100*(0.001 + 
                       m.x116)**0.6 + 100*(0.001 + m.x117)**0.6 + 100*(0.001 + m.x118)**0.6 + 100*(0.001 + m.x119)**0.6
                        + 100*(0.001 + m.x120)**0.6 + 100*(0.001 + m.x121)**0.6 + 100*(0.001 + m.x122)**0.6 + 100*(0.001
                        + m.x123)**0.6 + 100*(0.001 + m.x124)**0.6 + 100*(0.001 + m.x125)**0.6 + 100*(0.001 + m.x126)**
                       0.6 + 100*(0.001 + m.x127)**0.6 + 100*(0.001 + m.x128)**0.6 + 100*(0.001 + m.x129)**0.6 + 100*(
                       0.001 + m.x130)**0.6 + 100*(0.001 + m.x131)**0.6 + 100*(0.001 + m.x132)**0.6 + 100*(0.001 + 
                       m.x133)**0.6 + 100*(0.001 + m.x134)**0.6 + 100*(0.001 + m.x135)**0.6 + 100*(0.001 + m.x136)**0.6
                        + 100*(0.001 + m.x137)**0.6 + 100*(0.001 + m.x138)**0.6 + 100*(0.001 + m.x139)**0.6 + 100*(0.001
                        + m.x140)**0.6 + 100*(0.001 + m.x141)**0.6 + 100*(0.001 + m.x142)**0.6 + 100*(0.001 + m.x149)**
                       0.6 + 100*(0.001 + m.x150)**0.6 + 100*(0.001 + m.x151)**0.6 + 100*(0.001 + m.x143)**0.6 + 100*(
                       0.001 + m.x144)**0.6 + 100*(0.001 + m.x145)**0.6 + 100*(0.001 + m.x146)**0.6 + 100*(0.001 + 
                       m.x147)**0.6 + 100*(0.001 + m.x148)**0.6) + 48*m.x75 + 48*m.x76 + 48*m.x77 + 48*m.x78 + 48*m.x79
                        + 48*m.x80 + 48*m.x81 + 48*m.x82 + 48*m.x88 + 48*m.x89 + 48*m.x90 + 48*m.x91 + 48*m.x92 + 48*
                       m.x93 + 48*m.x94 + 48*m.x95 + 48*m.x96 + 48*m.x97 + 48*m.x98 + 48*m.x99 + 48*m.x100 + 48*m.x101
                        + 48*m.x102 + 48*m.x103 + 48*m.x104 + 48*m.x105 + 48*m.x106 + 48*m.x107 + 48*m.x108 + 48*m.x109
                        + 48*m.x110 + 48*m.x111 + 48*m.x112 + 48*m.x113 + 48*m.x114 + 48*m.x115 + 48*m.x116 + 48*m.x117
                        + 48*m.x118 + 48*m.x119 + 48*m.x120 + 48*m.x121 + 48*m.x122 + 48*m.x123 + 48*m.x124 + 48*m.x125
                        + 48*m.x126 + 48*m.x127 + 48*m.x128 + 48*m.x129 + 48*m.x130 + 48*m.x131 + 48*m.x132 + 48*m.x133
                        + 48*m.x134 + 48*m.x135 + 48*m.x136 + 48*m.x137 + 48*m.x138 + 48*m.x139 + 48*m.x140 + 48*m.x141
                        + 48*m.x142 + 48*m.x143 + 48*m.x144 + 48*m.x145 + 48*m.x146 + 48*m.x147 + 48*m.x148 + 48*m.x149
                        + 48*m.x150 + 48*m.x151 + 0.6*m.b1 + 0.6*m.b2 + 0.6*m.b3 + 0.6*m.b4 + 0.6*m.b5 + 0.6*m.b6
                        + 0.6*m.b7 + 0.6*m.b8 + 0.6*m.b9 + 0.6*m.b10 + 0.6*m.b11 + 0.6*m.b12 + 0.6*m.b13 + 0.6*m.b14
                        + 0.6*m.b15 + 0.6*m.b16 + 0.6*m.b17 + 0.6*m.b18 + 0.6*m.b19 + 0.6*m.b20 + 0.6*m.b21 + 0.6*m.b22
                        + 0.6*m.b23 + 0.6*m.b24 + 0.6*m.b25 + 0.6*m.b26 + 0.6*m.b27 + 0.6*m.b28 + 0.6*m.b29 + 0.6*m.b30
                        + 0.6*m.b31 + 0.6*m.b32 + 0.6*m.b33 + 0.6*m.b34 + 0.6*m.b35 + 0.6*m.b36 + 0.6*m.b37 + 0.6*m.b38
                        + 0.6*m.b39 + 0.6*m.b40 + 0.6*m.b41 + 0.6*m.b42 + 0.6*m.b43 + 0.6*m.b44 + 0.6*m.b45 + 0.6*m.b46
                        + 0.6*m.b47 + 0.6*m.b48 + 0.6*m.b49 + 0.6*m.b50 + 0.6*m.b51 + 0.6*m.b52 + 0.6*m.b53 + 0.6*m.b54
                        + 0.6*m.b55 + 0.6*m.b56 + 0.6*m.b57 + 0.6*m.b58 + 0.6*m.b59 + 0.6*m.b60 + 0.6*m.b61 + 0.6*m.b62
                        + 0.6*m.b63 + 0.6*m.b64 + 0.6*m.b65 + 0.6*m.b66 + 0.6*m.b67 + 0.6*m.b68 + 0.6*m.b69 + 0.6*m.b70
                        + 0.6*m.b71 + 0.6*m.b72 + 8000*m.x74, sense=minimize)

m.c2 = Constraint(expr=   m.x74 - m.x75 - m.x76 - m.x77 - m.x78 - m.x79 - m.x80 - m.x81 - m.x82 == 0)

m.c3 = Constraint(expr= - m.x75 - m.x92 - m.x96 - m.x100 - m.x104 - m.x128 - m.x133 - m.x138 == -40)

m.c4 = Constraint(expr= - m.x76 - m.x88 - m.x97 - m.x101 - m.x105 - m.x129 - m.x134 - m.x139 == -50)

m.c5 = Constraint(expr= - m.x77 - m.x89 - m.x93 - m.x102 - m.x106 - m.x130 - m.x135 - m.x140 == -60)

m.c6 = Constraint(expr= - m.x78 - m.x90 - m.x94 - m.x98 - m.x107 - m.x131 - m.x136 - m.x141 == -70)

m.c7 = Constraint(expr= - m.x79 - m.x91 - m.x95 - m.x99 - m.x103 - m.x132 - m.x137 - m.x142 == -80)

m.c8 = Constraint(expr=-(m.x92*m.x177 + m.x96*m.x180 + m.x100*m.x183 + m.x104*m.x186 + m.x128*m.x198 + m.x133*m.x201 + 
                       m.x138*m.x204) + 40*m.x159 == 0)

m.c9 = Constraint(expr=-(m.x92*m.x178 + m.x96*m.x181 + m.x100*m.x184 + m.x104*m.x187 + m.x128*m.x199 + m.x133*m.x202 + 
                       m.x138*m.x205) + 40*m.x160 == 0)

m.c10 = Constraint(expr=-(m.x92*m.x179 + m.x96*m.x182 + m.x100*m.x185 + m.x104*m.x188 + m.x128*m.x200 + m.x133*m.x203 + 
                        m.x138*m.x206) + 40*m.x161 == 0)

m.c11 = Constraint(expr=-(m.x88*m.x174 + m.x97*m.x180 + m.x101*m.x183 + m.x105*m.x186 + m.x129*m.x198 + m.x134*m.x201 + 
                        m.x139*m.x204) + 50*m.x162 == 0)

m.c12 = Constraint(expr=-(m.x88*m.x175 + m.x97*m.x181 + m.x101*m.x184 + m.x105*m.x187 + m.x129*m.x199 + m.x134*m.x202 + 
                        m.x139*m.x205) + 50*m.x163 == 0)

m.c13 = Constraint(expr=-(m.x88*m.x176 + m.x97*m.x182 + m.x101*m.x185 + m.x105*m.x188 + m.x129*m.x200 + m.x134*m.x203 + 
                        m.x139*m.x206) + 50*m.x164 == 0)

m.c14 = Constraint(expr=-(m.x89*m.x174 + m.x93*m.x177 + m.x102*m.x183 + m.x106*m.x186 + m.x130*m.x198 + m.x135*m.x201 + 
                        m.x140*m.x204) + 60*m.x165 == 0)

m.c15 = Constraint(expr=-(m.x89*m.x175 + m.x93*m.x178 + m.x102*m.x184 + m.x106*m.x187 + m.x130*m.x199 + m.x135*m.x202 + 
                        m.x140*m.x205) + 60*m.x166 == 0)

m.c16 = Constraint(expr=-(m.x89*m.x176 + m.x93*m.x179 + m.x102*m.x185 + m.x106*m.x188 + m.x130*m.x200 + m.x135*m.x203 + 
                        m.x140*m.x206) + 60*m.x167 == 0)

m.c17 = Constraint(expr=-(m.x90*m.x174 + m.x94*m.x177 + m.x98*m.x180 + m.x107*m.x186 + m.x131*m.x198 + m.x136*m.x201 + 
                        m.x141*m.x204) + 70*m.x168 == 0)

m.c18 = Constraint(expr=-(m.x90*m.x175 + m.x94*m.x178 + m.x98*m.x181 + m.x107*m.x187 + m.x131*m.x199 + m.x136*m.x202 + 
                        m.x141*m.x205) + 70*m.x169 == 0)

m.c19 = Constraint(expr=-(m.x90*m.x176 + m.x94*m.x179 + m.x98*m.x182 + m.x107*m.x188 + m.x131*m.x200 + m.x136*m.x203 + 
                        m.x141*m.x206) + 70*m.x170 == 0)

m.c20 = Constraint(expr=-(m.x91*m.x174 + m.x95*m.x177 + m.x99*m.x180 + m.x103*m.x183 + m.x132*m.x198 + m.x137*m.x201 + 
                        m.x142*m.x204) + 80*m.x171 == 0)

m.c21 = Constraint(expr=-(m.x91*m.x175 + m.x95*m.x178 + m.x99*m.x181 + m.x103*m.x184 + m.x132*m.x199 + m.x137*m.x202 + 
                        m.x142*m.x205) + 80*m.x172 == 0)

m.c22 = Constraint(expr=-(m.x91*m.x176 + m.x95*m.x179 + m.x99*m.x182 + m.x103*m.x185 + m.x132*m.x200 + m.x137*m.x203 + 
                        m.x142*m.x206) + 80*m.x173 == 0)

m.c23 = Constraint(expr= - m.x83 == -40)

m.c24 = Constraint(expr= - m.x84 == -50)

m.c25 = Constraint(expr= - m.x85 == -60)

m.c26 = Constraint(expr= - m.x86 == -70)

m.c27 = Constraint(expr= - m.x87 == -80)

m.c28 = Constraint(expr=-m.x83*m.x174 + 40*m.x159 == -1000)

m.c29 = Constraint(expr=-m.x83*m.x175 + 40*m.x160 == -1500)

m.c30 = Constraint(expr=-m.x83*m.x176 + 40*m.x161 == -1000)

m.c31 = Constraint(expr=-m.x84*m.x177 + 50*m.x162 == -1000)

m.c32 = Constraint(expr=-m.x84*m.x178 + 50*m.x163 == -1000)

m.c33 = Constraint(expr=-m.x84*m.x179 + 50*m.x164 == -1000)

m.c34 = Constraint(expr=-m.x85*m.x180 + 60*m.x165 == -1000)

m.c35 = Constraint(expr=-m.x85*m.x181 + 60*m.x166 == -1000)

m.c36 = Constraint(expr=-m.x85*m.x182 + 60*m.x167 == -1000)

m.c37 = Constraint(expr=-m.x86*m.x183 + 70*m.x168 == -2000)

m.c38 = Constraint(expr=-m.x86*m.x184 + 70*m.x169 == -2000)

m.c39 = Constraint(expr=-m.x86*m.x185 + 70*m.x170 == -2000)

m.c40 = Constraint(expr=-m.x87*m.x186 + 80*m.x171 == -1000)

m.c41 = Constraint(expr=-m.x87*m.x187 + 80*m.x172 == -1000)

m.c42 = Constraint(expr=-m.x87*m.x188 + 80*m.x173 == 0)

m.c43 = Constraint(expr=   m.x83 - m.x88 - m.x89 - m.x90 - m.x91 - m.x108 - m.x109 - m.x110 - m.x123 == 0)

m.c44 = Constraint(expr=   m.x84 - m.x92 - m.x93 - m.x94 - m.x95 - m.x111 - m.x112 - m.x113 - m.x124 == 0)

m.c45 = Constraint(expr=   m.x85 - m.x96 - m.x97 - m.x98 - m.x99 - m.x114 - m.x115 - m.x116 - m.x125 == 0)

m.c46 = Constraint(expr=   m.x86 - m.x100 - m.x101 - m.x102 - m.x103 - m.x117 - m.x118 - m.x119 - m.x126 == 0)

m.c47 = Constraint(expr=   m.x87 - m.x104 - m.x105 - m.x106 - m.x107 - m.x120 - m.x121 - m.x122 - m.x127 == 0)

m.c48 = Constraint(expr= - m.x174 + m.x207 == 0)

m.c49 = Constraint(expr= - m.x175 + m.x208 == 0)

m.c50 = Constraint(expr= - m.x176 + m.x209 == 0)

m.c51 = Constraint(expr= - m.x177 + m.x210 == 0)

m.c52 = Constraint(expr= - m.x178 + m.x211 == 0)

m.c53 = Constraint(expr= - m.x179 + m.x212 == 0)

m.c54 = Constraint(expr= - m.x180 + m.x213 == 0)

m.c55 = Constraint(expr= - m.x181 + m.x214 == 0)

m.c56 = Constraint(expr= - m.x182 + m.x215 == 0)

m.c57 = Constraint(expr= - m.x183 + m.x216 == 0)

m.c58 = Constraint(expr= - m.x184 + m.x217 == 0)

m.c59 = Constraint(expr= - m.x185 + m.x218 == 0)

m.c60 = Constraint(expr= - m.x186 + m.x219 == 0)

m.c61 = Constraint(expr= - m.x187 + m.x220 == 0)

m.c62 = Constraint(expr= - m.x188 + m.x221 == 0)

m.c63 = Constraint(expr= - m.x80 - m.x108 - m.x111 - m.x114 - m.x117 - m.x120 - m.x145 - m.x147 + m.x152 == 0)

m.c64 = Constraint(expr= - m.x81 - m.x109 - m.x112 - m.x115 - m.x118 - m.x121 - m.x143 - m.x148 + m.x153 == 0)

m.c65 = Constraint(expr= - m.x82 - m.x110 - m.x113 - m.x116 - m.x119 - m.x122 - m.x144 - m.x146 + m.x154 == 0)

m.c66 = Constraint(expr=m.x152*m.x189 - (m.x145*m.x225 + m.x147*m.x228 + m.x108*m.x207 + m.x111*m.x210 + m.x114*m.x213
                         + m.x117*m.x216 + m.x120*m.x219) == 0)

m.c67 = Constraint(expr=m.x152*m.x190 - (m.x145*m.x226 + m.x147*m.x229 + m.x108*m.x208 + m.x111*m.x211 + m.x114*m.x214
                         + m.x117*m.x217 + m.x120*m.x220) == 0)

m.c68 = Constraint(expr=m.x152*m.x191 - (m.x145*m.x227 + m.x147*m.x230 + m.x108*m.x209 + m.x111*m.x212 + m.x114*m.x215
                         + m.x117*m.x218 + m.x120*m.x221) == 0)

m.c69 = Constraint(expr=m.x153*m.x192 - (m.x143*m.x222 + m.x148*m.x228 + m.x109*m.x207 + m.x112*m.x210 + m.x115*m.x213
                         + m.x118*m.x216 + m.x121*m.x219) == 0)

m.c70 = Constraint(expr=m.x153*m.x193 - (m.x143*m.x223 + m.x148*m.x229 + m.x109*m.x208 + m.x112*m.x211 + m.x115*m.x214
                         + m.x118*m.x217 + m.x121*m.x220) == 0)

m.c71 = Constraint(expr=m.x153*m.x194 - (m.x143*m.x224 + m.x148*m.x230 + m.x109*m.x209 + m.x112*m.x212 + m.x115*m.x215
                         + m.x118*m.x218 + m.x121*m.x221) == 0)

m.c72 = Constraint(expr=m.x154*m.x195 - (m.x144*m.x222 + m.x146*m.x225 + m.x110*m.x207 + m.x113*m.x210 + m.x116*m.x213
                         + m.x119*m.x216 + m.x122*m.x219) == 0)

m.c73 = Constraint(expr=m.x154*m.x196 - (m.x144*m.x223 + m.x146*m.x226 + m.x110*m.x208 + m.x113*m.x211 + m.x116*m.x214
                         + m.x119*m.x217 + m.x122*m.x220) == 0)

m.c74 = Constraint(expr=m.x154*m.x197 - (m.x144*m.x224 + m.x146*m.x227 + m.x110*m.x209 + m.x113*m.x212 + m.x116*m.x215
                         + m.x119*m.x218 + m.x122*m.x221) == 0)

m.c75 = Constraint(expr=   m.x152 - m.x155 == 0)

m.c76 = Constraint(expr=   m.x153 - m.x156 == 0)

m.c77 = Constraint(expr=   m.x154 - m.x157 == 0)

m.c78 = Constraint(expr= - 0.0499999999999999*m.x189 + m.x198 == 0)

m.c79 = Constraint(expr= - m.x190 + m.x199 == 0)

m.c80 = Constraint(expr= - m.x191 + m.x200 == 0)

m.c81 = Constraint(expr= - m.x192 + m.x201 == 0)

m.c82 = Constraint(expr= - m.x193 + m.x202 == 0)

m.c83 = Constraint(expr= - 0.0499999999999999*m.x194 + m.x203 == 0)

m.c84 = Constraint(expr= - m.x195 + m.x204 == 0)

m.c85 = Constraint(expr= - 0.0499999999999999*m.x196 + m.x205 == 0)

m.c86 = Constraint(expr= - m.x197 + m.x206 == 0)

m.c87 = Constraint(expr= - m.x128 - m.x129 - m.x130 - m.x131 - m.x132 - m.x143 - m.x144 - m.x149 + m.x155 == 0)

m.c88 = Constraint(expr= - m.x133 - m.x134 - m.x135 - m.x136 - m.x137 - m.x145 - m.x146 - m.x150 + m.x156 == 0)

m.c89 = Constraint(expr= - m.x138 - m.x139 - m.x140 - m.x141 - m.x142 - m.x147 - m.x148 - m.x151 + m.x157 == 0)

m.c90 = Constraint(expr= - m.x198 + m.x222 == 0)

m.c91 = Constraint(expr= - m.x199 + m.x223 == 0)

m.c92 = Constraint(expr= - m.x200 + m.x224 == 0)

m.c93 = Constraint(expr= - m.x201 + m.x225 == 0)

m.c94 = Constraint(expr= - m.x202 + m.x226 == 0)

m.c95 = Constraint(expr= - m.x203 + m.x227 == 0)

m.c96 = Constraint(expr= - m.x204 + m.x228 == 0)

m.c97 = Constraint(expr= - m.x205 + m.x229 == 0)

m.c98 = Constraint(expr= - m.x206 + m.x230 == 0)

m.c99 = Constraint(expr= - m.x123 - m.x124 - m.x125 - m.x126 - m.x127 - m.x149 - m.x150 - m.x151 + m.x158 == 0)

m.c100 = Constraint(expr=m.x158*m.x231 - (m.x123*m.x207 + m.x124*m.x210 + m.x125*m.x213 + m.x126*m.x216 + m.x127*m.x219
                          + m.x149*m.x222 + m.x150*m.x225 + m.x151*m.x228) == 0)

m.c101 = Constraint(expr=m.x158*m.x232 - (m.x123*m.x208 + m.x124*m.x211 + m.x125*m.x214 + m.x126*m.x217 + m.x127*m.x220
                          + m.x149*m.x223 + m.x150*m.x226 + m.x151*m.x229) == 0)

m.c102 = Constraint(expr=m.x158*m.x233 - (m.x123*m.x209 + m.x124*m.x212 + m.x125*m.x215 + m.x126*m.x218 + m.x127*m.x221
                          + m.x149*m.x224 + m.x150*m.x227 + m.x151*m.x230) == 0)

m.c103 = Constraint(expr=-(0.95*m.x152*m.x189 + m.x158*m.x231) == -6000)

m.c104 = Constraint(expr=-(0.95*m.x154*m.x196 + m.x158*m.x232) == -6500)

m.c105 = Constraint(expr=-(0.95*m.x153*m.x194 + m.x158*m.x233) == -5000)

m.c106 = Constraint(expr= - 40*m.b58 + m.x128 <= 0)

m.c107 = Constraint(expr= - 50*m.b59 + m.x129 <= 0)

m.c108 = Constraint(expr= - 60*m.b60 + m.x130 <= 0)

m.c109 = Constraint(expr= - 70*m.b61 + m.x131 <= 0)

m.c110 = Constraint(expr= - 80*m.b62 + m.x132 <= 0)

m.c111 = Constraint(expr= - 40*m.b63 + m.x133 <= 0)

m.c112 = Constraint(expr= - 50*m.b64 + m.x134 <= 0)

m.c113 = Constraint(expr= - 60*m.b65 + m.x135 <= 0)

m.c114 = Constraint(expr= - 70*m.b66 + m.x136 <= 0)

m.c115 = Constraint(expr= - 80*m.b67 + m.x137 <= 0)

m.c116 = Constraint(expr= - 40*m.b68 + m.x138 <= 0)

m.c117 = Constraint(expr= - 50*m.b69 + m.x139 <= 0)

m.c118 = Constraint(expr= - 60*m.b70 + m.x140 <= 0)

m.c119 = Constraint(expr= - 70*m.b71 + m.x141 <= 0)

m.c120 = Constraint(expr= - 80*m.b72 + m.x142 <= 0)

m.c121 = Constraint(expr= - m.x128 <= 0)

m.c122 = Constraint(expr= - m.x129 <= 0)

m.c123 = Constraint(expr= - m.x130 <= 0)

m.c124 = Constraint(expr= - m.x131 <= 0)

m.c125 = Constraint(expr= - m.x132 <= 0)

m.c126 = Constraint(expr= - m.x133 <= 0)

m.c127 = Constraint(expr= - m.x134 <= 0)

m.c128 = Constraint(expr= - m.x135 <= 0)

m.c129 = Constraint(expr= - m.x136 <= 0)

m.c130 = Constraint(expr= - m.x137 <= 0)

m.c131 = Constraint(expr= - m.x138 <= 0)

m.c132 = Constraint(expr= - m.x139 <= 0)

m.c133 = Constraint(expr= - m.x140 <= 0)

m.c134 = Constraint(expr= - m.x141 <= 0)

m.c135 = Constraint(expr= - m.x142 <= 0)

m.c136 = Constraint(expr= - 40*m.b9 + m.x88 <= 0)

m.c137 = Constraint(expr= - 40*m.b10 + m.x89 <= 0)

m.c138 = Constraint(expr= - 40*m.b11 + m.x90 <= 0)

m.c139 = Constraint(expr= - 40*m.b12 + m.x91 <= 0)

m.c140 = Constraint(expr= - 40*m.b13 + m.x92 <= 0)

m.c141 = Constraint(expr= - 50*m.b14 + m.x93 <= 0)

m.c142 = Constraint(expr= - 50*m.b15 + m.x94 <= 0)

m.c143 = Constraint(expr= - 50*m.b16 + m.x95 <= 0)

m.c144 = Constraint(expr= - 40*m.b17 + m.x96 <= 0)

m.c145 = Constraint(expr= - 50*m.b18 + m.x97 <= 0)

m.c146 = Constraint(expr= - 60*m.b19 + m.x98 <= 0)

m.c147 = Constraint(expr= - 60*m.b20 + m.x99 <= 0)

m.c148 = Constraint(expr= - 40*m.b21 + m.x100 <= 0)

m.c149 = Constraint(expr= - 50*m.b22 + m.x101 <= 0)

m.c150 = Constraint(expr= - 60*m.b23 + m.x102 <= 0)

m.c151 = Constraint(expr= - 70*m.b24 + m.x103 <= 0)

m.c152 = Constraint(expr= - 40*m.b25 + m.x104 <= 0)

m.c153 = Constraint(expr= - 50*m.b26 + m.x105 <= 0)

m.c154 = Constraint(expr= - 60*m.b27 + m.x106 <= 0)

m.c155 = Constraint(expr= - 70*m.b28 + m.x107 <= 0)

m.c156 = Constraint(expr= - m.x88 <= 0)

m.c157 = Constraint(expr= - m.x89 <= 0)

m.c158 = Constraint(expr= - m.x90 <= 0)

m.c159 = Constraint(expr= - m.x91 <= 0)

m.c160 = Constraint(expr= - m.x92 <= 0)

m.c161 = Constraint(expr= - m.x93 <= 0)

m.c162 = Constraint(expr= - m.x94 <= 0)

m.c163 = Constraint(expr= - m.x95 <= 0)

m.c164 = Constraint(expr= - m.x96 <= 0)

m.c165 = Constraint(expr= - m.x97 <= 0)

m.c166 = Constraint(expr= - m.x98 <= 0)

m.c167 = Constraint(expr= - m.x99 <= 0)

m.c168 = Constraint(expr= - m.x100 <= 0)

m.c169 = Constraint(expr= - m.x101 <= 0)

m.c170 = Constraint(expr= - m.x102 <= 0)

m.c171 = Constraint(expr= - m.x103 <= 0)

m.c172 = Constraint(expr= - m.x104 <= 0)

m.c173 = Constraint(expr= - m.x105 <= 0)

m.c174 = Constraint(expr= - m.x106 <= 0)

m.c175 = Constraint(expr= - m.x107 <= 0)

m.c176 = Constraint(expr= - 40*m.b29 + m.x108 <= 0)

m.c177 = Constraint(expr= - 40*m.b30 + m.x109 <= 0)

m.c178 = Constraint(expr= - 40*m.b31 + m.x110 <= 0)

m.c179 = Constraint(expr= - 50*m.b32 + m.x111 <= 0)

m.c180 = Constraint(expr= - 50*m.b33 + m.x112 <= 0)

m.c181 = Constraint(expr= - 50*m.b34 + m.x113 <= 0)

m.c182 = Constraint(expr= - 60*m.b35 + m.x114 <= 0)

m.c183 = Constraint(expr= - 60*m.b36 + m.x115 <= 0)

m.c184 = Constraint(expr= - 60*m.b37 + m.x116 <= 0)

m.c185 = Constraint(expr= - 70*m.b38 + m.x117 <= 0)

m.c186 = Constraint(expr= - 70*m.b39 + m.x118 <= 0)

m.c187 = Constraint(expr= - 70*m.b40 + m.x119 <= 0)

m.c188 = Constraint(expr= - 80*m.b41 + m.x120 <= 0)

m.c189 = Constraint(expr= - 80*m.b42 + m.x121 <= 0)

m.c190 = Constraint(expr= - 80*m.b43 + m.x122 <= 0)

m.c191 = Constraint(expr= - m.x108 <= 0)

m.c192 = Constraint(expr= - m.x109 <= 0)

m.c193 = Constraint(expr= - m.x110 <= 0)

m.c194 = Constraint(expr= - m.x111 <= 0)

m.c195 = Constraint(expr= - m.x112 <= 0)

m.c196 = Constraint(expr= - m.x113 <= 0)

m.c197 = Constraint(expr= - m.x114 <= 0)

m.c198 = Constraint(expr= - m.x115 <= 0)

m.c199 = Constraint(expr= - m.x116 <= 0)

m.c200 = Constraint(expr= - m.x117 <= 0)

m.c201 = Constraint(expr= - m.x118 <= 0)

m.c202 = Constraint(expr= - m.x119 <= 0)

m.c203 = Constraint(expr= - m.x120 <= 0)

m.c204 = Constraint(expr= - m.x121 <= 0)

m.c205 = Constraint(expr= - m.x122 <= 0)

m.c206 = Constraint(expr= - 40*m.b44 + m.x123 <= 0)

m.c207 = Constraint(expr= - 50*m.b45 + m.x124 <= 0)

m.c208 = Constraint(expr= - 60*m.b46 + m.x125 <= 0)

m.c209 = Constraint(expr= - 70*m.b47 + m.x126 <= 0)

m.c210 = Constraint(expr= - 80*m.b48 + m.x127 <= 0)

m.c211 = Constraint(expr= - m.x123 <= 0)

m.c212 = Constraint(expr= - m.x124 <= 0)

m.c213 = Constraint(expr= - m.x125 <= 0)

m.c214 = Constraint(expr= - m.x126 <= 0)

m.c215 = Constraint(expr= - m.x127 <= 0)

m.c216 = Constraint(expr= - 300*m.b49 + m.x149 <= 0)

m.c217 = Constraint(expr= - 300*m.b50 + m.x150 <= 0)

m.c218 = Constraint(expr= - 300*m.b51 + m.x151 <= 0)

m.c219 = Constraint(expr= - m.x149 <= 0)

m.c220 = Constraint(expr= - m.x150 <= 0)

m.c221 = Constraint(expr= - m.x151 <= 0)

m.c222 = Constraint(expr= - 300*m.b52 + m.x143 <= 0)

m.c223 = Constraint(expr= - 300*m.b53 + m.x144 <= 0)

m.c224 = Constraint(expr= - 300*m.b54 + m.x145 <= 0)

m.c225 = Constraint(expr= - 300*m.b55 + m.x146 <= 0)

m.c226 = Constraint(expr= - 300*m.b56 + m.x147 <= 0)

m.c227 = Constraint(expr= - 300*m.b57 + m.x148 <= 0)

m.c228 = Constraint(expr= - m.x143 <= 0)

m.c229 = Constraint(expr= - m.x144 <= 0)

m.c230 = Constraint(expr= - m.x145 <= 0)

m.c231 = Constraint(expr= - m.x146 <= 0)

m.c232 = Constraint(expr= - m.x147 <= 0)

m.c233 = Constraint(expr= - m.x148 <= 0)

m.c234 = Constraint(expr= - 40*m.b1 + m.x75 <= 0)

m.c235 = Constraint(expr= - 50*m.b2 + m.x76 <= 0)

m.c236 = Constraint(expr= - 60*m.b3 + m.x77 <= 0)

m.c237 = Constraint(expr= - 70*m.b4 + m.x78 <= 0)

m.c238 = Constraint(expr= - 80*m.b5 + m.x79 <= 0)

m.c239 = Constraint(expr= - m.x75 <= 0)

m.c240 = Constraint(expr= - m.x76 <= 0)

m.c241 = Constraint(expr= - m.x77 <= 0)

m.c242 = Constraint(expr= - m.x78 <= 0)

m.c243 = Constraint(expr= - m.x79 <= 0)

m.c244 = Constraint(expr= - 300*m.b6 + m.x80 <= 0)

m.c245 = Constraint(expr= - 300*m.b7 + m.x81 <= 0)

m.c246 = Constraint(expr= - 300*m.b8 + m.x82 <= 0)

m.c247 = Constraint(expr= - m.x80 <= 0)

m.c248 = Constraint(expr= - m.x81 <= 0)

m.c249 = Constraint(expr= - m.x82 <= 0)

m.c250 = Constraint(expr=   m.b1 + m.b2 + m.b3 + m.b4 + m.b5 + m.b6 + m.b7 + m.b8 + m.b9 + m.b10 + m.b11 + m.b12 + m.b13
                          + m.b14 + m.b15 + m.b16 + m.b17 + m.b18 + m.b19 + m.b20 + m.b21 + m.b22 + m.b23 + m.b24
                          + m.b25 + m.b26 + m.b27 + m.b28 + m.b29 + m.b30 + m.b31 + m.b32 + m.b33 + m.b34 + m.b35
                          + m.b36 + m.b37 + m.b38 + m.b39 + m.b40 + m.b41 + m.b42 + m.b43 + m.b44 + m.b45 + m.b46
                          + m.b47 + m.b48 + m.b49 + m.b50 + m.b51 + m.b52 + m.b53 + m.b54 + m.b55 + m.b56 + m.b57
                          + m.b58 + m.b59 + m.b60 + m.b61 + m.b62 + m.b63 + m.b64 + m.b65 + m.b66 + m.b67 + m.b68
                          + m.b69 + m.b70 + m.b71 + m.b72 <= 72)
