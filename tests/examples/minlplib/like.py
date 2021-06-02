#  NLP written by GAMS Convert at 04/21/18 13:52:28
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          4        2        2        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         10       10        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         17        8        9        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0.1,None),initialize=0.333333333333333)
m.x2 = Var(within=Reals,bounds=(0.1,None),initialize=0.333333333333333)
m.x3 = Var(within=Reals,bounds=(0.1,None),initialize=0.333333333333333)
m.x4 = Var(within=Reals,bounds=(0,None),initialize=130)
m.x5 = Var(within=Reals,bounds=(0,None),initialize=160)
m.x6 = Var(within=Reals,bounds=(0,None),initialize=190)
m.x7 = Var(within=Reals,bounds=(0,None),initialize=15)
m.x8 = Var(within=Reals,bounds=(0,None),initialize=15)
m.x9 = Var(within=Reals,bounds=(0,None),initialize=15)

m.obj = Objective(expr=-(log(0.398942448887604*(m.x1/m.x7*exp(-0.5*((95 - m.x4)/m.x7)**2) + m.x2/m.x8*exp(-0.5*((95 - 
                       m.x5)/m.x8)**2) + m.x3/m.x9*exp(-0.5*((95 - m.x6)/m.x9)**2))) + log(0.398942448887604*(m.x1/m.x7*
                       exp(-0.5*((105 - m.x4)/m.x7)**2) + m.x2/m.x8*exp(-0.5*((105 - m.x5)/m.x8)**2) + m.x3/m.x9*exp(-
                       0.5*((105 - m.x6)/m.x9)**2))) + 4*log(0.398942448887604*(m.x1/m.x7*exp(-0.5*((110 - m.x4)/m.x7)**
                       2) + m.x2/m.x8*exp(-0.5*((110 - m.x5)/m.x8)**2) + m.x3/m.x9*exp(-0.5*((110 - m.x6)/m.x9)**2))) + 
                       4*log(0.398942448887604*(m.x1/m.x7*exp(-0.5*((115 - m.x4)/m.x7)**2) + m.x2/m.x8*exp(-0.5*((115 - 
                       m.x5)/m.x8)**2) + m.x3/m.x9*exp(-0.5*((115 - m.x6)/m.x9)**2))) + 15*log(0.398942448887604*(m.x1/
                       m.x7*exp(-0.5*((120 - m.x4)/m.x7)**2) + m.x2/m.x8*exp(-0.5*((120 - m.x5)/m.x8)**2) + m.x3/m.x9*
                       exp(-0.5*((120 - m.x6)/m.x9)**2))) + 15*log(0.398942448887604*(m.x1/m.x7*exp(-0.5*((125 - m.x4)/
                       m.x7)**2) + m.x2/m.x8*exp(-0.5*((125 - m.x5)/m.x8)**2) + m.x3/m.x9*exp(-0.5*((125 - m.x6)/m.x9)**
                       2))) + 15*log(0.398942448887604*(m.x1/m.x7*exp(-0.5*((130 - m.x4)/m.x7)**2) + m.x2/m.x8*exp(-0.5*
                       ((130 - m.x5)/m.x8)**2) + m.x3/m.x9*exp(-0.5*((130 - m.x6)/m.x9)**2))) + 13*log(0.398942448887604
                       *(m.x1/m.x7*exp(-0.5*((135 - m.x4)/m.x7)**2) + m.x2/m.x8*exp(-0.5*((135 - m.x5)/m.x8)**2) + m.x3/
                       m.x9*exp(-0.5*((135 - m.x6)/m.x9)**2))) + 21*log(0.398942448887604*(m.x1/m.x7*exp(-0.5*((140 - 
                       m.x4)/m.x7)**2) + m.x2/m.x8*exp(-0.5*((140 - m.x5)/m.x8)**2) + m.x3/m.x9*exp(-0.5*((140 - m.x6)/
                       m.x9)**2))) + 12*log(0.398942448887604*(m.x1/m.x7*exp(-0.5*((145 - m.x4)/m.x7)**2) + m.x2/m.x8*
                       exp(-0.5*((145 - m.x5)/m.x8)**2) + m.x3/m.x9*exp(-0.5*((145 - m.x6)/m.x9)**2))) + 17*log(
                       0.398942448887604*(m.x1/m.x7*exp(-0.5*((150 - m.x4)/m.x7)**2) + m.x2/m.x8*exp(-0.5*((150 - m.x5)/
                       m.x8)**2) + m.x3/m.x9*exp(-0.5*((150 - m.x6)/m.x9)**2))) + 4*log(0.398942448887604*(m.x1/m.x7*
                       exp(-0.5*((155 - m.x4)/m.x7)**2) + m.x2/m.x8*exp(-0.5*((155 - m.x5)/m.x8)**2) + m.x3/m.x9*exp(-
                       0.5*((155 - m.x6)/m.x9)**2))) + 20*log(0.398942448887604*(m.x1/m.x7*exp(-0.5*((160 - m.x4)/m.x7)
                       **2) + m.x2/m.x8*exp(-0.5*((160 - m.x5)/m.x8)**2) + m.x3/m.x9*exp(-0.5*((160 - m.x6)/m.x9)**2)))
                        + 8*log(0.398942448887604*(m.x1/m.x7*exp(-0.5*((165 - m.x4)/m.x7)**2) + m.x2/m.x8*exp(-0.5*((165
                        - m.x5)/m.x8)**2) + m.x3/m.x9*exp(-0.5*((165 - m.x6)/m.x9)**2))) + 17*log(0.398942448887604*(
                       m.x1/m.x7*exp(-0.5*((170 - m.x4)/m.x7)**2) + m.x2/m.x8*exp(-0.5*((170 - m.x5)/m.x8)**2) + m.x3/
                       m.x9*exp(-0.5*((170 - m.x6)/m.x9)**2))) + 8*log(0.398942448887604*(m.x1/m.x7*exp(-0.5*((175 - 
                       m.x4)/m.x7)**2) + m.x2/m.x8*exp(-0.5*((175 - m.x5)/m.x8)**2) + m.x3/m.x9*exp(-0.5*((175 - m.x6)/
                       m.x9)**2))) + 6*log(0.398942448887604*(m.x1/m.x7*exp(-0.5*((180 - m.x4)/m.x7)**2) + m.x2/m.x8*
                       exp(-0.5*((180 - m.x5)/m.x8)**2) + m.x3/m.x9*exp(-0.5*((180 - m.x6)/m.x9)**2))) + 6*log(
                       0.398942448887604*(m.x1/m.x7*exp(-0.5*((185 - m.x4)/m.x7)**2) + m.x2/m.x8*exp(-0.5*((185 - m.x5)/
                       m.x8)**2) + m.x3/m.x9*exp(-0.5*((185 - m.x6)/m.x9)**2))) + 7*log(0.398942448887604*(m.x1/m.x7*
                       exp(-0.5*((190 - m.x4)/m.x7)**2) + m.x2/m.x8*exp(-0.5*((190 - m.x5)/m.x8)**2) + m.x3/m.x9*exp(-
                       0.5*((190 - m.x6)/m.x9)**2))) + 4*log(0.398942448887604*(m.x1/m.x7*exp(-0.5*((195 - m.x4)/m.x7)**
                       2) + m.x2/m.x8*exp(-0.5*((195 - m.x5)/m.x8)**2) + m.x3/m.x9*exp(-0.5*((195 - m.x6)/m.x9)**2))) + 
                       3*log(0.398942448887604*(m.x1/m.x7*exp(-0.5*((200 - m.x4)/m.x7)**2) + m.x2/m.x8*exp(-0.5*((200 - 
                       m.x5)/m.x8)**2) + m.x3/m.x9*exp(-0.5*((200 - m.x6)/m.x9)**2))) + 3*log(0.398942448887604*(m.x1/
                       m.x7*exp(-0.5*((205 - m.x4)/m.x7)**2) + m.x2/m.x8*exp(-0.5*((205 - m.x5)/m.x8)**2) + m.x3/m.x9*
                       exp(-0.5*((205 - m.x6)/m.x9)**2))) + 8*log(0.398942448887604*(m.x1/m.x7*exp(-0.5*((210 - m.x4)/
                       m.x7)**2) + m.x2/m.x8*exp(-0.5*((210 - m.x5)/m.x8)**2) + m.x3/m.x9*exp(-0.5*((210 - m.x6)/m.x9)**
                       2))) + log(0.398942448887604*(m.x1/m.x7*exp(-0.5*((215 - m.x4)/m.x7)**2) + m.x2/m.x8*exp(-0.5*((
                       215 - m.x5)/m.x8)**2) + m.x3/m.x9*exp(-0.5*((215 - m.x6)/m.x9)**2))) + 6*log(0.398942448887604*(
                       m.x1/m.x7*exp(-0.5*((220 - m.x4)/m.x7)**2) + m.x2/m.x8*exp(-0.5*((220 - m.x5)/m.x8)**2) + m.x3/
                       m.x9*exp(-0.5*((220 - m.x6)/m.x9)**2))) + 5*log(0.398942448887604*(m.x1/m.x7*exp(-0.5*((230 - 
                       m.x4)/m.x7)**2) + m.x2/m.x8*exp(-0.5*((230 - m.x5)/m.x8)**2) + m.x3/m.x9*exp(-0.5*((230 - m.x6)/
                       m.x9)**2))) + log(0.398942448887604*(m.x1/m.x7*exp(-0.5*((235 - m.x4)/m.x7)**2) + m.x2/m.x8*exp(-
                       0.5*((235 - m.x5)/m.x8)**2) + m.x3/m.x9*exp(-0.5*((235 - m.x6)/m.x9)**2))) + 7*log(
                       0.398942448887604*(m.x1/m.x7*exp(-0.5*((240 - m.x4)/m.x7)**2) + m.x2/m.x8*exp(-0.5*((240 - m.x5)/
                       m.x8)**2) + m.x3/m.x9*exp(-0.5*((240 - m.x6)/m.x9)**2))) + log(0.398942448887604*(m.x1/m.x7*exp(-
                       0.5*((245 - m.x4)/m.x7)**2) + m.x2/m.x8*exp(-0.5*((245 - m.x5)/m.x8)**2) + m.x3/m.x9*exp(-0.5*((
                       245 - m.x6)/m.x9)**2))) + 2*log(0.398942448887604*(m.x1/m.x7*exp(-0.5*((260 - m.x4)/m.x7)**2) + 
                       m.x2/m.x8*exp(-0.5*((260 - m.x5)/m.x8)**2) + m.x3/m.x9*exp(-0.5*((260 - m.x6)/m.x9)**2))))
                       , sense=minimize)

m.c2 = Constraint(expr=   m.x1 + m.x2 + m.x3 == 1)

m.c3 = Constraint(expr= - m.x4 + m.x5 >= 0)

m.c4 = Constraint(expr= - m.x5 + m.x6 >= 0)
