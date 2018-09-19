####################################################
##
##	Kazuki Amakawa's Neural Network
##	main.py
##	Copyright(c) by Kazuki Amakawa, all right reserved
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
	if not tem:
		Error(tem)		
		return

	tem, Data = Train.Init(FileDie, SufixSet)
	if not tem:
		Error(tem)
		return

	tem, Model = Train.Train(Data, OutputDir)
	if not tem:
		Error(tem)
		return
	return
	

def TestMain():
	import Test
	tem = Test.Pretreatment()
	if not tem:
		Error(tem)
		return 

	tem, Model = Test.ReadModel(ModelDir)
	if not tem:
		Error(tem)
		return
	
	tem, Data = Test.ReadLocal(TestDir)
	if not tem:
		Error(tem)
		return
	
	tem, Result = Test.Test(Data)
	if not tem:
		Error(tem)
		return
	return


def ReLearn():
	import ReLearn
	import Test
	import Train

	tem = ReLearn.Pretreatment()
	if not tem:
		Error(tem)
		return
	
	tem, Model = Test.ReadModel(ModelDir)
	if not tem:
		Error(tem)
		return

        tem, Data = Train.Init(FileDie, SufixSet)
        if not tem:
                Error(tem)
                return

        tem, Model = Train.Train(Data, ModelDir, Model)
        if not tem:
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

	else:
		print("Unknown error, please connect the author and administrator")

	return

Files = GetSufixFile(FileDir + "/0", SufixSet)
Result = [0 for n in range(len(Files))]
Files.append(GetSufixFile(FileDir + "/1", SufixSet))
Result.append([1 for n in range(len(Files) - len(Result)]))


if __name__ == '__main__':
	import sys
	if len(sys.argv) != 2:
		Error(1)




