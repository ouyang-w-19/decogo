#  NLP written by GAMS Convert at 04/21/18 13:54:23
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          9        1        0        8        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          5        5        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         37       33        4        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,None),initialize=0)

m.obj = Objective(expr=(0.217796 + 0.813396*m.x1 + 0.67444*m.x2 + 0.305038*m.x3 + 0.129742*m.x4)*(0.091947 + 0.224508*
                       m.x1 + 0.063458*m.x2 + 0.93223*m.x3 + 0.528736*m.x4), sense=minimize)

m.c1 = Constraint(expr=   0.488509*m.x1 + 0.063565*m.x2 + 0.945686*m.x3 + 0.210704*m.x4 <= 3.562809)

m.c2 = Constraint(expr= - 0.324014*m.x1 - 0.501754*m.x2 - 0.719204*m.x3 + 0.099562*m.x4 <= -0.052215)

m.c3 = Constraint(expr=   0.445225*m.x1 - 0.346896*m.x2 + 0.637939*m.x3 - 0.257623*m.x4 <= 0.42792)

m.c4 = Constraint(expr= - 0.202821*m.x1 + 0.647361*m.x2 + 0.920135*m.x3 + 0.983091*m.x4 <= 0.84095)

m.c5 = Constraint(expr= - 0.88642*m.x1 - 0.802444*m.x2 - 0.305441*m.x3 - 0.180123*m.x4 <= -1.353686)

m.c6 = Constraint(expr= - 0.515399*m.x1 - 0.42482*m.x2 + 0.897498*m.x3 + 0.187268*m.x4 <= 2.137251)

m.c7 = Constraint(expr= - 0.591515*m.x1 + 0.060581*m.x2 - 0.427365*m.x3 + 0.579388*m.x4 <= -0.290987)

m.c8 = Constraint(expr=   0.423524*m.x1 + 0.940496*m.x2 - 0.437944*m.x3 - 0.742941*m.x4 <= 0.37362)
