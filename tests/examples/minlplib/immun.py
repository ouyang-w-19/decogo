#  NLP written by GAMS Convert at 04/21/18 13:52:25
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          8        8        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         22       22        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         64       58        6        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(None,187217.324724184),initialize=187217.324724184)
m.x2 = Var(within=Reals,bounds=(0,None),initialize=956.904106888036)
m.x3 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,None),initialize=45.5987315339227)
m.x5 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,None),initialize=40.6641597628654)
m.x10 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,None),initialize=66834.2651808549)
m.x12 = Var(within=Reals,bounds=(0,None),initialize=33347.8176607291)
m.x13 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,None),initialize=18186.5732712855)
m.x15 = Var(within=Reals,bounds=(0,None),initialize=27099.21721716)
m.x16 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,None),initialize=938765.155199853)
m.x18 = Var(within=Reals,bounds=(0,None),initialize=42000)
m.x19 = Var(within=Reals,bounds=(0,None),initialize=40000)
m.x20 = Var(within=Reals,bounds=(0,None),initialize=40000)
m.x21 = Var(within=Reals,bounds=(0,None),initialize=0)

m.obj = Objective(expr=(-m.x16)**2 + (50000 - m.x17)**2 + (42000 - m.x18)**2 + (40000 - m.x19)**2 + (40000 - m.x20)**2
                        + (45000 - m.x21)**2, sense=minimize)

m.c2 = Constraint(expr= - m.x10 - m.x16 == 0)

m.c3 = Constraint(expr=   1044.80727456326*m.x2 + 1079.40354193291*m.x3 + 74.5442033113223*m.x4 + 36.3324688408125*m.x5
                        + 41.3438438533384*m.x6 + 43.2231094830356*m.x7 + 43.8495313596014*m.x8 + 59.5100782737447*m.x9
                        + 1.00940093153723*m.x10 - m.x11 - m.x17 == 0)

m.c4 = Constraint(expr=   75.57763951196*m.x4 + 36.8361604344007*m.x5 + 41.9170101494904*m.x6 + 43.8223287926491*m.x7
                        + 44.4574350070353*m.x8 + 60.3350903666908*m.x9 + 1.0391091639109*m.x11 - m.x12 - m.x18 == 0)

m.c5 = Constraint(expr=   75.456505608033*m.x4 + 36.7771203803858*m.x5 + 41.8498266397494*m.x6 + 43.7520914870108*m.x7
                        + 44.3861797694312*m.x8 + 60.2383868299423*m.x9 + 1.02284761238063*m.x12 - m.x13 - m.x19 == 0)

m.c6 = Constraint(expr=   1167.30216560492*m.x4 + 74.4548991299823*m.x5 + 84.7245403892903*m.x6 + 88.5756558615307*m.x7
                        + 89.8593610189442*m.x8 + 121.951989954281*m.x9 + 1.05*m.x13 - m.x14 - m.x20 == 0)

m.c7 = Constraint(expr=   1115.8195763046*m.x5 + 1126.3428356729*m.x6 + 134.503508270593*m.x7 + 136.452834477414*m.x8
                        + 185.185989647919*m.x9 + 1.07600174350434*m.x14 - m.x15 - m.x21 == 0)

m.c8 = Constraint(expr=   m.x1 - 40.9351218608642*m.x2 - 43.2018652628815*m.x3 - 45.3473311101868*m.x4
                        - 39.805625287987*m.x5 - 41.3125769494053*m.x6 - 41.8781498541141*m.x7 - 42.1403213448084*m.x8
                        - 46.6038914670337*m.x9 == 0)
