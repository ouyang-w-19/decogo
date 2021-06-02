#  NLP written by GAMS Convert at 04/21/18 13:51:43
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          6        2        0        4        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          5        5        0        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         20        8       12        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(1E-6,1),initialize=0.937)
m.x2 = Var(within=Reals,bounds=(1E-6,1),initialize=1E-6)
m.x3 = Var(within=Reals,bounds=(60,100),initialize=80.166)
m.x5 = Var(within=Reals,bounds=(0,None),initialize=0)

m.obj = Objective(expr=   m.x5, sense=minimize)

m.c2 = Constraint(expr=0.361872516756437*m.x2/(m.x1 + 0.888649896608059*m.x2) + 0.868134622480909*m.x2/(
                       0.696880695582072*m.x1 + m.x2) - (0.361872516756437*m.x1*m.x2/(m.x1 + 0.888649896608059*m.x2)**2
                        + 0.604986259573375*m.x2*m.x1/(0.696880695582072*m.x1 + m.x2)**2) - 2755.64173589155/(219.161 + 
                       m.x3) - m.x5 <= -9.20816767045657)

m.c3 = Constraint(expr=0.868134622480909*m.x1/(0.696880695582072*m.x1 + m.x2) + 0.361872516756437*m.x1/(m.x1 + 
                       0.888649896608059*m.x2) - (0.321577974600906*m.x1*m.x2/(m.x1 + 0.888649896608059*m.x2)**2 + 
                       0.868134622480909*m.x2*m.x1/(0.696880695582072*m.x1 + m.x2)**2) - 4117.06819797521/(227.438 + 
                       m.x3) - m.x5 <= -12.6599269316621)

m.c4 = Constraint(expr=(-0.361872516756437*m.x2/(m.x1 + 0.888649896608059*m.x2)) - 0.868134622480909*m.x2/(
                       0.696880695582072*m.x1 + m.x2) + 0.361872516756437*m.x1*m.x2/(m.x1 + 0.888649896608059*m.x2)**2
                        + 0.604986259573375*m.x2*m.x1/(0.696880695582072*m.x1 + m.x2)**2 + 2755.64173589155/(219.161 + 
                       m.x3) - m.x5 <= 9.20816767045657)

m.c5 = Constraint(expr=(-0.868134622480909*m.x1/(0.696880695582072*m.x1 + m.x2)) - 0.361872516756437*m.x1/(m.x1 + 
                       0.888649896608059*m.x2) + 0.321577974600906*m.x1*m.x2/(m.x1 + 0.888649896608059*m.x2)**2 + 
                       0.868134622480909*m.x2*m.x1/(0.696880695582072*m.x1 + m.x2)**2 + 4117.06819797521/(227.438 + m.x3
                       ) - m.x5 <= 12.6599269316621)

m.c6 = Constraint(expr=   m.x1 + m.x2 == 1)
