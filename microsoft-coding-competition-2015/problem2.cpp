#include <string>
#include <iostream>
#include <sstream>
#include <stdlib.h>

int main(int argc, char const *argv[])
{

  std::string line;
  while (std::getline (std::cin,line))
  {
    std::stringstream ss(line);
    int old = 0;
    int current = 0;
    int cookie;
    ss >> cookie;
    if (cookie == 5280)
    {
      break;
    }
    while (ss)
    {
      ss >> current;
      int diff = abs(cookie - current) - abs(cookie - old);
      if (current == cookie)
      {
        printf("Moving from %d to %d: found it!\n",old, current);
        break;
      }
      else if(diff == 0)
      {
        printf("Moving from %d to %d: same.\n",old, current);
      }
      else if (diff > 0)
      {
        printf("Moving from %d to %d: colder.\n",old, current);
      }
      else
      {
        printf("Moving from %d to %d: warmer.\n",old, current);
      }
      old = current;
    }
    std::cout << std::endl;
  }
  return 0;
}
