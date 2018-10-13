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

#ifndef Initialization
KerasModel m("model.dumped", false);

#define Initialization

#endif


int yuvcnn(int width, int height, unsigned char *yuvbuff, int Dwidth, int Dheight) {
    if (Dwidth > width) || (Dheight > height)    return -1;

    DataChunk *sample = new DataChunk2D();

    sample->read_from_file(width, height, yuvbuff, Dwidth, Dheight);

    std::vector<float> response = m.compute_output(sample);

    delete sample;
    
    response[0]>response[1] ? return 0 : return 1;
}
