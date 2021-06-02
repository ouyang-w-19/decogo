#  MINLP written by GAMS Convert at 04/21/18 13:55:06
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        138       54       14       70        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        196       70       28        0       98        0        0        0
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
m.s1s99 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s100 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s101 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s102 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s103 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s104 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s105 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s106 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s107 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s108 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s109 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s110 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s111 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s112 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s113 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s114 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s115 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s116 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s117 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s118 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s119 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s120 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s121 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s122 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s123 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s124 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s125 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s126 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s127 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s128 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s129 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s130 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s131 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s132 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s133 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s134 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s135 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s136 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s137 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s138 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s139 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s140 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s141 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s142 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s143 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s144 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s145 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s146 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s147 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s148 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s149 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s150 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s151 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s152 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s153 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s154 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s155 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s156 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s157 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s158 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s159 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s160 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s161 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s162 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s163 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s164 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s165 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s166 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s167 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s168 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s169 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s170 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s171 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s172 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s173 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s174 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s175 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s176 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s177 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s178 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s179 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s180 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s181 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s182 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s183 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s184 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s185 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s186 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s187 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s188 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s189 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s190 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s191 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s192 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s193 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s194 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s195 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)
m.s1s196 = Var(within=CannotHandle,bounds=(0,None),initialize=0.142857142857143)

suffix sosno integer IN;
suffix ref integer IN;
let m.s1s99.sosno := 1;
let m.s1s99.ref   := 1;
let m.s1s100.sosno := 1;
let m.s1s100.ref   := 2;
let m.s1s101.sosno := 1;
let m.s1s101.ref   := 3;
let m.s1s102.sosno := 1;
let m.s1s102.ref   := 4;
let m.s1s103.sosno := 1;
let m.s1s103.ref   := 5;
let m.s1s104.sosno := 1;
let m.s1s104.ref   := 6;
let m.s1s105.sosno := 1;
let m.s1s105.ref   := 7;
let m.s1s106.sosno := 2;
let m.s1s106.ref   := 1;
let m.s1s107.sosno := 2;
let m.s1s107.ref   := 2;
let m.s1s108.sosno := 2;
let m.s1s108.ref   := 3;
let m.s1s109.sosno := 2;
let m.s1s109.ref   := 4;
let m.s1s110.sosno := 2;
let m.s1s110.ref   := 5;
let m.s1s111.sosno := 2;
let m.s1s111.ref   := 6;
let m.s1s112.sosno := 2;
let m.s1s112.ref   := 7;
let m.s1s113.sosno := 3;
let m.s1s113.ref   := 1;
let m.s1s114.sosno := 3;
let m.s1s114.ref   := 2;
let m.s1s115.sosno := 3;
let m.s1s115.ref   := 3;
let m.s1s116.sosno := 3;
let m.s1s116.ref   := 4;
let m.s1s117.sosno := 3;
let m.s1s117.ref   := 5;
let m.s1s118.sosno := 3;
let m.s1s118.ref   := 6;
let m.s1s119.sosno := 3;
let m.s1s119.ref   := 7;
let m.s1s120.sosno := 4;
let m.s1s120.ref   := 1;
let m.s1s121.sosno := 4;
let m.s1s121.ref   := 2;
let m.s1s122.sosno := 4;
let m.s1s122.ref   := 3;
let m.s1s123.sosno := 4;
let m.s1s123.ref   := 4;
let m.s1s124.sosno := 4;
let m.s1s124.ref   := 5;
let m.s1s125.sosno := 4;
let m.s1s125.ref   := 6;
let m.s1s126.sosno := 4;
let m.s1s126.ref   := 7;
let m.s1s127.sosno := 5;
let m.s1s127.ref   := 1;
let m.s1s128.sosno := 5;
let m.s1s128.ref   := 2;
let m.s1s129.sosno := 5;
let m.s1s129.ref   := 3;
let m.s1s130.sosno := 5;
let m.s1s130.ref   := 4;
let m.s1s131.sosno := 5;
let m.s1s131.ref   := 5;
let m.s1s132.sosno := 5;
let m.s1s132.ref   := 6;
let m.s1s133.sosno := 5;
let m.s1s133.ref   := 7;
let m.s1s134.sosno := 6;
let m.s1s134.ref   := 1;
let m.s1s135.sosno := 6;
let m.s1s135.ref   := 2;
let m.s1s136.sosno := 6;
let m.s1s136.ref   := 3;
let m.s1s137.sosno := 6;
let m.s1s137.ref   := 4;
let m.s1s138.sosno := 6;
let m.s1s138.ref   := 5;
let m.s1s139.sosno := 6;
let m.s1s139.ref   := 6;
let m.s1s140.sosno := 6;
let m.s1s140.ref   := 7;
let m.s1s141.sosno := 7;
let m.s1s141.ref   := 1;
let m.s1s142.sosno := 7;
let m.s1s142.ref   := 2;
let m.s1s143.sosno := 7;
let m.s1s143.ref   := 3;
let m.s1s144.sosno := 7;
let m.s1s144.ref   := 4;
let m.s1s145.sosno := 7;
let m.s1s145.ref   := 5;
let m.s1s146.sosno := 7;
let m.s1s146.ref   := 6;
let m.s1s147.sosno := 7;
let m.s1s147.ref   := 7;
let m.s1s148.sosno := 8;
let m.s1s148.ref   := 1;
let m.s1s149.sosno := 8;
let m.s1s149.ref   := 2;
let m.s1s150.sosno := 8;
let m.s1s150.ref   := 3;
let m.s1s151.sosno := 8;
let m.s1s151.ref   := 4;
let m.s1s152.sosno := 8;
let m.s1s152.ref   := 5;
let m.s1s153.sosno := 8;
let m.s1s153.ref   := 6;
let m.s1s154.sosno := 8;
let m.s1s154.ref   := 7;
let m.s1s155.sosno := 9;
let m.s1s155.ref   := 1;
let m.s1s156.sosno := 9;
let m.s1s156.ref   := 2;
let m.s1s157.sosno := 9;
let m.s1s157.ref   := 3;
let m.s1s158.sosno := 9;
let m.s1s158.ref   := 4;
let m.s1s159.sosno := 9;
let m.s1s159.ref   := 5;
let m.s1s160.sosno := 9;
let m.s1s160.ref   := 6;
let m.s1s161.sosno := 9;
let m.s1s161.ref   := 7;
let m.s1s162.sosno := 10;
let m.s1s162.ref   := 1;
let m.s1s163.sosno := 10;
let m.s1s163.ref   := 2;
let m.s1s164.sosno := 10;
let m.s1s164.ref   := 3;
let m.s1s165.sosno := 10;
let m.s1s165.ref   := 4;
let m.s1s166.sosno := 10;
let m.s1s166.ref   := 5;
let m.s1s167.sosno := 10;
let m.s1s167.ref   := 6;
let m.s1s168.sosno := 10;
let m.s1s168.ref   := 7;
let m.s1s169.sosno := 11;
let m.s1s169.ref   := 1;
let m.s1s170.sosno := 11;
let m.s1s170.ref   := 2;
let m.s1s171.sosno := 11;
let m.s1s171.ref   := 3;
let m.s1s172.sosno := 11;
let m.s1s172.ref   := 4;
let m.s1s173.sosno := 11;
let m.s1s173.ref   := 5;
let m.s1s174.sosno := 11;
let m.s1s174.ref   := 6;
let m.s1s175.sosno := 11;
let m.s1s175.ref   := 7;
let m.s1s176.sosno := 12;
let m.s1s176.ref   := 1;
let m.s1s177.sosno := 12;
let m.s1s177.ref   := 2;
let m.s1s178.sosno := 12;
let m.s1s178.ref   := 3;
let m.s1s179.sosno := 12;
let m.s1s179.ref   := 4;
let m.s1s180.sosno := 12;
let m.s1s180.ref   := 5;
let m.s1s181.sosno := 12;
let m.s1s181.ref   := 6;
let m.s1s182.sosno := 12;
let m.s1s182.ref   := 7;
let m.s1s183.sosno := 13;
let m.s1s183.ref   := 1;
let m.s1s184.sosno := 13;
let m.s1s184.ref   := 2;
let m.s1s185.sosno := 13;
let m.s1s185.ref   := 3;
let m.s1s186.sosno := 13;
let m.s1s186.ref   := 4;
let m.s1s187.sosno := 13;
let m.s1s187.ref   := 5;
let m.s1s188.sosno := 13;
let m.s1s188.ref   := 6;
let m.s1s189.sosno := 13;
let m.s1s189.ref   := 7;
let m.s1s190.sosno := 14;
let m.s1s190.ref   := 1;
let m.s1s191.sosno := 14;
let m.s1s191.ref   := 2;
let m.s1s192.sosno := 14;
let m.s1s192.ref   := 3;
let m.s1s193.sosno := 14;
let m.s1s193.ref   := 4;
let m.s1s194.sosno := 14;
let m.s1s194.ref   := 5;
let m.s1s195.sosno := 14;
let m.s1s195.ref   := 6;
let m.s1s196.sosno := 14;
let m.s1s196.ref   := 7;

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

m.c9 = Constraint(expr=   m.x29 - 38721.1970117411*m.s1s99 - 2543.8701482414*m.s1s100 - 207.747320703761*m.s1s101
                        - 23.9314504121258*m.s1s102 - 1.5722267648148*m.s1s103 - 0.181112645550961*m.s1s104
                        - 0.0390863672545667*m.s1s105 == 0)

m.c10 = Constraint(expr=   m.x30 - 32510.4890865135*m.s1s106 - 2135.84468132099*m.s1s107 - 174.425573683688*m.s1s108
                         - 20.0929521164322*m.s1s109 - 1.32004857865156*m.s1s110 - 0.152062982061963*m.s1s111
                         - 0.0328170876451919*m.s1s112 == 0)

m.c11 = Constraint(expr=   m.x31 - 63468.4628982673*m.s1s113 - 4169.69361956223*m.s1s114 - 340.521578201805*m.s1s115
                         - 39.2263796008983*m.s1s116 - 2.57705917665854*m.s1s117 - 0.296864304610023*m.s1s118
                         - 0.0640670186196026*m.s1s119 == 0)

m.c12 = Constraint(expr=   m.x32 - 50797.5773435889*m.s1s120 - 3337.25325093014*m.s1s121 - 272.539627020641*m.s1s122
                         - 31.3951994533022*m.s1s123 - 2.06257339263358*m.s1s124 - 0.237598120158509*m.s1s125
                         - 0.0512766370081929*m.s1s126 == 0)

m.c13 = Constraint(expr=   m.x33 - 59165.7349698592*m.s1s127 - 3887.01689524085*m.s1s128 - 317.436542928413*m.s1s129
                         - 36.5670992066393*m.s1s130 - 2.40235218067626*m.s1s131 - 0.27673893405488*m.s1s132
                         - 0.0597237127048799*m.s1s133 == 0)

m.c14 = Constraint(expr=   m.x34 - 32977.2294678044*m.s1s134 - 2166.50816836621*m.s1s135 - 176.929733450444*m.s1s136
                         - 20.3814187742893*m.s1s137 - 1.339*m.s1s138 - 0.154246090843839*m.s1s139
                         - 0.0332882297421199*m.s1s140 == 0)

m.c15 = Constraint(expr=   m.x35 - 33843.9321019273*m.s1s141 - 2223.4480134252*m.s1s142 - 181.579774357788*m.s1s143
                         - 20.9170801874496*m.s1s144 - 1.37419139860501*m.s1s145 - 0.158299963634093*m.s1s146
                         - 0.0341631060391402*m.s1s147 == 0)

m.c16 = Constraint(expr=   m.x36 - 31810.181054648*m.s1s148 - 2089.8364782095*m.s1s149 - 170.668274619734*m.s1s150
                         - 19.660130090483*m.s1s151 - 1.2916134290104*m.s1s152 - 0.148787395299671*m.s1s153
                         - 0.0321101751776739*m.s1s154 == 0)

m.c17 = Constraint(expr=   m.x37 - 39461.9459070343*m.s1s155 - 2592.53519858857*m.s1s156 - 211.721593458417*m.s1s157
                         - 24.3892667200816*m.s1s158 - 1.60230396616872*m.s1s159 - 0.184577388442944*m.s1s160
                         - 0.0398341019735132*m.s1s161 == 0)

m.c18 = Constraint(expr=   m.x38 - 32977.2294678044*m.s1s162 - 2166.50816836621*m.s1s163 - 176.929733450444*m.s1s164
                         - 20.3814187742893*m.s1s165 - 1.339*m.s1s166 - 0.154246090843839*m.s1s167
                         - 0.0332882297421199*m.s1s168 == 0)

m.c19 = Constraint(expr=   m.x39 - 52785.5148814787*m.s1s169 - 3467.85497167945*m.s1s170 - 283.205327698691*m.s1s171
                         - 32.6238347301504*m.s1s172 - 2.14329116080854*m.s1s173 - 0.246896402610059*m.s1s174
                         - 0.0532833223041444*m.s1s175 == 0)

m.c20 = Constraint(expr=   m.x40 - 30677.4142839491*m.s1s176 - 2015.41699236491*m.s1s177 - 164.590743970989*m.s1s178
                         - 18.9600290116536*m.s1s179 - 1.24561882211213*m.s1s180 - 0.143489047044288*m.s1s181
                         - 0.0309667255575633*m.s1s182 == 0)

m.c21 = Constraint(expr=   m.x41 - 28361.2795383154*m.s1s183 - 1863.25366856746*m.s1s184 - 152.164196629274*m.s1s185
                         - 17.5285530220005*m.s1s186 - 1.15157500841239*m.s1s187 - 0.132655670919396*m.s1s188
                         - 0.0286287479053886*m.s1s189 == 0)

m.c22 = Constraint(expr=   m.x42 - 50797.5773435889*m.s1s190 - 3337.25325093014*m.s1s191 - 272.539627020641*m.s1s192
                         - 31.3951994533022*m.s1s193 - 2.06257339263358*m.s1s194 - 0.237598120158509*m.s1s195
                         - 0.0512766370081929*m.s1s196 == 0)

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

m.c66 = Constraint(expr=   m.x68 - 9.11349113439539*m.s1s99 - 17.6144733325531*m.s1s100 - 32.2986551864818*m.s1s101
                         - 54.4931814987685*m.s1s102 - 105.323928905069*m.s1s103 - 177.698914733437*m.s1s104
                         - 257.546555368226*m.s1s105 - 7.65172765642961*m.s1s106 - 14.7891900880288*m.s1s107
                         - 27.118094428506*m.s1s108 - 45.7527173518919*m.s1s109 - 88.4304387640365*m.s1s110
                         - 149.196798497086*m.s1s111 - 216.237232413786*m.s1s112 - 14.9380525029139*m.s1s113
                         - 28.8721329260735*m.s1s114 - 52.941183552398*m.s1s115 - 89.3205462402005*m.s1s116
                         - 172.637944844116*m.s1s117 - 291.268810037089*m.s1s118 - 422.148209648796*m.s1s119
                         - 11.9558099050809*m.s1s120 - 23.1080813747994*m.s1s121 - 42.3719709499612*m.s1s122
                         - 71.4885338137291*m.s1s123 - 138.172392322055*m.s1s124 - 233.119713791557*m.s1s125
                         - 337.870264236031*m.s1s126 - 13.9253546563734*m.s1s127 - 26.9147996770731*m.s1s128
                         - 49.3521332015331*m.s1s129 - 83.2652237802191*m.s1s130 - 160.93427229773*m.s1s131
                         - 271.522775764452*m.s1s132 - 393.529446744536*m.s1s133 - 7.76158051882097*m.s1s134
                         - 15.0015127080393*m.s1s135 - 27.5074183079396*m.s1s136 - 46.4095712271164*m.s1s137
                         - 89.7*m.s1s138 - 151.338758602103*m.s1s139 - 219.341665817957*m.s1s140
                         - 7.96556922221359*m.s1s141 - 15.3957802311063*m.s1s142 - 28.2303641796868*m.s1s143
                         - 47.6293006671023*m.s1s144 - 92.0574820424717*m.s1s145 - 155.316221319321*m.s1s146
                         - 225.10637081608*m.s1s147 - 7.48690188831565*m.s1s148 - 14.4706163324673*m.s1s149
                         - 26.5339439013751*m.s1s150 - 44.7671586494086*m.s1s151 - 86.5255598074927*m.s1s152
                         - 145.982952158506*m.s1s153 - 211.579268940989*m.s1s154 - 9.28783513744935*m.s1s155
                         - 17.9514438466182*m.s1s156 - 32.916538800503*m.s1s157 - 55.5356535066454*m.s1s158
                         - 107.338809384118*m.s1s159 - 181.098351861986*m.s1s160 - 262.473503425068*m.s1s161
                         - 7.76158051882097*m.s1s162 - 15.0015127080393*m.s1s163 - 27.5074183079396*m.s1s164
                         - 46.4095712271164*m.s1s165 - 89.7*m.s1s166 - 151.338758602103*m.s1s167
                         - 219.341665817957*m.s1s168 - 12.4236944883441*m.s1s169 - 24.0124044704238*m.s1s170
                         - 44.0301766363479*m.s1s171 - 74.2862014846846*m.s1s172 - 143.579699122125*m.s1s173
                         - 242.242736071415*m.s1s174 - 351.092646411238*m.s1s175 - 7.22029184733547*m.s1s176
                         - 13.9553148538372*m.s1s177 - 25.5890649679471*m.s1s178 - 43.1729913716576*m.s1s179
                         - 83.44436769489*m.s1s180 - 140.784470672041*m.s1s181 - 204.044889780639*m.s1s182
                         - 6.67516217420068*m.s1s183 - 12.9016931463472*m.s1s184 - 23.6570989315674*m.s1s185
                         - 39.913444642481*m.s1s186 - 77.1443452237428*m.s1s187 - 130.155289178744*m.s1s188
                         - 188.639567333459*m.s1s189 - 11.9558099050809*m.s1s190 - 23.1080813747994*m.s1s191
                         - 42.3719709499612*m.s1s192 - 71.4885338137291*m.s1s193 - 138.172392322055*m.s1s194
                         - 233.119713791557*m.s1s195 - 337.870264236031*m.s1s196 == 0)

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

m.c111 = Constraint(expr= - m.b85 + m.s1s99 + m.s1s100 + m.s1s101 + m.s1s102 + m.s1s103 + m.s1s104 + m.s1s105 == 0)

m.c112 = Constraint(expr= - m.b86 + m.s1s106 + m.s1s107 + m.s1s108 + m.s1s109 + m.s1s110 + m.s1s111 + m.s1s112 == 0)

m.c113 = Constraint(expr= - m.b87 + m.s1s113 + m.s1s114 + m.s1s115 + m.s1s116 + m.s1s117 + m.s1s118 + m.s1s119 == 0)

m.c114 = Constraint(expr= - m.b88 + m.s1s120 + m.s1s121 + m.s1s122 + m.s1s123 + m.s1s124 + m.s1s125 + m.s1s126 == 0)

m.c115 = Constraint(expr= - m.b89 + m.s1s127 + m.s1s128 + m.s1s129 + m.s1s130 + m.s1s131 + m.s1s132 + m.s1s133 == 0)

m.c116 = Constraint(expr= - m.b90 + m.s1s134 + m.s1s135 + m.s1s136 + m.s1s137 + m.s1s138 + m.s1s139 + m.s1s140 == 0)

m.c117 = Constraint(expr= - m.b91 + m.s1s141 + m.s1s142 + m.s1s143 + m.s1s144 + m.s1s145 + m.s1s146 + m.s1s147 == 0)

m.c118 = Constraint(expr= - m.b92 + m.s1s148 + m.s1s149 + m.s1s150 + m.s1s151 + m.s1s152 + m.s1s153 + m.s1s154 == 0)

m.c119 = Constraint(expr= - m.b93 + m.s1s155 + m.s1s156 + m.s1s157 + m.s1s158 + m.s1s159 + m.s1s160 + m.s1s161 == 0)

m.c120 = Constraint(expr= - m.b94 + m.s1s162 + m.s1s163 + m.s1s164 + m.s1s165 + m.s1s166 + m.s1s167 + m.s1s168 == 0)

m.c121 = Constraint(expr= - m.b95 + m.s1s169 + m.s1s170 + m.s1s171 + m.s1s172 + m.s1s173 + m.s1s174 + m.s1s175 == 0)

m.c122 = Constraint(expr= - m.b96 + m.s1s176 + m.s1s177 + m.s1s178 + m.s1s179 + m.s1s180 + m.s1s181 + m.s1s182 == 0)

m.c123 = Constraint(expr= - m.b97 + m.s1s183 + m.s1s184 + m.s1s185 + m.s1s186 + m.s1s187 + m.s1s188 + m.s1s189 == 0)

m.c124 = Constraint(expr= - m.b98 + m.s1s190 + m.s1s191 + m.s1s192 + m.s1s193 + m.s1s194 + m.s1s195 + m.s1s196 == 0)

m.c125 = Constraint(expr=   m.x1 + m.x15 - 0.0176041976445841*m.s1s99 - 0.0686820348432157*m.s1s100
                          - 0.240338257044582*m.s1s101 - 0.708118780382974*m.s1s102 - 2.76269556439349*m.s1s103
                          - 8.13984688781727*m.s1s104 - 17.521769741878*m.s1s105 <= 0)

m.c126 = Constraint(expr=   m.x2 + m.x16 - 0.0192122784105588*m.s1s106 - 0.0749558941482069*m.s1s107
                          - 0.262292300976835*m.s1s108 - 0.772802909347502*m.s1s109 - 3.01505796619323*m.s1s110
                          - 8.88339291488115*m.s1s111 - 19.1223210124677*m.s1s112 <= 0)

m.c127 = Constraint(expr=   m.x3 + m.x17 - 0.0137502828767635*m.s1s113 - 0.0536461488738445*m.s1s114
                          - 0.187723353667753*m.s1s115 - 0.553097263345606*m.s1s116 - 2.15788565203237*m.s1s117
                          - 6.35786984108667*m.s1s118 - 13.6859001084016*m.s1s119 <= 0)

m.c128 = Constraint(expr=   m.x4 + m.x18 - 0.0153698320860398*m.s1s120 - 0.0599647518268192*m.s1s121
                          - 0.209833968534382*m.s1s122 - 0.618242703881818*m.s1s123 - 2.41204784147821*m.s1s124
                          - 7.10671865867823*m.s1s125 - 15.297866123752*m.s1s126 <= 0)

m.c129 = Constraint(expr=   m.x5 + m.x19 - 0.0142414920290718*m.s1s127 - 0.0555625806701283*m.s1s128
                          - 0.194429501479406*m.s1s129 - 0.572855870518057*m.s1s130 - 2.23497302480958*m.s1s131
                          - 6.58499563065165*m.s1s132 - 14.1748092785675*m.s1s133 <= 0)

m.c130 = Constraint(expr=   m.x6 + m.x20 - 0.0190758342372385*m.s1s134 - 0.0744235629590588*m.s1s135
                          - 0.260429520550158*m.s1s136 - 0.767314520523847*m.s1s137 - 2.99364524861134*m.s1s138
                          - 8.82030371865732*m.s1s139 - 18.9865157099025*m.s1s140 <= 0)

m.c131 = Constraint(expr=   m.x7 + m.x21 - 0.0188299954674205*m.s1s141 - 0.0734644333642121*m.s1s142
                          - 0.257073249355929*m.s1s143 - 0.757425796631457*m.s1s144 - 2.95506480929543*m.s1s145
                          - 8.70663253716935*m.s1s146 - 18.7418280277177*m.s1s147 <= 0)

m.c132 = Constraint(expr=   m.x8 + m.x22 - 0.0194226083350049*m.s1s148 - 0.0757764874800376*m.s1s149
                          - 0.265163793814297*m.s1s150 - 0.781263310246409*m.s1s151 - 3.04806586357418*m.s1s152
                          - 8.98064548017735*m.s1s153 - 19.3316661118795*m.s1s154 <= 0)

m.c133 = Constraint(expr=   m.x9 + m.x23 - 0.0174381887671401*m.s1s155 - 0.0680343582075014*m.s1s156
                          - 0.238071849619242*m.s1s157 - 0.701441168247406*m.s1s158 - 2.73664314220282*m.s1s159
                          - 8.06308753350335*m.s1s160 - 17.3565381656137*m.s1s161 <= 0)

m.c134 = Constraint(expr=   m.x10 + m.x24 - 0.0190758342372385*m.s1s162 - 0.0744235629590588*m.s1s163
                          - 0.260429520550158*m.s1s164 - 0.767314520523847*m.s1s165 - 2.99364524861134*m.s1s166
                          - 8.82030371865732*m.s1s167 - 18.9865157099025*m.s1s168 <= 0)

m.c135 = Constraint(expr=   m.x11 + m.x25 - 0.0150776355652448*m.s1s169 - 0.0588247594211735*m.s1s170
                          - 0.205844806180028*m.s1s171 - 0.606489265973719*m.s1s172 - 2.36619229905421*m.s1s173
                          - 6.97161253294371*m.s1s174 - 15.0070377508768*m.s1s175 <= 0)

m.c136 = Constraint(expr=   m.x12 + m.x26 - 0.0197779487583483*m.s1s176 - 0.0771628331590627*m.s1s177
                          - 0.270015017353593*m.s1s178 - 0.795556675515238*m.s1s179 - 3.10383082550202*m.s1s180
                          - 9.14494814806731*m.s1s181 - 19.6853427294401*m.s1s182 <= 0)

m.c137 = Constraint(expr=   m.x13 + m.x27 - 0.02056968839856*m.s1s183 - 0.0802517719822704*m.s1s184
                          - 0.280824105561038*m.s1s185 - 0.827403949655566*m.s1s186 - 3.22808162274528*m.s1s187
                          - 9.5110335315907*m.s1s188 - 20.4733752175652*m.s1s189 <= 0)

m.c138 = Constraint(expr=   m.x14 + m.x28 - 0.0153698320860398*m.s1s190 - 0.0599647518268192*m.s1s191
                          - 0.209833968534382*m.s1s192 - 0.618242703881818*m.s1s193 - 2.41204784147821*m.s1s194
                          - 7.10671865867823*m.s1s195 - 15.297866123752*m.s1s196 <= 0)
