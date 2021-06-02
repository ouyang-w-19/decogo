#  NLP written by GAMS Convert at 04/21/18 13:51:16
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         10        0        0       10        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          3        3        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         30        0       30        0


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(None,None),initialize=5.155228315)
m.x2 = Var(within=Reals,bounds=(None,None),initialize=5.793541075)
m.x3 = Var(within=Reals,bounds=(0,None),initialize=5.49209550544626)

m.obj = Objective(expr=m.x3, sense=minimize)

m.c1 = Constraint(expr=(2.545724188 - m.x1)**2 + (9.983058643 - m.x2)**2 - m.x3**2 <= 0)

m.c2 = Constraint(expr=(8.589400372 - m.x1)**2 + (6.208600402 - m.x2)**2 - m.x3**2 <= 0)

m.c3 = Constraint(expr=(5.953378204 - m.x1)**2 + (9.920197351 - m.x2)**2 - m.x3**2 <= 0)

m.c4 = Constraint(expr=(3.710241136 - m.x1)**2 + (7.860254203 - m.x2)**2 - m.x3**2 <= 0)

m.c5 = Constraint(expr=(3.629909053 - m.x1)**2 + (2.176232347 - m.x2)**2 - m.x3**2 <= 0)

m.c6 = Constraint(expr=(3.016475803 - m.x1)**2 + (6.757468831 - m.x2)**2 - m.x3**2 <= 0)

m.c7 = Constraint(expr=(4.148474536 - m.x1)**2 + (2.435660776 - m.x2)**2 - m.x3**2 <= 0)

m.c8 = Constraint(expr=(8.706433123 - m.x1)**2 + (3.250724797 - m.x2)**2 - m.x3**2 <= 0)

m.c9 = Constraint(expr=(1.604023507 - m.x1)**2 + (7.020357481 - m.x2)**2 - m.x3**2 <= 0)

m.c10 = Constraint(expr=(5.501896021 - m.x1)**2 + (4.918207429 - m.x2)**2 - m.x3**2 <= 0)
