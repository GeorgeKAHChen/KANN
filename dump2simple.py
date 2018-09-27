####################################################
#      
#       keras2cpp
#       FileName: dump_to_simple_cpp.py
#       Copyright(c) by pplonski, all right reserved
#       Github: https://github.com/pplonski/keras2cpp
#
####################################################
#       
#       Changed by KazukiAmakawa
#       For the program of KANN
#       Github: https://github.com/KazukiAmakawa/KANN
#
####################################################

from keras.models import Sequential, model_from_json
import json
import Setting
import Init
import os

model = model_from_json(open(Setting.ModelFolder + "/model.json").read())
model.load_weights(Setting.ModelFolder + "/model.h5")
model.compile(loss='categorical_crossentropy', optimizer='adadelta')
arch = json.loads(open(Setting.ModelFolder + "/model.json").read())

with open(Setting.ModelFolder + "/model.dumped", 'w') as fout:
    fout.write('layers ' + str(len(model.layers)) + '\n')

    layers = []
    for ind, l in enumerate(arch["config"]):
        fout.write('layer ' + str(ind) + ' ' + l['class_name'] + '\n')

        layers += [l['class_name']]
        if l['class_name'] == 'Convolution2D':
            W = model.layers[ind].get_weights()[0]
            fout.write(str(W.shape[0]) + ' ' + str(W.shape[1]) + ' ' + str(W.shape[2]) + ' ' + str(W.shape[3]) + ' ' + l['config']['border_mode'] + '\n')

            for i in range(W.shape[0]):
                for j in range(W.shape[1]):
                    for k in range(W.shape[2]):
                        fout.write(str(W[i,j,k]) + '\n')
            fout.write(str(model.layers[ind].get_weights()[1]) + '\n')

        if l['class_name'] == 'Activation':
            fout.write(l['config']['activation'] + '\n')
        if l['class_name'] == 'MaxPooling2D':
            fout.write(str(l['config']['pool_size'][0]) + ' ' + str(l['config']['pool_size'][1]) + '\n')
        if l['class_name'] == 'Dense':
            W = model.layers[ind].get_weights()[0]
            fout.write(str(W.shape[0]) + ' ' + str(W.shape[1]) + '\n')


            for w in W:
                fout.write(str(w) + '\n')
            fout.write(str(model.layers[ind].get_weights()[1]) + '\n')


if os.path.exists("tmp"):
    os.system("rm -rf tmp")
Init.BuildFile("tmp")
String = ""
String += "ModelFolder='" + str(Setting.ModelFolder) + "'\n"
String += "TestFolder='" + str(Setting.TestFolder) + "'\n"
String += "OutputFolder='" + str(Setting.OutputFolder) + "'\n"
File = open("tmp", "w")
File.write(String)
File.close()



