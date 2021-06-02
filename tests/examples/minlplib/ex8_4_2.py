#  NLP written by GAMS Convert at 04/21/18 13:51:47
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         11       11        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         25       25        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         81       21       60        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(-0.5,0.5),initialize=-0.328252868)
m.x2 = Var(within=Reals,bounds=(5.4,6.4),initialize=6.243266708)
m.x3 = Var(within=Reals,bounds=(0.4,1.4),initialize=0.950375356)
m.x4 = Var(within=Reals,bounds=(4.9,5.9),initialize=5.201137904)
m.x5 = Var(within=Reals,bounds=(1.3,2.3),initialize=1.592212117)
m.x6 = Var(within=Reals,bounds=(3.9,4.9),initialize=4.124052867)
m.x7 = Var(within=Reals,bounds=(2.1,3.1),initialize=2.449830504)
m.x8 = Var(within=Reals,bounds=(4.1,5.1),initialize=4.956270347)
m.x9 = Var(within=Reals,bounds=(2.8,3.8),initialize=2.867113723)
m.x10 = Var(within=Reals,bounds=(3,4),initialize=3.500210669)
m.x11 = Var(within=Reals,bounds=(3.9,4.9),initialize=4.898117627)
m.x12 = Var(within=Reals,bounds=(3.2,4.2),initialize=3.778733378)
m.x13 = Var(within=Reals,bounds=(4.7,5.7),initialize=5.691133039)
m.x14 = Var(within=Reals,bounds=(2.3,3.3),initialize=3.062250467)
m.x15 = Var(within=Reals,bounds=(5.6,6.6),initialize=5.730692483)
m.x16 = Var(within=Reals,bounds=(2.3,3.3),initialize=2.939718759)
m.x17 = Var(within=Reals,bounds=(6,7),initialize=6.159517864)
m.x18 = Var(within=Reals,bounds=(1.9,2.9),initialize=2.150080533)
m.x19 = Var(within=Reals,bounds=(6.9,7.9),initialize=7.568928609)
m.x20 = Var(within=Reals,bounds=(1,2),initialize=1.435356381)
m.x21 = Var(within=Reals,bounds=(0,10),initialize=3.59700266)
m.x22 = Var(within=Reals,bounds=(-2,2),initialize=-0.594234528)
m.x23 = Var(within=Reals,bounds=(-2,2),initialize=-1.47403364)
m.x24 = Var(within=Reals,bounds=(-2,2),initialize=-1.399592848)

m.obj = Objective(expr=m.x1**2 + (-5.9 + m.x2)**2 + (-0.9 + m.x3)**2 + (-5.4 + m.x4)**2 + (-1.8 + m.x5)**2 + (-4.4 + 
                       m.x6)**2 + (-2.6 + m.x7)**2 + (-4.6 + m.x8)**2 + (-3.3 + m.x9)**2 + (-3.5 + m.x10)**2 + (-4.4 + 
                       m.x11)**2 + (-3.7 + m.x12)**2 + (-5.2 + m.x13)**2 + (-2.8 + m.x14)**2 + (-6.1 + m.x15)**2 + (-2.8
                        + m.x16)**2 + (-6.5 + m.x17)**2 + (-2.4 + m.x18)**2 + (-7.4 + m.x19)**2 + (-1.5 + m.x20)**2
                       , sense=minimize)

m.c2 = Constraint(expr=m.x22*m.x1 + m.x1**2*m.x23 + m.x1**3*m.x24 - m.x2 + m.x21 == 0)

m.c3 = Constraint(expr=m.x22*m.x3 + m.x3**2*m.x23 + m.x3**3*m.x24 - m.x4 + m.x21 == 0)

m.c4 = Constraint(expr=m.x22*m.x5 + m.x5**2*m.x23 + m.x5**3*m.x24 - m.x6 + m.x21 == 0)

m.c5 = Constraint(expr=m.x22*m.x7 + m.x7**2*m.x23 + m.x7**3*m.x24 - m.x8 + m.x21 == 0)

m.c6 = Constraint(expr=m.x22*m.x9 + m.x9**2*m.x23 + m.x9**3*m.x24 - m.x10 + m.x21 == 0)

m.c7 = Constraint(expr=m.x22*m.x11 + m.x11**2*m.x23 + m.x11**3*m.x24 - m.x12 + m.x21 == 0)

m.c8 = Constraint(expr=m.x22*m.x13 + m.x13**2*m.x23 + m.x13**3*m.x24 - m.x14 + m.x21 == 0)

m.c9 = Constraint(expr=m.x22*m.x15 + m.x15**2*m.x23 + m.x15**3*m.x24 - m.x16 + m.x21 == 0)

m.c10 = Constraint(expr=m.x22*m.x17 + m.x17**2*m.x23 + m.x17**3*m.x24 - m.x18 + m.x21 == 0)

m.c11 = Constraint(expr=m.x22*m.x19 + m.x19**2*m.x23 + m.x19**3*m.x24 - m.x20 + m.x21 == 0)
