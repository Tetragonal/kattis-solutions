
#include <bits/stdc++.h>
#define SIZE 10001
using namespace std;
int main() {
  int g;
  cin >> g;

  bool** hasSprinkler = new bool*[SIZE];
  for(int i = 0; i < SIZE; i++) 
    hasSprinkler[i] = new bool[SIZE];
  
  vector<int> goblinX;
  vector<int> goblinY;
  for(int i = 0; i < g; i++){
    int x,y;
    cin >> x >> y;
    goblinX.push_back(x);
    goblinY.push_back(y);
  }

  int m;
  cin >> m;
  for(int i = 0; i < m; i++){
    int x,y,r;
    cin >> x >> y >> r;
    for(int j = -r; j <= r; j++) {
      for(int k = -r; k <= r; k++) {
        if((j*j)+(k*k)<=(r*r) && x+j >= 0 && y+k >= 0 && x+j<SIZE && y+k<SIZE) {
          hasSprinkler[x+j][y+k] = true;
        }
      }
    }
  }

  int count = g;
  for(int i = 0; i < g; i++){
    int x = goblinX[i];
    int y = goblinY[i];
    if(hasSprinkler[x][y]) count--;
  }
  cout << count << endl;
  return 0;
}

