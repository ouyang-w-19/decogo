#  MINLP written by GAMS Convert at 04/21/18 13:52:28
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         49       40        3        6        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        268      154        3      111        0        0        0        0
#  FX     23        0        0       23        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        507      171      336        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x3 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x4 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x5 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x6 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x7 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x8 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x9 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x10 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x11 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x12 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x13 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x14 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x15 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x16 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x17 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x18 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x19 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x20 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x21 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x22 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x23 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x24 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x25 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x26 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x27 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x28 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x29 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x30 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x31 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x32 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x33 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x34 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x35 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x36 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x37 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x38 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x39 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x40 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x41 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x42 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x43 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x44 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x45 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x46 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x47 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x48 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x49 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x50 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x51 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x52 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x53 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x54 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x55 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x56 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x57 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x58 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x59 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x60 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x61 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x62 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x63 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x64 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x65 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x66 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x67 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x68 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x69 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x70 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x71 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x72 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x73 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x74 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x75 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x76 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x77 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x78 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x79 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x80 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x81 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x82 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x83 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x84 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x85 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x86 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x87 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x88 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x89 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x90 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x91 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x92 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x93 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x94 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x95 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x96 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x97 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x98 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x99 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x100 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x101 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x102 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x103 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x104 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x105 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x106 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x107 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x108 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x109 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x110 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x111 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x112 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x113 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x114 = Var(within=Reals,bounds=(0.4,1),initialize=0.4)
m.x115 = Var(within=Reals,bounds=(20,None),initialize=99)
m.x116 = Var(within=Reals,bounds=(52.5,None),initialize=99)
m.x117 = Var(within=Reals,bounds=(151.25,None),initialize=151.25)
m.x118 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x119 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x120 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x121 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x122 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x123 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x124 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x125 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x126 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x127 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x128 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x129 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x130 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x131 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x132 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x133 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x134 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x135 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x136 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x137 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x138 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x139 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x140 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x141 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x142 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x143 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x144 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x145 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x146 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x147 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x148 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x149 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x150 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x151 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x152 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x153 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x154 = Var(within=Reals,bounds=(0,1),initialize=0)
m.b155 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b156 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b157 = Var(within=Binary,bounds=(0,1),initialize=0)
m.i158 = Var(within=Integers,bounds=(0,28),initialize=0)
m.i159 = Var(within=Integers,bounds=(0,28),initialize=0)
m.i160 = Var(within=Integers,bounds=(0,28),initialize=0)
m.i161 = Var(within=Integers,bounds=(0,28),initialize=0)
m.i162 = Var(within=Integers,bounds=(0,28),initialize=0)
m.i163 = Var(within=Integers,bounds=(0,28),initialize=0)
m.i164 = Var(within=Integers,bounds=(0,28),initialize=0)
m.i165 = Var(within=Integers,bounds=(0,28),initialize=0)
m.i166 = Var(within=Integers,bounds=(0,27),initialize=0)
m.i167 = Var(within=Integers,bounds=(0,27),initialize=0)
m.i168 = Var(within=Integers,bounds=(0,2),initialize=0)
m.i169 = Var(within=Integers,bounds=(0,27),initialize=0)
m.i170 = Var(within=Integers,bounds=(0,22),initialize=0)
m.i171 = Var(within=Integers,bounds=(0,22),initialize=0)
m.i172 = Var(within=Integers,bounds=(0,22),initialize=0)
m.i173 = Var(within=Integers,bounds=(0,17),initialize=0)
m.i174 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i175 = Var(within=Integers,bounds=(0,7),initialize=0)
m.i176 = Var(within=Integers,bounds=(0,2),initialize=0)
m.i177 = Var(within=Integers,bounds=(0,2),initialize=0)
m.i178 = Var(within=Integers,bounds=(0,2),initialize=0)
m.i179 = Var(within=Integers,bounds=(0,28),initialize=0)
m.i180 = Var(within=Integers,bounds=(0,28),initialize=0)
m.i181 = Var(within=Integers,bounds=(0,17),initialize=0)
m.i182 = Var(within=Integers,bounds=(0,17),initialize=0)
m.i183 = Var(within=Integers,bounds=(0,10),initialize=0)
m.i184 = Var(within=Integers,bounds=(0,10),initialize=0)
m.i185 = Var(within=Integers,bounds=(0,10),initialize=0)
m.i186 = Var(within=Integers,bounds=(0,7),initialize=0)
m.i187 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i188 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i189 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i190 = Var(within=Integers,bounds=(0,2),initialize=0)
m.i191 = Var(within=Integers,bounds=(0,2),initialize=0)
m.i192 = Var(within=Integers,bounds=(0,2),initialize=0)
m.i193 = Var(within=Integers,bounds=(0,2),initialize=0)
m.i194 = Var(within=Integers,bounds=(0,2),initialize=0)
m.i195 = Var(within=Integers,bounds=(0,28),initialize=0)
m.i196 = Var(within=Integers,bounds=(0,28),initialize=0)
m.i197 = Var(within=Integers,bounds=(0,28),initialize=0)
m.i198 = Var(within=Integers,bounds=(0,28),initialize=0)
m.i199 = Var(within=Integers,bounds=(0,28),initialize=0)
m.i200 = Var(within=Integers,bounds=(0,28),initialize=0)
m.i201 = Var(within=Integers,bounds=(0,28),initialize=0)
m.i202 = Var(within=Integers,bounds=(0,13),initialize=0)
m.i203 = Var(within=Integers,bounds=(0,10),initialize=0)
m.i204 = Var(within=Integers,bounds=(0,10),initialize=0)
m.i205 = Var(within=Integers,bounds=(0,0),initialize=0)
m.i206 = Var(within=Integers,bounds=(0,10),initialize=0)
m.i207 = Var(within=Integers,bounds=(0,8),initialize=0)
m.i208 = Var(within=Integers,bounds=(0,8),initialize=0)
m.i209 = Var(within=Integers,bounds=(0,8),initialize=0)
m.i210 = Var(within=Integers,bounds=(0,6),initialize=0)
m.i211 = Var(within=Integers,bounds=(0,4),initialize=0)
m.i212 = Var(within=Integers,bounds=(0,2),initialize=0)
m.i213 = Var(within=Integers,bounds=(0,0),initialize=0)
m.i214 = Var(within=Integers,bounds=(0,0),initialize=0)
m.i215 = Var(within=Integers,bounds=(0,0),initialize=0)
m.i216 = Var(within=Integers,bounds=(0,18),initialize=0)
m.i217 = Var(within=Integers,bounds=(0,17),initialize=0)
m.i218 = Var(within=Integers,bounds=(0,6),initialize=0)
m.i219 = Var(within=Integers,bounds=(0,6),initialize=0)
m.i220 = Var(within=Integers,bounds=(0,3),initialize=0)
m.i221 = Var(within=Integers,bounds=(0,3),initialize=0)
m.i222 = Var(within=Integers,bounds=(0,3),initialize=0)
m.i223 = Var(within=Integers,bounds=(0,2),initialize=0)
m.i224 = Var(within=Integers,bounds=(0,1),initialize=0)
m.i225 = Var(within=Integers,bounds=(0,1),initialize=0)
m.i226 = Var(within=Integers,bounds=(0,1),initialize=0)
m.i227 = Var(within=Integers,bounds=(0,0),initialize=0)
m.i228 = Var(within=Integers,bounds=(0,0),initialize=0)
m.i229 = Var(within=Integers,bounds=(0,0),initialize=0)
m.i230 = Var(within=Integers,bounds=(0,0),initialize=0)
m.i231 = Var(within=Integers,bounds=(0,0),initialize=0)
m.i232 = Var(within=Integers,bounds=(0,28),initialize=0)
m.i233 = Var(within=Integers,bounds=(0,28),initialize=0)
m.i234 = Var(within=Integers,bounds=(0,14),initialize=0)
m.i235 = Var(within=Integers,bounds=(0,28),initialize=0)
m.i236 = Var(within=Integers,bounds=(0,18),initialize=0)
m.i237 = Var(within=Integers,bounds=(0,17),initialize=0)
m.i238 = Var(within=Integers,bounds=(0,17),initialize=0)
m.i239 = Var(within=Integers,bounds=(0,4),initialize=0)
m.i240 = Var(within=Integers,bounds=(0,3),initialize=0)
m.i241 = Var(within=Integers,bounds=(0,3),initialize=0)
m.i242 = Var(within=Integers,bounds=(0,0),initialize=0)
m.i243 = Var(within=Integers,bounds=(0,3),initialize=0)
m.i244 = Var(within=Integers,bounds=(0,2),initialize=0)
m.i245 = Var(within=Integers,bounds=(0,2),initialize=0)
m.i246 = Var(within=Integers,bounds=(0,2),initialize=0)
m.i247 = Var(within=Integers,bounds=(0,2),initialize=0)
m.i248 = Var(within=Integers,bounds=(0,1),initialize=0)
m.i249 = Var(within=Integers,bounds=(0,0),initialize=0)
m.i250 = Var(within=Integers,bounds=(0,0),initialize=0)
m.i251 = Var(within=Integers,bounds=(0,0),initialize=0)
m.i252 = Var(within=Integers,bounds=(0,0),initialize=0)
m.i253 = Var(within=Integers,bounds=(0,6),initialize=0)
m.i254 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i255 = Var(within=Integers,bounds=(0,2),initialize=0)
m.i256 = Var(within=Integers,bounds=(0,2),initialize=0)
m.i257 = Var(within=Integers,bounds=(0,1),initialize=0)
m.i258 = Var(within=Integers,bounds=(0,1),initialize=0)
m.i259 = Var(within=Integers,bounds=(0,1),initialize=0)
m.i260 = Var(within=Integers,bounds=(0,0),initialize=0)
m.i261 = Var(within=Integers,bounds=(0,0),initialize=0)
m.i262 = Var(within=Integers,bounds=(0,0),initialize=0)
m.i263 = Var(within=Integers,bounds=(0,0),initialize=0)
m.i264 = Var(within=Integers,bounds=(0,0),initialize=0)
m.i265 = Var(within=Integers,bounds=(0,0),initialize=0)
m.i266 = Var(within=Integers,bounds=(0,0),initialize=0)
m.i267 = Var(within=Integers,bounds=(0,0),initialize=0)
m.i268 = Var(within=Integers,bounds=(0,0),initialize=0)

m.obj = Objective(expr=   m.x2 + m.x3, sense=minimize)

m.c2 = Constraint(expr=   m.x3 - 2.45*m.b155 - 2.45*m.b156 - 2.45*m.b157 == 0)

m.c3 = Constraint(expr=-(0.98488578017961*m.x115**0.5 + 0.98488578017961*m.x116**0.5 + 0.98488578017961*m.x117**0.5)
                        + m.x2 == 0)

m.c4 = Constraint(expr= - 168*m.b155 + 6*m.i158 + 6*m.i159 + 6*m.i160 + 6*m.i161 + 6*m.i162 + 6*m.i163 + 6*m.i164
                        + 6*m.i165 + 6*m.i166 + 6*m.i167 + 6*m.i168 + 6*m.i169 + 6*m.i170 + 6*m.i171 + 6*m.i172
                        + 6*m.i173 + 6*m.i174 + 6*m.i175 + 6*m.i176 + 6*m.i177 + 6*m.i178 + 6*m.i179 + 6*m.i180
                        + 6*m.i181 + 6*m.i182 + 6*m.i183 + 6*m.i184 + 6*m.i185 + 6*m.i186 + 6*m.i187 + 6*m.i188
                        + 6*m.i189 + 6*m.i190 + 6*m.i191 + 6*m.i192 + 6*m.i193 + 6*m.i194 <= 0)

m.c5 = Constraint(expr= - 168*m.b156 + 6*m.i195 + 6*m.i196 + 6*m.i197 + 6*m.i198 + 6*m.i199 + 6*m.i200 + 6*m.i201
                        + 6*m.i202 + 6*m.i203 + 6*m.i204 + 6*m.i205 + 6*m.i206 + 6*m.i207 + 6*m.i208 + 6*m.i209
                        + 6*m.i210 + 6*m.i211 + 6*m.i212 + 6*m.i213 + 6*m.i214 + 6*m.i215 + 6*m.i216 + 6*m.i217
                        + 6*m.i218 + 6*m.i219 + 6*m.i220 + 6*m.i221 + 6*m.i222 + 6*m.i223 + 6*m.i224 + 6*m.i225
                        + 6*m.i226 + 6*m.i227 + 6*m.i228 + 6*m.i229 + 6*m.i230 + 6*m.i231 <= 0)

m.c6 = Constraint(expr= - 168*m.b157 + 6*m.i232 + 6*m.i233 + 6*m.i234 + 6*m.i235 + 6*m.i236 + 6*m.i237 + 6*m.i238
                        + 6*m.i239 + 6*m.i240 + 6*m.i241 + 6*m.i242 + 6*m.i243 + 6*m.i244 + 6*m.i245 + 6*m.i246
                        + 6*m.i247 + 6*m.i248 + 6*m.i249 + 6*m.i250 + 6*m.i251 + 6*m.i252 + 6*m.i253 + 6*m.i254
                        + 6*m.i255 + 6*m.i256 + 6*m.i257 + 6*m.i258 + 6*m.i259 + 6*m.i260 + 6*m.i261 + 6*m.i262
                        + 6*m.i263 + 6*m.i264 + 6*m.i265 + 6*m.i266 + 6*m.i267 + 6*m.i268 <= 0)

m.c7 = Constraint(expr=-0.000384615384615385*(m.i158*m.x4*m.x115 + m.i195*m.x41*m.x116 + m.i232*m.x78*m.x117) + m.x118
                        == -1)

m.c8 = Constraint(expr=-0.000434782608695652*(m.i159*m.x5*m.x115 + m.i196*m.x42*m.x116 + m.i233*m.x79*m.x117) + m.x119
                        == -1)

m.c9 = Constraint(expr=-0.00222222222222222*(m.i160*m.x6*m.x115 + m.i197*m.x43*m.x116 + m.i234*m.x80*m.x117) + m.x120
                        == -1)

m.c10 = Constraint(expr=-0.000833333333333333*(m.i161*m.x7*m.x115 + m.i198*m.x44*m.x116 + m.i235*m.x81*m.x117) + m.x121
                         == -1)

m.c11 = Constraint(expr=-0.00178571428571429*(m.i162*m.x8*m.x115 + m.i199*m.x45*m.x116 + m.i236*m.x82*m.x117) + m.x122
                         == -1)

m.c12 = Constraint(expr=-0.00188679245283019*(m.i163*m.x9*m.x115 + m.i200*m.x46*m.x116 + m.i237*m.x83*m.x117) + m.x123
                         == -1)

m.c13 = Constraint(expr=-0.00188679245283019*(m.i164*m.x10*m.x115 + m.i201*m.x47*m.x116 + m.i238*m.x84*m.x117) + m.x124
                         == -1)

m.c14 = Constraint(expr=-0.00714285714285714*(m.i165*m.x11*m.x115 + m.i202*m.x48*m.x116 + m.i239*m.x85*m.x117) + m.x125
                         == -1)

m.c15 = Constraint(expr=-0.00909090909090909*(m.i166*m.x12*m.x115 + m.i203*m.x49*m.x116 + m.i240*m.x86*m.x117) + m.x126
                         == -1)

m.c16 = Constraint(expr=-0.00909090909090909*(m.i167*m.x13*m.x115 + m.i204*m.x50*m.x116 + m.i241*m.x87*m.x117) + m.x127
                         == -1)

m.c17 = Constraint(expr=-0.1*(m.i168*m.x14*m.x115 + m.i205*m.x51*m.x116 + m.i242*m.x88*m.x117) + m.x128 == -1)

m.c18 = Constraint(expr=-0.00909090909090909*(m.i169*m.x15*m.x115 + m.i206*m.x52*m.x116 + m.i243*m.x89*m.x117) + m.x129
                         == -1)

m.c19 = Constraint(expr=-0.0111111111111111*(m.i170*m.x16*m.x115 + m.i207*m.x53*m.x116 + m.i244*m.x90*m.x117) + m.x130
                         == -1)

m.c20 = Constraint(expr=-0.0111111111111111*(m.i171*m.x17*m.x115 + m.i208*m.x54*m.x116 + m.i245*m.x91*m.x117) + m.x131
                         == -1)

m.c21 = Constraint(expr=-0.0111111111111111*(m.i172*m.x18*m.x115 + m.i209*m.x55*m.x116 + m.i246*m.x92*m.x117) + m.x132
                         == -1)

m.c22 = Constraint(expr=-0.0142857142857143*(m.i173*m.x19*m.x115 + m.i210*m.x56*m.x116 + m.i247*m.x93*m.x117) + m.x133
                         == -1)

m.c23 = Constraint(expr=-0.02*(m.i174*m.x20*m.x115 + m.i211*m.x57*m.x116 + m.i248*m.x94*m.x117) + m.x134 == -1)

m.c24 = Constraint(expr=-0.0333333333333333*(m.i175*m.x21*m.x115 + m.i212*m.x58*m.x116 + m.i249*m.x95*m.x117) + m.x135
                         == -1)

m.c25 = Constraint(expr=-0.1*(m.i176*m.x22*m.x115 + m.i213*m.x59*m.x116 + m.i250*m.x96*m.x117) + m.x136 == -1)

m.c26 = Constraint(expr=-0.1*(m.i177*m.x23*m.x115 + m.i214*m.x60*m.x116 + m.i251*m.x97*m.x117) + m.x137 == -1)

m.c27 = Constraint(expr=-0.1*(m.i178*m.x24*m.x115 + m.i215*m.x61*m.x116 + m.i252*m.x98*m.x117) + m.x138 == -1)

m.c28 = Constraint(expr=-0.00526315789473684*(m.i179*m.x25*m.x115 + m.i216*m.x62*m.x116 + m.i253*m.x99*m.x117) + m.x139
                         == -1)

m.c29 = Constraint(expr=-0.00555555555555556*(m.i180*m.x26*m.x115 + m.i217*m.x63*m.x116 + m.i254*m.x100*m.x117) + m.x140
                         == -1)

m.c30 = Constraint(expr=-0.0142857142857143*(m.i181*m.x27*m.x115 + m.i218*m.x64*m.x116 + m.i255*m.x101*m.x117) + m.x141
                         == -1)

m.c31 = Constraint(expr=-0.0142857142857143*(m.i182*m.x28*m.x115 + m.i219*m.x65*m.x116 + m.i256*m.x102*m.x117) + m.x142
                         == -1)

m.c32 = Constraint(expr=-0.025*(m.i183*m.x29*m.x115 + m.i220*m.x66*m.x116 + m.i257*m.x103*m.x117) + m.x143 == -1)

m.c33 = Constraint(expr=-0.025*(m.i184*m.x30*m.x115 + m.i221*m.x67*m.x116 + m.i258*m.x104*m.x117) + m.x144 == -1)

m.c34 = Constraint(expr=-0.025*(m.i185*m.x31*m.x115 + m.i222*m.x68*m.x116 + m.i259*m.x105*m.x117) + m.x145 == -1)

m.c35 = Constraint(expr=-0.0333333333333333*(m.i186*m.x32*m.x115 + m.i223*m.x69*m.x116 + m.i260*m.x106*m.x117) + m.x146
                         == -1)

m.c36 = Constraint(expr=-0.05*(m.i187*m.x33*m.x115 + m.i224*m.x70*m.x116 + m.i261*m.x107*m.x117) + m.x147 == -1)

m.c37 = Constraint(expr=-0.05*(m.i188*m.x34*m.x115 + m.i225*m.x71*m.x116 + m.i262*m.x108*m.x117) + m.x148 == -1)

m.c38 = Constraint(expr=-0.05*(m.i189*m.x35*m.x115 + m.i226*m.x72*m.x116 + m.i263*m.x109*m.x117) + m.x149 == -1)

m.c39 = Constraint(expr=-0.1*(m.i190*m.x36*m.x115 + m.i227*m.x73*m.x116 + m.i264*m.x110*m.x117) + m.x150 == -1)

m.c40 = Constraint(expr=-0.1*(m.i191*m.x37*m.x115 + m.i228*m.x74*m.x116 + m.i265*m.x111*m.x117) + m.x151 == -1)

m.c41 = Constraint(expr=-0.1*(m.i192*m.x38*m.x115 + m.i229*m.x75*m.x116 + m.i266*m.x112*m.x117) + m.x152 == -1)

m.c42 = Constraint(expr=-0.1*(m.i193*m.x39*m.x115 + m.i230*m.x76*m.x116 + m.i267*m.x113*m.x117) + m.x153 == -1)

m.c43 = Constraint(expr=-0.1*(m.i194*m.x40*m.x115 + m.i231*m.x77*m.x116 + m.i268*m.x114*m.x117) + m.x154 == -1)

m.c44 = Constraint(expr=   m.x115 - 20*m.b155 >= 0)

m.c45 = Constraint(expr=   m.x116 - 52.5*m.b156 >= 0)

m.c46 = Constraint(expr=   m.x117 - 151.25*m.b157 >= 0)

m.c47 = Constraint(expr=   m.x115 - 50*m.b155 <= 0)

m.c48 = Constraint(expr=   m.x116 - 250*m.b156 <= 0)

m.c49 = Constraint(expr=   m.x117 - 250*m.b157 <= 0)
