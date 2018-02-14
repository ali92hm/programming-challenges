#include <string>
#include <iostream>
#include <sstream>
#include <stdlib.h>
#include <vector>
#include <stdio.h>

int main(int argc, char const *argv[])
{
  std::string line;
    int case_num = 0;
  while (std::getline (std::cin,line))
  {
    ++case_num;

    std::stringstream ss(line);
    int n, x, y, z = 0;
    ss >> n;
    ss >> x;
    ss >> y;
    ss >> z;
    std::getline (std::cin,line);
    std::stringstream ss1(line);

    std::vector<std::string> input_arr;
    while (ss1)
    {
      std::string a;
      ss1 >> a;
      if (a == "0")
        break;
      if (!a.empty())
        input_arr.push_back(a);
    }
    std::vector<int> turns(3, 0);
    int index = 0;
    if (input_arr.size() > 0)
    {
      for (int i = 0; i < input_arr.size() - 2; i+=2)
      {
        turns[index] += std::stoi(input_arr[i+1]);
        if (input_arr[i] != input_arr[i+2])
        {
          index++;
        }
      }
      turns[index] += std::stoi(input_arr[input_arr.size() - 2]);
      if (turns[0] < n || turns[2] > n)
      {
        printf("Case %d: Closed\n", case_num);
      }
      else if (((-turns[0]) % n + n) % n == x && ((turns[1] - turns[0]) % n + n) % n == y && ((turns[1] - turns[2] - turns[0]) % n + n) % n == z)
      {
        printf("Case %d: Open\n", case_num);
      }
      else
      {
        printf("Case %d: Closed\n", case_num);
      }
    }
  }
  return 0;
}
