#  MINLP written by GAMS Convert at 04/21/18 13:52:37
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        257       62       96       99        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        194      101       93        0        0        0        0        0
#  FX      1        1        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1979     1884       95        0


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
m.x148 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x149 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x150 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x151 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x152 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x153 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x154 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x155 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x156 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x157 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x158 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x159 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x160 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x161 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x162 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x163 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x164 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x165 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x166 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x167 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x168 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x169 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x170 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x171 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x172 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x173 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x174 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x175 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x176 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x177 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x178 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x179 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x180 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x181 = Var(within=Reals,bounds=(50,None),initialize=50)
m.x182 = Var(within=Reals,bounds=(100,None),initialize=100)
m.x183 = Var(within=Reals,bounds=(250,None),initialize=250)
m.x184 = Var(within=Reals,bounds=(0,None),initialize=800)
m.x185 = Var(within=Reals,bounds=(0,None),initialize=900)
m.x186 = Var(within=Reals,bounds=(0,None),initialize=1200)
m.x187 = Var(within=Reals,bounds=(0,None),initialize=600)
m.x188 = Var(within=Reals,bounds=(0,None),initialize=1000)
m.x189 = Var(within=Reals,bounds=(0,None),initialize=1100)
m.x190 = Var(within=Reals,bounds=(11.1111111111111,600),initialize=11.1111111111111)
m.x191 = Var(within=Reals,bounds=(33.3333333333333,600),initialize=33.3333333333333)
m.x192 = Var(within=Reals,bounds=(45.4545454545455,600),initialize=45.4545454545455)
m.x193 = Var(within=Reals,bounds=(200,600),initialize=200)
m.x194 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=m.x194, sense=maximize)

m.c1 = Constraint(expr=m.x194*m.x193 + 0.00203*(m.x190**2*(m.x185 - m.x181) + (m.x193 - m.x190)**2*m.x181) + 0.00203*(
                       m.x191**2*(m.x187 - m.x182) + (m.x193 - m.x191)**2*m.x182) + 0.00203*(m.x192**2*(m.x189 - m.x183)
                        + (m.x193 - m.x192)**2*m.x183) + 3800*m.b4 + 3800*m.b5 + 3800*m.b6 + 6080*m.b7 + 6080*m.b8
                        + 6080*m.b9 + 7500*m.b10 + 7500*m.b11 + 7500*m.b12 + 2250*m.b16 + 2250*m.b17 + 2250*m.b18
                        + 3080*m.b19 + 3080*m.b20 + 3080*m.b21 + 5390*m.b22 + 5390*m.b23 + 5390*m.b24 + 8360*m.b31
                        + 8360*m.b32 + 8360*m.b33 + 760*m.b34 + 760*m.b35 + 760*m.b36 + 1500*m.b37 + 1500*m.b38
                        + 1500*m.b39 + 3750*m.b43 + 3750*m.b44 + 3750*m.b45 + 4620*m.b46 + 4620*m.b47 + 4620*m.b48
                        + 770*m.b49 + 770*m.b50 + 770*m.b51 + 6840*m.b58 + 6840*m.b59 + 6840*m.b60 + 8360*m.b61
                        + 8360*m.b62 + 8360*m.b63 + 3750*m.b64 + 3750*m.b65 + 3750*m.b66 + 5250*m.b70 + 5250*m.b71
                        + 5250*m.b72 + 4620*m.b73 + 4620*m.b74 + 4620*m.b75 + 3080*m.b76 + 3080*m.b77 + 3080*m.b78
                        - 0.15*m.x97 - 0.15*m.x98 - 0.15*m.x99 - 0.15*m.x100 - 0.15*m.x101 - 0.15*m.x102 - 0.4*m.x106
                        - 0.4*m.x107 - 0.4*m.x108 - 0.4*m.x109 - 0.4*m.x110 - 0.4*m.x111 - 0.65*m.x115 - 0.65*m.x116
                        - 0.65*m.x117 - 0.65*m.x118 - 0.65*m.x119 - 0.65*m.x120 + 0.1406*m.x166 + 0.1406*m.x167
                        + 0.1406*m.x168 == 0)

m.c2 = Constraint(expr=   m.b1 - m.b3 + m.b4 + m.b7 - m.b12 - m.b21 + m.x121 - m.x123 == 0)

m.c3 = Constraint(expr= - m.b1 + m.b2 + m.b5 + m.b8 - m.b10 - m.b19 - m.x121 + m.x122 == 0)

m.c4 = Constraint(expr= - m.b2 + m.b3 + m.b6 + m.b9 - m.b11 - m.b20 - m.x122 + m.x123 == 0)

m.c5 = Constraint(expr= - m.b6 + m.b10 + m.b13 - m.b15 + m.b16 - m.b24 + m.x124 - m.x126 == 0)

m.c6 = Constraint(expr= - m.b4 + m.b11 - m.b13 + m.b14 + m.b17 - m.b22 - m.x124 + m.x125 == 0)

m.c7 = Constraint(expr= - m.b5 + m.b12 - m.b14 + m.b15 + m.b18 - m.b23 - m.x125 + m.x126 == 0)

m.c8 = Constraint(expr= - m.b9 - m.b18 + m.b19 + m.b22 + m.b25 - m.b27 + m.x127 - m.x129 == 0)

m.c9 = Constraint(expr= - m.b7 - m.b16 + m.b20 + m.b23 - m.b25 + m.b26 - m.x127 + m.x128 == 0)

m.c10 = Constraint(expr= - m.b8 - m.b17 + m.b21 + m.b24 - m.b26 + m.b27 - m.x128 + m.x129 == 0)

m.c11 = Constraint(expr=   m.b28 - m.b30 + m.b31 + m.b34 - m.b39 - m.b48 + m.x130 - m.x132 == 0)

m.c12 = Constraint(expr= - m.b28 + m.b29 + m.b32 + m.b35 - m.b37 - m.b46 - m.x130 + m.x131 == 0)

m.c13 = Constraint(expr= - m.b29 + m.b30 + m.b33 + m.b36 - m.b38 - m.b47 - m.x131 + m.x132 == 0)

m.c14 = Constraint(expr= - m.b33 + m.b37 + m.b40 - m.b42 + m.b43 - m.b51 + m.x133 - m.x135 == 0)

m.c15 = Constraint(expr= - m.b31 + m.b38 - m.b40 + m.b41 + m.b44 - m.b49 - m.x133 + m.x134 == 0)

m.c16 = Constraint(expr= - m.b32 + m.b39 - m.b41 + m.b42 + m.b45 - m.b50 - m.x134 + m.x135 == 0)

m.c17 = Constraint(expr= - m.b36 - m.b45 + m.b46 + m.b49 + m.b52 - m.b54 + m.x136 - m.x138 == 0)

m.c18 = Constraint(expr= - m.b34 - m.b43 + m.b47 + m.b50 - m.b52 + m.b53 - m.x136 + m.x137 == 0)

m.c19 = Constraint(expr= - m.b35 - m.b44 + m.b48 + m.b51 - m.b53 + m.b54 - m.x137 + m.x138 == 0)

m.c20 = Constraint(expr=   m.b55 - m.b57 + m.b58 + m.b61 - m.b66 - m.b75 + m.x139 - m.x141 == 0)

m.c21 = Constraint(expr= - m.b55 + m.b56 + m.b59 + m.b62 - m.b64 - m.b73 - m.x139 + m.x140 == 0)

m.c22 = Constraint(expr= - m.b56 + m.b57 + m.b60 + m.b63 - m.b65 - m.b74 - m.x140 + m.x141 == 0)

m.c23 = Constraint(expr= - m.b60 + m.b64 + m.b67 - m.b69 + m.b70 - m.b78 + m.x142 - m.x144 == 0)

m.c24 = Constraint(expr= - m.b58 + m.b65 - m.b67 + m.b68 + m.b71 - m.b76 - m.x142 + m.x143 == 0)

m.c25 = Constraint(expr= - m.b59 + m.b66 - m.b68 + m.b69 + m.b72 - m.b77 - m.x143 + m.x144 == 0)

m.c26 = Constraint(expr= - m.b63 - m.b72 + m.b73 + m.b76 + m.b79 - m.b81 + m.x145 - m.x147 == 0)

m.c27 = Constraint(expr= - m.b61 - m.b70 + m.b74 + m.b77 - m.b79 + m.b80 - m.x145 + m.x146 == 0)

m.c28 = Constraint(expr= - m.b62 - m.b71 + m.b75 + m.b78 - m.b80 + m.b81 - m.x146 + m.x147 == 0)

m.c29 = Constraint(expr=   m.b1 + m.b4 + m.b7 + m.b10 + m.b13 + m.b16 + m.b19 + m.b22 + m.b25 + m.x121 + m.x124 + m.x127
                         == 1)

m.c30 = Constraint(expr=   m.b28 + m.b31 + m.b34 + m.b37 + m.b40 + m.b43 + m.b46 + m.b49 + m.b52 + m.x130 + m.x133
                         + m.x136 == 1)

m.c31 = Constraint(expr=   m.b55 + m.b58 + m.b61 + m.b64 + m.b67 + m.b70 + m.b73 + m.b76 + m.b79 + m.x139 + m.x142
                         + m.x145 == 1)

m.c32 = Constraint(expr= - 5*m.b4 - 8*m.b7 - 10*m.b10 - 3*m.b16 - 4*m.b19 - 7*m.b22 - 0.00125*m.x94
                         - 0.000833333333333333*m.x103 - 0.001*m.x112 - m.x148 + m.x151 >= 0)

m.c33 = Constraint(expr= - 5*m.b5 - 8*m.b8 - 10*m.b11 - 3*m.b17 - 4*m.b20 - 7*m.b23 - 0.00125*m.x95
                         - 0.000833333333333333*m.x104 - 0.001*m.x113 - m.x151 + m.x154 >= 0)

m.c34 = Constraint(expr= - 5*m.b6 - 8*m.b9 - 10*m.b12 - 3*m.b18 - 4*m.b21 - 7*m.b24 - 0.00125*m.x96
                         - 0.000833333333333333*m.x105 - 0.001*m.x114 + m.x148 - m.x154 + m.x193 >= 0)

m.c35 = Constraint(expr= - 11*m.b31 - m.b34 - 2*m.b37 - 5*m.b43 - 6*m.b46 - m.b49 - 0.00111111111111111*m.x97
                         - 0.00166666666666667*m.x106 - 0.000909090909090909*m.x115 - m.x149 + m.x152 >= 0)

m.c36 = Constraint(expr= - 11*m.b32 - m.b35 - 2*m.b38 - 5*m.b44 - 6*m.b47 - m.b50 - 0.00111111111111111*m.x98
                         - 0.00166666666666667*m.x107 - 0.000909090909090909*m.x116 - m.x152 + m.x155 >= 0)

m.c37 = Constraint(expr= - 11*m.b33 - m.b36 - 2*m.b39 - 5*m.b45 - 6*m.b48 - m.b51 - 0.00111111111111111*m.x99
                         - 0.00166666666666667*m.x108 - 0.000909090909090909*m.x117 + m.x149 - m.x155 + m.x193 >= 0)

m.c38 = Constraint(expr= - 9*m.b58 - 11*m.b61 - 5*m.b64 - 7*m.b70 - 6*m.b73 - 4*m.b76 - 0.0025*m.x100 - 0.002*m.x109
                         - 0.00222222222222222*m.x118 - m.x150 + m.x153 >= 0)

m.c39 = Constraint(expr= - 9*m.b59 - 11*m.b62 - 5*m.b65 - 7*m.b71 - 6*m.b74 - 4*m.b77 - 0.0025*m.x101 - 0.002*m.x110
                         - 0.00222222222222222*m.x119 - m.x153 + m.x156 >= 0)

m.c40 = Constraint(expr= - 9*m.b60 - 11*m.b63 - 5*m.b66 - 7*m.b72 - 6*m.b75 - 4*m.b78 - 0.0025*m.x102 - 0.002*m.x111
                         - 0.00222222222222222*m.x120 + m.x150 - m.x156 + m.x193 >= 0)

m.c41 = Constraint(expr= - 5*m.b4 - 8*m.b7 - 10*m.b10 - 3*m.b16 - 4*m.b19 - 7*m.b22 + m.x151 - m.x157 == 0)

m.c42 = Constraint(expr= - 5*m.b5 - 8*m.b8 - 10*m.b11 - 3*m.b17 - 4*m.b20 - 7*m.b23 + m.x154 - m.x160 == 0)

m.c43 = Constraint(expr= - 5*m.b6 - 8*m.b9 - 10*m.b12 - 3*m.b18 - 4*m.b21 - 7*m.b24 + m.x148 - m.x163 + m.x193 == 0)

m.c44 = Constraint(expr= - 11*m.b31 - m.b34 - 2*m.b37 - 5*m.b43 - 6*m.b46 - m.b49 + m.x152 - m.x158 == 0)

m.c45 = Constraint(expr= - 11*m.b32 - m.b35 - 2*m.b38 - 5*m.b44 - 6*m.b47 - m.b50 + m.x155 - m.x161 == 0)

m.c46 = Constraint(expr= - 11*m.b33 - m.b36 - 2*m.b39 - 5*m.b45 - 6*m.b48 - m.b51 + m.x149 - m.x164 + m.x193 == 0)

m.c47 = Constraint(expr= - 9*m.b58 - 11*m.b61 - 5*m.b64 - 7*m.b70 - 6*m.b73 - 4*m.b76 + m.x153 - m.x159 == 0)

m.c48 = Constraint(expr= - 9*m.b59 - 11*m.b62 - 5*m.b65 - 7*m.b71 - 6*m.b74 - 4*m.b77 + m.x156 - m.x162 == 0)

m.c49 = Constraint(expr= - 9*m.b60 - 11*m.b63 - 5*m.b66 - 7*m.b72 - 6*m.b75 - 4*m.b78 + m.x150 - m.x165 + m.x193 == 0)

m.c50 = Constraint(expr=   m.x154 - m.x193 <= 0)

m.c51 = Constraint(expr=   m.x155 - m.x193 <= 0)

m.c52 = Constraint(expr=   m.x156 - m.x193 <= 0)

m.c53 = Constraint(expr= - 480000*m.b1 - 480000*m.b4 - 480000*m.b7 + m.x94 <= 0)

m.c54 = Constraint(expr= - 480000*m.b2 - 480000*m.b5 - 480000*m.b8 + m.x95 <= 0)

m.c55 = Constraint(expr= - 480000*m.b3 - 480000*m.b6 - 480000*m.b9 + m.x96 <= 0)

m.c56 = Constraint(expr= - 540000*m.b28 - 540000*m.b31 - 540000*m.b34 + m.x97 <= 0)

m.c57 = Constraint(expr= - 540000*m.b29 - 540000*m.b32 - 540000*m.b35 + m.x98 <= 0)

m.c58 = Constraint(expr= - 540000*m.b30 - 540000*m.b33 - 540000*m.b36 + m.x99 <= 0)

m.c59 = Constraint(expr= - 240000*m.b55 - 240000*m.b58 - 240000*m.b61 + m.x100 <= 0)

m.c60 = Constraint(expr= - 240000*m.b56 - 240000*m.b59 - 240000*m.b62 + m.x101 <= 0)

m.c61 = Constraint(expr= - 240000*m.b57 - 240000*m.b60 - 240000*m.b63 + m.x102 <= 0)

m.c62 = Constraint(expr= - 720000*m.b10 - 720000*m.b13 - 720000*m.b16 + m.x103 <= 0)

m.c63 = Constraint(expr= - 720000*m.b11 - 720000*m.b14 - 720000*m.b17 + m.x104 <= 0)

m.c64 = Constraint(expr= - 720000*m.b12 - 720000*m.b15 - 720000*m.b18 + m.x105 <= 0)

m.c65 = Constraint(expr= - 360000*m.b37 - 360000*m.b40 - 360000*m.b43 + m.x106 <= 0)

m.c66 = Constraint(expr= - 360000*m.b38 - 360000*m.b41 - 360000*m.b44 + m.x107 <= 0)

m.c67 = Constraint(expr= - 360000*m.b39 - 360000*m.b42 - 360000*m.b45 + m.x108 <= 0)

m.c68 = Constraint(expr= - 300000*m.b64 - 300000*m.b67 - 300000*m.b70 + m.x109 <= 0)

m.c69 = Constraint(expr= - 300000*m.b65 - 300000*m.b68 - 300000*m.b71 + m.x110 <= 0)

m.c70 = Constraint(expr= - 300000*m.b66 - 300000*m.b69 - 300000*m.b72 + m.x111 <= 0)

m.c71 = Constraint(expr= - 600000*m.b19 - 600000*m.b22 - 600000*m.b25 + m.x112 <= 0)

m.c72 = Constraint(expr= - 600000*m.b20 - 600000*m.b23 - 600000*m.b26 + m.x113 <= 0)

m.c73 = Constraint(expr= - 600000*m.b21 - 600000*m.b24 - 600000*m.b27 + m.x114 <= 0)

m.c74 = Constraint(expr= - 660000*m.b46 - 660000*m.b49 - 660000*m.b52 + m.x115 <= 0)

m.c75 = Constraint(expr= - 660000*m.b47 - 660000*m.b50 - 660000*m.b53 + m.x116 <= 0)

m.c76 = Constraint(expr= - 660000*m.b48 - 660000*m.b51 - 660000*m.b54 + m.x117 <= 0)

m.c77 = Constraint(expr= - 270000*m.b73 - 270000*m.b76 - 270000*m.b79 + m.x118 <= 0)

m.c78 = Constraint(expr= - 270000*m.b74 - 270000*m.b77 - 270000*m.b80 + m.x119 <= 0)

m.c79 = Constraint(expr= - 270000*m.b75 - 270000*m.b78 - 270000*m.b81 + m.x120 <= 0)

m.c80 = Constraint(expr=   m.b1 + m.b2 + m.b3 + m.b4 + m.b5 + m.b6 + m.b7 + m.b8 + m.b9 == 1)

m.c81 = Constraint(expr=   m.b28 + m.b29 + m.b30 + m.b31 + m.b32 + m.b33 + m.b34 + m.b35 + m.b36 + m.b55 + m.b56 + m.b57
                         + m.b58 + m.b59 + m.b60 + m.b61 + m.b62 + m.b63 == 1)

m.c82 = Constraint(expr=   m.b10 + m.b11 + m.b12 + m.b13 + m.b14 + m.b15 + m.b16 + m.b17 + m.b18 == 1)

m.c83 = Constraint(expr=   m.b37 + m.b38 + m.b39 + m.b40 + m.b41 + m.b42 + m.b43 + m.b44 + m.b45 + m.b64 + m.b65 + m.b66
                         + m.b67 + m.b68 + m.b69 + m.b70 + m.b71 + m.b72 == 1)

m.c84 = Constraint(expr=   m.b19 + m.b20 + m.b21 + m.b22 + m.b23 + m.b24 + m.b25 + m.b26 + m.b27 == 1)

m.c85 = Constraint(expr=   m.b46 + m.b47 + m.b48 + m.b49 + m.b50 + m.b51 + m.b52 + m.b53 + m.b54 + m.b73 + m.b74 + m.b75
                         + m.b76 + m.b77 + m.b78 + m.b79 + m.b80 + m.b81 == 1)

m.c86 = Constraint(expr=   m.b1 + m.b4 + m.b7 == 1)

m.c87 = Constraint(expr=m.x181*m.x193 - m.x97 - m.x98 - m.x99 - m.x100 - m.x101 - m.x102 == 0)

m.c88 = Constraint(expr=m.x182*m.x193 - m.x106 - m.x107 - m.x108 - m.x109 - m.x110 - m.x111 == 0)

m.c89 = Constraint(expr=m.x183*m.x193 - m.x115 - m.x116 - m.x117 - m.x118 - m.x119 - m.x120 == 0)

m.c90 = Constraint(expr=   m.x94 + m.x95 + m.x96 - m.x97 - m.x98 - m.x99 - m.x100 - m.x101 - m.x102 == 0)

m.c91 = Constraint(expr=   m.x103 + m.x104 + m.x105 - m.x106 - m.x107 - m.x108 - m.x109 - m.x110 - m.x111 == 0)

m.c92 = Constraint(expr=   m.x112 + m.x113 + m.x114 - m.x115 - m.x116 - m.x117 - m.x118 - m.x119 - m.x120 == 0)

m.c93 = Constraint(expr=   600*m.b1 + 600*m.b4 + 600*m.b7 - m.x148 + m.x169 <= 600)

m.c94 = Constraint(expr=   600*m.b1 + 600*m.b2 + 600*m.b4 + 600*m.b5 + 600*m.b7 + 600*m.b8 - m.x151 + m.x169 <= 600)

m.c95 = Constraint(expr=   600*m.b1 + 600*m.b2 + 600*m.b3 + 600*m.b4 + 600*m.b5 + 600*m.b6 + 600*m.b7 + 600*m.b8
                         + 600*m.b9 - m.x154 + m.x169 <= 600)

m.c96 = Constraint(expr=   600*m.b28 + 600*m.b31 + 600*m.b34 - m.x149 + m.x170 <= 600)

m.c97 = Constraint(expr=   600*m.b28 + 600*m.b29 + 600*m.b31 + 600*m.b32 + 600*m.b34 + 600*m.b35 - m.x152 + m.x170
                         <= 600)

m.c98 = Constraint(expr=   600*m.b28 + 600*m.b29 + 600*m.b30 + 600*m.b31 + 600*m.b32 + 600*m.b33 + 600*m.b34 + 600*m.b35
                         + 600*m.b36 - m.x155 + m.x170 <= 600)

m.c99 = Constraint(expr=   600*m.b55 + 600*m.b58 + 600*m.b61 - m.x150 + m.x170 <= 600)

m.c100 = Constraint(expr=   600*m.b55 + 600*m.b56 + 600*m.b58 + 600*m.b59 + 600*m.b61 + 600*m.b62 - m.x153 + m.x170
                          <= 600)

m.c101 = Constraint(expr=   600*m.b55 + 600*m.b56 + 600*m.b57 + 600*m.b58 + 600*m.b59 + 600*m.b60 + 600*m.b61
                          + 600*m.b62 + 600*m.b63 - m.x156 + m.x170 <= 600)

m.c102 = Constraint(expr=   600*m.b10 + 600*m.b13 + 600*m.b16 - m.x148 + m.x171 <= 600)

m.c103 = Constraint(expr=   600*m.b10 + 600*m.b11 + 600*m.b13 + 600*m.b14 + 600*m.b16 + 600*m.b17 - m.x151 + m.x171
                          <= 600)

m.c104 = Constraint(expr=   600*m.b10 + 600*m.b11 + 600*m.b12 + 600*m.b13 + 600*m.b14 + 600*m.b15 + 600*m.b16
                          + 600*m.b17 + 600*m.b18 - m.x154 + m.x171 <= 600)

m.c105 = Constraint(expr=   600*m.b37 + 600*m.b40 + 600*m.b43 - m.x149 + m.x172 <= 600)

m.c106 = Constraint(expr=   600*m.b37 + 600*m.b38 + 600*m.b40 + 600*m.b41 + 600*m.b43 + 600*m.b44 - m.x152 + m.x172
                          <= 600)

m.c107 = Constraint(expr=   600*m.b37 + 600*m.b38 + 600*m.b39 + 600*m.b40 + 600*m.b41 + 600*m.b42 + 600*m.b43
                          + 600*m.b44 + 600*m.b45 - m.x155 + m.x172 <= 600)

m.c108 = Constraint(expr=   600*m.b64 + 600*m.b67 + 600*m.b70 - m.x150 + m.x172 <= 600)

m.c109 = Constraint(expr=   600*m.b64 + 600*m.b65 + 600*m.b67 + 600*m.b68 + 600*m.b70 + 600*m.b71 - m.x153 + m.x172
                          <= 600)

m.c110 = Constraint(expr=   600*m.b64 + 600*m.b65 + 600*m.b66 + 600*m.b67 + 600*m.b68 + 600*m.b69 + 600*m.b70
                          + 600*m.b71 + 600*m.b72 - m.x156 + m.x172 <= 600)

m.c111 = Constraint(expr=   600*m.b19 + 600*m.b22 + 600*m.b25 - m.x148 + m.x173 <= 600)

m.c112 = Constraint(expr=   600*m.b19 + 600*m.b20 + 600*m.b22 + 600*m.b23 + 600*m.b25 + 600*m.b26 - m.x151 + m.x173
                          <= 600)

m.c113 = Constraint(expr=   600*m.b19 + 600*m.b20 + 600*m.b21 + 600*m.b22 + 600*m.b23 + 600*m.b24 + 600*m.b25
                          + 600*m.b26 + 600*m.b27 - m.x154 + m.x173 <= 600)

m.c114 = Constraint(expr=   600*m.b46 + 600*m.b49 + 600*m.b52 - m.x149 + m.x174 <= 600)

m.c115 = Constraint(expr=   600*m.b46 + 600*m.b47 + 600*m.b49 + 600*m.b50 + 600*m.b52 + 600*m.b53 - m.x152 + m.x174
                          <= 600)

m.c116 = Constraint(expr=   600*m.b46 + 600*m.b47 + 600*m.b48 + 600*m.b49 + 600*m.b50 + 600*m.b51 + 600*m.b52
                          + 600*m.b53 + 600*m.b54 - m.x155 + m.x174 <= 600)

m.c117 = Constraint(expr=   600*m.b73 + 600*m.b76 + 600*m.b79 - m.x150 + m.x174 <= 600)

m.c118 = Constraint(expr=   600*m.b73 + 600*m.b74 + 600*m.b76 + 600*m.b77 + 600*m.b79 + 600*m.b80 - m.x153 + m.x174
                          <= 600)

m.c119 = Constraint(expr=   600*m.b73 + 600*m.b74 + 600*m.b75 + 600*m.b76 + 600*m.b77 + 600*m.b78 + 600*m.b79
                          + 600*m.b80 + 600*m.b81 - m.x156 + m.x174 <= 600)

m.c120 = Constraint(expr= - 600*m.b1 - 600*m.b2 - 600*m.b3 - 600*m.b4 - 600*m.b5 - 600*m.b6 - 600*m.b7 - 600*m.b8
                          - 600*m.b9 - m.x148 + m.x169 >= -600)

m.c121 = Constraint(expr= - 600*m.b2 - 600*m.b3 - 600*m.b5 - 600*m.b6 - 600*m.b8 - 600*m.b9 - m.x151 + m.x169 >= -600)

m.c122 = Constraint(expr= - 600*m.b3 - 600*m.b6 - 600*m.b9 - m.x154 + m.x169 >= -600)

m.c123 = Constraint(expr= - 600*m.b28 - 600*m.b29 - 600*m.b30 - 600*m.b31 - 600*m.b32 - 600*m.b33 - 600*m.b34
                          - 600*m.b35 - 600*m.b36 - m.x149 + m.x170 >= -600)

m.c124 = Constraint(expr= - 600*m.b29 - 600*m.b30 - 600*m.b32 - 600*m.b33 - 600*m.b35 - 600*m.b36 - m.x152 + m.x170
                          >= -600)

m.c125 = Constraint(expr= - 600*m.b30 - 600*m.b33 - 600*m.b36 - m.x155 + m.x170 >= -600)

m.c126 = Constraint(expr= - 600*m.b55 - 600*m.b56 - 600*m.b57 - 600*m.b58 - 600*m.b59 - 600*m.b60 - 600*m.b61
                          - 600*m.b62 - 600*m.b63 - m.x150 + m.x170 >= -600)

m.c127 = Constraint(expr= - 600*m.b56 - 600*m.b57 - 600*m.b59 - 600*m.b60 - 600*m.b62 - 600*m.b63 - m.x153 + m.x170
                          >= -600)

m.c128 = Constraint(expr= - 600*m.b57 - 600*m.b60 - 600*m.b63 - m.x156 + m.x170 >= -600)

m.c129 = Constraint(expr= - 600*m.b10 - 600*m.b11 - 600*m.b12 - 600*m.b13 - 600*m.b14 - 600*m.b15 - 600*m.b16
                          - 600*m.b17 - 600*m.b18 - m.x148 + m.x171 >= -600)

m.c130 = Constraint(expr= - 600*m.b11 - 600*m.b12 - 600*m.b14 - 600*m.b15 - 600*m.b17 - 600*m.b18 - m.x151 + m.x171
                          >= -600)

m.c131 = Constraint(expr= - 600*m.b12 - 600*m.b15 - 600*m.b18 - m.x154 + m.x171 >= -600)

m.c132 = Constraint(expr= - 600*m.b37 - 600*m.b38 - 600*m.b39 - 600*m.b40 - 600*m.b41 - 600*m.b42 - 600*m.b43
                          - 600*m.b44 - 600*m.b45 - m.x149 + m.x172 >= -600)

m.c133 = Constraint(expr= - 600*m.b38 - 600*m.b39 - 600*m.b41 - 600*m.b42 - 600*m.b44 - 600*m.b45 - m.x152 + m.x172
                          >= -600)

m.c134 = Constraint(expr= - 600*m.b39 - 600*m.b42 - 600*m.b45 - m.x155 + m.x172 >= -600)

m.c135 = Constraint(expr= - 600*m.b64 - 600*m.b65 - 600*m.b66 - 600*m.b67 - 600*m.b68 - 600*m.b69 - 600*m.b70
                          - 600*m.b71 - 600*m.b72 - m.x150 + m.x172 >= -600)

m.c136 = Constraint(expr= - 600*m.b65 - 600*m.b66 - 600*m.b68 - 600*m.b69 - 600*m.b71 - 600*m.b72 - m.x153 + m.x172
                          >= -600)

m.c137 = Constraint(expr= - 600*m.b66 - 600*m.b69 - 600*m.b72 - m.x156 + m.x172 >= -600)

m.c138 = Constraint(expr= - 600*m.b19 - 600*m.b20 - 600*m.b21 - 600*m.b22 - 600*m.b23 - 600*m.b24 - 600*m.b25
                          - 600*m.b26 - 600*m.b27 - m.x148 + m.x173 >= -600)

m.c139 = Constraint(expr= - 600*m.b20 - 600*m.b21 - 600*m.b23 - 600*m.b24 - 600*m.b26 - 600*m.b27 - m.x151 + m.x173
                          >= -600)

m.c140 = Constraint(expr= - 600*m.b21 - 600*m.b24 - 600*m.b27 - m.x154 + m.x173 >= -600)

m.c141 = Constraint(expr= - 600*m.b46 - 600*m.b47 - 600*m.b48 - 600*m.b49 - 600*m.b50 - 600*m.b51 - 600*m.b52
                          - 600*m.b53 - 600*m.b54 - m.x149 + m.x174 >= -600)

m.c142 = Constraint(expr= - 600*m.b47 - 600*m.b48 - 600*m.b50 - 600*m.b51 - 600*m.b53 - 600*m.b54 - m.x152 + m.x174
                          >= -600)

m.c143 = Constraint(expr= - 600*m.b48 - 600*m.b51 - 600*m.b54 - m.x155 + m.x174 >= -600)

m.c144 = Constraint(expr= - 600*m.b73 - 600*m.b74 - 600*m.b75 - 600*m.b76 - 600*m.b77 - 600*m.b78 - 600*m.b79
                          - 600*m.b80 - 600*m.b81 - m.x150 + m.x174 >= -600)

m.c145 = Constraint(expr= - 600*m.b74 - 600*m.b75 - 600*m.b77 - 600*m.b78 - 600*m.b80 - 600*m.b81 - m.x153 + m.x174
                          >= -600)

m.c146 = Constraint(expr= - 600*m.b75 - 600*m.b78 - 600*m.b81 - m.x156 + m.x174 >= -600)

m.c147 = Constraint(expr=   600*m.b1 + 600*m.b4 + 600*m.b7 - m.x157 + m.x175 <= 600)

m.c148 = Constraint(expr=   600*m.b1 + 600*m.b2 + 600*m.b4 + 600*m.b5 + 600*m.b7 + 600*m.b8 - m.x160 + m.x175 <= 600)

m.c149 = Constraint(expr=   600*m.b1 + 600*m.b2 + 600*m.b3 + 600*m.b4 + 600*m.b5 + 600*m.b6 + 600*m.b7 + 600*m.b8
                          + 600*m.b9 - m.x163 + m.x175 <= 600)

m.c150 = Constraint(expr=   600*m.b28 + 600*m.b31 + 600*m.b34 - m.x158 + m.x176 <= 600)

m.c151 = Constraint(expr=   600*m.b28 + 600*m.b29 + 600*m.b31 + 600*m.b32 + 600*m.b34 + 600*m.b35 - m.x161 + m.x176
                          <= 600)

m.c152 = Constraint(expr=   600*m.b28 + 600*m.b29 + 600*m.b30 + 600*m.b31 + 600*m.b32 + 600*m.b33 + 600*m.b34
                          + 600*m.b35 + 600*m.b36 - m.x164 + m.x176 <= 600)

m.c153 = Constraint(expr=   600*m.b55 + 600*m.b58 + 600*m.b61 - m.x159 + m.x176 <= 600)

m.c154 = Constraint(expr=   600*m.b55 + 600*m.b56 + 600*m.b58 + 600*m.b59 + 600*m.b61 + 600*m.b62 - m.x162 + m.x176
                          <= 600)

m.c155 = Constraint(expr=   600*m.b55 + 600*m.b56 + 600*m.b57 + 600*m.b58 + 600*m.b59 + 600*m.b60 + 600*m.b61
                          + 600*m.b62 + 600*m.b63 - m.x165 + m.x176 <= 600)

m.c156 = Constraint(expr=   600*m.b10 + 600*m.b13 + 600*m.b16 - m.x157 + m.x177 <= 600)

m.c157 = Constraint(expr=   600*m.b10 + 600*m.b11 + 600*m.b13 + 600*m.b14 + 600*m.b16 + 600*m.b17 - m.x160 + m.x177
                          <= 600)

m.c158 = Constraint(expr=   600*m.b10 + 600*m.b11 + 600*m.b12 + 600*m.b13 + 600*m.b14 + 600*m.b15 + 600*m.b16
                          + 600*m.b17 + 600*m.b18 - m.x163 + m.x177 <= 600)

m.c159 = Constraint(expr=   600*m.b37 + 600*m.b40 + 600*m.b43 - m.x158 + m.x178 <= 600)

m.c160 = Constraint(expr=   600*m.b37 + 600*m.b38 + 600*m.b40 + 600*m.b41 + 600*m.b43 + 600*m.b44 - m.x161 + m.x178
                          <= 600)

m.c161 = Constraint(expr=   600*m.b37 + 600*m.b38 + 600*m.b39 + 600*m.b40 + 600*m.b41 + 600*m.b42 + 600*m.b43
                          + 600*m.b44 + 600*m.b45 - m.x164 + m.x178 <= 600)

m.c162 = Constraint(expr=   600*m.b64 + 600*m.b67 + 600*m.b70 - m.x159 + m.x178 <= 600)

m.c163 = Constraint(expr=   600*m.b64 + 600*m.b65 + 600*m.b67 + 600*m.b68 + 600*m.b70 + 600*m.b71 - m.x162 + m.x178
                          <= 600)

m.c164 = Constraint(expr=   600*m.b64 + 600*m.b65 + 600*m.b66 + 600*m.b67 + 600*m.b68 + 600*m.b69 + 600*m.b70
                          + 600*m.b71 + 600*m.b72 - m.x165 + m.x178 <= 600)

m.c165 = Constraint(expr=   600*m.b19 + 600*m.b22 + 600*m.b25 - m.x157 + m.x179 <= 600)

m.c166 = Constraint(expr=   600*m.b19 + 600*m.b20 + 600*m.b22 + 600*m.b23 + 600*m.b25 + 600*m.b26 - m.x160 + m.x179
                          <= 600)

m.c167 = Constraint(expr=   600*m.b19 + 600*m.b20 + 600*m.b21 + 600*m.b22 + 600*m.b23 + 600*m.b24 + 600*m.b25
                          + 600*m.b26 + 600*m.b27 - m.x163 + m.x179 <= 600)

m.c168 = Constraint(expr=   600*m.b46 + 600*m.b49 + 600*m.b52 - m.x158 + m.x180 <= 600)

m.c169 = Constraint(expr=   600*m.b46 + 600*m.b47 + 600*m.b49 + 600*m.b50 + 600*m.b52 + 600*m.b53 - m.x161 + m.x180
                          <= 600)

m.c170 = Constraint(expr=   600*m.b46 + 600*m.b47 + 600*m.b48 + 600*m.b49 + 600*m.b50 + 600*m.b51 + 600*m.b52
                          + 600*m.b53 + 600*m.b54 - m.x164 + m.x180 <= 600)

m.c171 = Constraint(expr=   600*m.b73 + 600*m.b76 + 600*m.b79 - m.x159 + m.x180 <= 600)

m.c172 = Constraint(expr=   600*m.b73 + 600*m.b74 + 600*m.b76 + 600*m.b77 + 600*m.b79 + 600*m.b80 - m.x162 + m.x180
                          <= 600)

m.c173 = Constraint(expr=   600*m.b73 + 600*m.b74 + 600*m.b75 + 600*m.b76 + 600*m.b77 + 600*m.b78 + 600*m.b79
                          + 600*m.b80 + 600*m.b81 - m.x165 + m.x180 <= 600)

m.c174 = Constraint(expr= - 600*m.b1 - 600*m.b2 - 600*m.b3 - 600*m.b4 - 600*m.b5 - 600*m.b6 - 600*m.b7 - 600*m.b8
                          - 600*m.b9 - m.x157 + m.x175 >= -600)

m.c175 = Constraint(expr= - 600*m.b2 - 600*m.b3 - 600*m.b5 - 600*m.b6 - 600*m.b8 - 600*m.b9 - m.x160 + m.x175 >= -600)

m.c176 = Constraint(expr= - 600*m.b3 - 600*m.b6 - 600*m.b9 - m.x163 + m.x175 >= -600)

m.c177 = Constraint(expr= - 600*m.b28 - 600*m.b29 - 600*m.b30 - 600*m.b31 - 600*m.b32 - 600*m.b33 - 600*m.b34
                          - 600*m.b35 - 600*m.b36 - m.x158 + m.x176 >= -600)

m.c178 = Constraint(expr= - 600*m.b29 - 600*m.b30 - 600*m.b32 - 600*m.b33 - 600*m.b35 - 600*m.b36 - m.x161 + m.x176
                          >= -600)

m.c179 = Constraint(expr= - 600*m.b30 - 600*m.b33 - 600*m.b36 - m.x164 + m.x176 >= -600)

m.c180 = Constraint(expr= - 600*m.b55 - 600*m.b56 - 600*m.b57 - 600*m.b58 - 600*m.b59 - 600*m.b60 - 600*m.b61
                          - 600*m.b62 - 600*m.b63 - m.x159 + m.x176 >= -600)

m.c181 = Constraint(expr= - 600*m.b56 - 600*m.b57 - 600*m.b59 - 600*m.b60 - 600*m.b62 - 600*m.b63 - m.x162 + m.x176
                          >= -600)

m.c182 = Constraint(expr= - 600*m.b57 - 600*m.b60 - 600*m.b63 - m.x165 + m.x176 >= -600)

m.c183 = Constraint(expr= - 600*m.b10 - 600*m.b11 - 600*m.b12 - 600*m.b13 - 600*m.b14 - 600*m.b15 - 600*m.b16
                          - 600*m.b17 - 600*m.b18 - m.x157 + m.x177 >= -600)

m.c184 = Constraint(expr= - 600*m.b11 - 600*m.b12 - 600*m.b14 - 600*m.b15 - 600*m.b17 - 600*m.b18 - m.x160 + m.x177
                          >= -600)

m.c185 = Constraint(expr= - 600*m.b12 - 600*m.b15 - 600*m.b18 - m.x163 + m.x177 >= -600)

m.c186 = Constraint(expr= - 600*m.b37 - 600*m.b38 - 600*m.b39 - 600*m.b40 - 600*m.b41 - 600*m.b42 - 600*m.b43
                          - 600*m.b44 - 600*m.b45 - m.x158 + m.x178 >= -600)

m.c187 = Constraint(expr= - 600*m.b38 - 600*m.b39 - 600*m.b41 - 600*m.b42 - 600*m.b44 - 600*m.b45 - m.x161 + m.x178
                          >= -600)

m.c188 = Constraint(expr= - 600*m.b39 - 600*m.b42 - 600*m.b45 - m.x164 + m.x178 >= -600)

m.c189 = Constraint(expr= - 600*m.b64 - 600*m.b65 - 600*m.b66 - 600*m.b67 - 600*m.b68 - 600*m.b69 - 600*m.b70
                          - 600*m.b71 - 600*m.b72 - m.x159 + m.x178 >= -600)

m.c190 = Constraint(expr= - 600*m.b65 - 600*m.b66 - 600*m.b68 - 600*m.b69 - 600*m.b71 - 600*m.b72 - m.x162 + m.x178
                          >= -600)

m.c191 = Constraint(expr= - 600*m.b66 - 600*m.b69 - 600*m.b72 - m.x165 + m.x178 >= -600)

m.c192 = Constraint(expr= - 600*m.b19 - 600*m.b20 - 600*m.b21 - 600*m.b22 - 600*m.b23 - 600*m.b24 - 600*m.b25
                          - 600*m.b26 - 600*m.b27 - m.x157 + m.x179 >= -600)

m.c193 = Constraint(expr= - 600*m.b20 - 600*m.b21 - 600*m.b23 - 600*m.b24 - 600*m.b26 - 600*m.b27 - m.x160 + m.x179
                          >= -600)

m.c194 = Constraint(expr= - 600*m.b21 - 600*m.b24 - 600*m.b27 - m.x163 + m.x179 >= -600)

m.c195 = Constraint(expr= - 600*m.b46 - 600*m.b47 - 600*m.b48 - 600*m.b49 - 600*m.b50 - 600*m.b51 - 600*m.b52
                          - 600*m.b53 - 600*m.b54 - m.x158 + m.x180 >= -600)

m.c196 = Constraint(expr= - 600*m.b47 - 600*m.b48 - 600*m.b50 - 600*m.b51 - 600*m.b53 - 600*m.b54 - m.x161 + m.x180
                          >= -600)

m.c197 = Constraint(expr= - 600*m.b48 - 600*m.b51 - 600*m.b54 - m.x164 + m.x180 >= -600)

m.c198 = Constraint(expr= - 600*m.b73 - 600*m.b74 - 600*m.b75 - 600*m.b76 - 600*m.b77 - 600*m.b78 - 600*m.b79
                          - 600*m.b80 - 600*m.b81 - m.x159 + m.x180 >= -600)

m.c199 = Constraint(expr= - 600*m.b74 - 600*m.b75 - 600*m.b77 - 600*m.b78 - 600*m.b80 - 600*m.b81 - m.x162 + m.x180
                          >= -600)

m.c200 = Constraint(expr= - 600*m.b75 - 600*m.b78 - 600*m.b81 - m.x165 + m.x180 >= -600)

m.c201 = Constraint(expr=-m.x184*(m.x175 - m.x169) + m.x94 + m.x95 + m.x96 == 0)

m.c202 = Constraint(expr=-m.x185*(m.x176 - m.x170) + m.x97 + m.x98 + m.x99 + m.x100 + m.x101 + m.x102 == 0)

m.c203 = Constraint(expr=-m.x186*(m.x177 - m.x171) + m.x103 + m.x104 + m.x105 == 0)

m.c204 = Constraint(expr=-m.x187*(m.x178 - m.x172) + m.x106 + m.x107 + m.x108 + m.x109 + m.x110 + m.x111 == 0)

m.c205 = Constraint(expr=-m.x188*(m.x179 - m.x173) + m.x112 + m.x113 + m.x114 == 0)

m.c206 = Constraint(expr=-m.x189*(m.x180 - m.x174) + m.x115 + m.x116 + m.x117 + m.x118 + m.x119 + m.x120 == 0)

m.c207 = Constraint(expr= - 800*m.b1 - 800*m.b2 - 800*m.b3 - 800*m.b4 - 800*m.b5 - 800*m.b6 - 800*m.b7 - 800*m.b8
                          - 800*m.b9 + m.x184 <= 0)

m.c208 = Constraint(expr= - 900*m.b28 - 900*m.b29 - 900*m.b30 - 900*m.b31 - 900*m.b32 - 900*m.b33 - 900*m.b34
                          - 900*m.b35 - 900*m.b36 - 400*m.b55 - 400*m.b56 - 400*m.b57 - 400*m.b58 - 400*m.b59
                          - 400*m.b60 - 400*m.b61 - 400*m.b62 - 400*m.b63 + m.x185 <= 0)

m.c209 = Constraint(expr= - 1200*m.b10 - 1200*m.b11 - 1200*m.b12 - 1200*m.b13 - 1200*m.b14 - 1200*m.b15 - 1200*m.b16
                          - 1200*m.b17 - 1200*m.b18 + m.x186 <= 0)

m.c210 = Constraint(expr= - 600*m.b37 - 600*m.b38 - 600*m.b39 - 600*m.b40 - 600*m.b41 - 600*m.b42 - 600*m.b43
                          - 600*m.b44 - 600*m.b45 - 500*m.b64 - 500*m.b65 - 500*m.b66 - 500*m.b67 - 500*m.b68
                          - 500*m.b69 - 500*m.b70 - 500*m.b71 - 500*m.b72 + m.x187 <= 0)

m.c211 = Constraint(expr= - 1000*m.b19 - 1000*m.b20 - 1000*m.b21 - 1000*m.b22 - 1000*m.b23 - 1000*m.b24 - 1000*m.b25
                          - 1000*m.b26 - 1000*m.b27 + m.x188 <= 0)

m.c212 = Constraint(expr= - 1100*m.b46 - 1100*m.b47 - 1100*m.b48 - 1100*m.b49 - 1100*m.b50 - 1100*m.b51 - 1100*m.b52
                          - 1100*m.b53 - 1100*m.b54 - 450*m.b73 - 450*m.b74 - 450*m.b75 - 450*m.b76 - 450*m.b77
                          - 450*m.b78 - 450*m.b79 - 450*m.b80 - 450*m.b81 + m.x189 <= 0)

m.c213 = Constraint(expr=   m.x170 - m.x176 + m.x190 == 0)

m.c214 = Constraint(expr=   m.x172 - m.x178 + m.x191 == 0)

m.c215 = Constraint(expr=   m.x174 - m.x180 + m.x192 == 0)

m.c216 = Constraint(expr=   m.x190 - m.x193 <= 0)

m.c217 = Constraint(expr=   m.x191 - m.x193 <= 0)

m.c218 = Constraint(expr=   m.x192 - m.x193 <= 0)

m.c219 = Constraint(expr=   600*m.b82 + 600*m.b88 + m.x169 - m.x170 <= 600)

m.c220 = Constraint(expr=   600*m.b83 + 600*m.b89 + m.x171 - m.x172 <= 600)

m.c221 = Constraint(expr=   600*m.b84 + 600*m.b90 + m.x173 - m.x174 <= 600)

m.c222 = Constraint(expr= - 600*m.b85 - 600*m.b91 + m.x169 - m.x170 >= -600)

m.c223 = Constraint(expr= - 600*m.b86 - 600*m.b92 + m.x171 - m.x172 >= -600)

m.c224 = Constraint(expr= - 600*m.b87 - 600*m.b93 + m.x173 - m.x174 >= -600)

m.c225 = Constraint(expr=   1200*m.b82 + 1200*m.b91 + m.x175 - m.x176 <= 1200)

m.c226 = Constraint(expr=   1200*m.b83 + 1200*m.b92 + m.x177 - m.x178 <= 1200)

m.c227 = Constraint(expr=   1200*m.b84 + 1200*m.b93 + m.x179 - m.x180 <= 1200)

m.c228 = Constraint(expr= - 1200*m.b85 - 1200*m.b88 + m.x175 - m.x176 >= -1200)

m.c229 = Constraint(expr= - 1200*m.b86 - 1200*m.b89 + m.x177 - m.x178 >= -1200)

m.c230 = Constraint(expr= - 1200*m.b87 - 1200*m.b90 + m.x179 - m.x180 >= -1200)

m.c231 = Constraint(expr= - 600*m.b82 - 600*m.b85 - 600*m.b88 - 600*m.b91 - m.x170 + m.x175 >= -600)

m.c232 = Constraint(expr= - 600*m.b83 - 600*m.b86 - 600*m.b89 - 600*m.b92 - m.x172 + m.x177 >= -600)

m.c233 = Constraint(expr= - 600*m.b84 - 600*m.b87 - 600*m.b90 - 600*m.b93 - m.x174 + m.x179 >= -600)

m.c234 = Constraint(expr= - 600*m.b82 - 600*m.b85 - 600*m.b88 - 600*m.b91 - m.x169 + m.x176 >= -600)

m.c235 = Constraint(expr= - 600*m.b83 - 600*m.b86 - 600*m.b89 - 600*m.b92 - m.x171 + m.x178 >= -600)

m.c236 = Constraint(expr= - 600*m.b84 - 600*m.b87 - 600*m.b90 - 600*m.b93 - m.x173 + m.x180 >= -600)

m.c237 = Constraint(expr=-(m.x170 - m.x169)*m.x184 - 480000*m.b82 + m.x166 >= -480000)

m.c238 = Constraint(expr=-(m.x172 - m.x171)*m.x186 - 360000*m.b83 + m.x167 >= -360000)

m.c239 = Constraint(expr=-(m.x174 - m.x173)*m.x188 - 600000*m.b84 + m.x168 >= -600000)

m.c240 = Constraint(expr=-(m.x176 - m.x175)*m.x185 - 480000*m.b82 + m.x166 >= -480000)

m.c241 = Constraint(expr=-(m.x178 - m.x177)*m.x187 - 360000*m.b83 + m.x167 >= -360000)

m.c242 = Constraint(expr=-(m.x180 - m.x179)*m.x189 - 600000*m.b84 + m.x168 >= -600000)

m.c243 = Constraint(expr=-(m.x169 - m.x170)*m.x185 - 480000*m.b85 + m.x166 >= -480000)

m.c244 = Constraint(expr=-(m.x171 - m.x172)*m.x187 - 360000*m.b86 + m.x167 >= -360000)

m.c245 = Constraint(expr=-(m.x173 - m.x174)*m.x189 - 600000*m.b87 + m.x168 >= -600000)

m.c246 = Constraint(expr=-(m.x175 - m.x176)*m.x184 - 480000*m.b85 + m.x166 >= -480000)

m.c247 = Constraint(expr=-(m.x177 - m.x178)*m.x186 - 360000*m.b86 + m.x167 >= -360000)

m.c248 = Constraint(expr=-(m.x179 - m.x180)*m.x188 - 600000*m.b87 + m.x168 >= -600000)

m.c249 = Constraint(expr=-(m.x185 - m.x184)*(m.x176 - m.x170) - 480000*m.b88 + m.x166 >= -480000)

m.c250 = Constraint(expr=-(m.x187 - m.x186)*(m.x178 - m.x172) - 360000*m.b89 + m.x167 >= -360000)

m.c251 = Constraint(expr=-(m.x189 - m.x188)*(m.x180 - m.x174) - 600000*m.b90 + m.x168 >= -600000)

m.c252 = Constraint(expr=-(m.x184 - m.x185)*(m.x175 - m.x169) - 480000*m.b91 + m.x166 >= -480000)

m.c253 = Constraint(expr=-(m.x186 - m.x187)*(m.x177 - m.x171) - 360000*m.b92 + m.x167 >= -360000)

m.c254 = Constraint(expr=-(m.x188 - m.x189)*(m.x179 - m.x173) - 600000*m.b93 + m.x168 >= -600000)

m.c255 = Constraint(expr=   480000*m.b82 + 480000*m.b85 + 480000*m.b88 + 480000*m.b91 - m.x94 - m.x95 - m.x96 + m.x166
                          >= 0)

m.c256 = Constraint(expr=   360000*m.b83 + 360000*m.b86 + 360000*m.b89 + 360000*m.b92 - m.x103 - m.x104 - m.x105
                          + m.x167 >= 0)

m.c257 = Constraint(expr=   600000*m.b84 + 600000*m.b87 + 600000*m.b90 + 600000*m.b93 - m.x112 - m.x113 - m.x114
                          + m.x168 >= 0)
