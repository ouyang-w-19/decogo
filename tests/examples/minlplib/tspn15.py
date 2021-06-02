#  MINLP written by GAMS Convert at 04/21/18 13:55:04
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         35       16        0       19        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        136       31      105        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        503      338      165        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(67,75),initialize=67)
m.x2 = Var(within=Reals,bounds=(0,15),initialize=0)
m.x3 = Var(within=Reals,bounds=(19,35),initialize=19)
m.x4 = Var(within=Reals,bounds=(86,94),initialize=86)
m.x5 = Var(within=Reals,bounds=(7,18),initialize=7)
m.x6 = Var(within=Reals,bounds=(37,44),initialize=37)
m.x7 = Var(within=Reals,bounds=(81,90),initialize=81)
m.x8 = Var(within=Reals,bounds=(62,74),initialize=62)
m.x9 = Var(within=Reals,bounds=(70,76),initialize=70)
m.x10 = Var(within=Reals,bounds=(101,103),initialize=101)
m.x11 = Var(within=Reals,bounds=(53,63),initialize=53)
m.x12 = Var(within=Reals,bounds=(44,48),initialize=44)
m.x13 = Var(within=Reals,bounds=(42,52),initialize=42)
m.x14 = Var(within=Reals,bounds=(71,73),initialize=71)
m.x15 = Var(within=Reals,bounds=(98,105),initialize=98)
m.x16 = Var(within=Reals,bounds=(16,24),initialize=16)
m.x17 = Var(within=Reals,bounds=(45,54),initialize=45)
m.x18 = Var(within=Reals,bounds=(68,84),initialize=68)
m.x19 = Var(within=Reals,bounds=(76,86),initialize=76)
m.x20 = Var(within=Reals,bounds=(38,49),initialize=38)
m.x21 = Var(within=Reals,bounds=(10,24),initialize=10)
m.x22 = Var(within=Reals,bounds=(45,52),initialize=45)
m.x23 = Var(within=Reals,bounds=(87,95),initialize=87)
m.x24 = Var(within=Reals,bounds=(85,88),initialize=85)
m.x25 = Var(within=Reals,bounds=(6,7),initialize=6)
m.x26 = Var(within=Reals,bounds=(30,46),initialize=30)
m.x27 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x28 = Var(within=Reals,bounds=(94,105),initialize=94)
m.x29 = Var(within=Reals,bounds=(77,85),initialize=77)
m.x30 = Var(within=Reals,bounds=(29,39),initialize=29)
m.b31 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b32 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b33 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b34 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b35 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b36 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b37 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b38 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b39 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b40 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b41 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b42 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b43 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b44 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b45 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b46 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b47 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b48 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b49 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b50 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b51 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b52 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b53 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b54 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b55 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b56 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b57 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b58 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b59 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b60 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b61 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b62 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b63 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b64 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b65 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b66 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b67 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b68 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b69 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b70 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b71 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b72 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b73 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b74 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b75 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b76 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b77 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b78 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b79 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b80 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b81 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b82 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b83 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b84 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b85 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b86 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b87 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b88 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b89 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b90 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b91 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b92 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b93 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b94 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b95 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b96 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b97 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b98 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b99 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b100 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b101 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b102 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b103 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b104 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b105 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b106 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b107 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b108 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b109 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b110 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b111 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b112 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b113 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b114 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b115 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b116 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b117 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b118 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b119 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b120 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b121 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b122 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b123 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b124 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b125 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b126 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b127 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b128 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b129 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b130 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b131 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b132 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b133 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b134 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b135 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=sqrt((m.x1 - m.x3)**2 + (m.x2 - m.x4)**2)*m.b31 + sqrt((m.x1 - m.x5)**2 + (m.x2 - m.x6)**2)*m.b32
                        + sqrt((m.x1 - m.x7)**2 + (m.x2 - m.x8)**2)*m.b33 + sqrt((m.x1 - m.x9)**2 + (m.x2 - m.x10)**2)*
                       m.b34 + sqrt((m.x1 - m.x11)**2 + (m.x2 - m.x12)**2)*m.b35 + sqrt((m.x1 - m.x13)**2 + (m.x2 - 
                       m.x14)**2)*m.b36 + sqrt((m.x1 - m.x15)**2 + (m.x2 - m.x16)**2)*m.b37 + sqrt((m.x1 - m.x17)**2 + (
                       m.x2 - m.x18)**2)*m.b38 + sqrt((m.x1 - m.x19)**2 + (m.x2 - m.x20)**2)*m.b39 + sqrt((m.x1 - m.x21)
                       **2 + (m.x2 - m.x22)**2)*m.b40 + sqrt((m.x1 - m.x23)**2 + (m.x2 - m.x24)**2)*m.b41 + sqrt((m.x1
                        - m.x25)**2 + (m.x2 - m.x26)**2)*m.b42 + sqrt((m.x1 - m.x27)**2 + (m.x2 - m.x28)**2)*m.b43 + 
                       sqrt((m.x1 - m.x29)**2 + (m.x2 - m.x30)**2)*m.b44 + sqrt((m.x3 - m.x5)**2 + (m.x4 - m.x6)**2)*
                       m.b45 + sqrt((m.x3 - m.x7)**2 + (m.x4 - m.x8)**2)*m.b46 + sqrt((m.x3 - m.x9)**2 + (m.x4 - m.x10)
                       **2)*m.b47 + sqrt((m.x3 - m.x11)**2 + (m.x4 - m.x12)**2)*m.b48 + sqrt((m.x3 - m.x13)**2 + (m.x4
                        - m.x14)**2)*m.b49 + sqrt((m.x3 - m.x15)**2 + (m.x4 - m.x16)**2)*m.b50 + sqrt((m.x3 - m.x17)**2
                        + (m.x4 - m.x18)**2)*m.b51 + sqrt((m.x3 - m.x19)**2 + (m.x4 - m.x20)**2)*m.b52 + sqrt((m.x3 - 
                       m.x21)**2 + (m.x4 - m.x22)**2)*m.b53 + sqrt((m.x3 - m.x23)**2 + (m.x4 - m.x24)**2)*m.b54 + sqrt((
                       m.x3 - m.x25)**2 + (m.x4 - m.x26)**2)*m.b55 + sqrt((m.x3 - m.x27)**2 + (m.x4 - m.x28)**2)*m.b56
                        + sqrt((m.x3 - m.x29)**2 + (m.x4 - m.x30)**2)*m.b57 + sqrt((m.x5 - m.x7)**2 + (m.x6 - m.x8)**2)*
                       m.b58 + sqrt((m.x5 - m.x9)**2 + (m.x6 - m.x10)**2)*m.b59 + sqrt((m.x5 - m.x11)**2 + (m.x6 - m.x12
                       )**2)*m.b60 + sqrt((m.x5 - m.x13)**2 + (m.x6 - m.x14)**2)*m.b61 + sqrt((m.x5 - m.x15)**2 + (m.x6
                        - m.x16)**2)*m.b62 + sqrt((m.x5 - m.x17)**2 + (m.x6 - m.x18)**2)*m.b63 + sqrt((m.x5 - m.x19)**2
                        + (m.x6 - m.x20)**2)*m.b64 + sqrt((m.x5 - m.x21)**2 + (m.x6 - m.x22)**2)*m.b65 + sqrt((m.x5 - 
                       m.x23)**2 + (m.x6 - m.x24)**2)*m.b66 + sqrt((m.x5 - m.x25)**2 + (m.x6 - m.x26)**2)*m.b67 + sqrt((
                       m.x5 - m.x27)**2 + (m.x6 - m.x28)**2)*m.b68 + sqrt((m.x5 - m.x29)**2 + (m.x6 - m.x30)**2)*m.b69
                        + sqrt((m.x7 - m.x9)**2 + (m.x8 - m.x10)**2)*m.b70 + sqrt((m.x7 - m.x11)**2 + (m.x8 - m.x12)**2)
                       *m.b71 + sqrt((m.x7 - m.x13)**2 + (m.x8 - m.x14)**2)*m.b72 + sqrt((m.x7 - m.x15)**2 + (m.x8 - 
                       m.x16)**2)*m.b73 + sqrt((m.x7 - m.x17)**2 + (m.x8 - m.x18)**2)*m.b74 + sqrt((m.x7 - m.x19)**2 + (
                       m.x8 - m.x20)**2)*m.b75 + sqrt((m.x7 - m.x21)**2 + (m.x8 - m.x22)**2)*m.b76 + sqrt((m.x7 - m.x23)
                       **2 + (m.x8 - m.x24)**2)*m.b77 + sqrt((m.x7 - m.x25)**2 + (m.x8 - m.x26)**2)*m.b78 + sqrt((m.x7
                        - m.x27)**2 + (m.x8 - m.x28)**2)*m.b79 + sqrt((m.x7 - m.x29)**2 + (m.x8 - m.x30)**2)*m.b80 + 
                       sqrt((m.x9 - m.x11)**2 + (m.x10 - m.x12)**2)*m.b81 + sqrt((m.x9 - m.x13)**2 + (m.x10 - m.x14)**2)
                       *m.b82 + sqrt((m.x9 - m.x15)**2 + (m.x10 - m.x16)**2)*m.b83 + sqrt((m.x9 - m.x17)**2 + (m.x10 - 
                       m.x18)**2)*m.b84 + sqrt((m.x9 - m.x19)**2 + (m.x10 - m.x20)**2)*m.b85 + sqrt((m.x9 - m.x21)**2 + 
                       (m.x10 - m.x22)**2)*m.b86 + sqrt((m.x9 - m.x23)**2 + (m.x10 - m.x24)**2)*m.b87 + sqrt((m.x9 - 
                       m.x25)**2 + (m.x10 - m.x26)**2)*m.b88 + sqrt((m.x9 - m.x27)**2 + (m.x10 - m.x28)**2)*m.b89 + 
                       sqrt((m.x9 - m.x29)**2 + (m.x10 - m.x30)**2)*m.b90 + sqrt((m.x11 - m.x13)**2 + (m.x12 - m.x14)**2
                       )*m.b91 + sqrt((m.x11 - m.x15)**2 + (m.x12 - m.x16)**2)*m.b92 + sqrt((m.x11 - m.x17)**2 + (m.x12
                        - m.x18)**2)*m.b93 + sqrt((m.x11 - m.x19)**2 + (m.x12 - m.x20)**2)*m.b94 + sqrt((m.x11 - m.x21)
                       **2 + (m.x12 - m.x22)**2)*m.b95 + sqrt((m.x11 - m.x23)**2 + (m.x12 - m.x24)**2)*m.b96 + sqrt((
                       m.x11 - m.x25)**2 + (m.x12 - m.x26)**2)*m.b97 + sqrt((m.x11 - m.x27)**2 + (m.x12 - m.x28)**2)*
                       m.b98 + sqrt((m.x11 - m.x29)**2 + (m.x12 - m.x30)**2)*m.b99 + sqrt((m.x13 - m.x15)**2 + (m.x14 - 
                       m.x16)**2)*m.b100 + sqrt((m.x13 - m.x17)**2 + (m.x14 - m.x18)**2)*m.b101 + sqrt((m.x13 - m.x19)**
                       2 + (m.x14 - m.x20)**2)*m.b102 + sqrt((m.x13 - m.x21)**2 + (m.x14 - m.x22)**2)*m.b103 + sqrt((
                       m.x13 - m.x23)**2 + (m.x14 - m.x24)**2)*m.b104 + sqrt((m.x13 - m.x25)**2 + (m.x14 - m.x26)**2)*
                       m.b105 + sqrt((m.x13 - m.x27)**2 + (m.x14 - m.x28)**2)*m.b106 + sqrt((m.x13 - m.x29)**2 + (m.x14
                        - m.x30)**2)*m.b107 + sqrt((m.x15 - m.x17)**2 + (m.x16 - m.x18)**2)*m.b108 + sqrt((m.x15 - m.x19
                       )**2 + (m.x16 - m.x20)**2)*m.b109 + sqrt((m.x15 - m.x21)**2 + (m.x16 - m.x22)**2)*m.b110 + sqrt((
                       m.x15 - m.x23)**2 + (m.x16 - m.x24)**2)*m.b111 + sqrt((m.x15 - m.x25)**2 + (m.x16 - m.x26)**2)*
                       m.b112 + sqrt((m.x15 - m.x27)**2 + (m.x16 - m.x28)**2)*m.b113 + sqrt((m.x15 - m.x29)**2 + (m.x16
                        - m.x30)**2)*m.b114 + sqrt((m.x17 - m.x19)**2 + (m.x18 - m.x20)**2)*m.b115 + sqrt((m.x17 - m.x21
                       )**2 + (m.x18 - m.x22)**2)*m.b116 + sqrt((m.x17 - m.x23)**2 + (m.x18 - m.x24)**2)*m.b117 + sqrt((
                       m.x17 - m.x25)**2 + (m.x18 - m.x26)**2)*m.b118 + sqrt((m.x17 - m.x27)**2 + (m.x18 - m.x28)**2)*
                       m.b119 + sqrt((m.x17 - m.x29)**2 + (m.x18 - m.x30)**2)*m.b120 + sqrt((m.x19 - m.x21)**2 + (m.x20
                        - m.x22)**2)*m.b121 + sqrt((m.x19 - m.x23)**2 + (m.x20 - m.x24)**2)*m.b122 + sqrt((m.x19 - m.x25
                       )**2 + (m.x20 - m.x26)**2)*m.b123 + sqrt((m.x19 - m.x27)**2 + (m.x20 - m.x28)**2)*m.b124 + sqrt((
                       m.x19 - m.x29)**2 + (m.x20 - m.x30)**2)*m.b125 + sqrt((m.x21 - m.x23)**2 + (m.x22 - m.x24)**2)*
                       m.b126 + sqrt((m.x21 - m.x25)**2 + (m.x22 - m.x26)**2)*m.b127 + sqrt((m.x21 - m.x27)**2 + (m.x22
                        - m.x28)**2)*m.b128 + sqrt((m.x21 - m.x29)**2 + (m.x22 - m.x30)**2)*m.b129 + sqrt((m.x23 - m.x25
                       )**2 + (m.x24 - m.x26)**2)*m.b130 + sqrt((m.x23 - m.x27)**2 + (m.x24 - m.x28)**2)*m.b131 + sqrt((
                       m.x23 - m.x29)**2 + (m.x24 - m.x30)**2)*m.b132 + sqrt((m.x25 - m.x27)**2 + (m.x26 - m.x28)**2)*
                       m.b133 + sqrt((m.x25 - m.x29)**2 + (m.x26 - m.x30)**2)*m.b134 + sqrt((m.x27 - m.x29)**2 + (m.x28
                        - m.x30)**2)*m.b135, sense=minimize)

m.c2 = Constraint(expr=0.0625*m.x1**2 - 8.875*m.x1 + 0.0177777777777778*m.x2**2 - 0.266666666666667*m.x2 <= -315.0625)

m.c3 = Constraint(expr=0.015625*m.x3**2 - 0.84375*m.x3 + 0.0625*m.x4**2 - 11.25*m.x4 <= -516.640625)

m.c4 = Constraint(expr=0.0330578512396694*m.x5**2 - 0.826446280991736*m.x5 + 0.0816326530612245*m.x6**2 - 
                       6.61224489795918*m.x6 <= -138.063248439872)

m.c5 = Constraint(expr=0.0493827160493827*m.x7**2 - 8.44444444444444*m.x7 + 0.0277777777777778*m.x8**2 - 
                       3.77777777777778*m.x8 <= -488.444444444444)

m.c6 = Constraint(expr=0.111111111111111*m.x9**2 - 16.2222222222222*m.x9 + m.x10**2 - 204*m.x10 <= -10995.1111111111)

m.c7 = Constraint(expr=0.04*m.x11**2 - 4.64*m.x11 + 0.25*m.x12**2 - 23*m.x12 <= -662.56)

m.c8 = Constraint(expr=0.04*m.x13**2 - 3.76*m.x13 + m.x14**2 - 144*m.x14 <= -5271.36)

m.c9 = Constraint(expr=0.0816326530612245*m.x15**2 - 16.5714285714286*m.x15 + 0.0625*m.x16**2 - 2.5*m.x16 <= -865)

m.c10 = Constraint(expr=0.0493827160493827*m.x17**2 - 4.88888888888889*m.x17 + 0.015625*m.x18**2 - 2.375*m.x18
                         <= -210.25)

m.c11 = Constraint(expr=0.04*m.x19**2 - 6.48*m.x19 + 0.0330578512396694*m.x20**2 - 2.87603305785124*m.x20
                         <= -323.993719008264)

m.c12 = Constraint(expr=0.0204081632653061*m.x21**2 - 0.693877551020408*m.x21 + 0.0816326530612245*m.x22**2 - 
                        7.91836734693877*m.x22 <= -196.918367346939)

m.c13 = Constraint(expr=0.0625*m.x23**2 - 11.375*m.x23 + 0.444444444444444*m.x24**2 - 76.8888888888889*m.x24
                         <= -3842.00694444444)

m.c14 = Constraint(expr=4*m.x25**2 - 52*m.x25 + 0.015625*m.x26**2 - 1.1875*m.x26 <= -190.5625)

m.c15 = Constraint(expr=0.0816326530612245*m.x27**2 - 0.571428571428571*m.x27 + 0.0330578512396694*m.x28**2 - 
                        6.57851239669422*m.x28 <= -327.280991735537)

m.c16 = Constraint(expr=0.0625*m.x29**2 - 10.125*m.x29 + 0.04*m.x30**2 - 2.72*m.x30 <= -455.3025)

m.c17 = Constraint(expr=   m.b31 + m.b32 + m.b33 + m.b34 + m.b35 + m.b36 + m.b37 + m.b38 + m.b39 + m.b40 + m.b41 + m.b42
                         + m.b43 + m.b44 == 2)

m.c18 = Constraint(expr=   m.b31 + m.b45 + m.b46 + m.b47 + m.b48 + m.b49 + m.b50 + m.b51 + m.b52 + m.b53 + m.b54 + m.b55
                         + m.b56 + m.b57 == 2)

m.c19 = Constraint(expr=   m.b32 + m.b45 + m.b58 + m.b59 + m.b60 + m.b61 + m.b62 + m.b63 + m.b64 + m.b65 + m.b66 + m.b67
                         + m.b68 + m.b69 == 2)

m.c20 = Constraint(expr=   m.b33 + m.b46 + m.b58 + m.b70 + m.b71 + m.b72 + m.b73 + m.b74 + m.b75 + m.b76 + m.b77 + m.b78
                         + m.b79 + m.b80 == 2)

m.c21 = Constraint(expr=   m.b34 + m.b47 + m.b59 + m.b70 + m.b81 + m.b82 + m.b83 + m.b84 + m.b85 + m.b86 + m.b87 + m.b88
                         + m.b89 + m.b90 == 2)

m.c22 = Constraint(expr=   m.b35 + m.b48 + m.b60 + m.b71 + m.b81 + m.b91 + m.b92 + m.b93 + m.b94 + m.b95 + m.b96 + m.b97
                         + m.b98 + m.b99 == 2)

m.c23 = Constraint(expr=   m.b36 + m.b49 + m.b61 + m.b72 + m.b82 + m.b91 + m.b100 + m.b101 + m.b102 + m.b103 + m.b104
                         + m.b105 + m.b106 + m.b107 == 2)

m.c24 = Constraint(expr=   m.b37 + m.b50 + m.b62 + m.b73 + m.b83 + m.b92 + m.b100 + m.b108 + m.b109 + m.b110 + m.b111
                         + m.b112 + m.b113 + m.b114 == 2)

m.c25 = Constraint(expr=   m.b38 + m.b51 + m.b63 + m.b74 + m.b84 + m.b93 + m.b101 + m.b108 + m.b115 + m.b116 + m.b117
                         + m.b118 + m.b119 + m.b120 == 2)

m.c26 = Constraint(expr=   m.b39 + m.b52 + m.b64 + m.b75 + m.b85 + m.b94 + m.b102 + m.b109 + m.b115 + m.b121 + m.b122
                         + m.b123 + m.b124 + m.b125 == 2)

m.c27 = Constraint(expr=   m.b40 + m.b53 + m.b65 + m.b76 + m.b86 + m.b95 + m.b103 + m.b110 + m.b116 + m.b121 + m.b126
                         + m.b127 + m.b128 + m.b129 == 2)

m.c28 = Constraint(expr=   m.b41 + m.b54 + m.b66 + m.b77 + m.b87 + m.b96 + m.b104 + m.b111 + m.b117 + m.b122 + m.b126
                         + m.b130 + m.b131 + m.b132 == 2)

m.c29 = Constraint(expr=   m.b42 + m.b55 + m.b67 + m.b78 + m.b88 + m.b97 + m.b105 + m.b112 + m.b118 + m.b123 + m.b127
                         + m.b130 + m.b133 + m.b134 == 2)

m.c30 = Constraint(expr=   m.b43 + m.b56 + m.b68 + m.b79 + m.b89 + m.b98 + m.b106 + m.b113 + m.b119 + m.b124 + m.b128
                         + m.b131 + m.b133 + m.b135 == 2)

m.c31 = Constraint(expr=   m.b44 + m.b57 + m.b69 + m.b80 + m.b90 + m.b99 + m.b107 + m.b114 + m.b120 + m.b125 + m.b129
                         + m.b132 + m.b134 + m.b135 == 2)

m.c32 = Constraint(expr=   m.b35 + m.b37 + m.b39 + m.b44 + m.b92 + m.b94 + m.b99 + m.b109 + m.b114 + m.b125 <= 4)

m.c33 = Constraint(expr=   m.b37 + m.b39 + m.b44 + m.b109 + m.b114 + m.b125 <= 3)

m.c34 = Constraint(expr=   m.b31 + m.b33 + m.b34 + m.b35 + m.b36 + m.b37 + m.b38 + m.b39 + m.b41 + m.b43 + m.b44 + m.b46
                         + m.b47 + m.b48 + m.b49 + m.b50 + m.b51 + m.b52 + m.b54 + m.b56 + m.b57 + m.b70 + m.b71 + m.b72
                         + m.b73 + m.b74 + m.b75 + m.b77 + m.b79 + m.b80 + m.b81 + m.b82 + m.b83 + m.b84 + m.b85 + m.b87
                         + m.b89 + m.b90 + m.b91 + m.b92 + m.b93 + m.b94 + m.b96 + m.b98 + m.b99 + m.b100 + m.b101
                         + m.b102 + m.b104 + m.b106 + m.b107 + m.b108 + m.b109 + m.b111 + m.b113 + m.b114 + m.b115
                         + m.b117 + m.b119 + m.b120 + m.b122 + m.b124 + m.b125 + m.b131 + m.b132 + m.b135 <= 11)

m.c35 = Constraint(expr=   m.b33 + m.b34 + m.b35 + m.b36 + m.b37 + m.b38 + m.b39 + m.b41 + m.b44 + m.b70 + m.b71 + m.b72
                         + m.b73 + m.b74 + m.b75 + m.b77 + m.b80 + m.b81 + m.b82 + m.b83 + m.b84 + m.b85 + m.b87 + m.b90
                         + m.b91 + m.b92 + m.b93 + m.b94 + m.b96 + m.b99 + m.b100 + m.b101 + m.b102 + m.b104 + m.b107
                         + m.b108 + m.b109 + m.b111 + m.b114 + m.b115 + m.b117 + m.b120 + m.b122 + m.b125 + m.b132 <= 9)
