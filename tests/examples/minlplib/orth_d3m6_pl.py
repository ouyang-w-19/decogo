#  NLP written by GAMS Convert at 04/21/18 13:52:44
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        127       67        1       59        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         42       42        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        590      140      450        0


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x23 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x25 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x26 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x27 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x28 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x29 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x30 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x31 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x32 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x33 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x34 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x35 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x36 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x37 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x38 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x39 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x40 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x41 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x42 = Var(within=Reals,bounds=(-1,1),initialize=0)

m.obj = Objective(expr=m.x1, sense=minimize)

m.c1 = Constraint(expr=   m.x1 >= 0)

m.c2 = Constraint(expr=-m.x3*m.x4 + m.x2 == 0)

m.c3 = Constraint(expr=-m.x3*m.x6 + m.x5 == 0)

m.c4 = Constraint(expr=-m.x3*m.x8 + m.x7 == 0)

m.c5 = Constraint(expr=-m.x3*m.x10 + m.x9 == 0)

m.c6 = Constraint(expr=-m.x3*m.x12 + m.x11 == 0)

m.c7 = Constraint(expr=-m.x4*m.x6 + m.x13 == 0)

m.c8 = Constraint(expr=-m.x4*m.x8 + m.x14 == 0)

m.c9 = Constraint(expr=-m.x4*m.x10 + m.x15 == 0)

m.c10 = Constraint(expr=-m.x4*m.x12 + m.x16 == 0)

m.c11 = Constraint(expr=-m.x6*m.x8 + m.x17 == 0)

m.c12 = Constraint(expr=-m.x6*m.x10 + m.x18 == 0)

m.c13 = Constraint(expr=-m.x6*m.x12 + m.x19 == 0)

m.c14 = Constraint(expr=-m.x8*m.x10 + m.x20 == 0)

m.c15 = Constraint(expr=-m.x8*m.x12 + m.x21 == 0)

m.c16 = Constraint(expr=-m.x10*m.x12 + m.x22 == 0)

m.c17 = Constraint(expr=   m.x3 + m.x4 + m.x6 + m.x8 + m.x10 + m.x12 == 3)

m.c18 = Constraint(expr=   m.x23 - m.x24 <= 0)

m.c19 = Constraint(expr= - m.x24 + m.x25 <= 0)

m.c20 = Constraint(expr= - m.x24 + m.x26 <= 0)

m.c21 = Constraint(expr= - m.x24 + m.x27 <= 0)

m.c22 = Constraint(expr= - m.x24 + m.x28 <= 0)

m.c23 = Constraint(expr= - m.x24 + m.x29 <= 0)

m.c24 = Constraint(expr= - m.x24 + m.x30 <= 0)

m.c25 = Constraint(expr= - m.x24 + m.x31 <= 0)

m.c26 = Constraint(expr= - m.x24 + m.x32 <= 0)

m.c27 = Constraint(expr= - m.x24 + m.x33 <= 0)

m.c28 = Constraint(expr= - m.x24 + m.x34 <= 0)

m.c29 = Constraint(expr= - m.x24 + m.x35 <= 0)

m.c30 = Constraint(expr= - m.x24 + m.x36 <= 0)

m.c31 = Constraint(expr= - m.x24 + m.x37 <= 0)

m.c32 = Constraint(expr= - m.x24 + m.x38 <= 0)

m.c33 = Constraint(expr= - m.x24 + m.x39 <= 0)

m.c34 = Constraint(expr= - m.x24 + m.x40 <= 0)

m.c35 = Constraint(expr= - m.x24 + m.x41 <= 0)

m.c36 = Constraint(expr= - m.x24 + m.x42 <= 0)

m.c37 = Constraint(expr=m.x23**2*m.x13 + m.x25**2*m.x14 + m.x26**2*m.x15 + m.x27**2*m.x16 + m.x28**2*m.x17 + m.x29**2*
                        m.x18 + m.x30**2*m.x19 + m.x31**2*m.x20 + m.x32**2*m.x21 + m.x33**2*m.x22 == 1)

m.c38 = Constraint(expr=m.x23**2*m.x5 + m.x25**2*m.x7 + m.x26**2*m.x9 + m.x27**2*m.x11 + m.x34**2*m.x17 + m.x35**2*m.x18
                         + m.x36**2*m.x19 + m.x37**2*m.x20 + m.x38**2*m.x21 + m.x39**2*m.x22 == 1)

m.c39 = Constraint(expr=m.x23**2*m.x2 + m.x28**2*m.x7 + m.x29**2*m.x9 + m.x30**2*m.x11 + m.x34**2*m.x14 + m.x35**2*m.x15
                         + m.x36**2*m.x16 + m.x40**2*m.x20 + m.x41**2*m.x21 + m.x42**2*m.x22 == 1)

m.c40 = Constraint(expr=m.x25**2*m.x2 + m.x28**2*m.x5 + m.x31**2*m.x9 + m.x32**2*m.x11 + m.x34**2*m.x13 + m.x37**2*m.x15
                         + m.x38**2*m.x16 + m.x40**2*m.x18 + m.x41**2*m.x19 + m.x24**2*m.x22 == 1)

m.c41 = Constraint(expr=m.x26**2*m.x2 + m.x29**2*m.x5 + m.x31**2*m.x7 + m.x33**2*m.x11 + m.x35**2*m.x13 + m.x37**2*m.x14
                         + m.x39**2*m.x16 + m.x40**2*m.x17 + m.x42**2*m.x19 + m.x24**2*m.x21 == 1)

m.c42 = Constraint(expr=m.x27**2*m.x2 + m.x30**2*m.x5 + m.x32**2*m.x7 + m.x33**2*m.x9 + m.x36**2*m.x13 + m.x38**2*m.x14
                         + m.x39**2*m.x15 + m.x41**2*m.x17 + m.x42**2*m.x18 + m.x24**2*m.x20 == 1)

m.c43 = Constraint(expr=m.x23*m.x31 - m.x25*m.x29 + m.x26*m.x28 == 0)

m.c44 = Constraint(expr=m.x23*m.x37 - m.x25*m.x35 + m.x26*m.x34 == 0)

m.c45 = Constraint(expr=m.x23*m.x32 - m.x25*m.x30 + m.x27*m.x28 == 0)

m.c46 = Constraint(expr=m.x23*m.x38 - m.x25*m.x36 + m.x27*m.x34 == 0)

m.c47 = Constraint(expr=m.x23*m.x33 - m.x26*m.x30 + m.x27*m.x29 == 0)

m.c48 = Constraint(expr=m.x23*m.x39 - m.x26*m.x36 + m.x27*m.x35 == 0)

m.c49 = Constraint(expr=m.x23*m.x40 - m.x28*m.x35 + m.x29*m.x34 == 0)

m.c50 = Constraint(expr=m.x23*m.x41 - m.x28*m.x36 + m.x30*m.x34 == 0)

m.c51 = Constraint(expr=m.x23*m.x42 - m.x29*m.x36 + m.x30*m.x35 == 0)

m.c52 = Constraint(expr=m.x25*m.x33 - m.x26*m.x32 + m.x27*m.x31 == 0)

m.c53 = Constraint(expr=m.x25*m.x39 - m.x26*m.x38 + m.x27*m.x37 == 0)

m.c54 = Constraint(expr=m.x25*m.x40 - m.x28*m.x37 + m.x31*m.x34 == 0)

m.c55 = Constraint(expr=m.x25*m.x41 - m.x28*m.x38 + m.x32*m.x34 == 0)

m.c56 = Constraint(expr=m.x24*m.x25 - m.x31*m.x38 + m.x32*m.x37 == 0)

m.c57 = Constraint(expr=m.x26*m.x40 - m.x29*m.x37 + m.x31*m.x35 == 0)

m.c58 = Constraint(expr=m.x26*m.x42 - m.x29*m.x39 + m.x33*m.x35 == 0)

m.c59 = Constraint(expr=m.x24*m.x26 - m.x31*m.x39 + m.x33*m.x37 == 0)

m.c60 = Constraint(expr=m.x27*m.x41 - m.x30*m.x38 + m.x32*m.x36 == 0)

m.c61 = Constraint(expr=m.x27*m.x42 - m.x30*m.x39 + m.x33*m.x36 == 0)

m.c62 = Constraint(expr=m.x24*m.x27 - m.x32*m.x39 + m.x33*m.x38 == 0)

m.c63 = Constraint(expr=m.x28*m.x33 - m.x29*m.x32 + m.x30*m.x31 == 0)

m.c64 = Constraint(expr=m.x28*m.x42 - m.x29*m.x41 + m.x30*m.x40 == 0)

m.c65 = Constraint(expr=m.x24*m.x28 - m.x31*m.x41 + m.x32*m.x40 == 0)

m.c66 = Constraint(expr=m.x24*m.x29 - m.x31*m.x42 + m.x33*m.x40 == 0)

m.c67 = Constraint(expr=m.x24*m.x30 - m.x32*m.x42 + m.x33*m.x41 == 0)

m.c68 = Constraint(expr=m.x34*m.x39 - m.x35*m.x38 + m.x36*m.x37 == 0)

m.c69 = Constraint(expr=m.x34*m.x42 - m.x35*m.x41 + m.x36*m.x40 == 0)

m.c70 = Constraint(expr=m.x24*m.x34 - m.x37*m.x41 + m.x38*m.x40 == 0)

m.c71 = Constraint(expr=m.x24*m.x35 - m.x37*m.x42 + m.x39*m.x40 == 0)

m.c72 = Constraint(expr=m.x24*m.x36 - m.x38*m.x42 + m.x39*m.x41 == 0)

m.c73 = Constraint(expr=m.x23*m.x24 - m.x25*m.x42 + m.x26*m.x41 - m.x27*m.x40 == 0)

m.c74 = Constraint(expr=m.x23*m.x24 - m.x25*m.x42 + m.x28*m.x39 - m.x33*m.x34 == 0)

m.c75 = Constraint(expr=m.x23*m.x24 + m.x26*m.x41 - m.x29*m.x38 + m.x32*m.x35 == 0)

m.c76 = Constraint(expr=m.x23*m.x24 - m.x27*m.x40 + m.x30*m.x37 - m.x31*m.x36 == 0)

m.c77 = Constraint(expr=m.x23*m.x24 + m.x28*m.x39 - m.x29*m.x38 + m.x30*m.x37 == 0)

m.c78 = Constraint(expr=m.x23*m.x24 - m.x31*m.x36 + m.x32*m.x35 - m.x33*m.x34 == 0)

m.c79 = Constraint(expr=m.x25*m.x42 - m.x26*m.x41 + m.x30*m.x37 - m.x31*m.x36 == 0)

m.c80 = Constraint(expr=m.x25*m.x42 + m.x27*m.x40 - m.x29*m.x38 + m.x32*m.x35 == 0)

m.c81 = Constraint(expr=m.x25*m.x42 - m.x28*m.x39 - m.x31*m.x36 + m.x32*m.x35 == 0)

m.c82 = Constraint(expr=m.x25*m.x42 - m.x29*m.x38 + m.x30*m.x37 + m.x33*m.x34 == 0)

m.c83 = Constraint(expr=m.x26*m.x41 - m.x27*m.x40 - m.x28*m.x39 + m.x33*m.x34 == 0)

m.c84 = Constraint(expr=m.x26*m.x41 - m.x28*m.x39 - m.x30*m.x37 + m.x32*m.x35 == 0)

m.c85 = Constraint(expr=m.x26*m.x41 - m.x29*m.x38 + m.x31*m.x36 + m.x33*m.x34 == 0)

m.c86 = Constraint(expr=m.x27*m.x40 + m.x28*m.x39 - m.x29*m.x38 + m.x31*m.x36 == 0)

m.c87 = Constraint(expr=m.x27*m.x40 - m.x30*m.x37 + m.x32*m.x35 - m.x33*m.x34 == 0)

m.c88 = Constraint(expr= - m.x1 + m.x23 <= 0)

m.c89 = Constraint(expr= - m.x1 - m.x23 <= 0)

m.c90 = Constraint(expr= - m.x1 + m.x25 <= 0)

m.c91 = Constraint(expr= - m.x1 - m.x25 <= 0)

m.c92 = Constraint(expr= - m.x1 + m.x26 <= 0)

m.c93 = Constraint(expr= - m.x1 - m.x26 <= 0)

m.c94 = Constraint(expr= - m.x1 + m.x27 <= 0)

m.c95 = Constraint(expr= - m.x1 - m.x27 <= 0)

m.c96 = Constraint(expr= - m.x1 + m.x28 <= 0)

m.c97 = Constraint(expr= - m.x1 - m.x28 <= 0)

m.c98 = Constraint(expr= - m.x1 + m.x29 <= 0)

m.c99 = Constraint(expr= - m.x1 - m.x29 <= 0)

m.c100 = Constraint(expr= - m.x1 + m.x30 <= 0)

m.c101 = Constraint(expr= - m.x1 - m.x30 <= 0)

m.c102 = Constraint(expr= - m.x1 + m.x31 <= 0)

m.c103 = Constraint(expr= - m.x1 - m.x31 <= 0)

m.c104 = Constraint(expr= - m.x1 + m.x32 <= 0)

m.c105 = Constraint(expr= - m.x1 - m.x32 <= 0)

m.c106 = Constraint(expr= - m.x1 + m.x33 <= 0)

m.c107 = Constraint(expr= - m.x1 - m.x33 <= 0)

m.c108 = Constraint(expr= - m.x1 + m.x34 <= 0)

m.c109 = Constraint(expr= - m.x1 - m.x34 <= 0)

m.c110 = Constraint(expr= - m.x1 + m.x35 <= 0)

m.c111 = Constraint(expr= - m.x1 - m.x35 <= 0)

m.c112 = Constraint(expr= - m.x1 + m.x36 <= 0)

m.c113 = Constraint(expr= - m.x1 - m.x36 <= 0)

m.c114 = Constraint(expr= - m.x1 + m.x37 <= 0)

m.c115 = Constraint(expr= - m.x1 - m.x37 <= 0)

m.c116 = Constraint(expr= - m.x1 + m.x38 <= 0)

m.c117 = Constraint(expr= - m.x1 - m.x38 <= 0)

m.c118 = Constraint(expr= - m.x1 + m.x39 <= 0)

m.c119 = Constraint(expr= - m.x1 - m.x39 <= 0)

m.c120 = Constraint(expr= - m.x1 + m.x40 <= 0)

m.c121 = Constraint(expr= - m.x1 - m.x40 <= 0)

m.c122 = Constraint(expr= - m.x1 + m.x41 <= 0)

m.c123 = Constraint(expr= - m.x1 - m.x41 <= 0)

m.c124 = Constraint(expr= - m.x1 + m.x42 <= 0)

m.c125 = Constraint(expr= - m.x1 - m.x42 <= 0)

m.c126 = Constraint(expr= - m.x1 + m.x24 <= 0)

m.c127 = Constraint(expr= - m.x1 - m.x24 <= 0)
