#include <bits/stdc++.h>
using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  vector<string> lines;
  string line;
  
  int C, N;
  while (cin >> C){
    cin >> N;
    vector<int> arr0(N);
    vector<int> arr1(N);
    for(int i = 0; i < N; i++){
      cin >> arr0[i];
      cin >> arr1[i];
    }
    vector<int> dp(C+1);
    vector<vector<int>> dp2;

    vector<int> tmp(C+1);
    for(int i = 0; i < C+1; i++){
      tmp[i] = -1;
    }
    dp2.push_back(tmp);
    for(int i = 0; i < N; i++) {
      vector<int> dp2New;
      vector<int> tmp;
      for(int c = C; c >= arr1[i]; c--) {
        int curr = dp[c-arr1[i]] + arr0[i];
        if(curr > dp[c]){
          dp[c] = curr;
          tmp.push_back(c-arr1[i]);
        } else {
          tmp.push_back(c);
        }
      }
      for(int j = 0; j < min(C+1, arr1[i]); j++){
        dp2New.push_back(j);
      }
      for(int j = tmp.size()-1; j >= 0; j--) {
        dp2New.push_back(tmp[j]);
      }
      dp2.push_back(dp2New);
    }
    
    vector<int> indices;
    int c = C;
    int x = 1;
    while(c) {
      while (dp2[N-x+1][c] == c) {
        x += 1;
      }
      int nextC = dp2[N-x+1][c];
      if(nextC == -1) break;
      indices.push_back(N-x);
      x += 1;
      c = nextC;
    }
    cout << indices.size() << endl;
    for(int i = 0; i < indices.size(); i++) {
      cout << indices[i] << " ";
    }
    cout << endl;
  }

  return 0;
}
