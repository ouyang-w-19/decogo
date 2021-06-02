#  NLP written by GAMS Convert at 04/21/18 13:51:48
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         46       46        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         76       76        0        0        0        0        0        0
#  FX      6        6        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        361       46      315        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x2 = Var(within=Reals,bounds=(-5,5),initialize=3.43266708)
m.x3 = Var(within=Reals,bounds=(-5,5),initialize=0.50375356)
m.x4 = Var(within=Reals,bounds=(-5,5),initialize=-1.98862096)
m.x5 = Var(within=Reals,bounds=(-5,5),initialize=-2.07787883)
m.x6 = Var(within=Reals,bounds=(-5,5),initialize=-2.75947133)
m.x7 = Var(within=Reals,bounds=(-5,5),initialize=-1.50169496)
m.x8 = Var(within=Reals,bounds=(-5,5),initialize=3.56270347)
m.x9 = Var(within=Reals,bounds=(-5,5),initialize=-4.32886277)
m.x10 = Var(within=Reals,bounds=(-5,5),initialize=0.00210668999999974)
m.x11 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x13 = Var(within=Reals,bounds=(-5,5),initialize=4.91133039)
m.x14 = Var(within=Reals,bounds=(-5,5),initialize=2.62250467)
m.x15 = Var(within=Reals,bounds=(-5,5),initialize=-3.69307517)
m.x16 = Var(within=Reals,bounds=(-5,5),initialize=1.39718759)
m.x17 = Var(within=Reals,bounds=(-5,5),initialize=-3.40482136)
m.x18 = Var(within=Reals,bounds=(-5,5),initialize=-2.49919467)
m.x19 = Var(within=Reals,bounds=(-5,5),initialize=1.68928609)
m.x20 = Var(within=Reals,bounds=(-5,5),initialize=-0.64643619)
m.x21 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x24 = Var(within=Reals,bounds=(-5,5),initialize=-3.49898212)
m.x25 = Var(within=Reals,bounds=(-5,5),initialize=0.8911365)
m.x26 = Var(within=Reals,bounds=(-5,5),initialize=3.30892812)
m.x27 = Var(within=Reals,bounds=(-5,5),initialize=-2.69184262)
m.x28 = Var(within=Reals,bounds=(-5,5),initialize=1.6573446)
m.x29 = Var(within=Reals,bounds=(-5,5),initialize=2.75857606)
m.x30 = Var(within=Reals,bounds=(-5,5),initialize=-1.96341523)
m.x31 = Var(within=Reals,bounds=(None,None),initialize=0.0848665660820583)
m.x32 = Var(within=Reals,bounds=(None,None),initialize=0.0410257523649882)
m.x33 = Var(within=Reals,bounds=(None,None),initialize=0.0433369072910337)
m.x34 = Var(within=Reals,bounds=(None,None),initialize=0.0533318858204364)
m.x35 = Var(within=Reals,bounds=(None,None),initialize=0.048742871418623)
m.x36 = Var(within=Reals,bounds=(None,None),initialize=0.0474070412149129)
m.x37 = Var(within=Reals,bounds=(None,None),initialize=0.0461135050589101)
m.x38 = Var(within=Reals,bounds=(None,None),initialize=0.0342436643329313)
m.x39 = Var(within=Reals,bounds=(None,None),initialize=0.234033993203568)
m.x40 = Var(within=Reals,bounds=(None,None),initialize=0.0305813197498946)
m.x41 = Var(within=Reals,bounds=(None,None),initialize=0.0206139788536328)
m.x42 = Var(within=Reals,bounds=(None,None),initialize=0.022321904556586)
m.x43 = Var(within=Reals,bounds=(None,None),initialize=0.019514587685195)
m.x44 = Var(within=Reals,bounds=(None,None),initialize=0.0231552480584656)
m.x45 = Var(within=Reals,bounds=(None,None),initialize=0.110991800051043)
m.x46 = Var(within=Reals,bounds=(None,None),initialize=0.0141433163490096)
m.x47 = Var(within=Reals,bounds=(None,None),initialize=0.06233782929589)
m.x48 = Var(within=Reals,bounds=(None,None),initialize=0.0422056151370249)
m.x49 = Var(within=Reals,bounds=(None,None),initialize=0.0122707298338899)
m.x50 = Var(within=Reals,bounds=(None,None),initialize=0.0294578214857431)
m.x51 = Var(within=Reals,bounds=(None,None),initialize=0.0124337559964587)
m.x52 = Var(within=Reals,bounds=(None,None),initialize=0.0149209531159923)
m.x53 = Var(within=Reals,bounds=(None,None),initialize=0.0241864337079319)
m.x54 = Var(within=Reals,bounds=(None,None),initialize=0.0285751692200051)
m.x55 = Var(within=Reals,bounds=(None,None),initialize=0.0169011255076456)
m.x56 = Var(within=Reals,bounds=(None,None),initialize=0.0206427090641815)
m.x57 = Var(within=Reals,bounds=(None,None),initialize=0.0268692752074436)
m.x58 = Var(within=Reals,bounds=(None,None),initialize=0.0119564718949588)
m.x59 = Var(within=Reals,bounds=(None,None),initialize=0.0219757698125455)
m.x60 = Var(within=Reals,bounds=(None,None),initialize=0.0587995371380756)
m.x61 = Var(within=Reals,bounds=(None,None),initialize=0.0310356025470503)
m.x62 = Var(within=Reals,bounds=(None,None),initialize=0.075455653192454)
m.x63 = Var(within=Reals,bounds=(None,None),initialize=0.0295607909263086)
m.x64 = Var(within=Reals,bounds=(None,None),initialize=0.0266495598227703)
m.x65 = Var(within=Reals,bounds=(None,None),initialize=0.0459626111078803)
m.x66 = Var(within=Reals,bounds=(None,None),initialize=0.0164878991409964)
m.x67 = Var(within=Reals,bounds=(None,None),initialize=0.0172772991007472)
m.x68 = Var(within=Reals,bounds=(None,None),initialize=0.350729712295995)
m.x69 = Var(within=Reals,bounds=(None,None),initialize=0.0252523239258106)
m.x70 = Var(within=Reals,bounds=(None,None),initialize=0.0220343327084997)
m.x71 = Var(within=Reals,bounds=(None,None),initialize=0.0157109506031469)
m.x72 = Var(within=Reals,bounds=(None,None),initialize=0.0961472396262811)
m.x73 = Var(within=Reals,bounds=(None,None),initialize=0.0123406666409974)
m.x74 = Var(within=Reals,bounds=(None,None),initialize=0.0342225900399961)
m.x75 = Var(within=Reals,bounds=(None,None),initialize=0.0215007077887895)

m.obj = Objective(expr=m.x31**6 - 2*m.x31**3 + m.x32**6 - 2*m.x32**3 + m.x33**6 - 2*m.x33**3 + m.x34**6 - 2*m.x34**3 + 
                       m.x35**6 - 2*m.x35**3 + m.x36**6 - 2*m.x36**3 + m.x37**6 - 2*m.x37**3 + m.x38**6 - 2*m.x38**3 + 
                       m.x39**6 - 2*m.x39**3 + m.x40**6 - 2*m.x40**3 + m.x41**6 - 2*m.x41**3 + m.x42**6 - 2*m.x42**3 + 
                       m.x43**6 - 2*m.x43**3 + m.x44**6 - 2*m.x44**3 + m.x45**6 - 2*m.x45**3 + m.x46**6 - 2*m.x46**3 + 
                       m.x47**6 - 2*m.x47**3 + m.x48**6 - 2*m.x48**3 + m.x49**6 - 2*m.x49**3 + m.x50**6 - 2*m.x50**3 + 
                       m.x51**6 - 2*m.x51**3 + m.x52**6 - 2*m.x52**3 + m.x53**6 - 2*m.x53**3 + m.x54**6 - 2*m.x54**3 + 
                       m.x55**6 - 2*m.x55**3 + m.x56**6 - 2*m.x56**3 + m.x57**6 - 2*m.x57**3 + m.x58**6 - 2*m.x58**3 + 
                       m.x59**6 - 2*m.x59**3 + m.x60**6 - 2*m.x60**3 + m.x61**6 - 2*m.x61**3 + m.x62**6 - 2*m.x62**3 + 
                       m.x63**6 - 2*m.x63**3 + m.x64**6 - 2*m.x64**3 + m.x65**6 - 2*m.x65**3 + m.x66**6 - 2*m.x66**3 + 
                       m.x67**6 - 2*m.x67**3 + m.x68**6 - 2*m.x68**3 + m.x69**6 - 2*m.x69**3 + m.x70**6 - 2*m.x70**3 + 
                       m.x71**6 - 2*m.x71**3 + m.x72**6 - 2*m.x72**3 + m.x73**6 - 2*m.x73**3 + m.x74**6 - 2*m.x74**3 + 
                       m.x75**6 - 2*m.x75**3, sense=minimize)

m.c2 = Constraint(expr=-1/((m.x1 - m.x2)**2 + (m.x11 - m.x12)**2 + (m.x21 - m.x22)**2) + m.x31 == 0)

m.c3 = Constraint(expr=-1/((m.x1 - m.x3)**2 + (m.x11 - m.x13)**2 + (m.x21 - m.x23)**2) + m.x32 == 0)

m.c4 = Constraint(expr=-1/((m.x1 - m.x4)**2 + (m.x11 - m.x14)**2 + (m.x21 - m.x24)**2) + m.x33 == 0)

m.c5 = Constraint(expr=-1/((m.x1 - m.x5)**2 + (m.x11 - m.x15)**2 + (m.x21 - m.x25)**2) + m.x34 == 0)

m.c6 = Constraint(expr=-1/((m.x1 - m.x6)**2 + (m.x11 - m.x16)**2 + (m.x21 - m.x26)**2) + m.x35 == 0)

m.c7 = Constraint(expr=-1/((m.x1 - m.x7)**2 + (m.x11 - m.x17)**2 + (m.x21 - m.x27)**2) + m.x36 == 0)

m.c8 = Constraint(expr=-1/((m.x1 - m.x8)**2 + (m.x11 - m.x18)**2 + (m.x21 - m.x28)**2) + m.x37 == 0)

m.c9 = Constraint(expr=-1/((m.x1 - m.x9)**2 + (m.x11 - m.x19)**2 + (m.x21 - m.x29)**2) + m.x38 == 0)

m.c10 = Constraint(expr=-1/((m.x1 - m.x10)**2 + (m.x11 - m.x20)**2 + (m.x21 - m.x30)**2) + m.x39 == 0)

m.c11 = Constraint(expr=-1/((m.x2 - m.x3)**2 + (m.x12 - m.x13)**2 + (m.x22 - m.x23)**2) + m.x40 == 0)

m.c12 = Constraint(expr=-1/((m.x2 - m.x4)**2 + (m.x12 - m.x14)**2 + (m.x22 - m.x24)**2) + m.x41 == 0)

m.c13 = Constraint(expr=-1/((m.x2 - m.x5)**2 + (m.x12 - m.x15)**2 + (m.x22 - m.x25)**2) + m.x42 == 0)

m.c14 = Constraint(expr=-1/((m.x2 - m.x6)**2 + (m.x12 - m.x16)**2 + (m.x22 - m.x26)**2) + m.x43 == 0)

m.c15 = Constraint(expr=-1/((m.x2 - m.x7)**2 + (m.x12 - m.x17)**2 + (m.x22 - m.x27)**2) + m.x44 == 0)

m.c16 = Constraint(expr=-1/((m.x2 - m.x8)**2 + (m.x12 - m.x18)**2 + (m.x22 - m.x28)**2) + m.x45 == 0)

m.c17 = Constraint(expr=-1/((m.x2 - m.x9)**2 + (m.x12 - m.x19)**2 + (m.x22 - m.x29)**2) + m.x46 == 0)

m.c18 = Constraint(expr=-1/((m.x2 - m.x10)**2 + (m.x12 - m.x20)**2 + (m.x22 - m.x30)**2) + m.x47 == 0)

m.c19 = Constraint(expr=-1/((m.x3 - m.x4)**2 + (m.x13 - m.x14)**2 + (m.x23 - m.x24)**2) + m.x48 == 0)

m.c20 = Constraint(expr=-1/((m.x3 - m.x5)**2 + (m.x13 - m.x15)**2 + (m.x23 - m.x25)**2) + m.x49 == 0)

m.c21 = Constraint(expr=-1/((m.x3 - m.x6)**2 + (m.x13 - m.x16)**2 + (m.x23 - m.x26)**2) + m.x50 == 0)

m.c22 = Constraint(expr=-1/((m.x3 - m.x7)**2 + (m.x13 - m.x17)**2 + (m.x23 - m.x27)**2) + m.x51 == 0)

m.c23 = Constraint(expr=-1/((m.x3 - m.x8)**2 + (m.x13 - m.x18)**2 + (m.x23 - m.x28)**2) + m.x52 == 0)

m.c24 = Constraint(expr=-1/((m.x3 - m.x9)**2 + (m.x13 - m.x19)**2 + (m.x23 - m.x29)**2) + m.x53 == 0)

m.c25 = Constraint(expr=-1/((m.x3 - m.x10)**2 + (m.x13 - m.x20)**2 + (m.x23 - m.x30)**2) + m.x54 == 0)

m.c26 = Constraint(expr=-1/((m.x4 - m.x5)**2 + (m.x14 - m.x15)**2 + (m.x24 - m.x25)**2) + m.x55 == 0)

m.c27 = Constraint(expr=-1/((m.x4 - m.x6)**2 + (m.x14 - m.x16)**2 + (m.x24 - m.x26)**2) + m.x56 == 0)

m.c28 = Constraint(expr=-1/((m.x4 - m.x7)**2 + (m.x14 - m.x17)**2 + (m.x24 - m.x27)**2) + m.x57 == 0)

m.c29 = Constraint(expr=-1/((m.x4 - m.x8)**2 + (m.x14 - m.x18)**2 + (m.x24 - m.x28)**2) + m.x58 == 0)

m.c30 = Constraint(expr=-1/((m.x4 - m.x9)**2 + (m.x14 - m.x19)**2 + (m.x24 - m.x29)**2) + m.x59 == 0)

m.c31 = Constraint(expr=-1/((m.x4 - m.x10)**2 + (m.x14 - m.x20)**2 + (m.x24 - m.x30)**2) + m.x60 == 0)

m.c32 = Constraint(expr=-1/((m.x5 - m.x6)**2 + (m.x15 - m.x16)**2 + (m.x25 - m.x26)**2) + m.x61 == 0)

m.c33 = Constraint(expr=-1/((m.x5 - m.x7)**2 + (m.x15 - m.x17)**2 + (m.x25 - m.x27)**2) + m.x62 == 0)

m.c34 = Constraint(expr=-1/((m.x5 - m.x8)**2 + (m.x15 - m.x18)**2 + (m.x25 - m.x28)**2) + m.x63 == 0)

m.c35 = Constraint(expr=-1/((m.x5 - m.x9)**2 + (m.x15 - m.x19)**2 + (m.x25 - m.x29)**2) + m.x64 == 0)

m.c36 = Constraint(expr=-1/((m.x5 - m.x10)**2 + (m.x15 - m.x20)**2 + (m.x25 - m.x30)**2) + m.x65 == 0)

m.c37 = Constraint(expr=-1/((m.x6 - m.x7)**2 + (m.x16 - m.x17)**2 + (m.x26 - m.x27)**2) + m.x66 == 0)

m.c38 = Constraint(expr=-1/((m.x6 - m.x8)**2 + (m.x16 - m.x18)**2 + (m.x26 - m.x28)**2) + m.x67 == 0)

m.c39 = Constraint(expr=-1/((m.x6 - m.x9)**2 + (m.x16 - m.x19)**2 + (m.x26 - m.x29)**2) + m.x68 == 0)

m.c40 = Constraint(expr=-1/((m.x6 - m.x10)**2 + (m.x16 - m.x20)**2 + (m.x26 - m.x30)**2) + m.x69 == 0)

m.c41 = Constraint(expr=-1/((m.x7 - m.x8)**2 + (m.x17 - m.x18)**2 + (m.x27 - m.x28)**2) + m.x70 == 0)

m.c42 = Constraint(expr=-1/((m.x7 - m.x9)**2 + (m.x17 - m.x19)**2 + (m.x27 - m.x29)**2) + m.x71 == 0)

m.c43 = Constraint(expr=-1/((m.x7 - m.x10)**2 + (m.x17 - m.x20)**2 + (m.x27 - m.x30)**2) + m.x72 == 0)

m.c44 = Constraint(expr=-1/((m.x8 - m.x9)**2 + (m.x18 - m.x19)**2 + (m.x28 - m.x29)**2) + m.x73 == 0)

m.c45 = Constraint(expr=-1/((m.x8 - m.x10)**2 + (m.x18 - m.x20)**2 + (m.x28 - m.x30)**2) + m.x74 == 0)

m.c46 = Constraint(expr=-1/((m.x9 - m.x10)**2 + (m.x19 - m.x20)**2 + (m.x29 - m.x30)**2) + m.x75 == 0)
