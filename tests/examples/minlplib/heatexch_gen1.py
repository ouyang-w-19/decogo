#  MINLP written by GAMS Convert at 04/21/18 13:52:23
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        121       77       12       32        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        113      101       12        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        401      277      124        0
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
m.x13 = Var(within=Reals,bounds=(370,650),initialize=650)
m.x14 = Var(within=Reals,bounds=(370,650),initialize=650)
m.x15 = Var(within=Reals,bounds=(370,650),initialize=650)
m.x16 = Var(within=Reals,bounds=(370,590),initialize=590)
m.x17 = Var(within=Reals,bounds=(370,590),initialize=590)
m.x18 = Var(within=Reals,bounds=(370,590),initialize=590)
m.x19 = Var(within=Reals,bounds=(410,650),initialize=410)
m.x20 = Var(within=Reals,bounds=(410,650),initialize=410)
m.x21 = Var(within=Reals,bounds=(410,650),initialize=410)
m.x22 = Var(within=Reals,bounds=(350,500),initialize=350)
m.x23 = Var(within=Reals,bounds=(350,500),initialize=350)
m.x24 = Var(within=Reals,bounds=(350,500),initialize=350)
m.x25 = Var(within=Reals,bounds=(0,None),initialize=2800)
m.x26 = Var(within=Reals,bounds=(0,None),initialize=2800)
m.x27 = Var(within=Reals,bounds=(0,None),initialize=1950)
m.x28 = Var(within=Reals,bounds=(0,None),initialize=1950)
m.x29 = Var(within=Reals,bounds=(0,None),initialize=3600)
m.x30 = Var(within=Reals,bounds=(0,None),initialize=3600)
m.x31 = Var(within=Reals,bounds=(0,None),initialize=1950)
m.x32 = Var(within=Reals,bounds=(0,None),initialize=1950)
m.x33 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x34 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x35 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x36 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x37 = Var(within=Reals,bounds=(10,None),initialize=240)
m.x38 = Var(within=Reals,bounds=(10,None),initialize=240)
m.x39 = Var(within=Reals,bounds=(10,None),initialize=240)
m.x40 = Var(within=Reals,bounds=(10,None),initialize=300)
m.x41 = Var(within=Reals,bounds=(10,None),initialize=300)
m.x42 = Var(within=Reals,bounds=(10,None),initialize=300)
m.x43 = Var(within=Reals,bounds=(10,None),initialize=180)
m.x44 = Var(within=Reals,bounds=(10,None),initialize=180)
m.x45 = Var(within=Reals,bounds=(10,None),initialize=180)
m.x46 = Var(within=Reals,bounds=(10,None),initialize=240)
m.x47 = Var(within=Reals,bounds=(10,None),initialize=240)
m.x48 = Var(within=Reals,bounds=(10,None),initialize=240)
m.x49 = Var(within=Reals,bounds=(10,None),initialize=330)
m.x50 = Var(within=Reals,bounds=(10,None),initialize=270)
m.x51 = Var(within=Reals,bounds=(10,None),initialize=270)
m.x52 = Var(within=Reals,bounds=(10,None),initialize=330)
m.x53 = Var(within=Reals,bounds=(0,10),initialize=10)
m.x54 = Var(within=Reals,bounds=(0,10),initialize=10)
m.x55 = Var(within=Reals,bounds=(0,10),initialize=10)
m.x56 = Var(within=Reals,bounds=(0,10),initialize=10)
m.x57 = Var(within=Reals,bounds=(0,20),initialize=20)
m.x58 = Var(within=Reals,bounds=(0,20),initialize=20)
m.x59 = Var(within=Reals,bounds=(0,20),initialize=20)
m.x60 = Var(within=Reals,bounds=(0,20),initialize=20)
m.x61 = Var(within=Reals,bounds=(0,15),initialize=15)
m.x62 = Var(within=Reals,bounds=(0,15),initialize=15)
m.x63 = Var(within=Reals,bounds=(0,13),initialize=13)
m.x64 = Var(within=Reals,bounds=(0,13),initialize=13)
m.x65 = Var(within=Reals,bounds=(0,15),initialize=15)
m.x66 = Var(within=Reals,bounds=(0,15),initialize=15)
m.x67 = Var(within=Reals,bounds=(0,13),initialize=13)
m.x68 = Var(within=Reals,bounds=(0,13),initialize=13)
m.x69 = Var(within=Reals,bounds=(370,650),initialize=650)
m.x70 = Var(within=Reals,bounds=(370,650),initialize=650)
m.x71 = Var(within=Reals,bounds=(370,650),initialize=650)
m.x72 = Var(within=Reals,bounds=(370,650),initialize=650)
m.x73 = Var(within=Reals,bounds=(370,590),initialize=590)
m.x74 = Var(within=Reals,bounds=(370,590),initialize=590)
m.x75 = Var(within=Reals,bounds=(370,590),initialize=590)
m.x76 = Var(within=Reals,bounds=(370,590),initialize=590)
m.x77 = Var(within=Reals,bounds=(410,650),initialize=410)
m.x78 = Var(within=Reals,bounds=(410,650),initialize=410)
m.x79 = Var(within=Reals,bounds=(350,500),initialize=350)
m.x80 = Var(within=Reals,bounds=(350,500),initialize=350)
m.x81 = Var(within=Reals,bounds=(410,650),initialize=410)
m.x82 = Var(within=Reals,bounds=(410,650),initialize=410)
m.x83 = Var(within=Reals,bounds=(350,500),initialize=350)
m.x84 = Var(within=Reals,bounds=(350,500),initialize=350)
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

m.obj = Objective(expr=   5500*m.b1 + 5500*m.b2 + 5500*m.b3 + 5500*m.b4 + 5500*m.b5 + 5500*m.b6 + 5500*m.b7 + 5500*m.b8
                        + 5500*m.b9 + 5500*m.b10 + 5500*m.b11 + 5500*m.b12 + 15*m.x33 + 15*m.x34 + 80*m.x35 + 80*m.x36
                        + 150*m.x97 + 150*m.x98 + 150*m.x99 + 150*m.x100 + 150*m.x101 + 150*m.x102 + 150*m.x103
                        + 150*m.x104 + 150*m.x105 + 150*m.x106 + 150*m.x107 + 150*m.x108 + 150*m.x109 + 150*m.x110
                        + 150*m.x111 + 150*m.x112, sense=minimize)

m.c1 = Constraint(expr=   10*m.x13 - 10*m.x14 - m.x25 - m.x27 == 0)

m.c2 = Constraint(expr=   10*m.x14 - 10*m.x15 - m.x26 - m.x28 == 0)

m.c3 = Constraint(expr=   20*m.x16 - 20*m.x17 - m.x29 - m.x31 == 0)

m.c4 = Constraint(expr=   20*m.x17 - 20*m.x18 - m.x30 - m.x32 == 0)

m.c5 = Constraint(expr=   15*m.x19 - 15*m.x20 - m.x25 - m.x29 == 0)

m.c6 = Constraint(expr=   15*m.x20 - 15*m.x21 - m.x26 - m.x30 == 0)

m.c7 = Constraint(expr=   13*m.x22 - 13*m.x23 - m.x27 - m.x31 == 0)

m.c8 = Constraint(expr=   13*m.x23 - 13*m.x24 - m.x28 - m.x32 == 0)

m.c9 = Constraint(expr=   10*m.x15 - m.x33 == 3700)

m.c10 = Constraint(expr=   20*m.x18 - m.x34 == 7400)

m.c11 = Constraint(expr= - m.x25 - m.x26 - m.x27 - m.x28 - m.x33 == -2800)

m.c12 = Constraint(expr= - m.x29 - m.x30 - m.x31 - m.x32 - m.x34 == -4400)

m.c13 = Constraint(expr= - 15*m.x19 - m.x35 == -9750)

m.c14 = Constraint(expr= - 13*m.x22 - m.x36 == -6500)

m.c15 = Constraint(expr= - m.x25 - m.x26 - m.x29 - m.x30 - m.x35 == -3600)

m.c16 = Constraint(expr= - m.x27 - m.x28 - m.x31 - m.x32 - m.x36 == -1950)

m.c17 = Constraint(expr=   m.x13 - m.x14 >= 0)

m.c18 = Constraint(expr=   m.x14 - m.x15 >= 0)

m.c19 = Constraint(expr=   m.x16 - m.x17 >= 0)

m.c20 = Constraint(expr=   m.x17 - m.x18 >= 0)

m.c21 = Constraint(expr=   m.x19 - m.x20 >= 0)

m.c22 = Constraint(expr=   m.x20 - m.x21 >= 0)

m.c23 = Constraint(expr=   m.x22 - m.x23 >= 0)

m.c24 = Constraint(expr=   m.x23 - m.x24 >= 0)

m.c25 = Constraint(expr=   m.x15 >= 370)

m.c26 = Constraint(expr=   m.x18 >= 370)

m.c27 = Constraint(expr= - m.x19 >= -650)

m.c28 = Constraint(expr= - m.x22 >= -500)

m.c29 = Constraint(expr= - m.x13 == -650)

m.c30 = Constraint(expr= - m.x16 == -590)

m.c31 = Constraint(expr= - m.x21 == -410)

m.c32 = Constraint(expr= - m.x24 == -350)

m.c33 = Constraint(expr= - m.x53 - m.x55 == -10)

m.c34 = Constraint(expr= - m.x54 - m.x56 == -10)

m.c35 = Constraint(expr= - m.x57 - m.x59 == -20)

m.c36 = Constraint(expr= - m.x58 - m.x60 == -20)

m.c37 = Constraint(expr= - m.x61 - m.x65 == -15)

m.c38 = Constraint(expr= - m.x62 - m.x66 == -15)

m.c39 = Constraint(expr= - m.x63 - m.x67 == -13)

m.c40 = Constraint(expr= - m.x64 - m.x68 == -13)

m.c41 = Constraint(expr=-m.x53*(m.x13 - m.x69) + m.x25 == 0)

m.c42 = Constraint(expr=-m.x54*(m.x14 - m.x70) + m.x26 == 0)

m.c43 = Constraint(expr=-m.x55*(m.x13 - m.x71) + m.x27 == 0)

m.c44 = Constraint(expr=-m.x56*(m.x14 - m.x72) + m.x28 == 0)

m.c45 = Constraint(expr=-m.x57*(m.x16 - m.x73) + m.x29 == 0)

m.c46 = Constraint(expr=-m.x58*(m.x17 - m.x74) + m.x30 == 0)

m.c47 = Constraint(expr=-m.x59*(m.x16 - m.x75) + m.x31 == 0)

m.c48 = Constraint(expr=-m.x60*(m.x17 - m.x76) + m.x32 == 0)

m.c49 = Constraint(expr=-m.x61*(m.x77 - m.x20) + m.x25 == 0)

m.c50 = Constraint(expr=-m.x62*(m.x78 - m.x21) + m.x26 == 0)

m.c51 = Constraint(expr=-m.x63*(m.x79 - m.x23) + m.x27 == 0)

m.c52 = Constraint(expr=-m.x64*(m.x80 - m.x24) + m.x28 == 0)

m.c53 = Constraint(expr=-m.x65*(m.x81 - m.x20) + m.x29 == 0)

m.c54 = Constraint(expr=-m.x66*(m.x82 - m.x21) + m.x30 == 0)

m.c55 = Constraint(expr=-m.x67*(m.x83 - m.x23) + m.x31 == 0)

m.c56 = Constraint(expr=-m.x68*(m.x84 - m.x24) + m.x32 == 0)

m.c57 = Constraint(expr=-(m.x53*m.x69 + m.x55*m.x71) + 10*m.x14 == 0)

m.c58 = Constraint(expr=-(m.x54*m.x70 + m.x56*m.x72) + 10*m.x15 == 0)

m.c59 = Constraint(expr=-(m.x57*m.x73 + m.x59*m.x75) + 20*m.x17 == 0)

m.c60 = Constraint(expr=-(m.x58*m.x74 + m.x60*m.x76) + 20*m.x18 == 0)

m.c61 = Constraint(expr=-(m.x61*m.x77 + m.x65*m.x81) + 15*m.x19 == 0)

m.c62 = Constraint(expr=-(m.x62*m.x78 + m.x66*m.x82) + 15*m.x20 == 0)

m.c63 = Constraint(expr=-(m.x63*m.x79 + m.x67*m.x83) + 13*m.x22 == 0)

m.c64 = Constraint(expr=-(m.x64*m.x80 + m.x68*m.x84) + 13*m.x23 == 0)

m.c65 = Constraint(expr=-(m.x37 - m.x38)/log(m.x37/(1e-6 + m.x38)) + m.x85 == 0)

m.c66 = Constraint(expr=-(m.x38 - m.x39)/log(m.x38/(1e-6 + m.x39)) + m.x86 == 0)

m.c67 = Constraint(expr=-(m.x40 - m.x41)/log(m.x40/(1e-6 + m.x41)) + m.x87 == 0)

m.c68 = Constraint(expr=-(m.x41 - m.x42)/log(m.x41/(1e-6 + m.x42)) + m.x88 == 0)

m.c69 = Constraint(expr=-(m.x43 - m.x44)/log(m.x43/(1e-6 + m.x44)) + m.x89 == 0)

m.c70 = Constraint(expr=-(m.x44 - m.x45)/log(m.x44/(1e-6 + m.x45)) + m.x90 == 0)

m.c71 = Constraint(expr=-(m.x46 - m.x47)/log(m.x46/(1e-6 + m.x47)) + m.x91 == 0)

m.c72 = Constraint(expr=-(m.x47 - m.x48)/log(m.x47/(1e-6 + m.x48)) + m.x92 == 0)

m.c73 = Constraint(expr=-2*m.x25/(0.01 + m.x85) + m.x97 == 0)

m.c74 = Constraint(expr=-2*m.x26/(0.01 + m.x86) + m.x98 == 0)

m.c75 = Constraint(expr=-2*m.x27/(0.01 + m.x87) + m.x100 == 0)

m.c76 = Constraint(expr=-2*m.x28/(0.01 + m.x88) + m.x101 == 0)

m.c77 = Constraint(expr=-2*m.x29/(0.01 + m.x89) + m.x103 == 0)

m.c78 = Constraint(expr=-2*m.x30/(0.01 + m.x90) + m.x104 == 0)

m.c79 = Constraint(expr=-2*m.x31/(0.01 + m.x91) + m.x106 == 0)

m.c80 = Constraint(expr=-2*m.x32/(0.01 + m.x92) + m.x107 == 0)

m.c81 = Constraint(expr=-(-70 + m.x49)/log(0.0142857140816327*m.x49) + m.x93 == 0)

m.c82 = Constraint(expr=-(-70 + m.x50)/log(0.0142857140816327*m.x50) + m.x94 == 0)

m.c83 = Constraint(expr=-(-30 + m.x51)/log(0.0333333322222223*m.x51) + m.x95 == 0)

m.c84 = Constraint(expr=-(-180 + m.x52)/log(0.00555555552469136*m.x52) + m.x96 == 0)

m.c85 = Constraint(expr=-2*m.x33/(0.01 + m.x93) + m.x109 == 0)

m.c86 = Constraint(expr=-2*m.x34/(0.01 + m.x94) + m.x110 == 0)

m.c87 = Constraint(expr=-1.2*m.x35/(0.01 + m.x95) + m.x111 == 0)

m.c88 = Constraint(expr=-1.2*m.x36/(0.01 + m.x96) + m.x112 == 0)

m.c89 = Constraint(expr= - 2800*m.b1 + m.x25 <= 0)

m.c90 = Constraint(expr= - 2800*m.b2 + m.x26 <= 0)

m.c91 = Constraint(expr= - 1950*m.b3 + m.x27 <= 0)

m.c92 = Constraint(expr= - 1950*m.b4 + m.x28 <= 0)

m.c93 = Constraint(expr= - 3600*m.b5 + m.x29 <= 0)

m.c94 = Constraint(expr= - 3600*m.b6 + m.x30 <= 0)

m.c95 = Constraint(expr= - 1950*m.b7 + m.x31 <= 0)

m.c96 = Constraint(expr= - 1950*m.b8 + m.x32 <= 0)

m.c97 = Constraint(expr= - 3600*m.b11 + m.x35 <= 0)

m.c98 = Constraint(expr= - 1950*m.b12 + m.x36 <= 0)

m.c99 = Constraint(expr= - 2800*m.b9 + m.x33 <= 0)

m.c100 = Constraint(expr= - 4400*m.b10 + m.x34 <= 0)

m.c101 = Constraint(expr=   280*m.b1 - m.x13 + m.x19 + m.x37 <= 280)

m.c102 = Constraint(expr=   280*m.b2 - m.x14 + m.x20 + m.x38 <= 280)

m.c103 = Constraint(expr=   130*m.b3 - m.x13 + m.x22 + m.x40 <= 130)

m.c104 = Constraint(expr=   130*m.b4 - m.x14 + m.x23 + m.x41 <= 130)

m.c105 = Constraint(expr=   280*m.b5 - m.x16 + m.x19 + m.x43 <= 280)

m.c106 = Constraint(expr=   280*m.b6 - m.x17 + m.x20 + m.x44 <= 280)

m.c107 = Constraint(expr=   130*m.b7 - m.x16 + m.x22 + m.x46 <= 130)

m.c108 = Constraint(expr=   130*m.b8 - m.x17 + m.x23 + m.x47 <= 130)

m.c109 = Constraint(expr=   280*m.b1 - m.x14 + m.x20 + m.x38 <= 280)

m.c110 = Constraint(expr=   280*m.b2 - m.x15 + m.x21 + m.x39 <= 280)

m.c111 = Constraint(expr=   130*m.b3 - m.x14 + m.x23 + m.x41 <= 130)

m.c112 = Constraint(expr=   130*m.b4 - m.x15 + m.x24 + m.x42 <= 130)

m.c113 = Constraint(expr=   280*m.b5 - m.x17 + m.x20 + m.x44 <= 280)

m.c114 = Constraint(expr=   280*m.b6 - m.x18 + m.x21 + m.x45 <= 280)

m.c115 = Constraint(expr=   130*m.b7 - m.x17 + m.x23 + m.x47 <= 130)

m.c116 = Constraint(expr=   130*m.b8 - m.x18 + m.x24 + m.x48 <= 130)

m.c117 = Constraint(expr= - m.x15 + m.x49 <= -320)

m.c118 = Constraint(expr= - m.x18 + m.x50 <= -320)

m.c119 = Constraint(expr=   m.x19 + m.x51 <= 680)

m.c120 = Constraint(expr=   m.x22 + m.x52 <= 680)
