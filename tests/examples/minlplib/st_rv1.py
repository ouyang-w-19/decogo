#  NLP written by GAMS Convert at 04/21/18 13:54:25
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          6        1        0        5        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         11       11        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         52       42       10        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,None),initialize=0)

m.obj = Objective(expr=(-0.00055*m.x1**2) - 0.0583*m.x1 - 0.0019*m.x2**2 - 0.2318*m.x2 - 0.0002*m.x3**2 - 0.0108*m.x3 - 
                       0.00095*m.x4**2 - 0.1634*m.x4 - 0.0046*m.x5**2 - 0.138*m.x5 - 0.0035*m.x6**2 - 0.357*m.x6 - 
                       0.00315*m.x7**2 - 0.1953*m.x7 - 0.00475*m.x8**2 - 0.361*m.x8 - 0.0048*m.x9**2 - 0.1824*m.x9 - 
                       0.003*m.x10**2 - 0.162*m.x10, sense=minimize)

m.c1 = Constraint(expr=   8*m.x1 + 7*m.x2 + 9*m.x3 + 9*m.x5 + 8*m.x6 + 2*m.x7 + 4*m.x9 + m.x10 <= 530)

m.c2 = Constraint(expr=   3*m.x1 + 4*m.x2 + 6*m.x3 + 9*m.x4 + 6*m.x6 + 9*m.x7 + m.x8 + m.x10 <= 395)

m.c3 = Constraint(expr=   2*m.x2 + m.x3 + 5*m.x4 + 5*m.x5 + 7*m.x7 + 4*m.x8 + 2*m.x9 <= 350)

m.c4 = Constraint(expr=   5*m.x1 + 7*m.x3 + m.x4 + 7*m.x5 + 5*m.x6 + 7*m.x8 + 9*m.x9 + 5*m.x10 <= 405)

m.c5 = Constraint(expr=   m.x1 + m.x2 + m.x3 + m.x4 + m.x5 + m.x6 + m.x7 + m.x8 + m.x9 + m.x10 <= 200)
