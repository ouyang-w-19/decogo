#  NLP written by GAMS Convert at 04/21/18 13:53:07
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         97       97        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        117      117        0        0        0        0        0        0
#  FX      4        4        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        337      257       80        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,None),initialize=14)
m.x2 = Var(within=Reals,bounds=(0,None),initialize=14)
m.x3 = Var(within=Reals,bounds=(0,None),initialize=14)
m.x4 = Var(within=Reals,bounds=(0,None),initialize=14)
m.x5 = Var(within=Reals,bounds=(0,None),initialize=14)
m.x6 = Var(within=Reals,bounds=(0,None),initialize=14)
m.x7 = Var(within=Reals,bounds=(0,None),initialize=14)
m.x8 = Var(within=Reals,bounds=(0,None),initialize=14)
m.x9 = Var(within=Reals,bounds=(0,None),initialize=14)
m.x10 = Var(within=Reals,bounds=(0,None),initialize=14)
m.x11 = Var(within=Reals,bounds=(0,None),initialize=14)
m.x12 = Var(within=Reals,bounds=(0,None),initialize=14)
m.x13 = Var(within=Reals,bounds=(0,None),initialize=14)
m.x14 = Var(within=Reals,bounds=(0,None),initialize=14)
m.x15 = Var(within=Reals,bounds=(0,None),initialize=14)
m.x16 = Var(within=Reals,bounds=(0,None),initialize=14)
m.x17 = Var(within=Reals,bounds=(18,18),initialize=18)
m.x18 = Var(within=Reals,bounds=(0,None),initialize=18)
m.x19 = Var(within=Reals,bounds=(0,None),initialize=18)
m.x20 = Var(within=Reals,bounds=(0,None),initialize=18)
m.x21 = Var(within=Reals,bounds=(0,None),initialize=18)
m.x22 = Var(within=Reals,bounds=(0,None),initialize=18)
m.x23 = Var(within=Reals,bounds=(0,None),initialize=18)
m.x24 = Var(within=Reals,bounds=(0,None),initialize=18)
m.x25 = Var(within=Reals,bounds=(0,None),initialize=18)
m.x26 = Var(within=Reals,bounds=(0,None),initialize=18)
m.x27 = Var(within=Reals,bounds=(0,None),initialize=18)
m.x28 = Var(within=Reals,bounds=(0,None),initialize=18)
m.x29 = Var(within=Reals,bounds=(0,None),initialize=18)
m.x30 = Var(within=Reals,bounds=(0,None),initialize=18)
m.x31 = Var(within=Reals,bounds=(0,None),initialize=18)
m.x32 = Var(within=Reals,bounds=(0,None),initialize=18)
m.x33 = Var(within=Reals,bounds=(0,None),initialize=18)
m.x34 = Var(within=Reals,bounds=(6.5,6.5),initialize=6.5)
m.x35 = Var(within=Reals,bounds=(0,None),initialize=7)
m.x36 = Var(within=Reals,bounds=(0,None),initialize=7)
m.x37 = Var(within=Reals,bounds=(0,None),initialize=7)
m.x38 = Var(within=Reals,bounds=(0,None),initialize=7)
m.x39 = Var(within=Reals,bounds=(0,None),initialize=7)
m.x40 = Var(within=Reals,bounds=(0,None),initialize=7)
m.x41 = Var(within=Reals,bounds=(0,None),initialize=7)
m.x42 = Var(within=Reals,bounds=(0,None),initialize=7)
m.x43 = Var(within=Reals,bounds=(0,None),initialize=7)
m.x44 = Var(within=Reals,bounds=(0,None),initialize=7)
m.x45 = Var(within=Reals,bounds=(0,None),initialize=7)
m.x46 = Var(within=Reals,bounds=(0,None),initialize=7)
m.x47 = Var(within=Reals,bounds=(0,None),initialize=7)
m.x48 = Var(within=Reals,bounds=(0,None),initialize=7)
m.x49 = Var(within=Reals,bounds=(0,None),initialize=7)
m.x50 = Var(within=Reals,bounds=(0,None),initialize=7)
m.x51 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x52 = Var(within=Reals,bounds=(0,None),initialize=7)
m.x53 = Var(within=Reals,bounds=(0,None),initialize=14)
m.x54 = Var(within=Reals,bounds=(0,None),initialize=21)
m.x55 = Var(within=Reals,bounds=(0,None),initialize=28)
m.x56 = Var(within=Reals,bounds=(0,None),initialize=35)
m.x57 = Var(within=Reals,bounds=(0,None),initialize=42)
m.x58 = Var(within=Reals,bounds=(0,None),initialize=49)
m.x59 = Var(within=Reals,bounds=(0,None),initialize=56)
m.x60 = Var(within=Reals,bounds=(0,None),initialize=63)
m.x61 = Var(within=Reals,bounds=(0,None),initialize=70)
m.x62 = Var(within=Reals,bounds=(0,None),initialize=77)
m.x63 = Var(within=Reals,bounds=(0,None),initialize=84)
m.x64 = Var(within=Reals,bounds=(0,None),initialize=91)
m.x65 = Var(within=Reals,bounds=(0,None),initialize=98)
m.x66 = Var(within=Reals,bounds=(0,None),initialize=105)
m.x67 = Var(within=Reals,bounds=(0,None),initialize=112)
m.x68 = Var(within=Reals,bounds=(0,None),initialize=11)
m.x69 = Var(within=Reals,bounds=(0,None),initialize=11)
m.x70 = Var(within=Reals,bounds=(0,None),initialize=11)
m.x71 = Var(within=Reals,bounds=(0,None),initialize=11)
m.x72 = Var(within=Reals,bounds=(0,None),initialize=11)
m.x73 = Var(within=Reals,bounds=(0,None),initialize=11)
m.x74 = Var(within=Reals,bounds=(0,None),initialize=11)
m.x75 = Var(within=Reals,bounds=(0,None),initialize=11)
m.x76 = Var(within=Reals,bounds=(0,None),initialize=11)
m.x77 = Var(within=Reals,bounds=(0,None),initialize=11)
m.x78 = Var(within=Reals,bounds=(0,None),initialize=11)
m.x79 = Var(within=Reals,bounds=(0,None),initialize=11)
m.x80 = Var(within=Reals,bounds=(0,None),initialize=11)
m.x81 = Var(within=Reals,bounds=(0,None),initialize=11)
m.x82 = Var(within=Reals,bounds=(0,None),initialize=11)
m.x83 = Var(within=Reals,bounds=(0,None),initialize=11)
m.x84 = Var(within=Reals,bounds=(500,500),initialize=500)
m.x85 = Var(within=Reals,bounds=(0,None),initialize=489)
m.x86 = Var(within=Reals,bounds=(0,None),initialize=478)
m.x87 = Var(within=Reals,bounds=(0,None),initialize=467)
m.x88 = Var(within=Reals,bounds=(0,None),initialize=456)
m.x89 = Var(within=Reals,bounds=(0,None),initialize=445)
m.x90 = Var(within=Reals,bounds=(0,None),initialize=434)
m.x91 = Var(within=Reals,bounds=(0,None),initialize=423)
m.x92 = Var(within=Reals,bounds=(0,None),initialize=412)
m.x93 = Var(within=Reals,bounds=(0,None),initialize=401)
m.x94 = Var(within=Reals,bounds=(0,None),initialize=390)
m.x95 = Var(within=Reals,bounds=(0,None),initialize=379)
m.x96 = Var(within=Reals,bounds=(0,None),initialize=368)
m.x97 = Var(within=Reals,bounds=(0,None),initialize=357)
m.x98 = Var(within=Reals,bounds=(0,None),initialize=346)
m.x99 = Var(within=Reals,bounds=(0,None),initialize=335)
m.x100 = Var(within=Reals,bounds=(0,None),initialize=324)
m.x101 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x102 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x103 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x104 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x105 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x106 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x107 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x108 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x109 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x110 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x111 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x112 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x113 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x114 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x115 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x116 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr= - m.x101 - 0.952380952380952*m.x102 - 0.90702947845805*m.x103 - 0.863837598531476*m.x104
                        - 0.822702474791882*m.x105 - 0.783526166468459*m.x106 - 0.746215396636628*m.x107
                        - 0.710681330130121*m.x108 - 0.676839362028687*m.x109 - 0.644608916217797*m.x110
                        - 0.613913253540759*m.x111 - 0.584679289086437*m.x112 - 0.556837418177559*m.x113
                        - 0.530321350645295*m.x114 - 0.505067952995519*m.x115 - 0.48101709809097*m.x116, sense=minimize)

m.c1 = Constraint(expr=   0.13*m.x1 - 0.87*m.x17 + m.x18 == 3.3)

m.c2 = Constraint(expr=   0.13*m.x2 - 0.87*m.x18 + m.x19 == 3.3345)

m.c3 = Constraint(expr=   0.13*m.x3 - 0.87*m.x19 + m.x20 == 3.3695175)

m.c4 = Constraint(expr=   0.13*m.x4 - 0.87*m.x20 + m.x21 == 3.4050602625)

m.c5 = Constraint(expr=   0.13*m.x5 - 0.87*m.x21 + m.x22 == 3.4411361664375)

m.c6 = Constraint(expr=   0.13*m.x6 - 0.87*m.x22 + m.x23 == 3.47775320893406)

m.c7 = Constraint(expr=   0.13*m.x7 - 0.87*m.x23 + m.x24 == 3.51491950706807)

m.c8 = Constraint(expr=   0.13*m.x8 - 0.87*m.x24 + m.x25 == 3.55264329967409)

m.c9 = Constraint(expr=   0.13*m.x9 - 0.87*m.x25 + m.x26 == 3.5909329491692)

m.c10 = Constraint(expr=   0.13*m.x10 - 0.87*m.x26 + m.x27 == 3.62979694340674)

m.c11 = Constraint(expr=   0.13*m.x11 - 0.87*m.x27 + m.x28 == 3.66924389755784)

m.c12 = Constraint(expr=   0.13*m.x12 - 0.87*m.x28 + m.x29 == 3.70928255602121)

m.c13 = Constraint(expr=   0.13*m.x13 - 0.87*m.x29 + m.x30 == 3.74992179436153)

m.c14 = Constraint(expr=   0.13*m.x14 - 0.87*m.x30 + m.x31 == 3.79117062127695)

m.c15 = Constraint(expr=   0.13*m.x15 - 0.87*m.x31 + m.x32 == 3.8330381805961)

m.c16 = Constraint(expr=   0.13*m.x16 - 0.87*m.x32 + m.x33 == 3.87553375330505)

m.c17 = Constraint(expr=-1.02**(-0.142857142857143*m.x52)*(1.1 + 0.1*m.x1) - 0.75*m.x34 + m.x35 == 0)

m.c18 = Constraint(expr=-1.02**(-0.142857142857143*m.x53)*(1.1 + 0.1*m.x2) - 0.75*m.x35 + m.x36 == 0)

m.c19 = Constraint(expr=-1.02**(-0.142857142857143*m.x54)*(1.1 + 0.1*m.x3) - 0.75*m.x36 + m.x37 == 0)

m.c20 = Constraint(expr=-1.02**(-0.142857142857143*m.x55)*(1.1 + 0.1*m.x4) - 0.75*m.x37 + m.x38 == 0)

m.c21 = Constraint(expr=-1.02**(-0.142857142857143*m.x56)*(1.1 + 0.1*m.x5) - 0.75*m.x38 + m.x39 == 0)

m.c22 = Constraint(expr=-1.02**(-0.142857142857143*m.x57)*(1.1 + 0.1*m.x6) - 0.75*m.x39 + m.x40 == 0)

m.c23 = Constraint(expr=-1.02**(-0.142857142857143*m.x58)*(1.1 + 0.1*m.x7) - 0.75*m.x40 + m.x41 == 0)

m.c24 = Constraint(expr=-1.02**(-0.142857142857143*m.x59)*(1.1 + 0.1*m.x8) - 0.75*m.x41 + m.x42 == 0)

m.c25 = Constraint(expr=-1.02**(-0.142857142857143*m.x60)*(1.1 + 0.1*m.x9) - 0.75*m.x42 + m.x43 == 0)

m.c26 = Constraint(expr=-1.02**(-0.142857142857143*m.x61)*(1.1 + 0.1*m.x10) - 0.75*m.x43 + m.x44 == 0)

m.c27 = Constraint(expr=-1.02**(-0.142857142857143*m.x62)*(1.1 + 0.1*m.x11) - 0.75*m.x44 + m.x45 == 0)

m.c28 = Constraint(expr=-1.02**(-0.142857142857143*m.x63)*(1.1 + 0.1*m.x12) - 0.75*m.x45 + m.x46 == 0)

m.c29 = Constraint(expr=-1.02**(-0.142857142857143*m.x64)*(1.1 + 0.1*m.x13) - 0.75*m.x46 + m.x47 == 0)

m.c30 = Constraint(expr=-1.02**(-0.142857142857143*m.x65)*(1.1 + 0.1*m.x14) - 0.75*m.x47 + m.x48 == 0)

m.c31 = Constraint(expr=-1.02**(-0.142857142857143*m.x66)*(1.1 + 0.1*m.x15) - 0.75*m.x48 + m.x49 == 0)

m.c32 = Constraint(expr=-1.02**(-0.142857142857143*m.x67)*(1.1 + 0.1*m.x16) - 0.75*m.x49 + m.x50 == 0)

m.c33 = Constraint(expr= - m.x35 - m.x51 + m.x52 == 0)

m.c34 = Constraint(expr= - m.x36 - m.x52 + m.x53 == 0)

m.c35 = Constraint(expr= - m.x37 - m.x53 + m.x54 == 0)

m.c36 = Constraint(expr= - m.x38 - m.x54 + m.x55 == 0)

m.c37 = Constraint(expr= - m.x39 - m.x55 + m.x56 == 0)

m.c38 = Constraint(expr= - m.x40 - m.x56 + m.x57 == 0)

m.c39 = Constraint(expr= - m.x41 - m.x57 + m.x58 == 0)

m.c40 = Constraint(expr= - m.x42 - m.x58 + m.x59 == 0)

m.c41 = Constraint(expr= - m.x43 - m.x59 + m.x60 == 0)

m.c42 = Constraint(expr= - m.x44 - m.x60 + m.x61 == 0)

m.c43 = Constraint(expr= - m.x45 - m.x61 + m.x62 == 0)

m.c44 = Constraint(expr= - m.x46 - m.x62 + m.x63 == 0)

m.c45 = Constraint(expr= - m.x47 - m.x63 + m.x64 == 0)

m.c46 = Constraint(expr= - m.x48 - m.x64 + m.x65 == 0)

m.c47 = Constraint(expr= - m.x49 - m.x65 + m.x66 == 0)

m.c48 = Constraint(expr= - m.x50 - m.x66 + m.x67 == 0)

m.c49 = Constraint(expr= - m.x18 + m.x35 + m.x68 == 0)

m.c50 = Constraint(expr= - m.x19 + m.x36 + m.x69 == 0)

m.c51 = Constraint(expr= - m.x20 + m.x37 + m.x70 == 0)

m.c52 = Constraint(expr= - m.x21 + m.x38 + m.x71 == 0)

m.c53 = Constraint(expr= - m.x22 + m.x39 + m.x72 == 0)

m.c54 = Constraint(expr= - m.x23 + m.x40 + m.x73 == 0)

m.c55 = Constraint(expr= - m.x24 + m.x41 + m.x74 == 0)

m.c56 = Constraint(expr= - m.x25 + m.x42 + m.x75 == 0)

m.c57 = Constraint(expr= - m.x26 + m.x43 + m.x76 == 0)

m.c58 = Constraint(expr= - m.x27 + m.x44 + m.x77 == 0)

m.c59 = Constraint(expr= - m.x28 + m.x45 + m.x78 == 0)

m.c60 = Constraint(expr= - m.x29 + m.x46 + m.x79 == 0)

m.c61 = Constraint(expr= - m.x30 + m.x47 + m.x80 == 0)

m.c62 = Constraint(expr= - m.x31 + m.x48 + m.x81 == 0)

m.c63 = Constraint(expr= - m.x32 + m.x49 + m.x82 == 0)

m.c64 = Constraint(expr= - m.x33 + m.x50 + m.x83 == 0)

m.c65 = Constraint(expr=   m.x68 - m.x84 + m.x85 == 0)

m.c66 = Constraint(expr=   m.x69 - m.x85 + m.x86 == 0)

m.c67 = Constraint(expr=   m.x70 - m.x86 + m.x87 == 0)

m.c68 = Constraint(expr=   m.x71 - m.x87 + m.x88 == 0)

m.c69 = Constraint(expr=   m.x72 - m.x88 + m.x89 == 0)

m.c70 = Constraint(expr=   m.x73 - m.x89 + m.x90 == 0)

m.c71 = Constraint(expr=   m.x74 - m.x90 + m.x91 == 0)

m.c72 = Constraint(expr=   m.x75 - m.x91 + m.x92 == 0)

m.c73 = Constraint(expr=   m.x76 - m.x92 + m.x93 == 0)

m.c74 = Constraint(expr=   m.x77 - m.x93 + m.x94 == 0)

m.c75 = Constraint(expr=   m.x78 - m.x94 + m.x95 == 0)

m.c76 = Constraint(expr=   m.x79 - m.x95 + m.x96 == 0)

m.c77 = Constraint(expr=   m.x80 - m.x96 + m.x97 == 0)

m.c78 = Constraint(expr=   m.x81 - m.x97 + m.x98 == 0)

m.c79 = Constraint(expr=   m.x82 - m.x98 + m.x99 == 0)

m.c80 = Constraint(expr=   m.x83 - m.x99 + m.x100 == 0)

m.c81 = Constraint(expr=-(m.x1 - 250/m.x85)*m.x68 + m.x101 == 0)

m.c82 = Constraint(expr=-(m.x2 - 250/m.x86)*m.x69 + m.x102 == 0)

m.c83 = Constraint(expr=-(m.x3 - 250/m.x87)*m.x70 + m.x103 == 0)

m.c84 = Constraint(expr=-(m.x4 - 250/m.x88)*m.x71 + m.x104 == 0)

m.c85 = Constraint(expr=-(m.x5 - 250/m.x89)*m.x72 + m.x105 == 0)

m.c86 = Constraint(expr=-(m.x6 - 250/m.x90)*m.x73 + m.x106 == 0)

m.c87 = Constraint(expr=-(m.x7 - 250/m.x91)*m.x74 + m.x107 == 0)

m.c88 = Constraint(expr=-(m.x8 - 250/m.x92)*m.x75 + m.x108 == 0)

m.c89 = Constraint(expr=-(m.x9 - 250/m.x93)*m.x76 + m.x109 == 0)

m.c90 = Constraint(expr=-(m.x10 - 250/m.x94)*m.x77 + m.x110 == 0)

m.c91 = Constraint(expr=-(m.x11 - 250/m.x95)*m.x78 + m.x111 == 0)

m.c92 = Constraint(expr=-(m.x12 - 250/m.x96)*m.x79 + m.x112 == 0)

m.c93 = Constraint(expr=-(m.x13 - 250/m.x97)*m.x80 + m.x113 == 0)

m.c94 = Constraint(expr=-(m.x14 - 250/m.x98)*m.x81 + m.x114 == 0)

m.c95 = Constraint(expr=-(m.x15 - 250/m.x99)*m.x82 + m.x115 == 0)

m.c96 = Constraint(expr=-(m.x16 - 250/m.x100)*m.x83 + m.x116 == 0)
