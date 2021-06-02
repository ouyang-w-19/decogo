#  NLP written by GAMS Convert at 04/21/18 13:52:28
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         79       79        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         91       91        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        301      211       90        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0.0001,None),initialize=1)
m.x2 = Var(within=Reals,bounds=(0.0001,None),initialize=1)
m.x3 = Var(within=Reals,bounds=(0.0001,None),initialize=1)
m.x4 = Var(within=Reals,bounds=(0.0001,None),initialize=1)
m.x5 = Var(within=Reals,bounds=(0.0001,None),initialize=1)
m.x6 = Var(within=Reals,bounds=(0.0001,None),initialize=1)
m.x7 = Var(within=Reals,bounds=(0.0001,None),initialize=1)
m.x8 = Var(within=Reals,bounds=(0.0001,None),initialize=1)
m.x9 = Var(within=Reals,bounds=(0.0001,None),initialize=1)
m.x10 = Var(within=Reals,bounds=(0.0001,None),initialize=1)
m.x11 = Var(within=Reals,bounds=(0.0001,None),initialize=1)
m.x12 = Var(within=Reals,bounds=(0.0001,None),initialize=1)
m.x13 = Var(within=Reals,bounds=(0.0001,None),initialize=1)
m.x14 = Var(within=Reals,bounds=(0.0001,None),initialize=1)
m.x15 = Var(within=Reals,bounds=(0.0001,None),initialize=1)
m.x16 = Var(within=Reals,bounds=(0.0001,None),initialize=1)
m.x17 = Var(within=Reals,bounds=(0.0001,None),initialize=1)
m.x18 = Var(within=Reals,bounds=(0.0001,None),initialize=1)
m.x19 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x20 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x21 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x22 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x23 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x24 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x25 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x26 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x27 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x28 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x29 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x30 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x31 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x32 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x33 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x34 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x35 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x36 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x37 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x38 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x39 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x40 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x41 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x42 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x43 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x44 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x45 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x46 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x47 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x48 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x49 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x50 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x51 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x52 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x53 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x54 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x55 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x56 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x57 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x58 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x59 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x60 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x61 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x62 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x63 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x64 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x65 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x66 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x67 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x68 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x69 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x70 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x71 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x72 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x73 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x74 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x75 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x76 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x77 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x78 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x79 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x80 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x81 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x82 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x83 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x84 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x85 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x86 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x87 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x88 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x89 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x90 = Var(within=Reals,bounds=(None,None),initialize=1)

m.obj = Objective(expr=-0.001*((464.504 - m.x20)*m.x20 + (405522.144 - m.x19)*m.x19 + (405407.292 - m.x31)*m.x31 + (
                       349.33 - m.x22)*m.x22 + (555583.632 - m.x21)*m.x21 + (555699.024 - m.x33)*m.x33 + (361.078 - 
                       m.x24)*m.x24 + (5273.992 - m.x23)*m.x23 + (5276.2 - m.x35)*m.x35 + (423.116 - m.x26)*m.x26 + (
                       119974.047 - m.x25)*m.x25 + (119997.18 - m.x37)*m.x37 + (464.504 - m.x28)*m.x28 + (38980.8 - 
                       m.x27)*m.x27 + (39110.4 - m.x39)*m.x39 + (167.578 - m.x32)*m.x32 + (405441.072 - m.x43)*m.x43 + (
                       346.51 - m.x34)*m.x34 + (555910.576 - m.x45)*m.x45 + (359.834 - m.x36)*m.x36 + (5279.788 - m.x47)
                       *m.x47 + (421.17 - m.x38)*m.x38 + (120093.918 - m.x49)*m.x49 + (430.508 - m.x40)*m.x40 + (39195.2
                        - m.x51)*m.x51 + (165.832 - m.x44)*m.x44 + (405616.728 - m.x55)*m.x55 + (347.442 - m.x46)*m.x46
                        + (556208.672 - m.x57)*m.x57 + (365.352 - m.x48)*m.x48 + (5281.812 - m.x59)*m.x59 + (415.676 - 
                       m.x50)*m.x50 + (120148.596 - m.x61)*m.x61 + (407.71 - m.x52)*m.x52 + (39305.6 - m.x63)*m.x63 + (
                       160.268 - m.x56)*m.x56 + (405832.92 - m.x67)*m.x67 + (357.308 - m.x58)*m.x58 + (556449.072 - 
                       m.x69)*m.x69 + (371.834 - m.x60)*m.x60 + (5282.916 - m.x71)*m.x71 + (412.832 - m.x62)*m.x62 + (
                       120182.244 - m.x73)*m.x73 + (372.616 - m.x64)*m.x64 + (39417.6 - m.x75)*m.x75 + (130.69 - m.x68)*
                       m.x68 + (405907.236 - m.x79)*m.x79 + (376.02 - m.x70)*m.x70 + (556554.848 - m.x81)*m.x81 + (
                       385.136 - m.x72)*m.x72 + (5282.916 - m.x83)*m.x83 + (408.6 - m.x74)*m.x74 + (120165.42 - m.x85)*
                       m.x85 + (402.2 - m.x76)*m.x76 + (39412.8 - m.x87)*m.x87 + (144.01 - m.x80)*m.x80 + (387.666 - 
                       m.x82)*m.x82 + (393.302 - m.x84)*m.x84 + (408.5 - m.x86)*m.x86 + (482.158 - m.x88)*m.x88)
                        + 734595853.838046, sense=minimize)

m.c1 = Constraint(expr= - m.x19 + m.x20 + m.x31 == -22)

m.c2 = Constraint(expr= - m.x20 - m.x21 + m.x22 + m.x33 == -1)

m.c3 = Constraint(expr= - m.x22 - m.x23 + m.x24 + m.x35 == 3)

m.c4 = Constraint(expr= - m.x24 - m.x25 + m.x26 + m.x37 == -27.2)

m.c5 = Constraint(expr= - m.x26 - m.x27 + m.x28 + m.x39 == 51.5)

m.c6 = Constraint(expr= - m.x31 + m.x32 + m.x43 == 44)

m.c7 = Constraint(expr= - m.x32 - m.x33 + m.x34 + m.x45 == 162)

m.c8 = Constraint(expr= - m.x34 - m.x35 + m.x36 + m.x47 == 8)

m.c9 = Constraint(expr= - m.x36 - m.x37 + m.x38 + m.x49 == 12.5)

m.c10 = Constraint(expr= - m.x38 - m.x39 + m.x40 + m.x51 == 53.5)

m.c11 = Constraint(expr= - m.x43 + m.x44 + m.x55 == -11)

m.c12 = Constraint(expr= - m.x44 - m.x45 + m.x46 + m.x57 == 60)

m.c13 = Constraint(expr= - m.x46 - m.x47 + m.x48 + m.x59 == 10)

m.c14 = Constraint(expr= - m.x48 - m.x49 + m.x50 + m.x61 == 18)

m.c15 = Constraint(expr= - m.x50 - m.x51 + m.x52 + m.x63 == 39)

m.c16 = Constraint(expr= - m.x55 + m.x56 + m.x67 == 124)

m.c17 = Constraint(expr= - m.x56 - m.x57 + m.x58 + m.x69 == 246)

m.c18 = Constraint(expr= - m.x58 - m.x59 + m.x60 + m.x71 == 6)

m.c19 = Constraint(expr= - m.x60 - m.x61 + m.x62 + m.x73 == 9.7)

m.c20 = Constraint(expr= - m.x62 - m.x63 + m.x64 + m.x75 == 17.2)

m.c21 = Constraint(expr= - m.x67 + m.x68 + m.x79 == 127)

m.c22 = Constraint(expr= - m.x68 - m.x69 + m.x70 + m.x81 == 175)

m.c23 = Constraint(expr= - m.x70 - m.x71 + m.x72 + m.x83 == 3)

m.c24 = Constraint(expr= - m.x72 - m.x73 + m.x74 + m.x85 == 10)

m.c25 = Constraint(expr= - m.x74 - m.x75 + m.x76 + m.x87 == 30.2)

m.c26 = Constraint(expr=   m.x19 - m.x79 + m.x80 == 78)

m.c27 = Constraint(expr=   m.x21 - m.x80 - m.x81 + m.x82 == 156)

m.c28 = Constraint(expr=   m.x23 - m.x82 - m.x83 + m.x84 == 3)

m.c29 = Constraint(expr=   m.x25 - m.x84 - m.x85 + m.x86 == 14)

m.c30 = Constraint(expr=   m.x27 - m.x86 - m.x87 + m.x88 == 23.2)

m.c31 = Constraint(expr=0.0841168*m.x29**2*sqrt(m.x1) - m.x22 == 0)

m.c32 = Constraint(expr=0.1280849*m.x30**2*sqrt(m.x2) - m.x24 == 0)

m.c33 = Constraint(expr=0.2605*m.x3**2.2 - m.x26 == 0)

m.c34 = Constraint(expr=   0.00103993344426*m.x21 + 0.1086956521739*m.x23 - m.x29 == 543.4)

m.c35 = Constraint(expr= - m.x1 + 0.002079866888519*m.x21 - 0.2173913043478*m.x23 == 0)

m.c36 = Constraint(expr=   0.2173913043478*m.x23 - m.x30 == 543.4)

m.c37 = Constraint(expr= - m.x2 + 0.2173913043478*m.x23 - 0.009510223490252*m.x25 == 0)

m.c38 = Constraint(expr= - m.x3 + 0.009510223490252*m.x25 == 550.11)

m.c39 = Constraint(expr=0.0841168*m.x41**2*sqrt(m.x4) - m.x34 == 0)

m.c40 = Constraint(expr=0.1280849*m.x42**2*sqrt(m.x5) - m.x36 == 0)

m.c41 = Constraint(expr=0.2605*m.x6**2.2 - m.x38 == 0)

m.c42 = Constraint(expr=   0.00103993344426*m.x33 + 0.1086956521739*m.x35 - m.x41 == 543.4)

m.c43 = Constraint(expr= - m.x4 + 0.002079866888519*m.x33 - 0.2173913043478*m.x35 == 0)

m.c44 = Constraint(expr=   0.2173913043478*m.x35 - m.x42 == 543.4)

m.c45 = Constraint(expr= - m.x5 + 0.2173913043478*m.x35 - 0.009510223490252*m.x37 == 0)

m.c46 = Constraint(expr= - m.x6 + 0.009510223490252*m.x37 == 550.11)

m.c47 = Constraint(expr=0.0841168*m.x53**2*sqrt(m.x7) - m.x46 == 0)

m.c48 = Constraint(expr=0.1280849*m.x54**2*sqrt(m.x8) - m.x48 == 0)

m.c49 = Constraint(expr=0.2605*m.x9**2.2 - m.x50 == 0)

m.c50 = Constraint(expr=   0.00103993344426*m.x45 + 0.1086956521739*m.x47 - m.x53 == 543.4)

m.c51 = Constraint(expr= - m.x7 + 0.002079866888519*m.x45 - 0.2173913043478*m.x47 == 0)

m.c52 = Constraint(expr=   0.2173913043478*m.x47 - m.x54 == 543.4)

m.c53 = Constraint(expr= - m.x8 + 0.2173913043478*m.x47 - 0.009510223490252*m.x49 == 0)

m.c54 = Constraint(expr= - m.x9 + 0.009510223490252*m.x49 == 550.11)

m.c55 = Constraint(expr=0.0841168*m.x65**2*sqrt(m.x10) - m.x58 == 0)

m.c56 = Constraint(expr=0.1280849*m.x66**2*sqrt(m.x11) - m.x60 == 0)

m.c57 = Constraint(expr=0.2605*m.x12**2.2 - m.x62 == 0)

m.c58 = Constraint(expr=   0.00103993344426*m.x57 + 0.1086956521739*m.x59 - m.x65 == 543.4)

m.c59 = Constraint(expr= - m.x10 + 0.002079866888519*m.x57 - 0.2173913043478*m.x59 == 0)

m.c60 = Constraint(expr=   0.2173913043478*m.x59 - m.x66 == 543.4)

m.c61 = Constraint(expr= - m.x11 + 0.2173913043478*m.x59 - 0.009510223490252*m.x61 == 0)

m.c62 = Constraint(expr= - m.x12 + 0.009510223490252*m.x61 == 550.11)

m.c63 = Constraint(expr=0.0841168*m.x77**2*sqrt(m.x13) - m.x70 == 0)

m.c64 = Constraint(expr=0.1280849*m.x78**2*sqrt(m.x14) - m.x72 == 0)

m.c65 = Constraint(expr=0.2605*m.x15**2.2 - m.x74 == 0)

m.c66 = Constraint(expr=   0.00103993344426*m.x69 + 0.1086956521739*m.x71 - m.x77 == 543.4)

m.c67 = Constraint(expr= - m.x13 + 0.002079866888519*m.x69 - 0.2173913043478*m.x71 == 0)

m.c68 = Constraint(expr=   0.2173913043478*m.x71 - m.x78 == 543.4)

m.c69 = Constraint(expr= - m.x14 + 0.2173913043478*m.x71 - 0.009510223490252*m.x73 == 0)

m.c70 = Constraint(expr= - m.x15 + 0.009510223490252*m.x73 == 550.11)

m.c71 = Constraint(expr=0.0841168*m.x89**2*sqrt(m.x16) - m.x82 == 0)

m.c72 = Constraint(expr=0.1280849*m.x90**2*sqrt(m.x17) - m.x84 == 0)

m.c73 = Constraint(expr=0.2605*m.x18**2.2 - m.x86 == 0)

m.c74 = Constraint(expr=   0.00103993344426*m.x81 + 0.1086956521739*m.x83 - m.x89 == 543.4)

m.c75 = Constraint(expr= - m.x16 + 0.002079866888519*m.x81 - 0.2173913043478*m.x83 == 0)

m.c76 = Constraint(expr=   0.2173913043478*m.x83 - m.x90 == 543.4)

m.c77 = Constraint(expr= - m.x17 + 0.2173913043478*m.x83 - 0.009510223490252*m.x85 == 0)

m.c78 = Constraint(expr= - m.x18 + 0.009510223490252*m.x85 == 550.11)
