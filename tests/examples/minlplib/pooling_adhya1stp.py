#  NLP written by GAMS Convert at 04/21/18 13:53:09
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         72       45        0       27        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         47       47        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        285      205       80        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(0,75),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,75),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,75),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,75),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,75),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,10),initialize=0)
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
m.x28 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x34 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x35 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x36 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x37 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x38 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x39 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x40 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x41 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x42 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x43 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x44 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x45 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x46 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x47 = Var(within=Reals,bounds=(0,10),initialize=0)

m.obj = Objective(expr= - 9*m.x28 - 18*m.x29 - 8*m.x30 - 3*m.x31 - 13*m.x32 - 22*m.x33 - 12*m.x34 - 7*m.x35 - 14*m.x36
                        - 23*m.x37 - 13*m.x38 - 8*m.x39 - 6*m.x40 - 15*m.x41 - 5*m.x42 - 11*m.x44 - 20*m.x45 - 10*m.x46
                        - 5*m.x47, sense=minimize)

m.c2 = Constraint(expr=   m.x28 + m.x29 + m.x30 + m.x31 <= 75)

m.c3 = Constraint(expr=   m.x32 + m.x33 + m.x34 + m.x35 <= 75)

m.c4 = Constraint(expr=   m.x36 + m.x37 + m.x38 + m.x39 <= 75)

m.c5 = Constraint(expr=   m.x40 + m.x41 + m.x42 + m.x43 <= 75)

m.c6 = Constraint(expr=   m.x44 + m.x45 + m.x46 + m.x47 <= 75)

m.c7 = Constraint(expr=   m.x28 + m.x29 + m.x30 + m.x31 + m.x32 + m.x33 + m.x34 + m.x35 <= 75)

m.c8 = Constraint(expr=   m.x36 + m.x37 + m.x38 + m.x39 + m.x40 + m.x41 + m.x42 + m.x43 + m.x44 + m.x45 + m.x46 + m.x47
                        <= 75)

m.c9 = Constraint(expr=   m.x28 + m.x32 + m.x36 + m.x40 + m.x44 <= 10)

m.c10 = Constraint(expr=   m.x29 + m.x33 + m.x37 + m.x41 + m.x45 <= 25)

m.c11 = Constraint(expr=   m.x30 + m.x34 + m.x38 + m.x42 + m.x46 <= 30)

m.c12 = Constraint(expr=   m.x31 + m.x35 + m.x39 + m.x43 + m.x47 <= 10)

m.c13 = Constraint(expr= - 2*m.x28 + m.x32 + m.x36 - 2*m.x44 <= 0)

m.c14 = Constraint(expr=   3*m.x28 - 2*m.x32 + 2.5*m.x36 - 0.3*m.x44 <= 0)

m.c15 = Constraint(expr=   0.75*m.x28 - 0.25*m.x32 - 0.25*m.x36 - 0.25*m.x40 + 0.75*m.x44 <= 0)

m.c16 = Constraint(expr= - 0.25*m.x28 + 1.25*m.x32 + 0.15*m.x36 + 0.25*m.x40 + 0.85*m.x44 <= 0)

m.c17 = Constraint(expr= - 3*m.x29 - m.x41 - 3*m.x45 <= 0)

m.c18 = Constraint(expr=   3.5*m.x29 - 1.5*m.x33 + 3*m.x37 + 0.5*m.x41 + 0.2*m.x45 <= 0)

m.c19 = Constraint(expr=   0.5*m.x29 - 0.5*m.x33 - 0.5*m.x37 - 0.5*m.x41 + 0.5*m.x45 <= 0)

m.c20 = Constraint(expr= - m.x29 + 0.5*m.x33 - 0.6*m.x37 - 0.5*m.x41 + 0.1*m.x45 <= 0)

m.c21 = Constraint(expr= - 0.5*m.x30 + 2.5*m.x34 + 2.5*m.x38 + 1.5*m.x42 - 0.5*m.x46 <= 0)

m.c22 = Constraint(expr=   0.5*m.x30 - 4.5*m.x34 - 2.5*m.x42 - 2.8*m.x46 <= 0)

m.c23 = Constraint(expr=   0.1*m.x30 - 0.9*m.x34 - 0.9*m.x38 - 0.9*m.x42 + 0.1*m.x46 <= 0)

m.c24 = Constraint(expr= - 0.3*m.x30 + 1.2*m.x34 + 0.1*m.x38 + 0.2*m.x42 + 0.8*m.x46 <= 0)

m.c25 = Constraint(expr= - 2*m.x31 + m.x35 + m.x39 - 2*m.x47 <= 0)

m.c26 = Constraint(expr=   2*m.x31 - 3*m.x35 + 1.5*m.x39 - m.x43 - 1.3*m.x47 <= 0)

m.c27 = Constraint(expr= - m.x35 - m.x39 - m.x43 <= 0)

m.c28 = Constraint(expr= - 1.3*m.x31 + 0.2*m.x35 - 0.9*m.x39 - 0.8*m.x43 - 0.2*m.x47 <= 0)

m.c29 = Constraint(expr=   m.x15 + m.x16 == 1)

m.c30 = Constraint(expr=   m.x17 + m.x18 + m.x19 == 1)

m.c31 = Constraint(expr=   m.x20 + m.x21 + m.x22 + m.x23 == 1)

m.c32 = Constraint(expr=   m.x24 + m.x25 + m.x26 + m.x27 == 1)

m.c33 = Constraint(expr=-m.x15*m.x7 + m.x28 == 0)

m.c34 = Constraint(expr=-m.x15*m.x8 + m.x29 == 0)

m.c35 = Constraint(expr=-m.x15*m.x9 + m.x30 == 0)

m.c36 = Constraint(expr=-m.x15*m.x10 + m.x31 == 0)

m.c37 = Constraint(expr=-m.x16*m.x7 + m.x32 == 0)

m.c38 = Constraint(expr=-m.x16*m.x8 + m.x33 == 0)

m.c39 = Constraint(expr=-m.x16*m.x9 + m.x34 == 0)

m.c40 = Constraint(expr=-m.x16*m.x10 + m.x35 == 0)

m.c41 = Constraint(expr=-m.x17*m.x11 + m.x36 == 0)

m.c42 = Constraint(expr=-m.x17*m.x12 + m.x37 == 0)

m.c43 = Constraint(expr=-m.x17*m.x13 + m.x38 == 0)

m.c44 = Constraint(expr=-m.x17*m.x14 + m.x39 == 0)

m.c45 = Constraint(expr=-m.x18*m.x11 + m.x40 == 0)

m.c46 = Constraint(expr=-m.x18*m.x12 + m.x41 == 0)

m.c47 = Constraint(expr=-m.x18*m.x13 + m.x42 == 0)

m.c48 = Constraint(expr=-m.x18*m.x14 + m.x43 == 0)

m.c49 = Constraint(expr=-m.x19*m.x11 + m.x44 == 0)

m.c50 = Constraint(expr=-m.x19*m.x12 + m.x45 == 0)

m.c51 = Constraint(expr=-m.x19*m.x13 + m.x46 == 0)

m.c52 = Constraint(expr=-m.x19*m.x14 + m.x47 == 0)

m.c53 = Constraint(expr=-m.x20*m.x2 + m.x28 == 0)

m.c54 = Constraint(expr=-m.x21*m.x2 + m.x29 == 0)

m.c55 = Constraint(expr=-m.x22*m.x2 + m.x30 == 0)

m.c56 = Constraint(expr=-m.x23*m.x2 + m.x31 == 0)

m.c57 = Constraint(expr=-m.x20*m.x3 + m.x32 == 0)

m.c58 = Constraint(expr=-m.x21*m.x3 + m.x33 == 0)

m.c59 = Constraint(expr=-m.x22*m.x3 + m.x34 == 0)

m.c60 = Constraint(expr=-m.x23*m.x3 + m.x35 == 0)

m.c61 = Constraint(expr=-m.x24*m.x4 + m.x36 == 0)

m.c62 = Constraint(expr=-m.x25*m.x4 + m.x37 == 0)

m.c63 = Constraint(expr=-m.x26*m.x4 + m.x38 == 0)

m.c64 = Constraint(expr=-m.x27*m.x4 + m.x39 == 0)

m.c65 = Constraint(expr=-m.x24*m.x5 + m.x40 == 0)

m.c66 = Constraint(expr=-m.x25*m.x5 + m.x41 == 0)

m.c67 = Constraint(expr=-m.x26*m.x5 + m.x42 == 0)

m.c68 = Constraint(expr=-m.x27*m.x5 + m.x43 == 0)

m.c69 = Constraint(expr=-m.x24*m.x6 + m.x44 == 0)

m.c70 = Constraint(expr=-m.x25*m.x6 + m.x45 == 0)

m.c71 = Constraint(expr=-m.x26*m.x6 + m.x46 == 0)

m.c72 = Constraint(expr=-m.x27*m.x6 + m.x47 == 0)
