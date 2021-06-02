#  NLP written by GAMS Convert at 04/21/18 13:51:47
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          9        9        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         15       15        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         65        9       56        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,1),initialize=0.171747132)
m.x2 = Var(within=Reals,bounds=(0,1),initialize=0.843266708)
m.x3 = Var(within=Reals,bounds=(0,1),initialize=0.550375356)
m.x4 = Var(within=Reals,bounds=(0,1),initialize=0.301137904)
m.x5 = Var(within=Reals,bounds=(0,1),initialize=0.292212117)
m.x6 = Var(within=Reals,bounds=(0,1),initialize=0.224052867)
m.x7 = Var(within=Reals,bounds=(0,1),initialize=0.349830504)
m.x8 = Var(within=Reals,bounds=(0,1),initialize=0.856270347)
m.x9 = Var(within=Reals,bounds=(-10,10),initialize=0.355)
m.x10 = Var(within=Reals,bounds=(-10,10),initialize=2.007)
m.x11 = Var(within=Reals,bounds=(-10,10),initialize=-4.575)
m.x12 = Var(within=Reals,bounds=(0,0.5),initialize=0.015)
m.x13 = Var(within=Reals,bounds=(0,0.5),initialize=0.11)
m.x14 = Var(within=Reals,bounds=(0,0.5),initialize=0.285)

m.obj = Objective(expr=((-0.1622 + m.x1)/m.x1)**2 + ((-0.6791 + m.x2)/m.x2)**2 + ((-0.679 + m.x3)/m.x3)**2 + ((-0.3875
                        + m.x4)/m.x4)**2 + ((-0.1822 + m.x5)/m.x5)**2 + ((-0.1249 + m.x6)/m.x6)**2 + ((-0.0857 + m.x7)/
                       m.x7)**2 + ((-0.0616 + m.x8)/m.x8)**2, sense=minimize)

m.c2 = Constraint(expr=exp(-4*m.x12)*m.x9 + exp(-4*m.x13)*m.x10 + exp(-4*m.x14)*m.x11 - m.x1 == 0)

m.c3 = Constraint(expr=exp(-8*m.x12)*m.x9 + exp(-8*m.x13)*m.x10 + exp(-8*m.x14)*m.x11 - m.x2 == 0)

m.c4 = Constraint(expr=exp(-12*m.x12)*m.x9 + exp(-12*m.x13)*m.x10 + exp(-12*m.x14)*m.x11 - m.x3 == 0)

m.c5 = Constraint(expr=exp(-24*m.x12)*m.x9 + exp(-24*m.x13)*m.x10 + exp(-24*m.x14)*m.x11 - m.x4 == 0)

m.c6 = Constraint(expr=exp(-48*m.x12)*m.x9 + exp(-48*m.x13)*m.x10 + exp(-48*m.x14)*m.x11 - m.x5 == 0)

m.c7 = Constraint(expr=exp(-72*m.x12)*m.x9 + exp(-72*m.x13)*m.x10 + exp(-72*m.x14)*m.x11 - m.x6 == 0)

m.c8 = Constraint(expr=exp(-94*m.x12)*m.x9 + exp(-94*m.x13)*m.x10 + exp(-94*m.x14)*m.x11 - m.x7 == 0)

m.c9 = Constraint(expr=exp(-118*m.x12)*m.x9 + exp(-118*m.x13)*m.x10 + exp(-118*m.x14)*m.x11 - m.x8 == 0)
