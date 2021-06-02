#  NLP written by GAMS Convert at 04/21/18 13:51:34
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          3        2        1        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          5        5        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         12        6        6        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(50,200),initialize=50)
m.x2 = Var(within=Reals,bounds=(37.5,150),initialize=37.5)
m.x3 = Var(within=Reals,bounds=(45,180),initialize=45)
m.x4 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=0.00533*m.x1**2 + 11.669*m.x1 + 0.00889*m.x2**2 + 10.333*m.x2 + 0.00741*m.x3**2 + 10.833*m.x3
                        + 653.1, sense=minimize)

m.c2 = Constraint(expr=-(0.01*(0.0676*m.x1*m.x1 + 0.00953*m.x1*m.x2 - 0.00507*m.x1*m.x3 + 0.00953*m.x2*m.x1 + 0.0521*
                       m.x2*m.x2 + 0.00901*m.x2*m.x3 - 0.00507*m.x3*m.x1 + 0.00901*m.x3*m.x2 + 0.0294*m.x3*m.x3) - 
                       0.000766*m.x1 - 3.42e-5*m.x2 + 0.000189*m.x3) + m.x4 == 0.040357)

m.c3 = Constraint(expr=   m.x1 + m.x2 + m.x3 - m.x4 >= 210)
