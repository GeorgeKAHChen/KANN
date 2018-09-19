####################################################
##
##    Kazuki Amakawa's Neural Network
##    Train.py
##    Copyright(c) by Kazuki Amakawa, all right reserved
##
####################################################
import Init
def Pretreatment(FileDir, SufixSet):
    print("Train model start ...", end = "\n")
    import os
    if not os.path.exists(FileDir):
        return 2, [], []
    if len(SufixSet) == 0:
        return 3, [], []
    for i in range(0, len(SufixSet)):
        if SufixSet[i] == "yuv":
            return 4, [], []
    Files1 = GetSufixFile(FileDir + "/0", SufixSet)
    Files2 = GetSufixFile(FileDir + "/1", SufixSet)
    
    Result = [0 for n in range(len(Files))]
    Files1.append(Files2)
    Result.append([1 for n in range(len(Files2))]))
    
    if len(Files1) == 0 or len(Files2) == 0
        return 5, [], []
       
    print("Initial Succeed", end = "\r")
    return 0, DataDir, Result

def Init(FileDir, SufixSet):
    
    return 0

def Train(Data, OutputDir):
    return 0




