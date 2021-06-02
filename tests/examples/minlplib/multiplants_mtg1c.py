#  MINLP written by GAMS Convert at 04/21/18 13:52:37
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        319       75      117      127        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        245      125      120        0        0        0        0        0
#  FX      1        1        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       2550     2455       95        0


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
m.b74 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b75 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b76 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b77 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b78 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b79 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b80 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b81 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b82 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b83 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b84 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b85 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b86 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b87 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b88 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b89 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b90 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b91 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b92 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b93 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b94 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b95 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b96 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b97 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b98 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b99 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b100 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b101 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b102 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b103 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b104 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b105 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b106 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b107 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b108 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b109 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b110 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b111 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b112 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b113 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b114 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b115 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b116 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b117 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b118 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b119 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b120 = Var(within=Binary,bounds=(0,1),initialize=0)
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
m.x193 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x194 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x195 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x196 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x197 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x198 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x199 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x200 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x201 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x202 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x203 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x204 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x205 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x206 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x207 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x208 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x209 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x210 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x211 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x212 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x213 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x214 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x215 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x216 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x217 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x218 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x219 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x220 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x221 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x222 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x223 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x224 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x225 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x226 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x227 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x228 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x229 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x230 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x231 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x232 = Var(within=Reals,bounds=(50,None),initialize=50)
m.x233 = Var(within=Reals,bounds=(100,None),initialize=100)
m.x234 = Var(within=Reals,bounds=(250,None),initialize=250)
m.x235 = Var(within=Reals,bounds=(0,None),initialize=800)
m.x236 = Var(within=Reals,bounds=(0,None),initialize=900)
m.x237 = Var(within=Reals,bounds=(0,None),initialize=1200)
m.x238 = Var(within=Reals,bounds=(0,None),initialize=600)
m.x239 = Var(within=Reals,bounds=(0,None),initialize=1000)
m.x240 = Var(within=Reals,bounds=(0,None),initialize=1100)
m.x241 = Var(within=Reals,bounds=(11.1111111111111,600),initialize=11.1111111111111)
m.x242 = Var(within=Reals,bounds=(33.3333333333333,600),initialize=33.3333333333333)
m.x243 = Var(within=Reals,bounds=(45.4545454545455,600),initialize=45.4545454545455)
m.x244 = Var(within=Reals,bounds=(200,600),initialize=200)
m.x245 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=m.x245, sense=maximize)

m.c1 = Constraint(expr=m.x245*m.x244 + 0.00203*(m.x241**2*(m.x236 - m.x232) + (m.x244 - m.x241)**2*m.x232) + 0.00203*(
                       m.x242**2*(m.x238 - m.x233) + (m.x244 - m.x242)**2*m.x233) + 0.00203*(m.x243**2*(m.x240 - m.x234)
                        + (m.x244 - m.x243)**2*m.x234) + 3800*m.b4 + 3800*m.b5 + 3800*m.b6 + 6080*m.b7 + 6080*m.b8
                        + 6080*m.b9 + 7500*m.b10 + 7500*m.b11 + 7500*m.b12 + 2250*m.b16 + 2250*m.b17 + 2250*m.b18
                        + 3080*m.b19 + 3080*m.b20 + 3080*m.b21 + 5390*m.b22 + 5390*m.b23 + 5390*m.b24 + 6840*m.b31
                        + 6840*m.b32 + 6840*m.b33 + 8360*m.b34 + 8360*m.b35 + 8360*m.b36 + 3750*m.b37 + 3750*m.b38
                        + 3750*m.b39 + 5250*m.b43 + 5250*m.b44 + 5250*m.b45 + 4620*m.b46 + 4620*m.b47 + 4620*m.b48
                        + 3080*m.b49 + 3080*m.b50 + 3080*m.b51 + 8360*m.b58 + 8360*m.b59 + 8360*m.b60 + 760*m.b61
                        + 760*m.b62 + 760*m.b63 + 1500*m.b64 + 1500*m.b65 + 1500*m.b66 + 3750*m.b70 + 3750*m.b71
                        + 3750*m.b72 + 4620*m.b73 + 4620*m.b74 + 4620*m.b75 + 770*m.b76 + 770*m.b77 + 770*m.b78
                        + 6840*m.b85 + 6840*m.b86 + 6840*m.b87 + 8360*m.b88 + 8360*m.b89 + 8360*m.b90 + 3750*m.b91
                        + 3750*m.b92 + 3750*m.b93 + 5250*m.b97 + 5250*m.b98 + 5250*m.b99 + 4620*m.b100 + 4620*m.b101
                        + 4620*m.b102 + 3080*m.b103 + 3080*m.b104 + 3080*m.b105 - 0.15*m.x127 - 0.15*m.x128
                        - 0.15*m.x129 - 0.15*m.x130 - 0.15*m.x131 - 0.15*m.x132 - 0.4*m.x139 - 0.4*m.x140 - 0.4*m.x141
                        - 0.4*m.x142 - 0.4*m.x143 - 0.4*m.x144 - 0.65*m.x151 - 0.65*m.x152 - 0.65*m.x153 - 0.65*m.x154
                        - 0.65*m.x155 - 0.65*m.x156 + 0.1406*m.x217 + 0.1406*m.x218 + 0.1406*m.x219 == 0)

m.c2 = Constraint(expr=   m.b1 - m.b3 + m.b4 + m.b7 - m.b12 - m.b21 + m.x157 - m.x159 == 0)

m.c3 = Constraint(expr= - m.b1 + m.b2 + m.b5 + m.b8 - m.b10 - m.b19 - m.x157 + m.x158 == 0)

m.c4 = Constraint(expr= - m.b2 + m.b3 + m.b6 + m.b9 - m.b11 - m.b20 - m.x158 + m.x159 == 0)

m.c5 = Constraint(expr= - m.b6 + m.b10 + m.b13 - m.b15 + m.b16 - m.b24 + m.x160 - m.x162 == 0)

m.c6 = Constraint(expr= - m.b4 + m.b11 - m.b13 + m.b14 + m.b17 - m.b22 - m.x160 + m.x161 == 0)

m.c7 = Constraint(expr= - m.b5 + m.b12 - m.b14 + m.b15 + m.b18 - m.b23 - m.x161 + m.x162 == 0)

m.c8 = Constraint(expr= - m.b9 - m.b18 + m.b19 + m.b22 + m.b25 - m.b27 + m.x163 - m.x165 == 0)

m.c9 = Constraint(expr= - m.b7 - m.b16 + m.b20 + m.b23 - m.b25 + m.b26 - m.x163 + m.x164 == 0)

m.c10 = Constraint(expr= - m.b8 - m.b17 + m.b21 + m.b24 - m.b26 + m.b27 - m.x164 + m.x165 == 0)

m.c11 = Constraint(expr=   m.b28 - m.b30 + m.b31 + m.b34 - m.b39 - m.b48 + m.x166 - m.x168 == 0)

m.c12 = Constraint(expr= - m.b28 + m.b29 + m.b32 + m.b35 - m.b37 - m.b46 - m.x166 + m.x167 == 0)

m.c13 = Constraint(expr= - m.b29 + m.b30 + m.b33 + m.b36 - m.b38 - m.b47 - m.x167 + m.x168 == 0)

m.c14 = Constraint(expr= - m.b33 + m.b37 + m.b40 - m.b42 + m.b43 - m.b51 + m.x169 - m.x171 == 0)

m.c15 = Constraint(expr= - m.b31 + m.b38 - m.b40 + m.b41 + m.b44 - m.b49 - m.x169 + m.x170 == 0)

m.c16 = Constraint(expr= - m.b32 + m.b39 - m.b41 + m.b42 + m.b45 - m.b50 - m.x170 + m.x171 == 0)

m.c17 = Constraint(expr= - m.b36 - m.b45 + m.b46 + m.b49 + m.b52 - m.b54 + m.x172 - m.x174 == 0)

m.c18 = Constraint(expr= - m.b34 - m.b43 + m.b47 + m.b50 - m.b52 + m.b53 - m.x172 + m.x173 == 0)

m.c19 = Constraint(expr= - m.b35 - m.b44 + m.b48 + m.b51 - m.b53 + m.b54 - m.x173 + m.x174 == 0)

m.c20 = Constraint(expr=   m.b55 - m.b57 + m.b58 + m.b61 - m.b66 - m.b75 + m.x175 - m.x177 == 0)

m.c21 = Constraint(expr= - m.b55 + m.b56 + m.b59 + m.b62 - m.b64 - m.b73 - m.x175 + m.x176 == 0)

m.c22 = Constraint(expr= - m.b56 + m.b57 + m.b60 + m.b63 - m.b65 - m.b74 - m.x176 + m.x177 == 0)

m.c23 = Constraint(expr= - m.b60 + m.b64 + m.b67 - m.b69 + m.b70 - m.b78 + m.x178 - m.x180 == 0)

m.c24 = Constraint(expr= - m.b58 + m.b65 - m.b67 + m.b68 + m.b71 - m.b76 - m.x178 + m.x179 == 0)

m.c25 = Constraint(expr= - m.b59 + m.b66 - m.b68 + m.b69 + m.b72 - m.b77 - m.x179 + m.x180 == 0)

m.c26 = Constraint(expr= - m.b63 - m.b72 + m.b73 + m.b76 + m.b79 - m.b81 + m.x181 - m.x183 == 0)

m.c27 = Constraint(expr= - m.b61 - m.b70 + m.b74 + m.b77 - m.b79 + m.b80 - m.x181 + m.x182 == 0)

m.c28 = Constraint(expr= - m.b62 - m.b71 + m.b75 + m.b78 - m.b80 + m.b81 - m.x182 + m.x183 == 0)

m.c29 = Constraint(expr=   m.b82 - m.b84 + m.b85 + m.b88 - m.b93 - m.b102 + m.x184 - m.x186 == 0)

m.c30 = Constraint(expr= - m.b82 + m.b83 + m.b86 + m.b89 - m.b91 - m.b100 - m.x184 + m.x185 == 0)

m.c31 = Constraint(expr= - m.b83 + m.b84 + m.b87 + m.b90 - m.b92 - m.b101 - m.x185 + m.x186 == 0)

m.c32 = Constraint(expr= - m.b87 + m.b91 + m.b94 - m.b96 + m.b97 - m.b105 + m.x187 - m.x189 == 0)

m.c33 = Constraint(expr= - m.b85 + m.b92 - m.b94 + m.b95 + m.b98 - m.b103 - m.x187 + m.x188 == 0)

m.c34 = Constraint(expr= - m.b86 + m.b93 - m.b95 + m.b96 + m.b99 - m.b104 - m.x188 + m.x189 == 0)

m.c35 = Constraint(expr= - m.b90 - m.b99 + m.b100 + m.b103 + m.b106 - m.b108 + m.x190 - m.x192 == 0)

m.c36 = Constraint(expr= - m.b88 - m.b97 + m.b101 + m.b104 - m.b106 + m.b107 - m.x190 + m.x191 == 0)

m.c37 = Constraint(expr= - m.b89 - m.b98 + m.b102 + m.b105 - m.b107 + m.b108 - m.x191 + m.x192 == 0)

m.c38 = Constraint(expr=   m.b1 + m.b4 + m.b7 + m.b10 + m.b13 + m.b16 + m.b19 + m.b22 + m.b25 + m.x157 + m.x160 + m.x163
                         == 1)

m.c39 = Constraint(expr=   m.b28 + m.b31 + m.b34 + m.b37 + m.b40 + m.b43 + m.b46 + m.b49 + m.b52 + m.x166 + m.x169
                         + m.x172 == 1)

m.c40 = Constraint(expr=   m.b55 + m.b58 + m.b61 + m.b64 + m.b67 + m.b70 + m.b73 + m.b76 + m.b79 + m.x175 + m.x178
                         + m.x181 == 1)

m.c41 = Constraint(expr=   m.b82 + m.b85 + m.b88 + m.b91 + m.b94 + m.b97 + m.b100 + m.b103 + m.b106 + m.x184 + m.x187
                         + m.x190 == 1)

m.c42 = Constraint(expr= - 5*m.b4 - 8*m.b7 - 10*m.b10 - 3*m.b16 - 4*m.b19 - 7*m.b22 - 0.00125*m.x121
                         - 0.000833333333333333*m.x133 - 0.001*m.x145 - m.x193 + m.x197 >= 0)

m.c43 = Constraint(expr= - 5*m.b5 - 8*m.b8 - 10*m.b11 - 3*m.b17 - 4*m.b20 - 7*m.b23 - 0.00125*m.x122
                         - 0.000833333333333333*m.x134 - 0.001*m.x146 - m.x197 + m.x201 >= 0)

m.c44 = Constraint(expr= - 5*m.b6 - 8*m.b9 - 10*m.b12 - 3*m.b18 - 4*m.b21 - 7*m.b24 - 0.00125*m.x123
                         - 0.000833333333333333*m.x135 - 0.001*m.x147 + m.x193 - m.x201 + m.x244 >= 0)

m.c45 = Constraint(expr= - 9*m.b31 - 11*m.b34 - 5*m.b37 - 7*m.b43 - 6*m.b46 - 4*m.b49 - 0.0025*m.x124 - 0.002*m.x136
                         - 0.00222222222222222*m.x148 - m.x194 + m.x198 >= 0)

m.c46 = Constraint(expr= - 9*m.b32 - 11*m.b35 - 5*m.b38 - 7*m.b44 - 6*m.b47 - 4*m.b50 - 0.0025*m.x125 - 0.002*m.x137
                         - 0.00222222222222222*m.x149 - m.x198 + m.x202 >= 0)

m.c47 = Constraint(expr= - 9*m.b33 - 11*m.b36 - 5*m.b39 - 7*m.b45 - 6*m.b48 - 4*m.b51 - 0.0025*m.x126 - 0.002*m.x138
                         - 0.00222222222222222*m.x150 + m.x194 - m.x202 + m.x244 >= 0)

m.c48 = Constraint(expr= - 11*m.b58 - m.b61 - 2*m.b64 - 5*m.b70 - 6*m.b73 - m.b76 - 0.00111111111111111*m.x127
                         - 0.00166666666666667*m.x139 - 0.000909090909090909*m.x151 - m.x195 + m.x199 >= 0)

m.c49 = Constraint(expr= - 11*m.b59 - m.b62 - 2*m.b65 - 5*m.b71 - 6*m.b74 - m.b77 - 0.00111111111111111*m.x128
                         - 0.00166666666666667*m.x140 - 0.000909090909090909*m.x152 - m.x199 + m.x203 >= 0)

m.c50 = Constraint(expr= - 11*m.b60 - m.b63 - 2*m.b66 - 5*m.b72 - 6*m.b75 - m.b78 - 0.00111111111111111*m.x129
                         - 0.00166666666666667*m.x141 - 0.000909090909090909*m.x153 + m.x195 - m.x203 + m.x244 >= 0)

m.c51 = Constraint(expr= - 9*m.b85 - 11*m.b88 - 5*m.b91 - 7*m.b97 - 6*m.b100 - 4*m.b103 - 0.0025*m.x130 - 0.002*m.x142
                         - 0.00222222222222222*m.x154 - m.x196 + m.x200 >= 0)

m.c52 = Constraint(expr= - 9*m.b86 - 11*m.b89 - 5*m.b92 - 7*m.b98 - 6*m.b101 - 4*m.b104 - 0.0025*m.x131 - 0.002*m.x143
                         - 0.00222222222222222*m.x155 - m.x200 + m.x204 >= 0)

m.c53 = Constraint(expr= - 9*m.b87 - 11*m.b90 - 5*m.b93 - 7*m.b99 - 6*m.b102 - 4*m.b105 - 0.0025*m.x132 - 0.002*m.x144
                         - 0.00222222222222222*m.x156 + m.x196 - m.x204 + m.x244 >= 0)

m.c54 = Constraint(expr= - 5*m.b4 - 8*m.b7 - 10*m.b10 - 3*m.b16 - 4*m.b19 - 7*m.b22 + m.x197 - m.x205 == 0)

m.c55 = Constraint(expr= - 5*m.b5 - 8*m.b8 - 10*m.b11 - 3*m.b17 - 4*m.b20 - 7*m.b23 + m.x201 - m.x209 == 0)

m.c56 = Constraint(expr= - 5*m.b6 - 8*m.b9 - 10*m.b12 - 3*m.b18 - 4*m.b21 - 7*m.b24 + m.x193 - m.x213 + m.x244 == 0)

m.c57 = Constraint(expr= - 9*m.b31 - 11*m.b34 - 5*m.b37 - 7*m.b43 - 6*m.b46 - 4*m.b49 + m.x198 - m.x206 == 0)

m.c58 = Constraint(expr= - 9*m.b32 - 11*m.b35 - 5*m.b38 - 7*m.b44 - 6*m.b47 - 4*m.b50 + m.x202 - m.x210 == 0)

m.c59 = Constraint(expr= - 9*m.b33 - 11*m.b36 - 5*m.b39 - 7*m.b45 - 6*m.b48 - 4*m.b51 + m.x194 - m.x214 + m.x244 == 0)

m.c60 = Constraint(expr= - 11*m.b58 - m.b61 - 2*m.b64 - 5*m.b70 - 6*m.b73 - m.b76 + m.x199 - m.x207 == 0)

m.c61 = Constraint(expr= - 11*m.b59 - m.b62 - 2*m.b65 - 5*m.b71 - 6*m.b74 - m.b77 + m.x203 - m.x211 == 0)

m.c62 = Constraint(expr= - 11*m.b60 - m.b63 - 2*m.b66 - 5*m.b72 - 6*m.b75 - m.b78 + m.x195 - m.x215 + m.x244 == 0)

m.c63 = Constraint(expr= - 9*m.b85 - 11*m.b88 - 5*m.b91 - 7*m.b97 - 6*m.b100 - 4*m.b103 + m.x200 - m.x208 == 0)

m.c64 = Constraint(expr= - 9*m.b86 - 11*m.b89 - 5*m.b92 - 7*m.b98 - 6*m.b101 - 4*m.b104 + m.x204 - m.x212 == 0)

m.c65 = Constraint(expr= - 9*m.b87 - 11*m.b90 - 5*m.b93 - 7*m.b99 - 6*m.b102 - 4*m.b105 + m.x196 - m.x216 + m.x244 == 0)

m.c66 = Constraint(expr=   m.x201 - m.x244 <= 0)

m.c67 = Constraint(expr=   m.x202 - m.x244 <= 0)

m.c68 = Constraint(expr=   m.x203 - m.x244 <= 0)

m.c69 = Constraint(expr=   m.x204 - m.x244 <= 0)

m.c70 = Constraint(expr= - 480000*m.b1 - 480000*m.b4 - 480000*m.b7 + m.x121 <= 0)

m.c71 = Constraint(expr= - 480000*m.b2 - 480000*m.b5 - 480000*m.b8 + m.x122 <= 0)

m.c72 = Constraint(expr= - 480000*m.b3 - 480000*m.b6 - 480000*m.b9 + m.x123 <= 0)

m.c73 = Constraint(expr= - 240000*m.b28 - 240000*m.b31 - 240000*m.b34 + m.x124 <= 0)

m.c74 = Constraint(expr= - 240000*m.b29 - 240000*m.b32 - 240000*m.b35 + m.x125 <= 0)

m.c75 = Constraint(expr= - 240000*m.b30 - 240000*m.b33 - 240000*m.b36 + m.x126 <= 0)

m.c76 = Constraint(expr= - 540000*m.b55 - 540000*m.b58 - 540000*m.b61 + m.x127 <= 0)

m.c77 = Constraint(expr= - 540000*m.b56 - 540000*m.b59 - 540000*m.b62 + m.x128 <= 0)

m.c78 = Constraint(expr= - 540000*m.b57 - 540000*m.b60 - 540000*m.b63 + m.x129 <= 0)

m.c79 = Constraint(expr= - 240000*m.b82 - 240000*m.b85 - 240000*m.b88 + m.x130 <= 0)

m.c80 = Constraint(expr= - 240000*m.b83 - 240000*m.b86 - 240000*m.b89 + m.x131 <= 0)

m.c81 = Constraint(expr= - 240000*m.b84 - 240000*m.b87 - 240000*m.b90 + m.x132 <= 0)

m.c82 = Constraint(expr= - 720000*m.b10 - 720000*m.b13 - 720000*m.b16 + m.x133 <= 0)

m.c83 = Constraint(expr= - 720000*m.b11 - 720000*m.b14 - 720000*m.b17 + m.x134 <= 0)

m.c84 = Constraint(expr= - 720000*m.b12 - 720000*m.b15 - 720000*m.b18 + m.x135 <= 0)

m.c85 = Constraint(expr= - 300000*m.b37 - 300000*m.b40 - 300000*m.b43 + m.x136 <= 0)

m.c86 = Constraint(expr= - 300000*m.b38 - 300000*m.b41 - 300000*m.b44 + m.x137 <= 0)

m.c87 = Constraint(expr= - 300000*m.b39 - 300000*m.b42 - 300000*m.b45 + m.x138 <= 0)

m.c88 = Constraint(expr= - 360000*m.b64 - 360000*m.b67 - 360000*m.b70 + m.x139 <= 0)

m.c89 = Constraint(expr= - 360000*m.b65 - 360000*m.b68 - 360000*m.b71 + m.x140 <= 0)

m.c90 = Constraint(expr= - 360000*m.b66 - 360000*m.b69 - 360000*m.b72 + m.x141 <= 0)

m.c91 = Constraint(expr= - 300000*m.b91 - 300000*m.b94 - 300000*m.b97 + m.x142 <= 0)

m.c92 = Constraint(expr= - 300000*m.b92 - 300000*m.b95 - 300000*m.b98 + m.x143 <= 0)

m.c93 = Constraint(expr= - 300000*m.b93 - 300000*m.b96 - 300000*m.b99 + m.x144 <= 0)

m.c94 = Constraint(expr= - 600000*m.b19 - 600000*m.b22 - 600000*m.b25 + m.x145 <= 0)

m.c95 = Constraint(expr= - 600000*m.b20 - 600000*m.b23 - 600000*m.b26 + m.x146 <= 0)

m.c96 = Constraint(expr= - 600000*m.b21 - 600000*m.b24 - 600000*m.b27 + m.x147 <= 0)

m.c97 = Constraint(expr= - 270000*m.b46 - 270000*m.b49 - 270000*m.b52 + m.x148 <= 0)

m.c98 = Constraint(expr= - 270000*m.b47 - 270000*m.b50 - 270000*m.b53 + m.x149 <= 0)

m.c99 = Constraint(expr= - 270000*m.b48 - 270000*m.b51 - 270000*m.b54 + m.x150 <= 0)

m.c100 = Constraint(expr= - 660000*m.b73 - 660000*m.b76 - 660000*m.b79 + m.x151 <= 0)

m.c101 = Constraint(expr= - 660000*m.b74 - 660000*m.b77 - 660000*m.b80 + m.x152 <= 0)

m.c102 = Constraint(expr= - 660000*m.b75 - 660000*m.b78 - 660000*m.b81 + m.x153 <= 0)

m.c103 = Constraint(expr= - 270000*m.b100 - 270000*m.b103 - 270000*m.b106 + m.x154 <= 0)

m.c104 = Constraint(expr= - 270000*m.b101 - 270000*m.b104 - 270000*m.b107 + m.x155 <= 0)

m.c105 = Constraint(expr= - 270000*m.b102 - 270000*m.b105 - 270000*m.b108 + m.x156 <= 0)

m.c106 = Constraint(expr=   m.b1 + m.b2 + m.b3 + m.b4 + m.b5 + m.b6 + m.b7 + m.b8 + m.b9 + m.b28 + m.b29 + m.b30 + m.b31
                          + m.b32 + m.b33 + m.b34 + m.b35 + m.b36 == 1)

m.c107 = Constraint(expr=   m.b55 + m.b56 + m.b57 + m.b58 + m.b59 + m.b60 + m.b61 + m.b62 + m.b63 + m.b82 + m.b83
                          + m.b84 + m.b85 + m.b86 + m.b87 + m.b88 + m.b89 + m.b90 == 1)

m.c108 = Constraint(expr=   m.b10 + m.b11 + m.b12 + m.b13 + m.b14 + m.b15 + m.b16 + m.b17 + m.b18 + m.b37 + m.b38
                          + m.b39 + m.b40 + m.b41 + m.b42 + m.b43 + m.b44 + m.b45 == 1)

m.c109 = Constraint(expr=   m.b64 + m.b65 + m.b66 + m.b67 + m.b68 + m.b69 + m.b70 + m.b71 + m.b72 + m.b91 + m.b92
                          + m.b93 + m.b94 + m.b95 + m.b96 + m.b97 + m.b98 + m.b99 == 1)

m.c110 = Constraint(expr=   m.b19 + m.b20 + m.b21 + m.b22 + m.b23 + m.b24 + m.b25 + m.b26 + m.b27 + m.b46 + m.b47
                          + m.b48 + m.b49 + m.b50 + m.b51 + m.b52 + m.b53 + m.b54 == 1)

m.c111 = Constraint(expr=   m.b73 + m.b74 + m.b75 + m.b76 + m.b77 + m.b78 + m.b79 + m.b80 + m.b81 + m.b100 + m.b101
                          + m.b102 + m.b103 + m.b104 + m.b105 + m.b106 + m.b107 + m.b108 == 1)

m.c112 = Constraint(expr=   m.b1 + m.b4 + m.b7 + m.b28 + m.b31 + m.b34 == 1)

m.c113 = Constraint(expr=m.x232*m.x244 - m.x127 - m.x128 - m.x129 - m.x130 - m.x131 - m.x132 == 0)

m.c114 = Constraint(expr=m.x233*m.x244 - m.x139 - m.x140 - m.x141 - m.x142 - m.x143 - m.x144 == 0)

m.c115 = Constraint(expr=m.x234*m.x244 - m.x151 - m.x152 - m.x153 - m.x154 - m.x155 - m.x156 == 0)

m.c116 = Constraint(expr=   m.x121 + m.x122 + m.x123 + m.x124 + m.x125 + m.x126 - m.x127 - m.x128 - m.x129 - m.x130
                          - m.x131 - m.x132 == 0)

m.c117 = Constraint(expr=   m.x133 + m.x134 + m.x135 + m.x136 + m.x137 + m.x138 - m.x139 - m.x140 - m.x141 - m.x142
                          - m.x143 - m.x144 == 0)

m.c118 = Constraint(expr=   m.x145 + m.x146 + m.x147 + m.x148 + m.x149 + m.x150 - m.x151 - m.x152 - m.x153 - m.x154
                          - m.x155 - m.x156 == 0)

m.c119 = Constraint(expr=   600*m.b1 + 600*m.b4 + 600*m.b7 - m.x193 + m.x220 <= 600)

m.c120 = Constraint(expr=   600*m.b1 + 600*m.b2 + 600*m.b4 + 600*m.b5 + 600*m.b7 + 600*m.b8 - m.x197 + m.x220 <= 600)

m.c121 = Constraint(expr=   600*m.b1 + 600*m.b2 + 600*m.b3 + 600*m.b4 + 600*m.b5 + 600*m.b6 + 600*m.b7 + 600*m.b8
                          + 600*m.b9 - m.x201 + m.x220 <= 600)

m.c122 = Constraint(expr=   600*m.b28 + 600*m.b31 + 600*m.b34 - m.x194 + m.x220 <= 600)

m.c123 = Constraint(expr=   600*m.b28 + 600*m.b29 + 600*m.b31 + 600*m.b32 + 600*m.b34 + 600*m.b35 - m.x198 + m.x220
                          <= 600)

m.c124 = Constraint(expr=   600*m.b28 + 600*m.b29 + 600*m.b30 + 600*m.b31 + 600*m.b32 + 600*m.b33 + 600*m.b34
                          + 600*m.b35 + 600*m.b36 - m.x202 + m.x220 <= 600)

m.c125 = Constraint(expr=   600*m.b55 + 600*m.b58 + 600*m.b61 - m.x195 + m.x221 <= 600)

m.c126 = Constraint(expr=   600*m.b55 + 600*m.b56 + 600*m.b58 + 600*m.b59 + 600*m.b61 + 600*m.b62 - m.x199 + m.x221
                          <= 600)

m.c127 = Constraint(expr=   600*m.b55 + 600*m.b56 + 600*m.b57 + 600*m.b58 + 600*m.b59 + 600*m.b60 + 600*m.b61
                          + 600*m.b62 + 600*m.b63 - m.x203 + m.x221 <= 600)

m.c128 = Constraint(expr=   600*m.b82 + 600*m.b85 + 600*m.b88 - m.x196 + m.x221 <= 600)

m.c129 = Constraint(expr=   600*m.b82 + 600*m.b83 + 600*m.b85 + 600*m.b86 + 600*m.b88 + 600*m.b89 - m.x200 + m.x221
                          <= 600)

m.c130 = Constraint(expr=   600*m.b82 + 600*m.b83 + 600*m.b84 + 600*m.b85 + 600*m.b86 + 600*m.b87 + 600*m.b88
                          + 600*m.b89 + 600*m.b90 - m.x204 + m.x221 <= 600)

m.c131 = Constraint(expr=   600*m.b10 + 600*m.b13 + 600*m.b16 - m.x193 + m.x222 <= 600)

m.c132 = Constraint(expr=   600*m.b10 + 600*m.b11 + 600*m.b13 + 600*m.b14 + 600*m.b16 + 600*m.b17 - m.x197 + m.x222
                          <= 600)

m.c133 = Constraint(expr=   600*m.b10 + 600*m.b11 + 600*m.b12 + 600*m.b13 + 600*m.b14 + 600*m.b15 + 600*m.b16
                          + 600*m.b17 + 600*m.b18 - m.x201 + m.x222 <= 600)

m.c134 = Constraint(expr=   600*m.b37 + 600*m.b40 + 600*m.b43 - m.x194 + m.x222 <= 600)

m.c135 = Constraint(expr=   600*m.b37 + 600*m.b38 + 600*m.b40 + 600*m.b41 + 600*m.b43 + 600*m.b44 - m.x198 + m.x222
                          <= 600)

m.c136 = Constraint(expr=   600*m.b37 + 600*m.b38 + 600*m.b39 + 600*m.b40 + 600*m.b41 + 600*m.b42 + 600*m.b43
                          + 600*m.b44 + 600*m.b45 - m.x202 + m.x222 <= 600)

m.c137 = Constraint(expr=   600*m.b64 + 600*m.b67 + 600*m.b70 - m.x195 + m.x223 <= 600)

m.c138 = Constraint(expr=   600*m.b64 + 600*m.b65 + 600*m.b67 + 600*m.b68 + 600*m.b70 + 600*m.b71 - m.x199 + m.x223
                          <= 600)

m.c139 = Constraint(expr=   600*m.b64 + 600*m.b65 + 600*m.b66 + 600*m.b67 + 600*m.b68 + 600*m.b69 + 600*m.b70
                          + 600*m.b71 + 600*m.b72 - m.x203 + m.x223 <= 600)

m.c140 = Constraint(expr=   600*m.b91 + 600*m.b94 + 600*m.b97 - m.x196 + m.x223 <= 600)

m.c141 = Constraint(expr=   600*m.b91 + 600*m.b92 + 600*m.b94 + 600*m.b95 + 600*m.b97 + 600*m.b98 - m.x200 + m.x223
                          <= 600)

m.c142 = Constraint(expr=   600*m.b91 + 600*m.b92 + 600*m.b93 + 600*m.b94 + 600*m.b95 + 600*m.b96 + 600*m.b97
                          + 600*m.b98 + 600*m.b99 - m.x204 + m.x223 <= 600)

m.c143 = Constraint(expr=   600*m.b19 + 600*m.b22 + 600*m.b25 - m.x193 + m.x224 <= 600)

m.c144 = Constraint(expr=   600*m.b19 + 600*m.b20 + 600*m.b22 + 600*m.b23 + 600*m.b25 + 600*m.b26 - m.x197 + m.x224
                          <= 600)

m.c145 = Constraint(expr=   600*m.b19 + 600*m.b20 + 600*m.b21 + 600*m.b22 + 600*m.b23 + 600*m.b24 + 600*m.b25
                          + 600*m.b26 + 600*m.b27 - m.x201 + m.x224 <= 600)

m.c146 = Constraint(expr=   600*m.b46 + 600*m.b49 + 600*m.b52 - m.x194 + m.x224 <= 600)

m.c147 = Constraint(expr=   600*m.b46 + 600*m.b47 + 600*m.b49 + 600*m.b50 + 600*m.b52 + 600*m.b53 - m.x198 + m.x224
                          <= 600)

m.c148 = Constraint(expr=   600*m.b46 + 600*m.b47 + 600*m.b48 + 600*m.b49 + 600*m.b50 + 600*m.b51 + 600*m.b52
                          + 600*m.b53 + 600*m.b54 - m.x202 + m.x224 <= 600)

m.c149 = Constraint(expr=   600*m.b73 + 600*m.b76 + 600*m.b79 - m.x195 + m.x225 <= 600)

m.c150 = Constraint(expr=   600*m.b73 + 600*m.b74 + 600*m.b76 + 600*m.b77 + 600*m.b79 + 600*m.b80 - m.x199 + m.x225
                          <= 600)

m.c151 = Constraint(expr=   600*m.b73 + 600*m.b74 + 600*m.b75 + 600*m.b76 + 600*m.b77 + 600*m.b78 + 600*m.b79
                          + 600*m.b80 + 600*m.b81 - m.x203 + m.x225 <= 600)

m.c152 = Constraint(expr=   600*m.b100 + 600*m.b103 + 600*m.b106 - m.x196 + m.x225 <= 600)

m.c153 = Constraint(expr=   600*m.b100 + 600*m.b101 + 600*m.b103 + 600*m.b104 + 600*m.b106 + 600*m.b107 - m.x200
                          + m.x225 <= 600)

m.c154 = Constraint(expr=   600*m.b100 + 600*m.b101 + 600*m.b102 + 600*m.b103 + 600*m.b104 + 600*m.b105 + 600*m.b106
                          + 600*m.b107 + 600*m.b108 - m.x204 + m.x225 <= 600)

m.c155 = Constraint(expr= - 600*m.b1 - 600*m.b2 - 600*m.b3 - 600*m.b4 - 600*m.b5 - 600*m.b6 - 600*m.b7 - 600*m.b8
                          - 600*m.b9 - m.x193 + m.x220 >= -600)

m.c156 = Constraint(expr= - 600*m.b2 - 600*m.b3 - 600*m.b5 - 600*m.b6 - 600*m.b8 - 600*m.b9 - m.x197 + m.x220 >= -600)

m.c157 = Constraint(expr= - 600*m.b3 - 600*m.b6 - 600*m.b9 - m.x201 + m.x220 >= -600)

m.c158 = Constraint(expr= - 600*m.b28 - 600*m.b29 - 600*m.b30 - 600*m.b31 - 600*m.b32 - 600*m.b33 - 600*m.b34
                          - 600*m.b35 - 600*m.b36 - m.x194 + m.x220 >= -600)

m.c159 = Constraint(expr= - 600*m.b29 - 600*m.b30 - 600*m.b32 - 600*m.b33 - 600*m.b35 - 600*m.b36 - m.x198 + m.x220
                          >= -600)

m.c160 = Constraint(expr= - 600*m.b30 - 600*m.b33 - 600*m.b36 - m.x202 + m.x220 >= -600)

m.c161 = Constraint(expr= - 600*m.b55 - 600*m.b56 - 600*m.b57 - 600*m.b58 - 600*m.b59 - 600*m.b60 - 600*m.b61
                          - 600*m.b62 - 600*m.b63 - m.x195 + m.x221 >= -600)

m.c162 = Constraint(expr= - 600*m.b56 - 600*m.b57 - 600*m.b59 - 600*m.b60 - 600*m.b62 - 600*m.b63 - m.x199 + m.x221
                          >= -600)

m.c163 = Constraint(expr= - 600*m.b57 - 600*m.b60 - 600*m.b63 - m.x203 + m.x221 >= -600)

m.c164 = Constraint(expr= - 600*m.b82 - 600*m.b83 - 600*m.b84 - 600*m.b85 - 600*m.b86 - 600*m.b87 - 600*m.b88
                          - 600*m.b89 - 600*m.b90 - m.x196 + m.x221 >= -600)

m.c165 = Constraint(expr= - 600*m.b83 - 600*m.b84 - 600*m.b86 - 600*m.b87 - 600*m.b89 - 600*m.b90 - m.x200 + m.x221
                          >= -600)

m.c166 = Constraint(expr= - 600*m.b84 - 600*m.b87 - 600*m.b90 - m.x204 + m.x221 >= -600)

m.c167 = Constraint(expr= - 600*m.b10 - 600*m.b11 - 600*m.b12 - 600*m.b13 - 600*m.b14 - 600*m.b15 - 600*m.b16
                          - 600*m.b17 - 600*m.b18 - m.x193 + m.x222 >= -600)

m.c168 = Constraint(expr= - 600*m.b11 - 600*m.b12 - 600*m.b14 - 600*m.b15 - 600*m.b17 - 600*m.b18 - m.x197 + m.x222
                          >= -600)

m.c169 = Constraint(expr= - 600*m.b12 - 600*m.b15 - 600*m.b18 - m.x201 + m.x222 >= -600)

m.c170 = Constraint(expr= - 600*m.b37 - 600*m.b38 - 600*m.b39 - 600*m.b40 - 600*m.b41 - 600*m.b42 - 600*m.b43
                          - 600*m.b44 - 600*m.b45 - m.x194 + m.x222 >= -600)

m.c171 = Constraint(expr= - 600*m.b38 - 600*m.b39 - 600*m.b41 - 600*m.b42 - 600*m.b44 - 600*m.b45 - m.x198 + m.x222
                          >= -600)

m.c172 = Constraint(expr= - 600*m.b39 - 600*m.b42 - 600*m.b45 - m.x202 + m.x222 >= -600)

m.c173 = Constraint(expr= - 600*m.b64 - 600*m.b65 - 600*m.b66 - 600*m.b67 - 600*m.b68 - 600*m.b69 - 600*m.b70
                          - 600*m.b71 - 600*m.b72 - m.x195 + m.x223 >= -600)

m.c174 = Constraint(expr= - 600*m.b65 - 600*m.b66 - 600*m.b68 - 600*m.b69 - 600*m.b71 - 600*m.b72 - m.x199 + m.x223
                          >= -600)

m.c175 = Constraint(expr= - 600*m.b66 - 600*m.b69 - 600*m.b72 - m.x203 + m.x223 >= -600)

m.c176 = Constraint(expr= - 600*m.b91 - 600*m.b92 - 600*m.b93 - 600*m.b94 - 600*m.b95 - 600*m.b96 - 600*m.b97
                          - 600*m.b98 - 600*m.b99 - m.x196 + m.x223 >= -600)

m.c177 = Constraint(expr= - 600*m.b92 - 600*m.b93 - 600*m.b95 - 600*m.b96 - 600*m.b98 - 600*m.b99 - m.x200 + m.x223
                          >= -600)

m.c178 = Constraint(expr= - 600*m.b93 - 600*m.b96 - 600*m.b99 - m.x204 + m.x223 >= -600)

m.c179 = Constraint(expr= - 600*m.b19 - 600*m.b20 - 600*m.b21 - 600*m.b22 - 600*m.b23 - 600*m.b24 - 600*m.b25
                          - 600*m.b26 - 600*m.b27 - m.x193 + m.x224 >= -600)

m.c180 = Constraint(expr= - 600*m.b20 - 600*m.b21 - 600*m.b23 - 600*m.b24 - 600*m.b26 - 600*m.b27 - m.x197 + m.x224
                          >= -600)

m.c181 = Constraint(expr= - 600*m.b21 - 600*m.b24 - 600*m.b27 - m.x201 + m.x224 >= -600)

m.c182 = Constraint(expr= - 600*m.b46 - 600*m.b47 - 600*m.b48 - 600*m.b49 - 600*m.b50 - 600*m.b51 - 600*m.b52
                          - 600*m.b53 - 600*m.b54 - m.x194 + m.x224 >= -600)

m.c183 = Constraint(expr= - 600*m.b47 - 600*m.b48 - 600*m.b50 - 600*m.b51 - 600*m.b53 - 600*m.b54 - m.x198 + m.x224
                          >= -600)

m.c184 = Constraint(expr= - 600*m.b48 - 600*m.b51 - 600*m.b54 - m.x202 + m.x224 >= -600)

m.c185 = Constraint(expr= - 600*m.b73 - 600*m.b74 - 600*m.b75 - 600*m.b76 - 600*m.b77 - 600*m.b78 - 600*m.b79
                          - 600*m.b80 - 600*m.b81 - m.x195 + m.x225 >= -600)

m.c186 = Constraint(expr= - 600*m.b74 - 600*m.b75 - 600*m.b77 - 600*m.b78 - 600*m.b80 - 600*m.b81 - m.x199 + m.x225
                          >= -600)

m.c187 = Constraint(expr= - 600*m.b75 - 600*m.b78 - 600*m.b81 - m.x203 + m.x225 >= -600)

m.c188 = Constraint(expr= - 600*m.b100 - 600*m.b101 - 600*m.b102 - 600*m.b103 - 600*m.b104 - 600*m.b105 - 600*m.b106
                          - 600*m.b107 - 600*m.b108 - m.x196 + m.x225 >= -600)

m.c189 = Constraint(expr= - 600*m.b101 - 600*m.b102 - 600*m.b104 - 600*m.b105 - 600*m.b107 - 600*m.b108 - m.x200
                          + m.x225 >= -600)

m.c190 = Constraint(expr= - 600*m.b102 - 600*m.b105 - 600*m.b108 - m.x204 + m.x225 >= -600)

m.c191 = Constraint(expr=   600*m.b1 + 600*m.b4 + 600*m.b7 - m.x205 + m.x226 <= 600)

m.c192 = Constraint(expr=   600*m.b1 + 600*m.b2 + 600*m.b4 + 600*m.b5 + 600*m.b7 + 600*m.b8 - m.x209 + m.x226 <= 600)

m.c193 = Constraint(expr=   600*m.b1 + 600*m.b2 + 600*m.b3 + 600*m.b4 + 600*m.b5 + 600*m.b6 + 600*m.b7 + 600*m.b8
                          + 600*m.b9 - m.x213 + m.x226 <= 600)

m.c194 = Constraint(expr=   600*m.b28 + 600*m.b31 + 600*m.b34 - m.x206 + m.x226 <= 600)

m.c195 = Constraint(expr=   600*m.b28 + 600*m.b29 + 600*m.b31 + 600*m.b32 + 600*m.b34 + 600*m.b35 - m.x210 + m.x226
                          <= 600)

m.c196 = Constraint(expr=   600*m.b28 + 600*m.b29 + 600*m.b30 + 600*m.b31 + 600*m.b32 + 600*m.b33 + 600*m.b34
                          + 600*m.b35 + 600*m.b36 - m.x214 + m.x226 <= 600)

m.c197 = Constraint(expr=   600*m.b55 + 600*m.b58 + 600*m.b61 - m.x207 + m.x227 <= 600)

m.c198 = Constraint(expr=   600*m.b55 + 600*m.b56 + 600*m.b58 + 600*m.b59 + 600*m.b61 + 600*m.b62 - m.x211 + m.x227
                          <= 600)

m.c199 = Constraint(expr=   600*m.b55 + 600*m.b56 + 600*m.b57 + 600*m.b58 + 600*m.b59 + 600*m.b60 + 600*m.b61
                          + 600*m.b62 + 600*m.b63 - m.x215 + m.x227 <= 600)

m.c200 = Constraint(expr=   600*m.b82 + 600*m.b85 + 600*m.b88 - m.x208 + m.x227 <= 600)

m.c201 = Constraint(expr=   600*m.b82 + 600*m.b83 + 600*m.b85 + 600*m.b86 + 600*m.b88 + 600*m.b89 - m.x212 + m.x227
                          <= 600)

m.c202 = Constraint(expr=   600*m.b82 + 600*m.b83 + 600*m.b84 + 600*m.b85 + 600*m.b86 + 600*m.b87 + 600*m.b88
                          + 600*m.b89 + 600*m.b90 - m.x216 + m.x227 <= 600)

m.c203 = Constraint(expr=   600*m.b10 + 600*m.b13 + 600*m.b16 - m.x205 + m.x228 <= 600)

m.c204 = Constraint(expr=   600*m.b10 + 600*m.b11 + 600*m.b13 + 600*m.b14 + 600*m.b16 + 600*m.b17 - m.x209 + m.x228
                          <= 600)

m.c205 = Constraint(expr=   600*m.b10 + 600*m.b11 + 600*m.b12 + 600*m.b13 + 600*m.b14 + 600*m.b15 + 600*m.b16
                          + 600*m.b17 + 600*m.b18 - m.x213 + m.x228 <= 600)

m.c206 = Constraint(expr=   600*m.b37 + 600*m.b40 + 600*m.b43 - m.x206 + m.x228 <= 600)

m.c207 = Constraint(expr=   600*m.b37 + 600*m.b38 + 600*m.b40 + 600*m.b41 + 600*m.b43 + 600*m.b44 - m.x210 + m.x228
                          <= 600)

m.c208 = Constraint(expr=   600*m.b37 + 600*m.b38 + 600*m.b39 + 600*m.b40 + 600*m.b41 + 600*m.b42 + 600*m.b43
                          + 600*m.b44 + 600*m.b45 - m.x214 + m.x228 <= 600)

m.c209 = Constraint(expr=   600*m.b64 + 600*m.b67 + 600*m.b70 - m.x207 + m.x229 <= 600)

m.c210 = Constraint(expr=   600*m.b64 + 600*m.b65 + 600*m.b67 + 600*m.b68 + 600*m.b70 + 600*m.b71 - m.x211 + m.x229
                          <= 600)

m.c211 = Constraint(expr=   600*m.b64 + 600*m.b65 + 600*m.b66 + 600*m.b67 + 600*m.b68 + 600*m.b69 + 600*m.b70
                          + 600*m.b71 + 600*m.b72 - m.x215 + m.x229 <= 600)

m.c212 = Constraint(expr=   600*m.b91 + 600*m.b94 + 600*m.b97 - m.x208 + m.x229 <= 600)

m.c213 = Constraint(expr=   600*m.b91 + 600*m.b92 + 600*m.b94 + 600*m.b95 + 600*m.b97 + 600*m.b98 - m.x212 + m.x229
                          <= 600)

m.c214 = Constraint(expr=   600*m.b91 + 600*m.b92 + 600*m.b93 + 600*m.b94 + 600*m.b95 + 600*m.b96 + 600*m.b97
                          + 600*m.b98 + 600*m.b99 - m.x216 + m.x229 <= 600)

m.c215 = Constraint(expr=   600*m.b19 + 600*m.b22 + 600*m.b25 - m.x205 + m.x230 <= 600)

m.c216 = Constraint(expr=   600*m.b19 + 600*m.b20 + 600*m.b22 + 600*m.b23 + 600*m.b25 + 600*m.b26 - m.x209 + m.x230
                          <= 600)

m.c217 = Constraint(expr=   600*m.b19 + 600*m.b20 + 600*m.b21 + 600*m.b22 + 600*m.b23 + 600*m.b24 + 600*m.b25
                          + 600*m.b26 + 600*m.b27 - m.x213 + m.x230 <= 600)

m.c218 = Constraint(expr=   600*m.b46 + 600*m.b49 + 600*m.b52 - m.x206 + m.x230 <= 600)

m.c219 = Constraint(expr=   600*m.b46 + 600*m.b47 + 600*m.b49 + 600*m.b50 + 600*m.b52 + 600*m.b53 - m.x210 + m.x230
                          <= 600)

m.c220 = Constraint(expr=   600*m.b46 + 600*m.b47 + 600*m.b48 + 600*m.b49 + 600*m.b50 + 600*m.b51 + 600*m.b52
                          + 600*m.b53 + 600*m.b54 - m.x214 + m.x230 <= 600)

m.c221 = Constraint(expr=   600*m.b73 + 600*m.b76 + 600*m.b79 - m.x207 + m.x231 <= 600)

m.c222 = Constraint(expr=   600*m.b73 + 600*m.b74 + 600*m.b76 + 600*m.b77 + 600*m.b79 + 600*m.b80 - m.x211 + m.x231
                          <= 600)

m.c223 = Constraint(expr=   600*m.b73 + 600*m.b74 + 600*m.b75 + 600*m.b76 + 600*m.b77 + 600*m.b78 + 600*m.b79
                          + 600*m.b80 + 600*m.b81 - m.x215 + m.x231 <= 600)

m.c224 = Constraint(expr=   600*m.b100 + 600*m.b103 + 600*m.b106 - m.x208 + m.x231 <= 600)

m.c225 = Constraint(expr=   600*m.b100 + 600*m.b101 + 600*m.b103 + 600*m.b104 + 600*m.b106 + 600*m.b107 - m.x212
                          + m.x231 <= 600)

m.c226 = Constraint(expr=   600*m.b100 + 600*m.b101 + 600*m.b102 + 600*m.b103 + 600*m.b104 + 600*m.b105 + 600*m.b106
                          + 600*m.b107 + 600*m.b108 - m.x216 + m.x231 <= 600)

m.c227 = Constraint(expr= - 600*m.b1 - 600*m.b2 - 600*m.b3 - 600*m.b4 - 600*m.b5 - 600*m.b6 - 600*m.b7 - 600*m.b8
                          - 600*m.b9 - m.x205 + m.x226 >= -600)

m.c228 = Constraint(expr= - 600*m.b2 - 600*m.b3 - 600*m.b5 - 600*m.b6 - 600*m.b8 - 600*m.b9 - m.x209 + m.x226 >= -600)

m.c229 = Constraint(expr= - 600*m.b3 - 600*m.b6 - 600*m.b9 - m.x213 + m.x226 >= -600)

m.c230 = Constraint(expr= - 600*m.b28 - 600*m.b29 - 600*m.b30 - 600*m.b31 - 600*m.b32 - 600*m.b33 - 600*m.b34
                          - 600*m.b35 - 600*m.b36 - m.x206 + m.x226 >= -600)

m.c231 = Constraint(expr= - 600*m.b29 - 600*m.b30 - 600*m.b32 - 600*m.b33 - 600*m.b35 - 600*m.b36 - m.x210 + m.x226
                          >= -600)

m.c232 = Constraint(expr= - 600*m.b30 - 600*m.b33 - 600*m.b36 - m.x214 + m.x226 >= -600)

m.c233 = Constraint(expr= - 600*m.b55 - 600*m.b56 - 600*m.b57 - 600*m.b58 - 600*m.b59 - 600*m.b60 - 600*m.b61
                          - 600*m.b62 - 600*m.b63 - m.x207 + m.x227 >= -600)

m.c234 = Constraint(expr= - 600*m.b56 - 600*m.b57 - 600*m.b59 - 600*m.b60 - 600*m.b62 - 600*m.b63 - m.x211 + m.x227
                          >= -600)

m.c235 = Constraint(expr= - 600*m.b57 - 600*m.b60 - 600*m.b63 - m.x215 + m.x227 >= -600)

m.c236 = Constraint(expr= - 600*m.b82 - 600*m.b83 - 600*m.b84 - 600*m.b85 - 600*m.b86 - 600*m.b87 - 600*m.b88
                          - 600*m.b89 - 600*m.b90 - m.x208 + m.x227 >= -600)

m.c237 = Constraint(expr= - 600*m.b83 - 600*m.b84 - 600*m.b86 - 600*m.b87 - 600*m.b89 - 600*m.b90 - m.x212 + m.x227
                          >= -600)

m.c238 = Constraint(expr= - 600*m.b84 - 600*m.b87 - 600*m.b90 - m.x216 + m.x227 >= -600)

m.c239 = Constraint(expr= - 600*m.b10 - 600*m.b11 - 600*m.b12 - 600*m.b13 - 600*m.b14 - 600*m.b15 - 600*m.b16
                          - 600*m.b17 - 600*m.b18 - m.x205 + m.x228 >= -600)

m.c240 = Constraint(expr= - 600*m.b11 - 600*m.b12 - 600*m.b14 - 600*m.b15 - 600*m.b17 - 600*m.b18 - m.x209 + m.x228
                          >= -600)

m.c241 = Constraint(expr= - 600*m.b12 - 600*m.b15 - 600*m.b18 - m.x213 + m.x228 >= -600)

m.c242 = Constraint(expr= - 600*m.b37 - 600*m.b38 - 600*m.b39 - 600*m.b40 - 600*m.b41 - 600*m.b42 - 600*m.b43
                          - 600*m.b44 - 600*m.b45 - m.x206 + m.x228 >= -600)

m.c243 = Constraint(expr= - 600*m.b38 - 600*m.b39 - 600*m.b41 - 600*m.b42 - 600*m.b44 - 600*m.b45 - m.x210 + m.x228
                          >= -600)

m.c244 = Constraint(expr= - 600*m.b39 - 600*m.b42 - 600*m.b45 - m.x214 + m.x228 >= -600)

m.c245 = Constraint(expr= - 600*m.b64 - 600*m.b65 - 600*m.b66 - 600*m.b67 - 600*m.b68 - 600*m.b69 - 600*m.b70
                          - 600*m.b71 - 600*m.b72 - m.x207 + m.x229 >= -600)

m.c246 = Constraint(expr= - 600*m.b65 - 600*m.b66 - 600*m.b68 - 600*m.b69 - 600*m.b71 - 600*m.b72 - m.x211 + m.x229
                          >= -600)

m.c247 = Constraint(expr= - 600*m.b66 - 600*m.b69 - 600*m.b72 - m.x215 + m.x229 >= -600)

m.c248 = Constraint(expr= - 600*m.b91 - 600*m.b92 - 600*m.b93 - 600*m.b94 - 600*m.b95 - 600*m.b96 - 600*m.b97
                          - 600*m.b98 - 600*m.b99 - m.x208 + m.x229 >= -600)

m.c249 = Constraint(expr= - 600*m.b92 - 600*m.b93 - 600*m.b95 - 600*m.b96 - 600*m.b98 - 600*m.b99 - m.x212 + m.x229
                          >= -600)

m.c250 = Constraint(expr= - 600*m.b93 - 600*m.b96 - 600*m.b99 - m.x216 + m.x229 >= -600)

m.c251 = Constraint(expr= - 600*m.b19 - 600*m.b20 - 600*m.b21 - 600*m.b22 - 600*m.b23 - 600*m.b24 - 600*m.b25
                          - 600*m.b26 - 600*m.b27 - m.x205 + m.x230 >= -600)

m.c252 = Constraint(expr= - 600*m.b20 - 600*m.b21 - 600*m.b23 - 600*m.b24 - 600*m.b26 - 600*m.b27 - m.x209 + m.x230
                          >= -600)

m.c253 = Constraint(expr= - 600*m.b21 - 600*m.b24 - 600*m.b27 - m.x213 + m.x230 >= -600)

m.c254 = Constraint(expr= - 600*m.b46 - 600*m.b47 - 600*m.b48 - 600*m.b49 - 600*m.b50 - 600*m.b51 - 600*m.b52
                          - 600*m.b53 - 600*m.b54 - m.x206 + m.x230 >= -600)

m.c255 = Constraint(expr= - 600*m.b47 - 600*m.b48 - 600*m.b50 - 600*m.b51 - 600*m.b53 - 600*m.b54 - m.x210 + m.x230
                          >= -600)

m.c256 = Constraint(expr= - 600*m.b48 - 600*m.b51 - 600*m.b54 - m.x214 + m.x230 >= -600)

m.c257 = Constraint(expr= - 600*m.b73 - 600*m.b74 - 600*m.b75 - 600*m.b76 - 600*m.b77 - 600*m.b78 - 600*m.b79
                          - 600*m.b80 - 600*m.b81 - m.x207 + m.x231 >= -600)

m.c258 = Constraint(expr= - 600*m.b74 - 600*m.b75 - 600*m.b77 - 600*m.b78 - 600*m.b80 - 600*m.b81 - m.x211 + m.x231
                          >= -600)

m.c259 = Constraint(expr= - 600*m.b75 - 600*m.b78 - 600*m.b81 - m.x215 + m.x231 >= -600)

m.c260 = Constraint(expr= - 600*m.b100 - 600*m.b101 - 600*m.b102 - 600*m.b103 - 600*m.b104 - 600*m.b105 - 600*m.b106
                          - 600*m.b107 - 600*m.b108 - m.x208 + m.x231 >= -600)

m.c261 = Constraint(expr= - 600*m.b101 - 600*m.b102 - 600*m.b104 - 600*m.b105 - 600*m.b107 - 600*m.b108 - m.x212
                          + m.x231 >= -600)

m.c262 = Constraint(expr= - 600*m.b102 - 600*m.b105 - 600*m.b108 - m.x216 + m.x231 >= -600)

m.c263 = Constraint(expr=-m.x235*(m.x226 - m.x220) + m.x121 + m.x122 + m.x123 + m.x124 + m.x125 + m.x126 == 0)

m.c264 = Constraint(expr=-m.x236*(m.x227 - m.x221) + m.x127 + m.x128 + m.x129 + m.x130 + m.x131 + m.x132 == 0)

m.c265 = Constraint(expr=-m.x237*(m.x228 - m.x222) + m.x133 + m.x134 + m.x135 + m.x136 + m.x137 + m.x138 == 0)

m.c266 = Constraint(expr=-m.x238*(m.x229 - m.x223) + m.x139 + m.x140 + m.x141 + m.x142 + m.x143 + m.x144 == 0)

m.c267 = Constraint(expr=-m.x239*(m.x230 - m.x224) + m.x145 + m.x146 + m.x147 + m.x148 + m.x149 + m.x150 == 0)

m.c268 = Constraint(expr=-m.x240*(m.x231 - m.x225) + m.x151 + m.x152 + m.x153 + m.x154 + m.x155 + m.x156 == 0)

m.c269 = Constraint(expr= - 800*m.b1 - 800*m.b2 - 800*m.b3 - 800*m.b4 - 800*m.b5 - 800*m.b6 - 800*m.b7 - 800*m.b8
                          - 800*m.b9 - 400*m.b28 - 400*m.b29 - 400*m.b30 - 400*m.b31 - 400*m.b32 - 400*m.b33 - 400*m.b34
                          - 400*m.b35 - 400*m.b36 + m.x235 <= 0)

m.c270 = Constraint(expr= - 900*m.b55 - 900*m.b56 - 900*m.b57 - 900*m.b58 - 900*m.b59 - 900*m.b60 - 900*m.b61
                          - 900*m.b62 - 900*m.b63 - 400*m.b82 - 400*m.b83 - 400*m.b84 - 400*m.b85 - 400*m.b86
                          - 400*m.b87 - 400*m.b88 - 400*m.b89 - 400*m.b90 + m.x236 <= 0)

m.c271 = Constraint(expr= - 1200*m.b10 - 1200*m.b11 - 1200*m.b12 - 1200*m.b13 - 1200*m.b14 - 1200*m.b15 - 1200*m.b16
                          - 1200*m.b17 - 1200*m.b18 - 500*m.b37 - 500*m.b38 - 500*m.b39 - 500*m.b40 - 500*m.b41
                          - 500*m.b42 - 500*m.b43 - 500*m.b44 - 500*m.b45 + m.x237 <= 0)

m.c272 = Constraint(expr= - 600*m.b64 - 600*m.b65 - 600*m.b66 - 600*m.b67 - 600*m.b68 - 600*m.b69 - 600*m.b70
                          - 600*m.b71 - 600*m.b72 - 500*m.b91 - 500*m.b92 - 500*m.b93 - 500*m.b94 - 500*m.b95
                          - 500*m.b96 - 500*m.b97 - 500*m.b98 - 500*m.b99 + m.x238 <= 0)

m.c273 = Constraint(expr= - 1000*m.b19 - 1000*m.b20 - 1000*m.b21 - 1000*m.b22 - 1000*m.b23 - 1000*m.b24 - 1000*m.b25
                          - 1000*m.b26 - 1000*m.b27 - 450*m.b46 - 450*m.b47 - 450*m.b48 - 450*m.b49 - 450*m.b50
                          - 450*m.b51 - 450*m.b52 - 450*m.b53 - 450*m.b54 + m.x239 <= 0)

m.c274 = Constraint(expr= - 1100*m.b73 - 1100*m.b74 - 1100*m.b75 - 1100*m.b76 - 1100*m.b77 - 1100*m.b78 - 1100*m.b79
                          - 1100*m.b80 - 1100*m.b81 - 450*m.b100 - 450*m.b101 - 450*m.b102 - 450*m.b103 - 450*m.b104
                          - 450*m.b105 - 450*m.b106 - 450*m.b107 - 450*m.b108 + m.x240 <= 0)

m.c275 = Constraint(expr=   m.x221 - m.x227 + m.x241 == 0)

m.c276 = Constraint(expr=   m.x223 - m.x229 + m.x242 == 0)

m.c277 = Constraint(expr=   m.x225 - m.x231 + m.x243 == 0)

m.c278 = Constraint(expr=   m.x241 - m.x244 <= 0)

m.c279 = Constraint(expr=   m.x242 - m.x244 <= 0)

m.c280 = Constraint(expr=   m.x243 - m.x244 <= 0)

m.c281 = Constraint(expr=   600*m.b109 + 600*m.b115 + m.x220 - m.x221 <= 600)

m.c282 = Constraint(expr=   600*m.b110 + 600*m.b116 + m.x222 - m.x223 <= 600)

m.c283 = Constraint(expr=   600*m.b111 + 600*m.b117 + m.x224 - m.x225 <= 600)

m.c284 = Constraint(expr= - 600*m.b112 - 600*m.b118 + m.x220 - m.x221 >= -600)

m.c285 = Constraint(expr= - 600*m.b113 - 600*m.b119 + m.x222 - m.x223 >= -600)

m.c286 = Constraint(expr= - 600*m.b114 - 600*m.b120 + m.x224 - m.x225 >= -600)

m.c287 = Constraint(expr=   1200*m.b109 + 1200*m.b118 + m.x226 - m.x227 <= 1200)

m.c288 = Constraint(expr=   1200*m.b110 + 1200*m.b119 + m.x228 - m.x229 <= 1200)

m.c289 = Constraint(expr=   1200*m.b111 + 1200*m.b120 + m.x230 - m.x231 <= 1200)

m.c290 = Constraint(expr= - 1200*m.b112 - 1200*m.b115 + m.x226 - m.x227 >= -1200)

m.c291 = Constraint(expr= - 1200*m.b113 - 1200*m.b116 + m.x228 - m.x229 >= -1200)

m.c292 = Constraint(expr= - 1200*m.b114 - 1200*m.b117 + m.x230 - m.x231 >= -1200)

m.c293 = Constraint(expr= - 600*m.b109 - 600*m.b112 - 600*m.b115 - 600*m.b118 - m.x221 + m.x226 >= -600)

m.c294 = Constraint(expr= - 600*m.b110 - 600*m.b113 - 600*m.b116 - 600*m.b119 - m.x223 + m.x228 >= -600)

m.c295 = Constraint(expr= - 600*m.b111 - 600*m.b114 - 600*m.b117 - 600*m.b120 - m.x225 + m.x230 >= -600)

m.c296 = Constraint(expr= - 600*m.b109 - 600*m.b112 - 600*m.b115 - 600*m.b118 - m.x220 + m.x227 >= -600)

m.c297 = Constraint(expr= - 600*m.b110 - 600*m.b113 - 600*m.b116 - 600*m.b119 - m.x222 + m.x229 >= -600)

m.c298 = Constraint(expr= - 600*m.b111 - 600*m.b114 - 600*m.b117 - 600*m.b120 - m.x224 + m.x231 >= -600)

m.c299 = Constraint(expr=-(m.x221 - m.x220)*m.x235 - 480000*m.b109 + m.x217 >= -480000)

m.c300 = Constraint(expr=-(m.x223 - m.x222)*m.x237 - 360000*m.b110 + m.x218 >= -360000)

m.c301 = Constraint(expr=-(m.x225 - m.x224)*m.x239 - 600000*m.b111 + m.x219 >= -600000)

m.c302 = Constraint(expr=-(m.x227 - m.x226)*m.x236 - 480000*m.b109 + m.x217 >= -480000)

m.c303 = Constraint(expr=-(m.x229 - m.x228)*m.x238 - 360000*m.b110 + m.x218 >= -360000)

m.c304 = Constraint(expr=-(m.x231 - m.x230)*m.x240 - 600000*m.b111 + m.x219 >= -600000)

m.c305 = Constraint(expr=-(m.x220 - m.x221)*m.x236 - 480000*m.b112 + m.x217 >= -480000)

m.c306 = Constraint(expr=-(m.x222 - m.x223)*m.x238 - 360000*m.b113 + m.x218 >= -360000)

m.c307 = Constraint(expr=-(m.x224 - m.x225)*m.x240 - 600000*m.b114 + m.x219 >= -600000)

m.c308 = Constraint(expr=-(m.x226 - m.x227)*m.x235 - 480000*m.b112 + m.x217 >= -480000)

m.c309 = Constraint(expr=-(m.x228 - m.x229)*m.x237 - 360000*m.b113 + m.x218 >= -360000)

m.c310 = Constraint(expr=-(m.x230 - m.x231)*m.x239 - 600000*m.b114 + m.x219 >= -600000)

m.c311 = Constraint(expr=-(m.x236 - m.x235)*(m.x227 - m.x221) - 480000*m.b115 + m.x217 >= -480000)

m.c312 = Constraint(expr=-(m.x238 - m.x237)*(m.x229 - m.x223) - 360000*m.b116 + m.x218 >= -360000)

m.c313 = Constraint(expr=-(m.x240 - m.x239)*(m.x231 - m.x225) - 600000*m.b117 + m.x219 >= -600000)

m.c314 = Constraint(expr=-(m.x235 - m.x236)*(m.x226 - m.x220) - 480000*m.b118 + m.x217 >= -480000)

m.c315 = Constraint(expr=-(m.x237 - m.x238)*(m.x228 - m.x222) - 360000*m.b119 + m.x218 >= -360000)

m.c316 = Constraint(expr=-(m.x239 - m.x240)*(m.x230 - m.x224) - 600000*m.b120 + m.x219 >= -600000)

m.c317 = Constraint(expr=   480000*m.b109 + 480000*m.b112 + 480000*m.b115 + 480000*m.b118 - m.x121 - m.x122 - m.x123
                          - m.x124 - m.x125 - m.x126 + m.x217 >= 0)

m.c318 = Constraint(expr=   360000*m.b110 + 360000*m.b113 + 360000*m.b116 + 360000*m.b119 - m.x133 - m.x134 - m.x135
                          - m.x136 - m.x137 - m.x138 + m.x218 >= 0)

m.c319 = Constraint(expr=   600000*m.b111 + 600000*m.b114 + 600000*m.b117 + 600000*m.b120 - m.x145 - m.x146 - m.x147
                          - m.x148 - m.x149 - m.x150 + m.x219 >= 0)
