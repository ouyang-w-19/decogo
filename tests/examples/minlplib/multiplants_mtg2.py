#  MINLP written by GAMS Convert at 04/21/18 13:52:37
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        307       73      116      118        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        230      118      112        0        0        0        0        0
#  FX     33       33        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       2690     2564      126        0


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
m.x145 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x146 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x147 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x148 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x149 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x150 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x151 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x152 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x153 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x154 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x155 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x156 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x157 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x158 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x159 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x160 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x161 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x162 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x163 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x164 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x165 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x166 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x167 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x168 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x169 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x170 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x171 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x172 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x173 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x174 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x175 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x176 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x177 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x178 = Var(within=Reals,bounds=(0,800),initialize=0)
m.x179 = Var(within=Reals,bounds=(0,800),initialize=0)
m.x180 = Var(within=Reals,bounds=(0,800),initialize=0)
m.x181 = Var(within=Reals,bounds=(0,800),initialize=0)
m.x182 = Var(within=Reals,bounds=(0,800),initialize=0)
m.x183 = Var(within=Reals,bounds=(0,800),initialize=0)
m.x184 = Var(within=Reals,bounds=(0,800),initialize=0)
m.x185 = Var(within=Reals,bounds=(0,1600),initialize=0)
m.x186 = Var(within=Reals,bounds=(0,1600),initialize=0)
m.x187 = Var(within=Reals,bounds=(0,1600),initialize=0)
m.x188 = Var(within=Reals,bounds=(0,1600),initialize=0)
m.x189 = Var(within=Reals,bounds=(0,1600),initialize=0)
m.x190 = Var(within=Reals,bounds=(0,1600),initialize=0)
m.x191 = Var(within=Reals,bounds=(0,1600),initialize=0)
m.x192 = Var(within=Reals,bounds=(0,1600),initialize=0)
m.x193 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x194 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x195 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x196 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x197 = Var(within=Reals,bounds=(0,800),initialize=0)
m.x198 = Var(within=Reals,bounds=(0,800),initialize=0)
m.x199 = Var(within=Reals,bounds=(0,800),initialize=0)
m.x200 = Var(within=Reals,bounds=(0,800),initialize=0)
m.x201 = Var(within=Reals,bounds=(0,800),initialize=0)
m.x202 = Var(within=Reals,bounds=(0,800),initialize=0)
m.x203 = Var(within=Reals,bounds=(0,800),initialize=0)
m.x204 = Var(within=Reals,bounds=(0,800),initialize=0)
m.x205 = Var(within=Reals,bounds=(0,1600),initialize=0)
m.x206 = Var(within=Reals,bounds=(0,1600),initialize=0)
m.x207 = Var(within=Reals,bounds=(0,1600),initialize=0)
m.x208 = Var(within=Reals,bounds=(0,1600),initialize=0)
m.x209 = Var(within=Reals,bounds=(0,1600),initialize=0)
m.x210 = Var(within=Reals,bounds=(0,1600),initialize=0)
m.x211 = Var(within=Reals,bounds=(0,1600),initialize=0)
m.x212 = Var(within=Reals,bounds=(0,1600),initialize=0)
m.x213 = Var(within=Reals,bounds=(60,None),initialize=60)
m.x214 = Var(within=Reals,bounds=(54,None),initialize=54)
m.x215 = Var(within=Reals,bounds=(500,None),initialize=500)
m.x216 = Var(within=Reals,bounds=(45,None),initialize=45)
m.x217 = Var(within=Reals,bounds=(0,None),initialize=1170)
m.x218 = Var(within=Reals,bounds=(0,None),initialize=1120)
m.x219 = Var(within=Reals,bounds=(0,None),initialize=1340)
m.x220 = Var(within=Reals,bounds=(0,None),initialize=1290)
m.x221 = Var(within=Reals,bounds=(0,None),initialize=1340)
m.x222 = Var(within=Reals,bounds=(0,None),initialize=1340)
m.x223 = Var(within=Reals,bounds=(0,None),initialize=1210)
m.x224 = Var(within=Reals,bounds=(0,None),initialize=1160)
m.x225 = Var(within=Reals,bounds=(21.4285714285714,800),initialize=21.4285714285714)
m.x226 = Var(within=Reals,bounds=(16.7441860465116,800),initialize=16.7441860465116)
m.x227 = Var(within=Reals,bounds=(149.253731343284,800),initialize=149.253731343284)
m.x228 = Var(within=Reals,bounds=(15.5172413793103,800),initialize=15.5172413793103)
m.x229 = Var(within=Reals,bounds=(400,800),initialize=400)
m.x230 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=m.x230, sense=maximize)

m.c1 = Constraint(expr=m.x230*m.x229 + 0.00203*(m.x225**2*(m.x218 - m.x213) + (m.x229 - m.x225)**2*m.x213) + 0.00203*(
                       m.x226**2*(m.x220 - m.x214) + (m.x229 - m.x226)**2*m.x214) + 0.00203*(m.x227**2*(m.x222 - m.x215)
                        + (m.x229 - m.x227)**2*m.x215) + 0.00203*(m.x228**2*(m.x224 - m.x216) + (m.x229 - m.x228)**2*
                       m.x216) + 7600*m.b1 + 7600*m.b2 + 7600*m.b3 + 7600*m.b4 + 7600*m.b5 + 7600*m.b6 + 7600*m.b7
                        + 7600*m.b8 + 7600*m.b9 + 7600*m.b10 + 7600*m.b11 + 7600*m.b12 + 7600*m.b13 + 7600*m.b14
                        + 7600*m.b15 + 7600*m.b16 + 760*m.b17 + 760*m.b18 + 760*m.b19 + 760*m.b20 + 3040*m.b21
                        + 3040*m.b22 + 3040*m.b23 + 3040*m.b24 + 7600*m.b25 + 7600*m.b26 + 7600*m.b27 + 7600*m.b28
                        + 760*m.b29 + 760*m.b30 + 760*m.b31 + 760*m.b32 + 3040*m.b33 + 3040*m.b34 + 3040*m.b35
                        + 3040*m.b36 + 7600*m.b37 + 7600*m.b38 + 7600*m.b39 + 7600*m.b40 + 3040*m.b41 + 3040*m.b42
                        + 3040*m.b43 + 3040*m.b44 + 3040*m.b45 + 3040*m.b46 + 3040*m.b47 + 3040*m.b48 + 2280*m.b49
                        + 2280*m.b50 + 2280*m.b51 + 2280*m.b52 + 2280*m.b53 + 2280*m.b54 + 2280*m.b55 + 2280*m.b56
                        + 9120*m.b57 + 9120*m.b58 + 9120*m.b59 + 9120*m.b60 + 2280*m.b61 + 2280*m.b62 + 2280*m.b63
                        + 2280*m.b64 + 760*m.b65 + 760*m.b66 + 760*m.b67 + 760*m.b68 + 9120*m.b69 + 9120*m.b70
                        + 9120*m.b71 + 9120*m.b72 + 2280*m.b73 + 2280*m.b74 + 2280*m.b75 + 2280*m.b76 + 760*m.b77
                        + 760*m.b78 + 760*m.b79 + 760*m.b80 + 9120*m.b81 + 9120*m.b82 + 9120*m.b83 + 9120*m.b84
                        + 9120*m.b85 + 9120*m.b86 + 9120*m.b87 + 9120*m.b88 + 9120*m.b89 + 9120*m.b90 + 9120*m.b91
                        + 9120*m.b92 + 9120*m.b93 + 9120*m.b94 + 9120*m.b95 + 9120*m.b96 - 4*m.x117 - 4*m.x118
                        - 4*m.x119 - 4*m.x120 - 1.5*m.x125 - 1.5*m.x126 - 1.5*m.x127 - 1.5*m.x128 - 6.5*m.x133
                        - 6.5*m.x134 - 6.5*m.x135 - 6.5*m.x136 - 3*m.x141 - 3*m.x142 - 3*m.x143 - 3*m.x144
                        + 0.1218*m.x193 + 0.1218*m.x194 + 0.1218*m.x195 + 0.1218*m.x196 == 0)

m.c2 = Constraint(expr=   m.b1 + m.b5 + m.b9 - m.b16 - m.b28 - m.b40 + m.x145 - m.x148 == 0)

m.c3 = Constraint(expr=   m.b2 + m.b6 + m.b10 - m.b13 - m.b25 - m.b37 - m.x145 + m.x146 == 0)

m.c4 = Constraint(expr=   m.b3 + m.b7 + m.b11 - m.b14 - m.b26 - m.b38 - m.x146 + m.x147 == 0)

m.c5 = Constraint(expr=   m.b4 + m.b8 + m.b12 - m.b15 - m.b27 - m.b39 - m.x147 + m.x148 == 0)

m.c6 = Constraint(expr= - m.b4 + m.b13 + m.b17 + m.b21 - m.b32 - m.b44 + m.x149 - m.x152 == 0)

m.c7 = Constraint(expr= - m.b1 + m.b14 + m.b18 + m.b22 - m.b29 - m.b41 - m.x149 + m.x150 == 0)

m.c8 = Constraint(expr= - m.b2 + m.b15 + m.b19 + m.b23 - m.b30 - m.b42 - m.x150 + m.x151 == 0)

m.c9 = Constraint(expr= - m.b3 + m.b16 + m.b20 + m.b24 - m.b31 - m.b43 - m.x151 + m.x152 == 0)

m.c10 = Constraint(expr= - m.b8 - m.b20 + m.b25 + m.b29 + m.b33 - m.b48 + m.x153 - m.x156 == 0)

m.c11 = Constraint(expr= - m.b5 - m.b17 + m.b26 + m.b30 + m.b34 - m.b45 - m.x153 + m.x154 == 0)

m.c12 = Constraint(expr= - m.b6 - m.b18 + m.b27 + m.b31 + m.b35 - m.b46 - m.x154 + m.x155 == 0)

m.c13 = Constraint(expr= - m.b7 - m.b19 + m.b28 + m.b32 + m.b36 - m.b47 - m.x155 + m.x156 == 0)

m.c14 = Constraint(expr= - m.b12 - m.b24 - m.b36 + m.b37 + m.b41 + m.b45 + m.x157 - m.x160 == 0)

m.c15 = Constraint(expr= - m.b9 - m.b21 - m.b33 + m.b38 + m.b42 + m.b46 - m.x157 + m.x158 == 0)

m.c16 = Constraint(expr= - m.b10 - m.b22 - m.b34 + m.b39 + m.b43 + m.b47 - m.x158 + m.x159 == 0)

m.c17 = Constraint(expr= - m.b11 - m.b23 - m.b35 + m.b40 + m.b44 + m.b48 - m.x159 + m.x160 == 0)

m.c18 = Constraint(expr=   m.b49 + m.b53 + m.b57 - m.b64 - m.b76 - m.b88 + m.x161 - m.x164 == 0)

m.c19 = Constraint(expr=   m.b50 + m.b54 + m.b58 - m.b61 - m.b73 - m.b85 - m.x161 + m.x162 == 0)

m.c20 = Constraint(expr=   m.b51 + m.b55 + m.b59 - m.b62 - m.b74 - m.b86 - m.x162 + m.x163 == 0)

m.c21 = Constraint(expr=   m.b52 + m.b56 + m.b60 - m.b63 - m.b75 - m.b87 - m.x163 + m.x164 == 0)

m.c22 = Constraint(expr= - m.b52 + m.b61 + m.b65 + m.b69 - m.b80 - m.b92 + m.x165 - m.x168 == 0)

m.c23 = Constraint(expr= - m.b49 + m.b62 + m.b66 + m.b70 - m.b77 - m.b89 - m.x165 + m.x166 == 0)

m.c24 = Constraint(expr= - m.b50 + m.b63 + m.b67 + m.b71 - m.b78 - m.b90 - m.x166 + m.x167 == 0)

m.c25 = Constraint(expr= - m.b51 + m.b64 + m.b68 + m.b72 - m.b79 - m.b91 - m.x167 + m.x168 == 0)

m.c26 = Constraint(expr= - m.b56 - m.b68 + m.b73 + m.b77 + m.b81 - m.b96 + m.x169 - m.x172 == 0)

m.c27 = Constraint(expr= - m.b53 - m.b65 + m.b74 + m.b78 + m.b82 - m.b93 - m.x169 + m.x170 == 0)

m.c28 = Constraint(expr= - m.b54 - m.b66 + m.b75 + m.b79 + m.b83 - m.b94 - m.x170 + m.x171 == 0)

m.c29 = Constraint(expr= - m.b55 - m.b67 + m.b76 + m.b80 + m.b84 - m.b95 - m.x171 + m.x172 == 0)

m.c30 = Constraint(expr= - m.b60 - m.b72 - m.b84 + m.b85 + m.b89 + m.b93 + m.x173 - m.x176 == 0)

m.c31 = Constraint(expr= - m.b57 - m.b69 - m.b81 + m.b86 + m.b90 + m.b94 - m.x173 + m.x174 == 0)

m.c32 = Constraint(expr= - m.b58 - m.b70 - m.b82 + m.b87 + m.b91 + m.b95 - m.x174 + m.x175 == 0)

m.c33 = Constraint(expr= - m.b59 - m.b71 - m.b83 + m.b88 + m.b92 + m.b96 - m.x175 + m.x176 == 0)

m.c34 = Constraint(expr=   m.b1 + m.b5 + m.b9 + m.b13 + m.b17 + m.b21 + m.b25 + m.b29 + m.b33 + m.b37 + m.b41 + m.b45
                         + m.x145 + m.x149 + m.x153 + m.x157 == 1)

m.c35 = Constraint(expr=   m.b49 + m.b53 + m.b57 + m.b61 + m.b65 + m.b69 + m.b73 + m.b77 + m.b81 + m.b85 + m.b89 + m.b93
                         + m.x161 + m.x165 + m.x169 + m.x173 == 1)

m.c36 = Constraint(expr= - 10*m.b1 - 10*m.b5 - 10*m.b9 - 10*m.b13 - m.b17 - 4*m.b21 - 10*m.b25 - m.b29 - 4*m.b33
                         - 10*m.b37 - 4*m.b41 - 4*m.b45 - 0.000854700854700855*m.x113 - 0.000746268656716418*m.x121
                         - 0.000746268656716418*m.x129 - 0.000826446280991736*m.x137 - m.x177 + m.x179 >= 0)

m.c37 = Constraint(expr= - 10*m.b2 - 10*m.b6 - 10*m.b10 - 10*m.b14 - m.b18 - 4*m.b22 - 10*m.b26 - m.b30 - 4*m.b34
                         - 10*m.b38 - 4*m.b42 - 4*m.b46 - 0.000854700854700855*m.x114 - 0.000746268656716418*m.x122
                         - 0.000746268656716418*m.x130 - 0.000826446280991736*m.x138 - m.x179 + m.x181 >= 0)

m.c38 = Constraint(expr= - 10*m.b3 - 10*m.b7 - 10*m.b11 - 10*m.b15 - m.b19 - 4*m.b23 - 10*m.b27 - m.b31 - 4*m.b35
                         - 10*m.b39 - 4*m.b43 - 4*m.b47 - 0.000854700854700855*m.x115 - 0.000746268656716418*m.x123
                         - 0.000746268656716418*m.x131 - 0.000826446280991736*m.x139 - m.x181 + m.x183 >= 0)

m.c39 = Constraint(expr= - 10*m.b4 - 10*m.b8 - 10*m.b12 - 10*m.b16 - m.b20 - 4*m.b24 - 10*m.b28 - m.b32 - 4*m.b36
                         - 10*m.b40 - 4*m.b44 - 4*m.b48 - 0.000854700854700855*m.x116 - 0.000746268656716418*m.x124
                         - 0.000746268656716418*m.x132 - 0.000826446280991736*m.x140 + m.x177 - m.x183 + m.x229 >= 0)

m.c40 = Constraint(expr= - 3*m.b49 - 3*m.b53 - 12*m.b57 - 3*m.b61 - m.b65 - 12*m.b69 - 3*m.b73 - m.b77 - 12*m.b81
                         - 12*m.b85 - 12*m.b89 - 12*m.b93 - 0.000892857142857143*m.x117 - 0.000775193798449612*m.x125
                         - 0.000746268656716418*m.x133 - 0.000862068965517241*m.x141 - m.x178 + m.x180 >= 0)

m.c41 = Constraint(expr= - 3*m.b50 - 3*m.b54 - 12*m.b58 - 3*m.b62 - m.b66 - 12*m.b70 - 3*m.b74 - m.b78 - 12*m.b82
                         - 12*m.b86 - 12*m.b90 - 12*m.b94 - 0.000892857142857143*m.x118 - 0.000775193798449612*m.x126
                         - 0.000746268656716418*m.x134 - 0.000862068965517241*m.x142 - m.x180 + m.x182 >= 0)

m.c42 = Constraint(expr= - 3*m.b51 - 3*m.b55 - 12*m.b59 - 3*m.b63 - m.b67 - 12*m.b71 - 3*m.b75 - m.b79 - 12*m.b83
                         - 12*m.b87 - 12*m.b91 - 12*m.b95 - 0.000892857142857143*m.x119 - 0.000775193798449612*m.x127
                         - 0.000746268656716418*m.x135 - 0.000862068965517241*m.x143 - m.x182 + m.x184 >= 0)

m.c43 = Constraint(expr= - 3*m.b52 - 3*m.b56 - 12*m.b60 - 3*m.b64 - m.b68 - 12*m.b72 - 3*m.b76 - m.b80 - 12*m.b84
                         - 12*m.b88 - 12*m.b92 - 12*m.b96 - 0.000892857142857143*m.x120 - 0.000775193798449612*m.x128
                         - 0.000746268656716418*m.x136 - 0.000862068965517241*m.x144 + m.x178 - m.x184 + m.x229 >= 0)

m.c44 = Constraint(expr= - 10*m.b1 - 10*m.b5 - 10*m.b9 - 10*m.b13 - m.b17 - 4*m.b21 - 10*m.b25 - m.b29 - 4*m.b33
                         - 10*m.b37 - 4*m.b41 - 4*m.b45 + m.x179 - m.x185 == 0)

m.c45 = Constraint(expr= - 10*m.b2 - 10*m.b6 - 10*m.b10 - 10*m.b14 - m.b18 - 4*m.b22 - 10*m.b26 - m.b30 - 4*m.b34
                         - 10*m.b38 - 4*m.b42 - 4*m.b46 + m.x181 - m.x187 == 0)

m.c46 = Constraint(expr= - 10*m.b3 - 10*m.b7 - 10*m.b11 - 10*m.b15 - m.b19 - 4*m.b23 - 10*m.b27 - m.b31 - 4*m.b35
                         - 10*m.b39 - 4*m.b43 - 4*m.b47 + m.x183 - m.x189 == 0)

m.c47 = Constraint(expr= - 10*m.b4 - 10*m.b8 - 10*m.b12 - 10*m.b16 - m.b20 - 4*m.b24 - 10*m.b28 - m.b32 - 4*m.b36
                         - 10*m.b40 - 4*m.b44 - 4*m.b48 + m.x177 - m.x191 + m.x229 == 0)

m.c48 = Constraint(expr= - 3*m.b49 - 3*m.b53 - 12*m.b57 - 3*m.b61 - m.b65 - 12*m.b69 - 3*m.b73 - m.b77 - 12*m.b81
                         - 12*m.b85 - 12*m.b89 - 12*m.b93 + m.x180 - m.x186 == 0)

m.c49 = Constraint(expr= - 3*m.b50 - 3*m.b54 - 12*m.b58 - 3*m.b62 - m.b66 - 12*m.b70 - 3*m.b74 - m.b78 - 12*m.b82
                         - 12*m.b86 - 12*m.b90 - 12*m.b94 + m.x182 - m.x188 == 0)

m.c50 = Constraint(expr= - 3*m.b51 - 3*m.b55 - 12*m.b59 - 3*m.b63 - m.b67 - 12*m.b71 - 3*m.b75 - m.b79 - 12*m.b83
                         - 12*m.b87 - 12*m.b91 - 12*m.b95 + m.x184 - m.x190 == 0)

m.c51 = Constraint(expr= - 3*m.b52 - 3*m.b56 - 12*m.b60 - 3*m.b64 - m.b68 - 12*m.b72 - 3*m.b76 - m.b80 - 12*m.b84
                         - 12*m.b88 - 12*m.b92 - 12*m.b96 + m.x178 - m.x192 + m.x229 == 0)

m.c52 = Constraint(expr=   m.x183 - m.x229 <= 0)

m.c53 = Constraint(expr=   m.x184 - m.x229 <= 0)

m.c54 = Constraint(expr= - 936000*m.b1 - 936000*m.b5 - 936000*m.b9 + m.x113 <= 0)

m.c55 = Constraint(expr= - 936000*m.b2 - 936000*m.b6 - 936000*m.b10 + m.x114 <= 0)

m.c56 = Constraint(expr= - 936000*m.b3 - 936000*m.b7 - 936000*m.b11 + m.x115 <= 0)

m.c57 = Constraint(expr= - 936000*m.b4 - 936000*m.b8 - 936000*m.b12 + m.x116 <= 0)

m.c58 = Constraint(expr= - 896000*m.b49 - 896000*m.b53 - 896000*m.b57 + m.x117 <= 0)

m.c59 = Constraint(expr= - 896000*m.b50 - 896000*m.b54 - 896000*m.b58 + m.x118 <= 0)

m.c60 = Constraint(expr= - 896000*m.b51 - 896000*m.b55 - 896000*m.b59 + m.x119 <= 0)

m.c61 = Constraint(expr= - 896000*m.b52 - 896000*m.b56 - 896000*m.b60 + m.x120 <= 0)

m.c62 = Constraint(expr= - 1072000*m.b13 - 1072000*m.b17 - 1072000*m.b21 + m.x121 <= 0)

m.c63 = Constraint(expr= - 1072000*m.b14 - 1072000*m.b18 - 1072000*m.b22 + m.x122 <= 0)

m.c64 = Constraint(expr= - 1072000*m.b15 - 1072000*m.b19 - 1072000*m.b23 + m.x123 <= 0)

m.c65 = Constraint(expr= - 1072000*m.b16 - 1072000*m.b20 - 1072000*m.b24 + m.x124 <= 0)

m.c66 = Constraint(expr= - 1032000*m.b61 - 1032000*m.b65 - 1032000*m.b69 + m.x125 <= 0)

m.c67 = Constraint(expr= - 1032000*m.b62 - 1032000*m.b66 - 1032000*m.b70 + m.x126 <= 0)

m.c68 = Constraint(expr= - 1032000*m.b63 - 1032000*m.b67 - 1032000*m.b71 + m.x127 <= 0)

m.c69 = Constraint(expr= - 1032000*m.b64 - 1032000*m.b68 - 1032000*m.b72 + m.x128 <= 0)

m.c70 = Constraint(expr= - 1072000*m.b25 - 1072000*m.b29 - 1072000*m.b33 + m.x129 <= 0)

m.c71 = Constraint(expr= - 1072000*m.b26 - 1072000*m.b30 - 1072000*m.b34 + m.x130 <= 0)

m.c72 = Constraint(expr= - 1072000*m.b27 - 1072000*m.b31 - 1072000*m.b35 + m.x131 <= 0)

m.c73 = Constraint(expr= - 1072000*m.b28 - 1072000*m.b32 - 1072000*m.b36 + m.x132 <= 0)

m.c74 = Constraint(expr= - 1072000*m.b73 - 1072000*m.b77 - 1072000*m.b81 + m.x133 <= 0)

m.c75 = Constraint(expr= - 1072000*m.b74 - 1072000*m.b78 - 1072000*m.b82 + m.x134 <= 0)

m.c76 = Constraint(expr= - 1072000*m.b75 - 1072000*m.b79 - 1072000*m.b83 + m.x135 <= 0)

m.c77 = Constraint(expr= - 1072000*m.b76 - 1072000*m.b80 - 1072000*m.b84 + m.x136 <= 0)

m.c78 = Constraint(expr= - 968000*m.b37 - 968000*m.b41 - 968000*m.b45 + m.x137 <= 0)

m.c79 = Constraint(expr= - 968000*m.b38 - 968000*m.b42 - 968000*m.b46 + m.x138 <= 0)

m.c80 = Constraint(expr= - 968000*m.b39 - 968000*m.b43 - 968000*m.b47 + m.x139 <= 0)

m.c81 = Constraint(expr= - 968000*m.b40 - 968000*m.b44 - 968000*m.b48 + m.x140 <= 0)

m.c82 = Constraint(expr= - 928000*m.b85 - 928000*m.b89 - 928000*m.b93 + m.x141 <= 0)

m.c83 = Constraint(expr= - 928000*m.b86 - 928000*m.b90 - 928000*m.b94 + m.x142 <= 0)

m.c84 = Constraint(expr= - 928000*m.b87 - 928000*m.b91 - 928000*m.b95 + m.x143 <= 0)

m.c85 = Constraint(expr= - 928000*m.b88 - 928000*m.b92 - 928000*m.b96 + m.x144 <= 0)

m.c86 = Constraint(expr=   m.b1 + m.b2 + m.b3 + m.b4 + m.b5 + m.b6 + m.b7 + m.b8 + m.b9 + m.b10 + m.b11 + m.b12 == 1)

m.c87 = Constraint(expr=   m.b49 + m.b50 + m.b51 + m.b52 + m.b53 + m.b54 + m.b55 + m.b56 + m.b57 + m.b58 + m.b59 + m.b60
                         == 1)

m.c88 = Constraint(expr=   m.b13 + m.b14 + m.b15 + m.b16 + m.b17 + m.b18 + m.b19 + m.b20 + m.b21 + m.b22 + m.b23 + m.b24
                         == 1)

m.c89 = Constraint(expr=   m.b61 + m.b62 + m.b63 + m.b64 + m.b65 + m.b66 + m.b67 + m.b68 + m.b69 + m.b70 + m.b71 + m.b72
                         == 1)

m.c90 = Constraint(expr=   m.b25 + m.b26 + m.b27 + m.b28 + m.b29 + m.b30 + m.b31 + m.b32 + m.b33 + m.b34 + m.b35 + m.b36
                         == 1)

m.c91 = Constraint(expr=   m.b73 + m.b74 + m.b75 + m.b76 + m.b77 + m.b78 + m.b79 + m.b80 + m.b81 + m.b82 + m.b83 + m.b84
                         == 1)

m.c92 = Constraint(expr=   m.b37 + m.b38 + m.b39 + m.b40 + m.b41 + m.b42 + m.b43 + m.b44 + m.b45 + m.b46 + m.b47 + m.b48
                         == 1)

m.c93 = Constraint(expr=   m.b85 + m.b86 + m.b87 + m.b88 + m.b89 + m.b90 + m.b91 + m.b92 + m.b93 + m.b94 + m.b95 + m.b96
                         == 1)

m.c94 = Constraint(expr=   m.b1 + m.b5 + m.b9 == 1)

m.c95 = Constraint(expr=m.x213*m.x229 - m.x117 - m.x118 - m.x119 - m.x120 == 0)

m.c96 = Constraint(expr=m.x214*m.x229 - m.x125 - m.x126 - m.x127 - m.x128 == 0)

m.c97 = Constraint(expr=m.x215*m.x229 - m.x133 - m.x134 - m.x135 - m.x136 == 0)

m.c98 = Constraint(expr=m.x216*m.x229 - m.x141 - m.x142 - m.x143 - m.x144 == 0)

m.c99 = Constraint(expr=   m.x113 + m.x114 + m.x115 + m.x116 - m.x117 - m.x118 - m.x119 - m.x120 == 0)

m.c100 = Constraint(expr=   m.x121 + m.x122 + m.x123 + m.x124 - m.x125 - m.x126 - m.x127 - m.x128 == 0)

m.c101 = Constraint(expr=   m.x129 + m.x130 + m.x131 + m.x132 - m.x133 - m.x134 - m.x135 - m.x136 == 0)

m.c102 = Constraint(expr=   m.x137 + m.x138 + m.x139 + m.x140 - m.x141 - m.x142 - m.x143 - m.x144 == 0)

m.c103 = Constraint(expr=   800*m.b1 + 800*m.b5 + 800*m.b9 - m.x177 + m.x197 <= 800)

m.c104 = Constraint(expr=   800*m.b1 + 800*m.b2 + 800*m.b5 + 800*m.b6 + 800*m.b9 + 800*m.b10 - m.x179 + m.x197 <= 800)

m.c105 = Constraint(expr=   800*m.b1 + 800*m.b2 + 800*m.b3 + 800*m.b5 + 800*m.b6 + 800*m.b7 + 800*m.b9 + 800*m.b10
                          + 800*m.b11 - m.x181 + m.x197 <= 800)

m.c106 = Constraint(expr=   800*m.b1 + 800*m.b2 + 800*m.b3 + 800*m.b4 + 800*m.b5 + 800*m.b6 + 800*m.b7 + 800*m.b8
                          + 800*m.b9 + 800*m.b10 + 800*m.b11 + 800*m.b12 - m.x183 + m.x197 <= 800)

m.c107 = Constraint(expr=   800*m.b49 + 800*m.b53 + 800*m.b57 - m.x178 + m.x198 <= 800)

m.c108 = Constraint(expr=   800*m.b49 + 800*m.b50 + 800*m.b53 + 800*m.b54 + 800*m.b57 + 800*m.b58 - m.x180 + m.x198
                          <= 800)

m.c109 = Constraint(expr=   800*m.b49 + 800*m.b50 + 800*m.b51 + 800*m.b53 + 800*m.b54 + 800*m.b55 + 800*m.b57
                          + 800*m.b58 + 800*m.b59 - m.x182 + m.x198 <= 800)

m.c110 = Constraint(expr=   800*m.b49 + 800*m.b50 + 800*m.b51 + 800*m.b52 + 800*m.b53 + 800*m.b54 + 800*m.b55
                          + 800*m.b56 + 800*m.b57 + 800*m.b58 + 800*m.b59 + 800*m.b60 - m.x184 + m.x198 <= 800)

m.c111 = Constraint(expr=   800*m.b13 + 800*m.b17 + 800*m.b21 - m.x177 + m.x199 <= 800)

m.c112 = Constraint(expr=   800*m.b13 + 800*m.b14 + 800*m.b17 + 800*m.b18 + 800*m.b21 + 800*m.b22 - m.x179 + m.x199
                          <= 800)

m.c113 = Constraint(expr=   800*m.b13 + 800*m.b14 + 800*m.b15 + 800*m.b17 + 800*m.b18 + 800*m.b19 + 800*m.b21
                          + 800*m.b22 + 800*m.b23 - m.x181 + m.x199 <= 800)

m.c114 = Constraint(expr=   800*m.b13 + 800*m.b14 + 800*m.b15 + 800*m.b16 + 800*m.b17 + 800*m.b18 + 800*m.b19
                          + 800*m.b20 + 800*m.b21 + 800*m.b22 + 800*m.b23 + 800*m.b24 - m.x183 + m.x199 <= 800)

m.c115 = Constraint(expr=   800*m.b61 + 800*m.b65 + 800*m.b69 - m.x178 + m.x200 <= 800)

m.c116 = Constraint(expr=   800*m.b61 + 800*m.b62 + 800*m.b65 + 800*m.b66 + 800*m.b69 + 800*m.b70 - m.x180 + m.x200
                          <= 800)

m.c117 = Constraint(expr=   800*m.b61 + 800*m.b62 + 800*m.b63 + 800*m.b65 + 800*m.b66 + 800*m.b67 + 800*m.b69
                          + 800*m.b70 + 800*m.b71 - m.x182 + m.x200 <= 800)

m.c118 = Constraint(expr=   800*m.b61 + 800*m.b62 + 800*m.b63 + 800*m.b64 + 800*m.b65 + 800*m.b66 + 800*m.b67
                          + 800*m.b68 + 800*m.b69 + 800*m.b70 + 800*m.b71 + 800*m.b72 - m.x184 + m.x200 <= 800)

m.c119 = Constraint(expr=   800*m.b25 + 800*m.b29 + 800*m.b33 - m.x177 + m.x201 <= 800)

m.c120 = Constraint(expr=   800*m.b25 + 800*m.b26 + 800*m.b29 + 800*m.b30 + 800*m.b33 + 800*m.b34 - m.x179 + m.x201
                          <= 800)

m.c121 = Constraint(expr=   800*m.b25 + 800*m.b26 + 800*m.b27 + 800*m.b29 + 800*m.b30 + 800*m.b31 + 800*m.b33
                          + 800*m.b34 + 800*m.b35 - m.x181 + m.x201 <= 800)

m.c122 = Constraint(expr=   800*m.b25 + 800*m.b26 + 800*m.b27 + 800*m.b28 + 800*m.b29 + 800*m.b30 + 800*m.b31
                          + 800*m.b32 + 800*m.b33 + 800*m.b34 + 800*m.b35 + 800*m.b36 - m.x183 + m.x201 <= 800)

m.c123 = Constraint(expr=   800*m.b73 + 800*m.b77 + 800*m.b81 - m.x178 + m.x202 <= 800)

m.c124 = Constraint(expr=   800*m.b73 + 800*m.b74 + 800*m.b77 + 800*m.b78 + 800*m.b81 + 800*m.b82 - m.x180 + m.x202
                          <= 800)

m.c125 = Constraint(expr=   800*m.b73 + 800*m.b74 + 800*m.b75 + 800*m.b77 + 800*m.b78 + 800*m.b79 + 800*m.b81
                          + 800*m.b82 + 800*m.b83 - m.x182 + m.x202 <= 800)

m.c126 = Constraint(expr=   800*m.b73 + 800*m.b74 + 800*m.b75 + 800*m.b76 + 800*m.b77 + 800*m.b78 + 800*m.b79
                          + 800*m.b80 + 800*m.b81 + 800*m.b82 + 800*m.b83 + 800*m.b84 - m.x184 + m.x202 <= 800)

m.c127 = Constraint(expr=   800*m.b37 + 800*m.b41 + 800*m.b45 - m.x177 + m.x203 <= 800)

m.c128 = Constraint(expr=   800*m.b37 + 800*m.b38 + 800*m.b41 + 800*m.b42 + 800*m.b45 + 800*m.b46 - m.x179 + m.x203
                          <= 800)

m.c129 = Constraint(expr=   800*m.b37 + 800*m.b38 + 800*m.b39 + 800*m.b41 + 800*m.b42 + 800*m.b43 + 800*m.b45
                          + 800*m.b46 + 800*m.b47 - m.x181 + m.x203 <= 800)

m.c130 = Constraint(expr=   800*m.b37 + 800*m.b38 + 800*m.b39 + 800*m.b40 + 800*m.b41 + 800*m.b42 + 800*m.b43
                          + 800*m.b44 + 800*m.b45 + 800*m.b46 + 800*m.b47 + 800*m.b48 - m.x183 + m.x203 <= 800)

m.c131 = Constraint(expr=   800*m.b85 + 800*m.b89 + 800*m.b93 - m.x178 + m.x204 <= 800)

m.c132 = Constraint(expr=   800*m.b85 + 800*m.b86 + 800*m.b89 + 800*m.b90 + 800*m.b93 + 800*m.b94 - m.x180 + m.x204
                          <= 800)

m.c133 = Constraint(expr=   800*m.b85 + 800*m.b86 + 800*m.b87 + 800*m.b89 + 800*m.b90 + 800*m.b91 + 800*m.b93
                          + 800*m.b94 + 800*m.b95 - m.x182 + m.x204 <= 800)

m.c134 = Constraint(expr=   800*m.b85 + 800*m.b86 + 800*m.b87 + 800*m.b88 + 800*m.b89 + 800*m.b90 + 800*m.b91
                          + 800*m.b92 + 800*m.b93 + 800*m.b94 + 800*m.b95 + 800*m.b96 - m.x184 + m.x204 <= 800)

m.c135 = Constraint(expr= - 800*m.b1 - 800*m.b2 - 800*m.b3 - 800*m.b4 - 800*m.b5 - 800*m.b6 - 800*m.b7 - 800*m.b8
                          - 800*m.b9 - 800*m.b10 - 800*m.b11 - 800*m.b12 - m.x177 + m.x197 >= -800)

m.c136 = Constraint(expr= - 800*m.b2 - 800*m.b3 - 800*m.b4 - 800*m.b6 - 800*m.b7 - 800*m.b8 - 800*m.b10 - 800*m.b11
                          - 800*m.b12 - m.x179 + m.x197 >= -800)

m.c137 = Constraint(expr= - 800*m.b3 - 800*m.b4 - 800*m.b7 - 800*m.b8 - 800*m.b11 - 800*m.b12 - m.x181 + m.x197 >= -800)

m.c138 = Constraint(expr= - 800*m.b4 - 800*m.b8 - 800*m.b12 - m.x183 + m.x197 >= -800)

m.c139 = Constraint(expr= - 800*m.b49 - 800*m.b50 - 800*m.b51 - 800*m.b52 - 800*m.b53 - 800*m.b54 - 800*m.b55
                          - 800*m.b56 - 800*m.b57 - 800*m.b58 - 800*m.b59 - 800*m.b60 - m.x178 + m.x198 >= -800)

m.c140 = Constraint(expr= - 800*m.b50 - 800*m.b51 - 800*m.b52 - 800*m.b54 - 800*m.b55 - 800*m.b56 - 800*m.b58
                          - 800*m.b59 - 800*m.b60 - m.x180 + m.x198 >= -800)

m.c141 = Constraint(expr= - 800*m.b51 - 800*m.b52 - 800*m.b55 - 800*m.b56 - 800*m.b59 - 800*m.b60 - m.x182 + m.x198
                          >= -800)

m.c142 = Constraint(expr= - 800*m.b52 - 800*m.b56 - 800*m.b60 - m.x184 + m.x198 >= -800)

m.c143 = Constraint(expr= - 800*m.b13 - 800*m.b14 - 800*m.b15 - 800*m.b16 - 800*m.b17 - 800*m.b18 - 800*m.b19
                          - 800*m.b20 - 800*m.b21 - 800*m.b22 - 800*m.b23 - 800*m.b24 - m.x177 + m.x199 >= -800)

m.c144 = Constraint(expr= - 800*m.b14 - 800*m.b15 - 800*m.b16 - 800*m.b18 - 800*m.b19 - 800*m.b20 - 800*m.b22
                          - 800*m.b23 - 800*m.b24 - m.x179 + m.x199 >= -800)

m.c145 = Constraint(expr= - 800*m.b15 - 800*m.b16 - 800*m.b19 - 800*m.b20 - 800*m.b23 - 800*m.b24 - m.x181 + m.x199
                          >= -800)

m.c146 = Constraint(expr= - 800*m.b16 - 800*m.b20 - 800*m.b24 - m.x183 + m.x199 >= -800)

m.c147 = Constraint(expr= - 800*m.b61 - 800*m.b62 - 800*m.b63 - 800*m.b64 - 800*m.b65 - 800*m.b66 - 800*m.b67
                          - 800*m.b68 - 800*m.b69 - 800*m.b70 - 800*m.b71 - 800*m.b72 - m.x178 + m.x200 >= -800)

m.c148 = Constraint(expr= - 800*m.b62 - 800*m.b63 - 800*m.b64 - 800*m.b66 - 800*m.b67 - 800*m.b68 - 800*m.b70
                          - 800*m.b71 - 800*m.b72 - m.x180 + m.x200 >= -800)

m.c149 = Constraint(expr= - 800*m.b63 - 800*m.b64 - 800*m.b67 - 800*m.b68 - 800*m.b71 - 800*m.b72 - m.x182 + m.x200
                          >= -800)

m.c150 = Constraint(expr= - 800*m.b64 - 800*m.b68 - 800*m.b72 - m.x184 + m.x200 >= -800)

m.c151 = Constraint(expr= - 800*m.b25 - 800*m.b26 - 800*m.b27 - 800*m.b28 - 800*m.b29 - 800*m.b30 - 800*m.b31
                          - 800*m.b32 - 800*m.b33 - 800*m.b34 - 800*m.b35 - 800*m.b36 - m.x177 + m.x201 >= -800)

m.c152 = Constraint(expr= - 800*m.b26 - 800*m.b27 - 800*m.b28 - 800*m.b30 - 800*m.b31 - 800*m.b32 - 800*m.b34
                          - 800*m.b35 - 800*m.b36 - m.x179 + m.x201 >= -800)

m.c153 = Constraint(expr= - 800*m.b27 - 800*m.b28 - 800*m.b31 - 800*m.b32 - 800*m.b35 - 800*m.b36 - m.x181 + m.x201
                          >= -800)

m.c154 = Constraint(expr= - 800*m.b28 - 800*m.b32 - 800*m.b36 - m.x183 + m.x201 >= -800)

m.c155 = Constraint(expr= - 800*m.b73 - 800*m.b74 - 800*m.b75 - 800*m.b76 - 800*m.b77 - 800*m.b78 - 800*m.b79
                          - 800*m.b80 - 800*m.b81 - 800*m.b82 - 800*m.b83 - 800*m.b84 - m.x178 + m.x202 >= -800)

m.c156 = Constraint(expr= - 800*m.b74 - 800*m.b75 - 800*m.b76 - 800*m.b78 - 800*m.b79 - 800*m.b80 - 800*m.b82
                          - 800*m.b83 - 800*m.b84 - m.x180 + m.x202 >= -800)

m.c157 = Constraint(expr= - 800*m.b75 - 800*m.b76 - 800*m.b79 - 800*m.b80 - 800*m.b83 - 800*m.b84 - m.x182 + m.x202
                          >= -800)

m.c158 = Constraint(expr= - 800*m.b76 - 800*m.b80 - 800*m.b84 - m.x184 + m.x202 >= -800)

m.c159 = Constraint(expr= - 800*m.b37 - 800*m.b38 - 800*m.b39 - 800*m.b40 - 800*m.b41 - 800*m.b42 - 800*m.b43
                          - 800*m.b44 - 800*m.b45 - 800*m.b46 - 800*m.b47 - 800*m.b48 - m.x177 + m.x203 >= -800)

m.c160 = Constraint(expr= - 800*m.b38 - 800*m.b39 - 800*m.b40 - 800*m.b42 - 800*m.b43 - 800*m.b44 - 800*m.b46
                          - 800*m.b47 - 800*m.b48 - m.x179 + m.x203 >= -800)

m.c161 = Constraint(expr= - 800*m.b39 - 800*m.b40 - 800*m.b43 - 800*m.b44 - 800*m.b47 - 800*m.b48 - m.x181 + m.x203
                          >= -800)

m.c162 = Constraint(expr= - 800*m.b40 - 800*m.b44 - 800*m.b48 - m.x183 + m.x203 >= -800)

m.c163 = Constraint(expr= - 800*m.b85 - 800*m.b86 - 800*m.b87 - 800*m.b88 - 800*m.b89 - 800*m.b90 - 800*m.b91
                          - 800*m.b92 - 800*m.b93 - 800*m.b94 - 800*m.b95 - 800*m.b96 - m.x178 + m.x204 >= -800)

m.c164 = Constraint(expr= - 800*m.b86 - 800*m.b87 - 800*m.b88 - 800*m.b90 - 800*m.b91 - 800*m.b92 - 800*m.b94
                          - 800*m.b95 - 800*m.b96 - m.x180 + m.x204 >= -800)

m.c165 = Constraint(expr= - 800*m.b87 - 800*m.b88 - 800*m.b91 - 800*m.b92 - 800*m.b95 - 800*m.b96 - m.x182 + m.x204
                          >= -800)

m.c166 = Constraint(expr= - 800*m.b88 - 800*m.b92 - 800*m.b96 - m.x184 + m.x204 >= -800)

m.c167 = Constraint(expr=   800*m.b1 + 800*m.b5 + 800*m.b9 - m.x185 + m.x205 <= 800)

m.c168 = Constraint(expr=   800*m.b1 + 800*m.b2 + 800*m.b5 + 800*m.b6 + 800*m.b9 + 800*m.b10 - m.x187 + m.x205 <= 800)

m.c169 = Constraint(expr=   800*m.b1 + 800*m.b2 + 800*m.b3 + 800*m.b5 + 800*m.b6 + 800*m.b7 + 800*m.b9 + 800*m.b10
                          + 800*m.b11 - m.x189 + m.x205 <= 800)

m.c170 = Constraint(expr=   800*m.b1 + 800*m.b2 + 800*m.b3 + 800*m.b4 + 800*m.b5 + 800*m.b6 + 800*m.b7 + 800*m.b8
                          + 800*m.b9 + 800*m.b10 + 800*m.b11 + 800*m.b12 - m.x191 + m.x205 <= 800)

m.c171 = Constraint(expr=   800*m.b49 + 800*m.b53 + 800*m.b57 - m.x186 + m.x206 <= 800)

m.c172 = Constraint(expr=   800*m.b49 + 800*m.b50 + 800*m.b53 + 800*m.b54 + 800*m.b57 + 800*m.b58 - m.x188 + m.x206
                          <= 800)

m.c173 = Constraint(expr=   800*m.b49 + 800*m.b50 + 800*m.b51 + 800*m.b53 + 800*m.b54 + 800*m.b55 + 800*m.b57
                          + 800*m.b58 + 800*m.b59 - m.x190 + m.x206 <= 800)

m.c174 = Constraint(expr=   800*m.b49 + 800*m.b50 + 800*m.b51 + 800*m.b52 + 800*m.b53 + 800*m.b54 + 800*m.b55
                          + 800*m.b56 + 800*m.b57 + 800*m.b58 + 800*m.b59 + 800*m.b60 - m.x192 + m.x206 <= 800)

m.c175 = Constraint(expr=   800*m.b13 + 800*m.b17 + 800*m.b21 - m.x185 + m.x207 <= 800)

m.c176 = Constraint(expr=   800*m.b13 + 800*m.b14 + 800*m.b17 + 800*m.b18 + 800*m.b21 + 800*m.b22 - m.x187 + m.x207
                          <= 800)

m.c177 = Constraint(expr=   800*m.b13 + 800*m.b14 + 800*m.b15 + 800*m.b17 + 800*m.b18 + 800*m.b19 + 800*m.b21
                          + 800*m.b22 + 800*m.b23 - m.x189 + m.x207 <= 800)

m.c178 = Constraint(expr=   800*m.b13 + 800*m.b14 + 800*m.b15 + 800*m.b16 + 800*m.b17 + 800*m.b18 + 800*m.b19
                          + 800*m.b20 + 800*m.b21 + 800*m.b22 + 800*m.b23 + 800*m.b24 - m.x191 + m.x207 <= 800)

m.c179 = Constraint(expr=   800*m.b61 + 800*m.b65 + 800*m.b69 - m.x186 + m.x208 <= 800)

m.c180 = Constraint(expr=   800*m.b61 + 800*m.b62 + 800*m.b65 + 800*m.b66 + 800*m.b69 + 800*m.b70 - m.x188 + m.x208
                          <= 800)

m.c181 = Constraint(expr=   800*m.b61 + 800*m.b62 + 800*m.b63 + 800*m.b65 + 800*m.b66 + 800*m.b67 + 800*m.b69
                          + 800*m.b70 + 800*m.b71 - m.x190 + m.x208 <= 800)

m.c182 = Constraint(expr=   800*m.b61 + 800*m.b62 + 800*m.b63 + 800*m.b64 + 800*m.b65 + 800*m.b66 + 800*m.b67
                          + 800*m.b68 + 800*m.b69 + 800*m.b70 + 800*m.b71 + 800*m.b72 - m.x192 + m.x208 <= 800)

m.c183 = Constraint(expr=   800*m.b25 + 800*m.b29 + 800*m.b33 - m.x185 + m.x209 <= 800)

m.c184 = Constraint(expr=   800*m.b25 + 800*m.b26 + 800*m.b29 + 800*m.b30 + 800*m.b33 + 800*m.b34 - m.x187 + m.x209
                          <= 800)

m.c185 = Constraint(expr=   800*m.b25 + 800*m.b26 + 800*m.b27 + 800*m.b29 + 800*m.b30 + 800*m.b31 + 800*m.b33
                          + 800*m.b34 + 800*m.b35 - m.x189 + m.x209 <= 800)

m.c186 = Constraint(expr=   800*m.b25 + 800*m.b26 + 800*m.b27 + 800*m.b28 + 800*m.b29 + 800*m.b30 + 800*m.b31
                          + 800*m.b32 + 800*m.b33 + 800*m.b34 + 800*m.b35 + 800*m.b36 - m.x191 + m.x209 <= 800)

m.c187 = Constraint(expr=   800*m.b73 + 800*m.b77 + 800*m.b81 - m.x186 + m.x210 <= 800)

m.c188 = Constraint(expr=   800*m.b73 + 800*m.b74 + 800*m.b77 + 800*m.b78 + 800*m.b81 + 800*m.b82 - m.x188 + m.x210
                          <= 800)

m.c189 = Constraint(expr=   800*m.b73 + 800*m.b74 + 800*m.b75 + 800*m.b77 + 800*m.b78 + 800*m.b79 + 800*m.b81
                          + 800*m.b82 + 800*m.b83 - m.x190 + m.x210 <= 800)

m.c190 = Constraint(expr=   800*m.b73 + 800*m.b74 + 800*m.b75 + 800*m.b76 + 800*m.b77 + 800*m.b78 + 800*m.b79
                          + 800*m.b80 + 800*m.b81 + 800*m.b82 + 800*m.b83 + 800*m.b84 - m.x192 + m.x210 <= 800)

m.c191 = Constraint(expr=   800*m.b37 + 800*m.b41 + 800*m.b45 - m.x185 + m.x211 <= 800)

m.c192 = Constraint(expr=   800*m.b37 + 800*m.b38 + 800*m.b41 + 800*m.b42 + 800*m.b45 + 800*m.b46 - m.x187 + m.x211
                          <= 800)

m.c193 = Constraint(expr=   800*m.b37 + 800*m.b38 + 800*m.b39 + 800*m.b41 + 800*m.b42 + 800*m.b43 + 800*m.b45
                          + 800*m.b46 + 800*m.b47 - m.x189 + m.x211 <= 800)

m.c194 = Constraint(expr=   800*m.b37 + 800*m.b38 + 800*m.b39 + 800*m.b40 + 800*m.b41 + 800*m.b42 + 800*m.b43
                          + 800*m.b44 + 800*m.b45 + 800*m.b46 + 800*m.b47 + 800*m.b48 - m.x191 + m.x211 <= 800)

m.c195 = Constraint(expr=   800*m.b85 + 800*m.b89 + 800*m.b93 - m.x186 + m.x212 <= 800)

m.c196 = Constraint(expr=   800*m.b85 + 800*m.b86 + 800*m.b89 + 800*m.b90 + 800*m.b93 + 800*m.b94 - m.x188 + m.x212
                          <= 800)

m.c197 = Constraint(expr=   800*m.b85 + 800*m.b86 + 800*m.b87 + 800*m.b89 + 800*m.b90 + 800*m.b91 + 800*m.b93
                          + 800*m.b94 + 800*m.b95 - m.x190 + m.x212 <= 800)

m.c198 = Constraint(expr=   800*m.b85 + 800*m.b86 + 800*m.b87 + 800*m.b88 + 800*m.b89 + 800*m.b90 + 800*m.b91
                          + 800*m.b92 + 800*m.b93 + 800*m.b94 + 800*m.b95 + 800*m.b96 - m.x192 + m.x212 <= 800)

m.c199 = Constraint(expr= - 800*m.b1 - 800*m.b2 - 800*m.b3 - 800*m.b4 - 800*m.b5 - 800*m.b6 - 800*m.b7 - 800*m.b8
                          - 800*m.b9 - 800*m.b10 - 800*m.b11 - 800*m.b12 - m.x185 + m.x205 >= -800)

m.c200 = Constraint(expr= - 800*m.b2 - 800*m.b3 - 800*m.b4 - 800*m.b6 - 800*m.b7 - 800*m.b8 - 800*m.b10 - 800*m.b11
                          - 800*m.b12 - m.x187 + m.x205 >= -800)

m.c201 = Constraint(expr= - 800*m.b3 - 800*m.b4 - 800*m.b7 - 800*m.b8 - 800*m.b11 - 800*m.b12 - m.x189 + m.x205 >= -800)

m.c202 = Constraint(expr= - 800*m.b4 - 800*m.b8 - 800*m.b12 - m.x191 + m.x205 >= -800)

m.c203 = Constraint(expr= - 800*m.b49 - 800*m.b50 - 800*m.b51 - 800*m.b52 - 800*m.b53 - 800*m.b54 - 800*m.b55
                          - 800*m.b56 - 800*m.b57 - 800*m.b58 - 800*m.b59 - 800*m.b60 - m.x186 + m.x206 >= -800)

m.c204 = Constraint(expr= - 800*m.b50 - 800*m.b51 - 800*m.b52 - 800*m.b54 - 800*m.b55 - 800*m.b56 - 800*m.b58
                          - 800*m.b59 - 800*m.b60 - m.x188 + m.x206 >= -800)

m.c205 = Constraint(expr= - 800*m.b51 - 800*m.b52 - 800*m.b55 - 800*m.b56 - 800*m.b59 - 800*m.b60 - m.x190 + m.x206
                          >= -800)

m.c206 = Constraint(expr= - 800*m.b52 - 800*m.b56 - 800*m.b60 - m.x192 + m.x206 >= -800)

m.c207 = Constraint(expr= - 800*m.b13 - 800*m.b14 - 800*m.b15 - 800*m.b16 - 800*m.b17 - 800*m.b18 - 800*m.b19
                          - 800*m.b20 - 800*m.b21 - 800*m.b22 - 800*m.b23 - 800*m.b24 - m.x185 + m.x207 >= -800)

m.c208 = Constraint(expr= - 800*m.b14 - 800*m.b15 - 800*m.b16 - 800*m.b18 - 800*m.b19 - 800*m.b20 - 800*m.b22
                          - 800*m.b23 - 800*m.b24 - m.x187 + m.x207 >= -800)

m.c209 = Constraint(expr= - 800*m.b15 - 800*m.b16 - 800*m.b19 - 800*m.b20 - 800*m.b23 - 800*m.b24 - m.x189 + m.x207
                          >= -800)

m.c210 = Constraint(expr= - 800*m.b16 - 800*m.b20 - 800*m.b24 - m.x191 + m.x207 >= -800)

m.c211 = Constraint(expr= - 800*m.b61 - 800*m.b62 - 800*m.b63 - 800*m.b64 - 800*m.b65 - 800*m.b66 - 800*m.b67
                          - 800*m.b68 - 800*m.b69 - 800*m.b70 - 800*m.b71 - 800*m.b72 - m.x186 + m.x208 >= -800)

m.c212 = Constraint(expr= - 800*m.b62 - 800*m.b63 - 800*m.b64 - 800*m.b66 - 800*m.b67 - 800*m.b68 - 800*m.b70
                          - 800*m.b71 - 800*m.b72 - m.x188 + m.x208 >= -800)

m.c213 = Constraint(expr= - 800*m.b63 - 800*m.b64 - 800*m.b67 - 800*m.b68 - 800*m.b71 - 800*m.b72 - m.x190 + m.x208
                          >= -800)

m.c214 = Constraint(expr= - 800*m.b64 - 800*m.b68 - 800*m.b72 - m.x192 + m.x208 >= -800)

m.c215 = Constraint(expr= - 800*m.b25 - 800*m.b26 - 800*m.b27 - 800*m.b28 - 800*m.b29 - 800*m.b30 - 800*m.b31
                          - 800*m.b32 - 800*m.b33 - 800*m.b34 - 800*m.b35 - 800*m.b36 - m.x185 + m.x209 >= -800)

m.c216 = Constraint(expr= - 800*m.b26 - 800*m.b27 - 800*m.b28 - 800*m.b30 - 800*m.b31 - 800*m.b32 - 800*m.b34
                          - 800*m.b35 - 800*m.b36 - m.x187 + m.x209 >= -800)

m.c217 = Constraint(expr= - 800*m.b27 - 800*m.b28 - 800*m.b31 - 800*m.b32 - 800*m.b35 - 800*m.b36 - m.x189 + m.x209
                          >= -800)

m.c218 = Constraint(expr= - 800*m.b28 - 800*m.b32 - 800*m.b36 - m.x191 + m.x209 >= -800)

m.c219 = Constraint(expr= - 800*m.b73 - 800*m.b74 - 800*m.b75 - 800*m.b76 - 800*m.b77 - 800*m.b78 - 800*m.b79
                          - 800*m.b80 - 800*m.b81 - 800*m.b82 - 800*m.b83 - 800*m.b84 - m.x186 + m.x210 >= -800)

m.c220 = Constraint(expr= - 800*m.b74 - 800*m.b75 - 800*m.b76 - 800*m.b78 - 800*m.b79 - 800*m.b80 - 800*m.b82
                          - 800*m.b83 - 800*m.b84 - m.x188 + m.x210 >= -800)

m.c221 = Constraint(expr= - 800*m.b75 - 800*m.b76 - 800*m.b79 - 800*m.b80 - 800*m.b83 - 800*m.b84 - m.x190 + m.x210
                          >= -800)

m.c222 = Constraint(expr= - 800*m.b76 - 800*m.b80 - 800*m.b84 - m.x192 + m.x210 >= -800)

m.c223 = Constraint(expr= - 800*m.b37 - 800*m.b38 - 800*m.b39 - 800*m.b40 - 800*m.b41 - 800*m.b42 - 800*m.b43
                          - 800*m.b44 - 800*m.b45 - 800*m.b46 - 800*m.b47 - 800*m.b48 - m.x185 + m.x211 >= -800)

m.c224 = Constraint(expr= - 800*m.b38 - 800*m.b39 - 800*m.b40 - 800*m.b42 - 800*m.b43 - 800*m.b44 - 800*m.b46
                          - 800*m.b47 - 800*m.b48 - m.x187 + m.x211 >= -800)

m.c225 = Constraint(expr= - 800*m.b39 - 800*m.b40 - 800*m.b43 - 800*m.b44 - 800*m.b47 - 800*m.b48 - m.x189 + m.x211
                          >= -800)

m.c226 = Constraint(expr= - 800*m.b40 - 800*m.b44 - 800*m.b48 - m.x191 + m.x211 >= -800)

m.c227 = Constraint(expr= - 800*m.b85 - 800*m.b86 - 800*m.b87 - 800*m.b88 - 800*m.b89 - 800*m.b90 - 800*m.b91
                          - 800*m.b92 - 800*m.b93 - 800*m.b94 - 800*m.b95 - 800*m.b96 - m.x186 + m.x212 >= -800)

m.c228 = Constraint(expr= - 800*m.b86 - 800*m.b87 - 800*m.b88 - 800*m.b90 - 800*m.b91 - 800*m.b92 - 800*m.b94
                          - 800*m.b95 - 800*m.b96 - m.x188 + m.x212 >= -800)

m.c229 = Constraint(expr= - 800*m.b87 - 800*m.b88 - 800*m.b91 - 800*m.b92 - 800*m.b95 - 800*m.b96 - m.x190 + m.x212
                          >= -800)

m.c230 = Constraint(expr= - 800*m.b88 - 800*m.b92 - 800*m.b96 - m.x192 + m.x212 >= -800)

m.c231 = Constraint(expr=-m.x217*(m.x205 - m.x197) + m.x113 + m.x114 + m.x115 + m.x116 == 0)

m.c232 = Constraint(expr=-m.x218*(m.x206 - m.x198) + m.x117 + m.x118 + m.x119 + m.x120 == 0)

m.c233 = Constraint(expr=-m.x219*(m.x207 - m.x199) + m.x121 + m.x122 + m.x123 + m.x124 == 0)

m.c234 = Constraint(expr=-m.x220*(m.x208 - m.x200) + m.x125 + m.x126 + m.x127 + m.x128 == 0)

m.c235 = Constraint(expr=-m.x221*(m.x209 - m.x201) + m.x129 + m.x130 + m.x131 + m.x132 == 0)

m.c236 = Constraint(expr=-m.x222*(m.x210 - m.x202) + m.x133 + m.x134 + m.x135 + m.x136 == 0)

m.c237 = Constraint(expr=-m.x223*(m.x211 - m.x203) + m.x137 + m.x138 + m.x139 + m.x140 == 0)

m.c238 = Constraint(expr=-m.x224*(m.x212 - m.x204) + m.x141 + m.x142 + m.x143 + m.x144 == 0)

m.c239 = Constraint(expr= - 1170*m.b1 - 1170*m.b2 - 1170*m.b3 - 1170*m.b4 - 1170*m.b5 - 1170*m.b6 - 1170*m.b7
                          - 1170*m.b8 - 1170*m.b9 - 1170*m.b10 - 1170*m.b11 - 1170*m.b12 + m.x217 <= 0)

m.c240 = Constraint(expr= - 1120*m.b49 - 1120*m.b50 - 1120*m.b51 - 1120*m.b52 - 1120*m.b53 - 1120*m.b54 - 1120*m.b55
                          - 1120*m.b56 - 1120*m.b57 - 1120*m.b58 - 1120*m.b59 - 1120*m.b60 + m.x218 <= 0)

m.c241 = Constraint(expr= - 1340*m.b13 - 1340*m.b14 - 1340*m.b15 - 1340*m.b16 - 1340*m.b17 - 1340*m.b18 - 1340*m.b19
                          - 1340*m.b20 - 1340*m.b21 - 1340*m.b22 - 1340*m.b23 - 1340*m.b24 + m.x219 <= 0)

m.c242 = Constraint(expr= - 1290*m.b61 - 1290*m.b62 - 1290*m.b63 - 1290*m.b64 - 1290*m.b65 - 1290*m.b66 - 1290*m.b67
                          - 1290*m.b68 - 1290*m.b69 - 1290*m.b70 - 1290*m.b71 - 1290*m.b72 + m.x220 <= 0)

m.c243 = Constraint(expr= - 1340*m.b25 - 1340*m.b26 - 1340*m.b27 - 1340*m.b28 - 1340*m.b29 - 1340*m.b30 - 1340*m.b31
                          - 1340*m.b32 - 1340*m.b33 - 1340*m.b34 - 1340*m.b35 - 1340*m.b36 + m.x221 <= 0)

m.c244 = Constraint(expr= - 1340*m.b73 - 1340*m.b74 - 1340*m.b75 - 1340*m.b76 - 1340*m.b77 - 1340*m.b78 - 1340*m.b79
                          - 1340*m.b80 - 1340*m.b81 - 1340*m.b82 - 1340*m.b83 - 1340*m.b84 + m.x222 <= 0)

m.c245 = Constraint(expr= - 1210*m.b37 - 1210*m.b38 - 1210*m.b39 - 1210*m.b40 - 1210*m.b41 - 1210*m.b42 - 1210*m.b43
                          - 1210*m.b44 - 1210*m.b45 - 1210*m.b46 - 1210*m.b47 - 1210*m.b48 + m.x223 <= 0)

m.c246 = Constraint(expr= - 1160*m.b85 - 1160*m.b86 - 1160*m.b87 - 1160*m.b88 - 1160*m.b89 - 1160*m.b90 - 1160*m.b91
                          - 1160*m.b92 - 1160*m.b93 - 1160*m.b94 - 1160*m.b95 - 1160*m.b96 + m.x224 <= 0)

m.c247 = Constraint(expr=   m.x198 - m.x206 + m.x225 == 0)

m.c248 = Constraint(expr=   m.x200 - m.x208 + m.x226 == 0)

m.c249 = Constraint(expr=   m.x202 - m.x210 + m.x227 == 0)

m.c250 = Constraint(expr=   m.x204 - m.x212 + m.x228 == 0)

m.c251 = Constraint(expr=   m.x225 - m.x229 <= 0)

m.c252 = Constraint(expr=   m.x226 - m.x229 <= 0)

m.c253 = Constraint(expr=   m.x227 - m.x229 <= 0)

m.c254 = Constraint(expr=   m.x228 - m.x229 <= 0)

m.c255 = Constraint(expr=   800*m.b97 + 800*m.b105 + m.x197 - m.x198 <= 800)

m.c256 = Constraint(expr=   800*m.b98 + 800*m.b106 + m.x199 - m.x200 <= 800)

m.c257 = Constraint(expr=   800*m.b99 + 800*m.b107 + m.x201 - m.x202 <= 800)

m.c258 = Constraint(expr=   800*m.b100 + 800*m.b108 + m.x203 - m.x204 <= 800)

m.c259 = Constraint(expr= - 800*m.b101 - 800*m.b109 + m.x197 - m.x198 >= -800)

m.c260 = Constraint(expr= - 800*m.b102 - 800*m.b110 + m.x199 - m.x200 >= -800)

m.c261 = Constraint(expr= - 800*m.b103 - 800*m.b111 + m.x201 - m.x202 >= -800)

m.c262 = Constraint(expr= - 800*m.b104 - 800*m.b112 + m.x203 - m.x204 >= -800)

m.c263 = Constraint(expr=   1600*m.b97 + 1600*m.b109 + m.x205 - m.x206 <= 1600)

m.c264 = Constraint(expr=   1600*m.b98 + 1600*m.b110 + m.x207 - m.x208 <= 1600)

m.c265 = Constraint(expr=   1600*m.b99 + 1600*m.b111 + m.x209 - m.x210 <= 1600)

m.c266 = Constraint(expr=   1600*m.b100 + 1600*m.b112 + m.x211 - m.x212 <= 1600)

m.c267 = Constraint(expr= - 1600*m.b101 - 1600*m.b105 + m.x205 - m.x206 >= -1600)

m.c268 = Constraint(expr= - 1600*m.b102 - 1600*m.b106 + m.x207 - m.x208 >= -1600)

m.c269 = Constraint(expr= - 1600*m.b103 - 1600*m.b107 + m.x209 - m.x210 >= -1600)

m.c270 = Constraint(expr= - 1600*m.b104 - 1600*m.b108 + m.x211 - m.x212 >= -1600)

m.c271 = Constraint(expr= - 800*m.b97 - 800*m.b101 - 800*m.b105 - 800*m.b109 - m.x198 + m.x205 >= -800)

m.c272 = Constraint(expr= - 800*m.b98 - 800*m.b102 - 800*m.b106 - 800*m.b110 - m.x200 + m.x207 >= -800)

m.c273 = Constraint(expr= - 800*m.b99 - 800*m.b103 - 800*m.b107 - 800*m.b111 - m.x202 + m.x209 >= -800)

m.c274 = Constraint(expr= - 800*m.b100 - 800*m.b104 - 800*m.b108 - 800*m.b112 - m.x204 + m.x211 >= -800)

m.c275 = Constraint(expr= - 800*m.b97 - 800*m.b101 - 800*m.b105 - 800*m.b109 - m.x197 + m.x206 >= -800)

m.c276 = Constraint(expr= - 800*m.b98 - 800*m.b102 - 800*m.b106 - 800*m.b110 - m.x199 + m.x208 >= -800)

m.c277 = Constraint(expr= - 800*m.b99 - 800*m.b103 - 800*m.b107 - 800*m.b111 - m.x201 + m.x210 >= -800)

m.c278 = Constraint(expr= - 800*m.b100 - 800*m.b104 - 800*m.b108 - 800*m.b112 - m.x203 + m.x212 >= -800)

m.c279 = Constraint(expr=-(m.x198 - m.x197)*m.x217 - 896000*m.b97 + m.x193 >= -896000)

m.c280 = Constraint(expr=-(m.x200 - m.x199)*m.x219 - 1032000*m.b98 + m.x194 >= -1032000)

m.c281 = Constraint(expr=-(m.x202 - m.x201)*m.x221 - 1072000*m.b99 + m.x195 >= -1072000)

m.c282 = Constraint(expr=-(m.x204 - m.x203)*m.x223 - 928000*m.b100 + m.x196 >= -928000)

m.c283 = Constraint(expr=-(m.x206 - m.x205)*m.x218 - 896000*m.b97 + m.x193 >= -896000)

m.c284 = Constraint(expr=-(m.x208 - m.x207)*m.x220 - 1032000*m.b98 + m.x194 >= -1032000)

m.c285 = Constraint(expr=-(m.x210 - m.x209)*m.x222 - 1072000*m.b99 + m.x195 >= -1072000)

m.c286 = Constraint(expr=-(m.x212 - m.x211)*m.x224 - 928000*m.b100 + m.x196 >= -928000)

m.c287 = Constraint(expr=-(m.x197 - m.x198)*m.x218 - 896000*m.b101 + m.x193 >= -896000)

m.c288 = Constraint(expr=-(m.x199 - m.x200)*m.x220 - 1032000*m.b102 + m.x194 >= -1032000)

m.c289 = Constraint(expr=-(m.x201 - m.x202)*m.x222 - 1072000*m.b103 + m.x195 >= -1072000)

m.c290 = Constraint(expr=-(m.x203 - m.x204)*m.x224 - 928000*m.b104 + m.x196 >= -928000)

m.c291 = Constraint(expr=-(m.x205 - m.x206)*m.x217 - 896000*m.b101 + m.x193 >= -896000)

m.c292 = Constraint(expr=-(m.x207 - m.x208)*m.x219 - 1032000*m.b102 + m.x194 >= -1032000)

m.c293 = Constraint(expr=-(m.x209 - m.x210)*m.x221 - 1072000*m.b103 + m.x195 >= -1072000)

m.c294 = Constraint(expr=-(m.x211 - m.x212)*m.x223 - 928000*m.b104 + m.x196 >= -928000)

m.c295 = Constraint(expr=-(m.x218 - m.x217)*(m.x206 - m.x198) - 896000*m.b105 + m.x193 >= -896000)

m.c296 = Constraint(expr=-(m.x220 - m.x219)*(m.x208 - m.x200) - 1032000*m.b106 + m.x194 >= -1032000)

m.c297 = Constraint(expr=-(m.x222 - m.x221)*(m.x210 - m.x202) - 1072000*m.b107 + m.x195 >= -1072000)

m.c298 = Constraint(expr=-(m.x224 - m.x223)*(m.x212 - m.x204) - 928000*m.b108 + m.x196 >= -928000)

m.c299 = Constraint(expr=-(m.x217 - m.x218)*(m.x205 - m.x197) - 896000*m.b109 + m.x193 >= -896000)

m.c300 = Constraint(expr=-(m.x219 - m.x220)*(m.x207 - m.x199) - 1032000*m.b110 + m.x194 >= -1032000)

m.c301 = Constraint(expr=-(m.x221 - m.x222)*(m.x209 - m.x201) - 1072000*m.b111 + m.x195 >= -1072000)

m.c302 = Constraint(expr=-(m.x223 - m.x224)*(m.x211 - m.x203) - 928000*m.b112 + m.x196 >= -928000)

m.c303 = Constraint(expr=   896000*m.b97 + 896000*m.b101 + 896000*m.b105 + 896000*m.b109 - m.x113 - m.x114 - m.x115
                          - m.x116 + m.x193 >= 0)

m.c304 = Constraint(expr=   1032000*m.b98 + 1032000*m.b102 + 1032000*m.b106 + 1032000*m.b110 - m.x121 - m.x122 - m.x123
                          - m.x124 + m.x194 >= 0)

m.c305 = Constraint(expr=   1072000*m.b99 + 1072000*m.b103 + 1072000*m.b107 + 1072000*m.b111 - m.x129 - m.x130 - m.x131
                          - m.x132 + m.x195 >= 0)

m.c306 = Constraint(expr=   928000*m.b100 + 928000*m.b104 + 928000*m.b108 + 928000*m.b112 - m.x137 - m.x138 - m.x139
                          - m.x140 + m.x196 >= 0)

m.c307 = Constraint(expr=   3*m.b49 + 3*m.b50 + 3*m.b51 + 3*m.b52 + 3*m.b53 + 3*m.b54 + 3*m.b55 + 3*m.b56 + 12*m.b57
                          + 12*m.b58 + 12*m.b59 + 12*m.b60 + 3*m.b61 + 3*m.b62 + 3*m.b63 + 3*m.b64 + m.b65 + m.b66
                          + m.b67 + m.b68 + 12*m.b69 + 12*m.b70 + 12*m.b71 + 12*m.b72 + 3*m.b73 + 3*m.b74 + 3*m.b75
                          + 3*m.b76 + m.b77 + m.b78 + m.b79 + m.b80 + 12*m.b81 + 12*m.b82 + 12*m.b83 + 12*m.b84
                          + 12*m.b85 + 12*m.b86 + 12*m.b87 + 12*m.b88 + 12*m.b89 + 12*m.b90 + 12*m.b91 + 12*m.b92
                          + 12*m.b93 + 12*m.b94 + 12*m.b95 + 12*m.b96 + m.x225 + m.x226 + m.x227 + m.x228 - m.x229 == 0)
