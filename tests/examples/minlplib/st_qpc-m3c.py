#  NLP written by GAMS Convert at 04/21/18 13:54:25
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         11        1        0       10        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         11       11        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        108       98       10        0
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

m.obj = Objective(expr=10*m.x1 - 0.068*m.x1*m.x1 - 0.046*m.x1*m.x2 + 10*m.x2 - 0.079*m.x1*m.x3 + 10*m.x3 - 0.051*m.x1*
                       m.x4 + 10*m.x4 - 0.069*m.x1*m.x5 + 10*m.x5 - 0.068*m.x1*m.x6 + 10*m.x6 - 0.046*m.x1*m.x7 + 10*
                       m.x7 - 0.079*m.x1*m.x8 + 10*m.x8 - 0.051*m.x1*m.x9 + 10*m.x9 - 0.069*m.x1*m.x10 + 10*m.x10 - 
                       0.046*m.x2*m.x1 - 0.055*m.x2*m.x2 - 0.058*m.x2*m.x3 - 0.045*m.x2*m.x4 - 0.06*m.x2*m.x5 - 0.046*
                       m.x2*m.x6 - 0.055*m.x2*m.x7 - 0.058*m.x2*m.x8 - 0.045*m.x2*m.x9 - 0.06*m.x2*m.x10 - 0.079*m.x3*
                       m.x1 - 0.058*m.x3*m.x2 - 0.133*m.x3*m.x3 - 0.067*m.x3*m.x4 - 0.089*m.x3*m.x5 - 0.079*m.x3*m.x6 - 
                       0.058*m.x3*m.x7 - 0.133*m.x3*m.x8 - 0.067*m.x3*m.x9 - 0.089*m.x3*m.x10 - 0.051*m.x4*m.x1 - 0.045*
                       m.x4*m.x2 - 0.067*m.x4*m.x3 - 0.069*m.x4*m.x4 - 0.058*m.x4*m.x5 - 0.051*m.x4*m.x6 - 0.045*m.x4*
                       m.x7 - 0.067*m.x4*m.x8 - 0.069*m.x4*m.x9 - 0.058*m.x4*m.x10 - 0.069*m.x5*m.x1 - 0.06*m.x5*m.x2 - 
                       0.089*m.x5*m.x3 - 0.058*m.x5*m.x4 - 0.119*m.x5*m.x5 - 0.069*m.x5*m.x6 - 0.06*m.x5*m.x7 - 0.089*
                       m.x5*m.x8 - 0.058*m.x5*m.x9 - 0.119*m.x5*m.x10 - 0.068*m.x6*m.x1 - 0.046*m.x6*m.x2 - 0.079*m.x6*
                       m.x3 - 0.051*m.x6*m.x4 - 0.069*m.x6*m.x5 - 0.068*m.x6*m.x6 - 0.046*m.x6*m.x7 - 0.079*m.x6*m.x8 - 
                       0.051*m.x6*m.x9 - 0.069*m.x6*m.x10 - 0.046*m.x7*m.x1 - 0.055*m.x7*m.x2 - 0.058*m.x7*m.x3 - 0.045*
                       m.x7*m.x4 - 0.06*m.x7*m.x5 - 0.046*m.x7*m.x6 - 0.055*m.x7*m.x7 - 0.058*m.x7*m.x8 - 0.045*m.x7*
                       m.x9 - 0.06*m.x7*m.x10 - 0.079*m.x8*m.x1 - 0.058*m.x8*m.x2 - 0.133*m.x8*m.x3 - 0.067*m.x8*m.x4 - 
                       0.089*m.x8*m.x5 - 0.079*m.x8*m.x6 - 0.058*m.x8*m.x7 - 0.133*m.x8*m.x8 - 0.067*m.x8*m.x9 - 0.089*
                       m.x8*m.x10 - 0.051*m.x9*m.x1 - 0.045*m.x9*m.x2 - 0.067*m.x9*m.x3 - 0.069*m.x9*m.x4 - 0.058*m.x9*
                       m.x5 - 0.051*m.x9*m.x6 - 0.045*m.x9*m.x7 - 0.067*m.x9*m.x8 - 0.069*m.x9*m.x9 - 0.058*m.x9*m.x10
                        - 0.069*m.x10*m.x1 - 0.06*m.x10*m.x2 - 0.089*m.x10*m.x3 - 0.058*m.x10*m.x4 - 0.119*m.x10*m.x5 - 
                       0.069*m.x10*m.x6 - 0.06*m.x10*m.x7 - 0.089*m.x10*m.x8 - 0.058*m.x10*m.x9 - 0.119*m.x10*m.x10
                       , sense=minimize)

m.c1 = Constraint(expr=   20*m.x1 + 20*m.x2 + 60*m.x3 + 60*m.x4 + 60*m.x5 + 60*m.x6 + 5*m.x7 + 45*m.x8 + 55*m.x9
                        + 65*m.x10 <= 600.1)

m.c2 = Constraint(expr=   5*m.x1 + 7*m.x2 + 3*m.x3 + 8*m.x4 + 13*m.x5 + 13*m.x6 + 2*m.x7 + 14*m.x8 + 14*m.x9 + 14*m.x10
                        <= 310.5)

m.c3 = Constraint(expr=   100*m.x1 + 130*m.x2 + 50*m.x3 + 70*m.x4 + 70*m.x5 + 70*m.x6 + 20*m.x7 + 80*m.x8 + 80*m.x9
                        + 80*m.x10 <= 1800)

m.c4 = Constraint(expr=   200*m.x1 + 280*m.x2 + 100*m.x3 + 200*m.x4 + 250*m.x5 + 280*m.x6 + 100*m.x7 + 180*m.x8
                        + 200*m.x9 + 220*m.x10 <= 3850)

m.c5 = Constraint(expr=   2*m.x1 + 2*m.x2 + 4*m.x3 + 4*m.x4 + 4*m.x5 + 4*m.x6 + 2*m.x7 + 6*m.x8 + 6*m.x9 + 6*m.x10
                        <= 18.6)

m.c6 = Constraint(expr=   4*m.x1 + 8*m.x2 + 2*m.x3 + 6*m.x4 + 10*m.x5 + 10*m.x6 + 5*m.x7 + 10*m.x8 + 10*m.x9 + 10*m.x10
                        <= 198.7)

m.c7 = Constraint(expr=   60*m.x1 + 110*m.x2 + 20*m.x3 + 40*m.x4 + 60*m.x5 + 70*m.x6 + 10*m.x7 + 40*m.x8 + 50*m.x9
                        + 50*m.x10 <= 882)

m.c8 = Constraint(expr=   150*m.x1 + 210*m.x2 + 40*m.x3 + 70*m.x4 + 90*m.x5 + 105*m.x6 + 60*m.x7 + 100*m.x8 + 140*m.x9
                        + 180*m.x10 <= 4200)

m.c9 = Constraint(expr=   80*m.x1 + 100*m.x2 + 6*m.x3 + 16*m.x4 + 20*m.x5 + 22*m.x6 + 20*m.x8 + 30*m.x9 + 30*m.x10
                        <= 40.25)

m.c10 = Constraint(expr=   40*m.x1 + 40*m.x2 + 12*m.x3 + 20*m.x4 + 24*m.x5 + 28*m.x6 + 40*m.x9 + 50*m.x10 <= 327)
