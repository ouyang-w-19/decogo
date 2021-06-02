#  NLP written by GAMS Convert at 04/21/18 13:55:19
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         39       21        2       16        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         41       41        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        153       75       78        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x34 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x35 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x36 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x37 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x38 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x39 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x40 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x41 = Var(within=Reals,bounds=(0,100000),initialize=0)

m.obj = Objective(expr=   m.x2 + m.x3 + m.x4 + m.x5, sense=minimize)

m.c2 = Constraint(expr= - m.x2 + m.x6 - m.x14 - m.x18 - m.x22 - m.x26 == 0)

m.c3 = Constraint(expr= - m.x3 + m.x7 - m.x15 - m.x19 - m.x23 - m.x27 == 0)

m.c4 = Constraint(expr= - m.x4 + m.x8 - m.x16 - m.x20 - m.x24 - m.x28 == 0)

m.c5 = Constraint(expr= - m.x5 - m.x17 - m.x21 - m.x25 - m.x29 == -70)

m.c6 = Constraint(expr=   m.x6 - m.x10 - m.x14 - m.x15 - m.x16 - m.x17 == 0)

m.c7 = Constraint(expr=   m.x7 - m.x11 - m.x18 - m.x19 - m.x20 - m.x21 == 0)

m.c8 = Constraint(expr=   m.x8 - m.x12 - m.x22 - m.x23 - m.x24 - m.x25 == 0)

m.c9 = Constraint(expr= - m.x13 - m.x26 - m.x27 - m.x28 - m.x29 == -60)

m.c10 = Constraint(expr=m.x6*m.x30 - (m.x14*m.x36 + m.x18*m.x38 + m.x22*m.x40) - 250*m.x26 == 0)

m.c11 = Constraint(expr=m.x6*m.x31 - (m.x14*m.x37 + m.x18*m.x39 + m.x22*m.x41) - 100*m.x26 == 0)

m.c12 = Constraint(expr=m.x7*m.x32 - (m.x15*m.x36 + m.x19*m.x38 + m.x23*m.x40) - 250*m.x27 == 0)

m.c13 = Constraint(expr=m.x7*m.x33 - (m.x15*m.x37 + m.x19*m.x39 + m.x23*m.x41) - 100*m.x27 == 0)

m.c14 = Constraint(expr=m.x8*m.x34 - (m.x16*m.x36 + m.x20*m.x38 + m.x24*m.x40) - 250*m.x28 == 0)

m.c15 = Constraint(expr=m.x8*m.x35 - (m.x16*m.x37 + m.x20*m.x39 + m.x24*m.x41) - 100*m.x28 == 0)

m.c16 = Constraint(expr=-m.x6*(m.x36 - m.x30) == -690)

m.c17 = Constraint(expr=-m.x6*(m.x37 - m.x31) == -1380)

m.c18 = Constraint(expr=-m.x7*(m.x38 - m.x32) == -2350)

m.c19 = Constraint(expr=-m.x7*(m.x39 - m.x33) == -2820)

m.c20 = Constraint(expr=-m.x8*(m.x40 - m.x34) == -6150)

m.c21 = Constraint(expr=-m.x8*(m.x41 - m.x35) == -18450)

m.c22 = Constraint(expr=   m.x30 <= 20)

m.c23 = Constraint(expr=   m.x31 <= 60)

m.c24 = Constraint(expr=   m.x32 <= 50)

m.c25 = Constraint(expr=   m.x33 <= 20)

m.c26 = Constraint(expr=   m.x34 <= 100)

m.c27 = Constraint(expr=   m.x35 <= 150)

m.c28 = Constraint(expr=   m.x36 <= 50)

m.c29 = Constraint(expr=   m.x37 <= 120)

m.c30 = Constraint(expr=   m.x38 <= 100)

m.c31 = Constraint(expr=   m.x39 <= 80)

m.c32 = Constraint(expr=   m.x40 <= 150)

m.c33 = Constraint(expr=   m.x41 <= 300)

m.c34 = Constraint(expr=-(m.x17*m.x36 + m.x21*m.x38 + m.x25*m.x40) - 250*m.x29 >= -14000)

m.c35 = Constraint(expr=-(m.x17*m.x37 + m.x21*m.x39 + m.x25*m.x41) - 100*m.x29 >= -5600)

m.c36 = Constraint(expr=   m.x6 <= 23)

m.c37 = Constraint(expr=   m.x7 <= 47)

m.c38 = Constraint(expr=   m.x8 <= 123)

m.c39 = Constraint(expr=   m.x9 <= 0)
