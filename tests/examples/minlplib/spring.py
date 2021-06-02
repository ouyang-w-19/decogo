#  MINLP written by GAMS Convert at 04/21/18 13:54:18
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          9        6        0        3        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         18        6       11        1        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         44       30       14        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0.414,None),initialize=0.414)
m.x2 = Var(within=Reals,bounds=(0.207,None),initialize=0.207)
m.x3 = Var(within=Reals,bounds=(0.00178571428571429,0.02),initialize=0.00178571428571429)
m.i4 = Var(within=Integers,bounds=(1,100),initialize=1)
m.x5 = Var(within=Reals,bounds=(1.1,None),initialize=1.1)
m.x6 = Var(within=Reals,bounds=(None,None),initialize=0)
m.b7 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b8 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b9 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b10 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b11 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b12 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b13 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b14 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b15 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b16 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b17 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=(1.570796327 + 0.7853981635*m.i4)*m.x1*m.x2**2, sense=minimize)

m.c2 = Constraint(expr=-m.x1/m.x2 + m.x5 == 0)

m.c3 = Constraint(expr=-((-1 + 4*m.x5)/(-4 + 4*m.x5) + 0.615/m.x5) + m.x6 == 0)

m.c4 = Constraint(expr=2546.47908913782*m.x6*m.x5/m.x2**2 <= 189000)

m.c5 = Constraint(expr=-6.95652173913044e-7*m.x5**3*m.i4/m.x2 + m.x3 == 0)

m.c6 = Constraint(expr=(2.1 + 1.05*m.i4)*m.x2 + 1000*m.x3 <= 14)

m.c7 = Constraint(expr=   m.x1 + m.x2 <= 3)

m.c8 = Constraint(expr=   m.x2 - 0.207*m.b7 - 0.225*m.b8 - 0.244*m.b9 - 0.263*m.b10 - 0.283*m.b11 - 0.307*m.b12
                        - 0.331*m.b13 - 0.362*m.b14 - 0.394*m.b15 - 0.4375*m.b16 - 0.5*m.b17 == 0)

m.c9 = Constraint(expr=   m.b7 + m.b8 + m.b9 + m.b10 + m.b11 + m.b12 + m.b13 + m.b14 + m.b15 + m.b16 + m.b17 == 1)
