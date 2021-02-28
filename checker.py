#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Author: Andrea Ceolin
February 2021

This script can be used to check if the implications of the parametric structure are violated.
It takes the name of the dataset as its argument, and prints a list of mistakes for each language.
If the output file only contains the list of languages, it means that no mistake has been found.
'''

################
###TABLEA CHECKER
#################

import sys

def check_power(P):
    x = [P[0]]
    FGM = P[1]
    FGA = P[2]
    FGK = P[3]
    SPK = P[4]
    FGP = P[5]
    FSP = P[6]
    FGN = P[7]
    SCO = P[8]
    GDP = P[9]
    FSN = P[10]
    FNN = P[11]
    FGT = P[12]
    FGG = P[13]
    FSG = P[14]
    CGB = P[15]
    FPC = P[16]
    DGR = P[17]
    DGP = P[18]
    CGR = P[19]
    NWD = P[20]
    FVP = P[21]
    DGD = P[22]
    DPQ = P[23]
    DCN = P[24]
    DNN = P[25]
    DIN = P[26]
    FGC = P[27]
    FGE = P[28]
    FCN = P[29]
    HMP = P[30]
    ARR = P[31]
    GCN = P[32]
    GFN = P[33]
    GFP = P[34]
    GP3 = P[35]
    GEI = P[36]
    CSE = P[37]
    EAL = P[38]
    CAL = P[39]
    LKA = P[40]
    LKO = P[41]
    LKP = P[42]
    DMP = P[43]
    DMG = P[44]
    GUN = P[45]
    GAD = P[46]
    GFL = P[47]
    PGL = P[48]
    GGH = P[49]
    GSI = P[50]
    ALP = P[51]
    GIT = P[52]
    UST = P[53]
    GPC = P[54]
    PSC = P[55]
    PCA = P[56]
    PMN = P[57]
    RHM = P[58]
    FRC = P[59]
    NRC = P[60]
    DOR = P[61]
    FFP = P[62]
    NUP = P[63]
    PNP = P[64]
    NUD = P[65]
    NUC = P[66]
    NM1 = P[67]
    NM2 = P[68]
    NUA = P[69]
    NGL = P[70]
    EAF = P[71]
    ACM = P[72]
    DSN = P[73]
    DSA = P[74]
    DSS = P[75]
    DOC = P[76]
    NEX = P[77]
    PEX = P[78]
    FEX = P[79]
    PDC = P[80]
    PCL = P[81]
    APO = P[82]
    WAP = P[83]
    AGE = P[84]
    OPK = P[85]
    TSP = P[86]
    TDP = P[87]
    TDC = P[88]
    TSA = P[89]
    TAR = P[90]
    TLC = P[91]
    TND = P[92]
    TDA = P[93]
    TNL = P[94]

    par = [[FGM, True],
           [FGA, FGM == "+"],
           [FGK, FGM == "+"],
           [SPK, FGK == "+"],
           [FGP, FGM == "+"],
           [FSP, FGP != "+"],
           [FGN, FGP == "+"],
           [SCO, FGM == '+' and FGN != "+"],
           [GDP, FGM == "+" and FGN != "+"],
           [FSN, FGN == "+"],
           [FNN, FSN == "+"],
           [FGT, True],
           [FGG, FGN == "+"],
           [FSG, FGN == "+"],
           [CGB, True],
           [FPC, True],
           [DGR, FPC == "-" and FGN == "+"],
           [DGP, DGR != "+"],
           [CGR, CGB == "-" and DGR == "+"],
           [NWD, FGP == "+" and (FSN == '-' or DGR == "+")],  #P20
           [FVP, FGA == "+" and NWD == "-"],
           [DGD, DGR == "+" or FSN == "-"],
           [DPQ, FNN == "+" and CGB == "-"],
           [DCN, DGR == "+" or FSN == "-"],
           [DNN, DCN == "-"],
           [DIN, FSN == "+"],
           [FGC, FGN != "+"],
           [FGE, FGM == '-' and FGC =='+'],
           [FCN, FGP == "+"],
           [HMP, True],  #P30
           [ARR, True],
           [GCN, True],
           [GFN, GCN == '+' and FGP == "+"],
           [GFP, GFN == '+'],
           [GP3, GFP == "+"],
           [GEI, GP3 == "+"],
           [CSE, True],
           [EAL, CSE == "+" and FGK == "+"],
           [CAL, FGK == "+" and CSE == '+' and GP3 != "+" and EAL != "+"],
           [LKA, True],
           [LKO, LKA == "-"],
           [LKP, True],
           [DMP, DCN == "+"],
           [DMG, DMP == "+"],
           [GUN, (GCN == "-" or (GFP == "+" and GP3 == "-")) and CAL == '-' and LKA == "-"],
           [GAD, GUN != "+" and LKA =="-"],
           [GFL, (GCN == '-' or GFN == "+") and GP3 != "+" and GUN != '+' and EAL != "+"],
           [PGL, GFL == "-"],
           [GGH, FGP == "+" and CGR =='-' and NWD =='+' and GFP != "+" and GUN != "+"],
           [GSI, True],
           [ALP, GSI =='-'],  #50
           [GIT, True],
           [UST, ARR == "+"],
           [GPC, FGG == "+"],
           [PSC, FSN == "+" and UST != "+" and GPC != "+"],
           [PCA, PSC == "-"],
           [PMN, GFP == "+"],
           [RHM, FGP == "+"],
           [FRC, True],  #60
           [NRC, FRC == "+"],
           [DOR, DGR == "+" and FRC == "+"],
           [FFP, FGN == "+" and (LKA == "+" or LKP =="+" or LKO =="+" or GAD =="+") and GFP != '+'],
           [NUP, FGP == "+" and (CSE == "+" or LKA == "+" or LKO == "+")],
           [PNP, FGP == "+" and (CSE =='-' or NUP == '-')],
           [NUD, FGP == "+"],
           [NUC, UST != "+" and PNP =="+" and NUD == "+"],
           [NM1, NUC == "+"],
           [NM2, NM1 == "+"],
           [NUA, NM2 == "+"],
           [NGL, ((FGP == "+" and UST == "+") or NUA == "+") and (GUN == "+" or PGL == "+" or GFL == "+" )],
           [EAF, NM1 == "-"],
           [ACM, ARR == "-" and NGL == "-"],
           [DSN, DCN == "+"],
           [DSA, DGR == "+" and ARR == "+"],
           [DSS, DGR == "+" and (ARR == "-" or DSA == "+")],
           [DOC, NWD=="-" and DCN=="+" and NUC=="+"],
           [NEX, (FSN == "-" or CGR == "-") and NWD == "-" and NUA != "+"],  #80
           [PEX, NEX == "+"],
           [FEX, PEX =="+"] ,
           [PDC, DGR == "+" and (CGR != "-" or NWD == "-") and GFP != "+"],
           [PCL, FGP == "+" and DMP != "+" and GFP != "+" and UST != "+" and (PDC == "-" or DGR != "+")],
           [APO, GFP != "+" and UST != '+'],
           [WAP, NUD == "+" and PDC == "-" and DMP != '+' and (APO == "-" or (NM1 == "-" and APO == "+"))],
           [AGE, APO == "+"],
           [OPK, DGR == "+" and GSI =='-'],
           [TSP, FSN == "-" or DGR == "+"],  #90
           [TDP, TSP == "+"],
           [TDC, TSP == "-"],
           [TSA, UST != "+" and TSP != "+" and ((DGR == "+" and NM1 == "+") or (ARR=="-" and NM1=="-") or NUC == "-")],
           [TAR, ARR == "+" and TSP != "+"],
           [TLC, TSP != "+" and TDC != "+" and (TSA == "+" or (PNP == "+" and TAR == "+"))],
           [TND, CGR == "+" and (TAR == "+" or TSA =="+")],
           [TDA, (DSS == "+" or DSA =="+") and (TAR =="+" or TSA =="+")],
           [TNL, TSP == "+" or TLC == "+" or (TSP != "+" and TDC != "+" and TAR != "+" and TSA != "+")]]

    counter = 1
    for parameter in par:
        #check if the value is different than '0' once the implications are checked
        if parameter[0] != "0" and parameter[1]:
            pass
        #check if the value is '0' when the implications are not checked
        elif parameter[0] == "0" and not parameter[1]:
            pass
        #ignore '?'
        elif parameter[0] == '?':
            pass
        #all the other cases are saved
        else:
            x.append('P' + str(counter))
        counter += 1
    return x


def main(file):
    with open (file, 'r') as f:
        langs = f.readlines()
    with open("errors_" + file, 'w') as out:
        for lang in langs:
            print(lang)
            out.write(str(check_power(lang.split())))
            out.write('\n')

if __name__ == "__main__":
    main(sys.argv[1])


