#  NLP written by GAMS Convert at 04/21/18 13:51:48
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          1        1        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         31       31        0        0        0        0        0        0
#  FX      6        6        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         31        1       30        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x2 = Var(within=Reals,bounds=(-5,5),initialize=3.43266708)
m.x3 = Var(within=Reals,bounds=(-5,5),initialize=0.50375356)
m.x4 = Var(within=Reals,bounds=(-5,5),initialize=-1.98862096)
m.x5 = Var(within=Reals,bounds=(-5,5),initialize=-2.07787883)
m.x6 = Var(within=Reals,bounds=(-5,5),initialize=-2.75947133)
m.x7 = Var(within=Reals,bounds=(-5,5),initialize=-1.50169496)
m.x8 = Var(within=Reals,bounds=(-5,5),initialize=3.56270347)
m.x9 = Var(within=Reals,bounds=(-5,5),initialize=-4.32886277)
m.x10 = Var(within=Reals,bounds=(-5,5),initialize=0.00210668999999974)
m.x11 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x13 = Var(within=Reals,bounds=(-5,5),initialize=4.91133039)
m.x14 = Var(within=Reals,bounds=(-5,5),initialize=2.62250467)
m.x15 = Var(within=Reals,bounds=(-5,5),initialize=-3.69307517)
m.x16 = Var(within=Reals,bounds=(-5,5),initialize=1.39718759)
m.x17 = Var(within=Reals,bounds=(-5,5),initialize=-3.40482136)
m.x18 = Var(within=Reals,bounds=(-5,5),initialize=-2.49919467)
m.x19 = Var(within=Reals,bounds=(-5,5),initialize=1.68928609)
m.x20 = Var(within=Reals,bounds=(-5,5),initialize=-0.64643619)
m.x21 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x24 = Var(within=Reals,bounds=(-5,5),initialize=-3.49898212)
m.x25 = Var(within=Reals,bounds=(-5,5),initialize=0.8911365)
m.x26 = Var(within=Reals,bounds=(-5,5),initialize=3.30892812)
m.x27 = Var(within=Reals,bounds=(-5,5),initialize=-2.69184262)
m.x28 = Var(within=Reals,bounds=(-5,5),initialize=1.6573446)
m.x29 = Var(within=Reals,bounds=(-5,5),initialize=2.75857606)
m.x30 = Var(within=Reals,bounds=(-5,5),initialize=-1.96341523)

m.obj = Objective(expr=(1 - exp(3 - 3*((m.x1 - m.x2)**2 + (m.x11 - m.x12)**2 + (m.x21 - m.x22)**2)**0.5))**2 + (1 - exp(
                       3 - 3*((m.x1 - m.x3)**2 + (m.x11 - m.x13)**2 + (m.x21 - m.x23)**2)**0.5))**2 + (1 - exp(3 - 3*((
                       m.x1 - m.x4)**2 + (m.x11 - m.x14)**2 + (m.x21 - m.x24)**2)**0.5))**2 + (1 - exp(3 - 3*((m.x1 - 
                       m.x5)**2 + (m.x11 - m.x15)**2 + (m.x21 - m.x25)**2)**0.5))**2 + (1 - exp(3 - 3*((m.x1 - m.x6)**2
                        + (m.x11 - m.x16)**2 + (m.x21 - m.x26)**2)**0.5))**2 + (1 - exp(3 - 3*((m.x1 - m.x7)**2 + (m.x11
                        - m.x17)**2 + (m.x21 - m.x27)**2)**0.5))**2 + (1 - exp(3 - 3*((m.x1 - m.x8)**2 + (m.x11 - m.x18)
                       **2 + (m.x21 - m.x28)**2)**0.5))**2 + (1 - exp(3 - 3*((m.x1 - m.x9)**2 + (m.x11 - m.x19)**2 + (
                       m.x21 - m.x29)**2)**0.5))**2 + (1 - exp(3 - 3*((m.x1 - m.x10)**2 + (m.x11 - m.x20)**2 + (m.x21 - 
                       m.x30)**2)**0.5))**2 + (1 - exp(3 - 3*((m.x2 - m.x3)**2 + (m.x12 - m.x13)**2 + (m.x22 - m.x23)**2
                       )**0.5))**2 + (1 - exp(3 - 3*((m.x2 - m.x4)**2 + (m.x12 - m.x14)**2 + (m.x22 - m.x24)**2)**0.5))
                       **2 + (1 - exp(3 - 3*((m.x2 - m.x5)**2 + (m.x12 - m.x15)**2 + (m.x22 - m.x25)**2)**0.5))**2 + (1
                        - exp(3 - 3*((m.x2 - m.x6)**2 + (m.x12 - m.x16)**2 + (m.x22 - m.x26)**2)**0.5))**2 + (1 - exp(3
                        - 3*((m.x2 - m.x7)**2 + (m.x12 - m.x17)**2 + (m.x22 - m.x27)**2)**0.5))**2 + (1 - exp(3 - 3*((
                       m.x2 - m.x8)**2 + (m.x12 - m.x18)**2 + (m.x22 - m.x28)**2)**0.5))**2 + (1 - exp(3 - 3*((m.x2 - 
                       m.x9)**2 + (m.x12 - m.x19)**2 + (m.x22 - m.x29)**2)**0.5))**2 + (1 - exp(3 - 3*((m.x2 - m.x10)**2
                        + (m.x12 - m.x20)**2 + (m.x22 - m.x30)**2)**0.5))**2 + (1 - exp(3 - 3*((m.x3 - m.x4)**2 + (m.x13
                        - m.x14)**2 + (m.x23 - m.x24)**2)**0.5))**2 + (1 - exp(3 - 3*((m.x3 - m.x5)**2 + (m.x13 - m.x15)
                       **2 + (m.x23 - m.x25)**2)**0.5))**2 + (1 - exp(3 - 3*((m.x3 - m.x6)**2 + (m.x13 - m.x16)**2 + (
                       m.x23 - m.x26)**2)**0.5))**2 + (1 - exp(3 - 3*((m.x3 - m.x7)**2 + (m.x13 - m.x17)**2 + (m.x23 - 
                       m.x27)**2)**0.5))**2 + (1 - exp(3 - 3*((m.x3 - m.x8)**2 + (m.x13 - m.x18)**2 + (m.x23 - m.x28)**2
                       )**0.5))**2 + (1 - exp(3 - 3*((m.x3 - m.x9)**2 + (m.x13 - m.x19)**2 + (m.x23 - m.x29)**2)**0.5))
                       **2 + (1 - exp(3 - 3*((m.x3 - m.x10)**2 + (m.x13 - m.x20)**2 + (m.x23 - m.x30)**2)**0.5))**2 + (1
                        - exp(3 - 3*((m.x4 - m.x5)**2 + (m.x14 - m.x15)**2 + (m.x24 - m.x25)**2)**0.5))**2 + (1 - exp(3
                        - 3*((m.x4 - m.x6)**2 + (m.x14 - m.x16)**2 + (m.x24 - m.x26)**2)**0.5))**2 + (1 - exp(3 - 3*((
                       m.x4 - m.x7)**2 + (m.x14 - m.x17)**2 + (m.x24 - m.x27)**2)**0.5))**2 + (1 - exp(3 - 3*((m.x4 - 
                       m.x8)**2 + (m.x14 - m.x18)**2 + (m.x24 - m.x28)**2)**0.5))**2 + (1 - exp(3 - 3*((m.x4 - m.x9)**2
                        + (m.x14 - m.x19)**2 + (m.x24 - m.x29)**2)**0.5))**2 + (1 - exp(3 - 3*((m.x4 - m.x10)**2 + (
                       m.x14 - m.x20)**2 + (m.x24 - m.x30)**2)**0.5))**2 + (1 - exp(3 - 3*((m.x5 - m.x6)**2 + (m.x15 - 
                       m.x16)**2 + (m.x25 - m.x26)**2)**0.5))**2 + (1 - exp(3 - 3*((m.x5 - m.x7)**2 + (m.x15 - m.x17)**2
                        + (m.x25 - m.x27)**2)**0.5))**2 + (1 - exp(3 - 3*((m.x5 - m.x8)**2 + (m.x15 - m.x18)**2 + (m.x25
                        - m.x28)**2)**0.5))**2 + (1 - exp(3 - 3*((m.x5 - m.x9)**2 + (m.x15 - m.x19)**2 + (m.x25 - m.x29)
                       **2)**0.5))**2 + (1 - exp(3 - 3*((m.x5 - m.x10)**2 + (m.x15 - m.x20)**2 + (m.x25 - m.x30)**2)**
                       0.5))**2 + (1 - exp(3 - 3*((m.x6 - m.x7)**2 + (m.x16 - m.x17)**2 + (m.x26 - m.x27)**2)**0.5))**2
                        + (1 - exp(3 - 3*((m.x6 - m.x8)**2 + (m.x16 - m.x18)**2 + (m.x26 - m.x28)**2)**0.5))**2 + (1 - 
                       exp(3 - 3*((m.x6 - m.x9)**2 + (m.x16 - m.x19)**2 + (m.x26 - m.x29)**2)**0.5))**2 + (1 - exp(3 - 3
                       *((m.x6 - m.x10)**2 + (m.x16 - m.x20)**2 + (m.x26 - m.x30)**2)**0.5))**2 + (1 - exp(3 - 3*((m.x7
                        - m.x8)**2 + (m.x17 - m.x18)**2 + (m.x27 - m.x28)**2)**0.5))**2 + (1 - exp(3 - 3*((m.x7 - m.x9)
                       **2 + (m.x17 - m.x19)**2 + (m.x27 - m.x29)**2)**0.5))**2 + (1 - exp(3 - 3*((m.x7 - m.x10)**2 + (
                       m.x17 - m.x20)**2 + (m.x27 - m.x30)**2)**0.5))**2 + (1 - exp(3 - 3*((m.x8 - m.x9)**2 + (m.x18 - 
                       m.x19)**2 + (m.x28 - m.x29)**2)**0.5))**2 + (1 - exp(3 - 3*((m.x8 - m.x10)**2 + (m.x18 - m.x20)**
                       2 + (m.x28 - m.x30)**2)**0.5))**2 + (1 - exp(3 - 3*((m.x9 - m.x10)**2 + (m.x19 - m.x20)**2 + (
                       m.x29 - m.x30)**2)**0.5))**2 - 45, sense=minimize)
