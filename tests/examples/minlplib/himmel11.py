#  NLP written by GAMS Convert at 04/21/18 13:52:24
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          5        4        1        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         10       10        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         27       11       16        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,92),initialize=0)
m.x2 = Var(within=Reals,bounds=(90,110),initialize=90)
m.x3 = Var(within=Reals,bounds=(20,25),initialize=20)
m.x4 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x5 = Var(within=Reals,bounds=(78,102),initialize=78.62)
m.x6 = Var(within=Reals,bounds=(33,45),initialize=33.44)
m.x7 = Var(within=Reals,bounds=(27,45),initialize=31.07)
m.x8 = Var(within=Reals,bounds=(27,45),initialize=44.18)
m.x9 = Var(within=Reals,bounds=(27,45),initialize=35.22)

m.obj = Objective(expr=5.3578547*m.x7**2 + 0.8356891*m.x5*m.x9 + 37.293239*m.x5 + 5000*m.x4 - 40792.141, sense=minimize)

m.c1 = Constraint(expr=   5*m.x4 - m.x5 + 7*m.x7 - m.x9 >= 0)

m.c2 = Constraint(expr=-(0.0056858*m.x6*m.x9 + 0.0006262*m.x5*m.x8 - 0.0022053*m.x7*m.x9) + m.x1 + 2*m.x4 == 85.334407)

m.c3 = Constraint(expr=-(0.0071317*m.x6*m.x9 + 0.0029955*m.x5*m.x6 + 0.0021813*m.x7**2) + m.x2 == 80.51249)

m.c4 = Constraint(expr=-(0.0047026*m.x7*m.x9 + 0.0012547*m.x5*m.x7 + 0.0019085*m.x7*m.x8) + m.x3 + 4*m.x4 == 9.300961)
