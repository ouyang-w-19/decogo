#  NLP written by GAMS Convert at 04/21/18 13:55:19
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         65       33        4       28        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         65       65        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        327      171      156        0
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

m.obj = Objective(expr=   m.x2 + m.x3 + m.x4 + m.x5 + m.x6 + m.x7 + m.x8 + m.x9 + m.x10 + m.x11 + m.x12 + m.x13 + m.x14
                        + m.x15 + m.x16 + m.x17, sense=minimize)

m.c2 = Constraint(expr= - m.x2 - m.x6 - m.x10 - m.x14 + m.x18 - m.x26 - m.x30 - m.x34 - m.x38 == 0)

m.c3 = Constraint(expr= - m.x3 - m.x7 - m.x11 - m.x15 + m.x19 - m.x27 - m.x31 - m.x35 - m.x39 == 0)

m.c4 = Constraint(expr= - m.x4 - m.x8 - m.x12 - m.x16 + m.x20 - m.x28 - m.x32 - m.x36 - m.x40 == 0)

m.c5 = Constraint(expr= - m.x5 - m.x9 - m.x13 - m.x17 - m.x29 - m.x33 - m.x37 - m.x41 == -95)

m.c6 = Constraint(expr=   m.x18 - m.x22 - m.x26 - m.x27 - m.x28 - m.x29 == 0)

m.c7 = Constraint(expr=   m.x19 - m.x23 - m.x30 - m.x31 - m.x32 - m.x33 == 0)

m.c8 = Constraint(expr=   m.x20 - m.x24 - m.x34 - m.x35 - m.x36 - m.x37 == 0)

m.c9 = Constraint(expr= - m.x25 - m.x38 - m.x39 - m.x40 - m.x41 == -50)

m.c10 = Constraint(expr=m.x18*m.x42 - (m.x26*m.x54 + m.x30*m.x58 + m.x34*m.x62) - 2*m.x2 - 3*m.x6 - 4*m.x10 - 623*m.x38
                         == 0)

m.c11 = Constraint(expr=m.x18*m.x43 - (m.x26*m.x55 + m.x30*m.x59 + m.x34*m.x63) - 2*m.x6 - 5*m.x10 - 2*m.x14 - 904*m.x38
                         == 0)

m.c12 = Constraint(expr=m.x18*m.x44 - (m.x26*m.x56 + m.x30*m.x60 + m.x34*m.x64) - 6*m.x2 - 2*m.x10 - m.x14 - 846*m.x38
                         == 0)

m.c13 = Constraint(expr=m.x18*m.x45 - (m.x26*m.x57 + m.x30*m.x61 + m.x34*m.x65) - 5*m.x2 - 3*m.x6 - m.x10 - 3*m.x14
                         - 611*m.x38 == 0)

m.c14 = Constraint(expr=m.x19*m.x46 - (m.x27*m.x54 + m.x31*m.x58 + m.x35*m.x62) - 2*m.x3 - 3*m.x7 - 4*m.x11 - 623*m.x39
                         == 0)

m.c15 = Constraint(expr=m.x19*m.x47 - (m.x27*m.x55 + m.x31*m.x59 + m.x35*m.x63) - 2*m.x7 - 5*m.x11 - 2*m.x15 - 904*m.x39
                         == 0)

m.c16 = Constraint(expr=m.x19*m.x48 - (m.x27*m.x56 + m.x31*m.x60 + m.x35*m.x64) - 6*m.x3 - 2*m.x11 - m.x15 - 846*m.x39
                         == 0)

m.c17 = Constraint(expr=m.x19*m.x49 - (m.x27*m.x57 + m.x31*m.x61 + m.x35*m.x65) - 5*m.x3 - 3*m.x7 - m.x11 - 3*m.x15
                         - 611*m.x39 == 0)

m.c18 = Constraint(expr=m.x20*m.x50 - (m.x28*m.x54 + m.x32*m.x58 + m.x36*m.x62) - 2*m.x4 - 3*m.x8 - 4*m.x12 - 623*m.x40
                         == 0)

m.c19 = Constraint(expr=m.x20*m.x51 - (m.x28*m.x55 + m.x32*m.x59 + m.x36*m.x63) - 2*m.x8 - 5*m.x12 - 2*m.x16 - 904*m.x40
                         == 0)

m.c20 = Constraint(expr=m.x20*m.x52 - (m.x28*m.x56 + m.x32*m.x60 + m.x36*m.x64) - 6*m.x4 - 2*m.x12 - m.x16 - 846*m.x40
                         == 0)

m.c21 = Constraint(expr=m.x20*m.x53 - (m.x28*m.x57 + m.x32*m.x61 + m.x36*m.x65) - 5*m.x4 - 3*m.x8 - m.x12 - 3*m.x16
                         - 611*m.x40 == 0)

m.c22 = Constraint(expr=-m.x18*(m.x54 - m.x42) == -18598)

m.c23 = Constraint(expr=-m.x18*(m.x55 - m.x43) == -3672)

m.c24 = Constraint(expr=-m.x18*(m.x56 - m.x44) == -7582)

m.c25 = Constraint(expr=-m.x18*(m.x57 - m.x45) == -11662)

m.c26 = Constraint(expr=-m.x19*(m.x58 - m.x46) == -1776)

m.c27 = Constraint(expr=-m.x19*(m.x59 - m.x47) == -576)

m.c28 = Constraint(expr=-m.x19*(m.x60 - m.x48) == -4236)

m.c29 = Constraint(expr=-m.x19*(m.x61 - m.x49) == -2724)

m.c30 = Constraint(expr=-m.x20*(m.x62 - m.x50) == -5130)

m.c31 = Constraint(expr=-m.x20*(m.x63 - m.x51) == -14310)

m.c32 = Constraint(expr=-m.x20*(m.x64 - m.x52) == -1035)

m.c33 = Constraint(expr=-m.x20*(m.x65 - m.x53) == -33975)

m.c34 = Constraint(expr=   m.x42 <= 326)

m.c35 = Constraint(expr=   m.x43 <= 842)

m.c36 = Constraint(expr=   m.x44 <= 733)

m.c37 = Constraint(expr=   m.x45 <= 214)

m.c38 = Constraint(expr=   m.x46 <= 751)

m.c39 = Constraint(expr=   m.x47 <= 963)

m.c40 = Constraint(expr=   m.x48 <= 337)

m.c41 = Constraint(expr=   m.x49 <= 762)

m.c42 = Constraint(expr=   m.x50 <= 837)

m.c43 = Constraint(expr=   m.x51 <= 695)

m.c44 = Constraint(expr=   m.x52 <= 991)

m.c45 = Constraint(expr=   m.x53 <= 180)

m.c46 = Constraint(expr=   m.x54 <= 873)

m.c47 = Constraint(expr=   m.x55 <= 950)

m.c48 = Constraint(expr=   m.x56 <= 956)

m.c49 = Constraint(expr=   m.x57 <= 557)

m.c50 = Constraint(expr=   m.x58 <= 899)

m.c51 = Constraint(expr=   m.x59 <= 1011)

m.c52 = Constraint(expr=   m.x60 <= 690)

m.c53 = Constraint(expr=   m.x61 <= 989)

m.c54 = Constraint(expr=   m.x62 <= 951)

m.c55 = Constraint(expr=   m.x63 <= 1013)

m.c56 = Constraint(expr=   m.x64 <= 1014)

m.c57 = Constraint(expr=   m.x65 <= 935)

m.c58 = Constraint(expr=-(m.x29*m.x54 + m.x33*m.x58 + m.x37*m.x62) - 2*m.x5 - 3*m.x9 - 4*m.x13 - 623*m.x41 >= -13015)

m.c59 = Constraint(expr=-(m.x29*m.x55 + m.x33*m.x59 + m.x37*m.x63) - 2*m.x9 - 5*m.x13 - 2*m.x17 - 904*m.x41 >= -69160)

m.c60 = Constraint(expr=-(m.x29*m.x56 + m.x33*m.x60 + m.x37*m.x64) - 6*m.x5 - 2*m.x13 - m.x17 - 846*m.x41 >= -65265)

m.c61 = Constraint(expr=-(m.x29*m.x57 + m.x33*m.x61 + m.x37*m.x65) - 5*m.x5 - 3*m.x9 - m.x13 - 3*m.x17 - 611*m.x41
                         >= -48260)

m.c62 = Constraint(expr=   m.x18 <= 34)

m.c63 = Constraint(expr=   m.x19 <= 12)

m.c64 = Constraint(expr=   m.x20 <= 45)

m.c65 = Constraint(expr=   m.x21 <= 0)
