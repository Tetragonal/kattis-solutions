#include <bits/stdc++.h>
using namespace std;

int w[21], h[21], x[21], y[21];
int n;
int score = 0;
int maxScore = 0;
bool subset[21];

bool intersect[21][21];

void solve(int curr) {
  for(int i = 0; i < curr-1; i++){
    if(subset[i] && intersect[i][curr-1]) return;
  }
  if(score > maxScore) maxScore = score;

  for(int i = curr; i < n; i++){
    score += w[i]*h[i];
    subset[i] = true;
    solve(i+1);
    score -= w[i]*h[i];
    subset[i] = false;
  }
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  while(true){
    cin >> n;
    if(n == 0) return 0;

    score = maxScore = 0;
    for(int i = 0; i < n; i++){
      cin >> w[i] >> h[i] >> x[i] >> y[i];
    }

    for(int i = 0; i < n; i++){
      for(int j = 0; j < n; j++){
        bool xIntersect = (x[i] >= x[j] && x[i] < x[j]+w[j]) ||
                          (x[j] >= x[i] && x[j] < x[i]+w[i]);
        bool yIntersect = (y[i] >= y[j] && y[i] < y[j]+h[j]) ||
                          (y[j] >= y[i] && y[j] < y[i]+h[i]);
        intersect[i][j] = xIntersect && yIntersect;
      }
    }

    solve(0);
    cout << maxScore << endl;
  }
}
