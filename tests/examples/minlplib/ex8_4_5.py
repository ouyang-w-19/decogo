#  NLP written by GAMS Convert at 04/21/18 13:51:47
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         12       12        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         16       16        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         67       12       55        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0.1757,0.2157),initialize=0.18256988528)
m.x2 = Var(within=Reals,bounds=(0.1747,0.2147),initialize=0.20843066832)
m.x3 = Var(within=Reals,bounds=(0.1535,0.1935),initialize=0.17551501424)
m.x4 = Var(within=Reals,bounds=(0.14,0.18),initialize=0.15204551616)
m.x5 = Var(within=Reals,bounds=(0.0644,0.1044),initialize=0.07608848468)
m.x6 = Var(within=Reals,bounds=(0.0427,0.0827),initialize=0.05166211468)
m.x7 = Var(within=Reals,bounds=(0.0256,0.0656),initialize=0.03959322016)
m.x8 = Var(within=Reals,bounds=(0.0142,0.0542),initialize=0.04845081388)
m.x9 = Var(within=Reals,bounds=(0.0123,0.0523),initialize=0.01498454892)
m.x10 = Var(within=Reals,bounds=(0.0035,0.0435),initialize=0.02350842676)
m.x11 = Var(within=Reals,bounds=(0.0046,0.0446),initialize=0.04452470508)
m.x12 = Var(within=Reals,bounds=(-0.2892,0.2893),initialize=0.045597259173)
m.x13 = Var(within=Reals,bounds=(-0.2892,0.2893),initialize=0.2841704630615)
m.x14 = Var(within=Reals,bounds=(-0.2892,0.2893),initialize=0.1517618951595)
m.x15 = Var(within=Reals,bounds=(-0.2892,0.2893),initialize=-0.2135943985845)

m.obj = Objective(expr=(-0.1957 + m.x1)**2 + (-0.1947 + m.x2)**2 + (-0.1735 + m.x3)**2 + (-0.16 + m.x4)**2 + (-0.0844 + 
                       m.x5)**2 + (-0.0627 + m.x6)**2 + (-0.0456 + m.x7)**2 + (-0.0342 + m.x8)**2 + (-0.0323 + m.x9)**2
                        + (-0.0235 + m.x10)**2 + (-0.0246 + m.x11)**2, sense=minimize)

m.c2 = Constraint(expr=m.x12*(16 + 4*m.x13)/(16 + 4*m.x14 + m.x15) - m.x1 == 0)

m.c3 = Constraint(expr=m.x12*(4 + 2*m.x13)/(4 + 2*m.x14 + m.x15) - m.x2 == 0)

m.c4 = Constraint(expr=m.x12*(1 + m.x13)/(1 + m.x14 + m.x15) - m.x3 == 0)

m.c5 = Constraint(expr=m.x12*(0.25 + 0.5*m.x13)/(0.25 + 0.5*m.x14 + m.x15) - m.x4 == 0)

m.c6 = Constraint(expr=m.x12*(0.0625 + 0.25*m.x13)/(0.0625 + 0.25*m.x14 + m.x15) - m.x5 == 0)

m.c7 = Constraint(expr=m.x12*(0.0277777777777778 + 0.166666666666667*m.x13)/(0.0277777777777778 + 0.166666666666667*
                       m.x14 + m.x15) - m.x6 == 0)

m.c8 = Constraint(expr=m.x12*(0.015625 + 0.125*m.x13)/(0.015625 + 0.125*m.x14 + m.x15) - m.x7 == 0)

m.c9 = Constraint(expr=m.x12*(0.01 + 0.1*m.x13)/(0.01 + 0.1*m.x14 + m.x15) - m.x8 == 0)

m.c10 = Constraint(expr=m.x12*(0.00694444444444444 + 0.0833333333333333*m.x13)/(0.00694444444444444 + 0.0833333333333333
                        *m.x14 + m.x15) - m.x9 == 0)

m.c11 = Constraint(expr=m.x12*(0.00510204081632653 + 0.0714285714285714*m.x13)/(0.00510204081632653 + 0.0714285714285714
                        *m.x14 + m.x15) - m.x10 == 0)

m.c12 = Constraint(expr=m.x12*(0.00390625 + 0.0625*m.x13)/(0.00390625 + 0.0625*m.x14 + m.x15) - m.x11 == 0)
