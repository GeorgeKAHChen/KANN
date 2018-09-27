####################################################
##
##    Kazuki Amakawa's Neural Network
##    install.py
##    Copyright(c) by Kazuki Amakawa, all right reserved
##
####################################################

def FileExist(FileName):
    import os
    Error = 0
    for i in range(0, len(FileName)):
        if not os.path.exists(FileName[i]):
            print("Error: " + str(FileName[i]) + " not exist")
            Error = 1
    return Error



def install():
    import os
    Error = 0
    Error += FileExist(["Init.py", "Setting.py", "Train.py", "Test.py", "help.sh", "clean.sh", "gitignore"])
    #Error += HeadExist() 
    if Error != 0:
        print("Install break")
        return 1
    os.system("g++ -std=c++11 test_run_cnn.cc keras_model.cc -o ctest")
    os.system("vim Setting.py")
    os.system("mv gitignore .gitignore")
    return 0


