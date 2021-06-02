#  NLP written by GAMS Convert at 04/21/18 13:51:45
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         15        1        0       14        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          8        8        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         46       11       35        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(1500,2000),initialize=1500)
m.x2 = Var(within=Reals,bounds=(1,120),initialize=1)
m.x3 = Var(within=Reals,bounds=(3000,3500),initialize=3000)
m.x4 = Var(within=Reals,bounds=(85,93),initialize=85)
m.x5 = Var(within=Reals,bounds=(90,95),initialize=90)
m.x6 = Var(within=Reals,bounds=(3,12),initialize=3)
m.x7 = Var(within=Reals,bounds=(145,162),initialize=145)

m.obj = Objective(expr=0.035*m.x1*m.x6 - 0.063*m.x3*m.x5 + 1.715*m.x1 + 4.0565*m.x3 + 10*m.x2 + 3000, sense=minimize)

m.c2 = Constraint(expr=0.0059553571*m.x6**2 + 0.88392857*m.x3/m.x1 - 0.1175625*m.x6 <= 1)

m.c3 = Constraint(expr=1.1088*m.x1/m.x3 + 0.1303533*m.x1/m.x3*m.x6 - 0.0066033*m.x1/m.x3*m.x6**2 <= 1)

m.c4 = Constraint(expr=0.00066173269*m.x6**2 - 0.019120592*m.x6 - 0.0056595559*m.x4 + 0.017239878*m.x5 <= 1)

m.c5 = Constraint(expr=56.85075/m.x5 + 1.08702*m.x6/m.x5 + 0.32175*m.x4/m.x5 - 0.03762*m.x6**2/m.x5 <= 1)

m.c6 = Constraint(expr=2462.3121*m.x2/m.x3/m.x4 - 25.125634*m.x2/m.x3 + 0.006198*m.x7 <= 1)

m.c7 = Constraint(expr=161.18996/m.x7 + 5000*m.x2/m.x3/m.x7 - 489510*m.x2/m.x3/m.x4/m.x7 <= 1)

m.c8 = Constraint(expr=44.333333/m.x5 + 0.33*m.x7/m.x5 <= 1)

m.c9 = Constraint(expr=   0.022556*m.x5 - 0.007595*m.x7 <= 1)

m.c10 = Constraint(expr= - 0.0005*m.x1 + 0.00061*m.x3 <= 1)

m.c11 = Constraint(expr=0.819672*m.x1/m.x3 + 0.819672/m.x3 <= 1)

m.c12 = Constraint(expr=24500*m.x2/m.x3/m.x4 - 250*m.x2/m.x3 <= 1)

m.c13 = Constraint(expr=1.2244898e-5*m.x3/m.x2*m.x4 + 0.010204082*m.x4 <= 1)

m.c14 = Constraint(expr=6.25e-5*m.x1*m.x6 + 6.25e-5*m.x1 - 7.625E-5*m.x3 <= 1)

m.c15 = Constraint(expr=1.22*m.x3/m.x1 + 1/m.x1 - m.x6 <= 1)
