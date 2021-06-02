#  NLP written by GAMS Convert at 04/21/18 13:53:09
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        325        1        0      324        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         51       51        0        0        0        0        0        0
#  FX      2        2        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1299       49     1250        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,1),initialize=0.14792899408284)
m.x2 = Var(within=Reals,bounds=(0,1),initialize=0.284023668639053)
m.x3 = Var(within=Reals,bounds=(0,1),initialize=0.408284023668639)
m.x4 = Var(within=Reals,bounds=(0,1),initialize=0.520710059171598)
m.x5 = Var(within=Reals,bounds=(0,1),initialize=0.621301775147929)
m.x6 = Var(within=Reals,bounds=(0,1),initialize=0.710059171597633)
m.x7 = Var(within=Reals,bounds=(0,1),initialize=0.78698224852071)
m.x8 = Var(within=Reals,bounds=(0,1),initialize=0.85207100591716)
m.x9 = Var(within=Reals,bounds=(0,1),initialize=0.905325443786982)
m.x10 = Var(within=Reals,bounds=(0,1),initialize=0.946745562130177)
m.x11 = Var(within=Reals,bounds=(0,1),initialize=0.976331360946746)
m.x12 = Var(within=Reals,bounds=(0,1),initialize=0.994082840236686)
m.x13 = Var(within=Reals,bounds=(0,1),initialize=1)
m.x14 = Var(within=Reals,bounds=(0,1),initialize=0.994082840236686)
m.x15 = Var(within=Reals,bounds=(0,1),initialize=0.976331360946746)
m.x16 = Var(within=Reals,bounds=(0,1),initialize=0.946745562130177)
m.x17 = Var(within=Reals,bounds=(0,1),initialize=0.905325443786982)
m.x18 = Var(within=Reals,bounds=(0,1),initialize=0.85207100591716)
m.x19 = Var(within=Reals,bounds=(0,1),initialize=0.78698224852071)
m.x20 = Var(within=Reals,bounds=(0,1),initialize=0.710059171597633)
m.x21 = Var(within=Reals,bounds=(0,1),initialize=0.621301775147929)
m.x22 = Var(within=Reals,bounds=(0,1),initialize=0.520710059171598)
m.x23 = Var(within=Reals,bounds=(0,1),initialize=0.408284023668639)
m.x24 = Var(within=Reals,bounds=(0,1),initialize=0.284023668639053)
m.x25 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,3.14159265358979),initialize=0.125663706143592)
m.x27 = Var(within=Reals,bounds=(0,3.14159265358979),initialize=0.251327412287183)
m.x28 = Var(within=Reals,bounds=(0,3.14159265358979),initialize=0.376991118430775)
m.x29 = Var(within=Reals,bounds=(0,3.14159265358979),initialize=0.502654824574367)
m.x30 = Var(within=Reals,bounds=(0,3.14159265358979),initialize=0.628318530717959)
m.x31 = Var(within=Reals,bounds=(0,3.14159265358979),initialize=0.75398223686155)
m.x32 = Var(within=Reals,bounds=(0,3.14159265358979),initialize=0.879645943005142)
m.x33 = Var(within=Reals,bounds=(0,3.14159265358979),initialize=1.00530964914873)
m.x34 = Var(within=Reals,bounds=(0,3.14159265358979),initialize=1.13097335529233)
m.x35 = Var(within=Reals,bounds=(0,3.14159265358979),initialize=1.25663706143592)
m.x36 = Var(within=Reals,bounds=(0,3.14159265358979),initialize=1.38230076757951)
m.x37 = Var(within=Reals,bounds=(0,3.14159265358979),initialize=1.5079644737231)
m.x38 = Var(within=Reals,bounds=(0,3.14159265358979),initialize=1.63362817986669)
m.x39 = Var(within=Reals,bounds=(0,3.14159265358979),initialize=1.75929188601028)
m.x40 = Var(within=Reals,bounds=(0,3.14159265358979),initialize=1.88495559215388)
m.x41 = Var(within=Reals,bounds=(0,3.14159265358979),initialize=2.01061929829747)
m.x42 = Var(within=Reals,bounds=(0,3.14159265358979),initialize=2.13628300444106)
m.x43 = Var(within=Reals,bounds=(0,3.14159265358979),initialize=2.26194671058465)
m.x44 = Var(within=Reals,bounds=(0,3.14159265358979),initialize=2.38761041672824)
m.x45 = Var(within=Reals,bounds=(0,3.14159265358979),initialize=2.51327412287183)
m.x46 = Var(within=Reals,bounds=(0,3.14159265358979),initialize=2.63893782901543)
m.x47 = Var(within=Reals,bounds=(0,3.14159265358979),initialize=2.76460153515902)
m.x48 = Var(within=Reals,bounds=(0,3.14159265358979),initialize=2.89026524130261)
m.x49 = Var(within=Reals,bounds=(0,3.14159265358979),initialize=3.0159289474462)
m.x50 = Var(within=Reals,bounds=(3.14159265358979,3.14159265358979),initialize=3.14159265358979)

m.obj = Objective(expr=-0.5*(m.x2*m.x1*sin(m.x27 - m.x26) + m.x3*m.x2*sin(m.x28 - m.x27) + m.x4*m.x3*sin(m.x29 - m.x28)
                        + m.x5*m.x4*sin(m.x30 - m.x29) + m.x6*m.x5*sin(m.x31 - m.x30) + m.x7*m.x6*sin(m.x32 - m.x31) + 
                       m.x8*m.x7*sin(m.x33 - m.x32) + m.x9*m.x8*sin(m.x34 - m.x33) + m.x10*m.x9*sin(m.x35 - m.x34) + 
                       m.x11*m.x10*sin(m.x36 - m.x35) + m.x12*m.x11*sin(m.x37 - m.x36) + m.x13*m.x12*sin(m.x38 - m.x37)
                        + m.x14*m.x13*sin(m.x39 - m.x38) + m.x15*m.x14*sin(m.x40 - m.x39) + m.x16*m.x15*sin(m.x41 - 
                       m.x40) + m.x17*m.x16*sin(m.x42 - m.x41) + m.x18*m.x17*sin(m.x43 - m.x42) + m.x19*m.x18*sin(m.x44
                        - m.x43) + m.x20*m.x19*sin(m.x45 - m.x44) + m.x21*m.x20*sin(m.x46 - m.x45) + m.x22*m.x21*sin(
                       m.x47 - m.x46) + m.x23*m.x22*sin(m.x48 - m.x47) + m.x24*m.x23*sin(m.x49 - m.x48) + m.x25*m.x24*
                       sin(m.x50 - m.x49)), sense=minimize)

m.c2 = Constraint(expr=m.x1**2 + m.x2**2 - 2*m.x1*m.x2*cos(m.x27 - m.x26) <= 1)

m.c3 = Constraint(expr=m.x1**2 + m.x3**2 - 2*m.x1*m.x3*cos(m.x28 - m.x26) <= 1)

m.c4 = Constraint(expr=m.x1**2 + m.x4**2 - 2*m.x1*m.x4*cos(m.x29 - m.x26) <= 1)

m.c5 = Constraint(expr=m.x1**2 + m.x5**2 - 2*m.x1*m.x5*cos(m.x30 - m.x26) <= 1)

m.c6 = Constraint(expr=m.x1**2 + m.x6**2 - 2*m.x1*m.x6*cos(m.x31 - m.x26) <= 1)

m.c7 = Constraint(expr=m.x1**2 + m.x7**2 - 2*m.x1*m.x7*cos(m.x32 - m.x26) <= 1)

m.c8 = Constraint(expr=m.x1**2 + m.x8**2 - 2*m.x1*m.x8*cos(m.x33 - m.x26) <= 1)

m.c9 = Constraint(expr=m.x1**2 + m.x9**2 - 2*m.x1*m.x9*cos(m.x34 - m.x26) <= 1)

m.c10 = Constraint(expr=m.x1**2 + m.x10**2 - 2*m.x1*m.x10*cos(m.x35 - m.x26) <= 1)

m.c11 = Constraint(expr=m.x1**2 + m.x11**2 - 2*m.x1*m.x11*cos(m.x36 - m.x26) <= 1)

m.c12 = Constraint(expr=m.x1**2 + m.x12**2 - 2*m.x1*m.x12*cos(m.x37 - m.x26) <= 1)

m.c13 = Constraint(expr=m.x1**2 + m.x13**2 - 2*m.x1*m.x13*cos(m.x38 - m.x26) <= 1)

m.c14 = Constraint(expr=m.x1**2 + m.x14**2 - 2*m.x1*m.x14*cos(m.x39 - m.x26) <= 1)

m.c15 = Constraint(expr=m.x1**2 + m.x15**2 - 2*m.x1*m.x15*cos(m.x40 - m.x26) <= 1)

m.c16 = Constraint(expr=m.x1**2 + m.x16**2 - 2*m.x1*m.x16*cos(m.x41 - m.x26) <= 1)

m.c17 = Constraint(expr=m.x1**2 + m.x17**2 - 2*m.x1*m.x17*cos(m.x42 - m.x26) <= 1)

m.c18 = Constraint(expr=m.x1**2 + m.x18**2 - 2*m.x1*m.x18*cos(m.x43 - m.x26) <= 1)

m.c19 = Constraint(expr=m.x1**2 + m.x19**2 - 2*m.x1*m.x19*cos(m.x44 - m.x26) <= 1)

m.c20 = Constraint(expr=m.x1**2 + m.x20**2 - 2*m.x1*m.x20*cos(m.x45 - m.x26) <= 1)

m.c21 = Constraint(expr=m.x1**2 + m.x21**2 - 2*m.x1*m.x21*cos(m.x46 - m.x26) <= 1)

m.c22 = Constraint(expr=m.x1**2 + m.x22**2 - 2*m.x1*m.x22*cos(m.x47 - m.x26) <= 1)

m.c23 = Constraint(expr=m.x1**2 + m.x23**2 - 2*m.x1*m.x23*cos(m.x48 - m.x26) <= 1)

m.c24 = Constraint(expr=m.x1**2 + m.x24**2 - 2*m.x1*m.x24*cos(m.x49 - m.x26) <= 1)

m.c25 = Constraint(expr=m.x1**2 + m.x25**2 - 2*m.x1*m.x25*cos(m.x50 - m.x26) <= 1)

m.c26 = Constraint(expr=m.x2**2 + m.x3**2 - 2*m.x2*m.x3*cos(m.x28 - m.x27) <= 1)

m.c27 = Constraint(expr=m.x2**2 + m.x4**2 - 2*m.x2*m.x4*cos(m.x29 - m.x27) <= 1)

m.c28 = Constraint(expr=m.x2**2 + m.x5**2 - 2*m.x2*m.x5*cos(m.x30 - m.x27) <= 1)

m.c29 = Constraint(expr=m.x2**2 + m.x6**2 - 2*m.x2*m.x6*cos(m.x31 - m.x27) <= 1)

m.c30 = Constraint(expr=m.x2**2 + m.x7**2 - 2*m.x2*m.x7*cos(m.x32 - m.x27) <= 1)

m.c31 = Constraint(expr=m.x2**2 + m.x8**2 - 2*m.x2*m.x8*cos(m.x33 - m.x27) <= 1)

m.c32 = Constraint(expr=m.x2**2 + m.x9**2 - 2*m.x2*m.x9*cos(m.x34 - m.x27) <= 1)

m.c33 = Constraint(expr=m.x2**2 + m.x10**2 - 2*m.x2*m.x10*cos(m.x35 - m.x27) <= 1)

m.c34 = Constraint(expr=m.x2**2 + m.x11**2 - 2*m.x2*m.x11*cos(m.x36 - m.x27) <= 1)

m.c35 = Constraint(expr=m.x2**2 + m.x12**2 - 2*m.x2*m.x12*cos(m.x37 - m.x27) <= 1)

m.c36 = Constraint(expr=m.x2**2 + m.x13**2 - 2*m.x2*m.x13*cos(m.x38 - m.x27) <= 1)

m.c37 = Constraint(expr=m.x2**2 + m.x14**2 - 2*m.x2*m.x14*cos(m.x39 - m.x27) <= 1)

m.c38 = Constraint(expr=m.x2**2 + m.x15**2 - 2*m.x2*m.x15*cos(m.x40 - m.x27) <= 1)

m.c39 = Constraint(expr=m.x2**2 + m.x16**2 - 2*m.x2*m.x16*cos(m.x41 - m.x27) <= 1)

m.c40 = Constraint(expr=m.x2**2 + m.x17**2 - 2*m.x2*m.x17*cos(m.x42 - m.x27) <= 1)

m.c41 = Constraint(expr=m.x2**2 + m.x18**2 - 2*m.x2*m.x18*cos(m.x43 - m.x27) <= 1)

m.c42 = Constraint(expr=m.x2**2 + m.x19**2 - 2*m.x2*m.x19*cos(m.x44 - m.x27) <= 1)

m.c43 = Constraint(expr=m.x2**2 + m.x20**2 - 2*m.x2*m.x20*cos(m.x45 - m.x27) <= 1)

m.c44 = Constraint(expr=m.x2**2 + m.x21**2 - 2*m.x2*m.x21*cos(m.x46 - m.x27) <= 1)

m.c45 = Constraint(expr=m.x2**2 + m.x22**2 - 2*m.x2*m.x22*cos(m.x47 - m.x27) <= 1)

m.c46 = Constraint(expr=m.x2**2 + m.x23**2 - 2*m.x2*m.x23*cos(m.x48 - m.x27) <= 1)

m.c47 = Constraint(expr=m.x2**2 + m.x24**2 - 2*m.x2*m.x24*cos(m.x49 - m.x27) <= 1)

m.c48 = Constraint(expr=m.x2**2 + m.x25**2 - 2*m.x2*m.x25*cos(m.x50 - m.x27) <= 1)

m.c49 = Constraint(expr=m.x3**2 + m.x4**2 - 2*m.x3*m.x4*cos(m.x29 - m.x28) <= 1)

m.c50 = Constraint(expr=m.x3**2 + m.x5**2 - 2*m.x3*m.x5*cos(m.x30 - m.x28) <= 1)

m.c51 = Constraint(expr=m.x3**2 + m.x6**2 - 2*m.x3*m.x6*cos(m.x31 - m.x28) <= 1)

m.c52 = Constraint(expr=m.x3**2 + m.x7**2 - 2*m.x3*m.x7*cos(m.x32 - m.x28) <= 1)

m.c53 = Constraint(expr=m.x3**2 + m.x8**2 - 2*m.x3*m.x8*cos(m.x33 - m.x28) <= 1)

m.c54 = Constraint(expr=m.x3**2 + m.x9**2 - 2*m.x3*m.x9*cos(m.x34 - m.x28) <= 1)

m.c55 = Constraint(expr=m.x3**2 + m.x10**2 - 2*m.x3*m.x10*cos(m.x35 - m.x28) <= 1)

m.c56 = Constraint(expr=m.x3**2 + m.x11**2 - 2*m.x3*m.x11*cos(m.x36 - m.x28) <= 1)

m.c57 = Constraint(expr=m.x3**2 + m.x12**2 - 2*m.x3*m.x12*cos(m.x37 - m.x28) <= 1)

m.c58 = Constraint(expr=m.x3**2 + m.x13**2 - 2*m.x3*m.x13*cos(m.x38 - m.x28) <= 1)

m.c59 = Constraint(expr=m.x3**2 + m.x14**2 - 2*m.x3*m.x14*cos(m.x39 - m.x28) <= 1)

m.c60 = Constraint(expr=m.x3**2 + m.x15**2 - 2*m.x3*m.x15*cos(m.x40 - m.x28) <= 1)

m.c61 = Constraint(expr=m.x3**2 + m.x16**2 - 2*m.x3*m.x16*cos(m.x41 - m.x28) <= 1)

m.c62 = Constraint(expr=m.x3**2 + m.x17**2 - 2*m.x3*m.x17*cos(m.x42 - m.x28) <= 1)

m.c63 = Constraint(expr=m.x3**2 + m.x18**2 - 2*m.x3*m.x18*cos(m.x43 - m.x28) <= 1)

m.c64 = Constraint(expr=m.x3**2 + m.x19**2 - 2*m.x3*m.x19*cos(m.x44 - m.x28) <= 1)

m.c65 = Constraint(expr=m.x3**2 + m.x20**2 - 2*m.x3*m.x20*cos(m.x45 - m.x28) <= 1)

m.c66 = Constraint(expr=m.x3**2 + m.x21**2 - 2*m.x3*m.x21*cos(m.x46 - m.x28) <= 1)

m.c67 = Constraint(expr=m.x3**2 + m.x22**2 - 2*m.x3*m.x22*cos(m.x47 - m.x28) <= 1)

m.c68 = Constraint(expr=m.x3**2 + m.x23**2 - 2*m.x3*m.x23*cos(m.x48 - m.x28) <= 1)

m.c69 = Constraint(expr=m.x3**2 + m.x24**2 - 2*m.x3*m.x24*cos(m.x49 - m.x28) <= 1)

m.c70 = Constraint(expr=m.x3**2 + m.x25**2 - 2*m.x3*m.x25*cos(m.x50 - m.x28) <= 1)

m.c71 = Constraint(expr=m.x4**2 + m.x5**2 - 2*m.x4*m.x5*cos(m.x30 - m.x29) <= 1)

m.c72 = Constraint(expr=m.x4**2 + m.x6**2 - 2*m.x4*m.x6*cos(m.x31 - m.x29) <= 1)

m.c73 = Constraint(expr=m.x4**2 + m.x7**2 - 2*m.x4*m.x7*cos(m.x32 - m.x29) <= 1)

m.c74 = Constraint(expr=m.x4**2 + m.x8**2 - 2*m.x4*m.x8*cos(m.x33 - m.x29) <= 1)

m.c75 = Constraint(expr=m.x4**2 + m.x9**2 - 2*m.x4*m.x9*cos(m.x34 - m.x29) <= 1)

m.c76 = Constraint(expr=m.x4**2 + m.x10**2 - 2*m.x4*m.x10*cos(m.x35 - m.x29) <= 1)

m.c77 = Constraint(expr=m.x4**2 + m.x11**2 - 2*m.x4*m.x11*cos(m.x36 - m.x29) <= 1)

m.c78 = Constraint(expr=m.x4**2 + m.x12**2 - 2*m.x4*m.x12*cos(m.x37 - m.x29) <= 1)

m.c79 = Constraint(expr=m.x4**2 + m.x13**2 - 2*m.x4*m.x13*cos(m.x38 - m.x29) <= 1)

m.c80 = Constraint(expr=m.x4**2 + m.x14**2 - 2*m.x4*m.x14*cos(m.x39 - m.x29) <= 1)

m.c81 = Constraint(expr=m.x4**2 + m.x15**2 - 2*m.x4*m.x15*cos(m.x40 - m.x29) <= 1)

m.c82 = Constraint(expr=m.x4**2 + m.x16**2 - 2*m.x4*m.x16*cos(m.x41 - m.x29) <= 1)

m.c83 = Constraint(expr=m.x4**2 + m.x17**2 - 2*m.x4*m.x17*cos(m.x42 - m.x29) <= 1)

m.c84 = Constraint(expr=m.x4**2 + m.x18**2 - 2*m.x4*m.x18*cos(m.x43 - m.x29) <= 1)

m.c85 = Constraint(expr=m.x4**2 + m.x19**2 - 2*m.x4*m.x19*cos(m.x44 - m.x29) <= 1)

m.c86 = Constraint(expr=m.x4**2 + m.x20**2 - 2*m.x4*m.x20*cos(m.x45 - m.x29) <= 1)

m.c87 = Constraint(expr=m.x4**2 + m.x21**2 - 2*m.x4*m.x21*cos(m.x46 - m.x29) <= 1)

m.c88 = Constraint(expr=m.x4**2 + m.x22**2 - 2*m.x4*m.x22*cos(m.x47 - m.x29) <= 1)

m.c89 = Constraint(expr=m.x4**2 + m.x23**2 - 2*m.x4*m.x23*cos(m.x48 - m.x29) <= 1)

m.c90 = Constraint(expr=m.x4**2 + m.x24**2 - 2*m.x4*m.x24*cos(m.x49 - m.x29) <= 1)

m.c91 = Constraint(expr=m.x4**2 + m.x25**2 - 2*m.x4*m.x25*cos(m.x50 - m.x29) <= 1)

m.c92 = Constraint(expr=m.x5**2 + m.x6**2 - 2*m.x5*m.x6*cos(m.x31 - m.x30) <= 1)

m.c93 = Constraint(expr=m.x5**2 + m.x7**2 - 2*m.x5*m.x7*cos(m.x32 - m.x30) <= 1)

m.c94 = Constraint(expr=m.x5**2 + m.x8**2 - 2*m.x5*m.x8*cos(m.x33 - m.x30) <= 1)

m.c95 = Constraint(expr=m.x5**2 + m.x9**2 - 2*m.x5*m.x9*cos(m.x34 - m.x30) <= 1)

m.c96 = Constraint(expr=m.x5**2 + m.x10**2 - 2*m.x5*m.x10*cos(m.x35 - m.x30) <= 1)

m.c97 = Constraint(expr=m.x5**2 + m.x11**2 - 2*m.x5*m.x11*cos(m.x36 - m.x30) <= 1)

m.c98 = Constraint(expr=m.x5**2 + m.x12**2 - 2*m.x5*m.x12*cos(m.x37 - m.x30) <= 1)

m.c99 = Constraint(expr=m.x5**2 + m.x13**2 - 2*m.x5*m.x13*cos(m.x38 - m.x30) <= 1)

m.c100 = Constraint(expr=m.x5**2 + m.x14**2 - 2*m.x5*m.x14*cos(m.x39 - m.x30) <= 1)

m.c101 = Constraint(expr=m.x5**2 + m.x15**2 - 2*m.x5*m.x15*cos(m.x40 - m.x30) <= 1)

m.c102 = Constraint(expr=m.x5**2 + m.x16**2 - 2*m.x5*m.x16*cos(m.x41 - m.x30) <= 1)

m.c103 = Constraint(expr=m.x5**2 + m.x17**2 - 2*m.x5*m.x17*cos(m.x42 - m.x30) <= 1)

m.c104 = Constraint(expr=m.x5**2 + m.x18**2 - 2*m.x5*m.x18*cos(m.x43 - m.x30) <= 1)

m.c105 = Constraint(expr=m.x5**2 + m.x19**2 - 2*m.x5*m.x19*cos(m.x44 - m.x30) <= 1)

m.c106 = Constraint(expr=m.x5**2 + m.x20**2 - 2*m.x5*m.x20*cos(m.x45 - m.x30) <= 1)

m.c107 = Constraint(expr=m.x5**2 + m.x21**2 - 2*m.x5*m.x21*cos(m.x46 - m.x30) <= 1)

m.c108 = Constraint(expr=m.x5**2 + m.x22**2 - 2*m.x5*m.x22*cos(m.x47 - m.x30) <= 1)

m.c109 = Constraint(expr=m.x5**2 + m.x23**2 - 2*m.x5*m.x23*cos(m.x48 - m.x30) <= 1)

m.c110 = Constraint(expr=m.x5**2 + m.x24**2 - 2*m.x5*m.x24*cos(m.x49 - m.x30) <= 1)

m.c111 = Constraint(expr=m.x5**2 + m.x25**2 - 2*m.x5*m.x25*cos(m.x50 - m.x30) <= 1)

m.c112 = Constraint(expr=m.x6**2 + m.x7**2 - 2*m.x6*m.x7*cos(m.x32 - m.x31) <= 1)

m.c113 = Constraint(expr=m.x6**2 + m.x8**2 - 2*m.x6*m.x8*cos(m.x33 - m.x31) <= 1)

m.c114 = Constraint(expr=m.x6**2 + m.x9**2 - 2*m.x6*m.x9*cos(m.x34 - m.x31) <= 1)

m.c115 = Constraint(expr=m.x6**2 + m.x10**2 - 2*m.x6*m.x10*cos(m.x35 - m.x31) <= 1)

m.c116 = Constraint(expr=m.x6**2 + m.x11**2 - 2*m.x6*m.x11*cos(m.x36 - m.x31) <= 1)

m.c117 = Constraint(expr=m.x6**2 + m.x12**2 - 2*m.x6*m.x12*cos(m.x37 - m.x31) <= 1)

m.c118 = Constraint(expr=m.x6**2 + m.x13**2 - 2*m.x6*m.x13*cos(m.x38 - m.x31) <= 1)

m.c119 = Constraint(expr=m.x6**2 + m.x14**2 - 2*m.x6*m.x14*cos(m.x39 - m.x31) <= 1)

m.c120 = Constraint(expr=m.x6**2 + m.x15**2 - 2*m.x6*m.x15*cos(m.x40 - m.x31) <= 1)

m.c121 = Constraint(expr=m.x6**2 + m.x16**2 - 2*m.x6*m.x16*cos(m.x41 - m.x31) <= 1)

m.c122 = Constraint(expr=m.x6**2 + m.x17**2 - 2*m.x6*m.x17*cos(m.x42 - m.x31) <= 1)

m.c123 = Constraint(expr=m.x6**2 + m.x18**2 - 2*m.x6*m.x18*cos(m.x43 - m.x31) <= 1)

m.c124 = Constraint(expr=m.x6**2 + m.x19**2 - 2*m.x6*m.x19*cos(m.x44 - m.x31) <= 1)

m.c125 = Constraint(expr=m.x6**2 + m.x20**2 - 2*m.x6*m.x20*cos(m.x45 - m.x31) <= 1)

m.c126 = Constraint(expr=m.x6**2 + m.x21**2 - 2*m.x6*m.x21*cos(m.x46 - m.x31) <= 1)

m.c127 = Constraint(expr=m.x6**2 + m.x22**2 - 2*m.x6*m.x22*cos(m.x47 - m.x31) <= 1)

m.c128 = Constraint(expr=m.x6**2 + m.x23**2 - 2*m.x6*m.x23*cos(m.x48 - m.x31) <= 1)

m.c129 = Constraint(expr=m.x6**2 + m.x24**2 - 2*m.x6*m.x24*cos(m.x49 - m.x31) <= 1)

m.c130 = Constraint(expr=m.x6**2 + m.x25**2 - 2*m.x6*m.x25*cos(m.x50 - m.x31) <= 1)

m.c131 = Constraint(expr=m.x7**2 + m.x8**2 - 2*m.x7*m.x8*cos(m.x33 - m.x32) <= 1)

m.c132 = Constraint(expr=m.x7**2 + m.x9**2 - 2*m.x7*m.x9*cos(m.x34 - m.x32) <= 1)

m.c133 = Constraint(expr=m.x7**2 + m.x10**2 - 2*m.x7*m.x10*cos(m.x35 - m.x32) <= 1)

m.c134 = Constraint(expr=m.x7**2 + m.x11**2 - 2*m.x7*m.x11*cos(m.x36 - m.x32) <= 1)

m.c135 = Constraint(expr=m.x7**2 + m.x12**2 - 2*m.x7*m.x12*cos(m.x37 - m.x32) <= 1)

m.c136 = Constraint(expr=m.x7**2 + m.x13**2 - 2*m.x7*m.x13*cos(m.x38 - m.x32) <= 1)

m.c137 = Constraint(expr=m.x7**2 + m.x14**2 - 2*m.x7*m.x14*cos(m.x39 - m.x32) <= 1)

m.c138 = Constraint(expr=m.x7**2 + m.x15**2 - 2*m.x7*m.x15*cos(m.x40 - m.x32) <= 1)

m.c139 = Constraint(expr=m.x7**2 + m.x16**2 - 2*m.x7*m.x16*cos(m.x41 - m.x32) <= 1)

m.c140 = Constraint(expr=m.x7**2 + m.x17**2 - 2*m.x7*m.x17*cos(m.x42 - m.x32) <= 1)

m.c141 = Constraint(expr=m.x7**2 + m.x18**2 - 2*m.x7*m.x18*cos(m.x43 - m.x32) <= 1)

m.c142 = Constraint(expr=m.x7**2 + m.x19**2 - 2*m.x7*m.x19*cos(m.x44 - m.x32) <= 1)

m.c143 = Constraint(expr=m.x7**2 + m.x20**2 - 2*m.x7*m.x20*cos(m.x45 - m.x32) <= 1)

m.c144 = Constraint(expr=m.x7**2 + m.x21**2 - 2*m.x7*m.x21*cos(m.x46 - m.x32) <= 1)

m.c145 = Constraint(expr=m.x7**2 + m.x22**2 - 2*m.x7*m.x22*cos(m.x47 - m.x32) <= 1)

m.c146 = Constraint(expr=m.x7**2 + m.x23**2 - 2*m.x7*m.x23*cos(m.x48 - m.x32) <= 1)

m.c147 = Constraint(expr=m.x7**2 + m.x24**2 - 2*m.x7*m.x24*cos(m.x49 - m.x32) <= 1)

m.c148 = Constraint(expr=m.x7**2 + m.x25**2 - 2*m.x7*m.x25*cos(m.x50 - m.x32) <= 1)

m.c149 = Constraint(expr=m.x8**2 + m.x9**2 - 2*m.x8*m.x9*cos(m.x34 - m.x33) <= 1)

m.c150 = Constraint(expr=m.x8**2 + m.x10**2 - 2*m.x8*m.x10*cos(m.x35 - m.x33) <= 1)

m.c151 = Constraint(expr=m.x8**2 + m.x11**2 - 2*m.x8*m.x11*cos(m.x36 - m.x33) <= 1)

m.c152 = Constraint(expr=m.x8**2 + m.x12**2 - 2*m.x8*m.x12*cos(m.x37 - m.x33) <= 1)

m.c153 = Constraint(expr=m.x8**2 + m.x13**2 - 2*m.x8*m.x13*cos(m.x38 - m.x33) <= 1)

m.c154 = Constraint(expr=m.x8**2 + m.x14**2 - 2*m.x8*m.x14*cos(m.x39 - m.x33) <= 1)

m.c155 = Constraint(expr=m.x8**2 + m.x15**2 - 2*m.x8*m.x15*cos(m.x40 - m.x33) <= 1)

m.c156 = Constraint(expr=m.x8**2 + m.x16**2 - 2*m.x8*m.x16*cos(m.x41 - m.x33) <= 1)

m.c157 = Constraint(expr=m.x8**2 + m.x17**2 - 2*m.x8*m.x17*cos(m.x42 - m.x33) <= 1)

m.c158 = Constraint(expr=m.x8**2 + m.x18**2 - 2*m.x8*m.x18*cos(m.x43 - m.x33) <= 1)

m.c159 = Constraint(expr=m.x8**2 + m.x19**2 - 2*m.x8*m.x19*cos(m.x44 - m.x33) <= 1)

m.c160 = Constraint(expr=m.x8**2 + m.x20**2 - 2*m.x8*m.x20*cos(m.x45 - m.x33) <= 1)

m.c161 = Constraint(expr=m.x8**2 + m.x21**2 - 2*m.x8*m.x21*cos(m.x46 - m.x33) <= 1)

m.c162 = Constraint(expr=m.x8**2 + m.x22**2 - 2*m.x8*m.x22*cos(m.x47 - m.x33) <= 1)

m.c163 = Constraint(expr=m.x8**2 + m.x23**2 - 2*m.x8*m.x23*cos(m.x48 - m.x33) <= 1)

m.c164 = Constraint(expr=m.x8**2 + m.x24**2 - 2*m.x8*m.x24*cos(m.x49 - m.x33) <= 1)

m.c165 = Constraint(expr=m.x8**2 + m.x25**2 - 2*m.x8*m.x25*cos(m.x50 - m.x33) <= 1)

m.c166 = Constraint(expr=m.x9**2 + m.x10**2 - 2*m.x9*m.x10*cos(m.x35 - m.x34) <= 1)

m.c167 = Constraint(expr=m.x9**2 + m.x11**2 - 2*m.x9*m.x11*cos(m.x36 - m.x34) <= 1)

m.c168 = Constraint(expr=m.x9**2 + m.x12**2 - 2*m.x9*m.x12*cos(m.x37 - m.x34) <= 1)

m.c169 = Constraint(expr=m.x9**2 + m.x13**2 - 2*m.x9*m.x13*cos(m.x38 - m.x34) <= 1)

m.c170 = Constraint(expr=m.x9**2 + m.x14**2 - 2*m.x9*m.x14*cos(m.x39 - m.x34) <= 1)

m.c171 = Constraint(expr=m.x9**2 + m.x15**2 - 2*m.x9*m.x15*cos(m.x40 - m.x34) <= 1)

m.c172 = Constraint(expr=m.x9**2 + m.x16**2 - 2*m.x9*m.x16*cos(m.x41 - m.x34) <= 1)

m.c173 = Constraint(expr=m.x9**2 + m.x17**2 - 2*m.x9*m.x17*cos(m.x42 - m.x34) <= 1)

m.c174 = Constraint(expr=m.x9**2 + m.x18**2 - 2*m.x9*m.x18*cos(m.x43 - m.x34) <= 1)

m.c175 = Constraint(expr=m.x9**2 + m.x19**2 - 2*m.x9*m.x19*cos(m.x44 - m.x34) <= 1)

m.c176 = Constraint(expr=m.x9**2 + m.x20**2 - 2*m.x9*m.x20*cos(m.x45 - m.x34) <= 1)

m.c177 = Constraint(expr=m.x9**2 + m.x21**2 - 2*m.x9*m.x21*cos(m.x46 - m.x34) <= 1)

m.c178 = Constraint(expr=m.x9**2 + m.x22**2 - 2*m.x9*m.x22*cos(m.x47 - m.x34) <= 1)

m.c179 = Constraint(expr=m.x9**2 + m.x23**2 - 2*m.x9*m.x23*cos(m.x48 - m.x34) <= 1)

m.c180 = Constraint(expr=m.x9**2 + m.x24**2 - 2*m.x9*m.x24*cos(m.x49 - m.x34) <= 1)

m.c181 = Constraint(expr=m.x9**2 + m.x25**2 - 2*m.x9*m.x25*cos(m.x50 - m.x34) <= 1)

m.c182 = Constraint(expr=m.x10**2 + m.x11**2 - 2*m.x10*m.x11*cos(m.x36 - m.x35) <= 1)

m.c183 = Constraint(expr=m.x10**2 + m.x12**2 - 2*m.x10*m.x12*cos(m.x37 - m.x35) <= 1)

m.c184 = Constraint(expr=m.x10**2 + m.x13**2 - 2*m.x10*m.x13*cos(m.x38 - m.x35) <= 1)

m.c185 = Constraint(expr=m.x10**2 + m.x14**2 - 2*m.x10*m.x14*cos(m.x39 - m.x35) <= 1)

m.c186 = Constraint(expr=m.x10**2 + m.x15**2 - 2*m.x10*m.x15*cos(m.x40 - m.x35) <= 1)

m.c187 = Constraint(expr=m.x10**2 + m.x16**2 - 2*m.x10*m.x16*cos(m.x41 - m.x35) <= 1)

m.c188 = Constraint(expr=m.x10**2 + m.x17**2 - 2*m.x10*m.x17*cos(m.x42 - m.x35) <= 1)

m.c189 = Constraint(expr=m.x10**2 + m.x18**2 - 2*m.x10*m.x18*cos(m.x43 - m.x35) <= 1)

m.c190 = Constraint(expr=m.x10**2 + m.x19**2 - 2*m.x10*m.x19*cos(m.x44 - m.x35) <= 1)

m.c191 = Constraint(expr=m.x10**2 + m.x20**2 - 2*m.x10*m.x20*cos(m.x45 - m.x35) <= 1)

m.c192 = Constraint(expr=m.x10**2 + m.x21**2 - 2*m.x10*m.x21*cos(m.x46 - m.x35) <= 1)

m.c193 = Constraint(expr=m.x10**2 + m.x22**2 - 2*m.x10*m.x22*cos(m.x47 - m.x35) <= 1)

m.c194 = Constraint(expr=m.x10**2 + m.x23**2 - 2*m.x10*m.x23*cos(m.x48 - m.x35) <= 1)

m.c195 = Constraint(expr=m.x10**2 + m.x24**2 - 2*m.x10*m.x24*cos(m.x49 - m.x35) <= 1)

m.c196 = Constraint(expr=m.x10**2 + m.x25**2 - 2*m.x10*m.x25*cos(m.x50 - m.x35) <= 1)

m.c197 = Constraint(expr=m.x11**2 + m.x12**2 - 2*m.x11*m.x12*cos(m.x37 - m.x36) <= 1)

m.c198 = Constraint(expr=m.x11**2 + m.x13**2 - 2*m.x11*m.x13*cos(m.x38 - m.x36) <= 1)

m.c199 = Constraint(expr=m.x11**2 + m.x14**2 - 2*m.x11*m.x14*cos(m.x39 - m.x36) <= 1)

m.c200 = Constraint(expr=m.x11**2 + m.x15**2 - 2*m.x11*m.x15*cos(m.x40 - m.x36) <= 1)

m.c201 = Constraint(expr=m.x11**2 + m.x16**2 - 2*m.x11*m.x16*cos(m.x41 - m.x36) <= 1)

m.c202 = Constraint(expr=m.x11**2 + m.x17**2 - 2*m.x11*m.x17*cos(m.x42 - m.x36) <= 1)

m.c203 = Constraint(expr=m.x11**2 + m.x18**2 - 2*m.x11*m.x18*cos(m.x43 - m.x36) <= 1)

m.c204 = Constraint(expr=m.x11**2 + m.x19**2 - 2*m.x11*m.x19*cos(m.x44 - m.x36) <= 1)

m.c205 = Constraint(expr=m.x11**2 + m.x20**2 - 2*m.x11*m.x20*cos(m.x45 - m.x36) <= 1)

m.c206 = Constraint(expr=m.x11**2 + m.x21**2 - 2*m.x11*m.x21*cos(m.x46 - m.x36) <= 1)

m.c207 = Constraint(expr=m.x11**2 + m.x22**2 - 2*m.x11*m.x22*cos(m.x47 - m.x36) <= 1)

m.c208 = Constraint(expr=m.x11**2 + m.x23**2 - 2*m.x11*m.x23*cos(m.x48 - m.x36) <= 1)

m.c209 = Constraint(expr=m.x11**2 + m.x24**2 - 2*m.x11*m.x24*cos(m.x49 - m.x36) <= 1)

m.c210 = Constraint(expr=m.x11**2 + m.x25**2 - 2*m.x11*m.x25*cos(m.x50 - m.x36) <= 1)

m.c211 = Constraint(expr=m.x12**2 + m.x13**2 - 2*m.x12*m.x13*cos(m.x38 - m.x37) <= 1)

m.c212 = Constraint(expr=m.x12**2 + m.x14**2 - 2*m.x12*m.x14*cos(m.x39 - m.x37) <= 1)

m.c213 = Constraint(expr=m.x12**2 + m.x15**2 - 2*m.x12*m.x15*cos(m.x40 - m.x37) <= 1)

m.c214 = Constraint(expr=m.x12**2 + m.x16**2 - 2*m.x12*m.x16*cos(m.x41 - m.x37) <= 1)

m.c215 = Constraint(expr=m.x12**2 + m.x17**2 - 2*m.x12*m.x17*cos(m.x42 - m.x37) <= 1)

m.c216 = Constraint(expr=m.x12**2 + m.x18**2 - 2*m.x12*m.x18*cos(m.x43 - m.x37) <= 1)

m.c217 = Constraint(expr=m.x12**2 + m.x19**2 - 2*m.x12*m.x19*cos(m.x44 - m.x37) <= 1)

m.c218 = Constraint(expr=m.x12**2 + m.x20**2 - 2*m.x12*m.x20*cos(m.x45 - m.x37) <= 1)

m.c219 = Constraint(expr=m.x12**2 + m.x21**2 - 2*m.x12*m.x21*cos(m.x46 - m.x37) <= 1)

m.c220 = Constraint(expr=m.x12**2 + m.x22**2 - 2*m.x12*m.x22*cos(m.x47 - m.x37) <= 1)

m.c221 = Constraint(expr=m.x12**2 + m.x23**2 - 2*m.x12*m.x23*cos(m.x48 - m.x37) <= 1)

m.c222 = Constraint(expr=m.x12**2 + m.x24**2 - 2*m.x12*m.x24*cos(m.x49 - m.x37) <= 1)

m.c223 = Constraint(expr=m.x12**2 + m.x25**2 - 2*m.x12*m.x25*cos(m.x50 - m.x37) <= 1)

m.c224 = Constraint(expr=m.x13**2 + m.x14**2 - 2*m.x13*m.x14*cos(m.x39 - m.x38) <= 1)

m.c225 = Constraint(expr=m.x13**2 + m.x15**2 - 2*m.x13*m.x15*cos(m.x40 - m.x38) <= 1)

m.c226 = Constraint(expr=m.x13**2 + m.x16**2 - 2*m.x13*m.x16*cos(m.x41 - m.x38) <= 1)

m.c227 = Constraint(expr=m.x13**2 + m.x17**2 - 2*m.x13*m.x17*cos(m.x42 - m.x38) <= 1)

m.c228 = Constraint(expr=m.x13**2 + m.x18**2 - 2*m.x13*m.x18*cos(m.x43 - m.x38) <= 1)

m.c229 = Constraint(expr=m.x13**2 + m.x19**2 - 2*m.x13*m.x19*cos(m.x44 - m.x38) <= 1)

m.c230 = Constraint(expr=m.x13**2 + m.x20**2 - 2*m.x13*m.x20*cos(m.x45 - m.x38) <= 1)

m.c231 = Constraint(expr=m.x13**2 + m.x21**2 - 2*m.x13*m.x21*cos(m.x46 - m.x38) <= 1)

m.c232 = Constraint(expr=m.x13**2 + m.x22**2 - 2*m.x13*m.x22*cos(m.x47 - m.x38) <= 1)

m.c233 = Constraint(expr=m.x13**2 + m.x23**2 - 2*m.x13*m.x23*cos(m.x48 - m.x38) <= 1)

m.c234 = Constraint(expr=m.x13**2 + m.x24**2 - 2*m.x13*m.x24*cos(m.x49 - m.x38) <= 1)

m.c235 = Constraint(expr=m.x13**2 + m.x25**2 - 2*m.x13*m.x25*cos(m.x50 - m.x38) <= 1)

m.c236 = Constraint(expr=m.x14**2 + m.x15**2 - 2*m.x14*m.x15*cos(m.x40 - m.x39) <= 1)

m.c237 = Constraint(expr=m.x14**2 + m.x16**2 - 2*m.x14*m.x16*cos(m.x41 - m.x39) <= 1)

m.c238 = Constraint(expr=m.x14**2 + m.x17**2 - 2*m.x14*m.x17*cos(m.x42 - m.x39) <= 1)

m.c239 = Constraint(expr=m.x14**2 + m.x18**2 - 2*m.x14*m.x18*cos(m.x43 - m.x39) <= 1)

m.c240 = Constraint(expr=m.x14**2 + m.x19**2 - 2*m.x14*m.x19*cos(m.x44 - m.x39) <= 1)

m.c241 = Constraint(expr=m.x14**2 + m.x20**2 - 2*m.x14*m.x20*cos(m.x45 - m.x39) <= 1)

m.c242 = Constraint(expr=m.x14**2 + m.x21**2 - 2*m.x14*m.x21*cos(m.x46 - m.x39) <= 1)

m.c243 = Constraint(expr=m.x14**2 + m.x22**2 - 2*m.x14*m.x22*cos(m.x47 - m.x39) <= 1)

m.c244 = Constraint(expr=m.x14**2 + m.x23**2 - 2*m.x14*m.x23*cos(m.x48 - m.x39) <= 1)

m.c245 = Constraint(expr=m.x14**2 + m.x24**2 - 2*m.x14*m.x24*cos(m.x49 - m.x39) <= 1)

m.c246 = Constraint(expr=m.x14**2 + m.x25**2 - 2*m.x14*m.x25*cos(m.x50 - m.x39) <= 1)

m.c247 = Constraint(expr=m.x15**2 + m.x16**2 - 2*m.x15*m.x16*cos(m.x41 - m.x40) <= 1)

m.c248 = Constraint(expr=m.x15**2 + m.x17**2 - 2*m.x15*m.x17*cos(m.x42 - m.x40) <= 1)

m.c249 = Constraint(expr=m.x15**2 + m.x18**2 - 2*m.x15*m.x18*cos(m.x43 - m.x40) <= 1)

m.c250 = Constraint(expr=m.x15**2 + m.x19**2 - 2*m.x15*m.x19*cos(m.x44 - m.x40) <= 1)

m.c251 = Constraint(expr=m.x15**2 + m.x20**2 - 2*m.x15*m.x20*cos(m.x45 - m.x40) <= 1)

m.c252 = Constraint(expr=m.x15**2 + m.x21**2 - 2*m.x15*m.x21*cos(m.x46 - m.x40) <= 1)

m.c253 = Constraint(expr=m.x15**2 + m.x22**2 - 2*m.x15*m.x22*cos(m.x47 - m.x40) <= 1)

m.c254 = Constraint(expr=m.x15**2 + m.x23**2 - 2*m.x15*m.x23*cos(m.x48 - m.x40) <= 1)

m.c255 = Constraint(expr=m.x15**2 + m.x24**2 - 2*m.x15*m.x24*cos(m.x49 - m.x40) <= 1)

m.c256 = Constraint(expr=m.x15**2 + m.x25**2 - 2*m.x15*m.x25*cos(m.x50 - m.x40) <= 1)

m.c257 = Constraint(expr=m.x16**2 + m.x17**2 - 2*m.x16*m.x17*cos(m.x42 - m.x41) <= 1)

m.c258 = Constraint(expr=m.x16**2 + m.x18**2 - 2*m.x16*m.x18*cos(m.x43 - m.x41) <= 1)

m.c259 = Constraint(expr=m.x16**2 + m.x19**2 - 2*m.x16*m.x19*cos(m.x44 - m.x41) <= 1)

m.c260 = Constraint(expr=m.x16**2 + m.x20**2 - 2*m.x16*m.x20*cos(m.x45 - m.x41) <= 1)

m.c261 = Constraint(expr=m.x16**2 + m.x21**2 - 2*m.x16*m.x21*cos(m.x46 - m.x41) <= 1)

m.c262 = Constraint(expr=m.x16**2 + m.x22**2 - 2*m.x16*m.x22*cos(m.x47 - m.x41) <= 1)

m.c263 = Constraint(expr=m.x16**2 + m.x23**2 - 2*m.x16*m.x23*cos(m.x48 - m.x41) <= 1)

m.c264 = Constraint(expr=m.x16**2 + m.x24**2 - 2*m.x16*m.x24*cos(m.x49 - m.x41) <= 1)

m.c265 = Constraint(expr=m.x16**2 + m.x25**2 - 2*m.x16*m.x25*cos(m.x50 - m.x41) <= 1)

m.c266 = Constraint(expr=m.x17**2 + m.x18**2 - 2*m.x17*m.x18*cos(m.x43 - m.x42) <= 1)

m.c267 = Constraint(expr=m.x17**2 + m.x19**2 - 2*m.x17*m.x19*cos(m.x44 - m.x42) <= 1)

m.c268 = Constraint(expr=m.x17**2 + m.x20**2 - 2*m.x17*m.x20*cos(m.x45 - m.x42) <= 1)

m.c269 = Constraint(expr=m.x17**2 + m.x21**2 - 2*m.x17*m.x21*cos(m.x46 - m.x42) <= 1)

m.c270 = Constraint(expr=m.x17**2 + m.x22**2 - 2*m.x17*m.x22*cos(m.x47 - m.x42) <= 1)

m.c271 = Constraint(expr=m.x17**2 + m.x23**2 - 2*m.x17*m.x23*cos(m.x48 - m.x42) <= 1)

m.c272 = Constraint(expr=m.x17**2 + m.x24**2 - 2*m.x17*m.x24*cos(m.x49 - m.x42) <= 1)

m.c273 = Constraint(expr=m.x17**2 + m.x25**2 - 2*m.x17*m.x25*cos(m.x50 - m.x42) <= 1)

m.c274 = Constraint(expr=m.x18**2 + m.x19**2 - 2*m.x18*m.x19*cos(m.x44 - m.x43) <= 1)

m.c275 = Constraint(expr=m.x18**2 + m.x20**2 - 2*m.x18*m.x20*cos(m.x45 - m.x43) <= 1)

m.c276 = Constraint(expr=m.x18**2 + m.x21**2 - 2*m.x18*m.x21*cos(m.x46 - m.x43) <= 1)

m.c277 = Constraint(expr=m.x18**2 + m.x22**2 - 2*m.x18*m.x22*cos(m.x47 - m.x43) <= 1)

m.c278 = Constraint(expr=m.x18**2 + m.x23**2 - 2*m.x18*m.x23*cos(m.x48 - m.x43) <= 1)

m.c279 = Constraint(expr=m.x18**2 + m.x24**2 - 2*m.x18*m.x24*cos(m.x49 - m.x43) <= 1)

m.c280 = Constraint(expr=m.x18**2 + m.x25**2 - 2*m.x18*m.x25*cos(m.x50 - m.x43) <= 1)

m.c281 = Constraint(expr=m.x19**2 + m.x20**2 - 2*m.x19*m.x20*cos(m.x45 - m.x44) <= 1)

m.c282 = Constraint(expr=m.x19**2 + m.x21**2 - 2*m.x19*m.x21*cos(m.x46 - m.x44) <= 1)

m.c283 = Constraint(expr=m.x19**2 + m.x22**2 - 2*m.x19*m.x22*cos(m.x47 - m.x44) <= 1)

m.c284 = Constraint(expr=m.x19**2 + m.x23**2 - 2*m.x19*m.x23*cos(m.x48 - m.x44) <= 1)

m.c285 = Constraint(expr=m.x19**2 + m.x24**2 - 2*m.x19*m.x24*cos(m.x49 - m.x44) <= 1)

m.c286 = Constraint(expr=m.x19**2 + m.x25**2 - 2*m.x19*m.x25*cos(m.x50 - m.x44) <= 1)

m.c287 = Constraint(expr=m.x20**2 + m.x21**2 - 2*m.x20*m.x21*cos(m.x46 - m.x45) <= 1)

m.c288 = Constraint(expr=m.x20**2 + m.x22**2 - 2*m.x20*m.x22*cos(m.x47 - m.x45) <= 1)

m.c289 = Constraint(expr=m.x20**2 + m.x23**2 - 2*m.x20*m.x23*cos(m.x48 - m.x45) <= 1)

m.c290 = Constraint(expr=m.x20**2 + m.x24**2 - 2*m.x20*m.x24*cos(m.x49 - m.x45) <= 1)

m.c291 = Constraint(expr=m.x20**2 + m.x25**2 - 2*m.x20*m.x25*cos(m.x50 - m.x45) <= 1)

m.c292 = Constraint(expr=m.x21**2 + m.x22**2 - 2*m.x21*m.x22*cos(m.x47 - m.x46) <= 1)

m.c293 = Constraint(expr=m.x21**2 + m.x23**2 - 2*m.x21*m.x23*cos(m.x48 - m.x46) <= 1)

m.c294 = Constraint(expr=m.x21**2 + m.x24**2 - 2*m.x21*m.x24*cos(m.x49 - m.x46) <= 1)

m.c295 = Constraint(expr=m.x21**2 + m.x25**2 - 2*m.x21*m.x25*cos(m.x50 - m.x46) <= 1)

m.c296 = Constraint(expr=m.x22**2 + m.x23**2 - 2*m.x22*m.x23*cos(m.x48 - m.x47) <= 1)

m.c297 = Constraint(expr=m.x22**2 + m.x24**2 - 2*m.x22*m.x24*cos(m.x49 - m.x47) <= 1)

m.c298 = Constraint(expr=m.x22**2 + m.x25**2 - 2*m.x22*m.x25*cos(m.x50 - m.x47) <= 1)

m.c299 = Constraint(expr=m.x23**2 + m.x24**2 - 2*m.x23*m.x24*cos(m.x49 - m.x48) <= 1)

m.c300 = Constraint(expr=m.x23**2 + m.x25**2 - 2*m.x23*m.x25*cos(m.x50 - m.x48) <= 1)

m.c301 = Constraint(expr=m.x24**2 + m.x25**2 - 2*m.x24*m.x25*cos(m.x50 - m.x49) <= 1)

m.c302 = Constraint(expr=   m.x26 - m.x27 <= 0)

m.c303 = Constraint(expr=   m.x27 - m.x28 <= 0)

m.c304 = Constraint(expr=   m.x28 - m.x29 <= 0)

m.c305 = Constraint(expr=   m.x29 - m.x30 <= 0)

m.c306 = Constraint(expr=   m.x30 - m.x31 <= 0)

m.c307 = Constraint(expr=   m.x31 - m.x32 <= 0)

m.c308 = Constraint(expr=   m.x32 - m.x33 <= 0)

m.c309 = Constraint(expr=   m.x33 - m.x34 <= 0)

m.c310 = Constraint(expr=   m.x34 - m.x35 <= 0)

m.c311 = Constraint(expr=   m.x35 - m.x36 <= 0)

m.c312 = Constraint(expr=   m.x36 - m.x37 <= 0)

m.c313 = Constraint(expr=   m.x37 - m.x38 <= 0)

m.c314 = Constraint(expr=   m.x38 - m.x39 <= 0)

m.c315 = Constraint(expr=   m.x39 - m.x40 <= 0)

m.c316 = Constraint(expr=   m.x40 - m.x41 <= 0)

m.c317 = Constraint(expr=   m.x41 - m.x42 <= 0)

m.c318 = Constraint(expr=   m.x42 - m.x43 <= 0)

m.c319 = Constraint(expr=   m.x43 - m.x44 <= 0)

m.c320 = Constraint(expr=   m.x44 - m.x45 <= 0)

m.c321 = Constraint(expr=   m.x45 - m.x46 <= 0)

m.c322 = Constraint(expr=   m.x46 - m.x47 <= 0)

m.c323 = Constraint(expr=   m.x47 - m.x48 <= 0)

m.c324 = Constraint(expr=   m.x48 - m.x49 <= 0)

m.c325 = Constraint(expr=   m.x49 - m.x50 <= 0)
