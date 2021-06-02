#  NLP written by GAMS Convert at 04/21/18 13:52:27
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        174      145        0       29        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        158      158        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        619      407      212        0


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(1.44,32),initialize=1.44)
m.x2 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x3 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x4 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x5 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,8),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,4),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,8.94427190999916),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,8.94427190999916),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,8.94427190999916),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,8.94427190999916),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,8.94427190999916),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,8.94427190999916),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,8.94427190999916),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,8.94427190999916),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,8.94427190999916),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,8.94427190999916),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,8.94427190999916),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,8.94427190999916),initialize=0)
m.x20 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x21 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x22 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x23 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x24 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x25 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x26 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x27 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x28 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x29 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x30 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x31 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x32 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x33 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x34 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x35 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x36 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x37 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x38 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x39 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x40 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x41 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x42 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x43 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x44 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x45 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x46 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x47 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x48 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x49 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x50 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x51 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x52 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x53 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x54 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x55 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x56 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x57 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x58 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x59 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x60 = Var(within=Reals,bounds=(0,8),initialize=0)
m.x61 = Var(within=Reals,bounds=(0,4),initialize=0)
m.x62 = Var(within=Reals,bounds=(0,8),initialize=0)
m.x63 = Var(within=Reals,bounds=(0,4),initialize=0)
m.x64 = Var(within=Reals,bounds=(0,8.94427190999916),initialize=0)
m.x65 = Var(within=Reals,bounds=(0,8.94427190999916),initialize=0)
m.x66 = Var(within=Reals,bounds=(0,8.94427190999916),initialize=0)
m.x67 = Var(within=Reals,bounds=(0,8.94427190999916),initialize=0)
m.x68 = Var(within=Reals,bounds=(0,8.94427190999916),initialize=0)
m.x69 = Var(within=Reals,bounds=(0,8.94427190999916),initialize=0)
m.x70 = Var(within=Reals,bounds=(0,8.94427190999916),initialize=0)
m.x71 = Var(within=Reals,bounds=(0,8.94427190999916),initialize=0)
m.x72 = Var(within=Reals,bounds=(0,8.94427190999916),initialize=0)
m.x73 = Var(within=Reals,bounds=(0,8.94427190999916),initialize=0)
m.x74 = Var(within=Reals,bounds=(0,8.94427190999916),initialize=0)
m.x75 = Var(within=Reals,bounds=(0,8.94427190999916),initialize=0)
m.x76 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x77 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x78 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x79 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x80 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x81 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x82 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x83 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x84 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x85 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x86 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x87 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x88 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x89 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x90 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x91 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x92 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x93 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x94 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x95 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x96 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x97 = Var(within=Reals,bounds=(-1,1),initialize=0)
m.x98 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x99 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x100 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x101 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x102 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x103 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x104 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x105 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x106 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x107 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x108 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x109 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x110 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x111 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x112 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x113 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x114 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x115 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x116 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x117 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x118 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x119 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x120 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x121 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x122 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x123 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x124 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x125 = Var(within=Reals,bounds=(-8.94427190999916,8.94427190999916),initialize=0)
m.x126 = Var(within=Reals,bounds=(1.2,6.8),initialize=1.2)
m.x127 = Var(within=Reals,bounds=(1.2,2.8),initialize=1.2)
m.x128 = Var(within=Reals,bounds=(0,8),initialize=0)
m.x129 = Var(within=Reals,bounds=(0,4),initialize=0)
m.x130 = Var(within=Reals,bounds=(0,8),initialize=0)
m.x131 = Var(within=Reals,bounds=(0,4),initialize=0)
m.x132 = Var(within=Reals,bounds=(0,8),initialize=0)
m.x133 = Var(within=Reals,bounds=(0,4),initialize=0)
m.x134 = Var(within=Reals,bounds=(0,8),initialize=0)
m.x135 = Var(within=Reals,bounds=(0,4),initialize=0)
m.x136 = Var(within=Reals,bounds=(0,8),initialize=0)
m.x137 = Var(within=Reals,bounds=(0,4),initialize=0)
m.x138 = Var(within=Reals,bounds=(0,8),initialize=0)
m.x139 = Var(within=Reals,bounds=(0,4),initialize=0)
m.x140 = Var(within=Reals,bounds=(0,8),initialize=0)
m.x141 = Var(within=Reals,bounds=(0,4),initialize=0)
m.x142 = Var(within=Reals,bounds=(0,8),initialize=0)
m.x143 = Var(within=Reals,bounds=(0,4),initialize=0)
m.x144 = Var(within=Reals,bounds=(0,8),initialize=0)
m.x145 = Var(within=Reals,bounds=(0,4),initialize=0)
m.x146 = Var(within=Reals,bounds=(0,8),initialize=0)
m.x147 = Var(within=Reals,bounds=(0,4),initialize=0)
m.x148 = Var(within=Reals,bounds=(0,8),initialize=0)
m.x149 = Var(within=Reals,bounds=(0,4),initialize=0)
m.x150 = Var(within=Reals,bounds=(0,8),initialize=0)
m.x151 = Var(within=Reals,bounds=(0,4),initialize=0)
m.x152 = Var(within=Reals,bounds=(0,8),initialize=0)
m.x153 = Var(within=Reals,bounds=(0,4),initialize=0)
m.x154 = Var(within=Reals,bounds=(0,8),initialize=0)
m.x155 = Var(within=Reals,bounds=(0,4),initialize=0)
m.x156 = Var(within=Reals,bounds=(0,8),initialize=0)
m.x157 = Var(within=Reals,bounds=(0,4),initialize=0)
m.x158 = Var(within=Reals,bounds=(0,32),initialize=0)

m.obj = Objective(expr=m.x158, sense=minimize)

m.c1 = Constraint(expr= - m.x1 + m.x158 == -8.5238934211693)

m.c2 = Constraint(expr=-m.x156*m.x157 + m.x1 == 0)

m.c3 = Constraint(expr=   m.x126 - m.x156 <= -1.2)

m.c4 = Constraint(expr=   m.x127 - m.x157 <= -1.2)

m.c5 = Constraint(expr= - 0.166666666666667*m.x128 - 0.166666666666667*m.x130 - 0.166666666666667*m.x132
                        - 0.166666666666667*m.x134 - 0.166666666666667*m.x136 - 0.166666666666667*m.x138 + m.x152 == 0)

m.c6 = Constraint(expr= - 0.166666666666667*m.x129 - 0.166666666666667*m.x131 - 0.166666666666667*m.x133
                        - 0.166666666666667*m.x135 - 0.166666666666667*m.x137 - 0.166666666666667*m.x139 + m.x153 == 0)

m.c7 = Constraint(expr= - 0.166666666666667*m.x140 - 0.166666666666667*m.x142 - 0.166666666666667*m.x144
                        - 0.166666666666667*m.x146 - 0.166666666666667*m.x148 - 0.166666666666667*m.x150 + m.x154 == 0)

m.c8 = Constraint(expr= - 0.166666666666667*m.x141 - 0.166666666666667*m.x143 - 0.166666666666667*m.x145
                        - 0.166666666666667*m.x147 - 0.166666666666667*m.x149 - 0.166666666666667*m.x151 + m.x155 == 0)

m.c9 = Constraint(expr=m.x2*m.x2 + m.x4*m.x4 == 1)

m.c10 = Constraint(expr=m.x3*m.x3 + m.x5*m.x5 == 1)

m.c11 = Constraint(expr=   m.x128 - m.x156 <= 0)

m.c12 = Constraint(expr=   m.x129 - m.x157 <= 0)

m.c13 = Constraint(expr=   m.x130 - m.x156 <= 0)

m.c14 = Constraint(expr=   m.x131 - m.x157 <= 0)

m.c15 = Constraint(expr=   m.x132 - m.x156 <= 0)

m.c16 = Constraint(expr=   m.x133 - m.x157 <= 0)

m.c17 = Constraint(expr=   m.x134 - m.x156 <= 0)

m.c18 = Constraint(expr=   m.x135 - m.x157 <= 0)

m.c19 = Constraint(expr=   m.x136 - m.x156 <= 0)

m.c20 = Constraint(expr=   m.x137 - m.x157 <= 0)

m.c21 = Constraint(expr=   m.x138 - m.x156 <= 0)

m.c22 = Constraint(expr=   m.x139 - m.x157 <= 0)

m.c23 = Constraint(expr=   m.x140 - m.x156 <= 0)

m.c24 = Constraint(expr=   m.x141 - m.x157 <= 0)

m.c25 = Constraint(expr=   m.x142 - m.x156 <= 0)

m.c26 = Constraint(expr=   m.x143 - m.x157 <= 0)

m.c27 = Constraint(expr=   m.x144 - m.x156 <= 0)

m.c28 = Constraint(expr=   m.x145 - m.x157 <= 0)

m.c29 = Constraint(expr=   m.x146 - m.x156 <= 0)

m.c30 = Constraint(expr=   m.x147 - m.x157 <= 0)

m.c31 = Constraint(expr=   m.x148 - m.x156 <= 0)

m.c32 = Constraint(expr=   m.x149 - m.x157 <= 0)

m.c33 = Constraint(expr=   m.x150 - m.x156 <= 0)

m.c34 = Constraint(expr=   m.x151 - m.x157 <= 0)

m.c35 = Constraint(expr=   0.833333333333333*m.x2 + 0.75*m.x4 + m.x128 - m.x152 == 0)

m.c36 = Constraint(expr= - 0.166666666666667*m.x2 + 0.75*m.x4 + m.x130 - m.x152 == 0)

m.c37 = Constraint(expr= - 0.666666666666667*m.x2 + 0.25*m.x4 + m.x132 - m.x152 == 0)

m.c38 = Constraint(expr= - 0.666666666666667*m.x2 - 0.25*m.x4 + m.x134 - m.x152 == 0)

m.c39 = Constraint(expr= - 0.166666666666667*m.x2 - 0.75*m.x4 + m.x136 - m.x152 == 0)

m.c40 = Constraint(expr=   0.833333333333333*m.x2 - 0.75*m.x4 + m.x138 - m.x152 == 0)

m.c41 = Constraint(expr=   0.833333333333333*m.x3 + 0.75*m.x5 + m.x140 - m.x154 == 0)

m.c42 = Constraint(expr= - 0.166666666666667*m.x3 + 0.75*m.x5 + m.x142 - m.x154 == 0)

m.c43 = Constraint(expr= - 0.666666666666667*m.x3 + 0.25*m.x5 + m.x144 - m.x154 == 0)

m.c44 = Constraint(expr= - 0.666666666666667*m.x3 - 0.25*m.x5 + m.x146 - m.x154 == 0)

m.c45 = Constraint(expr= - 0.166666666666667*m.x3 - 0.75*m.x5 + m.x148 - m.x154 == 0)

m.c46 = Constraint(expr=   0.833333333333333*m.x3 - 0.75*m.x5 + m.x150 - m.x154 == 0)

m.c47 = Constraint(expr= - 0.75*m.x2 + 0.833333333333333*m.x4 + m.x129 - m.x153 == 0)

m.c48 = Constraint(expr= - 0.75*m.x2 - 0.166666666666667*m.x4 + m.x131 - m.x153 == 0)

m.c49 = Constraint(expr= - 0.25*m.x2 - 0.666666666666667*m.x4 + m.x133 - m.x153 == 0)

m.c50 = Constraint(expr=   0.25*m.x2 - 0.666666666666667*m.x4 + m.x135 - m.x153 == 0)

m.c51 = Constraint(expr=   0.75*m.x2 - 0.166666666666667*m.x4 + m.x137 - m.x153 == 0)

m.c52 = Constraint(expr=   0.75*m.x2 + 0.833333333333333*m.x4 + m.x139 - m.x153 == 0)

m.c53 = Constraint(expr= - 0.75*m.x3 + 0.833333333333333*m.x5 + m.x141 - m.x155 == 0)

m.c54 = Constraint(expr= - 0.75*m.x3 - 0.166666666666667*m.x5 + m.x143 - m.x155 == 0)

m.c55 = Constraint(expr= - 0.25*m.x3 - 0.666666666666667*m.x5 + m.x145 - m.x155 == 0)

m.c56 = Constraint(expr=   0.25*m.x3 - 0.666666666666667*m.x5 + m.x147 - m.x155 == 0)

m.c57 = Constraint(expr=   0.75*m.x3 - 0.166666666666667*m.x5 + m.x149 - m.x155 == 0)

m.c58 = Constraint(expr=   0.75*m.x3 + 0.833333333333333*m.x5 + m.x151 - m.x155 == 0)

m.c59 = Constraint(expr=m.x32*m.x32 + m.x33*m.x33 == 1)

m.c60 = Constraint(expr= - m.x33 + m.x34 == 0)

m.c61 = Constraint(expr=   m.x32 + m.x35 == 0)

m.c62 = Constraint(expr=m.x32*m.x20 + m.x6 + m.x36 - m.x128 == 0)

m.c63 = Constraint(expr=m.x33*m.x20 + m.x7 + m.x37 - m.x129 == 0)

m.c64 = Constraint(expr=m.x32*m.x21 + m.x6 + m.x38 - m.x130 == 0)

m.c65 = Constraint(expr=m.x33*m.x21 + m.x7 + m.x39 - m.x131 == 0)

m.c66 = Constraint(expr=m.x32*m.x22 + m.x6 + m.x40 - m.x132 == 0)

m.c67 = Constraint(expr=m.x33*m.x22 + m.x7 + m.x41 - m.x133 == 0)

m.c68 = Constraint(expr=m.x32*m.x23 + m.x6 + m.x42 - m.x134 == 0)

m.c69 = Constraint(expr=m.x33*m.x23 + m.x7 + m.x43 - m.x135 == 0)

m.c70 = Constraint(expr=m.x32*m.x24 + m.x6 + m.x44 - m.x136 == 0)

m.c71 = Constraint(expr=m.x33*m.x24 + m.x7 + m.x45 - m.x137 == 0)

m.c72 = Constraint(expr=m.x32*m.x25 + m.x6 + m.x46 - m.x138 == 0)

m.c73 = Constraint(expr=m.x33*m.x25 + m.x7 + m.x47 - m.x139 == 0)

m.c74 = Constraint(expr=m.x32*m.x26 + m.x6 + m.x48 - m.x140 == 0)

m.c75 = Constraint(expr=m.x33*m.x26 + m.x7 + m.x49 - m.x141 == 0)

m.c76 = Constraint(expr=m.x32*m.x27 + m.x6 + m.x50 - m.x142 == 0)

m.c77 = Constraint(expr=m.x33*m.x27 + m.x7 + m.x51 - m.x143 == 0)

m.c78 = Constraint(expr=m.x32*m.x28 + m.x6 + m.x52 - m.x144 == 0)

m.c79 = Constraint(expr=m.x33*m.x28 + m.x7 + m.x53 - m.x145 == 0)

m.c80 = Constraint(expr=m.x32*m.x29 + m.x6 + m.x54 - m.x146 == 0)

m.c81 = Constraint(expr=m.x33*m.x29 + m.x7 + m.x55 - m.x147 == 0)

m.c82 = Constraint(expr=m.x32*m.x30 + m.x6 + m.x56 - m.x148 == 0)

m.c83 = Constraint(expr=m.x33*m.x30 + m.x7 + m.x57 - m.x149 == 0)

m.c84 = Constraint(expr=m.x32*m.x31 + m.x6 + m.x58 - m.x150 == 0)

m.c85 = Constraint(expr=m.x33*m.x31 + m.x7 + m.x59 - m.x151 == 0)

m.c86 = Constraint(expr=-m.x8*m.x34 + m.x36 == 0)

m.c87 = Constraint(expr=-m.x8*m.x35 + m.x37 == 0)

m.c88 = Constraint(expr=-m.x9*m.x34 + m.x38 == 0)

m.c89 = Constraint(expr=-m.x9*m.x35 + m.x39 == 0)

m.c90 = Constraint(expr=-m.x10*m.x34 + m.x40 == 0)

m.c91 = Constraint(expr=-m.x10*m.x35 + m.x41 == 0)

m.c92 = Constraint(expr=-m.x11*m.x34 + m.x42 == 0)

m.c93 = Constraint(expr=-m.x11*m.x35 + m.x43 == 0)

m.c94 = Constraint(expr=-m.x12*m.x34 + m.x44 == 0)

m.c95 = Constraint(expr=-m.x12*m.x35 + m.x45 == 0)

m.c96 = Constraint(expr=-m.x13*m.x34 + m.x46 == 0)

m.c97 = Constraint(expr=-m.x13*m.x35 + m.x47 == 0)

m.c98 = Constraint(expr=m.x14*m.x34 + m.x48 == 0)

m.c99 = Constraint(expr=m.x14*m.x35 + m.x49 == 0)

m.c100 = Constraint(expr=m.x15*m.x34 + m.x50 == 0)

m.c101 = Constraint(expr=m.x15*m.x35 + m.x51 == 0)

m.c102 = Constraint(expr=m.x16*m.x34 + m.x52 == 0)

m.c103 = Constraint(expr=m.x16*m.x35 + m.x53 == 0)

m.c104 = Constraint(expr=m.x17*m.x34 + m.x54 == 0)

m.c105 = Constraint(expr=m.x17*m.x35 + m.x55 == 0)

m.c106 = Constraint(expr=m.x18*m.x34 + m.x56 == 0)

m.c107 = Constraint(expr=m.x18*m.x35 + m.x57 == 0)

m.c108 = Constraint(expr=m.x19*m.x34 + m.x58 == 0)

m.c109 = Constraint(expr=m.x19*m.x35 + m.x59 == 0)

m.c110 = Constraint(expr=m.x90*m.x90 + m.x91*m.x91 == 1)

m.c111 = Constraint(expr=m.x92*m.x92 + m.x93*m.x93 == 1)

m.c112 = Constraint(expr= - m.x91 + m.x94 == 0)

m.c113 = Constraint(expr= - m.x93 + m.x96 == 0)

m.c114 = Constraint(expr=   m.x90 + m.x95 == 0)

m.c115 = Constraint(expr=   m.x92 + m.x97 == 0)

m.c116 = Constraint(expr=m.x90*m.x76 + m.x60 + m.x98 - m.x128 == 0)

m.c117 = Constraint(expr=m.x91*m.x76 + m.x61 + m.x99 - m.x129 == 0)

m.c118 = Constraint(expr=m.x90*m.x77 + m.x60 + m.x100 - m.x130 == 0)

m.c119 = Constraint(expr=m.x91*m.x77 + m.x61 + m.x101 - m.x131 == 0)

m.c120 = Constraint(expr=m.x90*m.x78 + m.x60 + m.x102 - m.x132 == 0)

m.c121 = Constraint(expr=m.x91*m.x78 + m.x61 + m.x103 - m.x133 == 0)

m.c122 = Constraint(expr=m.x90*m.x79 + m.x60 + m.x104 - m.x134 == 0)

m.c123 = Constraint(expr=m.x91*m.x79 + m.x61 + m.x105 - m.x135 == 0)

m.c124 = Constraint(expr=m.x90*m.x80 + m.x60 + m.x106 - m.x136 == 0)

m.c125 = Constraint(expr=m.x91*m.x80 + m.x61 + m.x107 - m.x137 == 0)

m.c126 = Constraint(expr=m.x90*m.x81 + m.x60 + m.x108 - m.x138 == 0)

m.c127 = Constraint(expr=m.x91*m.x81 + m.x61 + m.x109 - m.x139 == 0)

m.c128 = Constraint(expr=m.x92*m.x82 + m.x62 + m.x110 - m.x140 == 0)

m.c129 = Constraint(expr=m.x93*m.x82 + m.x63 + m.x111 - m.x141 == 0)

m.c130 = Constraint(expr=m.x92*m.x83 + m.x62 + m.x112 - m.x142 == 0)

m.c131 = Constraint(expr=m.x93*m.x83 + m.x63 + m.x113 - m.x143 == 0)

m.c132 = Constraint(expr=m.x92*m.x84 + m.x62 + m.x114 - m.x144 == 0)

m.c133 = Constraint(expr=m.x93*m.x84 + m.x63 + m.x115 - m.x145 == 0)

m.c134 = Constraint(expr=m.x92*m.x85 + m.x62 + m.x116 - m.x146 == 0)

m.c135 = Constraint(expr=m.x93*m.x85 + m.x63 + m.x117 - m.x147 == 0)

m.c136 = Constraint(expr=m.x92*m.x86 + m.x62 + m.x118 - m.x148 == 0)

m.c137 = Constraint(expr=m.x93*m.x86 + m.x63 + m.x119 - m.x149 == 0)

m.c138 = Constraint(expr=m.x92*m.x87 + m.x62 + m.x120 - m.x150 == 0)

m.c139 = Constraint(expr=m.x93*m.x87 + m.x63 + m.x121 - m.x151 == 0)

m.c140 = Constraint(expr=m.x90*m.x88 + m.x60 + m.x122 - m.x126 == 0)

m.c141 = Constraint(expr=m.x91*m.x88 + m.x61 + m.x123 - m.x127 == 0)

m.c142 = Constraint(expr=m.x92*m.x89 + m.x62 + m.x124 - m.x126 == 0)

m.c143 = Constraint(expr=m.x93*m.x89 + m.x63 + m.x125 - m.x127 == 0)

m.c144 = Constraint(expr=-m.x64*m.x94 + m.x98 == 0)

m.c145 = Constraint(expr=-m.x64*m.x95 + m.x99 == 0)

m.c146 = Constraint(expr=-m.x65*m.x94 + m.x100 == 0)

m.c147 = Constraint(expr=-m.x65*m.x95 + m.x101 == 0)

m.c148 = Constraint(expr=-m.x66*m.x94 + m.x102 == 0)

m.c149 = Constraint(expr=-m.x66*m.x95 + m.x103 == 0)

m.c150 = Constraint(expr=-m.x67*m.x94 + m.x104 == 0)

m.c151 = Constraint(expr=-m.x67*m.x95 + m.x105 == 0)

m.c152 = Constraint(expr=-m.x68*m.x94 + m.x106 == 0)

m.c153 = Constraint(expr=-m.x68*m.x95 + m.x107 == 0)

m.c154 = Constraint(expr=-m.x69*m.x94 + m.x108 == 0)

m.c155 = Constraint(expr=-m.x69*m.x95 + m.x109 == 0)

m.c156 = Constraint(expr=-m.x70*m.x96 + m.x110 == 0)

m.c157 = Constraint(expr=-m.x70*m.x97 + m.x111 == 0)

m.c158 = Constraint(expr=-m.x71*m.x96 + m.x112 == 0)

m.c159 = Constraint(expr=-m.x71*m.x97 + m.x113 == 0)

m.c160 = Constraint(expr=-m.x72*m.x96 + m.x114 == 0)

m.c161 = Constraint(expr=-m.x72*m.x97 + m.x115 == 0)

m.c162 = Constraint(expr=-m.x73*m.x96 + m.x116 == 0)

m.c163 = Constraint(expr=-m.x73*m.x97 + m.x117 == 0)

m.c164 = Constraint(expr=-m.x74*m.x96 + m.x118 == 0)

m.c165 = Constraint(expr=-m.x74*m.x97 + m.x119 == 0)

m.c166 = Constraint(expr=-m.x75*m.x96 + m.x120 == 0)

m.c167 = Constraint(expr=-m.x75*m.x97 + m.x121 == 0)

m.c168 = Constraint(expr=   1.2*m.x94 + m.x122 == 0)

m.c169 = Constraint(expr=   1.2*m.x95 + m.x123 == 0)

m.c170 = Constraint(expr=   1.2*m.x96 + m.x124 == 0)

m.c171 = Constraint(expr=   1.2*m.x97 + m.x125 == 0)

m.c172 = Constraint(expr=   m.x126 <= 4)

m.c173 = Constraint(expr=   m.x127 <= 2)

m.c174 = Constraint(expr=   m.x152 - m.x154 <= 0)
