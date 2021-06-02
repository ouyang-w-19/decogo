#  NLP written by GAMS Convert at 04/21/18 13:51:42
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         61        1        0       60        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         17       17        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        161       33      128        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(-18.999999,18.999999),initialize=0)
m.x2 = Var(within=Reals,bounds=(-18.999999,18.999999),initialize=0)
m.x3 = Var(within=Reals,bounds=(-18.999999,18.999999),initialize=0)
m.x4 = Var(within=Reals,bounds=(-18.999999,18.999999),initialize=0)
m.x5 = Var(within=Reals,bounds=(-18.999999,18.999999),initialize=0)
m.x6 = Var(within=Reals,bounds=(-18.999999,18.999999),initialize=0)
m.x7 = Var(within=Reals,bounds=(-18.999999,18.999999),initialize=0)
m.x8 = Var(within=Reals,bounds=(-18.999999,18.999999),initialize=0)
m.x9 = Var(within=Reals,bounds=(-18.999999,18.999999),initialize=0)
m.x10 = Var(within=Reals,bounds=(-18.999999,18.999999),initialize=0)
m.x11 = Var(within=Reals,bounds=(-18.999999,18.999999),initialize=0)
m.x12 = Var(within=Reals,bounds=(-18.999999,18.999999),initialize=0)
m.x13 = Var(within=Reals,bounds=(-18.999999,18.999999),initialize=0)
m.x14 = Var(within=Reals,bounds=(-18.999999,18.999999),initialize=0)
m.x15 = Var(within=Reals,bounds=(-18.999999,18.999999),initialize=0)
m.x16 = Var(within=Reals,bounds=(-18.999999,18.999999),initialize=0)

m.obj = Objective(expr=-(10*m.x2*m.x1 - 18*m.x1**2 - 14*m.x2**2 - 18*m.x9**2 + 10*m.x10*m.x9 - 14*m.x10**2 + 4*m.x3*m.x1
                        + 6*m.x3*m.x2 - 10*m.x3**2 + 4*m.x11*m.x9 + 6*m.x11*m.x10 - 10*m.x11**2 + 8*m.x4*m.x1 - 23*m.x4
                       **2 + 8*m.x12*m.x9 - 23*m.x12**2 + 2*m.x5*m.x1 + 4*m.x5*m.x2 + 10*m.x5*m.x4 - 18*m.x5**2 + 2*
                       m.x13*m.x9 + 4*m.x13*m.x10 + 10*m.x13*m.x12 - 18*m.x13**2 + 4*m.x6*m.x2 + 4*m.x6*m.x4 + 20*m.x6*
                       m.x5 - 20*m.x6**2 + 4*m.x14*m.x10 + 4*m.x14*m.x12 + 20*m.x14*m.x13 - 20*m.x14**2 + 12*m.x8*m.x1
                        + 10*m.x8*m.x3 + 20*m.x8*m.x4 + 2*m.x8*m.x6 - 32*m.x8**2 + 12*m.x16*m.x9 + 10*m.x16*m.x11 + 20*
                       m.x16*m.x12 + 2*m.x16*m.x14 - 32*m.x16**2 + 4*m.x7*m.x2 + 4*m.x7*m.x4 + 10*m.x7*m.x6 + 20*m.x7*
                       m.x8 - 19*m.x7**2 + 4*m.x15*m.x10 + 4*m.x15*m.x12 + 10*m.x15*m.x14 + 20*m.x15*m.x16 - 19*m.x15**2
                       ), sense=minimize)

m.c1 = Constraint(expr=-sqrt((m.x1 - m.x2)**2 + (m.x9 - m.x10)**2) <= -2.995353)

m.c2 = Constraint(expr=-sqrt((m.x1 - m.x3)**2 + (m.x9 - m.x11)**2) <= -2.532248)

m.c3 = Constraint(expr=-sqrt((m.x1 - m.x4)**2 + (m.x9 - m.x12)**2) <= -2.638959)

m.c4 = Constraint(expr=-sqrt((m.x1 - m.x5)**2 + (m.x9 - m.x13)**2) <= -2.638959)

m.c5 = Constraint(expr=-sqrt((m.x1 - m.x6)**2 + (m.x9 - m.x14)**2) <= -2.121321)

m.c6 = Constraint(expr=-sqrt((m.x1 - m.x7)**2 + (m.x9 - m.x15)**2) <= -1.914214)

m.c7 = Constraint(expr=-sqrt((m.x1 - m.x8)**2 + (m.x9 - m.x16)**2) <= -2.828428)

m.c8 = Constraint(expr=-sqrt((m.x2 - m.x3)**2 + (m.x10 - m.x11)**2) <= -2.699173)

m.c9 = Constraint(expr=-sqrt((m.x2 - m.x4)**2 + (m.x10 - m.x12)**2) <= -2.805884)

m.c10 = Constraint(expr=-sqrt((m.x2 - m.x5)**2 + (m.x10 - m.x13)**2) <= -2.805884)

m.c11 = Constraint(expr=-sqrt((m.x2 - m.x6)**2 + (m.x10 - m.x14)**2) <= -2.288246)

m.c12 = Constraint(expr=-sqrt((m.x2 - m.x7)**2 + (m.x10 - m.x15)**2) <= -2.081139)

m.c13 = Constraint(expr=-sqrt((m.x2 - m.x8)**2 + (m.x10 - m.x16)**2) <= -2.995353)

m.c14 = Constraint(expr=-sqrt((m.x3 - m.x4)**2 + (m.x11 - m.x12)**2) <= -2.342779)

m.c15 = Constraint(expr=-sqrt((m.x3 - m.x5)**2 + (m.x11 - m.x13)**2) <= -2.342779)

m.c16 = Constraint(expr=-sqrt((m.x3 - m.x6)**2 + (m.x11 - m.x14)**2) <= -1.825141)

m.c17 = Constraint(expr=-sqrt((m.x3 - m.x7)**2 + (m.x11 - m.x15)**2) <= -1.618034)

m.c18 = Constraint(expr=-sqrt((m.x3 - m.x8)**2 + (m.x11 - m.x16)**2) <= -2.532248)

m.c19 = Constraint(expr=-sqrt((m.x4 - m.x5)**2 + (m.x12 - m.x13)**2) <= -2.44949)

m.c20 = Constraint(expr=-sqrt((m.x4 - m.x6)**2 + (m.x12 - m.x14)**2) <= -1.931852)

m.c21 = Constraint(expr=-sqrt((m.x4 - m.x7)**2 + (m.x12 - m.x15)**2) <= -1.724745)

m.c22 = Constraint(expr=-sqrt((m.x4 - m.x8)**2 + (m.x12 - m.x16)**2) <= -2.638959)

m.c23 = Constraint(expr=-sqrt((m.x5 - m.x6)**2 + (m.x13 - m.x14)**2) <= -1.931852)

m.c24 = Constraint(expr=-sqrt((m.x5 - m.x7)**2 + (m.x13 - m.x15)**2) <= -1.724745)

m.c25 = Constraint(expr=-sqrt((m.x5 - m.x8)**2 + (m.x13 - m.x16)**2) <= -2.638959)

m.c26 = Constraint(expr=-sqrt((m.x6 - m.x7)**2 + (m.x14 - m.x15)**2) <= -1.207107)

m.c27 = Constraint(expr=-sqrt((m.x6 - m.x8)**2 + (m.x14 - m.x16)**2) <= -2.121321)

m.c28 = Constraint(expr=-sqrt((m.x7 - m.x8)**2 + (m.x15 - m.x16)**2) <= -1.914214)

m.c29 = Constraint(expr= - m.x1 <= 1.210786)

m.c30 = Constraint(expr= - m.x2 <= 1.043861)

m.c31 = Constraint(expr= - m.x3 <= 1.506966)

m.c32 = Constraint(expr= - m.x4 <= 1.400255)

m.c33 = Constraint(expr= - m.x5 <= 1.400255)

m.c34 = Constraint(expr= - m.x6 <= 1.917893)

m.c35 = Constraint(expr= - m.x7 <= 2.125)

m.c36 = Constraint(expr= - m.x8 <= 1.210786)

m.c37 = Constraint(expr=   m.x1 <= 1.210786)

m.c38 = Constraint(expr=   m.x2 <= 1.043861)

m.c39 = Constraint(expr=   m.x3 <= 1.506966)

m.c40 = Constraint(expr=   m.x4 <= 1.400255)

m.c41 = Constraint(expr=   m.x5 <= 1.400255)

m.c42 = Constraint(expr=   m.x6 <= 1.917893)

m.c43 = Constraint(expr=   m.x7 <= 2.125)

m.c44 = Constraint(expr=   m.x8 <= 1.210786)

m.c45 = Constraint(expr= - m.x9 <= 3.710786)

m.c46 = Constraint(expr= - m.x10 <= 3.543861)

m.c47 = Constraint(expr= - m.x11 <= 4.006966)

m.c48 = Constraint(expr= - m.x12 <= 3.900255)

m.c49 = Constraint(expr= - m.x13 <= 3.900255)

m.c50 = Constraint(expr= - m.x14 <= 4.417893)

m.c51 = Constraint(expr= - m.x15 <= 4.625)

m.c52 = Constraint(expr= - m.x16 <= 3.710786)

m.c53 = Constraint(expr=   m.x9 <= 3.710786)

m.c54 = Constraint(expr=   m.x10 <= 3.543861)

m.c55 = Constraint(expr=   m.x11 <= 4.006966)

m.c56 = Constraint(expr=   m.x12 <= 3.900255)

m.c57 = Constraint(expr=   m.x13 <= 3.900255)

m.c58 = Constraint(expr=   m.x14 <= 4.417893)

m.c59 = Constraint(expr=   m.x15 <= 4.625)

m.c60 = Constraint(expr=   m.x16 <= 3.710786)
