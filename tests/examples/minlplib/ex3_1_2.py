#  NLP written by GAMS Convert at 04/21/18 13:51:44
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          7        1        0        6        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          6        6        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         30        1       29        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(78,102),initialize=78)
m.x2 = Var(within=Reals,bounds=(33,45),initialize=33)
m.x3 = Var(within=Reals,bounds=(27,45),initialize=29.9953)
m.x4 = Var(within=Reals,bounds=(27,45),initialize=45)
m.x5 = Var(within=Reals,bounds=(27,45),initialize=36.7758)

m.obj = Objective(expr=0.8356891*m.x1*m.x5 + 37.293239*m.x1 + 5.3578547*m.x3*m.x3 - 40792.141, sense=minimize)

m.c2 = Constraint(expr=0.0056858*m.x2*m.x5 - 0.0022053*m.x3*m.x5 + 0.0006262*m.x1*m.x4 <= 6.665593)

m.c3 = Constraint(expr=0.0022053*m.x3*m.x5 - 0.0056858*m.x2*m.x5 - 0.0006262*m.x1*m.x4 <= 85.334407)

m.c4 = Constraint(expr=0.0071317*m.x2*m.x5 + 0.0021813*m.x3*m.x3 + 0.0029955*m.x1*m.x2 <= 29.48751)

m.c5 = Constraint(expr=(-0.0071317*m.x2*m.x5) - 0.0021813*m.x3*m.x3 - 0.0029955*m.x1*m.x2 <= -9.48751)

m.c6 = Constraint(expr=0.0047026*m.x3*m.x5 + 0.0019085*m.x3*m.x4 + 0.0012547*m.x1*m.x3 <= 15.599039)

m.c7 = Constraint(expr=(-0.0047026*m.x3*m.x5) - 0.0019085*m.x3*m.x4 - 0.0012547*m.x1*m.x3 <= -10.699039)
