#  MINLP written by GAMS Convert at 04/21/18 13:54:56
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        278      110       64      104        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        139      119       20        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        865      380      485        0
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
m.x15 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x16 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x17 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x18 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x19 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x20 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x21 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x22 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x23 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x24 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x25 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x26 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x27 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x28 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x29 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x30 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x31 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x32 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x33 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x34 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x35 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x36 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x37 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x38 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x39 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x40 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x41 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x42 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x43 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x44 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x45 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x46 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x47 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x48 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x49 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x50 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x51 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x52 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x53 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x54 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x55 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x56 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x57 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x58 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x59 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x60 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x61 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x62 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x63 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x64 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x65 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x66 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x67 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x68 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x69 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x70 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x71 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x72 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x73 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x74 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x75 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x76 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x77 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x78 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x79 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x80 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x81 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x82 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x83 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x84 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x85 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x86 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x87 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x88 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x89 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x90 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x91 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x92 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x93 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x94 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x95 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x96 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x97 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x98 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x99 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x100 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x101 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x102 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x103 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x104 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x105 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x106 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x107 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x108 = Var(within=Reals,bounds=(None,None),initialize=0)
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
m.x129 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x130 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x131 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x132 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x133 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x134 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x135 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x136 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x137 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x138 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=430.293*m.x129**2 + 2000*m.x129 + 2500*m.x130**2 + 2000*m.x130 + 100*m.x131**2 + 4000*m.x131 + 
                       100*m.x132**2 + 4000*m.x132 + 100*m.x133**2 + 4000*m.x133, sense=minimize)

m.c2 = Constraint(expr=-(1.1350191923074*m.x2**2 - 1.1350191923074*m.x2*m.x3*cos(m.x96 - m.x97) + 4.78186315175772*m.x2*
                       m.x3*sin(m.x96 - m.x97))*m.b109 + m.x15 == 0)

m.c3 = Constraint(expr=-(1.1350191923074*m.x3**2 - 1.1350191923074*m.x3*m.x2*cos(m.x97 - m.x96) + 4.78186315175772*m.x3*
                       m.x2*sin(m.x97 - m.x96))*m.b109 + m.x16 == 0)

m.c4 = Constraint(expr=-9.09008271975275*m.x7*m.x9*sin(m.x101 - m.x103)*m.b110 + m.x17 == 0)

m.c5 = Constraint(expr=-9.09008271975275*m.x9*m.x7*sin(m.x103 - m.x101)*m.b110 + m.x18 == 0)

m.c6 = Constraint(expr=-(1.8808847537004*m.x10**2 - 1.8808847537004*m.x10*m.x11*cos(m.x104 - m.x105) + 4.40294374946052*
                       m.x10*m.x11*sin(m.x104 - m.x105))*m.b111 + m.x19 == 0)

m.c7 = Constraint(expr=-(1.8808847537004*m.x11**2 - 1.8808847537004*m.x11*m.x10*cos(m.x105 - m.x104) + 4.40294374946052*
                       m.x11*m.x10*sin(m.x105 - m.x104))*m.b111 + m.x20 == 0)

m.c8 = Constraint(expr=-4.78194338179036*m.x4*m.x7*sin(m.x98 - m.x101)*m.b112 + m.x21 == 0)

m.c9 = Constraint(expr=-4.78194338179036*m.x7*m.x4*sin(m.x101 - m.x98)*m.b112 + m.x22 == 0)

m.c10 = Constraint(expr=-3.96793905245615*m.x5*m.x6*sin(m.x99 - m.x100)*m.b113 + m.x23 == 0)

m.c11 = Constraint(expr=-3.96793905245615*m.x6*m.x5*sin(m.x100 - m.x99)*m.b113 + m.x24 == 0)

m.c12 = Constraint(expr=-(1.42400548701993*m.x9**2 - 1.42400548701993*m.x9*m.x14*cos(m.x103 - m.x108) + 3.0290504569306*
                        m.x9*m.x14*sin(m.x103 - m.x108))*m.b114 + m.x25 == 0)

m.c13 = Constraint(expr=-(1.42400548701993*m.x14**2 - 1.42400548701993*m.x14*m.x9*cos(m.x108 - m.x103) + 3.0290504569306
                        *m.x14*m.x9*sin(m.x108 - m.x103))*m.b114 + m.x26 == 0)

m.c14 = Constraint(expr=-(6.84098066149567*m.x4**2 - 6.84098066149567*m.x4*m.x5*cos(m.x98 - m.x99) + 21.5785539816916*
                        m.x4*m.x5*sin(m.x98 - m.x99))*m.b115 + m.x27 == 0)

m.c15 = Constraint(expr=-(6.84098066149567*m.x5**2 - 6.84098066149567*m.x5*m.x4*cos(m.x99 - m.x98) + 21.5785539816916*
                        m.x5*m.x4*sin(m.x99 - m.x98))*m.b115 + m.x28 == 0)

m.c16 = Constraint(expr=-(3.09892740383799*m.x6**2 - 3.09892740383799*m.x6*m.x13*cos(m.x100 - m.x107) + 6.10275544819311
                        *m.x6*m.x13*sin(m.x100 - m.x107))*m.b116 + m.x29 == 0)

m.c17 = Constraint(expr=-(3.09892740383799*m.x13**2 - 3.09892740383799*m.x13*m.x6*cos(m.x107 - m.x100) + 
                        6.10275544819311*m.x13*m.x6*sin(m.x107 - m.x100))*m.b116 + m.x30 == 0)

m.c18 = Constraint(expr=-5.67697984672154*m.x7*m.x8*sin(m.x101 - m.x102)*m.b117 + m.x31 == 0)

m.c19 = Constraint(expr=-5.67697984672154*m.x8*m.x7*sin(m.x102 - m.x101)*m.b117 + m.x32 == 0)

m.c20 = Constraint(expr=-(1.13699415780633*m.x13**2 - 1.13699415780633*m.x13*m.x14*cos(m.x107 - m.x108) + 
                        2.31496347510535*m.x13*m.x14*sin(m.x107 - m.x108))*m.b118 + m.x33 == 0)

m.c21 = Constraint(expr=-(1.13699415780633*m.x14**2 - 1.13699415780633*m.x14*m.x13*cos(m.x108 - m.x107) + 
                        2.31496347510535*m.x14*m.x13*sin(m.x108 - m.x107))*m.b118 + m.x34 == 0)

m.c22 = Constraint(expr=-(1.52596744045097*m.x6**2 - 1.52596744045097*m.x6*m.x12*cos(m.x100 - m.x106) + 3.1759639650294*
                        m.x6*m.x12*sin(m.x100 - m.x106))*m.b119 + m.x35 == 0)

m.c23 = Constraint(expr=-(1.52596744045097*m.x12**2 - 1.52596744045097*m.x12*m.x6*cos(m.x106 - m.x100) + 3.1759639650294
                        *m.x12*m.x6*sin(m.x106 - m.x100))*m.b119 + m.x36 == 0)

m.c24 = Constraint(expr=-(1.95502856317726*m.x6**2 - 1.95502856317726*m.x6*m.x11*cos(m.x100 - m.x105) + 4.09407434424044
                        *m.x6*m.x11*sin(m.x100 - m.x105))*m.b120 + m.x37 == 0)

m.c25 = Constraint(expr=-(1.95502856317726*m.x11**2 - 1.95502856317726*m.x11*m.x6*cos(m.x105 - m.x100) + 
                        4.09407434424044*m.x11*m.x6*sin(m.x105 - m.x100))*m.b120 + m.x38 == 0)

m.c26 = Constraint(expr=-(2.48902458682192*m.x12**2 - 2.48902458682192*m.x12*m.x13*cos(m.x106 - m.x107) + 
                        2.25197462617221*m.x12*m.x13*sin(m.x106 - m.x107))*m.b121 + m.x39 == 0)

m.c27 = Constraint(expr=-(2.48902458682192*m.x13**2 - 2.48902458682192*m.x13*m.x12*cos(m.x107 - m.x106) + 
                        2.25197462617221*m.x13*m.x12*sin(m.x107 - m.x106))*m.b121 + m.x40 == 0)

m.c28 = Constraint(expr=-(1.02589745497019*m.x1**2 - 1.02589745497019*m.x1*m.x5*cos(m.x95 - m.x99) + 4.23498368233483*
                        m.x1*m.x5*sin(m.x95 - m.x99))*m.b122 + m.x41 == 0)

m.c29 = Constraint(expr=-(1.02589745497019*m.x5**2 - 1.02589745497019*m.x5*m.x1*cos(m.x99 - m.x95) + 4.23498368233483*
                        m.x5*m.x1*sin(m.x99 - m.x95))*m.b122 + m.x42 == 0)

m.c30 = Constraint(expr=-(3.90204955244743*m.x9**2 - 3.90204955244743*m.x9*m.x10*cos(m.x103 - m.x104) + 10.3653941270609
                        *m.x9*m.x10*sin(m.x103 - m.x104))*m.b123 + m.x43 == 0)

m.c31 = Constraint(expr=-(3.90204955244743*m.x10**2 - 3.90204955244743*m.x10*m.x9*cos(m.x104 - m.x103) + 
                        10.3653941270609*m.x10*m.x9*sin(m.x104 - m.x103))*m.b123 + m.x44 == 0)

m.c32 = Constraint(expr=-(4.99913160079803*m.x1**2 - 4.99913160079803*m.x1*m.x2*cos(m.x95 - m.x96) + 15.2630865231796*
                        m.x1*m.x2*sin(m.x95 - m.x96))*m.b124 + m.x45 == 0)

m.c33 = Constraint(expr=-(4.99913160079803*m.x2**2 - 4.99913160079803*m.x2*m.x1*cos(m.x96 - m.x95) + 15.2630865231796*
                        m.x2*m.x1*sin(m.x96 - m.x95))*m.b124 + m.x46 == 0)

m.c34 = Constraint(expr=-(1.7011396670944*m.x2**2 - 1.7011396670944*m.x2*m.x5*cos(m.x96 - m.x99) + 5.19392739796971*m.x2
                        *m.x5*sin(m.x96 - m.x99))*m.b125 + m.x47 == 0)

m.c35 = Constraint(expr=-(1.7011396670944*m.x5**2 - 1.7011396670944*m.x5*m.x2*cos(m.x99 - m.x96) + 5.19392739796971*m.x5
                        *m.x2*sin(m.x99 - m.x96))*m.b125 + m.x48 == 0)

m.c36 = Constraint(expr=-(1.98597570992556*m.x3**2 - 1.98597570992556*m.x3*m.x4*cos(m.x97 - m.x98) + 5.06881697759392*
                        m.x3*m.x4*sin(m.x97 - m.x98))*m.b126 + m.x49 == 0)

m.c37 = Constraint(expr=-(1.98597570992556*m.x4**2 - 1.98597570992556*m.x4*m.x3*cos(m.x98 - m.x97) + 5.06881697759392*
                        m.x4*m.x3*sin(m.x98 - m.x97))*m.b126 + m.x50 == 0)

m.c38 = Constraint(expr=-1.79797907152361*m.x4*m.x9*sin(m.x98 - m.x103)*m.b127 + m.x51 == 0)

m.c39 = Constraint(expr=-1.79797907152361*m.x9*m.x4*sin(m.x103 - m.x98)*m.b127 + m.x52 == 0)

m.c40 = Constraint(expr=-(1.68603315061494*m.x2**2 - 1.68603315061494*m.x2*m.x4*cos(m.x96 - m.x98) + 5.11583832587208*
                        m.x2*m.x4*sin(m.x96 - m.x98))*m.b128 + m.x53 == 0)

m.c41 = Constraint(expr=-(1.68603315061494*m.x4**2 - 1.68603315061494*m.x4*m.x2*cos(m.x98 - m.x96) + 5.11583832587208*
                        m.x4*m.x2*sin(m.x98 - m.x96))*m.b128 + m.x54 == 0)

m.c42 = Constraint(expr=-(4.75996315175772*m.x2**2 - 4.78186315175772*m.x2*m.x3*cos(m.x96 - m.x97) - 1.1350191923074*
                        m.x2*m.x3*sin(m.x96 - m.x97))*m.b109 + m.x55 == 0)

m.c43 = Constraint(expr=-(4.75996315175772*m.x3**2 - 4.78186315175772*m.x3*m.x2*cos(m.x97 - m.x96) - 1.1350191923074*
                        m.x3*m.x2*sin(m.x97 - m.x96))*m.b109 + m.x56 == 0)

m.c44 = Constraint(expr=-(9.09008271975275*m.x7**2 - 9.09008271975275*m.x7*m.x9*cos(m.x101 - m.x103))*m.b110 + m.x57
                         == 0)

m.c45 = Constraint(expr=-(9.09008271975275*m.x9**2 - 9.09008271975275*m.x9*m.x7*cos(m.x103 - m.x101))*m.b110 + m.x58
                         == 0)

m.c46 = Constraint(expr=-(4.40294374946052*m.x10**2 - 4.40294374946052*m.x10*m.x11*cos(m.x104 - m.x105) - 
                        1.8808847537004*m.x10*m.x11*sin(m.x104 - m.x105))*m.b111 + m.x59 == 0)

m.c47 = Constraint(expr=-(4.40294374946052*m.x11**2 - 4.40294374946052*m.x11*m.x10*cos(m.x105 - m.x104) - 
                        1.8808847537004*m.x11*m.x10*sin(m.x105 - m.x104))*m.b111 + m.x60 == 0)

m.c48 = Constraint(expr=-(4.78194338179036*m.x4**2 - 4.78194338179036*m.x4*m.x7*cos(m.x98 - m.x101))*m.b112 + m.x61
                         == 0)

m.c49 = Constraint(expr=-(4.78194338179036*m.x7**2 - 4.78194338179036*m.x7*m.x4*cos(m.x101 - m.x98))*m.b112 + m.x62
                         == 0)

m.c50 = Constraint(expr=-(3.96793905245615*m.x5**2 - 3.96793905245615*m.x5*m.x6*cos(m.x99 - m.x100))*m.b113 + m.x63
                         == 0)

m.c51 = Constraint(expr=-(3.96793905245615*m.x6**2 - 3.96793905245615*m.x6*m.x5*cos(m.x100 - m.x99))*m.b113 + m.x64
                         == 0)

m.c52 = Constraint(expr=-(3.0290504569306*m.x9**2 - 3.0290504569306*m.x9*m.x14*cos(m.x103 - m.x108) - 1.42400548701993*
                        m.x9*m.x14*sin(m.x103 - m.x108))*m.b114 + m.x65 == 0)

m.c53 = Constraint(expr=-(3.0290504569306*m.x14**2 - 3.0290504569306*m.x14*m.x9*cos(m.x108 - m.x103) - 1.42400548701993*
                        m.x14*m.x9*sin(m.x108 - m.x103))*m.b114 + m.x66 == 0)

m.c54 = Constraint(expr=-(21.5785539816916*m.x4**2 - 21.5785539816916*m.x4*m.x5*cos(m.x98 - m.x99) - 6.84098066149567*
                        m.x4*m.x5*sin(m.x98 - m.x99))*m.b115 + m.x67 == 0)

m.c55 = Constraint(expr=-(21.5785539816916*m.x5**2 - 21.5785539816916*m.x5*m.x4*cos(m.x99 - m.x98) - 6.84098066149567*
                        m.x5*m.x4*sin(m.x99 - m.x98))*m.b115 + m.x68 == 0)

m.c56 = Constraint(expr=-(6.10275544819311*m.x6**2 - 6.10275544819311*m.x6*m.x13*cos(m.x100 - m.x107) - 3.09892740383799
                        *m.x6*m.x13*sin(m.x100 - m.x107))*m.b116 + m.x69 == 0)

m.c57 = Constraint(expr=-(6.10275544819311*m.x13**2 - 6.10275544819311*m.x13*m.x6*cos(m.x107 - m.x100) - 
                        3.09892740383799*m.x13*m.x6*sin(m.x107 - m.x100))*m.b116 + m.x70 == 0)

m.c58 = Constraint(expr=-(5.67697984672154*m.x7**2 - 5.67697984672154*m.x7*m.x8*cos(m.x101 - m.x102))*m.b117 + m.x71
                         == 0)

m.c59 = Constraint(expr=-(5.67697984672154*m.x8**2 - 5.67697984672154*m.x8*m.x7*cos(m.x102 - m.x101))*m.b117 + m.x72
                         == 0)

m.c60 = Constraint(expr=-(2.31496347510535*m.x13**2 - 2.31496347510535*m.x13*m.x14*cos(m.x107 - m.x108) - 
                        1.13699415780633*m.x13*m.x14*sin(m.x107 - m.x108))*m.b118 + m.x73 == 0)

m.c61 = Constraint(expr=-(2.31496347510535*m.x14**2 - 2.31496347510535*m.x14*m.x13*cos(m.x108 - m.x107) - 
                        1.13699415780633*m.x14*m.x13*sin(m.x108 - m.x107))*m.b118 + m.x74 == 0)

m.c62 = Constraint(expr=-(3.1759639650294*m.x6**2 - 3.1759639650294*m.x6*m.x12*cos(m.x100 - m.x106) - 1.52596744045097*
                        m.x6*m.x12*sin(m.x100 - m.x106))*m.b119 + m.x75 == 0)

m.c63 = Constraint(expr=-(3.1759639650294*m.x12**2 - 3.1759639650294*m.x12*m.x6*cos(m.x106 - m.x100) - 1.52596744045097*
                        m.x12*m.x6*sin(m.x106 - m.x100))*m.b119 + m.x76 == 0)

m.c64 = Constraint(expr=-(4.09407434424044*m.x6**2 - 4.09407434424044*m.x6*m.x11*cos(m.x100 - m.x105) - 1.95502856317726
                        *m.x6*m.x11*sin(m.x100 - m.x105))*m.b120 + m.x77 == 0)

m.c65 = Constraint(expr=-(4.09407434424044*m.x11**2 - 4.09407434424044*m.x11*m.x6*cos(m.x105 - m.x100) - 
                        1.95502856317726*m.x11*m.x6*sin(m.x105 - m.x100))*m.b120 + m.x78 == 0)

m.c66 = Constraint(expr=-(2.25197462617221*m.x12**2 - 2.25197462617221*m.x12*m.x13*cos(m.x106 - m.x107) - 
                        2.48902458682192*m.x12*m.x13*sin(m.x106 - m.x107))*m.b121 + m.x79 == 0)

m.c67 = Constraint(expr=-(2.25197462617221*m.x13**2 - 2.25197462617221*m.x13*m.x12*cos(m.x107 - m.x106) - 
                        2.48902458682192*m.x13*m.x12*sin(m.x107 - m.x106))*m.b121 + m.x80 == 0)

m.c68 = Constraint(expr=-(4.21038368233483*m.x1**2 - 4.23498368233483*m.x1*m.x5*cos(m.x95 - m.x99) - 1.02589745497019*
                        m.x1*m.x5*sin(m.x95 - m.x99))*m.b122 + m.x81 == 0)

m.c69 = Constraint(expr=-(4.21038368233483*m.x5**2 - 4.23498368233483*m.x5*m.x1*cos(m.x99 - m.x95) - 1.02589745497019*
                        m.x5*m.x1*sin(m.x99 - m.x95))*m.b122 + m.x82 == 0)

m.c70 = Constraint(expr=-(10.3653941270609*m.x9**2 - 10.3653941270609*m.x9*m.x10*cos(m.x103 - m.x104) - 3.90204955244743
                        *m.x9*m.x10*sin(m.x103 - m.x104))*m.b123 + m.x83 == 0)

m.c71 = Constraint(expr=-(10.3653941270609*m.x10**2 - 10.3653941270609*m.x10*m.x9*cos(m.x104 - m.x103) - 
                        3.90204955244743*m.x10*m.x9*sin(m.x104 - m.x103))*m.b123 + m.x84 == 0)

m.c72 = Constraint(expr=-(15.2366865231796*m.x1**2 - 15.2630865231796*m.x1*m.x2*cos(m.x95 - m.x96) - 4.99913160079803*
                        m.x1*m.x2*sin(m.x95 - m.x96))*m.b124 + m.x85 == 0)

m.c73 = Constraint(expr=-(15.2366865231796*m.x2**2 - 15.2630865231796*m.x2*m.x1*cos(m.x96 - m.x95) - 4.99913160079803*
                        m.x2*m.x1*sin(m.x96 - m.x95))*m.b124 + m.x86 == 0)

m.c74 = Constraint(expr=-(5.17662739796971*m.x2**2 - 5.19392739796971*m.x2*m.x5*cos(m.x96 - m.x99) - 1.7011396670944*
                        m.x2*m.x5*sin(m.x96 - m.x99))*m.b125 + m.x87 == 0)

m.c75 = Constraint(expr=-(5.17662739796971*m.x5**2 - 5.19392739796971*m.x5*m.x2*cos(m.x99 - m.x96) - 1.7011396670944*
                        m.x5*m.x2*sin(m.x99 - m.x96))*m.b125 + m.x88 == 0)

m.c76 = Constraint(expr=-(5.06241697759392*m.x3**2 - 5.06881697759392*m.x3*m.x4*cos(m.x97 - m.x98) - 1.98597570992556*
                        m.x3*m.x4*sin(m.x97 - m.x98))*m.b126 + m.x89 == 0)

m.c77 = Constraint(expr=-(5.06241697759392*m.x4**2 - 5.06881697759392*m.x4*m.x3*cos(m.x98 - m.x97) - 1.98597570992556*
                        m.x4*m.x3*sin(m.x98 - m.x97))*m.b126 + m.x90 == 0)

m.c78 = Constraint(expr=-(1.79797907152361*m.x4**2 - 1.79797907152361*m.x4*m.x9*cos(m.x98 - m.x103))*m.b127 + m.x91
                         == 0)

m.c79 = Constraint(expr=-(1.79797907152361*m.x9**2 - 1.79797907152361*m.x9*m.x4*cos(m.x103 - m.x98))*m.b127 + m.x92
                         == 0)

m.c80 = Constraint(expr=-(5.09883832587208*m.x2**2 - 5.11583832587208*m.x2*m.x4*cos(m.x96 - m.x98) - 1.68603315061494*
                        m.x2*m.x4*sin(m.x96 - m.x98))*m.b128 + m.x93 == 0)

m.c81 = Constraint(expr=-(5.09883832587208*m.x4**2 - 5.11583832587208*m.x4*m.x2*cos(m.x98 - m.x96) - 1.68603315061494*
                        m.x4*m.x2*sin(m.x98 - m.x96))*m.b128 + m.x94 == 0)

m.c82 = Constraint(expr=m.x15**2 + m.x55**2 <= 9801)

m.c83 = Constraint(expr=m.x16**2 + m.x56**2 <= 9801)

m.c84 = Constraint(expr=m.x17**2 + m.x57**2 <= 9801)

m.c85 = Constraint(expr=m.x18**2 + m.x58**2 <= 9801)

m.c86 = Constraint(expr=m.x19**2 + m.x59**2 <= 9801)

m.c87 = Constraint(expr=m.x20**2 + m.x60**2 <= 9801)

m.c88 = Constraint(expr=m.x21**2 + m.x61**2 <= 9801)

m.c89 = Constraint(expr=m.x22**2 + m.x62**2 <= 9801)

m.c90 = Constraint(expr=m.x23**2 + m.x63**2 <= 9801)

m.c91 = Constraint(expr=m.x24**2 + m.x64**2 <= 9801)

m.c92 = Constraint(expr=m.x25**2 + m.x65**2 <= 9801)

m.c93 = Constraint(expr=m.x26**2 + m.x66**2 <= 9801)

m.c94 = Constraint(expr=m.x27**2 + m.x67**2 <= 9801)

m.c95 = Constraint(expr=m.x28**2 + m.x68**2 <= 9801)

m.c96 = Constraint(expr=m.x29**2 + m.x69**2 <= 9801)

m.c97 = Constraint(expr=m.x30**2 + m.x70**2 <= 9801)

m.c98 = Constraint(expr=m.x31**2 + m.x71**2 <= 9801)

m.c99 = Constraint(expr=m.x32**2 + m.x72**2 <= 9801)

m.c100 = Constraint(expr=m.x33**2 + m.x73**2 <= 9801)

m.c101 = Constraint(expr=m.x34**2 + m.x74**2 <= 9801)

m.c102 = Constraint(expr=m.x35**2 + m.x75**2 <= 9801)

m.c103 = Constraint(expr=m.x36**2 + m.x76**2 <= 9801)

m.c104 = Constraint(expr=m.x37**2 + m.x77**2 <= 9801)

m.c105 = Constraint(expr=m.x38**2 + m.x78**2 <= 9801)

m.c106 = Constraint(expr=m.x39**2 + m.x79**2 <= 9801)

m.c107 = Constraint(expr=m.x40**2 + m.x80**2 <= 9801)

m.c108 = Constraint(expr=m.x41**2 + m.x81**2 <= 9801)

m.c109 = Constraint(expr=m.x42**2 + m.x82**2 <= 9801)

m.c110 = Constraint(expr=m.x43**2 + m.x83**2 <= 9801)

m.c111 = Constraint(expr=m.x44**2 + m.x84**2 <= 9801)

m.c112 = Constraint(expr=m.x45**2 + m.x85**2 <= 9801)

m.c113 = Constraint(expr=m.x46**2 + m.x86**2 <= 9801)

m.c114 = Constraint(expr=m.x47**2 + m.x87**2 <= 9801)

m.c115 = Constraint(expr=m.x48**2 + m.x88**2 <= 9801)

m.c116 = Constraint(expr=m.x49**2 + m.x89**2 <= 9801)

m.c117 = Constraint(expr=m.x50**2 + m.x90**2 <= 9801)

m.c118 = Constraint(expr=m.x51**2 + m.x91**2 <= 9801)

m.c119 = Constraint(expr=m.x52**2 + m.x92**2 <= 9801)

m.c120 = Constraint(expr=m.x53**2 + m.x93**2 <= 9801)

m.c121 = Constraint(expr=m.x54**2 + m.x94**2 <= 9801)

m.c122 = Constraint(expr=   m.x129 <= 3.324)

m.c123 = Constraint(expr=   m.x130 <= 1.4)

m.c124 = Constraint(expr=   m.x131 <= 1)

m.c125 = Constraint(expr=   m.x132 <= 1)

m.c126 = Constraint(expr=   m.x133 <= 1)

m.c127 = Constraint(expr=   m.x129 >= 0)

m.c128 = Constraint(expr=   m.x130 >= 0)

m.c129 = Constraint(expr=   m.x131 >= 0)

m.c130 = Constraint(expr=   m.x132 >= 0)

m.c131 = Constraint(expr=   m.x133 >= 0)

m.c132 = Constraint(expr=   m.x134 <= 0.1)

m.c133 = Constraint(expr=   m.x135 <= 0.5)

m.c134 = Constraint(expr=   m.x136 <= 0.4)

m.c135 = Constraint(expr=   m.x137 <= 0.24)

m.c136 = Constraint(expr=   m.x138 <= 0.24)

m.c137 = Constraint(expr=   m.x134 >= 0)

m.c138 = Constraint(expr=   m.x135 >= -0.4)

m.c139 = Constraint(expr=   m.x136 >= 0)

m.c140 = Constraint(expr=   m.x137 >= -0.06)

m.c141 = Constraint(expr=   m.x138 >= -0.06)

m.c142 = Constraint(expr=   m.x1 <= 1.06)

m.c143 = Constraint(expr=   m.x2 <= 1.06)

m.c144 = Constraint(expr=   m.x3 <= 1.06)

m.c145 = Constraint(expr=   m.x4 <= 1.06)

m.c146 = Constraint(expr=   m.x5 <= 1.06)

m.c147 = Constraint(expr=   m.x6 <= 1.06)

m.c148 = Constraint(expr=   m.x7 <= 1.06)

m.c149 = Constraint(expr=   m.x8 <= 1.06)

m.c150 = Constraint(expr=   m.x9 <= 1.06)

m.c151 = Constraint(expr=   m.x10 <= 1.06)

m.c152 = Constraint(expr=   m.x11 <= 1.06)

m.c153 = Constraint(expr=   m.x12 <= 1.06)

m.c154 = Constraint(expr=   m.x13 <= 1.06)

m.c155 = Constraint(expr=   m.x14 <= 1.06)

m.c156 = Constraint(expr=   m.x1 >= 0.94)

m.c157 = Constraint(expr=   m.x2 >= 0.94)

m.c158 = Constraint(expr=   m.x3 >= 0.94)

m.c159 = Constraint(expr=   m.x4 >= 0.94)

m.c160 = Constraint(expr=   m.x5 >= 0.94)

m.c161 = Constraint(expr=   m.x6 >= 0.94)

m.c162 = Constraint(expr=   m.x7 >= 0.94)

m.c163 = Constraint(expr=   m.x8 >= 0.94)

m.c164 = Constraint(expr=   m.x9 >= 0.94)

m.c165 = Constraint(expr=   m.x10 >= 0.94)

m.c166 = Constraint(expr=   m.x11 >= 0.94)

m.c167 = Constraint(expr=   m.x12 >= 0.94)

m.c168 = Constraint(expr=   m.x13 >= 0.94)

m.c169 = Constraint(expr=   m.x14 >= 0.94)

m.c170 = Constraint(expr=   m.x96 - m.x97 >= -0.26)

m.c171 = Constraint(expr= - m.x96 + m.x97 >= -0.26)

m.c172 = Constraint(expr=   m.x101 - m.x103 >= -0.26)

m.c173 = Constraint(expr= - m.x101 + m.x103 >= -0.26)

m.c174 = Constraint(expr=   m.x104 - m.x105 >= -0.26)

m.c175 = Constraint(expr= - m.x104 + m.x105 >= -0.26)

m.c176 = Constraint(expr=   m.x98 - m.x101 >= -0.26)

m.c177 = Constraint(expr= - m.x98 + m.x101 >= -0.26)

m.c178 = Constraint(expr=   m.x99 - m.x100 >= -0.26)

m.c179 = Constraint(expr= - m.x99 + m.x100 >= -0.26)

m.c180 = Constraint(expr=   m.x103 - m.x108 >= -0.26)

m.c181 = Constraint(expr= - m.x103 + m.x108 >= -0.26)

m.c182 = Constraint(expr=   m.x98 - m.x99 >= -0.26)

m.c183 = Constraint(expr= - m.x98 + m.x99 >= -0.26)

m.c184 = Constraint(expr=   m.x100 - m.x107 >= -0.26)

m.c185 = Constraint(expr= - m.x100 + m.x107 >= -0.26)

m.c186 = Constraint(expr=   m.x101 - m.x102 >= -0.26)

m.c187 = Constraint(expr= - m.x101 + m.x102 >= -0.26)

m.c188 = Constraint(expr=   m.x107 - m.x108 >= -0.26)

m.c189 = Constraint(expr= - m.x107 + m.x108 >= -0.26)

m.c190 = Constraint(expr=   m.x100 - m.x106 >= -0.26)

m.c191 = Constraint(expr= - m.x100 + m.x106 >= -0.26)

m.c192 = Constraint(expr=   m.x100 - m.x105 >= -0.26)

m.c193 = Constraint(expr= - m.x100 + m.x105 >= -0.26)

m.c194 = Constraint(expr=   m.x106 - m.x107 >= -0.26)

m.c195 = Constraint(expr= - m.x106 + m.x107 >= -0.26)

m.c196 = Constraint(expr=   m.x95 - m.x99 >= -0.26)

m.c197 = Constraint(expr= - m.x95 + m.x99 >= -0.26)

m.c198 = Constraint(expr=   m.x103 - m.x104 >= -0.26)

m.c199 = Constraint(expr= - m.x103 + m.x104 >= -0.26)

m.c200 = Constraint(expr=   m.x95 - m.x96 >= -0.26)

m.c201 = Constraint(expr= - m.x95 + m.x96 >= -0.26)

m.c202 = Constraint(expr=   m.x96 - m.x99 >= -0.26)

m.c203 = Constraint(expr= - m.x96 + m.x99 >= -0.26)

m.c204 = Constraint(expr=   m.x97 - m.x98 >= -0.26)

m.c205 = Constraint(expr= - m.x97 + m.x98 >= -0.26)

m.c206 = Constraint(expr=   m.x98 - m.x103 >= -0.26)

m.c207 = Constraint(expr= - m.x98 + m.x103 >= -0.26)

m.c208 = Constraint(expr=   m.x96 - m.x98 >= -0.26)

m.c209 = Constraint(expr= - m.x96 + m.x98 >= -0.26)

m.c210 = Constraint(expr=   m.x96 - m.x97 <= 0.26)

m.c211 = Constraint(expr= - m.x96 + m.x97 <= 0.26)

m.c212 = Constraint(expr=   m.x101 - m.x103 <= 0.26)

m.c213 = Constraint(expr= - m.x101 + m.x103 <= 0.26)

m.c214 = Constraint(expr=   m.x104 - m.x105 <= 0.26)

m.c215 = Constraint(expr= - m.x104 + m.x105 <= 0.26)

m.c216 = Constraint(expr=   m.x98 - m.x101 <= 0.26)

m.c217 = Constraint(expr= - m.x98 + m.x101 <= 0.26)

m.c218 = Constraint(expr=   m.x99 - m.x100 <= 0.26)

m.c219 = Constraint(expr= - m.x99 + m.x100 <= 0.26)

m.c220 = Constraint(expr=   m.x103 - m.x108 <= 0.26)

m.c221 = Constraint(expr= - m.x103 + m.x108 <= 0.26)

m.c222 = Constraint(expr=   m.x98 - m.x99 <= 0.26)

m.c223 = Constraint(expr= - m.x98 + m.x99 <= 0.26)

m.c224 = Constraint(expr=   m.x100 - m.x107 <= 0.26)

m.c225 = Constraint(expr= - m.x100 + m.x107 <= 0.26)

m.c226 = Constraint(expr=   m.x101 - m.x102 <= 0.26)

m.c227 = Constraint(expr= - m.x101 + m.x102 <= 0.26)

m.c228 = Constraint(expr=   m.x107 - m.x108 <= 0.26)

m.c229 = Constraint(expr= - m.x107 + m.x108 <= 0.26)

m.c230 = Constraint(expr=   m.x100 - m.x106 <= 0.26)

m.c231 = Constraint(expr= - m.x100 + m.x106 <= 0.26)

m.c232 = Constraint(expr=   m.x100 - m.x105 <= 0.26)

m.c233 = Constraint(expr= - m.x100 + m.x105 <= 0.26)

m.c234 = Constraint(expr=   m.x106 - m.x107 <= 0.26)

m.c235 = Constraint(expr= - m.x106 + m.x107 <= 0.26)

m.c236 = Constraint(expr=   m.x95 - m.x99 <= 0.26)

m.c237 = Constraint(expr= - m.x95 + m.x99 <= 0.26)

m.c238 = Constraint(expr=   m.x103 - m.x104 <= 0.26)

m.c239 = Constraint(expr= - m.x103 + m.x104 <= 0.26)

m.c240 = Constraint(expr=   m.x95 - m.x96 <= 0.26)

m.c241 = Constraint(expr= - m.x95 + m.x96 <= 0.26)

m.c242 = Constraint(expr=   m.x96 - m.x99 <= 0.26)

m.c243 = Constraint(expr= - m.x96 + m.x99 <= 0.26)

m.c244 = Constraint(expr=   m.x97 - m.x98 <= 0.26)

m.c245 = Constraint(expr= - m.x97 + m.x98 <= 0.26)

m.c246 = Constraint(expr=   m.x98 - m.x103 <= 0.26)

m.c247 = Constraint(expr= - m.x98 + m.x103 <= 0.26)

m.c248 = Constraint(expr=   m.x96 - m.x98 <= 0.26)

m.c249 = Constraint(expr= - m.x96 + m.x98 <= 0.26)

m.c250 = Constraint(expr=   m.x95 == 0)

m.c251 = Constraint(expr=   m.x41 + m.x45 - m.x129 == 0)

m.c252 = Constraint(expr=   m.x15 + m.x46 + m.x47 + m.x53 - m.x130 == -0.217)

m.c253 = Constraint(expr=   m.x16 + m.x49 - m.x131 == -0.942)

m.c254 = Constraint(expr=   m.x24 + m.x29 + m.x35 + m.x37 - m.x132 == -0.112)

m.c255 = Constraint(expr=   m.x32 - m.x133 == 0)

m.c256 = Constraint(expr=   m.x81 + m.x85 - m.x134 == 0)

m.c257 = Constraint(expr=   m.x55 + m.x86 + m.x87 + m.x93 - m.x135 == -0.127)

m.c258 = Constraint(expr=   m.x56 + m.x89 - m.x136 == -0.19)

m.c259 = Constraint(expr=   m.x64 + m.x69 + m.x75 + m.x77 - m.x137 == -0.075)

m.c260 = Constraint(expr=   m.x72 - m.x138 == 0)

m.c261 = Constraint(expr=   m.x21 + m.x27 + m.x50 + m.x51 + m.x54 == -0.478)

m.c262 = Constraint(expr=   m.x23 + m.x28 + m.x42 + m.x48 == -0.076)

m.c263 = Constraint(expr=   m.x17 + m.x22 + m.x31 == 0)

m.c264 = Constraint(expr=   m.x18 + m.x25 + m.x43 + m.x52 == -0.295)

m.c265 = Constraint(expr=   m.x19 + m.x44 == -0.09)

m.c266 = Constraint(expr=   m.x20 + m.x38 == -0.035)

m.c267 = Constraint(expr=   m.x36 + m.x39 == -0.061)

m.c268 = Constraint(expr=   m.x30 + m.x33 + m.x40 == -0.135)

m.c269 = Constraint(expr=   m.x26 + m.x34 == -0.149)

m.c270 = Constraint(expr=   m.x61 + m.x67 + m.x90 + m.x91 + m.x94 == 0.039)

m.c271 = Constraint(expr=   m.x63 + m.x68 + m.x82 + m.x88 == -0.016)

m.c272 = Constraint(expr=   m.x57 + m.x62 + m.x71 == 0)

m.c273 = Constraint(expr=   m.x58 + m.x65 + m.x83 + m.x92 == -0.166)

m.c274 = Constraint(expr=   m.x59 + m.x84 == -0.058)

m.c275 = Constraint(expr=   m.x60 + m.x78 == -0.018)

m.c276 = Constraint(expr=   m.x76 + m.x79 == -0.016)

m.c277 = Constraint(expr=   m.x70 + m.x73 + m.x80 == -0.058)

m.c278 = Constraint(expr=   m.x66 + m.x74 == -0.05)
