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
#        164      132       32        0
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
m.x26 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,600),initialize=0)
m.x34 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x35 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x36 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x37 = Var(within=Reals,bounds=(0,200),initialize=0)

m.obj = Objective(expr= - 3*m.x10 - 9*m.x11 - 6*m.x13 + 7*m.x14 + m.x15 + 10*m.x16 + 4*m.x17 - 6*m.x18 - 12*m.x19
                        - 3*m.x20 - 9*m.x21 + 4*m.x22 - 2*m.x23 + 7*m.x24 + m.x25 + m.x28 - 5*m.x29 + 4*m.x30 - 2*m.x31
                        - 2*m.x34 - 8*m.x35 + m.x36 - 5*m.x37, sense=minimize)

m.c2 = Constraint(expr=   m.x10 + m.x11 + m.x12 + m.x13 <= 600)

m.c3 = Constraint(expr=   m.x14 + m.x15 + m.x16 + m.x17 <= 600)

m.c4 = Constraint(expr=   m.x28 + m.x29 + m.x30 + m.x31 <= 600)

m.c5 = Constraint(expr=   m.x18 + m.x19 + m.x20 + m.x21 <= 600)

m.c6 = Constraint(expr=   m.x22 + m.x23 + m.x24 + m.x25 <= 600)

m.c7 = Constraint(expr=   m.x34 + m.x35 + m.x36 + m.x37 <= 600)

m.c8 = Constraint(expr=   m.x10 + m.x11 + m.x12 + m.x13 + m.x14 + m.x15 + m.x16 + m.x17 <= 600)

m.c9 = Constraint(expr=   m.x18 + m.x19 + m.x20 + m.x21 + m.x22 + m.x23 + m.x24 + m.x25 <= 600)

m.c10 = Constraint(expr=   m.x10 + m.x14 + m.x18 + m.x22 + m.x28 + m.x34 <= 100)

m.c11 = Constraint(expr=   m.x11 + m.x15 + m.x19 + m.x23 + m.x29 + m.x35 <= 200)

m.c12 = Constraint(expr=   m.x12 + m.x16 + m.x20 + m.x24 + m.x30 + m.x36 <= 100)

m.c13 = Constraint(expr=   m.x13 + m.x17 + m.x21 + m.x25 + m.x31 + m.x37 <= 200)

m.c14 = Constraint(expr=   0.5*m.x10 - 1.5*m.x14 + m.x18 - m.x22 - 0.5*m.x28 <= 0)

m.c15 = Constraint(expr=   1.5*m.x11 - 0.5*m.x15 + 2*m.x19 + 0.5*m.x29 + m.x35 <= 0)

m.c16 = Constraint(expr= - 2*m.x16 + 0.5*m.x20 - 1.5*m.x24 - m.x30 - 0.5*m.x36 <= 0)

m.c17 = Constraint(expr=   m.x13 - m.x17 + 1.5*m.x21 - 0.5*m.x25 + 0.5*m.x37 <= 0)

m.c18 = Constraint(expr=   m.x2 + m.x3 + m.x4 + m.x5 == 1)

m.c19 = Constraint(expr=   m.x6 + m.x7 + m.x8 + m.x9 == 1)

m.c20 = Constraint(expr=-m.x2*m.x26 + m.x10 == 0)

m.c21 = Constraint(expr=-m.x3*m.x26 + m.x11 == 0)

m.c22 = Constraint(expr=-m.x4*m.x26 + m.x12 == 0)

m.c23 = Constraint(expr=-m.x5*m.x26 + m.x13 == 0)

m.c24 = Constraint(expr=-m.x2*m.x27 + m.x14 == 0)

m.c25 = Constraint(expr=-m.x3*m.x27 + m.x15 == 0)

m.c26 = Constraint(expr=-m.x4*m.x27 + m.x16 == 0)

m.c27 = Constraint(expr=-m.x5*m.x27 + m.x17 == 0)

m.c28 = Constraint(expr=-m.x6*m.x32 + m.x18 == 0)

m.c29 = Constraint(expr=-m.x7*m.x32 + m.x19 == 0)

m.c30 = Constraint(expr=-m.x8*m.x32 + m.x20 == 0)

m.c31 = Constraint(expr=-m.x9*m.x32 + m.x21 == 0)

m.c32 = Constraint(expr=-m.x6*m.x33 + m.x22 == 0)

m.c33 = Constraint(expr=-m.x7*m.x33 + m.x23 == 0)

m.c34 = Constraint(expr=-m.x8*m.x33 + m.x24 == 0)

m.c35 = Constraint(expr=-m.x9*m.x33 + m.x25 == 0)
