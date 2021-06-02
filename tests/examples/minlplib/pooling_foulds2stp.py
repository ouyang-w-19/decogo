#  NLP written by GAMS Convert at 04/21/18 13:53:10
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         53       37        0       16        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         49       49        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        216      152       64        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x34 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x35 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x36 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x37 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x38 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x39 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x40 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x41 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x42 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x43 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x44 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x45 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x46 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x47 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x48 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x49 = Var(within=Reals,bounds=(0,200),initialize=0)

m.obj = Objective(expr=   m.x4 - 5*m.x5 + 4*m.x6 - 2*m.x7 - 2*m.x10 - 8*m.x11 + m.x12 - 5*m.x13 - 3*m.x34 - 9*m.x35
                        - 6*m.x37 + 7*m.x38 + m.x39 + 10*m.x40 + 4*m.x41 - 6*m.x42 - 12*m.x43 - 3*m.x44 - 9*m.x45
                        + 4*m.x46 - 2*m.x47 + 7*m.x48 + m.x49, sense=minimize)

m.c2 = Constraint(expr=   m.x34 + m.x35 + m.x36 + m.x37 <= 600)

m.c3 = Constraint(expr=   m.x38 + m.x39 + m.x40 + m.x41 <= 600)

m.c4 = Constraint(expr=   m.x4 + m.x5 + m.x6 + m.x7 <= 600)

m.c5 = Constraint(expr=   m.x42 + m.x43 + m.x44 + m.x45 <= 600)

m.c6 = Constraint(expr=   m.x46 + m.x47 + m.x48 + m.x49 <= 600)

m.c7 = Constraint(expr=   m.x10 + m.x11 + m.x12 + m.x13 <= 600)

m.c8 = Constraint(expr=   m.x34 + m.x35 + m.x36 + m.x37 + m.x38 + m.x39 + m.x40 + m.x41 <= 600)

m.c9 = Constraint(expr=   m.x42 + m.x43 + m.x44 + m.x45 + m.x46 + m.x47 + m.x48 + m.x49 <= 600)

m.c10 = Constraint(expr=   m.x4 + m.x10 + m.x34 + m.x38 + m.x42 + m.x46 <= 100)

m.c11 = Constraint(expr=   m.x5 + m.x11 + m.x35 + m.x39 + m.x43 + m.x47 <= 200)

m.c12 = Constraint(expr=   m.x6 + m.x12 + m.x36 + m.x40 + m.x44 + m.x48 <= 100)

m.c13 = Constraint(expr=   m.x7 + m.x13 + m.x37 + m.x41 + m.x45 + m.x49 <= 200)

m.c14 = Constraint(expr= - 0.5*m.x4 + 0.5*m.x34 - 1.5*m.x38 + m.x42 - m.x46 <= 0)

m.c15 = Constraint(expr=   0.5*m.x5 + m.x11 + 1.5*m.x35 - 0.5*m.x39 + 2*m.x43 <= 0)

m.c16 = Constraint(expr= - m.x6 - 0.5*m.x12 - 2*m.x40 + 0.5*m.x44 - 1.5*m.x48 <= 0)

m.c17 = Constraint(expr=   0.5*m.x13 + m.x37 - m.x41 + 1.5*m.x45 - 0.5*m.x49 <= 0)

m.c18 = Constraint(expr=   m.x22 + m.x23 == 1)

m.c19 = Constraint(expr=   m.x24 + m.x25 == 1)

m.c20 = Constraint(expr=   m.x26 + m.x27 + m.x28 + m.x29 == 1)

m.c21 = Constraint(expr=   m.x30 + m.x31 + m.x32 + m.x33 == 1)

m.c22 = Constraint(expr=-m.x22*m.x14 + m.x34 == 0)

m.c23 = Constraint(expr=-m.x22*m.x15 + m.x35 == 0)

m.c24 = Constraint(expr=-m.x22*m.x16 + m.x36 == 0)

m.c25 = Constraint(expr=-m.x22*m.x17 + m.x37 == 0)

m.c26 = Constraint(expr=-m.x23*m.x14 + m.x38 == 0)

m.c27 = Constraint(expr=-m.x23*m.x15 + m.x39 == 0)

m.c28 = Constraint(expr=-m.x23*m.x16 + m.x40 == 0)

m.c29 = Constraint(expr=-m.x23*m.x17 + m.x41 == 0)

m.c30 = Constraint(expr=-m.x24*m.x18 + m.x42 == 0)

m.c31 = Constraint(expr=-m.x24*m.x19 + m.x43 == 0)

m.c32 = Constraint(expr=-m.x24*m.x20 + m.x44 == 0)

m.c33 = Constraint(expr=-m.x24*m.x21 + m.x45 == 0)

m.c34 = Constraint(expr=-m.x25*m.x18 + m.x46 == 0)

m.c35 = Constraint(expr=-m.x25*m.x19 + m.x47 == 0)

m.c36 = Constraint(expr=-m.x25*m.x20 + m.x48 == 0)

m.c37 = Constraint(expr=-m.x25*m.x21 + m.x49 == 0)

m.c38 = Constraint(expr=-m.x26*m.x2 + m.x34 == 0)

m.c39 = Constraint(expr=-m.x27*m.x2 + m.x35 == 0)

m.c40 = Constraint(expr=-m.x28*m.x2 + m.x36 == 0)

m.c41 = Constraint(expr=-m.x29*m.x2 + m.x37 == 0)

m.c42 = Constraint(expr=-m.x26*m.x3 + m.x38 == 0)

m.c43 = Constraint(expr=-m.x27*m.x3 + m.x39 == 0)

m.c44 = Constraint(expr=-m.x28*m.x3 + m.x40 == 0)

m.c45 = Constraint(expr=-m.x29*m.x3 + m.x41 == 0)

m.c46 = Constraint(expr=-m.x30*m.x8 + m.x42 == 0)

m.c47 = Constraint(expr=-m.x31*m.x8 + m.x43 == 0)

m.c48 = Constraint(expr=-m.x32*m.x8 + m.x44 == 0)

m.c49 = Constraint(expr=-m.x33*m.x8 + m.x45 == 0)

m.c50 = Constraint(expr=-m.x30*m.x9 + m.x46 == 0)

m.c51 = Constraint(expr=-m.x31*m.x9 + m.x47 == 0)

m.c52 = Constraint(expr=-m.x32*m.x9 + m.x48 == 0)

m.c53 = Constraint(expr=-m.x33*m.x9 + m.x49 == 0)
