#include <string>
#include <iostream>
#include <sstream>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
  std::string vowels = "aiyeou";
  std::string vowelCaps = "AIYEOU";
  std::string cons = "bkxznhdcwgpvjqtsrlmf";
  std::string consCaps = "BKXZNHDCWGPVJQTSRLMF";
  std::string line;
  while (std::getline (std::cin,line))
  {
    std::stringstream ss(line);
    std::string output;
    for (int i=0; i < line.size(); ++i)
    {
      std::size_t vowel_i = vowels.find(line[i]);
      std::size_t cons_i = cons.find(line[i]);
      std::size_t vowelC_i = vowelCaps.find(line[i]);
      std::size_t consC_i = consCaps.find(line[i]);

      if (vowel_i != std::string::npos)
      {
        output += vowels[(vowel_i + 3) % 6];
      }
      else if (cons_i != std::string::npos)
      {
        output += cons[(cons_i + 10) % 20];
      }
      else if (vowelC_i != std::string::npos)
      {
        output += vowelCaps[(vowelC_i + 3) % 6];
      }
      else if (consC_i != std::string::npos)
      {
        output += consCaps[(consC_i + 10) % 20];
      }
      else
      {
        output += line[i];
      }
    }
    std::cout << output << std::endl;
  }
  return 0;
}
