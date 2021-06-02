#  NLP written by GAMS Convert at 04/21/18 13:53:10
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         35       19        0       16        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         37       37        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        160      128       32        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,200),initialize=0)
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
m.x22 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x34 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x35 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x36 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x37 = Var(within=Reals,bounds=(0,200),initialize=0)

m.obj = Objective(expr=   m.x6 - 5*m.x7 + 4*m.x8 - 2*m.x9 - 2*m.x10 - 8*m.x11 + m.x12 - 5*m.x13 - 3*m.x22 - 9*m.x23
                        - 6*m.x25 + 7*m.x26 + m.x27 + 10*m.x28 + 4*m.x29 - 6*m.x30 - 12*m.x31 - 3*m.x32 - 9*m.x33
                        + 4*m.x34 - 2*m.x35 + 7*m.x36 + m.x37, sense=minimize)

m.c2 = Constraint(expr=   m.x22 + m.x23 + m.x24 + m.x25 <= 600)

m.c3 = Constraint(expr=   m.x26 + m.x27 + m.x28 + m.x29 <= 600)

m.c4 = Constraint(expr=   m.x6 + m.x7 + m.x8 + m.x9 <= 600)

m.c5 = Constraint(expr=   m.x30 + m.x31 + m.x32 + m.x33 <= 600)

m.c6 = Constraint(expr=   m.x34 + m.x35 + m.x36 + m.x37 <= 600)

m.c7 = Constraint(expr=   m.x10 + m.x11 + m.x12 + m.x13 <= 600)

m.c8 = Constraint(expr=   m.x22 + m.x23 + m.x24 + m.x25 + m.x26 + m.x27 + m.x28 + m.x29 <= 600)

m.c9 = Constraint(expr=   m.x30 + m.x31 + m.x32 + m.x33 + m.x34 + m.x35 + m.x36 + m.x37 <= 600)

m.c10 = Constraint(expr=   m.x6 + m.x10 + m.x22 + m.x26 + m.x30 + m.x34 <= 100)

m.c11 = Constraint(expr=   m.x7 + m.x11 + m.x23 + m.x27 + m.x31 + m.x35 <= 200)

m.c12 = Constraint(expr=   m.x8 + m.x12 + m.x24 + m.x28 + m.x32 + m.x36 <= 100)

m.c13 = Constraint(expr=   m.x9 + m.x13 + m.x25 + m.x29 + m.x33 + m.x37 <= 200)

m.c14 = Constraint(expr= - 0.5*m.x6 + 0.5*m.x22 - 1.5*m.x26 + m.x30 - m.x34 <= 0)

m.c15 = Constraint(expr=   0.5*m.x7 + m.x11 + 1.5*m.x23 - 0.5*m.x27 + 2*m.x31 <= 0)

m.c16 = Constraint(expr= - m.x8 - 0.5*m.x12 - 2*m.x28 + 0.5*m.x32 - 1.5*m.x36 <= 0)

m.c17 = Constraint(expr=   0.5*m.x13 + m.x25 - m.x29 + 1.5*m.x33 - 0.5*m.x37 <= 0)

m.c18 = Constraint(expr=   m.x2 + m.x3 == 1)

m.c19 = Constraint(expr=   m.x4 + m.x5 == 1)

m.c20 = Constraint(expr=-m.x2*m.x14 + m.x22 == 0)

m.c21 = Constraint(expr=-m.x2*m.x15 + m.x23 == 0)

m.c22 = Constraint(expr=-m.x2*m.x16 + m.x24 == 0)

m.c23 = Constraint(expr=-m.x2*m.x17 + m.x25 == 0)

m.c24 = Constraint(expr=-m.x3*m.x14 + m.x26 == 0)

m.c25 = Constraint(expr=-m.x3*m.x15 + m.x27 == 0)

m.c26 = Constraint(expr=-m.x3*m.x16 + m.x28 == 0)

m.c27 = Constraint(expr=-m.x3*m.x17 + m.x29 == 0)

m.c28 = Constraint(expr=-m.x4*m.x18 + m.x30 == 0)

m.c29 = Constraint(expr=-m.x4*m.x19 + m.x31 == 0)

m.c30 = Constraint(expr=-m.x4*m.x20 + m.x32 == 0)

m.c31 = Constraint(expr=-m.x4*m.x21 + m.x33 == 0)

m.c32 = Constraint(expr=-m.x5*m.x18 + m.x34 == 0)

m.c33 = Constraint(expr=-m.x5*m.x19 + m.x35 == 0)

m.c34 = Constraint(expr=-m.x5*m.x20 + m.x36 == 0)

m.c35 = Constraint(expr=-m.x5*m.x21 + m.x37 == 0)
