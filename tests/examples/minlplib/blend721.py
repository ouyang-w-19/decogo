#  MINLP written by GAMS Convert at 04/21/18 13:51:13
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        628       49      147      432        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        223      136       87        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1766     1510      256        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x34 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x35 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x36 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x37 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x38 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x39 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x40 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x41 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x42 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x43 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x44 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x45 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x46 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x47 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x48 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x49 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x50 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x51 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x52 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x53 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x54 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x55 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x56 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x57 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x58 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x59 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x60 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x61 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x62 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x63 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x64 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x65 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x66 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x67 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x68 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x69 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x70 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x71 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x72 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x73 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x74 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x75 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x76 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x77 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x78 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x79 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x80 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x81 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x82 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x83 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x84 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x85 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x86 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x87 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x88 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x89 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x90 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x91 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x92 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x93 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x94 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x95 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x96 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x97 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x98 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x99 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x100 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x101 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x102 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x103 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x104 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x105 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x106 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x107 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x108 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x109 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x110 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x111 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x112 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x113 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x114 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x115 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x116 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x117 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x118 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x119 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x120 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x121 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x122 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x123 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x124 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x125 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x126 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x127 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x128 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x129 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x130 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x131 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x132 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x133 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x134 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x135 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x136 = Var(within=Reals,bounds=(0,2),initialize=0)
m.b137 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b138 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b139 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b140 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b141 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b142 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b143 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b144 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b145 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b146 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b147 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b148 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b149 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b150 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b151 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b152 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b153 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b154 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b155 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b156 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b157 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b158 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b159 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b160 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b161 = Var(within=Binary,bounds=(0,1),initialize=0)
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
m.b173 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b174 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b175 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b176 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b177 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b178 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b179 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b180 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b181 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b182 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b183 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b184 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b185 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b186 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b187 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b188 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b189 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b190 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b191 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b192 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b193 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b194 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b195 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b196 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b197 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b198 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b199 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b200 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b201 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b202 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b203 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b204 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b205 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b206 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b207 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b208 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b209 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b210 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b211 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b212 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b213 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b214 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b215 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b216 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b217 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b218 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b219 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b220 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b221 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b222 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b223 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr= - 0.57*m.x2 - 0.57*m.x3 - 0.57*m.x4 - 0.94*m.x5 - 0.94*m.x6 - 0.94*m.x7 - 0.33*m.x8 - 0.33*m.x9
                        - 0.33*m.x10 - 0.33*m.x11 - 0.33*m.x12 - 0.33*m.x13 + 3.59*m.x14 + 3.59*m.x15 + 3.59*m.x16
                        - 0.63*m.x17 - 0.63*m.x18 - 0.63*m.x19 - 1.1*m.x20 - 1.1*m.x21 - 1.1*m.x22 - 0.64*m.x23
                        - 0.64*m.x24 - 0.64*m.x25 + 3.54*m.x26 + 3.54*m.x27 + 3.54*m.x28 - 0.59*m.x29 - 0.59*m.x30
                        - 0.59*m.x31 - 0.6*m.x32 - 0.6*m.x33 - 0.6*m.x34 - 0.22*m.x35 - 0.22*m.x36 - 0.22*m.x37
                        + 4.8*m.x38 + 4.8*m.x39 + 4.8*m.x40 + 3.58*m.x41 + 3.58*m.x42 + 3.58*m.x43 - 0.09*m.x44
                        - 0.09*m.x45 - 0.09*m.x46 - 0.8*m.x47 - 0.8*m.x48 - 0.8*m.x49 - 0.93*m.x50 - 0.93*m.x51
                        - 0.93*m.x52 + 4.61*m.x53 + 4.61*m.x54 + 4.61*m.x55 + 3.76*m.x56 + 3.76*m.x57 + 3.76*m.x58
                        - 0.96*m.x59 - 0.96*m.x60 - 0.96*m.x61 - 0.52*m.x62 - 0.52*m.x63 - 0.52*m.x64 - 0.49*m.x65
                        - 0.49*m.x66 - 0.49*m.x67 + 4.42*m.x68 + 4.42*m.x69 + 4.42*m.x70 + 3.63*m.x71 + 3.63*m.x72
                        + 3.63*m.x73 - 0.04*m.x74 - 0.04*m.x75 - 0.04*m.x76 - 0.91*m.x77 - 0.91*m.x78 - 0.91*m.x79
                        - 0.1*m.x80 - 0.1*m.x81 - 0.1*m.x82 + 4.76*m.x83 + 4.76*m.x84 + 4.76*m.x85 + 3.86*m.x86
                        + 3.86*m.x87 + 3.86*m.x88 - 0.3*m.b137 - 0.3*m.b138 - 0.3*m.b139 - 0.23*m.b140 - 0.23*m.b141
                        - 0.23*m.b142 - 0.19*m.b143 - 0.19*m.b144 - 0.19*m.b145 - 0.17*m.b146 - 0.17*m.b147
                        - 0.17*m.b148 - 0.44*m.b149 - 0.44*m.b150 - 0.44*m.b151 - 0.92*m.b152 - 0.92*m.b153
                        - 0.92*m.b154 - 0.18*m.b155 - 0.18*m.b156 - 0.18*m.b157 - 0.98*m.b158 - 0.98*m.b159
                        - 0.98*m.b160 - 0.11*m.b161 - 0.11*m.b162 - 0.11*m.b163 - 0.41*m.b164 - 0.41*m.b165
                        - 0.41*m.b166 - 0.26*m.b167 - 0.26*m.b168 - 0.26*m.b169 - 0.71*m.b170 - 0.71*m.b171
                        - 0.71*m.b172 - 0.12*m.b173 - 0.12*m.b174 - 0.12*m.b175 - 0.32*m.b176 - 0.32*m.b177
                        - 0.32*m.b178 - 0.51*m.b179 - 0.51*m.b180 - 0.51*m.b181 - 0.26*m.b182 - 0.26*m.b183
                        - 0.26*m.b184 - 0.03*m.b185 - 0.03*m.b186 - 0.03*m.b187 - 0.73*m.b188 - 0.73*m.b189
                        - 0.73*m.b190 - 0.58*m.b191 - 0.58*m.b192 - 0.58*m.b193 - 0.46*m.b194 - 0.46*m.b195
                        - 0.46*m.b196 - 0.55*m.b197 - 0.55*m.b198 - 0.55*m.b199 - 0.23*m.b200 - 0.23*m.b201
                        - 0.23*m.b202 - 0.62*m.b203 - 0.62*m.b204 - 0.62*m.b205 - 0.4*m.b206 - 0.4*m.b207 - 0.4*m.b208
                        - 0.99*m.b209 - 0.99*m.b210 - 0.99*m.b211 - 0.89*m.b212 - 0.89*m.b213 - 0.89*m.b214 - 0.8*m.b215
                        - 0.8*m.b216 - 0.8*m.b217 - 0.26*m.b218 - 0.26*m.b219 - 0.26*m.b220 - 0.68*m.b221 - 0.68*m.b222
                        - 0.68*m.b223, sense=maximize)

m.c2 = Constraint(expr=   m.x2 + m.x5 + m.x8 + m.x11 + m.x14 + m.x113 == 1.3)

m.c3 = Constraint(expr=   m.x17 + m.x20 + m.x23 + m.x26 + m.x116 == 2.3)

m.c4 = Constraint(expr= - m.x2 + m.x29 + m.x32 + m.x35 + m.x38 + m.x41 - m.x44 - m.x59 - m.x74 + m.x119 == 1.2)

m.c5 = Constraint(expr= - m.x5 - m.x17 - m.x29 + m.x44 + m.x47 + m.x50 + m.x53 + m.x56 - m.x62 - m.x77 + m.x122 == 1.1)

m.c6 = Constraint(expr= - m.x8 - m.x20 - m.x32 - m.x47 + m.x59 + m.x62 + m.x65 + m.x68 + m.x71 - m.x80 + m.x125 == 0.3)

m.c7 = Constraint(expr= - m.x11 - m.x23 - m.x35 - m.x50 - m.x65 + m.x74 + m.x77 + m.x80 + m.x83 + m.x86 + m.x128 == 1.7)

m.c8 = Constraint(expr= - m.x38 - m.x53 - m.x68 - m.x83 + m.x131 == 1.18)

m.c9 = Constraint(expr= - m.x14 - m.x26 - m.x41 - m.x56 - m.x71 - m.x86 + m.x134 == 0.66)

m.c10 = Constraint(expr=m.x89*m.x119 - 0.4*m.x2 + 0.5*m.x29 + 0.5*m.x32 + 0.5*m.x35 + 0.5*m.x38 + 0.5*m.x41 - 0.9*m.x44
                         - 0.1*m.x59 - 0.4*m.x74 == 0.6)

m.c11 = Constraint(expr=m.x92*m.x122 - 0.4*m.x5 - 0.1*m.x17 - 0.5*m.x29 + 0.9*m.x44 + 0.9*m.x47 + 0.9*m.x50 + 0.9*m.x53
                         + 0.9*m.x56 - 0.1*m.x62 - 0.4*m.x77 == 0.99)

m.c12 = Constraint(expr=m.x95*m.x125 - 0.4*m.x8 - 0.1*m.x20 - 0.5*m.x32 - 0.9*m.x47 + 0.1*m.x59 + 0.1*m.x62 + 0.1*m.x65
                         + 0.1*m.x68 + 0.1*m.x71 - 0.4*m.x80 == 0.03)

m.c13 = Constraint(expr=m.x98*m.x128 - 0.4*m.x11 - 0.1*m.x23 - 0.5*m.x35 - 0.9*m.x50 - 0.1*m.x65 + 0.4*m.x74 + 0.4*m.x77
                         + 0.4*m.x80 + 0.4*m.x83 + 0.4*m.x86 == 0.68)

m.c14 = Constraint(expr=m.x101*m.x119 - 0.1*m.x2 + 0.3*m.x29 + 0.3*m.x32 + 0.3*m.x35 + 0.3*m.x38 + 0.3*m.x41 - 0.4*m.x44
                         - 0.8*m.x59 - 0.2*m.x74 == 0.36)

m.c15 = Constraint(expr=m.x104*m.x122 - 0.1*m.x5 - 0.9*m.x17 - 0.3*m.x29 + 0.4*m.x44 + 0.4*m.x47 + 0.4*m.x50 + 0.4*m.x53
                         + 0.4*m.x56 - 0.8*m.x62 - 0.2*m.x77 == 0.44)

m.c16 = Constraint(expr=m.x107*m.x125 - 0.1*m.x8 - 0.9*m.x20 - 0.3*m.x32 - 0.4*m.x47 + 0.8*m.x59 + 0.8*m.x62 + 0.8*m.x65
                         + 0.8*m.x68 + 0.8*m.x71 - 0.2*m.x80 == 0.24)

m.c17 = Constraint(expr=m.x110*m.x128 - 0.1*m.x11 - 0.9*m.x23 - 0.3*m.x35 - 0.4*m.x50 - 0.8*m.x65 + 0.2*m.x74
                         + 0.2*m.x77 + 0.2*m.x80 + 0.2*m.x83 + 0.2*m.x86 == 0.34)

m.c18 = Constraint(expr=   m.x3 + m.x6 + m.x9 + m.x12 + m.x15 - m.x113 + m.x114 == 0.1)

m.c19 = Constraint(expr=   m.x4 + m.x7 + m.x10 + m.x13 + m.x16 - m.x114 + m.x115 == 0.4)

m.c20 = Constraint(expr=   m.x18 + m.x21 + m.x24 + m.x27 - m.x116 + m.x117 == 0.2)

m.c21 = Constraint(expr=   m.x19 + m.x22 + m.x25 + m.x28 - m.x117 + m.x118 == 0.8)

m.c22 = Constraint(expr= - m.x3 + m.x30 + m.x33 + m.x36 + m.x39 + m.x42 - m.x45 - m.x60 - m.x75 - m.x119 + m.x120 == 0)

m.c23 = Constraint(expr= - m.x4 + m.x31 + m.x34 + m.x37 + m.x40 + m.x43 - m.x46 - m.x61 - m.x76 - m.x120 + m.x121 == 0)

m.c24 = Constraint(expr= - m.x6 - m.x18 - m.x30 + m.x45 + m.x48 + m.x51 + m.x54 + m.x57 - m.x63 - m.x78 - m.x122
                         + m.x123 == 0)

m.c25 = Constraint(expr= - m.x7 - m.x19 - m.x31 + m.x46 + m.x49 + m.x52 + m.x55 + m.x58 - m.x64 - m.x79 - m.x123
                         + m.x124 == 0)

m.c26 = Constraint(expr= - m.x9 - m.x21 - m.x33 - m.x48 + m.x60 + m.x63 + m.x66 + m.x69 + m.x72 - m.x81 - m.x125
                         + m.x126 == 0)

m.c27 = Constraint(expr= - m.x10 - m.x22 - m.x34 - m.x49 + m.x61 + m.x64 + m.x67 + m.x70 + m.x73 - m.x82 - m.x126
                         + m.x127 == 0)

m.c28 = Constraint(expr= - m.x12 - m.x24 - m.x36 - m.x51 - m.x66 + m.x75 + m.x78 + m.x81 + m.x84 + m.x87 - m.x128
                         + m.x129 == 0)

m.c29 = Constraint(expr= - m.x13 - m.x25 - m.x37 - m.x52 - m.x67 + m.x76 + m.x79 + m.x82 + m.x85 + m.x88 - m.x129
                         + m.x130 == 0)

m.c30 = Constraint(expr= - m.x39 - m.x54 - m.x69 - m.x84 - m.x131 + m.x132 == -0.17)

m.c31 = Constraint(expr= - m.x40 - m.x55 - m.x70 - m.x85 - m.x132 + m.x133 == -0.73)

m.c32 = Constraint(expr= - m.x15 - m.x27 - m.x42 - m.x57 - m.x72 - m.x87 - m.x134 + m.x135 == -0.65)

m.c33 = Constraint(expr= - m.x16 - m.x28 - m.x43 - m.x58 - m.x73 - m.x88 - m.x135 + m.x136 == -0.65)

m.c34 = Constraint(expr=m.x90*m.x120 - (m.x89*m.x119 + m.x92*m.x45 + m.x95*m.x60 + m.x98*m.x75 - (m.x89*m.x30 + m.x89*
                        m.x33 + m.x89*m.x36 + m.x89*m.x39 + m.x89*m.x42)) - 0.4*m.x3 == 0)

m.c35 = Constraint(expr=m.x91*m.x121 - (m.x90*m.x120 + m.x93*m.x46 + m.x96*m.x61 + m.x99*m.x76 - (m.x90*m.x31 + m.x90*
                        m.x34 + m.x90*m.x37 + m.x90*m.x40 + m.x90*m.x43)) - 0.4*m.x4 == 0)

m.c36 = Constraint(expr=m.x93*m.x123 - (m.x92*m.x122 + m.x89*m.x30 + m.x95*m.x63 + m.x98*m.x78 - (m.x92*m.x45 + m.x92*
                        m.x48 + m.x92*m.x51 + m.x92*m.x54 + m.x92*m.x57)) - 0.4*m.x6 - 0.1*m.x18 == 0)

m.c37 = Constraint(expr=m.x94*m.x124 - (m.x93*m.x123 + m.x90*m.x31 + m.x96*m.x64 + m.x99*m.x79 - (m.x93*m.x46 + m.x93*
                        m.x49 + m.x93*m.x52 + m.x93*m.x55 + m.x93*m.x58)) - 0.4*m.x7 - 0.1*m.x19 == 0)

m.c38 = Constraint(expr=m.x96*m.x126 - (m.x95*m.x125 + m.x89*m.x33 + m.x92*m.x48 + m.x98*m.x81 - (m.x95*m.x60 + m.x95*
                        m.x63 + m.x95*m.x66 + m.x95*m.x69 + m.x95*m.x72)) - 0.4*m.x9 - 0.1*m.x21 == 0)

m.c39 = Constraint(expr=m.x97*m.x127 - (m.x96*m.x126 + m.x90*m.x34 + m.x93*m.x49 + m.x99*m.x82 - (m.x96*m.x61 + m.x96*
                        m.x64 + m.x96*m.x67 + m.x96*m.x70 + m.x96*m.x73)) - 0.4*m.x10 - 0.1*m.x22 == 0)

m.c40 = Constraint(expr=m.x99*m.x129 - (m.x98*m.x128 + m.x89*m.x36 + m.x92*m.x51 + m.x95*m.x66 - (m.x98*m.x75 + m.x98*
                        m.x78 + m.x98*m.x81 + m.x98*m.x84 + m.x98*m.x87)) - 0.4*m.x12 - 0.1*m.x24 == 0)

m.c41 = Constraint(expr=m.x100*m.x130 - (m.x99*m.x129 + m.x90*m.x37 + m.x93*m.x52 + m.x96*m.x67 - (m.x99*m.x76 + m.x99*
                        m.x79 + m.x99*m.x82 + m.x99*m.x85 + m.x99*m.x88)) - 0.4*m.x13 - 0.1*m.x25 == 0)

m.c42 = Constraint(expr=m.x102*m.x120 - (m.x101*m.x119 + m.x104*m.x45 + m.x107*m.x60 + m.x110*m.x75 - (m.x101*m.x30 + 
                        m.x101*m.x33 + m.x101*m.x36 + m.x101*m.x39 + m.x101*m.x42)) - 0.1*m.x3 == 0)

m.c43 = Constraint(expr=m.x103*m.x121 - (m.x102*m.x120 + m.x105*m.x46 + m.x108*m.x61 + m.x111*m.x76 - (m.x102*m.x31 + 
                        m.x102*m.x34 + m.x102*m.x37 + m.x102*m.x40 + m.x102*m.x43)) - 0.1*m.x4 == 0)

m.c44 = Constraint(expr=m.x105*m.x123 - (m.x104*m.x122 + m.x101*m.x30 + m.x107*m.x63 + m.x110*m.x78 - (m.x104*m.x45 + 
                        m.x104*m.x48 + m.x104*m.x51 + m.x104*m.x54 + m.x104*m.x57)) - 0.1*m.x6 - 0.9*m.x18 == 0)

m.c45 = Constraint(expr=m.x106*m.x124 - (m.x105*m.x123 + m.x102*m.x31 + m.x108*m.x64 + m.x111*m.x79 - (m.x105*m.x46 + 
                        m.x105*m.x49 + m.x105*m.x52 + m.x105*m.x55 + m.x105*m.x58)) - 0.1*m.x7 - 0.9*m.x19 == 0)

m.c46 = Constraint(expr=m.x108*m.x126 - (m.x107*m.x125 + m.x101*m.x33 + m.x104*m.x48 + m.x110*m.x81 - (m.x107*m.x60 + 
                        m.x107*m.x63 + m.x107*m.x66 + m.x107*m.x69 + m.x107*m.x72)) - 0.1*m.x9 - 0.9*m.x21 == 0)

m.c47 = Constraint(expr=m.x109*m.x127 - (m.x108*m.x126 + m.x102*m.x34 + m.x105*m.x49 + m.x111*m.x82 - (m.x108*m.x61 + 
                        m.x108*m.x64 + m.x108*m.x67 + m.x108*m.x70 + m.x108*m.x73)) - 0.1*m.x10 - 0.9*m.x22 == 0)

m.c48 = Constraint(expr=m.x111*m.x129 - (m.x110*m.x128 + m.x101*m.x36 + m.x104*m.x51 + m.x107*m.x66 - (m.x110*m.x75 + 
                        m.x110*m.x78 + m.x110*m.x81 + m.x110*m.x84 + m.x110*m.x87)) - 0.1*m.x12 - 0.9*m.x24 == 0)

m.c49 = Constraint(expr=m.x112*m.x130 - (m.x111*m.x129 + m.x102*m.x37 + m.x105*m.x52 + m.x108*m.x67 - (m.x111*m.x76 + 
                        m.x111*m.x79 + m.x111*m.x82 + m.x111*m.x85 + m.x111*m.x88)) - 0.1*m.x13 - 0.9*m.x25 == 0)

m.c50 = Constraint(expr=   m.x2 - m.b137 <= 0)

m.c51 = Constraint(expr=   m.x3 - m.b138 <= 0)

m.c52 = Constraint(expr=   m.x4 - m.b139 <= 0)

m.c53 = Constraint(expr=   m.x5 - m.b140 <= 0)

m.c54 = Constraint(expr=   m.x6 - m.b141 <= 0)

m.c55 = Constraint(expr=   m.x7 - m.b142 <= 0)

m.c56 = Constraint(expr=   m.x8 - m.b143 <= 0)

m.c57 = Constraint(expr=   m.x9 - m.b144 <= 0)

m.c58 = Constraint(expr=   m.x10 - m.b145 <= 0)

m.c59 = Constraint(expr=   m.x11 - m.b146 <= 0)

m.c60 = Constraint(expr=   m.x12 - m.b147 <= 0)

m.c61 = Constraint(expr=   m.x13 - m.b148 <= 0)

m.c62 = Constraint(expr=   m.x14 - m.b149 <= 0)

m.c63 = Constraint(expr=   m.x15 - m.b150 <= 0)

m.c64 = Constraint(expr=   m.x16 - m.b151 <= 0)

m.c65 = Constraint(expr=   m.x17 - m.b152 <= 0)

m.c66 = Constraint(expr=   m.x18 - m.b153 <= 0)

m.c67 = Constraint(expr=   m.x19 - m.b154 <= 0)

m.c68 = Constraint(expr=   m.x20 - m.b155 <= 0)

m.c69 = Constraint(expr=   m.x21 - m.b156 <= 0)

m.c70 = Constraint(expr=   m.x22 - m.b157 <= 0)

m.c71 = Constraint(expr=   m.x23 - m.b158 <= 0)

m.c72 = Constraint(expr=   m.x24 - m.b159 <= 0)

m.c73 = Constraint(expr=   m.x25 - m.b160 <= 0)

m.c74 = Constraint(expr=   m.x26 - m.b161 <= 0)

m.c75 = Constraint(expr=   m.x27 - m.b162 <= 0)

m.c76 = Constraint(expr=   m.x28 - m.b163 <= 0)

m.c77 = Constraint(expr=   m.x29 - m.b164 <= 0)

m.c78 = Constraint(expr=   m.x30 - m.b165 <= 0)

m.c79 = Constraint(expr=   m.x31 - m.b166 <= 0)

m.c80 = Constraint(expr=   m.x32 - m.b167 <= 0)

m.c81 = Constraint(expr=   m.x33 - m.b168 <= 0)

m.c82 = Constraint(expr=   m.x34 - m.b169 <= 0)

m.c83 = Constraint(expr=   m.x35 - m.b170 <= 0)

m.c84 = Constraint(expr=   m.x36 - m.b171 <= 0)

m.c85 = Constraint(expr=   m.x37 - m.b172 <= 0)

m.c86 = Constraint(expr=   m.x38 - m.b173 <= 0)

m.c87 = Constraint(expr=   m.x39 - m.b174 <= 0)

m.c88 = Constraint(expr=   m.x40 - m.b175 <= 0)

m.c89 = Constraint(expr=   m.x41 - m.b176 <= 0)

m.c90 = Constraint(expr=   m.x42 - m.b177 <= 0)

m.c91 = Constraint(expr=   m.x43 - m.b178 <= 0)

m.c92 = Constraint(expr=   m.x44 - m.b179 <= 0)

m.c93 = Constraint(expr=   m.x45 - m.b180 <= 0)

m.c94 = Constraint(expr=   m.x46 - m.b181 <= 0)

m.c95 = Constraint(expr=   m.x47 - m.b182 <= 0)

m.c96 = Constraint(expr=   m.x48 - m.b183 <= 0)

m.c97 = Constraint(expr=   m.x49 - m.b184 <= 0)

m.c98 = Constraint(expr=   m.x50 - m.b185 <= 0)

m.c99 = Constraint(expr=   m.x51 - m.b186 <= 0)

m.c100 = Constraint(expr=   m.x52 - m.b187 <= 0)

m.c101 = Constraint(expr=   m.x53 - m.b188 <= 0)

m.c102 = Constraint(expr=   m.x54 - m.b189 <= 0)

m.c103 = Constraint(expr=   m.x55 - m.b190 <= 0)

m.c104 = Constraint(expr=   m.x56 - m.b191 <= 0)

m.c105 = Constraint(expr=   m.x57 - m.b192 <= 0)

m.c106 = Constraint(expr=   m.x58 - m.b193 <= 0)

m.c107 = Constraint(expr=   m.x59 - m.b194 <= 0)

m.c108 = Constraint(expr=   m.x60 - m.b195 <= 0)

m.c109 = Constraint(expr=   m.x61 - m.b196 <= 0)

m.c110 = Constraint(expr=   m.x62 - m.b197 <= 0)

m.c111 = Constraint(expr=   m.x63 - m.b198 <= 0)

m.c112 = Constraint(expr=   m.x64 - m.b199 <= 0)

m.c113 = Constraint(expr=   m.x65 - m.b200 <= 0)

m.c114 = Constraint(expr=   m.x66 - m.b201 <= 0)

m.c115 = Constraint(expr=   m.x67 - m.b202 <= 0)

m.c116 = Constraint(expr=   m.x68 - m.b203 <= 0)

m.c117 = Constraint(expr=   m.x69 - m.b204 <= 0)

m.c118 = Constraint(expr=   m.x70 - m.b205 <= 0)

m.c119 = Constraint(expr=   m.x71 - m.b206 <= 0)

m.c120 = Constraint(expr=   m.x72 - m.b207 <= 0)

m.c121 = Constraint(expr=   m.x73 - m.b208 <= 0)

m.c122 = Constraint(expr=   m.x74 - m.b209 <= 0)

m.c123 = Constraint(expr=   m.x75 - m.b210 <= 0)

m.c124 = Constraint(expr=   m.x76 - m.b211 <= 0)

m.c125 = Constraint(expr=   m.x77 - m.b212 <= 0)

m.c126 = Constraint(expr=   m.x78 - m.b213 <= 0)

m.c127 = Constraint(expr=   m.x79 - m.b214 <= 0)

m.c128 = Constraint(expr=   m.x80 - m.b215 <= 0)

m.c129 = Constraint(expr=   m.x81 - m.b216 <= 0)

m.c130 = Constraint(expr=   m.x82 - m.b217 <= 0)

m.c131 = Constraint(expr=   m.x83 - m.b218 <= 0)

m.c132 = Constraint(expr=   m.x84 - m.b219 <= 0)

m.c133 = Constraint(expr=   m.x85 - m.b220 <= 0)

m.c134 = Constraint(expr=   m.x86 - m.b221 <= 0)

m.c135 = Constraint(expr=   m.x87 - m.b222 <= 0)

m.c136 = Constraint(expr=   m.x88 - m.b223 <= 0)

m.c137 = Constraint(expr=   m.x2 >= 0)

m.c138 = Constraint(expr=   m.x3 >= 0)

m.c139 = Constraint(expr=   m.x4 >= 0)

m.c140 = Constraint(expr=   m.x5 >= 0)

m.c141 = Constraint(expr=   m.x6 >= 0)

m.c142 = Constraint(expr=   m.x7 >= 0)

m.c143 = Constraint(expr=   m.x8 >= 0)

m.c144 = Constraint(expr=   m.x9 >= 0)

m.c145 = Constraint(expr=   m.x10 >= 0)

m.c146 = Constraint(expr=   m.x11 >= 0)

m.c147 = Constraint(expr=   m.x12 >= 0)

m.c148 = Constraint(expr=   m.x13 >= 0)

m.c149 = Constraint(expr=   m.x14 >= 0)

m.c150 = Constraint(expr=   m.x15 >= 0)

m.c151 = Constraint(expr=   m.x16 >= 0)

m.c152 = Constraint(expr=   m.x17 >= 0)

m.c153 = Constraint(expr=   m.x18 >= 0)

m.c154 = Constraint(expr=   m.x19 >= 0)

m.c155 = Constraint(expr=   m.x20 >= 0)

m.c156 = Constraint(expr=   m.x21 >= 0)

m.c157 = Constraint(expr=   m.x22 >= 0)

m.c158 = Constraint(expr=   m.x23 >= 0)

m.c159 = Constraint(expr=   m.x24 >= 0)

m.c160 = Constraint(expr=   m.x25 >= 0)

m.c161 = Constraint(expr=   m.x26 >= 0)

m.c162 = Constraint(expr=   m.x27 >= 0)

m.c163 = Constraint(expr=   m.x28 >= 0)

m.c164 = Constraint(expr=   m.x29 >= 0)

m.c165 = Constraint(expr=   m.x30 >= 0)

m.c166 = Constraint(expr=   m.x31 >= 0)

m.c167 = Constraint(expr=   m.x32 >= 0)

m.c168 = Constraint(expr=   m.x33 >= 0)

m.c169 = Constraint(expr=   m.x34 >= 0)

m.c170 = Constraint(expr=   m.x35 >= 0)

m.c171 = Constraint(expr=   m.x36 >= 0)

m.c172 = Constraint(expr=   m.x37 >= 0)

m.c173 = Constraint(expr=   m.x38 >= 0)

m.c174 = Constraint(expr=   m.x39 >= 0)

m.c175 = Constraint(expr=   m.x40 >= 0)

m.c176 = Constraint(expr=   m.x41 >= 0)

m.c177 = Constraint(expr=   m.x42 >= 0)

m.c178 = Constraint(expr=   m.x43 >= 0)

m.c179 = Constraint(expr=   m.x44 >= 0)

m.c180 = Constraint(expr=   m.x45 >= 0)

m.c181 = Constraint(expr=   m.x46 >= 0)

m.c182 = Constraint(expr=   m.x47 >= 0)

m.c183 = Constraint(expr=   m.x48 >= 0)

m.c184 = Constraint(expr=   m.x49 >= 0)

m.c185 = Constraint(expr=   m.x50 >= 0)

m.c186 = Constraint(expr=   m.x51 >= 0)

m.c187 = Constraint(expr=   m.x52 >= 0)

m.c188 = Constraint(expr=   m.x53 >= 0)

m.c189 = Constraint(expr=   m.x54 >= 0)

m.c190 = Constraint(expr=   m.x55 >= 0)

m.c191 = Constraint(expr=   m.x56 >= 0)

m.c192 = Constraint(expr=   m.x57 >= 0)

m.c193 = Constraint(expr=   m.x58 >= 0)

m.c194 = Constraint(expr=   m.x59 >= 0)

m.c195 = Constraint(expr=   m.x60 >= 0)

m.c196 = Constraint(expr=   m.x61 >= 0)

m.c197 = Constraint(expr=   m.x62 >= 0)

m.c198 = Constraint(expr=   m.x63 >= 0)

m.c199 = Constraint(expr=   m.x64 >= 0)

m.c200 = Constraint(expr=   m.x65 >= 0)

m.c201 = Constraint(expr=   m.x66 >= 0)

m.c202 = Constraint(expr=   m.x67 >= 0)

m.c203 = Constraint(expr=   m.x68 >= 0)

m.c204 = Constraint(expr=   m.x69 >= 0)

m.c205 = Constraint(expr=   m.x70 >= 0)

m.c206 = Constraint(expr=   m.x71 >= 0)

m.c207 = Constraint(expr=   m.x72 >= 0)

m.c208 = Constraint(expr=   m.x73 >= 0)

m.c209 = Constraint(expr=   m.x74 >= 0)

m.c210 = Constraint(expr=   m.x75 >= 0)

m.c211 = Constraint(expr=   m.x76 >= 0)

m.c212 = Constraint(expr=   m.x77 >= 0)

m.c213 = Constraint(expr=   m.x78 >= 0)

m.c214 = Constraint(expr=   m.x79 >= 0)

m.c215 = Constraint(expr=   m.x80 >= 0)

m.c216 = Constraint(expr=   m.x81 >= 0)

m.c217 = Constraint(expr=   m.x82 >= 0)

m.c218 = Constraint(expr=   m.x83 >= 0)

m.c219 = Constraint(expr=   m.x84 >= 0)

m.c220 = Constraint(expr=   m.x85 >= 0)

m.c221 = Constraint(expr=   m.x86 >= 0)

m.c222 = Constraint(expr=   m.x87 >= 0)

m.c223 = Constraint(expr=   m.x88 >= 0)

m.c224 = Constraint(expr=   m.b149 <= 1.2)

m.c225 = Constraint(expr=   m.b150 <= 1.2)

m.c226 = Constraint(expr=   m.b151 <= 1.2)

m.c227 = Constraint(expr=   m.b161 <= 0.9)

m.c228 = Constraint(expr=   m.b162 <= 0.9)

m.c229 = Constraint(expr=   m.b163 <= 0.9)

m.c230 = Constraint(expr=   m.b149 <= 0.7)

m.c231 = Constraint(expr=   m.b150 <= 0.7)

m.c232 = Constraint(expr=   m.b151 <= 0.7)

m.c233 = Constraint(expr=   m.b161 <= 1.5)

m.c234 = Constraint(expr=   m.b162 <= 1.5)

m.c235 = Constraint(expr=   m.b163 <= 1.5)

m.c236 = Constraint(expr= - m.b149 >= -1.5)

m.c237 = Constraint(expr= - m.b150 >= -1.5)

m.c238 = Constraint(expr= - m.b151 >= -1.5)

m.c239 = Constraint(expr= - m.b161 >= -1.8)

m.c240 = Constraint(expr= - m.b162 >= -1.8)

m.c241 = Constraint(expr= - m.b163 >= -1.8)

m.c242 = Constraint(expr= - m.b149 >= -1.6)

m.c243 = Constraint(expr= - m.b150 >= -1.6)

m.c244 = Constraint(expr= - m.b151 >= -1.6)

m.c245 = Constraint(expr= - m.b161 >= -0.8)

m.c246 = Constraint(expr= - m.b162 >= -0.8)

m.c247 = Constraint(expr= - m.b163 >= -0.8)

m.c248 = Constraint(expr= - m.x89 + m.b174 <= 0.9)

m.c249 = Constraint(expr= - m.x90 + m.b175 <= 0.9)

m.c250 = Constraint(expr= - m.x89 + m.b177 <= 0.8)

m.c251 = Constraint(expr= - m.x90 + m.b178 <= 0.8)

m.c252 = Constraint(expr= - m.x92 + m.b189 <= 0.9)

m.c253 = Constraint(expr= - m.x93 + m.b190 <= 0.9)

m.c254 = Constraint(expr= - m.x92 + m.b192 <= 0.8)

m.c255 = Constraint(expr= - m.x93 + m.b193 <= 0.8)

m.c256 = Constraint(expr= - m.x95 + m.b204 <= 0.9)

m.c257 = Constraint(expr= - m.x96 + m.b205 <= 0.9)

m.c258 = Constraint(expr= - m.x95 + m.b207 <= 0.8)

m.c259 = Constraint(expr= - m.x96 + m.b208 <= 0.8)

m.c260 = Constraint(expr= - m.x98 + m.b219 <= 0.9)

m.c261 = Constraint(expr= - m.x99 + m.b220 <= 0.9)

m.c262 = Constraint(expr= - m.x98 + m.b222 <= 0.8)

m.c263 = Constraint(expr= - m.x99 + m.b223 <= 0.8)

m.c264 = Constraint(expr= - m.x101 + m.b174 <= 0.8)

m.c265 = Constraint(expr= - m.x102 + m.b175 <= 0.8)

m.c266 = Constraint(expr= - m.x101 + m.b177 <= 0.6)

m.c267 = Constraint(expr= - m.x102 + m.b178 <= 0.6)

m.c268 = Constraint(expr= - m.x104 + m.b189 <= 0.8)

m.c269 = Constraint(expr= - m.x105 + m.b190 <= 0.8)

m.c270 = Constraint(expr= - m.x104 + m.b192 <= 0.6)

m.c271 = Constraint(expr= - m.x105 + m.b193 <= 0.6)

m.c272 = Constraint(expr= - m.x107 + m.b204 <= 0.8)

m.c273 = Constraint(expr= - m.x108 + m.b205 <= 0.8)

m.c274 = Constraint(expr= - m.x107 + m.b207 <= 0.6)

m.c275 = Constraint(expr= - m.x108 + m.b208 <= 0.6)

m.c276 = Constraint(expr= - m.x110 + m.b219 <= 0.8)

m.c277 = Constraint(expr= - m.x111 + m.b220 <= 0.8)

m.c278 = Constraint(expr= - m.x110 + m.b222 <= 0.6)

m.c279 = Constraint(expr= - m.x111 + m.b223 <= 0.6)

m.c280 = Constraint(expr= - m.x89 - m.b174 >= -1.4)

m.c281 = Constraint(expr= - m.x90 - m.b175 >= -1.4)

m.c282 = Constraint(expr= - m.x89 - m.b177 >= -1.9)

m.c283 = Constraint(expr= - m.x90 - m.b178 >= -1.9)

m.c284 = Constraint(expr= - m.x92 - m.b189 >= -1.4)

m.c285 = Constraint(expr= - m.x93 - m.b190 >= -1.4)

m.c286 = Constraint(expr= - m.x92 - m.b192 >= -1.9)

m.c287 = Constraint(expr= - m.x93 - m.b193 >= -1.9)

m.c288 = Constraint(expr= - m.x95 - m.b204 >= -1.4)

m.c289 = Constraint(expr= - m.x96 - m.b205 >= -1.4)

m.c290 = Constraint(expr= - m.x95 - m.b207 >= -1.9)

m.c291 = Constraint(expr= - m.x96 - m.b208 >= -1.9)

m.c292 = Constraint(expr= - m.x98 - m.b219 >= -1.4)

m.c293 = Constraint(expr= - m.x99 - m.b220 >= -1.4)

m.c294 = Constraint(expr= - m.x98 - m.b222 >= -1.9)

m.c295 = Constraint(expr= - m.x99 - m.b223 >= -1.9)

m.c296 = Constraint(expr= - m.x101 - m.b174 >= -2)

m.c297 = Constraint(expr= - m.x102 - m.b175 >= -2)

m.c298 = Constraint(expr= - m.x101 - m.b177 >= -1.7)

m.c299 = Constraint(expr= - m.x102 - m.b178 >= -1.7)

m.c300 = Constraint(expr= - m.x104 - m.b189 >= -2)

m.c301 = Constraint(expr= - m.x105 - m.b190 >= -2)

m.c302 = Constraint(expr= - m.x104 - m.b192 >= -1.7)

m.c303 = Constraint(expr= - m.x105 - m.b193 >= -1.7)

m.c304 = Constraint(expr= - m.x107 - m.b204 >= -2)

m.c305 = Constraint(expr= - m.x108 - m.b205 >= -2)

m.c306 = Constraint(expr= - m.x107 - m.b207 >= -1.7)

m.c307 = Constraint(expr= - m.x108 - m.b208 >= -1.7)

m.c308 = Constraint(expr= - m.x110 - m.b219 >= -2)

m.c309 = Constraint(expr= - m.x111 - m.b220 >= -2)

m.c310 = Constraint(expr= - m.x110 - m.b222 >= -1.7)

m.c311 = Constraint(expr= - m.x111 - m.b223 >= -1.7)

m.c312 = Constraint(expr=   m.b173 <= 1.4)

m.c313 = Constraint(expr=   m.b176 <= 1.3)

m.c314 = Constraint(expr=   m.b188 <= 1.8)

m.c315 = Constraint(expr=   m.b191 <= 1.7)

m.c316 = Constraint(expr=   m.b203 <= 1)

m.c317 = Constraint(expr=   m.b206 <= 0.9)

m.c318 = Constraint(expr=   m.b218 <= 1.3)

m.c319 = Constraint(expr=   m.b221 <= 1.2)

m.c320 = Constraint(expr=   m.b173 <= 1.1)

m.c321 = Constraint(expr=   m.b176 <= 0.9)

m.c322 = Constraint(expr=   m.b188 <= 1.2)

m.c323 = Constraint(expr=   m.b191 <= 1)

m.c324 = Constraint(expr=   m.b203 <= 1.6)

m.c325 = Constraint(expr=   m.b206 <= 1.4)

m.c326 = Constraint(expr=   m.b218 <= 1)

m.c327 = Constraint(expr=   m.b221 <= 0.8)

m.c328 = Constraint(expr= - m.b173 >= -0.9)

m.c329 = Constraint(expr= - m.b176 >= -1.4)

m.c330 = Constraint(expr= - m.b188 >= -0.5)

m.c331 = Constraint(expr= - m.b191 >= -1)

m.c332 = Constraint(expr= - m.b203 >= -1.3)

m.c333 = Constraint(expr= - m.b206 >= -1.8)

m.c334 = Constraint(expr= - m.b218 >= -1)

m.c335 = Constraint(expr= - m.b221 >= -1.5)

m.c336 = Constraint(expr= - m.b173 >= -1.7)

m.c337 = Constraint(expr= - m.b176 >= -1.4)

m.c338 = Constraint(expr= - m.b188 >= -1.6)

m.c339 = Constraint(expr= - m.b191 >= -1.3)

m.c340 = Constraint(expr= - m.b203 >= -1.2)

m.c341 = Constraint(expr= - m.b206 >= -0.9)

m.c342 = Constraint(expr= - m.b218 >= -1.8)

m.c343 = Constraint(expr= - m.b221 >= -1.5)

m.c344 = Constraint(expr=   m.b137 + m.b164 <= 1)

m.c345 = Constraint(expr=   m.b138 + m.b165 <= 1)

m.c346 = Constraint(expr=   m.b139 + m.b166 <= 1)

m.c347 = Constraint(expr=   m.b137 + m.b167 <= 1)

m.c348 = Constraint(expr=   m.b138 + m.b168 <= 1)

m.c349 = Constraint(expr=   m.b139 + m.b169 <= 1)

m.c350 = Constraint(expr=   m.b137 + m.b170 <= 1)

m.c351 = Constraint(expr=   m.b138 + m.b171 <= 1)

m.c352 = Constraint(expr=   m.b139 + m.b172 <= 1)

m.c353 = Constraint(expr=   m.b137 + m.b173 <= 1)

m.c354 = Constraint(expr=   m.b138 + m.b174 <= 1)

m.c355 = Constraint(expr=   m.b139 + m.b175 <= 1)

m.c356 = Constraint(expr=   m.b137 + m.b176 <= 1)

m.c357 = Constraint(expr=   m.b138 + m.b177 <= 1)

m.c358 = Constraint(expr=   m.b139 + m.b178 <= 1)

m.c359 = Constraint(expr=   m.b164 + m.b179 <= 1)

m.c360 = Constraint(expr=   m.b165 + m.b180 <= 1)

m.c361 = Constraint(expr=   m.b166 + m.b181 <= 1)

m.c362 = Constraint(expr=   m.b167 + m.b179 <= 1)

m.c363 = Constraint(expr=   m.b168 + m.b180 <= 1)

m.c364 = Constraint(expr=   m.b169 + m.b181 <= 1)

m.c365 = Constraint(expr=   m.b170 + m.b179 <= 1)

m.c366 = Constraint(expr=   m.b171 + m.b180 <= 1)

m.c367 = Constraint(expr=   m.b172 + m.b181 <= 1)

m.c368 = Constraint(expr=   m.b173 + m.b179 <= 1)

m.c369 = Constraint(expr=   m.b174 + m.b180 <= 1)

m.c370 = Constraint(expr=   m.b175 + m.b181 <= 1)

m.c371 = Constraint(expr=   m.b176 + m.b179 <= 1)

m.c372 = Constraint(expr=   m.b177 + m.b180 <= 1)

m.c373 = Constraint(expr=   m.b178 + m.b181 <= 1)

m.c374 = Constraint(expr=   m.b164 + m.b194 <= 1)

m.c375 = Constraint(expr=   m.b165 + m.b195 <= 1)

m.c376 = Constraint(expr=   m.b166 + m.b196 <= 1)

m.c377 = Constraint(expr=   m.b167 + m.b194 <= 1)

m.c378 = Constraint(expr=   m.b168 + m.b195 <= 1)

m.c379 = Constraint(expr=   m.b169 + m.b196 <= 1)

m.c380 = Constraint(expr=   m.b170 + m.b194 <= 1)

m.c381 = Constraint(expr=   m.b171 + m.b195 <= 1)

m.c382 = Constraint(expr=   m.b172 + m.b196 <= 1)

m.c383 = Constraint(expr=   m.b173 + m.b194 <= 1)

m.c384 = Constraint(expr=   m.b174 + m.b195 <= 1)

m.c385 = Constraint(expr=   m.b175 + m.b196 <= 1)

m.c386 = Constraint(expr=   m.b176 + m.b194 <= 1)

m.c387 = Constraint(expr=   m.b177 + m.b195 <= 1)

m.c388 = Constraint(expr=   m.b178 + m.b196 <= 1)

m.c389 = Constraint(expr=   m.b164 + m.b209 <= 1)

m.c390 = Constraint(expr=   m.b165 + m.b210 <= 1)

m.c391 = Constraint(expr=   m.b166 + m.b211 <= 1)

m.c392 = Constraint(expr=   m.b167 + m.b209 <= 1)

m.c393 = Constraint(expr=   m.b168 + m.b210 <= 1)

m.c394 = Constraint(expr=   m.b169 + m.b211 <= 1)

m.c395 = Constraint(expr=   m.b170 + m.b209 <= 1)

m.c396 = Constraint(expr=   m.b171 + m.b210 <= 1)

m.c397 = Constraint(expr=   m.b172 + m.b211 <= 1)

m.c398 = Constraint(expr=   m.b173 + m.b209 <= 1)

m.c399 = Constraint(expr=   m.b174 + m.b210 <= 1)

m.c400 = Constraint(expr=   m.b175 + m.b211 <= 1)

m.c401 = Constraint(expr=   m.b176 + m.b209 <= 1)

m.c402 = Constraint(expr=   m.b177 + m.b210 <= 1)

m.c403 = Constraint(expr=   m.b178 + m.b211 <= 1)

m.c404 = Constraint(expr=   m.b140 + m.b179 <= 1)

m.c405 = Constraint(expr=   m.b141 + m.b180 <= 1)

m.c406 = Constraint(expr=   m.b142 + m.b181 <= 1)

m.c407 = Constraint(expr=   m.b140 + m.b182 <= 1)

m.c408 = Constraint(expr=   m.b141 + m.b183 <= 1)

m.c409 = Constraint(expr=   m.b142 + m.b184 <= 1)

m.c410 = Constraint(expr=   m.b140 + m.b185 <= 1)

m.c411 = Constraint(expr=   m.b141 + m.b186 <= 1)

m.c412 = Constraint(expr=   m.b142 + m.b187 <= 1)

m.c413 = Constraint(expr=   m.b140 + m.b188 <= 1)

m.c414 = Constraint(expr=   m.b141 + m.b189 <= 1)

m.c415 = Constraint(expr=   m.b142 + m.b190 <= 1)

m.c416 = Constraint(expr=   m.b140 + m.b191 <= 1)

m.c417 = Constraint(expr=   m.b141 + m.b192 <= 1)

m.c418 = Constraint(expr=   m.b142 + m.b193 <= 1)

m.c419 = Constraint(expr=   m.b152 + m.b179 <= 1)

m.c420 = Constraint(expr=   m.b153 + m.b180 <= 1)

m.c421 = Constraint(expr=   m.b154 + m.b181 <= 1)

m.c422 = Constraint(expr=   m.b152 + m.b182 <= 1)

m.c423 = Constraint(expr=   m.b153 + m.b183 <= 1)

m.c424 = Constraint(expr=   m.b154 + m.b184 <= 1)

m.c425 = Constraint(expr=   m.b152 + m.b185 <= 1)

m.c426 = Constraint(expr=   m.b153 + m.b186 <= 1)

m.c427 = Constraint(expr=   m.b154 + m.b187 <= 1)

m.c428 = Constraint(expr=   m.b152 + m.b188 <= 1)

m.c429 = Constraint(expr=   m.b153 + m.b189 <= 1)

m.c430 = Constraint(expr=   m.b154 + m.b190 <= 1)

m.c431 = Constraint(expr=   m.b152 + m.b191 <= 1)

m.c432 = Constraint(expr=   m.b153 + m.b192 <= 1)

m.c433 = Constraint(expr=   m.b154 + m.b193 <= 1)

m.c434 = Constraint(expr=   m.b164 + m.b179 <= 1)

m.c435 = Constraint(expr=   m.b165 + m.b180 <= 1)

m.c436 = Constraint(expr=   m.b166 + m.b181 <= 1)

m.c437 = Constraint(expr=   m.b164 + m.b182 <= 1)

m.c438 = Constraint(expr=   m.b165 + m.b183 <= 1)

m.c439 = Constraint(expr=   m.b166 + m.b184 <= 1)

m.c440 = Constraint(expr=   m.b164 + m.b185 <= 1)

m.c441 = Constraint(expr=   m.b165 + m.b186 <= 1)

m.c442 = Constraint(expr=   m.b166 + m.b187 <= 1)

m.c443 = Constraint(expr=   m.b164 + m.b188 <= 1)

m.c444 = Constraint(expr=   m.b165 + m.b189 <= 1)

m.c445 = Constraint(expr=   m.b166 + m.b190 <= 1)

m.c446 = Constraint(expr=   m.b164 + m.b191 <= 1)

m.c447 = Constraint(expr=   m.b165 + m.b192 <= 1)

m.c448 = Constraint(expr=   m.b166 + m.b193 <= 1)

m.c449 = Constraint(expr=   m.b179 + m.b197 <= 1)

m.c450 = Constraint(expr=   m.b180 + m.b198 <= 1)

m.c451 = Constraint(expr=   m.b181 + m.b199 <= 1)

m.c452 = Constraint(expr=   m.b182 + m.b197 <= 1)

m.c453 = Constraint(expr=   m.b183 + m.b198 <= 1)

m.c454 = Constraint(expr=   m.b184 + m.b199 <= 1)

m.c455 = Constraint(expr=   m.b185 + m.b197 <= 1)

m.c456 = Constraint(expr=   m.b186 + m.b198 <= 1)

m.c457 = Constraint(expr=   m.b187 + m.b199 <= 1)

m.c458 = Constraint(expr=   m.b188 + m.b197 <= 1)

m.c459 = Constraint(expr=   m.b189 + m.b198 <= 1)

m.c460 = Constraint(expr=   m.b190 + m.b199 <= 1)

m.c461 = Constraint(expr=   m.b191 + m.b197 <= 1)

m.c462 = Constraint(expr=   m.b192 + m.b198 <= 1)

m.c463 = Constraint(expr=   m.b193 + m.b199 <= 1)

m.c464 = Constraint(expr=   m.b179 + m.b212 <= 1)

m.c465 = Constraint(expr=   m.b180 + m.b213 <= 1)

m.c466 = Constraint(expr=   m.b181 + m.b214 <= 1)

m.c467 = Constraint(expr=   m.b182 + m.b212 <= 1)

m.c468 = Constraint(expr=   m.b183 + m.b213 <= 1)

m.c469 = Constraint(expr=   m.b184 + m.b214 <= 1)

m.c470 = Constraint(expr=   m.b185 + m.b212 <= 1)

m.c471 = Constraint(expr=   m.b186 + m.b213 <= 1)

m.c472 = Constraint(expr=   m.b187 + m.b214 <= 1)

m.c473 = Constraint(expr=   m.b188 + m.b212 <= 1)

m.c474 = Constraint(expr=   m.b189 + m.b213 <= 1)

m.c475 = Constraint(expr=   m.b190 + m.b214 <= 1)

m.c476 = Constraint(expr=   m.b191 + m.b212 <= 1)

m.c477 = Constraint(expr=   m.b192 + m.b213 <= 1)

m.c478 = Constraint(expr=   m.b193 + m.b214 <= 1)

m.c479 = Constraint(expr=   m.b143 + m.b194 <= 1)

m.c480 = Constraint(expr=   m.b144 + m.b195 <= 1)

m.c481 = Constraint(expr=   m.b145 + m.b196 <= 1)

m.c482 = Constraint(expr=   m.b143 + m.b197 <= 1)

m.c483 = Constraint(expr=   m.b144 + m.b198 <= 1)

m.c484 = Constraint(expr=   m.b145 + m.b199 <= 1)

m.c485 = Constraint(expr=   m.b143 + m.b200 <= 1)

m.c486 = Constraint(expr=   m.b144 + m.b201 <= 1)

m.c487 = Constraint(expr=   m.b145 + m.b202 <= 1)

m.c488 = Constraint(expr=   m.b143 + m.b203 <= 1)

m.c489 = Constraint(expr=   m.b144 + m.b204 <= 1)

m.c490 = Constraint(expr=   m.b145 + m.b205 <= 1)

m.c491 = Constraint(expr=   m.b143 + m.b206 <= 1)

m.c492 = Constraint(expr=   m.b144 + m.b207 <= 1)

m.c493 = Constraint(expr=   m.b145 + m.b208 <= 1)

m.c494 = Constraint(expr=   m.b155 + m.b194 <= 1)

m.c495 = Constraint(expr=   m.b156 + m.b195 <= 1)

m.c496 = Constraint(expr=   m.b157 + m.b196 <= 1)

m.c497 = Constraint(expr=   m.b155 + m.b197 <= 1)

m.c498 = Constraint(expr=   m.b156 + m.b198 <= 1)

m.c499 = Constraint(expr=   m.b157 + m.b199 <= 1)

m.c500 = Constraint(expr=   m.b155 + m.b200 <= 1)

m.c501 = Constraint(expr=   m.b156 + m.b201 <= 1)

m.c502 = Constraint(expr=   m.b157 + m.b202 <= 1)

m.c503 = Constraint(expr=   m.b155 + m.b203 <= 1)

m.c504 = Constraint(expr=   m.b156 + m.b204 <= 1)

m.c505 = Constraint(expr=   m.b157 + m.b205 <= 1)

m.c506 = Constraint(expr=   m.b155 + m.b206 <= 1)

m.c507 = Constraint(expr=   m.b156 + m.b207 <= 1)

m.c508 = Constraint(expr=   m.b157 + m.b208 <= 1)

m.c509 = Constraint(expr=   m.b167 + m.b194 <= 1)

m.c510 = Constraint(expr=   m.b168 + m.b195 <= 1)

m.c511 = Constraint(expr=   m.b169 + m.b196 <= 1)

m.c512 = Constraint(expr=   m.b167 + m.b197 <= 1)

m.c513 = Constraint(expr=   m.b168 + m.b198 <= 1)

m.c514 = Constraint(expr=   m.b169 + m.b199 <= 1)

m.c515 = Constraint(expr=   m.b167 + m.b200 <= 1)

m.c516 = Constraint(expr=   m.b168 + m.b201 <= 1)

m.c517 = Constraint(expr=   m.b169 + m.b202 <= 1)

m.c518 = Constraint(expr=   m.b167 + m.b203 <= 1)

m.c519 = Constraint(expr=   m.b168 + m.b204 <= 1)

m.c520 = Constraint(expr=   m.b169 + m.b205 <= 1)

m.c521 = Constraint(expr=   m.b167 + m.b206 <= 1)

m.c522 = Constraint(expr=   m.b168 + m.b207 <= 1)

m.c523 = Constraint(expr=   m.b169 + m.b208 <= 1)

m.c524 = Constraint(expr=   m.b182 + m.b194 <= 1)

m.c525 = Constraint(expr=   m.b183 + m.b195 <= 1)

m.c526 = Constraint(expr=   m.b184 + m.b196 <= 1)

m.c527 = Constraint(expr=   m.b182 + m.b197 <= 1)

m.c528 = Constraint(expr=   m.b183 + m.b198 <= 1)

m.c529 = Constraint(expr=   m.b184 + m.b199 <= 1)

m.c530 = Constraint(expr=   m.b182 + m.b200 <= 1)

m.c531 = Constraint(expr=   m.b183 + m.b201 <= 1)

m.c532 = Constraint(expr=   m.b184 + m.b202 <= 1)

m.c533 = Constraint(expr=   m.b182 + m.b203 <= 1)

m.c534 = Constraint(expr=   m.b183 + m.b204 <= 1)

m.c535 = Constraint(expr=   m.b184 + m.b205 <= 1)

m.c536 = Constraint(expr=   m.b182 + m.b206 <= 1)

m.c537 = Constraint(expr=   m.b183 + m.b207 <= 1)

m.c538 = Constraint(expr=   m.b184 + m.b208 <= 1)

m.c539 = Constraint(expr=   m.b194 + m.b215 <= 1)

m.c540 = Constraint(expr=   m.b195 + m.b216 <= 1)

m.c541 = Constraint(expr=   m.b196 + m.b217 <= 1)

m.c542 = Constraint(expr=   m.b197 + m.b215 <= 1)

m.c543 = Constraint(expr=   m.b198 + m.b216 <= 1)

m.c544 = Constraint(expr=   m.b199 + m.b217 <= 1)

m.c545 = Constraint(expr=   m.b200 + m.b215 <= 1)

m.c546 = Constraint(expr=   m.b201 + m.b216 <= 1)

m.c547 = Constraint(expr=   m.b202 + m.b217 <= 1)

m.c548 = Constraint(expr=   m.b203 + m.b215 <= 1)

m.c549 = Constraint(expr=   m.b204 + m.b216 <= 1)

m.c550 = Constraint(expr=   m.b205 + m.b217 <= 1)

m.c551 = Constraint(expr=   m.b206 + m.b215 <= 1)

m.c552 = Constraint(expr=   m.b207 + m.b216 <= 1)

m.c553 = Constraint(expr=   m.b208 + m.b217 <= 1)

m.c554 = Constraint(expr=   m.b146 + m.b209 <= 1)

m.c555 = Constraint(expr=   m.b147 + m.b210 <= 1)

m.c556 = Constraint(expr=   m.b148 + m.b211 <= 1)

m.c557 = Constraint(expr=   m.b146 + m.b212 <= 1)

m.c558 = Constraint(expr=   m.b147 + m.b213 <= 1)

m.c559 = Constraint(expr=   m.b148 + m.b214 <= 1)

m.c560 = Constraint(expr=   m.b146 + m.b215 <= 1)

m.c561 = Constraint(expr=   m.b147 + m.b216 <= 1)

m.c562 = Constraint(expr=   m.b148 + m.b217 <= 1)

m.c563 = Constraint(expr=   m.b146 + m.b218 <= 1)

m.c564 = Constraint(expr=   m.b147 + m.b219 <= 1)

m.c565 = Constraint(expr=   m.b148 + m.b220 <= 1)

m.c566 = Constraint(expr=   m.b146 + m.b221 <= 1)

m.c567 = Constraint(expr=   m.b147 + m.b222 <= 1)

m.c568 = Constraint(expr=   m.b148 + m.b223 <= 1)

m.c569 = Constraint(expr=   m.b158 + m.b209 <= 1)

m.c570 = Constraint(expr=   m.b159 + m.b210 <= 1)

m.c571 = Constraint(expr=   m.b160 + m.b211 <= 1)

m.c572 = Constraint(expr=   m.b158 + m.b212 <= 1)

m.c573 = Constraint(expr=   m.b159 + m.b213 <= 1)

m.c574 = Constraint(expr=   m.b160 + m.b214 <= 1)

m.c575 = Constraint(expr=   m.b158 + m.b215 <= 1)

m.c576 = Constraint(expr=   m.b159 + m.b216 <= 1)

m.c577 = Constraint(expr=   m.b160 + m.b217 <= 1)

m.c578 = Constraint(expr=   m.b158 + m.b218 <= 1)

m.c579 = Constraint(expr=   m.b159 + m.b219 <= 1)

m.c580 = Constraint(expr=   m.b160 + m.b220 <= 1)

m.c581 = Constraint(expr=   m.b158 + m.b221 <= 1)

m.c582 = Constraint(expr=   m.b159 + m.b222 <= 1)

m.c583 = Constraint(expr=   m.b160 + m.b223 <= 1)

m.c584 = Constraint(expr=   m.b170 + m.b209 <= 1)

m.c585 = Constraint(expr=   m.b171 + m.b210 <= 1)

m.c586 = Constraint(expr=   m.b172 + m.b211 <= 1)

m.c587 = Constraint(expr=   m.b170 + m.b212 <= 1)

m.c588 = Constraint(expr=   m.b171 + m.b213 <= 1)

m.c589 = Constraint(expr=   m.b172 + m.b214 <= 1)

m.c590 = Constraint(expr=   m.b170 + m.b215 <= 1)

m.c591 = Constraint(expr=   m.b171 + m.b216 <= 1)

m.c592 = Constraint(expr=   m.b172 + m.b217 <= 1)

m.c593 = Constraint(expr=   m.b170 + m.b218 <= 1)

m.c594 = Constraint(expr=   m.b171 + m.b219 <= 1)

m.c595 = Constraint(expr=   m.b172 + m.b220 <= 1)

m.c596 = Constraint(expr=   m.b170 + m.b221 <= 1)

m.c597 = Constraint(expr=   m.b171 + m.b222 <= 1)

m.c598 = Constraint(expr=   m.b172 + m.b223 <= 1)

m.c599 = Constraint(expr=   m.b185 + m.b209 <= 1)

m.c600 = Constraint(expr=   m.b186 + m.b210 <= 1)

m.c601 = Constraint(expr=   m.b187 + m.b211 <= 1)

m.c602 = Constraint(expr=   m.b185 + m.b212 <= 1)

m.c603 = Constraint(expr=   m.b186 + m.b213 <= 1)

m.c604 = Constraint(expr=   m.b187 + m.b214 <= 1)

m.c605 = Constraint(expr=   m.b185 + m.b215 <= 1)

m.c606 = Constraint(expr=   m.b186 + m.b216 <= 1)

m.c607 = Constraint(expr=   m.b187 + m.b217 <= 1)

m.c608 = Constraint(expr=   m.b185 + m.b218 <= 1)

m.c609 = Constraint(expr=   m.b186 + m.b219 <= 1)

m.c610 = Constraint(expr=   m.b187 + m.b220 <= 1)

m.c611 = Constraint(expr=   m.b185 + m.b221 <= 1)

m.c612 = Constraint(expr=   m.b186 + m.b222 <= 1)

m.c613 = Constraint(expr=   m.b187 + m.b223 <= 1)

m.c614 = Constraint(expr=   m.b200 + m.b209 <= 1)

m.c615 = Constraint(expr=   m.b201 + m.b210 <= 1)

m.c616 = Constraint(expr=   m.b202 + m.b211 <= 1)

m.c617 = Constraint(expr=   m.b200 + m.b212 <= 1)

m.c618 = Constraint(expr=   m.b201 + m.b213 <= 1)

m.c619 = Constraint(expr=   m.b202 + m.b214 <= 1)

m.c620 = Constraint(expr=   m.b200 + m.b215 <= 1)

m.c621 = Constraint(expr=   m.b201 + m.b216 <= 1)

m.c622 = Constraint(expr=   m.b202 + m.b217 <= 1)

m.c623 = Constraint(expr=   m.b200 + m.b218 <= 1)

m.c624 = Constraint(expr=   m.b201 + m.b219 <= 1)

m.c625 = Constraint(expr=   m.b202 + m.b220 <= 1)

m.c626 = Constraint(expr=   m.b200 + m.b221 <= 1)

m.c627 = Constraint(expr=   m.b201 + m.b222 <= 1)

m.c628 = Constraint(expr=   m.b202 + m.b223 <= 1)
