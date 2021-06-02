#  NLP written by GAMS Convert at 04/21/18 13:52:24
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        151      151        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        202      202        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        601      151      450        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,6.2831854),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,6.2831854),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,6.2831854),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,6.2831854),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,6.2831854),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,6.2831854),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,6.2831854),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,6.2831854),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,6.2831854),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,6.2831854),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,6.2831854),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,6.2831854),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,6.2831854),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,6.2831854),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,6.2831854),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,6.2831854),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,6.2831854),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,6.2831854),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,6.2831854),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,6.2831854),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,6.2831854),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,6.2831854),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,6.2831854),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,6.2831854),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,6.2831854),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,6.2831854),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,6.2831854),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,6.2831854),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,6.2831854),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,6.2831854),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,6.2831854),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,6.2831854),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,6.2831854),initialize=0)
m.x34 = Var(within=Reals,bounds=(0,6.2831854),initialize=0)
m.x35 = Var(within=Reals,bounds=(0,6.2831854),initialize=0)
m.x36 = Var(within=Reals,bounds=(0,6.2831854),initialize=0)
m.x37 = Var(within=Reals,bounds=(0,6.2831854),initialize=0)
m.x38 = Var(within=Reals,bounds=(0,6.2831854),initialize=0)
m.x39 = Var(within=Reals,bounds=(0,6.2831854),initialize=0)
m.x40 = Var(within=Reals,bounds=(0,6.2831854),initialize=0)
m.x41 = Var(within=Reals,bounds=(0,6.2831854),initialize=0)
m.x42 = Var(within=Reals,bounds=(0,6.2831854),initialize=0)
m.x43 = Var(within=Reals,bounds=(0,6.2831854),initialize=0)
m.x44 = Var(within=Reals,bounds=(0,6.2831854),initialize=0)
m.x45 = Var(within=Reals,bounds=(0,6.2831854),initialize=0)
m.x46 = Var(within=Reals,bounds=(0,6.2831854),initialize=0)
m.x47 = Var(within=Reals,bounds=(0,6.2831854),initialize=0)
m.x48 = Var(within=Reals,bounds=(0,6.2831854),initialize=0)
m.x49 = Var(within=Reals,bounds=(0,6.2831854),initialize=0)
m.x50 = Var(within=Reals,bounds=(0,6.2831854),initialize=0)
m.x51 = Var(within=Reals,bounds=(0.08,0.417),initialize=0.08)
m.x52 = Var(within=Reals,bounds=(0.08,0.417),initialize=0.08)
m.x53 = Var(within=Reals,bounds=(0.08,0.417),initialize=0.08)
m.x54 = Var(within=Reals,bounds=(0.08,0.417),initialize=0.08)
m.x55 = Var(within=Reals,bounds=(0.08,0.417),initialize=0.08)
m.x56 = Var(within=Reals,bounds=(0.08,0.417),initialize=0.08)
m.x57 = Var(within=Reals,bounds=(0.08,0.417),initialize=0.08)
m.x58 = Var(within=Reals,bounds=(0.08,0.417),initialize=0.08)
m.x59 = Var(within=Reals,bounds=(0.08,0.417),initialize=0.08)
m.x60 = Var(within=Reals,bounds=(0.08,0.417),initialize=0.08)
m.x61 = Var(within=Reals,bounds=(0.08,0.417),initialize=0.08)
m.x62 = Var(within=Reals,bounds=(0.08,0.417),initialize=0.08)
m.x63 = Var(within=Reals,bounds=(0.08,0.417),initialize=0.08)
m.x64 = Var(within=Reals,bounds=(0.08,0.417),initialize=0.08)
m.x65 = Var(within=Reals,bounds=(0.08,0.417),initialize=0.08)
m.x66 = Var(within=Reals,bounds=(0.08,0.417),initialize=0.08)
m.x67 = Var(within=Reals,bounds=(0.08,0.417),initialize=0.08)
m.x68 = Var(within=Reals,bounds=(0.08,0.417),initialize=0.08)
m.x69 = Var(within=Reals,bounds=(0.08,0.417),initialize=0.08)
m.x70 = Var(within=Reals,bounds=(0.08,0.417),initialize=0.08)
m.x71 = Var(within=Reals,bounds=(0.08,0.417),initialize=0.08)
m.x72 = Var(within=Reals,bounds=(0.08,0.417),initialize=0.08)
m.x73 = Var(within=Reals,bounds=(0.08,0.417),initialize=0.08)
m.x74 = Var(within=Reals,bounds=(0.08,0.417),initialize=0.08)
m.x75 = Var(within=Reals,bounds=(0.08,0.417),initialize=0.08)
m.x76 = Var(within=Reals,bounds=(0.08,0.417),initialize=0.08)
m.x77 = Var(within=Reals,bounds=(0.08,0.417),initialize=0.08)
m.x78 = Var(within=Reals,bounds=(0.08,0.417),initialize=0.08)
m.x79 = Var(within=Reals,bounds=(0.08,0.417),initialize=0.08)
m.x80 = Var(within=Reals,bounds=(0.08,0.417),initialize=0.08)
m.x81 = Var(within=Reals,bounds=(0.08,0.417),initialize=0.08)
m.x82 = Var(within=Reals,bounds=(0.08,0.417),initialize=0.08)
m.x83 = Var(within=Reals,bounds=(0.08,0.417),initialize=0.08)
m.x84 = Var(within=Reals,bounds=(0.08,0.417),initialize=0.08)
m.x85 = Var(within=Reals,bounds=(0.08,0.417),initialize=0.08)
m.x86 = Var(within=Reals,bounds=(0.08,0.417),initialize=0.08)
m.x87 = Var(within=Reals,bounds=(0.08,0.417),initialize=0.08)
m.x88 = Var(within=Reals,bounds=(0.08,0.417),initialize=0.08)
m.x89 = Var(within=Reals,bounds=(0.08,0.417),initialize=0.08)
m.x90 = Var(within=Reals,bounds=(0.08,0.417),initialize=0.08)
m.x91 = Var(within=Reals,bounds=(0.08,0.417),initialize=0.08)
m.x92 = Var(within=Reals,bounds=(0.08,0.417),initialize=0.08)
m.x93 = Var(within=Reals,bounds=(0.08,0.417),initialize=0.08)
m.x94 = Var(within=Reals,bounds=(0.08,0.417),initialize=0.08)
m.x95 = Var(within=Reals,bounds=(0.08,0.417),initialize=0.08)
m.x96 = Var(within=Reals,bounds=(0.08,0.417),initialize=0.08)
m.x97 = Var(within=Reals,bounds=(0.08,0.417),initialize=0.08)
m.x98 = Var(within=Reals,bounds=(0.08,0.417),initialize=0.08)
m.x99 = Var(within=Reals,bounds=(0.08,0.417),initialize=0.08)
m.x100 = Var(within=Reals,bounds=(0.08,0.417),initialize=0.08)
m.x101 = Var(within=Reals,bounds=(0,6.2831854),initialize=0)
m.x102 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x103 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x104 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x105 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x106 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x107 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x108 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x109 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x110 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x111 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x112 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x113 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x114 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x115 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x116 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x117 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x118 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x119 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x120 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x121 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x122 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x123 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x124 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x125 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x126 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x127 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x128 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x129 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x130 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x131 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x132 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x133 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x134 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x135 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x136 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x137 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x138 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x139 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x140 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x141 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x142 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x143 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x144 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x145 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x146 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x147 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x148 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x149 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x150 = Var(within=Reals,bounds=(None,None),initialize=1.5)
m.x151 = Var(within=Reals,bounds=(None,None),initialize=1.09905)
m.x152 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x153 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x154 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x155 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x156 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x157 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x158 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x159 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x160 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x161 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x162 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x163 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x164 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x165 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x166 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x167 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x168 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x169 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x170 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x171 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x172 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x173 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x174 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x175 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x176 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x177 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x178 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x179 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x180 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x181 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x182 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x183 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x184 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x185 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x186 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x187 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x188 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x189 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x190 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x191 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x192 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x193 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x194 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x195 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x196 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x197 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x198 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x199 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x200 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x201 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=   m.x152, sense=minimize)

m.c1 = Constraint(expr=0.00437*cos(m.x1)/((0.0162079 + 0.486237*m.x51*m.x51)*m.x102*m.x102) - m.x201 == 0)

m.c2 = Constraint(expr=(-1/m.x102) - cos(m.x1)/((0.0162079 + 0.486237*m.x51*m.x51)*m.x102*m.x102*m.x102) == 0)

m.c3 = Constraint(expr=0.00437*m.x51/((0.01 + 0.3*m.x51*m.x51)*m.x102*m.x102) - 0.00437*cos(m.x1)/((0.0162079 + 0.486237
                       *m.x51*m.x51)*m.x102*m.x102*m.x102*m.x102) - 0.1*m.x1 + 0.1*m.x101 == 0)

m.c4 = Constraint(expr=0.00437*cos(m.x2)/((0.0162079 + 0.486237*m.x52*m.x52)*m.x103*m.x103) - m.x200 + m.x201 == 0)

m.c5 = Constraint(expr=(-1/m.x103) - cos(m.x2)/((0.0162079 + 0.486237*m.x52*m.x52)*m.x103*m.x103*m.x103) == 0)

m.c6 = Constraint(expr=0.00437*m.x52/((0.01 + 0.3*m.x52*m.x52)*m.x103*m.x103) - 0.00437*cos(m.x2)/((0.0162079 + 0.486237
                       *m.x52*m.x52)*m.x103*m.x103*m.x103*m.x103) - 0.1*m.x2 + 0.1*m.x1 == 0)

m.c7 = Constraint(expr=0.00437*cos(m.x3)/((0.0162079 + 0.486237*m.x53*m.x53)*m.x104*m.x104) - m.x199 + m.x200 == 0)

m.c8 = Constraint(expr=(-1/m.x104) - cos(m.x3)/((0.0162079 + 0.486237*m.x53*m.x53)*m.x104*m.x104*m.x104) == 0)

m.c9 = Constraint(expr=0.00437*m.x53/((0.01 + 0.3*m.x53*m.x53)*m.x104*m.x104) - 0.00437*cos(m.x3)/((0.0162079 + 0.486237
                       *m.x53*m.x53)*m.x104*m.x104*m.x104*m.x104) - 0.1*m.x3 + 0.1*m.x2 == 0)

m.c10 = Constraint(expr=0.00437*cos(m.x4)/((0.0162079 + 0.486237*m.x54*m.x54)*m.x105*m.x105) - m.x198 + m.x199 == 0)

m.c11 = Constraint(expr=(-1/m.x105) - cos(m.x4)/((0.0162079 + 0.486237*m.x54*m.x54)*m.x105*m.x105*m.x105) == 0)

m.c12 = Constraint(expr=0.00437*m.x54/((0.01 + 0.3*m.x54*m.x54)*m.x105*m.x105) - 0.00437*cos(m.x4)/((0.0162079 + 
                        0.486237*m.x54*m.x54)*m.x105*m.x105*m.x105*m.x105) - 0.1*m.x4 + 0.1*m.x3 == 0)

m.c13 = Constraint(expr=0.00437*cos(m.x5)/((0.0162079 + 0.486237*m.x55*m.x55)*m.x106*m.x106) - m.x197 + m.x198 == 0)

m.c14 = Constraint(expr=(-1/m.x106) - cos(m.x5)/((0.0162079 + 0.486237*m.x55*m.x55)*m.x106*m.x106*m.x106) == 0)

m.c15 = Constraint(expr=0.00437*m.x55/((0.01 + 0.3*m.x55*m.x55)*m.x106*m.x106) - 0.00437*cos(m.x5)/((0.0162079 + 
                        0.486237*m.x55*m.x55)*m.x106*m.x106*m.x106*m.x106) - 0.1*m.x5 + 0.1*m.x4 == 0)

m.c16 = Constraint(expr=0.00437*cos(m.x6)/((0.0162079 + 0.486237*m.x56*m.x56)*m.x107*m.x107) - m.x196 + m.x197 == 0)

m.c17 = Constraint(expr=(-1/m.x107) - cos(m.x6)/((0.0162079 + 0.486237*m.x56*m.x56)*m.x107*m.x107*m.x107) == 0)

m.c18 = Constraint(expr=0.00437*m.x56/((0.01 + 0.3*m.x56*m.x56)*m.x107*m.x107) - 0.00437*cos(m.x6)/((0.0162079 + 
                        0.486237*m.x56*m.x56)*m.x107*m.x107*m.x107*m.x107) - 0.1*m.x6 + 0.1*m.x5 == 0)

m.c19 = Constraint(expr=0.00437*cos(m.x7)/((0.0162079 + 0.486237*m.x57*m.x57)*m.x108*m.x108) - m.x195 + m.x196 == 0)

m.c20 = Constraint(expr=(-1/m.x108) - cos(m.x7)/((0.0162079 + 0.486237*m.x57*m.x57)*m.x108*m.x108*m.x108) == 0)

m.c21 = Constraint(expr=0.00437*m.x57/((0.01 + 0.3*m.x57*m.x57)*m.x108*m.x108) - 0.00437*cos(m.x7)/((0.0162079 + 
                        0.486237*m.x57*m.x57)*m.x108*m.x108*m.x108*m.x108) - 0.1*m.x7 + 0.1*m.x6 == 0)

m.c22 = Constraint(expr=0.00437*cos(m.x8)/((0.0162079 + 0.486237*m.x58*m.x58)*m.x109*m.x109) - m.x194 + m.x195 == 0)

m.c23 = Constraint(expr=(-1/m.x109) - cos(m.x8)/((0.0162079 + 0.486237*m.x58*m.x58)*m.x109*m.x109*m.x109) == 0)

m.c24 = Constraint(expr=0.00437*m.x58/((0.01 + 0.3*m.x58*m.x58)*m.x109*m.x109) - 0.00437*cos(m.x8)/((0.0162079 + 
                        0.486237*m.x58*m.x58)*m.x109*m.x109*m.x109*m.x109) - 0.1*m.x8 + 0.1*m.x7 == 0)

m.c25 = Constraint(expr=0.00437*cos(m.x9)/((0.0162079 + 0.486237*m.x59*m.x59)*m.x110*m.x110) - m.x193 + m.x194 == 0)

m.c26 = Constraint(expr=(-1/m.x110) - cos(m.x9)/((0.0162079 + 0.486237*m.x59*m.x59)*m.x110*m.x110*m.x110) == 0)

m.c27 = Constraint(expr=0.00437*m.x59/((0.01 + 0.3*m.x59*m.x59)*m.x110*m.x110) - 0.00437*cos(m.x9)/((0.0162079 + 
                        0.486237*m.x59*m.x59)*m.x110*m.x110*m.x110*m.x110) - 0.1*m.x9 + 0.1*m.x8 == 0)

m.c28 = Constraint(expr=0.00437*cos(m.x10)/((0.0162079 + 0.486237*m.x60*m.x60)*m.x111*m.x111) - m.x192 + m.x193 == 0)

m.c29 = Constraint(expr=(-1/m.x111) - cos(m.x10)/((0.0162079 + 0.486237*m.x60*m.x60)*m.x111*m.x111*m.x111) == 0)

m.c30 = Constraint(expr=0.00437*m.x60/((0.01 + 0.3*m.x60*m.x60)*m.x111*m.x111) - 0.00437*cos(m.x10)/((0.0162079 + 
                        0.486237*m.x60*m.x60)*m.x111*m.x111*m.x111*m.x111) - 0.1*m.x10 + 0.1*m.x9 == 0)

m.c31 = Constraint(expr=0.00437*cos(m.x11)/((0.0162079 + 0.486237*m.x61*m.x61)*m.x112*m.x112) - m.x191 + m.x192 == 0)

m.c32 = Constraint(expr=(-1/m.x112) - cos(m.x11)/((0.0162079 + 0.486237*m.x61*m.x61)*m.x112*m.x112*m.x112) == 0)

m.c33 = Constraint(expr=0.00437*m.x61/((0.01 + 0.3*m.x61*m.x61)*m.x112*m.x112) - 0.00437*cos(m.x11)/((0.0162079 + 
                        0.486237*m.x61*m.x61)*m.x112*m.x112*m.x112*m.x112) - 0.1*m.x11 + 0.1*m.x10 == 0)

m.c34 = Constraint(expr=0.00437*cos(m.x12)/((0.0162079 + 0.486237*m.x62*m.x62)*m.x113*m.x113) - m.x190 + m.x191 == 0)

m.c35 = Constraint(expr=(-1/m.x113) - cos(m.x12)/((0.0162079 + 0.486237*m.x62*m.x62)*m.x113*m.x113*m.x113) == 0)

m.c36 = Constraint(expr=0.00437*m.x62/((0.01 + 0.3*m.x62*m.x62)*m.x113*m.x113) - 0.00437*cos(m.x12)/((0.0162079 + 
                        0.486237*m.x62*m.x62)*m.x113*m.x113*m.x113*m.x113) - 0.1*m.x12 + 0.1*m.x11 == 0)

m.c37 = Constraint(expr=0.00437*cos(m.x13)/((0.0162079 + 0.486237*m.x63*m.x63)*m.x114*m.x114) - m.x189 + m.x190 == 0)

m.c38 = Constraint(expr=(-1/m.x114) - cos(m.x13)/((0.0162079 + 0.486237*m.x63*m.x63)*m.x114*m.x114*m.x114) == 0)

m.c39 = Constraint(expr=0.00437*m.x63/((0.01 + 0.3*m.x63*m.x63)*m.x114*m.x114) - 0.00437*cos(m.x13)/((0.0162079 + 
                        0.486237*m.x63*m.x63)*m.x114*m.x114*m.x114*m.x114) - 0.1*m.x13 + 0.1*m.x12 == 0)

m.c40 = Constraint(expr=0.00437*cos(m.x14)/((0.0162079 + 0.486237*m.x64*m.x64)*m.x115*m.x115) - m.x188 + m.x189 == 0)

m.c41 = Constraint(expr=(-1/m.x115) - cos(m.x14)/((0.0162079 + 0.486237*m.x64*m.x64)*m.x115*m.x115*m.x115) == 0)

m.c42 = Constraint(expr=0.00437*m.x64/((0.01 + 0.3*m.x64*m.x64)*m.x115*m.x115) - 0.00437*cos(m.x14)/((0.0162079 + 
                        0.486237*m.x64*m.x64)*m.x115*m.x115*m.x115*m.x115) - 0.1*m.x14 + 0.1*m.x13 == 0)

m.c43 = Constraint(expr=0.00437*cos(m.x15)/((0.0162079 + 0.486237*m.x65*m.x65)*m.x116*m.x116) - m.x187 + m.x188 == 0)

m.c44 = Constraint(expr=(-1/m.x116) - cos(m.x15)/((0.0162079 + 0.486237*m.x65*m.x65)*m.x116*m.x116*m.x116) == 0)

m.c45 = Constraint(expr=0.00437*m.x65/((0.01 + 0.3*m.x65*m.x65)*m.x116*m.x116) - 0.00437*cos(m.x15)/((0.0162079 + 
                        0.486237*m.x65*m.x65)*m.x116*m.x116*m.x116*m.x116) - 0.1*m.x15 + 0.1*m.x14 == 0)

m.c46 = Constraint(expr=0.00437*cos(m.x16)/((0.0162079 + 0.486237*m.x66*m.x66)*m.x117*m.x117) - m.x186 + m.x187 == 0)

m.c47 = Constraint(expr=(-1/m.x117) - cos(m.x16)/((0.0162079 + 0.486237*m.x66*m.x66)*m.x117*m.x117*m.x117) == 0)

m.c48 = Constraint(expr=0.00437*m.x66/((0.01 + 0.3*m.x66*m.x66)*m.x117*m.x117) - 0.00437*cos(m.x16)/((0.0162079 + 
                        0.486237*m.x66*m.x66)*m.x117*m.x117*m.x117*m.x117) - 0.1*m.x16 + 0.1*m.x15 == 0)

m.c49 = Constraint(expr=0.00437*cos(m.x17)/((0.0162079 + 0.486237*m.x67*m.x67)*m.x118*m.x118) - m.x185 + m.x186 == 0)

m.c50 = Constraint(expr=(-1/m.x118) - cos(m.x17)/((0.0162079 + 0.486237*m.x67*m.x67)*m.x118*m.x118*m.x118) == 0)

m.c51 = Constraint(expr=0.00437*m.x67/((0.01 + 0.3*m.x67*m.x67)*m.x118*m.x118) - 0.00437*cos(m.x17)/((0.0162079 + 
                        0.486237*m.x67*m.x67)*m.x118*m.x118*m.x118*m.x118) - 0.1*m.x17 + 0.1*m.x16 == 0)

m.c52 = Constraint(expr=0.00437*cos(m.x18)/((0.0162079 + 0.486237*m.x68*m.x68)*m.x119*m.x119) - m.x184 + m.x185 == 0)

m.c53 = Constraint(expr=(-1/m.x119) - cos(m.x18)/((0.0162079 + 0.486237*m.x68*m.x68)*m.x119*m.x119*m.x119) == 0)

m.c54 = Constraint(expr=0.00437*m.x68/((0.01 + 0.3*m.x68*m.x68)*m.x119*m.x119) - 0.00437*cos(m.x18)/((0.0162079 + 
                        0.486237*m.x68*m.x68)*m.x119*m.x119*m.x119*m.x119) - 0.1*m.x18 + 0.1*m.x17 == 0)

m.c55 = Constraint(expr=0.00437*cos(m.x19)/((0.0162079 + 0.486237*m.x69*m.x69)*m.x120*m.x120) - m.x183 + m.x184 == 0)

m.c56 = Constraint(expr=(-1/m.x120) - cos(m.x19)/((0.0162079 + 0.486237*m.x69*m.x69)*m.x120*m.x120*m.x120) == 0)

m.c57 = Constraint(expr=0.00437*m.x69/((0.01 + 0.3*m.x69*m.x69)*m.x120*m.x120) - 0.00437*cos(m.x19)/((0.0162079 + 
                        0.486237*m.x69*m.x69)*m.x120*m.x120*m.x120*m.x120) - 0.1*m.x19 + 0.1*m.x18 == 0)

m.c58 = Constraint(expr=0.00437*cos(m.x20)/((0.0162079 + 0.486237*m.x70*m.x70)*m.x121*m.x121) - m.x182 + m.x183 == 0)

m.c59 = Constraint(expr=(-1/m.x121) - cos(m.x20)/((0.0162079 + 0.486237*m.x70*m.x70)*m.x121*m.x121*m.x121) == 0)

m.c60 = Constraint(expr=0.00437*m.x70/((0.01 + 0.3*m.x70*m.x70)*m.x121*m.x121) - 0.00437*cos(m.x20)/((0.0162079 + 
                        0.486237*m.x70*m.x70)*m.x121*m.x121*m.x121*m.x121) - 0.1*m.x20 + 0.1*m.x19 == 0)

m.c61 = Constraint(expr=0.00437*cos(m.x21)/((0.0162079 + 0.486237*m.x71*m.x71)*m.x122*m.x122) - m.x181 + m.x182 == 0)

m.c62 = Constraint(expr=(-1/m.x122) - cos(m.x21)/((0.0162079 + 0.486237*m.x71*m.x71)*m.x122*m.x122*m.x122) == 0)

m.c63 = Constraint(expr=0.00437*m.x71/((0.01 + 0.3*m.x71*m.x71)*m.x122*m.x122) - 0.00437*cos(m.x21)/((0.0162079 + 
                        0.486237*m.x71*m.x71)*m.x122*m.x122*m.x122*m.x122) - 0.1*m.x21 + 0.1*m.x20 == 0)

m.c64 = Constraint(expr=0.00437*cos(m.x22)/((0.0162079 + 0.486237*m.x72*m.x72)*m.x123*m.x123) - m.x180 + m.x181 == 0)

m.c65 = Constraint(expr=(-1/m.x123) - cos(m.x22)/((0.0162079 + 0.486237*m.x72*m.x72)*m.x123*m.x123*m.x123) == 0)

m.c66 = Constraint(expr=0.00437*m.x72/((0.01 + 0.3*m.x72*m.x72)*m.x123*m.x123) - 0.00437*cos(m.x22)/((0.0162079 + 
                        0.486237*m.x72*m.x72)*m.x123*m.x123*m.x123*m.x123) - 0.1*m.x22 + 0.1*m.x21 == 0)

m.c67 = Constraint(expr=0.00437*cos(m.x23)/((0.0162079 + 0.486237*m.x73*m.x73)*m.x124*m.x124) - m.x179 + m.x180 == 0)

m.c68 = Constraint(expr=(-1/m.x124) - cos(m.x23)/((0.0162079 + 0.486237*m.x73*m.x73)*m.x124*m.x124*m.x124) == 0)

m.c69 = Constraint(expr=0.00437*m.x73/((0.01 + 0.3*m.x73*m.x73)*m.x124*m.x124) - 0.00437*cos(m.x23)/((0.0162079 + 
                        0.486237*m.x73*m.x73)*m.x124*m.x124*m.x124*m.x124) - 0.1*m.x23 + 0.1*m.x22 == 0)

m.c70 = Constraint(expr=0.00437*cos(m.x24)/((0.0162079 + 0.486237*m.x74*m.x74)*m.x125*m.x125) - m.x178 + m.x179 == 0)

m.c71 = Constraint(expr=(-1/m.x125) - cos(m.x24)/((0.0162079 + 0.486237*m.x74*m.x74)*m.x125*m.x125*m.x125) == 0)

m.c72 = Constraint(expr=0.00437*m.x74/((0.01 + 0.3*m.x74*m.x74)*m.x125*m.x125) - 0.00437*cos(m.x24)/((0.0162079 + 
                        0.486237*m.x74*m.x74)*m.x125*m.x125*m.x125*m.x125) - 0.1*m.x24 + 0.1*m.x23 == 0)

m.c73 = Constraint(expr=0.00437*cos(m.x25)/((0.0162079 + 0.486237*m.x75*m.x75)*m.x126*m.x126) - m.x177 + m.x178 == 0)

m.c74 = Constraint(expr=(-1/m.x126) - cos(m.x25)/((0.0162079 + 0.486237*m.x75*m.x75)*m.x126*m.x126*m.x126) == 0)

m.c75 = Constraint(expr=0.00437*m.x75/((0.01 + 0.3*m.x75*m.x75)*m.x126*m.x126) - 0.00437*cos(m.x25)/((0.0162079 + 
                        0.486237*m.x75*m.x75)*m.x126*m.x126*m.x126*m.x126) - 0.1*m.x25 + 0.1*m.x24 == 0)

m.c76 = Constraint(expr=0.00437*cos(m.x26)/((0.0162079 + 0.486237*m.x76*m.x76)*m.x127*m.x127) - m.x176 + m.x177 == 0)

m.c77 = Constraint(expr=(-1/m.x127) - cos(m.x26)/((0.0162079 + 0.486237*m.x76*m.x76)*m.x127*m.x127*m.x127) == 0)

m.c78 = Constraint(expr=0.00437*m.x76/((0.01 + 0.3*m.x76*m.x76)*m.x127*m.x127) - 0.00437*cos(m.x26)/((0.0162079 + 
                        0.486237*m.x76*m.x76)*m.x127*m.x127*m.x127*m.x127) - 0.1*m.x26 + 0.1*m.x25 == 0)

m.c79 = Constraint(expr=0.00437*cos(m.x27)/((0.0162079 + 0.486237*m.x77*m.x77)*m.x128*m.x128) - m.x175 + m.x176 == 0)

m.c80 = Constraint(expr=(-1/m.x128) - cos(m.x27)/((0.0162079 + 0.486237*m.x77*m.x77)*m.x128*m.x128*m.x128) == 0)

m.c81 = Constraint(expr=0.00437*m.x77/((0.01 + 0.3*m.x77*m.x77)*m.x128*m.x128) - 0.00437*cos(m.x27)/((0.0162079 + 
                        0.486237*m.x77*m.x77)*m.x128*m.x128*m.x128*m.x128) - 0.1*m.x27 + 0.1*m.x26 == 0)

m.c82 = Constraint(expr=0.00437*cos(m.x28)/((0.0162079 + 0.486237*m.x78*m.x78)*m.x129*m.x129) - m.x174 + m.x175 == 0)

m.c83 = Constraint(expr=(-1/m.x129) - cos(m.x28)/((0.0162079 + 0.486237*m.x78*m.x78)*m.x129*m.x129*m.x129) == 0)

m.c84 = Constraint(expr=0.00437*m.x78/((0.01 + 0.3*m.x78*m.x78)*m.x129*m.x129) - 0.00437*cos(m.x28)/((0.0162079 + 
                        0.486237*m.x78*m.x78)*m.x129*m.x129*m.x129*m.x129) - 0.1*m.x28 + 0.1*m.x27 == 0)

m.c85 = Constraint(expr=0.00437*cos(m.x29)/((0.0162079 + 0.486237*m.x79*m.x79)*m.x130*m.x130) - m.x173 + m.x174 == 0)

m.c86 = Constraint(expr=(-1/m.x130) - cos(m.x29)/((0.0162079 + 0.486237*m.x79*m.x79)*m.x130*m.x130*m.x130) == 0)

m.c87 = Constraint(expr=0.00437*m.x79/((0.01 + 0.3*m.x79*m.x79)*m.x130*m.x130) - 0.00437*cos(m.x29)/((0.0162079 + 
                        0.486237*m.x79*m.x79)*m.x130*m.x130*m.x130*m.x130) - 0.1*m.x29 + 0.1*m.x28 == 0)

m.c88 = Constraint(expr=0.00437*cos(m.x30)/((0.0162079 + 0.486237*m.x80*m.x80)*m.x131*m.x131) - m.x172 + m.x173 == 0)

m.c89 = Constraint(expr=(-1/m.x131) - cos(m.x30)/((0.0162079 + 0.486237*m.x80*m.x80)*m.x131*m.x131*m.x131) == 0)

m.c90 = Constraint(expr=0.00437*m.x80/((0.01 + 0.3*m.x80*m.x80)*m.x131*m.x131) - 0.00437*cos(m.x30)/((0.0162079 + 
                        0.486237*m.x80*m.x80)*m.x131*m.x131*m.x131*m.x131) - 0.1*m.x30 + 0.1*m.x29 == 0)

m.c91 = Constraint(expr=0.00437*cos(m.x31)/((0.0162079 + 0.486237*m.x81*m.x81)*m.x132*m.x132) - m.x171 + m.x172 == 0)

m.c92 = Constraint(expr=(-1/m.x132) - cos(m.x31)/((0.0162079 + 0.486237*m.x81*m.x81)*m.x132*m.x132*m.x132) == 0)

m.c93 = Constraint(expr=0.00437*m.x81/((0.01 + 0.3*m.x81*m.x81)*m.x132*m.x132) - 0.00437*cos(m.x31)/((0.0162079 + 
                        0.486237*m.x81*m.x81)*m.x132*m.x132*m.x132*m.x132) - 0.1*m.x31 + 0.1*m.x30 == 0)

m.c94 = Constraint(expr=0.00437*cos(m.x32)/((0.0162079 + 0.486237*m.x82*m.x82)*m.x133*m.x133) - m.x170 + m.x171 == 0)

m.c95 = Constraint(expr=(-1/m.x133) - cos(m.x32)/((0.0162079 + 0.486237*m.x82*m.x82)*m.x133*m.x133*m.x133) == 0)

m.c96 = Constraint(expr=0.00437*m.x82/((0.01 + 0.3*m.x82*m.x82)*m.x133*m.x133) - 0.00437*cos(m.x32)/((0.0162079 + 
                        0.486237*m.x82*m.x82)*m.x133*m.x133*m.x133*m.x133) - 0.1*m.x32 + 0.1*m.x31 == 0)

m.c97 = Constraint(expr=0.00437*cos(m.x33)/((0.0162079 + 0.486237*m.x83*m.x83)*m.x134*m.x134) - m.x169 + m.x170 == 0)

m.c98 = Constraint(expr=(-1/m.x134) - cos(m.x33)/((0.0162079 + 0.486237*m.x83*m.x83)*m.x134*m.x134*m.x134) == 0)

m.c99 = Constraint(expr=0.00437*m.x83/((0.01 + 0.3*m.x83*m.x83)*m.x134*m.x134) - 0.00437*cos(m.x33)/((0.0162079 + 
                        0.486237*m.x83*m.x83)*m.x134*m.x134*m.x134*m.x134) - 0.1*m.x33 + 0.1*m.x32 == 0)

m.c100 = Constraint(expr=0.00437*cos(m.x34)/((0.0162079 + 0.486237*m.x84*m.x84)*m.x135*m.x135) - m.x168 + m.x169 == 0)

m.c101 = Constraint(expr=(-1/m.x135) - cos(m.x34)/((0.0162079 + 0.486237*m.x84*m.x84)*m.x135*m.x135*m.x135) == 0)

m.c102 = Constraint(expr=0.00437*m.x84/((0.01 + 0.3*m.x84*m.x84)*m.x135*m.x135) - 0.00437*cos(m.x34)/((0.0162079 + 
                         0.486237*m.x84*m.x84)*m.x135*m.x135*m.x135*m.x135) - 0.1*m.x34 + 0.1*m.x33 == 0)

m.c103 = Constraint(expr=0.00437*cos(m.x35)/((0.0162079 + 0.486237*m.x85*m.x85)*m.x136*m.x136) - m.x167 + m.x168 == 0)

m.c104 = Constraint(expr=(-1/m.x136) - cos(m.x35)/((0.0162079 + 0.486237*m.x85*m.x85)*m.x136*m.x136*m.x136) == 0)

m.c105 = Constraint(expr=0.00437*m.x85/((0.01 + 0.3*m.x85*m.x85)*m.x136*m.x136) - 0.00437*cos(m.x35)/((0.0162079 + 
                         0.486237*m.x85*m.x85)*m.x136*m.x136*m.x136*m.x136) - 0.1*m.x35 + 0.1*m.x34 == 0)

m.c106 = Constraint(expr=0.00437*cos(m.x36)/((0.0162079 + 0.486237*m.x86*m.x86)*m.x137*m.x137) - m.x166 + m.x167 == 0)

m.c107 = Constraint(expr=(-1/m.x137) - cos(m.x36)/((0.0162079 + 0.486237*m.x86*m.x86)*m.x137*m.x137*m.x137) == 0)

m.c108 = Constraint(expr=0.00437*m.x86/((0.01 + 0.3*m.x86*m.x86)*m.x137*m.x137) - 0.00437*cos(m.x36)/((0.0162079 + 
                         0.486237*m.x86*m.x86)*m.x137*m.x137*m.x137*m.x137) - 0.1*m.x36 + 0.1*m.x35 == 0)

m.c109 = Constraint(expr=0.00437*cos(m.x37)/((0.0162079 + 0.486237*m.x87*m.x87)*m.x138*m.x138) - m.x165 + m.x166 == 0)

m.c110 = Constraint(expr=(-1/m.x138) - cos(m.x37)/((0.0162079 + 0.486237*m.x87*m.x87)*m.x138*m.x138*m.x138) == 0)

m.c111 = Constraint(expr=0.00437*m.x87/((0.01 + 0.3*m.x87*m.x87)*m.x138*m.x138) - 0.00437*cos(m.x37)/((0.0162079 + 
                         0.486237*m.x87*m.x87)*m.x138*m.x138*m.x138*m.x138) - 0.1*m.x37 + 0.1*m.x36 == 0)

m.c112 = Constraint(expr=0.00437*cos(m.x38)/((0.0162079 + 0.486237*m.x88*m.x88)*m.x139*m.x139) - m.x164 + m.x165 == 0)

m.c113 = Constraint(expr=(-1/m.x139) - cos(m.x38)/((0.0162079 + 0.486237*m.x88*m.x88)*m.x139*m.x139*m.x139) == 0)

m.c114 = Constraint(expr=0.00437*m.x88/((0.01 + 0.3*m.x88*m.x88)*m.x139*m.x139) - 0.00437*cos(m.x38)/((0.0162079 + 
                         0.486237*m.x88*m.x88)*m.x139*m.x139*m.x139*m.x139) - 0.1*m.x38 + 0.1*m.x37 == 0)

m.c115 = Constraint(expr=0.00437*cos(m.x39)/((0.0162079 + 0.486237*m.x89*m.x89)*m.x140*m.x140) - m.x163 + m.x164 == 0)

m.c116 = Constraint(expr=(-1/m.x140) - cos(m.x39)/((0.0162079 + 0.486237*m.x89*m.x89)*m.x140*m.x140*m.x140) == 0)

m.c117 = Constraint(expr=0.00437*m.x89/((0.01 + 0.3*m.x89*m.x89)*m.x140*m.x140) - 0.00437*cos(m.x39)/((0.0162079 + 
                         0.486237*m.x89*m.x89)*m.x140*m.x140*m.x140*m.x140) - 0.1*m.x39 + 0.1*m.x38 == 0)

m.c118 = Constraint(expr=0.00437*cos(m.x40)/((0.0162079 + 0.486237*m.x90*m.x90)*m.x141*m.x141) - m.x162 + m.x163 == 0)

m.c119 = Constraint(expr=(-1/m.x141) - cos(m.x40)/((0.0162079 + 0.486237*m.x90*m.x90)*m.x141*m.x141*m.x141) == 0)

m.c120 = Constraint(expr=0.00437*m.x90/((0.01 + 0.3*m.x90*m.x90)*m.x141*m.x141) - 0.00437*cos(m.x40)/((0.0162079 + 
                         0.486237*m.x90*m.x90)*m.x141*m.x141*m.x141*m.x141) - 0.1*m.x40 + 0.1*m.x39 == 0)

m.c121 = Constraint(expr=0.00437*cos(m.x41)/((0.0162079 + 0.486237*m.x91*m.x91)*m.x142*m.x142) - m.x161 + m.x162 == 0)

m.c122 = Constraint(expr=(-1/m.x142) - cos(m.x41)/((0.0162079 + 0.486237*m.x91*m.x91)*m.x142*m.x142*m.x142) == 0)

m.c123 = Constraint(expr=0.00437*m.x91/((0.01 + 0.3*m.x91*m.x91)*m.x142*m.x142) - 0.00437*cos(m.x41)/((0.0162079 + 
                         0.486237*m.x91*m.x91)*m.x142*m.x142*m.x142*m.x142) - 0.1*m.x41 + 0.1*m.x40 == 0)

m.c124 = Constraint(expr=0.00437*cos(m.x42)/((0.0162079 + 0.486237*m.x92*m.x92)*m.x143*m.x143) - m.x160 + m.x161 == 0)

m.c125 = Constraint(expr=(-1/m.x143) - cos(m.x42)/((0.0162079 + 0.486237*m.x92*m.x92)*m.x143*m.x143*m.x143) == 0)

m.c126 = Constraint(expr=0.00437*m.x92/((0.01 + 0.3*m.x92*m.x92)*m.x143*m.x143) - 0.00437*cos(m.x42)/((0.0162079 + 
                         0.486237*m.x92*m.x92)*m.x143*m.x143*m.x143*m.x143) - 0.1*m.x42 + 0.1*m.x41 == 0)

m.c127 = Constraint(expr=0.00437*cos(m.x43)/((0.0162079 + 0.486237*m.x93*m.x93)*m.x144*m.x144) - m.x159 + m.x160 == 0)

m.c128 = Constraint(expr=(-1/m.x144) - cos(m.x43)/((0.0162079 + 0.486237*m.x93*m.x93)*m.x144*m.x144*m.x144) == 0)

m.c129 = Constraint(expr=0.00437*m.x93/((0.01 + 0.3*m.x93*m.x93)*m.x144*m.x144) - 0.00437*cos(m.x43)/((0.0162079 + 
                         0.486237*m.x93*m.x93)*m.x144*m.x144*m.x144*m.x144) - 0.1*m.x43 + 0.1*m.x42 == 0)

m.c130 = Constraint(expr=0.00437*cos(m.x44)/((0.0162079 + 0.486237*m.x94*m.x94)*m.x145*m.x145) - m.x158 + m.x159 == 0)

m.c131 = Constraint(expr=(-1/m.x145) - cos(m.x44)/((0.0162079 + 0.486237*m.x94*m.x94)*m.x145*m.x145*m.x145) == 0)

m.c132 = Constraint(expr=0.00437*m.x94/((0.01 + 0.3*m.x94*m.x94)*m.x145*m.x145) - 0.00437*cos(m.x44)/((0.0162079 + 
                         0.486237*m.x94*m.x94)*m.x145*m.x145*m.x145*m.x145) - 0.1*m.x44 + 0.1*m.x43 == 0)

m.c133 = Constraint(expr=0.00437*cos(m.x45)/((0.0162079 + 0.486237*m.x95*m.x95)*m.x146*m.x146) - m.x157 + m.x158 == 0)

m.c134 = Constraint(expr=(-1/m.x146) - cos(m.x45)/((0.0162079 + 0.486237*m.x95*m.x95)*m.x146*m.x146*m.x146) == 0)

m.c135 = Constraint(expr=0.00437*m.x95/((0.01 + 0.3*m.x95*m.x95)*m.x146*m.x146) - 0.00437*cos(m.x45)/((0.0162079 + 
                         0.486237*m.x95*m.x95)*m.x146*m.x146*m.x146*m.x146) - 0.1*m.x45 + 0.1*m.x44 == 0)

m.c136 = Constraint(expr=0.00437*cos(m.x46)/((0.0162079 + 0.486237*m.x96*m.x96)*m.x147*m.x147) - m.x156 + m.x157 == 0)

m.c137 = Constraint(expr=(-1/m.x147) - cos(m.x46)/((0.0162079 + 0.486237*m.x96*m.x96)*m.x147*m.x147*m.x147) == 0)

m.c138 = Constraint(expr=0.00437*m.x96/((0.01 + 0.3*m.x96*m.x96)*m.x147*m.x147) - 0.00437*cos(m.x46)/((0.0162079 + 
                         0.486237*m.x96*m.x96)*m.x147*m.x147*m.x147*m.x147) - 0.1*m.x46 + 0.1*m.x45 == 0)

m.c139 = Constraint(expr=0.00437*cos(m.x47)/((0.0162079 + 0.486237*m.x97*m.x97)*m.x148*m.x148) - m.x155 + m.x156 == 0)

m.c140 = Constraint(expr=(-1/m.x148) - cos(m.x47)/((0.0162079 + 0.486237*m.x97*m.x97)*m.x148*m.x148*m.x148) == 0)

m.c141 = Constraint(expr=0.00437*m.x97/((0.01 + 0.3*m.x97*m.x97)*m.x148*m.x148) - 0.00437*cos(m.x47)/((0.0162079 + 
                         0.486237*m.x97*m.x97)*m.x148*m.x148*m.x148*m.x148) - 0.1*m.x47 + 0.1*m.x46 == 0)

m.c142 = Constraint(expr=0.00437*cos(m.x48)/((0.0162079 + 0.486237*m.x98*m.x98)*m.x149*m.x149) - m.x154 + m.x155 == 0)

m.c143 = Constraint(expr=(-1/m.x149) - cos(m.x48)/((0.0162079 + 0.486237*m.x98*m.x98)*m.x149*m.x149*m.x149) == 0)

m.c144 = Constraint(expr=0.00437*m.x98/((0.01 + 0.3*m.x98*m.x98)*m.x149*m.x149) - 0.00437*cos(m.x48)/((0.0162079 + 
                         0.486237*m.x98*m.x98)*m.x149*m.x149*m.x149*m.x149) - 0.1*m.x48 + 0.1*m.x47 == 0)

m.c145 = Constraint(expr=0.00437*cos(m.x49)/((0.0162079 + 0.486237*m.x99*m.x99)*m.x150*m.x150) - m.x153 + m.x154 == 0)

m.c146 = Constraint(expr=(-1/m.x150) - cos(m.x49)/((0.0162079 + 0.486237*m.x99*m.x99)*m.x150*m.x150*m.x150) == 0)

m.c147 = Constraint(expr=0.00437*m.x99/((0.01 + 0.3*m.x99*m.x99)*m.x150*m.x150) - 0.00437*cos(m.x49)/((0.0162079 + 
                         0.486237*m.x99*m.x99)*m.x150*m.x150*m.x150*m.x150) - 0.1*m.x49 + 0.1*m.x48 == 0)

m.c148 = Constraint(expr=0.00437*cos(m.x50)/((0.0162079 + 0.486237*m.x100*m.x100)*m.x151*m.x151) - m.x152 + m.x153 == 0)

m.c149 = Constraint(expr=(-1/m.x151) - cos(m.x50)/((0.0162079 + 0.486237*m.x100*m.x100)*m.x151*m.x151*m.x151) == 0)

m.c150 = Constraint(expr=0.00437*m.x100/((0.01 + 0.3*m.x100*m.x100)*m.x151*m.x151) - 0.00437*cos(m.x50)/((0.0162079 + 
                         0.486237*m.x100*m.x100)*m.x151*m.x151*m.x151*m.x151) - 0.1*m.x50 + 0.1*m.x49 == 0)
