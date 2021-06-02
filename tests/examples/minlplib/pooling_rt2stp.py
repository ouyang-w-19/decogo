#  NLP written by GAMS Convert at 04/21/18 13:53:11
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         73       41        3       29        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         47       47        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        360      288       72        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(0,12.5),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,17.5),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,60.98),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,12.5),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,17.5),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,161.29),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,161.29),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,12.5),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,12.5),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,12.5),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,17.5),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,17.5),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,17.5),initialize=0)
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
m.x28 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,12.5),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,12.5),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,12.5),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,17.5),initialize=0)
m.x34 = Var(within=Reals,bounds=(0,17.5),initialize=0)
m.x35 = Var(within=Reals,bounds=(0,17.5),initialize=0)
m.x36 = Var(within=Reals,bounds=(0,12.5),initialize=0)
m.x37 = Var(within=Reals,bounds=(0,12.5),initialize=0)
m.x38 = Var(within=Reals,bounds=(0,12.5),initialize=0)
m.x39 = Var(within=Reals,bounds=(0,17.5),initialize=0)
m.x40 = Var(within=Reals,bounds=(0,17.5),initialize=0)
m.x41 = Var(within=Reals,bounds=(0,17.5),initialize=0)
m.x42 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x43 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x44 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x45 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x46 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x47 = Var(within=Reals,bounds=(0,5),initialize=0)

m.obj = Objective(expr= - 180.8*m.x4 - 128*m.x7 - 88*m.x8 + 110*m.x11 - 140.8*m.x30 - 180.8*m.x31 - 100.8*m.x32
                        - 140.8*m.x33 - 180.8*m.x34 - 100.8*m.x35 - 128*m.x36 - 168*m.x37 - 88*m.x38 - 128*m.x39
                        - 168*m.x40 - 88*m.x41 + 110*m.x42 + 70*m.x43 + 150*m.x44 + 110*m.x45 + 70*m.x46 + 150*m.x47
                       , sense=minimize)

m.c2 = Constraint(expr=   m.x4 + m.x30 + m.x31 + m.x32 + m.x33 + m.x34 + m.x35 <= 60.98)

m.c3 = Constraint(expr=   m.x7 + m.x8 + m.x36 + m.x37 + m.x38 + m.x39 + m.x40 + m.x41 <= 161.29)

m.c4 = Constraint(expr=   m.x11 + m.x42 + m.x43 + m.x44 + m.x45 + m.x46 + m.x47 <= 5)

m.c5 = Constraint(expr=   m.x30 + m.x31 + m.x32 + m.x36 + m.x37 + m.x38 + m.x42 + m.x43 + m.x44 <= 12.5)

m.c6 = Constraint(expr=   m.x33 + m.x34 + m.x35 + m.x39 + m.x40 + m.x41 + m.x45 + m.x46 + m.x47 <= 17.5)

m.c7 = Constraint(expr=   m.x7 + m.x11 + m.x30 + m.x33 + m.x36 + m.x39 + m.x42 + m.x45 >= 5)

m.c8 = Constraint(expr=   m.x4 + m.x31 + m.x34 + m.x37 + m.x40 + m.x43 + m.x46 >= 5)

m.c9 = Constraint(expr=   m.x8 + m.x32 + m.x35 + m.x38 + m.x41 + m.x44 + m.x47 >= 5)

m.c10 = Constraint(expr=   m.x7 + m.x11 + m.x30 + m.x33 + m.x36 + m.x39 + m.x42 + m.x45 <= 300)

m.c11 = Constraint(expr=   m.x4 + m.x31 + m.x34 + m.x37 + m.x40 + m.x43 + m.x46 <= 300)

m.c12 = Constraint(expr=   m.x8 + m.x32 + m.x35 + m.x38 + m.x41 + m.x44 + m.x47 <= 300)

m.c13 = Constraint(expr= - 0.17*m.x7 - 0.04*m.x11 + 0.0299999999999999*m.x30 + 0.0299999999999999*m.x33 - 0.17*m.x36
                         - 0.17*m.x39 - 0.04*m.x42 - 0.04*m.x45 <= 0)

m.c14 = Constraint(expr= - 3*m.x7 - 3*m.x11 - 3*m.x36 - 3*m.x39 - 3*m.x42 - 3*m.x45 <= 0)

m.c15 = Constraint(expr= - 26.1*m.x7 - 14.8*m.x30 - 14.8*m.x33 - 26.1*m.x36 - 26.1*m.x39 <= 0)

m.c16 = Constraint(expr= - 15.2*m.x7 - 8.2*m.x30 - 8.2*m.x33 - 15.2*m.x36 - 15.2*m.x39 <= 0)

m.c17 = Constraint(expr=   0.12*m.x7 - 0.01*m.x11 - 0.08*m.x30 - 0.08*m.x33 + 0.12*m.x36 + 0.12*m.x39 - 0.01*m.x42
                         - 0.01*m.x45 <= 0)

m.c18 = Constraint(expr=   7.09999999999999*m.x7 - 19*m.x11 - 4.2*m.x30 - 4.2*m.x33 + 7.09999999999999*m.x36
                         + 7.09999999999999*m.x39 - 19*m.x42 - 19*m.x45 <= 0)

m.c19 = Constraint(expr=   1.5*m.x7 - 13.7*m.x11 - 5.5*m.x30 - 5.5*m.x33 + 1.5*m.x36 + 1.5*m.x39 - 13.7*m.x42
                         - 13.7*m.x45 <= 0)

m.c20 = Constraint(expr=   0.0299999999999999*m.x4 + 0.0299999999999999*m.x31 + 0.0299999999999999*m.x34 - 0.17*m.x37
                         - 0.17*m.x40 - 0.04*m.x43 - 0.04*m.x46 <= 0)

m.c21 = Constraint(expr=   2.1*m.x4 + 2.1*m.x31 + 2.1*m.x34 - 0.9*m.x37 - 0.9*m.x40 - 0.9*m.x43 - 0.9*m.x46 <= 0)

m.c22 = Constraint(expr= - 14.8*m.x4 - 14.8*m.x31 - 14.8*m.x34 - 26.1*m.x37 - 26.1*m.x40 <= 0)

m.c23 = Constraint(expr= - 8.2*m.x4 - 8.2*m.x31 - 8.2*m.x34 - 15.2*m.x37 - 15.2*m.x40 <= 0)

m.c24 = Constraint(expr= - 0.08*m.x4 - 0.08*m.x31 - 0.08*m.x34 + 0.12*m.x37 + 0.12*m.x40 - 0.01*m.x43 - 0.01*m.x46 <= 0)

m.c25 = Constraint(expr= - 3.2*m.x4 - 3.2*m.x31 - 3.2*m.x34 + 8.09999999999999*m.x37 + 8.09999999999999*m.x40 - 18*m.x43
                         - 18*m.x46 <= 0)

m.c26 = Constraint(expr= - 2.5*m.x4 - 2.5*m.x31 - 2.5*m.x34 + 4.5*m.x37 + 4.5*m.x40 - 10.7*m.x43 - 10.7*m.x46 <= 0)

m.c27 = Constraint(expr= - 0.17*m.x8 + 0.0299999999999999*m.x32 + 0.0299999999999999*m.x35 - 0.17*m.x38 - 0.17*m.x41
                         - 0.04*m.x44 - 0.04*m.x47 <= 0)

m.c28 = Constraint(expr= - 3*m.x8 - 3*m.x38 - 3*m.x41 - 3*m.x44 - 3*m.x47 <= 0)

m.c29 = Constraint(expr= - 26.1*m.x8 - 14.8*m.x32 - 14.8*m.x35 - 26.1*m.x38 - 26.1*m.x41 <= 0)

m.c30 = Constraint(expr= - 15.2*m.x8 - 8.2*m.x32 - 8.2*m.x35 - 15.2*m.x38 - 15.2*m.x41 <= 0)

m.c31 = Constraint(expr=   0.12*m.x8 - 0.08*m.x32 - 0.08*m.x35 + 0.12*m.x38 + 0.12*m.x41 - 0.01*m.x44 - 0.01*m.x47 <= 0)

m.c32 = Constraint(expr=   3.09999999999999*m.x8 - 8.2*m.x32 - 8.2*m.x35 + 3.09999999999999*m.x38
                         + 3.09999999999999*m.x41 - 23*m.x44 - 23*m.x47 <= 0)

m.c33 = Constraint(expr= - 7*m.x32 - 7*m.x35 - 15.2*m.x44 - 15.2*m.x47 <= 0)

m.c34 = Constraint(expr=   m.x18 + m.x20 + m.x22 == 1)

m.c35 = Constraint(expr=   m.x19 + m.x21 + m.x23 == 1)

m.c36 = Constraint(expr=   m.x24 + m.x25 + m.x26 == 1)

m.c37 = Constraint(expr=   m.x27 + m.x28 + m.x29 == 1)

m.c38 = Constraint(expr=-m.x18*m.x12 + m.x30 == 0)

m.c39 = Constraint(expr=-m.x18*m.x13 + m.x31 == 0)

m.c40 = Constraint(expr=-m.x18*m.x14 + m.x32 == 0)

m.c41 = Constraint(expr=-m.x19*m.x15 + m.x33 == 0)

m.c42 = Constraint(expr=-m.x19*m.x16 + m.x34 == 0)

m.c43 = Constraint(expr=-m.x19*m.x17 + m.x35 == 0)

m.c44 = Constraint(expr=-m.x20*m.x12 + m.x36 == 0)

m.c45 = Constraint(expr=-m.x20*m.x13 + m.x37 == 0)

m.c46 = Constraint(expr=-m.x20*m.x14 + m.x38 == 0)

m.c47 = Constraint(expr=-m.x21*m.x15 + m.x39 == 0)

m.c48 = Constraint(expr=-m.x21*m.x16 + m.x40 == 0)

m.c49 = Constraint(expr=-m.x21*m.x17 + m.x41 == 0)

m.c50 = Constraint(expr=-m.x22*m.x12 + m.x42 == 0)

m.c51 = Constraint(expr=-m.x22*m.x13 + m.x43 == 0)

m.c52 = Constraint(expr=-m.x22*m.x14 + m.x44 == 0)

m.c53 = Constraint(expr=-m.x23*m.x15 + m.x45 == 0)

m.c54 = Constraint(expr=-m.x23*m.x16 + m.x46 == 0)

m.c55 = Constraint(expr=-m.x23*m.x17 + m.x47 == 0)

m.c56 = Constraint(expr=-m.x24*m.x2 + m.x30 == 0)

m.c57 = Constraint(expr=-m.x25*m.x2 + m.x31 == 0)

m.c58 = Constraint(expr=-m.x26*m.x2 + m.x32 == 0)

m.c59 = Constraint(expr=-m.x27*m.x3 + m.x33 == 0)

m.c60 = Constraint(expr=-m.x28*m.x3 + m.x34 == 0)

m.c61 = Constraint(expr=-m.x29*m.x3 + m.x35 == 0)

m.c62 = Constraint(expr=-m.x24*m.x5 + m.x36 == 0)

m.c63 = Constraint(expr=-m.x25*m.x5 + m.x37 == 0)

m.c64 = Constraint(expr=-m.x26*m.x5 + m.x38 == 0)

m.c65 = Constraint(expr=-m.x27*m.x6 + m.x39 == 0)

m.c66 = Constraint(expr=-m.x28*m.x6 + m.x40 == 0)

m.c67 = Constraint(expr=-m.x29*m.x6 + m.x41 == 0)

m.c68 = Constraint(expr=-m.x24*m.x9 + m.x42 == 0)

m.c69 = Constraint(expr=-m.x25*m.x9 + m.x43 == 0)

m.c70 = Constraint(expr=-m.x26*m.x9 + m.x44 == 0)

m.c71 = Constraint(expr=-m.x27*m.x10 + m.x45 == 0)

m.c72 = Constraint(expr=-m.x28*m.x10 + m.x46 == 0)

m.c73 = Constraint(expr=-m.x29*m.x10 + m.x47 == 0)
