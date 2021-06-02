#  NLP written by GAMS Convert at 04/21/18 13:52:44
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         86       42        0       44        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         42       42        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        384      114      270        0


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,1),initialize=0)
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
m.x23 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x28 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,1),initialize=0)
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

m.c1 = Constraint(expr=-m.x2*m.x3*m.x4 + m.x5 == 0)

m.c2 = Constraint(expr=-m.x2*m.x3*m.x6 + m.x7 == 0)

m.c3 = Constraint(expr=-m.x2*m.x3*m.x8 + m.x9 == 0)

m.c4 = Constraint(expr=-m.x2*m.x3*m.x10 + m.x11 == 0)

m.c5 = Constraint(expr=-m.x2*m.x4*m.x6 + m.x12 == 0)

m.c6 = Constraint(expr=-m.x2*m.x4*m.x8 + m.x13 == 0)

m.c7 = Constraint(expr=-m.x2*m.x4*m.x10 + m.x14 == 0)

m.c8 = Constraint(expr=-m.x2*m.x6*m.x8 + m.x15 == 0)

m.c9 = Constraint(expr=-m.x2*m.x6*m.x10 + m.x16 == 0)

m.c10 = Constraint(expr=-m.x2*m.x8*m.x10 + m.x17 == 0)

m.c11 = Constraint(expr=-m.x3*m.x4*m.x6 + m.x18 == 0)

m.c12 = Constraint(expr=-m.x3*m.x4*m.x8 + m.x19 == 0)

m.c13 = Constraint(expr=-m.x3*m.x4*m.x10 + m.x20 == 0)

m.c14 = Constraint(expr=-m.x3*m.x6*m.x8 + m.x21 == 0)

m.c15 = Constraint(expr=-m.x3*m.x6*m.x10 + m.x22 == 0)

m.c16 = Constraint(expr=-m.x3*m.x8*m.x10 + m.x23 == 0)

m.c17 = Constraint(expr=-m.x4*m.x6*m.x8 + m.x24 == 0)

m.c18 = Constraint(expr=-m.x4*m.x6*m.x10 + m.x25 == 0)

m.c19 = Constraint(expr=-m.x4*m.x8*m.x10 + m.x26 == 0)

m.c20 = Constraint(expr=-m.x6*m.x8*m.x10 + m.x27 == 0)

m.c21 = Constraint(expr=   m.x2 + m.x3 + m.x4 + m.x6 + m.x8 + m.x10 == 4)

m.c22 = Constraint(expr=   m.x28 - m.x29 <= 0)

m.c23 = Constraint(expr= - m.x29 + m.x30 <= 0)

m.c24 = Constraint(expr= - m.x29 + m.x31 <= 0)

m.c25 = Constraint(expr= - m.x29 + m.x32 <= 0)

m.c26 = Constraint(expr= - m.x29 + m.x33 <= 0)

m.c27 = Constraint(expr= - m.x29 + m.x34 <= 0)

m.c28 = Constraint(expr= - m.x29 + m.x35 <= 0)

m.c29 = Constraint(expr= - m.x29 + m.x36 <= 0)

m.c30 = Constraint(expr= - m.x29 + m.x37 <= 0)

m.c31 = Constraint(expr= - m.x29 + m.x38 <= 0)

m.c32 = Constraint(expr= - m.x29 + m.x39 <= 0)

m.c33 = Constraint(expr= - m.x29 + m.x40 <= 0)

m.c34 = Constraint(expr= - m.x29 + m.x41 <= 0)

m.c35 = Constraint(expr= - m.x29 + m.x42 <= 0)

m.c36 = Constraint(expr=m.x28**2*m.x18 + m.x30**2*m.x19 + m.x31**2*m.x20 + m.x32**2*m.x21 + m.x33**2*m.x22 + m.x34**2*
                        m.x23 + m.x35**2*m.x24 + m.x36**2*m.x25 + m.x37**2*m.x26 + m.x38**2*m.x27 == 1)

m.c37 = Constraint(expr=m.x28**2*m.x12 + m.x30**2*m.x13 + m.x31**2*m.x14 + m.x32**2*m.x15 + m.x33**2*m.x16 + m.x34**2*
                        m.x17 + m.x39**2*m.x24 + m.x40**2*m.x25 + m.x41**2*m.x26 + m.x42**2*m.x27 == 1)

m.c38 = Constraint(expr=m.x28**2*m.x7 + m.x30**2*m.x9 + m.x31**2*m.x11 + m.x35**2*m.x15 + m.x36**2*m.x16 + m.x37**2*
                        m.x17 + m.x39**2*m.x21 + m.x40**2*m.x22 + m.x41**2*m.x23 + m.x29**2*m.x27 == 1)

m.c39 = Constraint(expr=m.x28**2*m.x5 + m.x32**2*m.x9 + m.x33**2*m.x11 + m.x35**2*m.x13 + m.x36**2*m.x14 + m.x38**2*
                        m.x17 + m.x39**2*m.x19 + m.x40**2*m.x20 + m.x42**2*m.x23 + m.x29**2*m.x26 == 1)

m.c40 = Constraint(expr=m.x30**2*m.x5 + m.x32**2*m.x7 + m.x34**2*m.x11 + m.x35**2*m.x12 + m.x37**2*m.x14 + m.x38**2*
                        m.x16 + m.x39**2*m.x18 + m.x41**2*m.x20 + m.x42**2*m.x22 + m.x29**2*m.x25 == 1)

m.c41 = Constraint(expr=m.x31**2*m.x5 + m.x33**2*m.x7 + m.x34**2*m.x9 + m.x36**2*m.x12 + m.x37**2*m.x13 + m.x38**2*m.x15
                         + m.x40**2*m.x18 + m.x41**2*m.x19 + m.x42**2*m.x21 + m.x29**2*m.x24 == 1)

m.c42 = Constraint(expr=m.x28*m.x34 - m.x30*m.x33 + m.x31*m.x32 == 0)

m.c43 = Constraint(expr=m.x28*m.x37 - m.x30*m.x36 + m.x31*m.x35 == 0)

m.c44 = Constraint(expr=m.x28*m.x41 - m.x30*m.x40 + m.x31*m.x39 == 0)

m.c45 = Constraint(expr=m.x28*m.x38 - m.x32*m.x36 + m.x33*m.x35 == 0)

m.c46 = Constraint(expr=m.x28*m.x42 - m.x32*m.x40 + m.x33*m.x39 == 0)

m.c47 = Constraint(expr=m.x28*m.x29 - m.x35*m.x40 + m.x36*m.x39 == 0)

m.c48 = Constraint(expr=m.x30*m.x38 - m.x32*m.x37 + m.x34*m.x35 == 0)

m.c49 = Constraint(expr=m.x30*m.x42 - m.x32*m.x41 + m.x34*m.x39 == 0)

m.c50 = Constraint(expr=m.x29*m.x30 - m.x35*m.x41 + m.x37*m.x39 == 0)

m.c51 = Constraint(expr=m.x31*m.x38 - m.x33*m.x37 + m.x34*m.x36 == 0)

m.c52 = Constraint(expr=m.x31*m.x42 - m.x33*m.x41 + m.x34*m.x40 == 0)

m.c53 = Constraint(expr=m.x29*m.x31 - m.x36*m.x41 + m.x37*m.x40 == 0)

m.c54 = Constraint(expr=m.x29*m.x32 - m.x35*m.x42 + m.x38*m.x39 == 0)

m.c55 = Constraint(expr=m.x29*m.x33 - m.x36*m.x42 + m.x38*m.x40 == 0)

m.c56 = Constraint(expr=m.x29*m.x34 - m.x37*m.x42 + m.x38*m.x41 == 0)

m.c57 = Constraint(expr= - m.x1 - m.x28 <= 0)

m.c58 = Constraint(expr= - m.x1 + m.x28 <= 0)

m.c59 = Constraint(expr= - m.x1 - m.x30 <= 0)

m.c60 = Constraint(expr= - m.x1 + m.x30 <= 0)

m.c61 = Constraint(expr= - m.x1 - m.x31 <= 0)

m.c62 = Constraint(expr= - m.x1 + m.x31 <= 0)

m.c63 = Constraint(expr= - m.x1 - m.x32 <= 0)

m.c64 = Constraint(expr= - m.x1 + m.x32 <= 0)

m.c65 = Constraint(expr= - m.x1 - m.x33 <= 0)

m.c66 = Constraint(expr= - m.x1 + m.x33 <= 0)

m.c67 = Constraint(expr= - m.x1 - m.x34 <= 0)

m.c68 = Constraint(expr= - m.x1 + m.x34 <= 0)

m.c69 = Constraint(expr= - m.x1 - m.x35 <= 0)

m.c70 = Constraint(expr= - m.x1 + m.x35 <= 0)

m.c71 = Constraint(expr= - m.x1 - m.x36 <= 0)

m.c72 = Constraint(expr= - m.x1 + m.x36 <= 0)

m.c73 = Constraint(expr= - m.x1 - m.x37 <= 0)

m.c74 = Constraint(expr= - m.x1 + m.x37 <= 0)

m.c75 = Constraint(expr= - m.x1 - m.x38 <= 0)

m.c76 = Constraint(expr= - m.x1 + m.x38 <= 0)

m.c77 = Constraint(expr= - m.x1 - m.x39 <= 0)

m.c78 = Constraint(expr= - m.x1 + m.x39 <= 0)

m.c79 = Constraint(expr= - m.x1 - m.x40 <= 0)

m.c80 = Constraint(expr= - m.x1 + m.x40 <= 0)

m.c81 = Constraint(expr= - m.x1 - m.x41 <= 0)

m.c82 = Constraint(expr= - m.x1 + m.x41 <= 0)

m.c83 = Constraint(expr= - m.x1 - m.x42 <= 0)

m.c84 = Constraint(expr= - m.x1 + m.x42 <= 0)

m.c85 = Constraint(expr= - m.x1 - m.x29 <= 0)

m.c86 = Constraint(expr= - m.x1 + m.x29 <= 0)
