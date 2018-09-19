####################################################
##
##    Kazuki Amakawa's Neural Network
##    main.py
##    Copyright(c) by Kazuki Amakawa, all right reserved
##
####################################################
import Init
import Setting 


FileDir = Setting.InputFolder
SufixSet = Setting.DataClass
OutputDir = Setting.OutputFolder
ModelDir = Setting.ModelFolder
TestDir = Setting.TestFolder


def TrainMain():
    import Train
    tem = Train.Pretreatment()
    if tem:
        Error(tem)        
        return

    tem, Data = Train.Init(FileDie, SufixSet)
    if tem:
        Error(tem)
        return

    tem, Model = Train.Train(Data, OutputDir)
    if tem:
        Error(tem)
        return
    return
    

def TestMain():
    import Test
    tem = Test.Pretreatment()
    if tem:
        Error(tem)
        return 

    tem, Model = Test.ReadModel(ModelDir)
    if tem:
        Error(tem)
        return
    
    tem, Data = Test.ReadLocal(TestDir)
    if tem:
        Error(tem)
        return
    
    tem, Result = Test.Test(Data)
    if tem:
        Error(tem)
        return
    return


def ReLearn():
    import ReLearn
    import Test
    import Train

    tem = ReLearn.Pretreatment()
    if tem:
        Error(tem)
        return
    
    tem, Model = Test.ReadModel(ModelDir)
    if tem:
        Error(tem)
        return

        tem, Data = Train.Init(FileDie, SufixSet)
        if tem:
                Error(tem)
                return

        tem, Model = Train.Train(Data, ModelDir, Model)
        if tem:
                Error(tem)
                return
        return    
    

def Error(code):
    """
    All error will be treated in this funtion, it is necesasry to input error
    code into this function
    """
    print("Error " + str(code) + "\t", end = "")
    if code == 1:
        print("No parameter, using `main help` to determine the parameter of program")
    if code == 2:
        print("No folder")
    if code == 3:
        print("sufix array is empty, please determine the kind of files will be used is folder")
    if code == 4:
        print("yuv error, please using yuv2rgb before learning")
    if code == 5:
        print("train data lacked, please have files in 0 and 1")
    else:
        print("Unknown error, please connect the author and administrator")
    
    print("For more help, please using command `make help`")
    return


if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        Error(1)




