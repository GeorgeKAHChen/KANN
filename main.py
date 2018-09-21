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
ModelSave = Setting.ModelSave
TestDir = Setting.TestFolder


def TrainMain():
    import Train
    tem, Data, Result = Train.Pretreatment(FileDir, SufixSet, ModelSave)
    if tem:
        Error(tem)        
        return

    tem = Train.Train(Data, Result, ModelSave)
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


"""
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
""" 

def Error(code):
    """
    All error will be treated in this funtion, it is necesasry to input error
    code into this function
    """
    print("Error " + str(code) + "\t:  ", end = "")
    if code == 1:
        print("No parameter, using `main help` to determine the parameter of program")
    elif code == 2:
        print("No folder")
    elif code == 3:
        print("sufix array is empty, please determine the kind of files will be used is folder")
    elif code == 4:
        print("yuv error, please using yuv2rgb before learning")
    elif code == 5:
        print("train data lacked, please have files in 0 and 1")
    elif code == 6:
        print("model saving folder is not exist")
    else:
        print("Unknown error, please connect the author and administrator")
    
    print("For more help, please using command `make help`")
    return


if __name__ == '__main__':
    import sys
    Init.StaClear()
    if len(sys.argv) != 2:
        Error(1)
    elif sys.argv[1] == "-t":
        TrainMain()
    






