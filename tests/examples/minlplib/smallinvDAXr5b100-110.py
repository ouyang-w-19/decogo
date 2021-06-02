#  MINLP written by GAMS Convert at 04/21/18 13:54:14
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          4        0        2        2        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         31        1        0       30        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        121       91       30        0


from pyomo.environ import *

model = m = ConcreteModel()


m.i1 = Var(within=Integers,bounds=(0,1E20),initialize=0)
m.i2 = Var(within=Integers,bounds=(0,1E20),initialize=0)
m.i3 = Var(within=Integers,bounds=(0,1E20),initialize=0)
m.i4 = Var(within=Integers,bounds=(0,1E20),initialize=0)
m.i5 = Var(within=Integers,bounds=(0,1E20),initialize=0)
m.i6 = Var(within=Integers,bounds=(0,1E20),initialize=0)
m.i7 = Var(within=Integers,bounds=(0,1E20),initialize=0)
m.i8 = Var(within=Integers,bounds=(0,1E20),initialize=0)
m.i9 = Var(within=Integers,bounds=(0,1E20),initialize=0)
m.i10 = Var(within=Integers,bounds=(0,1E20),initialize=0)
m.i11 = Var(within=Integers,bounds=(0,1E20),initialize=0)
m.i12 = Var(within=Integers,bounds=(0,1E20),initialize=0)
m.i13 = Var(within=Integers,bounds=(0,1E20),initialize=0)
m.i14 = Var(within=Integers,bounds=(0,1E20),initialize=0)
m.i15 = Var(within=Integers,bounds=(0,1E20),initialize=0)
m.i16 = Var(within=Integers,bounds=(0,1E20),initialize=0)
m.i17 = Var(within=Integers,bounds=(0,1E20),initialize=0)
m.i18 = Var(within=Integers,bounds=(0,1E20),initialize=0)
m.i19 = Var(within=Integers,bounds=(0,1E20),initialize=0)
m.i20 = Var(within=Integers,bounds=(0,1E20),initialize=0)
m.i21 = Var(within=Integers,bounds=(0,1E20),initialize=0)
m.i22 = Var(within=Integers,bounds=(0,1E20),initialize=0)
m.i23 = Var(within=Integers,bounds=(0,1E20),initialize=0)
m.i24 = Var(within=Integers,bounds=(0,1E20),initialize=0)
m.i25 = Var(within=Integers,bounds=(0,1E20),initialize=0)
m.i26 = Var(within=Integers,bounds=(0,1E20),initialize=0)
m.i27 = Var(within=Integers,bounds=(0,1E20),initialize=0)
m.i28 = Var(within=Integers,bounds=(0,1E20),initialize=0)
m.i29 = Var(within=Integers,bounds=(0,1E20),initialize=0)
m.i30 = Var(within=Integers,bounds=(0,1E20),initialize=0)
m.x31 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=m.x31, sense=minimize)

m.c1 = Constraint(expr=0.00558391*m.i1**2 + 0.0103737*m.i2**2 + 0.0221075*m.i3**2 + 0.00399551*m.i4**2 + 0.00267064*m.i5
                       **2 + 0.00516451*m.i6**2 + 0.00421051*m.i7**2 + 0.00368008*m.i8**2 + 0.00372788*m.i9**2 + 
                       0.00668969*m.i10**2 + 0.00613034*m.i11**2 + 0.0129271*m.i12**2 + 0.00697595*m.i13**2 + 0.0104282*
                       m.i14**2 + 0.00899168*m.i15**2 + 0.0206685*m.i16**2 + 0.0488863*m.i17**2 + 0.00894867*m.i18**2 + 
                       0.0124118*m.i19**2 + 0.0122291*m.i20**2 + 0.0128973*m.i21**2 + 0.00668043*m.i22**2 + 0.0153425*
                       m.i23**2 + 0.0128605*m.i24**2 + 0.00718697*m.i25**2 + 0.0102616*m.i26**2 + 0.0123235*m.i27**2 + 
                       0.00569465*m.i28**2 + 0.00818114*m.i29**2 + 0.00469456*m.i30**2 + 0.00901964*m.i1*m.i2 + 
                       0.00860972*m.i1*m.i3 + 0.00248004*m.i1*m.i4 + 0.001821292*m.i1*m.i5 + 0.00561078*m.i1*m.i6 + 
                       0.0051287*m.i1*m.i7 + 0.000691196*m.i1*m.i8 + 0.000805982*m.i1*m.i9 + 0.00531452*m.i1*m.i10 + 
                       0.00556768*m.i1*m.i11 + 0.00745224*m.i1*m.i12 + 0.00478224*m.i1*m.i13 + 0.00610824*m.i1*m.i14 + 
                       0.00577634*m.i1*m.i15 + 0.00613326*m.i1*m.i16 + 0.01432596*m.i1*m.i17 + 0.007501*m.i1*m.i18 + 
                       0.00716212*m.i1*m.i19 + 0.00512922*m.i1*m.i20 + 0.0087283*m.i1*m.i21 + 0.00245846*m.i1*m.i22 + 
                       0.0071572*m.i1*m.i23 + 0.00543966*m.i1*m.i24 + 0.00708258*m.i1*m.i25 + 0.00243422*m.i1*m.i26 + 
                       0.00729094*m.i1*m.i27 + 0.00386642*m.i1*m.i28 + 0.0061908*m.i1*m.i29 + 0.00366754*m.i1*m.i30 + 
                       0.01583972*m.i2*m.i3 + 0.00394608*m.i2*m.i4 + 0.001773554*m.i2*m.i5 + 0.00861376*m.i2*m.i6 + 
                       0.00604454*m.i2*m.i7 + 0.00312866*m.i2*m.i8 + 0.00184686*m.i2*m.i9 + 0.00924638*m.i2*m.i10 + 
                       0.01131902*m.i2*m.i11 + 0.01253232*m.i2*m.i12 + 0.00675858*m.i2*m.i13 + 0.00804604*m.i2*m.i14 + 
                       0.00869872*m.i2*m.i15 + 0.0094047*m.i2*m.i16 + 0.0251538*m.i2*m.i17 + 0.01321532*m.i2*m.i18 + 
                       0.01127964*m.i2*m.i19 + 0.0096635*m.i2*m.i20 + 0.0160783*m.i2*m.i21 + 0.00271*m.i2*m.i22 + 
                       0.01486022*m.i2*m.i23 + 0.01091018*m.i2*m.i24 + 0.01009426*m.i2*m.i25 + 0.00754144*m.i2*m.i26 + 
                       0.01408844*m.i2*m.i27 + 0.00544162*m.i2*m.i28 + 0.01096178*m.i2*m.i29 + 0.00574964*m.i2*m.i30 + 
                       0.00299428*m.i3*m.i4 + 0.001239314*m.i3*m.i5 + 0.01256412*m.i3*m.i6 + 0.00899714*m.i3*m.i7 + 
                       0.00444448*m.i3*m.i8 + 0.00616612*m.i3*m.i9 + 0.0146019*m.i3*m.i10 + 0.01249836*m.i3*m.i11 + 
                       0.0264968*m.i3*m.i12 + 0.01266506*m.i3*m.i13 + 0.01358566*m.i3*m.i14 + 0.01419766*m.i3*m.i15 + 
                       0.01033796*m.i3*m.i16 + 0.040104*m.i3*m.i17 + 0.01504214*m.i3*m.i18 + 0.0210518*m.i3*m.i19 + 
                       0.0169342*m.i3*m.i20 + 0.020394*m.i3*m.i21 + 0.006361*m.i3*m.i22 + 0.0173249*m.i3*m.i23 + 
                       0.01157254*m.i3*m.i24 + 0.01601196*m.i3*m.i25 + 0.01305808*m.i3*m.i26 + 0.018918*m.i3*m.i27 + 
                       0.0100768*m.i3*m.i28 + 0.01415258*m.i3*m.i29 + 0.00890208*m.i3*m.i30 + 0.00365082*m.i4*m.i5 + 
                       0.0031533*m.i4*m.i6 + 0.001664882*m.i4*m.i7 + 0.000487746*m.i4*m.i8 + 0.00074873*m.i4*m.i9 + 
                       0.00279536*m.i4*m.i10 + 0.000948078*m.i4*m.i11 + 0.00218644*m.i4*m.i12 + 0.001471884*m.i4*m.i13
                        + 0.001764448*m.i4*m.i14 + 0.001707856*m.i4*m.i15 + 0.00415534*m.i4*m.i16 + 0.00552118*m.i4*
                       m.i17 + 0.00298928*m.i4*m.i18 + 0.000446818*m.i4*m.i19 + 0.0042709*m.i4*m.i20 + 0.00437068*m.i4*
                       m.i21 + 0.001584414*m.i4*m.i22 + 0.0028495*m.i4*m.i23 + 0.00550266*m.i4*m.i24 + 0.0019381*m.i4*
                       m.i25 - 0.000779792*m.i4*m.i26 + 0.00383714*m.i4*m.i27 + 0.00170793*m.i4*m.i28 + 0.00220852*m.i4*
                       m.i29 + 0.001897386*m.i4*m.i30 + 0.00226608*m.i5*m.i6 + 0.001391572*m.i5*m.i7 + 0.001434726*m.i5*
                       m.i8 + 0.000718962*m.i5*m.i9 + 0.00117417*m.i5*m.i10 + 0.001240914*m.i5*m.i11 + 0.000587866*m.i5*
                       m.i12 + 0.0020154*m.i5*m.i13 + 0.00126883*m.i5*m.i14 + 0.000645164*m.i5*m.i15 + 0.0001425196*m.i5
                       *m.i16 + 0.001199014*m.i5*m.i17 + 0.001896292*m.i5*m.i18 - 0.000289412*m.i5*m.i19 + 0.001457998*
                       m.i5*m.i20 + 0.00199702*m.i5*m.i21 + 0.001266598*m.i5*m.i22 + 0.000764624*m.i5*m.i23 + 
                       0.001961312*m.i5*m.i24 + 0.001748826*m.i5*m.i25 - 0.00122625*m.i5*m.i26 + 0.000753266*m.i5*m.i27
                        + 0.00063941*m.i5*m.i28 + 0.001644068*m.i5*m.i29 + 0.001587886*m.i5*m.i30 + 0.00454154*m.i6*m.i7
                        + 0.001157686*m.i6*m.i8 + 0.0032018*m.i6*m.i9 + 0.00727798*m.i6*m.i10 + 0.0064553*m.i6*m.i11 + 
                       0.00791618*m.i6*m.i12 + 0.00687526*m.i6*m.i13 + 0.00638032*m.i6*m.i14 + 0.00425538*m.i6*m.i15 + 
                       0.00583332*m.i6*m.i16 + 0.01491304*m.i6*m.i17 + 0.00876772*m.i6*m.i18 + 0.00814434*m.i6*m.i19 + 
                       0.00549208*m.i6*m.i20 + 0.0103848*m.i6*m.i21 + 0.001352278*m.i6*m.i22 + 0.0063097*m.i6*m.i23 + 
                       0.0052012*m.i6*m.i24 + 0.00808494*m.i6*m.i25 + 0.00595234*m.i6*m.i26 + 0.00960786*m.i6*m.i27 + 
                       0.0035648*m.i6*m.i28 + 0.00730486*m.i6*m.i29 + 0.0036145*m.i6*m.i30 + 0.0027426*m.i7*m.i8 + 
                       0.00224138*m.i7*m.i9 + 0.00558948*m.i7*m.i10 + 0.00489378*m.i7*m.i11 + 0.0073565*m.i7*m.i12 + 
                       0.0050794*m.i7*m.i13 + 0.00363244*m.i7*m.i14 + 0.00634576*m.i7*m.i15 + 0.001588982*m.i7*m.i16 + 
                       0.00877926*m.i7*m.i17 + 0.00710862*m.i7*m.i18 + 0.00675396*m.i7*m.i19 + 0.00621206*m.i7*m.i20 + 
                       0.00746652*m.i7*m.i21 + 0.001927036*m.i7*m.i22 + 0.00410122*m.i7*m.i23 + 0.00344774*m.i7*m.i24 + 
                       0.00594546*m.i7*m.i25 + 0.00461784*m.i7*m.i26 + 0.00530234*m.i7*m.i27 + 0.00320122*m.i7*m.i28 + 
                       0.00474356*m.i7*m.i29 + 0.00341222*m.i7*m.i30 + 0.00105347*m.i8*m.i9 + 0.001879822*m.i8*m.i10 + 
                       0.00290244*m.i8*m.i11 + 0.00353818*m.i8*m.i12 + 0.0035513*m.i8*m.i13 + 0.00294406*m.i8*m.i14 + 
                       0.00389942*m.i8*m.i15 + 0.00286866*m.i8*m.i16 + 0.000920126*m.i8*m.i17 + 0.00274282*m.i8*m.i18 + 
                       0.0027675*m.i8*m.i19 + 0.00464592*m.i8*m.i20 + 0.001093444*m.i8*m.i21 + 0.000948594*m.i8*m.i22 + 
                       0.00275316*m.i8*m.i23 + 0.001626794*m.i8*m.i24 + 0.00209498*m.i8*m.i25 + 0.0031962*m.i8*m.i26 + 
                       0.001767658*m.i8*m.i27 + 0.00109948*m.i8*m.i28 + 0.00292004*m.i8*m.i29 + 0.00215496*m.i8*m.i30 + 
                       0.00329222*m.i9*m.i10 + 0.00239978*m.i9*m.i11 + 0.00365066*m.i9*m.i12 + 0.00463422*m.i9*m.i13 + 
                       0.00260888*m.i9*m.i14 + 0.00330432*m.i9*m.i15 + 0.000950274*m.i9*m.i16 + 0.00309664*m.i9*m.i17 + 
                       0.00325462*m.i9*m.i18 + 0.00494078*m.i9*m.i19 + 0.00339202*m.i9*m.i20 + 0.00283784*m.i9*m.i21 + 
                       0.001862472*m.i9*m.i22 + 0.001457294*m.i9*m.i23 + 0.000292408*m.i9*m.i24 + 0.00434258*m.i9*m.i25
                        + 0.0051917*m.i9*m.i26 + 0.00442724*m.i9*m.i27 + 0.00235362*m.i9*m.i28 + 0.0023207*m.i9*m.i29 + 
                       0.00232972*m.i9*m.i30 + 0.00661128*m.i10*m.i11 + 0.0099349*m.i10*m.i12 + 0.00670728*m.i10*m.i13
                        + 0.00688756*m.i10*m.i14 + 0.00814804*m.i10*m.i15 + 0.00387536*m.i10*m.i16 + 0.01709622*m.i10*
                       m.i17 + 0.00921546*m.i10*m.i18 + 0.01138012*m.i10*m.i19 + 0.0073598*m.i10*m.i20 + 0.012047*m.i10*
                       m.i21 + 0.001953884*m.i10*m.i22 + 0.01110682*m.i10*m.i23 + 0.00744232*m.i10*m.i24 + 0.00846572*
                       m.i10*m.i25 + 0.00811902*m.i10*m.i26 + 0.01093528*m.i10*m.i27 + 0.00642736*m.i10*m.i28 + 
                       0.00817838*m.i10*m.i29 + 0.00467066*m.i10*m.i30 + 0.01089978*m.i11*m.i12 + 0.00580646*m.i11*m.i13
                        + 0.00479126*m.i11*m.i14 + 0.00655088*m.i11*m.i15 + 0.00784072*m.i11*m.i16 + 0.0171429*m.i11*
                       m.i17 + 0.0099023*m.i11*m.i18 + 0.00881158*m.i11*m.i19 + 0.0065332*m.i11*m.i20 + 0.01111462*m.i11
                       *m.i21 + 0.00238226*m.i11*m.i22 + 0.00942038*m.i11*m.i23 + 0.00509366*m.i11*m.i24 + 0.0079177*
                       m.i11*m.i25 + 0.00653764*m.i11*m.i26 + 0.00963386*m.i11*m.i27 + 0.00518254*m.i11*m.i28 + 
                       0.00839924*m.i11*m.i29 + 0.00396162*m.i11*m.i30 + 0.00812884*m.i12*m.i13 + 0.00932748*m.i12*m.i14
                        + 0.01172114*m.i12*m.i15 + 0.00937084*m.i12*m.i16 + 0.033621*m.i12*m.i17 + 0.0125625*m.i12*m.i18
                        + 0.01635358*m.i12*m.i19 + 0.01460644*m.i12*m.i20 + 0.01374474*m.i12*m.i21 + 0.00526496*m.i12*
                       m.i22 + 0.01402198*m.i12*m.i23 + 0.00931776*m.i12*m.i24 + 0.01195866*m.i12*m.i25 + 0.00822682*
                       m.i12*m.i26 + 0.01241788*m.i12*m.i27 + 0.00706034*m.i12*m.i28 + 0.01219462*m.i12*m.i29 + 
                       0.00598988*m.i12*m.i30 + 0.0068538*m.i13*m.i14 + 0.00620178*m.i13*m.i15 + 0.00379406*m.i13*m.i16
                        + 0.00889862*m.i13*m.i17 + 0.00816594*m.i13*m.i18 + 0.01033824*m.i13*m.i19 + 0.00577162*m.i13*
                       m.i20 + 0.00736548*m.i13*m.i21 + 0.00410776*m.i13*m.i22 + 0.00580558*m.i13*m.i23 + 0.00459074*
                       m.i13*m.i24 + 0.0072167*m.i13*m.i25 + 0.00956086*m.i13*m.i26 + 0.00943468*m.i13*m.i27 + 
                       0.00587164*m.i13*m.i28 + 0.00902842*m.i13*m.i29 + 0.00550608*m.i13*m.i30 + 0.00635356*m.i14*m.i15
                        + 0.00709628*m.i14*m.i16 + 0.01555038*m.i14*m.i17 + 0.00826722*m.i14*m.i18 + 0.00751614*m.i14*
                       m.i19 + 0.00814342*m.i14*m.i20 + 0.00995652*m.i14*m.i21 + 0.00477798*m.i14*m.i22 + 0.0076843*
                       m.i14*m.i23 + 0.00817698*m.i14*m.i24 + 0.00886056*m.i14*m.i25 + 0.00579636*m.i14*m.i26 + 
                       0.01128084*m.i14*m.i27 + 0.00483444*m.i14*m.i28 + 0.0068342*m.i14*m.i29 + 0.0077372*m.i14*m.i30
                        + 0.00973548*m.i15*m.i16 + 0.01556958*m.i15*m.i17 + 0.00926266*m.i15*m.i18 + 0.01281188*m.i15*
                       m.i19 + 0.00669072*m.i15*m.i20 + 0.00937684*m.i15*m.i21 + 0.00639856*m.i15*m.i22 + 0.00611934*
                       m.i15*m.i23 + 0.00853942*m.i15*m.i24 + 0.00964296*m.i15*m.i25 + 0.00704584*m.i15*m.i26 + 
                       0.0119279*m.i15*m.i27 + 0.00648174*m.i15*m.i28 + 0.01050128*m.i15*m.i29 + 0.00502696*m.i15*m.i30
                        + 0.01809222*m.i16*m.i17 + 0.00823288*m.i16*m.i18 + 0.01161214*m.i16*m.i19 + 0.00533676*m.i16*
                       m.i20 + 0.01233794*m.i16*m.i21 + 0.00512778*m.i16*m.i22 + 0.00722276*m.i16*m.i23 + 0.01715638*
                       m.i16*m.i24 + 0.00677738*m.i16*m.i25 + 0.0069565*m.i16*m.i26 + 0.01691522*m.i16*m.i27 + 
                       0.00246824*m.i16*m.i28 + 0.00934088*m.i16*m.i29 + 0.00393866*m.i16*m.i30 + 0.01858542*m.i17*m.i18
                        + 0.0224912*m.i17*m.i19 + 0.01793624*m.i17*m.i20 + 0.0270204*m.i17*m.i21 + 0.01083832*m.i17*
                       m.i22 + 0.0216678*m.i17*m.i23 + 0.0183347*m.i17*m.i24 + 0.01893*m.i17*m.i25 + 0.01089098*m.i17*
                       m.i26 + 0.0209142*m.i17*m.i27 + 0.01273162*m.i17*m.i28 + 0.0200902*m.i17*m.i29 + 0.00774366*m.i17
                       *m.i30 + 0.01171594*m.i18*m.i19 + 0.00861454*m.i18*m.i20 + 0.01414322*m.i18*m.i21 + 0.001961404*
                       m.i18*m.i22 + 0.00910214*m.i18*m.i23 + 0.01003468*m.i18*m.i24 + 0.0094743*m.i18*m.i25 + 
                       0.00825794*m.i18*m.i26 + 0.01336058*m.i18*m.i27 + 0.00607998*m.i18*m.i28 + 0.01070732*m.i18*m.i29
                        + 0.00492858*m.i18*m.i30 + 0.0082848*m.i19*m.i20 + 0.0126004*m.i19*m.i21 + 0.00407366*m.i19*
                       m.i22 + 0.01381284*m.i19*m.i23 + 0.00838908*m.i19*m.i24 + 0.01198264*m.i19*m.i25 + 0.01583126*
                       m.i19*m.i26 + 0.01664044*m.i19*m.i27 + 0.00924324*m.i19*m.i28 + 0.01214842*m.i19*m.i29 + 
                       0.00592778*m.i19*m.i30 + 0.01071434*m.i20*m.i21 + 0.00296964*m.i20*m.i22 + 0.00736528*m.i20*m.i23
                        + 0.00606396*m.i20*m.i24 + 0.00628822*m.i20*m.i25 + 0.00817696*m.i20*m.i26 + 0.00776894*m.i20*
                       m.i27 + 0.0026202*m.i20*m.i28 + 0.00717342*m.i20*m.i29 + 0.00579184*m.i20*m.i30 + 0.00469936*
                       m.i21*m.i22 + 0.0138599*m.i21*m.i23 + 0.0125037*m.i21*m.i24 + 0.01211002*m.i21*m.i25 + 0.00836436
                       *m.i21*m.i26 + 0.016494*m.i21*m.i27 + 0.00602872*m.i21*m.i28 + 0.01180462*m.i21*m.i29 + 
                       0.00570478*m.i21*m.i30 + 0.0032176*m.i22*m.i23 + 0.00379112*m.i22*m.i24 + 0.00301976*m.i22*m.i25
                        + 0.00308424*m.i22*m.i26 + 0.00369962*m.i22*m.i27 + 0.00278784*m.i22*m.i28 + 0.00465846*m.i22*
                       m.i29 + 0.00297212*m.i22*m.i30 + 0.01019176*m.i23*m.i24 + 0.00779098*m.i23*m.i25 + 0.00577776*
                       m.i23*m.i26 + 0.01267514*m.i23*m.i27 + 0.00735432*m.i23*m.i28 + 0.00786386*m.i23*m.i29 + 
                       0.00559972*m.i23*m.i30 + 0.00725022*m.i24*m.i25 + 0.00455648*m.i24*m.i26 + 0.0157223*m.i24*m.i27
                        + 0.00579512*m.i24*m.i28 + 0.00792398*m.i24*m.i29 + 0.0045755*m.i24*m.i30 + 0.00723442*m.i25*
                       m.i26 + 0.01196012*m.i25*m.i27 + 0.0063273*m.i25*m.i28 + 0.0099815*m.i25*m.i29 + 0.0041794*m.i25*
                       m.i30 + 0.01139894*m.i26*m.i27 + 0.0080092*m.i26*m.i28 + 0.0080044*m.i26*m.i29 + 0.00493602*m.i26
                       *m.i30 + 0.00826208*m.i27*m.i28 + 0.01246152*m.i27*m.i29 + 0.0067556*m.i27*m.i30 + 0.00575648*
                       m.i28*m.i29 + 0.0044929*m.i28*m.i30 + 0.00469952*m.i29*m.i30 - m.x31 <= 0)

m.c2 = Constraint(expr=   0.00218236*m.i1 - 0.00115175*m.i2 - 0.00795114*m.i3 + 0.011626*m.i4 + 0.0084202*m.i5
                        + 0.00496825*m.i6 + 0.00254677*m.i7 - 0.00234318*m.i8 - 0.00770481*m.i9 - 0.00223195*m.i10
                        - 0.00151299*m.i11 - 0.00448068*m.i12 + 0.00386372*m.i13 - 0.0112346*m.i14 - 0.00311219*m.i15
                        + 0.00357072*m.i16 - 0.00928342*m.i17 - 0.00268175*m.i18 - 0.00631856*m.i19 - 0.00211388*m.i20
                        + 0.0132599*m.i21 + 0.00445572*m.i22 + 0.0067442*m.i23 + 0.0185808*m.i24 + 0.00160132*m.i25
                        - 0.00624596*m.i26 + 0.00206*m.i27 + 0.00229918*m.i28 + 0.00165023*m.i29 + 0.0035383*m.i30 >= 0)

m.c3 = Constraint(expr=   39.19*m.i1 + 41.47*m.i2 + 5.71*m.i3 + 53.59*m.i4 + 43.65*m.i5 + 85.46*m.i6 + 39.7*m.i7
                        + 44.91*m.i8 + 9.6*m.i9 + 11.26*m.i10 + 39.56*m.i11 + 46*m.i12 + 45.25*m.i13 + 21.9*m.i14
                        + 11.85*m.i15 + 37.4*m.i16 + 4.75*m.i17 + 44.44*m.i18 + 80.5*m.i19 + 49.46*m.i20 + 67.02*m.i21
                        + 59.25*m.i22 + 71.5*m.i23 + 48.8*m.i24 + 73.22*m.i25 + 101.9*m.i26 + 20.06*m.i27 + 36.33*m.i28
                        + 41.31*m.i29 + 53.09*m.i30 >= 10000)

m.c4 = Constraint(expr=   39.19*m.i1 + 41.47*m.i2 + 5.71*m.i3 + 53.59*m.i4 + 43.65*m.i5 + 85.46*m.i6 + 39.7*m.i7
                        + 44.91*m.i8 + 9.6*m.i9 + 11.26*m.i10 + 39.56*m.i11 + 46*m.i12 + 45.25*m.i13 + 21.9*m.i14
                        + 11.85*m.i15 + 37.4*m.i16 + 4.75*m.i17 + 44.44*m.i18 + 80.5*m.i19 + 49.46*m.i20 + 67.02*m.i21
                        + 59.25*m.i22 + 71.5*m.i23 + 48.8*m.i24 + 73.22*m.i25 + 101.9*m.i26 + 20.06*m.i27 + 36.33*m.i28
                        + 41.31*m.i29 + 53.09*m.i30 <= 11000)
