####################################################
##
##    Kazuki Amakawa's Neural Network
##    Train.py
##    Copyright(c) by Kazuki Amakawa, all right reserved
##
####################################################
import Init


def Pretreatment(FileDir, SufixSet, ModelFolder):
    import numpy as np
    from PIL import Image
    import cv2
    import os
    from keras.utils import to_categorical

    print("Train model start, data reading", end = "\r")
    
    #Initial data set
    Data = []

    #Get files direction
    if not os.path.exists(FileDir):
        return 2, [], []
    if len(SufixSet) == 0:
        return 3, [], []
    for i in range(0, len(SufixSet)):
        if SufixSet[i] == "yuv":
            return 4, [], []
    if not os.path.exists(ModelFolder):
        return 6, [], []

    Files1 = Init.GetSufixFile(FileDir + "/0", SufixSet)
    Files2 = Init.GetSufixFile(FileDir + "/1", SufixSet)
    
    #Build the sign
    Result = [0 for n in range(len(Files1))]
    Files1 += Files2
    Result += [1 for n in range(len(Files2))]

    
    if len(Files1) == 0 or len(Files2) == 0:
        return 5, [], []
    
    #Get image data and down sample    
    for i in range(0, len(Files1)):
        img = np.array(Image.open(Files1[i]).convert("L"))
        Data.append(cv2.resize(img, (128, 72)))

    print("Data read succeed, training surround initial", end = "\r")
    os.environ["CUDA_VISIBLE_DEVICES"]="0" 
    
    Data = np.array(Data)
    Result = np.array(Result)
    
    Data = Data.reshape(-1, 128, 72, 1)
    Data = Data / 255

    Result = to_categorical(Result)

    return 0, np.array(Data), np.array(Result)
        




def Train(trainX, trainY, ModelFolder, Iteration):
    """
    keras network training
    """
    import keras
    from keras.models import Sequential,Input,Model
    from keras.layers import Dense, Dropout, Flatten
    from keras.layers import Conv2D, MaxPooling2D
    from keras.layers.normalization import BatchNormalization
    from keras.layers.advanced_activations import LeakyReLU
    import os
    from sklearn.model_selection import train_test_split

    trainX,validX,trainY,validY = train_test_split(trainX, trainY, test_size=0.2, random_state=13)


    batch_size = 128 * 72
    epochs = Iteration
    num_classes = 2

    model = Sequential()
    model.add(Conv2D(16, kernel_size=(3, 3),activation='linear',input_shape=(128, 72, 1), padding='same'))
    model.add(LeakyReLU(alpha=0.1))
    model.add(MaxPooling2D((2, 2),padding='same'))
    model.add(Conv2D(64, (3, 3), activation='linear',padding='same'))
    model.add(LeakyReLU(alpha=0.1))
    model.add(MaxPooling2D(pool_size=(2, 2),padding='same'))
    #model.add(Conv2D(128, (3, 3), activation='linear',padding='same'))
    #model.add(LeakyReLU(alpha=0.1))                  
    #model.add(MaxPooling2D(pool_size=(2, 2),padding='same'))
    model.add(Flatten())
    model.add(Dense(64, activation='linear'))
    model.add(LeakyReLU(alpha=0.1))                  
    model.add(Dense(num_classes, activation='softmax'))

    model.compile(loss=keras.losses.categorical_crossentropy, optimizer=keras.optimizers.Adam(),metrics=['accuracy'])
    os.system("clear")
    print("Blank Model initial Succeed, Here is the summary of model", end = "\n")
    model.summary()
    input("Press Enter to continue")

    os.system("clear")
    print("Traning, this processing may take a long time", end = "\n")
    train = model.fit(trainX, trainY, batch_size=batch_size,epochs=epochs,verbose=1, validation_data=(validX, validY))
    
    print("Training succeed", end = "\r")
    scores = model.evaluate(trainX, trainY)
    
    model_json = model.to_json()
    with open(ModelFolder + "/model.json", "w") as json_file:
        json_file.write(model_json)
    model.save_weights(ModelFolder + "/model.h5")

    print("Model saving succeed, the location of model is " + ModelFolder, end = "\r")

    print("Training model end")
    return 0








