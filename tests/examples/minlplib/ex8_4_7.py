#  NLP written by GAMS Convert at 04/21/18 13:51:47
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         41       41        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         63       63        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        191       51      140        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0.9571,1.0171),initialize=0.96740482792)
m.x2 = Var(within=Reals,bounds=(0.8606,0.9206),initialize=0.91119600248)
m.x3 = Var(within=Reals,bounds=(0.0857,0.1457),initialize=0.11872252136)
m.x4 = Var(within=Reals,bounds=(544.47,550.47),initialize=546.276827424)
m.x5 = Var(within=Reals,bounds=(660.48,666.48),initialize=662.233272702)
m.x6 = Var(within=Reals,bounds=(0.9703,1.0303),initialize=0.98374317202)
m.x7 = Var(within=Reals,bounds=(0.805,0.865),initialize=0.82598983024)
m.x8 = Var(within=Reals,bounds=(0.108,0.168),initialize=0.15937622082)
m.x9 = Var(within=Reals,bounds=(528.77,534.77),initialize=529.172682338)
m.x10 = Var(within=Reals,bounds=(673.04,679.04),initialize=676.041264014)
m.x11 = Var(within=Reals,bounds=(0.9739,1.0339),initialize=1.03378705762)
m.x12 = Var(within=Reals,bounds=(0.7955,0.8555),initialize=0.83022400268)
m.x13 = Var(within=Reals,bounds=(0.155,0.215),initialize=0.21446798234)
m.x14 = Var(within=Reals,bounds=(509.21,515.21),initialize=513.783502802)
m.x15 = Var(within=Reals,bounds=(681.81,687.81),initialize=682.594154898)
m.x16 = Var(within=Reals,bounds=(0.946,1.006),initialize=0.98438312554)
m.x17 = Var(within=Reals,bounds=(0.772,0.832),initialize=0.78157107184)
m.x18 = Var(within=Reals,bounds=(0.1705,0.2305),initialize=0.18550483198)
m.x19 = Var(within=Reals,bounds=(487.59,493.59),initialize=491.603571654)
m.x20 = Var(within=Reals,bounds=(692.47,698.47),initialize=695.082138286)
m.x21 = Var(within=Reals,bounds=(0.9829,1.0429),initialize=1.00448201596)
m.x22 = Var(within=Reals,bounds=(0.722,0.782),initialize=0.74308648208)
m.x23 = Var(within=Reals,bounds=(0.212,0.272),initialize=0.2198894954)
m.x24 = Var(within=Reals,bounds=(461.67,467.67),initialize=462.570610728)
m.x25 = Var(within=Reals,bounds=(700.69,706.69),initialize=704.2246819)
m.x26 = Var(within=Reals,bounds=(0.9783,1.0383),initialize=1.02815356872)
m.x27 = Var(within=Reals,bounds=(0.6893,0.7493),initialize=0.70314894428)
m.x28 = Var(within=Reals,bounds=(0.2439,0.3039),initialize=0.2838440676)
m.x29 = Var(within=Reals,bounds=(435.47,441.47),initialize=440.125145636)
m.x30 = Var(within=Reals,bounds=(711.9,717.9),initialize=713.721950862)
m.x31 = Var(within=Reals,bounds=(0.9775,1.0375),initialize=0.98412953746)
m.x32 = Var(within=Reals,bounds=(0.6561,0.7161),initialize=0.68624309196)
m.x33 = Var(within=Reals,bounds=(0.2915,0.3515),initialize=0.30111036572)
m.x34 = Var(within=Reals,bounds=(405.04,411.04),initialize=410.274773866)
m.x35 = Var(within=Reals,bounds=(723.09,729.09),initialize=724.68068727)
m.x36 = Var(within=Reals,bounds=(0.9694,1.0294),initialize=0.98654885932)
m.x37 = Var(within=Reals,bounds=(0.6088,0.6688),initialize=0.64443735532)
m.x38 = Var(within=Reals,bounds=(0.3441,0.4041),initialize=0.38746314426)
m.x39 = Var(within=Reals,bounds=(372.56,378.56),initialize=376.329492062)
m.x40 = Var(within=Reals,bounds=(732.44,738.44),initialize=735.22278719)
m.x41 = Var(within=Reals,bounds=(0.9707,1.0307),initialize=0.99549841964)
m.x42 = Var(within=Reals,bounds=(0.567,0.627),initialize=0.57406172142)
m.x43 = Var(within=Reals,bounds=(0.3626,0.4226),initialize=0.38145273602)
m.x44 = Var(within=Reals,bounds=(337.26,343.26),initialize=337.539309084)
m.x45 = Var(within=Reals,bounds=(742.7,748.7),initialize=744.731301632)
m.x46 = Var(within=Reals,bounds=(0.9673,1.0273),initialize=0.97822597558)
m.x47 = Var(within=Reals,bounds=(0.528,0.588),initialize=0.56674362762)
m.x48 = Var(within=Reals,bounds=(0.4403,0.5003),initialize=0.47394473282)
m.x49 = Var(within=Reals,bounds=(303.55,309.55),initialize=308.16977032)
m.x50 = Var(within=Reals,bounds=(750.94,756.94),initialize=752.726835184)
m.x51 = Var(within=Reals,bounds=(0.0001,0.1),initialize=0.02)
m.x52 = Var(within=Reals,bounds=(5,15),initialize=12.5)
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

m.obj = Objective(expr=(-98.71 + 100*m.x1)**2 + (-89.06 + 100*m.x2)**2 + (-11.57 + 100*m.x3)**2 + (-547.47 + m.x4)**2 + 
                       (-663.48 + m.x5)**2 + (-100.03 + 100*m.x6)**2 + (-83.5 + 100*m.x7)**2 + (-13.8 + 100*m.x8)**2 + (
                       -531.77 + m.x9)**2 + (-676.04 + m.x10)**2 + (-100.39 + 100*m.x11)**2 + (-82.55 + 100*m.x12)**2 + 
                       (-18.5 + 100*m.x13)**2 + (-512.21 + m.x14)**2 + (-684.81 + m.x15)**2 + (-97.6 + 100*m.x16)**2 + (
                       -80.2 + 100*m.x17)**2 + (-20.05 + 100*m.x18)**2 + (-490.59 + m.x19)**2 + (-695.47 + m.x20)**2 + (
                       -101.29 + 100*m.x21)**2 + (-75.2 + 100*m.x22)**2 + (-24.2 + 100*m.x23)**2 + (-464.67 + m.x24)**2
                        + (-703.69 + m.x25)**2 + (-100.83 + 100*m.x26)**2 + (-71.93 + 100*m.x27)**2 + (-27.39 + 100*
                       m.x28)**2 + (-438.47 + m.x29)**2 + (-714.9 + m.x30)**2 + (-100.75 + 100*m.x31)**2 + (-68.61 + 100
                       *m.x32)**2 + (-32.15 + 100*m.x33)**2 + (-408.04 + m.x34)**2 + (-726.09 + m.x35)**2 + (-99.94 + 
                       100*m.x36)**2 + (-63.88 + 100*m.x37)**2 + (-37.41 + 100*m.x38)**2 + (-375.56 + m.x39)**2 + (-
                       735.44 + m.x40)**2 + (-100.07 + 100*m.x41)**2 + (-59.7 + 100*m.x42)**2 + (-39.26 + 100*m.x43)**2
                        + (-340.26 + m.x44)**2 + (-745.7 + m.x45)**2 + (-99.73 + 100*m.x46)**2 + (-55.8 + 100*m.x47)**2
                        + (-47.03 + 100*m.x48)**2 + (-306.55 + m.x49)**2 + (-753.94 + m.x50)**2, sense=minimize)

m.c2 = Constraint(expr=(-m.x53*m.x2) - 0.01*m.x2 + 0.01*m.x1 == 0)

m.c3 = Constraint(expr=(-m.x54*m.x7) - 0.01*m.x7 + 0.01*m.x6 == 0)

m.c4 = Constraint(expr=(-m.x55*m.x12) - 0.01*m.x12 + 0.01*m.x11 == 0)

m.c5 = Constraint(expr=(-m.x56*m.x17) - 0.01*m.x17 + 0.01*m.x16 == 0)

m.c6 = Constraint(expr=(-m.x57*m.x22) - 0.01*m.x22 + 0.01*m.x21 == 0)

m.c7 = Constraint(expr=(-m.x58*m.x27) - 0.01*m.x27 + 0.01*m.x26 == 0)

m.c8 = Constraint(expr=(-m.x59*m.x32) - 0.01*m.x32 + 0.01*m.x31 == 0)

m.c9 = Constraint(expr=(-m.x60*m.x37) - 0.01*m.x37 + 0.01*m.x36 == 0)

m.c10 = Constraint(expr=(-m.x61*m.x42) - 0.01*m.x42 + 0.01*m.x41 == 0)

m.c11 = Constraint(expr=(-m.x62*m.x47) - 0.01*m.x47 + 0.01*m.x46 == 0)

m.c12 = Constraint(expr=m.x53*m.x2 - 0.01*m.x3 == 0)

m.c13 = Constraint(expr=m.x54*m.x7 - 0.01*m.x8 == 0)

m.c14 = Constraint(expr=m.x55*m.x12 - 0.01*m.x13 == 0)

m.c15 = Constraint(expr=m.x56*m.x17 - 0.01*m.x18 == 0)

m.c16 = Constraint(expr=m.x57*m.x22 - 0.01*m.x23 == 0)

m.c17 = Constraint(expr=m.x58*m.x27 - 0.01*m.x28 == 0)

m.c18 = Constraint(expr=m.x59*m.x32 - 0.01*m.x33 == 0)

m.c19 = Constraint(expr=m.x60*m.x37 - 0.01*m.x38 == 0)

m.c20 = Constraint(expr=m.x61*m.x42 - 0.01*m.x43 == 0)

m.c21 = Constraint(expr=m.x62*m.x47 - 0.01*m.x48 == 0)

m.c22 = Constraint(expr=1000*m.x53*m.x2 + 0.01*m.x4 - 0.01*m.x5 == 0)

m.c23 = Constraint(expr=1000*m.x54*m.x7 + 0.01*m.x9 - 0.01*m.x10 == 0)

m.c24 = Constraint(expr=1000*m.x55*m.x12 + 0.01*m.x14 - 0.01*m.x15 == 0)

m.c25 = Constraint(expr=1000*m.x56*m.x17 + 0.01*m.x19 - 0.01*m.x20 == 0)

m.c26 = Constraint(expr=1000*m.x57*m.x22 + 0.01*m.x24 - 0.01*m.x25 == 0)

m.c27 = Constraint(expr=1000*m.x58*m.x27 + 0.01*m.x29 - 0.01*m.x30 == 0)

m.c28 = Constraint(expr=1000*m.x59*m.x32 + 0.01*m.x34 - 0.01*m.x35 == 0)

m.c29 = Constraint(expr=1000*m.x60*m.x37 + 0.01*m.x39 - 0.01*m.x40 == 0)

m.c30 = Constraint(expr=1000*m.x61*m.x42 + 0.01*m.x44 - 0.01*m.x45 == 0)

m.c31 = Constraint(expr=1000*m.x62*m.x47 + 0.01*m.x49 - 0.01*m.x50 == 0)

m.c32 = Constraint(expr=exp(-(-1 + 800/m.x5)*m.x52)*m.x51 - m.x53 == 0)

m.c33 = Constraint(expr=exp(-(-1 + 800/m.x10)*m.x52)*m.x51 - m.x54 == 0)

m.c34 = Constraint(expr=exp(-(-1 + 800/m.x15)*m.x52)*m.x51 - m.x55 == 0)

m.c35 = Constraint(expr=exp(-(-1 + 800/m.x20)*m.x52)*m.x51 - m.x56 == 0)

m.c36 = Constraint(expr=exp(-(-1 + 800/m.x25)*m.x52)*m.x51 - m.x57 == 0)

m.c37 = Constraint(expr=exp(-(-1 + 800/m.x30)*m.x52)*m.x51 - m.x58 == 0)

m.c38 = Constraint(expr=exp(-(-1 + 800/m.x35)*m.x52)*m.x51 - m.x59 == 0)

m.c39 = Constraint(expr=exp(-(-1 + 800/m.x40)*m.x52)*m.x51 - m.x60 == 0)

m.c40 = Constraint(expr=exp(-(-1 + 800/m.x45)*m.x52)*m.x51 - m.x61 == 0)

m.c41 = Constraint(expr=exp(-(-1 + 800/m.x50)*m.x52)*m.x51 - m.x62 == 0)
