#  NLP written by GAMS Convert at 04/21/18 13:55:19
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         13        1        7        5        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         66       66        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        156       91       65        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x2 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x3 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x4 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x5 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x6 = Var(within=Reals,bounds=(0,None),initialize=10)
m.x7 = Var(within=Reals,bounds=(0,None),initialize=5)
m.x8 = Var(within=Reals,bounds=(0,None),initialize=5)
m.x9 = Var(within=Reals,bounds=(0,None),initialize=5)
m.x10 = Var(within=Reals,bounds=(0,None),initialize=5)
m.x11 = Var(within=Reals,bounds=(0,None),initialize=5)
m.x12 = Var(within=Reals,bounds=(0,None),initialize=5)
m.x13 = Var(within=Reals,bounds=(0,None),initialize=5)
m.x14 = Var(within=Reals,bounds=(0,None),initialize=5)
m.x15 = Var(within=Reals,bounds=(0,None),initialize=5)
m.x16 = Var(within=Reals,bounds=(0,None),initialize=5)
m.x17 = Var(within=Reals,bounds=(0,None),initialize=5)
m.x18 = Var(within=Reals,bounds=(0,None),initialize=5)
m.x19 = Var(within=Reals,bounds=(0,None),initialize=5)
m.x20 = Var(within=Reals,bounds=(0,None),initialize=5)
m.x21 = Var(within=Reals,bounds=(0,None),initialize=5)
m.x22 = Var(within=Reals,bounds=(0,None),initialize=5)
m.x23 = Var(within=Reals,bounds=(0,None),initialize=5)
m.x24 = Var(within=Reals,bounds=(0,None),initialize=5)
m.x25 = Var(within=Reals,bounds=(0,None),initialize=15)
m.x26 = Var(within=Reals,bounds=(0,None),initialize=15)
m.x27 = Var(within=Reals,bounds=(0,None),initialize=15)
m.x28 = Var(within=Reals,bounds=(0,None),initialize=15)
m.x29 = Var(within=Reals,bounds=(0,None),initialize=15)
m.x30 = Var(within=Reals,bounds=(0,None),initialize=15)
m.x31 = Var(within=Reals,bounds=(0,None),initialize=15)
m.x32 = Var(within=Reals,bounds=(0,None),initialize=15)
m.x33 = Var(within=Reals,bounds=(0,None),initialize=15)
m.x34 = Var(within=Reals,bounds=(0,None),initialize=15)
m.x35 = Var(within=Reals,bounds=(0,None),initialize=15)
m.x36 = Var(within=Reals,bounds=(0,None),initialize=15)
m.x37 = Var(within=Reals,bounds=(0,None),initialize=15)
m.x38 = Var(within=Reals,bounds=(0,None),initialize=15)
m.x39 = Var(within=Reals,bounds=(0,None),initialize=15)
m.x40 = Var(within=Reals,bounds=(0,None),initialize=15)
m.x41 = Var(within=Reals,bounds=(0,None),initialize=15)
m.x42 = Var(within=Reals,bounds=(0,None),initialize=15)
m.x43 = Var(within=Reals,bounds=(0,None),initialize=15)
m.x44 = Var(within=Reals,bounds=(0,None),initialize=15)
m.x45 = Var(within=Reals,bounds=(0,None),initialize=7.5)
m.x46 = Var(within=Reals,bounds=(0,None),initialize=7.5)
m.x47 = Var(within=Reals,bounds=(0,None),initialize=7.5)
m.x48 = Var(within=Reals,bounds=(0,None),initialize=7.5)
m.x49 = Var(within=Reals,bounds=(0,None),initialize=7.5)
m.x50 = Var(within=Reals,bounds=(0,None),initialize=7.5)
m.x51 = Var(within=Reals,bounds=(0,None),initialize=7.5)
m.x52 = Var(within=Reals,bounds=(0,None),initialize=12.5)
m.x53 = Var(within=Reals,bounds=(0,None),initialize=12.5)
m.x54 = Var(within=Reals,bounds=(0,None),initialize=12.5)
m.x55 = Var(within=Reals,bounds=(0,None),initialize=12.5)
m.x56 = Var(within=Reals,bounds=(0,None),initialize=12.5)
m.x57 = Var(within=Reals,bounds=(0,None),initialize=12.5)
m.x58 = Var(within=Reals,bounds=(0,None),initialize=12.5)
m.x59 = Var(within=Reals,bounds=(0,None),initialize=12.5)
m.x60 = Var(within=Reals,bounds=(0,None),initialize=12.5)
m.x61 = Var(within=Reals,bounds=(0,None),initialize=12.5)
m.x62 = Var(within=Reals,bounds=(0,None),initialize=12.5)
m.x63 = Var(within=Reals,bounds=(0,None),initialize=12.5)
m.x64 = Var(within=Reals,bounds=(0,None),initialize=12.5)
m.x65 = Var(within=Reals,bounds=(0,None),initialize=12.5)

m.obj = Objective(expr=-(-60*0.84**m.x7*0.96**m.x25*0.92**m.x52 - 50*0.95**m.x1*0.83**m.x8*0.95**m.x26*0.94**m.x53 - 50*
                       0.85**m.x9*0.96**m.x27*0.92**m.x54 - 75*0.84**m.x10*0.96**m.x28*0.95**m.x55 - 40*0.85**m.x11*0.96
                       **m.x29*0.95**m.x56 - 60*0.85**m.x2*0.81**m.x12*0.9**m.x30*0.98**m.x57 - 35*0.9**m.x3*0.81**m.x13
                       *0.92**m.x31*0.98**m.x58 - 30*0.85**m.x4*0.82**m.x14*0.91**m.x32 - 25*0.8**m.x5*0.8**m.x15*0.92**
                       m.x33 - 150*0.86**m.x16*0.95**m.x34*0.96**m.x45*0.9**m.x59 - 30*0.99**m.x35*0.91**m.x46*0.95**
                       m.x60 - 45*0.98**m.x17*0.98**m.x36*0.92**m.x47*0.96**m.x61 - 125*0.99**m.x37*0.91**m.x48*0.91**
                       m.x62 - 200*0.88**m.x18*0.98**m.x38*0.92**m.x49*0.98**m.x63 - 200*0.87**m.x19*0.97**m.x39*0.98**
                       m.x50*0.99**m.x64 - 130*0.88**m.x20*0.98**m.x40*0.93**m.x51*0.99**m.x65 - 100*0.85**m.x21*0.95**
                       m.x41 - 100*0.95**m.x6*0.84**m.x22*0.92**m.x42 - 100*0.85**m.x23*0.93**m.x43 - 150*0.85**m.x24*
                       0.92**m.x44) - 1755, sense=minimize)

m.c1 = Constraint(expr=   m.x1 + m.x2 + m.x3 + m.x4 + m.x5 + m.x6 <= 200)

m.c2 = Constraint(expr=   m.x7 + m.x8 + m.x9 + m.x10 + m.x11 + m.x12 + m.x13 + m.x14 + m.x15 + m.x16 + m.x17 + m.x18
                        + m.x19 + m.x20 + m.x21 + m.x22 + m.x23 + m.x24 <= 100)

m.c3 = Constraint(expr=   m.x25 + m.x26 + m.x27 + m.x28 + m.x29 + m.x30 + m.x31 + m.x32 + m.x33 + m.x34 + m.x35 + m.x36
                        + m.x37 + m.x38 + m.x39 + m.x40 + m.x41 + m.x42 + m.x43 + m.x44 <= 300)

m.c4 = Constraint(expr=   m.x45 + m.x46 + m.x47 + m.x48 + m.x49 + m.x50 + m.x51 <= 150)

m.c5 = Constraint(expr=   m.x52 + m.x53 + m.x54 + m.x55 + m.x56 + m.x57 + m.x58 + m.x59 + m.x60 + m.x61 + m.x62 + m.x63
                        + m.x64 + m.x65 <= 250)

m.c6 = Constraint(expr=   m.x7 + m.x25 + m.x52 >= 30)

m.c7 = Constraint(expr=   m.x2 + m.x12 + m.x30 + m.x57 >= 100)

m.c8 = Constraint(expr=   m.x16 + m.x34 + m.x45 + m.x59 >= 40)

m.c9 = Constraint(expr=   m.x18 + m.x38 + m.x49 + m.x63 >= 50)

m.c10 = Constraint(expr=   m.x19 + m.x39 + m.x50 + m.x64 >= 70)

m.c11 = Constraint(expr=   m.x20 + m.x40 + m.x51 + m.x65 >= 35)

m.c12 = Constraint(expr=   m.x24 + m.x44 >= 10)
