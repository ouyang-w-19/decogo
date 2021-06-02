#  MINLP written by GAMS Convert at 04/21/18 13:51:16
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        285      123       96       66        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        297      209       88        0        0        0        0        0
#  FX     17       16        1        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1281      751      530        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(-1.6094379124341,3.68887945411394),initialize=2.99573227355399)
m.x2 = Var(within=Reals,bounds=(-1.6094379124341,3.68887945411394),initialize=2.99573227355399)
m.x3 = Var(within=Reals,bounds=(-1.6094379124341,3.68887945411394),initialize=2.94443897916644)
m.x4 = Var(within=Reals,bounds=(-1.6094379124341,3.68887945411394),initialize=2.94443897916644)
m.x5 = Var(within=Reals,bounds=(-1.6094379124341,3.68887945411394),initialize=0)
m.x6 = Var(within=Reals,bounds=(-1.6094379124341,3.68887945411394),initialize=1.9677597942808)
m.x7 = Var(within=Reals,bounds=(-1.6094379124341,3.68887945411394),initialize=1.27461261372086)
m.x8 = Var(within=Reals,bounds=(-6.90775527898214,3.68887945411394),initialize=-1.1298234508907)
m.x9 = Var(within=Reals,bounds=(-1.6094379124341,3.68887945411394),initialize=0)
m.x10 = Var(within=Reals,bounds=(-1.6094379124341,3.68887945411394),initialize=2.0433602879393)
m.x11 = Var(within=Reals,bounds=(-6.90775527898214,-0.693147180559945),initialize=-0.693147180559945)
m.x12 = Var(within=Reals,bounds=(0.693147180559945,6.90775527898214),initialize=0.693147180559945)
m.x13 = Var(within=Reals,bounds=(-0.693147180559945,2.99573227355399),initialize=0)
m.x14 = Var(within=Reals,bounds=(0.693147180559945,6.90775527898214),initialize=0.693147180559945)
m.x15 = Var(within=Reals,bounds=(0.693147180559945,6.90775527898214),initialize=0.693147180559945)
m.x16 = Var(within=Reals,bounds=(0.693147180559945,6.90775527898214),initialize=0.693147180559945)
m.x17 = Var(within=Reals,bounds=(0,5.29831736654804),initialize=2.94443897916644)
m.x18 = Var(within=Reals,bounds=(0,5.29831736654804),initialize=2.94443897916644)
m.x19 = Var(within=Reals,bounds=(0,5.29831736654804),initialize=2.94443897916644)
m.x20 = Var(within=Reals,bounds=(0,5.29831736654804),initialize=2.94443897916644)
m.x21 = Var(within=Reals,bounds=(0,5.29831736654804),initialize=2.94443897916644)
m.x22 = Var(within=Reals,bounds=(0,5.29831736654804),initialize=2.94443897916644)
m.x23 = Var(within=Reals,bounds=(0,5.29831736654804),initialize=2.94443897916644)
m.x24 = Var(within=Reals,bounds=(0,5.29831736654804),initialize=2.94443897916644)
m.x25 = Var(within=Reals,bounds=(0,5.29831736654804),initialize=2.94443897916644)
m.x26 = Var(within=Reals,bounds=(0,5.29831736654804),initialize=2.94443897916644)
m.x27 = Var(within=Reals,bounds=(0,5.29831736654804),initialize=2.94443897916644)
m.x28 = Var(within=Reals,bounds=(0,5.29831736654804),initialize=2.94443897916644)
m.x29 = Var(within=Reals,bounds=(0,5.29831736654804),initialize=2.94443897916644)
m.x30 = Var(within=Reals,bounds=(0,5.29831736654804),initialize=2.94443897916644)
m.x31 = Var(within=Reals,bounds=(0,5.29831736654804),initialize=2.94443897916644)
m.x32 = Var(within=Reals,bounds=(0,5.29831736654804),initialize=2.94443897916644)
m.x33 = Var(within=Reals,bounds=(0,5.29831736654804),initialize=2.61614353244073)
m.x34 = Var(within=Reals,bounds=(0,5.29831736654804),initialize=2.61614353244073)
m.x35 = Var(within=Reals,bounds=(0,5.29831736654804),initialize=2.61614353244073)
m.x36 = Var(within=Reals,bounds=(0,5.29831736654804),initialize=2.61614353244073)
m.x37 = Var(within=Reals,bounds=(0,5.29831736654804),initialize=2.61614353244073)
m.x38 = Var(within=Reals,bounds=(0,5.29831736654804),initialize=2.61614353244073)
m.x39 = Var(within=Reals,bounds=(0,5.29831736654804),initialize=2.61614353244073)
m.x40 = Var(within=Reals,bounds=(0,5.29831736654804),initialize=2.61614353244073)
m.x41 = Var(within=Reals,bounds=(0,5.29831736654804),initialize=2.94443897916644)
m.x42 = Var(within=Reals,bounds=(0,5.29831736654804),initialize=2.94443897916644)
m.x43 = Var(within=Reals,bounds=(0,5.29831736654804),initialize=2.94443897916644)
m.x44 = Var(within=Reals,bounds=(0,5.29831736654804),initialize=2.94443897916644)
m.x45 = Var(within=Reals,bounds=(0,5.29831736654804),initialize=2.94443897916644)
m.x46 = Var(within=Reals,bounds=(0,5.29831736654804),initialize=2.94443897916644)
m.x47 = Var(within=Reals,bounds=(0,5.29831736654804),initialize=2.94443897916644)
m.x48 = Var(within=Reals,bounds=(0,5.29831736654804),initialize=2.94443897916644)
m.x49 = Var(within=Reals,bounds=(None,None),initialize=3.17756893714648)
m.x50 = Var(within=Reals,bounds=(None,None),initialize=0.233622804898907)
m.x51 = Var(within=Reals,bounds=(None,None),initialize=0.399415336353673)
m.x52 = Var(within=Reals,bounds=(None,None),initialize=0.577807612471274)
m.x53 = Var(within=Reals,bounds=(None,None),initialize=0.0827635536142284)
m.x54 = Var(within=Reals,bounds=(0.587786664902119,0.587786664902119),initialize=0.587786664902119)
m.x55 = Var(within=Reals,bounds=(None,None),initialize=-1.07858898697236)
m.x56 = Var(within=Reals,bounds=(None,None),initialize=-0.604447984103336)
m.x57 = Var(within=Reals,bounds=(None,None),initialize=3.17756893714648)
m.x58 = Var(within=Reals,bounds=(None,None),initialize=0.591132698406824)
m.x59 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x60 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x61 = Var(within=Reals,bounds=(None,None),initialize=0.516209904652203)
m.x62 = Var(within=Reals,bounds=(0.587786664902119,0.587786664902119),initialize=0.587786664902119)
m.x63 = Var(within=Reals,bounds=(None,None),initialize=-1.1469821150246)
m.x64 = Var(within=Reals,bounds=(None,None),initialize=-0.689448619982603)
m.x65 = Var(within=Reals,bounds=(None,None),initialize=3.17756893714648)
m.x66 = Var(within=Reals,bounds=(None,None),initialize=0.647103242058539)
m.x67 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x68 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x69 = Var(within=Reals,bounds=(None,None),initialize=0.917954032114244)
m.x70 = Var(within=Reals,bounds=(0.587786664902119,0.587786664902119),initialize=0.587786664902119)
m.x71 = Var(within=Reals,bounds=(None,None),initialize=-1.01757906523769)
m.x72 = Var(within=Reals,bounds=(None,None),initialize=-0.603587003016137)
m.x73 = Var(within=Reals,bounds=(None,None),initialize=3.17756893714648)
m.x74 = Var(within=Reals,bounds=(None,None),initialize=0.259570495557779)
m.x75 = Var(within=Reals,bounds=(None,None),initialize=0.538673267899503)
m.x76 = Var(within=Reals,bounds=(None,None),initialize=0.594337876584314)
m.x77 = Var(within=Reals,bounds=(None,None),initialize=0.165264958927998)
m.x78 = Var(within=Reals,bounds=(0.587786664902119,0.587786664902119),initialize=0.587786664902119)
m.x79 = Var(within=Reals,bounds=(None,None),initialize=-0.938029907934514)
m.x80 = Var(within=Reals,bounds=(None,None),initialize=-0.456539109459263)
m.x81 = Var(within=Reals,bounds=(0,1.6094379124341),initialize=1.38629436111989)
m.x82 = Var(within=Reals,bounds=(0,1.6094379124341),initialize=0)
m.x83 = Var(within=Reals,bounds=(0,1.6094379124341),initialize=0)
m.x84 = Var(within=Reals,bounds=(0,1.6094379124341),initialize=0)
m.x85 = Var(within=Reals,bounds=(0,1.6094379124341),initialize=0)
m.x86 = Var(within=Reals,bounds=(0,1.6094379124341),initialize=0)
m.x87 = Var(within=Reals,bounds=(0,1.6094379124341),initialize=0)
m.x88 = Var(within=Reals,bounds=(0,1.6094379124341),initialize=0)
m.x89 = Var(within=Reals,bounds=(0,1.6094379124341),initialize=0)
m.x90 = Var(within=Reals,bounds=(0,1.6094379124341),initialize=0)
m.x91 = Var(within=Reals,bounds=(0,1.6094379124341),initialize=0)
m.x92 = Var(within=Reals,bounds=(0,1.6094379124341),initialize=0)
m.x93 = Var(within=Reals,bounds=(0,1.6094379124341),initialize=0)
m.x94 = Var(within=Reals,bounds=(0,1.6094379124341),initialize=0)
m.x95 = Var(within=Reals,bounds=(0,1.6094379124341),initialize=0)
m.x96 = Var(within=Reals,bounds=(0,1.6094379124341),initialize=1.38629436111989)
m.x98 = Var(within=Reals,bounds=(-2.30258509299405,6.90775527898214),initialize=3.68887945411394)
m.x99 = Var(within=Reals,bounds=(-2.30258509299405,6.90775527898214),initialize=4.38202663467388)
m.x100 = Var(within=Reals,bounds=(-2.30258509299405,6.90775527898214),initialize=2.0433602879393)
m.x101 = Var(within=Reals,bounds=(-2.30258509299405,6.90775527898214),initialize=2.73650746849925)
m.x102 = Var(within=Reals,bounds=(-2.30258509299405,6.90775527898214),initialize=1.9677597942808)
m.x103 = Var(within=Reals,bounds=(-2.30258509299405,6.90775527898214),initialize=1.9677597942808)
m.x104 = Var(within=Reals,bounds=(-2.30258509299405,6.90775527898214),initialize=0.949618090789135)
m.x105 = Var(within=Reals,bounds=(-2.30258509299405,6.90775527898214),initialize=0)
m.x106 = Var(within=Reals,bounds=(-6.90775527898214,2.99573227355399),initialize=-1.15316440313985)
m.x107 = Var(within=Reals,bounds=(-6.90775527898214,2.99573227355399),initialize=-1.15316440313985)
m.x108 = Var(within=Reals,bounds=(-6.90775527898214,2.99573227355399),initialize=-0.824868956414142)
m.x109 = Var(within=Reals,bounds=(-6.90775527898214,2.99573227355399),initialize=-1.15316440313985)
m.b110 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b111 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b112 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b113 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b114 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b115 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b116 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b117 = Var(within=Binary,bounds=(0,0),initialize=0)
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
m.x198 = Var(within=Reals,bounds=(None,1.6094379124341),initialize=-0.862636840383206)
m.x199 = Var(within=Reals,bounds=(None,1.6094379124341),initialize=-0.862636840383206)
m.x200 = Var(within=Reals,bounds=(None,1.6094379124341),initialize=-2.2489312015031)
m.x201 = Var(within=Reals,bounds=(None,1.6094379124341),initialize=-2.2489312015031)
m.x202 = Var(within=Reals,bounds=(None,1.6094379124341),initialize=-1.55578402094315)
m.x203 = Var(within=Reals,bounds=(None,1.6094379124341),initialize=-1.63138451460165)
m.x204 = Var(within=Reals,bounds=(None,1.6094379124341),initialize=-2.32453169516159)
m.x205 = Var(within=Reals,bounds=(None,1.6094379124341),initialize=-3.09889665499776)
m.x206 = Var(within=Reals,bounds=(None,1.6094379124341),initialize=-0.752600105692548)
m.x207 = Var(within=Reals,bounds=(None,1.6094379124341),initialize=-0.752600105692548)
m.x208 = Var(within=Reals,bounds=(None,1.6094379124341),initialize=0)
m.x209 = Var(within=Reals,bounds=(None,1.6094379124341),initialize=0)
m.x210 = Var(within=Reals,bounds=(None,1.6094379124341),initialize=-0.0594529251326021)
m.x211 = Var(within=Reals,bounds=(None,1.6094379124341),initialize=-2.17980108705855)
m.x212 = Var(within=Reals,bounds=(None,1.6094379124341),initialize=-2.8729482676185)
m.x213 = Var(within=Reals,bounds=(None,1.6094379124341),initialize=-3.39972974065073)
m.x214 = Var(within=Reals,bounds=(None,1.6094379124341),initialize=0.379588741113263)
m.x215 = Var(within=Reals,bounds=(None,1.6094379124341),initialize=0.379588741113263)
m.x216 = Var(within=Reals,bounds=(None,1.6094379124341),initialize=0)
m.x217 = Var(within=Reals,bounds=(None,1.6094379124341),initialize=0)
m.x218 = Var(within=Reals,bounds=(None,1.6094379124341),initialize=1.07273592167321)
m.x219 = Var(within=Reals,bounds=(None,1.6094379124341),initialize=-1.04921352161972)
m.x220 = Var(within=Reals,bounds=(None,1.6094379124341),initialize=-1.74236070217966)
m.x221 = Var(within=Reals,bounds=(None,1.6094379124341),initialize=-2.76785883450285)
m.x222 = Var(within=Reals,bounds=(None,1.6094379124341),initialize=-0.207931510667194)
m.x223 = Var(within=Reals,bounds=(None,1.6094379124341),initialize=-0.207931510667194)
m.x224 = Var(within=Reals,bounds=(None,1.6094379124341),initialize=-1.59422587178708)
m.x225 = Var(within=Reals,bounds=(None,1.6094379124341),initialize=-1.59422587178708)
m.x226 = Var(within=Reals,bounds=(None,1.6094379124341),initialize=-0.901078691227139)
m.x227 = Var(within=Reals,bounds=(None,1.6094379124341),initialize=-0.976679184885637)
m.x228 = Var(within=Reals,bounds=(None,1.6094379124341),initialize=-1.66982636544558)
m.x229 = Var(within=Reals,bounds=(None,1.6094379124341),initialize=-2.68796806893725)
m.x230 = Var(within=Reals,bounds=(None,None),initialize=-1.55578402094315)
m.x231 = Var(within=Reals,bounds=(-2.25129179860649,-2.25129179860649),initialize=-2.25129179860649)
m.x232 = Var(within=Reals,bounds=(None,None),initialize=-0.0594529251326021)
m.x233 = Var(within=Reals,bounds=(-2.25129179860649,-2.25129179860649),initialize=-2.25129179860649)
m.x234 = Var(within=Reals,bounds=(None,None),initialize=1.07273592167321)
m.x235 = Var(within=Reals,bounds=(-2.25129179860649,-2.25129179860649),initialize=-2.25129179860649)
m.x236 = Var(within=Reals,bounds=(None,None),initialize=-0.901078691227139)
m.x237 = Var(within=Reals,bounds=(-2.25129179860649,-2.25129179860649),initialize=-2.25129179860649)
m.x238 = Var(within=Reals,bounds=(None,None),initialize=0.422047741265856)
m.x239 = Var(within=Reals,bounds=(None,None),initialize=0.105511935316464)
m.x240 = Var(within=Reals,bounds=(None,None),initialize=0.105511935316464)
m.x241 = Var(within=Reals,bounds=(None,None),initialize=0.211023870632928)
m.x242 = Var(within=Reals,bounds=(None,None),initialize=0.0978292472354046)
m.x243 = Var(within=Reals,bounds=(None,None),initialize=0.0978292472354046)
m.x244 = Var(within=Reals,bounds=(None,None),initialize=0.0450989346367396)
m.x245 = Var(within=Reals,bounds=(None,None),initialize=0.471139945124032)
m.x246 = Var(within=Reals,bounds=(None,None),initialize=0.942279890248065)
m.x247 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x248 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x249 = Var(within=Reals,bounds=(None,None),initialize=0.0565320091501422)
m.x250 = Var(within=Reals,bounds=(None,None),initialize=0.0565320091501422)
m.x251 = Var(within=Reals,bounds=(None,None),initialize=0.033382290617452)
m.x252 = Var(within=Reals,bounds=(None,None),initialize=1.46168333554586)
m.x253 = Var(within=Reals,bounds=(None,None),initialize=2.92336667109171)
m.x254 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x255 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x256 = Var(within=Reals,bounds=(None,None),initialize=0.175106537920172)
m.x257 = Var(within=Reals,bounds=(None,None),initialize=0.175106537920172)
m.x258 = Var(within=Reals,bounds=(None,None),initialize=0.0627963182070535)
m.x259 = Var(within=Reals,bounds=(None,None),initialize=0.812262666134973)
m.x260 = Var(within=Reals,bounds=(None,None),initialize=0.203065666533743)
m.x261 = Var(within=Reals,bounds=(None,None),initialize=0.203065666533743)
m.x262 = Var(within=Reals,bounds=(None,None),initialize=0.406131333067486)
m.x263 = Var(within=Reals,bounds=(None,None),initialize=0.188279754672)
m.x264 = Var(within=Reals,bounds=(None,None),initialize=0.188279754672)
m.x265 = Var(within=Reals,bounds=(None,None),initialize=0.0680190089875055)
m.x266 = Var(within=Reals,bounds=(0.1,1),initialize=0.903778326897858)
m.x267 = Var(within=Reals,bounds=(0.1,1),initialize=0.975106465816068)
m.x268 = Var(within=Reals,bounds=(0.1,1),initialize=0.882989317955773)
m.x269 = Var(within=Reals,bounds=(0.95,0.95),initialize=0.95)
m.x270 = Var(within=Reals,bounds=(0.1,1),initialize=0.998315513250229)
m.x271 = Var(within=Reals,bounds=(0.1,1),initialize=0.931004925149313)
m.x272 = Var(within=Reals,bounds=(0.95,0.95),initialize=0.95)
m.x273 = Var(within=Reals,bounds=(0.1,1),initialize=0.998315513250229)
m.x274 = Var(within=Reals,bounds=(0.1,1),initialize=0.901706690780938)
m.x275 = Var(within=Reals,bounds=(0.95,0.95),initialize=0.95)
m.x276 = Var(within=Reals,bounds=(0.1,1),initialize=0.903778326897858)
m.x277 = Var(within=Reals,bounds=(0.1,1),initialize=0.975106465816068)
m.x278 = Var(within=Reals,bounds=(0.1,1),initialize=0.917593932953673)
m.x279 = Var(within=Reals,bounds=(0.95,0.95),initialize=0.95)
m.x280 = Var(within=Reals,bounds=(10,54.5),initialize=50)
m.x281 = Var(within=Reals,bounds=(10,54.5),initialize=50)
m.x282 = Var(within=Reals,bounds=(10,54.5),initialize=50)
m.x283 = Var(within=Reals,bounds=(10,54.5),initialize=50)
m.x284 = Var(within=Reals,bounds=(10,250),initialize=200)
m.x285 = Var(within=Reals,bounds=(10,250),initialize=200)
m.x286 = Var(within=Reals,bounds=(10,250),initialize=200)
m.x287 = Var(within=Reals,bounds=(10,250),initialize=200)
m.x288 = Var(within=Reals,bounds=(0.1,10),initialize=1.25)
m.x289 = Var(within=Reals,bounds=(0.1,10),initialize=1.25)
m.x290 = Var(within=Reals,bounds=(0.5,10),initialize=1.5)
m.x291 = Var(within=Reals,bounds=(0.5,10),initialize=1.5)
m.x292 = Var(within=Reals,bounds=(0.5,6),initialize=3)
m.x293 = Var(within=Reals,bounds=(0.5,6),initialize=3)
m.x294 = Var(within=Reals,bounds=(0.1,4),initialize=1)
m.x295 = Var(within=Reals,bounds=(0.1,4),initialize=1)
m.x296 = Var(within=Reals,bounds=(0.1,4),initialize=1)
m.x297 = Var(within=Reals,bounds=(0.1,4),initialize=1)

m.obj = Objective(expr=63400*exp(0.6*m.x1 + m.x81 + m.x89) + 5750*exp(0.6*m.x2 + m.x82 + m.x90) + 5750*exp(0.6*m.x3 + 
                       m.x83 + m.x91) + 5750*exp(0.6*m.x4 + m.x84 + m.x92) + 5750*exp(0.6*m.x5 + m.x85 + m.x93) + 23100*
                       exp(0.65*m.x6 + m.x86 + m.x94) + 5750*exp(0.6*m.x7 + m.x87 + m.x95) + 5750*exp(0.6*m.x8 + m.x88
                        + m.x96) + 5750*exp(0.6*m.x9 + m.x82 + m.x90) + 5750*exp(0.6*m.x10 + m.x84 + m.x92) + 360000*
                       exp(0.975*m.x11 + m.x88 + m.x96) + 2900*exp(0.85*m.x12 + m.x82 + m.x90) + 12100*exp(0.75*m.x13 + 
                       m.x83 + m.x91) + 2900*exp(0.85*m.x14 + m.x84 + m.x92) + 2900*exp(0.85*m.x15 + m.x85 + m.x93) + 
                       2900*exp(0.85*m.x16 + m.x87 + m.x95) + 5750*(exp(0.6*m.x98) + exp(0.6*m.x99) + exp(0.6*m.x100) + 
                       exp(0.6*m.x101) + exp(0.6*m.x102) + exp(0.6*m.x103) + exp(0.6*m.x104) + exp(0.6*m.x105))
                       , sense=minimize)

m.c1 = Constraint(expr=   m.x1 - m.x17 + m.x89 - m.x198 >= 0)

m.c2 = Constraint(expr=   m.x2 - m.x18 + m.x90 - m.x199 >= 0)

m.c3 = Constraint(expr=   m.x3 - m.x19 + m.x91 - m.x200 >= 0)

m.c4 = Constraint(expr=   m.x4 - m.x20 + m.x92 - m.x201 >= 0)

m.c5 = Constraint(expr=   m.x5 - m.x21 + m.x93 - m.x202 >= 0)

m.c6 = Constraint(expr=   m.x6 - m.x22 + m.x94 - m.x203 >= 0)

m.c7 = Constraint(expr=   m.x7 - m.x23 + m.x95 - m.x204 >= 0)

m.c8 = Constraint(expr=   m.x8 - m.x24 + m.x96 - m.x205 >= 0)

m.c9 = Constraint(expr=   m.x1 - m.x25 + m.x89 - m.x206 >= 0)

m.c10 = Constraint(expr=   m.x2 - m.x26 + m.x90 - m.x207 >= 0)

m.c11 = Constraint(expr=   m.x3 - m.x27 + m.x91 - m.x208 >= 0)

m.c12 = Constraint(expr=   m.x4 - m.x28 + m.x92 - m.x209 >= 0)

m.c13 = Constraint(expr=   m.x5 - m.x29 + m.x93 - m.x210 >= 0)

m.c14 = Constraint(expr=   m.x6 - m.x30 + m.x94 - m.x211 >= 0)

m.c15 = Constraint(expr=   m.x7 - m.x31 + m.x95 - m.x212 >= 0)

m.c16 = Constraint(expr=   m.x8 - m.x32 + m.x96 - m.x213 >= 0)

m.c17 = Constraint(expr=   m.x1 - m.x33 + m.x89 - m.x214 >= 0)

m.c18 = Constraint(expr=   m.x2 - m.x34 + m.x90 - m.x215 >= 0)

m.c19 = Constraint(expr=   m.x3 - m.x35 + m.x91 - m.x216 >= 0)

m.c20 = Constraint(expr=   m.x4 - m.x36 + m.x92 - m.x217 >= 0)

m.c21 = Constraint(expr=   m.x5 - m.x37 + m.x93 - m.x218 >= 0)

m.c22 = Constraint(expr=   m.x6 - m.x38 + m.x94 - m.x219 >= 0)

m.c23 = Constraint(expr=   m.x7 - m.x39 + m.x95 - m.x220 >= 0)

m.c24 = Constraint(expr=   m.x8 - m.x40 + m.x96 - m.x221 >= 0)

m.c25 = Constraint(expr=   m.x1 - m.x41 + m.x89 - m.x222 >= 0)

m.c26 = Constraint(expr=   m.x2 - m.x42 + m.x90 - m.x223 >= 0)

m.c27 = Constraint(expr=   m.x3 - m.x43 + m.x91 - m.x224 >= 0)

m.c28 = Constraint(expr=   m.x4 - m.x44 + m.x92 - m.x225 >= 0)

m.c29 = Constraint(expr=   m.x5 - m.x45 + m.x93 - m.x226 >= 0)

m.c30 = Constraint(expr=   m.x6 - m.x46 + m.x94 - m.x227 >= 0)

m.c31 = Constraint(expr=   m.x7 - m.x47 + m.x95 - m.x228 >= 0)

m.c32 = Constraint(expr=   m.x8 - m.x48 + m.x96 - m.x229 >= 0)

m.c33 = Constraint(expr=   m.x10 - m.x20 + m.x92 - m.x230 >= 0)

m.c34 = Constraint(expr=   m.x11 - m.x24 + m.x96 - m.x231 >= 0)

m.c35 = Constraint(expr=   m.x9 - m.x26 + m.x90 - m.x232 >= 0)

m.c36 = Constraint(expr=   m.x11 - m.x32 + m.x96 - m.x233 >= 0)

m.c37 = Constraint(expr=   m.x9 - m.x34 + m.x90 - m.x234 >= 0)

m.c38 = Constraint(expr=   m.x11 - m.x40 + m.x96 - m.x235 >= 0)

m.c39 = Constraint(expr=   m.x10 - m.x44 + m.x92 - m.x236 >= 0)

m.c40 = Constraint(expr=   m.x11 - m.x48 + m.x96 - m.x237 >= 0)

m.c41 = Constraint(expr=-log(15.6/(m.x280*m.x266*m.x267*m.x268*m.x269)) + m.x198 == 0)

m.c42 = Constraint(expr=-log(15.6/(m.x280*m.x266*m.x267*m.x268*m.x269)) + m.x199 == 0)

m.c43 = Constraint(expr=-log(15.6/(m.x284*m.x266*m.x267*m.x268*m.x269)) + m.x200 == 0)

m.c44 = Constraint(expr=-log(15.6/(m.x284*m.x266*m.x267*m.x268*m.x269)) + m.x201 == 0)

m.c45 = Constraint(expr=-log((7.8 + 15.6*m.x290)/(m.x284*m.x266*m.x267*m.x268*m.x269)) + m.x202 == 0)

m.c46 = Constraint(expr=-log((0.075 + 0.075*m.x294)/(exp(-0.03*m.x292)*m.x269*m.x268)) + m.x203 == 0)

m.c47 = Constraint(expr=-log(0.075/(exp(-0.03*m.x292)*m.x269*m.x268)) + m.x204 == 0)

m.c48 = Constraint(expr=-log((0.05*m.x294/(1 + m.x294)**2 + 0.025*m.x268)/(m.x268*m.x269*exp(-0.03*m.x292))) + m.x205
                         == 0)

m.c49 = Constraint(expr=-log(20.8/(m.x281*m.x272*m.x270*m.x271)) + m.x206 == 0)

m.c50 = Constraint(expr=-log(20.8/(m.x281*m.x272*m.x270*m.x271)) + m.x207 == 0)

m.c51 = Constraint(expr=-log((20.8 - 20.8*m.x281/m.x285 + 20.8*m.x288)/(m.x281*m.x270*m.x271*m.x272)) + m.x210 == 0)

m.c52 = Constraint(expr=-log((0.05 + 0.05*m.x295)/(m.x272*m.x271)) + m.x211 == 0)

m.c53 = Constraint(expr=-log(0.05/(m.x272*m.x271)) + m.x212 == 0)

m.c54 = Constraint(expr=-log((0.025*m.x295/(1 + m.x295)**2 + 0.025*m.x271)/(m.x271*m.x272)) + m.x213 == 0)

m.c55 = Constraint(expr=-log(62.5/(m.x282*m.x275*m.x273*m.x274)) + m.x214 == 0)

m.c56 = Constraint(expr=-log(62.5/(m.x282*m.x275*m.x273*m.x274)) + m.x215 == 0)

m.c57 = Constraint(expr=-log((62.5 - 62.5*m.x282/m.x286 + 62.5*m.x289)/(m.x282*m.x273*m.x274*m.x275)) + m.x218 == 0)

m.c58 = Constraint(expr=-log((0.15 + 0.15*m.x296)/(m.x275*m.x274)) + m.x219 == 0)

m.c59 = Constraint(expr=-log(0.15/(m.x275*m.x274)) + m.x220 == 0)

m.c60 = Constraint(expr=-log((0.125*m.x296/(1 + m.x296)**2 + 0.025*m.x274)/(m.x274*m.x275)) + m.x221 == 0)

m.c61 = Constraint(expr=-log(31.2/(m.x283*m.x276*m.x277*m.x278*m.x279)) + m.x222 == 0)

m.c62 = Constraint(expr=-log(31.2/(m.x283*m.x276*m.x277*m.x278*m.x279)) + m.x223 == 0)

m.c63 = Constraint(expr=-log(31.2/(m.x287*m.x276*m.x277*m.x278*m.x279)) + m.x224 == 0)

m.c64 = Constraint(expr=-log(31.2/(m.x287*m.x276*m.x277*m.x278*m.x279)) + m.x225 == 0)

m.c65 = Constraint(expr=-log((15.6 + 31.2*m.x291)/(m.x287*m.x276*m.x277*m.x278*m.x279)) + m.x226 == 0)

m.c66 = Constraint(expr=-log((0.15 + 0.15*m.x297)/(exp(-0.03*m.x293)*m.x279*m.x278)) + m.x227 == 0)

m.c67 = Constraint(expr=-log(0.15/(exp(-0.03*m.x293)*m.x279*m.x278)) + m.x228 == 0)

m.c68 = Constraint(expr=-log((0.125*m.x297/(1 + m.x297)**2 + 0.025*m.x278)/(m.x278*m.x279*exp(-0.03*m.x293))) + m.x229
                         == 0)

m.c69 = Constraint(expr=-log((7.8 + 15.6*m.x290)/(m.x284*m.x266*m.x267*m.x268*m.x269)) + m.x230 == 0)

m.c70 = Constraint(expr=-log((20.8 - 20.8*m.x281/m.x285 + 20.8*m.x288)/(m.x281*m.x270*m.x271*m.x272)) + m.x232 == 0)

m.c71 = Constraint(expr=-log((62.5 - 62.5*m.x282/m.x286 + 62.5*m.x289)/(m.x282*m.x273*m.x274*m.x275)) + m.x234 == 0)

m.c72 = Constraint(expr=-log((15.6 + 31.2*m.x291)/(m.x287*m.x276*m.x277*m.x278*m.x279)) + m.x236 == 0)

m.c73 = Constraint(expr=-exp(m.x199) + m.x238 == 0)

m.c74 = Constraint(expr=-15.6/(m.x284*m.x266*m.x267*m.x268*m.x269) + m.x239 == 0)

m.c75 = Constraint(expr=-15.6/(m.x284*m.x266*m.x267*m.x268*m.x269) + m.x240 == 0)

m.c76 = Constraint(expr=-(7.8 + 15.6*m.x290)/(m.x284*m.x266*m.x267*m.x268*m.x269) + m.x241 == 0)

m.c77 = Constraint(expr=-0.075/(exp(-0.03*m.x292)*m.x269*m.x268) + m.x242 == 0)

m.c78 = Constraint(expr=-0.075/(exp(-0.03*m.x292)*m.x269*m.x268) + m.x243 == 0)

m.c79 = Constraint(expr=-exp(m.x205) + m.x244 == 0)

m.c80 = Constraint(expr=-exp(m.x207) + m.x245 == 0)

m.c81 = Constraint(expr=-(20.8 - 20.8*m.x281/m.x285 + 20.8*m.x288)/(m.x281*m.x270*m.x271*m.x272) + m.x246 == 0)

m.c82 = Constraint(expr=-0.05/(m.x272*m.x271) + m.x249 == 0)

m.c83 = Constraint(expr=-0.05/(m.x272*m.x271) + m.x250 == 0)

m.c84 = Constraint(expr=-exp(m.x213) + m.x251 == 0)

m.c85 = Constraint(expr=-exp(m.x215) + m.x252 == 0)

m.c86 = Constraint(expr=-(62.5 - 62.5*m.x282/m.x286 + 62.5*m.x289)/(m.x282*m.x273*m.x274*m.x275) + m.x253 == 0)

m.c87 = Constraint(expr=-0.15/(m.x275*m.x274) + m.x256 == 0)

m.c88 = Constraint(expr=-0.15/(m.x275*m.x274) + m.x257 == 0)

m.c89 = Constraint(expr=-exp(m.x221) + m.x258 == 0)

m.c90 = Constraint(expr=-exp(m.x223) + m.x259 == 0)

m.c91 = Constraint(expr=-31.2/(m.x287*m.x276*m.x277*m.x278*m.x279) + m.x260 == 0)

m.c92 = Constraint(expr=-31.2/(m.x287*m.x276*m.x277*m.x278*m.x279) + m.x261 == 0)

m.c93 = Constraint(expr=-(15.6 + 31.2*m.x291)/(m.x287*m.x276*m.x277*m.x278*m.x279) + m.x262 == 0)

m.c94 = Constraint(expr=-0.15/(exp(-0.03*m.x293)*m.x279*m.x278) + m.x263 == 0)

m.c95 = Constraint(expr=-0.15/(exp(-0.03*m.x293)*m.x279*m.x278) + m.x264 == 0)

m.c96 = Constraint(expr=-exp(m.x229) + m.x265 == 0)

m.c97 = Constraint(expr=-log(4 + 3.8*log(0.35*m.x280/(1 - 0.0181818181818182*m.x280))) + m.x49 == 0)

m.c98 = Constraint(expr=-log(1.25 + (62.5 - 62.5*m.x280/m.x284)/m.x280*m.x266*m.x267*m.x268*m.x269*exp(m.x18)/exp(m.x12)
                        ) + m.x50 == 0)

m.c99 = Constraint(expr=-log(1.25 + 12.5*m.x292/(m.x284*m.x266*m.x267*m.x268*m.x269)*exp(m.x19)/exp(m.x13)) + m.x51
                         == 0)

m.c100 = Constraint(expr=-log(1.75 + (62.5 + 125*m.x290)/(m.x284*m.x266*m.x267*m.x268*m.x269)*exp(m.x20)/exp(m.x14))
                          + m.x52 == 0)

m.c101 = Constraint(expr=-log(1 + (312.5 + 625*m.x290)/(m.x284*m.x266*m.x267*m.x268*m.x269)*(1 - (0.24 - 0.24*exp(-1.5*
                         m.x292))*m.x284*(1 - 0.5*exp(-2*m.x290))/(25 + 50*m.x290))*exp(m.x21)/exp(m.x15)) + m.x53 == 0)

m.c102 = Constraint(expr=-log(0.3 + (3 - 2*m.x294/(1 + m.x294)**2 - m.x268)/(m.x268*m.x269*exp(-0.03*m.x292))*exp(m.x23)
                         /exp(m.x16)) + m.x55 == 0)

m.c103 = Constraint(expr=-log(0.375 + (0.005*m.x294/(1 + m.x294)**2 + 0.0025*m.x268)/(m.x268*m.x269*exp(-0.03*m.x292))*
                         exp(m.x24)/exp(m.x11)) + m.x56 == 0)

m.c104 = Constraint(expr=-log(4 + 3.8*log(0.35*m.x281/(1 - 0.0181818181818182*m.x281))) + m.x57 == 0)

m.c105 = Constraint(expr=-log(1.75 + (83.5 - 83.5*m.x281/m.x285 + 83.5*m.x288)/m.x281*m.x270*m.x271*m.x272*exp(m.x26)/
                         exp(m.x12)) + m.x58 == 0)

m.c106 = Constraint(expr=-log(1 + (835 - 835*m.x281/m.x285 + 835*m.x288)/(m.x281*m.x270*m.x271*m.x272)*(1 - 0.12*m.x281*
                         m.x270/(50 - 50*m.x281/m.x285 + 50*m.x288))*exp(m.x29)/exp(m.x15)) + m.x61 == 0)

m.c107 = Constraint(expr=-log(0.3 + (2 - m.x295/(1 + m.x295)**2 - m.x271)/(m.x271*m.x272)*exp(m.x31)/exp(m.x16)) + m.x63
                          == 0)

m.c108 = Constraint(expr=-log(0.375 + (0.0025*m.x295/(1 + m.x295)**2 + 0.0025*m.x271)/(m.x271*m.x272)*exp(m.x32)/exp(
                         m.x11)) + m.x64 == 0)

m.c109 = Constraint(expr=-log(4 + 3.8*log(0.35*m.x282/(1 - 0.0181818181818182*m.x282))) + m.x65 == 0)

m.c110 = Constraint(expr=-log(1.75 + (250 - 250*m.x282/m.x286 + 250*m.x289)/(m.x282*m.x273*m.x274*m.x275)*exp(m.x34)/
                         exp(m.x12)) + m.x66 == 0)

m.c111 = Constraint(expr=-log(1 + (2500 - 2500*m.x282/m.x286 + 2500*m.x289)/(m.x282*m.x273*m.x274*m.x275)*(1 - 0.12*
                         m.x282*m.x273/(50 - 50*m.x282/m.x286 + 50*m.x289))*exp(m.x37)/exp(m.x15)) + m.x69 == 0)

m.c112 = Constraint(expr=-log(0.3 + (6 - 5*m.x296/(1 + m.x296)**2 - m.x274)/(m.x274*m.x275)*exp(m.x39)/exp(m.x16))
                          + m.x71 == 0)

m.c113 = Constraint(expr=-log(0.375 + (0.0125*m.x296/(1 + m.x296)**2 + 0.0025*m.x274)/(m.x274*m.x275)*exp(m.x40)/exp(
                         m.x11)) + m.x72 == 0)

m.c114 = Constraint(expr=-log(4 + 3.8*log(0.35*m.x283/(1 - 0.0181818181818182*m.x283))) + m.x73 == 0)

m.c115 = Constraint(expr=-log(1.25 + (125 - 125*m.x283/m.x287)/(m.x283*m.x276*m.x277*m.x278*m.x279)*exp(m.x42)/exp(m.x12
                         )) + m.x74 == 0)

m.c116 = Constraint(expr=-log(1.25 + 25*m.x293/(m.x287*m.x276*m.x277*m.x278*m.x279)*exp(m.x43)/exp(m.x13)) + m.x75 == 0)

m.c117 = Constraint(expr=-log(1.75 + (125 + 250*m.x291)/(m.x287*m.x276*m.x277*m.x278*m.x279)*exp(m.x44)/exp(m.x14))
                          + m.x76 == 0)

m.c118 = Constraint(expr=-log(1 + (625 + 1250*m.x291)/(m.x287*m.x276*m.x277*m.x278*m.x279)*(1 - (0.24 - 0.24*exp(-1.5*
                         m.x293))*m.x287*(1 - 0.5*exp(-2*m.x291))/(25 + 50*m.x291))*exp(m.x45)/exp(m.x15)) + m.x77 == 0)

m.c119 = Constraint(expr=-log(0.3 + (6 - 5*m.x297/(1 + m.x297)**2 - m.x278)/(m.x278*m.x279*exp(-0.03*m.x293))*exp(m.x47)
                         /exp(m.x16)) + m.x79 == 0)

m.c120 = Constraint(expr=-log(0.375 + (0.0125*m.x297/(1 + m.x297)**2 + 0.0025*m.x278)/(m.x278*m.x279*exp(-0.03*m.x293))*
                         exp(m.x48)/exp(m.x11)) + m.x80 == 0)

m.c121 = Constraint(expr=-(1 - exp(-1.5*m.x292))*exp(-0.03*m.x292) + m.x266 == 0)

m.c122 = Constraint(expr=0.5*exp(-2*m.x290) + m.x267 == 1)

m.c123 = Constraint(expr=-25.1*m.x294/((1 + 10**(-3.5 + 4.9*m.x294/(1 + m.x294))*m.x294)*(1 + 25.1*m.x294)) + m.x268
                          == 0)

m.c124 = Constraint(expr=m.x281/m.x285*exp(-m.x288*m.x285/m.x281) + m.x270 == 1)

m.c125 = Constraint(expr=-50.1*m.x295/((1 + 10**(-4.25 + 5.95*m.x295/(1 + m.x295))*m.x295)*(1 + 50.1*m.x295)) + m.x271
                          == 0)

m.c126 = Constraint(expr=m.x282/m.x286*exp(-m.x289*m.x286/m.x282) + m.x273 == 1)

m.c127 = Constraint(expr=-31.6*m.x296/((1 + 10**(-3.75 + 5.25*m.x296/(1 + m.x296))*m.x296)*(1 + 31.6*m.x296)) + m.x274
                          == 0)

m.c128 = Constraint(expr=-(1 - exp(-1.5*m.x293))*exp(-0.03*m.x293) + m.x276 == 0)

m.c129 = Constraint(expr=0.5*exp(-2*m.x291) + m.x277 == 1)

m.c130 = Constraint(expr=-39.8*m.x297/((1 + 10**(-4 + 5.6*m.x297/(1 + m.x297))*m.x297)*(1 + 39.8*m.x297)) + m.x278 == 0)

m.c131 = Constraint(expr= - m.x17 + m.x49 - m.x81 - m.x106 <= 0)

m.c132 = Constraint(expr= - m.x18 + m.x50 - m.x82 - m.x106 <= 0)

m.c133 = Constraint(expr= - m.x19 + m.x51 - m.x83 - m.x106 <= 0)

m.c134 = Constraint(expr= - m.x20 + m.x52 - m.x84 - m.x106 <= 0)

m.c135 = Constraint(expr= - m.x21 + m.x53 - m.x85 - m.x106 <= 0)

m.c136 = Constraint(expr= - m.x22 + m.x54 - m.x86 - m.x106 <= 0)

m.c137 = Constraint(expr= - m.x23 + m.x55 - m.x87 - m.x106 <= 0)

m.c138 = Constraint(expr= - m.x24 + m.x56 - m.x88 - m.x106 <= 0)

m.c139 = Constraint(expr= - m.x25 + m.x57 - m.x81 - m.x107 <= 0)

m.c140 = Constraint(expr= - m.x26 + m.x58 - m.x82 - m.x107 <= 0)

m.c141 = Constraint(expr= - m.x27 + m.x59 - m.x83 - m.x107 <= 0)

m.c142 = Constraint(expr= - m.x28 + m.x60 - m.x84 - m.x107 <= 0)

m.c143 = Constraint(expr= - m.x29 + m.x61 - m.x85 - m.x107 <= 0)

m.c144 = Constraint(expr= - m.x30 + m.x62 - m.x86 - m.x107 <= 0)

m.c145 = Constraint(expr= - m.x31 + m.x63 - m.x87 - m.x107 <= 0)

m.c146 = Constraint(expr= - m.x32 + m.x64 - m.x88 - m.x107 <= 0)

m.c147 = Constraint(expr= - m.x33 + m.x65 - m.x81 - m.x108 <= 0)

m.c148 = Constraint(expr= - m.x34 + m.x66 - m.x82 - m.x108 <= 0)

m.c149 = Constraint(expr= - m.x35 + m.x67 - m.x83 - m.x108 <= 0)

m.c150 = Constraint(expr= - m.x36 + m.x68 - m.x84 - m.x108 <= 0)

m.c151 = Constraint(expr= - m.x37 + m.x69 - m.x85 - m.x108 <= 0)

m.c152 = Constraint(expr= - m.x38 + m.x70 - m.x86 - m.x108 <= 0)

m.c153 = Constraint(expr= - m.x39 + m.x71 - m.x87 - m.x108 <= 0)

m.c154 = Constraint(expr= - m.x40 + m.x72 - m.x88 - m.x108 <= 0)

m.c155 = Constraint(expr= - m.x41 + m.x73 - m.x81 - m.x109 <= 0)

m.c156 = Constraint(expr= - m.x42 + m.x74 - m.x82 - m.x109 <= 0)

m.c157 = Constraint(expr= - m.x43 + m.x75 - m.x83 - m.x109 <= 0)

m.c158 = Constraint(expr= - m.x44 + m.x76 - m.x84 - m.x109 <= 0)

m.c159 = Constraint(expr= - m.x45 + m.x77 - m.x85 - m.x109 <= 0)

m.c160 = Constraint(expr= - m.x46 + m.x78 - m.x86 - m.x109 <= 0)

m.c161 = Constraint(expr= - m.x47 + m.x79 - m.x87 - m.x109 <= 0)

m.c162 = Constraint(expr= - m.x48 + m.x80 - m.x88 - m.x109 <= 0)

m.c163 = Constraint(expr=6000*exp(m.x106) + 3000*exp(m.x107) + 1500*exp(m.x108) + 1000*exp(m.x109) <= 6000)

m.c164 = Constraint(expr=   m.x17 - m.x18 - 2.99573227355399*m.b110 <= 0)

m.c165 = Constraint(expr=   m.x18 - m.x19 - 2.99573227355399*m.b111 <= 0)

m.c166 = Constraint(expr=   m.x19 - m.x20 - 2.99573227355399*m.b112 <= 0)

m.c167 = Constraint(expr=   m.x20 - m.x21 - 2.99573227355399*m.b113 <= 0)

m.c168 = Constraint(expr=   m.x21 - m.x22 - 2.99573227355399*m.b114 <= 0)

m.c169 = Constraint(expr=   m.x22 - m.x23 - 2.99573227355399*m.b115 <= 0)

m.c170 = Constraint(expr=   m.x23 - m.x24 - 2.99573227355399*m.b116 <= 0)

m.c171 = Constraint(expr=   m.x25 - m.x26 - 2.99573227355399*m.b110 <= 0)

m.c172 = Constraint(expr=   m.x26 - m.x27 - 2.99573227355399*m.b111 <= 0)

m.c173 = Constraint(expr=   m.x27 - m.x28 - 2.99573227355399*m.b112 <= 0)

m.c174 = Constraint(expr=   m.x28 - m.x29 - 2.99573227355399*m.b113 <= 0)

m.c175 = Constraint(expr=   m.x29 - m.x30 - 2.99573227355399*m.b114 <= 0)

m.c176 = Constraint(expr=   m.x30 - m.x31 - 2.99573227355399*m.b115 <= 0)

m.c177 = Constraint(expr=   m.x31 - m.x32 - 2.99573227355399*m.b116 <= 0)

m.c178 = Constraint(expr=   m.x33 - m.x34 - 2.99573227355399*m.b110 <= 0)

m.c179 = Constraint(expr=   m.x34 - m.x35 - 2.99573227355399*m.b111 <= 0)

m.c180 = Constraint(expr=   m.x35 - m.x36 - 2.99573227355399*m.b112 <= 0)

m.c181 = Constraint(expr=   m.x36 - m.x37 - 2.99573227355399*m.b113 <= 0)

m.c182 = Constraint(expr=   m.x37 - m.x38 - 2.99573227355399*m.b114 <= 0)

m.c183 = Constraint(expr=   m.x38 - m.x39 - 2.99573227355399*m.b115 <= 0)

m.c184 = Constraint(expr=   m.x39 - m.x40 - 2.99573227355399*m.b116 <= 0)

m.c185 = Constraint(expr=   m.x41 - m.x42 - 2.99573227355399*m.b110 <= 0)

m.c186 = Constraint(expr=   m.x42 - m.x43 - 2.99573227355399*m.b111 <= 0)

m.c187 = Constraint(expr=   m.x43 - m.x44 - 2.99573227355399*m.b112 <= 0)

m.c188 = Constraint(expr=   m.x44 - m.x45 - 2.99573227355399*m.b113 <= 0)

m.c189 = Constraint(expr=   m.x45 - m.x46 - 2.99573227355399*m.b114 <= 0)

m.c190 = Constraint(expr=   m.x46 - m.x47 - 2.99573227355399*m.b115 <= 0)

m.c191 = Constraint(expr=   m.x47 - m.x48 - 2.99573227355399*m.b116 <= 0)

m.c192 = Constraint(expr=   m.x17 - m.x18 + 2.99573227355399*m.b110 >= 0)

m.c193 = Constraint(expr=   m.x18 - m.x19 + 2.99573227355399*m.b111 >= 0)

m.c194 = Constraint(expr=   m.x19 - m.x20 + 2.99573227355399*m.b112 >= 0)

m.c195 = Constraint(expr=   m.x20 - m.x21 + 2.99573227355399*m.b113 >= 0)

m.c196 = Constraint(expr=   m.x21 - m.x22 + 2.99573227355399*m.b114 >= 0)

m.c197 = Constraint(expr=   m.x22 - m.x23 + 2.99573227355399*m.b115 >= 0)

m.c198 = Constraint(expr=   m.x23 - m.x24 + 2.99573227355399*m.b116 >= 0)

m.c199 = Constraint(expr=   m.x25 - m.x26 + 2.99573227355399*m.b110 >= 0)

m.c200 = Constraint(expr=   m.x26 - m.x27 + 2.99573227355399*m.b111 >= 0)

m.c201 = Constraint(expr=   m.x27 - m.x28 + 2.99573227355399*m.b112 >= 0)

m.c202 = Constraint(expr=   m.x28 - m.x29 + 2.99573227355399*m.b113 >= 0)

m.c203 = Constraint(expr=   m.x29 - m.x30 + 2.99573227355399*m.b114 >= 0)

m.c204 = Constraint(expr=   m.x30 - m.x31 + 2.99573227355399*m.b115 >= 0)

m.c205 = Constraint(expr=   m.x31 - m.x32 + 2.99573227355399*m.b116 >= 0)

m.c206 = Constraint(expr=   m.x33 - m.x34 + 2.99573227355399*m.b110 >= 0)

m.c207 = Constraint(expr=   m.x34 - m.x35 + 2.99573227355399*m.b111 >= 0)

m.c208 = Constraint(expr=   m.x35 - m.x36 + 2.99573227355399*m.b112 >= 0)

m.c209 = Constraint(expr=   m.x36 - m.x37 + 2.99573227355399*m.b113 >= 0)

m.c210 = Constraint(expr=   m.x37 - m.x38 + 2.99573227355399*m.b114 >= 0)

m.c211 = Constraint(expr=   m.x38 - m.x39 + 2.99573227355399*m.b115 >= 0)

m.c212 = Constraint(expr=   m.x39 - m.x40 + 2.99573227355399*m.b116 >= 0)

m.c213 = Constraint(expr=   m.x41 - m.x42 + 2.99573227355399*m.b110 >= 0)

m.c214 = Constraint(expr=   m.x42 - m.x43 + 2.99573227355399*m.b111 >= 0)

m.c215 = Constraint(expr=   m.x43 - m.x44 + 2.99573227355399*m.b112 >= 0)

m.c216 = Constraint(expr=   m.x44 - m.x45 + 2.99573227355399*m.b113 >= 0)

m.c217 = Constraint(expr=   m.x45 - m.x46 + 2.99573227355399*m.b114 >= 0)

m.c218 = Constraint(expr=   m.x46 - m.x47 + 2.99573227355399*m.b115 >= 0)

m.c219 = Constraint(expr=   m.x47 - m.x48 + 2.99573227355399*m.b116 >= 0)

m.c220 = Constraint(expr=-(exp(m.x17 - m.x98) + exp(m.x18 - m.x98))*m.x238 - 10*m.b110 >= -11)

m.c221 = Constraint(expr=-(exp(m.x18 - m.x99) + exp(m.x19 - m.x99))*m.x239 - 10*m.b111 >= -11)

m.c222 = Constraint(expr=-(exp(m.x19 - m.x100) + exp(m.x20 - m.x100))*m.x240 - 10*m.b112 >= -11)

m.c223 = Constraint(expr=-(exp(m.x20 - m.x101) + exp(m.x21 - m.x101))*m.x241 - 10*m.b113 >= -11)

m.c224 = Constraint(expr=-(exp(m.x21 - m.x102) + exp(m.x22 - m.x102))*m.x242 - 10*m.b114 >= -11)

m.c225 = Constraint(expr=-(exp(m.x22 - m.x103) + exp(m.x23 - m.x103))*m.x243 - 10*m.b115 >= -11)

m.c226 = Constraint(expr=-(exp(m.x23 - m.x104) + exp(m.x24 - m.x104))*m.x244 - 10*m.b116 >= -11)

m.c227 = Constraint(expr=-(exp(m.x25 - m.x98) + exp(m.x26 - m.x98))*m.x245 - 10*m.b110 >= -11)

m.c228 = Constraint(expr=-(exp(m.x26 - m.x99) + exp(m.x27 - m.x99))*m.x246 - 10*m.b111 >= -11)

m.c229 = Constraint(expr=-(exp(m.x27 - m.x100) + exp(m.x28 - m.x100))*m.x247 - 10*m.b112 >= -11)

m.c230 = Constraint(expr=-(exp(m.x28 - m.x101) + exp(m.x29 - m.x101))*m.x248 - 10*m.b113 >= -11)

m.c231 = Constraint(expr=-(exp(m.x29 - m.x102) + exp(m.x30 - m.x102))*m.x249 - 10*m.b114 >= -11)

m.c232 = Constraint(expr=-(exp(m.x30 - m.x103) + exp(m.x31 - m.x103))*m.x250 - 10*m.b115 >= -11)

m.c233 = Constraint(expr=-(exp(m.x31 - m.x104) + exp(m.x32 - m.x104))*m.x251 - 10*m.b116 >= -11)

m.c234 = Constraint(expr=-(exp(m.x33 - m.x98) + exp(m.x34 - m.x98))*m.x252 - 10*m.b110 >= -11)

m.c235 = Constraint(expr=-(exp(m.x34 - m.x99) + exp(m.x35 - m.x99))*m.x253 - 10*m.b111 >= -11)

m.c236 = Constraint(expr=-(exp(m.x35 - m.x100) + exp(m.x36 - m.x100))*m.x254 - 10*m.b112 >= -11)

m.c237 = Constraint(expr=-(exp(m.x36 - m.x101) + exp(m.x37 - m.x101))*m.x255 - 10*m.b113 >= -11)

m.c238 = Constraint(expr=-(exp(m.x37 - m.x102) + exp(m.x38 - m.x102))*m.x256 - 10*m.b114 >= -11)

m.c239 = Constraint(expr=-(exp(m.x38 - m.x103) + exp(m.x39 - m.x103))*m.x257 - 10*m.b115 >= -11)

m.c240 = Constraint(expr=-(exp(m.x39 - m.x104) + exp(m.x40 - m.x104))*m.x258 - 10*m.b116 >= -11)

m.c241 = Constraint(expr=-(exp(m.x41 - m.x98) + exp(m.x42 - m.x98))*m.x259 - 10*m.b110 >= -11)

m.c242 = Constraint(expr=-(exp(m.x42 - m.x99) + exp(m.x43 - m.x99))*m.x260 - 10*m.b111 >= -11)

m.c243 = Constraint(expr=-(exp(m.x43 - m.x100) + exp(m.x44 - m.x100))*m.x261 - 10*m.b112 >= -11)

m.c244 = Constraint(expr=-(exp(m.x44 - m.x101) + exp(m.x45 - m.x101))*m.x262 - 10*m.b113 >= -11)

m.c245 = Constraint(expr=-(exp(m.x45 - m.x102) + exp(m.x46 - m.x102))*m.x263 - 10*m.b114 >= -11)

m.c246 = Constraint(expr=-(exp(m.x46 - m.x103) + exp(m.x47 - m.x103))*m.x264 - 10*m.b115 >= -11)

m.c247 = Constraint(expr=-(exp(m.x47 - m.x104) + exp(m.x48 - m.x104))*m.x265 - 10*m.b116 >= -11)

m.c248 = Constraint(expr=   m.x81 - 0.693147180559945*m.b126 - 1.09861228866811*m.b134 - 1.38629436111989*m.b142
                          - 1.6094379124341*m.b150 == 0)

m.c249 = Constraint(expr=   m.x82 - 0.693147180559945*m.b127 - 1.09861228866811*m.b135 - 1.38629436111989*m.b143
                          - 1.6094379124341*m.b151 == 0)

m.c250 = Constraint(expr=   m.x83 - 0.693147180559945*m.b128 - 1.09861228866811*m.b136 - 1.38629436111989*m.b144
                          - 1.6094379124341*m.b152 == 0)

m.c251 = Constraint(expr=   m.x84 - 0.693147180559945*m.b129 - 1.09861228866811*m.b137 - 1.38629436111989*m.b145
                          - 1.6094379124341*m.b153 == 0)

m.c252 = Constraint(expr=   m.x85 - 0.693147180559945*m.b130 - 1.09861228866811*m.b138 - 1.38629436111989*m.b146
                          - 1.6094379124341*m.b154 == 0)

m.c253 = Constraint(expr=   m.x86 - 0.693147180559945*m.b131 - 1.09861228866811*m.b139 - 1.38629436111989*m.b147
                          - 1.6094379124341*m.b155 == 0)

m.c254 = Constraint(expr=   m.x87 - 0.693147180559945*m.b132 - 1.09861228866811*m.b140 - 1.38629436111989*m.b148
                          - 1.6094379124341*m.b156 == 0)

m.c255 = Constraint(expr=   m.x88 - 0.693147180559945*m.b133 - 1.09861228866811*m.b141 - 1.38629436111989*m.b149
                          - 1.6094379124341*m.b157 == 0)

m.c256 = Constraint(expr=   m.b118 + m.b126 + m.b134 + m.b142 + m.b150 == 1)

m.c257 = Constraint(expr=   m.b119 + m.b127 + m.b135 + m.b143 + m.b151 == 1)

m.c258 = Constraint(expr=   m.b120 + m.b128 + m.b136 + m.b144 + m.b152 == 1)

m.c259 = Constraint(expr=   m.b121 + m.b129 + m.b137 + m.b145 + m.b153 == 1)

m.c260 = Constraint(expr=   m.b122 + m.b130 + m.b138 + m.b146 + m.b154 == 1)

m.c261 = Constraint(expr=   m.b123 + m.b131 + m.b139 + m.b147 + m.b155 == 1)

m.c262 = Constraint(expr=   m.b124 + m.b132 + m.b140 + m.b148 + m.b156 == 1)

m.c263 = Constraint(expr=   m.b125 + m.b133 + m.b141 + m.b149 + m.b157 == 1)

m.c264 = Constraint(expr=   m.x89 - 0.693147180559945*m.b166 - 1.09861228866811*m.b174 - 1.38629436111989*m.b182
                          - 1.6094379124341*m.b190 == 0)

m.c265 = Constraint(expr=   m.x90 - 0.693147180559945*m.b167 - 1.09861228866811*m.b175 - 1.38629436111989*m.b183
                          - 1.6094379124341*m.b191 == 0)

m.c266 = Constraint(expr=   m.x91 - 0.693147180559945*m.b168 - 1.09861228866811*m.b176 - 1.38629436111989*m.b184
                          - 1.6094379124341*m.b192 == 0)

m.c267 = Constraint(expr=   m.x92 - 0.693147180559945*m.b169 - 1.09861228866811*m.b177 - 1.38629436111989*m.b185
                          - 1.6094379124341*m.b193 == 0)

m.c268 = Constraint(expr=   m.x93 - 0.693147180559945*m.b170 - 1.09861228866811*m.b178 - 1.38629436111989*m.b186
                          - 1.6094379124341*m.b194 == 0)

m.c269 = Constraint(expr=   m.x94 - 0.693147180559945*m.b171 - 1.09861228866811*m.b179 - 1.38629436111989*m.b187
                          - 1.6094379124341*m.b195 == 0)

m.c270 = Constraint(expr=   m.x95 - 0.693147180559945*m.b172 - 1.09861228866811*m.b180 - 1.38629436111989*m.b188
                          - 1.6094379124341*m.b196 == 0)

m.c271 = Constraint(expr=   m.x96 - 0.693147180559945*m.b173 - 1.09861228866811*m.b181 - 1.38629436111989*m.b189
                          - 1.6094379124341*m.b197 == 0)

m.c272 = Constraint(expr=   m.b158 + m.b166 + m.b174 + m.b182 + m.b190 == 1)

m.c273 = Constraint(expr=   m.b159 + m.b167 + m.b175 + m.b183 + m.b191 == 1)

m.c274 = Constraint(expr=   m.b160 + m.b168 + m.b176 + m.b184 + m.b192 == 1)

m.c275 = Constraint(expr=   m.b161 + m.b169 + m.b177 + m.b185 + m.b193 == 1)

m.c276 = Constraint(expr=   m.b162 + m.b170 + m.b178 + m.b186 + m.b194 == 1)

m.c277 = Constraint(expr=   m.b163 + m.b171 + m.b179 + m.b187 + m.b195 == 1)

m.c278 = Constraint(expr=   m.b164 + m.b172 + m.b180 + m.b188 + m.b196 == 1)

m.c279 = Constraint(expr=   m.b165 + m.b173 + m.b181 + m.b189 + m.b197 == 1)

m.c280 = Constraint(expr=   m.b110 + m.b111 + m.b112 + m.b113 + m.b114 + m.b115 + m.b116 + m.b117 <= 7)

m.c282 = Constraint(expr=   m.x280 - m.x284 <= 0)

m.c283 = Constraint(expr=   m.x281 - m.x285 <= 0)

m.c284 = Constraint(expr=   m.x282 - m.x286 <= 0)

m.c285 = Constraint(expr=   m.x283 - m.x287 <= 0)
