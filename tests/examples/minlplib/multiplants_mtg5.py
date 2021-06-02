#  MINLP written by GAMS Convert at 04/21/18 13:52:37
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        309       72      129      108        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        191      113       78        0        0        0        0        0
#  FX     28       28        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1850     1686      164        0


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
m.x106 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x107 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x108 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x109 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x110 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x111 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x112 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x113 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x114 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x115 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x116 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x117 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x118 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x119 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x120 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x121 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x122 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x123 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x124 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x125 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x126 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x127 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x128 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x129 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x130 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x131 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x132 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x133 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x134 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x135 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x136 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x137 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x138 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x139 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x140 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x141 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x142 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x143 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x144 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x145 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x146 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x147 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x148 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x149 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x150 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x151 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x152 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x153 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x154 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x155 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x156 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x157 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x158 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x159 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x160 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x161 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x162 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x163 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x164 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x165 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x166 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x167 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x168 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x169 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x170 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x171 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x172 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x173 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x174 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x175 = Var(within=Reals,bounds=(150,None),initialize=150)
m.x176 = Var(within=Reals,bounds=(250,None),initialize=250)
m.x177 = Var(within=Reals,bounds=(500,None),initialize=500)
m.x178 = Var(within=Reals,bounds=(0,None),initialize=1170)
m.x179 = Var(within=Reals,bounds=(0,None),initialize=1120)
m.x180 = Var(within=Reals,bounds=(0,None),initialize=1120)
m.x181 = Var(within=Reals,bounds=(0,None),initialize=1340)
m.x182 = Var(within=Reals,bounds=(0,None),initialize=1290)
m.x183 = Var(within=Reals,bounds=(0,None),initialize=1860)
m.x184 = Var(within=Reals,bounds=(0,None),initialize=1340)
m.x185 = Var(within=Reals,bounds=(0,None),initialize=1340)
m.x186 = Var(within=Reals,bounds=(0,None),initialize=1340)
m.x187 = Var(within=Reals,bounds=(26.7857142857143,600),initialize=26.7857142857143)
m.x188 = Var(within=Reals,bounds=(26.8817204301075,600),initialize=26.8817204301075)
m.x189 = Var(within=Reals,bounds=(74.6268656716418,600),initialize=74.6268656716418)
m.x190 = Var(within=Reals,bounds=(200,600),initialize=200)
m.x191 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=m.x191, sense=maximize)

m.c1 = Constraint(expr=m.x191*m.x190 + 0.00203*(m.x187**2*(m.x180 - m.x175) + (m.x190 - m.x187)**2*m.x175) + 0.00203*(
                       m.x188**2*(m.x183 - m.x176) + (m.x190 - m.x188)**2*m.x176) + 0.00203*(m.x189**2*(m.x186 - m.x177)
                        + (m.x190 - m.x189)**2*m.x177) + 7600*m.b1 + 7600*m.b2 + 7600*m.b3 + 7600*m.b4 + 7600*m.b5
                        + 7600*m.b6 + 7500*m.b7 + 7500*m.b8 + 7500*m.b9 + 750*m.b10 + 750*m.b11 + 750*m.b12 + 7700*m.b13
                        + 7700*m.b14 + 7700*m.b15 + 770*m.b16 + 770*m.b17 + 770*m.b18 + 2280*m.b19 + 2280*m.b20
                        + 2280*m.b21 + 2280*m.b22 + 2280*m.b23 + 2280*m.b24 + 2250*m.b25 + 2250*m.b26 + 2250*m.b27
                        + 750*m.b28 + 750*m.b29 + 750*m.b30 + 2310*m.b31 + 2310*m.b32 + 2310*m.b33 + 770*m.b34
                        + 770*m.b35 + 770*m.b36 + 1520*m.b37 + 1520*m.b38 + 1520*m.b39 + 1520*m.b40 + 1520*m.b41
                        + 1520*m.b42 + 1500*m.b43 + 1500*m.b44 + 1500*m.b45 + 750*m.b46 + 750*m.b47 + 750*m.b48
                        + 1540*m.b49 + 1540*m.b50 + 1540*m.b51 + 770*m.b52 + 770*m.b53 + 770*m.b54 - 4*m.x85 - 4*m.x86
                        - 4*m.x87 - 1.5*m.x94 - 1.5*m.x95 - 1.5*m.x96 - 6.5*m.x103 - 6.5*m.x104 - 6.5*m.x105
                        + 0.1218*m.x151 + 0.1218*m.x152 + 0.1218*m.x153 + 0.1218*m.x154 + 0.1218*m.x155 + 0.1218*m.x156
                        == 0)

m.c2 = Constraint(expr=   m.b1 + m.b4 - m.b9 - m.b15 + m.x106 - m.x108 == 0)

m.c3 = Constraint(expr=   m.b2 + m.b5 - m.b7 - m.b13 - m.x106 + m.x107 == 0)

m.c4 = Constraint(expr=   m.b3 + m.b6 - m.b8 - m.b14 - m.x107 + m.x108 == 0)

m.c5 = Constraint(expr= - m.b3 + m.b7 + m.b10 - m.b18 + m.x109 - m.x111 == 0)

m.c6 = Constraint(expr= - m.b1 + m.b8 + m.b11 - m.b16 - m.x109 + m.x110 == 0)

m.c7 = Constraint(expr= - m.b2 + m.b9 + m.b12 - m.b17 - m.x110 + m.x111 == 0)

m.c8 = Constraint(expr= - m.b6 - m.b12 + m.b13 + m.b16 + m.x112 - m.x114 == 0)

m.c9 = Constraint(expr= - m.b4 - m.b10 + m.b14 + m.b17 - m.x112 + m.x113 == 0)

m.c10 = Constraint(expr= - m.b5 - m.b11 + m.b15 + m.b18 - m.x113 + m.x114 == 0)

m.c11 = Constraint(expr=   m.b19 + m.b22 - m.b27 - m.b33 + m.x115 - m.x117 == 0)

m.c12 = Constraint(expr=   m.b20 + m.b23 - m.b25 - m.b31 - m.x115 + m.x116 == 0)

m.c13 = Constraint(expr=   m.b21 + m.b24 - m.b26 - m.b32 - m.x116 + m.x117 == 0)

m.c14 = Constraint(expr= - m.b21 + m.b25 + m.b28 - m.b36 + m.x118 - m.x120 == 0)

m.c15 = Constraint(expr= - m.b19 + m.b26 + m.b29 - m.b34 - m.x118 + m.x119 == 0)

m.c16 = Constraint(expr= - m.b20 + m.b27 + m.b30 - m.b35 - m.x119 + m.x120 == 0)

m.c17 = Constraint(expr= - m.b24 - m.b30 + m.b31 + m.b34 + m.x121 - m.x123 == 0)

m.c18 = Constraint(expr= - m.b22 - m.b28 + m.b32 + m.b35 - m.x121 + m.x122 == 0)

m.c19 = Constraint(expr= - m.b23 - m.b29 + m.b33 + m.b36 - m.x122 + m.x123 == 0)

m.c20 = Constraint(expr=   m.b37 + m.b40 - m.b45 - m.b51 + m.x124 - m.x126 == 0)

m.c21 = Constraint(expr=   m.b38 + m.b41 - m.b43 - m.b49 - m.x124 + m.x125 == 0)

m.c22 = Constraint(expr=   m.b39 + m.b42 - m.b44 - m.b50 - m.x125 + m.x126 == 0)

m.c23 = Constraint(expr= - m.b39 + m.b43 + m.b46 - m.b54 + m.x127 - m.x129 == 0)

m.c24 = Constraint(expr= - m.b37 + m.b44 + m.b47 - m.b52 - m.x127 + m.x128 == 0)

m.c25 = Constraint(expr= - m.b38 + m.b45 + m.b48 - m.b53 - m.x128 + m.x129 == 0)

m.c26 = Constraint(expr= - m.b42 - m.b48 + m.b49 + m.b52 + m.x130 - m.x132 == 0)

m.c27 = Constraint(expr= - m.b40 - m.b46 + m.b50 + m.b53 - m.x130 + m.x131 == 0)

m.c28 = Constraint(expr= - m.b41 - m.b47 + m.b51 + m.b54 - m.x131 + m.x132 == 0)

m.c29 = Constraint(expr=   m.b1 + m.b4 + m.b7 + m.b10 + m.b13 + m.b16 + m.x106 + m.x109 + m.x112 == 1)

m.c30 = Constraint(expr=   m.b19 + m.b22 + m.b25 + m.b28 + m.b31 + m.b34 + m.x115 + m.x118 + m.x121 == 1)

m.c31 = Constraint(expr=   m.b37 + m.b40 + m.b43 + m.b46 + m.b49 + m.b52 + m.x124 + m.x127 + m.x130 == 1)

m.c32 = Constraint(expr= - 10*m.b1 - 10*m.b4 - 10*m.b7 - m.b10 - 10*m.b13 - m.b16 - 0.000854700854700855*m.x79
                         - 0.000746268656716418*m.x88 - 0.000746268656716418*m.x97 - m.x133 + m.x136 >= 0)

m.c33 = Constraint(expr= - 10*m.b2 - 10*m.b5 - 10*m.b8 - m.b11 - 10*m.b14 - m.b17 - 0.000854700854700855*m.x80
                         - 0.000746268656716418*m.x89 - 0.000746268656716418*m.x98 - m.x136 + m.x139 >= 0)

m.c34 = Constraint(expr= - 10*m.b3 - 10*m.b6 - 10*m.b9 - m.b12 - 10*m.b15 - m.b18 - 0.000854700854700855*m.x81
                         - 0.000746268656716418*m.x90 - 0.000746268656716418*m.x99 + m.x133 - m.x139 + m.x190 >= 0)

m.c35 = Constraint(expr= - 3*m.b19 - 3*m.b22 - 3*m.b25 - m.b28 - 3*m.b31 - m.b34 - 0.000892857142857143*m.x82
                         - 0.000775193798449612*m.x91 - 0.000746268656716418*m.x100 - m.x134 + m.x137 >= 0)

m.c36 = Constraint(expr= - 3*m.b20 - 3*m.b23 - 3*m.b26 - m.b29 - 3*m.b32 - m.b35 - 0.000892857142857143*m.x83
                         - 0.000775193798449612*m.x92 - 0.000746268656716418*m.x101 - m.x137 + m.x140 >= 0)

m.c37 = Constraint(expr= - 3*m.b21 - 3*m.b24 - 3*m.b27 - m.b30 - 3*m.b33 - m.b36 - 0.000892857142857143*m.x84
                         - 0.000775193798449612*m.x93 - 0.000746268656716418*m.x102 + m.x134 - m.x140 + m.x190 >= 0)

m.c38 = Constraint(expr= - 2*m.b37 - 2*m.b40 - 2*m.b43 - m.b46 - 2*m.b49 - m.b52 - 0.000892857142857143*m.x85
                         - 0.000537634408602151*m.x94 - 0.000746268656716418*m.x103 - m.x135 + m.x138 >= 0)

m.c39 = Constraint(expr= - 2*m.b38 - 2*m.b41 - 2*m.b44 - m.b47 - 2*m.b50 - m.b53 - 0.000892857142857143*m.x86
                         - 0.000537634408602151*m.x95 - 0.000746268656716418*m.x104 - m.x138 + m.x141 >= 0)

m.c40 = Constraint(expr= - 2*m.b39 - 2*m.b42 - 2*m.b45 - m.b48 - 2*m.b51 - m.b54 - 0.000892857142857143*m.x87
                         - 0.000537634408602151*m.x96 - 0.000746268656716418*m.x105 + m.x135 - m.x141 + m.x190 >= 0)

m.c41 = Constraint(expr= - 10*m.b1 - 10*m.b4 - 10*m.b7 - m.b10 - 10*m.b13 - m.b16 + m.x136 - m.x142 == 0)

m.c42 = Constraint(expr= - 10*m.b2 - 10*m.b5 - 10*m.b8 - m.b11 - 10*m.b14 - m.b17 + m.x139 - m.x145 == 0)

m.c43 = Constraint(expr= - 10*m.b3 - 10*m.b6 - 10*m.b9 - m.b12 - 10*m.b15 - m.b18 + m.x133 - m.x148 + m.x190 == 0)

m.c44 = Constraint(expr= - 3*m.b19 - 3*m.b22 - 3*m.b25 - m.b28 - 3*m.b31 - m.b34 + m.x137 - m.x143 == 0)

m.c45 = Constraint(expr= - 3*m.b20 - 3*m.b23 - 3*m.b26 - m.b29 - 3*m.b32 - m.b35 + m.x140 - m.x146 == 0)

m.c46 = Constraint(expr= - 3*m.b21 - 3*m.b24 - 3*m.b27 - m.b30 - 3*m.b33 - m.b36 + m.x134 - m.x149 + m.x190 == 0)

m.c47 = Constraint(expr= - 2*m.b37 - 2*m.b40 - 2*m.b43 - m.b46 - 2*m.b49 - m.b52 + m.x138 - m.x144 == 0)

m.c48 = Constraint(expr= - 2*m.b38 - 2*m.b41 - 2*m.b44 - m.b47 - 2*m.b50 - m.b53 + m.x141 - m.x147 == 0)

m.c49 = Constraint(expr= - 2*m.b39 - 2*m.b42 - 2*m.b45 - m.b48 - 2*m.b51 - m.b54 + m.x135 - m.x150 + m.x190 == 0)

m.c50 = Constraint(expr=   m.x139 - m.x190 <= 0)

m.c51 = Constraint(expr=   m.x140 - m.x190 <= 0)

m.c52 = Constraint(expr=   m.x141 - m.x190 <= 0)

m.c53 = Constraint(expr= - 702000*m.b1 - 702000*m.b4 + m.x79 <= 0)

m.c54 = Constraint(expr= - 702000*m.b2 - 702000*m.b5 + m.x80 <= 0)

m.c55 = Constraint(expr= - 702000*m.b3 - 702000*m.b6 + m.x81 <= 0)

m.c56 = Constraint(expr= - 672000*m.b19 - 672000*m.b22 + m.x82 <= 0)

m.c57 = Constraint(expr= - 672000*m.b20 - 672000*m.b23 + m.x83 <= 0)

m.c58 = Constraint(expr= - 672000*m.b21 - 672000*m.b24 + m.x84 <= 0)

m.c59 = Constraint(expr= - 672000*m.b37 - 672000*m.b40 + m.x85 <= 0)

m.c60 = Constraint(expr= - 672000*m.b38 - 672000*m.b41 + m.x86 <= 0)

m.c61 = Constraint(expr= - 672000*m.b39 - 672000*m.b42 + m.x87 <= 0)

m.c62 = Constraint(expr= - 804000*m.b7 - 804000*m.b10 + m.x88 <= 0)

m.c63 = Constraint(expr= - 804000*m.b8 - 804000*m.b11 + m.x89 <= 0)

m.c64 = Constraint(expr= - 804000*m.b9 - 804000*m.b12 + m.x90 <= 0)

m.c65 = Constraint(expr= - 774000*m.b25 - 774000*m.b28 + m.x91 <= 0)

m.c66 = Constraint(expr= - 774000*m.b26 - 774000*m.b29 + m.x92 <= 0)

m.c67 = Constraint(expr= - 774000*m.b27 - 774000*m.b30 + m.x93 <= 0)

m.c68 = Constraint(expr= - 1116000*m.b43 - 1116000*m.b46 + m.x94 <= 0)

m.c69 = Constraint(expr= - 1116000*m.b44 - 1116000*m.b47 + m.x95 <= 0)

m.c70 = Constraint(expr= - 1116000*m.b45 - 1116000*m.b48 + m.x96 <= 0)

m.c71 = Constraint(expr= - 804000*m.b13 - 804000*m.b16 + m.x97 <= 0)

m.c72 = Constraint(expr= - 804000*m.b14 - 804000*m.b17 + m.x98 <= 0)

m.c73 = Constraint(expr= - 804000*m.b15 - 804000*m.b18 + m.x99 <= 0)

m.c74 = Constraint(expr= - 804000*m.b31 - 804000*m.b34 + m.x100 <= 0)

m.c75 = Constraint(expr= - 804000*m.b32 - 804000*m.b35 + m.x101 <= 0)

m.c76 = Constraint(expr= - 804000*m.b33 - 804000*m.b36 + m.x102 <= 0)

m.c77 = Constraint(expr= - 804000*m.b49 - 804000*m.b52 + m.x103 <= 0)

m.c78 = Constraint(expr= - 804000*m.b50 - 804000*m.b53 + m.x104 <= 0)

m.c79 = Constraint(expr= - 804000*m.b51 - 804000*m.b54 + m.x105 <= 0)

m.c80 = Constraint(expr=   m.b1 + m.b2 + m.b3 + m.b4 + m.b5 + m.b6 == 1)

m.c81 = Constraint(expr=   m.b19 + m.b20 + m.b21 + m.b22 + m.b23 + m.b24 == 1)

m.c82 = Constraint(expr=   m.b37 + m.b38 + m.b39 + m.b40 + m.b41 + m.b42 == 1)

m.c83 = Constraint(expr=   m.b7 + m.b8 + m.b9 + m.b10 + m.b11 + m.b12 == 1)

m.c84 = Constraint(expr=   m.b25 + m.b26 + m.b27 + m.b28 + m.b29 + m.b30 == 1)

m.c85 = Constraint(expr=   m.b43 + m.b44 + m.b45 + m.b46 + m.b47 + m.b48 == 1)

m.c86 = Constraint(expr=   m.b13 + m.b14 + m.b15 + m.b16 + m.b17 + m.b18 == 1)

m.c87 = Constraint(expr=   m.b31 + m.b32 + m.b33 + m.b34 + m.b35 + m.b36 == 1)

m.c88 = Constraint(expr=   m.b49 + m.b50 + m.b51 + m.b52 + m.b53 + m.b54 == 1)

m.c89 = Constraint(expr=   m.b1 + m.b4 == 1)

m.c90 = Constraint(expr=m.x175*m.x190 - m.x85 - m.x86 - m.x87 == 0)

m.c91 = Constraint(expr=m.x176*m.x190 - m.x94 - m.x95 - m.x96 == 0)

m.c92 = Constraint(expr=m.x177*m.x190 - m.x103 - m.x104 - m.x105 == 0)

m.c93 = Constraint(expr=   m.x79 + m.x80 + m.x81 - m.x82 - m.x83 - m.x84 == 0)

m.c94 = Constraint(expr=   m.x82 + m.x83 + m.x84 - m.x85 - m.x86 - m.x87 == 0)

m.c95 = Constraint(expr=   m.x88 + m.x89 + m.x90 - m.x91 - m.x92 - m.x93 == 0)

m.c96 = Constraint(expr=   m.x91 + m.x92 + m.x93 - m.x94 - m.x95 - m.x96 == 0)

m.c97 = Constraint(expr=   m.x97 + m.x98 + m.x99 - m.x100 - m.x101 - m.x102 == 0)

m.c98 = Constraint(expr=   m.x100 + m.x101 + m.x102 - m.x103 - m.x104 - m.x105 == 0)

m.c99 = Constraint(expr=   600*m.b1 + 600*m.b4 - m.x133 + m.x157 <= 600)

m.c100 = Constraint(expr=   600*m.b1 + 600*m.b2 + 600*m.b4 + 600*m.b5 - m.x136 + m.x157 <= 600)

m.c101 = Constraint(expr=   600*m.b1 + 600*m.b2 + 600*m.b3 + 600*m.b4 + 600*m.b5 + 600*m.b6 - m.x139 + m.x157 <= 600)

m.c102 = Constraint(expr=   600*m.b19 + 600*m.b22 - m.x134 + m.x158 <= 600)

m.c103 = Constraint(expr=   600*m.b19 + 600*m.b20 + 600*m.b22 + 600*m.b23 - m.x137 + m.x158 <= 600)

m.c104 = Constraint(expr=   600*m.b19 + 600*m.b20 + 600*m.b21 + 600*m.b22 + 600*m.b23 + 600*m.b24 - m.x140 + m.x158
                          <= 600)

m.c105 = Constraint(expr=   600*m.b37 + 600*m.b40 - m.x135 + m.x159 <= 600)

m.c106 = Constraint(expr=   600*m.b37 + 600*m.b38 + 600*m.b40 + 600*m.b41 - m.x138 + m.x159 <= 600)

m.c107 = Constraint(expr=   600*m.b37 + 600*m.b38 + 600*m.b39 + 600*m.b40 + 600*m.b41 + 600*m.b42 - m.x141 + m.x159
                          <= 600)

m.c108 = Constraint(expr=   600*m.b7 + 600*m.b10 - m.x133 + m.x160 <= 600)

m.c109 = Constraint(expr=   600*m.b7 + 600*m.b8 + 600*m.b10 + 600*m.b11 - m.x136 + m.x160 <= 600)

m.c110 = Constraint(expr=   600*m.b7 + 600*m.b8 + 600*m.b9 + 600*m.b10 + 600*m.b11 + 600*m.b12 - m.x139 + m.x160 <= 600)

m.c111 = Constraint(expr=   600*m.b25 + 600*m.b28 - m.x134 + m.x161 <= 600)

m.c112 = Constraint(expr=   600*m.b25 + 600*m.b26 + 600*m.b28 + 600*m.b29 - m.x137 + m.x161 <= 600)

m.c113 = Constraint(expr=   600*m.b25 + 600*m.b26 + 600*m.b27 + 600*m.b28 + 600*m.b29 + 600*m.b30 - m.x140 + m.x161
                          <= 600)

m.c114 = Constraint(expr=   600*m.b43 + 600*m.b46 - m.x135 + m.x162 <= 600)

m.c115 = Constraint(expr=   600*m.b43 + 600*m.b44 + 600*m.b46 + 600*m.b47 - m.x138 + m.x162 <= 600)

m.c116 = Constraint(expr=   600*m.b43 + 600*m.b44 + 600*m.b45 + 600*m.b46 + 600*m.b47 + 600*m.b48 - m.x141 + m.x162
                          <= 600)

m.c117 = Constraint(expr=   600*m.b13 + 600*m.b16 - m.x133 + m.x163 <= 600)

m.c118 = Constraint(expr=   600*m.b13 + 600*m.b14 + 600*m.b16 + 600*m.b17 - m.x136 + m.x163 <= 600)

m.c119 = Constraint(expr=   600*m.b13 + 600*m.b14 + 600*m.b15 + 600*m.b16 + 600*m.b17 + 600*m.b18 - m.x139 + m.x163
                          <= 600)

m.c120 = Constraint(expr=   600*m.b31 + 600*m.b34 - m.x134 + m.x164 <= 600)

m.c121 = Constraint(expr=   600*m.b31 + 600*m.b32 + 600*m.b34 + 600*m.b35 - m.x137 + m.x164 <= 600)

m.c122 = Constraint(expr=   600*m.b31 + 600*m.b32 + 600*m.b33 + 600*m.b34 + 600*m.b35 + 600*m.b36 - m.x140 + m.x164
                          <= 600)

m.c123 = Constraint(expr=   600*m.b49 + 600*m.b52 - m.x135 + m.x165 <= 600)

m.c124 = Constraint(expr=   600*m.b49 + 600*m.b50 + 600*m.b52 + 600*m.b53 - m.x138 + m.x165 <= 600)

m.c125 = Constraint(expr=   600*m.b49 + 600*m.b50 + 600*m.b51 + 600*m.b52 + 600*m.b53 + 600*m.b54 - m.x141 + m.x165
                          <= 600)

m.c126 = Constraint(expr= - 600*m.b1 - 600*m.b2 - 600*m.b3 - 600*m.b4 - 600*m.b5 - 600*m.b6 - m.x133 + m.x157 >= -600)

m.c127 = Constraint(expr= - 600*m.b2 - 600*m.b3 - 600*m.b5 - 600*m.b6 - m.x136 + m.x157 >= -600)

m.c128 = Constraint(expr= - 600*m.b3 - 600*m.b6 - m.x139 + m.x157 >= -600)

m.c129 = Constraint(expr= - 600*m.b19 - 600*m.b20 - 600*m.b21 - 600*m.b22 - 600*m.b23 - 600*m.b24 - m.x134 + m.x158
                          >= -600)

m.c130 = Constraint(expr= - 600*m.b20 - 600*m.b21 - 600*m.b23 - 600*m.b24 - m.x137 + m.x158 >= -600)

m.c131 = Constraint(expr= - 600*m.b21 - 600*m.b24 - m.x140 + m.x158 >= -600)

m.c132 = Constraint(expr= - 600*m.b37 - 600*m.b38 - 600*m.b39 - 600*m.b40 - 600*m.b41 - 600*m.b42 - m.x135 + m.x159
                          >= -600)

m.c133 = Constraint(expr= - 600*m.b38 - 600*m.b39 - 600*m.b41 - 600*m.b42 - m.x138 + m.x159 >= -600)

m.c134 = Constraint(expr= - 600*m.b39 - 600*m.b42 - m.x141 + m.x159 >= -600)

m.c135 = Constraint(expr= - 600*m.b7 - 600*m.b8 - 600*m.b9 - 600*m.b10 - 600*m.b11 - 600*m.b12 - m.x133 + m.x160
                          >= -600)

m.c136 = Constraint(expr= - 600*m.b8 - 600*m.b9 - 600*m.b11 - 600*m.b12 - m.x136 + m.x160 >= -600)

m.c137 = Constraint(expr= - 600*m.b9 - 600*m.b12 - m.x139 + m.x160 >= -600)

m.c138 = Constraint(expr= - 600*m.b25 - 600*m.b26 - 600*m.b27 - 600*m.b28 - 600*m.b29 - 600*m.b30 - m.x134 + m.x161
                          >= -600)

m.c139 = Constraint(expr= - 600*m.b26 - 600*m.b27 - 600*m.b29 - 600*m.b30 - m.x137 + m.x161 >= -600)

m.c140 = Constraint(expr= - 600*m.b27 - 600*m.b30 - m.x140 + m.x161 >= -600)

m.c141 = Constraint(expr= - 600*m.b43 - 600*m.b44 - 600*m.b45 - 600*m.b46 - 600*m.b47 - 600*m.b48 - m.x135 + m.x162
                          >= -600)

m.c142 = Constraint(expr= - 600*m.b44 - 600*m.b45 - 600*m.b47 - 600*m.b48 - m.x138 + m.x162 >= -600)

m.c143 = Constraint(expr= - 600*m.b45 - 600*m.b48 - m.x141 + m.x162 >= -600)

m.c144 = Constraint(expr= - 600*m.b13 - 600*m.b14 - 600*m.b15 - 600*m.b16 - 600*m.b17 - 600*m.b18 - m.x133 + m.x163
                          >= -600)

m.c145 = Constraint(expr= - 600*m.b14 - 600*m.b15 - 600*m.b17 - 600*m.b18 - m.x136 + m.x163 >= -600)

m.c146 = Constraint(expr= - 600*m.b15 - 600*m.b18 - m.x139 + m.x163 >= -600)

m.c147 = Constraint(expr= - 600*m.b31 - 600*m.b32 - 600*m.b33 - 600*m.b34 - 600*m.b35 - 600*m.b36 - m.x134 + m.x164
                          >= -600)

m.c148 = Constraint(expr= - 600*m.b32 - 600*m.b33 - 600*m.b35 - 600*m.b36 - m.x137 + m.x164 >= -600)

m.c149 = Constraint(expr= - 600*m.b33 - 600*m.b36 - m.x140 + m.x164 >= -600)

m.c150 = Constraint(expr= - 600*m.b49 - 600*m.b50 - 600*m.b51 - 600*m.b52 - 600*m.b53 - 600*m.b54 - m.x135 + m.x165
                          >= -600)

m.c151 = Constraint(expr= - 600*m.b50 - 600*m.b51 - 600*m.b53 - 600*m.b54 - m.x138 + m.x165 >= -600)

m.c152 = Constraint(expr= - 600*m.b51 - 600*m.b54 - m.x141 + m.x165 >= -600)

m.c153 = Constraint(expr=   600*m.b1 + 600*m.b4 - m.x142 + m.x166 <= 600)

m.c154 = Constraint(expr=   600*m.b1 + 600*m.b2 + 600*m.b4 + 600*m.b5 - m.x145 + m.x166 <= 600)

m.c155 = Constraint(expr=   600*m.b1 + 600*m.b2 + 600*m.b3 + 600*m.b4 + 600*m.b5 + 600*m.b6 - m.x148 + m.x166 <= 600)

m.c156 = Constraint(expr=   600*m.b19 + 600*m.b22 - m.x143 + m.x167 <= 600)

m.c157 = Constraint(expr=   600*m.b19 + 600*m.b20 + 600*m.b22 + 600*m.b23 - m.x146 + m.x167 <= 600)

m.c158 = Constraint(expr=   600*m.b19 + 600*m.b20 + 600*m.b21 + 600*m.b22 + 600*m.b23 + 600*m.b24 - m.x149 + m.x167
                          <= 600)

m.c159 = Constraint(expr=   600*m.b37 + 600*m.b40 - m.x144 + m.x168 <= 600)

m.c160 = Constraint(expr=   600*m.b37 + 600*m.b38 + 600*m.b40 + 600*m.b41 - m.x147 + m.x168 <= 600)

m.c161 = Constraint(expr=   600*m.b37 + 600*m.b38 + 600*m.b39 + 600*m.b40 + 600*m.b41 + 600*m.b42 - m.x150 + m.x168
                          <= 600)

m.c162 = Constraint(expr=   600*m.b7 + 600*m.b10 - m.x142 + m.x169 <= 600)

m.c163 = Constraint(expr=   600*m.b7 + 600*m.b8 + 600*m.b10 + 600*m.b11 - m.x145 + m.x169 <= 600)

m.c164 = Constraint(expr=   600*m.b7 + 600*m.b8 + 600*m.b9 + 600*m.b10 + 600*m.b11 + 600*m.b12 - m.x148 + m.x169 <= 600)

m.c165 = Constraint(expr=   600*m.b25 + 600*m.b28 - m.x143 + m.x170 <= 600)

m.c166 = Constraint(expr=   600*m.b25 + 600*m.b26 + 600*m.b28 + 600*m.b29 - m.x146 + m.x170 <= 600)

m.c167 = Constraint(expr=   600*m.b25 + 600*m.b26 + 600*m.b27 + 600*m.b28 + 600*m.b29 + 600*m.b30 - m.x149 + m.x170
                          <= 600)

m.c168 = Constraint(expr=   600*m.b43 + 600*m.b46 - m.x144 + m.x171 <= 600)

m.c169 = Constraint(expr=   600*m.b43 + 600*m.b44 + 600*m.b46 + 600*m.b47 - m.x147 + m.x171 <= 600)

m.c170 = Constraint(expr=   600*m.b43 + 600*m.b44 + 600*m.b45 + 600*m.b46 + 600*m.b47 + 600*m.b48 - m.x150 + m.x171
                          <= 600)

m.c171 = Constraint(expr=   600*m.b13 + 600*m.b16 - m.x142 + m.x172 <= 600)

m.c172 = Constraint(expr=   600*m.b13 + 600*m.b14 + 600*m.b16 + 600*m.b17 - m.x145 + m.x172 <= 600)

m.c173 = Constraint(expr=   600*m.b13 + 600*m.b14 + 600*m.b15 + 600*m.b16 + 600*m.b17 + 600*m.b18 - m.x148 + m.x172
                          <= 600)

m.c174 = Constraint(expr=   600*m.b31 + 600*m.b34 - m.x143 + m.x173 <= 600)

m.c175 = Constraint(expr=   600*m.b31 + 600*m.b32 + 600*m.b34 + 600*m.b35 - m.x146 + m.x173 <= 600)

m.c176 = Constraint(expr=   600*m.b31 + 600*m.b32 + 600*m.b33 + 600*m.b34 + 600*m.b35 + 600*m.b36 - m.x149 + m.x173
                          <= 600)

m.c177 = Constraint(expr=   600*m.b49 + 600*m.b52 - m.x144 + m.x174 <= 600)

m.c178 = Constraint(expr=   600*m.b49 + 600*m.b50 + 600*m.b52 + 600*m.b53 - m.x147 + m.x174 <= 600)

m.c179 = Constraint(expr=   600*m.b49 + 600*m.b50 + 600*m.b51 + 600*m.b52 + 600*m.b53 + 600*m.b54 - m.x150 + m.x174
                          <= 600)

m.c180 = Constraint(expr= - 600*m.b1 - 600*m.b2 - 600*m.b3 - 600*m.b4 - 600*m.b5 - 600*m.b6 - m.x142 + m.x166 >= -600)

m.c181 = Constraint(expr= - 600*m.b2 - 600*m.b3 - 600*m.b5 - 600*m.b6 - m.x145 + m.x166 >= -600)

m.c182 = Constraint(expr= - 600*m.b3 - 600*m.b6 - m.x148 + m.x166 >= -600)

m.c183 = Constraint(expr= - 600*m.b19 - 600*m.b20 - 600*m.b21 - 600*m.b22 - 600*m.b23 - 600*m.b24 - m.x143 + m.x167
                          >= -600)

m.c184 = Constraint(expr= - 600*m.b20 - 600*m.b21 - 600*m.b23 - 600*m.b24 - m.x146 + m.x167 >= -600)

m.c185 = Constraint(expr= - 600*m.b21 - 600*m.b24 - m.x149 + m.x167 >= -600)

m.c186 = Constraint(expr= - 600*m.b37 - 600*m.b38 - 600*m.b39 - 600*m.b40 - 600*m.b41 - 600*m.b42 - m.x144 + m.x168
                          >= -600)

m.c187 = Constraint(expr= - 600*m.b38 - 600*m.b39 - 600*m.b41 - 600*m.b42 - m.x147 + m.x168 >= -600)

m.c188 = Constraint(expr= - 600*m.b39 - 600*m.b42 - m.x150 + m.x168 >= -600)

m.c189 = Constraint(expr= - 600*m.b7 - 600*m.b8 - 600*m.b9 - 600*m.b10 - 600*m.b11 - 600*m.b12 - m.x142 + m.x169
                          >= -600)

m.c190 = Constraint(expr= - 600*m.b8 - 600*m.b9 - 600*m.b11 - 600*m.b12 - m.x145 + m.x169 >= -600)

m.c191 = Constraint(expr= - 600*m.b9 - 600*m.b12 - m.x148 + m.x169 >= -600)

m.c192 = Constraint(expr= - 600*m.b25 - 600*m.b26 - 600*m.b27 - 600*m.b28 - 600*m.b29 - 600*m.b30 - m.x143 + m.x170
                          >= -600)

m.c193 = Constraint(expr= - 600*m.b26 - 600*m.b27 - 600*m.b29 - 600*m.b30 - m.x146 + m.x170 >= -600)

m.c194 = Constraint(expr= - 600*m.b27 - 600*m.b30 - m.x149 + m.x170 >= -600)

m.c195 = Constraint(expr= - 600*m.b43 - 600*m.b44 - 600*m.b45 - 600*m.b46 - 600*m.b47 - 600*m.b48 - m.x144 + m.x171
                          >= -600)

m.c196 = Constraint(expr= - 600*m.b44 - 600*m.b45 - 600*m.b47 - 600*m.b48 - m.x147 + m.x171 >= -600)

m.c197 = Constraint(expr= - 600*m.b45 - 600*m.b48 - m.x150 + m.x171 >= -600)

m.c198 = Constraint(expr= - 600*m.b13 - 600*m.b14 - 600*m.b15 - 600*m.b16 - 600*m.b17 - 600*m.b18 - m.x142 + m.x172
                          >= -600)

m.c199 = Constraint(expr= - 600*m.b14 - 600*m.b15 - 600*m.b17 - 600*m.b18 - m.x145 + m.x172 >= -600)

m.c200 = Constraint(expr= - 600*m.b15 - 600*m.b18 - m.x148 + m.x172 >= -600)

m.c201 = Constraint(expr= - 600*m.b31 - 600*m.b32 - 600*m.b33 - 600*m.b34 - 600*m.b35 - 600*m.b36 - m.x143 + m.x173
                          >= -600)

m.c202 = Constraint(expr= - 600*m.b32 - 600*m.b33 - 600*m.b35 - 600*m.b36 - m.x146 + m.x173 >= -600)

m.c203 = Constraint(expr= - 600*m.b33 - 600*m.b36 - m.x149 + m.x173 >= -600)

m.c204 = Constraint(expr= - 600*m.b49 - 600*m.b50 - 600*m.b51 - 600*m.b52 - 600*m.b53 - 600*m.b54 - m.x144 + m.x174
                          >= -600)

m.c205 = Constraint(expr= - 600*m.b50 - 600*m.b51 - 600*m.b53 - 600*m.b54 - m.x147 + m.x174 >= -600)

m.c206 = Constraint(expr= - 600*m.b51 - 600*m.b54 - m.x150 + m.x174 >= -600)

m.c207 = Constraint(expr=-m.x178*(m.x166 - m.x157) + m.x79 + m.x80 + m.x81 == 0)

m.c208 = Constraint(expr=-m.x179*(m.x167 - m.x158) + m.x82 + m.x83 + m.x84 == 0)

m.c209 = Constraint(expr=-m.x180*(m.x168 - m.x159) + m.x85 + m.x86 + m.x87 == 0)

m.c210 = Constraint(expr=-m.x181*(m.x169 - m.x160) + m.x88 + m.x89 + m.x90 == 0)

m.c211 = Constraint(expr=-m.x182*(m.x170 - m.x161) + m.x91 + m.x92 + m.x93 == 0)

m.c212 = Constraint(expr=-m.x183*(m.x171 - m.x162) + m.x94 + m.x95 + m.x96 == 0)

m.c213 = Constraint(expr=-m.x184*(m.x172 - m.x163) + m.x97 + m.x98 + m.x99 == 0)

m.c214 = Constraint(expr=-m.x185*(m.x173 - m.x164) + m.x100 + m.x101 + m.x102 == 0)

m.c215 = Constraint(expr=-m.x186*(m.x174 - m.x165) + m.x103 + m.x104 + m.x105 == 0)

m.c216 = Constraint(expr= - 1170*m.b1 - 1170*m.b2 - 1170*m.b3 - 1170*m.b4 - 1170*m.b5 - 1170*m.b6 + m.x178 <= 0)

m.c217 = Constraint(expr= - 1120*m.b19 - 1120*m.b20 - 1120*m.b21 - 1120*m.b22 - 1120*m.b23 - 1120*m.b24 + m.x179 <= 0)

m.c218 = Constraint(expr= - 1120*m.b37 - 1120*m.b38 - 1120*m.b39 - 1120*m.b40 - 1120*m.b41 - 1120*m.b42 + m.x180 <= 0)

m.c219 = Constraint(expr= - 1340*m.b7 - 1340*m.b8 - 1340*m.b9 - 1340*m.b10 - 1340*m.b11 - 1340*m.b12 + m.x181 <= 0)

m.c220 = Constraint(expr= - 1290*m.b25 - 1290*m.b26 - 1290*m.b27 - 1290*m.b28 - 1290*m.b29 - 1290*m.b30 + m.x182 <= 0)

m.c221 = Constraint(expr= - 1860*m.b43 - 1860*m.b44 - 1860*m.b45 - 1860*m.b46 - 1860*m.b47 - 1860*m.b48 + m.x183 <= 0)

m.c222 = Constraint(expr= - 1340*m.b13 - 1340*m.b14 - 1340*m.b15 - 1340*m.b16 - 1340*m.b17 - 1340*m.b18 + m.x184 <= 0)

m.c223 = Constraint(expr= - 1340*m.b31 - 1340*m.b32 - 1340*m.b33 - 1340*m.b34 - 1340*m.b35 - 1340*m.b36 + m.x185 <= 0)

m.c224 = Constraint(expr= - 1340*m.b49 - 1340*m.b50 - 1340*m.b51 - 1340*m.b52 - 1340*m.b53 - 1340*m.b54 + m.x186 <= 0)

m.c225 = Constraint(expr=   m.x159 - m.x168 + m.x187 == 0)

m.c226 = Constraint(expr=   m.x162 - m.x171 + m.x188 == 0)

m.c227 = Constraint(expr=   m.x165 - m.x174 + m.x189 == 0)

m.c228 = Constraint(expr=   m.x187 - m.x190 <= 0)

m.c229 = Constraint(expr=   m.x188 - m.x190 <= 0)

m.c230 = Constraint(expr=   m.x189 - m.x190 <= 0)

m.c231 = Constraint(expr=   600*m.b55 + 600*m.b67 + m.x157 - m.x158 <= 600)

m.c232 = Constraint(expr=   600*m.b56 + 600*m.b68 + m.x158 - m.x159 <= 600)

m.c233 = Constraint(expr=   600*m.b57 + 600*m.b69 + m.x160 - m.x161 <= 600)

m.c234 = Constraint(expr=   600*m.b58 + 600*m.b70 + m.x161 - m.x162 <= 600)

m.c235 = Constraint(expr=   600*m.b59 + 600*m.b71 + m.x163 - m.x164 <= 600)

m.c236 = Constraint(expr=   600*m.b60 + 600*m.b72 + m.x164 - m.x165 <= 600)

m.c237 = Constraint(expr= - 600*m.b61 - 600*m.b73 + m.x157 - m.x158 >= -600)

m.c238 = Constraint(expr= - 600*m.b62 - 600*m.b74 + m.x158 - m.x159 >= -600)

m.c239 = Constraint(expr= - 600*m.b63 - 600*m.b75 + m.x160 - m.x161 >= -600)

m.c240 = Constraint(expr= - 600*m.b64 - 600*m.b76 + m.x161 - m.x162 >= -600)

m.c241 = Constraint(expr= - 600*m.b65 - 600*m.b77 + m.x163 - m.x164 >= -600)

m.c242 = Constraint(expr= - 600*m.b66 - 600*m.b78 + m.x164 - m.x165 >= -600)

m.c243 = Constraint(expr=   1200*m.b55 + 1200*m.b73 + m.x166 - m.x167 <= 1200)

m.c244 = Constraint(expr=   1200*m.b56 + 1200*m.b74 + m.x167 - m.x168 <= 1200)

m.c245 = Constraint(expr=   1200*m.b57 + 1200*m.b75 + m.x169 - m.x170 <= 1200)

m.c246 = Constraint(expr=   1200*m.b58 + 1200*m.b76 + m.x170 - m.x171 <= 1200)

m.c247 = Constraint(expr=   1200*m.b59 + 1200*m.b77 + m.x172 - m.x173 <= 1200)

m.c248 = Constraint(expr=   1200*m.b60 + 1200*m.b78 + m.x173 - m.x174 <= 1200)

m.c249 = Constraint(expr= - 1200*m.b61 - 1200*m.b67 + m.x166 - m.x167 >= -1200)

m.c250 = Constraint(expr= - 1200*m.b62 - 1200*m.b68 + m.x167 - m.x168 >= -1200)

m.c251 = Constraint(expr= - 1200*m.b63 - 1200*m.b69 + m.x169 - m.x170 >= -1200)

m.c252 = Constraint(expr= - 1200*m.b64 - 1200*m.b70 + m.x170 - m.x171 >= -1200)

m.c253 = Constraint(expr= - 1200*m.b65 - 1200*m.b71 + m.x172 - m.x173 >= -1200)

m.c254 = Constraint(expr= - 1200*m.b66 - 1200*m.b72 + m.x173 - m.x174 >= -1200)

m.c255 = Constraint(expr= - 600*m.b55 - 600*m.b61 - 600*m.b67 - 600*m.b73 - m.x158 + m.x166 >= -600)

m.c256 = Constraint(expr= - 600*m.b56 - 600*m.b62 - 600*m.b68 - 600*m.b74 - m.x159 + m.x167 >= -600)

m.c257 = Constraint(expr= - 600*m.b57 - 600*m.b63 - 600*m.b69 - 600*m.b75 - m.x161 + m.x169 >= -600)

m.c258 = Constraint(expr= - 600*m.b58 - 600*m.b64 - 600*m.b70 - 600*m.b76 - m.x162 + m.x170 >= -600)

m.c259 = Constraint(expr= - 600*m.b59 - 600*m.b65 - 600*m.b71 - 600*m.b77 - m.x164 + m.x172 >= -600)

m.c260 = Constraint(expr= - 600*m.b60 - 600*m.b66 - 600*m.b72 - 600*m.b78 - m.x165 + m.x173 >= -600)

m.c261 = Constraint(expr= - 600*m.b55 - 600*m.b61 - 600*m.b67 - 600*m.b73 - m.x157 + m.x167 >= -600)

m.c262 = Constraint(expr= - 600*m.b56 - 600*m.b62 - 600*m.b68 - 600*m.b74 - m.x158 + m.x168 >= -600)

m.c263 = Constraint(expr= - 600*m.b57 - 600*m.b63 - 600*m.b69 - 600*m.b75 - m.x160 + m.x170 >= -600)

m.c264 = Constraint(expr= - 600*m.b58 - 600*m.b64 - 600*m.b70 - 600*m.b76 - m.x161 + m.x171 >= -600)

m.c265 = Constraint(expr= - 600*m.b59 - 600*m.b65 - 600*m.b71 - 600*m.b77 - m.x163 + m.x173 >= -600)

m.c266 = Constraint(expr= - 600*m.b60 - 600*m.b66 - 600*m.b72 - 600*m.b78 - m.x164 + m.x174 >= -600)

m.c267 = Constraint(expr=-(m.x158 - m.x157)*m.x178 - 672000*m.b55 + m.x151 >= -672000)

m.c268 = Constraint(expr=-(m.x159 - m.x158)*m.x179 - 672000*m.b56 + m.x152 >= -672000)

m.c269 = Constraint(expr=-(m.x161 - m.x160)*m.x181 - 774000*m.b57 + m.x153 >= -774000)

m.c270 = Constraint(expr=-(m.x162 - m.x161)*m.x182 - 774000*m.b58 + m.x154 >= -774000)

m.c271 = Constraint(expr=-(m.x164 - m.x163)*m.x184 - 804000*m.b59 + m.x155 >= -804000)

m.c272 = Constraint(expr=-(m.x165 - m.x164)*m.x185 - 804000*m.b60 + m.x156 >= -804000)

m.c273 = Constraint(expr=-(m.x167 - m.x166)*m.x179 - 672000*m.b55 + m.x151 >= -672000)

m.c274 = Constraint(expr=-(m.x168 - m.x167)*m.x180 - 672000*m.b56 + m.x152 >= -672000)

m.c275 = Constraint(expr=-(m.x170 - m.x169)*m.x182 - 774000*m.b57 + m.x153 >= -774000)

m.c276 = Constraint(expr=-(m.x171 - m.x170)*m.x183 - 774000*m.b58 + m.x154 >= -774000)

m.c277 = Constraint(expr=-(m.x173 - m.x172)*m.x185 - 804000*m.b59 + m.x155 >= -804000)

m.c278 = Constraint(expr=-(m.x174 - m.x173)*m.x186 - 804000*m.b60 + m.x156 >= -804000)

m.c279 = Constraint(expr=-(m.x157 - m.x158)*m.x179 - 672000*m.b61 + m.x151 >= -672000)

m.c280 = Constraint(expr=-(m.x158 - m.x159)*m.x180 - 672000*m.b62 + m.x152 >= -672000)

m.c281 = Constraint(expr=-(m.x160 - m.x161)*m.x182 - 774000*m.b63 + m.x153 >= -774000)

m.c282 = Constraint(expr=-(m.x161 - m.x162)*m.x183 - 774000*m.b64 + m.x154 >= -774000)

m.c283 = Constraint(expr=-(m.x163 - m.x164)*m.x185 - 804000*m.b65 + m.x155 >= -804000)

m.c284 = Constraint(expr=-(m.x164 - m.x165)*m.x186 - 804000*m.b66 + m.x156 >= -804000)

m.c285 = Constraint(expr=-(m.x166 - m.x167)*m.x178 - 672000*m.b61 + m.x151 >= -672000)

m.c286 = Constraint(expr=-(m.x167 - m.x168)*m.x179 - 672000*m.b62 + m.x152 >= -672000)

m.c287 = Constraint(expr=-(m.x169 - m.x170)*m.x181 - 774000*m.b63 + m.x153 >= -774000)

m.c288 = Constraint(expr=-(m.x170 - m.x171)*m.x182 - 774000*m.b64 + m.x154 >= -774000)

m.c289 = Constraint(expr=-(m.x172 - m.x173)*m.x184 - 804000*m.b65 + m.x155 >= -804000)

m.c290 = Constraint(expr=-(m.x173 - m.x174)*m.x185 - 804000*m.b66 + m.x156 >= -804000)

m.c291 = Constraint(expr=-(m.x179 - m.x178)*(m.x167 - m.x158) - 672000*m.b67 + m.x151 >= -672000)

m.c292 = Constraint(expr=-(m.x180 - m.x179)*(m.x168 - m.x159) - 672000*m.b68 + m.x152 >= -672000)

m.c293 = Constraint(expr=-(m.x182 - m.x181)*(m.x170 - m.x161) - 774000*m.b69 + m.x153 >= -774000)

m.c294 = Constraint(expr=-(m.x183 - m.x182)*(m.x171 - m.x162) - 774000*m.b70 + m.x154 >= -774000)

m.c295 = Constraint(expr=-(m.x185 - m.x184)*(m.x173 - m.x164) - 804000*m.b71 + m.x155 >= -804000)

m.c296 = Constraint(expr=-(m.x186 - m.x185)*(m.x174 - m.x165) - 804000*m.b72 + m.x156 >= -804000)

m.c297 = Constraint(expr=-(m.x178 - m.x179)*(m.x166 - m.x157) - 672000*m.b73 + m.x151 >= -672000)

m.c298 = Constraint(expr=-(m.x179 - m.x180)*(m.x167 - m.x158) - 672000*m.b74 + m.x152 >= -672000)

m.c299 = Constraint(expr=-(m.x181 - m.x182)*(m.x169 - m.x160) - 774000*m.b75 + m.x153 >= -774000)

m.c300 = Constraint(expr=-(m.x182 - m.x183)*(m.x170 - m.x161) - 774000*m.b76 + m.x154 >= -774000)

m.c301 = Constraint(expr=-(m.x184 - m.x185)*(m.x172 - m.x163) - 804000*m.b77 + m.x155 >= -804000)

m.c302 = Constraint(expr=-(m.x185 - m.x186)*(m.x173 - m.x164) - 804000*m.b78 + m.x156 >= -804000)

m.c303 = Constraint(expr=   672000*m.b55 + 672000*m.b61 + 672000*m.b67 + 672000*m.b73 - m.x79 - m.x80 - m.x81 + m.x151
                          >= 0)

m.c304 = Constraint(expr=   672000*m.b56 + 672000*m.b62 + 672000*m.b68 + 672000*m.b74 - m.x82 - m.x83 - m.x84 + m.x152
                          >= 0)

m.c305 = Constraint(expr=   774000*m.b57 + 774000*m.b63 + 774000*m.b69 + 774000*m.b75 - m.x88 - m.x89 - m.x90 + m.x153
                          >= 0)

m.c306 = Constraint(expr=   774000*m.b58 + 774000*m.b64 + 774000*m.b70 + 774000*m.b76 - m.x91 - m.x92 - m.x93 + m.x154
                          >= 0)

m.c307 = Constraint(expr=   804000*m.b59 + 804000*m.b65 + 804000*m.b71 + 804000*m.b77 - m.x97 - m.x98 - m.x99 + m.x155
                          >= 0)

m.c308 = Constraint(expr=   804000*m.b60 + 804000*m.b66 + 804000*m.b72 + 804000*m.b78 - m.x100 - m.x101 - m.x102
                          + m.x156 >= 0)

m.c309 = Constraint(expr=   2*m.b37 + 2*m.b38 + 2*m.b39 + 2*m.b40 + 2*m.b41 + 2*m.b42 + 2*m.b43 + 2*m.b44 + 2*m.b45
                          + m.b46 + m.b47 + m.b48 + 2*m.b49 + 2*m.b50 + 2*m.b51 + m.b52 + m.b53 + m.b54 + m.x187
                          + m.x188 + m.x189 - m.x190 == 0)
