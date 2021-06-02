#  MINLP written by GAMS Convert at 04/21/18 13:52:29
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         88       88        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        987       88        0      899        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1891     1187      704        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(1,2),initialize=1)
m.x2 = Var(within=Reals,bounds=(2,4),initialize=2.13333333333333)
m.x3 = Var(within=Reals,bounds=(2,4),initialize=2)
m.x4 = Var(within=Reals,bounds=(2,4),initialize=2)
m.x5 = Var(within=Reals,bounds=(2,3),initialize=2)
m.x6 = Var(within=Reals,bounds=(2,3),initialize=2)
m.x7 = Var(within=Reals,bounds=(2,4),initialize=2)
m.x8 = Var(within=Reals,bounds=(2,3),initialize=2)
m.x9 = Var(within=Reals,bounds=(2,3),initialize=2.13333333333333)
m.x10 = Var(within=Reals,bounds=(2,3),initialize=2)
m.x11 = Var(within=Reals,bounds=(2,3),initialize=2)
m.x12 = Var(within=Reals,bounds=(2,5),initialize=2)
m.x13 = Var(within=Reals,bounds=(2,4),initialize=2)
m.x14 = Var(within=Reals,bounds=(2,3),initialize=2)
m.x15 = Var(within=Reals,bounds=(2,3),initialize=2)
m.x16 = Var(within=Reals,bounds=(2,3),initialize=2)
m.x17 = Var(within=Reals,bounds=(2,3),initialize=2)
m.x18 = Var(within=Reals,bounds=(2,3),initialize=2)
m.x19 = Var(within=Reals,bounds=(2,3),initialize=2.33333333333333)
m.x20 = Var(within=Reals,bounds=(2,3),initialize=2)
m.x21 = Var(within=Reals,bounds=(2,5),initialize=3.26666666666667)
m.x22 = Var(within=Reals,bounds=(1,2),initialize=1)
m.x23 = Var(within=Reals,bounds=(2,3),initialize=2)
m.x24 = Var(within=Reals,bounds=(2,5),initialize=2)
m.x25 = Var(within=Reals,bounds=(2,4),initialize=2)
m.x26 = Var(within=Reals,bounds=(2,4),initialize=2)
m.x27 = Var(within=Reals,bounds=(2,3),initialize=2)
m.x28 = Var(within=Reals,bounds=(1,2),initialize=1)
m.x29 = Var(within=Reals,bounds=(2,4),initialize=2)
m.x30 = Var(within=Reals,bounds=(1,2),initialize=1)
m.x31 = Var(within=Reals,bounds=(2,4),initialize=2)
m.x32 = Var(within=Reals,bounds=(2,4),initialize=2)
m.x33 = Var(within=Reals,bounds=(3,6),initialize=3.66666666666666)
m.x34 = Var(within=Reals,bounds=(2,4),initialize=2)
m.x35 = Var(within=Reals,bounds=(2,4),initialize=2)
m.x36 = Var(within=Reals,bounds=(2,5),initialize=2.33333333333333)
m.x37 = Var(within=Reals,bounds=(2,4),initialize=2.33333333333333)
m.x38 = Var(within=Reals,bounds=(2,4),initialize=2)
m.x39 = Var(within=Reals,bounds=(1,2),initialize=1)
m.x40 = Var(within=Reals,bounds=(1,2),initialize=1)
m.x41 = Var(within=Reals,bounds=(1,2),initialize=1)
m.x42 = Var(within=Reals,bounds=(2,3),initialize=2)
m.x43 = Var(within=Reals,bounds=(2,3),initialize=2)
m.x44 = Var(within=Reals,bounds=(2,4),initialize=2)
m.x45 = Var(within=Reals,bounds=(2,4),initialize=2)
m.x46 = Var(within=Reals,bounds=(2,3),initialize=2)
m.x47 = Var(within=Reals,bounds=(2,3),initialize=2)
m.x48 = Var(within=Reals,bounds=(2,3),initialize=2)
m.x49 = Var(within=Reals,bounds=(4,None),initialize=4)
m.x50 = Var(within=Reals,bounds=(17,None),initialize=17)
m.x51 = Var(within=Reals,bounds=(15,None),initialize=15)
m.x52 = Var(within=Reals,bounds=(12,None),initialize=12)
m.x53 = Var(within=Reals,bounds=(7,None),initialize=7)
m.x54 = Var(within=Reals,bounds=(8,None),initialize=11)
m.x55 = Var(within=Reals,bounds=(17,None),initialize=17)
m.x56 = Var(within=Reals,bounds=(8,None),initialize=8)
m.x57 = Var(within=Reals,bounds=(9,None),initialize=9)
m.x58 = Var(within=Reals,bounds=(23,None),initialize=23)
m.x59 = Var(within=Reals,bounds=(17,None),initialize=17)
m.x60 = Var(within=Reals,bounds=(9,None),initialize=9)
m.x61 = Var(within=Reals,bounds=(7,None),initialize=7)
m.x62 = Var(within=Reals,bounds=(7,None),initialize=7)
m.x63 = Var(within=Reals,bounds=(8,None),initialize=8)
m.x64 = Var(within=Reals,bounds=(7,None),initialize=7)
m.x65 = Var(within=Reals,bounds=(25,None),initialize=25)
m.x66 = Var(within=Reals,bounds=(4,None),initialize=4)
m.x67 = Var(within=Reals,bounds=(11,None),initialize=11)
m.x68 = Var(within=Reals,bounds=(20,None),initialize=23)
m.x69 = Var(within=Reals,bounds=(19,None),initialize=19)
m.x70 = Var(within=Reals,bounds=(13,None),initialize=13)
m.x71 = Var(within=Reals,bounds=(4,None),initialize=4)
m.x72 = Var(within=Reals,bounds=(10,None),initialize=10)
m.x73 = Var(within=Reals,bounds=(4,None),initialize=4)
m.x74 = Var(within=Reals,bounds=(12,None),initialize=12)
m.x75 = Var(within=Reals,bounds=(11,None),initialize=11)
m.x76 = Var(within=Reals,bounds=(40,None),initialize=40)
m.x77 = Var(within=Reals,bounds=(11,None),initialize=20)
m.x78 = Var(within=Reals,bounds=(15,None),initialize=15)
m.x79 = Var(within=Reals,bounds=(30,None),initialize=30)
m.x80 = Var(within=Reals,bounds=(16,None),initialize=16)
m.x81 = Var(within=Reals,bounds=(10,None),initialize=10)
m.x82 = Var(within=Reals,bounds=(4,None),initialize=4)
m.x83 = Var(within=Reals,bounds=(4,None),initialize=4)
m.x84 = Var(within=Reals,bounds=(16,None),initialize=16)
m.x85 = Var(within=Reals,bounds=(13,None),initialize=13)
m.x86 = Var(within=Reals,bounds=(9,None),initialize=9)
m.x87 = Var(within=Reals,bounds=(10,None),initialize=10)
m.i89 = Var(within=Integers,bounds=(0,1),initialize=0.0499999999999998)
m.i90 = Var(within=Integers,bounds=(0,1),initialize=0.916666666666667)
m.i91 = Var(within=Integers,bounds=(0,1),initialize=0.208333333333328)
m.i92 = Var(within=Integers,bounds=(0,1),initialize=0.0416666666666676)
m.i93 = Var(within=Integers,bounds=(0,1),initialize=0.291666666666666)
m.i94 = Var(within=Integers,bounds=(0,1),initialize=0.118923613930309)
m.i95 = Var(within=Integers,bounds=(0,1),initialize=1)
m.i96 = Var(within=Integers,bounds=(0,1),initialize=0.339409719403031)
m.i97 = Var(within=Integers,bounds=(0,1),initialize=0.066666666666666)
m.i98 = Var(within=Integers,bounds=(0,1),initialize=0.0666666666666674)
m.i99 = Var(within=Integers,bounds=(0,1),initialize=0.416666666666667)
m.i100 = Var(within=Integers,bounds=(0,1),initialize=0.0416666666666689)
m.i101 = Var(within=Integers,bounds=(0,1),initialize=0.0833333333333333)
m.i102 = Var(within=Integers,bounds=(0,1),initialize=0.291666666666666)
m.i103 = Var(within=Integers,bounds=(0,1),initialize=0.166666666666667)
m.i104 = Var(within=Integers,bounds=(0,1),initialize=0.0833333333333332)
m.i105 = Var(within=Integers,bounds=(0,1),initialize=0.216666666666667)
m.i106 = Var(within=Integers,bounds=(0,1),initialize=0.500000000000001)
m.i107 = Var(within=Integers,bounds=(0,1),initialize=0.75)
m.i108 = Var(within=Integers,bounds=(0,1),initialize=1)
m.i109 = Var(within=Integers,bounds=(0,1),initialize=0.416666666666667)
m.i110 = Var(within=Integers,bounds=(0,1),initialize=0.0833333333333256)
m.i111 = Var(within=Integers,bounds=(0,1),initialize=0.833333333333334)
m.i112 = Var(within=Integers,bounds=(0,1),initialize=0.708333333333336)
m.i113 = Var(within=Integers,bounds=(0,1),initialize=0.166666666666671)
m.i114 = Var(within=Integers,bounds=(0,1),initialize=0.25)
m.i115 = Var(within=Integers,bounds=(0,1),initialize=0.116666666666666)
m.i116 = Var(within=Integers,bounds=(0,1),initialize=0.283333333333333)
m.i117 = Var(within=Integers,bounds=(0,1),initialize=0.333333333333333)
m.i118 = Var(within=Integers,bounds=(0,1),initialize=0.2)
m.i119 = Var(within=Integers,bounds=(0,1),initialize=0.333333333333333)
m.i120 = Var(within=Integers,bounds=(0,1),initialize=0.166666666666667)
m.i121 = Var(within=Integers,bounds=(0,1),initialize=0.687500009460761)
m.i122 = Var(within=Integers,bounds=(0,1),initialize=0.145833323872572)
m.i123 = Var(within=Integers,bounds=(0,1),initialize=0.0833333333333334)
m.i124 = Var(within=Integers,bounds=(0,1),initialize=0.166666666666663)
m.i125 = Var(within=Integers,bounds=(0,1),initialize=0.75)
m.i126 = Var(within=Integers,bounds=(0,1),initialize=0.0833333333333335)
m.i127 = Var(within=Integers,bounds=(0,1),initialize=0.583333333333337)
m.i128 = Var(within=Integers,bounds=(0,1),initialize=0.541666666666666)
m.i129 = Var(within=Integers,bounds=(0,1),initialize=0.500000000000002)
m.i130 = Var(within=Integers,bounds=(0,1),initialize=0.0833333333333332)
m.i131 = Var(within=Integers,bounds=(0,1),initialize=0.0416666666666666)
m.i132 = Var(within=Integers,bounds=(0,1),initialize=0.166666666666662)
m.i133 = Var(within=Integers,bounds=(0,1),initialize=0.110243055892633)
m.i134 = Var(within=Integers,bounds=(0,1),initialize=0.166666666666673)
m.i135 = Var(within=Integers,bounds=(0,1),initialize=0.0147569441073615)
m.i136 = Var(within=Integers,bounds=(0,1),initialize=0.249999999999997)
m.i137 = Var(within=Integers,bounds=(0,1),initialize=0.0208333301844284)
m.i138 = Var(within=Integers,bounds=(0,1),initialize=0.249999999999996)
m.i139 = Var(within=Integers,bounds=(0,1),initialize=0.0208333301770631)
m.i140 = Var(within=Integers,bounds=(0,1),initialize=0.0208333301777509)
m.i141 = Var(within=Integers,bounds=(0,1),initialize=0.25)
m.i142 = Var(within=Integers,bounds=(0,1),initialize=0.0833333333333333)
m.i143 = Var(within=Integers,bounds=(0,1),initialize=0.0833333333333333)
m.i144 = Var(within=Integers,bounds=(0,1),initialize=0.330280969044536)
m.i145 = Var(within=Integers,bounds=(0,1),initialize=0.625)
m.i146 = Var(within=Integers,bounds=(0,1),initialize=0.00305235797693697)
m.i147 = Var(within=Integers,bounds=(0,1),initialize=0.0208333427940989)
m.i148 = Var(within=Integers,bounds=(0,1),initialize=0.583333333333333)
m.i149 = Var(within=Integers,bounds=(0,1),initialize=0.503052364288797)
m.i150 = Var(within=Integers,bounds=(0,1),initialize=0.208333333333334)
m.i151 = Var(within=Integers,bounds=(0,1),initialize=0.0916666666666665)
m.i152 = Var(within=Integers,bounds=(0,1),initialize=0.18333333333333)
m.i153 = Var(within=Integers,bounds=(0,1),initialize=0.0802809753563962)
m.i154 = Var(within=Integers,bounds=(0,1),initialize=0.961385691310271)
m.i155 = Var(within=Integers,bounds=(0,1),initialize=0.916666666666663)
m.i156 = Var(within=Integers,bounds=(0,1),initialize=0.0386143086897254)
m.i157 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i158 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i159 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i160 = Var(within=Integers,bounds=(0,12),initialize=12)
m.i161 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i162 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i163 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i164 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i165 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i166 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i167 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i168 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i169 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i170 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i171 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i172 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i173 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i174 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i175 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i176 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i177 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i178 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i179 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i180 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i181 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i182 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i183 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i184 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i185 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i186 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i187 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i188 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i189 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i190 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i191 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i192 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i193 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i194 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i195 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i196 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i197 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i198 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i199 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i200 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i201 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i202 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i203 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i204 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i205 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i206 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i207 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i208 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i209 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i210 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i211 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i212 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i213 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i214 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i215 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i216 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i217 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i218 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i219 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i220 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i221 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i222 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i223 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i224 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i225 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i226 = Var(within=Integers,bounds=(0,12),initialize=12)
m.i227 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i228 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i229 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i230 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i231 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i232 = Var(within=Integers,bounds=(0,12),initialize=12)
m.i233 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i234 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i235 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i236 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i237 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i238 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i239 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i240 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i241 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i242 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i243 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i244 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i245 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i246 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i247 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i248 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i249 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i250 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i251 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i252 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i253 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i254 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i255 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i256 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i257 = Var(within=Integers,bounds=(0,12),initialize=5)
m.i258 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i259 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i260 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i261 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i262 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i263 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i264 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i265 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i266 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i267 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i268 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i269 = Var(within=Integers,bounds=(0,12),initialize=12)
m.i270 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i271 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i272 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i273 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i274 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i275 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i276 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i277 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i278 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i279 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i280 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i281 = Var(within=Integers,bounds=(0,12),initialize=12)
m.i282 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i283 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i284 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i285 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i286 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i287 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i288 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i289 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i290 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i291 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i292 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i293 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i294 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i295 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i296 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i297 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i298 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i299 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i300 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i301 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i302 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i303 = Var(within=Integers,bounds=(0,12),initialize=12)
m.i304 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i305 = Var(within=Integers,bounds=(0,12),initialize=12)
m.i306 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i307 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i308 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i309 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i310 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i311 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i312 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i313 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i314 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i315 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i316 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i317 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i318 = Var(within=Integers,bounds=(0,12),initialize=12)
m.i319 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i320 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i321 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i322 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i323 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i324 = Var(within=Integers,bounds=(0,12),initialize=12)
m.i325 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i326 = Var(within=Integers,bounds=(0,12),initialize=12)
m.i327 = Var(within=Integers,bounds=(0,12),initialize=12)
m.i328 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i329 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i330 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i331 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i332 = Var(within=Integers,bounds=(0,12),initialize=12)
m.i333 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i334 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i335 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i336 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i337 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i338 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i339 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i340 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i341 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i342 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i343 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i344 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i345 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i346 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i347 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i348 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i349 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i350 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i351 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i352 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i353 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i354 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i355 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i356 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i357 = Var(within=Integers,bounds=(0,12),initialize=12)
m.i358 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i359 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i360 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i361 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i362 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i363 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i364 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i365 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i366 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i367 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i368 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i369 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i370 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i371 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i372 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i373 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i374 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i375 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i376 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i377 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i378 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i379 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i380 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i381 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i382 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i383 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i384 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i385 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i386 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i387 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i388 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i389 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i390 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i391 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i392 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i393 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i394 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i395 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i396 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i397 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i398 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i399 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i400 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i401 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i402 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i403 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i404 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i405 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i406 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i407 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i408 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i409 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i410 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i411 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i412 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i413 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i414 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i415 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i416 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i417 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i418 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i419 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i420 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i421 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i422 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i423 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i424 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i425 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i426 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i427 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i428 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i429 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i430 = Var(within=Integers,bounds=(0,12),initialize=12)
m.i431 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i432 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i433 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i434 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i435 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i436 = Var(within=Integers,bounds=(0,12),initialize=12)
m.i437 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i438 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i439 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i440 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i441 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i442 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i443 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i444 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i445 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i446 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i447 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i448 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i449 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i450 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i451 = Var(within=Integers,bounds=(0,12),initialize=12)
m.i452 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i453 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i454 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i455 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i456 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i457 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i458 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i459 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i460 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i461 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i462 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i463 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i464 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i465 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i466 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i467 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i468 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i469 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i470 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i471 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i472 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i473 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i474 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i475 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i476 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i477 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i478 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i479 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i480 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i481 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i482 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i483 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i484 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i485 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i486 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i487 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i488 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i489 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i490 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i491 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i492 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i493 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i494 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i495 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i496 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i497 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i498 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i499 = Var(within=Integers,bounds=(0,12),initialize=12)
m.i500 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i501 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i502 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i503 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i504 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i505 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i506 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i507 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i508 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i509 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i510 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i511 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i512 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i513 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i514 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i515 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i516 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i517 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i518 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i519 = Var(within=Integers,bounds=(0,12),initialize=12)
m.i520 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i521 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i522 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i523 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i524 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i525 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i526 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i527 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i528 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i529 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i530 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i531 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i532 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i533 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i534 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i535 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i536 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i537 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i538 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i539 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i540 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i541 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i542 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i543 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i544 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i545 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i546 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i547 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i548 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i549 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i550 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i551 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i552 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i553 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i554 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i555 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i556 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i557 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i558 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i559 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i560 = Var(within=Integers,bounds=(0,12),initialize=12)
m.i561 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i562 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i563 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i564 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i565 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i566 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i567 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i568 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i569 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i570 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i571 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i572 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i573 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i574 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i575 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i576 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i577 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i578 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i579 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i580 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i581 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i582 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i583 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i584 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i585 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i586 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i587 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i588 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i589 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i590 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i591 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i592 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i593 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i594 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i595 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i596 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i597 = Var(within=Integers,bounds=(0,12),initialize=12)
m.i598 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i599 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i600 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i601 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i602 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i603 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i604 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i605 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i606 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i607 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i608 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i609 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i610 = Var(within=Integers,bounds=(0,12),initialize=12)
m.i611 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i612 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i613 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i614 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i615 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i616 = Var(within=Integers,bounds=(0,12),initialize=12)
m.i617 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i618 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i619 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i620 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i621 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i622 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i623 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i624 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i625 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i626 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i627 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i628 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i629 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i630 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i631 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i632 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i633 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i634 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i635 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i636 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i637 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i638 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i639 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i640 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i641 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i642 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i643 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i644 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i645 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i646 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i647 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i648 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i649 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i650 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i651 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i652 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i653 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i654 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i655 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i656 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i657 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i658 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i659 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i660 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i661 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i662 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i663 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i664 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i665 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i666 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i667 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i668 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i669 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i670 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i671 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i672 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i673 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i674 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i675 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i676 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i677 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i678 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i679 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i680 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i681 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i682 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i683 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i684 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i685 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i686 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i687 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i688 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i689 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i690 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i691 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i692 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i693 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i694 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i695 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i696 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i697 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i698 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i699 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i700 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i701 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i702 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i703 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i704 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i705 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i706 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i707 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i708 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i709 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i710 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i711 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i712 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i713 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i714 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i715 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i716 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i717 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i718 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i719 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i720 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i721 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i722 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i723 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i724 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i725 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i726 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i727 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i728 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i729 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i730 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i731 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i732 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i733 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i734 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i735 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i736 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i737 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i738 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i739 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i740 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i741 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i742 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i743 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i744 = Var(within=Integers,bounds=(0,12),initialize=12)
m.i745 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i746 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i747 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i748 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i749 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i750 = Var(within=Integers,bounds=(0,12),initialize=12)
m.i751 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i752 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i753 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i754 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i755 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i756 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i757 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i758 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i759 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i760 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i761 = Var(within=Integers,bounds=(0,12),initialize=12)
m.i762 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i763 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i764 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i765 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i766 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i767 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i768 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i769 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i770 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i771 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i772 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i773 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i774 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i775 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i776 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i777 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i778 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i779 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i780 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i781 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i782 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i783 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i784 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i785 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i786 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i787 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i788 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i789 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i790 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i791 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i792 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i793 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i794 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i795 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i796 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i797 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i798 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i799 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i800 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i801 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i802 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i803 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i804 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i805 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i806 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i807 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i808 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i809 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i810 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i811 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i812 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i813 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i814 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i815 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i816 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i817 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i818 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i819 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i820 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i821 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i822 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i823 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i824 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i825 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i826 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i827 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i828 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i829 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i830 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i831 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i832 = Var(within=Integers,bounds=(0,12),initialize=12)
m.i833 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i834 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i835 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i836 = Var(within=Integers,bounds=(0,12),initialize=12)
m.i837 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i838 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i839 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i840 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i841 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i842 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i843 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i844 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i845 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i846 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i847 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i848 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i849 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i850 = Var(within=Integers,bounds=(0,12),initialize=1.09090909094524)
m.i851 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i852 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i853 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i854 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i855 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i856 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i857 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i858 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i859 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i860 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i861 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i862 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i863 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i864 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i865 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i866 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i867 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i868 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i869 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i870 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i871 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i872 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i873 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i874 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i875 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i876 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i877 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i878 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i879 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i880 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i881 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i882 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i883 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i884 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i885 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i886 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i887 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i888 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i889 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i890 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i891 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i892 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i893 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i894 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i895 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i896 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i897 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i898 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i899 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i900 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i901 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i902 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i903 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i904 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i905 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i906 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i907 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i908 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i909 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i910 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i911 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i912 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i913 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i914 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i915 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i916 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i917 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i918 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i919 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i920 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i921 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i922 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i923 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i924 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i925 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i926 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i927 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i928 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i929 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i930 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i931 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i932 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i933 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i934 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i935 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i936 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i937 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i938 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i939 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i940 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i941 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i942 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i943 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i944 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i945 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i946 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i947 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i948 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i949 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i950 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i951 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i952 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i953 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i954 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i955 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i956 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i957 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i958 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i959 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i960 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i961 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i962 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i963 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i964 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i965 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i966 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i967 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i968 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i969 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i970 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i971 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i972 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i973 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i974 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i975 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i976 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i977 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i978 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i979 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i980 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i981 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i982 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i983 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i984 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i985 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i986 = Var(within=Integers,bounds=(0,12),initialize=0)
m.i987 = Var(within=Integers,bounds=(0,12),initialize=0)

m.obj = Objective(expr=(33.219 + 11.073*m.i160)*m.i89 + (64.7407488 + 6.6500096*m.i160)*m.i89 + 0.001*m.i160 + (44.292
                        + 14.764*m.i194)*m.i90 + (114.1305984 + 11.7232128*m.i194)*m.i90 + 0.001*m.i194 + (22.146 + 
                       7.382*m.i213)*m.i91 + (30.7017984 + 3.1536128*m.i213)*m.i91 + 0.001*m.i213 + (22.146 + 7.382*
                       m.i226)*m.i92 + (35.3738112 + 3.6335104*m.i226)*m.i92 + 0.001*m.i226 + (33.219 + 11.073*m.i232)*
                       m.i93 + (67.4104704 + 6.9242368*m.i232)*m.i93 + 0.001*m.i232 + (44.292 + 14.764*m.i253)*m.i94 + (
                       90.7705344 + 9.3237248*m.i253)*m.i94 + 0.001*m.i253 + (22.146 + 7.382*m.i257)*m.i95 + (38.0435328
                        + 3.9077376*m.i257)*m.i95 + 0.001*m.i257 + (44.292 + 14.764*m.i260)*m.i96 + (102.7842816 + 
                       10.5577472*m.i260)*m.i96 + 0.001*m.i260 + (55.365 + 18.455*m.i269)*m.i97 + (129.4814976 + 
                       13.3000192*m.i269)*m.i97 + 0.001*m.i269 + (44.292 + 14.764*m.i281)*m.i98 + (110.7934464 + 
                       11.3804288*m.i281)*m.i98 + 0.001*m.i281 + (44.292 + 14.764*m.i300)*m.i99 + (101.4494208 + 
                       10.4206336*m.i300)*m.i99 + 0.001*m.i300 + (44.292 + 14.764*m.i303)*m.i100 + (96.1099776 + 
                       9.8721792*m.i303)*m.i100 + 0.001*m.i303 + (33.219 + 11.073*m.i305)*m.i101 + (72.0824832 + 
                       7.4041344*m.i305)*m.i101 + 0.001*m.i305 + (44.292 + 14.764*m.i318)*m.i102 + (99.4471296 + 
                       10.2149632*m.i318)*m.i102 + 0.001*m.i318 + (44.292 + 14.764*m.i324)*m.i103 + (89.4356736 + 
                       9.1866112*m.i324)*m.i103 + 0.001*m.i324 + (33.219 + 11.073*m.i326)*m.i104 + (69.4127616 + 
                       7.1299072*m.i326)*m.i104 + 0.001*m.i326 + (33.219 + 11.073*m.i327)*m.i105 + (70.7476224 + 
                       7.2670208*m.i327)*m.i105 + 0.001*m.i327 + (33.219 + 11.073*m.i332)*m.i106 + (47.3875584 + 
                       4.8675328*m.i332)*m.i106 + 0.001*m.i332 + (33.219 + 11.073*m.i333)*m.i107 + (62.0710272 + 
                       6.3757824*m.i333)*m.i107 + 0.001*m.i333 + (55.365 + 18.455*m.i334)*m.i108 + (145.4998272 + 
                       14.9453824*m.i334)*m.i108 + 0.001*m.i334 + (22.146 + 7.382*m.i335)*m.i109 + (41.3806848 + 
                       4.2505216*m.i335)*m.i109 + 0.001*m.i335 + (22.146 + 7.382*m.i336)*m.i110 + (42.7155456 + 
                       4.3876352*m.i336)*m.i110 + 0.001*m.i336 + (22.146 + 7.382*m.i338)*m.i111 + (44.0504064 + 
                       4.5247488*m.i338)*m.i111 + 0.001*m.i338 + (55.365 + 18.455*m.i345)*m.i112 + (138.1580928 + 
                       14.1912576*m.i345)*m.i112 + 0.001*m.i345 + (44.292 + 14.764*m.i352)*m.i113 + (96.1099776 + 
                       9.8721792*m.i352)*m.i113 + 0.001*m.i352 + (55.365 + 18.455*m.i357)*m.i114 + (132.1512192 + 
                       13.5742464*m.i357)*m.i114 + 0.001*m.i357 + (33.219 + 11.073*m.i430)*m.i115 + (60.068736 + 
                       6.170112*m.i430)*m.i115 + 0.001*m.i430 + (22.146 + 7.382*m.i436)*m.i116 + (38.7109632 + 3.9762944
                       *m.i436)*m.i116 + 0.001*m.i436 + (33.219 + 11.073*m.i451)*m.i117 + (58.7338752 + 6.0329984*m.i451
                       )*m.i117 + 0.001*m.i451 + (33.219 + 11.073*m.i499)*m.i118 + (66.0756096 + 6.7871232*m.i499)*
                       m.i118 + 0.001*m.i499 + (55.365 + 18.455*m.i507)*m.i119 + (140.8278144 + 14.4654848*m.i507)*
                       m.i119 + 0.001*m.i507 + (33.219 + 11.073*m.i519)*m.i120 + (75.4196352 + 7.7469184*m.i519)*m.i120
                        + 0.001*m.i519 + (55.365 + 18.455*m.i527)*m.i121 + (130.148928 + 13.368576*m.i527)*m.i121 + 
                       0.001*m.i527 + (33.219 + 11.073*m.i547)*m.i122 + (70.080192 + 7.198464*m.i547)*m.i122 + 0.001*
                       m.i547 + (55.365 + 18.455*m.i560)*m.i123 + (132.1512192 + 13.5742464*m.i560)*m.i123 + 0.001*
                       m.i560 + (55.365 + 18.455*m.i564)*m.i124 + (134.8209408 + 13.8484736*m.i564)*m.i124 + 0.001*
                       m.i564 + (55.365 + 18.455*m.i584)*m.i125 + (118.1351808 + 12.1345536*m.i584)*m.i125 + 0.001*
                       m.i584 + (55.365 + 18.455*m.i597)*m.i126 + (150.17184 + 15.42528*m.i597)*m.i126 + 0.001*m.i597 + 
                       (33.219 + 11.073*m.i602)*m.i127 + (50.05728 + 5.14176*m.i602)*m.i127 + 0.001*m.i602 + (33.219 + 
                       11.073*m.i610)*m.i128 + (72.7499136 + 7.4726912*m.i610)*m.i128 + 0.001*m.i610 + (33.219 + 11.073*
                       m.i613)*m.i129 + (64.0733184 + 6.5814528*m.i613)*m.i129 + 0.001*m.i613 + (33.219 + 11.073*m.i616)
                       *m.i130 + (79.4242176 + 8.1582592*m.i616)*m.i130 + 0.001*m.i616 + (55.365 + 18.455*m.i628)*m.i131
                        + (134.1535104 + 13.7799168*m.i628)*m.i131 + 0.001*m.i628 + (55.365 + 18.455*m.i629)*m.i132 + (
                       134.8209408 + 13.8484736*m.i629)*m.i132 + 0.001*m.i629 + (77.511 + 25.837*m.i634)*m.i133 + (
                       205.5685632 + 21.1154944*m.i634)*m.i133 + 0.001*m.i634 + (55.365 + 18.455*m.i641)*m.i134 + (
                       144.1649664 + 14.8082688*m.i641)*m.i134 + 0.001*m.i641 + (77.511 + 25.837*m.i642)*m.i135 + (
                       217.5823104 + 22.3495168*m.i642)*m.i135 + 0.001*m.i642 + (33.219 + 11.073*m.i692)*m.i136 + (
                       64.0733184 + 6.5814528*m.i692)*m.i136 + 0.001*m.i692 + (77.511 + 25.837*m.i712)*m.i137 + (
                       194.8896768 + 20.0185856*m.i712)*m.i137 + 0.001*m.i712 + (55.365 + 18.455*m.i716)*m.i138 + (
                       130.8163584 + 13.4371328*m.i716)*m.i138 + 0.001*m.i716 + (66.438 + 22.146*m.i723)*m.i139 + (
                       152.8415616 + 15.6995072*m.i723)*m.i139 + 0.001*m.i723 + (66.438 + 22.146*m.i734)*m.i140 + (
                       164.8553088 + 16.9335296*m.i734)*m.i140 + 0.001*m.i734 + (33.219 + 11.073*m.i744)*m.i141 + (
                       71.4150528 + 7.3355776*m.i744)*m.i141 + 0.001*m.i744 + (55.365 + 18.455*m.i750)*m.i142 + (
                       128.8140672 + 13.2314624*m.i750)*m.i142 + 0.001*m.i750 + (55.365 + 18.455*m.i761)*m.i143 + (
                       127.4792064 + 13.0943488*m.i761)*m.i143 + 0.001*m.i761 + (44.292 + 14.764*m.i782)*m.i144 + (
                       102.7842816 + 10.5577472*m.i782)*m.i144 + 0.001*m.i782 + (22.146 + 7.382*m.i784)*m.i145 + (
                       26.697216 + 2.742272*m.i784)*m.i145 + 0.001*m.i784 + (22.146 + 7.382*m.i787)*m.i146 + (28.6995072
                        + 2.9479424*m.i787)*m.i146 + 0.001*m.i787 + (55.365 + 18.455*m.i792)*m.i147 + (134.8209408 + 
                       13.8484736*m.i792)*m.i147 + 0.001*m.i792 + (33.219 + 11.073*m.i818)*m.i148 + (71.4150528 + 
                       7.3355776*m.i818)*m.i148 + 0.001*m.i818 + (33.219 + 11.073*m.i823)*m.i149 + (72.7499136 + 
                       7.4726912*m.i823)*m.i149 + 0.001*m.i823 + (44.292 + 14.764*m.i832)*m.i150 + (104.1191424 + 
                       10.6948608*m.i832)*m.i150 + 0.001*m.i832 + (22.146 + 7.382*m.i836)*m.i151 + (28.0320768 + 
                       2.8793856*m.i836)*m.i151 + 0.001*m.i836 + (66.438 + 22.146*m.i850)*m.i152 + (174.1993344 + 
                       17.8933248*m.i850)*m.i152 + 0.001*m.i850 + (22.146 + 7.382*m.i866)*m.i153 + (30.034368 + 3.085056
                       *m.i866)*m.i153 + 0.001*m.i866 + (55.365 + 18.455*m.i867)*m.i154 + (118.8026112 + 12.2031104*
                       m.i867)*m.i154 + 0.001*m.i867 + (44.292 + 14.764*m.i887)*m.i155 + (103.451712 + 10.626304*m.i887)
                       *m.i155 + 0.001*m.i887 + (44.292 + 14.764*m.i930)*m.i156 + (87.4333824 + 8.9809408*m.i930)*m.i156
                        + 0.001*m.i930 + 0.001*m.i157 + 0.001*m.i158 + 0.001*m.i159 + 0.001*m.i161 + 0.001*m.i162
                        + 0.001*m.i163 + 0.001*m.i164 + 0.001*m.i165 + 0.001*m.i166 + 0.001*m.i167 + 0.001*m.i168
                        + 0.001*m.i169 + 0.001*m.i170 + 0.001*m.i171 + 0.001*m.i172 + 0.001*m.i173 + 0.001*m.i174
                        + 0.001*m.i175 + 0.001*m.i176 + 0.001*m.i177 + 0.001*m.i178 + 0.001*m.i179 + 0.001*m.i180
                        + 0.001*m.i181 + 0.001*m.i182 + 0.001*m.i183 + 0.001*m.i184 + 0.001*m.i185 + 0.001*m.i186
                        + 0.001*m.i187 + 0.001*m.i188 + 0.001*m.i189 + 0.001*m.i190 + 0.001*m.i191 + 0.001*m.i192
                        + 0.001*m.i193 + 0.001*m.i195 + 0.001*m.i196 + 0.001*m.i197 + 0.001*m.i198 + 0.001*m.i199
                        + 0.001*m.i200 + 0.001*m.i201 + 0.001*m.i202 + 0.001*m.i203 + 0.001*m.i204 + 0.001*m.i205
                        + 0.001*m.i206 + 0.001*m.i207 + 0.001*m.i208 + 0.001*m.i209 + 0.001*m.i210 + 0.001*m.i211
                        + 0.001*m.i212 + 0.001*m.i214 + 0.001*m.i215 + 0.001*m.i216 + 0.001*m.i217 + 0.001*m.i218
                        + 0.001*m.i219 + 0.001*m.i220 + 0.001*m.i221 + 0.001*m.i222 + 0.001*m.i223 + 0.001*m.i224
                        + 0.001*m.i225 + 0.001*m.i227 + 0.001*m.i228 + 0.001*m.i229 + 0.001*m.i230 + 0.001*m.i231
                        + 0.001*m.i233 + 0.001*m.i234 + 0.001*m.i235 + 0.001*m.i236 + 0.001*m.i237 + 0.001*m.i238
                        + 0.001*m.i239 + 0.001*m.i240 + 0.001*m.i241 + 0.001*m.i242 + 0.001*m.i243 + 0.001*m.i244
                        + 0.001*m.i245 + 0.001*m.i246 + 0.001*m.i247 + 0.001*m.i248 + 0.001*m.i249 + 0.001*m.i250
                        + 0.001*m.i251 + 0.001*m.i252 + 0.001*m.i254 + 0.001*m.i255 + 0.001*m.i256 + 0.001*m.i258
                        + 0.001*m.i259 + 0.001*m.i261 + 0.001*m.i262 + 0.001*m.i263 + 0.001*m.i264 + 0.001*m.i265
                        + 0.001*m.i266 + 0.001*m.i267 + 0.001*m.i268 + 0.001*m.i270 + 0.001*m.i271 + 0.001*m.i272
                        + 0.001*m.i273 + 0.001*m.i274 + 0.001*m.i275 + 0.001*m.i276 + 0.001*m.i277 + 0.001*m.i278
                        + 0.001*m.i279 + 0.001*m.i280 + 0.001*m.i282 + 0.001*m.i283 + 0.001*m.i284 + 0.001*m.i285
                        + 0.001*m.i286 + 0.001*m.i287 + 0.001*m.i288 + 0.001*m.i289 + 0.001*m.i290 + 0.001*m.i291
                        + 0.001*m.i292 + 0.001*m.i293 + 0.001*m.i294 + 0.001*m.i295 + 0.001*m.i296 + 0.001*m.i297
                        + 0.001*m.i298 + 0.001*m.i299 + 0.001*m.i301 + 0.001*m.i302 + 0.001*m.i304 + 0.001*m.i306
                        + 0.001*m.i307 + 0.001*m.i308 + 0.001*m.i309 + 0.001*m.i310 + 0.001*m.i311 + 0.001*m.i312
                        + 0.001*m.i313 + 0.001*m.i314 + 0.001*m.i315 + 0.001*m.i316 + 0.001*m.i317 + 0.001*m.i319
                        + 0.001*m.i320 + 0.001*m.i321 + 0.001*m.i322 + 0.001*m.i323 + 0.001*m.i325 + 0.001*m.i328
                        + 0.001*m.i329 + 0.001*m.i330 + 0.001*m.i331 + 0.001*m.i337 + 0.001*m.i339 + 0.001*m.i340
                        + 0.001*m.i341 + 0.001*m.i342 + 0.001*m.i343 + 0.001*m.i344 + 0.001*m.i346 + 0.001*m.i347
                        + 0.001*m.i348 + 0.001*m.i349 + 0.001*m.i350 + 0.001*m.i351 + 0.001*m.i353 + 0.001*m.i354
                        + 0.001*m.i355 + 0.001*m.i356 + 0.001*m.i358 + 0.001*m.i359 + 0.001*m.i360 + 0.001*m.i361
                        + 0.001*m.i362 + 0.001*m.i363 + 0.001*m.i364 + 0.001*m.i365 + 0.001*m.i366 + 0.001*m.i367
                        + 0.001*m.i368 + 0.001*m.i369 + 0.001*m.i370 + 0.001*m.i371 + 0.001*m.i372 + 0.001*m.i373
                        + 0.001*m.i374 + 0.001*m.i375 + 0.001*m.i376 + 0.001*m.i377 + 0.001*m.i378 + 0.001*m.i379
                        + 0.001*m.i380 + 0.001*m.i381 + 0.001*m.i382 + 0.001*m.i383 + 0.001*m.i384 + 0.001*m.i385
                        + 0.001*m.i386 + 0.001*m.i387 + 0.001*m.i388 + 0.001*m.i389 + 0.001*m.i390 + 0.001*m.i391
                        + 0.001*m.i392 + 0.001*m.i393 + 0.001*m.i394 + 0.001*m.i395 + 0.001*m.i396 + 0.001*m.i397
                        + 0.001*m.i398 + 0.001*m.i399 + 0.001*m.i400 + 0.001*m.i401 + 0.001*m.i402 + 0.001*m.i403
                        + 0.001*m.i404 + 0.001*m.i405 + 0.001*m.i406 + 0.001*m.i407 + 0.001*m.i408 + 0.001*m.i409
                        + 0.001*m.i410 + 0.001*m.i411 + 0.001*m.i412 + 0.001*m.i413 + 0.001*m.i414 + 0.001*m.i415
                        + 0.001*m.i416 + 0.001*m.i417 + 0.001*m.i418 + 0.001*m.i419 + 0.001*m.i420 + 0.001*m.i421
                        + 0.001*m.i422 + 0.001*m.i423 + 0.001*m.i424 + 0.001*m.i425 + 0.001*m.i426 + 0.001*m.i427
                        + 0.001*m.i428 + 0.001*m.i429 + 0.001*m.i431 + 0.001*m.i432 + 0.001*m.i433 + 0.001*m.i434
                        + 0.001*m.i435 + 0.001*m.i437 + 0.001*m.i438 + 0.001*m.i439 + 0.001*m.i440 + 0.001*m.i441
                        + 0.001*m.i442 + 0.001*m.i443 + 0.001*m.i444 + 0.001*m.i445 + 0.001*m.i446 + 0.001*m.i447
                        + 0.001*m.i448 + 0.001*m.i449 + 0.001*m.i450 + 0.001*m.i452 + 0.001*m.i453 + 0.001*m.i454
                        + 0.001*m.i455 + 0.001*m.i456 + 0.001*m.i457 + 0.001*m.i458 + 0.001*m.i459 + 0.001*m.i460
                        + 0.001*m.i461 + 0.001*m.i462 + 0.001*m.i463 + 0.001*m.i464 + 0.001*m.i465 + 0.001*m.i466
                        + 0.001*m.i467 + 0.001*m.i468 + 0.001*m.i469 + 0.001*m.i470 + 0.001*m.i471 + 0.001*m.i472
                        + 0.001*m.i473 + 0.001*m.i474 + 0.001*m.i475 + 0.001*m.i476 + 0.001*m.i477 + 0.001*m.i478
                        + 0.001*m.i479 + 0.001*m.i480 + 0.001*m.i481 + 0.001*m.i482 + 0.001*m.i483 + 0.001*m.i484
                        + 0.001*m.i485 + 0.001*m.i486 + 0.001*m.i487 + 0.001*m.i488 + 0.001*m.i489 + 0.001*m.i490
                        + 0.001*m.i491 + 0.001*m.i492 + 0.001*m.i493 + 0.001*m.i494 + 0.001*m.i495 + 0.001*m.i496
                        + 0.001*m.i497 + 0.001*m.i498 + 0.001*m.i500 + 0.001*m.i501 + 0.001*m.i502 + 0.001*m.i503
                        + 0.001*m.i504 + 0.001*m.i505 + 0.001*m.i506 + 0.001*m.i508 + 0.001*m.i509 + 0.001*m.i510
                        + 0.001*m.i511 + 0.001*m.i512 + 0.001*m.i513 + 0.001*m.i514 + 0.001*m.i515 + 0.001*m.i516
                        + 0.001*m.i517 + 0.001*m.i518 + 0.001*m.i520 + 0.001*m.i521 + 0.001*m.i522 + 0.001*m.i523
                        + 0.001*m.i524 + 0.001*m.i525 + 0.001*m.i526 + 0.001*m.i528 + 0.001*m.i529 + 0.001*m.i530
                        + 0.001*m.i531 + 0.001*m.i532 + 0.001*m.i533 + 0.001*m.i534 + 0.001*m.i535 + 0.001*m.i536
                        + 0.001*m.i537 + 0.001*m.i538 + 0.001*m.i539 + 0.001*m.i540 + 0.001*m.i541 + 0.001*m.i542
                        + 0.001*m.i543 + 0.001*m.i544 + 0.001*m.i545 + 0.001*m.i546 + 0.001*m.i548 + 0.001*m.i549
                        + 0.001*m.i550 + 0.001*m.i551 + 0.001*m.i552 + 0.001*m.i553 + 0.001*m.i554 + 0.001*m.i555
                        + 0.001*m.i556 + 0.001*m.i557 + 0.001*m.i558 + 0.001*m.i559 + 0.001*m.i561 + 0.001*m.i562
                        + 0.001*m.i563 + 0.001*m.i565 + 0.001*m.i566 + 0.001*m.i567 + 0.001*m.i568 + 0.001*m.i569
                        + 0.001*m.i570 + 0.001*m.i571 + 0.001*m.i572 + 0.001*m.i573 + 0.001*m.i574 + 0.001*m.i575
                        + 0.001*m.i576 + 0.001*m.i577 + 0.001*m.i578 + 0.001*m.i579 + 0.001*m.i580 + 0.001*m.i581
                        + 0.001*m.i582 + 0.001*m.i583 + 0.001*m.i585 + 0.001*m.i586 + 0.001*m.i587 + 0.001*m.i588
                        + 0.001*m.i589 + 0.001*m.i590 + 0.001*m.i591 + 0.001*m.i592 + 0.001*m.i593 + 0.001*m.i594
                        + 0.001*m.i595 + 0.001*m.i596 + 0.001*m.i598 + 0.001*m.i599 + 0.001*m.i600 + 0.001*m.i601
                        + 0.001*m.i603 + 0.001*m.i604 + 0.001*m.i605 + 0.001*m.i606 + 0.001*m.i607 + 0.001*m.i608
                        + 0.001*m.i609 + 0.001*m.i611 + 0.001*m.i612 + 0.001*m.i614 + 0.001*m.i615 + 0.001*m.i617
                        + 0.001*m.i618 + 0.001*m.i619 + 0.001*m.i620 + 0.001*m.i621 + 0.001*m.i622 + 0.001*m.i623
                        + 0.001*m.i624 + 0.001*m.i625 + 0.001*m.i626 + 0.001*m.i627 + 0.001*m.i630 + 0.001*m.i631
                        + 0.001*m.i632 + 0.001*m.i633 + 0.001*m.i635 + 0.001*m.i636 + 0.001*m.i637 + 0.001*m.i638
                        + 0.001*m.i639 + 0.001*m.i640 + 0.001*m.i643 + 0.001*m.i644 + 0.001*m.i645 + 0.001*m.i646
                        + 0.001*m.i647 + 0.001*m.i648 + 0.001*m.i649 + 0.001*m.i650 + 0.001*m.i651 + 0.001*m.i652
                        + 0.001*m.i653 + 0.001*m.i654 + 0.001*m.i655 + 0.001*m.i656 + 0.001*m.i657 + 0.001*m.i658
                        + 0.001*m.i659 + 0.001*m.i660 + 0.001*m.i661 + 0.001*m.i662 + 0.001*m.i663 + 0.001*m.i664
                        + 0.001*m.i665 + 0.001*m.i666 + 0.001*m.i667 + 0.001*m.i668 + 0.001*m.i669 + 0.001*m.i670
                        + 0.001*m.i671 + 0.001*m.i672 + 0.001*m.i673 + 0.001*m.i674 + 0.001*m.i675 + 0.001*m.i676
                        + 0.001*m.i677 + 0.001*m.i678 + 0.001*m.i679 + 0.001*m.i680 + 0.001*m.i681 + 0.001*m.i682
                        + 0.001*m.i683 + 0.001*m.i684 + 0.001*m.i685 + 0.001*m.i686 + 0.001*m.i687 + 0.001*m.i688
                        + 0.001*m.i689 + 0.001*m.i690 + 0.001*m.i691 + 0.001*m.i693 + 0.001*m.i694 + 0.001*m.i695
                        + 0.001*m.i696 + 0.001*m.i697 + 0.001*m.i698 + 0.001*m.i699 + 0.001*m.i700 + 0.001*m.i701
                        + 0.001*m.i702 + 0.001*m.i703 + 0.001*m.i704 + 0.001*m.i705 + 0.001*m.i706 + 0.001*m.i707
                        + 0.001*m.i708 + 0.001*m.i709 + 0.001*m.i710 + 0.001*m.i711 + 0.001*m.i713 + 0.001*m.i714
                        + 0.001*m.i715 + 0.001*m.i717 + 0.001*m.i718 + 0.001*m.i719 + 0.001*m.i720 + 0.001*m.i721
                        + 0.001*m.i722 + 0.001*m.i724 + 0.001*m.i725 + 0.001*m.i726 + 0.001*m.i727 + 0.001*m.i728
                        + 0.001*m.i729 + 0.001*m.i730 + 0.001*m.i731 + 0.001*m.i732 + 0.001*m.i733 + 0.001*m.i735
                        + 0.001*m.i736 + 0.001*m.i737 + 0.001*m.i738 + 0.001*m.i739 + 0.001*m.i740 + 0.001*m.i741
                        + 0.001*m.i742 + 0.001*m.i743 + 0.001*m.i745 + 0.001*m.i746 + 0.001*m.i747 + 0.001*m.i748
                        + 0.001*m.i749 + 0.001*m.i751 + 0.001*m.i752 + 0.001*m.i753 + 0.001*m.i754 + 0.001*m.i755
                        + 0.001*m.i756 + 0.001*m.i757 + 0.001*m.i758 + 0.001*m.i759 + 0.001*m.i760 + 0.001*m.i762
                        + 0.001*m.i763 + 0.001*m.i764 + 0.001*m.i765 + 0.001*m.i766 + 0.001*m.i767 + 0.001*m.i768
                        + 0.001*m.i769 + 0.001*m.i770 + 0.001*m.i771 + 0.001*m.i772 + 0.001*m.i773 + 0.001*m.i774
                        + 0.001*m.i775 + 0.001*m.i776 + 0.001*m.i777 + 0.001*m.i778 + 0.001*m.i779 + 0.001*m.i780
                        + 0.001*m.i781 + 0.001*m.i783 + 0.001*m.i785 + 0.001*m.i786 + 0.001*m.i788 + 0.001*m.i789
                        + 0.001*m.i790 + 0.001*m.i791 + 0.001*m.i793 + 0.001*m.i794 + 0.001*m.i795 + 0.001*m.i796
                        + 0.001*m.i797 + 0.001*m.i798 + 0.001*m.i799 + 0.001*m.i800 + 0.001*m.i801 + 0.001*m.i802
                        + 0.001*m.i803 + 0.001*m.i804 + 0.001*m.i805 + 0.001*m.i806 + 0.001*m.i807 + 0.001*m.i808
                        + 0.001*m.i809 + 0.001*m.i810 + 0.001*m.i811 + 0.001*m.i812 + 0.001*m.i813 + 0.001*m.i814
                        + 0.001*m.i815 + 0.001*m.i816 + 0.001*m.i817 + 0.001*m.i819 + 0.001*m.i820 + 0.001*m.i821
                        + 0.001*m.i822 + 0.001*m.i824 + 0.001*m.i825 + 0.001*m.i826 + 0.001*m.i827 + 0.001*m.i828
                        + 0.001*m.i829 + 0.001*m.i830 + 0.001*m.i831 + 0.001*m.i833 + 0.001*m.i834 + 0.001*m.i835
                        + 0.001*m.i837 + 0.001*m.i838 + 0.001*m.i839 + 0.001*m.i840 + 0.001*m.i841 + 0.001*m.i842
                        + 0.001*m.i843 + 0.001*m.i844 + 0.001*m.i845 + 0.001*m.i846 + 0.001*m.i847 + 0.001*m.i848
                        + 0.001*m.i849 + 0.001*m.i851 + 0.001*m.i852 + 0.001*m.i853 + 0.001*m.i854 + 0.001*m.i855
                        + 0.001*m.i856 + 0.001*m.i857 + 0.001*m.i858 + 0.001*m.i859 + 0.001*m.i860 + 0.001*m.i861
                        + 0.001*m.i862 + 0.001*m.i863 + 0.001*m.i864 + 0.001*m.i865 + 0.001*m.i868 + 0.001*m.i869
                        + 0.001*m.i870 + 0.001*m.i871 + 0.001*m.i872 + 0.001*m.i873 + 0.001*m.i874 + 0.001*m.i875
                        + 0.001*m.i876 + 0.001*m.i877 + 0.001*m.i878 + 0.001*m.i879 + 0.001*m.i880 + 0.001*m.i881
                        + 0.001*m.i882 + 0.001*m.i883 + 0.001*m.i884 + 0.001*m.i885 + 0.001*m.i886 + 0.001*m.i888
                        + 0.001*m.i889 + 0.001*m.i890 + 0.001*m.i891 + 0.001*m.i892 + 0.001*m.i893 + 0.001*m.i894
                        + 0.001*m.i895 + 0.001*m.i896 + 0.001*m.i897 + 0.001*m.i898 + 0.001*m.i899 + 0.001*m.i900
                        + 0.001*m.i901 + 0.001*m.i902 + 0.001*m.i903 + 0.001*m.i904 + 0.001*m.i905 + 0.001*m.i906
                        + 0.001*m.i907 + 0.001*m.i908 + 0.001*m.i909 + 0.001*m.i910 + 0.001*m.i911 + 0.001*m.i912
                        + 0.001*m.i913 + 0.001*m.i914 + 0.001*m.i915 + 0.001*m.i916 + 0.001*m.i917 + 0.001*m.i918
                        + 0.001*m.i919 + 0.001*m.i920 + 0.001*m.i921 + 0.001*m.i922 + 0.001*m.i923 + 0.001*m.i924
                        + 0.001*m.i925 + 0.001*m.i926 + 0.001*m.i927 + 0.001*m.i928 + 0.001*m.i929 + 0.001*m.i931
                        + 0.001*m.i932 + 0.001*m.i933 + 0.001*m.i934 + 0.001*m.i935 + 0.001*m.i936 + 0.001*m.i937
                        + 0.001*m.i938 + 0.001*m.i939 + 0.001*m.i940 + 0.001*m.i941 + 0.001*m.i942 + 0.001*m.i943
                        + 0.001*m.i944 + 0.001*m.i945 + 0.001*m.i946 + 0.001*m.i947 + 0.001*m.i948 + 0.001*m.i949
                        + 0.001*m.i950 + 0.001*m.i951 + 0.001*m.i952 + 0.001*m.i953 + 0.001*m.i954 + 0.001*m.i955
                        + 0.001*m.i956 + 0.001*m.i957 + 0.001*m.i958 + 0.001*m.i959 + 0.001*m.i960 + 0.001*m.i961
                        + 0.001*m.i962 + 0.001*m.i963 + 0.001*m.i964 + 0.001*m.i965 + 0.001*m.i966 + 0.001*m.i967
                        + 0.001*m.i968 + 0.001*m.i969 + 0.001*m.i970 + 0.001*m.i971 + 0.001*m.i972 + 0.001*m.i973
                        + 0.001*m.i974 + 0.001*m.i975 + 0.001*m.i976 + 0.001*m.i977 + 0.001*m.i978 + 0.001*m.i979
                        + 0.001*m.i980 + 0.001*m.i981 + 0.001*m.i982 + 0.001*m.i983 + 0.001*m.i984 + 0.001*m.i985
                        + 0.001*m.i986 + 0.001*m.i987, sense=minimize)

m.c1 = Constraint(expr=   m.x1 - m.i121 - m.i123 - m.i132 - m.i137 - m.i139 - m.i140 == 0)

m.c2 = Constraint(expr=   m.x2 - m.i89 - m.i90 - m.i119 - m.i123 - m.i128 - m.i150 == 0)

m.c3 = Constraint(expr=   m.x3 - m.i119 - m.i121 - m.i128 - m.i132 - m.i137 - m.i139 - m.i140 - m.i150 == 0)

m.c4 = Constraint(expr=   m.x4 - m.i97 - m.i100 - m.i101 - m.i102 - m.i124 - m.i125 - m.i134 - m.i138 - m.i152 == 0)

m.c5 = Constraint(expr=   m.x5 - m.i91 - m.i101 - m.i108 - m.i112 == 0)

m.c6 = Constraint(expr=   m.x6 - m.i95 - m.i125 - m.i138 == 0)

m.c7 = Constraint(expr=   m.x7 - m.i92 - m.i93 - m.i94 - m.i96 - m.i97 - m.i100 - m.i102 - m.i124 - m.i126 - m.i130
                        - m.i133 - m.i134 - m.i135 - m.i152 == 0)

m.c8 = Constraint(expr=   m.x8 - m.i108 - m.i112 - m.i126 - m.i130 - m.i133 - m.i135 == 0)

m.c9 = Constraint(expr=   m.x9 - m.i97 - m.i98 - m.i121 - m.i123 - m.i124 - m.i125 - m.i137 - m.i138 - m.i139 - m.i140
                        == 0)

m.c10 = Constraint(expr=   m.x10 - m.i121 - m.i123 - m.i124 - m.i125 - m.i137 - m.i138 - m.i139 - m.i140 == 0)

m.c11 = Constraint(expr=   m.x11 - m.i97 - m.i99 - m.i124 - m.i125 - m.i134 - m.i138 - m.i152 == 0)

m.c12 = Constraint(expr=   m.x12 - m.i89 - m.i106 - m.i114 - m.i118 - m.i141 - m.i142 - m.i143 - m.i148 == 0)

m.c13 = Constraint(expr=   m.x13 - m.i101 - m.i105 - m.i110 - m.i111 - m.i113 - m.i118 - m.i141 - m.i142 - m.i143 == 0)

m.c14 = Constraint(expr=   m.x14 - m.i103 - m.i104 - m.i107 - m.i109 - m.i148 == 0)

m.c15 = Constraint(expr=   m.x15 - m.i99 - m.i108 - m.i126 - m.i131 - m.i132 - m.i133 - m.i134 - m.i135 == 0)

m.c16 = Constraint(expr=   m.x16 - m.i99 - m.i108 - m.i126 - m.i131 - m.i132 - m.i133 - m.i134 - m.i135 == 0)

m.c17 = Constraint(expr=   m.x17 - m.i103 - m.i122 - m.i129 - m.i136 - m.i147 - m.i155 == 0)

m.c18 = Constraint(expr=   m.x18 - m.i94 - m.i129 - m.i133 - m.i136 - m.i139 - m.i154 - m.i156 == 0)

m.c19 = Constraint(expr=   m.x19 - m.i94 - m.i122 - m.i133 - m.i139 - m.i147 - m.i154 - m.i155 - m.i156 == 0)

m.c20 = Constraint(expr=   m.x20 - m.i90 - m.i113 - m.i155 == 0)

m.c21 = Constraint(expr=   m.x21 - m.i90 - m.i97 - m.i103 - m.i104 - m.i105 - m.i113 - m.i115 - m.i116 - m.i117 - m.i122
                         - m.i129 - m.i136 - m.i147 == 0)

m.c22 = Constraint(expr=   m.x22 - m.i98 - m.i99 - m.i132 - m.i134 - m.i152 == 0)

m.c23 = Constraint(expr=   m.x23 - m.i95 - m.i125 - m.i138 == 0)

m.c24 = Constraint(expr=   m.x24 - m.i89 - m.i106 - m.i114 - m.i118 - m.i141 - m.i142 - m.i143 - m.i148 == 0)

m.c25 = Constraint(expr=   m.x25 - m.i89 - m.i90 - m.i118 - m.i123 - m.i128 - m.i150 == 0)

m.c26 = Constraint(expr=   m.x26 - m.i96 - m.i114 - m.i119 - m.i120 - m.i121 - m.i135 - m.i137 - m.i140 - m.i142
                         - m.i143 == 0)

m.c27 = Constraint(expr=   m.x27 - m.i122 - m.i144 - m.i147 - m.i149 - m.i154 - m.i156 == 0)

m.c28 = Constraint(expr=   m.x28 - m.i96 - m.i135 - m.i140 - m.i143 - m.i149 - m.i156 == 0)

m.c29 = Constraint(expr=   m.x29 - m.i114 - m.i119 - m.i137 - m.i142 - m.i144 - m.i147 - m.i154 == 0)

m.c30 = Constraint(expr=   m.x30 - m.i123 - m.i124 - m.i125 == 0)

m.c31 = Constraint(expr=   m.x31 - m.i102 - m.i107 - m.i124 - m.i127 - m.i150 == 0)

m.c32 = Constraint(expr=   m.x32 - m.i90 - m.i93 - m.i97 - m.i100 - m.i129 - m.i152 == 0)

m.c33 = Constraint(expr=   m.x33 - m.i90 - m.i92 - m.i93 - m.i97 - m.i100 - m.i102 - m.i106 - m.i120 - m.i123 - m.i124
                         - m.i126 - m.i128 - m.i130 - m.i150 - m.i152 == 0)

m.c34 = Constraint(expr=   m.x34 - m.i93 - m.i100 - m.i102 - m.i115 - m.i117 - m.i127 - m.i136 - m.i151 == 0)

m.c35 = Constraint(expr=   m.x35 - m.i103 - m.i104 - m.i105 - m.i109 - m.i110 - m.i113 - m.i116 - m.i127 == 0)

m.c36 = Constraint(expr=   m.x36 - m.i93 - m.i100 - m.i102 - m.i103 - m.i104 - m.i105 - m.i113 - m.i115 - m.i116
                         - m.i117 - m.i136 - m.i151 == 0)

m.c37 = Constraint(expr=   m.x37 - m.i107 - m.i111 - m.i115 - m.i117 - m.i150 - m.i151 == 0)

m.c38 = Constraint(expr=   m.x38 - m.i105 - m.i110 - m.i111 - m.i113 - m.i115 - m.i127 == 0)

m.c39 = Constraint(expr=   m.x39 - m.i98 - m.i112 - m.i131 - m.i152 == 0)

m.c40 = Constraint(expr=   m.x40 - m.i98 - m.i112 - m.i131 - m.i152 == 0)

m.c41 = Constraint(expr=   m.x41 - m.i137 - m.i144 - m.i145 - m.i146 - m.i147 == 0)

m.c42 = Constraint(expr=   m.x42 - m.i119 - m.i121 - m.i137 - m.i139 - m.i140 - m.i155 == 0)

m.c43 = Constraint(expr=   m.x43 - m.i94 - m.i133 - m.i139 - m.i144 - m.i149 - m.i155 == 0)

m.c44 = Constraint(expr=   m.x44 - m.i94 - m.i96 - m.i114 - m.i120 - m.i133 - m.i135 - m.i141 - m.i142 - m.i143 - m.i148
                         == 0)

m.c45 = Constraint(expr=   m.x45 - m.i103 - m.i104 - m.i107 - m.i109 - m.i117 - m.i138 == 0)

m.c46 = Constraint(expr=   m.x46 - m.i119 - m.i145 - m.i153 - m.i154 == 0)

m.c47 = Constraint(expr=   m.x47 - m.i114 - m.i119 - m.i137 - m.i144 - m.i146 - m.i147 - m.i153 - m.i154 == 0)

m.c48 = Constraint(expr=   m.x48 - m.i114 - m.i119 - m.i137 - m.i142 - m.i144 - m.i147 - m.i154 == 0)

m.c49 = Constraint(expr=-((3 + m.i527)*m.i121 + (3 + m.i560)*m.i123 + (3 + m.i629)*m.i132 + (3 + m.i712)*m.i137 + (3 + 
                        m.i723)*m.i139 + (3 + m.i734)*m.i140) + m.x49 == 0)

m.c50 = Constraint(expr=-((3 + m.i160)*m.i89 + (3 + m.i194)*m.i90 + (3 + m.i507)*m.i119 + (3 + m.i560)*m.i123 + (3 + 
                        m.i610)*m.i128 + (3 + m.i832)*m.i150) + m.x50 == 0)

m.c51 = Constraint(expr=-((3 + m.i507)*m.i119 + (3 + m.i527)*m.i121 + (3 + m.i610)*m.i128 + (3 + m.i629)*m.i132 + (3 + 
                        m.i712)*m.i137 + (3 + m.i723)*m.i139 + (3 + m.i734)*m.i140 + (3 + m.i832)*m.i150) + m.x51 == 0)

m.c52 = Constraint(expr=-((3 + m.i269)*m.i97 + (3 + m.i303)*m.i100 + (3 + m.i305)*m.i101 + (3 + m.i318)*m.i102 + (3 + 
                        m.i564)*m.i124 + (3 + m.i584)*m.i125 + (3 + m.i641)*m.i134 + (3 + m.i716)*m.i138 + (3 + m.i850)*
                        m.i152) + m.x52 == 0)

m.c53 = Constraint(expr=-((3 + m.i213)*m.i91 + (3 + m.i305)*m.i101 + (3 + m.i334)*m.i108 + (3 + m.i345)*m.i112) + m.x53
                         == 0)

m.c54 = Constraint(expr=-((3 + m.i257)*m.i95 + (3 + m.i584)*m.i125 + (3 + m.i716)*m.i138) + m.x54 == 0)

m.c55 = Constraint(expr=-((3 + m.i226)*m.i92 + (3 + m.i232)*m.i93 + (3 + m.i253)*m.i94 + (3 + m.i260)*m.i96 + (3 + 
                        m.i269)*m.i97 + (3 + m.i303)*m.i100 + (3 + m.i318)*m.i102 + (3 + m.i564)*m.i124 + (3 + m.i597)*
                        m.i126 + (3 + m.i616)*m.i130 + (3 + m.i634)*m.i133 + (3 + m.i641)*m.i134 + (3 + m.i642)*m.i135
                         + (3 + m.i850)*m.i152) + m.x55 == 0)

m.c56 = Constraint(expr=-((3 + m.i334)*m.i108 + (3 + m.i345)*m.i112 + (3 + m.i597)*m.i126 + (3 + m.i616)*m.i130 + (3 + 
                        m.i634)*m.i133 + (3 + m.i642)*m.i135) + m.x56 == 0)

m.c57 = Constraint(expr=-((3 + m.i269)*m.i97 + (3 + m.i281)*m.i98 + (3 + m.i527)*m.i121 + (3 + m.i560)*m.i123 + (3 + 
                        m.i564)*m.i124 + (3 + m.i584)*m.i125 + (3 + m.i712)*m.i137 + (3 + m.i716)*m.i138 + (3 + m.i723)*
                        m.i139 + (3 + m.i734)*m.i140) + m.x57 == 0)

m.c58 = Constraint(expr=-((3 + m.i160)*m.i89 + (3 + m.i332)*m.i106 + (3 + m.i357)*m.i114 + (3 + m.i499)*m.i118 + (3 + 
                        m.i744)*m.i141 + (3 + m.i750)*m.i142 + (3 + m.i761)*m.i143 + (3 + m.i818)*m.i148) + m.x58 == 0)

m.c59 = Constraint(expr=-((3 + m.i305)*m.i101 + (3 + m.i327)*m.i105 + (3 + m.i336)*m.i110 + (3 + m.i338)*m.i111 + (3 + 
                        m.i352)*m.i113 + (3 + m.i499)*m.i118 + (3 + m.i744)*m.i141 + (3 + m.i750)*m.i142 + (3 + m.i761)*
                        m.i143) + m.x59 == 0)

m.c60 = Constraint(expr=-((3 + m.i324)*m.i103 + (3 + m.i326)*m.i104 + (3 + m.i333)*m.i107 + (3 + m.i335)*m.i109 + (3 + 
                        m.i818)*m.i148) + m.x60 == 0)

m.c61 = Constraint(expr=-((3 + m.i300)*m.i99 + (3 + m.i334)*m.i108 + (3 + m.i597)*m.i126 + (3 + m.i628)*m.i131 + (3 + 
                        m.i629)*m.i132 + (3 + m.i634)*m.i133 + (3 + m.i641)*m.i134 + (3 + m.i642)*m.i135) + m.x61 == 0)

m.c62 = Constraint(expr=-((3 + m.i300)*m.i99 + (3 + m.i334)*m.i108 + (3 + m.i597)*m.i126 + (3 + m.i628)*m.i131 + (3 + 
                        m.i629)*m.i132 + (3 + m.i634)*m.i133 + (3 + m.i641)*m.i134 + (3 + m.i642)*m.i135) + m.x62 == 0)

m.c63 = Constraint(expr=-((3 + m.i324)*m.i103 + (3 + m.i547)*m.i122 + (3 + m.i613)*m.i129 + (3 + m.i692)*m.i136 + (3 + 
                        m.i792)*m.i147 + (3 + m.i887)*m.i155) + m.x63 == 0)

m.c64 = Constraint(expr=-((3 + m.i253)*m.i94 + (3 + m.i547)*m.i122 + (3 + m.i634)*m.i133 + (3 + m.i723)*m.i139 + (3 + 
                        m.i792)*m.i147 + (3 + m.i867)*m.i154 + (3 + m.i887)*m.i155 + (3 + m.i930)*m.i156) + m.x64 == 0)

m.c65 = Constraint(expr=-((3 + m.i194)*m.i90 + (3 + m.i269)*m.i97 + (3 + m.i324)*m.i103 + (3 + m.i326)*m.i104 + (3 + 
                        m.i327)*m.i105 + (3 + m.i352)*m.i113 + (3 + m.i430)*m.i115 + (3 + m.i436)*m.i116 + (3 + m.i451)*
                        m.i117 + (3 + m.i547)*m.i122 + (3 + m.i613)*m.i129 + (3 + m.i692)*m.i136 + (3 + m.i792)*m.i147)
                         + m.x65 == 0)

m.c66 = Constraint(expr=-((3 + m.i281)*m.i98 + (3 + m.i300)*m.i99 + (3 + m.i629)*m.i132 + (3 + m.i641)*m.i134 + (3 + 
                        m.i850)*m.i152) + m.x66 == 0)

m.c67 = Constraint(expr=-((3 + m.i257)*m.i95 + (3 + m.i584)*m.i125 + (3 + m.i716)*m.i138) + m.x67 == 0)

m.c68 = Constraint(expr=-((3 + m.i160)*m.i89 + (3 + m.i332)*m.i106 + (3 + m.i357)*m.i114 + (3 + m.i499)*m.i118 + (3 + 
                        m.i744)*m.i141 + (3 + m.i750)*m.i142 + (3 + m.i761)*m.i143 + (3 + m.i818)*m.i148) + m.x68 == 0)

m.c69 = Constraint(expr=-((3 + m.i160)*m.i89 + (3 + m.i194)*m.i90 + (3 + m.i499)*m.i118 + (3 + m.i560)*m.i123 + (3 + 
                        m.i610)*m.i128 + (3 + m.i832)*m.i150) + m.x69 == 0)

m.c70 = Constraint(expr=-((3 + m.i260)*m.i96 + (3 + m.i357)*m.i114 + (3 + m.i507)*m.i119 + (3 + m.i519)*m.i120 + (3 + 
                        m.i527)*m.i121 + (3 + m.i642)*m.i135 + (3 + m.i712)*m.i137 + (3 + m.i734)*m.i140 + (3 + m.i750)*
                        m.i142 + (3 + m.i761)*m.i143) + m.x70 == 0)

m.c71 = Constraint(expr=-((3 + m.i260)*m.i96 + (3 + m.i642)*m.i135 + (3 + m.i734)*m.i140 + (3 + m.i761)*m.i143 + (3 + 
                        m.i823)*m.i149 + (3 + m.i930)*m.i156) + m.x71 == 0)

m.c72 = Constraint(expr=-((3 + m.i357)*m.i114 + (3 + m.i507)*m.i119 + (3 + m.i712)*m.i137 + (3 + m.i750)*m.i142 + (3 + 
                        m.i782)*m.i144 + (3 + m.i792)*m.i147 + (3 + m.i867)*m.i154) + m.x72 == 0)

m.c73 = Constraint(expr=-((3 + m.i560)*m.i123 + (3 + m.i564)*m.i124 + (3 + m.i584)*m.i125) + m.x73 == 0)

m.c74 = Constraint(expr=-((3 + m.i318)*m.i102 + (3 + m.i333)*m.i107 + (3 + m.i564)*m.i124 + (3 + m.i602)*m.i127 + (3 + 
                        m.i832)*m.i150) + m.x74 == 0)

m.c75 = Constraint(expr=-((3 + m.i194)*m.i90 + (3 + m.i232)*m.i93 + (3 + m.i269)*m.i97 + (3 + m.i303)*m.i100 + (3 + 
                        m.i613)*m.i129 + (3 + m.i850)*m.i152) + m.x75 == 0)

m.c76 = Constraint(expr=-((3 + m.i194)*m.i90 + (3 + m.i226)*m.i92 + (3 + m.i232)*m.i93 + (3 + m.i269)*m.i97 + (3 + 
                        m.i303)*m.i100 + (3 + m.i318)*m.i102 + (3 + m.i332)*m.i106 + (3 + m.i519)*m.i120 + (3 + m.i560)*
                        m.i123 + (3 + m.i564)*m.i124 + (3 + m.i597)*m.i126 + (3 + m.i610)*m.i128 + (3 + m.i616)*m.i130
                         + (3 + m.i832)*m.i150 + (3 + m.i850)*m.i152) + m.x76 == 0)

m.c77 = Constraint(expr=-((3 + m.i232)*m.i93 + (3 + m.i303)*m.i100 + (3 + m.i318)*m.i102 + (3 + m.i430)*m.i115 + (3 + 
                        m.i451)*m.i117 + (3 + m.i602)*m.i127 + (3 + m.i692)*m.i136 + (3 + m.i836)*m.i151) + m.x77 == 0)

m.c78 = Constraint(expr=-((3 + m.i324)*m.i103 + (3 + m.i326)*m.i104 + (3 + m.i327)*m.i105 + (3 + m.i335)*m.i109 + (3 + 
                        m.i336)*m.i110 + (3 + m.i352)*m.i113 + (3 + m.i436)*m.i116 + (3 + m.i602)*m.i127) + m.x78 == 0)

m.c79 = Constraint(expr=-((3 + m.i232)*m.i93 + (3 + m.i303)*m.i100 + (3 + m.i318)*m.i102 + (3 + m.i324)*m.i103 + (3 + 
                        m.i326)*m.i104 + (3 + m.i327)*m.i105 + (3 + m.i352)*m.i113 + (3 + m.i430)*m.i115 + (3 + m.i436)*
                        m.i116 + (3 + m.i451)*m.i117 + (3 + m.i692)*m.i136 + (3 + m.i836)*m.i151) + m.x79 == 0)

m.c80 = Constraint(expr=-((3 + m.i333)*m.i107 + (3 + m.i338)*m.i111 + (3 + m.i430)*m.i115 + (3 + m.i451)*m.i117 + (3 + 
                        m.i832)*m.i150 + (3 + m.i836)*m.i151) + m.x80 == 0)

m.c81 = Constraint(expr=-((3 + m.i327)*m.i105 + (3 + m.i336)*m.i110 + (3 + m.i338)*m.i111 + (3 + m.i352)*m.i113 + (3 + 
                        m.i430)*m.i115 + (3 + m.i602)*m.i127) + m.x81 == 0)

m.c82 = Constraint(expr=-((3 + m.i281)*m.i98 + (3 + m.i345)*m.i112 + (3 + m.i628)*m.i131 + (3 + m.i850)*m.i152) + m.x82
                         == 0)

m.c83 = Constraint(expr=-((3 + m.i281)*m.i98 + (3 + m.i345)*m.i112 + (3 + m.i628)*m.i131 + (3 + m.i850)*m.i152) + m.x83
                         == 0)

m.c84 = Constraint(expr=-((3 + m.i253)*m.i94 + (3 + m.i260)*m.i96 + (3 + m.i357)*m.i114 + (3 + m.i519)*m.i120 + (3 + 
                        m.i634)*m.i133 + (3 + m.i642)*m.i135 + (3 + m.i744)*m.i141 + (3 + m.i750)*m.i142 + (3 + m.i761)*
                        m.i143 + (3 + m.i818)*m.i148) + m.x84 == 0)

m.c85 = Constraint(expr=-((3 + m.i324)*m.i103 + (3 + m.i326)*m.i104 + (3 + m.i333)*m.i107 + (3 + m.i335)*m.i109 + (3 + 
                        m.i451)*m.i117 + (3 + m.i716)*m.i138) + m.x85 == 0)

m.c86 = Constraint(expr=-((3 + m.i357)*m.i114 + (3 + m.i507)*m.i119 + (3 + m.i712)*m.i137 + (3 + m.i782)*m.i144 + (3 + 
                        m.i787)*m.i146 + (3 + m.i792)*m.i147 + (3 + m.i866)*m.i153 + (3 + m.i867)*m.i154) + m.x86 == 0)

m.c87 = Constraint(expr=-((3 + m.i357)*m.i114 + (3 + m.i507)*m.i119 + (3 + m.i712)*m.i137 + (3 + m.i750)*m.i142 + (3 + 
                        m.i782)*m.i144 + (3 + m.i792)*m.i147 + (3 + m.i867)*m.i154) + m.x87 == 0)
