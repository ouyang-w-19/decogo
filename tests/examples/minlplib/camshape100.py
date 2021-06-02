#  NLP written by GAMS Convert at 04/21/18 13:51:13
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        201      100        0      101        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        200      200        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        697      398      299        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(1,1.00015482411709),initialize=1.00015482411709)
m.x2 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x3 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x4 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x5 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x6 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x7 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x8 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x9 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x10 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x11 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x12 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x13 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x14 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x15 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x16 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x17 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x18 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x19 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x20 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x21 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x22 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x23 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x24 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x25 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x26 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x27 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x28 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x29 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x30 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x31 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x32 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x33 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x34 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x35 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x36 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x37 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x38 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x39 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x40 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x41 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x42 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x43 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x44 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x45 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x46 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x47 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x48 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x49 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x50 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x51 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x52 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x53 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x54 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x55 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x56 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x57 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x58 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x59 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x60 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x61 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x62 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x63 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x64 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x65 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x66 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x67 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x68 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x69 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x70 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x71 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x72 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x73 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x74 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x75 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x76 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x77 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x78 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x79 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x80 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x81 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x82 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x83 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x84 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x85 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x86 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x87 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x88 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x89 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x90 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x91 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x92 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x93 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x94 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x95 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x96 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x97 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x98 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x99 = Var(within=Reals,bounds=(1,2),initialize=1.5)
m.x100 = Var(within=Reals,bounds=(1.98133707334501,2),initialize=1.98133707334501)
m.x101 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x102 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x103 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x104 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x105 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x106 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x107 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x108 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x109 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x110 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x111 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x112 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x113 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x114 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x115 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x116 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x117 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x118 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x119 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x120 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x121 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x122 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x123 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x124 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x125 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x126 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x127 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x128 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x129 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x130 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x131 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x132 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x133 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x134 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x135 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x136 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x137 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x138 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x139 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x140 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x141 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x142 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x143 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x144 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x145 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x146 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x147 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x148 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x149 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x150 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x151 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x152 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x153 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x154 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x155 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x156 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x157 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x158 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x159 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x160 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x161 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x162 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x163 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x164 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x165 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x166 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x167 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x168 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x169 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x170 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x171 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x172 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x173 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x174 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x175 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x176 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x177 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x178 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x179 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x180 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x181 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x182 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x183 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x184 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x185 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x186 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x187 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x188 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x189 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x190 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x191 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x192 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x193 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x194 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x195 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x196 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x197 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x198 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)
m.x199 = Var(within=Reals,bounds=(-0.0186629266549889,0.0186629266549889),initialize=0)

m.obj = Objective(expr= - 0.0314159265358979*m.x1 - 0.0314159265358979*m.x2 - 0.0314159265358979*m.x3
                        - 0.0314159265358979*m.x4 - 0.0314159265358979*m.x5 - 0.0314159265358979*m.x6
                        - 0.0314159265358979*m.x7 - 0.0314159265358979*m.x8 - 0.0314159265358979*m.x9
                        - 0.0314159265358979*m.x10 - 0.0314159265358979*m.x11 - 0.0314159265358979*m.x12
                        - 0.0314159265358979*m.x13 - 0.0314159265358979*m.x14 - 0.0314159265358979*m.x15
                        - 0.0314159265358979*m.x16 - 0.0314159265358979*m.x17 - 0.0314159265358979*m.x18
                        - 0.0314159265358979*m.x19 - 0.0314159265358979*m.x20 - 0.0314159265358979*m.x21
                        - 0.0314159265358979*m.x22 - 0.0314159265358979*m.x23 - 0.0314159265358979*m.x24
                        - 0.0314159265358979*m.x25 - 0.0314159265358979*m.x26 - 0.0314159265358979*m.x27
                        - 0.0314159265358979*m.x28 - 0.0314159265358979*m.x29 - 0.0314159265358979*m.x30
                        - 0.0314159265358979*m.x31 - 0.0314159265358979*m.x32 - 0.0314159265358979*m.x33
                        - 0.0314159265358979*m.x34 - 0.0314159265358979*m.x35 - 0.0314159265358979*m.x36
                        - 0.0314159265358979*m.x37 - 0.0314159265358979*m.x38 - 0.0314159265358979*m.x39
                        - 0.0314159265358979*m.x40 - 0.0314159265358979*m.x41 - 0.0314159265358979*m.x42
                        - 0.0314159265358979*m.x43 - 0.0314159265358979*m.x44 - 0.0314159265358979*m.x45
                        - 0.0314159265358979*m.x46 - 0.0314159265358979*m.x47 - 0.0314159265358979*m.x48
                        - 0.0314159265358979*m.x49 - 0.0314159265358979*m.x50 - 0.0314159265358979*m.x51
                        - 0.0314159265358979*m.x52 - 0.0314159265358979*m.x53 - 0.0314159265358979*m.x54
                        - 0.0314159265358979*m.x55 - 0.0314159265358979*m.x56 - 0.0314159265358979*m.x57
                        - 0.0314159265358979*m.x58 - 0.0314159265358979*m.x59 - 0.0314159265358979*m.x60
                        - 0.0314159265358979*m.x61 - 0.0314159265358979*m.x62 - 0.0314159265358979*m.x63
                        - 0.0314159265358979*m.x64 - 0.0314159265358979*m.x65 - 0.0314159265358979*m.x66
                        - 0.0314159265358979*m.x67 - 0.0314159265358979*m.x68 - 0.0314159265358979*m.x69
                        - 0.0314159265358979*m.x70 - 0.0314159265358979*m.x71 - 0.0314159265358979*m.x72
                        - 0.0314159265358979*m.x73 - 0.0314159265358979*m.x74 - 0.0314159265358979*m.x75
                        - 0.0314159265358979*m.x76 - 0.0314159265358979*m.x77 - 0.0314159265358979*m.x78
                        - 0.0314159265358979*m.x79 - 0.0314159265358979*m.x80 - 0.0314159265358979*m.x81
                        - 0.0314159265358979*m.x82 - 0.0314159265358979*m.x83 - 0.0314159265358979*m.x84
                        - 0.0314159265358979*m.x85 - 0.0314159265358979*m.x86 - 0.0314159265358979*m.x87
                        - 0.0314159265358979*m.x88 - 0.0314159265358979*m.x89 - 0.0314159265358979*m.x90
                        - 0.0314159265358979*m.x91 - 0.0314159265358979*m.x92 - 0.0314159265358979*m.x93
                        - 0.0314159265358979*m.x94 - 0.0314159265358979*m.x95 - 0.0314159265358979*m.x96
                        - 0.0314159265358979*m.x97 - 0.0314159265358979*m.x98 - 0.0314159265358979*m.x99
                        - 0.0314159265358979*m.x100, sense=minimize)

m.c2 = Constraint(expr=(-m.x1*m.x2) - m.x2*m.x3 + 1.99984519984971*m.x1*m.x3 <= 0)

m.c3 = Constraint(expr=(-m.x2*m.x3) - m.x3*m.x4 + 1.99984519984971*m.x2*m.x4 <= 0)

m.c4 = Constraint(expr=(-m.x3*m.x4) - m.x4*m.x5 + 1.99984519984971*m.x3*m.x5 <= 0)

m.c5 = Constraint(expr=(-m.x4*m.x5) - m.x5*m.x6 + 1.99984519984971*m.x4*m.x6 <= 0)

m.c6 = Constraint(expr=(-m.x5*m.x6) - m.x6*m.x7 + 1.99984519984971*m.x5*m.x7 <= 0)

m.c7 = Constraint(expr=(-m.x6*m.x7) - m.x7*m.x8 + 1.99984519984971*m.x6*m.x8 <= 0)

m.c8 = Constraint(expr=(-m.x7*m.x8) - m.x8*m.x9 + 1.99984519984971*m.x7*m.x9 <= 0)

m.c9 = Constraint(expr=(-m.x8*m.x9) - m.x9*m.x10 + 1.99984519984971*m.x8*m.x10 <= 0)

m.c10 = Constraint(expr=(-m.x9*m.x10) - m.x10*m.x11 + 1.99984519984971*m.x9*m.x11 <= 0)

m.c11 = Constraint(expr=(-m.x10*m.x11) - m.x11*m.x12 + 1.99984519984971*m.x10*m.x12 <= 0)

m.c12 = Constraint(expr=(-m.x11*m.x12) - m.x12*m.x13 + 1.99984519984971*m.x11*m.x13 <= 0)

m.c13 = Constraint(expr=(-m.x12*m.x13) - m.x13*m.x14 + 1.99984519984971*m.x12*m.x14 <= 0)

m.c14 = Constraint(expr=(-m.x13*m.x14) - m.x14*m.x15 + 1.99984519984971*m.x13*m.x15 <= 0)

m.c15 = Constraint(expr=(-m.x14*m.x15) - m.x15*m.x16 + 1.99984519984971*m.x14*m.x16 <= 0)

m.c16 = Constraint(expr=(-m.x15*m.x16) - m.x16*m.x17 + 1.99984519984971*m.x15*m.x17 <= 0)

m.c17 = Constraint(expr=(-m.x16*m.x17) - m.x17*m.x18 + 1.99984519984971*m.x16*m.x18 <= 0)

m.c18 = Constraint(expr=(-m.x17*m.x18) - m.x18*m.x19 + 1.99984519984971*m.x17*m.x19 <= 0)

m.c19 = Constraint(expr=(-m.x18*m.x19) - m.x19*m.x20 + 1.99984519984971*m.x18*m.x20 <= 0)

m.c20 = Constraint(expr=(-m.x19*m.x20) - m.x20*m.x21 + 1.99984519984971*m.x19*m.x21 <= 0)

m.c21 = Constraint(expr=(-m.x20*m.x21) - m.x21*m.x22 + 1.99984519984971*m.x20*m.x22 <= 0)

m.c22 = Constraint(expr=(-m.x21*m.x22) - m.x22*m.x23 + 1.99984519984971*m.x21*m.x23 <= 0)

m.c23 = Constraint(expr=(-m.x22*m.x23) - m.x23*m.x24 + 1.99984519984971*m.x22*m.x24 <= 0)

m.c24 = Constraint(expr=(-m.x23*m.x24) - m.x24*m.x25 + 1.99984519984971*m.x23*m.x25 <= 0)

m.c25 = Constraint(expr=(-m.x24*m.x25) - m.x25*m.x26 + 1.99984519984971*m.x24*m.x26 <= 0)

m.c26 = Constraint(expr=(-m.x25*m.x26) - m.x26*m.x27 + 1.99984519984971*m.x25*m.x27 <= 0)

m.c27 = Constraint(expr=(-m.x26*m.x27) - m.x27*m.x28 + 1.99984519984971*m.x26*m.x28 <= 0)

m.c28 = Constraint(expr=(-m.x27*m.x28) - m.x28*m.x29 + 1.99984519984971*m.x27*m.x29 <= 0)

m.c29 = Constraint(expr=(-m.x28*m.x29) - m.x29*m.x30 + 1.99984519984971*m.x28*m.x30 <= 0)

m.c30 = Constraint(expr=(-m.x29*m.x30) - m.x30*m.x31 + 1.99984519984971*m.x29*m.x31 <= 0)

m.c31 = Constraint(expr=(-m.x30*m.x31) - m.x31*m.x32 + 1.99984519984971*m.x30*m.x32 <= 0)

m.c32 = Constraint(expr=(-m.x31*m.x32) - m.x32*m.x33 + 1.99984519984971*m.x31*m.x33 <= 0)

m.c33 = Constraint(expr=(-m.x32*m.x33) - m.x33*m.x34 + 1.99984519984971*m.x32*m.x34 <= 0)

m.c34 = Constraint(expr=(-m.x33*m.x34) - m.x34*m.x35 + 1.99984519984971*m.x33*m.x35 <= 0)

m.c35 = Constraint(expr=(-m.x34*m.x35) - m.x35*m.x36 + 1.99984519984971*m.x34*m.x36 <= 0)

m.c36 = Constraint(expr=(-m.x35*m.x36) - m.x36*m.x37 + 1.99984519984971*m.x35*m.x37 <= 0)

m.c37 = Constraint(expr=(-m.x36*m.x37) - m.x37*m.x38 + 1.99984519984971*m.x36*m.x38 <= 0)

m.c38 = Constraint(expr=(-m.x37*m.x38) - m.x38*m.x39 + 1.99984519984971*m.x37*m.x39 <= 0)

m.c39 = Constraint(expr=(-m.x38*m.x39) - m.x39*m.x40 + 1.99984519984971*m.x38*m.x40 <= 0)

m.c40 = Constraint(expr=(-m.x39*m.x40) - m.x40*m.x41 + 1.99984519984971*m.x39*m.x41 <= 0)

m.c41 = Constraint(expr=(-m.x40*m.x41) - m.x41*m.x42 + 1.99984519984971*m.x40*m.x42 <= 0)

m.c42 = Constraint(expr=(-m.x41*m.x42) - m.x42*m.x43 + 1.99984519984971*m.x41*m.x43 <= 0)

m.c43 = Constraint(expr=(-m.x42*m.x43) - m.x43*m.x44 + 1.99984519984971*m.x42*m.x44 <= 0)

m.c44 = Constraint(expr=(-m.x43*m.x44) - m.x44*m.x45 + 1.99984519984971*m.x43*m.x45 <= 0)

m.c45 = Constraint(expr=(-m.x44*m.x45) - m.x45*m.x46 + 1.99984519984971*m.x44*m.x46 <= 0)

m.c46 = Constraint(expr=(-m.x45*m.x46) - m.x46*m.x47 + 1.99984519984971*m.x45*m.x47 <= 0)

m.c47 = Constraint(expr=(-m.x46*m.x47) - m.x47*m.x48 + 1.99984519984971*m.x46*m.x48 <= 0)

m.c48 = Constraint(expr=(-m.x47*m.x48) - m.x48*m.x49 + 1.99984519984971*m.x47*m.x49 <= 0)

m.c49 = Constraint(expr=(-m.x48*m.x49) - m.x49*m.x50 + 1.99984519984971*m.x48*m.x50 <= 0)

m.c50 = Constraint(expr=(-m.x49*m.x50) - m.x50*m.x51 + 1.99984519984971*m.x49*m.x51 <= 0)

m.c51 = Constraint(expr=(-m.x50*m.x51) - m.x51*m.x52 + 1.99984519984971*m.x50*m.x52 <= 0)

m.c52 = Constraint(expr=(-m.x51*m.x52) - m.x52*m.x53 + 1.99984519984971*m.x51*m.x53 <= 0)

m.c53 = Constraint(expr=(-m.x52*m.x53) - m.x53*m.x54 + 1.99984519984971*m.x52*m.x54 <= 0)

m.c54 = Constraint(expr=(-m.x53*m.x54) - m.x54*m.x55 + 1.99984519984971*m.x53*m.x55 <= 0)

m.c55 = Constraint(expr=(-m.x54*m.x55) - m.x55*m.x56 + 1.99984519984971*m.x54*m.x56 <= 0)

m.c56 = Constraint(expr=(-m.x55*m.x56) - m.x56*m.x57 + 1.99984519984971*m.x55*m.x57 <= 0)

m.c57 = Constraint(expr=(-m.x56*m.x57) - m.x57*m.x58 + 1.99984519984971*m.x56*m.x58 <= 0)

m.c58 = Constraint(expr=(-m.x57*m.x58) - m.x58*m.x59 + 1.99984519984971*m.x57*m.x59 <= 0)

m.c59 = Constraint(expr=(-m.x58*m.x59) - m.x59*m.x60 + 1.99984519984971*m.x58*m.x60 <= 0)

m.c60 = Constraint(expr=(-m.x59*m.x60) - m.x60*m.x61 + 1.99984519984971*m.x59*m.x61 <= 0)

m.c61 = Constraint(expr=(-m.x60*m.x61) - m.x61*m.x62 + 1.99984519984971*m.x60*m.x62 <= 0)

m.c62 = Constraint(expr=(-m.x61*m.x62) - m.x62*m.x63 + 1.99984519984971*m.x61*m.x63 <= 0)

m.c63 = Constraint(expr=(-m.x62*m.x63) - m.x63*m.x64 + 1.99984519984971*m.x62*m.x64 <= 0)

m.c64 = Constraint(expr=(-m.x63*m.x64) - m.x64*m.x65 + 1.99984519984971*m.x63*m.x65 <= 0)

m.c65 = Constraint(expr=(-m.x64*m.x65) - m.x65*m.x66 + 1.99984519984971*m.x64*m.x66 <= 0)

m.c66 = Constraint(expr=(-m.x65*m.x66) - m.x66*m.x67 + 1.99984519984971*m.x65*m.x67 <= 0)

m.c67 = Constraint(expr=(-m.x66*m.x67) - m.x67*m.x68 + 1.99984519984971*m.x66*m.x68 <= 0)

m.c68 = Constraint(expr=(-m.x67*m.x68) - m.x68*m.x69 + 1.99984519984971*m.x67*m.x69 <= 0)

m.c69 = Constraint(expr=(-m.x68*m.x69) - m.x69*m.x70 + 1.99984519984971*m.x68*m.x70 <= 0)

m.c70 = Constraint(expr=(-m.x69*m.x70) - m.x70*m.x71 + 1.99984519984971*m.x69*m.x71 <= 0)

m.c71 = Constraint(expr=(-m.x70*m.x71) - m.x71*m.x72 + 1.99984519984971*m.x70*m.x72 <= 0)

m.c72 = Constraint(expr=(-m.x71*m.x72) - m.x72*m.x73 + 1.99984519984971*m.x71*m.x73 <= 0)

m.c73 = Constraint(expr=(-m.x72*m.x73) - m.x73*m.x74 + 1.99984519984971*m.x72*m.x74 <= 0)

m.c74 = Constraint(expr=(-m.x73*m.x74) - m.x74*m.x75 + 1.99984519984971*m.x73*m.x75 <= 0)

m.c75 = Constraint(expr=(-m.x74*m.x75) - m.x75*m.x76 + 1.99984519984971*m.x74*m.x76 <= 0)

m.c76 = Constraint(expr=(-m.x75*m.x76) - m.x76*m.x77 + 1.99984519984971*m.x75*m.x77 <= 0)

m.c77 = Constraint(expr=(-m.x76*m.x77) - m.x77*m.x78 + 1.99984519984971*m.x76*m.x78 <= 0)

m.c78 = Constraint(expr=(-m.x77*m.x78) - m.x78*m.x79 + 1.99984519984971*m.x77*m.x79 <= 0)

m.c79 = Constraint(expr=(-m.x78*m.x79) - m.x79*m.x80 + 1.99984519984971*m.x78*m.x80 <= 0)

m.c80 = Constraint(expr=(-m.x79*m.x80) - m.x80*m.x81 + 1.99984519984971*m.x79*m.x81 <= 0)

m.c81 = Constraint(expr=(-m.x80*m.x81) - m.x81*m.x82 + 1.99984519984971*m.x80*m.x82 <= 0)

m.c82 = Constraint(expr=(-m.x81*m.x82) - m.x82*m.x83 + 1.99984519984971*m.x81*m.x83 <= 0)

m.c83 = Constraint(expr=(-m.x82*m.x83) - m.x83*m.x84 + 1.99984519984971*m.x82*m.x84 <= 0)

m.c84 = Constraint(expr=(-m.x83*m.x84) - m.x84*m.x85 + 1.99984519984971*m.x83*m.x85 <= 0)

m.c85 = Constraint(expr=(-m.x84*m.x85) - m.x85*m.x86 + 1.99984519984971*m.x84*m.x86 <= 0)

m.c86 = Constraint(expr=(-m.x85*m.x86) - m.x86*m.x87 + 1.99984519984971*m.x85*m.x87 <= 0)

m.c87 = Constraint(expr=(-m.x86*m.x87) - m.x87*m.x88 + 1.99984519984971*m.x86*m.x88 <= 0)

m.c88 = Constraint(expr=(-m.x87*m.x88) - m.x88*m.x89 + 1.99984519984971*m.x87*m.x89 <= 0)

m.c89 = Constraint(expr=(-m.x88*m.x89) - m.x89*m.x90 + 1.99984519984971*m.x88*m.x90 <= 0)

m.c90 = Constraint(expr=(-m.x89*m.x90) - m.x90*m.x91 + 1.99984519984971*m.x89*m.x91 <= 0)

m.c91 = Constraint(expr=(-m.x90*m.x91) - m.x91*m.x92 + 1.99984519984971*m.x90*m.x92 <= 0)

m.c92 = Constraint(expr=(-m.x91*m.x92) - m.x92*m.x93 + 1.99984519984971*m.x91*m.x93 <= 0)

m.c93 = Constraint(expr=(-m.x92*m.x93) - m.x93*m.x94 + 1.99984519984971*m.x92*m.x94 <= 0)

m.c94 = Constraint(expr=(-m.x93*m.x94) - m.x94*m.x95 + 1.99984519984971*m.x93*m.x95 <= 0)

m.c95 = Constraint(expr=(-m.x94*m.x95) - m.x95*m.x96 + 1.99984519984971*m.x94*m.x96 <= 0)

m.c96 = Constraint(expr=(-m.x95*m.x96) - m.x96*m.x97 + 1.99984519984971*m.x95*m.x97 <= 0)

m.c97 = Constraint(expr=(-m.x96*m.x97) - m.x97*m.x98 + 1.99984519984971*m.x96*m.x98 <= 0)

m.c98 = Constraint(expr=(-m.x97*m.x98) - m.x98*m.x99 + 1.99984519984971*m.x97*m.x99 <= 0)

m.c99 = Constraint(expr=(-m.x98*m.x99) - m.x99*m.x100 + 1.99984519984971*m.x98*m.x100 <= 0)

m.c100 = Constraint(expr=(-m.x1*m.x2) - m.x1 + 1.99984519984971*m.x2 <= 0)

m.c101 = Constraint(expr=(-m.x99*m.x100) - 2*m.x100 + 3.99969039969942*m.x99 <= 0)

m.c102 = Constraint(expr=1.99984519984971*m.x100**2 - 4*m.x100 <= 0)

m.c103 = Constraint(expr=   m.x1 - m.x2 + m.x101 == 0)

m.c104 = Constraint(expr=   m.x2 - m.x3 + m.x102 == 0)

m.c105 = Constraint(expr=   m.x3 - m.x4 + m.x103 == 0)

m.c106 = Constraint(expr=   m.x4 - m.x5 + m.x104 == 0)

m.c107 = Constraint(expr=   m.x5 - m.x6 + m.x105 == 0)

m.c108 = Constraint(expr=   m.x6 - m.x7 + m.x106 == 0)

m.c109 = Constraint(expr=   m.x7 - m.x8 + m.x107 == 0)

m.c110 = Constraint(expr=   m.x8 - m.x9 + m.x108 == 0)

m.c111 = Constraint(expr=   m.x9 - m.x10 + m.x109 == 0)

m.c112 = Constraint(expr=   m.x10 - m.x11 + m.x110 == 0)

m.c113 = Constraint(expr=   m.x11 - m.x12 + m.x111 == 0)

m.c114 = Constraint(expr=   m.x12 - m.x13 + m.x112 == 0)

m.c115 = Constraint(expr=   m.x13 - m.x14 + m.x113 == 0)

m.c116 = Constraint(expr=   m.x14 - m.x15 + m.x114 == 0)

m.c117 = Constraint(expr=   m.x15 - m.x16 + m.x115 == 0)

m.c118 = Constraint(expr=   m.x16 - m.x17 + m.x116 == 0)

m.c119 = Constraint(expr=   m.x17 - m.x18 + m.x117 == 0)

m.c120 = Constraint(expr=   m.x18 - m.x19 + m.x118 == 0)

m.c121 = Constraint(expr=   m.x19 - m.x20 + m.x119 == 0)

m.c122 = Constraint(expr=   m.x20 - m.x21 + m.x120 == 0)

m.c123 = Constraint(expr=   m.x21 - m.x22 + m.x121 == 0)

m.c124 = Constraint(expr=   m.x22 - m.x23 + m.x122 == 0)

m.c125 = Constraint(expr=   m.x23 - m.x24 + m.x123 == 0)

m.c126 = Constraint(expr=   m.x24 - m.x25 + m.x124 == 0)

m.c127 = Constraint(expr=   m.x25 - m.x26 + m.x125 == 0)

m.c128 = Constraint(expr=   m.x26 - m.x27 + m.x126 == 0)

m.c129 = Constraint(expr=   m.x27 - m.x28 + m.x127 == 0)

m.c130 = Constraint(expr=   m.x28 - m.x29 + m.x128 == 0)

m.c131 = Constraint(expr=   m.x29 - m.x30 + m.x129 == 0)

m.c132 = Constraint(expr=   m.x30 - m.x31 + m.x130 == 0)

m.c133 = Constraint(expr=   m.x31 - m.x32 + m.x131 == 0)

m.c134 = Constraint(expr=   m.x32 - m.x33 + m.x132 == 0)

m.c135 = Constraint(expr=   m.x33 - m.x34 + m.x133 == 0)

m.c136 = Constraint(expr=   m.x34 - m.x35 + m.x134 == 0)

m.c137 = Constraint(expr=   m.x35 - m.x36 + m.x135 == 0)

m.c138 = Constraint(expr=   m.x36 - m.x37 + m.x136 == 0)

m.c139 = Constraint(expr=   m.x37 - m.x38 + m.x137 == 0)

m.c140 = Constraint(expr=   m.x38 - m.x39 + m.x138 == 0)

m.c141 = Constraint(expr=   m.x39 - m.x40 + m.x139 == 0)

m.c142 = Constraint(expr=   m.x40 - m.x41 + m.x140 == 0)

m.c143 = Constraint(expr=   m.x41 - m.x42 + m.x141 == 0)

m.c144 = Constraint(expr=   m.x42 - m.x43 + m.x142 == 0)

m.c145 = Constraint(expr=   m.x43 - m.x44 + m.x143 == 0)

m.c146 = Constraint(expr=   m.x44 - m.x45 + m.x144 == 0)

m.c147 = Constraint(expr=   m.x45 - m.x46 + m.x145 == 0)

m.c148 = Constraint(expr=   m.x46 - m.x47 + m.x146 == 0)

m.c149 = Constraint(expr=   m.x47 - m.x48 + m.x147 == 0)

m.c150 = Constraint(expr=   m.x48 - m.x49 + m.x148 == 0)

m.c151 = Constraint(expr=   m.x49 - m.x50 + m.x149 == 0)

m.c152 = Constraint(expr=   m.x50 - m.x51 + m.x150 == 0)

m.c153 = Constraint(expr=   m.x51 - m.x52 + m.x151 == 0)

m.c154 = Constraint(expr=   m.x52 - m.x53 + m.x152 == 0)

m.c155 = Constraint(expr=   m.x53 - m.x54 + m.x153 == 0)

m.c156 = Constraint(expr=   m.x54 - m.x55 + m.x154 == 0)

m.c157 = Constraint(expr=   m.x55 - m.x56 + m.x155 == 0)

m.c158 = Constraint(expr=   m.x56 - m.x57 + m.x156 == 0)

m.c159 = Constraint(expr=   m.x57 - m.x58 + m.x157 == 0)

m.c160 = Constraint(expr=   m.x58 - m.x59 + m.x158 == 0)

m.c161 = Constraint(expr=   m.x59 - m.x60 + m.x159 == 0)

m.c162 = Constraint(expr=   m.x60 - m.x61 + m.x160 == 0)

m.c163 = Constraint(expr=   m.x61 - m.x62 + m.x161 == 0)

m.c164 = Constraint(expr=   m.x62 - m.x63 + m.x162 == 0)

m.c165 = Constraint(expr=   m.x63 - m.x64 + m.x163 == 0)

m.c166 = Constraint(expr=   m.x64 - m.x65 + m.x164 == 0)

m.c167 = Constraint(expr=   m.x65 - m.x66 + m.x165 == 0)

m.c168 = Constraint(expr=   m.x66 - m.x67 + m.x166 == 0)

m.c169 = Constraint(expr=   m.x67 - m.x68 + m.x167 == 0)

m.c170 = Constraint(expr=   m.x68 - m.x69 + m.x168 == 0)

m.c171 = Constraint(expr=   m.x69 - m.x70 + m.x169 == 0)

m.c172 = Constraint(expr=   m.x70 - m.x71 + m.x170 == 0)

m.c173 = Constraint(expr=   m.x71 - m.x72 + m.x171 == 0)

m.c174 = Constraint(expr=   m.x72 - m.x73 + m.x172 == 0)

m.c175 = Constraint(expr=   m.x73 - m.x74 + m.x173 == 0)

m.c176 = Constraint(expr=   m.x74 - m.x75 + m.x174 == 0)

m.c177 = Constraint(expr=   m.x75 - m.x76 + m.x175 == 0)

m.c178 = Constraint(expr=   m.x76 - m.x77 + m.x176 == 0)

m.c179 = Constraint(expr=   m.x77 - m.x78 + m.x177 == 0)

m.c180 = Constraint(expr=   m.x78 - m.x79 + m.x178 == 0)

m.c181 = Constraint(expr=   m.x79 - m.x80 + m.x179 == 0)

m.c182 = Constraint(expr=   m.x80 - m.x81 + m.x180 == 0)

m.c183 = Constraint(expr=   m.x81 - m.x82 + m.x181 == 0)

m.c184 = Constraint(expr=   m.x82 - m.x83 + m.x182 == 0)

m.c185 = Constraint(expr=   m.x83 - m.x84 + m.x183 == 0)

m.c186 = Constraint(expr=   m.x84 - m.x85 + m.x184 == 0)

m.c187 = Constraint(expr=   m.x85 - m.x86 + m.x185 == 0)

m.c188 = Constraint(expr=   m.x86 - m.x87 + m.x186 == 0)

m.c189 = Constraint(expr=   m.x87 - m.x88 + m.x187 == 0)

m.c190 = Constraint(expr=   m.x88 - m.x89 + m.x188 == 0)

m.c191 = Constraint(expr=   m.x89 - m.x90 + m.x189 == 0)

m.c192 = Constraint(expr=   m.x90 - m.x91 + m.x190 == 0)

m.c193 = Constraint(expr=   m.x91 - m.x92 + m.x191 == 0)

m.c194 = Constraint(expr=   m.x92 - m.x93 + m.x192 == 0)

m.c195 = Constraint(expr=   m.x93 - m.x94 + m.x193 == 0)

m.c196 = Constraint(expr=   m.x94 - m.x95 + m.x194 == 0)

m.c197 = Constraint(expr=   m.x95 - m.x96 + m.x195 == 0)

m.c198 = Constraint(expr=   m.x96 - m.x97 + m.x196 == 0)

m.c199 = Constraint(expr=   m.x97 - m.x98 + m.x197 == 0)

m.c200 = Constraint(expr=   m.x98 - m.x99 + m.x198 == 0)

m.c201 = Constraint(expr=   m.x99 - m.x100 + m.x199 == 0)
