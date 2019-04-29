//https://stackoverflow.com/questions/36730711/find-a-subset-with-sum-within-a-range

#include <bits/stdc++.h>
using namespace std;

int main(){
  int T, N;
  cin >> T >> N;

  vector<int> arr;
  for(int i = 0; i < N; i++){
    int n; cin >> n;
    arr.push_back(n);
  }

  bool dp[N][T+1];
  for(int i = 0; i < T+1; i++) dp[0][i] = false;
  for(int i = 0; i < N; i++) dp[i][0] = true;
  dp[0][arr[0]] = true;
  for(int i = 1; i < N; i++){
    for(int j = 0; j < T+1; j++){
      dp[i][j] = (j >= arr[i] && dp[i-1][j-arr[i]]) || dp[i-1][j];
    }
  }

  int tot = 0;
  for(int i = 0; i < N; i++) tot += arr[i];

  int k;
  int l = tot/2, r = T;
  for(int i = l; i <= r; i++){
    if(dp[N-1][i]){
      k = i;
      break;
    }
  }
  set<int> s1;
  for(int i = N-1; i >= 0; i--){
    if(k-arr[i] >= 0 && (i==0 || dp[i-1][k-arr[i]])){
      s1.insert(i);
      //cout << k << " " << i << endl;
      k -= arr[i];
      if(k == 0) break;
    }
  }

  /*
  for(int i = 0; i < N; i++){
    for(int j = 0; j < T; j++) cout << dp[i][j] << " ";
    cout << endl;
  }
  */
  //for(auto it=s1.begin(); it !=s1.end(); ++it) cout << *it << endl;

  int t1 = 0, t2 = 0;
  for(int i = 0; i < N; i++){
    if(s1.find(i) == s1.end()){
      cout << t1 << " ";
      t1 += arr[i];
    }
    else{
      cout << t2 << " ";
      t2 += arr[i];
    }
  }
  cout << endl;
  return 0;
}