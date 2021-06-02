#  NLP written by GAMS Convert at 04/21/18 13:55:19
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         96       51        0       45        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         91       91        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        476      176      300        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x34 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x35 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x36 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x37 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x38 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x39 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x40 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x41 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x42 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x43 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x44 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x45 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x46 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x47 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x48 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x49 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x50 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x51 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x52 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x53 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x54 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x55 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x56 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x57 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x58 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x59 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x60 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x61 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x62 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x63 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x64 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x65 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x66 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x67 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x68 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x69 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x70 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x71 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x72 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x73 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x74 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x75 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x76 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x77 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x78 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x79 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x80 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x81 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x82 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x83 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x84 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x85 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x86 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x87 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x88 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x89 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x90 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x91 = Var(within=Reals,bounds=(0,100000),initialize=0)

m.obj = Objective(expr=   m.x2 + m.x3 + m.x4 + m.x5 + m.x6 + m.x7 + m.x8 + m.x9 + m.x10 + m.x11 + m.x12 + m.x13 + m.x14
                        + m.x15 + m.x16, sense=minimize)

m.c2 = Constraint(expr= - m.x2 - m.x7 - m.x12 + m.x17 - m.x27 - m.x32 - m.x37 - m.x42 - m.x47 == 0)

m.c3 = Constraint(expr= - m.x3 - m.x8 - m.x13 + m.x18 - m.x28 - m.x33 - m.x38 - m.x43 - m.x48 == 0)

m.c4 = Constraint(expr= - m.x4 - m.x9 - m.x14 + m.x19 - m.x29 - m.x34 - m.x39 - m.x44 - m.x49 == 0)

m.c5 = Constraint(expr= - m.x5 - m.x10 - m.x15 + m.x20 - m.x30 - m.x35 - m.x40 - m.x45 - m.x50 == 0)

m.c6 = Constraint(expr= - m.x6 - m.x11 - m.x16 + m.x21 - m.x31 - m.x36 - m.x41 - m.x46 - m.x51 == 0)

m.c7 = Constraint(expr=   m.x17 - m.x22 - m.x27 - m.x28 - m.x29 - m.x30 - m.x31 == 0)

m.c8 = Constraint(expr=   m.x18 - m.x23 - m.x32 - m.x33 - m.x34 - m.x35 - m.x36 == 0)

m.c9 = Constraint(expr=   m.x19 - m.x24 - m.x37 - m.x38 - m.x39 - m.x40 - m.x41 == 0)

m.c10 = Constraint(expr=   m.x20 - m.x25 - m.x42 - m.x43 - m.x44 - m.x45 - m.x46 == 0)

m.c11 = Constraint(expr=   m.x21 - m.x26 - m.x47 - m.x48 - m.x49 - m.x50 - m.x51 == 0)

m.c12 = Constraint(expr=m.x17*m.x52 - (m.x27*m.x72 + m.x32*m.x76 + m.x37*m.x80 + m.x42*m.x84 + m.x47*m.x88) - 5*m.x2
                         == 0)

m.c13 = Constraint(expr=m.x17*m.x53 - (m.x27*m.x73 + m.x32*m.x77 + m.x37*m.x81 + m.x42*m.x85 + m.x47*m.x89) - 2*m.x7
                         - 4*m.x12 == 0)

m.c14 = Constraint(expr=m.x17*m.x54 - (m.x27*m.x74 + m.x32*m.x78 + m.x37*m.x82 + m.x42*m.x86 + m.x47*m.x90) - 3*m.x7
                         == 0)

m.c15 = Constraint(expr=m.x17*m.x55 - (m.x27*m.x75 + m.x32*m.x79 + m.x37*m.x83 + m.x42*m.x87 + m.x47*m.x91) - 2*m.x2
                         - 2*m.x7 - 3*m.x12 == 0)

m.c16 = Constraint(expr=m.x18*m.x56 - (m.x28*m.x72 + m.x33*m.x76 + m.x38*m.x80 + m.x43*m.x84 + m.x48*m.x88) - 5*m.x3
                         == 0)

m.c17 = Constraint(expr=m.x18*m.x57 - (m.x28*m.x73 + m.x33*m.x77 + m.x38*m.x81 + m.x43*m.x85 + m.x48*m.x89) - 2*m.x8
                         - 4*m.x13 == 0)

m.c18 = Constraint(expr=m.x18*m.x58 - (m.x28*m.x74 + m.x33*m.x78 + m.x38*m.x82 + m.x43*m.x86 + m.x48*m.x90) - 3*m.x8
                         == 0)

m.c19 = Constraint(expr=m.x18*m.x59 - (m.x28*m.x75 + m.x33*m.x79 + m.x38*m.x83 + m.x43*m.x87 + m.x48*m.x91) - 2*m.x3
                         - 2*m.x8 - 3*m.x13 == 0)

m.c20 = Constraint(expr=m.x19*m.x60 - (m.x29*m.x72 + m.x34*m.x76 + m.x39*m.x80 + m.x44*m.x84 + m.x49*m.x88) - 5*m.x4
                         == 0)

m.c21 = Constraint(expr=m.x19*m.x61 - (m.x29*m.x73 + m.x34*m.x77 + m.x39*m.x81 + m.x44*m.x85 + m.x49*m.x89) - 2*m.x9
                         - 4*m.x14 == 0)

m.c22 = Constraint(expr=m.x19*m.x62 - (m.x29*m.x74 + m.x34*m.x78 + m.x39*m.x82 + m.x44*m.x86 + m.x49*m.x90) - 3*m.x9
                         == 0)

m.c23 = Constraint(expr=m.x19*m.x63 - (m.x29*m.x75 + m.x34*m.x79 + m.x39*m.x83 + m.x44*m.x87 + m.x49*m.x91) - 2*m.x4
                         - 2*m.x9 - 3*m.x14 == 0)

m.c24 = Constraint(expr=m.x20*m.x64 - (m.x30*m.x72 + m.x35*m.x76 + m.x40*m.x80 + m.x45*m.x84 + m.x50*m.x88) - 5*m.x5
                         == 0)

m.c25 = Constraint(expr=m.x20*m.x65 - (m.x30*m.x73 + m.x35*m.x77 + m.x40*m.x81 + m.x45*m.x85 + m.x50*m.x89) - 2*m.x10
                         - 4*m.x15 == 0)

m.c26 = Constraint(expr=m.x20*m.x66 - (m.x30*m.x74 + m.x35*m.x78 + m.x40*m.x82 + m.x45*m.x86 + m.x50*m.x90) - 3*m.x10
                         == 0)

m.c27 = Constraint(expr=m.x20*m.x67 - (m.x30*m.x75 + m.x35*m.x79 + m.x40*m.x83 + m.x45*m.x87 + m.x50*m.x91) - 2*m.x5
                         - 2*m.x10 - 3*m.x15 == 0)

m.c28 = Constraint(expr=m.x21*m.x68 - (m.x31*m.x72 + m.x36*m.x76 + m.x41*m.x80 + m.x46*m.x84 + m.x51*m.x88) - 5*m.x6
                         == 0)

m.c29 = Constraint(expr=m.x21*m.x69 - (m.x31*m.x73 + m.x36*m.x77 + m.x41*m.x81 + m.x46*m.x85 + m.x51*m.x89) - 2*m.x11
                         - 4*m.x16 == 0)

m.c30 = Constraint(expr=m.x21*m.x70 - (m.x31*m.x74 + m.x36*m.x78 + m.x41*m.x82 + m.x46*m.x86 + m.x51*m.x90) - 3*m.x11
                         == 0)

m.c31 = Constraint(expr=m.x21*m.x71 - (m.x31*m.x75 + m.x36*m.x79 + m.x41*m.x83 + m.x46*m.x87 + m.x51*m.x91) - 2*m.x6
                         - 2*m.x11 - 3*m.x16 == 0)

m.c32 = Constraint(expr=-m.x17*(m.x72 - m.x52) == -1080)

m.c33 = Constraint(expr=-m.x17*(m.x73 - m.x53) == -28296)

m.c34 = Constraint(expr=-m.x17*(m.x74 - m.x54) == -2520)

m.c35 = Constraint(expr=-m.x17*(m.x75 - m.x55) == -2016)

m.c36 = Constraint(expr=-m.x18*(m.x76 - m.x56) == -3400)

m.c37 = Constraint(expr=-m.x18*(m.x77 - m.x57) == -32300)

m.c38 = Constraint(expr=-m.x18*(m.x78 - m.x58) == -4590)

m.c39 = Constraint(expr=-m.x18*(m.x79 - m.x59) == -1122)

m.c40 = Constraint(expr=-m.x19*(m.x80 - m.x60) == -5600)

m.c41 = Constraint(expr=-m.x19*(m.x81 - m.x61) == -1400)

m.c42 = Constraint(expr=-m.x19*(m.x82 - m.x62) == -11200)

m.c43 = Constraint(expr=-m.x19*(m.x83 - m.x63) == -2408)

m.c44 = Constraint(expr=-m.x20*(m.x84 - m.x64) == -3348)

m.c45 = Constraint(expr=-m.x20*(m.x85 - m.x65) == -2108)

m.c46 = Constraint(expr=-m.x20*(m.x86 - m.x66) == -1860)

m.c47 = Constraint(expr=-m.x20*(m.x87 - m.x67) == -1364)

m.c48 = Constraint(expr=-m.x21*(m.x88 - m.x68) == -1500)

m.c49 = Constraint(expr=-m.x21*(m.x89 - m.x69) == -190000)

m.c50 = Constraint(expr=-m.x21*(m.x90 - m.x70) == -1500)

m.c51 = Constraint(expr=-m.x21*(m.x91 - m.x71) == -4425)

m.c52 = Constraint(expr=   m.x52 <= 0)

m.c53 = Constraint(expr=   m.x53 <= 7)

m.c54 = Constraint(expr=   m.x54 <= 0)

m.c55 = Constraint(expr=   m.x55 <= 12)

m.c56 = Constraint(expr=   m.x56 <= 20)

m.c57 = Constraint(expr=   m.x57 <= 300)

m.c58 = Constraint(expr=   m.x58 <= 45)

m.c59 = Constraint(expr=   m.x59 <= 34)

m.c60 = Constraint(expr=   m.x60 <= 120)

m.c61 = Constraint(expr=   m.x61 <= 20)

m.c62 = Constraint(expr=   m.x62 <= 200)

m.c63 = Constraint(expr=   m.x63 <= 56)

m.c64 = Constraint(expr=   m.x64 <= 23)

m.c65 = Constraint(expr=   m.x65 <= 43)

m.c66 = Constraint(expr=   m.x66 <= 15)

m.c67 = Constraint(expr=   m.x67 <= 123)

m.c68 = Constraint(expr=   m.x68 <= 90)

m.c69 = Constraint(expr=   m.x69 <= 400)

m.c70 = Constraint(expr=   m.x70 <= 60)

m.c71 = Constraint(expr=   m.x71 <= 57)

m.c72 = Constraint(expr=   m.x72 <= 15)

m.c73 = Constraint(expr=   m.x73 <= 400)

m.c74 = Constraint(expr=   m.x74 <= 35)

m.c75 = Constraint(expr=   m.x75 <= 40)

m.c76 = Constraint(expr=   m.x76 <= 120)

m.c77 = Constraint(expr=   m.x77 <= 1250)

m.c78 = Constraint(expr=   m.x78 <= 180)

m.c79 = Constraint(expr=   m.x79 <= 67)

m.c80 = Constraint(expr=   m.x80 <= 220)

m.c81 = Constraint(expr=   m.x81 <= 45)

m.c82 = Constraint(expr=   m.x82 <= 400)

m.c83 = Constraint(expr=   m.x83 <= 99)

m.c84 = Constraint(expr=   m.x84 <= 50)

m.c85 = Constraint(expr=   m.x85 <= 60)

m.c86 = Constraint(expr=   m.x86 <= 30)

m.c87 = Constraint(expr=   m.x87 <= 134)

m.c88 = Constraint(expr=   m.x88 <= 150)

m.c89 = Constraint(expr=   m.x89 <= 8000)

m.c90 = Constraint(expr=   m.x90 <= 120)

m.c91 = Constraint(expr=   m.x91 <= 234)

m.c92 = Constraint(expr=   m.x17 <= 72)

m.c93 = Constraint(expr=   m.x18 <= 34)

m.c94 = Constraint(expr=   m.x19 <= 56)

m.c95 = Constraint(expr=   m.x20 <= 124)

m.c96 = Constraint(expr=   m.x21 <= 25)
