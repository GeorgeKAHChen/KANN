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
        img = np.array(Image.open(Files1[i]))
        Data.append(cv2.resize(img, (128, 72)))

    print("Data read succeed, training surround initial", end = "\r")
    os.environ["CUDA_VISIBLE_DEVICES"]="0" 

    return 0, np.array(Data), np.array(Result)
        



def TensorTrain(OutputDir, Data, Result, ModelFolder):
    import numpy as np
    import tensorflow as ts
    print("Training initial", end = "\r")
    
    #Training labels
    label_dict = {
        0: 'No person',
        1: 'Have person',
    }
    n_classes = 2

    #Training parameter
    training_iters = 200 
    learning_rate = 0.001 
    batch_size = 128

    x = tf.placeholder("float", [None, 28,28,1])
    y = tf.placeholder("float", [None, n_classes])


    print("Blank Model initial Succeed", end = "\r")
    
    print("Traning, this processing may take a long time", end = "\r")

    print("Training succeed", end = "\r")

    print("Model saving succeed, the location of model is " + SavStr, end = "\r")

    print("Training model end")

    return 0


def Train(OutputDir, Data, Result, ModelFolder):
    import keras
    from keras.models import Sequential,Input,Model
    from keras.layers import Dense, Dropout, Flatten
    from keras.layers import Conv2D, MaxPooling2D
    from keras.layers.normalization import BatchNormalization
    from keras.layers.advanced_activations import LeakyReLU

    print("Training initial", end = "\r")
    
    #batch_size = 64
    #epochs = 20
    #num_classes = 10

    fashion_model = Sequential()
    fashion_model.add(Conv2D(32, kernel_size=(3, 3),activation='linear',input_shape=(28,28,1),padding='same'))
    fashion_model.add(LeakyReLU(alpha=0.1))
    fashion_model.add(MaxPooling2D((2, 2),padding='same'))
    fashion_model.add(Conv2D(64, (3, 3), activation='linear',padding='same'))
    fashion_model.add(LeakyReLU(alpha=0.1))
    fashion_model.add(MaxPooling2D(pool_size=(2, 2),padding='same'))
    fashion_model.add(Conv2D(128, (3, 3), activation='linear',padding='same'))
    fashion_model.add(LeakyReLU(alpha=0.1))                  
    fashion_model.add(MaxPooling2D(pool_size=(2, 2),padding='same'))
    fashion_model.add(Flatten())
    fashion_model.add(Dense(128, activation='linear'))
    fashion_model.add(LeakyReLU(alpha=0.1))                  
    fashion_model.add(Dense(num_classes, activation='softmax'))

    fashion_model.compile(loss=keras.losses.categorical_crossentropy, optimizer=keras.optimizers.Adam(),metrics=['accuracy'])
    print("Blank Model initial Succeed, Here is the summary of model", end = "\n")
    fashion_model.summary()
    
    print("Traning, this processing may take a long time", end = "\r")
    #fashion_train = fashion_model.fit(train_X, train_label, batch_size=batch_size,epochs=epochs,verbose=1,validation_data=(valid_X, valid_label))
    
    print("Training succeed", end = "\r")
    fashion_model.save(filepath)

    print("Model saving succeed, the location of model is " + SavStr, end = "\r")

    print("Training model end")
    return 0








