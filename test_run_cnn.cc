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


int main(int argc, char *argv[]) {
  string dumped_cnn = argv[1];
  char *InpDir = argv[2];
  string response_file = argv[3];
  
  DIR *dir;
  struct dirent *ent;

  dir = opendir(InpDir);
  ofstream fout(response_file);
  KerasModel m(dumped_cnn, false);
  string inpdir(InpDir);

  while ((ent = readdir (dir)) != NULL) {
    system("clear");
    char * tmp_data = ent->d_name;
    
    string input_file(tmp_data);
    if(input_file == "." || input_file == "..")  continue;

    string input_data = inpdir + "/" + input_file;
    cout << "FileName: " << input_data << endl;
    // Input data sample
    DataChunk *sample = new DataChunk2D();
    //cout << sizeof(sample) << endl;
    sample->read_from_file(input_data);
    //cout << sizeof(sample) << endl;        
    // Construct network
    std::vector<float> response = m.compute_output(sample);

    // clean sample
    delete sample;
    // save response into file
    fout << input_file << "\t\t";
    response[0]>response[1] ? fout << "0" << endl: fout << "1" << endl;
  }
  system("clear");
  cout << "Ctest run succeed, the output file has been saved at  " << response_file  << endl;
  fout.close();
  closedir(dir);
  return 0;
}
