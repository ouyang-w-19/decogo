#  NLP written by GAMS Convert at 04/21/18 13:53:50
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        198      110       24       64        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        119      119        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        653      192      461        0
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
m.x109 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x110 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x111 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x112 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x113 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x114 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x115 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x116 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x117 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x118 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=430.293*m.x109**2 + 2000*m.x109 + 2500*m.x110**2 + 2000*m.x110 + 100*m.x111**2 + 4000*m.x111 + 
                       100*m.x112**2 + 4000*m.x112 + 100*m.x113**2 + 4000*m.x113, sense=minimize)

m.c2 = Constraint(expr=0.567509596153698*m.x82*m.x83 - 1.1350191923074*m.x82**2 - 2.39093157587886*m.x82*m.x97 + 
                       0.567509596153698*m.x83*m.x82 + 2.39093157587886*m.x83*m.x96 + 2.39093157587886*m.x96*m.x83 - 
                       1.1350191923074*m.x96**2 + 0.567509596153698*m.x96*m.x97 - 2.39093157587886*m.x97*m.x82 + 
                       0.567509596153698*m.x97*m.x96 + m.x1 == 0)

m.c3 = Constraint(expr=0.567509596153698*m.x82*m.x83 + 2.39093157587886*m.x82*m.x97 + 0.567509596153698*m.x83*m.x82 - 
                       1.1350191923074*m.x83**2 - 2.39093157587886*m.x83*m.x96 - 2.39093157587886*m.x96*m.x83 + 
                       0.567509596153698*m.x96*m.x97 + 2.39093157587886*m.x97*m.x82 + 0.567509596153698*m.x97*m.x96 - 
                       1.1350191923074*m.x97**2 + m.x2 == 0)

m.c4 = Constraint(expr=4.54504135987637*m.x89*m.x101 - 4.54504135987637*m.x87*m.x103 + 4.54504135987637*m.x101*m.x89 - 
                       4.54504135987637*m.x103*m.x87 + m.x3 == 0)

m.c5 = Constraint(expr=4.54504135987637*m.x87*m.x103 - 4.54504135987637*m.x89*m.x101 - 4.54504135987637*m.x101*m.x89 + 
                       4.54504135987637*m.x103*m.x87 + m.x4 == 0)

m.c6 = Constraint(expr=0.9404423768502*m.x90*m.x91 - 1.8808847537004*m.x90**2 - 2.20147187473026*m.x90*m.x105 + 
                       0.9404423768502*m.x91*m.x90 + 2.20147187473026*m.x91*m.x104 + 2.20147187473026*m.x104*m.x91 - 
                       1.8808847537004*m.x104**2 + 0.9404423768502*m.x104*m.x105 - 2.20147187473026*m.x105*m.x90 + 
                       0.9404423768502*m.x105*m.x104 + m.x5 == 0)

m.c7 = Constraint(expr=0.9404423768502*m.x90*m.x91 + 2.20147187473026*m.x90*m.x105 + 0.9404423768502*m.x91*m.x90 - 
                       1.8808847537004*m.x91**2 - 2.20147187473026*m.x91*m.x104 - 2.20147187473026*m.x104*m.x91 + 
                       0.9404423768502*m.x104*m.x105 + 2.20147187473026*m.x105*m.x90 + 0.9404423768502*m.x105*m.x104 - 
                       1.8808847537004*m.x105**2 + m.x6 == 0)

m.c8 = Constraint(expr=2.39097169089518*m.x87*m.x98 - 2.39097169089518*m.x84*m.x101 + 2.39097169089518*m.x98*m.x87 - 
                       2.39097169089518*m.x101*m.x84 + m.x7 == 0)

m.c9 = Constraint(expr=2.39097169089518*m.x84*m.x101 - 2.39097169089518*m.x87*m.x98 - 2.39097169089518*m.x98*m.x87 + 
                       2.39097169089518*m.x101*m.x84 + m.x8 == 0)

m.c10 = Constraint(expr=1.98396952622808*m.x86*m.x99 - 1.98396952622808*m.x85*m.x100 + 1.98396952622808*m.x99*m.x86 - 
                        1.98396952622808*m.x100*m.x85 + m.x9 == 0)

m.c11 = Constraint(expr=1.98396952622808*m.x85*m.x100 - 1.98396952622808*m.x86*m.x99 - 1.98396952622808*m.x99*m.x86 + 
                        1.98396952622808*m.x100*m.x85 + m.x10 == 0)

m.c12 = Constraint(expr=0.712002743509966*m.x89*m.x94 - 1.42400548701993*m.x89**2 - 1.5145252284653*m.x89*m.x108 + 
                        0.712002743509966*m.x94*m.x89 + 1.5145252284653*m.x94*m.x103 + 1.5145252284653*m.x103*m.x94 - 
                        1.42400548701993*m.x103**2 + 0.712002743509966*m.x103*m.x108 - 1.5145252284653*m.x108*m.x89 + 
                        0.712002743509966*m.x108*m.x103 + m.x11 == 0)

m.c13 = Constraint(expr=0.712002743509966*m.x89*m.x94 + 1.5145252284653*m.x89*m.x108 + 0.712002743509966*m.x94*m.x89 - 
                        1.42400548701993*m.x94**2 - 1.5145252284653*m.x94*m.x103 - 1.5145252284653*m.x103*m.x94 + 
                        0.712002743509966*m.x103*m.x108 + 1.5145252284653*m.x108*m.x89 + 0.712002743509966*m.x108*m.x103
                         - 1.42400548701993*m.x108**2 + m.x12 == 0)

m.c14 = Constraint(expr=3.42049033074784*m.x84*m.x85 - 6.84098066149567*m.x84**2 - 10.7892769908458*m.x84*m.x99 + 
                        3.42049033074784*m.x85*m.x84 + 10.7892769908458*m.x85*m.x98 + 10.7892769908458*m.x98*m.x85 - 
                        6.84098066149567*m.x98**2 + 3.42049033074784*m.x98*m.x99 - 10.7892769908458*m.x99*m.x84 + 
                        3.42049033074784*m.x99*m.x98 + m.x13 == 0)

m.c15 = Constraint(expr=3.42049033074784*m.x84*m.x85 + 10.7892769908458*m.x84*m.x99 + 3.42049033074784*m.x85*m.x84 - 
                        6.84098066149567*m.x85**2 - 10.7892769908458*m.x85*m.x98 - 10.7892769908458*m.x98*m.x85 + 
                        3.42049033074784*m.x98*m.x99 + 10.7892769908458*m.x99*m.x84 + 3.42049033074784*m.x99*m.x98 - 
                        6.84098066149567*m.x99**2 + m.x14 == 0)

m.c16 = Constraint(expr=1.54946370191899*m.x86*m.x93 - 3.09892740383799*m.x86**2 - 3.05137772409656*m.x86*m.x107 + 
                        1.54946370191899*m.x93*m.x86 + 3.05137772409656*m.x93*m.x100 + 3.05137772409656*m.x100*m.x93 - 
                        3.09892740383799*m.x100**2 + 1.54946370191899*m.x100*m.x107 - 3.05137772409656*m.x107*m.x86 + 
                        1.54946370191899*m.x107*m.x100 + m.x15 == 0)

m.c17 = Constraint(expr=1.54946370191899*m.x86*m.x93 + 3.05137772409656*m.x86*m.x107 + 1.54946370191899*m.x93*m.x86 - 
                        3.09892740383799*m.x93**2 - 3.05137772409656*m.x93*m.x100 - 3.05137772409656*m.x100*m.x93 + 
                        1.54946370191899*m.x100*m.x107 + 3.05137772409656*m.x107*m.x86 + 1.54946370191899*m.x107*m.x100
                         - 3.09892740383799*m.x107**2 + m.x16 == 0)

m.c18 = Constraint(expr=2.83848992336077*m.x88*m.x101 - 2.83848992336077*m.x87*m.x102 + 2.83848992336077*m.x101*m.x88 - 
                        2.83848992336077*m.x102*m.x87 + m.x17 == 0)

m.c19 = Constraint(expr=2.83848992336077*m.x87*m.x102 - 2.83848992336077*m.x88*m.x101 - 2.83848992336077*m.x101*m.x88 + 
                        2.83848992336077*m.x102*m.x87 + m.x18 == 0)

m.c20 = Constraint(expr=0.568497078903163*m.x93*m.x94 - 1.13699415780633*m.x93**2 - 1.15748173755268*m.x93*m.x108 + 
                        0.568497078903163*m.x94*m.x93 + 1.15748173755268*m.x94*m.x107 + 1.15748173755268*m.x107*m.x94 - 
                        1.13699415780633*m.x107**2 + 0.568497078903163*m.x107*m.x108 - 1.15748173755268*m.x108*m.x93 + 
                        0.568497078903163*m.x108*m.x107 + m.x19 == 0)

m.c21 = Constraint(expr=0.568497078903163*m.x93*m.x94 + 1.15748173755268*m.x93*m.x108 + 0.568497078903163*m.x94*m.x93 - 
                        1.13699415780633*m.x94**2 - 1.15748173755268*m.x94*m.x107 - 1.15748173755268*m.x107*m.x94 + 
                        0.568497078903163*m.x107*m.x108 + 1.15748173755268*m.x108*m.x93 + 0.568497078903163*m.x108*
                        m.x107 - 1.13699415780633*m.x108**2 + m.x20 == 0)

m.c22 = Constraint(expr=0.762983720225487*m.x86*m.x92 - 1.52596744045097*m.x86**2 - 1.5879819825147*m.x86*m.x106 + 
                        0.762983720225487*m.x92*m.x86 + 1.5879819825147*m.x92*m.x100 + 1.5879819825147*m.x100*m.x92 - 
                        1.52596744045097*m.x100**2 + 0.762983720225487*m.x100*m.x106 - 1.5879819825147*m.x106*m.x86 + 
                        0.762983720225487*m.x106*m.x100 + m.x21 == 0)

m.c23 = Constraint(expr=0.762983720225487*m.x86*m.x92 + 1.5879819825147*m.x86*m.x106 + 0.762983720225487*m.x92*m.x86 - 
                        1.52596744045097*m.x92**2 - 1.5879819825147*m.x92*m.x100 - 1.5879819825147*m.x100*m.x92 + 
                        0.762983720225487*m.x100*m.x106 + 1.5879819825147*m.x106*m.x86 + 0.762983720225487*m.x106*m.x100
                         - 1.52596744045097*m.x106**2 + m.x22 == 0)

m.c24 = Constraint(expr=0.97751428158863*m.x86*m.x91 - 1.95502856317726*m.x86**2 - 2.04703717212022*m.x86*m.x105 + 
                        0.97751428158863*m.x91*m.x86 + 2.04703717212022*m.x91*m.x100 + 2.04703717212022*m.x100*m.x91 - 
                        1.95502856317726*m.x100**2 + 0.97751428158863*m.x100*m.x105 - 2.04703717212022*m.x105*m.x86 + 
                        0.97751428158863*m.x105*m.x100 + m.x23 == 0)

m.c25 = Constraint(expr=0.97751428158863*m.x86*m.x91 + 2.04703717212022*m.x86*m.x105 + 0.97751428158863*m.x91*m.x86 - 
                        1.95502856317726*m.x91**2 - 2.04703717212022*m.x91*m.x100 - 2.04703717212022*m.x100*m.x91 + 
                        0.97751428158863*m.x100*m.x105 + 2.04703717212022*m.x105*m.x86 + 0.97751428158863*m.x105*m.x100
                         - 1.95502856317726*m.x105**2 + m.x24 == 0)

m.c26 = Constraint(expr=1.24451229341096*m.x92*m.x93 - 2.48902458682192*m.x92**2 - 1.12598731308611*m.x92*m.x107 + 
                        1.24451229341096*m.x93*m.x92 + 1.12598731308611*m.x93*m.x106 + 1.12598731308611*m.x106*m.x93 - 
                        2.48902458682192*m.x106**2 + 1.24451229341096*m.x106*m.x107 - 1.12598731308611*m.x107*m.x92 + 
                        1.24451229341096*m.x107*m.x106 + m.x25 == 0)

m.c27 = Constraint(expr=1.24451229341096*m.x92*m.x93 + 1.12598731308611*m.x92*m.x107 + 1.24451229341096*m.x93*m.x92 - 
                        2.48902458682192*m.x93**2 - 1.12598731308611*m.x93*m.x106 - 1.12598731308611*m.x106*m.x93 + 
                        1.24451229341096*m.x106*m.x107 + 1.12598731308611*m.x107*m.x92 + 1.24451229341096*m.x107*m.x106
                         - 2.48902458682192*m.x107**2 + m.x26 == 0)

m.c28 = Constraint(expr=0.512948727485094*m.x81*m.x85 - 1.02589745497019*m.x81**2 - 2.11749184116742*m.x81*m.x99 + 
                        0.512948727485094*m.x85*m.x81 + 2.11749184116742*m.x85*m.x95 + 2.11749184116742*m.x95*m.x85 - 
                        1.02589745497019*m.x95**2 + 0.512948727485094*m.x95*m.x99 - 2.11749184116742*m.x99*m.x81 + 
                        0.512948727485094*m.x99*m.x95 + m.x27 == 0)

m.c29 = Constraint(expr=0.512948727485094*m.x81*m.x85 + 2.11749184116742*m.x81*m.x99 + 0.512948727485094*m.x85*m.x81 - 
                        1.02589745497019*m.x85**2 - 2.11749184116742*m.x85*m.x95 - 2.11749184116742*m.x95*m.x85 + 
                        0.512948727485094*m.x95*m.x99 + 2.11749184116742*m.x99*m.x81 + 0.512948727485094*m.x99*m.x95 - 
                        1.02589745497019*m.x99**2 + m.x28 == 0)

m.c30 = Constraint(expr=1.95102477622371*m.x89*m.x90 - 3.90204955244743*m.x89**2 - 5.18269706353046*m.x89*m.x104 + 
                        1.95102477622371*m.x90*m.x89 + 5.18269706353046*m.x90*m.x103 + 5.18269706353046*m.x103*m.x90 - 
                        3.90204955244743*m.x103**2 + 1.95102477622371*m.x103*m.x104 - 5.18269706353046*m.x104*m.x89 + 
                        1.95102477622371*m.x104*m.x103 + m.x29 == 0)

m.c31 = Constraint(expr=1.95102477622371*m.x89*m.x90 + 5.18269706353046*m.x89*m.x104 + 1.95102477622371*m.x90*m.x89 - 
                        3.90204955244743*m.x90**2 - 5.18269706353046*m.x90*m.x103 - 5.18269706353046*m.x103*m.x90 + 
                        1.95102477622371*m.x103*m.x104 + 5.18269706353046*m.x104*m.x89 + 1.95102477622371*m.x104*m.x103
                         - 3.90204955244743*m.x104**2 + m.x30 == 0)

m.c32 = Constraint(expr=2.49956580039902*m.x81*m.x82 - 4.99913160079803*m.x81**2 - 7.63154326158978*m.x81*m.x96 + 
                        2.49956580039902*m.x82*m.x81 + 7.63154326158978*m.x82*m.x95 + 7.63154326158978*m.x95*m.x82 - 
                        4.99913160079803*m.x95**2 + 2.49956580039902*m.x95*m.x96 - 7.63154326158978*m.x96*m.x81 + 
                        2.49956580039902*m.x96*m.x95 + m.x31 == 0)

m.c33 = Constraint(expr=2.49956580039902*m.x81*m.x82 + 7.63154326158978*m.x81*m.x96 + 2.49956580039902*m.x82*m.x81 - 
                        4.99913160079803*m.x82**2 - 7.63154326158978*m.x82*m.x95 - 7.63154326158978*m.x95*m.x82 + 
                        2.49956580039902*m.x95*m.x96 + 7.63154326158978*m.x96*m.x81 + 2.49956580039902*m.x96*m.x95 - 
                        4.99913160079803*m.x96**2 + m.x32 == 0)

m.c34 = Constraint(expr=0.850569833547202*m.x82*m.x85 - 1.7011396670944*m.x82**2 - 2.59696369898486*m.x82*m.x99 + 
                        0.850569833547202*m.x85*m.x82 + 2.59696369898486*m.x85*m.x96 + 2.59696369898486*m.x96*m.x85 - 
                        1.7011396670944*m.x96**2 + 0.850569833547202*m.x96*m.x99 - 2.59696369898486*m.x99*m.x82 + 
                        0.850569833547202*m.x99*m.x96 + m.x33 == 0)

m.c35 = Constraint(expr=0.850569833547202*m.x82*m.x85 + 2.59696369898486*m.x82*m.x99 + 0.850569833547202*m.x85*m.x82 - 
                        1.7011396670944*m.x85**2 - 2.59696369898486*m.x85*m.x96 - 2.59696369898486*m.x96*m.x85 + 
                        0.850569833547202*m.x96*m.x99 + 2.59696369898486*m.x99*m.x82 + 0.850569833547202*m.x99*m.x96 - 
                        1.7011396670944*m.x99**2 + m.x34 == 0)

m.c36 = Constraint(expr=0.99298785496278*m.x83*m.x84 - 1.98597570992556*m.x83**2 - 2.53440848879696*m.x83*m.x98 + 
                        0.99298785496278*m.x84*m.x83 + 2.53440848879696*m.x84*m.x97 + 2.53440848879696*m.x97*m.x84 - 
                        1.98597570992556*m.x97**2 + 0.99298785496278*m.x97*m.x98 - 2.53440848879696*m.x98*m.x83 + 
                        0.99298785496278*m.x98*m.x97 + m.x35 == 0)

m.c37 = Constraint(expr=0.99298785496278*m.x83*m.x84 + 2.53440848879696*m.x83*m.x98 + 0.99298785496278*m.x84*m.x83 - 
                        1.98597570992556*m.x84**2 - 2.53440848879696*m.x84*m.x97 - 2.53440848879696*m.x97*m.x84 + 
                        0.99298785496278*m.x97*m.x98 + 2.53440848879696*m.x98*m.x83 + 0.99298785496278*m.x98*m.x97 - 
                        1.98597570992556*m.x98**2 + m.x36 == 0)

m.c38 = Constraint(expr=0.898989535761804*m.x89*m.x98 - 0.898989535761804*m.x84*m.x103 + 0.898989535761804*m.x98*m.x89
                         - 0.898989535761804*m.x103*m.x84 + m.x37 == 0)

m.c39 = Constraint(expr=0.898989535761804*m.x84*m.x103 - 0.898989535761804*m.x89*m.x98 - 0.898989535761804*m.x98*m.x89
                         + 0.898989535761804*m.x103*m.x84 + m.x38 == 0)

m.c40 = Constraint(expr=0.843016575307471*m.x82*m.x84 - 1.68603315061494*m.x82**2 - 2.55791916293604*m.x82*m.x98 + 
                        0.843016575307471*m.x84*m.x82 + 2.55791916293604*m.x84*m.x96 + 2.55791916293604*m.x96*m.x84 - 
                        1.68603315061494*m.x96**2 + 0.843016575307471*m.x96*m.x98 - 2.55791916293604*m.x98*m.x82 + 
                        0.843016575307471*m.x98*m.x96 + m.x39 == 0)

m.c41 = Constraint(expr=0.843016575307471*m.x82*m.x84 + 2.55791916293604*m.x82*m.x98 + 0.843016575307471*m.x84*m.x82 - 
                        1.68603315061494*m.x84**2 - 2.55791916293604*m.x84*m.x96 - 2.55791916293604*m.x96*m.x84 + 
                        0.843016575307471*m.x96*m.x98 + 2.55791916293604*m.x98*m.x82 + 0.843016575307471*m.x98*m.x96 - 
                        1.68603315061494*m.x98**2 + m.x40 == 0)

m.c42 = Constraint(expr=2.39093157587886*m.x82*m.x83 - 4.75996315175772*m.x82**2 + 0.567509596153698*m.x82*m.x97 + 
                        2.39093157587886*m.x83*m.x82 - 0.567509596153698*m.x83*m.x96 - 0.567509596153698*m.x96*m.x83 - 
                        4.75996315175772*m.x96**2 + 2.39093157587886*m.x96*m.x97 + 0.567509596153698*m.x97*m.x82 + 
                        2.39093157587886*m.x97*m.x96 + m.x41 == 0)

m.c43 = Constraint(expr=2.39093157587886*m.x82*m.x83 - 0.567509596153698*m.x82*m.x97 + 2.39093157587886*m.x83*m.x82 - 
                        4.75996315175772*m.x83**2 + 0.567509596153698*m.x83*m.x96 + 0.567509596153698*m.x96*m.x83 + 
                        2.39093157587886*m.x96*m.x97 - 0.567509596153698*m.x97*m.x82 + 2.39093157587886*m.x97*m.x96 - 
                        4.75996315175772*m.x97**2 + m.x42 == 0)

m.c44 = Constraint(expr=4.54504135987637*m.x87*m.x89 - 9.09008271975275*m.x87**2 + 4.54504135987637*m.x89*m.x87 - 
                        9.09008271975275*m.x101**2 + 4.54504135987637*m.x101*m.x103 + 4.54504135987637*m.x103*m.x101
                         + m.x43 == 0)

m.c45 = Constraint(expr=4.54504135987637*m.x87*m.x89 + 4.54504135987637*m.x89*m.x87 - 9.09008271975275*m.x89**2 + 
                        4.54504135987637*m.x101*m.x103 + 4.54504135987637*m.x103*m.x101 - 9.09008271975275*m.x103**2
                         + m.x44 == 0)

m.c46 = Constraint(expr=2.20147187473026*m.x90*m.x91 - 4.40294374946052*m.x90**2 + 0.9404423768502*m.x90*m.x105 + 
                        2.20147187473026*m.x91*m.x90 - 0.9404423768502*m.x91*m.x104 - 0.9404423768502*m.x104*m.x91 - 
                        4.40294374946052*m.x104**2 + 2.20147187473026*m.x104*m.x105 + 0.9404423768502*m.x105*m.x90 + 
                        2.20147187473026*m.x105*m.x104 + m.x45 == 0)

m.c47 = Constraint(expr=2.20147187473026*m.x90*m.x91 - 0.9404423768502*m.x90*m.x105 + 2.20147187473026*m.x91*m.x90 - 
                        4.40294374946052*m.x91**2 + 0.9404423768502*m.x91*m.x104 + 0.9404423768502*m.x104*m.x91 + 
                        2.20147187473026*m.x104*m.x105 - 0.9404423768502*m.x105*m.x90 + 2.20147187473026*m.x105*m.x104
                         - 4.40294374946052*m.x105**2 + m.x46 == 0)

m.c48 = Constraint(expr=2.39097169089518*m.x84*m.x87 - 4.78194338179036*m.x84**2 + 2.39097169089518*m.x87*m.x84 - 
                        4.78194338179036*m.x98**2 + 2.39097169089518*m.x98*m.x101 + 2.39097169089518*m.x101*m.x98
                         + m.x47 == 0)

m.c49 = Constraint(expr=2.39097169089518*m.x84*m.x87 + 2.39097169089518*m.x87*m.x84 - 4.78194338179036*m.x87**2 + 
                        2.39097169089518*m.x98*m.x101 + 2.39097169089518*m.x101*m.x98 - 4.78194338179036*m.x101**2
                         + m.x48 == 0)

m.c50 = Constraint(expr=1.98396952622808*m.x85*m.x86 - 3.96793905245615*m.x85**2 + 1.98396952622808*m.x86*m.x85 - 
                        3.96793905245615*m.x99**2 + 1.98396952622808*m.x99*m.x100 + 1.98396952622808*m.x100*m.x99
                         + m.x49 == 0)

m.c51 = Constraint(expr=1.98396952622808*m.x85*m.x86 + 1.98396952622808*m.x86*m.x85 - 3.96793905245615*m.x86**2 + 
                        1.98396952622808*m.x99*m.x100 + 1.98396952622808*m.x100*m.x99 - 3.96793905245615*m.x100**2
                         + m.x50 == 0)

m.c52 = Constraint(expr=1.5145252284653*m.x89*m.x94 - 3.0290504569306*m.x89**2 + 0.712002743509966*m.x89*m.x108 + 
                        1.5145252284653*m.x94*m.x89 - 0.712002743509966*m.x94*m.x103 - 0.712002743509966*m.x103*m.x94 - 
                        3.0290504569306*m.x103**2 + 1.5145252284653*m.x103*m.x108 + 0.712002743509966*m.x108*m.x89 + 
                        1.5145252284653*m.x108*m.x103 + m.x51 == 0)

m.c53 = Constraint(expr=1.5145252284653*m.x89*m.x94 - 0.712002743509966*m.x89*m.x108 + 1.5145252284653*m.x94*m.x89 - 
                        3.0290504569306*m.x94**2 + 0.712002743509966*m.x94*m.x103 + 0.712002743509966*m.x103*m.x94 + 
                        1.5145252284653*m.x103*m.x108 - 0.712002743509966*m.x108*m.x89 + 1.5145252284653*m.x108*m.x103
                         - 3.0290504569306*m.x108**2 + m.x52 == 0)

m.c54 = Constraint(expr=10.7892769908458*m.x84*m.x85 - 21.5785539816916*m.x84**2 + 3.42049033074784*m.x84*m.x99 + 
                        10.7892769908458*m.x85*m.x84 - 3.42049033074784*m.x85*m.x98 - 3.42049033074784*m.x98*m.x85 - 
                        21.5785539816916*m.x98**2 + 10.7892769908458*m.x98*m.x99 + 3.42049033074784*m.x99*m.x84 + 
                        10.7892769908458*m.x99*m.x98 + m.x53 == 0)

m.c55 = Constraint(expr=10.7892769908458*m.x84*m.x85 - 3.42049033074784*m.x84*m.x99 + 10.7892769908458*m.x85*m.x84 - 
                        21.5785539816916*m.x85**2 + 3.42049033074784*m.x85*m.x98 + 3.42049033074784*m.x98*m.x85 + 
                        10.7892769908458*m.x98*m.x99 - 3.42049033074784*m.x99*m.x84 + 10.7892769908458*m.x99*m.x98 - 
                        21.5785539816916*m.x99**2 + m.x54 == 0)

m.c56 = Constraint(expr=3.05137772409656*m.x86*m.x93 - 6.10275544819311*m.x86**2 + 1.54946370191899*m.x86*m.x107 + 
                        3.05137772409656*m.x93*m.x86 - 1.54946370191899*m.x93*m.x100 - 1.54946370191899*m.x100*m.x93 - 
                        6.10275544819311*m.x100**2 + 3.05137772409656*m.x100*m.x107 + 1.54946370191899*m.x107*m.x86 + 
                        3.05137772409656*m.x107*m.x100 + m.x55 == 0)

m.c57 = Constraint(expr=3.05137772409656*m.x86*m.x93 - 1.54946370191899*m.x86*m.x107 + 3.05137772409656*m.x93*m.x86 - 
                        6.10275544819311*m.x93**2 + 1.54946370191899*m.x93*m.x100 + 1.54946370191899*m.x100*m.x93 + 
                        3.05137772409656*m.x100*m.x107 - 1.54946370191899*m.x107*m.x86 + 3.05137772409656*m.x107*m.x100
                         - 6.10275544819311*m.x107**2 + m.x56 == 0)

m.c58 = Constraint(expr=2.83848992336077*m.x87*m.x88 - 5.67697984672154*m.x87**2 + 2.83848992336077*m.x88*m.x87 - 
                        5.67697984672154*m.x101**2 + 2.83848992336077*m.x101*m.x102 + 2.83848992336077*m.x102*m.x101
                         + m.x57 == 0)

m.c59 = Constraint(expr=2.83848992336077*m.x87*m.x88 + 2.83848992336077*m.x88*m.x87 - 5.67697984672154*m.x88**2 + 
                        2.83848992336077*m.x101*m.x102 + 2.83848992336077*m.x102*m.x101 - 5.67697984672154*m.x102**2
                         + m.x58 == 0)

m.c60 = Constraint(expr=1.15748173755268*m.x93*m.x94 - 2.31496347510535*m.x93**2 + 0.568497078903163*m.x93*m.x108 + 
                        1.15748173755268*m.x94*m.x93 - 0.568497078903163*m.x94*m.x107 - 0.568497078903163*m.x107*m.x94
                         - 2.31496347510535*m.x107**2 + 1.15748173755268*m.x107*m.x108 + 0.568497078903163*m.x108*m.x93
                         + 1.15748173755268*m.x108*m.x107 + m.x59 == 0)

m.c61 = Constraint(expr=1.15748173755268*m.x93*m.x94 - 0.568497078903163*m.x93*m.x108 + 1.15748173755268*m.x94*m.x93 - 
                        2.31496347510535*m.x94**2 + 0.568497078903163*m.x94*m.x107 + 0.568497078903163*m.x107*m.x94 + 
                        1.15748173755268*m.x107*m.x108 - 0.568497078903163*m.x108*m.x93 + 1.15748173755268*m.x108*m.x107
                         - 2.31496347510535*m.x108**2 + m.x60 == 0)

m.c62 = Constraint(expr=1.5879819825147*m.x86*m.x92 - 3.1759639650294*m.x86**2 + 0.762983720225487*m.x86*m.x106 + 
                        1.5879819825147*m.x92*m.x86 - 0.762983720225487*m.x92*m.x100 - 0.762983720225487*m.x100*m.x92 - 
                        3.1759639650294*m.x100**2 + 1.5879819825147*m.x100*m.x106 + 0.762983720225487*m.x106*m.x86 + 
                        1.5879819825147*m.x106*m.x100 + m.x61 == 0)

m.c63 = Constraint(expr=1.5879819825147*m.x86*m.x92 - 0.762983720225487*m.x86*m.x106 + 1.5879819825147*m.x92*m.x86 - 
                        3.1759639650294*m.x92**2 + 0.762983720225487*m.x92*m.x100 + 0.762983720225487*m.x100*m.x92 + 
                        1.5879819825147*m.x100*m.x106 - 0.762983720225487*m.x106*m.x86 + 1.5879819825147*m.x106*m.x100
                         - 3.1759639650294*m.x106**2 + m.x62 == 0)

m.c64 = Constraint(expr=2.04703717212022*m.x86*m.x91 - 4.09407434424044*m.x86**2 + 0.97751428158863*m.x86*m.x105 + 
                        2.04703717212022*m.x91*m.x86 - 0.97751428158863*m.x91*m.x100 - 0.97751428158863*m.x100*m.x91 - 
                        4.09407434424044*m.x100**2 + 2.04703717212022*m.x100*m.x105 + 0.97751428158863*m.x105*m.x86 + 
                        2.04703717212022*m.x105*m.x100 + m.x63 == 0)

m.c65 = Constraint(expr=2.04703717212022*m.x86*m.x91 - 0.97751428158863*m.x86*m.x105 + 2.04703717212022*m.x91*m.x86 - 
                        4.09407434424044*m.x91**2 + 0.97751428158863*m.x91*m.x100 + 0.97751428158863*m.x100*m.x91 + 
                        2.04703717212022*m.x100*m.x105 - 0.97751428158863*m.x105*m.x86 + 2.04703717212022*m.x105*m.x100
                         - 4.09407434424044*m.x105**2 + m.x64 == 0)

m.c66 = Constraint(expr=1.12598731308611*m.x92*m.x93 - 2.25197462617221*m.x92**2 + 1.24451229341096*m.x92*m.x107 + 
                        1.12598731308611*m.x93*m.x92 - 1.24451229341096*m.x93*m.x106 - 1.24451229341096*m.x106*m.x93 - 
                        2.25197462617221*m.x106**2 + 1.12598731308611*m.x106*m.x107 + 1.24451229341096*m.x107*m.x92 + 
                        1.12598731308611*m.x107*m.x106 + m.x65 == 0)

m.c67 = Constraint(expr=1.12598731308611*m.x92*m.x93 - 1.24451229341096*m.x92*m.x107 + 1.12598731308611*m.x93*m.x92 - 
                        2.25197462617221*m.x93**2 + 1.24451229341096*m.x93*m.x106 + 1.24451229341096*m.x106*m.x93 + 
                        1.12598731308611*m.x106*m.x107 - 1.24451229341096*m.x107*m.x92 + 1.12598731308611*m.x107*m.x106
                         - 2.25197462617221*m.x107**2 + m.x66 == 0)

m.c68 = Constraint(expr=2.11749184116742*m.x81*m.x85 - 4.21038368233483*m.x81**2 + 0.512948727485094*m.x81*m.x99 + 
                        2.11749184116742*m.x85*m.x81 - 0.512948727485094*m.x85*m.x95 - 0.512948727485094*m.x95*m.x85 - 
                        4.21038368233483*m.x95**2 + 2.11749184116742*m.x95*m.x99 + 0.512948727485094*m.x99*m.x81 + 
                        2.11749184116742*m.x99*m.x95 + m.x67 == 0)

m.c69 = Constraint(expr=2.11749184116742*m.x81*m.x85 - 0.512948727485094*m.x81*m.x99 + 2.11749184116742*m.x85*m.x81 - 
                        4.21038368233483*m.x85**2 + 0.512948727485094*m.x85*m.x95 + 0.512948727485094*m.x95*m.x85 + 
                        2.11749184116742*m.x95*m.x99 - 0.512948727485094*m.x99*m.x81 + 2.11749184116742*m.x99*m.x95 - 
                        4.21038368233483*m.x99**2 + m.x68 == 0)

m.c70 = Constraint(expr=5.18269706353046*m.x89*m.x90 - 10.3653941270609*m.x89**2 + 1.95102477622371*m.x89*m.x104 + 
                        5.18269706353046*m.x90*m.x89 - 1.95102477622371*m.x90*m.x103 - 1.95102477622371*m.x103*m.x90 - 
                        10.3653941270609*m.x103**2 + 5.18269706353046*m.x103*m.x104 + 1.95102477622371*m.x104*m.x89 + 
                        5.18269706353046*m.x104*m.x103 + m.x69 == 0)

m.c71 = Constraint(expr=5.18269706353046*m.x89*m.x90 - 1.95102477622371*m.x89*m.x104 + 5.18269706353046*m.x90*m.x89 - 
                        10.3653941270609*m.x90**2 + 1.95102477622371*m.x90*m.x103 + 1.95102477622371*m.x103*m.x90 + 
                        5.18269706353046*m.x103*m.x104 - 1.95102477622371*m.x104*m.x89 + 5.18269706353046*m.x104*m.x103
                         - 10.3653941270609*m.x104**2 + m.x70 == 0)

m.c72 = Constraint(expr=7.63154326158978*m.x81*m.x82 - 15.2366865231796*m.x81**2 + 2.49956580039902*m.x81*m.x96 + 
                        7.63154326158978*m.x82*m.x81 - 2.49956580039902*m.x82*m.x95 - 2.49956580039902*m.x95*m.x82 - 
                        15.2366865231796*m.x95**2 + 7.63154326158978*m.x95*m.x96 + 2.49956580039902*m.x96*m.x81 + 
                        7.63154326158978*m.x96*m.x95 + m.x71 == 0)

m.c73 = Constraint(expr=7.63154326158978*m.x81*m.x82 - 2.49956580039902*m.x81*m.x96 + 7.63154326158978*m.x82*m.x81 - 
                        15.2366865231796*m.x82**2 + 2.49956580039902*m.x82*m.x95 + 2.49956580039902*m.x95*m.x82 + 
                        7.63154326158978*m.x95*m.x96 - 2.49956580039902*m.x96*m.x81 + 7.63154326158978*m.x96*m.x95 - 
                        15.2366865231796*m.x96**2 + m.x72 == 0)

m.c74 = Constraint(expr=2.59696369898486*m.x82*m.x85 - 5.17662739796971*m.x82**2 + 0.850569833547202*m.x82*m.x99 + 
                        2.59696369898486*m.x85*m.x82 - 0.850569833547202*m.x85*m.x96 - 0.850569833547202*m.x96*m.x85 - 
                        5.17662739796971*m.x96**2 + 2.59696369898486*m.x96*m.x99 + 0.850569833547202*m.x99*m.x82 + 
                        2.59696369898486*m.x99*m.x96 + m.x73 == 0)

m.c75 = Constraint(expr=2.59696369898486*m.x82*m.x85 - 0.850569833547202*m.x82*m.x99 + 2.59696369898486*m.x85*m.x82 - 
                        5.17662739796971*m.x85**2 + 0.850569833547202*m.x85*m.x96 + 0.850569833547202*m.x96*m.x85 + 
                        2.59696369898486*m.x96*m.x99 - 0.850569833547202*m.x99*m.x82 + 2.59696369898486*m.x99*m.x96 - 
                        5.17662739796971*m.x99**2 + m.x74 == 0)

m.c76 = Constraint(expr=2.53440848879696*m.x83*m.x84 - 5.06241697759392*m.x83**2 + 0.99298785496278*m.x83*m.x98 + 
                        2.53440848879696*m.x84*m.x83 - 0.99298785496278*m.x84*m.x97 - 0.99298785496278*m.x97*m.x84 - 
                        5.06241697759392*m.x97**2 + 2.53440848879696*m.x97*m.x98 + 0.99298785496278*m.x98*m.x83 + 
                        2.53440848879696*m.x98*m.x97 + m.x75 == 0)

m.c77 = Constraint(expr=2.53440848879696*m.x83*m.x84 - 0.99298785496278*m.x83*m.x98 + 2.53440848879696*m.x84*m.x83 - 
                        5.06241697759392*m.x84**2 + 0.99298785496278*m.x84*m.x97 + 0.99298785496278*m.x97*m.x84 + 
                        2.53440848879696*m.x97*m.x98 - 0.99298785496278*m.x98*m.x83 + 2.53440848879696*m.x98*m.x97 - 
                        5.06241697759392*m.x98**2 + m.x76 == 0)

m.c78 = Constraint(expr=0.898989535761804*m.x84*m.x89 - 1.79797907152361*m.x84**2 + 0.898989535761804*m.x89*m.x84 - 
                        1.79797907152361*m.x98**2 + 0.898989535761804*m.x98*m.x103 + 0.898989535761804*m.x103*m.x98
                         + m.x77 == 0)

m.c79 = Constraint(expr=0.898989535761804*m.x84*m.x89 + 0.898989535761804*m.x89*m.x84 - 1.79797907152361*m.x89**2 + 
                        0.898989535761804*m.x98*m.x103 + 0.898989535761804*m.x103*m.x98 - 1.79797907152361*m.x103**2
                         + m.x78 == 0)

m.c80 = Constraint(expr=2.55791916293604*m.x82*m.x84 - 5.09883832587208*m.x82**2 + 0.843016575307471*m.x82*m.x98 + 
                        2.55791916293604*m.x84*m.x82 - 0.843016575307471*m.x84*m.x96 - 0.843016575307471*m.x96*m.x84 - 
                        5.09883832587208*m.x96**2 + 2.55791916293604*m.x96*m.x98 + 0.843016575307471*m.x98*m.x82 + 
                        2.55791916293604*m.x98*m.x96 + m.x79 == 0)

m.c81 = Constraint(expr=2.55791916293604*m.x82*m.x84 - 0.843016575307471*m.x82*m.x98 + 2.55791916293604*m.x84*m.x82 - 
                        5.09883832587208*m.x84**2 + 0.843016575307471*m.x84*m.x96 + 0.843016575307471*m.x96*m.x84 + 
                        2.55791916293604*m.x96*m.x98 - 0.843016575307471*m.x98*m.x82 + 2.55791916293604*m.x98*m.x96 - 
                        5.09883832587208*m.x98**2 + m.x80 == 0)

m.c82 = Constraint(expr=m.x1**2 + m.x41**2 <= 9801)

m.c83 = Constraint(expr=m.x2**2 + m.x42**2 <= 9801)

m.c84 = Constraint(expr=m.x3**2 + m.x43**2 <= 9801)

m.c85 = Constraint(expr=m.x4**2 + m.x44**2 <= 9801)

m.c86 = Constraint(expr=m.x5**2 + m.x45**2 <= 9801)

m.c87 = Constraint(expr=m.x6**2 + m.x46**2 <= 9801)

m.c88 = Constraint(expr=m.x7**2 + m.x47**2 <= 9801)

m.c89 = Constraint(expr=m.x8**2 + m.x48**2 <= 9801)

m.c90 = Constraint(expr=m.x9**2 + m.x49**2 <= 9801)

m.c91 = Constraint(expr=m.x10**2 + m.x50**2 <= 9801)

m.c92 = Constraint(expr=m.x11**2 + m.x51**2 <= 9801)

m.c93 = Constraint(expr=m.x12**2 + m.x52**2 <= 9801)

m.c94 = Constraint(expr=m.x13**2 + m.x53**2 <= 9801)

m.c95 = Constraint(expr=m.x14**2 + m.x54**2 <= 9801)

m.c96 = Constraint(expr=m.x15**2 + m.x55**2 <= 9801)

m.c97 = Constraint(expr=m.x16**2 + m.x56**2 <= 9801)

m.c98 = Constraint(expr=m.x17**2 + m.x57**2 <= 9801)

m.c99 = Constraint(expr=m.x18**2 + m.x58**2 <= 9801)

m.c100 = Constraint(expr=m.x19**2 + m.x59**2 <= 9801)

m.c101 = Constraint(expr=m.x20**2 + m.x60**2 <= 9801)

m.c102 = Constraint(expr=m.x21**2 + m.x61**2 <= 9801)

m.c103 = Constraint(expr=m.x22**2 + m.x62**2 <= 9801)

m.c104 = Constraint(expr=m.x23**2 + m.x63**2 <= 9801)

m.c105 = Constraint(expr=m.x24**2 + m.x64**2 <= 9801)

m.c106 = Constraint(expr=m.x25**2 + m.x65**2 <= 9801)

m.c107 = Constraint(expr=m.x26**2 + m.x66**2 <= 9801)

m.c108 = Constraint(expr=m.x27**2 + m.x67**2 <= 9801)

m.c109 = Constraint(expr=m.x28**2 + m.x68**2 <= 9801)

m.c110 = Constraint(expr=m.x29**2 + m.x69**2 <= 9801)

m.c111 = Constraint(expr=m.x30**2 + m.x70**2 <= 9801)

m.c112 = Constraint(expr=m.x31**2 + m.x71**2 <= 9801)

m.c113 = Constraint(expr=m.x32**2 + m.x72**2 <= 9801)

m.c114 = Constraint(expr=m.x33**2 + m.x73**2 <= 9801)

m.c115 = Constraint(expr=m.x34**2 + m.x74**2 <= 9801)

m.c116 = Constraint(expr=m.x35**2 + m.x75**2 <= 9801)

m.c117 = Constraint(expr=m.x36**2 + m.x76**2 <= 9801)

m.c118 = Constraint(expr=m.x37**2 + m.x77**2 <= 9801)

m.c119 = Constraint(expr=m.x38**2 + m.x78**2 <= 9801)

m.c120 = Constraint(expr=m.x39**2 + m.x79**2 <= 9801)

m.c121 = Constraint(expr=m.x40**2 + m.x80**2 <= 9801)

m.c122 = Constraint(expr=m.x81**2 + m.x95**2 <= 1.1236)

m.c123 = Constraint(expr=m.x82**2 + m.x96**2 <= 1.1236)

m.c124 = Constraint(expr=m.x83**2 + m.x97**2 <= 1.1236)

m.c125 = Constraint(expr=m.x84**2 + m.x98**2 <= 1.1236)

m.c126 = Constraint(expr=m.x85**2 + m.x99**2 <= 1.1236)

m.c127 = Constraint(expr=m.x86**2 + m.x100**2 <= 1.1236)

m.c128 = Constraint(expr=m.x87**2 + m.x101**2 <= 1.1236)

m.c129 = Constraint(expr=m.x88**2 + m.x102**2 <= 1.1236)

m.c130 = Constraint(expr=m.x89**2 + m.x103**2 <= 1.1236)

m.c131 = Constraint(expr=m.x90**2 + m.x104**2 <= 1.1236)

m.c132 = Constraint(expr=m.x91**2 + m.x105**2 <= 1.1236)

m.c133 = Constraint(expr=m.x92**2 + m.x106**2 <= 1.1236)

m.c134 = Constraint(expr=m.x93**2 + m.x107**2 <= 1.1236)

m.c135 = Constraint(expr=m.x94**2 + m.x108**2 <= 1.1236)

m.c136 = Constraint(expr=m.x81**2 + m.x95**2 >= 0.8836)

m.c137 = Constraint(expr=m.x82**2 + m.x96**2 >= 0.8836)

m.c138 = Constraint(expr=m.x83**2 + m.x97**2 >= 0.8836)

m.c139 = Constraint(expr=m.x84**2 + m.x98**2 >= 0.8836)

m.c140 = Constraint(expr=m.x85**2 + m.x99**2 >= 0.8836)

m.c141 = Constraint(expr=m.x86**2 + m.x100**2 >= 0.8836)

m.c142 = Constraint(expr=m.x87**2 + m.x101**2 >= 0.8836)

m.c143 = Constraint(expr=m.x88**2 + m.x102**2 >= 0.8836)

m.c144 = Constraint(expr=m.x89**2 + m.x103**2 >= 0.8836)

m.c145 = Constraint(expr=m.x90**2 + m.x104**2 >= 0.8836)

m.c146 = Constraint(expr=m.x91**2 + m.x105**2 >= 0.8836)

m.c147 = Constraint(expr=m.x92**2 + m.x106**2 >= 0.8836)

m.c148 = Constraint(expr=m.x93**2 + m.x107**2 >= 0.8836)

m.c149 = Constraint(expr=m.x94**2 + m.x108**2 >= 0.8836)

m.c150 = Constraint(expr=   m.x109 <= 3.324)

m.c151 = Constraint(expr=   m.x110 <= 1.4)

m.c152 = Constraint(expr=   m.x111 <= 1)

m.c153 = Constraint(expr=   m.x112 <= 1)

m.c154 = Constraint(expr=   m.x113 <= 1)

m.c155 = Constraint(expr=   m.x109 >= 0)

m.c156 = Constraint(expr=   m.x110 >= 0)

m.c157 = Constraint(expr=   m.x111 >= 0)

m.c158 = Constraint(expr=   m.x112 >= 0)

m.c159 = Constraint(expr=   m.x113 >= 0)

m.c160 = Constraint(expr=   m.x114 <= 0.1)

m.c161 = Constraint(expr=   m.x115 <= 0.5)

m.c162 = Constraint(expr=   m.x116 <= 0.4)

m.c163 = Constraint(expr=   m.x117 <= 0.24)

m.c164 = Constraint(expr=   m.x118 <= 0.24)

m.c165 = Constraint(expr=   m.x114 >= 0)

m.c166 = Constraint(expr=   m.x115 >= -0.4)

m.c167 = Constraint(expr=   m.x116 >= 0)

m.c168 = Constraint(expr=   m.x117 >= -0.06)

m.c169 = Constraint(expr=   m.x118 >= -0.06)

m.c170 = Constraint(expr=   m.x95 == 0)

m.c171 = Constraint(expr=   m.x27 + m.x31 - m.x109 == 0)

m.c172 = Constraint(expr=   m.x1 + m.x32 + m.x33 + m.x39 - m.x110 == -0.217)

m.c173 = Constraint(expr=   m.x2 + m.x35 - m.x111 == -0.942)

m.c174 = Constraint(expr=   m.x10 + m.x15 + m.x21 + m.x23 - m.x112 == -0.112)

m.c175 = Constraint(expr=   m.x18 - m.x113 == 0)

m.c176 = Constraint(expr=   m.x67 + m.x71 - m.x114 == 0)

m.c177 = Constraint(expr=   m.x41 + m.x72 + m.x73 + m.x79 - m.x115 == -0.127)

m.c178 = Constraint(expr=   m.x42 + m.x75 - m.x116 == -0.19)

m.c179 = Constraint(expr=   m.x50 + m.x55 + m.x61 + m.x63 - m.x117 == -0.075)

m.c180 = Constraint(expr=   m.x58 - m.x118 == 0)

m.c181 = Constraint(expr=   m.x7 + m.x13 + m.x36 + m.x37 + m.x40 == -0.478)

m.c182 = Constraint(expr=   m.x9 + m.x14 + m.x28 + m.x34 == -0.076)

m.c183 = Constraint(expr=   m.x3 + m.x8 + m.x17 == 0)

m.c184 = Constraint(expr=   m.x4 + m.x11 + m.x29 + m.x38 == -0.295)

m.c185 = Constraint(expr=   m.x5 + m.x30 == -0.09)

m.c186 = Constraint(expr=   m.x6 + m.x24 == -0.035)

m.c187 = Constraint(expr=   m.x22 + m.x25 == -0.061)

m.c188 = Constraint(expr=   m.x16 + m.x19 + m.x26 == -0.135)

m.c189 = Constraint(expr=   m.x12 + m.x20 == -0.149)

m.c190 = Constraint(expr=   m.x47 + m.x53 + m.x76 + m.x77 + m.x80 == 0.039)

m.c191 = Constraint(expr=   m.x49 + m.x54 + m.x68 + m.x74 == -0.016)

m.c192 = Constraint(expr=   m.x43 + m.x48 + m.x57 == 0)

m.c193 = Constraint(expr=   m.x44 + m.x51 + m.x69 + m.x78 == -0.166)

m.c194 = Constraint(expr=   m.x45 + m.x70 == -0.058)

m.c195 = Constraint(expr=   m.x46 + m.x64 == -0.018)

m.c196 = Constraint(expr=   m.x62 + m.x65 == -0.016)

m.c197 = Constraint(expr=   m.x56 + m.x59 + m.x66 == -0.058)

m.c198 = Constraint(expr=   m.x52 + m.x60 == -0.05)
