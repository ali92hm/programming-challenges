#include <string>
#include <iostream>
#include <sstream>
#include <stdlib.h>
#include <vector>
#include <stdio.h>
#include <algorithm>

std::string encrypt(std::string key, std::string cipher) {
  std::string output = "";
  for (int i = 0; i < key.size(); ++i)
  {
    output += cipher[key[i] - 65];
  }
  return output;
}

std::string decrypt(std::string key, std::string cipher) {
  std::string output = "";
  std::string ab = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  for (int i = 0; i < key.size(); ++i)
  {
    int ord = cipher.find(key[i]);
    output += ab[ord];
  }
  return output;
}

int main(int argc, char const *argv[])
{
  std::string line;
  int case_line= 1;
  while (std::getline (std::cin,line))
  {
    std::stringstream ss(line);
    std::string rest;
    int line_num;
    ss >> line_num;
    ss >> rest;
    std::string input;
    std::vector<std::string> keyspace;
    for (int i = 0 ; i < line_num; ++i) {
      std::getline (std::cin,input);
      keyspace.push_back(decrypt(input, rest));
    }
    if (keyspace.size() != 0) {
      std::sort(keyspace.begin(), keyspace.end());
      std::cout << "year " << case_line << std::endl;
      for (int i = 0; i < keyspace.size(); ++i)
      {
        std::cout << encrypt(keyspace[i], rest) << std::endl;
      }
      ++case_line;
    }
  }
  return 0;
}
