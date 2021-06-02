#  NLP written by GAMS Convert at 04/21/18 13:55:06
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         41       29        0       12        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         47       47        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        215      125       90        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x34 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x35 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x36 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x37 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x38 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x39 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x40 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x41 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x42 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x43 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x44 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x45 = Var(within=Reals,bounds=(0,1000000),initialize=0)
m.x46 = Var(within=Reals,bounds=(0,1000000),initialize=0)

m.obj = Objective(expr=   m.x44 + m.x45 + m.x46, sense=minimize)

m.c2 = Constraint(expr= - m.x28 - m.x34 - m.x35 - m.x36 == -13.1)

m.c3 = Constraint(expr= - m.x29 - m.x37 - m.x38 - m.x39 == -32.7)

m.c4 = Constraint(expr= - m.x30 - m.x40 - m.x41 - m.x42 == -56.5)

m.c5 = Constraint(expr= - m.x19 - m.x22 - m.x25 - m.x34 - m.x37 - m.x40 + m.x44 == 0)

m.c6 = Constraint(expr= - m.x20 - m.x23 - m.x26 - m.x35 - m.x38 - m.x41 + m.x45 == 0)

m.c7 = Constraint(expr= - m.x21 - m.x24 - m.x27 - m.x36 - m.x39 - m.x42 + m.x46 == 0)

m.c8 = Constraint(expr= - m.x19 - m.x20 - m.x21 - m.x31 + m.x44 == 0)

m.c9 = Constraint(expr= - m.x22 - m.x23 - m.x24 - m.x32 + m.x45 == 0)

m.c10 = Constraint(expr= - m.x25 - m.x26 - m.x27 - m.x33 + m.x46 == 0)

m.c11 = Constraint(expr= - m.x28 - m.x29 - m.x30 - m.x31 - m.x32 - m.x33 + m.x43 == 0)

m.c12 = Constraint(expr=m.x19*m.x10 + m.x22*m.x13 + m.x25*m.x16 - m.x44*m.x1 + 10*m.x34 + 110*m.x37 + 100*m.x40 == 0)

m.c13 = Constraint(expr=m.x19*m.x11 + m.x22*m.x14 + m.x25*m.x17 - m.x44*m.x2 + 390*m.x34 + 16780*m.x37 + 25*m.x40 == 0)

m.c14 = Constraint(expr=m.x19*m.x12 + m.x22*m.x15 + m.x25*m.x18 - m.x44*m.x3 + 25*m.x34 + 40*m.x37 + 35*m.x40 == 0)

m.c15 = Constraint(expr=m.x20*m.x10 + m.x23*m.x13 + m.x26*m.x16 - m.x45*m.x4 + 10*m.x35 + 110*m.x38 + 100*m.x41 == 0)

m.c16 = Constraint(expr=m.x20*m.x11 + m.x23*m.x14 + m.x26*m.x17 - m.x45*m.x5 + 390*m.x35 + 16780*m.x38 + 25*m.x41 == 0)

m.c17 = Constraint(expr=m.x20*m.x12 + m.x23*m.x15 + m.x26*m.x18 - m.x45*m.x6 + 25*m.x35 + 40*m.x38 + 35*m.x41 == 0)

m.c18 = Constraint(expr=m.x21*m.x10 + m.x24*m.x13 + m.x27*m.x16 - m.x46*m.x7 + 10*m.x36 + 110*m.x39 + 100*m.x42 == 0)

m.c19 = Constraint(expr=m.x21*m.x11 + m.x24*m.x14 + m.x27*m.x17 - m.x46*m.x8 + 390*m.x36 + 16780*m.x39 + 25*m.x42 == 0)

m.c20 = Constraint(expr=m.x21*m.x12 + m.x24*m.x15 + m.x27*m.x18 - m.x46*m.x9 + 25*m.x36 + 40*m.x39 + 35*m.x42 == 0)

m.c21 = Constraint(expr=   m.x1 <= 20000)

m.c22 = Constraint(expr=   m.x2 <= 20000)

m.c23 = Constraint(expr=   m.x3 <= 20000)

m.c24 = Constraint(expr=   m.x4 <= 20000)

m.c25 = Constraint(expr=   m.x5 <= 20000)

m.c26 = Constraint(expr=   m.x6 <= 20000)

m.c27 = Constraint(expr=   m.x7 <= 20000)

m.c28 = Constraint(expr=   m.x8 <= 20000)

m.c29 = Constraint(expr=   m.x9 <= 20000)

m.c30 = Constraint(expr= - m.x1 + m.x10 == 0)

m.c31 = Constraint(expr= - 0.001*m.x2 + m.x11 == 0)

m.c32 = Constraint(expr= - m.x3 + m.x12 == 0)

m.c33 = Constraint(expr= - 0.1*m.x4 + m.x13 == 0)

m.c34 = Constraint(expr= - 0.1*m.x5 + m.x14 == 0)

m.c35 = Constraint(expr= - 0.03*m.x6 + m.x15 == 0)

m.c36 = Constraint(expr= - 0.05*m.x7 + m.x16 == 0)

m.c37 = Constraint(expr= - m.x8 + m.x17 == 0)

m.c38 = Constraint(expr= - 0.8*m.x9 + m.x18 == 0)

m.c39 = Constraint(expr=m.x31*m.x10 + m.x32*m.x13 + m.x33*m.x16 + 10*m.x28 + 110*m.x29 + 100*m.x30 - 2*m.x43 <= 0)

m.c40 = Constraint(expr=m.x31*m.x11 + m.x32*m.x14 + m.x33*m.x17 + 390*m.x28 + 16780*m.x29 + 25*m.x30 - 2*m.x43 <= 0)

m.c41 = Constraint(expr=m.x31*m.x12 + m.x32*m.x15 + m.x33*m.x18 + 25*m.x28 + 40*m.x29 + 35*m.x30 - 5*m.x43 <= 0)
