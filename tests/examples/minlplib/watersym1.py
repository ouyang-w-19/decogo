#  MINLP written by GAMS Convert at 04/21/18 13:55:19
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        202       96       36       70        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        322       98       28        0      196        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1247     1187       60        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,None),initialize=0)
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
m.x57 = Var(within=Reals,bounds=(6.5,None),initialize=11.5)
m.x58 = Var(within=Reals,bounds=(3.25,None),initialize=8.25)
m.x59 = Var(within=Reals,bounds=(16.58,None),initialize=21.58)
m.x60 = Var(within=Reals,bounds=(14.92,None),initialize=19.92)
m.x61 = Var(within=Reals,bounds=(12.925,None),initialize=17.925)
m.x62 = Var(within=Reals,bounds=(12.26,None),initialize=17.26)
m.x63 = Var(within=Reals,bounds=(8.76,None),initialize=13.76)
m.x64 = Var(within=Reals,bounds=(16.08,None),initialize=21.08)
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
m.x93 = Var(within=Reals,bounds=(0,2.5),initialize=0.961470588235294)
m.x94 = Var(within=Reals,bounds=(0,6),initialize=2.30752941176471)
m.x95 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x96 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x97 = Var(within=Reals,bounds=(None,None),initialize=0)
m.b99 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b100 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b101 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b102 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b103 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b104 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b105 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b106 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b107 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b108 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b109 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b110 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b111 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b112 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b113 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b114 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b115 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b116 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b117 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b118 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b119 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b120 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b121 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b122 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b123 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b124 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b125 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b126 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.s1s127 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s128 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s129 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s130 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s131 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s132 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s133 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s134 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s135 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s136 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s137 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s138 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s139 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s140 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s141 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s142 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s143 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s144 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s145 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s146 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s147 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s148 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s149 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s150 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s151 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s152 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s153 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s154 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s155 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s156 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s157 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s158 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s159 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s160 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s161 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s162 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s163 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s164 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s165 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s166 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s167 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s168 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s169 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s170 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s171 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s172 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s173 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s174 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s175 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s176 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s177 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s178 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s179 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s180 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s181 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s182 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s183 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s184 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s185 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s186 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s187 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s188 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s189 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s190 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s191 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s192 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s193 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s194 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s195 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s196 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s197 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s198 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s199 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s200 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s201 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s202 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s203 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s204 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s205 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s206 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s207 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s208 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s209 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s210 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s211 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s212 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s213 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s214 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s215 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s216 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s217 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s218 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s219 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s220 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s221 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s222 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s223 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s224 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s225 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s226 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s227 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s228 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s229 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s230 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s231 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s232 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s233 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s234 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s235 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s236 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s237 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s238 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s239 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s240 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s241 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s242 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s243 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s244 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s245 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s246 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s247 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s248 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s249 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s250 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s251 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s252 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s253 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s254 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s255 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s256 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s257 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s258 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s259 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s260 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s261 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s262 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s263 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s264 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s265 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s266 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s267 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s268 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s269 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s270 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s271 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s272 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s273 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s274 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s275 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s276 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s277 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s278 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s279 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s280 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s281 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s282 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s283 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s284 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s285 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s286 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s287 = Var(within=CannotHandle,bounds=(0,None),initialize=0.0714285714285714)
m.s1s288 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s289 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s290 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s291 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s292 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s293 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s294 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s295 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s296 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s297 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s298 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s299 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s300 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s301 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s302 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s303 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s304 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s305 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s306 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s307 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s308 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s309 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s310 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s311 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s312 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s313 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s314 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s315 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s316 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s317 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s318 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s319 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s320 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s321 = Var(within=CannotHandle,bounds=(0,None),initialize=0)
m.s1s322 = Var(within=CannotHandle,bounds=(0,None),initialize=0)

suffix sosno integer IN;
suffix ref integer IN;
let m.s1s127.sosno := 1;
let m.s1s127.ref   := 1;
let m.s1s128.sosno := 1;
let m.s1s128.ref   := 2;
let m.s1s129.sosno := 1;
let m.s1s129.ref   := 3;
let m.s1s130.sosno := 1;
let m.s1s130.ref   := 4;
let m.s1s131.sosno := 1;
let m.s1s131.ref   := 5;
let m.s1s132.sosno := 1;
let m.s1s132.ref   := 6;
let m.s1s133.sosno := 1;
let m.s1s133.ref   := 7;
let m.s1s134.sosno := 2;
let m.s1s134.ref   := 1;
let m.s1s135.sosno := 2;
let m.s1s135.ref   := 2;
let m.s1s136.sosno := 2;
let m.s1s136.ref   := 3;
let m.s1s137.sosno := 2;
let m.s1s137.ref   := 4;
let m.s1s138.sosno := 2;
let m.s1s138.ref   := 5;
let m.s1s139.sosno := 2;
let m.s1s139.ref   := 6;
let m.s1s140.sosno := 2;
let m.s1s140.ref   := 7;
let m.s1s141.sosno := 3;
let m.s1s141.ref   := 1;
let m.s1s142.sosno := 3;
let m.s1s142.ref   := 2;
let m.s1s143.sosno := 3;
let m.s1s143.ref   := 3;
let m.s1s144.sosno := 3;
let m.s1s144.ref   := 4;
let m.s1s145.sosno := 3;
let m.s1s145.ref   := 5;
let m.s1s146.sosno := 3;
let m.s1s146.ref   := 6;
let m.s1s147.sosno := 3;
let m.s1s147.ref   := 7;
let m.s1s148.sosno := 4;
let m.s1s148.ref   := 1;
let m.s1s149.sosno := 4;
let m.s1s149.ref   := 2;
let m.s1s150.sosno := 4;
let m.s1s150.ref   := 3;
let m.s1s151.sosno := 4;
let m.s1s151.ref   := 4;
let m.s1s152.sosno := 4;
let m.s1s152.ref   := 5;
let m.s1s153.sosno := 4;
let m.s1s153.ref   := 6;
let m.s1s154.sosno := 4;
let m.s1s154.ref   := 7;
let m.s1s155.sosno := 5;
let m.s1s155.ref   := 1;
let m.s1s156.sosno := 5;
let m.s1s156.ref   := 2;
let m.s1s157.sosno := 5;
let m.s1s157.ref   := 3;
let m.s1s158.sosno := 5;
let m.s1s158.ref   := 4;
let m.s1s159.sosno := 5;
let m.s1s159.ref   := 5;
let m.s1s160.sosno := 5;
let m.s1s160.ref   := 6;
let m.s1s161.sosno := 5;
let m.s1s161.ref   := 7;
let m.s1s162.sosno := 6;
let m.s1s162.ref   := 1;
let m.s1s163.sosno := 6;
let m.s1s163.ref   := 2;
let m.s1s164.sosno := 6;
let m.s1s164.ref   := 3;
let m.s1s165.sosno := 6;
let m.s1s165.ref   := 4;
let m.s1s166.sosno := 6;
let m.s1s166.ref   := 5;
let m.s1s167.sosno := 6;
let m.s1s167.ref   := 6;
let m.s1s168.sosno := 6;
let m.s1s168.ref   := 7;
let m.s1s169.sosno := 7;
let m.s1s169.ref   := 1;
let m.s1s170.sosno := 7;
let m.s1s170.ref   := 2;
let m.s1s171.sosno := 7;
let m.s1s171.ref   := 3;
let m.s1s172.sosno := 7;
let m.s1s172.ref   := 4;
let m.s1s173.sosno := 7;
let m.s1s173.ref   := 5;
let m.s1s174.sosno := 7;
let m.s1s174.ref   := 6;
let m.s1s175.sosno := 7;
let m.s1s175.ref   := 7;
let m.s1s176.sosno := 8;
let m.s1s176.ref   := 1;
let m.s1s177.sosno := 8;
let m.s1s177.ref   := 2;
let m.s1s178.sosno := 8;
let m.s1s178.ref   := 3;
let m.s1s179.sosno := 8;
let m.s1s179.ref   := 4;
let m.s1s180.sosno := 8;
let m.s1s180.ref   := 5;
let m.s1s181.sosno := 8;
let m.s1s181.ref   := 6;
let m.s1s182.sosno := 8;
let m.s1s182.ref   := 7;
let m.s1s183.sosno := 9;
let m.s1s183.ref   := 1;
let m.s1s184.sosno := 9;
let m.s1s184.ref   := 2;
let m.s1s185.sosno := 9;
let m.s1s185.ref   := 3;
let m.s1s186.sosno := 9;
let m.s1s186.ref   := 4;
let m.s1s187.sosno := 9;
let m.s1s187.ref   := 5;
let m.s1s188.sosno := 9;
let m.s1s188.ref   := 6;
let m.s1s189.sosno := 9;
let m.s1s189.ref   := 7;
let m.s1s190.sosno := 10;
let m.s1s190.ref   := 1;
let m.s1s191.sosno := 10;
let m.s1s191.ref   := 2;
let m.s1s192.sosno := 10;
let m.s1s192.ref   := 3;
let m.s1s193.sosno := 10;
let m.s1s193.ref   := 4;
let m.s1s194.sosno := 10;
let m.s1s194.ref   := 5;
let m.s1s195.sosno := 10;
let m.s1s195.ref   := 6;
let m.s1s196.sosno := 10;
let m.s1s196.ref   := 7;
let m.s1s197.sosno := 11;
let m.s1s197.ref   := 1;
let m.s1s198.sosno := 11;
let m.s1s198.ref   := 2;
let m.s1s199.sosno := 11;
let m.s1s199.ref   := 3;
let m.s1s200.sosno := 11;
let m.s1s200.ref   := 4;
let m.s1s201.sosno := 11;
let m.s1s201.ref   := 5;
let m.s1s202.sosno := 11;
let m.s1s202.ref   := 6;
let m.s1s203.sosno := 11;
let m.s1s203.ref   := 7;
let m.s1s204.sosno := 12;
let m.s1s204.ref   := 1;
let m.s1s205.sosno := 12;
let m.s1s205.ref   := 2;
let m.s1s206.sosno := 12;
let m.s1s206.ref   := 3;
let m.s1s207.sosno := 12;
let m.s1s207.ref   := 4;
let m.s1s208.sosno := 12;
let m.s1s208.ref   := 5;
let m.s1s209.sosno := 12;
let m.s1s209.ref   := 6;
let m.s1s210.sosno := 12;
let m.s1s210.ref   := 7;
let m.s1s211.sosno := 13;
let m.s1s211.ref   := 1;
let m.s1s212.sosno := 13;
let m.s1s212.ref   := 2;
let m.s1s213.sosno := 13;
let m.s1s213.ref   := 3;
let m.s1s214.sosno := 13;
let m.s1s214.ref   := 4;
let m.s1s215.sosno := 13;
let m.s1s215.ref   := 5;
let m.s1s216.sosno := 13;
let m.s1s216.ref   := 6;
let m.s1s217.sosno := 13;
let m.s1s217.ref   := 7;
let m.s1s218.sosno := 14;
let m.s1s218.ref   := 1;
let m.s1s219.sosno := 14;
let m.s1s219.ref   := 2;
let m.s1s220.sosno := 14;
let m.s1s220.ref   := 3;
let m.s1s221.sosno := 14;
let m.s1s221.ref   := 4;
let m.s1s222.sosno := 14;
let m.s1s222.ref   := 5;
let m.s1s223.sosno := 14;
let m.s1s223.ref   := 6;
let m.s1s224.sosno := 14;
let m.s1s224.ref   := 7;
let m.s1s225.sosno := 15;
let m.s1s225.ref   := 1;
let m.s1s226.sosno := 15;
let m.s1s226.ref   := 2;
let m.s1s227.sosno := 15;
let m.s1s227.ref   := 3;
let m.s1s228.sosno := 15;
let m.s1s228.ref   := 4;
let m.s1s229.sosno := 15;
let m.s1s229.ref   := 5;
let m.s1s230.sosno := 15;
let m.s1s230.ref   := 6;
let m.s1s231.sosno := 15;
let m.s1s231.ref   := 7;
let m.s1s232.sosno := 16;
let m.s1s232.ref   := 1;
let m.s1s233.sosno := 16;
let m.s1s233.ref   := 2;
let m.s1s234.sosno := 16;
let m.s1s234.ref   := 3;
let m.s1s235.sosno := 16;
let m.s1s235.ref   := 4;
let m.s1s236.sosno := 16;
let m.s1s236.ref   := 5;
let m.s1s237.sosno := 16;
let m.s1s237.ref   := 6;
let m.s1s238.sosno := 16;
let m.s1s238.ref   := 7;
let m.s1s239.sosno := 17;
let m.s1s239.ref   := 1;
let m.s1s240.sosno := 17;
let m.s1s240.ref   := 2;
let m.s1s241.sosno := 17;
let m.s1s241.ref   := 3;
let m.s1s242.sosno := 17;
let m.s1s242.ref   := 4;
let m.s1s243.sosno := 17;
let m.s1s243.ref   := 5;
let m.s1s244.sosno := 17;
let m.s1s244.ref   := 6;
let m.s1s245.sosno := 17;
let m.s1s245.ref   := 7;
let m.s1s246.sosno := 18;
let m.s1s246.ref   := 1;
let m.s1s247.sosno := 18;
let m.s1s247.ref   := 2;
let m.s1s248.sosno := 18;
let m.s1s248.ref   := 3;
let m.s1s249.sosno := 18;
let m.s1s249.ref   := 4;
let m.s1s250.sosno := 18;
let m.s1s250.ref   := 5;
let m.s1s251.sosno := 18;
let m.s1s251.ref   := 6;
let m.s1s252.sosno := 18;
let m.s1s252.ref   := 7;
let m.s1s253.sosno := 19;
let m.s1s253.ref   := 1;
let m.s1s254.sosno := 19;
let m.s1s254.ref   := 2;
let m.s1s255.sosno := 19;
let m.s1s255.ref   := 3;
let m.s1s256.sosno := 19;
let m.s1s256.ref   := 4;
let m.s1s257.sosno := 19;
let m.s1s257.ref   := 5;
let m.s1s258.sosno := 19;
let m.s1s258.ref   := 6;
let m.s1s259.sosno := 19;
let m.s1s259.ref   := 7;
let m.s1s260.sosno := 20;
let m.s1s260.ref   := 1;
let m.s1s261.sosno := 20;
let m.s1s261.ref   := 2;
let m.s1s262.sosno := 20;
let m.s1s262.ref   := 3;
let m.s1s263.sosno := 20;
let m.s1s263.ref   := 4;
let m.s1s264.sosno := 20;
let m.s1s264.ref   := 5;
let m.s1s265.sosno := 20;
let m.s1s265.ref   := 6;
let m.s1s266.sosno := 20;
let m.s1s266.ref   := 7;
let m.s1s267.sosno := 21;
let m.s1s267.ref   := 1;
let m.s1s268.sosno := 21;
let m.s1s268.ref   := 2;
let m.s1s269.sosno := 21;
let m.s1s269.ref   := 3;
let m.s1s270.sosno := 21;
let m.s1s270.ref   := 4;
let m.s1s271.sosno := 21;
let m.s1s271.ref   := 5;
let m.s1s272.sosno := 21;
let m.s1s272.ref   := 6;
let m.s1s273.sosno := 21;
let m.s1s273.ref   := 7;
let m.s1s274.sosno := 22;
let m.s1s274.ref   := 1;
let m.s1s275.sosno := 22;
let m.s1s275.ref   := 2;
let m.s1s276.sosno := 22;
let m.s1s276.ref   := 3;
let m.s1s277.sosno := 22;
let m.s1s277.ref   := 4;
let m.s1s278.sosno := 22;
let m.s1s278.ref   := 5;
let m.s1s279.sosno := 22;
let m.s1s279.ref   := 6;
let m.s1s280.sosno := 22;
let m.s1s280.ref   := 7;
let m.s1s281.sosno := 23;
let m.s1s281.ref   := 1;
let m.s1s282.sosno := 23;
let m.s1s282.ref   := 2;
let m.s1s283.sosno := 23;
let m.s1s283.ref   := 3;
let m.s1s284.sosno := 23;
let m.s1s284.ref   := 4;
let m.s1s285.sosno := 23;
let m.s1s285.ref   := 5;
let m.s1s286.sosno := 23;
let m.s1s286.ref   := 6;
let m.s1s287.sosno := 23;
let m.s1s287.ref   := 7;
let m.s1s288.sosno := 24;
let m.s1s288.ref   := 1;
let m.s1s289.sosno := 24;
let m.s1s289.ref   := 2;
let m.s1s290.sosno := 24;
let m.s1s290.ref   := 3;
let m.s1s291.sosno := 24;
let m.s1s291.ref   := 4;
let m.s1s292.sosno := 24;
let m.s1s292.ref   := 5;
let m.s1s293.sosno := 24;
let m.s1s293.ref   := 6;
let m.s1s294.sosno := 24;
let m.s1s294.ref   := 7;
let m.s1s295.sosno := 25;
let m.s1s295.ref   := 1;
let m.s1s296.sosno := 25;
let m.s1s296.ref   := 2;
let m.s1s297.sosno := 25;
let m.s1s297.ref   := 3;
let m.s1s298.sosno := 25;
let m.s1s298.ref   := 4;
let m.s1s299.sosno := 25;
let m.s1s299.ref   := 5;
let m.s1s300.sosno := 25;
let m.s1s300.ref   := 6;
let m.s1s301.sosno := 25;
let m.s1s301.ref   := 7;
let m.s1s302.sosno := 26;
let m.s1s302.ref   := 1;
let m.s1s303.sosno := 26;
let m.s1s303.ref   := 2;
let m.s1s304.sosno := 26;
let m.s1s304.ref   := 3;
let m.s1s305.sosno := 26;
let m.s1s305.ref   := 4;
let m.s1s306.sosno := 26;
let m.s1s306.ref   := 5;
let m.s1s307.sosno := 26;
let m.s1s307.ref   := 6;
let m.s1s308.sosno := 26;
let m.s1s308.ref   := 7;
let m.s1s309.sosno := 27;
let m.s1s309.ref   := 1;
let m.s1s310.sosno := 27;
let m.s1s310.ref   := 2;
let m.s1s311.sosno := 27;
let m.s1s311.ref   := 3;
let m.s1s312.sosno := 27;
let m.s1s312.ref   := 4;
let m.s1s313.sosno := 27;
let m.s1s313.ref   := 5;
let m.s1s314.sosno := 27;
let m.s1s314.ref   := 6;
let m.s1s315.sosno := 27;
let m.s1s315.ref   := 7;
let m.s1s316.sosno := 28;
let m.s1s316.ref   := 1;
let m.s1s317.sosno := 28;
let m.s1s317.ref   := 2;
let m.s1s318.sosno := 28;
let m.s1s318.ref   := 3;
let m.s1s319.sosno := 28;
let m.s1s319.ref   := 4;
let m.s1s320.sosno := 28;
let m.s1s320.ref   := 5;
let m.s1s321.sosno := 28;
let m.s1s321.ref   := 6;
let m.s1s322.sosno := 28;
let m.s1s322.ref   := 7;

m.obj = Objective(expr=   10*m.x95 + m.x96 + 10*m.x97, sense=minimize)

m.c1 = Constraint(expr= - m.x1 - m.x2 - m.x3 + m.x8 + m.x14 + m.x26 + m.x93 == 0)

m.c2 = Constraint(expr= - m.x4 - m.x5 - m.x6 - m.x7 + m.x9 + m.x20 + m.x24 + m.x27 + m.x94 == 0)

m.c3 = Constraint(expr=   m.x1 + m.x4 - m.x8 - m.x9 - m.x10 - m.x11 - m.x12 - m.x13 + m.x15 + m.x17 + m.x21 + m.x28
                        == 1.212)

m.c4 = Constraint(expr=   m.x2 + m.x10 - m.x14 - m.x15 - m.x16 + m.x18 == 0.452)

m.c5 = Constraint(expr=   m.x11 + m.x16 - m.x17 - m.x18 - m.x19 + m.x22 == 0.245)

m.c6 = Constraint(expr=   m.x5 + m.x12 + m.x19 - m.x20 - m.x21 - m.x22 - m.x23 + m.x25 == 0.652)

m.c7 = Constraint(expr=   m.x6 + m.x23 - m.x24 - m.x25 == 0.252)

m.c8 = Constraint(expr=   m.x3 + m.x7 + m.x13 - m.x26 - m.x27 - m.x28 == 0.456)

m.c9 = Constraint(expr=   m.x29 - 38721.1970117411*m.s1s127 - 2543.8701482414*m.s1s128 - 207.747320703761*m.s1s129
                        - 23.9314504121258*m.s1s130 - 1.5722267648148*m.s1s131 - 0.181112645550961*m.s1s132
                        - 0.0390863672545667*m.s1s133 == 0)

m.c10 = Constraint(expr=   m.x30 - 32510.4890865135*m.s1s134 - 2135.84468132099*m.s1s135 - 174.425573683688*m.s1s136
                         - 20.0929521164322*m.s1s137 - 1.32004857865156*m.s1s138 - 0.152062982061963*m.s1s139
                         - 0.0328170876451919*m.s1s140 == 0)

m.c11 = Constraint(expr=   m.x31 - 63468.4628982673*m.s1s141 - 4169.69361956223*m.s1s142 - 340.521578201805*m.s1s143
                         - 39.2263796008983*m.s1s144 - 2.57705917665854*m.s1s145 - 0.296864304610023*m.s1s146
                         - 0.0640670186196026*m.s1s147 == 0)

m.c12 = Constraint(expr=   m.x32 - 50797.5773435889*m.s1s148 - 3337.25325093014*m.s1s149 - 272.539627020641*m.s1s150
                         - 31.3951994533022*m.s1s151 - 2.06257339263358*m.s1s152 - 0.237598120158509*m.s1s153
                         - 0.0512766370081929*m.s1s154 == 0)

m.c13 = Constraint(expr=   m.x33 - 59165.7349698592*m.s1s155 - 3887.01689524085*m.s1s156 - 317.436542928413*m.s1s157
                         - 36.5670992066393*m.s1s158 - 2.40235218067626*m.s1s159 - 0.27673893405488*m.s1s160
                         - 0.0597237127048799*m.s1s161 == 0)

m.c14 = Constraint(expr=   m.x34 - 32977.2294678044*m.s1s162 - 2166.50816836621*m.s1s163 - 176.929733450444*m.s1s164
                         - 20.3814187742893*m.s1s165 - 1.339*m.s1s166 - 0.154246090843839*m.s1s167
                         - 0.0332882297421199*m.s1s168 == 0)

m.c15 = Constraint(expr=   m.x35 - 33843.9321019273*m.s1s169 - 2223.4480134252*m.s1s170 - 181.579774357788*m.s1s171
                         - 20.9170801874496*m.s1s172 - 1.37419139860501*m.s1s173 - 0.158299963634093*m.s1s174
                         - 0.0341631060391402*m.s1s175 == 0)

m.c16 = Constraint(expr=   m.x36 - 38721.1970117411*m.s1s176 - 2543.8701482414*m.s1s177 - 207.747320703761*m.s1s178
                         - 23.9314504121258*m.s1s179 - 1.5722267648148*m.s1s180 - 0.181112645550961*m.s1s181
                         - 0.0390863672545667*m.s1s182 == 0)

m.c17 = Constraint(expr=   m.x37 - 50797.5773435889*m.s1s183 - 3337.25325093014*m.s1s184 - 272.539627020641*m.s1s185
                         - 31.3951994533022*m.s1s186 - 2.06257339263358*m.s1s187 - 0.237598120158509*m.s1s188
                         - 0.0512766370081929*m.s1s189 == 0)

m.c18 = Constraint(expr=   m.x38 - 31810.181054648*m.s1s190 - 2089.8364782095*m.s1s191 - 170.668274619734*m.s1s192
                         - 19.660130090483*m.s1s193 - 1.2916134290104*m.s1s194 - 0.148787395299671*m.s1s195
                         - 0.0321101751776739*m.s1s196 == 0)

m.c19 = Constraint(expr=   m.x39 - 39461.9459070343*m.s1s197 - 2592.53519858857*m.s1s198 - 211.721593458417*m.s1s199
                         - 24.3892667200816*m.s1s200 - 1.60230396616872*m.s1s201 - 0.184577388442944*m.s1s202
                         - 0.0398341019735132*m.s1s203 == 0)

m.c20 = Constraint(expr=   m.x40 - 32977.2294678044*m.s1s204 - 2166.50816836621*m.s1s205 - 176.929733450444*m.s1s206
                         - 20.3814187742893*m.s1s207 - 1.339*m.s1s208 - 0.154246090843839*m.s1s209
                         - 0.0332882297421199*m.s1s210 == 0)

m.c21 = Constraint(expr=   m.x41 - 52785.5148814787*m.s1s211 - 3467.85497167945*m.s1s212 - 283.205327698691*m.s1s213
                         - 32.6238347301504*m.s1s214 - 2.14329116080854*m.s1s215 - 0.246896402610059*m.s1s216
                         - 0.0532833223041444*m.s1s217 == 0)

m.c22 = Constraint(expr=   m.x42 - 32510.4890865135*m.s1s218 - 2135.84468132099*m.s1s219 - 174.425573683688*m.s1s220
                         - 20.0929521164322*m.s1s221 - 1.32004857865156*m.s1s222 - 0.152062982061963*m.s1s223
                         - 0.0328170876451919*m.s1s224 == 0)

m.c23 = Constraint(expr=   m.x43 - 31810.181054648*m.s1s225 - 2089.8364782095*m.s1s226 - 170.668274619734*m.s1s227
                         - 19.660130090483*m.s1s228 - 1.2916134290104*m.s1s229 - 0.148787395299671*m.s1s230
                         - 0.0321101751776739*m.s1s231 == 0)

m.c24 = Constraint(expr=   m.x44 - 30677.4142839491*m.s1s232 - 2015.41699236491*m.s1s233 - 164.590743970989*m.s1s234
                         - 18.9600290116536*m.s1s235 - 1.24561882211213*m.s1s236 - 0.143489047044288*m.s1s237
                         - 0.0309667255575633*m.s1s238 == 0)

m.c25 = Constraint(expr=   m.x45 - 39461.9459070343*m.s1s239 - 2592.53519858857*m.s1s240 - 211.721593458417*m.s1s241
                         - 24.3892667200816*m.s1s242 - 1.60230396616872*m.s1s243 - 0.184577388442944*m.s1s244
                         - 0.0398341019735132*m.s1s245 == 0)

m.c26 = Constraint(expr=   m.x46 - 30677.4142839491*m.s1s246 - 2015.41699236491*m.s1s247 - 164.590743970989*m.s1s248
                         - 18.9600290116536*m.s1s249 - 1.24561882211213*m.s1s250 - 0.143489047044288*m.s1s251
                         - 0.0309667255575633*m.s1s252 == 0)

m.c27 = Constraint(expr=   m.x47 - 28361.2795383154*m.s1s253 - 1863.25366856746*m.s1s254 - 152.164196629274*m.s1s255
                         - 17.5285530220005*m.s1s256 - 1.15157500841239*m.s1s257 - 0.132655670919396*m.s1s258
                         - 0.0286287479053886*m.s1s259 == 0)

m.c28 = Constraint(expr=   m.x48 - 59165.7349698592*m.s1s260 - 3887.01689524085*m.s1s261 - 317.436542928413*m.s1s262
                         - 36.5670992066393*m.s1s263 - 2.40235218067626*m.s1s264 - 0.27673893405488*m.s1s265
                         - 0.0597237127048799*m.s1s266 == 0)

m.c29 = Constraint(expr=   m.x49 - 32977.2294678044*m.s1s267 - 2166.50816836621*m.s1s268 - 176.929733450444*m.s1s269
                         - 20.3814187742893*m.s1s270 - 1.339*m.s1s271 - 0.154246090843839*m.s1s272
                         - 0.0332882297421199*m.s1s273 == 0)

m.c30 = Constraint(expr=   m.x50 - 28361.2795383154*m.s1s274 - 1863.25366856746*m.s1s275 - 152.164196629274*m.s1s276
                         - 17.5285530220005*m.s1s277 - 1.15157500841239*m.s1s278 - 0.132655670919396*m.s1s279
                         - 0.0286287479053886*m.s1s280 == 0)

m.c31 = Constraint(expr=   m.x51 - 50797.5773435889*m.s1s281 - 3337.25325093014*m.s1s282 - 272.539627020641*m.s1s283
                         - 31.3951994533022*m.s1s284 - 2.06257339263358*m.s1s285 - 0.237598120158509*m.s1s286
                         - 0.0512766370081929*m.s1s287 == 0)

m.c32 = Constraint(expr=   m.x52 - 32977.2294678044*m.s1s288 - 2166.50816836621*m.s1s289 - 176.929733450444*m.s1s290
                         - 20.3814187742893*m.s1s291 - 1.339*m.s1s292 - 0.154246090843839*m.s1s293
                         - 0.0332882297421199*m.s1s294 == 0)

m.c33 = Constraint(expr=   m.x53 - 50797.5773435889*m.s1s295 - 3337.25325093014*m.s1s296 - 272.539627020641*m.s1s297
                         - 31.3951994533022*m.s1s298 - 2.06257339263358*m.s1s299 - 0.237598120158509*m.s1s300
                         - 0.0512766370081929*m.s1s301 == 0)

m.c34 = Constraint(expr=   m.x54 - 63468.4628982673*m.s1s302 - 4169.69361956223*m.s1s303 - 340.521578201805*m.s1s304
                         - 39.2263796008983*m.s1s305 - 2.57705917665854*m.s1s306 - 0.296864304610023*m.s1s307
                         - 0.0640670186196026*m.s1s308 == 0)

m.c35 = Constraint(expr=   m.x55 - 33843.9321019273*m.s1s309 - 2223.4480134252*m.s1s310 - 181.579774357788*m.s1s311
                         - 20.9170801874496*m.s1s312 - 1.37419139860501*m.s1s313 - 0.158299963634093*m.s1s314
                         - 0.0341631060391402*m.s1s315 == 0)

m.c36 = Constraint(expr=   m.x56 - 52785.5148814787*m.s1s316 - 3467.85497167945*m.s1s317 - 283.205327698691*m.s1s318
                         - 32.6238347301504*m.s1s319 - 2.14329116080854*m.s1s320 - 0.246896402610059*m.s1s321
                         - 0.0532833223041444*m.s1s322 == 0)

m.c37 = Constraint(expr=-m.x1**2*m.x29 + m.x57 - m.x59 - m.x65 == 0)

m.c38 = Constraint(expr=-m.x2**2*m.x30 + m.x57 - m.x60 - m.x66 == 0)

m.c39 = Constraint(expr=-m.x3**2*m.x31 + m.x57 - m.x64 - m.x67 == 0)

m.c40 = Constraint(expr=-m.x4**2*m.x32 + m.x58 - m.x59 - m.x68 == 0)

m.c41 = Constraint(expr=-m.x5**2*m.x33 + m.x58 - m.x62 - m.x69 == 0)

m.c42 = Constraint(expr=-m.x6**2*m.x34 + m.x58 - m.x63 - m.x70 == 0)

m.c43 = Constraint(expr=-m.x7**2*m.x35 + m.x58 - m.x64 - m.x71 == 0)

m.c44 = Constraint(expr=-m.x8**2*m.x36 - m.x57 + m.x59 - m.x72 == 0)

m.c45 = Constraint(expr=-m.x9**2*m.x37 - m.x58 + m.x59 - m.x73 == 0)

m.c46 = Constraint(expr=-m.x10**2*m.x38 + m.x59 - m.x60 - m.x74 == 0)

m.c47 = Constraint(expr=-m.x11**2*m.x39 + m.x59 - m.x61 - m.x75 == 0)

m.c48 = Constraint(expr=-m.x12**2*m.x40 + m.x59 - m.x62 - m.x76 == 0)

m.c49 = Constraint(expr=-m.x13**2*m.x41 + m.x59 - m.x64 - m.x77 == 0)

m.c50 = Constraint(expr=-m.x14**2*m.x42 - m.x57 + m.x60 - m.x78 == 0)

m.c51 = Constraint(expr=-m.x15**2*m.x43 - m.x59 + m.x60 - m.x79 == 0)

m.c52 = Constraint(expr=-m.x16**2*m.x44 + m.x60 - m.x61 - m.x80 == 0)

m.c53 = Constraint(expr=-m.x17**2*m.x45 - m.x59 + m.x61 - m.x81 == 0)

m.c54 = Constraint(expr=-m.x18**2*m.x46 - m.x60 + m.x61 - m.x82 == 0)

m.c55 = Constraint(expr=-m.x19**2*m.x47 + m.x61 - m.x62 - m.x83 == 0)

m.c56 = Constraint(expr=-m.x20**2*m.x48 - m.x58 + m.x62 - m.x84 == 0)

m.c57 = Constraint(expr=-m.x21**2*m.x49 - m.x59 + m.x62 - m.x85 == 0)

m.c58 = Constraint(expr=-m.x22**2*m.x50 - m.x61 + m.x62 - m.x86 == 0)

m.c59 = Constraint(expr=-m.x23**2*m.x51 + m.x62 - m.x63 - m.x87 == 0)

m.c60 = Constraint(expr=-m.x24**2*m.x52 - m.x58 + m.x63 - m.x88 == 0)

m.c61 = Constraint(expr=-m.x25**2*m.x53 - m.x62 + m.x63 - m.x89 == 0)

m.c62 = Constraint(expr=-m.x26**2*m.x54 - m.x57 + m.x64 - m.x90 == 0)

m.c63 = Constraint(expr=-m.x27**2*m.x55 - m.x58 + m.x64 - m.x91 == 0)

m.c64 = Constraint(expr=-m.x28**2*m.x56 - m.x59 + m.x64 - m.x92 == 0)

m.c65 = Constraint(expr=   m.x65 + 12*m.b99 <= 12)

m.c66 = Constraint(expr=   m.x66 + 12*m.b100 <= 12)

m.c67 = Constraint(expr=   m.x67 + 12*m.b101 <= 12)

m.c68 = Constraint(expr=   m.x68 + 12*m.b102 <= 12)

m.c69 = Constraint(expr=   m.x69 + 12*m.b103 <= 12)

m.c70 = Constraint(expr=   m.x70 + 12*m.b104 <= 12)

m.c71 = Constraint(expr=   m.x71 + 12*m.b105 <= 12)

m.c72 = Constraint(expr=   m.x72 + 12*m.b106 <= 12)

m.c73 = Constraint(expr=   m.x73 + 12*m.b107 <= 12)

m.c74 = Constraint(expr=   m.x74 + 12*m.b108 <= 12)

m.c75 = Constraint(expr=   m.x75 + 12*m.b109 <= 12)

m.c76 = Constraint(expr=   m.x76 + 12*m.b110 <= 12)

m.c77 = Constraint(expr=   m.x77 + 12*m.b111 <= 12)

m.c78 = Constraint(expr=   m.x78 + 12*m.b112 <= 12)

m.c79 = Constraint(expr=   m.x79 + 12*m.b113 <= 12)

m.c80 = Constraint(expr=   m.x80 + 12*m.b114 <= 12)

m.c81 = Constraint(expr=   m.x81 + 12*m.b115 <= 12)

m.c82 = Constraint(expr=   m.x82 + 12*m.b116 <= 12)

m.c83 = Constraint(expr=   m.x83 + 12*m.b117 <= 12)

m.c84 = Constraint(expr=   m.x84 + 12*m.b118 <= 12)

m.c85 = Constraint(expr=   m.x85 + 12*m.b119 <= 12)

m.c86 = Constraint(expr=   m.x86 + 12*m.b120 <= 12)

m.c87 = Constraint(expr=   m.x87 + 12*m.b121 <= 12)

m.c88 = Constraint(expr=   m.x88 + 12*m.b122 <= 12)

m.c89 = Constraint(expr=   m.x89 + 12*m.b123 <= 12)

m.c90 = Constraint(expr=   m.x90 + 12*m.b124 <= 12)

m.c91 = Constraint(expr=   m.x91 + 12*m.b125 <= 12)

m.c92 = Constraint(expr=   m.x92 + 12*m.b126 <= 12)

m.c93 = Constraint(expr=   m.x65 - 12*m.b99 >= -12)

m.c94 = Constraint(expr=   m.x66 - 12*m.b100 >= -12)

m.c95 = Constraint(expr=   m.x67 - 12*m.b101 >= -12)

m.c96 = Constraint(expr=   m.x68 - 12*m.b102 >= -12)

m.c97 = Constraint(expr=   m.x69 - 12*m.b103 >= -12)

m.c98 = Constraint(expr=   m.x70 - 12*m.b104 >= -12)

m.c99 = Constraint(expr=   m.x71 - 12*m.b105 >= -12)

m.c100 = Constraint(expr=   m.x72 - 12*m.b106 >= -12)

m.c101 = Constraint(expr=   m.x73 - 12*m.b107 >= -12)

m.c102 = Constraint(expr=   m.x74 - 12*m.b108 >= -12)

m.c103 = Constraint(expr=   m.x75 - 12*m.b109 >= -12)

m.c104 = Constraint(expr=   m.x76 - 12*m.b110 >= -12)

m.c105 = Constraint(expr=   m.x77 - 12*m.b111 >= -12)

m.c106 = Constraint(expr=   m.x78 - 12*m.b112 >= -12)

m.c107 = Constraint(expr=   m.x79 - 12*m.b113 >= -12)

m.c108 = Constraint(expr=   m.x80 - 12*m.b114 >= -12)

m.c109 = Constraint(expr=   m.x81 - 12*m.b115 >= -12)

m.c110 = Constraint(expr=   m.x82 - 12*m.b116 >= -12)

m.c111 = Constraint(expr=   m.x83 - 12*m.b117 >= -12)

m.c112 = Constraint(expr=   m.x84 - 12*m.b118 >= -12)

m.c113 = Constraint(expr=   m.x85 - 12*m.b119 >= -12)

m.c114 = Constraint(expr=   m.x86 - 12*m.b120 >= -12)

m.c115 = Constraint(expr=   m.x87 - 12*m.b121 >= -12)

m.c116 = Constraint(expr=   m.x88 - 12*m.b122 >= -12)

m.c117 = Constraint(expr=   m.x89 - 12*m.b123 >= -12)

m.c118 = Constraint(expr=   m.x90 - 12*m.b124 >= -12)

m.c119 = Constraint(expr=   m.x91 - 12*m.b125 >= -12)

m.c120 = Constraint(expr=   m.x92 - 12*m.b126 >= -12)

m.c121 = Constraint(expr=-(1.02*m.x93*(-6.5 + m.x57) + 1.02*m.x94*(-3.25 + m.x58)) + m.x95 == 0)

m.c122 = Constraint(expr=   m.x96 - 9.11349113439539*m.s1s127 - 17.6144733325531*m.s1s128 - 32.2986551864818*m.s1s129
                          - 54.4931814987685*m.s1s130 - 105.323928905069*m.s1s131 - 177.698914733437*m.s1s132
                          - 257.546555368226*m.s1s133 - 7.65172765642961*m.s1s134 - 14.7891900880288*m.s1s135
                          - 27.118094428506*m.s1s136 - 45.7527173518919*m.s1s137 - 88.4304387640365*m.s1s138
                          - 149.196798497086*m.s1s139 - 216.237232413786*m.s1s140 - 14.9380525029139*m.s1s141
                          - 28.8721329260735*m.s1s142 - 52.941183552398*m.s1s143 - 89.3205462402005*m.s1s144
                          - 172.637944844116*m.s1s145 - 291.268810037089*m.s1s146 - 422.148209648796*m.s1s147
                          - 11.9558099050809*m.s1s148 - 23.1080813747994*m.s1s149 - 42.3719709499612*m.s1s150
                          - 71.4885338137291*m.s1s151 - 138.172392322055*m.s1s152 - 233.119713791557*m.s1s153
                          - 337.870264236031*m.s1s154 - 13.9253546563734*m.s1s155 - 26.9147996770731*m.s1s156
                          - 49.3521332015331*m.s1s157 - 83.2652237802191*m.s1s158 - 160.93427229773*m.s1s159
                          - 271.522775764452*m.s1s160 - 393.529446744536*m.s1s161 - 7.76158051882097*m.s1s162
                          - 15.0015127080393*m.s1s163 - 27.5074183079396*m.s1s164 - 46.4095712271164*m.s1s165
                          - 89.7*m.s1s166 - 151.338758602103*m.s1s167 - 219.341665817957*m.s1s168
                          - 7.96556922221359*m.s1s169 - 15.3957802311063*m.s1s170 - 28.2303641796868*m.s1s171
                          - 47.6293006671023*m.s1s172 - 92.0574820424717*m.s1s173 - 155.316221319321*m.s1s174
                          - 225.10637081608*m.s1s175 - 9.11349113439539*m.s1s176 - 17.6144733325531*m.s1s177
                          - 32.2986551864818*m.s1s178 - 54.4931814987685*m.s1s179 - 105.323928905069*m.s1s180
                          - 177.698914733437*m.s1s181 - 257.546555368226*m.s1s182 - 11.9558099050809*m.s1s183
                          - 23.1080813747994*m.s1s184 - 42.3719709499612*m.s1s185 - 71.4885338137291*m.s1s186
                          - 138.172392322055*m.s1s187 - 233.119713791557*m.s1s188 - 337.870264236031*m.s1s189
                          - 7.48690188831565*m.s1s190 - 14.4706163324673*m.s1s191 - 26.5339439013751*m.s1s192
                          - 44.7671586494086*m.s1s193 - 86.5255598074927*m.s1s194 - 145.982952158506*m.s1s195
                          - 211.579268940989*m.s1s196 - 9.28783513744935*m.s1s197 - 17.9514438466182*m.s1s198
                          - 32.916538800503*m.s1s199 - 55.5356535066454*m.s1s200 - 107.338809384118*m.s1s201
                          - 181.098351861986*m.s1s202 - 262.473503425068*m.s1s203 - 7.76158051882097*m.s1s204
                          - 15.0015127080393*m.s1s205 - 27.5074183079396*m.s1s206 - 46.4095712271164*m.s1s207
                          - 89.7*m.s1s208 - 151.338758602103*m.s1s209 - 219.341665817957*m.s1s210
                          - 12.4236944883441*m.s1s211 - 24.0124044704238*m.s1s212 - 44.0301766363479*m.s1s213
                          - 74.2862014846846*m.s1s214 - 143.579699122125*m.s1s215 - 242.242736071415*m.s1s216
                          - 351.092646411238*m.s1s217 - 7.65172765642961*m.s1s218 - 14.7891900880288*m.s1s219
                          - 27.118094428506*m.s1s220 - 45.7527173518919*m.s1s221 - 88.4304387640365*m.s1s222
                          - 149.196798497086*m.s1s223 - 216.237232413786*m.s1s224 - 7.48690188831565*m.s1s225
                          - 14.4706163324673*m.s1s226 - 26.5339439013751*m.s1s227 - 44.7671586494086*m.s1s228
                          - 86.5255598074927*m.s1s229 - 145.982952158506*m.s1s230 - 211.579268940989*m.s1s231
                          - 7.22029184733547*m.s1s232 - 13.9553148538372*m.s1s233 - 25.5890649679471*m.s1s234
                          - 43.1729913716576*m.s1s235 - 83.44436769489*m.s1s236 - 140.784470672041*m.s1s237
                          - 204.044889780639*m.s1s238 - 9.28783513744935*m.s1s239 - 17.9514438466182*m.s1s240
                          - 32.916538800503*m.s1s241 - 55.5356535066454*m.s1s242 - 107.338809384118*m.s1s243
                          - 181.098351861986*m.s1s244 - 262.473503425068*m.s1s245 - 7.22029184733547*m.s1s246
                          - 13.9553148538372*m.s1s247 - 25.5890649679471*m.s1s248 - 43.1729913716576*m.s1s249
                          - 83.44436769489*m.s1s250 - 140.784470672041*m.s1s251 - 204.044889780639*m.s1s252
                          - 6.67516217420068*m.s1s253 - 12.9016931463472*m.s1s254 - 23.6570989315674*m.s1s255
                          - 39.913444642481*m.s1s256 - 77.1443452237428*m.s1s257 - 130.155289178744*m.s1s258
                          - 188.639567333459*m.s1s259 - 13.9253546563734*m.s1s260 - 26.9147996770731*m.s1s261
                          - 49.3521332015331*m.s1s262 - 83.2652237802191*m.s1s263 - 160.93427229773*m.s1s264
                          - 271.522775764452*m.s1s265 - 393.529446744536*m.s1s266 - 7.76158051882097*m.s1s267
                          - 15.0015127080393*m.s1s268 - 27.5074183079396*m.s1s269 - 46.4095712271164*m.s1s270
                          - 89.7*m.s1s271 - 151.338758602103*m.s1s272 - 219.341665817957*m.s1s273
                          - 6.67516217420068*m.s1s274 - 12.9016931463472*m.s1s275 - 23.6570989315674*m.s1s276
                          - 39.913444642481*m.s1s277 - 77.1443452237428*m.s1s278 - 130.155289178744*m.s1s279
                          - 188.639567333459*m.s1s280 - 11.9558099050809*m.s1s281 - 23.1080813747994*m.s1s282
                          - 42.3719709499612*m.s1s283 - 71.4885338137291*m.s1s284 - 138.172392322055*m.s1s285
                          - 233.119713791557*m.s1s286 - 337.870264236031*m.s1s287 - 7.76158051882097*m.s1s288
                          - 15.0015127080393*m.s1s289 - 27.5074183079396*m.s1s290 - 46.4095712271164*m.s1s291
                          - 89.7*m.s1s292 - 151.338758602103*m.s1s293 - 219.341665817957*m.s1s294
                          - 11.9558099050809*m.s1s295 - 23.1080813747994*m.s1s296 - 42.3719709499612*m.s1s297
                          - 71.4885338137291*m.s1s298 - 138.172392322055*m.s1s299 - 233.119713791557*m.s1s300
                          - 337.870264236031*m.s1s301 - 14.9380525029139*m.s1s302 - 28.8721329260735*m.s1s303
                          - 52.941183552398*m.s1s304 - 89.3205462402005*m.s1s305 - 172.637944844116*m.s1s306
                          - 291.268810037089*m.s1s307 - 422.148209648796*m.s1s308 - 7.96556922221359*m.s1s309
                          - 15.3957802311063*m.s1s310 - 28.2303641796868*m.s1s311 - 47.6293006671023*m.s1s312
                          - 92.0574820424717*m.s1s313 - 155.316221319321*m.s1s314 - 225.10637081608*m.s1s315
                          - 12.4236944883441*m.s1s316 - 24.0124044704238*m.s1s317 - 44.0301766363479*m.s1s318
                          - 74.2862014846846*m.s1s319 - 143.579699122125*m.s1s320 - 242.242736071415*m.s1s321
                          - 351.092646411238*m.s1s322 == 0)

m.c123 = Constraint(expr= - 0.2*m.x93 - 0.17*m.x94 + m.x97 == 0)

m.c125 = Constraint(expr= - m.b99 + m.s1s127 + m.s1s128 + m.s1s129 + m.s1s130 + m.s1s131 + m.s1s132 + m.s1s133 == 0)

m.c126 = Constraint(expr= - m.b100 + m.s1s134 + m.s1s135 + m.s1s136 + m.s1s137 + m.s1s138 + m.s1s139 + m.s1s140 == 0)

m.c127 = Constraint(expr= - m.b101 + m.s1s141 + m.s1s142 + m.s1s143 + m.s1s144 + m.s1s145 + m.s1s146 + m.s1s147 == 0)

m.c128 = Constraint(expr= - m.b102 + m.s1s148 + m.s1s149 + m.s1s150 + m.s1s151 + m.s1s152 + m.s1s153 + m.s1s154 == 0)

m.c129 = Constraint(expr= - m.b103 + m.s1s155 + m.s1s156 + m.s1s157 + m.s1s158 + m.s1s159 + m.s1s160 + m.s1s161 == 0)

m.c130 = Constraint(expr= - m.b104 + m.s1s162 + m.s1s163 + m.s1s164 + m.s1s165 + m.s1s166 + m.s1s167 + m.s1s168 == 0)

m.c131 = Constraint(expr= - m.b105 + m.s1s169 + m.s1s170 + m.s1s171 + m.s1s172 + m.s1s173 + m.s1s174 + m.s1s175 == 0)

m.c132 = Constraint(expr= - m.b106 + m.s1s176 + m.s1s177 + m.s1s178 + m.s1s179 + m.s1s180 + m.s1s181 + m.s1s182 == 0)

m.c133 = Constraint(expr= - m.b107 + m.s1s183 + m.s1s184 + m.s1s185 + m.s1s186 + m.s1s187 + m.s1s188 + m.s1s189 == 0)

m.c134 = Constraint(expr= - m.b108 + m.s1s190 + m.s1s191 + m.s1s192 + m.s1s193 + m.s1s194 + m.s1s195 + m.s1s196 == 0)

m.c135 = Constraint(expr= - m.b109 + m.s1s197 + m.s1s198 + m.s1s199 + m.s1s200 + m.s1s201 + m.s1s202 + m.s1s203 == 0)

m.c136 = Constraint(expr= - m.b110 + m.s1s204 + m.s1s205 + m.s1s206 + m.s1s207 + m.s1s208 + m.s1s209 + m.s1s210 == 0)

m.c137 = Constraint(expr= - m.b111 + m.s1s211 + m.s1s212 + m.s1s213 + m.s1s214 + m.s1s215 + m.s1s216 + m.s1s217 == 0)

m.c138 = Constraint(expr= - m.b112 + m.s1s218 + m.s1s219 + m.s1s220 + m.s1s221 + m.s1s222 + m.s1s223 + m.s1s224 == 0)

m.c139 = Constraint(expr= - m.b113 + m.s1s225 + m.s1s226 + m.s1s227 + m.s1s228 + m.s1s229 + m.s1s230 + m.s1s231 == 0)

m.c140 = Constraint(expr= - m.b114 + m.s1s232 + m.s1s233 + m.s1s234 + m.s1s235 + m.s1s236 + m.s1s237 + m.s1s238 == 0)

m.c141 = Constraint(expr= - m.b115 + m.s1s239 + m.s1s240 + m.s1s241 + m.s1s242 + m.s1s243 + m.s1s244 + m.s1s245 == 0)

m.c142 = Constraint(expr= - m.b116 + m.s1s246 + m.s1s247 + m.s1s248 + m.s1s249 + m.s1s250 + m.s1s251 + m.s1s252 == 0)

m.c143 = Constraint(expr= - m.b117 + m.s1s253 + m.s1s254 + m.s1s255 + m.s1s256 + m.s1s257 + m.s1s258 + m.s1s259 == 0)

m.c144 = Constraint(expr= - m.b118 + m.s1s260 + m.s1s261 + m.s1s262 + m.s1s263 + m.s1s264 + m.s1s265 + m.s1s266 == 0)

m.c145 = Constraint(expr= - m.b119 + m.s1s267 + m.s1s268 + m.s1s269 + m.s1s270 + m.s1s271 + m.s1s272 + m.s1s273 == 0)

m.c146 = Constraint(expr= - m.b120 + m.s1s274 + m.s1s275 + m.s1s276 + m.s1s277 + m.s1s278 + m.s1s279 + m.s1s280 == 0)

m.c147 = Constraint(expr= - m.b121 + m.s1s281 + m.s1s282 + m.s1s283 + m.s1s284 + m.s1s285 + m.s1s286 + m.s1s287 == 0)

m.c148 = Constraint(expr= - m.b122 + m.s1s288 + m.s1s289 + m.s1s290 + m.s1s291 + m.s1s292 + m.s1s293 + m.s1s294 == 0)

m.c149 = Constraint(expr= - m.b123 + m.s1s295 + m.s1s296 + m.s1s297 + m.s1s298 + m.s1s299 + m.s1s300 + m.s1s301 == 0)

m.c150 = Constraint(expr= - m.b124 + m.s1s302 + m.s1s303 + m.s1s304 + m.s1s305 + m.s1s306 + m.s1s307 + m.s1s308 == 0)

m.c151 = Constraint(expr= - m.b125 + m.s1s309 + m.s1s310 + m.s1s311 + m.s1s312 + m.s1s313 + m.s1s314 + m.s1s315 == 0)

m.c152 = Constraint(expr= - m.b126 + m.s1s316 + m.s1s317 + m.s1s318 + m.s1s319 + m.s1s320 + m.s1s321 + m.s1s322 == 0)

m.c153 = Constraint(expr=   m.x1 - 0.0176041976445841*m.s1s127 - 0.0686820348432157*m.s1s128
                          - 0.240338257044582*m.s1s129 - 0.708118780382974*m.s1s130 - 2*m.s1s131 - 2*m.s1s132
                          - 2*m.s1s133 <= 0)

m.c154 = Constraint(expr=   m.x2 - 0.0192122784105588*m.s1s134 - 0.0749558941482069*m.s1s135
                          - 0.262292300976835*m.s1s136 - 0.772802909347502*m.s1s137 - 2*m.s1s138 - 2*m.s1s139
                          - 2*m.s1s140 <= 0)

m.c155 = Constraint(expr=   m.x3 - 0.0137502828767635*m.s1s141 - 0.0536461488738445*m.s1s142
                          - 0.187723353667753*m.s1s143 - 0.553097263345606*m.s1s144 - 2*m.s1s145 - 2*m.s1s146
                          - 2*m.s1s147 <= 0)

m.c156 = Constraint(expr=   m.x4 - 0.0153698320860398*m.s1s148 - 0.0599647518268192*m.s1s149
                          - 0.209833968534382*m.s1s150 - 0.618242703881818*m.s1s151 - 2*m.s1s152 - 2*m.s1s153
                          - 2*m.s1s154 <= 0)

m.c157 = Constraint(expr=   m.x5 - 0.0142414920290718*m.s1s155 - 0.0555625806701283*m.s1s156
                          - 0.194429501479406*m.s1s157 - 0.572855870518057*m.s1s158 - 2*m.s1s159 - 2*m.s1s160
                          - 2*m.s1s161 <= 0)

m.c158 = Constraint(expr=   m.x6 - 0.0190758342372385*m.s1s162 - 0.0744235629590588*m.s1s163
                          - 0.260429520550158*m.s1s164 - 0.767314520523847*m.s1s165 - 2*m.s1s166 - 2*m.s1s167
                          - 2*m.s1s168 <= 0)

m.c159 = Constraint(expr=   m.x7 - 0.0188299954674205*m.s1s169 - 0.0734644333642121*m.s1s170
                          - 0.257073249355929*m.s1s171 - 0.757425796631457*m.s1s172 - 2*m.s1s173 - 2*m.s1s174
                          - 2*m.s1s175 <= 0)

m.c160 = Constraint(expr=   m.x8 - 0.0176041976445841*m.s1s176 - 0.0686820348432157*m.s1s177
                          - 0.240338257044582*m.s1s178 - 0.708118780382974*m.s1s179 - 2*m.s1s180 - 2*m.s1s181
                          - 2*m.s1s182 <= 0)

m.c161 = Constraint(expr=   m.x9 - 0.0153698320860398*m.s1s183 - 0.0599647518268192*m.s1s184
                          - 0.209833968534382*m.s1s185 - 0.618242703881818*m.s1s186 - 2*m.s1s187 - 2*m.s1s188
                          - 2*m.s1s189 <= 0)

m.c162 = Constraint(expr=   m.x10 - 0.0194226083350049*m.s1s190 - 0.0757764874800376*m.s1s191
                          - 0.265163793814297*m.s1s192 - 0.781263310246409*m.s1s193 - 2*m.s1s194 - 2*m.s1s195
                          - 2*m.s1s196 <= 0)

m.c163 = Constraint(expr=   m.x11 - 0.0174381887671401*m.s1s197 - 0.0680343582075014*m.s1s198
                          - 0.238071849619242*m.s1s199 - 0.701441168247406*m.s1s200 - 2*m.s1s201 - 2*m.s1s202
                          - 2*m.s1s203 <= 0)

m.c164 = Constraint(expr=   m.x12 - 0.0190758342372385*m.s1s204 - 0.0744235629590588*m.s1s205
                          - 0.260429520550158*m.s1s206 - 0.767314520523847*m.s1s207 - 2*m.s1s208 - 2*m.s1s209
                          - 2*m.s1s210 <= 0)

m.c165 = Constraint(expr=   m.x13 - 0.0150776355652448*m.s1s211 - 0.0588247594211735*m.s1s212
                          - 0.205844806180028*m.s1s213 - 0.606489265973719*m.s1s214 - 2*m.s1s215 - 2*m.s1s216
                          - 2*m.s1s217 <= 0)

m.c166 = Constraint(expr=   m.x14 - 0.0192122784105588*m.s1s218 - 0.0749558941482069*m.s1s219
                          - 0.262292300976835*m.s1s220 - 0.772802909347502*m.s1s221 - 2*m.s1s222 - 2*m.s1s223
                          - 2*m.s1s224 <= 0)

m.c167 = Constraint(expr=   m.x15 - 0.0194226083350049*m.s1s225 - 0.0757764874800376*m.s1s226
                          - 0.265163793814297*m.s1s227 - 0.781263310246409*m.s1s228 - 2*m.s1s229 - 2*m.s1s230
                          - 2*m.s1s231 <= 0)

m.c168 = Constraint(expr=   m.x16 - 0.0197779487583483*m.s1s232 - 0.0771628331590627*m.s1s233
                          - 0.270015017353593*m.s1s234 - 0.795556675515238*m.s1s235 - 2*m.s1s236 - 2*m.s1s237
                          - 2*m.s1s238 <= 0)

m.c169 = Constraint(expr=   m.x17 - 0.0174381887671401*m.s1s239 - 0.0680343582075014*m.s1s240
                          - 0.238071849619242*m.s1s241 - 0.701441168247406*m.s1s242 - 2*m.s1s243 - 2*m.s1s244
                          - 2*m.s1s245 <= 0)

m.c170 = Constraint(expr=   m.x18 - 0.0197779487583483*m.s1s246 - 0.0771628331590627*m.s1s247
                          - 0.270015017353593*m.s1s248 - 0.795556675515238*m.s1s249 - 2*m.s1s250 - 2*m.s1s251
                          - 2*m.s1s252 <= 0)

m.c171 = Constraint(expr=   m.x19 - 0.02056968839856*m.s1s253 - 0.0802517719822704*m.s1s254 - 0.280824105561038*m.s1s255
                          - 0.827403949655566*m.s1s256 - 2*m.s1s257 - 2*m.s1s258 - 2*m.s1s259 <= 0)

m.c172 = Constraint(expr=   m.x20 - 0.0142414920290718*m.s1s260 - 0.0555625806701283*m.s1s261
                          - 0.194429501479406*m.s1s262 - 0.572855870518057*m.s1s263 - 2*m.s1s264 - 2*m.s1s265
                          - 2*m.s1s266 <= 0)

m.c173 = Constraint(expr=   m.x21 - 0.0190758342372385*m.s1s267 - 0.0744235629590588*m.s1s268
                          - 0.260429520550158*m.s1s269 - 0.767314520523847*m.s1s270 - 2*m.s1s271 - 2*m.s1s272
                          - 2*m.s1s273 <= 0)

m.c174 = Constraint(expr=   m.x22 - 0.02056968839856*m.s1s274 - 0.0802517719822704*m.s1s275 - 0.280824105561038*m.s1s276
                          - 0.827403949655566*m.s1s277 - 2*m.s1s278 - 2*m.s1s279 - 2*m.s1s280 <= 0)

m.c175 = Constraint(expr=   m.x23 - 0.0153698320860398*m.s1s281 - 0.0599647518268192*m.s1s282
                          - 0.209833968534382*m.s1s283 - 0.618242703881818*m.s1s284 - 2*m.s1s285 - 2*m.s1s286
                          - 2*m.s1s287 <= 0)

m.c176 = Constraint(expr=   m.x24 - 0.0190758342372385*m.s1s288 - 0.0744235629590588*m.s1s289
                          - 0.260429520550158*m.s1s290 - 0.767314520523847*m.s1s291 - 2*m.s1s292 - 2*m.s1s293
                          - 2*m.s1s294 <= 0)

m.c177 = Constraint(expr=   m.x25 - 0.0153698320860398*m.s1s295 - 0.0599647518268192*m.s1s296
                          - 0.209833968534382*m.s1s297 - 0.618242703881818*m.s1s298 - 2*m.s1s299 - 2*m.s1s300
                          - 2*m.s1s301 <= 0)

m.c178 = Constraint(expr=   m.x26 - 0.0137502828767635*m.s1s302 - 0.0536461488738445*m.s1s303
                          - 0.187723353667753*m.s1s304 - 0.553097263345606*m.s1s305 - 2*m.s1s306 - 2*m.s1s307
                          - 2*m.s1s308 <= 0)

m.c179 = Constraint(expr=   m.x27 - 0.0188299954674205*m.s1s309 - 0.0734644333642121*m.s1s310
                          - 0.257073249355929*m.s1s311 - 0.757425796631457*m.s1s312 - 2*m.s1s313 - 2*m.s1s314
                          - 2*m.s1s315 <= 0)

m.c180 = Constraint(expr=   m.x28 - 0.0150776355652448*m.s1s316 - 0.0588247594211735*m.s1s317
                          - 0.205844806180028*m.s1s318 - 0.606489265973719*m.s1s319 - 2*m.s1s320 - 2*m.s1s321
                          - 2*m.s1s322 <= 0)

m.c181 = Constraint(expr=   m.b99 + m.b106 <= 1)

m.c182 = Constraint(expr=   m.b100 + m.b112 <= 1)

m.c183 = Constraint(expr=   m.b101 + m.b124 <= 1)

m.c184 = Constraint(expr=   m.b102 + m.b107 <= 1)

m.c185 = Constraint(expr=   m.b103 + m.b118 <= 1)

m.c186 = Constraint(expr=   m.b104 + m.b122 <= 1)

m.c187 = Constraint(expr=   m.b105 + m.b125 <= 1)

m.c188 = Constraint(expr=   m.b108 + m.b113 <= 1)

m.c189 = Constraint(expr=   m.b109 + m.b115 <= 1)

m.c190 = Constraint(expr=   m.b110 + m.b119 <= 1)

m.c191 = Constraint(expr=   m.b111 + m.b126 <= 1)

m.c192 = Constraint(expr=   m.b114 + m.b116 <= 1)

m.c193 = Constraint(expr=   m.b117 + m.b120 <= 1)

m.c194 = Constraint(expr=   m.b121 + m.b123 <= 1)

m.c195 = Constraint(expr=   m.b99 + m.b100 + m.b101 >= 1)

m.c196 = Constraint(expr=   m.b102 + m.b103 + m.b104 + m.b105 >= 1)

m.c197 = Constraint(expr=   m.b99 + m.b102 + m.b108 + m.b109 + m.b110 + m.b111 >= 1)

m.c198 = Constraint(expr=   m.b100 + m.b108 + m.b116 >= 1)

m.c199 = Constraint(expr=   m.b109 + m.b116 + m.b120 >= 1)

m.c200 = Constraint(expr=   m.b103 + m.b110 + m.b120 + m.b121 >= 1)

m.c201 = Constraint(expr=   m.b104 + m.b121 >= 1)

m.c202 = Constraint(expr=   m.b101 + m.b105 + m.b111 >= 1)
