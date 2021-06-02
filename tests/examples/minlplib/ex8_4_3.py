#  NLP written by GAMS Convert at 04/21/18 13:51:47
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         26       26        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         53       53        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        151       51      100        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(-0.387,0.613),initialize=-0.215252868)
m.x2 = Var(within=Reals,bounds=(1.351,2.351),initialize=2.194266708)
m.x3 = Var(within=Reals,bounds=(-0.374,0.626),initialize=0.176375356)
m.x4 = Var(within=Reals,bounds=(1.354,2.354),initialize=1.655137904)
m.x5 = Var(within=Reals,bounds=(-0.328,0.672),initialize=-0.035787883)
m.x6 = Var(within=Reals,bounds=(1.349,2.349),initialize=1.573052867)
m.x7 = Var(within=Reals,bounds=(-0.345,0.655),initialize=0.00483050400000007)
m.x8 = Var(within=Reals,bounds=(1.315,2.315),initialize=2.171270347)
m.x9 = Var(within=Reals,bounds=(-0.281,0.719),initialize=-0.213886277)
m.x10 = Var(within=Reals,bounds=(1.328,2.328),initialize=1.828210669)
m.x11 = Var(within=Reals,bounds=(-0.255,0.745),initialize=0.743117627)
m.x12 = Var(within=Reals,bounds=(1.347,2.347),initialize=1.925733378)
m.x13 = Var(within=Reals,bounds=(-0.226,0.774),initialize=0.765133039)
m.x14 = Var(within=Reals,bounds=(1.304,2.304),initialize=2.066250467)
m.x15 = Var(within=Reals,bounds=(-0.236,0.764),initialize=-0.105307517)
m.x16 = Var(within=Reals,bounds=(1.332,2.332),initialize=1.971718759)
m.x17 = Var(within=Reals,bounds=(-0.188,0.812),initialize=-0.028482136)
m.x18 = Var(within=Reals,bounds=(1.338,2.338),initialize=1.588080533)
m.x19 = Var(within=Reals,bounds=(-0.176,0.824),initialize=0.492928609)
m.x20 = Var(within=Reals,bounds=(1.317,2.317),initialize=1.752356381)
m.x21 = Var(within=Reals,bounds=(-0.167,0.833),initialize=0.192700266)
m.x22 = Var(within=Reals,bounds=(1.32,2.32),initialize=1.671441368)
m.x23 = Var(within=Reals,bounds=(-0.101,0.899),initialize=0.03049159)
m.x24 = Var(within=Reals,bounds=(1.345,2.345),initialize=1.495101788)
m.x25 = Var(within=Reals,bounds=(-0.083,0.917),initialize=0.50611365)
m.x26 = Var(within=Reals,bounds=(1.329,2.329),initialize=2.159892812)
m.x27 = Var(within=Reals,bounds=(-0.081,0.919),initialize=0.149815738)
m.x28 = Var(within=Reals,bounds=(1.332,2.332),initialize=1.99773446)
m.x29 = Var(within=Reals,bounds=(-0.061,0.939),initialize=0.714857606)
m.x30 = Var(within=Reals,bounds=(1.32,2.32),initialize=1.623658477)
m.x31 = Var(within=Reals,bounds=(-0.025,0.975),initialize=0.085492291)
m.x32 = Var(within=Reals,bounds=(1.32,2.32),initialize=1.822384866)
m.x33 = Var(within=Reals,bounds=(0.00600000000000001,1.006),initialize=0.166172762)
m.x34 = Var(within=Reals,bounds=(1.299,2.299),initialize=2.171462311)
m.x35 = Var(within=Reals,bounds=(0.038,1.038),initialize=0.303114545)
m.x36 = Var(within=Reals,bounds=(1.338,2.338),initialize=1.623814322)
m.x37 = Var(within=Reals,bounds=(0.038,1.038),initialize=0.631955922)
m.x38 = Var(within=Reals,bounds=(1.335,2.335),initialize=2.057719071)
m.x39 = Var(within=Reals,bounds=(0.091,1.091),initialize=0.719248677)
m.x40 = Var(within=Reals,bounds=(1.311,2.311),initialize=1.774797865)
m.x41 = Var(within=Reals,bounds=(0.078,1.078),initialize=0.491306994)
m.x42 = Var(within=Reals,bounds=(1.294,2.294),initialize=1.411695357)
m.x43 = Var(within=Reals,bounds=(0.126,1.126),initialize=0.440212267)
m.x44 = Var(within=Reals,bounds=(1.325,2.325),initialize=1.371551514)
m.x45 = Var(within=Reals,bounds=(0.159,1.159),initialize=0.497550272)
m.x46 = Var(within=Reals,bounds=(1.301,2.301),initialize=1.483099593)
m.x47 = Var(within=Reals,bounds=(0.168,1.168),initialize=0.813727127)
m.x48 = Var(within=Reals,bounds=(1.31,2.31),initialize=1.870745547)
m.x49 = Var(within=Reals,bounds=(0.187,1.187),initialize=0.95696172)
m.x50 = Var(within=Reals,bounds=(1.302,2.302),initialize=1.599805864)
m.x51 = Var(within=Reals,bounds=(1,10),initialize=6.949956349)
m.x52 = Var(within=Reals,bounds=(2,10),initialize=8.046573392)

m.obj = Objective(expr=(-0.113 + m.x1)**2 + (-1.851 + m.x2)**2 + (-0.126 + m.x3)**2 + (-1.854 + m.x4)**2 + (-0.172 + 
                       m.x5)**2 + (-1.849 + m.x6)**2 + (-0.155 + m.x7)**2 + (-1.815 + m.x8)**2 + (-0.219 + m.x9)**2 + (-
                       1.828 + m.x10)**2 + (-0.245 + m.x11)**2 + (-1.847 + m.x12)**2 + (-0.274 + m.x13)**2 + (-1.804 + 
                       m.x14)**2 + (-0.264 + m.x15)**2 + (-1.832 + m.x16)**2 + (-0.312 + m.x17)**2 + (-1.838 + m.x18)**2
                        + (-0.324 + m.x19)**2 + (-1.817 + m.x20)**2 + (-0.333 + m.x21)**2 + (-1.82 + m.x22)**2 + (-0.399
                        + m.x23)**2 + (-1.845 + m.x24)**2 + (-0.417 + m.x25)**2 + (-1.829 + m.x26)**2 + (-0.419 + m.x27)
                       **2 + (-1.832 + m.x28)**2 + (-0.439 + m.x29)**2 + (-1.82 + m.x30)**2 + (-0.475 + m.x31)**2 + (-
                       1.82 + m.x32)**2 + (-0.506 + m.x33)**2 + (-1.799 + m.x34)**2 + (-0.538 + m.x35)**2 + (-1.838 + 
                       m.x36)**2 + (-0.538 + m.x37)**2 + (-1.835 + m.x38)**2 + (-0.591 + m.x39)**2 + (-1.811 + m.x40)**2
                        + (-0.578 + m.x41)**2 + (-1.794 + m.x42)**2 + (-0.626 + m.x43)**2 + (-1.825 + m.x44)**2 + (-
                       0.659 + m.x45)**2 + (-1.801 + m.x46)**2 + (-0.668 + m.x47)**2 + (-1.81 + m.x48)**2 + (-0.687 + 
                       m.x49)**2 + (-1.802 + m.x50)**2, sense=minimize)

m.c2 = Constraint(expr=1/(m.x1 - m.x52) - m.x2 + m.x51 == 0)

m.c3 = Constraint(expr=1/(m.x3 - m.x52) - m.x4 + m.x51 == 0)

m.c4 = Constraint(expr=1/(m.x5 - m.x52) - m.x6 + m.x51 == 0)

m.c5 = Constraint(expr=1/(m.x7 - m.x52) - m.x8 + m.x51 == 0)

m.c6 = Constraint(expr=1/(m.x9 - m.x52) - m.x10 + m.x51 == 0)

m.c7 = Constraint(expr=1/(m.x11 - m.x52) - m.x12 + m.x51 == 0)

m.c8 = Constraint(expr=1/(m.x13 - m.x52) - m.x14 + m.x51 == 0)

m.c9 = Constraint(expr=1/(m.x15 - m.x52) - m.x16 + m.x51 == 0)

m.c10 = Constraint(expr=1/(m.x17 - m.x52) - m.x18 + m.x51 == 0)

m.c11 = Constraint(expr=1/(m.x19 - m.x52) - m.x20 + m.x51 == 0)

m.c12 = Constraint(expr=1/(m.x21 - m.x52) - m.x22 + m.x51 == 0)

m.c13 = Constraint(expr=1/(m.x23 - m.x52) - m.x24 + m.x51 == 0)

m.c14 = Constraint(expr=1/(m.x25 - m.x52) - m.x26 + m.x51 == 0)

m.c15 = Constraint(expr=1/(m.x27 - m.x52) - m.x28 + m.x51 == 0)

m.c16 = Constraint(expr=1/(m.x29 - m.x52) - m.x30 + m.x51 == 0)

m.c17 = Constraint(expr=1/(m.x31 - m.x52) - m.x32 + m.x51 == 0)

m.c18 = Constraint(expr=1/(m.x33 - m.x52) - m.x34 + m.x51 == 0)

m.c19 = Constraint(expr=1/(m.x35 - m.x52) - m.x36 + m.x51 == 0)

m.c20 = Constraint(expr=1/(m.x37 - m.x52) - m.x38 + m.x51 == 0)

m.c21 = Constraint(expr=1/(m.x39 - m.x52) - m.x40 + m.x51 == 0)

m.c22 = Constraint(expr=1/(m.x41 - m.x52) - m.x42 + m.x51 == 0)

m.c23 = Constraint(expr=1/(m.x43 - m.x52) - m.x44 + m.x51 == 0)

m.c24 = Constraint(expr=1/(m.x45 - m.x52) - m.x46 + m.x51 == 0)

m.c25 = Constraint(expr=1/(m.x47 - m.x52) - m.x48 + m.x51 == 0)

m.c26 = Constraint(expr=1/(m.x49 - m.x52) - m.x50 + m.x51 == 0)
