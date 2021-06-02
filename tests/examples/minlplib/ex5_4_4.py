#  NLP written by GAMS Convert at 04/21/18 13:51:45
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         20       20        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         28       28        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         76       43       33        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(10,110),initialize=10)
m.x2 = Var(within=Reals,bounds=(10,110),initialize=10)
m.x3 = Var(within=Reals,bounds=(10,110),initialize=10)
m.x4 = Var(within=Reals,bounds=(10,110),initialize=10)
m.x5 = Var(within=Reals,bounds=(10,110),initialize=10)
m.x6 = Var(within=Reals,bounds=(10,110),initialize=10)
m.x7 = Var(within=Reals,bounds=(0,45),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,45),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,45),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,45),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,45),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,45),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,45),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,45),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,45),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,45),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,45),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,45),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,45),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,45),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,45),initialize=0)
m.x22 = Var(within=Reals,bounds=(100,200),initialize=100)
m.x23 = Var(within=Reals,bounds=(100,200),initialize=100)
m.x24 = Var(within=Reals,bounds=(100,200),initialize=100)
m.x25 = Var(within=Reals,bounds=(100,200),initialize=100)
m.x26 = Var(within=Reals,bounds=(100,200),initialize=100)
m.x27 = Var(within=Reals,bounds=(100,200),initialize=100)

m.obj = Objective(expr=1300*(2000/(0.333333333333333*m.x1*m.x2 + 0.166666666666667*m.x1 + 0.166666666666667*m.x2))**0.6
                        + 1300*(1000/(0.666666666666667*m.x3*m.x4 + 0.166666666666667*m.x3 + 0.166666666666667*m.x4))**
                       0.6 + 1300*(1500/(0.666666666666667*m.x5*m.x6 + 0.166666666666667*m.x5 + 0.166666666666667*m.x6))
                       **0.6, sense=minimize)

m.c1 = Constraint(expr=   m.x7 + m.x12 + m.x17 == 45)

m.c2 = Constraint(expr=   m.x7 - m.x8 + m.x14 + m.x20 == 0)

m.c3 = Constraint(expr=   m.x9 + m.x12 - m.x13 + m.x19 == 0)

m.c4 = Constraint(expr=   m.x10 + m.x15 + m.x17 - m.x18 == 0)

m.c5 = Constraint(expr= - m.x8 + m.x9 + m.x10 + m.x11 == 0)

m.c6 = Constraint(expr= - m.x13 + m.x14 + m.x15 + m.x16 == 0)

m.c7 = Constraint(expr= - m.x18 + m.x19 + m.x20 + m.x21 == 0)

m.c8 = Constraint(expr=m.x25*m.x14 + m.x27*m.x20 - m.x22*m.x8 + 100*m.x7 == 0)

m.c9 = Constraint(expr=m.x23*m.x9 + m.x27*m.x19 - m.x24*m.x13 + 100*m.x12 == 0)

m.c10 = Constraint(expr=m.x23*m.x10 + m.x25*m.x15 - m.x26*m.x18 + 100*m.x17 == 0)

m.c11 = Constraint(expr=m.x8*m.x23 - m.x8*m.x22 == 2000)

m.c12 = Constraint(expr=m.x13*m.x25 - m.x13*m.x24 == 1000)

m.c13 = Constraint(expr=m.x18*m.x27 - m.x18*m.x26 == 1500)

m.c14 = Constraint(expr=   m.x1 + m.x23 == 210)

m.c15 = Constraint(expr=   m.x2 + m.x22 == 130)

m.c16 = Constraint(expr=   m.x3 + m.x25 == 210)

m.c17 = Constraint(expr=   m.x4 + m.x24 == 160)

m.c18 = Constraint(expr=   m.x5 + m.x27 == 210)

m.c19 = Constraint(expr=   m.x6 + m.x26 == 180)
