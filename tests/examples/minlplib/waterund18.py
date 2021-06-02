#  NLP written by GAMS Convert at 04/21/18 13:55:19
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         65       33        4       28        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         61       61        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        287      131      156        0
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
m.x42 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x43 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x44 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x45 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x46 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x47 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x48 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x49 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x50 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x51 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x52 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x53 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x54 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x55 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x56 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x57 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x58 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x59 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x60 = Var(within=Reals,bounds=(0,100000),initialize=0)
m.x61 = Var(within=Reals,bounds=(0,100000),initialize=0)

m.obj = Objective(expr=   m.x2 + m.x3 + m.x4 + m.x5 + m.x6 + m.x7 + m.x8 + m.x9 + m.x10 + m.x11 + m.x12 + m.x13
                       , sense=minimize)

m.c2 = Constraint(expr= - m.x2 - m.x6 - m.x10 + m.x14 - m.x22 - m.x26 - m.x30 - m.x34 == 0)

m.c3 = Constraint(expr= - m.x3 - m.x7 - m.x11 + m.x15 - m.x23 - m.x27 - m.x31 - m.x35 == 0)

m.c4 = Constraint(expr= - m.x4 - m.x8 - m.x12 + m.x16 - m.x24 - m.x28 - m.x32 - m.x36 == 0)

m.c5 = Constraint(expr= - m.x5 - m.x9 - m.x13 - m.x25 - m.x29 - m.x33 - m.x37 == -170)

m.c6 = Constraint(expr=   m.x14 - m.x18 - m.x22 - m.x23 - m.x24 - m.x25 == 0)

m.c7 = Constraint(expr=   m.x15 - m.x19 - m.x26 - m.x27 - m.x28 - m.x29 == 0)

m.c8 = Constraint(expr=   m.x16 - m.x20 - m.x30 - m.x31 - m.x32 - m.x33 == 0)

m.c9 = Constraint(expr= - m.x21 - m.x34 - m.x35 - m.x36 - m.x37 == -140)

m.c10 = Constraint(expr=m.x14*m.x38 - (m.x22*m.x50 + m.x26*m.x54 + m.x30*m.x58) - 2*m.x6 - 250*m.x34 == 0)

m.c11 = Constraint(expr=m.x14*m.x39 - (m.x22*m.x51 + m.x26*m.x55 + m.x30*m.x59) - 3*m.x2 - m.x6 - 180*m.x34 == 0)

m.c12 = Constraint(expr=m.x14*m.x40 - (m.x22*m.x52 + m.x26*m.x56 + m.x30*m.x60) - m.x10 - 90*m.x34 == 0)

m.c13 = Constraint(expr=m.x14*m.x41 - (m.x22*m.x53 + m.x26*m.x57 + m.x30*m.x61) - 3*m.x10 - 90*m.x34 == 0)

m.c14 = Constraint(expr=m.x15*m.x42 - (m.x23*m.x50 + m.x27*m.x54 + m.x31*m.x58) - 2*m.x7 - 250*m.x35 == 0)

m.c15 = Constraint(expr=m.x15*m.x43 - (m.x23*m.x51 + m.x27*m.x55 + m.x31*m.x59) - 3*m.x3 - m.x7 - 180*m.x35 == 0)

m.c16 = Constraint(expr=m.x15*m.x44 - (m.x23*m.x52 + m.x27*m.x56 + m.x31*m.x60) - m.x11 - 90*m.x35 == 0)

m.c17 = Constraint(expr=m.x15*m.x45 - (m.x23*m.x53 + m.x27*m.x57 + m.x31*m.x61) - 3*m.x11 - 90*m.x35 == 0)

m.c18 = Constraint(expr=m.x16*m.x46 - (m.x24*m.x50 + m.x28*m.x54 + m.x32*m.x58) - 2*m.x8 - 250*m.x36 == 0)

m.c19 = Constraint(expr=m.x16*m.x47 - (m.x24*m.x51 + m.x28*m.x55 + m.x32*m.x59) - 3*m.x4 - m.x8 - 180*m.x36 == 0)

m.c20 = Constraint(expr=m.x16*m.x48 - (m.x24*m.x52 + m.x28*m.x56 + m.x32*m.x60) - m.x12 - 90*m.x36 == 0)

m.c21 = Constraint(expr=m.x16*m.x49 - (m.x24*m.x53 + m.x28*m.x57 + m.x32*m.x61) - 3*m.x12 - 90*m.x36 == 0)

m.c22 = Constraint(expr=-m.x14*(m.x50 - m.x38) == -3690)

m.c23 = Constraint(expr=-m.x14*(m.x51 - m.x39) == -3690)

m.c24 = Constraint(expr=-m.x14*(m.x52 - m.x40) == -1230)

m.c25 = Constraint(expr=-m.x14*(m.x53 - m.x41) == -3690)

m.c26 = Constraint(expr=-m.x15*(m.x54 - m.x42) == -940)

m.c27 = Constraint(expr=-m.x15*(m.x55 - m.x43) == -2350)

m.c28 = Constraint(expr=-m.x15*(m.x56 - m.x44) == -1175)

m.c29 = Constraint(expr=-m.x15*(m.x57 - m.x45) == -1880)

m.c30 = Constraint(expr=-m.x16*(m.x58 - m.x46) == -12300)

m.c31 = Constraint(expr=-m.x16*(m.x59 - m.x47) == -12300)

m.c32 = Constraint(expr=-m.x16*(m.x60 - m.x48) == -6150)

m.c33 = Constraint(expr=-m.x16*(m.x61 - m.x49) == -4920)

m.c34 = Constraint(expr=   m.x38 <= 20)

m.c35 = Constraint(expr=   m.x39 <= 30)

m.c36 = Constraint(expr=   m.x40 <= 20)

m.c37 = Constraint(expr=   m.x41 <= 10)

m.c38 = Constraint(expr=   m.x42 <= 50)

m.c39 = Constraint(expr=   m.x43 <= 20)

m.c40 = Constraint(expr=   m.x44 <= 20)

m.c41 = Constraint(expr=   m.x45 <= 20)

m.c42 = Constraint(expr=   m.x46 <= 100)

m.c43 = Constraint(expr=   m.x47 <= 150)

m.c44 = Constraint(expr=   m.x48 <= 30)

m.c45 = Constraint(expr=   m.x49 <= 20)

m.c46 = Constraint(expr=   m.x50 <= 50)

m.c47 = Constraint(expr=   m.x51 <= 60)

m.c48 = Constraint(expr=   m.x52 <= 30)

m.c49 = Constraint(expr=   m.x53 <= 40)

m.c50 = Constraint(expr=   m.x54 <= 70)

m.c51 = Constraint(expr=   m.x55 <= 70)

m.c52 = Constraint(expr=   m.x56 <= 45)

m.c53 = Constraint(expr=   m.x57 <= 60)

m.c54 = Constraint(expr=   m.x58 <= 200)

m.c55 = Constraint(expr=   m.x59 <= 250)

m.c56 = Constraint(expr=   m.x60 <= 80)

m.c57 = Constraint(expr=   m.x61 <= 60)

m.c58 = Constraint(expr=-(m.x25*m.x50 + m.x29*m.x54 + m.x33*m.x58) - 2*m.x9 - 250*m.x37 >= -34000)

m.c59 = Constraint(expr=-(m.x25*m.x51 + m.x29*m.x55 + m.x33*m.x59) - 3*m.x5 - m.x9 - 180*m.x37 >= -13600)

m.c60 = Constraint(expr=-(m.x25*m.x52 + m.x29*m.x56 + m.x33*m.x60) - m.x13 - 90*m.x37 >= -3400)

m.c61 = Constraint(expr=-(m.x25*m.x53 + m.x29*m.x57 + m.x33*m.x61) - 3*m.x13 - 90*m.x37 >= -10200)

m.c62 = Constraint(expr=   m.x14 <= 123)

m.c63 = Constraint(expr=   m.x15 <= 47)

m.c64 = Constraint(expr=   m.x16 <= 123)

m.c65 = Constraint(expr=   m.x17 <= 0)
