#  NLP written by GAMS Convert at 04/21/18 13:52:23
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         25        1       14       10        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         64       64        0        0        0        0        0        0
#  FX      4        4        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        162      142       20        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,0.067),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,0.067),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,0.067),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,0.067),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,0.033),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,0.3),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,0.15),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,0.1),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,0.34),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,0.35),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,1.39),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,1.06),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,2.62),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,3.73),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,0.62),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,2.3),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,1.03),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,0.12),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,1.45),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,1.46),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,0.48),initialize=0)
m.x34 = Var(within=Reals,bounds=(0,0.14),initialize=0)
m.x35 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x36 = Var(within=Reals,bounds=(0,0.1),initialize=0)
m.x37 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x38 = Var(within=Reals,bounds=(0,0.48),initialize=0)
m.x39 = Var(within=Reals,bounds=(0,0.8),initialize=0)
m.x40 = Var(within=Reals,bounds=(0,2.475),initialize=0)
m.x41 = Var(within=Reals,bounds=(0,3.7125),initialize=0)
m.x42 = Var(within=Reals,bounds=(0,0.297),initialize=0)
m.x43 = Var(within=Reals,bounds=(0,0.7128),initialize=0)
m.x44 = Var(within=Reals,bounds=(0,9.6525),initialize=0)
m.x45 = Var(within=Reals,bounds=(0,2.5245),initialize=0)
m.x46 = Var(within=Reals,bounds=(0,1.7028),initialize=0)
m.x47 = Var(within=Reals,bounds=(0,1.4256),initialize=0)
m.x48 = Var(within=Reals,bounds=(0,0.5148),initialize=0)
m.x49 = Var(within=Reals,bounds=(0,99),initialize=0)
m.x50 = Var(within=Reals,bounds=(2.2,2.2),initialize=2.2)
m.x51 = Var(within=Reals,bounds=(0.2,0.2),initialize=0.2)
m.x52 = Var(within=Reals,bounds=(1.47,1.47),initialize=1.47)
m.x53 = Var(within=Reals,bounds=(1.38,1.38),initialize=1.38)
m.x54 = Var(within=Reals,bounds=(0.2,None),initialize=0.2)
m.x55 = Var(within=Reals,bounds=(0.2,None),initialize=0.2)
m.x56 = Var(within=Reals,bounds=(0.2,None),initialize=0.2)
m.x57 = Var(within=Reals,bounds=(0.2,None),initialize=0.2)
m.x58 = Var(within=Reals,bounds=(0.2,None),initialize=0.2)
m.x59 = Var(within=Reals,bounds=(0.2,None),initialize=0.2)
m.x60 = Var(within=Reals,bounds=(0.2,None),initialize=0.2)
m.x61 = Var(within=Reals,bounds=(0.2,None),initialize=0.2)
m.x62 = Var(within=Reals,bounds=(0.2,None),initialize=0.2)
m.x63 = Var(within=Reals,bounds=(0.2,None),initialize=0.2)

m.obj = Objective(expr=-(-4.84/m.x50 - 0.14/m.x51 - 6.4827/m.x52 - 6.6654/m.x53 - 8.89583741831423*m.x54**(-
                       0.666666666666667) - 20.7788808225955*m.x55**(-0.515151515151515) - 12.8222379289592*m.x56**(-
                       0.538461538461538) - 112.274462577384*m.x57**(-0.123595505617978) - 78.984522912416*m.x58**(-
                       0.538461538461538) - 325.606233858943*m.x59**(-0.19047619047619) - 19.9925533406708*m.x60**(-
                       0.492537313432836) - 20.2959676146409*m.x61**(-0.851851851851852) - 34.6492709112034*m.x62**(-
                       1.32558139534884) - 2.07326743881507*m.x63**(-0.754385964912281) - (0.0372*m.x44 - 
                       6.47537234042553*log(1 - 0.102564102564103*m.x44) - 0.489999999999999*log(1 - 1.38888888888889*
                       m.x43) - 1.68*log(1 - 0.392156862745098*m.x45) - 1.2271875*log(1 - 0.581395348837209*m.x46) - 
                       0.2187*m.x46 - 0.979999999999999*log(1 - 0.694444444444444*m.x47) - 0.35*log(1 - 1.92307692307692
                       *m.x48))) + 0.25*m.x1 + 2.29*m.x2 + 2.22*m.x3 + 2.03*m.x4 + 1.96*m.x5 + 2.13*m.x6 + 0.4*m.x7
                        + 0.9*m.x8 + 1.15*m.x9 + 1.1*m.x10 + 1.1*m.x11 + 0.8*m.x12 + 0.8*m.x13 + 0.65*m.x14 + 0.7*m.x15
                        + 0.65*m.x16 + 1.5*m.x18 + 0.72*m.x19 + 0.46*m.x20 + 2.12*m.x21 + 1.08*m.x22 + 1.01*m.x23
                        + 0.82*m.x24 + 0.75*m.x25 + 0.04*m.x26 + 0.86*m.x27 + 0.14*m.x28 + 0.64*m.x29 + 0.77*m.x30
                        + 0.05*m.x31 + 0.94*m.x32 + 0.53*m.x33 + 0.31*m.x34 + 0.58*m.x35 + 0.7*m.x36 + 1.91*m.x37
                        + 0.43*m.x38 + 6*m.x39 + 2*m.x49, sense=minimize)

m.c1 = Constraint(expr=   m.x1 + m.x2 + m.x3 + m.x4 + m.x5 + m.x6 - m.x40 <= 0)

m.c2 = Constraint(expr=   m.x7 + m.x8 + m.x9 + m.x10 + m.x11 + m.x12 + m.x13 + m.x14 + m.x15 + m.x16 - m.x41 <= 0)

m.c3 = Constraint(expr=   m.x17 + m.x18 - m.x42 <= 0)

m.c4 = Constraint(expr=   m.x19 + m.x20 - m.x43 <= 0)

m.c5 = Constraint(expr=   m.x21 + m.x22 + m.x23 + m.x24 + m.x25 + m.x26 - m.x44 <= 0)

m.c6 = Constraint(expr=   m.x27 + m.x28 + m.x29 - m.x45 <= 0)

m.c7 = Constraint(expr=   m.x30 + m.x31 + m.x32 - m.x46 <= 0)

m.c8 = Constraint(expr=   m.x33 + m.x34 + m.x35 + m.x36 + m.x37 - m.x47 <= 0)

m.c9 = Constraint(expr=   m.x38 - m.x48 <= 0)

m.c10 = Constraint(expr=   m.x39 - m.x49 <= 0)

m.c11 = Constraint(expr=   m.x1 - m.x50 >= 0)

m.c12 = Constraint(expr=   m.x17 - m.x51 >= 0)

m.c13 = Constraint(expr=   m.x7 - m.x52 >= 0)

m.c14 = Constraint(expr=   m.x8 - m.x53 >= 0)

m.c15 = Constraint(expr=   m.x9 + m.x18 + m.x21 - m.x54 >= 0)

m.c16 = Constraint(expr=   m.x2 + m.x10 + m.x22 - m.x55 >= 0)

m.c17 = Constraint(expr=   m.x3 + m.x11 + m.x19 + m.x23 - m.x56 >= 0)

m.c18 = Constraint(expr=   m.x4 + m.x24 - m.x57 >= 0)

m.c19 = Constraint(expr=   m.x5 + m.x12 + m.x20 + m.x25 + m.x27 + m.x30 + m.x33 + m.x39 - m.x58 >= 0)

m.c20 = Constraint(expr=   m.x26 + m.x28 + m.x31 - m.x59 >= 0)

m.c21 = Constraint(expr=   m.x13 + m.x29 + m.x34 - m.x60 >= 0)

m.c22 = Constraint(expr=   m.x14 + m.x35 - m.x61 >= 0)

m.c23 = Constraint(expr=   m.x6 + m.x15 + m.x32 + m.x36 + m.x38 - m.x62 >= 0)

m.c24 = Constraint(expr=   m.x16 + m.x37 - m.x63 >= 0)
