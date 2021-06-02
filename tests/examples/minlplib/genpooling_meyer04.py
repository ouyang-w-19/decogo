#  MINLP written by GAMS Convert at 04/21/18 13:52:21
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        142       17       51       74        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        119       64       55        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        740      584      156        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,47.5),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,47.5),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,47.5),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,47.5),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,28),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,28),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,28),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,28),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x34 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x35 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x36 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x37 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x38 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x39 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x40 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x41 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x42 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x43 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x44 = Var(within=Reals,bounds=(0,300.5),initialize=0)
m.x45 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x46 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x47 = Var(within=Reals,bounds=(0,47.5),initialize=0)
m.x48 = Var(within=Reals,bounds=(0,28),initialize=0)
m.x49 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x50 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x51 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x52 = Var(within=Reals,bounds=(0,12),initialize=0)
m.x53 = Var(within=Reals,bounds=(0,175),initialize=0)
m.x54 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x55 = Var(within=Reals,bounds=(0,1200),initialize=0)
m.x56 = Var(within=Reals,bounds=(0,227.5),initialize=0)
m.x57 = Var(within=Reals,bounds=(0,200),initialize=0)
m.x58 = Var(within=Reals,bounds=(0,1080),initialize=0)
m.x59 = Var(within=Reals,bounds=(0,17.5),initialize=0)
m.x60 = Var(within=Reals,bounds=(0,2000),initialize=0)
m.x61 = Var(within=Reals,bounds=(0,360),initialize=0)
m.x62 = Var(within=Reals,bounds=(0,1400),initialize=0)
m.x63 = Var(within=Reals,bounds=(0,1400),initialize=0)
m.b64 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b65 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b66 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b67 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b68 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b69 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b70 = Var(within=Binary,bounds=(0,1),initialize=0)
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

m.obj = Objective(expr=   75.0708333333333*m.x1 + 150.141666666667*m.x2 + 280.264444444444*m.x3 + 245.231388888889*m.x4
                        + 55.0519444444444*m.x5 + 125.118055555556*m.x6 + 260.245555555556*m.x7 + 215.203055555556*m.x8
                        + 30.0283333333333*m.x9 + 115.108611111111*m.x10 + 240.226666666667*m.x11
                        + 220.207777777778*m.x12 + 55.0519444444444*m.x13 + 140.132222222222*m.x14
                        + 245.231388888889*m.x15 + 245.231388888889*m.x16 + 55.0519444444444*m.x17
                        + 40.0377777777778*m.x18 + 150.141666666667*m.x19 + 150.141666666667*m.x20
                        + 40.0377777777778*m.x21 + 120.113333333333*m.x22 + 230.217222222222*m.x23
                        + 230.217222222222*m.x24 + 30.0283333333333*m.x25 + 60.0566666666667*m.x26
                        + 175.165277777778*m.x27 + 165.155833333333*m.x28 + 1177.97083333333*m.x29
                        + 2975.27555555556*m.x30 + 1263.05111111111*m.x31 + 1293.07944444444*m.x32
                        + 1182.97555555556*m.x33 + 1313.09833333333*m.x34 + 1293.07944444444*m.x35
                        + 2975.27555555556*m.x36 + 3025.32277777778*m.x37 + 2995.29444444444*m.x38
                        + 1313.09833333333*m.x39 + 1233.02277777778*m.x40 + 1213.00388888889*m.x41
                        + 1293.07944444444*m.x42 + 1202.99444444444*m.x43 + 1213.00388888889*m.x44
                        + 150.141666666667*m.x45 + 135.1275*m.x46 + 100.094444444444*m.x47 + 90.085*m.x48
                        + 40.0377777777778*m.x49 + 70.0661111111111*m.x50 + 45.0425*m.x51 + 9345*m.b64 + 18690*m.b65
                        + 34888*m.b66 + 30527*m.b67 + 6853*m.b68 + 15575*m.b69 + 32396*m.b70 + 26789*m.b71 + 3738*m.b72
                        + 14329*m.b73 + 29904*m.b74 + 27412*m.b75 + 6853*m.b76 + 17444*m.b77 + 30527*m.b78 + 30527*m.b79
                        + 6853*m.b80 + 4984*m.b81 + 18690*m.b82 + 18690*m.b83 + 4984*m.b84 + 14952*m.b85 + 28658*m.b86
                        + 28658*m.b87 + 3738*m.b88 + 7476*m.b89 + 21805*m.b90 + 20559*m.b91 + 9345*m.b92 + 9968*m.b93
                        + 19936*m.b94 + 23674*m.b95 + 9968*m.b96 + 26166*m.b97 + 23674*m.b98 + 9968*m.b99 + 16198*m.b100
                        + 12460*m.b101 + 26166*m.b102 + 16198*m.b103 + 13706*m.b104 + 23674*m.b105 + 12460*m.b106
                        + 13706*m.b107 + 18690*m.b108 + 16821*m.b109 + 12460*m.b110 + 11214*m.b111 + 4984*m.b112
                        + 8722*m.b113 + 5607*m.b114 + 13972*m.b115 + 36676*m.b116 + 13972*m.b117 + 13972*m.b118
                       , sense=minimize)

m.c2 = Constraint(expr= - m.x1 - m.x2 - m.x3 - m.x4 - m.x45 <= -20)

m.c3 = Constraint(expr= - m.x5 - m.x6 - m.x7 - m.x8 - m.x46 <= -50)

m.c4 = Constraint(expr= - m.x9 - m.x10 - m.x11 - m.x12 - m.x47 <= -47.5)

m.c5 = Constraint(expr= - m.x13 - m.x14 - m.x15 - m.x16 - m.x48 <= -28)

m.c6 = Constraint(expr= - m.x17 - m.x18 - m.x19 - m.x20 - m.x49 <= -100)

m.c7 = Constraint(expr= - m.x21 - m.x22 - m.x23 - m.x24 - m.x50 <= -30)

m.c8 = Constraint(expr= - m.x25 - m.x26 - m.x27 - m.x28 - m.x51 <= -25)

m.c9 = Constraint(expr=   m.x1 + m.x2 + m.x3 + m.x4 + m.x45 <= 20)

m.c10 = Constraint(expr=   m.x5 + m.x6 + m.x7 + m.x8 + m.x46 <= 50)

m.c11 = Constraint(expr=   m.x9 + m.x10 + m.x11 + m.x12 + m.x47 <= 47.5)

m.c12 = Constraint(expr=   m.x13 + m.x14 + m.x15 + m.x16 + m.x48 <= 28)

m.c13 = Constraint(expr=   m.x17 + m.x18 + m.x19 + m.x20 + m.x49 <= 100)

m.c14 = Constraint(expr=   m.x21 + m.x22 + m.x23 + m.x24 + m.x50 <= 30)

m.c15 = Constraint(expr=   m.x25 + m.x26 + m.x27 + m.x28 + m.x51 <= 25)

m.c16 = Constraint(expr=   m.x29 + m.x33 + m.x34 + m.x35 - 300.5*m.b115 <= 0)

m.c17 = Constraint(expr=   m.x30 + m.x36 + m.x37 + m.x38 - 300.5*m.b116 <= 0)

m.c18 = Constraint(expr=   m.x31 + m.x39 + m.x40 + m.x41 - 300.5*m.b117 <= 0)

m.c19 = Constraint(expr=   m.x32 + m.x42 + m.x43 + m.x44 - 300.5*m.b118 <= 0)

m.c20 = Constraint(expr= - m.x29 - m.x30 - m.x31 - m.x32 - m.x45 - m.x46 - m.x47 - m.x48 - m.x49 - m.x50 - m.x51
                         <= -300.5)

m.c21 = Constraint(expr=   m.x29 + m.x30 + m.x31 + m.x32 + m.x45 + m.x46 + m.x47 + m.x48 + m.x49 + m.x50 + m.x51
                         <= 300.5)

m.c22 = Constraint(expr=   m.x1 + m.x5 + m.x9 + m.x13 + m.x17 + m.x21 + m.x25 - m.x29 - m.x33 - m.x34 - m.x35 + m.x36
                         + m.x39 + m.x42 == 0)

m.c23 = Constraint(expr=   m.x2 + m.x6 + m.x10 + m.x14 + m.x18 + m.x22 + m.x26 - m.x30 + m.x33 - m.x36 - m.x37 - m.x38
                         + m.x40 + m.x43 == 0)

m.c24 = Constraint(expr=   m.x3 + m.x7 + m.x11 + m.x15 + m.x19 + m.x23 + m.x27 - m.x31 + m.x34 + m.x37 - m.x39 - m.x40
                         - m.x41 + m.x44 == 0)

m.c25 = Constraint(expr=   m.x4 + m.x8 + m.x12 + m.x16 + m.x20 + m.x24 + m.x28 - m.x32 + m.x35 + m.x38 + m.x41 - m.x42
                         - m.x43 - m.x44 == 0)

m.c26 = Constraint(expr=0.01*(m.x55*m.x36 + m.x58*m.x39 + m.x61*m.x42) - (m.x52*m.x29 + m.x52*m.x33 + m.x52*m.x34 + 
                        m.x52*m.x35) + m.x1 + 8.00000000000001*m.x5 + 4*m.x9 + 12*m.x13 + 5*m.x17 + 0.5*m.x21 + 10*m.x25
                         == 0)

m.c27 = Constraint(expr=0.1*(m.x56*m.x36 + m.x59*m.x39 + m.x62*m.x42) - (m.x53*m.x29 + m.x53*m.x33 + m.x53*m.x34 + m.x53
                        *m.x35) + 50*m.x1 + 175*m.x5 + 8*m.x9 + 100*m.x13 + 70*m.x17 + 10*m.x21 + 5*m.x25 == 0)

m.c28 = Constraint(expr=0.05*(m.x57*m.x36 + m.x60*m.x39 + m.x63*m.x42) - (m.x54*m.x29 + m.x54*m.x33 + m.x54*m.x34 + 
                        m.x54*m.x35) + 25*m.x1 + 100*m.x5 + 5*m.x9 + 20*m.x13 + 12.5*m.x17 + 2.5*m.x21
                         + 7.50000000000001*m.x25 == 0)

m.c29 = Constraint(expr=m.x52*m.x33 + m.x58*m.x40 + m.x61*m.x43 - (m.x55*m.x30 + m.x55*m.x36 + m.x55*m.x37 + m.x55*m.x38
                        ) + 100*m.x2 + 800*m.x6 + 400*m.x10 + 1200*m.x14 + 500*m.x18 + 50*m.x22 + 1000*m.x26 == 0)

m.c30 = Constraint(expr=0.13*(m.x53*m.x33 + m.x59*m.x40 + m.x62*m.x43) - (m.x56*m.x30 + m.x56*m.x36 + m.x56*m.x37 + 
                        m.x56*m.x38) + 65*m.x2 + 227.5*m.x6 + 10.4*m.x10 + 130*m.x14 + 91*m.x18 + 13*m.x22 + 6.5*m.x26
                         == 0)

m.c31 = Constraint(expr=0.1*(m.x54*m.x33 + m.x60*m.x40 + m.x63*m.x43) - (m.x57*m.x30 + m.x57*m.x36 + m.x57*m.x37 + m.x57
                        *m.x38) + 50*m.x2 + 200*m.x6 + 10*m.x10 + 40*m.x14 + 25*m.x18 + 5*m.x22 + 15*m.x26 == 0)

m.c32 = Constraint(expr=0.9*(m.x52*m.x34 + m.x55*m.x37 + m.x61*m.x44) - (m.x58*m.x31 + m.x58*m.x39 + m.x58*m.x40 + m.x58
                        *m.x41) + 90*m.x3 + 720*m.x7 + 360*m.x11 + 1080*m.x15 + 450*m.x19 + 45*m.x23 + 900*m.x27 == 0)

m.c33 = Constraint(expr=0.01*(m.x53*m.x34 + m.x56*m.x37 + m.x62*m.x44) - (m.x59*m.x31 + m.x59*m.x39 + m.x59*m.x40 + 
                        m.x59*m.x41) + 5*m.x3 + 17.5*m.x7 + 0.800000000000001*m.x11 + 10*m.x15 + 7.00000000000001*m.x19
                         + m.x23 + 0.5*m.x27 == 0)

m.c34 = Constraint(expr=m.x54*m.x34 + m.x57*m.x37 + m.x63*m.x44 - (m.x60*m.x31 + m.x60*m.x39 + m.x60*m.x40 + m.x60*m.x41
                        ) + 500*m.x3 + 2000*m.x7 + 100*m.x11 + 400*m.x15 + 250*m.x19 + 50*m.x23 + 150*m.x27 == 0)

m.c35 = Constraint(expr=0.3*(m.x52*m.x35 + m.x55*m.x38 + m.x58*m.x41) - (m.x61*m.x32 + m.x61*m.x42 + m.x61*m.x43 + m.x61
                        *m.x44) + 30*m.x4 + 240*m.x8 + 120*m.x12 + 360*m.x16 + 150*m.x20 + 15*m.x24 + 300*m.x28 == 0)

m.c36 = Constraint(expr=0.8*(m.x53*m.x35 + m.x56*m.x38 + m.x59*m.x41) - (m.x62*m.x32 + m.x62*m.x42 + m.x62*m.x43 + m.x62
                        *m.x44) + 400*m.x4 + 1400*m.x8 + 64*m.x12 + 800*m.x16 + 560*m.x20 + 80*m.x24 + 40*m.x28 == 0)

m.c37 = Constraint(expr=0.7*(m.x54*m.x35 + m.x57*m.x38 + m.x60*m.x41) - (m.x63*m.x32 + m.x63*m.x42 + m.x63*m.x43 + m.x63
                        *m.x44) + 350*m.x4 + 1400*m.x8 + 70*m.x12 + 280*m.x16 + 175*m.x20 + 35*m.x24 + 105*m.x28 == 0)

m.c38 = Constraint(expr=m.x52*m.x29 + m.x55*m.x30 + m.x58*m.x31 + m.x61*m.x32 - 5*m.x29 - 5*m.x30 - 5*m.x31 - 5*m.x32
                         + 95*m.x45 + 795*m.x46 + 395*m.x47 + 1195*m.x48 + 495*m.x49 + 45*m.x50 + 995*m.x51 <= 0)

m.c39 = Constraint(expr=m.x53*m.x29 + m.x56*m.x30 + m.x59*m.x31 + m.x62*m.x32 - 5*m.x29 - 5*m.x30 - 5*m.x31 - 5*m.x32
                         + 495*m.x45 + 1745*m.x46 + 75*m.x47 + 995*m.x48 + 695*m.x49 + 95*m.x50 + 45*m.x51 <= 0)

m.c40 = Constraint(expr=m.x54*m.x29 + m.x57*m.x30 + m.x60*m.x31 + m.x63*m.x32 - 10*m.x29 - 10*m.x30 - 10*m.x31 - 10*
                        m.x32 + 490*m.x45 + 1990*m.x46 + 90*m.x47 + 390*m.x48 + 240*m.x49 + 40*m.x50 + 140*m.x51 <= 0)

m.c41 = Constraint(expr=   m.x1 - 0.2*m.b64 >= 0)

m.c42 = Constraint(expr=   m.x2 - 0.2*m.b65 >= 0)

m.c43 = Constraint(expr=   m.x3 - 0.2*m.b66 >= 0)

m.c44 = Constraint(expr=   m.x4 - 0.2*m.b67 >= 0)

m.c45 = Constraint(expr=   m.x5 - 0.2*m.b68 >= 0)

m.c46 = Constraint(expr=   m.x6 - 0.2*m.b69 >= 0)

m.c47 = Constraint(expr=   m.x7 - 0.2*m.b70 >= 0)

m.c48 = Constraint(expr=   m.x8 - 0.2*m.b71 >= 0)

m.c49 = Constraint(expr=   m.x9 - 0.2*m.b72 >= 0)

m.c50 = Constraint(expr=   m.x10 - 0.2*m.b73 >= 0)

m.c51 = Constraint(expr=   m.x11 - 0.2*m.b74 >= 0)

m.c52 = Constraint(expr=   m.x12 - 0.2*m.b75 >= 0)

m.c53 = Constraint(expr=   m.x13 - 0.2*m.b76 >= 0)

m.c54 = Constraint(expr=   m.x14 - 0.2*m.b77 >= 0)

m.c55 = Constraint(expr=   m.x15 - 0.2*m.b78 >= 0)

m.c56 = Constraint(expr=   m.x16 - 0.2*m.b79 >= 0)

m.c57 = Constraint(expr=   m.x17 - 0.2*m.b80 >= 0)

m.c58 = Constraint(expr=   m.x18 - 0.2*m.b81 >= 0)

m.c59 = Constraint(expr=   m.x19 - 0.2*m.b82 >= 0)

m.c60 = Constraint(expr=   m.x20 - 0.2*m.b83 >= 0)

m.c61 = Constraint(expr=   m.x21 - 0.2*m.b84 >= 0)

m.c62 = Constraint(expr=   m.x22 - 0.2*m.b85 >= 0)

m.c63 = Constraint(expr=   m.x23 - 0.2*m.b86 >= 0)

m.c64 = Constraint(expr=   m.x24 - 0.2*m.b87 >= 0)

m.c65 = Constraint(expr=   m.x25 - 0.2*m.b88 >= 0)

m.c66 = Constraint(expr=   m.x26 - 0.2*m.b89 >= 0)

m.c67 = Constraint(expr=   m.x27 - 0.2*m.b90 >= 0)

m.c68 = Constraint(expr=   m.x28 - 0.2*m.b91 >= 0)

m.c69 = Constraint(expr=   m.x1 - 20*m.b64 <= 0)

m.c70 = Constraint(expr=   m.x2 - 20*m.b65 <= 0)

m.c71 = Constraint(expr=   m.x3 - 20*m.b66 <= 0)

m.c72 = Constraint(expr=   m.x4 - 20*m.b67 <= 0)

m.c73 = Constraint(expr=   m.x5 - 50*m.b68 <= 0)

m.c74 = Constraint(expr=   m.x6 - 50*m.b69 <= 0)

m.c75 = Constraint(expr=   m.x7 - 50*m.b70 <= 0)

m.c76 = Constraint(expr=   m.x8 - 50*m.b71 <= 0)

m.c77 = Constraint(expr=   m.x9 - 47.5*m.b72 <= 0)

m.c78 = Constraint(expr=   m.x10 - 47.5*m.b73 <= 0)

m.c79 = Constraint(expr=   m.x11 - 47.5*m.b74 <= 0)

m.c80 = Constraint(expr=   m.x12 - 47.5*m.b75 <= 0)

m.c81 = Constraint(expr=   m.x13 - 28*m.b76 <= 0)

m.c82 = Constraint(expr=   m.x14 - 28*m.b77 <= 0)

m.c83 = Constraint(expr=   m.x15 - 28*m.b78 <= 0)

m.c84 = Constraint(expr=   m.x16 - 28*m.b79 <= 0)

m.c85 = Constraint(expr=   m.x17 - 100*m.b80 <= 0)

m.c86 = Constraint(expr=   m.x18 - 100*m.b81 <= 0)

m.c87 = Constraint(expr=   m.x19 - 100*m.b82 <= 0)

m.c88 = Constraint(expr=   m.x20 - 100*m.b83 <= 0)

m.c89 = Constraint(expr=   m.x21 - 30*m.b84 <= 0)

m.c90 = Constraint(expr=   m.x22 - 30*m.b85 <= 0)

m.c91 = Constraint(expr=   m.x23 - 30*m.b86 <= 0)

m.c92 = Constraint(expr=   m.x24 - 30*m.b87 <= 0)

m.c93 = Constraint(expr=   m.x25 - 25*m.b88 <= 0)

m.c94 = Constraint(expr=   m.x26 - 25*m.b89 <= 0)

m.c95 = Constraint(expr=   m.x27 - 25*m.b90 <= 0)

m.c96 = Constraint(expr=   m.x28 - 25*m.b91 <= 0)

m.c97 = Constraint(expr=   m.x29 - 0.2*m.b92 >= 0)

m.c98 = Constraint(expr=   m.x30 - 0.2*m.b93 >= 0)

m.c99 = Constraint(expr=   m.x31 - 0.2*m.b94 >= 0)

m.c100 = Constraint(expr=   m.x32 - 0.2*m.b95 >= 0)

m.c101 = Constraint(expr=   m.x29 - 300.5*m.b92 <= 0)

m.c102 = Constraint(expr=   m.x30 - 300.5*m.b93 <= 0)

m.c103 = Constraint(expr=   m.x31 - 300.5*m.b94 <= 0)

m.c104 = Constraint(expr=   m.x32 - 300.5*m.b95 <= 0)

m.c105 = Constraint(expr=   m.x45 - 0.2*m.b108 >= 0)

m.c106 = Constraint(expr=   m.x46 - 0.2*m.b109 >= 0)

m.c107 = Constraint(expr=   m.x47 - 0.2*m.b110 >= 0)

m.c108 = Constraint(expr=   m.x48 - 0.2*m.b111 >= 0)

m.c109 = Constraint(expr=   m.x49 - 0.2*m.b112 >= 0)

m.c110 = Constraint(expr=   m.x50 - 0.2*m.b113 >= 0)

m.c111 = Constraint(expr=   m.x51 - 0.2*m.b114 >= 0)

m.c112 = Constraint(expr=   m.x45 - 20*m.b108 <= 0)

m.c113 = Constraint(expr=   m.x46 - 50*m.b109 <= 0)

m.c114 = Constraint(expr=   m.x47 - 47.5*m.b110 <= 0)

m.c115 = Constraint(expr=   m.x48 - 28*m.b111 <= 0)

m.c116 = Constraint(expr=   m.x49 - 100*m.b112 <= 0)

m.c117 = Constraint(expr=   m.x50 - 30*m.b113 <= 0)

m.c118 = Constraint(expr=   m.x51 - 25*m.b114 <= 0)

m.c119 = Constraint(expr=   m.x36 - 0.2*m.b99 >= 0)

m.c120 = Constraint(expr=   m.x39 - 0.2*m.b102 >= 0)

m.c121 = Constraint(expr=   m.x42 - 0.2*m.b105 >= 0)

m.c122 = Constraint(expr=   m.x33 - 0.2*m.b96 >= 0)

m.c123 = Constraint(expr=   m.x40 - 0.2*m.b103 >= 0)

m.c124 = Constraint(expr=   m.x43 - 0.2*m.b106 >= 0)

m.c125 = Constraint(expr=   m.x34 - 0.2*m.b97 >= 0)

m.c126 = Constraint(expr=   m.x37 - 0.2*m.b100 >= 0)

m.c127 = Constraint(expr=   m.x44 - 0.2*m.b107 >= 0)

m.c128 = Constraint(expr=   m.x35 - 0.2*m.b98 >= 0)

m.c129 = Constraint(expr=   m.x38 - 0.2*m.b101 >= 0)

m.c130 = Constraint(expr=   m.x41 - 0.2*m.b104 >= 0)

m.c131 = Constraint(expr=   m.x36 - 300.5*m.b99 <= 0)

m.c132 = Constraint(expr=   m.x39 - 300.5*m.b102 <= 0)

m.c133 = Constraint(expr=   m.x42 - 300.5*m.b105 <= 0)

m.c134 = Constraint(expr=   m.x33 - 300.5*m.b96 <= 0)

m.c135 = Constraint(expr=   m.x40 - 300.5*m.b103 <= 0)

m.c136 = Constraint(expr=   m.x43 - 300.5*m.b106 <= 0)

m.c137 = Constraint(expr=   m.x34 - 300.5*m.b97 <= 0)

m.c138 = Constraint(expr=   m.x37 - 300.5*m.b100 <= 0)

m.c139 = Constraint(expr=   m.x44 - 300.5*m.b107 <= 0)

m.c140 = Constraint(expr=   m.x35 - 300.5*m.b98 <= 0)

m.c141 = Constraint(expr=   m.x38 - 300.5*m.b101 <= 0)

m.c142 = Constraint(expr=   m.x41 - 300.5*m.b104 <= 0)
