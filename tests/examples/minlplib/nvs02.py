#  MINLP written by GAMS Convert at 04/21/18 13:52:42
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          4        4        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          9        4        0        5        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         20        4       16        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.i1 = Var(within=Integers,bounds=(0,200),initialize=100)
m.i2 = Var(within=Integers,bounds=(0,200),initialize=100)
m.i3 = Var(within=Integers,bounds=(0,200),initialize=100)
m.i4 = Var(within=Integers,bounds=(0,200),initialize=100)
m.i5 = Var(within=Integers,bounds=(0,200),initialize=100)
m.x6 = Var(within=Reals,bounds=(0,92),initialize=0)
m.x7 = Var(within=Reals,bounds=(90,110),initialize=90)
m.x8 = Var(within=Reals,bounds=(20,25),initialize=20)

m.obj = Objective(expr=9.99999999999999e-5*(5.3578547*m.i3**2 + 0.8356891*m.i1*m.i5 + 37.293239*m.i1)
                        + 5.9207859, sense=minimize)

m.c1 = Constraint(expr=-(0.0056858*m.i2*m.i5 + 0.0006262*m.i1*m.i4 - 0.0022053*m.i3*m.i5) + m.x6 == 85.334407)

m.c2 = Constraint(expr=-(0.0071317*m.i2*m.i5 + 0.0029955*m.i1*m.i2 + 0.0021813*m.i3**2) + m.x7 == 80.51249)

m.c3 = Constraint(expr=-(0.0047026*m.i3*m.i5 + 0.0012547*m.i1*m.i3 + 0.0019085*m.i3*m.i4) + m.x8 == 9.300961)
