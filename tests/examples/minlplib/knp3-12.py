#  NLP written by GAMS Convert at 04/21/18 13:52:28
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         78       12       66        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         37       37        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        498       66      432        0


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(-2,2),initialize=-1.313011472)
m.x2 = Var(within=Reals,bounds=(-2,2),initialize=1.373066832)
m.x3 = Var(within=Reals,bounds=(-2,2),initialize=0.201501424)
m.x4 = Var(within=Reals,bounds=(-2,2),initialize=-0.795448384)
m.x5 = Var(within=Reals,bounds=(-2,2),initialize=-0.831151532)
m.x6 = Var(within=Reals,bounds=(-2,2),initialize=-1.103788532)
m.x7 = Var(within=Reals,bounds=(-2,2),initialize=-0.600677984)
m.x8 = Var(within=Reals,bounds=(-2,2),initialize=1.425081388)
m.x9 = Var(within=Reals,bounds=(-2,2),initialize=-1.731545108)
m.x10 = Var(within=Reals,bounds=(-2,2),initialize=0.000842675999999987)
m.x11 = Var(within=Reals,bounds=(-2,2),initialize=1.992470508)
m.x12 = Var(within=Reals,bounds=(-2,2),initialize=0.314933512)
m.x13 = Var(within=Reals,bounds=(-2,2),initialize=1.964532156)
m.x14 = Var(within=Reals,bounds=(-2,2),initialize=1.049001868)
m.x15 = Var(within=Reals,bounds=(-2,2),initialize=-1.477230068)
m.x16 = Var(within=Reals,bounds=(-2,2),initialize=0.558875036)
m.x17 = Var(within=Reals,bounds=(-2,2),initialize=-1.361928544)
m.x18 = Var(within=Reals,bounds=(-2,2),initialize=-0.999677868)
m.x19 = Var(within=Reals,bounds=(-2,2),initialize=0.675714436)
m.x20 = Var(within=Reals,bounds=(-2,2),initialize=-0.258574476)
m.x21 = Var(within=Reals,bounds=(-2,2),initialize=-0.561198936)
m.x22 = Var(within=Reals,bounds=(-2,2),initialize=-0.594234528)
m.x23 = Var(within=Reals,bounds=(-2,2),initialize=-1.47403364)
m.x24 = Var(within=Reals,bounds=(-2,2),initialize=-1.399592848)
m.x25 = Var(within=Reals,bounds=(-2,2),initialize=0.3564546)
m.x26 = Var(within=Reals,bounds=(-2,2),initialize=1.323571248)
m.x27 = Var(within=Reals,bounds=(-2,2),initialize=-1.076737048)
m.x28 = Var(within=Reals,bounds=(-2,2),initialize=0.66293784)
m.x29 = Var(within=Reals,bounds=(-2,2),initialize=1.103430424)
m.x30 = Var(within=Reals,bounds=(-2,2),initialize=-0.785366092)
m.x31 = Var(within=Reals,bounds=(-2,2),initialize=-1.558030836)
m.x32 = Var(within=Reals,bounds=(-2,2),initialize=0.00953946399999994)
m.x33 = Var(within=Reals,bounds=(-2,2),initialize=-1.359308952)
m.x34 = Var(within=Reals,bounds=(-2,2),initialize=1.489849244)
m.x35 = Var(within=Reals,bounds=(-2,2),initialize=-0.93954182)
m.x36 = Var(within=Reals,bounds=(-2,2),initialize=-0.856742712)
m.x37 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=m.x37, sense=maximize)

m.c1 = Constraint(expr=m.x1**2 + m.x2**2 + m.x3**2 == 4)

m.c2 = Constraint(expr=m.x4**2 + m.x5**2 + m.x6**2 == 4)

m.c3 = Constraint(expr=m.x7**2 + m.x8**2 + m.x9**2 == 4)

m.c4 = Constraint(expr=m.x10**2 + m.x11**2 + m.x12**2 == 4)

m.c5 = Constraint(expr=m.x13**2 + m.x14**2 + m.x15**2 == 4)

m.c6 = Constraint(expr=m.x16**2 + m.x17**2 + m.x18**2 == 4)

m.c7 = Constraint(expr=m.x19**2 + m.x20**2 + m.x21**2 == 4)

m.c8 = Constraint(expr=m.x22**2 + m.x23**2 + m.x24**2 == 4)

m.c9 = Constraint(expr=m.x25**2 + m.x26**2 + m.x27**2 == 4)

m.c10 = Constraint(expr=m.x28**2 + m.x29**2 + m.x30**2 == 4)

m.c11 = Constraint(expr=m.x31**2 + m.x32**2 + m.x33**2 == 4)

m.c12 = Constraint(expr=m.x34**2 + m.x35**2 + m.x36**2 == 4)

m.c13 = Constraint(expr=(m.x1 - m.x4)**2 + (m.x2 - m.x5)**2 + (m.x3 - m.x6)**2 - 4*m.x37 >= 0)

m.c14 = Constraint(expr=(m.x1 - m.x7)**2 + (m.x2 - m.x8)**2 + (m.x3 - m.x9)**2 - 4*m.x37 >= 0)

m.c15 = Constraint(expr=(m.x1 - m.x10)**2 + (m.x2 - m.x11)**2 + (m.x3 - m.x12)**2 - 4*m.x37 >= 0)

m.c16 = Constraint(expr=(m.x1 - m.x13)**2 + (m.x2 - m.x14)**2 + (m.x3 - m.x15)**2 - 4*m.x37 >= 0)

m.c17 = Constraint(expr=(m.x1 - m.x16)**2 + (m.x2 - m.x17)**2 + (m.x3 - m.x18)**2 - 4*m.x37 >= 0)

m.c18 = Constraint(expr=(m.x1 - m.x19)**2 + (m.x2 - m.x20)**2 + (m.x3 - m.x21)**2 - 4*m.x37 >= 0)

m.c19 = Constraint(expr=(m.x1 - m.x22)**2 + (m.x2 - m.x23)**2 + (m.x3 - m.x24)**2 - 4*m.x37 >= 0)

m.c20 = Constraint(expr=(m.x1 - m.x25)**2 + (m.x2 - m.x26)**2 + (m.x3 - m.x27)**2 - 4*m.x37 >= 0)

m.c21 = Constraint(expr=(m.x1 - m.x28)**2 + (m.x2 - m.x29)**2 + (m.x3 - m.x30)**2 - 4*m.x37 >= 0)

m.c22 = Constraint(expr=(m.x1 - m.x31)**2 + (m.x2 - m.x32)**2 + (m.x3 - m.x33)**2 - 4*m.x37 >= 0)

m.c23 = Constraint(expr=(m.x1 - m.x34)**2 + (m.x2 - m.x35)**2 + (m.x3 - m.x36)**2 - 4*m.x37 >= 0)

m.c24 = Constraint(expr=(m.x4 - m.x7)**2 + (m.x5 - m.x8)**2 + (m.x6 - m.x9)**2 - 4*m.x37 >= 0)

m.c25 = Constraint(expr=(m.x4 - m.x10)**2 + (m.x5 - m.x11)**2 + (m.x6 - m.x12)**2 - 4*m.x37 >= 0)

m.c26 = Constraint(expr=(m.x4 - m.x13)**2 + (m.x5 - m.x14)**2 + (m.x6 - m.x15)**2 - 4*m.x37 >= 0)

m.c27 = Constraint(expr=(m.x4 - m.x16)**2 + (m.x5 - m.x17)**2 + (m.x6 - m.x18)**2 - 4*m.x37 >= 0)

m.c28 = Constraint(expr=(m.x4 - m.x19)**2 + (m.x5 - m.x20)**2 + (m.x6 - m.x21)**2 - 4*m.x37 >= 0)

m.c29 = Constraint(expr=(m.x4 - m.x22)**2 + (m.x5 - m.x23)**2 + (m.x6 - m.x24)**2 - 4*m.x37 >= 0)

m.c30 = Constraint(expr=(m.x4 - m.x25)**2 + (m.x5 - m.x26)**2 + (m.x6 - m.x27)**2 - 4*m.x37 >= 0)

m.c31 = Constraint(expr=(m.x4 - m.x28)**2 + (m.x5 - m.x29)**2 + (m.x6 - m.x30)**2 - 4*m.x37 >= 0)

m.c32 = Constraint(expr=(m.x4 - m.x31)**2 + (m.x5 - m.x32)**2 + (m.x6 - m.x33)**2 - 4*m.x37 >= 0)

m.c33 = Constraint(expr=(m.x4 - m.x34)**2 + (m.x5 - m.x35)**2 + (m.x6 - m.x36)**2 - 4*m.x37 >= 0)

m.c34 = Constraint(expr=(m.x7 - m.x10)**2 + (m.x8 - m.x11)**2 + (m.x9 - m.x12)**2 - 4*m.x37 >= 0)

m.c35 = Constraint(expr=(m.x7 - m.x13)**2 + (m.x8 - m.x14)**2 + (m.x9 - m.x15)**2 - 4*m.x37 >= 0)

m.c36 = Constraint(expr=(m.x7 - m.x16)**2 + (m.x8 - m.x17)**2 + (m.x9 - m.x18)**2 - 4*m.x37 >= 0)

m.c37 = Constraint(expr=(m.x7 - m.x19)**2 + (m.x8 - m.x20)**2 + (m.x9 - m.x21)**2 - 4*m.x37 >= 0)

m.c38 = Constraint(expr=(m.x7 - m.x22)**2 + (m.x8 - m.x23)**2 + (m.x9 - m.x24)**2 - 4*m.x37 >= 0)

m.c39 = Constraint(expr=(m.x7 - m.x25)**2 + (m.x8 - m.x26)**2 + (m.x9 - m.x27)**2 - 4*m.x37 >= 0)

m.c40 = Constraint(expr=(m.x7 - m.x28)**2 + (m.x8 - m.x29)**2 + (m.x9 - m.x30)**2 - 4*m.x37 >= 0)

m.c41 = Constraint(expr=(m.x7 - m.x31)**2 + (m.x8 - m.x32)**2 + (m.x9 - m.x33)**2 - 4*m.x37 >= 0)

m.c42 = Constraint(expr=(m.x7 - m.x34)**2 + (m.x8 - m.x35)**2 + (m.x9 - m.x36)**2 - 4*m.x37 >= 0)

m.c43 = Constraint(expr=(m.x10 - m.x13)**2 + (m.x11 - m.x14)**2 + (m.x12 - m.x15)**2 - 4*m.x37 >= 0)

m.c44 = Constraint(expr=(m.x10 - m.x16)**2 + (m.x11 - m.x17)**2 + (m.x12 - m.x18)**2 - 4*m.x37 >= 0)

m.c45 = Constraint(expr=(m.x10 - m.x19)**2 + (m.x11 - m.x20)**2 + (m.x12 - m.x21)**2 - 4*m.x37 >= 0)

m.c46 = Constraint(expr=(m.x10 - m.x22)**2 + (m.x11 - m.x23)**2 + (m.x12 - m.x24)**2 - 4*m.x37 >= 0)

m.c47 = Constraint(expr=(m.x10 - m.x25)**2 + (m.x11 - m.x26)**2 + (m.x12 - m.x27)**2 - 4*m.x37 >= 0)

m.c48 = Constraint(expr=(m.x10 - m.x28)**2 + (m.x11 - m.x29)**2 + (m.x12 - m.x30)**2 - 4*m.x37 >= 0)

m.c49 = Constraint(expr=(m.x10 - m.x31)**2 + (m.x11 - m.x32)**2 + (m.x12 - m.x33)**2 - 4*m.x37 >= 0)

m.c50 = Constraint(expr=(m.x10 - m.x34)**2 + (m.x11 - m.x35)**2 + (m.x12 - m.x36)**2 - 4*m.x37 >= 0)

m.c51 = Constraint(expr=(m.x13 - m.x16)**2 + (m.x14 - m.x17)**2 + (m.x15 - m.x18)**2 - 4*m.x37 >= 0)

m.c52 = Constraint(expr=(m.x13 - m.x19)**2 + (m.x14 - m.x20)**2 + (m.x15 - m.x21)**2 - 4*m.x37 >= 0)

m.c53 = Constraint(expr=(m.x13 - m.x22)**2 + (m.x14 - m.x23)**2 + (m.x15 - m.x24)**2 - 4*m.x37 >= 0)

m.c54 = Constraint(expr=(m.x13 - m.x25)**2 + (m.x14 - m.x26)**2 + (m.x15 - m.x27)**2 - 4*m.x37 >= 0)

m.c55 = Constraint(expr=(m.x13 - m.x28)**2 + (m.x14 - m.x29)**2 + (m.x15 - m.x30)**2 - 4*m.x37 >= 0)

m.c56 = Constraint(expr=(m.x13 - m.x31)**2 + (m.x14 - m.x32)**2 + (m.x15 - m.x33)**2 - 4*m.x37 >= 0)

m.c57 = Constraint(expr=(m.x13 - m.x34)**2 + (m.x14 - m.x35)**2 + (m.x15 - m.x36)**2 - 4*m.x37 >= 0)

m.c58 = Constraint(expr=(m.x16 - m.x19)**2 + (m.x17 - m.x20)**2 + (m.x18 - m.x21)**2 - 4*m.x37 >= 0)

m.c59 = Constraint(expr=(m.x16 - m.x22)**2 + (m.x17 - m.x23)**2 + (m.x18 - m.x24)**2 - 4*m.x37 >= 0)

m.c60 = Constraint(expr=(m.x16 - m.x25)**2 + (m.x17 - m.x26)**2 + (m.x18 - m.x27)**2 - 4*m.x37 >= 0)

m.c61 = Constraint(expr=(m.x16 - m.x28)**2 + (m.x17 - m.x29)**2 + (m.x18 - m.x30)**2 - 4*m.x37 >= 0)

m.c62 = Constraint(expr=(m.x16 - m.x31)**2 + (m.x17 - m.x32)**2 + (m.x18 - m.x33)**2 - 4*m.x37 >= 0)

m.c63 = Constraint(expr=(m.x16 - m.x34)**2 + (m.x17 - m.x35)**2 + (m.x18 - m.x36)**2 - 4*m.x37 >= 0)

m.c64 = Constraint(expr=(m.x19 - m.x22)**2 + (m.x20 - m.x23)**2 + (m.x21 - m.x24)**2 - 4*m.x37 >= 0)

m.c65 = Constraint(expr=(m.x19 - m.x25)**2 + (m.x20 - m.x26)**2 + (m.x21 - m.x27)**2 - 4*m.x37 >= 0)

m.c66 = Constraint(expr=(m.x19 - m.x28)**2 + (m.x20 - m.x29)**2 + (m.x21 - m.x30)**2 - 4*m.x37 >= 0)

m.c67 = Constraint(expr=(m.x19 - m.x31)**2 + (m.x20 - m.x32)**2 + (m.x21 - m.x33)**2 - 4*m.x37 >= 0)

m.c68 = Constraint(expr=(m.x19 - m.x34)**2 + (m.x20 - m.x35)**2 + (m.x21 - m.x36)**2 - 4*m.x37 >= 0)

m.c69 = Constraint(expr=(m.x22 - m.x25)**2 + (m.x23 - m.x26)**2 + (m.x24 - m.x27)**2 - 4*m.x37 >= 0)

m.c70 = Constraint(expr=(m.x22 - m.x28)**2 + (m.x23 - m.x29)**2 + (m.x24 - m.x30)**2 - 4*m.x37 >= 0)

m.c71 = Constraint(expr=(m.x22 - m.x31)**2 + (m.x23 - m.x32)**2 + (m.x24 - m.x33)**2 - 4*m.x37 >= 0)

m.c72 = Constraint(expr=(m.x22 - m.x34)**2 + (m.x23 - m.x35)**2 + (m.x24 - m.x36)**2 - 4*m.x37 >= 0)

m.c73 = Constraint(expr=(m.x25 - m.x28)**2 + (m.x26 - m.x29)**2 + (m.x27 - m.x30)**2 - 4*m.x37 >= 0)

m.c74 = Constraint(expr=(m.x25 - m.x31)**2 + (m.x26 - m.x32)**2 + (m.x27 - m.x33)**2 - 4*m.x37 >= 0)

m.c75 = Constraint(expr=(m.x25 - m.x34)**2 + (m.x26 - m.x35)**2 + (m.x27 - m.x36)**2 - 4*m.x37 >= 0)

m.c76 = Constraint(expr=(m.x28 - m.x31)**2 + (m.x29 - m.x32)**2 + (m.x30 - m.x33)**2 - 4*m.x37 >= 0)

m.c77 = Constraint(expr=(m.x28 - m.x34)**2 + (m.x29 - m.x35)**2 + (m.x30 - m.x36)**2 - 4*m.x37 >= 0)

m.c78 = Constraint(expr=(m.x31 - m.x34)**2 + (m.x32 - m.x35)**2 + (m.x33 - m.x36)**2 - 4*m.x37 >= 0)
