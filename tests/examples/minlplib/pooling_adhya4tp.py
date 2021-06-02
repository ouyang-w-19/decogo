#  NLP written by GAMS Convert at 04/21/18 13:53:10
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
#        433      353       80        0
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
m.x10 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,15),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,15),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,15),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,15),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,15),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,15),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,15),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,15),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,15),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x34 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x35 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x36 = Var(within=Reals,bounds=(0,15),initialize=0)
m.x37 = Var(within=Reals,bounds=(0,15),initialize=0)
m.x38 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x39 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x40 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x41 = Var(within=Reals,bounds=(0,15),initialize=0)
m.x42 = Var(within=Reals,bounds=(0,15),initialize=0)
m.x43 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x44 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x45 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x46 = Var(within=Reals,bounds=(0,15),initialize=0)
m.x47 = Var(within=Reals,bounds=(0,15),initialize=0)
m.x48 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x49 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x50 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x51 = Var(within=Reals,bounds=(0,15),initialize=0)
m.x52 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x53 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x54 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x55 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x56 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x57 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x58 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x59 = Var(within=Reals,bounds=(0,85),initialize=0)

m.obj = Objective(expr=   5*m.x12 - 10*m.x13 - 15*m.x14 + 9*m.x15 + 5*m.x16 - 3*m.x17 - 18*m.x18 - 23*m.x19 + m.x20
                        - 3*m.x21 - 6*m.x22 - 21*m.x23 - 26*m.x24 - 2*m.x25 - 6*m.x26 - 5*m.x27 - 20*m.x28 - 25*m.x29
                        - m.x30 - 5*m.x31 - 4*m.x32 - 19*m.x33 - 24*m.x34 - 4*m.x36 - 7*m.x37 - 22*m.x38 - 27*m.x39
                        - 3*m.x40 - 7*m.x41 - 5*m.x42 - 20*m.x43 - 25*m.x44 - m.x45 - 5*m.x46 - 5*m.x47 - 20*m.x48
                        - 25*m.x49 - m.x50 - 5*m.x51, sense=minimize)

m.c2 = Constraint(expr=   m.x12 + m.x13 + m.x14 + m.x15 + m.x16 <= 85)

m.c3 = Constraint(expr=   m.x17 + m.x18 + m.x19 + m.x20 + m.x21 <= 85)

m.c4 = Constraint(expr=   m.x22 + m.x23 + m.x24 + m.x25 + m.x26 <= 85)

m.c5 = Constraint(expr=   m.x27 + m.x28 + m.x29 + m.x30 + m.x31 <= 85)

m.c6 = Constraint(expr=   m.x32 + m.x33 + m.x34 + m.x35 + m.x36 <= 85)

m.c7 = Constraint(expr=   m.x37 + m.x38 + m.x39 + m.x40 + m.x41 <= 85)

m.c8 = Constraint(expr=   m.x42 + m.x43 + m.x44 + m.x45 + m.x46 <= 85)

m.c9 = Constraint(expr=   m.x47 + m.x48 + m.x49 + m.x50 + m.x51 <= 85)

m.c10 = Constraint(expr=   m.x12 + m.x13 + m.x14 + m.x15 + m.x16 + m.x17 + m.x18 + m.x19 + m.x20 + m.x21 + m.x22 + m.x23
                         + m.x24 + m.x25 + m.x26 + m.x27 + m.x28 + m.x29 + m.x30 + m.x31 <= 85)

m.c11 = Constraint(expr=   m.x32 + m.x33 + m.x34 + m.x35 + m.x36 + m.x37 + m.x38 + m.x39 + m.x40 + m.x41 + m.x42 + m.x43
                         + m.x44 + m.x45 + m.x46 + m.x47 + m.x48 + m.x49 + m.x50 + m.x51 <= 85)

m.c12 = Constraint(expr=   m.x12 + m.x17 + m.x22 + m.x27 + m.x32 + m.x37 + m.x42 + m.x47 <= 15)

m.c13 = Constraint(expr=   m.x13 + m.x18 + m.x23 + m.x28 + m.x33 + m.x38 + m.x43 + m.x48 <= 25)

m.c14 = Constraint(expr=   m.x14 + m.x19 + m.x24 + m.x29 + m.x34 + m.x39 + m.x44 + m.x49 <= 10)

m.c15 = Constraint(expr=   m.x15 + m.x20 + m.x25 + m.x30 + m.x35 + m.x40 + m.x45 + m.x50 <= 20)

m.c16 = Constraint(expr=   m.x16 + m.x21 + m.x26 + m.x31 + m.x36 + m.x41 + m.x46 + m.x51 <= 15)

m.c17 = Constraint(expr= - 0.7*m.x12 + 0.2*m.x17 + 0.3*m.x27 + 0.4*m.x32 + 0.3*m.x42 + 0.2*m.x47 <= 0)

m.c18 = Constraint(expr=   0.2*m.x12 + 0.1*m.x17 + 0.2*m.x22 - 0.5*m.x27 + 0.1*m.x32 - 0.6*m.x37 - 0.2*m.x42
                         - 0.0999999999999999*m.x47 <= 0)

m.c19 = Constraint(expr= - 0.0999999999999999*m.x12 + 0.3*m.x17 + 0.3*m.x27 + 0.2*m.x32 + 0.1*m.x42 - 0.2*m.x47 <= 0)

m.c20 = Constraint(expr= - 0.7*m.x12 - 0.0999999999999999*m.x17 - 0.3*m.x22 - 0.4*m.x27 + 0.3*m.x32 + 0.3*m.x37
                         - 0.2*m.x42 - 0.0999999999999999*m.x47 <= 0)

m.c21 = Constraint(expr= - 0.9*m.x13 - 0.2*m.x23 + 0.1*m.x28 + 0.2*m.x33 - 0.2*m.x38 + 0.1*m.x43 <= 0)

m.c22 = Constraint(expr=   0.6*m.x13 + 0.5*m.x18 + 0.6*m.x23 - 0.1*m.x28 + 0.5*m.x33 - 0.2*m.x38 + 0.2*m.x43 + 0.3*m.x48
                         <= 0)

m.c23 = Constraint(expr= - 0.5*m.x13 - 0.1*m.x18 - 0.4*m.x23 - 0.1*m.x28 - 0.2*m.x33 - 0.4*m.x38 - 0.3*m.x43 - 0.6*m.x48
                         <= 0)

m.c24 = Constraint(expr= - 0.4*m.x13 + 0.2*m.x18 - 0.0999999999999999*m.x28 + 0.6*m.x33 + 0.6*m.x38 + 0.1*m.x43
                         + 0.2*m.x48 <= 0)

m.c25 = Constraint(expr= - 0.8*m.x14 + 0.0999999999999999*m.x19 - 0.1*m.x24 + 0.2*m.x29 + 0.3*m.x34 - 0.1*m.x39
                         + 0.2*m.x44 + 0.0999999999999999*m.x49 <= 0)

m.c26 = Constraint(expr=   0.6*m.x14 + 0.5*m.x19 + 0.6*m.x24 - 0.1*m.x29 + 0.5*m.x34 - 0.2*m.x39 + 0.2*m.x44 + 0.3*m.x49
                         <= 0)

m.c27 = Constraint(expr= - 0.6*m.x14 - 0.2*m.x19 - 0.5*m.x24 - 0.2*m.x29 - 0.3*m.x34 - 0.5*m.x39 - 0.4*m.x44 - 0.7*m.x49
                         <= 0)

m.c28 = Constraint(expr= - 0.9*m.x14 - 0.3*m.x19 - 0.5*m.x24 - 0.6*m.x29 + 0.1*m.x34 + 0.1*m.x39 - 0.4*m.x44 - 0.3*m.x49
                         <= 0)

m.c29 = Constraint(expr= - 0.7*m.x15 + 0.2*m.x20 + 0.3*m.x30 + 0.4*m.x35 + 0.3*m.x45 + 0.2*m.x50 <= 0)

m.c30 = Constraint(expr=   0.8*m.x15 + 0.7*m.x20 + 0.8*m.x25 + 0.0999999999999999*m.x30 + 0.7*m.x35 + 0.4*m.x45
                         + 0.5*m.x50 <= 0)

m.c31 = Constraint(expr= - 0.4*m.x15 - 0.3*m.x25 - 0.0999999999999999*m.x35 - 0.3*m.x40 - 0.2*m.x45 - 0.5*m.x50 <= 0)

m.c32 = Constraint(expr= - 0.6*m.x15 - 0.2*m.x25 - 0.3*m.x30 + 0.4*m.x35 + 0.4*m.x40 - 0.1*m.x45 <= 0)

m.c33 = Constraint(expr= - 1.1*m.x16 - 0.2*m.x21 - 0.4*m.x26 - 0.1*m.x31 - 0.4*m.x41 - 0.1*m.x46 - 0.2*m.x51 <= 0)

m.c34 = Constraint(expr= - 0.0999999999999999*m.x21 - 0.7*m.x31 - 0.0999999999999999*m.x36 - 0.8*m.x41 - 0.4*m.x46
                         - 0.3*m.x51 <= 0)

m.c35 = Constraint(expr= - 0.7*m.x16 - 0.3*m.x21 - 0.6*m.x26 - 0.3*m.x31 - 0.4*m.x36 - 0.6*m.x41 - 0.5*m.x46 - 0.8*m.x51
                         <= 0)

m.c36 = Constraint(expr= - 1.5*m.x16 - 0.9*m.x21 - 1.1*m.x26 - 1.2*m.x31 - 0.5*m.x36 - 0.5*m.x41 - m.x46 - 0.9*m.x51
                         <= 0)

m.c37 = Constraint(expr=   m.x2 + m.x3 + m.x4 + m.x5 + m.x6 == 1)

m.c38 = Constraint(expr=   m.x7 + m.x8 + m.x9 + m.x10 + m.x11 == 1)

m.c39 = Constraint(expr=-m.x2*m.x52 + m.x12 == 0)

m.c40 = Constraint(expr=-m.x3*m.x52 + m.x13 == 0)

m.c41 = Constraint(expr=-m.x4*m.x52 + m.x14 == 0)

m.c42 = Constraint(expr=-m.x5*m.x52 + m.x15 == 0)

m.c43 = Constraint(expr=-m.x6*m.x52 + m.x16 == 0)

m.c44 = Constraint(expr=-m.x2*m.x53 + m.x17 == 0)

m.c45 = Constraint(expr=-m.x3*m.x53 + m.x18 == 0)

m.c46 = Constraint(expr=-m.x4*m.x53 + m.x19 == 0)

m.c47 = Constraint(expr=-m.x5*m.x53 + m.x20 == 0)

m.c48 = Constraint(expr=-m.x6*m.x53 + m.x21 == 0)

m.c49 = Constraint(expr=-m.x2*m.x54 + m.x22 == 0)

m.c50 = Constraint(expr=-m.x3*m.x54 + m.x23 == 0)

m.c51 = Constraint(expr=-m.x4*m.x54 + m.x24 == 0)

m.c52 = Constraint(expr=-m.x5*m.x54 + m.x25 == 0)

m.c53 = Constraint(expr=-m.x6*m.x54 + m.x26 == 0)

m.c54 = Constraint(expr=-m.x2*m.x55 + m.x27 == 0)

m.c55 = Constraint(expr=-m.x3*m.x55 + m.x28 == 0)

m.c56 = Constraint(expr=-m.x4*m.x55 + m.x29 == 0)

m.c57 = Constraint(expr=-m.x5*m.x55 + m.x30 == 0)

m.c58 = Constraint(expr=-m.x6*m.x55 + m.x31 == 0)

m.c59 = Constraint(expr=-m.x7*m.x56 + m.x32 == 0)

m.c60 = Constraint(expr=-m.x8*m.x56 + m.x33 == 0)

m.c61 = Constraint(expr=-m.x9*m.x56 + m.x34 == 0)

m.c62 = Constraint(expr=-m.x10*m.x56 + m.x35 == 0)

m.c63 = Constraint(expr=-m.x11*m.x56 + m.x36 == 0)

m.c64 = Constraint(expr=-m.x7*m.x57 + m.x37 == 0)

m.c65 = Constraint(expr=-m.x8*m.x57 + m.x38 == 0)

m.c66 = Constraint(expr=-m.x9*m.x57 + m.x39 == 0)

m.c67 = Constraint(expr=-m.x10*m.x57 + m.x40 == 0)

m.c68 = Constraint(expr=-m.x11*m.x57 + m.x41 == 0)

m.c69 = Constraint(expr=-m.x7*m.x58 + m.x42 == 0)

m.c70 = Constraint(expr=-m.x8*m.x58 + m.x43 == 0)

m.c71 = Constraint(expr=-m.x9*m.x58 + m.x44 == 0)

m.c72 = Constraint(expr=-m.x10*m.x58 + m.x45 == 0)

m.c73 = Constraint(expr=-m.x11*m.x58 + m.x46 == 0)

m.c74 = Constraint(expr=-m.x7*m.x59 + m.x47 == 0)

m.c75 = Constraint(expr=-m.x8*m.x59 + m.x48 == 0)

m.c76 = Constraint(expr=-m.x9*m.x59 + m.x49 == 0)

m.c77 = Constraint(expr=-m.x10*m.x59 + m.x50 == 0)

m.c78 = Constraint(expr=-m.x11*m.x59 + m.x51 == 0)
