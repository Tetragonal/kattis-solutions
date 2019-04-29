#include <bits/stdc++.h>
using namespace std;

const int SIZE = 100005;
//-----------------------------------------------------------------------------
//https://en.wikipedia.org/wiki/Fenwick_tree
#define LSB(i) ((i) & -(i)) // zeroes all the bits except the least significant one

int A[2*SIZE];
int LOC[SIZE];

int sum(int i) // Returns the sum from index 1 to i
{
    int sum = 0;
    while (i > 0) 
        sum += A[i], i -= LSB(i);
    return sum;
}
 
void add(int i, int k) // Adds k to element with index i
{
    while (i < 2*SIZE) 
        A[i] += k, i += LSB(i);
}
//-----------------------------------------------------------------------------

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  
  int N;
  cin >> N;

  for(int n = 0; n < N; n++){
    memset(A, 0, sizeof(A));
    memset(LOC, 0, sizeof(LOC));
    int m, r;
    cin >> m >> r;

    for(int i = 1; i <= m; i++){
      add(SIZE+i, 1);
      LOC[i] = SIZE+i;
    }

    int in;
    for(int i = 0; i < r; i++){
      cin >> in;
      cout << sum(LOC[in]-1) << " ";
      add(LOC[in], -1);
      add(SIZE-i, 1);
      LOC[in] = SIZE-i;
    }
    cout << endl;
  }

  return 0;
}
