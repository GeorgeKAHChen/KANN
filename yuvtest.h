//####################################################
//
//       keras2cpp
//       FileName: test_run_cnn.cc
//       Copyright(c) by pplonski, all right reserved
//       Github: https://github.com/pplonski/keras2cpp
//
//####################################################

#include "keras_model.h"

#include <iostream>
#include <string>

#include <cstring>
#include <dirent.h>   
#include <stdlib.h>  
#include <unistd.h>

using namespace std;
using namespace keras;

KerasModel m("model.dumped", false);

int yuvcnn(int width, int height, unsigned char *yuvbuff) { 
    int i, j;
    vector< vector<float> > Image;

    //downsample problem
    for (i = 0; i < width; i ++){
        vector<float> tmp;
        for (j = 0; j < height; j ++){
           tmp.push_back((float)yuvbuff[i * height + j] / 255);
        }
        Image.push_back(tmp);
        delete tmp;
    }
    
    DataChunk *sample = new DataChunk2D();
    
    
    std::vector<float> response = m.compute_output(sample);

    delete sample;
    response[0]>response[1] ? return 0 : return 1;
}
