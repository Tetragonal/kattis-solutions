#include <bits/stdc++.h>

using namespace std;

int main() {
  long long wb[8][8] = {{3, 2, 1, 1, 2, 1, 1, 1},
                  {2, 0, 1, 0, 1, 0, 1, 0},
                  {1, 1, 0, 0, 1, 1, 0, 0},
                  {1, 0, 0, 0, 1, 0, 0, 0},
                  {2, 1, 1, 1, 0, 0, 0, 0},
                  {1, 0, 1, 0, 0, 0, 0, 0},
                  {1, 1, 0, 0, 0, 0, 0, 0},
                  {1, 0, 0, 0, 0, 0, 0, 0}};

  long long dp[25][8] = {};
  int flags[30] = {};

  int n, m;
  double x, y;

  cin >> n >> m;
  for (int i = 0; i < m; i++) {
    cin >> x >> y;

    flags[(int) x + 1] |= 1 << (int) y;
    //flags[(int) y + 1] |= 1 << (int) x;
  }
  
  /*cout << "Flags: ";
  for (int i = 0; i <= n; i++) {
    cout << flags[i] << ' ';
  }
  cout << endl;
*/
  dp[0][0] = 1;
  for (int i = 1; i <= n; i++) {
    for (int k = 0; k < 8; k++) {
      // k outshape, j inshape
      //cout << "Test: " << flags[i + 1] << ' ' << k << ' ' << (flags[i + 1] & k) << endl;
      if ((flags[i + 1] & k) != 0) {
//        cout << "Test, " << i << ' ' << k << endl;
        continue;
      }

      for (int j = 0; j < 8; j++) {
        dp[i][k] += wb[j | flags[i]][k] * dp[i - 1][j];
      }
    }
  }
 /*  
  for (int i = 0; i <= n; i++) {
    for (int j = 0; j < 8; j++) {
      cout << dp[i][j] << ' ';
    }
    cout << endl;
  }
*/
  cout << dp[n][0] << endl;
}

