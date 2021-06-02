#  MINLP written by GAMS Convert at 04/21/18 13:55:06
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        138       54       14       70        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        196       70      126        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        757      711       46        0
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
m.x43 = Var(within=Reals,bounds=(6.5,None),initialize=11.5)
m.x44 = Var(within=Reals,bounds=(3.25,None),initialize=8.25)
m.x45 = Var(within=Reals,bounds=(16.58,None),initialize=21.58)
m.x46 = Var(within=Reals,bounds=(14.92,None),initialize=19.92)
m.x47 = Var(within=Reals,bounds=(12.925,None),initialize=17.925)
m.x48 = Var(within=Reals,bounds=(12.26,None),initialize=17.26)
m.x49 = Var(within=Reals,bounds=(8.76,None),initialize=13.76)
m.x50 = Var(within=Reals,bounds=(16.08,None),initialize=21.08)
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
m.x65 = Var(within=Reals,bounds=(0,2.5),initialize=0.961470588235294)
m.x66 = Var(within=Reals,bounds=(0,6),initialize=2.30752941176471)
m.x67 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x68 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x69 = Var(within=Reals,bounds=(None,None),initialize=0)
m.b71 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b72 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b73 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b74 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b75 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b76 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b77 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b78 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b79 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b80 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b81 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b82 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b83 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b84 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b85 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b86 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b87 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b88 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b89 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b90 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b91 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b92 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b93 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b94 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b95 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b96 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b97 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b98 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b99 = Var(within=Binary,bounds=(0,1),initialize=0)
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

m.obj = Objective(expr=   10*m.x67 + m.x68 + 10*m.x69, sense=minimize)

m.c1 = Constraint(expr= - m.x1 - m.x2 - m.x3 + m.x15 + m.x16 + m.x17 + m.x65 == 0)

m.c2 = Constraint(expr= - m.x4 - m.x5 - m.x6 - m.x7 + m.x18 + m.x19 + m.x20 + m.x21 + m.x66 == 0)

m.c3 = Constraint(expr=   m.x1 + m.x4 - m.x8 - m.x9 - m.x10 - m.x11 - m.x15 - m.x18 + m.x22 + m.x23 + m.x24 + m.x25
                        == 1.212)

m.c4 = Constraint(expr=   m.x2 + m.x8 + m.x12 - m.x16 - m.x22 - m.x26 == 0.452)

m.c5 = Constraint(expr=   m.x9 - m.x12 + m.x13 - m.x23 + m.x26 - m.x27 == 0.245)

m.c6 = Constraint(expr=   m.x5 + m.x10 - m.x13 - m.x14 - m.x19 - m.x24 + m.x27 + m.x28 == 0.652)

m.c7 = Constraint(expr=   m.x6 + m.x14 - m.x20 - m.x28 == 0.252)

m.c8 = Constraint(expr=   m.x3 + m.x7 + m.x11 - m.x17 - m.x21 - m.x25 == 0.456)

m.c9 = Constraint(expr=   m.x29 - 38721.1970117411*m.b99 - 2543.8701482414*m.b100 - 207.747320703761*m.b101
                        - 23.9314504121258*m.b102 - 1.5722267648148*m.b103 - 0.181112645550961*m.b104
                        - 0.0390863672545667*m.b105 == 0)

m.c10 = Constraint(expr=   m.x30 - 32510.4890865135*m.b106 - 2135.84468132099*m.b107 - 174.425573683688*m.b108
                         - 20.0929521164322*m.b109 - 1.32004857865156*m.b110 - 0.152062982061963*m.b111
                         - 0.0328170876451919*m.b112 == 0)

m.c11 = Constraint(expr=   m.x31 - 63468.4628982673*m.b113 - 4169.69361956223*m.b114 - 340.521578201805*m.b115
                         - 39.2263796008983*m.b116 - 2.57705917665854*m.b117 - 0.296864304610023*m.b118
                         - 0.0640670186196026*m.b119 == 0)

m.c12 = Constraint(expr=   m.x32 - 50797.5773435889*m.b120 - 3337.25325093014*m.b121 - 272.539627020641*m.b122
                         - 31.3951994533022*m.b123 - 2.06257339263358*m.b124 - 0.237598120158509*m.b125
                         - 0.0512766370081929*m.b126 == 0)

m.c13 = Constraint(expr=   m.x33 - 59165.7349698592*m.b127 - 3887.01689524085*m.b128 - 317.436542928413*m.b129
                         - 36.5670992066393*m.b130 - 2.40235218067626*m.b131 - 0.27673893405488*m.b132
                         - 0.0597237127048799*m.b133 == 0)

m.c14 = Constraint(expr=   m.x34 - 32977.2294678044*m.b134 - 2166.50816836621*m.b135 - 176.929733450444*m.b136
                         - 20.3814187742893*m.b137 - 1.339*m.b138 - 0.154246090843839*m.b139 - 0.0332882297421199*m.b140
                         == 0)

m.c15 = Constraint(expr=   m.x35 - 33843.9321019273*m.b141 - 2223.4480134252*m.b142 - 181.579774357788*m.b143
                         - 20.9170801874496*m.b144 - 1.37419139860501*m.b145 - 0.158299963634093*m.b146
                         - 0.0341631060391402*m.b147 == 0)

m.c16 = Constraint(expr=   m.x36 - 31810.181054648*m.b148 - 2089.8364782095*m.b149 - 170.668274619734*m.b150
                         - 19.660130090483*m.b151 - 1.2916134290104*m.b152 - 0.148787395299671*m.b153
                         - 0.0321101751776739*m.b154 == 0)

m.c17 = Constraint(expr=   m.x37 - 39461.9459070343*m.b155 - 2592.53519858857*m.b156 - 211.721593458417*m.b157
                         - 24.3892667200816*m.b158 - 1.60230396616872*m.b159 - 0.184577388442944*m.b160
                         - 0.0398341019735132*m.b161 == 0)

m.c18 = Constraint(expr=   m.x38 - 32977.2294678044*m.b162 - 2166.50816836621*m.b163 - 176.929733450444*m.b164
                         - 20.3814187742893*m.b165 - 1.339*m.b166 - 0.154246090843839*m.b167 - 0.0332882297421199*m.b168
                         == 0)

m.c19 = Constraint(expr=   m.x39 - 52785.5148814787*m.b169 - 3467.85497167945*m.b170 - 283.205327698691*m.b171
                         - 32.6238347301504*m.b172 - 2.14329116080854*m.b173 - 0.246896402610059*m.b174
                         - 0.0532833223041444*m.b175 == 0)

m.c20 = Constraint(expr=   m.x40 - 30677.4142839491*m.b176 - 2015.41699236491*m.b177 - 164.590743970989*m.b178
                         - 18.9600290116536*m.b179 - 1.24561882211213*m.b180 - 0.143489047044288*m.b181
                         - 0.0309667255575633*m.b182 == 0)

m.c21 = Constraint(expr=   m.x41 - 28361.2795383154*m.b183 - 1863.25366856746*m.b184 - 152.164196629274*m.b185
                         - 17.5285530220005*m.b186 - 1.15157500841239*m.b187 - 0.132655670919396*m.b188
                         - 0.0286287479053886*m.b189 == 0)

m.c22 = Constraint(expr=   m.x42 - 50797.5773435889*m.b190 - 3337.25325093014*m.b191 - 272.539627020641*m.b192
                         - 31.3951994533022*m.b193 - 2.06257339263358*m.b194 - 0.237598120158509*m.b195
                         - 0.0512766370081929*m.b196 == 0)

m.c23 = Constraint(expr=-(m.x1 + m.x15)*(m.x1 - m.x15)*m.x29 + m.x43 - m.x45 - m.x51 == 0)

m.c24 = Constraint(expr=-(m.x2 + m.x16)*(m.x2 - m.x16)*m.x30 + m.x43 - m.x46 - m.x52 == 0)

m.c25 = Constraint(expr=-(m.x3 + m.x17)*(m.x3 - m.x17)*m.x31 + m.x43 - m.x50 - m.x53 == 0)

m.c26 = Constraint(expr=-(m.x4 + m.x18)*(m.x4 - m.x18)*m.x32 + m.x44 - m.x45 - m.x54 == 0)

m.c27 = Constraint(expr=-(m.x5 + m.x19)*(m.x5 - m.x19)*m.x33 + m.x44 - m.x48 - m.x55 == 0)

m.c28 = Constraint(expr=-(m.x6 + m.x20)*(m.x6 - m.x20)*m.x34 + m.x44 - m.x49 - m.x56 == 0)

m.c29 = Constraint(expr=-(m.x7 + m.x21)*(m.x7 - m.x21)*m.x35 + m.x44 - m.x50 - m.x57 == 0)

m.c30 = Constraint(expr=-(m.x8 + m.x22)*(m.x8 - m.x22)*m.x36 + m.x45 - m.x46 - m.x58 == 0)

m.c31 = Constraint(expr=-(m.x9 + m.x23)*(m.x9 - m.x23)*m.x37 + m.x45 - m.x47 - m.x59 == 0)

m.c32 = Constraint(expr=-(m.x10 + m.x24)*(m.x10 - m.x24)*m.x38 + m.x45 - m.x48 - m.x60 == 0)

m.c33 = Constraint(expr=-(m.x11 + m.x25)*(m.x11 - m.x25)*m.x39 + m.x45 - m.x50 - m.x61 == 0)

m.c34 = Constraint(expr=-(m.x12 + m.x26)*(m.x12 - m.x26)*m.x40 - m.x46 + m.x47 - m.x62 == 0)

m.c35 = Constraint(expr=-(m.x13 + m.x27)*(m.x13 - m.x27)*m.x41 - m.x47 + m.x48 - m.x63 == 0)

m.c36 = Constraint(expr=-(m.x14 + m.x28)*(m.x14 - m.x28)*m.x42 + m.x48 - m.x49 - m.x64 == 0)

m.c37 = Constraint(expr=   m.x51 + 12*m.b85 <= 12)

m.c38 = Constraint(expr=   m.x52 + 12*m.b86 <= 12)

m.c39 = Constraint(expr=   m.x53 + 12*m.b87 <= 12)

m.c40 = Constraint(expr=   m.x54 + 12*m.b88 <= 12)

m.c41 = Constraint(expr=   m.x55 + 12*m.b89 <= 12)

m.c42 = Constraint(expr=   m.x56 + 12*m.b90 <= 12)

m.c43 = Constraint(expr=   m.x57 + 12*m.b91 <= 12)

m.c44 = Constraint(expr=   m.x58 + 12*m.b92 <= 12)

m.c45 = Constraint(expr=   m.x59 + 12*m.b93 <= 12)

m.c46 = Constraint(expr=   m.x60 + 12*m.b94 <= 12)

m.c47 = Constraint(expr=   m.x61 + 12*m.b95 <= 12)

m.c48 = Constraint(expr=   m.x62 + 12*m.b96 <= 12)

m.c49 = Constraint(expr=   m.x63 + 12*m.b97 <= 12)

m.c50 = Constraint(expr=   m.x64 + 12*m.b98 <= 12)

m.c51 = Constraint(expr=   m.x51 - 12*m.b85 >= -12)

m.c52 = Constraint(expr=   m.x52 - 12*m.b86 >= -12)

m.c53 = Constraint(expr=   m.x53 - 12*m.b87 >= -12)

m.c54 = Constraint(expr=   m.x54 - 12*m.b88 >= -12)

m.c55 = Constraint(expr=   m.x55 - 12*m.b89 >= -12)

m.c56 = Constraint(expr=   m.x56 - 12*m.b90 >= -12)

m.c57 = Constraint(expr=   m.x57 - 12*m.b91 >= -12)

m.c58 = Constraint(expr=   m.x58 - 12*m.b92 >= -12)

m.c59 = Constraint(expr=   m.x59 - 12*m.b93 >= -12)

m.c60 = Constraint(expr=   m.x60 - 12*m.b94 >= -12)

m.c61 = Constraint(expr=   m.x61 - 12*m.b95 >= -12)

m.c62 = Constraint(expr=   m.x62 - 12*m.b96 >= -12)

m.c63 = Constraint(expr=   m.x63 - 12*m.b97 >= -12)

m.c64 = Constraint(expr=   m.x64 - 12*m.b98 >= -12)

m.c65 = Constraint(expr=-(1.02*m.x65*(-6.5 + m.x43) + 1.02*m.x66*(-3.25 + m.x44)) + m.x67 == 0)

m.c66 = Constraint(expr=   m.x68 - 9.11349113439539*m.b99 - 17.6144733325531*m.b100 - 32.2986551864818*m.b101
                         - 54.4931814987685*m.b102 - 105.323928905069*m.b103 - 177.698914733437*m.b104
                         - 257.546555368226*m.b105 - 7.65172765642961*m.b106 - 14.7891900880288*m.b107
                         - 27.118094428506*m.b108 - 45.7527173518919*m.b109 - 88.4304387640365*m.b110
                         - 149.196798497086*m.b111 - 216.237232413786*m.b112 - 14.9380525029139*m.b113
                         - 28.8721329260735*m.b114 - 52.941183552398*m.b115 - 89.3205462402005*m.b116
                         - 172.637944844116*m.b117 - 291.268810037089*m.b118 - 422.148209648796*m.b119
                         - 11.9558099050809*m.b120 - 23.1080813747994*m.b121 - 42.3719709499612*m.b122
                         - 71.4885338137291*m.b123 - 138.172392322055*m.b124 - 233.119713791557*m.b125
                         - 337.870264236031*m.b126 - 13.9253546563734*m.b127 - 26.9147996770731*m.b128
                         - 49.3521332015331*m.b129 - 83.2652237802191*m.b130 - 160.93427229773*m.b131
                         - 271.522775764452*m.b132 - 393.529446744536*m.b133 - 7.76158051882097*m.b134
                         - 15.0015127080393*m.b135 - 27.5074183079396*m.b136 - 46.4095712271164*m.b137 - 89.7*m.b138
                         - 151.338758602103*m.b139 - 219.341665817957*m.b140 - 7.96556922221359*m.b141
                         - 15.3957802311063*m.b142 - 28.2303641796868*m.b143 - 47.6293006671023*m.b144
                         - 92.0574820424717*m.b145 - 155.316221319321*m.b146 - 225.10637081608*m.b147
                         - 7.48690188831565*m.b148 - 14.4706163324673*m.b149 - 26.5339439013751*m.b150
                         - 44.7671586494086*m.b151 - 86.5255598074927*m.b152 - 145.982952158506*m.b153
                         - 211.579268940989*m.b154 - 9.28783513744935*m.b155 - 17.9514438466182*m.b156
                         - 32.916538800503*m.b157 - 55.5356535066454*m.b158 - 107.338809384118*m.b159
                         - 181.098351861986*m.b160 - 262.473503425068*m.b161 - 7.76158051882097*m.b162
                         - 15.0015127080393*m.b163 - 27.5074183079396*m.b164 - 46.4095712271164*m.b165 - 89.7*m.b166
                         - 151.338758602103*m.b167 - 219.341665817957*m.b168 - 12.4236944883441*m.b169
                         - 24.0124044704238*m.b170 - 44.0301766363479*m.b171 - 74.2862014846846*m.b172
                         - 143.579699122125*m.b173 - 242.242736071415*m.b174 - 351.092646411238*m.b175
                         - 7.22029184733547*m.b176 - 13.9553148538372*m.b177 - 25.5890649679471*m.b178
                         - 43.1729913716576*m.b179 - 83.44436769489*m.b180 - 140.784470672041*m.b181
                         - 204.044889780639*m.b182 - 6.67516217420068*m.b183 - 12.9016931463472*m.b184
                         - 23.6570989315674*m.b185 - 39.913444642481*m.b186 - 77.1443452237428*m.b187
                         - 130.155289178744*m.b188 - 188.639567333459*m.b189 - 11.9558099050809*m.b190
                         - 23.1080813747994*m.b191 - 42.3719709499612*m.b192 - 71.4885338137291*m.b193
                         - 138.172392322055*m.b194 - 233.119713791557*m.b195 - 337.870264236031*m.b196 == 0)

m.c67 = Constraint(expr= - 0.2*m.x65 - 0.17*m.x66 + m.x69 == 0)

m.c69 = Constraint(expr=   m.x1 - 2*m.b71 <= 0)

m.c70 = Constraint(expr=   m.x2 - 2*m.b72 <= 0)

m.c71 = Constraint(expr=   m.x3 - 2*m.b73 <= 0)

m.c72 = Constraint(expr=   m.x4 - 2*m.b74 <= 0)

m.c73 = Constraint(expr=   m.x5 - 2*m.b75 <= 0)

m.c74 = Constraint(expr=   m.x6 - 2*m.b76 <= 0)

m.c75 = Constraint(expr=   m.x7 - 2*m.b77 <= 0)

m.c76 = Constraint(expr=   m.x8 - 2*m.b78 <= 0)

m.c77 = Constraint(expr=   m.x9 - 2*m.b79 <= 0)

m.c78 = Constraint(expr=   m.x10 - 2*m.b80 <= 0)

m.c79 = Constraint(expr=   m.x11 - 2*m.b81 <= 0)

m.c80 = Constraint(expr=   m.x12 - 2*m.b82 <= 0)

m.c81 = Constraint(expr=   m.x13 - 2*m.b83 <= 0)

m.c82 = Constraint(expr=   m.x14 - 2*m.b84 <= 0)

m.c83 = Constraint(expr=   m.x15 + 2*m.b71 <= 2)

m.c84 = Constraint(expr=   m.x16 + 2*m.b72 <= 2)

m.c85 = Constraint(expr=   m.x17 + 2*m.b73 <= 2)

m.c86 = Constraint(expr=   m.x18 + 2*m.b74 <= 2)

m.c87 = Constraint(expr=   m.x19 + 2*m.b75 <= 2)

m.c88 = Constraint(expr=   m.x20 + 2*m.b76 <= 2)

m.c89 = Constraint(expr=   m.x21 + 2*m.b77 <= 2)

m.c90 = Constraint(expr=   m.x22 + 2*m.b78 <= 2)

m.c91 = Constraint(expr=   m.x23 + 2*m.b79 <= 2)

m.c92 = Constraint(expr=   m.x24 + 2*m.b80 <= 2)

m.c93 = Constraint(expr=   m.x25 + 2*m.b81 <= 2)

m.c94 = Constraint(expr=   m.x26 + 2*m.b82 <= 2)

m.c95 = Constraint(expr=   m.x27 + 2*m.b83 <= 2)

m.c96 = Constraint(expr=   m.x28 + 2*m.b84 <= 2)

m.c97 = Constraint(expr=   m.x1 + m.x15 - 2*m.b85 <= 0)

m.c98 = Constraint(expr=   m.x2 + m.x16 - 2*m.b86 <= 0)

m.c99 = Constraint(expr=   m.x3 + m.x17 - 2*m.b87 <= 0)

m.c100 = Constraint(expr=   m.x4 + m.x18 - 2*m.b88 <= 0)

m.c101 = Constraint(expr=   m.x5 + m.x19 - 2*m.b89 <= 0)

m.c102 = Constraint(expr=   m.x6 + m.x20 - 2*m.b90 <= 0)

m.c103 = Constraint(expr=   m.x7 + m.x21 - 2*m.b91 <= 0)

m.c104 = Constraint(expr=   m.x8 + m.x22 - 2*m.b92 <= 0)

m.c105 = Constraint(expr=   m.x9 + m.x23 - 2*m.b93 <= 0)

m.c106 = Constraint(expr=   m.x10 + m.x24 - 2*m.b94 <= 0)

m.c107 = Constraint(expr=   m.x11 + m.x25 - 2*m.b95 <= 0)

m.c108 = Constraint(expr=   m.x12 + m.x26 - 2*m.b96 <= 0)

m.c109 = Constraint(expr=   m.x13 + m.x27 - 2*m.b97 <= 0)

m.c110 = Constraint(expr=   m.x14 + m.x28 - 2*m.b98 <= 0)

m.c111 = Constraint(expr= - m.b85 + m.b99 + m.b100 + m.b101 + m.b102 + m.b103 + m.b104 + m.b105 == 0)

m.c112 = Constraint(expr= - m.b86 + m.b106 + m.b107 + m.b108 + m.b109 + m.b110 + m.b111 + m.b112 == 0)

m.c113 = Constraint(expr= - m.b87 + m.b113 + m.b114 + m.b115 + m.b116 + m.b117 + m.b118 + m.b119 == 0)

m.c114 = Constraint(expr= - m.b88 + m.b120 + m.b121 + m.b122 + m.b123 + m.b124 + m.b125 + m.b126 == 0)

m.c115 = Constraint(expr= - m.b89 + m.b127 + m.b128 + m.b129 + m.b130 + m.b131 + m.b132 + m.b133 == 0)

m.c116 = Constraint(expr= - m.b90 + m.b134 + m.b135 + m.b136 + m.b137 + m.b138 + m.b139 + m.b140 == 0)

m.c117 = Constraint(expr= - m.b91 + m.b141 + m.b142 + m.b143 + m.b144 + m.b145 + m.b146 + m.b147 == 0)

m.c118 = Constraint(expr= - m.b92 + m.b148 + m.b149 + m.b150 + m.b151 + m.b152 + m.b153 + m.b154 == 0)

m.c119 = Constraint(expr= - m.b93 + m.b155 + m.b156 + m.b157 + m.b158 + m.b159 + m.b160 + m.b161 == 0)

m.c120 = Constraint(expr= - m.b94 + m.b162 + m.b163 + m.b164 + m.b165 + m.b166 + m.b167 + m.b168 == 0)

m.c121 = Constraint(expr= - m.b95 + m.b169 + m.b170 + m.b171 + m.b172 + m.b173 + m.b174 + m.b175 == 0)

m.c122 = Constraint(expr= - m.b96 + m.b176 + m.b177 + m.b178 + m.b179 + m.b180 + m.b181 + m.b182 == 0)

m.c123 = Constraint(expr= - m.b97 + m.b183 + m.b184 + m.b185 + m.b186 + m.b187 + m.b188 + m.b189 == 0)

m.c124 = Constraint(expr= - m.b98 + m.b190 + m.b191 + m.b192 + m.b193 + m.b194 + m.b195 + m.b196 == 0)

m.c125 = Constraint(expr=   m.x1 + m.x15 - 0.0176041976445841*m.b99 - 0.0686820348432157*m.b100
                          - 0.240338257044582*m.b101 - 0.708118780382974*m.b102 - 2*m.b103 - 2*m.b104 - 2*m.b105 <= 0)

m.c126 = Constraint(expr=   m.x2 + m.x16 - 0.0192122784105588*m.b106 - 0.0749558941482069*m.b107
                          - 0.262292300976835*m.b108 - 0.772802909347502*m.b109 - 2*m.b110 - 2*m.b111 - 2*m.b112 <= 0)

m.c127 = Constraint(expr=   m.x3 + m.x17 - 0.0137502828767635*m.b113 - 0.0536461488738445*m.b114
                          - 0.187723353667753*m.b115 - 0.553097263345606*m.b116 - 2*m.b117 - 2*m.b118 - 2*m.b119 <= 0)

m.c128 = Constraint(expr=   m.x4 + m.x18 - 0.0153698320860398*m.b120 - 0.0599647518268192*m.b121
                          - 0.209833968534382*m.b122 - 0.618242703881818*m.b123 - 2*m.b124 - 2*m.b125 - 2*m.b126 <= 0)

m.c129 = Constraint(expr=   m.x5 + m.x19 - 0.0142414920290718*m.b127 - 0.0555625806701283*m.b128
                          - 0.194429501479406*m.b129 - 0.572855870518057*m.b130 - 2*m.b131 - 2*m.b132 - 2*m.b133 <= 0)

m.c130 = Constraint(expr=   m.x6 + m.x20 - 0.0190758342372385*m.b134 - 0.0744235629590588*m.b135
                          - 0.260429520550158*m.b136 - 0.767314520523847*m.b137 - 2*m.b138 - 2*m.b139 - 2*m.b140 <= 0)

m.c131 = Constraint(expr=   m.x7 + m.x21 - 0.0188299954674205*m.b141 - 0.0734644333642121*m.b142
                          - 0.257073249355929*m.b143 - 0.757425796631457*m.b144 - 2*m.b145 - 2*m.b146 - 2*m.b147 <= 0)

m.c132 = Constraint(expr=   m.x8 + m.x22 - 0.0194226083350049*m.b148 - 0.0757764874800376*m.b149
                          - 0.265163793814297*m.b150 - 0.781263310246409*m.b151 - 2*m.b152 - 2*m.b153 - 2*m.b154 <= 0)

m.c133 = Constraint(expr=   m.x9 + m.x23 - 0.0174381887671401*m.b155 - 0.0680343582075014*m.b156
                          - 0.238071849619242*m.b157 - 0.701441168247406*m.b158 - 2*m.b159 - 2*m.b160 - 2*m.b161 <= 0)

m.c134 = Constraint(expr=   m.x10 + m.x24 - 0.0190758342372385*m.b162 - 0.0744235629590588*m.b163
                          - 0.260429520550158*m.b164 - 0.767314520523847*m.b165 - 2*m.b166 - 2*m.b167 - 2*m.b168 <= 0)

m.c135 = Constraint(expr=   m.x11 + m.x25 - 0.0150776355652448*m.b169 - 0.0588247594211735*m.b170
                          - 0.205844806180028*m.b171 - 0.606489265973719*m.b172 - 2*m.b173 - 2*m.b174 - 2*m.b175 <= 0)

m.c136 = Constraint(expr=   m.x12 + m.x26 - 0.0197779487583483*m.b176 - 0.0771628331590627*m.b177
                          - 0.270015017353593*m.b178 - 0.795556675515238*m.b179 - 2*m.b180 - 2*m.b181 - 2*m.b182 <= 0)

m.c137 = Constraint(expr=   m.x13 + m.x27 - 0.02056968839856*m.b183 - 0.0802517719822704*m.b184
                          - 0.280824105561038*m.b185 - 0.827403949655566*m.b186 - 2*m.b187 - 2*m.b188 - 2*m.b189 <= 0)

m.c138 = Constraint(expr=   m.x14 + m.x28 - 0.0153698320860398*m.b190 - 0.0599647518268192*m.b191
                          - 0.209833968534382*m.b192 - 0.618242703881818*m.b193 - 2*m.b194 - 2*m.b195 - 2*m.b196 <= 0)
