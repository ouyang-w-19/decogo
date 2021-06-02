#  MINLP written by GAMS Convert at 04/21/18 13:51:24
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        130       66       20       44        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        183      161       22        0        0        0        0        0
#  FX     45       34       11        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        692      260      432        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x2 = Var(within=Reals,bounds=(0.9,1.05),initialize=1)
m.x3 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x4 = Var(within=Reals,bounds=(0.9,1.05),initialize=1)
m.x5 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x6 = Var(within=Reals,bounds=(0.9,1.05),initialize=1)
m.x7 = Var(within=Reals,bounds=(0.9,1.05),initialize=1)
m.x8 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x9 = Var(within=Reals,bounds=(0.9,1.05),initialize=1)
m.x10 = Var(within=Reals,bounds=(0.9,1.05),initialize=1)
m.x11 = Var(within=Reals,bounds=(0.9,1.05),initialize=1)
m.x12 = Var(within=Reals,bounds=(0.9,1.05),initialize=1)
m.x13 = Var(within=Reals,bounds=(0.9,1.05),initialize=1)
m.x14 = Var(within=Reals,bounds=(0.9,1.05),initialize=1)
m.x15 = Var(within=Reals,bounds=(0.9,1.05),initialize=1)
m.x16 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x17 = Var(within=Reals,bounds=(1.06,1.06),initialize=1.06)
m.x18 = Var(within=Reals,bounds=(None,None),initialize=1.066509)
m.x19 = Var(within=Reals,bounds=(None,None),initialize=1.068869)
m.x20 = Var(within=Reals,bounds=(None,None),initialize=0.920165)
m.x21 = Var(within=Reals,bounds=(None,None),initialize=0.956102)
m.x22 = Var(within=Reals,bounds=(None,None),initialize=0.909677)
m.x23 = Var(within=Reals,bounds=(None,None),initialize=0.89072)
m.x24 = Var(within=Reals,bounds=(None,None),initialize=0.899717)
m.x25 = Var(within=Reals,bounds=(None,None),initialize=0.92757)
m.x26 = Var(within=Reals,bounds=(None,None),initialize=0.942703)
m.x27 = Var(within=Reals,bounds=(None,None),initialize=0.952092)
m.x28 = Var(within=Reals,bounds=(None,None),initialize=0.951126)
m.x29 = Var(within=Reals,bounds=(None,None),initialize=0.982623)
m.x30 = Var(within=Reals,bounds=(None,None),initialize=0.940819)
m.x31 = Var(within=Reals,bounds=(None,None),initialize=0.880136)
m.x32 = Var(within=Reals,bounds=(None,None),initialize=0.944062)
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
m.x49 = Var(within=Reals,bounds=(0,0),initialize=0)
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
m.x65 = Var(within=Reals,bounds=(0,4),initialize=0)
m.x66 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x67 = Var(within=Reals,bounds=(0,0.8),initialize=0)
m.x68 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x69 = Var(within=Reals,bounds=(0,1.2),initialize=0)
m.x70 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x71 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x72 = Var(within=Reals,bounds=(0,0.24),initialize=0)
m.x73 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x74 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x75 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x76 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x77 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x78 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x79 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x80 = Var(within=Reals,bounds=(0,0.5),initialize=0)
m.x81 = Var(within=Reals,bounds=(-0.2,0.6),initialize=0)
m.x82 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x83 = Var(within=Reals,bounds=(-0.08,0.2),initialize=0)
m.x84 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x85 = Var(within=Reals,bounds=(-0.3,0.6),initialize=0)
m.x86 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x87 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x88 = Var(within=Reals,bounds=(-0.1,0.13),initialize=0)
m.x89 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x90 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x91 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x92 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x93 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x94 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x95 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x96 = Var(within=Reals,bounds=(-0.04,0.24),initialize=0)
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
m.x119 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x120 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x121 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x122 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x123 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x124 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x125 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x126 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x127 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x128 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x129 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x130 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x131 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x132 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x133 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x134 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x135 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x136 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x137 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x138 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x139 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x140 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x141 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x142 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x143 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x144 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x145 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x146 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x147 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x148 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x149 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x150 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x151 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x152 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x153 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x154 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x155 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x156 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x157 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x158 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x159 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x160 = Var(within=Reals,bounds=(0,0),initialize=0)
m.b162 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b163 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b164 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b165 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b166 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b167 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b168 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b169 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b170 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b171 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b172 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b173 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b174 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b175 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b176 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b177 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b178 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b179 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b180 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b181 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b182 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b183 = Var(within=Binary,bounds=(0,0),initialize=0)

m.obj = Objective(expr=   100*m.x130 + 100*m.x132 + 100*m.x134 + 100*m.x135 + 100*m.x137 + 100*m.x138 + 100*m.x139
                        + 100*m.x140 + 100*m.x141 + 100*m.x142 + 100*m.x143 + 100*m.x146 + 100*m.x148 + 100*m.x150
                        + 100*m.x151 + 100*m.x153 + 100*m.x154 + 100*m.x155 + 100*m.x156 + 100*m.x157 + 100*m.x158
                        + 100*m.x159 + 10*m.b162 + 10*m.b163 + 10*m.b164 + 10*m.b165 + 10*m.b166 + 10*m.b167 + 10*m.b168
                        + 10*m.b169 + 10*m.b170 + 10*m.b171 + 10*m.b172 + 10*m.b173 + 10*m.b174 + 10*m.b175 + 10*m.b176
                        + 10*m.b177 + 10*m.b178 + 10*m.b179 + 10*m.b180 + 10*m.b181 + 10*m.b182 + 10*m.b183
                       , sense=minimize)

m.c1 = Constraint(expr=-(15.8964171454635*m.x1*m.x1 + m.x1*m.x2*(-2.26704183302539*cos(m.x34 - m.x33) - 18.5374266808153
                       *sin(m.x34 - m.x33)) + m.x1*m.x5*(-13.6293753124381*cos(m.x37 - m.x33) - 7.07407023136926*sin(
                       m.x37 - m.x33))) + m.x65 == 0)

m.c2 = Constraint(expr=-(m.x2*m.x1*(-2.26704183302539*cos(m.x33 - m.x34) - 18.5374266808153*sin(m.x33 - m.x34)) + 
                       3.53430764694598*m.x2*m.x2 + m.x2*m.x3*(-1.26726581392059*cos(m.x35 - m.x34) - 7.28131607739717*
                       sin(m.x35 - m.x34))) + m.x66 == 0)

m.c3 = Constraint(expr=-(m.x3*m.x2*(-1.26726581392059*cos(m.x34 - m.x35) - 7.28131607739717*sin(m.x34 - m.x35)) + 
                       1.5448109718374*m.x3*m.x3 + m.x3*m.x4*(-0.27754515791681*cos(m.x36 - m.x35) - 1.6615816969355*
                       sin(m.x36 - m.x35))) + m.x67 == 0)

m.c4 = Constraint(expr=-(m.x4*m.x3*(-0.27754515791681*cos(m.x35 - m.x36) - 1.6615816969355*sin(m.x35 - m.x36)) + 
                       2.29003563010891*m.x4*m.x4 + m.x4*m.x6*(-0.864296115364742*cos(m.x38 - m.x36) - 6.06886185353939*
                       sin(m.x38 - m.x36)) + m.x4*m.x7*(-0.824884423842853*cos(m.x39 - m.x36) - 6.35284123437183*sin(
                       m.x39 - m.x36)) + m.x4*m.x9*(-0.323309932984507*cos(m.x41 - m.x36) - 3.06668980551481*sin(m.x41
                        - m.x36)) - 10*m.x4*m.x16*sin(m.x48 - m.x36)) + m.x68 == 0)

m.c5 = Constraint(expr=-(m.x5*m.x1*(-13.6293753124381*cos(m.x33 - m.x37) - 7.07407023136926*sin(m.x33 - m.x37)) + 
                       14.9328222636193*m.x5*m.x5 + m.x5*m.x6*(-0.556466438117951*cos(m.x38 - m.x37) - 3.59715804640533*
                       sin(m.x38 - m.x37)) + m.x5*m.x7*(-0.746980513063235*cos(m.x39 - m.x37) - 3.99601522253739*sin(
                       m.x39 - m.x37))) + m.x69 == 0)

m.c6 = Constraint(expr=-(m.x6*m.x4*(-0.864296115364742*cos(m.x36 - m.x38) - 6.06886185353939*sin(m.x36 - m.x38)) + m.x6*
                       m.x5*(-0.556466438117951*cos(m.x37 - m.x38) - 3.59715804640533*sin(m.x37 - m.x38)) + 
                       1.42076255348269*m.x6*m.x6) + m.x70 == 0.28)

m.c7 = Constraint(expr=-(m.x7*m.x4*(-0.824884423842853*cos(m.x36 - m.x39) - 6.35284123437183*sin(m.x36 - m.x39)) + m.x7*
                       m.x5*(-0.746980513063235*cos(m.x37 - m.x39) - 3.99601522253739*sin(m.x37 - m.x39)) + 
                       8.01827911901728*m.x7*m.x7 + m.x7*m.x8*(-6.44641418211119*cos(m.x40 - m.x39) - 56.4061240934729*
                       sin(m.x40 - m.x39)) - 20*m.x7*m.x15*sin(m.x47 - m.x39)) + m.x71 == 0)

m.c8 = Constraint(expr=-(m.x8*m.x7*(-6.44641418211119*cos(m.x39 - m.x40) - 56.4061240934729*sin(m.x39 - m.x40)) + 
                       7.92491432585426*m.x8*m.x8 + m.x8*m.x9*(-1.47850014374307*cos(m.x41 - m.x40) - 12.7315290155653*
                       sin(m.x41 - m.x40))) + m.x72 == 0)

m.c9 = Constraint(expr=-(m.x9*m.x4*(-0.323309932984507*cos(m.x36 - m.x41) - 3.06668980551481*sin(m.x36 - m.x41)) + m.x9*
                       m.x8*(-1.47850014374307*cos(m.x40 - m.x41) - 12.7315290155653*sin(m.x40 - m.x41)) + 
                       3.67227520253507*m.x9*m.x9 + m.x9*m.x10*(-1.53864841883629*cos(m.x42 - m.x41) - 12.6331133336033*
                       sin(m.x42 - m.x41)) + m.x9*m.x11*(-0.331816706971196*cos(m.x43 - m.x41) - 2.02240182793204*sin(
                       m.x43 - m.x41)) - 6.66666666666667*m.x9*m.x14*sin(m.x46 - m.x41)) + m.x73 == 0)

m.c10 = Constraint(expr=-(m.x10*m.x9*(-1.53864841883629*cos(m.x41 - m.x42) - 12.6331133336033*sin(m.x41 - m.x42)) + 
                        1.87592107119826*m.x10*m.x10 + m.x10*m.x11*(-0.337272652361963*cos(m.x43 - m.x42) - 
                        2.74800558799463*sin(m.x43 - m.x42)) - 6.66666666666667*m.x10*m.x12*sin(m.x44 - m.x42)) + m.x74
                         == 0)

m.c11 = Constraint(expr=-(m.x11*m.x9*(-0.331816706971196*cos(m.x41 - m.x43) - 2.02240182793204*sin(m.x41 - m.x43)) + 
                        m.x11*m.x10*(-0.337272652361963*cos(m.x42 - m.x43) - 2.74800558799463*sin(m.x42 - m.x43)) + 
                        0.669089359333159*m.x11*m.x11 - 6.66666666666667*m.x11*m.x13*sin(m.x45 - m.x43)) + m.x75 == 0.3)

m.c12 = Constraint(expr=6.66666666666667*m.x12*m.x10*sin(m.x42 - m.x44) + m.x76 == 0.56)

m.c13 = Constraint(expr=6.66666666666667*m.x13*m.x11*sin(m.x43 - m.x45) + m.x77 == 0)

m.c14 = Constraint(expr=6.66666666666667*m.x14*m.x9*sin(m.x41 - m.x46) + m.x78 == 0.44)

m.c15 = Constraint(expr=20*m.x15*m.x7*sin(m.x39 - m.x47) + m.x79 == 2.4)

m.c16 = Constraint(expr=10*m.x16*m.x4*sin(m.x36 - m.x48) + m.x80 == 0)

m.c17 = Constraint(expr=-(25.4742969121846*m.x1*m.x1 + m.x1*m.x2*(2.26704183302539*sin(m.x34 - m.x33) - 18.5374266808153
                        *cos(m.x34 - m.x33)) + m.x1*m.x5*(13.6293753124381*sin(m.x37 - m.x33) - 7.07407023136926*cos(
                        m.x37 - m.x33))) + m.x81 + m.x129 - m.x145 == 0)

m.c18 = Constraint(expr=-(m.x2*m.x1*(2.26704183302539*sin(m.x33 - m.x34) - 18.5374266808153*cos(m.x33 - m.x34)) + 
                        25.7248427582125*m.x2*m.x2 + m.x2*m.x3*(1.26726581392059*sin(m.x35 - m.x34) - 7.28131607739717*
                        cos(m.x35 - m.x34))) + m.x82 + m.x130 - m.x146 == 0)

m.c19 = Constraint(expr=-(m.x3*m.x2*(1.26726581392059*sin(m.x34 - m.x35) - 7.28131607739717*cos(m.x34 - m.x35)) + 
                        8.82609777433267*m.x3*m.x3 + m.x3*m.x4*(0.27754515791681*sin(m.x36 - m.x35) - 1.6615816969355*
                        cos(m.x36 - m.x35))) + m.x83 + m.x131 - m.x147 == 0)

m.c20 = Constraint(expr=-(m.x4*m.x3*(0.27754515791681*sin(m.x35 - m.x36) - 1.6615816969355*cos(m.x35 - m.x36)) + 
                        27.0030745903615*m.x4*m.x4 + m.x4*m.x6*(0.864296115364742*sin(m.x38 - m.x36) - 6.06886185353939*
                        cos(m.x38 - m.x36)) + m.x4*m.x7*(0.824884423842853*sin(m.x39 - m.x36) - 6.35284123437183*cos(
                        m.x39 - m.x36)) + m.x4*m.x9*(0.323309932984507*sin(m.x41 - m.x36) - 3.06668980551481*cos(m.x41
                         - m.x36)) - 10*m.x4*m.x16*cos(m.x48 - m.x36)) + m.x84 + m.x132 - m.x148 == 0)

m.c21 = Constraint(expr=-(m.x5*m.x1*(13.6293753124381*sin(m.x33 - m.x37) - 7.07407023136926*cos(m.x33 - m.x37)) + 
                        14.428443500312*m.x5*m.x5 + m.x5*m.x6*(0.556466438117951*sin(m.x38 - m.x37) - 3.59715804640533*
                        cos(m.x38 - m.x37)) + m.x5*m.x7*(0.746980513063235*sin(m.x39 - m.x37) - 3.99601522253739*cos(
                        m.x39 - m.x37))) + m.x85 + m.x133 - m.x149 == 0)

m.c22 = Constraint(expr=-(m.x6*m.x4*(0.864296115364742*sin(m.x36 - m.x38) - 6.06886185353939*cos(m.x36 - m.x38)) + m.x6*
                        m.x5*(0.556466438117951*sin(m.x37 - m.x38) - 3.59715804640533*cos(m.x37 - m.x38)) + 
                        9.58501989994471*m.x6*m.x6) + m.x86 + m.x134 - m.x150 == 0.08)

m.c23 = Constraint(expr=-(m.x7*m.x4*(0.824884423842853*sin(m.x36 - m.x39) - 6.35284123437183*cos(m.x36 - m.x39)) + m.x7*
                        m.x5*(0.746980513063235*sin(m.x37 - m.x39) - 3.99601522253739*cos(m.x37 - m.x39)) + 
                        86.6293805503822*m.x7*m.x7 + m.x7*m.x8*(6.44641418211119*sin(m.x40 - m.x39) - 56.4061240934729*
                        cos(m.x40 - m.x39)) - 20*m.x7*m.x15*cos(m.x47 - m.x39)) + m.x87 + m.x135 - m.x151 == -0.5)

m.c24 = Constraint(expr=-(m.x8*m.x7*(6.44641418211119*sin(m.x39 - m.x40) - 56.4061240934729*cos(m.x39 - m.x40)) + 
                        69.1318531090383*m.x8*m.x8 + m.x8*m.x9*(1.47850014374307*sin(m.x41 - m.x40) - 12.7315290155653*
                        cos(m.x41 - m.x40))) + m.x88 + m.x136 - m.x152 == 0)

m.c25 = Constraint(expr=-(m.x9*m.x4*(0.323309932984507*sin(m.x36 - m.x41) - 3.06668980551481*cos(m.x36 - m.x41)) + m.x9*
                        m.x8*(1.47850014374307*sin(m.x40 - m.x41) - 12.7315290155653*cos(m.x40 - m.x41)) + 
                        37.0715006492821*m.x9*m.x9 + m.x9*m.x10*(1.53864841883629*sin(m.x42 - m.x41) - 12.6331133336033*
                        cos(m.x42 - m.x41)) + m.x9*m.x11*(0.331816706971196*sin(m.x43 - m.x41) - 2.02240182793204*cos(
                        m.x43 - m.x41)) - 6.66666666666667*m.x9*m.x14*cos(m.x46 - m.x41)) + m.x89 + m.x137 - m.x153
                         == -0.2)

m.c26 = Constraint(expr=-(m.x10*m.x9*(1.53864841883629*sin(m.x41 - m.x42) - 12.6331133336033*cos(m.x41 - m.x42)) + 
                        22.0194855882646*m.x10*m.x10 + m.x10*m.x11*(0.337272652361963*sin(m.x43 - m.x42) - 
                        2.74800558799463*cos(m.x43 - m.x42)) - 6.66666666666667*m.x10*m.x12*cos(m.x44 - m.x42)) + m.x90
                         + m.x138 - m.x154 == -0.2)

m.c27 = Constraint(expr=-(m.x11*m.x9*(0.331816706971196*sin(m.x41 - m.x43) - 2.02240182793204*cos(m.x41 - m.x43)) + 
                        m.x11*m.x10*(0.337272652361963*sin(m.x42 - m.x43) - 2.74800558799463*cos(m.x42 - m.x43)) + 
                        11.3946740825933*m.x11*m.x11 - 6.66666666666667*m.x11*m.x13*cos(m.x45 - m.x43)) + m.x91 + m.x139
                         - m.x155 == 0.1)

m.c28 = Constraint(expr=-(6.66666666666667*m.x12*m.x12 - 6.66666666666667*m.x12*m.x10*cos(m.x42 - m.x44)) + m.x92
                         + m.x140 - m.x156 == -0.08)

m.c29 = Constraint(expr=-(6.66666666666667*m.x13*m.x13 - 6.66666666666667*m.x13*m.x11*cos(m.x43 - m.x45)) + m.x93
                         + m.x141 - m.x157 == -0.2)

m.c30 = Constraint(expr=-(6.66666666666667*m.x14*m.x14 - 6.66666666666667*m.x14*m.x9*cos(m.x41 - m.x46)) + m.x94
                         + m.x142 - m.x158 == -0.1)

m.c31 = Constraint(expr=-(20*m.x15*m.x15 - 20*m.x15*m.x7*cos(m.x39 - m.x47)) + m.x95 + m.x143 - m.x159 == 0)

m.c32 = Constraint(expr=-(10*m.x16*m.x16 - 10*m.x16*m.x4*cos(m.x36 - m.x48)) + m.x96 + m.x144 - m.x160 == 0)

m.c33 = Constraint(expr=   m.x33 == 0)

m.c34 = Constraint(expr=15.8964171454635*m.x17*m.x17 + m.x17*m.x18*(-2.26704183302539*cos(m.x50 - m.x49) - 
                        18.5374266808153*sin(m.x50 - m.x49)) + m.x17*m.x21*(-13.6293753124381*cos(m.x53 - m.x49) - 
                        7.07407023136926*sin(m.x53 - m.x49)) - m.x97 == 0)

m.c35 = Constraint(expr=m.x18*m.x17*(-2.26704183302539*cos(m.x49 - m.x50) - 18.5374266808153*sin(m.x49 - m.x50)) + 
                        3.53430764694598*m.x18*m.x18 + m.x18*m.x19*(-1.26726581392059*cos(m.x51 - m.x50) - 
                        7.28131607739717*sin(m.x51 - m.x50)) - m.x98 == 0)

m.c36 = Constraint(expr=m.x19*m.x18*(-1.26726581392059*cos(m.x50 - m.x51) - 7.28131607739717*sin(m.x50 - m.x51)) + 
                        1.5448109718374*m.x19*m.x19 + m.x19*m.x20*(-0.27754515791681*cos(m.x52 - m.x51) - 
                        1.6615816969355*sin(m.x52 - m.x51)) - m.x99 == 0)

m.c37 = Constraint(expr=m.x20*m.x19*(-0.27754515791681*cos(m.x51 - m.x52) - 1.6615816969355*sin(m.x51 - m.x52)) + 
                        2.29003563010891*m.x20*m.x20 + m.x20*m.x22*(-0.864296115364742*cos(m.x54 - m.x52) - 
                        6.06886185353939*sin(m.x54 - m.x52)) + m.x20*m.x23*(-0.824884423842853*cos(m.x55 - m.x52) - 
                        6.35284123437183*sin(m.x55 - m.x52)) + m.x20*m.x25*(-0.323309932984507*cos(m.x57 - m.x52) - 
                        3.06668980551481*sin(m.x57 - m.x52)) - 10*m.x20*m.x32*sin(m.x64 - m.x52) - m.x100 == 0)

m.c38 = Constraint(expr=m.x21*m.x17*(-13.6293753124381*cos(m.x49 - m.x53) - 7.07407023136926*sin(m.x49 - m.x53)) + 
                        14.9328222636193*m.x21*m.x21 + m.x21*m.x22*(-0.556466438117951*cos(m.x54 - m.x53) - 
                        3.59715804640533*sin(m.x54 - m.x53)) + m.x21*m.x23*(-0.746980513063235*cos(m.x55 - m.x53) - 
                        3.99601522253739*sin(m.x55 - m.x53)) - m.x101 == 0)

m.c39 = Constraint(expr=m.x22*m.x20*(-0.864296115364742*cos(m.x52 - m.x54) - 6.06886185353939*sin(m.x52 - m.x54)) + 
                        m.x22*m.x21*(-0.556466438117951*cos(m.x53 - m.x54) - 3.59715804640533*sin(m.x53 - m.x54)) + 
                        1.42076255348269*m.x22*m.x22 - m.x102 == 0)

m.c40 = Constraint(expr=m.x23*m.x20*(-0.824884423842853*cos(m.x52 - m.x55) - 6.35284123437183*sin(m.x52 - m.x55)) + 
                        m.x23*m.x21*(-0.746980513063235*cos(m.x53 - m.x55) - 3.99601522253739*sin(m.x53 - m.x55)) + 
                        8.01827911901728*m.x23*m.x23 + m.x23*m.x24*(-6.44641418211119*cos(m.x56 - m.x55) - 
                        56.4061240934729*sin(m.x56 - m.x55)) - 20*m.x23*m.x31*sin(m.x63 - m.x55) - m.x103 == 0)

m.c41 = Constraint(expr=m.x24*m.x23*(-6.44641418211119*cos(m.x55 - m.x56) - 56.4061240934729*sin(m.x55 - m.x56)) + 
                        7.92491432585426*m.x24*m.x24 + m.x24*m.x25*(-1.47850014374307*cos(m.x57 - m.x56) - 
                        12.7315290155653*sin(m.x57 - m.x56)) - m.x104 == 0)

m.c42 = Constraint(expr=m.x25*m.x20*(-0.323309932984507*cos(m.x52 - m.x57) - 3.06668980551481*sin(m.x52 - m.x57)) + 
                        m.x25*m.x24*(-1.47850014374307*cos(m.x56 - m.x57) - 12.7315290155653*sin(m.x56 - m.x57)) + 
                        3.67227520253507*m.x25*m.x25 + m.x25*m.x26*(-1.53864841883629*cos(m.x58 - m.x57) - 
                        12.6331133336033*sin(m.x58 - m.x57)) + m.x25*m.x27*(-0.331816706971196*cos(m.x59 - m.x57) - 
                        2.02240182793204*sin(m.x59 - m.x57)) - 6.66666666666667*m.x25*m.x30*sin(m.x62 - m.x57) - m.x105
                         == 0)

m.c43 = Constraint(expr=m.x26*m.x25*(-1.53864841883629*cos(m.x57 - m.x58) - 12.6331133336033*sin(m.x57 - m.x58)) + 
                        1.87592107119826*m.x26*m.x26 + m.x26*m.x27*(-0.337272652361963*cos(m.x59 - m.x58) - 
                        2.74800558799463*sin(m.x59 - m.x58)) - 6.66666666666667*m.x26*m.x28*sin(m.x60 - m.x58) - m.x106
                         == 0)

m.c44 = Constraint(expr=m.x27*m.x25*(-0.331816706971196*cos(m.x57 - m.x59) - 2.02240182793204*sin(m.x57 - m.x59)) + 
                        m.x27*m.x26*(-0.337272652361963*cos(m.x58 - m.x59) - 2.74800558799463*sin(m.x58 - m.x59)) + 
                        0.669089359333159*m.x27*m.x27 - 6.66666666666667*m.x27*m.x29*sin(m.x61 - m.x59) - m.x107 == 0)

m.c45 = Constraint(expr=-6.66666666666667*m.x28*m.x26*sin(m.x58 - m.x60) - m.x108 == 0)

m.c46 = Constraint(expr=-6.66666666666667*m.x29*m.x27*sin(m.x59 - m.x61) - m.x109 == 0)

m.c47 = Constraint(expr=-6.66666666666667*m.x30*m.x25*sin(m.x57 - m.x62) - m.x110 == 0)

m.c48 = Constraint(expr=-20*m.x31*m.x23*sin(m.x55 - m.x63) - m.x111 == 0)

m.c49 = Constraint(expr=-10*m.x32*m.x20*sin(m.x52 - m.x64) - m.x112 == 0)

m.c50 = Constraint(expr=25.4742969121846*m.x17*m.x17 + m.x17*m.x18*(2.26704183302539*sin(m.x50 - m.x49) - 
                        18.5374266808153*cos(m.x50 - m.x49)) + m.x17*m.x21*(13.6293753124381*sin(m.x53 - m.x49) - 
                        7.07407023136926*cos(m.x53 - m.x49)) - m.x113 - m.x129 + m.x145 == 0)

m.c51 = Constraint(expr=m.x18*m.x17*(2.26704183302539*sin(m.x49 - m.x50) - 18.5374266808153*cos(m.x49 - m.x50)) + 
                        25.7248427582125*m.x18*m.x18 + m.x18*m.x19*(1.26726581392059*sin(m.x51 - m.x50) - 
                        7.28131607739717*cos(m.x51 - m.x50)) - m.x114 - m.x130 + m.x146 == 0)

m.c52 = Constraint(expr=m.x19*m.x18*(1.26726581392059*sin(m.x50 - m.x51) - 7.28131607739717*cos(m.x50 - m.x51)) + 
                        8.82609777433267*m.x19*m.x19 + m.x19*m.x20*(0.27754515791681*sin(m.x52 - m.x51) - 
                        1.6615816969355*cos(m.x52 - m.x51)) - m.x115 - m.x131 + m.x147 == 0)

m.c53 = Constraint(expr=m.x20*m.x19*(0.27754515791681*sin(m.x51 - m.x52) - 1.6615816969355*cos(m.x51 - m.x52)) + 
                        27.0030745903615*m.x20*m.x20 + m.x20*m.x22*(0.864296115364742*sin(m.x54 - m.x52) - 
                        6.06886185353939*cos(m.x54 - m.x52)) + m.x20*m.x23*(0.824884423842853*sin(m.x55 - m.x52) - 
                        6.35284123437183*cos(m.x55 - m.x52)) + m.x20*m.x25*(0.323309932984507*sin(m.x57 - m.x52) - 
                        3.06668980551481*cos(m.x57 - m.x52)) - 10*m.x20*m.x32*cos(m.x64 - m.x52) - m.x116 - m.x132
                         + m.x148 == 0)

m.c54 = Constraint(expr=m.x21*m.x17*(13.6293753124381*sin(m.x49 - m.x53) - 7.07407023136926*cos(m.x49 - m.x53)) + 
                        14.428443500312*m.x21*m.x21 + m.x21*m.x22*(0.556466438117951*sin(m.x54 - m.x53) - 
                        3.59715804640533*cos(m.x54 - m.x53)) + m.x21*m.x23*(0.746980513063235*sin(m.x55 - m.x53) - 
                        3.99601522253739*cos(m.x55 - m.x53)) - m.x117 - m.x133 + m.x149 == 0)

m.c55 = Constraint(expr=m.x22*m.x20*(0.864296115364742*sin(m.x52 - m.x54) - 6.06886185353939*cos(m.x52 - m.x54)) + m.x22
                        *m.x21*(0.556466438117951*sin(m.x53 - m.x54) - 3.59715804640533*cos(m.x53 - m.x54)) + 
                        9.58501989994471*m.x22*m.x22 - m.x118 - m.x134 + m.x150 == 0)

m.c56 = Constraint(expr=m.x23*m.x20*(0.824884423842853*sin(m.x52 - m.x55) - 6.35284123437183*cos(m.x52 - m.x55)) + m.x23
                        *m.x21*(0.746980513063235*sin(m.x53 - m.x55) - 3.99601522253739*cos(m.x53 - m.x55)) + 
                        86.6293805503822*m.x23*m.x23 + m.x23*m.x24*(6.44641418211119*sin(m.x56 - m.x55) - 
                        56.4061240934729*cos(m.x56 - m.x55)) - 20*m.x23*m.x31*cos(m.x63 - m.x55) - m.x119 - m.x135
                         + m.x151 == 0.5)

m.c57 = Constraint(expr=m.x24*m.x23*(6.44641418211119*sin(m.x55 - m.x56) - 56.4061240934729*cos(m.x55 - m.x56)) + 
                        69.1318531090383*m.x24*m.x24 + m.x24*m.x25*(1.47850014374307*sin(m.x57 - m.x56) - 
                        12.7315290155653*cos(m.x57 - m.x56)) - m.x120 - m.x136 + m.x152 == 0)

m.c58 = Constraint(expr=m.x25*m.x20*(0.323309932984507*sin(m.x52 - m.x57) - 3.06668980551481*cos(m.x52 - m.x57)) + m.x25
                        *m.x24*(1.47850014374307*sin(m.x56 - m.x57) - 12.7315290155653*cos(m.x56 - m.x57)) + 
                        37.0715006492821*m.x25*m.x25 + m.x25*m.x26*(1.53864841883629*sin(m.x58 - m.x57) - 
                        12.6331133336033*cos(m.x58 - m.x57)) + m.x25*m.x27*(0.331816706971196*sin(m.x59 - m.x57) - 
                        2.02240182793204*cos(m.x59 - m.x57)) - 6.66666666666667*m.x25*m.x30*cos(m.x62 - m.x57) - m.x121
                         - m.x137 + m.x153 == 0.2)

m.c59 = Constraint(expr=m.x26*m.x25*(1.53864841883629*sin(m.x57 - m.x58) - 12.6331133336033*cos(m.x57 - m.x58)) + 
                        22.0194855882646*m.x26*m.x26 + m.x26*m.x27*(0.337272652361963*sin(m.x59 - m.x58) - 
                        2.74800558799463*cos(m.x59 - m.x58)) - 6.66666666666667*m.x26*m.x28*cos(m.x60 - m.x58) - m.x122
                         - m.x138 + m.x154 == 0.2)

m.c60 = Constraint(expr=m.x27*m.x25*(0.331816706971196*sin(m.x57 - m.x59) - 2.02240182793204*cos(m.x57 - m.x59)) + m.x27
                        *m.x26*(0.337272652361963*sin(m.x58 - m.x59) - 2.74800558799463*cos(m.x58 - m.x59)) + 
                        11.3946740825933*m.x27*m.x27 - 6.66666666666667*m.x27*m.x29*cos(m.x61 - m.x59) - m.x123 - m.x139
                         + m.x155 == 0)

m.c61 = Constraint(expr=6.66666666666667*m.x28*m.x28 - 6.66666666666667*m.x28*m.x26*cos(m.x58 - m.x60) - m.x124 - m.x140
                         + m.x156 == 0.2)

m.c62 = Constraint(expr=6.66666666666667*m.x29*m.x29 - 6.66666666666667*m.x29*m.x27*cos(m.x59 - m.x61) - m.x125 - m.x141
                         + m.x157 == 0.2)

m.c63 = Constraint(expr=6.66666666666667*m.x30*m.x30 - 6.66666666666667*m.x30*m.x25*cos(m.x57 - m.x62) - m.x126 - m.x142
                         + m.x158 == 0.2)

m.c64 = Constraint(expr=20*m.x31*m.x31 - 20*m.x31*m.x23*cos(m.x55 - m.x63) - m.x127 - m.x143 + m.x159 == 0.5)

m.c65 = Constraint(expr=10*m.x32*m.x32 - 10*m.x32*m.x20*cos(m.x52 - m.x64) - m.x128 - m.x144 + m.x160 == 0)

m.c66 = Constraint(expr= - m.x97 >= -4)

m.c67 = Constraint(expr= - m.x99 >= -0.8)

m.c68 = Constraint(expr= - m.x101 >= -1.2)

m.c69 = Constraint(expr= - m.x104 >= -0.24)

m.c70 = Constraint(expr= - m.x112 >= -0.5)

m.c71 = Constraint(expr=   m.x97 >= 0)

m.c72 = Constraint(expr=   m.x99 >= 0)

m.c73 = Constraint(expr=   m.x101 >= 0)

m.c74 = Constraint(expr=   m.x104 >= 0)

m.c75 = Constraint(expr=   m.x112 >= 0)

m.c76 = Constraint(expr= - m.x113 >= -0.6)

m.c77 = Constraint(expr= - m.x115 >= -0.2)

m.c78 = Constraint(expr= - m.x117 >= -0.6)

m.c79 = Constraint(expr= - m.x120 >= -0.13)

m.c80 = Constraint(expr= - m.x128 >= -0.24)

m.c81 = Constraint(expr=   m.x113 >= -0.2)

m.c82 = Constraint(expr=   m.x115 >= -0.08)

m.c83 = Constraint(expr=   m.x117 >= -0.3)

m.c84 = Constraint(expr=   m.x120 >= -0.1)

m.c85 = Constraint(expr=   m.x128 >= -0.04)

m.c86 = Constraint(expr=   m.x98 <= 0)

m.c87 = Constraint(expr=   m.x100 <= 0)

m.c88 = Constraint(expr=   m.x102 <= -0.329411764705882)

m.c89 = Constraint(expr=   m.x103 <= 0)

m.c90 = Constraint(expr=   m.x105 <= 0)

m.c91 = Constraint(expr=   m.x106 <= 0)

m.c92 = Constraint(expr=   m.x107 <= -0.352941176470588)

m.c93 = Constraint(expr=   m.x108 <= -0.658823529411765)

m.c94 = Constraint(expr=   m.x109 <= 0)

m.c95 = Constraint(expr=   m.x110 <= -0.517647058823529)

m.c96 = Constraint(expr=   m.x111 <= -2.82352941176471)

m.c97 = Constraint(expr=   m.x114 <= 0)

m.c98 = Constraint(expr=   m.x116 <= 0)

m.c99 = Constraint(expr=   m.x118 <= -0.0941176470588235)

m.c100 = Constraint(expr=   m.x119 <= 0)

m.c101 = Constraint(expr=   m.x121 <= 0)

m.c102 = Constraint(expr=   m.x122 <= 0)

m.c103 = Constraint(expr=   m.x123 <= -0.117647058823529)

m.c104 = Constraint(expr=   m.x124 <= -0.141176470588235)

m.c105 = Constraint(expr=   m.x125 <= 0)

m.c106 = Constraint(expr=   m.x126 <= -0.117647058823529)

m.c107 = Constraint(expr=   m.x127 <= -0.588235294117648)

m.c109 = Constraint(expr=   m.x130 - 0.4*m.b162 <= 0)

m.c110 = Constraint(expr=   m.x132 - 0.4*m.b163 <= 0)

m.c111 = Constraint(expr=   m.x134 - 0.4*m.b164 <= 0)

m.c112 = Constraint(expr=   m.x135 - 0.4*m.b165 <= 0)

m.c113 = Constraint(expr=   m.x137 - 0.4*m.b166 <= 0)

m.c114 = Constraint(expr=   m.x138 - 0.4*m.b167 <= 0)

m.c115 = Constraint(expr=   m.x139 - 0.4*m.b168 <= 0)

m.c116 = Constraint(expr=   m.x140 - 0.4*m.b169 <= 0)

m.c117 = Constraint(expr=   m.x141 - 0.4*m.b170 <= 0)

m.c118 = Constraint(expr=   m.x142 - 0.4*m.b171 <= 0)

m.c119 = Constraint(expr=   m.x143 - 0.4*m.b172 <= 0)

m.c120 = Constraint(expr=   m.x146 - 0.4*m.b173 <= 0)

m.c121 = Constraint(expr=   m.x148 - 0.4*m.b174 <= 0)

m.c122 = Constraint(expr=   m.x150 - 0.4*m.b175 <= 0)

m.c123 = Constraint(expr=   m.x151 - 0.4*m.b176 <= 0)

m.c124 = Constraint(expr=   m.x153 - 0.4*m.b177 <= 0)

m.c125 = Constraint(expr=   m.x154 - 0.4*m.b178 <= 0)

m.c126 = Constraint(expr=   m.x155 - 0.4*m.b179 <= 0)

m.c127 = Constraint(expr=   m.x156 - 0.4*m.b180 <= 0)

m.c128 = Constraint(expr=   m.x157 - 0.4*m.b181 <= 0)

m.c129 = Constraint(expr=   m.x158 - 0.4*m.b182 <= 0)

m.c130 = Constraint(expr=   m.x159 - 0.4*m.b183 <= 0)
