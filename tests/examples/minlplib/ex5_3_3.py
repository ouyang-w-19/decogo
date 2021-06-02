#  NLP written by GAMS Convert at 04/21/18 13:51:45
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         54       54        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         63       63        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        288       88      200        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x34 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x35 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x36 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x37 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x38 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x39 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x40 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x41 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x42 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x43 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x44 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x45 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x46 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x47 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x48 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x49 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x50 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x51 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x52 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x53 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x54 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x55 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x56 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x57 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x58 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x59 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x60 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x61 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x62 = Var(within=Reals,bounds=(0,1),initialize=0)

m.obj = Objective(expr=(0.00132223 + 0.0016446*m.x33 + 0.0018611*m.x34 + 0.001262*m.x35)*m.x6 + (-9.40700000000017e-5 + 
                       0.0015625*m.x43 + 0.0091604*m.x44 + 0.0076758*m.x45)*m.x15 + (0.00457315 - 0.001748*m.x53 - 
                       0.0002583*m.x54 - 0.0004691*m.x55)*m.x24 + 1.68776, sense=minimize)

m.c1 = Constraint(expr=   m.x1 + m.x2 + m.x3 + m.x4 + m.x5 == 600)

m.c2 = Constraint(expr= - m.x1 + m.x6 - m.x17 - m.x26 == 0)

m.c3 = Constraint(expr= - m.x2 - m.x11 + m.x15 - m.x27 == 0)

m.c4 = Constraint(expr= - m.x3 - m.x12 - m.x21 + m.x24 == 0)

m.c5 = Constraint(expr=   m.x7 - m.x8 - m.x9 == 0)

m.c6 = Constraint(expr=   m.x10 - m.x11 - m.x12 - m.x13 - m.x14 == 0)

m.c7 = Constraint(expr=   m.x16 - m.x17 - m.x18 - m.x19 == 0)

m.c8 = Constraint(expr=   m.x20 - m.x21 - m.x22 - m.x23 == 0)

m.c9 = Constraint(expr=   m.x25 - m.x26 - m.x27 - m.x28 - m.x29 == 0)

m.c10 = Constraint(expr=   m.x30 - m.x31 - m.x32 == 0)

m.c11 = Constraint(expr=m.x7*m.x37 - 0.85*m.x6*m.x33 == 0)

m.c12 = Constraint(expr=m.x16*m.x48 - 0.85*m.x15*m.x44 == 0)

m.c13 = Constraint(expr=m.x25*m.x59 - m.x24*m.x55 == 0)

m.c14 = Constraint(expr=m.x10*m.x40 - m.x6*m.x34 == 0)

m.c15 = Constraint(expr=m.x20*m.x51 - 0.85*m.x15*m.x45 == 0)

m.c16 = Constraint(expr=m.x30*m.x62 - 0.85*m.x24*m.x56 == 0)

m.c17 = Constraint(expr=m.x6*m.x33 - m.x7*m.x37 - m.x10*m.x39 == 0)

m.c18 = Constraint(expr=m.x6*m.x34 - m.x7*m.x38 - m.x10*m.x40 == 0)

m.c19 = Constraint(expr=m.x6*m.x35 - m.x10*m.x41 == 0)

m.c20 = Constraint(expr=m.x6*m.x36 - m.x10*m.x42 == 0)

m.c21 = Constraint(expr=m.x15*m.x43 - m.x16*m.x47 == 0)

m.c22 = Constraint(expr=m.x15*m.x44 - m.x16*m.x48 - m.x20*m.x50 == 0)

m.c23 = Constraint(expr=m.x15*m.x45 - m.x16*m.x49 - m.x20*m.x51 == 0)

m.c24 = Constraint(expr=m.x15*m.x46 - m.x20*m.x52 == 0)

m.c25 = Constraint(expr=m.x24*m.x53 - m.x25*m.x57 == 0)

m.c26 = Constraint(expr=m.x24*m.x54 - m.x25*m.x58 == 0)

m.c27 = Constraint(expr=m.x24*m.x55 - m.x25*m.x59 - m.x30*m.x61 == 0)

m.c28 = Constraint(expr=m.x24*m.x56 - m.x25*m.x60 - m.x30*m.x62 == 0)

m.c29 = Constraint(expr=m.x17*m.x47 + m.x26*m.x57 - m.x6*m.x33 + 0.25*m.x1 == 0)

m.c30 = Constraint(expr=m.x17*m.x48 + m.x26*m.x58 - m.x6*m.x34 + 0.333*m.x1 == 0)

m.c31 = Constraint(expr=m.x17*m.x49 + m.x26*m.x59 - m.x6*m.x35 + 0.167*m.x1 == 0)

m.c32 = Constraint(expr=m.x26*m.x60 - m.x6*m.x36 + 0.25*m.x1 == 0)

m.c33 = Constraint(expr=m.x11*m.x39 + m.x27*m.x57 - m.x15*m.x43 + 0.25*m.x2 == 0)

m.c34 = Constraint(expr=m.x11*m.x40 + m.x27*m.x58 - m.x15*m.x44 + 0.333*m.x2 == 0)

m.c35 = Constraint(expr=m.x11*m.x41 + m.x27*m.x59 - m.x15*m.x45 + 0.167*m.x2 == 0)

m.c36 = Constraint(expr=m.x11*m.x42 + m.x27*m.x60 - m.x15*m.x46 + 0.25*m.x2 == 0)

m.c37 = Constraint(expr=m.x12*m.x39 - m.x24*m.x53 + 0.25*m.x3 == 0)

m.c38 = Constraint(expr=m.x12*m.x40 + m.x21*m.x50 - m.x24*m.x54 + 0.333*m.x3 == 0)

m.c39 = Constraint(expr=m.x12*m.x41 + m.x21*m.x51 - m.x24*m.x55 + 0.167*m.x3 == 0)

m.c40 = Constraint(expr=m.x12*m.x42 + m.x21*m.x52 - m.x24*m.x56 + 0.25*m.x3 == 0)

m.c41 = Constraint(expr=m.x8*m.x37 + m.x13*m.x39 + m.x18*m.x47 + m.x28*m.x57 + 0.25*m.x4 == 50)

m.c42 = Constraint(expr=m.x8*m.x38 + m.x13*m.x40 + m.x18*m.x48 + m.x22*m.x50 + m.x28*m.x58 + 0.222*m.x4 == 100)

m.c43 = Constraint(expr=m.x13*m.x41 + m.x18*m.x49 + m.x22*m.x51 + m.x28*m.x59 + m.x31*m.x61 + 0.167*m.x4 == 40)

m.c44 = Constraint(expr=m.x13*m.x42 + m.x22*m.x52 + m.x28*m.x60 + m.x31*m.x62 + 0.25*m.x4 == 100)

m.c45 = Constraint(expr=   m.x33 + m.x34 + m.x35 + m.x36 == 1)

m.c46 = Constraint(expr=   m.x37 + m.x38 == 1)

m.c47 = Constraint(expr=   m.x39 + m.x40 + m.x41 + m.x42 == 1)

m.c48 = Constraint(expr=   m.x43 + m.x44 + m.x45 + m.x46 == 1)

m.c49 = Constraint(expr=   m.x47 + m.x48 + m.x49 == 1)

m.c50 = Constraint(expr=   m.x50 + m.x51 + m.x52 == 1)

m.c51 = Constraint(expr=   m.x53 + m.x54 + m.x55 + m.x56 == 1)

m.c52 = Constraint(expr=   m.x57 + m.x58 + m.x59 + m.x60 == 1)

m.c53 = Constraint(expr=   m.x61 + m.x62 == 1)
