#  NLP written by GAMS Convert at 04/21/18 13:54:00
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         36        1        8       27        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         15       15        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        110       47       63        0


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,None),initialize=1100.53862181846)
m.x2 = Var(within=Reals,bounds=(0,None),initialize=1279.53722102267)
m.x3 = Var(within=Reals,bounds=(0,None),initialize=913.955157873337)
m.x4 = Var(within=Reals,bounds=(100,None),initialize=913.955157873337)
m.x5 = Var(within=Reals,bounds=(100,None),initialize=733.692414545642)
m.x6 = Var(within=Reals,bounds=(100,None),initialize=913.955157873337)
m.x7 = Var(within=Reals,bounds=(300,None),initialize=1399.16837300491)
m.x8 = Var(within=Reals,bounds=(300,None),initialize=365.579732331283)
m.x9 = Var(within=Reals,bounds=(300,None),initialize=365.579732331283)
m.x10 = Var(within=Reals,bounds=(300,None),initialize=459.625873931453)
m.x11 = Var(within=Reals,bounds=(300,None),initialize=459.625873931453)
m.x12 = Var(within=Reals,bounds=(5,None),initialize=6.78386433964926)
m.x13 = Var(within=Reals,bounds=(5,None),initialize=10.3944267123785)
m.x14 = Var(within=Reals,bounds=(5,None),initialize=7.13617632404846)
m.x15 = Var(within=Reals,bounds=(None,None),initialize=155153.543657587)

m.obj = Objective(expr=m.x15, sense=minimize)

m.c1 = Constraint(expr=   m.x1 - 1.2*m.x4 >= 0)

m.c2 = Constraint(expr=   m.x1 - 1.5*m.x5 >= 0)

m.c3 = Constraint(expr=   m.x1 - 1.1*m.x6 >= 0)

m.c4 = Constraint(expr=   m.x2 - 1.4*m.x4 >= 0)

m.c5 = Constraint(expr=   m.x2 - 1.2*m.x6 >= 0)

m.c6 = Constraint(expr=   m.x3 - m.x4 >= 0)

m.c7 = Constraint(expr=   m.x3 - m.x5 >= 0)

m.c8 = Constraint(expr=   m.x3 - m.x6 >= 0)

m.c9 = Constraint(expr=   m.x8 - m.x9 <= 0)

m.c10 = Constraint(expr=   m.x10 - m.x11 <= 0)

m.c11 = Constraint(expr=   m.x8 - m.x11 <= 0)

m.c12 = Constraint(expr= - m.x8 + m.x9 == 0)

m.c13 = Constraint(expr=592*m.x1**0.65 + 582*m.x2**0.39 + 1200*m.x3**0.52 + 370*m.x7**0.22 + 250*m.x8**0.4 + 210*m.x9**
                        0.62 + 250*m.x10**0.4 + 200*m.x11**0.83 - m.x15 <= 0)

m.c14 = Constraint(expr=400000*m.x12/m.x4 + 300000*m.x13/m.x5 + 100000*m.x14/m.x6 <= 8000)

m.c15 = Constraint(expr=1.2*m.x4/m.x7 - m.x12 <= 0)

m.c16 = Constraint(expr=1.2*m.x4/m.x8 - m.x12 <= 0)

m.c17 = Constraint(expr=1.2*m.x4/m.x9 - m.x12 <= 0)

m.c18 = Constraint(expr=1.4*m.x4/m.x10 - m.x12 <= 0)

m.c19 = Constraint(expr=1.4*m.x4/m.x11 - m.x12 <= 0)

m.c20 = Constraint(expr=1.5*m.x5/m.x7 - m.x13 <= 0)

m.c21 = Constraint(expr=1.5*m.x5/m.x8 - m.x13 <= 0)

m.c22 = Constraint(expr=1.5*m.x5/m.x9 - m.x13 <= 0)

m.c23 = Constraint(expr=1.5*m.x5/m.x11 - m.x13 <= 0)

m.c24 = Constraint(expr=1.1*m.x6/m.x7 - m.x14 <= 0)

m.c25 = Constraint(expr=1.1*m.x6/m.x8 - m.x14 <= 0)

m.c26 = Constraint(expr=1.1*m.x6/m.x9 - m.x14 <= 0)

m.c27 = Constraint(expr=1.2*m.x6/m.x10 - m.x14 <= 0)

m.c28 = Constraint(expr=1.2*m.x6/m.x11 - m.x14 <= 0)

m.c29 = Constraint(expr=1.2*m.x4/m.x7 + 1.2*m.x4/m.x8 - m.x12 <= -3)

m.c30 = Constraint(expr=1.2*m.x4/m.x9 + 1.4*m.x4/m.x10 - m.x12 <= -1)

m.c31 = Constraint(expr=1.4*m.x4/m.x11 - m.x12 <= -4)

m.c32 = Constraint(expr=1.5*m.x5/m.x7 + 1.5*m.x5/m.x8 - m.x13 <= -6)

m.c33 = Constraint(expr=1.5*m.x5/m.x11 - m.x13 <= -8)

m.c34 = Constraint(expr=1.1*m.x6/m.x7 + 1.1*m.x6/m.x8 - m.x14 <= -2)

m.c35 = Constraint(expr=1.1*m.x6/m.x9 + 1.2*m.x6/m.x10 - m.x14 <= -2)

m.c36 = Constraint(expr=1.2*m.x6/m.x11 - m.x14 <= -4)
