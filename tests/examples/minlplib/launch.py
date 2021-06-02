#  NLP written by GAMS Convert at 04/21/18 13:52:28
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         29       23        0        6        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         39       39        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        108       56       52        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x2 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x3 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x4 = Var(within=Reals,bounds=(5,None),initialize=136)
m.x5 = Var(within=Reals,bounds=(5,None),initialize=47)
m.x6 = Var(within=Reals,bounds=(5,None),initialize=16)
m.x7 = Var(within=Reals,bounds=(50,None),initialize=2176)
m.x8 = Var(within=Reals,bounds=(50,None),initialize=564)
m.x9 = Var(within=Reals,bounds=(50,None),initialize=144)
m.x10 = Var(within=Reals,bounds=(2.5,4),initialize=2.5)
m.x11 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x12 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x13 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x14 = Var(within=Reals,bounds=(125,150),initialize=125)
m.x15 = Var(within=Reals,bounds=(75,100),initialize=75)
m.x16 = Var(within=Reals,bounds=(50,70),initialize=50)
m.x17 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x18 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x19 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x20 = Var(within=Reals,bounds=(20,None),initialize=746)
m.x21 = Var(within=Reals,bounds=(20,None),initialize=96)
m.x22 = Var(within=Reals,bounds=(20,None),initialize=129)
m.x23 = Var(within=Reals,bounds=(0.25,0.3),initialize=0.3)
m.x24 = Var(within=Reals,bounds=(0.24,0.29),initialize=0.29)
m.x25 = Var(within=Reals,bounds=(0.16,0.21),initialize=0.21)
m.x26 = Var(within=Reals,bounds=(1.2,1.4),initialize=1.2)
m.x27 = Var(within=Reals,bounds=(0.6,0.75),initialize=0.6)
m.x28 = Var(within=Reals,bounds=(0.7,0.9),initialize=0.7)
m.x29 = Var(within=Reals,bounds=(100,None),initialize=155)
m.x30 = Var(within=Reals,bounds=(100,None),initialize=314)
m.x31 = Var(within=Reals,bounds=(100,None),initialize=403)
m.x32 = Var(within=Reals,bounds=(240,290),initialize=240)
m.x33 = Var(within=Reals,bounds=(240,290),initialize=240)
m.x34 = Var(within=Reals,bounds=(340,375),initialize=340)
m.x35 = Var(within=Reals,bounds=(1000,None),initialize=1000)
m.x36 = Var(within=Reals,bounds=(1000,None),initialize=1000)
m.x37 = Var(within=Reals,bounds=(1000,None),initialize=1000)
m.x38 = Var(within=Reals,bounds=(35000,50000),initialize=38632)

m.obj = Objective(expr=5272.77*(m.x1**1.2781*m.x4**(-0.1959)*m.x23**2.4242*m.x17**0.38745*m.x7**(-0.9904) + m.x2**1.2781
                       *m.x5**(-0.1959)*m.x24**2.4242*m.x18**0.38745*m.x8**(-0.9904) + m.x3**1.2781*m.x6**(-0.1959)*
                       m.x25**2.4242*m.x19**0.38745*m.x9**(-0.9904)) + 0.185214*(10.3027592771433*m.x1**0.3322*m.x23**(-
                       1.5935)*m.x7**0.2362*m.x14**0.1079 + 10.3027592771433*m.x2**0.3322*m.x24**(-1.5935)*m.x8**0.2362*
                       m.x15**0.1079 + 7.94328234724281*m.x3**0.3322*m.x25**(-1.5935)*m.x9**0.2362*m.x16**0.1079) + 
                       160.99*(0.001*m.x20)**(-0.146) + 282.874*(0.001*m.x20)**0.648 + 160.99*(0.001*m.x21)**(-0.146) + 
                       282.874*(0.001*m.x21)**0.648 + 181.806*(0.001*m.x22)**0.539 + 232.57*(0.001*m.x22)**0.772 + 
                       38.0226256753606*(2.509*(0.001*m.x20)**0.736 + 0.0002085*m.x20 + 0.9744*(0.001*m.x20)**(-0.229))
                        + 38.0226256753606*(2.509*(0.001*m.x21)**0.736 + 0.0002085*m.x21 + 0.9744*(0.001*m.x21)**(-0.229
                       )) + 8.51138038202377*(7.05e-5*m.x22 - 0.000845197400305967*(0.001*m.x22)**(-1.33) + 
                       52.5264761174087*(0.001*m.x22)**0.498) + 0.1637577*(1000*m.x10)**0.786 + 0.125678613298076*(1000*
                       m.x10)**0.786 + 85*(0.003*m.x7 + 0.003*m.x8 + 0.003*m.x9)**0.46 - 850.76, sense=minimize)

m.c1 = Constraint(expr= - m.x1 + 0.5*m.x4 == 0)

m.c2 = Constraint(expr= - m.x2 + 0.6*m.x5 == 0)

m.c3 = Constraint(expr= - m.x3 + 0.7*m.x6 == 0)

m.c4 = Constraint(expr= - m.x4 - m.x5 - m.x6 - m.x7 - m.x8 - m.x9 - m.x10 + m.x11 == 20)

m.c5 = Constraint(expr= - m.x5 - m.x6 - m.x8 - m.x9 - m.x10 + m.x12 == 20)

m.c6 = Constraint(expr= - m.x6 - m.x9 - m.x10 + m.x13 == 20)

m.c7 = Constraint(expr=   m.x17 - 5*m.x20 == 0)

m.c8 = Constraint(expr=   m.x18 - 5*m.x21 == 0)

m.c9 = Constraint(expr=   m.x19 - m.x22 == 0)

m.c10 = Constraint(expr=m.x26*m.x11 - m.x17 == 0)

m.c11 = Constraint(expr=m.x27*m.x12 - m.x18 == 0)

m.c12 = Constraint(expr=m.x28*m.x13 - m.x19 == 0)

m.c13 = Constraint(expr=(1 - m.x23)*m.x11 - m.x7 == 0)

m.c14 = Constraint(expr=(1 - m.x24)*m.x12 - m.x8 == 0)

m.c15 = Constraint(expr=(1 - m.x25)*m.x13 - m.x9 == 0)

m.c16 = Constraint(expr=   12*m.x4 - m.x7 <= 0)

m.c17 = Constraint(expr=   10*m.x5 - m.x8 <= 0)

m.c18 = Constraint(expr=   7*m.x6 - m.x9 <= 0)

m.c19 = Constraint(expr= - 16*m.x4 + m.x7 <= 0)

m.c20 = Constraint(expr= - 12*m.x5 + m.x8 <= 0)

m.c21 = Constraint(expr= - 9*m.x6 + m.x9 <= 0)

m.c22 = Constraint(expr=m.x32*m.x7 - m.x17*m.x29 == 0)

m.c23 = Constraint(expr=m.x33*m.x8 - m.x18*m.x30 == 0)

m.c24 = Constraint(expr=m.x34*m.x9 - m.x19*m.x31 == 0)

m.c25 = Constraint(expr=-31.8*log(1/m.x23)*m.x32 + m.x35 == 0)

m.c26 = Constraint(expr=-31.8*log(1/m.x24)*m.x33 + m.x36 == 0)

m.c27 = Constraint(expr=-31.8*log(1/m.x25)*m.x34 + m.x37 == 0)

m.c28 = Constraint(expr= - m.x35 - m.x36 - m.x37 + m.x38 == 0)
