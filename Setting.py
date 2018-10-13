"""
Note: Some basic usage of vi/vim
      Press Esc key and input command `:wq` to escape vim and save change
      Press i key if you want to change some parameter
      Press Esc key and input command `:q!` to escape vim without changing
"""

####################################################
##
##    Kazuki Amakawa's Neural Network
##    Setting.py
##    Copyright(c) by Kazuki Amakawa, all right reserved
##
####################################################

"""
WARNING: It is necessary to determine all location before running.
         However, if you just need one function, you should confident
         datalist with followed list

main train
    DataClass, InputFolder, ModelSave, OutputFolder

main test
    DataClass, TestFolder, ModelFolder

main retrain
    DataClass, InputFolder, ModelFolder


"""


#====================================================
"""
string<vector> DataClass

This array include all kind of data will be used in the inpur folder
CAUSION: If the input is ".yuv", tt is necessary to transport yuv to rgb
         We made a tool "yuv2rgb.py" in ./Tool/yuv2rgb.py
"""

DataClass = ["jpg"]
#====================================================



#====================================================
"""
string InputFolder

This folder include data for training, you can put your data in different 
folder named by number and the system will sort with folder. Also, this
folder can save data you want to retrain the model
"""
InputFolder = "./Input/SampleInput"
#====================================================



#====================================================
"""
string ModelSave

This folder will save model you trained.
"""
ModelSave = "./Output/SampleModel"
#====================================================



#====================================================
"""
string OutputFolder

This folder will save the result of your test data
"""
OutputFolder = "./Output"
#====================================================



#====================================================
"""
string TestFolder

This folder is the location of your test data
"""
TestFolder = "./Input/Data"
#====================================================



#====================================================
"""
string ModelFolder

This folder will save the model you trained. And this is also the 
location of model you want to train again
"""
ModelFolder = "./Output/SampleModel"
#====================================================



#====================================================
"""
vector <*> Parameter

This vector include most parameter in the network, they are

    0   int     Iterator times
    1   int     Down Sample Image Size width
    2   int     Down Sample Image Size height
    3   string  Network Structure 
    (Not Finished)
"""
Parameter = [500, 128, 72, ""]
#====================================================


