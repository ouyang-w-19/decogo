#  MINLP written by GAMS Convert at 04/21/18 13:51:23
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        138       92        7       39        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        233       93      140        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        622      565       57        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x29 = Var(within=Reals,bounds=(0.01,4),initialize=1)
m.x30 = Var(within=Reals,bounds=(0.01,4),initialize=1)
m.x31 = Var(within=Reals,bounds=(0.01,4),initialize=1)
m.x32 = Var(within=Reals,bounds=(0.01,4),initialize=1)
m.x33 = Var(within=Reals,bounds=(0.01,4),initialize=1)
m.x34 = Var(within=Reals,bounds=(0.01,4),initialize=1)
m.x35 = Var(within=Reals,bounds=(0.01,4),initialize=1)
m.x36 = Var(within=Reals,bounds=(0.01,4),initialize=1)
m.x37 = Var(within=Reals,bounds=(0.01,4),initialize=1)
m.x38 = Var(within=Reals,bounds=(0.01,4),initialize=1)
m.x39 = Var(within=Reals,bounds=(0.01,4),initialize=1)
m.x40 = Var(within=Reals,bounds=(0.01,4),initialize=1)
m.x41 = Var(within=Reals,bounds=(0.01,4),initialize=1)
m.x42 = Var(within=Reals,bounds=(0.01,4),initialize=1)
m.x43 = Var(within=Reals,bounds=(0.01,4),initialize=1)
m.x44 = Var(within=Reals,bounds=(0.01,4),initialize=1)
m.x45 = Var(within=Reals,bounds=(0.01,4),initialize=1)
m.x46 = Var(within=Reals,bounds=(0.01,4),initialize=1)
m.x47 = Var(within=Reals,bounds=(0.01,4),initialize=1)
m.x48 = Var(within=Reals,bounds=(0.01,4),initialize=1)
m.x49 = Var(within=Reals,bounds=(0.01,4),initialize=1)
m.x50 = Var(within=Reals,bounds=(0.01,4),initialize=1)
m.x51 = Var(within=Reals,bounds=(0.01,4),initialize=1)
m.x52 = Var(within=Reals,bounds=(0.01,4),initialize=1)
m.x53 = Var(within=Reals,bounds=(0.01,4),initialize=1)
m.x54 = Var(within=Reals,bounds=(0.01,4),initialize=1)
m.x55 = Var(within=Reals,bounds=(0.01,4),initialize=1)
m.x56 = Var(within=Reals,bounds=(0.01,4),initialize=1)
m.x57 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x58 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x59 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x60 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x61 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x62 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x63 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x64 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x65 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x66 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x67 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x68 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x69 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x70 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x71 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x72 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x73 = Var(within=Reals,bounds=(0,None),initialize=0)
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
m.x92 = Var(within=Reals,bounds=(0,None),initialize=100)
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
m.b121 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b122 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b123 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b124 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b125 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b126 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b127 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b128 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b129 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b130 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b131 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b132 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b133 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b134 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b135 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b136 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b137 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b138 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b139 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b140 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b141 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b142 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b143 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b144 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b145 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b146 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b147 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b148 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b149 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b150 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b151 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b152 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b153 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b154 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b155 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b156 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b157 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b158 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b159 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b160 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b161 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b162 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b163 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b164 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b165 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b166 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b167 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b168 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b169 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b170 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b171 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b172 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b173 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b174 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b175 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b176 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b177 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b178 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b179 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b180 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b181 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b182 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b183 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b184 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b185 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b186 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b187 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b188 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b189 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b190 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b191 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b192 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b193 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b194 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b195 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b196 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b197 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b198 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b199 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b200 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b201 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b202 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b203 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b204 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b205 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b206 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b207 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b208 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b209 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b210 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b211 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b212 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b213 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b214 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b215 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b216 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b217 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b218 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b219 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b220 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b221 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b222 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b223 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b224 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b225 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b226 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b227 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b228 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b229 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b230 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b231 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b232 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=-((479700 - 479700*exp(-0.1*m.x1/m.x29))*m.x29 + 31980*m.x1 - 100*m.x29 + (252000 - 252000*exp(-
                       0.2*m.x2/m.x30))*m.x30 + 22680*m.x2 - 90*m.x30 + (423500 - 423500*exp(-0.1*m.x3/m.x31))*m.x31 + 
                       25410*m.x3 - 80*m.x31 + (157440 - 157440*exp(-0.2*m.x4/m.x32))*m.x32 + 19680*m.x4 - 75*m.x32 + (
                       172108.695652174 - 172108.695652174*exp(-0.23*m.x5/m.x33))*m.x33 + 40950*m.x5 - 90*m.x33 + (
                       33970.5882352941 - 33970.5882352941*exp(-0.34*m.x6/m.x34))*m.x34 + 8580*m.x6 - 93*m.x34 + (130200
                        - 130200*exp(-0.2*m.x7/m.x35))*m.x35 + 13440*m.x7 - 78*m.x35 + (200640 - 200640*exp(-0.2*m.x8/
                       m.x36))*m.x36 + 26334*m.x8 - 80*m.x36 + (526680 - 526680*exp(-0.1*m.x9/m.x37))*m.x37 + 26334*m.x9
                        - 85*m.x37 + (212850 - 212850*exp(-0.2*m.x10/m.x38))*m.x38 + 29670*m.x10 - 75*m.x38 + (141360 - 
                       141360*exp(-0.25*m.x11/m.x39))*m.x39 + 28500*m.x11 - 90*m.x39 + (152937.931034483 - 
                       152937.931034483*exp(-0.29*m.x12/m.x40))*m.x40 + 49104*m.x12 - 94*m.x40 + (76444.4444444444 - 
                       76444.4444444444*exp(-0.27*m.x13/m.x41))*m.x41 + 13932*m.x13 - 78*m.x41 + (76840 - 76840*exp(-0.3
                       *m.x14/m.x42))*m.x42 + 11526*m.x14 - 70*m.x42 + (102300 - 102300*exp(-0.3*m.x15/m.x43))*m.x43 + 
                       18810*m.x15 - 90*m.x43 + (170800 - 170800*exp(-0.2*m.x16/m.x44))*m.x44 + 17568*m.x16 - 90*m.x44
                        + (115200 - 115200*exp(-0.3*m.x17/m.x45))*m.x45 + 20160*m.x17 - 90*m.x45 + (176000 - 176000*exp(
                       -0.27*m.x18/m.x46))*m.x46 + 30360*m.x18 - 85*m.x46 + (126357.142857143 - 126357.142857143*exp(-
                       0.28*m.x19/m.x47))*m.x47 + 36600*m.x19 - 93*m.x47 + (45931.0344827586 - 45931.0344827586*exp(-
                       0.29*m.x20/m.x48))*m.x48 + 9000*m.x20 - 92*m.x48 + (123318 - 123318*exp(-0.25*m.x21/m.x49))*m.x49
                        + 17901*m.x21 - 75*m.x49 + (223200 - 223200*exp(-0.2*m.x22/m.x50))*m.x50 + 28800*m.x22 - 80*
                       m.x50 + (225000 - 225000*exp(-0.2*m.x23/m.x51))*m.x51 + 23750*m.x23 - 90*m.x51 + (240800 - 240800
                       *exp(-0.15*m.x24/m.x52))*m.x52 + 21672*m.x24 - 85*m.x52 + (115920 - 115920*exp(-0.25*m.x25/m.x53)
                       )*m.x53 + 19320*m.x25 - 80*m.x53 + (133241.379310345 - 133241.379310345*exp(-0.29*m.x26/m.x54))*
                       m.x54 + 42780*m.x26 - 92*m.x54 + (90763.6363636364 - 90763.6363636364*exp(-0.22*m.x27/m.x55))*
                       m.x55 + 13312*m.x27 - 85*m.x55 + (78857.1428571429 - 78857.1428571429*exp(-0.28*m.x28/m.x56))*
                       m.x56 + 11730*m.x28 - 72*m.x56)/m.x92, sense=minimize)

m.c2 = Constraint(expr= - 1300*m.x1 - 1100*m.x8 - 900*m.x15 - 1200*m.x22 + m.x57 + 300*m.x92 == 0)

m.c3 = Constraint(expr= - 1200*m.x2 - 1050*m.x9 - 800*m.x16 - 1000*m.x23 + m.x58 + 400*m.x92 == 0)

m.c4 = Constraint(expr= - 1100*m.x3 - 1000*m.x10 - 800*m.x17 - 800*m.x24 + m.x59 + 300*m.x92 == 0)

m.c5 = Constraint(expr= - 800*m.x4 - 1000*m.x11 - 1200*m.x18 - 700*m.x25 + m.x60 + 500*m.x92 == 0)

m.c6 = Constraint(expr= - 1300*m.x5 - 1200*m.x12 - 1000*m.x19 - 1200*m.x26 + m.x61 + 500*m.x92 == 0)

m.c7 = Constraint(expr= - 300*m.x6 - 400*m.x13 - 300*m.x20 - 400*m.x27 + m.x62 + 100*m.x92 == 0)

m.c8 = Constraint(expr= - 700*m.x7 - 600*m.x14 - 850*m.x21 - 600*m.x28 + m.x63 + 600*m.x92 == 0)

m.c9 = Constraint(expr=   m.x57 - 300*m.x92 <= 0)

m.c10 = Constraint(expr=   m.x58 - 300*m.x92 <= 0)

m.c11 = Constraint(expr=   m.x59 - 300*m.x92 <= 0)

m.c12 = Constraint(expr=   m.x60 - 300*m.x92 <= 0)

m.c13 = Constraint(expr=   m.x61 - 300*m.x92 <= 0)

m.c14 = Constraint(expr=   m.x62 - 300*m.x92 <= 0)

m.c15 = Constraint(expr=   m.x63 - 300*m.x92 <= 0)

m.c16 = Constraint(expr=   m.x29 - 0.01*m.b93 - m.b94 - 2*m.b95 - 3*m.b96 - 4*m.b97 == 0)

m.c17 = Constraint(expr=   m.x30 - 0.01*m.b98 - m.b99 - 2*m.b100 - 3*m.b101 - 4*m.b102 == 0)

m.c18 = Constraint(expr=   m.x31 - 0.01*m.b103 - m.b104 - 2*m.b105 - 3*m.b106 - 4*m.b107 == 0)

m.c19 = Constraint(expr=   m.x32 - 0.01*m.b108 - m.b109 - 2*m.b110 - 3*m.b111 - 4*m.b112 == 0)

m.c20 = Constraint(expr=   m.x33 - 0.01*m.b113 - m.b114 - 2*m.b115 - 3*m.b116 - 4*m.b117 == 0)

m.c21 = Constraint(expr=   m.x34 - 0.01*m.b118 - m.b119 - 2*m.b120 - 3*m.b121 - 4*m.b122 == 0)

m.c22 = Constraint(expr=   m.x35 - 0.01*m.b123 - m.b124 - 2*m.b125 - 3*m.b126 - 4*m.b127 == 0)

m.c23 = Constraint(expr=   m.x36 - 0.01*m.b128 - m.b129 - 2*m.b130 - 3*m.b131 - 4*m.b132 == 0)

m.c24 = Constraint(expr=   m.x37 - 0.01*m.b133 - m.b134 - 2*m.b135 - 3*m.b136 - 4*m.b137 == 0)

m.c25 = Constraint(expr=   m.x38 - 0.01*m.b138 - m.b139 - 2*m.b140 - 3*m.b141 - 4*m.b142 == 0)

m.c26 = Constraint(expr=   m.x39 - 0.01*m.b143 - m.b144 - 2*m.b145 - 3*m.b146 - 4*m.b147 == 0)

m.c27 = Constraint(expr=   m.x40 - 0.01*m.b148 - m.b149 - 2*m.b150 - 3*m.b151 - 4*m.b152 == 0)

m.c28 = Constraint(expr=   m.x41 - 0.01*m.b153 - m.b154 - 2*m.b155 - 3*m.b156 - 4*m.b157 == 0)

m.c29 = Constraint(expr=   m.x42 - 0.01*m.b158 - m.b159 - 2*m.b160 - 3*m.b161 - 4*m.b162 == 0)

m.c30 = Constraint(expr=   m.x43 - 0.01*m.b163 - m.b164 - 2*m.b165 - 3*m.b166 - 4*m.b167 == 0)

m.c31 = Constraint(expr=   m.x44 - 0.01*m.b168 - m.b169 - 2*m.b170 - 3*m.b171 - 4*m.b172 == 0)

m.c32 = Constraint(expr=   m.x45 - 0.01*m.b173 - m.b174 - 2*m.b175 - 3*m.b176 - 4*m.b177 == 0)

m.c33 = Constraint(expr=   m.x46 - 0.01*m.b178 - m.b179 - 2*m.b180 - 3*m.b181 - 4*m.b182 == 0)

m.c34 = Constraint(expr=   m.x47 - 0.01*m.b183 - m.b184 - 2*m.b185 - 3*m.b186 - 4*m.b187 == 0)

m.c35 = Constraint(expr=   m.x48 - 0.01*m.b188 - m.b189 - 2*m.b190 - 3*m.b191 - 4*m.b192 == 0)

m.c36 = Constraint(expr=   m.x49 - 0.01*m.b193 - m.b194 - 2*m.b195 - 3*m.b196 - 4*m.b197 == 0)

m.c37 = Constraint(expr=   m.x50 - 0.01*m.b198 - m.b199 - 2*m.b200 - 3*m.b201 - 4*m.b202 == 0)

m.c38 = Constraint(expr=   m.x51 - 0.01*m.b203 - m.b204 - 2*m.b205 - 3*m.b206 - 4*m.b207 == 0)

m.c39 = Constraint(expr=   m.x52 - 0.01*m.b208 - m.b209 - 2*m.b210 - 3*m.b211 - 4*m.b212 == 0)

m.c40 = Constraint(expr=   m.x53 - 0.01*m.b213 - m.b214 - 2*m.b215 - 3*m.b216 - 4*m.b217 == 0)

m.c41 = Constraint(expr=   m.x54 - 0.01*m.b218 - m.b219 - 2*m.b220 - 3*m.b221 - 4*m.b222 == 0)

m.c42 = Constraint(expr=   m.x55 - 0.01*m.b223 - m.b224 - 2*m.b225 - 3*m.b226 - 4*m.b227 == 0)

m.c43 = Constraint(expr=   m.x56 - 0.01*m.b228 - m.b229 - 2*m.b230 - 3*m.b231 - 4*m.b232 == 0)

m.c44 = Constraint(expr= - m.b93 - m.b94 - m.b95 - m.b96 - m.b97 == -1)

m.c45 = Constraint(expr= - m.b98 - m.b99 - m.b100 - m.b101 - m.b102 == -1)

m.c46 = Constraint(expr= - m.b103 - m.b104 - m.b105 - m.b106 - m.b107 == -1)

m.c47 = Constraint(expr= - m.b108 - m.b109 - m.b110 - m.b111 - m.b112 == -1)

m.c48 = Constraint(expr= - m.b113 - m.b114 - m.b115 - m.b116 - m.b117 == -1)

m.c49 = Constraint(expr= - m.b118 - m.b119 - m.b120 - m.b121 - m.b122 == -1)

m.c50 = Constraint(expr= - m.b123 - m.b124 - m.b125 - m.b126 - m.b127 == -1)

m.c51 = Constraint(expr= - m.b128 - m.b129 - m.b130 - m.b131 - m.b132 == -1)

m.c52 = Constraint(expr= - m.b133 - m.b134 - m.b135 - m.b136 - m.b137 == -1)

m.c53 = Constraint(expr= - m.b138 - m.b139 - m.b140 - m.b141 - m.b142 == -1)

m.c54 = Constraint(expr= - m.b143 - m.b144 - m.b145 - m.b146 - m.b147 == -1)

m.c55 = Constraint(expr= - m.b148 - m.b149 - m.b150 - m.b151 - m.b152 == -1)

m.c56 = Constraint(expr= - m.b153 - m.b154 - m.b155 - m.b156 - m.b157 == -1)

m.c57 = Constraint(expr= - m.b158 - m.b159 - m.b160 - m.b161 - m.b162 == -1)

m.c58 = Constraint(expr= - m.b163 - m.b164 - m.b165 - m.b166 - m.b167 == -1)

m.c59 = Constraint(expr= - m.b168 - m.b169 - m.b170 - m.b171 - m.b172 == -1)

m.c60 = Constraint(expr= - m.b173 - m.b174 - m.b175 - m.b176 - m.b177 == -1)

m.c61 = Constraint(expr= - m.b178 - m.b179 - m.b180 - m.b181 - m.b182 == -1)

m.c62 = Constraint(expr= - m.b183 - m.b184 - m.b185 - m.b186 - m.b187 == -1)

m.c63 = Constraint(expr= - m.b188 - m.b189 - m.b190 - m.b191 - m.b192 == -1)

m.c64 = Constraint(expr= - m.b193 - m.b194 - m.b195 - m.b196 - m.b197 == -1)

m.c65 = Constraint(expr= - m.b198 - m.b199 - m.b200 - m.b201 - m.b202 == -1)

m.c66 = Constraint(expr= - m.b203 - m.b204 - m.b205 - m.b206 - m.b207 == -1)

m.c67 = Constraint(expr= - m.b208 - m.b209 - m.b210 - m.b211 - m.b212 == -1)

m.c68 = Constraint(expr= - m.b213 - m.b214 - m.b215 - m.b216 - m.b217 == -1)

m.c69 = Constraint(expr= - m.b218 - m.b219 - m.b220 - m.b221 - m.b222 == -1)

m.c70 = Constraint(expr= - m.b223 - m.b224 - m.b225 - m.b226 - m.b227 == -1)

m.c71 = Constraint(expr= - m.b228 - m.b229 - m.b230 - m.b231 - m.b232 == -1)

m.c72 = Constraint(expr= - m.x1 - 2*m.x29 + m.x64 == 0)

m.c73 = Constraint(expr= - m.x2 - 3*m.x30 + m.x65 == 0)

m.c74 = Constraint(expr= - m.x3 - 3*m.x31 + m.x66 == 0)

m.c75 = Constraint(expr= - m.x4 - 3*m.x32 + m.x67 == 0)

m.c76 = Constraint(expr= - m.x5 - m.x33 + m.x68 == 0)

m.c77 = Constraint(expr= - m.x6 - 2*m.x34 + m.x69 == 0)

m.c78 = Constraint(expr= - m.x7 - 3*m.x35 + m.x70 == 0)

m.c79 = Constraint(expr= - m.x8 - 3*m.x36 + m.x71 == 0)

m.c80 = Constraint(expr= - m.x9 - m.x37 + m.x72 == 0)

m.c81 = Constraint(expr= - m.x10 - 2*m.x38 + m.x73 == 0)

m.c82 = Constraint(expr= - m.x11 - 2*m.x39 + m.x74 == 0)

m.c83 = Constraint(expr= - m.x12 - 2*m.x40 + m.x75 == 0)

m.c84 = Constraint(expr= - m.x13 - m.x41 + m.x76 == 0)

m.c85 = Constraint(expr= - m.x14 - m.x42 + m.x77 == 0)

m.c86 = Constraint(expr= - m.x15 - m.x43 + m.x78 == 0)

m.c87 = Constraint(expr= - m.x16 - 3*m.x44 + m.x79 == 0)

m.c88 = Constraint(expr= - m.x17 - m.x45 + m.x80 == 0)

m.c89 = Constraint(expr= - m.x18 - m.x46 + m.x81 == 0)

m.c90 = Constraint(expr= - m.x19 - 2*m.x47 + m.x82 == 0)

m.c91 = Constraint(expr= - m.x20 - m.x48 + m.x83 == 0)

m.c92 = Constraint(expr= - m.x21 - 2*m.x49 + m.x84 == 0)

m.c93 = Constraint(expr= - m.x22 - 2*m.x50 + m.x85 == 0)

m.c94 = Constraint(expr= - m.x23 - m.x51 + m.x86 == 0)

m.c95 = Constraint(expr= - m.x24 - 3*m.x52 + m.x87 == 0)

m.c96 = Constraint(expr= - m.x25 - 2*m.x53 + m.x88 == 0)

m.c97 = Constraint(expr= - m.x26 - 2*m.x54 + m.x89 == 0)

m.c98 = Constraint(expr= - m.x27 - m.x55 + m.x90 == 0)

m.c99 = Constraint(expr= - m.x28 - m.x56 + m.x91 == 0)

m.c100 = Constraint(expr=   m.x64 + m.x65 + m.x66 + m.x67 + m.x68 + m.x69 + m.x70 - m.x92 <= 0)

m.c101 = Constraint(expr=   m.x71 + m.x72 + m.x73 + m.x74 + m.x75 + m.x76 + m.x77 - m.x92 <= 0)

m.c102 = Constraint(expr=   m.x78 + m.x79 + m.x80 + m.x81 + m.x82 + m.x83 + m.x84 - m.x92 <= 0)

m.c103 = Constraint(expr=   m.x85 + m.x86 + m.x87 + m.x88 + m.x89 + m.x90 + m.x91 - m.x92 <= 0)

m.c104 = Constraint(expr=   m.x1 + 100*m.b93 <= 100)

m.c105 = Constraint(expr=   m.x2 + 100*m.b98 <= 100)

m.c106 = Constraint(expr=   m.x3 + 100*m.b103 <= 100)

m.c107 = Constraint(expr=   m.x4 + 100*m.b108 <= 100)

m.c108 = Constraint(expr=   m.x5 + 100*m.b113 <= 100)

m.c109 = Constraint(expr=   m.x6 + 100*m.b118 <= 100)

m.c110 = Constraint(expr=   m.x7 + 100*m.b123 <= 100)

m.c111 = Constraint(expr=   m.x8 + 100*m.b128 <= 100)

m.c112 = Constraint(expr=   m.x9 + 100*m.b133 <= 100)

m.c113 = Constraint(expr=   m.x10 + 100*m.b138 <= 100)

m.c114 = Constraint(expr=   m.x11 + 100*m.b143 <= 100)

m.c115 = Constraint(expr=   m.x12 + 100*m.b148 <= 100)

m.c116 = Constraint(expr=   m.x13 + 100*m.b153 <= 100)

m.c117 = Constraint(expr=   m.x14 + 100*m.b158 <= 100)

m.c118 = Constraint(expr=   m.x15 + 100*m.b163 <= 100)

m.c119 = Constraint(expr=   m.x16 + 100*m.b168 <= 100)

m.c120 = Constraint(expr=   m.x17 + 100*m.b173 <= 100)

m.c121 = Constraint(expr=   m.x18 + 100*m.b178 <= 100)

m.c122 = Constraint(expr=   m.x19 + 100*m.b183 <= 100)

m.c123 = Constraint(expr=   m.x20 + 100*m.b188 <= 100)

m.c124 = Constraint(expr=   m.x21 + 100*m.b193 <= 100)

m.c125 = Constraint(expr=   m.x22 + 100*m.b198 <= 100)

m.c126 = Constraint(expr=   m.x23 + 100*m.b203 <= 100)

m.c127 = Constraint(expr=   m.x24 + 100*m.b208 <= 100)

m.c128 = Constraint(expr=   m.x25 + 100*m.b213 <= 100)

m.c129 = Constraint(expr=   m.x26 + 100*m.b218 <= 100)

m.c130 = Constraint(expr=   m.x27 + 100*m.b223 <= 100)

m.c131 = Constraint(expr=   m.x28 + 100*m.b228 <= 100)

m.c132 = Constraint(expr=   m.x29 + m.x36 + m.x43 + m.x50 >= 1)

m.c133 = Constraint(expr=   m.x30 + m.x37 + m.x44 + m.x51 >= 1)

m.c134 = Constraint(expr=   m.x31 + m.x38 + m.x45 + m.x52 >= 1)

m.c135 = Constraint(expr=   m.x32 + m.x39 + m.x46 + m.x53 >= 1)

m.c136 = Constraint(expr=   m.x33 + m.x40 + m.x47 + m.x54 >= 1)

m.c137 = Constraint(expr=   m.x34 + m.x41 + m.x48 + m.x55 >= 1)

m.c138 = Constraint(expr=   m.x35 + m.x42 + m.x49 + m.x56 >= 1)
