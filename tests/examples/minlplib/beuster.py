#  MINLP written by GAMS Convert at 04/21/18 13:51:12
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        115      100       12        3        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        158      106       52        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        398      239      159        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(10,None),initialize=67.344)
m.x2 = Var(within=Reals,bounds=(0.001,None),initialize=1744.656)
m.x3 = Var(within=Reals,bounds=(1,None),initialize=3.042)
m.x4 = Var(within=Reals,bounds=(1,None),initialize=12.808)
m.x5 = Var(within=Reals,bounds=(2,None),initialize=216.161)
m.x6 = Var(within=Reals,bounds=(1,None),initialize=1.225)
m.x7 = Var(within=Reals,bounds=(0.1675,None),initialize=3.842)
m.x8 = Var(within=Reals,bounds=(0,None),initialize=1800)
m.x9 = Var(within=Reals,bounds=(0,None),initialize=241.731)
m.x10 = Var(within=Reals,bounds=(0,None),initialize=158.011)
m.x11 = Var(within=Reals,bounds=(0,None),initialize=88.847)
m.x12 = Var(within=Reals,bounds=(5,None),initialize=10)
m.x13 = Var(within=Reals,bounds=(5,None),initialize=12.176)
m.x14 = Var(within=Reals,bounds=(5,None),initialize=14.048)
m.x15 = Var(within=Reals,bounds=(5,None),initialize=16.416)
m.x16 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x17 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x18 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x19 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x20 = Var(within=Reals,bounds=(0,None),initialize=12.176)
m.x21 = Var(within=Reals,bounds=(0,None),initialize=14.048)
m.x22 = Var(within=Reals,bounds=(0,None),initialize=16.416)
m.x23 = Var(within=Reals,bounds=(0,None),initialize=18)
m.x24 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x28 = Var(within=Reals,bounds=(0.001,None),initialize=1.956)
m.x29 = Var(within=Reals,bounds=(0.001,None),initialize=1.317)
m.x30 = Var(within=Reals,bounds=(0.001,None),initialize=1.737)
m.x31 = Var(within=Reals,bounds=(0.001,None),initialize=1.248)
m.x32 = Var(within=Reals,bounds=(1,None),initialize=176.503)
m.x33 = Var(within=Reals,bounds=(1,None),initialize=10.861)
m.x34 = Var(within=Reals,bounds=(1,None),initialize=11.542)
m.x35 = Var(within=Reals,bounds=(1,None),initialize=17.256)
m.x36 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x37 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x38 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x39 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x40 = Var(within=Reals,bounds=(1,None),initialize=176.572)
m.x41 = Var(within=Reals,bounds=(1,None),initialize=154.169)
m.x42 = Var(within=Reals,bounds=(1,None),initialize=119.85)
m.x43 = Var(within=Reals,bounds=(1,None),initialize=60.852)
m.x44 = Var(within=Reals,bounds=(0.01,None),initialize=110.804)
m.x45 = Var(within=Reals,bounds=(0.01,None),initialize=120.863)
m.x46 = Var(within=Reals,bounds=(0.01,None),initialize=130.858)
m.x47 = Var(within=Reals,bounds=(0.01,None),initialize=140.397)
m.x48 = Var(within=Reals,bounds=(2,6),initialize=2.5)
m.x49 = Var(within=Reals,bounds=(2,6),initialize=2.5)
m.x50 = Var(within=Reals,bounds=(2,6),initialize=2.5)
m.x51 = Var(within=Reals,bounds=(2,6),initialize=2.5)
m.x52 = Var(within=Reals,bounds=(1.33,6),initialize=4)
m.x53 = Var(within=Reals,bounds=(1.33,6),initialize=4)
m.x54 = Var(within=Reals,bounds=(1.33,6),initialize=4)
m.x55 = Var(within=Reals,bounds=(1.33,6),initialize=4)
m.x56 = Var(within=Reals,bounds=(1.13E-8,None),initialize=2.1769E-8)
m.x57 = Var(within=Reals,bounds=(1.13E-8,None),initialize=2.1769E-8)
m.x58 = Var(within=Reals,bounds=(1.13E-8,None),initialize=2.1769E-8)
m.x59 = Var(within=Reals,bounds=(1.13E-8,None),initialize=2.1769E-8)
m.x60 = Var(within=Reals,bounds=(2.9E-7,None),initialize=1.299)
m.x61 = Var(within=Reals,bounds=(2.9E-7,None),initialize=1.642)
m.x62 = Var(within=Reals,bounds=(2.9E-7,None),initialize=2.167)
m.x63 = Var(within=Reals,bounds=(2.9E-7,None),initialize=3.069)
m.x64 = Var(within=Reals,bounds=(3E-7,None),initialize=1.3)
m.x65 = Var(within=Reals,bounds=(3E-7,None),initialize=1.643)
m.x66 = Var(within=Reals,bounds=(3E-7,None),initialize=2.169)
m.x67 = Var(within=Reals,bounds=(3E-7,None),initialize=3.072)
m.x68 = Var(within=Reals,bounds=(3E-10,None),initialize=1E-6)
m.x69 = Var(within=Reals,bounds=(3E-10,None),initialize=1E-6)
m.x70 = Var(within=Reals,bounds=(3E-10,None),initialize=2E-6)
m.x71 = Var(within=Reals,bounds=(3E-10,None),initialize=2E-6)
m.x72 = Var(within=Reals,bounds=(0.05,None),initialize=8.825)
m.x73 = Var(within=Reals,bounds=(0.05,None),initialize=0.543)
m.x74 = Var(within=Reals,bounds=(0.05,None),initialize=0.577)
m.x75 = Var(within=Reals,bounds=(0.05,None),initialize=0.863)
m.x76 = Var(within=Reals,bounds=(0,None),initialize=1121.796)
m.x77 = Var(within=Reals,bounds=(0,None),initialize=1121.796)
m.x78 = Var(within=Reals,bounds=(0,None),initialize=1121.796)
m.x79 = Var(within=Reals,bounds=(0,None),initialize=1121.796)
m.x80 = Var(within=Reals,bounds=(0,None),initialize=198000)
m.x81 = Var(within=Reals,bounds=(0,None),initialize=12183.696)
m.x82 = Var(within=Reals,bounds=(0,None),initialize=12947.373)
m.x83 = Var(within=Reals,bounds=(0,None),initialize=19357.594)
m.x84 = Var(within=Reals,bounds=(0,None),initialize=0.2)
m.x85 = Var(within=Reals,bounds=(0,None),initialize=0.027)
m.x86 = Var(within=Reals,bounds=(0,None),initialize=0.018)
m.x87 = Var(within=Reals,bounds=(0,None),initialize=0.01)
m.x88 = Var(within=Reals,bounds=(0,None),initialize=1.1)
m.x89 = Var(within=Reals,bounds=(0,None),initialize=0.168)
m.x90 = Var(within=Reals,bounds=(0,None),initialize=0.122)
m.x91 = Var(within=Reals,bounds=(0,None),initialize=0.108)
m.x92 = Var(within=Reals,bounds=(0,None),initialize=2.063)
m.x93 = Var(within=Reals,bounds=(0,None),initialize=0.15)
m.x94 = Var(within=Reals,bounds=(0,None),initialize=0.142)
m.x95 = Var(within=Reals,bounds=(0,None),initialize=0.186)
m.x96 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x97 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x98 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x99 = Var(within=Reals,bounds=(0,None),initialize=0)
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
m.b136 = Var(within=Binary,bounds=(0,1),initialize=0)
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
m.x153 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x154 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x155 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x156 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x157 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x158 = Var(within=Reals,bounds=(0,None),initialize=0)

m.obj = Objective(expr=   m.x153 + m.x154 + m.x155 + m.x156 + m.x157 + m.x158 + 3271.22725820856, sense=minimize)

m.c2 = Constraint(expr=   m.x8 == 1800)

m.c3 = Constraint(expr=   m.x12 == 5)

m.c4 = Constraint(expr=-(m.x99*(m.x24 + m.x25 + m.x26 + m.x27) + (m.x98 - m.x99)*(m.x24 + m.x25 + m.x26) + (m.x97 - 
                       m.x98)*(m.x24 + m.x25) + m.x24*(m.x96 - m.x97)) + m.x2 == 0)

m.c5 = Constraint(expr=-((m.x28*m.x24 + m.x29*m.x25 + m.x30*m.x26 + m.x31*m.x27)*m.x99 + (m.x28*m.x24 + m.x29*m.x25 + 
                       m.x30*m.x26)*(m.x98 - m.x99) + (m.x28*m.x24 + m.x29*m.x25)*(m.x97 - m.x98) + m.x28*m.x24*(m.x96
                        - m.x97))/m.x2 + m.x3 == 0)

m.c6 = Constraint(expr=-(m.x19*m.x99 + m.x18*(m.x98 - m.x99) + m.x17*(m.x97 - m.x98) + m.x16*(m.x96 - m.x97)) + m.x1
                        == 0)

m.c7 = Constraint(expr=-(m.x23*m.x99 + m.x22*(m.x98 - m.x99) + m.x21*(m.x97 - m.x98) + m.x20*(m.x96 - m.x97)) == -100)

m.c8 = Constraint(expr=-(m.x16*m.x97 - 1000*m.x97) + m.x9 == 1000)

m.c9 = Constraint(expr=-(m.x20*m.x97 - 10*m.x97) + m.x13 == 10)

m.c10 = Constraint(expr=-(m.x99*(m.x32 + m.x33 + m.x34 + m.x35) + (m.x98 - m.x99)*(m.x32 + m.x33 + m.x34) + (m.x97 - 
                        m.x98)*(m.x32 + m.x33) + m.x32*(m.x96 - m.x97)) + m.x5 == 0)

m.c11 = Constraint(expr=-(m.x99*(m.x36 + m.x37 + m.x38 + m.x39) + (m.x98 - m.x99)*(m.x36 + m.x37 + m.x38) + (m.x97 - 
                        m.x98)*(m.x36 + m.x37) + m.x36*(m.x96 - m.x97)) + m.x6 == 0)

m.c12 = Constraint(expr=-(m.x99*(m.x92 + m.x93 + m.x94 + m.x95) + (m.x98 - m.x99)*(m.x92 + m.x93 + m.x94) + (m.x97 - 
                        m.x98)*(m.x92 + m.x93) + m.x92*(m.x96 - m.x97)) + m.x7 == 0)

m.c13 = Constraint(expr=-(m.x99*(m.x72 + m.x73 + m.x74 + m.x75) + (m.x98 - m.x99)*(m.x72 + m.x73 + m.x74) + (m.x97 - 
                        m.x98)*(m.x72 + m.x73) + m.x72*(m.x96 - m.x97)) + m.x4 == 0)

m.c14 = Constraint(expr=-(m.x17*m.x98 - 1058*m.x98) + m.x10 == 1058)

m.c15 = Constraint(expr=-(m.x21*m.x98 - 10*m.x98) + m.x14 == 10)

m.c16 = Constraint(expr=-(m.x18*m.x99 - 1008*m.x99) + m.x11 == 1008)

m.c17 = Constraint(expr=-(m.x22*m.x99 - 13*m.x99) + m.x15 == 13)

m.c18 = Constraint(expr=0.00277777777777778*m.x40/log((m.x44 - m.x28)/(m.x20 - m.x28)) - 10000000*m.x56 == 0)

m.c19 = Constraint(expr=0.00277777777777778*m.x41/log((m.x45 - m.x29)/(m.x21 - m.x29)) - 10000000*m.x57 == 0)

m.c20 = Constraint(expr=0.00277777777777778*m.x42/log((m.x46 - m.x30)/(m.x22 - m.x30)) - 10000000*m.x58 == 0)

m.c21 = Constraint(expr=0.00277777777777778*m.x43/log((m.x47 - m.x31)/(m.x23 - m.x31)) - 10000000*m.x59 == 0)

m.c22 = Constraint(expr=   50*m.x28 - m.x44 == 0)

m.c23 = Constraint(expr=   50*m.x29 - m.x45 == 0)

m.c24 = Constraint(expr=   50*m.x30 - m.x46 == 0)

m.c25 = Constraint(expr=   50*m.x31 - m.x47 == 0)

m.c26 = Constraint(expr=   m.x40 - 65.38084341288*m.x48 + 65.38084341288*m.x60 == 0)

m.c27 = Constraint(expr=   m.x41 - 65.38084341288*m.x49 + 65.38084341288*m.x61 == 0)

m.c28 = Constraint(expr=   m.x42 - 65.38084341288*m.x50 + 65.38084341288*m.x62 == 0)

m.c29 = Constraint(expr=   m.x43 - 65.38084341288*m.x51 + 65.38084341288*m.x63 == 0)

m.c30 = Constraint(expr= - m.x60 + m.x64 - 1000*m.x68 == 0)

m.c31 = Constraint(expr= - m.x61 + m.x65 - 1000*m.x69 == 0)

m.c32 = Constraint(expr= - m.x62 + m.x66 - 1000*m.x70 == 0)

m.c33 = Constraint(expr= - m.x63 + m.x67 - 1000*m.x71 == 0)

m.c34 = Constraint(expr=-1e-5*(12.09*m.x44**2 + 3.66*m.x44 - 0.08*m.x44**3 + 0.0002592*m.x44**4) + m.x64 == 0)

m.c35 = Constraint(expr=-1e-5*(12.09*m.x45**2 + 3.66*m.x45 - 0.08*m.x45**3 + 0.0002592*m.x45**4) + m.x65 == 0)

m.c36 = Constraint(expr=-1e-5*(12.09*m.x46**2 + 3.66*m.x46 - 0.08*m.x46**3 + 0.0002592*m.x46**4) + m.x66 == 0)

m.c37 = Constraint(expr=-1e-5*(12.09*m.x47**2 + 3.66*m.x47 - 0.08*m.x47**3 + 0.0002592*m.x47**4) + m.x67 == 0)

m.c38 = Constraint(expr=-1e-5*(12.09*m.x28**2 + 3.66*m.x28 - 0.08*m.x28**3 + 0.0002592*m.x28**4) + 1000*m.x68 == 0)

m.c39 = Constraint(expr=-1e-5*(12.09*m.x29**2 + 3.66*m.x29 - 0.08*m.x29**3 + 0.0002592*m.x29**4) + 1000*m.x69 == 0)

m.c40 = Constraint(expr=-1e-5*(12.09*m.x30**2 + 3.66*m.x30 - 0.08*m.x30**3 + 0.0002592*m.x30**4) + 1000*m.x70 == 0)

m.c41 = Constraint(expr=-1e-5*(12.09*m.x31**2 + 3.66*m.x31 - 0.08*m.x31**3 + 0.0002592*m.x31**4) + 1000*m.x71 == 0)

m.c42 = Constraint(expr=-0.000113572384718704*(7936.50793650794*m.x52)**0.75 + 10000000*m.x56 == 0)

m.c43 = Constraint(expr=-0.000113572384718704*(7936.50793650794*m.x53)**0.75 + 10000000*m.x57 == 0)

m.c44 = Constraint(expr=-0.000113572384718704*(7936.50793650794*m.x54)**0.75 + 10000000*m.x58 == 0)

m.c45 = Constraint(expr=-0.000113572384718704*(7936.50793650794*m.x55)**0.75 + 10000000*m.x59 == 0)

m.c46 = Constraint(expr= - m.x8 + m.x16 + m.x24 == 0)

m.c47 = Constraint(expr= - m.x9 + m.x17 + m.x25 == 0)

m.c48 = Constraint(expr= - m.x10 + m.x18 + m.x26 == 0)

m.c49 = Constraint(expr= - m.x11 + m.x19 + m.x27 == 0)

m.c50 = Constraint(expr=m.x12*m.x8 - (m.x20*m.x16 + m.x28*m.x24) == 0)

m.c51 = Constraint(expr=m.x13*m.x9 - (m.x21*m.x17 + m.x29*m.x25) == 0)

m.c52 = Constraint(expr=m.x14*m.x10 - (m.x22*m.x18 + m.x30*m.x26) == 0)

m.c53 = Constraint(expr=m.x15*m.x11 - (m.x23*m.x19 + m.x31*m.x27) == 0)

m.c54 = Constraint(expr=-2.77777777777778e-5*m.x48*m.x8 + m.x84 == 0)

m.c55 = Constraint(expr=-2.77777777777778e-5*m.x49*m.x9 + m.x85 == 0)

m.c56 = Constraint(expr=-2.77777777777778e-5*m.x50*m.x10 + m.x86 == 0)

m.c57 = Constraint(expr=-2.77777777777778e-5*m.x51*m.x11 + m.x87 == 0)

m.c58 = Constraint(expr=-m.x24/m.x40 + m.x72 == 0)

m.c59 = Constraint(expr=-m.x25/m.x41 + m.x73 == 0)

m.c60 = Constraint(expr=-m.x26/m.x42 + m.x74 == 0)

m.c61 = Constraint(expr=-m.x27/m.x43 + m.x75 == 0)

m.c62 = Constraint(expr=   m.x32 - 20*m.x72 == 0)

m.c63 = Constraint(expr=   m.x33 - 20*m.x73 == 0)

m.c64 = Constraint(expr=   m.x34 - 20*m.x74 == 0)

m.c65 = Constraint(expr=   m.x35 - 20*m.x75 == 0)

m.c66 = Constraint(expr= - 373.932*m.x52 + m.x76 == 0)

m.c67 = Constraint(expr= - 373.932*m.x53 + m.x77 == 0)

m.c68 = Constraint(expr= - 373.932*m.x54 + m.x78 == 0)

m.c69 = Constraint(expr= - 373.932*m.x55 + m.x79 == 0)

m.c70 = Constraint(expr=-m.x32*m.x76 + m.x80 == 0)

m.c71 = Constraint(expr=-m.x33*m.x77 + m.x81 == 0)

m.c72 = Constraint(expr=-m.x34*m.x78 + m.x82 == 0)

m.c73 = Constraint(expr=-m.x35*m.x79 + m.x83 == 0)

m.c74 = Constraint(expr= - 5.55555555555556E-6*m.x80 + m.x88 == 0)

m.c75 = Constraint(expr= - 5.55555555555556E-6*m.x81 + m.x89 == 0)

m.c76 = Constraint(expr= - 5.55555555555556E-6*m.x82 + m.x90 == 0)

m.c77 = Constraint(expr= - 5.55555555555556E-6*m.x83 + m.x91 == 0)

m.c78 = Constraint(expr= - 1.58730158730159*m.x84 - 1.58730158730159*m.x88 + m.x92 == 0)

m.c79 = Constraint(expr= - 1.58730158730159*m.x85 - 1.58730158730159*m.x89 + m.x93 == 0)

m.c80 = Constraint(expr= - 1.58730158730159*m.x86 - 1.58730158730159*m.x90 + m.x94 == 0)

m.c81 = Constraint(expr= - 1.58730158730159*m.x87 - 1.58730158730159*m.x91 + m.x95 == 0)

m.c82 = Constraint(expr=   m.x36 - 0.909090909090909*m.x88 >= 0)

m.c83 = Constraint(expr=   m.x37 - 0.909090909090909*m.x89 >= 0)

m.c84 = Constraint(expr=   m.x38 - 0.909090909090909*m.x90 >= 0)

m.c85 = Constraint(expr=   m.x39 - 0.909090909090909*m.x91 >= 0)

m.c86 = Constraint(expr=   m.x32 - m.b100 - 2*m.b104 - 4*m.b108 - 8*m.b112 - 16*m.b116 - 32*m.b120 - 64*m.b124
                         - 128*m.b128 == 0)

m.c87 = Constraint(expr=   m.x33 - m.b101 - 2*m.b105 - 4*m.b109 - 8*m.b113 - 16*m.b117 - 32*m.b121 - 64*m.b125
                         - 128*m.b129 == 0)

m.c88 = Constraint(expr=   m.x34 - m.b102 - 2*m.b106 - 4*m.b110 - 8*m.b114 - 16*m.b118 - 32*m.b122 - 64*m.b126
                         - 128*m.b130 == 0)

m.c89 = Constraint(expr=   m.x35 - m.b103 - 2*m.b107 - 4*m.b111 - 8*m.b115 - 16*m.b119 - 32*m.b123 - 64*m.b127
                         - 128*m.b131 == 0)

m.c90 = Constraint(expr=   m.x36 - m.b132 - 2*m.b136 - 4*m.b140 - 8*m.b144 == 0)

m.c91 = Constraint(expr=   m.x37 - m.b133 - 2*m.b137 - 4*m.b141 - 8*m.b145 == 0)

m.c92 = Constraint(expr=   m.x38 - m.b134 - 2*m.b138 - 4*m.b142 - 8*m.b146 == 0)

m.c93 = Constraint(expr=   m.x39 - m.b135 - 2*m.b139 - 4*m.b143 - 8*m.b147 == 0)

m.c94 = Constraint(expr=   m.x96 - m.b148 == 0)

m.c95 = Constraint(expr=   m.x97 - m.b149 == 0)

m.c96 = Constraint(expr=   m.x98 - m.b150 == 0)

m.c97 = Constraint(expr=   m.x99 - m.b151 == 0)

m.c98 = Constraint(expr=   m.b148 == 1)

m.c99 = Constraint(expr= - m.b148 + m.b149 <= 0)

m.c100 = Constraint(expr= - m.b149 + m.b150 <= 0)

m.c101 = Constraint(expr= - m.b150 + m.b151 <= 0)

m.c102 = Constraint(expr= - 1261.75908530902*m.x96 - 1261.75908530902*m.x97 - 1261.75908530902*m.x98
                          - 1261.75908530902*m.x99 + m.x153 == 0)

m.c103 = Constraint(expr= - 292.07386234005*m.x6 + m.x154 == 0)

m.c104 = Constraint(expr= - 2103.94993266178*m.x7 + m.x157 == 0)

m.c105 = Constraint(expr= - 45.7380420143865*m.x2 + m.x155 == 0)

m.c106 = Constraint(expr=-4.57380420143865*m.x2*m.x3 + m.x156 == 0)

m.c107 = Constraint(expr= - 764.973851088085*m.x4 + m.x158 == 0)

m.c108 = Constraint(expr=   m.x20 - m.x28 >= 0.01)

m.c109 = Constraint(expr=   m.x21 - m.x29 >= 0.01)

m.c110 = Constraint(expr=   m.x22 - m.x30 >= 0.01)

m.c111 = Constraint(expr=   m.x23 - m.x31 >= 0.01)

m.c112 = Constraint(expr= - m.x28 + m.x44 >= 0.01)

m.c113 = Constraint(expr= - m.x29 + m.x45 >= 0.01)

m.c114 = Constraint(expr= - m.x30 + m.x46 >= 0.01)

m.c115 = Constraint(expr= - m.x31 + m.x47 >= 0.01)
