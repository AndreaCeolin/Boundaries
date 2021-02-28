#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Author: Andrea Ceolin
February 2021

This script is used to generate artificial distances'''



import random, sys

###DEFINE EMPIRICAL RATIO
def setp(num):
    ratio = ['Ratio', 0.933, 0.786, 0.929, 0.141, 0.857, 0.333, 1.0, 0.0, 0.5, 0.75, 0.996, 0.067, 0.411, 0.375, 0.649, 0.0, 0.243,
     0.154, 0.595, 0.246, 0.25, 0.333, 0.048, 0.222, 0.056, 1.0, 0.5, 0.083, 0.0, 0.564, 0.522, 0.75, 0.833, 0.76, 0.0,
     0.978, 0.077, 0.278, 0.267, 0.182, 0.2, 0.667, 0.25, 0.333, 0.545, 0.049, 0.007, 0.571, 0.0, 0.067, 0.002, 0.356,
     0.2, 0.418, 0.0, 0.08, 0.044, 0.6, 0.415, 0.375, 0.183, 0.631, 0.792, 0.833, 0.333, 0.8, 0.75, 1.0, 0.0, 0.4,
     0.333, 0.333, 0.1, 0.359, 0.5, 0.625, 1.0, 1.0, 0.143, 0.187, 0.045, 0.1, 0.4, 0.333, 0.175, 0.0, 0.45, 0.618,
     0.611, 0.55, 0.25, 0.25, 0.875, 0.534]
    r = random.random()
    if r < ratio[num]:
        return "+"
    else:
        return "-"
    

###GENERATE LANGUAGES FOLLOWING THE EMPIRICAL RATIO
def generator():
        P = list(range(95))
        P[0] = "Lang"
        #P1-FGM
        FGM = setp(1)
        P[1] = FGM
        #P2-FGA
        #P3-FGK
        #P5-FGP
        if FGM == '+':
            FGA = setp(2)
            FGK = setp(3)
            FGP = setp(5)
        else:
            FGA = '0'
            FGK = '0'
            FGP = '0'
        P[2] = FGA
        P[3] = FGK
        P[5] = FGP
        #P4-SPK
        if FGK == "+":
            SPK = setp(4)
        else:
            SPK = '0'
        P[4] = SPK
        #P6-FSP
        if FGP != "+":
            FSP = setp(6)
        else:
            FSP = '0'
        P[6] = FSP
        #P7-FGN
        if FGP == "+":
            FGN = setp(7)
        else:
            FGN = '0'
        P[7] = FGN
        #P8-SCO
        #P9-GDP
        if FGM == "+" and FGN != "+":
            SCO = setp(8)
            GDP = setp(9)
        else:
            SCO = '0'
            GDP = '0'
        P[8] = SCO
        P[9] = GDP
        #P10-FSN
        #P13-FGG
        #P14-FSG
        if FGN == "+":
            FSN = setp(10)
            FGG = setp(13)
            FSG = setp(14)
        else:
            FSN = '0'
            FGG = '0'
            FSG = '0'
        P[10] = FSN
        P[13] = FGG
        P[14] = FSG
        #P11-FNN
        if FSN == "+":
            FNN = setp(11)
        else:
            FNN = '0'
        P[11] = FNN
        #P12-FGT
        FGT = setp(12)
        P[12] = FGT
        #P15-CGB
        CGB = setp(15)
        P[15] = CGB
        #P16-FPC
        FPC = setp(16)
        P[16] = FPC
        #P17-DGR
        if FPC == "-" and FGN == "+":
            DGR = setp(17)
        else:
            DGR = '0'
        P[17] = DGR
        #P18-DGP
        if DGR != '+':
            DGP = setp(18)
        else:
            DGP = '0'
        P[18] = DGP
        #P19-CGR
        if CGB == "-" and DGR == "+":
            CGR = setp(19)
        else:
            CGR = '0'
        P[19] = CGR
        #P20-NWD
        if FGP == "+" and (FSN == '-' or DGR == "+"):
            NWD = setp(20)
        else:
            NWD = '0'
        P[20] = NWD
        #P21-DGD
        if DGR == "+" or FSN == "-":
            DGD = setp(21)
        else:
            DGD = '0'
        P[21] = DGD
        #P22-DPQ
        if FNN == "+" and CGB == "-":
            DPQ = setp(22)
        else:
            DPQ = '0'
        P[22] = DPQ
        #P23-DCN
        if DGR == "+" or FSN == "-":
            DCN = setp(23)
        else:
            DCN = '0'
        P[23] = DCN
        #P24-DNN
        if DCN == '-':
            DNN = setp(24)
        else:
            DNN = '0'
        P[24] = DNN
        #P25-DIN
        if FSN == "+":
            DIN = setp(25)
        else:
            DIN = '0'
        P[25] = DIN
        #P26-FGC
        if FGN != "+":
            FGC = setp(26)
        else:
            FGC = '0'
        P[26] = FGC
        #P27-FGE
        if FGM == '-' and FGC =='+':
            FGE = setp(27)
        else:
            FGE = '0'
        P[27] = FGE
        #P28-FCN
        if FGP == "+":
            FCN = setp(28)
        else:
            FCN = '0'
        P[28] = FCN
        #P29-HMP
        HMP = setp(29)
        P[29] = HMP
        #P30-ARR
        ARR = setp(30)
        P[30] = ARR
        #P31-GCN
        GCN = setp(31)
        P[31] = GCN
        #P32-GFN
        if FGP == "+" and GCN == "+":
            GFN = setp(32)
        else:
            GFN = '0'
        P[32] = GFN
        #P33-GFP
        if GFN == "+":
            GFP = setp(33)
        else:
            GFP = '0'
        P[33] = GFP
        #P34-GP3
        if GFP == "+":
            GP3 = setp(34)
        else:
            GP3 = '0'
        P[34] = GP3
        #P35-GEI
        if GP3 == "+":
            GEI = setp(35)
        else:
            GEI = '0'
        P[35] = GEI
        #P36-CSE
        CSE = setp(36)
        P[36] = CSE
        #P37-EAL
        if FGK == "+" and CSE == "+":
            EAL = setp(37)
        else:
            EAL = '0'
        P[37] = EAL
        #P38-CAL
        if FGK == "+" and CSE == "+" and EAL != '+' and GP3 != "+":
            CAL = setp(38)
        else:
            CAL = '0'
        P[38] = CAL
        #P39-LKA
        #P41-LKP
        LKA = setp(39)
        LKP = setp(41)
        P[39] = LKA
        P[41] = LKP
        #P40-LKO
        if LKA == "-":
            LKO = setp(40)
        else:
            LKO = '0'
        P[40] = LKO
        #P42-DMP
        if DCN == "+":
            DMP = setp(42)
        else:
            DMP = '0'
        P[42] = DMP
        #P43-DMG
        if DMP == "+":
            DMG = setp(43)
        else:
            DMG = '0'
        P[43] = DMG
        # P44-GUN
        if (GCN == "-" or (GFP == "+" and GP3 == "-")) and CAL == '-' and LKA == '-':
            GUN = setp(44)
        else:
            GUN = '0'
        P[44] = GUN
        # P45-GAD
        if LKA == "-" and GUN != "+":
            GAD = setp(45)
        else:
            GAD = '0'
        P[45] = GAD
        # P46-GFL
        if (GCN == "-" or GFN == "+") and GP3 != "+" and EAL != "+" and GUN != "+":
            GFL = setp(46)
        else:
            GFL = '0'
        P[46] = GFL
        # P47-PGL
        if GFL == '-':
            PGL = setp(47)
        else:
            PGL = '0'
        P[47] = PGL
        # P48-GGH
        if CGR == '-' and NWD == '+' and FGP == "+" and GFP != "+" and GUN != "+":
            GGH = setp(48)
        else:
            GGH = '0'
        P[48] = GGH
        # P49-GSI
        GSI = setp(49)
        P[49] = GSI
        # P50-ALP
        if GSI == "-":
            ALP = setp(50)
        else:
            ALP = '0'
        P[50] = ALP
        # P51-GIT
        GIT = setp(51)
        P[51] = GIT
        #######################################
        # P52-UST
        if ARR == "+":
            UST = setp(52)
        else:
            UST = '0'
        P[52] = UST
        # P53-GPC
        if FGG == "+":
            GPC = setp(53)
        else:
            GPC = '0'
        P[53] = GPC
        # P54-PSC
        if FSN == "+" and UST != "+" and GPC != "+":
            PSC = setp(54)
        else:
            PSC = '0'
        P[54] = PSC
        # P55-PCA
        if PSC == "-":
            PCA = setp(55)
        else:
            PCA = '0'
        P[55] = PCA
        # P56-PMN
        if GFP == "+":
            PMN = setp(56)
        else:
            PMN = "0"
        P[56] = PMN
        # P57-RHM
        if FGP == "+":
            RHM = setp(57)
        else:
            RHM = '0'
        P[57] = RHM
        # P58-FRC
        FRC = setp(58)
        P[58] = FRC
        # P59-NRC
        if FRC == "+":
            NRC = setp(59)
        else:
            NRC = '0'
        P[59] = NRC
        # P60-DOR
        if DGR == "+" and FRC == "+":
            DOR = setp(60)
        else:
            DOR = '0'
        P[60] = DOR
        # P61-FFP
        if FGN == "+" and (LKA == "+" or LKP == "+" or LKO == "+" or GAD == "+") and GFP != '+':
            FFP = setp(61)
        else:
            FFP = '0'
        P[61] = FFP
        # P62-NUP
        if FGP == "+" and (CSE == "+" or LKA == "+" or LKO == "+"):
            NUP = setp(62)
        else:
            NUP = '0'
        P[62] = NUP
        # P63-PNP
        if FGP == "+" and (CSE == '-' or NUP == '-'):
            PNP = setp(63)
        else:
            PNP = '0'
        P[63] = PNP
        # P64-NUD
        if FGP == "+":
            NUD = setp(64)
        else:
            NUD = '0'
        P[64] = NUD
        # P65-NUC
        if UST != "+" and PNP == "+" and NUD == "+":
            NUC = setp(65)
        else:
            NUC = '0'
        P[65] = NUC
        # P66-NM1
        if NUC == "+":
            NM1 = setp(66)
        else:
            NM1 = '0'
        P[66] = NM1
        # P67-NM2
        if NM1 == "+":
            NM2 = setp(67)
        else:
            NM2 = '0'
        P[67] = NM2
        # P68-NUA
        if NM2 == "+":
            NUA = setp(68)
        else:
            NUA = '0'
        P[68] = NUA
        # P69-NGL
        if ((FGP == "+" and UST == "+") or NUA == "+") and (GUN == "+" or GFL == "+" or PGL == "+"):
            NGL = setp(69)
        else:
            NGL = '0'
        P[69] = NGL
        # P70-EAF
        if NM1 == '-':
            EAF = setp(70)
        else:
            EAF = '0'
        P[70] = EAF
        # P71-ACM
        if ARR == "-" and NGL == "-":
            ACM = setp(71)
        else:
            ACM = '0'
        P[71] = ACM
        # P72-DSN
        if DCN == "+":
            DSN = setp(72)
        else:
            DSN = '0'
        P[72] = DSN
        # P73-DSA
        if DGR == "+" and ARR == "+":
            DSA = setp(73)
        else:
            DSA = '0'
        P[73] = DSA
        # P74-DSS
        if DGR == "+" and (ARR == "-" or DSA == "+"):
            DSS = setp(74)
        else:
            DSS = "0"
        P[74] = DSS
        # P75-DOC
        if NWD == "-" and DCN == "+" and NUC == "+":
            DOC = setp(75)
        else:
            DOC = '0'
        P[75] = DOC
        # P76-NEX
        if (FSN == "-" or CGR == "-") and NWD == "-" and NUA != "+":
            NEX = setp(76)
        else:
            NEX = '0'
        P[76] = NEX
        # P77-PEX
        if NEX == "+":
            PEX = setp(77)
        else:
            PEX = '0'
        P[77] = PEX
        # P78-FEX
        if PEX == "+":
            FEX = setp(78)
        else:
            FEX = '0'
        P[78] = FEX
        ######################################
        # P79-PDC
        if DGR == "+" and (CGR != "-" or NWD == "-") and GFP != "+":
            PDC = setp(79)
        else:
            PDC = '0'
        P[79] = PDC
        # P80-PCL
        if FGP == "+" and DMP != "+" and GFP != "+" and (PDC == "-" or DGR != "+") and UST != "+":
            PCL = setp(80)
        else:
            PCL = '0'
        P[80] = PCL
        # P81-APO
        if GFP != "+" and UST != '+':
            APO = setp(81)
        else:
            APO = '0'
        P[81] = APO
        # P82-WAP
        if PDC == "-" and NUD == "+" and DMP != '+' and (APO == "-" or (NM1 == "-" and APO == "+")):
            WAP = setp(82)
        else:
            WAP = '0'
        P[82] = WAP
        # P83-AGE
        if APO == "+":
            AGE = setp(83)
        else:
            AGE = '0'
        P[83] = AGE
        # P84-OPK
        if DGR == "+" and GSI == '-':
            OPK = setp(84)
        else:
            OPK = '0'
        P[84] = OPK
        # P85-TSP
        if FSN == "-" or DGR == "+":
            TSP = setp(85)
        else:
            TSP = '0'
        P[85] = TSP
        # P86-TDP
        if TSP == "+":
            TDP = setp(86)
        else:
            TDP = '0'
        P[86] = TDP
        # P87-TDC
        if TSP == "-":
            TDC = setp(87)
        else:
            TDC = '0'
        P[87] = TDC
        # P88-TSA
        if UST != "+" and TSP != "+" and ((DGR == "+" and NM1 == "+") or (ARR == "-" and NM1 == "-") or NUC == "-"):
            TSA = setp(88)
        else:
            TSA = '0'
        P[88] = TSA
        # P89-TAR
        if ARR == "+" and TSP != "+":
            TAR = setp(89)
        else:
            TAR = '0'
        P[89] = TAR
        # 90-TLC
        if TSP != "+" and TDC != "+" and (TSA == "+" or (PNP == "+" and TAR == "+")):
            TLC = setp(90)
        else:
            TLC = '0'
        P[90] = TLC
        # 91-TND
        if CGR == "+" and (TSA == "+" or TAR == "+"):
            TND = setp(91)
        else:
            TND = '0'
        P[91] = TND
        # 92-TDA
        if (DSS == "+" or DSA == "+") and (TAR == "+" or TSA == "+"):
            TDA = setp(92)
        else:
            TDA = '0'
        P[92] = TDA
        # 93-TNL
        if TSP == "+" or TLC == "+" or (TSP != "+" and TDC != "+" and TAR != "+" and TSA != "+"):
            TNL = setp(93)
        else:
            TNL = '0'
        P[93] = TNL
        #94-FVP
        if FGA == "+" and NWD == "-":
            FVP = setp(94)
        else:
            FVP = '0'
        P[94] = FVP
        return P


##################################################################################
    

####JACCARD DISTANCE
def jaccard(P1, P2):
    id = 0.0
    dif = 0.0
    for i in range(len(P1)):
        if P1[i] == P2[i] == "+":
            id = id + 1
        elif (P1[i] == "+" and P2[i] == "-") or (P1[i] == "-" and P2[i] == "+"):
            dif = dif + 1
    dist = dif / (dif + id)
    return dist

####GENERATE DISTANCES
def distance(number):
    #run generator() to create a number of possible language
    random_sample = []    
    for i in range(number):
        lang = generator()
        random_sample.append(lang)
    #create a list of pairwise distances
    dist_list=[]
    for i in range(len(random_sample)):
        print(i)
        p0 = random_sample[i]
        for j in range(i + 1, len(random_sample)):
    #calculate the distance between the strings
            dist = jaccard(p0, random_sample[j])
            dist_round=round(dist, 3)
            dist_list.append(dist_round)
    dist_list.sort()
    return dist_list


if __name__ == "__main__":
    result = distance(int(sys.argv[1]))
    f = open('random_langs.txt', 'w')
    for lang in result:
        f.write('Random' + ', ' + str(lang))
        f.write('\n')
    f.close()

