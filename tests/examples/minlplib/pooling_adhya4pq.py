#  NLP written by GAMS Convert at 04/21/18 13:53:09
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         78       43        0       35        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         59       59        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        431      351       80        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,15),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,15),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,15),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,15),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,15),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,15),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,15),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,15),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,15),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x34 = Var(within=Reals,bounds=(0,15),initialize=0)
m.x35 = Var(within=Reals,bounds=(0,15),initialize=0)
m.x36 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x37 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x38 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x39 = Var(within=Reals,bounds=(0,15),initialize=0)
m.x40 = Var(within=Reals,bounds=(0,15),initialize=0)
m.x41 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x42 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x43 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x44 = Var(within=Reals,bounds=(0,15),initialize=0)
m.x45 = Var(within=Reals,bounds=(0,15),initialize=0)
m.x46 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x47 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x48 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x49 = Var(within=Reals,bounds=(0,15),initialize=0)
m.x50 = Var(within=Reals,bounds=(0,15),initialize=0)
m.x51 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x52 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x53 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x54 = Var(within=Reals,bounds=(0,15),initialize=0)
m.x55 = Var(within=Reals,bounds=(0,15),initialize=0)
m.x56 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x57 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x58 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x59 = Var(within=Reals,bounds=(0,15),initialize=0)

m.obj = Objective(expr=   5*m.x20 - 10*m.x21 - 15*m.x22 + 9*m.x23 + 5*m.x24 - 3*m.x25 - 18*m.x26 - 23*m.x27 + m.x28
                        - 3*m.x29 - 6*m.x30 - 21*m.x31 - 26*m.x32 - 2*m.x33 - 6*m.x34 - 5*m.x35 - 20*m.x36 - 25*m.x37
                        - m.x38 - 5*m.x39 - 4*m.x40 - 19*m.x41 - 24*m.x42 - 4*m.x44 - 7*m.x45 - 22*m.x46 - 27*m.x47
                        - 3*m.x48 - 7*m.x49 - 5*m.x50 - 20*m.x51 - 25*m.x52 - m.x53 - 5*m.x54 - 5*m.x55 - 20*m.x56
                        - 25*m.x57 - m.x58 - 5*m.x59, sense=minimize)

m.c2 = Constraint(expr=   m.x20 + m.x21 + m.x22 + m.x23 + m.x24 <= 85)

m.c3 = Constraint(expr=   m.x25 + m.x26 + m.x27 + m.x28 + m.x29 <= 85)

m.c4 = Constraint(expr=   m.x30 + m.x31 + m.x32 + m.x33 + m.x34 <= 85)

m.c5 = Constraint(expr=   m.x35 + m.x36 + m.x37 + m.x38 + m.x39 <= 85)

m.c6 = Constraint(expr=   m.x40 + m.x41 + m.x42 + m.x43 + m.x44 <= 85)

m.c7 = Constraint(expr=   m.x45 + m.x46 + m.x47 + m.x48 + m.x49 <= 85)

m.c8 = Constraint(expr=   m.x50 + m.x51 + m.x52 + m.x53 + m.x54 <= 85)

m.c9 = Constraint(expr=   m.x55 + m.x56 + m.x57 + m.x58 + m.x59 <= 85)

m.c10 = Constraint(expr=   m.x20 + m.x21 + m.x22 + m.x23 + m.x24 + m.x25 + m.x26 + m.x27 + m.x28 + m.x29 + m.x30 + m.x31
                         + m.x32 + m.x33 + m.x34 + m.x35 + m.x36 + m.x37 + m.x38 + m.x39 <= 85)

m.c11 = Constraint(expr=   m.x40 + m.x41 + m.x42 + m.x43 + m.x44 + m.x45 + m.x46 + m.x47 + m.x48 + m.x49 + m.x50 + m.x51
                         + m.x52 + m.x53 + m.x54 + m.x55 + m.x56 + m.x57 + m.x58 + m.x59 <= 85)

m.c12 = Constraint(expr=   m.x20 + m.x25 + m.x30 + m.x35 + m.x40 + m.x45 + m.x50 + m.x55 <= 15)

m.c13 = Constraint(expr=   m.x21 + m.x26 + m.x31 + m.x36 + m.x41 + m.x46 + m.x51 + m.x56 <= 25)

m.c14 = Constraint(expr=   m.x22 + m.x27 + m.x32 + m.x37 + m.x42 + m.x47 + m.x52 + m.x57 <= 10)

m.c15 = Constraint(expr=   m.x23 + m.x28 + m.x33 + m.x38 + m.x43 + m.x48 + m.x53 + m.x58 <= 20)

m.c16 = Constraint(expr=   m.x24 + m.x29 + m.x34 + m.x39 + m.x44 + m.x49 + m.x54 + m.x59 <= 15)

m.c17 = Constraint(expr= - 0.7*m.x20 + 0.2*m.x25 + 0.3*m.x35 + 0.4*m.x40 + 0.3*m.x50 + 0.2*m.x55 <= 0)

m.c18 = Constraint(expr=   0.2*m.x20 + 0.1*m.x25 + 0.2*m.x30 - 0.5*m.x35 + 0.1*m.x40 - 0.6*m.x45 - 0.2*m.x50
                         - 0.0999999999999999*m.x55 <= 0)

m.c19 = Constraint(expr= - 0.0999999999999999*m.x20 + 0.3*m.x25 + 0.3*m.x35 + 0.2*m.x40 + 0.1*m.x50 - 0.2*m.x55 <= 0)

m.c20 = Constraint(expr= - 0.7*m.x20 - 0.0999999999999999*m.x25 - 0.3*m.x30 - 0.4*m.x35 + 0.3*m.x40 + 0.3*m.x45
                         - 0.2*m.x50 - 0.0999999999999999*m.x55 <= 0)

m.c21 = Constraint(expr= - 0.9*m.x21 - 0.2*m.x31 + 0.1*m.x36 + 0.2*m.x41 - 0.2*m.x46 + 0.1*m.x51 <= 0)

m.c22 = Constraint(expr=   0.6*m.x21 + 0.5*m.x26 + 0.6*m.x31 - 0.1*m.x36 + 0.5*m.x41 - 0.2*m.x46 + 0.2*m.x51 + 0.3*m.x56
                         <= 0)

m.c23 = Constraint(expr= - 0.5*m.x21 - 0.1*m.x26 - 0.4*m.x31 - 0.1*m.x36 - 0.2*m.x41 - 0.4*m.x46 - 0.3*m.x51 - 0.6*m.x56
                         <= 0)

m.c24 = Constraint(expr= - 0.4*m.x21 + 0.2*m.x26 - 0.0999999999999999*m.x36 + 0.6*m.x41 + 0.6*m.x46 + 0.1*m.x51
                         + 0.2*m.x56 <= 0)

m.c25 = Constraint(expr= - 0.8*m.x22 + 0.0999999999999999*m.x27 - 0.1*m.x32 + 0.2*m.x37 + 0.3*m.x42 - 0.1*m.x47
                         + 0.2*m.x52 + 0.0999999999999999*m.x57 <= 0)

m.c26 = Constraint(expr=   0.6*m.x22 + 0.5*m.x27 + 0.6*m.x32 - 0.1*m.x37 + 0.5*m.x42 - 0.2*m.x47 + 0.2*m.x52 + 0.3*m.x57
                         <= 0)

m.c27 = Constraint(expr= - 0.6*m.x22 - 0.2*m.x27 - 0.5*m.x32 - 0.2*m.x37 - 0.3*m.x42 - 0.5*m.x47 - 0.4*m.x52 - 0.7*m.x57
                         <= 0)

m.c28 = Constraint(expr= - 0.9*m.x22 - 0.3*m.x27 - 0.5*m.x32 - 0.6*m.x37 + 0.1*m.x42 + 0.1*m.x47 - 0.4*m.x52 - 0.3*m.x57
                         <= 0)

m.c29 = Constraint(expr= - 0.7*m.x23 + 0.2*m.x28 + 0.3*m.x38 + 0.4*m.x43 + 0.3*m.x53 + 0.2*m.x58 <= 0)

m.c30 = Constraint(expr=   0.8*m.x23 + 0.7*m.x28 + 0.8*m.x33 + 0.0999999999999999*m.x38 + 0.7*m.x43 + 0.4*m.x53
                         + 0.5*m.x58 <= 0)

m.c31 = Constraint(expr= - 0.4*m.x23 - 0.3*m.x33 - 0.0999999999999999*m.x43 - 0.3*m.x48 - 0.2*m.x53 - 0.5*m.x58 <= 0)

m.c32 = Constraint(expr= - 0.6*m.x23 - 0.2*m.x33 - 0.3*m.x38 + 0.4*m.x43 + 0.4*m.x48 - 0.1*m.x53 <= 0)

m.c33 = Constraint(expr= - 1.1*m.x24 - 0.2*m.x29 - 0.4*m.x34 - 0.1*m.x39 - 0.4*m.x49 - 0.1*m.x54 - 0.2*m.x59 <= 0)

m.c34 = Constraint(expr= - 0.0999999999999999*m.x29 - 0.7*m.x39 - 0.0999999999999999*m.x44 - 0.8*m.x49 - 0.4*m.x54
                         - 0.3*m.x59 <= 0)

m.c35 = Constraint(expr= - 0.7*m.x24 - 0.3*m.x29 - 0.6*m.x34 - 0.3*m.x39 - 0.4*m.x44 - 0.6*m.x49 - 0.5*m.x54 - 0.8*m.x59
                         <= 0)

m.c36 = Constraint(expr= - 1.5*m.x24 - 0.9*m.x29 - 1.1*m.x34 - 1.2*m.x39 - 0.5*m.x44 - 0.5*m.x49 - m.x54 - 0.9*m.x59
                         <= 0)

m.c37 = Constraint(expr=   m.x2 + m.x3 + m.x4 + m.x5 == 1)

m.c38 = Constraint(expr=   m.x6 + m.x7 + m.x8 + m.x9 == 1)

m.c39 = Constraint(expr=-m.x2*m.x10 + m.x20 == 0)

m.c40 = Constraint(expr=-m.x2*m.x11 + m.x21 == 0)

m.c41 = Constraint(expr=-m.x2*m.x12 + m.x22 == 0)

m.c42 = Constraint(expr=-m.x2*m.x13 + m.x23 == 0)

m.c43 = Constraint(expr=-m.x2*m.x14 + m.x24 == 0)

m.c44 = Constraint(expr=-m.x3*m.x10 + m.x25 == 0)

m.c45 = Constraint(expr=-m.x3*m.x11 + m.x26 == 0)

m.c46 = Constraint(expr=-m.x3*m.x12 + m.x27 == 0)

m.c47 = Constraint(expr=-m.x3*m.x13 + m.x28 == 0)

m.c48 = Constraint(expr=-m.x3*m.x14 + m.x29 == 0)

m.c49 = Constraint(expr=-m.x4*m.x10 + m.x30 == 0)

m.c50 = Constraint(expr=-m.x4*m.x11 + m.x31 == 0)

m.c51 = Constraint(expr=-m.x4*m.x12 + m.x32 == 0)

m.c52 = Constraint(expr=-m.x4*m.x13 + m.x33 == 0)

m.c53 = Constraint(expr=-m.x4*m.x14 + m.x34 == 0)

m.c54 = Constraint(expr=-m.x5*m.x10 + m.x35 == 0)

m.c55 = Constraint(expr=-m.x5*m.x11 + m.x36 == 0)

m.c56 = Constraint(expr=-m.x5*m.x12 + m.x37 == 0)

m.c57 = Constraint(expr=-m.x5*m.x13 + m.x38 == 0)

m.c58 = Constraint(expr=-m.x5*m.x14 + m.x39 == 0)

m.c59 = Constraint(expr=-m.x6*m.x15 + m.x40 == 0)

m.c60 = Constraint(expr=-m.x6*m.x16 + m.x41 == 0)

m.c61 = Constraint(expr=-m.x6*m.x17 + m.x42 == 0)

m.c62 = Constraint(expr=-m.x6*m.x18 + m.x43 == 0)

m.c63 = Constraint(expr=-m.x6*m.x19 + m.x44 == 0)

m.c64 = Constraint(expr=-m.x7*m.x15 + m.x45 == 0)

m.c65 = Constraint(expr=-m.x7*m.x16 + m.x46 == 0)

m.c66 = Constraint(expr=-m.x7*m.x17 + m.x47 == 0)

m.c67 = Constraint(expr=-m.x7*m.x18 + m.x48 == 0)

m.c68 = Constraint(expr=-m.x7*m.x19 + m.x49 == 0)

m.c69 = Constraint(expr=-m.x8*m.x15 + m.x50 == 0)

m.c70 = Constraint(expr=-m.x8*m.x16 + m.x51 == 0)

m.c71 = Constraint(expr=-m.x8*m.x17 + m.x52 == 0)

m.c72 = Constraint(expr=-m.x8*m.x18 + m.x53 == 0)

m.c73 = Constraint(expr=-m.x8*m.x19 + m.x54 == 0)

m.c74 = Constraint(expr=-m.x9*m.x15 + m.x55 == 0)

m.c75 = Constraint(expr=-m.x9*m.x16 + m.x56 == 0)

m.c76 = Constraint(expr=-m.x9*m.x17 + m.x57 == 0)

m.c77 = Constraint(expr=-m.x9*m.x18 + m.x58 == 0)

m.c78 = Constraint(expr=-m.x9*m.x19 + m.x59 == 0)
