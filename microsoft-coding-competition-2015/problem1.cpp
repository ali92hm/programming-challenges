#include <iostream>

int main(int argc, char const *argv[])
{
  using namespace std;
  int num_inputs;
  cin >> num_inputs;

  for (int i = 0; i < num_inputs; ++i)
  {
    int num_plays;
    cin >> num_plays;
    int win = 0;
    for (int j = 0; j < num_plays; j++)
    {
      char player_1, player_2;
      char tmp;
      cin >> player_1;
      cin >> player_2;
      if (player_1 == player_2)
      {
        continue;
      }
      if ((player_1 == 'P' && player_2 == 'R')
          || (player_1 == 'S' && player_2 == 'P')
          || (player_1 == 'R' && player_2 == 'S'))
      {
        win += 1;
        continue;
      }
      if ((player_2 == 'P' && player_1 == 'R')
          || (player_2 == 'S' && player_1 == 'P')
          || (player_2 == 'R' && player_1 == 'S'))
      {
        win -= 1;
        continue;
      }
    }
    if (win == 0)
    {
      cout << "TIE" << endl;
    }
    else if (win > 0)
    {
      cout << "Player 1" << endl;
    }
    else
    {
      cout << "Player 2" << endl;
    }
  }

  return 0;
}
