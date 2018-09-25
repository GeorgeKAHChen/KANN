####################################################
##
##    Kazuki Amakawa's Neural Network
##    main.py
##    Copyright(c) by Kazuki Amakawa, all right reserved
##
####################################################
import Init
def Pretreatment(FileDir, SufixSet, ModelDir):
    import numpy as np
    from PIL import Image
    import cv2
    import os
    print("Test model start, data reading", end = "\r")
    
    #Initial data set
    TestData = []

    #Get files direction
    if not os.path.exists(FileDir):
        return 2, [], []
    if len(SufixSet) == 0:
        return 3, [], []
    for i in range(0, len(SufixSet)):
        if SufixSet[i] == "yuv":
            return 4, [], []
    if not os.path.exists(ModelDir):
        return 8, [], []
    
    Files1 = Init.GetSufixFile(FileDir, SufixSet)
    
    Name = []
    for i in range(0, len(Files1)):
        Str = ""
        for j in range(len(Files1[i]) - 1, -1, -1):
            if Files1[i][j] == "/":
                break
            Str = Files1[i][j] + Str
        Name.append(Str)

    if len(Files1) == 0:
        return 7, [], []

    Data = []
    #Get image data and down sample    
    for i in range(0, len(Files1)):
        img = np.array(Image.open(Files1[i]).convert("L"))
        Data.append(cv2.resize(img, (128, 72)))
    
    Data = np.array(Data)
    Data = Data.reshape(-1, 128, 72, 1)
    Data = Data / 255

    print("Data read succeed, testing surround initial", end = "\r")
    os.environ["CUDA_VISIBLE_DEVICES"]="0" 

    return 0, np.array(Data), Name
        

def Test(TestData, ModelDir, OutputDir, FileNames):
    import keras
    import os
    from keras.models import model_from_json

    with open(ModelDir + '/model.json', 'r') as f:
        model = model_from_json(f.read())

    model.load_weights(ModelDir + "/model.h5")
    print("Model read succeed, testing", end = "\r")

    OutputStr = "FileName\t |\tResult"
    for i in range(0, len(TestData)):
        OutputStr += FileNames[i]
        OutputStr += "\t\t"
        OutputStr += model.predict_classes(TestData[i])
        OutputStr += "\n"        
    
    print("Test ended, result saving", end = "\r")
    FileName = OutputDir + "/Result.out"
    File = open(FileName, "w")
    File.write(OutputStr)
    File.close()
    print("Test model end", end = "\n")

    return 0 




