#  NLP written by GAMS Convert at 04/21/18 13:54:11
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         18        5       13        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         11       11        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         55       26       29        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(None,None),initialize=934.032)
m.x2 = Var(within=Reals,bounds=(None,None),initialize=934.032)
m.x3 = Var(within=Reals,bounds=(None,None),initialize=1011.868)
m.x4 = Var(within=Reals,bounds=(1.05,None),initialize=1.2)
m.x5 = Var(within=Reals,bounds=(1.05,None),initialize=1.2)
m.x6 = Var(within=Reals,bounds=(1.05,None),initialize=1.3)
m.x7 = Var(within=Reals,bounds=(None,None),initialize=45.8)
m.x8 = Var(within=Reals,bounds=(None,None),initialize=43.2)
m.x9 = Var(within=Reals,bounds=(None,None),initialize=30.5)
m.x10 = Var(within=Reals,bounds=(1,None),initialize=76.3939536510076)

m.obj = Objective(expr=(0.0039*m.x7 + 0.0039*m.x8)*(495*m.x4 + 385*m.x5 + 315*m.x6)/m.x10, sense=minimize)

m.c1 = Constraint(expr=-0.5*m.x9*m.x4*(0.8*m.x7 + 0.333333333333333*m.x8) + m.x1 == 0)

m.c2 = Constraint(expr=-0.5*m.x9*m.x5*(0.8*m.x7 + 0.333333333333333*m.x8) + m.x2 == 0)

m.c3 = Constraint(expr=-0.5*m.x9*m.x6*(0.8*m.x7 + 0.333333333333333*m.x8) + m.x3 == 0)

m.c4 = Constraint(expr=-sqrt(m.x8*m.x8 - m.x9*m.x9) - m.x7 + m.x10 == 0)

m.c5 = Constraint(expr=   m.x1 - 8.4652734375*m.x10 >= 0)

m.c6 = Constraint(expr=   m.x2 - 9.65006510416667*m.x10 >= 0)

m.c7 = Constraint(expr=   m.x3 - 8.8716796875*m.x10 >= 0)

m.c8 = Constraint(expr=0.5*m.x1*m.x9 - 2.2*(8.4652734375*m.x10)**1.33333333333333 >= 0)

m.c9 = Constraint(expr=0.5*m.x2*m.x9 - 2.2*(9.65006510416667*m.x10)**1.33333333333333 >= 0)

m.c10 = Constraint(expr=0.5*m.x3*m.x9 - 2.2*(8.8716796875*m.x10)**1.33333333333333 >= 0)

m.c11 = Constraint(expr=   m.x4 - 0.0111771747883801*m.x7 >= 0.2)

m.c12 = Constraint(expr=   m.x5 - 0.0137655360411427*m.x7 >= 0.2)

m.c13 = Constraint(expr=   m.x6 - 0.0155663872253648*m.x7 >= 0.2)

m.c14 = Constraint(expr=   m.x4 - 0.0111771747883801*m.x8 >= 0.2)

m.c15 = Constraint(expr=   m.x5 - 0.0137655360411427*m.x8 >= 0.2)

m.c16 = Constraint(expr=   m.x6 - 0.0155663872253648*m.x8 >= 0.2)

m.c17 = Constraint(expr=   m.x8 - m.x9 >= 0)
