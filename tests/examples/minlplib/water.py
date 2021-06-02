#  DNLP written by GAMS Convert at 04/21/18 13:55:13
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         26       26        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         42       42        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        113       67       46        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x2 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x3 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x4 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x5 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x6 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x7 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x8 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x9 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x10 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x11 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x12 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x13 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x14 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x15 = Var(within=Reals,bounds=(0.15,2),initialize=0.547722557505166)
m.x16 = Var(within=Reals,bounds=(0.15,2),initialize=0.547722557505166)
m.x17 = Var(within=Reals,bounds=(0.15,2),initialize=0.547722557505166)
m.x18 = Var(within=Reals,bounds=(0.15,2),initialize=0.547722557505166)
m.x19 = Var(within=Reals,bounds=(0.15,2),initialize=0.547722557505166)
m.x20 = Var(within=Reals,bounds=(0.15,2),initialize=0.547722557505166)
m.x21 = Var(within=Reals,bounds=(0.15,2),initialize=0.547722557505166)
m.x22 = Var(within=Reals,bounds=(0.15,2),initialize=0.547722557505166)
m.x23 = Var(within=Reals,bounds=(0.15,2),initialize=0.547722557505166)
m.x24 = Var(within=Reals,bounds=(0.15,2),initialize=0.547722557505166)
m.x25 = Var(within=Reals,bounds=(0.15,2),initialize=0.547722557505166)
m.x26 = Var(within=Reals,bounds=(0.15,2),initialize=0.547722557505166)
m.x27 = Var(within=Reals,bounds=(0.15,2),initialize=0.547722557505166)
m.x28 = Var(within=Reals,bounds=(0.15,2),initialize=0.547722557505166)
m.x29 = Var(within=Reals,bounds=(6.5,None),initialize=7.5)
m.x30 = Var(within=Reals,bounds=(3.25,None),initialize=4.25)
m.x31 = Var(within=Reals,bounds=(16.58,None),initialize=17.58)
m.x32 = Var(within=Reals,bounds=(14.92,None),initialize=15.92)
m.x33 = Var(within=Reals,bounds=(12.925,None),initialize=13.925)
m.x34 = Var(within=Reals,bounds=(12.26,None),initialize=13.26)
m.x35 = Var(within=Reals,bounds=(8.76,None),initialize=9.76)
m.x36 = Var(within=Reals,bounds=(16.08,None),initialize=17.08)
m.x37 = Var(within=Reals,bounds=(0,2.5),initialize=0.961470588235294)
m.x38 = Var(within=Reals,bounds=(0,6),initialize=2.30752941176471)
m.x39 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x40 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x41 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=   10*m.x39 + m.x40 + 10*m.x41, sense=minimize)

m.c1 = Constraint(expr= - m.x1 - m.x2 - m.x3 + m.x37 == 0)

m.c2 = Constraint(expr= - m.x4 - m.x5 - m.x6 - m.x7 + m.x38 == 0)

m.c3 = Constraint(expr=   m.x1 + m.x4 - m.x8 - m.x9 - m.x10 - m.x11 == 1.212)

m.c4 = Constraint(expr=   m.x2 + m.x8 + m.x12 == 0.452)

m.c5 = Constraint(expr=   m.x9 - m.x12 + m.x13 == 0.245)

m.c6 = Constraint(expr=   m.x5 + m.x10 - m.x13 - m.x14 == 0.652)

m.c7 = Constraint(expr=   m.x6 + m.x14 == 0.252)

m.c8 = Constraint(expr=   m.x3 + m.x7 + m.x11 == 0.456)

m.c9 = Constraint(expr=-1.5722267648148*abs(m.x1)*m.x1/m.x15**5.33 + m.x29 - m.x31 == 0)

m.c10 = Constraint(expr=-1.32004857865156*abs(m.x2)*m.x2/m.x16**5.33 + m.x29 - m.x32 == 0)

m.c11 = Constraint(expr=-2.57705917665854*abs(m.x3)*m.x3/m.x17**5.33 + m.x29 - m.x36 == 0)

m.c12 = Constraint(expr=-2.06257339263358*abs(m.x4)*m.x4/m.x18**5.33 + m.x30 - m.x31 == 0)

m.c13 = Constraint(expr=-2.40235218067626*abs(m.x5)*m.x5/m.x19**5.33 + m.x30 - m.x34 == 0)

m.c14 = Constraint(expr=-1.339*abs(m.x6)*m.x6/m.x20**5.33 + m.x30 - m.x35 == 0)

m.c15 = Constraint(expr=-1.37419139860501*abs(m.x7)*m.x7/m.x21**5.33 + m.x30 - m.x36 == 0)

m.c16 = Constraint(expr=-1.2916134290104*abs(m.x8)*m.x8/m.x22**5.33 + m.x31 - m.x32 == 0)

m.c17 = Constraint(expr=-1.60230396616872*abs(m.x9)*m.x9/m.x23**5.33 + m.x31 - m.x33 == 0)

m.c18 = Constraint(expr=-1.339*abs(m.x10)*m.x10/m.x24**5.33 + m.x31 - m.x34 == 0)

m.c19 = Constraint(expr=-2.14329116080854*abs(m.x11)*m.x11/m.x25**5.33 + m.x31 - m.x36 == 0)

m.c20 = Constraint(expr=-1.24561882211213*abs(m.x12)*m.x12/m.x26**5.33 - m.x32 + m.x33 == 0)

m.c21 = Constraint(expr=-1.15157500841239*abs(m.x13)*m.x13/m.x27**5.33 - m.x33 + m.x34 == 0)

m.c22 = Constraint(expr=-2.06257339263358*abs(m.x14)*m.x14/m.x28**5.33 + m.x34 - m.x35 == 0)

m.c23 = Constraint(expr=-(1.02*m.x37*(-6.5 + m.x29) + 1.02*m.x38*(-3.25 + m.x30)) + m.x39 == 0)

m.c24 = Constraint(expr=-0.069*(1526.43375224737*m.x15**1.29 + 1281.60056179763*m.x16**1.29 + 2501.99920063936*m.x17**
                        1.29 + 2002.49843945008*m.x18**1.29 + 2332.38075793812*m.x19**1.29 + 1300*m.x20**1.29 + 
                        1334.16640641263*m.x21**1.29 + 1253.99362039845*m.x22**1.29 + 1555.6349186104*m.x23**1.29 + 1300
                        *m.x24**1.29 + 2080.86520466848*m.x25**1.29 + 1209.33866224478*m.x26**1.29 + 1118.03398874989*
                        m.x27**1.29 + 2002.49843945008*m.x28**1.29) + m.x40 == 0)

m.c25 = Constraint(expr= - 0.2*m.x37 - 0.17*m.x38 + m.x41 == 0)
