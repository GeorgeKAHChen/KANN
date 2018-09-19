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
    Files1 = Init.GetSufixFile(FileDir + "/0", SufixSet)
    Files2 = Init.GetSufixFile(FileDir + "/1", SufixSet)
    
    Result = [0 for n in range(len(Files1))]
    Files1.append(Files2)
    Result.append([1 for n in range(len(Files2))])
    
    if len(Files1) == 0 or len(Files2) == 0:
        return 5, [], []
       
    print("Initial Succeed", end = "\r")
    return 0, Files1, Result



def Train(OutputDir, DataDir, Result):
    import numpy as np
    from PIL import Image

    import keras
    from keras.models import Sequential,Input,Model
    from keras.layers import Dense, Dropout, Flatten
    from keras.layers import Conv2D, MaxPooling2D
    from keras.layers.normalization import BatchNormalization
    from keras.layers.advanced_activations import LeakyReLU
    
    #Initial model
    batch_size = 64
    epochs = 20
    num_classes = 10
    
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

    sign = 0

    #Leaning Loop
    while 1:
        if sign == len(OutputDir):
            break
        
        RoundX = []
        RoundY = []
        for i in range(0, len(10)):
            if sign == len(OutputDir):
                break
            img = np.array(Image.open(OutputDir[sign]))
            RoundX.append(img)
            RoundY.append(Result[sign])
            
            sign += 1
        fashion_train = fashion_model.fit(RoundX, RoundY, batch_size=batch_size,epochs=epochs,verbose=1,validation_data=(valid_X, valid_label))

    return 0, fashion_model




