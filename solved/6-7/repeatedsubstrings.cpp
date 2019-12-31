#include <bits/stdc++.h>

using namespace std;

#define int long long
template <typename T>
inline T modpow(T base, T exp, T modulus) {
  base %= modulus;
  T result = 1;
  while (exp > 0) {
    if (exp & 1) result = (result * base) % modulus;
    base = (base * base) % modulus;
    exp >>= 1;
  }
  return result;
}

string str;
const int MOD1 = 982451653;
const int MOD2 = 941083981;
const int MOD3 = 735632791; 
const int BASE = 31;
int N;

vector<string> possibleAns;
bool p(int n, bool b) {
  if(b) possibleAns.clear();
  int h1, h2, h3;
  h1 = h2 = h3 = 0;
  unordered_map<int, int> count1;
  unordered_map<int, int> count2;
  unordered_map<int, int> count3;
  for (int i = 0; i < n; i++) {
    h1 = ((h1 * BASE) + str[i] - 'a' + 1) % MOD1;
    h2 = ((h2 * BASE) + str[i] - 'a' + 1) % MOD2;
    h3 = ((h3 * BASE) + str[i] - 'a' + 1) % MOD3;
  }
  count1[h1]++;
  count2[h2]++;
  count3[h3]++;
  int pow1 = modpow(BASE,n-1,MOD1);
  int pow2 = modpow(BASE,n-1,MOD2);
  int pow3 = modpow(BASE,n-1,MOD3);
  for (int i = n; i < N; i++) {
    h1 -= pow1 * (str[i - n] - 'a' + 1) % MOD1;
    h2 -= pow2 * (str[i - n] - 'a' + 1) % MOD2;
    h3 -= pow3 * (str[i - n] - 'a' + 1) % MOD3;
    h1 = (((h1+MOD1) * BASE) + str[i] - 'a' + 1) % MOD1;
    h2 = (((h2+MOD2) * BASE) + str[i] - 'a' + 1) % MOD2;
    h3 = (((h3+MOD3) * BASE) + str[i] - 'a' + 1) % MOD3;
    count1[h1]++;
    count2[h2]++;
    count3[h3]++;
    if((count1[h1] >= 2) && (count2[h2] >= 2) && (count3[h3] >= 2)){
      if(b) possibleAns.push_back(str.substr(i-n+1, n));
      else return true;
    }
  }
  return false;
}

signed main() {
  cin >> str;
  N = str.size();

  int lo = 1;
  int hi = N;
  while (lo < hi){
    int mid = (lo+hi)/2;
    if(p(mid, false)){
      lo = mid+1;
    } else{
      hi = mid;
    }
  }

  /*
     cout << lo - 1 << endl;
     for(int i = 1; i < N; i++) {
     cout << p(i, false) << " ";
     }
     cout << endl;
   */
  p(lo-1, true);
  sort(possibleAns.begin(),possibleAns.end());
  /*
  for(string s : possibleAns){
    cout << s << " ";
    }
    cout << endl;
    */
  cout << possibleAns[0] << endl;
  return 0;
}
