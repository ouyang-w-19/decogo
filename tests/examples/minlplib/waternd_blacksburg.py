#  MINLP written by GAMS Convert at 04/21/18 13:55:13
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        206      136       35       35        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        592      102      490        0        0        0        0        0
#  FX     13        1       12        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1854     1714      140        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(715.564563,715.564563),initialize=715.564563)
m.x2 = Var(within=Reals,bounds=(682.578941,715.568941),initialize=682.578941)
m.x3 = Var(within=Reals,bounds=(679.835732,715.565732),initialize=679.835732)
m.x4 = Var(within=Reals,bounds=(676.482921,715.572921),initialize=676.482921)
m.x5 = Var(within=Reals,bounds=(686.388954,715.568954),initialize=686.388954)
m.x6 = Var(within=Reals,bounds=(682.731342,715.571342),initialize=682.731342)
m.x7 = Var(within=Reals,bounds=(678.921329,715.571329),initialize=678.921329)
m.x8 = Var(within=Reals,bounds=(678.311727,715.571727),initialize=678.311727)
m.x9 = Var(within=Reals,bounds=(678.311727,715.571727),initialize=678.311727)
m.x10 = Var(within=Reals,bounds=(672.97771,715.56771),initialize=672.97771)
m.x11 = Var(within=Reals,bounds=(676.482921,715.572921),initialize=676.482921)
m.x12 = Var(within=Reals,bounds=(681.969339,715.569339),initialize=681.969339)
m.x13 = Var(within=Reals,bounds=(673.13011,715.57011),initialize=673.13011)
m.x14 = Var(within=Reals,bounds=(681.207337,715.567337),initialize=681.207337)
m.x15 = Var(within=Reals,bounds=(683.188543,715.568543),initialize=683.188543)
m.x16 = Var(within=Reals,bounds=(683.493344,715.413344),initialize=683.493344)
m.x17 = Var(within=Reals,bounds=(685.017349,715.567349),initialize=685.017349)
m.x18 = Var(within=Reals,bounds=(672.825309,715.565309),initialize=672.825309)
m.x19 = Var(within=Reals,bounds=(683.493344,715.573344),initialize=683.493344)
m.x20 = Var(within=Reals,bounds=(685.16975,715.56975),initialize=685.16975)
m.x21 = Var(within=Reals,bounds=(682.27414,715.56414),initialize=682.27414)
m.x22 = Var(within=Reals,bounds=(682.731342,715.571342),initialize=682.731342)
m.x23 = Var(within=Reals,bounds=(683.493344,715.573344),initialize=683.493344)
m.x24 = Var(within=Reals,bounds=(687.303357,715.573357),initialize=687.303357)
m.x25 = Var(within=Reals,bounds=(693.856578,715.566578),initialize=693.856578)
m.x26 = Var(within=Reals,bounds=(675.568518,715.568518),initialize=675.568518)
m.x27 = Var(within=Reals,bounds=(669.9297,715.5697),initialize=669.9297)
m.x28 = Var(within=Reals,bounds=(670.691702,715.571702),initialize=670.691702)
m.x29 = Var(within=Reals,bounds=(669.624899,715.564899),initialize=669.624899)
m.x30 = Var(within=Reals,bounds=(676.17812,715.56812),initialize=676.17812)
m.x31 = Var(within=Reals,bounds=(677.092523,715.572523),initialize=677.092523)
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
m.x67 = Var(within=Reals,bounds=(0.000506711468928022,0.291865806102541),initialize=0.000506711468928022)
m.x68 = Var(within=Reals,bounds=(0.000506711468928022,0.291865806102541),initialize=0.000506711468928022)
m.x69 = Var(within=Reals,bounds=(0.000506711468928022,0.291865806102541),initialize=0.000506711468928022)
m.x70 = Var(within=Reals,bounds=(0.000506711468928022,0.291865806102541),initialize=0.000506711468928022)
m.x71 = Var(within=Reals,bounds=(0.000506711468928022,0.291865806102541),initialize=0.000506711468928022)
m.x72 = Var(within=Reals,bounds=(0.000506711468928022,0.291865806102541),initialize=0.000506711468928022)
m.x73 = Var(within=Reals,bounds=(0.000506711468928022,0.291865806102541),initialize=0.000506711468928022)
m.x74 = Var(within=Reals,bounds=(0.000506711468928022,0.291865806102541),initialize=0.000506711468928022)
m.x75 = Var(within=Reals,bounds=(0.000506711468928022,0.291865806102541),initialize=0.000506711468928022)
m.x76 = Var(within=Reals,bounds=(0.000506711468928022,0.291865806102541),initialize=0.000506711468928022)
m.x77 = Var(within=Reals,bounds=(0.000506711468928022,0.291865806102541),initialize=0.000506711468928022)
m.x78 = Var(within=Reals,bounds=(0.000506711468928022,0.291865806102541),initialize=0.000506711468928022)
m.x79 = Var(within=Reals,bounds=(0.000506711468928022,0.291865806102541),initialize=0.000506711468928022)
m.x80 = Var(within=Reals,bounds=(0.000506711468928022,0.291865806102541),initialize=0.000506711468928022)
m.x81 = Var(within=Reals,bounds=(0.000506711468928022,0.291865806102541),initialize=0.000506711468928022)
m.x82 = Var(within=Reals,bounds=(0.000506711468928022,0.291865806102541),initialize=0.000506711468928022)
m.x83 = Var(within=Reals,bounds=(0.000506711468928022,0.291865806102541),initialize=0.000506711468928022)
m.x84 = Var(within=Reals,bounds=(0.000506711468928022,0.291865806102541),initialize=0.000506711468928022)
m.x85 = Var(within=Reals,bounds=(0.000506711468928022,0.291865806102541),initialize=0.000506711468928022)
m.x86 = Var(within=Reals,bounds=(0.000506711468928022,0.291865806102541),initialize=0.000506711468928022)
m.x87 = Var(within=Reals,bounds=(0.000506711468928022,0.291865806102541),initialize=0.000506711468928022)
m.x88 = Var(within=Reals,bounds=(0.000506711468928022,0.291865806102541),initialize=0.000506711468928022)
m.x89 = Var(within=Reals,bounds=(0.000506711468928022,0.291865806102541),initialize=0.000506711468928022)
m.x90 = Var(within=Reals,bounds=(0.000506711468928022,0.291865806102541),initialize=0.000506711468928022)
m.x91 = Var(within=Reals,bounds=(0.000506711468928022,0.291865806102541),initialize=0.000506711468928022)
m.x92 = Var(within=Reals,bounds=(0.000506711468928022,0.291865806102541),initialize=0.000506711468928022)
m.x93 = Var(within=Reals,bounds=(0.000506711468928022,0.291865806102541),initialize=0.000506711468928022)
m.x94 = Var(within=Reals,bounds=(0.000506711468928022,0.291865806102541),initialize=0.000506711468928022)
m.x95 = Var(within=Reals,bounds=(0.000506711468928022,0.291865806102541),initialize=0.000506711468928022)
m.x96 = Var(within=Reals,bounds=(0.000506711468928022,0.291865806102541),initialize=0.000506711468928022)
m.x97 = Var(within=Reals,bounds=(0.000506711468928022,0.291865806102541),initialize=0.000506711468928022)
m.x98 = Var(within=Reals,bounds=(0.000506711468928022,0.291865806102541),initialize=0.000506711468928022)
m.x99 = Var(within=Reals,bounds=(0.000506711468928022,0.291865806102541),initialize=0.000506711468928022)
m.x100 = Var(within=Reals,bounds=(0.000506711468928022,0.291865806102541),initialize=0.000506711468928022)
m.x101 = Var(within=Reals,bounds=(0.000506711468928022,0.291865806102541),initialize=0.000506711468928022)
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
m.b224 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b225 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b226 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b227 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b228 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b229 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b230 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b231 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b232 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b233 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b234 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b235 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b236 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b237 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b238 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b239 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b240 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b241 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b242 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b243 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b244 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b245 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b246 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b247 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b248 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b249 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b250 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b251 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b252 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b253 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b254 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b255 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b256 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b257 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b258 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b259 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b260 = Var(within=Binary,bounds=(1,1),initialize=1)
m.b261 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b262 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b263 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b264 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b265 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b266 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b267 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b268 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b269 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b270 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b271 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b272 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b273 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b274 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b275 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b276 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b277 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b278 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b279 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b280 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b281 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b282 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b283 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b284 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b285 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b286 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b287 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b288 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b289 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b290 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b291 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b292 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b293 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b294 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b295 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b296 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b297 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b298 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b299 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b300 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b301 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b302 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b303 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b304 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b305 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b306 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b307 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b308 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b309 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b310 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b311 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b312 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b313 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b314 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b315 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b316 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b317 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b318 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b319 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b320 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b321 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b322 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b323 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b324 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b325 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b326 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b327 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b328 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b329 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b330 = Var(within=Binary,bounds=(1,1),initialize=1)
m.b331 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b332 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b333 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b334 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b335 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b336 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b337 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b338 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b339 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b340 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b341 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b342 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b343 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b344 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b345 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b346 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b347 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b348 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b349 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b350 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b351 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b352 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b353 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b354 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b355 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b356 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b357 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b358 = Var(within=Binary,bounds=(1,1),initialize=1)
m.b359 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b360 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b361 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b362 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b363 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b364 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b365 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b366 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b367 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b368 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b369 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b370 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b371 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b372 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b373 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b374 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b375 = Var(within=Binary,bounds=(1,1),initialize=1)
m.b376 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b377 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b378 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b379 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b380 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b381 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b382 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b383 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b384 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b385 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b386 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b387 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b388 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b389 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b390 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b391 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b392 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b393 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b394 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b395 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b396 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b397 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b398 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b399 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b400 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b401 = Var(within=Binary,bounds=(1,1),initialize=1)
m.b402 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b403 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b404 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b405 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b406 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b407 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b408 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b409 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b410 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b411 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b412 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b413 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b414 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b415 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b416 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b417 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b418 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b419 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b420 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b421 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b422 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b423 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b424 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b425 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b426 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b427 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b428 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b429 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b430 = Var(within=Binary,bounds=(1,1),initialize=1)
m.b431 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b432 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b433 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b434 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b435 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b436 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b437 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b438 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b439 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b440 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b441 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b442 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b443 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b444 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b445 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b446 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b447 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b448 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b449 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b450 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b451 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b452 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b453 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b454 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b455 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b456 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b457 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b458 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b459 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b460 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b461 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b462 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b463 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b464 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b465 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b466 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b467 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b468 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b469 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b470 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b471 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b472 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b473 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b474 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b475 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b476 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b477 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b478 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b479 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b480 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b481 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b482 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b483 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b484 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b485 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b486 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b487 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b488 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b489 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b490 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b491 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b492 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b493 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b494 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b495 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b496 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b497 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b498 = Var(within=Binary,bounds=(1,1),initialize=1)
m.b499 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b500 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b501 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b502 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b503 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b504 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b505 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b506 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b507 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b508 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b509 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b510 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b511 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b512 = Var(within=Binary,bounds=(1,1),initialize=1)
m.b513 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b514 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b515 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b516 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b517 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b518 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b519 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b520 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b521 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b522 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b523 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b524 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b525 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b526 = Var(within=Binary,bounds=(1,1),initialize=1)
m.b527 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b528 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b529 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b530 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b531 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b532 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b533 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b534 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b535 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b536 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b537 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b538 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b539 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b540 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b541 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b542 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b543 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b544 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b545 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b546 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b547 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b548 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b549 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b550 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b551 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b552 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b553 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b554 = Var(within=Binary,bounds=(1,1),initialize=1)
m.b555 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b556 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b557 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b558 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b559 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b560 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b561 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b562 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b563 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b564 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b565 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b566 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b567 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b568 = Var(within=Binary,bounds=(1,1),initialize=1)
m.b569 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b570 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b571 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b572 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b573 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b574 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b575 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b576 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b577 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b578 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b579 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b580 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b581 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b582 = Var(within=Binary,bounds=(1,1),initialize=1)
m.b583 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b584 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b585 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b586 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b587 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b588 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b589 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b590 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b591 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=   218.089541088904*m.b102 + 872.358163940174*m.b103 + 1962.80586896925*m.b104
                        + 3489.43265617614*m.b105 + 7851.22347421523*m.b106 + 13957.7306222119*m.b107
                        + 21808.9541005816*m.b108 + 31404.8939051698*m.b109 + 42745.5500567488*m.b110
                        + 55830.9225137742*m.b111 + 70661.0112928637*m.b112 + 87235.8163940174*m.b113
                        + 105555.33785878*m.b114 + 125619.575604061*m.b115 + 31.041358012654*m.b116
                        + 124.165431991485*m.b117 + 279.372221995624*m.b118 + 496.66172802507*m.b119
                        + 1117.48888774597*m.b120 + 1986.64691174549*m.b121 + 3104.13580008278*m.b122
                        + 4469.9555521665*m.b123 + 6084.10617095324*m.b124 + 7946.58765052986*m.b125
                        + 10057.3999932616*m.b126 + 12416.5431991485*m.b127 + 15024.0172741036*m.b128
                        + 17879.8222063008*m.b129 + 293.132824119496*m.b130 + 1172.53129591959*m.b131
                        + 2638.19541595867*m.b132 + 4690.12518423675*m.b133 + 10552.7816616011*m.b134
                        + 18760.5007335966*m.b135 + 29313.2824007817*m.b136 + 42211.1266575723*m.b137
                        + 57454.0335318884*m.b138 + 75042.0029678902*m.b139 + 94975.0349879137*m.b140
                        + 117253.129591959*m.b141 + 141876.286835865*m.b142 + 168844.506607954*m.b143
                        + 24.1610570098493*m.b144 + 96.6442279933722*m.b145 + 217.449512996594*m.b146
                        + 386.576912019514*m.b147 + 869.798051802275*m.b148 + 1546.3076478019*m.b149
                        + 2416.10570006443*m.b150 + 3479.1922081296*m.b151 + 4735.56717429866*m.b152
                        + 6185.23059396912*m.b153 + 7828.18246898197*m.b154 + 9664.42279933722*m.b155
                        + 11693.9515896374*m.b156 + 13916.7688306774*m.b157 + 142.086216057922*m.b158
                        + 568.344863961023*m.b159 + 1278.77594397997*m.b160 + 2273.37945611476*m.b161
                        + 5115.10377483722*m.b162 + 9093.51782283504*m.b163 + 14208.6216003789*m.b164
                        + 20460.4151047621*m.b165 + 27848.8983495179*m.b166 + 36374.07130758*m.b167
                        + 46035.9339897748*m.b168 + 56834.4863961023*m.b169 + 68769.7285536289*m.b170
                        + 81841.660408222*m.b171 + 24.8010850101102*m.b172 + 99.2043399931966*m.b173
                        + 223.209764996503*m.b174 + 396.81736002003*m.b175 + 892.839059797037*m.b176
                        + 1587.26943979666*m.b177 + 2480.10850006614*m.b178 + 3571.35624013303*m.b179
                        + 4861.01266235955*m.b180 + 6349.07776202128*m.b181 + 8035.55154100798*m.b182
                        + 9920.43399931966*m.b183 + 12003.7251416807*m.b184 + 14285.4249586424*m.b185
                        + 49.4421630201551*m.b186 + 197.768651986437*m.b187 + 444.979466993029*m.b188
                        + 791.074608039932*m.b189 + 1779.91786759538*m.b190 + 3164.29843159463*m.b191
                        + 4944.21630013184*m.b192 + 7119.6714722652*m.b193 + 9690.66395270388*m.b194
                        + 12657.1937320295*m.b195 + 16019.2608140095*m.b196 + 19776.8651986437*m.b197
                        + 23930.0068953506*m.b198 + 28478.6858852935*m.b199 + 111.844893045594*m.b200
                        + 447.379571969319*m.b201 + 1006.60403698423*m.b202 + 1789.51828809033*m.b203
                        + 4026.4161470847*m.b204 + 7158.07315108299*m.b205 + 11184.4893002982*m.b206
                        + 16105.6645925999*m.b207 + 21921.5990386408*m.b208 + 28632.2926171153*m.b209
                        + 36237.7453365457*m.b210 + 44737.9571969319*m.b211 + 54132.9282195795*m.b212
                        + 64422.6583618775*m.b213 + 184.168057075076*m.b214 + 736.672227949479*m.b215
                        + 1657.51251297403*m.b216 + 2946.68891214874*m.b217 + 6630.05005049283*m.b218
                        + 11786.75564649*m.b219 + 18416.8057004911*m.b220 + 26520.2002089879*m.b221
                        + 36096.9391895216*m.b222 + 47147.0226070096*m.b223 + 59670.4504754851*m.b224
                        + 73667.2227949479*m.b225 + 89137.3396004807*m.b226 + 106080.800821918*m.b227
                        + 175.687686071619*m.b228 + 702.750743951805*m.b229 + 1581.18917397523*m.b230
                        + 2811.00297614189*m.b231 + 6324.75669456223*m.b232 + 11244.0119025595*m.b233
                        + 17568.7686004685*m.b234 + 25299.0267849424*m.b235 + 34434.7864727147*m.b236
                        + 44976.0476303185*m.b237 + 56922.8102711404*m.b238 + 70275.0743951805*m.b239
                        + 85032.840035906*m.b240 + 101196.107126383*m.b241 + 92.4840460377012*m.b242
                        + 369.93618397463*m.b243 + 832.356413986961*m.b244 + 1479.74473607469*m.b245
                        + 3329.42565524314*m.b246 + 5918.97894324173*m.b247 + 9248.40460024662*m.b248
                        + 13317.7026244961*m.b249 + 18126.8730247988*m.b250 + 23675.9157835374*m.b251
                        + 29964.8309077588*m.b252 + 36993.618397463*m.b253 + 44762.2782702675*m.b254
                        + 53270.8104909373*m.b255 + 97.7642770398537*m.b256 + 391.057107973181*m.b257
                        + 879.878492986216*m.b258 + 1564.22843207896*m.b259 + 3519.51397119993*m.b260
                        + 6256.91372719843*m.b261 + 9776.4277002607*m.b262 + 14078.0558885244*m.b263
                        + 19161.7983013012*m.b264 + 25027.6549199677*m.b265 + 31675.6257519734*m.b266
                        + 39105.7107973181*m.b267 + 47317.9100746253*m.b268 + 56312.2235466482*m.b269
                        + 15.2006650061966*m.b270 + 60.8026599958302*m.b271 + 136.805984997857*m.b272
                        + 243.210640012277*m.b273 + 547.223939875603*m.b274 + 972.84255987537*m.b275
                        + 1520.06650004053*m.b276 + 2188.89576008154*m.b277 + 2979.33034144618*m.b278
                        + 3891.37024123885*m.b279 + 4925.01546061779*m.b280 + 6080.26599958302*m.b281
                        + 7357.12186103012*m.b282 + 8755.5830391679*m.b283 + 67.0429330273301*m.b284
                        + 268.171731981609*m.b285 + 603.386396990548*m.b286 + 1072.68692805415*m.b287
                        + 2413.54558745134*m.b288 + 4290.74771145032*m.b289 + 6704.29330017878*m.b290
                        + 9654.18235235961*m.b291 + 13140.4148743784*m.b292 + 17162.990853464*m.b293
                        + 21721.9102947248*m.b294 + 26817.1731981609*m.b295 + 32448.7795765434*m.b296
                        + 38616.72940433*m.b297 + 33.2814560135672*m.b298 + 133.12582399087*m.b299
                        + 299.533103995308*m.b300 + 532.50329602688*m.b301 + 1198.13241572764*m.b302
                        + 2130.01318372713*m.b303 + 3328.14560008875*m.b304 + 4792.52966417852*m.b305
                        + 6523.16537916636*m.b306 + 8520.05273871243*m.b307 + 10783.1917453526*m.b308
                        + 13312.582399087*m.b309 + 16108.2247062554*m.b310 + 19170.1186541781*m.b311
                        + 17.600770007175*m.b312 + 70.4030799951718*m.b313 + 158.406929997519*m.b314
                        + 281.612320014215*m.b315 + 633.627719855962*m.b316 + 1126.44927985569*m.b317
                        + 1760.07700004693*m.b318 + 2534.51088009441*m.b319 + 3449.75092167452*m.b320
                        + 4505.79712143446*m.b321 + 5702.64948071534*m.b322 + 7040.30799951718*m.b323
                        + 8518.77268119277*m.b324 + 10138.0435190365*m.b325 + 72.1631570294174*m.b326
                        + 288.652627980204*m.b327 + 649.468412989826*m.b328 + 1154.61051205828*m.b329
                        + 2597.87365140944*m.b330 + 4618.44204740834*m.b331 + 7216.31570019243*m.b332
                        + 10391.4946083871*m.b333 + 14143.9787788655*m.b334 + 18473.7681978813*m.b335
                        + 23380.8628709329*m.b336 + 28865.2627980204*m.b337 + 34926.9679928904*m.b338
                        + 41565.9784280497*m.b339 + 9.44041300384839*m.b340 + 37.7616519974103*m.b341
                        + 84.963716998669*m.b342 + 151.046608007625*m.b343 + 339.854867922743*m.b344
                        + 604.186431922598*m.b345 + 944.041300025174*m.b346 + 1359.41947205064*m.b347
                        + 1850.32094889815*m.b348 + 2416.74572876939*m.b349 + 3058.69381238368*m.b350
                        + 3776.16519974103*m.b351 + 4569.15989263976*m.b352 + 5437.67788748322*m.b353
                        + 66.5629120271344*m.b354 + 266.251647981741*m.b355 + 599.066207990616*m.b356
                        + 1065.00659205376*m.b357 + 2396.26483145527*m.b358 + 4260.02636745425*m.b359
                        + 6656.2912001775*m.b360 + 9585.05932835704*m.b361 + 13046.3307583327*m.b362
                        + 17040.1054774249*m.b363 + 21566.3834907053*m.b364 + 26625.1647981741*m.b365
                        + 32216.4494125109*m.b366 + 38340.2373083563*m.b367 + 48.4821210197638*m.b368
                        + 193.9284839867*m.b369 + 436.339088993165*m.b370 + 775.713936039156*m.b371
                        + 1745.35635560324*m.b372 + 3102.8557436025*m.b373 + 4848.21210012928*m.b374
                        + 6981.42542426005*m.b375 + 9502.49572061254*m.b376 + 12411.4229799513*m.b377
                        + 15708.2072059704*m.b378 + 19392.84839867*m.b379 + 23465.3465672855*m.b380
                        + 27925.701693346*m.b381 + 131.685761053682*m.b382 + 526.743043963876*m.b383
                        + 1185.17184898143*m.b384 + 2106.97217610636*m.b385 + 4740.68739492233*m.b386
                        + 8427.88870292031*m.b387 + 13168.5761003512*m.b388 + 18962.7495847064*m.b389
                        + 25810.4091685284*m.b390 + 33711.5548267323*m.b391 + 42666.1865693521*m.b392
                        + 52674.3043963876*m.b393 + 63735.9083329241*m.b394 + 75850.9983287913*m.b395
                        + 122.565362049964*m.b396 + 490.261447966378*m.b397 + 1103.08825798272*m.b398
                        + 1961.04579209899*m.b399 + 4412.35303099697*m.b400 + 7844.18316699509*m.b401
                        + 12256.5362003268*m.b402 + 17649.4121286574*m.b403 + 24022.8109636607*m.b404
                        + 31376.732681989*m.b405 + 39711.1772929814*m.b406 + 49026.1447966378*m.b407
                        + 59321.635216306*m.b408 + 70597.6485052906*m.b409 + 61.1226740249167*m.b410
                        + 244.490695983233*m.b411 + 550.104065991383*m.b412 + 977.962784049365*m.b413
                        + 2200.41626349979*m.b414 + 3911.85113549886*m.b415 + 6112.26740016299*m.b416
                        + 8801.66505632786*m.b417 + 11980.0441098151*m.b418 + 15647.4045489815*m.b419
                        + 19803.7463784842*m.b420 + 24449.0695983233*m.b421 + 29583.3742201422*m.b422
                        + 35206.6602206541*m.b423 + 121.285306049442*m.b424 + 485.141223966729*m.b425
                        + 1091.5677539829*m.b426 + 1940.56489609796*m.b427 + 4366.27101500744*m.b428
                        + 7762.25958300559*m.b429 + 12128.5306003234*m.b430 + 17465.0840646506*m.b431
                        + 23771.919987539*m.b432 + 31049.0383458847*m.b433 + 39296.4391489293*m.b434
                        + 48514.1223966729*m.b435 + 58702.0881122193*m.b436 + 69860.3362493607*m.b437
                        + 161.447063065814*m.b438 + 645.788251955712*m.b439 + 1453.02356697724*m.b440
                        + 2583.15300813039*m.b441 + 5812.09426667878*m.b442 + 10332.6120306763*m.b443
                        + 16144.7063004305*m.b444 + 23248.377072866*m.b445 + 31643.6243633599*m.b446
                        + 41330.4481411579*m.b447 + 52308.8484185616*m.b448 + 64578.8251955712*m.b449
                        + 78140.378502941*m.b450 + 92993.5082791622*m.b451 + 65.2828560266126*m.b452
                        + 261.131423982092*m.b453 + 587.545703990796*m.b454 + 1044.52569605273*m.b455
                        + 2350.18281546575*m.b456 + 4178.10278346475*m.b457 + 6528.28560017408*m.b458
                        + 9400.73126435017*m.b459 + 12795.4397822109*m.b460 + 16712.4111413205*m.b461
                        + 21151.6453466533*m.b462 + 26113.1423982092*m.b463 + 31596.9023084241*m.b464
                        + 37602.9250524263*m.b465 + 188.968267077033*m.b466 + 755.873067948162*m.b467
                        + 1700.71440297336*m.b468 + 3023.49227215262*m.b469 + 6802.85761045355*m.b470
                        + 12093.9690864507*m.b471 + 18896.8267005039*m.b472 + 27211.4304490136*m.b473
                        + 37037.7803499782*m.b474 + 48375.8763674008*m.b475 + 61225.7185156802*m.b476
                        + 75587.3067948162*m.b477 + 91460.6412408061*m.b478 + 108845.721781656*m.b479
                        + 18.0807910073706*m.b480 + 72.3231639950401*m.b481 + 162.727118997451*m.b482
                        + 289.292656014603*m.b483 + 650.908475852033*m.b484 + 1157.17062385176*m.b485
                        + 1808.07910004821*m.b486 + 2603.63390409698*m.b487 + 3543.83503772019*m.b488
                        + 4628.68249747358*m.b489 + 5858.17628473485*m.b490 + 7232.31639950401*m.b491
                        + 8751.1028452253*m.b492 + 10414.5356150102*m.b493 + 112.164907045724*m.b494
                        + 448.659627969231*m.b495 + 1009.48416298419*m.b496 + 1794.63851209059*m.b497
                        + 4037.93665108208*m.b498 + 7178.55404708036*m.b499 + 11216.4907002991*m.b500
                        + 16151.7466086016*m.b501 + 21984.3217826713*m.b502 + 28714.2162011414*m.b503
                        + 36341.4298725587*m.b504 + 44865.9627969231*m.b505 + 54287.8149956012*m.b506
                        + 64606.9864258599*m.b507 + 56.1624570228947*m.b508 + 224.649827984594*m.b509
                        + 505.462112992082*m.b510 + 898.599312045359*m.b511 + 2021.84845154039*m.b512
                        + 3594.39724753953*m.b513 + 5616.24570014977*m.b514 + 8087.39380830125*m.b515
                        + 11007.8415773432*m.b516 + 14377.5889965772*m.b517 + 18196.6360702826*m.b518
                        + 22464.9827984594*m.b519 + 27182.629191806*m.b520 + 32349.5752289256*m.b521
                        + 154.726769063074*m.b522 + 618.907075957555*m.b523 + 1392.54092097819*m.b524
                        + 2475.62830412496*m.b525 + 5570.16368273377*m.b526 + 9902.5132147314*m.b527
                        + 15472.6769004126*m.b528 + 22280.6547368299*m.b529 + 30326.4467387205*m.b530
                        + 39610.0528766102*m.b531 + 50131.4731622885*m.b532 + 61890.7075957555*m.b533
                        + 74887.7562064856*m.b534 + 89122.61893553*m.b535 + 43.3618970176765*m.b536
                        + 173.447587988105*m.b537 + 390.257072993887*m.b538 + 693.790352035021*m.b539
                        + 1561.02829164514*m.b540 + 2775.16140764448*m.b541 + 4336.18970011563*m.b542
                        + 6244.11316823259*m.b543 + 8498.93181612541*m.b544 + 11100.645635534*m.b545
                        + 14049.2546297623*m.b546 + 17344.7587988105*m.b547 + 20987.1581509386*m.b548
                        + 24976.4526696263*m.b549 + 50.722219020677*m.b550 + 202.888875986086*m.b551
                        + 456.499970992849*m.b552 + 811.555504040966*m.b553 + 1825.99988358491*m.b554
                        + 3246.22201558413*m.b555 + 5072.22190013526*m.b556 + 7303.99953627207*m.b557
                        + 9941.55492882566*m.b558 + 12984.8880681338*m.b559 + 16433.9989580615*m.b560
                        + 20288.8875986086*m.b561 + 24549.5539994374*m.b562 + 29215.9981412234*m.b563
                        + 67.8429680276562*m.b564 + 271.371871981389*m.b565 + 610.586711990435*m.b566
                        + 1085.48748805479*m.b567 + 2442.3468474448*m.b568 + 4341.94995144376*m.b569
                        + 6784.29680018091*m.b570 + 9769.3873923639*m.b571 + 13297.2217344545*m.b572
                        + 17367.7998135292*m.b573 + 21981.1216347573*m.b574 + 27137.1871981389*m.b575
                        + 32835.9965165976*m.b576 + 39077.5495642862*m.b577 + 116.805110047616*m.b578
                        + 467.220439967958*m.b579 + 1051.24598998353*m.b580 + 1868.88176009434*m.b581
                        + 4204.98395904411*m.b582 + 7475.52703904232*m.b583 + 11680.5110003115*m.b584
                        + 16819.9358406265*m.b585 + 22893.8015711127*m.b586 + 29902.1081695196*m.b587
                        + 37844.8556447473*m.b588 + 46722.0439967958*m.b589 + 56533.6732479157*m.b590
                        + 67279.7433536059*m.b591, sense=minimize)

m.c2 = Constraint(expr= - m.x32 + m.x34 + m.x35 == -0.00328762)

m.c3 = Constraint(expr= - m.x34 + m.x36 + m.x37 + m.x38 == -0.00319109)

m.c4 = Constraint(expr= - m.x36 + m.x39 + m.x40 == -0.00162583)

m.c5 = Constraint(expr= - m.x33 + m.x41 == -0.00087317)

m.c6 = Constraint(expr= - m.x41 + m.x42 + m.x43 == -0.00338478)

m.c7 = Constraint(expr= - m.x42 + m.x44 == -0.00326365)

m.c8 = Constraint(expr= - m.x44 + m.x45 + m.x46 == -0.01265459)

m.c9 = Constraint(expr= - m.x35 - m.x45 + m.x47 == -0.00071607)

m.c10 = Constraint(expr=   m.x48 + m.x49 + m.x50 - m.x63 == -0.00067948)

m.c11 = Constraint(expr= - m.x48 == -0.00328762)

m.c12 = Constraint(expr= - m.x37 + m.x51 - m.x52 == -0.00635758)

m.c13 = Constraint(expr= - m.x49 + m.x52 == -0.00171037)

m.c14 = Constraint(expr= - m.x38 + m.x53 - m.x60 == -0.00635758)

m.c15 = Constraint(expr= - m.x53 + m.x54 == -0.00162583)

m.c16 = Constraint(expr= - m.x51 + m.x55 + m.x56 == -0.00325166)

m.c17 = Constraint(expr= - m.x55 == -0.00328762)

m.c18 = Constraint(expr= - m.x39 - m.x56 == -0.00065487)

m.c19 = Constraint(expr= - m.x40 + m.x57 + m.x58 == -0.00653928)

m.c20 = Constraint(expr= - m.x57 - m.x62 == -0.00328762)

m.c21 = Constraint(expr= - m.x59 == -0.00069147)

m.c22 = Constraint(expr= - m.x43 + m.x59 == -0.00323967)

m.c23 = Constraint(expr=   m.x60 - m.x61 == -0.00074005)

m.c24 = Constraint(expr= - m.x54 + m.x61 == -0.00325166)

m.c25 = Constraint(expr= - m.x58 + m.x62 == -0.00646673)

m.c26 = Constraint(expr= - m.x50 == -0.00323166)

m.c27 = Constraint(expr=   m.x63 + m.x64 + m.x65 - m.x66 == -0.00331223)

m.c28 = Constraint(expr= - m.x64 == -0.00321507)

m.c29 = Constraint(expr= - m.x65 == -0.00161384)

m.c30 = Constraint(expr= - m.x46 + m.x66 == -0.00264473)

m.c31 = Constraint(expr= - m.x47 == -0.00323967)

m.c32 = Constraint(expr=SignPower(m.x32,1.852) - 1.59495210696227*(1.27323954473516*m.x67)**2.435*(m.x1 - m.x2) == 0)

m.c33 = Constraint(expr=SignPower(m.x33,1.852) - 11.205771761802*(1.27323954473516*m.x68)**2.435*(m.x1 - m.x5) == 0)

m.c34 = Constraint(expr=SignPower(m.x34,1.852) - 1.18663740272357*(1.27323954473516*m.x69)**2.435*(m.x2 - m.x3) == 0)

m.c35 = Constraint(expr=SignPower(m.x35,1.852) - 14.3968193495999*(1.27323954473516*m.x70)**2.435*(m.x2 - m.x9) == 0)

m.c36 = Constraint(expr=SignPower(m.x36,1.852) - 2.44810779480808*(1.27323954473516*m.x71)**2.435*(m.x3 - m.x4) == 0)

m.c37 = Constraint(expr=SignPower(m.x37,1.852) - 14.0252885276747*(1.27323954473516*m.x72)**2.435*(m.x3 - m.x12) == 0)

m.c38 = Constraint(expr=SignPower(m.x38,1.852) - 7.0353389054679*(1.27323954473516*m.x73)**2.435*(m.x3 - m.x14) == 0)

m.c39 = Constraint(expr=SignPower(m.x39,1.852) - 3.11004252044289*(1.27323954473516*m.x74)**2.435*(m.x4 - m.x18) == 0)

m.c40 = Constraint(expr=SignPower(m.x40,1.852) - 1.888722607984*(1.27323954473516*m.x75)**2.435*(m.x4 - m.x19) == 0)

m.c41 = Constraint(expr=SignPower(m.x41,1.852) - 1.97989045700326*(1.27323954473516*m.x76)**2.435*(m.x5 - m.x6) == 0)

m.c42 = Constraint(expr=SignPower(m.x42,1.852) - 3.76110678510308*(1.27323954473516*m.x77)**2.435*(m.x6 - m.x7) == 0)

m.c43 = Constraint(expr=SignPower(m.x43,1.852) - 3.557970084762*(1.27323954473516*m.x78)**2.435*(m.x6 - m.x22) == 0)

m.c44 = Constraint(expr=SignPower(m.x44,1.852) - 22.8833654925219*(1.27323954473516*m.x79)**2.435*(m.x7 - m.x8) == 0)

m.c45 = Constraint(expr=SignPower(m.x45,1.852) - 5.18835255797036*(1.27323954473516*m.x80)**2.435*(m.x8 - m.x9) == 0)

m.c46 = Constraint(expr=SignPower(m.x46,1.852) - 10.4515371239884*(1.27323954473516*m.x81)**2.435*(m.x8 - m.x30) == 0)

m.c47 = Constraint(expr=SignPower(m.x47,1.852) - 19.7629065617235*(1.27323954473516*m.x82)**2.435*(m.x9 - m.x31) == 0)

m.c48 = Constraint(expr=SignPower(m.x48,1.852) - 4.82022111261548*(1.27323954473516*m.x83)**2.435*(m.x10 - m.x11) == 0)

m.c49 = Constraint(expr=SignPower(m.x49,1.852) - 36.8460969794844*(1.27323954473516*m.x84)**2.435*(m.x10 - m.x13) == 0)

m.c50 = Constraint(expr=SignPower(m.x50,1.852) - 5.22576856199418*(1.27323954473516*m.x85)**2.435*(m.x10 - m.x26) == 0)

m.c51 = Constraint(expr=SignPower(m.x51,1.852) - 7.17465254716033*(1.27323954473516*m.x86)**2.435*(m.x12 - m.x16) == 0)

m.c52 = Constraint(expr=SignPower(m.x52,1.852) - 2.64145774215016*(1.27323954473516*m.x87)**2.435*(m.x13 - m.x12) == 0)

m.c53 = Constraint(expr=SignPower(m.x53,1.852) - 2.83801530259736*(1.27323954473516*m.x88)**2.435*(m.x14 - m.x15) == 0)

m.c54 = Constraint(expr=SignPower(m.x54,1.852) - 5.69088932405649*(1.27323954473516*m.x89)**2.435*(m.x15 - m.x24) == 0)

m.c55 = Constraint(expr=SignPower(m.x55,1.852) - 2.86796797069865*(1.27323954473516*m.x90)**2.435*(m.x16 - m.x17) == 0)

m.c56 = Constraint(expr=SignPower(m.x56,1.852) - 2.15452896113933*(1.27323954473516*m.x91)**2.435*(m.x16 - m.x18) == 0)

m.c57 = Constraint(expr=SignPower(m.x57,1.852) - 5.32823461222936*(1.27323954473516*m.x92)**2.435*(m.x19 - m.x20) == 0)

m.c58 = Constraint(expr=SignPower(m.x58,1.852) - 1.8407448956728*(1.27323954473516*m.x93)**2.435*(m.x19 - m.x25) == 0)

m.c59 = Constraint(expr=SignPower(m.x59,1.852) - 19.2382276264565*(1.27323954473516*m.x94)**2.435*(m.x22 - m.x21) == 0)

m.c60 = Constraint(expr=SignPower(m.x60,1.852) - 3.10116936061281*(1.27323954473516*m.x95)**2.435*(m.x23 - m.x14) == 0)

m.c61 = Constraint(expr=SignPower(m.x61,1.852) - 6.19350348088199*(1.27323954473516*m.x96)**2.435*(m.x24 - m.x23) == 0)

m.c62 = Constraint(expr=SignPower(m.x62,1.852) - 2.24810726141632*(1.27323954473516*m.x97)**2.435*(m.x25 - m.x20) == 0)

m.c63 = Constraint(expr=SignPower(m.x63,1.852) - 8.02184399184347*(1.27323954473516*m.x98)**2.435*(m.x27 - m.x10) == 0)

m.c64 = Constraint(expr=SignPower(m.x64,1.852) - 6.85779092047186*(1.27323954473516*m.x99)**2.435*(m.x27 - m.x28) == 0)

m.c65 = Constraint(expr=SignPower(m.x65,1.852) - 5.1271691551641*(1.27323954473516*m.x100)**2.435*(m.x27 - m.x29) == 0)

m.c66 = Constraint(expr=SignPower(m.x66,1.852) - 2.97797222162956*(1.27323954473516*m.x101)**2.435*(m.x30 - m.x27) == 0)

m.c67 = Constraint(expr=   m.x32 - 2*m.x67 <= 0)

m.c68 = Constraint(expr=   m.x33 - 2*m.x68 <= 0)

m.c69 = Constraint(expr=   m.x34 - 2*m.x69 <= 0)

m.c70 = Constraint(expr=   m.x35 - 2*m.x70 <= 0)

m.c71 = Constraint(expr=   m.x36 - 2*m.x71 <= 0)

m.c72 = Constraint(expr=   m.x37 - 2*m.x72 <= 0)

m.c73 = Constraint(expr=   m.x38 - 2*m.x73 <= 0)

m.c74 = Constraint(expr=   m.x39 - 2*m.x74 <= 0)

m.c75 = Constraint(expr=   m.x40 - 2*m.x75 <= 0)

m.c76 = Constraint(expr=   m.x41 - 2*m.x76 <= 0)

m.c77 = Constraint(expr=   m.x42 - 2*m.x77 <= 0)

m.c78 = Constraint(expr=   m.x43 - 2*m.x78 <= 0)

m.c79 = Constraint(expr=   m.x44 - 2*m.x79 <= 0)

m.c80 = Constraint(expr=   m.x45 - 2*m.x80 <= 0)

m.c81 = Constraint(expr=   m.x46 - 2*m.x81 <= 0)

m.c82 = Constraint(expr=   m.x47 - 2*m.x82 <= 0)

m.c83 = Constraint(expr=   m.x48 - 2*m.x83 <= 0)

m.c84 = Constraint(expr=   m.x49 - 2*m.x84 <= 0)

m.c85 = Constraint(expr=   m.x50 - 2*m.x85 <= 0)

m.c86 = Constraint(expr=   m.x51 - 2*m.x86 <= 0)

m.c87 = Constraint(expr=   m.x52 - 2*m.x87 <= 0)

m.c88 = Constraint(expr=   m.x53 - 2*m.x88 <= 0)

m.c89 = Constraint(expr=   m.x54 - 2*m.x89 <= 0)

m.c90 = Constraint(expr=   m.x55 - 2*m.x90 <= 0)

m.c91 = Constraint(expr=   m.x56 - 2*m.x91 <= 0)

m.c92 = Constraint(expr=   m.x57 - 2*m.x92 <= 0)

m.c93 = Constraint(expr=   m.x58 - 2*m.x93 <= 0)

m.c94 = Constraint(expr=   m.x59 - 2*m.x94 <= 0)

m.c95 = Constraint(expr=   m.x60 - 2*m.x95 <= 0)

m.c96 = Constraint(expr=   m.x61 - 2*m.x96 <= 0)

m.c97 = Constraint(expr=   m.x62 - 2*m.x97 <= 0)

m.c98 = Constraint(expr=   m.x63 - 2*m.x98 <= 0)

m.c99 = Constraint(expr=   m.x64 - 2*m.x99 <= 0)

m.c100 = Constraint(expr=   m.x65 - 2*m.x100 <= 0)

m.c101 = Constraint(expr=   m.x66 - 2*m.x101 <= 0)

m.c102 = Constraint(expr=   m.x32 + 2*m.x67 >= 0)

m.c103 = Constraint(expr=   m.x33 + 2*m.x68 >= 0)

m.c104 = Constraint(expr=   m.x34 + 2*m.x69 >= 0)

m.c105 = Constraint(expr=   m.x35 + 2*m.x70 >= 0)

m.c106 = Constraint(expr=   m.x36 + 2*m.x71 >= 0)

m.c107 = Constraint(expr=   m.x37 + 2*m.x72 >= 0)

m.c108 = Constraint(expr=   m.x38 + 2*m.x73 >= 0)

m.c109 = Constraint(expr=   m.x39 + 2*m.x74 >= 0)

m.c110 = Constraint(expr=   m.x40 + 2*m.x75 >= 0)

m.c111 = Constraint(expr=   m.x41 + 2*m.x76 >= 0)

m.c112 = Constraint(expr=   m.x42 + 2*m.x77 >= 0)

m.c113 = Constraint(expr=   m.x43 + 2*m.x78 >= 0)

m.c114 = Constraint(expr=   m.x44 + 2*m.x79 >= 0)

m.c115 = Constraint(expr=   m.x45 + 2*m.x80 >= 0)

m.c116 = Constraint(expr=   m.x46 + 2*m.x81 >= 0)

m.c117 = Constraint(expr=   m.x47 + 2*m.x82 >= 0)

m.c118 = Constraint(expr=   m.x48 + 2*m.x83 >= 0)

m.c119 = Constraint(expr=   m.x49 + 2*m.x84 >= 0)

m.c120 = Constraint(expr=   m.x50 + 2*m.x85 >= 0)

m.c121 = Constraint(expr=   m.x51 + 2*m.x86 >= 0)

m.c122 = Constraint(expr=   m.x52 + 2*m.x87 >= 0)

m.c123 = Constraint(expr=   m.x53 + 2*m.x88 >= 0)

m.c124 = Constraint(expr=   m.x54 + 2*m.x89 >= 0)

m.c125 = Constraint(expr=   m.x55 + 2*m.x90 >= 0)

m.c126 = Constraint(expr=   m.x56 + 2*m.x91 >= 0)

m.c127 = Constraint(expr=   m.x57 + 2*m.x92 >= 0)

m.c128 = Constraint(expr=   m.x58 + 2*m.x93 >= 0)

m.c129 = Constraint(expr=   m.x59 + 2*m.x94 >= 0)

m.c130 = Constraint(expr=   m.x60 + 2*m.x95 >= 0)

m.c131 = Constraint(expr=   m.x61 + 2*m.x96 >= 0)

m.c132 = Constraint(expr=   m.x62 + 2*m.x97 >= 0)

m.c133 = Constraint(expr=   m.x63 + 2*m.x98 >= 0)

m.c134 = Constraint(expr=   m.x64 + 2*m.x99 >= 0)

m.c135 = Constraint(expr=   m.x65 + 2*m.x100 >= 0)

m.c136 = Constraint(expr=   m.x66 + 2*m.x101 >= 0)

m.c137 = Constraint(expr=   m.x67 - 0.000506711468928022*m.b102 - 0.00202684587571209*m.b103 - 0.0045604032203522*m.b104
                          - 0.00810738350284835*m.b105 - 0.0182416128814088*m.b106 - 0.0324295340113934*m.b107
                          - 0.0506711468928022*m.b108 - 0.0729664515256351*m.b109 - 0.0993154479098923*m.b110
                          - 0.129718136045574*m.b111 - 0.164174515932679*m.b112 - 0.202684587571209*m.b113
                          - 0.245248350961163*m.b114 - 0.291865806102541*m.b115 == 0)

m.c138 = Constraint(expr=   m.x68 - 0.000506711468928022*m.b116 - 0.00202684587571209*m.b117 - 0.0045604032203522*m.b118
                          - 0.00810738350284835*m.b119 - 0.0182416128814088*m.b120 - 0.0324295340113934*m.b121
                          - 0.0506711468928022*m.b122 - 0.0729664515256351*m.b123 - 0.0993154479098923*m.b124
                          - 0.129718136045574*m.b125 - 0.164174515932679*m.b126 - 0.202684587571209*m.b127
                          - 0.245248350961163*m.b128 - 0.291865806102541*m.b129 == 0)

m.c139 = Constraint(expr=   m.x69 - 0.000506711468928022*m.b130 - 0.00202684587571209*m.b131 - 0.0045604032203522*m.b132
                          - 0.00810738350284835*m.b133 - 0.0182416128814088*m.b134 - 0.0324295340113934*m.b135
                          - 0.0506711468928022*m.b136 - 0.0729664515256351*m.b137 - 0.0993154479098923*m.b138
                          - 0.129718136045574*m.b139 - 0.164174515932679*m.b140 - 0.202684587571209*m.b141
                          - 0.245248350961163*m.b142 - 0.291865806102541*m.b143 == 0)

m.c140 = Constraint(expr=   m.x70 - 0.000506711468928022*m.b144 - 0.00202684587571209*m.b145 - 0.0045604032203522*m.b146
                          - 0.00810738350284835*m.b147 - 0.0182416128814088*m.b148 - 0.0324295340113934*m.b149
                          - 0.0506711468928022*m.b150 - 0.0729664515256351*m.b151 - 0.0993154479098923*m.b152
                          - 0.129718136045574*m.b153 - 0.164174515932679*m.b154 - 0.202684587571209*m.b155
                          - 0.245248350961163*m.b156 - 0.291865806102541*m.b157 == 0)

m.c141 = Constraint(expr=   m.x71 - 0.000506711468928022*m.b158 - 0.00202684587571209*m.b159 - 0.0045604032203522*m.b160
                          - 0.00810738350284835*m.b161 - 0.0182416128814088*m.b162 - 0.0324295340113934*m.b163
                          - 0.0506711468928022*m.b164 - 0.0729664515256351*m.b165 - 0.0993154479098923*m.b166
                          - 0.129718136045574*m.b167 - 0.164174515932679*m.b168 - 0.202684587571209*m.b169
                          - 0.245248350961163*m.b170 - 0.291865806102541*m.b171 == 0)

m.c142 = Constraint(expr=   m.x72 - 0.000506711468928022*m.b172 - 0.00202684587571209*m.b173 - 0.0045604032203522*m.b174
                          - 0.00810738350284835*m.b175 - 0.0182416128814088*m.b176 - 0.0324295340113934*m.b177
                          - 0.0506711468928022*m.b178 - 0.0729664515256351*m.b179 - 0.0993154479098923*m.b180
                          - 0.129718136045574*m.b181 - 0.164174515932679*m.b182 - 0.202684587571209*m.b183
                          - 0.245248350961163*m.b184 - 0.291865806102541*m.b185 == 0)

m.c143 = Constraint(expr=   m.x73 - 0.000506711468928022*m.b186 - 0.00202684587571209*m.b187 - 0.0045604032203522*m.b188
                          - 0.00810738350284835*m.b189 - 0.0182416128814088*m.b190 - 0.0324295340113934*m.b191
                          - 0.0506711468928022*m.b192 - 0.0729664515256351*m.b193 - 0.0993154479098923*m.b194
                          - 0.129718136045574*m.b195 - 0.164174515932679*m.b196 - 0.202684587571209*m.b197
                          - 0.245248350961163*m.b198 - 0.291865806102541*m.b199 == 0)

m.c144 = Constraint(expr=   m.x74 - 0.000506711468928022*m.b200 - 0.00202684587571209*m.b201 - 0.0045604032203522*m.b202
                          - 0.00810738350284835*m.b203 - 0.0182416128814088*m.b204 - 0.0324295340113934*m.b205
                          - 0.0506711468928022*m.b206 - 0.0729664515256351*m.b207 - 0.0993154479098923*m.b208
                          - 0.129718136045574*m.b209 - 0.164174515932679*m.b210 - 0.202684587571209*m.b211
                          - 0.245248350961163*m.b212 - 0.291865806102541*m.b213 == 0)

m.c145 = Constraint(expr=   m.x75 - 0.000506711468928022*m.b214 - 0.00202684587571209*m.b215 - 0.0045604032203522*m.b216
                          - 0.00810738350284835*m.b217 - 0.0182416128814088*m.b218 - 0.0324295340113934*m.b219
                          - 0.0506711468928022*m.b220 - 0.0729664515256351*m.b221 - 0.0993154479098923*m.b222
                          - 0.129718136045574*m.b223 - 0.164174515932679*m.b224 - 0.202684587571209*m.b225
                          - 0.245248350961163*m.b226 - 0.291865806102541*m.b227 == 0)

m.c146 = Constraint(expr=   m.x76 - 0.000506711468928022*m.b228 - 0.00202684587571209*m.b229 - 0.0045604032203522*m.b230
                          - 0.00810738350284835*m.b231 - 0.0182416128814088*m.b232 - 0.0324295340113934*m.b233
                          - 0.0506711468928022*m.b234 - 0.0729664515256351*m.b235 - 0.0993154479098923*m.b236
                          - 0.129718136045574*m.b237 - 0.164174515932679*m.b238 - 0.202684587571209*m.b239
                          - 0.245248350961163*m.b240 - 0.291865806102541*m.b241 == 0)

m.c147 = Constraint(expr=   m.x77 - 0.000506711468928022*m.b242 - 0.00202684587571209*m.b243 - 0.0045604032203522*m.b244
                          - 0.00810738350284835*m.b245 - 0.0182416128814088*m.b246 - 0.0324295340113934*m.b247
                          - 0.0506711468928022*m.b248 - 0.0729664515256351*m.b249 - 0.0993154479098923*m.b250
                          - 0.129718136045574*m.b251 - 0.164174515932679*m.b252 - 0.202684587571209*m.b253
                          - 0.245248350961163*m.b254 - 0.291865806102541*m.b255 == 0)

m.c148 = Constraint(expr=   m.x78 - 0.000506711468928022*m.b256 - 0.00202684587571209*m.b257 - 0.0045604032203522*m.b258
                          - 0.00810738350284835*m.b259 - 0.0182416128814088*m.b260 - 0.0324295340113934*m.b261
                          - 0.0506711468928022*m.b262 - 0.0729664515256351*m.b263 - 0.0993154479098923*m.b264
                          - 0.129718136045574*m.b265 - 0.164174515932679*m.b266 - 0.202684587571209*m.b267
                          - 0.245248350961163*m.b268 - 0.291865806102541*m.b269 == 0)

m.c149 = Constraint(expr=   m.x79 - 0.000506711468928022*m.b270 - 0.00202684587571209*m.b271 - 0.0045604032203522*m.b272
                          - 0.00810738350284835*m.b273 - 0.0182416128814088*m.b274 - 0.0324295340113934*m.b275
                          - 0.0506711468928022*m.b276 - 0.0729664515256351*m.b277 - 0.0993154479098923*m.b278
                          - 0.129718136045574*m.b279 - 0.164174515932679*m.b280 - 0.202684587571209*m.b281
                          - 0.245248350961163*m.b282 - 0.291865806102541*m.b283 == 0)

m.c150 = Constraint(expr=   m.x80 - 0.000506711468928022*m.b284 - 0.00202684587571209*m.b285 - 0.0045604032203522*m.b286
                          - 0.00810738350284835*m.b287 - 0.0182416128814088*m.b288 - 0.0324295340113934*m.b289
                          - 0.0506711468928022*m.b290 - 0.0729664515256351*m.b291 - 0.0993154479098923*m.b292
                          - 0.129718136045574*m.b293 - 0.164174515932679*m.b294 - 0.202684587571209*m.b295
                          - 0.245248350961163*m.b296 - 0.291865806102541*m.b297 == 0)

m.c151 = Constraint(expr=   m.x81 - 0.000506711468928022*m.b298 - 0.00202684587571209*m.b299 - 0.0045604032203522*m.b300
                          - 0.00810738350284835*m.b301 - 0.0182416128814088*m.b302 - 0.0324295340113934*m.b303
                          - 0.0506711468928022*m.b304 - 0.0729664515256351*m.b305 - 0.0993154479098923*m.b306
                          - 0.129718136045574*m.b307 - 0.164174515932679*m.b308 - 0.202684587571209*m.b309
                          - 0.245248350961163*m.b310 - 0.291865806102541*m.b311 == 0)

m.c152 = Constraint(expr=   m.x82 - 0.000506711468928022*m.b312 - 0.00202684587571209*m.b313 - 0.0045604032203522*m.b314
                          - 0.00810738350284835*m.b315 - 0.0182416128814088*m.b316 - 0.0324295340113934*m.b317
                          - 0.0506711468928022*m.b318 - 0.0729664515256351*m.b319 - 0.0993154479098923*m.b320
                          - 0.129718136045574*m.b321 - 0.164174515932679*m.b322 - 0.202684587571209*m.b323
                          - 0.245248350961163*m.b324 - 0.291865806102541*m.b325 == 0)

m.c153 = Constraint(expr=   m.x83 - 0.000506711468928022*m.b326 - 0.00202684587571209*m.b327 - 0.0045604032203522*m.b328
                          - 0.00810738350284835*m.b329 - 0.0182416128814088*m.b330 - 0.0324295340113934*m.b331
                          - 0.0506711468928022*m.b332 - 0.0729664515256351*m.b333 - 0.0993154479098923*m.b334
                          - 0.129718136045574*m.b335 - 0.164174515932679*m.b336 - 0.202684587571209*m.b337
                          - 0.245248350961163*m.b338 - 0.291865806102541*m.b339 == 0)

m.c154 = Constraint(expr=   m.x84 - 0.000506711468928022*m.b340 - 0.00202684587571209*m.b341 - 0.0045604032203522*m.b342
                          - 0.00810738350284835*m.b343 - 0.0182416128814088*m.b344 - 0.0324295340113934*m.b345
                          - 0.0506711468928022*m.b346 - 0.0729664515256351*m.b347 - 0.0993154479098923*m.b348
                          - 0.129718136045574*m.b349 - 0.164174515932679*m.b350 - 0.202684587571209*m.b351
                          - 0.245248350961163*m.b352 - 0.291865806102541*m.b353 == 0)

m.c155 = Constraint(expr=   m.x85 - 0.000506711468928022*m.b354 - 0.00202684587571209*m.b355 - 0.0045604032203522*m.b356
                          - 0.00810738350284835*m.b357 - 0.0182416128814088*m.b358 - 0.0324295340113934*m.b359
                          - 0.0506711468928022*m.b360 - 0.0729664515256351*m.b361 - 0.0993154479098923*m.b362
                          - 0.129718136045574*m.b363 - 0.164174515932679*m.b364 - 0.202684587571209*m.b365
                          - 0.245248350961163*m.b366 - 0.291865806102541*m.b367 == 0)

m.c156 = Constraint(expr=   m.x86 - 0.000506711468928022*m.b368 - 0.00202684587571209*m.b369 - 0.0045604032203522*m.b370
                          - 0.00810738350284835*m.b371 - 0.0182416128814088*m.b372 - 0.0324295340113934*m.b373
                          - 0.0506711468928022*m.b374 - 0.0729664515256351*m.b375 - 0.0993154479098923*m.b376
                          - 0.129718136045574*m.b377 - 0.164174515932679*m.b378 - 0.202684587571209*m.b379
                          - 0.245248350961163*m.b380 - 0.291865806102541*m.b381 == 0)

m.c157 = Constraint(expr=   m.x87 - 0.000506711468928022*m.b382 - 0.00202684587571209*m.b383 - 0.0045604032203522*m.b384
                          - 0.00810738350284835*m.b385 - 0.0182416128814088*m.b386 - 0.0324295340113934*m.b387
                          - 0.0506711468928022*m.b388 - 0.0729664515256351*m.b389 - 0.0993154479098923*m.b390
                          - 0.129718136045574*m.b391 - 0.164174515932679*m.b392 - 0.202684587571209*m.b393
                          - 0.245248350961163*m.b394 - 0.291865806102541*m.b395 == 0)

m.c158 = Constraint(expr=   m.x88 - 0.000506711468928022*m.b396 - 0.00202684587571209*m.b397 - 0.0045604032203522*m.b398
                          - 0.00810738350284835*m.b399 - 0.0182416128814088*m.b400 - 0.0324295340113934*m.b401
                          - 0.0506711468928022*m.b402 - 0.0729664515256351*m.b403 - 0.0993154479098923*m.b404
                          - 0.129718136045574*m.b405 - 0.164174515932679*m.b406 - 0.202684587571209*m.b407
                          - 0.245248350961163*m.b408 - 0.291865806102541*m.b409 == 0)

m.c159 = Constraint(expr=   m.x89 - 0.000506711468928022*m.b410 - 0.00202684587571209*m.b411 - 0.0045604032203522*m.b412
                          - 0.00810738350284835*m.b413 - 0.0182416128814088*m.b414 - 0.0324295340113934*m.b415
                          - 0.0506711468928022*m.b416 - 0.0729664515256351*m.b417 - 0.0993154479098923*m.b418
                          - 0.129718136045574*m.b419 - 0.164174515932679*m.b420 - 0.202684587571209*m.b421
                          - 0.245248350961163*m.b422 - 0.291865806102541*m.b423 == 0)

m.c160 = Constraint(expr=   m.x90 - 0.000506711468928022*m.b424 - 0.00202684587571209*m.b425 - 0.0045604032203522*m.b426
                          - 0.00810738350284835*m.b427 - 0.0182416128814088*m.b428 - 0.0324295340113934*m.b429
                          - 0.0506711468928022*m.b430 - 0.0729664515256351*m.b431 - 0.0993154479098923*m.b432
                          - 0.129718136045574*m.b433 - 0.164174515932679*m.b434 - 0.202684587571209*m.b435
                          - 0.245248350961163*m.b436 - 0.291865806102541*m.b437 == 0)

m.c161 = Constraint(expr=   m.x91 - 0.000506711468928022*m.b438 - 0.00202684587571209*m.b439 - 0.0045604032203522*m.b440
                          - 0.00810738350284835*m.b441 - 0.0182416128814088*m.b442 - 0.0324295340113934*m.b443
                          - 0.0506711468928022*m.b444 - 0.0729664515256351*m.b445 - 0.0993154479098923*m.b446
                          - 0.129718136045574*m.b447 - 0.164174515932679*m.b448 - 0.202684587571209*m.b449
                          - 0.245248350961163*m.b450 - 0.291865806102541*m.b451 == 0)

m.c162 = Constraint(expr=   m.x92 - 0.000506711468928022*m.b452 - 0.00202684587571209*m.b453 - 0.0045604032203522*m.b454
                          - 0.00810738350284835*m.b455 - 0.0182416128814088*m.b456 - 0.0324295340113934*m.b457
                          - 0.0506711468928022*m.b458 - 0.0729664515256351*m.b459 - 0.0993154479098923*m.b460
                          - 0.129718136045574*m.b461 - 0.164174515932679*m.b462 - 0.202684587571209*m.b463
                          - 0.245248350961163*m.b464 - 0.291865806102541*m.b465 == 0)

m.c163 = Constraint(expr=   m.x93 - 0.000506711468928022*m.b466 - 0.00202684587571209*m.b467 - 0.0045604032203522*m.b468
                          - 0.00810738350284835*m.b469 - 0.0182416128814088*m.b470 - 0.0324295340113934*m.b471
                          - 0.0506711468928022*m.b472 - 0.0729664515256351*m.b473 - 0.0993154479098923*m.b474
                          - 0.129718136045574*m.b475 - 0.164174515932679*m.b476 - 0.202684587571209*m.b477
                          - 0.245248350961163*m.b478 - 0.291865806102541*m.b479 == 0)

m.c164 = Constraint(expr=   m.x94 - 0.000506711468928022*m.b480 - 0.00202684587571209*m.b481 - 0.0045604032203522*m.b482
                          - 0.00810738350284835*m.b483 - 0.0182416128814088*m.b484 - 0.0324295340113934*m.b485
                          - 0.0506711468928022*m.b486 - 0.0729664515256351*m.b487 - 0.0993154479098923*m.b488
                          - 0.129718136045574*m.b489 - 0.164174515932679*m.b490 - 0.202684587571209*m.b491
                          - 0.245248350961163*m.b492 - 0.291865806102541*m.b493 == 0)

m.c165 = Constraint(expr=   m.x95 - 0.000506711468928022*m.b494 - 0.00202684587571209*m.b495 - 0.0045604032203522*m.b496
                          - 0.00810738350284835*m.b497 - 0.0182416128814088*m.b498 - 0.0324295340113934*m.b499
                          - 0.0506711468928022*m.b500 - 0.0729664515256351*m.b501 - 0.0993154479098923*m.b502
                          - 0.129718136045574*m.b503 - 0.164174515932679*m.b504 - 0.202684587571209*m.b505
                          - 0.245248350961163*m.b506 - 0.291865806102541*m.b507 == 0)

m.c166 = Constraint(expr=   m.x96 - 0.000506711468928022*m.b508 - 0.00202684587571209*m.b509 - 0.0045604032203522*m.b510
                          - 0.00810738350284835*m.b511 - 0.0182416128814088*m.b512 - 0.0324295340113934*m.b513
                          - 0.0506711468928022*m.b514 - 0.0729664515256351*m.b515 - 0.0993154479098923*m.b516
                          - 0.129718136045574*m.b517 - 0.164174515932679*m.b518 - 0.202684587571209*m.b519
                          - 0.245248350961163*m.b520 - 0.291865806102541*m.b521 == 0)

m.c167 = Constraint(expr=   m.x97 - 0.000506711468928022*m.b522 - 0.00202684587571209*m.b523 - 0.0045604032203522*m.b524
                          - 0.00810738350284835*m.b525 - 0.0182416128814088*m.b526 - 0.0324295340113934*m.b527
                          - 0.0506711468928022*m.b528 - 0.0729664515256351*m.b529 - 0.0993154479098923*m.b530
                          - 0.129718136045574*m.b531 - 0.164174515932679*m.b532 - 0.202684587571209*m.b533
                          - 0.245248350961163*m.b534 - 0.291865806102541*m.b535 == 0)

m.c168 = Constraint(expr=   m.x98 - 0.000506711468928022*m.b536 - 0.00202684587571209*m.b537 - 0.0045604032203522*m.b538
                          - 0.00810738350284835*m.b539 - 0.0182416128814088*m.b540 - 0.0324295340113934*m.b541
                          - 0.0506711468928022*m.b542 - 0.0729664515256351*m.b543 - 0.0993154479098923*m.b544
                          - 0.129718136045574*m.b545 - 0.164174515932679*m.b546 - 0.202684587571209*m.b547
                          - 0.245248350961163*m.b548 - 0.291865806102541*m.b549 == 0)

m.c169 = Constraint(expr=   m.x99 - 0.000506711468928022*m.b550 - 0.00202684587571209*m.b551 - 0.0045604032203522*m.b552
                          - 0.00810738350284835*m.b553 - 0.0182416128814088*m.b554 - 0.0324295340113934*m.b555
                          - 0.0506711468928022*m.b556 - 0.0729664515256351*m.b557 - 0.0993154479098923*m.b558
                          - 0.129718136045574*m.b559 - 0.164174515932679*m.b560 - 0.202684587571209*m.b561
                          - 0.245248350961163*m.b562 - 0.291865806102541*m.b563 == 0)

m.c170 = Constraint(expr=   m.x100 - 0.000506711468928022*m.b564 - 0.00202684587571209*m.b565
                          - 0.0045604032203522*m.b566 - 0.00810738350284835*m.b567 - 0.0182416128814088*m.b568
                          - 0.0324295340113934*m.b569 - 0.0506711468928022*m.b570 - 0.0729664515256351*m.b571
                          - 0.0993154479098923*m.b572 - 0.129718136045574*m.b573 - 0.164174515932679*m.b574
                          - 0.202684587571209*m.b575 - 0.245248350961163*m.b576 - 0.291865806102541*m.b577 == 0)

m.c171 = Constraint(expr=   m.x101 - 0.000506711468928022*m.b578 - 0.00202684587571209*m.b579
                          - 0.0045604032203522*m.b580 - 0.00810738350284835*m.b581 - 0.0182416128814088*m.b582
                          - 0.0324295340113934*m.b583 - 0.0506711468928022*m.b584 - 0.0729664515256351*m.b585
                          - 0.0993154479098923*m.b586 - 0.129718136045574*m.b587 - 0.164174515932679*m.b588
                          - 0.202684587571209*m.b589 - 0.245248350961163*m.b590 - 0.291865806102541*m.b591 == 0)

m.c172 = Constraint(expr=   m.b102 + m.b103 + m.b104 + m.b105 + m.b106 + m.b107 + m.b108 + m.b109 + m.b110 + m.b111
                          + m.b112 + m.b113 + m.b114 + m.b115 == 1)

m.c173 = Constraint(expr=   m.b116 + m.b117 + m.b118 + m.b119 + m.b120 + m.b121 + m.b122 + m.b123 + m.b124 + m.b125
                          + m.b126 + m.b127 + m.b128 + m.b129 == 1)

m.c174 = Constraint(expr=   m.b130 + m.b131 + m.b132 + m.b133 + m.b134 + m.b135 + m.b136 + m.b137 + m.b138 + m.b139
                          + m.b140 + m.b141 + m.b142 + m.b143 == 1)

m.c175 = Constraint(expr=   m.b144 + m.b145 + m.b146 + m.b147 + m.b148 + m.b149 + m.b150 + m.b151 + m.b152 + m.b153
                          + m.b154 + m.b155 + m.b156 + m.b157 == 1)

m.c176 = Constraint(expr=   m.b158 + m.b159 + m.b160 + m.b161 + m.b162 + m.b163 + m.b164 + m.b165 + m.b166 + m.b167
                          + m.b168 + m.b169 + m.b170 + m.b171 == 1)

m.c177 = Constraint(expr=   m.b172 + m.b173 + m.b174 + m.b175 + m.b176 + m.b177 + m.b178 + m.b179 + m.b180 + m.b181
                          + m.b182 + m.b183 + m.b184 + m.b185 == 1)

m.c178 = Constraint(expr=   m.b186 + m.b187 + m.b188 + m.b189 + m.b190 + m.b191 + m.b192 + m.b193 + m.b194 + m.b195
                          + m.b196 + m.b197 + m.b198 + m.b199 == 1)

m.c179 = Constraint(expr=   m.b200 + m.b201 + m.b202 + m.b203 + m.b204 + m.b205 + m.b206 + m.b207 + m.b208 + m.b209
                          + m.b210 + m.b211 + m.b212 + m.b213 == 1)

m.c180 = Constraint(expr=   m.b214 + m.b215 + m.b216 + m.b217 + m.b218 + m.b219 + m.b220 + m.b221 + m.b222 + m.b223
                          + m.b224 + m.b225 + m.b226 + m.b227 == 1)

m.c181 = Constraint(expr=   m.b228 + m.b229 + m.b230 + m.b231 + m.b232 + m.b233 + m.b234 + m.b235 + m.b236 + m.b237
                          + m.b238 + m.b239 + m.b240 + m.b241 == 1)

m.c182 = Constraint(expr=   m.b242 + m.b243 + m.b244 + m.b245 + m.b246 + m.b247 + m.b248 + m.b249 + m.b250 + m.b251
                          + m.b252 + m.b253 + m.b254 + m.b255 == 1)

m.c183 = Constraint(expr=   m.b256 + m.b257 + m.b258 + m.b259 + m.b260 + m.b261 + m.b262 + m.b263 + m.b264 + m.b265
                          + m.b266 + m.b267 + m.b268 + m.b269 == 1)

m.c184 = Constraint(expr=   m.b270 + m.b271 + m.b272 + m.b273 + m.b274 + m.b275 + m.b276 + m.b277 + m.b278 + m.b279
                          + m.b280 + m.b281 + m.b282 + m.b283 == 1)

m.c185 = Constraint(expr=   m.b284 + m.b285 + m.b286 + m.b287 + m.b288 + m.b289 + m.b290 + m.b291 + m.b292 + m.b293
                          + m.b294 + m.b295 + m.b296 + m.b297 == 1)

m.c186 = Constraint(expr=   m.b298 + m.b299 + m.b300 + m.b301 + m.b302 + m.b303 + m.b304 + m.b305 + m.b306 + m.b307
                          + m.b308 + m.b309 + m.b310 + m.b311 == 1)

m.c187 = Constraint(expr=   m.b312 + m.b313 + m.b314 + m.b315 + m.b316 + m.b317 + m.b318 + m.b319 + m.b320 + m.b321
                          + m.b322 + m.b323 + m.b324 + m.b325 == 1)

m.c188 = Constraint(expr=   m.b326 + m.b327 + m.b328 + m.b329 + m.b330 + m.b331 + m.b332 + m.b333 + m.b334 + m.b335
                          + m.b336 + m.b337 + m.b338 + m.b339 == 1)

m.c189 = Constraint(expr=   m.b340 + m.b341 + m.b342 + m.b343 + m.b344 + m.b345 + m.b346 + m.b347 + m.b348 + m.b349
                          + m.b350 + m.b351 + m.b352 + m.b353 == 1)

m.c190 = Constraint(expr=   m.b354 + m.b355 + m.b356 + m.b357 + m.b358 + m.b359 + m.b360 + m.b361 + m.b362 + m.b363
                          + m.b364 + m.b365 + m.b366 + m.b367 == 1)

m.c191 = Constraint(expr=   m.b368 + m.b369 + m.b370 + m.b371 + m.b372 + m.b373 + m.b374 + m.b375 + m.b376 + m.b377
                          + m.b378 + m.b379 + m.b380 + m.b381 == 1)

m.c192 = Constraint(expr=   m.b382 + m.b383 + m.b384 + m.b385 + m.b386 + m.b387 + m.b388 + m.b389 + m.b390 + m.b391
                          + m.b392 + m.b393 + m.b394 + m.b395 == 1)

m.c193 = Constraint(expr=   m.b396 + m.b397 + m.b398 + m.b399 + m.b400 + m.b401 + m.b402 + m.b403 + m.b404 + m.b405
                          + m.b406 + m.b407 + m.b408 + m.b409 == 1)

m.c194 = Constraint(expr=   m.b410 + m.b411 + m.b412 + m.b413 + m.b414 + m.b415 + m.b416 + m.b417 + m.b418 + m.b419
                          + m.b420 + m.b421 + m.b422 + m.b423 == 1)

m.c195 = Constraint(expr=   m.b424 + m.b425 + m.b426 + m.b427 + m.b428 + m.b429 + m.b430 + m.b431 + m.b432 + m.b433
                          + m.b434 + m.b435 + m.b436 + m.b437 == 1)

m.c196 = Constraint(expr=   m.b438 + m.b439 + m.b440 + m.b441 + m.b442 + m.b443 + m.b444 + m.b445 + m.b446 + m.b447
                          + m.b448 + m.b449 + m.b450 + m.b451 == 1)

m.c197 = Constraint(expr=   m.b452 + m.b453 + m.b454 + m.b455 + m.b456 + m.b457 + m.b458 + m.b459 + m.b460 + m.b461
                          + m.b462 + m.b463 + m.b464 + m.b465 == 1)

m.c198 = Constraint(expr=   m.b466 + m.b467 + m.b468 + m.b469 + m.b470 + m.b471 + m.b472 + m.b473 + m.b474 + m.b475
                          + m.b476 + m.b477 + m.b478 + m.b479 == 1)

m.c199 = Constraint(expr=   m.b480 + m.b481 + m.b482 + m.b483 + m.b484 + m.b485 + m.b486 + m.b487 + m.b488 + m.b489
                          + m.b490 + m.b491 + m.b492 + m.b493 == 1)

m.c200 = Constraint(expr=   m.b494 + m.b495 + m.b496 + m.b497 + m.b498 + m.b499 + m.b500 + m.b501 + m.b502 + m.b503
                          + m.b504 + m.b505 + m.b506 + m.b507 == 1)

m.c201 = Constraint(expr=   m.b508 + m.b509 + m.b510 + m.b511 + m.b512 + m.b513 + m.b514 + m.b515 + m.b516 + m.b517
                          + m.b518 + m.b519 + m.b520 + m.b521 == 1)

m.c202 = Constraint(expr=   m.b522 + m.b523 + m.b524 + m.b525 + m.b526 + m.b527 + m.b528 + m.b529 + m.b530 + m.b531
                          + m.b532 + m.b533 + m.b534 + m.b535 == 1)

m.c203 = Constraint(expr=   m.b536 + m.b537 + m.b538 + m.b539 + m.b540 + m.b541 + m.b542 + m.b543 + m.b544 + m.b545
                          + m.b546 + m.b547 + m.b548 + m.b549 == 1)

m.c204 = Constraint(expr=   m.b550 + m.b551 + m.b552 + m.b553 + m.b554 + m.b555 + m.b556 + m.b557 + m.b558 + m.b559
                          + m.b560 + m.b561 + m.b562 + m.b563 == 1)

m.c205 = Constraint(expr=   m.b564 + m.b565 + m.b566 + m.b567 + m.b568 + m.b569 + m.b570 + m.b571 + m.b572 + m.b573
                          + m.b574 + m.b575 + m.b576 + m.b577 == 1)

m.c206 = Constraint(expr=   m.b578 + m.b579 + m.b580 + m.b581 + m.b582 + m.b583 + m.b584 + m.b585 + m.b586 + m.b587
                          + m.b588 + m.b589 + m.b590 + m.b591 == 1)
