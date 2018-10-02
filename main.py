####################################################
##
##    Kazuki Amakawa's Neural Network
##    main.py
##    Copyright(c) by Kazuki Amakawa, all right reserved
##
####################################################
import Init
import Setting 

SufixSet = Setting.DataClass
FileDir = Setting.InputFolder
ModelSave = Setting.ModelSave
OutputDir = Setting.OutputFolder
ModelDir = Setting.ModelFolder
TestDir = Setting.TestFolder
Iteration = Setting.iteration

def TrainMain(Presentation):
    import Train
    tem, Data, Result = Train.Pretreatment(FileDir, SufixSet, ModelSave)
    if tem:
        Error(tem)        
        return

    tem = Train.Train(Data, Result, ModelSave, Iteration, Presentation)
    if tem:
        Error(tem)
        return
    return
    


def TestMain(Presentation):
    import Test
    tem, TestData, FileNames = Test.Pretreatment(TestDir, SufixSet, ModelDir, 0)
    if tem:
        Error(tem)
        return 
    
    tem = Test.Test(TestData, ModelDir, OutputDir, FileNames)
    if tem:
        Error(tem)
        return
    return



def Error(code):
    import os
    """
    All error will be treated in this funtion, it is necesasry to input error
    code into this function
    """
    print()
    print()
    code += 100
    print("Error " + str(code) + "\t:   ", end = "")
    if code - 100 == 1:
        print("No parameter, using `main help` to determine the parameter of program")
    elif code - 100 == 2:
        print("No folder")
    elif code - 100 == 3:
        print("sufix array is empty, please determine the kind of files will be used is folder")
    elif code - 100 == 4:
        print("yuv error, please using yuv2rgb before learning")
    elif code - 100 == 5:
        print("train data lacked, please have files in 0 and 1")
    elif code - 100 == 6:
        print("model saving folder is not exist")
    elif code - 100 == 7:
        print("test data is not be found")
    elif code - 100 == 8:
        print("make setting error, the parameter p only have 0 and 1 value")
    elif code - 100 == 9:
        print("Command error, you have been installed or the files of system are lost")
    elif code - 100 == 10:
        print("Install error, please using command `make install` to install the system before using it")
    else:
        print("Unknown error, please connect the author and administrator")
    
    print("For more help, please using command `make help`")
    os._exit(0)
    return





if __name__ == '__main__':
    import sys
    import os
    if sys.argv[1] == "-i":
        try:
            import install
            if install.install(int(sys.argv[3])) == 0:
                print("Install succeed")
                if sys.argv[3] == "0":
                    os.system("rm -rf install.py")
                os._exit(0)
            else:
               print("Install failed, please determine the relationship package and file integrity")
               os._exit(0)
        except:
            Error(9)
            os._exit(0)
    
    if sys.argv[3] == "0":
        try:
            import install
            Error(10)
            os._exit(0)
        except:
            pass

    Init.StaClear()
    if len(sys.argv) != 4:
        Error(1)
    elif sys.argv[2] != "0" and sys.argv[2] != "1":
        Error(8)
    elif sys.argv[1] == "-l":
        TrainMain(int(sys.argv[2]))
    elif sys.argv[1] == "-t":
        TestMain(int(sys.argv[2]))
    elif sys.argv[1] == "-ci":
        try:
            import dump2simple
        except:
            Error(-1)
        import Test
        tmp, Data, Name = Test.Pretreatment(TestDir, SufixSet, ModelDir, 1) 
        if tmp != 0:
            Error(tmp)
            os._exit(0)
        if not os.path.exists(TestDir + "/tmp"):
            os.system("mkdir " + TestDir + "/tmp")
        else:
            os.system("rm -rf " + TestDir + "/tmp")
            os.system("mkdir " + TestDir + "/tmp")
               
        for i in range(0, len(Name)):
            Init.BuildFile(TestDir + "/tmp/" + Name[i] + ".dat")
            with open(TestDir + "/tmp/" + Name[i] + ".dat", "w") as fin:
                fin.write("1 " + str(len(Data[i])) + " " + str(len(Data[i][0]))  + "\n")
                for j in range(0, len(Data[i])):
                    fin.write("[")
                    for k in range(0, len(Data[i][j])):
                        fin.write(str(Data[i][j][k]))
                        if k != len(Data[i][j]) - 1:
                            fin.write("\t")
                        else:
                            fin.write("]\n")
                        
        """
        import numpy as np
        np.set_printoptions(threshold=np.inf)
        with open(TestDir + "/data.dat", "w") as fin:
            fin.write(str(len(Data)) + " " + str(len(Data[0])) + " " + str(len(Data[0][0])) + "  1\n")
            fin.write("[")
            for b in Data:
                fin.write("[")
                for c in b:
                    fin.write("[")
                    for d in c:
                        fin.write("[" + str(d) + "]\t")
                    fin.write("]\n")            
                fin.write("]\n")
            fin.write("]")
        """
        print() 




