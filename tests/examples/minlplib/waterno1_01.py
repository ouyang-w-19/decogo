#  MINLP written by GAMS Convert at 04/21/18 13:55:15
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        183      102       39       42        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        158      143       15        0        0        0        0        0
#  FX      5        5        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        484      426       58        0
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
m.x17 = Var(within=Reals,bounds=(148.299332771269,638.10455381568),initialize=148.299332771269)
m.x18 = Var(within=Reals,bounds=(0,135.302691146811),initialize=0)
m.x19 = Var(within=Reals,bounds=(0.8,1.2),initialize=0.8)
m.x20 = Var(within=Reals,bounds=(148.299332771269,638.10455381568),initialize=148.299332771269)
m.x21 = Var(within=Reals,bounds=(0,135.302691146811),initialize=0)
m.x22 = Var(within=Reals,bounds=(287.427397827187,413.764247971),initialize=287.427397827187)
m.x23 = Var(within=Reals,bounds=(0,126.336850143813),initialize=0)
m.x24 = Var(within=Reals,bounds=(74.1748123438468,106.777870451),initialize=74.1748123438468)
m.x25 = Var(within=Reals,bounds=(0,32.6030581071532),initialize=0)
m.x26 = Var(within=Reals,bounds=(74.1748123438468,106.777870451),initialize=74.1748123438468)
m.x27 = Var(within=Reals,bounds=(0,32.6030581071532),initialize=0)
m.x28 = Var(within=Reals,bounds=(74.1748123438468,106.777870451),initialize=74.1748123438468)
m.x29 = Var(within=Reals,bounds=(0,32.6030581071532),initialize=0)
m.x30 = Var(within=Reals,bounds=(74.1748123434975,106.777870452),initialize=74.1748123434975)
m.x31 = Var(within=Reals,bounds=(0,32.6030581085025),initialize=0)
m.x32 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,0.64163),initialize=0)
m.x34 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x35 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x36 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x37 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x38 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x39 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x40 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x41 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x42 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x43 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x44 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x45 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x46 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x47 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x48 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x49 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x50 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x51 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x52 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x53 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x54 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x55 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x56 = Var(within=Reals,bounds=(0,0.429286),initialize=0)
m.x57 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x58 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x59 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x60 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x61 = Var(within=Reals,bounds=(-5,5),initialize=0)
m.x62 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x63 = Var(within=Reals,bounds=(6.3,6.3),initialize=6.3)
m.x64 = Var(within=Reals,bounds=(5,10),initialize=5)
m.x65 = Var(within=Reals,bounds=(4.6,4.6),initialize=4.6)
m.x66 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x67 = Var(within=Reals,bounds=(4.6,4.6),initialize=4.6)
m.x68 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x69 = Var(within=Reals,bounds=(10,10),initialize=10)
m.x70 = Var(within=Reals,bounds=(0,16.5),initialize=0)
m.x71 = Var(within=Reals,bounds=(0,0.045826),initialize=0)
m.x72 = Var(within=Reals,bounds=(287.427397827187,413.764247971),initialize=287.427397827187)
m.x73 = Var(within=Reals,bounds=(0,0.091663),initialize=0)
m.x74 = Var(within=Reals,bounds=(0,126.336850143813),initialize=0)
m.x75 = Var(within=Reals,bounds=(0,0.091663),initialize=0)
m.x76 = Var(within=Reals,bounds=(0.8,1.2),initialize=0.8)
m.x77 = Var(within=Reals,bounds=(0,0.091663),initialize=0)
m.x78 = Var(within=Reals,bounds=(148.299332771269,638.10455381568),initialize=148.299332771269)
m.x79 = Var(within=Reals,bounds=(0,0.091663),initialize=0)
m.x80 = Var(within=Reals,bounds=(0,135.302691146811),initialize=0)
m.x81 = Var(within=Reals,bounds=(0,0.091663),initialize=0)
m.x82 = Var(within=Reals,bounds=(0.8,1.2),initialize=0.8)
m.x83 = Var(within=Reals,bounds=(0,0.091663),initialize=0)
m.x84 = Var(within=Reals,bounds=(148.299332771269,638.10455381568),initialize=148.299332771269)
m.x85 = Var(within=Reals,bounds=(0,0.045826),initialize=0)
m.x86 = Var(within=Reals,bounds=(0,135.302691146811),initialize=0)
m.x87 = Var(within=Reals,bounds=(0,0.119163),initialize=0)
m.x88 = Var(within=Reals,bounds=(0.8,1.2),initialize=0.8)
m.x89 = Var(within=Reals,bounds=(0,0.119163),initialize=0)
m.x90 = Var(within=Reals,bounds=(148.299332771269,638.10455381568),initialize=148.299332771269)
m.x91 = Var(within=Reals,bounds=(0,0.119163),initialize=0)
m.x92 = Var(within=Reals,bounds=(0,135.302691146811),initialize=0)
m.x93 = Var(within=Reals,bounds=(0,0.071797),initialize=0)
m.x94 = Var(within=Reals,bounds=(0.8,1.2),initialize=0.8)
m.x95 = Var(within=Reals,bounds=(305,310),initialize=305)
m.x96 = Var(within=Reals,bounds=(240,246),initialize=240)
m.x97 = Var(within=Reals,bounds=(240,246),initialize=240)
m.x98 = Var(within=Reals,bounds=(243,259.5),initialize=243)
m.x99 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x100 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x101 = Var(within=Reals,bounds=(-232.35111544525,232.35111544525),initialize=0)
m.x102 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x103 = Var(within=Reals,bounds=(-103800.7251715,103800.7251715),initialize=0)
m.x104 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x105 = Var(within=Reals,bounds=(-22646.161845275,22646.161845275),initialize=0)
m.x106 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x107 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x108 = Var(within=Reals,bounds=(-1693.1005454625,1693.1005454625),initialize=0)
m.x109 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x110 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x111 = Var(within=Reals,bounds=(-1975.896081255,1975.896081255),initialize=0)
m.x112 = Var(within=Reals,bounds=(-35055.017651,35055.017651),initialize=0)
m.x113 = Var(within=Reals,bounds=(-987.9480406275,987.9480406275),initialize=0)
m.x114 = Var(within=Reals,bounds=(-1270.74357642,1270.74357642),initialize=0)
m.x115 = Var(within=Reals,bounds=(-186.06385100525,186.06385100525),initialize=0)
m.x116 = Var(within=Reals,bounds=(-186.06385100525,186.06385100525),initialize=0)
m.x117 = Var(within=Reals,bounds=(214.9,1000),initialize=214.9)
m.x118 = Var(within=Reals,bounds=(-9303.19255025,9303.19255025),initialize=0)
m.x119 = Var(within=Reals,bounds=(231.04,1000),initialize=231.04)
m.x120 = Var(within=Reals,bounds=(-14219.27742075,14219.27742075),initialize=0)
m.x121 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x122 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x123 = Var(within=Reals,bounds=(-1596.630932455,1596.630932455),initialize=0)
m.x124 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x125 = Var(within=Reals,bounds=(300,1000),initialize=300)
m.x126 = Var(within=Reals,bounds=(-62.00958485375,62.00958485375),initialize=0)
m.x127 = Var(within=Reals,bounds=(-62.00958485375,62.00958485375),initialize=0)
m.x128 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x129 = Var(within=Reals,bounds=(-3.100479242675,3.100479242675),initialize=0)
m.x130 = Var(within=Reals,bounds=(-3.100479242675,3.100479242675),initialize=0)
m.x131 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x132 = Var(within=Reals,bounds=(243,1000),initialize=243)
m.x133 = Var(within=Reals,bounds=(-138489.1922805,138489.1922805),initialize=0)
m.x134 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x135 = Var(within=Reals,bounds=(-138489.1922805,138489.1922805),initialize=0)
m.x136 = Var(within=Reals,bounds=(-1846.52256374,1846.52256374),initialize=0)
m.x137 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x138 = Var(within=Reals,bounds=(-538.866468715,538.866468715),initialize=0)
m.x139 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x140 = Var(within=Reals,bounds=(-259.21503776,259.21503776),initialize=0)
m.x141 = Var(within=Reals,bounds=(34.1,34.1),initialize=34.1)
m.x142 = Var(within=Reals,bounds=(-34.1,1000),initialize=0)
m.x143 = Var(within=Reals,bounds=(-1000,1000),initialize=0)
m.x144 = Var(within=Reals,bounds=(148.299332771269,638.10455381568),initialize=148.299332771269)
m.x145 = Var(within=Reals,bounds=(0,135.302691146811),initialize=0)
m.x146 = Var(within=Reals,bounds=(0.8,1.2),initialize=0.8)
m.x147 = Var(within=Reals,bounds=(0,46.5022459484905),initialize=0)
m.x148 = Var(within=Reals,bounds=(0,143.448141849487),initialize=0)
m.x149 = Var(within=Reals,bounds=(0,143.448141849487),initialize=0)
m.x150 = Var(within=Reals,bounds=(0,143.448141849487),initialize=0)
m.x151 = Var(within=Reals,bounds=(0,143.448141849487),initialize=0)
m.x152 = Var(within=Reals,bounds=(0,143.448141849487),initialize=0)
m.x153 = Var(within=Reals,bounds=(0,143.448141849487),initialize=0)
m.x154 = Var(within=Reals,bounds=(0,46.5022459484905),initialize=0)
m.x155 = Var(within=Reals,bounds=(0,31.205539800995),initialize=0)
m.x156 = Var(within=Reals,bounds=(0,31.205539800995),initialize=0)
m.x157 = Var(within=Reals,bounds=(0,31.205539800995),initialize=0)
m.x158 = Var(within=Reals,bounds=(0,18.8016762007756),initialize=0)

m.obj = Objective(expr=   m.x147 + m.x148 + m.x149 + m.x150 + m.x151 + m.x152 + m.x153 + m.x154 + m.x155 + m.x156
                        + m.x157 + m.x158, sense=minimize)

m.c2 = Constraint(expr=   m.x72 + m.x74 == 413.764247971)

m.c3 = Constraint(expr= - 443.128162372*m.x76 + m.x78 + m.x80 == 0)

m.c4 = Constraint(expr= - 443.128162372*m.x82 + m.x84 + m.x86 == 0)

m.c5 = Constraint(expr= - 443.128162372*m.x88 + m.x90 + m.x92 == 0)

m.c6 = Constraint(expr= - 443.128162372*m.x94 + m.x144 + m.x145 == 0)

m.c7 = Constraint(expr=   m.x17 + m.x18 - 443.128162372*m.x146 == 0)

m.c8 = Constraint(expr= - 443.128162372*m.x19 + m.x20 + m.x21 == 0)

m.c9 = Constraint(expr=   m.x22 + m.x23 == 413.764247971)

m.c10 = Constraint(expr=   m.x24 + m.x25 == 106.777870451)

m.c11 = Constraint(expr=   m.x26 + m.x27 == 106.777870451)

m.c12 = Constraint(expr=   m.x28 + m.x29 == 106.777870451)

m.c13 = Constraint(expr=   m.x30 + m.x31 == 106.777870452)

m.c14 = Constraint(expr= - m.x32 + m.x33 == 0)

m.c15 = Constraint(expr=   m.x32 - m.x34 - m.x35 - m.x36 == 0)

m.c16 = Constraint(expr=   m.x37 == 0.025)

m.c17 = Constraint(expr=   m.x38 == 0.013)

m.c18 = Constraint(expr=   m.x39 + m.x40 - m.x41 == 0)

m.c19 = Constraint(expr=   m.x36 - m.x39 + m.x42 - m.x43 == 0)

m.c20 = Constraint(expr=   m.x35 - m.x44 == 0)

m.c21 = Constraint(expr=   m.x41 + m.x45 + m.x46 + m.x47 - m.x48 - m.x49 == 0)

m.c22 = Constraint(expr= - m.x37 + m.x43 + m.x44 - m.x50 == 0)

m.c23 = Constraint(expr= - m.x38 - m.x40 + m.x50 == 0)

m.c24 = Constraint(expr=   m.x34 - m.x42 == 0)

m.c25 = Constraint(expr= - m.x51 == 0.1624)

m.c26 = Constraint(expr=   m.x51 - m.x52 + m.x53 == 0)

m.c27 = Constraint(expr=   m.x54 + m.x55 - m.x56 == 0)

m.c28 = Constraint(expr=   m.x56 + m.x57 - m.x58 == 0)

m.c29 = Constraint(expr= - m.x57 - m.x59 == 0.0138888888888889)

m.c30 = Constraint(expr= - m.x46 + m.x59 - m.x60 == 0)

m.c31 = Constraint(expr=   m.x61 == 0)

m.c32 = Constraint(expr= - m.x47 + m.x58 == 0)

m.c33 = Constraint(expr= - m.x45 - m.x53 == 0)

m.c34 = Constraint(expr= - m.x33 + m.x62 == 0)

m.c35 = Constraint(expr=   3600*m.x52 + 239.978718892*m.x63 - 239.978718892*m.x64 == 0)

m.c36 = Constraint(expr=   3600*m.x48 - 3600*m.x54 + 416.560177655*m.x65 - 416.560177655*m.x66 == 0)

m.c37 = Constraint(expr=   3600*m.x49 - 3600*m.x55 + 416.560177655*m.x67 - 416.560177655*m.x68 == 0)

m.c38 = Constraint(expr=   3600*m.x60 - 3600*m.x61 + 165.129961038*m.x69 - 165.129961038*m.x70 == 0)

m.c39 = Constraint(expr= - 0.037494*m.b2 + m.x71 >= 0)

m.c40 = Constraint(expr= - 0.074997*m.b3 + m.x73 >= 0)

m.c41 = Constraint(expr= - 0.074997*m.b4 + m.x75 >= 0)

m.c42 = Constraint(expr= - 0.074997*m.b5 + m.x77 >= 0)

m.c43 = Constraint(expr= - 0.074997*m.b6 + m.x79 >= 0)

m.c44 = Constraint(expr= - 0.074997*m.b7 + m.x81 >= 0)

m.c45 = Constraint(expr= - 0.074997*m.b8 + m.x83 >= 0)

m.c46 = Constraint(expr= - 0.037494*m.b9 + m.x85 >= 0)

m.c47 = Constraint(expr= - 0.097497*m.b10 + m.x87 >= 0)

m.c48 = Constraint(expr= - 0.097497*m.b11 + m.x89 >= 0)

m.c49 = Constraint(expr= - 0.097497*m.b12 + m.x91 >= 0)

m.c50 = Constraint(expr= - 0.058743*m.b13 + m.x93 >= 0)

m.c51 = Constraint(expr= - 0.045826*m.b2 + m.x71 <= 0)

m.c52 = Constraint(expr= - 0.091663*m.b3 + m.x73 <= 0)

m.c53 = Constraint(expr= - 0.091663*m.b4 + m.x75 <= 0)

m.c54 = Constraint(expr= - 0.091663*m.b5 + m.x77 <= 0)

m.c55 = Constraint(expr= - 0.091663*m.b6 + m.x79 <= 0)

m.c56 = Constraint(expr= - 0.091663*m.b7 + m.x81 <= 0)

m.c57 = Constraint(expr= - 0.091663*m.b8 + m.x83 <= 0)

m.c58 = Constraint(expr= - 0.045826*m.b9 + m.x85 <= 0)

m.c59 = Constraint(expr= - 0.119163*m.b10 + m.x87 <= 0)

m.c60 = Constraint(expr= - 0.119163*m.b11 + m.x89 <= 0)

m.c61 = Constraint(expr= - 0.119163*m.b12 + m.x91 <= 0)

m.c62 = Constraint(expr= - 0.071797*m.b13 + m.x93 <= 0)

m.c63 = Constraint(expr= - m.x63 + m.x95 == 300)

m.c64 = Constraint(expr= - m.x65 + m.x96 == 240)

m.c65 = Constraint(expr= - m.x67 + m.x97 == 240)

m.c66 = Constraint(expr= - m.x69 + m.x98 == 243)

m.c67 = Constraint(expr=   m.x99 - m.x100 - m.x101 == 0)

m.c68 = Constraint(expr=   m.x100 - m.x102 - m.x103 == 0)

m.c69 = Constraint(expr=   m.x100 - m.x104 - m.x105 == 0)

m.c70 = Constraint(expr=   m.x106 - m.x107 - m.x108 == 0)

m.c71 = Constraint(expr= - m.x109 + m.x110 - m.x111 == 0)

m.c72 = Constraint(expr=   m.x104 - m.x109 - m.x112 == 0)

m.c73 = Constraint(expr=   m.x100 - m.x106 - m.x113 == 0)

m.c74 = Constraint(expr=   m.x107 - m.x110 - m.x114 == 0)

m.c75 = Constraint(expr=   m.x102 - m.x104 - m.x115 == 0)

m.c76 = Constraint(expr=   m.x104 - m.x107 - m.x116 == 0)

m.c77 = Constraint(expr=   m.x107 - m.x117 - m.x118 == 0)

m.c78 = Constraint(expr=   m.x110 - m.x119 - m.x120 == 0)

m.c79 = Constraint(expr= - m.x121 + m.x122 - m.x123 == 0)

m.c80 = Constraint(expr= - m.x124 + m.x125 - m.x126 == 0)

m.c81 = Constraint(expr= - m.x95 + m.x124 - m.x127 == 0)

m.c82 = Constraint(expr=   m.x96 - m.x128 - m.x129 == 0)

m.c83 = Constraint(expr=   m.x97 - m.x128 - m.x130 == 0)

m.c84 = Constraint(expr= - m.x131 + m.x132 - m.x133 == 0)

m.c85 = Constraint(expr= - m.x121 + m.x134 - m.x135 == 0)

m.c86 = Constraint(expr=   m.x132 - m.x134 - m.x136 == 0)

m.c87 = Constraint(expr= - m.x121 + m.x137 - m.x138 == 0)

m.c88 = Constraint(expr=   m.x98 - m.x139 - m.x140 == 0)

m.c89 = Constraint(expr=   m.x99 - m.x141 - m.x142 == 0)

m.c90 = Constraint(expr= - m.x128 + m.x131 - m.x143 == 0)

m.c91 = Constraint(expr= - 239.978718892*m.x63 + 239.978718892*m.x64 - 416.560177655*m.x65 + 416.560177655*m.x66
                         - 416.560177655*m.x67 + 416.560177655*m.x68 - 165.129961038*m.x69 + 165.129961038*m.x70 >= 0)

m.c92 = Constraint(expr=   m.b2 - m.b9 >= 0)

m.c93 = Constraint(expr=   m.b3 - m.b4 >= 0)

m.c94 = Constraint(expr=   m.b4 - m.b5 >= 0)

m.c95 = Constraint(expr=   m.b5 - m.b6 >= 0)

m.c96 = Constraint(expr=   m.b6 - m.b7 >= 0)

m.c97 = Constraint(expr=   m.b7 - m.b8 >= 0)

m.c98 = Constraint(expr=   m.b10 - m.b11 >= 0)

m.c99 = Constraint(expr=   m.b11 - m.b12 >= 0)

m.c100 = Constraint(expr=   m.x33 - m.x71 - m.x73 - m.x75 - m.x77 - m.x79 - m.x81 - m.x83 - m.x85 == 0)

m.c101 = Constraint(expr=   m.x56 - m.x87 - m.x89 - m.x91 - m.x93 == 0)

m.c102 = Constraint(expr= - 712.572602172813*m.b2 + m.x72 - m.x142 >= -712.572602172813)

m.c103 = Constraint(expr= - 851.700667228731*m.b3 + m.x78 - m.x142 >= -851.700667228731)

m.c104 = Constraint(expr= - 851.700667228731*m.b4 + m.x84 - m.x142 >= -851.700667228731)

m.c105 = Constraint(expr= - 851.700667228731*m.b5 + m.x90 - m.x142 >= -851.700667228731)

m.c106 = Constraint(expr= - 851.700667228731*m.b6 - m.x142 + m.x144 >= -851.700667228731)

m.c107 = Constraint(expr= - 851.700667228731*m.b7 + m.x17 - m.x142 >= -851.700667228731)

m.c108 = Constraint(expr= - 851.700667228731*m.b8 + m.x20 - m.x142 >= -851.700667228731)

m.c109 = Constraint(expr= - 712.572602172813*m.b9 + m.x22 - m.x142 >= -712.572602172813)

m.c110 = Constraint(expr= - 925.825187656153*m.b10 + m.x24 - m.x143 >= -925.825187656153)

m.c111 = Constraint(expr= - 925.825187656153*m.b11 + m.x26 - m.x143 >= -925.825187656153)

m.c112 = Constraint(expr= - 925.825187656153*m.b12 + m.x28 - m.x143 >= -925.825187656153)

m.c113 = Constraint(expr= - 925.825187656502*m.b13 + m.x30 - m.x143 >= -925.825187656502)

m.c114 = Constraint(expr=   447.864247971*m.b2 + m.x72 - m.x142 <= 447.864247971)

m.c115 = Constraint(expr=   672.20455381568*m.b3 + m.x78 - m.x142 <= 672.20455381568)

m.c116 = Constraint(expr=   672.20455381568*m.b4 + m.x84 - m.x142 <= 672.20455381568)

m.c117 = Constraint(expr=   672.20455381568*m.b5 + m.x90 - m.x142 <= 672.20455381568)

m.c118 = Constraint(expr=   672.20455381568*m.b6 - m.x142 + m.x144 <= 672.20455381568)

m.c119 = Constraint(expr=   672.20455381568*m.b7 + m.x17 - m.x142 <= 672.20455381568)

m.c120 = Constraint(expr=   672.20455381568*m.b8 + m.x20 - m.x142 <= 672.20455381568)

m.c121 = Constraint(expr=   447.864247971*m.b9 + m.x22 - m.x142 <= 447.864247971)

m.c122 = Constraint(expr=   1106.777870451*m.b10 + m.x24 - m.x143 <= 1106.777870451)

m.c123 = Constraint(expr=   1106.777870451*m.b11 + m.x26 - m.x143 <= 1106.777870451)

m.c124 = Constraint(expr=   1106.777870451*m.b12 + m.x28 - m.x143 <= 1106.777870451)

m.c125 = Constraint(expr=   1106.777870452*m.b13 + m.x30 - m.x143 <= 1106.777870452)

m.c126 = Constraint(expr= - 5*m.b14 + m.x41 <= 0)

m.c127 = Constraint(expr= - 5*m.b15 + m.x58 <= 0)

m.c128 = Constraint(expr= - 5*m.b16 + m.x53 <= 0)

m.c129 = Constraint(expr= - 1000*m.b14 + m.x109 - m.x121 >= -1000)

m.c130 = Constraint(expr= - 1000*m.b15 + m.x131 - m.x137 >= -1000)

m.c131 = Constraint(expr= - 1000*m.b16 + m.x122 - m.x124 >= -1000)

m.c132 = Constraint(expr= - 1000*m.b14 + m.x109 - m.x121 <= 0)

m.c133 = Constraint(expr= - 1000*m.b15 + m.x131 - m.x137 <= 0)

m.c134 = Constraint(expr= - 1000*m.b16 + m.x122 - m.x124 <= 0)

m.c135 = Constraint(expr= - m.x96 + m.x121 >= 60)

m.c136 = Constraint(expr= - m.x97 + m.x121 >= 60)

m.c137 = Constraint(expr= - m.x98 + m.x134 >= 50)

m.c138 = Constraint(expr=60159.7666785*m.x71**2 - m.x74 == 0)

m.c139 = Constraint(expr=16103.4266989*m.x73**2 - m.x80 == 0)

m.c140 = Constraint(expr=16103.4266989*m.x75**2 - m.x86 == 0)

m.c141 = Constraint(expr=16103.4266989*m.x77**2 - m.x92 == 0)

m.c142 = Constraint(expr=16103.4266989*m.x79**2 - m.x145 == 0)

m.c143 = Constraint(expr=16103.4266989*m.x81**2 - m.x18 == 0)

m.c144 = Constraint(expr=16103.4266989*m.x83**2 - m.x21 == 0)

m.c145 = Constraint(expr=60159.7666785*m.x85**2 - m.x23 == 0)

m.c146 = Constraint(expr=2296.01902001*m.x87**2 - m.x25 == 0)

m.c147 = Constraint(expr=2296.01902001*m.x89**2 - m.x27 == 0)

m.c148 = Constraint(expr=2296.01902001*m.x91**2 - m.x29 == 0)

m.c149 = Constraint(expr=6324.78464025*m.x93**2 - m.x31 == 0)

m.c150 = Constraint(expr=2.4525*m.x71*m.x72 - m.x147 <= 0)

m.c151 = Constraint(expr=2.4525*m.x73*m.x78 - m.x148 <= 0)

m.c152 = Constraint(expr=2.4525*m.x75*m.x84 - m.x149 <= 0)

m.c153 = Constraint(expr=2.4525*m.x77*m.x90 - m.x150 <= 0)

m.c154 = Constraint(expr=2.4525*m.x79*m.x144 - m.x151 <= 0)

m.c155 = Constraint(expr=2.4525*m.x17*m.x81 - m.x152 <= 0)

m.c156 = Constraint(expr=2.4525*m.x20*m.x83 - m.x153 <= 0)

m.c157 = Constraint(expr=2.4525*m.x22*m.x85 - m.x154 <= 0)

m.c158 = Constraint(expr=2.4525*m.x24*m.x87 - m.x155 <= 0)

m.c159 = Constraint(expr=2.4525*m.x26*m.x89 - m.x156 <= 0)

m.c160 = Constraint(expr=2.4525*m.x28*m.x91 - m.x157 <= 0)

m.c161 = Constraint(expr=2.4525*m.x30*m.x93 - m.x158 <= 0)

m.c162 = Constraint(expr=SignPower(m.x32,2) - 0.107595782151047*m.x101 == 0)

m.c163 = Constraint(expr=SignPower(m.x34,2) - 0.000240846101592208*m.x103 == 0)

m.c164 = Constraint(expr=SignPower(m.x36,2) - 0.0011039398274554*m.x105 == 0)

m.c165 = Constraint(expr=SignPower(m.x44,2) - 0.0147658094299242*m.x108 == 0)

m.c166 = Constraint(expr=SignPower(m.x40,2) - 0.0126524872624481*m.x111 == 0)

m.c167 = Constraint(expr=SignPower(m.x39,2) - 0.000713164667292268*m.x112 == 0)

m.c168 = Constraint(expr=SignPower(m.x35,2) - 0.0253049745248962*m.x113 == 0)

m.c169 = Constraint(expr=SignPower(m.x50,2) - 0.0196735206566467*m.x114 == 0)

m.c170 = Constraint(expr=SignPower(m.x42,2) - 0.13436247753087*m.x115 == 0)

m.c171 = Constraint(expr=SignPower(m.x43,2) - 0.13436247753087*m.x116 == 0)

m.c172 = Constraint(expr=SignPower(m.x37,2) - 0.00268724955062101*m.x118 == 0)

m.c173 = Constraint(expr=SignPower(m.x38,2) - 0.00175817654162355*m.x120 == 0)

m.c174 = Constraint(expr=SignPower(m.x45,2) - 0.0156579704750926*m.x123 == 0)

m.c175 = Constraint(expr=SignPower(m.x51,2) - 0.4031634796292*m.x126 == 0)

m.c176 = Constraint(expr=SignPower(m.x52,2) - 0.4031634796292*m.x127 == 0)

m.c177 = Constraint(expr=SignPower(m.x54,2) - 8.06326959261651*m.x129 == 0)

m.c178 = Constraint(expr=SignPower(m.x55,2) - 8.06326959261651*m.x130 == 0)

m.c179 = Constraint(expr=SignPower(m.x57,2) - 0.000180519501834947*m.x133 == 0)

m.c180 = Constraint(expr=SignPower(m.x46,2) - 0.000180519501834947*m.x135 == 0)

m.c181 = Constraint(expr=SignPower(m.x59,2) - 0.013538962637621*m.x136 == 0)

m.c182 = Constraint(expr=SignPower(m.x47,2) - 0.0463936827608069*m.x138 == 0)

m.c183 = Constraint(expr=SignPower(m.x61,2) - 0.0964450219247959*m.x140 == 0)
