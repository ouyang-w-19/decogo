#  NLP written by GAMS Convert at 04/21/18 13:53:09
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         75       36        0       39        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         53       53        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        410      346       64        0
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
m.x10 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x34 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x35 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x36 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x37 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x38 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x39 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x40 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x41 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x42 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x43 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x44 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x45 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x46 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x47 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x48 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x49 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x50 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x51 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x52 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x53 = Var(within=Reals,bounds=(0,10),initialize=0)

m.obj = Objective(expr= - 9*m.x22 - 18*m.x23 - 8*m.x24 - 3*m.x25 - 13*m.x26 - 22*m.x27 - 12*m.x28 - 7*m.x29 - 14*m.x30
                        - 23*m.x31 - 13*m.x32 - 8*m.x33 - 6*m.x34 - 15*m.x35 - 5*m.x36 - 11*m.x38 - 20*m.x39 - 10*m.x40
                        - 5*m.x41 - 11*m.x42 - 20*m.x43 - 10*m.x44 - 5*m.x45 - 7*m.x46 - 16*m.x47 - 6*m.x48 - m.x49
                        - 5*m.x50 - 14*m.x51 - 4*m.x52 + m.x53, sense=minimize)

m.c2 = Constraint(expr=   m.x22 + m.x23 + m.x24 + m.x25 <= 75)

m.c3 = Constraint(expr=   m.x26 + m.x27 + m.x28 + m.x29 <= 75)

m.c4 = Constraint(expr=   m.x30 + m.x31 + m.x32 + m.x33 <= 75)

m.c5 = Constraint(expr=   m.x34 + m.x35 + m.x36 + m.x37 <= 75)

m.c6 = Constraint(expr=   m.x38 + m.x39 + m.x40 + m.x41 <= 75)

m.c7 = Constraint(expr=   m.x42 + m.x43 + m.x44 + m.x45 <= 75)

m.c8 = Constraint(expr=   m.x46 + m.x47 + m.x48 + m.x49 <= 75)

m.c9 = Constraint(expr=   m.x50 + m.x51 + m.x52 + m.x53 <= 75)

m.c10 = Constraint(expr=   m.x22 + m.x23 + m.x24 + m.x25 + m.x26 + m.x27 + m.x28 + m.x29 <= 75)

m.c11 = Constraint(expr=   m.x30 + m.x31 + m.x32 + m.x33 + m.x34 + m.x35 + m.x36 + m.x37 + m.x38 + m.x39 + m.x40 + m.x41
                         <= 75)

m.c12 = Constraint(expr=   m.x42 + m.x43 + m.x44 + m.x45 + m.x46 + m.x47 + m.x48 + m.x49 + m.x50 + m.x51 + m.x52 + m.x53
                         <= 75)

m.c13 = Constraint(expr=   m.x22 + m.x26 + m.x30 + m.x34 + m.x38 + m.x42 + m.x46 + m.x50 <= 10)

m.c14 = Constraint(expr=   m.x23 + m.x27 + m.x31 + m.x35 + m.x39 + m.x43 + m.x47 + m.x51 <= 25)

m.c15 = Constraint(expr=   m.x24 + m.x28 + m.x32 + m.x36 + m.x40 + m.x44 + m.x48 + m.x52 <= 30)

m.c16 = Constraint(expr=   m.x25 + m.x29 + m.x33 + m.x37 + m.x41 + m.x45 + m.x49 + m.x53 <= 10)

m.c17 = Constraint(expr= - 2*m.x22 + m.x26 + m.x30 - 2*m.x38 - 1.2*m.x42 + 2*m.x46 <= 0)

m.c18 = Constraint(expr=   3*m.x22 - 2*m.x26 + 2.5*m.x30 - 0.3*m.x38 - 0.3*m.x42 - 2*m.x46 <= 0)

m.c19 = Constraint(expr=   0.75*m.x22 - 0.25*m.x26 - 0.25*m.x30 - 0.25*m.x34 + 0.75*m.x38 + 0.75*m.x42 - 1.55*m.x46
                         - 0.25*m.x50 <= 0)

m.c20 = Constraint(expr= - 0.25*m.x22 + 1.25*m.x26 + 0.15*m.x30 + 0.25*m.x34 + 0.85*m.x38 + 2.75*m.x42 + 2.15*m.x46
                         + 0.25*m.x50 <= 0)

m.c21 = Constraint(expr= - m.x22 - 2*m.x26 + m.x30 - 3*m.x34 - 3*m.x38 + 0.0999999999999996*m.x42 - 2.5*m.x46 - m.x50
                         <= 0)

m.c22 = Constraint(expr=   4*m.x22 - m.x26 + 5*m.x30 - m.x34 + 2*m.x38 - 2*m.x42 - 2.1*m.x46 - 3*m.x50 <= 0)

m.c23 = Constraint(expr= - 3*m.x23 - m.x35 - 3*m.x39 - 2.2*m.x43 + m.x47 - m.x51 <= 0)

m.c24 = Constraint(expr=   3.5*m.x23 - 1.5*m.x27 + 3*m.x31 + 0.5*m.x35 + 0.2*m.x39 + 0.2*m.x43 - 1.5*m.x47 + 0.5*m.x51
                         <= 0)

m.c25 = Constraint(expr=   0.5*m.x23 - 0.5*m.x27 - 0.5*m.x31 - 0.5*m.x35 + 0.5*m.x39 + 0.5*m.x43 - 1.8*m.x47 - 0.5*m.x51
                         <= 0)

m.c26 = Constraint(expr= - m.x23 + 0.5*m.x27 - 0.6*m.x31 - 0.5*m.x35 + 0.1*m.x39 + 2*m.x43 + 1.4*m.x47 - 0.5*m.x51 <= 0)

m.c27 = Constraint(expr= - 2*m.x23 - 3*m.x27 - 4*m.x35 - 4*m.x39 - 0.9*m.x43 - 3.5*m.x47 - 2*m.x51 <= 0)

m.c28 = Constraint(expr=   3*m.x23 - 2*m.x27 + 4*m.x31 - 2*m.x35 + m.x39 - 3*m.x43 - 3.1*m.x47 - 4*m.x51 <= 0)

m.c29 = Constraint(expr= - 0.5*m.x24 + 2.5*m.x28 + 2.5*m.x32 + 1.5*m.x36 - 0.5*m.x40 + 0.3*m.x44 + 3.5*m.x48 + 1.5*m.x52
                         <= 0)

m.c30 = Constraint(expr=   0.5*m.x24 - 4.5*m.x28 - 2.5*m.x36 - 2.8*m.x40 - 2.8*m.x44 - 4.5*m.x48 - 2.5*m.x52 <= 0)

m.c31 = Constraint(expr=   0.1*m.x24 - 0.9*m.x28 - 0.9*m.x32 - 0.9*m.x36 + 0.1*m.x40 + 0.1*m.x44 - 2.2*m.x48 - 0.9*m.x52
                         <= 0)

m.c32 = Constraint(expr= - 0.3*m.x24 + 1.2*m.x28 + 0.1*m.x32 + 0.2*m.x36 + 0.8*m.x40 + 2.7*m.x44 + 2.1*m.x48 + 0.2*m.x52
                         <= 0)

m.c33 = Constraint(expr= - 2*m.x24 - 3*m.x28 - 4*m.x36 - 4*m.x40 - 0.9*m.x44 - 3.5*m.x48 - 2*m.x52 <= 0)

m.c34 = Constraint(expr=   3*m.x24 - 2*m.x28 + 4*m.x32 - 2*m.x36 + m.x40 - 3*m.x44 - 3.1*m.x48 - 4*m.x52 <= 0)

m.c35 = Constraint(expr= - 2*m.x25 + m.x29 + m.x33 - 2*m.x41 - 1.2*m.x45 + 2*m.x49 <= 0)

m.c36 = Constraint(expr=   2*m.x25 - 3*m.x29 + 1.5*m.x33 - m.x37 - 1.3*m.x41 - 1.3*m.x45 - 3*m.x49 - m.x53 <= 0)

m.c37 = Constraint(expr= - m.x29 - m.x33 - m.x37 - 2.3*m.x49 - m.x53 <= 0)

m.c38 = Constraint(expr= - 1.3*m.x25 + 0.2*m.x29 - 0.9*m.x33 - 0.8*m.x37 - 0.2*m.x41 + 1.7*m.x45 + 1.1*m.x49 - 0.8*m.x53
                         <= 0)

m.c39 = Constraint(expr= - m.x25 - 2*m.x29 + m.x33 - 3*m.x37 - 3*m.x41 + 0.0999999999999996*m.x45 - 2.5*m.x49 - m.x53
                         <= 0)

m.c40 = Constraint(expr=   3*m.x25 - 2*m.x29 + 4*m.x33 - 2*m.x37 + m.x41 - 3*m.x45 - 3.1*m.x49 - 4*m.x53 <= 0)

m.c41 = Constraint(expr=   m.x2 + m.x3 == 1)

m.c42 = Constraint(expr=   m.x4 + m.x5 + m.x6 == 1)

m.c43 = Constraint(expr=   m.x7 + m.x8 + m.x9 == 1)

m.c44 = Constraint(expr=-m.x2*m.x10 + m.x22 == 0)

m.c45 = Constraint(expr=-m.x2*m.x11 + m.x23 == 0)

m.c46 = Constraint(expr=-m.x2*m.x12 + m.x24 == 0)

m.c47 = Constraint(expr=-m.x2*m.x13 + m.x25 == 0)

m.c48 = Constraint(expr=-m.x3*m.x10 + m.x26 == 0)

m.c49 = Constraint(expr=-m.x3*m.x11 + m.x27 == 0)

m.c50 = Constraint(expr=-m.x3*m.x12 + m.x28 == 0)

m.c51 = Constraint(expr=-m.x3*m.x13 + m.x29 == 0)

m.c52 = Constraint(expr=-m.x4*m.x14 + m.x30 == 0)

m.c53 = Constraint(expr=-m.x4*m.x15 + m.x31 == 0)

m.c54 = Constraint(expr=-m.x4*m.x16 + m.x32 == 0)

m.c55 = Constraint(expr=-m.x4*m.x17 + m.x33 == 0)

m.c56 = Constraint(expr=-m.x5*m.x14 + m.x34 == 0)

m.c57 = Constraint(expr=-m.x5*m.x15 + m.x35 == 0)

m.c58 = Constraint(expr=-m.x5*m.x16 + m.x36 == 0)

m.c59 = Constraint(expr=-m.x5*m.x17 + m.x37 == 0)

m.c60 = Constraint(expr=-m.x6*m.x14 + m.x38 == 0)

m.c61 = Constraint(expr=-m.x6*m.x15 + m.x39 == 0)

m.c62 = Constraint(expr=-m.x6*m.x16 + m.x40 == 0)

m.c63 = Constraint(expr=-m.x6*m.x17 + m.x41 == 0)

m.c64 = Constraint(expr=-m.x7*m.x18 + m.x42 == 0)

m.c65 = Constraint(expr=-m.x7*m.x19 + m.x43 == 0)

m.c66 = Constraint(expr=-m.x7*m.x20 + m.x44 == 0)

m.c67 = Constraint(expr=-m.x7*m.x21 + m.x45 == 0)

m.c68 = Constraint(expr=-m.x8*m.x18 + m.x46 == 0)

m.c69 = Constraint(expr=-m.x8*m.x19 + m.x47 == 0)

m.c70 = Constraint(expr=-m.x8*m.x20 + m.x48 == 0)

m.c71 = Constraint(expr=-m.x8*m.x21 + m.x49 == 0)

m.c72 = Constraint(expr=-m.x9*m.x18 + m.x50 == 0)

m.c73 = Constraint(expr=-m.x9*m.x19 + m.x51 == 0)

m.c74 = Constraint(expr=-m.x9*m.x20 + m.x52 == 0)

m.c75 = Constraint(expr=-m.x9*m.x21 + m.x53 == 0)
